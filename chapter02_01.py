# Chapter02 -1 
# 파이썬 심ㅘ
# 데이터 모델(Data Model)

# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions) ,클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value




# 두 점 사이의 거리를 구해보자 
# 1. 일반적인 튜플
# 일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
from math import sqrt
line_len1 = sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)
print('일반적인 튜플')
print(line_len1)

# 2. 네임트 튜플
# 네임트 튜플 사용
# 일반적인 튜플은 뭐가 뭔지 모르게 된다. 지금은 뭐 x, y... 로 쉽지만 변수가 많아지고 개념이 복잡해지면 힘들다.
from collections import namedtuple

# 네임트 튜플 선언
Point = namedtuple('point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
line_len2 = sqrt((pt2.x-pt1.x)**2 + (pt2.y-pt1.y)**2)
print('네임드 튜플')
print(line_len2)


Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False

# Dict to Unpacking
temp_dict = {'x':75, 'y':55}

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)    # 이렇게 안하면 x에 다 들어가게 돼서 오류가 나다.
print(p1,p2,p3,p4, p5)

print(p1[0]+p2[1])  # Index Error 주의
print(p1.x+p2.y)    # 클래스 변수 접근 방식

# Unpacking
x, y = p3
print(x + y)

# 네임드 튜플 메서드
temp = [52, 38]

# _make(): 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p1._fields,p2._fields,p3._fields)

# _asdict() : OrderedDict 반환   - dictionary형식으로 반환한다.
print(p1._asdict(), p4._asdict())
print(dict(p1._asdict()))

# _replace() : tuple은 불변 - 수정된 새로운 객체를 반환한다.
print(p2._replace(y=100))
print(p2)



# 실 사용 실습
# 학생 전체 그룹 생성
# 반 20명, 4개의 반 -> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언 with list_comprehension
numbers = [str(n) for n in range(1, 21)]

ranks = 'A B C D'.split()   # list로 만들어줬다.

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students[37].rank)

for s in students:
  print(s)