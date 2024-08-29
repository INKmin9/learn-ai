import random

def generate_numbers(n):
    random_list = []
    while len(random_list) < n:
        random_number = random.randint(1, 45)
        if random_number not in random_list:
            random_list.append(random_number)
    return random_list

print(generate_numbers(6))

