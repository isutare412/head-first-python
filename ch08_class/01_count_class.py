class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def __str__(self) -> str:
        return str(self.val)

    def increase(self) -> None:
        self.val += self.incr


if __name__ == '__main__':
    counter = CountFromBy(100, 3)

    for i in range(10):
        counter.increase()
        print(counter)
