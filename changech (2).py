import os

def main():
    menu()

def menu():
    print("Welcome to the word converter")
    print("1. standered word converter")
    print("2. file convert")
    menutiem = input("enter 1-2: ")
    if menutiem == "1":
        word = input("enter a word \n")
        convert(word)
    elif menutiem == "2":
        fileconvert()
    else:
        print("not a valid entry")

def fileconvert():
    print(os.listdir())
    x = input("enter the file you want to convert: ")
    with open(x, "r") as f:
        word = f.read()
    convert(word)

def rep():
    reset = input("do you want to reset y/n?: ")
    if reset == "y":
        main()
    elif reset == "n":
        print("ok bye!")

def convert(word):
    replacements = {
        "a": "001",
        "b": "002",
        "c": "003",
        "d": "004",
        "e": "005",
        "f": "006",
        "g": "007",
        "h": "008",
        "i": "009",
        "j": "010",
        "k": "011",
        "l": "012",
        "m": "013",
        "n": "014",
        "o": "015",
        "p": "016",
        "q": "017",
        "r": "018",
        "s": "019",
        "t": "020",
        "u": "021",
        "v": "022",
        "w": "023",
        "x": "024",
        "y": "025",
        "z": "026",
        " ": "000"
    }

    newst = ""
    for character in word:
        if character in replacements:
            newst += replacements[character]
        else:
            newst += character

    print(newst)
    rep()

if __name__ == "__main__":
    main()
