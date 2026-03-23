import sys

def state():
    if len(sys.argv) != 2:
        # print("Error: El programa necesita exactamente un argumento.")
        return

    arg = sys.argv[1]

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    for acronym, capital in capital_cities.items():
        if capital == arg:
            for state, acro in states.items():
                if acro == acronym:
                    print(state)
                    return

    print("Unknown capital city")

if __name__ == "__main__":
    state()