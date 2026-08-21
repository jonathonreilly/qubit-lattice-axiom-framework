---
claim_id: opposite_lock_four_event_minkowski_gram_signature_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Minkowski Gram signature of the three nsopp displacements from origin of axis, face, and body events is reported versus nsgram (1,2,0). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_four_event_minkowski_gram_signature_2026_08_15.py
---

# Minkowski Gram Signature Of Three Nsopp Displacements

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact 3×3 Minkowski Gram of three four-event displacements under
nsopp-process formation ticks, with signature by exact rational LDL. The
Gram and signature are displayed, not adopted. No metric is written into
Admissibility. Uniqueness is not required. L1 is not attached. This is not
an nsgram reprint.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_four_event_minkowski_gram_signature_2026_08_15.py`](../scripts/opposite_lock_four_event_minkowski_gram_signature_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Four events only, with sites as in the gram4 / nsgram four-event list and
with nsopp-process formation ticks (not a hop-cost shortest-path fill):

```text
O = (0,0,0),   t(O) = 0,
A = (1,0,0),   t(A) = 3,
D = (1,1,0),   t(D) = 3,
B = (1,1,1),   t(B) = 2.
```

The process is the opposite-lock two-site seed on the Euclidean host
`B_3(0)`: seed `{0,(0,1,0)}` locks `+e_1/−e_1` at tick 0; a six-neighbor
step is allowed if and only if it is perpendicular to the parent lock
axis; a newly formed site locks the incoming step. Seed sites have tick 0.
The extra seed site `(0,1,0)` is not one of the three displacements from
the origin used here. Incoming-lock uniqueness is not required. A later
parent does not re-form a site.

The 4-vector of a site `x` is `u(x) = (t(x), x_1, x_2, x_3)`. The Minkowski
product is

```text
u · v = t_u t_v − x_u · x_v.
```

Let `G` be the 3×3 Gram of `(u(A), u(D), u(B))`. Exact arithmetic gives

```text
G = (( 8,  8,  5),
     ( 8,  7,  4),
     ( 5,  4,  1)).
```

Exact rational LDL yields diagonal pivots `(8, −1, −9/8)` and signature

```text
(n+, n−, n0) = (1, 2, 0).
```

That triple equals the displayed nsgram / gram4 comparison value `(1, 2, 0)`.
The equality is a signature comparison only. The nine Gram entries are not
the nsgram Gram: nsgram uses nnseed ticks `t(A,D,B)=(2,1,2)`, whose Gram is
`((3,1,3),(1,-1,0),(3,0,1))`. This note is therefore not an nsgram reprint.
The common signature is displayed, not adopted as a spacetime metric, and
is not written into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact four-event Minkowski Gram entries and exact rational LDL signature are proved on nsopp-process formation ticks; metric adoption and Admissibility edits remain outside the claim."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "report the 3x3 Minkowski Gram signature of axis, face, and body displacements under nsopp formation ticks versus nsgram (1,2,0)"
source_of_blocker_text: handoff
reachability_to_target: advances
next_trace_action: "Use this result only as a displayed four-event Gram/signature lemma; do not adopt a metric or attach L1."
artifact_role: theorem
conditional_surface_status: "exact on the four named events and nsopp-process formation ticks; not adopted as framework structure"
hypothetical_axiom_status: "no axiom or primitive is edited or proposed"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies `Z^3` sites
  with nearest-neighbor adjacency. It is quoted without rewrite. The live
  Admissibility sentence supplies one fixed nearest-neighbor admissibility
  rule and no metric.
- **Process tick input:** `t(O,A,D,B)=(0,3,3,2)` is the nsopp-process
  formation-tick list on these four events. Seed sites have tick 0. The
  runner enumerates the opposite-lock process on `B_3(0)` to read those
  ticks. It does not fill by hop-cost shortest path.
- **Displayed comparison input:** nsgram reports signature `(1,2,0)` on
  nnseed ticks of the same three displacements, equal to the gram4 triple.
  That triple is a comparison target, not a derived lemma of this note.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** a spacetime metric, a clock map, a lock
  attachment, and any Admissibility rewrite remain outside the target.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

## Displayed Process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is `s · e_i = 0`. If `q` lies in `B_3(0)`, is still unformed,
and the step is allowed, then `q` forms next and locks the incoming step
`s`. If several allowed parents reach `q` at the same earliest formation,
each such incoming step is kept as a possible lock. Uniqueness is not
required. A later parent does not re-form `q`.

The score domain for the Gram is exactly the four events `O,A,D,B`. Locks
are used only to grow the allowed process that assigns formation ticks.
Locks are not attached as L1 and are not scored.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float
is used in the Gram, the LDL pivots, or the signature count.

```text
u(A) = (3, 1, 0, 0),
u(D) = (3, 1, 1, 0),
u(B) = (2, 1, 1, 1).
```

`u(O)=(0,0,0,0)`. `G_ij = u_i · u_j` in the order `(A,D,B)`. A
unit-lower-triangular `L` and diagonal `D` satisfy `G = L D L^T` over the
rationals whenever the successive Schur pivots are computed without float
rounding. The signature `(n+, n−, n0)` is the count of strictly positive,
strictly negative, and zero diagonal entries of `D`. By Sylvester inertia
this is the inertia of `G`.

Leading principal minors of `G` are an independent exact cross-check:

```text
Δ1 = 8,     Δ2 = -8,     Δ3 = det(G) = 9.
```

The sequence `(1, Δ1, Δ2, Δ3)` has two sign changes and no zero, hence
again `(n+, n−, n0)=(1,2,0)`.

## Theorem 1 — Four Formation Ticks And Nine Exact Gram Entries

Direct enumeration of the displayed opposite-lock process on `B_3(0)`
assigns

```text
t(O) = 0,   t(A) = 3,   t(D) = 3,   t(B) = 2.
```

Both seed sites have tick 0. The extra seed `(0,1,0)` is not a Gram
vector. Direct expansion of the Minkowski product then yields

```text
u(A)·u(A) = 9 − 1 = 8,
u(A)·u(D) = 9 − 1 = 8,
u(A)·u(B) = 6 − 1 = 5,
u(D)·u(D) = 9 − 2 = 7,
u(D)·u(B) = 6 − 2 = 4,
u(B)·u(B) = 4 − 3 = 1.
```

Symmetry of the product gives the remaining three entries. Therefore

```text
G = (( 8,  8,  5),
     ( 8,  7,  4),
     ( 5,  4,  1)).
