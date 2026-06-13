# Gauge-Vacuum Plaquette Ring Transverse Rho Ladder Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. Runner `TOTAL: PASS=45 FAIL=0`.

**Claim boundary:** finite transverse-ring rho diagnostic at `beta = 6`,
tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`, and source
`MODE_MAX = 200`. The internal environment link uses the derived
dimension-stripped class-channel factor `D_lambda`. The simple ring values are
computed for `N = 3` and `N = 4`; the `N = 2` ring is a two-node doubled-edge
multigraph and is reported separately. This note does not compute the full
physical `3D` unmarked spatial Wilson environment, a strip-depth limit, a
wider slab limit, an `L_perp` limit, analytic `P(6)`, or a repinning.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
`scripts/gauge_vacuum_plaquette_ring_transverse_rho_ladder_bounded_2026_06_12.py`

Runner cache:
`logs/runner-cache/gauge_vacuum_plaquette_ring_transverse_rho_ladder_bounded_2026_06_12.txt`

No literature value, new axiom, external citation, fitted selector, or new
comparator number is imported. Existing finite packet inputs are restated on
their scoped surfaces. The comparison number `0.5934` is used under the
existing plaquette reuse license as fenced comparison context.

Context pointers, not one-hop authorities:
`docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md`,
`docs/GAUGE_VACUUM_PLAQUETTE_THREE_STRIP_ENVIRONMENT_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md`,
`docs/GAUGE_VACUUM_PLAQUETTE_FOUR_STRIP_PARITY_TEST_BOUNDED_NOTE_2026-06-12.md`,
`scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py`,
`scripts/gauge_vacuum_plaquette_three_strip_environment_rho_ladder_bounded_2026_06_12.py`,
`scripts/gauge_vacuum_plaquette_four_strip_parity_test_bounded_2026_06_12.py`.

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
- [GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md](GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md)
  for the supplied finite rim/far slice language and the local rim-lift
  boundary object.
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

## Geometry Read

The cited geometry notes do not name a closed transverse loop. The spatial
tensor-transfer note says:

```text
Slice the unmarked spatial environment along the one orthogonal remaining
spatial direction.
```

It also says the slice step integrates:

```text
shared spatial links
```

The rim-lift row names:

```text
one unmarked edge slice adjacent to the marked plaquette
```

and:

```text
the finite rim neighborhood touching that marked plaquette and the edge slice
```

The finite tensor-word packet names one finite matrix object; it does not
state a transverse topology beyond that packet. These quotes license an
orthogonal/edge-slice construction and a rim-neighborhood boundary object, but
the geometry surface does not name a closed transverse loop or a periodic
transverse chain.

Therefore this note applies both-readings discipline to topology. The open
chain remains the previously measured finite strip-width approximation. The
ring is a uniform-density diagnostic: every transverse unit has the same
number of internal environment links, so the edge/middle link-density
asymmetry of the open chain is removed inside this finite packet.

## Construction

Let

```text
B_4 = {(p,q) : 0 <= p,q <= 4},
D_(p,q) = c_(p,q)(6)/(d_(p,q)c_(0,0)(6)),
M = N_f + N_fbar.
```

The derived dimension-stripped internal-link factor is

```text
E_D(a,b) = 1 + sum_{lambda != (0,0)} D_lambda N_{a,b}^{lambda}.
```

For an open `N`-chain:

```text
D_open(a_0,...,a_{N-1})
  = product_i D_{a_i} product_{i=0}^{N-2} E_D(a_i,a_{i+1}).
```

For an `N`-ring:

```text
D_ring(a_0,...,a_{N-1})
  = product_i D_{a_i} product_{i=0}^{N-1} E_D(a_i,a_{i+1 mod N}).
```

The finite transfer in both cases is

```text
T_N = D_N M_N D_N M_N^T D_N,
M_N = M tensor ... tensor M.
```

The readout is the normalized one-unit marginal of the Perron vector:

```text
rho_N(a) = sum_{all other unit labels} psi_N(a, ...)
           / sum_{all other unit labels} psi_N((0,0), ...).
