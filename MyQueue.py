class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def append(self, x):
        self.input_stack.append(x)

    def popleft(self):
        if len(self.output_stack) == 0:
            while len(self.input_stack) > 0:
                x = self.input_stack.pop()
                self.output_stack.append(x)

        if len(self.output_stack) == 0:
            return None

        return self.output_stack.pop()

    def is_empty(self):
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def size(self):
        return len(self.input_stack) + len(self.output_stack)


def main():
    sor = MyQueue()

    sor.append(1)
    sor.append(2)
    sor.append(3)

    print(sor.size())      # 3
    print(sor.is_empty())  # False

    print(sor.popleft())  # 1
    print(sor.popleft())  # 2

    print(sor.size())      # 1

    print(sor.popleft())  # 3
    print(sor.is_empty()) # True


if __name__ == "__main__":
    main()