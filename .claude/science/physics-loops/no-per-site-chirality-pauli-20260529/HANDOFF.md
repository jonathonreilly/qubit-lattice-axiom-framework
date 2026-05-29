# Handoff

This branch repairs `no_per_site_chirality_theorem_note_2026-05-02` by
narrowing it to the algebra the runner actually proves: inside a supplied
complex Pauli `M_2(C)` representation of `Cl(3)`, no nonzero matrix
anticommutes with all three Pauli generators, so no `gamma_5` involution exists
inside that carrier.

The previous source text claimed the framework-level physical carrier
identification `H_x ~= C^2`. Audit held that bridge conditional. This branch
does not use that bridge.

Verification:

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

No new axioms, observed targets, external comparators, or audit-status claims
are introduced.
