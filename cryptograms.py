import sys

#open file in dictionary
filename = 'dictionary.txt'
file_open = open(filename)
dictionary = file_open.read().split('\n')
file_open.close()

#map by length dictionary
map_by_length = dict()
#decrypted string list
decrypted_str = []
#alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

def main():
    encrypt_input = input("Enter your encrypted text: ")
    print(encrypt_input.split(" "))


if __name__ == '__main__':
    main()