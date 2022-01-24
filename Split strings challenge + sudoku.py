
def solution(s):
    splitted = list()
    s1 = "_"
    if len(s) % 2 != 0:
        s = s + s1
    for i in range(0, len(s)):
        if i % 2 == 0:
            splitted.append(s[i:i+2])
    return splitted


s = "1234567"
print(solution(s))
