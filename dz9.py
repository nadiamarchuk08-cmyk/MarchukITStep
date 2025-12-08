class PowersOfTwo:
    def __init__(self, max_number):
        self.max_number = max_number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_number:
            raise StopIteration
        value = 2 ** self.current
        self.current += 1
        return value

iterator = PowersOfTwo(10)

for num in iterator:
    print(num)