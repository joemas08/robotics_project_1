import easysensors
from easygopigo3 import EasyGoPiGo3
import time

size_1 = 0
size_2 = 0
gp3_obj = EasyGoPiGo3()
ultrasonic_sensor_1 = gp3_obj.init_ultrasonic_sensor()
ultrasonic_sensor_2 = gp3_obj.init_ultrasonic_sensor('AD2')
print(gp3_obj.volt())
distance_threshold = 6.0
turn = 0

for i in range(100):
    gp3_obj.set_speed(200)
    distance_cm_sensor_1 = ultrasonic_sensor_1.read()
    distance_inches_sensor_1 = ultrasonic_sensor_1.read_inches()
    if turn > 1:
      gp3_obj.stop()
      break
    elif distance_inches_sensor_1 < distance_threshold and turn == 0:
      gp3_obj.forward()
      size_2 += 2.54
    elif distance_inches_sensor_1 < distance_threshold and turn == 1:
      gp3_obj.forward()
      size_1 += 2.54
    else:
      gp3_obj.drive_inches(3)
      time.sleep(.5)
      gp3_obj.steer(0, 70)
      time.sleep(2.35)
      gp3_obj.stop()
      gp3_obj.drive_inches(3)
      turn += 1
      continue
    print("~ Right Sensor ~\n")
    print(f"Distance in inches: {distance_inches_sensor_1}")
    print(f"Distance in cm: {distance_cm_sensor_1}")
    print("-" * 30)
    print("~ Left Sensor ~\n")
    distance_cm_sensor_2 = ultrasonic_sensor_2.read()
    distance_inches_sensor_2 = ultrasonic_sensor_2.read_inches()
    print(f"Distance in inches: {distance_inches_sensor_2}")
    print(f"Distance in cm: {distance_cm_sensor_2}\n")
    print("~" * 50 + "\n")
    print(f"Total Side 1 measured: {size_1}\n")
    print(f"Total Side 2 measured: {size_2}\n")
    time.sleep(0.225)
