def is_valid():
    coordinates = input()

    if '-' not in coordinates:
        print('ERROR')
        return

    coordinates = coordinates.split('-')

    start_longitude = coordinates[0][0]
    start_latitude = int(coordinates[0][1])

    end_longitude = coordinates[1][0]
    end_latitude = int(coordinates[1][1])

    step_map = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
    }

    if (start_longitude not in step_map.keys() or
        end_longitude not in step_map.keys()):
        print('ERROR')
        return

    if (start_latitude not in step_map.values() or
        end_latitude not in step_map.values()):
        print('ERROR')
        return

    start_longitude = step_map[start_longitude]
    end_longitude = step_map[end_longitude]

    longitude_difference = abs(end_longitude - start_longitude)
    latitude_difference = abs(end_latitude - start_latitude)

    if ((longitude_difference == 1 and latitude_difference == 2) or
        (longitude_difference == 2 and latitude_difference == 1)):
        print('YES')
    else:
        print('NO')


is_valid()
