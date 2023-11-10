import sys

# Check if the "/?" switch is provided as a command-line argument
if "/?" in sys.argv:
    print("Usage: calculategas.exe /?")
    print("This program calculates the total fuel consumption and cost for a given trip.")
    print("You will be prompted to enter the car's fuel efficiency (L/100km), the distance traveled (km),")
    print("and the cost of gas per liter ($/L).")
    sys.exit()

# Ask the user for the car's fuel efficiency (Liters per 100 kilometers)
fuel_efficiency = float(input("Enter the car's fuel efficiency (L/100km): "))

# Ask the user for the distance traveled (kilometers)
distance = float(input("Enter the distance traveled (km): "))

# Ask the user for the cost of gas per liter
cost_per_liter = float(input("Enter the cost of gas per liter ($/L): "))

# Calculate the total fuel consumption based on the distance
total_fuel_consumption = (fuel_efficiency / 100) * distance

# Calculate the total cost for the gas
total_cost = total_fuel_consumption * cost_per_liter

# Print the result
print(f"The total fuel consumption is {total_fuel_consumption:.2f} liters for {distance:.2f} kilometers.")
print(f"The total cost of the gas is ${total_cost:.2f}.")
