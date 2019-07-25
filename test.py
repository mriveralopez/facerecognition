import os


def devolverfiles(directory):
    for file in os.listdir(directory):
        # print(os.path.join(directory, file))
        name = file.split(".")
        print(name[0])
        # if os.path.isdir(os.path.join(directory, file)):
        #     devolverfiles(os.path.join(directory, file))


devolverfiles("./people/")