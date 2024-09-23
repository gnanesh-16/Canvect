# Canvect v0.1.4 Release Notes

# Overiew
So, this is the newr version add on's to that Canvect is a Python package designed for sending and managing CAN (Controller Area Network) messages related to acceleration control. It provides a simple yet flexible API for creating and dispatching CAN messages, making it ideal for applications in automotive and industrial systems where CAN communication is essential.

# New Features
1. Dynamic Parameter Input: Users can now input dynamic parameters for the following

- arbitration_id: Specify the CAN ID as a hexadecimal value.
- seventh_byte: Set the seventh byte for the CAN message (value between 0-15).
- channel: Define the CAN channel (e.g., 'PCAN_USBBUS2').
- interface: Choose the CAN interface (e.g., 'pcan').
- bitrate: Set the bitrate for the CAN bus communication (e.g., 500000).

This enhancement allows users to customize their CAN message sending directly from input prompts, making the package more versatile and user-friendly.

## Installation

```bash
pip install canvect==0.1.4

```

## Usage Examples

1. You can now easily modify parameters like arbitration_id, bitrate, and channel to suit your specific needs:ds

```bash 
from Canvect import continuous_acceleration_send

continuous_acceleration_send(
    arbitration_id=int(input("Enter arbitration ID (hex): "), 16),  # Custom CAN ID
    seventh_byte=int(input("Enter the value for the seventh byte (0-15): ")),  # Seventh byte
    channel=input("Enter CAN channel (e.g., 'PCAN_USBBUS2'): "),  # Custom CAN channel
    interface=input("Enter CAN interface (e.g., 'pcan'): "),  # Custom interface
    bitrate=int(input("Enter bitrate (e.g., 500000): "))  # Custom bitrate
)

```


## Example with RingBuffer

```bash 
from Canvect import RingBuffer

# Create a RingBuffer with a capacity of 5 items
buffer = RingBuffer(capacity=5)

# Append items to the buffer
for i in range(10):
    buffer.append(f"message_{i}")
    print(f"Buffer after appending message_{i}: {buffer}")

# Access items by index
for i in range(len(buffer)):
    print(f"Item at index {i}: {buffer[i]}")


```
1. The buffer can hold up to 5 items. Once it reaches the maximum capacity, new items will overwrite the oldest ones.

2. You can access items using their index. If you try to access an index that is out of range, an IndexError will be raised.

Note: Here refers to above example


```bash 
from Canvect import CANBusHandler, send_Canvect_message

# Initialize CAN bus
bus_handler = CANBusHandler(channel='PCAN_USBBUS2', interface='pcan', bitrate=500000)

# Define custom CAN data (8 bytes)
data = [0x11, 0xC8, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]

# Send CAN message with a custom CAN ID and data
send_Canvect_message(bus_handler.bus, arbitration_id=0x200, data=data)

# Shutdown the bus after sending
bus_handler.shutdown()

```
