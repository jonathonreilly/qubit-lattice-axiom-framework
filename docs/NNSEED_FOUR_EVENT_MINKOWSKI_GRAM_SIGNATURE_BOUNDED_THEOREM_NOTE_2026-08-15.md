---
claim_id: nnseed_four_event_minkowski_gram_signature_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Minkowski Gram signature of the three nnseed displacements from origin of axis, face, and body events is reported versus gram4 (1,2,0). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_four_event_minkowski_gram_signature_2026_08_15.py
---

# Minkowski Gram Signature Of Three Nnseed Displacements

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact 3×3 Minkowski Gram of three displayed four-event
displacements under displayed nnseed ticks, with signature by exact
rational LDL. The Gram and signature are displayed, not adopted. No
metric is written into Admissibility. Uniqueness is not required. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_four_event_minkowski_gram_signature_2026_08_15.py`](../scripts/nnseed_four_event_minkowski_gram_signature_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Four events only, with sites as in the gram4 four-event list and with
displayed nnseed ticks (not recomputed by a path dump):

```text
O = (0,0,0),   t(O) = 0,
A = (1,0,0),   t(A) = 2,
D = (1,1,0),   t(D) = 1,
B = (1,1,1),   t(B) = 2.
```

The two-site nnseed includes the extra seed site `(0,1,0)`. That site is
not one of the three displacements from the origin used here.

The 4-vector of a site `x` is `u(x) = (t(x), x_1, x_2, x_3)`. The Minkowski
product is

```text
u · v = t_u t_v − x_u · x_v.
```

Let `G` be the 3×3 Gram of `(u(A), u(D), u(B))`. Exact arithmetic gives

```text
G = (( 3,  1,  3),
     ( 1, -1,  0),
     ( 3,  0,  1)).
```

Exact rational LDL yields diagonal pivots `(3, -4/3, -5/4)` and signature

```text
(n+, n−, n0) = (1, 2, 0).
```

That triple equals the displayed gram4 comparison value `(1, 2, 0)`. The
equality is a signature comparison only. The nine Gram entries are not
the 1-seed Gram: the 1-seed HOLD ticks on the same three sites are
`t(A,D,B)=(3,2,3)`, whose Gram is `((8,5,8),(5,2,4),(8,4,6))`. This note
is therefore not a 1-seed Gram clone. The common signature is displayed,
not adopted as a spacetime metric, and is not written into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact four-event Minkowski Gram entries and exact rational LDL signature are proved on displayed nnseed ticks; metric adoption and Admissibility edits remain outside the claim."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "report the 3x3 Minkowski Gram signature of axis, face, and body displacements under nnseed ticks versus gram4 (1,2,0)"
source_of_blocker_text: handoff
reachability_to_target: advances
next_trace_action: "Use this result only as a displayed four-event Gram/signature lemma; do not adopt a metric or attach L1."
artifact_role: theorem
conditional_surface_status: "exact on the four displayed events and displayed nnseed ticks; not adopted as framework structure"
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
- **Displayed tick input:** `t(O,A,D,B)=(0,2,1,2)` is the nnseed reverse/face
  HOLD tick list on these four events. The runner does not grow a formation
  process and does not dump paths.
- **Displayed comparison input:** gram4 reports signature `(1,2,0)` on
  1-seed HOLD ticks of the same three displacements. That triple is a
  comparison target, not a derived lemma of this note.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** a spacetime metric, a clock map, a lock
  attachment, and any Admissibility rewrite remain outside the target.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float
is used in the Gram, the LDL pivots, or the signature count.

```text
u(A) = (2, 1, 0, 0),
u(D) = (1, 1, 1, 0),
u(B) = (2, 1, 1, 1).
```

`G_ij = u_i · u_j` in the order `(A,D,B)`. A unit-lower-triangular `L` and
diagonal `D` satisfy `G = L D L^T` over the rationals whenever the
successive Schur pivots are computed without float rounding. The signature
`(n+, n−, n0)` is the count of strictly positive, strictly negative, and
zero diagonal entries of `D`. By Sylvester inertia this is the inertia of
`G`.

Leading principal minors of `G` are an independent exact cross-check:

```text
Δ1 = 3,     Δ2 = -4,     Δ3 = det(G) = 5.
```

The sequence `(1, Δ1, Δ2, Δ3)` has two sign changes and no zero, hence
again `(n+, n−, n0)=(1,2,0)`.

## Theorem 1 — The Nine Exact Gram Entries

Direct expansion of the Minkowski product yields

```text
u(A)·u(A) = 4 − 1 = 3,
u(A)·u(D) = 2 − 1 = 1,
u(A)·u(B) = 4 − 1 = 3,
u(D)·u(D) = 1 − 2 = −1,
u(D)·u(B) = 2 − 2 = 0,
u(B)·u(B) = 4 − 3 = 1.
```

Symmetry of the product gives the remaining three entries. Therefore

```text
G = (( 3,  1,  3),
     ( 1, -1,  0),
     ( 3,  0,  1)).
