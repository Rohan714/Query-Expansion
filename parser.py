import requests
import bs4
from bs4 import BeautifulSoup

def parseLink(query, adress, SE):
    file=open(adress,'r')
    while(True):
        link = file.readline()
        if (link==""):
            break
        l=len(link)
        link=link[:l-1]
        print(link)
        x=link[l-4:l-1]
        if(x=="pdf"):
            continue
        try:
            page = requests.get(link)
            soup = BeautifulSoup(page.text,'html.parser')
        except:
            continue
 
        #writing content of each page to a text file
        with open("C:\\Users\\DELL\\Desktop\\Project\\"+SE+"\\paragraph\\"+query+".txt", 'a',encoding="utf-8") as file1:
            for x in soup.find_all('header'):
                file1.write(x.get_text()+"\n")
            for x in soup.find_all('p'):
                file1.write(x.get_text()+"\n")

              
file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
#i=0
while(True):
    query=file.readline()
    
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    #address="C:\\Users\\DELL\\Desktop\\Project\\Google\\QueryLinks\\"+query+".txt"
    #parseLink(query, address, "Google")
    
    address="C:\\Users\\DELL\\Desktop\\Project\\Bing\\QueryLinks\\"+query+".txt"
    parseLink(query, address, "Bing")
    
    
    
    
