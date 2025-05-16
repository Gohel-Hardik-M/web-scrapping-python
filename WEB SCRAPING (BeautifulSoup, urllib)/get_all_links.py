from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup 

def get_all_links(url):
    try:
         html = urlopen(url)
    except HTTPError as e:
        return None 
    else: 
        try :
             bsObj = BeautifulSoup(html, "html.parser")
             links = bsObj.findAll("a")
        except AttributeError as e:
            return None 
        else :
            return [link.attrs['href'] for link in links]
        

html = get_all_links("https://docs.python.org/3/library/urllib.html")
print(html)  
