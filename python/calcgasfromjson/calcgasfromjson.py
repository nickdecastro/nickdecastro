import json
import sys

def calculate_fuel_consumption(fuel_efficiency, distance, cost_per_liter):
    total_fuel_consumption = (fuel_efficiency / 100) * distance
    total_cost = total_fuel_consumption * cost_per_liter
    return total_fuel_consumption, total_cost

def print_usage():
    usage_text = (
        "Usage:\n"
        "  script.exe <filename> : Calculates gas consumption based on the JSON file provided.\n"
        "  script.exe /?         : Displays this help message.\n\n"
        "The JSON file format:\n"
        "[\n"
        "  {\n"
        "    \"fuel_efficiency\": <value>,\n"
        "    \"distance\": <value>,\n"
        "    \"cost_per_liter\": <value>\n"
        "  },\n"
        "  ...\n"
        "]"
    )
    print(usage_text)

def main():
    # Check if user asks for help
    if len(sys.argv) == 2 and sys.argv[1] in ("/?", "/"):
        print_usage()
        sys.exit(0)

    # Check if the file name is provided
    if len(sys.argv) < 2:
        print("Error: No filename provided.")
        print_usage()
        sys.exit(1)

    # Read the file name from command line arguments
    filename = sys.argv[1]

    # Attempt to read the data from the JSON file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' contains invalid JSON.")
        sys.exit(1)

    # Calculate the fuel consumption and cost for each record
    for record in data:
        fuel_efficiency = record.get('fuel_efficiency')
        distance = record.get('distance')
        cost_per_liter = record.get('cost_per_liter')

        if fuel_efficiency is None or distance is None or cost_per_liter is None:
            print("Error: One or more required fields are missing in the record.")
            continue

        total_fuel_consumption, total_cost = calculate_fuel_consumption(fuel_efficiency, distance, cost_per_liter)
        
        # Print the results
        print(f"Distance: {distance} km")
        print(f"Fuel Efficiency: {fuel_efficiency} L/100km")
        print(f"Cost per Liter: ${cost_per_liter}")
        print(f"Total Fuel Consumption: {total_fuel_consumption:.2f} L")
        print(f"Total Cost: ${total_cost:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()