import os
import sys
import time
from datetime import datetime
from os import path

# NOTES: Verify version number on banner and writing output.

def printBanner():
    # VERIFY VERSION NUMBER FOR EACH UPDATE
    print("-------------------------------------------------------------------------------------------")
    print("    ██████╗ ███╗   ███╗██████╗  ██████╗ ███╗   ██╗                                         ") 
    print("   ██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗████╗  ██║                                         ")
    print("   ██║   ██║██╔████╔██║██████╔╝██║   ██║██╔██╗ ██║                                         ")
    print("   ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║██║╚██╗██║                                         ")
    print("   ╚██████╔╝██║ ╚═╝ ██║██║  ██║╚██████╔╝██║ ╚████║                                         ")
    print("    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                         ")
    print("   ██╗   ██╗███████╗██████╗ ██╗███████╗██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗  ")
    print("   ██║   ██║██╔════╝██╔══██╗██║██╔════╝██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║  ")
    print("   ██║   ██║█████╗  ██████╔╝██║█████╗  ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║  ")
    print("   ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝  ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║  ")
    print("    ╚████╔╝ ███████╗██║  ██║██║██║     ██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║  ")
    print("     ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝  ")
    print("   ████████╗ ██████╗  ██████╗ ██╗                                                          ")
    print("   ╚══██╔══╝██╔═══██╗██╔═══██╗██║                                                          ")
    print("      ██║   ██║   ██║██║   ██║██║                                                          ")
    print("      ██║   ██║   ██║██║   ██║██║                                                          ")
    print("      ██║   ╚██████╔╝╚██████╔╝███████╗                                       Version 1.01  ")
    print("      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                 by: Kirsten Sotelo  ")
    print("-------------------------------------------------------------------------------------------")
    print()
    print()                                             

def printDict(dict):
    tempString = "\nREF\tIPN\n"
    for key in dict:
        tempString += str(key) + "\t" + str(dict[key]) + "\n"
    return tempString

class refAndIpn:

    # method for reading the file and collecting the Ref and Ipn *** FOR REVISION FILES ONLY
    def collectRefAndIpnREV(file_path):
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
            REFandIPNDict = {val[0] : val[1] for val in sorted(REFandIPNDict.items(), key = lambda x: (x[1], x[0]))}
            #REFandIPNDict = {val[0] : val[1] for val in sorted(REFandIPNDict.items(), key = lambda x: (x[0], x[1]))} ---- line to sort by REF then IPN
            
            return REFandIPNDict
        else:
            raise Exception("This file is not compatible or does not exist")


    # method for reading the file and collecting the Ref and Ipn *** FOR OMRON TEXT FILES ONLY (essentially same as the revision method, but adjusted for the OMRON text file format)
    def collectRefAndIpnOMRON(file_path): 
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

                # defining temporary variables
                # X,Y,ROT,REST is not used for this program
                nothing = ""
                num = 0
                ref = ''
                ipn = ''
                rest = ""

                # the first 4 elements of splitted will always be the same format: 'None', number, REF, IPN, rest
                # everything after that (rest) is unimportant info and varies in length
                # use len(splitted), and assigning the first 5 elements accordingly, but if the count is greater than 4, just add it to the 'rest' variable
                for i in range(len(splitted)):
                    if i == 0:
                        nothing = str(splitted[i])
                    elif i == 1:
                        num = str(splitted[i])
                    elif i == 2:
                        ref = str(splitted[i])
                    elif i == 3:
                        ipn = str(splitted[i])
                    elif i >= 4:
                        rest += str(splitted[i]) + " "

                # create a refAndIpn object from these assigned variables AFTER the for loop above, and add it to the REFandIPNDict list if it has a valid ref and ipn.
                #tempREFandIPN = refAndIpn(ref, ipn)

                if nothing == "" and num == 0 and ref == '' and ipn == '' and rest == "":
                    continue
                elif len(rest) <= 3:
                    continue
                else:
                    #REFandIPNDict.update(ref = ipn)
                    REFandIPNDict[ref] = ipn

                # ---------- END OF READING LINES AND CREATING OBJECTS ---------------------------

            # sort the dict by IPN first, then REF  (value then key)(not exactly sure how this works, but it works)
            REFandIPNDict = {val[0] : val[1] for val in sorted(REFandIPNDict.items(), key = lambda x: (x[1], x[0]))}
            #REFandIPNDict = {val[0] : val[1] for val in sorted(REFandIPNDict.items(), key = lambda x: (x[0], x[1]))} ---- line to sort by REF then IPN
            
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

    def changedInNext(self, other):
        thisDict = self
        otherDict = other

         # changed list means the ref has a changed ipn (changed in next revision)
        changed = []

        # iterating through this dictionary's keys, if the key is in the other dictionary: check if this value is the same, if not the same, add to changed list
        for key in thisDict.keys():
            if key in otherDict.keys() and thisDict[key] != otherDict[key]:
                tempFromDict = {}
                tempToDict = {}
                tempFromDict.update({key: thisDict[key]})
                tempToDict.update({key: otherDict[key]})
                changed.append([tempFromDict, tempToDict])
            else:
                continue
            
        return changed
    
    def printChangedInNext(dict):
        tempString = ""
        tempString += "\nFrom:\t\t\tTo:"
        tempString += "\nREF\tIPN\t\tREF\tIPN\n"
        for i in dict:
            for j in i:
                for key, value in j.items():
                    tempString += str(key) + "\t" + str(value) + "\t\t"
            tempString += "\n"
        
        return tempString


