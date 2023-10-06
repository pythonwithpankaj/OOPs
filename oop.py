### OOP(Object oriented programming)
      #  class -- collection of function(methods) and data(attributes)
           # Attributes Types:
                       # class attributes -- defined by class
                       # instance attributes -- defined by object(instance)
           # Methods -- function defined in class
           # types in methods:
                      # instance methods
                      # class method
                      # static method
      # object or instance -- entity which acceses the defination of class

# class institute:
#     courses=['Java','Python','PHP','Digital Marketing','Autocad']            

# obj=institute()
# print(obj.courses)
# obj.courses.remove('Autocad')
# obj1=institute()
# print(obj1.courses)
# obj2=institute()
# print(obj2.courses)
# obj3=institute()   
# print(obj3.courses) 


# class institute:
#     courses=['Java','Python','PHP','Digital Marketing','Autocad']
#     def Entry(self):
#         print('welcome to our institute')
#     def Councelling(self):
#         print('you are in councelling department')
#     def Billing(self):
#         print('you are in billing department')
#     def Training(self):
#         print('you are in training department')
# obj=institute()
# obj.Entry()                  #Entry(obj)
# obj.Councelling()
# obj.Billing()
# obj.Training()  



#  class institute:
#      courses=['Java','Python','PHP','Digital Marketing','AutoCad']
#      fee=[12000,15000,18000,10000,9000]
#      def __init__(self,name,course):
#          print('welcome to our institute')
#          self.name=name                        # instance attributes
#          self.course=course
#      def councelling(self):       
#          if self.course in self.courses:
#           print('you are in councelling department')
#           print('you have choosen course:',self.course)
#          else:
#              print('No course available in this name')
#      def billing(self,amount):
#          self.amount=amount
#          print('you are in billing department')
#          print('your name:',self.name)
#          print('your course:',self.course)
#          print('paid amount:',self.amount)
#          index=self.courses.index(self.course)
#          self.balance=self.fee[index]-amount
#          print('Balance:',self.balance)
#      def traininig(self):
#          if self.balance==0:
#           print('you are in training department')
#           print('you can start your training')
#          else:
#             print('Please clear your balance')
#      def _del_(self):
#         print('Destructor')       
  
#  obj=institute('Pankaj kumar','Python')
#  obj.councelling()
#  obj.billing(15000)
#  obj.traininig()
#  del obj     


## constructor and destructor are per defined method of a class

#  class Book:
#      def __init__(self ,title,author,price):
#          self.title=title
#          self.author=author
#          self.price=price
#      def view(self):
#          print("Title:",self.title)
#          print("Author Name:",self.author)
#          print("Price:",self.price)
#  
#  b1=Book('abc','mr. xyz',200)
#  b1.view()


# class BankAccount:
#     def __init__(self,acc_no,name,balance):
#         self.acc_no=acc_no
#         self.name=name
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#     def withdrawl(self,amount):
#         self.balance-=amount
#     def bankfee(self):
#         self.balance-=(self.balance*0.05)
#     def display(self):
#         print('Account NO:',self.acc_no)
#         print('Account Holder Name:',self.name)
#         print('Account Balance:',self.balance)                
 
# b1=BankAccount(75054026,'Rohit',50000)
# b1.display()
# b1.deposite(30000)
# b1.withdrawl(40000)
# b1.bankfee()
# b1.display()


###  OOPs Features:
              # Inheritance
                        # Single Inheritance
                        # Multiple Inheritance
                        # Multilevel Inheritance
                        # hierarichal Inheritance
                        # Hybrid Inheritance
              # Polymorphism
              # Encapsulation
              # Abstraction

# Inheritance

# class Vehicle:                        # base class or parent class
#     wheels=4
#     def start(self):
#         print('start vehicle')
#     def stop(self):
#         print('stop vehicle') 
# class Design:
#     def interior(self):
#         print('Interior Design')
#     def exterior(self):
#         print('Exterior Design')            
 
