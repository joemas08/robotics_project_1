import easysensors
from easygopigo3 import EasyGoPiGo3
import time

gp3_obj = EasyGoPiGo3()
ultrasonic_sensor_1 = gp3_obj.init_ultrasonic_sensor()
ultrasonic_sensor_2 = gp3_obj.init_ultrasonic_sensor('AD2')

for i in range(20):
    distance_cm_sensor_1 = ultrasonic_sensor_1.read()
    distance_inches_sensor_1 = ultrasonic_sensor_1.read_inches()
    print("~ Sensor 1 ~\n")
    print(f"Distance in inches: {distance_inches_sensor_1}")
    print(f"Distance in cm: {distance_cm_sensor_1}")
    print("-" * 30)
    print("~ Sensor 2 ~\n")
    distance_cm_sensor_2 = ultrasonic_sensor_2.read()
    distance_inches_sensor_2 = ultrasonic_sensor_2.read_inches()
    print(f"Distance in inches: {distance_inches_sensor_2}")
    print(f"Distance in cm: {distance_cm_sensor_2}\n")
    print("~" * 50 + "\n")
    time.sleep(1)
