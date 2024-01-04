
# !Closing a file will free up the resources that were tied with the file. It is done using the close() method in Python/include working directory
file1 = open("5-fileHandling/test1.txt", "r")
read_content = file1.read()
print(read_content)
file1.close()

# !no need to specify close() when using the with...open syntax
# read from test1.txt
with open("5-fileHandling/test1.txt") as text_file:
    text = text_file.read()
    print(text)

# write to test1.txt/overwrites
with open("5-fileHandling/test1.txt", mode="w") as text_file:
    text_file.write("Samson is a Software Engineer!")

# when no file exists/creates new file
with open("5-fileHandling/test2.txt", mode="w") as text_file:
    text_file.write("Programming is fun!")
    
# append to test1.txt
with open("5-fileHandling/test1.txt", mode="a") as text_file:
    text_file.write("Samson loves coding in JavaScript and Python!")

# test changes
with open("5-fileHandling/test1.txt") as text_file:
    text = text_file.read()
    print(text)

# !try...finally
# If an exception occurs when we are performing some operation with the file, the code exits without closing the file. A safer way is to use a try...finally block.
try:
    file1 = open("5-fileHandling/test1.txt", "r")
    read_content = file1.read()
    print(read_content)
finally:
    file1.close()

'''
TODO: check on file operation methods
close/detach/fileno/flush/isatty/read/readable/readline/readlines/seekable/tell/truncate/writable/write/writelines/
'''