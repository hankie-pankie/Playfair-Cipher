#I made a java file that encrypts strings with the playfair cipher
#I want to make some python to do the same

import math

alphabet = "abcdefghijklmnopqrstuvwxy"

codeword = raw_input("Enter a codeword: ")

message = raw_input("Enter some text to encrypt or decrypt: ")

#function to create the coded index fuck
def index(codeword) :
	#I would like to insert a line that changes codeword from
	#'apple' to 'aple' so that the index has no repeated letters
	index = alphabet
	#nested for loop that removes letters IN codeword FROM alphabet
	for x in alphabet :
		for y in codeword :
			if x == y :
				index = index.replace(x, "")
	#then adds codeword to begginning of alphabet
	index = codeword + index
	#if codeword=hamlet, index=hamletbcdfgijknopqrsuvwxy
	print index
	return index

#function to encrypt message with given index
def encrypt(message, index) :
	#I needed to remove spaces from and turn lowercase the string
	message = message.replace(" ", "")
	message = message.lower()
	#playfair cipher can only deal with 25 (0-24 for computer) letters
	#eliminate z
	message = message.replace("z", "x")
	#establish ciphertext that we can later add to
	ciphertext = ""
	#this is how I parse even and odd locations in the message
	#[0::2] = start at 0, go till end, move by 2
	#[1::2] = start at 1, go till end, move by 2
	even = message [0::2]
	odd = message [1::2]
	print even, odd
	#here is where playfair math starts
	for x in even :
		print ("x " + x)
		pos = index.index(x)
		print pos
		posPlus = index.index(x) #troublesome
		encPos = 5 * (math.	floor(pos / 5)) + posPlus - 5 * (math.floor(posPlus / 5))
		if(encPos > 24) :
					encPos = encPos - 24
		print pos
		print posPlus
		print encPos
	for x in odd :
		pos = index.index(x)
		posNeg = index.index(x) #troublesome
		encPos = 5 * (math.floor(pos / 5)) + posNeg - 5 * (math.floor(posNeg / 5))
		if(encPos > 24) :
					encPos = encPos - 24
		print pos
		print posNeg
		print encPos
		print ciphertext
	return ciphertext

encrypt(message, index(codeword))