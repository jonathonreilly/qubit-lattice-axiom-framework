# RLARGE v2: the 4D large-field R-operation for the soft-kernel RG (integration of lanes C, D, E; 2026-10-28)

**v2 header (integration, not new mathematics).** This file is the v2 integration of RLARGE.md. The v1 file (sessions 17-20)
is kept byte-identical as **RLARGE_v1_snapshot.md**; every "v1 l.N" below is a line of that snapshot. The proven frozen
lemmas of v1 (§3-§7, checks §9-§9A) are carried as **Appendix A, verbatim**, with v2 reading notes at its head; nothing
in their proofs is edited. The pre-stated target text of v1 §1 is reproduced verbatim in §1.0. Every v2 change is tagged
**[v2-Xn]** with the source decision it applies. Integration record: RLARGE_INTEGRATION_LOG.md.

**Binding inputs (read for this integration; md5 of the working files at 01:18 UTC, 2026-10-28, while other agents were
editing them: PLD.md 4db9b142…, HIST.md 90f0ea9f…, FLOW.md 895c7958…, PROOF.md b76300ff…):**
- REVIEW_S16_S17 (all RLARGE fixes applied in v1, confirmed by REVIEW_S18_S19); REVIEW_S18_S19 fix 8 (applied in v1 [S20],
  confirmed by REVIEW_S20); **REVIEW_S20 fix 9** (the N5 ↔ RLARGE compatibility note v1 l.101-106 is stale: K-independence
  only given (BG-unif); "recorded in (SF)" was false). Applied here as [v2-C].
