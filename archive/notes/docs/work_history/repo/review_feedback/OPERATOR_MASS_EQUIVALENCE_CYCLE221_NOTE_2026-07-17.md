# Operator mass consistency across supplied kernels — Cycle 221

**Date:** 2026-07-17

**Authority:** none

**Status:** conditional effective-kernel consistency probe; audit unset

**Constitutional effect:** none

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/operator_mass_equivalence_cycle221_2026_07_17.py
```

## Result up front

One supplied operator is reused across several separately supplied effective
kernels.  On the three positive phase-register sectors whose rest phase is
unaliased, its eigenvalue agrees with designed rest mass, low-momentum
dispersion mass, and independently measured fixed-force inertia.  Supplying
the same operator as charge then gives conditional common acceleration in an
external gradient and in a finite-coin scalar Green field.  A direct
`M tensor M` vertex is Hermitian, reciprocal, attractive at the tested
separation, and entangles coherent source sectors.

That is a useful rest/dispersion/fixed-force inertia consistency bridge.  It
is not one autonomous common law.  The contact, force, source, composition,
and exchange rules are distinct candidate inputs, and several equalities are
true because `M` was deliberately placed in those inputs.

The decisive binding ablation is negative for the stronger interpretation:
**equal-direction kinematics binds**.  Replacing the contact coin by the
identity, deleting its rest phase, or replacing the phase register by the
identity leaves the prepared equal-direction object exactly coincident for
eight tested ticks.  Deleting the entire contact replacement releases it.
Thus the shared contact-sector geometry supplies persistence; `M` controls
phase and response inside that sector but does not cause its binding.

There is no beta lookup during the tested update.  Spectral host preparation
and later sector analysis do use the eigenvectors of the supplied register.

## Candidate objects and separately supplied effective kernels

The common onsite data are

```text
S                             fixed nine-state cyclic phase register
M = 3 i (S-I)(S+I)^-1         supplied Cayley mass operator
C(S)                          supplied register/direction coin
```

The runner then tests `M` in four different fixtures:

```text
contact       shared-register replacement on equal-direction coincidence;
fixed force   exp(+i strength x Q), first with Q=I and then with Q=M;
field probe   the same coordinate kick driven by a Cycle-216 scalar gradient;
exchange      -g0^2 K(r) M_source tensor M_probe at one fixed separation.
```

These formulas have no branch-specific beta table.  They are nevertheless
separately supplied effective kernels, not consequences of one generated
microscopic update.

## What is independently measured

The nine-cycle has four positive eigenvalues of `M`:

| sector | `M` eigenvalue | principal rest-phase mass | dispersion mass |
|---:|---:|---:|---:|
| 1 | 1.09191070 | 1.09191070 | 1.09191073 |
| 2 | 2.51729889 | 2.51729889 | 2.51729872 |
| 3 | 5.19615242 | 5.19615242 | 5.19615474 |
| 4 | 17.01384546 | -1.83571046 | not used in the packet test |

The rest and dispersion formulas are designed parts of `C(S)`.  They are
internal algebraic consistency checks, not independent discoveries of `M`.
The fourth row exposes a principal-phase alias: adding one supplied `2 pi`
lift recovers `17.01384546`, but the update itself does not choose that lift.
The clock/phase branch is therefore open.

The independent operational measurement is the response to one fixed
identity charge `Q=I`.  The three unaliased sectors return inertial masses

```text
1.09114039, 2.51694355, 5.19583841,
```

within 1.2 percent of the three `M` eigenvalues.  Norm, sector weight,
positive packet probabilities, and boundary leakage controls pass.  This is
a finite-packet numerical test, not an exact continuum theorem.

## Conditional universal response

Replacing identity charge by the supplied choice `Q=M` gives the same signed
acceleration across all three tested sectors to the packet tolerance.
Reversing the gradient reverses the acceleration.  Pre-, post-, and symmetric
kick schedules agree at the one tested weak strength; a full weak-field limit
has not been proved.

The charge-family ablation compares

```text
Q in {I, M, 2M, M+I, M^2}.
```

Across the three sectors, common acceleration occurs exactly for the tested
choices proportional to `M`.  `I`, `M+I`, and `M^2` fail that equality.  This
selects `Q proportional to M` within the finite family, while leaving its
overall normalization supplied.  Consequently the result is **conditional
common acceleration**, not a derivation of the equivalence principle.

## Binding boundary

The contact compiler owns one shared register and replaces the independent
two-carrier coin only on coincidence.  The six equal-direction states stream
both carriers over the same edge, so their relative coordinate cannot open.
The runner verifies:

- exact unitarity of the abstract contact block;
- covariance under all 24 proper-cubic frames;
- passive register-basis invariance;
- conservation of two coherent phase-sector weights;
- exact contact persistence under the full `C(S)` block;
- the same persistence with `C=I`, with the rest factor deleted, and with
  `S=I`; and
- release when the complete contact replacement is deleted.

The result is therefore a supplied invariant sector, not a dynamically
generated molecular bound state and not a protective-gap theorem.  The
abstract shared register is also not a strict nearest-neighbour one-qubit
encoding.

## Static field and exchange boundary

The response fixture reuses the finite-coin local field of Cycle 216, but the
source is reduced on the host to one selected `M` eigenvalue before the scalar
gradient is applied.  It does not implement a coherent operator-valued local
source coupled to a field carrier.

Separately, the direct vertex

```text
-g0^2 K(r) M_source tensor M_probe
```

is Hermitian and swap symmetric.  At separation `(4,0,0)` on the finite
zero-mean torus, its sector expectation equals the scalar pair potential and
is attractive.  At one fixed exposure of 2048 ticks it gives a coherent
two-sector source pair a nonzero second Schmidt coefficient.  This exposure
is fixed rather than tuned to a mass gap, but the direct vertex is still an
inserted effective action; it is not generated by the Cycle-216 local field
dynamics.  No inverse-distance continuum theorem, radiation theorem,
nonlinear field equation, or tensor geometry follows.

## Composition and records

The supplied additive composition

```text
M_total = M tensor I + I tensor M
```

makes the two-object rest unitary factorize.  This verifies the chosen tensor
composition; it does not derive additivity, and it excludes binding and field
energy.

The record control implements an actual unitary orthogonal write followed by
a unitary copy.  One record has probabilities `(1/2,1/2)` and two records have
only correlated `00` and `11` alternatives, each with probability `1/2`.
The declared matter source operator is `M tensor I_records`, so zero, one, and
two orthogonal redundant records all retain source expectation
`1.804604798...`.

This establishes redundancy invariance conditional on a matter-only source
map.  It does not model the energy or source charge of physical record
deposition, and it does not derive a record-formation process.

## Qualification and quantum scope

This candidate propagates coherent phase-register amplitudes between sparse
records.  Whether they are law-derived process variables compatible with
record-state Qualification or additional physical state requiring a widened
candidate ontology remains unresolved; no physical record-writing map is
implemented.

The abstract coin has eigenphases outside the `pi/4` grid.  Without an exact
qubit encoding and a specified logical Clifford group, that does not establish
non-Clifford qubit dynamics.  It only rules out one coarse eigenphase-grid
description of the abstract nine-state coin.

## Complete supplied-content ledger

The following remain inputs rather than derived outcomes:

- the existence and nine-state dimension of `S`;
- the Cayley map from `S` to `M` and the `1/3` common-cone rest map;
- the formula `C(S)` and its proper-cubic direction representation;
- spectral host preparation of the tested packets;
- the shared contact register, contact trigger, free/contact split, and the
  absence of a shared-to-product transition;
- the external coordinate kick, the choice `Q=M`, and its overall scale;
- additive tensor composition and phase unwrapping;
- the finite scalar field, attractive sign, coupling, background removal,
  boundary convention, host-extracted source eigenvalue, and direct
  `M tensor M` vertex;
- the coherent-register candidate ontology and its initial population;
- the nine-state block or strict one-qubit nearest-neighbour encoding;
- record deposition energy and record source charge; and
- observed species, statistics, chirality, gauge charges, abundance, mass
  ratios, preparation, occurrence, and Born frequencies.

Register population remains supplied.  Every tested kernel conserves the
register sectors rather than generating or selecting them.  This is not a
selected particle spectrum, not a gravity theory, and not an empirical mass
prediction.  There is no axiom conclusion.

## Attribution and novelty boundary

Interacting-walk bound molecules have broader prior art, including Ahlbrecht,
Alberti, Meschede, Scholz, Werner, and Werner:

<https://arxiv.org/abs/1105.1051>

Apadula, Bisio, D'Ariano, and Perinotti already introduced a Dirac quantum
walk in which mass is an extra degree of freedom spanning all mass values:

<https://arxiv.org/abs/1806.03940>

Zych and Brukner formulate the quantum equivalence principle through equality
of rest, inertial, and gravitational internal-energy operators:

<https://arxiv.org/abs/1502.00971>

Therefore dynamical mass operators, mass as an internal walk degree of
freedom, operator equivalence conditions, and interacting-walk molecules are
not claimed as new.  The bounded repo-local result is the integration and
operational testing of this particular nine-state Cayley register, supplied
proper-cubic contact compiler, and supplied scalar Green vertex in the three
unaliased positive sectors.  Global novelty has not been established.

This work stays only on the draft parking branch and draft PR #5389.  It
changes no foundation, axiom, primitive, registry, policy, queue, or audit
surface.

## Verification

```text
python3 scripts/operator_mass_equivalence_cycle221_2026_07_17.py
```
