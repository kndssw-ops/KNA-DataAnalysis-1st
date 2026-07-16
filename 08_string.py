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

# text = "a,b,c,d"
# print(text.count(",")) # 3

# # ======================

# print("=== find ===")

# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환

email = "hong@company.com"
at = email.find("@")  # @위치의 인덱스인 4가 할당됨
user_id = email[:at]  # hong 이라는 사용자의 아이디만 추출
print(user_id)
