import numpy as np
from scipy.spatial.distance import jensenshannon


def jensen_shannon_distance_func(u, v):
    u = np.abs(u)
    v = np.abs(v)
    u /= np.sum(u)
    v /= np.sum(v)
    epsilon = 1e-12
    u = np.clip(u, epsilon, None)
    v = np.clip(v, epsilon, None)
    distance = jensenshannon(u, v)
    distance = distance * 10
    return round(distance, 2)
