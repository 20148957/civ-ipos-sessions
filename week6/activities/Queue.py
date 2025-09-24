class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(q.peek())
    q.dequeue()
    print(q.peek())
    q.dequeue()
    print(q.peek())