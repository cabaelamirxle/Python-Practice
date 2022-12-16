from queue import Queue

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()