def count_substrs(str_list: list[str], target: str) -> int:
    '''
    This function takes a list of strings and a target string and counts
    the number of strings in the list that contain the target as a substring.
    
    Arguments:
        str_list: a list of strings
        target: the target string (len(target) > 0).

    Returns: 
        The number of strings in the list that contain the target substring.
    '''
    assert len(target) > 0
    count = 0
    for s in str_list:
        if target in s:
            count += 1
    return count
