class Person:
    def setName(self, name):
        self.name = name
    def getName(self, name):
        return self.name
    def greet(self):
        print('Hello, my name is %s'%self.name)
        
person1 = Person()
person2 = Person()

person1.setName("tae hee kim")
person2.setName('dong won kagn')

person1.greet()
person2.greet()