def rgbint2rgbfloat(rgb):
    """
    Convert rgb integer values (0-255) to rgb float values (0.0-1.0) suitable
    with colour.Color usage.

    Args:
        rgb (tuple): Tuple of integer values from 0 to 255

    Returns:
        tuple: Tuple of float values from 0.0 to 1.0
    """
    return tuple([(i / 255) for i in rgb])

def rgbfloat2rgbint(rgb):
    """
    Convert rgb float values (0.0-1.0) to rgb integer values (0-255).

    Args:
        rgb (tuple): Tuple of float values from 0.0 to 1.0

    Returns:
        tuple: Tuple of integer values from 0 to 255
    """
    return tuple([int(255 * i) for i in rgb])
