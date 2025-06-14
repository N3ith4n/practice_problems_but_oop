class DifferenceCalculator:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def show_difference(self):
        result = self.first - self.second
        print(f"The difference of the two numbers is {result}")

# Run the program
if __name__ == "__main__":
    calc = DifferenceCalculator()
    calc.show_difference()
