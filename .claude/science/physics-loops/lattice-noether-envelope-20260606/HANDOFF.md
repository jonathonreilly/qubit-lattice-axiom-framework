# Handoff

## Summary

This PR repairs the new audited conditional Noether row by replacing the
overbroad "arbitrary bilinear gives nearest-neighbour current" wording with a
support-envelope theorem.

For arbitrary `c_xy`, the current on pair `{p,q}` uses only `c_pq` and `c_qp`;
if both vanish, that pair current vanishes. Therefore Noether preserves the
Hamiltonian support envelope. Nearest-neighbour current support is claimed only
for the admitted staggered nearest-neighbour carrier.

The PR also reconciles the `i` convention:

- the variational current for anti-Hermitian `t=i` is imaginary;
- the physical Hermitian number-current in the continuity equation is
  `J_num = i j_var`, giving the source formula's `-1/2` prefactor;
- runner C2 now uses the same `-1/2` convention as the note.

## Verification

```text
python3 scripts/audit_companion_lattice_noether_onsite_internal_2026_06_05.py
TOTAL: 14 PASS / 0 FAIL
```

```text
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_lattice_noether_onsite_internal_2026_06_05.py --check-only --allow-non-main
All relevant caches are fresh.
```

## Boundaries

- No new axioms.
- No audit ledger/result edits.
- Site-mixing generators remain out of scope.
- The admitted staggered carrier remains admitted context, not rederived here.
