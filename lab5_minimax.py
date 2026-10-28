"""Lab 5: Minimax and alpha-beta pruning with leaf-evaluation counters.

The actual supplied tree was not attached in the prompt, so TREE below is a
clearly documented example. Replace its leaf values/branch order with the
course tree before submission if it differs.
"""
from copy import deepcopy

# Root is MAX; A, B and C are MIN nodes. Each child value is a terminal leaf.
TREE = {
    "A": [3, 5, 6],
    "B": [2, 9, 1],
    "C": [0, -1, 7],
}
TREE_REORDERED = {
    "A": [6, 5, 3],   # same minimum as A
    "B": [9, 2, 1],   # same minimum as B, less favorable ordering
    "C": [7, 0, -1],  # same minimum as C, less favorable ordering
}
# A branch order that puts low values early under MIN can prune sooner.
TREE_BETTER_ORDER = {
    "A": [3, 5, 6],
    "B": [2, 9, 1],
    "C": [0, -1, 7],
}

def minimax(tree):
    count = 0
    trace = []
    child_values = {}
    for name, leaves in tree.items():
        values=[]
        for i, value in enumerate(leaves, 1):
            count += 1
            values.append(value)
            trace.append(f"Evaluate leaf {name}{i} = {value}")
        child_values[name] = min(values)  # each child is MIN
        trace.append(f"MIN node {name} returns {child_values[name]}")
    root_value=max(child_values.values()) # root is MAX
    trace.append(f"MAX root returns max{tuple(child_values.values())} = {root_value}")
    return {"value":root_value,"leaf_evaluations":count,"trace":trace,"child_values":child_values}

def alpha_beta(tree):
    count = 0
    trace = []
    alpha = float("-inf")
    root_value = float("-inf")
    child_values = {}
    for name, leaves in tree.items():
        value = float("inf")  # MIN node; beta is local to this child
        beta = float("inf")
        trace.append(f"Enter MIN node {name} with alpha={alpha}, beta={beta}")
        for i, leaf in enumerate(leaves, 1):
            count += 1
            trace.append(f"Evaluate leaf {name}{i} = {leaf} (leaf count={count})")
            value = min(value, leaf)
            beta = min(beta, value)
            trace.append(f"Update {name}: value={value}, beta={beta}")
            if beta <= alpha:
                skipped = leaves[i:]
                trace.append(f"PRUNE at {name}: beta={beta} <= alpha={alpha}; skipped leaves {skipped}")
                break
        child_values[name] = value
        root_value = max(root_value, value)
        alpha = max(alpha, root_value)
        trace.append(f"Return from {name}: {value}; root best={root_value}; alpha={alpha}")
    trace.append(f"MAX root returns {root_value}")
    return {"value":root_value,"leaf_evaluations":count,"trace":trace,"child_values":child_values}

def show(label, tree):
    print(f"=== {label} ===")
    print("Tree:", tree)
    mm=minimax(tree)
    ab=alpha_beta(tree)
    print(f"Minimax root value: {mm['value']}")
    print(f"Minimax leaf evaluations: {mm['leaf_evaluations']}")
    print(f"Alpha-beta root value: {ab['value']}")
    print(f"Alpha-beta leaf evaluations: {ab['leaf_evaluations']}")
    print(f"Leaves saved by alpha-beta: {mm['leaf_evaluations']-ab['leaf_evaluations']}")
    print("Minimax trace:")
    for line in mm["trace"]: print("  "+line)
    print("Alpha-beta trace:")
    for line in ab["trace"]: print("  "+line)
    assert mm["value"] == ab["value"], "Minimax and alpha-beta must agree"
    return mm,ab

if __name__=="__main__":
    show("Original ordering", TREE)
    show("Reordered leaves", TREE_REORDERED)
    # Edge case: single-leaf MIN branches, no opportunity for within-branch pruning.
    show("Edge case: one leaf per MIN child", {"A":[4],"B":[2],"C":[5]})
