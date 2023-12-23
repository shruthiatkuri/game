"""num=4
print(id(4))
x=2
x=x+3
x+=2
print(x)
while x<20:
    x+=2
    print(x)
a,b=5,6
print(a)
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(bin(25))
print(0b0101)

a=5
b=6
'''temp=a
a=b
b=temp'''
a=a+b
b=a-b
a=a-b
print(a)
print(b)
"""
"""print(~12)
print(bin(12))
print(12 & 13)
print (12| 13)
print(25&30)
print(bin(25))
print(bin(30))
print(bin(24))
print(12^13)"""

"""print(25^30)
print(bin(25))
print(bin(30))
print(bin(7))
print(10<<2)
import math
x=math.sqrt(25)
print(x)
print(math.pow(3,2))
print(math.pi)"""


"""if True:
    print("Im right")"""


"""if False:
    print("Im right")
print("Bye")"""


"""x=int(input("Enter a number: "))
y=x%2
if y==0:
    print(+x," is even number")
if y!=0:
    print(+x," is odd number")"""


"""x=int(input("Enter a number: "))
y=x%2
if y==0:
    print(x," is even")
else:
    print(x," is odd")
print("Bye")"""
      


"""x=int(input("Enter a number: "))
y=x%2
z=5
if y==0:
    print(+x," is even")
    if (x>z):
        print(+x,"is greater than ",+z)
    else:
        print(+x,"is smaller than",+z)
else:
    print(+x," is odd")
print("Bye")"""



"""x=61
if x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
elif x==4:
    print("Four")
else:
    print("Wrong input!!")"""



"""i= 0
while i<=5:
    print("HI")
    i=i+1
"""


"""I=5
while I>=1:
    print("Hello", I)
    I=I-3"""
      



"""i=1
j=1
while i<=5:
    print("Hello ", end="")
    j=1
    while j<=1:
        print("Hey", end="")
        j=j+1
    i=i+1
    print()"""


"""#x=["shruthi","6","7.8"]
x='shruthi'
#for i in x:
#for i in [1,4,"good"]:
#for i in range(10):
for i in range(10,20,2): 
    print(i)"""

"""av=5
x=int(input("Enter a number: "))
i=1
while i<=x:
    if i>av:
        print("Out of stock")
        break
    print("candy")
    i+=1

print("Bye")"""


"""for i in range(1,100):
    if i%3!=0 and i%5!=0:
        print(i)"""


"""for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    print(i)

print("Bye")"""


"""for i in range(5):
    if(i==3):
        continue
    print("Hello",i)"""

"""for i in range(5):
    if(i==3):
        break
    print("Hello",i)"""


"""for i in range(5):
    if(i==3):
        pass
    print("Hello",i)
"""


"""for i in range(4):
    for i in range(4):

        print("# ",end="") 
    print()"""


"""for i in range(4):
    for j in range(i+1):
        print("#",end="")
    print()"""



"""for i in range(4):
    for j in range(4-i):
        print("#",end="")
        i-=1
    print()"""



"""num=[10,16,22,27,36,43]
for i in num:
    if i%5==0:
        print(i)
        break
else:
    print("Not found")"""



"""x=int(input("Enter a number: "))
for i in range(2,x):
    if x% i==0:
        print(x,"is not aprime number")
else:
    print(x,"is prime number")"""


"""def greet():
    print("Helllo")
    print("Good Morning")

greet()
"""

"""def add(x,y):
    a=x+y
    return a
    #print(a)
result=add(3,4)
print(result)"""



"""def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b
result1, results2=add_sub(3,4)
print(result1, results2)
"""

"""def person(name,age=18):
    print(name)
    print(age)
person('shruthi',23)"""



"""def sum(*b):
    #c=a
    c=0
    #print(c)
    #print(b)
    for i in b:
        c=c+i
        print(c)
sum(5,6,34,78)"""



"""def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person("shruthi",age=23,city='hyd',cell=998667658)"""


"""a=10
def sum():
    a=15
    print(a)


print(a)
sum()
"""



#list=[2,5,8,19,16,28,60]
"""def numbers(list):
    for i in list:
        if i%2==0:
            print(i,"is even number")
        else:
            print(i,"is odd number")
print("Done")

numbers([2,5,8,19,16,28,60])"""



""""def even_odd(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    #return even, odd
    print(even)
    print(odd)
list=[2,5,78,98,23,14]
even_odd(list)
print(even)
print(odd)"""



#FIBONACCI SERIES

"""def fibonacci(n):
    first=0
    second=1
    print(first)
    print(second)
    if n<0:
        print("Invalid")
    else:    
        for i in range(0,n):
            series=first+second
            first=second
            second=series
            if series<100:
                print(series)
fibonacci(200)
"""


#FACTORIAL NUMBER
"""def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
f=fact(5)
print(f)"""


"""a="Hello world!!"
print("H"in a)
print(len(a))   
print(a[2:5])"""     



"""fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
 """


"""fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp)"""

        

"""fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)"""


"""fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)"""



"""fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('From:')==-1: 	continue
    print(line)"""


"""fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
"""



"""fname=input("Enter file name: ")
fhand=open(fname,'r')
#count=0
for line in fhand:
    print(line.upper())
    #count+=1"""



