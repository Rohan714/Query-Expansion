from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def createDict(query,SE):
    file=open("C:\\Users\\DELL\\Desktop\\Project\\"+SE+"\\paraExtended\\"+query+".txt","r",encoding="utf-8")
    word_dict={}
    while (True):
        key=file.readline()
        if not key:
            break
        word=word_tokenize(key)
        if word[0] in stop_words:
            continue
        if key in word_dict:
            word_dict[key]+=1
        else:
            word_dict[key]=1
            
    #sorting in reverse        
    word_dict1=sorted(word_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) 
    
    #print (word_dict)        
    file1=open("C:\\Users\\DELL\\Desktop\\Project\\"+SE+"\\word_dict\\"+query+".txt","w",encoding="utf-8")
    for obj in word_dict1:
        file1.write(obj[0]+str(obj[1])+"\n")
    

#createDict("swine flu vaccine","Bing")

file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    #address="C:\\Users\\DELL\\Desktop\\Project\\Google\\QueryLinks\\"+query+".txt"
    #parseLink(query, address, "Google")
    
    #address="C:\\Users\\DELL\\Desktop\\Project\\Bing\\QueryLinks\\"+query+".txt"
    createDict(query, "Bing")
    



