class ProductCalculator:
    def __init__(self):
        self.first = int(input("Give me some numbers, first one = "))
        self.second = int(input("second one = "))

    def multiply(self):
        product = self.first * self.second
        print(f"The product of the two numbers is {product}")

# Run the program
if __name__ == "__main__":
    calculator = ProductCalculator()
    calculator.multiply()
