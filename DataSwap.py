def swapFileData():
    file1 = input("Enter the file name:- ")
    file2 = input("Enter the file name:- ")

    with open(file1, "r") as a:
        fileA = a.read()

    with open(file2, "r") as b:
        fileB = b.read()

    with open(file1, "w") as a:
        a.write(fileB)

    with open(file2, "w") as b:
        b.write(fileA)

swapFileData()