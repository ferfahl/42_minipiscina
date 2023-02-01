import sys

def get_states():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    return states

def get_city():
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    return capital_cities

def capital_city():
    states = get_states()
    capitols = get_city()
    error = "Unknown state"

    if (len(sys.argv) == 2):
        state = states.get(sys.argv[1], error)
        capital = capitols.get(state, error)
        print(capital)

if __name__ == '__main__':
    capital_city()