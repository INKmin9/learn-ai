# 리스트에서 값의 존재 확인하기
어떤 값이 리스트에 있는지 확인하는 함수를 보자. 
```python
# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))
```
```python
True
False
```
쓰는 데 아주 어렵진 않다. 하지만 내장함수 `in`을 통해 더 쉽게 접근 가능하다. 
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)
```
```python
True
False
```

# 리스트 안의 리스트(Nested List)
리스트 안에는 또 다른 리스트가 있을 수 있다. 이를 영어로 **Nested List** 라 부른다.
```python
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)
```
```python
[62, 75, 77]
[85, 91, 89]
62
91
75.0
```

# `sort` 메소드
저번에 정렬된 *새로운*리스트를 리턴시켜주는 `sorted`함수를 봤다. `some_list.sort()`는 새로운 리스트를 생성하지 않고 `some_list`를 정렬된 상태로 바꿔준다.
```python
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)
```
```python
[1, 3, 5, 7]
```

# `reverse` 메소드
`some_list.reverse()`는 `some_list`의 원소들을 뒤집어진 순서로 배치한다. 
```python
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)
```
```python
[1, 7, 3, 5]
```

# `index` 메소드
`some_list.index(x)`는 `some_list`의 `x`의 값을 갖고 있는 원소의 인덱스를 리턴해준다.  
```python
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))
```
```python
1
2
```

# `remove` 메소드
`some_list.index(x)`는 `some_list`에서 첫 번째로 `x`의 값을 갖고 있는 원소를 삭제한다.  
```python
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)
```
```python
['딸기', '당근', '수박', '참외', '메론']
```