# Born/gravity P3 perturbation tournament — Cycle 475

Date: 2026-07-19

Authority: none

Audit: unset

Admission target: none

## Result

Cycle 475 tests the missing perturbative step in Accessible Prediction premise
P3.  P3 is a supplied conditional premise that asserts

```text
|I3/I1| ~ epsilon^2,
|beta-1| ~ epsilon,
therefore |beta-1| ~ C sqrt(|I3/I1|).
```

The conditional scenario currently takes exponent `1/2` and `C=1` as inputs.
The exact three-path expansion shows why these are genuine law-level inputs.
For an amplitude deformation

```text
A -> A + epsilon f(A),
```

the Sorkin functional is exactly

```text
I3(epsilon) = L_f epsilon + Q_f epsilon^2,
```

because the zeroth-order quadratic inclusion cancels.  The **generic
first-order I3 coefficient** `L_f` need not vanish.  For the explicit cubic
deformation `f(A)=|A|^2 A`, both train and held fixtures have `L_f != 0`, so
the direct route is linear in small `epsilon`, not quadratic.

An equal **symmetric ±epsilon route** cancels the linear term and gives
`I3=Q_f epsilon^2` exactly.  This route constructively realizes the desired
square-root exponent when a candidate `beta=1+epsilon` is separately
supplied.  However its coefficient

```text
C = 1/sqrt(|Q_f/I1|)
```

differs between train and held.  The coefficient C is not universal on this
candidate family, and the train coefficient misses the held configuration
without refit.

An exact **phase-only route** `A -> exp(i epsilon |A|^2)A` changes phase while
leaving every detector weight and `I3` exactly unchanged.  Whether such a
phase deformation affects a gravitational response depends on a separately
specified source/interaction law.

The licensed conclusion is constructive and bounded:

- quadratic `I3` scaling requires an explicit cancellation mechanism on the
  tested perturbative family;
- the symmetric route supplies one such mechanism;
- a universal cross-experiment coefficient and a shared physical deformation
  remain open.

**Broad P3, Born, gravity, or no-go claim: FAIL.**  This is a law-level
comparator, not a physical-M2 compiler.  It derives no probability, occurrence,
Record, mass law, Newton coupling, or empirical bound.  There is no axiom
pressure.

Runner:

`scripts/born_gravity_p3_perturbation_tournament_cycle475_2026_07_19.py`

## The other side of the bridge

The binding Accessible Prediction note explicitly makes P3 conditional.  Its
runner computes experimental companion bounds only after supplying

```text
|I3/I1| ~ epsilon^2,
|beta-1| ~ epsilon,
C = 1.
```

The older nonlinear Born/gravity examples do not establish these statements.
They show large nonzero `I3` and a response-sign change for two finite
nonlinear propagators, but their fitted mass exponents remain approximately
one.  The note was correctly narrowed to exhibited examples.

The current physical Born campaign compiles finite exact proportional effect
relations but does not yet select a state/grade, probability law, or an
amplitude-deformation parameter.  The physical gravity/source campaign
constructs branch-controlled field/test responses but does not derive a
universal mass exponent.  Cycle 475 therefore attacks the exact algebraic
contract those shores would have to share before P3 can bridge them.

## Exact expansion

For three path amplitudes `a_0,a_1,a_2`, let

```text
A_S = sum_{i in S} a_i
```

for each nonempty subset `S`.  The Sorkin functional uses signs

```text
(+,+,+,-,-,-,+)
```

on `(A,B,C,AB,AC,BC,ABC)`.  For any supplied deformation values `f_S`,

```text
|A_S + epsilon f_S|^2
 = |A_S|^2
 + 2 epsilon Re(A_S* f_S)
 + epsilon^2 |f_S|^2.
```

Inclusion-exclusion cancels the baseline exactly and gives

```text
L_f = I3[ 2 Re(A_S* f_S) ],
Q_f = I3[ |f_S|^2 ].
```

Nothing in linear amplitude addition alone sets `L_f=0` for a nonlinear
detector/propagator deformation.  A symmetry, environment average, special
functional identity, or tuned geometry could do so, but that is additional
content to derive and test.

The frozen exact fixtures are:

```text
train = (1, (2+i)/3, (-1+2i)/4),
held  = ((3+i)/5, (-2+4i)/5, (1-2i)/3).
```

For `f(A)=|A|^2 A`, exact coefficients are:

| fixture | `L_f` | `Q_f` | `I1` | `Q_f/I1` |
|---|---:|---:|---:|---:|
| train | `-19/9` | `-7577/1728` | `389/144` | `-7577/4668` |
| held | `-752/375` | `-135556/84375` | `89/225` | `-135556/33375` |

