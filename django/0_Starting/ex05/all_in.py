import sys

def check_argv():
    if len(sys.argv) != 2:
        return

    # strip() -> remove spaces before and after a string (like trim in C)
    # casefold() -> normalize to avoid case sensitive
    # split() -> crop de string in a list by a separator
    arg = [s.strip().casefold() for s in sys.argv[1].split(",")]

    # # None removes falsy values
    cleaned = list(filter(None, arg))

    # print(arg)
    # print(cleaned)

    if cleaned:
        return cleaned
    else:
        exit()

def all_in():
    arg = check_argv()

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

if __name__ == "__main__":
    all_in()