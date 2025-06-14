class SumTwoNumbers:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def show_sum(self):
        total = self.first + self.second
        print(f"The sum of the two numbers is {total}")

# Run the program
if __name__ == "__main__":
    calculator = SumTwoNumbers()
    calculator.show_sum()
