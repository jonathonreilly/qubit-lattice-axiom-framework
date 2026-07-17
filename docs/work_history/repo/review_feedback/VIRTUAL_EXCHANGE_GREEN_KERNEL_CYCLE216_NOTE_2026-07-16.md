# Virtual-exchange Green kernel — Cycle 216

**Date:** 2026-07-16

**Authority:** none

**Status:** conditional exact static-exchange bridge

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py
```

## Question

Cycle 215 proved that one six-state local unitary contains the complete
source-free scalar wave, but its tested one-field injection port did not equal
the direct point source used in Cycle 213.  Is a persistent classical field
expectation actually required for two bodies to feel the Green interaction?

Or can the same finite carrier supply it through static virtual exchange?

## Candidate local stiffness

Let `U` be the Cycle-214/215 proper-cubic coin-plus-stream field walk.  Form

```text
K=2I-U-U^dagger.
```

`K` is Hermitian, positive semidefinite, translation invariant, proper-cubic,
and radius one because both `U` and `U^dagger` move by one edge.  Use it in the
local quadratic action

```text
S[Psi,J] = (1/2) <Psi,K Psi> - g Re<J,Psi>.
```

A Cycle-210 object couples locally through

```text
J(x) = Q delta_x |scalar>,
```

where `Q` is the representation-safe vacuum-relative mass scalar from Cycle
213.  Eliminating `Psi` gives the static pair term

```text
S_eff[J] = -(g^2/2) <J,K^+ J>.
```

The quadratic-action and effective-action interpretation remains supplied
candidate physics.  The inverse is a theorem about the response of the local
operator; it is not inserted into the microscopic update.

## Exact identity

For every nonzero lattice momentum,

```text
<scalar|K(k)^+|scalar> = 3/L(k).
```

Thus the scalar-source block of the finite-coin stiffness inverse is exactly
`3 L^+`, with no long-wavelength approximation.  Cycle 215's four flat modes
are zero modes of `K`, but the scalar source is exactly orthogonal to them.
Only the ordinary constant acoustic mode remains; on the finite torus the
same uniform background subtraction used in Cycles 211 and 213 removes it.
In plain text: the scalar block is exactly 3 L^+.

The runner checks the identity over 64 held-out momenta, solves the complete
coin-valued position-space equation, and verifies

```text
K Psi = rho |scalar>,
<scalar|Psi> = 3 L^+ rho.
```

The on-shell positive stiffness equals the scalar source pairing.

## Result up front

The static virtual-exchange route succeeds conditionally.

- `K` is positive semidefinite, radius one, and transforms in all 24
  proper-cubic frames.
- The coin-valued field sourced at one site solves its local equation, and its
  scalar projection equals exactly three copies of the Cycle-211 Green field.
- On a side-41 torus, axial radii `4..12` fit `a+b/r` with `R^2>0.9994`; the
  fitted `b` is within one percent of `3/(4 pi)`.
- Two local positive charges have a symmetric negative pair potential and
  equal-and-opposite stationary forces.
- Coupling that force into the actual Cycle-210 molecular walk gives the same
  acceleration for all three tuned species within the existing finite packet
  error.  The molecular scalar band remains above `0.999`.
- Source composition is additive.  Coupling deletion removes acceleration,
  and one or two spectator records do not multiply the source.
- Moving within the same unitary cubic matter family while detuning rest
  charge from curvature inertia breaks the universal response.

## Bare-metal reading

The conditional common-law chain is now

```text
one proper-cubic finite coin U
  -> exact causal scalar wave                  [Cycle 215]
  -> local positive stiffness K=2I-U-U^dagger
  -> exact static scalar exchange 3 L^+
  -> -Q_source Q_test/r pair potential
  -> species-independent molecular response   [when Q=m_inertial].
```

This route does not need an external source time series or a macroscopic
classical one-point field.  The body appears as a local interaction vertex in
the static action, and the nonlocal-looking Green response is derived by
eliminating the local carrier.

## Conditions and remaining work

The following remain supplied:

- the six-state field coin and coin-then-stream dynamics;
- the Hermitian stiffness choice `K=2I-U-U^dagger`;
- the local quadratic action and the rule that its stationary elimination is
  the physical static exchange observable;
- the scalar source vertex, vacuum reference/phase branch, coupling magnitude,
  and attractive action sign;
- the uniform background subtraction on the finite periodic comparator; and
- the tuned equality of rest charge and inertial mass.

The construction is static.  It does not yet join the Cycle-214 real emission
sector to this virtual kernel, derive radiation reaction, establish a positive
local combined matter-field Hamiltonian, or show how a moving quantum source
selects retarded rather than advanced response.  It has no tensor geometry,
nonlinear self-coupling, stress-energy source, gravitational field energy,
continuum theorem, Lorentz theorem, or empirical prediction.  This is not
general relativity.

It also does not derive a clock rate, occurrence, record formation, Born
frequencies, or an axiom update.  There is no axiom conclusion.

## Attribution and scope

Resolvents, quadratic-field elimination, and virtual exchange are standard
mathematical-physics structures.  No novelty is claimed for those tools.  The
bounded exact composition with the internal cubic carrier is the result being
parked; global novelty has not been established.

The one-dimensional Thirring-QCA molecule used in Cycles 205–209 is published
prior work of Bisio, D'Ariano, Mosco, Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

The Thirring-QCA is not the cubic exchange carrier used here.

This work remains on the draft parking branch and changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py
```
