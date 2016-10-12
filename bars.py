import sys
import math
import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    biggest_bar = max(data, key = lambda bar: bar['Cells']['SeatsCount'])    
    return (biggest_bar['Cells']['Name'], biggest_bar['Cells']['SeatsCount'])


def get_smallest_bar(data):
    smallest_bar = min(data, key = lambda bar: bar['Cells']['SeatsCount'])    
    return (smallest_bar['Cells']['Name'], smallest_bar['Cells']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    distance_to_current_bar = lambda bar: distance(
        longitude,
        latitude,
        bar['Cells']['geoData']['coordinates'][0],
        bar['Cells']['geoData']['coordinates'][1]
    )
    
    closest_bar = min(data, key = distance_to_current_bar)
    
    return closest_bar['Cells']['Name']


def distance(
        my_longitude, my_latitude,
        bar_longitude, bar_latitude):
    return math.sqrt(
        (my_longitude - bar_longitude) ** 2 +
        (my_latitude - bar_latitude) ** 2
    )

if __name__ == '__main__':
    if len (sys.argv) == 1:
        filepath = input('Enter file path > ')
        longitude = float(input('Enter longitude > '))
        latitude = float(input('Enter latitud > '))
    elif len (sys.argv) != 4:
        print (
            'Error: incorrect parameters are transferred.\n'
            'It is necessary to transfer a file name, longitude and latitude, '
            'or not to transfer anything.'
        )
        sys.exit (1)
    else:
        filepath = sys.argv[1]
        longitude = float(sys.argv[2])
        latitude = float(sys.argv[3])
    
    data = load_data(filepath)

    print('Smallest bar (seats count): %s (%d)' % get_smallest_bar(data))    
    print('Biggest bar (seats count): %s (%d):' % get_biggest_bar(data))
    print('Closest bar: ', get_closest_bar(data, longitude, latitude))  
