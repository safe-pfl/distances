from scipy.stats import wasserstein_distance


def wasserstein_distance_func(u, v):
    distance = wasserstein_distance(u, v)
    distance = distance * 10
    return round(distance, 2)
