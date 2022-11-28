A = {"Tom", "Sara", "Ali", "Ying", "Amit", "Megan", "Alan", "Layla", "Jane", "Alex"}
B = {"UofO", "UofA", "OT", "UofT", "UBC", "QU", "Y", "CU", "MU", "UofW"}

A_pref = {
  "Tom": ["UBC", "UofT", "UofW", "UofA", "QU", "OT", "MU", "UofO", "YU", "CU"], 
  "Sara": ["UofO", "QU", "UofT", "MU", "UofA", "UofW", "OT", "YU", "CU", "UBC"], 
  "Ali": ["QU", "UofT", "CU", "OT", "UofO", "MU", "UofA", "YU", "UBC", "UofW"], 
  "Ying": ["MU", "OT", "UofA", "UBC", "QU", "CU", "UofW", "YU", "UofT", "UofO"], 
  "Amit": ["UofT", "YU", "UofA", "OT", "UBC", "UofW", "QU", "UofO", "MU", "CU"],
  "Megan": ["YU", "UofW", "UBC", "UofT", "QU", "UofO", "MU", "OT", "CU", "UofA"], 
  "Alan": ["MU", "YU", "CU", "UofO", "UofA", "UofT", "UBC", "QU", "OT", "UofW"], 
  "Layla": ["UofT", "UofA", "MU", "CU", "YU", "UBC", "QU", "UofW", "OT", "UofO"],
  "Jane": ["OT", "UofO", "UofA", "MU", "YU", "UofT", "QU", "UBC", "UofW", "CU"],
  "Alex": ["UofW", "UofO", "OT", "MU", "YU", "UofT", "UBC", "CU", "QU", "UofA"]
}

B_pref = {
  "UofO": ["Tom", "Alex", "Sara", "Jane", "Layla", "Ying", "Amit", "Alan", "Ali", "Megan"],
  "UofA": ['Ying', 'Alex', 'Megan', 'Amit', 'Sara', 'Jane', 'Tom', 'Alan', 'Layla', 'Ali'], 
  "OT": ['Alex', 'Jane', 'Megan', 'Ying', 'Sara', 'Layla', 'Ali', 'Tom', 'Amit', 'Alan'],
  "UofT": ['Alan', 'Amit', 'Ying', 'Megan', 'Ali', 'Sara', 'Tom', 'Alex', 'Layla', 'Jane'], 
  "UBC": ['Tom', 'Layla', 'Alex', 'Megan', 'Jane', 'Sara', 'Ali', 'Alan', 'Ying', 'Amit'], 
  "QU": ['Jane', 'Sara', 'Amit', 'Tom', 'Ali', 'Alan', 'Ying', 'Layla', 'Megan', 'Alex'], 
  "YU": ['Sara', 'Jane', 'Alex', 'Ying', 'Ali', 'Layla', 'Alan', 'Megan', 'Tom', 'Amit'],
  "CU": ['Ying', 'Tom', 'Alan', 'Layla', 'Ali', 'Megan', 'Sara', 'Amit', 'Jane', 'Alex'], 
  "MU": ['Tom', 'Alan', 'Layla', 'Megan', 'Sara', 'Alex', 'Jane', 'Ali', 'Amit', 'Ying'], 
  "UofW": ['Jane', 'Ali', 'Amit', 'Megan', 'Layla', 'Ying', 'Tom', 'Alex', 'Sara', 'Alan']
}

def pref_to_rank(pref):
    return {
        a: {b: idx for idx, b in enumerate(a_pref)}
        for a, a_pref in pref.items()
    }
  
from collections import deque



