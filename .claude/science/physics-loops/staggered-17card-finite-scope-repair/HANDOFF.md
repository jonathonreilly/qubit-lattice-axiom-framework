# Handoff

## Target

`staggered_fermion_card_2026-04-11`

## Repair

The note is narrowed to the finite canonical 17-card runner certificate:

```text
scripts/frontier_staggered_17card.py
1D n=61: SCORE 17/17
3D n=9:  SCORE 17/17
3D n=11: SCORE 17/17 with C17 4/6 family gate
3D n=13: SCORE 17/17 with C17 4/6 family gate
```

Screened-Poisson, positive-source, physical-gravity, universal graph-family,
and framework-native staggered-realization claims are removed from the binding
claim.

## Verification

- `bash docs/audit/scripts/run_pipeline.sh` completed after final source-note and runner edits; only the pre-existing Maradudin conditional-repair-prefix warning remained.
- `PYTHONPATH=scripts python3 scripts/frontier_staggered_17card_finite_scope_repair.py | tee outputs/staggered_17card_finite_scope_repair_2026-05-25.txt` -> PASS=27 FAIL=0.
- `python3 -m py_compile scripts/frontier_staggered_17card_finite_scope_repair.py` -> pass.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors; pre-existing warning/notices only.
- `python3 scripts/render_controlled_vocabulary.py --check` -> clean.
- `python3 scripts/vocab_lint.py --report-only docs/STAGGERED_FERMION_CARD_2026-04-11.md .claude/science/physics-loops/staggered-17card-finite-scope-repair/*.md` -> 0 violations.
- `git diff --check` -> pass.
- Runner classification hint: `A=0`, `B=4`, `C=1`, `D=0`, dominant `B`; the wrapper executes the canonical finite runner and parses four `17/17` score blocks.

## Audit queue state

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `deps`: `[]`
- `open_dependency_paths`: `[]`
- `transitive_descendants`: `280`
- `load_bearing_score`: `11.634`
- queue position: `1`
- queue ready: `true`
- criticality: `critical`

## Remaining blockers

The bridge from this finite runner certificate to a physical staggered-gravity theorem remains open.
