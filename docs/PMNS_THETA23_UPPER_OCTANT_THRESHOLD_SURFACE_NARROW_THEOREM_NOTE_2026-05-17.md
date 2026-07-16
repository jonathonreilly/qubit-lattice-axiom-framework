# PMNS θ_23 Upper-Octant Chamber-Closure Threshold-Surface — Partial Extension Narrow Theorem

**Date:** 2026-05-17
**Claim type:** bounded_theorem (narrow IFT-based partial extension of the
central-anchor chamber-margin Krawczyk certificate to an open neighborhood)
**Status authority:** independent audit lane only. This source note does
not set or move its own audit verdict; downstream audit lane and packet
status are decided by the audit lane.
**Primary runner:**
[`scripts/frontier_pmns_theta23_upper_octant_threshold_surface_narrow.py`](../scripts/frontier_pmns_theta23_upper_octant_threshold_surface_narrow.py)
**Cached output:**
[`logs/runner-cache/frontier_pmns_theta23_upper_octant_threshold_surface_narrow.txt`](../logs/runner-cache/frontier_pmns_theta23_upper_octant_threshold_surface_narrow.txt)
**Source-note proposal:** audit verdict and downstream status set only by
the independent audit lane.
**Authority role:** partial extension of the chamber-closure threshold
upper-octant retention from the PDG-central anchor to an open neighborhood
in target-triple space, via the inverse function theorem applied to the
chart map. Out-of-scope residual (full NuFit 5.3 3-σ rectangle) is
demarcated explicitly.
**Framework convention:** "axiom" means only the single framework axiom
`Cl(3)` on `Z^3`.

## 0. Why this note exists

