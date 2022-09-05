import json
from pprint import pprint

import requests

from data_structures.datacenter import Datacenter

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.

    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    try:
        response = requests.get(url)
    except Exception as ex:
        if not max_retries:
            raise ex
        return get_data(url, max_retries-1, delay_between_retries)

    return response.json()


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    pprint(data)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    for datacenter in datacenters:
        print(datacenter)


if __name__ == '__main__':
    main()