```

These four ticks and nine values are the claim of Theorem 1. They are not
imported from nsgram.

## Theorem 2 — Signature From Exact Rational LDL

The unpivoted rational LDL of `G` is

```text
L = ((1,    0,  0),
     (1,    1,  0),
     (5/8,  1,  1)),
D = diag(8, −1, −9/8).
```

The first pivot is `D_11 = G_AA = 8`. The Schur complement in the
`(D,B)` block then produces `D_22 = −1` and `D_33 = −9/8`. Direct
multiplication recovers `L D L^T = G`. The product of the pivots is
`8 · (−1) · (−9/8) = 9 = det(G)`.

The pivot signs are one positive and two negative, with no zero, so

```text
(n+, n−, n0) = (1, 2, 0).
```

## Theorem 3 — Comparison With Nsgram / Gram4 Signature `(1,2,0)`

The displayed nsgram signature on nnseed ticks is `(1,2,0)`, equal to the
displayed gram4 signature on 1-seed ticks. The nsopp signature of
Theorem 2 equals that triple:

```text
(1, 2, 0) = (1, 2, 0).
```

The equality is displayed, not adopted. It does not write a metric into
Admissibility, does not select a clock, and does not attach L1. It also
does not claim uniqueness: nsgram and gram4 are different matrices on the
same three sites with the same inertia, so the signature does not name a
unique Gram.

## Not An Nsgram Reprint

On the same sites, the displayed nsgram ticks are `t(A)=2`, `t(D)=1`,
`t(B)=2`, with

```text
u_ns(A) = (2, 1, 0, 0),
u_ns(D) = (1, 1, 1, 0),
u_ns(B) = (2, 1, 1, 1),
G_ns = (( 3,  1,  3),
        ( 1, -1,  0),
        ( 3,  0,  1)).
