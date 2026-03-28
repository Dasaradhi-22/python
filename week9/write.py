try:
    file = open("sample.txt","w+")
    file.write("Hello !!\nThis is files in python\ni am dasaradhi")
    print("Written content successfully")
except FileNotFoundError:
    print("File does not exist..")
