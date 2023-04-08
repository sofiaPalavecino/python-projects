def get_word_count(file_contents):
    return str(len(file_contents.split()))


def get_character_count(file_contents):
    file_contents_lowercase = file_contents.lower()
    appearances_of_characters = {my_list: 0 for my_list in set(file_contents_lowercase)}
    for character in appearances_of_characters:
        appearances_of_characters[character] = file_contents_lowercase.count(character)
    return appearances_of_characters


def print_characters_report(appearances_of_characters):
    appearances_of_characters = sorted(appearances_of_characters.items(), key=lambda x: x[1], reverse=True)
    for character_info in appearances_of_characters:
        if character_info[0].isalpha():
            print("The '" + character_info[0] + "' was found " + str(character_info[1]) +" times")


with open("./books/frankenstein.txt", "r") as file:
    fileContents = file.read()
    print("Word count: " + get_word_count(fileContents))
    print("Number of appearances of each character in the file: ")
    characters_appearances = get_character_count(fileContents)
    print_characters_report(characters_appearances)
