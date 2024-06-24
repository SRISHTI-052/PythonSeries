#This program prints the content of a directory using the OS module 

import os

directory_path='/'

contents=os.listdir(directory_path)

for item in contents:
    print(item)