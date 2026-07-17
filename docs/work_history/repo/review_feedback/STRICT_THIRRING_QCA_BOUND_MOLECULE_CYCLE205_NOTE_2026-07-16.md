# Strict Thirring-QCA bound molecule — Cycle 205

Date: 2026-07-16

Status: primary-source reproduction plus deterministic finite operational
extension; audit unset

Authority: none

Companion runner:
`scripts/strict_thirring_qca_bound_molecule_cycle205_2026_07_16.py`

This note and runner live only on the draft parking branch and draft PR #5389.
They change no foundation, axiom, primitive, registry, policy, audit, or queue
surface.

## Attribution boundary

The microscopic construction and the existence of its two-particle bound
states are prior work. The primary source is Bisio, D'Ariano, Mosco,
Perinotti, and Tosini, *Solutions of a Two-Particle Interacting Quantum Walk*:

<https://arxiv.org/abs/1804.08508>

That paper studies a one-dimensional fermionic Thirring quantum walk: a
strict Dirac walk is followed by an onsite number-preserving interaction
phase, and the two-particle problem has scattering and molecular bound
solutions. Cycle 205 claims no novelty for that automaton, its analytic
solution, or the existence of the bound molecule.

Our narrower extension is an operational tournament. We independently build
the finite two-particle update and ask whether one selected molecular branch
has mutually coherent rest phase, dispersion curvature, total-force response,
internal binding, and spectator-record behavior. The answer is positive for
dispersion versus forced inertia and negative only in the modest sense that
the rest phase is a distinct coordinate under the standard one-tick phase
map. No broad impossibility follows.

## Result up front

The runner reproduces a strict local update of the form

```text
U_2 = (W_m tensor W_m) V_chi,

W_m = [[n T_dagger, -i m],
       [-i m,        n T]],       n = sqrt(1-m^2),
```

where `V_chi` contributes `exp(i chi)` only when the two walkers occupy the
same site with opposite internal labels. Each constituent moves by at most one
edge per tick. The update is exactly unitary, translation invariant, and
preserves fermionic antisymmetry.

At `m=0.6` and `chi=0.2 pi`, the selected positive-phase molecular branch has
approximately

```text
rest quasiphase       0.372979 per tick
curvature mass        0.5696
near-pair probability 0.971
```

A center-localized packet is assembled from the exact finite-ring bound
eigenvector at each retained total momentum. Applying equal weak phase
gradients to both constituents gives a total force. The complete real-space
unitary trajectory returns `F_total/a` within one percent of the independently
extracted curvature mass while the relative coordinate stays bound. There is
no band projection during evolution.

This is the campaign's first strict-update, fermionic, relativistic-walk
candidate in which local interaction, durable composite identity, dispersion
mass, and measured inertia coexist. It is stronger than the nonrelativistic
generator composite of Cycle 203, but remains a candidate model rather than a
selected law.

## Independent controls

The finite total-momentum block is unitary to numerical precision and agrees
with a literal position-space application of the two single-particle walks
and the onsite interaction phase. A localized basis state reaches only the
one-edge light cone in one tick. Reversing the cyclic order of walk and
interaction preserves the finite spectrum, as expected for the two orderings
`WV` and `VW` of unitary factors.

The bound branch is selected by three independent properties rather than by
an expected eigenvalue: positive quasiphase, fermionic exchange parity, and
maximum probability near zero relative separation. Rest phase and curvature
converge from finite rings. The curvature uses the first allowed nonzero ring
momentum and an explicit leading `1/L^2` extrapolation; it does not pretend an
arbitrary infinitesimal momentum is available on a periodic finite ring. Six
held-out `(m, chi)` pairs retain positive curvature and localized molecular
branches, so the reference point is not an isolated lookup.

Deleting the external phase gradient removes center acceleration. Deleting
the interaction from the subsequent evolution increases relative variance by
more than two orders of magnitude and reduces near-pair weight. That control
should not be read as proving that the free walk has no localized sector; the
cited model has special free bound solutions. It shows only that the prepared
interacting molecule is not preserved in the same way under this deletion.

