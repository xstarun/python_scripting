from selenium import webdriver
 
driver=webdriver.Firefox()
driver.implicitly_wait(20)
driver.maximize_window()
 
driver.get('http://www.google.com')
 
driver.quit()