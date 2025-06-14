class EqualityChecker:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def check(self):
        if self.first == self.second:
            print("The two numbers you gave are equal")
        else:
            print("The two numbers you gave are not equal")

# Run the program
if __name__ == "__main__":
    checker = EqualityChecker()
    checker.check()
