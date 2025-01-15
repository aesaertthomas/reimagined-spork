# test class Fraction
from model.Fraction import Fraction
print("Fraction 1: ")
b1 = Fraction(3, 4)
print(b1)
print("Change denominator to 6: ")
b1.denominator = 6
print(b1)
print("Simplify fraction 1: ")
b1.simplify()
print(b1)
print("\nFraction 2 after simplification: ")
b2 = Fraction(4, 10)
b2.simplify
print(b2)