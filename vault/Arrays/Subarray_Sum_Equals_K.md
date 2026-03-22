---
created: 2026-03-22
revisions:
  - 2026-03-24
  - 2026-03-29
  - 2026-04-06
  - 2026-04-21
---

## Metadata & Placement Tags
**Companies:** #Amazon #Google #Facebook #Microsoft #Meta #Service-Based
**Confidence Level:** [ ] Low [ ] Mid [ ] High
**Concepts:** #prefixsum [[Prefix Sum]], #hashmap [[HashMap]], #subarray [[Subarray]]

---

## Difficulty
**Medium**
#medium

---

## Pattern
**Prefix Sum with Hashing** (Frequency Map)

---

## Key Idea
The core intuition is that the sum of a subarray `nums[i...j]` can be expressed as `PrefixSum[j] - PrefixSum[i-1]`. If this difference equals `k`, then `PrefixSum[j] - k = PrefixSum[i-1]`. By storing the frequency of all seen prefix sums in a hash map, we can count how many times `PrefixSum[j] - k` has occurred previously in $O(1)$ time.

---

## Approach

### Brute Force
The naive approach involves iterating through every possible subarray $(i, j)$ and calculating its sum.
1. Use a nested loop where the outer loop starts at index `i` and the inner loop starts at `j = i`.
2. Calculate the sum of the subarray from `i` to `j`.
3. If `sum == k`, increment the counter.
- **Why inefficient?** It takes $O(n^2)$ or $O(n^3)$ time, making it too slow for arrays with $n > 10^4$.

### Optimal
The optimal approach uses a **Hash Map** to store the frequency of prefix sums encountered so far.
1. Initialize `count = 0`, `current_prefix_sum = 0`.
2. Initialize a hash map `prefix_sums_found` with `{0: 1}` to handle cases where a subarray starting from index 0 sums to `k`.
3. Iterate through the array:
    - Add the current element to `current_prefix_sum`.
    - Check if `(current_prefix_sum - k)` exists in the map.
    - If it exists, add its frequency to `count`.
    - Update the map with the `current_prefix_sum` frequency (increment by 1).
4. Return `count`.

---

## Code
```python
def subarraySum(nums: list[int], k: int) -> int:
    # count stores the total number of valid subarrays
    count = 0
    current_prefix_sum = 0
    
    # Map stores {prefix_sum: frequency}
    # Base case: sum 0 has occurred once (to catch subarrays starting at index 0)
    prefix_sums_found = {0: 1}
    
    for num in nums:
        current_prefix_sum += num
        
        # If (current_prefix_sum - target) was seen before, it means 
        # the elements between that point and now sum up to k.
        target = current_prefix_sum - k
        if target in prefix_sums_found:
            count += prefix_sums_found[target]
            
        # Record the current prefix sum in the map
        prefix_sums_found[current_prefix_sum] = prefix_sums_found.get(current_prefix_sum, 0) + 1
        
    return count
```

---

## Dry Run
**Input:** `nums = [1, 2, 3], k = 3`

| Step | Element | `current_prefix_sum` | `target = curr - k` | `target` in Map? | `count` | Map State |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Start | - | 0 | - | - | 0 | `{0: 1}` |
| 1 | 1 | 1 | -2 | No | 0 | `{0: 1, 1: 1}` |
| 2 | 2 | 3 | 0 | **Yes** (freq 1) | 1 | `{0: 1, 1: 1, 3: 1}` |
| 3 | 3 | 6 | 3 | **Yes** (freq 1) | 2 | `{0: 1, 1: 1, 3: 1, 6: 1}` |

**Result:** 2 subarrays (Subarrays: `[1, 2]` and `[3]`)

---

## Edge Cases
1. **Empty Array:** Should return 0.
2. **All Zeros:** If `k=0`, many subarrays will sum to 0. (e.g., `[0,0,0], k=0` -> 6 subarrays).
3. **Negative Numbers:** Unlike Sliding Window, the Prefix Sum + Hash Map approach handles negatives correctly because the prefix sum is not monotonic.
4. **$k$ is larger than total sum:** Should return 0 if no combination matches.

---

## Mistakes
> [!CAUTION] Mistakes
> - **Forgetting `{0: 1}`:** If you don't initialize the map with `0: 1`, you will miss subarrays that sum to `k` starting from index 0.
> - **Updating map before checking target:** Always check `current_prefix_sum - k` **before** adding the current `current_prefix_sum` to the map. Otherwise, if `k=0`, you will count the empty subarray or double-count.
> - **Using Sliding Window:** Sliding window only works when all numbers are non-negative. If the array contains negative numbers, the window sum doesn't move monotonically, necessitating the Prefix Sum + Hash Map approach.

---

## Complexity
- **Time Complexity:** $O(n)$
  *We traverse the array exactly once, performing $O(1)$ hash map lookups and insertions at each step.*
- **Space Complexity:** $O(n)$
  *In the worst case (all prefix sums are unique), the hash map will store $n$ entries.*

---
### 🔄 Revision Checklist
- [ ] Day 2 Revision (2026-03-24)
- [ ] Day 7 Revision (2026-03-29)
- [ ] Day 15 Revision (2026-04-06)
- [ ] Day 30 Revision (2026-04-21)
