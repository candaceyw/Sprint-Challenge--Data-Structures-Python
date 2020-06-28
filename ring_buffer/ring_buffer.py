class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.cur = 0

    def append(self, item):
        self.buffer[self.cur] = item
        self.cur = (self.cur + 1) % self.capacity

    def get(self):
        return [node for node in self.buffer if node is not None]