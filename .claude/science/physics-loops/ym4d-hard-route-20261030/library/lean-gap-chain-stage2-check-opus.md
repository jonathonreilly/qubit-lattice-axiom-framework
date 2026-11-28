lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-28T18:35:07Z

# Faithfulness check of Lean Stage 2 of the gap chain (queue row 1665)

Started 2026-11-28T06:35:07Z (date -u). Pinned commit b31d9c96b, branch
claude/ym4d-hard-route. Reader: Claude Opus 5.5, high reasoning, Mac mini
worker. Lean was not run. Object of check: lean/gapchain/GapChain/Stage2.lean
and lean/gapchain/RECEIPT-2.md (FINISH row 1654, by gpt-6.2-astra max).
Baseline: library/lean-gap-chain-stage0-check-opus.md (row 1653).

Status: done 2026-11-28T06:39:27Z (date -u). Sections are in step order 0, 1, 4, 2, 3.

## 0. Sources read

- `lean/gapchain/GapChain/Stage2.lean`, all 657 lines. SHA-256 `989e4972…db87`, equal to the hash in RECEIPT-2.
- `lean/gapchain/RECEIPT-2.md`, all. FINISH rows 1654 and 1665.
- `library/lean-gap-chain-stage0-check-opus.md` (row 1653), all.
- `lean/gapchain/GapChain/Stage0.lean` L1-30 and L170-292 (HasMassGap, HasUniqueVacuum, listMoment, latticeU, CutoffStates, ExpClusters, Inputs, the Chain section).
- Release declarations: see Section 3 for the files I read and the ones I could not read.

Method: I compare each statement and definition with Stage 0 and with the hand construction (check 1458, cited by the receipt). Lean was not run. Where the kernel's acceptance settles a point, I say so and rely on the receipt's build log.

## 1. Item 1: the declaration that discharges massGap_of_expClusters

Quote, Stage2.lean L588-590 (inside `namespace GapChain.Stage2`, file variables L23):

```lean
variable {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K} {S : CumulantFamily}
theorem massGap_of_expClusters (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hm : 0 < m) (hc : ExpClusters L K ν m) :
    HasMassGap (centredOf S) m
```

Stage0.lean L250-254 has the same section variables, in the same order, and the same binders and conclusion, character for character.

The agreement check is L613:
`example : type_of% @GapChain.massGap_of_expClusters := @massGap_of_expClusters`.

Which constant does the bare name on the right resolve to? Inside `namespace GapChain.Stage2`, both `GapChain.Stage2.massGap_of_expClusters` and `GapChain.massGap_of_expClusters` are visible. If the right side named the Stage 0 constant, the example would be `X : type X`, which proves nothing. I settle this from the receipt's axiom report, not from the Lean name-resolution rule:
- L618, in the same namespace, uses the same bare name in `uniqueVacuum_of_expClusters`.
- The receipt reports `uniqueVacuum_of_expClusters` depends on `[propext, Classical.choice, Quot.sound]` only. The Stage 0 constant depends on `sorryAx` (RECEIPT-0, check 1653 Section 6).
- So at L618 the bare name resolved to the Stage 2 constant. (If both had been candidates and both elaborated, Lean would have reported an ambiguity error and the build would have failed.)
- L613 has the same name in the same scope, so it also names the Stage 2 constant.

So the kernel checked that `@GapChain.Stage2.massGap_of_expClusters` has the type of `@GapChain.massGap_of_expClusters`, with every implicit binder (the `@` forms). The check is up to definitional equality. That is enough: Stage 0's type was found faithful (check 1653, Sections 3-4).

Extra hypotheses: none. The `Completion` section adds `variable {σ} {hσ}` (L520). The statement does not mention σ or hσ, so Lean does not add them; an extra binder would also make the L613 example fail. `hm : 0 < m` is in the signature and not used in the proof (the linter is switched off, L586). That is harmless: the proof shows the bound for every m, and the signature only matches Stage 0.

Note: Stage 2 does not change Stage 0. `GapChain.massGap_of_expClusters` keeps its `sorry`. The Stage 0 compositions `massGap_of_mNeutral` and `su2_fixed_observable_gap_of_mNeutral` still call the Stage 0 constant, so their axiom lists keep `sorryAx` until a later stage rewires them to `Stage2.massGap_of_expClusters`. Stage 2 discharges the placeholder in the sense "a sorry-free term of the same type exists", which is what the brief asked.

Verdict item 1: **HOLDS.**

## 4. Item 4: forbidden tokens in Stage2.lean

Counts by `grep -c` (lines) and `grep -ow` (whole words), run on the pinned file:

| token | lines | whole words |
|---|---:|---:|
| sorry | 0 | 0 |
| admit | 0 | 0 |
| axiom | 33 | 0 |
| native_decide | 0 | 0 |
| opaque | 0 | 0 |
| implemented_by | 0 | 0 |

