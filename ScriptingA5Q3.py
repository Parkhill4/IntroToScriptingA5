"""
    Question 3:
"""

str1 = "P@#yn26at^&i5ve"
str1Length = len(str1)
print("The length of str1 is: ", str1Length)

str2 = "/*Jon is @developer & musician"
str2fixed = ""
for i in str2:
    if i.isalnum():
        str2fixed += i
print(str2fixed)

str3 = "Emma-is-a-data-scientist"
str3fixed = str3.replace("-"," ")
print(str3fixed)

str4 = "Hello, have a good day"
for i in range(len(str4)):
    if(str4[i] == 'a' or str4[i] == 'e' or str4[i] == 'i' or str4[i] == 'o' or str4[i] == 'u'):
        print(str4[i], end = "")
