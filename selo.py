"""from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')"""

"""import os
from selenium import webdriver
# chromedriver = "/Users/adam/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()"""

 # import time

from selenium import webdriver
#import pyscreenshot as ImageGrab
 #import selenium.webdriver.chrome.service as service
browser = webdriver.Firefox()

 #service = service.Service('/path/to/chromedriver')
#service.start()
#capabilities = {'chrome.binary': '/path/to/custom/chrome'}
#driver = webdriver.Remote(service.service_url, capabilities)
browser.get('http://student.vidyamandir.com/')
browser.save_screenshot("screenshot.png")
browser.close()
#time.sleep(5)
#img_landing = ImageGrab.grab()
#plt.imshow(img_landing, cmap='gray', interpolation='bicubic')
#browser.get('http://student.vidyamandir.com/purchasable_course')
#time.sleep(5)
#browser.get('http://student.vidyamandir.com/free_test')
#time.sleep(5)
#plt.imshow(img_free_test, cmap='gray', interpolation='bicubic')
#plt.show()
#print (response)
#time.sleep(5) # Let the user actually see something!

