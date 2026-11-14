# RLARGE v3: the 4D large-field R-operation for the soft-kernel RG (integration of REVIEW_RLARGE_V2 and lanes C, D, F, G, H, BFT; 2026-10-28)

**v3 header (integration, not new mathematics).** This file is the v3 integration of RLARGE.md. The v2 file is kept
byte-identical as **RLARGE_v2_snapshot.md** (md5 24a73553…); the v1 file stays as RLARGE_v1_snapshot.md. "v2 l.N" below is a
line of the v2 snapshot. The pre-stated target text of v1 §1 is reproduced verbatim in §1.0 (byte-identical to v1 l.64-93
and to v2 l.111-140). The proven frozen lemmas of v1 are carried as **Appendix A, verbatim** (v2 l.617-1041), with v3 reading
notes at its head. Every v3 change is tagged **[v3-Xn]** with the source it applies; v2 tags ([v2-…]) are kept where the v2
text survives. Integration record: RLARGE_INTEGRATION_LOG.md, section "v3".

**Binding input.** **REVIEW_RLARGE_V2.md** (md5 43057df5…): Part 1 (36 rows, 31 stale or wrong statuses), Part 2 (soundness:
"The three-way pricing of §3 is NOT sound as written. The defect is architectural, not a status lag"; fixes V-1, R-1; §4.3
"ARGUED stands, with the list replaced by Part 3's"; (RLF-3) mis-stated; FI-1, S4-5 non-circularity checks), Part 3 (the
rebuilt critical-path DAG), "Required fixes, for the RLARGE owner" 1-7. Applied as [v3-V1] (§3 re-based), [v3-R1] (§2.1,
§4.3 steps 4, 6), [v3-3'] ((RLF-3) restated), [v3-L] (§4.2 list), [v3-T] (thresholds), [v3-K] (conflicts), [v3-D] (§7 DAG),
[v3-S] (statuses, Part 1 rows F1-A10 by label).

**Other inputs read for v3 (read-only; md5 at 09:37 UTC, 2026-10-28, while other agents were editing BFT_A.md, BFT_B.md and
FLOW.md; anything written after that is not integrated):** HW.md 05e7f210… (§2-§6, §13-§15, §18-§19 in full; §1, §7-§17 by
heading) with REVIEW_HW_S2 363fb1ae… (bottom line, §5, tally, binding fixes); SQ.md 688f6a61… (§0, §0.1-§0.3 incl. DESC-ε)
with REVIEW_SQ_S2 f8499475… (bottom line, Priority 5, tally, fixes, strategy); SF.md ceec42df… (header §1, §16.3, §20.1-§20.2,
§22.6-§23.2) with REVIEW_SF_S7 abc625e0… (bottom line, Parts C, E, F); HIST.md 468e9f03… (§25.6-§25.7) with REVIEW_HIST_S4
bc0a9da0… (bottom line, Priority 5, tally, fixes, strategy); FLOW.md 5153af89… (§9 F-ind/FI-1, Lemma F-mono l.1296-1330,
(F-3) l.67-71, §79-§83, session 10) with REVIEW_FLOW_S9 8eb166d5… (bottom line, §7-§9); REVIEW_FLOW_S10 does not exist at
read time; PLD.md 4db9b142… and REVIEW_PLD_S3 aa57397e… (unchanged since v2, which integrated them; not re-read in full);
PROOF.md 488c2388… (header l.1-30; [S23] l.6600-6713, the BFT statement and **CROSS-LANE STATUS (session 23)**); REVIEW_S22
fc6bb7f2… Part 5 (BFT, l.372-435); REVIEW_BFT_A_S5 2837755b… (bottom line only; later than PROOF's S23 map, see §8 K19);
EXISTENCE.md 4988c83d… §17.8 (K8, K9 answers to v2).

Status words as in PROOF.md: PROVEN-HERE (counted or not, said each time), CONDITIONAL (implication proven, hypotheses
named), ARGUED, OPEN, HYPOTHESIS, GAP. Review verdicts are quoted from the review files (CONFIRMED / CONFIRMED-WITH-FIX /
GAP / WRONG); a status with no later review is marked "unreviewed" or "as in v2". Weights: **P** = paper-scale, **s** =
session-scale, as given by the owners; where no owner gives one, the cell says so. Class tags (REVIEW_RLARGE_V2 Part 3):
**[A]** node-A small-field item, **[BFT]** a BFT clause, **[FLOW]**, **[HW]**, **[R]** RLARGE-owned, **[other]**. Balaban
CMP 122 is [not-read]; nothing here is attributed to it. Imported items are never load-bearing for a PROVEN-HERE claim. This
file makes no tally change in PROOF.md (the ledger owner decides). Arithmetic marked **[hand]** is the integrator's
order-of-magnitude arithmetic from quoted constants, unreviewed, not a numeric job.

---

## 0. Conventions

- **Levels** (v1 §0, unchanged). Level k = after k RG steps; k = 0 bare, k = K the unit lattice. U_k is the level-k field on
  Λ_k; d = 4; L ≥ 3 odd; G = SU(N), N ≥ 2. A level-k cube is a level-k block (L⁴ level-k sites = one level-(k+1) site);
  π(z) := ⌊z/L⌋. T is the side of the level-K torus in level-K sites; T_k = T·L^{K-1-k} (v1 §1A, R1819-fix F2).
- **Action normalisation [v2-F; FLOW Lemma F-norm, CONFIRMED].** s(U) := 1 - N⁻¹Re tr U ∈ [0, 2]; the level-k Wilson term is
  u_kΣ_ps(U_p) with **u_k := 1/g_k² = β_Wilson = 2N/g_std²**. One-loop slope per step **β_1 := β_0^std = 11N²/(12π²)** per log
  L. **[v3-S, F7]** FLOW writes this quantity β_0′ (FLOW l.420-421); the same quantity, cosmetic. Inequality (B):
  s(U) ≥ ||1 - U||²_op/(2N).
- **The exact chain** (v1 §0; HIST §0; HW §0). W(U_0, …, U_K) := e^{-S_0(U_0)}Π_{i<K}K_i(U_{i+1}, U_i), K_i = Π_ck^{(i)}_c,
  k^{(i)}_c(V; M) = e^{-κu_iφ_M(V)}/∫e^{-κu_iφ_M}; ∫K_i dU_{i+1} = 1, Z_K = ∫W. Lemma TD: given U_k the level-(k+1) links are
  independent with densities k^{(k)}_c. **The kernel couplings u_i are parameters of W** (see §4.4 on FI-1).
- **History weights [v3-V1; HW §2, Lemmas HR, RX, PROVEN-HERE, elementary, uncounted].** For a fixed history-independent
  defect rule D_j (a function of (U_{j-1}, U_j)), every chain configuration has exactly one admissible history 𝔥(c);
  **Z(𝔥) := ∫W·1_𝔥 ≥ 0 and Σ_𝔥Z(𝔥) = Z_K** (Lemma HR). The relaxed event R(𝔥) (no unreturned defect outside 𝔥's own regions)
  gives **Z(𝔥) = Z(R(𝔥))·μ_{R(𝔥)}(𝔥) and Z(∅) ≤ Z(R(𝔥))** (Lemma RX; (ii)-(iii) need the history-independent D_j, HW RHW1-fix
  H-2). μ_{R(𝔥)} := W·1_{R(𝔥)}/Z(R(𝔥)) is **the single conditioned law** of §3. Z(𝔥) is the unrenormalised history weight:
  ∫W·1_𝔥 contains no extraction (HW RHW1-fix H-10).
- **Indicators.** χ_Q := Π_{p⊂int Q}1{||1 - U(p)||_op < ε_1} (cube-INTERIOR plaquettes only), ζ_Q := 1 - χ_Q; χ_Q is never
  changed [v2-E8, fix SG-2].
- **Tori [v2-E7].** Hypercubic tori wherever GT-lat′ (ii) / Lemma W1R-sym produces ONE coupling shift; with a different time
  side two shifts are needed (PLD §12 item 4). See K9 (§8) for EXISTENCE's (K9-req).
- **Thresholds [v3-T; REVIEW_RLARGE_V2 Required fix 5, A1, A5, A6, H5, H8].**
  - ε_1 (the cut), ε_loc (v1 §5), ε_♮, ε^J_loc, ε^J_♮ (as v2).
  - **η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}** [v2-E9] (Lemma RS (R3)'s value); η_q := min{ε_1/(2L²), ε_1/(256NA_d),
    δ_0/A_d} (RS-lin; joint route). For ε_1 ≤ 2, η_1 ≤ η_q unless δ_0/A_d binds ("CORRECT", REVIEW_RLARGE_V2 §2.3).
  - **Stage-0 chart threshold τ_c and (TH-ch″) [v3-T, A5; SF §16.3, §20.2].** τ_c = τ^A = 3.60·10⁻³¹ "PROVEN admissible";
    τ^♯ = 1.10·10⁻¹⁴ "⇐ (GF-B^𝔥)" (SF §20.2). The binding stage-0 threshold condition is
    **(TH-ch″) := (TH-ch′) ∧ ε_1 ≤ ε_br/(1.011√N)**, (TH-ch′): ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}, with every RLARGE
    stage-0 small-field threshold (incl. ε_*) ≤ τ_c (SF RSF5-fix TH-1, RSF6-fix TH-2). (TH-ch′) alone is not admissible.
  - **Current ε_1 ceiling [v3-T, A5].** On the class adopted by PROOF session 23 ([SF7-edit]: 𝔠_∞^♯ = 315.19, λ_min ≥ 3.17·10⁻³,
    ε_* = 2.476·10⁻¹³/C_Δ), at τ^A: **ε_1 ≤ min{9.52·10⁻⁴⁰ (TB-1: ≈ 6.7·10⁻⁴⁰), 1.13·10⁻¹⁸/C_Δ, 2.40·10⁻⁷/C_♭, 7.5·10⁻⁵r_♭,
    2.04·10⁻⁹}** (REVIEW_SF_S7 C-3). So **ε_1 ≲ 6.7·10⁻⁴⁰** modulo the unevaluated C_Δ, C_♭, r_♭; the τ_c lever is (GF-B^𝔥),
    which "now moves ε_1 by ≈ 16 orders" (REVIEW_SF_S7 C-2). Every lane's ε_1 = 0.5 numerics are "illustrative, not
    admissible under (TH-ch′)" (SF §16.3); this includes Appendix A's c32/c33 (reading note there).
  - **N5 compatibility [v2-C, updated v3-S A1, A2, A4].** The small-field package covers this file's small-field region only
    if ε_1, ε_loc, ε^J_loc ≤ the N5 background threshold (matching units). Level 0: **ε_* = 2.476·10⁻¹³/C_Δ** on the session-23
    class (N5-w0: 1.7·10⁻²⁴/C_Δ) (PROOF header l.12-16). The 0 → 1 factor is 1/(1 + 36p_L𝔠_∞^♯) ≈ 8·10⁻⁶; level-i ≥ 1
    constants are not covered by CI-bg; the level-uniform form is GAP along the per-level route (CURV-F2′, CURV-F2″)
    (REVIEW_RLARGE_V2 A1). v2's "(BG-unif)" is re-pointed: (i) ⊂ BFT-0 + BFT-1 (θ_w = 0), (ii) ⊂ BFT-2, (iii) ⊂ BFT-3, (iv) ⇐
    BFT-4 (PROOF l.6631). **So K-independent thresholds, hence K-independent exponents and n_♯, exist only under BFT-0, 1
    (θ_w = 0), 2, 4** (PROOF l.6702-6703: N5 "needs, for level-uniformity, BFT-0, 1 (θ_w = 0), 2 and 4"). Row 3a of §4.2.
  - **(TC) for the collar extension [v3-T; HW Lemma W-cb].** ε_loc/2 ≥ (16N + 3)A_dη_q. "Whether RLARGE's ε_loc obeys (TC) is for
    the owner of the thresholds" (HW l.226-227). [hand] Since η_q ≤ ε_1/(256NA_d), (TC) holds whenever
    ε_loc ≥ (16N + 3)ε_1/(128N) (≈ 0.137ε_1 at N = 2); its compatibility with CL (c)'s use of ε_loc (v1 §5) and with
    (TH-ch″) (ε_loc ≤ τ_c) is not checked: unresolved item U3 (§8).
  - [v2-E8, TL-1, SG-2] ε_1 < 2sin(π/N) (implied); the N5-background clause is an EVENT in U, not a change of χ_Q.
- **The defect exponent [v3-T, W8, H8; HW Theorem HW^cap, §18.1, §19 notes].** The unreturned per-defect exponent is
  **a := min{θa_bad, a_A}**, **a_bad := c_pr·min{ε_1², t_pr²}** (HW Lemma W-bad), with **max{6θ, 24θ}(1 + 2Rg_K²) < 1** (HW
  CAP-1) and a_A the exponent of (SDP)^A (§3.3; "If a_A < θa_bad, θ is lowered to a_A/a_bad and nothing else changes", HW §18.1).
  Sources of (c_pr, t_pr): via (REG-min) (primary), c_pr = c_♭/C′², t_pr = C′τ_♭ (c_♭ = 1/640, C′ = 53 at N = 2, L = 3);
  via (AE), c = 1/(2NC_cone), t = 2, C_cone = 2/η_AE ≈ 1.1-2.3·10¹⁵ (N = 2) (HW TE (ii)). **a_bad (= v2's "a_coh") is the binding entry**
  (REVIEW_RLARGE_V2 H8, 2.1 item 4; SQ l.224-225 asks RLARGE to record it as binding: recorded). [hand] At ε_1 ≲ 6.7·10⁻⁴⁰,
  ε_1 < t_pr on both routes, so a_bad = c_prε_1²: ≈ 2.5·10⁻⁸⁵ via (REG-min) (consistent with REVIEW_SF_S7 TB-1's "a_bad
  4.2·10⁻⁸⁵" at ε_1 = 8.95·10⁻⁴⁰), ≈ 10⁻⁹⁴ via (AE); hence a ≲ 10⁻⁸⁶. v2's a_♯ formula (§3.4) is superseded for unreturned
  defects (§3.5). **Requirement recorded (REVIEW_HIST_S3/S4 via REVIEW_RLARGE_V2 H5): g² ≪ ε_1²·10⁻¹³ wherever the CLS-cone
  price must beat per-defect entropy** (energy route); on the HW route the corresponding requirement is HIST-sum's and
  REL-seq's smallness conditions on e^{-a/g_K²} (§5).
- **Flow hypothesis (F_R) and its quantifier [v2-F, v2-E1 with E1-a, E1-b; unchanged].** Along **the soft chain's own
  effective coupling sequence** (u_k) (FLOW Def F-g; node A5):
    **(F_R)_{[0,k]}:  β_-(m - j)log L - R ≤ u_j - u_m ≤ β_+(m - j)log L + R  for 0 ≤ j ≤ m ≤ k,**
  0 < β_- ≤ β_+, R ≥ 0 fixed (FLOW Theorem F-flow: R = 2R_0, β_± = β_0^std ± C_ργ²/log L; FLOW (F-3), l.67-68: "If g_0, …,
  g_{n-1} ∈ (0, γ], then for all 0 ≤ j ≤ n" the bracket holds). Sufficient bracket (E1-b) and reason as v2 §0. "The chain's
  own sequence" is a fixed-point condition (A5's content).
- **Lemma F-mono [v3-S, F5; FLOW l.1296-1330: "PROVEN-HERE (arithmetic; given the hypotheses of Theorem F-flow)", not counted
  separately ([RFL3-fix tally]); CONFIRMED-WITH-FIX S3-2 per REVIEW_RLARGE_V2 F5].** If g_0, …, g_k ∈ (0, γ]:
  (i) u_k − u_{k+1} ≥ β_- log L − R ≥ −R; (ii) g_k² ≤ g_{k+1}²/(1 − Rg_{k+1}²) ≤ 2g_{k+1}² for g_{k+1}² ≤ 1/(2R), and
  e^{−a/g_k²} ≤ e^{aR}e^{−a/g_{k+1}²}; **1/g_{k+1}² ≤ 1/g_k² + R (⋆)**; g_{k+1}^{-p} ≤ g_k^{-p}(1 + Rg_k²)^{p/2}; (iii) exact
  monotonicity g_k ≤ g_{k+1} "is NOT implied by (F_R) in general", and its availability for all k ≥ k_0 "rests on Corollary
  UNIV-rate, which is a GAP". All five HIST uses H1-H5 are "COVERED"; H3 (Λ^J_1 → (1 + R)Λ^J_1) was not in v2's K4 list.
  **Still owed by HIST:** restate CL^J's Setting as "g_{k+1}^{-2} ≤ g_k^{-2} + R, g_k, g_{k+1} ≤ min{1, √κ}/√2" and carry the
  R-dependence of C_J and Λ^J_1 (FLOW l.1327-1328; HIST l.190, 349, 767 still say g_k ≤ g_{k+1}). Row 4a of §4.2.
- **Consequences of R > 0 [v2-F, unchanged in kind].** Every "priced at the finer coupling" use acquires e^{aR}; v1 §7.2 (iv)'s
  "g_j ≤ g_K by (F)" reads g_j² ≤ g_K²/(1 - Rg_K²) ≤ 2g_K² for g_K² ≤ 1/(2R) ("CORRECT. It agrees with F-mono (ii)",
  REVIEW_RLARGE_V2 §2.3); HIST-sum's step (5): C_ℓ → C_ℓe^{aR}; (P2) uses β_+ for the prefactor. On the HW route the bad
  window is priced at its own level's coupling u_j, so the defect price itself carries no e^{aR} (HW Theorem HW); HIST-sum's
  constant uses C_ℓe^{aR} (HW RHW1-fix W-4).
- **Sign of the coupling shift [v3-S, F4: K1 resolved].** R1 (iii)/R1^J add +δβΣs(U_p) to the log of the integrand, i.e.
  **u → u - δβ**. FLOW agrees: β[𝒮^{LF}_k] = −δβ_k (FLOW l.204-205); "K1 is right" (REVIEW_FLOW_S3 l.34, as quoted by
  REVIEW_RLARGE_V2 F4). No bound changes.
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
- **v1 §1A [R1617-fix, session 18; R1819-fix 8, session 20]** (text in RLARGE_v1_snapshot.md l.95-161): (1) one exponent a_♯
  and n_♯ := ⌊4/(a_♯β_-)⌋; (2) two thresholds: returned vs unreturned decided by the defect number alone, collar-bad
  configurations returned; (3) (RLF-0)/(RLF-1) indexed by connected supports S, extracted only at levels with T_k ≥ W :=
  2n_♯ + 5, wrap levels a bounded term; (4) Z_K^ref defined; (5) (SF-last) added to (RLF-4); (6) (RLF-5) complex fields added.
- **v2 amendments (v2 §1.1, l.148-163, kept):** [v2-E1] quantifier "the soft chain's own effective coupling sequence, obeying
  (F_R), with g_K ≤ g_0" (§1.0 not edited, E1-a); [v2-E2] collar-badness by σ_Q, the "(H-ch) fails" clause deleted
  (SHADOW); [v2-E3] σ-restricted gas, collar-bad activity family, extraction at V = 1 after the sea average; [v2-H] joint
  route (CL^J, R1^J, R1_Λ), representation (I_k^E), δβ_k shifts u_k of u_k𝓔_k; [v2-H] n_♯ ≥ n_H, ≥ n^J_*; [v2-H] (RLF-3) per
  history (the (H-w) form); [v2-F] (RLF-δ)_k from (F_R)_{[0,k]} only (FI-1); [v2-E7] hypercubic tori; [v2-A] (PLD)_k removed,
  three-way pricing.
- **v3 amendments (this file), each against v2 §1.2:**
  - **[v3-3′]** (RLF-3) is restated as **(RLF-3′)**: exponent a = min{θa_bad, a_A} (not a_♯); reference Z(∅) (HW (ref-a)), not
    Z_K^{sf}; per-component shadow form (Lemma HS′); C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc; the passage to Z_K^{sf} goes through
    (NA-∅) in the NA-1 form (REVIEW_RLARGE_V2 W8, 2.2 item 3, Required fix 3; HW §19 notes). v2's (RLF-3) text is kept below,
    marked superseded.
  - **[v3-V1]** [v2-A]'s "three-way pricing" (one branch per defect, prices multiplied) is withdrawn as written: the defect
    price is HW's forward joint moment under μ_{R(𝔥)} (§3). (PLD)_k stays not a hypothesis.
  - **[v3-4]** (RLF-4) states the (NA-∅) link explicitly (with 𝒱_K^{LF}).
  - **[v3-δ]** (RLF-δ)_k: the g_{k+1}-dependence of the stage-k constants (FI-1, §4.4) is named; the exponent is node A's
    returned-cluster exponent a_ret (§1.2 (RLF-0)), not v2's a_♯ formula.
  - **[v3-5]** (RLF-5): the S4-5 conflict with (I_k^E)″ (b″) and its two options recorded (REVIEW_HIST_S4 S4-5).
  - **[v3-R1]** (RLF-2): each returned cluster is priced in-step at its own level with level-uniform constants and its sum is
    renormalised, never bookkept (REVIEW_HW_S2 §5.1; HW §18.1); read as a probability bound it is (SDP)^A.
  - **[v3-cb]** Scope: the HW route covers bad cubes (D-a) for SU(2); collar-bad / non-quiet cubes only via W-cb with (TC);
    SU(N ≥ 3) needs (KS-N) (§2.3, §3.6).

### 1.2 Theorem RLF, v3 (amended target; OPEN)
There are constants ε_1 > 0, θ ∈ (0, 1), a_bad, a_A, a_ret > 0, κ_d > 0, C, B_0, an integer n_♯ ≥ max{n^J_*, n_H} and g_0 > 0,
independent of g, K, T and the history, such that for every K, every hypercubic torus with T ≥ 3, and **the soft chain's
own effective coupling sequence (g_k) with g_K ≤ g_0 obeying (F_R) (§0)**, with a := min{θa_bad, a_A},
max{6θ, 24θ}(1 + 2Rg_K²) < 1 and W := 2n_♯ + 5:
- **(RLF-0) Counterterms.** For each level k with T_{k+1} ≥ W there are field-independent infinite-volume numbers
  c̄_0^{sea}(g_k) and δβ_k (= δβ_k^{sea} of (W1-ret′^J)_k (a)), with |c̄_0^{sea}| + |δβ_k| ≤ Cg_k^{-p}e^{-a_ret/g_k²} (p a fixed
  power; PLD Proposition W1R gives p = 6 + p(SC)); translation invariant; ONE coupling shift per level by B_4 (GT-lat′ (ii),
  W1R-sym; hypercubic torus). Σ_k|δβ_k| ≤ Ce^{a_retR}e^{-a‴/g_K²} for every a‴ < a_ret ((P2), β_+ in the prefactor).
  **[v3-δ]** v2 wrote a_♯ here. a_ret denotes the exponent of the returned-cluster bounds of (W1-ret′^J)_k (a)-(b), a node-A
  output; **no source states its value** (v2's a_♯ list, §3.5, was a formula for the joint price of defects; unresolved item U1,
  §8). HW needs only a_A (§3.3), and lowers θ if a_A < θa_bad.
- **(RLF-δ)_k [v2-F; v3-δ].** For every k: if g_0, …, g_k ∈ (0, γ_0] and (F_R)_{[0,k]} holds for the chain's own sequence,
  then |δβ_k| ≤ g_k⁶. Derived at level k from data on levels [0, k] only, never from g_K or from (F) on [0, K]. **[v3-δ]** The
  stage-k constants also use the kernel coupling g_{k+1} of K_{k+1} through CL^J (F-mono uses H1-H4); §4.4 records how this
  is read (FI-1 bracket, row 2b of §4.2). The γ_0 needed for Cg^{-p}e^{-a_ret/g²} ≤ g⁶ is g-independent but astronomically
  small (REVIEW_RLARGE_V2 §2.3: "g² ≲ 10⁻⁹⁵" with the (AE)-route a_coh at ε_1 ≲ 10⁻³⁹).
- **(RLF-1) Vacuum.** Z_K = exp(𝒱_K^{LF})·Z_K^{ren}, 𝒱_K^{LF} := Σ_{k<K: T_{k+1}≥W}N_{k+1}c̄_0^{sea}(g_k): field- and
  history-independent, the only K-divergent quantity (HIST (P3)). (Unchanged from v2.)
- **(RLF-2) Returned contributions.** Every defect configuration 𝒟 (§2) with n(𝒟) ≤ n_♯ is returned: after the sea average and
  the extraction of c̄_0^{sea}, δβ_k at V = 1 (§2.4), its contribution is a remainder activity that is gauge invariant, C³,
  local up to e^{-κ_dd} tails, and an admissible irrelevant polymer of the small-field package at level k + 1 in the sense of
  (SF-irr)_{k+1}, as a two-field polymer in (U_{k+1}, U_{k+2}) after U_k is integrated. Its summation over levels and cells is
  node A4's contraction. **[v3-R1]** Each returned cluster is priced once, in-step, at its own level with level-uniform
  constants; the sum of those prices is renormalised (c̄_0^{sea} into 𝒱^{LF}, δβ_k into the flow), never bookkept
  (REVIEW_HW_S2 §5.1: "What LF-count, K3-b, P4-div and GAS forbid is BOOKKEEPING the SUM of those prices over levels").
  Read as a probability bound under the relaxed laws, this in-step price is **(SDP)^A** (§3.3), a per-level output of node A.
- **(RLF-3′) Unreturned large fields, per history [v3-3′].** With Z(𝔥) := ∫W·1_𝔥 (§0; Σ_𝔥Z(𝔥) = Z_K), for every admissible 𝔥:
    **Z(𝔥) ≤ Z(∅)·exp(B_0Σ_{(j,𝒟)}Σ_{k=j}^{K-1}|sh_k(𝒟)|)·Π_jΠ_{𝒟∈comp(𝒰_j)}(C_ℓe^{-au_j})^{|𝒟|},
     C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc,  C_fc = c_sf + 81C_Ae^{θa_bad R},  λ_* = 6θ(1 + 2Rg_K²),  n_int = dL^{d-1}(L - 1),**
  (the (H-w′) form of HW Lemma HS′, with B_0 = c_LI + c_f + 164ε_♯ from Theorem HW^cap + Lemma REL-seq), and
    **Σ_{𝔥≠∅}Z(𝔥) ≤ Z(∅)(exp(C_H|T|e^{-(n_♯+1)a/g_K²}) - 1),  Z(∅) ≤ Z_K ≤ Z(∅)exp(C_H|T|e^{-(n_♯+1)a/g_K²})**
  uniformly in K (Theorem HIST-sum with Lemma HS′; C_H computed from C_ℓe^{aR}; n_H computed from this a). Status:
  CONDITIONAL on the §4.2 rows 10-10f (HW §18.1 "Net statement"). Scope: SU(2) (SU(N ≥ 3): (KS-N)); bad-only defects
  (collar extension: §3.6).
  - *Superseded v2 text (v2 l.183-185, kept for citers):* "Z_K = Σ_{𝔥 admissible}Z(𝔥) with every Z(𝔥) ≥ 0 and
    Z(𝔥) ≤ Z_K^{sf}·Π_{j<K}Π_{𝒟∈comp(𝒰_j)}(C_ℓe^{-a_♯/g_j²})^{|𝒟|}·exp(B_0Σ_{k<K}|Ω^c_k(𝔥)|) (the (H-w) form, HIST §7.4), and
    Σ_{𝔥≠∅}Z(𝔥) ≤ Z_K^{sf}(exp(C_H|T|e^{-(n_♯+1)a_♯/g_K²}) - 1) uniformly in K (Theorem HIST-sum, with C_ℓ → C_ℓe^{a_♯R})."
    Its exponent (a_♯) and its reference (Z_K^{sf}) are wrong for the route that is proven (REVIEW_RLARGE_V2 W8).
- **(RLF-4) Output [v3-4].** Under (SF-last) and **(NA-∅)** (NA-1 form, HW §13.3):
    |log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a′/g_K²} uniformly in K,
  with Z(∅) = ∫W·1{every *-component of every D_j has ≤ n_♯ cubes}; with (RLF-3′) and (RLF-1) this gives |log Z_K^{ren} -
  log Z_K^{sf}| ≤ C|T|e^{-a′/g_K²} (any a′ < a, and a′ ≤ the (NA-∅) exponent). Z_K^{ref} := exp(𝒱_K^{LF})·Z_K^{sf,ref} as v1 §1A
  (its soft-RG definition is part of node A). Then exp(-E′_-|T|) ≤ Z_K/Z_K^{ref} ≤ exp(E′_+|T|): L6-soft for this
  normalisation. HW Remark GAS (PROVEN-HERE, arithmetic, uncounted): the returned gas in Z(∅) must be extracted, not
  bookkept, which is why 𝒱_K^{LF} appears in (NA-∅).
- **(RLF-5) Complex fields [v3-5].** Analyticity of the returned remainders, the polymers they feed into the level-(k+1)
  representation, and the large-field factors on the complex neighbourhood node A uses. v2: "The g-uniform width is not
  shown; PLD §9.4 ARGUES width O(g/√κ) for one frozen activity." **S4-5 (binding integration item, REVIEW_HIST_S4):** (RLF-5)'s
  width and (I_k^E)″ (b″) (holomorphy of every polymer on 𝔇_{2ε_1,α_E} with g-independent α_E) "cannot hold for the same
  polymers" — a conflict of targets, not of proofs. Options: (1) primary: "the returned remainders are holomorphic on
  𝔇_{2ε_1,α_E} after re-centring the inner integral at the holomorphic critical branch", with the redefinition of the cut-good
  indicators on the fluctuation about the complex background as its proof obligation; (2) fallback: two polymer classes,
  small-field at width α_E and large-field at width c·g√N/√κ with size e^{-a/g²}, carried separately through (SF^J)_k's
  cluster expansion ("a node A norm decision"). **Not chosen here** (a node-A norm decision; unresolved item U2, §8).
- **Composition.** LF-count, R4D-iso and Theorem CE as v1 §1; the level-K step needs (SF-last). With **EXISTENCE's
  (RLF-3^dis)_v2** (EXISTENCE §17.8): since Z(𝔥) decomposes Z_K (Lemma HR) and (RLF-3′) is relative to Z(∅) ≤ Z_K, ratios
  Σ_{𝔥∈𝒜}Z(𝔥)/Z_K are bounded by Σ_{𝔥∈𝒜}Z(𝔥)/Z(∅) with no vacuum-normalisation fact [inference; answers EXISTENCE's request
  "state whether Z(𝔥) decomposes Z_K or Z_K^{ren}": it decomposes Z_K; the restricted-sum factorisation EXISTENCE uses is
  still ARGUED there; K8, §8].

### 1.3 Numbering map v2 → v3 (for the existence lane and other citers)

| v2 label (place) | v3 label (place) | change |
|---|---|---|
| §1.0 (RLF-0)…(RLF-4), pre-stated | §1.0, verbatim | none |
| §1.1 | §1.1 | v3 list added |
| §1.2 (RLF-0) | §1.2 (RLF-0) | exponent a_♯ → a_ret (node A's; value unstated, U1) |
| §1.2 (RLF-δ)_k | §1.2 (RLF-δ)_k | g_{k+1}-dependence named (FI-1 bracket, §4.4) |
| §1.2 (RLF-1) | §1.2 (RLF-1) | unchanged |
| §1.2 (RLF-2) | §1.2 (RLF-2) | in-step price per level, sum renormalised; (SDP)^A reading |
| §1.2 (RLF-3) | §1.2 **(RLF-3′)** (v2 text kept, superseded) | exponent a = min{θa_bad, a_A}; reference Z(∅); HS′ shadow form; C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc |
| §1.2 (RLF-4) | §1.2 (RLF-4) | via (NA-∅) with 𝒱_K^{LF} |
| §1.2 (RLF-5) | §1.2 (RLF-5) | S4-5 options; K7 → S4-5 |
| §1.3 (v1 → v2 map) | kept in RLARGE_v2_snapshot.md l.196-223 | v1 labels: read v1 → v2 there, then v2 → v3 here |
| §0 thresholds (ε_1, η_1, η_q, [v2-C]) | §0 thresholds | τ_c, (TH-ch″), ε_1 ≲ 6.7·10⁻⁴⁰, ε_*, (TC), a, a_bad binding |
| §0 (F_R), R-consequences | §0 (F_R), F-mono | K4 resolved modulo HIST |
| §2.1 RS ordering "priced before U_k is integrated" | §2.1 | ordering kept; pricing role removed (R-1) |
| §2.2, §2.3 (D-a)-(D-d), §2.4 | §2.2-§2.4 | coverage per family (HW^cap / W-cb / DX-rel / E10) |
| §3 "three-way price" | §3 (re-based) | **forward joint moments under μ_{R(𝔥)}** |
| §3.1 branch (i) | §3.4 (i) = moment (M-i) | plain chain PROVEN (SU(2)); in-history ⇐ (LI)/(LI^F) |
| §3.2 branch (ii) | §3.4 (ii) | implication PLD-desc ⇐ (SG^fl) kept; not consumed by HW; stage 0: DX-rel |
| §3.3 branch (iii) | §3.2 windows (W-bad ⇐ (CLS-min)) + §3.3 fine moment | fixed-V integrand bound and e^{B_0} absorption DELETED (FV) |
| §3.4 case split, greedy factors, a_♯ | §3.5 | superseded (Lemma CH); a_♯ → a |
| §4.1 (I_k^E) | §4.1 (I_k^E)″ | HIST §25.6 |
| §4.2 rows 1-16 | §4.2 rows 1-22 | v2 row number in the last column |
| §4.3 steps 1-7 | §4.3 steps 1-7 | steps 4, 6 replaced (R-1); three non-circularity checks |
| §4.4 FI-1 | §4.4 | g_{k+1} bracket named |
| §5 HIST-sum, (P1)-(P5) | §5 | Lemma HR/RX/HS′, REL-seq; n_H, W, wrap levels recomputed [hand] |
| §6, §7, §8 K1-K10 | §6, §7, §8 K1-K10 (K-numbers kept) + K11-K21 | statuses updated |
| EXISTENCE's (RLF-3^dis) reading of v2 (RLF-3) | reads §1.2 (RLF-3′) | Z(𝔥) decomposes Z_K; reference Z(∅) (K8) |
| "branch (ii)", "branch (iii)" (EXISTENCE §17, other citers) | §3.4 (ii); §3.2-§3.3 | (iii) is now the window lower bound + fine moment |

---

## 2. Defects (definition)

### 2.1 Where the level-(k+1) R-operation acts (RS ordering, HIST §7.1) [v3-R1]
Stage k is the RG step that integrates U_k. Stage k inserts the level-(k+1) large-field indicators into the stage-k integrand
J_k, decides 𝒰_{k+1}, runs the level-(k+1) R-operation on J_k (CL^J, R1^J), and only then integrates U_k (v1 R-9 ordering).
Level-0 cubes are handled by the bare R1 (Appendix A). **[v3-R1] This ordering is a statement about the R-operation's
bookkeeping only; it has no pricing role.** v2's reading "each bad level-(k+1) cube is priced … before U_k is integrated"
(v2 §4.3 step 6) cannot be a fixed-V integrand bound (REVIEW_HW_S1 R-1, as quoted by REVIEW_RLARGE_V2 W6): by Proposition
FV (§3.1) no bound at a fixed coarse field V = U_{k+1} exists. "In-step" is read **forward**: stage k consumes the level-k
effective density and the stage-k kernel, never a fixed-V law (HW §5, Reading of FV).

### 2.2 Bad and collar-bad cubes [v2-E2; v3-cb]
Let Q be a level-(k+1) cube of the current small-field region (or a level-0 cube).
- **Bad:** ζ_Q = 1.
- **Collar-bad (bare form; PLD §9.1 (i)):** σ_Q = 0, σ_Q := 1{max_{p⊂N_1(Q)}||1 - U_p||_op ≤ ε_loc/2 and
  max_{c∈C(Q)}||V_c - S_c(U)||_op ≤ ε_loc/2}; σ ≡ 1 on Y implies ε_♭(U; Y) ≤ ε_loc (CONFIRMED, REVIEW_PLD_S1_S2).
- **Joint form (stage k ≥ 0):** non-quiet cubes (η_k(Q) ≥ η_q on R_k(Q)) are collar-bad. **σ^J_Q is still not stated in any
  source** (K2; "Unchanged: no σ^J_Q anywhere", REVIEW_RLARGE_V2 H10). Read per cube as "non-quiet, or ε^J_♭(D; Q) > ε^J_loc"
  pending I-σ^J (row 14).
- **History-independent defect rule [v3-V1; HW §0].** HW computes D_j by fixed history-independent rules from (U_{j-1}, U_j);
  Lemma RX (ii)-(iii), and therefore Z(∅) ≤ Z(R(𝔥)), use that convention (HW RHW1-fix H-2). HW reads "RLARGE's two-threshold
  collar rule" as possibly history-dependent near Σ(Ω^c_{j-1}) (HW Lemma HR Remark (2)), in which case RX (ii) "can fail".
  σ_Q reads only the sample's own links (§2.2), but no source states that the full defect rule is history-independent near
  the history boundary. **v3 adopts HW's history-independent convention for the HW route** and records the question as K14
  (unresolved).
- **Deleted [v2-E2]:** "(H-ch) fails on Q's box" (Proposition SHADOW). (H-ch)/(H-ch)^J survive only as the Taylor step's chart
  condition.

### 2.3 Defect configurations and which statement prices each family [v3-cb, v3-S A6, W9]
A level-(k+1) **defect configuration** 𝒟 is a *-connected set of bad or collar-bad cubes; n(𝒟) := |𝒟|.
**Returned:** n(𝒟) ≤ n_♯. **Unreturned:** n(𝒟) > n_♯ (join 𝒰_{k+1}; admissibility (A1)-(A2)).

| family | unreturned (history) price on the HW route | stage-0 in-step routing (lane F) | status |
|---|---|---|---|
| (D-a) bad, ζ_Q = 1 | Theorem HW^cap (bad windows, §3.3) | cut-bad history: bare R1 by Wilson positivity (App. A) | CONDITIONAL (§4.2 rows 9-10e) |
| (D-b) collar-bad (σ_Q = 0; non-quiet) | **only** Theorem HW's W-cb extension: (TC), θ < 1/(96·82), (M-i) unreduced on collar links, uncapped (M-f)_{96θ}; **not** HW^cap (HW §19 Scope; REVIEW_HW_S1 W-3 via REVIEW_RLARGE_V2 W9); REL-seq and DECL are proven for bad-only defects (HW §13 preamble), so (REL) is not discharged for this family | **DX-rel** (in-step, PROVEN inequality) for every fine plaquette > τ_c and every mismatch > τ_c, inter-cube included (SF RSF5-fix CH-1) | W-cb CONDITIONAL [uncounted] ⇐ (CLS-min) + (TC); row 10f |
| (D-c) rough inter-cube plaquette in N_1(Q) used as N5 background [v2-E8] | as (D-b) | DX-rel, as (D-b) | as (D-b) |
| (D-d) boundary-adjacent (within distance 1 of ∂Λ(𝔥)) [v2-E10] | **not needed for bad cubes**: "bad windows lie in the cube's own column, inside the small-field columns by Lemma DJ's argument, so no extension of (SG^fl) to ∂Λ(𝔥) is needed in this route" (HW §5.3 (5)); still needed for collar-bad cubes | needed: (CH-c) ⇐ E10 for holes meeting ∂Λ(𝔥) (SF RSF5-fix CH-2) | **E10 OPEN** (row 13) |

**(CH-c) [v3-S A6].** "(CH-c) is CONDITIONAL ⇐ DX-rel (PROVEN inequality) + (DX-loc) [OPEN] + RLARGE E10 [OPEN] + the CH-3 V-scope
(𝒱^sf(Λ′), local ε_bg)" (SF §16.3, RSF5-fix status). SF's owner note for RLARGE, adopted: "at stage 0, §3.4's plaquette leg
above τ_c for (D-b)/(D-c) is DX-rel (in-step), not branches (ii)/(iii); (D-d)/E10 is now on lane F's path". Also: "INF also
needs 𝒞(P) ⊂ 𝒞^♭(Λ_k), i.e. a FULL cone; boundary-adjacent defects stay in E10" (SQ RSQ1-fix S1-1a).

### 2.4 The σ-restricted gas and the collar-bad activity family [v2-E3; unchanged]
- **(α)** Theorem R1 (i) (and R1^J (i), R1_Λ) is run with σ in place of (H-ch); written proof not yet (I-σ, row 14).
- **(β)** The returned collar-bad configurations are an explicit activity family 𝓗^{cb}_X(V) of (SC)_k. **[v3-V1]** v2's
  "Its price is the three-way price of §3" now reads: its in-step price is node A's ((RLF-2), (SDP)^A); when such a cube is
  unreturned it is priced by W-cb (§3.6).
- **(γ)** No pointwise Taylor extraction in the level-k sample; extraction after the sea average at V = 1 (W1R-sym + W1R-tay,
  PROVEN-HERE, CONFIRMED-WITH-FIX). The two-field form is I-tay^J (row 15). HW Lemma K3-b (PROVEN-HERE, arithmetic,
  uncounted): the in-sea extraction-collar cost "is not summable as bookkeeping", which supports E3; the Ω^c-attached part
  is summable (≤ 1 in B_0, Lemma K3-a). K3 settled except I-tay^J.

---

## 3. The price of an unreturned defect: forward joint moments under one conditioned law [v3-V1]

**What v3 replaces, and why (REVIEW_RLARGE_V2 Part 2.1, verdict "NOT SOUND AS WRITTEN; repairable by re-basing on HW").** v2
§3 priced each defect by one of three branches and multiplied the prices; v2 §3.3 stated branch (iii) as a fixed-V
integrand bound whose removed-cone normalisation "must be absorbed by the history bookkeeping (e^{B_0} per boundary cube)".
That sentence is **deleted** [v3-R1], and the §3.4 case split, greedy factors (7⁴, 81, 5⁴), RS-joint and a_♯ formula are
superseded for unreturned defects (§3.5). The content below is HW's (HW §2-§5, §13-§15, §18), with HW's statuses.

### 3.1 The lesson of Proposition FV
**Proposition FV [HW §5; CONDITIONAL ⇐ (CLS-min); uncounted; "CONFIRMED as CONDITIONAL ⇐ (CLS-min) by REVIEW_HW_S1 l.235-251"
per REVIEW_RLARGE_V2].** For every k, every level-(k+1) cube Q, every V with ζ_Q(V) = 1 and EVERY level-k field U:
  κΦ_{int Q}(U, V) + F^col_Q(U) ≥ a_bad = c_pr·min{ε_1², t_pr²};
hence for every family of conditional laws of U_k given U_{k+1} = V and every λ > 0,
sup_V E[exp(λu_k(κΦ_{int Q} + F^col_Q)) | U_{k+1} = V] ≥ exp(λa_bad/g_k²).
**Lesson (stated for every consumer of this file).**
1. At a fixed bad coarse field, mismatch plus fine energy cannot be small: the normalisation of any "removed-cone" integrand is
   ≥ e^{θa_bad u_k}, and it **cancels the price exactly** (Lemma EQ: the moment E_μe^{θX} IS the removed-window normalisation).
2. The suppression of bad V lives in V's own law; it can only be collected **forward**, as a moment under the level-k
   marginal and the kernel (KS-chain factorisation: kernel moment given U_k, exact, times a moment under the level-k law).
3. FV does not refute branch (ii)'s forward law μ^+ (U from μ_{𝔥,ω}, then V from the kernel) on good V (HW RHW1-fix H-6);
   it refutes every fixed-V ("integrate U_k at fixed U_{k+1}") reading of branch (iii) and of v2 §4.3 step 6.
4. Probabilities taken under different laws (RS-joint under W/Z_K, PLD-desc under μ^+_{𝔥,ω}, branch (iii) under "an unnamed
   law") cannot be multiplied; that, "and not 'probability versus integrand', is why they did not combine" (HW §5.3 (1)). K5
   is resolved for bad cubes.
5. Z_K-relative probabilities are the wrong currency: Proposition PF (HW §3.1, PROVEN-HERE, elementary): Z_K-relative
   per-history bounds carry no information on Z_K/Z(∅); every bound must be relative to a reference that does not see the
   defects. Hence (ref-a) Z^sf := Z(∅).

### 3.2 The single law, the windows, and the combination
- **The law.** μ_{R(𝔥)} (§0): the chain conditioned on "no unreturned defect outside 𝔥's own regions". For Lemma REL-seq the
  laws of the restricted relaxed family **ℛ_𝔥^↑** (S ⊇ S(𝔥), level-first ascending relaxation, step animal declared; HW
  RHW2-fix RS-1) are used as well; every moment hypothesis below is stated on ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}} only.
- **Lemma CH [HW-2] (PROVEN-HERE, counted).** For X_Q ≥ 0 bounded with X_Q ≥ π_Q on {Q ∈ D_j}:
  Z(𝔥) ≤ Z(R(𝔥))·exp(-θΣ_Qπ_Q)·E_{μ_{R(𝔥)}}[exp(θΣ_QX_Q)]. "No probability, conditional independence, greedy subfamily or
  disjointness of supports is used; the defects of all levels enter one pointwise product." Lemma CAP (ii): CH holds with
  X^cap_Q := min{X_Q, π_Q}.
- **The coherent-background lower bound (one energy threshold per defect).** Lemma TE + Lemma W-bad [HW-1] (CONDITIONAL ⇐
  (CLS-min); level 0 PROVEN-HERE by (B)): for a bad level-(k+1) cube, X_Q := u_{k+1}Σ_{P∈𝒫(Q)}ℰ_P(V) ≥ a_bad·u_{k+1} = π_Q.
  ℰ_P(V) is the cone-local free-boundary minimum 𝓔^{𝒞(P)}(V) (HW §12A: "every use is the infimum", CONFIRMED by REVIEW_HW_S2).
  **This is where the coherent background is priced: (CLS-min)_{c_pr,t_pr}**, primary source **(CLS-min) ⇐ (REG-min)** (SQ
  DESC + SUP-price + PRICE-iii; Corollary DESC-ε "CONFIRMED as CONDITIONAL" ⇐ (REG-min), REVIEW_SQ_S2 tally), parallel source
  (CLS-min) ⇐ (AE) ⇐ (MS-Sob) (AE-red, CONFIRMED as CONDITIONAL, REVIEW_HIST_S4). Lemma DJ: the bad windows of distinct
  (k, Q), Q ∈ 𝒰_{k+1}, use disjoint term sets.
- **The upper split (mismatch / fine).** Lemma CAP (iii): X^cap_Q ≤ Y^mis_Q + min{π_Q, Y^f_Q}, Y^mis_Q := 6κu_{k+1}Φ_{int Q}(U, V)
  (**mismatch**, branch (i)'s object), Y^f_Q := 24u_{k+1}F^col_Q(U) (**fine column energy**: fluctuation and coherent
  background of the finer fields together; "The split of the fine part into fluctuation and background (PLD-desc's B_V) is
  not needed anywhere below", HW §4 Reading).

### 3.3 The three moment inputs and the conditional theorem
- **Mismatch moment (M-i)** ⇐ Lemma H4-red′ [HW-7] (PROVEN-HERE, counted; SU(2); bad-only; "CONFIRMED (SU(2), CONDITIONAL ⇐
  (LI^F))", REVIEW_HW_S2): the int(𝒰) links are peeled exactly, level by level from the top, with Lemma KS (c)
  ∫k_ce^{λκuφ} ≤ (1 - λ)^{-3/2} (uniform in M, u, κ), the fine factors riding as spectators. Consumes **(LI^F)** (future
  insensitivity with the capped spectator weights only, LI-1) [OPEN, HW]. Plain chain, no hypothesis: Lemma KS-chain [HW-4]
  (PROVEN-HERE, SU(2)). SU(N ≥ 3): **(KS-N)** [HYPOTHESIS, s].
- **Fine (fluctuation) moment, capped (M-f^A)_θ** [HW §18.1]: E_R[Π_{Q∈A}e^{θmin{π_Q,Y^f_Q}}] ≤ C_fc^{|A|}e^{c·shadow sums},
  C_fc = c_sf + 81C_Ae^{θa_bad R}, the same constant at every level; **(M-f^A)_θ ⇐ (SF-cap)^A_θ + (SDP)^A_θ** by Lemma CAP-dec
  (PROVEN-HERE, elementary, "RECOUNTED as uncounted", REVIEW_HW_S2).
  - **(SF-cap)^A_θ** [OPEN; node A]: c_sf at rate 24θ(1 + 2Rg_K²) < 1 on defect-free columns, uniformly under conditioning on
    finer defects in other columns (the small-field fluctuation half; source: F^col_Q ≤ Σ_{x under Q}𝓔_{k,x} plus node A's
    local coupling response).
  - **(SDP)^A_θ** [OPEN, P; node A]: for every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}}, every k, every set S of level-k cubes in Λ_k:
    μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·exp(c_A·shadow sums), a_A ≥ θa_bad. It is (RLF-2)'s in-step returned price read as a
    probability, "proven at each level k separately from: the stage-(k-1) R-operated representation, (I_{k-1}^E)′ in its
    two-field form (d); (CLS-min) for the in-step window; (W1-ret′^J)_{k-1} (c); (SC)_{k-1}; R1^J's gas convergence …; the
    (LI)-type future tilt. **It is never derived from (SDP)^A at level k - 1.**" Lemma LOOP-const (PROVEN-HERE, arithmetic about
    the bound) shows it is not obtainable by column induction inside ∫W·1_𝔥 (LF-count at n = 1, ×81 per level). Node A must
    use the non-saturating split its R-operation encodes: a returned finer cluster enters as c_0(Y) + T_Y·(coarse curvature)²
    + R(Y)𝔯, i.e. (W1-ret′^J) (a)-(b) + I-tay^J + (SF-irr) (HW §18.1, REVIEW_HW_S2 §5.4).
- **Coherent background: (CLS-min)** (§3.2), through TE (ii) only.
- **Theorem HW^cap [HW-7] (CONDITIONAL; implication PROVEN-HERE; counted; "CONFIRMED-WITH-FIX", CAP-1, LI-1).** Under (F_R)
  with g_K² ≤ 1/(2R), (CLS-min), SU(2), bad-only defects, (LI^F) and (M-f^cap)_θ with max{6θ, 24θ}(1 + 2Rg_K²) < 1:
  Z(𝔥) ≤ Z(R(𝔥))·exp((c_LI + c_f)·shadow sums)·Π_jΠ_{Q∈𝒰_j}[e^{-θa_bad u_j}(1 - λ_*)^{-3n_int/2}C_fc].
- **Lemma REL-seq [HW-6] (CONDITIONAL; counted; "CONFIRMED-WITH-FIX (CONDITIONAL, implication proven; counted [HW-6])", RS-1).**
  Under (F_R) (lower half), (PRICE^ℛ) on ℛ_𝔥^↑, n_♯ ≥ n_H (with B_0 ≥ c) and ε_♯ ≤ ½: Z(R(𝔥)) ≤ Z(∅)·exp(164ε_♯·shadow sums),
  B = 164ε_♯ → 0 as g_K → 0. (SDP)^A on ℛ_𝔥^↑ with S = 𝒟 gives (PRICE^ℛ) directly (HW §18.1 Remark). **(REL) is no longer an
  independent residual.**
- **Net (HW §18.1, CONDITIONAL; implications proven):** **(H-w′) ⇐ (F_R) [g_K² ≤ 1/(2R)] + (CLS-min) + (LI^F) + (M-f^A)_θ**,
  via HW^cap and REL-seq on ℛ_𝔥^↑, with a = θa_bad, C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc, max{6θ, 24θ}(1 + 2Rg_K²) < 1; scope SU(2),
  bad-only. Then HIST-sum (with HS′) gives (RLF-3′). The passage Z(∅) → Z_K^{sf} is (NA-∅) (§1.2 (RLF-4)).

### 3.4 What the three v2 branches became [v3-V1]
- **(i) Kernel mismatch** = the moment (M-i). "PROVEN for the plain chain stands (RS, RS-lin, KN, and for SU(2) the exact
  moments of KS-chain)"; in-history it is H4-red′ ⇐ (LI^F) (HW route), not "≤ e^{Σ|ρ|} × kernel" (H-4) (REVIEW_RLARGE_V2 2.1
  item 1). v2 §6's "unconditional" reads "plain chain; in-history ⇐ (LI) [SU(2); (KS-N) for N ≥ 3]". Statements kept from
  v2 §3.1 for the representation route and for collar links: Lemma RS (R3)-(R4), RS-lin (b)-(c), Lemma KN with KN-step,
  CL^J (c)'s numerator, PLD-SG/§9.5 at t = ε_loc/4.
