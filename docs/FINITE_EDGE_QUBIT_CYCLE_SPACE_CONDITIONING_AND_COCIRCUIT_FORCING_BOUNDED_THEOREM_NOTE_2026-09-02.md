---
claim_id: finite_edge_qubit_cycle_space_conditioning_and_cocircuit_forcing_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "For the explicitly listed open cube, 3x3 grid, and 3x3 grid with one pendant edge only: even vertex parity selects the graph cycle space; its uniform finite measure has coordinate marginals in {0,1/2,1}; an observed edge set forces a target edge exactly when it contains the non-target support of a cocircuit through that target; coordinate-projector conditioning is order-independent; and the complete two-observation cube census has 96 adjacent cases that force one further edge and 168 disjoint cases that force none."
upstream_dependencies: []
runner: scripts/finite_edge_qubit_cycle_space_conditioning_and_cocircuit_forcing_check_2026_09_02.py
---

# Finite edge-qubit cycle spaces: conditioning and cocircuit forcing

**Date:** 2026-09-02

**Type:** bounded_theorem

**Status:** proposed_retained

**Audit:** unset; the independent audit lane owns any verdict.

**Primary runner:**
[finite_edge_qubit_cycle_space_conditioning_and_cocircuit_forcing_check_2026_09_02.py](../scripts/finite_edge_qubit_cycle_space_conditioning_and_cocircuit_forcing_check_2026_09_02.py)

**Runner cache:**
[finite_edge_qubit_cycle_space_conditioning_and_cocircuit_forcing_check_2026_09_02.txt](../logs/runner-cache/finite_edge_qubit_cycle_space_conditioning_and_cocircuit_forcing_check_2026_09_02.txt)

## Boundary

This note is a finite theorem about three declared graphs and a binary variable
on each edge. It does not identify those variables with physical fermions,
framework Record objects, lattice sites, an admissibility law, or any object supplied by the
framework axioms. It makes no formation-law, locality, spectral, or
selection-rule claim. In particular, a forcing set need not be local: the
cocircuit characterization below includes wider graph cuts.

There are no imported scientific values or load-bearing scientific sources.
All graph definitions and all finite checks are contained in the runner.

## Definitions

For a finite connected graph `G=(V,E)`, write an edge assignment as
`x in F_2^E`. The allowed set in this note is

```text
C(G) = {x : sum_{e incident to v} x_e = 0 mod 2 for every v in V}.
```

Thus `C(G)` is the graph cycle space. The state used below is simply the
uniform finite measure on `C(G)`. Observing `(e,b)` means restricting that
finite set to assignments with `x_e=b` and renormalizing when the restricted
set is nonempty.

The cut space `C(G)^perp` is computed explicitly. A cocircuit is an
inclusion-minimal nonzero cut-space word. For a target edge `q`, an observed
edge set `S subset E\{q}` forces `q` when every pair of allowed assignments
that agrees on `S` also agrees at `q`.

The fixtures are:

- the open `2x2x2` cube graph (`|V|=8`, `|E|=12`);
- the open `3x3` square grid (`|V|=9`, `|E|=12`);
- that grid with one pendant edge from vertex `0` to a new vertex `9`
  (`|V|=10`, `|E|=13`).

## Results

### T1. Cycle-space support and face generators

For the cube, grid, and pendant-grid fixtures respectively,

```text
dim C(G) = 5, 4, 4,
|C(G)|   = 32, 16, 16.
```

The declared elementary face boundaries have ranks `5,4,4` and span the full
cycle space in each fixture. These equal `|E|-|V|+1`, as expected for the
three connected graphs. The runner independently enumerates every edge word,
tests every vertex parity, computes both ranks over `F_2`, and compares the
two finite sets.

### T2. Exact finite marginals

Under the uniform measure on `C(G)`, every edge marginal is exactly one of
`0`, `1/2`, or `1`. On the cube and plain grid every edge has marginal `1/2`.
On the pendant grid the pendant edge is fixed to `0`, while each other edge
has marginal `1/2`.

### T3. Complete two-observation cube census

Conditioning on one cube edge leaves every other cube-edge marginal at
`1/2`. Over all `66` unordered pairs of distinct cube edges and all four
binary value assignments, there are exactly:

```text
96  adjacent-edge cases: one further edge becomes forced;
168 disjoint-edge cases: no further edge becomes forced.
```

This is only a two-observation statement on the cube. It is not a general
neighbourhood-only locality rule.

### T4. Cocircuit forcing characterization on all three fixtures

For every target edge `q` and every subset `S` of the remaining edges, `S`
forces `q` if and only if there is a cocircuit `h` with

```text
h_q = 1,  support(h) \ {q} subset S.
```

The runner verifies both sides independently for every one of the `102,400`
target/observed-set masks: the left side by searching the enumerated cycle
space for a difference word invisible on `S` but nonzero at `q`, and the right
side by enumerating the inclusion-minimal nonzero cut-space words. The
cocircuit counts are `63`, `53`, and `54` for the cube, grid, and pendant grid.

A deliberately nonlocal cube regression is included. Observing the three
mutually disjoint edges

```text
(1,5), (2,6), (3,7)
```

forces the target `(0,4)` for all eight assignments of the three observed
values. Four allowed cycle-space words remain in each case. This is the
constant-coordinate face cut and demonstrates why T3 cannot be promoted to a
general local-star rule.

### T5. Order-independent coordinate conditioning

Coordinate observations are commuting diagonal projectors. Consequently two
successive observations restrict to the same intersection in either order.
The runner checks the exact final finite set and exact rational joint
probability for all `264`, `264`, and `312` edge-pair/value cases in the three
fixtures. No random or floating-point evidence is used.

## Evidence and falsifiers

Every result is finite and exact. The runner uses integer bit masks, `F_2`
elimination, set equality, and `fractions.Fraction`. It contains explicit
falsifiers showing that each of the following mutations is rejected:

- corrupting a face generator;
- removing an allowed support word;
- replacing an exact marginal by `1/3`;
- corrupting the plain-grid marginal profile by inserting a spurious `0`;
- omitting a needed cocircuit;
- replacing sequential intersection by a last-observation-only update;
- restricting the forcing prediction to local vertex stars.

The paired cache records the direct runner output and the runner SHA-256. A
green cache is execution evidence for these finite claims only; it is not an
audit verdict.

## What does not move

This source note changes no axiom, primitive, physical dictionary, audit
status, effective status, or framework rule. Its path-derived claim remains
unaudited until the independent audit lane acts after landing.
