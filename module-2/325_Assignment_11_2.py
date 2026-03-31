#|Maddison Montijo | 3.13.2026 | 11.2 Assignment

#|The Purpose of this Program is to :
#|1. Create a program with a recursive function that accepts an integer argument, n, and prints the number of 1 up to and including n. Then, write a non-recursive method that takes an integer argument, n, and prints the number of 1 up to and including n.

#|2.In your code documentation include an explanation of each functions approach to solving the problem.
#|3.Include test code that will not allow a negative or 0 value.
#|4.In your display, include which function is being invoked at both the start and end of the output.

#| Recursion function
def recursive(n):
#| Base case
#| If n is 1, print 1
    if n == 1:
        print(n)
    else:
        print(n)
        #| Recursive call
        #| If n is greater than 1, call the function again with n-1
        recursive(n-1)



#| Iterative function
def iterative(n):
    #| For loop
    #| Print the numbers from 1 to n
    
    for i in range(1,n+1):
        print(i)


#| Function to get a positive integer
#| Prompt the user to enter a positive integer
def get_positive_int():
    #| While loop
    #| Keep prompting the user until they enter a positive integer
    while True:
        try:
            #| Try to convert the input to an integer
            #| If successful, return the integer
            n = int(input("Enter a positive integer: "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

#| Main function
#| Call the recursive and iterative functions
def main():
    #| Get a positive integer
    n = get_positive_int()
    print("Recursive:")
    recursive(n)

    #| Get a positive integer
    print("\nIterative:")
    iterative(n)
              
#| Call the main function
if __name__ == "__main__":
    main()