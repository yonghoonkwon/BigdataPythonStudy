class Student:
    def __init__(self, name, hakbun):
        self.name = name
        self.hakbun = hakbun
    def info(self):
        print('Name: %s, hakbun: %s'%(self.name, self.hakbun))

student1 = Student('lg-1', 1)
student2 = Student('lg-2', 2)

student1.info()
student2.info()