- **(ii) Fluctuation about the background.** "The implication PLD-desc ⇐ (SG^fl) is correct. It is valid only on good V (𝒱^sf),
  with a forward law μ^+ … However, no route to (H-w) now consumes it: HW does not, and stage 0 uses DX-rel for (D-b)/(D-c)
  above τ_c. The (SG^fl) row survives only as a node-A clause" (REVIEW_RLARGE_V2 2.1 item 2). Proposition PLD-desc (PROVEN-HERE,
  CONFIRMED-WITH-FIX, PD-1), Lemma HS-net, Proposition INH, PLD-SG as an implication: unchanged. The fluctuation content
  consumed on the HW route is (SF-cap)^A.
- **(iii) Coherent background** = the window lower bound X_Q ≥ a_bad·u_{k+1} (W-bad ⇐ (CLS-min)), plus the fine moment for the
  upper side. v2's "chain-energy bound in ℒ_𝔥 … the removed-cone integrand is the history in which the cube is large-field"
  is the RG-direction reading refuted by FV and is withdrawn. What v2 called CLS-sf in cone form is (CLS-min) (equivalent to
  the every-chain form on a full cone, SQ RSQ1-fix S1-1).

### 3.5 Superseded v2 §3.4 (case split, joint pricing, a_♯) [v3-V1]
For unreturned defects the case split (RS dichotomy → mismatch / fluctuation / background), the greedy disjointness factors
7⁴, 81, 5⁴, RS-joint's c_RS = 81 ⇐ (PLD-q)_k, and the a_♯ := min{…}/greedy formula are **not consumed** (HW §5.3 (5): "Not
consumed by Theorem HW: RS-joint, (PLD-q)_k, (SG^fl)_k, PLD-desc, (BG)_k, the case split of RLARGE §3.4, and the boundary family
E10"). They remain valid as statements where proven (RS-joint CONDITIONAL ⇐ (PLD-q)_k on the plain measure) and are kept in
RLARGE_v2_snapshot.md l.363-378. The exponent of unreturned defects is a = min{θa_bad, a_A} (§0). v2's remark "No counted item
depends on a_♯ or n_♯" stands for the frozen lemmas (R1/R1^J hold for every cutoff n_c ≥ n_*, n^J_*).

