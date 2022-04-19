import sys

#open file in dictionary
filename = 'dictionary.txt'
file_open = open(filename)
dictionary = file_open.read().split('\n')
file_open.close()

#map by length dictionary
map_by_length = dict()
#alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
#input
#encrypt_input = ""
#all solutions found?
finished = False

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

def backtrack(a, k, input):
    c = []
    num_c = 0
    counter = 0

    if(is_solution(a, k, input)):
        process_solutions(a, k, input)
    else:
        k += 1
        construct_c(a, k, input, c, num_c)
        for counter in num_c:
            a[k] = c[counter]
            backtrack(a, k, input)
            if finished:
                break

def is_solution(a, k, input):
    pass
def construct_c(a, k, input, c, num_c):
    pass
def process_solutions(a, k):
    pass

if __name__ == '__main__':
    main()