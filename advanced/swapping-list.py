numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for i in range(len(numbers)//2):
     tmp = numbers[i]
     numbers[i] = numbers[len(numbers) - i - 1]
     numbers[len(numbers) - i - 1] = tmp

# 여기에 코드를 작성하세요

print("뒤집어진 리스트: " + str(numbers))