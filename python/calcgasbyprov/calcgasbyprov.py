import json
import sys

def calculate_fuel_consumption(fuel_efficiency, distances, cost_per_liter):
    total_fuel_consumption = 0
    total_cost = 0
    for destination in distances:
        # Assume the province is given in the destination dictionary
        province = destination.get('province')
        distance = destination.get('distance')
        # Retrieve province-specific fuel efficiency and cost per liter
        prov_fuel_efficiency = fuel_efficiency.get(province)
        prov_cost_per_liter = cost_per_liter.get(province)
        
        if prov_fuel_efficiency is None or prov_cost_per_liter is None:
            print(f"Error: Fuel efficiency or cost per liter not provided for province {province}.")
            continue
        
        # Calculate consumption and cost for the current destination
        dest_fuel_consumption = (prov_fuel_efficiency / 100) * distance
        dest_cost = dest_fuel_consumption * prov_cost_per_liter
        total_fuel_consumption += dest_fuel_consumption
        total_cost += dest_cost
        
    return total_fuel_consumption, total_cost

def print_usage():
    usage_text = (
        "Usage:\n"
        "  script.exe <filename> : Calculates gas consumption based on the JSON file provided.\n"
        "  script.exe /?         : Displays this help message.\n\n"
        "The JSON file format:\n"
        "[\n"
        "  {\n"
        "    \"fuel_efficiency\": {\"province1\": <value>, \"province2\": <value>, ...},\n"
        "    \"destinations\": [{\"province\": \"province1\", \"distance\": <value>}, ...],\n"
        "    \"cost_per_liter\": {\"province1\": <value>, \"province2\": <value>, ...}\n"
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
        destinations = record.get('destinations')
        cost_per_liter = record.get('cost_per_liter')

        if fuel_efficiency is None or destinations is None or cost_per_liter is None:
            print("Error: One or more required fields are missing in the record.")
            continue

        total_fuel_consumption, total_cost = calculate_fuel_consumption(fuel_efficiency, destinations, cost_per_liter)
        
        # Print the results
        for destination in destinations:
            print(f"Destination: {destination['province']}, Distance: {destination['distance']} km")
        print(f"Fuel Efficiency by province: {fuel_efficiency}")
        print(f"Cost per Liter by province: {cost_per_liter}")
        print(f"Total Fuel Consumption: {total_fuel_consumption:.2f} L")
        print(f"Total Cost: ${total_cost:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()
