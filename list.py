numbers = [3, 5, 1, 65, 32, 78]

numbers.append(1) # 리스트에 요소 추가
len(numbers) # 리스트 길이 출력
del numbers[0] # 리스트 0번 인덱스 삭제
numbers.insert(0,1) # 0번 인덱스에 1 삽입, 원래 있던 값 보존
new_list = sorted(numbers) # numbers 리스트 순서대로 정렬
reverse_list = sorted(numbers, reverse=True) # numbers 리스트 순서대로 정렬
numbers.sort(reverse=True) # 리스트 정렬 / 역정렬
# sorted: 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# sort: 아무것도 리턴하지 않고, 기존 리스트를 정렬

