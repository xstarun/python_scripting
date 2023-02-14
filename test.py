#import this 
from PIL import Image
import nose
import unittest


import time
import datetime
now = datetime.datetime.now()
from selenium import webdriver
#video_id = input ("youtube_id of video ::")
video_id = "IkzlYyqexB"

class TestAssertSeleniumTitle(unittest.TestCase):
 def setup(self):
  browser = webdriver.Chrome()
  browser.maximize_window()
#Home Page
 def testVideo(self):
  self.browser.get('https://www.youtube.com/watch?v='+video_id+"'")
  time.sleep(10)
  self.assertEqual("Bhang%")
#browser.find_element_by_xpath("//button[@aria-label='Pause']").click()
#video_name = browser.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']")
#print ("video played is "+video_name)
#if  find(video_name) in browser.page_source:

#views = browser.find_element_by_xpath("//span[@class='view-count style-scope yt-view-count-renderer']")

#print("video has following "+views)
 def teardown(self):
  time.sleep(10)
  browser.save_screenshot("vchecktext.png")
  browser.close()
