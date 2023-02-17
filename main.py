import easysensors
from easygopigo3 import EasyGoPiGo3
import time

size_1,size_2 = 0
gp3_obj = EasyGoPiGo3()
ultrasonic_sensor_1 = gp3_obj.init_ultrasonic_sensor()
distance_inches_sensor_1 = 0.0
distance_threshold = 6.0
turn = 0

def turn_bot():
  gp3_obj.drive_inches(3)
  time.sleep(.5)
  gp3_obj.steer(0, 70)
  time.sleep(2.35)
  gp3_obj.stop()
  gp3_obj.drive_inches(3)
  turn += 1

def measure_side(side):
  gp3_obj.forward()
  side += 2.54
  return side

def cm_to_inch(side):
    inch = side/2.54
    return inch

def print_results():
  print(f"Voltage: {gp3_obj.volt()}")
  print("~" * 50 + "\n")
  print("~ Right Sensor ~\n")
  print(f"Distance from object (inches): {distance_inches_sensor_1}. Stop past: {distance_threshold} inches.")
  print("~" * 50 + "\n")
  print(f"Total Side 1 measured: {size_1}\n centimeters. ({cm_to_inch(size_1)} inches.)")
  print(f"Total Side 2 measured: {size_2}\n centimeters. ({cm_to_inch(size_2)} inches.)")
  
def get_measure():
  for i in range(100):
    gp3_obj.set_speed(200)
    distance_inches_sensor_1 = ultrasonic_sensor_1.read_inches()
    if turn > 1:
      gp3_obj.stop()
      break
    elif distance_inches_sensor_1 < distance_threshold and turn == 0:
      gp3_obj.forward()
      measure_side(size_1)
    elif distance_inches_sensor_1 < distance_threshold and turn == 1:
      measure_side(size_2)
    else:
      turn_bot()
      continue
    print_results()
    time.sleep(0.225)

get_measure()
