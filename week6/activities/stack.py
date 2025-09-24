class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

if __name__ == "__main__":
    s = stack()
    s.push('Work')
    print(s.peek())
    s.pop()
    print(s.peek())
