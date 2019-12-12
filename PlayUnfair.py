#I made a java file that encrypts strings with the playfair cipher
#I want to make some python to do the same

import math

alphabet = "abcdefghijklmnopqrstuvwxy"

codeword = raw_input("Enter a codeword: ")

message = raw_input("Enter some text to encrypt or decrypt: ")

#function to create the coded index
def indexus(codeword) :
	#I would like to insert a line that changes codeword from
	#'jonathan' to 'jonathn' so that the index has no repeated letters
	indexC = alphabet
	#nested for loop that removes letters IN codeword FROM alphabet
	for x in alphabet :
		for y in codeword :
			if x == y :
				indexC = indexC.replace(x, "")
	#then adds codeword to begginning of alphabet
	indexC = codeword + indexC
	#if codeword=hamlet, index=hamletbcdfgijknopqrsuvwxy
	print indexC
	return indexC

#function to encrypt message with given index
def encrypt(message, indexC) :
	#I needed to remove spaces from and turn lowercase the string
	message = message.replace(" ", "")
	message = message.lower()
	#playfair cipher can only deal with 25 (0-24 for computer) letters
	#eliminate z
	message = message.replace("z", "x")
	#establish nil ciphertext that we can later add to
	ciphertext = ""

	#for x in message :
	#	pos = indexC.index(x)
	#	print pos

	#this is how I parse even and odd locations in the message
	#[0::2] = start at 0, go till end, move by 2
	#[1::2] = start at 1, go till end, move by 2
	even = message [0::2]
	odd = message [1::2]
	print message
	print even, odd

	#so far everything works

	#here is where playfair math starts
	for x in even :
		iPos = indexC.index(x)	#index position of x in message
		mPos = message.index(x)
		print x, "pos", iPos
		posPlus = indexC.index(message[mPos + 1])	#needs to find position of next letter in message
		print message[mPos + 1], "posPlus", posPlus
	#	encPos = 5 * (math.	floor(pos / 5)) + posPlus - 5 * (math.floor(posPlus / 5))
	#	encPos = encPos - 24
	for x in odd :
		iPos = indexC.index(x)
		mPos = message.index(x)
		print x, "pos", iPos
		posNeg = indexC.index(message[mPos - 1])
		print message[mPos - 1], "posNeg", posNeg
	#	encPos = 5 * (math.floor(pos / 5)) + posNeg - 5 * (math.floor(posNeg / 5))
	#	if(encPos > 24) :
	#	encPos = encPos - 24
	return ciphertext

encrypt(message, indexus(codeword))