# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 15:42:07 2018

@author: vijayana
"""

from selenium import webdriver
from bs4 import BeautifulSoup


import PIL.ImageGrab

def work(url, title):
    browser.get(url)
    im = PIL.ImageGrab.grab()     
    im.show() 
    return 

browser = webdriver.Chrome()
browser.get('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=R1THWpigMZiHhwOfpIb4Bw')
            
browser.maximize_window()
inputElement = browser.find_element_by_id("lst-ib")
inputElement.send_keys('Testing')

#inputpassword = browser.find_element_by_id("password")
#inputpassword.send_keys('Test@123')
button = browser.find_element_by_name("btnK").click()

htmlstring = browser.page_source

soup = BeautifulSoup(htmlstring,"lxml")
testing = soup.select(".r > a")


                                                    
for a in testing: 
    print(a.get('href')+"\n")
    print(a.text)
    work(a.get('href'),a.text)


  
