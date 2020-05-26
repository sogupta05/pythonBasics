f = open('factorial.py','r')  # open a file in read only mode

print(f.readline())

f1 = open('abc','w')  # 'w' is for writing, it will overwrite any existing data
# 'a' is for append, it will append new data to already existing one
f1.write("new file")

for data in f:  #making a copy of the file
    f1.write(data)

pic = open('ip.JPG','rb')

#for data in pic:  #making a copy of the file
#    print(data)

pic2 = open('sonia1.JPeG','wb')

for data in pic:  #making a copy of the file
    pic2.write(data)
