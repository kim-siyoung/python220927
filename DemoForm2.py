# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웹서버에 요청
import urllib.request
# 크롤링
from bs4 import BeautifulSoup


# 화면로딩 (DemoForm2.ui)
form_class = uic.loadUiType("Demoform2.ui")[0]

# 클래스 정의 (부모 클래스 변경)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 시그널을 처리하는 슬롯메서드
    def firstClick(self):
        # 파일에 저장
        f =open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

        # 페이징처리(한페이지에 10개)
        for i in range(1,6):
            url = \
            "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print(url)
            data = urllib.request.urlopen(url)
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")

            for item in cartoons:   
                title = item.find("a").text.strip()
                print(title)
                f.write(title +"\n")

        f.close()
        self.label.setText("네이버 웹툰을 크롤링~")
    def secondClick(self):
        self.label.setText("야옹야옹")
    def thirdClick(self):
        self.label.setText("귀염둥이")

# 직접 모듈을 실행한 경우
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
