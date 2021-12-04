#Gavin Stark
#10.1 Your own class
#This is a class representing a microwave, it makes use of the time library and sleep function
import time
class Microwave():
    nextId = 1#the only class variable is nextId
    __powerPer = 100
    __brand = ""
    __id = 0
    __maxPower = 1200
    
    def __init__(self, brand, maxPower):
        self.__maxPower = maxPower
        self.__brand = brand
        self.__id = self.nextId#sets the individual Id to the class variable and then increments the class variable
        self.nextId += 1
    def set_maxPower(self, maxPow):#all the get and set functions are simple
        self.__maxPower = maxPow
    def get_maxPower(self):
        return self.__maxPower
    def get_id(self):
        return self.__id
    def set_brand(self, brand):
        self.__brand = brand
    def get_brand(self):
        return self.__brand
    def set_powerPer(self, power):
        if power <= 100 and power > 0:#a percentage can't be zero or over 100 so this if statement stops that
            self.__powerPer = power
        else:
            print("cannot be over 100 or less than 1")
    def get_powerPer(self):
        return self.__powerPer
    def cook(self, time1):
        for i in range(0, time1):#time cannot be a float because microwaves only take int inputs.
            print("Time remaining: " + str(time1 - i) + 'seconds')#I think this is a pretty good way to do a decrementing for loop, the time1 - i gives remaining time and decremets as the loop progresses
            time.sleep(1)
        print("Cooking Finished!")
    def applyHeat(self, desHeatAppl):
        adjPow = (self.__powerPer/100)*self.__maxPower#power percentage gets converted into a decimal value and then is multiplied by maxPower
        
        self.cook(int(desHeatAppl/adjPow))#cook is run for the desired heat/adjusted heat as watts are a measurement of joules per second
        
def Main():
    mic = Microwave("Toshiba", 1200)
    print("maxPower is: " + str(mic.get_maxPower()))
    print("id number is: " + str(mic.get_id()))
    print("brand is: " + mic.get_brand())
    print("powerPer is: " + str(mic.get_powerPer()))
    mic.set_maxPower(500)
    print("maxPow was set to: " + str(mic.get_maxPower()))
    mic.set_brand("Panasonic")
    print("brand was set to: " + mic.get_brand())
    mic.set_powerPer(80)
    print("powerPer was set to: " + str(mic.get_powerPer()))
    mic.cook(5)
    mic.applyHeat(4800)
    mic.set_powerPer(50)
    mic.applyHeat(1200)
Main()