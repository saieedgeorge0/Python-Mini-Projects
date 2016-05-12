def read_text():
    email = open("email.txt")
    contents = email.read()
    print(contents)
    email.close()
read_text()
