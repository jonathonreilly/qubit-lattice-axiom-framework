# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - no_per_site_bosonic_ccr_theorem_note_2026-05-02
  - q_integer_spectrum_theorem_note_2026-05-02
  - per_site_su2_spin_half_theorem_note_2026-05-02
  - no_per_site_chirality_theorem_note_2026-05-02
source_of_blocker_text: audit_ledger
target_blocker_text: "Old per-site rows imported physical H_x = C^2 / Pauli-module identification through an older uniqueness theorem now scoped away from that bridge."
reachability_to_target: closes
artifact_role: theorem_and_runner_certificate
next_trace_action: "Independent auditor reviews the repaired A1-local statements from the generated audit queue."
```

The direct repair is the dependency swap: the rows no longer ask the older
per-site uniqueness theorem to identify the physical per-site Hilbert space.
They instead use A1's explicit qubit local algebra `M_2(C)` and retained
Pauli-irrep uniqueness only where the Pauli triple itself is load-bearing.

The charge and spin rows are deliberately narrowed:

- `Q_total` is an A1 qubit occupation-count theorem for rank-one readout
  projections, not a physical electric charge theorem.
- `S_i = sigma_i/2` is the local Pauli `su(2)` action, not a derivation of
  the full physical spin generator or spin-statistics.

The bosonic CCR and chirality rows are direct one-site no-go statements in
`M_2(C)`.
