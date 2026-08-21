---
claim_id: perpnn_four_event_minkowski_gram_signature_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Minkowski Gram signature of the three perpnn displacements from origin of axis, face, and body events is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_four_event_minkowski_gram_signature_2026_08_15.py
---

# Minkowski Gram Signature Of Three Perpnn Displacements

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact 3×3 Minkowski Gram of the displacements from origin of the
axis, face, and body events under displayed perpnn ticks, together with the
exact signature `(n+, n−, n0)` and the member-versus-3+1 comparison.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_four_event_minkowski_gram_signature_2026_08_15.py`](../scripts/perpnn_four_event_minkowski_gram_signature_2026_08_15.py)

## Result Up Front

Four events only. The recorded set is the recperp #7033 event list

```text
R = {O, A, D, B},
O = (0,0,0),   A = (1,0,0),   D = (1,1,0),   B = (1,1,1).
```

Displayed perpnn ticks from #7024, not recomputed by path dump:

```text
t(O) = 0,   t(A) = 3,   t(D) = 2,   t(B) = 3.
```

Clock is this displayed tick assignment. Uniqueness of the ticks is not
required. This display does not attach L1. No hop-cost is used.

The 4-vector of a site `x` in `R` is

```text
u(x) = (t(x), x_1, x_2, x_3).
```

The Minkowski product is

```text
u·v = t_u t_v − x_u·x_v.
```

Displacements from the origin event are `u(A)`, `u(D)`, `u(B)`, because
`u(O)=(0,0,0,0)`. The Gram `G` is the 3×3 matrix with

```text
G_ij = u_i · u_j
```

in the order `(A, D, B)`.

The nine exact entries are

```text
G = [[8, 5, 8],
     [5, 2, 4],
     [8, 4, 6]].
```

Exact rational LDL, with no float signature, yields diagonal

```text
D = diag(8, −9/8, −10/9).
```

The inertia of `D` is the signature of `G`:

```text
(n+, n−, n0) = (1, 2, 0).
```

That triple is `(1,2,0)`, not `(2,1,0)` and not other. Relative to the
displayed 3+1 Minkowski product on 4-vectors, whose coordinate signature is
`(1,3,0)`, the three displacements span a nondegenerate Lorentzian 3-plane,
which is the `(1,2,0)` member of 3+1 rather than a Euclidean `(0,3,0)`
3-plane. Displayed, not adopted.
The note does not write a metric into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The nine Gram entries and the exact rational signature of the three perpnn displacements close on the named four events; uniqueness of ticks, a physical time metric, and adoption into Admissibility remain outside the claim."
trace_class: upstream_support
target_claim_id: physical_lorentzian_clock_map
target_blocker_text: "display a Minkowski Gram signature on recorded events without writing a metric into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the Gram and signature displayed on the three displacements from origin; do not attach L1, do not dump paths, and do not adopt the signature as a metric."
conditional_surface_status: "exact for the named four-event set and displayed perpnn ticks; not adopted as a metric or uniqueness theorem"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise Boundary

The current Record axiom supplies formation, one locked admissible
possibility per present record, content-only readout, and unreadability at
absence. It does not supply a scalar collection functional, a uniqueness
theorem for ticks, or a spacetime metric.

The current Admissibility axiom supplies one fixed nearest-neighbor
probability rule, covariant under lattice translations and proper cubic
rotations. It does not define a time metric. This display therefore cannot
be written into Admissibility.

The four sites of `R` are ordinary points of `Z^3`. Occupancy of those four
sites, and the integers `t`, are named display data. They are not selected
by a formation dump, hop length, or shortest-path fill.

## Exact Objects

Let `R` and `t` be as above. Define

```text
u:R -> Z^4,     u(x) = (t(x), x_1, x_2, x_3),
u·v = t_u t_v − (x_u)_1 (x_v)_1 − (x_u)_2 (x_v)_2 − (x_u)_3 (x_v)_3.
```

The displacement list, in order, is `(u(A), u(D), u(B))`. The score domain is exactly `R`.
Signature is the inertia triple of `G`, read from exact
rational LDL (equivalently from the sign pattern of the leading principal
minors). No floating-point eigenvalue is used.

## Theorem 1 — Nine Exact Gram Entries

Direct evaluation of the Minkowski products gives

```text
u(A) = (3,1,0,0),
u(D) = (2,1,1,0),
u(B) = (3,1,1,1),
```

and

| `G_ij` | `A` | `D` | `B` |
|---|---:|---:|---:|
| `A` | `8` | `5` | `8` |
| `D` | `5` | `2` | `4` |
| `B` | `8` | `4` | `6` |

Explicitly:

```text
A·A = 3·3 − 1 = 8,
A·D = 3·2 − 1 = 5,
A·B = 3·3 − 1 = 8,
D·D = 2·2 − (1+1) = 2,
D·B = 2·3 − (1+1) = 4,
B·B = 3·3 − (1+1+1) = 6.
```

The matrix is symmetric. The diagonal equals the per-event squares
`t(x)^2 − |x|_2^2` on `A`, `D`, and `B`.

## Theorem 2 — Signature `(n+, n−, n0)`

Exact rational LDL of `G` with unit lower-triangular `L` produces

```text
L = [[1,     0,   0],
     [5/8,   1,   0],
     [1,     8/9, 1]],
