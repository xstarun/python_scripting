#! /usr/bin/python 
try:
	print ("Hello World!")
	print ("- From your friendly Python program")

	import time
	import webbrowser
	import http.client
	#import  BeautifulSoup
	import urllib.request
	 #import requests

	#urllib.request.urlopen('http://www.google.com')
	
	page = urllib.request.urlopen("https://www.googhhle.com")
	status = page.getcode() 
	print (status)
except: 	
	



        #as response:
 	#html = response.read()

finally:
 	print (status)
