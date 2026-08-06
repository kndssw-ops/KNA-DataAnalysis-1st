first_name = "Ned"
middle_name = "J"
last_name = "Park"
print(first_name)
print(middle_name)
print(last_name)


def say_hello():
    print("안녕하세요")


say_hello()


# 함수 안에서 벌어지는 일들을 만들어봅시다



def show_number():
    my_number = 44
    print(f"my_number: {my_number}")


# 위 함수를 실행해봅시다
show_number()

# 여기서도 my_number 값을 정해봅시다
# 아랫줄의 my_number는 show_number함수 안의 my_number와 다른 존재
my_number = 24
show_number()

# 그래서 함수안의 my_number 데이터가 영향을 끼치는 범위를
# 전문용어로 스코프(scope)라고 부른다

# 실습1: 답안
def startChecking():
    
