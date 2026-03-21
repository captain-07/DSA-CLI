import re

def detect_folder(content: str):
    """
    Analyzes content to map the problem to a subfolder.
    Attempts to identify the 'Pattern' section for more accurate routing.
    """
    content_lower = content.lower()
    
    # Try to extract the pattern from the "Pattern" section first
    pattern_section = re.search(r"## Pattern\s*(?:---)?\s*(.*?)(?:\n##|---|$)", content, re.DOTALL | re.IGNORECASE)
    search_scope = pattern_section.group(1).lower() if pattern_section else content_lower

    mapping = {
        "Arrays": ["array", "subarrays", "two pointer", "two-pointer", "sliding window", "prefix sum"],
        "Hashing": ["hash", "map", "set", "dictionary", "frequency"],
        "DP": ["dynamic programming", "memoization", "dp", "knapsack", "lcs", "lis"],
        "Trees": ["tree", "binary tree", "bst", "traversal", "depth-first search", "breadth-first search"],
        "Graph": ["graph", "bfs", "dfs", "dijkstra", "bellman-ford", "kruskal", "prim", "topological"],
        "Strings": ["string", "anagram", "palindrome", "substring"],
        "Math": ["math", "prime", "modulo", "gcd", "sieve", "bit manipulation"],
        "Heaps": ["heap", "priority queue"],
        "Recursion": ["recursion", "backtracking"]
    }

    # First pass: check in Pattern section (if found) or entire content
    for folder, keywords in mapping.items():
        for keyword in keywords:
            if keyword in search_scope:
                # If we found it in the limited scope, high confidence
                return folder

    # Second pass: if nothing found in Pattern section, check entire content (if not already done)
    if pattern_section:
        for folder, keywords in mapping.items():
            for keyword in keywords:
                if keyword in content_lower:
                    return folder
    
    return "Misc"
