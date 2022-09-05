import ipaddress

from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipaddress.IPv4Network(ipv4_network)
        self.entries = [Entry(**entry) for entry in raw_entry_list]

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        self.entries = [
            entry for entry in self.entries if self._is_entry_in_network(entry)
        ]

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)

    def _is_entry_in_network(self, entry):
        try:
            address = ipaddress.ip_address(entry.address)
            return address in self.ipv4_network
        except ValueError:
            return False

    def __str__(self):
        return f"{self.ipv4_network} - " + " ".join(
            [str(entry) for entry in self.entries]
        )

    def __eq__(self, other):
        if not isinstance(other, NetworkCollection):
            return False

        return self.ipv4_network == other.ipv4_network and self.entries == other.entries