The 33 lines with `axiom` are the 33 `#print axioms` commands (L625-657); the whole word is `axioms`, so no `axiom` declaration exists. There are 33 theorems and 33 print commands, one each, matching the 33 reports in RECEIPT-2. The file has two `set_option` lines (autoImplicit false, Elab.async false) and one `set_option linter.unusedVariables false in`; none changes what the kernel accepts.

Verdict item 4: **HOLDS** (all six counts are zero as declarations).

## 2. Item 2: the new definitions in Stage2.lean

Stage 2 adds ten definitions. None enters the statement of `massGap_of_expClusters`: that type is Stage 0's (item 1). So no Stage 2 definition can weaken the final theorem; a wrong one could only make the proof fail. I still read each one for its meaning.

| definition | content | trivial? |
|---|---|---|
| `approximation` (L42) | release `ApproxTriple`: cutoff `K i.natPred`, state `ν i.natPred`, offset = the common face mean c of `faceMeanData` | no. Reindex ℕ+ → ℕ by natPred is a bijection (keeps j = 0; check 1458 dropped it, both fine). Probability of each state is proved, not assumed |
| `mesh` (L51), `scale` (L435) | `meshSize L K` = L^(−K) | no; `mesh_pos` proves > 0 from 13 ≤ L |
| `average` (L116) | linear extension of `listMoment μ` to the formal span | no |
| `connectedValue` (L119) | Re E(reflMulShift Z Z (t e₃)) − ‖E Z‖² | no; `latticeU_eq` proves it equals Stage 0's `latticeU` for t ≥ 0 |
| `negativeMirror` (L171) | mirror height −a/2, index −1 in a·ℤ/2 | no; check 1458's link mirror |
| `unitStep` (L173) | step a = 1·a, positive | no |
| `oddTime` (L175) | (2n+1)a | no; the same t as in `ExpClusters` |
| `linkTest` (L255) | spanRep(Z) − average(Z) at cutoff j | no; check 1458's A = B − νB |
| `osCovariance` (L542) | Re⟨v, T_{t⁺} v⟩ − \|⟨Ω,v⟩\|² | no; t⁺ = `toNNReal` is used only at t ≥ 0 |

No Prop is `True` by construction. No measure or span is zero. No index type is empty. The hypotheses of the intermediate lemmas are satisfiable: `linkTest_mem` and `oddMoment_eq` need mesh ≤ δ for the support margin δ of Z; `continuum_grid_bound` gets this from an eventual filter (mesh → 0) and intersects it with the frequent set of `ExpClusters`.

Verdict item 2: **HOLDS.**

## 3. Item 3: Hilbert space, vacuum, Hamiltonian, and what HasMassGap reads

### 3.1 The Lean objects (release at 3932084, read in ~/ym4d-papers/sa-ym4-lean-full, git HEAD 3932084)

- `ReflectionPositivity/ReconstructionOfAFunctional.lean`: `PhysicalSpace σ hσ` = `FormCompletion (reflectionForm σ) hσ`, the completion of the positive-time formal span under the reflection form. `vacuum` = class of the empty tuple. `timeShift` = `Classical.epsilon (IsTimeShiftFamily σ hσ)`, where the family must satisfy T_t[F] = [τ_{t e₃} F].
- `LimitTheorem/FunctionalDefs.lean` L78: `HasReconstruction σ h` = VacuumProperties ∧ TimeSemigroupProperties ∧ SpaceShiftProperties ∧ MatrixElementFormula.
- `ReflectionPositivity/ReconstructionOfTheLimitOfALatticeApproximation.lean` L24-39: TimeSemigroupProperties says the time-shift family is unique and is `timeShift`; it is a strongly continuous self-adjoint contraction semigroup with zero kernel; `pairHamiltonian` is the unique `IsHeatGenerator`, that is, it has a projection-valued resolution F on [0, ∞) with `timeShift t = F.expNegMulOp t`; and H Ω = 0.

So the space is the OS completion of σ = `centredOf S`, built from the continuum functional alone. The lattice triple `approximation` only supplies the hypotheses of `limit_reconstruction` (bound, reflection positivity, convergence). This is check 1458 R1 steps 1-4 (L36-44 of that file), and the same space that check 1653 Section 4 found faithful: the tr F² sector of separated C¹_c tensors.

### 3.2 What HasMassGap reads

`HasMassGap σ m` (Stage 0, unchanged): ∃ hσ, HasReconstruction σ hσ ∧ ∀ ψ with ⟨Ω, ψ⟩ = 0, ∀ t ≥ 0, ‖timeShift t ψ‖ ≤ e^(−mt)‖ψ‖.

