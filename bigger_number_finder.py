class NumberComparer:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def compare(self):
        if self.first >= self.second:
            print(f"{self.first} is the bigger number")
        else:
            print(f"{self.second} is the bigger number")

# Run the program
if __name__ == "__main__":
    comparer = NumberComparer()
    comparer.compare()
