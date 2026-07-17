# Finite-coin scalar-wave dilation — Cycle 215

**Date:** 2026-07-16

**Authority:** none

**Status:** positive conditional exact-dilation theorem

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py
```

## Question

Cycle 213 used two real numbers at every site to carry a reversible scalar
wave.  Cycle 214 independently introduced a six-direction unitary acoustic
carrier so an object could source a finite local field excitation.

Are those genuinely two different field laws, or is the Cycle-214 carrier an
exact finite-coin unitary dilation of the Cycle-213 scalar process?

## Result up front

They are the same source-free scalar law on the tested candidate surface.

For the onsite field coin

```text
C = P_scalar + P_vector - P_even
  = (1/3) J - R,
```

followed by one-edge directional streaming, define

```text
phi_n(x) = <scalar | Psi_n(x)>.
```

Then every complex field state, not merely a prepared scalar state, obeys

```text
phi_(n+1) - 2 phi_n + phi_(n-1) = -(1/3) L phi_n.
```

This is Cycle 213 exactly at `dt^2=1/3`.  The six-state carrier therefore gives
an exact finite-coin unitary dilation of the scalar wave rather than an
approximation or a second postulate.

## Exact algebra

For momentum phases `(x,x^-1,y,y^-1,z,z^-1)`, let

```text
gamma = (x+x^-1+y+y^-1+z+z^-1)/6.
```

The runner proves symbolically

```text
<s| [U^2 - 2 gamma U + I] = 0
```

and

```text
det(lambda I-U)
  = (lambda^2-2 gamma lambda+1)
    (lambda-1)^2 (lambda+1)^2.
```

Thus there are exactly two acoustic modes and four scalar-invisible flat
modes.  The acoustic relation is

```text
cos(omega) = gamma = 1-L(k)/6,
```

which gives the displayed real-space recurrence and small-momentum speed
`1/sqrt(3)`.

Inside the normalized proper-cubic family

```text
C(a) = P_scalar + P_vector + a P_even,     |a|=1,
```

the symbolic greatest common divisor of all scalar-wave residual components
is `a+1`.  Therefore this exact wave identity selects `a=-1` within that
family.  This is not a uniqueness theorem over all QCAs, larger coins, block
updates, or alternative representations.

## Constructive controls

- Twelve literal ticks from an arbitrary complex internal field state obey
  the scalar recurrence to machine precision while the parent norm remains
  one.
- The parent commutes with translations and all 24 proper-cubic frames and
  has an exact one-edge causal cone.
- The six-state coin embeds as a block in three qubits.  Its computational
  columns have unequal nonzero magnitudes `1/3` and `2/3`, so the embedding is
  not a Clifford unitary.
- Held-out momenta have the exact two-acoustic/four-flat spectrum, and the
  scalar row has zero overlap with all four flat modes.
- Changing the even-sector phase inside the same cubic unitary family breaks
  the scalar-wave recurrence.
- With the direct zero-mean source used in Cycles 211 and 213, the wave law at
  the selected coefficient still time-averages to the same static Green
  sector.

## Exact source-port identity

If a local scalar amplitude `j_n(x)` is added after the coin and before the
one-edge stream, the projected field obeys

```text
phi_(n+1) - 2 Gamma phi_n + phi_(n-1)
  = Gamma j_n - j_(n-1),
```

where `Gamma` is the six-neighbour average.  This identity is verified for a
random complex source history.  It makes the source residual precise: this
specific constant one-field source port supplies

```text
(Gamma-I)j = -L j/6,
```

not the direct point `rho` used by the classical forced wave equation.

That is a property of this port and sector, not a no-go against autonomous
gravity or quantum fields.  A conjugate source register, multi-field coherent
state, local reservoir, different injection ordering, or exchange-observable
route may change the forced term.  The required N1-N8 exercise therefore
fails the broader no-go and queues those routes rather than declaring them
closed.

## Bare-metal reading

The strongest current conditional chain is

```text
six-state onsite coin + one-edge stream
  -> exact unitary local process
  -> exact scalar wave projection
  -> exact causal and proper-cubic field propagation
  -> same time-averaged static Green sector when directly driven.
```

This removes the continuous two-slice wave rule as independent law content:
on this candidate surface, it is a projected theorem of the finite coin.
The coin and stream are still supplied candidate dynamics, and the direct
static source port is not yet autonomously generated.

## Conditions and scope

The result consumes:

- the six-direction field alphabet and the displayed coin;
- a synchronous coin-then-stream tick;
- the scalar projection as the field observable; and
- for the Green comparison only, a supplied zero-mean direct source.

It does not derive the coin from the four axioms, select this family over all
local laws, quantize a many-field sector, supply a persistent autonomous point
source, prove universal second-body response, or establish positive local
matter-plus-field energy.  It is not general relativity, a continuum theorem,
an empirical prediction, a record/Born/clock result, or an axiom proposal.
There is no axiom conclusion.

## Attribution

Coined quantum walks and unitary dilations are broad prior-art classes.  The
factorization and bounded composition here are derived directly, but global
novelty has not been established.

The one-dimensional Thirring-QCA molecule used in Cycles 205–209 is published
prior work of Bisio, D'Ariano, Mosco, Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

The Thirring-QCA is not the cubic field carrier used here.

This work remains on the draft parking branch and changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py
```
