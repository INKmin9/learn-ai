name = "최지웅"
age = 32
num_1 = 1
num_2 = 3

# format mtd : num1/num2를 소수점 2자기까지 표기하는 방법
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))
print("제 이름은 {}이고 {}살입니다.".format(name, age))

# %기호
print("제 이름은 %s이고 %d살입니다." % (name, age))

# f-string
print(f"제 이름은 {name}이고 {age}살입니다.")
