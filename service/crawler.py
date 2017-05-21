#coding: utf-8
import urllib2
import re
from bs4 import BeautifulSoup
import sys

class Crawler(object):

  def __init__(self):
    self.soup = None

  def get_image_from_matome(self,url):

    image_list = []

    html = urllib2.urlopen(url).read()
    self.soup = BeautifulSoup(html,"html5lib")
    img_elements = self.soup.select("img.MTMItemThumb")
    for el in img_elements:
      image_list.append(el["src"])

    return image_list

crawler = Crawler()