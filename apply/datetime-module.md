스탠다드 라이브러리에 있는 `datetime` 모듈은 '날짜'와 '시간'을 다루기 위한 다양한 '클래스'를 갖추고 있다. 
```python
import datetime
```
# `datetime`값 생성
2020년 3월 14일을 파이썬으로 어떻게 표현할 수 있을까?
```python
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))
```
```python
2020-03-14 00:00:00
<class 'datetime.datetime'>
```
보시다시피 시간은 자동으로 00시 00분 00초로 설정되었는데, 우리가 시간까지도 직접 정할 수 있습니다.
```python
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))
```
```python
2020-03-14 13:06:15
<class 'datetime.datetime'>
```
# 오늘 날짜
우리가 날짜와 시간을 정해 주는게 아니라, 코드를 실행한 '지금 이 순간'의 날짜와 시간을 받아올 수도 있다. 
```python
today = datetime.datetime.now()
print(today)
print(type(today))
```
```python
2020-04-05 17:49:12.360266
<class 'datetime.datetime'>
```

# `timedelta` 타입
두 `datetime` 값 사이의 기간을 알고싶으면, 마치 숫자 뺄셈을 하듯이 그냥 빼면 된다. 
```python
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))
```
```python
22 days, 4:42:57.360266
<class 'datetime.timedelta'>
```
보시다시피 두 `datetime`값을 빼면, `timedelta`라는 타입이 나오는데, 이건 날짜 간의 차이를 나타내는 타입이라고 생각하면 된다. 반대로 `timedelta`를 생성해서 `datetime`값에 더할 수 있다. 
```python
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)
```
```python
2020-04-05 17:54:24.221660
2020-04-10 21:05:14.221660
```
# `datetime` 해부하기
`datetime`값에서 '연도'나 '월'같은 값들을 추출하려면 어떻게 해야 할까?
```python
today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초
```
```python
2020-04-05 17:59:21.709817
2020
4
5
17
59
21
709817
```
# `datetime`포매팅

`datetime`값을 출력하면 별로 예쁘지 않다. 하지만 `strftime()`함수를 사용하면, 우리 입맛대로 바꿀 수 있다.
```python
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))
```
```python
2020-04-05 18:09:55.233501
Sunday, April 05th 2020
```
`%A`, `%B`, `%d`, `%Y`와 같은 걸 포맷 코드라 한다. 

| 포맷 코드  | 설명                                       | 예시       |
|--------|------------------------------------------|----------|
| %a     | 요일 (짧은 버전)                               | Mon      |
| %A     | 요일 (풀 버전)	                               | Monday   |
| %w     | 요일 (숫자 버전, 0~6, 0이 일요일)	                 | 5        |
| %d     | 일 (01~31)	                               | 23       |
| %b     | 월 (짧은 버전)	                               | Nov      |
| %B     | 월 (풀 버전)	                                | November |
| %m     | 월 (숫자 버전, 01~12)	                        | 10       |
| %y     | 연도 (짧은 버전)	                              | 16       |
| %Y     | 연도 (풀 버전)	                               | 2016     |
| %H     | 시간 (00~23)	                              | 14       |
| %I     | 시간 (00~12)	                              | 10       |
| %p     | AM/PM	                                   | AM       |
| %M     | 분 (00~59)	                               | 34       |
| %S     | 초 (00~59)	                               | 12       |
| %f     | 마이크로초 (000000~999999)	                   | 413215   |
| %Z     | 표준시간대	                                   | PST      |
| %j     | 1년 중 며칠째인지 (001~366)	                    | 162      |
| %U     | 1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	 | 35       |
| %W     | 1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	 | 35       |