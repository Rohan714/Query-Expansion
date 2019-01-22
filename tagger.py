import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def postagger(name, adress, SE):  
    
    file = open(adress,'r', encoding="utf-8")
    words=[]
    query_tagged = []
    jk=0
    while (True):
        query=file.readline()
        if query=="":
            break
        text = nltk.word_tokenize(query)   
        list_tagged =nltk.pos_tag(text)

        r=""
        for obj in list_tagged:
            r = r + obj[0] + "_" + obj[1] + " "
            
        query_tagged.append(str)
        
        i=0
        while i<len(list_tagged):
            cur = list_tagged[i][1][0]
            wr = []
            while i<len(list_tagged) and list_tagged[i][1]=="CD":
                wr.append(list_tagged[i][0])
                i=i+1
            if i>=len(list_tagged) or list_tagged[i][1][0] not in ('N','J','V'):
                for j in range(len(wr)):
                    strt = ""
                    for k in range(j,len(wr)):
                        strt = strt + wr[k]
                        #print(strt)
                        words.append(strt)
                        strt = strt + " "
                    i=i+1
                    continue
            else:
                cur = list_tagged[i][1][0]
            if cur not in ('N','J','V'):
                i=i+1
                continue
            while i<len(list_tagged) and (cur == list_tagged[i][1][0] or list_tagged[i][1]=="CD"):
                wr.append(list_tagged[i][0])
                i=i+1
 
            for j in range(len(wr)):
                strt = ""
                for k in range(j,len(wr)):
                    strt = strt + wr[k]
                    words.append(strt)
                    strt = strt + " "
        print(jk)
        jk+=1
                    
    with open("C:\\Users\\DELL\\Desktop\\Project\\"+SE+"\\paraExtended\\"+name+".txt",'a',encoding="utf-8") as filehandle:
        for i in words:
            filehandle.write('%s\n' % i)

    with open("C:\\Users\\DELL\\Desktop\\Project\\"+SE+"\\paraTagged\\"+name+".txt",'a',encoding="utf-8") as filehandle:
        for i in query_tagged:
            filehandle.write('%s\n' % i)
    
query="swine flu vaccine"
address="C:\\Users\\DELL\\Desktop\\Project\\Bing\\paragraph\\"+query+".txt"
postagger("swine flu vaccine", address, "Bing")   
file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    address="C:\\Users\\DELL\\Desktop\\Project\\Bing\\paragraph\\"+query+".txt"
    postagger(query, address, "Bing")
    


