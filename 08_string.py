# """ """ - 여러 줄 문자열

# notice = """설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검"""

# print(notice)
# # 설비 점검 안내
# # 1. 전원 확인
# # 2. 센서 점검
# # 위와 같이 직접 작성한 줄바꿈이 반영되어 여러줄로 출력함

# #작성하는 개발자가 보기 편한 방식으로 출력했을 때 문제
# notice = """설비 점검 안내
#  1. 전원 확인
#  2. 센서 점검"""

# print(notice)

# # 삼중 따옴표는 탭도 그대로 유지

# # =========================
# # 이스케이프 문자

# # notice 이스케이프 사ㅛㅇ해서 개선
# notice = "설비 점검 안내\n1. 전원확인\n2. 센서점검"

# tap = "이름\t상태"
# print(tap)
# print("이름 상태")

# backslash = "이름\\상태"
# print(backslash) # 이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

# quotes = "It's me"  # 감싸는 따옴표와 str내부 따옴표의 종류가 같으 떄는 \를 사용
# print(quotes)

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 ㅏㄶ았다면 "빈 문자열"
# 빈 문자ㅕㄹ은 글자수 0, 길이 0
# " " 따옴표 안에 공백(스페이스바)이 있는 경우는 "공백 문자열"
# 공백 (스페이스바)의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨
# print("" == "  ")  # False

# 실습 결과
# 설비: PUMP_A - str
# 상태: 정상 - str
# 가동: 1200 - int
# 점검: 2026-07-16 - str

# code = "PUMP_A"
# state = "정상"
# hour = 1200
# date = "2026-07-16"

# card = "설비: " + code + "\n상태: " + state + "\n가동: " + str(hour) + "\n점검: " + date

# # 코드 정리
# # ===================
# #        "설비: " + code
# #      + "\n상태: " + state
# #      + "\n가동: " + str(hour)
# #      + "\n점검: " + date

# print(card)

# 설비: PUMP_A
# 상태: 정상
# 가동: 1200
# 점검: 2026-07-16

# ===============
# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열[인덱스번호]
# 문자열의 첫 글자 인덱스는 0

# word = "PYTHON"
# print(word[0], word[3], word[5])  # P H N

# print(word[100]) # InexError > 변수에 저장된 문자열의 길이보다 큰 인덱스를 호출했기 때문

# abc = "abcdefghijklmnopqrstuvwxyz"

# # 자기 이름 출력하기 (성 뺴고) # seung won
# print(abc[-8], abc[4], abc[-6], abc[13], abc[6], abc[-4], abc[-12], abc[-13])

# # 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# # 주의사항은 음수 인덱스는 가장 마지막 글자가 -1부터 시작

# # =========================
# print("=== 슬라이싱 ===")

# 슬라이싱 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함래서 출력
# 끝인덱스 글자는 제외하고 출력

# word = "PYTHON"
# print("word[3:5] 결과: ", word[3:5])
# print("word[3:6] 결과: ", word[3:6])

# 슬라이싱은 end가 포함되지 않고 출력하기 떄문에 없는 인덱스인 6도 사용할 수 있음

# print(word[6])  # 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고, 넘치면 Error

# print(word[:6]) = print(word[0:6]) 완전 동일
# print(word[0:]) = print(word[0:6])
# print(word[:]) = print(word[0:6])
# 음수 인덱스도 사용 가능

# step
# 문자열[시작:끝;간격(step)]

# 처음문자 > 간격만큼 뛰고 입력 > ~똑같이

# start와 end를 생략하고 step만 입력
# print(word[::2])  # word 변수의 모든 글자를 두 칸씩 뛰면서 출력

# # 순서 뒤집기
# print(word[::-1])
# # 스텝은 인덱스가 아니고, 음수 입력 시 문자열의 순서를 뒤집음

# # 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
# print("범위를 벗어난 슬라이싱", word[:100])  # 정상출력됨

# word = "temp_sensor"
# print(word[5:])  # sensor

# word = "sensor_01"
# print(word[-2:]) # 01

