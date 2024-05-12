from tabulate import tabulate
from customer_dao import CustomerDAO
from vehicle_dao import VehicleDAO
from lease_dao import LeaseDAO
from payment_dao import PaymentDAO
from customer_not_found_exception import CustomerNotFoundException
from car_not_found_exception import CarNotFoundException
from lease_not_found_exception import LeaseNotFoundException
from vehicle import Vehicle
from customer import Customer
from lease import Lease
from payment import Payment


def main():
    customer_dao = CustomerDAO()
    vehicle_dao = VehicleDAO()
    lease_dao = LeaseDAO()
    payment_dao = PaymentDAO()

    while True:
        print("\nMain Menu:")
        print("1. Customer Management")
        print("2. Vehicle Management")
        print("3. Lease Management")
        print("4. Payment Handling")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\nCustomer Management:")
                print("1. Add Customer")
                print("2. Remove Customer")
                print("3. List Customers")
                print("4. Find Customer by ID")
                print("5. Back to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    # Add Customer
                    customer_id = input("Enter new customer ID: ")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    email = input("Enter email: ")
                    phone_number = input("Enter phone number: ")
                    customer_dao.add_customer(
                        customer_id, first_name, last_name, email, phone_number
                    )

                elif sub_choice == "2":
                    # Remove Customer
                    customer_id = input("Enter customer ID to remove: ")
                    customer_dao.remove_customer(customer_id)

                elif sub_choice == "3":
                    # List Customers
                    try:
                        customers = customer_dao.list_customers()
                        if customers:
                            headers = [
                                "Customer ID",
                                "First Name",
                                "Last Name",
                                "Email",
                                "Phone Number",
                            ]
                            table = [
                                [
                                    customer.customerID,
                                    customer.firstName,
                                    customer.lastName,
                                    customer.email,
                                    customer.phoneNumber,
                                ]
                                for customer in customers
                            ]
                            print(tabulate(table, headers, tablefmt="grid"))
                        else:
                            print("No customers found.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub_choice == "4":
                    # Find Customer by ID
                    customer_id = input("Enter customer ID to find: ")
                    try:
                        customer = customer_dao.find_customer_by_id(customer_id)
                        if customer:
                            headers = [
                                "Customer ID",
                                "First Name",
                                "Last Name",
                                "Email",
                                "Phone Number",
                            ]
                            table = [
                                [
                                    customer.customerID,
                                    customer.firstName,
                                    customer.lastName,
                                    customer.email,
                                    customer.phoneNumber,
                                ]
                            ]
                            print(tabulate(table, headers, tablefmt="grid"))
                        else:
                            print("Customer not found.")
                    except CustomerNotFoundException as e:
                        print(f"Error: {e}")

                elif sub_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                print("\nVehicle Management:")
                print("1. Add Vehicle")
                print("2. Remove Vehicle")
                print("3. List Available Cars")
                print("4. List Rented Cars")
                print("5. Find Car by ID")
                print("6. Back to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    # Add Vehicle
                    vehicle_id = input("Enter vehicle ID: ")
                    make = input("Enter make: ")
                    model = input("Enter model: ")
                    year = int(input("Enter year: "))
                    daily_rate = float(input("Enter daily rate: "))
                    status = input("Enter status (available/notAvailable): ")
                    passenger_capacity = int(input("Enter passenger capacity: "))
                    engine_capacity = float(input("Enter engine capacity: "))

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
                    vehicle_dao.add_vehicle(vehicle)

                elif sub_choice == "2":
                    # Remove Vehicle
                    vehicle_id = input("Enter vehicle ID to remove: ")
                    vehicle_dao.remove_vehicle(vehicle_id)

                elif sub_choice == "3":
                    # List Available Cars
                    cars = vehicle_dao.list_available_cars()
                    car_data = [
                        [
                            car.vehicleID,
                            car.make,
                            car.model,
                            car.year,
                            car.dailyRate,
                            car.status,
                            car.passengerCapacity,
                            car.engineCapacity,
                        ]
                        for car in cars
                    ]
                    headers = [
                        "ID",
                        "Make",
                        "Model",
                        "Year",
                        "Daily Rate",
                        "Status",
                        "Passenger Capacity",
                        "Engine Capacity",
                    ]
                    print(tabulate(car_data, headers, tablefmt="grid"))

                elif sub_choice == "4":
                    # List Rented Cars
                    cars = vehicle_dao.list_rented_cars()
                    car_data = [
                        [
                            car.vehicleID,
                            car.make,
                            car.model,
                            car.year,
                            car.dailyRate,
                            car.status,
                            car.passengerCapacity,
                            car.engineCapacity,
                        ]
                        for car in cars
                    ]
                    headers = [
                        "ID",
                        "Make",
                        "Model",
                        "Year",
                        "Daily Rate",
                        "Status",
                        "Passenger Capacity",
                        "Engine Capacity",
                    ]
                    print(tabulate(car_data, headers, tablefmt="grid"))

                elif sub_choice == "5":
                    # Find Car by ID
                    car_id = input("Enter car ID to find: ")
                    car = vehicle_dao.find_car_by_id(car_id)
                    if car:
                        car_data = [
                            [
                                car.vehicleID,
                                car.make,
                                car.model,
                                car.year,
                                car.dailyRate,
                                car.status,
                                car.passengerCapacity,
                                car.engineCapacity,
                            ]
                        ]
                        headers = [
                            "ID",
                            "Make",
                            "Model",
                            "Year",
                            "Daily Rate",
                            "Status",
                            "Passenger Capacity",
                            "Engine Capacity",
                        ]
                        print(tabulate(car_data, headers, tablefmt="grid"))
                    else:
                        print("Car not found.")

                elif sub_choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                print("\nLease Management:")
                print("1. Create Lease")
                print("2. Return Car")
                print("3. List Active Leases")
                print("4. List Lease History")
                print("5. Back to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    # Create Lease
                    pass
                elif sub_choice == "2":
                    # Return Car
                    pass
                elif sub_choice == "3":
                    # List Active Leases
                    leases = lease_dao.list_active_leases()
                    lease_data = [
                        [
                            lease.leaseID,
                            lease.vehicleID,
                            lease.customerID,
                            lease.startDate,
                            lease.endDate,
                            lease.type,
                        ]
                        for lease in leases
                    ]
                    print(
                        tabulate(
                            lease_data,
                            headers=[
                                "Lease ID",
                                "Vehicle ID",
                                "Customer ID",
                                "Start Date",
                                "End Date",
                                "Type",
                            ],
                        )
                    )
                elif sub_choice == "4":
                    # List Lease History
                    leases = lease_dao.list_lease_history()
                    lease_data = [
                        [
                            lease.leaseID,
                            lease.vehicleID,
                            lease.customerID,
                            lease.startDate,
                            lease.endDate,
                            lease.type,
                        ]
                        for lease in leases
                    ]
                    print(
                        tabulate(
                            lease_data,
                            headers=[
                                "Lease ID",
                                "Vehicle ID",
                                "Customer ID",
                                "Start Date",
                                "End Date",
                                "Type",
                            ],
                        )
                    )
                elif sub_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            while True:
                print("\nPayment Handling:")
                print("1. Record Payment")
                print("2. Retrieve Payment History")
                print("3. Calculate Total Revenue")
                print("4. Back to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    # Record Payment
                    pass
                elif sub_choice == "2":
                    # Retrieve Payment History
                    pass
                elif sub_choice == "3":
                    # Calculate Total Revenue
                    pass
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
