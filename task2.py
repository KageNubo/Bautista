class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I'm studying {self.course}.")


student1 = Student("Reymart Tibe", 25, "PMA (Pedicure, Manicure, and Arot)")
student2 = Student("Marvie Urmenita", 18, "Information Technology")
student3 = Student("John Kian Shane Tejano", 23, "MassComm")


student1.introduce()
student2.introduce()
student3.introduce()