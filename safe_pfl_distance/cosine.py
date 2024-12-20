from scipy.spatial.distance import cosine


def cosine_distance(u, v):
    distance = cosine(u, v)
    return format(distance, ".2f")
