# Faithfulness check of lean/gapchain/GapChain/Stage0.lean (FINISH.md row 1653)

Checker: Opus 5.5 (Claude Code subagent). Reading check only; Lean not built or run.
Sources read are listed in section 0. Findings are appended as the check proceeds.

## 0. Sources read

- `lean/gapchain/GapChain/Stage0.lean` (all 376 lines), `lean/gapchain/RECEIPT-0.md` (all).
- `library/lean-gap-chain-design-fable.md` (row 1457, all 814 lines), `library/lean-gap-chain-design-check-astra62.md` (check 1458, all).
- `library/sa-ym4-lean-trajectory-check-astra62.md` (row 1453) L90-112, the statement of (M-neutral-all).
- `library/gap-k2-tool-design-fable.md` (row 1468) Sections 3.1-3.3; `library/gap-agy-seed-approaches-neon-check-astra62.md` (check 1527) part (ii) and the plan; `library/gap-agy-seed-neon.md` (row 1368) Section 0 and the statements of Theorem 4 and Corollary 5 (by grep, not the proofs).
- `library/gap-direction8-fable.md` (row 1643) Sections 1.1, 1.5, 1.6, 3.
- Hand definitions behind the Lean objects: `library/gap-flux-exercise.md` (row 731) 3.0 and 8.4; `library/gap-solve9-astra62.md` (row 1161) L40-65, L140-152, L210-228.
- Other modules: `Wilson.lean` L1-165 (Sides, Site, transport, halfTrace, centerMinus, action, partition), `LemmaM1.lean` (HSNormLE, ketBra, lemmaM1). `lean/gapchain/RECEIPT.md` headings only.
- Not read: `Stage2.lean`, `RECEIPT-2.md` (as instructed). The Sussman-Alpoge release is not in this folder. Where a verdict rests on a release convention, I say so and name the file that reports it (mostly check 1458, which read the release at 3932084a9b82).

Method: I compared each declaration with the hand statement it encodes. I did not build or run Lean. Where Lean's acceptance settles a point (for example `Iff.rfl`), I rely on the receipt's kernel output.

## 1. The physical hypothesis (item 1)

### 1.1 Centre action and P_0

- `centreElt` = `Wilson.centerMinus` = the matrix -1 in SU(2). **FAITHFUL.**
- `centreSign Γ μ cuts e`: -1 on a slice link whose axis is in `cuts` and whose source has residue 0 in that axis; +1 elsewhere. Row 1468 3.1: "C_z multiplies by -1 the links (x, i) with z_i = 1 and x_i = 0". The design 4.1 has the same rule for one axis. A link has one axis, so the rule for a set of cuts is the product of the single-axis rules. **FAITHFUL.** Not confirmed here: that `Γ.coordResidues p ν` is the residue of the ν-coordinate mod the side. Check 1458 item 2 read it ([coords] link) and found the sign well defined on orbits.
- `centreShift`, `centreShift_measurePreserving`, `centreTranslation`, `IsCentreTranslation`, `centreTranslation_spec`. The translation is the pullback φ ↦ φ ∘ shift, built from Mathlib's `Lp.compMeasurePreserving`. This replaces the design's `Classical.epsilon` (design 4.1 point 2) by an explicit operator. That is better than the design: no existence lemma is needed. **FAITHFUL.**
- `neutralProj` = (1/8) Σ over the 8 subsets of the three axes other than μ of `centreTranslation`. The map cuts ↦ C_cuts is a homomorphism from (Z_2)^3 (symmetric difference) to unitaries, so the average is the orthogonal projector onto the centre-invariant vectors. Hand P_0 (row 1468 3.1, check 1453) is the projector on centre-neutral **gauge-invariant** states. Here P_0 is the centre average only, on all of L^2. The release's T carries P_G on both sides (design 2.1), and C_z commutes with gauge transformations (−1 is central). So P_0 T^w = (P_0 P_G) T^w for w ≥ 1. Check 1527 (i) makes the same remark ("on raw L^2 the latter is P_G (1/8) Σ C_z"). **FAITHFUL** for every use in Stage 0 (always P_0 T^u with u ≥ 1). The receipt's scratch check reports the mask count 8.

