# Born Lane Comparison Note

**Date:** 2026-04-02  
**Status:** complete, bounded comparison

This note compares the two best bounded unitary lanes on the same corrected
Sorkin harness:

- modular gap + layer normalization
- central-band `|y|` removal + layer normalization

Script:
[scripts/born_compare_modular_central_ln.py](/Users/jonreilly/Projects/Physics/scripts/born_compare_modular_central_ln.py)

## Setup

- `N = 25, 40, 60`
- `npl = 25`
- same seed set across both lanes
- corrected Sorkin metric with `-P(empty)`
- `gap = 2.0`
- `y_cut = 2.0`

## Strongest retained rows

Numbers below are synced to the current runner stdout (runner hash
`c95402c8307b...`).

### Modular gap + LN

| N | pur_min | mean `|I3|/P` | max `|I3|/P` | seeds |
|---|---:|---:|---:|---:|
| 25 | `0.908` | `4.67e-16` | `1.44e-15` | 8 |
| 40 | `0.958` | `2.78e-16` | `7.77e-16` | 8 |
| 60 | `0.957` | `1.80e-16` | `4.44e-16` | 7 |

### Central-band `|y|<2` + LN

| N | pur_min | mean `|I3|/P` | max `|I3|/P` | seeds | removed |
|---|---:|---:|---:|---:|---:|
| 25 | `0.942` | `4.44e-16` | `8.88e-16` | 8 | `15.9%` |
| 40 | `0.948` | `2.41e-16` | `8.88e-16` | 8 | `16.1%` |
| 60 | `0.947` | `3.22e-16` | `6.66e-16` | 7 | `17.3%` |

## Readout

Both best LN lanes are Born-clean on the corrected harness at machine
precision. All `|I3|/P` entries above are at order `1e-16` to `1e-15`, which
is the floating-point noise floor for double-precision sums of order-1
probabilities, so neither lane carries a physical Born-violation signal at
the sample sizes here.

The safe summary is:

- Born cleanliness is retained for both lanes at machine precision
- the per-row `|I3|/P` ordering between modular and central-band is not
  monotone in `N` on this seed set (e.g. modular has the higher max at
  `N=25` and the lower max at `N=60`), so this comparison does not pin a
  qualitative stability winner
- central-band remains the simpler hard-geometry lever and keeps the better
  bounded joint-decoherence story

## Interpretation

The result is an apples-to-apples tie in the main sense: both lanes survive
the corrected Born harness cleanly. The distinction is not Born compliance
but which bounded trade-off they prefer:

- modular gap + LN: Born-clean at machine precision on this seed set
- central-band `|y|` + LN: Born-clean at machine precision, with a small
  finite-`N` decoherence advantage at `N=40` and `N=60`

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/combined_gravity_scaling.py`
- `scripts/generative_causal_dag_interference.py`
- `scripts/topology_families.py`
