# Minimal exchange-action selection — Cycle 217

**Date:** 2026-07-16

**Authority:** none

**Status:** conditional minimal-functional-calculus selection theorem

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/minimal_exchange_action_selection_cycle217_2026_07_16.py
```

## Question

Cycle 216 obtained the exact static Green interaction by choosing

```text
K=2I-U-U^dagger.
```

Was that merely a convenient Hermitianization, or is it selected by the
smallest stable static action that can be built directly from the already
chosen one-tick field unitary `U`?

## Scoped selection result

Consider the most general degree-one Hermitian Laurent polynomial

```text
K = a I + b U + b* U^dagger,
```

with `a` real.  Ask for:

1. a stationary null mode, `K(1)=0`; and
2. positivity on both sides of that mode for every unit-circle eigenphase.

Write `b=u+iv`.  The null condition gives `a=-2u`.  Around phase zero,

```text
K'(0)=-2v,
K''(0)=-2u.
```

Two-sided positivity forces `v=0` and `u<0`.  Therefore

```text
K = kappa (2I-U-U^dagger),     kappa>0.
```

It is unique up to positive scale inside this degree-one Hermitian Laurent
family.  That scale is absorbed into `g^2/kappa`, leaving one physical
coupling magnitude.

This is not uniqueness over all local actions, degree-two polynomials, larger
blocks, nonlinear field laws, alternate QCAs, or continuum theories.

## Source-vector selection

The six directions form one transitive proper-cubic orbit.  The runner stacks
`R-I` for all 24 frame permutations and finds rank five: the invariant
subspace is one-dimensional.  Its normalized vector is

```text
|scalar> = (1,1,1,1,1,1)/sqrt(6).
```

Thus a local proper-cubic scalar source is unique up to its coefficient.
Group-averaging an arbitrary six-component source deletes every other part.
The coefficient used for matter is the vacuum-relative mass scalar `Q` from
Cycle 213.
Equivalently, this is the unique proper-cubic scalar source direction.

## Attraction and one coupling

For the stable local quadratic action

```text
S = (kappa/2) <Psi,K_0 Psi> - g Re<J,Psi>,
```

stationary elimination gives

```text
S_eff = -(g^2/(2 kappa)) <J,K_0^+ J>.
```

Because the Green kernel is positive near a positive source, like scalar
charges have a negative cross action: the attractive sign follows from stable
quadratic elimination rather than a second sign choice.  The same vertex
coefficient appears once as source and once as response, so there is one
source/response coupling rather than two independently fitted constants.

The runner sends that force through the actual Cycle-210 molecular walk.  All
three tuned species again have the same acceleration within finite packet
error, and the force transforms through all 24 proper-cubic frames.

## What this retires

Conditional on using the already selected field walk and its minimal
degree-one static functional calculus, Cycle 217 retires three apparent free
choices from Cycle 216:

- the form of `K` is fixed up to scale;
- the local scalar source direction is unique; and
- the attractive sign plus equal source/response coupling follow from one
  positive quadratic action.

The positive scale is not a new physical dial separate from coupling because
only `g^2/kappa` enters the exchange strength.

## What remains supplied

The construction still consumes:

- the finite field walk `U` and the choice to use its minimal degree-one
  stationary quadratic functional calculus;
- the physical identification of the stationary action with virtual exchange;
- the matter charge coefficient `Q`, its vacuum reference and branch;
- the magnitude of `g^2/kappa`; and
- most importantly, the tuned equality `Q=m_inertial` in the Cycle-210 matter
  family.

Dropping the stationary null condition permits an independent positive
`mu^2 I` term and screens the field.  Higher-degree positive functions of `U`
also exist and are outside this selection surface.  No global law uniqueness
is claimed.

There is still no tensor geometry, nonlinear field self-coupling,
stress-energy source, dynamical retarded/advanced selection, radiation
reaction, continuum/Lorentz theorem, empirical prediction, clock-rate law,
record formation, occurrence, or Born-frequency derivation.  There is no
axiom conclusion.

## Attribution and scope

Positive quadratic elimination and Laurent functional calculus are standard
tools.  No global novelty is claimed.  The result is the bounded selection and
composition on this internal candidate surface; global novelty has not been
established.

The one-dimensional Thirring-QCA molecule used in Cycles 205–209 is published
prior work of Bisio, D'Ariano, Mosco, Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

The Thirring-QCA is not the proper-cubic field/action mechanism selected here.

This work remains on the draft parking branch and changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/minimal_exchange_action_selection_cycle217_2026_07_16.py
```
