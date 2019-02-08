import requests
import bs4
from bs4 import BeautifulSoup
import re
from validator_collection import checkers

def start(keyword):
    
    i=0
    j=1
    xyz=[]
    while i<50:
        offset=j*10-9
        j=j+1
        x=keyword+'&b='+str(offset)
        print(x)
        res = requests.get('https://in.search.yahoo.com/search?p='+x)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        links = soup.select('a > href')
        cleanr = re.compile('<.*?>')
        
        n=len(links)
        print(n)
        for k in range(n):
            cleantext = re.sub(cleanr, '', str(links[k]))
            k+=1
            s=cleantext[:4]
            
            if(s!='http'):
                cleantext='https://'+cleantext
            
            if(not checkers.is_url(cleantext)):
                continue
            
            i+=1
            #link =cleantext
            print(cleantext)
            xyz.append(cleantext)
            
    file2= open("C:\\Users\\DELL\\Desktop\\xyz.txt", 'a')
    for m in range(50):
        file2.write(xyz[m]+"\n")
              

start("swine flu vaccine")