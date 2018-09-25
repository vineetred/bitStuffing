text = open('send.txt')
file_content= text.read()

output= ' '.join(format(ord(x), '08b') for x in file_content) #This converts the
#text file into 8 bit long binary forms of the charecter

finalString = output.replace(" ", "") #The above functions returns bit strings with spaces in them. This removes it.

unstuffedOutput = ""
decodedOutput = ""
count = 0 #Counter to check for consecutive 1s
# print(finalString + "\n")

for bit in finalString:
	standardOutput = bit

	if(count == 5):
		if(standardOutput == '0'):
			count = 1
		elif(standardOutput== '1'):
			count = count + 1
			unstuffedOutput = unstuffedOutput + standardOutput

	elif(count == 6):
		if(standardOutput == '1'):
			print("Transmission Error")
		elif(standardOutput == '0'):
			unstuffedOutput = unstuffedOutput[:len(unstuffedOutput)-7]
			count = 0
	elif(count<=4):
		if(standardOutput == '1'):
			count = count + 1
			unstuffedOutput = unstuffedOutput + standardOutput
		elif(standardOutput == '0'):
			count = 0
			unstuffedOutput = unstuffedOutput + standardOutput

for i in range(0,len(unstuffedOutput),8):
    decodedOutput = decodedOutput + chr(int(unstuffedOutput[i:i+8], 2))
# print(decodedOutput)

f = open("output.txt", "w")
f.write(decodedOutput)
f.close