# 실습 1. 딕셔너리 만들고 다루기

# 1) 센서명을, 키(key), 측정값을 값(value)으로 딕셔너리 저장
sensors = {"모터온도": 78, "진동": 0.5}

# 2) 키로 값을 꺼내고 새 키로 추가, 기존 키로 수정
print(sensors["진동"])  # 값 꺼내기
print(sensors.get("진동", 0))  # 값 더 안전하게 꺼내기

sensors["압력"] = 95  # 추가
sensors["진동"] = 0.3  # 있던 키를 언급하면 수정

print(sensors)

# 3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인

print(sensors.get("면적", -1))  # 면적 key는 존재하지 않아서 -1로 대체
print("진동" in sensors)  # 존재하는 key
print("면적" in sensors)  # 존재하지 않은 key


# 실습 2

# 1) 센서 딕셔너리와 새 데이터 딕셔너리를 각각 저장
sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 80, "유량": 42}

# 2) update로 새 데이터를 한 번에 반영
sensors.update(new_data)
print(sensors)

# 3) del로 특정 키를 삭제하고 len으로 개수 확인
del sensors["진동"]
print("센서수: ", len(sensors))


# 실습 3

# 1) 센서명-측정값 딕셔너리 저장
sensors = {"모터온도": 58.4, "면적": 76.7, "압력": 95}

# 2) values의 합을 개수로 나눠 평균 구하기
avg = sum(sensors.values()) / len(sensors)
print("평균", avg)

# 3) items로 순회하며 가장 큰 값과 그 센서명을 찾아 출력
# for name, value in sensors.items():


# 실습 4

# 1) 센서명 리스트와 측정값 리스트를 각각 저장
names = ["온도", "진동", "압력"]
values = [78, 0.5, 95]

# 2) zip으로 두 리스트를 짝지어 dict로 변환
sensors = dict(zip(names, values))
print(sensors)

# 3) items로 순회하며 이름, 값 쌍 출력
for name, value in sensors.items():
    print(name, value)
# 실습 5

# 실습 6

# 실습 7

# 실습 8
