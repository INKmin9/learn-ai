# 자리수 합 리턴
def sum_digit(num):
    # 여기에 코드를 작성하세요
    if num < 10:
        return num
    elif num < 100:
        digit = num // 10 + num % 10
        return digit
    elif num <= 1000:
        digit = num // 100 + (num % 100) // 10 + (num % 10)
        return digit


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 여기에 코드를 작성하세요
total_sum = 0
for num in range(1, 1000):
    total_sum += sum_digit(num)

print(total_sum + 1)