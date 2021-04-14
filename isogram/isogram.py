def is_isogram(string):
    lstring = list(string.lower())
    for i in range(len(lstring)):
        if lstring[i] in lstring[i+1:]:
            if lstring[i] not in (" ", "-"):
                return False
    return True