```

These nine values are the claim of Theorem 1. They are not imported from
the 1-seed Gram.

## Theorem 2 — Signature From Exact Rational LDL

The unpivoted rational LDL of `G` is

```text
L = ((1,   0,  0),
     (1/3, 1,  0),
     (1,   3/4, 1)),
D = diag(3, −4/3, −5/4).
```

The first pivot is `D_11 = G_AA = 3`. The Schur complement in the
`(D,B)` block then produces `D_22 = −4/3` and `D_33 = −5/4`. Direct
multiplication recovers `L D L^T = G`. The product of the pivots is
`3 · (−4/3) · (−5/4) = 5 = det(G)`.

The pivot signs are one positive and two negative, with no zero, so

```text
(n+, n−, n0) = (1, 2, 0).
```

## Theorem 3 — Comparison With Gram4 Signature `(1,2,0)`

The displayed gram4 signature on 1-seed HOLD ticks is `(1,2,0)`. The
nnseed signature of Theorem 2 equals that triple:

```text
(1, 2, 0) = (1, 2, 0).
```

The equality is displayed, not adopted. It does not write a metric into
Admissibility, does not select a clock, and does not attach L1. It also
does not claim uniqueness: the 1-seed Gram on the same three sites is a
different matrix with the same inertia, so the signature does not name a
unique Gram.

## Not A 1-Seed Gram Clone

On the same sites, the displayed 1-seed HOLD ticks are `t(A)=3`,
`t(D)=2`, `t(B)=3`, with

```text
u_1(A) = (3, 1, 0, 0),
u_1(D) = (2, 1, 1, 0),
u_1(B) = (3, 1, 1, 1),
G_1 = ((8, 5, 8),
       (5, 2, 4),
       (8, 4, 6)).
