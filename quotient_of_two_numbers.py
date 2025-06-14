class DecimalQuotientCalculator:
    def __init__(self):
        self.first = float(input("Give me some numbers, first one = "))
        self.second = float(input("second one = "))

    def compute(self):
        if self.second != 0:
            quotient = self.first / self.second
            print(f"The quotient is {quotient}")
        else:
            print("Cannot divide by zero.")

# Run the program
if __name__ == "__main__":
    calc = DecimalQuotientCalculator()
    calc.compute()
