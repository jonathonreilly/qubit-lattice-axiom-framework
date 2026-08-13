---
claim_id: admissibility_six_star_is_not_a_four_link_plaquette_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "At the origin of Z^3 the Admissibility nearest-neighbor condition is the six-site star S={±e1,±e2,±e3}. A unit square in the z=0 plane has four links L. |S|=6≠4=|L|, so there is no bijection of neighbor sites to plaquette links. A function of the six neighbor possibilities is not a function of four link angles without an extra site-versus-edge pairing. The pairing is displayed and is not adopted. The statement is a cardinality/type split of the axiom stencil versus one plaquette. It is not a 16-atom site-product comparison, not a holonomy axiom, and not the June 10 ln Z_L object."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_six_star_is_not_a_four_link_plaquette_2026_08_13.py
---

# Admissibility six-star is not a four-link plaquette

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** one origin in `Z^3`; the six nearest-neighbor sites versus the four
links of one unit square.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_six_star_is_not_a_four_link_plaquette_2026_08_13.py`](../scripts/admissibility_six_star_is_not_a_four_link_plaquette_2026_08_13.py)
**Parents:** the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

At the origin of `Z^3` the nearest-neighbor star is a set of six *sites*. A
unit plaquette in the plane `z=0` is a set of four *edges*. Those two finite
sets have different cardinalities and different types. There is therefore no
bijection of neighbor sites to plaquette links.

The current Lattice and Admissibility sentences name nearest-neighbor
adjacency of sites and a distribution determined by nearest-neighbor
conditions. Neither sentence names a four-link holonomy.

A function of the six neighbor possibilities is not a function of four link
angles unless an extra pairing of site type to edge type is supplied. That
pairing is displayed below. It is extra. Do not adopt a holonomy axiom.

This is a cardinality and type split of the axiom's local stencil versus one
square. It is not a comparison of a 16-atom site-bit product to a holonomy
`H`. The plaquette count of this one square is `N_p=1`, which is not `96`.
This is not the June 10 `\ln Z_L` object. Do not import `0.5934`. Do not
adopt `L_phys`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 6-versus-4 cardinality split and the site-versus-edge type split are exact on declared finite sets. No holonomy axiom is adopted. No June 10 partition function is imported."
trace_class: negative_route_pruning
target_claim_id: admissibility_local_stencil_versus_plaquette
target_blocker_text: "keep the axiom local condition as a six-site nearest-neighbor star and do not identify it with a four-link plaquette"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for one origin and one unit square; no holonomy law is derived"
hypothetical_axiom_status: "no axiom edit, adoption, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e1=(1,0,0)`, `e2=(0,1,0)`, `e3=(0,0,1)` in `Z^3`. The origin is
`0=(0,0,0)`.

The nearest-neighbor star at the origin is the set of *sites*

`S = {±e1, ±e2, ±e3}`.

These six points are the Lattice nearest neighbors of `0`. Each has graph
distance `1` from the origin. The origin itself is not a member of `S`. The
edge-diagonal site `e1+e2` is not a member of `S`.

A unit plaquette in the plane `z=0` has oriented links

```text
L = {(0, e1), (e1, e1+e2), (e1+e2, e2), (e2, 0)}.
```

These four objects are *edges*: ordered pairs of sites. The integer
`star_size` is `|S|`. The integer `plaquette_link_count` is `|L|`. Both
counts are exact integers.

A neighbor-condition 6-tuple is a map from `S` to a local possibility domain.
A link-angle 4-tuple is a map from `L` to an angle label. Those two maps have
different domains.

An extra pairing of types is any assignment that sends members of `L` to
members of `S` (or the reverse) in order to pretend the two domains coincide.
One such assignment is displayed in Theorem 3. It is not a bijection and it
is not axiom content.

The plaquette count of this one square is the integer `N_p=1`.

## Theorem 1 — Cardinalities Differ; There Is No Bijection

`|S|=6` and `|L|=4`, so

`|S|=6 ≠ 4=|L|`.

There is no bijection of neighbor sites to plaquette links. A finite set of
six elements is not in bijection with a finite set of four elements.

