# f=open("file.txt",'w')
# f.write("This is file concept. Write the content into the file in write mode")
f=open("file.txt",'r')
# print(f.read())
t=open("wfile.txt",'w')
t.write("This is write file")

for data in f:
    t.write(data)

af=open("data.txt",'a')
af.write("Go with the flow")