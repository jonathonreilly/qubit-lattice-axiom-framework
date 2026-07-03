# eta UD2 Fixed-Token Square Homology Certificate

Date: 2026-06-06

Status: exact-support

actual_current_surface_status: exact-support
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This artifact prunes the automatic-null-square shortcut in a scoped UD2 finite model; it does not identify the closed-PR detour swaps as the same braid class."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Summary

The eta base-flux block left one topology blocker open: a future theorem must
prove or cite the relevant `UD_2(Z^3)` homotopy bridge, or eta remains scoped to
base area flux.

This block supplies a narrow exact certificate on one finite `UD_2` model. Let
`G` be a connected finite subgraph of `Z^3` consisting of one unit square plus a
two-edge parking tail for a second token. Build the unordered two-token
cubical configuration complex `UD_2(G)`: cells are unordered pairs of disjoint
open cells of `G`.

The runner forms the cellular chain complex over `GF(2)` and checks the loop
where one token traverses the unit square while the other token is parked at
the tail endpoint. The loop is:

- a valid cellular `1`-cycle in `UD_2(G)`;
- not in the image of the cellular `boundary_2` map.

Therefore it is not null-homologous mod `2`. Since a null-homotopic loop is
null-homologous, the fixed-token unit-square loop is not null-homotopic in this
finite `UD_2` model.

## What This Prunes

This prunes the shortcut:

```text
one-token plaquette square in UD_2(Z^3) is automatically null-homotopic
```

At least in the explicit finite connected subgraph, the analogous fixed-token
loop is homologically nonzero. The graph-as-`1`-complex warning in the parent
eta base-flux block was real: a geometric square in the site graph is not a
filled `2`-cell unless a separate cubical/filling premise is added.

## What This Does Not Prove

This block does not prove the full closed-PR braid-invariant no-go. It does not
show that the compared detour swaps from closed PR #2207 are the same element
of `B_2(Z^3)`. It also does not classify the full graph braid group of `Z^3`.

The remaining possible positive route is now narrower:

```text
identify the actual compared detour swaps in UD_2(Z^3), then evaluate eta
holonomy on those classes.
```

If a future theorem identifies same-class detours with different eta area
holonomy, the parent eta area-flux theorem becomes the obstruction. This block
does not supply that identification.

## Runner

Runner:

```text
scripts/frontier_eta_ud2_fixed_token_square_homology_2026_06_06.py
```

Cache:

```text
logs/runner-cache/frontier_eta_ud2_fixed_token_square_homology_2026_06_06.txt
```

The runner checks:

- the base graph is connected and has one square cycle plus a parking tail;
- `UD_2(G)` has `0`, `1`, and `2` cells;
- the fixed-token square is a valid cellular `1`-cycle;
- `H_1(UD_2(G); GF(2))` is nonzero;
- the fixed-token square cycle is not in `im(boundary_2)`;
- the result prunes only the automatic-null-square shortcut.
