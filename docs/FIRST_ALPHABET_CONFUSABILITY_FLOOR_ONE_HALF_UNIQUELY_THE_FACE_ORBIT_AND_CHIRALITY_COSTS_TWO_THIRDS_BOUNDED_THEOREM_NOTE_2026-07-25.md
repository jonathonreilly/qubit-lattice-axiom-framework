# The First Availability Set Has Confusability Floor 1/2, Attained Only by the Face Orbit, While Every Chiral Alternative Costs at Least 2/3 — the Two Sides of the Free-Orbit Residual Are No Longer Symmetric (Bounded Theorem)

**Date:** 2026-07-25
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact orbit classification and exact rational
overlap arithmetic; general proofs with a finite scan as witness; the
minimality premise is named and **not** adopted).
**Status authority:** none. Audit: unset. Constitutional effect: none. This
note edits no axiom, foundation, Qualification, primitive, registry, policy,
queue, audit-status, or PR-control surface. **It introduces no axiom and no
primitive, adopts no formation rule, and does not settle which side the fixed
rule's `A0` sits on.**
**Primary runner:**
[`scripts/physical_first_alphabet_confusability_floor_cycle705_2026_07_25.py`](../scripts/physical_first_alphabet_confusability_floor_cycle705_2026_07_25.py)
(9 PASS / 0 FAIL, exit 0; exact rational arithmetic, no sampling, no floating
point, no repository imports).

## The residual this addresses

The landed bootstrap continuation closes with a named residual:

> "**The free off-mirror part of `A0`**: the locus-class question is now
> exactly this — any derivation showing the all-open availability set avoids
> unpaired free off-mirror orbits (or must contain them) settles the
> realized-alphabet bootstrap. The safe/dangerous split is fully classified;
> what remains is **which side the fixed rule's `A0` sits on**."
> — [`BOOTSTRAP_CONTINUATION_..._2026-07-04`](BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md),
> Residual 1

Before this note the two sides were **symmetric**: the axioms supply proper
covariance only, so nothing in the framework preferred an achiral `A0` to a
chiral one. This note does not break that symmetry by adding a premise. It
shows the two sides are **already** separated by a functional the framework
already carries, and computes the separation exactly.

It does not settle the residual. It re-prices it.

## Answer

Write `A0` for the first availability set: nonempty (landed Theorem 1, from
"Records form.") and proper-cubic-invariant as a set of contents (landed
Theorem 1 of the empty-state bootstrap). Contents are polar vectors on the
content sphere — the landed coupled-action model, carried here as a **named
model, not as axiom content** (see Scope).

For two contents of equal length the Qubit clause supplies a state overlap
with no freedom in it. In `Cl(3,0)`, a unit vector `v` satisfies `v^2 = 1`, so
`P_v = (1 + v)/2` is idempotent, and

```text
Tr(P_v P_w) = (1 + v . w) / 2.
```

This is forced by the algebra, not chosen: it is **not a normalization
convention**, and it imports no dimensionless number. Define

```text
conf(A) = max over distinct pairs v, w in A of Tr(P_v P_w),
```

the largest overlap between two contents the same first record could lock —
the extent to which the lawful alphabet is not self-distinguishing.

**Theorem 1 (orbit sizes).** Proper-cubic orbits on the content sphere have
sizes exactly `{6, 8, 12, 24}`, and the size-6 orbit is unique: the face orbit
`<100> = {±e1, ±e2, ±e3}`.

**Theorem 2 (the quarter-turn identity).** For the three 90-degree rotations
`R_x, R_y, R_z` about the coordinate axes,

```text
v . R_x v = v_x^2,   v . R_y v = v_y^2,   v . R_z v = v_z^2,
```

so the three inner products sum to `|v|^2`. Moreover `R_a v = v` holds exactly
when `v` lies on axis `a`.

**Theorem 3 (floor, and a unique saturator).** `conf(A0) >= 1/2` for every
nonempty proper-cubic-invariant `A0` on the content sphere, and **equality
holds only for the face orbit**. The named mirror-locus values are exact:

