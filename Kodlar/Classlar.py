class Matematik:
    def Topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def Cıkart(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def Carp(self,sayi1,sayi2):
        return sayi1 * sayi2    
    
    def Bol(self,sayi1,sayi2):
        return sayi1 / sayi2    
    
matematik = Matematik()
print("Toplam = " + str(matematik.Cıkart(2, 29)))



#%% Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Engin", "Kutlu", 18)
print(person1.firstName)


class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self,CreditCardNumber):
        self.creditCardNumber = CreditCardNumber
        
ahmet = Worker()

mehmet = Customer()
