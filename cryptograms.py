import sys

#open file in dictionary
filename = 'dictionary.txt'
file_open = open(filename)
dictionary = file_open.read().split('\n')
file_open.close()

encrypt_input = ""

def simple_sub_checker(encrypt_str, decrypt_str):
    sub_dict = {}
    for (e, d) in zip(encrypt_str, decrypt_str):
        if e not in sub_dict:
            sub_dict[e] = d
        if sub_dict[e] != d:
            return False
    e_len = len(set(encrypt_str))
    d_len = len(set(decrypt_str))
    if e_len != d_len:
        return False
    return True

#backtracking based on Silber slides [ppt L21]
def backtracking(full_dict, possible_words, user_encrypted, index, final):
    final = []
    for value in full_dict[len(user_encrypted[index])]:
        encrypt_str = " ".join(user_encrypted[:index + 1])
        decrypt_str = " ".join(possible_words + [value])
        #candidates
        if simple_sub_checker(encrypt_str, decrypt_str):
            if (index + 1 == len(user_encrypted)):
                final.append(decrypt_str)
            else:
                #recure
                final.extend(backtracking(full_dict, possible_words + [value], user_encrypted, index + 1, final))
    return final

#create a dictionary sorted by length 
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
    candidates = []
    solutions = backtracking(new_dictionary, candidates, encrypt_input, 0, [])
    
    #print the results
    print(len(solutions))
    for s in solutions:
        print(s)


if __name__ == "__main__":
    main()