```

`G ≠ G_1` entrywise. The nnseed calculation uses ticks `(2,1,2)` and
returns the Gram of Theorem 1. Sharing an inertia with `G_1` is the
Theorem 3 comparison, not a reprint of `G_1`.

## No-Go Discipline Gate

The negative statement gated here is only:

> The displayed Minkowski Gram and its signature are not adopted as
> framework structure and are not written into Admissibility.

It is not a no-go for a later metric construction, a later clock map, or
Lorentz emergence.

### N1 — Alternative routes

| Route | Status | Attempt and disposition |
|---|---|---|
| direct Minkowski expansion | ATTEMPTED | Expand all nine products from the four displayed 4-vectors; the Gram is the matrix of Theorem 1. |
| unpivoted rational LDL | ATTEMPTED | Compute unit-lower `L` and diagonal `D` over `Fraction`; reconstruct `G` and read pivot signs. |
| leading-principal-minor inertia | ATTEMPTED | `(Δ1,Δ2,Δ3)=(3,-4,5)` has two sign changes from `(1,Δ1,Δ2,Δ3)` and no zero minor. |
| 1-seed Gram reprint test | ATTEMPTED | Replace nnseed ticks by `(3,2,3)`; the Gram becomes `G_1 ≠ G`, so the claim is not a 1-seed clone. |
| Euclidean-product mutation | ATTEMPTED | The positive-definite product `t_u t_v + x_u·x_v` on the same 4-vectors has LDL signature `(3,0,0)`, distinct from `(1,2,0)`. |
| seed-site contamination test | ATTEMPTED | The extra nnseed site `(0,1,0)` is not among `{A,D,B}` and is not used as a Gram vector. |

These are distinct expansion, inertia, reprint, mutation, and support
attacks. Each is closed by the algebra above and a corresponding runner
gate; no prior negative result is used as authority.

### N2 — Wall independence

There is no multi-wall impossibility claim. The four events, the displayed
ticks, the Minkowski product, and the LDL signature are one declared
comparison contract, not independently claimed physical walls.

### N3 — Hidden-wall scan

The load-bearing conditions are explicit: four named events, displayed
nnseed ticks, the product `t_u t_v − x_u·x_v`, order `(A,D,B)`, and
unpivoted rational LDL. No formation-path dump, hop-cost shortest-path
rule, or Admissibility metric is used.

### N4 — Residual matching

No prior no-go, wall, or campaign is cited as a witness. The axiom memo
supplies only the lattice and admissibility sentences quoted above. The
Gram entries and the signature are closed directly here.

### N5 — Rhetoric audit

The runner and note resolve the following exact granularities:

```text
per_element: all nine Gram entries and all three LDL pivots are evaluated as exact rationals
per_site: only the four named events O, A, D, B enter; the extra seed (0,1,0) is excluded from the Gram
per_mode: Minkowski versus Euclidean products are both computed; only the Minkowski product is the claim
per_block: the 3x3 Gram block of (u(A),u(D),u(B)) is the sole signature carrier
lattice_wide: checked and not executed — no lattice-wide metric, formation growth, or Admissibility rewrite is claimed
```

The report is per four-event block. It is not upgraded to a lattice-wide
metric or a physical clock.

### N6 — Partial-closure paths

No new axiom is required to display this Gram. A later theory may adopt a
metric, a different tick assignment, or a larger event set. Those are live
construction paths, not forbidden escapes and not premises of this theorem.
Uniqueness is not required.

### N7 — Steelman

The strongest counterargument is that matching gram4's `(1,2,0)` already
selects Minkowski inertia as framework structure, or that ticks `(2,1,2)`
were chosen to force the match. The first fails because Theorem 3 is a
comparison of displayed triples, not an adoption. The second fails because
the ticks are the displayed nnseed HOLD list, the Gram is computed from
them rather than fitted, and the 1-seed Gram is a different matrix with
the same inertia. A uniqueness or adoption theorem remains open.

### N8 — Cross-cycle echo

The 1-seed four-event Gram is a same-day comparison input, not a proof
lemma and not a reprint. No previously retired wall is being revived: this
note closes only the nnseed four-event Gram/signature display and leaves
metric adoption open.

**Gate result:** the narrowly stated non-adoption boundary passes N1-N8.
This is a source-side scope check, not an audit verdict.

## What This Does Not Claim

- It does not recompute nnseed formation, grow a ball, or dump paths.
- It does not claim that `(1,2,0)` is the unique signature of these three
  sites under every tick assignment.
- It does not identify `G` with the 1-seed Gram.
- It does not attach L1, or any lock, to the four events.
- It does not adopt `G`, the Minkowski product, or the signature as
  framework structure.
- It does not write a metric into Admissibility.
- It does not edit Lattice, Qubit, Admissibility, Record, or any primitive.
- It does not use observational, fitted, or literature values.

## Exact Target And Obligation Graph

| Obligation | Disposition |
|---|---|
| bind the four events and displayed nnseed ticks | declared; not recomputed |
| exclude the extra seed `(0,1,0)` from the three displacements | checked |
| compute the nine Minkowski Gram entries | proved in Theorem 1 |
| compute exact rational LDL and reconstruct `G` | proved in Theorem 2 |
| read the signature from pivot signs | proved `(1,2,0)` in Theorem 2 |
| compare with gram4 `(1,2,0)` | proved equal in Theorem 3; displayed, not adopted |
| separate the 1-seed Gram clone | `G ≠ G_1` entrywise |
| protect the non-adoption boundary | committed N1-N8 record above |

The runner recomputes the Gram, the LDL reconstruction, the minor
sequence, the 1-seed contrast, and the Euclidean mutation. It does not
treat source-text presence as mathematical proof.

## Primary Runner

The paired runner performs exact rational checks of Theorems 1–3, the
1-seed non-clone contrast, the Euclidean mutation, the extra-seed
exclusion, source-boundary pins, and note/runner agreement. It writes no
cache and edits no axiom file.
