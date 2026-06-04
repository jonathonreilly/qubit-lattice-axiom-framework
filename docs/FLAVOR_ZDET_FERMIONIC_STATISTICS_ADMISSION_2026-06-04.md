# Flavor — Z=det(D+J) reduces to a single fermionic-statistics admission (matter is fermionic, not bosonic); it is not forced by the axioms, fully discharges the log-det det⁺¹ factor, and only partially serves the Koide chirality gate (shared ancestor, distinct atoms)

**Date:** 2026-06-04
**Claim type:** localization + admission identification (names the single remaining log-det factor as one fermionic-statistics admission; disproves it is forced; bounds its multi-gate keep). A candidate Tier-A input for user approval. Not a value derivation.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not edit, re-cite, or promote any existing row.
**Runner:** `scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py` (SCORECARD 6/6).

## Context
The log-det generator `W = log|det(D+J)|` (dominant blocker, 59 rows) has three factors: **(1)** additivity
[Record axiom — closed], **(2)** det multiplicative-character + log [audit-ready math], **(3)** *why
`Z=det`*. Factors 1–2 are supplied; this note resolves factor 3.

## Result — `Z=det` reduces to one fermionic-statistics admission, and it is not forced
- **The qubit `Cl(3,0)` does not force the fermionic frame.** `Cl(3,0)` is a spinor *module*: its
  anticommutation `{γ_i,γ_j}=2δ` is among on-site *operators*, not the matter *amplitudes* (c-numbers).
  The axioms' **native cross-site product is commuting (bosonic)** — verified: bare ladder operators on
  different sites commute. The anticommuting frame requires a **Jordan-Wigner string** (`c_x = (∏_{y<x}σ³)σ⁺`),
  a change of generators not supplied by Lattice+Quantum+Record (verified `{c₁,c₂}=0`).
- **The disproof — dimension is blind to fermion-vs-hard-core-boson.** Per-site dim-2 (the retained
  `grassmann_forcing_bridge`) excludes only the *free* boson (dim ∞). The **hard-core boson** is dim-2
  (`(σ⁺)²=0`) *and* commutes cross-site → yields `1/det` (permanent / bosonic), not `det`. So dimension
  cannot select the fermion; the discriminator is **cross-site statistics** (signed `det` vs unsigned
  `permanent`, verified distinct), and the axioms fix neither. Reflection positivity passes for both the
  fermionic `det⁺¹` and the bosonic `det⁻¹ᐟ²`; the additive baseline vanishes for both; the single-site
  Clifford `(−1)^F` grading is the wrong factor (`Z=det` needs *cross-site* anticommutation).

So factor 3 is precisely **one admission FS:** *"matter integrates as a fermionic (Grassmann /
anticommuting) degree of freedom, not a bosonic (commuting) one."* It is physically standard, and
**not forced** by the three axioms.

## Multi-gate keep — asymmetric (the honest scope)
- **Fully discharges `Z=det`.** With the already-retained pieces — `spin_statistics_berezin_determinant`
  (`Z_F=det`, retained_bounded), `grassmann_forcing_bridge` (dim-2, retained_bounded),
  `staggered_only_det_positivity_case_a` (retained) — plus the audit-ready det-character math, FS yields
  `Z=det(D+J)` and thereby the `det⁺¹` content of the **59-row log-det cluster**.
- **Only partially serves Koide.** `Z=det` (cross-site Z³ *spatial* Fermi statistics) and the Koide
  chirality gate (anticommutation with `Γ_χ=(2/3)J−I` on the *internal generation* R³, splitting the C₃
  orbit) share a **fermionic-frame ancestor** but are **two distinct atoms on different factors**.
  Verified: `Γ_χ` is circulant (eig `{−1,−1,1}`) and **commutes** with every C₃-equivariant mass operator,
  so the spatial frame does not supply the generation chiral grading — which remains blocked by the
  retained_bounded `koide_z3_equivariant_anticommuting_no_go`. FS gives Koide the ambient graded category
  only; its chiral grading is a **separate live import**. (Earlier framing that `Z=det` *is* the same
  admission as the Koide gate is an overclaim, corrected here.)

## For the user — adoption decision
FS is a candidate **single Tier-A input** (no imports without user approval, per repo policy): adopting
*"matter integrates anticommuting/Grassmann"* discharges the `det⁺¹` factor gating ~59 log-det rows
(combined with the retained Berezin / dim-2 / det-positivity pieces). It is physically standard and
judicious for the log-det cluster; it does **not** close the Koide chirality gate. The user decides
adoption; this note delivers the assessment and the precise statement + asymmetric keep.

## Status-citation flag (for the audit lane, not changed here)
The `staggered_dirac_substep1_statistics_agnostic_no_forcing` note is `effective_status = unaudited` on
`origin/main`; some notes cite it as `retained_no_go` (stale). Surfaced for the independent audit lane via
the source-note channel; not altered here.

## The next paths this opens (not closing)
- **Force FS:** does a spin-statistics / OS-positivity principle in a continuum limit force the
  anticommuting (`det⁺¹`) orientation over the equally-RP-passing hard-core-boson (`1/det`)? The three
  axioms supply no dynamics/action/continuum structure to drive it — likely needs a 4th structural input.
- **Koide transport:** whether any single principle forces *both* the cross-site CAR sign and the internal
  generation `Γ_χ` — currently obstructed by the retained no-go (the spatial frame does not transport to
  the generation factor).

## Provenance (verified 2026-06-04)
- Berezin Gaussian = det; native cross-site commuting; JW string → CAR; hard-core boson dim-2 + commuting;
  det ≠ permanent; `Γ_χ` circulant commuting with C₃-equivariant `H`: verified directly (runner 6/6).
  Retained anchors confirmed on origin/main (`spin_statistics_berezin_determinant`,
  `staggered_dirac_substep1_grassmann_forcing_bridge`, `staggered_only_det_positivity_case_a`,
  `koide_z3_equivariant_anticommuting_no_go`).
- This note sets no audit status; it names the single fermionic-statistics admission and its asymmetric
  keep, and surfaces (does not change) the stale status citation.
