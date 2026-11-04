# YM4 assembly: our proof of T0, by submanuscript

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, written for the lead at the owner's direction ("we should be able to build the skeleton they did, and then prove it"). Research text. It is not an audit, it grants no status, and it is not yet checked by the other model. It follows `library/process-review-2026-11-04.md`, Section 4, item 1.

Credit. The architecture below follows the assembly of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) wherever it is sound: their one-page `YM4_assembly_overview.pdf` (thirteen positions L, M, G, E, N, P, C, T, R, K, H, V, Z), their `QED3_assembly_outline.tex`, the outline `YM4_sketch_500.tex` and the complete account `theorem_0_complete_account_raw_I/II/III.tex`, all at commit `31a47c543775`, and their YM3_I text. Tadeusz Balaban's papers (CMP 89, 95, 96, 98, 99, 102, 109, 116, 119, 122a, 122b) are the source of the renormalisation-group method. Jonathan Dimock's expositions ("The renormalization group according to Balaban" I–III, arXiv 1108.1335, 1212.5562, 1304.0705; his QED_3 series, arXiv 1502.02946, 1512.04373, 1712.10029, 2009.01156) are the readable complete proofs we port from. Osterwalder and Schrader (OS I, OS II) are credited for the reconstruction method. Every library note named below credits its own sources.

## 0. Conventions

**Texts and line numbers.**

- **SA L** is a line of the outline `YM4_sketch_500.tex` (32,992 lines; the local copy is `scratchpad/sa/ym4.tex`).
- **CA-I, CA-II, CA-III L** are lines of the complete account, parts I–III (local copies `scratchpad/sa/ca_I.tex` etc.). Chapter starts, read here: CA-I L3531 "The coupling flow and ultraviolet stability"; CA-II L5 "Bounds on connected correlations on the torus", L60348 "A volume-free bound for each ball", L64630 "Limits, invariance, reflection positivity and reconstruction", L68374 "A two-point witness of non-triviality"; CA-III L5 "Uniqueness up to the renormalised coupling", L75922 "O(4) invariance under an infrared decay hypothesis", L111167 "Statements used without proof in this account".
- **Y3 L** is a line of `YM3/YM3_I.tex`. That file is not in this working copy. Every Y3 line below is taken from a check file that read it (`gates/o4-check-1.md`, `gates/o4-check-2.md`, `gates/cluster-check.md`) or from `library/t0-skeleton.md`.
- **Overview** is `YM4_assembly_overview.pdf`: one page (1584 × 1728 pt), thirteen boxes and a set of arrows. I read its text and the coordinates of its boxes and arrows from the PDF content stream. Its footer says Target Theorem A "remains unproved" and that arrows record required inputs "subject to the stated open obligations". It links a 44-page `YM4O1.pdf` of 29 October 2026, which is not in this working copy and which I have not read.
- **QED3 outline** is `QED3_assembly_outline.tex` (569 lines). Its blocks are LP, MB, FB, FD, RS, RT, LF, UV, IR, FP, CL, the external RP, R, C, and the assembly AS.

**Status words.** Each statement and each submanuscript carries one of these.

- **[C] checked**: proved here and checked line by line once by the other model; the check file is named. A checked result is still an implication from its named inputs.
- **[P] proved, not checked**: proved here, not yet checked by the other model.
- **[SP] proved in a source**: the outline or complete account gives a detailed proof; we cite it and have not rebuilt it (FINISH item 9). Its line-by-line check waits for the hardening pass.
- **[SS] sketched in a source**: the source gives an outline of a proof, or names the item as an obligation.
- **[O] open**: no proof here or in a source.

**Open inputs** are written inside the statement that needs them as `⟦open: NAME⟧`. Each name is defined once, in the submanuscript that owns it.

**Shared notation** (as in SA L3784–3808 and SA (0a), L6905–6915).

- G = SU(2), N = 2, dimension 4. L > 1 is an odd integer, the block factor. The spacing is a_K = L^{−K}.
- The compatible tori are T_ℓ with ℓ = 2L^m, m ≥ m₀; M = L^{m₀}; localisation cubes at scale a_s = L^{−s} have side M a_s (SA D1, L4088–4137).
- a_p(U) = 1 − ½ Re tr U_p. Wilson's measure is μ_{K,ℓ,β}(dU) = Z^{−1} e^{−β Σ_p a_p(U)} dU, with product Haar measure dU.
- The observable is O_K(f) = Σ_p f(x(p)) a_p(U), with x(p) the plaquette barycentre (the scalar action density tr F², SA L6911–6913).
- ‖f‖_♯ = max(‖f‖_∞, c_M ‖∇f‖_∞). A separated n-tuple has real C¹ entries with pairwise disjoint compact supports, separation at least d > 0, and each support in a ball of radius R.
- 𝒢_{a,β} is the set of translation-invariant Wilson DLR states on aZ⁴ at β (SA G3, L4486–4500). "Periodic Gibbs state" means a DLR state invariant under a full-rank sublattice of translations.
- The flow is x₀ = β, x_k = x_{k−1} − b_k. A first-passage datum (K, β) is one where the run reaches the window g^{−2} < x_K ≤ g^{−2} + B_♯ for the first time at step K (SA Theorem 0(a), L6915). 𝒲_K(g) is the set of such β.
- The shape class 𝔗(d; ϑ) is that of SA 0(c)(3): Lipschitz f, h ≥ 0, each supported in a ball of radius d, d ≤ dist(supp f, supp h) ≤ 6d, ∫f ≥ ϑ‖f‖_∞ d⁴, Lip f ≤ ‖f‖_∞/(ϑ d), the same for h. K_free(f,h) = ∬ f(x)h(y)|x − y|^{−8} dx dy.
- 𝒮_{≠,n} is the Schwartz space on (R⁴)ⁿ flat on all coincidence diagonals; 𝒮_{+,n} also flat off the positive-time region; |φ|_r = max_{|α|≤r} sup_x (1+|x|²)^{r/2}|∂^α φ(x)| (SA L77–84).

**Two names called D4.** The outline's "Requirement D4" (SA L4179) is the one-point transfer between periodic states. Our "(D4)" (`library/loc-4.md` §5, `t0-skeleton.md` convergence point) is complex domain admission of every carried composition. Below, the first is **SA-D4** and the second is **(D4)**.

## 1. T0, the target

T0 is the owner's target (GOAL.md, 2026-11-03), pinned to the outline's main theorem (SA L65–130) and Theorem 0′ (SA L7017–7038), with the Wightman theory included (owner, 2026-11-03: "Include it") and with non-triviality in the sense NT1 + NT2 of GOAL.md. When the OpenAI write-up is public, T0 is re-pinned to its statement.

**Theorem T0.** Fix G = SU(2), Wilson's action and an odd block factor L large enough for the order of constants in Section 3. There is g_* > 0 such that for every reference coupling 0 < g ≤ g_* the following hold.

1. **Data and limits.** First-passage data (K, β) exist with K arbitrarily large. Let (K_j, β_j) be first-passage data with K_j → ∞, and let ν_j be periodic Wilson Gibbs states on a_{K_j}Z⁴ at β_j. From every such sequence one can extract a subsequence along which the moments of O(f) − ν_j(O(f)) converge on every separated tuple. The limit S is a *volume-first limit*: the infinite-volume state is taken at each fixed spacing first.
2. **Decomposition.** S has a canonical decomposition S = ∫ σ_ξ λ(dξ) over a compact metric space (X, λ), unique up to isomorphism. The one-point function of σ_ξ is 𝔠_ξ ∫f with 𝔠_ξ real, continuous, and ∫ 𝔠_ξ λ(dξ) = 0.
3. **The Osterwalder–Schrader axioms per component.** For every ξ ∈ X (as in SA 0′(3)), the full moment functionals G_{ξ,n}, with G_{ξ,0} = 1, satisfy:
   - **E0′, regularity and growth.** Each G_{ξ,n} extends uniquely and continuously to 𝒮_{≠,n}, and |G_{ξ,n}(φ)| ≤ A Bⁿ (n!)^p |φ|_{kn} for n ≥ 1, with A, B, p, k independent of n and ξ.
   - **E1, Euclidean invariance.** Invariance under simultaneous translations of R⁴ and every element of O(4).
   - **E2, reflection positivity.** With θ(x₁,x₂,x₃,x₄) = (x₁,x₂,x₃,−x₄) and (Θφ̄)(x₁,…,x_n) = conj φ(θx₁,…,θx_n): Σ_{m,n=0}^{N} G_{ξ,m+n}(Θφ̄_m ⊗ φ_n) ≥ 0 for all φ_n ∈ 𝒮_{+,n}.
   - **E3, symmetry and reality.** Permutation invariance, and G_{ξ,n}(φ̄) = conj G_{ξ,n}(φ).
   - **E4, clustering.** For φ ∈ 𝒮_{+,m}, ψ ∈ 𝒮_{+,n} and v ∈ R³, G_{ξ,m+n}(Θφ̄ ⊗ τ_{(v,0)}ψ) → conj G_{ξ,m}(φ) G_{ξ,n}(ψ) as |v| → ∞. Quantitatively, |σ_ξ(X·τ_vY) − σ_ξ(X)σ_ξ(Y)| ≤ C(X,Y)|v|^{−2} for |v| ≥ r(X,Y), with C, r the same for all ξ and all volume-first limits at g (SA 0′(3)(iv)).
   - **Vacuum and cone.** On the OS space ℋ(σ_ξ), ker H = CΩ, and the joint spectrum of (H, P) lies in {E ≥ |q|}.
4. **Wightman theory.** For each ξ there is a separable Hilbert space with a unique vacuum, one Hermitian scalar tempered field, a strongly continuous unitary representation of the proper orthochronous Poincaré group with spectrum in the closed forward cone, and locality, whose Schwinger functions are the G_{ξ,n} on diagonal-flat tests.
5. **Non-triviality.** NT1: for each ξ, H_{σ_ξ} ≠ 0 on Ω^⊥. NT2 (GOAL.md; working draft, owner may change): along the trajectory, gauge-invariant correlators at scale r equal their leading perturbative values in the running coupling g_r, including the three-gluon vertex part (NT2-V), and g_r → 0 at the one-loop rate; stated as `parts/witness.md` Text 8.1. In addition the connected two-point function of each σ_ξ obeys the law SA 0(c)(4) on R⁴: on 𝔗(d; ϑ) pairs of class C¹ it equals ζ² (3(N²−1)/π⁴) g(d)⁴ K_free(f,h)(1 + η) with (1 − ½)(1 − η̄)⁴ ≤ 1 + η ≤ (1 + ½)(1 + η̄)⁴.

