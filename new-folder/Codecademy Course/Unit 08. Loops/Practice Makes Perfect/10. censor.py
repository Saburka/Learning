def censor(text, word):
    text = text.split()
    new_text = []
    for item in text:
        if item == word:
            new_text.append(len(item) * "*")
        else:
            new_text.append(item)
    return " ".join(new_text)
