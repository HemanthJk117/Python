#SLICING
'''name = "MICHAEL JACKSON"
print(name[0:7:2])''' #out put MCAL
#STRING CONCATENATION (AdDing the two words

'''name = "HEmanth"
last_name = "Kumar"
full_name = name + " " +last_name
print(full_name)'''
# STRING LENGTH
'''name = "Hemanth"
print(len(name ))'''
#String Metgods
s = "ello world"

'''print(s.upper())
print(s.lower())
print(s.replace("l","d")) 
print("MANAGEMENT".count("A"))'''
'''print(s.capitalize())'''# first character to captial 
'''print(s.title())''' #both are same
'''print(s.strip('e'))''' # rempve elemnets in left or right ending point
'''print(s.endswith("ld"))''' # it will check the ld is last or not
'''print(s.split('o'))'''#splits into each word
'''print('w'.join(s))'''
#problem on vowels count
'''s = input()
s=s.lower()
a=s.count('a')
e=s.count('e')
i=s.count('i')
o=s.count('o')
u=s.count('u')
print(f"Number of vowels: {a+e+i+o+u}")'''
# problem on gradesq and marks and avg
'''s = int(input("MArks 1: "))
p = int(input("MArks 2: "))
m = int(input("MArks 3: "))
total = s+p+m

avg = total/3
print(total)
print(avg)
if avg >=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
else:
    print("fail")'''
# Palindrome
'''n = input("Enter the name: ")
k = n[::-1]
if n==k:
    print("Palindrome")
else:
    print("Not a palindrome")'''
#LArgest Numebr among three
'''a= input()
x,y,z = a.split(",")
if x>y:
    if x>z:
        large = x
    else:
        large = z
elif y>x:
    if y>z:
        large= y
        
    else:
        large = z
elif z>x:
    if z>y:
        large = z
    else:
        large = y

print(large)'''
# leap year
'''year = int(input("Enetr the year: "))
leap = False
if year %100==0 and year%400!=0:

    leap = False
elif year%4==0:
    leap = True
else:
    leap = False
print(leap)'''
# Problem no of words
'''n = "Count the number of occurrences of a character in a string."
words = n.split(" ")
print(len(words))'''
#problem the number of times occurance
'''n=" Let me know if you want a quick demo of the difference between "
print(n.count("e"))    '''
# how many sentences in the string
'''n = "Hemanth Kumar"
sentences = n.split(" ")
print((sentences))'''
