# Locally bound composite mass bridge — Cycle 203

Date: 2026-07-16

Status: source-grade exact band derivation plus deterministic finite local-law
probe; audit unset

Authority: none

Companion runner:
`scripts/locally_bound_composite_mass_bridge_cycle203_2026_07_16.py`

This note and runner live only on the draft parking branch and draft PR #5389.
They change no foundation, axiom, primitive, registry, policy, audit, or queue
surface.

## Result up front

Cycle 203 replaces Cycle 202's freely spreading one-carrier packet with the
first autonomously bound relative sector in the mass campaign.

Two distinguishable carriers hop to nearest neighbours with amplitude `J` and
attract by `-U` only when they occupy the same site. The interaction is local,
translation invariant, and independent of any record count. It produces a
bound two-carrier band whose one-dimensional energy is

```text
E_b(K) = -sqrt[U^2 + 16 J^2 cos^2(K/2)].
```

The inverse rest curvature is therefore

```text
M_pair = sqrt(U^2 + 16 J^2) / (4 J^2).
```

The runner constructs a broad center-of-mass packet directly from the exact
finite-ring bound eigenvector in each retained total-momentum block. It then applies the same
onsite phase gradient to each constituent and evolves the complete two-body
wavefunction under the local hopping-plus-contact generator. The measured
total force divided by center acceleration recovers `M_pair` while the
relative coordinate remains bound.

This is a composite matter mechanism, not merely a renamed coefficient or a
durable trace of where something was.

## Finite results

The direct two-body experiment uses `J=0.5`; the force on the whole object is
the sum of the two constituent forces. No band projection is applied during
evolution.

| attraction `U` | measured total `F/a` | bound-band mass | relative error |
|---:|---:|---:|---:|
| 0.4 | 2.039960 | 2.039608 | 0.017% |
| 0.7 | 2.119421 | 2.118962 | 0.022% |
| 1.0 | 2.236743 | 2.236068 | 0.030% |
| 1.5 | 2.501242 | 2.500000 | 0.050% |
| 2.0 | 2.830723 | 2.828427 | 0.081% |

For `U=1`, more than 91.9% of probability begins within relative distance two
and the same fraction remains there after the pushed trajectory. Relative
variance changes by less than the runner tolerance while the pair's center
moves. Norm remains one, and less than `10^-5` probability reaches the region
used to diagnose the periodic boundary.

A four-point control narrows total-momentum width and weakens the push. The
mass error falls from about `0.153%` to `0.016%`, so the agreement has the
expected broad-packet, weak-force limit.

## Bare-metal interpretation

This construction separates three things that had been conflated in older
matter proxies:

```text
membership: two carrier histories belong to one composite sector;
binding: a local interaction keeps their relative separation finite;
mass: the composite band's rest curvature controls whole-object response.
```

The mass is not either carrier, not the contact record, and not the number of
records used to follow the pair. It is a dynamical invariant of the bound
sector created by hopping and attraction together.

The center is still prepared as a broad packet. “Autonomous” here applies to
internal binding after preparation: the local law keeps the constituents
together without a fixed trap, moving wall, host-side membership lookup, or
repeated projection. The framework has not yet generated the pair from its
own boundary process.

## Binding deletion

The sharpest control begins with the same `U=1` bound packet and removes the
contact attraction during evolution.

With attraction retained, close-pair probability remains above `0.9` and
relative variance stays near `2`. With attraction deleted, close-pair
probability falls below `0.15` and relative variance grows above `220` over
the same duration. Deleting the force instead removes center acceleration
while leaving the binding intact.

The object behavior is therefore carried by the interaction. It is not a
packet-shape artifact or an implicit permanent-membership declaration.

## Locality and composition

The two-body generator is

```text
H = -J sum_<x,y>,a (|x><y|_a + |y><x|_a)
    - U sum_x |x,x><x,x|.
```

Every generator term is onsite or nearest neighbour. The finite experiment
uses a symmetric split between the exact hopping exponential and onsite
potential exponential. Four time steps show the expected second-order
convergence of the fitted acceleration. As in Cycle 202, locality belongs exactly to the finite-range
generator; its finite-time exponential is not claimed to have strict finite
support.

The prepared sector is symmetric under exchanging the two carrier labels and
the evolution preserves that symmetry. The carriers are nevertheless typed as
distinguishable in this probe. No fermionic, bosonic, or spin-statistics claim
follows.

## Proper-cubic extension

