
def backwardslist(array):
    """ Takes in a list and returns the list backwards"""
    x = len(array)
    backlist = []
    while x > 0:
        backlist.append(array[x-1])
        x-=1
    return backlist

def min(array):
    """ Returns the lowest number in an list of numbers"""
    x = array[-1]
    for i in array:
        if i < x:
            x = i
    return x


def firsthalfsum(array):
    """Returns the sum of the first half of the list.
        ***IF THE LIST HAS AN ODD NUMBER OF ELEMENTS, split the middle element in
        half and add it to the sum.
        """
    sum = 0
    if len(array)%2 == 0:
        for i in range(int(len(array)/2)):
            sum+=array[i]
    else:
        for i in range(int(len(array)/2)):
            sum+=array[i]
        sum+=(array[int(len(array)/2)+1])/2
    return sum


def divisibleby(array, divisor):
    """ Returns each element divisible by the paramater 'divisor'

    """

def max(array):
    """ Returns the highest number in a list of numbers """

def avg(array):
    """ Returns the average of a list of numbers"""

def suprise():
    """ Create a surprise function for the person that receives your code.
        Feel free to get creative change parameters, print out shapes,  etc.

        """


################################
####    BONUS FUNCTION       ###
################################
def gcd(array):
    """ Returns the greatest common Divisor of a list of numbers """
    """ Greatest Common Divisor is the greatest number that each number in the list is 
        divisible by. 
        EXAMPLE: [500, 50, 20] Greatest Common Divisor = 10
                 [18, 30, 42]  Greatest Common Divisor = 6
                 [33, 66, 99, 101] Greatest Common Divisor = 1
                 
                 """


