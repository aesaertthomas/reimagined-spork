# Ex03
# Test class Hotelguest

from model.Hotelguest import Hotelguest

guest1 = Hotelguest("Claerhout", "Joerie", -100, True)
guest2 = Hotelguest("Dewitte", "Marie", 300, False)

print("*** The following guests are staying with us: ")
print(guest1)
print(guest2)
print("**** checks out with error")
guest1.checked_in = "is leaving"
print(guest1)