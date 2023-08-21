import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

l = []
for i in range(0, 226, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={i}&filter=", headers=headers)
    content = response.text
    print(response.status_code)
    soup = BeautifulSoup(content, "html.parser")
    all_titles = soup.findAll("a")
    for title in all_titles:
        name = title.find("span", attrs={"class": "title"})
        print(name)
        if name is not None:
            Chinese_name = name.string
            l.append(Chinese_name)

print(len(l))
#     del l[0]
# print(l)