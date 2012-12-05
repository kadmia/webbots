#I'm already not liking the pycurl interface
import pycurl

curl = pycurl.Curl()

def get_page(url):
  curl.setopt(pycurl.URL, url)
  curl.perform()

get_page("http://www.schrenk.com/nostarch/webbots/hello_world.html")


import urllib2
for item in urllib2.urlopen("http://www.schrenk.com/nostarch/webbots/hello_world.html"):
  print item
