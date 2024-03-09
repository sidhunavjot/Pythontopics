"""Write a python script to print two given words in dictionary order"""

def print_in_dictionary_order(word1, word2):
    if word1 < word2:
        print(word1, word2)
    else:
        print(word2, word1)

if __name__ == '__main__':
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    print("Words in dictionary order:")
    print_in_dictionary_order(word1, word2)



