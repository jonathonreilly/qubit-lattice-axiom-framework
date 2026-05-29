# Claim Status Certificate

Actual current-surface status: `proposed_retained`

Independent audit remains required before any effective retained status
lands. This PR does not apply audit verdicts and does not retag the ledger
manually.

| Claim | Proposed status | Reason | Boundary |
|---|---|---|---|
| `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | `proposed_retained` no-go | finite trace obstruction in A1 `M_2(C)` | no statement about collective/effective bosons |
| `q_integer_spectrum_theorem_note_2026-05-02` | `proposed_retained` positive theorem | rank-one qubit projection sums have integer spectrum | not physical electric charge/hypercharge/Noether charge |
| `per_site_su2_spin_half_theorem_note_2026-05-02` | `proposed_retained` positive theorem | Pauli action `S_i = sigma_i/2` is the unique two-dimensional `j=1/2` module | not full physical spin generator or spin-statistics |
| `no_per_site_chirality_theorem_note_2026-05-02` | `proposed_retained` no-go | no `gamma_5` in `M_2(C)` anticommutes with all three Pauli generators | larger spacetime/multi-site chirality remains separate |

Pipeline result after regeneration:

- all four rows: `audit_status: unaudited`, `effective_status: unaudited`
- all four rows: present as ready entries in `docs/audit/data/audit_queue.json`
- `no_per_site_chirality_theorem_note_2026-05-02`: queue rank #1, critical,
  876 descendants

Bare `retained` is not used as a branch-local status.
