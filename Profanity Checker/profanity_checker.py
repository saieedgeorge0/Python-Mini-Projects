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
    connection.close()
    if "true" in output:
        print("There are profane words in this text file.")
    if "false" in output:
        print("There are not profane words in this text file.")
    else:
        print("Document not scanned properly.")

read_text()
