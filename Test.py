import re

def correct(query):
    
    add="C:\\Users\\DELL\\Desktop\\Project\\Bing\\paragraph\\"+query+".txt"
    add1="C:\\Users\\DELL\\Desktop\\Project\\Bing\\paragraph1\\"+query+".txt"
    file = open(add,'r',encoding="utf-8")
    file1= open(add1,'a',encoding="utf-8")
    i=0
    s=""
    while(True):
        r=file.readline()
        s+=r
        i+=1
        if(i==100 or r==""):
            i=0
            s=re.sub("[\{(<\[].*?[\>)}\]]", "", s)
            file1.write(s)
            s=""
            
        if(r==""):
            break
            
correct("swine flu vaccine")