```

`G ≠ G_ns` entrywise. The nsopp calculation uses ticks `(3,3,2)` and
returns the Gram of Theorem 1. Sharing an inertia with `G_ns` is the
Theorem 3 comparison, not a reprint of `G_ns`.

The 1-seed / gram4 ticks `(3,2,3)` on the same sites produce a third
matrix `((8,5,8),(5,2,4),(8,4,6))`, also distinct from `G`.

## No-Go Discipline Gate

The negative statement gated here is only:

> The displayed Minkowski Gram and its signature are not adopted as
> framework structure and are not written into Admissibility.

It is not a no-go for a later metric construction, a later clock map, or
Lorentz emergence.

### N1 — Alternative routes

| Route | Status | Attempt and disposition |
|---|---|---|
| nsopp process tick enumeration | ATTEMPTED | Grow the opposite-lock seed on `B_3(0)` by perp-steps; the four events receive ticks `(0,3,3,2)`. |
| direct Minkowski expansion | ATTEMPTED | Expand all nine products from the four 4-vectors; the Gram is the matrix of Theorem 1. |
| unpivoted rational LDL | ATTEMPTED | Compute unit-lower `L` and diagonal `D` over `Fraction`; reconstruct `G` and read pivot signs. |
| leading-principal-minor inertia | ATTEMPTED | `(Δ1,Δ2,Δ3)=(8,-8,9)` has two sign changes from `(1,Δ1,Δ2,Δ3)` and no zero minor. |
| nsgram reprint test | ATTEMPTED | Replace nsopp ticks by `(2,1,2)`; the Gram becomes `G_ns ≠ G`, so the claim is not an nsgram clone. |
| 1-seed Gram reprint test | ATTEMPTED | Replace nsopp ticks by `(3,2,3)`; the Gram becomes `G_1 ≠ G`. |
| Euclidean-product mutation | ATTEMPTED | The positive-definite product `t_u t_v + x_u·x_v` on the same 4-vectors has LDL signature `(3,0,0)`, distinct from `(1,2,0)`. |
| seed-site contamination test | ATTEMPTED | The extra opposite-lock seed site `(0,1,0)` is not among `{A,D,B}` and is not used as a Gram vector. |

These are distinct process, expansion, inertia, reprint, mutation, and
support attacks. Each is closed by the algebra above and a corresponding
runner gate; no prior negative result is used as authority.

### N2 — Wall independence

There is no multi-wall impossibility claim. The four events, the nsopp
formation ticks, the Minkowski product, and the LDL signature are one
declared comparison contract, not independently claimed physical walls.

### N3 — Hidden-wall scan

The load-bearing conditions are explicit: four named events, nsopp-process
formation ticks on `B_3(0)`, the product `t_u t_v − x_u·x_v`, order
`(A,D,B)`, and unpivoted rational LDL. No hop-cost shortest-path fill or
Admissibility metric is used.

### N4 — Residual matching

No prior no-go, wall, or campaign is cited as a witness. The axiom memo
supplies only the lattice and admissibility sentences quoted above. The
formation ticks, the Gram entries, and the signature are closed directly
here.

### N5 — Rhetoric audit

The runner and note resolve the following exact granularities:

```text
per_element: all nine Gram entries and all three LDL pivots are evaluated as exact rationals
per_site: only the four named events O, A, D, B enter; the extra seed (0,1,0) is excluded from the Gram
per_mode: Minkowski versus Euclidean products are both computed; only the Minkowski product is the claim
per_block: the 3x3 Gram block of (u(A),u(D),u(B)) is the sole signature carrier
lattice_wide: checked and not executed — no lattice-wide metric, hop-cost fill, or Admissibility rewrite is claimed
```

The report is per four-event block. It is not upgraded to a lattice-wide
metric or a physical clock.

### N6 — Partial-closure paths

No new axiom is required to display this Gram. A later theory may adopt a
metric, a different tick assignment, or a larger event set. Those are live
construction paths, not forbidden escapes and not premises of this theorem.
Uniqueness is not required.

### N7 — Steelman

The strongest counterargument is that matching nsgram's `(1,2,0)` already
selects Minkowski inertia as framework structure, or that ticks `(3,3,2)`
were chosen to force the match. The first fails because Theorem 3 is a
comparison of displayed triples, not an adoption. The second fails because
the ticks are the nsopp-process formation list, the Gram is computed from
them rather than fitted, and the nsgram Gram is a different matrix with
the same inertia. A uniqueness or adoption theorem remains open.

### N8 — Cross-cycle echo

The nsgram four-event Gram is a same-day comparison input, not a proof
lemma and not a reprint. No previously retired wall is being revived: this
note closes only the nsopp four-event Gram/signature display and leaves
metric adoption open.

**Gate result:** the narrowly stated non-adoption boundary passes N1-N8.
This is a source-side scope check, not an audit verdict.

## What This Does Not Claim

- It does not fill ticks by hop-cost shortest path.
- It does not claim that `(1,2,0)` is the unique signature of these three
  sites under every tick assignment.
- It does not identify `G` with the nsgram Gram or with the 1-seed Gram.
- It does not attach L1, or any lock, to the four events.
- It does not adopt `G`, the Minkowski product, or the signature as
  framework structure.
- It does not write a metric into Admissibility.
- It does not edit Lattice, Qubit, Admissibility, Record, or any primitive.
- It does not use observational, fitted, or literature values.

## Exact Target And Obligation Graph

| Obligation | Disposition |
|---|---|
| bind the four events and nsopp-process formation ticks | declared and enumerated on `B_3(0)` |
| exclude the extra seed `(0,1,0)` from the three displacements | checked |
| compute the nine Minkowski Gram entries | proved in Theorem 1 |
| compute exact rational LDL and reconstruct `G` | proved in Theorem 2 |
| read the signature from pivot signs | proved `(1,2,0)` in Theorem 2 |
| compare with nsgram / gram4 `(1,2,0)` | proved equal in Theorem 3; displayed, not adopted |
| separate the nsgram reprint | `G ≠ G_ns` entrywise |
| protect the non-adoption boundary | committed N1-N8 record above |

The runner enumerates the nsopp process ticks, recomputes the Gram, the
LDL reconstruction, the minor sequence, the nsgram contrast, the 1-seed
contrast, and the Euclidean mutation. It does not treat source-text
presence as mathematical proof.

## Primary Runner

The paired runner performs exact rational checks of Theorems 1–3, the
nsgram non-reprint contrast, the 1-seed contrast, the Euclidean mutation,
the extra-seed exclusion, source-boundary pins, and note/runner agreement.
It writes no cache and edits no axiom file.
