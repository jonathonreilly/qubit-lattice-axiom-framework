# Gauge-Vacuum Plaquette Rim-Boundary Eta-Env Constructed Readout

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite construction of the rim-boundary vector on the
existing tensor-word packet at `beta = 6`, tensor `NMAX = 4`,
tensor `MODE_MAX = 80`, followed by a matrix-element-bond re-read of the
one/two/three-word ladder through the existing source-sector Perron machinery
at source `NMAX = 7`, source `MODE_MAX = 200`. This note does not compute the
physical 3D unmarked spatial Wilson environment, an all-weight or untruncated
tensor-transfer Perron state, an `L_perp` limit, analytic `P(6)`, or a
canonical repinning.

**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** `scripts/gauge_vacuum_plaquette_rim_boundary_eta_env_constructed_readout_2026_06_12.py`

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the finite tensor-transfer ingredient language and the open
  boundary-character target.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `tensor_word` construction and its `boundary0`/`amp`
  surface.
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
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934` used only in fenced
  distance reporting.

No literature value, new axiom, external citation, fitted selector, or new
comparator number is used.

## Defining Lines Read

The tensor-transfer note supplies the local character weight:

```text
exp[(beta/3) Re Tr U_p] = sum_lambda d_lambda c_lambda(beta) chi_lambda(U_p),
```

and the open target:

```text
z_(p,q)^env(beta)
  = <chi_(p,q), (T_beta^env,tensor)^(L_perp-1) eta_beta^env>,

rho_(p,q)(beta)
  = z_(p,q)^env(beta) / z_(0,0)^env(beta).
```

It also says `eta_beta^env` is the exact positive boundary state induced by
the rim coupling of the marked plaquette to the unmarked environment. The
finite packet does not evaluate that full object.

The rim-lift note defines the rim variables and plaquettes:

```text
Xi^rim denote the unmarked Wilson link variables in the finite rim
neighborhood touching that marked plaquette and the edge slice.
```

and partitions plaquettes as:

```text
Omega^rim: the rim neighborhood of unmarked plaquettes that touch both
  the marked plaquette and the edge slice;
Omega^far: the remainder of the unmarked plaquettes.
```

The same note gives the rim Boltzmann/Haar integral:

```text
B_beta(W)(U)
 = integral_(Omega^rim(U)) dmu_H(Xi^rim)
     exp[(beta / 3) A^rim(U, Xi^rim; W)],
```

and the compressed descendant:

```text
eta_beta(W) = P_cls B_beta(W).
```

The `SU(3)` product-Fubini note records the supplied finite support split:

```text
Xi = Xi^rim sqcup Xi^far,
```

with

```text
A(U,W; Xi) = A^rim(U,W; Xi^rim) + A^far(U; Xi^far) + A^0(U,W),
```

and says the marked class-sector data carried by the rim factor is
`P_cls B_beta(W)`.

The finite tensor-word packet supplies the actual finite local object used
here:

```text
diag_c := diag(c_(p,q)(6) / (d_(p,q) c_(0,0)(6))),
N_f, N_fbar := SU(3) fundamental / anti-fundamental fusion matrices,
tensor_word := diag_c * (N_f + N_fbar) * diag_c * (N_f + N_fbar)^T * diag_c.
```

It also supplies the old unit-boundary readout:

```text
boundary0 = e_(0,0),
amp := tensor_word * boundary0.
```

## Construction Choice

On the finite packet, the rim factor is the one explicit Wilson/fusion word
available after compression. The supplied far side is the trivial far boundary
`e_(0,0)`. Therefore the constructed finite rim-boundary vector is

```text
eta_constructed := tensor_word * e_(0,0).
```

The finite word is symmetric on this packet, so applying it from the left or
right gives the same component vector after identifying the class-sector basis.
The scalar normalization is irrelevant for `rho`; the runner reports both
unnormalized `eta` and normalized `eta / eta_(0,0)`.

The finite ladder readout replaces the old unit vector on unmarked word slots:

```text
rho_lambda^(k, eta)
  = sum_(other word labels) psi_k(lambda, other labels)
      product_(unmarked slots j) eta_constructed(label_j)
    / same expression with lambda = (0,0).
