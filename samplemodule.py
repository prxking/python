class SampleModule:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def div(self, x, y):
        if y == 0:
            return "Error: Division by zero is not allowed."
        return x / y