### 1.2 The rank-one test on one cube

`RankOneAtTime Γ μ β w` = ∃ φ, c with ‖φ‖ = 1, 0 < c, and `HSNormLE (c⁻¹ • (P_0 * T^w) − ketBra φ) (2/5)`. `NeutralRankOneTest` = ∃ w, 1 ≤ w ∧ 1024 w ≤ Γ.side ∧ `RankOneAtTime`.

Against row 1453 L101-105: "an integer 1 ≤ w_K ≤ n_K/1024, a unit vector φ_K, and c_K > 0 with ‖c_K^(-1) P_0 T_K^(w_K) − |φ_K⟩⟨φ_K|‖_HS ≤ 2/5".
- 1 ≤ w and 1024 w ≤ n: exact (1024 w ≤ n is w ≤ n/1024 over the integers).
- `ketBra φ` = `rankOne ℂ φ φ` = x ↦ ⟪φ, x⟫ φ, the projector |φ⟩⟨φ| for a unit φ.
- `HSNormLE A δ`: every finite orthonormal family has Σ ‖A e_i‖² ≤ δ². Check 1458 item 1 shows this is ‖A‖_HS ≤ |δ| on the complete slice space, and that it cannot accept a divergent sum. δ = 2/5 ≥ 0. 
- The scale c is real and positive, as in the hand statement.
- The transfer is `Γ.transfer μ β`, the release's T = P_G K^(1/2) e^(−V) K^(1/2) P_G. The lane's T is e^(−V/2) K e^(−V/2) on invariant functions. Check 1458 item 3 shows that the nonzero neutral spectra agree with multiplicity, so the test at a given w is the same statement s(2w) ≤ 4/21 in both forms (row 1356 M1/M2).
**FAITHFUL.**

### 1.3 Cutoff, side, coupling, tail

- `betaAt L M K g₀` = (renormalizedBareCoupling L M K g₀ ^ 2)⁻¹. This is β_K = g_K^(−2) at the release's least root, at every cutoff K, as the design 4.2 and check 1458 item 4 require. At the extracted cutoffs, `FixedObservableWitnesses` itself states `IsLeast {u | 0 < u ∧ ...} (g j)` for this same `renormalizedBareCoupling`, so the identification is kernel-checked there. **FAITHFUL.**
  Remark (benign; not confirmed against the release). If the root set is empty at some cutoff, Lean's `sInf ∅ = 0` would give `betaAt = 0`. At β = 0 the bond kernel is constant, T is the rank-one projector on constants, and the test holds with c = 1. So at such a cutoff (M-neutral-all) would be trivially true. This only weakens the hypothesis at cutoffs that no consumer reads: every consumer uses the K_j, where `Inputs.beta_pos` holds. No effect on the implication.
- `NeutralAtCutoff L M g₀ ℓ K`: every Γ with `Γ.side = ℓ * L^K` passes the test at `TimeAxis.timeIdx` and β_K. Cube side n_K = ℓ b^K with b = L: exact. All such Γ are one cube (check 1458 item 4), and the receipt's `seedCubeExists` shows the ∀ is not empty. Time axis: `TimeAxis.timeIdx`, the correction of check 1458. **FAITHFUL.**
- `MNeutralAll L M g₀ ℓ` = 0 < ℓ ∧ 4 ∣ ℓ ∧ ∃ K₀, ∀ K ≥ K₀, `NeutralAtCutoff`. Row 1453: "a single physical side ℓ ∈ 4ℕ_{>0} and a K₀ such that for every K ≥ K₀ ...". The witnesses w, φ, c may depend on K: they do (they sit inside `NeutralAtCutoff K`). The seed of row 1453 is `∃ ℓ, MNeutralAll L M g₀ ℓ`, and the packaged theorem quantifies `∀ ℓ, MNeutralAll ... ℓ → ...`, which is the same thing on the left of an implication (check 1458 item 4, last paragraph). **FAITHFUL.**
- `MNeutralAlong` (frequent j along a given K), `KappaSeedAlong`: the design's (M-neutral-Lean) and the frequent κ-seed. **FAITHFUL.**

### 1.4 Which hypothesis this is: (M-neutral-all), not (PUR-io)

