
#create a function that takes number as an argument 
def factorial(number):
    if number == 0: #check if the the number == 0 
        #return 1(factorial of 0 == 1)
        return 1
    else:
        #else return the number multiplied be each number below it 
        return number * factorial(number - 1)
    
number = int(input('Enter a number: '))#ask user for input that is an integer 

print(factorial(number))


