from bs4 import BeautifulSoup
import urllib.request
import json
import os
class Data:
    def __init__(self, title, description, paras) -> None:
        self.title = title
        self.description = description
        self.paras = paras

# Initialize the JSON data object


url = 'https://cn.chinadaily.com.cn/a/202302/20/WS63f31fd0a3102ada8b22fc6a.html'

def crawl_News(url):
    if "cn.chinadaily.com.cn" not in url:
        return "khong dung duoc"
    else:
        data = {"content": []}
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        # Get title
        title = soup.select('h1.dabiaoti')[0].text.strip()
        description = None
        # Get content
        content = soup.find('div', class_="article")
        p_tags = content.find_all("p")

        paras = []
        for p in p_tags:
            para = p.text
            paras.append(para)
        # Store the data in a Data object
        content = Data(title, description, paras)
        data["content"].append({"title": content.title, "description": content.description, "paras": content.paras})
        title = data['content'][0]['title']
        description = data['content'][0]['title']
        paras = data['content'][0]['paras']
        return title, description,paras

print(crawl_News(url))