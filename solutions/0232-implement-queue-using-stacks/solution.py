class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        self.stackA.append(x)

    def pop(self) -> int:
        if self.stackB == [] and self.empty() == False:
            while self.stackA != []:
                item = self.stackA.pop()
                self.stackB.append(item)
        return self.stackB.pop()

    def peek(self) -> int:
        if self.stackB == [] and self.empty() == False:
            while self.stackA != []:
                item = self.stackA.pop()
                self.stackB.append(item)
        return self.stackB[-1]

    def empty(self) -> bool:
        sA, sB = len(self.stackA), len(self.stackB)
        return sA == sB == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
