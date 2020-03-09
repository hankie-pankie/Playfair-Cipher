#I made a java file that encrypts strings with the playfair cipher
#I want to make some python to do the same

import pdb
import math

alphabet = "abcdefghijklmnopqrstuvwxy"

codeword = raw_input("Enter a codeword: ")

message = raw_input("Enter some text to encrypt or decrypt: ")

#function to create the coded index
def indexus(codeword) :
	#I would like to insert a line that changes codeword from
	#'attack' to 'atck' so that the index has no repeated letters
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
	if len(message) % 2 == 1:
		message = message + "x"
	ciphertext = ""

	enuMessage = enumerate(message)
	for ind, letter, in enuMessage:
		iPos = indexC.index(letter)

		#pdb.set_trace()
		if ind % 2 == 0:
			pos2 = indexC.index(message[ind + 1])
			encPos = 5 * (math.floor(iPos / 5)) + pos2 - 5 * (math.floor(pos2 / 5))
			if encPos > 24 :
				encPos = encPos - 24
			if encPos < 0 :
				encPos = encPos + 24
			encPos = int(encPos)
			encLetter = indexC[encPos]
			#hmmmmm
		else:
			pos2 = indexC.index(message[ind - 1])
			encpos = 5 * (math.floor(iPos / 5)) + pos2 - 5 * (math.floor(pos2 / 5))
			if encPos > 24 :
				encPos = encPos - 24
			if encPos < 0 :
				encPos = encPos + 24
			encPos = int(encPos)
			encLetter = indexC[encPos]

		print ind, letter, iPos, encLetter, pos2

		ciphertext += encLetter

	print ciphertext

	return ciphertext

encrypt(message, indexus(codeword))