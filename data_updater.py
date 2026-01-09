import datetime
import random
import os

# 1. 模拟获取数据 (实际操作中这里换成爬虫代码)
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
value = random.randint(100, 500)

# 2. 将数据保存到 CSV 文件中
file_exists = os.path.isfile('data.csv')
with open('data.csv', 'a', encoding='utf-8') as f:
    if not file_exists:
        f.write("time,price\n")  # 写入表头
    f.write(f"{now},{value}\n")

print(f"数据已更新: {now} - {value}")
