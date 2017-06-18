def anti_vowel(text):
    for letter in text:
        if letter in "aeiouAEIOU":
            text = text.replace(letter,"")
    return text
