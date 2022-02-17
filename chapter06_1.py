# # 객체 슬라이싱

# class Objects:
#   def __init__(self):
#     self._numbers = [n for n in range(1, 10000, 3)]
    
#   def __len__(self):
#     return len(self._numbers)
  
#   def __getitem__(self, idx):
#     return self._numbers[idx]
    
# s = Objects()
# print(s.__dict__)
# print(len(s))
# print(s[1:100])








# 파이썬 추상 클래스

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 함
# 개발과 관련된 공통된 내용(필드, 메서드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것


# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contain__ 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜
class IterTestA():
  def __getitem__(self, idx):
    return range(1, 50, 2)[idx]

i1 = IterTestA()
print(i1[4])

# Sequence 상속
# 요구사항인 추상메서드를 모두 구현해야 동작

from collections.abc import Sequence