The same obstruction is already visible in the supports. The star contains
`-e1`, `-e2`, and `±e3`, none of which is a vertex of this square. The square
contains the origin and the edge-diagonal `e1+e2`, neither of which is a
member of `S`.

## Theorem 2 — The Axiom Sentences Name A Site Star, Not A Four-Link Holonomy

Quote Lattice
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)):

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic
> rotations about each site.

Quote Admissibility from the same memo:

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

The Lattice sentence names nearest-neighbor adjacency of *sites*. The
Admissibility sentence names a distribution at a site determined by
nearest-neighbor *conditions*: the 6-tuple of neighboring possibilities on
`S`. Neither sentence names a four-link holonomy, a link 1-form, or an angle
sum around `L`.

## Theorem 3 — A 6-Tuple Function Is Not A 4-Angle Function Without Extra Pairing

A function of the six neighbor possibilities is a function of a 6-tuple
indexed by sites. A function of four link angles is a function of a 4-tuple
indexed by edges. Those are different types.

Without an extra pairing of types (sites versus edges), a map on `S` is not a
map on `L`. Cardinality already forbids a bijection. Type forbids even a
type-preserving identification: a site is a point of `Z^3`; a link is an
ordered pair of points.

Display one extra pairing; do not adopt it. Enumerate the four links against
the first four star sites in the order `(e1,-e1,e2,-e2,e3,-e3)`:

```text
(0, e1)        ⟷  e1
(e1, e1+e2)    ⟷ -e1
(e1+e2, e2)    ⟷  e2
(e2, 0)        ⟷ -e2
unused star sites: e3, -e3
```

This pairing leaves two star sites unpaired, sends edges to sites, and is
therefore not a bijection of equal types. Any later encoding that would turn
the leftover site possibilities into link angles is a further extra. Do not
adopt a holonomy axiom.

## Theorem 4 — Cardinality/Type Split Of The Local Stencil, Not A 16-Atom Product

This result compares the axiom's local six-site stencil to one four-link
plaquette. It is not a comparison of a 16-atom product of one-site bits on
the four plaquette vertices to a holonomy `H`. Those are different finite
objects: a 16-row site-bit table versus the six-versus-four stencil count
proved here.

Do not adopt `L_phys`. Do not adopt a holonomy axiom. The axioms already name
the six-site nearest-neighbor condition. This note does not add a link-angle
law.

## Theorem 5 — One Square Has `N_p=1`, Not `96`

The plaquette count of this one square is `N_p=1`. That integer is not `96`.
The count `96` belongs to a different object (the June 10 `\ln Z_L` listing
for a larger lattice). This note does not use that listing as a lemma and
does not import its numerical constant.

Not June 10 `\ln Z_L`. Do not import `0.5934`.

### N5 — rhetoric and resolution audit (Theorem 5)

"`N_p=1`" resolves only the number of squares declared in the object `L`
above. It does not resolve a four-dimensional plaquette inventory, a
partition function, or a continuum coupling. A reader who replaces `1` by
`96`, or who imports `0.5934`, is reading a different object than the one
proved.

## Consequence For The Axiom Surface

No axiom is edited. The current memo already names nearest-neighbor adjacency
of sites and a distribution determined by nearest-neighbor conditions. Those
clauses make the local stencil the six-site star `S`. Identifying that
stencil with the four-link set `L` requires an extra pairing of types. The
pairing is displayed and is not adopted.

The predicate `|S|=|L|` is false: `6 ≠ 4`.

## What This Does Not Claim

- It does not adopt a holonomy axiom or a link 1-form.
- It does not adopt `L_phys`.
- It does not identify a 16-atom site-bit product with a holonomy `H`.
- It does not import June 10 `\ln Z_L` or `0.5934`.
- It does not cite any unmerged pull request.

The safe downstream use is only the split: the axiom local condition is the
six-site star, and one unit square is a four-edge set of a different type.

## Reproduction

```bash
python3 -B scripts/admissibility_six_star_is_not_a_four_link_plaquette_2026_08_13.py
```

Audit status remains the independent audit lane's responsibility.
