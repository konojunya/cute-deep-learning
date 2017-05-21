#coding: utf-8
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import json
import sys
import urllib2

class Flickr(object):

  def __init__(self):
    self.apikey = "c4a7c50d154924087d7cb1f3390ce339"

  def get_image(self,query, N):

    NUM_OF_PHOTO = str(N)
    option = '&sort=relevance&privacy_filter=1&content_type=1&per_page='+ NUM_OF_PHOTO +'&format=json&nojsoncallback=1'
    url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key='+ self.apikey + option

    register_openers()
    datagen, headers = multipart_encode({'text': query})
    request = urllib2.Request(url,datagen, headers)
    response = urllib2.urlopen(request)
    res_dat = response.read()

    url_list = []
    template_url = 'https://farm%s.staticflickr.com/%s/%s_%s.jpg'
    for i in json.loads(res_dat)['photos']['photo']:
        img_url = template_url % (i['farm'],i['server'],i['id'],i['secret'])
        url_list.append(img_url)

    return url_list

flickr = Flickr()