#Write a python funcion to find the maximum of three numbers

#find the maximum of two number first
def max_of_two(x,y):
    #check if x is greater than y
    if x > y:
        return x
    #return y if it is greater
    return y

#check the max of the three
def max_of_three(x,y,z):
    #call the max_of_two function to check y and z 
    #then check between x and z
    return max_of_two(x, max_of_two(y,z))



#call the max_of_three function
print(max_of_three(3, -6, 5))