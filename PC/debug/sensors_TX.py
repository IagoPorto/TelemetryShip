import zenoh

class zenoh_pub:

    def __init__ (self, key: str = "sensors") -> None:

        self.session = zenoh.open()
        self.writer = self.session.declare_publisher (key)


    def send_data (self, message: str) -> None:

        self.writer.put (message)
        print("Data: " + message)


    def close_communication (self) -> None:

        self.session.close ()

