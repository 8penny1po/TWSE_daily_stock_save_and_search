import requests
import json
import os
import sqlite3
print(os.getcwd())

def get_data(d):
    cd=os.path.dirname(os.path.abspath(__file__))
    dbp=os.path.join(cd,'stock.db')
    conn=sqlite3.connect(dbp)
    cookies = {
        '_ga': 'GA1.1.79233902.1782883600',
        '_ga_J2HVMN6FVP': 'GS2.1.s1783347540$o7$g0$t1783347540$j60$l0$h0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'referer': 'https://www.twse.com.tw/zh/trading/historical/mi-index.html',
        'sec-ch-ua': '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': '_ga=GA1.1.79233902.1782883600; _ga_J2HVMN6FVP=GS2.1.s1783347540$o7$g0$t1783347540$j60$l0$h0',
    }

    params = {
        'date': d,
        'type': 'ALLBUT0999NOTIND',
        'response': 'json',
        '_': '1789152551771',
    }

    response = requests.get('https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX', params=params, cookies=cookies, headers=headers).json()
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
            conn.execute('''INSERT INTO stocks(
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
                    (d, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], '-'+i[10], i[15]))
        else:
            conn.execute('''INSERT INTO stocks(
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
                            (d, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[10], i[15]))
        conn.commit()
    conn.close()
#a=input('請輸入日期(YYYYMMDD):')
#get_data(a)