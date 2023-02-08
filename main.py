import easysensors
from easygopigo3 import EasyGoPiGo3
import time

gp3_obj = EasyGoPiGo3()
ultrasonic_sensor = gp3_obj.init_ultrasonic_sensor('AD2')

for i in range(20):
    distance_cm = ultrasonic_sensor.read()
    distance_inches = ultrasonic_sensor.read_inches()
    print(f"Distance in inches: {distance_inches}")
    print(f"Distance in cm: {distance_cm}")
    time.sleep(1)

