class Car:
    def __init__(self, brand, model, fuel_type, horsepower, year, body_type, transmission, price, heated_seats, trunk_volume, wheel_size, country_of_origin):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.horsepower = horsepower
        self.year = year
        self.body_type = body_type
        self.transmission = transmission
        self.price = price
        self.trunk_volume = trunk_volume
        self.country_of_origin = country_of_origin  
        self.wheel_size = wheel_size
        self.heated_seats = heated_seats

    def __repr__(self):
        return (f"{self.brand} {self.model} ({self.year}), {self.fuel_type}, {self.horsepower} HP, "
                f"{self.body_type}, Transmission: {self.transmission}, Price: {self.price} USD, "
                f"Heated Seats: {self.heated_seats}, Trunk Volume: {self.trunk_volume} L, "
                f"Wheel Size: {self.wheel_size} inches, Country of Origin: {self.country_of_origin}")

class ExpertSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def apply_rules(self, car):
        for rule in self.rules:
            if not rule(car):
                return False
        return True
    
#Rules
  
    def filter_by_fuel_type(self, fuel_type):
        return [car for car in self.cars if car.fuel_type == fuel_type]

    def filter_by_year_range(self, min_year, max_year):
        return [car for car in self.cars if min_year <= car.year <= max_year]

    def filter_by_horsepower(self, min_hp, max_hp):
        return [car for car in self.cars if min_hp <= car.horsepower <= max_hp]

    def filter_by_body_type(self, body_type):
        return [car for car in self.cars if car.body_type == body_type]

    def filter_by_transmission(self, transmission):
        return [car for car in self.cars if car.transmission == transmission]

    def filter_by_price_range(self, min_price, max_price):
        return [car for car in self.cars if min_price <= car.price <= max_price]

    def filter_by_heated_seats(self, heated_seats):
        return [car for car in self.cars if car.heated_seats == heated_seats]

    def filter_by_trunk_volume(self, min_trunk_volume):
        return [car for car in self.cars if car.trunk_volume >= min_trunk_volume]

    def filter_by_wheel_size(self, min_wheel_size):
        return [car for car in self.cars if car.wheel_size >= min_wheel_size]

    def filter_by_country_of_origin(self, country_of_origin):
        return [car for car in self.cars if car.country_of_origin == country_of_origin] 
    


