#! /usr/bin/python3.8

import subprocess
import sys
import os


def cpp_file(src):
    confirm = input(
        'Do you want to copy the contents of "templet.txt"?(Y/N): ').lower()
    if confirm == 'y':
        with open(src, 'w') as file, open("{}/templet.txt".format(os.path.dirname(__file__)), 'r') as templet:
            file.write(templet.read())
    else:
        files(src)


def files(src):
    file = open(src, 'w+')
    file.close()


try:
    if len(sys.argv) == 1:
        print('Enter proper file name with extension.')
    else:
        file_name = sys.argv[1]
        name, ext = file_name.split('.')
        file = os.getcwd() + '/' + file_name
        if ext == 'cpp':
            cpp_file(file)
        else:
            files(file)
        subprocess.run("code .", shell=True)

except FileNotFoundError:
    print("'templet.txt' is not found.")
