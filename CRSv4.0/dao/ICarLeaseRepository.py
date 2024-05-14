from abc import ABC, abstractmethod
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from datetime import date
from typing import List


class ICarLeaseRepository(ABC):
    @abstractmethod
    def addVehicle(self, vehicle: Vehicle) -> None:
        pass

    @abstractmethod
    def removeVehicle(self, vehicle_id: int) -> None:
        pass

    @abstractmethod
    def listAvailableVehicles(self) -> List[Vehicle]:
        pass

    @abstractmethod
    def listRentedVehicles(self) -> List[Vehicle]:
        pass

    @abstractmethod
    def findVehicleById(self, vehicle_id: int) -> Vehicle:
        pass

    @abstractmethod
    def addCustomer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def removeCustomer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def listCustomers(self) -> List[Customer]:
        pass

    @abstractmethod
    def findCustomerById(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def createLease(
        self, customer_id: int, vehicle_id: int, start_date: date, end_date: date
    ) -> Lease:
        pass

    @abstractmethod
    def returnVehicle(self, lease_id: int) -> Lease:
        pass

    @abstractmethod
    def listActiveLeases(self) -> List[Lease]:
        pass

    @abstractmethod
    def listLeaseHistory(self) -> List[Lease]:
        pass

    @abstractmethod
    def recordPayment(self, lease: Lease, amount: float) -> None:
        pass
