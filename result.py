# -*- coding: utf-8 -*-
"""
@author: Reggie

This is result.py.
"""

def display(res):
    with open('sortedData.txt','r',encoding='UTF-8') as processed:  
        array= []
        for line in processed:
            start= str(line).find('*')
            end= str(line).find("\\")
            array.append(line[int(start)+1:int(end)])
    for item in (array[0:res]):
        print (item)

# For testing
#display(10)