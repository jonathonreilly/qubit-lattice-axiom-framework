# Flavor — CORRECTION: "Q=1 is the framework default" is NOT forced; it rests entirely on the unaudited PRR premise, and Q=2/3 is admissible under native C3

**Date:** 2026-05-30
**Claim type:** bounded correction of a prior campaign statement + sharpened localization of the single unaudited premise.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_Q1_default_rests_on_PRR_2026_05_30.py` (SCORECARD PASS=3).
**Source:** 6-agent build `wf_9977f75f` (reference-state cone; tracial-vs-Gibbs; observability; PRR steelman).

## The correction
Earlier in the campaign (and in my reporting) the conclusion hardened to "**Q=1 (democratic) is the
framework's honest default, and r=1/2 is a genuine import.**" This build shows the **default half is an
overstatement**: A1+A2 do **not** force the trace on the generation factor.

## Why
- **C₃-invariant reference states form a 2-parameter cone.** By Schur, any C₃-invariant state on
  `ℝ[Z₃]=ℝ⊕ℂ` is scalar on each isotypic block, fixed by two block masses `(w_s, w_d)`. The trace weights
  them by **dimension** `(1:2) → r=1 → Q=1`; a non-tracial state weights them `(1:1) → r=1/2 → Q=2/3`.
- **The `(1:1)` state is explicit and admissible.** `ρ_(1:1) = ½P_s + ¼P_d` (diagonal 1/3, off-diagonal
  1/12; eigenvalues {½,¼,¼}) is PSD, trace 1, and **commutes with the C₃ shift** — a perfectly valid
  C₃-invariant reference giving Q=2/3.
- **The trace is privileged ONLY by full U(3) invariance = PRR.** Verified: Haar `U(3)` leaves `ρ_τ`
  invariant (dev ~1e-15) but not `ρ_(1:1)` (dev ~0.35). Full inner-automorphism invariance is the **PRR**
  premise — `inner_automorphism_invariance_...` is **unaudited, user-approval-required, NOT derived from
  A1+A2**. The only symmetry A1+A2 genuinely supply on the generation factor is **C₃**, which leaves the
  entire `(w_s,w_d)` cone open. The "dynamics-independence ⇒ trace" steelman collapses into PRR
  (KMS-for-all-dynamics ⟺ tracial ⟺ U(3)-invariant; A1+A2 give no generation Hamiltonian).

## A second correction (to the build's own MAP, and my framing)
**`r=|b|²/a²` is a spectral invariant of the operator `H` alone — the reference state does NOT enter the
retained Koide functional** (`Q=(a²+2b²)/3a²`, no `ρ`). So the reference-state cone does **not** by itself
select `r=1/2`: the posited bridge `r* = w_d/(2w_s)` is an **inserted equation-of-state** (variance
minimization gives a different `b`), not derived. The measure framing correctly *localizes* the unaudited
premise (PRR), but it is **not** the mechanism that fixes the value.

## Honest status of the value question (superseding "Q=1 default")
- **Q=1 is NOT forced** — it is *default-pending-PRR*. Drop the unaudited full-U(3) premise and the trace
  loses its privilege.
- **Q=2/3 is REACHABLE, not derived** — an admissible C₃-invariant reference gives it, but no native
  principle (stronger than C₃, weaker than PRR) selects the `(1:1)` point, and the state→operator bridge
  does not load-bear.
- **NEITHER Q=1 nor Q=2/3 is forced by A1+A2 alone.** The block weighting is **physically observable**
  (any C₃-invariant observable touching the doublet distinguishes the states: `⟨R⟩_τ=0` vs
  `⟨R⟩_(1:1)=1/4`), not gauge — *provided* the doublet `(J−I)` direction is a retained observable and the
  a-vs-b orientation is not separately convention.

## The decisive, decidable, no-import next step
The value is fixed **at the readout structure, not the reference-state choice**: does the physical mass
readout factor through the **SO(2)/U(1)_b doublet-frame quotient** — counting the doublet **once**
(`1:1 → r=1/2`) — or use its full **2-real-dimensional** content (`1:2 → r=1`)? This is a structural
question about the **already-retained** Koide functional (`det_R(αP_s+βP_d)=αβ²` currently carries the
`(1,2)` weighting on the unreduced carrier), requiring **no PRR and no new axiom**. It supersedes both the
reference-cone framing and the inserted `r*` bridge, and pairs with the unaudited
`koide_real_rep_block_count_permitted_not_forced` (runner 15/15) whose stated surviving handle is this same quotient.

## Reframed campaign bottom line
The framework derives all charged-lepton flavor **except** whether the doublet is counted once (complex /
SO(2)-quotient → Q=2/3, observed) or twice (real dimension → Q=1). That single binary is **not** settled by
A1+A2; "Q=1 default" was an artifact of silently assuming PRR (full-unitary symmetry where only C₃ is
native). The genuinely open, import-free question is the doublet-frame quotient in the retained readout.

## Stale-citation flags (verified vs origin/main ledger)
- Retained: `koide_circulant_q_two_thirds` (operator functional); `pre_record_reference_state` (retained
  but identification-half **excluded** from scope); `prr_local_derivation_from_jaynes` (retained_bounded,
  **spatial-qubit only**, does not act on the generation factor).
- **Unaudited (the single load-bearing premise):** `inner_automorphism_invariance_tracial_identification`
  (full-U(3)/PRR); also `axiom_first_kms_condition`, `koide_real_rep_block_count_permitted_not_forced`.
