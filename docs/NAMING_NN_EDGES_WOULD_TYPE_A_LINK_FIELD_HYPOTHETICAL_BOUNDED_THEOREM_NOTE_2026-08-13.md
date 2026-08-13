---
claim_id: naming_nn_edges_would_type_a_link_field_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the unit cube, |V|=8 sites and |E|=12 nearest-neighbor edges. Current Lattice names sites of Z^3 with nearest-neighbor adjacency, so a map θ:E→{0,1} is an extra object. The displayed, unadopted counterfactual sentence S' names those edges as a set E; then θ has the same type as a site occupancy o:V→{0,1}. The integer 8≠12 survives. S' does not name a holonomy, a group, a Bianchi identity, L_phys, or gauge values. Formation occupancy, Newton B, and Born K are not dissolved. S' is displayed only; it is not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/naming_nn_edges_would_type_a_link_field_hypothetical_2026_08_13.py
---

# Naming Nearest-Neighbor Edges Would Type a Link Field (Hypothetical)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** finite unit-cube counting and type comparison under the current
Lattice sentence versus one displayed, unadopted retype of that sentence.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/naming_nn_edges_would_type_a_link_field_hypothetical_2026_08_13.py`](../scripts/naming_nn_edges_would_type_a_link_field_hypothetical_2026_08_13.py)
**Parents on origin/main:** the current axiom memo only,
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
**Friction-audit role:** addendum candidate C9. Hypothetical Lattice retype.
Not a holonomy law. Not `L_phys`.

## Result Up Front

On the unit cube the runner counts eight sites and twelve nearest-neighbor
edges. Those integers are unequal, so there is no bijection between sites and
edges. That inequality is not a missing connection axiom. It is a counting
fact about the 0-skeleton and the 1-skeleton of one cube.

The current Lattice sentence names physical sites as the points of `Z^3`
together with nearest-neighbor *adjacency*. Adjacency is a relation on the
named site set. It does not promote the related pairs to a named domain. A
map `θ:E→{0,1}` is therefore extra relative to the current sentence: its
domain is not an axiom-named set.

Display, and do not adopt, the counterfactual sentence `S'`:

> Physical sites are points of `Z^3`; nearest-neighbor *edges* are named
> objects (the adjacency relation is promoted to a set `E`).

Under `S'`, `θ` has the same type as a site occupancy `o:V→{0,1}`: both are
`{0,1}`-fields on a named set. The integer `8≠12` survives. The reading “a
connection cannot exist unless we add an axiom” is a reading of the current
sentence `S`, not of `8≠12`.

`S'` still does not name a holonomy, a group, or a Bianchi identity. Gauge
*values* remain extra. Only the *domain* of `θ` becomes axiom-typed. This
note does not adopt `S'` and does not adopt `L_phys`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Unit-cube cardinalities and the S versus S' typing of θ are proved on declared finite objects; S' is displayed and not adopted; holonomy, group, Bianchi, L_phys, and gauge values remain untyped."
trace_class: axiom_challenge_counterfactual
target_claim_id: naming_nn_edges_would_type_a_link_field
target_blocker_text: "decide whether a {0,1}-assignment on nearest-neighbor edges is extra or a field on a named 1-skeleton"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for |V|=8, |E|=12, and the type comparison under displayed S'; S' is not adopted"
hypothetical_axiom_status: "C9 counterfactual: Lattice names sites and NN edges; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on the unit cube in `Z^3`.

`V = {0,1}^3`

so `|V| = 8`. An edge is an unordered pair of sites that differ in exactly one
coordinate. There are twelve such pairs:

- four edges parallel to each of the three lattice axes.

Write `E` for that set, so `|E| = 12`. The identity gates are `vertex_count()`
and `edge_count()` in the primary runner; both values are counted from the
listed sets, not inserted as free constants.

A site occupancy is a map

`o : V → {0,1}`.

A link field is a map

`θ : E → {0,1}`.

Current Lattice sentence `S`, quoted from the axiom memo:

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic
> rotations about each site.

Counterfactual sentence `S'` (displayed, not adopted):

