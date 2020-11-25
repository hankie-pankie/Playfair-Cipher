	import java.util.Scanner;

public class PlayUnfair {
	
	final static String alphabet = "abcdefghijklmnopqrstuvwxy";
	public static String index = "";
	
	public static void main(String[] args) {
		//creates input scanner
		Scanner input = new Scanner(System.in);
		
		System.out.println("enter a codeword");
		
		String codeword = input.nextLine();
		//some formatting for codeword. I also need to replace repeated letters in codeword with ""
		codeword = codeword.toLowerCase();
		codeword = codeword.replaceAll("\\s+", "")
		codeword = codeword.replaceAll("z", "x")
		//creates the encryption index
		index(codeword);
		
		System.out.println("Enter some text to encrypt or decrypt");
		
		//establishes input as string.
		String plaintext = input.nextLine();
		
		//some formatting for the plaintext
		plaintext = plaintext.replaceAll("\\s+", "");
		plaintext = plaintext.toLowerCase();
		plaintext = plaintext.replaceAll("z", "x");
		
		//function to ensure even number of letters in plaintext
				if(plaintext.length() % 2 == 1) {
					plaintext = plaintext + "x";
				}
				
		//encrypts string!
		String ciphertext = encrypt(plaintext);
		//prints string
		System.out.println(ciphertext);
		input.close();
	}
	
	//code index method
	public static String index(String codeword) {
		index = alphabet;
		for(int i = 0; i < codeword.length(); i++) {
			
			index = index.replaceAll(String.valueOf(codeword.charAt(i)), "");
		}
		index = codeword + index;
		return index;
	}
	
	//encryption method. also decryption because they are the same function
	public static String encrypt(String plaintext) {
		//makes nil string that we can add letters to later
		String ciphertext = "";
		//for loop to move through letters of the string
		for(int i = 0; i < plaintext.length(); i++) {
			//we need 3 positions to encrypt: the position at the letter; if even, then position after the letter; if odd, then position before the letter.
			double pos = index.indexOf(plaintext.charAt(i));	
		
			//separates into even and odd somehow
			if(i % 2 == 0) { //element of even
				double posPlus = index.indexOf(plaintext.charAt(i + 1));
				//encryption formula for even!
				double encPos = 5 * (Math.floor(pos / 5)) + posPlus - 5 * (Math.floor(posPlus / 5));
				if(encPos > 24) {
					encPos = encPos - 24;
				}
				if(encPos < 0) {
					encPos = encPos + 24;
				}
				//makes character from position
				char echar = index.charAt((int) encPos);
				
				//need to switch the letter if it's the same as before
				//there's a math glitch if the letters are in the same column
				if(echar == plaintext.charAt(i)){
					echar = plaintext.charAt(i + 1);
					
				}
				//adds encrypted letter to ciphertext
				ciphertext += echar;
			}
			
			else{
				int posNeg = index.indexOf(plaintext.charAt(i - 1));
				//encryption formula for odd!
				double encPos = 5 * (Math.floor(pos / 5)) + posNeg - 5 * (Math.floor(posNeg / 5));
				if(encPos > 24) {
					encPos = encPos - 24;
				}
				if(encPos < 0) {
					encPos = encPos + 24;
				}
				//makes character out of position
				char echar = index.charAt((int) encPos);
				//adds encrypted letter to ciphertext
				
				//same switch for letters in same column
				if(echar == plaintext.charAt(i)){
					echar = plaintext.charAt(i - 1);
					
				}
				ciphertext += echar;
			}
		}
		return ciphertext;
	}
}