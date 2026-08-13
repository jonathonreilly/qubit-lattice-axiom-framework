---
claim_id: lattice_green_on_z3_is_not_continuum_one_over_r_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the cube {-2..2}^3 of Z^3 the graph reciprocal 1/d is not nn-harmonic at e1, so G_cont∘d is not a lattice Green function; Record additivity does not select a kernel; the Newton packet is not retired."
upstream_dependencies:
  - minimal_axioms
  - newton_law_derived_note
runner: scripts/lattice_green_on_z3_is_not_continuum_one_over_r_2026_08_13.py
---

# Discrete Z^3 Graph-Distance Reciprocal Is Not a Continuum 1/r Lattice Green Trial

**Date:** 2026-08-13
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** exact Fraction / integer-lattice comparison of the formal
continuum Newton-packet kernel symbol with the 6-nearest-neighbor graph
reciprocal on a finite cube of `Z^3`. The continuum symbol composed with
graph distance is not a lattice Green function. Record additivity does
not select a kernel. The Newton packet is not retired.
**Status authority:** independent audit lane only. This source note does
not set, predict, or estimate an audit verdict.
**Primary runner:**
[`scripts/lattice_green_on_z3_is_not_continuum_one_over_r_2026_08_13.py`](../scripts/lattice_green_on_z3_is_not_continuum_one_over_r_2026_08_13.py)

Parents (the only load-bearing textual inputs):

