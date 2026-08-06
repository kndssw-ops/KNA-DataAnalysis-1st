# while은 특정 조건(횟수 X)이 False가 될 때까지
# 반복해야 하는 경우 사용

# 무한루프 유의

# count = 1

# while count <= 3:
#    print(count)
# While 문은 조건이 거짓이 되는 플래그를 꼭 세워야 함
# 무한루프의 강제 종료: 컨씨

# whlie은 사용 체크리스트
# 1. 반복 전 변수(시작값) 존재 여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경되는지

# count = 1 # 1번

# while count <= 3:
#     count = 0 # 반복문 안에 count변수를 계속 0으로 재할당해서 무한루프에 빠짐
#     print(count)
#     count += 1

# answer = 7
# q = 0
# while q != answer:
#     q = int(input("무슨 숫자일까"))
# print("정답입니다!")

# break
# 반복을 그만 돌고 싶을 때
# [1, 2, 1, 2, 1]
# 위 리스트를 돌면서 10 ㅣ사이 되면 중단하고 싶을 떄
# 예 2) 사용자 입력값을 누적하다가 누적값이 총 15를 넘으면
# 종료하고 싶을때
# break 사용 시 즉시 for문을 나감

# input_sum = 0

# while True:
#     user_input = int(input("값을 입력하세요. 값의 누적이 15넘으면 종료: "))
#     input_sum = user_input  # 누적값 업데이트

#     if input_sum > 15:
#         print("누적 합계: ", input_sum, "입력을 종료합니다")
#         break  # 누적 합계가 15를 넘으면 반복 종료
# print("break를 통해 whlie문을 나가면 이후 코드가 실행됨")

# 사용자 입력값을 확인만 하고 저장할 필요가 없는 경우
# while True:
#     # 변수 x는 반복을 돌 때마다 재할당되기 떄문에 휘발되지만
#     x = input("입력 (종료는 q 를 입력하세요): ")
#     # 현재 입력값이 뭔지는 확인할 수 있음
#     if x == "q":
#         break
#     print("입력받은 값: ", x)
# print("종료")

# n = int(input("횟수: "))

# for i in range(n):
#     v = int(input("측정값: "))

#     if v > 80:
#         print("이상 발생")
#         print("가동 횟수:", n)
#         break
#     else:
#         print("정상 상태")

# 실습 up down 게임
# 1~50 중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 정답이고, 게임이 종료되었다고 출력


# answer = 7
# while True:
#     user_input = int(input("숫자를 입력하세요: "))
#     if user_input < answer:
#         print("UP")
#     elif user_input > answer:
#         print("DOWN")
#     else:
#         print("정답입니다")
#         print("게임이 종료되었습니다.")
#         break

# 최댓값 찾기
# first = int(input("1번째 입력값: "))

# max_value = first

# for i in range(4):
#     v = int(input(f"{i + 2}번째 입력: "))
# if v > max_value:
#     max_value = v
# print("최댓값: ", max_value)


# 흐름 표를 보고 코드 작성

# total = 0
# for i in [4, 7, 6]:
#     if i > 5:
#         total += i
#     print("합계:", total)


# n = int(input("횟수: "))
# found = False
# for i in range(n):
#     v = int(input("측정값: "))
#     if v > 80:
#         found = True
#         break
# if found:
#     print("발견")
# else:
#     print("없음")

# # 실습

# temps = [30, 31 ,32 , 33, 34]

# for t in temps:
#     if t > 30:
#         print("고온")

# 실습

temps = [28, 29, 30, 31, 32, 36]
total = 0
count = 0

for t in temps:
    if t > 30:
        total += t
        count += 1
print("고온 평균:", total / count)
