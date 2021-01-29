# F:\python
# file=open("hello.txt", "a")
# file.write("\n i am here Sumit Singh")
# file.close()

#---To read the data---
# file=open("hello.txt", "r")
# d=file.read()
# print(d)
# file.close()

# ---To read the data, second method---
# file=open("hello.txt", "r")
# print(file.read(20))
# file.seek(0)
# print(file.read())
# file.close()

# ---To read lines and tell--- 
# file=open("hello.txt", "r")
# print(file.readline(20))
# print(file.readlines())
# print(file.tell())
# file.close()

#---Excercise for read and write from txt files---
#This program is to read
# file=open("hello.txt", "r")
# d=file.read()
# file.close()

#---This program is to write from above file---
# file=open("demo.txt", "w")
# file.write(d)
# print(d)
# file.close()

#---Reading and writing an image file---
#---This program is to read the image---
file=open("bullet.jpg", "rb+")
d=file.read()
# file.close()

# #This program is to write from the above image
# file=open("Royal_Enfiled.jpg", "wb+")
# file.write(d)
# file.close()

# To make a copy of an image using loop.

i=10
if i<=1:
    for i in file :
        file=open("Royal_Enfiled.jpg", "wb+")
        file.write(d)
        i=i+1
    file.close()
file.close()
    

# to find out a particular alphabet in a text file & print the total count.