# Adding cars to the database
expert_system = ExpertSystem()
expert_system.add_car(Car("Toyota", "Land Cruiser", "Gasoline", 300, 2021, "SUV", "Automatic", 85000, True, 750, 18, "Japan"))
expert_system.add_car(Car("Ford", "Mustang Mach-E", "Electric", 340, 2022, "Crossover", "Automatic", 55000, True, 500, 19, "USA"))
expert_system.add_car(Car("Audi", "Q8", "Diesel", 250, 2020, "SUV", "Automatic", 70000, True, 500, 20, "Germany"))
expert_system.add_car(Car("BMW", "iX", "Electric", 500, 2022, "Crossover", "Automatic", 100000, True, 600, 21, "Germany"))
expert_system.add_car(Car("Hyundai", "Ioniq 5", "Electric", 280, 2022, "Hatchback", "Automatic", 45000, True, 500, 20, "South Korea"))
expert_system.add_car(Car("Nissan", "Ariya", "Electric", 250, 2022, "Crossover", "Automatic", 55000, True, 450, 19, "Japan"))
expert_system.add_car(Car("Chevrolet", "Bolt EV", "Electric", 200, 2021, "Hatchback", "Automatic", 37000, False, 400, 18, "USA"))
expert_system.add_car(Car("Ford", "F-150 Lightning", "Electric", 426, 2022, "Pickup", "Automatic", 90000, True, 1200, 22, "USA"))
expert_system.add_car(Car("Porsche", "Taycan", "Electric", 616, 2021, "Sedan", "Automatic", 105000, True, 400, 21, "Germany"))
expert_system.add_car(Car("Volkswagen", "ID.4", "Electric", 295, 2022, "Crossover", "Automatic", 52000, True, 500, 20, "Germany"))
expert_system.add_car(Car("Kia", "EV6", "Electric", 320,  2022, "Crossover", "Automatic", 65000, True, 500, 19, "South Korea"))
expert_system.add_car(Car("Tesla", "Model Y", "Electric", 450, 2021, "Crossover", "Automatic", 70000, True, 550, 21, "USA"))
expert_system.add_car(Car("BMW", "X5 M", "Gasoline", 617, 2021, "SUV", "Automatic", 120000, True, 500, 22, "Germany"))
expert_system.add_car(Car("Land Rover", "Range Rover", "Diesel", 300, 2020, "SUV", "Automatic", 90000, True, 550, 21, "UK"))
expert_system.add_car(Car("Mercedes", "GLE", "Diesel", 330, 2021, "SUV", "Automatic", 95000, True, 600, 22, "Germany"))
expert_system.add_car(Car("Chevrolet", "Tahoe", "Diesel", 355, 2021, "SUV", "Automatic", 95000, True, 1000, 20, "USA"))
expert_system.add_car(Car("Jeep", "Grand Cherokee", "Gasoline", 295, 2021, "SUV", "Automatic", 75000, True, 700, 19, "USA"))
expert_system.add_car(Car("Ram", "1500 TRX", "Gasoline", 702, 2021, "Pickup", "Automatic", 80000, True, 1200, 22, "USA"))
expert_system.add_car(Car("Ford", "Explorer", "Gasoline", 400, 2021, "SUV", "Automatic", 65000, True, 800, 20, "USA"))
expert_system.add_car(Car("Audi", "Q7", "Diesel", 333, 2022, "SUV", "Automatic", 85000, True, 600, 21, "Germany"))
expert_system.add_car(Car("Mazda", "CX-5", "Diesel", 175, 2022, "SUV", "Automatic", 45000, True, 500, 18, "Japan"))
expert_system.add_car(Car("Toyota", "Highlander", "Hybrid", 243, 2022, "SUV", "Automatic", 75000, True, 600, 19, "Japan"))
expert_system.add_car(Car("Subaru", "Outback", "Gasoline", 182, 2020, "Crossover", "Automatic", 45000, False, 450, 18, "Japan"))
expert_system.add_car(Car("Hyundai", "Santa Fe", "Diesel", 200, 2020, "SUV", "Automatic", 62000, True, 750, 19, "South Korea"))
expert_system.add_car(Car("Ford", "Bronco", "Gasoline", 330, 2021, "SUV", "Automatic", 70000, True, 800, 20, "USA"))
expert_system.add_car(Car("Volkswagen", "Tiguan", "Gasoline", 220, 2020, "Crossover", "Automatic", 55000, True, 400, 18, "Germany"))
expert_system.add_car(Car("Porsche", "Macan", "Gasoline", 265, 2021, "Crossover", "Automatic", 75000, True, 500, 19, "Germany"))
expert_system.add_car(Car("Mercedes", "GLC", "Gasoline", 255, 2021, "Crossover", "Automatic", 80000, True, 550, 20, "Germany"))
expert_system.add_car(Car("BMW", "X3", "Diesel", 265, 2021, "SUV", "Automatic", 70000, True, 600, 21, "Germany"))
expert_system.add_car(Car("Volvo", "XC90", "Hybrid", 400, 2021, "SUV", "Automatic", 85000, True, 600, 21, "Sweden"))
expert_system.add_car(Car("Toyota", "RAV4", "Hybrid", 219, 2023, "Crossover", "Automatic", 40000, True, 500, 18, "Japan"))
expert_system.add_car(Car("Kia", "Sorento", "Hybrid", 227, 2023, "SUV", "Automatic", 65000, True, 650, 19, "South Korea"))
expert_system.add_car(Car("Jaguar", "I-Pace", "Electric", 394, 2022, "Crossover", "Automatic", 95000, True, 400, 20, "UK"))
expert_system.add_car(Car("Honda", "Pilot", "Gasoline", 280, 2021, "SUV", "Automatic", 60000, True, 800, 19, "Japan"))
expert_system.add_car(Car("Subaru", "Forester", "Gasoline", 182, 2020, "Crossover", "Automatic", 45000, False, 450, 18, "Japan"))
expert_system.add_car(Car("Chevrolet", "Traverse", "Gasoline", 310,  2021, "SUV", "Automatic", 70000, True, 700, 20, "USA"))
expert_system.add_car(Car("Cadillac", "XT6", "Gasoline", 310, 2021, "Crossover", "Automatic", 75000, True, 600, 19, "USA"))
expert_system.add_car(Car("Lincoln", "Aviator", "Gasoline", 400, 2022, "Crossover", "Automatic", 80000, True, 700, 20, "USA"))
expert_system.add_car(Car("BMW", "X6", "Gasoline", 335, 2021, "SUV", "Automatic", 120000, True, 750, 22, "Germany"))
expert_system.add_car(Car("Ford", "Focus", "Gasoline", 150, 2021, "Hatchback", "Manual", 25000, False, 350, 15, "USA"))
expert_system.add_car(Car("Volkswagen", "Golf", "Diesel", 130, 2020, "Hatchback", "Manual", 23000, False, 400, 16, "Germany"))
expert_system.add_car(Car("Mazda", "Mazda3", "Gasoline", 155, 2021, "Hatchback", "Manual", 25000, False, 350, 17, "Japan"))
expert_system.add_car(Car("Chevrolet", "Spark", "Gasoline", 98, 2020, "Hatchback", "Manual", 15000, False, 250, 14, "USA"))

