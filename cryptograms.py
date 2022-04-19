# import sys

#open file in dictionary
filename = 'dictionary.txt'
file_open = open(filename)
dictionary = file_open.read().split('\n')
file_open.close()

encrypt_input = ""

import sys
from pathlib import Path

def is_good_cipher(decoded, encoded):
    """Check if the decoded string is valid.
    Create a map for each indexed position. A valid decoding must be a one-to-one mapping.
    """
    cipher_map = {}
    for (enc, dec) in zip(encoded, decoded):
        if enc not in cipher_map:
            cipher_map[enc] = dec
        elif cipher_map[enc] != dec:
            return False
    if len(set(decoded)) != len(set(encoded)):
        return False
    return True

def backtracking(full_dict, possible_words, user_encrypted, index, final):
    #backtracking based on Silber slides [ppt L21]
    final = []
    for word in full_dict[len(user_encrypted[index])]:
        encoded = " ".join(user_encrypted[: index + 1])
        decoded = " ".join(possible_words + [word])
        if is_good_cipher(encoded, decoded):
            if index + 1 == len(user_encrypted):
                final.append(decoded)
            else:
                final.extend(backtracking(full_dict, possible_words + [word], user_encrypted, index+1, final))
    return final

def make_dictionary():
    map_by_length = {}
    for d in dictionary:
        key = len(d)
        if key in map_by_length:
            map_by_length.get(key).append(d)
        else:
            new_list = []
            new_list.append(d)
            map_by_length[key] = new_list
    return map_by_length

def main():
    # Make dictionary
    new_dictionary = make_dictionary()
    #user encrypted text input
    encrypt_input = input("Enter your encrypted text: ")
    encrypt_input = encrypt_input.split(" ")
    #start sub solving
    results = backtracking(new_dictionary, [], encrypt_input, 0, [])
    
    #print the results
    print(len(results))
    for res in results:
        print(res)


if __name__ == "__main__":
    main()