with open ("infilename.txt", "r") as file:
    for line in file:
        data = line.rstrip("\r\n\r\n")
        print (data)
