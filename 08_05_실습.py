# 실습 1) import 세 방식으로 모듈 가져오기
import math

print(math.sqrt(16))  # 4.0
print(math.ceil(4.2))  # 5
# =========================
from math import sqrt, ceil

print(sqrt(16))  # 4.0
print(ceil(4.2))  # 5
# =========================
import math as m

print(m.sqrt(16))  # 4.0
print(m.ceil(4.2))  # 5

# 실습 2) 표준 아리브러리로 센서값 만들기
import random
import math

sensor = random.randint(1, 100)
root = math.sqrt(sensor)
print("무작위값:", sensor)
print("제곱근:", root)
# 실습 4) os로 파일 존재

import os

folder = "test_folder"
filename = "test.txt"

path = os.path.join(folder, filename)

exists = os.path.exists(path)

print(exists)

if exists:
    print("파일 있음")
else:
    print("파일 없음")
# 실습 5) datetime으로 점검 기록 남기기
