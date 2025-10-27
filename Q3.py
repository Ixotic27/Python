def count(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        file.close()

        count = 0

        for i in range(len(content)):
            ascii = ord(content[i])
            if not (48 <= ascii <= 57 or 65 <= ascii <= 90 or
                    97 <= ascii <= 122 or ascii == 32):
                count += 1

        print("Number of special characters:", count)

    except FileNotFoundError:
        print("File not found. Check the name again.")
file=input("Enter the file name: ")
count(file)