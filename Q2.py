def join_strings(str1, str2):
    joined = str1 + " " + str2
    length = len(joined)
    return joined, length

first = input("Enter the first string: ")
second = input("Enter the second string: ")

result, size = join_strings(first, second)

print("The joined string:", result)
print("Length of new string:", size)