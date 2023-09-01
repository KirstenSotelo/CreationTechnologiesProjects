import os
import sys
from os import path

def printDict(dict):
    print("REF\t IPN")
    for key in dict:
        print(key, "\t", dict[key])

class refAndIpn:

    # method for reading the file and collecting the Ref and Ipn
    def collectRefAndIpn(file_path):
        REFandIPNDict = {}

    # --------- START OF READING LINES ---------------------
        # Checking if reading the file path is valid
        if(os.path.isfile(file_path)):

            #if valid, open the filepath and set to read. 'while True' line is for "while this file has a next element, else, break"
            file = open(file_path, 'r')
            while True:

                # Checking if the line exists, else, break from loop
                line = file.readline()
                if not line:
                    break
                
                # Checking if the line is only empty spaces(for whatever reason), then ignore this line
                if line.isspace():
                    continue
                
                # split the line, and get rid of any empty strings and new line strings
                splitted = line.split('\t')
                while ('') in splitted:
                    splitted.remove('')
                while ('\n') in splitted:
                    splitted.remove('\n')

                # after organizing the line, check if the first 3 characters are equal to "GFT", if true, then ignore the whole line
                """ if len(splitted) > 0:
                    gftCheck = splitted[0][:3]
                    if gftCheck == "GFT" or gftCheck == "GFB":
                        continue """
                    

                # defining temporary variables
                # X,Y,ROT,REST is not used for this program
                ref = ""
                ipn = 0
                x = 0
                y = 0
                rot = 0
                rest = ""

                # the first 5 elements of splitted will always be the same format: str, int, int, int, str
                # everything after that (rest) is unimportant info and varies in length
                # use len(splitted), and assigning the first 5 elements accordingly, but if the count is greater than 5, just add it to the 'rest' variable
                for i in range(len(splitted)):
                    if i == 0:
                        ref = str(splitted[i])
                    elif i == 1:
                        ipn = str(splitted[i])
                    elif i == 2:
                        x = int(splitted[i])
                    elif i == 3:
                        y = int(splitted[i])
                    elif i == 4:
                        rot = str(splitted[i])
                    elif i >= 5:
                        rest += str(splitted[i]) + " "

                # create a refAndIpn object from these assigned variables AFTER the for loop above, and add it to the REFandIPNDict list if it has a valid ref and ipn.
                #tempREFandIPN = refAndIpn(ref, ipn)

                if ref == "" and x == 0 and y == 0 and rot == 0 and rest == "":
                    continue
                elif len(rest) <= 3:
                    continue
                else:
                    #REFandIPNDict.update(ref = ipn)
                    REFandIPNDict[ref] = ipn

                # ---------- END OF READING LINES AND CREATING OBJECTS ---------------------------

            # sort the dict by IPN first, then REF  (value then key)(not exactly sure how this works, but it works)
            REFandIPNDict = {val[0] : val[1] for val in sorted(REFandIPNDict.items(), key = lambda x: (x[0], x[1]))}
            
            return REFandIPNDict
        else:
            raise Exception("This file is not compatible or does not exist")

    # method for comparing this object with other object (able to use ==)
    def __eq__(self, other): 
        if not isinstance(other, refAndIpn):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.REF == other.REF and self.IPN == other.IPN
    
    def checkSame(self, other):
        thisDict = self
        otherDict = other
        if thisDict == otherDict:
            return True

    def unchangedInNext(self, other):
        thisDict = self
        otherDict = other

         # changed list means the ref has a changed ipn (changed in next revision)
        unchanged = {}

        # iterating through this dictionary's keys, if the key is in the other dictionary: check if this value is the same, if not the same, add to changed list
        for key in thisDict.keys():
            if key in otherDict.keys() and thisDict[key] == otherDict[key]:
                unchanged.update({key: thisDict[key]})
            else:
                continue
            
        return unchanged
    
    def removedInNext(self, other):
        thisDict = self
        thisDictKeys = thisDict.keys()
        otherDict = other
        otherDictKeys = otherDict.keys()
        
        # removed list means the ref and ipn are in list1, but not the other list (removed in next revision); iterate through ref of thisDict, then compare with the ref of otherDict?
        removed = {}
        # iterating through this dictionary's keys, if the key is not in the other dictionary, then it was removed in the next revision
        for key in thisDict.keys():
            if key not in otherDictKeys:
                removed.update({key: thisDict[key]})
        return removed
        
    def addedInNext(self, other):
        thisDict = self
        otherDict = other

        # added dictionary means a new ref and ipn are in list2, but not in the first list (added in next revision)
        added = {}

        # iterating through this dictionary's keys, if the key is in the other dictionary: check if this value is the same
        for key in otherDict.keys():
            if key not in thisDict.keys():
                    #added[key] = otherDict[key]
                added.update({key: otherDict[key]})

        return added

    def adjustedInNext(self, other):
        thisDict = self
        otherDict = other

         # changed list means the ref has a changed ipn (changed in next revision)
        adjusted = []

        # iterating through this dictionary's keys, if the key is in the other dictionary: check if this value is the same, if not the same, add to changed list
        for key in thisDict.keys():
            if key in otherDict.keys() and thisDict[key] != otherDict[key]:
                tempFromDict = {}
                tempToDict = {}
                tempFromDict.update({key: thisDict[key]})
                tempToDict.update({key: otherDict[key]})
                adjusted.append([tempFromDict, tempToDict])
            else:
                continue
            
        return adjusted
    
    def printChangedInNext(dict):
        print("From:\t\t\t To:")
        print("REF\t IPN\t\t REF\t IPN")
        for i in dict:
            for j in i:
                for key, value in j.items():
                    print(key, "\t", value, "\t", end = " ")
            print()

            """ for eachInnerList in outerList:
                print(eachInnerList) """

            """ for eachkey in eachInnerList:
                print(eachkey, "\t", eachInnerList[eachkey]) """