def gale_shapley(*, A, B, A_pref, B_pref):
    """Create a stable matching using the
    Gale-Shapley algorithm.
    
    A -- set[str].
    B -- set[str].
    A_pref -- dict[str, list[str]].
    B_pref -- dict[str, list[str]].

    Output: list of (a, b) pairs.
    """
    B_rank = pref_to_rank(B_pref)
    ask_list = {a: deque(bs) for a, bs in A_pref.items()}
    pair = {}
    #
    remaining_A = set(A)
    while len(remaining_A) > 0:
        a = remaining_A.pop()
        b = ask_list[a].popleft()
        if b not in pair:
            pair[b] = a
        else:
            a0 = pair[b]
            b_prefer_a0 = B_rank[b][a0] < B_rank[b][a]
            if b_prefer_a0:
                remaining_A.add(a)
            else:
                remaining_A.add(a0)
                pair[b] = a
    #
    return [(a, b) for b, a in pair.items()]

print(gale_shapley(
A = {"Tom", "Sara", "Ali", "Ying", "Amit", "Megan", "Alan", "Layla", "Jane", "Alex"},
B = {"UofO", "UofA", "OT", "UofT", "UBC", "QU", "Y", "CU", "MU", "UofW"},
  A_pref = {
  "Tom": ["UBC", "UofT", "UofW", "UofA", "QU", "OT", "MU", "UofO", "YU", "CU"], 
  "Sara": ["UofO", "QU", "UofT", "MU", "UofA", "UofW", "OT", "YU", "CU", "UBC"], 
  "Ali": ["QU", "UofT", "CU", "OT", "UofO", "MU", "UofA", "YU", "UBC", "UofW"], 
  "Ying": ["MU", "OT", "UofA", "UBC", "QU", "CU", "UofW", "YU", "UofT", "UofO"], 
  "Amit": ["UofT", "YU", "UofA", "OT", "UBC", "UofW", "QU", "UofO", "MU", "CU"],
  "Megan": ["YU", "UofW", "UBC", "UofT", "QU", "UofO", "MU", "OT", "CU", "UofA"], 
  "Alan": ["MU", "YU", "CU", "UofO", "UofA", "UofT", "UBC", "QU", "OT", "UofW"], 
  "Layla": ["UofT", "UofA", "MU", "CU", "YU", "UBC", "QU", "UofW", "OT", "UofO"],
  "Jane": ["OT", "UofO", "UofA", "MU", "YU", "UofT", "QU", "UBC", "UofW", "CU"],
  "Alex": ["UofW", "UofO", "OT", "MU", "YU", "UofT", "UBC", "CU", "QU", "UofA"]
  },
  B_pref = {
  "UofO": ["Tom", "Alex", "Sara", "Jane", "Layla", "Ying", "Amit", "Alan", "Ali", "Megan"],
  "UofA": ['Ying', 'Alex', 'Megan', 'Amit', 'Sara', 'Jane', 'Tom', 'Alan', 'Layla', 'Ali'], 
  "OT": ['Alex', 'Jane', 'Megan', 'Ying', 'Sara', 'Layla', 'Ali', 'Tom', 'Amit', 'Alan'],
  "UofT": ['Alan', 'Amit', 'Ying', 'Megan', 'Ali', 'Sara', 'Tom', 'Alex', 'Layla', 'Jane'], 
  "UBC": ['Tom', 'Layla', 'Alex', 'Megan', 'Jane', 'Sara', 'Ali', 'Alan', 'Ying', 'Amit'], 
  "QU": ['Jane', 'Sara', 'Amit', 'Tom', 'Ali', 'Alan', 'Ying', 'Layla', 'Megan', 'Alex'], 
  "YU": ['Sara', 'Jane', 'Alex', 'Ying', 'Ali', 'Layla', 'Alan', 'Megan', 'Tom', 'Amit'],
  "CU": ['Ying', 'Tom', 'Alan', 'Layla', 'Ali', 'Megan', 'Sara', 'Amit', 'Jane', 'Alex'], 
  "MU": ['Tom', 'Alan', 'Layla', 'Megan', 'Sara', 'Alex', 'Jane', 'Ali', 'Amit', 'Ying'], 
  "UofW": ['Jane', 'Ali', 'Amit', 'Megan', 'Layla', 'Ying', 'Tom', 'Alex', 'Sara', 'Alan']
  },
))