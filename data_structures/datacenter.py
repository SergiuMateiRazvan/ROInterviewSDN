import re

from data_structures.cluster import Cluster


class Datacenter:
    def __init__(self, name, cluster_list):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.clusters = [
            Cluster(key, value["networks"], value["security_level"])
            for key, value in cluster_list.items()
        ]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        self.clusters = [
            cluster
            for cluster in self.clusters
            if self._is_cluster_in_datacenter(cluster)
        ]

    def _is_cluster_in_datacenter(self, cluster):
        first_three_letters = self.name[:3].upper()
        return re.fullmatch(first_three_letters + r"-\d{1,3}", cluster.name) is not None

    def __str__(self):
        return f"{self.name}: " + ";".join([str(cluster) for cluster in self.clusters])