# word = "PYTHON"
# print(word[::-1]) # NOHTYP

# =======================
# len() - 문자열의 길이 반환
# len(문자열)

# print(len("Hello World!"))  # 12(공백도 모두 글자 취급을 한다)
# print(len(""))  # 0 (빈 문자열은 0 출력)

# var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요!"
# print(len(var))  # 변수에 담긴 문자열의 길이 출력도 가능

# print(len("이것도") - len("가능할까?"))
# len()은 int로 반환하기 때문에 가능하다

# print("abc 변수의 길이:", len(abc), " / 마지막 인덱스 번호:", len(abc) - 1)

# print(abc[len(abc) - 1])

# PH = "01012345678"
# print(len(PH)) # 11

# ===============================
# print("=== in 활용 ===")

# # - 특정 문자가 문자열에 포함되었는지 여부 확인
# # "여부"를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# # 찾을문자열 in 문자열
# print("고장" in "설비 고장 발생") # True
# print("정상" in "설비 고장 발생") # False
# print("설비에서 고장" in "설비 고장 발생") # False
# print("설비에서 고장" in "설비에서 고자이 났습니다.") # True

# # not in - in의 정반대 동작

# print("고장" not in "설비 고장 발생") # False
# print("정상" not in "설비 고장 발생") # True
# print("설비에서 고장" not in "설비 고장 발생") # True
# print("설비에서 고장" not in "설비에서 고자이 났습니다.") # False

# print(" " in "설비 고장 발생") # True
# # 따옴표로 감싼 공백(스페이스바)는 정말 "한 글자"로 취급

# =======================
# print("=== count ===")

# # .count() - 문자열에 특정 글자의 수(int)를 반환
# # 문자열.count("찾을 글자")
# print("banana".count("a"))  # 3
# print("010-1234-1234".count("-"))  # 2
# print("layla@spreatics.com".count("@"))  # 1
# 찾는 문자열이 없으면 에러 발생

# str = "a, b, c, d, e,a, a"

# a의 갯수 새기
# print(str.count("a"))  # 3

# # 쉼표의 갯수?
# print(str.count(","))  # 6
# print(str.count(", "))  # 5 # 찾는 문자열과 완전히 동일해야함


# text = "a,b,c,d"
# print(text.count(",")) # 3

# # ======================

# print("=== find ===")

# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환

# email = "hong@company.com"
# at = email.find("@")  # @위치의 인덱스인 4가 할당됨
# user_id = email[:at]  # hong 이라는 사용자의 아이디만 추출
# print(user_id)

# ====================

# 특정 문자열의 위치 index번호를 반환

# email = "Layla@spreatics.com"
# at = email.index("@")  # 5
# print(email[0:at])  # Layla
# print(email[:at])  # 시작 번호가 0이라면 start 생략 가능
# print(email[at:])  # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략
# print(email[at + 1 :]) # 이렇게 기입하면 @를 포함하지 않고 출력

# find 에서 했던 SQE 뽑아내기 실습 index로 바꾸기

# sqe = "SQE-00Q8"
# sqe_index = sqe.index("-")
# print(sqe_index)  # 3
# sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
# print(sqe_fin)  # SQE


# SQE
# sqe = "SQE-00Q8"
# sqe_index = sqe.find("SQE")
# print(sqe_index)  # 0

# sqe_index = sqe.find("-")
# print(sqe_index)  # 3
# sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
# print(sqe_fin)  # SQE

# ========================
# startswith

# 특정문자열로 시작하는지 검사
# True/False (불리언)

# EQP로 시작하는지 검사
# print("EQP-001".startswith("EQP"))  # True

# # 변수 활용
# eqp = "EQP"
# print("EQP-001".startswith(eqp)) # True
# # 주의사항) 변수명은 따옴표 감싸기 금지

# # ================================
# # endswith

# # 특정 문자열로 끝나는지 확인
# # True/False (불리언)

# str2 = "월요일 입니다! 여러분은 할 수 있어요!"

