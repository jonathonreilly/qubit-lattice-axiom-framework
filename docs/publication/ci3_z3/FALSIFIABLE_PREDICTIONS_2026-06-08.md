# Falsifiable Predictions — Honest Catalog (Publication Surface)

**Date:** 2026-06-08 (hardened: falsifier-inventory pass + NuFit-6.1 currency + tension-chase)
**Claim type:** meta (publication-surface catalog; backward-looking)
**Status authority:** independent audit lane only. This note sets no audit
verdict, promotes nothing, and introduces no new derivation, axiom, or fitted
value. It catalogs the framework's falsifiable forecasts and their **honest
standing against current data**, each pointing to its rigorous source note.
**Companion runner:**
[`scripts/audit_companion_falsifiable_predictions_catalog_2026_06_08.py`](../../../scripts/audit_companion_falsifiable_predictions_catalog_2026_06_08.py)
(SCORECARD PASS=N FAIL=0; re-states the headline numbers, current standings, and
falsifier margins, and cross-checks them against this note; defers rigorous
derivations to the cited per-prediction runners).
**Supersedes (currency):** the forecasts here postdate
`PREDICTION_SURFACE_2026-04-15.md`; the PMNS standings are refreshed to **NuFit-6.1
(Nov 2025)** per the companion note
`PMNS_DCP_FORECAST_STANDING_DEGRADES_UNDER_NUFIT6_BOUNDED_NOTE_2026-06-08`.

## Headline (read this first)

A 2026-06-08 falsifier-inventory pass + tension-chase sorted the forecasts on
this publication surface into:
**(A)** clean forward falsifier (sharp · derived-not-fit · a named experiment can
decisively kill it soon), **(B)** postdiction consistent-by-construction, **(C)**
too-wide / untestable-in-practice, **(D)** fit-conditional / parasitic.

**Bucket A is empty in this catalog.** The current publication surface identifies
**no clean, unconditional, forward falsifier**. Its sharpest near-term forecasts
(P1–P3) are
**exposed but conditional**, and the latest global fit (**NuFit-6.1**) now **leans
against** both flavor bets. Two predictions that look like tensions (`n_s`, `J`) are,
on inspection, **not independent tests of the axioms** — each re-expresses a chain
the framework already admits as un-derived (an imported inflation formula + an `N_e`
extrapolation; the β=6 coupling + the CKM `δ` admission), and each **dissolves under
its own chain/comparator uncertainty**. The impressive sub-% electroweak/QCD matches
are **postdictions calibrated through the imported β=6 plaquette**, not forward
falsifiers. The honest framing is the point: the framework's empirical content is
real but conditional, and where it is sharp it is currently unfavorable.

## Table A — exposed forward bets (sharp-ish, conditional, current data lean against)

NuFit-6.1 (Nov 2025) NO best fits used as the comparison window (named external).

| # | Observable | Framework forecast | Current standing (NuFit-6.1, sourced) | Falsifier | Bucket · status |
|---|---|---|---|---|---|
| **P1** | PMNS `δ_CP` | third quadrant, `δ_CP ∈ [251.86°, 270.00°]` (≈18° bracket; `sin δ_CP ≈ −0.987` at the anchor) | **disfavored-but-allowed.** NuFit-6.1 NO best fit `δ_CP = 207°` no-SK / `212°` with-SK; the band is **within** the 3σ range `[114°, 405°]` (not excluded) but the best fit is **outside** it. (Was a favorable "match" under the stale NuFit-5.3 T2K-driven framing.) | a 5σ DUNE / Hyper-K `δ_CP` (design ±15°) **outside** `[251.86°, 270.00°]` falsifies it (band at maximal-CP peak sensitivity) | **D** · unaudited; consumes NuFit `(s₁₂², s₁₃²)` as inputs |
| **P2** | PMNS `θ_23` octant | upper octant, `s₂₃² > 0.5` (certified `> 0.5277` over the NuFit-5.3 rectangle) | **disfavored.** NuFit-6.1 NO gives `s₂₃² = 0.470` in **both** the without-SK and with-SK fits (lower octant); the earlier NuFit-6.0 without-SK upper value (0.561) moved down. The upper-octant prediction is now against the central fit (though `s₂₃² > 0.5` is still inside the 3σ range `[0.432, 0.587]`). | a settled lower-octant determination (`s₂₃² < 0.5`) at significance (DUNE/NOvA/T2K/Hyper-K/JUNO) falsifies it | **D** · unaudited; same consumed rectangle |
| **P3** | Higgs vacuum | **conditional beyond-SM `y_t` signature** (not a robust binary): central-value stable — framework `y_t(v)=0.918` is below the `≈0.93` stability boundary, `λ(M_Pl)=0` — **but the framework's own ±3% `y_t` band `[0.890, 0.946]` straddles the boundary** (boundary 0.44σ_sys above center; Gaussian-tail diagnostic ~33% metastable under the source sigma convention; hard-interval fraction ~28%), and `y_t=0.918` rests on the open-gate `y_t(M_Pl)/g_s=1/√6` Ward identity | **weakly disfavored / not robust.** SM with current `m_t` is near-critical / metastable; the boundary `λ(M_Pl)=0` is an **admitted SM-shared input** (native derivation retired), so "stable" is a choice the SM can also make; ~0.75σ vs the SM `y_t` extraction, and the verdict flips inside the framework's own `y_t` systematic | a definitive **metastability** determination (precision `m_t`/`m_H`/`α_s`, `λ` at the high scale) — or a `y_t` lower-5σ bound above `≈0.93` — falsifies it (HL-LHC ~2030; FCC-ee 2040s) | **B** · unaudited; knife-edge in `y_t` (see robustness note) |

