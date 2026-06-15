# Gauge-Vacuum Plaquette Four-Strip Parity Test Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem

**Claim boundary:** finite four-strip environment-side computation at
`beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`,
and source `MODE_MAX = 200`. The strip layer has four transverse units, so
the state space is `B_4 x B_4 x B_4 x B_4`, dimension `25^4 = 390625`.
The transverse geometry is an open `4`-chain with internal links
`unit1-unit2`, `unit2-unit3`, and `unit3-unit4`; there is no ring link.
The primary internal-link convention is the licensed dimension-stripped
contraction. The full-character contraction is reported as a control. This
note does not compute the full physical `3D` unmarked spatial Wilson
environment, a strip-depth limit, a wider slab limit, an `L_perp` limit,
analytic `P(6)`, or a repinning.

**Status:** source proposal; independent audit required. Runner `PASS=45 FAIL=0`.
Status authority: independent audit lane only. This source note does not set,
predict, promote, or demote any audit outcome.

**Primary runner:** [`scripts/gauge_vacuum_plaquette_four_strip_parity_test_bounded_2026_06_12.py`](../scripts/gauge_vacuum_plaquette_four_strip_parity_test_bounded_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/gauge_vacuum_plaquette_four_strip_parity_test_bounded_2026_06_12.txt`](../logs/runner-cache/gauge_vacuum_plaquette_four_strip_parity_test_bounded_2026_06_12.txt)

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
docs/GAUGE_VACUUM_PLAQUETTE_THREE_STRIP_ENVIRONMENT_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md,
docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md.

## Construction

Let

```text
B_4 = {(p,q) : 0 <= p,q <= 4},
D_(p,q) = c_(p,q)(6)/(d_(p,q)c_(0,0)(6)),
M = N_f + N_fbar.
```

For a four-strip layer, the state is `(a,b,c,d) in B_4^4`. The layer-to-layer
bond is

```text
M_4 = M tensor M tensor M tensor M.
```

The three internal links use the W38/W40 dimension-stripped pair factor as
primary:

```text
E_D(x,y) = 1 + sum_{lambda != (0,0)} D_lambda N_{x,y}^{lambda}.
```

The full-character control replaces `D_lambda` with `d_lambda D_lambda`:

```text
E_full(x,y) = 1 + sum_{lambda != (0,0)} d_lambda D_lambda N_{x,y}^{lambda}.
```

The finite four-strip diagonal is

```text
D_4(a,b,c,d) = D_a D_b D_c D_d E(a,b) E(b,c) E(c,d),
T_4 = D_4 M_4 D_4 M_4^T D_4.
```

There is no `E(d,a)` factor. The runner applies `T_4` matrix-free by reshaping
vectors to `25 x 25 x 25 x 25` and applying `M` or `M^T` along each axis.

The deterministic resource estimate printed before the eigensolve is:

```text
four-strip layer state count = 390625
dense transfer storage would be 1.110 TiB
one float64 vector storage = 2.980 MiB
eigsh ncv=32 vector basis storage estimate = 95.367 MiB
matrix-free matvec multiply-add scale estimate = 78125000
```

The boundary-character readout keeps the existing marked-interface convention:

```text
rho_4strip(a)
  = sum_{b,c,d} psi_4strip(a,b,c,d)
    / sum_{b,c,d} psi_4strip((0,0),b,c,d).
```

The opposite edge marginal agrees with this edge marginal by open-chain
reversal. The two inner marginals agree with each other and are separately
reported as diagnostics.

## Gates

The one-word and landed strip anchors are reproduced:

```text
P(rho_word) = 0.434215413259920
two-strip dimension-stripped P = 0.439904783618900
three-strip dimension-stripped P = 0.436904879677743
two-strip full-character P = 0.447034890458824
three-strip full-character P = 0.441391418390688
```

Cutting all three internal links reproduces four independent word chains:

```text
all-link cut residual on four word-chain tensor = 4.441e-16
all-link cut max |rho-rho_word| = 5.551e-17
P(all-link cut marginal) = 0.434215413259920
```

Single-link cuts reproduce the expected factorized chains against the landed
anchors. For the dimension-stripped primary:

```text
cut link 3-4 residual on psi_3strip tensor psi_word = 8.882e-16
cut link 3-4 edge marginal max |rho-rho_3strip| = 1.110e-16
cut link 3-4 P(edge marginal) = 0.436904879677743

cut link 1-2 residual on psi_word tensor psi_3strip = 8.882e-16
cut link 1-2 block-edge marginal max |rho-rho_3strip| = 3.886e-16
cut link 1-2 P(block-edge marginal) = 0.436904879677743

cut link 2-3 residual on psi_2strip tensor psi_2strip = 7.772e-16
cut link 2-3 edge marginal max |rho-rho_2strip| = 2.220e-16
cut link 2-3 P(edge marginal) = 0.439904783618900
```

For the full-character control:

```text
cut link 3-4 residual on psi_3strip tensor psi_word = 2.309e-14
cut link 3-4 edge marginal max |rho-rho_3strip| = 1.110e-16
cut link 3-4 P(edge marginal) = 0.441391418390689

cut link 1-2 residual on psi_word tensor psi_3strip = 2.309e-14
cut link 1-2 block-edge marginal max |rho-rho_3strip| = 2.220e-16
cut link 1-2 P(block-edge marginal) = 0.441391418390688

cut link 2-3 residual on psi_2strip tensor psi_2strip = 1.599e-14
cut link 2-3 edge marginal max |rho-rho_2strip| = 2.220e-16
cut link 2-3 P(edge marginal) = 0.447034890458824
```

The full four-strip Perron solves are admissible on the finite box:

```text
dimension-stripped:
  combined internal factor min/max = 1.000000000000000 / 4.890974918740656
  eigenvalue = 11.029722455357625
  Perron residual = 1.332e-15
  psi_min = -2.407e-35
  rho_edge min/max = 3.991e-24 / 1.000e+00
  edge reversal residual = 2.331e-15
  inner reversal residual = 3.331e-16
  edge conjugation residual = 1.110e-16

full-character:
  combined internal factor min/max = 1.000000000000000 / 206.296666771831468
  eigenvalue = 1453.320477080826095
  Perron residual = 1.705e-13
  psi_min = -9.404e-37
  rho_edge min/max = 1.661e-24 / 1.000e+00
  edge reversal residual = 2.220e-15
  inner reversal residual = 3.553e-15
  edge conjugation residual = 1.110e-16
```

The tiny negative `psi_min` values are numerical roundoff around zero; the
normalized edge rho entries are finite and nonnegative at the printed scale.

## Four-Strip Rho Values

Selected edge and inner marginal values:

| reading | `rho_edge(1,0)` | `rho_edge(1,1)` | `P(edge rho)` | `rho_inner(1,0)` | `rho_inner(1,1)` | `P(inner rho)` |
|---|---:|---:|---:|---:|---:|---:|
| dimension-stripped | `0.516765488421587` | `0.202499597996785` | `0.438273257015454` | `0.765661478406071` | `0.242142665998304` | `0.445322221638842` |
| full-character | `0.703879456911549` | `0.339171272352561` | `0.443683201450925` | `1.342476222461378` | `0.693640281401391` | `0.460729884020911` |

## Parity Measurement

The fenced comparator is used only as comparison/reuse context.

```text
dimension-stripped reading:
P(1) = 0.434215413259920
P(2) = 0.439904783618900
P(3) = 0.436904879677743
P(4) = 0.438273257015454
increment P2-P1 = 0.005689370358980
increment P3-P2 = -0.002999903941156
increment P4-P3 = 0.001368377337710
odd subsequence P(1)->P(3) monotone upward = True
even subsequence P(2)->P(4) monotone downward = True
measured tails move toward each other = True
measured two-sided tail bracket = [0.436904879677743, 0.438273257015454]
bracket note: measured from P(3) and P(4) only; no extrapolation
|P(1) - 0.5934| = 0.159184586740080
|P(2) - 0.5934| = 0.153495216381100
|P(3) - 0.5934| = 0.156495120322257
|P(4) - 0.5934| = 0.155126742984546
```

Thus, at the measured rungs only, the primary even and odd subsequences are
monotone in opposite directions and the last measured odd/even pair gives the
measured bracket `[0.436904879677743, 0.438273257015454]`. This is a finite
measurement, not an extrapolated width limit.

The density diagnostic requested in the task is:

```text
N=1: internal_links=0, density=(N-1)/N=0.000000000000, incident_counts=[0],
     P=0.434215413259920, P-P(1)=0.000000000000000
N=2: internal_links=1, density=(N-1)/N=0.500000000000, incident_counts=[1, 1],
     P=0.439904783618900, P-P(1)=0.005689370358980
N=3: internal_links=2, density=(N-1)/N=0.666666666667, incident_counts=[1, 2, 1],
     P=0.436904879677743, P-P(1)=0.002689466417823
N=4: internal_links=3, density=(N-1)/N=0.750000000000, incident_counts=[1, 2, 2, 1],
     P=0.438273257015454, P-P(1)=0.004057843755534
density-order monotone P-deviation = False
```

The scalar density order by itself does not give a monotone P-deviation across
`N = 1..4`. The parity-resolved measurement above remains the labeled
diagnostic surface from this rung.

## Full-Character Control Ladder

```text
full-character control reading:
P(1) = 0.434215413259920
P(2) = 0.447034890458824
P(3) = 0.441391418390688
P(4) = 0.443683201450925
increment P2-P1 = 0.012819477198904
increment P3-P2 = -0.005643472068136
increment P4-P3 = 0.002291783060236
odd subsequence P(1)->P(3) monotone upward = True
even subsequence P(2)->P(4) monotone downward = True
measured tails move toward each other = True
measured two-sided tail bracket = [0.441391418390688, 0.443683201450925]
bracket note: measured from P(3) and P(4) only; no extrapolation
|P(1) - 0.5934| = 0.159184586740080
|P(2) - 0.5934| = 0.146365109541176
|P(3) - 0.5934| = 0.152008581609312
|P(4) - 0.5934| = 0.149716798549075
```

## Named Residuals

- finite four-strip width rung;
- finite dominant-weight box `B_4`;
- finite Wilson Bessel mode support;
- product-orientation internal-link contraction inherited from the landed strip runners;
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
python3 scripts/gauge_vacuum_plaquette_four_strip_parity_test_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=45, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_four_strip_parity_test_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
