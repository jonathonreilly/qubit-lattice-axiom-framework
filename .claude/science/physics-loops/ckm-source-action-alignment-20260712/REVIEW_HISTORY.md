# Review history

## Pre-review deep fanout — 2026-07-12

1. Residual-symmetry route: exact fixed-spectrum `Z_2` counterfamily spans
   overlap `[0,1]`; full `S_3` degenerates and shared `C_3` co-diagonalizes.
2. Determinant/variational route: exact `18`-dimensional composite has
   `det Z=t^3R^-5`; volume-mode suppression uniquely forces the desired law,
   while natural trace-spectral actions fail.
3. Inverse-spectral route: Jacobi/NNI spectra leave spectral weights,
   coefficients, and relative phases free; the exact coefficient needed for
   the law simply restates a new source rule.

Initial runner result:
`SUMMARY: EXACT_PASS=21 BOUNDARY_PASS=19 FAIL=0`.

## Review-loop iteration 1

- Code/runner: RISK; core equations passed, but the action domain,
  affine-distance proof, generic action scope, Jacobi check, and NNI branch
  needed stronger artifacts.
- Physics/Nature/labeling: BOUNDED / BOUNDED / PASS; the determinant encoding
  needed explicit circularity and selector disclosure.
- Imports/governance/no-go discipline: FIX / FIX / FAIL; the bundled selector
  wall and narrative N1-N8 evidence were split and rebuilt.

## Review-loop iteration 2

All verified findings were fixed and only changed files were re-reviewed.

- Code/runner: PASS, including independent affine-distance projection,
  general block powers, strict Jacobi counterfamily, orbital variation, and
  direct NNI branch control.
- Physics claim: PASS WITH BOUNDED CLAIMS; physical target OPEN.
- Nature retention: BOUNDED.
- Import support: DISCLOSED and bounded.
- Labeling convention: PASS.
- Repository governance: PASS.
- No-go discipline: PASS on the corrected five-wall N1-N8 packet.

Final runner result:
`SUMMARY: EXACT_PASS=27 BOUNDARY_PASS=24 FAIL=0`.

No reviewer applied an audit verdict. Audit compatibility validation remains
pending.

## Audit compatibility validation

The validation pipeline recognized the new leaf row
`ckm_composite_positive_volume_alignment_source_action_boundary_note_2026-07-12`
as `bounded_theorem`, `unaudited`, with the stacked parent, retained
residual-`Z_2`, minimal-axiom, and retained `S_3` boundary dependencies plus
the paired runner. It also seeded the unlanded stacked parent row, for two new
rows total. Strict lint passed with no errors (31 existing warnings and 248
notices). All generated audit, publication, and front-door outputs were
restored from the intended block-02 base and are absent from the source diff.
