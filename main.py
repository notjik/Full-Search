import sys
from geocoder import get_coords
from map import get_img, show_map


def main():
    toponym_to_find = ' '.join(sys.argv[1:])
    if toponym_to_find:
        lat, lon = get_coords(toponym_to_find)
        show_map(get_img((lat, lon)))


if __name__ == '__main__':
    main()