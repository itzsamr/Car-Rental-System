from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.vehicle import Vehicle
from exception.myexceptions import VehicleNotFoundException
from pyodbc import *


def car_management_menu(car_repository):
    while True:
        print("\nCar Management Menu:")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. List Available Cars")
        print("4. List Rented Cars")
        print("5. Find Car by ID")
        print("0. Go Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_id = int(input("Enter vehicle ID: "))
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            daily_rate = float(input("Enter daily rate: "))
            status = input("Enter status (available/notAvailable): ")
            passenger_capacity = int(input("Enter passenger capacity: "))
            engine_capacity = int(input("Enter engine capacity: "))

            vehicle = Vehicle(
                vehicle_id,
                make,
                model,
                year,
                daily_rate,
                status,
                passenger_capacity,
                engine_capacity,
            )
            car_repository.addVehicle(vehicle)
            print("Car added successfully.")

        elif choice == "2":
            vehicle_id = int(input("Enter vehicle ID to remove: "))
            car_repository.removeVehicle(vehicle_id)
            print("Car removed successfully.")

        elif choice == "3":
            available_cars = car_repository.listAvailableVehicles()
            print("Available Cars:")
            for car in available_cars:
                print(car.__dict__)

        elif choice == "4":
            rented_cars = car_repository.listRentedVehicles()
            print("Rented Cars:")
            for car in rented_cars:
                print(car.__dict__)

        elif choice == "5":
            vehicle_id = int(input("Enter vehicle ID to find: "))
            try:
                car = car_repository.findVehicleById(vehicle_id)
                print("Car found:")
                print(car.__dict__)
            except VehicleNotFoundException as e:
                print(e)

        elif choice == "0":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    car_repository = ICarLeaseRepositoryImpl()

    while True:
        print("\nMain Menu:")
        print("1. Car Management")
        print("2. Customer Management")
        print("3. Lease Management")
        print("4. Payment Handling")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            car_management_menu(car_repository)

        # Add other submenu options for Customer Management, Lease Management, and Payment Handling

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
