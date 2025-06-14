class OddEvenCounter:
    def __init__(self):
        self.numbers = []
        self.odd_count = 0
        self.even_count = 0

    def get_inputs(self):
        for i in range(10):
            num = int(input(f"Enter number {i + 1} = "))
            self.numbers.append(num)

    def count_odd_even(self):
        for num in self.numbers:
            if num % 2 == 0:
                self.even_count += 1
            else:
                self.odd_count += 1

    def show_results(self):
        print(f"There are a total of {self.odd_count} odd numbers")
        print(f"There are a total of {self.even_count} even numbers")

# Run the program
if __name__ == "__main__":
    counter = OddEvenCounter()
    counter.get_inputs()
    counter.count_odd_even()
    counter.show_results()
