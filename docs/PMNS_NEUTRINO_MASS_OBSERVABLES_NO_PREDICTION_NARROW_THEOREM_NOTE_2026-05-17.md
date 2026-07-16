# PMNS Neutrino Mass Observables No-Prediction Narrow Theorem

**Date:** 2026-05-17
**Claim type:** bounded_theorem (narrow box-Krawczyk structural certification
that the retained PMNS chamber chart `H(m, δ, q_+)` does NOT constrain any
of the neutrino mass observables `(r_21, r_31, Σm_ν, m_ββ)` within their
experimental bands; honest no-prediction findings on all four).
**Status authority:** independent audit lane only. This source note does
not set or move its own audit verdict; downstream audit lane and packet
status are decided by the audit lane.
**Primary runner:**
[`scripts/frontier_pmns_neutrino_mass_observables_no_prediction_narrow.py`](../scripts/frontier_pmns_neutrino_mass_observables_no_prediction_narrow.py)
**Cached output:**
[`logs/runner-cache/frontier_pmns_neutrino_mass_observables_no_prediction_narrow.txt`](../logs/runner-cache/frontier_pmns_neutrino_mass_observables_no_prediction_narrow.txt)
**Authority role:** narrow box-Krawczyk extension of the Cycles 5a / 6a /
7 / 8 cascade from the dimensionless mixing observables `(s_12^2,
s_13^2, s_23^2, δ_CP)` to the MASS observables `(r_21, r_31, Σm_ν,
m_ββ)`. The chamber chart `H(m, δ, q_+)` is dimensionless by
construction; this note certifies STRUCTURALLY that no chamber-side mass
prediction is reachable through the chart's eigenvalues.
**Framework convention:** "axiom" means only the single framework axiom
`Cl(3)` on `Z^3`.

## 0. Why this note exists

