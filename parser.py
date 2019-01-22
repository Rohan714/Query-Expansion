# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:24:33 2019

@author: Kritesh
"""

import requests
import bs4
from bs4 import BeautifulSoup

def parseLink(query, adress):
    file=open(adress,'r')
    while(True):
        link = file.readline()
        if (link==""):
            break
        l=len(link)
        link=link[:l-1]
        print(link)
        try:
            page = requests.get(link)
            soup = BeautifulSoup(page.text,'html.parser')
        except:
            continue
        #print(soup)  
        #writing content of each page to a text file
        with open("C:\\Users\\kritesh\\Desktop\\Project\\Google\\paragraph\\"+query+".txt", 'a',encoding="utf-8") as file1:
            for x in soup.find_all('header'):
                file1.write(x.get_text()+"\n")
            for x in soup.find_all('p'):
                file1.write(x.get_text()+"\n")

              
file=open("C:\\Users\\kritesh\\Desktop\\Project\\query_lists.txt",'r')
i=0
while(True):
    query=file.readline()
    if(i<2):
        i+=1
        continue
    
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    address="C:\\Users\\kritesh\\Desktop\\Project\\Google\\QueryLinks\\"+query+".txt"
    parseLink(query, address)
