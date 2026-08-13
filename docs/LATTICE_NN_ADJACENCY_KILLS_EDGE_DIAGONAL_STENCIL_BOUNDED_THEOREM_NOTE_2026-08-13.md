---
claim_id: lattice_nn_adjacency_kills_edge_diagonal_stencil_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On Z^3 at the origin, the unnormalized six-neighbor stencil of φ(x)=x1²+x2²+x3² equals 6 and the twelve-site edge-diagonal stencil equals 24, so the two O_h classes are distinct operators; Lattice names nearest-neighbor adjacency, which is the 6-NN cubic graph of graph distance 1, not the 18-neighbor graph; inside the two-parameter family Δ_{α,β}=α Δ_NN + β Δ_edge a later graph-Laplacian supplier of the named adjacency forces β=0 and a rational multiple of Δ_NN; that supplier is extra; no Green function, 1/r kernel, product M_s M_t, Newton constant, or Laplacian axiom is selected."
upstream_dependencies:
  - minimal_axioms
runner: scripts/lattice_nn_adjacency_kills_edge_diagonal_stencil_2026_08_13.py
---

# Lattice NN Adjacency Kills The Edge-Diagonal Stencil Coefficient

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact integer stencil arithmetic on `Z^3` at the origin; two
`O_h`-invariant neighbor classes; the two-parameter family
`Δ_{α,β}=α Δ_NN + β Δ_edge` with `α,β ∈ Q`; Lattice nearest-neighbor
adjacency as the six-neighbor cubic graph.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/lattice_nn_adjacency_kills_edge_diagonal_stencil_2026_08_13.py`](../scripts/lattice_nn_adjacency_kills_edge_diagonal_stencil_2026_08_13.py)

## Result Up Front

The current Lattice sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The named adjacency phrase is **nearest-neighbor adjacency**. That phrase is
the six-neighbor cubic graph, not the eighteen-neighbor graph that would add
the edge-diagonals.

The axioms do not name a field operator. This note does not install one.

Five exact statements locate the split.

1. **The two stencils disagree on `φ`.** With `φ(x)=x1²+x2²+x3²` one has
   `(Δ_NN φ)(0)=6` and `(Δ_edge φ)(0)=24`. Hence `Δ_NN ≠ Δ_edge` as
   operators.
2. **Edge-diagonals are not nearest neighbors.** Every edge-diagonal site
   has graph distance `2` from the origin on the named six-neighbor graph.
   Those twelve sites are not nearest neighbors.
3. **Named-adjacency Laplacian kills `β`.** If a later supplier says the
   field operator is a graph Laplacian of the *named* adjacency, then
   `β=0` and the operator is a rational multiple of `Δ_NN`. That supplier
   is extra. Lattice kills only the edge-diagonal coefficient inside this
   two-parameter class.
4. **No kernel, no Newton product, no constant.** The note does not select
   a Green function, a 1/r kernel, a product `M_s M_t`, or Newton’s
   constant.
5. **No Laplacian axiom.** The note does not adopt a Laplacian axiom. It
   does not claim that `Δ_NN` is the only `O_h`-invariant operator on all
   of `ℓ²(Z^3)`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The integer identities (Δ_NN φ)(0)=6 and (Δ_edge φ)(0)=24, the graph-distance-2 listing of the twelve edge-diagonals, and the β=0 restriction inside Δ_{α,β} are proved by exact integer arithmetic on declared Z^3 neighbor classes; a field-operator supplier remains extra."
trace_class: negative_route_pruning
target_claim_id: lattice_nn_adjacency_kills_edge_diagonal_stencil
target_blocker_text: "derive an O_h field-operator stencil with a nonzero edge-diagonal coefficient from Lattice nearest-neighbor adjacency"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "If a later supplier names the field operator as the graph Laplacian of the named adjacency, then β=0 and the operator is a rational multiple of Δ_NN. That supplier is extra. Do not adopt axiom text."
conditional_surface_status: "exact for the 6-versus-24 split, graph distance 2, and β=0 inside the named two-parameter family; a field operator, Green function, and Laplacian axiom remain open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at the origin of `Z^3`. Write `e1=(1,0,0)`, `e2=(0,1,0)`, `e3=(0,0,1)`.
Graph distance is the `ℓ¹` path metric of the six-neighbor cubic graph.

Two `O_h`-invariant neighbor classes:

- NN (`6`): `±e1`, `±e2`, `±e3`. Graph distance `1`.
- Edge-diagonal (`12`): `±e_i ± e_j` for `i<j`. Graph distance `2`.

The twelve edge-diagonal sites are

```text
( 1, 1, 0), ( 1,-1, 0), (-1, 1, 0), (-1,-1, 0),
( 1, 0, 1), ( 1, 0,-1), (-1, 0, 1), (-1, 0,-1),
( 0, 1, 1), ( 0, 1,-1), ( 0,-1, 1), ( 0,-1,-1).
```

The eighteen-neighbor set is the disjoint union of these two classes. It is
not the named adjacency.

Two unnormalized stencils act on a test function `φ` by

```text
(Δ_NN φ)(0)   = Σ_{x NN}   (φ(x) − φ(0))
(Δ_edge φ)(0) = Σ_{x edge} (φ(x) − φ(0))
```

A two-parameter `O_h` stencil is

`Δ_{α,β} = α Δ_NN + β Δ_edge`, `α,β ∈ Q`.

The executed test function is the integer quadratic

`φ(x) = x1² + x2² + x3²`.

Then `φ(0)=0`, `φ=1` on every NN site, and `φ=2` on every edge-diagonal
site.

`O_h` is the signed-permutation group on the three axes (order `48`). It
preserves the cubic lattice, the six-neighbor graph, and each of the two
classes. Proper cubic rotations about a site are the index-two rotation
subgroup; the full `O_h` orbit decomposition is used only to name the
classes.

## Exact Target And Obligation Graph

**Exact target.** At the origin of `Z^3`, evaluate the two unnormalized
`O_h` stencils on `φ`; prove they disagree; prove every edge-diagonal has
graph distance `2` on the named adjacency; and record that a later
graph-Laplacian supplier of that adjacency forces `β=0` inside
`Δ_{α,β}`, without installing a field operator, a Green function, or a
Laplacian axiom.

| Obligation | Role | Disposition |
|---|---|---|
| pin the Lattice nearest-neighbor sentence | premise | quoted; no edit |
| evaluate `(Δ_NN φ)(0)` and `(Δ_edge φ)(0)` | Theorem 1 | exact integers `6` and `24` |
| conclude `Δ_NN ≠ Δ_edge` as operators | Theorem 1 | they disagree on `φ` |
| list graph distances of the twelve edge sites | Theorem 2 | each equals `2` |
| identify the named graph as `6`-NN, not `18` | Theorem 2 | Lattice phrase |
| restrict `Δ_{α,β}` under a named-adjacency Laplacian supplier | Theorem 3 | `β=0`; rational multiple of `Δ_NN` |
| record that the supplier is extra | Theorem 3 | axioms name no field operator |
| refuse Green, `1/r`, `M_s M_t`, Newton constant | Theorem 4 | scoped negative |
| refuse a Laplacian axiom and `ℓ²` uniqueness | Theorem 5 | scoped negative |
| adopt a Laplacian axiom or install `1/r` | non-claim | not attempted |

## Theorem 1 — The Two Stencils Disagree On `φ`

**Claim.** `(Δ_NN φ)(0) = 6` and `(Δ_edge φ)(0) = 24`. Hence
`Δ_NN ≠ Δ_edge` as operators: they disagree on this `φ`.

**Proof.** The origin value is `φ(0,0,0)=0`. Each of the six NN sites is a
standard basis vector or its negative, so `φ(NN)=1+0+0=1`. The unnormalized
NN stencil is therefore

`(Δ_NN φ)(0) = 6 · (1 − 0) = 6`.

Each of the twelve edge-diagonal sites has two coordinates in `{±1}` and
one coordinate `0`, so `φ(edge)=1+1+0=2`. The unnormalized edge stencil is
therefore

`(Δ_edge φ)(0) = 12 · (2 − 0) = 24`.

If the two operators were equal they would agree on every test function, in
particular on `φ`. They do not: `6 ≠ 24`. A predicate
“`Δ_NN φ = Δ_edge φ` at `0`” fails.

The arithmetic is integer. No continuum limit is used.

## Theorem 2 — Edge-Diagonals Are Not Nearest Neighbors

**Claim.** The graph distance of an edge-diagonal from the origin is `2`,
so those twelve sites are not nearest neighbors. The named adjacency graph
is the `6`-NN cubic graph, not the `18`-neighbor graph.

**Proof.** The Lattice sentence names **nearest-neighbor adjacency** on the
cubic lattice `Z^3`. The unique translation-invariant cubic graph whose
degree-`6` star at the origin is `{±e1, ±e2, ±e3}` is the six-neighbor
cubic graph. Its graph distance from the origin is the `ℓ¹` norm
`d(x)=|x1|+|x2|+|x3|`.

On that graph, every listed edge-diagonal satisfies

`d(±e_i ± e_j)=1+1+0=2`.

A nearest neighbor is a site at graph distance `1`. The twelve
edge-diagonals are therefore not nearest neighbors. A predicate
“edge-diagonals are nearest neighbors” fails.

The eighteen-neighbor set is the disjoint union of the six NN sites and the
twelve edge-diagonals. Using that set as the adjacency would name a
different graph. Lattice does not name it.

Proper cubic rotations permute the six NN sites among themselves and the
twelve edge-diagonals among themselves. They do not mix the two classes,
and they do not move an edge-diagonal onto the NN star.

## Theorem 3 — Named-Adjacency Laplacian Forces `β=0`

**Claim.** If a later supplier says the field operator is a graph Laplacian
of the *named* adjacency, then `β=0` and the operator is a rational
multiple of `Δ_NN`. That supplier is extra: the axioms do not name a field
operator. Lattice kills only the edge-diagonal coefficient inside this
two-parameter class.

**Proof.** The two-parameter family is

`Δ_{α,β} = α Δ_NN + β Δ_edge`, `α,β ∈ Q`.

A graph Laplacian of an undirected graph with no loops acts at the origin
by a rational multiple of `Σ_{x ∼ 0} (φ(x)−φ(0))`, where `∼` is the named
adjacency. Theorem 2 identifies that adjacency with the six-neighbor cubic
graph. The twelve edge-diagonals are not adjacent to the origin, so they
do not appear in the sum. Therefore `β=0` and

`Δ_{α,0} = α Δ_NN`.

That is a rational multiple of `Δ_NN`.

The supplier that *identifies* a field operator with that graph Laplacian
is extra. The Lattice sentence names sites, nearest-neighbor adjacency,
translations, and proper cubic rotations. It does not name a field
operator, a Laplacian, or a coefficient `β`. Admissibility names a
nearest-neighbor probability rule, not a stencil. Record names locking and
readout, not a stencil. Inside the declared class `Δ_{α,β}`, the Lattice
nearest-neighbor clause is enough to kill `β`. It is not enough to install
the operator.

## Theorem 4 — No Green Function, No `1/r`, No Newton Product

**Claim.** This does not select a Green function, a 1/r kernel, a product
`M_s M_t`, or Newton’s constant.

**Proof.** Theorems 1--3 are statements about two unnormalized stencils on
one quadratic test function, and about which of those stencils can appear
in a later named-adjacency Laplacian. A Green function is an inverse of an
operator. No inverse is constructed. A `1/r` kernel is a pointwise function
of Euclidean radius. No such function is written, fitted, or installed. A
product `M_s M_t` is a two-argument pairing of readout scalars. No pairing
is written. Newton’s constant is a dimensionful coupling. It is not
imported and not named as a derived value.

Selecting the operator class is not selecting a kernel, a pairing, or a
constant. The note does not claim gravity.

## Theorem 5 — No Laplacian Axiom, No `ℓ²` Uniqueness

**Claim.** Do not adopt a Laplacian axiom. Do not claim that `Δ_NN` is the
only `O_h`-invariant operator on all of `ℓ²(Z^3)` — only that, inside this two-parameter stencil family, Lattice’s NN clause forces `β=0`.

**Proof.** An axiom-sentence change that named a Laplacian would be a
different document. This note quotes the current Lattice sentence and does
not edit it.

`O_h`-invariant operators on `ℓ²(Z^3)` include, among others, longer-range
radial stencils, polynomials in `Δ_NN`, and Fourier multipliers constant
on `O_h` orbits in the Brillouin zone. None of those objects is classified
here. The executed family is the two-parameter stencil `Δ_{α,β}`. Inside
that family, Theorem 3 gives `β=0` once the named adjacency is used as the
graph. That is the whole uniqueness claim.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom-sentence change is
  necessary;
- adopt a Laplacian axiom;
- claim that `Δ_NN` is the only `O_h`-invariant operator on all of
  `ℓ²(Z^3)`;
- select a Green function, install a 1/r kernel, write a product
  `M_s M_t`, or import Newton’s constant;
- claim gravity;
- replace nearest-neighbor adjacency by the eighteen-neighbor graph;
- assert that the axioms already name a field operator.

The scope is the exact cubic split: `6` versus `24` on `φ`, graph
distance `2` for the edge class, and `β=0` inside `Δ_{α,β}` under a
named-adjacency Laplacian supplier.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice NN sentence | premise | quoted; no edit |
| six NN sites and twelve edge-diagonals | Theorem 1--2 | listed here |
| `(Δ_NN φ)(0)=6`, `(Δ_edge φ)(0)=24` | Theorem 1 | computed here |
| graph distance `2` on the named graph | Theorem 2 | computed here |
| `β=0` inside `Δ_{α,β}` under a named-adjacency Laplacian | Theorem 3 | computed here |
| field-operator supplier | residual | extra; not derived |
| Green function, `1/r`, `M_s M_t`, Newton constant | none | not selected |
| observed or fitted kernels | none | not used |

The exact advance is a finite lattice-geometry theorem about two stencil
coefficients. Independent audit is required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | A later field-operator construction on `Z^3` may be tempted to mix the twelve edge-diagonals into an `O_h` stencil. The named Lattice adjacency is nearest-neighbor. This note asks whether that clause already kills the edge-diagonal coefficient inside `Δ_{α,β}`, and answers yes, while leaving the operator itself uninstalled. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for `Δ_NN`, `delta_nn`, edge-diagonal stencil coefficients, and a `6`-versus-`24` split of unnormalized `O_h` stencils on `φ(x)=‖x‖²`. Hits: `LATTICE_LAPLACIAN_SHELL_LOCALIZATION_IDENTITY_BOUNDED_THEOREM_NOTE_2026-06-16.md` is a shell-localization identity, not this coefficient split; the `LATTICE_NN_*` notes are continuum, RG, light-cone, or distance-law surfaces. No landed note that `(Δ_NN φ)(0)=6 ≠ 24=(Δ_edge φ)(0)` forces `β=0` inside `Δ_{α,β}` appears on that commit. Unmerged drafts are not premises. |
| V3 | Independently checkable? | Textbook cubic graph distance and the integer quadratic `φ` do not mention a field operator, a Green function, or Newton’s constant. The runner recomputes both stencils by summing `φ(x)−φ(0)` over the listed sites. |
| V4 | More than a restatement? | Yes. The discriminating witnesses are the integers `6` and `24` and the graph-distance-`2` listing. The Lattice sentence names nearest-neighbor adjacency; it does not evaluate either stencil. |
| V5 | One-step relabel? | No. The claim is not a corollary of the Lattice sentence alone. That sentence names the adjacency graph. The two-parameter family, the test function `φ`, and the coefficient `β` are declared objects of this note. |

## No-Go Discipline Gate (Theorems 4 and 5 only)

The negative claims are restricted to: this block does not select a Green
function, a `1/r` kernel, a product `M_s M_t`, or Newton’s constant; it
does not adopt a Laplacian axiom; it does not claim `ℓ²(Z^3)` uniqueness
for `Δ_NN`. The gate does not ship a global non-existence theorem against
later operators.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| equate the two stencils | treat `Δ_NN φ = Δ_edge φ` at the origin | Theorem 1: `6 ≠ 24` | **ATTEMPTED** |
| treat edge-diagonals as NN | read graph distance `2` as nearest | Theorem 2: `d=2` | **ATTEMPTED** |
| use the `18`-neighbor graph | add the twelve edge sites to the adjacency | Theorem 2: that graph is not named | **ATTEMPTED** |
| keep `β` with a named-adjacency Laplacian | write `Δ_{α,β}` with `β≠0` as the graph Laplacian of the named graph | Theorem 3: `β=0` | **ATTEMPTED** |
| read Lattice as already naming the operator | treat the adjacency sentence as a Laplacian axiom | Theorem 3: the supplier is extra | **ATTEMPTED** |
| install `1/r` or a Green function | pass from the stencil to a kernel | Theorem 4: no inverse, no kernel | **ATTEMPTED** |
| claim `ℓ²` uniqueness or adopt a Laplacian axiom | treat `Δ_NN` as the only `O_h` operator | Theorem 5: family-internal only | **ATTEMPTED** |

### N2 — wall independence

Theorems 4 and 5 close only the route that would read a Green function, a
`1/r` kernel, a Newton product, a Laplacian axiom, or `ℓ²` uniqueness off
the `6`-versus-`24` split. They do not close a later field-operator
derivation that supplies `Δ_NN` by other means, nor a later kernel
analysis of that operator.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `Z^3` with six-neighbor adjacency | declared Lattice object |
| origin evaluation point | explicit hypothesis |
| NN class of size `6` | listed; graph distance `1` |
| edge-diagonal class of size `12` | listed; graph distance `2` |
| test function `φ(x)=x1²+x2²+x3²` | declared integer quadratic |
| family `Δ_{α,β}` | declared two-parameter stencil |
| named-adjacency Laplacian supplier | extra; not derived |
| Green function, `1/r`, `M_s M_t`, Newton constant | not selected |
| Laplacian axiom | not adopted |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice nearest-neighbor adjacency sentence | quoted as premise only; no edit |
| two `O_h` neighbor classes | `6` versus `12` sites | listed here |
| stencil evaluations on `φ` | `6` versus `24` | computed here |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | origin, six NN sites, twelve edge-diagonals, integers `6` and `24` | no classification of every map on `Z^3` |
| per site | stencils evaluated at the origin; `O_h` orbits that site’s neighbor classes | no composite multi-site operator |
| per mode | unnormalized graph stencils on one quadratic; no Green function | no harmonic-mode exhaustion |
| per block | the `6`-versus-`24` split, graph distance `2`, and `β=0` inside `Δ_{α,β}` | no dynamics, kernel, or Newton constant |
| lattice-wide | checked and not executed | no uniqueness of `Δ_NN` on all of `ℓ²(Z^3)` |

The obstruction is per-origin / declared stencil family; it is not
lattice-wide uniqueness.

### N6 — live partial-closure paths

1. A later supplier that names a field operator by other executable
   objects, including a named-adjacency Laplacian, in which case Theorem 3
   already forces `β=0` inside this family.
2. A later analysis of a Green function of whatever operator is supplied.
3. A later pairing of readout scalars, independent of this stencil split.
4. A different adjacency, including the eighteen-neighbor graph, if and
   when that adjacency is the Lattice object. It is not the present object.

The quoted Lattice sentence already names nearest-neighbor adjacency.
Killing `β` inside `Δ_{α,β}` uses that clause. No axiom sentence is edited
here. A later derivation of an operator is not forbidden.

### N7 — hostile steelman

> The two `O_h` classes are just the same Laplacian at different ranges.
> On a quadratic they must agree up to a constant, so `Δ_edge` is a
> multiple of `Δ_NN` and the eighteen-neighbor stencil is still
> nearest-neighbor in the only sense that matters.

**Answer.** That identification is exactly the predicate
“`Δ_NN φ = Δ_edge φ` at `0`,” or the predicate “edge-diagonals are
nearest neighbors.” Theorem 1 gives `6 ≠ 24`, so the operators disagree
on this quadratic. Theorem 2 gives graph distance `2` on the named graph,
so the twelve sites are not nearest neighbors. A constant multiple would
require `24=c·6` together with operator equality; operator equality already
fails on `φ`. The eighteen-neighbor graph is a different adjacency.

### N8 — cross-cycle echo

The 2026-06-16 lattice-Laplacian shell-localization note and the landed
`LATTICE_NN_*` continuum and RG notes treat other objects: shells of a
already-chosen Laplacian, or continuum/RG diagnostics of a nearest-neighbor
surface. They do not evaluate `(Δ_NN φ)(0)` against `(Δ_edge φ)(0)` or kill
`β` inside `Δ_{α,β}`. The present negatives face a narrower residual: the
named adjacency does not include the edge-diagonal coefficient. The earlier
notes are not cancelled.

**Gate disposition.** PASS for the `6`-versus-`24` split, the
graph-distance-`2` listing, and the scoped negatives of Theorems 4 and 5.
FAIL / DO NOT SHIP for installing `1/r`, claiming gravity, or editing an
axiom sentence to name a Laplacian.

## Primary Runner

[`scripts/lattice_nn_adjacency_kills_edge_diagonal_stencil_2026_08_13.py`](../scripts/lattice_nn_adjacency_kills_edge_diagonal_stencil_2026_08_13.py)
recomputes the six NN sites, the twelve edge-diagonals, the integer values
`(Δ_NN φ)(0)=6` and `(Δ_edge φ)(0)=24`, and the graph-distance-`2` listing
in exact integer arithmetic on `Z^3`. Identity gates call `delta_nn_phi()`
and `delta_edge_phi()`. A predicate “`Δ_NN φ = Δ_edge φ` at `0`” must fail
(`6 ≠ 24`). A predicate “edge-diagonals are nearest neighbors” must fail
(graph distance `2`).
