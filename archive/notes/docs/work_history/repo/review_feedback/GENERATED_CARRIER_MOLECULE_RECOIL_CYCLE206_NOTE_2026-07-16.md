# Generated carrier–molecule recoil — Cycle 206

Date: 2026-07-16

Status: deterministic finite candidate-law construction; audit unset

Authority: none

Companion runner:
`scripts/generated_carrier_molecule_recoil_cycle206_2026_07_16.py`

This note and runner live only on the draft parking branch and draft PR #5389.
They change no foundation, axiom, primitive, registry, policy, audit, or queue
surface.

## Attribution boundary

The two-particle bound-state engine is inherited from the Thirring quantum
cellular automaton introduced and solved by Bisio, D'Ariano, Perinotti, and
Tosini:

<https://doi.org/10.1103/PhysRevA.97.032132>

Bisio, D'Ariano, Mosco, Perinotti, and Tosini also give a simplified
two-particle derivation and simulations:

<https://doi.org/10.3390/e20060435>

The strict Dirac walk, its onsite two-particle phase, and the existence and
solution of its two-particle bound states are prior work from those papers.
This repository calls the selected localized bound-state packet a “molecule.”
Cycle 206 adds a distinguishable third carrier and a candidate onsite collision
phase between that carrier and either constituent. The three-body extension
and its operational tournament are exploratory framework work; they are not
attributed to the cited papers.

## Result up front

Cycle 205 measured the molecule's inertia with a supplied phase-gradient
force. Cycle 206 removes that force profile. A third Dirac carrier is prepared
to cross the molecule, and a fixed translation-invariant phase is applied
only when the projectile and a constituent occupy the same site. All three
carriers then receive the same kind of strict one-edge walk. Nothing changes
with time except the state; there is no scheduled kick, moving wall, force
lookup, or host-selected collision instant.

With the projectile phase deleted, the wave packets cross geometrically but
the molecule acquires neither momentum nor displacement. With phases
`eta=0.03 pi` and `0.06 pi`, the projectile loses and the molecule gains
oppositely directed first-harmonic momentum. The exact total translation
charge—both phase and magnitude of the simultaneous-translation
characteristic—is constant to numerical precision. The molecule recoils, and
the stronger phase produces more recoil.

The interaction is not perfectly elastic. At the reference readout, the weak
collision retains about 98.7% of the exact selected molecular band; the
stronger collision retains about 95.2%. Within the surviving branch, more
than 99.7% of its relative-coordinate probability remains within distance
two. The remainder is a real inelastic/breakup channel, not discarded noise.

This advances matter from “responds to an imposed force” to “exchanges
momentum with another lawful carrier while predominantly remaining the same
bound object.” In that precise sense, it is generated recoil rather than a
supplied-force response.

## The microscopic candidate

The three-body step is

```text
U_3 = (W_pair tensor W_pair tensor W_projectile) V_pair V_collision,
```

where `V_pair` is the Cycle-205 Thirring interaction and `V_collision`
contributes `exp(i eta)` whenever the distinguishable projectile shares a site
with either fermion. If all three coincide, the two constituent–projectile
contacts contribute twice. Every interaction is onsite; every walk moves its
carrier by at most one edge in a tick.

The runner verifies norm preservation on a generic complex state, exact
translation covariance, reflection covariance with internal-label exchange,
and fermionic antisymmetry of the two molecule constituents. Moving the
interaction layer from the beginning to the end of the tick is an exact
time-origin conjugacy, not a new spectrum or a hidden second law.

The phases are generic complex non-Clifford angles. This is not a rebit-only
or classical carrier interaction.

## What is conserved

For a narrow packet, the phase of the one-step translation characteristic is
an operational momentum coordinate. Separate projectile and pair
characteristics change during the collision. Their phases move in opposite
directions and approximately balance at weak scattering. More fundamentally,
the characteristic for translating all three carriers together remains
exactly constant throughout the complete trajectory. That exact statement is
the finite translation-symmetry conservation test; it does not rely on fitting
packet centers.

