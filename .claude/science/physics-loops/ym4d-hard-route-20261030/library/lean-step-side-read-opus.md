lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T01:31Z

# lean-step-side-read-opus: what in the SA YM4 Lean release needs block side 2^40, and where the floor H is chosen

Queue row 1464 (next row 2 of row 1460). Started 2026-11-24T13:31Z on Mac mini worker 3. Read only, no proof, no build.
Source: Sussman-Alpoge YM4 Lean release at `~/ym4d-papers/sa-ym4-lean-full`, commit 3932084a9b82 (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text).

## Plan

1. Confirm the release commit; find `IsUnitMeshStepParameters` and its side hypothesis (side_ge / side_gt / 2^40).
2. List every lemma in `YangMills/Construction/ClusterExpansionOfAStep` and `YangMills/Construction/TotalDensitiesGiveASystem` that reads the side hypothesis, with the inequality each needs; then their direct consumers.
3. Find where the coupling ceiling/floor H of the calibration is chosen, and how it relates to the side.
4. Decide (a) explicit floor H(L) and smallest admissible side, with numbers, or (b) side bound structural, no small-block step.

## Results (written step by step)

### Step 1. The hypotheses (release 3932084a9b82fc79466b4a2faad9ec032b637445, confirmed by `git rev-parse HEAD` in the read-only copy)

All paths below are relative to the release root.

- `YangMills/Construction/TotalDensitiesGiveASystem/TopStatementDefs.lean:12-18`, `structure IsUnitMeshStepParameters (ℓ : TorusLumps.StepParameters)`:
  `coupling_eq_one : ℓ.coupling = 1`; `side_odd : Odd ℓ.side`; `side_ge : 2 ^ 40 ≤ ℓ.side`; `one_le_baseDepth : 1 ≤ ℓ.baseDepth`; `side_gt : 11 * 2 ^ 12 * ℓ.baseDepth < ℓ.side`; `threshold_mem : ℓ.threshold ∈ Ioo 0 1`.
- `YangMills/Construction/ClusterExpansionOfAStep/LumpsOnATorus.lean:11-27`, `structure StepParameters`: fields `coupling, side, grid, baseDepth, threshold, κ, κ₁, rt, n₁, E, E₃, derivBound, n₀, y₁, B`. Note: `coupling` here is a lattice-unit (mesh) parameter, set to 1 by `coupling_eq_one`; it is not beta.
- `YangMills/Construction/ClusterExpansionOfAStep/EffectiveDensityOfAStep.lean:211-230`, `structure StepParameters.Admissible`: `a_ge : 1 ≤ coupling`, `L_odd`, `L_ge : 2 ^ 16 ≤ side`, `κ ≤ 1/8`, `depth_lt : 11 * 2 ^ 12 * baseDepth < side`, `n₀_ge : 4096 ≤ n₀`, `y₁_ge : 1 ≤ y₁`, `range_ge : 2 ^ 16 ≤ clusterRange y₁`, positivity of the rest.
- So the step-level cluster expansion asks only side >= 2^16 (plus side > 11*2^12*baseDepth = 45056*baseDepth). The 2^40 appears in the top-level structure. Step 2 finds who reads 2^40.

