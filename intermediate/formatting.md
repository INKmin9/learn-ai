## 파이썬에서 문자열을 포매팅하는 세 가지 방법에 대해 알아보자

### `%`기호
```python
name = "최지용"
age = 32

print("제 이름은 $s이고 %d살입니다" %(name, age))
```
```python
제 이름은 최지웅이고 32살입니다.
```
이제는 잘 쓰지 않는 오래된 방식입니다. `%s`, `%d`와 같은 '포맷 스트링'이라는 것을 사용하는데, C나 자바 등 많은 언어들에서 이와 유사한 방식으로 문자열을 포매팅합니다. 

### `format()` 메소드
```python
name = "최지웅"
age = 32

print("제 이름은 {}이고 {}살입니다.".format(name, age))
```
```python
제 이름은 최지웅이고 32살입니다.
```
앞에서 배웠던 방식이다. 

### f-string
```python
name = "최지웅"
age = 32

print(f"제 이름은 {name}이고 {age}살입니다.")
```
```python
제 이름은 최지웅이고 32살입니다.
```
파이썬 3.6에서 추가된 문법이다. 훨씬 편리하므로 최근에 많이 사용한다. 