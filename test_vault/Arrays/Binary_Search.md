---
created: 2026-04-10
revisions:
  - 2026-04-12
  - 2026-04-17
  - 2026-04-25
  - 2026-05-10
---

# Binary Search

---

## Metadata & Placement Tags

- **Target Companies:**
  - #Amazon #Google #Microsoft #Facebook #Adobe #Apple #Bloomberg #Uber

- **Confidence Checklist:**
  - [ ] Low  
  - [ ] Medium  
  - [ ] High  

- **Concepts:**
  - #searching [[Searching]], #array [[Array]], #divide-and-conquer [[Divide and Conquer]]

## Pattern

Decrease and Conquer (Logarithmic Search Space Reduction).

---
## Difficulty

Easy
#easy

---

## ⚡ Key Idea (Core Insight)

The array must be **sorted**. By comparing the target with the middle element, we can eliminate half of the remaining search space in each step. This transforms a linear scan into a logarithmic search by exploiting the ordered property of the data.

---

## ⚡ Quick Recall (VERY IMPORTANT)

Calculate `mid = low + (high - low) // 2` to avoid overflow and keep shrinking the `[low, high]` window until `low > high`.

---

## Approach

### Brute Force
- Linear Search: Iterate through every element in the array until the target is found or the end is reached.
- **Time:** $O(n)$
- **Space:** $O(1)$

### Optimal
1. Initialize `low = 0` and `high = len(nums) - 1`.
2. While `low <= high`:
   - Calculate `mid`.
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, move `low = mid + 1` (search right).
   - If `nums[mid] > target`, move `high = mid - 1` (search left).
3. If the loop ends without finding the target, return -1.

---

## Code (Python)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Edge case: Empty array check
        if not nums:
            return -1
            
        low, high = 0, len(nums) - 1
        
        while low <= high:
            # Prevent potential overflow in other languages, idiomatic in Python
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
```

---

## Dry Run (Smart Example)

**Input:** `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

| Step | low | high | mid | nums[mid] | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 5 | 2 | 3 | `nums[2] < 9` -> `low = 3` |
| 2 | 3 | 5 | 4 | 9 | `nums[4] == 9` -> **Return 4** |

**Input:** `nums = [5]`, `target = 5` (Single element)

| Step | low | high | mid | nums[mid] | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 0 | 0 | 5 | `nums[0] == 5` -> **Return 0** |

---

## Edge Cases

- **Empty Array:** Handled by returning -1 immediately or by the `low <= high` condition (where `0 <= -1` is false).
- **Single Element:** Check if the single element is the target or not.
- **Target Not Present:** Loop terminates with `low > high`, returning -1.
- **Target is First/Last Element:** Correctly identified by `mid` as the window shrinks.

---

## Mistakes

- **CRITICAL:** **Forgot to handle empty array.** Always check `if not nums` or ensure your loop bounds correctly handle a length of 0.
- **Off-by-one errors:** Using `while low < high` instead of `while low <= high`.
- **Integer Overflow:** Using `(low + high) // 2` instead of `low + (high - low) // 2` (relevant in Java/C++).
- **Incorrect Bounds Update:** Using `low = mid` or `high = mid` instead of `mid + 1` / `mid - 1`, leading to infinite loops.

---

## Complexity

Time: $O(\log n)$ → The search space is halved in every iteration.  
Space: $O(1)$ → Iterative approach uses constant extra space.

---

## Similar Problems

- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Medium
- [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Medium
- [Search Insert Position](https://leetcode.com/problems/search-insert-position/) - Easy

---

## Tags and Properties
- #dsa #important #revisit #blind75
- #searching [[Searching]] #binary-search [[Binary Search]]
- **Revision Date:** 2026-04-10
- **Problem Link:** [LeetCode - Binary Search](https://leetcode.com/problems/binary-search/)

---
### 🔄 Revision Checklist
- [ ] Day 2 Revision (2026-04-12)
- [ ] Day 7 Revision (2026-04-17)
- [ ] Day 15 Revision (2026-04-25)
- [ ] Day 30 Revision (2026-05-10)
