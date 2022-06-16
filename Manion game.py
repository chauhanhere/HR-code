'''
#counting number of words letter formed by each vowel constant
def minion_game(s):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            print(i,s[i])
            kevsc += (len(s)-i)
        else:
            print(i,s[i])
            stusc += (len(s)-i)
    if kevsc > stusc:
        print ("Kevin",kevsc)
    elif kevsc < stusc:
        print ("Stuart",stusc)
    else:
        print ("Draw")
print(minion_game("BANANA"))
'''














