# Crypt

shift = 3 # defining the shift count

text = "BEZI LISKA K TABORU"

encryption = ""

for c in text:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the shift
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character

    else:

        # since character is not uppercase, leave it as it is
        encryption += c
        
print("Plain text:",text)

print("Encrypted text:",encryption)

# Decrypt

shift = 3 # defining the shift count

encrypted_text = "EHCL OLVND N WDERUX"

plain_text = ""

for c in encrypted_text:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the negative shift
        new_index = (c_index - shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to plain string
        plain_text = plain_text + new_character

    else:

        # since character is not uppercase, leave it as it is
        plain_text += c

print("Encrypted text:",encrypted_text)

print("Decrypted text:",plain_text)

# Vigenere cypher

def vigenere_cipher(text, keys, decrypt=False):

    # vigenere cipher for lowercase letters
    n = len(keys)

    translatedText =""

    i = 0 #used to record the count of lowercase characters processed so far

    # iterate over each character in the text
    for c in text:

        #translate only if c is lowercase
        if c.islower():

            shift = keys[i%n] #decide which key is to be used

            if decrypt == True:

                # if decryption is to be performed, make the key negative
                shift = -shift

            # Perform the shift operation
            shifted_c = chr((ord(c) - ord('a') + shift)%26 + ord('a'))

            translatedText += shifted_c

            i += 1

        else:

            translatedText += c
            
    return translatedText

    text = "we will call the first manned moon mission the Project Apollo"

encrypted_text = vigenere_cipher(text, [1,2,3])

print("Plain text:\n", text)

print("Encrypted text:\n", encrypted_text)