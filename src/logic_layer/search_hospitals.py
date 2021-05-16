from typing import List
from math import asin, cos, radians, sin, sqrt
from src.data_layer.bot_io import RequestInput
from src.data_layer.item import search_items_on_quantity
from src.models.hospital import HospitalModel


def get_dist_between_two_latitude_longitude(*args) -> float:
    """
    Calculate distance between two geo locations
    :param args: first_latitude, first_longitude, second_latitude, second_longitude
    :return: Distance between 2 locations by using Haversine formula https://en.wikipedia.org/wiki/Haversine_formula
    """
    first_latitude, first_longitude, second_latitude,  second_longitude = map(radians, args)

    latitude_distance = abs(second_latitude - first_latitude)
    longitude_distance = abs(second_longitude - first_longitude)
    # Calculate Haversine
    harvesine = sin(latitude_distance/2)**2 + cos(first_latitude) * cos(second_latitude) * sin(longitude_distance/2)**2
    corner_opposite = asin(sqrt(harvesine)) * 2
    earth_radius = 6378
    return corner_opposite * earth_radius


def sort_by_location(source_hospital, target_hospitals_list):
    """
    :param source_hospital: Source hospital to search from
    :param target_hospitals_list: List of target hospitals
    :return: List of sorted hospitals
    """
    # Sort target_hospitals_list by nearest location
    target_hospitals_list = [{"id": hospital.id,
                              "name": hospital.name,
                              "latitude": hospital.latitude,
                              "longitude": hospital.longitude}
                             for hospital in target_hospitals_list]

    for target_hospital in target_hospitals_list:
        distance = get_dist_between_two_latitude_longitude(source_hospital.latitude,
                                                           source_hospital.longitude,
                                                           target_hospital["latitude"],
                                                           target_hospital["longitude"])
        target_hospital.update({"distance": distance})

    # Sort by distance
    target_hospitals_list = sorted(target_hospitals_list, key=lambda values: values["distance"], reverse=False)

    return target_hospitals_list


def search_hospitals(request_input: RequestInput, db_session) -> List[dict]:
    """
    Search hospitals based on requested items. Sort them by nearest location
    :param request_input: RequestInput
    :param db_session: DB session
    :return: List of Hospital dictionaries
    """
    # Search hospitals which has requested resources
    hospitals_list = search_items_on_quantity(request_input, db_session)
    if len(hospitals_list) < 1:
        return []

    # Get source hospital
    source_hospital = db_session.query(HospitalModel).filter(HospitalModel.id == request_input.hospital_id).one()

    # Sort hospitals by nearest location
    return sort_by_location(source_hospital, hospitals_list)

