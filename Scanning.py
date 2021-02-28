import sys,os
import re
import inflect

convert = inflect.engine() #used to convert number to words
OutPut = open('TestingOutPut.txt','w') #Open Txt file outputs  

def LoadFile(FileName):
    #Open Txt file that has been allocated for the input
    #reads content and splits the different lines 
    #then file would be closed and the lines would be used for checking.
    Content = TestVar.read()
    TestVar = open(FileName,'r') 
    splitline = Content.splitlines()#splits the lines
    TestVar.close()
    return splitline

def CheckForNumbers(CheckingStrings):#checks for validation on the string
    WithDigits = re.findall('\\S\\d+\\S',CheckingStrings)
    #finds numbers with space on either side 
    #to outline the invalidations
    #for loop check whether the findings are digits. 
    #if true it would use the function to change it into words 
    #if not it would return invalidate.
    for i in range(len(WithDigits)):
        if WithDigits[i].isnumeric()!=False:
            WithDigits = convert.number_to_words(WithDigits)
            print(CheckingStrings+"\nNumber converted: " + WithDigits+"\n",file=OutPut)
        else:
            print("Number Invalid\n",file=OutPut)
            
    return WithDigits

#allcate the file and calles functions
Sentence = LoadFile("Testing.txt")
for sentences in Sentence:
    CheckForNumbers(sentences)


#CheckForNumbers(Scan())
#CheckForNumbers(Scan())
#CheckForNumbers(Scan())
#CheckForNumbers(Scan())
#CheckForNumbers(Scan())
#CheckForNumbers(Scan())

#for line in TestVar:
        #    splitline = line.split(".")
        #    informations = convert.number_to_words(splitline)
        #    print(informations,file=OutPut)
        #ChangeToString = "".join(splitline)# joins the split so its not a list