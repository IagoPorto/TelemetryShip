from sensors_TX import zenoh_pub
import time

#Defining publishers
dist = zenoh_pub("sensors/dist")
accel = zenoh_pub("sensors/accel")
gyro = zenoh_pub("sensors/gyro")
magnet = zenoh_pub("sensors/magnet")

count = 0

while True:

    count += 1
    dist.send_data ("Mucha distancia la verdad: " + str(count))
    accel.send_data ("Voy muy rápido la verdad: " + str(count))   
    gyro.send_data ("Giro mucho la verdad: " + str(count))
    magnet.send_data ("No sé que es la verdad: " + str(count))
    time.sleep(1)