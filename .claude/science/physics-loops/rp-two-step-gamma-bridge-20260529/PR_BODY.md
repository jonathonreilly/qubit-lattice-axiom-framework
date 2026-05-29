## Summary

Repairs the critical audited-conditional free staggered two-step RP positivity
row by deriving the missing free-fermion transfer bridge inside the packet.

The auditor accepted the action-derived two-step dispersion and positivity
checks, but conditioned retention on an in-packet derivation of the decaying
mode and `Gamma(t1)` bridge. This PR adds that bridge directly to the registered
runner and source note.

## Science Boundary

- no new axioms
- no observed target values
- no fitted selectors
- no external comparator
- no gauge-background closure claim
- no author-applied audit promotion

## Added Bridge

- constructs the decaying spectral projector for `T_odd T_even`;
- proves the positive-time one-particle kernel is `e^{-2E}`;
- builds finite exterior-algebra `Gamma(K)` on occupation wedges;
- checks `Gamma(K) a_p^dag = t_p a_p^dag Gamma(K)`;
- checks `Gamma(K)=B^dag B` and positive Hermitian Fock transfer.

## Verification

```text
python3 -m py_compile scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py
python3 scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

Key runner readout:

```text
C5 Gamma bridge: PASS
projector residual: 3.4e-15
wedge=tensor error: 3.5e-18
intertwiner error: 3.5e-18
PASS=5 FAIL=0
```

Audit queue readout after pipeline regeneration:

```text
axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28
rank: 1
ready: true
queue_reason: unaudited
criticality: critical
deps: []
runner classification: C=15
```

## Target Row

`axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28`

The branch is intended to reset this row for independent re-audit. It does not
retag the ledger as retained.
