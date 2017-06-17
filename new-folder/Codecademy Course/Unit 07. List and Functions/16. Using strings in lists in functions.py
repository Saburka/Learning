n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for x in range(len(words)):
        result += words[x]
    return result


print join_strings(n)
