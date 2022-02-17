# 시퀀스 형
# 컨테이너 : 서로 다른 자료형[list, tuple, collections, deque]
# Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes


# 지능형 리스트 (Comprehending Lists)

# Non Comprehending Lists

chars = '!@#$%^&*()_+'
codes1 = []
for s in chars:
  codes1.append(ord(s))    # 유니코드를 보여줌

print(codes1)
# Comprehending Lists
codes2 = [ord(s) for s in chars]

print(codes2)
# 조건을 추가하고 싶으면?
codes3 = [ord(s) for s in chars if ord(s) > 40]

print(codes3)

codes4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(codes4)

# Generator
import array
from audioop import reverse          # array 쓰려면 가져와야 하구나... 몰랐다

# Generator : 한번에 한개의 항목을 생성(메모리 유지 x)
tuple_g = (ord(s) for s in chars)
# Array
array_g = array.array('I', (ord(s) for s in chars))
print(tuple_g)    # 어떻게 생성 수식만 물고있고 next나 for문에서 사용되지 않으면 올리지 않는다.
print(next(tuple_g))
print(array_g)
print(array_g.tolist())

print()
print()




print(('%s ' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s ' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
  print(s)
  
  
# Tuple Advanced

# Packing & Unpacking

a, b = divmod(100, 9)
print(divmod(100, 9))
print(divmod(*(100, 9)))    # 이렇게 패킹된 것을 언패킹할 수 있다.
print(*divmod(100,9))       # 마지막에 언패킹된다.


x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1,2,3,4,5
print(x, y, rest)


# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]
print(l, m, id(l), id(m))
l = l * 2
m = m * 2
print(l, m, id(l), id(m))
l *= 2
m *= 2
print(l, m, id(l), id(m))     # 여기서 list의 id는 변하지 않는다. 수정 가능 - But 튜플은 새로 만들어진다.


# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'mandarin', 'lemon', 'strawberry']

# sorted : 정렬 후 '새로운' 객체를 반환

test = sorted(f_list)

print(test)
print(f_list)

print(sorted(f_list))                     # 알파벳 순
print(sorted(f_list, reverse=True))       # 알파벳 역순
print(sorted(f_list, key=len))            # 길이가 짧은 것부터 길 순서로 배열
print(sorted(f_list, key=lambda x:x[-1])) # 마지막 글자의 알파벳 순
print(f_list)     # 원본은 변경되지 않았다.

