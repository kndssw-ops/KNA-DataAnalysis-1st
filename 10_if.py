# 조건문 - if
# 항상 실행되지 않고 조건에 따라서
# 실행되는 코드가 달랐으면 할 때 사용
# 코드의 분기라고도 표현
# 조건문의 조건은 True와 False로 결과가 나와야 함

# if 조건식:
#   실행할 코드 (한 칸 들여쓰기)

# if문의 :은 그 다음 올 코드가 if문 조건식의 결과가 True일 때만
# 실행하라는 의미
# 즉, 여기서부터 이조건에 속한다라는 신호
# 조건에 속하는 코드는 모두 들여쓰기가 적용되어있어야 함

# temp = 85

# if temp > 80:  # 만약에ㅔㅔ temp라는 변수의 값이 80보다 크다면?
#     print("temp 변수의 값이 80보다 크다!!!!")
#     print("♨")
# print("이건 항상 실행되는 코드")

# temp = 70  # 1,2안 모두 정사 동작
# temp = 90
# if temp > 80:  # 50이 80보다 큰 지 비교하고 False라는 결과를 확인하면
#     # 들여쓰기 한 코드는 실행 안함
#     print("temp 변수의 값이 80보다 크다!!!!")
#     print("♨")
# print("이건 항상 실행되는 코드")  # 이 코드만 실행

# # temp 변수의 값이 80보다 크다면 "경고" 출력
# # temp 변수의 값이 80 이하라면 "정상" 출력
# # 위 두가지를 모두 하고싶은 경우

# # 1안
# if temp > 80:
#     print("경고")
# print("정상") # if문 밖의 코드는 무조건 실행됨
# # 이 경우에는 temp 변수ㅢ 값이 90이어도 실행되는것

# # 2안 > else 사용
# if temp > 80:
#     print("경고")
# else: # if문의 조건이 Flase 일때만 출력
#     print("정상") # 항상 실행되지 않음
# if문의 코드블럭과 else문의 코드블럭은 절대 동시에 실행되지 않음
# 둘 중의 하나만 실행
# 2개의 분기로 코드를 실행해야할 때 사용

# if문 실습
# 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성하기

# age = int(input("나이는?: "))
# if age >= 19:
#     print("성인입니다")
# else:
#     print("미성년자입니다")

# 숫자 맞추기 게임

# answer = 50

# n = int(input("숫자를 입력해주세요: "))

# if n == answer:
#     print("맞았습니다 그냥 운이 좋으시네요")
# else:
#     print("틀렸습니다 운이없으시네요ㅋㅋ")
# print("게임이 종료되었습니다.")


# n = input("색을 입력하세요(빨강색,초록색)")

# # or 사용 + if문 중첩
# if n == "초록색" or n == "빨강색":
#     # n 이 초록색 이거나 빨강색 일떄만 실행
#     if n == "초록색":
#         print("건너세요")  # 중첩 if문 들여쓰기 더 주의
#     else:
#         print("기다리세요")
# else:
#     print("ㄱㄷ")


# elif
# n = float(input("체온을 입력하세요"))
# if n <= 36.2:
#     print("저체온")
# elif n >= 36.9 and n < 37.8:
#     print("미열임")
# elif n >= 37.8:
#     print("고온")
# else:
#     print("정상")
# print("체온측정 완료")

# elif의 순서 주의

# score = 50

# if score >= 90:
#     print("우수")
# elif score >= 70:
#     print("보통")
# elif score >= 50:
#     print("미흡")
# else:
#     print("비상")

# # not 연산자
# if not (3 == 5):
#     print("")
# # 3과 5는 같지 않으니 False가 되지만
# # 앞에 not이 False를 뒤집어 True로 뒤집어 if가 인식


# temp = float(input("측정값을 넣으시오: "))
# if temp > 80:
#     print("위험")
# elif temp > 60:
#     print("주의")
# else:
#     print("정상")
# print("온도측정완료")

# ID = "admin"
# P = 1234
# s_ID = input("아이디: ")
# s_P = input("비밀번호: ")
# if s_ID == ID and s_P == P:
#     print("로그인 성공")
# else:
#     print("아이디나 비밀번호가 틀렸습니다")

t = int(input("온도를 입력하세요: "))
d = float(input("진동으로 입력하세요: "))
e = int(input("전류를 입력하세요: "))
if t > 80 or d > 4.0:
    print("위험: 즉시 정지")
else:
    if e > 60 and t > 70:
        print("주의: 부하 점검")
    elif d > 2.5:
        print("주의: 진동 관찰")
    else:
        print("정상")
