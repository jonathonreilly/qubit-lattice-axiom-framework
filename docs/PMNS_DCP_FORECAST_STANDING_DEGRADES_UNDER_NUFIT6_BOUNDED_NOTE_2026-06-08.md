# PMNS δ_CP Forecast Under NuFIT-6.1: the Standing Degrades From Favorable to Disfavored-but-Allowed; the Predicted Band Is Input-Stable but Not Re-Certified (Comparator Refresh of the Stale NuFIT-5.3 Framing)

**Date:** 2026-06-08
**Type:** bounded comparator-refresh note (updates the named external comparator from NuFIT-5.3 to the current NuFIT-6.1 table, with NuFIT-6.0 kept as a historical cross-check; NOT a new prediction, NOT a no_go, NOT a re-certification of the band)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_pmns_dcp_nufit6_comparator_refresh_exact.py`](../scripts/audit_companion_pmns_dcp_nufit6_comparator_refresh_exact.py) (18/18)

## Result

The landed PMNS forecast
([`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](./PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md))
certifies `δ_CP ∈ [251.86°, 270.00°]` (third quadrant) over the chamber-boundary preimage of the **NuFIT-5.3** NO
3σ rectangle on `(s₁₂², s₁₃²)` (its named external comparators `X3`/`X3*`), and predicts the `θ₂₃` **upper octant**.
This note refreshes the comparator to **NuFIT-6.1 (2025)**, the official current table based on data available in
November 2025 ([NuFIT results page](https://www.nu-fit.org/?q=node%2F12);
[v6.1 parameter table](https://www.nu-fit.org/sites/default/files/v61.tbl-parameters.pdf)), and keeps
**NuFIT-6.0 (2024)** ([arXiv:2410.05380](https://arxiv.org/abs/2410.05380), JHEP 12 (2024) 216) as a historical
cross-check. NuFIT values are used **only** as comparators; the framework's predicted band is unchanged landed theorem
content, taken **as stated**.

**(A) The forecast is input-stable but not re-certified here.** The forecast **consumes** `(s₁₂², s₁₃²)`
as inputs and produces `δ_CP` as the forced output — it does **not** consume the measured `δ_CP`. So whether the
predicted band moves is governed by whether the *input* rectangle moved. The NuFIT-6.0 NO rectangle barely moved
relative to NuFIT-5.3, and the current NuFIT-6.1 NO rectangle is still a small, nearby comparator: its `s₁₂²` 3σ range
is a stricter subset of the NuFIT-5.3 range, while its `s₁₃²` upper edge expands by only about eight percent of the
NuFIT-5.3 `s₁₃²` width. The current v6.1 rectangles
(`s₁₂² ∈ [0.2893, 0.3295]`, `s₁₃² ∈ [0.02070, 0.02420]` no-SK / `[0.02064, 0.02418]` with-SK) also lie inside the
region the chamber box `B` maps onto (`s₁₂² ∈ [0.008, 0.97]`, `s₁₃² ∈ [0.0005, 0.121]`, the landed runner's Part-4
coverage). **Honest caveat:** the landed box-Krawczyk certificate covers only the sub-boxes whose image overlaps the
*NuFIT-5.3*
rectangle (5404 of 6400; 996 skipped), **not all of box `B`**, and this note does **not** re-run the certificate over
the NuFIT-6 rectangle. So the band is taken **as** the landed `[251.86°, 270.00°]` for the standing assessment below;
the nearby-input comparison makes a large band shift unlikely, but that is an **expectation, not a re-certified
result**.

**(B) The standing degrades from favorable to disfavored-but-allowed.** NuFIT-6.1 gives NO best-fit `δ_CP` values of
**207° (+23/−20, no-SK)** / **212° (+26/−36, with-SK)**. The framework band `[251.86°, 270.00°]` is **within** the
NuFIT-6.1 3σ range for both columns (`[114°, 405°]` no-SK, `[125°, 365°]` with-SK) — so it is **not excluded** — but
the best fit lies **outside** the band. The same disposition already appears in NuFIT-6.0 (`177°` no-SK / `212°`
with-SK; 3σ `[96°, 422°]` / `[124°, 364°]`). Under NuFIT-5.3 the band sat near the T2K-driven `~230–270°` region and
read as a tight 7.3% sub-region match; under current NuFIT it is a **forward bet that current data lean against**.
*(Any band-edge-to-best-fit sigma count would be only a crude asymmetric-error yardstick, **not** a likelihood
significance; the NO `δ_CP` likelihood is non-Gaussian/wrapped and the 3σ interval remains broad.)*

**(C) The θ₂₃ upper-octant prediction is now current-data disfavored for NO.** The framework predicts `s₂₃² > 0.5`.
NuFIT-6.0 was SK-dependent for NO: **0.561 (no-SK → upper, agrees)** but **0.470 (with-SK → lower, disagrees)**.
Current NuFIT-6.1 gives **0.470** for the NO best fit in both the no-SK and with-SK columns, so the upper-octant
prediction is now disfavored in both current best fits, while the v6.1 3σ ranges still include upper-octant values
(`[0.432, 0.587]` no-SK, `[0.435, 0.584]` with-SK).

**(D) Decisively testable, currently unfavorable.** The band's upper edge is `270° = −90°` (maximal CP), exactly where
the DUNE / Hyper-K era is designed to have strong sensitivity — no insensitive-region escape hatch. The honest framing
is **"a sharp forward bet current data lean against, decisively testable by next-generation long-baseline data,"** not
the stale NuFIT-5.3 "tight match."

## Why this matters (falsifiability honesty)

The standing notes were frozen at NuFIT-5.3, when T2K drove `δ_CP` toward `~270°` and the band looked confirmed.
NOvA plus the NuFIT-6.0/6.1 global fits have since pulled the NO best fit away from the third-quadrant band. So the
framework's band is now genuinely **out on a limb** — which *improves* its discriminating power
(a future near-maximal third-quadrant result would distinguish it from the drifting global fit) while making its
current standing **unfavorable**. Any falsifiability claim that reaches a manuscript surface should quote the
NuFIT-6.1 standing, not the NuFIT-5.3 one.

## Scope — what this is and is not

- **Is:** a comparator refresh (NuFIT-5.3 → current NuFIT-6.1, with a NuFIT-6.0 historical cross-check) plus the
  verifiable observations that the consumed `(s₁₂², s₁₃²)` inputs stayed nearby (so the band is **expected** stable),
  the band — taken as the landed `[251.86°, 270.00°]` — is within current NuFIT-6.1 3σ but the best fit is outside it
  (disfavored-but-allowed), and the `θ₂₃` upper-octant prediction is now disfavored in current NO best fits.
- **Is not:** a change to the framework's predicted band; a re-certification of the bracket over the NuFIT-6.1
  rectangle (explicitly not re-run); a new prediction; a no_go or a claim the forecast is excluded (it is **within**
  NuFIT-6.1 3σ); a claim of a likelihood significance for the "disfavored" reading. The underlying forecast's
  `unaudited` / conditional (`X6` preimage-localization) status is unchanged.
- **Residual:** a fully rigorous re-run would recompute the chamber preimage of the NuFIT-6.1 rectangle and re-run the
  box-Krawczyk bracket over its image-overlap sub-boxes (the landed certificate covers only the NuFIT-5.3-overlap
  sub-boxes). The band-stability here rides the same `X6` admission plus the nearby-input comparison, as an expectation
  only.

## Forbidden-import / reprove-and-cite discipline

- The standing arithmetic (input shift vs 3σ width; NuFIT-6.0/6.1 rectangles inside the box-`B` image region;
  band-within-3σ; best-fit-outside-band; octant test) is **reproven** in the runner from the numbers.
- NuFIT-5.3, **NuFIT-6.0** ([arXiv:2410.05380](https://arxiv.org/abs/2410.05380)), and
  **NuFIT-6.1** ([official table](https://www.nu-fit.org/sites/default/files/v61.tbl-parameters.pdf)) values are
  **comparators** / named external admissions for the labeling step — never derivation inputs. The predicted band
  `[251.86°, 270.00°]` is the landed theorem content, inherited (not re-derived, not re-certified) here. No value is
  fit; no PDG/NuFIT value is a derivation input.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](./PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)

**Independent audit required.** This note asserts no effective-status change.