# print(str2.endswith("!")) # T
# print(str2.endswith("요!")) # T
# print(str2.endswith("음!")) # F
# print(str2.endswith("음!")) # F
# print(str2.endswith("월요일 입니다! 여러분은 할 수 있어요!")) # T
# print(str2.endswith("월요일 입니다!              여러분은 할 수 있어요!")) # F
# print(str2.endswith("월요일 입니다! 여러분은 할 수 있어요! ")) # F
# print(str2.endswith(" 월요일 입니다! 여러분은 할 수 있어요!")) # F

# 실습

# str = "sensor_log.csv"

# print(str.startswith("sensor")) # True
# print(str.endswith(".csv")) # True

# ===========================
# end와len의 차이
# endswith는 . 사용 len은 안씀
# .으로 연결하는 이런 도구들은 매서드
# 문자열이나  int, float 처럼 특정 자료형 내부에 포함된 기능
# () -> 함수
# len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 "내장함수"

# "str".startswith("s")
# 123.startswith(1)
# .으로 사용하는 매서드 들은 특저 자료형(객체 타입) 마다 다름
# int 자료형의 객체에는 stratswith 라는 매서드가 없음

# print(len(123)) # len 내장함수는 길이를 반환하기 떄문에 int 자료형 사용 불가

# ====================
# num = 1
# num = num + 1  # 2
# num += 1  # 3
# += 은 복합할당연산자 원래 내 자신의 값에 다음 오는 연사자와 값을 재할당 함

# ============================

# str = "abcefg"
# print(str)

# # str.upper # 값에 재할당을 안했기 때문에 아래는 소문자 그대로 출력, 앞으로 대문자 출력값을 사용하고 싶다면 재할당 해야함

# print(str)

# str = str.upper()

# str1 = "WARNING"
# s = str1.lower()
# print(s) warning

# str = "ready"
# s = str.upper()
# print(s) # READY

# ========================

# print("ABC".isupper()) # True
# print("abc".islower()) # True
# print("Abc".isupper()) # False

# 실습6

# str = "Sensor_LOG.CSV"
# s = str.lower()
# print(s.startswith("sensor")) # True
# print(s.endswith("csv")) # True

# ==================
# .strip(): 앞 뒤의 모든 공백 제거
# .lstrip() 앞의 공백 제거
# .rstrip() 뒤의 공백 제거

# raw = "  정상      "
# print(raw.strip())
# print(raw.lstrip())
# print(raw.rstrip())

# 문자열의 가운데 공백은 strip으로 지우지 못함
# print("       정      상         ".strip()) # 가운데 공백은 남아있음

# =======================

# str5 = "=정상============"
# print(str5.strip("="))  # 앞뒤 문자를 다 지움
# print(str5.strip("= "))  # 공백 상관없이 다 지움

# str6 = "==정==상==="
# print(str6.strip("=")) # 글자 사이에 있는 문자열은 지우지 않음

# str = "WARNING"
# print(str.strip().lower())

# ========================
# raw = ' NORMAL '
# step1 = raw.strip() # 'NORMAL'
# clean = raw.strip().lower() # 'normal'
# print(clean)

# # 체이닝 0
# chain = raw.strip().lower()

# # 기존 변수에 재할당도 가능
# raw = raw.strip().lower()

# # 변수에 할당하지 않고 사용가능
# print(raw.strip().lower())

# ===실습===
# str = "     Warning     "
# print("[" + str.lower() + "]") # [    warning    ]

# str = str.lower()
# print("[" + str.strip() + "]") # [warning]

# =========================
# replace

# 특정 문자열을 제거하거나 치환할 때 사용
# 제거할 때는 인자의 두 번째를 ""(빈문자열)로 작성/ ("a","b") a를 b로 바꿈
# print("정 상 가 동".replace(" ", ""))
# print("     정          상 가 동".replace(" ", ""))  # 정상가동 (모든공백제거)
# print("     정          상 가 동".replace("  ", ""))  # 두칸 공백에 해당하는 부분만 제거

