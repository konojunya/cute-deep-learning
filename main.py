#coding: utf-8
from service.flickr import flickr
from service.crawler import crawler
import urllib
import os.path
import re
import time

def read_image(actress,url):
  img = urllib.urlopen(url)
  image_path = os.path.basename(url)
  localfile = open("store/"+ str(actress) + "-" + str(image_path), 'wb')
  localfile.write(img.read())
  img.close()
  localfile.close()

def get_from_flickr():
  url_list = []
  f = open("./actressList.txt","r")

  for actress in f:
    actress = str.strip(actress)
    url_list = flickr.get_image(actress, 50)

    for url in url_list:
      read_image(actress,url)
      print str(actress) + "-" + str(url)

  f.close()

def get_from_webpage(url):
  url_list = crawler.get_image_from_matome(url)

  for url in url_list:
    read_image("matome",url)
    print "saving...\t" + url

  for org_file in os.listdir('/Users/kounojunya/dev/hobby/cute/deep-learning/store/'):
    jpg = re.compile("jpg")
    if jpg.search(org_file):
      file_name = re.sub(r'\.jpg\%.*',"",org_file) + ".jpg"
      org_file = "/Users/kounojunya/dev/hobby/cute/deep-learning/store/"+org_file
      file_name = "/Users/kounojunya/dev/hobby/cute/deep-learning/store/"+file_name
      os.rename(org_file,file_name)
    else:
        pass

if __name__ == '__main__':

  # get_from_flickr()

  f = open("./image_list.txt", "r")

  for url in f:
      get_from_webpage(str.strip(url))
      time.sleep(5)
  f.close()
