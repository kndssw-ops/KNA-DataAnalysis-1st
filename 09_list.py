# list는 파이썬의 자료형 주 하나
# 여러 개의 값을[대괄호]에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

# temps = [35, 36, 37, 38] # int 리스트
# float_temps = [36.4, 36.5, 36.6, 36.7] # float 리스트
# machines = ["펌프", "압축기", "모터"] # string 리스트

# # 자료형이 달라도 한 리스트에 담을 수 있음
# mixed = ["펌프", 78, True]

# # 리스트에 자동으로 순서 인덱스가 붙는다면?
# print(temps[2]) # 37 > 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# # 리스트 ㅏ네 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑고싶다면?
# print(temps[-1]) # 가자 마지막 요소 출력

# # 빈 리스트
# empty = []

# # 리스트에 담긴 값의 갯수 새기
# # len() 내장함수 사용
# print(len(temps)) # 4
# print(len(empty)) # 0

# # 리스트의 담긴 값의 갯수 변수에 저장
# temps_length = len(temps) # 변수에 4라는 값이 할당
# print(len(temps_length)) # 4

# 실습

# temps = [32, 32, 33, 34, 34]
# # print(temps)
# # print(len(temps))  # 5
# # empty = []
# # print(len(empty))  # 0

# # 리스트의 인덱스
# print(temps[0], temps[-1])  # 0번째와 제일 마지막 요소 출력
# # -1을 사용하는 이유는 최신 값은 대체로 뒤에 추가됨
# # 가장 최신 값은 마지막 인덱스의 요소
# # len 함수를 사요해서 리스트 길이 -1로 계산이 가능하지만
# # 이 작업이 번거로워 -1을 가장 많이 사용

# # 없는 인덱스 호출
# # temps 리스트는 길이가 5
# print(temps[5]) # IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

# 실습
# temps = [22, 23, 24, 25, 26, 27]
# print(temps[0])
# print(temps[2])
# print(temps[-1])

# 실습

# r = [20, 25, 26, 28, 27, 30]
# a = r[0]  # 20
# b = r[-1]  # 30
# print(a + b)
# print((a + b) / 2)

# # 다른 자료형의 값이 들어있는 리스트의 요소 타입
# # float 값이 들어있는 float_temps 리스트ㅢ 0번쨰 요소
# print(type(float_temps[0]))  # <class 'float'>
# print(type(machines[0]))  # <class 'string'>

# # 퀴즈
# mixed = ["펌프", 78, True]

# print(type(mixed[1]))  # class int
# print(type(mixed[-1]))  # class bool
# print(type(mixed))  # class list

# 리스트 슬라이싱
# 리스트명 [시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략 가능

# temps = [35, 36, 37, 38]

# #실습 4, 5

# temps = [22, 24, 27, 26, 23, 20, 25, 28, 30, 21]
# print(temps[:3])  # [22, 24, 27]
# print(temps[-3:])  # [28, 30, 21]

# print(len(temps[:3]))  # 3

# r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# first = r[:6]
# second = r[-6:]

# print(len(first))
# print(len(second))

# # ===================

# #==in==

# machines = ["펌프", "모터", "압축기"]
# print("모터" in machines) # True
# print("밸브" in machines) # False
# print("밸브" not in machines) # True

# temps = [25, 26, 240, 28, 27]
# print(24 in temps)  # False
# print(240 in temps)  # True
# print(temps.index(240))  # 2

# temps[2] = 24

# print(24 in temps)  # True

# 리스트 값 추가
# append(추가할값)
# 리스트의 가장 마지막에 값을 추가
# 리스트의 원본이 수정됨, 재할당이 필요하지 않음
nums = [1, 2, 3, 4, 5]

# nums.append(999)
# print(nums)  # 999가 바로 뒤에 붙음

# # 만약 원본 리스트와 특정 값을 추가한 리스트 둘다 필요하다면
# # 원본 리스트 복사해서 리스트 수정 진행
# # nums = [1, 2, 3, 4, 5] > 기존 리스트는 원본으로 둠

# new_nums = nums
# print(new_nums)

# new_nums.append(111)
# print("원본 nums 리스트:", nums)
# print("복사본new_nums에 111 append 결과:", new_nums)

# # ====================
# # insert
# # 리스트에서 원하는 위치에 값을 삽입
# # 기존 배열에서 삭제는 되지 않고, 해당하는 인덱스 값을 삽입(뒤에 요소들은 밀어내기)
# nums.insert(3, 333)
# print(nums)

