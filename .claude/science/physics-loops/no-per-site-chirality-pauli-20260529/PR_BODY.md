## Summary

Repairs the audited-conditional `no_per_site_chirality` row by narrowing it to
the supplied-Pauli `M_2(C)` no-go the runner proves.

The prior source text depended on a framework-level carrier bridge
`H_x ~= C^2`. This branch removes that load-bearing identification and keeps
only the exact finite algebra statement:

- `sigma_1 sigma_2 sigma_3 = i I`;
- no nonzero `M in M_2(C)` anticommutes with all three `sigma_i`;
- no `gamma_5` involution exists inside the supplied Pauli carrier.

## Science Boundary

- no new axioms
- no framework-H_x carrier identification
- no physical chirality mechanism claim
- no Standard Model left/right assignment claim
- no author-applied audit promotion

## Verification

```text
python3 -m py_compile scripts/no_per_site_chirality_check.py
python3 scripts/no_per_site_chirality_check.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

Key runner readout:

```text
Test 4 (no M anticommutes with all sigma_i): PASS
Test 5 (no gamma5 candidate exists): PASS
Test 6 (even/odd subalgebras coincide on Pauli): PASS
OVERALL: PASS
```

Audit queue readout after pipeline regeneration:

```text
no_per_site_chirality_theorem_note_2026-05-02
rank: 1
ready: true
queue_reason: unaudited
criticality: critical
deps: []
runner classification: C=6
```

## Target Row

`no_per_site_chirality_theorem_note_2026-05-02`

The branch is intended to reset this row for independent re-audit. It does not
retag the ledger as retained.
