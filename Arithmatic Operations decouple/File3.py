from File1 import ClassA
from File2 import ClassB

class ClassC(ClassB):

    def __init__(self,ClassB):
        self.var3= ClassB.var1
        self.var4= ClassB.var2
        print(self.var3)#testing
        print(self.var4)#testing

    def checkWholeNumber(self):
        if self.var3%2 ==0 or (self.var3+1)%2 & self.var4%2 == 0 or (self.var4+1)%2:
            print(self.var3) #if value is whole then it will print some value or will throw exception
            return True
        return False
    def addDictAndAss(self):
        myDict={}
        myDict["x"]=self.var3
        myDict["y"]=self.var4
        print(myDict) #to check whether values are added or not
        print("Please select one arithmatic operator i.e. '+','-','/','*'")
        operator=input()
        if operator == '+':
            add=ClassA.addition(**myDict)
            print(add)
        elif operator == '-':
            sub=ClassA.substraction(**myDict)
            print(sub)
        elif operator == '/':
            div=ClassA.division(**myDict)
            print(div)
        elif operator == '*':
            mul=ClassA.multiplication(**myDict)
            print(mul)

# Creating object and calling(assiging)
object1 = ClassB()
object2 = ClassC(object1)
object2.checkWholeNumber()
object2.addDictAndAss()
object3= ClassA()
