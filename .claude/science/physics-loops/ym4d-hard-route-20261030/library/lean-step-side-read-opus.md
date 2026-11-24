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

### Step 3. The coupling floor of a step: existential, with an explicit lower bound in L

Definitions (`ClusterExpansionOfAStep/EffectiveDensityOfAStep.lean:14`): `clusterRange x = ⌈x ^ (1/100)⌉₊`. (`ParametersOfARenormalizationStep.lean:33`): `boxRadius x = clusterRange x / 2 ^ 11` (natural division).

- `FloorConditions (C c x)` (`ParametersOfARenormalizationStep.lean:127-154`) is a list of 16 inequalities in the step coupling x. Among them `radius_ge : 16 ≤ boxRadius x ∧ C ≤ boxRadius x` (131) and `range_ge : C ≤ clusterRange x` (138).
- `EventuallyFloorConditions` (`ClusterExpansionOfAStep/FloorsOfTheParameters.lean:7-9`): for every admissible T and every C, c > 0 there is y with FloorConditions C c x for all x >= y. Proof `eventuallyFloorConditions_holds` (`FloorsOfTheParametersProof.lean:580-594`): `filter_upwards` of 16 `eventually_*` lemmas, then `eventually_atTop.1`. **The floor y is an existential witness of a filter statement. The release computes no number for it.**
- The C the cell of the flow uses: `CellOfTheFlow/TheDrawsStandOnGroundsProof.lean:119-121`: `hCpos : 0 < 2 ^ 40 * Tb.side + 4 * Tb.n₀ + 2 ^ 17`, `obtain ⟨yF, hyF⟩ := hFl Tb hAdm _ 1 hCpos one_pos`; the floor is `max (max yD yG) (max yF (max Tb.floorMin 1))` (121), with yD, yG further existential floors (from `stageStateDensityStatement`, `HullStateIsHotCase`). The same C at `TheStepGivenItsStateIsTheGasProof.lean:299, 327` and `ExpansionReturnsAtDrawnParametersProof.lean:30, 58-63`. The floor applies to every stage coupling: `hon.le_coupling` (`TheDrawsStandOnGroundsProof.lean:131`), i.e. y <= (T.stage j).coupling.
- `floorMin = max yC 2^1600` (`ParametersOfARenormalizationStep.lean:88`), yC = max y₀ 1 with y₀ existential from the eventual property P (`ParametersCanBeChosenProof.lean:357-363`).
- The well-posed step also asks `range_ge_side : 2 ^ 40 * R.params.side ≤ R.range` (`ClusterExpansionOfAStep/AdmissionAtAStepForm.lean:12`; also `FactorsOfAStep.lean:122`), with R.range = clusterRange of the stage coupling (`MarkedIntegralsAreTheGasAtAStepProof.lean:442`, `RegularityOfTheImageProof.lean:59`).

**Explicit lower bound on the floor (read off, arithmetic by hand, PROVED from the cited clauses).** Let x be any stage coupling at which the cell of the flow runs, L the side. Then FloorConditions (2^40 L + 4 n₀ + 2^17) 1 x holds, so by `radius_ge`, C <= ⌈x^(1/100)⌉ / 2^11 (natural division), hence ⌈x^(1/100)⌉ >= 2^11 C and x^(1/100) > 2^11 C - 1 >= 2^51 L + 2^13 n₀ + 2^28 - 1. So

  **H(L) := floor of the step coupling >= (2^51 L)^100 = 2^5100 L^100,** and also >= 2^1600 (floorMin).

At the smallest side the release admits through this clause, L = 2^40 (n₀ >= 4096): x > (2^91)^100 = **2^9100 ≈ 10^2739**. This is a lower bound on the floor, not the floor: the floor itself is max(yD, yG, yF, yC, 2^1600, 1) with yD, yG, yF, yC existential. The inequality is linear in L inside the 100th root, so the floor grows at least like L^100.

Caveat on units: x is the stage `coupling` of the flow (`(T.stage j).coupling`), the same quantity `TotalDensityFlow.coupling ℓ β K` that `IsFirstPassageDatum` compares with g^(-2) (`TopStatementDefs.lean:20-34`). So x is an inverse squared coupling on the β scale (to be confirmed in Step 4 against the flow's initial value).

