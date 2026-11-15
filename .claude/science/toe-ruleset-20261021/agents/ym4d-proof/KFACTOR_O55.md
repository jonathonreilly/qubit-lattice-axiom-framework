Reviewer model: claude-opus-5-5

# KFACTOR_O55 — Opus 5.5 worker, STEP 4 / target T56-4 (RTARGET.md §55): the level-count factor ≈ 25(k−1)

## PRE-STATED (written 2026-10-28T22:55:53Z UTC, before reading any source passage for this question; read so far:
the step-4 brief incl. its CORRECTION, REVIEW_BRIEF_55.md, and REVIEW55_TUNIF.md W8-W13 (the σ > 0 section). KFACTOR55.md
(Codex) NOT read and will not be read until §§1-5 and the conclusion below are written.)

Role: primary worker (not a reviewer). Rules: no git; write only this file and checks/kf55_*; exact arithmetic only.

**Targets.**
- **K1 (existence/origin).** Is a level-count factor ≈ 25(k−1) (or any factor growing with the number k of RG levels)
  present in the source text, and where does it FIRST arise (file + locating string)? Candidates named by the brief:
  BFT_A (W2)/(SPD)/GAP-1/F3/[RBA2-fix] B3/l.229/l.244/l.822-831; BFT_B COF-crit/§35.6/§36.5/NCE;
  REVIEW_BFT_B_S9_S10 COF-crit/S10-6; PROOF.md CURV-F2″.
- **K2 (what it multiplies).** Fixed-size quantity (e.g. a fixed small-field threshold, η², κ_+L²η² with η fixed) or a
  quantity shrinking with the level (g_k², g_k ~ k^{−1/2})?
- **K3 (absorption).** Is it absorbed by (a) a level-dependent small-field threshold of Balaban's kind, (b) exponential
  decay across levels, (c) asymptotic-freedom running?
- **K4 (repair).** If not absorbed: the minimal repair, aimed (per the CORRECTION) at a carrier-type input for the
  non-level-wise-co-closed part V_l of the BCH₂ rows that Theorem COF can consume; prove it if possible, else state the
  exact missing object.
- **Classification** against KF-F1 (not in the source) / KF-F2 (fixed-size: genuine non-uniformity) / KF-F3 (g_k²-size:
  marginal at d = 4).

**What would count as a refutation (of each claim I may end up making).**
- "The factor is in the source": refuted if the level sum the files bound by ≈25(k−1) is in fact geometric/convergent
  k-uniformly once the text's own estimates are used (e.g. a decay factor L^{−c(k−l)} or L^{−c(m−l)} that the
  ≈25(k−1) derivation dropped), or if the 25 is arithmetic on a misidentified symbol (systemic defect 1).
- "It first arises at X": refuted by an earlier (upstream) passage that already carries the same non-summable sum.
- "It multiplies a fixed-size quantity": refuted if the multiplied quantity carries an explicit g_k² (or other
  level-shrinking) factor in the source, or if η is level-dependent in the source.
- "Not absorbed": refuted by a source passage in which a level-dependent threshold, exponential decay across levels, or
  AF running provably controls the same sum k-uniformly.
- "θ cannot remove it" (S10-6): refuted by any θ in the admissible window giving a k-uniform bound for the same object.
- A claimed repair: refuted if its hypothesis is not met by V_l as defined in the source, or if the proof uses a
  bound the source does not establish (I will label each input PROVEN-in-source / CONFIRMED-by-me / ASSUMED).

---

## §0. Read record (appended 2026-10-28T23:24Z UTC; KFACTOR55.md still unread)

