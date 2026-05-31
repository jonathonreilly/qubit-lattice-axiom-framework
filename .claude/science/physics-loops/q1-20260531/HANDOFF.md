# Handoff

This draft PR is for workers on the `Q = 2/3` Koide hunt.

What to use:

- The `Q=1` source matrix is exact and exposes offsite `-2/9`.
- Strict onsite descent erases the reduced `Z` coordinate and returns
  effective `Q=2/3`.
- The repeated `2/9` footprint is real as `2/d^2` arithmetic.
- APS eta is exact at the forced `d=3` surface.
- The bridge `coeff_nonid(S_Q1) = -eta_APS` is now exact.
- Q1-alone signed readout is no-go: the source is transposition-even, while
  `delta` is transposition-odd.
- The unlock map splits the positive targets cleanly: strict onsite
  source-domain selection gives charged-lepton `Q=2/3`, while the Q1 offsite
  source shadow gives APS/Brannen magnitude `2/9`.
- If a future odd orientation/basepoint primitive supplies
  `epsilon in {+1,-1}`, then `delta = epsilon * eta_APS` can feed the existing
  selected-line scalar/point bridge.

What not to use:

- Do not cite this as dark matter.
- Do not cite this as retained `Q=2/3` closure.
- Do not cite this as `delta = eta_APS`.
- Do not cite Q1 as fixing the sign of `delta`.
- Do not merge the APS, anomaly, Brannen, and offsite matrix coefficient into
  full physical phase closure without a signed selected-line readout theorem.

Best next theorem:

```text
derive_signed_selected_line_orientation_or_source_domain_Z_erasure
```