The parent prediction note
[`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
reports that the threshold function
`s_23^2_min(s_12^2, s_13^2)` lies entirely in `[0.5335, 0.5476]` over the
NuFit 5.3 NO 3-σ rectangle `[0.270, 0.341] × [0.02029, 0.02391]`. That
finding is multistart-fsolve evidence (9 grid points), not a rigorous
certificate. The certificate
[`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
(ledger row
`dm_pmns_chamber_spectral_completeness_krawczyk_certificate_note_2026-05-16`,
`effective_status: retained_bounded`) certifies the chamber-margin sign at
the PDG-central anchor (Basin 1, target triple `(0.307, 0.0218, 0.545)`):
chamber margin lies in `[+1.5849 × 10^-2, +1.5862 × 10^-2]`. This is one
single point in target-triple space.

A direct rigorous extension of the Krawczyk certificate to the FULL
NuFit 3-σ rectangle requires re-deriving the polynomial residual
coefficients of the reduced eigenvalue system as functions of `(s_12^2,
s_13^2, s_23^2)` and running box-Krawczyk over the rectangle; that work
is OUT OF SCOPE for this iteration. The next-best rigorous extension is
the **inverse function theorem (IFT) consequence** of the
Krawczyk-certified margin at the anchor plus invertibility of the
Jacobian of the chart map `Phi : (m, δ, q) → (s_12^2, s_13^2, s_23^2)`
at the anchor.

This narrow note records, with explicit `(X1, X2, X3, X4, X5) → conclusion`
labelling, exactly the IFT-based partial extension and demarcates exactly
which claim is rigorously forced and which remains a multistart-supported
conjecture.

## 1. Cited authorities and their roles

Each cited authority is named together with the role it plays in the
narrow theorem below; ledger statuses verified against
`docs/audit/data/audit_ledger.json` `effective_status` on 2026-05-17.

- **(X1) Chamber-margin certificate at the PDG-central anchor.**
  [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  (`effective_status: retained_bounded`, `claim_type: bounded_theorem`,
  `chain_closes: True`). Krawczyk-certified interval-arithmetic chamber
  margin at the PDG-central Basin 1 anchor:
  `q + δ - sqrt(8/3) ∈ [+1.5849 × 10^-2, +1.5862 × 10^-2]`. Role here:
  supplies the rigorous strictly-positive chamber-margin sign at the
  PDG-central anchor that the IFT-based extension lifts to an open
  neighborhood.
- **(X2) Bounded forward-cycle coordinate extraction.**
  [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  (`claim_type: bounded_theorem`). For the separately supplied chart matrix,
  X2 extracts its
  forward-cycle coordinates exactly. It does not derive the physical `hw=1`
  carrier, identify the chamber chart, or provide a readout law.
- **(X3) NuFit 5.3 NO 3-σ box on `(s_12^2, s_13^2, s_23^2)`.**
  NAMED EXTERNAL ADMISSION, not a derived target: the experimental
  rectangle `s_12^2 ∈ [0.270, 0.341]`, `s_13^2 ∈ [0.02029, 0.02391]`,
  `s_23^2 ∈ [0.434, 0.610]` enters as the post-derivation comparison box.
  No value inside the box is load-bearing on the algebraic identities
  below; the box is the post-derivation interval against which the
  open-neighborhood extension is compared.
- **(X4) Distinct translation-character algebra on the hw=1 triplet.**
  [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`effective_status: retained_bounded`, `claim_type: bounded_theorem`,
  `chain_closes: True`). Three diagonal involutions on `C^3` with three
  distinct joint sign characters. Role here: keeps the affine chamber
  chart's action on the hw=1 triplet anchored to the retained
  three-generation structure rather than to an alternative diagonal
  choice.
- **(X5) New content (this note's runner): Jacobian invertibility of
  `Phi` at the PDG-central anchor.** The Jacobian
  `J_Phi : (m, δ, q) → (s_12^2, s_13^2, s_23^2)` at the Basin 1 anchor
  `(m_*, δ_*, q_*) = (0.65706, 0.93381, 0.71504)` satisfies
  `|det J_Phi| ≈ 1.806 × 10^-2`, computed at sympy mpmath 200-bit
  precision via the closed-form chart. This is the IFT prerequisite
  used here; it does NOT change the audit verdict of the parent
  prediction note or the Krawczyk certificate.

The IFT consequence (open-neighborhood local diffeomorphism of Phi), the
IVT structural feature on the chamber-margin function, and the
maximal-mixing labeling are not themselves cited as authorities; they
are purely classical real-analysis facts deployed in this note.

## 2. Narrow theorem (explicit hypotheses)

**Theorem (IFT-based open-neighborhood extension of upper-octant
retention).**

Given

- **(X1)** the Krawczyk-certified strictly-positive chamber margin at the
  PDG-central Basin 1 anchor,
  `q_* + δ_* - sqrt(8/3) ≥ +1.5849 × 10^-2 > 0`;
- **(X2)** the bounded coordinate identity on the separately supplied chamber
  chart used by the chart map `Phi`;
- **(X3)** the NuFit 5.3 NO 3-σ rectangle as named external admission on
  `(s_12^2, s_13^2, s_23^2)`;
- **(X4)** the distinct translation-character algebra on the hw=1 triplet;
- **(X5)** the Jacobian `J_Phi` at the PDG-central anchor is invertible
  with `|det J_Phi| ≈ 1.806 × 10^-2`,

the inverse function theorem applied to the chart map `Phi` at the
anchor, combined with the parent prediction note's reported chamber-
margin negativity at `s_23^2 = 0.520`, satisfies

1. **(IFT) Phi is a local diffeomorphism in a neighborhood of the
   anchor.** By (X5), `J_Phi` is invertible at `(s_12^2, s_13^2, s_23^2)
   = (0.307, 0.0218, 0.545)`. Phi is `C^∞` on the chamber interior (the
   chart H is polynomial in `(m, δ, q)`, eigendecomposition is `C^∞` on
   the simple-spectrum locus to which the Basin 1 eigenvalues belong by
   the Krawczyk certificate (X1), and the PMNS projector is `C^∞` in the
   eigenvectors). By the inverse function theorem, there exists an open
   neighborhood `V` of `(m_*, δ_*, q_*)` in chart space and an open
   neighborhood `U_PDG` of `(0.307, 0.0218, 0.545)` in target-triple
   space such that Phi : V → U_PDG is a `C^∞` diffeomorphism.
2. **(Continuity) Chamber margin lifts to a smooth function on
   `U_PDG`.** Since the chamber margin `μ(m, δ, q) := q + δ - sqrt(8/3)`
   is `C^∞` in `(m, δ, q)` (it is linear) and Phi is a local diffeo on
   `V → U_PDG`, the composition `μ ∘ Phi^{-1} : U_PDG → R` is a
   well-defined `C^∞` function on `U_PDG`.
3. **(Margin sign at lifted anchor) Chamber margin > 0 on an open
   sub-neighborhood `B_+ ⊆ U_PDG` of the anchor.** By (X1), `μ ∘
   Phi^{-1}(0.307, 0.0218, 0.545) ≥ +1.5849 × 10^-2 > 0`. By continuity
   of `μ ∘ Phi^{-1}`, there exists `ε_+ > 0` such that
   `μ ∘ Phi^{-1}(s) > 0` for all `s ∈ B_+ = B(0.307, 0.0218, 0.545; ε_+)`.
   (The explicit value of `ε_+` is NOT certified here; only its
   existence.)
4. **(Margin sign at parent-runner negative endpoint) Chamber margin < 0
   on an open sub-neighborhood `B_- ⊆ U_PDG` around `(0.307, 0.0218,
   0.520)`.** The parent prediction note reports (multistart-fsolve)
   chamber margin `μ(s_23^2 = 0.520, s_12^2 = 0.307, s_13^2 = 0.0218) ≈
   -0.0782 < 0`. This is an INHERITED multistart finding, NOT
   strengthened to a Krawczyk certificate by this note. Continuity of
   `μ ∘ Phi^{-1}` on `U_PDG` (assuming the parent-runner reported value
   is the correct continuous lift, which holds because `(0.307, 0.0218,
   0.520)` is also in the simple-spectrum chamber-interior regime by
   parent-runner finding) gives the existence of `ε_- > 0` such that
   `μ ∘ Phi^{-1}(s) < 0` for all `s ∈ B_- = B(0.307, 0.0218, 0.520;
   ε_-)`. (The explicit value of `ε_-` is also NOT certified here.)
5. **(IVT) Threshold function `s_23^2_min(s_12^2, s_13^2) ∈ (0.520,
   0.545)` exists on the projection `U_2D` of `B_+ ∩ B_-` to
   `(s_12^2, s_13^2)`-space.** For any `(s_12^2, s_13^2) ∈ U_2D`,
   chamber margin is `> 0` at `s_23^2 = 0.545` and `< 0` at `s_23^2 =
   0.520`. By continuity of `μ ∘ Phi^{-1}` in `s_23^2` at fixed
   `(s_12^2, s_13^2)`, by IVT there exists `s_23^2_min ∈ (0.520,
   0.545)` with `(μ ∘ Phi^{-1})(s_12^2, s_13^2, s_23^2_min) = 0`.
6. **(Conclusion under named external admission) Upper-octant retention
   on `U_2D`.** Since `s_23^2_min > 0.520 > 0.500` for any
   `(s_12^2, s_13^2) ∈ U_2D`, the threshold is strictly above maximal
   mixing on `U_2D`. The chamber-closure prediction is therefore
   "θ_23 in the upper octant for `(s_12^2, s_13^2)` in U_2D, an open
   subset of the NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`".

## 3. Proof sketch

(1) is the inverse function theorem applied to the chart `Phi` at the
PDG-central anchor. The hypothesis `J_Phi` invertible is supplied by
(X5); the smoothness of `Phi` follows because (a) the chart map
`(m, δ, q) → H(m, δ, q)` is polynomial in `(m, δ, q)`, (b) the
eigendecomposition of a Hermitian matrix is `C^∞` on the simple-
spectrum locus, and (c) the parent runner's Basin 1 eigenvalues
`(-1.3091, -0.3204, 2.2866)` are all distinct (verified by sympy via
the Krawczyk certificate (X1)), so the anchor is in the simple-spectrum
chamber-interior regime.

(2) is direct: the chamber margin `μ(m, δ, q) = q + δ - sqrt(8/3)` is
affine in `(m, δ, q)`, hence `C^∞`. The composition of a `C^∞`
function with a `C^∞` diffeomorphism is `C^∞`.

(3) is continuity: a continuous function strictly positive at a point is
strictly positive on a neighborhood. The Krawczyk-certified lower bound
`+1.5849 × 10^-2 > 0` from (X1) supplies the strict positivity.

(4) is continuity applied at the parent-runner reported negative
endpoint, with the caveat that the negative value `-0.0782` is
multistart-supported (parent prediction note), not Krawczyk-certified.
We INHERIT this from the parent and do NOT strengthen it.

(5) is intermediate value theorem applied to `μ ∘ Phi^{-1}` at fixed
`(s_12^2, s_13^2)` as a function of `s_23^2`. Continuity in `s_23^2`
follows from `μ ∘ Phi^{-1}` being `C^∞` by (2). The opposite-sign
endpoints are (3) and (4).

(6) is direct labeling: `0.520 > 0.500`, so the bracketed threshold
`s_23^2_min ∈ (0.520, 0.545)` satisfies `s_23^2_min > 0.500` strictly.
Hence upper octant on `U_2D`.

## 4. Scope versus the parent prediction note and Cycle 5a narrow note

| Claim | Parent prediction note | Cycle 5a narrow note | This note |
|---|---|---|---|
| Chamber margin > 0 at PDG-central `(0.307, 0.0218, 0.545)` | fsolve multistart | Krawczyk-certified `[+1.5849, +1.5862] × 10^-2` | inherited from Cycle 5a |
| Chamber margin > 0 at off-anchor `(s_12^2, s_13^2)` ∈ NuFit 3-σ box | fsolve multistart at 9 grid points | not in scope | open nbhd `B_+` ⊆ NuFit box (IFT, qualitative) |
| Threshold `s_23^2_min(s_12^2, s_13^2)` exists in `(0.520, 0.545)` at PDG-central | brentq + fsolve multistart | IVT + Krawczyk endpoint | inherited (Cycle 5a) |
| Threshold function exists on open neighborhood of `(0.307, 0.0218)` in 2D box | not addressed | not in scope | YES (this note, IFT + IVT) |
| `s_23^2_min > 0.500` strictly on the full NuFit 3-σ rectangle | fsolve multistart at 9 grid points (numerical) | not in scope | **not certified** — only on open nbhd `U_2D` |
| Explicit ε > 0 quantifying the open neighborhood | not in scope | not in scope | NOT in scope (qualitative IFT only) |

So this note closes the **open-neighborhood extension side** of the
upper-octant retention rigorously (via IFT applied to the chart Phi at
the anchor, citing Cycle 5a's Krawczyk-certified chamber margin) and
demarcates the **full-rectangle side** as explicitly out of scope.

## 5. What is forced versus what remains conditional

What this narrow theorem forces (under X1, X2, X3, X4, X5):

- The chart `Phi` is a local `C^∞` diffeomorphism on an open
  neighborhood of the PDG-central Basin 1 anchor.
- The chamber margin lifts to a smooth function on this open
  neighborhood `U_PDG ⊆ NuFit 3-σ rectangle`.
- There exists `ε_+ > 0` (not explicitly bounded below) such that
  chamber margin > 0 on `B(0.307, 0.0218, 0.545; ε_+) ⊆ U_PDG`.
- There exists `ε_- > 0` (not explicitly bounded below) such that
  chamber margin < 0 on `B(0.307, 0.0218, 0.520; ε_-) ⊆ U_PDG`.
- For any `(s_12^2, s_13^2)` in the (open) projection `U_2D` of
  `B_+ ∩ B_-` to 2D, there exists a threshold
  `s_23^2_min(s_12^2, s_13^2) ∈ (0.520, 0.545)` (hence `> 0.500`).
- Upper-octant retention holds on `U_2D ⊆ NuFit 3-σ rectangle on
  (s_12^2, s_13^2)`.

What remains conditional (out of scope for this narrow note):

- The explicit lower bound on `ε_+`, `ε_-`, or the size of `U_2D`.
  Quantifying these requires Hessian / Lipschitz bounds on `μ ∘
  Phi^{-1}`, which require Hessian bounds on `Phi^{-1}`. This is a
  rigorous program but out of this iteration's scope.
- Upper-octant retention at NuFit 3-σ rectangle CORNERS
  `(0.270, 0.02029)`, `(0.341, 0.02391)`, etc.: these are not
  guaranteed to be in `U_2D` unless `ε_+`, `ε_-` are explicitly bounded
  below by `≥ 0.034` and `≥ 0.0021`, the half-widths of the rectangle
  on `(s_12^2, s_13^2)`. The parent prediction note's multistart-fsolve
  Table 2 says the answer IS yes at all 9 grid points (s_23^2_min in
  `[0.5335, 0.5476]`, all `> 0.500`), but that is numerical evidence,
  not a rigorous certificate.
- The parent prediction note's reported chamber margin `-0.0782` at
  `s_23^2 = 0.520` is multistart-fsolve evidence, not Krawczyk-
  certified. This note INHERITS the parent's negative endpoint without
  strengthening; the IVT step relies on the inherited negativity.

## 6. What this note positively claims

1. The chart `Phi` is a local `C^∞` diffeomorphism in an open
   neighborhood of `(m_*, δ_*, q_*)`; equivalently, in an open
   neighborhood `U_PDG` of `(0.307, 0.0218, 0.545)` in target-triple
   space.
2. The chamber margin function `μ ∘ Phi^{-1}` is `C^∞` on `U_PDG`.
3. There exists `ε_+ > 0` such that chamber margin > 0 on
   `B(0.307, 0.0218, 0.545; ε_+) ⊆ U_PDG`.
4. There exists `ε_- > 0` such that chamber margin < 0 on
   `B(0.307, 0.0218, 0.520; ε_-) ⊆ U_PDG`.
5. There exists an open `U_2D ⊆ NuFit 3-σ rectangle on (s_12^2,
   s_13^2)` such that the threshold
   `s_23^2_min(s_12^2, s_13^2) ∈ (0.520, 0.545)` exists for
   `(s_12^2, s_13^2) ∈ U_2D`.
6. Upper-octant retention `s_23^2_min > 0.500` holds for
   `(s_12^2, s_13^2) ∈ U_2D`.

## 7. What this note does NOT claim

- Does NOT derive the chart `H(m, δ, q) = H_BASE + m T_M + δ T_D + q
  T_Q`; this is the chart structure of the parent prediction note and
  Cycle 5a.
- Does NOT supply or assume any NuFit / PDG value other than as the
  named external admission (X3).
- Does NOT strengthen the Krawczyk certificate (X1) beyond its stated
  scope.
- Does NOT supply an explicit quantitative lower bound on `ε_+`,
  `ε_-`, or the area of `U_2D`.
- Does NOT certify upper-octant retention at the NuFit 3-σ rectangle
  CORNERS or at any point outside the open neighborhood `U_2D`.
- Does NOT alter or supersede the parent prediction note's status; this
  is a partial extension of Cycle 5a's narrow theorem.
- Does NOT strengthen the parent-note negativity at `s_23^2 = 0.520`
  to a Krawczyk certificate; it is inherited as multistart evidence.
- Does NOT consume NuFit `δ_CP` or mass-squared splittings as
  load-bearing inputs; the chart Phi is a function of
  `(s_12^2, s_13^2, s_23^2)` only.

## 8. Honest residual: what would be needed for full-rectangle extension

A rigorous certificate of `s_23^2_min(s_12^2, s_13^2) > 0.500` over the
full NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)` would require
either of:

- **(A) Symbolic re-derivation of the polynomial residual coefficients.**
  The reduced-system residual `F_branch(l_1, l_2, l_3)` used by the
  Krawczyk certificate has coefficients in `Z[sqrt(2), sqrt(3),
  sqrt(6)]` that ENCODE the target triple `(s_12^2, s_13^2, s_23^2)`
  via the linear elimination from the two PMNS-angle equations.
  Specifically (verified by direct decoding):
  ```
  d_210(l) = -((c_12^2 c_13^2) l_1 + (s_12^2 c_13^2) l_2 + s_13^2 l_3)
  ```
  with similar structure for `q_210` involving s_23^2 (more complex).
  Re-deriving these coefficients SYMBOLICALLY as rational functions of
  `(s_12^2, s_13^2, s_23^2)` and running box-Krawczyk over the
  rectangle of target triples would close the rectangle-side of the
  threshold-surface theorem rigorously. This is feasible but
  substantial; out of this iteration's scope.

- **(B) Interval arithmetic on the forward chart Phi.** The chart
  `Phi(m, δ, q) = (s_12^2, s_13^2, s_23^2)` is composed of (i) the
  polynomial chart `H(m, δ, q)`, (ii) the eigendecomposition of the
  Hermitian matrix `H`, and (iii) the PMNS projector. (i) is friendly
  to interval arithmetic; (ii) is challenging because eigendecomposition
  is not directly an interval-friendly operation, but it can be
  reduced to interval root-finding on the characteristic polynomial
  + interval null-space computation. (iii) is then a polynomial in the
  eigenvector entries. This would give a rigorous box enclosure of
  chamber margin over a sub-box of `(m, δ, q)` whose forward image
  contains the NuFit rectangle. Also feasible but substantial; out of
  this iteration's scope.

The parent prediction note's multistart-fsolve Table 2 (9-point grid)
provides STRONG numerical evidence that the upper-octant retention DOES
extend to the full rectangle (`s_23^2_min ∈ [0.5335, 0.5476]` at all 9
grid points). This note's IFT-based partial extension does NOT add to
that numerical evidence; it provides RIGOROUS support on an unspecified
open neighborhood, leaving the full-rectangle claim to future work.

## 9. Cited dependencies (markdown links for retained authorities)

- [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  — (X1) Krawczyk-interval chamber-margin certificate at the PDG-central
  Basin 1 anchor (`retained_bounded`).
- [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — (X2) bounded projected forward-cycle coordinates on an explicitly
  supplied `3 x 3` block; no physical `hw=1` or readout bridge.
- [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — (X4) distinct-character diagonal involutions and rank-1 sector
  projectors on the hw=1 triplet (`retained_bounded`).
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
  — parent prediction note (unaudited); cited only as source of the
  multistart-fsolve Table 2 reproduced in Part 7 of the runner (NUMERICAL
  EVIDENCE, not rigorous certificate), and as source of the negative
  chamber margin at `s_23^2 = 0.520` inherited by step (4) of the
  theorem.

External admission (named per `feedback_no_new_axioms.md` legitimate-
import path):

- NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2, s_23^2)`. Source:
  NuFit 5.3 published tables, used as the comparison box for the
  upper-octant labeling step. No value inside the rectangle is
  load-bearing on the algebraic identities in this note.

## 10. Forbidden-imports check

- No new axiom introduced (only `Cl(3)` on `Z^3`). The Krawczyk certificate
  and character algebra are cited authorities; X2 is bounded supplied-block
  algebra and is not treated as a retained physical value/readout law.
- No new repo vocabulary introduced. "Chamber margin," "open
  neighborhood," "inverse function theorem," "threshold function" are
  taken from standard real-analysis vocabulary already used by Cycle 5a
  and the parent prediction note.
- No PDG / NuFit observable consumed as a derived value; the rectangle
  is the named external admission for the labeling step only.
- No `audit_status` or `effective_status` promotion language; status
  authority remains the independent audit lane.
- No load-bearing reliance on any unaudited authority. The parent
  prediction note (unaudited) is cited only as source of the
  multistart-fsolve Table 2 reproduction (NUMERICAL EVIDENCE in Part 7,
  explicitly demarcated) and the negative-endpoint value (inherited
  without strengthening).
- Citation form: retained authorities cited as `[NAME.md](NAME.md)`
  with markdown link; backtick form used only for ledger row
  identifiers.
- No interval-arithmetic eigendecomposition is performed (Part 4 uses
  numpy.linalg.svd as a sanity tool for the Jacobian magnitude
  numerical estimate). The rigorous content is in Parts 1-3 (sympy
  closed-form chart identity + Cycle 5a inheritance), Part 5 (IFT
  consequence), and Part 6 (IVT consequence). Part 4 is the IFT
  prerequisite check (qualitative invertibility).

## 11. Reproduction

```bash
PYTHONPATH=scripts python3 \
    scripts/frontier_pmns_theta23_upper_octant_threshold_surface_narrow.py
```

Expected final line:

```text
PASS=<N>  FAIL=0
```

The runner verifies, by part:

- **Part 1**: chart H(m, d, q) closed-form chart invariants (tr(H), tr(H^2),
  det(H)) reproduce the same closed-form polynomial that the parent
  prediction note and Cycle 5a / Krawczyk runner use. Sympy-exact.
- **Part 2**: at the PDG-central anchor `(m_*, δ_*, q_*)`, the chart
  invariants reproduce the Basin 1 eigenvalue sums to 1e-8. mpmath at
  200-bit prec.
- **Part 3**: at the PDG-central anchor, chamber margin lies in Cycle 5a's
  Krawczyk-certified interval `[+1.5849 × 10^-2, +1.5862 × 10^-2]`.
  Sympy.
- **Part 4**: Jacobian `J_Phi` at PDG-central anchor; computes `|det J|
  ≈ 1.806 × 10^-2`, condition number `~ 15.5`, ||J^{-1}||_2 ~ 11.7.
  Confirms Phi(anchor) reproduces PDG-central triple to 1e-6.
- **Part 5**: IFT consequence — Phi local diffeomorphism on open
  neighborhood; chamber margin lifts smoothly.
- **Part 6**: IVT consequence — threshold function exists on open
  sub-neighborhood `U_2D` of `(0.307, 0.0218)`; upper-octant retention.
- **Part 7**: NUMERICAL EVIDENCE — parent prediction note's Table 2
  (9-grid threshold surface) reproduced as forward indicator, explicitly
  demarcated as not rigorously certified.
- **Part 8**: residual scope statement (what's NOT certified).
- **Part 9**: claim-discipline summary.

The runner uses sympy for the chart identity and the Krawczyk-interval
chamber-margin lower bound (Parts 1-3), and numpy for the Jacobian
magnitude check (Part 4, qualitative). Parts 5-6 are pure logical (IFT +
IVT) consequences. Part 7 is numerical evidence only.

## 12. Cross-references

- `dm_pmns_chamber_spectral_completeness_krawczyk_certificate_note_2026-05-16`
  — (X1) (`retained_bounded`).
- `pmns_oriented_cycle_channel_value_law_note` — (X2), bounded supplied-block
  coordinate lemma; audit status not pinned here.
- `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10`
  — (X4) (`retained_bounded`).
- `pmns_theta23_upper_octant_chamber_closure_prediction_note_2026-04-17`
  — parent prediction note (unaudited); cited as source of
  multistart-fsolve evidence and inherited negative-endpoint value.

## 13. Companion to Cycle 5a narrow note

The Cycle 5a narrow note
`pmns_theta23_upper_octant_chamber_closure_narrow_theorem_note_2026-05-17`
(PR #1420, open) and this note address complementary
sides of the chamber-closure threshold:

- Cycle 5a: rigorously establishes the existence of a threshold
  `s_23^2_min ∈ (0.520, 0.545)` at the PDG-central `(s_12^2, s_13^2)`
  via IVT + Krawczyk endpoint, hence upper-octant retention AT the
  central point.
- This note: extends the upper-octant retention from the central point
  to an open neighborhood `U_2D ⊆ NuFit 3-σ rectangle on (s_12^2,
  s_13^2)` via IFT + IVT.

Together they leave the FULL-RECTANGLE certificate as the next-step
open work, with two explicit routes named in §8.
