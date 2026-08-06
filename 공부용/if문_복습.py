# score = 80

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


dict = {
    "가": 50,
    "나": 40,
    "다": 30,
}

max_value = 50
max_key = ""

for key, value in dict.items():
    if max_value > value:
        max_value = value
        max_key = key

print("최대값: ", max_value, "최대값받은놈: ", max_key)
