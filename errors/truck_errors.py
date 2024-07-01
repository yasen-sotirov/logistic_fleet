class TruckIdError(Exception):
    """
    Throws an exception if there are no more available tucks from this type.
    """
    pass


class TruckTypeError(Exception):
    """
    Throws an exception if there are no such type tucks available.
    """
    pass