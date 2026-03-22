---
created: 2026-03-22
revisions:
  - 2026-03-24
  - 2026-03-29
  - 2026-04-06
  - 2026-04-21
---

I will generate the Two Sum DSA note according to the provided template and save it to the Obsidian vault under the `Hashing` folder.

## Metadata & Placement Tags
- **Common Companies:** #Amazon #Google #TCS #Service-Based #Adobe #Apple #Microsoft
- **Confidence Level:** [ ] Low [ ] Mid [ ] High
- **Concept Links:** #hashmap [[HashMap]], #twopointers [[Two Pointers]], #arrays [[Arrays]]

---
## Difficulty
- **Classification:** Easy
- **Tag:** #easy

---
## Pattern
- **Pattern Name:** Hashing / HashMap Optimization
- **Description:** Using a dictionary (hash map) to store elements as we traverse the array, allowing for $O(1)$ lookups of the required complement.

---
## Logic Evolution
- **Brute Force:** The naive approach involves two nested loops to check every possible pair of elements. For each element at index $i$, we iterate through the rest of the array (index $j$) and check if `nums[i] + nums[j] == target`. This results in a time complexity of $O(n^2)$, which is inefficient for large datasets.
- **Optimal (One-Pass Hash Map):** The key idea is to iterate through the array once and, for each element `num`, calculate its required complement: `complement = target - num`. We then check if this `complement` already exists in our hash map. If it does, we have found our two numbers and return their indices. If not, we store the current number and its index in the hash map to be used as a potential complement for future elements. This eliminates the need for a second pass.

---
## Python Implementation (Optimal)
```python
def twoSum(nums: list[int], target: int) -> list[int]:
    # Stores value to index mapping: {value: index}
    seen = {}
    
    for i, num in enumerate(nums):
        # Calculate the number needed to reach the target
        complement = target - num
        
        # Check if the complement has been encountered before
        if complement in seen:
            # Return indices of the complement and current number
            return [seen[complement], i]
        
        # Store current number and index for future lookup
        seen[num] = i
    
    # Per constraints, a solution is guaranteed
    return []
```

---
## Dry Run Table
Tracing `nums = [2, 11, 7, 15]`, `target = 9`:

| Step | `i` | `num` | `complement` (target - num) | `complement in seen`? | `seen` (after step) | Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 2 | 7 | No | `{2: 0}` | - |
| 2 | 1 | 11 | -2 | No | `{2: 0, 11: 1}` | - |
| 3 | 2 | 7 | 2 | **Yes** (at index 0) | `{2: 0, 11: 1}` | `[0, 2]` |

---
## Edge Cases
1. **Minimum Array Size ($n=2$):** The smallest valid input must still return the indices correctly.
2. **Negative Integers:** The logic should handle cases like `nums = [-3, 4, 3, 90]`, `target = 0` correctly.
3. **All Identical Elements:** If `nums = [3, 3]`, `target = 6`, the map must handle the first `3` before checking the second `3` to avoid using the same index twice.
4. **Target is 0:** Ensuring the math holds even when the complement is the number itself or zero.

---
## Common Mistakes
> [!CAUTION] Mistakes
> - **Self-usage:** Trying to use the same element twice (e.g., if `target` is 10 and `nums` has a 5, you shouldn't return `[index_of_5, index_of_5]`). The complement check must happen *before* or *separately* from adding the current number to the map.
> - **Forget about the complement check:** Adding the current number to the hash map *before* checking for the complement can lead to using the same index twice if `target - num == num`. This is why we check for the complement **first**.
> - **Returning values instead of indices:** Read the problem carefully; usually, the *indices* of the numbers are required, not the numbers themselves.

---
## Complexity Analysis
- **Time Complexity:** $O(n)$
  - We traverse the list containing $n$ elements only once. Each lookup in the hash map (dictionary) takes $O(1)$ on average.
- **Space Complexity:** $O(n)$
  - In the worst case, we might store all $n$ elements in the hash map if the complement is only found at the very end of the array.

---

---
### 🔄 Revision Checklist
- [ ] Day 2 Revision (2026-03-24)
- [ ] Day 7 Revision (2026-03-29)
- [ ] Day 15 Revision (2026-04-06)
- [ ] Day 30 Revision (2026-04-21)