- [`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) — formal
  continuum kernel symbol and already-isolated source-linear product
  pairing.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — Lattice
  (`Z^3`, nearest-neighbor adjacency) and Record (including additivity of
  scalar readout on pairwise-disjoint records).

No axiom is edited. No gravitational coupling, no `G_N`, and no physical
Newton force law is imported or claimed. The continuum kernel is not
installed on the lattice.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "1/d fails nn-harmonicity at e1 by exact Fraction; G_cont∘d is not a lattice Green; Record additivity does not pick a kernel."
trace_class: negative_route_pruning
target_claim_id: discrete_z3_green_versus_one_over_r
target_blocker_text: "derive a 1/r kernel from the lattice after the product pairing is isolated"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The remaining Newton object is a lattice Green, not G_cont∘d. Do not install 1/r. Do not retire the Newton packet."
hypothetical_axiom_status: "no edit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Objects

The Newton packet uses, as a formal symbol for `r > 0`,

```text
G_cont(r) = 1/(4 π r).
```

That symbol is not constructed here. It is quoted from the parent packet
as a formal radial expression. This note does not identify it with a
lattice function and does not install `1/r` on `Z^3`.

Let `Z^3` carry the 6-nearest-neighbor adjacency of the Lattice axiom.
Graph distance from the origin is

```text
d(x, 0) = |x_1| + |x_2| + |x_3|.
```

Write `d(x)` for `d(x, 0)`. On the punctured cube

```text
C* = {-2, …, 2}^3 \ {0}
```

the graph reciprocal is the `Q`-valued function `x ↦ 1/d(x)`. The
composition `G_cont ∘ d` is the formal multiple `(1/(4 π)) · (1/d)` on
`C*`. Neither function is assigned a finite reciprocal at the origin:
`d(0) = 0`.

The 6-nearest-neighbor Laplacian (continuum sign) is

```text
(Δ_nn g)(x) = Σ_{y ~ x} (g(y) − g(x)) = (Σ_{y ~ x} g(y)) − 6 g(x).
```

A **graph Green trial** on the closed cube `C = {-2, …, 2}^3` is a
`Q`-valued function `g: C → Q` satisfying the lattice Poisson identities

```text
(Δ_nn g)(0) = −1,
(Δ_nn g)(x) = 0    for all x with 0 < |x|_∞ ≤ 1.
```

The already-isolated product pairing of the Newton packet is the
source-linear map

```text
π(M, G) := M · G,
```

the formal rule `phi = M G` recorded in the parent packet. This note
does not enlarge, replace, or re-derive `π`.

## Theorem 1

At the executed sites `e_1 = (1,0,0)`, `2 e_1 = (2,0,0)`, and
`e_1 + e_2 = (1,1,0)`,

```text
d(e_1) = 1,     d(2 e_1) = 2,     d(e_1 + e_2) = 2,
1/d(e_1) = 1,   1/d(2 e_1) = 1/2, 1/d(e_1 + e_2) = 1/2.
```

The six 6-nearest-neighbor sites of `e_1` and the corresponding
`1/d` values are

```text
(0,0,0)   : 1/d undefined (not a finite lattice value),
(2,0,0)   : 1/2,
(1, 1,0)  : 1/2,
(1,-1,0)  : 1/2,
(1,0, 1)  : 1/2,
(1,0,-1)  : 1/2.
```

The center value is `1/d(e_1) = 1`. The nn-Laplacian of `1/d` at `e_1`
is therefore not the zero element of `Q`: the stencil meets the origin,
where `1/d` is not a finite lattice value, so the predicate
“`1/d` is nn-harmonic off `0`” fails at `e_1`.

Under the unique `Q`-valued extension that agrees with `1/d` on `C*` and
places `0` at the undefined origin (the only integer that is not a
reciprocal of a positive graph distance on `C`), the same stencil
evaluates to the explicit nonzero Fraction

```text
(Δ_nn f)(e_1) = 0 + 5 · (1/2) − 6 · 1 = −7/2 ≠ 0.
```

## Theorem 2

Consequently `G_cont ∘ d` is not a lattice Green function.

On `C*` the composition is a positive formal multiple of `1/d`. A
positive multiple of a function that fails to be nn-harmonic at `e_1`
cannot satisfy `(Δ_nn g)(e_1) = 0`. Even if the origin value is left
free in `Q`, no extension of `1/d` is a graph Green trial: Poisson at
the origin forces one origin value, and harmonicity at `e_1` forces
another.

Let `g(0) = c ∈ Q` and `g = 1/d` on `C*`. The six neighbors of the
origin are `± e_i`, each with `1/d = 1`, so

```text
(Δ_nn g)(0) = 6 · 1 − 6 c = 6(1 − c).
```

The identity `(Δ_nn g)(0) = −1` forces `c = 7/6`. The stencil at `e_1`
gives

```text
(Δ_nn g)(e_1) = c + 5 · (1/2) − 6 = c − 7/2,
```

and `(Δ_nn g)(e_1) = 0` forces `c = 7/2`. These are distinct elements of
`Q`. Therefore no function that equals `1/d` at every executed site of
`C*` satisfies the lattice Poisson identities, and the formal
composition `G_cont ∘ d` is not a lattice Green function.

The same non-harmonicity is visible at a site whose stencil never meets
the origin: at `e_1 + e_2`,

```text
(Δ_nn (1/d))(e_1 + e_2) = 2 · 1 + 4 · (1/3) − 6 · (1/2) = 1/3 ≠ 0.
```

## Theorem 3

Record additivity does not pick either kernel.

The Record axiom of the parent memo states that records form; that a
present record locks exactly one admissible local possibility; that a
site never carries more than one record; that records are permanent;
and that for any finite collection of pairwise-disjoint records, scalar
readout `I` is additive, with `I(empty) = 0`.

That additivity is a statement about scalar readout of disjoint records.
It does not name a Green function, a Laplacian, a radial kernel, graph
distance, `1/d`, or `G_cont`. It therefore does not select
`G_cont ∘ d` over a graph Green trial, nor the reverse.

## Theorem 4

This note does not retire the Newton packet. It splits the remaining
kernel object from the already-isolated product pairing `π`.

The parent packet still records the formal algebra `G(r) = 1/(4 π r)`,
`phi = M G`, `|grad phi| = M/(4 π r^2)` as bounded-support
potential-kernel algebra, and it still refuses a physical force law.
The product pairing `π(M, G) := M · G` is already isolated there as
source-linearity. What remains unidentified is the kernel object
itself: the formal continuum symbol is not the 6-nn graph reciprocal,
and the graph reciprocal is not a lattice Green function. Separating
those objects does not delete the packet.

## Non-claims

This row does not prove, install, or claim:

- a physical Newton force law, a gravitational coupling, or `G_N`;
- that `1/r` or `G_cont` is the lattice Green function on `Z^3`;
- that a graph Green function on `Z^3` has been constructed;
- that Record additivity produces a pairing of sources or a kernel;
- retirement, replacement, or promotion of the Newton parent packet;
- any axiom edit or new primitive.

## Verification

Run:

```bash
python3 scripts/lattice_green_on_z3_is_not_continuum_one_over_r_2026_08_13.py
```

Expected closeout: `PASS >= 10`, `FAIL = 0`, and the mutation predicate
“`1/d` is nn-harmonic off `0`” fails at `e_1`.
