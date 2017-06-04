import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Alisdair.html'
position = 18
count = 7
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(0,count):
	for tag in tags[position-1:position]:
		print tag.get('href', None)
	    	temp = tag.get('href', None)
	    	html = urllib.urlopen(temp).read()
	    	soup = BeautifulSoup(html)
	    	tags = soup('a')
	    