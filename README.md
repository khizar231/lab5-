# CAI601400 — Artificial Intelligence Lab 5: Minimax and Alpha-Beta

## Important tree assumption
The prompt refers to a supplied tree, but no tree diagram or leaf values were attached. `lab5_minimax.py` therefore contains an explicit, reproducible example tree. Replace the leaf values and branch order with the exact course tree before submission if it differs.

## Example tree
Root is MAX; A, B and C are MIN nodes.
- A: [3, 5, 6] → MIN(A)=3
- B: [2, 9, 1] → MIN(B)=1
- C: [0, -1, 7] → MIN(C)=-1
Root value = max(3, 1, -1) = 3.

The reordering experiment keeps every branch's leaf values unchanged and changes only the order in which leaves are visited:
- A: [6, 5, 3]
- B: [9, 2, 1]
- C: [7, 0, -1]

## Run
Requires Python 3.10+; no third-party dependencies.
```bash
python lab5_minimax.py
```

## Counting convention
A leaf evaluation is counted each time an algorithm visits/evaluates a terminal value. Pruned leaves are not counted by alpha-beta. Minimax evaluates every leaf. The root is MAX and its children are MIN.

## Files
- `lab5_minimax.py` — Minimax and alpha-beta, trace output, counters and assertions.
- `Lab5_Report.docx` — hand trace, comparison, edge case, reflection.
- `outputs.txt` — captured console output.

## Submission
Verify the example tree against the course handout. Upload source, report, README and outputs to your GitHub lab folder, commit changes, and submit the repository URL plus final commit identifier. Give the instructor access. Do not upload credentials, private information or virtual environments.
