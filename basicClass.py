import datetime
import math

current_time = datetime.datetime.now()
clock_time = current_time.strftime("%H:%M:%S")

class Clock:
  #assigning variables
  def __init__(self, type, time):
    self.type = type
    self.time = time

  #showing the current time
  def show_time(self):
    print(f"The time right now - {self.time}")
  
  #showing the type of the clock
  def show_type(self):
    print(f"The type of the clock is - {self.type}.")

clock1 = Clock("Big Grandmas Clock", clock_time)

clock1.show_time()
clock1.show_type()

class operationsCircle:
  #getting the variables
  def __init__(self, radius):
    self.radius = radius

  #calculating an area
  def area(self):
    return self.radius ** 2 * math.pi

  #calculating a diameter
  def diameter(self):
    return self.radius * 2
    
  #calculating a circumference
  def circumference(self):
    return self.radius * 2 * math.pi

circle = operationsCircle(25)

class Square:
    def __init__(self, l):
        self.l = l
    
    @property
    def area(self):
        return self.l ** 2

square = Square(7)

print(circle.area())
print(circle.diameter())
print(circle.circumference())
print(square.area)
