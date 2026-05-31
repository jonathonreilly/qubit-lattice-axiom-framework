# Flavor value campaign — CAPSTONE: the four-channel reframe dissolves the "selection" problem (validated)

**Date:** 2026-05-31
**Claim type:** campaign capstone / validated reframe (with two honest caveats). Recontextualizes the entire charged-lepton value campaign.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_four_channel_reframe_validated_2026_05_31.py` (SCORECARD PASS=4).
**Source:** validation build `wf_1c38487f`; resolves the campaign by correcting its framing (user + parallel-worker reframe).

## The category error the campaign was making
The campaign spent ~30+ probes trying to **force/select** one Koide value (Q=2/3 over Q=1) via a native
principle — symmetry, measure/positivity, locality, chirality, records — and kept landing on bounded
obstructions and "no-selection" negatives. **That was the wrong question.** The generation operator
`H = aI + bC + b̄C²` splits by C₃-Fourier into a **singlet** `a` and a **doublet** `b`, and the special
Koide values are **readouts of different channels, not competing answers to one question.**

## The validated structure — one operator, independent channels
`H` has exactly **3 real degrees of freedom** `(a, |b|, δ=arg b)`, carried on orthogonal C₃ channels:

| channel | datum | reads | physical sector |
|---|---|---|---|
| **SCALE** = singlet `a` | the flavor-**universal** mass scale (degenerate base) | gauge / Higgs-universal couplings | `Q=1/3` floor* |
| **RATIO** = doublet `\|b\|` (`r=\|b\|²/a²`) | the mass-ratio **spread** | Yukawa-texture couplings | `Q=2/3` at `r=1/2`* |
| **CP** = doublet phase `δ` | the **orientation** (Q-orthogonal) | CP-violation | Brannen `δ` |
| *(topological)* **ASYMMETRY** = signed flow / `η` | the index/anomaly datum at `d=3` | anomaly / index | `L₃ = 2/9` |

**Independence is genuine, not a relabeling** (verified): the Jacobian of `(mean-eigenvalue, Q, δ)` w.r.t.
`(a,|b|,δ)` has nonzero determinant — three independently recoverable orthogonal channels. The scale `a` is
a separate axis from the ratio `r`; `δ` is Q-orthogonal (`dQ/dδ=0`) yet physical (sets which generation is
heaviest). This is **more than three points on one `Q(r)` curve plus a phase.**

**SCALE = singlet = what gauge sees** (verified): a generation-universal coupling `G=gI` is *purely* singlet
(doublet coefficient `=0`); `U(1)_em`/`U(1)_Y` commute with circulants (Probe 14) and act only on the singlet.
So generation-blind couplings read the **universal mass scale**; the doublet carries the generation-*differences*.

## What this dissolves — the campaign negatives are correct-and-expected
- "No symmetry selects Q=2/3 over Q=1" → **right** — the ratio and asymmetry are *different channels*, nothing
  to select between.
- "Onsite-locality collapses the operator to Q=1/3" → **not a failure** — locality projects onto the singlet,
  i.e. it reads the **scale channel** (the universal mass); it was never destroying the masses.
- "Q is δ-blind" / "ratio doesn't label the scale" (the retained **source-selector firewall** Results 1 & 4) →
  these *are* the channel-orthogonality statements (Q⊥CP, ratio⊥scale).
- "Unforced r=1/2" → `r=1/2` is the empirical charged-lepton **mass-ratio input** read by the ratio channel —
  a Yukawa-like datum, **not** something a scale/gauge/symmetry principle could ever fix (wrong channel). The
  campaign was asking the scale/gauge sector to deliver a ratio-sector datum: the category error.

## What is derived vs input (honest accounting)
- **Derived (framework structure):** the C₃-channel decomposition itself (3 generations, singlet⊕doublet,
  the circulant form, the channel orthogonality), `J_cs` forced by Schur, the signed/Hermitian readout from
  reflection positivity, the exact identity `Q=1/3+(2/3)r`, and the **topological** `η = 2/9` at `d=3` and the
  CP order-parameter δ (both retained_bounded).
- **Empirical input (read, not forced):** the **ratio** `r=1/2` (= the measured lepton mass spread) and the
  **scale** `a` (the overall mass unit). These are the Yukawa-like data the framework *carries in their channels*,
  not predicts — and that is the correct, honest status, not a failure.

## Two honest caveats (do not overstate)
1. **The asymmetry is topological, not a 4th continuous channel.** `η=(d²−1)/(12d)=2/9` at `d=3` lives in
   index space and is fixed once `d=3`. Honest count: **3 continuous channels of `H` + 1 topological datum.**
2. **The specific Q-numbers are readout-convention-locked.** `b=0 → Q=1/3` and `Q=2/3 ↔ r=1/2` hold in the
   **dispersion readout** `D=(Σλ²)/(Σλ)²`; the **Brannen signed-√** readout gives `Q=1/(2r+1)` (floor `Q=1`,
   `Q=2/3` at `r=1/4`). The channel **structure** is convention-independent; the specific values marked `*`
   above are not (the repo's signed-vs-singular-value ambiguity — a separately-flagged live dimension).

## Capstone bottom line
The charged-lepton "value problem" was a **framing error**. The framework's job was never to output one
number; it is to provide the **channel structure**, and it does — correctly assigning each charged-lepton
datum (scale, ratio, asymmetry, CP) to its own C₃-channel and its own physical sector. The dozen+ "selection"
no-gos were all *confirming* channel-independence while being misread as failures to close. **The framework
derives the channel architecture and the topological data; the scale and ratio are empirical inputs read in
their channels — which is the honest, correct, and complete account of charged-lepton flavor on A1+A2.**

## Next genuinely-derivable target (not a selection)
The derivable content lives in the **topological channels**: the asymmetry `η=2/9` (= APS `(d²−1)/12d` at the
forced `d=3`) and the CP order-parameter — and whether `d=3` itself + these fix the `2/9` family
`(N−1)/N²` structurally. That is a topological/index question, not a value-selection one, and it does not
require forcing the ratio. The readout-convention (signed-vs-dispersion) dimension is the remaining label to pin.

## Stale-citation flags
- Anchors: `koide_circulant_q_two_thirds` (retained), `koide_circulant_character_bridge` (retained),
  `charged_lepton_koide_ratio_source_selector_firewall` (retained — Results 1/4 = channel-orthogonality),
  `new_parity_is_circulant_phase` (retained_bounded — δ as parity order parameter),
  `axiom_first_z_n_equivariant_spectral_asymmetry` (retained_bounded — η/2-9). Probe 14 = unaudited (gauge-singlet).
