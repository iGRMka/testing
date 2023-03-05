#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#methods, class variables, instance variables, constructor etc
#objects for Ur classes
#methods=functions, but inside the class


#self word is mandatory for calling variables names into method
#instance and class variables have whole defferent purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100 #class variables
    #default constructor
    def __init__(self, a, b):
        self.firstNumber = a #instance variable
        self.secondNumber = b #instance variable
        print("I'm called automatically when object is created")

    def getData(self):
        print("I'm now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num  #or self.num=Calculator.num


obj = Calculator(2, 3) #syntax to create objects in python
obj.getData()
print(obj.Summation())


obj1 = Calculator(4, 5) #syntax to create objects in python
obj1.getData()
print(obj1.Summation())



