class Subject:
    def __init__(self):
        self.score = None
        self.subject_name = None
        self.max_score = None
    
    def get_subject_name(self):
        return self.subject_name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score
    
    def get_max_score(self):
        return self.max_score
    
    def __add__(self, other):
        if issubclass(type(other), Subject):
            return self.score + other.score
        else:
            return self.score + other
    
    def __sub__(self, other):
        if issubclass(type(other), Subject):
            return self.score - other.score
        else:
            return self.score - other
        
    def __radd__(self, other):
        if issubclass(type(other), Subject):
            return self.score + other.score
        else:
            return self.score + other
    
    def __rsub__(self, other):
        if issubclass(type(other), Subject):
            return - self.score + other.score
        else:
            return - self.score + other
        
    def __iadd__(self, other):
        if issubclass(type(other), Subject):
            return self.score + other.score
        else:
            return self.score + other
    
    def __isub__(self, other):
        if issubclass(type(other), Subject):
            return self.score - other.score
        else:
            return self.score - other
    
    def __pos__(self):
        return self.score
    
    def __neg__(self):
        return -self.score
    

class Korean(Subject):
    def __init__(self):
        super().__init__()
        self.max_score = 100
        self.subject_name = "국어"

class Math(Subject):
    def __init__(self):
        super().__init__()
        self.max_score = 100
        self.subject_name = "수학"

class History(Subject):
    def __init__(self):
        super().__init__()
        self.max_score = 50
        self.subject_name = "역사"

class Student:
    def __init__(self, name):
        self.name = name
        self.kor = Korean()
        self.math = Math()
        self.his = History()
        self.subjects = [self.kor,
                         self.math,
                         self.his]
    def get_name(self):
        return self.name
    
    def make_sum(self):
        return sum(self.subjects)
    
    def print(self):
        print("===== Student", self.name, " =====")
        for i in range(3):
            print(["국어", "수학", "역사"][i], ":", self.subjects[i].score, "/", self.subjects[i].max_score)

    def __lt__(self, other):
        return sum(self.subjects) < sum(other.subjects)
    def __le__(self, other):
        return sum(self.subjects) <= sum(other.subjects)
    def __gt__(self, other):
        return sum(self.subjects) > sum(other.subjects)
    def __ge__(self, other):
        return sum(self.subjects) >= sum(other.subjects)
    def __eq__(self, other):
        return sum(self.subjects) == sum(other.subjects)
    def __ne__(self, other):
        return sum(self.subjects) != sum(other.subjects)
        
def print_rank(students):
    temp = sorted(students, reverse=True)
    for i in range(len(students)):
        print("Rank ", i+1, " :  ", temp[i].name, "  ( ", sum(temp[i].subjects), " / ", 
              sum((i.max_score for i in temp[i].subjects)), ")", sep='')

if __name__ == "__main__":
    n = int(input("How many students: ")) 
    students = []
    
    for i in range(n):
        name = input("Name of Students: ") 
        student = Student(name)

        for subject in student.subjects:
            score = int(input("Score of %s : " %subject.get_subject_name())) 
            subject.set_score(score)
        
        print() 
        student.print() 
        print()
        students.append(student) 

    print("===== Rank =====") 
    print_rank(students)