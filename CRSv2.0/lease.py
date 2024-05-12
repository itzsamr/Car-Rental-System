class Lease:
    def __init__(
        self, __leaseID, __vehicleID, __customerID, __startDate, __endDate, __leaseType
    ):
        self.leaseID = __leaseID
        self.vehicleID = __vehicleID
        self.customerID = __customerID
        self.startDate = __startDate
        self.endDate = __endDate
        self.leaseType = __leaseType
