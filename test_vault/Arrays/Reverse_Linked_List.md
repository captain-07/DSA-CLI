---
created: 2026-04-07
revisions:
  - 2026-04-09
  - 2026-04-14
  - 2026-04-22
  - 2026-05-07
---

# Reverse Linked List

---

## Metadata & Placement Tags

- **Target Companies:**
  - #Amazon #Google #Microsoft #Meta #Apple #Adobe

- **Confidence Checklist:**
  - [ ] Low  
  - [ ] Medium  
  - [ ] High  

- **Concepts:**
  - #linkedlist [[Linked List]]
  - #pointers [[Pointers]]
  - #recursion [[Recursion]]

---
## Pattern

Three Pointers (Iterative)  
Divide and Conquer (Recursive)

---
## Difficulty

Easy #easy

---
## ⚡ Key Idea (Core Insight)

The core insight is to reverse the `next` pointer of each node to point to its predecessor instead of its successor. Since changing `curr.next` breaks the link to the rest of the list, we must store the `next_node` in a temporary variable before performing the reversal.

---
## ⚡ Quick Recall (VERY IMPORTANT)

Maintain `prev`, `curr`, and `temp_next` pointers. In each step: `temp_next = curr.next`, `curr.next = prev`, then move `prev` and `curr` forward.

---
## Approach

### Brute Force
- Copy all node values into an array, reverse the array, and create a brand new linked list from the reversed values.
- **Complexity:** Time: O(N), Space: O(N).

### Optimal (Iterative)
1. Initialize `prev` as `None` and `curr` as `head`.
2. Iterate through the list while `curr` is not `None`.
3. Save `next_node = curr.next`.
4. Reverse the link: `curr.next = prev`.
5. Advance pointers: `prev = curr`, `curr = next_node`.
6. Return `prev` as the new head.

### Optimal (Recursive)
1. Base case: If list is empty or has one node, return `head`.
2. Recursively reverse the rest of the list: `new_head = self.reverseList(head.next)`.
3. Flip the link for the current node: `head.next.next = head`.
4. Break the old link: `head.next = None`.
5. Return `new_head`.

---
## Code (Python)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # Store next node to avoid losing the rest of the list
            next_node = curr.next
            # Reverse the pointer
            curr.next = prev
            # Move pointers forward
            prev = curr
            curr = next_node
            
        # prev ends up at the new head of the reversed list
        return prev
```

---
## Dry Run (Smart Example)

**Input:** `1 -> 2 -> 3 -> None`

| Step | Variables | Explanation |
| :--- | :--- | :--- |
| Init | `prev=None`, `curr=1` | Initial state. |
| 1 | `next=2`, `1.next=None`, `prev=1`, `curr=2` | Node 1 now points to None. |
| 2 | `next=3`, `2.next=1`, `prev=2`, `curr=3` | Node 2 now points to 1. |
| 3 | `next=None`, `3.next=2`, `prev=3`, `curr=None` | Node 3 now points to 2. |
| End | `return prev(3)` | Loop terminates as `curr` is None. |

---
## Edge Cases

- **Empty List (`head = None`):** Function should return `None` immediately.
- **Single Node (`1 -> None`):** Loop runs once, `prev` becomes `1`, returns `1`.
- **Two Nodes (`1 -> 2`):** Standard reversal logic holds; returns `2 -> 1`.
- **Circular List:** Will cause an infinite loop (detect first using Floyd's).

---
## Mistakes

- **User Mistake:** Forgot edge cases for empty list (ensure `while curr` handles this or add `if not head`).
- Forgetting to save `curr.next` before overwriting it.
- Returning `curr` instead of `prev` (at the end, `curr` is `None`).
- Not breaking the `head.next` link in recursive approach (causes cycles).

---
## Complexity

**Time:** O(N) → We visit each of the N nodes exactly once.  
**Space:** O(1) → Iterative approach uses only three pointer variables regardless of list size. (Note: Recursive is O(N) due to call stack).

---
## Similar Problems

- [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) - Medium
- [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) - Easy
- [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) - Hard
- [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) - Medium

---
## Tags and Properties

- #dsa #important #revisit #linkedlist [[Linked List]] #pointers [[Pointers]]
- **Revision Date:** 2026-04-07
- **Problem Link:** [Reverse Linked List - LeetCode](https://leetcode.com/problems/reverse-linked-list/)

---
### 🔄 Revision Checklist
- [ ] Day 2 Revision (2026-04-09)
- [ ] Day 7 Revision (2026-04-14)
- [ ] Day 15 Revision (2026-04-22)
- [ ] Day 30 Revision (2026-05-07)