The same local mechanism is tested on a three-dimensional proper-cubic
relative lattice. At fixed total momentum `K`, the contact interaction gives
the finite-volume secular equation

```text
1 = U mean_q 1 / [epsilon_K(q) - E_b(K)],
epsilon_K(q) = -4J sum_i cos(K_i/2) cos(q_i).
```

For `J=0.5`, `U=6`, and a `17^3` relative grid, the rest bound energy is about
`-7.103918` below a continuum floor of `-6`, a gap of about `1.103918`.
Increasing the relative grid from `13^3` through `21^3` stabilizes that energy.
All 24 proper-cubic frames give the same held-out `E_b(K)` to numerical
precision, and the three axial curvatures agree and are positive.

This establishes a proper-cubic bound-sector extension of the mechanism. The
full forced two-body trajectory is run on the one-dimensional slice; a 3D
source/collision simulation remains open.

## Record redundancy

A one-bit factor labelled as a candidate spectator record is tensored onto
the final bound pair, then a second decoupled copy is added. Tracing either
factor out returns exactly the same two-body probability. The composite mass
and binding therefore do not increase when redundant witnesses are added.

This does not make records irrelevant. A generated record ancestry could
certify that later rest, force, collision, and gravity tests refer to the same
composite, and records can retain measurement results. But the tested binding
is in the coherent relational sector, not in record count.

## The rest-energy seam

The bound band closes dispersion/inertial agreement but exposes, rather than
hides, the remaining rest-energy problem.

Adding a uniform onsite cost `mu` to each constituent shifts the composite
rest gap by `2 mu` without changing its curvature or response. For `J=0.5`
and `U=1`, the unshifted bound energy is `-sqrt(5)` and the inertial mass is
`sqrt(5)`. Choosing `mu=2` or `mu=3` changes the positive excitation gap from
about `1.764` to `3.764` while inertia remains about `2.236`.

Therefore the rest-gap offset remains independent in this nonrelativistic
contact model. Tuning `mu` until rest gap equals inertia would insert the
desired relation. A successful TOE route must instead derive a physical
vacuum/clock normalization or use a relativistic interacting law in which the
rest-energy and response coordinates are linked.

This is a discriminator for this candidate package, not a no-go against other
binding routes.

## Cross-lane effect

### O — operational quantum

The composite exists in a coherent relational wavefunction. Complete record
count does not determine its relative phase or bound-band momentum. The
equal-record-fibre experiment remains necessary to decide whether the fixed
law and complete records reconstruct that state or Qualification needs a
wider working-state clause.

### T — time

Generator time now calibrates both internal binding and whole-object inertia,
but an additive rest-energy/clock zero remains free. This makes the time lane
more concrete: rate alone is not enough; energy normalization must be tied to
an operational clock or vacuum.

### I — matter

The lane advances from a free coherent packet to a locally bound composite
with an exact rest/moving band, internal persistence, whole-object inertial
response, interaction deletion, and a proper-cubic extension. Still missing
are autonomous creation, collisions/scattering, conserved charges, genuine
statistics, species, relativistic rest/inertial equality, and empirical mass
selection.

### G — gravity

The interaction and kinetic energy now provide a concrete local energy ledger
that a gravity candidate could source. No such source equation is yet linked,
and the mass-to-gravity map remains open. Archive count must still not be
substituted for bound energy or inertial response.

### B — boundary

The law binds a supplied pair but does not select or repeatedly prepare it.
The total-momentum envelope, interaction strength, and carrier number are
inputs. A boundary/history process must eventually generate those sectors and
their frequencies.

## Next construction

The highest-leverage next tests are:

1. use the bound pair's local kinetic plus interaction ledger as a candidate
   gravitational source and test whether the same composite responds
   universally to the resulting lapse/resource field;
2. collide a third lawful carrier with the pair to replace the supplied force
   profile with generated momentum exchange; and
3. run the complete-record-fibre discriminator on two equal-record bound-pair
   phases whose later position records differ.

The rest-gap seam should be attacked in parallel with a relativistic local
interaction, not closed by choosing an onsite offset.

## Scope boundary

This is an exact/numerical candidate-law construction for a bound composite.
It is not an elementary particle, quantum field theory, Standard Model
spectrum, relativistic binding theorem, empirical mass, autonomous universe,
equivalence principle, or gravity law. Multiple `U` values and bound masses
survive; none is selected. It makes no minimum-content or broad no-go claim
and supports no axiom conclusion.