# class car(Vehicle,Design):                   # derived class or child class 
#     pass
# class sportscar(car):
#     pass
# class truck(Vehicle):
#     pass
# class bus(Vehicle):
#     pass

# c1=car()
# print('no of wheels:',c1.wheels)
# c1.start()
# c1.stop()
# c1.interior()
# c1.exterior()

# t1=truck
# t1.start()


#  class Person:
#      def __init__(self,name,age):
#          self.name=name
#          self.age=age
#      def display(self):
#          print('Name:',self.name)
#          print('Age:',self.age)
#  class student:
#      def __init__(self,name,age,section):
#          #Person.__init__(self,name,age)            1st
#          #super().__init__(name,age)                2nd
#          self.section=section
#      def displayStudent(self):
#          print('Student name:',self.name)
#          print('Age:',self.age)
#          print('section:',self.section)                
  
#  s1=student('Raman',21,'A')
#  s1.displayStudent()


## Polymorphism  --  many form
                    # Method overloading
                    # Method overriding
                    # operator overloading

#  class calc:
#      def __init__(self,a,b=0):
#          self.a=a
#          self.b=b
#      def add(self):
#          return self.a+self.b    
  
#  c1=calc(3,2)                          # hypertuning
#  print(c1.add())


#  class Vehicle:                        # base class or parent class
#      wheels=4
#      def start(self):
#          print('start vehicle')
#      def stop(self):
#          print('stop vehicle') 
#  class Design:
#      def interior(self):
#          print('Interior Design')
#      def exterior(self):
#          print('Exterior Design')  
#  
#  class car(Vehicle,Design):
#      def start(self):
#          print('start car')
  
#  c1=car()
#  c1.start()
#  c1.stop()

#  i=5
#  j=7
#  i+j           #__add__(i,j)
#  i-j           #__sub__(i,j)
#  i='python'
#  i-        


#  class calc:
#        def __init__(self,a):
#            self.a=a
#        def __add__(self,other):
#            return self.a+other.a   
  
#  x=calc(4)
#  y=calc(5)
#  print(x+y)


### Encapsulation  --  binding the data
 
## access modifiers
           #  public
           #  protected  
           #  private

#  class Employee:
#      def __init__(self,name,age,loc):
#          self.name=name
#          self._age=age
#          self.__loc=loc
#  
#      def display(self):
#          print('Name:',self.name)
#          print('Age:',self._age)
#          print('Location:',self.__loc)
#      def changeloc(self,newloc):
#          self.__loc=newloc
  
#  e1=Employee('Radhe',30,'Mathura')            
#  print(e1.name)
#  print(e1._age)
#  e1.display()

#  print(e1.__loc)
#  e1.changeloc('Noida')
#  e1.display()



## Abstraction  -- hiding the method(Process)

# from abc import abstractmethod ,ABC

# class Vehicle(ABC):                        # base class or parent class
#     wheels=4
#     @abstractmethod
#     def start(self):
#         print('start vehicle')
#     def stop(self):
#         print('stop vehicle') 
# class Design:
#     def interior(self):
#         print('Interior Design')
#     def exterior(self):
#         print('Exterior Design')  
# 
# class car(Vehicle,Design):
#     def start(self):
#         print('New start method in car')

# v1=Vehicle()
# c1=car()
# c1.start()


### Static Method

#  class calc:
#      @staticmethod
#      def iseven(n):
#          if n%2==0:
#              print('Even')
#          else:
#              print('Odd')


#  c=calc()
#  c.iseven(10)                


### Class Method

#  class Employee:
#     def __init__(self,name,age,loc):
#         self.name=name
#         self.age=age
#         self.loc=loc
#     @classmethod    
#     def getdata(self,name,by,loc):   
#         return self(name,2023-by,loc)
#     def display(self):
#         print('Name:',self.name)
#         print('Age:',self.age)
#         print('Location:',self.loc)
  
#  e1=Employee.getdata("Rohan",2001,"Delhi")
#  e1.display()
#  e1=Employee("Rohit",20,"Noida")
#  e1.display()