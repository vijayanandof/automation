# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:46:55 2018

@author: vijayana
"""
from flask import Flask, session


from bs4 import BeautifulSoup
import codecs
import re

listt=[]


app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')


def index():
    
    f=codecs.open("spell_check_result.html", 'r')
    htmldata = f.read()
    
    print ("----------------------------")
    
    
    soup = BeautifulSoup(htmldata,"lxml")
    table = soup.find("table")
    counter = 1
    final_list=[]
    htmlstring="<html lang='en'><head><title>SpellCheck</title><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'><script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>"
    
    for row in table.find_all("tr")[1:]:
      col = row.find_all("td")
      mistakes = col[0].text
      
      lst = re.findall(r'"([^"]*)"', mistakes)
      
      first_quote=lst[0]
      
      final_list.append(first_quote)
      counter=counter +1
      
     # print (first_quote)
      
    print (counter)
    print (len(list(set(final_list)))) 
    
    listt=list(set(final_list))
    
    htmlstring += "<h1 align='center'>Total Spelling Errors::"+str(counter)+"<br>  Length of remove-repeat list:"+str(len(list(set(final_list))))+" </h1><br>"
    htmlstring+="<div class='container'><table class='table table-striped table-bordered table-hover table-condensed'><thead><tr><th>S.No</th><th>Words</th><th>Delete</th></tr></thead><tbody>"
    count =0
    
    listt.sort()
    
    for item in listt:
        count = count +1
        htmlstring+="<tr><td>"+str(count)+"</td><td>"+item+"</td>"+"<td><button type='button' class='btn'  >X</button></td></tr>"
    
    session['data'] = listt
    return htmlstring

@app.route('/remove/<remove>')

def test(remove):
    
    datalist=""
    removestring = remove
    data = session['data']
    
    data.remove(removestring)
    
    session['data']=data
    
    for item in data:    
     datalist+=""+item+"<br>"+""

    return datalist
def err():
     return "<h1>Error</h1>"

#remove and store in session again and again till file is generated!

if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1',port=5000)