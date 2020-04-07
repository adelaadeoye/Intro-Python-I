
number = int(input("Enter a Number"))


def PrimeNumber(number):
    count= 0
    if (number==1):
        print("The number is not a prime")
    else:
        for i in range(number):
            if(number%2==0):
                count+=1

        if(count>2):
            print("The number is not a prime")
        else:
            print("The number is a prime")

PrimeNumber(number)