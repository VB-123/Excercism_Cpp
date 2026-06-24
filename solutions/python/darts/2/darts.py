from math import sqrt
def score(x, y):
    """Returns the earned points in a single toss of a Darts game.
    
    :param x: int - the x coordinate of the dart.
    :param y: int - the y coordinate of the dart.
    :return: int - The points scored.
    Rules: If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle (radius 10) of the target, player earns 1 point.
    If the dart lands in the middle circle (radius 5) of the target, player earns 5 points.
    If the dart lands in the inner circle (radius 1) of the target, player earns 10 points."""
    radius = sqrt(x**2 + y**2)
    if radius > 10:
        return 0
    if 5 < radius <= 10:
        return 1
    if 1 < radius <= 5:
        return 5
    if radius <= 1:
        return 10
