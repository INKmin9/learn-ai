# Optional Parameter

파라미터에 '기본값(default value)'을 설정할 수 있는데, 기본값을 설정해 두면, 함수를 호출할 때 파라미터에 값을 꼭 넘겨주지 않아도 된다. 이런 파라미터를  '옵셔널 파라미터(optional parameter)'라 한다. 필수가 아니니 옵셔널이라 하는 것. 

아래 코드를 보면 `myself()`함수를 호출할 때 한 번은 파라미터 `nationality`에 들어갈 값을 제공했고, 한 번은 제공하지 않았다. 각각 어떻게 출력되는지 확인하자. 

```python
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터에 값을 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터에 값을 제공하지 않는 경우
```
```python
내 이름은 코드잇
나이는 1살
국적은 미국

내 이름은 코드잇
나이는 1살
국적은 한국
```

## 옵셔널 파라미터는 꼭 마지막에!

참고로 옵셔널 파라미터는 모두 마지막에 있어야 한다. 아래처럼 옵셔널 파라미터를 중간에 껴넣으면 오류가 발생한다..
```python
def myself(name, nationality="한국", age):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때
```
```python
# Error
File "myself.py", line 1
     def myself(name, nationality = "한국", age):
               ^
SyntaxError: non-default argument follows default argument
```

# Syntactic Sugar
자주 쓰이는 표현을 더 간략하게 쓸 수 있게 하는 문법을 'Syntactic Sugar'라고 한다. 

```python
# 다음 두 줄은 같습니다
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7
```

앞으로 `x += 1`과 같은 문법을 자주 보게 될 텐데, 자주 사용하시길..