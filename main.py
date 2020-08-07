# -*- coding: utf-8 -*-
"""
@author: Reggie

This is the main file to get started.
"""

from os import path
import crawler, alg, result

def collect(link,num):
    crawlerExist = path.exists("crawler.py")
    if crawlerExist:  
        print ("The system is crawling the data...")
        crawler.one(link,num, "youtubeData.txt")
        print ("Crawled successfully")
    else:
        print ("'crawler.py' does not exist!") 
        
def process(newLink,num):
    algExist = path.exists("alg.py")
    if algExist:
        crawler.one(newLink,1, "targetData.txt")
        alg.cB("youtubeData.txt","targetData.txt") # content-based algorithms 
        print('Processing done.')
    else:
        print ("'alg.py' does not exist!")

def display(res):
    resultExist = path.exists("result.py")
    if resultExist:
        result.display(res) # result display
    else:
        print ("'result.py' does not exist!")

link= str(input('===============================\nWelcome! Please input the link as the search area.\n'))
num= int(input('-------------------------------\nPlease input the number of datasets to crawl?\n'))
collect(link,num)
newLink= str(input('-------------------------------\nPlease input the link to search its similar clips.\n'))
print('-------------------------------\nSystem is processing the data...\n')
process(newLink,num)
res= int(input('-------------------------------\nPlease input the number of recommended videos:\n'))
display(res)
print('exit\n===============================\n')

# Recommendated websites: 
# https://www.youtube.com/watch?v=lJzCsj3aP3k&t=19s
# https://www.youtube.com/watch?v=6gKBV1FVESs