Both first-order coefficients are exact and nonzero.  The held fixture and
all thresholds are frozen before evaluating its outputs.

## Three constructive routes

### Direct cubic route

The direct law applies `A+epsilon|A|^2A`.  Over the frozen small-`epsilon`
grid, both train and held log slopes approach one.  Thus its natural
cross-scaling against a separately linear `beta-1` would also be linear in
`I3`, not square-root.

This does not falsify P3.  It shows that P3 is not the generic Taylor order of
this common deformation class.

### Symmetric ±epsilon route

Take two equally weighted supplied sectors:

```text
P_sym(A) = ( |A+epsilon f(A)|^2 + |A-epsilon f(A)|^2 ) / 2.
```

Then

```text
I3_sym = Q_f epsilon^2
```

exactly.  This could arise from a protected `epsilon -> -epsilon` symmetry or
an open-system mixture, but Cycle 475 does not derive either.  Deleting one
companion restores a linear term, so the cancellation mechanism is visible.

If the gravity comparator `beta=1+epsilon` is supplied, each fixture satisfies

```text
|beta-1| = C_fixture sqrt(|I3/I1|),
C_fixture = 1/sqrt(|Q_f/I1|).
```

The values are approximately

```text
C_train = 0.7849044297,
C_held  = 0.4961937214.
```

At held `epsilon=10^-3`, using the train coefficient overpredicts the supplied
held `|beta-1|` by about 58%.  The exponent survives; coefficient universality
does not.

### Phase-only route

For

```text
A -> exp(i epsilon |A|^2) A,
```

the magnitude is exactly unchanged for every subset, so `I3=0` for every
`epsilon`.  This route proves only detector blindness to exact local phase.  A
wrapped phase is not energy, and a phase deformation is not a rate or gravity
response without an operational coupling.

## Deletions, permutations, and covariance scope

Deleting one of the seven inclusion terms makes baseline `I3` nonzero.
Deleting the negative companion from the symmetric route reintroduces the
linear coefficient.  These controls distinguish exact cancellation from a
small fitted residual.

All six path-label permutations preserve `L_f`, `Q_f`, `I1`, and the exact
ratios.  The scalar tournament is carried unchanged with an apparatus through
all 24 proper-cubic frames.  It does not construct a new spatial tensor or a
physical M2 gate schedule; cubic covariance is not the missing P3 content.

## Supplied, derived, and open

Supplied:

1. three-path amplitudes, quadratic detector functional, and Sorkin
   inclusion signs;
2. the cubic deformation `f(A)=|A|^2A` and finite train/held fixtures;
3. candidate gravity comparator `beta(epsilon)=1+epsilon`;
4. equal weights and opposite signs for the symmetric route;
5. `I1` normalization, perturbation domain, tolerances, and resource caps;
6. the conditional P3 exponent/coefficient when reproducing the published
   scenario table.

Derived:

1. exact `I3=L epsilon+Q epsilon^2` expansion;
2. nonzero direct-route `L` and small-parameter slope one on train/held;
3. exact symmetric cancellation and slope two;
4. exact train/held coefficients and held no-refit mismatch;
5. phase-only blindness, inclusion/companion deletions, path permutations,
   and scalar frame carry.

Open:

1. physical selection and generation of an amplitude deformation;
2. why one parameter controls both detector and gravitational source/response
   channels;
3. a symmetry or open-system law that protects `L=0`;
4. a geometry/apparatus-independent coefficient and normalization;
5. a physical M2 compiler, state/grade selection, occurrence, Records,
   probability/frequency, mass law, source normalization, and calibration;
6. an empirical Born/gravity cross-bound.

## Six-wall effect

- `C_ref`: deformation, ± sectors, detector functional, beta comparator,
  normalization, and coefficient convention remain supplied.
- `C_num`: materially clarified.  The P3 exponent and coefficient are law
  inputs unless cancellation and universality are separately derived.
- `C_wrap`: unchanged.  Phase is not energy or rate.
- `C_int`: the shared-epsilon detector/gravity coupling remains open.
- `C_local`: unchanged.  This is exact law algebra, not a physical-M2
  compiler.
- `C_source`: candidate beta response remains supplied rather than generated
  by a physical mass/source law.

## N1 — Alternative route enumeration

