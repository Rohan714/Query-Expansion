def getlinks(query):
    from   selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    browser = webdriver.Firefox()
    #query='swine flu vaccine'
    browser.get('https://duckduckgo.com/html/?q='+query)
    #res = browser.find_element_by_xpath("/html/body/div[2]/div[4]/div[3]/div/div[1]/div[5]/div[12]/a")
    res = browser.find_element_by_css_selector(".btn")
    #res = browser.findElement(By.className("result--more__btn btn btn--full"))
    res.click()
    WebDriverWait(browser,10)
    elems = browser.find_elements_by_xpath("//a[@href]")
    #file=open('/home/pritu/Desktop/queryexpansion/query_links/swine.txt','w')
    i=-1
    lists=[]
    for elem in elems:
        lists.append(elem.get_attribute("href"))

    lists=lists[1:length-1]
    i=-1
    file=open('/home/pritu/Desktop/queryexpansion/query_links/'+query+'.txt','w')
    for x in lists:
        i+=1
        if(i%4!=0):
            continue    
        file.write(x)
        file.write('\n')
    file.close()
    
#getlinks('Marriage or divorce laws')

file1=open('/home/pritu/Desktop/queryexpansion/query_lists.txt','r')
while(True):
    query=file1.readline()
    if(query==""):
        break
    getlinks(query)