The runner also repeats the weak collision on a held-out ring size. Selected
molecular-band population, pair momentum, and recoil position remain stable
within the declared finite tolerances. The late readout occurs after contact
has fallen by more than an order of magnitude and before any second encounter.

## Why this does not yet remeasure one mass

It would be misleading to divide a single unconditional center velocity by
the transferred momentum and call that the Cycle-205 mass. The collision
produces an outgoing entangled mixture: a dominant molecular band, a small
breakup sector, and correlated projectile channels. Stronger coupling both
increases recoil and lowers projectile-subsystem purity and molecular-band
population. The unconditional center is therefore not one narrow freely
propagating mass packet.

The correct next experiment is an asymptotic scattering construction with a
physical late outcome record. Each record-conditioned scattering branch must
retain a narrow molecular momentum distribution; only then should its recoil
velocity be compared with the independently fixed Cycle-205 dispersion mass.
That is a sharper bridge between operational quantum theory and matter than
post-selecting a convenient number in the current finite trajectory.

This is a named open completion of this candidate, not a claim that such a
scattering construction is impossible.

## Bare-metal interpretation

This model answers one conceptual question directly: interaction need not be
only through permanent records. Coherent, unrecorded carrier amplitudes
propagate under the local walk, and their local coincidence changes the future
through the onsite phase. A later record may archive which outgoing channel
occurred, but the record is not the force carrier and record count is not the
mass.

That conclusion is conditional on this candidate quantum law. It does not
derive the law from Admissibility, prove that the current Qualification text
allows every coherent working variable, or decide the ontology of the final
framework.

## Cross-lane effect

### O — operational quantum

The collision creates a concrete entangled branch structure whose
unconditional state cannot be replaced by a single classical recoil number.
It supplies the physical target for a late record process: generate a local
outgoing-channel record, condition on the complete record corpus, and verify
the predicted molecular response. The actual formation and probability of
that record remain open.

### T — time

One strict tick composes interaction and propagation, and the two cyclic
placements are related by an exact time-origin conjugacy. This strengthens the
case that clock meaning must be derived from repeated physical processes, not
from an arbitrary ordering label. The quasiphase-to-energy composition seam
from Cycles 204–205 remains.

### I — matter

The lane gains generated scattering, momentum exchange, whole-object recoil,
fermionic pair identity, and quantified survival/breakup channels under one
strict update. Still missing are an asymptotic S-matrix, record-conditioned
mass recovery, multiple molecule species, charge interpretation, autonomous
creation, empirical parameter selection, and three-dimensional covariance.

### G — gravity

The collision provides a local momentum/interaction ledger that a future
active-source rule must respect. It does not make the projectile phase a
gravitational field, generate a common lapse, or close the source/response
triangle. Archive count remains excluded as a mass proxy by the spectator
record controls of Cycles 201–205.

### B — boundary

Incoming packets, carrier number, masses, and both interaction angles remain
prepared. The framework does not yet generate their abundance, collision
distribution, or late outcome record from a common boundary/history process.

## Next construction

The immediate continuation is a local late-channel detector coupled to the
outgoing projectile. It must write a record without feeding back into the
already separated molecule, expose transmitted/reflected/breakup branches,
and allow each retained molecular branch to face the dispersion/inertia test.
In parallel, the same interaction architecture needs a proper-cubic lift and
an energy/source ledger suitable for the Cycle-204 gravity triangle.

## Scope boundary

This is a finite one-dimensional candidate-law probe. The proper-cubic lift
remains open. It is not a derivation of the microscopic law, a relativistic
field theory, an elementary-particle spectrum, an empirical cross section, a
gravity result, or a completed measurement process. The distinguishable
projectile and collision angle are supplied. It makes no broad no-go or
minimum-content claim and supports no axiom conclusion.
