def sort_on(dict):
    return dict["num"]

def character_count(text):
    lower_case = text.lower()
    dic={}
    notalpha=0
    for letters in lower_case:
        if letters.isalpha() == True:
            if letters in dic:
                dic[letters] += 1
            else:
                dic[letters] = 1
        else: notalpha += 1

    return dic

def wordcount(input):
    count = 0
    word_list = input.split()
    return len(word_list) 

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    numwords = wordcount(file_contents)
    characters = character_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{numwords} words found in the document")
    char_list = []
    for char, num in characters.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    for letter in char_list:
        print(f"The '{letter['char']}' character was found {letter['num']} times")
    print ("--- End report ---")

if __name__ == "__main__":
    main()