### 3.6 Collar-bad and non-quiet unreturned cubes (W-cb extension) [v3-cb]
Lemma W-cb (CONDITIONAL [uncounted] ⇐ (CLS-min) and (TC)): X^cb_Q := κu_kΦ_{C(Q)} + u_kΣ_pℰ_p ≥ a_cbu_k with a_cb := min{c_pr·min{
ε_loc²/4, t_pr²}, κε_loc²/(64N), c_pr·min{η_q², t_pr²}}. Theorem HW's proof with these windows gives the price e^{-θa_D(u_j - R)},
a_D := min{a_bad, a_cb}, with θ ∈ (0, 1/(96·82)) (collar windows overlap ≤ 82 times; RHW1-fix W-3), (M-i) and (M-f)_{96θ} for
the collar sums **as stated** ("The reduction of (M-i) to (LI) below does NOT cover collar links, which are also read by the
neighbours' collar clauses inside R(𝔥) (Conflict K2's territory)"), and (REL) not discharged by REL-seq (bad-only). This
family is a separate open row (10f) and the main source of E10's remaining need.

---

## 4. The inductive step over levels

### 4.1 The representation (I_k^E)″ [v3-S H1, H2; HIST §25.6]
(I_k^E)″ (HIST §25.6, HYPOTHESIS, P) is §14.1/§20.3 (C) with: (a″) main term u_k𝓔^{an}_k (Theorem A5 (C)); (b″) polymers
E_k(X; ·) holomorphic on 𝔇_{2ε_1,α_E}(X), α_E ≤ s_5/4 g-independent; (c) unchanged (large-field factor; under v3 the
unreturned prices are those of §3, not entered into ℒ_𝔥 at fixed V); (d″) two-field form u_k[𝓔^{an}_k(U_k) + κΦ^{♭,ℂ}_k(U_k,
U_{k+1})] + polymers + R1^J remainders + coupling-shift polymer + the kernel normalisation (NORM-an). Hypothesis items: (a3-q),
(a4), (a5) := (a5-G) + (a5-U). (I_0^E) holds (𝓔_0 = Σs, E_0 ≡ 0).
**Status (REVIEW_HIST_S4):** "(I_k^E)″ | HYPOTHESIS | Stated; inherits S4-1/S4-2; conflicts with (RLF-5)'s width as stated
(S4-5)". S2-1, S2-3 repaired; S2-2 repaired once S3-7's notation fix is applied; new defects S3-6, S4-1, S4-2, S4-5 (as
quoted by REVIEW_RLARGE_V2 H1). **Theorem A5 is ARGUED**, not CONDITIONAL: "(a5-G) is false in ℓ^∞→ℓ^∞" (S4-1, G ≳ L^{2(k-1)}
at the trivial chain) and the base-set gap S4-2; after restatement "CONDITIONAL ⇐ (a5-G♯) + (R♯) + (a5-U) + (a3-q) +
(MS-Sob)" with (R♯) OPEN, PROOF-owned. HIST l.1683 still says CONDITIONAL (stale in the lane file; REVIEW_RLARGE_V2 H2).
**Naming note [v3-S]:** HW §18.1 writes (I_{k-1}^E)′ (d) as an input of (SDP)^A; read (I_{k-1}^E)″ (d″) (K17).
**Why not v1's (I_k):** (D1-c)/H-2 (unchanged from v2).

