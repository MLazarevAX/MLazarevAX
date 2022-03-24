import sqlite3

def sqlite_create():
    bd = sqlite3.connect("2048.sqlite")
    cur = bd.cursor()

    cur.execute("""
    create table if not exists RECORDS(
        name text,
        score integer
    )""")
    cur.close()

def sqlite_sort():
    bd = sqlite3.connect("2048.sqlite")
    cur = bd.cursor()

    cur.execute('''
    SELECT name gamer, max(score) score FROM RECORDS
    GROUP by name
    ORDER BY score DESC
    limit 3
    ''')
    result = cur.fetchall()
    cur.close()
    return result

def sqlite_insert(score1, player_name):
    bd = sqlite3.connect("2048.sqlite")
    cur = bd.cursor()
    score1 = int(score1)
    # Insert a row of data
    cur.execute("INSERT INTO RECORDS VALUES (?, ?)", (player_name, score1))
    # Save (commit) the changes
    bd.commit()
    cur.close()