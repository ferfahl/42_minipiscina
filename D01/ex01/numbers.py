def numbers():
    t_src = open("numbers.txt", "r")
    str_src = t_src.read().split(",")
    for number in str_src:
        print(number.strip())

if __name__ == '__main__':
    numbers()