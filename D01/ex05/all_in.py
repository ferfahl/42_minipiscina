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

def all_in():
    error = "is neither a capital city nor a state"
    message = "is the capital of"
    states1 = get_states()
    capitols1 = get_city()
    states2 = states_dict()
    capitols2 = capital_dict()

    if (len(sys.argv) == 2):
        str_full = str(sys.argv[1])
        l_str = str_full.split(",")
        for x in l_str:
            if (state.lower() = l_str.lower()):
                state = states1.get(sys.argv[1], error)
                capital = capitols1.get(state, error)
            elif (capitol.lower() = l_str.lower()):
                capital = capitols2.get(sys.argv[1], error)
                state = states2.get(capital, error)



if __name__ == '__main__':
    all_in()