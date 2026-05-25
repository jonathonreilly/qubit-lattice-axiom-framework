# Handoff

## Summary

This block repairs `fermion_parity_z2_grading_theorem_note_2026-05-02` by
separating the algebraic parity theorem from the lattice-Noether current row.

`Q_hat_total` is now defined directly as `sum_x n_hat_x`; the runner checks
the parity involution, spectrum, even/odd dimension split, odd action on
single fermion operators, and even action on bilinears. Hamiltonian
conservation is stated only as conditional on Z2-even dynamics.

## Pipeline Result

After `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_id: fermion_parity_z2_grading_theorem_note_2026-05-02
claim_type: positive_theorem
audit_status: unaudited
effective_status: unaudited
deps: []
ready: true
audit_queue_rank: 2
transitive_descendants: 890
```

## Runner

```text
OVERALL: PASS
tests: 7 / 7
```