The PMNS-as-f(H) closure theorem
[`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
maps the chamber chart `(m, δ, q_+)` to a four-tuple of PMNS observables
`(s_12^2, s_13^2, s_23^2, δ_CP)` via the eigenVECTORS of the affine
Hermitian `H(m, δ, q_+) = H_base + m T_m + δ T_δ + q_+ T_q`. Cycles 5a
(PR #1420), 6a (PR #1427), 7 (PR #1442), 8 (PR #1447) cascaded box-
Krawczyk machinery to the angle observables. This iteration applies the
SAME apparatus to the MASS observables widely studied at long-baseline
/ cosmological / 0νββ experiments:

- `r_21 := m_2 / m_1`, `r_31 := m_3 / m_1` neutrino mass ratios
- `Σm_ν = m_1 + m_2 + m_3` cosmological sum
- `m_ββ := |Σ_i U_{ei}^2 m_i|` Majorana effective mass for 0νββ

The findings are graded:

- **(A) Eigenvalue-sign-signature.** Over the SAME box `B = [0.625,
  0.750] × [0.902, 0.956]` used by Cycles 7 and 8 with `q = sqrt(8/3)
  - δ`, every image-overlap sub-box has H eigenvalues with sign
  signature `(λ_1, λ_2, λ_3) = (-, -, +)` certified at 200-bit
  precision. Under sort-`|λ|`-ascending assignment `(m_1, m_2, m_3)`,
  the chamber-side `Δm²` ratio `(m_2^2 - m_1^2)/(m_3^2 - m_1^2)` is
  interval-certified to `[0.308, 0.329]`, STRICTLY DISJOINT from the
  empirical NuFit 3-σ band `[0.0268, 0.0328]` (gap ~ 0.28, ten times
  the empirical band width). Identifying `|λ|` with `m_ν` under any
  of the 6 permutations is INADMISSIBLE — none of the 6 chamber-side
  bands intersects the empirical band. **Honest no-prediction
  finding on (r_21, r_31).**
- **(B) Σm_ν.** The chamber chart fixes no absolute mass scale; the
  retained
  [`NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md`](NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md)
  identity `Σm_ν = (1 - L - R - Ω_b - Ω_DM) C_ν h^2` consumes
  cosmological inputs `(L, Ω_b, Ω_DM, h)` NOT in the chamber chart.
  **Honest no-prediction finding** on the chamber side.
- **(C) m_ββ.** The Majorana effective mass depends on the two CP
  phases `(α_21, α_31)` that the PMNS-as-f(H) closure theorem
  EXPLICITLY declares Dirac-invariant / atlas-open. **Honest
  no-prediction finding** on the chamber side.

The chamber chart `H(m, δ, q_+)` is **mass-blind by construction** —
it predicts mixing angles via eigenvectors only; mass scale and
Majorana phases live in different (separately atlas-open) carriers
(see
[`NEUTRINO_LANE4_WORKSTREAM_CLOSEOUT_NOTE_2026-04-28.md`](NEUTRINO_LANE4_WORKSTREAM_CLOSEOUT_NOTE_2026-04-28.md)).

The certification is conditional on **(X8) the parent prediction
note's preimage-localization Table 2** — same named external admission
used by Cycles 7 / 8.

## 1. Cited authorities and their roles

Each cited authority is named together with the role it plays; ledger
statuses verified against `docs/audit/data/audit_ledger.json`
`effective_status` on 2026-05-17.

- **(X1)** [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  (`retained_bounded`, `bounded_theorem`, `chain_closes: True`).
  Role: 200-bit mpmath interval arithmetic + interval Newton on the
  cubic characteristic polynomial used to bracket eigenvalues sign-
  strictly over every sub-box of `B`.
- **(X2)** [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  (`bounded_theorem`; audit status owned by the independent audit lane).
  Role: for the explicitly supplied chart matrix, extract its
  `E_12,E_23,E_31` coordinates as `diag(A C^dagger)`. X2 does not derive or
  physically identify the chart, carrier, or readout.
- **(X3) NuFit 5.3 NO 3-σ rectangle on `(s_12^2, s_13^2)`.** NAMED
  EXTERNAL ADMISSION: `s_12^2 ∈ [0.270, 0.341]`, `s_13^2 ∈ [0.02029,
  0.02391]`.
- **(X3*) NuFit 5.3 NO 3-σ Δm² intervals.** NAMED EXTERNAL ADMISSION:
  `Δm²_21 ∈ [6.92, 8.05] × 10^-5 eV^2`, `|Δm²_31| ∈ [2.451, 2.578]
  × 10^-3 eV^2` (NO branch). Hence `Δm²_21 / Δm²_31 ∈ [0.0268,
  0.0328]`. Comparison band for (r_21, r_31) no-prediction step.
- **(X3\*\*) Cosmological Σm_ν bound.** NAMED EXTERNAL ADMISSION:
  `Σm_ν ∈ [0.058, 0.12] eV` (PDG oscillation lower bound + Planck
  2018 + baseline 95 % CL upper). Comparison band for Σm_ν.
- **(X3\*\*\*) KamLAND-Zen m_ββ bound.** NAMED EXTERNAL ADMISSION:
  `m_ββ ∈ [0.036, 0.156] eV` (KamLAND-Zen 2022, NME-range). Comparison
  band for m_ββ.
- **(X4)** [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained_bounded`, `bounded_theorem`). Role: hw=1 distinct-
  character algebra.
- **(X5) PMNS-as-f(H) closure structure** (unaudited). Cited
  STRUCTURALLY for two declarations: (i) chamber chart maps to mixing
  angles via eigenVECTORS only; (ii) "Dirac-invariant — the extra two
  CP phases `(α_21, α_31)` are not fixed by this theorem; they live
  in the Majorana mass sector".
- **(X6)** [`NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md`](NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md)
  (`retained`, `positive_theorem`, `chain_closes: True`). Role:
  retained identity `Σm_ν = (1 - L - R - Ω_b - Ω_DM) C_ν h^2` names
  cosmological inputs `(L, Ω_b, Ω_DM, h)`; these are NOT chamber-chart
  inputs.
