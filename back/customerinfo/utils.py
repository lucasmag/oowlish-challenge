from dataclasses import dataclass
from enum import Enum
from typing import Optional

import requests
from cache_memoize import cache_memoize

GEOCODE_API = "https://maps.googleapis.com/maps/api/geocode/json"
API_KEY = "AIzaSyDxyhQVuEYmwryRhCpcaZfXfYsxNSXuvbg"


@dataclass
class Coordinates:
    latitude: Optional[float]
    longitude: Optional[float]


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class Gender(ChoiceEnum):
    MALE = "male"
    FEMALE = "female"


@cache_memoize(10 * 60)
def get_coordinates_from_address(address):
    print(address)
    params = {"address": address, "key": API_KEY}
    response = requests.post(GEOCODE_API, params=params)
    response_json = response.json()

    if response_json["status"] == "REQUEST_DENIED":
        print("vish")

    if response_json["status"] == "OK":
        coordinates_resp = response_json["results"][0]["geometry"]["location"]
        coordinates = Coordinates(coordinates_resp["lat"], coordinates_resp["lng"])
        return coordinates

    return Coordinates(None, None)
