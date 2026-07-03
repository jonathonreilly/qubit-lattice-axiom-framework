# Gauge-Vacuum Plaquette Word-Limit Box/Mode Sweep Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite word-limit diagnostics for the eta-weighted
word-count reduction at `beta = 6`.  The sweep varies the word-packet
dominant-weight box and Bessel mode support, then varies the source box
independently at fixed word packet.  It does not claim an untruncated Wilson
environment, a physical 3D rim computation, an analytic `P(6)`, a fit, an
extrapolated limit, or canonical repinning.

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:** [scripts/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.py](../scripts/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.txt](../logs/runner-cache/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.txt)

## Load-Bearing Inputs

- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
  supplies the finite tensor-word/source Perron readout surface used by this
  sweep.
- [GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the finite-packet theta identity used as the ratio diagnostic.

```yaml
claim_id: gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_note_2026-06-12
claim_type_author_hint: bounded_theorem
runner_path: scripts/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.py
audit_authority: independent audit lane only
declared_one_hop_deps:
  - gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_bounded_note_2026-06-11
  - gauge_vacuum_plaquette_word_count_theta_identification_two_term_asymptotic_narrow_theorem_note_2026-06-12
proposal_allowed: false
audit_required_before_effective_retained: true
```

## Setup

The runner uses the finite tensor-word packet

```text
tensor_word = diag(D) M diag(D) M^T diag(D),
M = N_f + N_fbar,
D_(p,q) = c_(p,q)(6) / (d_(p,q) c_(0,0)(6)).
```

For each word-packet cell it recomputes `eta_inf`, forms the Route B
eta-weighted finite-rank reduction, evaluates `P_k` through `k = 40`, and
reports `P_inf` as the fundamental/antifundamental pair-support source Perron
limit.  The `k = 40` value is checked against that limit in every cell.

The theta diagnostic is recomputed from the W29 closed form

```text
theta = (L_eta(f) / L_eta(0)) * sqrt(D_f / d_f) * t(f,0) / t(0,0),
```

and compared with the measured finite mid-tail increment ratio.

## Word-Box And Mode Sweep

Fixed source readout: `source NMAX = 7`, `source MODE_MAX = 200`.

| word NMAX | MODE_MAX | word box | theta | measured ratio | P_inf | P40 error | distance to 0.5934 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 80 | 16 | 0.263745855986681 | 0.263711666964916 | 0.615191992185898 | 2.220e-16 | 0.021791992185898 |
| 3 | 200 | 16 | 0.263745855986681 | 0.263711666964916 | 0.615191992185898 | 2.220e-16 | 0.021791992185898 |
| 4 | 80 | 25 | 0.263745855973467 | 0.263714844278881 | 0.615191992185898 | 4.441e-16 | 0.021791992185898 |
| 4 | 200 | 25 | 0.263745855973467 | 0.263714844278881 | 0.615191992185898 | 4.441e-16 | 0.021791992185898 |
| 5 | 80 | 36 | 0.263745855973467 | 0.263714870591533 | 0.615191992185898 | 0.000e+00 | 0.021791992185898 |
| 5 | 200 | 36 | 0.263745855973467 | 0.263714870591533 | 0.615191992185898 | 0.000e+00 | 0.021791992185898 |
| 6 | 80 | 49 | 0.263745855973467 | 0.263714844278881 | 0.615191992185898 | 4.441e-16 | 0.021791992185898 |
| 6 | 200 | 49 | 0.263745855973467 | 0.263714844278881 | 0.615191992185898 | 4.441e-16 | 0.021791992185898 |
| 7 | 80 | 64 | 0.263745855973467 | 0.263714855724793 | 0.615191992185898 | 4.441e-16 | 0.021791992185898 |
| 7 | 200 | 64 | 0.263745855973467 | 0.263714855724793 | 0.615191992185898 | 4.441e-16 | 0.021791992185898 |

Computed spans:

```text
word-axis P_inf span = 0.000000000000e+00
word-axis P40 span   = 4.440892098501e-16
theta span           = 1.321337483873e-11
```

The word-box and mode axes do not move the computed word-limit value toward
the fenced comparator in these cells.  The distance remains
`0.021791992185898`.

## Source-Box Sweep

Fixed word packet: `word NMAX = 4`, `word MODE_MAX = 80`.
Fixed source mode support: `SOURCE_MODE_MAX = 200`.

| source NMAX | P_inf | P40 error | distance to 0.5934 |
|---:|---:|---:|---:|
| 5 | 0.615191040446003 | 1.110e-16 | 0.021791040446003 |
| 7 | 0.615191992185898 | 4.441e-16 | 0.021791992185898 |
| 9 | 0.615191992282189 | 0.000e+00 | 0.021791992282189 |

Computed source-box drift:

```text
source-box P_inf span over NMAX=5,7,9 = 9.518361862026e-07
source NMAX 5->7 drift = +9.517398950054e-07
source NMAX 7->9 drift = +9.629119723797e-11
```

This source-box sensitivity is far smaller than the fenced comparator distance
in the measured cells.

## Verdict Diagnostic

Within this finite sweep, the dominant-weight word box and tensor-word
Bessel-mode support do not account for the `0.021791992185898` distance from
the fenced comparator.  The source-box sweep changes the value by about
`9.52e-7` over `NMAX = 5, 7, 9`, also not enough to account for that distance.

The residual named by this sweep is the structural 1D word-chain versus 3D
rim-geometry target.  This note does not retire that target.

No Richardson-style word-axis extrapolation is emitted as a load-bearing
quantity, because the computed `P_inf` cells are identical at the `1e-12`
scale.  Any such extrapolation would be a non-load-bearing diagnostic only.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=47, FAIL=0
```

Refresh the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```

Named residuals: finite dominant-weight box; finite Bessel mode support;
source-box truncation; finite word count checked through `k = 40`; no physical
3D unmarked spatial Wilson environment computation; no all-weight or
untruncated convergence proof; no `L_perp` limit; no analytic `P(6)`; no
canonical repinning.
