import pytest

from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter


def mock_cluster(cluster_name, networks=None, security_level=1):
    return Cluster(cluster_name, networks or {}, security_level)


def to_mock_cluster_list(cluster_dict):
    return [
        mock_cluster(key, value["networks"], value["security_level"])
        for key, value in cluster_dict.items()
    ]


def mock_cluster_dict(*cluster_names):
    return {
        cluster_name: {
            "networks": {
                "10.0.8.0/22": [
                    {
                        "address": "10.0.11.254",
                        "available": True,
                        "last_used": "30/01/20 " "17:00:00",
                    },
                ],
                "192.168.0.0/24": [
                    {
                        "address": "255.255.255.0",
                        "available": True,
                        "last_used": "30/01/20 " "17:00:00",
                    },
                ],
            },
            "security_level": 1,
        }
        for cluster_name in cluster_names
    }


class TestDatacenter:
    @pytest.mark.parametrize(
        "name, cluster_list, expected",
        [
            (
                "Berlin",
                mock_cluster_dict("BER-1", "BER-100", "TEST-1"),
                to_mock_cluster_list(mock_cluster_dict("BER-1", "BER-100")),
            ),
            (
                "Paris",
                mock_cluster_dict("PAR-1", "PAR-999", "PAR"),
                to_mock_cluster_list(mock_cluster_dict("PAR-1", "PAR-999")),
            ),
            ("Madrid", mock_cluster_dict("MAD-", "MAD-109284", "10"), []),
            (
                "Berlin",
                mock_cluster_dict("BER-1", "BER-100"),
                to_mock_cluster_list(mock_cluster_dict("BER-1", "BER-100")),
            ),
        ],
    )
    def test_remove_invalid_clusters(self, name, cluster_list, expected):
        datacenter = Datacenter(name, cluster_list)
        datacenter.remove_invalid_clusters()
        assert datacenter.clusters == expected

    @pytest.mark.parametrize(
        "name, cluster, expected",
        [
            ("Berlin", mock_cluster("BER-1"), True),
            ("Berlin", mock_cluster("BER-100"), True),
            ("Berlin", mock_cluster("BER-1000"), False),
            ("Berlin", mock_cluster("TEST-1"), False),
        ],
    )
    def test_is_cluster_in_datacenter(self, name, cluster, expected):
        datacenter = Datacenter(name, {})
        assert datacenter._is_cluster_in_datacenter(cluster) == expected
