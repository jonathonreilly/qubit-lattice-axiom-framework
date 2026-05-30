# Handoff

Cycle 1 produced an exact no-go for the current P1' residual if P1' is
interpreted as the standard staggered `epsilon` index on finite even periodic
`Z^4` tori.

The proof is the square bipartite block identity:

```text
D = [[0,B],[-B^dag,0]],  B square
=> D^dag D = diag(BB^dag, B^dagB)
=> Tr(eps exp(-tD^dagD)) = 0.
```

Verification:

```text
python3 scripts/frontier_abj_epsilon_index_square_block_no_go.py
TOTAL: PASS=45 FAIL=0
```

This does not close the 3+1 lane.  It narrows the next positive work to one of:

1. taste-singlet/Adams staggered index permission theorem;
2. finite local Wess-Zumino/cohomology anomaly-to-inconsistency proof;
3. framework-admissible non-flat/imbalanced complex;
4. explicit bounded composition using ABJ as a named accepted premise.

Recommended next block: taste-singlet/Adams staggered index permission theorem,
because it stays closest to the current staggered substrate while escaping the
square-block `epsilon` no-go.
