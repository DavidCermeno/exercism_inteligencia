def convert(number):
    factorable = ""
    if number % 3 == 0:
        factorable += "Pling"
    if number % 5 == 0:
        factorable += "Plang"
    if number % 7 == 0:
        factorable += "Plong"
    if factorable:
        return factorable
    if not factorable:
        return str(number)

print(convert(28))
print(convert(30))
print(convert(34))
print(convert(8))
print(convert(52))
print(convert(1))
