def read_file(filename=""):
    with open("my_file_0.txt") as f:
        file = f.read()
        print(file)