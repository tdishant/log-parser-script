import os # for working with files
import re # for finding words in log file using regex

TEXT_TO_FIND = [] # words to find inside the log files
PATH_TO_LOGS = "logs/" # path to the log files

# function to create regex pattern from the given list of words to find
def getRegexPattern():
    return "|".join(TEXT_TO_FIND)

# function to read all the log files and find the words
def processLogs():
    patternToFind = getRegexPattern() # get the regex pattern to find
    for fileName in os.listdir(PATH_TO_LOGS): # iterate over each file in logs folder
        filePath = os.path.join(PATH_TO_LOGS, fileName) # create the complete file path
        if (os.path.isfile(filePath)): 
            print("Reading the file {0}".format(filePath))
            with open(filePath, 'r') as file: # open the file
                for line in file: # read the file line-wise
                    match = re.search(patternToFind, line) # check if word is found in the line
                    if match:
                        with open("output.log", "a") as outputFile: # if the word is found in a line, then write it in "output.log" file
                            outputFile.write(line)
            print("Successfully read the file {0}".format(filePath))
        else:
            print("Error in reading file {0}".format(filePath))

# the main function of the script
def main():
    print("Iterating over each log file inside the {0} directory".format(PATH_TO_LOGS))
    processLogs()
    print("Successfully iterated over each log file inside the {0} directory".format(PATH_TO_LOGS))

# the script starts here
if __name__ == "__main__":
    print("SCRIPT STARTS HERE")
    main()
    print("SCRIPT ENDS HERE")