| orbit | size | conf | achiral |
|---|---:|---:|---|
| face `<100>` | 6 | **1/2** | yes |
| corner `<111>` | 8 | 2/3 | yes |
| edge `<110>` | 12 | 3/4 | yes |
| any size-24 orbit | 24 | `>= 2/3` | chiral or not |

**Theorem 4 (chirality costs).** Every orbit other than the face orbit has
`conf >= 2/3`. Since set-level chirality requires an unpaired free
off-mirror orbit (landed Theorem 2), which has 24 elements, **every chiral
`A0` has `conf >= 2/3 > 1/2`.** No chiral `A0` is confusability-minimal.

**Theorem 5 (distinguishable capacity).** Mutually distinguishable contents
are pairwise antipodal Bloch vectors, so **at most two** contents of any `A0`
are mutually distinguishable, while `|A0| >= 6`. A **chiral** `A0` built on a
single unpaired free orbit contains **no** antipodal pair, hence **no two
perfectly distinguishable contents at all**.

## Why this bears on the residual

The residual asked for a derivation picking a side. This note does not supply
one. What it supplies is that the sides are no longer interchangeable:

- the achiral option can be as good as `1/2`, and exactly one set achieves it;
- every chiral option is at least `2/3`, strictly worse;
- the achiral optimum is the three Pauli bases, `{±e1, ±e2, ±e3}` — the
  minimal lawful alphabet is exactly an orthogonal frame and its antipodes;
- a chiral alphabet is not merely worse on a scalar: it contains no
  perfectly distinguishable pair whatsoever (Theorem 5).

**The premise that would settle it, named and not adopted.** If the fixed
rule's `A0` minimizes `conf` — equivalently, if `conf(A0) < 2/3` — then `A0`
is the face orbit and is **achiral**, settling Residual 1 on the safe side.
That antecedent is an **import**: nothing in the four axioms says the rule
optimizes anything, and this note does **not** adopt it, does not propose
adopting it, and awards it no status. It is recorded so that the cost of
settling the residual is now one explicitly stated sentence rather than an
open-ended search.

## Proofs

**Theorem 1.** By orbit-stabilizer, `|orbit| * |stabilizer| = 24`. A point of
the sphere fixed by a nontrivial rotation lies on that rotation's axis, and a
point fixed by rotations about two distinct axes would be fixed by the
(infinite) group they generate — impossible. So every stabilizer is the cyclic
group of the single axis through the point: orders `1, 2, 3, 4` for generic,
2-fold, 3-fold and 4-fold axes respectively. `O` has no 6-fold axis, so no
stabilizer of order 6 or 12 arises, and the sizes are `24, 12, 8, 6`. Size 6
requires an order-4 stabilizer, i.e. a 4-fold axis, i.e. a face direction; all
six face directions lie in one orbit. Runner rows C1, C2 verify the group and
re-earn orbit-stabilizer exactly on the scan; the scan is a **witness**, and
the argument above is the proof.

**Theorem 2.** `R_z: (x,y,z) -> (-y,x,z)`, so `v . R_z v = -xy + yx + z^2 =
z^2`, and cyclically. The sum is `x^2 + y^2 + z^2 = |v|^2`. `R_a` fixes `v`
exactly on its axis, since a 90-degree rotation has no other fixed points on
the sphere. Runner row C5 verifies both statements exactly on 290 directions.

**Theorem 3 and 4.** Let `v` be a content that is **not** a face direction.
Then all three quarter-turns move `v`, so each `(v, R_a v)` is a **distinct**
pair inside the orbit. By Theorem 2 the three values `v_a^2` sum to `|v|^2`,
so `max_a v_a^2 >= |v|^2 / 3`, giving a distinct pair with
`cos >= 1/3` and hence `conf >= (1 + 1/3)/2 = 2/3`. If instead `v` **is** a
face direction, the only large term is the one belonging to the quarter-turn
that fixes `v` — which is not a distinct pair — and the remaining two vanish;
the face orbit's actual maximum is over the perpendicular pairs, `cos = 0`,
giving exactly `1/2`. So the face orbit is the unique orbit below `2/3`, and
its value is `1/2`.

