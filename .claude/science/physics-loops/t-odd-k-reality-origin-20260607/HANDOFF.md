# Handoff

## What Changed

This block adds an exact finite classifier for T-odd/K-odd Hermitian
generation-factor operators on the supplied `C3` carrier.

Main result:

```text
T-odd noncommuting generation selector
  <=> supplied C3-breaking singlet-doublet bridge vector.
```

The C3-invariant K-odd line is only `A=i(C-C^2)`, which commutes with `S` and
was already route-pruned. C3 averaging kills the bridge component.

## Files

- `docs/T_ODD_K_REALITY_SOURCE_SPACE_CLASSIFIER_NO_GO_NOTE_2026-06-07.md`
- `scripts/frontier_t_odd_k_reality_source_space_classifier.py`
- `logs/runner-cache/frontier_t_odd_k_reality_source_space_classifier.txt`
- `.claude/science/physics-loops/t-odd-k-reality-origin-20260607/*`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_t_odd_k_reality_source_space_classifier.py
```

Expected: `TOTAL: PASS=19 FAIL=0`.

## Reviewer Focus

- Confirm the K-odd Hermitian space split is stated only on the finite
  generation carrier.
- Confirm the note does not claim K-reality is impossible.
- Confirm the live route is correctly left open: derive the C3-breaking doublet
  vector from same-source physics or a spin-generation-entangled carrier.
