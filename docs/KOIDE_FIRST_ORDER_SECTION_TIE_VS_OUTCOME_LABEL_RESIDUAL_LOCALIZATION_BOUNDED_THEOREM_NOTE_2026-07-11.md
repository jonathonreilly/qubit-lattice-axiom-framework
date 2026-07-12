# Koide First-Order Section Fork: Weight-Stage Versus Outcome-Stage K-Reality (Bounded Residual Localization)

**Date:** 2026-07-11
**Claim type:** bounded_theorem
**Status:** **UNDECIDED WITH EXACT RESIDUAL**; source-side bounded
classification; independent audit required.
**Status authority:** independent audit lane. This note does not set, predict,
promote, or demote an audit result and does not adopt a premise.
**Primary runner:**
[`scripts/frontier_koide_first_order_section_question_2026_07_11.py`](../scripts/frontier_koide_first_order_section_question_2026_07_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_first_order_section_question_2026_07_11.txt`](../logs/runner-cache/frontier_koide_first_order_section_question_2026_07_11.txt)

## Boundary

This note classifies a two-stage fork on the declared `C_3` circulant probe

```text
W(a,b,c) = a I + b C + c C^2,       C^3 = I.
```

The one-component Grassmann calculation gives one power of

```text
Z(a,b,c) = det W = a^3 + b^3 + c^3 - 3abc.
```

There are then two analytic prescriptions:

1. **weight-stage K-reality:** impose `c = conj(b)` on the coupling section
   before classifying the weight's analytic dependence;
2. **outcome-stage K-reality:** keep `b,c` independent through the
   holomorphic calculation and impose K-real grouping only on the registered
   data afterward.

The runner proves that these prescriptions differ in analytic type but agree
pointwise after restriction to the same K-real locus. It does **not** select a
physical prescription. It also recomputes two conditional endpoint equations:
the supplied per-outcome-cell law gives `r = 1/2`, while the supplied
per-real-mode law gives `r = 1`. It does **not** derive either weighting law or
prove that choosing a K-reality stage selects its associated endpoint.

Thus the result remains **UNDECIDED WITH EXACT RESIDUAL**. The stage question
is localized exactly to where K-reality is imposed. The value question still
contains the separate equipartition-granularity residual. In particular, no
fix in this review upgrades the note to a derivation of `r = 1/2` or `r = 1`.

All load-bearing source-note rows cited below are currently `unaudited`. Their
source-side results are used only at their declared scope; no audit grade is
imported.

## Exact calculations

### 1. First-power Grassmann determinant

On the `hw=1` corner triplet, the supplied rotation acts by the three-cycle
`C`. An explicit exterior-algebra expansion followed by nested Berezin
integration gives

```text
Z = det W = a^3 + b^3 + c^3 - 3abc
  = (a+b+c)(a+b omega+c omega^2)(a+b omega^2+c omega).
```

No determinant identity is assumed by the Grassmann engine (runner checks
1–4). This is a statement about the declared finite bilinear probe, not a
derivation of a physical charged-lepton Yukawa coupling.

### 2. The analytic stage classifier

With `b,c` independent, the doublet factor is the holomorphic polynomial

```text
a^2 + b^2 + c^2 - ab - ac - bc,
```

so its derivative with respect to the independent symbol `conj(b)` vanishes.
After the weight-stage restriction `c = conj(b)`, conjugate dependence is
present and

```text
partial_b partial_conj(b) det W = -3a,
Delta_(Re b, Im b) det W = -12a.
```

These identities classify when conjugacy is imposed (checks 5–6 and 12).
They do not turn holomorphy into an equipartition theorem.

### 3. Conditional endpoint arithmetic

The runner solves the two alternative equations without using the withdrawn
`rho`-map arithmetic:

```text
per-outcome-cell law:  3 a^2 = epsilon, 6 |b|^2 = epsilon
                       => r = |b|^2/a^2 = 1/2, Q = (1+2r)/3 = 2/3;

per-real-mode law:     3 a^2 = epsilon, 6 |b|^2 = 2 epsilon
                       => r = |b|^2/a^2 = 1,   Q = (1+2r)/3 = 1.
```

Check 7 certifies only these implications. The
[`orbit-occupancy independence note`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
explicitly records that the per-outcome-cell equation is conditional and is
not supplied by the realized-state primitive. The first-order determinant
does not change that status.

### 4. Transfer objects do not settle the measure question

The runner separately checks:

- `aI+bC` is generically non-self-adjoint because `C^T=C^2 != C` (check 8);
- the Hermitian block object `[[0,M],[M^dagger,0]]` has determinant
  `-|det M|^2` for the three-by-three block (check 9);
- a toy one-component Grassmann measure with real antisymmetric kinetic term
  still gives one determinant power (check 10).

These are distinct algebraic objects. The checks do not prove that the
physical first-order action is Osterwalder–Schrader positive, nor do they
show that reflection positivity is irrelevant.

### 5. Spatial corner reflections are convention-sensitive

For the finite periodic box used by the runner, the site-centered reflection
`x_mu -> -x_mu` acts as the identity on the corner plane waves, whereas the
link-centered reflection `x_mu -> 1-x_mu` acts by `(-1)^(n_mu)` on the corner
label `(n_1,n_2,n_3)` (check 11).

Therefore the finite spatial corner calculation does not reduce a full
Osterwalder–Schrader transformation to coupling conjugation. A full test still
needs the reflection center, time direction, field transformation, measure,
and positivity form. That is a live route for deciding the stage, not a route
closed by this note.

### 6. Pointwise K-real data are stage-blind

Restricting the holomorphic answer after the calculation and imposing the
same restriction before evaluation give the same polynomial on
`c = conj(b)`. On that common locus the circulant is Hermitian and has the
real spectrum

```text
lambda_k = a + 2 |b| cos(delta + 2 pi k/3).
```

Checks 13–15 verify a generic untied point has complex `Z`, the K-real locus
has real `Z`, and the determinant equals the product of the common real
spectrum. This establishes why K-real point values alone cannot identify the
stage. It does **not** exhibit a generic untied physical action as lawful and
does not establish a theta-sector or physical-mass identification.

## Result

> Within the source-defined two-cell fork, the exact structural distinction
> is the stage at which `c = conj(b)` is imposed: weight stage before analytic
> classification versus outcome stage after the holomorphic calculation.
> The determinant algebra localizes that distinction and leaves it
> undecided. The conditional `r = 1` and `r = 1/2` endpoints require their
> respective equipartition-granularity laws; selecting a stage alone does not
> derive either value.

This is the exact residual carried forward. A later theorem may test the full
first-order action and decide the stage. Such a theorem would answer the stage
question without, by itself, discharging the remaining value/equipartition
residual.

## No-Go Discipline Gate

**Status: PASS.** Although this is a bounded classification rather than a
global no-go, it contains negative statements about what the checked surface
does not decide, so the N1–N8 walk is mandatory.

**N1 — alternative routes.**

| route | attempt | disposition |
| --- | --- | --- |
| first-power Berezin determinant | Infer the physical stage from the single determinant power. | ATTEMPTED: the determinant is holomorphic before restriction and accepts either restriction order pointwise (checks 3, 14). |
| mixed Wirtinger derivative | Use `partial_b partial_conj(b) Z=-3a` to force the weight-stage prescription. | ATTEMPTED: the derivative diagnoses the already-imposed tied section; it does not require that section physically (checks 6, 12). |
| endpoint arithmetic | Use `r=1/2` or `r=1` as a selector. | ATTEMPTED: each endpoint follows only after its alternative equipartition equation is supplied (check 7). |
| second-order Hermitian block | Transfer `-|det M|^2` directly to the one-component measure. | ATTEMPTED: the runner separates the block transfer object from the first-power Grassmann measure (checks 9–10). |
| spatial reflection | Treat corner reflection as identity and infer that reflection positivity adds nothing. | ATTEMPTED: site- and link-centered reflections act differently, and no full positivity form is tested (check 11). |
| K-real spectrum | Use the common real spectrum or determinant phase to identify the stage. | ATTEMPTED: both restriction orders agree on the same K-real point data (checks 13–15). |

**N2 — wall independence.** The stage-selection residual and the
equipartition-granularity residual are independent. One may specify when
K-reality acts without choosing an energy law, or impose one of the two energy
laws without deriving when the physical action imposes K-reality. A future
Osterwalder–Schrader theorem could close the first while leaving the second
open.

**N3 — hidden-wall scan.** The `C_3` coupling is a declared probe, not a
derived Yukawa. One Grassmann pair per site and the staggered kinetic class are
inherited source-side inputs. The two equipartition equations are conditional.
The reflection center and full positivity form are unsupplied. Historical
admission wording has no premise authority because no admission premise class
exists. All cited scientific rows are currently `unaudited`.

**N4 — residual matching.**

| cited source | exact scope used here | match |
| --- | --- | --- |
| [`staggered first-order determinant note`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md) | first-power determinant and tied/untied analytic split | yes; physical selector not imported |
| [`channel-space holomorphy note`](KOIDE_GENERATION_CHANNEL_SPACE_HOLOMORPHY_CHANNEL_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-06-11.md) | source-side tied/untied classification | yes; broader channel claim remains unaudited |
| [`orbit-occupancy independence note`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md) | per-outcome-cell endpoint is conditional | yes |
| [`dynamical determinant route-pruning no-go`](KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md) | second-order transfer-family wall | yes; not transferred to the measure |
| [`Kähler–Dirac index-route no-go`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md) | `r=1` on its tested realization and an open one-slot route | yes; no global impossibility inferred |

**N5 — rhetoric audit.** The result is restricted to a finite bilinear
`C_3` corner probe and two named analytic prescriptions. It is not a theorem
about all matter actions, all reflection-positive measures, interacting
actions, gauge-sector contributions, or physical charged-lepton masses.

**N6 — partial-closure path.** No new axiom or primitive is required. A
framework-native theorem for the full first-order action could decide the
K-reality stage. A separate derivation of the weighting/equipartition law would
still be needed to select the value.

**N7 — steelman.** Grant the complete first-order determinant result, the
source-defined two-cell fork, and the common K-real spectrum. The two
restriction orders still agree pointwise, while their analytic derivatives
differ. Without an action-level stage theorem and a weighting law, the
strongest package does not select an endpoint.

**N8 — cross-cycle echo.** The result preserves the existing occupancy
independence wall and the declared-open one-slot route in the two source-side
no-go notes. It sharpens the live action-level route instead of declaring that
route impossible. No later retained theorem is cited as retiring either
residual.

## Scope and imports

- The `C_3` circulant is a declared probe coupling, not a derived physical
  Yukawa.
- The one-component Grassmann measure and kinetic-class surface are inherited
  from the
  [`staggered-Dirac realization gate`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  at its declared source scope.
- The open charged-lepton selector is recorded by the
  [`chain-of-custody note`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md),
  which explicitly gives historical admission language zero premise weight.
- The current
  [`Qualification`](MINIMAL_AXIOMS_2026-06-29.md#qualification)
  leaves non-fixed structure conditional or open; this note does not create an
  admission class.
- No measured value, fitted selector, empirical comparator, or audit verdict is
  consumed.

## Verification

```bash
python3 scripts/frontier_koide_first_order_section_question_2026_07_11.py
```

Expected: 16 `[PASS]` lines, residual disclosures,
`TOTAL: PASS=16 FAIL=0`, and a final verdict beginning
`UNDECIDED WITH EXACT RESIDUAL`.

Independent audit is required. The source note and runner do not set an
effective status.
