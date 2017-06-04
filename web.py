
from urllib.request import urlopen
my_address = "https://realpython.com/practice/aphrodite.html"
html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')
start_tag = "<title>"
end_tag = "</title>"
start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)
print(html_text[start_index:end_index])