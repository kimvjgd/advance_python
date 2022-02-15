# Chapter01-1
# 파이썬 심화
# OOP - 코드의 재사영, 코드 중복 방지
# 클래스 상세설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

class Student():
  """
  Student Class
  Author : Kim
  Date : 2022.02.15
  """
  # 클래스 변수
  student_count = 0
  
  def __init__(self, name, number, grade, details, email=None):
    # 인스턴스 변수
    self._name = name
    self._number = number
    self._grade = grade
    self._details = details
    self._email = email
    
    Student.student_count += 1
    
  
  def __str__(self):
    return 'str : {}'.format(self._name)
  
  def __repr__(self):
    return 'repr : {}'.format(self._name)
  
  def detail_info(self):
    print('Current Id : {}'.format(id(self)))
    print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))
  
  def __del__(self):
    Student.student_count -= 1
  
student1 = Student('Kim', 1, 1, {'gender':'Male', 'score1':95, 'score2':86}, )
student2 = Student('Lee', 2, 2, {'gender':'Male', 'score1':95, 'score2':86})
student3 = Student('Choi', 3, 3, {'gender':'Male', 'score1':95, 'score2':86})

print(dir(student1))
print()
print()
print(student1.__dict__)
print()
print()

# Docstring
print(Student.__doc__)

Student.detail_info(student1)

print()
print()
print()
print()


# 비교
print(student1.__class__)
print(student2.__class__)
print(id(student1.__class__)==id(student2.__class__))
print()

# 인스턴스 변수는 직접 접근을 권장하지 않는다.
