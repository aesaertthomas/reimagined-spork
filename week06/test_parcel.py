# Ex Homework 1 - test class Parcel
from model.Parcel import Parcel

bol = Parcel("GSM", 3, 3, 4)
print(bol)
print(f"Volume of the parcel is: {bol.volume:.2f} cm³")

amazon = Parcel("Amazon", 3.3, 34, 3)
print(amazon)
print(f"Volume of the parcel is: {amazon.volume:.2f} cm³")

