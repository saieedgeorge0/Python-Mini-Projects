import urllib

def read_text():
    email = open("email.txt")
    contents = email.read()
    print(contents)
    email.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
