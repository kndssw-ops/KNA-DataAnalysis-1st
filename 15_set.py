# ==============

# set
# 빈 set 만들기
# list_= [] # 빈 리스트
# print(type(empty_tuple))

# # 값을 포함한 셋 만들기
# logs = ["S01", "S02", "S01", "S03,", "S01"]
# unique = {logs}
# # print(type(unique)) # error

# print(unique) # 중복되었던 S01이 한번만 들어감
# 지금은 길이가 짧아서 순서대로 정렬된 것처럼 보이지만
# 셋은 순서가 없는 값의 묶음
# print(unique[0]) # error

# logs = [("WQR_01") * 4, ("WQR_06") * 2, ("WQR_03") * 1, ("WQR_05") * 1]
# unique = set(logs)
# print(sorted(unique))
# print("종류 수:", len(unique))

# =========================

# 집합 연산

# hour_1 = {"a1", "b2", "c3", "d4"}
# hour_2 = {"b2", "e5", "c3", "f6"}
# print(hour_1.union(hour_2))

# # .union은 원본 셋에 변화 x

# # |연산자를 활용해 짧게 작성 가능
# print(hour_1 | hour_2)

# # intersection
# #
# # 앞뒤순서가 결과에 영향을 미치지 않음
# print(hour_1.intersection(hour_2))
# print(hour_2.intersection(hour_1))

# # & 연산자 사용 교집합
# print(hour_1 & hour_2)

# 3개의 print문은 공통으로 {"b2", "c3"} 출력

# 차집합
# 순서에 따라 결과가 다름
# 앞에 작성된 set에서
# diffrence의 인자로 전달된 셋에 있는 값들을
# 제외한 결과를 출력
# 연산자는 (-)

# print(hour_1.difference(hour_2))
# print(hour_2.difference(hour_1))

# line_a = {"S01", "S02", "S03", "S05"}
# line_b = {"S03", "S04", "S05"}
# print(line_a.intersection(line_b))
# print(line_a.difference(line_b))
# print(line_b.difference(line_a))

yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}
print(today - (yesterday))
print(today & (yesterday))
