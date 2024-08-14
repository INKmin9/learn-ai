리스트와 문자열은 굉장히 비슷하다. 리스트가 어떤 자료형들의 나열이라면, 문자열은 문자들의 나열이라고 할 수 있다. 지금부터 파이썬에서 리스트와 문자열이 어떻게 같고 어떻게 다른지 알아보자.

# 인덱싱(Indexing)
두 자료형은 공통적으로 인덱싱이 가능하다. 
```python
# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])
```
```python
A
B
E
J
A
B
E
J
```
# for 반복문
두 자료형은 공통적으로 인덱싱이 가능하다. 따라서 for문에도 활용할 수 있다. 
```python
# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)
```
```python
C
O
D
E
I
T

C
O
D
E
I
T
```
# 슬라이싱(Slicing)
두 자료형은 공통적으로 슬라이싱이 가능하다. 
```python
# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])
```
```python
['A', 'B', 'C', 'D', 'E']
['E', 'F', 'G', 'H', 'I', 'J']
['A', 'B', 'C', 'D']
ABCDE
EFGHIJ
ABCD
```
# 덧셈 연산
두 자료형에게 모두 덧셈은 "연결"하는 연산이다. 
```python
# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)
```
```python
[1, 2, 3, 4, 5, 6, 7, 8]
12345678
```

# len함수
두 자료형은 모두길이를 재는 `len`함수를 쓸 수 있다. 
```python
# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))
```
```python
5
13
```

# Mutable (수정 가능) vs. Immutable (수정 불가능)
하지만 차이점이 있다. 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없다는 것이다. 리스트와 같이 수정 가능한 자료형을 'mutable'한 자료형이라고 부르고, 문자열과 같이 수정 불가능한 자료형을 'immutable'한 자료형이라고 부른다. 숫자, 불, 문자열은 모두 immutable한 자료형이다. 
```python
# 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)
```
```python
[5, 2, 3, 4]
```

리스트 `numbers`의 인덱스 `0`에 `5`를 새롭게 지정했다. `[5, 2, 3, 4]`가 출력되었다. 이처럼 리스트는 데이터의 생성, 삭제, 수정이 가능하다. 
```python
# 문자열 데이터 바꾸기
name = "codeit"
name[0] = "C"
print(name)
```
```python
# Error
Traceback (most recent call last):
  File "untitled.py", line 3, in <module>
    name[0] = "C"
TypeError: 'str' object does not support item assignment
```
문자열 `name`의 인덱스 `0`에 `"C"`를 새롭게 지정해주었더니 오류가 나왔다. `TypeError: 'str' object does not support item assignment`는 문자열은 변형이 불가능하다는 메세지다. 이처럼 문자열은 리스트와 달리 데이터의 생성, 삭제, 수정이 불가하다. 