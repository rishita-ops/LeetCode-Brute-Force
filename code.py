def brute_force_sum(array, target):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == target:
                return f"{array[i]} + {array[j]} = {target} and index of {array[i]} is {i} and index of {array[j]} is {j}"
    return "No pair found that adds up to the target."
