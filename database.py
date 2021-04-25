import sqlite3

# Creates an empty table. If no tables exist, create a default one
def create_list(name="list1"):
    try:
        con = sqlite3.connect("list.db")
        cur = con.cursor()
        
        temp2 = 'CREATE TABLE IF NOT EXISTS ' + name + ' (LIST_NAME TEXT, STATUS TEXT, DESCRIPTION TEXT)'
        cur.execute(temp2)
        con.commit()

        cur.close()
    except:
        print("Unable to create list")

    finally:
        list_all_lists()


def list_all_lists():
    print("Available lists:")
    con = sqlite3.connect("list.db")
    cur = con.cursor()
    cur.execute('SELECT NAME FROM SQLITE_MASTER')
    for a in cur.fetchall():
        print(a)
    cur.close()

def list_all_todo(sub:str = ""):
    counter = 1
    try:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        t = ('%' + sub.upper() + '%',)
        c.execute('SELECT * FROM STOCKS WHERE SYMBOL LIKE ?', t)
        d= c.fetchall()
        conn.close()
    except:
        print("Unable to fetch list")

    if d != []:
        for date, act, stock, quantity, price in d:
            print("[" + str(counter) + "]\t"+ date + '\t' + str(act) + '\t' + str(stock) + '\t' + str(quantity) + '\t' + str(price))
            counter+=1



# cur.execute("INSERT INTO list1 VALUES ('do','complete','es'")
# cur.execute('insert into list1 values("do", "complete", "yes")')

# cur.execute('''CREATE TABLE IF NOT EXISTS list1 (LIST_NAME text, STATUS text, DESCRIPTION text)''')

# con.close()
# cur.execute('SELECT NAME FROM SQLITE_MASTER WHERE NAME = ?',temp)
# print(cur.fetchall())


# list_users()
# list_all("wert")