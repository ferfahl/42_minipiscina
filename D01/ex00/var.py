def my_var():
    a = 42
    print(a, "has a type", type(a))
    a = "42"
    print(a, "has a type", type(a))
    a = "quarante-deux"
    print(a, "has a type", type(a))
    a = 42.0
    print(a, "has a type", type(a))
    a = True
    print(a, "has a type", type(a))
    a = [42]
    print(a, "has a type", type(a))
    a = {42: 42}
    print(a, "has a type", type(a))
    a = (42,)
    print(a, "has a type", type(a))
    a =  set()
    print(a, "has a type", type(a))

if __name__ == '__main__':
    my_var()