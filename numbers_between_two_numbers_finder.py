class BetweenNumbers:
    def __init__(self):
        self.first = int(input("Give two more numbers = "))
        self.second = int(input("Last one = "))
        self.in_between = []

    def collect_numbers(self):
        for number in range(self.first + 1, self.second):
            self.in_between.append(number)

    def show_result(self):
        print(self.in_between)

# Run the program
if __name__ == "__main__":
    numbers = BetweenNumbers()
    numbers.collect_numbers()
    numbers.show_result()
