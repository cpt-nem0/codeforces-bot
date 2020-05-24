#! /usr/bin/python3.8

import sys
import os


# copy contents of templet to .cpp
def cpp_file(src):
    file = open(src, "w")
    with open('templet.txt', "r") as templet:
        file.write(templet.read())

    # os.system("geany {}".format(src))


def create_file(src):
    file = open(src, "w+")
    file.close()


try:
    # file name
    file_name = str(sys.argv[1])
    name, ext = file_name.split('.')
    file = os.getcwd() + '/' + file_name
    # calling cpp function for templet addition and file creation
    if ext == 'cpp':
        confirm = input('Do you want to copy templets?(y/n): ')
        if confirm.lower() == 'y':
            cpp_file(file)
        else:
            create_file(file)

    # just for now
    else:
        create_file(file)


except IndexError:
    print('File must be Enter')

except FileNotFoundError:
    print("'templet.txt' not Found.")