Stage 0 encodes **(M-neutral-all) of row 1453 exactly**, at the aspect 1024 of the row 1161 route. It does **not** encode the lane's current weakest consumer. Three differences, each read from the hand files:

1. **All late cutoffs, not infinitely many.** Row 1468 3.1 states the consumer as "(PUR-io) P_K ≥ 457/625 at infinitely many K, for one l and one g_0", and row 1643 A2 records that (PUR-io) gives "a calibrated continuum limit" with a gap. Check 1527 (ii), Handoff, says why that conclusion is existential: row 1461 selects a defining subsequence *inside* the passing set E, and "A gap for every preassigned limit ... do[es] not follow". Stage 0 fixes the release's witnesses first (from `su2_fixed_observable_continuum_limit`) and asks for the gap of *that* S. For a preassigned limit the hypothesis must hold along the witness sequence K_j, which an io-hypothesis does not give. So the all-late-K hypothesis is the correct one for Stage 0's conclusion. It is stronger than (PUR-io). A proof of (PUR-io) alone would not discharge it. This agrees with row 1643 1.5 ("(PUR-io) does not plug into the kernel-checked theorem"); it now also holds for Stage 0. Row 1468 3.3 gives the bridge: (BASE-K2) at every late K gives (M-neutral-all).
2. **The aspect.** `NeutralRankOneTest` asks for some w ≤ n/1024. Row 1368 Corollary 5 and check 1527 (ii) give sufficient forms at smaller aspects (w ≤ n/68 via B3 and SH, or the threshold 5/9 at a changed aspect), with other thresholds and rates. Monotonicity goes the wrong way (check 1527 (ii): "monotonicity goes the wrong way to infer s(2⌊n/1024⌋) ≤ 4/21"). So a seed proved at those aspects does not discharge Stage 0's hypothesis on the same side. Check 1527's own handoff recovers (M-io-exists) on an enlarged side ℓ' = 2^(j+8) ℓ; that ℓ' is an integer multiple of 4, and β_K stays the least root at K, so it fits `NeutralAtCutoff` at ℓ' — but only at the passing cutoffs, so difference 1 still applies.
3. **The form of the test.** (PUR-io) is a purity bound on sixteen masses. Fact PUR gives s_K(u) ≤ 4/21 at u = n/512. Turning that into `RankOneAtTime` at w = n/1024 needs the **converse** direction of Lemma M1 (row 1356), which Stage 1 did not build (W1 is the forward direction only). This does not affect Stage 0's statements; it matters for any future "PUR to M-neutral" lemma.

Verdict for item 1: **FAITHFUL to (M-neutral-all) as row 1453, row 1457 4.2 and check 1458 state it.** Not a statement of (PUR-io). This is a scope fact, not an error: Stage 0's brief and design ask for (M-neutral-all), and its preassigned-limit conclusion needs it.

## 2. Finite-volume quantities and kappaWeight (item 2)

### 2.1 NeutralTailLE and NeutralPhysicalSeed

`NeutralTailLE Γ β u b`: with T the time-axis transfer and A = P_0 T^u, require 0 < ‖T‖, `TraceSummablePW A`, and Re(tracePW A)/‖T‖^u − 1 ≤ b.

Row 1161 L144: "Normalize every static magnetic transfer F_m by λ_0 = ‖F_0‖ of the same spatial box. ... s(v) = X_{0,0}(v) − 1", with X_{0,0}(v) = Tr_{q=0}(F_0/λ_0)^v the periodic neutral trace. So s(u) = Tr(P_0 T^u)/‖T‖^u − 1. The Lean quantity is this, with the release's T and the Peter–Weyl trace. The summability and ‖T‖ > 0 clauses stop a junk value (Lean's `∑'` of a non-summable family is 0; division by 0 is 0). Both clauses are true at β > 0 (T is trace class and nonzero). **FAITHFUL.** Convention not confirmed here: that `tracePW` sums ⟪e_k, A e_k⟫ over a complete basis; check 1458 item 1 reports the release's Peter–Weyl completeness and Parseval.

