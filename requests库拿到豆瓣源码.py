import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}  # 定义请求头把程序伪装成浏览器
response = requests.get("http://movie.douban.com/top250", headers = headers)
# requests.get() 第一个参数为爬取的网站的链接
print(response.status_code)
print(response.text)

