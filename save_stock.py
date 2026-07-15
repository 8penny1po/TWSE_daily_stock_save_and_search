#openapi
import requests
import sqlite3
import os
#print('-----')
#print(os.getcwd())
def save_data_in_db():
    #--------將資料(stock.db)儲存在這檔案旁
    cd=os.path.dirname(os.path.abspath(__file__))
    dbp=os.path.join(cd,'stock.db')
    #------
    conn=sqlite3.connect(dbp)
    #print(dbp)
    openapi='https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL'
    ope=requests.get(openapi)
    ope.encoding='utf-8'
    print(ope.status_code)
    data=ope.json()
    #_______將民國年轉西元年
    for i in data:
        change_year=int(i['Date'])
        change_year+=19110000
        i['Date']=str(change_year)
    #________

    conn.execute('''
                CREATE TABLE IF NOT EXISTS stocks(
                date TEXT,
                code TEXT,
                name TEXT,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume INTEGER,
                value INTEGER,
                change REAL,
                tx INTEGER,
                PRIMARY KEY(date,code))''')
    for i in data:
        conn.execute('''INSERT INTO stocks(
                    date,
                    code,
                    name,
                    open,
                    high,
                    low,
                    close,
                    volume,
                    value,
                    change,
                    tx)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?)''',
                    (i['Date'],
                    i['Code'],
                    i['Name'],
                    i['OpeningPrice'],
                    i['HighestPrice'],
                    i['LowestPrice'],
                    i['ClosingPrice'],
                    i['TradeVolume'],
                    i['TradeValue'],
                    i['Change'],
                    i['Transaction'])
                    )
    conn.commit()
    conn.close()