def reader(path):
    with open(file=path,mode='r') as a:
        contents = a.readlines()
        return contents
