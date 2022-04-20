import sys

#open file in dictionary
filename = 'dictionary.txt'
file_open = open(filename)
dictionary = file_open.read().split('\n')
file_open.close()

encrypt_input = ""

def decrypt(input):
    new_dictionary = make_dictionary()
    for d in new_dictionary:
        attemptUpper = decrypt(d.upper())
        attemptLower = decrypt(d.lower())
        if attemptUpper == 1:
            input('The password is: ' + d.upper())
            break
        if attemptLower == 1:
            input('The password is: ' + d.lower())
            break
        attempts+=2
        if (attempts/1000).is_integer():
            print('Please be patient, human. I have tried ' + str(attempts) + ' passwords.')

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
    
    #user encrypted text input
    encrypt_input = input("Enter your encrypted text: ")
    encrypt_input = encrypt_input.split(" ")

    final = decrypt(encrypt_input)
    
    #print the results
    print(len(final))
    for s in final:
        print(s)


if __name__ == "__main__":
    main()