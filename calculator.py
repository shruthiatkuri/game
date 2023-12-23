"""x=int(input("Enter the x value: "))
y=int(input("Enter the y value: "))

#z=int(x)+int(y)
print(x+y)"""



""""x=float(input("Enter x value: "))
y=float(input("Enter y value: "))
z=x+y
z=round(z)
print(f"{z:,}")"""



"""cheeses=['cheddar','Edam','Gouda']
for cheese in cheeses:
    print(cheese)"""


"""numbers = [5, 10, 15]
for i in range(len(numbers)): 
    numbers[i] = numbers[i] * 2
print(numbers)"""

"""nums = [3, 41, 12, 9, 74, 15] 
print(len(nums)) 
print(max(nums))""" 


"""total = 0 
count = 0 
while (True): 
    inp = input('Enter a number: ') 
    if inp == 'done': 
        break 
    value = float(inp) 
    total = total + value 
    count = count + 1
average = total / count 
print('Average:', average)"""

"""word = 'brontosaurus' 
d = dict() 
for c in word: 
    if c not in d: 
        d[c] = 1 
    else: 
        d[c] = d[c] + 1 
print(d)"""


"""word = 'brontosaurus' 
d = dict() 
for c in word: 
    d[c] = d.get(c,0) + 1
print(d)"""


fname = input('Enter the file name: ') 
try: 
    fhand = open(fname) 
except: 
    print('File cannot be opened:', fname) 
    exit() 
counts = dict() 
for line in fhand: 
    words = line.split() 
    for word in words: 
        if word not in counts: 
            counts[word] = 1 
        else: 
            counts[word] += 1 
print(counts)


