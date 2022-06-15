import json
from textwrap import indent


def addKeyWord():

    json_open = open("lessons.json", "r")
    chapters = json.load(json_open)
    keyword = input("please enter your question: ")
    keyword = keyword.split(" ")

    for i in keyword:
        for k in chapters:
            for r in chapters[k]:
                if i == r:
                    print("You can find the answer in ", k)
                    Q = True
                    KeyAdd()
                else:
                    Q = False
    if not Q:
        print("we coldn't find any Info")
        KeyAdd()


def KeyAdd():
    json_open = open("lessons.json", "r")
    chapters = json.load(json_open)

    user = input("""Please enter what you wan t to do:
    1)add new chapter
    2) add keyword to existing chapter
    3) Question Analysis
    """)

    if int(user) == 1:

        chapter = input("Type the name of the chapter: ")
        keys = []
        key = "0"
        while key != "x":
            key = input("enter key ('x' to finish) : ")
            if key != "x":
                keys.append(key)

        chapters[chapter] = keys
        json_new = open("lessons.json", "w")
        json.dump(chapters, json_new, indent=4)

    elif int(user) == 2:
        chapter = input("Type the chapter you want to add keywords: ")

        for i in chapters:
            print(i)

            if i == chapter:

                val = chapters[i]
                key = input(" Type new key you want to enter: ")
                val.append(key)
                chapters[i] = val
        json_open = open("lessons.json", "w")
        json.dump(chapters, json_open, indent=4)

    elif int(user) == 3:
        addKeyWord()
    else:
        print("incorrect input")
        KeyAdd()

