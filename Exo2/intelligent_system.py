from tkinter import W
from prompt_toolkit import prompt
import json

def calculate_percentage_of_similitude(chapter_words, question_words, results):
    percentage = 0
    for question_word in question_words:
        for chapter_word in chapter_words:
            if (question_word == chapter_word):
                percentage = percentage + 1
    results.append(percentage)

def addKeyWord(user):
    json_open = open("lessons.json", "r")
    chapters = json.load(json_open)
    keyword = user.split(" ")
    json_open.close()
    if (len(keyword) != 2):
        print("Wrong Nomenclature given\n")
        return
    if (keyword[0] == "Variable" or keyword[0] == "List" or keyword[0] == "Condition" or keyword[0] == "Iterations" or keyword[0] == "Strings"):
        new_db = str(chapters[keyword[0]]) + ' ' + keyword[1] + ' ' + ']'
        chapters[keyword[0]] = new_db
        json_open = open("lessons.json", "w")
        json_open.seek(0)
        json.dump(chapters, json_open, indent=4)
        print("You've successfully added the Keyword:", keyword[1], " in ", keyword[0], "Chapter")
        json_open.close()
    else:
        print("Wrong Nomenclature given\n")

def find_chapter(question):
    json_open = open("lessons.json")
    results = []
    chapters = json.load(json_open)
    question_words = question.split(" ")
    chapter_number = 1
    for chapter_name in chapters:
        chapter_words = chapters[chapter_name][0].split(" ")
        calculate_percentage_of_similitude(chapter_words, question_words, results)
    for result in results:
        if (max(results) == result):
            break
        chapter_number = chapter_number + 1
    print("The Number of Keyword found for the different chapter is :", results)
    if (max(results) < 20):
        print("Your question doesn't link to a special chapter")
        json_open.close()
        return
    print("The system found that the chapter you are looking for is chapter number : ", chapter_number)
    json_open.close()

def main():
    while True:
        print ("""
        1.Ask a question to find the chapter
        """)
        option = input("Choose optionn 1\n")
        #if (option == "1"):
        #    keyword = input("send: Chapter_name Keyword_to_add\n")
        #    addKeyWord(keyword)
        if (option == "1"):
            value = input("What is your question ?\n")
            find_chapter(value)
        elif (option != "1"):
            print("No Valid Choice Try again")

main()