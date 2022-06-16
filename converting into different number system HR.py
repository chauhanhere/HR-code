def print_formatted(number):
    for i in range(1,number+1,1):
        w=len(bin(number)[2:])
        print(w)
        print(str(i).rjust(w,' '),oct(i).lstrip("0o").rjust(w,' '),hex(i).lstrip("0x").rjust(w,' ').upper(),bin(i).lstrip('0b').rjust(w,' '))

    
if __name__ == '__main__':
    n = int(input("Enter the number"))
    print_formatted(n)
