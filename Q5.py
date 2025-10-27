def copy_n_lines(n):
    try:
        file = open("Sample.txt", "r")
        chunk_file = open("Chunk.txt", "w")
        for i in range(n):
            line = file.readline()
            if not line:
                break
            chunk_file.writelines(line)
        
        file.close()
        chunk_file.close()
        print("Contents of Chunk.txt:")
        chunk_file = open("Chunk.txt", "r")
        print(chunk_file.read())
        chunk_file.close()

    except FileNotFoundError:
        print("Sample.txt not found. Make sure it's in the same folder.")

n = int(input("Enter how many lines to copy: "))
copy_n_lines(n)