# Handoff

This branch repairs the Observable parent P2 blocker on the finite source
surface the parent actually consumes.

The key theorem is finite-dimensional:

```text
D^T = -D, S positive diagonal
S + D = S^(1/2) (I + S^(-1/2) D S^(-1/2)) S^(1/2)
det(S + D) > 0
```

For the local derivative patch, `D` is invertible and small real diagonal
sources keep `det(D+tJ)` nonzero by the Neumann bound, so the determinant
sign cannot cross zero. Thus `det(D+J)` is real-positive on the branch the
parent differentiates, and `log det = Re Log det = log|det|`.

The parent note now states the live load-bearing surface as Record/P1 plus the
finite real-positive source branch, not Record/P1 plus admitted P2.

Remaining boundary:

- Global/off-sector P2 for arbitrary complex sources is not derived.
- `AC_phi_lambda`/Berezin determinant identification remains separate where a
  downstream row needs it.
- The audit/review loop must decide whether this closes the row.
