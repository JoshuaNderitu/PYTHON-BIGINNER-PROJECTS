#Write a Python function to sum all the numbers in a list.


#define a function with parameter numbers
def sum_of_list(num_list):
    sum = 0 #initialize the sum to zero
    for i in num_list: #use a for loop to iterate the list 
        #add each to the sum 
        sum += i
    
    return sum
    
print(sum_of_list([8,2,5,3,2])) #print the sum