from urllib.request import urlopen   
from urllib.error import HTTPError 
from bs4 import BeautifulSoup 

def getTitle(url):
    try:
        html = urlopen(url)
    
    except HTTPError as e:
        return None
    
    else: 
      try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1 
        
      except AttributeError as e:
          return None
    return title


        
       
