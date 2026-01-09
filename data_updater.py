import yfinance as yf
import datetime
import os

# 1. 获取黄金期货数据 (代码 GC=F 代表纽约金)
# 如果你想监控境内金价，可以换成别的代码，但 GC=F 是全球基准
gold = yf.Ticker("GC=F")
data = gold.history(period="1d")

# 获取最新的一行数据的收盘价
current_price = data['Close'].iloc[-1]
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

# 2. 写入 CSV
file_exists = os.path.isfile('data.csv')
with open('data.csv', 'a', encoding='utf-8') as f:
    if not file_exists:
        f.write("time,price\n")
    f.write(f"{now},{round(current_price, 2)}\n")

print(f"当前金价已记录: {now} - ${current_price}")
