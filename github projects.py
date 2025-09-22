#to find factors of a given number
n=int(input("enter number"))
for i in range(2,n):
    if n%i==0:
        print("the factors of",n,"are",i)
    else:
        pass