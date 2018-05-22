# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:09:22 2018

@author: vijayana
"""

import tkinter

r = tkinter.Tk()
text = r.clipboard_get()
print(text)
r.withdraw()
r.update()
r.clipboard_append("I've Changed it")
r.destroy()

