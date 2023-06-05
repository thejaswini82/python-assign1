class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

# code to test

student = Student()

student.setName("John")
print(student.getName())  # Output: John

student.setRollNumber("12345")
print(student.getRollNumber())  # Output: 12345
