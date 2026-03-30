#Task Description:

#One of the earliest encryption systems is attributed to Julius Caesar and the Caesar
#Cipher. If the letter to be encrypted is the N-th letter in the alphabet, replace it with
#the (N + K)-th where K is some fixed integer (Caesar used K = 3). We usually treat a 
#space as zero and all arithmetic is then done modulo 27. Thus for K = 1 the message 
#ATTACK AT DAWN becomes BUUBDLABUAEBXO.

#Decrypting such a message is trivial since one only needs to try 26 different values of 
#K. This process is aided by knowledge of the language, since then one can determine when
#the decrypted text froms recognisable words.

#If one does not know the language, then a dictionary would be necessary. Write a program 
#that will read in a dictionary and some encrypted text, determine the value of K that was
#used, and then decrypt the ciphertext to produce the original message.

#The original message contained only letters and spaces has been encrpyted using the above
#method. The most suitable value of K will be the one which produces the most matches with
#the words in the dictionary.

#The signature of your function should be:

#def solve(incoming: str) -> int

#You may implement other functions called by your solve function if you wish.

#Input Spec

#Input will consist of a dictionary and the encrypted text. The dictionary will consist of
#no more than 100 lines each containing a word in uppercase characters and not more than
#20 characters in length.

#The dictionary portion will be terminated by a line consisting of a single '#'. The
#encrypted text will follow immediately and will consist of a single line of uppercase
#text (and space characters) containing no more than 250 characters.

#Note that the dictionary will not necessarily contain all the words in the original text,
#although it will certainly contain a large portion of them. It may also contain words
#that are not in the original text.

#The dictionary will not appear in any particular order.

#Output Spec

#Output will consist of the rotation needed to decode the message, expressed in integer
#form.

#Sample Input & Output

#An input of:

#THIS
#DAWN
#THAT
#THE
#ZORRO
#OTHER
#AT
#THING
##
#BUUBDLA PSSPABUAEBXO

#Should yield the output:

#26

def solve(words: list[str], cipher: str) -> int:

    K = 26
    max_matches = 0   # or 0
    best_K = 0

    # Map character to number: A=1, ..., Z=26, space=0
    def char_to_num(c):
        if c == " ":
            return 0
        return ord(c) - ord("A") + 1

    # Map number back to character, modulo 27
    def num_to_char(n):
        n %= 27          # wrap around 0-26
        if n == 0:
            return " "
        return chr(n - 1 + ord("A"))

    for n in range(1, K + 1):
        shifted = "".join(num_to_char(char_to_num(c) + n) for c in cipher)
        print(f"K={n}: {shifted}")
        
        shifted_words = shifted.split()
        
        matches = sum(1 for w in shifted_words if w in words)
        
        print(f"K={n}: {shifted} → Matches: {matches}")
        
        if matches > max_matches:
            max_matches = matches
            best_K = n
            
    print(f"\nBest K: {best_K} with {max_matches} matches")
        
        
if __name__ == "__main__":
    
    words = []
    
    while True:
        
        user_input = input()
        
        if user_input == "#":
            break
        
        words.append(user_input)
        
    print(words)
    
    cipher_input = input()
    
    s = solve(words, cipher_input)
    
    #print(s)