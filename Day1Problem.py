sampleInput = open("day1_SampleInput.txt", "r")
list1 = []
list2 = []
netDifference = 0
fileLine = sampleInput.readline()
lineCount = 0
while fileLine != "":
    lineCount += 1
    fileContents = fileLine.split(" ")
    print(fileContents)
    list1.append(int(fileContents[0]))
    list2.append(int(fileContents[3][:5:]))
    fileLine = sampleInput.readline()
print("Number of lines read : " + str(lineCount))
list1.sort()
list2.sort()
for i in range(len(list1)):
    netDifference += abs(list1[i] - list2[i])
print(netDifference)

for i in range(len(list1)):
    list1[i] = (list1[i])*(list2.count(list1[i]))
print(sum(list1))

