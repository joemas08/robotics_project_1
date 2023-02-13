import easysensors
from easygopigo3 import EasyGoPiGo3
import time

size = 0
gp3_obj = EasyGoPiGo3()
ultrasonic_sensor_1 = gp3_obj.init_ultrasonic_sensor()
ultrasonic_sensor_2 = gp3_obj.init_ultrasonic_sensor('AD2')
print(gp3_obj.volt())
distance_threshold = 6.0
gp3_obj.set_speed(200)

for i in range(50):
    distance_cm_sensor_1 = ultrasonic_sensor_1.read()
    distance_inches_sensor_1 = ultrasonic_sensor_1.read_inches()
    if distance_inches_sensor_1 < distance_threshold:
      gp3_obj.forward()
    else:
        gp3_obj.stop()
        break
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
    size += 2.54
    print(f"Total size measured: {size}\n")
    time.sleep(0.25)