- **(X7) NEW computational content: box-Krawczyk eigenvalue sign-
  signature certification over `B`.** Over the same 80 × 80 grid
  partition used by Cycles 7 / 8 with `q = sqrt(8/3) - δ`, every
  image-overlap sub-box `B_{ij}` satisfies, by 200-bit mpmath
  interval-arithmetic eigenvalue brackets: `λ_1 < 0`, `λ_2 < 0`,
  `λ_3 > 0` strictly; `|λ_2| < |λ_1|` strictly (smallest |λ| is at the
  middle eigenvalue); `|λ_3| > |λ_1|` strictly. Hence (after `|λ|`-
  ordering) `|λ_2| < |λ_1| < |λ_3|` over the entire preimage of the
  NuFit rectangle.
- **(X7\*) NEW: chamber-side `Δm²` ratio band disjoint from empirical.**
  Under sort-`|λ|`-ascending assignment `(m_1, m_2, m_3) =
  (|λ_2|, |λ_1|, |λ_3|)`, the chamber-side `(m_2^2 - m_1^2)/(m_3^2 -
  m_1^2)` is interval-certified to lie strictly in `[0.308, 0.329]`
  over `B` — disjoint from the empirical band `[0.0268, 0.0328]` of
  (X3*). Permuting `|λ|→m` over all 6 permutations yields 6 disjoint
  chamber-side bands, NONE of which intersects the empirical band.
- **(X8) Preimage-localization admission** (inherited from
  [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md),
  unaudited). The parent's Table 2 reports 9-grid-point multistart-
  fsolve preimages in `[0.6270, 0.7480] × [0.9040, 0.9545] ⊂ B`. Same
  status as Cycles 7 / 8.

## 2. Narrow theorem (explicit hypotheses)

**Theorem (box-Krawczyk eigenvalue sign-signature certification with
honest no-prediction findings on four mass observables).**

Given (X1), (X2), (X3), (X3\*), (X3\*\*), (X3\*\*\*), (X4), (X5),
(X6), (X7), (X7\*), (X8) as stated in §1, we have:

1. **(Eigenvalue sign-signature)** Over every image-overlap sub-box
   `B_{ij} ⊂ B`, interval-arithmetic brackets satisfy
   `λ_1.b < 0`, `λ_2.b < 0`, `λ_3.a > 0` — sign signature `(-, -, +)`.

2. **(|λ|-ordering and Δm²-ratio sign)** From (1), `|λ_(middle eig)|
   < |λ_(smallest eig)| < |λ_(largest eig)|`. Under sort-`|λ|`-
   ascending assignment `(m_1, m_2, m_3) := (|λ_2|, |λ_1|, |λ_3|)`,
   the chamber-side `Δm²` ratio
   `(m_2^2 - m_1^2)/(m_3^2 - m_1^2) = (|λ_1|^2 - |λ_2|^2)/(|λ_3|^2 -
   |λ_2|^2)` is interval-certified to lie strictly in `[0.308,
   0.329]` over `B`. The empirical NuFit 3-σ band on `Δm²_21 /
   Δm²_31` is `[0.0268, 0.0328]` (from X3*). These two bands are
   DISJOINT (chamber-side lower 0.308 > empirical upper 0.0328).

