"""
1- Reading and writing files
"""


# create and write to a file
file = open("file_created.txt", "w")

file.writelines("hello \n")
file.writelines("i \n")
file.writelines("created \n")
file.writelines("this \n")
file.writelines("file")
file.writelines(["testing \n", "next \n", "line \n"])

file.close()

file = open("file_created.txt", "r")

for i in file.readlines():
    print(i)

file.close()