# Function to choose an option
def choose_option(prompt, options):
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    while True:
        try:
            choice = int(input(f"Choose an option (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Choose a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a number.")

# Questionnaire for selecting car characteristics
print("Welcome to the car selection system!")

fuel_type = choose_option("Select your preferred fuel type:", ["Gasoline", "Diesel", "Electric", "Hybrid"])
country_of_origin = choose_option("Select the country of origin:", ["Japan", "Germany", "USA", "South Korea", "Sweden"])
min_year = int(input("Enter the minimum year of manufacture: "))
max_year = int(input("Enter the maximum year of manufacture: "))
min_hp = int(input("Enter the minimum horsepower: "))
max_hp = int(input("Enter the maximum horsepower: "))
body_type = choose_option("Select your preferred body type:", ["Sedan", "Coupe", "SUV", "Crossover", "Hatchback"])
transmission = choose_option("Select the type of transmission:", ["Automatic", "Manual"]) 
min_price = float(input("Enter the minimum price (USD): "))
max_price = float(input("Enter the maximum price (USD): "))
min_trunk_volume = float(input("Enter the minimum trunk volume (L): "))
min_wheel_size = float(input("Enter the minimum wheel size (inches): "))
heated_seats = choose_option("Do you need heated seats?", ["Yes", "No"])

# Convert 'Yes'/'No' to boolean value
heated_seats = True if heated_seats == "Yes" else False


# Filter by all parameters

filtered_cars = expert_system.filter_by_fuel_type(fuel_type)
print(f"After fuel type filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if min_year <= car.year <= max_year]
print(f"After year filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if min_hp <= car.horsepower <= max_hp]
print(f"After horsepower filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if car.body_type == body_type]
print(f"After body type filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if car.transmission == transmission]
print(f"After transmission filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if min_price <= car.price <= max_price]
print(f"After price filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if car.heated_seats == heated_seats]
print(f"After heated seats filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if car.trunk_volume >= min_trunk_volume]
print(f"After trunk volume filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if car.wheel_size >= min_wheel_size]
print(f"After wheel size filter: {len(filtered_cars)} cars found")

filtered_cars = [car for car in filtered_cars if car.country_of_origin == country_of_origin]
print(f"After country of origin filter: {len(filtered_cars)} cars found")

# Display the search results
print("Search results:")
for car in filtered_cars:
    print(car)

    
    
    