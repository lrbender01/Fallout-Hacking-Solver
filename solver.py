#!/usr/bin/env python3

# Solve hacking minigame in Fallout 3, Fallout New Vegas, Fallout 4, and Fallout 76 given
# file with all possible choices as argument.
# Luke Bender (lrbender01@gmail.com) 1-15-21

import sys

words = []
matches = dict()

# Count number of matching letters in two words of same length
def get_matches(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count = count + 1
    return count

# Count total number of matching letters for word in entire list
def count_similar():
    for word in words:
        num_same = 0
        for compare in words:
            if word == compare:
                continue
            else:
                num_same = num_same + get_matches(word, compare)
        matches[word] = num_same

# Find most popular word in word list 
def find_most_popular():
    curr_word = ""
    most_matches = -1
    for word in words:
        if matches[word] > most_matches:
            most_matches = matches[word]
            curr_word = word
    return curr_word

# Remove all words that don't match the correct number of characters in current choice
def remove_impossible(choice, correct):
    keep_words = []
    for word in words:
        if word == choice:
            del matches[word]
        elif get_matches(choice, word) != correct:
            del matches[word]
        else:
            keep_words.append(word)
    return keep_words

 # Main function       
def main():
    # Global variables
    global words
    global matches
    global used_words
    global used_words_correct

    # Check correct number of arguments
    if len(sys.argv) != 2:
        print("Error: incorrect number of arguments", file = sys.stderr)
        print("Usage: solver.py <FILE>", file = sys.stderr)
        sys.exit(1)

    # Try to open the file
    try:
        file = open(sys.argv[1], 'r')
    except:
        print("Error: file cannot be opened or doesn't exist: \'" + sys.argv[1] + "\'", file = sys.stderr)
        sys.exit(1)

    # Read in all words
    for line in file:
        words.append(line.rstrip())

    # Check that word length is uniform
    word_length = len(words[0])
    for word in words:
        if len(word) != word_length:
            print("Error: all words must be same length", file = sys.stderr)
            sys.exit(1)

    try_num = 1
    # Loop until an answer has been found or problem is deemed impossible
    while(True):
        # Count similarities between words
        count_similar()

        #print(words) # DEBUGGING
        #print(matches) # DEBUGGING

        curr_choice = find_most_popular()
        num_correct = int(input("(" + str(len(words)) + ") " + str(try_num) + ": How many correct for \'" + curr_choice + "\'? "))

        if num_correct == word_length:
            print("=== " + curr_choice + " is the correct answer ===")
            print("=== Found in " + str(try_num) + " tries ===")
            sys.exit(0)
        elif num_correct > word_length:
            print("Error: cannot be more correct than word length")
            sys.exit(1)

        words = remove_impossible(curr_choice, num_correct)

        if len(words) == 0:
            print("Error: no possible words remaining")
            sys.exit(1)

        try_num = try_num + 1
        
if __name__ == '__main__':
    main()