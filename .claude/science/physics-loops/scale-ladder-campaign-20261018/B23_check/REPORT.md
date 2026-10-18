# B23 check

Provenance: a fresh-context checker of the same model family. It rebuilt every letter independently from `B7_check/chk_core.py` (its own gauge, lifts and conventions). b23lib was used only for the gauge dictionary and the stored records. Saved by the supervisor from the hand-back.

**Runs:** `chk_b23.py` PASS=11; `chk_b23_flat_axes.py` PASS=3 (a first-version criterion was too strict for a nodal line).

## Verdicts

- **Gauge dictionary:** exact.
- **Survivors:** 12 of 12 pass all three tests (10 random plus the 2 named closest cases).
  - The k* level is a D₊⊕D₋ 4-fold level whose two blocks are untilted isotropic cones of opposite chirality.
  - The first defective node re-locates at E and is confirmed defective.
- **Stratified defects:** 9 of 9 confirmed. Some "flat" defects are exact nodal lines.
- **Rejections:** 10 of 10 confirmed. Each has a sign change of real r(k) and an explicit bisected crossing.
- **Counts:** all match.
- **Correction:** the 5,458 8-fold levels are pure G3/2, so the "unscreened" bullet was split.
