from vehicle import Vehicle
from DBConnUtil import DBConnUtil
from car_not_found_exception import CarNotFoundException


class VehicleDAO:
    def add_vehicle(self, vehicle):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    vehicle.make,
                    vehicle.model,
                    vehicle.year,
                    vehicle.dailyRate,
                    vehicle.status,
                    vehicle.passengerCapacity,
                    vehicle.engineCapacity,
                ),
            )
            conn.commit()
            print("Vehicle added successfully.")
        except Exception as e:
            print(f"Error adding vehicle: {e}")
        finally:
            if conn:
                conn.close()

    def remove_vehicle(self, vehicleID):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Vehicle WHERE vehicleID = ?", (vehicleID,))
            if cursor.rowcount == 0:
                raise CarNotFoundException(f"Vehicle with ID {vehicleID} not found.")
            else:
                print("Vehicle removed successfully.")
            conn.commit()
        except CarNotFoundException as cne:
            print(cne)
        except Exception as e:
            print(f"Error removing vehicle: {e}")
        finally:
            if conn:
                conn.close()

    def list_available_cars(self):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE status = 'available'")
            cars = []
            for row in cursor.fetchall():
                car = Vehicle(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
                cars.append(car)
            return cars
        except Exception as e:
            print(f"Error listing available cars: {e}")
        finally:
            if conn:
                conn.close()

    def list_rented_cars(self):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE status = 'notAvailable'")
            cars = []
            for row in cursor.fetchall():
                car = Vehicle(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
                cars.append(car)
            return cars
        except Exception as e:
            print(f"Error listing rented cars: {e}")
        finally:
            if conn:
                conn.close()

    def find_car_by_id(self, vehicleID):
        try:
            conn = DBConnUtil.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE vehicleID = ?", (vehicleID,))
            row = cursor.fetchone()
            if row:
                return Vehicle(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
            else:
                raise CarNotFoundException(f"Vehicle with ID {vehicleID} not found.")
        except CarNotFoundException as cne:
            print(cne)
        except Exception as e:
            print(f"Error finding vehicle: {e}")
        finally:
            if conn:
                conn.close()