With `timeShift t = e^(−tH)` for the unique heat generator H ≥ 0, this is the spectral gap of H. Proof: Ω is fixed by every e^(−tH) and these are self-adjoint, so Ω^⊥ reduces H. For ψ ⊥ Ω let μ_ψ be its spectral measure. Then ∫ e^(−2tλ) dμ_ψ ≤ e^(−2mt) μ_ψ([0,∞)) for all t. If μ_ψ([0, m−ε]) > 0, the left side is ≥ e^(−2t(m−ε)) μ_ψ([0, m−ε]), which contradicts the bound as t → ∞. So spec(H|Ω^⊥) ⊂ [m, ∞). The converse is the spectral theorem. With `HasMassGap.uniqueVacuum`: spec(H) ⊂ {0} ∪ [m, ∞) and ker H = ℂΩ. The bound is over **every** ψ in the completed space, not a dense set or only `posClass` vectors. It is not a weaker quantity such as decay of one correlator.

### 3.3 The reconstruction steps against the hand proof of check 1458

1. **Odd-grid moments** (`oddMoment_eq`, L330). Lean: Re m_n = `latticeU (ν j) Z ((2n+1)a)`, where m_n is the release's `reflectionMoment` at mirror −a/2, step a, insertion 1, test A = `linkTest`. The proof shifts both factors by +a: `translate_negativeMirror` proves τ_a ∘ r_{−a/2} = site reflection; `shift_comp_shift` gives τ_{(2n+1)a}. Check 1458 L27: m_n = ν(conj(r_{−a/2}A) τ_{2na}A) = ν(conj(θA) τ_{(2n+1)a}A) = u_j(Z;(2n+1)a). **Same.** This also settles the open convention of check 1653 Section 3(a): the kernel proved the identity with the release's `translate`, and the continuum `IsTimeShiftFamily` uses the same `translate`. So `latticeU` and `timeShift` move supports in the same direction, whatever that direction is.
2. **Log-convexity and the ratio** (`linkMoments`, `oddGrid_ratio`, `cutoff_ratio`). Positivity m_n ≥ 0 and m_{n+1}² ≤ m_n m_{n+2} come from the release's `periodic_gibbs_reflection_transfer` on the named ν_j. The scalar `sequenceLemma_of_bound` (row 1459) with q = e^(−2ma) gives m_{s+d} ≤ e^(−m(t_{s+d}−t_s)) m_s with no C. Check 1458 L33. **Same.** C may be any real; a negative C only strengthens the hypothesis.
3. **Dense times** (`refine_odd_times`, `continuum_grid_bound`, `bound_all_times`). Lean uses grids L^(−k)(2r+1), odd L, the frequent set of `ExpClusters` for this Z intersected with the eventual sets {mesh ≤ δ} and {K_j ≥ k}, and `le_of_tendsto_of_tendsto_of_frequently` on the whole-sequence moment limits (`latticeU_tendsto` from `Inputs.moments`). It then moves to all t ≥ 0 by continuity, with the left endpoint L^(−k) → 0. Check 1458 L50 and L59. **Same.** The rate is m, not a reduced rate.
4. **Completion** (`vacuum_mean`, `osCovariance_posClass`, `completed_covariance_bound`, `massGap_of_expClusters`). Lean: ⟨Ω, posClass Z⟩ = σ.spanExtension Z by span induction; the matrix-element formula at spatial shift 0 gives `osCovariance (posClass Z) t = connectedValue σ Z t`; the inequality is a closed condition in v at fixed t and `posClass` has dense range (`dense_range_posClass`), so it holds for every v. For v ⊥ Ω, the semigroup law and self-adjointness give osCovariance v (2t) = ‖T_t v‖², and osCovariance v 0 = ‖v‖²; the square root gives the rate m. Check 1458 L52-61 applies Q to posClass vectors instead of extending the covariance bound by closure. The two routes give the same statement.

Verdict item 3: **HOLDS.** The Hilbert space, vacuum and Hamiltonian are the release's OS reconstruction of `centredOf S` on the named witnesses. HasMassGap reads the spectral gap of that Hamiltonian on the whole vacuum complement.

## 5. Verdicts and limits

| item | verdict |
|---|---|
| 1. type of the discharging declaration | HOLDS |
| 2. new definitions | HOLDS |
| 3. Hilbert space, vacuum, Hamiltonian, HasMassGap | HOLDS |
| 4. forbidden tokens | HOLDS (all zero) |

Not checked here: the proofs (the kernel checked them; I did not replay them or run Lean), the statements of the release lemmas the proof calls, and the receipt's build log. The checks above rely on the receipt's report of the axiom lists. Nothing here is called new.

RESULT row 1665 (2026-11-28T06:39:27Z, Claude Opus 5.5 high, reading check; Lean not run): items 1-4 HOLD. Stage2.massGap_of_expClusters has exactly Stage 0's type, with no extra hypothesis (kernel example L613, which names the Stage 2 constant). No definition trivializes. The space, vacuum and Hamiltonian are the release's OS reconstruction of centredOf S, and HasMassGap is the spectral gap of that H on all of Ω^⊥. The token counts are 0. Open: ExpClusters (Stage 3) and the Stage 4 placeholders; rewiring Stage 0's compositions.
