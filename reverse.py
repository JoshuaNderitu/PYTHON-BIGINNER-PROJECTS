#Write a Python program to reverse a string.
#create a function that take an argument 
def string_reverse(word):
    reversed = '' #initialize an empty string for the reversed string 

    index = len(word) #assign a variable index the length of the string

    while index > 0: #initialize a while loop to check when the index drops to 0

        reversed += word[index - 1] # add letters from the word string 

        index -= 1 #decrement the index after each iteration

    return reversed #return the reversed string 

print(string_reverse('1234abcd')) # print the reversed sring

    