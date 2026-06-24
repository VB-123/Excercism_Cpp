from math import sqrt
def score(x, y):
    radius = sqrt(x**2 + y**2)
    if radius > 10:
        return 0
    if 5 < radius <= 10:
        return 1
    if 1 < radius <= 5:
        return 5
    if radius <= 1:
        return 10
