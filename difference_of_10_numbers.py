class Subtractor:
    def __init__(self):
        self.numbers = []
        self.get_inputs()

    def get_inputs(self):
        for i in range(10):
            num = int(input(f"Enter number {i + 1} = "))
            self.numbers.append(num)

    def subtract_rest(self):
        first = self.numbers[0]
        remaining_sum = sum(self.numbers[1:])
        result = first - remaining_sum
        print(result)

# Run the program
if __name__ == "__main__":
    subtractor = Subtractor()
    subtractor.subtract_rest()
