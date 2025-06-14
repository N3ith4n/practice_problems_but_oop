class QuotientCalculator:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def compute_quotient(self):
        if self.second != 0:
            quotient = self.first // self.second
            print(f"The quotient without decimal point is {quotient}")
        else:
            print("Cannot divide by zero.")

# Run the program
if __name__ == "__main__":
    calc = QuotientCalculator()
    calc.compute_quotient()
