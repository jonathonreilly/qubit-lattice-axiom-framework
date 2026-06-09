# P3 Vacuum-Stability Forecast Robustness: "Absolutely Stable" Is a Knife-Edge — the Framework's Own ±3% `y_t` Band Straddles the Stability Boundary

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** robustness / conditionality analysis of an existing prediction (quantitative straddle + reframing)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Scope:** pressure-test of the headline P3 vacuum-stability forecast
([`HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03`](HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md)).
It does **not** dispute that note's discrimination framing; it quantifies the forecast's robustness and
proposes a cleaner statement. It adds no axiom and no derived fitted value; `m_H`, the SM `y_t`
extraction, and the literature stability boundary are explicit external comparators.
**Primary runner:** [`scripts/p3_vacuum_stability_pressure_test_2026_06_08.py`](../scripts/p3_vacuum_stability_pressure_test_2026_06_08.py) (PASS=4).

## The question

P3 forecasts the Higgs vacuum is **absolutely stable** (D1, a "binary YES" in the source note's table),
versus the SM's metastable. The whole forecast rests on one load-bearing number: the framework's
predicted top Yukawa **`y_t(v) = 0.918`**, which sits **below** the SM stability boundary
`y_t_crit ≈ 0.93` (at `m_H = 125.25`; Buttazzo 2013 / Bednyakov 2015, admitted comparator), so `λ`
stays positive to `M_Pl`. But the source note attaches a **±3 % systematic** to that `y_t`, and derives
it from an **open-gate** Ward-identity relation. A reviewer's first attack: *is "absolutely stable" a
robust prediction, or a knife-edge in `y_t`?*

## Findings

1. **RG grounding (1-loop, qualitative).** Integrating the 1-loop SM RGEs from the top scale to `M_Pl`:
   `λ(v) ≈ 0.129` (from `m_H = 125.25`), and the `−6 y_t⁴` term drives `λ` negative at a high scale for
   SM-like `y_t` (metastable), with the crossing **strongly** `y_t`-sensitive — a 1-loop stability
   boundary in the `~0.91–0.95` band (consistent with the literature 2-loop `y_t_crit ≈ 0.93`). This
   confirms the mechanism: stability is a steep function of `y_t`, decided right where the framework's
   value sits.

2. **The straddle (the core finding).** The framework's `y_t(v) = 0.918 ± 3 %` band is **`[0.890, 0.946]`**,
   which **straddles** the boundary `y_t_crit ≈ 0.93`. The boundary lies only **0.44 σ_sys above** the
   central value, so **≈ 33 % of the framework's own `y_t` band is on the metastable side** (`y_t > 0.93`).
   The stable/metastable verdict therefore **flips inside the framework's own systematic** — "absolutely
   stable" is the central call only, not a robust binary.

3. **Open-gate dependency.** `y_t(v) = 0.918` derives from the Ward-identity relation
   `y_t(M_Pl)/g_s(M_Pl) = 1/√6` — which the source note itself flags as an **open-gate / bounded** input
   (not retained) — plus standard SM running and the 3 % surrogate systematic. So the stability **sign**
   rides on an un-closed relation, not a retained theorem.

## Reframing (the recommendation)

State P3 as a **conditional beyond-SM signature**, not "absolutely stable." The genuine, defensible
content is: *the framework predicts `y_t` lower than the SM extraction (0.918 vs 0.94), which — if it
holds at a tightened precision — would put the vacuum on the stable side.* That is a real beyond-SM
forecast (a SM "written in lattice notation" would not predict a specific `y_t`). But the **binary
"absolutely stable"** overstates it: within the framework's own ±3 % `y_t` band, ~1/3 is metastable, and
the discrimination versus the SM is ~0.75 σ (as the source note already notes). The honest headline:
**"central-value stable; ≈ 2/3 of the `y_t` band stable; a ~0.75 σ beyond-SM `y_t` signature pending a
tighter, audited `y_t`."** The single highest-leverage step to make P3 robust is to **tighten/close the
`y_t` Ward-identity gate and shrink the 3 % systematic below the ~1.3 % margin to the boundary.**

## What is and is not claimed

- **Is:** "absolutely stable" is not robust — the framework's `y_t = 0.918 ± 3 %` band straddles the SM
  stability boundary `≈ 0.93` (boundary 0.44 σ_sys above center; ~33 % of the band metastable), and the
  `y_t` value rests on an open-gate Ward identity. P3 is best stated as a conditional beyond-SM `y_t`
  signature.
- **Is not:** does **not** derive `y_t`, the stability boundary, or `m_H`; does **not** claim the vacuum
  *is* metastable (the central value is stable); does **not** dispute the source note's discrimination
  framing or its honest ~0.75 σ caveat; the 1-loop RG is a qualitative grounding, not a precise boundary
  (that is the literature 2-loop comparator). Adds no axiom or fitted value.

## Boundaries (honest)

- **The precise boundary is a literature comparator.** `y_t_crit ≈ 0.93` / `m_t ≲ 171.5 GeV` at
  `m_H = 125.25` is the SM 2-loop+ result (Buttazzo/Bednyakov); the 1-loop RG here only grounds the
  mechanism and the steep `y_t`-sensitivity.
- **The ±3 % is the source note's own stated systematic**, treated as ~1 σ (consistent with its own
  "0.75 σ" usage). Read as a hard bound, the conclusion is the same: the boundary lies inside the band.

## Load-bearing inputs

- [`HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md`](HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md)
  — defines P3, the framework `y_t(v) = 0.918 ± 3 %`, the boundary `≈ 0.93`, and the open `y_t` gate.
- [`HIGGS_VACUUM_EXPLICIT_SYSTEMATIC_NOTE.md`](HIGGS_VACUUM_EXPLICIT_SYSTEMATIC_NOTE.md)
  — the Higgs/vacuum lane systematic surface (the inherited `y_t` residual budget).

## Forbidden-imports check

No PDG / literature value is consumed as a derived quantity. `m_H = 125.25`, the SM `y_t ≈ 0.94`
extraction, and the literature stability boundary `≈ 0.93` are named external comparators (exactly as
the P3 note uses them). The 1-loop SM RGEs are standard and reproduced in the runner; `λ(v) = m_H²/2v²`
is the tree relation.
