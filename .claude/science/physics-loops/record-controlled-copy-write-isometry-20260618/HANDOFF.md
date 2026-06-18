# Handoff

## Target

`record_formation_to_kraus_isometry_bridge_2026-06-06`

Current audit blocker:

```text
missing_bridge_theorem: derive the ideal pointer-label record-write isometry from the finite controlled-copy/fresh-fragment dynamics, or narrow the ledger scope to the already-supplied projective write premise.
```

## What This Branch Does

Adds `RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`, proving that for the explicit finite controlled-copy model:

```text
U_cc(pi/4)(|psi>|0>) = P_0|psi>|eta_0> + P_1|psi>|eta_1>
<eta_0|eta_1> = 0
C_R|eta_r> = |r>
W|psi> = P_0|psi>|0> + P_1|psi>|1>
K_r = <r|W = P_r
```

The existing record-to-Kraus bridge now cites this theorem and its runner checks the new source-side bridge.

## What This Branch Does Not Do

- Does not audit.
- Does not retag the ledger.
- Does not land to main.
- Does not edit audit/status surfaces.
- Does not claim retained or proposed retained status.
- Does not derive arbitrary persistent dynamics to `W`.
- Does not derive the quantum-Darwinism record reading from Minimal Axioms.
- Does not derive Born probabilities or downstream selectors.

## Verification

```text
python3 scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py
python3 scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
python3 -m py_compile scripts/frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py scripts/frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py
git diff --check
```

Latest direct runner results before packaging:

- `frontier_record_formation_controlled_copy_write_isometry_2026_06_18.py`: `PASS=40 FAIL=0`
- `frontier_record_formation_to_kraus_isometry_bridge_2026_06_06.py`: `PASS=75 FAIL=0`

## Next Action

Reviewer should inspect the source-side theorem and decide whether the repair is suitable for independent audit re-run of the bounded support row.
