# function named in_example, receives a letter and word.
# Return true if the letter
# exists, else return false

def in_example(letter, word):
    for char in word:
        if char == letter:
            return True
    return False




