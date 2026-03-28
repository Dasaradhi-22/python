try:
    file = open("sample.txt","r")
    temp=file.read()
    print(temp)
except FileNotFoundError:
    print("File does not exist..")
