## `break`문
만약 `while`문의 조건 부분과 상관없이 반복문에서 나오고 싶으면, `break`문을 사용한다. 
```python
i = 100

while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)
```
```python
115
```

## `continue`문
현재 진행되고 있는 작동 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 `continue`문을 쓰면 된다.
```python
i = 0

while i < 15:
    i = i + 1

    # i가 홀수면 print(i)하지 않고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)
```
```python
2
4
6
8
10
12
14
```