Reviewer model: claude-opus-5-5

# COFM55 — Theorem COF / Theorem CC-FUN (b) at m > 0 (exponentially weighted version)

## PRE-STATED (written 2026-10-28T23:53Z UTC, before any derivation; only the brief REVIEW_BRIEF_55.md and the task text had been read)

Worker role: Opus 5.5 worker (not a reviewer of a batch); the binding rules of REVIEW_BRIEF_55.md apply.
Write scope: this file `$L/COFM55.md` and `$L/checks/cm55_*` only. No git.

### Targets
- **T1 (statement).** State precisely what BFT-5 clause (b) (REVIEW_S22.md, located by string) and each of
  its consumers need at m > 0: which norm (the e^{±m d}-weighted sup / Campanato (Hölder) pair, d = level-k
  ancestor distance), which range of m (0 < m < m_*′, with m_*′ located by string and its definition quoted),
  and whether uniformity in k and T is required.
- **T2 (proof).** Prove, or locate exactly where the proof fails, Theorem COF and Theorem CC-FUN (b) at
  m > 0, via a weighted (Combes-Thomas type) conjugation from the banked m = 0 results, addressing each
  item CODEX_REVIEW_GAPZ.md F5 lists: uniform a(m); fine/coarse measure factors; weighted source and output
  maps; Campanato (Hölder) estimates; the slice transfer.
- **T3 (inputs).** Check that the X1 / Lemma FLUX root-charge step survives the weights (claim to test:
  each entry of the face-flux current reads one face, so the weights cost only e^{O(m)}); locate weighted
  versions of LINEAR_PACKAGE Thm 4.2(ii) and BFT_A Prop BL-4, or state that they are missing.
- **T4 (uniformity).** Say whether the m > 0 result is uniform in k and T, and how small m must be
  (explicit dependence of the admissible m on the constants that enter).

### What would count as a refutation (of "COF / CC-FUN (b) hold at small m > 0, uniformly in k, T")
- R1. An operator in the chain whose kernel is NOT uniformly finite-range or exponentially decaying in the
  level-k ancestor distance (e.g. a non-local projection — Hodge/Leray-type projection onto a co-closed
  class has only power-law decay in general), so that ‖W_m X W_m^{-1} − X‖ is not O(m) uniformly in k, T.
- R2. A range or coefficient bound that grows with k or T (e.g. a range measured in fine units that is
  ~L^k in level-k units, or a Schur bound that carries a volume factor), making a(m) non-uniform.
- R3. A step in the m = 0 proof that is not an operator-norm statement on a fixed space (e.g. a
  compactness/contradiction argument, a duality/zero-mode count, a sup over a global set of sources) so
  that the conjugation template has nothing to act on.
- R4. A face-flux / root-charge entry that reads unboundedly many faces or a region whose diameter grows
  with k, so that weights cost more than e^{O(m)}.
- R5. A weighted input (LINEAR_PACKAGE Thm 4.2(ii) weighted, BFT_A Prop BL-4 weighted) that is absent and
  not derivable by the same conjugation — then the m > 0 theorem is CONDITIONAL on that input, which I
  must state as such rather than call proven.
A precise statement of a missing input is an acceptable outcome; a CONFIRMED / PROVEN that rests on
an unchecked input is not.

### PRE-STATED addendum (appended 2026-10-29T00:18Z, after READING and exploratory reasoning, before any criteria file, script or written derivation)

