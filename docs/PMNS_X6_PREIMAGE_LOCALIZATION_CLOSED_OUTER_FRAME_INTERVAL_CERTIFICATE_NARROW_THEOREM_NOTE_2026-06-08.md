# (X6) Preimage-Localization Closed: an Outer-Frame Interval Certificate that the Basin-1 Chamber-Boundary Preimage of the NuFit Rectangle Is Contained in Box `B` — Narrow Theorem

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Scope:** retires the named (X6) preimage-localization admission under the headline δ_CP forecast
P1 ([`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17`](PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)),
its **(X6) preimage-localization** — previously a multistart-fsolve "named external admission" (9 grid
points). Adds no axiom and no fitted value.
**Primary runner:**
[`scripts/pmns_x6_preimage_localization_outer_frame_certificate_2026_06_08.py`](../scripts/pmns_x6_preimage_localization_outer_frame_certificate_2026_06_08.py)
(reuses the P1 note's 200-bit `mpmath.iv` machinery; PASS=2 — S0 anchor-in-rect, S1 all 12167 shell
sub-boxes certified disjoint from the NuFit rectangle).
**Cached output:**
[`logs/runner-cache/pmns_x6_preimage_localization_outer_frame_certificate_2026_06_08.txt`](../logs/runner-cache/pmns_x6_preimage_localization_outer_frame_certificate_2026_06_08.txt).

## What (X6) was, and what this closes

P1 forecasts `δ_CP ∈ [251.86°, 270°]` by a rigorous box-Krawczyk certificate over box
`B = [0.625,0.750] × [0.902,0.956]` in the chart parameters `(m,δ)`, **conditional on (X6)**: the
assumption that the Basin-1 chamber-boundary preimage of the NuFit `(s₁₂²,s₁₃²)` rectangle lies in `B`.
The P1 note supported (X6) only by multistart-fsolve at **9** grid points (parent Table 2) and named it
an external admission with tightening route "outer-frame Krawczyk." This note executes that route and
upgrades (X6) to a **rigorous interval certificate over the entire rectangle**.

## Theorem (outer-frame containment)

Let `F(m,δ) = (s₁₂²(m,δ), s₁₃²(m,δ))` be the forward map on the chamber boundary `q = √(8/3) − δ`
(eigen-decomposition of the chart Hermitian `H(m,δ,q)`, adjugate projectors → mixing angles), and let
`rect = [0.270,0.341] × [0.02029,0.02391]` (NuFit 5.3 NO 3σ, named external). Let `B` be as above and
`S` the closed shell of width `W = 0.03` immediately surrounding `B` (`S = (B grown by W) ∖ int(B)`).

**Certificate.** Tiling `S` into `12167` interval sub-boxes (four strips bottom/top/left/right,
bisection to depth ≤ 16) and evaluating `F` in 200-bit `mpmath.iv` interval arithmetic, **every**
sub-box's interval image is **disjoint** from `rect` (disjoint = separated in ≥ 1 coordinate).
Hence `F(S) ∩ rect = ∅`, so `F⁻¹(rect) ∩ S = ∅`.

**Topological separation lemma.** `F` is continuous on `S` (the certificate's all-boxes-succeed with no
interval-Newton failure exhibits a positive eigenvalue gap on `S`, so no level-crossing discontinuity
there). A closed shell `S` that fully encloses `int(B)` with `F⁻¹(rect) ∩ S = ∅` separates the domain:
the connected component of `F⁻¹(rect)` containing the anchor (the PDG-central preimage, which lies in
`B`) cannot cross `S`, hence is contained in `int(B) ⊂ B`. This component **is** the Basin-1 preimage.
Therefore the Basin-1 chamber-boundary preimage of the whole NuFit rectangle is contained in `B`. ∎

## Independent float cross-check and the two-component structure

