# PMNS Predictive-Surface Characterization — Campaign Synthesis Note

**Date:** 2026-05-17
**Type:** meta (campaign-level synthesis)
**Claim type:** meta
**Status authority:** independent audit lane only. This note does not set
or move its own audit verdict; downstream audit lane and packet status
are decided by the audit lane.
**Authority role:** campaign-level synthesis recording the architectural
state reached by Cycles 5a / 6a / 7 / 8 / 9 of the physics-loop
PMNS-chamber-chart predictive-surface campaign. Catalogs already-shipped
narrow theorem source notes; does NOT introduce new derivations.
**Framework convention:** the physical baseline is
`Cl(3)` on `Z^3`.

## Authority disclaimer

This is a campaign-level synthesis note. It records the architectural
partition that has emerged from five already-shipped source-note PRs
(cycles 5a, 6a, 7, 8, 9). Each cited source note is independently
proposed at its own PR and is audit-lane-decided on its own merits.
This synthesis does NOT promote any of those notes, does NOT propose a
new theorem, and does NOT modify any retained or in-flight authority.
The architectural reading offered here is descriptive, not normative.

```yaml
actual_current_surface_status: campaign synthesis (cycles 5a-9)
proposal_allowed: false
proposal_allowed_reason: |
  This is a campaign-level synthesis, not a new derivation. Each
  individual cycle's narrow theorem is independently proposed in its
  own source-note PR. This synthesis catalogs the architectural
  partition the campaign converged to; it does not promote, demote,
  or modify any cited authority.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 0. Scope and disclaimer

This synthesis catalogs ALREADY-LANDED narrow theorem source notes from
five cycles of the physics-loop PMNS-chamber-chart campaign (Cycles 5a,
6a, 7, 8, 9). Each cycle's narrow theorem is a stand-alone source-note
PR; this synthesis does not amend or supplement them. The architectural
reading is the campaign's observation that those five narrow theorems
collectively answer a single question:

> "What does the framework's PMNS chamber chart predict over the NuFit
> 5.3 NO 3-σ rectangle?"

The answer the cycles converged to is an explicit partition of the
eight PMNS observables into a predicted subset (`s_23^2`, `δ_CP`), an
architecturally silent subset (`s_12^2`, `s_13^2`, `r_21`, `r_31`,
`Σm_ν`, `m_ββ`), and the audit-lane-determined status of each cycle's
narrow theorem. This synthesis names that partition; it does not
introduce it as new content.

The companion BAE / Koide structural foreclosure result (PRs #1412,
#1415, #1419) lives on a separate carrier and is recorded only as a
cross-reference in §8 below.

## 1. The campaign question

The PMNS-as-f(H) closure theorem note
[`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
(`unaudited / bounded_theorem`) maps the chamber chart parameters
`(m, δ, q_+)` to a four-tuple of dimensionless PMNS observables
`(s_12^2, s_13^2, s_23^2, δ_CP)` via the eigenVECTORS of the affine
Hermitian operator family

```
H(m, δ, q_+) = H_base + m T_m + δ T_δ + q_+ T_q.
```

The PDG-central anchor for Basin 1 sits at
`(m_*, δ_*, q_*) ≈ (0.65706, 0.93381, 0.71504)`, with chamber margin
`q_* + δ_* − sqrt(8/3) ≈ +0.0159 > 0` (chamber-interior pin).