D = diag(8, −9/8, −10/9),
G = L D L^T.
```

The diagonal signs are `+`, `−`, `−`, with no zero. Therefore

```text
(n+, n−, n0) = (1, 2, 0).
```

The same inertia is recovered from the leading principal minors

```text
Δ_1 = 8,    Δ_2 = −9,    Δ_3 = det(G) = 10,
```

whose sign pattern `+, −, +` has two changes and no vanishing minor.

## Theorem 3 — `(1,2,0)` Versus `(2,1,0)` Or Other, And Member Versus 3+1

The computed triple is `(1,2,0)`. It is not `(2,1,0)`. It is not other.

The displayed product on 4-vectors is the coordinate Minkowski form of
signature `(1,3,0)`. A nondegenerate 3-plane in that 3+1 space is a
Lorentzian member when its induced signature is `(1,2,0)`, and a Euclidean
member when the induced signature is `(0,3,0)`. Here `det(G)=10 ≠ 0`, so
the three displacements are linearly independent and span a Lorentzian
3-member of the displayed 3+1 product.

The comparison is reported. It is displayed, not adopted. It does not
select a physical metric, write an interval into Admissibility, or claim
that every tick assignment on `R` yields the same signature.

## Mutations That Stay Outside The Claim

On these four `{0,1}`-coordinate events the coordinate L1 length equals
`|x|_2^2`. That numerical coincidence is not a license to attach L1. The
spatial part of the product remains the Euclidean inner product.

A different tick assignment on the same four events can change the Gram
signature. The simultaneous assignment `t'(A)=t'(D)=t'(B)=0` produces the
purely spatial Gram `−[[1,1,1],[1,2,2],[1,2,3]]` with exact LDL diagonal
`(−1,−1,−1)` and signature `(0,3,0)`. Uniqueness of the displayed perpnn ticks is not required and is not claimed.

Path dump and shortest-path fill are not used. The ticks are the displayed
#7024 values.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| Record unreadability at absence | score domain is `R` only | current axiom memo |
| Admissibility does not define a time metric | forbids writing the display into Admissibility | current axiom memo |
| `R` as recperp #7033 events | displayed recorded events | named mathematical input |
| perpnn ticks from #7024 | displayed clock on `R` | named mathematical input; not a path dump |
| `u·v = t_u t_v − x_u·x_v` | Minkowski product | declared bilinear form |
| Gram order `(A,D,B)` | matrix presentation | declared order |
| space/time inertia of `G` | signature | exact rational LDL |

There are no measured, fitted, literature, or observational inputs. No
physical time metric is selected. No uniqueness theorem is claimed.

## Primary Runner

The paired runner builds the three displacements from the displayed ticks,
computes the nine exact Gram entries, reads the signature from exact
rational LDL and from principal minors, classifies `(1,2,0)` versus
`(2,1,0)` or other, compares that inertia to the 3+1 coordinate signature,
checks that a mutated tick assignment can change the signature, and pins
the current Record/Admissibility boundary together with the
displayed-not-adopted scope of the note.
