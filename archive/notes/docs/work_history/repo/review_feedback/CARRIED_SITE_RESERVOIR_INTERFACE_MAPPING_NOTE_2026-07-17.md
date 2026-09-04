# Carried / site-reservoir interface mapping — 2026-07-17

**Type:** constructive local-code interface and stream-repair probe

**Status:** exact local interface; fixed-stream mismatch quantified; two repairs pass

**Authority:** none

**Audit:** unset

**Constitutional effect:** none

**Runner:** `scripts/carried_site_reservoir_interface_mapping_2026_07_17.py`

## Result

One carried `e/g` matter-direction block and the site-reservoir/field `Q=1`
block are the same seven-state local exchange system up to a supplied local
minus sign.  Extending that map over all six matter directions gives an exact
42-state intertwiner for:

- the conjugate source/field vertex;
- the common matter coin and six-direction field coin; and
- all 24 proper-cubic frame representations.

The exact vertex intertwiner and exact coin intertwiner are constructive
results on this declared local code space.

The unmodified streams do not intertwine.  In the site-local route the
fixed reservoir excitation remains at the departure cell while matter streams one
edge.  In the carried route the `e/g` source label moves with matter.  A tagged
position comparison gives the exact one-step residual rather than identifying
states that live at different reservoir locations.

Two constructive repairs close that stream mismatch on the declared
one-matter sparse domain:

1. a co-moving repair transports the reservoir flag along the same directed
   edge as matter; and
2. a staggered catch-up repair first streams matter, temporarily leaves the
   local image, and then applies a direction-conditioned transposition between
   the upstream and arrival-cell reservoir tags.

Both repaired macrosteps exactly reproduce the carried update.  This is a
constructive interface mapping with no no-go claim and no axiom pressure.

## Exact seven-state isometry

Let the site block be

```text
{|r>} direct-sum {|f_b> : b=0,...,5},
```

and fix a carried matter direction `d`.  Define

```text
J_d |r>   = -|e,d;0_f>,
J_d |f_b> =  |g,d;f_b>.
```

The local minus sign is load-bearing.  The site gate is

```text
V_site(theta)=exp(-i theta T_site),
```

whereas the carried convention is

```text
V_carried(theta)=exp(+i theta T_carried).
```

The map obeys

```text
J T_site = -T_carried J,
J V_site(theta) = V_carried(theta) J.
```

With `J=direct-sum_d J_d`, the cold-run residuals are

```text
J^dagger J - I                         0.0
J J^dagger - I                         0.0
vertex intertwiner                     0.0
generator-sign identity                0.0
matter-plus-field coin intertwiner     0.0
maximum 24-frame intertwiner           0.0
```

The site frame representation is matter direction tensored with a scalar
reservoir plus vector field.  The carried frame representation is `D` on the
excited branch and `D tensor D` on the ground/field branch.  The same `J`
intertwines them without a preferred direction or frame.

## Physical-M2 boundary

For one fixed direction, the input reservoir/field block is the `Q=1`
subspace of seven physical M2: one reservoir M2 plus six field M2.  Its seven
computational states map injectively into seven states of the direct carried
18-M2 cell.  All six direction blocks fill the carried 42-state active code.

The matter direction on the site side is a logical label in this runner.  No
physical Cycle-269 matter-state encoder is constructed, and this result is not
a Cycle-269 physical state encoder.  The local map is a bounded code isometry
between the displayed blocks; the runner does not synthesize one full-Hilbert
unitary converting the different physical allocations.

The co-moving and catch-up rules below are nearest-neighbor logical
permutations on the declared one-matter domain.  Their compilation into the
Cycle-269 physical matter representation, and their collision behavior for
several matter carriers, remain untested imports.

## Tagged sparse domain

The site-side sparse state keeps the reservoir coordinate explicit:

```text
reservoir branch: (matter cell, reservoir cell) x matter direction
field branch:     (matter cell, field cell) x matter direction x field direction.
```

The local image has `reservoir cell = matter cell`.  The carried excited
amplitude maps to the negative of that co-located reservoir amplitude; the
ground/field amplitude maps without an extra phase.  This tagged Hilbert space
makes departure-cell and arrival-cell reservoir states orthogonal when their
positions differ.

The tested tick is

```text
matter and field coins
  -> local source/field vertex
  -> matter stream
  -> field stream.
```

The separate one-matter contact fixture is not applied.  It is the identity
on the executed matter-number sector, so omitting it does not change the
tested update.

## Exact fixed-reservoir mismatch

For a co-located reservoir branch with direction `d`, the two streams give

```text
site fixed:  |body=x+e_d, reservoir=x>,
carried:     |body=x+e_d, reservoir tag=x+e_d>.
```

These tags are orthogonal on the declared lattice domain.  If the postvertex
reservoir-branch squared norm is `w_r`, then

```text
local-image leakage norm = sqrt(w_r),
tagged stream residual   = sqrt(2 w_r).
```

For the scalar reservoir input at

```text
theta=0.8 m=0.3627245233399082,
w_r=cos^2(theta)=0.8741007838712862,
```

the runner obtains

```text
image leakage norm       0.9349335719029922
tagged stream residual   1.322195737303133
exact target             1.322195737303132.
```

At coupling deletion `theta=0`, the fixed-reservoir residual becomes exactly
`sqrt(2)=1.4142135623730963`: deleting emission does not repair the different
stream ownership.  This is a route-specific stream mismatch, not a local
vertex mismatch and not a shared substrate obstruction.

