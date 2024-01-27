from tx.sensors_TX import zenoh_pub
from Sensorizacion.comm_arduino import CommArduino    
import time

comm_ard = CommArduino ()

#Defining publishers
dist = zenoh_pub("sensors/dist")
accel = zenoh_pub("sensors/accel")
gyro = zenoh_pub("sensors/gyro")
magnet = zenoh_pub("sensors/magnet")

while True:

    dist.send_data (comm_ard.getDistance ())
    accel.send_data (comm_ard.getAccelerometer ())   
    gyro.send_data (comm_ard.getGyroscope ())
    magnet.send_data (comm_ard.getMagnetometer ())
    time.sleep(1)
    
