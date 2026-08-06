# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료혀의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 Python이 튜플로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

# sensor = ("모터온도", 78)
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))

# sensor = "모터온도", 78
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))

# sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = (
#     "모터온도",
#     78,
# )  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'int'>

# sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>


# sensor = () #  괄호 없고 쉼표없고 값도 안담김
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))

# 튜플의 인덱스

# print(sensor[0])

# 튜플의 슬라이싱
# s = (
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
# )
# print(s[1:4])
# # 슬라이싱한 결과는 소괄호에 감싸져 이씀
# # 튜플은 슬라싱해도 튜플 상태를 유지
# print(type(s[1:4]))

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언
# a, b, c = "a", "b", "c"
# print(a)  # 문자열a
# print(b)  # 문자열b
# print(c)  # 문자열c

# unpacking = (
#     1, # 변수1
#     2, # 변수2
#     3, # 변수3
# )

# unpacking = one, two, three
# # one, two, three라는 알 수 없는 변수를
# # unpacking 변수에 할당하겠다는 의미
# # 동작x
# one, two, three = unpacking
# # unpacking이라는 변수에 담긴 튜플 내부의 값들을
# # 할당 연산자 왼쪽 원 투 쓰리 변수에
# # 풀어서 담겠다는 의미
# print("one", one)
# print("two", two)
# print("three", three)

# 리스트는 언패킹이 될까?

# one, two, three, four = [11, 22, 33, 44]
# print("one", one)
# print("two", two)
# print("three", three)
# print("four", four)

# 튜플의 길이
# print(len(tup)) # 5
# print()

# # 특정 값이 처음 나온 인덱스 찾기
# print(tup.index("warning"))
# print(tup.index("Warning")) # 오류발생

# ==================================

# 튜플리스트
# 리스트 안에 튜플을 담은 것을 표현
# for문으로 리스트를 사용해서
# 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# ============================

# temps_13= [
# (81, "qox_001"),
# (88, "qox_002"),
# (95, "qox_003"),
# (89, "qox_004"),]

# warning = 90

# for name, temp in temps_13:
#     if temp >= warning:
#         print("경고", name, "설비 온도 이상")

# 리스트 안의 튜블 값 갯수가 늘어나면
# for문에서 변수를 여러 개 작성하면 됨

# tup_list = [("일", "one", 1, "1"),("일", "one", 1, "1")]

# for kor_str, eng_str, num, num_str in tup_list:
#     print("kor_str", "eng_str", "num", "num_str")

# 튜플 리스트 정렬
# sorted()를 사용하여
# 튜플의 특정 값 기준으로 리스트를 정렬
# hot = sorted(temps_13, reserve=True)
# print(hot)

# 실습

# sensor = ("모터온도", 78)
# print(sensor)
# print(sensor[0])
# print(sensor[1])

# name, value = sensor
# print(name, value)

# 실습2

# sensor = [("회전속도", 91), ("펌프입력", 92), ("설비온도", 89), ("설비진동수", 88)]
# for name, value in sensor:
#     print(name, value)
# for name, value in sensor:
#     if value > 90:
#         print(name, "경고")

# 실습3
# sensor = [("모터온도", 80, (5, 5)), ("펌프압력", 50, (4, 4)), ("회전속도", 40, (6, 6))]
# for name, value, adr in sensor:
#     x, y = adr
#     print(name, "위치: ", x, y)
#     if x <= 5:
#         print(name)
