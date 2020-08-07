# -*- coding: utf-8 -*-
"""
@author: Reggie

This is crawler.py.
"""
import requests
from bs4 import BeautifulSoup

def one(video,num,txt):
    videoList = []
    file = open(txt,"w+", encoding="utf-8") 
    
    for i in range(num): 
        try:
            html = requests.get(video) # connect to the server
            bs = BeautifulSoup(html.text, 'lxml') # manage tags in HTML document
            videoList.append(video)
            
            name = bs.find('title').get_text().strip()
            author = bs.find('a', {"class": "yt-uix-sessionlink spf-link "}).get_text().strip()
            interactionCount = bs.find('meta', {"itemprop": "interactionCount"})['content']
            genre = bs.find('meta', {"itemprop": "genre"})['content']
            like = bs.find('button', {"class": "yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked yt-uix-clickcard-target yt-uix-tooltip"}).get_text().strip()
            dislike = bs.find('button', {"class": "yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked yt-uix-clickcard-target yt-uix-tooltip"}).get_text().strip()
            
            file.write(video+ '\n') 
            file.write(name + '\n')
            file.write(author + '\n')   
            file.write(interactionCount + '\n')
            file.write(genre + '\n') 
            file.write(like + '\n')
            file.write(dislike + '\n' + '\n') 
            
            print("-------------------------------\nVideo collected: \"" + name +"\"\n-------------------------------")
            
            videos = bs.find_all('a', {"class": " content-link spf-link yt-uix-sessionlink spf-link "})
            videoIndex = 0
            
            while video in videoList:
                video = 'https://www.youtube.com' + videos[videoIndex]['href']
                videoIndex = videoIndex+1
        
        except AttributeError:
#            print ("attribute error")
            continue 
        except ValueError:
#            print ("value error")
            pass

#        if bs.find('meta', {"name": "description"}): description = bs.find('meta', {"name": "description"})['content']
#        if bs.find('meta', {"name": "keywords"}): keywords = bs.find('meta', {"name": "keywords"})['content']
#        duration = bs.find('meta', {"itemprop": "duration"})['content']
#        datePublished = bs.find('meta', {"itemprop": "datePublished"})['content']
#        file.write(description + '\n')
#        file.write(keywords + '\n')
#        file.write(str(int(duration[duration.find('T')+1:duration.find('M')])*60 + int(duration[duration.find('M')+1:-1])) + '\n')   # in seconds
#        file.write(datePublished + '\n')             
    
    file.close()

# For testing
#one('https://www.youtube.com/watch?v=4V2V-Rk0Bwk',100)