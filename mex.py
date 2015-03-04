#!/usr/bin/python

import sys

if len(sys.argv) > 1 :
  bitsnoopURL = sys.argv[1]
else :
  print "Err: no input url"
  sys.exit()

import pycurl
from StringIO import StringIO
import BeautifulSoup

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, bitsnoopURL)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()

soup = BeautifulSoup.BeautifulSoup(body)

for li in soup.findAll('li') :
    if 'Full Magnet link:' in str(li) :
        print li.findAll('a')[0]['href']
