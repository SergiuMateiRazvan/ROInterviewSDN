import pytest

from data_structures.entry import Entry
from data_structures.network_collection import NetworkCollection


class TestNetworkCollection:
    @pytest.mark.parametrize(
        "network, entries, expected",
        [
            (
                "10.0.8.0/22",
                [
                    {
                        "address": "192.10.11.254",
                        "available": True,
                        "last_used": "30/01/20 " "17:00:00",
                    },
                    {
                        "address": "10.0.8.1",
                        "available": False,
                        "last_used": "30/01/20 " "16:00:00",
                    },
                    {
                        "address": "10.0.8.0",
                        "available": False,
                        "last_used": "30/01/20 " "16:00:00",
                    },
                ],
                [
                    Entry(**data)
                    for data in [
                        {
                            "address": "10.0.8.1",
                            "available": False,
                            "last_used": "30/01/20 " "16:00:00",
                        },
                        {
                            "address": "10.0.8.0",
                            "available": False,
                            "last_used": "30/01/20 " "16:00:00",
                        },
                    ]
                ],
            ),
            (
                "10.0.8.0/22",
                [
                    {
                        "address": "192.10.11.254",
                        "available": True,
                        "last_used": "30/01/20 " "17:00:00",
                    },
                ],
                [],
            ),
        ],
    )
    def test_remove_invalid_records(self, network, entries, expected):
        n_c = NetworkCollection(network, entries)
        n_c.remove_invalid_records()
        assert n_c.entries == expected

    @pytest.mark.parametrize(
        "entry, network, expected",
        [
            (
                Entry(
                    "10.0.11.254",
                    True,
                    "30/01/20 17:00:00",
                ),
                "10.0.8.0/22",
                True,
            ),
            (
                Entry(
                    "10.0.11.254",
                    True,
                    "30/01/20 17:00:00",
                ),
                "10.1.8.0/22",
                False,
            ),
        ],
    )
    def test_is_entry_in_network(self, entry, network, expected):
        n_c = NetworkCollection(network, [])

        assert n_c._is_entry_in_network(entry) == expected

    @pytest.mark.parametrize(
        "entries, expected",
        [
            (
                [
                    {
                        "address": "10.0.8.1",
                        "available": False,
                        "last_used": "30/01/20 " "16:00:00",
                    },
                    {
                        "address": "10.0.8.0",
                        "available": False,
                        "last_used": "30/01/20 " "16:00:00",
                    },
                ],
                [
                    Entry(**data)
                    for data in [
                        {
                            "address": "10.0.8.0",
                            "available": False,
                            "last_used": "30/01/20 " "16:00:00",
                        },
                        {
                            "address": "10.0.8.1",
                            "available": False,
                            "last_used": "30/01/20 " "16:00:00",
                        },
                    ]
                ],
            ),
            (
                [
                    {
                        "address": "10.0.8.1",
                        "available": False,
                        "last_used": "30/01/20 " "16:00:00",
                    },
                    {
                        "address": "10.0.8.0",
                        "available": False,
                        "last_used": "30/01/20 " "16:00:00",
                    },
                    {
                        "address": "10.0.8.2",
                        "available": False,
                        "last_used": "30/01/20 " "16:00:00",
                    },
                ],
                [
                    Entry(**data)
                    for data in [
                        {
                            "address": "10.0.8.0",
                            "available": False,
                            "last_used": "30/01/20 " "16:00:00",
                        },
                        {
                            "address": "10.0.8.1",
                            "available": False,
                            "last_used": "30/01/20 " "16:00:00",
                        },
                        {
                            "address": "10.0.8.2",
                            "available": False,
                            "last_used": "30/01/20 " "16:00:00",
                        },
                    ]
                ],
            ),
        ],
    )
    def test_sort_records(self, entries, expected):
        n_c = NetworkCollection("10.0.8.0/22", entries)
        n_c.sort_records()
        assert n_c.entries == expected
