# 변수 서넌 바법
# 변수이름 = 값
# 오른쪽 값을 왼쪽이름에 "저장"하라는 코드
temp = 36  # 숫자로 저장하고 싶다면 따옴표 금지
name = "센서 A"  # 글자는 무조건 따옴표로 감싸기

# print(temp) # 36
# print("temp") # temp

# # = 은 "같다" 가 ㅏ니라 "저장"하는 것
# # 비교는 ==을 사용

# # ======================
# print("==== 변수 사용 ====")

# x = 5
# #변수를 "재할당" 할 때 변수 기존 자신의 값을 활용할수 있음
# #
# x = x + 5
# print(x) # 10
# # y = y + 5 # 오류 발생. y가 선언되지 앟았기 때문

# # ======================
# print("==== 재할당 ====")

# print("재할당하기 전 temp:", temp)
# temp = 15  # 위에서 할당했던 36이라는 값을 15로 재할당(수정)
# Temp = 150  # temp와 다른 변수로 동작

# print(
#     "temp:",
#     temp,)
# print("Temp:", Temp)
# 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴

#  print(score) 선언하지 않아 오류 발생
score = 10
score = 20
score = 30
# print(score)

# ================================
# print("==== 값복사 ====")

# a = 10
# b = a  # b 변수에는 10이 저장 (저장할 때의 그 순간의 a 값을 b에 복사)
# a = 100
# print(b) # 10 b 변수의 값은 10이 그대로 유지됨

# ===========================
# print("===== 여러 변수 한 번에 선언 및 할당 =====")

# # 형식: 변수1, 변수2, ... = 값1, 값2, ... < 변수와 값의 갯수가 같아야함
# width, height = 10, 20
# print("width:", "height:")

# x, y, z = 10, 20  # 변수 3개, 값 2개

# ============================
# print("===주석으로 변수설명===")

# temp = 25  # 온도(섭씨)
# count = 3  # 센서 개수
# # temp = 1000000 주석처리된 코드는 동작하지 않음
# print(temp) # 25

# temperature = 30
# print(temperature)
# name = "센서A"
# print(name)

# my_number = 409
# print(my_number) # 409
# mood = "happy"
# print(mood) # happy

# x = 10
# print(x) # 10
# x = x + 5
# print(x) # 15
# x = x * 2
# print(x) # 30

# a = 100
# b = a
# a = 999
# print(a) # 999
# print(b) # 100


# print(temp)  # NameError발생

# score = 90
# print(Score)  # NameError발생

# temp = 25
# print(temp)  # 25
# score = 90
# print(score) # 90

# 주석으로 변수 설며 달기

# temp = 25  # 온도(섭씨)
# count = 3  # 센서 개수
# # temp # 실행되지 않음
# print(temp)  # 25

# 값 예측 미니 퀴즈

# x = 5
# x = 10
# x = x + 1
# print(x)  # 11

# name = "센서A"
# temp = 25
# print("설비") # 설비
# print(name) # 센서A
# print(temp) # 25

# a = 25
# b = 3
# temp = a
# count = b
# print(temp) # 25
# print(count) # 3

# # 예시 x, y, z = 1, 2, 3
# width, height = 4, 3
# print(width) # 4
# print(height) # 3