# # 글자 치환
# print("고장".replace("고장", "fault"))  # fault
# print("고장".replace("고", "fault"))  # fault장

# # replace() 체이닝
# str9 = "설비 정상 가동"
# print(str9.replace("정상", "점검"))  # 설비 점검 가동

# # 체이닝
# num = "    010-1234-5678    "
# num = num.replace(" ", "").replace("-", "")  # 01012345678


# ====================
# split

# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 떄문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

# drinks = "에스프레소 아메리카노 카페라떼"
# print(drinks.split())  # ['에스프레소', '아메리카노', '카페라떼']
# # 띄어쓰기를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환

# 구분자를 특저하고 싶은 경우
# fruits = "딸기, 거봉, 키위, 사쿠란보"
# print(fruits.split(","))  # ['딸기', ' 거봉', ' 키위', ' 사쿠란보']

# # fruits2 = "딸기, 거봉, 키위, 사쿠란보"
# # print(fruits2.split(", "))

# # 리스트의 인덱스
# fruits_list = fruits.split(",")
# print(fruits_list)

# # 거봉만 출력하기
# print(fruits_list[1])  # 출력하고자 하는 요소의 인덱스를 대괄호로 감싸서 호출


# split 횟수 제한
# num = "010-1234-1234"
# # ["010", "1234-1234"]
# print(num.split("-", 1)) # 괄호의 숫자만큼 나눔

# str = "a,b,c,d"
# print(str.split(","))

# # ================

# # join
# # 리스트를 하나의 문자별로 합침
# # "구분자" join(리스트)
# # 모든 요소가 합쳐져서 하나의 문자열로 반환

# fruits = "딸기, 거봉, 키위, 사쿠란보"

# "-".join(fruits_list) # "딸기-거봉-키위-사쿠란보"
# ",".join(fruits_list)
# ", ".join(fruits_list)

# n = ["2025", "01", "15"]
# print("-".join(n))  # 2025-01-15

# # pyThon 출력하기

# word = "python"
# print(word.replace("t", "T")) # pyThon

# # ========================
# # print의 sep.end로 구분자 넣기

# print("2026", "07", "27")

# sep속성을 사용하면 구분을 공백이 아닌 특저 문자ㅕㄹ로 가능
# print("2026", "07", "27", sep="사랑해")  # 2026사랑해07사랑해27

# print("안녕", "하세")  # 안녕 하세
# print("안녕", "하세", end="요")  # 안녕 하세요
# end 속성 사용 시 출력은 마지막에 해당 문자열이 붙어서 출력

# print("안녕", "하세", end="요", "ㅎㅎ") # end 속성 뒤에 또 인자 붙이기 불가

# print 함수 + 사용 시 sep과 end
# print("안녕", "하세", end="요" + "이렇게?!") # 정상동작 하나 이렇게 코딩X

# 기본적으로 print문에는 sep으로 공백 한 칸
# end로 \n(줄바꿈)이 적용됨

# print("이런식으로 쓰죠", "근데 안보이는 기본값이 있어요", sep=" ", end="\n")

# n = "2025/01/15"
# p = n.split("/")
# print("-".join(p)) # 2025-01-15

# r = "1, NORMAL,25.3"
# p = r.split(",")
# s = p[1].strip().lower()
# print(s)  # nomal

# # =======================
# # f-string

# name = "PUMP_A"
# temp = 87
# print(f"설비 {name}, 온도 {temp}도")
# 따옴표 밖애 f작성하기
# 변수명은 꼭 {중괄호}에 감싸기

# f-string 연산
# hour = 8

# # 우리는 하루에 8시간 수업을 듣고, 이는 480분입니다

# print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour*60}분입니다")
a = 86
b = 87
c = 88
print(f"평균{(a + b + c) / 3}")

r = 87.456
print(f"{r:.1f}")
print(f"{r:.2f}")

str = "5, sensor_2, WARNING, 0.78912"
p = str.strip().split(",") 

print(f"[센서 {p[1]}] 상태 {p[2].lower()}, 측정값 {float(p[-1]):.2f}")
