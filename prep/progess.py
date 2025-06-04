# DSA Interview Preparation Tracker (Python)

# ✅ Core Topics Checklist
# You can mark topics as completed like: done['Arrays'] = True

done = {
    'Arrays': False,
    'Hashing': False,
    'Stack': False,
    'Queue & Deque': False,
    'Linked List': False,
    'Recursion & Backtracking': False,
    'Binary Trees': False,
    'Binary Search Trees (BST)': False,
    'Heaps / Priority Queues': False,
    'Trie': False,
    'Graphs': False,
    'Greedy': False,
    'Dynamic Programming': False,
    'Bit Manipulation': False,
}

# 📚 Detailed Learning Map + Must Practice Problems
DSA_TOPICS = {
    "Arrays": [
        "Two Pointer Technique",
        "Sliding Window",
        "Prefix Sum",
        "Kadane’s Algorithm",
        "Dutch National Flag Problem",
        "PROBLEMS: Two Sum, Best Time to Buy and Sell Stock, Product of Array Except Self"
    ],
    "Hashing": [
        "Frequency Counting",
        "2Sum/3Sum/4Sum",
        "Group Anagrams",
        "Longest Consecutive Sequence",
        "PROBLEMS: Group Anagrams, Longest Consecutive Sequence, Subarray Sum Equals K"
    ],
    "Stack": [
        "Valid Parentheses",
        "Min Stack",
        "Monotonic Stack",
        "Reverse Polish Notation",
        "PROBLEMS: Valid Parentheses, Daily Temperatures, Largest Rectangle in Histogram"
    ],
    "Queue & Deque": [
        "Sliding Window Maximum",
        "Queue via Stacks",
        "Circular Queue",
        "PROBLEMS: Sliding Window Maximum, Implement Queue using Stacks, Rotting Oranges"
    ],
    "Linked List": [
        "Reverse Linked List",
        "Cycle Detection",
        "Merge Sorted Lists",
        "Intersection Node",
        "Add Two Numbers",
        "LRU Cache",
        "PROBLEMS: Reverse Linked List, Detect Cycle, Merge Two Sorted Lists"
    ],
    "Recursion & Backtracking": [
        "Subsets",
        "Permutations",
        "N-Queens",
        "Sudoku Solver",
        "Generate Parentheses",
        "PROBLEMS: Subsets, Permutations, Word Search"
    ],
    "Binary Trees": [
        "Inorder/Preorder/Postorder",
        "Level Order",
        "Height/Diameter",
        "Lowest Common Ancestor",
        "Serialize & Deserialize",
        "PROBLEMS: Invert Binary Tree, Diameter of Binary Tree, Lowest Common Ancestor"
    ],
    "Binary Search Trees (BST)": [
        "Insert/Delete",
        "Validate BST",
        "Kth Smallest Element",
        "Floor and Ceil",
        "PROBLEMS: Validate BST, Kth Smallest Element, Trim BST"
    ],
    "Heaps / Priority Queues": [
        "Kth Largest/Smallest",
        "Merge K Lists",
        "Top K Frequent",
        "Median of Stream",
        "PROBLEMS: Kth Largest Element, Top K Frequent Elements, Merge K Sorted Lists"
    ],
    "Trie": [
        "Insert/Search Word",
        "Autocomplete",
        "Word Search II",
        "PROBLEMS: Implement Trie, Word Search II, Replace Words"
    ],
    "Graphs": [
        "DFS & BFS",
        "Topological Sort",
        "Cycle Detection",
        "Dijkstra’s Algo",
        "Union Find",
        "Kruskal/Prim",
        "PROBLEMS: Number of Islands, Course Schedule, Clone Graph"
    ],
    "Greedy": [
        "Activity Selection",
        "Job Sequencing",
        "Fractional Knapsack",
        "Jump Game",
        "Gas Station",
        "PROBLEMS: Jump Game, Gas Station, Merge Intervals"
    ],
    "Dynamic Programming": [
        "0/1 Knapsack",
        "Fibonacci (Memo/Tab)",
        "LCS & LIS",
        "Coin Change",
        "Matrix DP (Unique Paths)",
        "PROBLEMS: House Robber, Longest Increasing Subsequence, Coin Change"
    ],
    "Bit Manipulation": [
        "XOR Tricks",
        "Single Number",
        "Count Set Bits",
        "Power of 2",
        "PROBLEMS: Single Number, Missing Number, Sum of Two Integers"
    ]
}

# You can create helper functions below to print your progress

def print_progress():
    for topic, completed in done.items():
        status = "✅" if completed else "❌"
        print(f"{status} {topic}")


print_progress()
