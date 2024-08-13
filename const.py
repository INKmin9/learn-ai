# 상수 (constant)
PI=3.14 # 수정되지 않는 값이라 약속한다. 

def calculate_area(r):
    return r*r*PI

radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

PI=3 #되도록이면 안하는걸 추천
radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
