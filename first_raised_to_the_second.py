class ExponentCalculator:
    def __init__(self):
        self.base = int(input("Give me some numbers, first one = "))
        self.exponent = int(input("second one = "))

    def compute(self):
        result = self.base ** self.exponent
        print(result)

# Run the program
if __name__ == "__main__":
    calc = ExponentCalculator()
    calc.compute()
