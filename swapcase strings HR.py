'''
#Use of swapcase function
s="HackerRank.com presents Pythonist 2"
print(s.swapcase())

#spliting and joining a string
def split_and_join(line):
    x=line.split(' ')
    return '-'.join(x)

#printing last name and first name
def print_full_name(first, last):
    # Write your code here
    print("Hello"+" "+first+" "+last +"! You just delved into python.")

#Mutable,list is mutable but tuple is not  
def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    return ''.join(l)

#counting sub string in a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

# string validatos
s = input("Enter the string")
print(any(a.isalnum() for a in s) )
print(any(a.isalpha() for a in s) )
print(any(a.isdigit() for a in s) )
print(any(a.islower() for a in s) )
print(any(a.isupper() for a in s) )

#Replace all ______ with rjust, ljust or center. 

thickness = int(input("Enter any odd number")) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
'''
def wrap(string, max_width):
    s = ""
    for c in range(0,len(string),max_width):
        print(c)
        s += string[c:c+max_width] + "\n"
    return s
print(wrap("bdhb njvbfjvbfbdbfd",4))

s="sbhdbhbf dbejfebrf"
x=""
v=4
for c in range(0,len(s),v):
    print(c)
    x+=s[c:c+3]+"\n"
    print(x)






