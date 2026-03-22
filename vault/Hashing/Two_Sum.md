---
created: 2026-03-22
revisions:
  - 2026-03-24
  - 2026-03-29
  - 2026-04-06
  - 2026-04-21
---

I will read the existing prompt template and the main logic to ensure the generated note aligns with the project's standards and formatting requirements.

I will read `dsa/generator.py` to understand how the generation logic is implemented and then I'll decide whether to run the tool or generate the content directly.

# Two Sum
---
## Metadata & Placement Tags
- **Common Companies:** #Amazon, #Google, #Facebook, #Microsoft, #Apple, #Adobe, #TCS, #Service-Based
- **Confidence Level:** [ ] Low [ ] Mid [ ] High
- **Concepts:** #hashmap [[HashMap]], #arrays [[Arrays]], #searching [[Searching]]

---
## Difficulty
**Easy** #easy

---
## Pattern
**Hashing** (One-pass Hash Map)

---
## Key Idea
The core intuition is to trade space for time. Instead of looking for the second number by iterating through the rest of the array (Brute Force), we store the numbers we have already seen in a Hash Map. For every new number `x` we encounter, we calculate its **complement** (`target - x`) and check if that complement is already present in our map.

---
## Approach

### Brute Force
The naive approach involves using two nested loops to check every possible pair of numbers in the array.
1. The outer loop picks an element `i`.
2. The inner loop iterates through the remaining elements `j` to see if `nums[i] + nums[j] == target`.
This is inefficient because it performs $O(n^2)$ comparisons, making it too slow for large input sizes.

### Optimal (One-Pass Hash Map)
We can solve this in a single pass using a Hash Map (dictionary in Python):
1. Create an empty hash map to store value-to-index mappings.
2. Iterate through the array once.
3. For each element `nums[i]`, calculate `complement = target - nums[i]`.
4. Check if `complement` exists in the hash map.
   - If **Yes**: We have found the two numbers. Return the indices `[map[complement], i]`.
   - If **No**: Add the current number and its index to the hash map: `map[nums[i]] = i`.
5. This ensures we check for the complement in $O(1)$ average time.

---
## Code
```python
def twoSum(nums: list[int], target: int) -> list[int]:
    # hash_map stores: {value: index}
    prev_map = {} 
    
    for i, n in enumerate(nums):
        complement = target - n
        
        # Check if the required complement has been seen before
        if complement in prev_map:
            # Found the pair! Return indices of complement and current
            return [prev_map[complement], i]
        
        # Store current number and index for future complement checks
        prev_map[n] = i
        
    return [] # Should not reach here per problem constraints
```

---
## Dry Run
Input: `nums = [3, 2, 4]`, `target = 6`

| Step | `i` | `n` | `complement` (`6 - n`) | `prev_map` (Before) | `complement` in `prev_map`? | `prev_map` (After) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 3 | 3 | `{}` | No | `{3: 0}` |
| 2 | 1 | 2 | 4 | `{3: 0}` | No | `{3: 0, 2: 1}` |
| 3 | 2 | 4 | 2 | `{3: 0, 2: 1}` | **Yes!** (at index 1) | - |

**Output:** `[1, 2]`

---
## Edge Cases
1. **Minimum Array Size:** The array contains exactly two elements (e.g., `nums = [5, 5], target = 10`).
2. **Negative Integers:** The target or the numbers themselves are negative (e.g., `nums = [-1, -2, -3], target = -5`).
3. **Large Numbers:** Elements or target exceed standard 32-bit integer ranges (Python handles this automatically).
4. **Complement is the same as the number:** For `target = 6` and `n = 3`, the complement is `3`. We must ensure we don't use the same element twice (handled by checking `prev_map` *before* adding the current index).

---
## Mistakes
> [!CAUTION] Mistakes
> - **The "Complement" Oversight:** Many beginners forget to calculate the complement and instead try to find any two numbers that look "right." The logic MUST be: `current + x = target` $\implies$ `x = target - current`.
> - **Addressing User Note:** *Forget about the complement check* — Failing to check if the complement exists in the map before adding the current element can lead to missing the solution or using the same index twice if the complement is equal to the current number.
> - **Indexing Errors:** Returning the values instead of the indices as requested by the problem.
> - **One-based vs Zero-based:** Forgetting that array indices start at `0` in Python.

---
## Complexity
- **Time Complexity:** $O(n)$
  - We traverse the list containing $n$ elements exactly once. Each lookup in the hash table takes $O(1)$ time on average.
- **Space Complexity:** $O(n)$
  - In the worst case, we might store $n$ elements in the hash map if the pair is found at the very end of the array.

---
### 🔄 Revision Checklist
- [ ] Day 2 Revision (2026-03-24)
- [ ] Day 7 Revision (2026-03-29)
- [ ] Day 15 Revision (2026-04-06)
- [ ] Day 30 Revision (2026-04-21)
