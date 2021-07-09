class Math:
    def __init__(self) -> int:
        pass

    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def pr():
        print("Run")

print(Math.add5(10))
print(Math.add10(10))
Math.pr()