# demoFile.py
from unittest import result


for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---서식지정---")
for x in range(1,6):
   print(x,"*",x,"=",str(x*x).rjust(3)) # 우측 정렬

print("---서식지정---")
for x in range(1,6):
   print(x,"*",x,"=",str(x*x).zfill(3)) # 자릿수 지정 빈자리는 0으로 채움

# 서식지정
print("{0:x}".format(10)) # 16진수로 변경
print("{0:b}".format(10)) # 2진수로 변경
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000)) # 3자리마다 ,

# 파일 쓰기(raw string notation) 유니코드 지정
# f = open("c:\\work\\demo.txt","wt",encoding="utf-8")
f = open(r"c:\work\demo.txt","wt",encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일 읽기(윈도우 -> c:\work  리눅스, 맥 -> /users/kim/desktop)
f = open("c:/work/demo.txt", "rt", encoding="utf-8")
# 처음부터 끝까지 하나의 문자열
result = f.read() # str로 리턴
print(result)
# 어디쯤 읽고 있어?
print(f.tell())
# 리셋
f.seek(0)
lst = f.readlines() # list로 리턴
print(lst)
for item in lst:
    print(item, end="") # 줄바꿈 지움 \n을 ""으로 변환

print("---한줄씩 처리---") # 용량이 크면 readlines 는 전체 읽어오니까 오래걸림
f.seek(0)
print(f.readline(), end ="")
print(f.readline(), end ="")

f.close()