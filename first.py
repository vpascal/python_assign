import re

with open('regex_sum_374111.txt', 'r') as f:
    read_data = f.read()
    y = re.findall('[0-9]+', read_data)
    y = map(int, y)
    y = sum(y)
    print y