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

def capital_dict():
    capitols = get_city()
    inv_c = {v: k for k, v in capitols.items()}
    return inv_c

def states_dict():
    states = get_states()
    inv_s = {v: k for k, v in states.items()}
    return inv_s

def state():
    states = states_dict()
    capitols = capital_dict()
    error = "Unknown capital city"
    
    if (len(sys.argv) == 2):
        capital = capitols.get(sys.argv[1], error)
        state = states.get(capital, error)
        print(state)


if __name__ == '__main__':
    state()