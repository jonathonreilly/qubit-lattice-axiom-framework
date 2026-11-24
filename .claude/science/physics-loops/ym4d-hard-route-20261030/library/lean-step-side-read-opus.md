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

### Step 2. Where the side is chosen (the order of choice)

The parameter structure the step reads is `RenormalizationStepParameters.ParameterAssignment` (`YangMills/Construction/ClusterExpansionOfAStep/ParametersOfARenormalizationStep.lean:34-61`), with `Admissible` at lines 90-126. Its side clauses: `L_odd` (99), `L_ge : 2 ^ 40 ≤ T.side` (100), `L_gt : 11 * 2 ^ 12 * T.baseDepth < T.side` (101), `J₀_ge : 625 ≤ T.baseDepth` (98), `σ_L : 2 ^ 10 * side * (N 0 + 1) * threshold ≤ 1` (112), and `fits : ∀ y ≥ floorMin, (stepParameters y).Admissible` (126) with `floorMin = max yC 2^1600` (88). Also `n₁ = side^(1/640)` (65).

The existence statement is `ParametersCanBeChosen` (`ClusterExpansionOfAStep/ParametersExist.lean:7-21`): for every a >= 1 (mesh coupling), there are cK, κ, δ₁, J₀; for every eventual property P there is **L₀** such that every odd L >= L₀ admits an assignment with side = L. Proof: `parametersCanBeChosen_holds` (`ParametersCanBeChosenProof.lean:184-...`), from five hypotheses `ChainCoercivity`, `holeSavingStatement`, `ColdChainAtSmallCoordinates`, `AdmissibleParametersExist`, `ExistsCutoff`. Proved in the release as `step_parameters_exist` (`TheStatementsProvedTogether/FromMeansAtABondProof.lean:75`).

Order of choice in that proof (lines 188-290):
1. a given; cK and LK from `ChainCoercivity` (189); κ from `holeSavingStatement a` (190); δ₁, LA from `ColdChainAtSmallCoordinates a` (191); J₀ = max 625 (Jf1, Jf2) from the hole saving at Θ = 1 and 9/8 (192-203); LB1, LB2 from the hole saving at J₀ (204-205).
2. LC from the eventual property P (207).
3. **L₀ = max (max (max LK LA) (max LB1 LB2)) (max LC (max (2 ^ 40) (11 * 2 ^ 12 * J₀ + 1)))** (208). So 2^40 is one floor among six; LK, LA, LB1, LB2, LC are existential witnesses (no number at this point of the release).
4. Then, at the chosen L: the cold-chain constants (lam, ρA, σA, cg, N) from `hA L` (224), the cut δ₂ (231-), Ct, κ₀, rt <= min(κ₀, δ₂/2^14, ceilRate) (256), η₃, the threshold σ <= min(..., 1/(2^10 L (N0+1)), ...) (284). The threshold shrinks like 1/L.
5. The standard lump grid `standardLumpGrid L` needs only `2 ^ 16 ≤ L` (lines 23-51: lumps are intervals of length 16384 = 2^14 around a central interval [-8192, 8192]).

So within this proof the side is chosen **before** the threshold, n₀, Cs and the floor of the step coupling; those depend on L. Step 3 reads where the coupling floor is fixed.

