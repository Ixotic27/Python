def find(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        file.close()

        words = content.split()

        target = ['a', 'c', 'd', 'g', 'p', 's']
        print("Words starting with a, c, d, g, p, or s:")

        for i in words:
            if i[0] in target:
                print(i,end=" ")

    except FileNotFoundError:
        print("File not found. Please check the file name.")

file = input("Enter the file name: ")
find(file)