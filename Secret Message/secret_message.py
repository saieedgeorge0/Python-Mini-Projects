import os
def rename_files():
    file_list = os.listdir("message")
    saved_path = os.getcwd()
    os.chdir("message")

    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        os.rename(file_name, new_name)
    os.chdir(saved_path)
rename_files()
