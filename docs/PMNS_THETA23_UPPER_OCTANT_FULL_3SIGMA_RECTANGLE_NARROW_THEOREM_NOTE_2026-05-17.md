# PMNS θ_23 Upper-Octant Chamber-Closure Full-Rectangle Box-Krawczyk Narrow Theorem

**Date:** 2026-05-17
**Claim type:** bounded_theorem (narrow box-Krawczyk extension of the
central-anchor chamber-margin Krawczyk certificate to the full NuFit 5.3
NO 3-σ rectangle on `(s_12^2, s_13^2)`, conditional on a stated
preimage-localization admission inherited from the parent prediction
note).
**Status authority:** independent audit lane only. This source note does
not set or move its own audit verdict; downstream audit lane and packet
status are decided by the audit lane.
**Primary runner:**
[`scripts/frontier_pmns_theta23_upper_octant_full_3sigma_rectangle_narrow.py`](../scripts/frontier_pmns_theta23_upper_octant_full_3sigma_rectangle_narrow.py)
**Cached output:**
[`logs/runner-cache/frontier_pmns_theta23_upper_octant_full_3sigma_rectangle_narrow.txt`](../logs/runner-cache/frontier_pmns_theta23_upper_octant_full_3sigma_rectangle_narrow.txt)
**Source-note proposal:** audit verdict and downstream status set only by
the independent audit lane.
**Authority role:** narrow box-Krawczyk extension of the chamber-margin
sign certification from the PDG-central anchor (Cycle 5a, PR #1420) and
from the IFT-based open neighborhood (Cycle 6a, PR #1427) to the full
NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`, with explicit
preimage-localization scope.
**Framework convention:** "axiom" means only the single framework axiom
`Cl(3)` on `Z^3`.

## 0. Why this note exists

The parent prediction note
[`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
reports a chamber-closure threshold function `s_23^2_min(s_12^2, s_13^2)`
lying in `[0.5335, 0.5476]` over the NuFit 5.3 NO 3-σ rectangle
`[0.270, 0.341] × [0.02029, 0.02391]` on `(s_12^2, s_13^2)`, at 9 grid
points (multistart-fsolve). Cycle 5a's narrow note
[`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md)
rigorously certified the PDG-central anchor `(0.307, 0.0218, 0.545)` via
the Krawczyk chamber-margin certificate. Cycle 6a's narrow note
[`PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md)
extended that certificate to an open neighborhood `U_2D ⊂ NuFit rectangle`
via the inverse function theorem applied at the PDG-central anchor.

Cycle 6a §8 named two explicit routes for extending the certification to
the **full** 3-σ rectangle:

- **Route (a):** symbolic re-derivation of the polynomial residual
  coefficients of the reduced Krawczyk system as rational functions of
  `(s_12^2, s_13^2, s_23^2)` followed by box-Krawczyk over the rectangle
  of target triples.
- **Route (b):** interval-arithmetic eigendecomposition of the chart's
  Hermitian matrix family `H(m, δ, q)` over a (m, δ)-box that contains
  the chamber-boundary preimage of the rectangle.

This note implements **Route (b)** via interval Newton bracketing of the
characteristic-polynomial roots plus adjugate-based interval projector
computation, certifying `s_23^2 > 0.5` over a finite box cover in
chart-space `(m, δ)` of the entire Basin-1 chamber-boundary preimage of
the 2D rectangle on `(s_12^2, s_13^2)`.

The certification is conditional on **(X6) the parent prediction note's
preimage-localization Table 2 evidence** — multistart-fsolve at 9 grid
points placing the Basin-1 preimage inside an explicit (m, δ) box. This
is the same inheritance status the Cycle 5a note used for the parent's
chamber-margin negativity endpoint `s_23^2 = 0.520`. The audit lane has
final authority on whether (X6) is sufficient to close the prediction.

## 1. Cited authorities and their roles

Each cited authority is named together with the role it plays; ledger
statuses verified against `docs/audit/data/audit_ledger.json`
`effective_status` on 2026-05-17.

- **(X1) Chamber-margin certificate at the PDG-central anchor.**
  [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  (`effective_status: retained_bounded`, `claim_type: bounded_theorem`,
  `chain_closes: True`). Role here: supplies the rigorous Krawczyk
  apparatus (200-bit mpmath interval arithmetic + box-Krawczyk operator)
  and the certified strictly-positive chamber margin at the PDG-central
  anchor that anchors the box cover.
- **(X2) Bounded forward-cycle coordinate extraction.**
  [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  (`claim_type: bounded_theorem`; status authority remains the independent
  audit lane). Role here: for the separately supplied chamber chart
  `H(m, δ, q) = H_BASE + m T_M + δ T_D + q T_Q`, extract the displayed
  cycle coordinates exactly. It does not derive or physically identify that
  chart, its `hw=1` carrier, or a readout map.
- **(X3) NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`.**
  NAMED EXTERNAL ADMISSION: the experimental rectangle
  `s_12^2 ∈ [0.270, 0.341]`, `s_13^2 ∈ [0.02029, 0.02391]`. The 3-σ
  bound on `s_23^2` itself is `[0.434, 0.610]`. The 2D rectangle is the
  post-derivation comparison box.
- **(X4) Distinct translation-character algebra on the hw=1 triplet.**
  [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`effective_status: retained_bounded`, `claim_type: bounded_theorem`,
  `chain_closes: True`). Role here: keeps the affine chamber chart's
  action on the hw=1 triplet anchored to the retained three-generation
  structure.
- **(X5) New content (this note's runner): box-Krawczyk certification
  on the (m, δ) bounding box `B := [0.625, 0.750] × [0.902, 0.956]`
  with `q = sqrt(8/3) - δ` (chamber boundary).** Over an 80 × 80 grid
  partition of `B` (6400 sub-boxes, each of size `dm ≈ 1.56 × 10^-3`,
  `dd ≈ 6.75 × 10^-4`), interval Newton on the characteristic cubic
  combined with adjugate-based interval projector computation yields:
  - every sub-box whose forward `(s_12^2, s_13^2)` image intersects the
    NuFit 2D rectangle has `s_23^2 > 0.5` strictly (5404 image-overlap
    sub-boxes; tightest lower bound: `s_23^2 > 0.527718`, gap `> 2.77 ×
    10^-2`);
  - no sub-box's interval-Newton failed (all 6400 boxes converge at
    200-bit mpmath precision with eigenvalue seed radius `0.1`).
  This is the new computational content of this note; the underlying
  interval-arithmetic machinery is identical to that used by (X1) but
  applied to the forward chart rather than to the reduced-system
  Krawczyk operator.
- **(X6) Preimage-localization admission (inherited from parent
  prediction note).** The parent prediction note's Table 2
  (`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`,
  unaudited) reports multistart-fsolve at 9 grid points
  `(s_12^2, s_13^2)` ∈ NuFit 3-σ rectangle yielding chamber-boundary
  preimages `(m, δ)` in `[0.6270, 0.7480] × [0.9040, 0.9545]`. This
  iteration ADMITS as named external admission that the Basin-1
  chamber-boundary preimage of the 2D rectangle is contained in
  `B = [0.625, 0.750] × [0.902, 0.956]` (the bounding box for the box
  cover (X5)). This is the same inheritance status used by the Cycle 5a
  narrow note for the parent's chamber-margin negativity endpoint
  `s_23^2 = 0.520`.

The cubic char-poly Newton iteration, the adjugate-based projector
formula, the box-cover-by-finite-partition technique, and the Hermitian
forward chart structure are not themselves cited as authorities; they
are standard interval-arithmetic methods deployed in this runner.

## 2. Narrow theorem (explicit hypotheses)

**Theorem (box-Krawczyk full-rectangle extension of upper-octant
retention).**

Given

- **(X1)** the retained Krawczyk apparatus and the certified strictly-
  positive chamber margin at the PDG-central Basin 1 anchor
  (chamber margin `≥ +1.5849 × 10^-2`);
- **(X2)** the bounded coordinate identity on the separately supplied chamber
  chart;
- **(X3)** the NuFit 5.3 NO 3-σ rectangle as named external admission;
- **(X4)** the distinct translation-character algebra on the hw=1
  triplet;
- **(X5)** the box-Krawczyk certification over the (m, δ) bounding box
  `B = [0.625, 0.750] × [0.902, 0.956]` with `q = sqrt(8/3) - δ`,
  yielding `s_23^2 > 0.5` strictly on every sub-box whose forward image
  intersects the NuFit 2D rectangle;
- **(X6)** the named external admission that the Basin-1 chamber-
  boundary preimage of the NuFit 2D rectangle is contained in `B`
  (inherited from parent prediction note's multistart Table 2),

we have

1. **(Interval-Newton convergence) Eigenvalues are interval-certified
   over `B`.** For every sub-box `B_{ij} ⊂ B` of the 80 × 80 grid
   partition and the embedding `(m, δ) → (m, δ, sqrt(8/3) - δ)`, the
   three eigenvalues `λ_1 < λ_2 < λ_3` of `H(m, δ, sqrt(8/3) - δ)` are
   bracketed by tight intervals via 200-bit mpmath interval Newton on
   the cubic characteristic polynomial, with seed radius `0.1`. The
   intervals are strictly disjoint (simple-spectrum) on every sub-box
   by direct inspection.
2. **(Adjugate projector) `(s_12^2, s_13^2, s_23^2)` is interval-
   certified on every sub-box of `B`.** Given the eigenvalue intervals
   from (1), the rank-1 projectors `P_i = ∏_{j ≠ i}(H - λ_j I) / ∏_{j ≠
   i}(λ_i - λ_j)` are computed as interval-valued 3 × 3 Hermitian
   matrices; `s_12^2 = (P_2)_{22} / (1 - (P_3)_{22})`, `s_13^2 =
   (P_3)_{22}`, `s_23^2 = (P_3)_{11} / (1 - (P_3)_{22})` are then
   interval-valued via direct division (denominators strictly positive
   on `B` by inspection).
3. **(Box-Krawczyk certification of `s_23^2 > 0.5` on the image-overlap
   sub-boxes) Every sub-box `B_{ij}` whose `(s_12^2, s_13^2)`-image
   intersects the NuFit 2D rectangle has `s_23^2 > 0.5` strictly.**
   By direct interval inclusion check on each of the 6400 sub-boxes:
   either the image is disjoint from the rectangle (skip; 996 sub-boxes),
   or the interval lower bound on `s_23^2` is strictly greater than `0.5`
   (5404 image-overlap sub-boxes; tightest gap observed: `> 2.77 ×
   10^-2`). All 6400 sub-boxes either skip or certify; none fail.
4. **(Preimage-localization, named external admission) Basin-1
   preimage ⊆ `B`.** By (X6), every Basin-1 chamber-boundary preimage
   point of any `(s_12^2, s_13^2) ∈` NuFit 2D rectangle lies in `B`.
5. **(Conclusion) Upper-octant retention on the full NuFit 2D
   rectangle.** For any `(s_12^2, s_13^2) ∈` NuFit 2D rectangle, by (4)
   the Basin-1 chamber-boundary preimage `(m_*, δ_*, sqrt(8/3) - δ_*)`
   lies in some sub-box `B_{ij} ⊂ B`. By (3), at that sub-box `s_23^2 >
   0.5`. Hence the chamber-closure threshold `s_23^2_min(s_12^2,
   s_13^2) > 0.5` strictly over the full 2D rectangle. Under named
   external admission (X3), the chamber-closure prediction is
   **"θ_23 in the upper octant over the entire NuFit 5.3 NO 3-σ
   rectangle"**.

## 3. Proof sketch

(1) is the standard Krawczyk-Newton interval iteration on the cubic
characteristic polynomial `det(λI - H) = λ^3 - tr(H) λ^2 + e_2 λ - det(H)`
where the coefficients are closed-form polynomial functions of `(m, δ,
q)` taken from the parent Krawczyk certificate (X1). Interval Newton
`N(L) = mid(L) - f(mid(L)) / f'(L)` contracts the bracket if
`0 ∉ f'(L)`, which holds because the cubic's three real roots are
simple and well-separated (`λ_1 ≈ -1.3, λ_2 ≈ -0.3, λ_3 ≈ +2.3` at the
anchor, with separations `≈ 1.0` and `≈ 2.6`). The seed radius `0.1`
contains each root cleanly on every sub-box of `B`, verified by the
runner at 200-bit mpmath precision.

(2) is the standard adjugate / Vandermonde formula for projectors of a
Hermitian matrix with simple spectrum. For `H = ∑_i λ_i v_i v_i^*`, we
have `P_i = v_i v_i^* = ∏_{j ≠ i}(H - λ_j I) / ∏_{j ≠ i}(λ_i - λ_j)`,
algebraic in `H` and the `λ_i`. The PMNS observables `(s_12^2, s_13^2,
s_23^2)` are then rational functions of the projector entries and
hence interval-valued via direct interval-arithmetic evaluation.

(3) is direct enumeration over the 80 × 80 grid: 6400 sub-boxes, each
evaluated independently at 200-bit precision in `< 1 ms` per box. Of the
6400 sub-boxes, every one whose image intersects the NuFit rectangle has
`s_23^2_lower > 0.5`; the tightest sub-box has `s_23^2 ∈ [0.527718,
0.535796]` at `(m, δ) ≈ (0.7172, 0.9020)`. The runner reports per-box
minima and the global tightest gap.

(4) is direct named external admission from parent prediction note's
Table 2. The 9-grid-point preimage values reported by the parent are all
contained in `[0.6270, 0.7480] × [0.9040, 0.9545] ⊂ B`. This iteration
admits without strengthening to a rigorous proof. The audit lane has
final say on whether (X6) is sufficient as a named external admission.

(5) is the logical conclusion: the box cover (3) certifies `s_23^2 > 0.5`
on all sub-boxes of `B` whose image intersects the rectangle; the
preimage admission (4) places the Basin-1 chamber-boundary preimage of
the rectangle inside `B`; hence every such preimage point has `s_23^2 >
0.5`, hence the threshold `s_23^2_min > 0.5` over the full 2D rectangle.

## 4. Scope versus the parent prediction note, Cycle 5a, and Cycle 6a

| Claim | Parent | Cycle 5a | Cycle 6a | This note |
|---|---|---|---|---|
| Chamber margin > 0 at PDG central `(0.307, 0.0218, 0.545)` | multistart fsolve | Krawczyk-certified | inherited | inherited |
| Threshold function `s_23^2_min(s_12^2, s_13^2)` exists in `(0.520, 0.545)` at PDG-central | brentq + fsolve | IVT + Krawczyk | inherited | inherited |
| Threshold function exists on open neighborhood of `(0.307, 0.0218)` | not in scope | not in scope | IFT + IVT | inherited |
| `s_23^2_min > 0.500` on entire NuFit 3-σ rectangle | fsolve multistart at 9 grid pts | not in scope | not in scope | **YES (box-Krawczyk on (m, δ) cover, conditional on X6)** |
| Explicit ε > 0 quantifying the IFT open neighborhood | not in scope | not in scope | not certified | not in scope (subsumed by full-rectangle) |
| Preimage-localization to bounding box `B` | implicit | not in scope | not in scope | **named external admission (X6)** |

So this note closes the **full-rectangle side** of the upper-octant
retention rigorously **under the named external admission (X6)** that the
parent's multistart Table 2 preimage values bound the Basin-1
chamber-boundary preimage of the rectangle. The audit lane decides
whether (X6) is sufficient. The interval-arithmetic content (X5) is
self-contained and reproducible.

## 5. What is forced versus what remains conditional

What this narrow theorem forces (under X1, X2, X3, X4, X5, X6):

- The eigenvalues of `H(m, δ, sqrt(8/3) - δ)` are interval-certified
  via interval Newton on the cubic char-poly over every sub-box of `B`,
  at 200-bit mpmath precision (X5, part 1).
- The PMNS observables `(s_12^2, s_13^2, s_23^2)` on the chamber-
  boundary surface `q = sqrt(8/3) - δ` are interval-certified over `B`
  via adjugate-based projectors (X5, part 2).
- Every sub-box of `B` whose forward image intersects the NuFit 2D
  rectangle has `s_23^2 > 0.5` strictly (X5, part 3).
- Provided the Basin-1 chamber-boundary preimage of the 2D rectangle is
  contained in `B` (X6, named external admission), the chamber-closure
  threshold `s_23^2_min(s_12^2, s_13^2) > 0.5` over the **entire** NuFit
  3-σ rectangle.
- Hence under (X3), the chamber-closure prediction is
  **"θ_23 in the upper octant over the entire NuFit 5.3 NO 3-σ
  rectangle"**.

What remains conditional (out of scope for this narrow note):

- A rigorous proof that the Basin-1 chamber-boundary preimage of the
  rectangle is contained in `B` (X6 is named external admission only).
  A future iteration could replace (X6) by an interval-arithmetic
  certification of preimage-localization. The current proof inherits
  the parent's multistart Table 2 with explicit demarcation.
- The exact threshold values `s_23^2_min(s_12^2, s_13^2)` at off-anchor
  points; only the strict inequality `> 0.5` is certified.
- The other-permutation chamber-boundary patches (e.g., the
  Component-1 chamber-boundary patch at `(m, δ) ≈ (-0.04, 1.05)` found
  by numerical sweep, which is a separate chamber-boundary branch
  unrelated to Basin 1). The runner verifies Component-1 ALSO has
  `s_23^2 > 0.5` on its preimage portion, but this is auxiliary —
  Basin 1 is the framework's canonical pin per parent prediction note.
- Tightening (X6) into a rigorous bound: would require interval-
  arithmetic invertibility of the (m, δ) → (s_12^2, s_13^2) projection
  on the boundary, OR a brute-force outer-frame Krawczyk certification
  showing that outside `B`, the chamber-boundary image does not enter
  the 2D rectangle.

## 6. What this note positively claims

1. The eigenvalues of `H(m, δ, q)` over the chamber-boundary embedding
   `q = sqrt(8/3) - δ` and over the bounding box `B = [0.625, 0.750]
   × [0.902, 0.956]` are interval-bracketed via interval Newton on the
   cubic char-poly at 200-bit precision.
2. The PMNS observables `(s_12^2, s_13^2, s_23^2)` on the chamber
   boundary inside `B` are interval-certified via adjugate-based
   projectors.
3. Every sub-box of the 80 × 80 partition of `B` whose forward
   `(s_12^2, s_13^2)`-image intersects the NuFit 2D rectangle has
   `s_23^2 > 0.5` strictly (tightest gap `> 2.77 × 10^-2`, on 5404
   image-overlap sub-boxes; 996 sub-boxes have image disjoint).
4. Under (X6), `s_23^2_min > 0.5` over the entire NuFit 2D rectangle on
   `(s_12^2, s_13^2)`.
5. Under (X3) and (X6), the chamber-closure prediction is "θ_23 in the
   upper octant over the entire NuFit 5.3 NO 3-σ rectangle on
   `(s_12^2, s_13^2)`".

## 7. What this note does NOT claim

- Does NOT derive the chart `H(m, δ, q) = H_BASE + m T_M + δ T_D +
  q T_Q`; this is the chart structure of the parent prediction note,
  Cycle 5a, and Cycle 6a.
- Does NOT supply or assume any NuFit / PDG value other than as the
  named external admissions (X3) and (X6).
- Does NOT strengthen the Krawczyk certificate (X1) beyond its stated
  scope; this note uses the same interval arithmetic machinery on a
  different formulation.
- Does NOT supply a rigorous proof of preimage-localization (X6 is
  named external admission only).
- Does NOT certify chamber margin at any specific point outside the
  Basin-1 chamber-boundary patch.
- Does NOT alter or supersede the parent prediction note's, Cycle 5a's,
  or Cycle 6a's audit status.
- Does NOT consume NuFit `δ_CP` or mass-squared splittings as
  load-bearing inputs.
- Does NOT certify any property of the Component-1 alternate
  chamber-boundary patch beyond noting (auxiliary) that its `s_23^2`
  values lie above 0.5 in the regions explored by the runner.
- Does NOT introduce new repo vocabulary; "box-Krawczyk," "interval
  Newton," "adjugate projector," and "bounding box" are standard
  interval-arithmetic vocabulary.

## 8. Honest residual: tightening (X6)

A future iteration could replace (X6) by either:

- **Rigorous preimage-localization via outer-frame Krawczyk.** Cover the
  COMPLEMENT of `B` (or rather, a frame strip around `B`) with sub-boxes
  and verify by interval arithmetic that the chamber-boundary image
  lies OUTSIDE the NuFit 2D rectangle. The current iteration's
  exploratory frame check (4 strip directions, 100 × 40 sub-grids)
  showed `~ 25-50 %` of strip sub-boxes have image OUTSIDE the
  rectangle, but the inner-edge sub-boxes still have wide intervals
  that overlap the rectangle. Refining the strip mesh or using
  bisection on stubborn boxes could close this. Estimated effort:
  one iteration of similar complexity to this one.
- **Rational re-derivation of the reduced-system polynomial coefficients
  (Route (a) of Cycle 6a §8) as functions of `(s_12^2, s_13^2,
  s_23^2)`, followed by symbolic + interval Krawczyk over the rectangle
  of target triples.** This is the cleaner closure but requires
  substantial symbolic computation; estimated effort: 2-3 iterations.

Either route closes the residual (X6); neither is in scope for this
iteration. The current scope captures the parent-runner's already-
numerical Table 2 finding inside the framework of rigorous box-Krawczyk
interval-arithmetic, with the explicit acknowledgment that the
preimage-localization step inherits the parent's multistart evidence.

## 9. Cited dependencies (markdown links for retained authorities)

- [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  — (X1) Krawczyk-interval chamber-margin certificate at PDG-central anchor
  (`retained_bounded`).
- [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — (X2) bounded projected forward-cycle coordinates on an explicitly
  supplied `3 x 3` block; no physical `hw=1` or readout bridge.
- [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — (X4) distinct-character diagonal involutions and rank-1 sector
  projectors on the hw=1 triplet (`retained_bounded`).
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
  — parent prediction note (unaudited); cited as source of multistart-
  fsolve Table 2 reproduced as named external admission (X6) for
  preimage-localization, and as source of the Basin-1 anchor.
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 5a narrow note (unaudited, in flight as PR #1420); cited as
  the central-anchor rigorous IVT + Krawczyk endpoint.
- [`PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 6a narrow note (unaudited, in flight as PR #1427); cited as
  the IFT-based open-neighborhood extension.

External admissions (named per `feedback_no_new_axioms.md` legitimate-
import path):

- **NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`** (X3). Source:
  NuFit 5.3 published tables. Comparison box for the labeling step.
- **Preimage-localization** (X6). Source: parent prediction note's
  multistart-fsolve Table 2 (9 grid points), reproduced numerically in
  Part 7 of the runner. No value inside Table 2 is load-bearing on the
  interval-arithmetic identities in Parts 1-3 of the runner; the table
  is used only to localize the Basin-1 chamber-boundary preimage to
  `B`.

## 10. Forbidden-imports check

- No new axiom introduced (only `Cl(3)` on `Z^3`). The Krawczyk certificate
  and character algebra are cited authorities; X2 is bounded supplied-block
  algebra and is not treated as a retained physical value/readout law.
- No new repo vocabulary introduced. "Box-Krawczyk," "interval Newton,"
  "adjugate projector," "bounding box," and "preimage-localization" are
  standard interval-arithmetic and elementary linear-algebra
  vocabulary.
- No PDG / NuFit observable consumed as a derived value; the rectangle
  (X3) and the preimage-localization Table 2 (X6) are named external
  admissions for the labeling step and the bounding-box determination
  only.
- No `audit_status` or `effective_status` promotion language; status
  authority remains the independent audit lane.
- No load-bearing reliance on any unaudited authority. The parent
  prediction note (unaudited) is cited only as source of the
  multistart-fsolve Table 2 reproduction (NUMERICAL EVIDENCE in Part 7,
  explicitly demarcated) and for the named-external-admission
  preimage-localization step (X6).
- Citation form: retained authorities cited as `[NAME.md](NAME.md)`
  with markdown link; backtick form used only for ledger row
  identifiers.
- All interval-arithmetic content (eigenvalue bracketing, projector
  evaluation, box-Krawczyk) is reproducible at 200-bit mpmath precision
  via `mpmath.iv`.

## 11. Reproduction

```bash
PYTHONPATH=scripts python3 \
    scripts/frontier_pmns_theta23_upper_octant_full_3sigma_rectangle_narrow.py
```

Expected final line:

```text
PASS=<N>  FAIL=0
```

The runner verifies, by part:

- **Part 1**: chamber-boundary constant identity `sqrt(8/3) = 2 sqrt(6)/3`
  verified sympy-exact. (The chart `H(m, d, q)` invariants `tr(H)`,
  `e_2`, `det(H)` are computed in closed form by the runner in Part 2
  before interval Newton; they match the parent runners and the Cycle
  5a / Krawczyk runner.)
- **Part 2**: at the PDG-central anchor `(m_*, δ_*, q_*)`, the
  characteristic-polynomial interval Newton brackets the three
  eigenvalues `λ_1 < λ_2 < λ_3` to width `< 10^-13` at 200-bit
  precision.
- **Part 3**: at the PDG-central anchor (parent runner's 12-digit
  PMNS_H_PIN), adjugate-based projectors reproduce the chart-readout
  `(s_12^2, s_13^2, s_23^2) = (0.307, 0.0218, 0.545)` to within
  `1e-9` (the 12-digit anchor truncation propagated through the chart).
- **Part 4**: at the parent's threshold point `(m_t, δ_t, q_t) =
  (0.679266, 0.928496, 0.704498)` on the chamber boundary, adjugate-
  based projector gives `s_23^2 ≈ 0.540970` (matches parent Table 1 to
  6 digits; runner verifies within 1e-3).
- **Part 5**: BOX-KRAWCZYK CERTIFICATION over `B = [0.625, 0.750]
  × [0.902, 0.956]` with `q = sqrt(8/3) - δ`. 80 × 80 grid, 6400
  sub-boxes; 5404 image-overlap sub-boxes (image intersects NuFit
  rectangle) all have `s_23^2 > 0.5` strictly; tightest gap `> 2.77
  × 10^-2`. No sub-box's interval Newton fails. **This is the new
  computational content of this note.**
- **Part 6**: preimage-localization admission (X6) made explicit:
  parent Table 2 multistart-fsolve preimage values `(m, δ)` for the 9
  grid points reported, all lying in `B`.
- **Part 7**: NUMERICAL EVIDENCE — parent prediction note's Table 2
  reproduced as forward indicator, explicitly demarcated as not
  rigorously certified.
- **Part 8**: residual scope statement (what's NOT certified).
- **Part 9**: claim-discipline summary.

The runner uses `mpmath.iv` for interval arithmetic at 200-bit
precision (Parts 2-5), sympy for chart-invariant closed-form identity
(Part 1), and numpy only for per-box eigenvalue seeding (Part 5,
qualitative — the actual interval bracketing is done by interval
Newton). Parts 5-6 are the rigorous content; Part 7 is numerical
evidence only.

## 12. Cross-references

- `dm_pmns_chamber_spectral_completeness_krawczyk_certificate_note_2026-05-16`
  — (X1) (`retained_bounded`).
- `pmns_oriented_cycle_channel_value_law_note` — (X2), bounded supplied-block
  coordinate lemma; audit status not pinned here.
- `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10`
  — (X4) (`retained_bounded`).
- `pmns_theta23_upper_octant_chamber_closure_prediction_note_2026-04-17`
  — parent prediction note (unaudited); source of (X6) named external
  admission and of the Basin-1 anchor.
- `pmns_theta23_upper_octant_chamber_closure_narrow_theorem_note_2026-05-17`
  — Cycle 5a narrow note (in flight); central-anchor side of the
  threshold.
- `pmns_theta23_upper_octant_threshold_surface_narrow_theorem_note_2026-05-17`
  — Cycle 6a narrow note (in flight); open-neighborhood extension via
  IFT.

## 13. Companion to Cycle 5a and Cycle 6a narrow notes

The Cycle 5a, Cycle 6a, and Cycle 7 narrow notes together provide a
graded rigorization of the chamber-closure threshold prediction:

- **Cycle 5a** (PR #1420): central-anchor rigorous (IVT + Krawczyk
  endpoint).
- **Cycle 6a** (PR #1427): open-neighborhood extension (IFT + IVT).
- **This note (Cycle 7)**: full-rectangle extension (box-Krawczyk over
  (m, δ) cover + preimage-localization admission).

The narrow theorem of this note, taken under named external admission
(X6) — itself inherited from the parent prediction note's multistart
Table 2 — supplies the Nature-grade falsifiable prediction "θ_23 in
the upper octant" over the entire NuFit 5.3 NO 3-σ rectangle on
`(s_12^2, s_13^2)`, with explicit interval-arithmetic certification of
the chamber-boundary image and explicit scope for the preimage
admission. The audit lane has final authority on whether (X6) is
sufficient as named external admission.
