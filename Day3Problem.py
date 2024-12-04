import re 

filePointer = open("day3_SampleInput.txt", "r")
fileContents = filePointer.read()
# fileContents = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
goodValues = 0
# print(fileContentsBroken)
fileBrokenByDOs = fileContents.split("do()")
for j in fileBrokenByDOs:
    dontBreaks = j.split("don't()")
    doableMULs = dontBreaks[0]
    fileContentsBroken = doableMULs.split("mul(")
    for i in fileContentsBroken:
    # print("i : ", i)
        commaSplit = i.split(",")
        if commaSplit[0].isnumeric() == True:
            bracketSplit = commaSplit[1].split(")")
            if bracketSplit[0].isnumeric() == True:
                goodValues += (int)(commaSplit[0])*int(bracketSplit[0])
print(goodValues)