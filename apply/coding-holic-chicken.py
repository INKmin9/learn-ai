with open('file/chicken.txt', 'r', encoding='UTF-8') as f:
    total_revenue = 0
    total_days = 0
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출
        total_days += 1
        total_revenue += revenue
    print(total_revenue / total_days)