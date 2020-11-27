#Python Playfair cipher algorithm

import pdb
import math

#alphabet = [a-z]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "u", "v", "w", "x", "y"]
alphabob = []

def phormat(txt) :
	txt = txt.replace(" ", "")
	txt = txt.lower()
	txt	= txt.replace("z", "x")
	txt = splt(txt)
	return txt

def splt(word) :
	return [char for char in word]

#function to create the coded index
def indexus(key) :
	key.extend(alphabet)
	for x in key :
		if x not in alphabob :
			alphabob.append(x)
	return alphabob

#function to encrypt message with given index
def encrypt(plaintext, idx) :
	#something funky
	if len(plaintext) % 2 == 1 :
		plaintext.append("x")
	ciphertext = ""
	enutext = enumerate(plaintext)
	for pos,letr in enutext :
		idx = alphabob.index(letr)	
		if pos % 2 == 0 :
			posPlus = alphabob.index(plaintext[pos + 1])
			edx = 5 * (math.floor(idx / 5)) + posPlus - 5 * (math.floor(posPlus / 5))
			if edx > 24 :
				edx = edx - 24
			if edx < 0 :
				edx = edx + 24
			edx = int(edx)
			echar = alphabob[edx]
			if echar == plaintext[pos] :
				echar = plaintext[pos + 1]
			ciphertext += echar
		else :
			posNeg = alphabob.index(plaintext[pos - 1])
			edx = 5 * (math.floor(idx / 5)) + posNeg - 5 * (math.floor(posNeg / 5))
			if edx > 24 :
				edx = edx - 24
			if edx < 0 :
				edx = edx + 24
			edx = int(edx)
			echar = alphabob[edx]
			if echar == plaintext[pos] :
				echar = plaintext[pos - 1]
			ciphertext += echar
	print ciphertext
	return ciphertext

key = raw_input("Enter a codeword: ")
key = phormat(key)

plaintext = raw_input("Enter some text to encrypt or decrypt: ")
plaintext = phormat(plaintext)

butt = indexus(key)
encrypt(plaintext, butt)

#encrypt(plaintext, indexus(key))