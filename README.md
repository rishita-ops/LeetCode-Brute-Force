# LeetCode — Brute Force (Pair Sum)

A focused Python implementation that **finds two elements of an array whose sum equals a target** by checking **every possible pair** with two nested loops. Clean, minimal, and correct — this program is the entry point to understanding the brute-force mindset, pair enumeration (`j` starting at `i + 1`), and the trade-off between a simple O(n²) solution and the O(n) hash-map solution it naturally leads to. Brute force is always the right _first_ solution to write: it is easy to prove correct, and every optimized version is measured against it.

🔗 **Related LeetCode problem:** [Two Sum](https://leetcode.com/problems/two-sum/)

---

## Problem Statement

Given an array of `n` integers and an integer `target`, find **two different elements** whose sum equals `target`. Print the two values and **their indices**. If no such pair exists, report that.

**Example Input:**

```
Enter the size of the array: 5
Enter the elements of the array: 1 2 3 4 5
Enter the target: 9
```

**Example Output:**

```
4 + 5 = 9 and index of 4 is 3 and index of 5 is 4
```

**How this differs from the official LeetCode wording:** the official problem returns the two **indices as a list** (for example `[3, 4]`), guarantees **exactly one solution**, and does not allow using the same element twice. This version prints a formatted message instead and returns the first pair it finds.

---

## The Code

```python
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
```

---

## The Critical Idea — Try Every Pair Exactly Once

This is the most important thing to understand about this program.

**The array is never modified.** Nothing is sorted, stored, or remembered. The function simply **enumerates every pair of positions** `(i, j)` with `i < j`, adds the two elements, and stops at the first pair that hits the target.

For `n = 5`, the pairs visited (in order) are:

```
        j=1     j=2     j=3     j=4
i=0    (0,1)   (0,2)   (0,3)   (0,4)
i=1            (1,2)   (1,3)   (1,4)
i=2                    (2,3)   (2,4)
i=3                            (3,4)
```

That is `n(n-1)/2 = 10` pairs — each unordered pair once, no element paired with itself, and no pair checked twice.

| Approach                    | Modifies array?   | Extra space | Time       |
| --------------------------- | ----------------- | ----------- | ---------- |
| **Brute force (this code)** | ❌ No             | O(1)        | O(n²)      |
| Sort + two pointers         | ✅ Yes (sorts it) | O(1)        | O(n log n) |
| Hash map (one pass)         | ❌ No             | O(n)        | O(n)       |

Brute force trades speed for simplicity and zero extra memory. For small arrays it is perfectly fine; for large arrays it is the baseline to beat.

---

## How the Loops Work

```python
for i in range(n):
    for j in range(i + 1, n):
        if array[i] + array[j] == target:
            return ...
```

- **Outer loop:** `i` runs `0 … n-1` — picks the first element of the pair
- **Inner loop:** `j` runs `i+1 … n-1` — picks the second element, always _after_ `i`
- **Test:** `array[i] + array[j] == target` — checks the pair's sum
- **Found:** the function **returns immediately** with a formatted message, so later pairs are never examined
- **Not found:** both loops finish, and the fallback message is returned

> **Off-by-one note:** The inner loop starts at `i + 1`, not `0` and not `i`. Starting at `i` would pair an element with **itself** (a false match whenever `2 × element == target`). Starting at `0` would check every pair twice, once as `(i, j)` and again as `(j, i)`, doubling the work.

---

## Algorithm (Pseudocode)

```
read n
read array[0..n-1]
read target

for i from 0 to n-1:
    for j from i+1 to n-1:
        if array[i] + array[j] == target:
            report array[i], array[j], i, j
            stop

report "no pair found"
```

---

## Dry Run

**Input:** `array = [1, 2, 3, 4, 5]`, `target = 9`

| `i` | `j` | `array[i] + array[j]` | Equals 9? |
| --- | --- | --------------------- | --------- |
| 0   | 1   | 1 + 2 = 3             | No        |
| 0   | 2   | 1 + 3 = 4             | No        |
| 0   | 3   | 1 + 4 = 5             | No        |
| 0   | 4   | 1 + 5 = 6             | No        |
| 1   | 2   | 2 + 3 = 5             | No        |
| 1   | 3   | 2 + 4 = 6             | No        |
| 1   | 4   | 2 + 5 = 7             | No        |
| 2   | 3   | 3 + 4 = 7             | No        |
| 2   | 4   | 3 + 5 = 8             | No        |
| 3   | 4   | 4 + 5 = 9             | **Yes**   |

**Output:** `4 + 5 = 9 and index of 4 is 3 and index of 5 is 4` ✅

---

## Complexity Analysis

| Metric            | Complexity                                                                     |
| ----------------- | ------------------------------------------------------------------------------ |
| Time (worst case) | **O(n²)** — all `n(n-1)/2` pairs are checked when the match is last or missing |
| Time (best case)  | **O(1)** — the very first pair `(0, 1)` already matches                        |
| Space             | **O(1)** — only the loop variables `i`, `j`, and `n`; the array is not copied  |

---

## Edge Cases

| Scenario                                                  | Behavior                                                                                         |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `n = 0` or `n = 1`                                        | Inner loop never runs — returns "No pair found…" ✅                                              |
| No pair adds up to the target                             | Every pair is checked, then the fallback message is returned ✅                                  |
| Duplicate values `[3, 3]`, target `6`                     | Different positions, so `(0, 1)` is a valid pair ✅                                              |
| Single element that is half the target `[5]`, target `10` | An element is never paired with itself — "No pair found…" ✅                                     |
| Negative numbers `[-1, 4, 5]`, target `4`                 | `-1 + 5 = 4` found at indices 0 and 2 ✅                                                         |
| Zeros `[0, 0]`, target `0`                                | `0 + 0 = 0` found at indices 0 and 1 ✅                                                          |
| Several valid pairs `[1, 4, 2, 3]`, target `5`            | Only the **first** pair found, `(1, 4)` at indices 0 and 1 is returned ⚠️                        |
| Non-integer input                                         | The sum still works for floats, but exact comparison with `==` can miss pairs due to rounding ⚠️ |

---

## Code-Quality Notes

**The file defines the function but never calls it.** The comment at the top says the program should ask for the array size, the elements, and the target, but the code contains only `brute_force_sum`. Running the file as it stands prints nothing. The "How to Compile and Run" section below includes a small driver that adds the input part.

**The function returns a string, not the indices.** That matches the required output format, but a reusable function would normally return the indices `(i, j)` (or `None`) and let the caller decide how to print them. A string return is harder to test and cannot be reused by other code.

**Not a direct LeetCode submission.** LeetCode calls a method on a class and expects a list of two indices back, so the standalone function above will not run in the LeetCode editor as it is. The submittable brute-force version is:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

**The array size is not needed in Python.** `len(array)` already gives `n`, so reading the size separately is only for matching the input format of the exercise.

---

## The Natural Extension — One-Pass Hash Map

The brute-force version asks, for each element, "is there _any_ later element that completes the sum?" and answers by scanning. A dictionary answers the same question instantly: remember every element seen so far, and for each new element look up its **complement** `target - element`.

```python
def hash_map_sum(array, target):
    seen = {}                       # value -> index
    for i, x in enumerate(array):
        need = target - x
        if need in seen:
            j = seen[need]
            return f"{array[j]} + {x} = {target} and index of {array[j]} is {j} and index of {x} is {i}"
        seen[x] = i
    return "No pair found that adds up to the target."
```

**Trace for `[1, 2, 3, 4, 5]`, `target = 9`:**

| `i` | `x` | `need = 9 - x` | `need` in `seen`?   | `seen` afterwards    |
| --- | --- | -------------- | ------------------- | -------------------- |
| 0   | 1   | 8              | No                  | `{1: 0}`             |
| 1   | 2   | 7              | No                  | `{1: 0, 2: 1}`       |
| 2   | 3   | 6              | No                  | `{1: 0, 2: 1, 3: 2}` |
| 3   | 4   | 5              | No                  | `{…, 4: 3}`          |
| 4   | 5   | 4              | **Yes**, at index 3 | —                    |

**Result:** `4 + 5 = 9 and index of 4 is 3 and index of 5 is 4` ✅ — the same answer as brute force, in one pass.

| Property        | Brute force (this code)                    | Hash map                      |
| --------------- | ------------------------------------------ | ----------------------------- |
| Time            | O(n²)                                      | **O(n)**                      |
| Extra space     | **O(1)**                                   | O(n)                          |
| Modifies array? | ❌ No                                      | ❌ No                         |
| Simplicity      | ✅ Very simple                             | Slightly more to reason about |
| When to use     | Small inputs, or as a correctness baseline | Large inputs, interviews      |

---

## Repository Structure

```
LeetCode-Brute-Force/
│
├── brute_force.py     # Main Python implementation
└── README.md          # Project documentation
```

---

## How to Compile and Run

**Prerequisites:** Python 3.8+

Add this driver below the function in `brute_force.py` so the program reads input as described in the comments:

```python
size = int(input("Enter the size of the array: "))
array = list(map(int, input("Enter the elements of the array: ").split()))
target = int(input("Enter the target: "))
print(brute_force_sum(array, target))
```

```bash
# Clone the repository
git clone https://github.com/rishita-ops/LeetCode-Brute-Force.git
cd LeetCode-Brute-Force

# Run
python3 brute_force.py
```

**On Windows:**

```bash
python brute_force.py
```

**Sample session:**

```
Enter the size of the array: 5
Enter the elements of the array: 1 2 3 4 5
Enter the target: 9
4 + 5 = 9 and index of 4 is 3 and index of 5 is 4
```

---

## Key Concepts Covered

- **Brute force** — try every possibility; simple, obviously correct, and slow
- **Pair enumeration** — nested loops with `j` starting at `i + 1` visit each unordered pair once
- **Early return** — stops at the first valid pair instead of scanning everything
- **O(n²) time, O(1) space** — the baseline cost to compare optimized solutions against
- **Complement lookup** — checking `target - x` is the idea behind the O(n) hash-map version
- **Returning data vs printing** — return indices from functions, format output at the call site
- **Python f-strings** — building the formatted result message

---

## Why This Problem Matters in DSA

The pair-sum pattern, and the brute-force-to-optimal progression, appears across a broad family of problems:

| Problem / Concept                                      | Connection                                                                          |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **Two Sum**                                            | The problem this solution is based on; the hash-map version is the optimal solution |
| **Two Sum II — Input Array Is Sorted** (LeetCode #167) | Sorted input allows two pointers in O(n) with O(1) space                            |
| **3Sum** (LeetCode #15)                                | Fix one element, then run the pair-sum idea on the rest                             |
| **4Sum** (LeetCode #18)                                | Fix two elements, then pair-sum on the rest                                         |
| **Two Sum IV — Input Is a BST** (LeetCode #653)        | Pair sum over a tree, using a set or in-order traversal                             |
| **Subarray Sum Equals K** (LeetCode #560)              | The same "look up the complement" idea, applied to prefix sums                      |

Every problem that asks "which elements combine to a target?" starts from this brute-force baseline and improves it with sorting, two pointers, or hashing.

---

## Contributing

Contributions are welcome. Consider adding:

- A version that **returns the indices** instead of a formatted string
- The **hash-map** version as a separate file for side-by-side comparison
- A **sort + two-pointer** version
- A version that finds **all** pairs instead of stopping at the first
- Input validation for empty arrays and non-integer input
- Implementations in C++, Java, or JavaScript

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
# Then open a Pull Request
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

_Part of a structured LeetCode practice series — fundamentals, done right._
