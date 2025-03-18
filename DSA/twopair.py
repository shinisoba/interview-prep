#Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target. 

def twoSum(arr, target):
    s = set()
    for num in arr:
        complement = target - num #complement + num should be equal to target, so we try to subtract to extract complement

        # if the complement exists in the set, we have the pair
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False

arr = [0, -1, 2, -3, 1]
target = -2
