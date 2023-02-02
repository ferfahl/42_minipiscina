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
    return(dict_state_capital)

def dict_capital(dict_state_capital):
    dict_capital_state = {v: k for k, v in dict_state_capital.items()}
    return(dict_capital_state)

def all_in():
    error = "is neither a capital city nor a state"
    message = "is the capital of"
    states = dict_state()
    capitols = dict_capital(states)
    if (len(sys.argv) == 2):
        str_full = str(sys.argv[1])
        l_str = str_full.split(",")
        for x in l_str:
            title_str = x.strip()
            if len(title_str):
                capital = capitols.get(title_str.title())
                state = states.get(title_str.title())
                if capital:
                    state = states.get(capital)
                    print(capital, message, state)
                elif state:
                    capital = capitols.get(state)
                    print(capital, message, state)
                else:
                    print(title_str, error)

if __name__ == '__main__':
    all_in()