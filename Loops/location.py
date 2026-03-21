import sys 
def main():

    coordinate_tuple = (42.376, -71.115)
    coordinate_list = (42.376, -71.115)
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")
main()

'''
def main():

    coordinates  = (42.376, -71.115)
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

main()
'''