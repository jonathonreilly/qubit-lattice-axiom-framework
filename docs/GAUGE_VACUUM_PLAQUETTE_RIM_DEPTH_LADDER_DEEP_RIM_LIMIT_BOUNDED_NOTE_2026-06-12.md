# Gauge-Vacuum Plaquette Rim-Depth Ladder Deep-Rim Limit

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Type:** bounded_theorem

**Claim boundary:** finite rim-depth ladder measurement on the existing
tensor-word packet at `beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`,
source `NMAX = 7`, source `MODE_MAX = 200`, and word counts `1`, `2`, `3`
under the derived matrix-element adjacent bond. This note evaluates
`eta_k = tensor_word^k e_(0,0)` for `k = 0, 1, 2, 3, 5, 8, 12, 20` plus
the finite tensor-word Perron-boundary reference `eta_inf`. "Deep-rim limit"
here means only that finite 25-state Perron-boundary reference; it does not
mean a physical rim, all-weight, or untruncated limit. It does not compute the
physical 3D unmarked spatial Wilson environment, an all-weight or
untruncated tensor-transfer limit, an `L_perp` limit, analytic `P(6)`, or a
canonical repinning.

**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** [`scripts/gauge_vacuum_plaquette_rim_depth_ladder_deep_rim_limit_2026_06_12.py`](../scripts/gauge_vacuum_plaquette_rim_depth_ladder_deep_rim_limit_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/gauge_vacuum_plaquette_rim_depth_ladder_deep_rim_limit_2026_06_12.txt`](../logs/runner-cache/gauge_vacuum_plaquette_rim_depth_ladder_deep_rim_limit_2026_06_12.txt)

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the finite tensor-transfer language and the open boundary-character
  target.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `tensor_word`, `boundary0`, and `amp` packet.
- [GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md](GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md)
  for the supplied-partition rim integral surface.
- [GAUGE_VACUUM_PLAQUETTE_SU3_FULL_SLICE_PRODUCT_FUBINI_FACTORIZATION_NOTE_2026-06-06.md](GAUGE_VACUUM_PLAQUETTE_SU3_FULL_SLICE_PRODUCT_FUBINI_FACTORIZATION_NOTE_2026-06-06.md)
  for the finite `SU(3)` product-Fubini rim/far factorization once the support
  partition is supplied.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  and [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the matrix-element adjacent bond `delta_(lambda,mu) / d_lambda`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source-sector Perron machinery with `rho` supplied as input.
- [GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md)
  for the depth-one constructed-rim readout and eta-weighted boundary
  convention being extended here.
- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the derived matrix-element adjacent bond used in the ladder.
- [GAUGE_VACUUM_PLAQUETTE_TRIVIAL_SLICE_EIGEN_IDENTITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_TRIVIAL_SLICE_EIGEN_IDENTITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the trivial-slice identity used as the `k = 0` gate.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934`, used only in fenced
  distance reporting.

No literature value, new axiom, external citation, fitted selector, or new
comparator number is used.

## Normalization and Readout

The rim-depth vectors are normalized by the rim-boundary row convention:

```text
rho_eta_k(lambda) = eta_k(lambda) / eta_k(0,0).
```

The higher-weight L1 column below is
`sum_(lambda != (0,0)) |rho_eta_k(lambda)|`. The weighted readout is the same
finite expression used by the constructed-rim runner; scalar normalization of
`eta_k` cancels between numerator and denominator for the two- and three-word
rows.

The one-word row has no unmarked slot, so it stays at the tensor-word Perron
anchor for every `eta_k`:

```text
P1 = 0.434215413260.
```

## The Table

| depth | higher L1 | higher L1 / total L1 | `||eta_k - eta_inf||_inf` | `P2` | `P3` | `|P3 - 0.592817119605|` |
|---:|---:|---:|---:|---:|---:|---:|
| `0` | `0.000000000000` | `0.000000000000` | `3.785149223171e-01` | `0.429196712321` | `0.429196712321` | `0.163620407284` |
| `1` | `0.720753266493` | `0.418859159258` | `1.672490524921e-01` | `0.431504881786` | `0.487332641164` | `0.105484478441` |
| `2` | `0.943987938485` | `0.485593516193` | `6.669331420564e-02` | `0.432465615318` | `0.524083379824` | `0.068733739781` |
| `3` | `1.033609675074` | `0.508263551134` | `2.559925643371e-02` | `0.432836697103` | `0.536381703306` | `0.056435416299` |
| `5` | `1.081483179565` | `0.519573345671` | `3.637524928573e-03` | `0.433030156204` | `0.542223091293` | `0.050594028312` |
| `8` | `1.088994966639` | `0.521300904995` | `1.914976898197e-04` | `0.433060212494` | `0.543094536619` | `0.049722582986` |
| `12` | `1.089404185700` | `0.521394660332` | `3.768721553221e-06` | `0.433061847558` | `0.543141664312` | `0.049675455293` |
| `20` | `1.089412397728` | `0.521396541397` | `1.459356024913e-09` | `0.433061880367` | `0.543142609685` | `0.049674509920` |
| `inf` | `1.089412400909` | `0.521396542126` | `0.000000000000e+00` | `0.433061880380` | `0.543142610051` | `0.049674509554` |

Gate checks:

- `k = 0` reproduces the trivial-slice matrix-element row:
  `P2 = P3 = 0.429196712321`.
- `k = 1` reproduces the constructed-rim row from the rim-boundary note:
  `P2 = 0.431504881786`, `P3 = 0.487332641164`.
- `k = 20` is within `3.662140590777e-10` of the Perron-boundary `P3` and
  within `1.270922256325e-11` of the Perron-boundary `P2`.

## Answers

The sampled finite-depth `P3` sequence is monotone nondecreasing:

```text
+5.813592884225e-02
+3.675073866007e-02
+1.229832348179e-02
+5.841387987016e-03
+8.714453268881e-04
+4.712769287019e-05
+9.453728445630e-07
```

The sampled finite-depth `P2` sequence is also monotone nondecreasing and
approaches `0.433061880380` in the finite tensor-word Perron-boundary
readout.

On this finite packet, the sampled normalized `eta_k` vectors move rapidly
toward `eta_inf`: the rho-space sup-distance falls from `3.785149223171e-01` at
`k = 0` to `1.459356024913e-09` at `k = 20`.

The finite tensor-word Perron-boundary three-word readout lands at:

```text
P3(eta_inf) = 0.543142610051.
```

That is not the existing marginal-branch value `0.592817119605` at displayed
precision. The measured finite-packet divergence is:

```text
|P3(eta_inf) - 0.592817119605| = 0.049674509554.
```

So the deep-rim finite tensor-word ladder does not revive the `0.5928`
marginal branch on this packet. The honest landing point is the
Perron-boundary value itself, with the divergence above.

## Fenced Comparator Distances

The canonical comparison number below is admitted only as a comparison/reuse
number, not as a derived value, fit target, or repinning input. The
`0.592817119605` number is the existing matrix-element/marginal
readout, not a new comparator.

```text
k=0: P2 = 0.429196712321; P3 = 0.429196712321; higher_L1 = 0.000000000000; |P3 - P_trivial3| = 0.000000000000; |P3 - P_marginal3| = 0.163620407284; |P3 - 0.5934| = 0.164203287679
k=1: P2 = 0.431504881786; P3 = 0.487332641164; higher_L1 = 0.720753266493; |P3 - P_trivial3| = 0.058135928843; |P3 - P_marginal3| = 0.105484478441; |P3 - 0.5934| = 0.106067358836
k=2: P2 = 0.432465615318; P3 = 0.524083379824; higher_L1 = 0.943987938485; |P3 - P_trivial3| = 0.094886667503; |P3 - P_marginal3| = 0.068733739781; |P3 - 0.5934| = 0.069316620176
k=3: P2 = 0.432836697103; P3 = 0.536381703306; higher_L1 = 1.033609675074; |P3 - P_trivial3| = 0.107184990985; |P3 - P_marginal3| = 0.056435416299; |P3 - 0.5934| = 0.057018296694
k=5: P2 = 0.433030156204; P3 = 0.542223091293; higher_L1 = 1.081483179565; |P3 - P_trivial3| = 0.113026378972; |P3 - P_marginal3| = 0.050594028312; |P3 - 0.5934| = 0.051176908707
k=8: P2 = 0.433060212494; P3 = 0.543094536619; higher_L1 = 1.088994966639; |P3 - P_trivial3| = 0.113897824298; |P3 - P_marginal3| = 0.049722582986; |P3 - 0.5934| = 0.050305463381
k=12: P2 = 0.433061847558; P3 = 0.543141664312; higher_L1 = 1.089404185700; |P3 - P_trivial3| = 0.113944951991; |P3 - P_marginal3| = 0.049675455293; |P3 - 0.5934| = 0.050258335688
k=20: P2 = 0.433061880367; P3 = 0.543142609685; higher_L1 = 1.089412397728; |P3 - P_trivial3| = 0.113945897364; |P3 - P_marginal3| = 0.049674509920; |P3 - 0.5934| = 0.050257390315
k=inf: P2 = 0.433061880380; P3 = 0.543142610051; higher_L1 = 1.089412400909; |P3 - P_trivial3| = 0.113945897730; |P3 - P_marginal3| = 0.049674509554; |P3 - 0.5934| = 0.050257389949
```

## Negative-Claim Discipline Gate

This gate is for the narrow finite-packet statement only: the
`eta_k = tensor_word^k e_(0,0)` depth ladder and its Perron-boundary limit do
not equal the three-word marginal readout at displayed precision. It is not a
claim about every possible physical rim-boundary construction.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Unit boundary `eta_0 = e_(0,0)` | Reproduces the trivial-slice row `P3 = 0.429196712321`, not the marginal row. | ATTEMPTED |
| Constructed depth-1 rim `eta_1 = tensor_word e_(0,0)` | Reproduces the rim-boundary row `P3 = 0.487332641164`, still below the marginal row. | ATTEMPTED |
| Deeper finite depths `k = 2, 3, 5, 8, 12, 20` | The measured `P3` values rise monotonically but approach the Perron-boundary value near `0.543142610051`. | ATTEMPTED |
| Tensor-word Perron boundary `eta_inf` | Direct Perron-vector readout gives `P3 = 0.543142610051`, with marginal-branch divergence `0.049674509554`. | ATTEMPTED |
| Two-word convergence cross-check | The same eta ladder has a stable two-word limit `P2 = 0.433061880380`, so the three-word landing is not a divergent-in-truncation artifact in this packet. | ATTEMPTED |
| Marginal readout convention | The existing marginal row remains reproducible, but it is a different readout convention from the eta-weighted boundary ladder. | ATTEMPTED |

**N2 wall independence audit.** Collapsed wall set:

| wall | meaning |
|---|---|
| W1 | finite word count `1`, `2`, `3` only |
| W2 | finite tensor/source boxes and finite Bessel mode support |
| W3 | no physical 3D unmarked spatial Wilson environment computation |
| W4 | no all-weight, untruncated, or `L_perp` limit |
| W5 | no analytic `P(6)` or canonical repinning |

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| W1/W2 | no | no | yes |
| W1/W3 | no | no | yes |
| W1/W4 | no | no | yes |
| W1/W5 | no | no | yes |
| W2/W3 | no | no | yes |
| W2/W4 | no | no | yes |
| W2/W5 | no | no | yes |
| W3/W4 | no | no | yes |
| W3/W5 | no | no | yes |
| W4/W5 | no | no | yes |

**N3 hidden-wall scan.** The load-bearing computation is the displayed eta
ladder plus the runner table. "Canonical" appears only in fenced
comparison-number reporting and in the named residual "no canonical
repinning"; it is non-load-bearing. No "new axiom", "framework provides",
"standard QFT", or "obviously" step is used to move the number.

**N4 residual matching.** No prior negative row is used as a witness. The
current target is the boundary-state residual named by
[GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md)
and
[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md):
whether a deeper finite rim-boundary ladder moves the derived
matrix-element readout toward the marginal row. The current runner
attacks that same finite-packet residual by measuring the eta-depth ladder.

**N5 rhetoric audit.** The phrase "does not revive the marginal branch" is
limited to this finite packet: tensor `NMAX = 4`, tensor `MODE_MAX = 80`,
source `NMAX = 7`, source `MODE_MAX = 200`, word counts up to `3`, and the
eta-depth ladder defined above. It is not asserted for all boxes, all word
counts, a physical 3D slab, or an untruncated `L_perp` limit.

**N6 partial-closure path scan.** Possible future paths remain: a full
`P_cls B_6(W)` rim evaluation, a broader finite rim/far support packet, an
`L_perp` propagation study, an all-weight tensor-transfer theorem, or a
separate derivation that identifies the marginal readout with a boundary law.
This note does not say that any path needs a new axiom, and it does not use
primitive-absence wall language.

**N7 steelman.** A reviewer can fairly argue that the eta-depth ladder here
iterates the finite local tensor word from `e_(0,0)`, while the physical rim
object named by the tensor-transfer and rim-lift authorities is the compressed
rim integral `P_cls B_beta(W)`. That full object could have support, weights,
dimension factors, or propagation behavior not represented by powers of this
25-state packet, and a later theorem could still make the marginal readout a
finite-word boundary law on a different surface. This note accepts that
objection and keeps the claim to the measured packet.

**N8 cross-cycle echo.** The same boundary-character residual appears in
the spatial-environment transfer lane and the source-sector readout lane,
including
[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
and
[GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md).
It is not retired here. The mechanism that would change the result is the
same one named there: evaluate or derive a different full rim-boundary state,
then re-read the finite ladder.

Gate result: PASS for the bounded finite-packet negative only.

## Named Residuals

- finite word count only;
- finite dominant-weight box and finite Bessel mode support only;
- no physical 3D unmarked spatial Wilson environment computation;
- no all-weight or untruncated convergence proof;
- no `L_perp` limit;
- no analytic `P(6)`;
- no canonical repinning.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gauge_vacuum_plaquette_rim_depth_ladder_deep_rim_limit_2026_06_12.py
```

Expected tail:

```text
TOTAL: PASS=22, FAIL=0
```

Cache refresh command:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_rim_depth_ladder_deep_rim_limit_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
