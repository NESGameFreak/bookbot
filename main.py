def main():
    word_count = 0
    letter_count_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    for word in words:
        word_count += 1

    #print(f"This book has {count} words")
    letter_count_dict = count_characters(file_contents)

    #sort and print the dictionary
    list_of_dict = dict_into_list_of_dict(letter_count_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    
    #Print Final Result
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for item in list_of_dict:
        print(f"The '{item['letter']}' character was found {item['num']} times")
    print("--- End report ---")

def count_characters(file_string):
    import string
    new_string = file_string.lower()
    char_list = {}

    #creates a-z in dictionary keys
    for index, character in enumerate(string.ascii_lowercase):
        char_list[character] = 0
    
    #add ' ' and symbol keys
    #char_list[' '] = 0
    #char_list['Symbols'] = 0

    #checks for each letter, space and symbol
    for char in new_string:
        if char in string.ascii_lowercase:
            char_list[char] +=1
        #elif char == " ":
        #    char_list[' '] += 1
        #else:
        #    char_list['Symbols'] += 1
    
    return char_list

def sort_on(dict):
    return dict["num"]

def dict_into_list_of_dict(dict):
    return [{"letter": k, "num": v} for k, v in dict.items()]
main()