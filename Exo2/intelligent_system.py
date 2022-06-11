from prompt_toolkit import prompt
import json

def calculate_percentage_of_similitude(chapter_words, question_words, results):
    percentage = 0
    for question_word in question_words:
        for chapter_word in chapter_words:
            if (question_word == chapter_word):
                percentage = percentage + 1
    results.append(percentage)


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
    if (max(results) < 20):
        print("Your question doesn't link to a special chapter")
        return
    print("The system found that the chapter you are looking for is chapter number : ", chapter_number)

def main():
    while True:
        value = input("What is your question ?\n")
        find_chapter(value)

main()