import yfinance as yf
import datetime
import os

# 获取金价 (GC=F 是黄金期货代码)
gold = yf.Ticker("GC=F")
data = gold.history(period="1d")
current_price = data['Close'].iloc[-1]
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

# 写入文件
file_exists = os.path.isfile('data.csv')
with open('data.csv', 'a', encoding='utf-8') as f:
    if not file_exists:
        f.write("time,price\n")
    f.write(f"{now},{round(current_price, 2)}\n")
