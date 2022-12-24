import datetime

current_time = datetime.datetime.now()
clock_time = current_time.strftime("%H:%M:%S")

class Clock:
  def __init__(self, type, time):
    self.type = type
    self.time = time

  def show_time(self):
    print(f"The time right now - {self.time}")
    
  def show_type(self):
    print(f"The type of the clock is - {self.type}.")

clock1 = Clock("Big Grandmas Clock", clock_time)

clock1.show_time()
clock1.show_type()