| Route | Status | Disposition |
|---|---|---|
| direct cubic amplitude deformation | attempted / positive nonquadratic | exact linear term survives |
| equal symmetric ±epsilon sectors | attempted / positive quadratic | exponent lands; coefficient varies |
| exact phase-only deformation | attempted / detector-blind | `I3` stays zero |
| other detector functionals/generalized measures | open | could change Taylor order |
| other shared source/propagator deformations | open | requires explicit beta response |
| symmetry-protected physical M2 compiler | open | could promote symmetric route |
| open-system/Record-conditioned law | open | requires occurrence/environment semantics |
| direct empirical two-parameter law | open | falsifiable but not derived |

The constructive symmetric route prevents a broad impossibility conclusion.
The direct and phase routes prevent quadratic scaling from being treated as
automatic.

## N2 — Wall-independence audit

Cancellation order, shared parameter selection, gravity response, coefficient
universality, physical compilation, occurrence, and empirical calibration are
separate contracts.  The direct/symmetric/phase routes are alternative
mechanisms for one cancellation obligation, not multiple constitutional
walls.

## N3 — Hidden-wall scan

The probe explicitly supplies amplitudes, `f`, detector functional, ± sector
weights, beta comparator, `I1`, finite epsilon grid, path identities,
tolerance, and coefficient convention.  It does not hide a state selector,
probability interpretation, physical deformation generator, source law,
experimental normalization, or Record.

## N4 — Residual matching

The exact witness matches P3's missing perturbative derivation: why `I3` begins
at second order while beta changes at first order.  It does not match the
finite Born-quotient residual, probability/occurrence, physical mass response,
Newton coupling, P1/P2, or empirical gravity residuals.

## N5 — Rhetoric audit

Tests cover exact three-path algebra, two frozen amplitude configurations,
three deformation families, label permutations, and scalar frame carry.  They
do not cover arbitrary interferometers, physical apparatus, source dynamics,
continuum gravity, or experimental data.  “Generic” refers only to the
nonvanishing allowed first derivative, exhibited explicitly here.

## N6 — Partial-closure path scan

The symmetric route gives the required exponent without axiom change.  It can
be promoted by physically generating the two sectors, deriving equal weights,
coupling the same parameter to an actual mass response, and finding a held-
stable normalization.  Each is a concrete constructive target.

## N7 — Steelman

Grant that P3 could be correct for a deeper symmetry-protected deformation.
Cycle 475 does not exclude it; it identifies its terminal obligations.  A
candidate that compiles `epsilon -> -epsilon`, cancels `L` for every lawful
apparatus, produces `beta-1` from the same epsilon, and predicts one held-stable
coefficient would genuinely bridge the conditional scenario.

## N8 — Cross-cycle echo and claim gate

The Accessible Prediction note already labels P3 supplied.  The older
nonlinear examples leave beta near one, while the current physical Born and
gravity campaigns close different finite mechanisms.  Cycle 475 explains why
“common linearity” alone does not fill the quantitative gap and keeps the
symmetric constructive route live.

Bounded perturbation-order and coefficient audit: **PASS** only if the frozen
executable passes.

Broad P3, Born, gravity, or no-go claim: **FAIL**.

No minimum-content theorem, shared-substrate obstruction, or axiom-pressure
claim follows.  There is **no axiom pressure**.

## Interpretation firewall

- `I3` here is an algebraic detector functional, not a derived probability or
  frequency.
- `beta` is a supplied comparator, not a measured or physically derived mass
  law.
- Equal ± sectors are supplied, not occurrence weights.
- A phase is not energy; epsilon is not a rate or time.
- A law-level comparator is not a physical-M2 compiler.
- No conditional scenario is promoted to a framework prediction.

## Frozen execution

The final cold execution reports `RESULT pass=11 fail=0`.

The direct-route log slopes on the frozen `epsilon=10^-6..10^-2` grid are
`1.001542341905022` on train and `1.0005980570805808` on held.  The symmetric
route slopes are `2.0000000000000004` and `2.0`.  The exact coefficients give
`C_train=0.7849044296638619` and `C_held=0.4961937213966059`.  At held
`epsilon=0.001`, `|I3/I1|=4.061602996254682e-06`; the train coefficient
predicts `|beta-1|=0.0015818507889512178` instead of the supplied `0.001`, a
relative no-refit miss of `0.5818507889512179`.

All twelve fixture/path-permutation comparisons and all 24 scalar frame
carriages pass.  Deleting the train `AB` baseline term produces exact
`I3=26/9`; deleting one symmetric companion restores the exact linear term in
`epsilon*(-7577*epsilon-3648)/3456`.  Three malformed domains are refused.
The runner takes `0.9285928750177845` seconds including imports and peaks at
`77,168,640` bytes, below the frozen 60-second and 1-GiB caps.
