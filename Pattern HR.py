''''
n, m =7,21
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

N, M = map(int,input().split())
for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))

def add(n):
    return n+n
v=(1,2,3,4)
s=map(add,v)
print(list(s))


x="BNANSHS"
s=x.center(20,'!')
print(s)

n,m=7,21
for i in range(1,n,2):
    print((".|."*i).center(m,'-'))
print("Welcome".center(m,'-'))
for i in range(n-2,-1,-2):
    print((".|."*i).center(m,'-'))

#pattern increasing order
n=int(input("Enter odd number"))
for i in range(1,n+1,2):
    print((i*'*').center(n,' '))

#pattern increasing order
n=int(input("Enter odd number"))    
for i in range(n-2,-1,-2):
    print((i*'*').center(n,' '))

#Diamond Shape
n=int(input("Enter odd number"))
for i in range(1,n+1,2):
    print((i*'*').center(n,' '))
#print(("Suraj Chauhan").center(n,'-'))
for i in range(n-1,-1,-2):
    print((i*'*').center(n,' '))

#
n=int(input("Enter odd number"))
for i in range(1,n,2):
    print((i*'*').center(n,' '))
print(("Suraj Chauhan").center(n,'-'))
for i in range(n,-1,-2):
    print(i)
    print((i*'*').center(n,' '))

#Pattern in increasing order in 
n=int(input("Enter odd number"))
for i in range(1,n,1):
    print('*'*i)
'''
n=int(input("Enter any number"))
for i in range(1,n,1):
    for j in range(i,i+1):
        print(j,'%d',j)
'''
#pattern in reverse order
n=int(input("Enter odd number"))
for i in range(n,-1,-1):
    print('*'*i)
print("Suraj Chauhan")

#Both in increasing and decresing order
n=int(input("Enter the digit"))
for i in range(1,n+1,1):
    print(i*"*")
for j in range(n-1,-1,-1):
    print(j*"*")



import string
alpha = string.ascii_lowercase
print(alpha)
n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(i)
    print(L)
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))


#Pattern with the alphabetical order

import string
def print_rangoli(size):
    alpha ="*"
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(4*size-3, ' '))
print_rangoli(5)

s='Suraj'
print(s.removeprefix('S'))
'''
