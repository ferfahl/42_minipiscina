def numbers():
    t_src = open("numbers.txt", "r")
    str_src = t_src.read()
    list_int = str_src.split(",")
    for x in list_int:
        print(x)

if __name__ == '__main__':
    numbers()