
class Student(object):
  """
  Student Class
  Author : Kim
  Date : 2022.02.16
  Description : Class, Static, Instance Method
  """
  
  # Class Variable
  tuition_per = 1.0
  
  def __init__(self, id, first_name, last_name, email, grade, tuition_per, gpa):
    self._id = id
    self._first_name = first_name
    self._last_name = last_name
    self._emamil = email
    self._grade = grade
    self._tuition = tuition_per
    self._gpa = gpa
  
  # Instance Method
  def full_name(self):
    return '{}, {}'.format(self._first_name, self._last_name)
  
  def detail_info(self):
    return 'Student Detail Info : {} {} {} {} {} {}'.format(self._id, self.full_name(), self._emamil, self._grade, self._tuition, self._gpa)
  
  # Instance Mehod
  def get_fee(self):
    return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)
  
  # Instance Mehod
  def get_fee_culc(self):
    return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)
  
  def __str__(self):
    return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._emamil)

  # Class Method
  @classmethod
  def raise_fee(cls, per):
    if per <= 1:
      print('Please Enter 1 or More')
      return
    cls.tuition_per = per
    # Student.tuition_per = per 과 같다
    # cls == Student
    print('Success')

  @classmethod
  def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
    return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)
  
  @staticmethod
  def is_scholarshop_st(inst):
    if inst._gpa >= 4.0:
      return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry, Not a scholarship recipient'
    
student_1 = Student(1, 'Kim', 'Donghyun', 'kimvjgd@naver.com', '1', 400, 4.3)
student_2 = Student(2, 'Lee', 'Youngho', 'leelee@naver.com', '2', 500, 2.3)

# print(student_1.__dict__)
# print(student_2.__dict__)
print(student_1)
print(student_2)

print(student_1.detail_info())
print(student_2.detail_info())

print(student_1.get_fee())
print(student_2.get_fee())

# 학비 정보 인상 후
# Student.tuition_per = 1.2
Student.raise_fee(1.5)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

# 클래스 메서드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'Student3@gdsa.com', '3', 550, 1.1)
student_4 = Student.student_const(4, 'Park', 'Gayoung', 'Student3@gdsa.com', '4', 300, 1.3)

# 전체정보
print(student_3.detail_info())
print(student_4.detail_info())

# 학생 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)

# 장학금 혜택 여부(스테이틱 메서드 사용)
print(Student.is_scholarshop_st(student_1))
print(student_2.is_scholarshop_st(student_2))
print(Student.is_scholarshop_st(student_3))
print(student_3.is_scholarshop_st(student_4))

