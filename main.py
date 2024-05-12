from tabulate import tabulate
from .dao import *
from .entity import *
from .util import *
from .exception import *
import sys

sys.path.append(
    "C:/Users/91915/OneDrive - Valliammai Engineering College/Desktop/CarRentalSystem/dao"
)
sys.path.append(
    "C:/Users/91915/OneDrive - Valliammai Engineering College/Desktop/CarRentalSystem/entity"
)
sys.path.append(
    "C:/Users/91915/OneDrive - Valliammai Engineering College/Desktop/CarRentalSystem/exception"
)
sys.path.append(
    "C:/Users/91915/OneDrive - Valliammai Engineering College/Desktop/CarRentalSystem/util"
)


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
                    try:
                        customer_id = input("Enter new customer ID: ")
                        first_name = input("Enter first name: ")
                        last_name = input("Enter last name: ")
                        email = input("Enter email: ")
                        phone_number = input("Enter phone number: ")
                        customer_dao.add_customer(
                            customer_id, first_name, last_name, email, phone_number
                        )
                        print("Customer added successfully.")
                    except Exception as e:
                        print(f"Error adding customer: {e}")

                elif sub_choice == "2":
                    # Remove Customer
                    try:
                        customer_id = input("Enter customer ID to remove: ")
                        customer_dao.remove_customer(customer_id)
                        print("Customer removed successfully.")
                    except Exception as e:
                        print(f"Error removing customer: {e}")

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
                        print(f"Error listing customers: {e}")

                elif sub_choice == "4":
                    # Find Customer by ID
                    try:
                        customer_id = input("Enter customer ID to find: ")
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
                    try:
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
                        print("Vehicle added successfully.")
                    except Exception as e:
                        print(f"Error adding vehicle: {e}")

                elif sub_choice == "2":
                    # Remove Vehicle
                    try:
                        vehicle_id = input("Enter vehicle ID to remove: ")
                        vehicle_dao.remove_vehicle(vehicle_id)
                        print("Vehicle removed successfully.")
                    except Exception as e:
                        print(f"Error removing vehicle: {e}")

                elif sub_choice == "3":
                    # List Available Cars
                    try:
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
                    except Exception as e:
                        print(f"Error listing available cars: {e}")

                elif sub_choice == "4":
                    # List Rented Cars
                    try:
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
                    except Exception as e:
                        print(f"Error listing rented cars: {e}")

                elif sub_choice == "5":
                    # Find Car by ID
                    try:
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
                    except Exception as e:
                        print(f"Error finding car: {e}")

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
                    try:
                        lease_id = input("Enter new lease ID: ")
                        customer_id = input("Enter customer ID: ")
                        car_id = input("Enter car ID: ")
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        lease_type = input(
                            "Enter lease type (DailyLease/MonthlyLease): "
                        )
                        lease_dao.create_lease(
                            lease_id,
                            customer_id,
                            car_id,
                            start_date,
                            end_date,
                            lease_type,
                        )
                        print("Lease created successfully.")
                    except Exception as e:
                        print(f"Error creating lease: {e}")

                elif sub_choice == "2":
                    # Return Car
                    try:
                        lease_id = input("Enter lease ID to return the car: ")
                        lease_dao.return_car(lease_id)
                        print("Car returned successfully.")
                    except Exception as e:
                        print(f"Error returning car: {e}")

                elif sub_choice == "3":
                    # List Active Leases
                    try:
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
                    except Exception as e:
                        print(f"Error listing active leases: {e}")

                elif sub_choice == "4":
                    # List Lease History
                    try:
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
                        headers = [
                            "Lease ID",
                            "Vehicle ID",
                            "Customer ID",
                            "Start Date",
                            "End Date",
                            "Type",
                        ]
                        print(tabulate(lease_data, headers, tablefmt="grid"))
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
                print("4. List All Payments")
                print("5. Back to Main Menu")

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
                    # List All Payments
                    try:
                        payments = payment_dao.list_all_payments()

                        if payments:
                            print("All Payments:")
                            payment_data = [
                                [
                                    payment.paymentID,
                                    payment.leaseID,
                                    payment.paymentDate,
                                    payment.amount,
                                ]
                                for payment in payments
                            ]
                            print(
                                tabulate(
                                    payment_data,
                                    headers=[
                                        "Payment ID",
                                        "Lease ID",
                                        "Payment Date",
                                        "Amount",
                                    ],
                                    tablefmt="grid",
                                )
                            )
                        else:
                            print("No payments found.")
                    except Exception as e:
                        print(f"Error listing all payments: {e}")

                elif sub_choice == "5":
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
