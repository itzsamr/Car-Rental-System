class CarNotFoundException(Exception):
    def __init__(self, message="Car not found."):
        super().__init__(message)
