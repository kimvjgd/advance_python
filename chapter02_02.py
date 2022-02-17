# Chapter02-2
# 파이썬 심화

# 매직메서드 심화
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions) ,클래스(Class)

# 매직메서드 기초 설명

# 기본형
print(int)

# 모든 속성 및 메서드 출력
print(dir(int))

print()
print()
print()

n = 100
print(n + 200)
print(n.__add__(200))    # 위의 +를 쓰는 순간 파이썬에서 내부적으로 __add__ 매직 메서드가 실행된다.
print(n.__doc__)

print(n.__bool__(), bool(n))  # 다 같은 의미이다.
print(n*100, n.__mul__(100))


print()
print()
print()
print()
print()
print()
# 클래스 예제
class Student:
  def __init__(self,name, height):
    self._name = name
    self._height = height
    
  def __str__(self):
    return 'Student Class Info : {}, {}'.format(self._name, self._height)
  
  def __ge__(self,x):
    print('Called. >> __ge__Method')
    if self._height >= x._height:
      return True
    else:
      return False
    
  def __le__(self,x):
    print('Called. >> __le__Method')
    if self._height <= x._height:
      return True
    else:
      return False
  
  def __sub__(self, x):
    print('Called. >> __sub__Method')
    return self._height - x._height
    
  
s1 = Student('James', 181)
s2 = Student('Linda', 163)

# print(s1 + s2) 이건 당연히 안되지
# print(s1._height + s2._height) # 이건 당연히 가능

# 매직 메서드 출력
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)

# 벡터(Vector) 
class Vector(object):
  def __init__(self, *args):
    '''Create a vector, example : v = Vector(1,2)'''
    if len(args) == 0:
      self._x, self._y = 0, 0
    else:
      self._x, self._y = args
    
  def __repr__(self):
    """Returns the vector informations"""
    return 'Vector(%r, %r)' %(self._x, self._y)
  
  def __add__(self, other):
    return Vector(self._x + other._x, self._y + other._y)

  def __mul__(self, y):
    return Vector(self._x * y, self._y * y)
  
  def __bool__(self):
    return bool(max(self._x, self._y))
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()  # 0,0 으로

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(v1,v2,v3)
print(v1+v2)
print(v1*4)
print(bool(v1), bool(v2), bool(v3))   # 0 0아니면 True가 나온다.