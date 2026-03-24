import sys

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

def check_argv():
    if len(sys.argv) != 2:
        return

    # strip() -> remove spaces before and after a string (like trim in C)
    # casefold() -> normalize to avoid case sensitive
    # split() -> crop de string in a list by a separator
    arg = [s.strip() for s in sys.argv[1].split(",")]
    # arg = [s.strip().casefold() for s in sys.argv[1].split(",")]

    # # None removes falsy values
    cleaned = list(filter(None, arg))

    if cleaned:
        return cleaned
    else:
        exit()

def find_capital(arg):
    # print(">>Finding in capitals...<<")
    for acronym in capital_cities:
        if capital_cities[acronym].casefold() == arg.casefold():
            for state in states:
                if states[state] == acronym:
                    print(f"{capital_cities[acronym]} is the capital of {state}")
                    return
    print(f"{arg} is neither a capital city nor a state")

def find_state(args):
    for arg in args:
        # print(f"Checking {arg}")
        """
        - La expresión busca la primera clave original de states cuya versión normalizada
        con casefold()coincida con arg (que previamente debe estar normalizado).
        - Si encuentra una coincidencia devuelve esa clave tal cual está
        en el diccionario; si no encuentra nada devuelve None.

        Generator expression: (EXPR for VAR in ITERABLE if COND)
        """
        match = next((key for key in states if key.casefold() == arg.casefold()), None)
        if match:
            acronym = states[match]
            capital = capital_cities.get(acronym, "Unknown capital")
            print(f"{capital} is the capital of {match}")
        else:
            find_capital(arg)

def all_in():
    args = check_argv()
    find_state(args)

if __name__ == "__main__":
    all_in()