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
                    lease_id = input("Enter new lease ID: ")
                    customer_id = input("Enter customer ID: ")
                    car_id = input("Enter car ID: ")
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    lease_type = input("Enter lease type (DailyLease/MonthlyLease): ")
                    lease_dao.create_lease(
                        lease_id, customer_id, car_id, start_date, end_date, lease_type
                    )

                elif sub_choice == "2":
                    # Return Car
                    lease_id = input("Enter lease ID to return the car: ")
                    lease_dao.return_car(lease_id)

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
                    headers = [
                        "Lease ID",
                        "Vehicle ID",
                        "Customer ID",
                        "Start Date",
                        "End Date",
                        "Type",
                    ]
                    print(tabulate(lease_data, headers, tablefmt="grid"))

                elif sub_choice == "4":
                    # List Lease History
                    try:
                        leases = lease_dao.list_lease_history()
                        if leases:
                            lease_data = [
                                [
                                    lease.leaseID,
                                    lease.vehicleID,
                                    lease.customerID,
                                    lease.startDate,
                                    lease.endDate,
                                    lease.leaseType,
                                ]
                                for lease in leases
                            ]
                            headers = [
                                "Lease ID",
                                "Vehicle ID",
                                "Customer ID",
                                "Start Date",
                                "End Date",
                                "Type",
                            ]
                            print(
                                tabulate(lease_data, headers=headers, tablefmt="grid")
                            )
                        else:
                            print("No lease history found.")
                    except Exception as e:
                        print(f"Error listing lease history: {e}")

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
                    try:
                        payment_id = int(input("Enter new payment ID: "))
                        lease_id = int(input("Enter lease ID: "))
                        payment_date = input("Enter payment date (YYYY-MM-DD): ")
                        amount = float(input("Enter payment amount: "))
                        payment_dao.record_payment(
                            payment_id, lease_id, payment_date, amount
                        )
                        print("Payment recorded successfully.")
                    except ValueError:
                        print(
                            "Invalid input. Please enter valid lease ID, payment date, and payment amount."
                        )
                    except Exception as e:
                        print(f"Error recording payment: {e}")

                elif sub_choice == "2":
                    # Retrieve Payment History
                    try:
                        customer_id = int(input("Enter customer ID: "))

                        # Call the method to retrieve payment history from PaymentDAO
                        payments = payment_dao.retrieve_payment_history(customer_id)

                        if payments:
                            print("Payment History:")
                            for payment in payments:
                                print(
                                    f"Payment ID: {payment.paymentID}, Payment Date: {payment.paymentDate}, Amount: {payment.amount}"
                                )
                        else:
                            print("No payment history found for the given customer ID.")
                    except ValueError:
                        print("Invalid input. Please enter a valid customer ID.")
                    except Exception as e:
                        print(f"Error retrieving payment history: {e}")

                elif sub_choice == "3":
                    # Calculate Total Revenue
                    try:
                        total_revenue = payment_dao.calculate_total_revenue()
                        print(f"Total Revenue: {total_revenue}")
                    except Exception as e:
                        print(f"Error calculating total revenue: {e}")

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
