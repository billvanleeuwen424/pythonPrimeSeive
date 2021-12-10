import math


#this function requires a current list of prime numbers, will return a list of non-prime numbers
def createDivisorList(limit, primeList):

    divisorList = []

    #get a number
    for i in range(2, limit):
        flag = False 

        #check if divisible by prime
        for j in primeList:
            if ((i % j) == 0):
                flag = True
                break
        
        if(flag == False):
            divisorList.append(i)

    return divisorList
            

#def checkIfPrime(number, primeList):


def sieve(limit):

    
    primeList = [2]

    numList = createDivisorList(limit, primeList)

    while(len(numList) > 0):
        nextNum = numList[0]

        primeFlag = True
        #only go up to the sqrt of the number, rounded up
        for i in range(2,math.ceil(math.sqrt(nextNum))):

            # if this is triggered, the number is evenly divisible, and is not considered prime
            if(nextNum % i == 0):
                primeFlag = False
                break

        if(primeFlag):
            primeList.append(nextNum)
            numList = createDivisorList(limit,primeList)


    return primeList
        

def main():
    print("this program will output all prime numbers up to the number entered below:")
    limit = input()
    limit = int(limit)
    primeList = sieve(limit)

    print(primeList)


if __name__ == "__main__":
    main()