# Gauge-Vacuum Plaquette Three-Strip Environment Rho Ladder Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem

**Claim boundary:** finite three-strip environment-side computation at
`beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`,
and source `MODE_MAX = 200`. The strip layer has three transverse units, so
the state space is `B_4 x B_4 x B_4`, dimension `25^3 = 15625`. The transverse
geometry is an open `3`-chain with internal links `unit1-unit2` and
`unit2-unit3`; there is no `unit3-unit1` ring link. This note computes the
next finite strip-width rung under both W38 internal-link readings and composes
the resulting `rho_3strip` through the existing source solve. It does not
compute the full physical `3D` unmarked spatial Wilson environment, a strip
depth limit, a wider slab limit, an `L_perp` limit, analytic `P(6)`, or a
repinning.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_three_strip_environment_rho_ladder_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_three_strip_environment_rho_ladder_bounded_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. The comparison number `0.5934` is used under the
existing plaquette reuse license as fenced comparison context.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite one-word construction
  `tensor_word := diag_c * (N_f + N_fbar) * diag_c * (N_f + N_fbar)^T * diag_c`.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the finite tensor-transfer language: matrix elements are finite sums of
  Wilson coefficients and exact nonnegative `SU(3)` fusion/intertwiner
  multiplicities.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the marked/non-marked compression distinction and the normalized
  one-link coefficient `a_lambda(beta) = c_lambda(beta)/(d_lambda c_0(beta))`.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character-convolution and Schur-orthogonality dictionary used for
  the finite internal-link character channels.
- [GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md)
  for the formal central-sequence convention
  `Z_beta^env(W) = lambda_env(beta) sum d_(p,q) r_(p,q)^env(beta) chi_(p,q)(W)`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source-sector Perron machinery with supplied `rho`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
  for the one-word rho normalization convention
  `rho^tw_(p,q) = psi_tw[p,q]/psi_tw[0,0]` and the composed one-word value.