```

For simple rings, all unit marginals agree by the finite cyclic symmetry. For
`N = 2`, the ring has two links between the same pair:

```text
D_ring2(a,b) = D_a D_b E_D(a,b) E_D(b,a).
```

That is a doubled-edge multigraph, not a simple-cycle rung. It is still a
well-defined cut gate and diagnostic, so it is reported separately while the
simple-ring ladder starts at `N = 3`.

## Gates

The word and open-chain anchors are reproduced under the same finite source
readout:

```text
P(rho_word) = 0.434215413259920
P(open N=2) = 0.439904783618900
P(open N=3) = 0.436904879677743
```

The `N = 4` open chain is also computed by the same matrix-free operator:

```text
P(open N=4) = 0.438273257015453
```

Cut gates:

```text
cut one N=2 doubled-ring edge -> open N=2
cut the N=3 closing ring edge -> open N=3
cut the N=4 closing ring edge -> open N=4
```

The runner checks these as rho-vector and composed-`P` equalities at
double-precision tolerance.

## Ring Measurement

Primary simple-ring values:

| object | links per transverse object | `rho_(1,0)` | `rho_(1,1)` | `P` |
|---|---:|---:|---:|---:|
| ring `N=3` simple cycle | `3` | `0.706140932688793` | `0.240890371746918` | `0.443670871217007` |
| ring `N=4` simple cycle | `4` | `0.711524433459755` | `0.239885439681920` | `0.443819912885704` |

Doubled-edge diagnostic:

| object | links per transverse object | `rho_(1,0)` | `rho_(1,1)` | `P` |
|---|---:|---:|---:|---:|
| ring `N=2` doubled edge | `2` | `0.726012528790230` | `0.239343780988132` | `0.444222385798573` |

## Ladder Readout

The fenced comparator is used only as comparison/reuse context.

```text
open-chain ladder:
N=1 P=0.434215413259920 increment=baseline          |P-0.5934|=0.159184586740080
N=2 P=0.439904783618900 increment=+0.005689370358980 |P-0.5934|=0.153495216381100
N=3 P=0.436904879677743 increment=-0.002999903941157 |P-0.5934|=0.156495120322257
N=4 P=0.438273257015453 increment=+0.001368377337710 |P-0.5934|=0.155126742984547

ring diagnostic and simple-ring ladder:
N=2 doubled-edge P=0.444222385798573 increment=baseline          |P-0.5934|=0.149177614201427
N=3 simple ring  P=0.443670871217007 increment=-0.000551514581566 |P-0.5934|=0.149729128782993
N=4 simple ring  P=0.443819912885704 increment=+0.000149041668697 |P-0.5934|=0.149580087114296
```

The open-chain ladder keeps the parity oscillation on the finite values shown
above. The simple-ring sample has one positive finite increment, `N = 3` to
`N = 4`; that is consistent with the uniform-density diagnostic, but it is not
enough by itself to establish a multi-rung monotone law. If the doubled-edge
`N = 2` diagnostic is included, the displayed ring sequence is not monotone.

Non-load-bearing geometric diagnostic: the ring removes the open-chain
edge/middle link-density split inside each displayed simple cycle. The
measured simple-ring increment is positive over `N = 3 -> N = 4`, while the
doubled-edge `N = 2` object should not be read as a simple-cycle rung.

## Cross-Geometry Comparison and Bracket Caution

The measured simple-ring values sit above the displayed open-chain `N = 3`
and `N = 4` pair
(`[0.436904879677743, 0.438273257015454]`): simple rings give
`0.443670871217007` (`N = 3`) and `0.443819912885704` (`N = 4`). This is a
finite diagnostic, not a limit theorem.

The checked topology bookkeeping is only this: each simple-ring unit has one
internal environment link, while an open `N`-chain has `(N - 1)/N` internal
links per unit. That explains why the finite comparison is worth recording,
but it does not prove a shared slab limit, approach side, monotonicity, or
preferred extrapolant.

The practical caution is therefore limited: the open-chain odd/even pair is a
last measured pair, not a proven enclosure of the width limit. Neither
geometry's ladder is extrapolated here; the wider-`N` ring rung remains a
named next diagnostic.

## Named Residuals

- transverse-topology underdetermination in the cited geometry notes;
- finite simple ring widths `N = 3` and `N = 4`;
- doubled-edge `N = 2` multigraph diagnostic;
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
python3 scripts/gauge_vacuum_plaquette_ring_transverse_rho_ladder_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=44, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_ring_transverse_rho_ladder_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
