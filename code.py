#Brute Force
#ask for array size and elements and then a target
#ex : array size = 5 array = [1, 2, 3, 4, 5] target = 9
#output : 4+5=9 and index of 4 is 3 and index of 5 is 4
def brute_force_sum(array, target):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == target:
                return f"{array[i]} + {array[j]} = {target} and index of {array[i]} is {i} and index of {array[j]} is {j}"
    return "No pair found that adds up to the target."
