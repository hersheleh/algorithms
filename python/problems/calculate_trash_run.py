"""Calculate Max trash takeout time."""

def calculate_trash(trash_type, D, T):
    """Collect Trash."""
    trip_total = 0
    track_all_houses = False
    for i in reversed(range(len(D))):                 # for each house
        trash = T[i]
        trash_count = 0
        for bag in trash:      # for each bag
            if bag == trash_type:
                trash_count += 1
                track_all_houses = True
        if track_all_houses:
            trip_total += D[i] * 2 + trash_count
    return trip_total


def solution(D, T):
    """Calculate Trash runs for glass metal & plasitc."""
    glass_trip = calculate_trash('G', D, T)  # calculate Glass
    metal_trip = calculate_trash('M', D, T)  # calculate Metal
    plastic_trip = calculate_trash('P', D, T)  # calculate Plastic

    return max([glass_trip, metal_trip, plastic_trip])


if __name__ == '__main__':
    D = [2, 5]
    T = ['PGP', 'M']

    print(solution(D,T))
