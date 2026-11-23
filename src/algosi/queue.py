from collections import deque

class Queue():
    def __init__(self):
        self._items = deque()

    def add_value(self, value):
        self._items.append(value)

    def pop_value(self):
        return self._items.popleft()

    def peek(self):
        return self._items[0]

    def __len__(self):
        return len(self._items)