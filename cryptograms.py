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
    # encrypt_input = input("Enter your encrypted text: ")
    # encrypt_input = encrypt_input.split(" ")

    #build the dictionary
    make_dictionary()
    for key, value in map_by_length.items():
        print(key, " : ", value)

#dictionary to search by length
def make_dictionary():
    for d in dictionary:
        key = len(d)
        if key in map_by_length:
            map_by_length.get(key).append(d)
        else:
            new_list = []
            new_list.append(d)
            map_by_length[key] = new_list


if __name__ == '__main__':
    main()