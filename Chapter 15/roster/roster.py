import json
import sqlite3


conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()


cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER
    );
''')


fname = input("filename: ")
if (len(fname) < 1) : fname = "roster_data.json"
json_file = open(fname).read()

roster_list = json.loads(json_file)
for roster in roster_list :
    user_name = roster[0]
    course_title = roster[1]
    role = roster[2]

    cur.execute('INSERT OR IGNORE INTO User ( name ) VALUES ( ? )', ( user_name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', ( user_name, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course ( title ) VALUES ( ? )', ( course_title, ))
    cur.execute('SELECT id FROM Course WHERE title = ? ', ( course_title, ))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member ( user_id, course_id, role ) VALUES ( ?, ?, ? )', ( user_id, course_id, role ))

conn.commit()