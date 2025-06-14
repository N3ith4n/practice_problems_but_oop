class SmallerNumberFinder:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def find_smaller(self):
        if self.first <= self.second:
            print(f"{self.first} is the smaller number")
        else:
            print(f"{self.second} is the smaller number")

# Run the program
if __name__ == "__main__":
    finder = SmallerNumberFinder()
    finder.find_smaller()
