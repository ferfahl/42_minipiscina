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

def dict_state():
    dict_state_capital = get_states()
    for key, value in dict_state_capital.items():
        dict_state_capital[key] = get_city().get(value)
    print(dict_state_capital)
    return(dict_state_capital)

def dict_capital(dict_state_capital):
    dict_capital_state = {v: k for k, v in dict_state_capital.items()}
    print(dict_capital_state)

def all_in():
    error = "is neither a capital city nor a state"
    message = "is the capital of"
    states = dict_state()
    capitols = dict_capital(states)

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