from local_lib.path import Path

def my_program():
    folder = Path("myfolder")
    folder.mkdir_p()
    file = folder / "myfile.txt"
    file.touch()
    file.write_text("Hello there!")
    print(file.read_bytes().decode("utf-8"))


if __name__ == '__main__':
    my_program()