class UniqueChecker:
    def __init__(self):
        self.numbers = []

    def run(self):
        try:
            while True:
                num = int(input("Give me a number = "))
                if num not in self.numbers:
                    print("Unique")
                    self.numbers.append(num)
                    print(self.numbers)
                else:
                    print("Duplicate")
        except ValueError:
            print("Invalid!")

# Run the program
if __name__ == "__main__":
    checker = UniqueChecker()
    checker.run()
