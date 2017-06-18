def anti_vowel(text):
    r = ""
    for letter in text:
        if letter in "aeiouAEIOU":
            continue
        else:
            r = r + letter
    return r
