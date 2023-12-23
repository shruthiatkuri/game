"""import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)

"""




"""import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)"""


"""import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    for line in x:
        if line!=x:
            print(x)"""
            # UNIQUE

        


"""import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)"""



"""import re
x1 = '10.5 for cookies'
x2='We just received ^10.00 for cookies. '
x1= re.findall('^[0-9.]+',x1)
print(x1)
x2=re.findall('\^[0-9.]+',x2)
print(x2)"""



#print("hi\"there\"")

# search for the lines that contain 'From'

"""import re
filename=open("mbox-short.txt")
for line in filename:
    line=line.rstrip()
    if re.search('From:',line):
        print(line)"""


"""import re
file=input("Enter aa file name: ")
fhand=open(file,'r')
for line in fhand:
    line=line.rstrip()
    if re.search('^To:',line):
        print(line)
"""



"""import re
file=input("Enter file name: ")
fhand=open(file,'r')
for i in fhand:
    i=i.rstrip()
    if re.search('T.:',i):
        print(i)"""


"""import re
filename=input("Enter filename: ")
fhand=open(filename,'r')
for line in fhand:
    line=line.rstrip()
    if re.search('From:.+@',line):
        print(line)"""



"""import re 
filename=input("Enter the filename: ")
fhand=open(filename,'r')
for line in fhand:
    line=line.rstrip()
    if re.search('^From:.*y',line):
        print(line)"""



"""import re
file=open("mbox-short.txt")
for line in file:
    line=line.strip()
    x=re.findall('\S+@\S+',line)
    if len(x)>0:
        #print(\n)
        print(line)
"""



"""import re
file=open("mbox-short.txt")
for line in file:
    line=line.rstrip()
    x=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    if x!=line:
        print(x)"""


"""import re
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    x=re.findall('^X\S*:[0-9.]+',line)
    if len(x)>0:
        print(x)

"""
"""class Person:
  def  __init__(self, name, age):
    self.name = name
    self.age = age
  def student(self):
    print(self.name, self.age)
x=Person("RAm", "26")
x.student()
"""



"""class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name, self.age)

class student (Person):
    def __info__(self,name, age):
        super().__init__(name,age)
        self.student_roll_number=roll_num

    def print_student(self):
        super().print_person()

x=student("Sam","34","2338990")
x.printstudent()

"""

import pygame
print('Starting Game')
print('Initialising pygame')
pygame.init()
print('Initialising HelloworldGame')
pygame.display.set_mode((200, 100))
pygame.display.set_caption('Hello World')
print('Update display')
pygame.display.update()
print('Starting main Game Playing Loop')
running= True
while running:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        print('Recieved Quit event: ', event)
                        running= False
print('Game over')
pygame.quit()