# # ========================
# # extend
# # 리스트 연결
# # 다른 리스트의 값들을 풀어서 이어붙임
# data = [1, 2, 3]
# new_data = [7, 8, 9]
# sum_data = data.extend(new_data)
# print(data)


# # 함수의 반환 개념을 안 뒤에 확인할 내용
# print(data.extend(new_data))
# # extend매서드는 data라는 리스트를 수정함 그러나 이름 반환하지 않음
# # 반환값이 없어서 print할 값이 없는것
# print(data)  # [1, 2, 3, 7, 8, 9]

# # 리스트를 수정하는 매서드는 모두 반환값이 없는가?
# print(data.append[123])
# print(data.insert[0, 123])
# print(data.extend[new_data])
# 현재 배운 매서드는 반환값이 없음.


# 정리
# 오늘 꼭 알아야 하는 리스트 수정 매서드와 개념
# .append() : 리스트의 가장 마지막에 값을 추가
# .insert() : 원하는 위치에 값을 넣음
# .extend() : 다른 리스트의 값들을 이어붙임
# 위 세 가지 매서드 들은 원본 리스트 자체를 수정함!


# temps = []
# temps.append(30)
# print(temps)
# temps.insert(0, 28)
# print(temps)
# temps.extend([31, 32])
# print(temps)


# =======================

# remove(값) : 위치는 모르고 삭제함

# list1 = ["딸기", "사과", "배", "포도", "수박", "망고"]
# list1.remove("수박")
# print(list1)


# # .pop(인덱스) : 인덱스로 특정 요소를 삭제할 떄 사용
# # 삭제한 인덱스의 값을 반환
# list1.pop(0)
# print(list1)
# print(list1.pop(2))
# # 삭제도 하고, 삭제한 인덱스 값도 출력


# # del : 인덱스로 리스트의 요소 삭제 (슬라이싱으로 영역 삭제 가능)
# del list1[0]
# print(list1)
# del list1[:] # 앞뒤 생략
# print(list1) # [] > 빈 리스트가 됨

# del 건너뛰기
# list2 = ["빨강", "노랑", "초록", "파랑", "남색", "보라"]
# del list2[::2]
# print(list2)

# 실습

# list = [25, 26, 24, 999, 28, 26]
# list.remove(999)
# print(list)  # [25, 26, 24, 28, 26]
# l = list.pop(4)
# print(l)  # 26
# del list[0]
# print(list)

# temps = [27, 24, 30, 22, 26]
# temps.sort()
# print(temps)  # [22, 24, 26, 27, 30]
# temps.sort(reverse=True)
# print(temps)  # [30, 27, 26, 24, 22]

# # ==================
# # 리스트 정렬하기
# # 리스트.sort()
# # 데이터를 정렬하는 친구
# # 기본적으로 오름차순(작은 숫자부터 큰 숫자까지)
# # 내림차순으로 정렬하고 싶은 경우에는 .sort(reverse=True)

# n = [37, 2, 8, 109, 1004, -1, 22]

# # 오름차순 정렬
# n.sort()  # 원본 리스트가 수정됨
# print("n 리스트 오름차순 정렬결과:", n)  # [-1, 2, 8, 22, 37, 109, 1004]

# # 내림차순 정렬
# n.sort(reverse=True)
# print("n 리스트 내림차순 정렬결과:", n)

# # 리스트 순서 뒤집기
# # .reverse()
# # 오름내림차순 등의 정렬은 해주지 않음
# # 뒤로 계속 쌓인 결과(최신)를 앞에서부터 보고싶을 때 서술

# n = [37, 2, 8, 109, 1004, -1, 22]

# n.reverse()
# print("n순서 뒤집기 결과:", n)

# 리스트 안 값의 갯수 구하기
# .count(찾을값)

# f = ["텀블러", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
# print(f.count("일회용컵"))
# print(f)  # 원본 배열에 변화 없음

# # 특정 값의 위치 찾기
# # index.(=위치를찾을값)
# # 리스트에서 가장 첫 위치만 찾아줌
# print(f.index("일회용컵"))
# print(f) # 원본 배열에 변화가 없음

temps = [
    25,
    28,
    30,
    21,
    22,
    26,
    24,
]

temps.sort()
print(temps)

temps.reverse()
print(temps)

print(temps.count(24))
print(temps.index(24))
