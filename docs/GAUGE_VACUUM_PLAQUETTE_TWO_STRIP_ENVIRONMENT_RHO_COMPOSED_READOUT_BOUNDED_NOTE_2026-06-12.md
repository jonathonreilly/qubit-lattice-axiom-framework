# Gauge-Vacuum Plaquette Two-Strip Environment Rho Composed Readout Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem

**Claim boundary:** finite two-strip environment-side computation at
`beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source
`NMAX = 7`, and source `MODE_MAX = 200`. The strip layer has two
transverse units, so the primary state space is `B_4 x B_4`, dimension
`25^2 = 625`. This note computes a first finite two-strip rho-production
rung and composes it through the existing source solve. It does not compute
the full physical `3D` unmarked spatial Wilson environment, a wider slab
limit, the strip-depth direction, a `3D` stack, an `L_perp` limit, analytic
`P(6)`, or a repinning.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. The comparison number `0.5934` is used only under
the existing plaquette reuse license as fenced comparison context.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite one-word construction
  `tensor_word := diag_c * (N_f + N_fbar) * diag_c * (N_f + N_fbar)^T * diag_c`.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the tensor-transfer construction language: one slice step has matrix
  elements that are finite sums of products of Wilson coefficients
  `c_lambda(beta)` and exact nonnegative `SU(3)` fusion/intertwiner
  multiplicities.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the marked/non-marked compression distinction and the normalized
  one-link coefficient `a_lambda(beta) = c_lambda(beta)/(d_lambda c_0(beta))`.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character-convolution and Schur-orthogonality dictionary used to
  keep the internal-link character channels diagonal/fusion-counted on this
  finite class-sector packet.
- [GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md)
  for the formal central-sequence convention
  `Z_beta^env(W) = lambda_env(beta) sum d_(p,q) r_(p,q)^env(beta) chi_(p,q)(W)`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source-sector Perron machinery with supplied `rho`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
  for the one-word rho normalization convention
  `rho^tw_(p,q) = psi_tw[p,q]/psi_tw[0,0]` and the composed one-word value.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934` only.

Context pointers, not one-hop authorities:
docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md,
docs/GAUGE_VACUUM_PLAQUETTE_WIDTH_REDUCTION_MAP_DERIVED_COUPLED_LIFT_BOUNDED_NOTE_2026-06-12.md.

## Construction

Let

```text
B_4 = {(p,q) : 0 <= p,q <= 4},
D_(p,q) = c_(p,q)(6)/(d_(p,q)c_(0,0)(6)),
M = N_f + N_fbar.
```

The one-word object is

```text
T_word = D M D M^T D.
```

For a two-strip layer, the state is a pair `(a,b) in B_4 x B_4`, where
`a` and `b` are the two transverse unit labels. This finite reading keeps
the pair state space free, dimension `25^2 = 625`; the internal link enters
as an environment-link diagonal pair factor rather than as a marked-sector
Haar delta.

The layer-to-layer bond is the word bond on each transverse unit:

```text
M_pair = M tensor M.
```

The trivial-channel cut has

```text
D_pair^cut(a,b) = D_a D_b,
T_cut = D_pair^cut M_pair D_pair^cut M_pair^T D_pair^cut.
```

This gives `T_cut = T_word tensor T_word`, so the cut is the factorized
control.

For the full internal environment link, the normalized Wilson class-function
character coefficients on the finite box are

```text
w_lambda = d_lambda D_lambda.
```

The primary internal-link factor is

```text
E_full(a,b) = 1 + sum_{lambda != (0,0)} w_lambda N_{a,b}^{lambda},
D_pair(a,b) = D_a D_b E_full(a,b),
T_strip = D_pair M_pair D_pair M_pair^T D_pair.
```

Here `N_{a,b}^{lambda}` is the exact finite `SU(3)` tensor-product
multiplicity generated by the runner from character decompositions and
cross-checked against the existing fundamental and antifundamental
recurrence matrices. The conjugate-orientation reading
`N_{a,bar(b)}^{lambda}` is also computed; on this symmetric finite packet it
agrees numerically with the product-orientation reading.

The notes do not fix every possible `6j`/matrix-element normalization for a
future all-link two-strip tensor. The runner therefore also reports a
dimension-stripped control

```text
E_D(a,b) = 1 + sum_{lambda != (0,0)} D_lambda N_{a,b}^{lambda}.
```

The primary reading is `E_full`, because it uses the full normalized
class-function coefficient `d_lambda D_lambda` named by the Wilson character
sum. The control records normalization sensitivity; it is not selected as the
primary environment-link reading.

The link roles are:

| link class | finite treatment |
|---|---|
| layer-to-layer | `M_pair = M tensor M`, the word-construction bond on each transverse unit |
| intra-layer internal | full environment character channels through `E_full(a,b)`; not the marked-sector `delta/d` compression |
| marked interface | compressed source interface; the readout is the left marginal of the strip Perron vector, normalized at `(0,0)` |

The boundary-character projection convention is

```text
rho_strip(a)
  = sum_b psi_strip(a,b) / sum_b psi_strip((0,0),b).
```

Right marginal equality is checked as a symmetry gate. The source embedding is
the same finite zero-extension used by the one-word composed readout.

## Gates

The finite state-space and fusion gates pass:

```text
one-word state count = 25
two-strip pair state count = 625
fusion table shape = (25, 25, 25)
fundamental recurrence mismatches = 0
antifundamental recurrence mismatches = 0
(1,0) x (0,1) = {(0, 0): 1, (1, 1): 1}
(1,1) x (1,1) = {(0, 0): 1, (0, 3): 1, (1, 1): 2, (2, 2): 1, (3, 0): 1}
```

The cut gate passes:

