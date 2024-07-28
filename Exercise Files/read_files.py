# inputFile = open("inputFile.txt", "r")
# for line in inputFile:
#     line_split = line.split()
#     if line_split[2] == "P":
#         print(line)
# inputFile.close()


inputfile = open("inputFile.txt", "r")
for line in inputfile:
    line_slpit = line.split()
    if line_slpit[-1] == "P":
        print(line)
inputfile.close()