from ctypes import pointer
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
#input
encrypt_input = ""

def main():
    encrypt_input = input("Enter your encrypted text: ")
    encrypt_input = encrypt_input.split(" ")
    
    #build the dictionary
    make_dictionary()
    #solve encrypted text
    possible_solutions(encrypt_input)

    # for key, value in map_by_length.items():
    #     print(key, " : ", value)
def update_map(decode, input_text, possible_text):
    input_array = list(input_text)
    possible_array = list(possible_text)
    possible_encode = True

    for i in input_array:
        if ((decode.get(i) == "!") and (decode not in possible_array[i])):
            decode.replace(i, possible_array[i])
        elif ((decode.get(i) != possible_array[i])):
            possible_encode = False
            break
    return possible_encode

def decoding():
    character_map = dict()
    for c in alphabet:
        character_map[c] = '!'
    return character_map

def solve_decrypt(text, decoded_str, decode, index):
    matching = False

    if (len(encrypt_input) == len(decoded_str)):
        decrypted_str.append(decoded_str)
        matching = True
    else:
        same_length = map_by_length.get(len(text.get(index)))
        for same in same_length:
            new_decode = decoding()
            new_decode.update(decode)

            if(update_map(new_decode, text.get(index), same)):
                update_decrypted_str = decrypted_str + " " + same
                solve_decrypt(text, update_decrypted_str, new_decode, index+1)
    return matching


def possible_solutions(text):
    current_length_list = map_by_length.get(len(text[0]));
    for t in current_length_list:
        decode = decoding()
        if(update_map(decode, text[0], t)):
            solve_decrypt(text, t, decode, 1)

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