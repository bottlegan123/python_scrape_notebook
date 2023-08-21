# 获取豆瓣top250
from bs4 import BeautifulSoup
import requests
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
for start_num in range(0, 250, 25):
    print(start_num)
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=headers)
    print(response.status_code)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")  # 获得网页的html

    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        # print(title)
        title_string = title.string
        if "/" not in title_string:
            print(title_string)

"""
from bs4 import BeautifulSoup
import requests
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
for start_num in range(0, 250, 25):
    print(start_num)
    if start_num != 0:
        response = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=headers)
        print(response.status_code)
        content = response.text
        soup = BeautifulSoup(content, "html.parser")  # 获得网页的html

        all_titles = soup.findAll("span", attrs={"class": "title"})
        for title in all_titles:
            # print(title)
            title_string = title.string
            if "/" not in title_string:
                print(title_string)
    else:
        response = requests.get("https://movie.douban.com/top250", headers=headers)
        print(response.status_code)
        content = response.text
        soup = BeautifulSoup(content, "html.parser")  # 获得网页的html

        all_titles = soup.findAll("span", attrs={"class": "title"})
        for title in all_titles:
            # print(title)
            title_string = title.string
            if "/" not in title_string:
                print(title_string)
    # 不写else，那么不满足if时就啥也不输出
# 到现在我们只能获得一页网页上面的排名在top250以内的电影，但是其他网页的也排名在top250的我们没有得到
# 那要怎么办呢？那么就需要对网页进行操作，返回去
"""


"""
from bs4 import BeautifulSoup
import requests
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
response = requests.get("https://movie.douban.com/top250", headers=headers)
print(response.status_code)
content = response.text
soup = BeautifulSoup(content, "html.parser")  # 获得网页的html

all_as = soup.findAll("a")
for title in all_as:
    span = title.find("span", attrs={"class": "title"})
    if span != None:
        print(span.string)
    else:
        print("")

"""


