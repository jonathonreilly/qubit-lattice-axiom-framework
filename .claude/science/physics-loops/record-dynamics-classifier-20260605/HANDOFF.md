# Handoff - Record Dynamics Classifier

## Summary

This cycle creates a bounded dynamics classifier after the Record axiom reset.
It accepts the user's corrected target: the framework does not need to force
Koide; it needs to show Koide is a stable setting on a dial under a physically
selected dynamics class.

## Files

- `docs/GENERATION_DIAL_DYNAMICS_STABILITY_CLASSIFIER_2026-06-05.md`
- `docs/RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md`
- `docs/GENERATION_DIAL_LOCAL_STABILITY_GRAMMAR_2026-06-05.md`
- `scripts/generation_dial_dynamics_stability_classifier_2026_06_05.py`
- `scripts/record_function_finite_sector_algebra_2026_06_05.py`
- `scripts/generation_dial_local_stability_grammar_2026_06_05.py`
- `logs/runner-cache/generation_dial_dynamics_stability_classifier_2026_06_05.txt`
- `logs/runner-cache/record_function_finite_sector_algebra_2026_06_05.txt`
- `logs/runner-cache/generation_dial_local_stability_grammar_2026_06_05.txt`
- `.claude/science/physics-loops/record-dynamics-classifier-20260605/`

## Result

Runner results:

- Record-function algebra: PASS=18 FAIL=0.
- Local stability grammar: PASS=13 FAIL=0.
- Dynamics classifier: PASS=26 FAIL=0.

Review PR:
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2700

Main content:

- Exact dial: `r(s)=2^(s-1)`, `Q(s)=1/3+(2/3)r(s)`.
- Two-sector entropy ascent stabilizes `s=0` (`r=1/2`, `Q=2/3`).
- Reverse branch `r -> sqrt(r/2)` gives `s' = s/2`, so `s=0` is stable.
- Sharpening `r -> 2r^2` gives `s' = 2s`, so `s=0` is repelling.
- Real-mode entropy ascent stabilizes `s=1`.
- Heat-kernel path crosses `s=0` as transit.

## Next exact action

Audit the three bounded scaffold rows. Then target the remaining physical
partition/arrow gate: why the charged-lepton record should use the two-sector
entropy arrow rather than real-mode/Born entropy, sharpening, or transit.

## Honest classification

Bounded theorem / dynamics proposal. Physical `Q=2/3` selection remains open
until a native two-sector entropy-arrow derivation exists.
