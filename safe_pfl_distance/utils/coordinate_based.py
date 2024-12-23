def coordinate_based_distance(u, v, model_weight_indices, sensitivity_parameter):
    # try:
    #     if not isinstance(model_weight_indices, dict):
    #         raise TypeError("model_weight_indices must be a dictionary.")
    #     if not isinstance(sensitivity_parameter, (int, float)):
    #         raise TypeError("sensitivity_parameter must be a number.")
    #     if sensitivity_parameter <= 0:
    #         raise ValueError("sensitivity_parameter must be positive.")

    #     if u not in model_weight_indices or v not in model_weight_indices:
    #         return 1.0

        indices_u = model_weight_indices[u]
        indices_v = model_weight_indices[v]

        intersection = len(indices_u & indices_v)
        # if intersection >= sensitivity_parameter:
        #     return 0.0
        similarity = intersection / sensitivity_parameter
        distance = 1 - similarity
        return distance

    # except TypeError as e:
    #     raise
    # except ValueError as e:
    #     raise
    # except Exception as e:
    #     raise Exception(f"An unexpected error occurred: {e}")
