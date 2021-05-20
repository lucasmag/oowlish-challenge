import logging
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict
import requests
from cache_memoize import cache_memoize
from environ import Env

env = Env()
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

MAPS_GEOCODE_API = "https://maps.googleapis.com/maps/api/geocode/json"


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
def get_coordinates_from_address(address) -> Coordinates:
    log.info(f"Getting coordinates for {address}")
    params = {"address": address, "key": env.str("MAPS_GEOCODE_API_KEY")}
    response = requests.post(MAPS_GEOCODE_API, params=params)
    response_json = response.json()

    successful_response: bool = check_status_code(address, response_json)

    if successful_response:
        coordinates_resp = response_json["results"][0]["geometry"]["location"]
        coordinates = Coordinates(coordinates_resp["lat"], coordinates_resp["lng"])
        return coordinates

    return Coordinates(None, None)


def check_status_code(address: str, response: Dict) -> bool:
    if response["status"] == "OK":
        return True

    elif response["status"] == "ZERO_RESULTS":
        log.warning(f"No results for address {address}.")

    else:
        log.warning(f"There was a problem with request for address {address}.")

        if response.get("error_message", None):
            log.warning(response["error_message"])

    return False
