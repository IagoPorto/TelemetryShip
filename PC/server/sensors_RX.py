import zenoh

class zenoh_sub:

    def __init__ (self, key: str = "sensors") -> None:

        self.session = zenoh.open()
        self.subscriber = self.session.declare_subscriber (key, self.read_data)


    def read_data (self, sample) -> None:

        self.data = sample.payload.decode('utf-8').strip()
        #print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.decode('utf-8').strip ()}')")


    def close_communication (self) -> None:

        self.session.close ()

    def get_data(self) -> str:

        return self.data




if __name__ == "__main__":

    subscriber = zenoh_sub ()
    input("Press Enter to stop...")
