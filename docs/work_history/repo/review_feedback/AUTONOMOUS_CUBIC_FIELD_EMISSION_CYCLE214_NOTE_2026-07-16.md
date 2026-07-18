# Autonomous cubic field emission — Cycle 214

**Date:** 2026-07-16

**Authority:** none

**Status:** conditional autonomous finite-alphabet matter/field exchange

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py
```

## Question

Cycle 213 supplied a reversible retarded field, but still imposed an external
source history and used two unbounded real values at each site.  Can one local
unitary instead make the Cycle-210 object coherently create, propagate, and
reabsorb a finite-alphabet field carrier without being told when to source it?

## Candidate process

Use the direct sum of two sectors:

```text
bound object + field vacuum
bound object + one six-direction field carrier.
```

The body is always the exact Cycle-210 bound-object carrier.  The second
sector adds one hard-core field excitation.  At every body site, the same
onsite vertex rotates between the no-field scalar object and the scalar
object times scalar field state:

```text
|object, vacuum>_scalar
  <->
|object, one field>_(scalar x scalar).
```

The angle is `g Q`, where `Q` is Cycle 213's vacuum-relative mass scalar.
After the vertex, the body and field each stream at most one cubic edge.  No
site address, time counter, outcome label, or protocol-specific source table
appears in the law.

The field coin is

```text
C_field = P_scalar + P_vector - P_even.
```

It is a six-state proper-cubic unitary.  Its scalar/longitudinal pair has
linear small-momentum phases with isotropic slope `1/sqrt(3)`; the remaining
transverse/zone-edge sectors are retained rather than silently discarded.
It is the bounded acoustic field carrier tested here.

## Result up front

The autonomous finite-alphabet exchange probe succeeds in its bounded
zero/one-field sector.

- The field coin is exactly unitary, commutes with all 24 proper-cubic frames,
  and has the same acoustic slope along axial, face-diagonal, body-diagonal,
  and held-out directions.
- A literal full-position implementation preserves norm and commutes with a
  simultaneous translation of body and field.
- The efficient relative-coordinate runner is exactly both the zero-momentum
  and a held-out nonzero fixed-total-momentum block of that literal local law;
  the reduction is not a hidden nonlocal interaction.
- Starting with the object and field vacuum, the same onsite vertex produces
  one-field probability `sin^2(g Q)` on the first tick and continues to emit,
  propagate, and reabsorb coherently with no external source history.
- Reversing seven ticks restores the exact object-plus-vacuum state.  Deleting
  the vertex leaves the field vacuum exact.  A longer finite-volume forward
  history also shows field amplitude returning to the source channel; this is
  a recurrence/reabsorption control, not an infinite-volume decay theorem.
- Relative separation grows by at most two edges per tick because body and
  field each stream one edge.  The complete invariant history is unchanged
  under all 24 cubic frames.
- Fixed-total-momentum blocks remain normalized.  In every populated relative
  Fourier cell, body recoil plus field momentum equals that fixed total
  momentum by construction of the translation sector.
- A `2 pi` phase lift and representation changes were already closed in Cycle
  213.  One or two normalized spectator records do not change `Q` or the
  emission angle.
- Moving within the same local unitary cubic body family while detuning rest
  charge from curvature inertia changes source strength per unit inertia.
  Cubic symmetry does not force the desired alignment.

The important gain is narrow but real: source activation is now state-driven,
not an imposed time series, and the carrier uses a finite local occupancy and
six-direction coin rather than a classical real field register.

## Bare-metal reading

The conditional chain is now

```text
local contact law
  -> persistent proper-cubic object
  -> vacuum-relative mass scalar Q
  -> identical onsite number-changing vertex at every site
  -> coherent field creation / reabsorption
  -> one-edge body and field transport
  -> exact translation-sector recoil accounting.
```

Records are spectators.  They can later archive a detector result, but they
neither constitute the object nor multiply its source.

## Conditions and remaining gap

The following are supplied candidate physics:

- the zero/one-field sector and its hard-core occupancy interpretation;
- the six-direction acoustic field coin;
- the scalar-to-scalar onsite vertex and its ordering within a tick;
- the vacuum-relative charge map, principal phase branch, and coupling `g`;
- the restriction to at most one field excitation; and
- the identification of the field excitation as the carrier relevant to the
  gravity-shaped lane.

The construction conserves quantum norm and fixed lattice quasimomentum.  It
does not yet establish a positive local energy shared by body and field.
Floquet quasiphase is not silently renamed energy.

Most importantly, the static Green sector remains open.  The runner has not
shown that virtual or repeated carriers dress the body into the Cycle-213
`1/r`-shaped time-averaged field, nor that a second body acquires the universal
weak response.  A many-field/Fock completion, self-energy renormalization,
vacuum stability, emission threshold, field statistics, and continuum limit
are all absent.  The current one-field sector can model coherent emission and
absorption, not a macroscopic field.

There is no tensor geometry, nonlinear backreaction, stress-energy source,
Lorentz-covariant theorem, general relativity, empirical prediction, clock
rate, occurrence law, record formation, or Born-frequency derivation.  There
is no axiom conclusion.

## Attribution and scope

Number-changing quantum-walk and quantum-optical emission constructions are
broad prior-art classes; the present bounded composition makes no global
novelty claim.  Global novelty has not been established.

This work remains on the draft parking branch.  It changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py
```
