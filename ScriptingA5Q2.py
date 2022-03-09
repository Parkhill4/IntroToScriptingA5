"""
        Question 2:
"""
def numVowels(string):
    count = 0
    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
            count = count + 1
    return count
def numConsonants(string):
    count = 0
    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
            count = count + 0
        else:
            count = count + 1
    return count
string = input("Enter a string:")
print("The number of vowels is:",numVowels(string))
print("The number of consonants is:",numConsonants(string))
