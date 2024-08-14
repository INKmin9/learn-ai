# while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 코드를 작성해 보세요.

sum_of_multiples = 0
for i in range(1, 1000):
    if i % 2 == 0 or i % 3 == 0:
        sum_of_multiples += i

print(sum_of_multiples)