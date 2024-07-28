# inputFile = open("inputFile.txt", "r")
# for line in inputFile:
#     line_split = line.split()
#     if line_split[2] == "P":
#         print(line)
# inputFile.close()


inputfile = open("Exercise Files/inputFile.txt", "r")
for line in inputfile:
    line_slpit = line.split()  # whe you split something it becomes a list
    if line_slpit[-1] == "F":
        print(line)
inputfile.close()