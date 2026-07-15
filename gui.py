import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import save_stock
import search_stock
root=tk.Tk()
root.title('TwStockSearch')
root.geometry('600x400')
def save_button():
    button_save['text']='已儲存'
    save_stock.save_data_in_db()
    
button_save=tk.Button(root,text='儲存昨日資料',command=save_button)
button_save.grid(row=0,column=0)
label_code=tk.Label(root,text='輸入代碼:')
label_code.grid(row=1,column=0)
entry_code=tk.Entry(root)
entry_code.grid(row=1,column=1)


label_date=tk.Label(root,text='輸入日期(YYYYMMDD或all):')
label_date.grid(row=2,column=0)
entry_date=tk.Entry(root)
entry_date.grid(row=2,column=1)


tree=ttk.Treeview(root,columns=('date','code','name','open','highest','lowest','close','volume','value','change','transaction'),show='headings')
tree.heading('date',text='日期')
tree.heading('code',text='代碼')
tree.heading('name',text='名稱')
tree.heading('open',text='開盤')
tree.heading('highest',text='高點')
tree.heading('lowest',text='低點')
tree.heading('close',text='收盤')
tree.heading('volume',text='成交股數')
tree.heading('value',text='成交金額')
tree.heading('change',text='漲跌價差')
tree.heading('transaction',text='成交筆數')

tree.column("date", width=100)
tree.column("code", width=100)
tree.column("name", width=100)
tree.column("open", width=100)
tree.column("highest", width=100)
tree.column("lowest", width=100)
tree.column("close", width=100)
tree.column("volume", width=100)
tree.column("value", width=110)
tree.column("change", width=100)
tree.column("transaction", width=100)

root.grid_rowconfigure(4,weight=1)
scrollbery=ttk.Scrollbar(root)
scrollbery.config(command=tree.yview)
tree.config(yscrollcommand=scrollbery.set)
scrollberx=ttk.Scrollbar(root,orient='horizontal')
scrollberx.config(command=tree.xview)
tree.config(yscrollcommand=scrollbery.set)
tree.config(xscrollcommand=scrollberx.set)



def gsd():
    tree.delete(*tree.get_children())
    code=entry_code.get()
    date=entry_date.get()
    if not code:
        messagebox.showwarning('error','請輸入股票代碼')
        return
    elif not date:
        messagebox.showwarning('error','請輸入日期')
        return
    if date!='all':
        try:
            datetime.strptime(date,'%Y%M%d')
        except ValueError:
            messagebox.showwarning('error','請輸入正確日期或格式(YYYYMMDD)')
            return
    result=search_stock.get_stock_data(code,date)
    for i in result:
        tree.insert('','end',values=i)
    tree.grid(row=4,column=0,sticky='news')
    scrollbery.grid(row=4,column=1,sticky='nsw')
    scrollberx.grid(row=5,column=0,sticky='new')

'''    search_results=tk.Label(root,text='search results:')
    search_results.grid(row=4,column=0)
    search_results_t=tk.Text(root,width=100,height=30)
    search_results_t.grid(row=5,column=0)
    search_results_t.insert('1.0',str(result))'''
button_search=tk.Button(root,text='查詢',command=gsd)
button_search.grid(row=3,column=0)

root.mainloop()