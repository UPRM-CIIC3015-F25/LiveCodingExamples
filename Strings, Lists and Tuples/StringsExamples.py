# UPRM CIIC 3015 Fall 2025
# Lecture 5: Lists, Strings and Tuples
# Live Coding Examples
# Instructors: Karelys López and Bienvenido Vélez

# PART B: EXAMPLES WITH STRINGS

# Example 1
# Function count_vowels(w) that returns the count of vowels in a given word
def count_vowels(w):
    count = 0
    for c in w:
        if c in 'aeiouAEIOU':
            count += 1
    return count





# Example 2:
# Function find_first_consonant(w) to find position of first consonant in a
# word w.
# Returns -1 if w contains no consonants
def find_first_consonant(w):
    for idx in range(len(w)):
        if not w[idx] in "aeiouAEIOU":
            return idx
    return -1


# Example 3:
# Function replace_all_letters(word, letter, replacement) to return a new
# string that replace all occurrences of a letter by a replacement in a given
# word.
def replace_all_letters(word, letter, replacement):
    result = ''
    # for c in word:
    #     if c == letter:
    #         result += replacement
    #     else:
    #         result += c
    idx=0
    while idx < len(word):
        if word[idx] == letter:
            result += replacement
        else:
            result += word[idx]
        idx += 1
    return result


# Example 4:
# Function replace_all_words(sentence, word, replacement) to return a new
# string that replace all occurrences of a word by a replacement in a given
# sentence.
def replace_all_words(sentence, word, replacement):
    words = sentence.split()
    new_list = []
    for w in words:
        if w == word:
            new_list.append(replacement)
        else:
            new_list.append(w)
    return ' '.join(new_list)




