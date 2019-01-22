import requests
import bs4
from bs4 import BeautifulSoup

def parseLink(query, adress):
    file=open(adress,'r')
    while(True):
        link = file.readline()
        page = requests.get(link)
        soup = BeautifulSoup(page.content,'html.parser')
            
        #writing content of each page to a text file
        with open("C:\\Users\\DELL\\Desktop\\Project\\Google\\paragraph\\"+query+".txt", 'a') as file1:
            for x in soup.find_all('header'):
                file1.write(x.get_text()+"\n")
            for x in soup.find_all('p'):
                file1.write(x.get_text()+"\n")

              
file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
while(True):
    query=file.readline()
    if(query==""):
        break
    
    address="C:\\Users\\DELL\\Desktop\\Project\\Google\\QueryLinks\\"+query+".txt"
    parseLink(query, address)
    
    