# Handoff

This block adds the missing Wilson-action normalization transformation theorem
requested by the audit ledger for the `g_bare` rescaling row.

Core result:

```text
T'_a = c T_a,  g' T'_a = g T_a
=> g'^2 = g^2/c^2
=> beta' = 2 N_c/g'^2 = c^2 beta
=> beta' g'^2 = beta g^2 = 2 N_c.
```

What it moves:

- The rescaling row now has a direct theorem for `beta_new/beta_old`.
- The constraint row now cites the Wilson small-a matching theorem for WM.

What remains open:

- Wilson action-surface selection.
- Local beta=6 derivation.
- Independent audit/effective-status decisions.
