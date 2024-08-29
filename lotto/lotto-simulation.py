from random import randint

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    if winning_numbers[6] in numbers:
        for i in range(len(numbers)):
            if numbers[i] in winning_numbers[:6]:
                count += 1
        if count == 5:
            return count + 2

    else:
        for i in range(len(numbers)):
            if numbers[i] in winning_numbers[:6]:
                count += 1
        return count


# 위닝 넘버에 있는 맨 마지막 숫자를 특별하게 생각해야함..
# 일단 들어갔을 때 보너스 숫자와 일치하는게 있다 / 없다 로 구분
# 있을 경우, 나머지 숫자와 비교하여 숫자 셈하기. -> 5개 일치 >> 7반환(+2) / 불일치 >> 1반환(-4)
# 없을 경우 평범하게 셈한다.

def check(numbers, winning_numbers):
    winning_check = count_matching_numbers(numbers, winning_numbers)
    if winning_check == 6:
        return 10000000000
    elif winning_check == 5:
        return 1000000
    elif winning_check == 4:
        return 50000
    elif winning_check == 3:
        return 5000
    elif winning_check == 7: # 보너스 번호
        return 50000000
    else:
        return 0


print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))