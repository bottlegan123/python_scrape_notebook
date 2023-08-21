import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
content = requests.get("http://books.toscrape.com", headers = headers).text
soup = BeautifulSoup(content, "html.parser")  # "html.parser"指定html解析器
# BeautifulSoup这个构造函数会把看起来复杂的HTML内容解析成树状结构
print(soup.p)  # 找到第一个<p></p>
all_price = soup.findAll("p", attrs={"class": "price_color"})  # 第一个参数p表示找p标签
# BeautifulSoup对象的findAll方法可以根据标签、属性等找出所有符合要求的元素
print(all_price)
# findAll会返回一个可叠迭代象

l = []
for price in all_price:
    print(price.string[2:])  # string属性会把标签包围的文字属性返回
    print(type(price.string[2:]))
    l.append(price.string[2:])

print(l)
# 把爬虫得到的数据转为列表之后就可以转为Series再之后就可以转为DataFrame

import pandas as pd
s1 = pd.Series(l)
d1 = pd.DataFrame({"price": s1})
d1.to_csv("DouBanTop250_price", )

