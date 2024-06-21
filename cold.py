def cold(temperatures: list[int]) -> int:
    '''
    This function takes a list of temperatures. It returns an int
    representing the number of times the temperature dropped below 0.

    Arguments:
        temperatures: a list of integers representing temperatures

    Returns:
        an int representing the number of times the temperature dropped below 0

    '''
    # TODO: Implement this function.
    dip_count = 0
    for temp in temperatures:
        if temp < 0:
            dip_count += 1
    return dip_count
