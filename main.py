import easysensors
from easygopigo3 import EasyGoPiGo3
import time

gp3_obj = EasyGoPiGo3()
ultrasonic_sensor_1 = gp3_obj.init_ultrasonic_sensor()
ultrasonic_sensor_2 = gp3_obj.init_ultrasonic_sensor('AD2')

for i in range(20):
    distance_cm_sensor_1 = ultrasonic_sensor.read()
    distance_inches_sensor_1 = ultrasonic_sensor.read_inches()
    print(f"Distance in inches: {distance_inches}")
    print(f"Distance in cm: {distance_cm}")
    print('---------------------------------')
    distance_cm_sensor_2 = ultrasonic_sensor.read()
    distance_inches_sensor_2 = ultrasonic_sensor.read_inches()
    print(f"Distance in inches: {distance_inches}")
    print(f"Distance in cm: {distance_cm}")
    time.sleep(1)
