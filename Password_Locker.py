# #class Student:

#     #school_name = "GBHS"
#     #def __init__(self, name, marks):
#         #self.name = name
#         #self.marks = marks
    
#     #def welcome(self):
#         #print("Welcome", self.name)

#     #def get_marks(self):
#         #return self.marks

# #s1 = Student("Ammad", 94)
# #print(s1.name, s1.marks, s1.school_name)
# #s1.welcome()
# #print(s1.get_marks())

# #s2 = Student("Hammad", 90)
# #print(s2.name, s2.marks, s2.school_name)
# #s1.welcome()





# class Student:

#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def avg(self):

#         avg = (student.marks1 + student.marks2 + student.marks3) / 3
#         return avg

# student = Student(str(input("Name: ")), int(input("Sub1: ")), int(input("Sub2: ")), int(input("Sub3: ")))
# #marks1 = Student(int(input("Sub2: ")))
# #marks2 = Student(int(input("Sub2: ")))
# #marks3 = Student(int(input("Sub3: ")))

# print(student.name, "your avg is", student.avg()) # ----> OUTPUT =    Ammad your avg is 200






class Student:

    @staticmethod
    def hello():
        print("Hello kiddo" + ', ', end= '',)

    def __init__(self, name, list):
        self.name = name
        self.list = list

    def avg(self):

        sum = 0

        for val in self.list:
            sum += val
        avg = sum/3
        return avg

name = input("Name: ")
sub1 = int(input("Sub1: "))
sub2 = int(input("Sub2: "))
sub3 = int(input("Sub3: "))

list = [sub1, sub2, sub3]

student = Student(name, list)

print(student.hello(), student.name, "your avg is", student.avg()) # ----> OUTPUT =    Hello kiddo your avg is 200