class SumCalculator:
    def __init__(self):
        self.numbers = []

    def get_inputs(self):
        for i in range(1, 11):
            num = int(input(f"Enter number {i} = "))
            self.numbers.append(num)

    def compute_sum(self):
        total = sum(self.numbers)
        print(f"The sum of all numbers is {total}")

# Run the program
if __name__ == "__main__":
    calc = SumCalculator()
    calc.get_inputs()
    calc.compute_sum()
