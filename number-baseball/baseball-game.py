from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    while len(new_guess) < 3:
        num = int(input(f'{len(new_guess) + 1}번째 숫자를 입력하세요: '))
        if num in new_guess:
            print('중복되는 숫자입니다. 다시 입력하세요.')
        elif num > 9 or num < 0:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
        else:
            new_guess.append(num)
    return new_guess

def get_score(guesses, solution):  # 유저가 뽑은 것, 컴퓨터가 뽑은 것
    strike_count = 0
    ball_count = 0

    for i in range(len(guesses)):
        if guesses[i] in solution:
            if guesses[i] == solution[i]:
                strike_count += 1
            else:
                ball_count += 1
    return strike_count, ball_count

ANSWER = generate_numbers()
tries = 0

while True:
    GUESS = take_guess()  # 각 시도에서 새로운 추측을 입력받음
    strike_count, ball_count = get_score(GUESS, ANSWER)
    print('{}S {}B'.format(strike_count, ball_count))
    tries += 1

    if strike_count == 3:
        break  # strike_count가 3일 때 루프 종료

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))
