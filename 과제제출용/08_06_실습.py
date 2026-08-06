# 실습1) with open으로 파일에 쓰기

# ① with open으로 파일을 쓰기 모드 w, utf-8로 열기

with open("bye.txt", "w", encoding="utf-8") as b:

    # ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
    b.write("잘가세요\n")
    b.write("\t다시봅시다\n")

# ③ with 블록이 끝나면 파일이 자동으로 닫힘

# ④ r 모드로 다시 열어 쓴 내용을 확인
with open("bye.txt", "r", encoding="utf-8") as b:
    lines = b.readlines()
    print(lines)

# 실습 2) a 모드로 기록 이어붙이기

# ① with open으로 파일을 추가 모드 a로 열기

with open("bye.txt", "a", encoding="utf-8") as c:

    # ② write로 새 기록 문장을 쓰기
    c.write("어서오세요\n")
    c.write("\t좋은아침입니다\n")
# ③ w 모드와 달리 기존 내용이 보존됨을 확인
# ④ r 모드로 열어 전체가 쌓였는지 확인
with open("bye.txt", "r", encoding="utf-8") as c:
    lines = c.readlines()
    print(lines)

# 실습 3) csv.reader로 CSV 읽기

# ① csv 모듈을 import
import csv
import os

csv_path = os.path.join("data", "08_press.csv")

# ② with open으로 CSV를 읽기 모드 utf-8로 열기
with open(csv_path, "r", encoding="utf-8") as f:

    # ③ csv.reader로 reader 객체를 만들기
    reader = csv.reader(f)
    # ④ for로 각 행(리스트)을 하나씩 꺼내 출력
    for row in reader:
        print(row)
