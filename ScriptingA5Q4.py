"""
    Question 4:
"""

n = int(input("Enter the number of integers to be in the list:"))
import random
list = []
for i in range(0,n):
    num = random.randint(0, 100)
    list.append(num)
list.sort()
print(list)
def getAverage():
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    avg = total/n
    print(avg)

def getMedian():
    median = list[n//2]
    print(median)

getAverage()
getMedian()
