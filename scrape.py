import urllib
from BeautifulSoup import *
import re

url = "http://python-data.dr-chuck.net/comments_374116.html"

html=urllib.urlopen(url).read()

soup = BeautifulSoup(html)
table = soup('span', { "class" : 'comments'})

#numbers = [d.text.encode('utf-8') for d in table]
#y = map(int, numbers)
#y = sum(y)
#print y

table = str(table)
y = re.findall('[0-9]+', table)
y = map(int, y)
y = sum(y)
print y