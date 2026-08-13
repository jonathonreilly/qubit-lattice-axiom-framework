---
claim_id: cube_has_eight_vertices_and_twelve_edges_occupancy_is_not_connection_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the unit cube the 0-skeleton has eight vertices and the 1-skeleton has twelve edges. Site occupancy is a map on vertices; a binary link field is a map on edges. These objects have unequal domains and unequal configuration counts, so occupancy is not a connection. The note displays a link field and does not add a connection axiom. It is not a holonomy computation and is not Bianchi."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_has_eight_vertices_and_twelve_edges_occupancy_is_not_connection_2026_08_13.py
---

# Cube Has Eight Vertices And Twelve Edges; Occupancy Is Not A Connection

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact 0-skeleton versus 1-skeleton counting on the unit cube
`{0,1}^3`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_has_eight_vertices_and_twelve_edges_occupancy_is_not_connection_2026_08_13.py`](../scripts/cube_has_eight_vertices_and_twelve_edges_occupancy_is_not_connection_2026_08_13.py)
**Parent:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The unit cube has eight vertices and twelve edges. Those two finite sets are
not in bijection. A site occupancy is an eight-bit map on vertices. A binary
link field is a twelve-bit map on edges. Those two configuration sets are
unequal. Occupancy therefore is not a connection.

The extra object that would carry a gauge field on this cube is a map on
edges. This note displays that map. It does not add a connection axiom. The
counting is not a holonomy computation and is not Bianchi.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite counts |V|=8 and |E|=12, with 2^8 occupancy patterns and 2^12 link fields, are identities of the unit-cube 0-skeleton and 1-skeleton. No dynamics, holonomy, or gauge axiom is derived."
trace_class: negative_route_pruning
target_claim_id: occupancy_is_not_connection
target_blocker_text: "identify site occupancy with a connection or other edge-supported gauge field"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for unit-cube vertex/edge cardinalities and binary configuration counts; physical gauge dynamics remain open"
hypothetical_axiom_status: "no edit, addition, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the unit cube be the product `{0,1}^3`. Write

`V = {0,1}^3`

for its vertices. Then `|V| = 8`. An edge is an unordered pair of vertices
that differ in exactly one coordinate. Write `E` for the set of all such
pairs. Then `|E| = 12`.

A **site occupancy** is a map

`o : V -> {0,1}`.

There are `2^8 = 256` occupancy patterns.

A **link field** is a map

`θ : E -> {0,1}`.

There are `2^12 = 4096` link fields. The symbol `θ` is displayed as that
edge-supported map and is not promoted to an axiom.

The 0-skeleton is the set `V`. The 1-skeleton is the graph `(V,E)`. Occupancy
is a 0-cochain with values in `{0,1}`. A connection, in the narrow sense used
here, is a 1-cochain: a field assigned to edges.

## Canonical Parent Wording

The only parent is the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

**Lattice.** Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency, standard translations, and proper cubic rotations
about each site.

**Record.** When present, a record locks exactly one admissible local
possibility. A site never carries more than one record; records are
permanent. The interpretive reading in the same memo states that a forming
record locks a possibility at a site.

Occupancy is therefore a site-supported object: its domain is `V`. A
connection is edge-supported: its domain is `E`. Lattice names sites and
nearest-neighbor adjacency; it does not identify a site value with a
nearest-neighbor value. Record locks a possibility at a site; it does not
lock a value on an edge.

## Theorem 1 — No Bijection Between Vertices And Edges

`|V| = 8` and `|E| = 12`. These integers are unequal, so there is no
bijection `V ↔ E`.

Every vertex has degree three: the three coordinates each flip independently.
Handshaking then gives

`2 |E| = sum_{v in V} deg(v) = 8 * 3 = 24`,

hence `|E| = 12`. The same count is the number of unordered pairs that differ
in exactly one coordinate: three axis directions and four edges per
direction.

Because the domains have different cardinality, no identification of a
vertex-supported assignment with an edge-supported assignment can be a
bijection of the underlying sets.

## Theorem 2 — Occupancy Patterns Are Not Link Fields

The set of occupancies is `{0,1}^V`. Its cardinality is

`2^{|V|} = 2^8 = 256`.

The set of binary link fields is `{0,1}^E`. Its cardinality is

`2^{|E|} = 2^{12} = 4096`.

These finite sets are unequal. In particular there is no bijection between
occupancy patterns and binary link fields. An eight-bit site pattern is not
a twelve-bit edge pattern.

## Theorem 3 — Occupancy Lives On Sites; A Connection Lives On Edges

Lattice supplies sites of `Z^3` and nearest-neighbor adjacency. Record locks
a possibility at a site. Occupancy is a function of those sites: `o` is
defined on `V`.

A connection, as an extra object for a gauge field on this cube, is a function
of the nearest-neighbor pairs: `θ` is defined on `E`.

The two objects are typed by different skeletons. The extra object for a
gauge field is a map on edges. Nearest-neighbor adjacency names which pairs
may carry that map; it does not fill the map from occupancy.

## Theorem 4 — Display The Link Field; Add No Connection Axiom

The map `θ : E -> {0,1}` is displayed so that the 1-skeleton object is
explicit. This note does not add a connection axiom. The displayed field is
not a holonomy. The counting is not a holonomy computation and is not
Bianchi. Face products, cube identities, and parallel transport are outside
the present 0-skeleton versus 1-skeleton block.

## Theorem 5 — No Imported Continuum Gauge Number And No Four-Dimensional Claim

This note does not import a continuum gauge coupling and does not claim
four-dimensional `SU(3)`. The only numbers used as identities are

`|V| = 8`, `|E| = 12`, `2^8 = 256`, `2^{12} = 4096`.

## Mutation And Identity Gates

The identity gates of the companion runner call `vertex_count()` and
`edge_count()`. Those functions return `|V|` and `|E|` by enumerating `V` and
`E`. The predicate `|V| = |E|` fails because `8 ≠ 12`.

## What This Note Does Not Do

- It does not identify occupancy with a connection.
- It does not add a connection axiom.
- It does not compute holonomy or Bianchi identities.
- It does not claim four-dimensional `SU(3)`.
- It does not edit the axiom memo.

The live remainder is any later derivation that *constructs* an edge map from
other retained structure. Such a construction would still have to produce a
twelve-bit object, not relabel the eight-bit occupancy.
