import asyncio
import websockets
from sensors_RX import zenoh_sub

dist = zenoh_sub ("sensors/dist")
accel = zenoh_sub ("sensors/accel")
gyro = zenoh_sub ("sensors/gyro")
magnet = zenoh_sub ("sensors/magnet")


async def send_data (websocket):

    while True:
        data = dist.get_data () + ";" + accel.get_data () + ";" + gyro.get_data () + ";" + magnet.get_data ()
        print (data)

        await websocket.send (data)
        await asyncio.sleep (0.25)


async def main ():

    server = await websockets.serve (send_data, "localhost", 8765)
    await server.wait_closed ()

if __name__ == "__main__":
    asyncio.run (main ())
