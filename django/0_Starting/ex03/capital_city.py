import sys

def capital_city():
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

    # for state in states:
    #     if state == arg:
    #         exist = True
    #         for acronym in capital_cities:
    #             if acronym == states[state]:
    #                 print(capital_cities[acronym])
    #         break
    #     else:
    #         exist = False

    # if exist == False:
    #     print("Unknown state")

    if arg in states:
        acronym = states[arg]
        print(capital_cities[acronym])
    else:
        print("Unknown state")


if __name__ == "__main__":
    capital_city()