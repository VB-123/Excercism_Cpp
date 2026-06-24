"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    moved_wagon1,moved_wagon2,locomotive,*rest = each_wagons_id
    fixed_list = [locomotive,*missing_wagons,*rest,moved_wagon1,moved_wagon2]
    return fixed_list


def add_missing_stops(route,**kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_list = list(kwargs.values())
    return {**route,"stops": stops_list}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route,**more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    new_wagon_rows = []
    new_rows1,new_rows2,new_rows3 =[],[],[]
    for row in wagons_rows:
        wagon1,wagon2,wagon3 = row
        new_rows1.append(wagon1)
        new_rows2.append(wagon2)
        new_rows3.append(wagon3)
    new_wagon_rows = [new_rows1,new_rows2,new_rows3]
    return new_wagon_rows
