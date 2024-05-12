from DBConnUtil import DBConnUtil
from payment import Payment


class PaymentDAO:
    def record_payment(self, payment_id, lease_id, payment_date, amount):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Payment (paymentID, leaseID, paymentDate, amount) VALUES (?, ?, ?, ?)",
                (payment_id, lease_id, payment_date, amount),
            )
            conn.commit()
            print("Payment recorded successfully.")
        except Exception as e:
            print(f"Error recording payment: {e}")
        finally:
            if conn:
                conn.close()

    def retrieve_payment_history(self, customerID):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT p.paymentID, p.leaseID, p.paymentDate, p.amount "
                "FROM Payment p JOIN Lease l ON p.leaseID = l.leaseID "
                "WHERE l.customerID = ?",
                (customerID,),
            )
            payments = []
            for row in cursor.fetchall():
                payments.append(row)
            return payments
        except Exception as e:
            print(f"Error retrieving payment history: {e}")
        finally:
            if conn:
                conn.close()

    def calculate_total_revenue(self):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(amount) FROM Payment")
            total_revenue = cursor.fetchone()[0]
            return total_revenue
        except Exception as e:
            print(f"Error calculating total revenue: {e}")
        finally:
            if conn:
                conn.close()

    def list_all_payments(self):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Payment")
            payments = []
            for row in cursor.fetchall():
                payment = Payment(
                    paymentID=row[0], leaseID=row[1], paymentDate=row[2], amount=row[3]
                )
                payments.append(payment)
            conn.close()
            return payments
        except Exception as e:
            print(f"Error listing all payments: {e}")
