# Generated beta phase register — Cycle 220

**Date:** 2026-07-16

**Authority:** none

**Status:** conditional one-law phase-sector construction

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/generated_beta_phase_register_cycle220_2026_07_16.py
```

## Question

Cycle 219 found one formula `C(beta)` joining massless field and massive
matter, but each beta was still a different coin.  Can beta become a conserved
state label of one fixed local law, so several mass sectors coexist without a
per-species lookup?

## One fixed phase-register law

Let `S` be one fixed odd-dimensional onsite unitary.  Define the Cayley mass
operator

```text
M = 3 i (S-I)(S+I)^-1.
```

If

```text
S |beta> = exp(i beta) |beta>,
```

then

```text
M |beta> = -3 tan(beta/2) |beta>.
```

Use the one register-direction coin

```text
C(S)
 = exp(i M/3) tensor (P_scalar-P_even)
 + exp(i M/3) S tensor P_vector.
```

In every beta eigensector this reduces exactly to the Cycle-219 coin.  The
formula contains no branch-specific table.

The runner uses the simple nine-state cyclic permutation as an illustrative
`S`.  Nine is odd, so `-1` is absent and the Cayley transform is finite.  This
choice is a structural witness, not a fit to observed masses.

## Result up front

The one fixed local phase-register law succeeds conditionally.

- `S` and `C(S)` are unitary; `M` is Hermitian and commutes with both.
- Beta becomes a conserved state label.  Every eigenstate realizes exactly
  the analytic Cycle-219 coin and mass `-3 tan(beta/2)`.
- The beta-zero eigenstate is the massless field sector.  The same fixed coin
  contains four distinct positive massive object sectors and their conjugate
  signed partners.
- The complete coin commutes with all 24 proper-cubic frame operations.
- Arbitrary changes of phase-register basis transform `S`, `M`, and `C(S)`
  together and leave the physics representation invariant.
- Two massive sectors coexist in coherent superposition for 37 ticks without
  mixing or switching laws.  The mass operator supplies the exchange charge
  in each sector.
- A register-controlled contact coin acts on the equal-direction contact
  sector.  Binding consumes the mass operator through the common coin rather
  than consulting a selected beta number.  This test preserves norm and
  contact-sector support; the dynamical binding theorem remains inherited
  from the Cycle-210 construction rather than being re-proved here.
- Spectator records do not duplicate mass or source charge.

Thus beta is no longer necessarily a law knob: it can be a conserved quantum
number of one law.

## Bare-metal reading

The current candidate hierarchy is

```text
one local register S
  -> one Hermitian mass operator M(S)
  -> one direction/register coin C(S)
  -> beta=0 massless field sector
  -> beta<0 positive massive object sectors
  -> one operator-valued binding and exchange interface.
```

No per-species lookup appears in propagation, binding, or charge extraction.
The spectrum is the spectrum of one local operator.

## What remains supplied

Register selection remains supplied.  Specifically:

- the existence, dimension, and exact unitary `S`;
- the choice of the Cayley functional relation;
- which signed beta sectors are physical particles, antiparticles, or absent;
- the initial/boundary population of those sectors;
- the four-qubit block encoding of the illustrative nine-state register; and
- interactions that can change or combine beta rather than merely conserve it.

Changing a nine-cycle to an eleven-cycle changes the generated masses.  The
runner tests that discriminator.  An even cycle hits beta `pi`, where the
Cayley mass diverges.  Neither observation selects the physical register.

This is not an observed mass spectrum, a Koide result, or a prediction.  It
does not explain three families, choose positive-mass sectors, or reproduce
known mass ratios.  It converts a per-law parameter into an operator spectrum;
it does not derive which operator Nature uses.

The local register is an abstract onsite/block degree of freedom.  Although a
nine-state register fits dimensionally inside four qubits, no strict
nearest-neighbour block compiler is supplied here.  The original one-qubit
lattice therefore still needs a physical encoding theorem before this can be
called microscopic closure.

There is no fermionic statistics, chirality/gauge content, tensor/nonlinear
gravity, radiation, continuum theorem, empirical prediction, clock-rate law,
occurrence, record formation, or Born-frequency derivation.  There is no
axiom conclusion.

## Attribution and scope

Cayley transforms, phase estimation/registers, and block-diagonal conserved
sectors are standard mathematical structures.  No global novelty is claimed;
global novelty has not been established.

The one-dimensional Thirring-QCA molecule used in Cycles 205–209 is published
prior work of Bisio, D'Ariano, Mosco, Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

The Thirring-QCA is not the phase-register spectrum mechanism used here.

This work remains on the draft parking branch and changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/generated_beta_phase_register_cycle220_2026_07_16.py
```
