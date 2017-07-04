import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

a = "vlad"
org = "lena"

cur.executescript('''
DROP TABLE IF EXISTS test;

CREATE TABLE test (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

''')



cur.execute("Insert into test(name) values (?)",(a,))

cur.execute('SELECT name FROM test WHERE name = ? ', (org, ))
row = cur.fetchone()
print(row)

conn.commit()
