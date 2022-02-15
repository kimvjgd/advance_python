# Chapter01-1
# 파이썬 심화
# OOP - 코드의 재사영, 코드 중복 방지
# 클래스 상세설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

class Student():
  def __init__(self, name, number, grade, details):
    self._name = name
    self._number = number
    self._grade = grade
    self._details = details
  
  def __str__(self):
    return 'str : {}'.format(self._name)
  
  def __repr__(self):
    return 'repr : {}'.format(self._name)
    
  
student1 = Student('Kim', 1, 1, {'gender':'Male', 'score1':95, 'score2':86})
student2 = Student('Lee', 2, 2, {'gender':'Male', 'score1':95, 'score2':86})
student3 = Student('Choi', 3, 3, {'gender':'Male', 'score1':95, 'score2':86})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print(students_list)

for x in students_list:
  print(x)