Read by grep + sed only, located by string (line numbers are as of this session; drift noted where found):
- **BFT_A.md**: §1 (l.18-47, norms; ω_l, 𝔐^∇ residual weight L^{k-1-j}‖r^c_j‖); §3.6 BA-6 (l.152-170); §3.9 table (l.224-230;
  **l.229 is the row "soft (∂ρ^{(2)})^Tr_l … ≤ 2κp_LL²L^{-3(k-l)}η² own | geometric"**; l.230 third order); §3.10 (l.232-257;
  **l.244 is the [A^T, χ]A commutator, "acts on the residual Ax"**); [RBA1-fix] GAP 1 (F3) (l.387-390); §7 (l.437-574: BL-1,
  BL-2, BL-5, BL-6 (a)-(c), BL-7); [RBA2-fix] B2-B4 (l.814-834; **B3 is l.819-824, (W2) is l.830-831**); §12 (l.869-951,
  incl. SPD's statement and the BCH₂ row definition); §13.1-13.8 (l.957-1075: BR-2, CR-1, **SPD proof l.1024-1048**, 13.7);
  [RBA3-fix] B2' (l.1329-1331); §18.5 Theorem XB and §18.6 HX (l.1499-1558); §23.10-23.12 (G♯R, CO-B, HL; l.2059-2090);
  §28.9-28.12 (FG, BOG, NC, Corollary NC incl. Remark 1 "Ω = k"; l.2546-2599); §31.1 (l.2777-2813: Lemma CD, Prop. SR).
  No occurrence of "25(k" in BFT_A (grep: none).
- **BFT_B.md**: §18.0-18.1 (l.2455-2528: N_res, Lemma RT, TC, Theorem RH statements); §19.1-19.5 (l.2591-2645, **the
  BCH₂-row size at l.2629**); §27 (l.3571-3640); §29.1-29.5 (l.3659-3750; **Corollary RHT-V's sizes l.3733-3736**);
  §31 (l.3775-3822); §34 (l.3946-4002); §35.1-35.8 (l.4003-4131; **COF-crit is §35.6, l.4106-4110**); §36.5 NCE (l.4197-4212).
- **REVIEW_BFT_B_S9_S10.md**: l.1-120 (bottom line, l.68-77 the headline), l.440-560 (S10-1..S10-8; **S10-6 l.503-542**).
- **PROOF.md**: header l.1-60; [S23]/[S22] headers l.170-215; **CURV-F2″ l.6557-6563**.
- Also: REVIEW_BFT_A_S8 l.345-380, 545-595 (S8-12/13, biggest wall); REVIEW_BFT_A_S7 l.150-162 (Lemma CD review);
  REVIEW_BFT_A_S6 l.26, l.229 (Corollary NC); REVIEW_BFT_A_S5 l.28-40, l.215; REVIEW_BFT_A_S3 l.25-27, l.154-170 (SPD);
  REVIEW_BFT_B_S6 l.39, l.113-127 (Lemma TC); NORMS.md l.267-290 (Lemma N1-4: "θ_w = d − 1 = 3 for the residuals");
  REVIEW55_TUNIF.md l.318-372 (W1-W5) and l.396-430 (W9-W11, the σ > 0 section); HANDOFF.md l.95-160 (item 5);
  KFACTOR.md first 1500 bytes only (its header, to see what it claims; not used as evidence).
- Line-number drift found: none against the brief's BFT_A l.229/l.244/l.822-831 (they match); REVIEW55_TUNIF's errata
  already note its own drift.

## §1. K1 — Is the factor there, and where does it first arise?

**Answer: the factor is in the source as the honest consequence of an a-priori input bound; it is not in the object at
critical points (§4).** Chronology in the source, by string:
1. **The input bound that causes it.** Every source bound on the BCH₂ plain row R^B_l (⟨R^B_l, u⟩ = 2κ_l⟨r_l(x), B(x_l, u_l)⟩,
   BFT_A §12.0) estimates the **residual r_l by the 𝔐^∇ weight**, |r_l| ≤ L^{-2(k-1-l)}η own (BA-6 "|r_l| ≤ L^{-2(k-1-l)}η",
   l.155; Corollary NC "σ ≤ 2κ_+L^{-2(k-1-l)}η·2p_LL^{-(k-l)}η", l.2581; BFT_B §19.4 "own |r_l| ≤ L^{-2(k-1-l)}η …
   give π_l ≤ 2C_B'κ_+L²η²", l.2629). The row is linear in r_l, so this weight fixes its coarse size at O(η²) per level.
2. **First statement of "no level decay".** BFT_A session 1 table l.229 wrote "geometric"; [RBA1-fix] GAP 1 (F3) (l.387-390)
   corrected it: "O(η²) per level in plain-current coarse units (j^c = L^{3(k-l)}j), with no level decay".
3. **First appearance of the factor (k − 1).** On the linear side, BL-6 (b) (l.538-543): currents at all levels give
   "r_{k-1}(x) = ((k − 1)c/κ_{k-1})e_μ … the ratio is ≥ (k − 1)/κ_+" (a genuine (k−1) for a NON-decaying source family).
   For the rows, **[RBA2-fix] B3 (l.819-824)**: "the level-0 images add up to Σ_l||j^c_l|| ≤ (k − 1)η²: the entire level-count
   loss sits in the level-0 image". Corollary NC Remark 1 (l.2590-2591): "O(1)η² per level: Ω = k".
4. **Where it sits on the live route.** BFT_B Corollary COF-crit (§35.6, l.4106-4110) feeds "π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²"
   (uniform in l, §29.4 l.3735) into Theorem COF, whose right side is ‖j‖_Pc = max_lL^{θ(k-l)}π_l(j_l) — the substitution
   REVIEW_BFT_B_S9_S10 S10-6 catches (l.503-542). **CONFIRMED** (re-derived: ‖V‖_Pc ≤ L^{θ(k-1)}·2C_NCC_bchκ_+L²η² is all the
   quoted inputs give).
5. **The numbers.** The sharper route (COF-size step 3, π_0(C(j)) ≤ Σ_lπ_l(ĵ_l)) gives **C_f(k − 1)·2C_NCC_bchκ_+L²η² with
   C_f = 1 + 2d/(1 − L^{-3}) = 121/13 ≈ 9.31** (kf55_1 A1). The "≈ 25(k−1)" is the CLASS route optimised over θ:
   C_C(θ)L^{θ(k-1)} ≈ C_f·L^{θ(k-1)}/(θ ln L), minimised at θ* = 1/((k−1)ln L), value C_f·e·(k−1) = 25.3009(k−1)
   (kf55_1 A1, rigorous e). **But θ* < α = ¼ for every k ≥ 5** (kf55_1 A2, rigorous ln 3: θ* > ¼ exactly for k ≤ 4), so
   the optimum lies outside Theorem COF's window 0 < α < θ < 1; inside the window the class route grows like L^{α(k-1)}
   (exponentially). So the honest pre-repair figure is the sharper route's **≈ 9.31(k−1)**, and HANDOFF item 5's "the
   sharper route leaves ≈ 25(k-1)" misattributes both the value and the route (REFUTED as stated; immaterial after §4).
6. **Not the same factor: CURV-F2″** (PROOF.md l.6557-6563) is the per-level route's first-order θ-cascade
   (θ_0 = θ·Π_j(16κ_j𝔠_∞^{(j+1)})^{-1}, hence D_g ∝ k and ε_unif = O(1/k)). It lives in the per-level route the composite
   route replaced; it shares only the symptom (growth in k). Nothing below touches it.

## §2. K2 — What does it multiply?

**A fixed-size quantity.** In every occurrence the factor multiplies the per-level a-priori row size 2C_NCC_bchκ_+L²η² (or
A_Bη², A_B := c_Bκ_+L²), where η is the 𝔐^∇ radius of the configuration. In the composite problem g is absorbed (BFT_A §1.1:
"B-NA-red's E_NA … at g = 1"), and η ≤ C_0||B_k||_D ≤ C_0ε_0 with ε_0 independent of k (BFT_A §3.9, l.211-213; BFT-5 asks for
ε_5 "not on k or T", BFT_B §27.5). There is no g_k and no level-dependent threshold anywhere in the bound. So, **as written,
the factor is KF-F2-shaped.** What §4 shows is that the per-level quantity is not actually fixed-size at critical points: it is
an upper bound that the true rows beat by L^{-(k-1-l)}.

## §3. K3 — Is it absorbed?

- **(a) Level-dependent small-field threshold (Balaban's kind): NO.** The composite problem has one threshold ε_0 in coarse units
  (§2). Even if the RG fed a level-dependent background size, Balaban's ||1 − U_p|| ≲ p(g_k)g_k (PROOF.md l.870) gives
  k·(p(g_k)g_k)² ≍ p(g_k)²/β_0, which still grows (logarithmically); ARGUED, and moot after §4.
- **(c) Asymptotic-freedom running: NO.** No coupling enters 𝔉_k (§2); κ_l ∈ [κ_-, κ_+] is a fixed range.
- **(b) Exponential decay across levels: NOT in the source text** — S10-6 is right that nothing in sessions 9-10 supplies a
  level-decay input, and every source bound on the rows is uniform in l. **But the decay is there, and it follows from lemmas
  the source has already proved and reviewed:** at a critical point the residual r_l is the transport of the top residual and of
  the sources above l (Lemma RT-cc (c)), which in own units is L^{-3(k-1-l)} (Lemma TC; NORMS Lemma N1-4's "θ_w = d − 1 = 3
  for the residuals"), one full power L^{-(k-1-l)} below the 𝔐^∇ weight used in §1 item 1. The row is linear in r_l. §4 writes
  this out. So: **absorbed by exponential decay across levels — decay in the distance k − 1 − l to the top, supplied by
  criticality (transport), not by SPD-type carrier decay, not by a threshold, not by AF.**

## §4. K4 — The repair at the critical point: Lemma TR (PROVEN here, as an implication of reviewed source lemmas)

**Notation.** BFT_A §1, §7.1, §12.0: d = 4, L ≥ 3 odd, κ_l ∈ [κ_-, κ_+], κ̂ := κ_+/κ_-; coarse units r^c_i := L^{k-1-i}r_i
(level-(i+1) 1-form), π_l(j) := L^{3(k-l)}sup_own|j|; 𝔐 := 𝔐^∇ (BFT_A §1.4), whose residual term is L^{k-1-j}||r^c_j||_∞.
Trivial background on 𝒞_glob, weight m = 0. For a level index l write **m := k − 1 − l** (distance to the top step).
Constants, all from the source at second order (third order at the source's own ARGUED status, BFT_A l.230):
- A_s := κ_+(1 + C_6L^{-3}) — residual-type rows: BA-6's κρ^{(2)}_l (own ≤ κC_6L^{-3(k-l)}η², BFT_A l.155-157) and CR-1's
  s^C_l (own ≤ κ_lL^{-3(k-1-l)}η², l.1018-1019);
- A_B := c_Bκ_+L² — the a-priori BCH₂ row bound π_l(R^B_l) ≤ A_Bη² (BFT_B §19.4 l.2629 with c_B = 2C_bch; BA-6 l.157-158
  gives the same form with c_B = 2p_L);
- A_W — the level-0 Wilson plain row, π_0 ≤ A_Wη² (BFT_A l.227, BA-3 / §28.6 (b));
- C_f := 1 + 2d(1 − L^{-3})^{-1} = 121/13 at d = 4, L = 3; A_j := C_f·max(A_B, A_W);
- C_NC^B := 8dN_Rq_R(q_R + 1)^d, the constant of BFT_B §29.4 (sup_own|V_l| ≤ C_NC^Bsup_own|R^B_l|). **Symbol collision
  (systemic defect 1):** BFT_A Proposition NC's C_NC(q_R, N_R) = 48N_R(2q+1)⁴q⁵(1+8q) (l.2570) is a different constant (it
  bounds W, not V). Both are k-independent; nothing below depends on which is meant beyond its name.

> **Lemma TR (transport decay of the residuals and of the BCH₂ rows at critical points).** Let x* be a critical point of
> 𝔉_k∘exp with ||x*||_𝔐 ≤ η ≤ η_0. Then for 0 ≤ l ≤ k − 2, m = k − 1 − l:
> **(TR-1)** ||r^c_l(x*)||_∞ ≤ κ_-^{-1}L^{-2m}η[κ_+ + (2A_s + mA_j)η]   (the 𝔐^∇ weight alone gives only L^{-m}η);
> **(TR-2)** π_l(R^B_l(x*)) ≤ A_Bη²·min{1, κ̂L^{-m}[1 + (2A_s + mA_j)η/κ_+]};
> **(TR-3)** for every θ ∈ (0, 1): ‖V‖_Pc := max_{1≤l≤k-1}L^{θ(k-l)}π_l(V_l) ≤ K_Pc(θ)η²,
>   K_Pc(θ) := C_NC^BA_Bκ̂L^θ[1 + 2A_sη/κ_+ + A_jη/(κ_+e(1 − θ)ln L)];
> **(TR-4)** Σ_{1≤l≤k-1}π_l(V_l) ≤ K_Ση², K_Σ := C_NC^BA_Bκ̂[(L/(L−1))(1 + 2A_sη/κ_+) + (L/(L−1)²)A_jη/κ_+].
> All constants are independent of k, T and of any gauge fixing.

**Proof.**
*Step 0 (criticality is a linear identity; no (GI) needed).* REVIEW_BFT_A_S7 l.152-153 (its review of Lemma CD): "At a
critical point 𝔑^0 = Hx − NB". E_src's gradient is Hx − NB − S (BFT_A §7.1: sources enter as −⟨S, x⟩), so **x* is a critical
point of E_src(·; B_k) with source S* := 𝔑^0(x*; B)**. A critical point of E_src exists only if Ξ^TS* = 0 on Λ_0 (Lemma FG
(iv): E_src(x + Ξλ) − E_src(x) = −⟨S, Ξλ⟩), so S* is a Setting LIN^cc source and **Lemma RT-cc applies to (S*, x*)**.
(Lemma CD (i) even gives (CC-0); only composite co-closedness is used here.) Slots of S*: residual-type s_l = BA-6's κ_lρ^{(2)}_l
+ CR-1's s^C_l (+ higher order); plain currents j_l = R^B_l (+ at l = 0 the Wilson plain row; + higher order); divergence form
only at level 0 (the Wilson q, which never enters r_i). The whole BCH₂ row is put in the plain slot: Setting LIN^cc places no
condition on individual plain currents, and the split R^B_l = d*W_l + V_l is used only in Step 3.

*Step 1 (transport ⇒ TR-1).* Lemma RT-cc (c) (BFT_B §29.1; CONFIRMED, REVIEW_BFT_B_S9_S10) at (S*, x*), for 0 ≤ i ≤ k − 2:
  r_i = κ_i^{-1}[s_i + (Q_str^{(i+1→k)})^Tρ_{k-1} − Σ_{l=i+1}^{k-1}(Q_str^{(i+1→l)})^Tĵ_l],  ρ_{k-1} := κ_{k-1}r_{k-1} − s_{k-1}.
Lemma TC's sup bounds (BFT_B §19.2; CONFIRMED, REVIEW_BFT_B_S6 B.2, valid for any current — co-closedness is not used for the
size): in level-(i+1) coarse units, with m = k − 1 − i,
  ||r^c_i|| ≤ κ_-^{-1}[||s^c_i|| + L^{-2m}(||ρ_{k-1}|| + Σ_{l=i+1}^{k-1}π_l(ĵ_l))].
A-priori sizes on the 𝔐^∇-ball: ||s^c_i|| ≤ A_sL^{-2m}η² (own sizes above, times L^m); ||ρ_{k-1}|| ≤ κ_+||r^c_{k-1}|| +
||s^c_{k-1}|| ≤ κ_+η + A_sη²; and by Lemma FT (ii) (CONFIRMED), π_l(ĵ_l) ≤ π_l(j_l) + 2dΣ_{l'≤l}L^{-3(l-l')}π_{l'}(j_{l'}) ≤
A_jη², so the sum over the m levels above i is ≤ mA_jη². Collecting: ||r^c_i(x*)|| ≤ κ_-^{-1}[A_sL^{-2m}η² + L^{-2m}(κ_+η +
A_sη² + mA_jη²)] = κ_-^{-1}L^{-2m}η[κ_+ + (2A_s + mA_j)η]. ∎(TR-1)
*Reading.* This is the "transport gains L^{-2} per level in coarse units" of Theorem RH (BFT_B l.2621) and NORMS Lemma N1-4's
residual exponent d − 1 = 3 (own units), now at the nonlinear critical point. The source used it for N_res and for the 𝔐
residual weight (§31.2 (a)), never for the size of the rows. Note that the residual-type rows already scale like L^{-2m}, so
nothing in S* limits the decay.

*Step 2 (rows ⇒ TR-2).* The BCH₂ row is linear in the residual: ⟨R^B_l, u⟩ = 2κ_lΣ_c⟨r_l(x)(c), B_c(x_l, u_l)⟩ (BFT_A §12.0;
§28.12 "R_c(u) := 2κ_lr_l(x)(c)B_c(x_l, u_l)"), and every source estimate of it has the form
  (★) π_l(R^B_l) ≤ c_Bκ_+L^{3(k-l)}·sup_own|x_l|·sup_own|r_l|  (BFT_B l.2629; BA-6 "κ·2p_Ls_l·|r_l|", l.157).
With sup_own|x_l| ≤ L^{-(k-l)}η and sup_own|r_l| = L^{-m}||r^c_l||: π_l(R^B_l) ≤ c_Bκ_+L^{m+2}η||r^c_l||_∞. The 𝔐^∇ weight
||r^c_l|| ≤ L^{-m}η reproduces the source's A_Bη²; (TR-1) gives A_Bη²·κ̂L^{-m}[1 + (2A_s + mA_j)η/κ_+]. ∎(TR-2)
(kf55_1 B1 checks this algebra exactly, m ≤ 400, 243 parameter sets.)

*Step 3 (remainders ⇒ TR-3, TR-4).* BFT_B §29.4 (l.3733-3735): sup_own|V_l| ≤ C_NC^Bsup_own|R^B_l|, obtained piece by piece
(Lemma BOG on cubes of side q_R + 1, ≤ N_R pieces per link), so it transmits any level-dependent bound: π_l(V_l) ≤ C_NC^B·(TR-2).
With L^{θ(k-l)} = L^{θ(m+1)} and min{1, ·} ≤ second argument (κ̂ ≥ 1), max_l L^{θ(k-l)}π_l(V_l) ≤ C_NC^BA_Bη²L^θκ̂·
max_{m≥0}L^{-(1-θ)m}[1 + (2A_s + mA_j)η/κ_+], and sup_{t≥0}tL^{-(1-θ)t} = 1/(e(1 − θ)ln L): (TR-3). Σ_{m≥0}L^{-m} = L/(L−1)
and Σ_{m≥0}mL^{-m} = L/(L−1)²: (TR-4). ∎ (kf55_1 B2 checks both closed forms against the exact maxima and sums for
2 ≤ k ≤ 400; B3, the control, shows the old bounds grow — class norm by ≥ 2·10⁴⁹, level sum by ≥ 75 at k = 400 — while the
new ones do not; B4: no gain is claimed at the top step m = 0.)

*Step 4 (optional; removes the factor m).* Feeding (TR-2) for the levels l > i back into Step 1 in place of A_Bη²:
Σ_{l>i}π_l(ĵ_l) ≤ C_f[A_Bκ̂Σ_{n≥0}L^{-n}(1 + (2A_s + nA_j)η/κ_+) + 2d(1−L^{-3})^{-1}A_W]η² = O(1)η², so
||r^c_i(x*)|| ≤ κ_-^{-1}L^{-2m}η(κ_+ + c'η) and π_l(R^B_l) ≤ A_Bκ̂L^{-m}(1 + c'η/κ_+)η², c' independent of m, k, T. Not
needed below.

**Scope, stated plainly.** Identical to Corollary COF-crit's: critical points of 𝔉_k∘exp in the 𝔐^∇-ball; trivial
background; m = 0; the source's second-order row sizes (third order at its ARGUED status); Corollary NC's no-wrap proviso
(REVIEW_BFT_A_S6 P6-4) as in §29.4. **No new hypothesis. No (SPD), no (W2), no (SB), no (G♯-rough), no (GI).**

> **Corollary COF-crit♯ (§35.6 with its proof repaired; the k-uniform statement is TRUE).** At every critical point of
> 𝔉_k∘exp with ||x*||_𝔐 ≤ η ≤ η_0 and every 0 < α < θ < 1: ||f_0||_∞ + [f_0]^∞_α ≤ C_funC'_♯η², with C'_♯ independent of
> k, T and Γ. *Proof.* §35.6 verbatim with "π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²" replaced by (TR-3) (or, on the sharper route,
> π_0(C(j)) ≤ Σ_lπ_l(ĵ_l) ≤ C_f(K_Σ + O(L^{-3})A_W)η² by (TR-4) and Lemma FT). ∎
> **What is NOT discharged** (pre-existing in §35.6, not part of the k-factor): the top-residual input of Corollary RHT-V
> ("||r^c_{k-1}||_∞ ≤ ||x||_inv ≤ G_Rη²"), which REVIEW_BFT_B_S9_S10 marks as an (H-inv) hypothesis for the non-co-closed
> rows; the (G)-slot Campanato size of the W_l (quoted, never written); second order only; trivial background; m = 0.

**Consequences for the record (each re-derived above).**
- REVIEW_BFT_B_S9_S10 S10-6: "COF-crit is WRONG as stated" — the DERIVATION is wrong (CONFIRMED: the substitution is real);
  the k-uniform STATEMENT is true (Corollary COF-crit♯). Its "honest status … CONDITIONAL on (SPD) for the k-uniform form"
  is **REFUTED**: the k-uniform form needs no (SPD)/(W2). "There is no choice of θ in (α, 1) that removes the factor" is
  **CONFIRMED** relative to S10-6's inputs — the factor is removed by a better INPUT, not by θ.
- S10-7: "the curvature half [of NCE (i)] is PROVEN with a constant O(k), k-uniform only given (SPD)" — **REFUTED as to k**:
  it is k-uniform by Corollary COF-crit♯, with NCE (i)'s other inputs as they stand.
- REVIEW55_TUNIF W9 (a) "the actual rows do not decay at birth at all" and W9 (e) "a decay hypothesis on V_l … that V_l does
  not satisfy" — **REFUTED at critical points**: π_l(V_l) ≤ C_NC^BA_Bκ̂L^{-(k-1-l)}[1 + O((k−l)η)]η², i.e. decay at birth with
  σ = 1. The cited lines (BFT_A l.819-824, BFT_B l.3735) are upper bounds on the whole 𝔐^∇-ball (and [RBA2-fix] B2 says
  explicitly "no lower bound on the rows exists"). THETAW's *form* "a row born at level l has plain coarse size ≲
  L^{-σ(k-l)}η²" therefore HOLDS at critical points with σ = 1, and Theorem COF's class norm consumes it for every θ < 1;
  this does not rescue THETAW's (W2)-based derivation (W9 (a)'s transport-distance objection stands; (W2) is not used here).
- REVIEW55_TUNIF W11 ("the level sum becomes geometric only through DECAY of what is summed … independent of θ"):
  **CONFIRMED**; Lemma TR supplies that decay.
- Corollary NC Remark 1 (BFT_A l.2590-2592: "Ω = k. So (NC-Γ) must use the smooth-part cancellation of V_l"): **REFUTED at
  critical points** (transport suffices, no smooth-part cancellation is used). On the whole 𝔐^∇-ball the a-priori bound is
  attained in order (a residual saturating the 𝔐 weight is admissible: x_l = 0, x_{l+1} = −c e_μ with |c| = L^{-2m}η own;
  ARGUED) — that is §5's subject.
- By-product (ARGUED, not part of the k-factor): the (G)-slot Campanato of the co-closed completions, ω_l[W^c_l]_α ≤
  ω_lL^{α(k-l)}||W^c_l||_∞ (BL-2 (e)), is ≤ CL^{(θ+α-1)(k-l)}η² with the a-priori rows (bounded iff θ ≤ 1 − α) and
  ≤ CL^{(θ+α-2)(k-l)}η² with (TR-2) (bounded for all θ, α < 1).

## §5. Off the critical set: the factor in the contraction is a norm artifact, and the exact object there

**(a) Where it still bites.** BFT-0's fixed point is produced by a contraction on a ball of 𝔐^∇ (BFT_A §3.9,
Φ(x) = 𝓛^{-1}(NB + 𝔑(x; B))), so (H-rem^∇) must bound the rows — and their Lipschitz constant — at EVERY point of the ball,
where Step 0 of §4 is unavailable. On the 𝔐^∇-ball the a-priori row bound is attained in order (§4, last bullets; ARGUED),
so **in the 𝔐^∇ pair the level-count factor is real for the contraction**: ‖R^B‖_Pc ≍ L^{θ(k-1)}η² and Σ_lπ_l ≍ (k − 1)η²
(this is S10-8's "a-posteriori" caveat, made quantitative).

**(b) Diagnosis.** 𝔐^∇ weights the residual by L^{k-1-j} (own-unit exponent θ_w^r = 2), one power below what every response
of the chain delivers (θ_w^r = d − 1 = 3: NORMS Lemma N1-4 "θ_w = d − 1 = 3 for the residuals"; BL-4; Theorem RH; (TR-1)).
The iterates of the contraction are responses, so nothing forces the ball to contain residuals that saturate the weaker
weight. **The minimal repair is to measure the residual in its transport weight.**

**(c) The transport-weighted pair (definition).** 𝔐^♯ := 𝔐^∇ with L^{k-1-j}||r^c_j||_∞ replaced by **L^{2(k-1-j)}||r^c_j||_∞**
(still a max over j). 𝒴^♯: **(R♯)** ||s||_{R♯} := max_lL^{2(k-1-l)}||s^c_l||_∞ (the (R) slot at source exponent θ_R = 1);
**(G♯)** ω^♯_l := L^{θ_G(k-l)} for l ≥ 1 with 1 < θ_G ≤ 2 − α (ω^♯_0 := 1); **(P0), (Pl-c)** unchanged (0 < α < θ < 1).

**(d) Proposition ROW♯ — PROVEN here at second order** (same inputs as §4: (★), BA-6, CR-1, BA-6's Lipschitz form
BFT_A l.380, Proposition/Corollary NC). For x, x' in the 𝔐^♯-ball of radius η, with m = k − 1 − l:
π_l(R^B_l(x)) ≤ A_BL^{-m}η² and π_l(R^B_l(x) − R^B_l(x')) ≤ 2A_BL^{-m}η||x − x'||_♯ (own |r_l| ≤ L^{-3m}η, |x_l| ≤ L^{-(m+1)}η,
then (★)); hence ‖R^B‖_Pc ≤ A_BL^θη² and ‖V‖_Pc ≤ C_NC^BA_BL^θη², Lipschitz 2× that over η. Commutator rows:
||s^C||_{R♯} ≤ κ_+η² (own ≤ κ_+L^{-4m}η²). BA-6's residual part: ||κρ^{(2)}||_{R♯} ≤ κ_+C_6L^{-3}η², Lipschitz
2C_LipL^{-3}η (BFT_A l.380). Co-closed completions (if split off): ||W^c_l||_∞ ≤ C_NC^AL^{-(k-l)}π_l(R^B_l) ≤
C_NC^AA_BL·L^{-2(k-l)}η², so ω^♯_l(||W^c_l||_∞ + [W^c_l]_α) ≤ 2C_NC^AA_BL·L^{(θ_G+α-2)(k-l)}η², bounded since θ_G + α ≤ 2.
**No level-count factor in any row of the ♯-ball.**

**(e) Proposition TW — PROVEN (implication of Lemma RT / RT-cc (c), Lemma TC, Lemma FT (iii), BL-4).** For every
composite-co-closed source y ∈ 𝒴^♯ with data B_k, every critical point x of E_src obeys
  max_{0≤i≤k-2}L^{2(k-1-i)}||r^c_i(x)||_∞ ≤ κ_-^{-1}[||s||_{R♯} + κ_+||r^c_{k-1}(x)||_∞ + ||s^c_{k-1}||_∞
     + C_f(||j||_Pc/(L^θ − 1) + ||j^c_0||_∞/(1 − L^{-3})) + 6||G||_{G♯}/(L^{θ_G-1} − 1)].
*Proof.* §4 Step 1 with the class sizes in place of the row sizes: L^{2m}||s^c_i|| ≤ ||s||_{R♯}; Σ_{l>i}π_l(ĵ_l) ≤
C_fΣ_{l>i}(L^{-θ(k-l)}||j||_Pc + L^{-3l}||j^c_0||_∞) (Lemma FT (iii)); Σ_{l>i}6L^{k-l}||G^c_l|| ≤ 6||G||_{G♯}Σ_{n≥1}L^{(1-θ_G)n}.
The top residual of the response is the old (H-lin) top output. ∎ (This is BFT_B §31.2 (a)'s display read at the weight L^{2m}
instead of L^m; the funnel is priced exactly as there.)

**(f) Inclusions — PROVEN (one line each).** ||s||_R ≤ L^θ||s||_{R♯} (ω^R_lL^{k-1-l} = L^θL^{(1+θ)m} ≤ L^θL^{2m} for θ ≤ 1);
||G||_Y ≤ ||G||_{G♯} (θ_G > θ); (P0), (Pl-c) equal. So every linear bound proven on 𝒴 holds on 𝒴^♯, and ||·||_{𝔐^♯} differs from
||·||_{𝔐^∇} only in the residual component, which (e) supplies for composite-co-closed sources and BL-4 for the data map.

**(g) Reduction — ARGUED (written here, not reviewed component by component).** BFT-0 in (𝔐^♯, 𝒴^♯) ⟸ (H-lin^∇) on 𝒴 [whatever
its status: Corollary HL, COF, …] + Proposition TW [PROVEN, cc sources] + **the residual output at the ♯ weight of the
gauge-fixed response to NON-composite-co-closed sources** [the off-critical NCR remainder: OPEN, as in the 𝔐^∇ pair —
(TENT-Q)/(NEUT-box)/(GT-sup) — now needed at the stronger weight] + Proposition ROW♯ [PROVEN, second order] + the source's
third-order, (FP♯') and gauge-variant items [unchanged]. **In this pair the plain-row level sum is k-uniform; the
level-count factor occurs nowhere.** Consistency with the exponent bookkeeping: θ_w^r = 3 meets the composite contraction's
requirement θ_w^r > d − 2θ_A = 2 (REVIEW55_TUNIF W5 (a), NORMS l.651-662) and the coupling (C2) θ_w^r ≤ 2 + θ_R at θ_R = 1
(BL-5 (a) has "no upper restriction on θ", BFT_A l.511; the θ < 1 of BL-6 (a) is the plain-current exponent, kept < 1 in (Pl-c)).
Codex F10's endpoint cost (REVIEW55_TUNIF W4: "with HX's Σ-aggregation … the endpoint costs k") is a cost of a Σ over levels;
𝔐^♯'s residual component is a max, and N_res = Σ_i||r_i||_{C^{1,α}} is summable in the ♯ pair (5L^{(1+α)m}·L^{-2m}).

**(h) The route the CORRECTION named — a carrier-type input that Theorem COF can consume for V_l — and why it is not minimal.**
A carrier version of COF would pair C(j) = Σ_l(Q_str^{(0→l)})^Tĵ_l (co-closed under (CC-0)) with a smooth representative of Y^p
and telescope as in Theorem XB Step 3. It needs at least: (1) SPD-type carrier decay for V_l (Corollary NC Remark 1: "small by
SPD and Lemma CS" — ARGUED there); (2) the same for the funnel parts h_l^Tψ_l (not in the source); (3) C¹-ℓ¹ control of some
representative of Y^p at every level ((PW-ℓ¹)-type: expected FALSE for Γ_E; LR-grad OPEN since session 3); and (4) (CC-0),
which fails off the critical set anyway. At the critical point it is superseded by Lemma TR (no new input); off it, it still
needs (4) like everything else. **So no carrier input is the missing object at either scope.**

**(i) The exact missing object, for the next worker.** For the k-factor itself: **none at the critical point** (Lemma TR,
proven). For the contraction: a component-by-component review of (g) — in particular that (H-rem) and the Lipschitz forms close
in (𝔐^♯, 𝒴^♯) at third order — and **Proposition TW off the critical set**, i.e. the ♯-weighted residual pairing
⟨D(S), λ^Γ_*⟩ of Proposition NCR with the level-i residual probes Y^{(b_i)}; this is the residual half of the lane's existing
open item (NC-Γ) off the critical set, not a new wall.

## §6. Classification

- **KF-F1 (not in the source): NO.** The factor is in the source (§1), and S10-6 derives it correctly from the inputs it quotes.
- **KF-F2 (fixed-size, genuine non-uniformity): KF-F2 in FORM only.** It multiplies a fixed-size a-priori bound (§2), but that
  bound is not the size of the object: at critical points the rows decay like L^{-(k-1-l)} (Lemma TR, PROVEN), and on the
  contraction's ball the non-decay is an artifact of the residual weight θ_w^r = 2 (§5, ARGUED, residual component PROVEN).
  **Not a genuine non-uniformity.**
- **KF-F3 (g_k²-size, marginal at d = 4): NO.** No coupling enters the composite problem. (There IS a d = 4 marginality
  underneath — the coarse-unit push-down contracts by exactly 1 per level, COF-size step 1 — which is why non-decaying
  per-level sources would produce a level count; the sources decay.)
- **Verdict line: KF-F2 as written; REMOVED at critical points (Corollary COF-crit♯, PROVEN as an implication of reviewed
  source lemmas); removable in the contraction by the transport-weighted pair (ARGUED).**

## §7. Check record

- **kf55_1** — criteria `checks/kf55_1_criteria.md` written 2026-10-28T23:20:01Z, before `checks/kf55_1.py` (written and run
  23:21Z); output `checks/kf55_1_out.txt`, stderr `checks/kf55_1_err.txt` (empty). Exact `Fraction` arithmetic; e and ln 3 by
  rigorous rational enclosures. **Results: A1 PASS (C_f = 121/13, C_f·e ∈ [25.300931, 25.300931]); A2 PASS (θ* > ¼ exactly
  for k ≤ 4, < ¼ for 5 ≤ k ≤ 10⁴, none undecided); B1 PASS; B2 PASS; B3 PASS (control fires: old/new ≥ 2.1·10⁴⁹ for the
  class norm, ≥ 75.6 for the level sum, at k = 400); B4 PASS. OVERALL PASS.**
- **Discriminating power (systemic defect 3).** A2 can fail and decides a real question (the admissibility of S10-6's θ*).
  Part B tests only the algebra from (TR-1) to (TR-2)-(TR-4) with free positive constants — it is built from my own formulas,
  so it can catch an exponent/units slip or a wrong closed form, but it cannot test (TR-1)'s inputs; those rest on the source
  lemmas (RT-cc, TC, FT — each CONFIRMED by a lane review, and bb6 B1 already measured the transport bound L^{-2m} as attained,
  BFT_B l.2621-2623). No check reaches the nonabelian rows themselves.

**Errata to §4-§5 line references (checked by grep after writing).** BL-5 (a)'s "no upper restriction on θ" is BFT_A
**l.518** (not l.511). BFT_B's "transport gains L^{-2} per level in coarse units" is at **l.2505 and l.2622** (not l.2621);
bb6 B1's "the bound L^{-2m} is attained (ratio 1.000 for m = 1, 2, 3)" is at **l.2610-2611** (not l.2621-2623). NORMS
l.651-662 is correct and says more than I quoted: "Soft condition at θ_A = 1: θ_w^r > d − 2 = 2. Delivered value
θ_w^r = d − 1 = 3 (J-str (c), PROVEN), margin exactly one power of L" (l.662-663) — that one power is the power Lemma TR uses.

## §4-A. Amendment after reading CODEX_REVIEW_C2.md and REVIEW55_BFTB Finding 6 (appended 2026-10-28T23:31Z UTC)

Both were read after §0-§7 were written (CODEX_REVIEW_C2 records "Review completed: 2026-10-28 23:21:26 UTC"; it is a Codex
review of REVIEW55_BFTB, located by grep for "COF-crit" across CODEX_REVIEW_*). KFACTOR55.md is still unread.

**(1) (CC-0) at critical points is FALSE — I agree with Codex C2 §6 and REVIEW55_BFTB Finding 6 (a).** Lemma CD is an identity
on Λ_* (ξ = 0 at the level-k roots; BFT_A §31.0, §33.3), so it gives composite co-closedness only. At a critical point,
𝔑^0 = Hx − NB and an unpinned gauge variation moves only the top residual, so D(𝔑^0) = κ_{k-1}ev_k^Td*r_{k-1}(x; B) as a
level-0 function (both reviews derive this; I re-derived it: Wilson and lower soft terms are invariant, r_{k-1} shifts by
d ev_kλ). Codex's explicit family (k = 1, L = 3, T = 2, N = 2; g_t = exp(tA), exp(tB) at the two non-root endpoints of a
block-face link e, so every plaquette and every complete S4' contour is 1 and U_t is an exact critical point;
x(t) = −t dξ + δ_eR(t), R(t) = −(t²/2)[A, B] + O(t³), Qδ_e = δ_{(X,0)}/27) gives root charge ±κ_0R(t)/27 ≠ 0. I checked the
logic of each step (the handles of the S4' contours stay inside blocks, so only the straight leg sees the face link e:
L starting positions, weight L^{-4}, total L^{-3}); I did not re-run its 64 × 1944 contour enumeration. **AGREE.**

**(2) What this does to my text.** *Lemma TR is unaffected:* Step 0 derives composite co-closedness from criticality and
never uses (CC-0); Lemma RT-cc (a)-(c) and Lemma FT (ii) need only that (the cascade gives d*ρ_l = ψ_l for l ≤ k − 1 with
ψ_{k-1} = R_k(D_j) possibly ≠ 0, and FT (ii) bounds h_l^Tψ_l whether or not ψ_{k-1} vanishes). **Withdrawn:** the
parenthetical in Step 0, "(Lemma CD (i) even gives (CC-0); …)" — it repeated §35.6's error. **Withdrawn in its stated
form:** Corollary COF-crit♯ ("§35.6 verbatim with …"), because §35.6's route needs (CC-0). It is replaced by:

> **Corollary COF-crit♯♯ (the repaired curvature half at critical points).** Let x* be a critical point of 𝔉_k∘exp with
> ||x*||_𝔐 ≤ η ≤ η_0, and x_rows := x* − x(B_k) the response to S* = 𝔑^0(x*; B) with homogeneous data (trivial background,
> m = 0, 0 < α < θ < 1). Then
> **||f_0(x_rows)||_∞ ≤ C·N(S*) ≤ C_♯η²,  ||f_0(x_rows)||_∞ + [f_0(x_rows)]^∞_α ≤ C[N(S*) + κ_+||r^c_{k-1}(x_rows)||_∞],**
> with C, C_♯ independent of k, T and Γ, where N(S*) := ||G^c_0||_∞ + [G^c_0]_α + ||G||_Y + ||s||_R + J and
> J := Σ_lπ_l(j_l) ≤ {A_Bκ̂[(L/(L−1))(1 + 2A_sη/κ_+) + (L/(L−1)²)A_jη/κ_+] + A_W + A_B}η².
> *Proof.* S* is composite-co-closed (Step 0), so CODEX_REVIEW_C2's whole-class bound (C2-COF) (§4 there; CONFIRMED there as a
> conditional theorem on the lane-A inputs YH, W0/LES-div/LE/BL-C, GU, LIN0/BL-5, PW-cc) applies. It prices ALL plain
> currents by their coarse SUM J, with no co-closedness and no V/W split; (TR-2) summed over l ≥ 1 (Σ_{m≥0}L^{-m} = L/(L−1),
> Σ_{m≥0}mL^{-m} = L/(L−1)²) plus the level-0 plain slot bounds J k-uniformly. The other slots of N(S*) are the source's
> a-priori ones (Wilson q: sup ≤ 9η² PROVEN, Hölder ARGUED, BFT_A l.226; ||s||_R ≤ C_sκ_+L^θη² by CR-1 + BA-6; no positive-level
> G slot when the BCH₂ rows are kept whole). ∎ **Sup half: PROVEN as an implication. Hölder half: PROVEN as an implication
> with the top-response term retained, exactly as Codex C2 requires.**
> *(Without Lemma TR, J ≤ (k − 1)A_Bη² + A_Wη²: this is Codex C2 §7's and REVIEW55_BFTB Finding 6 (b)'s O(kη²); both say "a
> new level-decay/cancellation estimate is still needed for the desired uniform conclusion". Lemma TR is that estimate.)*

> **Remark TOP-crit (ARGUED, sketch; outside the k-factor question).** The retained term is also O(η²) k-uniformly at critical
> points: r_{k-1}(x_rows)(b) = Ê(Y^{(b)}, x_rows) = ⟨S*, Y^{(b)}⟩ (Lemma FG (ii)), and since ⟨S*, Ξλ⟩ = ⟨D_j, λ⟩ = 0 for
> λ ∈ Λ_0, Y^{(b)} may be replaced by its tent-axial representative PY^{(b)} (P − 1 is a composite gauge trivial at level k,
> BFT_A §12.2 LR-pot). By Lemma TS and Corollary FP (BFT_A §13.13, PROVEN-HERE; T ≥ 3, 0 < m < m_*'),
> ||(PY^{(b)})^c_j||_{∞,m} ≤ C(m), hence ||(PY^{(b)})_l||_1 ≤ C'(m)L^{3(k-l)} T-uniformly and |⟨j_l, (PY^{(b)})_l⟩| ≤ C'(m)π_l(j_l):
> the plain part costs C'(m)J. The s- and G_0-pairings are bounded by Theorem W's weighted residual and curvature bounds.
> So κ_+||r^c_{k-1}(x_rows)||_∞ ≤ C(J + ||G^c_0|| + ||s||_R) = O(η²), which would also discharge Corollary RHT-V's (H-inv)
> parenthetical at critical points. Not claimed: I have not checked Corollary FP's constants, the T ≥ 3 proviso against the
> lane's small-torus treatment, or the normalisation of Y^{(b)}.

**(3) Effect on §4's "Consequences" list.** Each entry stands with "Corollary COF-crit♯" read as "Corollary COF-crit♯♯"; in
particular S10-6's and S10-7's "k-uniform only given (SPD)" and REVIEW55_BFTB Finding 6 (b)'s "the k-uniform form needs a
level-decay input for the rows (lane A's (SPD)/(W2))" are **REFUTED as to the input named**: the level-decay input exists
and is Lemma TR, which uses neither (SPD) nor (W2). The statement "COF-crit's k-uniform STATEMENT is true" is now: **true for
the sup half (PROVEN as an implication); true for the full Hölder statement given Remark TOP-crit (ARGUED)**. The
"(CC-0) at critical points" clause of §35.6 is FALSE (Codex C2 §6), and nothing here needs it.

## §8. Summary table (every claim I decided; written 2026-10-28T23:33Z UTC, before reading KFACTOR55.md)

| # | Claim (file, locating string) | Verdict | Where |
|---|---|---|---|
| 1 | S10-6: §35.6 substitutes per-level π_l(V_l) for ‖j‖_Pc; ‖V‖_Pc ≍ L^{θ(k-1)}·2C_NCC_bchκ_+L²η² from the quoted inputs | **CONFIRMED** | §1.4 |
| 2 | S10-6: "Corollary COF-crit (§35.6) is WRONG as stated" | **CONFIRMED** for its proof (two defects: this one and (CC-0), Codex C2 §6); the k-uniform sup conclusion is **TRUE** (COF-crit♯♯) | §4, §4-A |
| 3 | S10-6: "CONDITIONAL on (SPD) for the k-uniform form" | **REFUTED** — Lemma TR, no (SPD)/(W2) | §4 |
| 4 | S10-6: "no choice of θ in (α, 1) … removes the factor" | **CONFIRMED** (relative to its inputs; the fix is an input, not θ) | §4 |
| 5 | S10-6: sharper route ≈ 9.31(k−1)·2C_NCC_bchκ_+L²η² | **CONFIRMED** (C_f = 121/13) | kf55_1 A1 |
| 6 | S10-6: class route optimised, ≈ 25(k−1) at θ* = 1/((k−1)ln L) | arithmetic **CONFIRMED** (25.3009(k−1)); θ* < α = ¼ for all k ≥ 5, so **not attainable in COF's window** | kf55_1 A1, A2 |
| 7 | HANDOFF item 5: "the sharper route leaves ≈ 25(k-1)" | **REFUTED** (sharper route: ≈ 9.31(k−1)) | §1.5 |
| 8 | HANDOFF item 5: "The missing input is lane A's (SPD)/(W2), OPEN" | **REFUTED** (SPD is proven and not needed; (W2) not needed; Lemma TR) | §4 |
| 9 | HANDOFF item 5: the factor k is "UPSTREAM of (TENT-Q), (NEUT-box), (Y-sup^loc)"; "attack the factor k first" | **REFUTED** at critical points (removed); off the critical set the factor is a norm artifact (§5, ARGUED) and the remaining items are the off-critical remainder | §4, §5 |
| 10 | S10-7: NCE (i) curvature half O(k), k-uniform only given (SPD) | **REFUTED as to k** (sup half k-uniform, PROVEN as implication) | §4-A |
| 11 | BFT_A [RBA2-fix] B3: rows "O(η²) per level … no level decay" | **CONFIRMED** as an upper bound on the 𝔐^∇-ball; **REFUTED** as a description of the rows at critical points | §4 |
| 12 | BFT_A Corollary NC Remark 1: "Ω = k … must use the smooth-part cancellation of V_l" | **REFUTED** at critical points | §4 |
| 13 | REVIEW55_TUNIF W9 (a)/(e): rows "do not decay at birth at all"; V_l does not satisfy a decay hypothesis | **REFUTED** at critical points (decay at birth with σ = 1) | §4 |
| 14 | REVIEW55_TUNIF W11: a level sum becomes geometric only through decay of what is summed | **CONFIRMED** | §4 |
| 15 | REVIEW55_BFTB Finding 6 (a) and CODEX_REVIEW_C2 §6: (CC-0) false at critical points; CD is on Λ_* only | **CONFIRMED** (logic re-checked; enumeration not re-run) | §4-A |
| 16 | REVIEW55_BFTB Finding 6 (b), CODEX_REVIEW_C2 §7: the available estimate is O(kη²); a level-decay estimate is needed | **CONFIRMED** as to the then-available estimate; the named input "(SPD)/(W2)" **REFUTED** — the decay estimate is Lemma TR | §4-A |
| 17 | CORRECTION: the factor sits in COF-crit for V_l | **CONFIRMED** | §1 |
| 18 | CORRECTION: SPD at exponent 1 proven in carrier form | **NOT-VERIFIED by me** (read l.1024-1048, did not re-derive the counts; REVIEW_BFT_A_S3 l.25 confirms it); not load-bearing here | — |
| 19 | CORRECTION: lane A's live route (XB, CO-B, HL) uses neither (W2) nor (SB) | **CONFIRMED** (read §18.5 Steps 1-5, §23.11-23.12; BFT_A l.1546) | §0 |
| 20 | CORRECTION: "the missing object is a carrier-type input that Theorem COF can consume for V_l" | **REFUTED** as the minimal object (none is needed at critical points; the carrier route needs ≥ 3 new inputs plus (CC-0)) | §5 (h) |
| 21 | PROOF.md CURV-F2″ as the same level-count factor | **NOT the same object** (per-level θ-cascade, ε_unif = O(1/k)) | §1.6 |
| 22 | NEW: Lemma TR (TR-1)-(TR-4) | **PROVEN here** as an implication of RT-cc, TC, FT (CONFIRMED by lane reviews) and the source's second-order slot sizes | §4 |
| 23 | NEW: Corollary COF-crit♯♯ (sup half; Hölder half with the top-response term) | **PROVEN here** as an implication (C2-COF + Lemma TR) | §4-A |
| 24 | NEW: Remark TOP-crit (top residual of the row response O(η²), k-uniform) | **ARGUED** | §4-A |
| 25 | NEW: Propositions ROW♯ (second order), TW, inclusions (f) | **PROVEN here** | §5 |
| 26 | NEW: BFT-0 in the transport-weighted pair has no level-count factor | **ARGUED** | §5 (g) |
| 27 | Classification | **KF-F2 in form only; not a genuine non-uniformity** | §6 |

Counts over rows 1-21 (claims of others): CONFIRMED 10 (1, 4, 5, 11-as-bound, 14, 15, 16-as-estimate, 17, 19, and 2 for its
proof), REFUTED 9 (3, 7, 8, 9, 10, 12, 13, 20, and 6 as "the" figure), NOT-VERIFIED 1 (18), not-the-same 1 (21). Rows 2, 6, 11,
16 carry a split verdict and are counted once, by their first verdict word.

## §4-B. Response to the coordinator's mid-task correction (BALABAN_EXTRACT.md), checked against my conclusion
(appended 2026-10-28T23:36Z UTC; I read BALABAN_EXTRACT §5 (M1-M9), §7.5, §7.6 and §9 by grep + sed. My conclusion in §1-§8
was written before this message arrived and is not changed by it; each point is checked below. KFACTOR55.md still unread,
except through the two sentences the extract quotes from it at l.445-447, which only locate the rows.)

1. **"Drop the g_k-threshold hypothesis."** Agreed, and my §3 (a) already answered NO. Its supporting aside quoted PROOF.md
   l.870 ("||1 − U_p|| ≲ p(g_k)g_k at each scale") and derived k(p(g_k)g_k)² ≍ p(g_k)²/β_0; BALABAN_EXTRACT M7 (l.270-277)
   reads Balaban's thresholds as FIXED (ε_0 for the background in coarse units, ε_1 per bond), the alternative being
   g_k/γ_k·ε_1 ≍ g_k³ε_1. **The aside is withdrawn as moot** (it computed a consequence of a misattributed threshold); the
   answer to (3)(a) stays NO, now because the thresholds do not shrink with g_k at all. KF-F3: my §6 already says NO, on the
   independent ground that no coupling enters 𝔉_k; I agree it was framed on the misattribution (extract §8.2).
2. **Balaban's mechanism (M1 one-shot composite definitions; M2 every level re-evaluated at the one current background;
   M5 per-level contributions shrink geometrically).** Consistent with Lemma TR, which is this lane's version of M1-M2: the
   critical point x* of 𝔉_k IS the background defined once from the full k-step constraint, every level's BCH₂ row is
   evaluated at it, and at it the level-l row carries L^{-(k-1-l)} (TR-2), so the level sum is geometric (TR-4). (M5 itself is
   about renormalised polymer activities, (L^jη)^α; it is the same structural feature, not the same object.)
3. **The extract's sharpest point, checked item by item.**
   - *"The two level-count rows are LINEAR in the soft residual."* **CONFIRMED** — my (★) in §4 Step 2 (BFT_A §12.0, §28.12).
   - *"The hard scheme has a matching term through its Lagrange multiplier."* **CONFIRMED in this lane's variables:**
     κ_lr_l = ρ_l + s_l with ρ_l the effective residual current, and R^B_l = 2B(x_l, ·)^T(ρ_l + s_l). The Euler-Lagrange
     cascade ρ_{l-1} = Q_{str,l}^Tρ_l − d*G_l − ĵ_l (Lemma RT-cc (b)) is the multiplier's transport; in the hard limit ρ_l is
     the multiplier. **In both schemes the multiplier at a critical point decays like L^{-3} per level in own units**
     (NORMS l.662: "θ_w^r = d − 1 = 3 (J-str (c), PROVEN), margin exactly one power of L"), and that power is what Lemma TR
     feeds into the rows. So hard vs soft is not where the factor lives; extract §9 (b)'s "the multiplier carries the same
     information, so this alone does not remove the level count" is right about hardness and is answered by transport.
   - *"The factor k may come from the UNITS the rows are summed in."* **CONFIRMED, with a correction to which units.** The
     responsible units are the a-priori units of the MULTIPLIER — 𝔐^∇'s residual weight L^{k-1-j}||r^c_j|| (θ_w^r = 2) — not
     the plain-current currency of the level sum. Summed as currents in plain coarse units (the currency of [RBA2-fix] B3 and of
     (C2-COF)'s J), the rows at a critical point give the geometric sum (TR-4). The extract's [Inference] (l.455-461) that "the
     lane's factor arises when the same terms are measured as currents in plain coarse units at level 0" is therefore
     **REFUTED as the mechanism**: the currency is harmless once the multiplier carries its transported size; with the 𝔐^∇
     multiplier size the factor appears in any currency in which the rows are summed without decay.
   - *"The hard constraint absorbs sources in Ran Q_k^T exactly" (extract §7.5).* **CONFIRMED** (cross-checked as asked): for
     Q_kA = B, ⟨Q_k^Ts, A⟩ = ⟨s, B⟩ on the constraint set; in the soft chain the same source is a data shift / residual-type
     sources (BFT_A BL-1 (i), (iii); Lemma TS, BFT_A l.1069-1075). The soft scheme's genuine price is BFT_A BL-6 (b): a
     NON-decaying Ran Q^T family at every level gives r_{k-1} = (k − 1)c/κ exactly — a real (k − 1). **The rows at a critical
     point are not such a family** (they decay, TR-2), so the soft scheme pays their stacking geometrically. Hence **the
     level-count factor is not an argument for the hard scheme** (relevant to extract §9's Step-3 question).

**Errata to §4-B (checked by grep after writing).** The §4-B header time should read **2026-10-28T23:33:48Z** (the append's
actual stat time; "23:36Z" was a typing error). BALABAN_EXTRACT's M7 is at **l.274-277** (not l.270-277); its [Inference] is at
**l.457-463** (not l.455-461); its §9 (b) "the multiplier carries the same information" is at l.610.

---

## §9. Comparison with KFACTOR55.md (Codex gpt-6-astra/max) — read 2026-10-28T23:34:02Z UTC, after §0-§8 and §4-A/§4-B

KFACTOR55 (288 lines, mod 18:44 local = 22:44Z) ends with a [LEAD] note and a complete §7; it does not look unfinished.
Point by point (C# = my numbering of its claims, in its order):

| C# | KFACTOR55 claim (locating string) | Mine | Agree? / who is right |
|---|---|---|---|
| C1 | §1 "at g = 1"; the g_j are gauge transformations, not couplings | §2 | **Agree.** |
| C2 | §1 "First level-count step": BA-6's plain row (1), π_l ≤ 2κ_+p_LL²η², "own-unit decay already used up"; GAP 1 (F3), then B3 | §1 items 1-3 | **Agree on the text.** But (1) is computed with the 𝔐^∇ residual weight |r_l| ≤ L^{-2(k-1-l)}η; KFACTOR55 never asks whether r_l is smaller at the point where COF-crit is stated. That is the one step where we part (C12, C21). |
| C3 | §1 "Two different commutators must be separated": [A^T, χ]A (§3.10) is LINEAR in the displacement (size CL³η/ℓ), not a quadratic η² row; B3's grouping is wrong in degree | not addressed | **Codex is right; I missed it.** I add: it is linear in the residual Ax of what it acts on, so on responses (BA-11's E = Σ[𝓛_□, χ_□]𝓖_□ψ_□) it inherits the same transport decay — (COMM) would then be k-uniform on responses (ARGUED; outside 𝒞_glob, not my target). |
| C4 | (2): W decays, V "uniform in l"; no coupling in (1)-(2) | §1, §2 | **Agree.** |
| C5 | §1 "Fixed field scale": η = C_0ε, chart radii, no η ∼ g_k | §2 | **Agree.** |
| C6 | §2 (6): π_0(C(j)) ≤ A_f[B + (k−1)M], A_f = 121/13 | §1.5, kf55_1 A1 | **Agree** (independently: same 121/13). |
| C7 | §2 "The failed substitution" (7) | §1.4 | **Agree.** |
| C8 | §2 consequence [C_base + C_stack(k−1)]η²; NCE §36.5 (i) unsupported; no lower bound | §4 | **Agree as to the source's route**; Lemma TR removes C_stack(k−1) at critical points. |
| C9 | §3 (8): A_f·e·n ≤ inf F_n ≤ A_f·e·(n+2); "≈ 25(k−1)" is (121e/13)(k−1) | §1.5, kf55_1 A1 | **Agree** (my 25.3009(k−1) is its leading term; its two-sided bound is the sharper statement). |
| C10 | §3 "The optimization is not legal at fixed Hölder exponent for arbitrarily large k" | §1.5, kf55_1 A2 | **Agree — found independently.** A2 adds the threshold: illegal for every k ≥ 5 at α = ¼, L = 3. |
| C11 | §3 constant co-closed currents j_l = L^{-3(k-l)}a give π_0(C(j)) = k − 1: (CC-0) + slot sizes cannot give a uniform aggregation; "not claimed to be an admissible BCH₂ remainder" | §4-B (BL-6 (b)) | **Agree**, and it is the right witness: Lemma TR shows the rows of a critical point are NOT such a family (they decay like L^{-(k-1-l)}), which is exactly the "additional structure" C11 says is needed. |
| C12 | §4.1 "Geometric convolution is not geometric decay to the top … Neither is an unspent L^{-δ(k-l)} gain" | §4 | **Agree for the two objects it examines (funnel kernel, push-down); its search was incomplete.** The unspent gain is inside the row, in the residual factor r_l: one power L^{-(k-1-l)} (NORMS l.662's "margin exactly one power of L"). |
| C13 | W and residual pairings decay; CO-B restricted to level-wise co-closed rows | §4, §5 (h) | **Agree.** |
| C14 | §4.1 three statements named SPD; carrier (9)-(10) L^{-(m-l)}η²; W2 = SPD + (SB), (SB) open | §5 (h), table #18 | **Agree.** |
| C15 | §4.1 carrier route via Proposition SR needs (PW-ℓ¹) | §5 (h) | **Agree** (and it is not minimal, §5 (h)). |
| C16 | §4.2 a contraction with Lipschitz Ckη needs η ≤ q/(2Ck); η = O(k^{-1/2}) controls kη² but not kη | §5 | **Agree.** This is why §5 asks for a k-uniform Lipschitz bound (ROW♯ gives 2A_BL^{-m}η, k-uniform) rather than a shrinking radius. |
| C17 | §4.2 AF table (conditional on (AF)) | §3 (c) | **Agree as conditional algebra** (I re-derived the four limits: c²/(b log L); c√(k/(b log L)); 0; c/(b log L)). Moot: no coupling enters. |
| C18 | §4.2 restoring g does not insert a missing g²: (g^{-2}H)^{-1}g^{-2}N = H^{-1}N; quadratic term gets one power of g | §3 (c) | **Agree** (re-derived). |
| C19 | §4.2 text connects no threshold to a coupling; PROOF's L5 reports fixed ε_0, ε_1 and the g_kε_1/γ_k alternative; no Balaban inference | §3 (a), §4-B.1 | **Agree; Codex was the more careful.** My §3 (a) aside used PROOF l.870's "p(g_k)g_k"; withdrawn in §4-B.1 after BALABAN_EXTRACT M7. |
| C20 | §4.2 per-level running: Σ_q g_[q]² ≍ H_n diverges | — | **Agree** (re-derived the two-sided harmonic bound). |
| C21 | §6 (J-unif) and "a stronger but simpler sufficient input: π_l(V_l) ≤ AL^{-δ(k-l)}η² … proves (J-unif) as an implication" — "not proved for the actual V_l here" | §4 | **Agree that it suffices — and Lemma TR proves it at critical points** with δ = 1 up to the factor 1 + O((k−l)η) (any δ < 1 exactly; Step 4 removes the factor). Codex states the input; this file proves it from RT-cc, TC, FT and the source's slot sizes. |
| C22 | §6 "OPEN — Minimal substantive obligation … a bound valid only at already-existing critical points supplies regularity, not their construction" | §5 | **Agree with the distinction.** At critical points the obligation is discharged (COF-crit♯♯). For construction, §5 gives the norm-level repair: ROW♯'s Lipschitz bound (the "difference estimate" C22 asks for) is PROVEN at second order in the transport-weighted pair; the off-critical remainder stays OPEN in both. |
| C23 | §6 "Immediate honest repair": keep [C_base + C_stack(k−1)]η²; radius η_k ≤ c/k for a fixed-depth contraction | §4, §5 | **Superseded.** Valid but not minimal (it gives up the uniform domain, as Codex says); Lemma TR (critical points) and the ♯ pair (ARGUED, contraction) need no shrinking radius. |
| C24 | §6 "Why the count is upstream of the root-charge repairs": (6) holds after imposing (CC-0), so TENT-Q/NEUT-box/Y-sup^loc cannot repair it by the displayed substitutions | §8 #9 | **Right as a statement of logical independence; two premises have since moved:** (CC-0) at critical points is false (CODEX_REVIEW_C2 §6, which I agree with, §4-A), the whole-class (C2-COF) replacing it; and after Lemma TR the count is gone at critical points, so "upstream" no longer describes it. |
| C25 | §7.1 "KF-F2 is the source-level diagnosis … a genuine non-uniformity of the available bound and a missing proof obligation, not a theorem that the actual nonlinear response diverges" | §6 | **Agree as to the available bound; disagree with "genuine" as the brief defines KF-F2.** The per-level quantity is not fixed-size at critical points (Lemma TR). Codex's own hedge ("not a theorem that the actual response diverges") is what Lemma TR cashes. |
| C26 | §7.2 KF-F1 rejected; 25(k−1) not intrinsic; direct bound (121/13)(k−1) | §1, §6 | **Agree.** |
| C27 | §7.3 KF-F3 only as a possible extra normalisation | §6 | **Agree.** |
| C28 | "Least certain point": whether the actual non-co-closed BCH₂ family, "with its criticality/Ward identities and carrier cancellations", satisfies a direct uniform estimate the slot-by-slot bounds miss | §4 | **This is where I resolve it: YES at critical points, through the criticality identities (the Euler-Lagrange transport of the multiplier, Lemma RT-cc (c)), with no carrier cancellation and no Ward identity.** |

**Net.** No factual disagreement about the source text: both analyses locate the factor in the same steps, get the same 121/13,
reject the same θ-optimisation (C10) and the same g-threshold readings. **The one substantive difference is the bottom line:
KFACTOR55 leaves the uniform estimate OPEN as the "minimal substantive obligation" (C21, C22, C28); this file proves it at
critical points (Lemma TR → COF-crit♯♯) and reduces the contraction case to a norm choice whose only remaining open input is the
lane's existing off-critical remainder (§5, ARGUED).** Who is right: on what the source text contains, both; on whether the
obligation is open, this file, because the decay follows from lemmas the lane has already proved and reviewed (RT-cc, TC, FT)
plus the one observation that the BCH₂ row is linear in r_l — the step KFACTOR55's §4.1 search for "unspent decay" did not
examine. Codex is right and I was wrong (by omission) on C3 ([A^T, χ]A is linear, not quadratic), and Codex was more careful on
C19. **The Codex reviewer who checks this file should attack (TR-1) first** — in particular Step 0 (that x* is the E_src
critical point for S* = 𝔑^0(x*)), the use of Lemma TC's sup bounds on non-co-closed currents, and the a-priori sizes A_s, A_j.

## §10. For the lead (written 2026-10-28T23:36Z UTC)

**Bottom line.** The ≈ 25(k−1) is real in the source's bounds and absent from the object. It comes from bounding the BCH₂
row R^B_l = 2κ_lB(x_l, ·)^Tr_l with the 𝔐^∇ residual weight (own |r_l| ≤ L^{-2(k-1-l)}η, θ_w^r = 2). At a critical point the
residual is the transported multiplier, one power L^{-(k-1-l)} smaller (Lemma RT-cc (c) + Lemma TC; NORMS l.662 "margin exactly
one power of L"), so the rows decay like L^{-(k-1-l)} and the level sum is geometric. **Lemma TR (PROVEN here, as an
implication of reviewed source lemmas; no (SPD), (W2), (SB) or (GI)) + CODEX_REVIEW_C2's whole-class (C2-COF) ⇒ the curvature
sup half of COF-crit / NCE (i) is k- and T-uniform at critical points; the Hölder half holds with the top-response term retained
(Remark TOP-crit, ARGUED, bounds that term too).** For the contraction the factor is a norm artifact, removed by the
transport-weighted pair θ_w^r = 3 that NORMS/[S24-fix 3] already ask for (ARGUED; its residual component and the rows' bound
and Lipschitz constant PROVEN). Classification: **KF-F2 in form, not a genuine non-uniformity.**

**Counts (claims of others, §8 rows 1-21; split rows counted by their first verdict word): CONFIRMED 10 / NOT-VERIFIED 1 /
REFUTED 9** (+1 "not the same object": CURV-F2″). New results of this file: Lemma TR, Corollary COF-crit♯♯, Propositions ROW♯
and TW, inclusions (f) — PROVEN (ROW♯ at second order); Remark TOP-crit and the §5 (g) reduction — ARGUED. Check kf55_1: PASS
(criteria before script; its limits are stated in §7).

**Every REFUTED item, with its correction.**
1. S10-6 "CONDITIONAL on (SPD) for the k-uniform form" → the k-uniform form follows from Lemma TR; neither (SPD) nor (W2) is used.
2. S10-6's "≈ 25(k−1)" as the figure → its θ* = 1/((k−1)ln L) is below α = ¼ for every k ≥ 5 (kf55_1 A2), outside COF's window;
   the honest pre-repair figure was the sharper route's (121/13)(k−1); after Lemma TR it is O(1).
3. HANDOFF item 5 "the sharper route leaves ≈ 25(k-1)" → the sharper route leaves (121/13)(k−1) ≈ 9.31(k−1) (pre-repair).
4. HANDOFF item 5 "The missing input is lane A's (SPD)/(W2), OPEN" → the missing input was the decay of the rows at critical
   points; it is Lemma TR, proven here; (SPD) is proven anyway and not needed; (W2) is not needed.
5. HANDOFF item 5 "UPSTREAM of (TENT-Q), (NEUT-box), (Y-sup^loc) … attack the factor k first" → at critical points the factor is
   gone; off the critical set it is a norm artifact (§5), and what remains there is the off-critical remainder itself.
6. S10-7 "the curvature half is PROVEN with a constant O(k), k-uniform only given (SPD)" → sup half k-uniform at critical points
   ((C2-COF) + Lemma TR); Hölder half with the top-response term.
7. BFT_A Corollary NC Remark 1 "Ω = k. So (NC-Γ) must use the smooth-part cancellation of V_l" → at critical points transport
   suffices; no smooth-part cancellation is used.
8. REVIEW55_TUNIF W9 (a) "the actual rows do not decay at birth at all" and W9 (e) "a decay hypothesis on V_l … that V_l does
   not satisfy" → at critical points π_l(V_l) ≤ C_NC^BA_Bκ̂L^{-(k-1-l)}[1 + O((k−l)η)]η²: decay at birth with σ = 1.
9. The CORRECTION's "the missing object is a carrier-type input that Theorem COF can consume for V_l" → not the minimal object:
   none is needed at critical points; the carrier route needs ≥ 3 new inputs plus (CC-0), which fails at critical points.
Also refuted inside split rows / §4-B: REVIEW55_BFTB Finding 6 (b)'s named input "(lane A's (SPD)/(W2))" (same correction as 4);
BALABAN_EXTRACT §7.6's [Inference] that the factor "arises when the same terms are measured as currents in plain coarse units"
(the plain-current currency is harmless; the a-priori size of the multiplier is the cause); and, credited to Codex KFACTOR55 C3,
BFT_A [RBA2-fix] B3's grouping of [A^T, χ]A with the O(η²) rows (it is linear in the displacement, O(η/ℓ)). My own withdrawn
items: §3 (a)'s p(g_k)g_k aside (§4-B.1); Step 0's "(Lemma CD (i) even gives (CC-0))" and Corollary COF-crit♯ in its "§35.6
verbatim" form (§4-A).

**What should change in HANDOFF's critical path and PROOF.md.**
- HANDOFF item 5 should be rewritten along these lines: *"The level-count factor is REMOVED at critical points: Lemma TR
  (KFACTOR_O55 §4) — the BCH₂ rows are linear in the residual, and at a critical point the residual is the transported
  multiplier, so π_l(R^B_l) ≲ L^{-(k-1-l)}η²; with CODEX_REVIEW_C2's whole-class (C2-COF), NCE (i)'s curvature sup half is
  k-, T-uniform; Hölder half with the top-response term (Remark TOP-crit, ARGUED). It is no longer upstream of (TENT-Q),
  (NEUT-box), (Y-sup^loc). For the contraction, adopt the transport-weighted residual weight θ_w^r = 3 (KFACTOR_O55 §5; ARGUED);
  the remaining open input there is the off-critical remainder, already on the list."* Strike "(SPD)/(W2), OPEN" as the missing
  input and the "sharper route leaves ≈ 25(k-1)" figure.
- BFT_B §35.6 / §36.5 (i): record (CC-0)-at-critical-points as FALSE (CODEX_REVIEW_C2 §6, REVIEW55_BFTB Finding 6 (a); I agree),
  COF-crit's proof as REFUTED, and its sup conclusion as PROVEN-as-implication via (C2-COF) + Lemma TR.
- Whether PROOF.md's numeric tally moves depends on how the lead maps COF-crit/NCE (i) to tally rows; I make no tally claim.
- Next worker, in order: (1) a Codex review of Lemma TR, attacking (TR-1) — Step 0, Lemma TC's sup bounds on non-co-closed
  currents, and the a-priori sizes A_s, A_j; (2) a component-by-component check of the §5 (g) reduction in (𝔐^♯, 𝒴^♯),
  including the third-order rows and Lipschitz forms; (3) Remark TOP-crit written out (Corollary FP's constants, T ≥ 3,
  normalisation of Y^{(b)}); (4) the off-critical remainder at the ♯ residual weight (the lane's existing item, not new).

**Codex verdicts used, agree/disagree.** CODEX_REVIEW_C2 §6 ((CC-0) at every critical point REFUTED): **AGREE** (logic
re-checked, enumeration not re-run). CODEX_REVIEW_C2 §4 (whole-class (C2-COF) CONFIRMED as a conditional theorem): **AGREE with
its structure** (coarse face-sum flux b with ||b|| ≤ J, the straight-path source P(b) = residual top source + d*Σb(e)G_e, then
strict plain-only COF); I did not re-verify its dipole filling or its constants, and I use it as a labelled conditional input.
CODEX_REVIEW_C2 §7 (S10-6's loss is an unremoved estimation loss; a level-decay estimate is needed): **AGREE**, and Lemma TR is
that estimate. CODEX_REVIEW_THETAW F10 as quoted in REVIEW55_TUNIF W4 (Σ-aggregation endpoint costs k): **AGREE for Σ**; the
♯ pair uses a max. KFACTOR55: §9 — agree on every statement about the source; disagree with its bottom line that the uniform
estimate is open (it is proven at critical points here), and with "genuine" in its KF-F2 verdict; it was right where I was
silent ([A^T, χ]A, C3) and more careful on Balaban's thresholds (C19).

**Erratum to §4's constant A_j (self-check after §10).** The level-0 plain slot of S* carries both the Wilson plain row and
R^B_0, so its a-priori size is (A_W + A_B)η², not max(A_W, A_B)η². Read **A_j := C_f·(A_A + A_W) with A_A := A_B**, i.e.
A_j := C_f(A_B + A_W), everywhere A_j appears (TR-1 to TR-4, K_Pc, K_Σ, COF-crit♯♯). This only enlarges a k-independent
constant; kf55_1 treats A_j as a free positive parameter, so its verdicts are unaffected.
(The symbol "A_A" in the erratum line above is a typing slip, not a new constant: the definition is A_j := C_f(A_B + A_W).)

**Erratum to §7 (stat times, `TZ=UTC stat`).** checks/kf55_1_criteria.md born 2026-10-28T23:20:01Z (birth = mod);
checks/kf55_1.py born 23:20:27Z (26 s after the criteria; birth = mod); kf55_1_out.txt completed 23:21:37Z; kf55_1_err.txt
empty. "written and run 23:21Z" in §7 should read "written 23:20:27Z, run completed 23:21:37Z". Criteria-before-script holds.
No other repository file was written by this worker (checked with find -newer against the criteria file: every other newer
file belongs to other workers).
