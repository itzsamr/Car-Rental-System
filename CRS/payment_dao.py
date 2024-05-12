from DBConnUtil import DBConnUtil


class PaymentDAO:
    def record_payment(self, leaseID, amount):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Payment (leaseID, paymentDate, amount) VALUES (?, GETDATE(), ?)",
                (leaseID, amount),
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
