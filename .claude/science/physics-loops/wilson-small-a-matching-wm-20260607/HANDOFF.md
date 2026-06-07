# Handoff

This PR targets the `beta_gbare` conditional blocker by adding a source theorem
for the exact Wilson small-`a` coefficient matching:

```text
S_W = beta sum_p (1 - Re Tr U_p / N_c)
Tr(T_a T_b)=delta_ab/2
=> beta = 2 N_c / g_bare^2.
```

Reviewer focus:

- Check the factor of two from summing unordered plaquette planes against
  `(1/4) F_{mu nu}F_{mu nu}`.
- Check that the note does not claim Wilson action-surface selection.
- Check that the downstream `beta_gbare` row remains audit-owned and only
  gains a one-hop source packet for `WM`.

Verification:

```text
PYTHONPATH=scripts python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py
PYTHONPATH=scripts python3 scripts/frontier_beta_gbare_squared_rescaling_invariance.py
```
