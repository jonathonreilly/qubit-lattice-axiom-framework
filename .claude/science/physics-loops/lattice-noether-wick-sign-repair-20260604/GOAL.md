# Goal

Repair the audited conditional row
`lattice_noether_carrier_independent_bilateral_identity_narrow_theorem_note_2026-05-17`
without adding axioms or editing audit results.

Auditor repair target:

```text
missing_bridge_theorem: derive or explicitly define the Wick-contraction sign
convention for <chi_bar_a chi_b> from the cited Berezin surface, then update
the on-shell convention and runner comments/source consistently.
```

Repair: define the current bilinear
`B_ab := d log det(M)/dM_ab = (M^{-1})_{b,a}` and record that strict ordered
Berezin `<chi_bar_a chi_b>_ord = -B_ab`. Add runner exhibit `E0` verifying the
identity symbolically.

