# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과로 반환 가능

# 함수 객체 예제

def factorial(n):
  """Factorial Function -> n:int"""
  if n==1:
    return 1
  return n * factorial(n-1)


class A:
  pass


print(factorial(5))
print(factorial.__doc__)
print(set(dir(factorial))-set(dir(A)))    # factorial이 갖는 메서드만 보고 싶다? 차집합으로 보여줄 수 있다.
print(factorial.__name__)                 # 함수의 이름

# 변수 할당
var_func = factorial
print(var_func(5))
print(list(map(var_func, range(1,6))))    # 1!, 2!, 3!, 4!, 5!을 모두 보여준다.


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher order function)

print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

# reduce()
from functools import reduce
from operator import add

print(reduce(add, range(1,11)))
# 1을 넣어서 add하고 reduce에 저장 -> 2를 넣고 reduce에 add하고 저장 .....-> 
# print(sum(range(1,11)))  이러면 쉽긴하지만... 나중에 reduce 쓰일 수 있다.

# 익명합수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1,11)))

# Callable : 호출 연산자 -> 메서드 형태로 호출 가능한지 확인

import random

# 로또 추첨 클래스 선언
class LottoGame:
  def __init__(self):
    self._balls = [n for n in range(1, 46)]
  
  def pick(self):
    random.shuffle(self._balls)
    return sorted([random.choice(self._balls) for n in range(6)])
  
  def __call__(self):
    return self.pick()
 
game = LottoGame()

# 함수로서 사용할 수 있는지 보자.
print(callable(str), callable(list), callable(factorial), callable(3.14), callable(game))

print(game.pick())
print(game())
print(callable(game))


# 다양한 매개변수 입력(*args, **kwargs)
def args_test(name, *contents, point=None, **attrs):
  return '<args_test> -> ({})({})({})({})'.format(name, contents, point, attrs)

print(args_test('test1'))
print(args_test('test1', 'test2'))
print(args_test('test1', 'test2', 'test3', id='admin'))

# 함수 Signatures
# 함수의 인자에 대한 정보를 표시해주는 클래스 형태의 메서드
from inspect import signature

sg = signature(args_test)
print(sg)
print(sg.parameters)

# 모든 정보 출력
for name, param in sg.parameters.items():
  print(name, param.kind, param.default)

print()
print()
print()
print()


# partial 사용법 : 인수 고정해서 새로운 값을 리턴해준다.
# 주로 특정 인수 고정 후 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10, 100))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)
print(five(100))
print(six())   # 5 * 6
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1,11))))