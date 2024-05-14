from .ICarLeaseRepository import ICarLeaseRepository
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from datetime import date
from typing import List


class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def addVehicle(self, vehicle: Vehicle) -> None:
        # Implementation
        pass

    def removeVehicle(self, vehicle_id: int) -> None:
        # Implementation
        pass

    def listAvailableVehicles(self) -> List[Vehicle]:
        # Implementation
        pass

    def listRentedVehicles(self) -> List[Vehicle]:
        # Implementation
        pass

    def findVehicleById(self, vehicle_id: int) -> Vehicle:
        # Implementation
        pass

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