The mass mixing and interaction angle are generic complex, non-Clifford
phases. Norm, exchange parity, and a periodic-boundary comparator are checked
through the forced trajectory.

## What “mass” means here

The candidate object's identity is the localized relative-coordinate sector.
Its operational inertial mass is the inverse curvature of that branch's
center-of-mass quasiphase. A force is applied independently as a phase gradient
to both physical constituents; their combined impulse divided by the measured
center acceleration recovers the same number.

The mass is therefore neither a stored record nor the number of sites occupied.
One spectator record can be tensored onto the final state and then a second
independent spectator record can be added. Tracing either out returns the same
matter probability exactly. Redundant witnesses do not double the molecule's
mass or binding.

The record factors in this control are deliberately decoupled. This does not
show that the framework's full record process can prepare, identify, or read
the molecule. It only rules out raw archive multiplicity as the tested mass
coordinate.

## The remaining rest/clock seam

For the reference molecule, rest quasiphase and curvature mass are both
law-derived but numerically unequal. That is not a defect by itself: a
discrete-time unitary supplies an angle modulo `2 pi`, whereas inertial response
uses local band curvature. A physical clock/energy map must say how the angle
is read and composed before the two can be compared as masses.

Cycle 204 showed that choosing a nonlinear phase map after seeing the answer
can repair a one-particle equality while leaving multiparticle composition
unexplained. This molecule provides a better test bed for that issue because
its phase and curvature arise from an actual interaction. The next clock-map
probe must be fixed across free particles and molecules and must survive
composition; it may not be chosen separately for each `(m, chi)` sector.

This observation is a discriminator among operational clock maps, not a
no-go claim against strict QCA matter.

## Cross-lane effect

### O — operational quantum

The probe supplies a concrete, non-Clifford coherent object whose later
position statistics depend on its molecular band phase. Records remain
spectators in this construction. The equal-complete-record-fibre experiment
is still required to learn whether the fixed law plus actual records determine
the molecule's future or whether a coherent/relational working state remains
ontic between records.

### T — time

One strict tick now advances a bound composite, and its rest quasiphase and
motion are both measurable within the same update. The unresolved question is
which compositional clock map converts quasiphase into operational energy.
This sharpens the time lane without adopting a time axiom.

### I — matter

The lane gains a published strict fermionic mechanism, independently
reproduced, with internal binding and a mass confirmed by forced response.
Still open are a proper-cubic lift, autonomous production, generated
collisions, conserved-charge interpretation, species selection, empirical
mass ratios, and a universal rest/inertial coordinate.

### G — gravity

The molecule gives gravity a much better source/probe target than archive
count: a local interaction creates a persistent sector with independently
measured inertia. No active source rule, common lapse coupling, or tensor
field is implemented here. The Cycle-204 triangle must be rerun on the full
strict update rather than attaching an external rest-sector potential by
hand.

### B — boundary

The two-particle sector, branch packet, mass parameter, interaction angle, and
weak force are prepared inputs. Nothing selects their cosmological abundance
or creates the molecule from the framework's boundary/history process.

## Next probes

The highest-leverage continuations are:

1. replace the imposed phase-gradient force with momentum exchange generated
   by a third lawful carrier and verify whole-molecule recoil;
2. test one clock/source map simultaneously on free and molecular branches,
   including phase composition and record redundancy;
3. construct or rule in a proper-cubic interacting lift with the same strict
   locality and covariance controls; and
4. run two equal-record molecular preparations whose hidden band phases give
   different later records, while accounting for complete preparation history.

## Scope boundary

This is a finite reproduction and operational extension of a published
one-dimensional model. The proper-cubic lift remains open. It is not a law
selection, elementary-particle derivation, Standard Model result, empirical
mass prediction, gravity theory, or proof that records are sufficient or
insufficient. It supports no axiom conclusion.
