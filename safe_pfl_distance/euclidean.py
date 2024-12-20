import numpy as np


def euclidean_distance(u, v):
    distance = np.linalg.norm(u - v)
    distance = distance * 10**4
    return format(distance, ".2f")
