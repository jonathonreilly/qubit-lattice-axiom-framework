# Handoff

This branch repairs the audited-conditional
`axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` row by
adding the missing bridge theorem inside the packet.

The auditor accepted the staggered two-step calculation and positivity checks,
but held the row conditional because the source asserted the free-fermion
`Gamma(t1)` transfer bridge as a standard relation. The runner now derives and
checks the bridge directly:

- action-derived `T_odd T_even` is split by the decaying spectral projector
  `P_-`, selecting `e^{-2E}`;
- finite exterior-algebra `Gamma(K)` is built on occupation-basis wedges;
- the creation-operator intertwiner
  `Gamma(K) a_p^dag = t_p a_p^dag Gamma(K)` is checked;
- `Gamma(K)=B^dag B` and positivity are verified on finite Fock carriers.

Verification:

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

No new axioms, observed targets, external comparators, or audit-status claims
are introduced.