- PLD.md §12, §14.9, §15.6 (proposed edits E1-E8), with REVIEW_PLD_S1_S2 (B1-B9) and **REVIEW_PLD_S3 Part 5 ranking**:
  adopt E2, E3, E7; E1 with fixes E1-a (do not edit pre-stated §1) and E1-b (make "o(1)" precise); E8 with fix SG-2 (the cut
  clause is an event, never a change of χ_Q); REWRITE E4, E5, E6; add E9 (η_1 is RLARGE's (R3) value, not c_1ε_1) and E10
  (price defects adjacent to the history boundary). Applied as [v2-E1] … [v2-E10].
- **Lead architecture decision (binding):** every defect is priced three ways: (i) kernel mismatch (Lemma KN / RS, proven);
  (ii) fluctuation ((SG^fl) + PLD-desc, proven given (SG^fl)); (iii) coherent background (pointwise chain-energy bound from
  HIST's (I_k^E) plus CLS-sf in cone form, entered directly into ℒ_𝔥; ARGUED; its wall is CLS-sf cone form / (MSG), under
  attack in HIST.md session 3). **(PLD)_k is NOT an inductive hypothesis.** Applied as [v2-A].
- PLD's Proposition SHADOW (CONFIRMED-WITH-FIX, REVIEW_PLD_S1_S2) and the local collar clause σ_Q, with the σ-restricted
  gas for R1 (i) (fix B4). Applied as [v2-E2], [v2-E3].
- HIST.md §2-§18 with REVIEW_HIST_S1, REVIEW_HIST_S2: the joint-integrand route (CL^J, R1^J, R1_Λ = G5's local R1),
  (H-Mayer^J) as a whole-lattice Mayer expansion of small two-field activities, (I_k^E) (statement with GAPs S2-1..S2-3),
  n_♯ ≥ n_H, (D1-c) (refutes the per-cube coarse-Wilson forms of (H-pos) and (I_k)), (P4) ARGUED, RLF-step^J ARGUED with gaps
  H-1, H-3, H-4. Applied as [v2-H].
- FLOW.md §0, §4, §7-§10, §19-§19A with REVIEW_FLOW_S1_S2: the (F) quantifier is "the chain's own coupling sequence";
  additive constant R and (F_R); one-step monotonicity "not implied" by (F_R) (factors e^{aR}); (P2) uses β_+; RLARGE must
  deliver the per-level (RLF-δ)_k from (F_R) on [0, k] only (FI-1). Applied as [v2-F].

Status words as in PROOF.md: PROVEN-HERE (counted or not, said each time), CONDITIONAL (implication proven, hypotheses
named), ARGUED, OPEN, HYPOTHESIS. Review verdicts are quoted from the review files (CONFIRMED / CONFIRMED-WITH-FIX / GAP /
WRONG). Weights: **P** = paper-scale, **s** = session-scale (REVIEW_S15_CONVERGENCE's convention). Balaban CMP 122 is
[not-read]; nothing here is attributed to it. Imported items are never load-bearing for a PROVEN-HERE claim. This file
makes no tally change in PROOF.md (the ledger owner decides).

---

## 0. Conventions

- **Levels** (v1 §0, unchanged). Level k = after k RG steps; k = 0 bare, k = K the unit lattice. U_k is the level-k field on
  Λ_k; d = 4; L ≥ 3 odd; G = SU(N), N ≥ 2. A level-k cube is a level-k block (L⁴ level-k sites = one level-(k+1) site);
  π(z) := ⌊z/L⌋ is the level-(k+1) cube containing the level-k cube z (HIST §0). T is the side of the level-K torus in
  level-K sites; T_k = T·L^{K-1-k} is the level-k side in level-k cubes (v1 §1A, R1819-fix F2).
- **Action normalisation [v2-F; FLOW §0, Lemma F-norm, CONFIRMED].** s(U) := 1 - N⁻¹Re tr U ∈ [0, 2]; the level-k Wilson term
  is u_kΣ_ps(U_p) with **u_k := 1/g_k² = β_Wilson = 2N/g_std²**, g_std the coupling of (1/(4g_std²))∫F^aF^a with
  tr(T^aT^b) = δ^{ab}/2. One-loop slope per step: **β_1 := β_0^std = 11N²/(12π²)** per log L (2N × 2b_0, b_0 = 11N/(48π²);
  PLD.md §0 notes that EXISTENCE.md's normalisation is the same measure with g² → 2Ng²). Inequality (B):
  s(U) = ||1 - U||²_HS/(2N) ≥ ||1 - U||²_op/(2N).
- **The exact chain** (v1 §0; HIST §0). W(U_0, …, U_K) := e^{-S_0(U_0)}Π_{i<K}K_i(U_{i+1}, U_i), S_0 = Wilson at g_0, K_i = Π_c
  k^{(i)}_c, k^{(i)}_c(V, U) = e^{-(κ/g_i²)φ_{M̄_c(U)}(V)}/∫e^{-(κ/g_i²)φ_{M̄_c(U)}} (HIST (3.0), the normalised D4-norm kernel
  with the SU(N) maximiser W_0). ∫K_i dU_{i+1} = 1, so Z_K = ∫W = ∫e^{-S_k}dU_k. Lemma TD (HIST §2): given U_k, the level-(k+1)
  links are independent with densities k^{(k)}_c (plain chain measure).
- **Indicators.** χ_Q := Π_{p⊂int Q}1{||1 - U(p)||_op < ε_1} (cube-INTERIOR plaquettes only), ζ_Q := 1 - χ_Q. χ_Q is never
  changed: Proposition CL (a)-(b) and CL^J (a)-(b) use that it reads only interior plaquettes [v2-E8, fix SG-2].
- **Tori [v2-E7].** Hypercubic tori (equal sides) wherever GT-lat' (ii) / Lemma W1R-sym is used to produce ONE coupling
  shift. With a different time side the time-preserving subgroup of B_4 splits Λ²R⁴ into the electric and magnetic triplets
  and two shifts are needed (PLD §12 item 4, REVIEW_PLD_S1_S2 B9). The per-history route of §3 uses no reflection
  positivity, so RLF-step does not need the even tori of the chessboard results; those stay in the existence lane.
- **Thresholds.**
  - ε_1 (the cut), ε_loc (v1 §5), ε_♮ (v1 §7.2, R1's chart condition), ε^J_loc, ε^J_♮ (HIST §4-§5, joint route).
  - **η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))} [v2-E9]**: Lemma RS (R3)'s value (v1 §6). It is **not** KN-step's c_1ε_1 (that
    is EXISTENCE's re-centred dichotomy, RX34-fix 9); PLD §15's "η_1 = c_1ε_1" is withdrawn by REVIEW_PLD_S3 B-S3-2 (F-9',
    INH-1). Proposition INH holds a fortiori with this η_1 (REVIEW_PLD_S3, INH-1).
  - η_q := min{ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d} (HIST Lemma RS-lin, joint route's quietness threshold). For ε_1 ≤ 2,
    η_1 ≤ ε_1/(256NA_d), so η_1 ≤ η_q unless the δ_0/A_d cap binds; a price at the lower threshold implies one at the higher.
  - **[v2-C, REVIEW_S20 fix 9] N5 compatibility (replaces v1 l.101-106).** For the small-field package to cover this file's
    small-field region, ε_1, ε_loc (and ε^J_loc) must be ≤ the N5 background threshold in matching units (ε_1 is an
    operator-norm cut on ||1 - U_p||_op; N5 uses |log U_p|_HS; the conversion is cosmetic, REVIEW_S20). The N5 threshold is
    proven at level 0 (Theorem N5-sf0, ≈ 2·10⁻³²/C_Δ) and at level i ≥ 1 only in the per-level form, shrinking by ≈ 10⁻⁴⁰ per
    level (Proposition NAH-ind, PROOF [S20]). **So K-independent thresholds, hence K-independent a'' ∝ ε_1² and n_♯, exist
    only under (BG-unif)** (or another level-uniform N5 threshold; precise template REVIEW_S20 Part 2). This is a real
    dependence of RLF on N5's level-uniformity, not "only finiteness". It is written into (SF^J)_k in §4.2 (row 3).
  - **[v2-E8, with fixes TL-1, SG-2]** ε_1 < 2sin(π/N) is implied once ε_1 ≤ ε_* < 2sin(π/N); it is recorded explicitly
    because ε_* is an existence constant (Lemma TL needs it: the principal log of a cut-good plaquette is traceless). The
    clause "the cut controls every plaquette used as an N5 background" is implemented as an EVENT in U inside (SG^fl)'s
    domain (like 𝒱^sf of §3.2), with the residual rough inter-cube plaquettes priced as defects (§2.3); it is not a change of
    χ_Q.
- **Flow hypothesis (F_R) and its quantifier [v2-F, v2-E1 with E1-a, E1-b].** Along **the soft chain's own effective
  coupling sequence** (u_k) (FLOW Def F-g; node A5), never "every sequence obeying (F)":
    **(F_R)_{[0,k]}:  β_-(m - j)log L - R ≤ u_j - u_m ≤ β_+(m - j)log L + R  for 0 ≤ j ≤ m ≤ k,**
  with 0 < β_- ≤ β_+ and R ≥ 0 fixed constants (FLOW Theorem F-flow: R = 2R_0, β_± = β_0^std ± C_ργ²/log L, given (UNIV-1L),
  (SF-g), (RLF-δ); CONFIRMED conditional as labelled, REVIEW_FLOW_S1_S2). (F) of v1 §0 is (F_R) with R = 0. *Sufficient
  bracket (E1-b, REVIEW_PLD_S3):* sequences with 1/g_j² - 1/g_k² ≥ β_1(k - j)log L - C(1 + log(1 + k - j)) for all j ≤ k (the
  two-loop-tolerant form). *Reason:* PLD-AF (CONFIRMED, REVIEW_PLD_S1_S2) makes the uniform (PLD-dis) statements consistent
  with one-loop running only for sequences running at least as fast as the chain (one-loop basis ARGUED); for sequences with
  β_+ < β_1 the level-k field is at strong coupling (FLOW §4 FI-2). Since the kernel couplings enter the chain's running
  through the noise, "the chain's own sequence" is a fixed-point condition (A5's content; EXISTENCE RX56-fix 9).
- **Consequences of R > 0 (FLOW §19A table, with REVIEW_FLOW_S1_S2 RN-1, RN-2) [v2-F].**
  - One-step monotonicity 1/g_i² ≥ 1/g_{i+1}² is **not implied** by (F_R) (it is not false: u_i - u_{i+1} = b_i + ρ_i ≥ b_i - C_ργ²,
    so it holds at levels with b_i > C_ργ²). Every use acquires a factor: Lemma RS's "priced at the finer coupling" and v1 §7.1's
    (Ce^{-a_RS/g_k²})^{n/c_RS} ≤ (Ce^{-a_RS/g_{k+1}²})^{n/c_RS} hold with C → Ce^{a_RS R}; v1 §7.2 (iv)'s "g_j ≤ g_K by (F)" reads
    g_j² ≤ g_K²/(1 - Rg_K²) ≤ 2g_K² for g_K² ≤ 1/(2R); PLD Corollary PLD-fin's ordering (PLD l.194) likewise (FLOW §19A PLD row);
    HIST's CL^J/RS-lin hypothesis g_k ≤ g_{k+1} likewise (integration note; HIST states it as a hypothesis, see Conflict K4).
  - Lemma LF-n, (P1) = HIST-sum, (P2): C → Ce^{aR} (per n-cube term e^{naR}); the slope criteria naβ_- > 4, n_*, n_♯, n_H are
    unchanged (they use β_- only).
  - **(P2) uses β_+** for the polynomial prefactor: g_k^{-6} ≤ (1/g_K² + β_+(K - k)log L + R)³ (RN-2).
  - Proposition SHADOW's comparison uses the UPPER half (RPLD-fix F-6); under (F_R) it acquires e^{3κε_♮R}.
- **Sign of the coupling shift [v2-H, HIST (c4) RH2-fix 9].** R1 (iii) and R1^J add +δβΣs(U_p) to the LOG of the integrand;
  in the density e^{-u Σs} this is **u → u - δβ**. See Conflict K1 for v1 §8.3 / FLOW (SF-g) FR-2, which wrote "+δβ". Only
  |δβ_k| enters any bound.
- **Polymers, clusters** (v1 §0): *-connected sets of cubes; *-separated = cube distance ≥ 2.

---

## 1. Target: Theorem RLF

### 1.0 Pre-stated text (v1 §1, l.64-93, verbatim; not edited)

**What a 4D large-field R-operation must deliver** (the reconstruction target LF-count names, in the soft setting):

**Theorem RLF (target; OPEN).** There are g-independent constants ε_1 > 0, a > 0, κ_d > 0, C, an integer n_* ≥ 0 with
(n_* + 1)aβ_- > 4, and g_0 > 0 such that for every K, every torus T (side ≥ 3 blocks at level K) and every coupling
sequence with g_K ≤ g_0 obeying (F):

- **(RLF-0) Counterterms.** For each level k and each cluster shape Y with |Y| ≤ n_* (shapes up to translation), there
  are a field-independent number c_0(Y; g_k) and a field-independent Ad-invariant quadratic form T_Y(g_k) on
  su(N) ⊗ Λ²R⁴, with |c_0(Y; g_k)| + ||T_Y(g_k)|| ≤ C^{|Y|}e^{-a|Y|/g_k²}, depending only on (Y, g_k, L, N, κ, ε_1) and on
  the shape class (translation covariant; B_4-covariant). The marginal parts combine per level into ONE coupling shift
  δβ_k := Σ_{[Y]}t̄_{[Y]}(g_k) (B_4-orbit averages), with Σ_k|δβ_k| ≤ Ce^{-a/g_K²} uniformly in K and |δβ_k| ≤ g_k^6.
- **(RLF-1) Exact factorisation of the vacuum part.** Z_K = exp(Σ_{k<K}Σ_{Y: |Y|≤n_*}c_0(Y; g_k)) · Z_K^{ren}, where the
  inner sum runs over all placements of all shapes at level k (so the prefactor is a field-independent c-number,
  Σ_k O(N_k e^{-a/g_k²}), the only K-divergent quantity, which LF-count shows to be divergent).
- **(RLF-2) Returned (recycled) contributions.** In Z_K^{ren} every level-k cluster of ≤ n_* bad cubes with a small-field
  collar is returned to the small-field region: its contribution is the remainder R(Y) after subtracting c_0 and the
  T_Y-term, with |R(Y)| ≤ C^{|Y|}e^{-a|Y|/g_k²}·𝔯_k(Y) and 𝔯_k(Y) the GT-lat remainder functional of the level-(k+1)
  background on Y's box, and with exponential tails e^{-κ_d d(X)} in its dependence on the far field; and per final
  unit cell, Σ_{k}Σ_{Y in the cell}|R(Y)| ≤ C sup_k(C e^{-a/g_k²}) uniformly in K (summable against L^{4(K-k)}).
- **(RLF-3) Unreturned large fields.** Clusters with |Y| > n_* (and clusters whose collar is not small-field) stay
  large-field regions, nested as in Dimock II (small-field regions decrease with k), with weights
  ≤ Π_Y(Ce^{-a/g_k²})^{|Y|}, and Σ over all such histories ≤ exp(C|T|e^{-(n_*+1)a/g_K²}).
- **(RLF-4) Output.** |log Z_K^{ren} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} uniformly in K (any a' < a), where Z_K^{sf} is the
  small-field partition function of the soft RG with couplings shifted by δβ_k. Together with the small-field package
  (node A), this is L6-soft modulo the vacuum c-number of (RLF-1).
- **Composition.** With **LF-count**: the divergent per-level sum of LF-count sits entirely in the c-number of (RLF-1).
  With **R4D-iso**: the case |Y| = 1, frozen exterior, is R4D-iso/R4D-lat/D4-norm (c_0 = log(1 + ρ_0), T_Y = c_ρ-term).
  With **Theorem CE**: at level K the remainders R(Y) and the unreturned large-field polymers are activities H(X) obeying
  |H(X)| ≤ H_0e^{-κd(X)} with κ > 3κ_0 + 3 (≈ 457 in M-units) and H_0 ≤ c_0(κ), for g_K small enough (to be made
  explicit).

### 1.1 Amendment history
- **v1 §1A [R1617-fix, session 18; R1819-fix 8, session 20]** (text in RLARGE_v1_snapshot.md l.95-161; confirmed by
  REVIEW_S18_S19, loose end REVIEW_S20 fix 9): (1) one exponent a_♯ and n_♯ := ⌊4/(a_♯β_-)⌋; (2) two thresholds: returned vs
  unreturned decided by the defect number alone, collar-bad configurations returned; (3) (RLF-0)/(RLF-1) indexed by
  connected supports S, extracted only at levels with T_k ≥ W := 2n_♯ + 5, wrap levels a bounded term; (4) Z_K^ref defined;
  (5) (SF-last) added to (RLF-4); (6) (RLF-5) complex fields added.
- **v2 amendments (this file), each against v1 §1A:**
  - **[v2-E1]** quantifier: "every coupling sequence with g_K ≤ g_0 obeying (F)" → "the soft chain's own effective coupling
    sequence, obeying (F_R) (§0), with g_K ≤ g_0" (sufficient bracket: E1-b's two-loop-tolerant form). §1.0 is not edited
    (E1-a).
  - **[v2-E2]** collar-badness by the local clause σ_Q (§2.2); the clause "(H-ch) fails on Q's box" of v1 §1A item 2 is
    deleted (Proposition SHADOW).
  - **[v2-E3]** returned configurations: σ-restricted gas; the collar-bad returned configurations are an explicit activity
    family; no pointwise Taylor extraction; extraction at V = 1 after the sea average (§2.4, §4.3 step 3).
  - **[v2-H]** joint-integrand route at stages k ≥ 0 (CL^J, R1^J, R1_Λ); the representation is (I_k^E) (chain-energy main
    term), not v1 §8.1's coarse-Wilson (I_k); the counterterm δβ_k shifts the coupling u_k of the main term u_k𝓔_k
    (HIST (c4)), up to a small β = 0 polymer.
  - **[v2-H]** threshold n_♯ ≥ n_H := ⌊(4 + 38416B_0/log L)/(a_♯β_-)⌋ (HIST Theorem HIST-sum), and ≥ n^J_* (HIST §5).
  - **[v2-H, existence-lane request]** (RLF-3) is stated per history as a nonnegative ratio bound (the (H-w) form), §1.2.
  - **[v2-F]** (RLF-δ)_k added: the per-level coupling-shift bound, derived at level k from (F_R)_{[0,k]} only (FI-1).
  - **[v2-E7]** hypercubic tori.
  - **[v2-A]** (PLD)_k removed from the hypotheses; three-way defect pricing (§3).

### 1.2 Theorem RLF, v2 (amended target; OPEN)
There are constants ε_1 > 0, a_♯ > 0, κ_d > 0, C, B_0, an integer n_♯ ≥ max{n^J_*, n_H} and g_0 > 0, independent of g, K, T and
the history, such that for every K, every hypercubic torus with T ≥ 3, and **the soft chain's own effective coupling
sequence (g_k) with g_K ≤ g_0 obeying (F_R) (§0)**, with W := 2n_♯ + 5:
- **(RLF-0) Counterterms.** For each level k with T_{k+1} ≥ W there are field-independent infinite-volume numbers
  c̄_0^{sea}(g_k) and δβ_k (= δβ_k^{sea} of (W1-ret'^J)_k (a)), with |c̄_0^{sea}| + |δβ_k| ≤ Cg_k^{-p}e^{-a_♯/g_k²} (p a fixed
  power; PLD Proposition W1R gives p = 6 + p(SC)); translation invariant; ONE coupling shift per level by B_4 (GT-lat' (ii),
  W1R-sym; hypercubic torus). Σ_k|δβ_k| ≤ Ce^{a_♯R}e^{-a'''/g_K²} for every a''' < a_♯ ((P2), with β_+ in the prefactor).
- **(RLF-δ)_k [v2-F, new item; FI-1].** For every k: if g_0, …, g_k ∈ (0, γ_0] and (F_R)_{[0,k]} holds for the chain's own
  sequence, then |δβ_k| ≤ g_k⁶. The bound is derived at level k from data on levels [0, k] only, never from g_K or from (F) on
  [0, K]. (It is the per-level bound |δβ_k| ≤ Cg_k^{-p}e^{-a_♯/g_k²} ≤ g_k⁶ for g_k ≤ γ_0; it uses no flow input beyond g_k ≤ γ_0.)
- **(RLF-1) Vacuum.** Z_K = exp(𝒱_K^{LF})·Z_K^{ren}, 𝒱_K^{LF} := Σ_{k<K: T_{k+1}≥W}N_{k+1}c̄_0^{sea}(g_k): field- and
  history-independent, the only K-divergent quantity (HIST (P3)).
- **(RLF-2) Returned contributions.** Every defect configuration 𝒟 (§2) with n(𝒟) ≤ n_♯ is returned: after the sea average
  and the extraction of c̄_0^{sea}, δβ_k at V = 1 (§2.4), its contribution is a remainder activity that is gauge invariant,
  C³, local up to e^{-κ_dd} tails, and an admissible irrelevant polymer of the small-field package at level k + 1 in the sense
  of (SF-irr)_{k+1} (PLD §9.3), as a two-field polymer in (U_{k+1}, U_{k+2}) after U_k is integrated (HIST H-pos^J (iii)).
  Its summation over levels and cells is node A4's contraction (v1 §10).
- **(RLF-3) Unreturned large fields, per history.** Z_K = Σ_{𝔥 admissible}Z(𝔥) with every Z(𝔥) ≥ 0 and
    Z(𝔥) ≤ Z_K^{sf}·Π_{j<K}Π_{𝒟∈comp(𝒰_j)}(C_ℓe^{-a_♯/g_j²})^{|𝒟|}·exp(B_0Σ_{k<K}|Ω^c_k(𝔥)|)   (the (H-w) form, HIST §7.4),
  and Σ_{𝔥≠∅}Z(𝔥) ≤ Z_K^{sf}(exp(C_H|T|e^{-(n_♯+1)a_♯/g_K²}) - 1) uniformly in K (Theorem HIST-sum, with C_ℓ → C_ℓe^{a_♯R}).
- **(RLF-4) Output.** Under (SF-last): |log Z_K^{ren} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} (any a' < a_♯), with Z_K^{sf} the
  small-field partition function of the soft RG with shifted couplings; Z_K^{ref} := exp(𝒱_K^{LF})·Z_K^{sf,ref} as v1 §1A
  (RLF-4) (its soft-RG definition is part of node A; REVIEW_S18_S19 accepted the pointer for a target). Then
  exp(-E'_-|T|) ≤ Z_K/Z_K^{ref} ≤ exp(E'_+|T|): L6-soft for this normalisation.
- **(RLF-5) Complex fields** (v1 §1A, unchanged): analyticity of the returned remainders, the polymers they feed into the
  level-(k+1) representation, and the large-field factors on the complex neighbourhood node A uses, with the bounds up to
  e^{O(δ)} per cube. The g-uniform width is not shown; PLD §9.4 ARGUES width O(g/√κ) for one frozen activity. The same
  gauge-covariant domain question is (I_k^E)'s GAP S2-2 (§4.2, Conflict K7).
- **Composition.** LF-count, R4D-iso and Theorem CE as v1 §1; the level-K step needs (SF-last).

### 1.3 Numbering map, v1 → v2 (for the existence lane and other citers)

| v1 label (place) | v2 label (place) | change |
|---|---|---|
| §1 (RLF-0)…(RLF-4) (pre-stated) | §1.0, verbatim | none |
| §1A (RLF-0) connected supports S, T_k ≥ W | §1.2 (RLF-0) | sea-averaged numbers extracted at V = 1 (E3); joint route T_{k+1} ≥ W; bound Cg^{-p}e^{-a_♯/g²}; (F_R) factor in Σ_k |
| §1A (RLF-0) "|δβ_k| ≤ g_k⁶" | §1.2 **(RLF-δ)_k** (new item) | per-level, from (F_R)_{[0,k]} only (FI-1) |
| §1A (RLF-1) | §1.2 (RLF-1) | 𝒱^LF indexed by level-(k+1) cubes (HIST (P3)); unchanged in kind |
| §1A (RLF-2) | §1.2 (RLF-2) | defects with σ_Q (E2); σ-restricted gas + collar-bad family (E3); (SF-irr) admissibility; two-field form |
| §1A (RLF-3) | §1.2 (RLF-3) | per-history nonnegative bound (H-w) + HIST-sum; threshold n_♯ ≥ n_H; C_ℓ → C_ℓe^{a_♯R} |
| §1A (RLF-4) | §1.2 (RLF-4) | unchanged |
| §1A (RLF-5) complex fields | §1.2 (RLF-5) | unchanged; linked to (I_k^E) GAP S2-2 |
| §1A item 1 (a_♯, n_♯ := ⌊4/(a_♯β_-)⌋; N5 note l.101-106) | §0 thresholds, §4.4 (a_♯), §5 (n_♯ ≥ n_H) | N5 note replaced (needs (BG-unif)); c_RS = 5⁴ replaced by the three-way price (§3.4) |
| §1A item 2 (defect configuration; collar-bad incl. "(H-ch) fails") | §2.2-§2.3 | (H-ch) clause deleted; σ_Q; E8 event; E10 boundary family |
| §1A items 3-6 | §1.2 | as noted per item |
| §8.1 (I_k) | §4.1 (I_k^E) (HIST §14.1; GAPs S2-1..S2-3) | coarse-Wilson main term ARGUED false on the ε_1-domain ((D1-c), H-2) |
| §8.2 (F) | §0 (F_R) | quantifier and R |
| §8.2 (SF)_k | §4.2 (SF^J)_k | two-field output; level-uniform thresholds; outputs (SG^fl)_k, (I_{k+1}^E) |
| §8.2 (H-pos)_k | retired: Theorem H-pos^J (HIST §6) | content relocated, not removed (RH1-fix H-10) |
| §8.2 (H-Mayer)_k | §4.2 (H-Mayer^J)_k | whole-lattice, small two-field activities (H-1) |
| §8.2 **(PLD)_k (i), (ii)** | **not a hypothesis**: §3 three-way pricing | [v2-A]; PLD-SG kept as an implication only |
| §8.2 (W1-ret')_k (a)-(d); (R1-loc) | §4.2 (W1-ret'^J)_k; R1-loc = Corollary R1_Λ (HIST §5) | σ-gas, extraction after average (E3), (SC)_k, (SF-irr)_{k+1} |
| §8.2 (HIST)_k | §5: (H-w) [P] + Theorem HIST-sum (CONDITIONAL) | combinatorial half proven (conditional); analytic half (H-w) |
| §8.2 (SF-last) | §4.2 (SF-last) | unchanged |
| §8.3 Proposition RLF-step | §4.3 RLF-step v2 | ARGUED (was CONDITIONAL in v1; v1's list was incomplete: G5, (D1-c), H-1..H-4) |
| §8.4 (P1)-(P5) | §5.3 | (P1) = HIST-sum; (P2) β_+ and e^{aR}; (P4) ARGUED (re-based on (I_k^E)(b)) |
| §11 walls 1-7 | §4.2 table, §7 DAG | complete list |
| EXISTENCE's (RLF-3^dis) (its own label; EXISTENCE §13.4-§13.5, §13.9) | reads §1.2 (RLF-3) | the per-history (H-w) form is the nonnegative-ratio statement EXISTENCE §13.5 proposed, with Z_K^{sf} in place of Z_K^{ref} (Conflict K8) |

---

## 2. Defects (definition)

### 2.1 Where the level-(k+1) R-operation acts (RS ordering, HIST §7.1)
Stage k is the RG step that integrates U_k. Stage k inserts the level-(k+1) large-field indicators into the stage-k
integrand J_k (HIST §2), decides the new unreturned set 𝒰_{k+1}, runs the level-(k+1) R-operation on J_k (CL^J, R1^J), and
only then integrates U_k (v1 R-9 ordering, made explicit by HIST §7.1). Level-0 cubes (𝒰_0) are handled by the bare R1 of v1
§7.2 (Appendix A), whose level-0 action is Wilson's.

### 2.2 Bad and collar-bad cubes [v2-E2]
Let Q be a level-(k+1) cube of the current small-field region (or, at the bare level, a level-0 cube).
- **Bad:** ζ_Q = 1 (some interior plaquette ≥ ε_1).
- **Collar-bad (bare form; PLD §9.1 (i)):** σ_Q = 0, where
    σ_Q := 1{max_{p⊂N_1(Q)}||1 - U_p||_op ≤ ε_loc/2 and max_{c∈C(Q)}||V_c - S_c(U)||_op ≤ ε_loc/2},
  U the sample's own links (one global completion for every cube). σ ≡ 1 on a cluster Y implies ε_♭(U; Y) ≤ ε_loc, which is
  what Proposition CL (c) needs (PLD §9.1; CONFIRMED, REVIEW_PLD_S1_S2).
- **Joint form (stage k ≥ 0, HIST §4-§6):** non-quiet cubes (η_k(Q) ≥ η_q on R_k(Q)) are collar-bad (HIST H-pos^J bullet 3,
  RH1-fix H-11), and CL^J (c) needs quietness and ε^J_♭(D; Y) ≤ ε^J_loc. **The joint analogue σ^J_Q of σ_Q (a per-cube local
  clause implying ε^J_♭(D; Y) ≤ ε^J_loc for clusters) is not stated in any source** (Conflict K2; integration item I-σ^J, §4.2).
  Until it is, the joint route's collar-badness is "non-quiet, or ε^J_♭(D; Q) > ε^J_loc" read per cube.
- **Deleted [v2-E2]:** v1 §1A item 2's clause "(H-ch) fails on Q's box". **Reason: Proposition SHADOW (PLD §9.1,
  PROVEN-HERE, CONFIRMED-WITH-FIX):** P_cut,k(the collar-bad component of Q_0 has ≥ (2n_c + 1)⁴ cubes) ≥ ¼e^{-3κε_♮/g_{k-1}²},
  incompatible with any weight (Ce^{-a/g_k²})^{n(𝒟)} that dominates the cut-law probability (box radius R_* ∝ n_♯). The same
  applies to (H-ch)^J used as a defect criterion (REVIEW_PLD_S1_S2: G5 is to be met by σ_Q, not by a box-local (H-ch)).
  (H-ch)/(H-ch)^J survive only as the chart condition of the Taylor step (R1 (ii)-(iii), R1_Λ's Λ'), never as a defect
  criterion.

### 2.3 Defect configurations
A level-(k+1) **defect configuration** 𝒟 is a *-connected set of cubes each of which is bad or collar-bad; n(𝒟) := |𝒟|. The
families that need a price (each priced by §3):
- (D-a) bad cubes ζ_Q = 1 generated by the step (RS-generated: a level-(k+1) plaquette ≥ ε_1);
- (D-b) collar-bad cubes (σ_Q = 0, or the joint clause of §2.2), including non-quiet cubes;
- (D-c) **[v2-E8 / SG-2]** cubes with a rough INTER-cube plaquette in N_1(Q) used as an N5 background where (SG^fl) is
  applied: an event in U (not a change of χ_Q), priced as (D-b) (it makes σ_Q = 0 when the plaquette is ≥ ε_loc/2; below that it
  is inside 𝒱^sf's control);
- (D-d) **[v2-E10] boundary-adjacent defects:** defects of types (D-a)-(D-c) with a plaquette or cube within distance 1 of
  ∂Λ(𝔥). PLD's interior sets 𝒫°(𝔥), 𝒬°(𝔥) exclude them and v1/PLD sent them to "(HIST)'s boundary terms e^{B_0} per boundary
  cube"; **e^{B_0} is a cost, not a suppression** (REVIEW_PLD_S3 SG-1). They need their own e^{-a/g²}: either (SG^fl) is stated
  for every plaquette with at least one link in Λ(𝔥) (the exterior ω is fixed in μ_{𝔥,ω}, so the others are constants), or this
  family is priced separately. **OPEN; neither is written** (item E10 of §4.2).
- **Returned:** n(𝒟) ≤ n_♯ (whatever the collar). **Unreturned:** n(𝒟) > n_♯, which join the history as 𝒰_{k+1} (HIST §7.1,
  admissibility (A1)-(A2)).

### 2.4 The σ-restricted gas and the collar-bad activity family [v2-E3; PLD §9.1 repair (α)-(β), fix B4]
- **(α)** The convergent gas of Theorem R1 (i) (and R1^J (i), R1_Λ) is run with σ in place of (H-ch): only clusters with σ ≡ 1
  on Y carry CL (c)'s bound, by Lemma 7.2-0's proof verbatim with "ε_♭ ≤ ε_loc on the support" supplied by σ ≡ 1 (PLD §9.1;
  REVIEW_PLD_S1_S2 B4: "Lemma 7.2-0 verbatim"). Status: the substitution is stated in PLD as a repair "(proposed; not
  written as a proof here)"; REVIEW_PLD_S1_S2 requires it and REVIEW_PLD_S3 confirms B4 as applied in PLD's text. **Written
  proof: not yet** (item I-σ of §4.2, s).
- **(β)** The returned collar-bad configurations (σ_Q = 0 for some Q, n ≤ n_♯) are an explicit activity family 𝓗^{cb}_X(V) of
  (SC)_k (PLD §9.1 (β)), the sea average of their frozen weights. Its price is the three-way price of §3 (REVIEW_PLD_S3
  B-S3-7: coherent cut-good backgrounds make σ_Q = 0 on whole regions with zero mismatch and zero fluctuation, so the
  probability route alone does not price them).
- **(γ)** No Taylor extraction is applied pointwise in the level-k sample (R1 (ii)-(iii) are not applied to sea samples).
  Extraction is done after the sea average, in V, at V = 1 (Lemma W1R-sym + Lemma W1R-tay, PLD §9.2-§9.3, PROVEN-HERE,
  CONFIRMED-WITH-FIX), so that the extracted numbers are defined for every V and the chart condition enters only the bound on
  the remainder. The pointwise remainder's ε_V (the soft residual, O(g_k/√κ) in every sample) is integrated out.
  (W1R-tay is stated for one-field A_x(V); the joint route's two-field form is Conflict K3.)

---

## 3. The three-way price of a defect [v2-A]

**Principle (lead decision; REVIEW_PLD_S3 Part 5 and Recommendation).** Every defect of §2.3 created at stage k is priced
in-step by one of three branches. (PLD)_k is not an inductive hypothesis, and no look-ahead is used. The v1 route "(PLD)_k as
a hypothesis" is withdrawn because, as a torus-wide uniform statement, it is downstream of A5 (PLD-AF; REVIEW_PLD_S1_S2
Part 5), and the per-history (SG^ph)/(SG^net) contain every coarser scale (Finding 2, Proposition INH). The look-ahead route
of PLD §15.6 E4-E5 is withdrawn: PLD-desc does not reach step 6 (Arch-1), and its cascade ends at a bad coarse cube priced by
nothing in-step (Arch-2, Proposition CF) (REVIEW_PLD_S3: WRONG as an architecture).

### 3.1 Branch (i): kernel mismatch. Status: **PROVEN** (unconditional)
- **Statements used.** Lemma RS (R3)-(R4) (v1 §6; PROVEN-HERE, CONFIRMED by REVIEW_S16_S17): if ||1 - V_P|| ≥ ε_1 then either a
  level-k plaquette of U_4(P) is ≥ η_1 or some c ∈ ∂P has ||V_c - S_c|| ≥ ε_1/8, the latter of conditional probability
  ≤ ec_N^{-1}(κ/g²)^{N²-1}e^{-κε_1²/(256Ng²)}, multiplicative over distinct links. Lemma RS-lin (b)-(c) (HIST §3; CONFIRMED by
  REVIEW_HIST_S1): the same with η_q and exponent κε_1²/(1024N). Lemma KN with Corollary KN-step (EXISTENCE §13; CONFIRMED-
  WITH-FIX / CONFIRMED by REVIEW_X3_X4; KN is quadratic in the background defect, and removes RS's linear δ_c loss only with
  KN-step's re-centred dichotomy (RX34-fix 9), which v2 does NOT adopt for η_1 (E9)). CL^J (c) numerator (HIST §4, CONFIRMED-
  WITH-FIX): per bad cube a mismatch on some c ∈ int Q, exponent κε_1²/(1024N). PLD-SG (ii)/(iii) and §9.5 use KN at
  t = ε_loc/4 for the collar clause (exponent κε_loc²/(64N)).
- **Covers:** (D-a) on the mismatch side of the dichotomy; (D-b) on the mismatch side of the collar split (||V_c - W'_c|| >
  ε_loc/4, PLD §9.5); per link c independent given U (Lemma TD; under μ^+_{𝔥,ω}: product kernel).
- **In-history caveat.** With history indicators and G_k's U_{k+1}-dependent factor present, the conditional law of the
  int(Q) links is K_k tilted by e^{Σρ} (HIST H-1/H-4). The step "≤ e^{Σ|ρ|} × Πk^{(k)}_c" is ARGUED, not written (gap H-4).

### 3.2 Branch (ii): fluctuation about the background. Status: **PROVEN given (SG^fl)_k**
- **Statements used.** Proposition PLD-desc (PLD §15.3; PROVEN-HERE; CONFIRMED-WITH-FIX by REVIEW_PLD_S3, fix PD-1: read
  τ > 2τ_bg strictly, or define B_V with ">"): under (SG^fl)_k, for A ⊂ 𝒫°(𝔥), τ ∈ (0, ε_1],
    μ^+(||1 - U_p||_op ≥ τ ∀p ∈ A, V ∈ 𝒱^sf(A)) ≤ E_{μ^+}[1_{𝒱^sf(A)}(V)(C_fle^{-a_fl(τ/2)/g²})^{|A∖B_V|}],
  B_V := {p ∈ A : |X_p(𝔟(V))|_HS ≥ τ/2}; Lemma HS-net (PROVEN, CONFIRMED); Lemma TL (uncounted, CONFIRMED). PLD-SG (i)-(iii)
  (CONFIRMED) is retained as an **implication only** ((SG^net)_k ⇒ (PLD)_k on (M3)); REVIEW_PLD_S3: "record it as an
  implication, not as progress on (PLD)".
- **Domain.** Only on V ∈ 𝒱^sf(A) (every level-(k+1) plaquette within R_bg of A is < ε_1). Only for the plaquettes of A ∖ B_V
  (the fluctuation part). The background part B_V and the event V ∉ 𝒱^sf go to branch (iii) / to the level-(k+1) defect count.
- **(SG^fl)_k (PLD §15.2): HYPOTHESIS, a clause of (SF^J)_k's output; weight s given (SF) and (I_k^E) (PLD E6).** Inputs per
  PLD §15.2 table: (I_k^E) (fixes 𝔟(V) as the minimiser of 𝓔_k + kernel term given V), N5-sf0 (level 0, PROVEN [S19], the
  Gaussian part) and N5-sf_i ⇐ (NA-H_loc)_i (OPEN for i ≥ 2; Theorem NAH1 gives level 1, PROOF [S20]), (SF)_k's cluster
  expansion (OPEN, node A), threshold compatibility (§0), (BG)_k. At level 0 the passage from covariance to exponential moments
  needs (G0-1)-(G0-4) (PLD §15.4; CONFIRMED as a reduction).
- **(BG)_k (PLD §15.2): OPEN, part of (SF)/N2, s.** 𝔟(V) local with exponential tails (radius R_bg) and curvature
  ||X(𝔟(V))|| ≤ C_IL^{-2}max_{P nearby}||X_P(V)|| (+ quadratic). Under v2 only locality (R_bg) is load-bearing; the value of C_I
  decided only the withdrawn look-ahead depth (REVIEW_PLD_S3: "no longer decisive").
- **Scope fix SG-1 (E10).** (SG^fl) is stated on 𝒫°(𝔥); boundary-adjacent plaquettes need the extension of §2.3 (D-d).
- **What branch (ii) cannot see (why branch (iii) exists).** Proposition INH (PLD §15.3, CONFIRMED-WITH-FIX) with Proposition
  CF (HIST §6, CONFIRMED): cut-good level-(k+1) fields carry coherent level-k curvature up to ≈ ε/L² with zero kernel mismatch
  and zero fluctuation about their own background; every RS-compatible threshold has η_RS ≤ ε_1/L²(1 + o(1)), so no choice of
  thresholds puts η_RS in PLD-desc's in-step range (REVIEW_PLD_S3, INH structural strengthening).

### 3.3 Branch (iii): coherent background, by a pointwise chain-energy bound in ℒ_𝔥. Status: **ARGUED**
- **Statement (REVIEW_PLD_S3 Part 5 proposed text, ARGUED by that reviewer, not proven; adopted by the lead).** Under
  (I_k^E), the stage-k joint main term u_k[Σ_x𝓔_{k,x}(U) + κΦ_k(U, V)] restricted to the cone of a level-(k+1) plaquette P is
  ≥ u_kc_sf·min{||1 - V_P||², ε_1²} (CLS-sf, cone form). So a defect cube carries a factor ≤ e^{-u_kc_sfε_1²/C} (resp. ε_loc² for
  collar-bad) times the integrand with that cube's cone energy removed. That factor enters ℒ_𝔥 directly (Dimock II form), and
  the removed-cone integrand is the history in which the cube is large-field. No probability under the per-history law is
  needed, and no later step is consulted.
- **Why it is coherent (REVIEW_PLD_S3).** It sees CF's cost (CF (3): ≈ θ²/(2g_0²) per site; HIST l.403-412: aggregating bounds
  see CF, sup-threshold and fluctuation bounds do not); it is in-step because the CF preimage on the cone is level-k
  small-field (curvature ≈ ε_1/L² < ε_1); it is the form v1's Proposition CL (c) already uses at the bare level (Wilson
  positivity as the energy bound).
- **Inputs and their status.**
  - **CLS-sf in cone form.** HIST Theorem CLS-red (CONDITIONAL ⇐ (AE); CONFIRMED by REVIEW_HIST_S2): if E_𝒞(P) < η_E then
    |log U_k(P)|²_HS ≤ C_*E_𝒞(P), and s(U_k(P)) ≤ max{C_loc, 2/η_E}·E_𝒞(P) for every level-k field (strong form, per cone),
    hence E(chain) ≥ c_clΣ_Ps(U_k(P)). This is a per-cone bound on the **tree chain energy of a full chain**; the restatement in
    the cone-local form on the (I_k^E) main term, with RLARGE's η_1, is HIST session-3 Target S5 (pre-stated 01:00 UTC; not
    yet written at read time).
  - **(AE)** [OPEN; P] (HIST §15.3 restated form, RH2-fix S2-5/S2-7): its linear case is Lemma E-loc (PROVEN-HERE, CONFIRMED);
    its non-abelian content is the depth-uniform multiscale linearisation, with the gauge on the cone as the wall (CS-F2).
    (AE) ⇐ (MSG) + (MS-Sob) is [inference] (HIST §15.5). **(MSG)** (a depth-uniform local small-field gauge on cones) is HIST
    session-3 Target S4 (pre-stated; under attack). REVIEW_HIST_S2: the same (MSG) also discharges the gauge part of (I_k^E)'s
    GAPs S2-1 and S2-2.
  - **(I_k^E)** (HIST §14.1): HYPOTHESIS [P], with statement GAPs S2-1 (localised main term undefined on Λ_k), S2-2 (the
    single-gauge polydisc misses the ε_1-domain on large polymers), S2-3 (kernel normalisation not listed); repaired form
    (I_k^E)' announced for HIST §20.3 (not present at read time).
  - The removed-cone normalisation must be absorbed by the history bookkeeping (e^{B_0} per boundary cube), as for any new
    large-field region (REVIEW_PLD_S3) — part of (H-w).
- **Weight.** CLS-sf becomes a main-path wall [P] (REVIEW_PLD_S3 tally note: the weight of RLF-step's large-field pricing rises
  from s to P; the main-path OPEN count is unchanged).

### 3.4 Assignment of a defect to a branch, and the exponent a_♯
- **Case split (ARGUED; assembled from §3.1-§3.3, not written as a proof).** A level-(k+1) bad cube (D-a): RS (R3)/RS-lin (c)
  either gives a mismatch link (branch (i)) or a level-k plaquette ≥ η_1 (≥ η_q) in U_4(P); that plaquette is either a
  fluctuation about 𝔟(V) on V ∈ 𝒱^sf (branch (ii), A ∖ B_V) or carried by the background, B_V ≠ ∅ or V ∉ 𝒱^sf (branch (iii),
  the cone energy of P). A collar-bad cube (D-b, D-c): PLD §9.5's split at η_♭' gives a KN mismatch (branch (i)) or a plaquette
  of N_1(Q) ≥ η_♭', priced as above (branches (ii)/(iii)). Boundary-adjacent (D-d): open (E10).
- **Joint pricing over many cubes.** Greedy disjointness factors from the sources: 7⁴ (PLD-SG (ii), cube distance ≥ 4), 81
  (HIST RS-joint, non-*-adjacent cubes), 5⁴ (v1 §7.1 c_RS, ARGUED). RS-joint's c_RS = 81 is CONDITIONAL ⇐ (PLD-q)_k under the
  plain chain measure (CONFIRMED as CONDITIONAL, REVIEW_HIST_S1), in-history form ARGUED (H-4). **Under v2, (PLD-q)_k is not a
  hypothesis; its role is taken by branches (ii)+(iii), and branch (iii) is an integrand bound, not a probability, so
  RS-joint's probabilistic proof does not consume it as written** (Conflict K5).
- **The exponent.** a_♯ := min{a''_J (R1^J grading), a_ker := κε_1²/(1024N) or κε_1²/(256N) (RS-lin / RS), κε_loc²/(64N) (KN
  collar), a_fl(η/2) (branch (ii) at the threshold used), a_coh (branch (iii): u_kc_sf·min{η², ε_1²}-type, not yet a number)}
  divided by the greedy factor of the joint pricing. Every entry except a_coh is a stated constant in its source; a_coh waits for
  CLS-sf's cone form. The combination is ARGUED (as in v1, where a_♯ used c_RS = 5⁴, ARGUED). **No counted item depends on
  a_♯ or n_♯** (v1 §1A item 2 note; R1/R1^J hold for every cutoff n_c ≥ n_*, n^J_*).

---

## 4. The inductive step over levels

### 4.1 The representation (I_k^E) [v2-H; replaces v1 §8.1 (I_k)]
(I_k^E) (HIST §14.1, verbatim reference): for every admissible history 𝔥 and level-k configuration U with 1_𝔥(U) = 1, on the
small-field region Λ_k(𝔥),
  e^{-S_k(U)}|_𝔥 = e^{𝒱_k}·exp(-u_kΣ_{x∈Λ_k}𝓔_{k,x}(U) - Σ_{X⊂Λ_k}E_k(X; U))·ℒ_𝔥(U),
with (a) main term u_k𝓔_k (𝓔_k the soft-chain tree tower of HIST §14.0, β[𝓔_k] = 1 by Lemma HF + F-tree), (b) polymers with a
per-cube g-independent sup bound E_0 on a g-independent domain and β[ΣE_k] = 0, (c) large-field factor ℒ_𝔥 (v1 §8.1 bound, with
the three-way prices of §3 entering it), (d) the two-field stage-k form u_k[Σ_x𝓔_{k,x}(U_k) + κΦ_k(U_k, U_{k+1})] + polymers +
R1^J remainders + coupling-shift polymer. (I_0^E) holds (𝓔_0 = Σs, E_0 ≡ 0).
**Why not v1's (I_k):** (D1-c) and its broadening H-2 (HIST §6; CONFIRMED as ARGUED, REVIEW_HIST_S1): any per-cube-bounded
representation whose main term is the coarse Wilson action fails on every domain containing fields of size t with g ≪ t, which
includes the ε_1-small-field region. **Status of (I_k^E): HYPOTHESIS [P], statement GAPs S2-1, S2-2, S2-3** (REVIEW_HIST_S2;
target S2 MET-WITH-FIX).

### 4.2 Complete named-hypothesis list for RLF-step v2

| # | hypothesis (precise statement at) | owner file | status | weight |
|---|---|---|---|---|
| 1 | **(F_R)** along the chain's own sequence (§0) ⇐ Theorem F-flow ⇐ (UNIV-1L) ⇐ Theorem UNIV ⇐ (U-IR), (U-loc); plus (SF-g), (RLF-δ), (SF-cont), (SF-∞) | FLOW §4, §7, §18, §23 | F-flow, F-tune CONFIRMED conditional; (U-loc) PROVEN-HERE [S3, unreviewed]; (U-IR) OPEN [s-P] (REVIEW_FLOW_S1_S2: IR-term vertices, slice, longitudinal sector paper-scale) | **P** (node A5) |
| 2 | **(RLF-δ)_k** per level, from (F_R)_{[0,k]} only (§1.2) | this file (requirement FI-1, FLOW §4/§9) | delivered by (W1-ret'^J)_k (a)'s bound if that bound uses only g_k ≤ γ_0 (it does as stated; §4.4) | s (bookkeeping), given #5 |
| 3 | **(SF^J)_k**: small-field step integrating U_k against a density with polymers in (U_k, U_{k+1}, U_{k+2}), outputting two-field polymers in (U_{k+1}, U_{k+2}) on Λ_{k+1}, in the (I_{k+1}^E) form, **with level-uniform thresholds** [v2-C], and with the clauses (SG^fl)_k, (SF-irr)_{k+1}, (RLF-5)'s width | HIST §6, §8 (H-3); PROOF nodes N2, N4, N5, N6 (A1-A4) | OPEN; new in kind (REVIEW_HIST_S1) | **P×3-4** |
| 3a | **(BG-unif)** (level-uniform N5 thresholds; template REVIEW_S20 Part 2) | PROOF [S20] (NAH-ind), ⊂ B-NA | named, not precisely stated in PROOF (REVIEW_S20 fix 12) | **P** (cf. CMP 102) |
| 4 | **(I_k^E)** (§4.1) | HIST §14.1 (§20.3 repair pending) | HYPOTHESIS with GAPs S2-1..S2-3 | **P** (statement repair: s) |
| 5 | **(W1-ret'^J)_k** (a)-(c): sea average over U_k of the σ-restricted joint gas; c̄_0^{sea}, δβ_k at V = 1; returned remainders admissible two-field polymers; unreturned weights (C_ℓe^{-a_♯/g_k²})^{n} | HIST §8; PLD §9 (Proposition W1R) | W1R: (a)-(b) CONDITIONAL ⇐ (SC)_k + (SF-irr)_{k+1} (one-field form); (c) priced by §3 | **s to P** |
| 5a | **(SC)_k** (fixed-V sea expansion, with the collar-bad family 𝓗^{cb}) | PLD §9.4 | HYPOTHESIS ("close in strength to (W1-ret') (a)-(b)", REVIEW_PLD_S1_S2) | s to P |
| 5b | **(SF-irr)_{k+1}** (admissibility of C³, local, 𝔯^♭-bounded activities) | PLD §9.3 | HYPOTHESIS, part of node A | inside #3 |
| 6 | **(H-Mayer^J)_k**: whole-lattice Mayer expansion of G_k's U_{k+1}-dependent factor, two-field activities ≤ (Ce^{-a''_J/g_{k-1}²})^{#cubes}e^{-κ'd}, κ' > 3κ_0 + 3 | HIST §8 (H-1) | ARGUED (REVIEW_HIST_S1, S2) | s given #5 at k - 1 |
| 7 | **(SG^fl)_k** (branch (ii)) | PLD §15.2 | HYPOTHESIS, clause of #3 | s given (SF) and (I_k^E) |
| 8 | **(BG)_k** (locality radius R_bg of 𝔟(V)) | PLD §15.2 | OPEN, part of (SF)/N2 | s |
| 9 | **CLS-sf, cone form on the (I_k^E) main term** (branch (iii)) ⇐ CLS-red ⇐ (AE) ⇐ (MSG) + (MS-Sob) [inference] | HIST §15, Targets S4-S5 | CLS-red CONDITIONAL (CONFIRMED); (AE) OPEN; (MSG) under attack | **P** |
| 10 | **(H-w)**: per-history nonnegative weights with the (RLF-3) bound and B_0 per large-field cube per level, incl. the removed-cone normalisation of branch (iii) and (H-w)(c)'s per-cube normalisation mismatch (fragile: a log(1/g) per cube per level would make n_H infinite, RH1-fix H-11) | HIST §7.4 | OPEN | **P** (CMP 122 II's subject by title) |
| 11 | **(SF-last)**: level-K integrand as product measure × small activities, or a correlated-Gaussian cluster expansion | v1 §8.2 | HYPOTHESIS | s given (SF) |
| 12 | **H-4**: in-history form of the mismatch pricing (tilt e^{Σ|ρ|}) | HIST §7.3 | ARGUED | s |
| 13 | **E10**: pricing of boundary-adjacent defects (D-d) | this file (§2.3); PLD SG-1 | OPEN, unwritten | weight not assigned by any source (integrator's estimate: s) |
| 14 | **I-σ / I-σ^J**: written proof of the σ-restricted gas (bare: Lemma 7.2-0 with σ; joint: σ^J_Q stated and the per-cube ⇒ cluster implication for ε^J_♭) | this file / HIST | bare: substitution stated (PLD §9.1), proof unwritten; joint: not stated | s |
| 15 | **I-tay^J**: extraction after the sea average in the two-field joint form (W1R-sym/W1R-tay with GT-lat'' and C = the level-(k+2) links) | PLD / HIST | not written | s |
| 16 | **(RLF-5)** g-uniform complex width (shared with #4's S2-2) | node A | not shown; one activity ARGUED width O(g/√κ) | inside #3 |

Not hypotheses of RLF-step v2 (withdrawn or relocated): (H-pos)_k (relocated: Theorem H-pos^J, (D1-c)); (PLD)_k (i)-(ii),
(PLD-q)_k as inputs ([v2-A]); (PLD-dis), (NH), (WH), (INF) (torus-wide / existence-lane objects; (INF) is tracked in PLD §15.5
and EXISTENCE as one item, REVIEW_PLD_S3 INF-1); (CLS-NA) large-field and (D1-b) (not consumed; REVIEW_HIST_S1/S2: do not
attack); Theorem TS / TS_K (frozen shadows, not used by RLF-step).

### 4.3 Proposition RLF-step v2: (I_k^E) on Λ_k + #1-#16 ⇒ (I_{k+1}^E) on Λ_{k+1}. Status: **ARGUED**
(It is HIST's RLF-step^J — ARGUED with gaps H-1, H-3, H-4 and requirement H-2, REVIEW_HIST_S1 — with PLD's E2/E3 and the
three-way pricing in place of (PLD)_k.)
1. *Exact.* Stage k: insert the level-(k+1) indicators into J_k (RS ordering); the whole-lattice Mayer step of (H-Mayer^J)_k
   [#6]; CL^J (a)-(b) on the components (PROVEN-HERE, HIST §4): ⟨Ξ^J⟩_cut with the joint frozen gas, pointwise in U_k.
2. *Frozen R-step, σ-restricted.* R1^J (i) / R1_Λ on the σ-good part (§2.4 (α) [#14]), cutoff n_c = n_♯: convergent gas,
   graded logarithm, bounds (PROVEN-HERE for the (H-ch)^J-good region, HIST §5). **No pointwise Taylor extraction** (§2.4 (γ)).
3. *Sea average and re-extraction at V = 1.* (W1-ret'^J)_k (a)-(b) [#5, #5a, #5b, #15]: c̄_0^{sea}, δβ_k (one shift, hypercubic
   torus; W1R-sym), returned remainders as admissible two-field polymers, including the collar-bad family 𝓗^{cb} [§2.4 (β)].
4. *Unreturned configurations.* n(𝒟) > n_♯: weight (C_ℓe^{-a_♯/g_k²})^{n(𝒟)} by the three-way price (§3) [#7-#9, #12, #13].
5. *Small-field step.* (SF^J)_k [#3] integrates U_k on Λ_k against the (I_k^E) density [#4] with the shifted coupling (u_k →
   u_k - δβ_k, plus the β = 0 polymer δβ_k(Σs - 𝓔_k), HIST (c4)); needed only on Λ_{k+1} (Theorem H-pos^J (iii)); outputs the
   two-field (I_{k+1}^E) density, (SG^fl)_{k+1}, and the flow step.
6. *New level-(k+1) large fields.* Before U_k is integrated (RS ordering), each bad level-(k+1) cube is priced by §3 (branch (i)
   PROVEN; (ii) given (SG^fl)_k; (iii) ARGUED); returned or not by the level-(k+1) R-operation like any other defect.
7. *Nesting and assembly.* Lemma H-nest (PROVEN); the next stage's activities read only Λ_{k+1} data (collar property, width
   1). Assembly over k: (H-w) [#10] + Theorem HIST-sum (§5).
Constants (C_ℓ, B_0, E_0, a_♯, n_♯) are the same at every level; the flow constants β_-, R are fixed first (FLOW Lemma F-ind).

### 4.4 Non-circularity with FLOW (FI-1) [v2-F]
Lemma F-ind (FLOW §9; CONFIRMED-WITH-FIX) is non-circular only if (SF-g)_k and (RLF-δ)_k at level k use the flow on [0, k] only, along
the chain's own sequence. **What v2 delivers:** in steps 1-6 every constant at stage k depends on g_k (and g_{k±1} through
CL^J's hypothesis g_k ≤ g_{k+1} ≤ min{1, √κ}, see Conflict K4) and on fixed constants; the bound |δβ_k| ≤ Cg_k^{-p}e^{-a_♯/g_k²}
≤ g_k⁶ uses g_k ≤ γ_0 only. The quantities involving g_K — Σ_k|δβ_k|, (P1) = HIST-sum, (P5), (RLF-3)'s total — are used only
in the assembly (step 7) and in (RLF-4), never fed back into FLOW. n_♯ depends on β_- only, which F-ind fixes first
(β_- := β_0'/2) [inference: v2's n_♯ ≥ n_H also depends on B_0, a level-uniform constant of (H-w)]. **Status: the requirement
is met by the structure of steps 1-6 as stated; it is not a theorem until #3, #5 are proven with constants depending on
[0, k] only** (this is a requirement on those hypotheses' statements, recorded in their rows).

---

## 5. History sum (HIST §7, verbatim references)

### 5.1 Definitions (HIST §7.1; CONFIRMED by REVIEW_HIST_S1)
Projection π, collar N_ρ, one-step shadow Σ(A) := N_1(π(A)); history 𝔥 = (𝒰_0, …, 𝒰_{K-1}) of new unreturned sets;
Ω^c_k(𝔥) := ∪_{j≤k}sh_k(𝒰_j), Λ_k(𝔥) its complement; admissibility (A1) every component of 𝒰_k has > n_♯ cubes, (A2)
𝒰_k ∩ Σ(Ω^c_{k-1}) = ∅. Returned configurations are not part of the history. Lemma H-nest (i)-(iii) (PROVEN; nesting, collar
property of width 1, columns). The activity collar (width 1) and the Taylor-extraction collar (width ∝ n_c) are separated
(HIST §7.1 Remark); otherwise (HI-F1) would be met.

### 5.2 Theorem HIST-sum (HIST §7.4): CONDITIONAL ⇐ (H-w) + lower half of the flow; CONFIRMED (REVIEW_HIST_S1)
With c_B := 38416B_0/log L, **n_H := ⌊(4 + c_B)/(aβ_-)⌋**, γ_H := (n_H + 1)aβ_- - 4 - c_B > 0, n_♯ ≥ n_H and
6400C_ℓe^{38417B_0}e^{-a/g_K²} ≤ ½: Σ_{𝔥≠∅}Z(𝔥) ≤ Z^{sf}_K(exp(C_H|T|e^{-(n_♯+1)a/g_K²}) - 1), C_H := 2·6400^{n_♯}(C_ℓe^{38417B_0})^{n_♯+1}
/(1 - L^{-γ_H}), uniformly in K; and Z(∅) ≤ Z_K ≤ Z^{sf}_K exp(C_H|T|e^{-(n_♯+1)a/g_K²}). Inputs: Lemma H-geo (PROVEN; per-level
shadow ≤ 2401·16 cubes, cutoff-independent; observed 256 in h3), (g3), (H-w).
- **[v2-F] Under (F_R):** the proof's step (5) uses e^{-na/g_j²} ≤ e^{-na/g_K²}L^{-naβ_-(K-j)}; under (F_R) it acquires e^{naR},
  i.e. C'_ℓ → C'_ℓe^{aR} (FLOW §19A's (P1) row; integration arithmetic). n_H and γ_H are unchanged.
- **The logarithmic flow is load-bearing** (β_- = 0 diverges for every n; HIST §7.4).
- **[v2-H] Threshold.** v1's n_♯ := ⌊4/(a_♯β_-)⌋ is superseded: n_♯ ≥ max{n^J_*, n_H} (n_H reduces to v1's value at B_0 = 0).

### 5.3 (P1)-(P5) over K levels (HIST §7.5)
- **(P1)** = Theorem HIST-sum (CONDITIONAL); supersedes v1 (P1) (which did not count persistence of the regions).
- **(P2)** arithmetic PROVEN given the per-stage bounds: Σ_k|δβ_k| ≤ C'e^{a'''R}e^{-a'''/g_K²}/(1 - L^{-a'''β_-}); prefactor with
  β_+ (RN-2); the missing shift on extraction collars is a boundary term (HIST RH2-fix N-1: 12L⁸ per cube). Coupling shift read
  against 𝓔_k (HIST (c4)), with the sign of §0.
- **(P3)** arithmetic PROVEN: 𝒱^LF_K := Σ_kN_{k+1}c̄_0(g_k), field- and history-independent; history corrections ≤ C(n_♯)e^{-a''/g_k²}
  per cube of Ω^c, in B_0 (d).
- **(P4)** ARGUED (HIST RH1-fix H-2): re-based on (I_k^E)(b)'s per-cube E_0 and on (W1-ret')(b); Lemma P4-div (PROVEN, not
  counted) shows the bookkeeping-only version diverges ((HI-F4) MET for it).
- **(P5)** arithmetic PROVEN (v1 §8.4): composition with Theorem CE at level K needs g_K² < a_♯/(8(3κ_0 + 3)) and
  C_ℓe^{-a_♯/(4g_K²)} ≤ c(κ_0); applying CE needs (SF-last).

---

## 6. What is proven outright, and what is conditional

**PROVEN-HERE, reviewed (the frozen and one-step content; no hypothesis beyond stated parameter ranges):**
- v1 (Appendix A): Lemma GT-lat' (CONFIRMED); Proposition CL (CONFIRMED-WITH-FIX, CL-1 applied); Lemma RS (CONFIRMED); Theorem
  R1 with Lemma 7.2-0 + Theorem TS (repaired S18; CONFIRMED-WITH-FIX by REVIEW_S18_S19, F1/F2 applied S20, accepted by
  REVIEW_S20). Lemma LF-n arithmetic.
- HIST: Lemma PM (with KQ), Lemma RS-lin, Proposition CL^J, Theorem R1^J (with GT-lat'', Lemma 7.2-0^J, Corollary R1_Λ), Lemma
  H-geo (with H-nest) (REVIEW_HIST_S1: CONFIRMED / CONFIRMED-WITH-FIX); Lemma HF, Lemma E-loc (REVIEW_HIST_S2: CONFIRMED-WITH-
  FIX / CONFIRMED). Uncounted: Lemma TD, Proposition CF, Theorem H-pos^J, TS_K, Lemma P4-div, (P2), (P3).
- PLD: Proposition SHADOW, Lemmas W1R-sym + W1R-tay (CONFIRMED-WITH-FIX); Lemma HS-net + Proposition PLD-SG (CONFIRMED);
  Proposition PLD-desc + Proposition INH (CONFIRMED-WITH-FIX, INH-1, PD-1). PLD-SG and PLD-desc are implications from (SG)
  hypotheses.
- EXISTENCE: Lemma KN (CONFIRMED-WITH-FIX), Corollary KN-step (CONFIRMED) (REVIEW_X3_X4).
- **Branch (i) of §3 is proven unconditionally** (plain chain measure; in-history form ARGUED, H-4).

**CONDITIONAL (implication proven, hypotheses named):**
- Branch (ii) of §3 ⇐ (SG^fl)_k (PLD-desc).
- Theorem HIST-sum ⇐ (H-w) + the lower half of the flow; Lemma RS-joint ⇐ (PLD-q)_k (plain measure); Theorem CLS-red ⇐ (AE);
  Proposition W1R ⇐ (SC)_k + (SF-irr)_{k+1}; FLOW Theorems F-flow, F-tune ⇐ (UNIV-1L), (SF-g), (RLF-δ) (+ (SF-cont), (SF-∞)).

**ARGUED:** branch (iii) of §3; the case split §3.4; (H-Mayer^J); (P4); RLF-step v2 (§4.3); (D1-c) and H-2 (coarse-Wilson forms
false); the Laplace link; (RLF-5) width for one activity; RS-joint in-history (H-4).

**OPEN / HYPOTHESIS (the §4.2 list):** (F_R)'s inputs (U-IR) etc. [P]; (SF^J)_k [P×3-4] with (BG-unif) [P]; (I_k^E) [P]; CLS-sf
cone form / (AE) / (MSG) [P]; (H-w) [P]; (W1-ret'^J) with (SC) [s to P]; (SG^fl), (BG), (SF-last), (H-Mayer^J), H-4, E10, I-σ,
I-σ^J, I-tay^J [s].

**Theorem RLF (§1.2): OPEN**, reduced to the §4.2 list (by induction on k with (I_0^E), steps 1-7, HIST-sum, (P2)-(P5), and
(SF-last) + Theorem CE at level K). L5 stays IMPORTED-NOT-YET-REVERIFIED in PROOF (CMP 122 not read); RLF is the re-derivation
target that would replace it.

---

## 7. Critical-path DAG (open items → UV stability for the soft RG)

Target: **L6-soft** (UV stability), exp(-E_-|T|) ≤ Z_K/Z_K^{ref} ≤ exp(E_+|T|) uniformly in K (REVIEW_S15_CONVERGENCE (b)).
**P** = paper-scale, **s** = session-scale; ✓ = proven (reviewed); (C) = conditional implication proven.

```
L6-soft ⇐ RLF (§1.2: RLF-1 + RLF-3 + RLF-4) + node A bulk bound + C (assembly, P: CMP 119)
RLF ⇐ induction over k: RLF-step v2 (§4.3, ARGUED) + HIST-sum (C) + (P2)(P3)(P5) ✓arith + (SF-last) [s] + Theorem CE ✓
RLF-step v2
 ├─ exact rewriting: CL^J ✓, R1^J/R1_Λ ✓ ── σ-restricted gas I-σ, I-σ^J [s] ◄── SHADOW ✓ (forces σ_Q)
 ├─ (H-Mayer^J)_k [s, ARGUED] ◄── (W1-ret'^J)_{k-1}
 ├─ (W1-ret'^J)_k [s to P] ◄── (SC)_k [s to P] + (SF-irr)_{k+1} (⊂ A) + W1R-sym/W1R-tay ✓ + I-tay^J [s]
 ├─ defect prices (§3)
 │   ├─ (i) mismatch: RS ✓, RS-lin ✓, KN ✓   (in-history tilt H-4 [s, ARGUED])
 │   ├─ (ii) fluctuation: PLD-desc ✓ (C) ◄── (SG^fl)_k [s given SF, I^E] ◄── (SF^J)_k, (BG)_k [s], N5-sf_i ◄── (NA-H_loc)_i
 │   ├─ (iii) coherent: chain-energy bound in ℒ_𝔥 [ARGUED] ◄── CLS-sf cone form [P]
 │   │        ◄── CLS-red (C) ◄── (AE) [P, OPEN] ◄── (MSG) [P?; HIST S4, under attack] + (MS-Sob) [inference]
 │   │        ◄── (I_k^E) localised main term (GAP S2-1) ◄── (MSG) (shared, REVIEW_HIST_S2)
 │   └─ boundary-adjacent defects E10 [OPEN; weight unassigned]
 ├─ (I_k^E) [P; GAPs S2-1..S2-3, statement repair s] ◄── (SF^J)_k
 └─ (SF^J)_k [P×3-4 = node A1-A4: N2 (⇐ B-NA), N4, N5 (levels ≥ 2 via (BG-unif) [P]), N6] + (RLF-5) width
(H-w) [P] ── analytic half of the history (feeds HIST-sum, RLF-3, existence lane's (RLF-3^dis))
(F_R) along the chain's sequence [P, node A5] ◄── F-flow (C) ◄── UNIV-1L ◄── Theorem UNIV (C) ◄── (U-IR) [s-P], (U-loc) [s, proven S3 unreviewed]
     + (SF-g), (SF-cont), (SF-∞) (⊂ node A) + (RLF-δ)_k (from this file, per level; FI-1)
```

**Paper-scale nodes on this path:** node A (A1 N2/B-NA, A3 N5 incl. (BG-unif), A4 N6) = (SF^J); (I_k^E) (new in kind, part of
what (SF^J) outputs); CLS-sf cone form via (AE)/(MSG); (H-w); A5 (F_R) via (U-IR)'s vertex/slice/longitudinal parts; C
(assembly). **Session-scale:** I-σ, I-σ^J, I-tay^J, (H-Mayer^J), (SG^fl) given (SF), (BG)_k, (SF-last), H-4, E10 (estimate),
the (I_k^E) statement repairs, (U-loc) review. **Proven and not on the open path:** everything in §6's first block.
**Shared object:** (MSG) discharges the gauge part of (AE), (I_k^E) S2-1 and S2-2 (REVIEW_HIST_S2), and plausibly the
gauge-covariant complex domain of (RLF-5) [inference].

---

## 8. Integration conflicts (for the lead)

- **K1 (sign of δβ).** HIST (c4) [RH2-fix 9]: adding +δβΣs to log e^{-S} is u_k → u_k - δβ. v1 §8.3 wrote "1/g̃_{k+1}² =
  flow(1/g̃_k²) + δβ_k^{sea}" with R1 (iii)'s +δβ_jΣs in log Ξ; FLOW's (SF-g) FR-2 fix matched v1's "+δβ_k". **v2 adopts
  HIST's sign** (§0; δβ defined as in R1 (iii)); FLOW (SF-g)'s sign should be re-checked by its owner. No bound changes (|δβ|).
- **K2 (joint collar clause).** SHADOW + E2 require a LOCAL collar clause; HIST's joint route defines collar-badness via non-
  quietness and per-cluster ε^J_♭ (and its §6 bullet says non-quiet cubes "violate (H-ch)^J, so they are collar-bad", i.e. it
  names the (H-ch)^J failure as the reason). The joint σ^J_Q, with "σ^J ≡ 1 on Y ⇒ ε^J_♭(D; Y) ≤ ε^J_loc", is not stated (the
  completion uses kernel maximisers W_0, not the sample's links, so PLD's argument does not transfer verbatim). Chosen: local
  per-cube reading (§2.2) pending item I-σ^J.
- **K3 (extraction after averaging vs R1_Λ).** HIST RLF-step^J step 2 applies R1_Λ's Taylor extraction pointwise in the sample
  (with an extraction-collar cost ≲ C(n_♯)C^J_*g_k^{-6}e^{-a''_J/g_k²} per in-sea collar-bad cube); E3 (adopted) forbids
  pointwise extraction. Chosen: E3. The two-field joint form of W1R-tay is not written (I-tay^J). Not checked by any source:
  whether the extraction-collar cost of HIST's version is summable over levels (a single-cube cost with exponent ≈ a''_J plus
  the cost of an (H-ch)^J failure is the LF-count-type sum); under E3 the cost does not arise in that form.
- **K4 (one-step monotonicity in HIST).** CL^J, RS-lin, Theorem H-pos^J assume g_k ≤ g_{k+1} ≤ min{1, √κ}; REVIEW_FLOW_S1_S2 RN-1
  says one-step monotonicity is not implied by (F_R). HIST is not in FLOW's §19A consumer map. Chosen: read the hypothesis as
  g_k² ≤ g_{k+1}²·(1 + O(Rg²)) with factors e^{aR} (as for RS); the HIST owner should confirm where g_k ≤ g_{k+1} is load-bearing
  (CL^J (c) uses it in (3.1) and the C(Y) sup).
- **K5 (RS-joint vs the three-way price).** RS-joint (c_RS = 81) is a probability product consuming (PLD-q)_k; v2 removes
  (PLD-q)_k and branch (iii) is an integrand factor, not a probability. The greedy combination of an integrand bound with
  probabilistic branches over many cubes is not written; §3.4 records it as ARGUED.
- **K6 (thresholds).** Three thresholds coexist: RS's η_1 (E9, adopted), RS-lin's η_q (joint route), PLD's withdrawn c_1ε_1.
  HIST Target S5 states CLS-sf with RLARGE's η_1; the joint route consumes η_q. Since η_1 ≤ η_q unless δ_0/A_d binds, a price at
  η_1 covers η_q; if the cap binds the order should be re-checked.
- **K7 (complex domain).** (RLF-5) (v1) and (I_k^E)(b) (GAP S2-2) both need a g-independent gauge-covariant complex domain on
  the ε_1-domain; FLOW's (SF-bg) is stated on a neighbourhood of the trivial field only (REVIEW_HIST_S2). Not reconciled; recorded
  as one object (#4, #16).
- **K8 (existence lane's (RLF-3^dis) reading).** EXISTENCE §13.5/§13.9 asks RLF-3 to be stated as nonnegative ratios to Z_K^{ref};
  v2's (RLF-3) is HIST's (H-w) form, nonnegative, as a ratio to Z_K^{sf} (with Z_K/Z_K^{ref} two-sided by (RLF-1), (RLF-4) and
  node A). Whether this makes (RLF-3^dis) "a literal instance" is for the existence lane to confirm; v2 does not edit EXISTENCE.
- **K9 (tori).** E7 requires hypercubic tori for one shift; EXISTENCE ES1 allows a different time side ℓ_0 (PLD §12 item 4).
  If the existence lane consumes RLF on such tori, RLF must allow two (electric/magnetic) shifts. Not reconciled.
- **K10 (v1 §8.5 / §11 weights).** v1 weighted (PLD) [s given SF] and (HIST) [P]; v2 removes (PLD) and adds CLS-sf [P]
  (REVIEW_PLD_S3); v1's "(W1-ret') [s to P]" is kept. v1 §10's tally text and §12 (68 → …) are history in the snapshot; this file
  makes no tally claim.

---
# Appendix A. Frozen and one-step content of v1 (§3-§9A), verbatim from RLARGE_v1_snapshot.md l.194-580 and l.723-758

**v2 reading notes (the text below is not edited; read it with these notes).**
- **§3 (definition of the R-operation), l.208-219:** under v2 the R-operation is run on the σ-restricted gas (§2.4 (α)); "split
  each connected term … into c-number + quadratic part + remainder" is done after the sea average at V = 1 (§2.4 (γ)), not in
  the sample; cutoff n_♯ ≥ max{n^J_*, n_H} (§5.2).
- **§5 Proposition CL, l.254-314:** unchanged (bare level). CL (c)'s hypothesis ε_♭ ≤ ε_loc is supplied per cluster by σ ≡ 1
  (§2.2) in place of (H-ch).
- **§6 Lemma RS, l.316-361:** "1/g_i² ≥ 1/g_{i+1}² under (F)" (l.354) is not implied by (F_R): factor e^{a_RS R} (§0). η_1 here is
  v2's η_1 (E9). "the large-deviation hypothesis (PLD) of §8" (l.356) is replaced by branches (ii)-(iii) of §3.
- **§7.1, l.365-379:** n_* unchanged; a_♯, c_RS = 5⁴ and n_♯ := ⌊4/(a_♯β_-)⌋ are superseded by §3.4 and §5.2.
- **§7.2 Theorem R1, l.381-510:** (i) is used with σ in place of (H-ch) (§2.4 (α), item I-σ); (ii)-(iii) are not applied
  pointwise in sea samples (§2.4 (γ)); (iv) l.482 "g_j ≤ g_K by (F)" reads g_j² ≤ g_K²/(1 - Rg_K²) (§0). The Reading l.500-510
  stands.
- **§7.3 Theorem TS, §7.4:** frozen-background shadow; not used by RLF-step v2 (as v1 l.555-557 says).
- **§8 (l.582-721) is NOT reproduced:** it is superseded by §4-§5 of v2 (map in §1.3); see the snapshot l.582-721.
- **§9, §9A (checks c32, c33):** records, unchanged.

</content>
</invoke>

## 3. The R-operation in the soft setting: what it is (definition-level, exact)

The soft kernel makes the RG an exact Markov chain with positive integrand, so the R-operation can be formulated as an
exact rewriting of one RG step, with no constraint fibres (W3 absent). Fix a level j and write U for the level-j field,
V for the level-(j+1) coarse links, e^{-S}(U) := e^{-S_j(U)}·K_j(V, U) for the step-j integrand (bare form: S_j = Wilson
at g := g_j, as in R4D-iso; effective levels: §8).

- **Notation.** For a set B of level-j cubes, int(B) := the links with both ends in one cube of B; C(B) := the coarse
  links with an endpoint block in B (≤ 8|B|); w_B(U_{int B}; D) := exp(-(1/g²)Σ_{p∩int B≠∅}s(U_p))·Π_{c∈C(B)}k_c, where
  D := U restricted to the links outside int(B), together with V. Every factor of e^{-S} that involves an int(B) link is in
  w_B, so e^{-S} = w_B·w_rest with w_rest independent of U_{int B}.
- **Frozen cluster activity.** r_B(D) := Num_B/Den_B, Num_B := ∫Π_{Q∈B}ζ_Q w_B dU_{int B}, Den_B := ∫Π_{Q∈B}χ_Q w_B dU_{int B}.
  For |B| = 1 this is R4D-iso's ρ (with the D4-norm kernel).
- **The R-operation at level j** (definition). Expand Π_Q(χ_Q + ζ_Q) = Σ_BΠ_{Q∈B}ζ_QΠ_{Q∉B}χ_Q, pass to the frozen activities
  (Proposition CL (a)), take the logarithm of the resulting hard-core gas (Theorem R1 (i)), and split each connected
  term of total cube number N ≤ n_* into (its value at trivial data: a c-number) + (its Ad-invariant quadratic part: after
  B_4-averaging, a coupling shift) + (a remainder of irrelevant order) **[R1617-fix R-6: a remainder of order 𝔯(D) (§7.2);
  this is irrelevant for BG-b-regular frozen data only; in a sea sample it is O(g²) relative to the extracted terms and
  must be re-extracted after the sea average, §8.2 (W1-ret'). R-3b: the connected terms are localised at the base points
  of their UNFATTENED supports, §7.2 (iii). R-1: in the induction the cutoff is n_♯ and collar-bad configurations are
  returned too, §1A.]**. The c-numbers are the vacuum counterterm, the
  quadratic parts are "returned" to the small-field action as the coupling shift δβ_j, and the remainders are small
  local insertions. Terms with N > n_* are kept unrenormalised (they are summable: Lemma LF-n). This is the soft-kernel
  form of "converting large-field contributions back to small-field contributions" (Dimock II p.31 [read]); whether it
  coincides with Balaban's construction is unknown [CMP 122 not-read].

## 4. Lemma GT-lat' (lattice Taylor lemma without point symmetry; B_4 orbit averages): PROVEN-HERE [S17]

*Setting.* As GT-lat (PROOF L5 [S9]): box B̂ = {|x_μ| ≤ R_0} about a block centre 0, R̂ its links, complete-axial tree
paths π_x from 0, P̂_p := log(hol(π_x)U_p hol(π_x)^{-1}), Φ(D) := (P̂_{(0;μ,ν)})_{μ<ν}, ε_2, ε_3 as there. Two changes:
(1) C is ANY finite set of coarse links c (straight segments of length L between block centres inside B̂), not
necessarily from 0 or B_4-symmetric; ε_V := max_{c∈C}||log(V_cS_c^{-1})||_op, S_c the straight fine transporter along c.
(2) F is C³ on {ε_2 + ε_V ≤ r_1} and invariant under all gauge transformations of the data; **no B_4 or ι invariance**.

*Claim.* (i) Put Q_F(Φ) := ½D²F̃_rad(0)(𝓛Φ, 𝓛Φ) (GT's radial chart, 𝓛 GT's linear map). Then Q_F is Ad-invariant, so
Q_F(Φ) = Σ_{a,b}t^F_{ab}⟨Φ_a, Φ_b⟩_HS for a real symmetric 6 × 6 matrix t^F (a, b label the planes μ < ν), and
  |F(D) - F(1) - Q_F(Φ(D))| ≤ C K_F 𝔯(D),  𝔯 := ε_2(ε_3 + ε_V) + (ε_3 + ε_V)² + ε_2³,
with K_F as in GT-lat and C = C(R_0, C).
(ii) For R ∈ B_4 (about 0), (R·D) the rotated data and F∘R(D) := F(R·D): t^{F∘R} = Λ²(R)^T t^F Λ²(R). If a finite family
{F_i} is permuted by D ↦ R·D for every R ∈ B_4, then Σ_iQ_{F_i}(Φ) = c̄·Σ_a||Φ_a||²_HS with c̄ := (1/6)Σ_i tr t^{F_i}.

*Proof.* (i) GT-lat steps 1-3 hold with one addition. In tree gauge a coarse link c from x to x' has S_c = hol of the
closed loop π_x c π_{x'}^{-1}, which bounds a lattice surface of at most A(R_0) plaquettes in B̂ (the box's 2-complex is
simply connected; the count is combinatorial). As for U_b in GT-lat step 1, ||log S_c|| ≤ Cε_2 and
log S_c = Σ±P̂_{p_i} + O(ε_2²). Use the tree coordinate Y_c := log V_c; then ||Y_c|| ≤ ε_V + Cε_2 + Cε_Vε_2. For the
reference data put V^Φ_c := S_c(D^Φ) (so ε_V(D^Φ) = 0). Since log S_c(D) - log S_c(D^Φ) = Σ±(P̂_{p_i}(D) - P̂_{p_i}(D^Φ)) +
O(ε_2²) and ||P̂_p(D) - P̂_p(D^Φ)|| ≤ ε_3 + Cε_2² (GT-lat step 2), |Y_c(D) - Y_c(D^Φ)| ≤ C(ε_V + ε_3 + ε_2²). So step 2's two
estimates |Z(D) - Z(D^Φ)| ≤ C(ε_3 + ε_2² + ε_V), |Z(D^Φ)| ≤ Cε_2 hold. Step 3 is unchanged: a constant gauge
transformation acts on every tree coordinate (links and coarse links) by Ad, so DF̃(0) = 0. Step 4 without B_4: F(D^Φ) =
F̃_rad(𝓛Φ) = F(1) + Q_F(Φ) + R_3 with |R_3| ≤ CK_Fε_2³; D²F̃_rad(0) is Ad-invariant and 𝓛 is Ad-equivariant, so Q_F is
Ad-invariant. Ad-invariant symmetric bilinear forms on su(N) ⊗ R⁶ are ⟨·,·⟩_HS ⊗ t, because su(N) is absolutely
irreducible under Ad (End_Ad(su(N)) = R), exactly as in GT step 5. Combine as in GT-lat step 5.
(ii) GT-lat step 4 proves R·(𝓛Φ) = 𝓛(Λ²(R)Φ) exactly on the lattice (coarse straight links map to coarse straight links).
Hence Q_{F∘R}(Φ) = Q_F(Λ²(R)Φ), i.e. t^{F∘R} = Λ²(R)^Tt^FΛ²(R). If the family is permuted, T := Σ_it^{F_i} commutes with
Λ²(R) for every R ∈ B_4. Λ²R⁴ is absolutely irreducible under B_4 (GT step 5; c19 P1), so T = (tr T/6)·1. ∎

*Remark.* (i) is the general (non-symmetric) cluster version of GT-lat: a cluster of cubes has no point symmetry, and its
quadratic part is a general Ad-invariant form. (ii) says the B_4-orbit sum of the shapes restores a single invariant.

## 5. Proposition CL (frozen cluster activities): PROVEN-HERE [S17]

*Setting.* §3, bare form at level j (Wilson at g, normalised soft kernel D4-norm), g ≤ min(1, √κ). Constants:
n_ℓ := 4L³(L - 1) (links with both ends in one block), n_P := 6n_ℓ, A_d(L) := (d - 1)L(L - 1)/2 (Lemma RS), p_L := 5L - 4
(contour length, NA-lev), r := ε_1/16, c_N the Haar-ball constant (μ{||U - 1|| ≤ δ} ≥ c_Nδ^{N²-1}, δ ≤ 1),
  b_1 := n_P + 12κ(1 + A_d(L))²,  b_0 := 16n_P + 12κp_L²,  ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}.
For a cluster Y, N_1(Y) := the sites of the blocks of Y and of their *-neighbours, and the **completion parameter**
  ε_♭(D; Y) := min over U° ∈ SU(N)^{int Y} of [max_{p ⊂ N_1(Y)}||1 - U°_p||_op + max_{c∈C(Y)}||V_c - S_c(U°)||_op]
(U° completes D on int(Y); the minimum is attained by compactness).

*Claims.*
- (a) **Exact Fubini identity.** For every set B of cubes, Z_B/Z_∅ = ⟨r_B⟩_cut, where Z_B := ∫Π_{Q∈B}ζ_QΠ_{Q∉B}χ_Q e^{-S},
  ⟨·⟩_cut is the all-cut probability measure, and r_B is evaluated on the sample's links outside int(B). Hence
  Z/Z_∅ = ⟨Ξ⟩_cut with Ξ(U) := Σ_B r_B(U) (the frozen gas, evaluated on one sample).
- (b) **Factorisation.** If Y_1, …, Y_m are the *-components of B, then r_B = Π_ir_{Y_i}.
- (c) **Size, per cube uniform.** If ε_♭(D; Y) ≤ ε_loc then, for every *-connected Y of ANY size,
  r_Y(D) ≤ (C_r g^{-p_r} e^{-ε_1²/(4Ng²)})^{|Y|},  p_r := (N² - 1)(n_ℓ + 16),
  C_r := e^{b_0r²}c_N^{-(n_ℓ+8)}e^8κ^{8(N²-1)}r^{-(N²-1)n_ℓ}.
- (d) **Derivatives.** In the tree (or any local Lie) coordinates z of the data, for q ≤ 3 and coordinates z_1..z_q,
  |∂_{z_1}···∂_{z_q}r_Y| ≤ B_q(Λ_1/g²)^q r_Y, Λ_1 := 6 + 8κ(2 + C_𝒩) **[R1617-fix CL-1: was 6 + κ(2 + C_𝒩), asserted;
  the per-link multiplicity 8 is derived in the proof]** (C_𝒩 := Λ'/κ with Λ' from D4-norm (3)), B_q combinatorial.
- (e) **Invariance.** r_Y is invariant under all gauge transformations of D, covariant under translations and under B_4
  about any block centre: r_{RY}(R·D) = r_Y(D).

*Proof.* (a) Z_B = ∫(Π_{Q∉B}χ_Q)w_rest·Num_B: the indicators χ_Q, Q ∉ B, involve only interior plaquettes of Q, hence no
int(B) link. Integrating the all-cut integrand over U_{int B} gives (Π_{Q∉B}χ_Q)w_rest·Den_B. So
Z_B = ∫(Π_{Q∉B}χ_Q)w_rest Den_B·r_B = Z_∅⟨r_B⟩_cut, because r_B depends only on links outside int(B). Sum over B (finite). ∎
(b) For *-separated Y, Y': a plaquette meeting int(Q) has all vertices within sup-distance 1 of the sites of Q, while the
sites of non-touching blocks are at sup-distance ≥ L + 1 ≥ 4; so no plaquette meets both int(Y) and int(Y'). A coarse link's
contours lie in its two endpoint blocks, which touch; so no coarse link is in C(Y) ∩ C(Y'). Hence w_B = Πw_{Y_i} in
disjoint variables, and the indicators factorise. ∎
(c) *Numerator.* On Π_{Q∈Y}ζ_Q every Q ∈ Y has an interior plaquette p_Q with ||1 - U_{p_Q}|| ≥ ε_1, so by (B)
s(U_{p_Q}) ≥ ε_1²/(2N). The p_Q are distinct (disjoint interiors) and all other Wilson terms are ≥ 0, so the Wilson factor is
≤ e^{-|Y|ε_1²/(2Ng²)}. Each k_c ≤ e c_N^{-1}(κ/g²)^{N²-1} (D4-norm (2)), |C(Y)| ≤ 8|Y|, Haar mass 1. *Denominator.* Let U°
attain ε° := ε_♭(D; Y) ≤ ε_loc; restrict to the caps ||U_b - U°_b|| ≤ rg (b ∈ int Y). A plaquette meeting int(Y) has
≤ 4 interior links, so ||1 - U_p|| ≤ ε° + 4rg ≤ ε_1/4 + ε_1/4 < ε_1: every χ_Q = 1, and s(U_p) ≤ ½||1 - U_p||² ≤
(ε°)² + 16r²g²; there are ≤ n_P|Y| such plaquettes. Each kernel term is the mean over contours of
1 - N^{-1}Re tr(V_c^{-1}T^σ_y(U)) ≤ ½||V_c - T^σ_y(U)||² (unitary words; D4-norm's linearity remark), and
||V_c - T^σ_y(U)|| ≤ ||V_c - S_c(U°)|| + ||S_c(U°) - T^σ_y(U°)|| + ||T^σ_y(U°) - T^σ_y(U)|| ≤ ε° + A_d(L)ε° + p_Lrg, by the
ribbon bound of Lemma RS (all plaquettes of the two endpoint blocks lie in N_1(Y)) and p_L ≤ 5L - 4 links per contour.
With (x + y + z)² ≤ 3(x² + y² + z²) and 𝒩 ≤ 1: g²S ≤ |Y|(b_1(ε°)² + b_0r²g²) on the caps. Haar caps give
(c_N(rg)^{N²-1})^{n_ℓ|Y|}. Divide; b_1(ε°)² ≤ ε_1²/(4N) gives the exponent ≥ |Y|ε_1²/(4N). ∎
(d) The data enter polynomially through the Wilson terms (each link in ≤ 6 plaquettes, |∂s(U_p)| ≤ 1) and through the
kernel (|∂ of (κ/g²)(1 - N^{-1}Re tr V^{-1}M̄)| ≤ κ/g² per contour-mean; log 𝒩 by D4-norm (3)); the indicators do not
depend on D. **[R1617-fix CL-1] Multiplicity.** The contours of c = (X, X + e_μ) lie in B(X) ∪ B(X + e_μ) and cross
between the two blocks only along e_μ. So a fine link inside one block B lies in contours of at most the 2d = 8 coarse
links with an endpoint block B, and a link joining B to B + e_ν lies in contours of the coarse link (B, B + e_ν) only. A
fine data link therefore enters at most 8 kernel factors, each through the contour mean (first-derivative factor
≤ 2κ/g²: a contour may back-track along e_μ where its axial part meets the straight leg, as in Lemma RS (R1), so a link
occurs in one contour at most twice, once in each block; M̄_c is a mean) and through log 𝒩(M̄_c) (≤ Λ'/g² = κC_𝒩/g², D4-norm
(3)); a coarse link V_c enters one kernel factor (same bounds). With the 6 Wilson terms: first derivatives of the exponent
are ≤ (6 + 8κ(2 + C_𝒩))/g² = Λ_1/g², and the q-th derivatives of the exponent obey the same bound with a q-dependent
combinatorial factor, absorbed in B_q. Derivatives of the ratio of two positive integrals with D-independent indicators are joint cumulants of
bounded variables under two probability measures, as in R4D-iso step 3. ∎
(e) As R4D-iso step 1 (change of variables on int(Y), Haar invariance; the S4' family and the cuts are B_4-symmetric, L1
re-checks). ∎

*Remark.* (c) is uniform in |Y| because the denominator caps are placed around a completion of the given data, not
around 1 in a tree gauge (whose constants grow with the box). It is the frozen form of the Peierls bound that LF-count's
failure mode (RLF-F1) asks about: **the exponent of a frozen cluster of n bad cubes is ≥ n·ε_1²/(4N) (minus a polynomial
g-loss per cube).** RLF-F1 is AVOIDED in the frozen setting.

## 6. Lemma RS (one-step re-seeding of a coarse large field): PROVEN-HERE [S17]

*Setting.* One soft step from level i to level i + 1 (any i; no hypothesis on S_i). A level-(i+1) plaquette
P = (X; μ, ν) with coarse links c_1 = (X, X+e_μ), c_2 = (X+e_μ, X+e_μ+e_ν), c_3 = (X+e_ν, X+e_μ+e_ν), c_4 = (X, X+e_ν);
V_P := V_{c_1}V_{c_2}V_{c_3}^{-1}V_{c_4}^{-1}. U_4 := the union of the four blocks B(X), B(X+e_μ), B(X+e_ν), B(X+e_μ+e_ν);
η := max{||1 - U_p||_op : p a fine plaquette with all vertices in U_4}. S_c the straight transporter between the block
centres; δ_c := max_{σ,y}||T^σ_y - S_c||_op over the S4' contours of c.

*Claim.*
- (R1) **Ribbon bound.** δ_c ≤ A_d(L)η, A_d(L) := (d - 1)L(L - 1)/2 (= 9 for d = 4, L = 3); hence ||M̄_c - S_c|| ≤ A_d(L)η.
- (R2) **Square bound.** ||1 - S_P|| ≤ L²η, S_P := S_{c_1}S_{c_2}S_{c_3}^{-1}S_{c_4}^{-1}; hence
  ||1 - V_P|| ≤ L²η + Σ_{i=1}^4||V_{c_i} - S_{c_i}||.
- (R3) **Dichotomy.** Put η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}. If ||1 - V_P|| ≥ ε_1 then either η ≥ η_1, or η < η_1
  and some c ∈ ∂P has ||V_c - S_c|| ≥ ε_1/8.
- (R4) **Kernel branch, unconditional.** For every U with δ_c(U) ≤ A_d(L)η_1 and g² ≤ κ,
  ∫_{||V_c - S_c|| ≥ ε_1/8} k_c(V_c, U) dV_c ≤ e c_N^{-1}(κ/g²)^{N²-1} e^{-κε_1²/(256Ng²)},
  and for distinct coarse links the bound multiplies (k = Π_ck_c is a product of conditional densities).
- (R5) **Plaquette branch.** On {η ≥ η_1} some plaquette of U_4 has s(U_p) ≥ η_1²/(2N) (inequality (B)).

*Proof.* (R1) Lasso: if a closed loop ℓ is built by successively attaching plaquettes, hol(ℓ) = Π_iw_iU_{p_i}^{±1}w_i^{-1},
and ||ab - 1|| ≤ ||a - 1|| + ||b - 1|| for unitaries gives ||hol(ℓ) - 1|| ≤ Σ_i||U_{p_i} - 1||. Now T^σ_yS_c^{-1} is the holonomy
of the loop γ·leg(y)·(γ + Le_μ)^{-1}·leg(c_X)^{-1}, where γ = s_1…s_m is the order-σ axial path c_X → y and leg(z) the
straight path z → z + Le_μ; S4' pairing (the same σ at both ends) and translation covariance of P^σ make the far-end path
the translate γ + Le_μ. With γ_t := s_1…s_t and ℓ_t := γ_t·leg(z_t)·(γ_t + Le_μ)^{-1}·leg(c_X)^{-1}, inserting
hol(leg(z_{t-1}))^{-1}hol(γ_{t-1})^{-1}hol(γ_{t-1})hol(leg(z_{t-1})) = 1 gives
hol(ℓ_t) = hol(γ_{t-1})R_thol(γ_{t-1})^{-1}·hol(ℓ_{t-1}), R_t := the holonomy of the 1 × L rectangle spanned by s_t and
leg(z_{t-1}); ℓ_0 is trivial. If s_t is along ±μ the rectangle is degenerate (a back-tracking path) and R_t = 1 exactly.
Otherwise R_t is a product of L conjugated plaquettes. The axial path has Σ_{α≠μ}|y_α - (c_X)_α| ≤ (d - 1)(L - 1)/2 steps off
the μ-direction. All rectangles lie in B(X) ∪ B(X + e_μ) ⊂ U_4. So δ_c ≤ A_d(L)η, and M̄_c is a mean of the T^σ_y. (R2) S_P
is the holonomy of the L × L square through the four block centres, a product of L² conjugated plaquettes of U_4; then
telescope V_P against S_P (unitaries). (R3) If η < η_1 and all four ||V_c - S_c|| < ε_1/8, (R2) gives ||1 - V_P|| <
L²η_1 + ε_1/2 ≤ ε_1. (R4) |N^{-1}tr A| ≤ ||A||_op and (B) give 1 - N^{-1}Re tr(V^{-1}M̄) ≥ [1 - N^{-1}Re tr(V^{-1}S)] -
||M̄ - S|| ≥ ||V - S||²_op/(2N) - δ_c. D4-norm (2) gives 𝒩(M̄) ≥ e^{-(κ/g²)(1 - N^{-1}Re tr V_0^{-1}M̄)}e^{-1}c_N(g²/κ)^{N²-1}
with V_0 the maximiser, and 1 - N^{-1}Re tr(V_0^{-1}M̄) ≤ 1 - N^{-1}Re tr(S^{-1}M̄) ≤ ||M̄ - S|| ≤ δ_c (S is a candidate). So
k_c ≤ e c_N^{-1}(κ/g²)^{N²-1}exp(-(κ/g²)[||V_c - S_c||²/(2N) - 2δ_c]); on the event the bracket is ≥ ε_1²/(128N) -
2A_d(L)η_1 ≥ ε_1²/(256N). Haar mass 1. (R5) (B). ∎

*What RS buys (RLF-F4).* A level-(i+1) large field is pointwise reduced to level-i objects, across ONE step: either a
kernel mismatch, priced unconditionally by the normalised soft kernel at the FINER coupling g_i (1/g_i² ≥ 1/g_{i+1}² under
(F)), or a level-i plaquette ≥ η_1, priced by the level-i action (bare level: Wilson positivity; effective levels: the
large-deviation hypothesis (PLD) of §8). This is the soft-kernel form of the one-step regularity of Dimock QED Lemma 23
(NOTES §4 [read]); it is never iterated, so E8*-ob's obstruction does not apply. The pairing of contour orders (S4') is
what makes the far-end path a translate; without it the ribbon bound needs the area between two different axial paths
(c32 A controls this). **RLF-F4 is AVOIDED.**

*Constants (d = 4, L = 3).* A_4 = 9, L² = 9, η_1 = min{ε_1/18, ε_1²/(4608N)}; kernel exponent κε_1²/(256N).

## 7. Theorem R1 (frozen one-level R-operation) and Theorem TS (two scales, frozen exterior): PROVEN-HERE [S17; R1 (iii), TS hypotheses repaired S18, unreviewed]

### 7.1 Lemma LF-n (cluster-count arithmetic; not counted)
Under (F), with w_i := Ce^{-a/g_i²} and integers n ≥ 1: L^{4(K-i)}w_i^n ≤ C^ne^{-na/g_K²}L^{(4 - naβ_-)(K-i)}. Hence
Σ_{i≤K}L^{4(K-i)}w_i^n ≤ C^ne^{-na/g_K²}/(1 - L^{4-naβ_-}) whenever naβ_- > 4, and (LF-count, the other half) the sum diverges as
K → ∞ when w_i ≥ e^{-a/g_i²} per n-cluster and naβ_+ ≤ 4. *Proof.* Substitute 1/g_i² ≥ 1/g_K² + β_-(K - i)log L. ∎
**Definition.** For 0 < a'' < ε_1²/(4N): **n_* := ⌊4/(a''β_-)⌋**, so (n_* + 1)a''β_- > 4. n_* is g- and K-independent.
Consequence: only clusters of total cube number ≤ n_* need counterterms; LF-count's divergence comes from them alone.

**[R1617-fix R-8, R-10] Definitions for the induction.** a_RS := min{a_η, κε_1²/(256N)} (the two branches of Lemma RS
at effective levels; a_η from (PLD)_k (i)). c_RS := 5⁴ (ARGUED, not written: among n level-(k+1) bad cubes a greedy
choice gives ≥ n/5⁴ whose RS regions, U_4(P) with its 1-neighbourhood, are pairwise disjoint, so RS prices them by
(Ce^{-a_RS/g_k²})^{n/c_RS} ≤ (Ce^{-a_RS/g_{k+1}²})^{n/c_RS}; the joint pricing of the two branches is part of (HIST)'s ordering).
**a_♯ := min{a'', a_♭, a_RS/c_RS}, n_♯ := ⌊4/(a_♯β_-)⌋ ≥ n_*.** Theorem R1 below holds for every cutoff n_c ≥ n_* (its
constants depend on n_c); the induction uses n_c = n_♯. [inference, R-10] With the crude constants of §9 C and a_η taken
at its bare-level value η_1²/(2N) ≈ 1.8·10⁻¹⁰, n_♯ is of order 10¹³. It is finite and g- and K-independent, which is all
Lemma LF-n needs; it is a property of the bounds, not of the theory.

### 7.2 Theorem R1 (one level, frozen background) [R1617-fix: (iii) re-localised (R-3b); (H-loc) derived from (H-ch) (R-3a); torus wrap (R-4); cutoff n_c]
*Setting.* Level j, bare form, a frozen full configuration D (all level-j links and the level-(j+1) coarse links). Fix an
integer cutoff n_c ≥ n_*, put R_* := (n_c + 2)L [R1617-fix: was (16n_* + 2)L, the size needed by fattened polymers; the
localisation below uses unfattened supports], and assume
  **(H-ch)** ε_2 + ε_V ≤ ε_♮ on the box B̂_*(x) of radius R_* about every block centre x,
with ε_♮ := min{r_1(R_*), ε_loc/C_♮(R_*)}, r_1 = GT-lat's chart radius for R_*, and C_♮(R_*) ≥ 3 chosen so that every
point of the GT-lat' chart ball used in (ii) (tree coordinates |Z| ≤ C(R_*)ε_♮) has ε_♭(·; Y) ≤ ε_loc for every Y in the
box [S18 note: session 17 took C_♮ = 3, which covers the data themselves (Lemma 7.2-0) but not the whole ball over which
K_F is a supremum; constants only] **[R1819-fix F1: why C_♮(R_*) exists. On the chart ball, ε_♭(·; Y) is Lipschitz in the
tree coordinates, with a constant C'(R_*) (finitely many links in the box, each entering through smooth functions of
the principal logs, which stay principal on the ball); so for |Z| ≤ C(R_*)ε_♮, ε_♭(Z; Y) ≤ 2ε_♮ + C'(R_*)C(R_*)ε_♮ (the data
bound of Lemma 7.2-0 plus the Lipschitz step), and C_♮(R_*) := max(3, 2 + C'(R_*)C(R_*)) gives ε_♭ ≤ ε_loc on the whole
ball. C' is an existence constant (not computed), like r_1.]**. Session 17's (H-loc) is no longer a hypothesis (Lemma 7.2-0). Fix
a'' ∈ (0, ε_1²/(4N)), a_1 := ε_1²/(4N) - a'', κ := 4κ_0 + 3 with Theorem CE's [S11] κ_0 = 16 log 12800, κ_1 := κ - κ_0 - 2,
and c_0(κ), B, C_K, K_0 those of Theorem CE [S11]. Gas polymers (used for the hard core only): Ŷ := Y + {0, 1}⁴ (cube
coordinates). T_j := the side of the level-j torus in cubes (≥ 3); **W := 2n_c + 5.**
*Hypothesis on g (G1):* θ := 2(C_rg^{-p_r}e^{-a_1/g²})^{1/16} ≤ C_Kc_0(κ)e^{-2κ_1}, and g ≤ min(1, √κ).

**Lemma 7.2-0 (R-3a: completion for clusters of every size).** Under (H-ch), ε_♭(D; Y) ≤ 2ε_♮ < ε_loc for every set Y of
cubes. So Proposition CL (c) applies to every *-connected Y, whatever its size.
*Proof.* Take U° := D's own links on int(Y). Every plaquette p ⊂ N_1(Y) and every coarse link c ∈ C(Y) lies in some box
B̂_*(x) (R_* ≥ 2L). ||1 - U_p||_op ≤ ||log U_p||_op = ||P̂_p||_op ≤ ε_2 (|e^{iθ} - 1| ≤ |θ|; conjugation invariance), and
||V_c - S_c||_op = ||V_cS_c^{-1} - 1||_op ≤ ||log(V_cS_c^{-1})||_op ≤ ε_V. So ε_♭ ≤ 2ε_♮ ≤ 2ε_loc/3. ∎

*Claims.*
- (i) **The gas and its logarithm.** Ξ(D) = Σ_{families of polymers with pairwise disjoint X_i}Π_iz_{X_i}, with
  z_X := Σ_{Y: Ŷ=X}r_Y(D). log Ξ(D) = Σ_XΣ_{N≥1}𝓗^{(N)}_X(D), absolutely convergent, where 𝓗^{(N)}_X collects the terms of
  Theorem CE's 𝓗_X (step 3) whose clusters (Y_1, …, Y_n) have Σ|Y_i| = N, and
  |𝓗^{(N)}_X| ≤ e^{-a''N/g²}·2κ_0Bc_0(κ)e^{-κ_0d(X)}.
  **Tuple form [R1617-fix].** For a tuple τ = (Y_1, …, Y_n) of clusters let G(τ) be its touching graph (edge {i, j} iff
  Y_i ∪ Y_j contains two cubes at sup-distance ≤ 1, i.e. Y_i and Y_j touch or overlap), φ^T(G) := Σ over connected
  spanning subgraphs H ⊂ G of (-1)^{|E(H)|}, supp τ := ∪Y_i (UNFATTENED) and N(τ) := Σ|Y_i|. Then
    log Ξ(D) = Σ_{n≥1}(1/n!)Σ_τφ^T(G(τ))Π_ir_{Y_i}(D),
  absolutely convergent, and for every cube x
    Σ_{τ: supp τ ∋ x}(1/n!)|φ^T(G(τ))|Π_ir_{Y_i}(D)·e^{a''N(τ)/g²} ≤ 2κ_0Bc_0K_0.
- (ii) **Taylor form.** For a cube set S and N ≤ n_c put
    𝓖^{(N)}_S(D) := Σ_{n≥1}(1/n!)Σ_{τ: supp τ = S, N(τ) = N}φ^T(G(τ))Π_ir_{Y_i}(D),
  a finite polynomial in the r_Y (Y ⊂ S), zero unless S is *-connected with |S| ≤ N. For x ∈ S:
  𝓖^{(N)}_S(D) = 𝓖^{(N)}_S(1) + Q^{(N)}_{S,x}(Φ_x(D)) + R^{(N)}_{S,x}(D), with Q^{(N)}_{S,x} = Σt⟨Φ_a, Φ_b⟩ Ad-invariant
  (matrix t^{(N)}_{S,x}) and Σ_{S∋x}|R^{(N)}_{S,x}(D)| ≤ C_*g^{-6}e^{-a''N/g²}𝔯_x(D), 𝔯_x := 𝔯 on B̂_*(x),
  C_* = C(n_c, L, N, κ).
- (iii) **Assembly (re-localised).** If T_j ≥ W, then with N_j the number of level-j cubes
    log Ξ(D) = N_jc̄_0(g) + δβ_j·Σ_ps(U_p) + Σ_xℛ_x(D),
    c̄_0(g) := Σ_{N≤n_c}Σ_{S∋0}𝓖^{(N)}_S(1)/|S|,  δβ_j := (2N/L⁴)c̄_1,  c̄_1 := (1/6)Σ_{N≤n_c}Σ_{S∋0}tr t^{(N)}_{S,0}/|S|
  (both computed on the cubes of Z⁴), |c̄_0| ≤ 2κ_0Bc_0K_0e^{-a''/g²}, |δβ_j| ≤ C_*g^{-6}e^{-a''/g²},
    |ℛ_x| ≤ C_*g^{-6}e^{-a''/g²}𝔯_x + 2κ_0Bc_0K_0e^{-a''(n_c+1)/g²}.
  c̄_0 and δβ_j are field-independent numbers depending only on (g, L, N, κ, ε_1, a'', n_c); Σ_p runs over all level-j
  plaquettes.
- (iv) **Torus wrap (R-4).** If T_j < W, log Ξ(D) = Σ_xℛ^w_x(D) with |ℛ^w_x| ≤ 2κ_0Bc_0K_0e^{-a''/g²} (nothing is
  extracted). Over all levels j < K, the number of level-j cubes on levels with T_j < W is ≤ (L⁴/(L⁴ - 1))W⁴, uniformly in K
  and T, and those levels have g_j ≤ g_K. So the wrap levels contribute in total a field-dependent term of absolute value
  ≤ (L⁴/(L⁴ - 1))W⁴·2κ_0Bc_0K_0e^{-a''/g_K²}, uniformly in K: a bounded boundary-type term, not of irrelevant order, absorbed
  by the C|T|e^{-a'/g_K²} of (RLF-4) (|T| ≥ 1).

*Proof.* (i) **Hard core = disjointness.** For cube sets, Ŷ ∩ Ŷ' ≠ ∅ iff some x ∈ Y, x' ∈ Y' have
x - x' ∈ {0,1}⁴ - {0,1}⁴ = {-1, 0, 1}⁴, i.e. iff Y and Y' touch or overlap (torus side ≥ 3). The *-components of B are
pairwise *-separated *-connected sets, and a family of pairwise *-separated *-connected sets is the set of components of
its union; so B ↦ (components) is a bijection onto families with pairwise disjoint Ŷ_i. With CL (b), Σ_BΠr = Σ_{disjoint}Πz_X.
Ŷ is *-connected (a polymer), |Ŷ| ≤ 16|Y|, d(Ŷ) ≤ 2(|Ŷ| - 1) (a spanning tree of centre-to-centre segments, each ≤ √4 = 2),
and #{Y : Ŷ = X} ≤ 2^{|X|}. **Grading.** Put r'_Y := e^{a''|Y|/g²}r_Y and z'_X := Σ_{Ŷ=X}r'_Y. By CL (c), applicable to every
cluster by Lemma 7.2-0, |z'_X| ≤ 2^{|X|}max(C_rg^{-p_r}e^{-a_1/g²})^{|Y|} ≤ θ^{|X|} (|Y| ≥ |X|/16, base < 1). By (G1) and
C_Kc_0(κ) ≤ 1, θ^{|X|} ≤ C_Kc_0e^{-2κ_1|X|} ≤ C_Kc_0e^{-κ_1d(X)}: z' lies in Theorem CE's polydisc 𝔻 with H_0 = c_0(κ). CE
steps 3-4 (PROVEN, L5 [S10]-[S11]; statements about P(z) = Σ_{disjoint}Πz on 𝔻 for any z ∈ 𝔻) give log P = Σ_X𝓗_X,
𝓗_X = Σ_n(1/n!)Σ_{(X_1..X_n): ∪X_i = X}ρ^T(g(X_1..X_n))Πz_{X_i} (ρ^T on the overlap graph g), with
Σ_n(1/n!)Σ|ρ^T|Π|z'_{X_i}| ≤ 2κ_0Bc_0e^{-(κ-3κ_0-3)d(X)} = 2κ_0Bc_0e^{-κ_0d(X)}. **Tuple form.** Substitute
z_{X_i} = Σ_{Ŷ_i = X_i}r_{Y_i}. By the hard-core equivalence the overlap graph of (Ŷ_1, …, Ŷ_n) is the touching graph G(τ),
so each X-tuple term expands into the τ-terms with Ŷ_i = X_i, and the τ-series is a regrouping of the X-series. Because
r'_Y ≥ 0, |z'_X| = Σ_{Ŷ=X}r'_Y, so the τ-series of the nonnegative terms (1/n!)|φ^T|Πr'_{Y_i} has the same sum as the
X-majorant: absolute convergence, and rearrangements are allowed. Every τ with supp τ ∋ x has ∪Ŷ_i ∋ x (Y ⊂ Ŷ), so
Σ_{supp τ ∋ x}(1/n!)|φ^T|Πr'_{Y_i} ≤ Σ_{X∋x}2κ_0Bc_0e^{-κ_0d(X)} ≤ 2κ_0Bc_0K_0 ((g4) [S11]). If G(τ) is disconnected,
φ^T = 0; if it is connected, supp τ is *-connected. Grouping by N = N(τ): every term of 𝓗^{(N)}_X (and of 𝓖^{(N)}_S) is a
majorant term times e^{-a''N/g²}. ∎(i)
(ii) 𝓖^{(N)}_S involves tuples with n ≤ N and Y_i ⊂ S: finitely many. **Locality.** r_Y depends on D only through the links
of plaquettes meeting int(Y) and the coarse links of C(Y) with their contours, i.e. inside the blocks of Y and their
*-neighbours. S is *-connected with |S| ≤ N ≤ n_c, so S lies within cube sup-distance n_c - 1 of x, and 𝓖^{(N)}_S depends on D
only inside B̂_*(x) (fine sup-distance ≤ n_cL + (L - 1)/2 < R_*). **Invariance.** Each r_Y is gauge-invariant (CL (e)).
**Derivatives.** The product rule over ≤ n_c factors and CL (d) give K_F ≤ B(n_c)(Λ_1/g²)³·sup_{ball}Σ_{supp τ = S, N(τ) = N}
(1/n!)|φ^T|Πr_{Y_i}. On the chart ball every r_Y obeys CL (c) (choice of C_♮), so the bound of (i), whose derivation used only
CL (c), bounds Σ_{S∋x} of these suprema by e^{-a''N/g²}2κ_0Bc_0K_0. Apply GT-lat' (i) to each F = 𝓖^{(N)}_S with C := all
coarse links in B̂_*(x). ∎(ii)
(iii) **Localisation.** Σ_S𝓖^{(N)}_S = Σ_xΣ_{S∋x}𝓖^{(N)}_S/|S|. Fix x. **The family is permuted (the repaired step).** Let
R ∈ B_4 act about the block centre c_x of x: on fine sites z ↦ c_x + R(z - c_x); on cubes y ↦ x + R(y - x) (blocks go to
blocks because c_y = Ly + o); on data D ↦ R·D. Then (a) r_{RY}(R·D) = r_Y(D) (CL (e)); (b) R preserves the sup-distance of
cubes, hence touching, so G(Rτ) = G(τ) for Rτ := (RY_1, …, RY_n); (c) N(Rτ) = N(τ), supp(Rτ) = R(supp τ), |RS| = |S|;
(d) x ∈ RS ⟺ x ∈ S. So τ ↦ Rτ maps {τ: supp τ = S, N(τ) = N} bijectively onto {τ: supp τ = RS, N(τ) = N}, term by term, and
𝓖^{(N)}_{RS}(R·D) = 𝓖^{(N)}_S(D). Hence F_S := 𝓖^{(N)}_S/|S| (S ∋ x) satisfies F_S(R·D) = F_{R^{-1}S}(D): the finite family
{F_S : S ∋ x, |S| ≤ N} is permuted by D ↦ R·D, which is exactly the hypothesis of GT-lat' (ii). (This is the step that is
false for the session-17 assignment: Ŷ = Y + {0,1}⁴ is not B_4-covariant about x, R(Ŷ) = (RY)^ + t_R, and x ∈ Ŷ does not
imply x ∈ (RY)^; REVIEW_S16_S17, R1 (iii); c33 B2-B3.) **Coupling shift.** GT-lat' (ii) gives
Σ_{S∋x}Q^{(N)}_{S,x}(Φ_x)/|S| = c̄_1^{(N)}Σ_a||Φ_{x,a}||²_HS with c̄_1^{(N)} := (1/6)Σ_{S∋x}tr t^{(N)}_{S,x}/|S|. **Translation and
torus.** If T_j ≥ W, each S ∋ x with |S| ≤ n_c, together with B̂_*(x), embeds isometrically into Z⁴ (the box spans
2n_c + 5 = W ≤ T_j cubes per direction, and its fine side 2R_* + 1 ≤ T_jL - 2 for L ≥ 3), the touching relation on it is the Z⁴ one, and the r_Y are the same functions of
the same data. So 𝓖^{(N)}_S(1) and t^{(N)}_{S,x} are their Z⁴ values, which are translation invariant: c̄_0 and c̄_1 do not
depend on x and are the infinite-volume numbers of the statement. **Identification with the Wilson action** (unchanged):
let B_x := the plaquettes with base point in block x (6L⁴ plaquettes; the B_x partition all plaquettes). For p ∈ B_x,
s(U_p) = ||P̂_p||²_HS/(2N) + O(N²||P̂_p||⁴) (1 - N^{-1}Re tr e^Y = ||Y||²_HS/(2N) + O(Y⁴), R4D-iso step 4), and
|‖P̂_p‖²_HS - ‖Φ_{x,a(p)}‖²_HS| ≤ 2Nε_2ε_3. Summing over B_x (L⁴ base points per plane):
Σ_{p∈B_x}s(U_p) = (L⁴/(2N))Σ_a||Φ_{x,a}||² + O(L⁴(ε_2ε_3 + ε_2³)). So Σ_xc̄_1||Φ_x||² = δβ_jΣ_ps(U_p) + O(c̄_1Σ_x𝔯_x). Collect
R^{(N)}, this identification error, and the tail Σ_{N>n_c} (≤ 2κ_0Bc_0K_0e^{-a''(n_c+1)/g²} per x, by (i)) into ℛ_x. The
bounds on c̄_0 and δβ_j follow from (i)-(ii) (N ≥ 1). ∎(iii)
(iv) On a level with T_j < W put ℛ^w_x := Σ_NΣ_{S∋x}𝓖^{(N)}_S/|S|; (i) bounds it. Count: T_j = T·L^{K-1-j} ≥ 3L^{K-1-j}, so
T_j < W only when K - 1 - j < log_L(W/3), and Σ_{such j}T_j⁴ ≤ W⁴Σ_{m≥0}L^{-4m}. For these j, g_j ≤ g_K by (F). ∎
**[R1819-fix F2]** T and T_j as in §1A (T the level-K side in level-K sites, T_j the level-j side in level-j cubes).
**[R1819 note]** W⁴ ≈ (2·10¹³)⁴ is absorbed into the g-independent constant C of (RLF-4); this is legitimate (it is
g- and K-independent) and is the only place the wrap levels enter.

**Remark 7.2-B (the value of δβ_j is unchanged; a second repair route).** On GT-lat' step 2's reference data,
Q_{F,x}(Φ) = ½D²F̃(0)(𝓛_xΦ, 𝓛_xΦ), the Hessian at the identity configuration in per-link Lie coordinates. (a) **Centre
independence.** 𝓛_xΦ - 𝓛_{x'}Φ is the constant su(N)-valued 1-form ½(x' - x)^νΦ_νμ, which on a box is d of a linear
function; and the Hessian of a gauge-invariant F at the critical point 1 is invariant under the linearised gauge action
(expand F(e^{tλ}·exp(sA)) = F(exp(sA)) to second order and use DF̃(0) = 0). So Q_{F,x} = Q_{F,x'}. (b) **Translation.**
Q_{F_{X+a}} = Q_{F_X} by translation covariance. Hence ANY base-point assignment that gives the placements of each
translation class total weight 1 per cube (the fattened one of session 17 included) yields, at every x, the same form
Σ_{classes}Q_{[X]}, the total quadratic coefficient per cube. The class set is B_4-invariant, so this total is scalar by the
argument of GT-lat' (ii). So the session-17 formula for δβ_j gives the right number, and anisotropic marginal terms do not
arise; what was false was the claimed permutation of the family {X ∋ x}, and with it the B_4-invariance of the full
localised functional. c33: A5/B4 (constant data: the two localisations agree), A3/B2 (generic data: the fattened one is
not invariant, the tuple one is). The counted repair is (iii); Remark 7.2-B is ARGUED-level supplementary (not counted).

*Reading [R1617-fix R-6].* Under (H-ch), the whole level-j large-field gas is exactly e^{c-number}·e^{δβ_jΣs}·e^{Σℛ}: every
cluster tuple of total size N ≤ n_c contributes a vacuum constant and its share of ONE uniform coupling shift, and the rest
is ℛ: a local remainder of order 𝔯_x(D) plus an unrenormalised tail of order e^{-a''(n_c+1)/g²} per cube, which Lemma LF-n
sums. **The remainder is irrelevant only for BG-b-regular frozen data** (where 𝔯_x is small with the scale, §7.3 (b1)).
**In a sea sample** ε_V = max||log(V_cS_c^{-1})|| is an O(g/√κ) fluctuation, so 𝔯_x = O(g²), the same order as the extracted
quadratic part, and |ℛ_x| ≤ C_*g^{-4}e^{-a''/g²} per cube. Summed over levels with L^{4(K-j)} cubes this diverges (LF-count).
So in the fluctuating integral the c-number and marginal parts of ℛ must be re-extracted after the sea average: that is
(W1-ret') in §8.2. What R1 gives pointwise in a sea sample satisfying (H-ch) is the exact identity (iii) with these bounds,
not smallness. **RLF-F2 is AVOIDED (frozen, R1 (iii) as repaired):** the counterterms are field-independent and the
B_4 orbit structure of the tuple supports plus the base-point partition B_x reduce all marginal parts to one coupling shift
of the uniform Wilson action.

### 7.3 Theorem TS (two scales; the level-k field may be large; frozen exterior) [R1617-fix R-5: hypotheses on the region R1 uses]
*Setting.* Levels j < k. Δ := one level-(k-1) cube (one level-k site; so Δ lies in a level-k cell that may be large-field
at level k). A frozen multi-level background: for each inner level i ∈ [j, k-1], a full configuration D_i (level-i links
and level-(i+1) coarse links, the latter = the level-(i+1) links of D_{i+1}), with T_i ≥ W (wrap levels: §7.2 (iv)).
Assume:
- **(R1)_i at every inner level i:** D_i satisfies Theorem R1's hypothesis (H-ch) on the whole level-i torus (R1's gas
  identity is a statement about the whole level; frozen exterior means all of D_i is given), and (G1) holds at g_i.
- **BG-b relative to level k-1, on Δ_*.** For i = k-1-n (n ≥ 0) let 𝒬_n(Δ) := the level-i cubes inside Δ (L^{4n} of them)
  and Δ_{*,n} := the level-i cubes within cube sup-distance R_*/L + 1 of 𝒬_n(Δ) (the cubes that meet a box B̂_*(x),
  x ∈ 𝒬_n(Δ)). For Q ∈ Δ_{*,n} let ε_•(Q) be R4D-iso/GT-lat's parameters of D_i on Q's box, and assume
  (b1) ε_2(Q) + ε_V(Q) ≤ M_2σ_n², σ_n := L^{-n}, with M_2 ≤ ε_TS := ε_♮;
  (b2) Σ_nō_n ≤ M_3, ō_n := σ_n^{-2}L^{-4n}Σ_{Q∈Δ_{*,n}}(ε_3 + ε_V)(Q).
- **Coupling window:** g_i² < a''/3 at every inner level (so that w(g) := C_*g^{-6}e^{-a''/g²} is increasing on the inner
  couplings: d log w/dg = -6/g + 2a''/g³ > 0 iff g² < a''/3).
**No hypothesis is made on the level-k field** (it may have ||1 - U_k(P)|| ≥ ε_1 at Δ). The inner integrands are of bare
form at each inner level (frozen model; effective levels: §8).

*Claims.*
- (TS-a) **Fixed counterterms.** At each inner level i the large-field gas satisfies Theorem R1 with the constants
  c̄_0(g_i), δβ_i of 7.2, which do not depend on the level-k field or on any datum.
- (TS-b) **Inner remainders based in Δ, uniformly in j, k.** Σ_{i=j}^{k-1}Σ_{x∈𝒬_{k-1-i}(Δ)}|ℛ_x| ≤ C_TS[w_{k-1}(3M_2M_3 +
  M_2³/(1 - L^{-2})) + e^{-a''(n_c+1)/g_{k-1}²}/(1 - L^{4-(n_c+1)a''β_-})], with w_i := C_*g_i^{-6}e^{-a''/g_i²} and
  C_TS = C(n_c, L, N, κ), including the box-overlap factor (2R_*/L + 3)⁴.
- (TS-c) **Outer suppression, one step.** If Δ's level-k cell has a plaquette P with ||1 - U_k(P)|| ≥ ε_1, then by Lemma RS
  applied to the step k-1 → k: either some level-(k-1) plaquette in U_4(P) has s ≥ η_1²/(2N) (cost e^{-η_1²/(2Ng_{k-1}²)} in
  the level-(k-1) Wilson weight in the bare model), or a mismatch event of conditional probability
  ≤ e c_N^{-1}(κ/g_{k-1}²)^{N²-1}e^{-κε_1²/(256Ng_{k-1}²)}, uniformly in everything (Lemma RS (R4)).
- (TS-d) Both suppressions are kept in product form: the inner levels contribute exp(N-weighted c-numbers + coupling
  shifts + the remainders of (TS-b)) and the outer large field contributes the factor of (TS-c); neither needs the other.

*Proof.* (TS-a) Theorem R1 at level i under (R1)_i; its constants are the infinite-volume numbers (T_i ≥ W).
(TS-b) For x ∈ 𝒬_n(Δ) every cube meeting B̂_*(x) is in Δ_{*,n}. **Box merging.** For the box B̂_*(x),
ε_2(B̂_*) = max_{Q⊂B̂_*}ε_2(Q) (conjugation does not change ||log U_p||), ε_V(B̂_*) = max ε_V(Q), and
ε_3(B̂_*) ≤ C(R_*)max_{Q⊂B̂_*}(ε_3(Q) + ε_2(Q)²): compare the base plaquette of B̂_* with those of a chain of ≤ 2R_*/L + 1
overlapping cube boxes; consecutive base plaquettes differ by ≤ ε_3 + Cε_2² after transport, and changing the transport
path conjugates by a holonomy h with ||h - 1|| ≤ (area)ε_2, which moves a plaquette log of size ε_2 by ≤ 2||h - 1||ε_2. Then
with ε_3 ≤ 2ε_2 and (b1) on Δ_{*,n}, every product in 𝔯_x is bounded by C(n_c)Σ_{Q⊂B̂_*(x)}[3M_2σ_n²(ε_3 + ε_V)(Q) + M_2³σ_n⁶]
(max ≤ sum). Each Q ∈ Δ_{*,n} lies in ≤ (2R_*/L + 3)⁴ of the boxes B̂_*(x). Sum over x ∈ 𝒬_n(Δ) and use L^{4n}σ_n⁴ = 1
(the d = 4 marginality, as in BG-sum) and |Δ_{*,n}|σ_n⁴ ≤ (2R_*/L + 3)⁴ for the M_2³ term: the level-n total is
≤ C[3M_2ō_n + M_2³σ_n²]·w_i, with w_i ≤ w_{k-1} (g_i ≤ g_{k-1} and the coupling window). Sum over n with (b2). The tail:
|𝒬_n(Δ)| = L^{4n} cubes, each ≤ 2κ_0Bc_0K_0e^{-a''(n_c+1)/g_{k-1-n}²}; Lemma LF-n. (TS-c) Lemma RS (R3)-(R5) at the step
k-1 → k; the kernel branch is unconditional (R4); the plaquette branch is a pointwise lower bound on the level-(k-1) Wilson
term. (TS-d) The inner statements use only the inner data; the outer one uses only the step k-1 → k. ∎
**Role [R1617-fix R-6].** TS is the frozen-background shadow of the induction: it shows what the inner remainders cost when
the frozen data are BG-b-regular. Proposition RLF-step (§8.3) does not use TS; it uses R1 pointwise in the sea sample and
re-extracts after the sea average.

### 7.4 Outcome against RTARGET §7 and §2's failure modes (frozen exterior)
- **W2-F1 (no smooth background inside a multi-scale large region): CIRCUMVENTED for BG-b-regular frozen data only
  [R1617-fix R-6], with a named hypothesis.** The inner renormalisation at level i needs only (H-ch), a level-i statement
  about level-i data; the summation over inner levels (TS-b) needs BG-b relative to the LAST level at which the region is
  small-field (k - 1), on Δ_*, never the large level-k field. The Taylor parameter is ε_•(level-i data), not a smooth
  family. Hypothesis: BG-b of the FROZEN data at level k-1. [R1617-fix R-6: session 17 wrote "(= node N2/BG-reg)"; that
  conflates the background minimiser, for which N2/BG-reg would supply BG-b, with a frozen sample. A level-i sea sample
  violates (b1) once L^{-2n}M_2 < g, and then 𝔯 = O(g²): §7.2 Reading.] In the fluctuating integral W2-F1 is carried by the
  sea-averaged re-extraction (W1-ret') of §8.2.
- **W2-F2 (inner vacuum depends on the outer field): AVOIDED by construction.** c̄_0(g_i), δβ_i are defined at the trivial
  datum, in infinite volume.
- **W2-F3 (history combinatorics): AVOIDED in the frozen setting.** Per level, the sum over large-field sets is a hard-core
  polymer gas, exponentiated by CE steps 3-4; tuples with N ≤ n_c carry counterterms, N > n_c are summable (LF-n); inner
  levels decouple from the outer one (TS-d). Across levels in the fluctuating integral it is the bookkeeping (HIST) of §8.
- **RTARGET §7 form.** The "alternatively" form is met in the frozen setting, with the correction that renormalisation is
  level by level relative to the next coarser small-field level; "both suppressions kept" holds in the product form
  (TS-d) rather than as e^{-a/g_j²}e^{-a/g_{j+1}²} per inner cube (inner cubes are renormalised and need no outer factor).
- RLF-F1 AVOIDED (Proposition CL (c) with Lemma 7.2-0); **RLF-F2 AVOIDED (R1 (iii) as repaired [R1617-fix R-3b]; session
  17's proof of this was invalid, Remark 7.2-B)**; **RLF-F3 AVOIDED for BG-b-regular frozen data only** (TS-b uses no
  level-k regularity, but does use BG-b of the frozen inner data); RLF-F4 AVOIDED (Lemma RS).
- **Scope (not success items, as pre-stated):** frozen exterior (the sea is a fixed configuration); bare-form inner
  integrands; (H-ch) on every inner level (in the real integral it fails with density e^{-c/g²}: §8).

[Appendix A, part 2: v1 §9-§9A, l.723-758]

## 9. Check c32 (criteria first: checks/c32_criteria.md; script checks/c32_rlarge.py; record checks/c32_time.txt)
**All four parts PASS, first and only runs** (laptop, load ≤ 2.5, ≥ 36% free, peak RSS ≤ 41 MB, ≤ 4 s each).
- **A (Lemma RS, SU(2), d = 4, L = 3):** A1-A4 hold on 15 random configurations (t = 0.01-0.2) and three sharp ones. Random
  fields use the constants loosely (max ribbon ratio 1.99 of the proven 9; square 0.80 of 9). **A5 sharpness:** a constant
  abelian flux in the planes (α, 0) gives ribbon ratio 8.99997 and a flux in (0, 1) gives square ratio 8.99997, so
  A_4(3) = 9 and L² = 9 are attained (the area counts are exact, not overcounts). **A6:** with additional flux in the planes
  (1,2), (1,3), (2,3), UNPAIRED contour orders reach 14.9999 > 9 while the S4'-paired ones stay at 9.0000: the S4' pairing
  is load-bearing for the ribbon constant.
- **B (hard core):** B1 fattening ⇔ touching on 4000 pairs in (Z/6)⁴ (1961 touching), B2 components ↔ disjoint fattened
  families (2000 + 2000 instances), B3 the t^N coefficients of log Ξ_T are exactly extensive (c_N/T equal for T = 12, 14, 16 to
  ≤ 2e-12, N ≤ 4): the graded logarithm is local, as Theorem R1 (i) uses.
- **C (arithmetic, one-loop rate [inference]):** n_* = 382 (SU(2), ε_1 = 0.5), 95 (ε_1 = 1), 23 (ε_1 = 2); SU(3): 255, 63, 15.
  So **for every admissible ε_1 (≤ 2) the R-operation is needed (n_* ≥ 15), and n_* is finite and g-independent.**
  **[R1617-fix R-10] This conclusion is also [inference]:** it rests on the one-loop rate and on a'' = 0.9ε_1²/(4N), the
  frozen lower bound on the per-cube cost, not the true cost; n_* is a property of the bound. After R-8 the exponent that
  matters is a_♯ = min{a'', a_♭, a_RS/c_RS}, which makes the relevant integer n_♯ far larger (§7.1). RS at
  N = 2, κ = 1, ε_1 = 0.5: η_1 = 2.7·10⁻⁵, plaquette exponent η_1²/4 = 1.8·10⁻¹⁰, kernel exponent 4.9·10⁻⁴; CL: ε_loc = 3.5·10⁻³.
  These are g-independent but very small (crude constants, recorded as such).
- **D (GT-lat' (ii)):** the full B_4 average of 20 random t is (tr t/6)·1 to 1e-12; the rotation-only average is
  non-scalar in 20/20 (reflections needed, as in c19 P1).
- [R1617-fix] c32 tests none of CL (c), R1 (iii) or TS (REVIEW_S16_S17); c33 below tests R1 (iii)'s localisation step.

## 9A. Check c33 [S18] (criteria first: checks/c33_criteria.md; script checks/c33_bfour.py; record checks/c33_time.txt)
Toy B_4 step (R-3b): explicit hard-core gases with isometry-covariant scalar activities r_Y(D) (depending on D on Y and its
*-boundary), F^tup_x = the repaired tuple-support localisation, F^fat_x = session 17's fattened one.
- **B (d = 4, T = 7, N ≤ 2, all 384 elements of B_4 about x): PASS.** F^tup_x is invariant to ≤ 1.3e-15 (relative); F^fat_x
  changes by 0.68-3.9 (relative) for each of three random fields; the review's case ({x - e_1} has x in its fattening, its
  reflection {x + e_1} does not) confirmed; on constant data F^tup_x = F^fat_x to 2.7e-14 (Remark 7.2-B).
- **A (d = 2, T = 9, N ≤ 3, whole torus, brute-force log Ξ): FAIL as pre-registered** (A1, A4, A5), on the constant seed
  only, where the double-precision brute-force coefficient c_3 = a_3 - a_1a_2 + a_1³/3 cancels ~3 digits (relative errors
  2.9e-9 against the written 1e-10 / 1e-12). On the five random seeds the tuple identity holds (A1, A4 ≤ 5.6e-12); A2
  (tuple localisation invariant under all 8 elements, ≤ 6.2e-14) and A3 (fattened not invariant, 0.61-2.0) hold on every
  seed; A5's F^tup = F^fat on constant data holds (4.8e-13). Post-run diagnostic (not a criterion; c33_diag_mp.py): at 40
  digits the constant seed's tuple totals equal the brute-force coefficients to ≤ 3.0e-34. No criterion edited.
- Scope: toy scalar activities, not Wilson/soft-kernel ones; it tests the combinatorics and the permutation property, not
  GT-lat' (ii) (c32 D).
