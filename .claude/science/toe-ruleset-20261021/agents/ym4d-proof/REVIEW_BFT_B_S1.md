# REVIEW_BFT_B_S1: hostile review of BFT lane B session 1 (BFT_B.md: BFT-3 locality, BFT-4 branch-action class; check bb1)

Reviewer: an independent agent that wrote none of BFT_B.md, BFT_A.md or the ledger. I edited no file except this one. No
commits, PRs or pushes.

Inputs (read 2026-10-28 UTC, after BFT_B.md's last write at 05:10 UTC):
- BFT_B.md l.1-517 in full; BFT_B_LOG.md in full.
- REVIEW_S22.md Part 5 (l.372-437, the BFT statement) and HG-ind / NAH-unif′ (l.249-292).
- BFT_A.md l.1-328 in full. There is no REVIEW_BFT_A_S1.md yet, so lane A's items are read here as unreviewed.
- PROOF.md: [S19] block kernels, Setting N5-bg, N5-cov, AX (l.5246-5305); Theorem N5-sf0 and its evaluation (l.5415-5475);
  [S20] 𝔠_∞, U0, FPq, N5-an♭, BR1, SC1, LOC (l.5596-5740); ENV (l.6164-6171); TOWER-VAR (l.6295-6318); (FP♯') (l.3184-3190).
- LINEAR_PACKAGE.md: Theorems 4.2/4.2′ (l.205-237) and Lemma 6.7 (KF) (l.368-370). SF.md: M_min and μ (l.785-786), (L-loc)_k
  (l.848-851).
- checks/bb1_criteria.md, bb1_decay.py and bb1_diag.py (line by line), bb1A/B/diag outputs, c37_kcurv.py l.130-200 and
  l.395-405, c37D.out, c37_criteria.md D2. I also checked birth and modification times with `stat`.

My rerun (lock-guarded runner and outputs) is in the scratchpad at
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revBB1/`.

---

## Bottom line

- **Theorem BB-3_1 (BFT-3 at k = 1): CONFIRMED-WITH-FIX.** I re-derived steps (1)-(7) against BR1, N5-sf0 (b), N5-an♭,
  U0, ENV and the block-kernel algebra. Every step holds:
  - the Neumann series for 𝔊_ch;
  - the source support;
  - BB-IFT;
  - Cauchy on the half polydisc;
  - the ENV route for E_1^br.

  It needs four small fixes:
  - B1-1: a factor 2 in the quoted value of μ_1.
  - B1-2: the "rate ≥ Lμ_1 − …/d_1" phrasing.
  - B1-3: chart derivatives versus left-trivialised derivatives.
  - B1-4: closedness of the polydisc.

  The theorem is genuinely all-order, and it is correct for every curvature-small real V and its fixed-radius complex
  neighbourhood. One point in its favour: BFT-3 counts the tree as a *minimal spanning tree*, and the star from x_0 is a
  spanning tree, so the max-distance form gives e^{-(μ/n)𝔱} directly. No factor 2 is lost between 𝔱_S and 𝔱.
- **Lemma BB-NL: CONFIRMED as a toy; its title OVERCLAIMS.** It shows that the *analytic* content of BFT-2 does not imply
  BFT-3: holomorphy, polydisc bounds, gauge invariance and extensivity. It does not show "BFT-0/1/2 ⇏ BFT-3". BFT-0/1/2
  concern the critical point of one specific local functional, and if BFT-0/2 are proven by a contraction in a norm with
  exponential weights (BFT's 𝔐 has them), BFT-3 for n ≤ 4 follows by BB-3_k.
- **Proposition BB-3_k: CONFIRMED as an implication, with one domain fix (B3k-1, half radius).** Its hypothesis (H-𝔊_w) is,
  up to restatement, **the same object as lane A's (H-lin^∇) with weight m > 0**. The two lanes therefore share one open
  linear estimate (Part B.4).
- **Failure mode B3-F2 (O(k) marginal level sum for ∂³E_k^br): NOT ESTABLISHED, and its dependency conclusion is wrong.**
  - The power count ignores the structure of the soft cubic vertex. Since φ̂ = ½|ρ|² + O(ρ⁴), the vertex is ⟨r, ρ^{(2)}⟩ with
    r the chain residual. Lane A's CEN2/BA-6 makes it irrelevant.
  - The k-uniform constant of the E-part at n ≤ 4 follows from BFT-1/2 by BB-E1 + Cauchy. It is not "⊂ BFT-4".
- **Construction BB-loc at k = 1: CONFIRMED.** I checked (a)-(d), including the *-connectivity argument. One gap is
  routine (B-loc-1: RW for compressions to non-box index sets).
- **COMP-F2 does affect BB-loc's general-k extension (l.313-314), but not k = 1.** At depth k the composite lift carries
  E_∅ = L^{2k}S_W(V_k). Lift-pinned activities are then O(L^{2k}), not k-uniform. This is BA-2 in energy form.
- **(BB-mix) per-cube smallness: correctly OPEN.**
  - BB-mix ⇒ bound: CONFIRMED (the lattice-animal count is standard).
  - The in-place correction of 05:09 is right, but the pre-stated §1.4 lines l.96-101 still carry the withdrawn claims
    unmarked (fix B-mix-1).
  - The [inference] "K ≈ Ce^{-μM_c}" is overstated by a factor ≈ 2^d in the exponent (B-mix-2).
  - BB-mix-gap (2) is a route failure. It should be labelled ARGUED, not PROVEN-HERE (B-mix-3).
- **BB-env: CONFIRMED.**
- **BB-4-ind: CONFIRMED as algebra; misdescribed and near-vacuous.**
  - It is the per-level architecture that BFT's anti-circularity clause excludes, so "the clause is respected" (l.384) is
    false as written.
  - Its closing condition 4C_QC_W ≤ (1 − λ)² is scale-invariant, so shrinking ε_0 cannot supply it.
  - The Lipschitz strengthening ignores the variation of κ_k.
- **B4-F1: CONFIRMED** as a correctly labelled inference (F² is marginal).
- **Corollary BB-4c: CONFIRMED-WITH-FIX.**
  - (i) and (iv) sum over X where X^+ is needed.
  - (ii)'s "contractible X" does not cover the polymers with holes that (iii)'s far term uses. A fix is given.
- **bb1:**
  - I re-ran A, B and the diagnostic under the lock: byte-identical numbers (Part C).
  - **c37 D2 is float32.** This is verified from the source code, not only from the diagnostic: `kernel(hat, rdt=np.float32)`,
    complex64 hats, and `colsums` reduced in float32. The value **156.6868** is right, and 156.0789 is an accumulation
    artefact.
  - A2's FAIL verdict was correctly kept.
  - A3's rates of 1.7-2.4 are per coarse ℓ^∞ shell. In BFT's ℓ¹ distance they are ≈ 0.5-1.
  - The proven rate is Lμ_1 ≈ 7·10⁻¹¹ per level-1 unit, not 1.4·10⁻¹⁰, which puts it ≈ 10¹⁰ below the measured rate.

---

# PART A: the abstract tools

## Lemma BB-geo (l.122-126): CONFIRMED
- The Euler-tour argument for 𝔱 ≤ 2𝔱_S is standard and correct.
- (c) is PROOF l.5252.
- Add one line: the star from x_0 is itself a **spanning** tree, so 𝔱 ≤ n·max_id(x_0, x_i). The pair version gives
  𝔱(y_1, …, y_n) ≤ (n − 1)max d. Every "e^{-(μ/n)𝔱_S}" in the file can then be read as "e^{-(μ/n)𝔱}", which is the form
  BFT-3 states. Without this line, a reader converting 𝔱_S → 𝔱 by (a) loses a spurious factor 2 in m_0.

## Lemma BB-C (l.128-135): CONFIRMED
- Commuting derivatives and putting the decaying one first is legitimate.
- Cauchy on the polydisc of radius ϱ/2 about a half-polydisc point is legitimate, and the factor α! ≤ (n − 1)! is correct.
- The block factor (N² − 1)^{n/2} is correct.
- The pair version is correct.

## Lemma BB-IFT (l.137-139): CONFIRMED
The source sum uses d(x, x′) ≥ d(x, y) − r_s. Correct.

## Lemma BB-MCT (l.141-154): CONFIRMED (solid norms); B3-F3 CONFIRMED as a statement about solid norms
- The commutator bound |Δ| ≤ Σ_j(e^{mr_j} − 1)|L_j| and the Neumann step are correct.
- The ℓ^∞ lower bound ≳ L^{2(k−1)} is quoted from SF §6.2 and REVIEW_HIST_S4 S4-1 (COMP-F1). I did not re-derive it.
- The ℓ² Rayleigh test field is standard.
- **Reading fix (B-MCT-1).** In lane A's coarse-unit pair, the weight e^{mf} with f = d(·, y) in level-k units has coarse
  Lipschitz constant m and coarse Hölder seminorm O(m) at every scale between one own step and one coarse unit. The
  smoothing of f "at scale L^{-(k−j)}" that l.153-154 asks for is therefore automatic in coarse units. In coarse units
  (H-op) is the m > 0 Combes-Thomas step for lane A's (H-lin^∇), and it is plausibly routine there (Part B.4). Keep it
  OPEN, but describe it as that.

## Lemma BB-NL (l.156-163; pre-statement l.57-59): CONFIRMED as a toy; title and l.504 OVERCLAIM (fix B-NL-1)
- The toy is holomorphic, bounded on uniform polydiscs, gauge invariant and extensive.
- Its pair kernel n_P^{-1}φ″(∂_yS_W)(∂_{y′}S_W) is ≍ n_P^{-1}|∂S_W|². That is non-zero on the polydisc and on curved real
  points, though it vanishes at V = 1.
- Against e^{-m_0d} with d up to the torus diameter ≍ n_P^{1/4}, no n_P-uniform C_0 exists. The argument is correct.
- **But BFT-0/1/2 are statements about the critical point of 𝔉_k, not about arbitrary functions.** The toy is "not a branch
  action" (l.163).
- Moreover BFT's 𝔐 carries exponential weights (REVIEW_S22 l.396). If BFT-0/2 are proven by the contraction in 𝔐 with
  m > 0, uniformly in the weight centre, then the n = 1 response to a localised source decays by IFT. BFT-3 for n ≤ 4
  then follows by BB-3_k.
- **Fix B-NL-1.** Retitle it "the analytic content of BFT-2 does not imply BFT-3". Make the same change at l.57-59, l.162 and
  l.504: "BFT-3 does not follow from BFT-0/1/2" → "BFT-3 does not follow from BFT-0/1/2 proven in unweighted norms (m = 0);
  it follows from them proven with m > 0".

---

# PART B: BFT-3

## B.1 Theorem BB-3_1 (l.165-224): CONFIRMED-WITH-FIX

These are the steps I re-derived.

**(F1) and (F2) (l.168-174).**
- U0 makes the block-interior links of U^(0)(e^zV^r) exactly 1 for complex z too, so h, Π and P_0 (block-interior transports
  M_U) do not depend on V. D_0 depends on V through the crossing links only. This is correct, and agrees with CURV1
  l.6026.
- (U^(0)(V), V) lies in N5-sf0 (a)'s complex neighbourhood: on crossing links z_e = z_c, |z_c| ≤ α_*/8.
- N5-sf0 (b) gives |C_0| ≤ c_Ce^{-m_1d} on 𝔑(α_*), complex points included. Correct.

**Step (2), the inverse.**
- On ker h, ΠO_chΠ = ΠO_0Π(1 + C_0ΠΔΠ) (C_0 maps into ker h and ΠO_0ΠC_0 = Π there).
- The bound is N_{μ_1}(|C_0ΠΔΠ|) ≤ N_{μ_1}(|C_0|)N_{μ_1}(|Π|)²N_{μ_1}(|Δ|), where:
  - N_{μ_1}(|C_0|) ≤ c_CΣe^{-(m_1/2)d} ≤ 4coth⁴(m_1/4)c_C = c_N;
  - N_{μ_1}(|Δ|) ≤ e^{μ_1r_1}C_♭r (range r_1, N5-an♭ Lipschitz in the local AX chart). For the chart variables at complex
    z: |log(g e^{z}V^r)| ≤ 2(r_♭/16 + r_♭/6) < r_♭/2.
- The arithmetic of ε_B gives c_Np_1²e^{μ_1r_1}C_♭·12𝔠_∞ε ≤ ¼.
- Then M_{μ_1}(𝔊_ch) ≤ (4/3)M_{μ_1}(C_0) ≤ (4/3)c_C. Correct.
- (p_1 = N_{μ_1}(|Π|) + 1 is generous; harmless.)

**Step (3), the source.**
- Only f_z (crossing links and φ̂_c) and D_0 depend on z_c. The support is within r_g of c (Setting N5-bg: the variables
  reach blocks at coarse ℓ^∞ distance ≤ 2).
- S_1 is finite by Cauchy on N5-an♭'s polydisc.
- Correct. S_1 is not evaluated, and the file says so.

**Steps (4)-(5).**
- BB-IFT with G_0 = 2c_C, then BB-C on 𝒟 with per-coordinate radius ϱ = ϱ′/(N² − 1)^{1/2}.
- 𝒟 ⊂ {|z_c|_HS ≤ ϱ′} touches the boundary of the open set on which (1) gives holomorphy (fix B1-4).

**Step (6).** This is a routine Lipschitz composition.

**Step (7).**
- ENV needs criticality without fixing; BR1 (ii) gives that for real V.
- For complex V, the identities ∇_UF(U(V), V) = 0 and ENV's formula continue analytically from the totally real set. The
  file's "by continuity" should read "by analytic continuation" (fix B1-3). It is the same fact.
- ∂E/∂z_y equals ∇_yE only up to the local factor dexp_{z_y}^{-T}, which depends on z_y alone. This is harmless, but it
  must be said (fix B1-3).
- The pair version of BB-C then applies.

**Fixes (binding).**
- **B1-1 (l.220, l.326, l.459): μ_1 is off by 2.**
  - PROOF l.5471 evaluates m = 9.66·10⁻¹¹ with N5-w0 and m_1 = m/2. SF l.785 uses μ = m_1 = 4.83·10⁻¹¹.
  - So μ_1 = m_1/2 ≈ **2.4·10⁻¹¹** (level-0 units), and Lμ_1 ≈ **7.2·10⁻¹¹** per level-1 unit, not 4.8·10⁻¹¹ and
    1.4·10⁻¹⁰.
  - "≈ 10¹⁰ below the measured rate" survives: the measured ℓ¹ rate is 0.5-1.
  - The M_c estimate at l.326 doubles.
- **B1-2 (l.194-195).** "Rates ≥ Lμ_1 − (2dLμ_1)/d_1 per level-1 unit" is an odd form of a correct statement. Replace it by:
  "e^{-μ_1𝔱^{(0)}} ≤ e^{2dLμ_1n}e^{-Lμ_1𝔱^{(1)}} (each of the n tree edges loses ≤ 2dL), so the rate is Lμ_1/n in level-1
  units with constant factor e^{2dLμ_1n} ≈ 1". The rate needs no "asymptotically".
- **B1-3 (l.21-25, l.192-193, l.212).** State that ∂/∂z_y is the chart derivative at e^zV^r. The left-trivialised derivative
  at V = e^zV^r differs from it by dexp_{z_y}^{±1} (local, bounded on the domain), which changes C_1 and C_E by a factor
  ≤ (1 + O(ϱ))^n. Also replace "by continuity" (l.193) with "by analytic continuation from real V".
- **B1-4 (l.197, l.208).** 𝒟 must lie in the open domain of (1): take per-coordinate radius ϱ(1 − δ), or note that BR1 (v)'s
  domain is closed (|z_c| ≤ α_*/8) and that ϱ′ ≤ α_*/8 strictly when r_♭/16 < α_*/8.

**Scope (no fix needed).** It holds on tori T ≥ T_0 only. BFT's "every non-wrapping box with the boundary convention of
N5-sf0" clause is not covered. Say so in "What it is not".

## B.2 Proposition BB-E1 (l.228-237): CONFIRMED (algebraic)
- ENV at level k − 1 gives ∇_yE_k^br as a local function of U_{k−1}, and Faà di Bruno follows.
- At general k, ENV needs U_{k−1} critical for F_{k−1} = E_{k−1}^br + soft. In lane A's Balaban convention (BA-9) that
  E_{k−1}^br is E^{cb}. Add "(E^{cb} in Balaban's convention, BA-9)" at l.229.

## B.3 Proposition BB-3_k (l.239-247) and the back-substitution (l.249-264)
- **BB-3_k: CONFIRMED as an implication, with a domain fix.**
  - **B3k-1 (l.241-242).** BB-C gives the bound on the *half* polydisc. BFT-2's polydisc around a real point of curvature
    ≤ ε_0 has radius r_ℂε_0, so BFT-3 is obtained on |z| ≤ r_ℂε_0/2.
  - That is BFT-3 with r_ℂ → r_ℂ/2, or with ε ≤ ε_0/2. State that.
  - Also, "S_1 (BFT-1/2 bound the fields there)" needs the source s_y bounded on the *complex* domain. BFT-2 gives that;
    cite it.
- **The back-substitution identity Ξ_{j←k} = ζ_j⋯ζ_{k−1} and the telescoping (l.251-254): CONFIRMED (algebraic).** Two
  gaps:
  - **B3k-2 (Gronwall step missing).** The telescoping has the *non-trivial* Ξ_{j←i}(V) on the left of each term. "Reduces
    it to (LEG_w) + (LOC-ζ)" needs the iterated expansion Ξ = Σ_{i_1<…<i_p}Ξ^0δ_{i_1}Ξ^0⋯δ_{i_p}Ξ^0. In the weighted
    operator norm this gives ||Ξ(V)|| ≤ C_Lexp(C_LΣ_i||δ_i||) when ||Ξ^0_{a←b}|| ≤ C_L for **every** sub-chain. That is
    the second half of (LEG_w), so it must be required for all sub-chains (a, b), not only for (i, k). Write it.
  - **B3k-3 (gauge compatibility).** (LOC-ζ) uses "a local AX gauge" at each level i. The products need these gauges to be
    compatible across levels (block-constant at level i + 1). Lane A's (UHL) finding applies: the AX gradient loses
    L^{k(1−α)} for Hölder curvature. AX is fine for the sup bound on ζ_i that (LOC-ζ) asks for, but the gauge choice must
    be made once for the chain. Name this, or route through lane A's global gauge on 𝒞_glob.
- **The telescoping route is the per-level route.** It bounds ζ_i through the per-level covariances at level i (LOC-ζ via
  (I_i) ⇐ BFT-4_i). That is legitimate as an implication, but it re-imports the per-level uniformity that BFT was
  introduced to avoid. Mark it as "per-level alternative". The composite route is B.4.

## B.4 Is (H-𝔊_w) the same object as lane A's (H-lin^∇)? **Yes, after two restatements: one shared open linear estimate**

Lane A's (H-lin^∇) is ||𝓛^{-1}||_{𝒴^∇→𝔐^∇} ≤ G and ||𝓛^{-1}N||_{D→𝔐^∇} ≤ G_D at the trivial chain. It is stated with m = 0
("m = 0 suffices", BFT_A l.44), but its norms ||·||_{∞,m} and [·]_{α,m} carry the weight. The matching:

| lane B item | lane A object | note |
|---|---|---|
| (H-𝔊_w)_k: weighted inverse at Z(V_k), residual-type source s_y at level k − 1 near y | (H-lin^∇) **with m > 0**, uniformly in the weight centre, plus (H-rem^∇) with weights (Neumann series from the trivial chain to Z(V), as in Theorem BA's contraction) | s_y = ∂_{V_k(y)} of the top soft gradient is exactly a **residual-type source s_{k−1}**, so the sub-item used is lane A's new **(G♯-res)** (OPEN) |
| (LEG_w): trivial composite tangents Ξ^0_{i←k} = the linear chain-minimiser map B_k ↦ B_i, pointwise e^{-md} and weighted-operator bounded | the **data part** ||𝓛^{-1}N||_{D→𝔐^∇} at m > 0, configuration level | BFT_A §3.11 row "data map … configuration-level (into 𝔐^∇): OPEN", with (G♯_0-field^∇). Lane B's "PROVEN for gauge-invariant outputs" (LINEAR_PACKAGE 4.2′ (ii), 6.7) is the same row's PROVEN half |
| (H-op) (BB-MCT in the non-solid pair) | the m = 0 → m > 0 Combes-Thomas step in (𝔐^∇, 𝒴^∇) | plausibly routine in coarse units (B-MCT-1); not written by either lane |
| (LOC-ζ) | not needed on the composite route: the nonlinear dependence of the inverse on V is (H-rem^∇)'s Lipschitz bound in the weighted norm | the weights commute with finite-range remainders at cost e^{mr} |

Two restatements are required for this to be literally one estimate:
- **B4-1 (centre).** (H-𝔊_w) is stated "on S_k at Z(V_k)" (l.73-76), with S_k the composite slice *at the lift*. BA-2
  (COMP-F2) shows that the lift is not a centre in any decaying norm. Restate (H-𝔊_w) in lane A's (C-glob) centring:
  per-level covariant slice with Feynman terms, data in a global gauge on 𝒞_glob. Outside 𝒞_glob it inherits lane A's
  (UHL) + (SL-cov) through BA-11 patching.
- **B4-2 (weights).** Lane A must carry (H-lin^∇) and (H-rem^∇) at m > 0, uniformly in the centre y of f = d(·, y). Lane A's
  BA-7/BA-8 one-coarse-unit estimates are unaffected (m ≤ 1 per coarse unit). G0-F3 / G♯_0-plain (the long-range part)
  becomes an *exponential* screening statement, which is what N2-exp already gives for gauge-invariant outputs.

**Consequence.** On the composite route, BFT-3 for n ≤ 4, both the U_j part and the E part, rests on exactly lane A's open
items at m > 0: (G♯-res), (G♯_0-field^∇), (LED-src), (G♯_0-fine-up), G♯_0-plain, and (H-rem^∇). Nothing new is added by
lane B. The two lanes share one open linear estimate.

## B.5 Failure mode B3-F1 (l.266-270): CONFIRMED as a statement about the absolute bound; one wording fix
- Z_row = 2.8489 at T = 8 (I reproduce 2.848902) and 2.866 at T = 10. The row sum is not T-converged at 1%; say so.
- **B3F1-1.** "The absolute pointwise bound grows ≥ 2.85^{k−j}" is not justified. For non-negative kernels,
  N_0(|ζ_j|⋯|ζ_{k−1}|) ≥ Π(min row sums) and ≤ Π(max row sums). The rows differ across the 324 fine links per cell, and the
  level-i ζ_i (i ≥ 1) are different operators (the fine functional is E_i^br + soft), whose row sums were not measured.
  Write "the absolute route's bound is ≈ Π_iN_0(|ζ_i|), with N_0(|ζ_0|) = 2.85".

## B.6 Failure mode B3-F2 (l.84-87, l.272-279, l.281-285, l.492, l.505): NOT ESTABLISHED; dependency claim WRONG (fix B3F2-1, binding)
- **The power count is incomplete.** By TOWER-VAR (c)-(d), φ̂ = ½|ρ|² + O(ρ⁴) and ρ = r + ρ^{(2)} + O(3). The soft cubic
  vertex at level l is therefore κ⟨r_l, ρ^{(2)}_l⟩, symmetrised. On the composite legs (the chain minimiser):
  - r_l is the residual, ≲ L^{-2(k−1−l)} own (N2-lin; lane A BA-3);
  - ρ^{(2)}_l is the S4′ BCH commutator, which BA-4 (CEN2) reduces to the oscillation of the leg on N(X, μ):
    ≲ L^{-3(k−l)} own on smooth legs (BA-6).

  The density is then ≲ L^{-5(k−l)} per level-l site, and L^{4(k−l)} sites per level-k unit give **L^{-(k−l)} per level:
  irrelevant, not O(1)**.
  - B3-F2's count ("three legs of size L^{-(k−j)} and one derivative") treats the vertex as a generic cubic, which the
    residual factor forbids.
  - The Wilson cubic vertex lives at level 0 only, so it is one level, not a level sum.
  - I have not written the Lipschitz forms. Lane A labels (H-rem^∇) ARGUED for exactly this reason. So the correct status
    is "absolute generic bound O(k); with the residual structure + CEN2, irrelevant [sizes PROVEN in BA-4/BA-6,
    unreviewed]".
- **The dependency conclusion is wrong independently of the count.** BB-E1 writes ∂^nE_k^br as derivatives of the local
  function ∇_yE = −κπ(M̄_y(U_{k−1})V_y^{-1}).
  - BFT-1/2 make this function holomorphic and bounded (|π| ≲ soft fluctuation ≤ C_0ε) on the uniform polydisc.
  - So Cauchy gives |∂^{n−1}∇_yE| ≤ (n − 1)!C(2/(r_ℂε_0))^{n−1}, **k-uniformly, from BFT-1/2 alone**. Decay needs (H-𝔊_w) in
    addition (BB-3_k).
  - The "non-running" cancellation that B3-F2 asks for is therefore encoded in BFT-1/2's uniform radius, which is lane A's
    BA-4-BA-6 content. It is not BFT-4 content.
- **Fix B3F2-1.** Replace "OCCURS [inference]" with "OCCURS for absolute generic-vertex bounds only; the residual structure
  of the soft vertex + CEN2 (BA-4/BA-6) make the level sum geometric". Replace "⊂ BFT-4" / "BFT-4 ⇒ BFT-3(E), not the
  converse" (l.87, l.285, l.478, l.492, l.505) with "k-uniform constant ⇐ BFT-1/2 (Cauchy via BB-E1); decay ⇐ (H-𝔊_w)".
  BB-4c (iv) remains a *second* derivation, from BFT-4.

---

# PART C: check bb1

## Pre-registration: CONFIRMED
`stat` (EDT): bb1_criteria.md 00:54:32, bb1_decay.py 00:54:56, bb1A/B.out 00:56:07/00:56:36, bb1_diag.py 01:02:07,
bb1diag.out 01:02:43. The criteria predate the script by 24 s and the outputs by 1.5 min. The diagnostic postdates A2's
FAIL and is disclosed as post-hoc (l.10-11 of the log; l.445-449). The lock was acquired twice, and both acquisitions are
disclosed.

## Script audit (line level)
- `hats` (l.22-49):
  - a_S = κC^0Q^T (`kap*Cg[:, 6:]`, Cg = Õ^{-1}rhs − (1 − Π)rhs, rhs = [D^*ι, Q^*]). This matches c37's level0_hats.
  - a_B = J + x d_1 with x = −Cg[:, :6] = −C^0D^*ι. This matches CURV-lin (i).
  - H_1 = −κ(Qx)d_1. This matches H-fac.
  - Hermitian completion at −K. Correct.
- A1 compares d(a_S − a_B) and Q(a_S − a_B) fibrewise. This is a genuine test, not a tautology (the formulas differ), and
  the tolerance 1e-6 is honest. One observation: `Dk` in A1 is the fibre d of the fine level (F.d(K)), which annihilates
  fluctuation gauge directions as claimed.
- `stats` (l.52-71) casts every hat to complex128 before the FFT and accumulates in float64. The T = 10 hats are solved in
  complex64 (l.80). That is adequate for profiles down to 8·10⁻⁵ against a maximum of 0.7, since complex64 relative
  precision is ≈ 6·10⁻⁸.
- P(s) is the max over the cells at coarse ℓ^∞ shell s. The local rates r_s = log(P(s)/P(s + 1)) match the criteria.

## Is c37 really float32? **YES, verified in source**
- c37_kcurv.py l.136-141: `level0_hats(..., cdt=np.complex64)`, and xh, aph are allocated complex64 unconditionally.
- l.162-169: `kernel(hat, rdt=np.float32)`: `out = np.zeros(hat.shape, rdt)`.
- l.195-196: `colsums(k) = np.abs(k).sum(axis=(0, 1, 2, 3, 4))`, a float32 reduction over 8⁴·324 ≈ 1.3·10⁶ entries along
  non-contiguous axes, where numpy does not use pairwise summation.
- l.403: D2 calls `colsums(ka)` on that float32 kernel.
- The diagnostic isolates the cause cleanly. The same float32 kernel summed in float64 gives 156.686796. complex128 solves
  cast to complex64 reproduce 156.078934 exactly. So the 0.39% discrepancy is the reduction, not the solve.
- The row sum (reduced over axes including the contiguous last one) agrees to 2·10⁻⁶. **156.6868 is right.**
- A2's recorded verdict FAIL is correct practice: the criterion was pre-registered against a number that turned out to be
  wrong. l.448's "(1 + Z_col)(1 + Z_row)² = 2.33·10³" is right: 2327 → 2336. c37 D2 printed a different combination,
  (1 + Z_col)max(1, Z_row)², which changes 1274.9 → 1279.8. Both change in the third digit only (B-bb1-1: name which
  quantity E3 uses).

## Re-run under the numeric lock
See the "Re-run record" below.

## A3 reading
- **B-bb1-2.** "Decays at ≈ 1.7-2.4 per coarse ℓ^∞ shell" (l.222, l.453) is right as written. It is a rate in ℓ^∞ shells,
  while BFT's d is ℓ¹. The file's own weighted sums (N_{0.5} = 18.9, N_{1.0} = 5216 at T = 10) place the ℓ¹ rate between
  0.5 and ≈ 1. The comparison with the proven rate should use the ℓ¹ figure: measured 0.5-1, proven Lμ_1 ≈ 7.2·10⁻¹¹
  (B1-1) per level-1 ℓ¹ unit, a gap ≈ 10¹⁰.
- The shell s = 5 at T = 10 is antipodal (wrap). A3 tests only s ≤ 3 for stability and r_2, r_3 for rate, which is correct.
- The non-monotone local rates (a_S: 0.87, 1.03, 3.04, 0.95, 2.13) are cell-geometry oscillations, as the file says. A3's
  ≥ 0.5 thresholds were met with margin only at r_3(a_S) = 0.945.

---

# PART D: BFT-4

## D.1 Construction BB-loc at k = 1 (l.289-314): CONFIRMED (one routine gap)
- **The pinned problem.** Λ_Y is Π-invariant (Π is the identity on crossing links and acts within blocks). So
  K_Y = Π_YO_YΠ_Y ⊕ (1 − Π)1_Y and C_{0,Y} is the inverse of the compressed slice operator on H_Y.
  - The contraction (Lip ≤ 𝔠_∞C_♭r ≤ ½, ||Φ_Y(0)||_∞ ≤ 6𝔠_∞ε) is BR1's, given N_0(|C_{0,Y}|) ≤ 𝔠_∞.
  - **B-loc-1 (routine).** That bound needs Theorem RW (or RW-ℓ²) for K_Y. (RW1)/(RW2) do hold for compressions: CT♯ on
    (Õ(1, 1))_{Ω_□∩Λ_Y} with gap ≥ γ_0 and D_m entrywise smaller. But the RW partition of Λ_Y is into Ω_□ ∩ Λ_Y, which are
    not boxes, and RW is stated for box partitions ([R20-fix RW2-1]). Add one sentence: RW's proof uses the partition only
    through (RW1)/(RW2) and the box counting, both inherited by intersections.
- **(a)** A*_𝒬 = A* (the same map). Möbius inversion with ΔE(∅) = 0. Correct.
- **(b)** Gauge invariance holds:
  - h_{ĜU^(0)} = h (interior links stay 1);
  - R_Ĝ preserves ker h (hR_Ĝ = A_Ĝh) and the fixing (N5-cov);
  - f_{GV}(R_ĜA) = f_V(A).

  The support X^+ is correct for M_c ≥ 3.
- **(c)** The *-connectivity argument holds:
  - K_{Y_1∪Y_2} splits (Õ range ≤ 1 block);
  - the nonlinear equation splits (variables ≤ 2 blocks < M_c);
  - the unique fixed point in the r-ball of H_{Y_1∪Y_2} is the sum;
  - no density (diameter ≤ 2 blocks) touches both supports;
  - the Möbius sum of an additive set function over a disconnected X vanishes.

  Correct, also on the complex domain by the same argument.
- **(d)** U0 (ii): L^{d−2} corner plaquettes per coarse plaquette. E_∅ = L^{d−2}S_W(V). Correct.
- **Reading note (not a defect).** R_1 = (L^{d−2} − 1)S_W + Σ_XR(X) is O(1)·S_W, not small. The quadratic form of E_1^br is
  H_1(1) = κ_0(1 − κ_0QC_0Q^T) (SC1), not that of S_W. BFT-4 asks only for ||R||_𝒜 ≤ C_0, so this is allowed, but it matters
  for BB-4-ind (D.5).

## D.2 Does COMP-F2 (lane A's BA-2) affect BB-loc? **Not at k = 1; yes for the general-k sentence (l.313-314), fix B-loc-2**
- At k = 1 the pinned problems are one-step contractions in the **undecayed sup norm** about the one-step lift. BA-2's
  conclusion is that (CL-1) at the lift holds in sup (θ_w = 0) and fails only in decaying (scale-weighted) norms. BB-loc
  uses only BR1's sup-norm contraction, so it is unaffected.
- At general k, "the same construction for the composite problem with S_k-compressions" pins the fluctuation to the
  **composite** lift Z^lift off Y. Then:
  - (i) By TOWER-VAR (b) (k-fold corners), E_∅ = L^{k(d−2)}S_W(V_k) = **L^{2k}S_W(V_k)**. Single-cube activities
    ΔE({Q}) ≈ (c − L^{2k})S_W|_Q are O(L^{2k}), so ||R_k||_𝒜 is not k-uniform for this decomposition (cancellations occur
    only in the full Möbius sum).
  - (ii) By BA-2, the pinned composite problems' centre is ≳ L^kε from the tower in every decaying norm. So "BFT-0 on the
    pinned composite problems" is not available in lane A's 𝔐^∇.
- **Fix B-loc-2.** Restrict BB-loc to the **one-step** use, as BB-4-ind (O2) does: level-k action → level k + 1, pinned to the
  one-step lift, factor L^{d−2} once. Alternatively, pin to lane A's centre: the trivial chain in a global gauge (this
  breaks the gauge covariance of (b) unless the pinning is gauge-covariant) or a smooth lift (needs (UHL)). Delete "general
  k: … an implication; not written" or replace it with this.

## D.3 Lemma BB-mix ⇒ bound and the 05:09 correction (l.316-327): CONFIRMED; three fixes
- The corrected argument is right:
  - *-connected cube sets containing a given cube number ≤ (eΔ)^{n−1} with Δ = 3⁴ − 1 = 80 (the standard lattice-animal
    bound);
  - Σ_nc_an^{n−1}e^{m_0n}K^{(n−n_0)_+} < ∞ iff c_ane^{m_0}K < 1;
  - no distance decay beyond connectivity is needed.
- The first version's error, counting polymers as unconstrained subsets, is correctly identified and corrected in place.
- **B-mix-1 (binding).** The pre-stated §1.4 still carries the withdrawn statements unmarked:
  - l.96-98 has the old (BB-mix): "K^{|X|}Σ_{trees}Πe^{-md}";
  - l.99-101 has BB-mix-gap's "the polymer sum of e^{-μ max d} diverges", which the correction says is false.

  Mark both in place: "[superseded 05:09: see §2.4]".
- **B-mix-2 (l.324-327, [inference]).** "At least (n − n_0) cube widths must be crossed, each costing e^{-μM_c}" overstates
  the gain.
  - In a compact blob of n cubes, a density's dependence tree can visit ≈ 2^d = 16 cubes per corner point. So the
    Steiner length needed is ≳ (n/2^d − 1)M_c, not (n − n_0)M_c.
  - The natural K is ≈ Ce^{-μM_c/2^d}, and M_c ≳ 2^d(m_0 + log(Cc_an))/μ.
  - With B1-1's μ_1 = 2.4·10⁻¹¹ this is M_c ≳ 10¹³ level-0 spacings, still of CE-exp's order (3.2·10¹³; SF l.785, which
    uses μ = m_1).
- **B-mix-3 (l.329-341).**
  - BB-mix-gap (1) is PROVEN: R(X) is the |X|-th Möbius difference in pinning, and BFT-3's n ≤ 4 V-derivatives do not
    reach it.
  - (2) is a **route failure**. It bounds the coercivity radius in t of *one* interpolation family (|Im t| ≲ γ/(4(S + γ))).
    It does not prove that no holomorphic family with a large radius exists. Label (2) **ARGUED (route NO-GO)**, not
    PROVEN-HERE.
  - Also, the Cauchy radius about points t ∈ [0, 1]^X is ϱ − 1, while the requirement is written as "ϱ ≥ 1/K" (l.333).
    State it as "the radius about [0, 1]^X must exceed 1/K".

## D.4 Routes (R1), (R2) (l.343-359): CONFIRMED as recorded obstacles
- The pitfall in (R1) is right. C_0(s) is injective, so A − C_0(s)𝒢(A) has the zeros of 𝒢 as fixed points for every s.
- The stated remaining obstacle is correct: the nonlinear N(A) couples neighbouring boxes, and the smallness per box is
  O(ε) against entropy 3⁴.
- (R2)'s p! vertex loss is correct for star-like trees.

## D.5 Lemma BB-env (l.361-370): CONFIRMED
- E′ = δR(U(s)) by criticality in every fine direction.
- E″(0) = ⟨∇δR, U′(0)⟩ with Hess F·U′ = −∇δR modulo gauge directions, against which ∇δR is orthogonal. SC1's representative
  argument gives U′ = −C∇δR. Correct.

## D.6 Proposition BB-4-ind (l.372-384): algebra CONFIRMED; description WRONG; near-vacuous as stated (fixes B4i-1..3, binding)
- **Algebra.** r_* is the smaller root of C_Qr² − (1 − λ)r + C_W = 0. The induction x_k ≤ r_* ⇒ x_{k+1} ≤ r_* holds from
  x_0 = 0. r_* ≤ 2C_W/(1 − λ) follows from √(a² − b) ≥ a − b/a. Correct.
- **B4i-1 (anti-circularity, l.384).** BFT's clause (REVIEW_S22 l.422-423) forbids "the per-level covariances C^{(j)} as
  Newton inverses" and requires "one contraction for 𝔉_k in 𝔐".
  - BB-4-ind's (O1) is the one-step branch with BR1/N5-sf0 conclusions, which is exactly a per-level Newton inverse.
  - "No composite covariance enters — the anti-circularity clause is respected" inverts the clause.
  - Write instead: "BB-4-ind is the per-level (Balaban-type) architecture, an alternative to BFT's composite route. It is
    non-circular if (O1)-(O4) are proven with constants depending only on ρ_R, but it is outside BFT's anti-circularity
    clause."
  - The same applies to the "logical order" paragraph (l.497-499).
- **B4i-2 (scale invariance of the closing condition).** On a polydisc of radius ρ in curvature coordinates:
  - C_W ≍ sup|R_1(X)| ≍ c·ρ² (R_1 is O(1)·S_W, D.1);
  - BB-env's second-order term gives C_Q ≍ 1/ρ² by Cauchy.

  So 4C_QC_W is a ρ-independent O(1) number, and shrinking ε_0 cannot make 4C_QC_W ≤ (1 − λ)² true. With λ ≥ 1 (B4-F1) the
  condition fails outright in ||·||_𝒜. The same scale-invariance also forbids treating (O1) as perturbative in R. Hess R_1
  is O(1) relative to Hess S_W, so (O1) is the non-perturbative per-level N5 at level k for actions E_k^br, i.e.
  NAH-unif/(I_k). Record both points next to B4-F1.
- **B4i-3 (Lipschitz strengthening).** Φ_k depends on k through κ_k. |R_{k+1} − R_k| ≤ Lip·|R_k − R_{k−1}| +
  |||Φ_k(R_{k−1}) − Φ_{k−1}(R_{k−1})|||. The second term vanishes only for constant κ_k, or is summable only if
  Σ|κ_{k+1} − κ_k| < ∞. Add this hypothesis.

## D.7 Failure mode B4-F1 (l.386-395): CONFIRMED (correctly labelled inference)
- The Schwarz-lemma count (fine curvature ε/L², L^4 fine polymers per coarse cube) correctly identifies the marginal F²
  coefficient.
- The remedy (Loc-extraction plus a smoothness-sensitive Taylor norm) is the standard one.
- "λ ≥ 1" needs attainment, which is not shown, and the file says "inference for the attainment". Fine.

## D.8 Corollary BB-4c (l.397-429): CONFIRMED-WITH-FIX
- **(i) (fix B4c-1).** R_i(X) depends on V on X^+, not on X (BB-loc (b)). The derivative sum is over links of X^+:
  (n_Q|X^+|)² ≤ (81n_Q|X|)², and the polymers are X with b ∈ X^+. Either re-index polymers by X^+ (m_0 → m_0/81 in the
  norm) or carry the factor 81². The same applies in (iii) and (iv) ("polymers X containing the cubes of all y's" → "with
  X^+ containing").
- **(ii) (fix B4c-2).** ∇R_i(1) = 0 by Ad-invariance is correct. But "on contractible X a flat field is gauge-trivial" is
  used in (iii)'s far term "at flat points" for polymers leaving Λ. Those include *-connected X with holes, i.e. X^+ not
  simply connected, where flat fields with non-trivial holonomy are not gauge-trivial.
  - Fix: Taylor-expand about V = 1 in an AX gauge of X^+ (links ≤ 3·diam(X^+)·ε, AX) instead of about a flat point. This
    costs poly(|X|), which e^{-(m_0/2)|X|} absorbs, for |X| ≲ r_ℂε_0/ε.
  - For larger X, use plain Cauchy: the bound C e^{-(m_0/2)|X|} with |X| ≳ ε_0/ε is ≤ e^{-c/ε} ≪ ε.
  - Write this.
- **(iii)-(v).** These are plausible as implications. The far term's rate m_0/(2M_c) comes from BFT-4 at level i directly,
  so no compounding across levels occurs. The claims "θ-cascade CURV-F2″ does not arise" and "r-compounding S22-4 does not
  arise" are therefore correct *given BFT-4 at every level*. (v)'s "NAH-unif′ ⇐ (H-K) + BFT-2 + BFT-4" is consistent with
  REVIEW_S22 l.426: under BFT, NAH-unif′ is unnecessary, and BB-4c (v) says what it would take on the per-level route.
- **(iv).** The rate m_0/(8M_c) per level-i unit is correct (|X| − 1 ≥ 𝔱_S/(4M_c) − n, split e^{m_0|X|}), with fix B4c-1's
  X^+.

---

# Overclaims
1. BB-NL's title "BFT-0/1/2 do not imply BFT-3" (l.57, l.504). Fix B-NL-1.
2. "The k-uniform n = 3, 4 part of BFT-3 for E is … a consequence of BFT-4, not an input to it" / "BFT-4 ⇒ BFT-3(E), not the
   converse" (l.86-87, l.285, l.492, l.505-506). Fix B3F2-1.
3. "Anti-circularity clause is respected" (l.384). Fix B4i-1.
4. "General k: the same construction … given BFT-0 on the pinned composite problems" (l.313-314). Fix B-loc-2.
5. BB-mix-gap (2) labelled PROVEN-HERE. Fix B-mix-3.
6. μ_1 = 4.8·10⁻¹¹, Lμ_1 ≈ 1.4·10⁻¹⁰ (l.220, l.459). Fix B1-1.

No item is counted in the PROOF tally, and none should be until it has been through this review's fixes.

# Tally (lane B session 1; unreviewed before this file; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | BB-geo, BB-C, BB-IFT, BB-MCT (solid), BB-E1, back-substitution identity, BB-loc (a)-(d) at k = 1, BB-mix ⇒ bound, routes R1/R2 as obstacles, BB-env, B4-F1 (inference), B3-F3 (solid norms) |
| CONFIRMED-WITH-FIX | **Theorem BB-3_1** (B1-1..4), BB-3_k (B3k-1..3), BB-4c (B4c-1, -2), B3-F1 (B3F1-1) |
| CONFIRMED, title/description wrong | BB-NL (B-NL-1), BB-4-ind (B4i-1..3) |
| RELABEL | BB-mix-gap (2): PROVEN-HERE → ARGUED (route NO-GO) |
| NOT ESTABLISHED | B3-F2 (power count incomplete; dependency conclusion wrong) |
| OPEN, correctly labelled | (BB-mix), (H-𝔊_w) k ≥ 2, (H-op), (O1)-(O4), (LEG_w) [ARGUED] |
| check bb1 | pre-registration CONFIRMED; A1 PASS, A2 FAIL (verdict correctly kept; c37 D2 float32 artefact VERIFIED in source), A3 PASS; my rerun byte-identical |

# Required fixes (binding for the next lane-B session)
1. **B1-1.** μ_1 = m_1/2 ≈ 2.4·10⁻¹¹ (level-0 units), Lμ_1 ≈ 7.2·10⁻¹¹ (l.220, l.326, l.459). Redo the M_c estimate with
   B-mix-2.
2. **B1-2/B1-3/B1-4.** The unit-conversion sentence, chart versus left-trivialised derivatives, "analytic continuation", and
   a closed or shrunken 𝒟. Add to BB-geo that the star is a spanning tree, so 𝔱 can replace 𝔱_S throughout.
3. **B-NL-1.** Narrow BB-NL to the analytic content of BFT-2, at l.57-59, l.162 and l.504.
4. **B3k-1/2/3.** The half-radius domain, the Gronwall expansion with (LEG_w) for all sub-chains, and gauge compatibility
   across levels. Mark the telescoping route as the per-level alternative.
5. **B4-1/B4-2.** Restate (H-𝔊_w) in lane A's (C-glob) centring with m > 0, and record that it *is* lane A's (H-lin^∇)_m
   (sub-items (G♯-res), (G♯_0-field^∇)) plus (H-rem^∇)_m. (LEG_w) is lane A's open data-map row at m > 0.
6. **B3F2-1.** Correct B3-F2 and every "⊂ BFT-4 / BFT-4 ⇒ BFT-3(E)" sentence (l.86-87, l.285, l.478, l.492, l.505-506).
7. **B-loc-1/B-loc-2.** Add the RW-for-compressions sentence. Restrict BB-loc to one-step use, or re-centre it; delete the
   lift-pinned general-k sentence (E_∅ = L^{2k}S_W).
8. **B-mix-1/2/3.** Mark l.96-101 as superseded in place. Use K ≈ e^{-μM_c/2^d}. Label BB-mix-gap (2) as a route NO-GO
   (ARGUED).
9. **B4i-1/2/3.** BB-4-ind is the per-level architecture, outside BFT's anti-circularity clause. 4C_QC_W ≤ (1 − λ)² is
   scale-invariant, and (O1) is non-perturbative. Add the κ_k variation to the Lipschitz strengthening.
10. **B4c-1/B4c-2.** Use X^+ in (i)/(iii)/(iv). Replace "flat point / contractible" by the AX-Taylor plus large-|X| Cauchy
    split.
11. **B-bb1-1/2.** In l.448, say which combination E3 uses: (1 + Z_col)(1 + Z_row)² goes 2327 → 2336, and c37's printed
    (1 + Z_col)max(1, Z_row)² goes 1274.9 → 1279.8. Compare the
    proven and measured rates in ℓ¹ (0.5-1 measured). Note that Z_row and Z_col are not T-converged at 1% (T = 8 → 10:
    2.849 → 2.866, 156.69 → 158.06).

# Strategic verdict: the minimal set of open estimates BFT-0..4 now rest on (lanes A and B merged)

On 𝒞_glob (small data in a global gauge), with lane A's centring (C-glob) and Balaban's identification convention (BA-9):

1. **(H-lin^∇)_m: one linear estimate at the trivial chain in (𝒴^∇ → 𝔐^∇), with exponential weight m > 0 uniform in the
   centre.**
   - Sub-items, all OPEN: (G♯-res) (residual-type sources, which are exactly BFT-3's top sources s_y); (G♯_0-field^∇)
     (configuration-level ∇-control and the data map into 𝔐^∇ = lane B's (LEG_w)); (LED-src); (G♯_0-fine-up); G♯_0-plain
     (global; with m > 0 an exponential-screening statement).
   - The m = 0 → m > 0 step is lane B's (H-op): a Combes-Thomas commutator estimate in the coarse-unit pair, plausibly
     routine there.
   - **This single estimate feeds BFT-0, 1, 2 (lane A) and BFT-3 (lane B, via BB-3_k), including BFT-3's E-part with a
     k-uniform constant.**
2. **(H-rem^∇)_m: the nonlinear remainder bounds in the same weighted pair.** ARGUED: the second-order sizes are PROVEN-HERE
   in BA-3-BA-6, but the Lipschitz forms and the Hölder algebra are not written. The centring cancellation CEN2 that it
   contains is also what removes B3-F2.
3. **(FP♯') in the weighted pair.** This is a hypothesis of lane A's Theorem BA.
4. **(BB-mix)_k: per-cube smallness K < e^{-m_0}/(80e) of the Möbius differences of one-step pinned problems, uniformly in
   k.** OPEN even at k = 1. It is an all-order propagation estimate, not reducible to BFT-3 (BB-mix-gap (1)). Its natural
   source is the weighted inverse of item 1 applied to the *pinned* problems with tree expansion (route R2), losing p!
   vertex factors, or a second interpolation of the nonlinear couplings (R1).
5. **(Loc-4): level-uniformity of BFT-4.** BFT-4 cannot be closed by induction in its own polydisc norm (B4-F1; B4i-2). A
   per-level induction is needed in a smoothness-sensitive norm with extraction of the marginal F² coefficient, which is
   fixed at tree level by FLOW F-tree and c38 C. This is the per-level architecture, and (O1) in it is the
   non-perturbative per-level N5 for actions E_k^br. **Alternatively**, BFT-4 at level k could be read off the composite
   solution by BB-loc applied one step at a time on top of BFT-0..3 (items 1-4). That alternative is not written by either
   lane, and it is the route consistent with the anti-circularity clause.
6. **Outside 𝒞_glob (generic curvature-small backgrounds):** (UHL) (a local Coulomb-type gauge with coarse C^{1,α} control),
   (SL-cov) (a local covariant fixing), and the slice-term part of (COMM). These are lane A's; BFT-3/4 inherit them through
   patching.

**Net.** BFT-0..3 rest on one linear estimate (1) plus the remainder bound (2) and (FP♯'), with (6) for generic
backgrounds. BFT-4 adds two genuinely new estimates, (4) and (5); neither BFT-0..3 nor Cauchy produces them. At k = 1,
BFT-3 is a theorem (BB-3_1, after B1-1..4), and BFT-4's decomposition exists exactly (BB-loc), with only (4) open.

---

## Re-run record
- Runner: `revBB1/run.sh` in the scratchpad.
  - It waits with `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, then waits for load1 < 8.
  - Environment: nice 10; OPENBLAS/OMP/MKL/vecLib threads = 1; PYTHONDONTWRITEBYTECODE=1 (so no `__pycache__` is written
    into the read-only checks/); `/usr/bin/time -l`; python3 without -I; no `timeout`; no trap.
  - It runs `bb1_decay.py A`, `bb1_decay.py B` and `bb1_diag.py` from checks/ unchanged, with outputs to `revBB1/`.
  - It calls `rmdir` exactly once.
- Lock held 05:20:21-05:22:15 UTC (load1 2.60, free 42%). Wall times: A 52.3 s, B 31.7 s, diag 30.2 s. Peak RSS 588 MB.
  After the run: no process is left (`pgrep` empty), the lock directory has been removed, and checks/ holds no pycache.
- **Result: with the timing/RSS suffixes stripped, bb1A.out, bb1B.out and bb1diag.out are byte-identical to the recorded
  ones.** A1 PASS (6.00e-15, 7.52e-14); A2 FAIL (Z_row 2.848902, Z_col 156.686797); A3 PASS; diag 156.078934 / 156.686796
  / 156.686797 / 156.078934.
