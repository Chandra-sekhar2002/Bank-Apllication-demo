class Human():
    life="Air & Water"
    #Instance Attributes
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    #Instance Method
    def Eating(self,food):
        return "{} is eating {}".format(self.name,food)
#Creating object of human class
Ram=Human('Ram',6,70)
Scott=Human('Scott',6,76)
print(Human.life)#Accessing class level variable

print("Height of {} is {}".format(Ram.name,Ram.height))
print("Weight of {} is {}".format(Ram.name,Ram.weight))
print(Ram.Eating("Pizza"))

print("Height of {} is {}".format(Scott.name,Scott.height))
print("Weight of {} is {}".format(Scott.name,Scott.weight))
print(Scott.Eating("Big Burger"))
