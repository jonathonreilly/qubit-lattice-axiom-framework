# No-Go Ledger

- A max clique size of 30 from min-degree/min-fill gives a treewidth upper
  bound of 29, not a lower bound. Do not write this as a global infeasibility
  theorem.
- The 4 GiB truncation threshold is about `1.91`, but the nearest admissible
  integer less than or equal to that threshold remains `1`. This repairs the
  arithmetic without creating a nontrivial truncation route.
- This block cannot close the gauge-scalar bridge because it does not compute
  `<P>(beta=6)` and does not provide a new exact contraction engine.