Honest no-prediction companions: the framework leaves **θ_12 and θ_13 unconstrained**
inside NuFit 3σ (it takes them as the inputs that pin the chamber preimage) — a
structural feature, not a fragility (source: the P1 note).

## Table B — two apparent tensions that are NOT independent axiom-tests

A dedicated chase (2026-06-08) found that the two predictions which look like they
"move against the data" each **re-express an already-admitted chain** and **dissolve
under their own uncertainties** — neither tests `{Lattice, Quantum, Record}`.

| # | Observable | Framework value | Current data (sourced) | Apparent pull | What it actually is |
|---|---|---|---|---|---|
| **T1** | CMB `n_s` | `0.9667` (`= 1 − 2/N_e`, `N_e ≈ 60`) | ACT DR6 2025: `0.974 ± 0.003` ([arXiv:2503.14452](https://arxiv.org/abs/2503.14452)); Planck 2018: `0.9649 ± 0.0042` | `−2.4σ` vs ACT; **`−0.4σ` vs Planck** | the **universal plateau/Starobinsky** formula `1 − 2/N_e` (not framework-distinctive; the framework's own first-principles result `1 − d/N_e = 0.95` is patched to it by an **underived** growth-noise term), riding an `N_e ≈ 60` **assumption** (the simulation reaches only `N_e ≈ 1.4`; `N_e ≈ 77` reproduces ACT). It is the **same** tension ACT inflicted on the entire plateau class. **Not an axiom-test.** |
| **T2** | Jarlskog `J` | `≈ 3.33×10⁻⁵` (NLO `J̄ = √5 α_s³(4−α_s)/288`; exact-matrix `3.331×10⁻⁵`; the LO atlas form `√5 α_s³/72 = 3.42×10⁻⁵`) | representative global-fit comparison windows used by the cited source chain span `≈ (3.00 ± 0.13)` to `(3.16 ⁺⁰·¹³₋₀·¹¹)×10⁻⁵` | `≈ +1.4σ` (vs 3.16) to `+2.6σ` (vs 3.00) — **mild, comparator-dependent** | the **imported** textbook Wolfenstein form `J = A²λ⁶η̄` over two non-clean inputs: `α_s` (the β=6 plaquette — the same input behind every mass; the excess **vanishes** if `α_s` drops ~2% into its bound) and `η = √5/6` (= the CKM `δ` admission `cos²δ = 1/n_quark`). The one robust, `α_s`-independent residual is `η = √5/6` sitting `≈ +1.8σ` above the global apex `η̄ ≈ 0.347` — a standing property of the **δ admission**, not a new falsifier. |

So T1/T2 are honest debits, but they **do not add independent empirical jeopardy
on this catalog surface**:
they restate the imported-plateau / `N_e`-extrapolation chain and the β=6-`α_s` ⊕
`δ`-admission chains respectively, and the publication surface's "no clean
forward falsifier identified" status is **unchanged**.

## Not forward falsifiers (stated to prevent over-quoting)

- **Precision EW/QCD postdictions** (`α_s`, `m_t`, `m_H`, `v`, `sin²θ_W`, `Δm²₃₁`):
  sub-% agreement, but **calibrated or bracketed through the imported β=6 plaquette**
  `⟨P⟩ = 0.5934` (itself the lattice comparator, with an open analytic-derivation
  gate) and convention knobs (`g_bare = 1`, `κ_EW`). Re-measuring these inputs
  re-calibrates the comparator rather than excluding the framework. `sin²θ_W`'s
  "−0.26%" hides a ~10σ nominal pull once the tiny experimental error is restored.
  **Do not quote these as predictions.**
- **Clean but untestable-in-practice** (bucket C): the Lorentz-violation `Y₄₀`
  cubic-harmonic fingerprint (distinctive, `retained_bounded`, but 7–18 orders below
  every current/foreseeable bound); proton decay (`τ_p ~ 4×10⁴⁷` yr, ~13 orders
  beyond Hyper-K); the 3-generation / 3-color counts (retrodictions). Distinctive,
  not near-term falsifiers.

## Honest conditionality (read before quoting any number)

1. **External comparison bands are not derived.** The NuFit (5.3 / 6.0 / 6.1) NO
   rectangles and bands, the ACT `n_s`, the J global-fit comparison windows,
   and the SM stability-boundary inputs are **named external admissions** used only as comparison windows /
   labeling steps — never as derived framework values.
2. **The PMNS forecasts (P1, P2) are conditional** on a preimage-localization
   admission and on the flavor/PMNS chain (downstream of the matter-content sector
   and the `AC_φλ` flavor admission); they are **unaudited**.
3. **The vacuum-stability forecast (P3) is conditional and not robust.** It is framed
   as a **discrimination test**, not a closure of `m_H`; and its headline binary is a
   **knife-edge in `y_t`**: the framework's own ±3% `y_t(v)=0.918` band `[0.890, 0.946]`
   straddles the stability boundary `≈0.93` (0.44σ_sys above center; ~33% Gaussian-tail
   diagnostic, ~28% hard-interval fraction), and `y_t=0.918` rests on the open-gate
   `y_t(M_Pl)/g_s=1/√6` Ward identity. The defensible content is a
   ~0.75σ beyond-SM `y_t` signature (framework `y_t` < SM `y_t≈0.94`), pending a tighter,
   audited `y_t` — see
   [`P3_VACUUM_STABILITY_KNIFE_EDGE_IN_YT_ROBUSTNESS_NARROW_THEOREM_NOTE_2026-06-08`](../../P3_VACUUM_STABILITY_KNIFE_EDGE_IN_YT_ROBUSTNESS_NARROW_THEOREM_NOTE_2026-06-08.md).
4. **Provenance discipline.** No NuFit / ACT / global-fit observable is consumed
   as a derived value; all are comparison windows. Status authority is the independent
   audit lane; the source notes are unaudited and these forecasts inherit that status.

## What would falsify the framework (one line each)

- **P1:** `δ_CP` measured at 5σ outside `[251.86°, 270.00°]` (DUNE/Hyper-K) — NuFit-6.1 best fit (207° no-SK / 212° with-SK) already leans this way.
- **P2:** `θ_23` settled in the lower octant (`s₂₃² < 0.5`) at significance — NuFit-6.1 already prefers it in both variants.
- **P3:** the electroweak vacuum shown to be metastable, **or** `y_t` pinned with a lower-5σ bound above the stability boundary `≈0.93` (the forecast is a knife-edge: the framework's own ±3% `y_t` band already straddles that boundary).
- **T1 / T2 are not independent axiom-tests** (see Table B): they restate already-admitted chains and dissolve under their own uncertainties.

A confirmation of P1–P3 would be a strong coordinated success; a clean violation of
any one (within its stated conditionality) is a falsification. As of this catalog
review the sharp forecasts are **conditional and currently unfavorable**, and this
publication surface identifies **no clean unconditional forward falsifier**.

## What this note does not claim

- Does **not** derive the PMNS chamber chart, the NuFit/ACT bands, `m_H`, `n_s`, or `J`;
  it catalogs forecasts and their current standing, deferring derivations to the cited notes.
- Does **not** promote any source note's status or assert an audit verdict.
- Introduces **no** new axiom, no new derivation, and no new repo vocabulary.

## Cited sources (markdown links)

- [`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](../../PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)
  — P1 (δ_CP third-quadrant bracket; θ_12/θ_13 no-prediction).
- [`PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md`](../../PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md)
  — P2 (θ_23 upper octant over the full NuFit rectangle).
- [`HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md`](../../HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md)
  — P3 (vacuum-stability discrimination test; framework `y_t(v)=0.918`).
- [`P3_VACUUM_STABILITY_KNIFE_EDGE_IN_YT_ROBUSTNESS_NARROW_THEOREM_NOTE_2026-06-08.md`](../../P3_VACUUM_STABILITY_KNIFE_EDGE_IN_YT_ROBUSTNESS_NARROW_THEOREM_NOTE_2026-06-08.md)
  — P3 robustness: the ±3% `y_t` band straddles the stability boundary (knife-edge); reframing to a conditional beyond-SM `y_t` signature.
- [`PRIMORDIAL_SPECTRUM_NOTE.md`](../../PRIMORDIAL_SPECTRUM_NOTE.md)
  — T1 (n_s; the growth-noise correction flagged `missing_bridge_theorem`).
- [`CKM_JARLSKOG_EXACT_NLO_CLOSED_FORM_THEOREM_NOTE_2026-04-25.md`](../../CKM_JARLSKOG_EXACT_NLO_CLOSED_FORM_THEOREM_NOTE_2026-04-25.md)
  — T2 (J NLO closed form).
- `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`
  — the two genuine admissions (`AC_φλ`, `θ`) the flavor forecasts are conditional on.

The PMNS `δ_CP` / `θ_23` NuFit-6.1 standing refresh is carried by the companion note
`PMNS_DCP_FORECAST_STANDING_DEGRADES_UNDER_NUFIT6_BOUNDED_NOTE_2026-06-08` (cited by
name to keep the citation graph to on-surface authorities).