"""fname=input("Enter a file name: ")
fhand=open(fname,'r')
count=0
total=0
for line in fhand:
    if line.startswith("X-DSPAM_Confidence:"):
        space_index=line.find(" ")
        my_num=float(line[space_index+1:])
        #print(my_num)
        total +=my_num
        count +=1
print(total/count)"""



"""filename=input("Enter filename: ")
fhand=open(filename,'r')
count=0
for line in fhand:
    count+=1
    print(count, "are subjevt in file")"""


"""filename=input("enter s file name: ")
if filename=="na na boo boo":
    print("NA NA BOO BOO TO YOU - YOU HAVE BEEN PUNK'D!")
#fhand=open(filename,"r")"""




"""num =121
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")"""


"""def anagrams(a,b):
    if len(a)!=len(b):
        print("False")
    else:
        x=sorted(a)
        y=sorted(b)
        if x==y:
            print("Anagrams")
        else:
            print("not anagrams")

anagrams("list","still")
"""




#coursera
"""print("hELLO WORLD!!")

# This is acomment line you cn represent by # symbol in python

#variables
age=20
sentence="My name is shruthi"

print(age)
print(sentence)


#Assigning multible values to multible variables

ram,sam,jam=20,23,22 
print(sam)

# All variables holding same value

John=Ram=Bob=17
print(Ram)

name, age= "shruthi",22
print(name,age)

#Arithmetic Operations and Strings

age1 =12
age2 =18

print(age1+age2)
print(age1-age2)
print(age1*age2)
print(age1/age2)
print(age1%age2) # REmainder like 0


# Strings
sent1="today is abeautiful day"
print(sent1)

first_name="shruthi"
last_name="atkuri"
print(first_name+" "+last_name)
print(first_name[0])
print(first_name[0:4])

a="shruthi"
age=23
sentence= "My name is %s and %d years old" 
print(sentence %(a, age))
print(f"Hello {a}")

x=int(input("Enter the x value:"))
y=int(input("Enter the y value: "))
a=x+y
b=x-y
c=x/y
d=x%y
print(a, b,c,d)

name="shruthi"
print(name)
"""


"""sweet, spicy, healthy= "jalebi","chicken","kimchi"
print(sweet, spicy, healthy)


print("\nHell0"*10)

name, age= "shruthi", 23
print(name, age)

s="shruthi"
print(s[1:])


#LIst
shopping_list= ['apples','banana','oranges','cheese']
print(shopping_list)
print(shopping_list[0])

# add items o list
shopping_list.append('blueberries')
print(shopping_list)

#update an item
shopping_list[0]='cherries'
print(shopping_list)

#delete item from list

del shopping_list[2]
print(shopping_list)

#Adding two strings
shopping_list_2=['bread','jam','peanut butter']
print(shopping_list_2)
print(shopping_list+shopping_list_2)
print(shopping_list*2)

#CALLING min and max functions

list_num=[7,87,54,0,43,4]
print(max(list_num))
print(min(list_num))


#Exercises

print((15+30)/2)

a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

name="shruthi"
print(name)

a,b,c='pizza','pie','pudding'
print(b)

print("\nhello"*10)

name, age="shruthi",23
print("My name is ",name, age)

sen1= "Hi there"
sen2= "How are you doing?"
print(sen1+" "+sen2)

sen1="I love pizza"
print(sen1[3])

sen1="I still love pizza"
print(sen1[0:6])

sen1="pizza is love. Pizza is life"
print(sen1[1:])
"""







#Dictonaries

"""students={'bob':12,'rachel':13,'emily':15}
print(students)
print(students['rachel'])
print(students['bob'])

#update
students['rachel']=14
print(students)

#deleting element

del students["emily"]
print(students)
print(len(students))"""


#Tuple

"""tup=("oranges","apples","bananas")
#tup[0]="cherries"
#tup.append("cherries")
print(tup)
tup2=(12,14)
tup3=tup+tup2
print(tup3)"""



# Conditional statements

"""if 5==3:
    print("hello")
else:
    print("OK")

age=18
if age<=13:
    print("you are a child")
elif age>=13 and age<=18:
    print("You are a teenager ")
else:
    print("YOur are an adult")
"""

#Loops

"""list1=['apples','bananas','cherries']
tup1=(2,6,10)
for item in list1:
    print(item)
for i in tup1:
    print(i)

for i in range(0,11,5):
    print(i)"""


#students={'bob':12,'rachel':13,'emily':15}
#print(students)
#print(students['rachel'])
#print(students['bob'])


"""word = 'brontosaurus' 
d = dict() 
for c in word: 
    if c not in d: 
        d[c] = 1 
    else: 
        d[c] = d[c] + 1 
print(d)"""


"""counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100} 
print(counts.get('jan', 0)) 
print(counts.get('tim', 0)) """
 


"""word = 'brontosaurus' 
d = dict() 
for c in word: 
    if c not in d: 
        d[c] = 1 
    else: 
        d[c] = d[c] + 1 
print(d)
"""
"""word = 'brontosaurus' 
d = dict() 
for c in word: 
    d[c] = d.get(c,0)+ 1
print(d)
"""

"""counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100} 
for key in counts: 
    print(key, counts[key]) 
"""

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100} 
lst = list(counts.keys()) 
print(lst) lst.sort() 
for key in lst: 
    print(key, counts[key]) 

