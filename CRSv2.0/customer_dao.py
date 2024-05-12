from customer import Customer
from DBConnUtil import DBConnUtil
from customer_not_found_exception import CustomerNotFoundException


class CustomerDAO:
    def add_customer(self, customer_id, first_name, last_name, email, phone_number):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Customer (customerID, firstName, lastName, email, phoneNumber) VALUES (?, ?, ?, ?, ?)",
                (customer_id, first_name, last_name, email, phone_number),
            )
            conn.commit()
            print("Customer added successfully.")
        except Exception as e:
            print(f"Error adding customer: {e}")
        finally:
            if conn:
                conn.close()

    def remove_customer(self, customerID):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Customer WHERE customerID = ?", (customerID,))
            if cursor.rowcount == 0:
                raise CustomerNotFoundException(
                    f"Customer with ID {customerID} not found."
                )
            else:
                print("Customer removed successfully.")
            conn.commit()
        except CustomerNotFoundException as cne:
            print(cne)
        except Exception as e:
            print(f"Error removing customer: {e}")
        finally:
            if conn:
                conn.close()

    def list_customers(self):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer")
            customers = []
            for row in cursor.fetchall():
                customer = Customer(row[0], row[1], row[2], row[3], row[4])
                customers.append(customer)
            return customers
        except Exception as e:
            print(f"Error listing customers: {e}")
        finally:
            if conn:
                conn.close()

    def find_customer_by_id(self, customerID):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE customerID = ?", (customerID,))
            row = cursor.fetchone()
            if row:
                return Customer(row[0], row[1], row[2], row[3], row[4])
            else:
                raise CustomerNotFoundException(
                    f"Customer with ID {customerID} not found."
                )
        except CustomerNotFoundException as cne:
            print(cne)
        except Exception as e:
            print(f"Error finding customer: {e}")
        finally:
            if conn:
                conn.close()