`NeutralPhysicalSeed Γ β` = ∃ u, 3 ≤ u ∧ 512 u ≤ side ∧ `NeutralTailLE` u (1/2). Row 1161 L213: "Suppose s(u) ≤ 1/2 for an integer 3 ≤ u ≤ n/512"; design N2: "u = max(3, 2w) ≤ n/512, s_+(u) ≤ 1/2". **FAITHFUL.**

### 2.2 twistedPartition and pfaffianSign

`twistedPartition β sides k` = ∫ exp(−β Σ_x Σ_{p=(i<j)} (1 − sign · halfTrace(transport U x i j))) d(Haar), with sign = −1 iff k p ∧ x_i = 0 ∧ x_j = 0.

Row 731 3.0: "The stack of the plane (μ,ν) is the set of (μ,ν)-plaquettes with base point at x_μ = x_ν = 0. ... s^k_p = −1 if p lies in an odd number of the stacks of the planes with k_{μν} = 1 ... Z^k(n) is the integral of exp(−β Σ_p (1 − ½ s^k_p tr U_p))." A plaquette lies only in the stack of its own plane, so "odd number of stacks" is "its own plane is twisted and it is on that stack". `halfTrace` = Re tr/2; `Wilson.haar` is the product of normalized Haar measures; one geometric plaquette per site and plane (`action_eq_geometric`). `twistedPartition_untwisted` proves k = 0 gives `Wilson.partition`. **FAITHFUL.**

`pfaffianSign k` = product over the pairs (01|23), (02|13), (03|12) of (−1)^(k_p k_q). Row 731 8.3: Pf(k) = k_12 k_34 + k_13 k_24 + k_14 k_23 on axes 1..4. Shifting to 0..3 gives exactly the three Lean pairs. The set of three perfect matchings is invariant under all axis permutations, so the sign does not depend on which axis is time. **FAITHFUL.**

### 2.3 kappaWeight and KappaSeedOnCube

`kappaWeight β sides` = (Σ over the 64 maps k : Plane → Bool of pfaffianSign k · twistedPartition β sides k) / 8. Row 731 8.4: "W_kappa = (1/8) sum over all 64 twists of (−1)^{Pf(k)} Z^k". Exact, prefactor 1/8. Consistency check: with m = 0 every Pf term vanishes, so the eight electric twists enter with sign +1 and give (1/8) Σ_e Tr(C_e T^N) = Tr(P_0 T^N); 1/8 is the right weight. The receipt's scratch check reports the count 64. **FAITHFUL.**

`KappaSeedOnCube Γ β`: N = side/2; sides = N on the time axis and `Γ.side` on the other three; top = ‖T‖ of the n^3 slice; require 0 < top and kappaWeight/top^N − 1 < 2^(−18). Theorem S-w (row 731 8.4): S_w(a; B) := W_w(a, B)/λ_0(B)^a − 1, with λ_0(B) the top eigenvalue of the periodic box (Lemma W (c)); the seed is S_w(N; (2N)^3). Here 2N = n (4 ∣ n gives exact division), B = n^3, a = N. Row 1161 L213: "In both cases S_κ < 2^(−18)" on Q_{n/2}. **FAITHFUL.** The equality λ_0(B) = ‖release T‖ is a hand identification (check 1458 item 3); it is a proof obligation of Stage 4, not a statement issue.

### 2.4 The 4/21 bound at 2w and at max(3, 2w)

`neutralTail_of_rankOneAtTime` (placeholder, Stage 4): from `RankOneAtTime` at w ≥ 1 and β > 0, `NeutralTailLE` at 2w and at max(3, 2w), both with b = 4/21. Hand: row 1356 M2 forward direction, s(2w) ≤ 4/21, then monotonicity in u. Section 5 below checks that it is true as stated. **FAITHFUL.**

`neutralPhysicalSeed_of_mNeutral` (proved, inherits the placeholder): takes the second conjunct (u = max(3, 2w)) and 4/21 ≤ 1/2, and proves 512 max(3, 2w) ≤ side from 1024 w ≤ side and 1536 ≤ side. The case w = 1 needs 1536 ≤ side; it is supplied from side ≥ 2^70. Correct. The name says "of_mNeutral", but the hypothesis is the one-cube `NeutralRankOneTest`; the statement is what the docstring and design N2 say.

## 3. latticeU and ExpClusters (item 3)

