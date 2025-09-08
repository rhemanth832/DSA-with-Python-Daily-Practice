def isValid(s : str) -> bool:
    while "()" in s or "[]" in s or "{}" in s:
        s=s.replace("()", "").replace("[]", "").replace("{}", "")
    return not s
print(isValid('{}'))
print(isValid("(]]"))
print(isValid("({[]})"))