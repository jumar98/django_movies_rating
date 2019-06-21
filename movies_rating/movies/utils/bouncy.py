def is_bouncy(number: int) -> bool:
    """
    We define a function with which,
    we'll know which is a bouncy number

    :param number: int
    :return: bool
    """
    arr = list(map(int, str(number)))
    increase, decrease = False, False
    i = 0
    while i < len(arr) - 1:
        if arr[i] < arr[i+1]:
            increase = True
        elif arr[i] > arr[i+1]:
            decrease = True
        if increase & decrease:
            return True
        i = i + 1
    return False


def minimun_number(total_number: int = 21780, proportion_start: float = 0.90, proportion_end: float = 0.99,) -> int:
    """
    Here, we iterate to know when the numbers bouncy
    bring to proportion of 99%

    :param proportion_end_: float
    :param proportion_start: float
    :param total_number: int
    :return: int
    """
    if proportion_start > proportion_end or proportion_end == 100.0:
        return -1

    bouncy_number = total_number * proportion_start
    while bouncy_number <= proportion_end * total_number:
        total_number = total_number + 1
        if is_bouncy(total_number):
            bouncy_number = bouncy_number + 1
    return total_number - 1