`listMoment ν fs` = `centeredMoment ν fs.get`: the lattice moment of a list of any length, overlaps allowed. This is check 1458's correction (do not use `SepTuple.juxt`, which returns the empty tuple on overlap). **FAITHFUL.**

`latticeU ν Z t` = Re Σ_{X,Y ∈ supp z} conj(z_X) z_Y · listMoment(θ_* X ++ (τ_{t e_3})_* Y) − |Σ_X z_X listMoment(X)|². Check 1458, 4.4: the same formula, word for word (conjugate the first coefficient, reflect the first tuple, translate the second, subtract the squared mean in the same state, real part).

Is it the correlation the reconstruction needs? Write B_X for the product of individually ν-centred smeared energies, F = Σ conj(z_X) B_{θX}, H = Σ z_Y B_{τY}. Then the double sum is ν(F H), and by reflection and shift invariance of ν the mean term is ν(F) ν(H). So latticeU is Re of a covariance. In the limit, with σ = centredOf S, it tends to ⟨v, T_t v⟩ − |⟨Ω, v⟩|² = ‖T_{t/2} Q v‖² for v = posClass Z (check 1458, "Lines 314–322"). The lattice moment centres each factor, as the continuum `centredOfCumulants` does, and `Inputs.moments` states exactly this convergence. **FAITHFUL.**

Conventions I could not confirm here (release not in this folder): (a) that `pushList (translate (t • timeBasisVec))` moves supports **up** by t (pushforward) and not down; (b) that `TimeAxis.timeReflection` is the site reflection x_3 ↦ −x_3. Check 1458 writes (τ_t)_* and θ_* and verified the odd-grid identity m_n = u_j(Z; (2n+1) a_j) against the release with these meanings. If (a) were reversed, the definition would still type-check but Stage 2's odd-moment identity would fail; Stage 2 must prove that identity, so a build would expose it. I record it as the first thing Stage 2 should confirm.

`ExpClusters L K ν m` = ∀ Z ∈ PositiveSpan, ∃ᶠ j, ∃ C, ∀ n ∈ ℕ, latticeU (ν j) Z ((2n+1) a_j) ≤ C exp(−m (2n+1) a_j), a_j = `meshSize L (K j)`. Check 1458: "Keep the order ∀Z ∃^freq j ∃C_{j,Z} ∀n with one common positive physical rate"; the odd grid (2n+1) a_j for n ≥ 0 at the link mirror −a_j/2; the full C^1_c positive span. All three are present. **FAITHFUL.** (Convention not confirmed: `meshSize L K` = L^(−K); check 1458 "The two tori" reports mesh a = L^(−K).)

`CutoffStates`, `Inputs` (strictMono, beta_pos, isLimit, moments). Check 1458, R1 and 4.4: these four public clauses suffice for reconstruction; the design's `mixture` field "can be retained but is unnecessary". It is dropped. `FixedObservableWitnesses.inputs` derives all four from the export. **FAITHFUL.**

## 4. The continuum conclusion (item 4)

