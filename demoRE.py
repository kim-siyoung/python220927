# demoRE.py

import re

# print(dir(re))
result = re.search("[0-9]*th", "  35th")
# 매칭 오브젝트
print(result)
print(result.group())

# result = re.match("[0-9]*th", "  35th") # 정확하게 일치할 때만
# print(result)
# print(result.group())

result = re.search("apple", "This is an apple")
print(result.group())

print("---년도 찾기---")
print(bool(re.search("\d{4}","올해는 2022년")))
result = re.search("\d{5}", "우리 동네는 52300") # 숫자 연속 5자리 있어?
print(result.group())