What is not in T0: uniqueness of the limit (E3 of the outline's catalogue, SA L4226ff), the tuned and matched runs (E2–E4), the Ward route of 0(e), the four-point clause 0(c)(5), the identification with the full gauge theory (F4, SA L4416), SU(N) for N ≥ 3, and the mass gap.

## 2. Plan of the proof

The proof runs in five layers. Each layer is a group of submanuscripts with one stated interface to the next.

**Lattice structure (no renormalisation group).** At fixed spacing, every periodic Wilson DLR state has a common period, is invariant under all lattice isometries, and is reflection positive at every coordinate site, coordinate bond and diagonal mirror (LG1). No single torus is adapted to a coordinate and a diagonal mirror of one plane (Lemma S), so diagonal positivity comes through infinite-volume periodic states, and the limit is volume-first. The same lattice positivity gives the chessboard estimates used to move bounds between states, and the plateau law that decomposes states into ergodic components (PH1, lattice half).

**The hard core: one exact renormalisation-group step, iterated.** Balaban's block averaging gives coordinates (BG1). The linear estimates on a fixed regular background are the flat package and its curved, complex and layered extensions (FP1, PR1). The background itself is the regular critical orbit with prescribed averages, continued holomorphically (BG1). One step integrates a fluctuation scale: the regular part by a convergent polymer expansion with a pointed marginal extraction (NL1, OL1), the large-field part by histories that retain the Wilson factor and pay for every created region (LF1). Sources are carried as local coupling changes inside the same step (SC1). The step needs every carried composition (lifted and stage cores, stored arguments, healing gauges, logarithm charts) to lie in the complex domains where its activities are defined, with room. This is **(D4)**. The outline states it as a hypothesis and the complete account assumes Balaban's stage theorem for it (Section 9). We do not use the outline's (R5) old-chart datum for stage admission. We define stage domains intrinsically, by seven normalised bounds on the stage fields themselves, glued over all admitted real centres (ST1). The closed induction (IN1) then maps one class of presentations into itself at every level with one order of constants, and gives the flow and first passage. Its output on compatible tori is the source bound and stability statement D1 (UV1).

**From D1 to continuum Euclidean structure.** Under D1 and LG1, chessboard transfer gives one-point differences, cumulant bounds and the graded factorial bound D2 for every periodic Gibbs state (SR1). Compactness gives a volume-first limit on separated tuples, the diagonal-flat extension with factorial growth, the OS Hilbert space and the spectral cone (SR1, CL1). The phase construction gives the canonical decomposition, unique vacuum per component and |v|^{−2} clustering (PH1).

**Short distance.** The two-point law (F2), with the running normalisation (F3), gives the upper bound TU10 that rotation invariance needs, uniformly over periodic states, and gives the lower bound that non-triviality needs (TP1). The insertion bound, plate density, angular kernels, two-point harmonic elimination and all-orders closure give O(4) for each component (RO1). NT1 follows from the R⁴ two-point law by a short time-translation argument; NT2 is the witness (WT1).

**Reconstruction.** The direct scalar reconstruction of YM3_I, ported to four dimensions, gives one Wightman theory per component (WR1). The assembly AS1 checks that all clauses hold with one set of parameters and one component.

The volume-first order matches the QED3 outline ("Spatial volume tends to infinity at fixed lattice spacing; the continuum limit is taken afterwards", its title block). The position layout matches the YM4 overview. Where we differ from their YM4 assembly, Section 8 says why.

## 3. Order of choice of the constants

The master order is the outline's (SA L19469–19470), which Theorem 2.11's proof states as the order in which every condition is a floor, a ceiling or a window endpoint at its last constant (SA L19448–19468):

(r, 𝔭₀, 𝔭₁, q, κ₀, β_s, θ_s, θ_c) ≺ L ≺ (M₁, R₁) ≺ κ ≺ (κ̄, κ₁) ≺ M₁′ ≺ M₂ ≺ (Θ₁, ϖ_T) ≺ M ≺ σ_⋆ ≺ a_Λ ≺ (A₁, A₀, C₀, C₁, α₁, α₀, E₀, M₀, α′, 𝖡) ≺ (λ̲, c₅, B̄) ≺ γ ≺ (ϱ, c_a) ≺ (g, ℓ, β, K).

Our additions, in place:

- With L: the flat-package constants of FP1 (c(L), C L⁸, the kernel rate), the Hölder exponent α_H ∈ (0, ½] of the clause (H) (`library/bx-fix.md`), and the averaging Definition A (`library/assign-adopt.md`).
- After the A1 constants (row 7 of `library/c4-order.md`): the common continuation radius r_B ≤ 1/8 (`library/a1-balaban.md` L2459–2545), then the intrinsic tube radius δ ≤ min{1/40, r_B/40} (`library/intrinsic-dom.md` (5)), then the tube-distance floor η_* > 0 of ST1.
- The stage allowance β_R and phase term of SA (R22) (SA L6126–6133) come with the radius coefficients C₀, C₁; ST1's forcing ceiling C u_l < β_R/2 is a ceiling on g.
- After F2's shape class: ϑ_* = 1/12000 (SA F2, L4289ff), ϑ_W ≤ 10^{−7} for Lemma W, then d₀ and n₀ of SA 0(c)(3), then γ_W(ϑ) as a ceiling on g.
- The GEO5(c) depth d₀ = 5 + log_L C₄^GC is chosen after r and B̄, not after M (`library/c4-order.md` row 19, `gates/geo5c-gate.md`). This corrects the printed 2.8 order.

**The order is not yet acyclic.** `library/c4-order.md` [P] displays a consistent order **only** conditionally on an early uniform cost envelope C̄₀^UM. Without it the budget cycle κ̄ → M → C₀^UM → Θ → κ̄ remains. Its two ends are SA L19477 ("δ₀M ≫ κ̄ ≫ Lκ") and (UM19) at SA L14583 (log(R_s − 1) ≥ Θ, with Θ = C_h(C₀ + K_*) at (UM18), L14576). This is ⟦open: IN-order⟧ of IN1.

## 4. The submanuscripts

| Code | Title | Overview position | Their YM3 / QED3 analogue (named in the overview or the QED3 outline) | Status |
|---|---|---|---|---|
| LG1 | Lattice Gibbs states and all mirrors | L | YLO1; LP (LPM1/LPO1) | [C] |
| FP1 | The flat propagator package | M (flat part) | YPO1; MB (MBM1/MBO1) | [C] |
| PR1 | Propagators and response in a background | M | YPO1; MB, FB | real critical [C]; complex single-layer [C]; layered complex [O] |
| BG1 | Averages, gauges and constrained backgrounds | G | YBO1; replaces the fermion position (FB) | A1, 2.4 [C]; intrinsic tube [P]; layered admission [O] |
| ST1 | Intrinsic stage domains and stage admission (D4) | between G and N/H; ours | none; their stage step is Balaban CMP 122a (1.60)–(1.70), assumed in CA-I | nesting, allowance [P]; coverage, stage map, witnesses, drop-outs [O] |
| FC1 | The free curvature model | P | YGO1; replaces QED3's quartic probe (FD) | [SP] |
| OL1 | Marginal extraction and the one-loop law | E | YEO1; RN (RNM1/RNO1) | partly [C], Theorem V [P], increment clause [O] |
| NL1 | The exact local nonlinear step | N | YNO1; RS (NLM1/NLO1) | many links [C]; whole step [O] through (D4) |
| LF1 | Large-field histories | H (exactness, rarity) | YHO1; TP (TPM1/TPO1), LF | C1, GEO, floor screening, 2.4, 2.8, 2.13 parts [C]; C3 mass bound [O] |
| SC1 | Sources inside the step | R (early) | YSO1; RR (RRM1/RRO1) | finite-source freezing [SP]; profile induction [P]; whole [O] |
| IN1 | The closed induction, the flow and first passage | T, with C4 | YTO1; RT (CVM1), replaces common tuning | [O] |
| UV1 | Torus source bound and ordinary stability (D1) | R/H interface | UV | criteria [C]; D1 [O] |
| AG1 | Ages and uniform rarity of old regions | H (stability) | YHO1 | [O] |
| SR1 | All-state transfer, graded bounds and growth | R (later) | YSO1; RR, VT, IR | [C] as implication from D1 |
| CL1 | Continuum limits, Euclidean Hilbert space, cones | C | YCO1; CL (CEM1/CEO1) | [C] as implication |
| TP1 | The two-point law and TU10 | V | YVO1; replaces component cumulants (FP) | [O] |
| RO1 | O(4) covariance | Z (rotation step) | YAO1 rotation part; QED3's R (RPM1 Thm A) does not apply here | [C] as implication from D1, TU10 |
| PH1 | Phases, components and clustering | K | YKO1; EC (ECM1/ECO1), C | [C] as implication |
| WR1 | Wightman reconstruction per component | Z (assembly; their H3) | YAO1 reconstruction (Y3 Thm IV-76-59); QED3's RP | [C] as implication |
| WT1 | Non-triviality NT1, NT2 | P/V/Z | QED3's AS (κ₄ > 0) | Lemma W [P]; NT2 [O] |
| AS1 | Assembly of T0 | Z | YAO1; AS | [O] until its inputs close |

One-line statements:

- **LG1.** Every periodic SU(2) Wilson DLR state at β > 0 has the common period 2Z⁴ and is invariant and reflection positive at every coordinate site, coordinate bond and diagonal mirror.
- **FP1.** The flat constrained precision has a gap c(L)I ≤ A_k^flat ≤ CL⁸I and exponentially decaying kernels, uniformly in depth and compatible torus.
- **PR1.** At admitted regular backgrounds the gauge-fixed fluctuation Hessian is coercive and its constrained inverses and responses have weighted exponential kernels, with Hölder and Cauchy bounds on the complex domain.
- **BG1.** Every admitted regular datum has a unique regular critical orbit with prescribed averages, holomorphic in the datum, and the canonical branches glue to an intrinsic tube with no preferred centre.
- **ST1.** Stage fields lie in intrinsic seven-bound domains, and each actual stage map spends less than half the coefficient margin between consecutive stages; hence (D4).
- **FC1.** The free exact-cochain curvature kernel converges to the continuum kernel with a quantified error, and the free two-point coefficient of tr F² is positive with kernel |x − y|^{−8}.
- **OL1.** The pointed member's marginal coefficient cancels against its own counterterm, and the Gaussian increment b_j⁰ obeys the one-loop law with c₀ = 11N² log L/(12π²).
- **NL1.** Given the class at level k and (D4), the ordinary step is holomorphic on its product box with a label-independent majorant, and its output satisfies the class bounds at level k+1.
- **LF1.** Large-field moves are exact Borel operations preserving every sourced integral, histories keep their margins with an entropy bound, and each created region costs exp[−c p₀(g_j) − κ|X|_j].
- **SC1.** Each source is carried as a local coupling change with an exact sourced mass identity, inside the same step.
- **IN1.** One nonempty class 𝔆_j, with constants independent of j, contains the bare measure and is mapped into 𝔆_{j+1} by the exact step; the flow reaches first passage with increments independent of torus and finer cutoff.
- **UV1.** On compatible tori, log Z_{K,ℓ}(w) is a sum of local holomorphic source energies decaying like e^{−κ m(X)}, with normalised upper stability and an unsourced floor, uniformly in K and ℓ.
- **AG1.** Live large-field regions persisting from level j to level k have a summable tail r(k − j), uniformly in volume and test position.
- **SR1.** D1 and LG1 give state-uniform one-point differences, cumulant bounds, the graded bound [2B(R)]ⁿ(n!)^k max{1, d^{−5n}}, and the diagonal-flat extension with factorial growth.
- **CL1.** Volume-first subsequential limits exist on separated tuples, carry all lattice mirrors, and give the OS Hilbert space with H ≥ |P_j|.
- **TP1.** For every periodic Gibbs state, the connected two-point function on 𝔗(d; ϑ_*) is C_G ζ² g(d)⁴ K_free (1 + r) with |r| ≤ ½, and g(d)^{−2} ~ c_* log(1/d), ζ → 1; hence TU10.
- **RO1.** Under D1, the cone and TU10, every component's Schwinger functions are O(4) covariant on separated and diagonal-flat tests.
- **PH1.** Each limit decomposes canonically into ergodic components with unique vacuum and uniform |v|^{−2} clustering, and ker H ≅ L²(X, λ).
- **WR1.** Each component's Schwinger functions are those of a local scalar Wightman theory with Poincaré covariance, forward-cone spectrum and unique vacuum.
- **WT1.** H ≠ 0 on Ω^⊥ in each component (NT1), and the NT2 witness holds across scales.
- **AS1.** The clauses of T0 hold together at one g, along one sequence, for every component.

## 5. The submanuscripts in full

Each entry has: (a) main theorem, (b) imports, (c) sources, (d) status and open inputs.

### LG1. Lattice Gibbs states and all mirrors

**(a) Theorem LG1.** Fix d = 4, G = SU(2), L odd, a > 0 and β > 0.

1. *Finite cutoff.* μ_{K,ℓ,β} is a probability measure; O(f)∘𝗋^* = O(𝗋f) for every lattice isometry 𝗋 (barycentres), and O(f) stays on the side of a bond-bisecting mirror where f is (SA (0a), L6908–6913).
2. *DLR.* Periodic limits of torus measures are DLR states; 𝒢_{a,β} is a nonempty compact convex set; the finite-bond conditional kernels preserve continuous local functions (SA L4486–4500).
3. *Torus positivity.* On a cubic torus with an even number of sites per axis, μ_{K,ℓ,β} is reflection positive at every coordinate site plane and link plane (Osterwalder–Seiler). The one-direction and four-direction chessboard estimates hold (SA (ST1)–(ST4), (AM5)–(AM7)).
4. *Common period (rank 11).* Every periodic Wilson DLR state is invariant under link reflections and under translations by 2aZ⁴ (temporal gauge and two-layer determination; Y3 Lemmas IV-54-9, IV-54-13, Prop IV-54-16 ported).
5. *All mirrors (rank 12, AM1).* Every periodic Wilson DLR state is invariant and reflection positive at every coordinate site, coordinate bond and diagonal lattice mirror, on the full bounded Borel half-space bond algebra; compositions give all unit translations and the signed permutation group W₄ (lower tangent, folding, Jensen on adapted split tori, positive crossing kernels; Y3 Props IV-29-40, IV-54-17).
6. *Lemma S.* No period lattice Γ ⊂ Z⁴ is adapted to both m = e₄ and n = e₁ − e₄.

**(b) Imports.** None. This submanuscript reads no renormalisation-group statement.

**(c) Sources.** SA L229–605 (finite-cutoff foundations), L2084–2698 (periodic Gibbs states, link reflections), L2698–3195 (all mirrors; positive crossing kernels on split tori L2773; chessboard L2885; lower tangent L2944; folding L2993); SA G1 (L4429–4440) states these as proved. Y3 L73340–73800, L78336–78808, L78850–79037 (as read in `gates/o4-check-1.md`). Their YM3 analogue YLO1 and QED3 LP. Ours: `library/am1-port.md`, `library/t0-skeleton.md` Lemma S, `parts/upper-chain.md` Lemma 1.1 (coordinate case), `library/d2-d4.md` §2 (chessboard).

**(d) Status: [C].** `gates/o4-check-1.md` §1 (am1-port, all eight sections, first failing step none; one wording omission: the cube size r in (9) is not chosen). Lemma S checked by Codex (FINISH row 161). Chessboard steps checked in `gates/bridge-check.md` §1. No open input.

### FP1. The flat propagator package

**(a) Theorem FP1** (Balaban's flat package F0–F5). Fix L odd. For the unweighted classical flat precision A_k^flat with the plain constraint and the soft internal-contour gauge, uniformly in the number k of previous blocking steps and in compatible tori, including real flat holonomies:

1. c(L) I ≤ A_k^flat ≤ C L⁸ I, and ‖da‖² ≤ E_k(a) ≤ 256‖da‖² (curl-energy comparison).
2. The flat precision, its constrained covariance and their first and Hölder differences have kernels bounded by C e^{−c dist(x,y)} in scale units; periodisation and unitary flat holonomies preserve the bounds.
3. The level-0 seam holds; the lattice Uhlenbeck gauge (Lemma U) and the quadratic estimate (LC) hold.
4. The mesh-uniform scalar block estimate and its Dirichlet compressions hold.

**(b) Imports.** None.

**(c) Sources.** SA L605–1150 (block normalisation, uniform scalar gap), L8396–8776 (flat gap), L8776–9060 (flat action upper bound), L9060–9583 (flat exponential kernels); SA A2 and A3 (L3835–3897) record that these sections prove the flat case. Balaban CMP 89 (1983), CMP 95 (1984) 17–40, CMP 96 (1984) 223–250. Dimock II Theorem 2.2; Dimock QED_3 (arXiv 1712.10029, Section 3). Ours: `library/flat-port.md`, `library/lattice-uhlenbeck.md`, `library/seam-quadratic-c.md`, `library/fan-ext.md`, `library/fd-local.md`.

**(d) Status: [C].** `gates/flat-port-gate.md`; Lemma U and (LC) in `gates/share-check-199fac1cb.md` (with a seed repair); flat one-jump and several-jump chain in checks 73b09692a and 00f9df685 (FINISH, "State of our route").

### PR1. Propagators and response in a background field

**(a) Theorem PR1.** Fix the constants of FP1 and of BG1(2). Let (U, A′, 𝐉) be a regular pair in the admitted core: a regular background U, a complex fluctuation-side datum A′ and an independent current 𝐉 (SA L5665–5670), with the Hölder clause (H) of `library/bx-fix.md` §2.2 (Hölder-continuous first differences of real and complex potentials at the pair's own scale, in the real gauge of (R4); exponent α_H ∈ (0, ½]). Then, with constants independent of depth, volume and position:

1. *(A2) Coercivity.* With Q the derivative of the block average and 𝓔 the gauge-fixed fluctuation Hessian, Re⟨B, 𝓔B⟩ ≥ c‖B‖² on QB = 0, on each conditioning set with its boundary conditions, and with c/2 on the complex neighbourhood; residual gauge directions, torus holonomies and node constraints are removed or treated separately (SA A2, L3835–3863).
2. *(A3) Inverse and response.* The inverses and response operators actually used, including conditional covariances and derivatives of U(V), have kernels ≤ C e^{−c d(x,y)} in the weighted path distance with the stated first and Hölder differences, on the full complex datum polydisc (the product bond-log domain (PW1) with the scale-weighted bounds (PW2)–(PW3)); holomorphic derivatives in decoupling parameters obey Cauchy bounds on a fixed enlarged disc (SA A3, L3864–3897).
3. *Profile.* At a real critical regular background, η^{−2} l(x)²|∂U − 1| and l(x)³|J(U)| are ≤ C P_σ(x) (SA L9681).
4. *(PW6) at complete fields.* On U^H, the window datum satisfies (PW6) on the whole ν-disc and fine-parameter polydisc (bx-fix Lemma 2), and (BX′) holds.
5. *Layered complex comparison* ⟦open: PR-lay⟧. On the full earlier-parameter and switch domains, along the stage path supplied by ST1, dist_∞(D_e(t), 𝒯_e^c) ≥ η_* and ‖∂_t F_a‖ ≤ C r_a^{lift} Σ_{l∈E_n} u_l √(1+|m−l|) e^{−D|m−l|}, D ≥ log 4 (`library/layered-a3.md` (1)). Its first missing piece is the uniform real target-datum admission and complex bound (8) of layered-a3 for the actual layered stage family.
6. *Counterterm accounting and profile inputs of A2* ⟦open: PR-H⟧: (H-ct) (SA L7864) and (H-prof).

**(b) Imports.** FP1; BG1(2), BG1(3).

**(c) Sources.** SA L9583–10103 (constrained backgrounds), L10103–12889 (constrained propagators, local decay, layered row maps, field-row Gram bounds), L13426–13894 (PW6 at L13560–13567). SA A3 itself says the non-Abelian background and multiscale response estimates "remain to be proved" (SA L3864–3897). Balaban CMP 99 (1985) 389–434, CMP 102 (1985) 277–309, CMP 109 (1987) 249–301 ((3.31) is the Hölder clause). Ours: `library/a2-curved.md`, `a2-layers.md`, `a2-full.md`, `h-walk.md`, `h-walk-fix.md`, `a3-profile.md`, `a3-derivative.md`, `p82-curved.md`, `a3-close.md`, `meet-6c.md`, `a3-clauses.md`, `dec-field.md`, `pw-bridge.md`, `nl-r9.md`, `bx.md`, `bx-fix.md`, `layered-a3.md`, `regional-gauss.md`.

**(d) Status.** Real-critical A3 chain [C] (gates of the same names; `gates/a3-balaban-reads-gate.md`). A2 [C] on separated layers with independent currents (`gates/a2-curved-gate.md`, `a2-layers-gate.md`, `a2-full-gate.md`, `h-walk-gate.md`, `h-walk-fix-gate.md`). (PW6) on U^H and Theorem BX′: bx-fix by Claude, checked by Codex in `gates/bx-fix-check.md`. Regional matrices and gaps on ℛ₄ [C] (`gates/regional-gauss-check.md`). PR-lay [O]: `layered-a3.md` (Codex, round 1 not checked; rounds 2–4 running) proves that the lifts do not absorb the reversed scale loss (its (3): L^{2v}/L_♭^{2v} > 4^v) and that profile decay pays fixed losses under (5). PR-H [O].

### BG1. Averages, gauges and constrained backgrounds

**(a) Theorem BG1.** Fix L and the constants of rows 1–7 of `library/c4-order.md`.

1. *Averages and charts.* The block average of Definition A (`library/assign-adopt.md`) has the pivot chart of SA L7931–8396 (pivot derivative, exact straightening, coarea and determinant factors) at regular configurations.
2. *(A1) The constrained critical orbit.* For every allowed nested family of small-field regions on separated sequences and every regular coarse datum V in the admitted real class ℛ_e of a determining set e, there is a regular critical orbit [U(V)] of the Wilson action with the prescribed block averages, unique among regular critical orbits in a stated larger neighbourhood. Its axial representative is Borel in all real data and holomorphic on ‖B‖_∞ < r_B, with r_B and all constants independent of depth and volume, and compatible with restriction, seams and change of torus (Balaban CMP 102 Theorem 1; SA A1, L3811–3834). Uniqueness is of orbits: a field is not unique without a gauge condition (`library/intrinsic-dom.md` §2, the pure-gauge family U_t).
3. *Prepared boxes (Proposition 2.4 = Balaban CMP 122a Proposition 1).* The prepared-box minimiser has a unique regular orbit, analytic in exterior data, with a uniform freed-average Hessian gap; the joint reference chart has a uniform real slice.
4. *Intrinsic datum tube.* With δ ≤ min{1/40, r_B/40} and 𝒯_e = ∪_{V∈ℛ_e} {e^{iB}V : ‖B‖_∞ < δ}, the map T_e(D) = Φ_V(i^{−1} Log(DV^{−1})) is well defined and holomorphic on 𝒯_e, solves the constrained critical equations, agrees with the (R5) continuation wherever both are defined with the common-radius choices, and satisfies T_e(D^v) = T_e(D)^{ṽ} for real node gauges v (`intrinsic-dom.md` (5)–(6) and §3). δ depends on no centre, depth or volume when r_B does not.
5. *Single-level field domain.* Under `library/a3-close.md` L74–87's single-level hypotheses, ‖i^{−1}Log[M_e(e^{iη_p w}U) M_e(U)^{−1}]‖_∞ ≤ 2L^{d−p}‖w‖_∞, so ‖w‖_∞ < min{c_T, δ/2}L^{p−d} puts the datum in 𝒯_e uniformly in depth (`intrinsic-dom.md` (7)).
6. *Background package (OA5)–(OA7)* for the admitted fixed-sequence substitutions, with tower response decay (`library/oa7.md` (5)–(7)).
7. *Layered target-datum admission* ⟦open: BG-lay⟧ = ⟦open: ST-cov⟧ of ST1 restricted to backgrounds: for the actual layered stage family, every inherited determining set has M_e(U) ∈ ℛ_e with its real-regularity margin and M_e(𝐔) ∈ 𝒯_e with distance η_* to the complement.

**(b) Imports.** FP1; PR1(1)–(3) for (2)–(3) (the A1 proof reads A2, A3 at the real critical reference).

**(c) Sources.** SA L7043–7931 (block averages and gauge fixing), L7931–8396 (pivot chart), L9583–10103 ((1b) the background field: statements L9658, multiplier contraction L9832–9911, tower existence L9746–9755, restriction identity L9776–9780); SA L5696–5727 ((R5) continuation domain). CA-I L46053–46081, L47850–47984 (operator identities; conditional). Balaban CMP 98 (averaging), CMP 99, CMP 102 (277–309), CMP 122a Proposition 1. Ours: `library/a1-balaban.md`, `a1-orbit.md`, `ref-chart.md`, `assign-adopt.md`, `intrinsic-dom.md`, `oa7.md`, `a3-close.md`.

**(d) Status.** (2) [C] as an implication on separated sequences (`gates/a1-balaban-gate.md`); (3) [C] (`gates/ref-chart-gate.md`, `gates/ref-chart-regate.md`); (1) Definition A [C] (`gates/a2-full-gate.md`); (4)–(5) [P] (Codex, not checked); (6) [P] (Codex, not checked; it is a correction of an inference, not of SA's (OA7)); (7) [O].

### ST1. Intrinsic stage domains and stage admission (D4)

This submanuscript is our design. It replaces the outline's stage admission through the (R5) old-chart datum, which stopped ten lanes (rows 240–262; `library/stage-thm.md` first open input: the returned datum must lie in every old (R5) continuation ball on the full complex source).

**Definitions.** A *stage record* of level s keeps the geometric data of `library/stage-thm.md` L58–63: levels, regions, both erosion rules, truncations and preceding structures. It discards each record's old real reference and old (R5) ball. For a tower e = (Z, p, d) put T_e = T_e(M_e(𝐔)) on the open set where every required M_e(𝐔) ∈ 𝒯_e and M_e(U) ∈ ℛ_e. The *intrinsic domain* D_n^int is the set of pairs P = (U, A′, 𝐉) (with their stored data) satisfying, for every record and tower,

q_a(P) < c_n(m) r_a^{lift}, for the seven normalised readouts: η_s^{−2}|∂𝐔 − 1|, L^{s−p}η_p^{−2}|∂T_e − 1|, |𝐉|, L^{s−p}L^{2(p−d)}|J(T_e)|, η_s^{−2}|∂U − 1|, |A′|, |∇_U A′|,

with the lift outside the bracket (CA-I L49595–49624), read on the prescribed erosion and also with 𝐔 = U (SA L5707–5720), one real splitting for all records, 𝐉 independent of J(𝐔); together with the real gauge witnesses U^u = e^{iηA}, ℓ_i|A|, ℓ_i²|∇^ηA| < 𝖫₀^{2e(Q)} B M α_{0,i} on Q ∩ X for the four cube families of CA-I L48527–48565 (`intrinsic-dom.md` (8)–(9)). There is no old-chart test.

**(a) Theorem ST1.** Fix L, the constants through the radius coefficients of Section 3, a finite admissible history, and n.

1. *Nesting.* For the same field, c_{n+1}(m) ≤ c_n(m) gives D_{n+1}^int ⊂ D_n^int.
2. *Allowance.* With fixed lifts and distinct marks, d_n(m) = c_n(m) − c_{n+1}(m) = g_k(m)/(2𝖭) + β_R Σ_{l∈E_n} 2^{−|m−l|}, and Σ_n d_n(m) ≤ g_k(m)/2 + 3β_R.
3. *Coverage* ⟦open: ST-cov⟧. Every lifted, layered stage field required by NL1, LF1 and SC1 lies in an open set where (8) is defined: for every inherited determining set e, M_e(U) ∈ ℛ_e with its margin and dist_∞(M_e(𝐔), 𝒯_e^c) ≥ η_*, uniformly on the full earlier-parameter domain and the interpolation discs (SA (R11), L5813–5826: |ν| < ϱ_F, ϱ_F > 1).
4. *The stage map* ⟦open: ST-map⟧. For every stage, starting at 0 → 1, the actual stage map S_n(·; ζ) (ζ = earlier parameters, fluctuations, returns, switches) is realised on each previous read by a compatible fixed-system path X_t from P to the prescribed returned pair S_n(P; ζ), including the assigned independent current, whose complete forcing (f, b) of the saddle system (`library/stage-resp.md` (2)) is bounded in the weighted A3 norms, with support and shell distance such that ‖(d/dt)F_a(X_t)‖ ≤ C r_a u_l √(1+|m−l|) e^{−D|m−l|}, D ≥ log 4, sup_l C u_l < β_R/2, uniformly in P, ζ, t, a (`stage-resp.md` (4)). The first missing construction is the matched stage reconstruction: identify the actual (A_j, B_j) collar datum and returned pair on the full parameter domain (`library/shift-map.md` §4; CA-I L54287 gives only the instruction "Express U_k^{(n)} through the new background ...").
5. *No new mark.* For reads with no new mark, the readout change stays below the phase allowance g_k(m) r_a/(4𝖭) ⟦open: ST-phase⟧ (`stage-resp.md` §4).
6. *Witnesses and stored slots* ⟦open: ST-wit⟧. After returns, the real gauge witnesses (9) hold with new witnesses or a restriction argument, and stored slots are admitted; the complex return factors ‖g‖‖g^{−1}‖ are controlled (`intrinsic-dom.md` §5; SA L5729–5736).
7. *Drop-outs* ⟦open: ST-drop⟧. On a component where integrations stop, the boundary terms are carried with unchanged mass along route (c) of `library/d4-route.md`, with the saved-argument construction of `library/dropout-bt.md` (6) admitted at later steps.

**Conclusion.** Under 3–7, for every n and ζ: q_a(S_n(P; ζ)) < c_n(m) r_a^{lift} − d_n(m) r_a^{lift}/2 for P ∈ D_{n+1}^int (half the margin left; `intrinsic-dom.md` (11)–(12), `stage-resp.md` (5)); so S_n(D_{n+1}^int; ζ) ⊂ D_n^int, and by composition with full quantifiers every carried composition (lifted and stage cores, stored arguments, healing gauges, logarithm charts) lies in its activity domain with room. This is **(D4)**. On admitted domains the Boolean bracket bound (2M_f/ϱ_F)(R_s − 1)^{−|𝒦|} holds (`intrinsic-dom.md` (13) = SA L5849–5861).

*Activities on the new domains.* Agreement with (R5) preserves existing values but does not extend activity domains ((3/2 − z)^{−1} is bounded on |z| < 1 and has a pole in |z| < 2; `intrinsic-dom.md` §6). NL1 and LF1 must construct their activities on D^int and reproduce their bounds there; ST1 supplies only the domains and the admission.

**(b) Imports.** BG1(2)–(5) (the tube), PR1(2), PR1(5) (weighted response along the path), the stage geometry of LF1(2) (C2), and the coefficient (R22) of SA L6126–6158.

**(c) Sources.** SA L5523–6453 (objects carried; (R5) L5696–5727; (R10)–(R11) L5810–5826; (R22) and inclusion hypotheses L6126–6158: "analytic inclusion hypotheses"); SA L17251–17650 (stages; L17564 "both written in the new variables"; L17618–17624); SA B4 text L4036–4037. CA-I L42670–56650 (items 4.12–4.19, indexed in `library/sa-index/ca-4.12-4.19/`), in particular L45004–45013, L49495–49546 (Remark 4.14 supply scope), L53806–53814, L54247–54287, L54986–54994 (Theorem 4.18 assumes "the stage theorem" of Balaban CMP 122a (1.60)–(1.70)). CA-III L111385–111395 lists "cube families under a stage move", "the arrest theorem" and "newborn terms, space inclusions and continuation of stored domains" as stated with proof incomplete. Balaban CMP 122a (175–202), CMP 122b (355–392). Ours: `library/intrinsic-dom.md`, `stage-thm.md`, `stage-resp.md`, `shift-map.md`, `layered-a3.md`, `collar-block.md`, `d4-stage.md`, `d4-budget.md`, `d4-incr.md`, `d4-chart.md`, `d4-route.md`, `dropout-bt.md`, `stage-tangent.md`, `wf-c-stage.md`, `loc-4.md` §5, `wf-c.md` Lemma C (single-layer collar comparison).

**(d) Status.** (1), (2) and the numerical inclusion (12) [P] (Codex, not checked). (3)–(7) [O]. No counterexample to any actual stage is claimed in any note. Corrections that bound the route: the collar block route needs the actual field estimate (`collar-block.md`); WF-c's common-ball extension does not give stage admission, and physical-current replacement fails (`wf-c-stage.md` §4); one-response increments must pass through the earlier composition (`d4-incr.md`); the datum-only reduction drops changed rows, coefficient derivatives, the multiplier anchor and the gauge tangent (`stage-tangent.md`). Shift-map and layered-a3 rounds 2–4 are running.

### FC1. The free curvature model

**(a) Theorem FC1** (SA F1, L4252–4288). Let a = ℓ/n. For the standard Gaussian on ran d₁ (covariance P_ex), the physical curvature kernel K_{a,ℓ;P,Q}(p,q) = a^{−4}P_ex(p_P, q_Q) satisfies |K_{a,ℓ;P,Q}(p,q) − K_{P,Q}(x(p) − x(q))| ≤ C r^{−4}[(a/r)^{1/2} + (r/ℓ)⁴] for a ≤ r/10, r ≤ ℓ/10, r = |x(p) − x(q)|, uniformly in a, ℓ, positions and orientations. Separated smearing converges, and the quadratic-density coefficient is positive with kernel |x − y|^{−8}: the free two-point function of the curvature density is (3(N²−1)/π⁴) g⁴ K_free(f,h) at leading order, with 0 ≤ K_free(f,h) ≤ v₄²‖f‖_∞‖h‖_∞ for pairs in radius-d balls at distance ≥ d.

**(b) Imports.** None.

**(c) Sources.** SA L1379–1670 (free curvature model, exact calculation), L1670–2084 (uniform comparison for the free lattice curvature). Their YM3 analogue YGO1. Ours: `library/nt2-free-value-by-hand.md` is a different free computation.

**(d) Status: [SP].** The catalogue records F1 as proved (SA L4252: "The exact continuum coefficient is proved"). Not rebuilt here; its check waits for the hardening pass.

### OL1. Marginal extraction and the one-loop law

**(a) Theorem OL1.** Fix L and c₀ = 11N² log L/(12π²).

1. *(B2) Pointed extraction.* For an actual regular member with no stored colour spectators, with pointed totals converging normally, locally gauge invariant and covariant under unit translations and W₄, the coefficient is defined by (ph:extractor) and cancelled by the member's own midpoint tent action; |b(E)| + ‖T[E]‖ ≤ C a^{−2}‖E‖ on physical radius a; with σ = L^{−(n−j)}, ρ = max(1, a_out/a), 0 < α_H ≤ 1, the near-domain sum at one base point after vacuum and own-counterterm subtraction is ≤ C‖E‖[ρ²σ^{4+α_H} + ρ³σ⁶ + (1 + ρ²σ⁴)e^{−c/σ}] (SA B2, L3937–3985). Input: PR1 on the complex datum domain and the core inclusions of ST1.
2. *Exact substitution.* At the trivial background and every fixed depth, background substitution preserves the bulk coefficient exactly: b[Ψ_{k−1}∘p_k] = b[Ψ_{k−1}] (`prefactor-loc.md` Theorem S, Corollary T). So b_k⁰ = A_k − A_{k−1} with A_k = b[Ψ_k].
3. *One-loop value.* |b[Ψ_k] − k c₀| ≤ c₂(L) (`b-value.md` Theorem V), hence the first clause of RF10 (SA L20356).
4. *(B3) Increment law* ⟦open: OL-incr⟧. b_j⁰ is independent of β and |b_j⁰ − c₀| ≤ C L^{−σj}, or a stated summable substitute; `rf10-incr.md` shows (3) alone does not give it (A_k = kc₀ + a((−1)^k − 1) satisfies (3) with |b_{k+1}⁰ − b_k⁰| = 4|a|), and that the averaged gauge factor's lower bound excludes every α > ½ in the norm of row 185.
5. *Nonlinear errors* ⟦open: OL-nl⟧ (supplied by IN1). b_j = b_j⁰ + f_j + q_j with |f_j| ≤ C x_{j−1}^{−1/2}(log x_{j−1})^p and |q_j| ≤ C x_{j−1}^{−(κ₀−4)/2}, κ₀ > 4.

**(b) Imports.** FP1, PR1, BG1, FC1 (free comparison), ST1 (core inclusions for (1)).

**(c) Sources.** SA L6453–6829 (radius of quadratic extraction), L12889–13426 (pointed Hessian and own counterterm), L13426–13894 (nonlinear remainder in a pointed window), L20144–21454 (running coupling; RF10 L20356; one-loop reduction L21064). Balaban CMP 109, CMP 119 (243–285). Ours: `library/prefactor.md`, `prefactor-loc.md`, `b-value.md`, `rf10-incr.md`, `b2-extract.md`, Theorem P1 (`gates/p1-gate-2f2ec0f89.md`).

**(d) Status.** `prefactor.md` [C] (Claude, row 158); (2) [C] (Codex, row 166); (3) [P]; `b2-extract.md` Theorem P and Lemma R [C] (Codex, row 202); (1) in full [SS] (SA states the implication under hypotheses it says must be proved, L3976–3985); (4) [O]; (5) [O].

### NL1. The exact local nonlinear step

**(a) Theorem NL1** (one ordinary step). Assume the presentation at level k lies in the class 𝔆_k of IN1 with the constants of Section 3, (D4) from ST1, PR1, BG1 and OL1(1). Then:

1. *(B1) Polymer majorant.* With polymers finite connected sets of scale cubes and a specified size a(X), Σ_{Y≁X} |z(Y)| e^{a(Y)} ≤ a(X) with strict room for complex sources and decoupling parameters, for the actual complex interacting matrices and all allowed cores; the connected-cluster logarithm converges absolutely with termwise differentiation and a majorant for each derivative; the finite-volume identity is exact (SA B1, L3910–3936; abstract part SA L1150–1379).
2. *(WF) Substitution room.* Every nested substitution of the window stays in its hereditary pair core (WF room, (O1), inner Landau admission, same-depth removed-map comparison, R9 bounds [PW], [NL]), the removed factor e^{−cM/σ_j} holds (WF7: box first, Rule W, (LD)), and 6(c) holds at complex data with (10.2) pointed-core admission (WF-c).
3. *(B4) The ordinary step.* The step is holomorphic on the ordinary product box (a separate Euclidean regular member at each base point, its own scalar counterterm, a variable Wilson weight, scale-small noncovariant defects) with a majorant independent of the number of labels; the small-field one-step map 1.6 is holomorphic with the radius ratios of SA L7569 (SA B4, L4006–4038).
4. *(LOC) Localisation.* Every occurrence of (R10) has its triple in the core of F for |ν| < ϱ_F, ϱ_F > 1 (SA (R11)), with separate inner and removed radii; Boolean corners obey (13) of ST1.
5. *(R-cov) Covariance.* The kept forms built from A^rel, the elimination factors and the recorded returns are covariant (`kept-cov.md` (4), (8), (13)), with the clause of Defect 1 of `gates/kept-cov-check.md` (Δ^loc_k and the rejected chains carried as A^rel pair functions) and the native action h_f named as an input (Defect 2).
6. *(R-inv) Zero defect budget.* For the invariant regular specialisation, including constant scalar sources, every (INS) defect has zero total (`r-inv.md`).
7. *Nonconstant sources.* The source-profile induction holds under the inherited ordinary formation inputs (`src-array.md`).

Open inputs: ⟦open: D4⟧ = ST1; ⟦open: NL-ER7⟧ the estimate (ER8u) = (ER7) (`bx-fix.md` "Still open on (19)", item 1); [T4]'s premises P81, P82°, M1 reduced to the flat package at U₀ = 1 (same list, item 3); the evaluation points of large-field consumers against (H) (item 6); (UR), (YA) are cited (item 5).

**(b) Imports.** IN1 (inductive hypothesis 𝔆_k), ST1, PR1, BG1, OL1, LF1(2) (geometry), SC1.

**(c) Sources.** SA L1150–1379, L4856–5127 (weighted analytic domains, scale forgetting), L5127–5523 (single-zone reserve test), L13894–17251 (localised complex Gaussian functional, unmarked majorant, source insertion, renewed pointing, windows, first-source bootstrap, old-activity Hessian; WF15 at L16327–16328). SA B4 text: "Actual nonlinear background/core inclusions and history formation remain to be verified" (SA L4036–4037). CA-I chapter from L3531. Balaban CMP 109, CMP 116, CMP 119. Dimock I–III. Ours: `library/wf-room-2.md`, `o1-decoupled.md`, `removed-fix.md`, `pw-bridge.md`, `nl-r9.md`, `dec-field.md`, `wf7-bf.md`, `wf-c.md`, `ld-decoupled.md`, `cond-c.md`, `b4-step.md`, `um1-fix.md`, `b4-induction.md`, `ti-cov.md`, `ti-2.md`, `bx-fix.md`, `gamma-bx.md`, `ur-ya.md`, `ur-gauge.md`, `loc.md`, `loc-4.md`, `kept-cov.md`, `r-inv.md`, `src-array.md`, `red.md`, `carrier-adopt.md`.

**(d) Status.** (2) [C] as an implication end to end (FINISH "Where it stands"; gates `wf-room-2-gate`, `o1-decoupled-gate`, `removed-fix-gate`, `pw-bridge-gate`, `wf7-extension-gate`, `wf-c` checked by Codex ADVANCE row 177). (3) one-level implication [C] (rows 210–222; `gates/b4-ind-check.md` found defect D1 at its line 217, closed for constant sources by (6)); (5) [C] (`gates/kept-cov-check.md`); (6) [C] (`gates/r-inv-check.md`); (4): loc-4 Sections 3–7 [C] (`gates/loc-4-check.md`), Lemmas M and W hold with (D4); (7) [P] (Codex, not checked); (1) for the actual gas [SS] (SA B1 says the primitive hypotheses must still be verified for the actual complex interacting matrices); `b4-step.md` §10 [P]. NL1 as a whole [O] through (D4).

### LF1. Large-field histories

**(a) Theorem LF1.** Fix the constants of Section 3.

1. *(C1) Exact operations.* Every move is a specified Borel kernel, change of variables or partition of unity on an explicit space; tests are total; every stored variable is integrated or retained exactly once; for every bounded gauge-invariant F the sourced construction preserves ∫F e^{−βA}; for real inputs every probability weight is nonnegative (SA C1, L4041–4051).
2. *(C2) Margins and determination.* Histories are constructive; at level j, tests, backgrounds and retained terms depend on a stated enlargement of the determining regions, inside the next margin; healing, restriction, joining and continuation preserve this; nothing wraps an admissible torus; the number of histories of given size has an entropy bound with the size function of (3) (SA C2, L4052–4062).
3. *(C3) Rarity* ⟦open: LF-mass⟧. Each created component X at level j has mass 𝔐_j(X) ≤ exp[−c p₀(g_j) − κ|X|_j], p₀(g) = (log g^{−2})^p, κ above the entropy rate of (2), with the supremum over external complex data inside the internal integral, including the Wilson factor, stored Jacobians, gauge factors and insertion weights; failure of existence of a background is covered; drop-outs without their own Wilson factor are bounded after attachment (SA C3, L4063–4074).
4. *Prepared actions (2.8).* Prepared, reference and healed actions cancel to a paid core, a positive quadratic form and a remainder ≤ C g_k^{1/2} (SA L17598, L17854); open there: I1 and the Gaussian comparison of 2.8-T^C ⟦open: LF-2.8⟧.
5. *Healed deletion (2.10).* Healed deletion and restriction factor exactly on the actual read and support sets, and the connected sum has local activity bounds ⟦open: LF-2.10⟧ beyond the conditional repairs.
6. *Loaded labels (2.13).* Loaded labels and history masses sum to the normalised extensive bound with creation payments kept; feeds OSF16 (SA L19782) and UV1 ⟦open: LF-2.13⟧ for the remaining items (rigidity on every compatible fibre; (8.1) for the literal operations).
7. *Floor screening (Theorem R)* and the prepared-box input (D-F).

**(b) Imports.** BG1(2)–(3), PR1, ST1 (stage cores and drop-outs), NL1 (activities), IN1 (inductive hypothesis).

**(c) Sources.** SA L17251–19529 (large-field histories and the induction; (2a)–(2b) L17315–17497; 2.4 L17656; 2.5–2.7 L17676–17794; 2.10 L17451, L18877; 2.13 L17820, L18944–19406), SA L5127–5523. CA-I chapter from L3531. CA-III L111215, L111223 and L111393 list, among others, "positivity dichotomy of the large-field operations", "geometry and counting of live large-field regions" and "the arrest theorem" as outstanding. Balaban CMP 122a, 122b. Dimock II (nested decreasing regions; no R operation, II Remark 3 after Theorem 3.1). Ours: `library/c1-repr.md`, `geo-prop23.md`, `geo-2.md`–`geo-5.md`, `geo5c-count.md`, `floor-screen.md`, `ref-chart.md`, `sa-2.8-terms.md`, `sa-2.13.md`, `sa-2.13-2.md`, `pre-213.md`, `inn-213.md`, `inn-fix.md`, `carrier-adopt.md`, `inv-root.md`, `um-envelope.md`, `s210.md`, `s210-fix.md`, `sa-histories.md`.

**(d) Status.** (1) [C] for the measure operations (`c1-repr.md`, checked by Claude, ADVANCE). (2) GEO1–GEO6, EXT, W3 [C] under three supplied rules (`gates/geo-gate.md`, `gates/geo5c-gate.md`); rest of C2 [O]. (7) [C] (`gates/floor-screen-gate.md`, `support-envelope-gate.md`, `support-physical-gate.md`). (4) [C] conditional (`gates/sa-2.8-terms-gate.md`). (6): (Pre) Theorem P [C], (Inn) under Definition R [C] (`gates/inn-fix-check.md`), joint chart [C], (4.1) via the inverse-root carrier [C] (`gates/carrier-check.md`, with the replacement Definition D). (5): `s210-fix.md` Lemma G [C], repairs pass conditionally (row 211); `gates/s210-3-check.md` found Definitions 3.1–3.2 WRONG, repaired in row 203. (3) [O].

### SC1. Sources inside the step

**(a) Theorem SC1.** Fix the real choices of the run independently of the source. For sources w in the ordinary source ball, including the global mirror-periodised Lipschitz profiles used by the chessboard (SA D1, L4088–4100), each source is transported as a local coupling change, the exact sourced mass identity is retained, and the step of NL1 is holomorphic in the source on that ball; the source-profile induction holds; the constant-source slopes of the flow are as in SA (3c).

**(b) Imports.** NL1, LF1(1), IN1, ST1 (source discs are among the interpolation discs of ST1(3)).

**(c) Sources.** SA L19529–19813 (ordinary source formation and volume bounds), L22345–23385 (sources, local energies; running-shift identity L22351; (4a) L22562); finite-source freezing SA L22950–23150 (classified by `src-array.md` as proved under the inherited formation inputs). Overview R box ("Early: source variations"). Ours: `library/src-array.md`.

**(d) Status.** Finite-source freezing [SP] (conditional on its inputs); source-profile induction [P]; SC1 as a whole [O] through NL1 and IN1.

### IN1. The closed induction, the flow and first passage

**(a) Theorem IN1.** With the order of Section 3:

1. *(C4) Invariant class.* There is one nonempty class 𝔆_j of complete presentations, with the same constants at every level, containing the bare measure x₀ = β with |β − θ₀| ≤ 𝗍₀ ≤ c θ₀(log θ₀)^{−C}; under the increment and tube conditions the exact step maps 𝔆_j into 𝔆_{j+1}; the conclusions include NL1's analytic polymer bounds, LF1(1)–(3), boundary bounds, covariance and the stability floor (SA C4, L4075–4087; Theorem 2.11, L19435–19446).
2. *Order.* All constants admit one simultaneous order of choice ⟦open: IN-order⟧ (Section 3).
3. *(E1) Flow.* x_j = β − Σ_{i≤j} b_i is defined up to first passage, b_i ≤ B_♯, λ(j − i) − C ≤ x_i − x_j ≤ B_♯(j − i) with λ > 0, and the increments are independent of the admissible torus and of the unused finer cutoff (SA E1, L4197–4206).
4. *First passage* (SA 0(a), L6915). Each run from β ≥ g^{−2} + B_♯ reaches first passage; c(β − g^{−2}) − C ≤ K(β,g) ≤ C(β − g^{−2}) + C; g^{−2} < x_K ≤ g^{−2} + B_♯; 𝒲_K(g) ≠ ∅ for infinitely many K; β/log(1/a_K) → 11N²/(12π²) uniformly on 𝒲_K(g).

Open inputs: ⟦open: IN-C4⟧ the closure itself, which needs NL1 and LF1(3) at every level; ⟦open: IN-order⟧; OL1(4)–(5) for (3).

**(b) Imports.** NL1, LF1, OL1, SC1, ST1.

**(c) Sources.** SA L19435–19528 (Theorem 2.11, why the induction closes, order L19469–19470), L19813–20144 (first passage and the arithmetic of a marginal flow), L20144–22345 (running coupling; 3.1 L20719; 3.4 L21456; 3.8 L22042). CA-I chapter from L3531. CA-III L111241 lists Lemma 7.3 "non-convergence of the first-passage offsets" as outstanding; I have not read where the complete account uses it, so whether T0's path reads it is not settled here. Their QED3 analogue RT ("one microscopic mass and vacuum assignment gives controlled trajectories"). Ours: `library/c4-order.md`, `b4-induction.md`.

**(d) Status: [O].** `c4-order.md` [P] (conditional order, cycle named). (4) is elementary arithmetic once (3) holds (SA gives it in 0(a)).

### UV1. Torus source bound and ordinary stability (D1)

**(a) Theorem UV1** (SA D1, L4088–4137). Fix M = L^{m₀}, the compatible tori ℓ = 2L^m, m ≥ m₀, all scales 0 ≤ s ≤ K, cubes of side M a_s with even counts in every direction. Index a domain X by its union of cubes and let m(X) be the least number of edges of a connected cubical edge tree meeting every cube. Then, uniformly in the cutoff and the allowed torus, at first-passage data:

1. *(ST5)–(ST6).* log Z_{K,ℓ}(w) = Σ_X E_X(w) + Σ point counterterms, with E_X holomorphic on the ordinary source ball, depending on w only on a fixed number of neighbouring cube layers of X, independent of the representation of w by a list of tests, and |E_X| ≤ C e^{−κ m(X)} with κ above the rooted entropy rate for this indexing (multiplicities of extra domain types included); point counterterms holomorphic, cutoff-dependent bounds allowed but uniform in the torus.
2. *Normalised upper stability* on the ordinary source ball.
3. *Unsourced floor.* The unsourced partition-function floor in the form of SA L23481, with constants uniform in cutoff and allowed torus, including the reserve and the allocation of Wilson factors. (The consumer form CT4 of `parts/upper-chain.md` Text 7 is log Z_L(β) ≥ (L/P)⁴ log Z_Tor(β) − c_F(L/a_*)⁴.)

**(b) Imports.** IN1 (class at every level), SC1, LF1 (normalised positive label/history representation), C1.

**(c) Sources.** SA L22345–23385 (local energies, separated bounds), L23385–23621 (ordinary stability from a normalised history representation; OH4 L23439; floor L23481). CA-II L5–60348. QED3's UV. Ours: `library/d1-floor.md` (sufficient criteria: Lemmas L, B, Theorems F, U), `c1-repr.md`, `p2-floor.md`; `parts/upper-chain.md` Text 7 (UV-CT, a consumer form).

**(d) Status.** Criteria [C] (`d1-floor.md`, checked by Codex, row 176). `p2-floor.md` [P] partial. D1 [O]: its criteria must be verified for the actual construction (SA L4128–4137).

### AG1. Ages and uniform rarity of old regions

**(a) Theorem AG1.** (SA D3, L4165–4178; 4.13 L23258; 4.14 L23300–23315.) The probabilities or positive weights of live regions persisting from level j to level k ≥ j have a bound r(k − j) with Σ_m r(m) < ∞, uniformly in volume and in the location of a test, with every moment in m used by TP1; witness selection, reflection replication and pattern counting preserve the insertion and source weights. The weighted surviving-lineage age tail (4.14) is summable with the factor L^{8α} from two source derivatives (the overview's H box). ⟦open: AG-rarity⟧.

**(b) Imports.** LF1, IN1, LG1 (chessboard replication).

**(c) Sources.** SA L4165–4178, L23258–23315. CA-II L68374ff (two-point witness chapter). CA-III L111191: Proposition 8.12, "uniform rarity of never-healed old large-field regions", is in its list of statements "for which no complete argument is known"; L111431 lists "the age lemma" as stated with proof incomplete. Their YM3 analogue YHO1.

**(d) Status: [O].** D2 does not need AG1 (SA L4174–4176), so SR1, CL1, PH1 and RO1's UI step do not wait on it. TP1 does.

### SR1. All-state transfer, graded bounds and growth

**(a) Theorem SR1.** Assume UV1 in its rooted geometry and LG1. Let ρ, ν be periodic Gibbs states at the same first-passage datum, with tests real C¹, each support in its own radius-R ball placed anywhere, distinct supports at distance ≥ d. Then, with constants uniform in cutoff, states and positions:

1. *SA-D4, one-point transfer.* |ν(O_K(f)) − ρ(O_K(f))| ≤ C₁(R)‖f‖_♯; if both are invariant under all plaquette isometries, |ν(a_p) − ρ(a_p)| ≤ C a_K⁴.
2. *G4, cumulants.* |κ_n^ρ(O(f₁), …, O(f_n))| ≤ C_n(d; R) Π‖f_i‖_♯ for n ≥ 2; common holomorphic cell normalisers.
3. *D2, graded bound.* |ρ Π_i [O_K(f_i) − ν(O_K(f_i))]| ≤ B(R)ⁿ (n!)^k max{1, d^{−5n}} Π‖f_i‖_♯, with B(R) = C(R+1)⁴, k = ⌈p⌉ + 5 (cell-normaliser loss Q_i ≤ Cn^p); cumulants with [2B(R)]ⁿ.
4. *H1, diagonal-flat extension.* Passed to a separated-tuple limit, S_n extends uniquely to 𝒮_{≠}(R^{4n}) with |S_n(φ)| ≤ C_Eⁿ (n!)^{k+32} sup_{|α|≤20n, x}(1+|x|²)^{10n}|∂^αφ(x)|; constrained tensor density; RP transfers to finite positive-time sequences.

**(b) Imports.** UV1, LG1.

**(c) Sources.** SA L23621–24041 (transfer to all periodic states; domination lemma L23640; cell normalisers L23833; cumulants L23904), L24041–24366 (rooted domain counting (GS1)–(GS4)), L24917–25424 (quantitative diagonal-flat extension (QF1)–(QF22)); catalogue D2, D4, G4, H1 (L4138–4164, L4179–4196, L4541–4571, L4572–4599). CA-II L60348–64630. Ours: `library/d2-d4.md`, `growth-qf3.md`.

**(d) Status: [C]** as implications from full D1, S1d and S1g (`gates/bridge-check.md` §1; `gates/cluster-check.md` Part B). Open only through UV1.

### CL1. Continuum limits, Euclidean Hilbert space and cones

**(a) Theorem CL1.** Assume SR1, LG1 and IN1(4). Let (K_j, β_j) be first-passage data with K_j → ∞ and ν_j ∈ 𝒢_{a_j,β_j} centering states.

1. *Compactness.* One subsequence makes the ν_j-centred moments converge on every separated C¹ tuple (countable extension, moving tests, mirrors, one-point and cumulant limits). Every volume-first limit is a limit of SA 0(a)(iii) type.
2. *Inheritance.* The limit S is invariant under translations and W₄, reflection positive at every coordinate and diagonal mirror, symmetric, real, and regular on E^n_≠ (a unique distribution of locally finite order).
3. *Hilbert space (H2).* On ℂ𝔖({x₄ > 0}) with ⟨F, G⟩ = σ_S(θF̄·G), the separable space ℋ(S) carries e^{−tH} (strongly continuous, self-adjoint contractions, H ≥ 0, HΩ = 0), a unitary representation e^{iv·P} of R³ commuting with H, and a unitary representation of W₃; the same on the diagonal-flat extended domain.
4. *Cones.* H ≥ |P_j|, j = 1, 2, 3 (O6), and the cube cone.

**(b) Imports.** SR1, LG1, IN1.

**(c) Sources.** SA L4649–4856 (from local source bounds to continuum limits), L24366–24917 (compactness, lattice Gibbs limit), L25424–25966 (separated moments to Euclidean evolution; L25736–25904 for the cone); SA 0(b) L6921ff; Y3 L72903–74672, L75249–75578. CA-II L64630–68374. QED3's CL. Ours: `library/s4-s6.md`, `cone-o6.md`.

**(d) Status: [C]** as implications (`gates/bridge-check.md` §§2–3).

### TP1. The two-point law and TU10

**(a) Theorem TP1.** Let ϑ_* = 1/12000 (or a broader class). There are d₀ ∈ (0,1), n₀, and for each ϑ a ceiling γ_W(ϑ), such that for g ≤ γ_W(ϑ_*), d ≤ d₀, K − s(d) ≥ n₀, every periodic Gibbs state ρ at a first-passage datum and every C¹ pair (f, h) ∈ 𝔗(d; ϑ_*):

1. *(F2) Extraction* ⟦open: TP-F2⟧. S^T_2[ρ](f,h) = C_G ζ_K(d)² g_K(d)⁴ K_free(f,h)(1 + r_{K}(f,h)), C_G = 3(N²−1)/π⁴ > 0, |r| ≤ ½, with all lower cutoff requirements explicit, and the eventual cutoff threshold and constants uniform in ρ and support positions (SA F2, L4289–4359). The complete-force term (GCB52) of the conditional law must be bounded: the outline says that neither the small Hessian nor the Gaussian boundary theorem bounds the exterior and old-activity effects (SA L28196–28221).
2. *(F3) Running normalisation* ⟦open: TP-F3⟧. g_K(d)^{−2} = c_* log(1/d)(1 + o(1)), ζ_K(d) = 1 + o(1), c_* > 0, with the uniformity F2 needs; ζ is the derivative of the running coupling with respect to a constant source (SA F3, L4360–4378).
3. *7.6, transfer* ⟦open: TP-7.6⟧. One common reference/all-state normaliser carries the reference-torus law to every periodic state with O(d²) error (SA L26062, L26765–26934); the first step, the identification of (a) with the localised sourced exponent of Proposition 7.3, is the first unproved step of `ref-73.md`.
4. *TU10.* Consequently 0 ≤ S_2[ρ](f,h) ≤ u(d)‖f‖_∞‖h‖_∞ with u(d) = C′[log(1/d)]^{−2} → 0, and these closed inequalities pass to every limit and to all-state phase realisations (SA L4380–4412).
5. *Law on R⁴.* Limits of CL1 obey SA 0(c)(4) with ε̄ = ½ on R⁴; the same for each component of PH1 (SA 0′(3)(ii)).

**(b) Imports.** UV1, IN1, OL1, FC1, AG1, PR1, BG1, LF1, SR1, CL1, LG1.

**(c) Sources.** SA L25966–26704 (short-distance coefficient and non-triviality; (7a) L26000), L26704–27091 (covariance and transfer estimates for interacting extraction), L27091–28229 (sharp cutoff boundaries; marginal log-concavity L27149; GCB52 L28196–28221); catalogue F2, F3 (L4289–4415). CA-II L68374ff. CA-III L111245–111248: "the source lemma" and "the continuum kernel" (route: a classical computation for the free field) are listed as outstanding. Their YM3 analogue YVO1. Ours: `library/tu10.md`, `ref-73.md`; `parts/witness.md`.

**(d) Status: [O].** `tu10.md` (Codex, not checked): Lemma N's moment proof passes; the D1 source estimates and E1 flow bounds alone do not give TU10 ((2)–(5) there exhibit the missing coupling dependence). `ref-73.md` [P] (finite probability identity, stops at (a)). (4) given (1)–(3) is the outline's short closed-inequality deduction [SP].

### RO1. O(4) covariance

**(a) Theorem RO1.** Let S be a volume-first limit through periodic Gibbs states, or a canonical component of PH1 with its all-state realisation. Assume UV1 (rooted D1), LG1, CL1(2)–(4) and TP1(4) in its state-uniform form. Then:

1. *(UI) Insertion.* A one-field Hilbert insertion bound C η^{−p}‖k‖_♯ holds, independent of the number of surrounding fields (Y3 Prop IV-55-9 at d = 4).
2. *(PD) Plates.* An analytic L¹ plate density with exponent ℘ = p + 5 = 5 holds, with a scaled parametrix.
3. *(AK) Angular kernels.* Holomorphic product kernels on tubes, removal of plane smoothing, frame gluing to one kernel on a connected domain U_n, Gram representation, finite band 4|m| ≤ 5n, boost positivity, cut inequality with the empty tuple.
4. *(TU) Two-point harmonics.* Every nonconstant two-point harmonic vanishes, the critical frequency included.
5. *(AC) All orders.* Polygon divisibility, discrete convexity a_k = kb₂, local translations, removal of exceptional distributional support, hence every M(n) = 0: the hierarchy is O(4) invariant on separated compact C¹ tuples and on the diagonal-flat extension.

**(b) Imports.** UV1, LG1, CL1, TP1(4), SR1(4) (diagonal-flat density), PH1 (for components).

**(c) Sources.** SA L28229–28527 (one-field insertion), L28527–28888 (plate bound; ℘ = p + 5 at L28789), L28888–29922 (AK1–AK50), L29922–30508 (TU1–TU29), L30508–30866 (HC1–HC13). Y3 L75578–77017 (IV-55-9, IV-55-19, IV-56-17, IV-37-27). The QED3 outline's R uses RPM1 Theorem A with the insertion bound E e^{F(f)} ≤ exp{C(‖f‖₁ + ‖f‖₂²)}; by Lemma N (`t0-skeleton.md` §2) that hypothesis fails for O in four dimensions, so RPM1's route is not available here. Ours: `library/ui-port.md`, `pd-port.md`, `ak-port.md`, `tu-port.md`, `ac-port.md`.

**(d) Status: [C]** as implications from D1 (through UI), TU10 and the cone (`gates/o4-check-1.md` §§2–3 for UI, PD; `gates/o4-check-2.md` §§1–3 for AK, TU, AC; first failing step none; defects are wording or scope). Lemma N [C] (Codex, row 159). `pd-port.md` §5 and `tu-port.md` §§3–4 are our own text (shorter than the outline), checked as such.

### PH1. Phases, components and clustering

**(a) Theorem PH1.** Assume LG1, SR1 (all-state bounds S3) and CL1.

1. *(G3) Lattice plateau law.* With one numerical C independent of a, β, ν, r, n, A, B: for A, B depending on bonds in a[−r, r]⁴ and y ∈ aZ⁴ with n = |y|_∞/a − 2r ≥ 1, |ν(Āτ_yB) − Pl_ν(A,B)| ≤ C[(r/n)² + (r/n)³] 𝒩_{ν,r}(A)^{1/2} 𝒩_{ν,r}(B)^{1/2}, for every ν ∈ 𝒢_{a,β}, mixtures included (SA G3, L4486–4540).
2. *Conditional kernels and lattice decomposition.* On the compact metric configuration space there are Borel conditional probabilities with simultaneous uniqueness; with the DLR equations and (1) they give a unique decomposition of 𝒢_{a,β} into ergodic DLR states, and the pure set is closed.
3. *Canonical decomposition.* Each volume-first limit has a canonical decomposition (X, λ, σ_ξ), unique up to isomorphism; isometries leaving S invariant permute components and preserve λ; one-point functions 𝔠_ξ∫f with ∫𝔠_ξ dλ = 0; each σ_ξ has the invariances, positivity, symmetry, regularity, growth and bounds of S with the same constants.
4. *Clustering.* |σ_ξ(X·τ_vY) − σ_ξ(X)σ_ξ(Y)| ≤ C(X,Y)|v|^{−2} for |v| ≥ r(X,Y), uniform in ξ and over volume-first limits at g.
5. *(PV4) Vacuum.* P₀[F] ↦ (ξ ↦ σ_ξ(F)) extends to a unitary ker H → L²(X, λ) with Ω ↦ 1; ker H_{σ_ξ} = CΩ_{σ_ξ}; (PV3) is derived from the limit's bounds, RP and translation invariance.

**(b) Imports.** LG1, SR1, CL1.

**(c) Sources.** SA L3195–3757 (uniform lattice plateau, (PL4)–(PL16)), L30866–31111 (compact-metric conditional law), L31111–31386 (phase construction, conditional canonical decomposition), L31386–31533 (invariant Hilbert space; PV4 L31442, under (PV1)–(PV3) which that section does not derive, SA L31438–31440, as read in `gates/cluster-check.md`). Y3 L77017–78324, L79580–79749. CA-II L64630–68374. QED3's EC and C. Ours: `library/cluster-port.md`.

**(d) Status: [C]** (`gates/cluster-check.md` Part A, first failing step none; reading needed: ν_j ∈ 𝒢_{a_j,β_j}, as SA L31143 fixes).

### WR1. Wightman reconstruction per component

**(a) Theorem WR1.** Let σ be a component with: E0′ from SR1(4) (k_E = 20, κ_E = k + 32); invariance under R⁴ ⋊ O(4) on separated and diagonal-flat tests (RO1 for σ); reflection positivity on positive-time diagonal-flat sequences (SR1(4), CL1); symmetry and reality; the cone and unique vacuum (CL1(4), PH1(5)); the plate density of RO1(2) (`pd-port.md` (7)); and the bounds of `cluster-port.md` §§8–9. Then there are a separable Hilbert space, a dense invariant domain D₀, one Hermitian tempered scalar field, a strongly continuous unitary representation of the proper orthochronous Poincaré group with spectrum in V̄₊, locality, and a unique cyclic vacuum, whose Euclidean continuation is the tr F² hierarchy of σ on separated and diagonal-flat tests.

**(b) Imports.** SR1, CL1, RO1, PH1.

**(c) Sources.** SA L31533–31889 (reconstruction hypotheses, RC1; the per-component scope at L31799–31831). The outline imports this step: H3 is an "imported theorem" and "the reconstruction theorem itself remains external" (SA L4616–4630). Y3 L79749–81160 (Rec1–Rec4, IV-75-22 to IV-76-59), a direct scalar reconstruction we port. OS I, OS II §IV.1 (method). Ours: `library/wightman.md`.

**(d) Status: [C]** as an implication (`gates/o4-check-2.md` §4; it does not use OS II's continuation theorem; the four-dimensional changes l = 6 > ℘ = 5, weight power 3, S³ band density and SO⁺(1,3) checked). Its input is O(4) for each component, not for the averaged limit.

### WT1. Non-triviality

**(a) Theorem WT1.**

1. *NT1 (Lemma W).* Fix ϑ_W ≤ 10^{−7}. Assume the law SA 0(c)(4) on R⁴ for C¹ pairs in 𝔗(d; ϑ_W) at one d ≤ d₀ with |ε| ≤ ½ (needs g ≤ γ_W(ϑ_W)), for a component σ. Then H_σ ≠ 0 on Ω^⊥. (Proof in `t0-skeleton.md` §3.10: e^{−tH} = 1 would make the connected value constant in t; K_free changes by a factor > 7·10⁴ between t = 0 and t = 4d − 2ρ, while the error factors change by at most 48.)
2. *NT2* ⟦open: WT-NT2⟧. `parts/witness.md` Text 8.1 with (NT2-V), on the reflection-positive state with an admissible blocking map; this needs ε → 0 on R⁴ and the vertex part, where the outline gives only |ε| ≤ ½ on R⁴ (SA 0(c)(4)).
3. *X1* ⟦open: WT-X1⟧. The witness reads the outline's law, blocking map, gauge and observables without a change of law (`library/route-decisions.md` §8).

**(b) Imports.** TP1(5), CL1(3), PH1(3) (law per component), F3 for NT2.

**(c) Sources.** SA L25966–27091 ((7a)–(7b)), 0(c)(4)–(5). CA-II L68374ff. QED3's AS selects a component with κ₄^λ(f) > 0 by intersecting a full-measure set with a positive-measure set; ours needs no selection, since Lemma W applies to each component. Ours: `library/t0-skeleton.md` Lemma W, `parts/witness.md`, `parts/witness--rank-u.md`, `library/witness-running-tests.md`, `library/nt2-free-value-by-hand.md`.

**(d) Status.** (1) [P] (Claude, not yet checked; `nt1-window`, row 152, is a fallback). (2), (3) [O]. The NT2 definition is a working draft (GOAL.md).

## 6. Dependency graph

Edges read "A → B": B imports a statement of A.

**Ours.**

- LG1 → SR1, CL1, PH1, RO1, TP1, AG1
- FP1 → PR1, BG1, OL1
- PR1 → BG1 (A1's proof reads A2, A3 at the reference), BG1 → PR1 (A3 reads A1). This pair is one argument at a real critical reference; `library/a1-balaban.md` and the A3 chain are checked together. It is not a cycle in the order of constants (rows 4–7 of `c4-order.md`).
- BG1 → ST1, NL1, LF1, OL1, TP1
- PR1 → ST1, NL1, LF1, OL1, TP1
- LF1(2) → ST1 (stage geometry)
- ST1 → NL1, LF1, SC1, OL1(1)
- FC1 → OL1, TP1
- OL1 → IN1, TP1, NL1
- NL1 → IN1, LF1, SC1
- LF1 → IN1, UV1, AG1
- SC1 → IN1, UV1
- IN1 → NL1, LF1 (the inductive hypothesis at level k; the induction itself is the closure)
- IN1 → UV1, TP1, CL1, AG1
- UV1 → SR1, RO1, TP1
- AG1 → TP1
- SR1 → CL1, PH1, TP1, RO1, WR1
- CL1 → PH1, RO1, TP1, WR1, WT1
- TP1 → RO1, WT1
- PH1 → RO1 (components), WR1, WT1
- RO1 → WR1
- IN1, CL1, PH1, RO1, SR1, WR1, WT1 → AS1

**Theirs, as drawn in the overview** (read from the path coordinates of the PDF; labels are as printed; where a label sits between two arrows, my assignment is a reading, not certain):

- M → G; G → E; M + G + E jointly → N ("all three"); M → P ("free covariances")
- N → T; T → H ("flow hypothesis within the same induction"); T → R (early part)
- H → R (later part; the label "real history bounds" sits near this arrow); R early → R later ("source derivatives"); L → R later ("periodic-state source transfer")
- L + T + R later jointly → C (labels "one bare sequence", "uniform separated bounds", "all inputs")
- C → K ("lattice cone; limits")
- L, C, K, H, R later, P jointly → V ("periodic-state reflections and chessboards", "passage to limits and the selected phase", "history stability and ages", "source response", "free curvature coefficient", "all inputs")
- C + K jointly → Z ("Continuum cone, selected phase and reflected moment bounds for Z"; "structural inputs and component nontriviality"); V → Z; R → Z ("factorial growth and means"); all → Z ("all inputs; common parameters and phase")
- An annotation beside N: E, N, T, H and the source variations are one compatible induction, with previous-level bounds controlling the next step.

**Correspondence.** Their L = LG1; M = FP1 + PR1; G = BG1; E = OL1; N = NL1; P = FC1; C = CL1; T = IN1; R early = SC1; R later = UV1 + SR1; K = PH1; H = LF1 + AG1; V = TP1; Z = RO1 + WR1 + WT1 + AS1. ST1 has no box of its own in their overview; its content is their G box's "Required: Real and complex domains compatible with iteration" and the inclusions their outline states as hypotheses (Section 9).

## 7. Order of writing

Two principles from the process review: hardest first when choosing what to attack; the easier analogue first when building (port the YM3 or QED3 argument where one exists).

**Hardest open submanuscripts (flagged).**

1. **ST1** (stage admission, (D4)). Every open input of NL1, LF1's drop-outs and SC1 waits on it. The outline states it as a hypothesis; the complete account assumes Balaban's stage theorem. No published proof is known to us. First statement: ST-map at stage 0 → 1 with one collar layer (shift-map §4), then ST-cov for the layered family (layered-a3 (8)).
2. **TP1** (F2 with the complete-force term, F3, 7.6, state-uniform TU10), with AG1 inside it. It is needed twice: for O(4) through TU10 and for NT1/NT2. The outline itself states that no force bound is asserted for the resummed interacting conditional density (SA L28219–28221), and the complete account lists uniform rarity of never-healed old regions among statements with no complete argument known (CA-III L111191). First statement: TU10 as an upper bound only (it needs no exact coefficient), through 7.3 on a reference torus with a coarse positive reference estimate (`tu10.md`, next route). Port from YM3's YVO1 first.
3. **IN1** (the closed induction C4, with LF1(3), the C3 mass bound, inside it). First statement, cheap and early: break the budget cycle κ̄ → M → C₀^UM → Θ → κ̄ by a uniform cost envelope chosen before M, or show the cycle is real. A circular order kills the induction.

**Order.**

- *Phase A, freeze what is checked* (cheap, parallel, gives stable interfaces). Distil and referee once: LG1, FP1, SR1, CL1, PH1, RO1, WR1. Their notes are checked; the work is one minimal manuscript each with numbered statements and the definitions made explicit.
- *Phase B, the hard core, hardest first.* ST1 (Claude at length, long sessions), with IN1's order table beside it. Then BG1 and PR1 distilled with the layered parts left as the named open inputs ST1 fills. Then NL1 and LF1 (distil the checked links; attack LF-mass), OL1 (OL-incr), SC1, UV1.
- *Phase C, short distance.* AG1 and TP1 start in parallel with Phase B, from the YM3 analogue, since D2 and the consumer side do not need them. Then WT1 (Lemma W's check is one reading; NT2 after F3).
- *Phase D.* AS1, the final document, one line-by-line review, then the owner.

## 8. Where we depart from their assembly, and why

1. **Stage admission by intrinsic domains (ST1).** The outline's core definition builds in the (R5) chart Φ_{M_e(U)}(i^{−1}Log[M_e(𝐔)M_e(U)^{−1}]) in a chosen continuation domain (SA L5696–5727). Every stage then needs the returned datum in every old continuation ball on the full complex source, which ten lanes could not prove (`stage-thm.md`). Intrinsic domains remove the old-centre requirement; they keep the matching requirement (stage-resp §2). This is a change of definition, so NL1 and LF1 must rebuild their activities on the new domains (Section 5, ST1).
2. **The Hölder clause (H) in the core** (PR1(4)). bx.md shows an admitted input on the core (R4)–(R6) that violates (PW6). The repair is Balaban's CMP 109 (3.31) placed in the core.
3. **Kept forms from A^rel** (NL1(5)). The covariance proof works for the relative form and fails for the absolute-Hessian form (Defect 1 of `gates/kept-cov-check.md`); the measure is unchanged.
4. **Reconstruction is proved, not imported** (WR1). The outline imports H3; T0 includes the Wightman theory, so we port YM3_I's direct reconstruction.
5. **Non-triviality per component without selection** (WT1). QED3's AS selects a component; Lemma W gives NT1 in every component from the law on R⁴.
6. **Off-path parts dropped.** E2–E4, 2.12, the Ward route of 0(e), 0(c)(5) and the typed potential tests (SA L3779–3780, L4469–4470) are not on T0's path.
7. **Volume-first, as theirs.** Lemma S forces it for diagonal positivity; our joint torus extraction (upper chain Theorems 8, 10.2) serves T1 only.

## 9. Points where our notes disagree with their texts

Each item names the passage I read and the note that disagrees. None is a counterexample to their main theorem; their overview itself says Target Theorem A remains unproved.

1. **(PW6) as a conclusion of A1–A3.** SA L13560–13567 says that "the local regularity conclusion of A1–A3" gives (PW6); SA L16327–16328 states WF15 "on every specified complex core". `library/bx.md` (Codex; checked by Claude in `library/bx-fix.md`, ADVANCE) gives an admitted input on the core (R4)–(R6) whose box datum violates the affine remainder bound for every uniform constant; the first failing input is (PW6) for the complete field. This does not refute SA's theorem given (PW6). The repair (H) is checked by Codex (`gates/bx-fix-check.md`). This bears on their M and N boxes.
2. **The outline's absolute kept form is not covariant under the native action.** `gates/kept-cov-check.md` Defect 1: Δ^{(j)} contains G^{(2)}_V (SA L10200–10204, L17531); at a non-centre site of the flat witness the contour Hessian at 1^g is cos ε, not 1, so the covariance identity (4) fails for that form. I did not check whether the outline asserts covariance of the absolute form; the defect breaks the covariance claim only if that form is meant.
3. **A critical field is not unique without a gauge condition.** `intrinsic-dom.md` §2's pure-gauge family U_t gives distinct constrained critical fields arbitrarily close to 1. The outline states uniqueness of the orbit (SA L9667) and uses an axial representative, so this agrees with the outline; it corrects only a request in our own row 259.
4. **The (R) bound ER12 in one gauge.** `library/ur-ya.md` (checked by Claude in `ur-gauge.md`): (R) = SA ER12 is false for the representative fixed by (Id), uniformly in j, and holds for the Landau representative. The check notes SA leaves the gauge of ER2 open, so this is not a correction of SA's text.
5. **Order of constants.** Their N-box annotation says previous-level bounds control the next step in one compatible induction. `c4-order.md` [P] finds the supplied dependencies give that order only with an early uniform cost envelope; otherwise the cycle of Section 3 remains. This is a gap in the supplied dependencies, not a contradiction of their claim, and it is not checked.
6. **Stage theorem.** The complete account's Theorem 4.18 assumes "the stage theorem" of Balaban CMP 122a (1.60)–(1.70) (CA-I L54986–54994), and Remark 4.14 places background inclusion and drop-out spaces "outside the implication" (CA-I L49495–49546). This agrees with what their texts say of themselves; it is why ST1 exists.

I found nothing in the one-page overview that our checked notes contradict outright. Items 1 and 2 are against the outline, not the overview.

## 10. The final assembly theorem

**Theorem AS1.** Fix L and the constants in the order of Section 3. Assume:

- LG1, FP1, SR1, CL1, PH1, RO1, WR1 (all [C] as implications);
- BG1 and PR1, with ⟦BG-lay⟧, ⟦PR-lay⟧, ⟦PR-H⟧;
- ST1, with ⟦ST-cov⟧, ⟦ST-map⟧, ⟦ST-phase⟧, ⟦ST-wit⟧, ⟦ST-drop⟧;
- OL1 with ⟦OL-incr⟧, ⟦OL-nl⟧; NL1 with ⟦D4⟧ (= ST1), ⟦NL-ER7⟧; LF1 with ⟦LF-mass⟧, ⟦LF-2.8⟧, ⟦LF-2.10⟧, ⟦LF-2.13⟧; SC1; IN1 with ⟦IN-C4⟧, ⟦IN-order⟧; UV1;
- AG1 with ⟦AG-rarity⟧; TP1 with ⟦TP-F2⟧, ⟦TP-F3⟧, ⟦TP-7.6⟧;
- WT1 with ⟦WT-NT2⟧, ⟦WT-X1⟧.

Then T0 holds.

*Proof.* Take g ≤ g_* := min{γ, γ_W(ϑ_*), γ_W(ϑ_W), γ_W(ϑ₀)} after all other constants.

1. *Data.* IN1 closes the induction (C4) at every level with one set of constants; IN1(3)–(4) give first-passage data with K arbitrarily large. NL1 and LF1 at each level read ST1's (D4) and SC1's sources. UV1 then gives D1 on compatible tori, uniformly in K and ℓ.
2. *All states and limits.* SR1 (from UV1 and LG1) gives state-uniform one-point differences, cumulant and graded bounds. CL1 gives, along a subsequence of any first-passage sequence with centering states ν_j, a volume-first limit S with W₄ and translation invariance, RP at coordinate and diagonal mirrors, symmetry, reality, regularity, the Hilbert space ℋ(S) and the cone H ≥ |P_j|. This is T0(1).
3. *Components.* PH1 gives the canonical decomposition with the stated one-point functions (T0(2)); each σ_ξ inherits the invariances, positivity, symmetry, regularity, growth and bounds with the same constants, has a unique vacuum, and clusters at rate |v|^{−2} uniformly (E4).
4. *Growth.* SR1(4) gives E0′ for S and for each σ_ξ, with k_E = 20 and factorial exponent k + 32, independent of n and ξ; RP transfers to positive-time diagonal-flat sequences (E2 on 𝒮_{+}).
5. *Two-point law.* TP1 gives F2 and F3 for every periodic Gibbs state, uniformly; hence TU10 in its state-uniform form, and the law SA 0(c)(4) on R⁴ for S and for each σ_ξ.
6. *Rotations.* RO1, run for each component with its all-state realisation (UV1 for UI, CL1 for the cone, TP1 for TU10), gives O(4) covariance on separated and diagonal-flat tests. With translations, this is E1. E3 passes from the lattice through CL1. So each σ_ξ satisfies E0′–E4 and has the vacuum and cone: T0(3).
7. *Wightman.* WR1, applied to each σ_ξ with the inputs of steps 3–6, gives T0(4).
8. *Non-triviality.* WT1(1) applied to each σ_ξ with the law of step 5 gives NT1 in each component; WT1(2)–(3) give NT2. The law of step 5 is the last sentence of T0(5).
9. *One set of parameters.* Every step uses the same g, the same order of constants, the same subsequence and the same component; no step chooses a constant before one it depends on, by IN1(2). ∎

*What the assembly does not show.* It proves no open input. With every input closed, the proof is an implication chain, each link written by hand; no step rests on a computation. The current open inputs, hardest first: ST-map and ST-cov (ST1), TP-F2 with AG-rarity (TP1, AG1), IN-order and LF-mass (IN1, LF1), then OL-incr, NL-ER7, PR-H, LF-2.8/2.10/2.13, TP-F3, TP-7.6, WT-NT2, WT-X1.
