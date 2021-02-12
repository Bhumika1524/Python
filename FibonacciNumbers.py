#Program to print Fibonacci Numbers Without Recursion 
n=int(input("Enter the value of 'n': "))
#first two terms are first and second
first=0
second=1
sum=0
count=1
print("Fibonacci Sequence: ")
# Count should not be more then n.
while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second	

#Program to generate Fibonacci sequence recursively 
def Fibonacci(Number):
    if(Number==0):
        return 0
    elif(Number==1):
        return 1
    else:
        return (Fibonacci(Number-2)+Fibonacci(Number-1)) #return the sum of two prevous terms
n=int(input("Enter the value of 'n': "))
print("Fibonacci Sequence:")
for n in range(0, n):
  print(Fibonacci(n))
