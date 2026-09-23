import requests
import json
import os
import sqlite3
import time
print(os.getcwd())

def get_data(d):
    cd=os.path.dirname(os.path.abspath(__file__))
    dbp=os.path.join(cd,'stock.db')
    conn=sqlite3.connect(dbp)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'
    }

    params = {
        'date': d,
        'type': 'ALLBUT0999NOTIND',
        'response': 'json',
        '_': '1789152551771',
    }

    response = requests.get('https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX', params=params, headers=headers).json()
    print(type(response))
    print(response.keys())
    '''
    with open(dbp, 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=2)'''
    conn.execute('''
                    CREATE TABLE IF NOT EXISTS stocks(
                    date TEXT,
                    code TEXT,
                    name TEXT,
                    volum INTEGER,
                    tx INTEGER,
                    value INTEGER,
                    open REAL,
                    high REAL,
                    low REAL,
                    close REAL,
                    change REAL,
                    peratio REAL,
                    PRIMARY KEY(date,code))''')
    for i in response['tables'][8]['data']:
        if '-' in i[9]:
            datalist=[(d, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], '-'+i[10], i[15])]
        else:
            datalist=[(d, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[10], i[15])]
        conn.executemany('''INSERT OR IGNORE INTO stocks(
                    date,
                    code,
                    name,
                    volum,
                    tx,
                    value,
                    open,
                    high,
                    low,
                    close,
                    change,
                    peratio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                datalist)
    conn.commit()
    conn.close()
    time.sleep(1)
#a=input('請輸入日期(YYYYMMDD):')
#get_data(a)