- [GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the derived dimension-stripped internal-link contraction convention.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934`.

Context pointers, not one-hop authorities:
docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md,
docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md.

## Construction

Let

```text
B_4 = {(p,q) : 0 <= p,q <= 4},
D_(p,q) = c_(p,q)(6)/(d_(p,q)c_(0,0)(6)),
M = N_f + N_fbar.
```

For a three-strip layer, the state is `(a,b,c) in B_4^3`, where `a`, `b`,
and `c` are the open-chain transverse unit labels. The layer-to-layer bond is

```text
M_3 = M tensor M tensor M.
```

The two internal links use the same W38 pair factor `E`:

```text
E_full(a,b) = 1 + sum_{lambda != (0,0)} d_lambda D_lambda N_{a,b}^{lambda}
E_D(a,b)    = 1 + sum_{lambda != (0,0)} D_lambda N_{a,b}^{lambda}.
```

The finite three-strip diagonal is

```text
D_3(a,b,c) = D_a D_b D_c E(a,b) E(b,c),
T_3 = D_3 M_3 D_3 M_3^T D_3.
```

There is no `E(c,a)` factor. This matches the open-boundary convention stated
in the task and used here for the strip-width rung.

The runner applies `T_3` matrix-free by reshaping vectors to `25 x 25 x 25`
and applying `M` or `M^T` along each axis. A dense `15625 x 15625` transfer
would require about `1.819 GiB`, so it is not built.

The boundary-character readout keeps the W38 marked-interface convention:

```text
rho_3strip(a)
  = sum_{b,c} psi_3strip(a,b,c)
    / sum_{b,c} psi_3strip((0,0),b,c).
```

The right outer marginal agrees with the left marginal by open-chain reversal.
The center marginal is finite but different, as expected for an open `3`-chain.

## Gates

The finite state-space gate passes:

```text
one-word state count = 25
three-strip layer state count = 15625
dense transfer storage would be 1.819 GiB
fusion table shape = (25, 25, 25)
```

The one-word and W38 two-strip anchors are reproduced:

```text
P(rho_word) = 0.434215413259920
two-strip full-character P = 0.447034890458824
two-strip dimension-stripped P = 0.439904783618900
```

Cutting both internal links reproduces three independent word chains:

```text
both-link cut residual on psi_word tensor psi_word tensor psi_word = 4.441e-16
both-link cut max |rho-rho_word| = 2.776e-17
P(both-link cut marginal) = 0.434215413259920
```

Cutting one internal link reproduces `(2-strip) x (1-word)` and the W38
two-strip rho marginal:

```text
full-character right-link cut residual = 2.665e-15
full-character right-link cut left marginal max |rho-rho_2strip| = 2.220e-16
full-character right-link cut P(left marginal) = 0.447034890458824
full-character left-link cut residual = 3.109e-15
full-character left-link cut center marginal max |rho-rho_2strip| = 3.331e-16

dimension-stripped right-link cut residual = 5.551e-16
dimension-stripped right-link cut left marginal max |rho-rho_2strip| = 2.220e-16
dimension-stripped right-link cut P(left marginal) = 0.439904783618900
dimension-stripped left-link cut residual = 5.551e-16
dimension-stripped left-link cut center marginal max |rho-rho_2strip| = 3.331e-16
```

The full three-strip Perron solves are admissible on the finite box:

```text
full-character:
  combined internal factor min/max = 1.000000000000000 / 34.913614095442682
  eigenvalue = 125.843628815856690
  Perron residual = 1.776e-14
  psi_min = -3.762e-37
  rho_left min/max = 1.473e-24 / 1.000e+00
  left/right marginal residual = 8.882e-16
  conjugation residual = 1.110e-16

dimension-stripped:
  combined internal factor min/max = 1.000000000000000 / 2.881356246816831
  eigenvalue = 5.015948012281473
  Perron residual = 8.882e-16
  psi_min = -4.815e-35
  rho_left min/max = 3.645e-24 / 1.000e+00
  left/right marginal residual = 3.331e-16
  conjugation residual = 2.776e-17
```

The tiny negative `psi_min` values are numerical roundoff around zero; the
normalized rho entries are finite and nonnegative at the printed scale.

## Three-Strip Rho Values

Selected left-marginal values:

| reading | `rho_(1,0)` | `rho_(1,1)` | `P` |
|---|---:|---:|---:|
| full-character | `0.622521176293775` | `0.331340164127031` | `0.441391418390688` |
| dimension-stripped | `0.469564971869026` | `0.200666996037837` | `0.436904879677743` |

## Ladder Measurement

The fenced comparator is used only as comparison/reuse context.

```text
full-character reading:
P(1-strip word) = 0.434215413259920
P(2-strip) = 0.447034890458824
P(3-strip) = 0.441391418390688
increment P2-P1 = 0.012819477198904
increment P3-P2 = -0.005643472068136
non_load_bearing_geometric_diagnostic:
  first two increments do not support a contracting-ratio diagnostic;
  empirical ratio = -0.440226382134992
|P1 - 0.5934| = 0.159184586740080
|P2 - 0.5934| = 0.146365109541176
|P3 - 0.5934| = 0.152008581609312
distance change P1->P2 = 0.012819477198904
distance change P2->P3 = -0.005643472068136

dimension-stripped reading:
P(1-strip word) = 0.434215413259920
P(2-strip) = 0.439904783618900
P(3-strip) = 0.436904879677743
increment P2-P1 = 0.005689370358980
increment P3-P2 = -0.002999903941156
non_load_bearing_geometric_diagnostic:
  first two increments do not support a contracting-ratio diagnostic;
  empirical ratio = -0.527282238960147
|P1 - 0.5934| = 0.159184586740080
|P2 - 0.5934| = 0.153495216381100
|P3 - 0.5934| = 0.156495120322257
distance change P1->P2 = 0.005689370358980
distance change P2->P3 = -0.002999903941156
```

The finite three-strip rung remains above the one-strip word value under both
readings, but it is below the corresponding two-strip rung. The first two
width increments therefore do not support a contracting geometric ladder
diagnostic.

## Named Residuals

- finite three-strip width rung;
- finite dominant-weight box `B_4`;
- finite Wilson Bessel mode support;
- product-orientation internal-link contraction inherited from W38;
- future all-link `6j`/intertwiner normalization;
- strip-depth direction;
- wider slab limit;
- `3D` stack;
- `L_perp` limit;
- analytic `P(6)`;
- no repinning.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_three_strip_environment_rho_ladder_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=39, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_three_strip_environment_rho_ladder_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
