# Python code to reverse a string

def reverse_1(s):
    string = ""
    for i in s:
        string = i + string
    return string


def reverse_2(s):
    if len(s) == 0:
        return s
    else:
        return reverse_2(s[1:]) + s[0]


given_string = "Sakibul Islam"
print("The original string: ", given_string)
print("The reversed string: ", reverse_1(given_string))
print("The reversed string: ", reverse_2(given_string))
