class RemainderCalculator:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def compute_remainder(self):
        if self.second != 0:
            remainder = self.first % self.second
            print(f"The remainder is {remainder}")
        else:
            print("Cannot divide by zero.")

# Run the program
if __name__ == "__main__":
    calc = RemainderCalculator()
    calc.compute_remainder()
