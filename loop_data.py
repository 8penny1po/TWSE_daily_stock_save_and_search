import os
import sqlite3
import better_bug
def loop_save(date,rang):
    yyyy=int(date[0:4])
    mm=int(date[4:6])
    nowmm=int(date[4:6])
    dd=int(date[6:8])
    while ((mm+int(rang))%12)!=(nowmm%12):
        if dd==0:
            mm-=1
            if mm==0:
                mm=12
                yyyy-=1
            if mm in [1,3,5,7,8,10,12]:
                dd=31
            elif mm in [4,6,9,11]:
                dd=30
            else:
                if yyyy%4==0 and yyyy%100!=0 or yyyy%400==0:
                    dd=29
                else:
                    dd=28
        date2=str(yyyy)+str(mm).zfill(2)+str(dd).zfill(2)
        better_bug.get_data(date2)
        dd-=1
        print(date2)
#a,b=input('日期和範圍').split()
#loop_save(a,b)
