class EvenNumberPrinter:
    def __init__(self):
        self.range_list = []
        self.even_numbers = []

    def generate_range(self):
        for number in range(101):
            self.range_list.append(number)

    def filter_even(self):
        for number in self.range_list:
            if number % 2 == 0:
                self.even_numbers.append(number)

    def show_result(self):
        print(self.even_numbers)

# Run the program
if __name__ == "__main__":
    printer = EvenNumberPrinter()
    printer.generate_range()
    printer.filter_even()
    printer.show_result()
