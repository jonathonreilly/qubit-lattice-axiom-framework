# Proper-cubic generated recoil — Cycle 212

**Date:** 2026-07-16

**Authority:** none

**Status:** finite conditional three-carrier collision and relational
incremental-mass result

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/proper_cubic_generated_recoil_cycle212_2026_07_16.py
```

## Attribution boundary

The one-dimensional Thirring engine is prior work of Bisio, D'Ariano, Mosco,
Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

It supplies the molecule reproduced in Cycle 205, not this cubic collision.
Cycle 212 extends the internal Cycle-210 six-direction invariant object with a
third carrier and an onsite partial-SWAP tournament.  Global novelty has not
been established; no literature-wide novelty claim is made.

## Question

Cycle 210 measured the proper-cubic object's inertia with a supplied local
phase gradient.  Does the same object exhibit its independently fixed mass
when recoil is generated instead by a third carrier and a fixed onsite law?

## Candidate collision

Inside Cycle 210's exact equal-direction bound sector, the two constituents
are represented by one six-direction molecular register.  A distinguishable
six-direction projectile supplies the third carrier.  When projectile and
molecule meet, their direction registers receive

```text
V_eta = cos(eta) I + i sin(eta) SWAP.
```

They then receive their separate cubic coins and stream one cardinal edge.
The partial-SWAP is onsite, unitary, translation invariant, and commutes with
simultaneous application of every proper-cubic direction permutation.  It
does not move the molecule out of the equal-direction constituent sector, so
the underlying two-carrier object remains exactly bound.

The update contains no scheduled kick, force profile, collision lookup, or
chosen impact tick.  The same contact gate is present at every site and every
tick.  Collision deletion is exactly `eta=0`.

## Result up front

The finite generated-recoil test succeeds at its scoped target.

A localized relative packet encounters the contact region under the strict
law.  A supplied late partition into relational branches divides the outgoing
relative position into projectile-left (`T`), projectile-right (`R`), and
unresolved (`X`) sectors.  Increasing the partial-SWAP angle from zero through
`pi/4` to `pi/2` increases the `R` probability and generates a monotone change
in the molecule's conditional momentum.

The important comparator subtracts the `eta=0` branch selected by the same
relational mask.  Thus finite-packet recoil created merely by the late
partition is removed before a mass is inferred.  The collision-generated
increment satisfies

```text
m_incremental = |Delta p_molecule| / |Delta v_molecule|.
```

For the reference volume, both nonzero collision strengths give an
incremental mass within `0.4%` of the independently evaluated tangent mass of
the Cycle-210 band and within `2.5%` of its zero-momentum rest/curvature mass.
The strong `R` branch remains more than `88%` in the scalar molecular band.

Reference values:

| `eta/pi` | `(T,R,X)` | generated `Delta p_x` in `R` | incremental mass |
|---:|---|---:|---:|
| 0 | `(0.3062795, 0.5209750, 0.1727455)` | baseline | — |
| 0.25 | `(0.2998875, 0.5268328, 0.1732797)` | 0.00417497 | 0.61893579 |
| 0.50 | `(0.2998090, 0.5310433, 0.1691477)` | 0.00568970 | 0.61920578 |

```text
independent tangent mass        0.61821461
zero-momentum rest/curvature    0.60813011
held-out L=29 incremental       0.62055312
held-out L=33 incremental       0.62140969
```

Two held-out volumes retain the incremental mass to within `0.2%` of each
other even though the finite recoil magnitude drifts.  This is the stable
quantity; an asymptotic scattering amplitude is not claimed.

## Why the subtraction matters

Even with collision deletion, a finite late position partition selects a
nonzero conditional molecular momentum.  Calling that absolute momentum
“generated recoil” would be wrong.  Cycle 212 therefore compares identical
prepared packets, identical evolution duration, and identical relational
masks, changing only the onsite collision angle.

This turns the deletion branch into the counterfactual baseline and makes the
reported `Delta p/Delta v` interaction-generated.

## Controls

The runner checks:

- exact unitarity of the fixed-total-momentum relative update;
- one-edge constituent streaming and radius-two relative support;
- molecule, projectile, and partial-SWAP covariance in all 24 cubic frames;
- common-basis representation invariance;
- cyclic collision/coin time-origin phase equivalence;
- generic complex non-Clifford coin phases;
- positive normalized `T/R/X` alternatives;
- collision deletion and monotone angle response;
- independent tangent-mass and rest/curvature-mass comparators;
- scalar-band survival and momentum coherence;
- redundant outcome-record invariance; and
- held-out finite-volume stability of the incremental mass.

## Detector and record boundary

The late `T/R/X` position partition is supplied.  It is relational and can be
compiled by the arithmetic/coherent machinery of Cycle 209, but that compiler
has not yet been physically joined to this three-dimensional collision.
Record formation remains open.  No occurrence or Born-frequency theorem is
claimed.

## Scope

This is finite pre-asymptotic scattering, not an S-matrix.  The packet has
visible transverse spreading and boundary sensitivity; the absolute branch
weights and recoil magnitudes are not presented as converged observables.
Only the deletion-subtracted incremental mass is stable across the tested
volumes.

The molecule, projectile coin, packet, total momentum, partial-SWAP angle,
late partition, and readout are supplied.  There is no autonomous
preparation, species selection, active field coupling, clock derivation,
record occurrence, or empirical prediction.  No axiom conclusion follows.
No foundation, primitive, registry, policy, queue, or audit surface is
changed.

## Verification

```text
python3 scripts/proper_cubic_generated_recoil_cycle212_2026_07_16.py
```
