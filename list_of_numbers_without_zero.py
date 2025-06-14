class ZeroEndingFilter:
    def __init__(self):
        self.all_numbers = []
        self.filtered_numbers = []

    def generate_numbers(self):
        for number in range(101):
            self.all_numbers.append(number)

    def remove_ending_zero(self):
        for number in self.all_numbers:
            if number % 10 != 0:
                self.filtered_numbers.append(number)

    def display(self):
        print(self.filtered_numbers)

# Run the program
if __name__ == "__main__":
    filter_obj = ZeroEndingFilter()
    filter_obj.generate_numbers()
    filter_obj.remove_ending_zero()
    filter_obj.display()
