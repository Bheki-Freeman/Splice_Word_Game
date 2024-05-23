import re
import random

pure_alphabets = []
random_alphabets = []

for letter in range(ord('a'), ord('z')+1): 
    pure_alphabets.append(chr(letter)) # I just have to create alphabets first

for word in range(0,len(pure_alphabets)):
    wordl = random.sample(pure_alphabets,1)
    random_alphabets.append(''.join(wordl)) # Then I can randomize them
    

lst = [] # I need an emply list to append to

def add_list(lst, random_alphabets) -> None: # add list into  list
    for item in range(4):
        rand_value = random.randint(0, len(random_alphabets))
        ps = rand_value
        if ps > 23:
            continue
        psx = ps + 5
        lst.append(random_alphabets[ps:psx:1])
    

add_list(lst, random_alphabets) #Add The lists

def empty_list(lst): # To clear elements from the list
    lst.clear()
    

def create_list() -> None:
    while len(lst) < 3: # Just to make sure that we have a 4 elements list (the main one)
        empty_list(lst)
        add_list(lst, random_alphabets)