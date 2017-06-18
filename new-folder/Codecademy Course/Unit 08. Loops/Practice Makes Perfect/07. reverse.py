def reverse(text):
    reversed_word = ""
    for letter in range(len(text)-1,-1,-1): # Starting from the last letter
        reversed_word = reversed_word + text[letter]
    return reversed_word
