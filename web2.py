# web2.py

# 웹서버에 요청
from operator import le
from os import link
import urllib.request
# 크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen(
    "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

soup = BeautifulSoup(data, "html.parser")
cartoons = soup.find_all("td", class_="title")
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)
print("개수:{0}".format(len(cartoons)))

# 주석처리 : 검색할 태그
# <td class="title">
#    <a href="/webtoon/detail">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>

for item in cartoons:
    title = item.find("a").text.strip()
    print(title)