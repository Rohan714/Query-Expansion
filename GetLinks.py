def googleSearch(query,i):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    name="links"+str(i)+".txt"
    file=open("C:\\Users\\Kritesh\\Desktop\\Project\\Google\\QueryLinks\\"+name,'w')
      
    for j in search(query, tld="co.in", num=50, stop=1, pause=2): 
        file.write(j+"\n")
i=0
file= open("C:\\Users\\Kritesh\\Desktop\\Project\\query_lists.txt", 'r')
while True:
    s=file.readline()
    if(s==""):
        break
    googleSearch(s,i)
    i=i+1
    print(i) 
        
#==========================================================
        
def bingSearch(search_term, i):

    subscription_key = '6726f5f948824c1f8b3a5cd619745b97'
    assert subscription_key
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
    #search_term = "swine flu"
    
    import requests
    
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML","count":"50"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    #print(response)
    #print(search_results)
    name="links"+str(i)+".txt"
    file=open("C:\\Users\\DELL\\Desktop\\Project\\bing\\QueryLinks\\"+name,'w')
    for v in search_results["webPages"]["value"]:
        #print(v["url"])
        #print(" ")
        file.write(v["url"]+"\n")
     
 i=0
file= open("C:\\Users\\Kritesh\\Desktop\\Project\\query_lists.txt", 'r')
while True:
    s=file.readline()
    if(s==""):
        break
    bingSearch(s,i)
    i=i+1
    print(i)
        
#========================================================================
        
def yahooSearch():
    
    import simplejson, urllib
    APP_ID = '5A1rZg48' # Change this to your API key
    SEARCH_BASE = 'http://search.yahooapis.com/ WebSearchService/V1/webSearch'
    
    class YahooSearchError(Exception):
        pass
    
    def search(query, results=20, start=1, **kwargs):
        kwargs.update({
            'appid': APP_ID,
            'query': query,
            'results': results,
            'start': start,
            'output': 'json'
        })
        url = SEARCH_BASE + '?' + urllib.parse.urlencode(kwargs)
        print(url)
        result = simplejson.load(urllib.request.urlopen(url))
        '''if 'Error' in result:
            # An error occurred; raise an exception
            raise YahooSearchError, result['Error']'''
        return result['ResultSet']
    
    info = search('swine flu vaccine')
    results = info['Result']
    for result in results:
        print(result['Url'])
     
#==========================================================================
        
