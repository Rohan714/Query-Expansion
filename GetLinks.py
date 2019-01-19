def googleSearch(query):
    from googlesearch import search 
    query = "swine flu vaccine"
      
    for j in search(query, tld="co.in", num=50, start=0,stop=None, pause=2.0): 
        print(j)
        
#==========================================================
        
def bingSearch(search_term):

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
    file=open("C:\\Users\\DELL\\Desktop\\Project\\bing\\links.txt",'w')
    for v in search_results["webPages"]["value"]:
        #print(v["url"])
        #print(" ")
        file.write(v["url"]+"\n")
        
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
        
bingSearch("swine flu vaccine")

googleSearch("swine flu vaccine")

yahooSearch()
