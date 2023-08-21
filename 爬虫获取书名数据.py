import requests
from bs4 import BeautifulSoup
import pandas as pd

content = requests.get("http://books.toscrape.com/").text  # 获取源码
soup = BeautifulSoup(content, "html.parser")  # BeautifulSoup把复杂数据转为树状结构
all_titles = soup.findAll("h3")  # 在返回的树状结构中找到符合条件的元素组成的可迭代对象
l = []
for title in all_titles:
    all_names = title.findAll("a")  # 会返回一个可迭代对象
# 这里的情况也可以直接title.find("a")找到第一个<a></a>
    for name in all_names:
        print(name.string)
        l.append(name.string)

print(l)
s1 = pd.Series(l)
d1 = pd.DataFrame({"书名": s1})
d1.to_csv("books_scrape_书名", index=False)



