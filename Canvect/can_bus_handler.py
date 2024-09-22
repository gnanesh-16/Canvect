import time
import can

# Custom Ring Buffer Implementation
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.size = 0

    def append(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        return self.buffer[(self.head - self.size + index) % self.capacity]

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"RingBuffer({self.buffer})"

# Function to send CAN message for acceleration control
def send_Canvect_message(bus, arbitration_id, data):
    message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
    try:
        bus.send(message)
        print(f"CAN Message sent: ID=0x{arbitration_id:X}, Data: {' '.join(f'{byte:02X}' for byte in data)}")
    except can.CanError as e:
        print(f"Message not sent: {e}")

def continuous_Canvect_message(arbitration_id, seventh_byte, channel, interface, bitrate, data_accel, sleep_time, buffer_capacity):
    # Initialize CAN bus
    try:
        bus = can.interface.Bus(channel=channel, interface=interface, bitrate=bitrate)
    except can.CanError as e:
        print(f"Failed to initialize CAN bus: {e}")
        return

    # Create a ring buffer to store acceleration messages
    acc_buffer = RingBuffer(capacity=buffer_capacity)

    try:
        while True:
            # Update the data_accel message bytes dynamically
            data_accel[6] = seventh_byte  # Update seventh byte
            
            # Calculate checksum for Byte 7
            data_accel[7] = data_accel[0] ^ data_accel[1] ^ data_accel[2] ^ data_accel[3] ^ data_accel[4] ^ data_accel[5] ^ data_accel[6]

            # Append the message to the ring buffer
            acc_buffer.append(data_accel)

            # Send the CAN message for vehicle speed control
            send_Canvect_message(bus, arbitration_id, data_accel)

            # Optional: Print current buffer contents (for debugging)
            print("Current Buffer State:", acc_buffer)

            time.sleep(sleep_time)  # Send according to user-specified interval

    except KeyboardInterrupt:
        print("Exiting Acceleration Control...")
    finally:
        bus.shutdown()

if __name__ == "__main__":
    # User inputs
    arbitration_id = int(input("Enter arbitration ID (hex): "), 16)
    seventh_byte = int(input("Enter the value for the seventh byte (0-15): "))
    channel = input("Enter CAN channel (e.g., 'PCAN_USBBUS2'): ")
    interface = input("Enter CAN interface (e.g., 'pcan'): ")
    bitrate = int(input("Enter bitrate (e.g., 500000): "))
    
    # User specifies ring buffer capacity
    buffer_capacity = int(input("Enter ring buffer capacity: "))
    
    # User specifies data_accel
    data_accel = [
        int(input("Enter Byte 0: ")),
        int(input("Enter Byte 1: ")),
        int(input("Enter Byte 2: ")),
        int(input("Enter Byte 3: ")),
        int(input("Enter Byte 4: ")),
        int(input("Enter Byte 5: ")),
        seventh_byte,  # Already inputted
        0x00  # Placeholder for Byte 7 (will be updated in the loop)
    ]

    sleep_time = float(input("Enter sleep time (in seconds): "))

    # Start sending CAN frames
    continuous_Canvect_message(
        arbitration_id=arbitration_id,
        seventh_byte=seventh_byte,
        channel=channel,
        interface=interface,
        bitrate=bitrate,
        data_accel=data_accel,
        sleep_time=sleep_time,
        buffer_capacity=buffer_capacity
    )
