import save_stock
import search_stock
mode=input('輸入模式(A:儲存資料,B:查詢資料)')
if mode=='A':
    save_stock.save_data_in_db()
elif mode=='B':
    ask=input('輸入股票代碼')
    ab=input('輸入日期YYYYMMDD(若要查詢全部資料請輸入all)')
    askcode=search_stock.get_stock_data(ask, ab)
    print(askcode)