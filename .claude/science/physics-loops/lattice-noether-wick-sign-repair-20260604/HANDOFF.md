# Handoff

Branch: `physics-loop/lattice-noether-wick-sign-repair-20260604`

Target:
`lattice_noether_carrier_independent_bilateral_identity_narrow_theorem_note_2026-05-17`

What changed:

- Defined the current-bilinear convention
  `B_ab := d log det(M)/dM_ab = (M^{-1})_{b,a}`.
- Stated the strict ordered Berezin sign:
  `<chi_bar_a chi_b>_ord = -B_ab`.
- Added runner exhibit `E0` to verify the sign relation symbolically on a
  generic `2 x 2` matrix.
- Updated runner comments/source consistently.
- Refreshed
  `logs/runner-cache/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.txt`.

Checks:

```text
python3 scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py
python3 -m py_compile scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py
git diff --check
```

Remaining residual:

```text
Parent physical identification of the generic carrier M with M_KS remains out of scope.
```