```text
cut max |T_cut - T_word tensor T_word| = 2.776e-17
cut marginal max |rho-rho_word| = 3.886e-16
cut trivial-slice max |rho-rho_word| = 4.441e-16
P(cut marginal) = 0.434215413259920
```

The full-character strip gates pass:

```text
internal factor min/max = 1.000000000000000 / 5.908774331064158
transfer min = 0.000e+00
transfer symmetry residual = 1.110e-16
Perron residual = 2.220e-15
psi_min = 3.893e-42
rho min/max = 1.694e-24 / 1.000e+00
left/right marginal residual = 6.661e-16
conjugation residual = 5.551e-16
```

The one-word source machinery is reproduced:

```text
P(rho_word) = 0.434215413259920
u0(rho_word) = 0.811757498147861
alpha_s(rho_word; alpha_bare=1) = 1.517565281370676
```

## Rho Table

| `(p,q)` | `rho_word` | `rho_strip full-character` | `strip/word` |
|---:|---:|---:|---:|
| `(0,0)` | `1.000000000000e+00` | `1.000000000000e+00` | `1.000000000000e+00` |
| `(0,1)` | `3.785149223171e-01` | `8.251793568626e-01` | `2.180044453231e+00` |
| `(0,2)` | `7.570581877783e-02` | `1.318942062003e-01` | `1.742193774924e+00` |
| `(0,3)` | `9.488300432729e-04` | `2.460536915169e-03` | `2.593232510516e+00` |
| `(0,4)` | `2.744981301341e-06` | `2.689142597034e-06` | `9.796578926496e-01` |
| `(1,0)` | `3.785149223171e-01` | `8.251793568626e-01` | `2.180044453231e+00` |
| `(1,1)` | `1.710420190918e-01` | `3.470173120560e-01` | `2.028842467474e+00` |
| `(1,2)` | `3.962593031883e-03` | `1.753066227175e-02` | `4.424038030325e+00` |
| `(1,3)` | `2.556269520369e-05` | `6.123817353261e-05` | `2.395607076823e+00` |
| `(1,4)` | `6.698526652901e-09` | `1.272127051574e-08` | `1.899114712073e+00` |
| `(2,0)` | `7.570581877783e-02` | `1.318942062003e-01` | `1.742193774924e+00` |
| `(2,1)` | `3.962593031883e-03` | `1.753066227175e-02` | `4.424038030325e+00` |
| `(2,2)` | `4.937702387904e-05` | `1.452270694314e-04` | `2.941187176189e+00` |
| `(2,3)` | `2.384722181200e-08` | `6.338609970215e-08` | `2.658007721061e+00` |
| `(2,4)` | `2.203570760518e-12` | `1.431555067305e-12` | `6.496524155043e-01` |
| `(3,0)` | `9.488300432729e-04` | `2.460536915169e-03` | `2.593232510516e+00` |
| `(3,1)` | `2.556269520369e-05` | `6.123817353261e-05` | `2.395607076823e+00` |
| `(3,2)` | `2.384722181200e-08` | `6.338609970215e-08` | `2.658007721061e+00` |
| `(3,3)` | `3.999837210632e-12` | `2.879012273503e-12` | `7.197823616047e-01` |
| `(3,4)` | `1.915080453821e-17` | `6.961376229670e-18` | `3.635030693243e-01` |
| `(4,0)` | `2.744981301341e-06` | `2.689142597034e-06` | `9.796578926496e-01` |
| `(4,1)` | `6.698526652901e-09` | `1.272127051574e-08` | `1.899114712073e+00` |
| `(4,2)` | `2.203570760518e-12` | `1.431555067305e-12` | `6.496524155043e-01` |
| `(4,3)` | `1.915080453821e-17` | `6.961376229670e-18` | `3.635030693243e-01` |
| `(4,4)` | `2.286765266123e-23` | `1.694121305209e-24` | `7.408374310675e-02` |

## Measurement

```text
P(rho_word) = 0.434215413259920
P(rho_strip full-character) = 0.447034890458824
P(rho_strip dimension-stripped control) = 0.439904783618900
P_deep_rim_k4 = 0.603630724651002
P_word_limit_rung20 = 0.615191992181771
P_word_limit = 0.615191992185898
0.5934 fenced comparator = 0.593400000000000
P_strip - P_word = 0.012819477198904
|P_word - 0.5934| = 0.159184586740080
|P_strip - 0.5934| = 0.146365109541176
|P_word_limit - 0.5934| = 0.021791992185898
distance_change_vs_word = 0.012819477198904
distance_closure_fraction_vs_word = 0.080532151142472
distance_ratio_strip_to_word = 0.919467848857528
distance_ratio_strip_to_word_limit = 6.716463015065305
```

Answer to the finite measurement question: on the primary full-character
two-strip reading, enriching the environment geometry moves the composed
readout toward the fenced comparator relative to the one-word rho. The movement
is `+0.012819477198904` in `P`, reducing the one-word comparator distance by
about `8.0532%`. This is a finite first-rung improvement, not a match: the
remaining distance is `0.146365109541176`, and it is still much larger than
the word-limit distance `0.021791992185898`.

The dimension-stripped control also moves in the same direction, but less:

```text
P = 0.439904783618900
P - P_word = 0.005689370358980
```

## Named Residuals

- finite two-strip first rung only;
- finite dominant-weight box `B_4` only;
- finite Wilson Bessel mode support only;
- internal-link normalization and future `6j`/intertwiner normalization remain
  open for a full two-strip tensor;
- strip-depth direction remains open;
- wider slab limit remains open;
- stacking the slab to the physical `3D` environment remains open;
- `L_perp` remains open;
- analytic `P(6)` remains open;
- no repinning is supplied.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=31, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
