lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-24T09:52Z

# Row 1449: does the kernel-checked Wilson continuum construction supply the gap chain's continuum inputs?

Started 2026-11-23T21:52Z (date -u), Mac mini worker 2, at commit 9f6c0bca2. Port reading, not a proof lane. No claim about the Lean release beyond its authors' recorded checks.

Credit: the source is Ethan Sussman and Levent Alpoge's public `YM4 Lean` release (written with OpenAI Codex assistance; reduced from the OpenAI Lean archives read in row 692), commit 3932084a9b82 of 2026-11-20. Quotes below are short and attributed.

## Plan

1. Locate the source. The row names a read-only checkout on an external volume. This session's scope rule allows reading only the repository, ~/ym4d-papers and own /tmp scratch, so the source is fetched by public URL into a /tmp scratch folder, pinned at 3932084a9b82.
2. Q1: read Challenge.lean, README.md, doc/Theorem.tex, doc/verification.md, Formulation/*.lean. State exactly what `YangMills.wilson_subsequence` and `YangMills.su2_fixed_observable_continuum_limit` assert.
3. Q2: read the gap chain's inputs (P1)-(P4), class C, (H2), (TOT) in library/gap-seed-audit-fable.md L104-130, gap-os-equiv.md Statement (5), gap-mini-branch-fable.md 5.3, rows 1342, 1349, 1356, 1359. Table: supplied / components only / not supplied, with the Lean declaration.
4. Q3: compare the Lean coupling sequence with the (M-neutral) trajectory of row 1367.
5. Q4: map onto library/t0-tree.md.
6. Next two rows with decisive outcomes; RESULT line.

## Repo search

(pending)

## Step 0. Source

Fetched by public URL into /tmp/ym4lean-w2-1449 (raw.githubusercontent.com, repository ethanwsussman/Yang--Mills-LLM-experiment, folder `YM4 Lean`, commit 3932084a9b82fc79466b4a2faad9ec032b637445, authored 2026-11-21T01:22Z, message "Update README.md"). The folder holds 12,651 files (135 MB). The external-volume checkout named in the row was not opened (scope rule of this session). Nothing was built or run. Read: Challenge.lean (264 lines), README.md, doc/Theorem.tex, doc/verification.md, then the Formulation files named below.

Their verification record (doc/verification.md, quoted in short): source fingerprint `3dcd0129...`; "Lean reported exactly `Classical.choice`, `Quot.sound`, `propext` for each theorem"; Con Leche accepted 333,678 grouped declarations; Nanoda accepted 342,294 expanded declarations; native and stock Comparator matched the public theorem; "The Windows Lake invocation exited with status 2" for the sandboxed stock rebuild. We have not replayed any of this.

Repo search: `grep -rn 3932084a` and `wilson_subsequence` over this target folder find only row 1449 and this file. Row 692 (`library/prior/oai-release-2026-11-11.md`) read the OpenAI release `YangMills.jointExistence`, which is a different theorem (beta/log(1/a) slope family, OPE, unique-vacuum Wightman for one phase). Their README says this construction "was carried out independently of OAI's".

## Step 1. Q1: what the two declarations assert

### 1a. `YangMills.wilson_subsequence` (Challenge.lean L260-262; proof Formulation/WilsonSubsequence.lean L70-72)

It is `Wilson.ContinuumLimitFor Wilson.selectedGauge` with `selectedGauge := specialUnitary 2`. Challenge.lean imports only Mathlib. Read from the Lean text (Challenge.lean L230-256), unfolded:

- **Model.** Torus `Site N = Fin 4 → ZMod N`, N = `siteCount L m K = 2 L^(m+K)`, mesh a = L^(-K), physical side `physicalSide L m = 2 L^m`. Law `law G N β` = product Haar times density exp(-β Σ_p s_p), normalised; s_p = `energy` = 1 - (1/2) Re tr U_p for SU(2). So β here is the standard Wilson β_W (β_W = 4/g_std^2 for SU(2)), and their g^2 = 1/β = g_std^2/4.
- **Observable.** `smear`: Φ(f) = Σ_p s_p f_ℓ(x_p), f_ℓ the ℓ-periodisation, x_p the barycentre. `centeredMoment` = E Π_i (Φ(f_i) - E Φ(f_i)). This is the renormalised tr F^2 density, centred; not a Wilson loop, not a field strength.
- **Coupling rule.** Reference torus side ℓ_0 = 2L^M (M fixed by L). `referenceResponse G L M K β` = centred two-point moment of (bump, bump translated by 3 e_1) on that torus; bump supported in radius 1/8 (Theorem.tex). `fixedPhysicalLevel G g0` = (3 dim G g0^4/π^4) ∫∫ χ(x) χ_0(y) |x-y|^-8. `couplingsAt` = {g > 0 : referenceResponse(β = g^-2) = level}; `bareCoupling` = sInf of it. Claimed: for all large k and every g0 in (0, δ), the infimum is attained (`IsLeast`). One threshold serves all g0 in (0, δ).
- **Quantifiers.** ∃ L_0, ∀ odd L ≥ L_0, ∃ M ≥ 1, δ > 0 with 8 ≤ 2L^M, [roots exist eventually in k uniformly in g0], and ∀ g0 ∈ (0, δ), ∃ K: ℕ → ℕ+ strictly increasing, m: ℕ → ℕ+ with 2L^{m_j} → ∞, v: ℕ → ℕ → ℕ+ with 2L^{v(j,t)} → ∞ in t for each j, and S: Family, such that the items below hold. **S depends on L, g0 and the extracted subsequence. No uniqueness of S is asserted.**
- **Asymptotic freedom.** g(K_j)^2 K_j log L → 24π^2/(11 C_A) with C_A = 8, i.e. 3π^2/11. (Their g^2 = g_std^2/4, so g_std^2 log(1/a_j) → 12π^2/11 = 1/(2 b_0) for SU(2): the one-loop rate.) No two-loop term, no rate of convergence.
- **Limits, order.** For each n and each `Separated` real tuple f (C^∞, compact support, pairwise disjoint `tsupport`): ∃ z: ℕ → ℂ with (i) for each j, centeredMoment on the torus of side 2L^{v(j,t)} at cutoff K_j → z_j as t → ∞ (infinite volume first, at fixed cutoff); (ii) z_j → S_n(f_1 ⊗ ... ⊗ f_n) as j → ∞; (iii) the diagonal sequence on sides 2L^{m_j} also → S_n(⊗f). Only separated tests. Nothing at coinciding points; S_n on non-separated tests is constrained only by the axioms below on flat tests.
- **`WilsonOS.EuclideanAxioms S`** (Challenge.lean L170-185), on `Flat` tests (Schwartz with all derivatives zero on the collision set Δ_n): normalisation S_0(c) = c; complex linearity on flat tests; growth |S_{n}(f)| ≤ c C^n (n!)^s p_{kn}(f) (Theorem.tex writes κ for s); full O(4) and translations (every R in `Matrix.orthogonalGroup (Fin 4) ℝ`, every v); permutation symmetry; reflection reality; reflection positivity on finite sequences of tests flat outside {distinct points, all times > 0}. **No clustering for S itself.**
- **`HasOSDecomposition S`** (L218-226): a probability space (Ξ, ρ) and T: Ξ → Family with (a) ∀ ξ, `WilsonOS.Axioms (T ξ)` = EuclideanAxioms plus spatial clustering: for admissible Φ, Ψ and every spatial v ≠ 0 (v_3 = 0), pairing(Φ, τ_{tv} Ψ) → (Σ T_n(JΦ_n))(Σ T_n(Ψ_n)) as t → ∞; (b) on separated tensors, ξ ↦ T ξ n (⊗f) is ρ-integrable and S_n(⊗f) = ∫ T ξ n(⊗f) dρ; (c) for ρ-a.e. ξ some separated smooth quadruple has nonzero connected 4-point. **Clustering is a limit with no rate.** The averaging formula is asserted on separated tensors only. Nothing says the components are extremal, distinct, or measurable beyond that integrability.
- **Nontriviality.** ∃ separated smooth pair with Re S_2 > 0; ∃ separated smooth quadruple with connected S > 0 (moment-cumulant formula, `connected`, L203-209). Since moments are centred, S_1 = 0 on separated tests, so this is the fourth cumulant.
- **Not asserted (by the statement's own text):** a mass gap or any decay rate; uniqueness of the limit, of the vacuum, or of the coupling sequence (only a subsequence); clustering of S; anything at coinciding points (contact terms); Wilson loops or other observables; the Wightman theory (`Reconstruction/` is excluded from the proof environment per verification.md); a non-Gaussian statement for S beyond one quadruple; any infinite-volume uniqueness.

### 1b. `YangMills.su2_fixed_observable_continuum_limit` (Formulation/FixedObservableContinuum.lean L169-171)

It is `FixedObservableLimit FixedObservableContinuum` (same file, L19-66, L70-80). It is the stronger internal statement; `wilson_subsequence` is derived from it (WilsonSubsequence.lean L14-67, via `continuum_matrix_iff_quaternion`). Extra content beyond 1a:

- **Infinite-volume lattice states.** ∃ ν_j, a measure on `InfiniteLattice.GaugeField (meshSize L K_j)`, with `InfiniteLattice.IsInfiniteVolumeLimit L (K_j) (β_j) (ν_j)`. The inner limit z_j of 1a is `InfiniteLattice.centeredMoment (ν_j) f` (WilsonSubsequence.lean L48). So at every cutoff of the subsequence there is an infinite-volume lattice state.
- **Cumulants.** S here is a `CumulantFamily`. Infinite-volume cumulants `smearedEnergyCumulant (ν_j) X` and torus cumulants `connectedSchwingerR4 L (m_j) (K_j) (β_j) X` both → S_n(X) for X in `TestSpaces.SepTupleOfCard n` (the README says separated compactly supported real C^1 tests).
- **β slope.** β_j/(K_j log L) → 11/(3π^2), i.e. β_j ~ (11/(3π^2)) log(1/a_j).
- **Components.** ∃ `A : SeparatedTuples.DecompositionData` with `A.IsCanonical (centredOf S)`; for each ξ a `FlatSequence` T with `HasSchwingerSequence (A.comp ξ) T` and `SystemsWithFiveBounds.OSAxioms D T`; a.e. ξ `IsNonGaussianOnSmoothQuadruple`.
- **Proof route as named in the file (not checked here).** `BranchHot.fixed_observable_continuum_of_no_escape`: exact selection of the least root "enters a fixed first-passage window along a subsequence if a positive fixed reference level cannot escape to an infinitely cold terminal state"; the no-escape input is `noEscapingTables_of_stageDecay Formulation.stopped_covariance_vanishes`. The subsequence K_j is extracted where the record-gap and root conditions hold frequently (`extraction_of_frequently_atTop`), and the continuum limit comes from `su2_continuum_limit_of_frequent_passage`. So the subsequence is not all large K; it is a frequent set chosen by the proof.

Open inside Step 1 (next): the definitions of `IsInfiniteVolumeLimit`, `SepTupleOfCard`, `DecompositionData.IsCanonical` and `SystemsWithFiveBounds.OSAxioms` (whether the component axioms include anything beyond Challenge's `Axioms`, e.g. a cluster rate).

### 1c. Definitions behind 1b, and what the proof proves internally

Files read (YangMills/Construction/...): SystemsWithFiveBounds/SystemWithFiveBounds.lean, SystemsWithFiveBounds/TheoremOverASystemWithFiveBounds.lean, LimitTheorem/ConditionsAtGivenConstants.lean, SeparatedSequences' `DecompositionData` (Continuum/CanonicalDecompositionOfAFunctional.lean), InfiniteLattice/InfiniteVolumeLimitPointsOfTheTorusStates.lean; Formulation/ContinuumLimit.lean L100-135, L260-319.

- **Canonical decomposition** (`DecompositionData.IsCanonical σ`): Ξ compact metrisable, ρ a probability with full support, ξ ↦ comp ξ continuous on each separated tuple and injective, each comp ξ permutation invariant and entrywise linear; and the defining identity ∫ comp_ξ(X) Π_k comp_ξ(Y_k) dρ = iterated limit of σ(X ∪ τ_{v_1}Y_1 ∪ ...) as the shifts go to infinity. So the components are the far-translation (cluster) decomposition of the separated functional. `DecompositionProperties` adds uniqueness up to isomorphism (internal).
- **Infinite-volume states.** `TorusStateLimitPoints`: at each admissible L, K > 0, β > 0, the set of weak limit points of lifted periodic Wilson measures on growing cubic tori is non-empty and closed; each limit point is Gibbs (`IsGibbs β`), invariant under lattice shifts and the hyperoctahedral group, and reflection positive across every axial half-integer plane (`IsSymmetricReflPosGibbs`); local quantities and separated Ursell functions converge along the subsequence; uniform Ursell bounds pass to the limit. No uniqueness of the infinite-volume state at fixed (K, β).
- **Component OS axioms** (`SystemsWithFiveBounds.OSAxioms K T`): growth, Euclidean invariance, OS positivity, permutation symmetry, `HasClusterProperty`, reflection reality. This is what the public theorem exports per component.
- **What the proof establishes per component but does not export.** `SystemsWithFiveBounds.ComponentProperties M ϑ d0 η K σ` (TheoremOverASystemWithFiveBounds.lean L240-249) holds for every component of every canonical decomposition, via `MainTheorem.Statement` / `ErgodicDecompositionConclusion.components`. It contains:
  - `InverseSquareClustering K σ`: for separated tuples X, Y and |v| ≥ r(X,Y), |σ(X ∪ τ_v Y) - σ(X)σ(Y)| ≤ C(X,Y) |v|^-2. **A polynomial cluster rate, not exponential.** C and r depend on the tuples.
  - `ComponentReconstruction σ`: ker H = ℂ Ω (unique vacuum per component), joint spectrum of (H, P) in the closed forward cone, |P_i| ≤ H, a unitary spatial-rotation representation.
  - `TwoPointLawHolds ϑ d0 η σ`: for separation d ≤ d0 and C^1 pairs in `separatedPairsR4 d ϑ`, the connected two-point value is (3(N^2-1)/π^4)(12π^2/(11N^2))^2 K_8(f,h)/log(1/d)^2 times (1+η) with (1+η) in [½(1-ηBar d)^4, 3/2(1+ηBar d)^4], ηBar(d) → 0. This is the short-distance asymptotic-freedom law of the two-point function, with N = 2.
  - `LocalCumulantBounds M K σ`: |connected_n(X)| ≤ localBound(n,d,R) Π ||f_i||_sharp and ≤ globalPrefactor(d,R) globalBase(R)^n (n!)^s Π ||f_i||_sharp, at separation d and support radius R. No decay in d beyond monotonicity.
  - `ComponentFieldData σ` (data for Wightman reconstruction).
  `ErgodicDecompositionConclusion` also has `ZeroEnergyIsL2`-type content in `LimitProperties` (ker H of the full limit ≅ L^2 of the decomposition law, internal) and `two_le_rank`.
- **Can the public route export more?** `fixed_observable_continuum_of_components` and `su2_continuum_limit_of_frequent_passage` are stated for any P with `HoldsForComponents P` (ContinuumLimit.lean L102-106: every σ with `ComponentProperties` has a Schwinger sequence T with P D T). So the same extraction yields components with any property derivable from `ComponentProperties`, e.g. the |v|^-2 cluster rate or ker H = ℂΩ. That instance is a few lines of Lean that the release does not contain. **Not built or checked here; a candidate, not a result.**
- **No mass gap anywhere in what was read.** The strongest cluster statement is |v|^-2. The internal `FiveBoundSystem` (SystemWithFiveBounds.lean L72-111) carries cutoff-uniform bounds: cumulant bound (a* max(1, d^-p) ballConst(R))^n (n!)^s, one-point bound, the lattice two-point law at K ≥ threshold(d), and a one-insertion bound. None of them decays in the separation.