```

For one word there is no unmarked word slot, so the ladder anchor remains the
existing one-word tensor Perron readout. The runner also reports a separate
`eta` coefficient control, namely `eta / eta_(0,0)` used directly as a
`rho` vector; that is not the one-word Perron ladder anchor.

## Constructed Eta

At `beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`:

```text
eta_(0,0) = 0.845063479299967
higher-weight L1 mass = 0.609082263099655
total L1 mass = 1.454145742399622
higher L1 / eta_(0,0) = 0.720753266493
higher L1 / total L1 = 0.418859159258
higher L2 / eta_(0,0) = 0.353323610429
higher L2 / total L2 = 0.333140744640
```

The nonzero support after normalization by `eta_(0,0)` is:

| weight | `eta` | `eta / eta_(0,0)` |
|---:|---:|---:|
| `(0,0)` | `0.845063479299967` | `1.000000000000` |
| `(1,0)` | `0.178533071011641` | `0.211265869825` |
| `(0,1)` | `0.178533071011641` | `0.211265869825` |
| `(1,1)` | `0.137119830699031` | `0.162259799480` |
| `(2,0)` | `0.057448145188670` | `0.067980863682` |
| `(0,2)` | `0.057448145188670` | `0.067980863682` |

Thus the trivial slice `e_(0,0)` is the special zero-higher-weight case, and
the constructed finite rim vector is not that special case.

## Baseline Gate

The runner first reproduces the existing one-word and matrix-element
readouts:

| words | readout | `rho_(1,0)` | `rho_(1,1)` | `P(6)` |
|---:|---|---:|---:|---:|
| 1 | one-word anchor | `0.378514922317` | `0.171042019092` | `0.434215413260` |
| 2 | matrix-element / trivial slice | `0.211265869825` | `0.162259799480` | `0.429196712321` |
| 2 | matrix-element / marginal | `0.448136509420` | `0.162403385294` | `0.436251149956` |
| 3 | matrix-element / trivial slice | `0.211265869825` | `0.162259799480` | `0.429196712321` |
| 3 | matrix-element / marginal | `22.802148174123` | `0.162354707873` | `0.592817119605` |

## Constructed-Boundary Re-Read

Under the derived matrix-element bond and the constructed `eta` boundary on
unmarked word slots:

| words | readout | `rho_(1,0)` | `rho_(1,1)` | `P(6)` |
|---:|---|---:|---:|---:|
| 1 | one-word anchor | `0.378514922317` | `0.171042019092` | `0.434215413260` |
| 2 | matrix-element / constructed eta | `0.287722573724` | `0.162297788516` | `0.431504881786` |
| 3 | matrix-element / constructed eta | `2.570788717063` | `0.162266447734` | `0.487332641164` |

The direct `eta / eta_(0,0)` coefficient control gives

```text
rho_(1,0) = 0.211265869825
rho_(1,1) = 0.162259799480
P = 0.429196712321
```

This is expected because `eta = tensor_word e_(0,0)` is the old
trivial-slice column. It is reported only to separate the boundary-vector
coefficient control from the one-word Perron ladder anchor.

## Fenced Comparator Distances

The canonical comparison number below is admitted only as a comparison/reuse
number, not as a derived value, fit target, or repinning input.

```text
one-word anchor:
P = 0.434215413260
|P - P_loc_reference| = 0.018191745785
|P - P_triv_reference| = 0.011683673613
|P - 0.5934| = 0.159184586740

two-word matrix_element constructed_eta:
P = 0.431504881786
|P - P_loc_reference| = 0.020902277259
|P - P_triv_reference| = 0.008973142139
|P - 0.5934| = 0.161895118214
direction_vs_tw1 = away by 0.002710531474

three-word matrix_element constructed_eta:
P = 0.487332641164
|P - P_loc_reference| = 0.034925482119
|P - P_triv_reference| = 0.064800901517
|P - 0.5934| = 0.106067358836
direction_vs_tw1 = toward by 0.053117227904

