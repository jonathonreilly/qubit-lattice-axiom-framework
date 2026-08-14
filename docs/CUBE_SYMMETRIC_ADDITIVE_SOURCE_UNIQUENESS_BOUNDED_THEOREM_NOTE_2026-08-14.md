---
claim_id: cube_symmetric_additive_source_uniqueness_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed unit cube A=[0,1]^3 with vertex set V, the Q-linear maps Q^V → Q invariant under the 24-element proper rotation group of A form a 1-dimensional space spanned by ρ(o)=∑_{v∈V} o(v). Occupancy is a {0,1}-valued function on V, identified with a vector in Q^8. No physical source law, flux law, or extra axiom is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_symmetric_additive_source_uniqueness_2026_08_14.py
---

# Cube-Symmetric Additive Source Uniqueness On One Bounded Cube

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact linear-algebra uniqueness for cube-symmetric maps
`Q^8 → Q` on the displayed eight-vertex cube `A = [0,1]^3`. Occupancy
is a function of those eight vertices. No physical source identification,
flux inversion, or extra axiom is asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_symmetric_additive_source_uniqueness_2026_08_14.py`](../scripts/cube_symmetric_additive_source_uniqueness_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `A = [0,1]^3` and let `V` be its eight vertices. Occupancy is a
function `o: V → {0,1}`, identified with a vector in `Q^8` by the
fixed binary labeling

```text
index(x,y,z) = x + 2y + 4z,     (x,y,z) in {0,1}^3.
```

A linear decoder is a `Q`-linear map `f: Q^8 → Q`. Write `c = (1/2,1/2,1/2)`
for the cube center. Cube-symmetric means

```text
f(o ∘ R^{-1}) = f(o)
```

for every proper cube rotation `R` that preserves `A`: equivalently, for
every `3 × 3` signed permutation matrix `P` of determinant `+1`,

```text
R(x) = c + P(x − c).
```

There are exactly 24 such maps. They are the rotation group of `A` acting
on the eight vertices.

**Theorem.** The space of cube-symmetric linear maps `Q^8 → Q` is
1-dimensional, spanned by

```text
ρ(o) = ∑_{v ∈ V} o(v).
```

Thus any cube-symmetric linear decoder of occupancy is a rational multiple
of the vertex sum. The word "unique" refers only to this one-dimensional
span. It names no physical source law.

`ρ` is a function of occupancy, not a fifth extra.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Q-linear algebra on the displayed eight-vertex cube classifies cube-symmetric decoders as the span of the vertex sum."
trace_class: frontier_discovery
target_claim_id: cube_symmetric_additive_source_uniqueness
target_blocker_text: "whether a cube-symmetric linear occupancy decoder is unique"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the displayed mathematical host A=[0,1]^3 over Q; no physical source identification is asserted"
hypothetical_axiom_status: "none; ρ is a function of occupancy and is not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentences below supply the
  cubic lattice `Z^3` and the existence of proper cubic rotations, together
  with the no-privileged-site clause. The live Record sentences supply that
  a present record locks one admissible local possibility and that a readout
  value is determined by record content. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the unit cube `A = [0,1]^3`, its
  eight vertices, the identification of occupancy with `Q^8`, and invariance
  under the 24-element rotation group of `A` about `c` are supplied
  mathematical data for this theorem. Those 24 maps are the rotation group
  of the displayed cube. They are not renamed after Lattice.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** any identification of `ρ` with a physical source,
  any inversion from flux to occupancy, and any selection of occupancy by
  Admissibility remain separate, open obligations outside the target proved
  here.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float
is used.

Vertices lie in `Z^3`. Linear maps are `Q`-linear. The cube center `c`
has coordinates in `Q`.

Write `e_v` for the occupancy that equals `1` at `v` and `0` at every
other vertex of `V`. These eight vectors are the standard basis of `Q^8`.

A general linear decoder is `f(o) = w · o` for a unique weight vector
`w ∈ Q^8`. Cube-symmetry is the linear condition `w · (o ∘ R^{-1}) = w · o`
for every proper rotation `R` of `A` and every `o ∈ Q^8`.

## Exact Target And Proof Obligations

The exact target is to prove that the cube-symmetric subspace of
`Hom_Q(Q^8, Q)` is spanned by `ρ`.

The obligation graph is:

1. the eight vertices form one orbit under the 24-element rotation group of
   `A`;
2. invariance forces `f(e_v)` to be the same rational number for every
   vertex `v`;
3. linearity then forces `f = c ρ` for that common value `c = f(e_v)`;
4. `ρ` itself is invariant, because each rotation merely permutes the
   summands.

All four obligations are closed below and in the runner. The runner
row-reduces the complete 8-weight invariance system over `Q` rather than
sampling a coefficient grid. The displayed cube, the `{0,1}` occupancy
range, and `Q`-linearity are theorem hypotheses. Nonlinear decoders,
improper isometries, other hosts, and lattice-wide lifts are outside this
theorem. There is no missing lemma for the bounded algebraic target; a
physical interpretation would be a separate claim with separate support.

## Theorem 1 — one orbit

The eight vertices of `A` form a single orbit under the 24 proper
rotations of `A`. Explicitly: for any pair `u, v ∈ V` there is a signed
permutation matrix `P` of determinant `+1` such that
`v = c + P(u − c)`.

The companion runner enumerates the 24 matrices, checks that they form a
group of order 24, checks that each preserves `V`, and checks transitivity
on `V`.

## Theorem 2 — equal values on basis occupancies

Let `f` be cube-symmetric and `Q`-linear. For any vertices `u, v` choose
`R` with `R(u) = v`. Occupancy transforms by

```text
e_u ∘ R^{-1} = e_{R(u)} = e_v,
```

so invariance gives `f(e_v) = f(e_u)`. Therefore `f(e_v)` is independent
of `v`.

## Theorem 3 — uniqueness

Every `o ∈ Q^8` expands as `o = ∑_{v ∈ V} o(v) e_v`. Linearity and
Theorem 2 give

```text
f(o) = ∑_{v ∈ V} o(v) f(e_v) = c ∑_{v ∈ V} o(v) = c ρ(o),
```

where `c = f(e_v)` is the common basis value. Hence the cube-symmetric
subspace is at most 1-dimensional.

Equivalently, writing `f(o) = w · o`, the 24 invariance identities
`(P_R^⊤ − I_8) w = 0` form a rank-7 system on `Q^8` whose nullspace is
`span_Q{(1,1,1,1,1,1,1,1)}`.

## Theorem 4 — `ρ` is itself invariant

Each proper rotation of `A` permutes `V`. Therefore

```text
ρ(o ∘ R^{-1}) = ∑_{v ∈ V} o(R^{-1} v) = ∑_{u ∈ V} o(u) = ρ(o).
```

So `ρ` is cube-symmetric, the subspace is exactly 1-dimensional, and it is
spanned by `ρ`.

## Physical-Interpretation Boundary

The proved output is the one-dimensional space of cube-symmetric linear
maps on the displayed cube. This note neither assigns `ρ` a physical
source label nor changes the Qubit statement. `ρ` is a function of
occupancy, not a fifth extra, and no additional axiom is proposed.

## Mutation Checks

Two non-equivalences guard the load-bearing conclusions:

1. the eight single-site occupancies all give `ρ(e_v) = 1`, so the common
   basis value is not a hidden site-dependent weight;
2. the mutated functional that weights one vertex by `2` and the others
   by `1` fails invariance under any rotation that moves that vertex.

## What This Does Not Claim

- The displayed cube is not claimed to exhaust the lattice, and no
  lattice-wide decoder is classified.
- Cube-symmetry is invariance under the rotation group of `A`. It is not
  a renaming of Lattice.
- Nonlinear maps, maps into a larger codomain, and maps that use more than
  the eight vertex occupancies are not classified.
- Uniqueness of a flux given `ρ` is a separate question and is not proved
  here.
- No claim is made that Record locks a particular occupancy pattern or
  that Admissibility selects `ρ`.
- `ρ` is not proposed as axiom content.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

> When present, a record locks exactly one admissible local possibility.

> Only records are readable. A readout value is determined by record content
> alone.

Their dependency role is limited to the cubic lattice vocabulary, the
existence of proper cubic rotations, the no-privileged-site clause, and
the lock-and-content readout rule. This theorem separately supplies the
unit cube, the occupancy identification with `Q^8`, and cube-symmetry
under the rotation group of that cube.

## Runner Contract

The companion runner checks Theorems 1–4 with exact rational arithmetic.
It enumerates the 24 proper rotations, checks the single orbit, row-reduces
the complete eight-weight invariance system, checks that `ρ` is invariant
on the generic occupancy `(1,0,1,0,0,1,1,0)` under those rotations, checks
that every single-site occupancy has `ρ = 1`, and checks that weighting
one vertex by `2` breaks invariance. It also quotes the live Lattice and
Record sentences, prints substantive N5 scope certificates, and records
the import boundary. Declared review inputs are this note and the axiom
memo only.
