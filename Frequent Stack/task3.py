from collections import deque, defaultdict

class FreqStack:
    def __init__(self):
        self.stack = deque()
        self.freq = defaultdict(int)
        self.max_f = 0

    def push(self, val):
        freq = self.freq[val] + 1
        self.freq[val] = freq
        if freq > self.max_f:
            self.max_f = freq
        while len(self.stack) < freq:
            self.stack.append(deque())
        self.stack[freq-1].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_f - 1].pop()
        self.freq[val] -= 1
        if not self.stack[self.max_f - 1]:
            self.max_f -= 1
        return val

# freqStack = FreqStack()
# freqStack.push(5)
# print(freqStack)
# freqStack.push(7)
# print(freqStack)
# freqStack.push(5)
# print(freqStack)
# freqStack.push(7)
# print(freqStack)
# freqStack.push(4)
# print(freqStack)
# freqStack.push(5)
# print(freqStack)
# print(freqStack)
# print(freqStack)
# freqStack.pop()
# print(freqStack)
# freqStack.pop()
# print(freqStack)