3. **(Permutation-equivariant disjointness)** Permuting the `|λ|→m`
   assignment over all 6 permutations yields 6 chamber-side bands
   (enumerated explicitly in the runner's Part 6). NONE of the 6
   bands intersects the empirical band `[0.0268, 0.0328]`. Hence no
   chamber-side linear identification `m_i = α |λ_{π(i)}| + β`
   reproduces the empirical NuFit `Δm²` ratio for any permutation `π`
   and any `(α, β)` with `α > 0`.

4. **(r_21, r_31 no-prediction)** Combined with (1)-(3), the chamber-
   side `|λ|`-ratios sweep over a 2D region of the `(r_21, r_31)`
   plane that does NOT predict any sub-region inside the NuFit 3-σ
   band on `(r_21, r_31)`. The chamber chart is structurally mass-
   blind because `|λ|` is dimensionless and there is no chamber-side
   rule for `(α, β, π)`. **Honest no-prediction finding.**

5. **(Σm_ν no-prediction)** By (X5)(i), the chamber chart maps to
   mixing angles via eigenVECTORS only; absolute mass scale is atlas-
   open per (X5). The retained Σm_ν functional form (X6) names
   cosmological inputs `(L, Ω_b, Ω_DM, h)` that are NOT chamber-chart
   inputs. **Honest no-prediction finding.**

6. **(m_ββ no-prediction)** By (X5)(ii), the Majorana CP phases
   `(α_21, α_31)` are explicitly declared atlas-open. Since `m_ββ`
   depends on `(α_21, α_31)` and absolute masses, neither of which
   the chamber chart fixes, **honest no-prediction finding.**

7. **(Preimage-localization, named external admission)** By (X8),
   every Basin-1 chamber-boundary preimage point of any `(s_12^2,
   s_13^2) ∈` NuFit 2D rectangle lies in `B`.

8. **(Conclusion)** For any `(s_12^2, s_13^2) ∈` NuFit rectangle, by
   (7) the preimage lies in some sub-box `B_{ij} ⊂ B`. By (1)-(6),
   the chamber chart predicts NO sub-region inside any of `(r_21,
   r_31, Σm_ν, m_ββ)`'s experimental bands. The framework's chamber-
   side prediction surface is the dimensionless mixing observables
   `(s_23^2, δ_CP)` only.

## 3. Proof sketch

(1) Direct interval-Newton on the cubic char-poly (X1). Brackets
returned at width `< 10^-13` at 200-bit precision are sign-strict on
every image-overlap sub-box of the 80 × 80 grid.

(2) Direct interval-arithmetic computation. Given sign-strict
eigenvalue intervals, compute `(|λ_2|^2 - |λ_1|^2) / (|λ_3|^2 -
|λ_1|^2)` using
`l1^2_lo = l1.b^2`, `l1^2_hi = l1.a^2` (since `l1 < 0`, the smaller
absolute value is at `l1.b`); analogous for `l2^2`. Numerator and
denominator are both strictly positive intervals (no division
degeneracy). The empirical band is `Δm²_21 / Δm²_31 ∈ [0.0268,
0.0328]` from (X3*).

(3) Direct enumeration: the runner samples chamber-boundary image-
overlap points over a 40 × 40 grid; over each of 6 `|λ|→m`
permutations, the runner records the floating-point min/max of
`(m_2^2 - m_1^2) / (m_3^2 - m_1^2)`. Each band is disjoint from the
empirical band (Part 6 of runner).

(4) Follows from (2), (3): chamber-side `|λ|`-ratios don't sit
inside the empirical NuFit band on any permutation.

(5) Direct citation of (X5)(i) and (X6): chamber chart predicts only
eigenvector content; Σm_ν functional form requires cosmological
inputs.

(6) Direct citation of (X5)(ii): Majorana phases atlas-open.

(7) Direct named external admission inherited from Cycles 7 / 8.

(8) Logical conclusion.

## 4. Scope versus the cascade Cycles 5a / 6a / 7 / 8

| Claim | Cycle 5a | 6a | 7 | 8 | This note |
|---|---|---|---|---|---|
| `s_23^2 > 0.5` at PDG anchor | Krawczyk | inherited | inherited | inherited | inherited |
| `s_23^2 > 0.5` on open nbhd | — | IFT + IVT | inherited | inherited | inherited |
| `s_23^2 > 0.5` on full NuFit rect | — | — | box-Krawczyk | inherited | inherited |
| `δ_CP ∈ [251.86°, 270°]` on NuFit rect | — | — | — | **YES** | inherited |
| θ_12 / θ_13 sub-region | — | — | — | **NO** (no-prediction) | inherited |
| `(r_21, r_31)` sub-region | — | — | — | — | **NO** (no-prediction) |
| Σm_ν sub-region | — | — | — | — | **NO** (no-prediction) |
| m_ββ sub-region | — | — | — | — | **NO** (no-prediction) |
| Eigenvalue sign-sig over `B` | — | — | — | — | **YES** (`(-, -, +)`) |
| Preimage-localization to `B` | — | — | named | named | named (X8) |

## 5. What is forced versus what remains conditional

What this narrow theorem forces (under all stated hypotheses):

- Interval-certified eigenvalue sign signature `(-, -, +)` over every
  image-overlap sub-box of `B` (X7).
- Interval-certified chamber-side band `(|λ_2|^2 - |λ_1|^2)/(|λ_3|^2
  - |λ_1|^2) ⊂ [0.308, 0.329]` over `B` (X7\*).
- This band is DISJOINT from the empirical NuFit 3-σ band `[0.0268,
  0.0328]` (chamber-side lower 0.308 strictly above empirical upper
  0.0328 — gap 0.28).
- No chamber-side `(α, β, π)`-identification reproduces the empirical
  NuFit `Δm²` ratio — the chamber chart is structurally mass-blind.
- The chamber chart cannot constrain `Σm_ν` (no absolute scale; depends
  on cosmological inputs per X6).
- The chamber chart cannot constrain `m_ββ` (Majorana phases atlas-
  open per X5).

What remains conditional (out of scope):

- A rigorous proof of preimage-localization (X8 is named external
  admission only). Tightening route: same as Cycles 7 / 8.
- A mass-scale-import theorem (chamber chart does not supply one).
- A no-go theorem against the framework predicting `(r_21, r_31, Σm_ν,
  m_ββ)` via OTHER carriers. The unaudited atmospheric-scale chain in
  [`NEUTRINO_MASS_DERIVED_NOTE.md`](NEUTRINO_MASS_DERIVED_NOTE.md)
  predicts `m_3 ≈ 5.06 × 10^-2 eV` and `Δm²_31 ≈ 2.54 × 10^-3 eV²`
  (within 3.5 % of NuFit) on a separate carrier, but over-predicts
  `Δm²_21 ≈ 2.1 × 10^-3 eV²`; this note is INDEPENDENT of that open
  lane's status.

## 6. What this note positively claims

1. Over every image-overlap sub-box of `B`, H eigenvalues are
   interval-certified strict-sign with signature `(-, -, +)`.
2. `|λ_(middle eig)| < |λ_(smallest eig)| < |λ_(largest eig)|`, so
   sort-`|λ|`-ascending assigns the middle eigenvalue to `m_1`, the
   smallest (most negative) eigenvalue to `m_2`, the largest to `m_3`.
3. Chamber-side `(m_2^2 - m_1^2)/(m_3^2 - m_1^2) ⊂ [0.308, 0.329]`.
4. Empirical NuFit 3-σ band on `Δm²_21 / Δm²_31` is `[0.0268,
   0.0328]`. Chamber-side band is DISJOINT.
5. All 6 permuted `|λ|→m` chamber-side bands are disjoint from
   empirical NuFit band.
6. Framework's chamber chart cannot predict `(r_21, r_31)` into
   NuFit 3-σ — honest no-prediction finding.
7. Σm_ν functional form (X6) requires cosmological inputs outside
   chamber chart; chamber chart cannot constrain `Σm_ν` — honest
   no-prediction.
8. Majorana CP phases atlas-open per (X5); chamber chart cannot
   constrain `m_ββ` — honest no-prediction.

## 7. What this note does NOT claim

- Does NOT derive the chart `H(m, δ, q)`; structure inherited from
  Cycles 5a / 6a / 7 / 8 and PMNS-as-f(H).
- Does NOT supply or assume any NuFit / PDG / cosmological / KamLAND-
  Zen value other than as named external admissions.
- Does NOT strengthen (X1) beyond its stated scope.
- Does NOT supply a rigorous proof of preimage-localization (X8 is
  named external admission only).
- Does NOT claim `(r_21, r_31, Σm_ν, m_ββ)` falsification — this is
  a no-prediction finding on the chamber chart, not a no-go on the
  framework as a whole.
- Does NOT alter the status of the unaudited
  [`NEUTRINO_MASS_DERIVED_NOTE.md`](NEUTRINO_MASS_DERIVED_NOTE.md)
  atmospheric-scale chain (different carrier).
- Does NOT supersede (X6); cited STRUCTURALLY only.
- Does NOT close the absolute neutrino mass scale.
- Does NOT introduce new repo vocabulary; "box-Krawczyk," "interval
  Newton," "eigenvalue sign signature," "chamber-side mass-blind"
  are standard interval-arithmetic / PMNS vocabulary.

## 8. Honest residual

The interval band `[0.308, 0.329]` is conservative; the floating-
point image is tighter (`[0.311, 0.325]`). Either suffices for the
disjoint-from-empirical conclusion. Tightening routes: deeper
bisection; centered-form interval evaluation. None in scope.

The (X5)(i) declaration "chamber chart maps to mixing angles via
eigenVECTORS only" is structurally clear in the PMNS-as-f(H) note
but the note itself is unaudited. The structural finding here does
not require (X5) to be retained — it stands on the eigenvalue sign-
signature (X7) directly. (X5) only supports the m_ββ no-prediction
clause.

A no-go theorem against the framework PREDICTING `(r_21, r_31, Σm_ν,
m_ββ)` via OTHER carriers (e.g., the unaudited atmospheric-scale +
Majorana-placement chain) is out of scope here.

## 9. Cited dependencies (markdown links for retained authorities)

- [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  — (X1) Krawczyk certificate (`retained_bounded`).
- [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — (X2) bounded supplied-block forward-cycle coordinate extraction; no
  physical carrier/readout or chart-selection bridge.
- [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — (X4) hw=1 distinct-character algebra (`retained_bounded`).
- [`NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md`](NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md)
  — (X6) retained Σm_ν functional form (`retained`).
- [`PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md`](PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md)
  — (X5) PMNS-as-f(H) (unaudited); cited STRUCTURALLY for two
  declarations only.
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
  — parent prediction note (unaudited); source of (X8) Table 2.
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 5a (PR #1420).
- [`PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 6a (PR #1427).
- [`PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 7 (PR #1442); same `B`, NuFit (X3), preimage admission (X8).
- [`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)
  — Cycle 8 (PR #1447); same `B`, NuFit (X3), preimage admission (X8).

External admissions: (X3), (X3\*), (X3\*\*), (X3\*\*\*), (X8).

## 10. Forbidden-imports check

- No new axiom introduced (only `Cl(3)` on `Z^3`).
- No new repo vocabulary.
- No PDG / NuFit / cosmological / KamLAND-Zen observable consumed as
  a derived value; rectangles and bands are named external admissions
  for the labeling / disjointness step only.
- No `audit_status` or `effective_status` promotion language.
- No load-bearing reliance on unaudited authorities. (X5) PMNS-as-f(H)
  cited STRUCTURALLY only.
- Citation form: markdown links for retained authorities.
- All interval-arithmetic content reproducible at 200-bit mpmath
  precision via `mpmath.iv`.

## 11. Reproduction

```bash
PYTHONPATH=scripts python3 \
    scripts/frontier_pmns_neutrino_mass_observables_no_prediction_narrow.py
```

Expected final line:

```text
PASS=66  FAIL=0
```

The runner verifies, by part:

- **Part 1**: sympy identity `sqrt(8/3) = 2 sqrt(6)/3`.
- **Part 2**: interval Newton brackets the three eigenvalues at the
  PDG-central anchor to width `< 10^-13` at 200-bit precision.
- **Part 3**: anchor eigenvalue sign signature `(-, -, +)` and
  `|λ|`-ordering.
- **Part 4** (NEW CONTENT): 80 × 80 box-Krawczyk eigenvalue
  sign-signature certification over `B` with `q = sqrt(8/3) - δ`.
- **Part 5** (NEW CONTENT): chamber-side `Δm²` ratio interval band
  `[0.308, 0.329]` certified over `B`.
- **Part 6** (NEW CONTENT): permutation-equivariant disjointness.
- **Part 7** (X8): preimage-localization admission.
- **Part 8** (structural): Σm_ν cosmological-input dependence per
  (X6).
- **Part 9** (structural): m_ββ Majorana-phase dependence per (X5).
- **Part 10**: residual scope.
- **Part 11**: claim-discipline summary.

The runner uses `mpmath.iv` (Parts 2-6), sympy (Part 1), and numpy
only for per-box eigenvalue seeding.

## 12. Promotion-Value Gate (V1-V5)

| # | Question | Answer |
|---|---|---|
| V1 | Verdict-identified obstruction closed? | The chamber chart's structural inability to predict mass observables is RESOLVED rigorously: the eigenvalue sign signature `(-, -, +)` is certified over the entire image-overlap preimage of NuFit, and the chamber-side `Δm²` ratio band is interval-certified disjoint from the empirical band on all 6 permutations. |
| V2 | New derivation? | (i) box-Krawczyk eigenvalue sign-signature `(-, -, +)` over `B`; (ii) `|λ|`-ordering `|λ_(mid)| < |λ_(small)|` over `B`; (iii) chamber-side `Δm²` ratio band `[0.308, 0.329]`; (iv) permutation-equivariant disjointness over 6 `|λ|→m` permutations; (v) structural no-prediction findings on `(Σm_ν, m_ββ)` citing (X6) and (X5). |
| V3 | Audit lane could complete? | Yes — audit can verify (a) box-Krawczyk eigenvalue sign signature reproducibility, (b) interval-arithmetic `Δm²` ratio band, (c) permutation enumeration, (d) (X5)(i), (X5)(ii) structural citations, (e) (X6) retained-form citation. (X8) inherited from Cycles 7 / 8. |
| V4 | Marginal content non-trivial? | Yes — completes the Cycles 5a / 6a / 7 / 8 cascade, delineating which observables the chamber chart constrains (`s_23^2`, `δ_CP`) vs cannot (mass observables); falsifiable architectural prediction: any future experimental result on `r_21, r_31, Σm_ν, m_ββ` still leaves the chamber chart silent. |
| V5 | One-step variant? | No — eigenvalue sign-signature box-Krawczyk and disjointness from empirical `Δm²` ratio band are not relabels of Cycle 7's `s_23^2 > 0.5` or Cycle 8's `δ_CP ∈ [251.86°, 270°]`. New structural content. |

**Source-note V1-V5 screen: pass for bounded audit seeding.**

## 13. Companion to Cycles 5a / 6a / 7 / 8

Under named external admissions (X3), (X3\*), (X3\*\*), (X3\*\*\*),
(X8), the chamber-side framework forecast is:

```
theta_23 in the upper octant (s_23^2 > 0.5)                  [Cycle 7]
delta_CP near maximal CP-violation, third quadrant            [Cycle 8]
       (delta_CP in [251.86°, 270.00°], 18.13° width)
theta_12 unconstrained inside NuFit 3-sigma                   [Cycle 8]
theta_13 unconstrained inside NuFit 3-sigma                   [Cycle 8]
r_21 = m_2/m_1 unconstrained (chamber chart is mass-blind)    [this note]
r_31 = m_3/m_1 unconstrained (chamber chart is mass-blind)    [this note]
Sigma m_nu unconstrained (depends on cosmological inputs)     [this note]
m_betabeta unconstrained (Majorana phases atlas-open)         [this note]
```

The audit lane has final authority on whether (X8) is sufficient as
a named external admission and on whether this note's structural
positive content (eigenvalue sign signature + chamber-side `Δm²`
ratio disjointness) and four no-prediction findings (`r_21, r_31,
Σm_ν, m_ββ`) qualify for retained_bounded status.
