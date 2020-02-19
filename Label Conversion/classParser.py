import os
import sys
import fileinput



currentPath = os.getcwd()
# currentPath += '/filesToRead/'
currentPath += '/' + sys.argv[1]

print(currentPath)

targetPath = currentPath[:-1]
targetPath += '_converted/'

if not os.path.exists(targetPath):
    os.makedirs(targetPath)
# targetPath = os.getcwd()
# targetPath += '/convertedFiles/'

#TO USE THIS ADD THE FILES IN A 'filesToRead' FOLDER IN THE LOCATION OF THE SCRIPT.
#EDIT THE CONE CODES TO THE NUMBER OF CLASS YOU ARE USING.
print(sys.argv)
# yellowConeCode = 2
print(len(sys.argv))
orangeConeCode = int(sys.argv[2])
blueConeCode = int(sys.argv[3])
yellowConeCode = int(sys.argv[4])
bigOrangeConeCode = int(sys.argv[5])
#EDIT THE CONE CODES TO THE NUMBER OF CLASS YOU ARE USING.


noOfYellowCones = 0
noOfBlueCones = 0
noOfOrangeCones = 0
noOfBigOrangeCones = 0
noOfFilesScanned = 0
noOfLinesScanned = 0

for filename in os.listdir(currentPath):
    pathOfFile = currentPath + '/' + filename
    pathOfTargetFile = targetPath + '/' + filename
    file = open(pathOfFile, "r")
    targetFile = open(pathOfTargetFile, "w")
    noOfFilesScanned += 1

    for line in file:
        noOfLinesScanned += 1
        if line[0] == str(orangeConeCode):
            line = str(0) + line[1:] 
        elif line[0] == str(blueConeCode):
            line = str(1) + line[1:] 
        elif line[0] == str(yellowConeCode):
            line = str(2) + line[1:] 
        elif line[0] == str(bigOrangeConeCode):
            line = str(3) + line[1:] 

        targetFile.write(line)

    file.close()
    targetFile.close()

# for line in fileinput.input(os.listdir(currentPath), inplace=True):



sys.stdout.write("scanned {} lines \n".format(noOfLinesScanned))
    #     if line[0] == str(yellowConeCode):
    #         noOfYellowCones += 1
    #     elif line[0] == str(blueConeCode):
    #         noOfBlueCones += 1
    #     elif line[0] == str(orangeConeCode):
    #         print("FILE:" + filename)
    #         noOfOrangeCones += 1
    #     elif line[0] == str(bigOrangeConeCode):
    #         noOfBigOrangeCones += 1


# print("No of Files Scanned: " + str(noOfFilesScanned))
# print("No of Yellow Cones: " + str(noOfYellowCones))
# print("No of Blue Cones: " + str(noOfBlueCones))
# print("No of Orange Cones: " + str(noOfOrangeCones))
# print("No of Big Orange Cones: " + str(noOfBigOrangeCones))
# print("No of Cones " + str(noOfYellowCones + noOfBlueCones + noOfOrangeCones + noOfBigOrangeCones))