### 4.2 Complete named-hypothesis list for RLF-step v3 [v3-L]

Columns: owner file; status quoted from the latest review that judges the item (lane file where none, marked); tag; weight
(owner's, where given); v2 row. "HW-route" = consumed by (RLF-3′) through §3.3.

| # | hypothesis (statement at) | owner file | current status (source) | tag | weight | v2 row |
|---|---|---|---|---|---|---|
| 1 | **(F_R)** along the chain's own sequence (§0) ⇐ F-flow ⇐ (UNIV-1L) ⇐ Theorem UNIV | FLOW §4, §7, §80 | F-flow, F-tune CONFIRMED conditional (REVIEW_FLOW_S1_S2). Theorem UNIV for SU(N): "rests on (L-loc2), (VFINE), (VC-V) and (DEF), of which (VFINE) and (VC-V) are of the type proved here for the scalar, and (DEF) is new" (FLOW §80, session 10, **unreviewed**); (L-loc2) ARGUED; (VFINE) [s], (VC-V) [s], **(DEF) [s-P], "the crux"**; scalar-proxy (UIR) PROVEN (Theorem UIR-S, session 10, unreviewed); k-uniform vector step gap OPEN [s]. Last **reviewed** OPEN list: "(V-IR) in the form (Q1)(d) …; (V-IR-S), now (UIR) …; the vector off-shell defect …; (L-loc2)" (REVIEW_FLOW_S9 §7). Lemma U-loc′ CONFIRMED (counted) (REVIEW_FLOW_S3 l.203, via REVIEW_RLARGE_V2 F2); (U-IR) dissolved (F3); (IRR*) retired | [FLOW] | **P** (node A5) | 1 |
| 1a | layer-1 inputs of F-flow: (SF-g), (SF-cont), (SF-∞); (SF-bg) | FLOW §4; node A | (SF-g), (SF-cont), (SF-∞) ⊂ node A (as v2); (SF-bg) "is no longer used by UNIV (Lemma TOW, CONFIRMED)"; where node A uses it, it is BFT-2, 3 at the trivial field (REVIEW_RLARGE_V2 F6; PROOF l.6633) | [A]/[BFT] | inside 3 | 1 |
| 2 | **(RLF-δ)_k** per level, from (F_R)_{[0,k]} only | this file (FI-1) | delivered by (W1-ret′^J)_k (a)'s bound if that bound uses only g_k ≤ γ_0 (as v2) and row 2b | [R] | s, given 5 | 2 |
| 2b | **FI-1 g_{k+1} bracket** (§4.4): the stage-k constants use the kernel coupling g_{k+1} (CL^J, F-mono H1-H4) | this file / HIST / FLOW | NEW item (REVIEW_RLARGE_V2 2.2 item 4(b): "§4.4's 'met by the structure' should name this"); reading chosen in §4.4 [inference, not checked against F-ind's proof] | [R] | not assigned (integrator's estimate: s) | — |
| 3 | **(SF^J)_k** = node A1-A4 (small-field step, two-field output in the (I_{k+1}^E)″ form, level-uniform thresholds, clauses (SF-irr)_{k+1}, (RLF-5)'s width, (SF-cap)^A, (SDP)^A) | SF.md; PROOF N2, N4, N5, N6; HIST §6, §8 | SF: "A1.0 PROVEN; A1.k OPEN; A3's CE and RW proven but their composition at k ≥ 1 not written; A4 all HYPOTHESIS/OPEN"; open names "(DX-loc-3/4), (GF-B^𝔥), (GF-dec)_k, (C_♭-eval), the C_Δ evaluation"; "No RLARGE §4.2 row discharged" (REVIEW_SF_S7 E-1; SF l.49-52) | [A] | **P×3-4** | 3 |
| 3a | **N5 level-uniformity** (was (BG-unif), now re-pointed to BFT) | PROOF [S23]; BFT_A.md, BFT_B.md | needs BFT-0, 1 (θ_w = 0), 2, 4 (PROOF l.6702-6703); per-level route GAP (CURV-F2′, CURV-F2″); NAH-unif′ GAP as written; COMP GAP ((CL-4)) (PROOF header l.8-10); BFT OPEN, clause table PROOF l.6693-6698 (row 23 below) | [BFT]/[A] | **P** | 3a |
| 3b | **stage-0 out-of-chart (CH-c)** and **(SG^fl)_0** | SF.md §16.3 | (CH-c) "CONDITIONAL ⇐ DX-rel (PROVEN inequality) + (DX-loc) [OPEN] + RLARGE E10 [OPEN] + the CH-3 V-scope"; (SG^fl)_0 ⇐ O2 + O3 + O4 + N5-sf0 + (G0-1)-(G0-4) + (I_0^E) + (BG)_0 + (TH) on the non-circular O-chain O0-O5 (SF §16.3; CONDITIONAL per REVIEW_RLARGE_V2 A8); it must consume only CE-Q (band), not CE-Q^∞ (REVIEW_SF_S3 l.223 via A8) | [A] | inside 3 | 3, 7 |
| 3c | **(C_♭-eval), C_Δ evaluation** (binding iff C_Δ ≳ 1.2·10²¹ after the rerun), **(GF-B^𝔥)** (τ^♯; moves ε_1 ≈ 16 orders), **(MIN_1)**, small tori, FP_U's background dependence, **(CL-4)** | PROOF; SF.md | OPEN (PROOF l.6706-6707; REVIEW_SF_S7 C-2, E-1) | [A] | s (owners) | — |
| 4 | **(I_k^E)″** (§4.1) | HIST §25.6 | HYPOTHESIS; inherits S4-1/S4-2; S4-5 (REVIEW_HIST_S4); Theorem A5 ARGUED ⇐ (after restatement) (a5-G♯) + **(R♯)** [OPEN, PROOF/N2-owned] + (a5-U) [OPEN, HIST] + (a3-q) [OPEN, HIST] + (MS-Sob); (a4) ARGUED | [A] | **P** (statement fixes s) | 4 |
| 4a | **CL^J Setting restatement** (F-mono H1-H5, incl. H3) | HIST (owner) | owed by HIST (FLOW l.1327-1328; REVIEW_RLARGE_V2 F5, "Still owed by HIST") | [A]/[FLOW] | s | (K4) |
| 5 | **(W1-ret′^J)_k** (a)-(c): sea average of the σ-restricted joint gas; c̄_0^{sea}, δβ_k at V = 1; returned remainders admissible two-field polymers; (c) the in-step returned price (feeds (SDP)^A) | HIST §8; PLD §9 (Prop. W1R) | W1R: (a)-(b) CONDITIONAL ⇐ (SC)_k + (SF-irr)_{k+1} (one-field form) (as v2; PLD unchanged); unreturned prices are no longer this row's (§3) | [A] | s to P | 5 |
| 5a | **(SC)_k** fixed-V sea expansion with the collar-bad family | PLD §9.4 | HYPOTHESIS (as v2) | [A] | s to P | 5a |
| 5b | **(SF-irr)_{k+1}** admissibility of C³, local, 𝔯^♭-bounded activities | PLD §9.3 | HYPOTHESIS, part of node A ("the A4 wall", REVIEW_RLARGE_V2 Part 3) | [A] | inside 3 | 5b |
| 6 | **(H-Mayer^J)_k** | HIST §8 | ARGUED (REVIEW_HIST_S1, S2; as v2) | [A]/[R] | s, given 5 at k - 1 | 6 |
| 7 | **(SG^fl)_k, k ≥ 1** | PLD §15.2 | HYPOTHESIS; **not consumed by the HW route** ("survives only as a node-A clause", REVIEW_RLARGE_V2 2.1 item 2) | [A] | s given (SF), (I_k^E) | 7 |
| 8 | **(BG)_k** = BFT-3 (R_bg) (+ BFT-1 one-step, C_I) | PLD §15.2 → BFT_B.md | "= BFT-3 (R_bg, load-bearing under v2); C_I = BFT-1 one-step (not load-bearing). BFT-3: k = 1 PROVEN (Theorem BB-3_1); k ≥ 2 ⇐ weighted (H-inv+)_m" (REVIEW_RLARGE_V2 A3). Under v3 it is load-bearing only for (SG^fl)/PLD-desc (row 7) and as FLOW's (SF-bg) (row 1a) [integrator reading; HW §11 lists (BG)_k as not consumed "except through (REG-min)", a reading SQ withdrew, K18] | [BFT] | s | 8 |
| 9 | **(CLS-min)_{c_pr,t_pr}** (HW-route, coherent background) ⇐ **(REG-min)** | SQ.md §0.3 | Corollary DESC-ε "CONFIRMED as CONDITIONAL (M2-1 optional)" ⇐ (REG-min); **(REG-min) OPEN; "its wall = (MIN-reg)_cone"**; "(REG-min) ⇐ (BFT-cone) + (MIN-reg)_cone" is "close to circular"; "The wall did not move closer" (REVIEW_SQ_S2). SQ requires of BFT: θ_w > 1 as a stated value, and a cone-box uniqueness/ε-regularity clause (its item 4) (REVIEW_SQ_S2 Priority 5) | [A] | **P** | 9 |
| 9p | parallel: (CLS-min) ⇐ (AE) ⇐ (MS-Sob) | HIST §15.3, §26 | (AE) CONDITIONAL ⇐ (MS-Sob) (Theorem AE-red CONFIRMED); (MS-Sob) ⇐[ARGUED] MSG-loc-dev + MS-HLS + (SQ-dev) [OPEN]; Theorem MSG CONFIRMED-WITH-FIX (C_M = 66.1); MSG-loc a GAP, MSG-loc′ PROVEN (REVIEW_HIST_S3/S4 via REVIEW_RLARGE_V2 H3, H4). Whether the merger lowers the wall count: UNDECIDED (REVIEW_SQ_S2) | [A] | P | 9 |
| 10 | **(H-w′)** (per-history bound) | HW.md §18.1 | **CONDITIONAL ⇐ (F_R) [g_K² ≤ 1/(2R)] + (CLS-min) + (LI^F) + (M-f^A)_θ** (implications proven: Theorem HW^cap [HW-7] CONFIRMED-WITH-FIX, REL-seq [HW-6] CONFIRMED-WITH-FIX; REVIEW_HW_S2). Its open inputs are rows 9, 10a-10e | [HW] | — (conditional theorem) | 10 |
| 10a | **(LI^F)** (capped spectator weights only, LI-1; over ℛ_𝔥^↑ and R(𝔥)) | HW.md §14 | OPEN (REVIEW_HW_S2 tally: "(LI^F) | OPEN, this file | OPEN (LI-1)") | [HW] | s to P (HW, for (LI)) | 12 (replaces H-4) |
| 10b | **(SDP)^A_θ** (in-step returned price as a probability, per level, never from level k - 1) | node A (HW §18.1; owner files: RLARGE (RLF-2), rows 4, 5, 5a, 14, 15; R1^J) | OPEN, P; "not written anywhere as a probability bound under μ ∈ ℛ_𝔥^↑ (new interface item)" (HW §19 A1); "status WRONG" as HW's wall, re-owned (REVIEW_HW_S2) | [A] | **P** | — |
| 10c | **(SF-cap)^A_θ**, rate 24θ(1 + 2Rg_K²) < 1 | node A (HW §18.1; (I_k^E) main term, (SF^J)_k) | OPEN (REVIEW_HW_S2: "OPEN, node A; rate 24θ (CAP-1)") | [A] | not given | — |
| 10d | **(NA-∅)** (NA-1 form, with 𝒱_K^{LF}) | node A (RLARGE (RLF-1), (RLF-4)) | OPEN; "WRONG AS WRITTEN" in the session-2 form, fixed by NA-1 (REVIEW_HW_S2) | [A] | not given | — |
| 10e | **(KS-N)** for SU(N ≥ 3) | HW.md §5.2 | HYPOTHESIS, s (scalar polar part checked numerically for N = 3 in w1 B; general M not checked) | [HW] | s | — |
| 10f | **collar-bad / non-quiet unreturned cubes**: W-cb with (TC), θ < 1/(96·82), (M-i) for collar links as stated, (M-f)_{96θ} for collar sums, (REL) for non-bad defect notions | HW.md §5.1; this file (TC) | W-cb CONDITIONAL [uncounted] ⇐ (CLS-min) + (TC); "not by HW^cap" (HW §19); REL-seq bad-only (HW §13) | [HW]/[R] | not given | (13, D-b) |
| 11 | **(SF-last)** level-K integrand; **now a many-level item** (wrap levels, §5.4) | v1 §8.2 | HYPOTHESIS; "≈ 60 final levels are affected by the torus clause (wrapped clusters break 'shapes up to translation'), not O(1)" (REVIEW_SF_S5 l.343 via REVIEW_RLARGE_V2 A7) | [A]/[R] | s given (SF) (as v2; scale now larger, K16) | 11 |
| 12 | **H-4** (in-history tilt e^{Σ|ρ|} of the mismatch pricing) | HIST §7.3 | ARGUED; on the HW route replaced by (LI)/(LI^F) (row 10a), "a different object (H-8)" (REVIEW_RLARGE_V2 W7); still relevant for RS-joint in-history | [A] | s | 12 |
| 13 | **E10** boundary-adjacent defects (D-d) | this file; SF (CH-c) | OPEN, unwritten; not needed for bad cubes on the HW route; needed for collar-bad cubes and for (CH-c) at stage 0 ("E10 is now on lane F's path") | [R]/[A] | not assigned (integrator's estimate: s) | 13 |
| 14 | **I-σ / I-σ^J** (written σ-restricted gas; σ^J_Q stated, K2) — input to (SDP)^A via R1^J | this file / HIST | bare: substitution stated (PLD §9.1), proof unwritten; joint: σ^J_Q "Unchanged: no σ^J_Q anywhere" (REVIEW_RLARGE_V2 H10) | [R] | s | 14 |
| 15 | **I-tay^J** (two-field W1R-tay) — input to (W1-ret′^J) and (SDP)^A | PLD / HIST | not written; "the residual is I-tay^J (the two-field W1R-tay), unchanged" (HW §7, K3 outcome) | [R]/[A] | s | 15 |
| 16 | **(RLF-5)** width — **S4-5 decision** (re-centring vs two polymer classes) | node A / lead | conflict of targets (REVIEW_HIST_S4 S4-5, "binding; integration item for the lead") | [A] | inside 3 | 16 |
| 17 | **(SC)**, **(SF-irr)**, **(W1-ret′^J)** at level k - 1 as inputs of (SDP)^A | as rows 5-5b | as rows 5-5b | [A] | — | — |
| 18 | **non-circularity of (SDP)^A** (§4.3 check (a)) | node A / this file | to be confirmed: node A's stage-(k-1) representation must not consume (H-w′) or HIST-sum at levels ≥ k (HW §19 note [inference]) | [R]/[A] | s (integrator's estimate) | — |
| 19 | **history-independent defect rule** (K14) | this file / HW | adopted for the HW route; not stated in any source for the collar rule near Σ(Ω^c) | [R] | s (integrator's estimate) | — |
| 20 | **(TC)** vs ε_loc's other uses (U3) | this file (thresholds) | sufficient condition [hand] §0; compatibility unchecked | [R] | s (integrator's estimate) | — |
| 21 | **assembly C** (L6-soft from RLF + node A bulk bound) | other (CMP 119) | OPEN | [other] | **P** | (§7) |
| 22 | **BFT-5** ⇐ (G♯_0-field) + (R♯_ω) + (G♯-patch) | none | "no status recorded in any BFT review or lane file" (PROOF l.6698); unowned | [BFT] | not given | — |
| 23 | **BFT-0/1/2, BFT-3 (k ≥ 2), BFT-4 (k ≥ 2)** | BFT_A.md, BFT_B.md | PROOF l.6695-6697 (REVIEW_BFT_B_S5, REVIEW_BFT_A_S4): BFT-0/1/2 OPEN on 𝒞_glob ⇐ (H-inv+) [(CO-0), (CO-up), (G♯-rough) curvature half, (SB)] + (Res-Hölder) + LRL (b) + (H-rem^∇) [ARGUED] + (FP♯′) + (N1); BFT-3 k = 1 PROVEN, k ≥ 2 ⇐ weighted (H-inv+)_m; BFT-4 k = 1 PROVEN, k ≥ 2 ⇐ (W-comm) [GAP 1] + (CovLift) + (Mult-Y) + (Pair-loc), (I-id)_Z, (E3^∇) [ARGUED]. Later: REVIEW_BFT_A_S5 calls lane A's "completes the gauge-invariant half of (H-lin^∇)" "OVERSTATED (fix U7)": complete only "for the soft-RG source class …, at m = 0 and the trivial background"; "The level-0 Wilson rows remain OPEN" (not in PROOF's map; K19) | [BFT] | **P** | (3a, 8) |

**Not hypotheses of RLF-step v3 (withdrawn, relocated, or off the HW route):** (H-pos)_k (relocated: Theorem H-pos^J); (PLD)_k
(i)-(ii), (PLD-q)_k ([v2-A]); RS-joint and the greedy joint pricing (§3.5); the fixed-V branch (iii) and its e^{B_0} absorption
(deleted, §3.1); (REL) (discharged by REL-seq, bad-only); (PLD-dis), (NH), (WH), (INF) (existence-lane objects); (CLS-NA)
large-field and (D1-b) ("not consumed; do not attack"; under SDP-1 the pointwise density bound (D1-b) "is not needed",
REVIEW_HW_S2 §5.4); Theorem TS / TS_K; CLS-cone and CLS-red (off the HW route; parallel source, row 9p).

### 4.3 Proposition RLF-step v3: (I_k^E)″ on Λ_k + §4.2 ⇒ (I_{k+1}^E)″ on Λ_{k+1}, and (RLF-3′) over k. Status: **ARGUED**
"ARGUED stands, with the list replaced by Part 3's" (REVIEW_RLARGE_V2 §2.2). Steps 1-3, 5 as v2; steps 4, 6 replaced [v3-R1].
1. *Exact.* Stage k: insert the level-(k+1) indicators into J_k (RS ordering, bookkeeping only, §2.1); (H-Mayer^J)_k [row 6];
   CL^J (a)-(b) (PROVEN-HERE, HIST §4).
2. *Frozen R-step, σ-restricted.* R1^J (i) / R1_Λ on the σ-good part [row 14], cutoff n_c = n_♯; no pointwise Taylor extraction.
3. *Sea average and re-extraction at V = 1.* (W1-ret′^J)_k (a)-(b) [rows 5, 5a, 5b, 15]: c̄_0^{sea}, δβ_k, returned remainders
   (incl. 𝓗^{cb}) as admissible two-field polymers. Each returned cluster's in-step price is (RLF-2)/(SDP)^A [row 10b].
4. *Unreturned configurations [v3-R1].* **Not priced in the stage-k integrand.** They are the components 𝒰_{k+1} of the
   history; their weight is collected forward, for all levels at once, by Lemma CH under μ_{R(𝔥)} (§3.2-§3.3): the window
   lower bound (CLS-min) [row 9], the mismatch moment (M-i) ⇐ (LI^F) [row 10a], the capped fine moment (M-f^A) ⇐ (SF-cap)^A +
   (SDP)^A [rows 10b, 10c].
5. *Small-field step.* (SF^J)_k [row 3] integrates U_k on Λ_k against the (I_k^E)″ density [row 4] with the shifted coupling
   (u_k → u_k - δβ_k, plus the β = 0 polymer, HIST (c4)); outputs (I_{k+1}^E)″, the flow step, and — new under v3 — the
   per-level outputs (SF-cap)^A and (SDP)^A at level k + 1. (SG^fl)_{k+1} is an output only for consumers of branch (ii).
6. *New level-(k+1) large fields [v3-R1].* v2's "Before U_k is integrated (RS ordering), each bad level-(k+1) cube is priced by
   §3" is **withdrawn** (it "cannot be a fixed-V integrand bound", REVIEW_RLARGE_V2 W6). A new bad cube is either returned
   (step 3) or joins 𝒰_{k+1} (step 4).
7. *Nesting and assembly.* Lemma H-nest (PROVEN); assembly over k: (H-w′) [row 10] + Theorem HIST-sum with HS′ (§5) gives
   (RLF-3′) relative to Z(∅); (NA-∅) [row 10d] gives (RLF-4).
**Three non-circularity checks (REVIEW_RLARGE_V2 §2.2 item 4; "the integrator must add").**
- **(a) (SDP)^A at level k is built from the stage-(k-1) representation.** Node A must not consume (H-w′) or HIST-sum at levels
  ≥ k. The laws ℛ_𝔥^↑ carry the history indicators of coarser levels, so their U_{≤k} marginal is tilted by the future
  probability; "That tilt is (LI)'s content, and it must enter (SDP)^A only through (LI^F) [inference]". HW's own hypotheses
  consume neither (H-w) nor HIST-sum (HW-F4, HW §6). **Status: a requirement on (SDP)^A's proof; not checked** [row 18].
- **(b) FI-1's g_{k+1}-dependence:** §4.4.
- **(c) S4-5:** "Until node A chooses one, steps 3 and 5 cannot both use their stated complex domains" [row 16; U2].
Constants (C_ℓ, B_0, E_0, a, n_♯) are the same at every level; the flow constants β_-, R are fixed first (FLOW Lemma F-ind).

### 4.4 Non-circularity with FLOW (FI-1), including the g_{k+1}-dependence [v2-F; v3-δ]
- **Requirement (FLOW [RFL-fix FI-1], binding; paraphrased).** Lemma F-ind's induction over k is non-circular only if (SF-g)_k
  and (RLF-δ)_k at level k use the flow on [0, k] only, along the chain's own sequence.
- **What the sources give.** (F-3) (FLOW l.67-68): if g_0, …, g_{n-1} ∈ (0, γ], the bracket β_-(n - j)log L - R ≤ u_j - u_n ≤
  β_+(n - j)log L + R holds for all j ≤ n. At n = k + 1 this needs g_0, …, g_k ≤ γ only, i.e. data on [0, k]; F-mono (⋆)
  1/g_{k+1}² ≤ 1/g_k² + R is its j = k case. But F-flow at n = k + 1 consumes (RLF-δ)_j for j ≤ k (u_{k+1} contains δβ_k).
- **The dependence (REVIEW_RLARGE_V2 §2.2 item 4(b)).** "FI-1 (§4.4) says the stage-k constants depend on g_k and g_{k±1}. By
  F-mono, the g_{k+1}-dependence (HIST H1-H4) uses (F_R) at (k, k + 1), i.e. a datum one level beyond [0, k], and g_{k+1} is
  itself an output of stage k (through δβ_k). The fixed point is consistent only if the kernel coupling sequence is fixed first
  (A5's fixed-point reading, l.89), or if CL^J's Setting is stated with an a-priori bracket for g_{k+1} [inference; not checked
  against F-ind's proof]."
- **Reading adopted in v3 (integration choice, both options kept; for the lead, U4).** In W the kernel couplings u_i are
  parameters (§0; HW §0: k^{(i)}_c carries κu_i); g_{k+1} in CL^J (c)-(d) is the coupling of the next kernel K_{k+1}. So:
  - **Option A (primary in v3): fix the kernel sequence first.** Stage k's constants are functions of the parameters (g_k,
    g_{k+1}) of W and are bounded using only the a-priori bracket 1/g_{k+1}² ≤ 1/g_k² + R and g_{k+1}² ≤ 1/(2R) as a hypothesis
    on the kernel sequence over [0, k + 1]; "the chain's own sequence" (effective = kernel couplings) is the separate
    fixed-point statement A5. Then (RLF-δ)_k uses data on [0, k] plus that bracket, and F-flow at n = k + 1 must REPRODUCE the
    bracket (it does, by (F-3), if the effective and kernel sequences agree on [0, k + 1]: this agreement is A5).
  - **Option B: state CL^J's Setting with the a-priori bracket** "g_{k+1}^{-2} ≤ g_k^{-2} + R, g_k, g_{k+1} ≤ min{1, √κ}/√2"
    (FLOW's requested restatement, row 4a) and check, in F-ind's induction order (β_-, R first; then C_ρ; then γ), that the
    bracket at (k, k + 1) is an output of the step at k rather than an input. Not checked by any source.
  Neither option is a theorem here. **The requirement is met by the structure of steps 1-6 only modulo row 2b**; v2's "met by the
  structure of steps 1-6 as stated" is withdrawn.
- **What does not feed back.** Σ_k|δβ_k|, (P1) = HIST-sum, (P5), (RLF-3′)'s total are used only in the assembly and in (RLF-4),
  never in FLOW. n_♯ ≥ n_H depends on a, B_0 and β_- (fixed first by F-ind, β_- := β_0′/2). Under v3, a = min{θa_bad, a_A}
  and B_0 = c_LI + c_f + 164ε_♯ are level-uniform constants of HW's hypotheses (§3.3); REL-seq's order of constants is "a, C_ℓ,
  c … → B_0 → n_H → n_♯ ≥ n_H → g_0(n_♯)" (HW §13.2), non-circular.

---

## 5. History sum

### 5.1 Definitions (HIST §7.1; CONFIRMED by REVIEW_HIST_S1; unchanged) and the exact representation (HW §2)
Projection π, collar N_ρ, one-step shadow Σ(A) := N_1(π(A)); history 𝔥 = (𝒰_0, …, 𝒰_{K-1}); Ω^c_k(𝔥) := ∪_{j≤k}sh_k(𝒰_j),
Λ_k(𝔥) its complement; admissibility (A1) every component of 𝒰_k has > n_♯ cubes, (A2) 𝒰_k ∩ Σ(Ω^c_{k-1}) = ∅; Lemma H-nest
(PROVEN). **[v3-V1]** Lemma HR (Z(𝔥) := ∫W·1_𝔥, Σ_𝔥Z(𝔥) = Z_K) and Lemma RX (relaxed event R(𝔥), Z(𝔥) = Z(R(𝔥))μ_{R(𝔥)}(𝔥),
Z(∅) ≤ Z(R(𝔥))) (HW §2; PROVEN-HERE, elementary, uncounted). Returned configurations are not part of the history.

### 5.2 Theorem HIST-sum with Lemma HS′ (HIST §7.4; HW §3.2): CONDITIONAL ⇐ (H-w′) + lower half of the flow
HIST-sum (CONFIRMED conditional, REVIEW_HIST_S1) holds verbatim with (H-w)'s factor exp(B_0Σ_k|Ω^c_k|) replaced by the larger
per-component shadow sum exp(B_0Σ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|) (Lemma HS′, PROVEN-HERE, one line, uncounted). With c_B :=
38416B_0/log L, **n_H := ⌊(4 + c_B)/(aβ_-)⌋**, n_♯ ≥ n_H and 6400C_ℓe^{aR}e^{38417B_0}e^{-a/g_K²} ≤ ½: Σ_{𝔥≠∅}Z(𝔥) ≤
Z(∅)(exp(C_H|T|e^{-(n_♯+1)a/g_K²}) - 1), C_H := 2·6400^{n_♯}(C_ℓe^{aR}e^{38417B_0})^{n_♯+1}/(1 - L^{-γ_H}), uniformly in K
(reference (ref-a), HW Theorem HW). **[v3-3′] a is HW's a = min{θa_bad, a_A}, not v2's a_♯.** Lemma REL-seq additionally needs
ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c} ≤ min{½, 1/164} (HW §13.2; the e^{38416c} is an over-estimate,
REVIEW_HW_S2 recommended note). "The logarithmic flow is load-bearing" (β_- = 0 diverges for every n; HIST §7.4).

### 5.3 (P1)-(P5) over K levels (HIST §7.5; v2 §5.3, updated)
- **(P1)** = HIST-sum with HS′ (CONDITIONAL), now relative to Z(∅).
- **(P2)** arithmetic PROVEN given the per-stage bounds; exponent a_ret (K12); prefactor with β_+; sign of §0.
- **(P3)** arithmetic PROVEN: 𝒱^LF_K field- and history-independent. HW Remark GAS: the returned gas in Z(∅) must be
  extracted (𝒱^{LF} in (NA-∅)), not bookkept.
- **(P4)** ARGUED (HIST RH1-fix H-2), re-based on (I_k^E)(b)'s per-cube E_0. Not consumed by the HW route ((ref-a) needs no
  representation-side B_0 items; HW §13.3: "No per-history B_0 item is left: HIST §7.4's (a)-(d) are artifacts of the
  R-operation representation and do not occur in ∫W·1_𝔥").
- **(P5)** arithmetic PROVEN (v1 §8.4) with a in place of a_♯: composition with Theorem CE at level K needs
  g_K² < a/(8(3κ_0 + 3)) and C_ℓe^{-a/(4g_K²)} ≤ c(κ_0) [v3: exponent relabelled; the arithmetic is v1's]; applying CE needs
  (SF-last).

### 5.4 n_H, W, wrap levels and coupling ceilings, recomputed [v3-T; Required fix 3; all [hand] unless quoted]
| source | ε_1 used | exponent | n (threshold) | wrap levels ≈ log_L W | status |
|---|---|---|---|---|---|
| HW §13.2 (w2 C1) | recorded constants of h4 (ε_1 = O(1) era) | a ≈ 10⁻¹⁷ | n_H ≈ 9.45·10²¹ | ≈ 46 (REVIEW_RLARGE_V2 2.2 item 3) | illustrative; not admissible under (TH-ch″) |
| REVIEW_SF_S5 l.343 (via REVIEW_RLARGE_V2 A7) | — | — | — | ≈ 60 | quoted |
| SF §22.7 / REVIEW_SF_S7 TB-1 | 1.27·10⁻³⁹ / 8.95·10⁻⁴⁰ | v1's a″ < ε_1²/(4N) | RLARGE n_* = 5.9·10⁷⁹ / 1.19·10⁸⁰ | ≈ 42 | v1's n_* formula, not n_H |
| **v3 [hand]** | **≲ 6.7·10⁻⁴⁰** (rerun class, TB-1) | a_bad = c_prε_1² ≈ 2.5·10⁻⁸⁵ ((REG-min) route, ε_1 < t_pr); **a = θa_bad ≲ 1.0·10⁻⁸⁶** (θ < 1/24) | **n_H ≥ 4/(aβ_-) ≳ 2·10⁸⁷** (β_- = β_0′/2 ≈ 0.186 at N = 2; c_B ≥ 0 and a_A < θa_bad only increase it) | W ≳ 4·10⁸⁷ ⇒ **≈ 184 wrap levels** (L = 3) | integrator arithmetic, unreviewed |
- **Reading.** Every row is K-independent and g-independent, so legitimate for a proof; but the (SF-last)/torus clause is a
  many-level item (A7: "not O(1)"), and its scale depends on which exponent is in force (K16).
- **Coupling ceilings from this file [hand].** HIST-sum's, REL-seq's and (RLF-δ)'s smallness conditions all have the form
  e^{-a/g²} ≪ (polynomial and C_ℓ factors)^{-1}, with log C_ℓ ≈ (3n_int/2)·log(1/(1 - λ_*)) ≤ 324·log(4/3) ≈ 93 at λ_* ≤ ¼, so
  g_K² ≲ a/10² ≈ 10⁻⁸⁸ on the (REG-min) route at the current ε_1 ceiling. This is far above the binding DX′ ceiling
  g_0² ≲ 2.5·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 C-1), so RLF's own ceilings do not bind at the current constants. REVIEW_RLARGE_V2 §2.3
  quotes g² ≲ 10⁻⁹⁵ for the (AE)-route a_coh; the (AE)-route a_bad at ε_1 ≲ 6.7·10⁻⁴⁰ is ≈ ε_1²/(2NC_cone) ≈ 10⁻⁹⁴ [hand].

---

## 6. What is proven outright, and what is conditional [v3-S A10]

**PROVEN-HERE, reviewed (no hypothesis beyond stated parameter ranges):**
- v1 (Appendix A): Lemma GT-lat′ (CONFIRMED); Proposition CL (CONFIRMED-WITH-FIX); Lemma RS (CONFIRMED); Theorem R1 with Lemma
  7.2-0 + Theorem TS (CONFIRMED-WITH-FIX, accepted by REVIEW_S20); Lemma LF-n arithmetic.
- HIST: Lemma PM (with KQ), Lemma RS-lin, Proposition CL^J, Theorem R1^J (with GT-lat″, Lemma 7.2-0^J, Corollary R1_Λ), Lemma
  H-geo (with H-nest); Lemma HF, Lemma E-loc; **Theorem MSG (CONFIRMED-WITH-FIX), MSG-loc′; Lemmas TERM-an, NORM-an (C_N
  existence-only), POL, EXT, (R♯_∞) (CONFIRMED; (R♯_∞) "not the one NA-IFT needs")** (REVIEW_HIST_S3/S4). Whole-file tally
  "11 PROVEN-HERE / 5 CONDITIONAL / 8 ARGUED / 4 OPEN + 1 HYPOTHESIS" (REVIEW_HIST_S4).
- PLD: Proposition SHADOW, Lemmas W1R-sym + W1R-tay; Lemma HS-net + Proposition PLD-SG; Proposition PLD-desc + Proposition INH.
- EXISTENCE: Lemma KN, Corollary KN-step.
- **HW (6 counted; REVIEW_HW_S2 "Counted: 6 in total"):** [HW-4] Lemma KS + KS-chain (SU(2), unconditional); TE (i), (iii) and
  W-bad's level-0 case (unconditional parts of [HW-1]). Uncounted, PROVEN-HERE elementary: Lemmas HR, RX, PF, HS′, HW-split, DJ,
  EQ, HÖ, LI-a, DECL, CAP, CAP-dec, K3-a, K3-b, Remark GAS, Observation SAT, Lemmas LOOP-div, LOOP-const (arithmetic about bounds).
- **FLOW:** Lemma U-loc′ CONFIRMED (counted); Lemma F-mono PROVEN (arithmetic, not counted separately); the REVIEW_FLOW_S9-
  confirmed items (S-2pt, S-tel, S-fix); session-10 items (FINE-IR, IR-id, UIR-S, V-bord, V-Jac, V-tel, §79 (a)) PROVEN-HERE
  as claimed, **unreviewed**.
- **SQ:** Lemmas TOP (not counted), REFL, SHIFT; Theorem REG-lin (given LES-sup); Theorem REG-lin-src (CONFIRMED-WITH-FIX).
- **SF:** among 58 + 1 PROVEN-HERE (REVIEW_SF_S7), the ones this file uses: Lemma DX-rel (PROVEN inequality), Propositions CI-0
  (computer-assisted), CI-bg, Corollary CI-BR1 (the constants behind (TH-ch″)).
- **BFT:** BFT-3 and BFT-4 at k = 1 PROVEN (lane B; PROOF l.6696-6697).
- Branch (i) of v2 = moment (M-i): **plain chain PROVEN (SU(2), KS-chain); in-history ⇐ (LI)/(LI^F)**.

**CONDITIONAL (implication proven, hypotheses named):**
- HW: [HW-1] Lemma TE (ii) + W-bad ⇐ (CLS-min); [HW-2] Lemma CH + Theorem HW ⇐ (F_R), (CLS-min), (M-i)_{24θ}, (M-f)_{96θ},
  (REL), θ < 1/96; [HW-5] H4-red ⇐ (LI); [HW-6] REL-seq ⇐ (PRICE^ℛ) on ℛ_𝔥^↑; [HW-7] H4-red′ + Theorem HW^cap ⇐ (LI^F),
  (M-f^cap), (CLS-min) (CAP-1); Proposition FV ⇐ (CLS-min) (uncounted); W-cb ⇐ (CLS-min) + (TC) (uncounted).
  Net: (H-w′) ⇐ (F_R) + (CLS-min) + (LI^F) + (M-f^A)_θ (§3.3).
- Theorem HIST-sum (with HS′) ⇐ (H-w′) + lower half of the flow; Lemma RS-joint ⇐ (PLD-q)_k (plain measure; off the HW route);
  Theorem CLS-red ⇐ (AE); Corollary CLS-cone ⇐ (AE) (scope fix S3-5); **Theorem AE-red: (AE) ⇐ (MS-Sob)**; **Corollary DESC-ε
  (and PRICE-iii): (CLS-min) ⇐ (REG-min)**; Proposition W1R ⇐ (SC)_k + (SF-irr)_{k+1}; FLOW F-flow, F-tune ⇐ (UNIV-1L), (SF-g),
  (RLF-δ) (+ (SF-cont), (SF-∞)); Lemma V-2pt (a)-(c) ⇐ (L-loc2); SF (CH-c) ⇐ DX-rel + (DX-loc) + E10 + CH-3 scope; PLD-desc ⇐
  (SG^fl)_k (good V only; not on the HW route).

**ARGUED:** Theorem A5 (S4-1, S4-2); (a4); (H-Mayer^J); (P4); RLF-step v3 (§4.3); (D1-c) and H-2; the Laplace link; (RLF-5)
width for one activity (O(g/√κ)); H-4; (L-loc2); SQ §11.6 (NA-0)-(NA-5); (MS-Sob) ⇐ MSG-loc-dev + MS-HLS + (SQ-dev).

**OPEN / HYPOTHESIS:** the §4.2 list.

**Theorem RLF (§1.2): OPEN**, reduced to the §4.2 list (by induction on k with (I_0^E), steps 1-7, (H-w′) + HIST-sum + REL-seq,
(NA-∅), (P2)-(P5), (SF-last) + Theorem CE at level K). L5 stays IMPORTED-NOT-YET-REVERIFIED in PROOF (CMP 122 not read); RLF
is the re-derivation target that would replace it.

---

## 7. Critical-path DAG (open items → UV stability for the soft RG) [v3-D; REVIEW_RLARGE_V2 Part 3, updated]

Target: **L6-soft** (UV stability), exp(-E_-|T|) ≤ Z_K/Z_K^{ref} ≤ exp(E_+|T|) uniformly in K. ✓ = proven (reviewed); (C) =
conditional implication proven. Tags as §4.2.

```
L6-soft (UV stability)  ⇐ (RLF-1) + (RLF-3') + (RLF-4) + node-A bulk bound + assembly C [other, P: CMP 119]
│
├─ (RLF-3') per-history bound, exponent a = min{θa_bad, a_A}, reference Z(∅)  ⇐ HIST-sum + HS' (C) ⇐ (H-w')
│   (H-w') (C: HW^cap [HW-7] + REL-seq [HW-6] on ℛ_𝔥^↑ + H4-red' + CAP-dec)  ⇐
│     ├─ (F_R), g_K² ≤ 1/(2R)                                     → FLOW branch below
│     ├─ (CLS-min)  ⇐ (REG-min) [A/SQ, OPEN, P]  ⇐ (MIN-reg)_cone [A/SQ, OPEN; "close to circular" with (BFT-cone)]
│     │      SQ needs from BFT: θ_w > 1 stated + cone-box uniqueness/ε-regularity clause (item 4)
│     │      parallel: ⇐ (AE) (C, AE-red) ⇐ (MS-Sob) [HIST/SQ, OPEN] ⇐[ARGUED] MSG-loc-dev + MS-HLS + (SQ-dev) [OPEN]
│     ├─ (LI^F) capped future-tilt bound [HW, OPEN, s-P]
│     ├─ (M-f^A)_θ ⇐ (SF-cap)^A [A, OPEN] + (SDP)^A [A, OPEN, P]   (CAP-dec ✓)
│     │      (SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]
│     │                + R1^J gas on the σ-good part: I-σ [R, s], I-σ^J + σ^J_Q statement (K2) [R/HIST, s]
│     │                + non-circularity check (a) [R/A]; never by column induction (LOOP-const)
│     ├─ (KS-N) for SU(N ≥ 3) [HW, HYPOTHESIS, s]
│     ├─ collar-bad family: W-cb with (TC) [HW/R, C uncounted], (M-i) on collar links, (REL) non-bad, E10 [R/A, OPEN]
│     └─ history-independent defect rule (K14) [R]
│
├─ (RLF-4) ⇐ (NA-∅), NA-1 form with 𝒱_K^{LF} [A, OPEN] + (SF-last) incl. ≈ 46-184 wrap levels (K16) [A/R, HYPOTHESIS]
│
├─ (RLF-2) returned contributions / (RLF-0) counterterms (exponent a_ret, K12)
│     ├─ (W1-ret'^J)_k (a)-(b) ⇐ (SC)_k [A/PLD] + (SF-irr)_{k+1} [A, the A4 wall] + I-tay^J [R/HIST]
│     ├─ (H-Mayer^J)_k [HIST, ARGUED, s]
│     └─ RLF-step v3 assembly [R, ARGUED]: FI-1 g_{k+1} bracket (option A/B) [R]
│
├─ (I_k^E)'' [A/HIST, HYPOTHESIS, P]
│     ├─ Theorem A5 [ARGUED] ⇐ (a5-G♯) + (R♯) [A/PROOF-N2, OPEN] + (a5-U) [HIST, OPEN] + (a3-q) [HIST, OPEN] + (MS-Sob)
│     ├─ (a4) [HIST, ARGUED]; statement fixes S4-1, S4-2 [HIST, s]; CL^J Setting restatement (H1-H5) [HIST, s]
│     └─ S4-5: (RLF-5) width vs (b'') — node-A norm decision [A / lead, binding]
│
├─ (SF^J)_k = node A1-A4 [A, P×3-4]
│     ├─ A1.k, A1.loc; A3 composition at k ≥ 1; (GF-dec)_k; (GF-B^𝔥) (τ^♯; ε_1 lever); (DX-loc-3), (DX-loc-4) [SF, OPEN]
│     ├─ stage 0: (CH-c) (C) ⇐ DX-rel ✓ + (DX-loc) + E10 [R/SF, OPEN] + CH-3 scope;  (SG^fl)_0 (C) on the O-chain
│     ├─ (SG^fl)_k, k ≥ 1 [A/PLD, HYPOTHESIS; off the HW route]
│     ├─ (C_♭-eval), C_Δ evaluation (binding iff C_Δ ≳ 1.2·10²¹) [A/PROOF, OPEN, s]
│     └─ N5 level-uniformity ⇐ BFT-0, BFT-1 (θ_w = 0), BFT-2, BFT-4; (MIN_1); small tori; FP_U background dependence; (CL-4) [A/PROOF]
│
├─ BFT [BFT, OPEN, P]
│     ├─ BFT-0/1/2 ⇐ (H-lin^∇) [⇐ (H-inv+): (CO-0) = (G♯_0-lev0), (CO-up), (G♯-rough) curvature half, (SB)] + (Res-Hölder)
│     │            + LRL (b) + (H-rem^∇) third order [ARGUED] + (FP♯') + background slice (N1); PROOF's (CL-4)
│     │            (REVIEW_BFT_A_S5: gauge-invariant half complete only for the soft-RG source class, m = 0, trivial
│     │             background; level-0 Wilson rows (G♯_0-lev0) = (LED-src) + G♯_0-plain OPEN)
│     ├─ BFT-3 (= v2 (BG)_k, R_bg; = FLOW (SF-bg) at trivial field): k = 1 ✓; k ≥ 2 ⇐ weighted (H-inv+)_m
│     ├─ BFT-4: k = 1 ✓; k ≥ 2 ⇐ (W-comm) [GAP 1] + (CovLift) + (Mult-Y) + (Pair-loc), (I-id)_Z, (E3^∇) [ARGUED]
│     └─ BFT-5 [no status anywhere; unowned] ⇐ (G♯_0-field) + (R♯_ω) + (G♯-patch)
│
└─ (F_R) along the chain's own sequence [FLOW, node A5, P]  ⇐ F-flow (C) ⇐ (UNIV-1L) ⇐ Theorem UNIV ⇐
      (L-loc2) [ARGUED] + (VFINE) [s] + (VC-V) [s] + (DEF) [s-P, the crux]  (FLOW §80, session 10, unreviewed);
      reviewed list (REVIEW_FLOW_S9): (V-IR) form (Q1)(d), (UIR), vector off-shell defect, (L-loc2);
      scalar-proxy (UIR) PROVEN (session 10, unreviewed); k-uniform vector step gap [s];
      + (SF-g), (SF-cont), (SF-∞) [layer 1, ⊂ node A]; (SF-bg) = BFT-2, 3 at trivial field;
      + (RLF-δ)_k per level, FI-1 + g_{k+1} bracket [R]
```

**Open items on the critical path, grouped by owner file.**
- **RLARGE.md [R]:** I-σ; I-σ^J with σ^J_Q (K2); I-tay^J (shared with HIST/PLD); E10 (shared with SF); FI-1 with the g_{k+1}
  bracket (U4); (RLF-δ)_k; a_ret (U1); the (SF-last) wrap-level clause (K16); (TC) vs ε_loc (U3); the history-independent rule
  (K14); the (SDP)^A non-circularity check (a). Done in v3: V-1, R-1, (RLF-3′), a_bad recorded as binding, g² ≪ ε_1²·10⁻¹³
  recorded, τ_c/(TH-ch″) in [v2-C], the c32/c33 reading note.
- **HW.md [HW]:** (LI^F) (capped weights); (KS-N); W-cb's collar extension ((TC), (M-i) on collar links, (REL) for non-bad
  defect notions).
- **Node A [A].** SF.md: A1.k/A1.loc, the A3 composition, (GF-dec)_k, (GF-B^𝔥), (DX-loc-3/4), (CH-c)'s inputs, (C_♭-eval), C_Δ.
  PLD.md: (SC)_k, (SF-irr)_{k+1}, (SG^fl)_k (off the HW route). HIST.md: (I_k^E)″ with (a5-U), (a3-q), (a4), S4-1/S4-2, the CL^J
  restatement (H1-H5), (H-Mayer^J), the stale A5 status at HIST l.1683. SQ.md: (REG-min) ⇐ (MIN-reg)_cone (parallel: (MS-Sob)/
  (SQ-dev) with HIST). PROOF.md: (R♯), (a5-G♯), (CL-4), (MIN_1), small tori, FP_U's background dependence. Node-A interface
  items (owner file within node A not fixed by any source, U10): **(SDP)^A, (SF-cap)^A, (NA-∅)**, the **S4-5** decision.
- **BFT_A.md / BFT_B.md [BFT]:** BFT-0/1/2 ((H-inv+) [(CO-0), (CO-up), (SB)], (Res-Hölder), LRL (b), (FP♯′), (N1)); BFT-3 at k ≥ 2;
  BFT-4 at k ≥ 2 ((W-comm) GAP 1, (CovLift), (Mult-Y), (Pair-loc)); SQ's θ_w > 1 + cone-box clause; BFT-5 (unowned).
- **FLOW.md [FLOW]:** (L-loc2), (VFINE), (VC-V), (DEF) (crux); the k-uniform vector step gap; review of session 10.
- **Other:** the assembly C [P].

**Shared objects (one proof, several consumers).** (H-inv+) feeds BFT-0/1/2, BFT-3 and BFT-4. (CLS-min) feeds W-bad, W-cb, FV,
SAT and (SDP)^A. BFT-3 serves as v2's R_bg and FLOW's (SF-bg). I-tay^J feeds (W1-ret′^J) and (SDP)^A. E10 feeds this file's
collar-bad family and SF's (CH-c). (SC), (W1-ret′^J), R1^J feed both (RLF-2) and (SDP)^A (the same in-step price, two readings).

---

## 8. Integration conflicts and unresolved items (for the lead) [v3-K]

**K1-K10 (v2 labels kept).**
- **K1 (sign of δβ): RESOLVED.** FLOW agrees (u → u − δβ); "K1 is right" (REVIEW_FLOW_S3 l.34 via REVIEW_RLARGE_V2 F4).
- **K2 (joint collar clause): OPEN.** No σ^J_Q anywhere (REVIEW_RLARGE_V2 H10). Also the territory of W-cb's unreduced (M-i)
  on collar links (HW §5.1).
- **K3 (extraction after averaging vs R1_Λ):** moot for HW's (ref-a) route (∫W·1_𝔥 contains no extraction; HW RHW1-fix
  H-10); open for the R-operation: K3-a settled (≤ 1 in B_0), K3-b supports E3, residual I-tay^J (HW §7).
