'''
This function checks on a first look if an array qualifies for the requirement.
start by taking the array A = [a1, a2, a3, a4, ..., an] of size n and the sum of the elements is sum(A)
This array A should be split in two arrays B and C non empty. The sizes for these two are Sb and Sc (size B and C)

sum(B) + sum(C) = sum(A)
Sb + Sc = n
so, we have:
    sum(B)/Sb = sum(C)/Sc = sum(A)/n = average of partitions is avg of array
    sum(B)/Sb = (sum(A) - sum(B)) / (n - Sb)

sum(B) * (n - Sb) = (sum(A) - sum(B)) * Sb
n * sum(B) - Sb * sum(B) = Sb * sum(A) - Sb * sum(B) --- Sb*sum(B) is reduced
so we have: n * sum(B) = Sb * sum(A) ----
            sum(B) = (Sb * sum(A)) / n
    sum(B) should be an integer so Sb * sum(A) should be a multiple of n
    so, for at least a possible length of a partition (range [1 to n-1]),
    sum(A) * lengthOfPartition % n should be 0
(here I take only lengths from 1 to n / 2, because the lengths of B and C are proportional so if one partition has a
length > n / 2, the other one for certain has a length < n / 2 (I hope that I was clear I'm not that good at explanations)

Long story short, if at least for one length, the property is True, the array A should be taken into consideration.
'''
def isValid(arraySum, arraySize):
    for i in range(1, arraySize // 2 + 1):
        if arraySum * i % arraySize == 0:
            return True
    return False


'''
This function is similar to the one above but we also want to check if the sum of a partition exists in a 
list of sets of possible sums (explanations for possibleSum variable later)
'''
def findSpecificSum(arraySum, arraySize, possibleSums):
    for i in range(1, arraySize // 2 + 1):
        if arraySum * i % arraySize == 0 \
                and arraySum * i // arraySize in possibleSums[i]:
            return True
    return False

'''
Aaand the mayhem begins.
First we check if A qualifies.
Then, create a list of sets (in order for the sums to not repeat),
list having the size n / 2 + 1
Every set from the list represents all possible sums computed for a partition of size = index of set

Then, iterate through array A, and for every element and for every set from the list, 
we compute the sum adding the current item to all sums from the set from "above" the current set we are currently filling.

Then, check if we can find a specific sum at least once in the sets, and we're done.
'''
def splitArray(A):
    arraySize = len(A)
    arraySum = sum(A)

    if not isValid(arraySum, arraySize):
        return False

    possibleSums = [set() for _ in range(arraySize // 2 + 2)]
    possibleSums[0].add(0)

    for item in A:
        for i in range(arraySize // 2, 0, -1):
            for currentSum in possibleSums[i - 1]:
                possibleSums[i].add(currentSum + item)

    if findSpecificSum(arraySum, arraySize, possibleSums):
        return True

    return False


if __name__ == '__main__':
    print(splitArray([2, 4, 5, 7, 10, 14]))
