# Gauge-Vacuum Plaquette Tensor-Word Perron-Derived Rho Composed Readout

**Date:** 2026-06-11
**Type:** bounded_theorem
**Claim boundary:** finite bounded computation on the tensor-word truncation
`0 <= p,q <= NMAX`, with the primary readout at tensor-word `NMAX = 4`,
`MODE_MAX = 80`, `beta = 6`, composed into the existing source-sector Perron
machinery at source `NMAX = 7`, `MODE_MAX = 200`. This source note does not
compute the physical 3D unmarked spatial Wilson environment, the untruncated
tensor-transfer Perron state, the multi-word tensor-transfer limit, the
`L_perp` limit, an analytic plaquette value, or any canonical repinning.

**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** scripts/gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11.py

## Inputs

The one-hop authorities for the finite computation are:

- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source-sector operator
  `T_src(6) = exp(3J) D_6^loc C_(Z_6^env) exp(3J)` and the two reference
  solves.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  and
  [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite 25-state tensor-word matrix and its nonnegativity,
  conjugation-swap, and boundary-readout checks.
- [GAUGE_VACUUM_PLAQUETTE_PERRON_JACOBI_UNDERDETERMINATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_PERRON_JACOBI_UNDERDETERMINATION_NOTE.md)
  for the remaining residual: an explicit residual source-sector environment
  operator, or an equivalent Perron eigenvector construction once the local
  factor is fixed.
- [GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md)
  for the unnormalized per-weight formal convolution packaging (coefficient
  dictionary only, not an independent unmarked-DOF environment derivation).
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md)
  and
  [GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
  for the normalized finite coefficient convention `rho_(0,0)=1` and the
  single-link comparison packet.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse-number license used in the fenced
  comparator block below.

No literature value, new axiom, external citation, or fitted selector is used.

## Anchor Gate

The runner first rebuilds the finite tensor-word matrix at `NMAX = 4`,
`MODE_MAX = 80` and cross-checks it against the existing tensor runner's
construction:

```text
tensor-word shape: 25 x 25
tensor-word min entry: 0.000000000000e+00
tensor-word conjugation-swap residual: 1.387778780781e-17
boundary readout min entry: 0.000000000000e+00
cross-check against existing tensor runner construction: 0.000000000000e+00
```

It then reproduces the source-sector reference Perron solves at source
`NMAX = 7`, `MODE_MAX = 200`:

```text
P_loc(6)  = 0.452407159045
P_triv(6) = 0.422531739647
```

The runner treats any anchor drift as a stop condition. The completed run has:

```text
TOTAL: PASS=17 FAIL=0
```

## Derived Rho

Let `psi_tw` be the Perron eigenvector of the finite tensor-word matrix. The
finite boundary-character readout used here is

```text
rho^tw_(p,q)(6) = psi_tw[p,q] / psi_tw[0,0].
```

This is the normalized finite amplitude ratio `z_(p,q)/z_(0,0)` named by the
boundary-character law. It matches the normalized convention of the finite
character-measure packet by setting `rho^tw_(0,0)=1`; no dimension factor is
inserted in this ratio. The single-link comparison remains the separate
coefficient packet `c_(p,q)(6)/(d_(p,q)c_(0,0)(6))`.

Runner readout:

```text
tensor-word Perron eigenvalue: 1.012369912748
psi residual infinity norm: 1.665334536938e-16
rho_tw min on available box: 2.286765266123e-23
rho_tw conjugation-symmetry residual: 5.551115123126e-17
```

Selected values:

| `(p,q)` | `rho^tw` | single-link `c/(d c00)` | relative difference |
|---:|---:|---:|---:|
| `(0,0)` | `1.000000000000e+00` | `1.000000000000e+00` | `0.000000e+00` |
| `(1,0)` | `3.785149223171e-01` | `4.225317396500e-01` | `1.041740e-01` |
| `(1,1)` | `1.710420190918e-01` | `1.622597994799e-01` | `5.412443e-02` |
| `(2,0)` | `7.570581877783e-02` | `1.359617273634e-01` | `4.431829e-01` |
| `(2,1)` | `3.962593031883e-03` | `4.828805556745e-02` | `9.179384e-01` |
| `(2,2)` | `4.937702387904e-05` | `1.350507888830e-02` | `9.963438e-01` |
| `(4,4)` | `2.286765266123e-23` | `2.275225312476e-05` | `1.000000e+00` |

The full 25-weight table is printed by the runner, including comparison to
`rho=1` and absolute distance from the `rho=delta` reference. Relative distance
to the `rho=delta` reference is undefined off `(0,0)` because the denominator
is zero, so the runner prints the absolute delta-reference difference there.

## Composed Readout

The primary source-sector embedding treats the finite tensor-word packet as a
finite class-polynomial readout and zero-extends uncomputed tensor-word weights
outside the available word box before feeding the diagonal sequence into the
source `NMAX = 7` Perron solve. The runner also tests a positive-tail
sensitivity with uncomputed source-box weights set to `rho=1`, and a matched
source-box solve restricted to `NMAX = 4`.

```text
embedding       source_NMAX   P(6)            u0              alpha_s(alpha_bare=1)   Perron eigenvalue
zero-extension       7        0.434215413260  0.811757498148  1.517565281371          3.577553737908
positive-tail        7        0.434215413260  0.811757498148  1.517565281371          3.577553737908
matched-box          4        0.434210050581  0.811754991780  1.517574652630          3.577542372089
```

The zero-extension and positive-tail embeddings differ by `1.077e-14` in
`P(6)` on the source `NMAX = 7` box. The matched-box source solve differs from
the primary readout by `5.363e-06`.

This note names

```text
P^tw(6) = 0.434215413260
u0^tw   = 0.811757498148
alpha_s^tw(v; alpha_bare=1) = 1.517565281371
```

as the finite zero-extended composed readout.

## Truncation Drift

The tensor-word truncation sweep is stable on the printed cells:

| `NMAX_tw` | `MODE_MAX` | `rho^tw_(1,0)` | `rho^tw_(1,1)` | `P^tw_zero_ext(6)` |
|---:|---:|---:|---:|---:|
| 3 | 80 | `0.378514922289` | `0.171042019072` | `0.434215413259` |
| 3 | 200 | `0.378514922289` | `0.171042019072` | `0.434215413259` |
| 4 | 80 | `0.378514922317` | `0.171042019092` | `0.434215413260` |
| 4 | 200 | `0.378514922317` | `0.171042019092` | `0.434215413260` |
| 5 | 80 | `0.378514922317` | `0.171042019092` | `0.434215413260` |
| 5 | 200 | `0.378514922317` | `0.171042019092` | `0.434215413260` |
| 6 | 80 | `0.378514922317` | `0.171042019092` | `0.434215413260` |
| 6 | 200 | `0.378514922317` | `0.171042019092` | `0.434215413260` |

Sweep spans:

```text
span P_zero across sweep: 8.739675649849e-13
span rho10 across sweep: 2.802436060989e-11
span rho11 across sweep: 1.945871241915e-11
```

Verdict on this finite ladder: converging on the tested cells, not wandering.
This is not an untruncated convergence proof.

## Family Exclusion

Each of the three enumerated one-parameter families is fitted to
`rho^tw_(1,0)` and then measured on the remaining finite tensor-word weights.

| family | fitted parameter | domain note | maximum relative mismatch |
|---|---:|---|---:|
| `exp(-tau(p+q))` | `tau = 0.971499782002` | inside `tau >= 0` | `1.842648e+19` at `(4,4)` |
| `c_(p,q)(beta_env)/c_(0,0)(beta_env)` | `beta_env = 1.965846209685` | inside `beta_env >= 0` | `1.446280e+16` at `(4,4)` |
| `(c_(p,q)(6)/c_(0,0)(6))^k` | `k = -4.097053477418` | unconstrained real fit; outside enumerated `k >= 0`; constrained `k=0` already misses the fit weight by `1.641904e+00` relative | `1.180715e+33` at `(4,4)` |

Thus the finite `rho^tw` object lies outside the three tested family forms on
the available tensor-word box after the stated `rho_(1,0)` fit. This is a
measured finite-box family exclusion, not a statement about untested families
or the physical all-weight environment.

## Comparator Distances

The reuse license from
[PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
is applied here: the canonical comparison number in the fenced block is an
admitted comparison/reuse number, not a value derived by this note, not a fit
target, and not a repinning input.

```text
canonical comparison/reuse number: 0.5934
|P_tw - P_loc_reference| = 0.018191745785
|P_tw - P_triv_reference| = 0.011683673613
|P_tw - 0.5934| = 0.159184586740
```

## Bounded Statement

On the finite one-word tensor-transfer truncation at `beta = 6`, the Perron
eigenvector of the explicit 25-state tensor-word matrix gives normalized
coefficients `rho^tw_(p,q)(6) = psi_tw[p,q]/psi_tw[0,0]`. The runner verifies
positive available-box coefficients, conjugation symmetry, stable tested
truncation drift, and measured mismatch from each of the three enumerated
source-sector family forms after fitting to `rho^tw_(1,0)`. Feeding the finite
zero-extended `rho^tw` into the existing source-sector Perron machinery gives
the definite finite readout `P^tw(6) = 0.434215413260`.

Named residuals:

- finite one-word tensor box is not the physical 3D unmarked spatial Wilson
  environment;
- multi-word coverage, untruncated tensor-transfer convergence, and the
  `L_perp` limit remain open;
- the zero-extension is a finite-support embedding of the computed word packet,
  not an all-weight residual environment theorem;
- no analytic `P(6)` is supplied;
- no canonical repinning is supplied;
- the structural underdetermination statement remains untouched. This row adds
  one constructed finite candidate inside the named Perron-eigenvector route
  from the underdetermination note; it does not prove that candidate is the
  physical environment.

## No-Go Discipline Source Gate

This gate controls the negative wording "outside the three tested family
forms" on the finite box. It is a source-side rhetoric check, not an audit
outcome.

**N1 alternative route enumeration.**

| route | attempt | result |
|---|---|---|
| Decay family | Fit `tau` to `rho^tw_(1,0)` and compare remaining weights. | ATTEMPTED: max relative mismatch `1.842648e+19`. |
| One-plaquette family | Fit `beta_env` to `rho^tw_(1,0)` and compare remaining weights. | ATTEMPTED: max relative mismatch `1.446280e+16`. |
| Tube-power family | Fit real `k` to `rho^tw_(1,0)` and compare remaining weights. | ATTEMPTED: exact fit requires `k=-4.097053477418`, outside the enumerated `k>=0` domain; even that real extension has max relative mismatch `1.180715e+33`. |
| Padding artifact | Change the source-box tail from zero-extension to positive `rho=1` tail. | ATTEMPTED: `P(6)` changes by `1.077e-14`; family mismatch is measured before source padding, on the tensor-word box. |
| Truncation artifact | Sweep tensor `NMAX in {3,4,5,6}` and `MODE_MAX in {80,200}`. | ATTEMPTED: `P_zero` span is `8.739675649849e-13`; `rho10` and `rho11` spans are `2.802436060989e-11` and `1.945871241915e-11`. |

**N2 wall independence.** The finite statement has three explicit boundaries:
finite one-word tensor box, finite source embedding, and three-family
comparison. None is presented as an independent physical wall; they are the
conditions under which the printed numbers are meaningful.

**N3 hidden-wall scan.** The note uses no new axiom, literature comparator,
fitted selector, physical 3D environment, untruncated tensor-transfer
convergence, or status implication. The canonical comparator appears only in
the fenced comparison block under the reuse license.

**N4 residual matching.** The cited underdetermination residual is the lack of
a forced residual source-sector environment operator after the local factor is
fixed. This note does not claim that residual is resolved physically; it supplies
a finite constructed candidate in the named Perron-eigenvector route.

**N5 rhetoric audit.** "Outside the three tested family forms" means outside
those three forms on the printed finite tensor-word box after the stated
`rho_(1,0)` fit. It does not speak about other families, other normalizations,
multi-word tensor-transfer operators, all-weight limits, or the physical
environment.

**N6 partial-path scan.** The tensor-word Perron vector is a partial
construction path, not a new axiom. The open follow-up is to extend the
boundary-character Perron solve beyond one finite word and finite weight boxes.

**N7 steelman.** A reviewer can correctly argue that the physical all-weight
Perron vector of the full spatial tensor-transfer operator may differ from this
one-word finite vector, and that a different exact boundary-state normalization
could alter the all-weight coefficients. This note accepts that objection as a
named residual and keeps the claim finite.

**N8 cross-cycle echo.** The earlier source-sector Perron row already narrowed
its family statement when a separate finite Schur construction existed outside
the three enumerated families. This note follows the same discipline: it reports
one constructed finite candidate outside those families and leaves the broader
physical environment target open.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11.py
```

Expected tail:

```text
TOTAL: PASS=17 FAIL=0
```

Cache refresh command:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