- **K4 (one-step monotonicity in HIST): RESOLVED modulo HIST's restatement** (Lemma F-mono; H3 added; row 4a).
- **K5 (RS-joint vs three-way price): RESOLVED for bad cubes** (HW §5.3: one law, Lemma CH). For collar-bad cubes only via W-cb
  with (M-i) unreduced (K15).
- **K6 (thresholds): extended.** η_1, η_q as v2, plus τ_c, (TH-ch′)/(TH-ch″) (SF), (TC) (HW W-cb). ε_1 ≲ 6.7·10⁻⁴⁰ (§0).
- **K7 (complex domain): now S4-5 (binding).** Options (1) re-centring at the holomorphic critical branch (primary per
  REVIEW_HIST_S4) / (2) two polymer classes (fallback, node-A norm decision). **Not chosen in v3** (U2).
- **K8 (existence lane's (RLF-3^dis)): answered for v3 [inference].** EXISTENCE §17.8 requested: "state whether Z(𝔥)
  decomposes Z_K or Z_K^{ren}". Under v3, Z(𝔥) := ∫W·1_𝔥 decomposes **Z_K** (Lemma HR), and (RLF-3′)'s reference is Z(∅) ≤ Z_K,
  which carries the vacuum through (NA-∅). Ratios Z(𝔥)/Z_K are then bounded by Z(𝔥)/Z(∅) without EXISTENCE's normalisation
  fact Z(∅) ≥ e^{-E_∅|T|}Z_K^{sf}. The exponent EXISTENCE should read is a (not a_♯), and its restricted-sum factorisation is
  still ARGUED there. For the existence lane to confirm (U11).
- **K9 (tori): OPEN.** EXISTENCE §17.8 (K9-req): either two per-level shifts δβ^{el}, δβ^{mag} on anisotropic tori, or, "if v2's
  counterterms are infinite-volume numbers … with the torus entering only at the wrap levels T_{k+1} < W, a single shift
  suffices and only the wrap-level term is anisotropic; v2 should say which of the two holds". v3 keeps (RLF-0)'s
  "infinite-volume numbers" but no source proves that the sea average is torus-independent above the wrap levels (U5).
- **K10 (weights/tallies): superseded.** v2's row weights for (H-w), (BG)_k, (MSG) are stale; v3 quotes owners' weights; no tally
  claim.

**New conflicts.**
- **K11 (FI-1, g_{k+1}).** Stage-k constants use the next kernel coupling; options A (fix the kernel sequence first; A5 separate)
  and B (a-priori bracket in CL^J's Setting) in §4.4; **v3 chooses A as primary, keeps B**; neither checked against F-ind's
  proof (U4).
- **K12 (the returned-cluster exponent).** (RLF-0)/(RLF-2)/(RLF-δ) need node A's exponent a_ret; (SDP)^A needs a_A ≥ θa_bad or θ
  is lowered. No source states either value; v2's a_♯ formula is not a returned-cluster statement (U1).
- **K13 ((REG-min) vs (AE) as the (CLS-min) source).** HW and SQ take (REG-min) as primary; REVIEW_SQ_S2: the merger's effect
  on the wall count is "UNDECIDED"; SQ's "NET LOSS of 6-9 orders" for the sup route was computed at ε_1 = 0.5 where the τ_♭
  cap binds. [hand] At ε_1 ≲ 6.7·10⁻⁴⁰ (< t_pr on both routes) the coefficients are c_pr = c_♭/C′² ≈ 5.6·10⁻⁷ (REG-min) against
  1/(2NC_cone) ≈ 2.2·10⁻¹⁶ (AE), i.e. the comparison reverses; an observation from quoted constants, unreviewed (U7).
- **K14 (history-independent defect rule).** HW's Lemma RX (ii)-(iii) and REL-seq need it; HW reads RLARGE's collar rule as
  possibly history-dependent near Σ(Ω^c_{j-1}). v3 adopts the history-independent convention for the HW route (U6).
- **K15 (collar-bad coverage).** HW^cap, H4-red′, DECL and REL-seq are bad-only. The collar family (D-b)/(D-c) is covered only by
  Theorem HW's W-cb extension (uncapped, θ < 1/(96·82), (M-i) unreduced, (REL) undischarged), plus E10 at ∂Λ(𝔥). This is the
  largest remaining gap between (RLF-3′) and the full defect notion of §2.
- **K16 (wrap-level count).** ≈ 42 (SF §22.7, v1 n_* formula), ≈ 46 (REVIEW_RLARGE_V2, n_H ≈ 10²²), ≈ 60 (REVIEW_SF_S5), ≈ 184
  (v3 [hand], n_H at the current ε_1 ceiling). Chosen: "many-level, K-independent"; (SF-last) must be stated for that number
  (§5.4).
- **K17 (naming).** HW §18.1/§19 cite (I_{k-1}^E)′ (d); current HIST is (I^E)″ (d″). Read ″ (cosmetic).
- **K18 ((REG-min) and (BG)_k).** HW §11/§19 and SQ l.249's heading call (REG-min) "the cone-local sup form of (BG)_k/(SF-bg)";
  SQ RSQ1-fix S1-3 (CONFIRMED by REVIEW_SQ_S2) withdraws that: (REG-min) is "B-NA-class (multi-scale Schauder, cone-local, free
  boundary)", and REVIEW_S22 Part 5 calls it "a sibling, not a corollary" of BFT. **Chosen: the reviewed reading** (row 9; (BG)_k
  = BFT-3 is a separate row 8).
