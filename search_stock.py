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
        if date=='all':
            cursor.execute('SELECT * FROM stocks WHERE code=?',(askcode,))
           
            f=1
        else:
            cursor.execute('SELECT * FROM stocks WHERE code=? AND date=?',(askcode,date))
            f=2
    row=cursor.fetchall()
    #print('日期,代碼,名稱,開盤價,最高價,最低價,收盤價,成交股數,成交金額,漲跌價差,成交筆數')
    '''for i in row:
        print(i)'''
    return row
    conn.close()
