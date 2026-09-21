import sqlite3
import os
def get_stock_data(askcode,date):
    cd=os.path.dirname(os.path.abspath(__file__))
    dbp=os.path.join(cd,'stock.db')
    conn = sqlite3.connect(dbp)
    cursor = conn.cursor()
    f=0
    #cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print(cursor.fetchall())

    while f==0:
        if date=='all' and askcode!='':
            cursor.execute('SELECT * FROM stocks WHERE code=? ORDER BY date DESC',(askcode,))
           
            f=1
        elif date=='all' and not askcode:
            cursor.execute('SELECT * FROM stocks ORDER BY date DESC')
            f=2
        elif not askcode:
            cursor.execute('SELECT * FROM stocks WHERE date=? ORDER BY date DESC',(date,))
            f=3
        else:
            cursor.execute('SELECT * FROM stocks WHERE code=? AND date=? ORDER BY date DESC',(askcode,date))
            f=4
    row=cursor.fetchall()
    print(f)
    '''for i in row:
        print(i)'''
    return row
    conn.close()
