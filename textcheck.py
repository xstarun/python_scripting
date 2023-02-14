#! /usr/bin/python 
print ("Hello World!")
print ("- From your friendly Python program")

import time
import webbrowser
import http.client
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



url = ["http://learn.vlyop.com","http://stuent.vidyamandir.com"]
hdr = {'User-Agent': 'Mozilla/5.0'}

#for i in url :

response = urllib.request.urlopen()
html = response.read
strhtml = html.decode()
data =findall("%course%",strhtml)
if data>=1 :
	print (data)+"for"+(i)
else:
	print("no such  words in " + i)