if __name__ == "__main__":
    print("------------------------------------------------------------")
    print(" ██████╗ ███████╗██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗ ") 
    print(" ██╔══██╗██╔════╝██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║ ")
    print(" ██████╔╝█████╗  ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║ ")
    print(" ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║ ")
    print(" ██║  ██║███████╗ ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║ ")
    print(" ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ")
    print(" ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ██████╗ ███████╗")
    print("██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗██╔════╝")
    print("██║     ██║   ██║██╔████╔██║██████╔╝███████║██████╔╝█████╗  ")
    print("██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██╔══██╗██╔══╝  ")
    print("╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║██║  ██║███████╗")
    print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
    print(" ████████╗ ██████╗  ██████╗ ██╗                             ")
    print(" ╚══██╔══╝██╔═══██╗██╔═══██╗██║                             ")
    print("    ██║   ██║   ██║██║   ██║██║                             ")
    print("    ██║   ██║   ██║██║   ██║██║                             ")
    print("    ██║   ╚██████╔╝╚██████╔╝███████╗             Version 1.0")
    print("    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝       by Kirsten Sotelo")
    print("------------------------------------------------------------")
    print()
    print()
    print("Files MUST be within the same folder and include '.prg' (Ctrl+Shft+V to paste)")
    
    file1Input = input("Enter Old Revision: ")
    while path.isfile(file1Input) == False:
        file1Input = input("Please re-enter Old Revision:")
    else:
        file2Input = input("Enter New Revision: ") 
        while path.isfile(file2Input) == False:
            file2Input = input("Please re-enter New Revision:")

    refAndIpnDict1 = refAndIpn.collectRefAndIpn(file1Input)
    refAndIpnDict2 = refAndIpn.collectRefAndIpn(file2Input)
    adjustedInNextRevision = refAndIpn.unchangedInNext(refAndIpnDict1, refAndIpnDict2)
    removedInNextRevision = refAndIpn.removedInNext(refAndIpnDict1, refAndIpnDict2)
    addedInNextRevision = refAndIpn.addedInNext(refAndIpnDict1, refAndIpnDict2)
    changedInNextRevision = refAndIpn.adjustedInNext(refAndIpnDict1, refAndIpnDict2)

    # Creating a text file with name "revDifferenceRaw", which is the output of the terminal
    file3Output = str((file1Input) + " compared to " + (file2Input))
    sys.stdout = open(file3Output, 'w')

    if refAndIpn.checkSame(refAndIpnDict1, refAndIpnDict2):
        print("NO CHANGES IN NEXT REVISION")
    else:
        #print("Unchanged In Next Revision:")
        #printDict(unchangedInNextRevision)

        print()
        print("Rev1: ", file1Input, "\tLines:", len(refAndIpnDict1))
        print("Rev2: ", file2Input, "\tLines:", len(refAndIpnDict2))

        print("\nCHANGES:")
        if len(removedInNextRevision) > 0:
            print("\nRemoved ", len(removedInNextRevision), " Items in Next Revision ( Removed from", file1Input, "): ")
            printDict(removedInNextRevision)

        if len(addedInNextRevision) > 0:
            print("\nAdded ", len(addedInNextRevision), " Items in Next Revision ( Added to", file2Input, "): ")
            printDict(addedInNextRevision)

        if len(adjustedInNextRevision) > 0:
            print("\nChanged ", len(changedInNextRevision), " Items in Next Revision ( Changed from", file1Input, "to", file2Input, "): ")
            refAndIpn.printChangedInNext(changedInNextRevision)

        sys.stdout.close()

    