The retained Krawczyk certificate
[`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
(`retained_bounded / bounded_theorem`) brackets the chamber margin at
the anchor at 200-bit mpmath precision in
`[+1.5849 × 10^-2, +1.5862 × 10^-2]`. This is the interval-arithmetic
foundation reused across all five campaign cycles.

The campaign question is the natural follow-on:

> Given the retained Krawczyk apparatus and the chart structure, what
> sub-regions of the NuFit 5.3 NO 3-σ rectangle does the chamber chart
> force? Which PMNS observables admit a sub-region prediction inside
> their experimental bands, and which are the chart structurally silent
> about?

## 2. The chamber chart

For convenience, the chamber chart is the affine Hermitian map

```
Phi : (m, δ, q_+) → (s_12^2, s_13^2, s_23^2, δ_CP)
```

defined by diagonalization of `H(m, δ, q_+)`. The first three outputs
are PMNS mixing-angle squared sines; the fourth is the Dirac CP-phase
(extracted from eigenvector rephasing-invariants `J` and `ReBox`). The
chamber-boundary surface is `q = sqrt(8/3) − δ` (the algebraic locus
where the chamber margin vanishes); the Basin-1 chamber-boundary
preimage `B = [0.625, 0.750] × [0.902, 0.956]` is the bounding box used
by Cycles 7 / 8 / 9 for box-Krawczyk on `(m, δ)` at fixed
`q = sqrt(8/3) − δ`.

The map `Phi` does NOT consume any neutrino mass-squared splittings,
absolute mass scale, or Majorana CP phases as input. The chart is
dimensionless and acts only on the four dimensionless mixing
observables.

## 3. Observable partition

The five-cycle cascade established the following partition of the
eight commonly-discussed PMNS observables (the four dimensionless
mixing observables plus four mass observables widely reported by
long-baseline / cosmological / 0νββ experiments).

### 3.1 Predicted (sub-region inside experimental band)

| Observable | Cycle | Source PR | Forecast | NuFit 3-σ band | Sub-region |
|---|---|---|---|---|---|
| `s_23^2` (upper octant) | Cycle 7 | PR #1442 ([`PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md)) | `s_23^2 > 0.5` strictly | `[0.434, 0.610]` | upper octant `(0.5, 0.610]` |
| `δ_CP` (third quadrant) | Cycle 8 | PR #1447 ([`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)) | `δ_CP ∈ [251.86°, 270.00°]` | `[120°, 369°]` (width 249°) | `[251.86°, 270.00°]` (width 18.13°) |

The `s_23^2` forecast is "upper octant" — interval-certified at
200-bit precision over the full NuFit 5.3 NO 3-σ rectangle on
`(s_12^2, s_13^2)`, conditional on the named preimage-localization
admission (X6) inherited from the parent prediction note.

The `δ_CP` forecast is "third quadrant near maximal CP-violation,
within 18.13° of 270° on the lower side" — interval-certified over
the same `(m, δ)` bounding box `B` via 200-bit projector identities
on the Jarlskog `J` and the cos-companion rephasing-invariant
`ReBox + c_12^2 c_13^2 s_13^2 s_23^2`. The bracket lies inside a
7.3 % sub-region of the NuFit 3-σ band on δ_CP.

### 3.2 Architecturally silent (no sub-region prediction)

| Observable | Cycle | Source PR | Honest finding |
|---|---|---|---|
| `s_12^2` | Cycle 8 | PR #1447 | chamber-boundary image of `B` covers 100 % of NuFit `(s_12^2, s_13^2)` rectangle on 20 × 20 cell partition (marginal s_12² coverage 20/20 cells) |
| `s_13^2` | Cycle 8 | PR #1447 | same as `s_12^2` (marginal s_13² coverage 20/20 cells) |
| `r_21 := m_2/m_1` | Cycle 9 | PR #1452 ([`PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md)) | chamber-side `(m_2^2 − m_1^2)/(m_3^2 − m_1^2) ⊂ [0.308, 0.329]` is DISJOINT from empirical NuFit `[0.0268, 0.0328]` over all 6 `|λ|→m` permutations |
| `r_31 := m_3/m_1` | Cycle 9 | PR #1452 | same — no chamber-side linear identification fits |
| `Σm_ν` | Cycle 9 | PR #1452 | retained Σm_ν functional form ([`NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md`](NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md)) names cosmological inputs `(L, Ω_b, Ω_DM, h)` not in chamber chart |
| `m_ββ` | Cycle 9 | PR #1452 | Majorana CP phases `(α_21, α_31)` declared atlas-open per parent PMNS-as-f(H) note; chamber chart does not constrain |

Honest no-prediction findings are NOT counter-examples. The chamber-
boundary image of `B` is consistent with the entire NuFit 3-σ rectangle
on `(s_12^2, s_13^2)`; it simply does not single out a sub-region.

## 4. Structural reason for the partition

