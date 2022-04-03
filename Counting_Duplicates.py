def duplicate_count(text):

    count = {}
    text = list(text)
    total = 0;

    for idx, i in enumerate(text):
        if i.lower() not in count.keys():
            count[i.lower()] = 1
        else:
            count[i.lower()] = count[i.lower()] + 1

    for i in count.keys():
        if count[i] > 1:
            total = total + 1

    return total

print(duplicate_count("abcdeaB"))
