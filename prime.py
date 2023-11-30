# A school method based Python3 program
# to check if a number is prime
 
 
# import sqrt from math module
from math import sqrt
 
 
 
# Function check whether a number
# is prime or not
def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True
 
 
# Driver Code
if __name__ == '__main__':
    if isPrime(11):
        print("true")
    else:
        print("false")
 
