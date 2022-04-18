import sys

encrypt_input = input("Enter your encrypted text: ")

for i in range(26):
    word = ''
    for j in range(len(encrypt_input)):
        extract = ord(encrypt_input[j]) - 97
        decrypt_value = ((extract - i) % 26) + 97
        word += chr(decrypt_value)
    if w in word:
        print("Decrypt Word is:", word)
        print("The key is:", i)
 