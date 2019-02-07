from bs4 import BeautifulSoup, Comment
import requests

def el_is_visible(element):
    try:
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True
    except:
        return False

def get_visible_text(soup):
    try:
        text = soup.findAll(text=True)
        text = ' '.join([t.strip() for t in text if el_is_visible(t)])
        return text
    except:
        return ''
  

def parseLink(query, adress, SE):
    file=open(adress,'r')
    while(True):
        link = file.readline()
        if (link==""):
            break
        l=len(link)
        link=link[:l-1]
        print(link)
        if(link.find(".pdf")!=-1):
            continue
        x=link[l-4:l-1]
        if(x=="pdf"):
            continue
        try:
            headers={
                    'User-Agent':'Pankaj',
                    'From':'pcnitp@gmail.com'}
            #page = requests.get(link)
            page=requests.get(link,headers=headers)
            soup = BeautifulSoup(page.text,'html.parser')
        except:
            continue

        text=get_visible_text(soup)
        #writing content of each page to a text file
        file1 =open("C:\\Users\\DELL\\Desktop\\Project\\"+SE+"\\paragraph1\\"+query+".txt", 'a',encoding="utf-8")
        file1.write(text)
           
                
    
file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
i=0
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
    
    
    
