'''for i in range (1,6):
    for j in range(1,11):
        print(f"{i} * {j}={i*j}")'''
#problem
'''n= 10
for i in range(0,n):
    if n-i==5:
        print("Stop the shairng of candies00")
        continue
    print("Giev candie to forend")'''
#problem
'''n= 5
for i in range (1,n+1):
    print(i)'''
#probrem
'''n=5
i=1
sum = 0
while i<=n:
    sum+=i
    i+=1
print(sum)'''
#prbeln
'''n=10
i=1
sum=0
while i<=10:
    if i%2==0:
        sum+=i
    i+=1
print(sum)'''
#problem
'''n=3
i=1
while i<=10:
    print(f"{n} * {i} = {n*i}")
    i+=1'''
#using for loop
'''n=3
for i in range (1,11):
    print(f"{n} * {i} = {n*i}")'''
#problem Factorial
'''n=5
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1

print(fact)'''
'''n=5
fact =1 
for i in range (1,n+1):
    fact = fact*i
    print(fact)'''
#problem Reverse a number
'''n=1234
rev =0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)'''

'''n=6745
m=str(n)
k=len(m)
for i in range(k-1,-1,-2):
    print(m[i],end="")'''
#Sum of theh digits of a number
'''n=123
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)'''
#for Loop
'''n= 695
s=str(n)
sum=0
for i in range (0,3):
    l=int(s[i])
    sum=sum+l
print(sum)'''
#Palindrome for a number in loops
'''n=1234321
rev=0
k=n
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
if (k==rev):
    print("PAlindrome")
else:
    print("Not a Palindrome")'''
#using for loop
'''n=1234329
s=str(n)
k=len(s)
rev=""
for i in range (k-1,-1,-1):
   rev=rev+s[i]
print (rev)

if (n==int(rev)):
    print("PAlindrome")
else:
    print("Not a Palindrome")'''
#problrm on counting the no of digits
'''2345
count=0
while n!=0:
    n=n//10
    count+=1

print(count)'''
#for loop
'''2345
s=str(n)
count=0
for i in s:
    count+=1
print(count)'''
#problem for fibonacci series
'''x,y=0,1
n=10
i=1
print(x,y)
while i<=n:
    sum= x+y
    print(sum,end=" ")
    x=y
    y=sum
    i=i+1'''

#for loop
'''x,y=0,1
sum=0
print(x,y,end=" ")
for i in range (0,10):
    sum=x+y
    print(sum,end=" ")
    x=y
    y=sum'''
#power of number using loops
'''n=3
i=1
while i<=4:
    print(f"{n} power {i} = {n**i}")
    i+=1'''
#for loop
'''n=3
for i in range (1,4):
    print(f"{n} power {i} = {n**i}")'''
#sum of natural number upto limit
'''n=10
m=20
i = n
sum = 0
while i <= m:
    print(i, end=" ")
    sum += i
    i += 1
print("\nTotal:", sum)'''
#for loop
'''n=int(input())
m=int(input())
sum=0
for i in range (n,m+1):
    sum=sum+i
print(sum)'''
#problem factors of a number
'''n=16
i=1
count=0
while i<=n:
    if (n%i==0):
        print(i,end=" ")
        count+=1
       
    i=i+1
print(f"\n{count}")'''
# for loop
'''n=30
count=0
for i in range(1,n+1):
    if (n%i==0):
        print(i,end=" ")
        count+=1
print(f"\n{count}")'''

