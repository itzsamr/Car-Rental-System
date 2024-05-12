from entity.lease import Lease
from util.DBConnUtil import DBConnUtil
from exception.lease_not_found_exception import LeaseNotFoundException


class LeaseDAO:
    def create_lease(
        self, leaseID, customerID, vehicleID, startDate, endDate, leaseType
    ):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Lease (leaseID, vehicleID, customerID, startDate, endDate, type) VALUES (?, ?, ?, ?, ?, ?)",
                (leaseID, vehicleID, customerID, startDate, endDate, leaseType),
            )
            conn.commit()
            print("Lease created successfully.")
        except Exception as e:
            print(f"Error creating lease: {e}")
        finally:
            if conn:
                conn.close()

    def return_car(self, leaseID):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Lease SET endDate = GETDATE() WHERE leaseID = ?", (leaseID,)
            )
            if cursor.rowcount == 0:
                raise LeaseNotFoundException(f"Lease with ID {leaseID} not found.")
            else:
                print("Car returned successfully.")
            conn.commit()
        except LeaseNotFoundException as lne:
            print(lne)
        except Exception as e:
            print(f"Error returning car: {e}")
        finally:
            if conn:
                conn.close()

    def list_active_leases(self):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Lease WHERE endDate IS NULL")
            leases = []
            for row in cursor.fetchall():
                lease = Lease(row[0], row[1], row[2], row[3], row[4], row[5])
                leases.append(lease)
            return leases
        except Exception as e:
            print(f"Error listing active leases: {e}")
        finally:
            if conn:
                conn.close()

    def list_lease_history(self):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Lease")
            leases = []
            for row in cursor.fetchall():
                lease = Lease(row[0], row[1], row[2], row[3], row[4], row[5])
                leases.append(lease)
            return leases
        except Exception as e:
            print(f"Error listing lease history: {e}")
        finally:
            if conn:
                conn.close()
