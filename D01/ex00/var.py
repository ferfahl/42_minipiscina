def my_var():
    a = 42
    print(a, "has a type", type(a))
    b = "42"
    print(b, "has a type", type(b))
    c = "quarante-deux"
    print(c, "has a type", type(c))
    d = 42.0
    print(d, "has a type", type(d))
    e = True
    print(e, "has a type", type(e))
    f = [42]
    print(f, "has a type", type(f))
    g = {42: 42}
    print(g, "has a type", type(g))
    h = (42,)
    print(h, "has a type", type(h))
    i =  set()
    print(i, "has a type", type(i))

if __name__ == '__main__':
    my_var()
    