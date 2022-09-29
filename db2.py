# db1.py
import sqlite3

# 연결객체(일단은 메모리에서 작업)
# con = sqlite3.connect(":memory:")
# 실제 물리적인 파일에 저장(sample.db)
con = sqlite3.connect("c:\\work\\sample.db")

# 구문을 실행하는 커서
cur = con.cursor()
# 데이터 구조(Table)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
# 입력 파라미터 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNumber))
# 여러건 입력
datalist = (("tom","010-123"),("dsp","010-5678"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)
# 검색
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
# 연결객체에서 완료
con.commit()