import random
answer = random.randint(1, 20)

flag = 1
for i in range(4):
    number = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(4-i)))
    if number == answer:
        flag = 0
        break
    elif number < answer:
        print('Up')
    elif number > answer:
        print('Down')

if flag == 0:
    print('축하합니다. {}번만에 숫자를 맞히셨습니다.'.format(i + 1))
else:
    print("아쉽습니다. 정답은 {}였습니다.".format(answer))