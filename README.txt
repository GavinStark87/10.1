This class is meant to emulate a mircowave and some of the aspects of a microwave. The class has methods that a microwave could or would have. The microwave class uses the library 'time' as that is a large part of what microwaves do in real life

The class variable is nextId which increments with each new object. This is so that each object can have a unique id that it can be identified by

The first data variable is __powerPer, which is short for power percentage. This is the percentage of power the microwave is using and can be changed with the set_power function. This is an integer.
The second data variable is __brand, which is a string. Brand is the brand of microwave and can be changed with set_brand.
The third data variable is __id, which is an int. __id is the id of the microwave that it gets identified by
the fourth data variable is __maxPower, which is an int. __maxPower is the highest amount of wattage the microwave can apply.

The first method, __init__ takes a string which it sets the data variable __brand to.
The next seven methods are get and set methods for power and brand.
set_maxPower takes an integer and sets __maxPower to that integer
get_maxPower returns __maxPower
get_id returns __id
set_brand takes a string and sets __brand to that string
get_brand returns a string containing the brand of microwave
set_powerPer takes an integer <= 100 and > 0 and sets powerPer to that integer
get_powerPer returns an int containing powerPer

The cook method takes an integer which represents the number of seconds cook should run for. The cook method prints out the amount of time remaining, waits one second, and repeats until the for loop is finished and it has waited the given number of seconds

The applyHeat method takes an integer value representing the amount of heat the user wants applied. The method determines the effective wattage by multiplying (__powerPer/100) by maxPower and then divides the desired heat by the adjusted wattage. The method then runs cook for that amount of time.

The demo program first creates a microwave object with brand "Toshiba" and maxPower 1200
The program then shows all of the get and set functions by printing out and changing the data variables
The program then shows the cook method which cooks for 5 seconds.
Next, the program uses the applyHeat method and applies 4800 watts. This takes 12 seconds as maxPower is 500 and the powerPer is 80.
The powerPer then gets changed to 50 and the applyHeat function is run again, this time with 1200 watts as the desired heat.

The demo program gets run immediately upon running the code