## Co-moving repair

On the reservoir branch, replace the fixed stream by

```text
|body=x,d; reservoir=x>
    -> |body=x+e_d,d; reservoir=x+e_d>.
```

The ground/field branch retains the ordinary matter and field streams.  On the
declared one-matter image, this co-moving permutation gives

```text
J G_site,co-moving = G_carried J.
```

Cold-run controls give

```text
one-step full-update residual           0.0
one-step local-image leakage             0.0
maximum four-tick intertwiner residual   0.0
four-tick inverse residual               2.7508449838546606e-15
coupling-deletion residual               0.0
```

Thus moving source capacity is not blocked by the local seven-state algebra;
it requires a different stream law.

## Staggered catch-up repair

The second repair retains the fixed matter-stream substep, then applies a
direction-tagged nearest-neighbor catch-up:

```text
matter stream:
  |body=x,d; reservoir=x>
      -> |body=x+e_d,d; reservoir=x>

reservoir catch-up at y=x+e_d:
  |body=y,d; reservoir=y-e_d>
      <-> |body=y,d; reservoir=y>,
  all other reservoir tags fixed.
```

The two-way arrow is load-bearing.  The catch-up is a conditional
transposition, not a reset of the reservoir tag, so it is a norm-preserving
involution on the full tagged one-matter basis.  An adversarial off-image state
with simultaneous upstream-tag and arrival-tag amplitudes has norm-change
`0.0` and catch-up-involution residual `0.0`.

For the scalar input, the intermediate leakage is
`0.9349335719029922`.  After catch-up the leakage and staggered-versus-co-moving
residual are both `0.0`; the staggered inverse residual is below the runner
tolerance at `1.02811195848043e-15`.  The intermediate state is therefore
outside the local image, while the complete reversible staggered macrostep
closes exactly.

The co-moving and staggered macrosteps are both tested on an anisotropic
colocated/separated sparse state under all 24 proper-cubic frames. Their common
maximum covariance residual is

```text
2.092290251208289e-16.
```

This covariance test concerns the completed macrostep.  It does not turn the
two compiler substeps into physical time or supply a multiparticle collision
schedule.

## Mass, contact, and semantic scope

Both sides use the same Cycle-219 matter coin, so the interface preserves the
bare one-particle fixture:

```text
analytic mass     0.4534056541748852
dispersion mass   0.4534056690336209.
```

The coupling and phase-to-mass normalization remain supplied.  No dressed
mass is computed.  The algebraic contact fixture is one for matter number zero
and one and has phase `exp(i0.37)` at number two, but the contact fixture is not
applied in this one-matter runner.

The conserved object remains an internal excitation/field-number charge.  It
is not energy, work, stress, a rate, gravity, a gravitational source, a clock,
a Record, an occurrence rule, or a Born/probability law.

## Supplied structure

The load-bearing supplied structure is:

1. the site-reservoir and carried seven-state basis identifications;
2. the local minus sign in `J_d`;
3. the one-matter, one-total-excitation sparse domain;
4. the Cycle-219 matter coin, Cycle-214/215 field coin, and their streams;
5. `beta=-0.3`, `theta=0.8m`, and the vertex sign conventions;
6. the explicit reservoir-position tag used for the comparison;
7. the co-moving reservoir permutation;
8. the matter-stream-then-conditional-transposition staggered schedule;
9. infinite cubic geometry and all initial-state choices.

Derived here are the exact local isometry/intertwiners, tagged fixed-stream
residual, repaired full-step equality, catch-up involution, co-moving four-tick
inversion, staggered one-step inversion, proper-cubic covariance, and deletion
controls.

Not earned are a Cycle-269 physical state encoder, full-Fock CAR transport,
several-matter collision law, prepared multiparticle sector, dressed mass,
physical contact scattering, energy/stress/source identification, clock,
metric response, occurrence, Record, Born law, or empirical calibration.

## Disposition and ledger effect

```text
local seven-state vertex interface:       PASS exactly
onsite coin and frame interface:           PASS exactly
fixed-reservoir full stream:               MISMATCH, exact tagged residual
co-moving repair:                          PASS exactly on declared domain
staggered catch-up repair:                 PASS as a reversible completed macrostep
Cycle-269 physical state compiler:         NOT CONSTRUCTED
shared obstruction or axiom pressure:      NONE
```

The defensible dependency-ledger movement is route-specific:

- `C_source`: improves because the formerly separate carried and site-local
  source blocks now have an exact local dictionary and two explicit stream
  repairs;
- `C_local`: improves on the declared one-matter logical domain, but the
  Cycle-269 physical compilation of either repaired stream remains open;
- `C_int`: unchanged beyond the already supplied reversible local vertex;
- `C_ref`, `C_num`, and `C_wrap`: unchanged.

No 0–5 framework maturity score should change from this interface probe.  It
constructs a local dictionary and candidate stream laws; it does not add a
common physical CAR compiler, gravity/source equation, clock, dressed inertia,
Record, or Born rule.

In particular, the conserved ledger used by the runner is not gravity and is
not identified with energy or a physical source equation.

The highest-value next test is a physical implementation of the staggered
catch-up on mapped Cycle-269 matter-direction controls, including edge
collisions and same-code contact, while retaining the exact macrostep
intertwiner.

## Verification

```text
python3 -m py_compile \
  scripts/carried_site_reservoir_interface_mapping_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/carried_site_reservoir_interface_mapping_2026_07_17.py
```
