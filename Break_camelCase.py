def solution(s):

    s = list(s)
    idx = 0

    while idx < len(s):
        if s[idx].isupper():
            s.insert(idx, " ")
            idx = idx + 1
        idx = idx + 1
    return "".join(s)

solution("helloWorld")