Reading done before this addendum (no derivation written to any file): REVIEW_BRIEF_55.md; PROOF.md l.1-60 ([S26-BANKED],
[S26-REVIEW]) and l.3466-3482 (the m_*′ definition); COFUN_CC.md in full; REVIEW_S22.md l.370-450 (BFT statement);
BFT_B.md l.90-110, 170-205, 286-330, 3584-3602, 3625-3626, 3655-3714, 3740-3780 (§29.5, §30), 3820-3860 (§32), 4003-4110
(§35.0-35.6); BFT_A.md l.436-560 (§7), 588-684 (§8.1-8.6 incl. BL-4 and its weighted remark), 875-960 (§12), 1069-1215
(§13.8-13.13: Lemma TS, Prop W, Thm W, Cor FP), 1392-1560 (§18.1-18.6), 1688-1760 (§21), 1874-2080 (§23), 2195-2290
(§26), 2401-2720 (§28 incl. §28.13), 2752-2850 (§31), 3049-3260 (§33.8-35), 3287-3360 (§36), 3465-3510, 3622-3740
(§38.1-38.2, §38.10, §40); LINEAR_PACKAGE.md l.97-116, 205-290 (§4), 356-386 (§6.2), 424-494 (§9-10); RTARGET.md l.572-700;
CODEX_REVIEW_GAPZ.md l.55-100 (F5); CODEX_REVIEW_TOPCC.md (on disk now: 363 lines, complete, ends with "Exactly what may
be banked"; read l.1-41, 147, 268-296, 348-363 and the grep hits); REVIEW_BFT_A_S3 l.295-330; REVIEW_BFT_A_S5 l.20-45,
98-170, 225-250, 380-395; REVIEW_BFT_A_S6 l.15-35, 99, 181, 293-345; REVIEW_BFT_A_S7 l.1-80, 270-335; REVIEW_BFT_B_S9_S10
l.241-290; SESSION25_RESULTS.md l.1405-1440; GSHARP55.md (35 lines, stub).

Suspicions formed while reading (marked (c): no pre-registration weight beyond the label).
- **T5 (c) GU at m > 0 without DX_m/DB_m.** BFT_A §28.13 and BFT_B §30 make the weighted sup of Theorem GU conditional on
  DX_m, DB_m (OPEN; and DB's proof pairs against the global Coulomb representative, whose gradient tail is polynomial
  (LRL (a): (1 + D)^{-5}), so it cannot absorb e^{md} test currents). Suspicion: for DIVERGENCE-FORM level-l sources the
  carrier class is not needed — ⟨d*G_l, Y^p_l⟩ = ⟨G_l, dY^p_l⟩ is a curvature (gauge-invariant) pairing, and a weighted
  ℓ¹ bound on the level-l curvature of the plaquette response closes by the same Lemma LD bootstrap with (i) Lemma EX's
  carrier bound for the explicit part (through Lemma CS), (ii) Theorem W's weighted sup of f_l(Z′), (iii) Lemma BW.
  Refuted if any of the three inputs does not cover the level-l curvature, or the bootstrap needs a quantity that is not
  a curvature, or a power of L^{k-l} or a factor T survives.
- **T6 (c) Theorem COF at m > 0, for 0 ≤ m ≤ m_Y.** Given T5, every input of COF's proof (BFT_B §35.5 (a)-(d)) has a
  CONFIRMED weighted version up to m_Y (W0_m, Thm W, the 𝒩_m part of Thm Y_m, Lemma WT, W0-loc) or is local (SPLIT, DF-cc,
  COF-size, FT (iv), the push-downs). Refuted if some step uses a global (non-local, non-exponential) object paired with
  a weighted source, e.g. Lemma LE or the Coulomb potential (COF (d) cites W0 step 4 = LES-div + LE: must be replaced by
  W0-loc).
- **T7 (c) The top residual and the residual half reach m < m_*′, not only m ≤ m_Y**: TOP-cc's inputs are data-map
  bounds (Prop W, Cor FP, Thm W) with no bootstrap. Refuted if any TOP-cc step needs Y^p (the plaquette response).
- **T8 (c) Combes-Thomas as stated (Codex F5) is not available**: BFT_B Lemma BB-MCT already records B3-F3 (solid norms:
  ||𝓛^{-1}|| ~ L^{2k}, so the admissible m ~ L^{-2k}); the lane's weighted inputs are instead the translation-invariant
  form of Combes-Thomas (strip analyticity, LINEAR_PACKAGE Thm 4.2′) propagated by duality. To be stated with the exact
  failure, not re-derived as a theorem.
- **T9 (c) Locality constants.** FLUX costs e^{4m} (ℓ¹, d = 4); the DEC subtraction Q^T b costs ≤ e^{(11/3)m}; Lemma FT
  (iv)'s e^{2m} is right in ℓ¹ only because roots are block centres (with corner roots it would be e^{3m} at L = 3).
  To be decided by an exact enumeration (check cm55_loc, criteria first).

Numeric checks: only `checks/cm55_*`, criteria file first, exact integers/Fractions, rigorous rational bounds for
logarithms/exponentials, designed-FAIL controls. No check can decide k- or T-uniformity; none is claimed to.

---

## 0. Check record cm55 (criteria → amendments → scripts → one run each)

Files: `checks/cm55_criteria.md` (born 00:19:56Z; Amendment A1 00:21Z and A2 00:23Z, both appended BEFORE any script
existed and before any output was seen — A1 corrects my own wrong closed form for L3 (the decisive bound < 5ρ_b is
unchanged), A2 corrects a mis-stated sanity clause of N1), `checks/cm55_num.py`, `checks/cm55_loc.py`, outputs
`checks/cm55_num_out.txt`, `checks/cm55_loc_out.txt`, `/usr/bin/time` reports `checks/cm55_num_err.txt`,
`checks/cm55_loc_err.txt`. One run each (00:22:30Z, 0.04 s; 00:22:35-00:22:40Z, 5.1 s; < 16 MB), `python3 -I -B`,
nice 10, one thread, Fractions/ints only. No criterion edited after the run.

| item | result | what it decides (and could it fail?) |
|---|---|---|
| L0 | PASS | order-averaged h_l has no sign cancellation; its support is all 216 block-interior links (centre and corner roots) |
| L1 | PASS | **FLUX read radius D_F(l) = 4(1 − L^{l−k}) exactly** (32/9, 8/3) < 4: FLUX costs e^{4m} (could fail: C1 fires) |
| L2 | PASS | **DEC subtraction Q_{k−1}^T read radius D_Q = 10/3** ≤ 11/3 (both the Q_str^T and the h^T d* parts) (C2 fires) |
| L3 | PASS | straight push-down transposes: **D_P(a, b) = 5(ρ_b − ρ_a)** < 5ρ_b exactly as Amendment A1 predicted (C3 fires) |
| L4 | PASS | **Lemma FT (iv)**: funnel read radius 16/9 (k = 2), 52/27 (k = 3), i.e. 2(1 − L^{−k}) < 2 in ℓ¹ with centre roots; my pre-run prediction 5/3 was WRONG (I mislocated the level-0 avatar of the root), the criterion ≤ 2 holds |
| C4 | FIRES | with CORNER roots the same radius is 8/3 > 2: FT (iv)'s e^{2m} depends on the centre-root convention |
| N1 | PASS | rigorous enclosure of ln 2, width 3.4·10^{−60} |
| N2 | PASS | **ln 2/4160 ∈ [1.66621918·10^{−4}, same]** ≤ 1.67·10^{−4}: BFT_A §38.10's bound m_Y ≤ 1.67·10^{−4} is right (C5 fires at 1.66·10^{−4}) |
| N3 | PASS | at L^c ≥ 260, m ≤ ln 2/(16L^c): e^{4m(L^c+4)} ≤ 2^{264/1040} ≤ 6/5 (exact integer comparison) (C6 fires at L^c = 100) |
| N4 | PASS | Lemma BW's coefficient ¼·2^{4.2/16} ≤ ½ (sanity) |
| N5 | PASS | for every tabulated strip width (LINEAR_PACKAGE §4), m_*′/6 ≥ 2.33·10^{−3} > ln 2/4160: the ln 2 branch of m_Y binds |
| N6 | info | e^{40 m_Y} ≤ 1.0067: every e^{cm} locality factor used below is ≈ 1 on [0, m_Y] |

What cm55 cannot decide (stated in the criteria before the run): any analytic statement (Lemma K, Theorems GU_m, COF_m,
CC-FUN_m), any uniformity in k or T, the value of C_j (so m_Y is only bounded above).

---

## 1. Symbols pinned (systemic defect 1) and conventions

- **m is the exponential WEIGHT rate only.** BFT_B §35.5 (c) and COFUN_CC §6.1 use m as a level index ("Σ_{0≤m<k−1}",
  "m = k − 1 − i"); below, level indices are i, l, l′, a, b — never m.
- **m′** is the package weight at which the dual responses are bounded: BFT_A fixes **m′ := m_*′/3** (§18.4 "Fix
  m′ := m_*′/3", §21.0); μ := m′ − m; **S(μ) := coth⁴(μ/2)** (BFT_A §13.9). Where a statement holds "for m < m_*′", read
  "with any m′ ∈ (m, m_*′), constants depending on μ".
- **m_*′** (located by string, PROOF.md l.3480): "Let η′_*(κ, κ̂, L) be the largest η ≤ 0.1 for which some r_0 gives θ_a ≤
  π/2, ρ_R ≤ ½, Ψ_L ≥ 1/10, br′_V ≥ (1 − ρ_R)/(4D_2Γ) and 4c_φ ≤ ψ_0/2, and **m_*′ := min_{κ∈[κ_−,κ_+]}η′_*.**" — the
  proven analyticity strip of LINEAR_PACKAGE Theorem 4.2′ (N2-exp′); 0.0384 at L = 3, κ ≡ 1 (LINEAR_PACKAGE §4 table).
- **m_Y := min(m′/2, ln 2/(16L^c))** (BFT_A §26.3, Lemma BW), c fixed by **L^c ≥ max(260, 6952C_j)** (§33.11 heading;
  Lemma BW's ¼-contraction), C_j = C(C_K, C_φ) uncomputed.
- **Weights** (BFT_A §12.0, §13.9, §31.0; LINEAR_PACKAGE §1.4): coarse position of a level-l object = L^{l−k}·(base
  point); **dist** := ℓ¹ torus distance of coarse positions (never ℓ^∞ unless said); w(z) := e^{m·dist(z, X_0)};
  ||H||_{∞,m} := sup_z w(z)|H^c(z)|; [H]_{α,m} := sup_B w(z_B)ρ^{−α}Osc_2(H^c; B) (box-weighted Campanato);
  [H]^∞_{α,m} := sup_{z≠z′,|z−z′|_∞≤1} w(z)|H^c(z) − H^c(z′)|/|z − z′|_∞^α (weighted pointwise, BFT_A §13.9);
  ||x||_{inv,m} := max_j[||f_j||_{∞,m} + [f_j]_{α,m} + L^{k−1−j}||r^c_j||_{∞,m}]; ||s||_{R,m}, ||B_k||_{D,m} as BFT_A §12.0;
  **||G_0||^L_m := ||e^{mφ_{X_0}}G^c_0||_∞ + [e^{mφ_{X_0}}G^c_0]^∞_α** (Lipschitz-weighted source norm, BFT_A §31.0).
  New shorthands: **π_{l,m}(j) := ||j^c_l||_{∞,m}** (= L^{3(k−l)}sup_b w(b)|j(b)|); ||j||_{Pc,m} := max_{1≤l<k}ω_lπ_{l,m}(j_l);
  |j|_{Σ,m} := Σ_{0≤l<k}π_{l,m}(j_l); **||G||^{sup}_{Y,m} := max_{1≤l<k}ω_l||G^c_l||_{∞,m}** (no Hölder norm of G_l, l ≥ 1);
  **N_m(S) := ||G_0||^L_m + ||j^c_0||_{∞,m} + ||j||_{Pc,m} + ||G||^{sup}_{Y,m} + ||s||_{R,m}**, and N_{Σ,m}(S) the same with
  |j|_{Σ,m} in place of ||j^c_0||_{∞,m} + ||j||_{Pc,m}. At m = 0 these are COFUN_CC's N(S), N_Σ(S) up to the level-0
  source norm (||G_0||^L_0 = ||G^c_0||_∞ + [G^c_0]^∞_α, equivalent to ||G^c_0||_∞ + [G^c_0]_α by BL-C).
- **Collisions avoided.** w_h := max|kernel of h_l| (= COFUN_CC's "w" = 10/81) — never the weight w(z). C_size (COF-size)
  vs C_BLC (BL-C). G_D (BL-4, m = 0) vs G_D(m) := e^{20m}G_D♭ (Proposition W). A(μ) := 4κ̂G_D(m′)S(μ)/κ_− (COF's A at
  μ = m′). C_Z(c) (Theorem Y step 4) is Theorem W's bound for Z′, not a new constant. d = 4 is the dimension.

---

## 2. T1 — what clause (b) and its consumers need at m > 0

**The clause (located by string).** BFT_B §32.1: "(b) *Composite-co-closed sources.* For every composite-co-closed source S
(Ξ^TS = 0, §27.1), the response x = H_E^{-1}S obeys the (G♯) bounds in SF/RTARGET §33's 𝔐-pair, ||x||_𝔐 ≤ C_5||S||_{𝔐*},
together with BFT-3's weighted locality at rate ≥ m_Y …" and "(d) *Scope.* m = 0 for (a)-(c); the weighted form of (b) at
0 ≤ m ≤ m_Y is stated as the weighted clause and is **not** claimed at the same status." REVIEW_S22 l.388-392 (BFT
statement): the norm 𝔐 has "exponential weights e^{±m d} … in level-k ancestor distance", with m_0 > 0 "depending only on
(N, L, κ_±)"; RTARGET §33 (the 𝔐-pair's origin) states its targets "uniformly in k ≥ 1, T and X_0, for m < m_*′ (some
stated loss)".

**Precisely what the weighted clause (b) is.** For every weight centre X_0 and every composite-co-closed S,
||x(S)||_{𝔐,m;X_0} ≤ C_5(m)||S||_{𝔐*,m;X_0} with C_5(m) independent of k, T (T ≥ 5 for S_E; all T for the gauge-invariant
half) and X_0. Because the bound is uniform in X_0 it is an **exponential-locality statement for the response map**: a
source localised at X_0 has a response decaying like e^{−m·dist(·, X_0)} (it is not used on global objects such as the
rows S*, whose weighted norms grow like e^{mT}; the rows use m = 0). Its two halves:
- **gauge-invariant half** = (NC-Γ)_cc with weights: ||x||_{inv,m} ≤ C·N_m(S) (Theorem CC-INV_m below). Γ-independent for
  (cc) sources (Lemma FG (iii)), so no slice transfer is involved.
- **field-component half** (𝔐's gauge-variant components) = (G♯_0-field)_m in a stated slice; then the background transfer.

**Which m.** Three different ranges are on file and must not be conflated:
| source | range | where it comes from |
|---|---|---|
| RTARGET §33, LINEAR_PACKAGE Thm 6.8 | 0 ≤ m < m_*′ | the analyticity strip of the data symbols (LP Thm 4.2′) |
| BFT_A Prop W, Thm W, Cor FP, TOPD-based bounds | 0 ≤ m < m′ < m_*′ | the same strip, via kernels; no bootstrap |
| BFT_A Lemma BW, Thm Y_m (𝒩_m), QH_m, W0_m; BFT_B §32.1 (b), (d) | 0 ≤ m ≤ m_Y | the YH/Y bootstrap: the cut-off dipole has coarse radius ≈ 1.03L^c, so its weights cost e^{4.2mL^c} |
cm55 N2, N5: m_Y = ln 2/(16L^c) ≤ 1.666·10^{−4} per coarse unit (the m′/2 branch never binds for the tabulated strips).

**Which consumers, and what each takes from the weighted clause (quoted, not re-judged).**
- BFT-3 (locality, n ≤ 4) through BFT_B Proposition BB-3_k: it needs (H-𝔊_w)_k — "the response to any level-(k−1) source
  supported within the contour neighbourhood of a level-k link y, |s|_∞ ≤ 1, obeys |(𝔊s)(x)| ≤ G_0e^{−m d(x,y)} for every
  level-j link x (own units of level j, the slice representative)" — a **configuration-level** (field-component) bound,
  any m > 0, returning m_0 = m/4. At the trivial background its top-source case is the data map at a shifted datum (Lemma
  TS), whose potential half is BFT_A Corollary FP (CONFIRMED, REVIEW_BFT_A_S3) in S_tent; BB-3_k's slice is different
  (BFT_B l.99-105). Not settled here.
- The composite contraction (CL-0)-(CL-4) in 𝔐 and SF's (a5-G♯): the full weighted (G♯) pair, i.e. both halves.
- Rate thresholds: BFT_A §38.10 (table MR, read-only survey, ARGUED) finds no consumer with a threshold on m itself (scales
  R, M_c, M ∝ 1/m), with two rows NOT DETERMINED (N5's polymer scale; ε_mix at R ∝ 1/m_Y). Quoted, not re-judged.
**So T1's answer:** the weighted clause needs the e^{±m·dist}-weighted (sup + Campanato / Lipschitz-weighted Hölder) pair
of §1, for some fixed m > 0, uniformly in k, T and X_0; lane B's own statement fixes m ∈ [0, m_Y]. This file proves the
gauge-invariant half at the trivial background on that whole range (§5-§7); the field-component half and the background
transfer stay OPEN (§9).

---

## 3. T8 — the Combes-Thomas template (CODEX_REVIEW_GAPZ F5) is not the route; what replaces each of its items

**The template** (CODEX_REVIEW_GAPZ l.71-75): ||H^{-1}|| ≤ M, ||W_mHW_m^{-1} − H|| ≤ a(m), Ma(m) < 1 ⇒
||(W_mHW_m^{-1})^{-1}|| ≤ M/(1 − Ma(m)). The Neumann-series algebra is correct (CONFIRMED; it is two lines). It cannot be
applied to the m = 0 results banked for clause (b), for three separate reasons:
1. **Those results are not inverse bounds on a fixed space.** Theorems COF, W0, GU, CC-FUN, CC-INV bound gauge-INVARIANT
   outputs (f_j, r_j) by source norms. W_mHW_m^{-1} − H applied to a configuration produces terms in the configuration itself
   (potentials, undifferentiated), which no output norm controls. A configuration-level inverse bound in a fixed slice is
   (G♯_0-field) — OPEN at m = 0 (only its potential half, for data + residual sources, is proven: BFT_A Corollary FP).
2. **In the solid norms where a(m) = O(m) is automatic, M is not uniform.** This is on file as BFT_B **Lemma BB-MCT,
   failure mode B3-F3 "OCCURS for solid norms"**: "in ℓ^∞ → ℓ^∞, ||𝓛^{-1}|| ≳ L^{2(k-1)} … and in own-units ℓ² the chain's
   gap is ≲ L^{-2(k-1)} … With G ∝ L^{2k} the admissible m ∝ L^{-2k}: no uniform rate." My own scaling count agrees (ARGUED,
   not a theorem): the level-0 block d_0^*d_0 couples links within two fine steps (2/n coarse units), so
   ||W_md_0^*d_0W_m^{-1} − d_0^*d_0||_{∞→∞} ≤ ||d_0^*d_0||(e^{2m/n} − 1) = O(m/n) in own units, against an own-unit inverse of
   size ≍ n² on smooth modes: Ma(m) ≍ m·n. This is exactly Codex's "Finite range alone does not supply A uniformly over lattice
   refinements". (I did not re-derive BB-MCT's lower bound L^{2(k−1)}; NOT-VERIFIED as a theorem, consistent with my count.)
3. **In the non-solid pair** (Hölder/divergence-form, SF §33) the commutator is first order and needs the weight smoothed at
   each level's scale: BB-MCT names this (H-op), OPEN.

**What the lane's weighted inputs actually are.** For the translation-invariant data maps the template holds in Fourier form:
conjugation by e^{a·x} shifts p → p + ia, and LINEAR_PACKAGE Theorem 4.2′ (i) bounds the analytic continuation of the
B_k-symbols of r_{k−1} and f_0 by M on the whole strip {|Im p_α| < m_*′}, uniformly in k, T and the offset u. **Uniformity of
"a(m)" is supplied by Lemma 4.1's exact cancellation of the fine Green's function 1/φ**, not by a commutator estimate. Every
non-translation-invariant object (sources, slots, push-downs, funnels, root charges) enters by exact duality against dual
responses (Y^p, Y^{(b)}, the data response y^{(b)}) and through local maps with explicit e^{cm} (cm55). The only place where a
weight meets a non-local construction is the YH/Y bootstrap (Lemma LD's dipole of coarse radius ≈ 1.03L^c), priced by Lemma
BW; that is where m_Y comes from (§8).

| F5 item | how it is met below | where |
|---|---|---|
| uniform a(m) | strip bound M on {abs Im p < m_*′} (LP 4.2′), uniform in k, T, u; S(m′ − m) on summing the kernels | §4.2, BFT_A Prop W |
| fine/coarse measure factors | exact power counting: n²·L^{−2(k−l)}·L^{−2l} = 1, and 6L^{4(k−l)} level-l plaquettes per coarse cell against L^{−4(k−l)} | Lemma K steps 2-3, GU_m (ii) |
| weighted source/output maps | FLUX e^{4m}, DEC e^{(10/3)m}, straight push-down transposes e^{5m}, funnel e^{2m}; Lemma TS exact (no weight) | §4.1, §4.4, cm55 L1-L4 |
| the requested positive m | 0 ≤ m ≤ m_Y for the curvature half; 0 ≤ m < m_*′ for the residuals, the top residual and the datum | §8 |
| Campanato estimates | LES-dd → W0-loc (local; Lemma LE is NOT used — it is false with weights), Lemma WT (e^{8m}), weighted BL-C (e^{8m}) | §6 (d) |
| slice transfer | not needed for the gauge-invariant outputs of (cc) sources (Lemma FG (iii)); needed, and OPEN, for the field components | §9 |

---

## 4. T3 — the root-charge step and the two named inputs under the weights

### 4.1 Lemma FLUX_m and Lemma DEC_m. **PROVEN-HERE (elementary; cm55 L1, L2).**
> **Lemma FLUX_m.** For 0 ≤ l < k and every level-l 1-form j: **||Φ_lj||_{∞,m} ≤ e^{4(1−L^{l−k})m}π_{l,m}(j) < e^{4m}π_{l,m}(j)**.
> Hence for every Setting LIN^cc source, b(S) = Σ_lΦ_l(j_l) + s_{k−1} obeys d*b(S) = q(S) (exact, weight-free, FLUX (iii)) and
> **||b(S)||_{∞,m} ≤ e^{4m}|j|_{Σ,m} + L^{−θ}||s||_{R,m} ≤ e^{4m}K_θN_m(S)**, K_θ := max(1, (L^θ − 1)^{-1}).
>
> *Proof.* Φ_lj(X, μ) sums j over the L^{3(k−l)} level-l links (Z, μ) of the upper μ-face of B_l(X); their coarse positions
> lie in X + L^{l−k}{0, …, L^{k−l} − 1}⁴, so dist(X, ·) ≤ 4(1 − L^{l−k}) (cm55 L1: attained, 32/9 and 8/3) and
> w(X) ≤ e^{4(1−L^{l−k})m}w(Z, μ). Sum: w(X)|Φ_lj(X, μ)| ≤ e^{…}L^{3(k−l)}sup w|j| = e^{…}π_{l,m}(j). The class bound uses
> π_{l,m}(j_l) ≤ L^{−θ(k−l)}||j||_{Pc,m} (l ≥ 1) and ||s_{k−1}||_{∞,m} ≤ L^{−θ}||s||_{R,m} (ω^R_{k−1} = L^θ). ∎

> **Lemma DEC_m.** In Lemma DEC (COFUN_CC §3), parts (i), (ii), (iv), (v) are exact identities and carry no weight; (iii)
> becomes **π_{k−1,m}(Q_{k−1}^Tb_j) ≤ e^{(10/3)m}(1 + 2dL³w_h)||b_j||_{∞,m}**, hence
> ||j′||_{Pc,m} ≤ ||j||_{Pc,m} + L^θe^{(22/3)m}(1 + 2dL³w_h)|j|_{Σ,m} and **N_m(S′) ≤ (1 + L^θe^{(22/3)m}(1 + 2dL³w_h)K_θ)N_m(S)**
> (same with N_{Σ,m}).
>
> *Proof.* Q^T = Q_str^T − h^Td* (one step); the coefficients are those of COFUN_CC §2.3 (L^{−3} per link from Q_str^T,
> 2d·w_h from h^Td*), and every coarse link read lies within dist 10/3 of the output link (cm55 L2: both parts attain 10/3).
> Then Lemma FLUX_m for ||b_j||_{∞,m}. ∎

**Verdict on COFUN_CC §2.2's "its weighted version costs only e^{O(m)}" and on the T3 question: CONFIRMED**, with the
explicit constants e^{4m} (FLUX) and e^{(10/3)m} (the subtraction). Codex TOPCC §2 says the same in words ("a local weight
costs only a bounded coarse-distance factor"). The root-charge step creates no obstruction at any m ≥ 0.

### 4.2 LINEAR_PACKAGE Theorem 4.2 (ii): its weighted version is itself plus a row sum (found)
Theorem 4.2′ (ii) (LP l.219-221, with 4.2 (ii) at l.211-217) **is** an exponential kernel bound: every entry obeys
|K(X)| ≤ Me^{−m″|X|_1} for every m″ < m_*′, uniformly in k, T and the fine offset u. For 0 ≤ m < m′ < m_*′ the weighted
data map follows by the row sum Σ_Xe^{−(m′−m)|X|_1} ≤ coth⁴((m′ − m)/2) = S(μ):
**w(P)|f_0(P)| ≤ 4M·S(μ)·||B_k||_{D,m}**, i.e. X1's row-sum constant C_D = 4M((1 + e^{−m′})/(1 − e^{−m′}))⁴ (CODEX_REVIEW_X1
§3) becomes **C_D(m) = 4M·coth⁴((m′ − m)/2)** ((1 + e^{−x})/(1 − e^{−x}) = coth(x/2)). This is written in BFT_A Proposition W's
"f_0 sup" step (through LP Lemma 6.7 (KF), the level-l version), CONFIRMED given the package (REVIEW_BFT_A_S3 l.299-307).
As at m = 0 it is a sup bound per offset u and supplies no Hölder modulus in u (CODEX_REVIEW_TOPCC confirms this at m = 0;
the weights change nothing): the Hölder half comes from the weighted BL-4, next.

### 4.3 BFT_A Proposition BL-4: its weighted version is Proposition W (found; CONFIRMED)
BFT_A §13.9 **Proposition W**: "For 0 ≤ m < m′ < m_*′ there is G_D(m) … with ||x(B_k)||_{inv,m} ≤ G_D(m)||B_k||_{D,m},
uniformly in k ≥ 1, T ≥ 1, X_0", **G_D(m) := e^{20m}·G_D♭** (BL-4's G_D with C_f → M_fS(μ), C_R → MS(μ)); its proof also gives
**weighted BL-C: [H]^∞_{α,m} ≤ e^{8m}(C_BLC[H]_{α,m} + 2·8^α||H||_{∞,m})**. Status: CONFIRMED given the package (REVIEW_BFT_A_S3
l.299). I re-read the proof: the only non-local steps are the two kernels B_k ↦ r_{k−1}, B_k ↦ f_0 (LP Thm 6.8 (a), Lemma
6.7); every other step (J^c_0 as a convex combination of r_{k−1} at distances ≤ 5; LES on Q_n(z_B) within distance 2; BL-C's
boxes within 8; 𝒜 within 4) reads within bounded coarse distance — **CONFIRMED** (structure re-derived, constants quoted).
BL-4's own "*Remark (weights m > 0, ARGUED)*" (BFT_A §8.5) is the statement of Proposition W and is superseded by it.
**So Theorem CC-FUN (b)'s second route "BL-4 + BL-C" has the weighted form "Proposition W + weighted BL-C", for every
0 ≤ m < m_*′.**

### 4.4 Lemma FT (iv) (BFT_B §29.2): "each funnel term costs at most e^{2m}" — CONFIRMED in ℓ¹, with a convention caveat
cm55 L4 enumerates the read set of h_l^Tψ_l (h_l^T at a block-interior level-l link reads ψ_l at its level-(l+1) block; ψ_l
reads d*j_{l′} at the level-l′ site whose level-0 avatar is that block's root): the ℓ¹ radius is **2(ρ_{l+1} − ρ_0) < 2**
(16/9 at k = 2, 52/27 at k = 3 for l = k − 1). So FT (iv)'s e^{2m}, which REVIEW_BFT_B_S9_S10 S9-6 CONFIRMED by an ℓ^∞-style
count ("within one coarse unit and … one more"), is **right in the ℓ¹ metric the weights use — but only because roots are
block centres**: with corner roots the radius is 8/3 (control C4). COFUN_CC §6.2's "FT (iv) prices the funnel at e^{2m}":
CONFIRMED with that precision.

---

## 5. T5 — Theorem GU at m > 0 without DX_m, DB_m (new)

**Why this is the crux.** Theorem COF's G-slots at levels ≥ 1 are bounded by Theorem GU (BFT_B §35.5 (a)), whose sup part
pairs d*G_l/(6 sup|G_l|) ∈ 𝔉_l with Y^p_l through Theorem Y's carrier dual 𝒬_B (BFT_A §28.7 step 2). Theorem Y's bootstrap
bounds the Z′-term of 𝒬_B by Lemma DB, whose proof (§18.5 Steps 3-4) pairs the carrier current's smooth parts against the
**global Coulomb representative** of Z′_l, with |∇A(b)| ≤ ρ_l²C_aΦ(1 + D)^{−5} (LRL (a), BFT_A §18.2 (i)) — a POLYNOMIAL
tail. That is why BFT_A §28.13 lists "the weighted CO-0R, CO-B and GU sup parts: conditional on DX_m and DB_m", and BFT_B
§30 does not claim (H-inv+)_m. **For divergence-form test currents none of this is needed**: ⟨d*G_l, Y_l⟩ = ⟨G_l, dY_l⟩ is a
pairing with a CURVATURE, which is gauge invariant and, for Z′, exponentially decaying by Theorem W.

> **Lemma K (weighted curvature-ℓ¹ dual of the plaquette response). PROVEN-HERE as an implication.**
> For 0 ≤ m ≤ m_Y and 0 ≤ l ≤ k − 1 put **K_l(m) := sup_p Σ_{q′}e^{m·dist(q′, p)}|dY^p_l(q′)|** (p over level-0 plaquettes,
> q′ over all level-l plaquettes; dY^p_l is the same at every minimiser Y^p of E_src with the single source G_0 = δ_p,
> B_k = 0). Then, uniformly in k ≥ 1 and T ≥ 1,
>   **K_l(m) ≤ C_YK(m)·(k − l + 1)²·L^{−2l}**,
>   C_YK(m) := max{ (72/5)C_EX(c) + 12e^{4m′}S(μ)C_Z(c),  12C_EX(c) + 6e^{4m′}S(μ)G_D(m′)C_βe^{128m′L^c} },  μ := m′ − m ≥ m′/2.
>
> *Inputs, status quoted:* Lemma LD (exact decomposition) and Lemma PC: CONFIRMED (REVIEW_BFT_A_S5 l.22); Lemma EX, carrier
> part: CONFIRMED-WITH-FIX (S5 l.23; U3 is a dropped L^i absorbed in C_g); Theorem Y steps 2-4 and Case B (the constants C_β,
> C_Z(c), the β → β_str gauge change): CONFIRMED (S5 l.139-163); Lemma CS: CONFIRMED (S6 l.21); Theorem W: CONFIRMED (S3
> l.309); Lemma BW: CONFIRMED (S6 l.295).
>
> *Proof.* Composite gauge directions x_j ↦ x_j + d ev^{(j)}λ change no curvature dx_j (dd = 0). Fix p; X_0 := its coarse cell.
> **Case A (T ≥ 8L^c; r := L^{k+c}).**
> *Step 1 (exact).* Lemma LD and Theorem Y step 2: modulo composite gauge, Y^p = g + Z′ + Σ_qG_e(q)Y^q with g_j := Q^{(0→j)}g_0,
> g_0 = d*(χω^p), Z′ the minimiser with datum β_str and the residual sources s_i, G_e = 𝒫e. Hence, for every level-l plaquette q′,
>   **dY^p_l(q′) = dg_l(q′) + dZ′_l(q′) + Σ_qG_e(q)dY^q_l(q′).**   (K1)
> *Step 2 (explicit part).* For a level-l 2-form G with sup|G| ≤ 1, R := d*G/6 ∈ 𝔉_l (Lemma CS) and ⟨R, Q^{(0→l)}g_0⟩ =
> ⟨G, dg_l⟩/6. Lemma EX: L^{2l}|⟨R, Q^{(0→l)}g_0⟩| ≤ C_EX(c)(k − l + 1)². With G := sgn(dg_l):
> Σ_{q′}|dg_l(q′)| ≤ 6C_EX(c)(k − l + 1)²L^{−2l}. Support: dg_l = 𝒬^{(0→l)}dg_0 (d∘Q_i = 𝒬_i∘d, LINEAR_PACKAGE Lemma 2.2 (i),
> iterated); (𝒬^{(0→l)}H)^c(q′) is a probability average of H^c over level-0 plaquettes with base points in q′ + [0, 3ρ_l)⁴
> (BL-2 (d)); dg_0 vanishes outside the fine ℓ^∞ ball of radius r + 2 about p. So dg_l(q′) ≠ 0 forces coarse ℓ^∞ distance
> ≤ 3ρ_l + L^c + 2/n < L^c + 2, i.e. dist(q′, p) ≤ 4(L^c + 4). For m ≤ m_Y ≤ ln 2/(16L^c), L^c ≥ 260:
> e^{m·dist} ≤ 2^{(L^c+4)/(4L^c)} ≤ 6/5 (cm55 N3). So E_l(m) := sup_pΣ_{q′}e^{m·dist(q′,p)}|dg_l(q′)| ≤ (36/5)C_EX(c)(k − l + 1)²L^{−2l}.
> *Step 3 (the screened part Z′).* Theorem Y step 4 (Theorem W at weight m′, centre X_0): ||Z′||_{inv,m′} ≤ C_Z(c)n^{−2}, in
> particular |f_l(Z′)(q′)| ≤ C_Z(c)n^{−2}e^{−m′dist(q′, X_0)} for every level-l plaquette q′ (f_l = L^{2(k−l)}dZ′_l). With
> dist(q′, p) ≤ dist(q′, X_0) + 4, dist(q′, X_0) ≥ dist(Y, X_0) − 4 for q′ positioned in the coarse cell Y, 6L^{4(k−l)} level-l
> plaquettes per cell, and Σ_Ye^{−μ·dist(Y,X_0)} ≤ S(μ):
>   Z_l(m) := Σ_{q′}e^{m·dist(q′,p)}|dZ′_l(q′)| ≤ L^{−2(k−l)}·C_Z(c)n^{−2}·e^{4m}·6L^{4(k−l)}e^{4μ}S(μ) = **6e^{4m′}S(μ)C_Z(c)L^{−2l}**
>   (L-powers: −2(k − l) − 2k + 4(k − l) = −2l; the fine/coarse factors cancel exactly).
> *Step 4 (bootstrap).* By dist(q′, p) ≤ dist(q′, q) + dist(q, p) and Lemma BW (Σ_q|G_e(q)|e^{m·dist(q,p)} ≤ ¼e^{4.2mL^c} ≤ ½ for
> m ≤ ln 2/(4.2L^c) ⊇ [0, m_Y]):
>   Σ_{q′}e^{m·dist(q′,p)}|Σ_qG_e(q)dY^q_l(q′)| ≤ Σ_q|G_e(q)|e^{m·dist(q,p)}·Σ_{q′}e^{m·dist(q′,q)}|dY^q_l(q′)| ≤ ½K_l(m).
> *Step 5 (closing).* For fixed (k, T) every sum is finite, so K_l(m) < ∞. (K1) gives K_l(m) ≤ E_l(m) + Z_l(m) + ½K_l(m), hence
> K_l(m) ≤ 2(E_l + Z_l) ≤ [(72/5)C_EX(c)(k − l + 1)² + 12e^{4m′}S(μ)C_Z(c)]L^{−2l}.
> **Case B (T < 8L^c; r = ∞).** Theorem Y Case B: G′ = 0, e = 0, Y^p = g + Z (mod gauge), g_0 = y^p = d*ω^p, Z the data response
> with datum β_str = −Q_str^{(0→k)}y^p, ||β_str||_{D,m′} ≤ C_βe^{128m′L^c}n^{−2}; no bootstrap. Lemma EX (r = ∞) + Lemma CS as in
> Step 2 give Σ|dg_l| ≤ 6C_EX(c)(k − l + 1)²L^{−2l}, and every weight is ≤ e^{m·diam} with coarse ℓ¹ diameter ≤ 2T < 16L^c,
> so ≤ e^{16mL^c} ≤ 2. Proposition W at m′ and Step 3's count: Σe^{m·dist}|dZ_l| ≤ 6e^{4m′}S(μ)G_D(m′)C_βe^{128m′L^c}L^{−2l}. ∎
>
> *Remarks.* (1) No Coulomb representative, no Lemma DX, no Lemma DB, no slice: every pairing is with a curvature. (2) At
> m = 0 Lemma K is the divergence-form special case of Theorem Y's 𝒬_B (L^{2l}Σ|dY^p_l| ≤ 6(k − l + 1)²𝒬_B(Y^p) by Lemma CS);
> it is not stronger there. What is new is that its WEIGHTED form closes with inputs that are already CONFIRMED.
> (3) The (k − l + 1)² is inherited from Lemma EX's crude carrier count; for G = sgn(dg_l) the shell count gives (k − l + c)
> (one O(L^{−2l}) per scale), but nothing below needs the improvement.

> **Theorem GU_m ((G♯-up) with exponential weights). PROVEN-HERE as an implication** (inputs: Lemma K; Lemmas DUAL, TOPD,
> TS; Proposition W; Lemma WT (CONFIRMED REVIEW_BFT_A_S7 l.289, explicitly "for … GU"); Theorem GU steps 3-5 (CONFIRMED
> REVIEW_BFT_A_S6 l.181)). Let 0 < α < 1, 1 ≤ l ≤ k − 1, G_l a level-l 2-form, source d*G_l only, B_k = 0. Uniformly in k ≥ 1,
> T ≥ 1 and the weight centre X_0:
> (i) for 0 ≤ m ≤ m_Y: **||f_0||_{∞,m} ≤ C_YK(m)(k − l + 1)²||G^c_l||_{∞,m}**;
> (ii) for 0 ≤ m < m′ < m_*′: **||r_{k−1}||_{∞,m} ≤ 6e^{4μ}S(μ)G_D(m′)κ_−^{−1}||G^c_l||_{∞,m}**, and every L^{k−1−i}||r^c_i||_{∞,m} is
>   bounded by GU step 3's bound with weighted sups and a factor e^{15m};
> (iii) for 0 ≤ m ≤ m_Y: **||x(G_l)||_{inv,m} ≤ C_GU(m)(k − l + 1)²L^{α(k−l)}||G^c_l||_{∞,m}**;
> hence for 0 < α < θ and G = (G_1, …, G_{k−1}): ||x(G)||_{inv,m} ≤ C_GU(m)Σ_{t≥1}(t + 1)²L^{−(θ−α)t}·||G||^{sup}_{Y,m}.
>
> *Proof.* (i) GU step 1 (Lemma DUAL with j = d*G_l; d*d* = 0): f_0(p) = n²⟨d*G_l, Y^p_l⟩ = n²⟨G_l, dY^p_l⟩. With
> dist(p, X_0) ≤ dist(p, q) + dist(q, X_0) and |G_l(q)| = L^{−2(k−l)}|G^c_l(q)| ≤ L^{−2(k−l)}e^{−m·dist(q,X_0)}||G^c_l||_{∞,m}:
>   w(p)|f_0(p)| ≤ n²Σ_qw(q)|G_l(q)|e^{m·dist(q,p)}|dY^p_l(q)| ≤ n²L^{−2(k−l)}||G^c_l||_{∞,m}K_l(m) ≤ C_YK(m)(k − l + 1)²||G^c_l||_{∞,m},
> since n²L^{−2(k−l)}L^{−2l} = 1. (ii) Lemma TOPD with the single source G_l and Lemma TS: r_{k−1}(b) = ⟨G_l, dy_l⟩, y the
> source-free minimiser with datum δ_b/κ_{k−1}. Proposition W at m′ centred at b's base site X_b (||δ_b/κ_{k−1}||_{D,m′} =
> κ_{k−1}^{−1}): |f_l(y)(q)| ≤ G_D(m′)κ_−^{−1}e^{−m′dist(q,X_b)}. So w(X_b)|r_{k−1}(b)| ≤ Σ_qw(q)|G_l(q)|e^{m·dist(q,X_b)}
> L^{−2(k−l)}|f_l(y)(q)| ≤ L^{−4(k−l)}||G^c_l||_{∞,m}G_D(m′)κ_−^{−1}·6L^{4(k−l)}e^{4μ}S(μ). The lower residuals: GU step 3's three
> Euler-Lagrange relations (κ_ir_i = κ_{k−1}(Q_str^{(i+1→k)})^Tr_{k−1}, i ≥ l; κ_{l−1}r_{l−1} = κ_lQ_l^Tr_l − d*G_l; κ_ir_i =
> (Q_str^{(i+1→l)})^Tκ_{l−1}r_{l−1}, i < l − 1; all inputs co-closed) each read within dist < 5 (cm55 L3; d*G_l within ρ_l), so
> each costs ≤ e^{5m}. This part uses no bootstrap (it is LINEAR_PACKAGE Theorem 6.8 (a)-(b)'s source part for one level).
> (iii) GU steps 4-5 are local; Lemma WT: [f_0]_{α,m} ≤ e^{8m}[(C_α + 1)L^{α(k−l)}(||f_0||_{∞,m} + 96||G^c_l||_{∞,m}) +
> 16C_ακ_+||r_{k−1}||_{∞,m}], and the upper levels likewise; insert (i), (ii). The level sum is GU's own: Σ_{l≥1}(k − l + 1)²
> L^{α(k−l)}ω_l^{−1} = Σ_{t≥1}(t + 1)²L^{−(θ−α)t} < ∞ iff α < θ. ∎

> **Corollary LIN0_m (by-product; PROVEN as an implication).** For level-wise co-closed plain currents, 0 < α < θ < 1,
> 0 ≤ m ≤ m_Y, uniformly in k, T, X_0: ||x||_{inv,m} ≤ C(m)(||B_k||_{D,m} + ||s||_{R,m} + ||G_0||^L_m + ||G||^{sup}_{Y,m} +
> ||j^c_0||_{∞,m} + ||j||_{Pc,m}). *Proof.* BFT_A Corollary LIN0's superposition with each member weighted: data + (R)
> Theorem W; (G) at level 0 and (P0) W0_m; (G) at levels ≥ 1 GU_m; (Pl-c) BL-6 (a)'s exact push-down (straight transposes on
> co-closed currents, read radius < 5: e^{5m}) to (R) + (P0). ∎ **Not included:** rough currents in the F3 weight (Corollary
> G♯R needs CO-0R_m, i.e. DX_m) and non-divergence-form carrier currents (CO-B_m, DB_m). This is the weighted gauge-invariant
> (H-inv) on BL-7's pair; BFT_B §30's sentence "(H-inv+)_m for m > 0 is NOT claimed here" was right when written (GU_m
> OPEN); its GU member is now supplied, its (Res-Hölder)_m member is Theorem RHT_m (CONFIRMED there); I do not assemble
> (H-inv+)_m here (lane B's Corollary RH-inv would have to be re-read with weights).

---

## 6. T6 — Theorem COF at m > 0

> **Theorem COF_m ((CO-fun) under (CC-0), exponentially weighted). PROVEN-HERE as an implication; unreviewed.**
> At the trivial background, 0 < α < θ < 1 and **0 ≤ m ≤ m_Y**: there are C_fun,sup(m), C_fun(m) < ∞, independent of k ≥ 1,
> T ≥ 1 and the weight centre X_0, such that for every Setting LIN^cc source S in the (P0) + (Pl-c) + (G) + (R) classes that
> satisfies (CC-0) (a non-co-closed top residual slot first moved into j_{k−1} by X-T7's reclassification, which costs
> π_{k−1,m}(Q^Ts_{k−1}) ≤ e^{(10/3)m}(1 + 2dL³w_h)L^{−θ}||s||_{R,m}, cm55 L2):
>   **||f_0||_{∞,m} ≤ C_fun,sup(m)·N_m(S),   ||f_0||_{∞,m} + [f_0]^∞_{α,m} ≤ C_fun(m)·(N_m(S) + κ_+||r^c_{k−1}||_{∞,m}).**
> Both also hold with N_{Σ,m}(S). At m = 0 this is BFT_B §35.5's Theorem COF (with the Lipschitz G_0 norm, equivalent by BL-C).

*Proof* (BFT_B §35.5's four steps, each with its weighted input; status of each input quoted). By Lemma SPLIT (exact; with the
top slot repaired) f_0 = f_0[S^G] + f_0[S^s] + f_0[S^j], and S^j satisfies (CC-0).

**(a) G-slots.** Level 0: **Theorem W0_m** (BFT_A §33.12; CONFIRMED, REVIEW_BFT_A_S7 l.314, 0 ≤ m ≤ m_Y):
||x(G_0)||_{inv,m} ≤ C_W0(m)||G_0||^L_m. Levels ≥ 1: **Theorem GU_m (iii)** (§5). Total ≤ C(m)(||G_0||^L_m + ||G||^{sup}_{Y,m}).

**(b) s-slots.** **Theorem W** (BFT_A §13.10; CONFIRMED, REVIEW_BFT_A_S3 l.309; α ≤ θ, 0 ≤ m < m′ < m_*′):
||x(s)||_{inv,m} ≤ G_R(m)||s||_{R,m}.

**(c) Plain currents, sup half.** BFT_B §35.5 (c)'s exact identity, written with level indices i:
  f_0[S^j](p) = n²[⟨C(j), Y^p_0⟩ − Σ_{0≤i≤k−2}⟨T_i(j), r_i(Y^p)⟩],  T_i(j) := Σ_{l>i}(Q^{(i+1→l)})^Tj_l = Σ_{l>i}(Q_str^{(i+1→l)})^Tĵ_l,
with C(j) = Σ_l(Q_str^{(0→l)})^Tĵ_l co-closed (Lemma DF-cc (i)-(iii) under (CC-0); exact, weight-free).
- *Weighted sizes.* Lemma FT (ii) + (iv) (§4.4): π_{l,m}(h_l^Tψ_l) ≤ e^{2m}·2dΣ_{l′≤l}L^{−3(l−l′)}π_{l′,m}(j_{l′}); so COF-size's
  steps 2-3 give max_lπ_{l,m}(ĵ_l) ≤ Σ_lπ_{l,m}(ĵ_l) ≤ e^{2m}C_size(||j^c_0||_{∞,m} + ||j||_{Pc,m}) (or ≤ e^{2m}(121/13)|j|_{Σ,m}),
  and COF-size step 1 (the straight push-down transpose is a coarse-unit contraction, BL-2 (c); read radius < 5, cm55 L3)
  gives π_{0,m}(C(j)) ≤ e^{5m}Σ_lπ_{l,m}(ĵ_l).
- *First term.* C(j) co-closed ⇒ ⟨C(j), Y^p_0⟩ = ⟨C(j), Y^p_0 + dλ⟩ for every λ; with w(p) ≤ w(b)e^{m·dist(b,p)},
  w(p)|⟨C(j), Y^p_0 + dλ⟩| ≤ n^{−3}π_{0,m}(C(j))·Σ_be^{m·dist(b,p)}|Y^p_0(b) + dλ(b)|; minimising over λ,
  ≤ n^{−3}π_{0,m}(C(j))·𝒩_m(Y^p; p) ≤ n^{−2}C_YN(m)π_{0,m}(C(j)) by **Theorem Y_m, 𝒩_m part** (BFT_A §28.13; CONFIRMED,
  REVIEW_BFT_A_S6 l.301, 0 ≤ m ≤ m_Y). Times n²: ≤ C_YN(m)π_{0,m}(C(j)).
- *Residual terms (no bootstrap).* TOPD with G_0 = δ_p: r_{k−1}(Y^p)(b) = n^{−2}f_0(Y^{(b)})(p); Proposition W at m′ centred at
  b: |f_0(Y^{(b)})(p)| ≤ G_D(m′)κ_−^{−1}e^{−m′dist(p,X_b)}; so Σ_be^{m·dist(b,p)}|r_{k−1}(Y^p)(b)| ≤ 4e^{4μ}n^{−2}G_D(m′)S(μ)/κ_−.
  Y^p has its source at level 0, so κ_ir_i(Y^p) = κ_{k−1}(Q_str^{(i+1→k)})^Tr_{k−1}(Y^p) with ||Q_str^Tu||_1 ≤ L||u||_1 per step and
  composite read radius < 5: Σ_be^{m·dist(b,p)}|r_i(Y^p)(b)| ≤ κ̂e^{5m}L^{k−1−i}·4e^{4μ}n^{−2}G_D(m′)S(μ)/κ_−. With
  sup_bw(b)|T_i(b)| ≤ e^{5m}Σ_{l>i}L^{−3(l−i−1)}L^{−3(k−l)}π_{l,m}(ĵ_l) and i = l − 1 − a (L^{−3a}L^{−3(k−l)}L^{k−l+a} =
  L^{−2a}L^{−2(k−l)}, exactly BFT_B §35.5 (c)'s exchange):
  Σ_iw(p)n²|⟨T_i, r_i(Y^p)⟩| ≤ e^{10m+4μ}A(μ)(1 − L^{−2})^{−2}max_lπ_{l,m}(ĵ_l),  A(μ) := 4κ̂G_D(m′)S(μ)/κ_−.
- So **||f_0[S^j]||_{∞,m} ≤ e^{2m}[e^{5m}C_YN(m) + e^{10m+4μ}A(μ)(1 − L^{−2})^{−2}]C_size(||j^c_0||_{∞,m} + ||j||_{Pc,m})**.

**(d) Plain currents, Hölder half.** The j-only problem's level-0 equation is d*dx_0 = h, h := C(j) − (Q_str^{(0→k)})^Tρ_{k−1}
(Lemma RT-cc (d) with G = 0, rewritten by DF-cc (ii) under (CC-0); ρ_{k−1} = κ_{k−1}r_{k−1}). BFT_B §35.5 (d) runs W0 step 4,
i.e. LES-div **+ Lemma LE** — and **Lemma LE cannot be weighted** (BFT_A §28.13: "a weighted LE is false for the global
Coulomb potential"; CONFIRMED as ARGUED by REVIEW_BFT_A_S6). Replace it by **Theorem W0-loc** (BFT_A §33.9; CONFIRMED,
REVIEW_BFT_A_S7): its proof uses only that F := dx_0 is closed, that d*F = d*G_0 + h on the periodic lift, and LES-dd with
the LOCAL sup of h — nothing about h's co-closedness or about j_0 being the only source (Lemma W0-use's reading of step 4,
which REVIEW55_BFTB and Codex C2 accepted at m = 0, applies verbatim). With G_0 = 0: ρ_c^{−α}Osc_2(f_0; B) ≤
C_α′[sup_{Q(z)}|f_0| + sup_{Q(z)}n³|h|], and n³|h| ≤ |C(j)^c| + κ_+|r_{k−1}| locally ((Q_str^{(0→k)})^T reads r_{k−1} on ≤ 2
coarse links per component). **Lemma WT** (e^{8m}) and weighted BL-C:
  [f_0[S^j]]^∞_{α,m} ≤ C(m)(||f_0[S^j]||_{∞,m} + π_{0,m}(C(j)) + κ_+||r^c_{k−1}[S^j]||_{∞,m}).
The j-only top residual differs from S's by those of the G- and s-slot responses (COFUN_CC §4.1 precision (2)), which W0_m
step 2, GU_m (ii) and Theorem W bound by N_m(S). Collect (a)-(d). ∎

**The m-range of each step.** (a) needs m ≤ m_Y (W0_m; GU_m (i) through Lemma K); (c)'s first term needs m ≤ m_Y (𝒩_m);
(b), (c)'s residual terms and (d)'s inputs hold for every m < m_*′. So **m_Y binds exactly through the YH/Y bootstrap
(Lemma BW), in three places: 𝒬^L_{H,m} (inside W0_m), 𝒩_m, and Lemma K.**

---

## 7. Theorem CC-FUN (b) at m > 0, the top residual, and (NC-Γ)_cc at m > 0

> **Theorem CC-FUN_m. PROVEN-HERE as an implication; unreviewed.** At the trivial background, 0 < α < θ < 1, 0 ≤ m ≤ m_Y,
> with constants independent of k ≥ 1, T ≥ 1, X_0, for every Setting LIN^cc source S with B_k = 0 in the classes:
> (a) ||f_0(S)||_{∞,m} ≤ C_sup(m)·N_m(S);
> (b) **||f_0(S)||_{∞,m} + [f_0(S)]^∞_{α,m} ≤ C_H(m)·(N_m(S) + κ_+||r^c_{k−1}(S)||_{∞,m})** — Theorem CC-FUN (b) with weights;
> (c) with Lemma TOP-cc_m: ||f_0(S)||_{∞,m} + [f_0(S)]^∞_{α,m} + κ_+||r^c_{k−1}(S)||_{∞,m} ≤ C_H′(m)·N_m(S).
> All three also with N_{Σ,m}.
>
> *Proof.* Lemma DEC_m: f_0(S) = f_0(S′) + f_0(y), y the source-free minimiser with datum b/κ_{k−1}, ||b||_{∞,m} ≤ e^{4m}K_θN_m(S).
> (a) COF_m's sup half on S′ ((CC-0), no top slot): ≤ C_fun,sup(m)(1 + L^θe^{(22/3)m}(1 + 2dL³w_h)K_θ)N_m(S); Proposition W:
> ||f_0(y)||_{∞,m} ≤ G_D(m)e^{4m}K_θN_m(S)/κ_−. (b) COF_m on S′, and ||r^c_{k−1}(S′)||_{∞,m} ≤ ||r^c_{k−1}(S)||_{∞,m} +
> (G_D(m) + 1)e^{4m}K_θN_m(S)/κ_− (DEC (v), Proposition W); the datum: ||f_0(y)||_{∞,m} + [f_0(y)]^∞_{α,m} ≤
> (1 + e^{8m}(C_BLC + 2·8^α))G_D(m)e^{4m}K_θN_m(S)/κ_− (Proposition W + weighted BL-C). Seminorms are subadditive.
> (c) Substitute Lemma TOP-cc_m. ∎

> **Lemma TOP-cc_m. PROVEN-HERE as an implication; unreviewed.** At the trivial background, 0 < α < θ < 1, and for every
> **0 ≤ m < m_*′** (constants depending on μ = m′ − m, any m′ ∈ (m, m_*′)): ||r^c_{k−1}(S)||_{∞,m} ≤ C^{cc}_top(m)·N_m(S) (and
> ≤ C·N_{Σ,m}(S)), uniformly in k, T, X_0 and the gauge fixing.
>
> *Proof.* COFUN_CC §5 (CONFIRMED at m = 0 by CODEX_REVIEW_TOPCC, "Lemma TOP-cc | CONFIRMED") with each step weighted.
> DEC (v): r_{k−1}(S) = r_{k−1}(S′) + r_{k−1}(y) + b/κ_{k−1}; the last two ≤ (G_D(m) + 1)e^{4m}K_θN_m(S)/κ_−.
> (1) S′^G: level 0 — W0_m **step 2** (BFT_A §33.12), which uses only Proposition W and Corollary FP at m′, hence holds for
> every m < m′ < m_*′ (W0_m is stated on [0, m_Y] because its steps 1 and 3 use the bootstrap; step 2 does not):
> ||r_{k−1}||_{∞,m} ≤ C_top(m)||G^c_0||_{∞,m}; levels ≥ 1 — GU_m (ii), summed against ω_l: Σ_lL^{−θ(k−l)} ≤ (L^θ − 1)^{−1}.
> (2) S′^s: Theorem W (its ||·||_{inv,m} contains L^0||r^c_{k−1}||_{∞,m}): ≤ G_R(m)||s||_{R,m}.
> (3) S′^j: TOPD + TS: r_{k−1}(x(S′^j))(b) = ⟨C(j′), Y^{(b)}_0⟩ − Σ_i⟨T_i(j′), r_i(y^{(b)})⟩. First term: w(X_b)|⟨C(j′), Y^{(b)}_0 + dλ⟩|
> ≤ n^{−3}π_{0,m}(C(j′))·𝒩_m(Y^{(b)}; b) and, by W0_m step 2's Corollary-FP bound (T ≥ 3; T ≤ 2 by the lift of BFT_A 28.4),
> Σ_ze^{m·dist(z,b)}|(PY^{(b)})_0(z)| ≤ 4n³e^{20m′}(1083G_D(m′) + 40)S(μ)/κ_−: the term is ≤ 4e^{20m′}(1083G_D(m′) + 40)S(μ)κ_−^{−1}
> π_{0,m}(C(j′)). Residual terms: Proposition W at m′ centred at b: Σ_{b′}e^{m·dist(b′,b)}|r_{k−1}(y^{(b)})(b′)| ≤ 4e^{4μ}G_D(m′)S(μ)/κ_−,
> κ_ir_i = κ_{k−1}(Q_str^{(i+1→k)})^Tr_{k−1}, and the sum of §6 (c) without its n²: ≤ e^{10m+4μ}A(μ)(1 − L^{−2})^{−2}max_lπ_{l,m}(ĵ′_l).
> Then §6 (c)'s weighted sizes and Lemma DEC_m (iii). Γ-uniformity: r_{k−1} is a gauge-invariant output (Lemma FG (iii)). ∎
> **No step uses Y^p, Lemma BW or any bootstrap — so the top residual of every (cc) response decays at every rate below
> m_*′**, not only below m_Y.

> **Theorem CC-INV_m ((NC-Γ)_cc with weights; gauge-invariant half of the weighted clause (b) at the trivial background).
> PROVEN-HERE as an implication; unreviewed.** For 0 < α < θ < 1 and 0 ≤ m ≤ m_Y, for every Setting LIN^cc source with B_k = 0
> in the classes: **||x||_{inv,m} ≤ C_inv(m)·N_m(S)** (and ≤ C·N_{Σ,m}(S)), with ||f_0||_{∞,m} + [f_0]^∞_{α,m} ≤ C_H′(m)N_m(S),
> uniformly in k, T, X_0 and the gauge fixing Γ. **Its residual half (every L^{k−1−j}||r^c_j||_{∞,m}) holds for 0 ≤ m < m_*′.**
>
> *Components.* f_0 pair: CC-FUN_m (c). Top residual: TOP-cc_m. Lower residuals: Lemma RT-cc (c)'s transport formula, every
> operator in it a straight composite transpose, a d*, or a funnel (read radii < 5, cm55 L3; e^{2m}, §4.4) — this is BFT_B
> **Theorem RHT_m-cc** (§29.5; CONFIRMED-WITH-FIX, REVIEW_BFT_B_S9_S10 S9-8: c_w = 12 suffices), giving COFUN_CC §6.1's
> (a)-bound with weighted norms and a factor ≤ e^{14m}. Tower f_j (j ≥ 1): f_j = 𝒜^{(0→j)}f_0 − R_j is local (Lemma WT; W0_m
> step 4: e^{8m}); COFUN_CC §6.1's summability is unchanged. ∎

---

## 8. T4 — uniformity in k and T, and how small m must be

**Uniformity.** Every result of §4-§7 holds with constants independent of k ≥ 1, of the torus side T ≥ 1 and of the weight
centre X_0 (and of the gauge fixing for the gauge-invariant outputs). T enters nowhere: Lemma K splits T ≥ 8L^c (bootstrap)
from T < 8L^c (no bootstrap, finite-torus weight ≤ e^{16mL^c} ≤ 2); Corollary FP's T ≤ 2 case is BFT_A 28.4's periodic lift;
the sums over coarse cells are bounded by S(μ) on every torus. k enters only through (k − l + 1)² factors absorbed by
ω_l = L^{θ(k−l)} with α < θ (GU's own mechanism) and through the rows' source norm (the level count, COFUN_CC §6.4 (I1),
(I3)), which is untouched: CC-INV_m is k-uniform in N_{Σ,m}.

**How small m must be.**
| statement | admissible m | the binding input |
|---|---|---|
| FLUX_m, DEC_m, funnel (FT (iv)), push-downs | every m ≥ 0 | (local; e^{cm}, c ≤ 5) |
| datum part (Prop W + weighted BL-C), Theorem W, TOP-cc_m, residual half of CC-INV_m (RHT_m-cc), GU_m (ii) | **0 ≤ m < m_*′** (any m′ ∈ (m, m_*′); constants ∝ S(m′ − m)) | the analyticity strip of LP Thm 4.2′ |
| Lemma K, GU_m (i)/(iii), W0_m, 𝒩_m; hence COF_m, CC-FUN_m (a)-(c), the curvature half of CC-INV_m | **0 ≤ m ≤ m_Y** | the YH/Y bootstrap (Lemma BW) |
with m_*′ = 0.0384 at L = 3, κ ≡ 1 (0.0140 at κ ∈ [¼, 4]), and **m_Y = ln 2/(16L^c) ≤ 1.666·10^{−4} per coarse unit** (cm55 N2,
N5: the m′/2 branch never binds for the tabulated strips; the true m_Y is smaller still, through the uncomputed C_j in
L^c ≥ 6952C_j). On [0, m_Y] every e^{cm} factor used is ≤ 1.0067 (cm55 N6); the constants are dominated by S(μ) with
μ ≥ m′/2 = m_*′/6 and by e^{128m′L^c} (Case B), i.e. astronomically large but fixed (as at m = 0, REVIEW_BFT_A_S5 fix U4).

**Where m_Y comes from, and what would remove it.** Lemma LD's cut-off dipole has coarse radius ≈ 1.03L^c, with L^c fixed
by the requirement Σ|G_e| ≤ ¼ (Lemma PC's crude ℓ¹ bound); weighting it costs e^{4.2mL^c}, which must stay ≤ 2. It is a
property of the PROOF of Theorem YH/Y, not of the response: the located kernel rate is ≈ 1 per coarse unit (LINEAR_PACKAGE §4
table, numerical, not proven). Two known routes would enlarge it — iterating LD on e instead of Lemma PC (REVIEW_BFT_A_S5's
optional fix 3), or a non-bootstrap proof of 𝒩* and 𝒬_H* — neither attempted here. Whether m_Y suffices downstream: BFT_A
§38.10 (ARGUED, read-only) finds no rate threshold among the consumers read, with two rows NOT DETERMINED; lane B's own
weighted clause (BFT_B §32.1 (b), (d)) is stated at exactly this rate. Quoted, not re-judged.

---

## 9. What this does to BFT-5 clause (b), and what remains (COFUN_CC §6.2's list, at m > 0)

- **(R3) weighted locality, gauge-invariant half at Z = 1: DISCHARGED as an implication on lane B's own range 0 ≤ m ≤ m_Y**
  (Theorem CC-INV_m: COF_m + CC-FUN_m + TOP-cc_m + RHT_m-cc), the residual half on 0 ≤ m < m_*′. The only new analytic step
  is Lemma K (§5); everything else is a CONFIRMED weighted input or local bookkeeping with exact radii (cm55). Unreviewed.
- **(R1) field components (the 𝔐-pair's gauge-variant part), at every m ≥ 0: OPEN, unchanged.** At m > 0 the available
  piece is BFT_A Corollary FP (potential half, data + residual-type sources, S_tent, 0 ≤ m < m_*′; CONFIRMED); its gradient
  half LR-grad is OPEN ("as stated FALSE", REVIEW_BFT_A_S3 l.330). Nothing in §5-§7 touches it. (GSHARP55's target.)
- **(R2) the background Z(V_k), incl. (CC-dec_Z): OPEN, unchanged**; with weights, the frame patching (G♯-patch^Ω) must in
  addition preserve e^{m·dist} — not examined here.
- **BFT-3 through (H-𝔊_w)_k** needs a configuration-level (slice-representative) bound; not supplied here (§2).
- **DX_m, DB_m stay OPEN, but are no longer on clause (b)'s path**: they are needed only for CO-0R_m (rough currents in the
  F3 weight) and CO-B_m (non-divergence-form carrier currents), which the (cc) curvature half no longer uses (plain currents
  go through COF's level-0 pairing, divergence-form ones through GU_m). They are **not "mechanical"** (§10, R-7).
- **(R4) the level count**: unchanged by the weights (CC-INV_m is k-uniform in N_{Σ,m}); applied to localised sources it is
  the locality statement, applied to the rows it is the m = 0 statement with Lemma TR (pending CODEX_REVIEW_TR).
**Net: clause (b) stays OPEN on (R1) and (R2) only; "Theorem COF at m > 0" moves from OPEN to PROVEN-as-an-implication
(pending a Codex review of Lemma K and of §6 (d)).**

---

## 10. Claims of others re-checked in this work (verdicts CONFIRMED / NOT-VERIFIED / REFUTED)

- **R-1 CONFIRMED.** COFUN_CC §2.2, FLUX "local (one face), so its weighted version costs only e^{O(m)}": exactly
  e^{4(1−L^{l−k})m} < e^{4m} (cm55 L1, radius attained).
- **R-2 CONFIRMED, with a convention caveat.** COFUN_CC §6.2 (R3) / BFT_B §29.2 FT (iv), "each funnel term costs at most
  e^{2m}": ℓ¹ radius 2(1 − L^{−k}) < 2 with centre roots (cm55 L4); 8/3 with corner roots (C4).
- **R-3 REFUTED (as an account of COF_m's inputs).** COFUN_CC §6.2 (R3): "The binding item is Theorem COF at m > 0 (its
  level-0 pairing needs YH_m: 𝒬_{H,m} ARGUED; DX_m, DB_m OPEN — BFT_A §28.13 heading)". Correct: 𝒬_{H,m} is Lemma QH_m,
  CONFIRMED (REVIEW_BFT_A_S7 l.302) — agreeing with CODEX_REVIEW_TOPCC's refutation of this line; and COF_m needs neither
  DX_m nor DB_m — its positive-level G-slots need GU_m, supplied by Lemma K (§5-§6).
- **R-4 CONFIRMED (in substance).** COFUN_CC §6.2 (R3): "TOP-cc_m needs W0 step 3's weighted form (BFT_A l.2614 …)": the
  weighted form is written out in W0_m step 2 (§33.12, CONFIRMED); TOP-cc_m then holds for every m < m_*′ (§7).
- **R-5 CONFIRMED.** COFUN_CC §6.2 (R3): "The (cc) step adds no new obstruction at m > 0" (FLUX_m, DEC_m, Lemma TS exact).
- **R-6 REFUTED for GU (stands for CO-0R, CO-B).** BFT_A §28.13: "𝒬_{R,m}, 𝒬_{B,m}, and with them the weighted CO-0R, CO-B
  and GU sup parts: conditional on DX_m and DB_m." Correct statement: GU's weighted sup holds on [0, m_Y] by Lemma K without
  DX_m, DB_m (Theorem GU_m (i)); for divergence-form sources the carrier pairing is a curvature pairing.
- **R-7 REFUTED (as stated).** REVIEW_BFT_A_S6 Part 5 item 2 (l.330-332): "DX_m, DB_m: mechanical, 1-2 pages. DX and DB
  pair against Φ_{m′}-weighted objects. Test currents of growth e^{md} shift m′ to m′ − m." In DX (BFT_A §18.4 Steps 3-5)
  and DB (§18.5 Steps 3-4, incl. Lemma TOP's (P1)-(P3)) the object paired with the test current is the gradient of the GLOBAL
  Coulomb representative, which LRL (a) bounds only by ρ_l²C_aΦ_{m′}(1 + d(b))^{−5} — a power tail (it comes from the far-field
  term III with Σ_yH(y) = 0, BFT_A §18.2 (i)); Σ_be^{m·d(b)}(1 + d(b))^{−5} grows like e^{mT}, so no shift m′ → m′ − m exists on
  that route. Correct statement: DX_m, DB_m are OPEN and need a representative with exponential decay AND gradient control
  (an LR-grad-type input) or a different idea; GU_m does not need them.
- **R-8 status change (no verdict).** BFT_B §30 / REVIEW_BFT_A_S7 l.320 "the weighted sups of GU, CO-0R and CO-B are quoted
  OPEN" — correct when written; GU's is now supplied (§5).
- **R-9 CONFIRMED.** BFT_A §8.5 "*Remark (weights m > 0, ARGUED)*" for BL-4: it is Proposition W (§13.9), CONFIRMED given the
  package (REVIEW_BFT_A_S3 l.299); structure re-read (§4.3).
- **R-10 CONFIRMED.** BFT_A §38.10 "m_Y ≤ 1.67·10^{−4}": ln 2/4160 = 1.66621918…·10^{−4} (cm55 N2, rigorous).
- **R-11 REFUTED (one clause) / AGREE (the rest).** CODEX_REVIEW_TOPCC §5 (l.276): "The current remaining input description
  should retain the positive-level weighted sup obligations DX_m/DB_m and the full COF assembly". For COF_m the positive-level
  obligation is GU_m's weighted sup, which needs neither DX_m nor DB_m (Lemma K). I agree with the rest of that paragraph
  (the 𝒬_{H,m} line is stale; the weighted COF assembly had not been supplied).
- **R-12 CONFIRMED (algebra) / AGREE.** CODEX_REVIEW_GAPZ F5's template and its list of missing work (§3 addresses each item).
- **R-13 NOT-VERIFIED.** BFT_B Lemma BB-MCT, B3-F3 ("||𝓛^{-1}|| ≳ L^{2(k-1)} … no uniform rate" in solid norms): I did not
  re-derive the lower bound; my independent scaling count (Ma(m) ≍ m·n, §3 item 2, ARGUED) agrees with its conclusion.
- **R-14 CONFIRMED.** CODEX_REVIEW_X1 §3's row-sum constant 4M((1 + e^{−m′})/(1 − e^{−m′}))⁴ = 4M coth⁴(m′/2), the m = 0 case
  of §4.2's C_D(m) = 4M coth⁴((m′ − m)/2).
- **R-15 CONFIRMED in conclusion.** REVIEW_BFT_B_S9_S10 S9-6 "(iv): the funnel reads ψ within one coarse unit and d* within one
  more, so e^{2m} ✓": the count is ℓ^∞-style; the ℓ¹ radius is 2(1 − L^{−k}) (cm55 L4) and needs centre roots (C4).
- **R-16 CONFIRMED.** COFUN_CC §2.4 / CODEX_REVIEW_TOPCC: LP Thm 4.2/4.2′ give a per-offset sup bound and no Hölder modulus in
  the offset — unchanged by weights (§4.2); the weighted Hölder half of the datum is Proposition W.

**Counts: CONFIRMED 10 (R-1, 2, 4, 5, 9, 10, 12, 14, 15, 16) · NOT-VERIFIED 1 (R-13) · REFUTED 4 (R-3, R-6, R-7, R-11);
one status change (R-8).**

---

## 11. Summary table, Codex agreement, and what changes for the lead

### 11.1 Results of this file (status words; none has a Codex review)
| result | status | m-range | k, T, X_0 |
|---|---|---|---|
| Lemma FLUX_m (e^{4(1−L^{l−k})m}) | PROVEN-HERE (elementary; cm55 L1) | all m ≥ 0 | uniform |
| Lemma DEC_m (e^{(10/3)m}; N_m(S′) ≤ (1 + L^θe^{(22/3)m}(1 + 2dL³w_h)K_θ)N_m(S)) | PROVEN-HERE (elementary; cm55 L2) | all m ≥ 0 | uniform |
| weighted LP Thm 4.2 (ii): itself + row sum, C_D(m) = 4M coth⁴((m′ − m)/2) | located (BFT_A Prop W's f_0-sup step) | m < m_*′ | uniform |
| weighted BL-4 (+ BL-C): BFT_A Proposition W (+ weighted BL-C) | located; CONFIRMED (REVIEW_BFT_A_S3) | m < m_*′ | uniform |
| **Lemma K** (weighted curvature-ℓ¹ dual of Y^p) | **PROVEN-HERE as an implication — the only new analytic step** | m ≤ m_Y | uniform |
| **Theorem GU_m** (weighted (G♯-up), no DX_m/DB_m) | PROVEN-HERE as an implication | (i), (iii): m ≤ m_Y; (ii): m < m_*′ | uniform |
| Corollary LIN0_m (by-product) | PROVEN as an implication | m ≤ m_Y | uniform |
| **Theorem COF_m** | PROVEN-HERE as an implication | m ≤ m_Y | uniform |
| **Theorem CC-FUN_m (a), (b)** | PROVEN-HERE as an implication | m ≤ m_Y | uniform |
| Lemma TOP-cc_m | PROVEN-HERE as an implication (on CODEX-CONFIRMED TOP-cc) | **m < m_*′** | uniform |
| Theorem CC-FUN_m (c), Theorem CC-INV_m | PROVEN as implications | m ≤ m_Y (residual half m < m_*′) | uniform (and in Γ) |
| Combes-Thomas template (F5) in solid norms | not available (BB-MCT B3-F3; my scaling count Ma(m) ≍ m·n, ARGUED) | — | — |

### 11.2 Codex verdicts used, and whether I agree
- **CODEX_REVIEW_GAPZ F5** (template; "the missing work is substantial: uniform a(m), fine/coarse measure factors, weighted
  source/output maps, the requested positive m, Campanato estimates, and the slice transfer"): **AGREE** with both. Each item
  is met in §3's table by a different mechanism (strip analyticity + duality), not by the template.
- **CODEX_REVIEW_TOPCC** (on disk now: 363 lines, complete): TOP-cc, CC-FUN (c), CC-INV, FLUX, DEC, H-FREE CONFIRMED at
  m = 0 — **AGREE** (used as the m = 0 anchor; I re-derived the weighted bookkeeping, not TOP-cc's m = 0 algebra in full);
  its REFUTED verdict on COFUN_CC's stale "𝒬_{H,m} ARGUED" — **AGREE**; "retain … DX_m/DB_m" — **DISAGREE** for COF_m (R-11);
  "general weighted COF … NOT-VERIFIED here" — **AGREE** as a statement about what existed before this file.
- **CODEX_REVIEW_X1 §3** (row-sum C_D) and **§8** (the banked sup theorem): **AGREE** (R-14; CC-FUN_m (a) is its weighted form).
- **CODEX_REVIEW_C2 item 1** ((C2-COF), Hölder half with the top-response term kept): **AGREE**; CC-FUN_m (b) is its weighted form.

### 11.3 What should change in PROOF.md's tally / HANDOFF's critical path (no file edited by me)
1. **Tally: no change** (105-item tally; all of this is lane-level and unreviewed).
2. **BFT-5 clause (b)'s third open item, "Theorem COF at m > 0" (SESSION25_RESULTS l.1425; COFUN_CC §6.2 (R3)):** → PROVEN as
   an implication on 0 ≤ m ≤ m_Y — **lane B's own range for the weighted clause (BFT_B §32.1 (d))** — together with the whole
   gauge-invariant half of the weighted clause at Z = 1 (Theorem CC-INV_m). Bank only after a Codex review; **review priority:
   (1) Lemma K (§5), (2) COF_m (d) (W0-loc in place of LES-div + Lemma LE for the j-only problem), (3) TOP-cc_m's range m < m_*′.**
3. **Clause (b) then stays OPEN on (R1) field components and (R2) the background transfer only** (both also at m > 0).
4. **BFT_A §28.13 / §35 and BFT_B §30:** "the weighted sup of GU conditional on DX_m, DB_m" → GU_m PROVEN as an implication
   (Lemma K). **DX_m, DB_m remain OPEN for CO-0R_m and CO-B_m only, and are NOT "mechanical"** (REVIEW_BFT_A_S6 l.323-324
   refuted, R-7): the cited route meets LRL (a)'s polynomial (1 + d)^{−5} tail.
5. **COFUN_CC §6.2 (R3)'s input list** should read: COF_m ⇐ W0_m, Theorem W, Theorem Y_m (𝒩_m), Lemma WT, W0-loc, FT (iv),
   Lemma K — all CONFIRMED except Lemma K (new).
6. **The rate:** state everywhere which range is meant — curvature half m ≤ m_Y = ln 2/(16L^c) ≤ 1.67·10^{−4} per coarse unit
   (bootstrap-limited); residual half, top residual and datum m < m_*′ (strip-limited). "0 < m < m_*′" for the (cc) curvature
   half is NOT what is proven.
7. **SMALLNESS_DAG / critical path:** the node "Theorem COF at m > 0" can be re-pointed to Lemma K + the CONFIRMED weighted
   lane-A inputs; no new k- or T-dependence enters; C_fun(m) is k-uniform in N_{Σ,m} exactly as C_fun is.

### 11.4 Line and wording corrections to this file (verified by grep after writing; content unchanged)
- §5, Theorem GU_m's input list: "Lemma WT (CONFIRMED REVIEW_BFT_A_S7 l.289 …)" → **l.295** (l.289 is Theorem W0-loc).
- §10 R-7: "REVIEW_BFT_A_S6 Part 5 item 2 (l.330-332)" → **l.323-324**.
- §2, "(it is not used on global objects such as the rows S*, whose weighted norms grow like e^{mT}; the rows use m = 0)":
  this is my reading (ARGUED), not a quoted statement; how the composite contraction (CL-0)-(CL-4) consumes the weighted pair
  is not determined here.
- PRE-STATED addendum T9: the predicted funnel radius was refuted by cm55 L4 (actual 2(1 − L^{−k}), not 5/3); FT (iv)'s e^{2m}
  holds regardless (criterion ≤ 2 passed); C4 confirms the corner-root caveat.

Files written: this file; checks/cm55_criteria.md, cm55_loc.py, cm55_num.py, cm55_loc_out.txt, cm55_num_out.txt,
cm55_loc_err.txt, cm55_num_err.txt. No git command was run; no other lane file was edited.
UTC end of writing: 2026-10-29T00:34:28Z

### 11.5 Precisions appended after a re-read of §0-§11 (00:40Z; nothing above is edited; no conclusion changes)
- §2's "REVIEW_S22 l.388-392" → the norm's weights are at **REVIEW_S22 l.396** ("exponential weights e^{±m d} are in level-k
  ancestor distance") and the claim with m_0 > 0 at **l.399**. Ancestor distance and position distance differ by < 8 (ℓ¹),
  i.e. by a factor e^{8m} ≤ 1.0014 on [0, m_Y]: immaterial.
- Lemma K Step 4 / Lemma BW: BW is written with the coarse ℓ¹ CELL distance; Lemma K weights by POSITION distance. Over
  supp G_e both are ≤ 4(1.03L^c + 1) + 8 ≤ 4.2L^c (L^c ≥ 260), so BW's bound ¼e^{4.2mL^c} ≤ ¼·2^{4.2/16} < 0.31 < ½ holds
  verbatim in the position distance.
- §6 (d), "accepted at m = 0": the precise sources are REVIEW_BFT_B_S9_S10 **S10-1** (l.452: "Lemma W0-use: CONFIRMED (checked
  against BFT_A l.2465-2494, line by line)") and REVIEW55_BFTB **Finding 22** (l.495-503: steps 1, 2, 4, 5 classified
  correctly; its "third use" is W0 step 3's TOPD bound, harmless for COF and exactly what TOP-cc handles through C(j′)
  co-closed). The W0-loc replacement of step 4 does not add a Hodge step: in W0-loc the equation is −ΔF = dd*F = d(d*G_0 + h)
  with h = d*F − d*G_0 automatically co-closed for an actual response.
- R-7, supporting the refutation: REVIEW_BFT_A_S6 itself (l.315-316), confirming the Lemma LE obstruction, writes "A localised
  exact F with nonzero moments gives ∇B ~ |z|^{-4} … That is a power, which no exponential weight can absorb." DX and DB pair
  their test currents against exactly such a ∇A (the global Coulomb representative, LRL (a)); the same review's Part 5 item 2
  ("mechanical … shift m′ to m′ − m", l.323-324) is inconsistent with its own l.315-316.
- §5 Remark (2): the inequality L^{2l}Σ|dY^p_l| ≤ 6(k − l + 1)²𝒬_B(Y^p) is the statement that sgn-test currents d*G/6 lie in
  𝔉_l; it is only used to say that Lemma K is not new at m = 0, never as an input.
UTC end of appended precisions: 2026-10-29T00:36:16Z
- §11.5's heading says "00:40Z"; the append was made at 00:36Z (stamp above). Nothing else changes.
- **cm55 provenance (stat, local EDT = UTC − 4, quoted in UTC):** cm55_criteria.md born 00:19:56Z, last modified 00:21:21Z (so
  Amendment A2's header time "00:23Z" is wrong: both amendments were written by 00:21:21Z); cm55_loc.py born 00:21:53Z;
  cm55_num.py born 00:22:22Z; cm55_num_out.txt 00:22:30Z; cm55_loc_out.txt 00:22:35-00:22:40Z. Order criteria → amendments →
  scripts → runs holds. The criteria file is deliberately not touched again, to keep its mtime as evidence.

### 11.6 The PRE-STATED refutation criteria, scored (appended last)
- **R1 (a non-local, non-exponential object paired with a weighted source): OCCURS on the m = 0 routes, and is bypassed.** It
  is exactly Lemma LE (global Coulomb potential; COF (d)'s m = 0 input) and LRL (a)'s ∇A (DX/DB, hence GU's m = 0 sup input).
  Bypassed by W0-loc/LES-dd (§6 (d)) and by Lemma K (§5). No such object remains in COF_m, CC-FUN_m, TOP-cc_m, CC-INV_m.
- **R2 (a range/coefficient bound growing with k or T): OCCURS for the literal Combes-Thomas template** (Ma(m) ≍ m·n in solid
  norms; BB-MCT's B3-F3) — hence that route is not used; does NOT occur on the duality route (all radii k-free, cm55 L1-L4).
- **R3 (an m = 0 step that is not an operator-norm statement): OCCURS** — the banked m = 0 results bound gauge-invariant outputs,
  not a configuration inverse; this is why the conjugation is done on the dual responses instead (§3).
- **R4 (a face-flux entry reading unboundedly many faces): does NOT occur** (cm55 L1: one face, radius 4(1 − L^{l−k})).
- **R5 (a needed weighted input absent): PARTLY.** Present: weighted LP 4.2 (ii) (itself + row sum) and weighted BL-4
  (Proposition W). Absent but NOT needed for the gauge-invariant half: DX_m, DB_m. Absent AND needed for the full clause (b):
  (G♯_0-field)_m (field components) and the background transfer — so the full weighted clause (b) is CONDITIONAL on those, as
  stated in §9, while its gauge-invariant half at Z = 1 is not conditional on anything beyond CONFIRMED inputs + Lemma K.
UTC final: 2026-10-29T00:36:56Z
