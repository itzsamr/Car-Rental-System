from .ICarLeaseRepository import ICarLeaseRepository
from datetime import date
from entity.vehicle import Vehicle
from entity.lease import Lease
from entity.customer import Customer
from entity.payment import Payment
from typing import List
from exception.myexceptions import VehicleNotFoundException
from util.DBConnection import DBConnection


class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.connection = DBConnection.getConnection()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()  # Commit changes to the database
        return cursor.fetchall()

    def addVehicle(self, vehicle: Vehicle) -> None:
        query = (
            f"INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity) "
            f"VALUES ('{vehicle.get_id()},'{vehicle.get_make()}', '{vehicle.get_model()}', {vehicle.get_year()}, {vehicle.get_daily_rate()}, "
            f"'{vehicle.get_status()}', {vehicle.get_passenger_capacity()}, {vehicle.get_engine_capacity()})"
        )
        self.execute_query(query)

    def removeVehicle(self, vehicle_id: int) -> None:
        query = f"DELETE FROM Vehicle WHERE vehicleID = {vehicle_id}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        if cursor.rowcount == 0:
            raise VehicleNotFoundException(vehicle_id)

    def listAvailableVehicles(self) -> List[Vehicle]:
        query = "SELECT * FROM Vehicle WHERE status = 'available'"
        rows = self.execute_query(query)
        vehicles = []
        for row in rows:
            vehicle = Vehicle(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
            )
            vehicles.append(vehicle)
        return vehicles

    def listRentedVehicles(self) -> List[Vehicle]:
        query = "SELECT * FROM Vehicle WHERE status = 'notAvailable'"
        rows = self.execute_query(query)
        vehicles = []
        for row in rows:
            vehicle = Vehicle(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
            )
            vehicles.append(vehicle)
        return vehicles

    def findVehicleById(self, vehicle_id: int) -> Vehicle:
        query = "SELECT * FROM Vehicle WHERE vehicleID = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (vehicle_id,))
        row = cursor.fetchone()

        if row is None:
            raise VehicleNotFoundException(vehicle_id)

        vehicle = Vehicle(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        )
        return vehicle

    def addCustomer(self, customer: Customer) -> None:
        # Implementation
        pass

    def removeCustomer(self, customer_id: int) -> None:
        # Implementation
        pass

    def listCustomers(self) -> List[Customer]:
        # Implementation
        pass

    def findCustomerById(self, customer_id: int) -> Customer:
        # Implementation
        pass

    def createLease(
        self, customer_id: int, vehicle_id: int, start_date: date, end_date: date
    ) -> Lease:
        # Implementation
        pass

    def returnVehicle(self, lease_id: int) -> Lease:
        # Implementation
        pass

    def listActiveLeases(self) -> List[Lease]:
        # Implementation
        pass

    def listLeaseHistory(self) -> List[Lease]:
        # Implementation
        pass

    def recordPayment(self, lease: Lease, amount: float) -> None:
        # Implementation
        pass
