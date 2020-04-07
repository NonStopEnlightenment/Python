def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
    else:
        return True

primelst=filter(isPrime, range(2,30))
print ('Prime numbers between 1-10:', list(primelst))
