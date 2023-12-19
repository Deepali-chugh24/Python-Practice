class student:
    def __init__(self,name,age,rollNo,Marks):
        self.name=name
        self.age=age
        self.rollNo=rollNo
        self.Marks=Marks
        def __str__(self):
            print(s.name,s.age,s.rollNo,s.Marks)

s=student("Nitsimran",20,1,100)





class temprature:
    a=int(input('Enter temprature '))
    def __init__(self):
      self.b=self.a*9/5+32
      self.c=5/9*(self.a-32)
      print(f"converted temprature from Celsius to Fahrenheit {self.b} ")
      print(f"converted temprature from Fahrenheit to Celsius {self.c}  ")
d=temprature()



          
