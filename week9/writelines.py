try:
    file = open("sample.txt","+a")
    file.writelines(["\nThis is Python lab","\nMake sure to listen Carefully"])
except FileNotFoundError:
    print("File does not exist..")

