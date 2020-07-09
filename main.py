# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# And write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.

# Extra:

# Randomly generate two lists to test this
import random


def generateRandomList():
    randomlist = []
    for i in range(0, 15):
        n = random.randint(1, 30)
        randomlist.append(n)

    return randomlist


def verifyBiggerList(list1, list2):
    if(len(list1) >= len(list2)):
        return 1
    else:
        return 0


def main():
    list1 = []
    list2 = []
    listResult = []

    list1 = generateRandomList()
    print("List #1: ")
    print(list1)
    print("\n")

    list2 = generateRandomList()
    print("List #2: ")
    print(list2)
    print("\n")

    if(verifyBiggerList(list1, list2)):
        for item in list1:
            if item in list2:
                if item not in listResult:
                    listResult.append(item)

    else:
        for item in list2:
            if item in list1:
                if item not in listResult:
                    listResult.append(item)

    print(listResult)


main()
