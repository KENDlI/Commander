import os


def get_current_directory ():
    print("Current directory is " + os.getcwd())
    i = 0
    while i < 3:
        print ("#")
        i += 1
    menu()

def get_content_list():
    print ("Curent directory contents ")
    current_dir = os.getcwd()
    print (os.listdir(current_dir))
    i = 0
    while i < 3:
        print ("#")
        i += 1
    menu()

def change_dir():
    path=raw_input("Enter the path to the directory you want to go to:")
    os.chdir(path)
    get_current_directory()
    i = 0
    while i < 3:
        print ("#")
        i += 1
    menu()

def new_dir():
    name = raw_input("Enter the name of the new directory :")
    os.mkdir(name)
    i = 0
    while i < 3:
        print ("#")
        i += 1
    menu()

def remove_dir():
    path = raw_input("Enter the path to the directory you want to delete:")
    os.rmdir(path)
    i = 0
    while i < 3:
        print ("#")
        i += 1
    menu()

def new_file():
    name=raw_input("Enter file name:")
    open(name,"w+")
    i = 0
    while i < 3:
        print ("#")
        i += 1
    menu()

def remove_file():
    path = raw_input("Enter the path to the file you want to delete:")
    os.remove(path)
    i = 0
    while i < 3:
        print ("#")
        i += 1
    menu()

def menu():
    print "Choose what you want to do:"
    print ("1.Find out the current directory")
    print ("2.Get content of the current directory")
    print ("3.Change the directory")
    print ("4.Make a new directory")
    print ("5.Remove directory")
    print ("6.Make a new file in the current directory")
    print ("7.Delete a file")
    print ("8.Exit")
    n=input()
    if n == 1:
        get_current_directory()
    if n == 2:
        get_content_list()
    if n == 3:
        change_dir()
    if n == 4:
        new_dir()
    if n == 5:
        remove_dir()
    if n == 6:
        new_file()
    if n == 7:
        remove_file()
    if n == 8:
            return
    else:
        print ("There is no such item")


i=0
while i<5:
    print ("#")
    i+=1

menu()
