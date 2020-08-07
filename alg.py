# -*- coding: utf-8 -*-
"""
@author: Reggie

This is alg.py.
"""

import operator, re
from difflib import SequenceMatcher
import numpy as py

def cos_sim(vector_a, vector_b):
    vector_a = py.mat(vector_a)
    vector_b = py.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = py.linalg.norm(vector_a) * py.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def cB(txt1, txt2):
    l = 8 
    newList=[] 
    
    # String
    nameList=[]
    authorList=[] 
    genreList=[] 
    
    viewsList=[] # Integer
    
    with open(txt2, 'r', encoding='UTF-8') as target:
        t= []
        for line in target:
            t.append(line)
    nameT= str(t[1])
    authorT= str(t[2])
    genreT= str(t[4])
    viewsT= float(re.sub("\D", "", t[3]))
    likesT= float(re.sub("\D", "", t[5]))
    dislikes= float(re.sub("\D", "", t[6]))
    ratingT= (likesT+1)/(dislikes+1)
    
    target.close()

    with open(txt1,'r',encoding='UTF-8') as raw:  
        array= []
        newNum= -1
        for line in raw:
            array.append(line)
            newNum= newNum+1
    
    raw.close()
    
    for i in range (int((float(newNum)/8))):
        link= array[l*i]
                
        # String
        name= str(array[l*i+1])
        nameList.append(name)
        nameRatio= (similar(nameT,nameList[i]))

        author= str(array[l*i+2])
        authorList.append(author)
        authorRatio= (similar(authorT,authorList[i]))
    
        genre= str(array[l*i+4])
        genreList.append(genre)
        genreRatio= (similar(genreT,genreList[i]))
                
        # Integer
        views= float(re.sub("\D", "", array[l*i+3]))
        viewsList.append(views)
        viewsRatio= cos_sim(viewsT,views)
        
        likes= float(re.sub("\D", "", array[l*i+5]))
        dislikes= float(re.sub("\D", "", array[l*i+6]))    
        rating= (likes+1)/(dislikes+1)
        ratingRatio= cos_sim(ratingT,rating)
        #function
                     
        sim= cos_sim(viewsT,viewsList[i])* nameRatio* authorRatio* genreRatio* ratingRatio* viewsRatio
        rec= sim # ######
        newList.append([rec, "*"+link])
        
    sorted(newList, key= operator.itemgetter(0))
    file = open("sortedData.txt","w+", encoding="utf-8") 
    for item in newList:
        file.write(str(item)+"\n")
    file.close()

# For testing
#cB("youtubeData.txt","targetData.txt")