#Python Playfair cipher algorithm

import pdb
import math

#alphabet = [a-z]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "u", "v", "w", "x", "y"]
indeks = []

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
		if x not in indeks :
			indeks.append(x)
	return indeks

#function to encrypt message with given index
def encrypt(plaintext, idx) :
	#something funky
	if len(plaintext) % 2 == 1 :
		plaintext.append("x")
	ciphertext = ""
	enutext = enumerate(plaintext)
	for pos,letr in enutext :
		#index of each letter in indeks
		idx = indeks.index(letr)	
		if pos % 2 == 0 :
			posPlus = indeks.index(plaintext[pos + 1])
			#new encrypted position of letter in indeks
			edx = 5 * (math.floor(idx / 5)) + posPlus - 5 * (math.floor(posPlus / 5))
			if edx > 24 :
				edx = edx - 24
			if edx < 0 :
				edx = edx + 24
			edx = int(edx)
			eletr = indeks[edx]
			if eletr == plaintext[pos] :
				eletr = plaintext[pos + 1]
			ciphertext += eletr
		else :
			posNeg = indeks.index(plaintext[pos - 1])
			edx = 5 * (math.floor(idx / 5)) + posNeg - 5 * (math.floor(posNeg / 5))
			if edx > 24 :
				edx = edx - 24
			if edx < 0 :
				edx = edx + 24
			edx = int(edx)
			eletr = indeks[edx]
			if eletr == plaintext[pos] :
				eletr = plaintext[pos - 1]
			ciphertext += eletr
	print ciphertext
	return ciphertext

codeword = raw_input("Enter a codeword: ")
key = phormat(codeword)

message = raw_input("Enter some text to encrypt or decrypt: ")
plaintext = phormat(message)

encrypt(plaintext, indexus(key))