# Handoff

## What changed

This block repairs the dimension-5 parity row by narrowing it to formal sign
algebra:

- formal 4x4 Dirac parity conjugation;
- abstract derivative sign character;
- exhaustive enumeration of the four SME-style structures;
- odd total spatial-index count gives P-odd weight;
- even total spatial-index count gives P-even weight.

No lattice-action Lorentz-violation no-go or actual staggered derivative
representative claim is made.

## Files

- `docs/PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md`
- `scripts/frontier_parity_dim5_formal_sign_repair.py`
- `outputs/parity_dim5_formal_sign_repair_2026-05-25.txt`

## Verification

- `bash docs/audit/scripts/run_pipeline.sh`
- `PYTHONPATH=scripts python3 scripts/frontier_parity_dim5_formal_sign_repair.py`
- `python3 -m py_compile scripts/frontier_parity_dim5_formal_sign_repair.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md .claude/science/physics-loops/parity-dim5-formal-sign-repair/*.md`
- `git diff --check`

## Remaining blocker

The branch does not prove how combined staggered parity conjugates the actual
lattice derivative representatives. If audit accepts the rescope, the row
should be judged only as narrowed bounded-support.
