# 파이썬 변수 범위(global)

# b = 10

# def func_v(a):
#   print(a)
#   print(b)
#   b = 5
  
# func_v(5)

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언된 연결된 정보을 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메서드에 직접 접근이 가능하다.

a = 10
print(a+10)   # 20
print(a+100)  # 110  위의 식은 누적이 되지 않는다.

print('\n\n')

class Averager():
  def __init__(self):
    self._series = []
  
  def __call__(self, v):
    self._series.append(v)
    print('class >> {} / {}'.format(self._series, len(self._series)))
    return sum(self._series) / len(self._series)

# 인스턴스 생성
avg_cls = Averager()

print(avg_cls(15))    # 15 / 1 = 15
print(avg_cls(35))    # (15+35) / 2 = 25
print(avg_cls(40))    # (15+35+40) / 3 = 30


# 클로저(Closure) 사용
def closure_avg1():
  # Free variable(내부영역과 외부영역의 사이)
  series = []
  # 클로져 영역
  def avarager(v):
    series.append(v)
    print('def >> {} / {}'.format(series, len(series)))
    return sum(series) / len(series)
  return avarager

avg_closure1 = closure_avg1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print(avg_closure1.__code__.co_freevars)
# 위는 어떠한 free variable을 사용하는지 보여준다.

def closure_avg2():
  # Free variable
  cnt = 0
  total = 0
  # 클로저 영역
  def averager(v):
    nonlocal cnt, total
    cnt += 1
    total += v
    return total / cnt
  return averager

avg_closure2 = closure_avg2()

print(avg_closure2(10))
print(avg_closure2(20))
print(avg_closure2(30))
print(avg_closure2(40))




# 데코레이터 실습
import time
def perf_clock(func):
  def perf_clocked(*args):
    # 시작 시간
    st = time.perf_counter()
    result = func(*args)
    # 종료 시간
    et = time.perf_counter() - st
    # 함수명
    name = func.__name__
    # 매개변수
    arg_str = ','.join(repr(arg) for arg in args)
    # 출력
    print('[%0.5fs] %s(%s) -> %r' %(et, name, arg_str, result))
    return result
  return perf_clocked

# def time_func(seconds):
#   time.sleep(seconds)
  
# def sum_func(*numbers):
#   return sum(numbers)

# def fact_func(n):
#   return 1 if n<2 else n * fact_func(n-1)



#  데코레이터 미사용
# non_deco1 = perf_clock(time_func)
# non_deco2 = perf_clock(sum_func)
# non_deco3 = perf_clock(fact_func)


# 데코레이터 사용
@perf_clock
def time_func(seconds):
  time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
  return sum(numbers)

@perf_clock
def fact_func(n):
  return 1 if n<2 else n * fact_func(n-1)


non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

non_deco1(2)
non_deco2(100, 200, 300, 500)
non_deco3(100)

