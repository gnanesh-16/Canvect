# my_can_package/ring_buffer.py

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
