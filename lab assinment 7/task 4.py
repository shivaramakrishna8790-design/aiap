class Rectangle:
    def __init__(self, length, width):  # ✅ Added 'self'
        self.length = length
        self.width = width

    def display(self):
        print(f"Length: {self.length}, Width: {self.width}")

# Example
r = Rectangle(10, 5)
r.display()