- `HasMassGap σ m` = ∃ hσ : IsPosSemidef (reflectionForm σ), HasReconstruction σ hσ ∧ ∀ ψ ⊥ Ω, ∀ t ≥ 0, ‖timeShift t ψ‖ ≤ e^(−m t) ‖ψ‖. Design 4.3, unchanged. `HasReconstruction` pins the epsilon-chosen `timeShift` (design 4.3 point 1; check 1458 4.3). The time scale: check 1458 derives ‖T_r Qv‖ ≤ e^(−M r)‖Qv‖ from (EC-ν) at rate M, so the rate in `ExpClusters` and in `HasMassGap` is the same number. **FAITHFUL.**
- `HasUniqueVacuum σ`: every vector fixed by all timeShift t is c Ω. **FAITHFUL.** With `HasMassGap.uniqueVacuum` (m > 0) the pair says: simple vacuum, and spectrum of H in {0} ∪ [m, ∞) (check 1458 4.3 gives the equivalence with the heat resolution). The space is `PhysicalSpace (centredOf S)`, the completion of positive-time separated C^1_c tensors of centred smeared plaquette energies: the tr F^2 sector, as design 4.3 point 4 and the receipt say. The flat-Schwartz space is Stage 5. Correctly scoped.
- `gapRate ℓ` = (2/ℓ) log(2^18/5041) with real casts. Theorem S-w: s < 2^(−18) gives m_0 > log(2^18/5041)/N with N = n/2 lattice steps; mesh a with n a = ℓ gives the physical rate ≥ (2/ℓ) log(2^18/5041). Check 1458 4.5 states the same. **FAITHFUL.**
- Blocking factor. `massGap_of_expClusters`, `kappaSeedAlong_of_mNeutral`, `expClusters_of_kappaSeed`, `expClusters_of_mNeutral`, `massGap_of_mNeutral` all take `Conventions.IsAdmissibleBlockingFactor L`. The top proof builds it as ⟨hodd, 13 ≤ L⟩ and `kappaSeedAlong_of_mNeutral` uses `hL.2` for L ≥ 2. So the predicate is Odd L ∧ 13 ≤ L, as check 1458 reports. This is check 1458's correction of the design's 3 ≤ L. **FAITHFUL.**
- `FixedObservableWitnesses` and `fixedObservableContinuum_iff` (`Iff.rfl`). The kernel accepted `Iff.rfl`, so `∃ K v ν S X₂ X₄, FixedObservableWitnesses ...` is definitionally the release's `FixedObservableContinuum L M g₀`, all conjuncts and scopes included (D, T at their inner scope; A, D at theirs; the per-n quantifiers). This is the strongest faithfulness check in the file. **FAITHFUL.**
- `FixedObservableContinuumWithGap`: one ∃ over the six witnesses, the full witness predicate, then ∀ ℓ, MNeutralAll ℓ → gap ∧ unique vacuum for `centredOf S` of the same S. This is check 1458's repaired packaging (one binder block; no second existential that could pick another S). **FAITHFUL.**
- `su2_fixed_observable_gap_of_mNeutral : FixedObservableLimit FixedObservableContinuumWithGap`. The proof takes L₀ from the release, raises it to max(L₀, 13), keeps M, δ and the calibration clauses of the release, and for each g₀ ∈ (0, δ) reuses the release's witnesses. The outer order is the release's own (check 1458: M, δ after L; calibration before g₀; witnesses and ℓ inside g₀). The receipt's `forgetGap` reports that dropping the gap clause gives back the release statement. **FAITHFUL.**

## 5. The four placeholders (item 5)

For each I ask: is it false as stated, or stronger than what the hand chain proves?

