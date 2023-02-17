import easysensors
from easygopigo3 import EasyGoPiGo3
import time


gp3_obj = EasyGoPiGo3()
ultrasonic_sensor_1 = gp3_obj.init_ultrasonic_sensor()
distance_inches_sensor_1 = 0.0
distance_threshold = 6.0

def turn_bot():
  gp3_obj.drive_inches(3)
  time.sleep(.5)
  gp3_obj.steer(0, 70)
  time.sleep(2.35)
  gp3_obj.stop()
  gp3_obj.drive_inches(3)


def cm_to_inch(side):
    inch = side/2.54
    return inch

def print_results(a, b):
  print(f"Voltage: {gp3_obj.volt()}")
  print("~" * 50 + "\n")
  print("~ Right Sensor ~\n")
  print(f"Distance from object (inches): {ultrasonic_sensor_1.read_inches()}.")
  print("~" * 50 + "\n")
  print(f"Total Side 1 measured: {a}\n centimeters. ({cm_to_inch(a)} inches.)")
  print(f"Total Side 2 measured: {b}\n centimeters. ({cm_to_inch(b)} inches.)")

def get_measure():
  turn = 0
  size_1, size_2 = 0.0, 0.0
  for i in range(100):
    gp3_obj.set_speed(200)
    distance_inches_sensor_1 = ultrasonic_sensor_1.read_inches()
    if turn > 1:
      gp3_obj.stop()
      break
    elif distance_inches_sensor_1 < distance_threshold and turn == 0:
      gp3_obj.forward()
      size_1 += 2.54
    elif distance_inches_sensor_1 < distance_threshold and turn == 1:
      gp3_obj.forward()
      size_2 += 2.54
    else:
      turn_bot()
      turn += 1
      continue
    print_results(size_1, size_2)
    time.sleep(0.225)

get_measure()
