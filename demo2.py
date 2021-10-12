import sqlite3

conn = sqlite3.connect('demo2.db')
c = conn.cursor()
c.execute('''DROP TABLE Ride''')
c.execute('''CREATE TABLE Ride(
CA         	VARCHAR(10),
UNIT        VARCHAR(10),
SCP         VARCHAR(10),
STATION     VARCHAR(20),
LINENAME	VARCHAR(20),
DIVISION	VARCHAR(5),
DATE		CHAR(10),
TIME 		CHAR(8),
DESC 		VARCHAR(10),
ENTRIES		VARCHAR(10),
EXITS		VARCHAR(10)
)''')
conn.commit()
print('created the table.')
file_data = [i.strip('\n').split(',') for i in open('turnstile_211009.txt')]
c.executemany('INSERT INTO Ride VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', file_data)
conn.commit()
c.execute('''SELECT COUNT(*) FROM Ride''')
print(c.fetchall()[0], 'rows of data imported')
