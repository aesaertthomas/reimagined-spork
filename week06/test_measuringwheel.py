# Ex05
# Test class MeasuringWheel
from model.MeasuringWheel import MeasuringWheel

measuring_wheel1 = MeasuringWheel(0.9)  # radius
measuring_wheel2 = MeasuringWheel(0.45, 123)  # radius , rotations
print(measuring_wheel1)
print(measuring_wheel2)

waarde = input("Enter the number of rotations or close with 'c':> ")
while (waarde != "c" and waarde.isnumeric()):
    measuring_wheel1.rotations += int(waarde)
    waarde = input(
        "Enter the number of rotations or close with 'c':> ")
print(measuring_wheel1)
print(f"Measuring wheel1 covered this distance: {measuring_wheel1.distance():.2f}m")
