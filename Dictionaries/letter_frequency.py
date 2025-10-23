

def letter_frequency(text):
    d = {}
    for l in text:
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    return d

def most_frecuent_letter(text):
    d=letter_frequency(text)
    max = 0
    max_letter = ""
    for k in d:
        if d[k] > max:
            max = d[k]
            max_letter = k
    return max_letter

print(f"Most frecuent l"
      f"etter is \'{most_frecuent_letter("This could be a very long text")}\'")