three-word classification:
constructed_eta is neither the trivial-slice stationary value
0.429196712321 nor the marginal revival value 0.592817119605.
It is closer to the trivial-slice P-distance in this finite box.
```

## Bounded Result

The constructed finite packet rim boundary is not `e_(0,0)`: it has
measured higher-weight content. Replacing the old `e_(0,0)` readout on
unmarked word slots by this constructed `eta` changes the matrix-element
ladder:

```text
0.434215413260 -> 0.431504881786 -> 0.487332641164.
```

So at the tested finite packet, the constructed boundary does not behave like
the stationary trivial slice, and it does not behave like the three-word
marginal revival. It is an intermediate finite readout, closer to the
trivial-slice value than to the marginal revival at three words.

## No-Go Discipline Gate

Skill freshness: `origin/main` had a readable `no-go-discipline` skill body;
the current worktree was dirty, so no worktree update was attempted. This
section follows the `origin/main` skill text.

This gate is for the narrow finite statement only: the constructed finite
packet `eta` readout is not the three-word marginal revival. It is not a claim
that the physical rim-boundary route is unavailable.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Unit boundary `e_(0,0)` | Reproduced the old trivial-slice ladder `0.4342 -> 0.4292 -> 0.4292`; it is not the constructed rim vector. | ATTEMPTED |
| Marginal readout | Reproduced the old two/three-word marginal rows, including `0.592817119605`; it is not selected by `eta = tensor_word e_(0,0)`. | ATTEMPTED |
| Constructed `eta` on unmarked slots | Implemented directly; three-word `P = 0.487332641164`. | ATTEMPTED |
| Direct `eta` coefficient control | Implemented separately; gives `P = 0.429196712321`, but this is not the one-word Perron ladder anchor. | ATTEMPTED |
| Left/right rim-word convention | The finite word is symmetric on this packet, so left/right application gives the same component vector. | ATTEMPTED |
| Full physical rim `B_6` / `eta_6` | Not evaluated here; remains a named residual and could change the readout. | NAMED RESIDUAL |

**N2 wall independence.** The collapsed residual set is: finite word count;
finite dominant-weight box and Bessel support; no physical 3D unmarked spatial
Wilson environment computation; no all-weight or untruncated convergence
proof; no `L_perp` limit; no analytic `P(6)`; no canonical repinning. Closing
one of these does not automatically close the others.

**N3 hidden-wall scan.** The load-bearing construction is the displayed
`eta = tensor_word e_(0,0)` plus direct runner readout. "Canonical" appears
only in the Peter-Weyl/comparator context inherited from source notes and is
not used as a hidden selection rule. The physical rim/far support partition,
compression bridge, and untruncated environment are explicit residuals, not
silent inputs.

**N4 residual matching.** The residual attacked here is exactly the
in-flight N7 objection that the true rim boundary need not equal the unit
vector. This note constructs the finite packet rim vector and re-reads the
finite ladder. It does not cite earlier no-go rows as witnesses against the
full physical rim problem.

**N5 rhetoric audit.** Phrases such as "does not behave like marginal" mean
only the finite `NMAX = 4`, `MODE_MAX = 80`, one/two/three-word constructed
readout above. They do not assert a lattice-wide, all-volume, or physical
3D negative.

**N6 partial-closure path scan.** A future full rim-boundary evaluation, a
larger finite rim/far support packet, an `L_perp` propagation study, or an
untruncated tensor-transfer theorem could produce a different `eta_beta^env`
and require a re-read. Those paths are not blocked.

**N7 steelman.** A hostile reviewer can fairly say that `tensor_word e_(0,0)`
is only the finite packet's local rim column, not the full `P_cls B_6(W)` of
the physical Wilson slab. The true `eta_beta^env` could have broader support,
different dimension factors after a full compression bridge, or nontrivial
`L_perp` propagation that moves the readout toward the marginal branch. This
note accepts that steelman and therefore keeps the claim finite.

**N8 cross-cycle echo.** The same boundary-state residual appears in the
spatial-environment transfer/tensor-transfer lane and the source-sector
Perron solve lane. This row answers one finite-packet construction question;
it does not retire the broader physical boundary-character measure residual.

Gate result: PASS for the bounded finite-packet statement only.

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
PYTHONPATH=scripts python3 scripts/gauge_vacuum_plaquette_rim_boundary_eta_env_constructed_readout_2026_06_12.py
```

Expected tail:

```text
TOTAL: PASS=20, FAIL=0
```

Cache refresh command:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_rim_boundary_eta_env_constructed_readout_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
