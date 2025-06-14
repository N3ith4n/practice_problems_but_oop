class NumberChecker:
    def __init__(self):
        self.numbers = []
        self.unique = []
        self.duplicates = []
        self.get_inputs()

    def get_inputs(self):
        for i in range(10):
            num = int(input(f"Enter number {i + 1} = "))
            self.numbers.append(num)

    def check_duplicates(self):
        for num in self.numbers:
            if num not in self.unique and num not in self.duplicates:
                self.unique.append(num)
            elif num in self.unique:
                self.unique.remove(num)
                self.duplicates.append(num)

    def show_results(self):
        print(f"The numbers that don’t have duplicates are {self.unique}")
        print(f"The numbers that have duplicates are {self.duplicates}")

# Run the program
if __name__ == "__main__":
    checker = NumberChecker()
    checker.check_duplicates()
    checker.show_results()
