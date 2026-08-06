# 실습 2)
def sensor_temp(machine, temp):
    print(machine, temp, "도")


sensor_temp("모터", 78)  # 모터 78도
sensor_temp("펌프", 92)  # 펌프 92도

sensor_temp(78, "모터")


# 실습 3)
def sensor_temp(machine, temp):
    print(machine, temp)


sensor_temp(machine="모터", temp=78)  # 모터 78
sensor_temp(temp=92, machine="펌프")  # 펌프 92

sensor_temp("모터", temp=78)  # 모터 78