**P1. `neutralTail_of_rankOneAtTime` (Stage 4, W8). True as stated; equal in strength to row 1356 M2 (forward) plus monotonicity.** My hand derivation, for any cube and β > 0. Let B = P_0 T^w. P_0 is an orthogonal projector that commutes with T (each C_z commutes with P_G, with the bond operator and with e^(−V): a spatial plaquette in plane (ν, j) holds two ν-links with the same ν-coordinate, so both or neither flip). So B ≥ 0, B² = P_0 T^(2w), B is Hilbert–Schmidt. Stage 1's `lemmaM1` with δ = 2/5 gives (21/25) Tr B² ≤ ‖B‖² ≤ ‖T‖^(2w). So Tr(P_0 T^(2w))/‖T‖^(2w) − 1 ≤ 4/21. This needs no assumption that the top eigenvector is neutral: ‖P_0 T^w‖ ≤ ‖T‖^w suffices. For u' = max(3, 2w) ≥ 2w: Tr(P_0 T^(u')) ≤ ‖T‖^(u'−2w) Tr(P_0 T^(2w)), so the bound carries over. Summability and ‖T‖ > 0 hold because T is trace class and nonzero at β > 0 (release `TransferProperties`). Not false, not stronger.

**P2. `kappaSeed_of_neutralPhysicalSeed` (Stage 4, W7). Same strength as row 1161's explicit-aspect theorem; not false on any reading I can test.** Hypotheses 4 ∣ n, n ≥ 2^70, β > 0, ∃ u with 3 ≤ u ≤ n/512 and s(u) ≤ 1/2; conclusion S_κ(n/2; n^3) < 2^(−18) in periodic-vacuum units. Row 1161 L213: "One sufficient lattice range is 4∣n, n≥2^70. Suppose s(u)≤1/2 for an integer 3≤u≤n/512 ... In both cases S_κ<2^(−18)", for every coupling. Check 1162 read it; row 1643 3.2 re-derived its eleven numerical inequalities (structure not re-checked). Truth rests on that hand theorem and on the identification of λ_0 with ‖release T‖. Nothing is added.

**P3. `massGap_of_expClusters` (Stage 2). Same strength as check 1458's hand proof; not false.** Hypotheses: admissible L, the four `Inputs` clauses, m > 0, (EC-ν) on the odd grid. Conclusion: positivity, reconstruction and the semigroup bound at the same rate m. Check 1458 proves exactly this by hand (sequence lemma at the link mirror −a/2; limit on the nested odd grids D_k, which needs L odd; strong continuity; density of posClass in Ω^⊥), and supplies positivity and `HasReconstruction` from the same four public clauses with admissible L. The hypothesis `C ∈ ℝ` with no sign is harmless (a negative C only strengthens the hypothesis, since latticeU on the grid is a reflected moment, hence ≥ 0). Open convention: the translate direction of Section 3 (a).

**P4. `expClusters_of_kappaSeed` (Stage 3). Same strength as the hand lower half; not false on the hand record.** From the frequent κ-seed on cubes ℓ L^(K_j) at β_(K_j): Theorem S-w (row 731) gives the even gap m_0 > (2/n) log(2^18/5041) on every cube L' ≥ n at that β; the release's ν_j are weak limits of tori of side 2 L^(m+K_j) ≥ n; EV-L (c, d) and P-ev (b) give the covariance bound for bounded continuous centre-blind local functions; check 1458 "Lines 324–332" turns that into (EC-ν) at the j of the seed, with C_{j,Z} absorbing the slab width. The good set of j does not depend on Z here, so the conclusion's ∀Z ∃ᶠj is weaker than what the hand gives. Not stronger. The hand inputs (TM-tw), (S), (L), EV-L, P-ev and the two-torus bridge W10 are hand proofs, several "HOLDS AFTER CORRECTION" (row 1643 A2).

No placeholder is false as stated, and none is stronger than the hand chain proves. So the conditional top theorem is not vacuous for a false-placeholder reason. Its only vacuity is the one the design names (4.5 point 3): if (M-neutral-all) is false, the clause is empty.

## 6. The thirteen proved theorems (item 6)

| Theorem | What it proves | Weaker than its name? |
|---|---|---|
| `centreShift_measurePreserving` | the shift preserves product Haar | no |
| `centreTranslation_spec` | the defined operator satisfies the pullback formula a.e. | no (it does not claim unitarity or involution) |
| `twistedPartition_untwisted` | zero twist = `Wilson.partition` (the lane's Wilson module, not the release's trace) | no; the receipt says `Wilson.partition` |
| `neutralPhysicalSeed_of_mNeutral` | one-cube test → one-cube N-phys, given 1536 ≤ side; inherits P1 | name says "mNeutral"; hypothesis is the one-cube test. Statement matches docstring and design N2 |
| `MNeutralAll.along` | all late K → frequent along any strictly increasing K | no |
| `HasMassGap.uniqueVacuum` | gap at m > 0 → every fixed vector is c Ω; no placeholder | no |
| `gapRate_pos` | rate > 0 for ℓ > 0 | no |
| `kappaSeedAlong_of_mNeutral` | frequent test → frequent κ-seed, with 4 ∣ n and n ≥ 2^70 proved from K_j ≥ 70 and L ≥ 2; inherits P1, P2 | no |
| `expClusters_of_mNeutral` | composition; inherits P1, P2, P4 | no |
| `massGap_of_mNeutral` | composition plus uniqueVacuum; inherits all four | no |
| `fixedObservableContinuum_iff` | `Iff.rfl` | no; it is the definitional check |
| `FixedObservableWitnesses.inputs` | the four `Inputs` clauses from the export | no |
| `su2_fixed_observable_gap_of_mNeutral` | the packaged conditional theorem; inherits all four | no; "of_mNeutral" marks it conditional, and the receipt says `sorryAx` |

None proves less than its name says. Eight of the thirteen depend on no placeholder. The other five (`neutralPhysicalSeed_of_mNeutral`, `kappaSeedAlong_of_mNeutral`, `expClusters_of_mNeutral`, `massGap_of_mNeutral`, `su2_fixed_observable_gap_of_mNeutral`) call one, and the receipt's axiom list shows `sorryAx` for exactly those five plus the four placeholders.

## 7. Verdict per declaration

Definitions (29): `centreElt`, `centreSign`, `centreShift`, `centreTranslation`, `IsCentreTranslation`, `neutralProj`, `RankOneAtTime`, `NeutralRankOneTest`, `NeutralTailLE`, `NeutralPhysicalSeed`, `twistedPartition`, `pfaffianSign`, `kappaWeight`, `KappaSeedOnCube`, `betaAt`, `NeutralAtCutoff`, `MNeutralAll`, `MNeutralAlong`, `KappaSeedAlong`, `HasMassGap`, `HasUniqueVacuum`, `listMoment`, `latticeU`, `CutoffStates`, `ExpClusters`, `Inputs`, `gapRate`, `FixedObservableWitnesses`, `FixedObservableContinuumWithGap`: all **FAITHFUL**.

Theorem statements (17: four placeholders, thirteen proved): all **FAITHFUL**. No correction is needed for any statement.

Release conventions I could not confirm from this folder (each is reported by check 1458, which read the release): `coordResidues` is the residue mod the side; `pushList (translate v)` moves supports by +v; `timeReflection` is x_3 ↦ −x_3; `meshSize L K` = L^(−K); `tracePW` is the diagonal sum in the complete Peter–Weyl basis; the matrix-element scaling between `reflectedCorrelation` and `timeShift`; `renormalizedBareCoupling` off the extracted cutoffs (only the benign remark of 1.3 depends on it).

Notes for the lead (no file other than this one was written):
1. Stage 0 is conditional on (M-neutral-all) at aspect 1024, at **every** late cutoff. A proof of (PUR-io) (row 1468 3.1, row 1643 A2), or of a seed at the smaller aspects of row 1368 / check 1527 (ii), does not discharge it. The standing text should say which seed Stage 0 consumes. To consume (PUR-io) a different top theorem is needed: one that re-selects the release's cutoff sequence inside the passing set (row 1461), which the exported `FixedObservableLimit` does not allow without reopening the release's private step.
2. A future "PUR to rank-one test" lemma needs the converse of Lemma M1, which Stage 1 did not build.
3. Stage 2 should first confirm the translate direction of `pushList` in the odd-moment identity.

## RESULT

RESULT row 1653 (Claude Opus 5.5 high, reading check of row 1652; nothing built or run). All 29 definitions and all 17 theorem statements of Stage0.lean are FAITHFUL; no correction needed.
(1) Hypothesis: FAITHFUL to (M-neutral-all) of row 1453 (side ℓL^K, β_K = least-root g_K^(−2), 1 ≤ w, 1024w ≤ ℓL^K, HS error ≤ 2/5, 4 ∣ ℓ, all K ≥ K₀). It is not (PUR-io): io-cutoffs, the smaller aspects of rows 1368/1527 and the purity form do not discharge it.
(2) kappaWeight: FAITHFUL (row 731 Pf sign, 64 twists, 1/8; S_κ(n/2; n^3) in periodic-vacuum units); 4/21 at 2w and max(3,2w): FAITHFUL.
(3) latticeU / ExpClusters: FAITHFUL; the correlation is Re cov → ‖T_{t/2}Qv‖², odd grid, ∀Z ∃ᶠj ∃C ∀n. Translate direction not confirmed here.
(4) Continuum: FAITHFUL; unique vacuum and semigroup gap (2/ℓ)log(2^18/5041) on the tr F² separated-tensor completion; Odd L ∧ 13 ≤ L; Iff.rfl fixes the witness scopes; one witness block, then ∀ℓ.
(5) Placeholders: none false, none stronger than the hand chain (P1 re-derived here; P2 = row 1161; P3 = check 1458; P4 = rows 731/1179 with check 1458).
(6) Proved theorems: none weaker than its name; 8 placeholder-free, 5 inherit sorryAx.
Stage 2 may build on Stage 0 as it stands.
