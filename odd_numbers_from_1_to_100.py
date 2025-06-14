class OddNumberPrinter:
    def __init__(self):
        self.odd_numbers = []

    def collect_odd_numbers(self):
        number = 0
        while number <= 100:
            if number % 2 == 1:
                self.odd_numbers.append(number)
            number += 1

    def display(self):
        print(self.odd_numbers)

# Run the program
if __name__ == "__main__":
    printer = OddNumberPrinter()
    printer.collect_odd_numbers()
    printer.display()
