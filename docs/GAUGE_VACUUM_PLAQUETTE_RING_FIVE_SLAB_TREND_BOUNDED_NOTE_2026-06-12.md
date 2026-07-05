# Gauge-Vacuum Plaquette Ring Five Finite Trend Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. Runner `TOTAL: PASS=37 FAIL=0`.

**Claim boundary:** finite transverse-ring rho diagnostic at `beta = 6`,
tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`, and source
`MODE_MAX = 200`. The internal environment link uses the derived
dimension-stripped class-channel factor `D_lambda`. This note computes the
simple-ring `N = 5` point and restates the same-code-path `N = 3,4` anchors.
It does not compute the physical `3D` unmarked spatial Wilson environment, a
strip-depth limit, a wider slab limit, an `L_perp` limit, analytic `P(6)`, or
a repinning.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
`scripts/gauge_vacuum_plaquette_ring_five_slab_trend_bounded_2026_06_12.py`

Runner cache:
`logs/runner-cache/gauge_vacuum_plaquette_ring_five_slab_trend_bounded_2026_06_12.txt`

No new imports: no literature value, new axiom, external citation, fitted
selector, or new comparator number is used. Existing finite packet inputs are
restated on their scoped surfaces. The comparison number `0.5934` and the
open-chain four-strip context interval are used only inside the fenced
comparison block.

Context pointers, not one-hop authorities:
`docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md`
`docs/GAUGE_VACUUM_PLAQUETTE_THREE_STRIP_ENVIRONMENT_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md`
`docs/GAUGE_VACUUM_PLAQUETTE_FOUR_STRIP_PARITY_TEST_BOUNDED_NOTE_2026-06-12.md`
`scripts/gauge_vacuum_plaquette_ring_transverse_rho_ladder_bounded_2026_06_12.py`
`scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py`

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the tensor-transfer construction language: spatial plaquette factors are
  expanded in characters and shared slice links are integrated by Haar /
  Peter-Weyl decomposition.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `25`-state tensor-word packet, `D_lambda` convention, and
  finite `SU(3)` fundamental / anti-fundamental fusion primitives on `B_4`.
- [GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the finite adjacent-word contraction that reduces the connected
  internal environment link to the dimension-stripped `D_lambda` class-channel
  factor used here.
- [GAUGE_VACUUM_PLAQUETTE_RING_TRANSVERSE_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_RING_TRANSVERSE_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md)
  for the landed finite-ring construction, same-code-path `N = 3,4` anchors,
  and bracket-caution boundary extended here to `N = 5`.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the same-link mixed Wilson kernel and its per-link
  matrix-coefficient convolution eigenvalue.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the Schur-orthogonality character-convolution dictionary that supplies
  the inverse-dimension shared-link factor.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the finite source-sector Perron machinery with supplied `rho`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
  for the one-word rho normalization convention and composed one-word value.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934` used only in the fenced
  distance block.

## Construction

Let

```text
B_4 = {(p,q) : 0 <= p,q <= 4},
D_(p,q) = c_(p,q)(6)/(d_(p,q)c_(0,0)(6)),
M = N_f + N_fbar.
```

The internal-link factor used here is

```text
E_D(a,b) = 1 + sum_{lambda != (0,0)} D_lambda N_{a,b}^{lambda}.
```

For an `N`-ring:

```text
D_ring(a_0,...,a_{N-1})
  = product_i D_{a_i} product_{i=0}^{N-1} E_D(a_i,a_{i+1 mod N}).
```

The finite transfer is applied matrix-free:

```text
T_N = D_N M_N D_N M_N^T D_N,
M_N = M tensor ... tensor M.
```

The readout is the normalized one-unit marginal of the Perron vector:

```text
rho_N(a) = sum_{all other unit labels} psi_N(a, ...)
           / sum_{all other unit labels} psi_N((0,0), ...).
```

## N=5 State Space

The `N = 5` ring has

```text
25^5 = 9765625
```

states. A single float64 vector is `78.125` MB decimal (`74.506` MiB). The
runner prints the memory estimate before building the packet or solving. It
uses deterministic power iteration because an `eigsh` basis at `ncv = 24`
would be about `1.746` GiB, while the power path uses a few vectors plus the
diagonal.

## Gates

The same matrix-free power path reproduces the simple-ring anchors:

```text
P(ring N=3) = 0.443670871217023
P(ring N=4) = 0.443819912885700
```

The `N = 5` one-link cut gate is applied as a transfer-level check: cutting
the closing edge of the `N = 5` ring leaves the open five-chain edge set. The
runner verifies that the cut-ring matvec and open-five matvec agree on three
deterministic probe vectors. It does not need the full open-five Perron solve
for this gate.

The ring symmetry gate is the translation-marginal agreement across all five
unit marginals. The rho admissibility gate checks finite rho, rho of the
trivial channel equal to `1`, nonnegative finite-box rho within numerical
tolerance, and conjugation symmetry on `B_4`.

## Measurement

Primary simple-ring values:

| object | links per transverse object | `rho_(1,0)` | `rho_(1,1)` | `P` |
|---|---:|---:|---:|---:|
| ring `N=3` simple cycle | `3` | `0.706140932689393` | `0.240890371746946` | `0.443670871217023` |
| ring `N=4` simple cycle | `4` | `0.711524433459604` | `0.239885439681919` | `0.443819912885700` |
| ring `N=5` simple cycle | `5` | `0.708705386538277` | `0.240221325991754` | `0.443741696435695` |

The finite increments are:

```text
N=3 -> N=4: +0.000149041668676
N=4 -> N=5: -0.000078216450005
```

The rise from `N = 3` to `N = 4` does not continue at `N = 5`. The finite
`N = 4 -> N = 5` increment flips sign and its absolute value is about
`0.524795855410589` of the previous increment. This is a measured
finite-ring result, not an extrapolation of the slab limit.

Non-load-bearing geometric diagnostic: over `N = 3,4,5`, the simple-ring
sample shows a damped two-increment oscillation rather than a monotone rise.

## Fenced Comparator Distances

The fenced comparator values are comparison context only.

```text
simple-ring ladder:
N=3 simple ring | P=0.443670871217023 | increment=baseline          | |P-0.5934|=0.149729128782977 | distance_to_open4_low=+0.006765991539280 | distance_to_open4_high=+0.005397614201569
N=4 simple ring | P=0.443819912885700 | increment=+0.000149041668676 | |P-0.5934|=0.149580087114300 | distance_to_open4_low=+0.006915033207957 | distance_to_open4_high=+0.005546655870246
N=5 simple ring | P=0.443741696435695 | increment=-0.000078216450005 | |P-0.5934|=0.149658303564305 | distance_to_open4_low=+0.006836816757952 | distance_to_open4_high=+0.005468439420241

open-chain four-strip context interval = [0.436904879677743, 0.438273257015454]
```

The displayed `N = 5` value remains above the open-chain four-strip context
interval, while the simple-ring finite increment no longer points upward at
this rung.

## Named Residuals

- transverse-topology underdetermination in the cited geometry notes;
- finite simple ring widths `N = 3,4,5`;
- finite dominant-weight box `B_4`;
- finite Wilson Bessel mode support;
- scalar class-channel internal-link contraction;
- future all-link `6j` / intertwiner normalization;
- full rim `eta_beta^env` evaluation;
- strip-depth direction;
- wider slab limit;
- `3D` stack;
- `L_perp` limit;
- analytic `P(6)`;
- no repinning.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_ring_five_slab_trend_bounded_2026_06_12.py
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_ring_five_slab_trend_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