> Physical sites are points of `Z^3`; nearest-neighbor *edges* are named
> objects (the adjacency relation is promoted to a set `E`).

Both sentences name the same site set. On the unit cube both therefore give
`|V| = 8`. They disagree only about whether `E` is a named domain.

## Theorem 1 — Eight Sites Are Not Twelve Edges

The runner enumerates `V` and `E` and checks

`vertex_count() = 8`, `edge_count() = 12`, `8 ≠ 12`.

There is no bijection `V ↔ E`. The mutation predicate `|V| = |E|` fails. The
mutation predicate “`S` and `S'` disagree about `|V|`” also fails: both
sentences keep eight sites on this cube.

## Theorem 2 — Under `S` The Link Map Is Extra; Under `S'` It Is Typed

Under `S`, the named carrier is the site set. Nearest-neighbor adjacency is a
relation on that set. The pair set `E` is not a named domain, so a map
`θ:E→{0,1}` is extra: it requires a domain the current sentence does not
name.

Under `S'`, `E` is named. Then `θ` has the same type as occupancy `o:V→{0,1}`:
each is a `{0,1}`-field on a named set. The fields are still not the same
object, because their domains have different cardinalities. The integer
`8 ≠ 12` survives, and so do the unequal pattern counts `2^8 = 256` and
`2^12 = 4096`.

The TOE-wall reading “a connection cannot exist unless we add an axiom” is
therefore a reading of `S`, not a reading of the counting inequality. This
note records that reading. It does not adopt `S'`.

## Theorem 3 — `S'` Types The Domain, Not Gauge Values

`S'` names sites and nearest-neighbor edges. It does not name:

- a holonomy around a face or larger loop,
- a structure group or a connection-value group,
- a Bianchi identity,
- or `L_phys`.

Gauge *values* remain extra. Only the *domain* of `θ` becomes axiom-typed
under the counterfactual. Display `S'`. Do not adopt it. Do not adopt
`L_phys`.

## Theorem 4 — Formation, Newton, And Born Stay Undissolved

C9 does not dissolve formation occupancy `o`. Formation remains a
`{0,1}`-field on sites: Record still locks a possibility at a site, and
`o` is still indexed by `V`. Naming edges does not move formation onto `E`.

C9 does not dissolve Newton `B` or Born `K`. Those remain outside this
retype.

What C9 would change is only the type of a `{0,1}`-assignment on
nearest-neighbor edges. Constructions that presently treat a link-valued map
or a star-plaquette assignment as an extra object would, under displayed
`S'`, become fields on a named 1-skeleton. That is a domain retype, not a
holonomy law and not a value law.

## Exact Target And Obligation Graph

**Exact target.** On the unit cube, count `|V|` and `|E|`, compare the type of
`θ` under current `S` with its type under displayed `S'`, and record that
`S'` is not adopted.

| Obligation | Role | Disposition |
|---|---|---|
| count unit-cube sites | identity gate | `vertex_count()` returns 8 |
| count unit-cube NN edges | identity gate | `edge_count()` returns 12 |
| reject `|V| = |E|` | mutation | fails; `8 ≠ 12` |
| reject “`S` and `S'` disagree about `|V|`” | mutation | fails; both have 8 sites |
| type `θ` under `S` | extra-object test | domain `E` is unnamed |
| type `θ` under `S'` | counterfactual type | `{0,1}`-field on named `E` |
| keep holonomy, group, Bianchi extra | negative scope | `S'` does not name them |
| keep formation, Newton `B`, Born `K` | negative scope | not dissolved |
| adopt `S'` or `L_phys` | axiom edit | not performed |

## What This Note Does Not Claim

- It does not edit the Lattice axiom or any other axiom.
- It does not adopt a connection axiom, `S'`, or `L_phys`.
- It does not compute a holonomy, impose a structure group, or prove a
  Bianchi identity.
- It does not identify `θ` with a physical gauge field or with Wilson
  plaquettes.
- It does not dissolve formation occupancy, Newton `B`, or Born `K`.
- It does not claim four-dimensional `SU(3)`.
- It does not cite unmerged companion constructions as parents.

Independent audit remains required. No canonical axiom edit is proposed.
