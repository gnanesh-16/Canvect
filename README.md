# Canvect
So, this is the newr version add on's to that Canvect is a Python package designed for sending and managing CAN (Controller Area Network) messages related to acceleration control. It provides a simple yet flexible API for creating and dispatching CAN messages, making it ideal for applications in automotive and industrial systems where CAN communication is essential.
# CAN Package

A Python package for handling CAN bus communication to easily handle the CAN bus communication for vehicle control. It also includes a RingBuffer implementation to store CAN messages efficiently.

## Installation

```bash
pip install .

```

## How to use package 

1. yoU can modify parameters like arbitration_id, bitrate, and channel to suit your needs

```bash 
from my_can_package import continuous_acceleration_send

continuous_acceleration_send(
    arbitration_id=0x200,  # Custom CAN ID
    channel='PCAN_USBBUS1',  # Custom CAN channel
    bitrate=250000  # Custom bitrate
)
```


## Example

```bash 
from my_can_package import RingBuffer

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

## Sending CAN Messages

1. Overview:
The package provides functionality to send acceleration messages or any custom CAN message using the python-can library. You can customize the arbitration_id (CAN ID), data (8-byte payload), and CAN bus parameters such as bitrate and channel.

2. Example Code for Sending CAN Messages
3. Setup:
    *  Initialize the CAN bus using your desired channel, interface, and bitrate.

    * 3.2 Send messages with the specified arbitration_id (CAN ID) and data payload (8 bytes)

```bash 
from my_can_package import continuous_acceleration_send

# Example for continuously sending acceleration messages
continuous_acceleration_send(
    arbitration_id=0x130,  # Custom CAN ID
    channel='PCAN_USBBUS2',  # Custom CAN channel
    bitrate=500000  # Custom bitrate
)

```
4. Explanation

* The function continuous_acceleration_send sends acceleration messages continuously to the CAN bus.

* You can modify the arbitration_id (CAN ID) as needed, as well as adjust the channel and bitrate to match your specific CAN bus setup.

* Messages are sent at an interval of 10ms with dynamic byte values (like the seventh_byte) incrementing automatically


## Customizing CAN Parameters 

You have full control over the following parameters when sending CAN messages:

* arbitration_id: This is the CAN ID used for sending the message.
* channel: Specify the CAN interface/channel you are using. (e.g., PCAN_USBBUS2, can0).
* bitrate: Define the CAN bus bitrate, typically 500000 for high-speed CAN.

```bash 
from my_can_package import CANBusHandler, send_acceleration_message

# Initialize CAN bus
bus_handler = CANBusHandler(channel='PCAN_USBBUS2', interface='pcan', bitrate=500000)

# Define custom CAN data (8 bytes)
data = [0x11, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00]

# Send CAN message with a custom CAN ID and data
send_acceleration_message(bus_handler.bus, arbitration_id=0x200, data=data)

# Shutdown the bus after sending
bus_handler.shutdown()

```
Explanation:
* You can use CANBusHandler to set up the CAN bus and * send_acceleration_message to send custom messages.
* This example sends a message with a CAN ID of 0x200 and an 8-byte payload.