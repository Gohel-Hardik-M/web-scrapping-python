from urllib import urlopen 
from bs4 import BeautifulSoup 
import re
from urllib.error import HTTPError

def get_all_jpg_images(url):
    try:
         html = urlopen(url)
    except HTTPError as e :
        return None
    else :
        try:
            bsObj = BeautifulSoup(html)
            images = bsObj.findAll({"img",re.compile("\.\.\/img/gifts/img.*\.jpg")})
        
        except AttributeError as e:
            return None
        else : 
            return [image["src"]  for image in images] 