# --------------------------------------------------- MAIN --------------------------------------------------------------
if __name__ == "__main__":
    # Print banner, ask for user inputs.
    printBanner()
    print("Files MUST be within the same folder and include '.prg' and '.txt'")
    
    file1Input = input("Enter Revision (.prg file): ")
    while path.isfile(file1Input) == False:
        file1Input = input("Please Re-enter Revision (.prg file):")
    else:
        file2Input = input("Enter OMRON Text File: ") 
        while path.isfile(file2Input) == False:
            file2Input = input("Please Re-enter OMRON Text File:")
    
    # With each input, collect the Ref and Ipn, and compile the differences. 
    refAndIpnDict1 = refAndIpn.collectRefAndIpnREV(file1Input)
    refAndIpnDict2 = refAndIpn.collectRefAndIpnOMRON(file2Input)
    unchangedInNext = refAndIpn.unchangedInNext(refAndIpnDict1, refAndIpnDict2)
    removedInNext = refAndIpn.removedInNext(refAndIpnDict1, refAndIpnDict2)
    addedInNext = refAndIpn.addedInNext(refAndIpnDict1, refAndIpnDict2)
    changedInNext = refAndIpn.changedInNext(refAndIpnDict1, refAndIpnDict2)

    # -------------------- WRITING NEW FILE ----------------------------------------------------------------
    file3Output = str((file1Input) + " compared to " + (file2Input))
    with open(file3Output, 'w') as newFile:
        # Start of writing file. Print version of the Compare tool then date. 
        # VERIFY VERSION NUMBER FOR EACH UPDATE
        newFile.write("Omron Verification Tool Version: 1.01")
        now = datetime.now()
        dt_string = now.strftime("%b-%d-%Y %H:%M:%S")
        newFile.write("\nDate Created: " + repr(dt_string))
        newFile.write("\n\nRevision File: " + repr(file1Input) + "\tLines: " + repr(len(refAndIpnDict1)))
        newFile.write("\nOmron File: " + repr(file2Input) + "\tLines: " + repr(len(refAndIpnDict2)))

        # Checking if the two revisions are the same. 
        if refAndIpn.checkSame(refAndIpnDict1, refAndIpnDict2):
            newFile.write("\n\nNo Difference Between " + repr(file1Input) + " and " + repr(file2Input))

        # If not the same, print the removed, added, and changed dicitonaries
        else:
            #print("Unchanged In Next Revision:")
            #printDict(unchangedInNextRevision)

            newFile.write("\n\nCHANGES:")
            if len(removedInNext) > 0:
                newFile.write("\n\nTo Add " + repr(len(removedInNext)) + " Items in OMRON File")
                tempString = printDict(removedInNext)
                newFile.write(tempString)

            if len(addedInNext) > 0:
                newFile.write("\nTo Remove " + repr(len(addedInNext)) + " Items in OMRON File")
                tempString = printDict(addedInNext)
                newFile.write(tempString)

            if len(changedInNext) > 0:
                newFile.write("\nTo Change " + repr(len(changedInNext)) + " Items in OMRON File")
                tempString = refAndIpn.printChangedInNext(changedInNext)
                newFile.write(tempString)
        
        newFile.close()
        # ---------- END OF FILE ---------------------------------------------------------------

        # Print confirmations
        if path.isfile(file3Output):
            print("A new file: '" + file3Output + "' has succesfully been created. Program will close in 3 seconds.")
        else:
            print("A new file has NOT been created. Format of input files are not compatible. Program will close in 3 seconds.")

        time.sleep(3)
