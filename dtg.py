import sqlite3
import os
def dg(d,code):
    cd=os.path.dirname(os.path.abspath(__file__))
    dbp=os.path.join(cd,'stock.db')
    conn = sqlite3.connect(dbp)
    cursor = conn.cursor()
    yyyy=int(d[0:4])
    mm=int(d[4:6])
    dd=int(d[6:8])
    i=0
    vwma=[]
    sma=[]
    date=[]
    volum=[]
    close=[]
    openn=[]
    high=[]
    low=[]
    while i<20:
        date2=str(yyyy)+str(mm).zfill(2)+str(dd).zfill(2)
        cursor.execute('SELECT date,volum,close,open,high,low FROM stocks WHERE date<=? AND code=? ORDER BY date DESC LIMIT 20',(date2,code))
        row=cursor.fetchall()
        #print(row[0])
        #print(len(row))
        if len(row)!=0:
            i+=1
            indexv=0
            indexs=0
            vvv=0
            day=str(row[0][0])
            if day in date:
                i-=1
            else:
                if len(row)<20:
                    return
                else:
                    for j in range(20):
                        vv,cc=float(str(row[j][1]).replace(',','')),float(str(row[j][2]).replace(',',''))
                        indexv+=(vv*cc)
                        vvv+=vv
                        indexs+=cc
                    day,vv,cc,oo,hh,ll=str(row[0][0]),float(str(row[0][1]).replace(',','')),float(str(row[0][2]).replace(',','')),float(str(row[0][3]).replace(',','')),float(str(row[0][4]).replace(',','')),float(str(row[0][5]).replace(',',''))
                    vwma.append(indexv/vvv)
                    sma.append(indexs/20)
                    date.append(day)
                    volum.append(vv)
                    close.append(cc)
                    openn.append(oo)
                    high.append(hh)
                    low.append(ll)

        dd-=1
        if dd<=0:
            mm-=1
            if mm in [1,3,5,7,8,10,12]:
                dd=31
            elif mm in [4,6,9,11]:
                dd=30
            else:
                if yyyy%4==0 and yyyy%100!=0 or yyyy%400==0:
                    dd=29
                else:
                    dd=28
        if mm==0:
            yyyy-=1
            mm=12
    #print(vwma,sma,date,volum,close,openn,high,low)
    return vwma[::-1],sma[::-1],date[::-1],volum[::-1],close[::-1],openn[::-1],high[::-1],low[::-1]
'''a,b=input().split()
aa=dg(a,b)'''
