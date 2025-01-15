# Ex04
# Test class Car

import random
from model.Car import Car

cars = []
cars.append(Car("Volkswagen", "passat", "darkgrey", "diesel"))
cars.append(Car("Opel", "astra", "green", "petrol"))
cars.append(Car("Seat", "ibiza", "blue", "diesel"))

for car in cars:
    print(f"Car {car} has on his km-counter {car.mileage} kms")

    
print("\nAt the end of the day: ")
for car in cars:
    car.drive(random.randint(10, 300))
    print(f"\tCar {car} has on his km-counter {car.mileage} kms and makes this noise: {car.make_noise()}")
