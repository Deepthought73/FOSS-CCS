#! /usr/bin/python3

from sys import argv
import os

DATA = ""

def print_help():
    help = """
help/?/h    to print help
            help
replace     replace first string to the second. Providing first is in the file.
            replace "string from the file" "replace to this string"
save        save the file with the given path.
            save path/to/save
quit        to quit
    """
    print(help)



def load_svg(filePath):
    global DATA
    print(f"Reading file {filePath}")
    with open(filePath, "r") as f:
        DATA = f.read()
    print(f"Loaded file {filePath}")


def interpret_cmd(cmd):
    global DATA
    cmd = cmd.split(" ")
    if cmd[0] in ["help" , "?", "h"]:
        print_help()

    elif cmd[0] == "data":
        print(DATA)

    elif cmd[0] == "replace":
        try:
            t = DATA.split("\n")
            t = [line.replace(f">{cmd[1]}<", f">{cmd[2]}<") for line in t]
            DATA = "\n".join(t)


        except IndexError:
            print("Failed to replace, Proper argument not provided")

    elif cmd[0] == "save":
        try:
            filePath = cmd[1]
        except IndexError:
            print("Save path not provided")

        if os.path.isfile(filePath):
            print()
            choice = input(f"{filePath}: Already exists. Want to continue? [y/n] :").strip().lower()
            if choice == "y":
                pass 
            elif choice == "n":
                return
            else:
                print(f"Invaild choice: {choice}")
                return

        with open(filePath, "w") as f:
            f.write(DATA)

    elif cmd[0] == "quit":
        print("Quiting..")
        del DATA
        exit()

    else:
        print(f"Invaild command: {cmd[0]}\n Use help/h/? to get help")

def main():
    filePath = argv[1]
    if os.path.isfile(filePath) == False:
        print(f"Invaild file path: {filePath}")
        exit(-1)
    print(f"File Path: {filePath}")
    if (filePath[-4::] == ".svg") == False:
        print(f"Not a svg file: {filePath}")
        exit(-1)

    load_svg(filePath)
    print("use ? to get help")

    while True:
        cmd = input(">>> ")
        interpret_cmd(cmd)

if __name__ == "__main__":
    main()


