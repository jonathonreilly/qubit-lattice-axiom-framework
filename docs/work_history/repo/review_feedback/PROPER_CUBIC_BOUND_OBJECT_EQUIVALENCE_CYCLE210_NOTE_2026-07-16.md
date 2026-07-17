# Proper-cubic bound object and conditional equivalence — Cycle 210

**Date:** 2026-07-16

**Authority:** none

**Status:** strict proper-cubic candidate interaction and bounded conditional
rest/inertia/source-response bridge

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py
```

## Attribution boundary

Cycle 205's one-dimensional Thirring engine is prior work of Bisio,
D'Ariano, Mosco, Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

It supplies the earlier strict fermionic molecule, not the construction in
this note.  The general isotropic-quantum-walk background includes D'Ariano,
Erba, and Perinotti:

<https://arxiv.org/abs/1708.00826>

Their classified two-component three-dimensional walk uses a BCC generating
set.  Cycle 210 instead tests a supplied six-direction cardinal carrier and a
new candidate contact coin on standard cubic edges.  Global novelty has not
been established; the result is an internal framework construction requiring
a dedicated literature comparison before any novelty claim.

## Question

Cycles 205–209 use a strong published one-dimensional object and progressively
replace imposed force and global readout with generated recoil and a local
coherent detector.  But rotating a line apparatus inside three dimensions is
not a three-dimensional matter law.

Can one strict proper-cubic update produce a law-derived persistent object,
give it one operational dispersion mass under forced inertia, and let the
same scalar participate in a weak source/response test without identifying
mass with a record count?

## Candidate mechanism

Each distinguishable carrier has six direction modes

```text
+x, -x, +y, -y, +z, -z.
```

Every tick contains an onsite coin followed by one cardinal-edge stream.  The
six-direction representation of the 24-element proper-cubic group splits
into scalar, even-traceless, and vector sectors with projectors `P0`, `PE`,
and `PV`.  The molecular coin is

```text
C = exp(i phi) [P0 + exp(i alpha) PE + exp(i beta) PV].
```

Two separated carriers receive independent generic complex proper-cubic
coins.  When they occupy the same site, the contact correction replaces that
independent coin by a
unitary which acts as `C` on the six equal-direction states `|d,d>` and as the
identity on their orthogonal complement.  Equal-direction components then
take the same edge and remain coincident.  This is an exact invariant bound
sector, not a potential inserted into a continuum equation.

The contact correction is onsite, unitary, number preserving, and commutes
with simultaneous rotation of the two direction registers.  Its binding
projector and phases are supplied candidate law content; they are not derived
from the axioms.

This is exact invariant-sector, or kinematic, binding.  The construction does
not yet prove a protective quasienergy gap against every symmetry-allowed
perturbation.  In that precise sense it is more engineered than the published
Thirring molecule, whose bound state arises from the solved two-particle
spectrum.

## Result up front

The construction succeeds at the bounded structural target.

- The interacting pair remains at zero relative separation under every
  tested tick: it is a law-derived persistent object.
- Deleting only the contact correction sends the identical prepared pair
  through independent coins and disperses its relative coordinate.
- Every constituent moves at most one cardinal edge per tick.
- The one-object Bloch walk and the two-body contact update are exactly
  covariant under all 24 proper-cubic rotations.
- The low-momentum scalar band has an isotropic curvature tensor.
- A literal local phase gradient accelerates a packet with `F/a` equal to the
  independently computed curvature mass.
- One and two decoupled spectator records leave the matter distribution and
  mass data unchanged.

The reference finite checks give:

| `beta` | `alpha` | rest/curvature mass | measured `F/a` | relative difference | `|a|/g` |
|---:|---:|---:|---:|---:|---:|
| -0.2 | -0.60301205 | 0.30100402 | 0.30232871 | +0.440% | 0.995630 |
| -0.3 | -0.91021696 | 0.45340565 | 0.45413794 | +0.162% | 0.998392 |
| -0.4 | -1.22439032 | 0.60813011 | 0.60695632 | -0.193% | 1.001936 |

For the reference `beta=-0.4` object, contact probability remains one through
twelve interacting ticks.  With only the contact correction deleted it falls
to `0.06195`, relative variance grows to `26.94`, and norm remains one.  A
random vector spanning the full six-dimensional equal-direction sector also
remains exactly at contact, so persistence is a domain property rather than
one selected eigenvector.

The interaction deletion is important: a real Grover deletion coin was also
tested and rejected as a control because it accidentally preserves the
maximally entangled equal-direction input.  The retained complex deletion
coin removes that hidden symmetry while retaining locality, unitarity, and
cubic covariance.

## The aligned family and what it means

For the scalar molecular band, the exact curvature mass is

```text
m_disp = 3 tan(-beta/2),   for the tested negative-beta branch.
```

The analytic reason is small but useful.  A momentum derivative maps the
normalized scalar direction vector wholly into the odd/vector sector with
squared norm `1/3`.  Second-order unitary perturbation therefore gives

```text
d2 omega / dk_i2 = -(1/3) cot(beta/2)
```

on every axis, with zero mixed derivatives.  The runner verifies both that
projector identity and a held-out `beta=-0.35` numerical band.

Fixing the contact coin to `SU(6)` imposes

```text
6 phi + 2 alpha + 3 beta = 0  (mod 2 pi).
```

Cycle 210 then investigates—not derives—the one-condition family

```text
phi = m_disp.
```

For `beta = -0.2, -0.3, -0.4`, the corresponding `alpha` is solved from the
determinant condition.  Rest phase, curvature mass, and measured forced
inertia agree for every member.  A held-out two-molecule composition test
adds both rest phase and inertia.  The construction therefore shows that
strict locality, exact cubic symmetry, binding, composition, and operational
mass agreement can coexist in one update.

The runner also conjugates the complete molecular and contact blocks into a
Fourier coin basis and checks that their spectra are unchanged.  It compares
coin-then-stream with its cyclic time-origin schedule, verifies the exact
free-coin/contact-correction factorization, and keeps all retained phases
away from Clifford quarter-turns.  The result is neither a coordinate-basis
effect nor a rebit-only control.

It does **not** show that the update selects this family.  Shifting `alpha`
while preserving unitarity, cubic covariance, and `SU(6)` changes `phi`
without changing the curvature mass.  The alignment is one explicit law
condition, not a theorem of the present symmetry assumptions.

The internal excitation gap `min(|alpha|,|beta|)` also remains different from
the aligned rest/inertial scalar.  Thus “rest phase,” “internal gap,” and
“inertia” must not be silently treated as synonyms.

## Conditional scalar-lapse source/response bridge

The runner next lets the same local rest generator play two roles:

```text
source charge of one bound object = phi;
force in a supplied scalar-lapse gradient g = phi g.
```

Because the tuned family has `phi=m_inertial`, all three tested species
accelerate at the same weak-field rate.  Source charges add for two objects
and do not double when a redundant archive record is added.

This is a useful equivalence-principle construction, but the source map
remains supplied.  No local field equation generates the lapse, no exchange
carrier mediates it, no backreaction or curvature is calculated, and no
continuum Einstein equation follows.

## Bare-metal interpretation

This cycle sharpens the mass ontology:

```text
the object is the invariant two-carrier continuation sector;
its inertial mass is the inverse curvature of that sector's propagation;
its rest/source scalar is a phase of the local collision generator;
records can identify or archive the object but do not constitute its mass.
```

That is structurally compatible with the Cycle-209 detector: coherent
nonrecord possibilities do the propagation and comparison, while a later
causally complete apparatus may append a class record.  Record formation
remains open.

## Remaining seams

The construction deliberately leaves visible:

1. selection or derivation of the six-mode block and contact projector;
2. selection of `alpha`, `beta`, and the one-condition alignment family;
3. autonomous preparation of the invariant bound sector;
4. generated cubic third-carrier scattering and record-conditioned recoil;
5. a derived clock/energy map outside the aligned branch;
6. an active scalar source, propagation law, universal coupling, and
   backreaction;
7. fermionic statistics and a physical species/chirality spectrum;
8. occurrence, record formation, and Born frequencies; and
9. an empirical prediction.

## Scope

This is a finite candidate-law result on the draft parking branch.  It does
not replace or extend the cited Thirring solution, establish global novelty,
derive a mass value, select a microscopic law, prove gravity, or complete a
TOE.  It makes no axiom conclusion and changes no foundation, primitive,
registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py
```
