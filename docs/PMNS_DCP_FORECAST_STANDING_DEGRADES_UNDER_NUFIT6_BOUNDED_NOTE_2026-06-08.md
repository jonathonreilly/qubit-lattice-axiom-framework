# PMNS δ_CP Forecast Under NuFit-6: the Standing Degrades From Favorable to Disfavored-but-Allowed; the Predicted Band Is Input-Stable but Not Re-Certified (Comparator Refresh of the Stale NuFit-5.3 Framing)

**Date:** 2026-06-08
**Type:** bounded comparator-refresh note (updates the named external comparator from NuFit-5.3 to NuFit-6.0 and re-reports the experimental standing; NOT a new prediction, NOT a no_go, NOT a re-certification of the band)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_pmns_dcp_nufit6_comparator_refresh_exact.py`](../scripts/audit_companion_pmns_dcp_nufit6_comparator_refresh_exact.py) (11/11)

## Result

The landed PMNS forecast
([`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](./PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md))
certifies `δ_CP ∈ [251.86°, 270.00°]` (third quadrant) over the chamber-boundary preimage of the **NuFit-5.3** NO
3σ rectangle on `(s₁₂², s₁₃²)` (its named external comparators `X3`/`X3*`), and predicts the `θ₂₃` **upper octant**.
This note refreshes the comparator to **NuFit-6.0 (2024)** ([arXiv:2410.05380](https://arxiv.org/abs/2410.05380),
JHEP 12 (2024) 216) and re-reports the standing. (NuFit-6.1, Nov 2025, [nu-fit.org node/309](http://www.nu-fit.org/?q=node%2F309),
is the latest version; it is qualitatively the same for this purpose — NO consistent with CP conservation within 1σ,
`θ₂₃` octant still ambiguous — so v6.0 is used here as the precise comparator.) NuFit-6.0 is used **only** as the
comparator; the framework's predicted band is unchanged landed theorem content, taken **as stated**.

**(A) The forecast is input-stable but not re-certified here (runner A1–A3).** The forecast **consumes** `(s₁₂², s₁₃²)`
as inputs and produces `δ_CP` as the forced output — it does **not** consume the measured `δ_CP`. So whether the
predicted band moves is governed by whether the *input* rectangle moved. It barely did: the NuFit-6.0 NO rectangle
(`s₁₂² ∈ [0.275, 0.345]`, `s₁₃² ∈ [0.02023, 0.02376]` no-SK / `[0.02030, 0.02388]` with-SK) shifts from the
NuFit-5.3 rectangle by **about 7%** (`s₁₂²` shift `0.005/0.071 = 7.0%`) of its 3σ width, and lies inside the region
the chamber box `B` maps onto (`s₁₂² ∈ [0.008, 0.97]`, `s₁₃² ∈ [0.0005, 0.121]`, the landed runner's Part-4 coverage).
**Honest caveat:** the landed box-Krawczyk certificate covers only the sub-boxes whose image overlaps the *NuFit-5.3*
rectangle (5404 of 6400; 996 skipped), **not all of box `B`**, and this note does **not** re-run the certificate over
the 6.0 rectangle. So the band is taken **as** the landed `[251.86°, 270.00°]` for the standing assessment below; the
~7% input shift makes a large band shift unlikely, but that is an **expectation, not a re-certified result**.

**(B) The standing degrades from favorable to disfavored-but-allowed (runner B).** NuFit-6.0 moved the NO best-fit
`δ_CP` to **177° (+19/−20, no-SK)** / **212° (+26/−41, with-SK)** — CP-conserving within ~1σ. The framework band
`[251.86°, 270.00°]` is **within** the NuFit-6.0 3σ range for both columns (`[96°, 422°]` no-SK, `[124°, 364°]`
with-SK) — so it is **not excluded** — but the best fit now lies **outside** the band. Under NuFit-5.3 the band sat
near the T2K-driven `~230–270°` region and read as a tight 7.3% sub-region match; under NuFit-6.0 it is a **forward
bet that current data lean against**. *(A rough "~1.5σ with-SK to ~2σ no-SK" band-edge-to-best-fit figure is only a
crude asymmetric-error yardstick, **not** a likelihood significance — the NO `δ_CP` likelihood is strongly
non-Gaussian/wrapped, its 3σ reaching 422°, and NO is consistent with CP conservation within 1σ.)*

**(C) The θ₂₃ upper-octant prediction is now SK-dependent (runner C).** The framework predicts `s₂₃² > 0.5`.
NuFit-6.0 NO gives **0.561 (no-SK → upper, agrees)** but **0.470 (with-SK → lower, disagrees)**. The octant
confirmation is no longer clean — it flips with the SK-atmospheric choice.

**(D) Decisively testable, currently unfavorable (runner D).** The band's upper edge is `270° = −90°` (maximal CP),
exactly where DUNE / Hyper-K (~2031–32) have peak sensitivity — no insensitive-region escape hatch. The honest
framing is **"a sharp forward bet current data lean against, decisively testable by ~2031,"** not the stale
NuFit-5.3 "tight match."

## Why this matters (falsifiability honesty)

The standing notes were frozen at NuFit-5.3, when T2K drove `δ_CP` toward `~270°` and the band looked confirmed.
NOvA plus the NuFit-6.0/6.1 global fits have since pulled the NO best fit back toward CP conservation (consistent
within 1σ). So the framework's band is now genuinely **out on a limb** — which *improves* its discriminating power
(a future near-maximal third-quadrant result would distinguish it from the drifting global fit) while making its
current standing **unfavorable**. Any falsifiability claim that reaches a manuscript surface should quote the
NuFit-6.0/6.1 standing, not the NuFit-5.3 one.

## Scope — what this is and is not

- **Is:** a comparator refresh (NuFit-5.3 → NuFit-6.0) plus the verifiable observations that (A) the consumed
  `(s₁₂², s₁₃²)` inputs barely moved (so the band is **expected** stable), (B) the band — taken as the landed
  `[251.86°, 270.00°]` — is within NuFit-6.0 3σ but the best fit is outside it (disfavored-but-allowed), and (C) the
  `θ₂₃` octant is now SK-dependent.
- **Is not:** a change to the framework's predicted band; a re-certification of the bracket over the NuFit-6.0
  rectangle (explicitly not re-run); a new prediction; a no_go or a claim the forecast is excluded (it is **within**
  NuFit-6.0 3σ); a claim of a likelihood significance for the "disfavored" reading. The underlying forecast's
  `unaudited` / conditional (`X6` preimage-localization) status is unchanged.
- **Residual:** a fully rigorous re-run would recompute the chamber preimage of the NuFit-6.0 rectangle and re-run the
  box-Krawczyk bracket over its image-overlap sub-boxes (the landed certificate covers only the NuFit-5.3-overlap
  sub-boxes). The band-stability here rides the same `X6` admission plus the small (~7%) input shift, as an
  expectation only.

## Forbidden-import / reprove-and-cite discipline

- The standing arithmetic (input shift vs 3σ width; NuFit-6.0 rectangle inside the box-`B` image region;
  band-within-3σ; best-fit-outside-band; octant test) is **reproven** in the runner from the numbers.
- NuFit-5.3, **NuFit-6.0** ([arXiv:2410.05380](https://arxiv.org/abs/2410.05380)), and NuFit-6.1 values are
  **comparators** / named external admissions for the labeling step — never derivation inputs. The predicted band
  `[251.86°, 270.00°]` is the landed theorem content, inherited (not re-derived, not re-certified) here. No value is
  fit; no PDG/NuFit value is a derivation input.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md`](./PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)

**Independent audit required.** This note asserts no effective-status change.