The chamber chart is **mass-blind by construction**: it predicts the
PMNS mixing matrix `U_PMNS` via the eigenVECTORS of `H(m, δ, q_+)`. The
eigenvalues of `H` are dimensionless and carry no absolute mass scale.
Cycle 9 (PR #1452) certified at 200-bit precision that the eigenvalue
sign signature is `(λ_1, λ_2, λ_3) = (−, −, +)` over the entire
preimage box `B`, with `|λ_(middle)| < |λ_(smallest)| < |λ_(largest)|`.
No linear identification `m_i = α |λ_{π(i)}| + β` over the six
permutations matches the empirical `Δm²` ratio.

Architecturally, the partition reads as follows:

- The four dimensionless mixing observables `(s_12^2, s_13^2, s_23^2,
  δ_CP)` are functions of three independent chamber chart parameters
  `(m, δ, q_+)`; this is a 3-input → 4-output map. Three of the four
  outputs PIN the chart preimage (any three of them invert `Phi` to
  fix `(m, δ, q_+)`), and the fourth is then forced.
- Cycle 7 (PR #1442) chose `(s_12^2, s_13^2)` as input pair and showed
  `s_23^2` is forced into the upper octant on the full NuFit rectangle.
- Cycle 8 (PR #1447) extended the SAME box-Krawczyk apparatus to the
  fourth output `δ_CP` and certified the third-quadrant bracket.
- The `s_12^2`, `s_13^2` no-prediction findings in Cycle 8 are the
  expected consequence: if `(s_12^2, s_13^2)` is the input pair that
  PINS the preimage, the chart does not back-predict its own input.
- The four mass observables `(r_21, r_31, Σm_ν, m_ββ)` live in the
  COMPLEMENT of the chart's range: the chart is dimensionless, so it
  cannot fix any absolute mass scale; Majorana phases are explicitly
  declared atlas-open by the parent closure note. Cycle 9 (PR #1452)
  certified this STRUCTURALLY (eigenvalue sign-signature + disjoint-
  band check), not just by absence of derivation.

The partition is therefore intrinsic to the chamber chart's
architecture: 3 independent inputs → 4 dimensionless outputs (two
pinning, one predicted, one predicted phase); mass-scale and Majorana
sector live on different carriers.

## 5. Cycle-by-cycle cascade table

| Cycle | PR | Source-note file | New content | Forecast / finding |
|---|---|---|---|---|
| 5a | #1420 ([`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md)) | narrow rescope citing Krawczyk certificate | Krawczyk-certified chamber margin at PDG-central anchor; IVT bridge to threshold-surface existence | `s_23^2_min ∈ (0.520, 0.545)` at PDG-central anchor (IVT on continuous margin); chamber forces upper octant at the anchor |
| 6a | #1427 ([`PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md)) | IFT-based partial extension | Jacobian `|det J_Phi| ≈ 1.806 × 10^-2` at the anchor; IFT lifts margin sign to an open neighborhood `U_2D ⊂ NuFit` | `s_23^2 > 0.5` strictly on an open neighborhood of `(0.307, 0.0218)` |
| 7 | #1442 ([`PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md)) | box-Krawczyk extension to full rectangle | 80 × 80 grid partition of `B = [0.625, 0.750] × [0.902, 0.956]`; 5404 image-overlap sub-boxes all certify `s_23^2 > 0.5`; tightest gap `> 2.77 × 10^-2` | `s_23^2 > 0.5` strictly on the ENTIRE NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)` |
| 8 | #1447 ([`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)) | box-Krawczyk on Jarlskog `J` and cos-companion `ReBox + c_12^2 c_13^2 s_13^2 s_23^2`; chamber-boundary coverage of `(s_12^2, s_13^2)` | `J < 0` and `cos_neg_num > 0` over all image-overlap sub-boxes; recursive bisection at max depth 6 | `δ_CP ∈ [251.86°, 270.00°]` over full rectangle (positive forecast); `s_12^2`, `s_13^2` no-prediction (chamber-boundary image covers entire NuFit rectangle) |
| 9 | #1452 ([`PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md)) | eigenvalue sign-signature box-Krawczyk; chamber-side `Δm²` ratio band; permutation enumeration | sign signature `(−, −, +)` on `B`; chamber-side `(m_2^2 − m_1^2)/(m_3^2 − m_1^2) ⊂ [0.308, 0.329]`; all 6 permutations disjoint from empirical `[0.0268, 0.0328]` | `(r_21, r_31, Σm_ν, m_ββ)` no-prediction (all four mass observables architecturally silent) |

All five cycles share the same retained interval-arithmetic apparatus
(200-bit mpmath, interval Newton on the cubic characteristic
polynomial, adjugate-based interval projectors) and the same `(m, δ)`
bounding box `B` from Cycle 7 onward. The full-rectangle / no-
prediction conclusions of Cycles 7 / 8 / 9 inherit the same named
preimage-localization admission (X6 / X8) from the parent prediction
note's multistart Table 2 (9 grid points). The audit lane has final
authority on whether that named external admission is sufficient.

## 6. What the chamber chart predicts versus what it inputs

A compact restatement of the partition using `Phi : (m, δ, q_+) →
(s_12^2, s_13^2, s_23^2, δ_CP)`:

| PMNS observable | Role in `Phi` | Status |
|---|---|---|
| `s_12^2` | input (pins preimage) | no sub-region forecast (Cycle 8) |
| `s_13^2` | input (pins preimage) | no sub-region forecast (Cycle 8) |
| `s_23^2` | predicted output | upper octant, full rectangle (Cycle 7) |
| `δ_CP` | predicted output | third quadrant `[251.86°, 270.00°]` (Cycle 8) |
| `r_21`, `r_31` | not in `Phi`'s codomain (`|λ|`-ratios sit in `[0.308, 0.329]`, disjoint from empirical) | no chamber-side identification (Cycle 9) |
| `Σm_ν` | not in `Phi`'s codomain (cosmological inputs `(L, Ω_b, Ω_DM, h)`) | no prediction (Cycle 9) |
| `m_ββ` | not in `Phi`'s codomain (Majorana phases atlas-open) | no prediction (Cycle 9) |

The two predicted outputs (`s_23^2`, `δ_CP`) are exactly the rows where
`Phi` is forced once `(s_12^2, s_13^2)` is admitted. The four
architecturally-silent mass observables are exactly the rows OUTSIDE
the chart's codomain.

## 7. Falsifiability

The framework predicts only two of the eight observables in this
partition. The corresponding falsifiability conditions are:

| Predicted observable | Forecast | Refutation condition |
|---|---|---|
| `s_23^2` | upper octant, full NuFit 3-σ rectangle | `s_23^2 ≤ 0.5` measured consistently with NuFit-3σ-acceptable correlated `(s_12^2, s_13^2)` |
| `δ_CP` | `[251.86°, 270.00°]` over full rectangle | `δ_CP` outside `[251.86°, 270.00°]` at > 3σ |

For the six architecturally-silent observables (`s_12^2`, `s_13^2`,
`r_21`, `r_31`, `Σm_ν`, `m_ββ`), the framework predicts NOTHING; any
measurement of these inside their experimental bands is consistent
with the framework but is not a confirmation. Disconfirmation of these
six would have to come from a different carrier (e.g., the unaudited
atmospheric-scale chain in [`NEUTRINO_MASS_DERIVED_NOTE.md`](NEUTRINO_MASS_DERIVED_NOTE.md))
or from a future framework extension; it is OUT OF SCOPE for this
synthesis.

The framework is therefore falsifiable with respect to the chamber-
chart's predicted subset: any future tension between the bracket
`[251.86°, 270.00°]` and the global δ_CP fit at > 3σ, OR a measurement
of `s_23^2` confirmed in the lower octant under NuFit-3σ-acceptable
correlated values, would refute the chamber-chart-as-PMNS-source
identification.

DUNE, T2HK, and JUNO measurements expected in the late 2020s will test
both forecasts. The δ_CP forecast in particular sits inside the
forthcoming sensitivity band and is the cleanest near-term test.

## 8. Companion: BAE / Koide structural foreclosure

This synthesis covers the PMNS chamber chart's PREDICTIVE-surface side.
A parallel campaign on the same days produced three structural
foreclosure results on the Koide-`Q` / BAE side, on a different
carrier (Hermitian circulant `Herm_circ(3)`) and a different question
(canonical-weighting selection on the `(trivial, doublet)` isotype
decomposition, and `U(1)_b` angular convention on the doublet plane):

- PR #1412 ([`BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md`](BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md))
  — consolidated bounded obstruction over a tested 9-attack-vector set
  AV1-AV9. Honest verdict: F1 multiplicity-weighting is not forced
  over F3 rank-weighting from the physical `Cl(3)`/`Z^3` framework baseline + retained authorities on the
  tested AV set; Koide `Q = 2/3` stays an empirical coincidence under
  current framework baseline. Open sub-locus: `U(1)_b` angular convention on the
  `C_3`-doublet plane.

- PR #1415 ([`BAE_U1B_CANONICAL_PHASE_NOTE_2026-05-17.md`](BAE_U1B_CANONICAL_PHASE_NOTE_2026-05-17.md))
  — stretch attempt on `U(1)_b`. Tested five named mechanisms; none
  supplies a canonical direction on `(Re b, Im b)`. Bounded narrowing:
  the maximal retained discrete subgroup of `O(2)` is dihedral `D_3`,
  whose fundamental-domain wedge is F3-shape, not F1-shape.

- PR #1419 ([`BAE_U1B_SIX_RAY_DIRAC_MEASURE_NOTE_2026-05-17.md`](BAE_U1B_SIX_RAY_DIRAC_MEASURE_NOTE_2026-05-17.md))
  — stretch attempt on the six-ray Dirac-measure sub-locus. Tested
  three sub-routes (S1-S3); all negative. Bounded narrowing: the six-
  ray locus `(R)` IS the maximal retained discrete-symmetry fix locus
  on the doublet plane, but no retained intersection of `<C_3, K, γ>`
  collapses `(R)` to a single-ray subset.

These three PRs are the negative-content companion to the present
PMNS-chamber-chart synthesis. They live on the `Herm_circ(3)` carrier,
not on the `H(m, δ, q_+)` chamber chart, and the two carriers are
independent. The PMNS chamber chart's predictive-surface partition
documented here is unaffected by the F1-vs-F3 / `U(1)_b` open sub-
locus.

This synthesis does not promote or amend the BAE / Koide results; it
records the cross-reference so that the architectural state of the
framework's Cycle 1 / 2 / 3 / 4 negative-content side is visible
alongside the Cycle 5a / 6a / 7 / 8 / 9 positive-content side.

## 9. What is NOT in this synthesis

The following observables and chains are OUT OF SCOPE for this
synthesis. Each has its own derivation chain on a different carrier
and its own separate audit status; consolidating them is NOT a goal of
this PMNS-chamber-chart synthesis:

- **Higgs mass numerical values.** Three values along three separate
  chains: 125.1 GeV (full 3-loop SM RGE in [`HIGGS_MASS_DERIVED_NOTE.md`](HIGGS_MASS_DERIVED_NOTE.md)),
  140.3 GeV (tree-level `m_H = v / (2 u_0)` in [`HIGGS_MASS_FROM_AXIOM_NOTE.md`](HIGGS_MASS_FROM_AXIOM_NOTE.md)),
  119.93 GeV (corrected-y_t RGE diagnostic). Out of scope.
- **Light quark masses.** Out of scope; quark-sector chains live on
  different carriers and are not consolidated here.
- **α_em.** Out of scope.
- **H_0 (Hubble).** Out of scope.
- **Λ (cosmological constant).** Out of scope.
- **Atmospheric mass-scale chain.** [`NEUTRINO_MASS_DERIVED_NOTE.md`](NEUTRINO_MASS_DERIVED_NOTE.md)
  (unaudited) predicts `m_3 ≈ 5.06 × 10^-2 eV`, `Δm²_31 ≈ 2.54 × 10^-3
  eV²` (within 3.5 % of NuFit) on a separate carrier but over-predicts
  `Δm²_21`. The synthesis here is independent of that open lane's
  status; Cycle 9 (PR #1452) explicitly does not alter it.
- **Direct quark-sector Yukawa coupling chains.** Out of scope.
- **Hostile-audit findings on adjacent PMNS notes**
  (`DM_LEPTOGENESIS_PMNS_*_NOTE_2026-05-17.md`,
  `LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE_2026-05-17.md`,
  etc.). Out of scope; these are audit-pipeline products on adjacent
  source notes, not on the chamber-chart predictive surface itself.

## 10. Cited source-note PRs (markdown links)

Five Cycle source notes (audit-lane-decided independently):

- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 5a (PR #1420)
- [`PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 6a (PR #1427)
- [`PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 7 (PR #1442)
- [`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 8 (PR #1447)
- [`PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 9 (PR #1452)

Three BAE / Koide companion source notes (negative-content side,
audit-lane-decided independently):

- [`BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md`](BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md)
  — PR #1412
- [`BAE_U1B_CANONICAL_PHASE_NOTE_2026-05-17.md`](BAE_U1B_CANONICAL_PHASE_NOTE_2026-05-17.md)
  — PR #1415
- [`BAE_U1B_SIX_RAY_DIRAC_MEASURE_NOTE_2026-05-17.md`](BAE_U1B_SIX_RAY_DIRAC_MEASURE_NOTE_2026-05-17.md)
  — PR #1419

Dependencies shared across the campaign. The status labels below are dated
2026-05-17 ledger snapshots; the oriented-cycle coordinate lemma's mutable
audit status is intentionally not pinned here:

- [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  — `retained_bounded / bounded_theorem`. Chamber-margin certificate at
  the PDG-central anchor; supplies the 200-bit mpmath interval
  arithmetic + interval Newton on the cubic char-poly + adjugate
  projectors reused by Cycles 5a / 6a / 7 / 8 / 9.
- [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — `bounded_theorem`; audit status not pinned here. For the separately
  supplied chamber matrix, extracts the forward-cycle coordinates exactly.
  It does not derive/fix the chart, carrier, or physical readout.
- [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — `retained_bounded / bounded_theorem`. Distinct-character algebra on
  the hw=1 triplet.
- [`NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md`](NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md)
  — `retained / positive_theorem`. Σm_ν functional form naming
  cosmological inputs `(L, Ω_b, Ω_DM, h)`.

Parent / structural references (status varies; audit-lane-decided):

- [`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
  — `unaudited / bounded_theorem`. PMNS-as-f(H) closure structure
  declaring eigenvector-only mapping and Majorana CP phases atlas-open.
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
  — `unaudited / positive_theorem`. Parent prediction note supplying
  the multistart Table 2 named external admission used by Cycles 7 / 8
  / 9.

## 11. Forbidden-imports check

- **No new framework premise.** the physical `Cl(3)` local algebra on the `Z^3` spatial substrate
  is unchanged. This synthesis introduces nothing beyond the five
  source-note PRs.
- **No new repo vocabulary.** All terms used in this synthesis
  ("chamber chart", "chamber margin", "box-Krawczyk", "interval
  Newton", "adjugate projector", "Basin 1", "chamber boundary", "PDG-
  central anchor", "image-overlap sub-box", "Jarlskog", "ReBox",
  "eigenvalue sign signature", "mass-blind") are repo-canonical or
  standard interval-arithmetic vocabulary already used by the five
  source notes. No new tags, no new class names, no new framings are
  introduced.
- **No status promotion.** This synthesis does not change the
  `effective_status` of any cited authority. Each cited PR is
  audit-lane-decided independently. The synthesis's claim type is
  `meta`; the audit lane has full authority on the synthesis itself.
- **No PDG values as derivation input.** The NuFit 5.3 NO 3-σ rectangle
  is the COMPARISON box for the labeling step in each cited source PR,
  not a derivation input. Cycle 9's empirical band `[0.0268, 0.0328]`
  on `Δm²_21 / Δm²_31` is the comparison band for the disjointness
  check, not a derivation input.
- **No fitted selectors.** All five source PRs use interval-arithmetic
  certification of algebraic identities, not numerical fits.
- **No load-bearing literature comparator.** The NuFit and KamLAND-Zen
  bands enter only as labeling-step admissions per the synthesis's
  cited source notes.
- **Status authority disclaimer prominent.** Synthesis's
  `effective_status` is generated by the audit pipeline only after
  independent audit review.

## 12. Audit-graph effect

This synthesis touches NO ledger rows directly (it is a `meta`
campaign-level synthesis). Each cited source note's audit graph effect
is the responsibility of its own PR. The synthesis's purpose is
descriptive: to make the architectural partition visible as a single
citeable record, so that future PRs proposing PMNS-chamber-chart-
predictive-surface extensions can point to the partition and the five
cycles' shared interval-arithmetic apparatus without re-deriving the
cascade.

## 13. Cross-references

- Canonical synthesis template:
  [`AUDIT_BACKLOG_NOTE_2026-05-02.md`](AUDIT_BACKLOG_NOTE_2026-05-02.md)
  (campaign-level synthesis with `proposal_allowed: false` and
  "not a new derivation" framing).
- Recent campaign synthesis (different campaign):
  [`KOIDE_BAE_30_PROBE_CAMPAIGN_NOTE_2026-05-09.md`](KOIDE_BAE_30_PROBE_CAMPAIGN_NOTE_2026-05-09.md)
  (terminal synthesis for the 30-probe BAE campaign, upstream of the
  Cycle 1-4 BAE / Koide foreclosure cited in §8).
- Adjacent recent synthesis (different gate):
  [`STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md)
  (single-gate synthesis on a different surface; cited as example of
  the `meta` / `bounded_theorem` synthesis distinction).
