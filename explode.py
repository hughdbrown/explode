#!/usr/bin/env python
"""
The function 'explode' produces an animation of exploding bombs.
"""

class ForceException(Exception):
    def __init__(self, force):
        msg = "The value of force is {0}. Only a force between 1 and 10 inclusive is permitted.".format(force)
        super(ForceException, self).__init__(msg)


class ChamberException(Exception):
    def __init__(self, chamber_size):
        msg = "The length of 'bombs' is {0}. The string must be 1 to 50 characters long.".format(chamber_size)
        super(ChamberException, self).__init__(msg)


def explode(bombs, force):
    """
    Given a representation of a chamber with bombs in it, creates an animation
    of the resulting shrapnel as the bombs explode. Each bomb will produce
    shrapnel moving left and right at constant speed, given by the 'force'
    parameter. Left-moving shrapnel will appear as '<', right-moving shrapnel
    as '>' and locations with shrapnel moving in both directions as 'X'.
    Shrapnel can move through each other.

    @param bombs: A string of length 1 to 50 in which every character is
                  either a . or a B, the latter representing a bomb.
    @param force: The speed at which shrapnel moves both to the left and
                  to the right.
    @return: A list of strings, each representing a unit of time, starting
             with the initial input string and ending when the chamber is
             empty.
    >>> explode('.....B.....', 1)
    ['.....B.....', '....<.>....', '...<...>...', '..<.....>..', '.<.......>.', '<.........>', '...........']
    >>> explode('B....', 1)
    ['B....', '.>...', '..>..', '...>.', '....>', '.....']
    >>> explode('B...B', 1)
    ['B...B', '.>.<.', '..X..', '.<.>.', '<...>', '.....']
    >>> explode('B...B.', 1)
    ['B...B.', '.>.<.>', '..X...', '.<.>..', '<...>.', '.....>', '......']
    >>> explode('B..B.', 1)
    ['B..B.', '.><.>', '.<>..', '<..>.', '....>', '.....']
    """
    # Check that the input parameters obey the required constraints.
    chamber_size = len(bombs)
    if not (1 <= chamber_size <= 50):
        raise ChamberException(chamber_size)
    elif not (1 <= force <= 10):
        raise ForceException(force)
    return list(_generate_animations(bombs, force))


def _generate_animations(bombs, force):
    # Keep track of the locations of left-moving and right-moving shrapnel
    # in their own sets, initializing the location of each piece to the
    # location of the bomb from which they come.
    yield bombs
    chamber_size = len(bombs)
    left, right = _initialize_shrapnel_locations(bombs)
    # Update the animation until no more shrapnel is flying.
    while left or right:
        left, right = _update_shrapnel(left, right, force, chamber_size)
        # Update the locations of the shrapnel.
        chamber = ['.'] * chamber_size
        for left_shrapnel in left:
            chamber[left_shrapnel] = '<'
        for right_shrapnel in right:
            chamber[right_shrapnel] = '>'
        for both_shrapnel in left & right:
            chamber[both_shrapnel] = 'X'
        # Join the chamber into a string and add it to the animation.
        yield "".join(chamber)


def _initialize_shrapnel_locations(bombs):
    """
    Returns two sets of locations, representing locations of left-moving and
    right-moving shrapnel, initialized to the positions of the bombs from
    which they come.

    @param bombs: A string comprised of '.' and 'B' characters, the 'B'
                  representing bombs, the locations of which in the string
                  are to be placed in left and right shrapnel sets.
    @return: Two identical sets, each with the locations in the input string
             of the bombs.
    """
    if set(bombs) - set('.B'):
        raise Exception("Improper string input 'bombs'.")
    left = set(index for index, char in enumerate(bombs) if char == 'B')
    return left, left.copy()


def _update_shrapnel(left, right, force, chamber_size):
    """
    Given two sets with the locations of left and right moving shrapnel,
    returns two sets with the updated locations after they have moved
    a distance given by the parameter 'force'.
    """
    def _updated_shrapnel(series):
        return set(shrapnel for shrapnel in series if 0 <= shrapnel < chamber_size)
    nextleft = _updated_shrapnel(shrapnel - force for shrapnel in left)
    nextright = _updated_shrapnel(shrapnel + force for shrapnel in right)
    return nextleft, nextright


if __name__ == '__main__':
    import doctest
    doctest.testmod()
