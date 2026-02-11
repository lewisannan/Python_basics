class Student:
    def __init__(self,Fullname,Course,Age,FeesPaid):
        self.Fullname = Fullname
        self.Course = Course
        self.Age = Age
        self.FeesPaid = FeesPaid

    def leadership(self):
        print("I am a student leader at our School. ")



Stu1 = Student("Hasfa Aisha","Medicine",24,56000)
print("My name is",Stu1.Fullname,"and I study",Stu1.Course,".","I am",Stu1.Age,"years old.","The school fees paid amounts to",Stu1.FeesPaid)
print()
Stu2 = Student("George Clinton","Law",26,66000)
print("My name is",Stu2.Fullname,"and I study",Stu2.Course,".","I am",Stu2.Age,"years old.","The school fees paid amounts to",Stu2.FeesPaid)
Stu2.leadership()
print()
Stu3 = Student("Alex Evelyn","Accounting",22,35000)
print("My name is",Stu3.Fullname,"and I study",Stu3.Course,".","I am",Stu3.Age,"years old.","The school fees paid amounts to",Stu3.FeesPaid)
print()
