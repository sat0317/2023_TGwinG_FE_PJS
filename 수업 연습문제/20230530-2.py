class Person:
    def __init__(self, name, age, studentid):
        self.name = name
        self.age = age
        self.studentid = studentid

class TGWinG:
    def Role(self, role):
        self.role = role
    def IsWork(self):
        if self.role == "쩌리":
            print(f"{self.name}은(는) 일을 안 합니다.")
        else:
            print(f"{self.name}은(는) 일을 합니다.")
    def IsFresh(self):
        if self.age == 20:
            print(f"{self.age}은(는) 신입생입니다.")
        elif self.age <=25:
            print(f"{self.age}은(는) 재학생입니다.")
        else:
            print(f"{self.age}은(는) 재학생 중에서도 화석입니다.")