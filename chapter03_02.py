# 헤시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 x, Set -> 중복허용 x
# Dict 및 Set 심화

# Dict 구조

print(__builtins__.__dict__)   # dictionary형태의 python 내장 메서드들을 보여준다.\
  

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])     # list 변경가능해서 유니크한 값을 생성할 수 없다.

print(hash(t1))
# print(hash(t2))               # 에러난다.


# 지능형 딕셔너리(Comprehending Dict)
import csv
# 외부 CSV to List of tuple

with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
  temp = csv.reader(f)
  # Header Skip
  next(temp)
  # 변환
  NA_CODES = [tuple(x) for x in temp]
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}
print()
print()
print(n_code1)
print(n_code2)


# Dict Setdefault 예제
source = (
  ('k1', 'val1'),
  ('k1', 'val2'),
  ('k2', 'val3'),
  ('k2', 'val4'),
  ('k2', 'val5')
)
# key 값이 중복되면 어떻게 해야할까?
new_dict1 = {}
# No user setdefault
for k, v in source:
  if k in new_dict1:
    new_dict1[k].append(v)
  else:
    new_dict1[k] = [v]
print(new_dict1)
  
# Use setdefault
new_dict2 = {}

for k, v in source:
  new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):
  def __missing__(self, key):
    print('Called : __missing__')
    if isinstance(key, str):
      raise KeyError(key)
    return self[str(key)]
  def get(self, key, default=None):
    print('Called : __getitem__')
    try:
      return self[key]
    except KeyError:
      return default
  def __contains__(self, key):
    print('Called : __contains__')
    return key in self.keys() or str(key) in self.keys()
  
user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one':1, 'two':2})
user_dict3 = UserDict([('one',1),('two',2)])
# 출력
print(user_dict1)
print(user_dict2)
print(user_dict3)
print(user_dict2.get('two'))
print(user_dict2.get('aaa'))    # user_dict2['three']같이 직접적으로 접근하면 없으면 에러 -> get으로 안전하게 불러와야함  
print('one' in user_dict3)


# dictionary는 원래 가변적이다.
a = {'name': 'kim'}
a['name'] = 'park'
print(a)

print()
print()
print()
# immutable Dict    불변적인 dictionary를 사용하고 싶다?
from types import MappingProxyType

d = {'key1': 'TEST1'}
# Read Only
d_frozen = MappingProxyType(d)
print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# d_frozen['key1'] = 'TEST2'

print()
print()

# Set 구조(FrozenSet)
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})    # 중요한 데이터여서 얼린다. 수정 추가 삭제 x

# 추가
s1.add('Melon')
# s5.add('melon')
print(s1, type(s1))
print(s5, type(s5))



# 지능형 집합(Comprehending Set)
from unicodedata import name

print({chr(i) for i in range(0, 256)})