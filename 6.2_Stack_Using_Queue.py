from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.top_element = None

    def push(self, x: int) -> None:
        self.queue2.append(x)
        self.top_element = x

        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        # Swap queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()
        return None

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.queue1) == 0

# Example usage:
obj = MyStack()

obj.push(1)
obj.push(2)
print(obj.top())   # Output: 2
print(obj.pop())   # Output: 2
print(obj.empty()) # Output: False

