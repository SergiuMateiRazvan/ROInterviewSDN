class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

    def __gt__(self, other):
        return self.get_address_decimal() > other.get_address_decimal()

    def get_address_decimal(self):
        return int(self.address.split(".")[-1][0])

    def __str__(self):
        return f"{self.address} - {self.available} - {self.last_used}"

    def __eq__(self, other):
        if not isinstance(other, Entry):
            return False

        return (
            self.address == other.address
            and self.available == other.available
            and self.last_used == other.last_used
        )
