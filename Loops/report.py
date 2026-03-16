def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    #add into a dictionay
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    """spacecraft["distance"] = 0.01"""
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU 
    Orbit: {spacecraft.get("orbit", "Unknown")}
    """
main()

'''
def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU 
    """
main()
'''