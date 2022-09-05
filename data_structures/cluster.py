from data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name, network_list, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        self.name = name
        self.security_level = security_level
        self.networks = [
            NetworkCollection(key, value) for key, value in network_list.items()
        ]

    def __str__(self):
        return f"{self.name} - {self.security_level} - " + "<->".join(
            [str(network) for network in self.networks]
        )

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return (
            self.name == other.name
            and self.networks == other.networks
            and self.security_level == other.security_level
        )
