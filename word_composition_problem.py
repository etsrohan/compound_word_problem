### Rohan Srivastava
### 23/07/2021
### Word Composition Problem

import time

def load_input() -> list:
    """A function to help load the input from the .txt file into a list"""
    while True:
        # Getting user input to select which data set to use
        select = input("Whould you like to use Input Set 1 or 2 or your own file?\n(Enter '1' or '2' or 'o' for own)\n-- ")
        if select == str(1):
            try:
                with open("Input_01.txt") as fileobj:
                    data = fileobj.readlines()
                break
            except FileNotFoundError:
                print("Please make sure that Input_01.txt is in the directory.")
        elif select == str(2):
            try:
                with open("Input_02.txt") as fileobj:
                    data = fileobj.readlines()
                break
            except FileNotFoundError:
                print("Please make sure that Input_02.txt is in the directory.")
        elif select.lower() == "o":
            name = input("Enter your file name as a .txt: ")
            try:
                with open(name) as fileobj:
                    data = fileobj.readlines()
                break
            except FileNotFoundError:
                print("Please make sure the file (.txt) exists in the directory\n")
        else:
            print("Please select between 1 or 2")

    return [x.strip() for x in data]

def split_n_check(s: str, words: set, memory: dict) -> bool:
    """This function splits the word into left and right and checks of left is a word and right is a compound word"""
    # Optimization to see if we already visited the given string s before
    if s in memory:
        return memory[s]
    else:
        memory[s] = False
    
    for i in range(1, len(s)):
        # Splitting the word into left and right parts to check if available in set-words
        left = s[:i]
        right = s[i:]

        # If statements checking if left is in words and right is either in words or is compound word
        if left in words and right in words:
            #return True (previous code)

            # Optimization to set given string s and value True as key value pair
            memory[s] = True
            break
        if left in words and split_n_check(right, words, memory):
            #return True (previous code)

            # Optimization
            memory[s] = True
            break

    # Return False if word splits are not in words
    # return False
    # Optimization to return word value in memory dictionary
    return memory[s]

def log_answers(first: list, second: list, secs: float) -> None:
    message = "Longest Compound Word(s): "
    for s in first:
        message += s
        if s != first[-1]:
            message += ", "
        else:
            message += "\n"
    message += "Second Longest Compound Word(s): "
    for s in second:
        message += s
        if s != second[-1]:
            message += ", "

    message += "\n\nTime taken for program to execute: " + str(secs)
    
    print(message)
    

    with open("Output.txt", 'w') as fileobj:
        fileobj.write(message)


def main():
    # Using a set for words from input because it uses hash function so lookup is O(1)
    words = set(load_input())
    answer = []

    # Setting start time for program
    start = time.perf_counter()

    # Initializing memory to optimize the split_n_check function
    memory = {}
    for s in words:
        if split_n_check(s, words, memory):
            answer.append(s)
    
    # Sorting the answers (compound words) from longest to shortest
    answer.sort(reverse = True, key = len)
    print(memory)

    # This is where I found out that the 2nd input set had
    # 2 different answers with same length hence why it kept giving me
    # 2 answers alternatively every time I ran the code multiple times
    """print(answer[:4])
    for i in range(4):
        print(len(answer[i]))"""

    # I decided to print out all the words tied for first and second
    first = []
    second = []

    # Putting in the first and longest compound word in first list
    first.append(answer[0])
    count = 1
    # Checking rest of list for similar length compound word to first place
    for s in answer[1:]:
        if len(s) == len(first[0]):
            first.append(s)
            count += 1
        if len(s) < len(first[0]):
            break
    # Putting second longest compound word into second list
    second.append(answer[count])
    count += 1
    # Checking rest of list for similar length compound word to second place
    for s in answer[count:]:
        if len(s) == len(second[0]):
            second.append(s)
        if len(s) < len(second[0]):
            break
    
    # Setting end time of program
    end = time.perf_counter()

    #print(first)
    #print(second)

    # Printing Output to console and an output.txt file
    log_answers(first, second, end - start)



    

if __name__ == "__main__":
    main()