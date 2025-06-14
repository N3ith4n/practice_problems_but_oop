class NumberFilter:
    def __init__(self):
        self.all_numbers = []
        self.filtered_numbers = []

    def generate_numbers(self):
        for number in range(101):
            self.all_numbers.append(number)

    def filter_numbers(self):
        for number in self.all_numbers:
            if number % 5 != 0 and number % 10 != 0:
                self.filtered_numbers.append(number)

    def display(self):
        print(self.filtered_numbers)

# Run the program
if __name__ == "__main__":
    nf = NumberFilter()
    nf.generate_numbers()
    nf.filter_numbers()
    nf.display()
