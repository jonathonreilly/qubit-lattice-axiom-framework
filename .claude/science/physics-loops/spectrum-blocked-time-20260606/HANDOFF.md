# Handoff

This branch repairs the spectrum-condition blocked-time normalization blocker.

The source row imported the two-step object `T := T_hat^2` but still wrote
`H = -(1/a_tau) log(T/M_T)` and used the same one-step factor for `m_gap`.
The already-present bridge note proves that `T_hat^2` advances `2 a_tau`, so
the correct reconstruction is:

```text
H = -(1/(2 a_tau)) log(T/M_T)
m_gap = -(1/(2 a_tau)) log(lambda_1/M_T)
```

The primary runner now constructs `T = exp(-2 a_tau H_lat)`, reconstructs with
`1/(2 a_tau)`, and checks that the old normalization is exactly twice the
correct Hamiltonian. The output file and runner cache were refreshed.

Remaining boundary:

- SC3 is still conditional on top-eigenvalue nondegeneracy.
- SC4 is still a temporal corollary conditioned on a supplied transfer gap.
- The audit/review loop must decide whether the repaired row can move out of
  `audited_conditional`.
