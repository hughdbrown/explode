"""
The function 'explode' produces an animation of exploding bombs.
"""


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
    """
    # Check that the input parameters obey the required constraints.
    chamber_size = len(bombs)
    if chamber_size < 1 or chamber_size > 50:
        raise Exception("The length of 'bombs' is '%s'. The string must be 1 "
                        "to 50 characters long." % len(bombs))
    if force < 1 or force > 10:
        raise Exception("The value of force is '%s'. Only a force between 1 " \
                        "and 10 inclusive is permitted." % force)

    # Initialize our animation sequence to start with the input string.
    animation = [bombs]

    # Keep track of the locations of left-moving and right-moving shrapnel
    # in their own sets, initializing the location of each piece to the
    # location of the bomb from which they come.
    left, right = _initialize_shrapnel_locations(bombs)

    chamber = None
    EMPTY_CHAMBER = '.' * chamber_size
    # Until the chamber is empty, we contine updating our animation.
    while chamber != EMPTY_CHAMBER:
        # Update the locations of the shrapnel.
        left, right = _update_shrapnel(left, right, force)

        # Build the updated picture of the chamber as a list.
        chamber = []
        for location in xrange(chamber_size):
            if location in left:
                chamber.append('X' if location in right else '<')
            else:
                chamber.append('>' if location in right else '.')

        # Join the chamber into a string and add it to the animation.
        chamber = "".join(chamber)
        animation.append(chamber)

    return animation


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
    left = set([])
    right = set([])
    for index, char in enumerate(bombs):
        if char == 'B':
            left.add(index)
            right.add(index)
        elif char != '.':
            raise Exception("Improper string input 'bombs'.")
    return left, right


def _update_shrapnel(left, right, force):
    """
    Given two sets with the locations of left and right moving shrapnel,
    returns two sets with the updated locations after they have moved
    a distance given by the parameter 'force'.
    """
    # Update the locations of left-moving shrapnel.
    nextleft = set([])
    for shrapnel in left:
        nextleft.add(shrapnel - force)

    # Update the locations of right-moving shrapnel.
    nextright = set([])
    for shrapnel in right:
        nextright.add(shrapnel + force)

    return nextleft, nextright
