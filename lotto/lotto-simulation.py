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
    for i in range(len(numbers)):
        if numbers[i] in winning_numbers:
            count += 1
    return count


print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))