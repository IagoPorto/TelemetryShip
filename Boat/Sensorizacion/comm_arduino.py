from serial import Serial

class CommArduino:

    def __init__ (self) -> None:

        self.serial = Serial ("/dev/ttyUSB0", 9600);

        self.serial.flush ()


    def getDistance (self):

        self.serial.write ("0".encode ())
        return self.serial.read_until (b'\n').decode ("ascii")


    def getAccelerometer (self):

        self.serial.write ("1".encode ())
        return self.serial.read_until (b'\n').decode ("ascii")



    def getGyroscope (self):

        self.serial.write ("2".encode ())
        return self.serial.read_until (b'\n').decode ("ascii")


    def getMagnetometer (self):

        self.serial.write ("3".encode ())
        return self.serial.read_until (b'\n').decode ("ascii")
    

if __name__ == "__main__":

    comm = CommArduino ()

    print (comm.getDistance ())
    print (comm.getAccelerometer ())
    print (comm.getGyroscope ())
    print (comm.getMagnetometer ())