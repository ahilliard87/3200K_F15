import random


def random_point():
    """ This function generates a random geographic coordinate.

    >>> lat, lng = random_point()
    >>> -90 <= lat <= 90
    True
    >>> -180 <= lng <= 180
    True
    >>> random.seed(100)
    

        
    """
    

    lat = random.uniform(-90, 90)
    lng = random.uniform(-180, 180)
    return lat, lng
    
    




if __name__ == '__main__':
    import doctest
    doctest.testmod()
