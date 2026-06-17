# HKD Correspondence General Charts Bounded Theorem Note (2026-06-12)

Status: pipeline-derived bounded real-Schur claim. The audit lane grades.

Runner:

```bash
python3 scripts/frontier_hkd_correspondence_general_charts_2026_06_12.py
```

## Claim

Within the runner's fixed finite Schur convention, the checked charts satisfy

```text
real H_kd_after = 0  <=>  zero misaligned survivors  <=>  all chart periods are even
```

The `H_kd_after` side is now a real floating-point Schur-complement quantity,
not the previous 0/1 parity proxy. The cross-family anchors are recomputed
self-contained checks: the (4,8,4)=L8 chart is protected (real Schur
H_kd_after<1e-14) and the (5,10,5)=L10 chart is unprotected (real Schur
H_kd_after = 0.7524). The exact L10 magnitude depends on this runner's fixed
probe energy E=-0.6. Caveat: the real Schur H_kd_after and the parity
survivor count both restrict to the even-d2 kept support, so they share that
support; their coincidence is nonetheless nontrivial because the Schur
MAGNITUDE is a genuine floating-point recompute (1.148, 2.639, 0.643 - not a
0/1 proxy) independent of the parity arithmetic. The parity survivor count is computed
separately from coordinate parity data and is not used to build the Schur block.

## Machinery

For each chart `q=(q1,q2,q3)`, the runner builds the dense periodic
nearest-neighbor Hamiltonian with onsite `4.0`, hop `-1.0`, and fixed Schur
energy `E=-0.6`. It then performs two real Schur decimations, retaining even
coordinates on axes `0` and `2`. On the resulting real Schur Hamiltonian, it
keeps the diagonal and the entries with even periodic `d2`; finally it measures
`H_kd_after` as `max|H[k,d]|` across the raw checkerboard kept/decimated block.

The independent parity diagnostic uses the same post-decimation coordinates:

```text
raw_i(a,b)      = |a_i - b_i| mod 2
periodic_i(a,b) = min(|a_i-b_i|, q_i-|a_i-b_i|) mod 2
```

A misaligned survivor is counted when `sum_i periodic_i = 0 mod 2` while
`sum_i raw_i = 1 mod 2`. This count is support-only; it does not inspect or set
the Schur matrix entries.

## Results

Anchor gates:

| label | periods | sites | Schur sites | H_kd_before | H_kd_after | misaligned |
|---|---:|---:|---:|---:|---:|---:|
| protected original family, `L=8` | `(4,8,4)` | 128 | 32 | `1.0252645007009416e+00` | `0.0000000000000000e+00` | 0 |
| unprotected original family, `L=10` | `(5,10,5)` | 250 | 90 | `1.7572014742952367e+00` | `7.5243559739582566e-01` | 700 |

The anti-fabrication gate checks that the real pre-truncation
`H_kd_before` block is nonzero before the even-d2 truncation.

General-chart table:

| label | periods | sites | Schur sites | all periods even | H_kd_after | misaligned |
|---|---:|---:|---:|---:|---:|---:|
| all_even_cube | `(4,4,4)` | 64 | 16 | true | `0.0000000000000000e+00` | 0 |
| all_even_rectangular | `(4,6,4)` | 96 | 24 | true | `0.0000000000000000e+00` | 0 |
| one_odd_middle | `(4,5,4)` | 80 | 20 | false | `1.1476977330246578e+00` | 32 |
| one_odd_first_minimal | `(3,4,4)` | 48 | 16 | false | `2.6389342991774600e+00` | 32 |
| all_even_larger | `(6,6,4)` | 144 | 36 | true | `0.0000000000000000e+00` | 0 |
| one_odd_first | `(5,6,4)` | 120 | 36 | false | `6.4271141355526795e-01` | 72 |

Witnesses:

- All-even chart `(4,4,4)`: no real misaligned `H_kd` survivor;
  `H_kd_after=0.0000000000000000e+00`.
- One-odd chart `(4,5,4)`: `keep=(0,4,0)`, `drop=(2,1,2)`,
  `delta=(2,2,2)`, `raw_parity=(0,1,0)`,
  `periodic_parity=(0,0,0)`, `d2=12`, real Schur magnitude
  `1.1476977330246578e+00`, equal to `H_kd_after`.

Runner result:

```text
TOTAL: PASS=11 FAIL=0
```

## Scope

This is a bounded finite-chart statement for the fixed real-Schur convention
above. It does not claim a continuum theorem, an all-period exhaustive
classification, an interacting model, or a universal physical amplitude law.

Memory discipline: every executed chart has at most 250 sites, while the runner
enforces `q1*q2*q3 <= 3000`. A single dense float64 array at that bound is
`72.0 MB`, below the stated `~150 MB` ceiling; charts are processed one at a
time.
