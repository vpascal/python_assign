import urllib
import json

address = raw_input('Enter location: ')
print 'Retrieving', address

uh = urllib.urlopen(address)
data = uh.read()
tree = json.loads(data)


mylist=[]

for item in tree["comments"]:
	mylist.append(item["count"])

mylist=map(int,mylist)
mylist=sum(mylist)
print mylist


