newfile = open("dairy.text","w")
newfile.write("why you like about these session\n")
newfile.write("why you like about these session\n")
newfile.write("why you hate this session")

newfile.close()

newfile2 = open("dairy.text","r")
content = newfile2.read()
print(content)

newfile2.close()