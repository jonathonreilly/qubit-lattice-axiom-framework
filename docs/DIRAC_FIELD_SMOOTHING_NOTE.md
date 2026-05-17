# Dirac Field Smoothing Note — Finite m₀ = 0.10 Runner Output (Binding)

Date: 2026-04-10 (scope narrowed 2026-05-17 per audited_conditional `scope_too_broad` repair: binding scope is the finite m₀ = 0.10 runner output only; nearby-mass robustness and physical-readout interpretation split out)

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `scope_too_broad`, stating: *"Split the auditable finite
`m0 = 0.10` runner-output statement from the unsupported nearby-mass
robustness and physical-readout interpretation; then re-audit the
broader claim only after adding completed `0.08 / 0.12` logs and a
retained readout bridge."*

This revision implements the splitting. The binding evidence of this
note is exactly the **finite `m0 = 0.10` runner output** from
`scripts/frontier_dirac_walk_3plus1d_field_smoothing_scan.py` on the
declared scan grid (`N ∈ {8..24}` sweep at offset = 3; offset sweep
`{2..6}` at N = 16; baseline `1/(r+0.1)` kernel).

The following are **demoted to out-of-binding-scope** until separately
addressed:
- nearby-mass robustness claims at `m0 ∈ {0.08, 0.12}` — no
  completed runner logs are registered at those mass values;
- physical-readout interpretation (i.e. translating field-smoothing
  behaviour into a physical observable) — requires a separately
  retained Dirac readout bridge that is not supplied here.

This note records the source-field broadening scan in
[`scripts/frontier_dirac_walk_3plus1d_field_smoothing_scan.py`](../scripts/frontier_dirac_walk_3plus1d_field_smoothing_scan.py).

## Setup

- Architecture: 4-component Dirac walk
- Operating point: `n = 29`, `m0 = 0.10`
- Source offset for the N sweep: `3`
- N sweep: `8, 10, 12, 14, 16, 18, 20, 22, 24`
- Offset sweep: `2, 3, 4, 5, 6` at `N = 16`
- Baseline profile: localized inverse-distance kernel `1 / (r + 0.1)`
- Broader controls:
  - softened inverse-distance kernel `1 / (r + 1.0)`
  - Gaussian kernel with `sigma = 3.0`
- Each candidate was rescaled to match the baseline integrated kernel strength on the same lattice and source placement.

## Results At `m0 = 0.10`

### Baseline localized profile

- matched strength: `5.000000e-04`
- kernel sum: `1988.345367`
- N biases:
  `[-6.5974e-12, +1.4238e-08, +3.7648e-09, -1.2380e-09, +1.4669e-10, +3.6893e-10, -6.0910e-10, +5.5181e-10, +7.7030e-10]`
- monotone increasing TOWARD bias over N: `NO`
- offset biases:
  `[-4.5270e-09, +1.4669e-10, +7.0437e-08, +1.0825e-08, -4.4725e-09]`
- TOWARD count: `3/5`
- offset power law: not available because the sign mix prevents a clean fit

### Softened inverse-distance profile

- matched strength: `5.472940e-04`
- kernel sum: `1816.523876`
- N biases:
  `[+1.2650e-09, +8.1856e-09, +2.3096e-09, -5.9860e-10, +2.5213e-10, +1.5936e-10, -5.3973e-10, +4.3390e-10, +7.4438e-10]`
- monotone increasing TOWARD bias over N: `NO`
- offset biases:
  `[-2.7379e-10, +2.5213e-10, +1.1900e-08, +7.8340e-09, +7.3784e-09]`
- TOWARD count: `4/5`
- offset power law: not available because of the sign mix

### Gaussian profile

- matched strength: `2.337921e-03`
- kernel sum: `425.237936`
- N biases:
  `[+8.5728e-08, +9.0220e-08, +2.1594e-08, +9.6070e-10, +7.1611e-09, -2.9615e-09, -1.4386e-08, +8.0078e-09, +1.1359e-08]`
- monotone increasing TOWARD bias over N: `NO`
- offset biases:
  `[+5.0675e-09, +7.1611e-09, +9.3181e-08, +8.5366e-08, +8.4413e-08]`
- TOWARD count: `5/5`
- offset power law: `alpha = 3.053`, `R^2 = 0.8098`

## Nearby Mass Checks

Spot checks at `m0 = 0.08` and `m0 = 0.12` did not restore N monotonicity. In both cases, the Gaussian profile remained the best offset-law candidate, reaching `5/5` TOWARD offsets, while the localized profile still failed the N trend.

## Interpretation

Broadening the source field helps the offset-distance law, and the Gaussian control is clearly better than the current localized profile on that metric. It does not fix the N-monotonicity failure, though, and the nearby mass spot checks did not reveal a better local operating point that changes that conclusion.