A separate float forward map (`numpy.linalg.eigh`, anchor-validated to reproduce the P1 note's
`δ_CP = 260.88°`) finds the true Basin-1 preimage bounding box `m ∈ [0.62682, 0.74828]`,
`δ ∈ [0.90383, 0.95467]` — **strictly inside `B`** with margins ≈ 0.0017 on every side. A wide-domain
scan shows `F⁻¹(rect)` on the chamber boundary has **exactly two** connected components: the Basin-1
component above (the anchor's component) and a disjoint **Basin-0** at `m ∈ [−0.057, 0.024]`,
`δ ∈ [1.039, 1.091]` where the Jarlskog **flips sign** (`J > 0`, `δ_CP ≈ 105°`). Basin-0 lies far
outside the shell `S` (≈ 0.57 away in `m`), so it is a *different* component, not Basin-1 — which
justifies identifying "Basin-1" with the anchor's connected component, exactly as (X6) intends. This
confirms the interval certificate's conclusion and shows the few sub-boxes that needed deeper bisection
were dependency blow-up at the tight margin, not genuine escapes.

## What this closes, and what conditionality it relocates to (honest)

Closing (X6) **retires the multistart preimage admission** but **relocates** (does not eliminate) the
forecast's conditionality. With (X6) certified, the P1 δ_CP forecast rests on:

1. **The chart `H(m,δ,q)` and the chamber-boundary surface `q = √(8/3) − δ`** — the parent forecast's
   chart structure. The forecast is on that boundary surface, so the on-boundary statement remains a
   separate condition.
2. **The measured-theta23 branch filter** distinguishing Basin-1 from the disjoint Basin-0 (`J > 0`,
   `δ_CP ≈ 105°`). Basin-0 predicts `s₂₃² ≈ 0.70–0.72`, outside the measured-theta23 band used by the
   branch-robustness note; the filter is empirical, not derived from the interval shell certificate.
3. **The NuFit input bands** on `(s₁₂²,s₁₃²)` — a named external comparison input (`θ₁₂,θ₁₃` are the
   framework's inputs, not predictions).

So the **specific admission this note closes is (X6)**: the preimage-localization is now a 200-bit
certificate rather than a 9-point multistart claim. The remaining conditionalities are the retained
chart/boundary structure and measured inputs — not a new unproven preimage admission.

## Review stress tests

The submitted packet stress-tested the certificate against topological-lemma soundness,
interval-arithmetic rigor, shell coverage, eigenvalue degeneracy, scope/relocation, and numerical traps.
The durable checks retained here are: the runner reproduces `PASS=2` with `12167` shell boxes cleared;
the separation lemma uses connectedness of the anchor component; `F` is continuous on `S` by positive
eigenvalue gap and zero interval-Newton failures; the four strips tile the enclosing annulus. This is not
an audit verdict. The independent audit lane decides retention. The over-broad branch-local phrase "no
remaining unproven framework admission" is not used: closing (X6) relocates conditionality (items 1-3),
it does not eliminate it.

## What is and is not claimed

- **Is:** a rigorous 200-bit interval certificate (plus an explicit topological lemma and an independent
  float cross-check) that the Basin-1 chamber-boundary preimage of the NuFit rectangle ⊂ `B`. This
  retires the multistart-fsolve admission (X6).
- **Is not:** does **not** re-derive the chart `H(m,δ,q)`, the chamber boundary, or the NuFit bands;
  does **not** alter the P1 δ_CP bracket `[251.86°,270°]` (that interval cert is unchanged); does **not**
  address off-chamber-boundary preimages (X6 concerns the chamber boundary, matching scope); adds no
  axiom or fitted value.

## Boundaries (honest)

- **Scope = the chamber boundary** `q = √(8/3) − δ`, matching (X6)'s statement; the certificate is over
  `(m,δ)` with `q` slaved to the boundary.
- **`B` and `rect` are the P1 note's objects**; `rect` is a named external comparison band.
- **The topological lemma is stated explicitly** and relies on `F`-continuity on `S` (established by the
  positive eigenvalue gap there) and full shell enclosure (the four strips cover `(B+W) ∖ int(B)`).

## Load-bearing inputs

- [`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)
  — defines (X6), the chart `H(m,δ,q)`, box `B`, and the rect; this note closes (X6).
- [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  — the 200-bit interval-Newton / adjugate-projector apparatus (`retained_bounded`), reused verbatim.

## Forbidden-imports check

No PDG / NuFit value is consumed as a derived quantity; the rectangle and box `B` are the P1 note's
named comparison/admission objects. The chart, eigenvalue enclosure, projectors, and disjointness test
are reproduced in the runner at 200-bit `mpmath.iv`; the float cross-check is independent (`numpy`).
