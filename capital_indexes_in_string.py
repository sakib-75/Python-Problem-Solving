def capital_indexes(string):
    index = []
    for char_index, char in enumerate(string):
        if char.isupper():
            index.append(char_index)
        else:
            continue
    return index


print(capital_indexes("TEsT WoRd"))
