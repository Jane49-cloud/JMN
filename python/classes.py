class MyComplexNumber:
    def __init__(self, real=0, imag=0):
        print("MyComplexNumber constructor is executing.....")
        self.real_part = real
        self.imag_part = imag

    def display(self):
        print("{0} + {1}j ".format(self.real_part, self.imag_part))


# creating a new object against the
complex1 = MyComplexNumber(40, 50)
complex1.display()
complex2 = MyComplexNumber(30, 54)
complex2.new_attribute = 60
print(complex2.real_part, complex2.imag_part, complex2.new_attribute)
