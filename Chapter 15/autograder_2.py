import sqlite3 as s3


conn = s3.connect('autograder_2.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
print('successfully deleted table Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
print('successfully created table Counts')

fname = input('Enter filename: ')
try :
    fhand = open(fname)
    print(f'Opened file {fname} successfully')
except : quit('FILE_OPEN_FAILURE')


for line in fhand :
    line.rstrip()
    if line.startswith('From: ') :
        content = line.split()
        org = content[1].split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()
        if row == None : cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else : cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()
print('Successfully populated the Counts table')


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr) :
    print(row)


cur.close()