- **K19 (BFT status freshness).** PROOF's session-23 map quotes REVIEW_BFT_A_S4; REVIEW_BFT_A_S5 (later) narrows lane A's
  gauge-invariant (H-lin^∇) claim to the soft-RG source class at m = 0 and trivial background, with the level-0 Wilson rows OPEN
  (fix U7). v3's DAG carries both; BFT_A.md/BFT_B.md were being edited at read time.
- **K20 (stale pointer in HW).** HW §19 A5 says (CLS-min) ⇐ (REG-min) is "implication PROVEN in SQ, unreviewed"; REVIEW_SQ_S1/S2
  have since confirmed DESC-ε/PRICE-iii as CONDITIONAL ⇐ (REG-min). v3 uses the reviewed status.
- **K21 (items for other owners, recorded only).** PROOF: KW-1 windows "< 2.585·10⁻²" (old class) and "< 1.939·10⁻²" (session-23
  class), and fix N-1 (the coth⁸ term ≥ 7.8·10⁵⁶C_Δ) (REVIEW_RLARGE_V2 Part 4). HIST: the CL^J restatement and l.1683's stale A5
  status. No other file is edited by this integration.

**Unresolved items for the lead (decisions, not proofs).**
- **U1** a_ret and a_A: which node-A statement fixes the returned-cluster exponent, and whether a_A ≥ θa_bad (else θ is lowered).
- **U2** S4-5: re-centring (primary per REVIEW_HIST_S4) or two polymer classes (a node-A norm decision).
- **U3** (TC) vs ε_loc: adopt ε_loc ≥ (16N + 3)ε_1/(128N) [hand sufficient condition] if compatible with CL (c) and (TH-ch″).
- **U4** FI-1: option A (kernel sequence fixed first; A5 separate) or option B (a-priori bracket in CL^J's Setting).
- **U5** K9: torus-independent infinite-volume counterterms above the wrap levels, or two shifts on anisotropic tori.
- **U6** K14: confirm the history-independent defect rule (or restate RX for a history-dependent collar rule).
- **U7** K13: which (CLS-min) source is primary given the current ε_1 ceiling.
- **U8** E10: now needed only for collar-bad cubes and stage-0 (CH-c); choose its route ((SG^fl) on every plaquette with a link in
  Λ(𝔥), or a separate price).
- **U9** BFT scope: SQ's θ_w > 1 and cone-box clause as requirements on lane A; an owner for BFT-5.
- **U10** Which node-A file writes (SDP)^A, (SF-cap)^A, (NA-∅) (HW §19 names RLARGE (RLF-2), HIST, PLD, R1^J as sources, not an
  owner).
- **U11** K8: the existence lane to confirm that (RLF-3′) with reference Z(∅) gives (RLF-3^dis) as a literal instance.

---
# Appendix A. Frozen and one-step content of v1 (§3-§9A), verbatim from RLARGE_v1_snapshot.md l.194-580 and l.723-758

**v3 reading notes (the text below is not edited; read it with these notes; they replace v2's notes, v2 l.598-612).**
- **§3 (definition of the R-operation):** run on the σ-restricted gas (§2.4 (α)); the split into c-number + quadratic part +
  remainder is done after the sea average at V = 1 (§2.4 (γ)); cutoff n_♯ ≥ max{n^J_*, n_H} with n_H from v3's a (§5.2).
- **§5 Proposition CL:** unchanged (bare level). CL (c)'s hypothesis ε_♭ ≤ ε_loc is supplied per cluster by σ ≡ 1 (§2.2).
- **§6 Lemma RS:** "1/g_i² ≥ 1/g_{i+1}² under (F)" is not implied by (F_R): factor e^{a_RS R} (§0, F-mono). η_1 is v2/v3's η_1
  (E9). "the large-deviation hypothesis (PLD) of §8" is replaced by §3 of v3 (forward joint moments), not by v2's branches.
- **§7.1:** n_* unchanged; a_♯, c_RS = 5⁴ and n_♯ := ⌊4/(a_♯β_-)⌋ are superseded by §3.5 and §5.2 (a = min{θa_bad, a_A}).
- **§7.2 Theorem R1:** (i) with σ in place of (H-ch) (item I-σ); (ii)-(iii) not applied pointwise in sea samples; (iv) "g_j ≤ g_K
  by (F)" reads g_j² ≤ g_K²/(1 - Rg_K²) (§0). The Reading stands.
- **§7.3 Theorem TS, §7.4:** frozen-background shadow; not used by RLF-step v3.
- **§8 (v1 l.582-721) is NOT reproduced:** superseded by v3 §4-§5 (maps: v1 → v2 in RLARGE_v2_snapshot.md §1.3, v2 → v3 in
  §1.3 here).
- **§9, §9A (checks c32, c33) [v3-T, REVIEW_RLARGE_V2 A5].** Records, unchanged. Their ε_1 = 0.5 is "outside the admissible range"
  (REVIEW_SF_S5 l.359 via REVIEW_RLARGE_V2 A5): under (TH-ch″), ε_1 ≲ 6.7·10⁻⁴⁰ (§0). Their numerics at ε_1 = 0.5 are
  illustrative only; whether any of their conclusions depends on the value of ε_1 is not re-checked in this integration.


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
