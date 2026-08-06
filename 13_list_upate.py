# 기존 배열의 모든 요소에 3을 곱한 값을 가진 세 리스트

# temps = [1, 5, 2, 7, 4, 8, 10, 3]
# doubled = []

# for in temps:
#     doubled.append(t*3)

# print(doubled)

# 조건에 맞는 값으로 새 리스트 만들기
# high = []
# low = []

# for t in temps:
#     if t < 5:
#         low.append(t)
#     else:
#         high.append(t)

# print("high:", high)
# print("low:", low)

# 복습) sort(): 원본 배열을 오름타순으로 정렬해줌
# 하지만 반환해주지 않기 때문에 print로 바로 찍으면 None 출력


# 정렬된 배열을 출력하고 싶다면 아래처럼
# low.sort()
# print(low)

# temps = [28, 29, 30, 31, 32, 33, 35]
# high = []
# for t in temps:
#     if t > 30:
#         high.append(t)
#         print(high)
#         print("개수: ", len(high))


# temps = [23, 24, 25, 26, 27]
# h = []
# for t in temps:
#     h.append(t * 1.8 + 32)
    # print(h)

# 실습

temps = [22, 24, 25, 30, 31, 32, 36]
empty_temps = []
total_1 = 0
total_2 = 0

for i in temps:
    total_1 += i
    if i > 30:
        empty_temps.append(i)

for i in empty_temps:
    total_2 += i

print(
    f"전체 평균 : {round(total_1/len(temps),1)} / 고온 개수 : {len(empty_temps)} / 고온 평균 : {round(total_2/len(empty_temps),1)}"
)

