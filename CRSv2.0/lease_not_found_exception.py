class LeaseNotFoundException(Exception):
    def __init__(self, message="Lease not found."):
        super().__init__(message)
