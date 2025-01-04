class Car:
    def __init__(self, company, model, color, year):
        
        self.company = company
        self.model = model
        self.color = color
        self.year = year

    def display_info(self):
       
        print(f"Car Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")

def main():
    
    cars = []

    while True:
        print("\nCar Menu:")
        print("1. Add Car")
        print("2. View Cars")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            company = input("Enter car company: ")
            model = input("Enter car model: ")
            color = input("Enter car color: ")
            year = input("Enter car year: ")

            car = Car(company, model, color, year)
            cars.append(car)
            print("Car added successfully.")

        elif choice == '2':
            if not cars:
                print("No cars in the list.")
            else:
                print("\nCars in the List:")
                for car in cars:
                    car.display_info()
                    print("---------")  

        elif choice == '3':
            print("Exiting the car system.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
