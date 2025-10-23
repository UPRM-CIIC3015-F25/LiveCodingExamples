

def letter_frequency(text):
    d = {}
    for l in text:
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    return d

def are_anagrams(word1, word2):
    d1=letter_frequency(word1)
    d1_sorted=dict(sorted(d1.items()))
    d2=letter_frequency(word2)
    d2_sorted=dict(sorted(d2.items()))
    return d1_sorted == d2_sorted

print(are_anagrams("foo", "oof"))
print(are_anagrams("foo", "off"))








