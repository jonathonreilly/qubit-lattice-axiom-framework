# Common matter/field coin family — Cycle 219

**Date:** 2026-07-16

**Authority:** none

**Status:** conditional one-parameter common-law family

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/common_matter_field_coin_family_cycle219_2026_07_16.py
```

## Question

Cycle 218 put matter and field on one common acoustic cone, but retained the
Cycle-210 `det C=1` condition.  That condition made the even-sector phase
`O(beta^3)` and squeezed the clean mass tangent into a narrow momentum window.

Can field and matter instead be two members of one proper-cubic coin family,
with the exact field coin as the massless endpoint and a robust internal gap
for massive matter?

## Candidate common family

Use

```text
C(beta)
  = exp[-i tan(beta/2)]
    [P_scalar - P_even + exp(i beta) P_vector].
```

The same even-sector phase `-1` is used at every beta.  The scalar phase is the
common-cone rest energy

```text
E_rest = -tan(beta/2) = m/3,
```

and the vector phase controls curvature

```text
m = -3 tan(beta/2).
```

At `beta=0`, rest energy and mass vanish and `C(0)` is exactly the Cycle-214
field coin selected by the Cycle-215 scalar-wave theorem.  Negative beta gives
the effective Cycle-210 bound object a positive mass.

## Result up front

The one proper-cubic coin family succeeds conditionally.

- `beta=0` is exactly the massless endpoint with acoustic speed
  `c^2=1/3`.
- For beta `-0.2,-0.3,-0.4` and held-out `-0.35`, rest mass
  `E_rest/c^2` equals the independent curvature mass.
- Every family member is unitary and commutes with all 24 cubic frames.  The
  existing contact correction keeps the two-carrier object exactly bound.
- The shared even phase is antipodal to the scalar phase at the massless
  endpoint and remains a robust internal gap, removing Cycle 218's accidental
  near-degeneracy.
- Broad finite packets recover forced inertia within 0.7%, stay in the scalar
  band, and respond universally to the Cycle-216 static exchange kernel.
- Two-object composition and record-redundancy controls pass.

In short, rest/dispersion/inertial/exchange mass agrees within the stated
finite-packet tolerance.

The conditional chain is now unusually compact:

```text
one coin family C(beta)
  beta=0       -> causal acoustic field
  beta<0       -> persistent massive object
  same cone    -> E_rest=m c^2
  same scalar  -> virtual exchange source/response.
```

## Why `det C=1` is not retained

The determinant-one condition was a Cycle-210 parameter constraint, not a
consequence of locality, unitarity, cubic covariance, or the current axioms.
On the common-cone family it forces the even phase close to the scalar phase
and narrows the usable band.  Cycle 219 drops it rather than treating a
convenient matrix subgroup as physics.

The runner verifies that the resulting determinant phases are nonzero at each
tested beta, although their departure begins only at higher order in beta.
In plain text: det C=1 is not retained exactly.  This is not a proof that
Nature rejects `SU(6)`; it is an explicit
candidate comparison showing that `det C=1` is not needed for the present
field, mass, binding, or exchange bridges.

## Central remaining caveat

A one-parameter family is not one generated spectrum.  The three beta values
tested here are three distinct coins.  Unless beta becomes a conserved local
state, a bound-state eigenvalue, or a spectrum derived from one fixed
interaction, choosing beta separately for each species would be a hidden law
table.

Therefore beta selection remains open.  Cycle 219 establishes a common
functional architecture and a massless-to-massive continuation; it does not
yet provide one microscopic law in which several particle masses coexist or
derive the observed spectrum.

## Conditions and scope

The following remain supplied:

- the common coin family itself and coin-then-stream order;
- the common acoustic cone condition;
- the beta value for a candidate object;
- the contact binding architecture;
- the vacuum-relative rest-energy reading;
- the virtual-exchange action and overall coupling; and
- the interpretation of different beta sectors as field/matter content.

The common-cone relation is not forced by the coin architecture: shifting the
global scalar phase preserves locality, unitarity, and cubic covariance while
breaking rest/inertia alignment.  The runner includes that control.

There is no generated beta spectrum, statistics/chirality/gauge content,
fermionic many-body law, tensor/nonlinear gravity, radiation, continuum
theorem, empirical prediction, clock-rate theorem, occurrence, record
formation, or Born-frequency derivation.  There is no axiom conclusion.

## Attribution and scope

Proper-cubic coined walks and massive-to-massless quantum-walk families have
broad prior art.  No global novelty is claimed; global novelty has not been
established.

This work remains on the draft parking branch and changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/common_matter_field_coin_family_cycle219_2026_07_16.py
```
