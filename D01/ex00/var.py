def my_var():
    t_list = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]
    for x in t_list:
        print(x, "has a type", type(x))

if __name__ == '__main__':
    my_var()