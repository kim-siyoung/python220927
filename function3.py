# function3.py
# 기본값
def times(a=10, b=20):
    return a*b

# 호출
print (times())
print (times(5))
print (times(5,6))

# 키워드 인자
def connectURI(server, port):
    strURI = "http://" + server + ":" + port
    return strURI

# 호출
print(connectURI("credu.com","80"))
print(connectURI(port="80", server="text.com"))

# 가변인자(*)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result: # 줄맞추기 중요
                result.append(x)
    return result

# 호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

# 정의되지 않은 인자(딕셔너리처리)
def userURIBuilder(server, port, **user):
    strURI = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURI += key + "=" + user[key] + "&"
    return strURI

# 호출
print(userURIBuilder("credu.com","80", id ="kim", passwd ="1234"))
print(userURIBuilder("credu.com","80", id ="kim", passwd ="1234", name="mike"))

#  람다 함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3)) # 글로벌(내장함수 목록) 찍어봤을때 한번 쓰고 버림 없음 
print(globals())