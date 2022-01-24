def disemvowel(string):
    chars = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
    for i in string:
        if i in chars:
            string = string.replace(i, "")
    return string


st = "O Hi my name is slim shady nAme gas   aaaAass "
print(disemvowel(st))