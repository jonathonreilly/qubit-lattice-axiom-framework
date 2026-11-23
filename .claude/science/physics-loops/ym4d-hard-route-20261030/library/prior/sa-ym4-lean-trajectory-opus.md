lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-24T10:06Z

# Port reading: the Lean coupling trajectory (row 1451)

Started 2026-11-23T22:06Z (date -u), Mac mini worker 2, at commit 92079d88b.
Source: Ethan Sussman and Levent Alpoge, public `YM4 Lean` release (with OpenAI
Codex assistance), commit 3932084a9b82, read-only checkout at
`~/ym4d-papers/sa-ym4-lean-full`. Read only; nothing built or run. All quotes are
short and attributed to that release.

## Plan

1. Read rows 1449-1450 and the earlier Lean-input reading
   (`library/prior/sa-ym4-lean-inputs-opus.md`) for what is already on file.
2. Locate and read `bare_root_with_window_data`, `runDomain`, `IsTunedAt`,
   `NoEscapingLevel`, `IsFirstPassagePair`, `Formulation.stopped_covariance_vanishes`
   and their files.
3. Decide (a) beta_K at every late K; (b) first-passage pairs vs. rows 1332/1353;
   (c) ComponentProperties exportability; (d) what is fixed at the physical scale.
4. Next two rows.

## Steps

## Repo search

`grep` of this folder for `bare_root_with_window_data`, `runDomain`, `IsTunedAt`, `NoEscapingLevel`, `IsFirstPassagePair`, `stopped_covariance_vanishes`: hits only in FINISH rows 1449-1451 and `library/prior/sa-ym4-lean-inputs-opus.md` (row 1449, Step 1b and Step 3, which names these declarations as unread). Row 1449 is the base of this note; its Step 3 defines (M-neutral-Lean) and (M-neutral-all).

Source opened at `~/ym4d-papers/sa-ym4-lean-full` (resolves to the external-volume checkout named in the row), git HEAD 3932084a9b82fc79466b4a2faad9ec032b637445, 2026-11-20. Read only. Paths below are relative to `YM4 Lean/`.

## Step 1. The six declarations (read 22:10-22:20Z)

Notation: b = their odd blocking factor (their `L`); K = cutoff level, mesh b^-K; β = bare Wilson β = g^-2 (standard normalisation, row 1449 Step 1a); `flowCouplings p β j` = their effective inverse coupling after j block steps from bare β (`TotalDensityFlow.coupling` agrees with it while the run stays above the floor, `total_flow_of_above_total`).

**1.1 `runDomain`** (YangMills/ContinuumLimit/RunAboveTheFloor.lean L43-44):
`{β | y + 2 * T.B < β ∧ ∀ j < k, y + 2 * T.B < flowCouplings (T.stepParameters y) β j}`.
A floor condition only: the bare β and every effective coupling before level k lie above y + 2B. **No upper bound on β.**
The same file's `RunTable` (L23-37) carries `descent : HasLinearDescent ... lam c₅` and `abs_flow_step_le` (L105-110): |x_{t+1} - x_t| ≤ 2B while the run is above the floor. As used in `bare_root_with_window_data` and `tuned_first_passage_index`, descent reads lam (K - i) - c₅ ≤ x_i - x_K for i ≤ K. So on a run, lam (K-i) - c₅ ≤ x_i - x_K ≤ 2B (K-i): the effective coupling falls at a rate between lam and 2B per step.

**1.2 `IsTunedAt T y P K β`** (YangMills/ContinuumLimit/FirstPassageOfATunedPair.lean L13-15): the flow from β stays ≥ y at every level j < K and its level-K value is exactly P. `tuned_first_passage_index` (same file L57-113): if tuned at K with P = `passageThreshold Bs g` and K ≥ `runDepth lam c₅`, there is a first-passage index K' ≤ K with K - K' < runDepth, i.e. the flow first drops to the threshold within a bounded number of steps of K.

