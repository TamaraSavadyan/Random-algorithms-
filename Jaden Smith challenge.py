def to_jaden_case(string):
    s1 = string.title()
    return s1


def jaden_case(string):
    string = list(string)
    string1 = ""
    k = 0
    string[0] = string[0].upper()
    while k < len(string):
        if string[k] == " ":
            string[k + 1] = string[k + 1].upper()
        k += 1
    return string1.join(string)


def jaden_WINNER(string):
    string = string[0].upper() + string[1:]
    for i in range(0, len(string)):
        if string[i] == " ":
            string = string[:i + 1] + string[i + 1].upper() + string[i + 2:]
    return string


s = "how can mirrors be real if our eyes aren't real"
s1 = s
s = jaden_WINNER(s)
print(s1, " RESULT: ", s)
print(jaden_case(s1))
print(to_jaden_case(s1))
