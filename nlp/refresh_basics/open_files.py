# 1. Open and read a file

myfile = open('text.txt')

# Prints the content of the file
# print(myfile.read())

# Returns the cursor from end of the file to the start
# myfile.seek(0)

# content = myfile.readlines()
# myfile.close()
#
# for line in content:
#     print(line)
# # myfile.read()


# 2. Open and write(overwrite) to a file

# myfile = open('text.txt', 'w+')
# myfile.write('New text')
# myfile.seek(0)
# print(myfile.read())
# myfile.close()


#3. Create/Open and write(append) to a file

# myfile = open('likes.txt', 'a+')
# myfile.write("I look, I look, I hear")
# myfile.close()
#
# newfile = open('likes.txt')
# print(newfile.read())
# newfile.close()
#
# myfile = open('likes.txt', mode='a+')
# myfile.write('\nHe sent the Prophets to show us the way')
# myfile.close()
#
# newfile = open('likes.txt')
# print(newfile.read())

# 4. Using a sample context manager to automatically close file after opening

with open('likes.txt', mode='r') as thefile:
    print(thefile.read())
