def main():
    count = 0
    letter_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    for word in words:
        count += 1

    print(f"This book has {count} words")
    letter_count = count_characters(file_contents)
    #print(letter_count)
    #print(words)
    #print(file_contents)

def count_characters(file_string):
    import string
    new_string = file_string.lower()
    char_list = {}

    #creates a-z in dictionary keys
    for index, character in enumerate(string.ascii_lowercase):
        char_list[character] = 0
    
    #add ' ' and symbol keys
    char_list[' '] = 0
    char_list['Symbols'] = 0

    #checks for each letter, space and symbol
    for char in new_string:
        if char in string.ascii_lowercase:
            char_list[char] +=1
        elif char == " ":
            char_list[' '] += 1
        else:
            char_list['Symbols'] += 1
    
    return char_list

def sort_on(dict):
    return dict ["num"]

main()