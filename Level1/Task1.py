#Task1: String Reversal
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "hello"

print("The Original String is: ", end="")
print(s)

print("The revers string(Using loop) is :",end="")
print(reverse(s))
