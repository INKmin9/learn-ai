# r은 read의 약자, w은 write의 약자
with open('chicken.txt', 'r', encoding='UTF-8') as f:
    print(type(f))
    for line in f:
        print(line) # 모든 줄 출력