For a general `A0`, which is a union of orbits: `conf` is a maximum over
pairs, hence monotone under adding points, so `conf(A0) >= conf(o)` for any
orbit `o` contained in `A0`. If `A0` is not exactly the face orbit it contains
some non-face orbit and `conf(A0) >= 2/3`. **This monotonicity step is
elementary and is not machine-checked**; the runner instead checks the
exactly-computable part — unions inside a single shell, where cross-orbit
overlaps are rational (row C6, one such union exists within the scan, at
`|v|^2 = 9`). Theorem 4 then follows from the landed reduction of set-level
chirality to unpaired free off-mirror orbits, which have size 24. Rows C4,
C6, C7.

**Theorem 5.** Two qubit states are perfectly distinguishable iff orthogonal
iff their Bloch vectors are antipodal (landed usage,
[`READOUT_BRIDGE_..._2026-07-06`](READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md):
"orthogonal rank-1 projections in `M_2` are antipodal Bloch pairs"). Three
pairwise-antipodal vectors would force two of them equal, so the cap is 2.
A chiral orbit excludes its own inversion image, so it contains no antipodal
pair and the cap drops to 1. Row C8 verifies the cap by direct search over
triples, so the cap is checked and not assumed.

## Controls

Row C9 isolates what is load-bearing. Two sets **beat** the floor — an
antipodal pair (`conf = 0`) and the four tetrahedral directions
(`conf = 1/3`) — and both are smaller than the minimum orbit size, so neither
can be cubic-invariant; the tetrahedron is a non-invariant half of the corner
orbit. A third set **ties** the floor: a rotated orthogonal frame also reaches
exactly `1/2` while not being cubic-invariant. That last control is reported
because it bounds the claim — **the number `1/2` is not itself special to
invariance**; what invariance forces is that the only invariant set reaching
it is the face orbit, in the cubic frame. Row C3 rejects a wrong overlap
formula, and verifies that `P_a` is idempotent exactly when `a` is a unit
vector rather than assuming it.

Two errors were found by the runner's own guards during construction and are
recorded here rather than silently fixed: an earlier C9 used a
different-length representative set, and an earlier C6 union check compared
orbits at different radii and was therefore computing a meaningless overlap
while passing. Both were caught by an equal-length assertion added to the
overlap function, which is retained.

## Scope

- **The content model is a named model, not axiom content.** That contents
  transform as polar vectors under the coupled cubic action is carried from
  the landed empty-state bootstrap as a named model. If contents are not that,
  the orbit arithmetic does not apply. This is the largest scope limit here.
- **The state reading is landed usage, not re-derived.** That a content's
  state is the rank-one projector along its polar vector is the identification
  already used on `main`; it is load-bearing for the word "confusability" and
  is cited, not proved.
- Contents are taken on the content sphere, so the cubic-fixed point `v = 0`
  is excluded by construction. The axioms do not by themselves exclude it, and
  nothing here argues that they do.
- Representatives of unequal length are outside the exact arithmetic; the
  cross-shell union case is settled by monotonicity, not by computation.
- The general statements are proved above; the scan (primitive integer
  directions with components in `[-3, 3]`, 290 directions, 14 orbits, 2 of
  them chiral) is a witness.
- **No formation rule is supplied**: no site selection, no possibility
  selection, no weight, no rate. Which element of `A0` a first record locks
  remains downstream, exactly as the axioms leave it.
- No lane, row, or obligation status is changed, and no N1–N8 verdict is
  awarded.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the Qubit
`Cl(3,0)` clause, the Admissibility covariance sentence, and "Records form."
The residual and the reduction of chirality to unpaired free off-mirror orbits
are from
[`BOOTSTRAP_CONTINUATION_..._2026-07-04`](BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md);
the nonemptiness and proper-invariance of `A0`, the orbit dichotomy, and the
content-sphere model are from
[`EMPTY_STATE_BOOTSTRAP_..._2026-07-04`](EMPTY_STATE_BOOTSTRAP_ALL_OPEN_AVAILABILITY_ORBIT_DICHOTOMY_DEGREE_NINE_CHIRALITY_WALL_BOUNDED_THEOREM_NOTE_2026-07-04.md).
The Bloch-antipodal distinguishability reading is landed usage in
[`READOUT_BRIDGE_..._2026-07-06`](READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md).
All pieces the runner needs are re-earned inside it.
