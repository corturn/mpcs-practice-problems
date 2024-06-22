def firstlast(stream: str, character: str) -> int:
    '''
    Given a string and a non-whitespace character the program finds the first 
    token that starts and ends with the character, if one exists, along with the
    index 0 ≤ i < |S| of the first letter of that token.

    If the string contains one or more tokens that start and end with the 
    character, then the output should contain the first such token and the index 
    0 ≤ i < |S| of the token's first character.

    If the string does not contain a token that starts and ends with the 
    character, then the output should contain NONE and -1.

    Parameters:
        stream (str): A string for which to find the first token that starts and
            ends with the character.
        character (str): A non-whitespace character.

    Returns:
        the index 0 ≤ i < |S| of the token's first character or -1, if no
        suitable token exists.
    '''
    # TODO: Implement this function
    tokens = stream.split()
    for token in tokens: 
        if token[0] == character and token[-1] == character:
            return stream.index(token)
    return -1