**1.3 `bare_root_with_window_data`** (YangMills/ContinuumLimit/ReferenceRoots.lean L9-23, statement). For every Q holding at admissible parameters: ∃ b_0, ∀ odd b ≥ b_0, ∃ parameter table T, floor y, constants (lam, cr, Bs ≥ 2, γ > 0, ...), with a one-loop average slope and `RunTable`, and

> `∀ H : ℝ, ∃ (M : ℕ+) (δ : ℝ), 8 ≤ torusSide L M ∧ 0 < δ ∧ ∀ᶠ K : ℕ in atTop, ∀ g₀ ∈ Ioo (0:ℝ) δ, ... IsLeast {t | 0 < t ∧ referenceResponse L M K (t ^ 2)⁻¹ = fixedPhysicalLevel g₀} g ∧ b ∈ runDomain T y K ∧ IsTunedAt T y P K b ∧ H ≤ P`

with g = `renormalizedBareCoupling L M K g₀`, b = g^-2, P = flow coupling at level K. **This holds at every late K (`∀ᶠ K in atTop`), uniformly in g₀ ∈ (0, δ).** It controls the least root from one side only: the bare β_K is in the run domain, and the effective coupling at level K (unit physical scale) is at least H. The reference level M (torus side 2b^M) and δ depend on H. The proof (L24-95) builds a tuned trial bk at each level with flow value at least H (`all_cutoff_trial`), shows the least root lies at or above bk (`leastBareAt_of_trial`: the response is continuous, tends to 0 cold, and the trial is on the high side of the level), and then monotonicity of the tuned branch (`tuned_branch_of_le`) gives P ≥ flow value of bk ≥ H.

**1.4 `NoEscapingLevel T y L M`** (YangMills/ContinuumLimit/FixedReferenceLevelBound.lean L13-18): for every level r > 0, every strictly increasing k_j and bare b_j in the run domain, tuned, with `referenceResponse L M (k j) (b j) = r` for all j, the level-k_j flow value cannot tend to +∞. That is: **at a fixed positive reference response, the effective coupling at unit physical scale stays bounded along every sequence of cutoffs** (no escape to the cold end). It is proved from stage decay (`noEscapingLevel_of_stageDecay`, L22-79): if the level-K flow tends to ∞, the reference covariance at a stopped level is at most r/2, contradicting the level r.

**1.5 `Formulation.stopped_covariance_vanishes`** (YangMills/ContinuumLimit/CovarianceAtTheStoppingLevel.lean L44): `AtResponseParameters BranchHot.StageDecayAt` (contents read in Step 2 below). It feeds `noEscapingTables_of_stageDecay` (FixedReferenceLevelBound.lean L87-91), which is the only use of NoEscapingLevel in `fixed_observable_continuum_of_components` (Formulation/FixedObservableContinuum.lean L156-166).

**1.6 Where the subsequence is chosen** (Formulation/FixedObservableContinuum.lean L84-152, proof of `BranchHot.fixed_observable_continuum_of_no_escape`). Two "frequently" filters, then a compactness subsequence:
1. `uniform_record_gap` (YangMills/ContinuumLimit/RecordCutoffs.lean L53-58): ∃ X, **∃ᶠ k** (frequently, not eventually), for every tuned (b, P) with P ≥ X, every earlier level i < k has flow value ≥ P + s/4, s = `slopeConst` of the blocking factor. These are record cutoffs of the one-loop table `oneLoop T` (`slope_record_cutoffs`). The cutoffs w_j are extracted from (record cutoffs) ∧ (eventual root data with H = max X (Bs + γ^-2 + 1)) by `extraction_of_frequently_atTop`.
2. `ReferenceCalibration.fixed_window_of_positive_reference` with NoEscapingLevel: some W ≥ H such that, frequently in j, P_j ≤ W (`hwin`).
3. At those j, with G = (W - Bs)^{-1/2} so that `passageThreshold Bs G = W`, the pair (K_j, b_j) is an `IsFirstPassagePair p Bs G` (b_j ≥ W, P_j ≤ W, every earlier level > W).
4. `su2_continuum_limit_of_frequent_passage` takes a further subsequence φ along which the lattice data converge; the β-slope clause is proved there.

