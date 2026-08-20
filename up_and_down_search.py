import os
import sqlite3
def get_change_data(date,change):
    cd=os.path.dirname(os.path.abspath(__file__))
    dbp=os.path.join(cd,'stock.db')
    conn = sqlite3.connect(dbp)
    cursor = conn.cursor()
    if date!='all':
        if float(change)>0:
            cursor.execute("SELECT * FROM stocks WHERE  date=? AND change>=?", (date, change))
        else:
            cursor.execute("SELECT * FROM stocks WHERE date=? AND change<=?", (date, change))
    else:
        if float(change)>0:
            cursor.execute("SELECT * FROM stocks WHERE change>?", (change,))
        else:
            cursor.execute("SELECT * FROM stocks WHERE change<?", (change,))

    data = cursor.fetchall()
    conn.close()
    return data