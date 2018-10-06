text = open('input.txt')
file_content= text.read()

output= ' '.join(format(ord(x), '08b') for x in file_content) #This converts the
#text file into 8 bit long binary forms of the charecter

finalString = output.replace(" ", "") #The above functions returns bit strings with spaces in them. This removes it.

standardOutput = ""
stuffedOutput = ""
decodedOutput = ""
count = 0 #Counter to check for consecutive 1s
seperate = '01111110' #Frame separatorprint(finalString + "\n")
print(file_content)
for bit in finalString: 
    standardOutput = bit #loading each bit into the the var
    
    if(count == 5):
        count = 1
        stuffedOutput = stuffedOutput + '0' + standardOutput #Putting an end to consecutive 1s

    elif(count<=4):
        if(standardOutput == '1'):
            count = count + 1
            stuffedOutput = stuffedOutput + standardOutput

        elif(standardOutput == '0'):
            count = 0
            stuffedOutput = stuffedOutput + standardOutput

    if(len(stuffedOutput)%400==0):
        stuffedOutput = stuffedOutput + seperate

stuffedOutput = seperate + stuffedOutput #Adding the flag to the first frame


for i in range(0,len(stuffedOutput),8):
    decodedOutput = decodedOutput + chr(int(stuffedOutput[i:i+8], 2))
# print(decodedOutput)

f = open("send.txt", "w")
f.write(decodedOutput)
f.close