Reviewer model: claude-opus-5-5

# BGT55 — (R2): background transfer of BFT-5 clause (b) from Z = 1 to a general small background Z = Z(V_k)

## PRE-STATED (written 2026-10-29 00:38 UTC, before any derivation in this file)

Role: worker (Opus 5.5), scope given by the lead. Write-set: this file and `checks/bg55_*` only. No git.

### Targets
- T1. State (R2) precisely: the exact inequality/identity clause (b) of BFT-5 (REVIEW_S22.md, located by
  string) needs at a general small background Z = Z(V_k); the frame/gauge in which it is posed; the norm
  (the orbit norm of GSHARP55's Proposition GF-DEP, located by string); the uniformity (in k, in T, in the
  background within the small-field set).
- T2. Build a background-covariant root-charge decomposition (CC-dec_Z) and a background EP-rec, and test each
  against the recorded defects: REVIEW55_BFTB REFUTED-list items 11 and 13 (root covariance of Q_l^Z; S^G
  not composite-co-closed at curved Z), HESSREL / CODEX_REVIEW_GAPZ F7 (naive relative-Hessian Neumann
  series fails at a pure gauge).
- T3. Find a transfer mechanism that does not use the refuted relative-Hessian series: (a) frame
  conjugation + perturbation in curvature, and/or (b) analyticity in the background with Cauchy estimates.
- T4. For each step: PROVEN-HERE (implication from named banked inputs, re-derived here), ARGUED, or OPEN,
  with the exact missing input named.

### What would count as a refutation of my own construction (stated in advance)
- R-a. A pure-gauge background Z = g·1 (curvature 0) at which the transferred bound would predict a
  nonzero change of a gauge-covariant quantity that is in fact only conjugated (the F7 failure mode): the
  transfer must give EXACT equality-up-to-conjugation at every pure gauge, else it is wrong.
- R-b. An explicit small-field background at which the constructed decomposition (CC-dec_Z) is not a
  decomposition (pieces do not sum to the identity / range is not complementary / a piece is not
  covariant under the background gauge action) — tested in exact rational arithmetic on a small model.
- R-c. Any step whose constant depends on k, T, or the volume when uniformity is claimed.
- R-d. Any step that silently uses (GAP-Z) or the refuted relative-Hessian Neumann series.
- R-e. Any step that needs an inverse bound where a condition-number bound (FWD-0) is the true requirement.

### Gate discipline
Any numeric check: `checks/bg55_<id>_criteria.md` with pre-registered PASS/FAIL written before the script;
exact rational arithmetic only (python fractions / sympy rationals), no floats for verdicts.

---

# FINDINGS (appended from 2026-10-29T01:2xZ; everything below was written after the PRE-STATED block)

## 1. Read record, and symbols pinned (systemic defect 1)

**Read (located by string; line numbers as of 00:40-01:25Z):** REVIEW_BRIEF_55 (all). REVIEW_S22.md l.373-435 (BFT statement;
"BFT-5 (linear stability at the background)" is at l.419). BFT_B.md §12.0-12.1 (l.1586-1632), §15.0-15.2 (l.2016-2109), §19.1-19.5
(l.2591-2645), §25.5 (l.3491-3517), §27.1-27.5 (l.3584-3628), §32 (l.3823-3862), §38.0-38.3 (l.4313-4360), §40-§41 (l.4447-4614).
BFT_A.md l.1-100 (§1-§2), l.187-320 (§3.8-§3.11). GSHARP55.md (all, 894 lines). CODEX_REVIEW_GSHARP.md (all 523 lines, read at
01:20Z; complete — ends with "Exactly what may be banked" item 7). COFUN_CC.md l.1-560. REVIEW55_BFTB.md l.268-370, 600-669.
HESSREL.md l.125-200, 353-548. CODEX_REVIEW_GAPZ.md (all; complete). BALABAN_EXTRACT.md l.48-480. KFACTOR_O55.md l.117-180,
l.225-235. KFACTOR_OFF55.md §2.1 (l.133-160). HIGHER55.md (all, in progress at 00:58Z; used only for its §2 verdict on Lemma SG).
CODEX_REVIEW_TOPCC.md l.255-300, 340-363. COFM55.md l.505-530. PLAN_S26.md l.1-80. PROOF.md l.1-60 (header incl. [S26-BANKED]).
NODEA_RES55, FLOW55 (first 2.5 kB each: not about (R2); not used).

**Collisions met, and the names used below.**
- **Z** names the background chain (BFT_B §38.1 "Background chain") — and, elsewhere, a level-(l+1) site in RT-cc's "ψ_l(Z)" (BFT_B
  l.3599), V^{-1}δV in Lemma SG (KFACTOR_OFF55 l.137), and Z_col (PROOF). **Here Z is only the background chain**; sites are X, Y.
- **T** is the coarse torus side. **My alignment map is called Υ** (never T).
- **E**: E_src (BFT_A l.449), E_Z (BFT_B §12.0), SG's E_l (KFACTOR_OFF55). **Mine is E_Υ := Υ^T H_Z Υ − H_1 ("aligned defect").**
- **δ**: HESSREL/FR-price's (δλ)(b) = (Ad_{Z(b)} − 1)λ(y′). **Mine is δ_Υ** (the bound on E_Υ).
- **m**: the weight rate, and Lemma TR's depth "m := k − 1 − l" (KFACTOR_O55 l.121). **Depth is q := k − 1 − l here** (GSHARP55's
  convention); m is only a weight rate.
- **ρ**: NA-alg's soft fluctuation; BFT_B's level step ρ_j = L^{−(k−j)}; RT-cc's multiplier ρ_l = κ_l r_l − s_l. **I write the level
  step as L^{−(k−j)} explicitly; ρ is the soft fluctuation; RT-cc's multiplier is written ρ^{RT}_l.**
- **θ** is always the class exponent of CC-INV/RT-cc (0 < α < θ < 1), never REVIEW_S22's θ_w.
- **N(S)**: COFUN_CC §1 "N(S) := ‖G^c_0‖_∞ + [G^c_0]_α + ‖j^c_0‖_∞ + ‖j‖_Pc + ‖G‖_Y + ‖s‖_R". **N_Z** below is its covariant version (§2.2).
- **Λ_0**: level-0 su(N)-valued functions vanishing at the level-k roots (BFT_B §12.0; at Z ≠ 1 there is no quotient by constants,
  BFT_B §40.2 consequence 1). **Λ_E(x)** = the S_E gauge function Σ_Xχ^5_Xλ^E_X(x) (BFT_B §15.0 writes Λ(x)), with Λ_EΞ_1 = −1 on Λ_0.
- **Ξ_1, Ξ_Z**: Ξ_Zλ := (d_{Z_l} ev^{(l)}λ)_{l<k} (BFT_B §38.1), Ξ_1 the same at Z = 1. **cc_1 / cc_Z**: S with Ξ_1^T S = 0 /
  Ξ_Z^T S = 0 on Λ_0 (composite co-closedness at 1 / at Z).
- **𝔐^∇** is BFT_A §1.4's norm (residual term L^{k−1−j}‖r^c_j‖_∞). **|||·|||_♯** (new, §6.2) is 𝔐^∇ with the residual term replaced by
  max_j L^{(1+θ)(k−1−j)}‖r^c_j‖_∞. Covariant versions carry a subscript Z.

## 2. T1 — (R2) stated precisely

### 2.1 What clause (b) is at Z = 1 now (inputs, with their status as read)
- **Gauge-invariant half: banked.** PROOF.md l.12 "[2026-10-29T00:15Z] Gauge-invariant half of BFT-5 clause (b) at the trivial
  background": for every Setting LIN^cc source with B_k = 0, ‖f_0‖_∞ + [f_0]^∞_α + κ_+‖r_{k−1}‖_∞ + ‖x‖_inv ≤ C·N(S), uniformly in
  k ≥ 1, T ≥ 1 and admissible gauge fixing (CC-INV, TOP-cc; CODEX_REVIEW_TOPCC "Exactly what may be banked" item 3). Also with N_Σ, Ñ_Σ.
- **Field half: CONFIRMED by Codex** (CODEX_REVIEW_GSHARP "Exactly what may be banked" items 1, 2, 4, read 01:20Z):
  ‖x_E(S)‖_{𝔐^∇} ≤ C_GF·N(S) on S_E, Z = 1, m = 0, 0 < α < θ < 1, and the same for the orbit norm ‖[x]‖_{𝔐^∇} :=
  inf_{λ∈Λ_0}‖x + Ξ_1λ‖_{𝔐^∇}, which is equivalent to the S_E norm up to C_Π (EP-bd). Not yet in PROOF's header when I read it.
- **Weighted half: COFM55 (CC-INV_m), Codex check running** — not used here except as a named prerequisite in §7.
I write **C_b** for the resulting constant: ‖[x]‖_{𝔐^∇} + ‖x‖_inv ≤ C_b·N(S) for every cc_1 source S (Z = 1, m = 0).

### 2.2 The statement
> **(R2) — BFT-5 clause (b) at a background.** Fix d = 4, odd L ≥ 3, κ_±, 0 < α < θ < 1. There are ε_b > 0, C_b′ < ∞ and T_b,
> depending only on (N, L, κ_±, α, θ), such that for every k ≥ 1, every coarse side T ≥ T_b, every level-k field V in the class
> 𝒦(ε), ε ≤ ε_b (real, and on BFT-2's complex ball |z|_∞ ≤ r_ℂε), and the composite critical background Z = Z(V) of BFT-0
> (any gauge representative):
> **(a)** Ker H_Z = Ran Ξ_Z on {x_k = 0} (this is (N1-nd), BFT_B §40.3);
> **(b)** for every S ∈ cc_Z, the response set {x : H_Z x = S} is non-empty, equals x_* + Ran Ξ_Z, and its **covariant orbit norm** obeys
>   ‖[x]‖_{𝔐^∇_Z} := inf_{λ∈Λ_0}‖x + Ξ_Zλ‖_{𝔐^∇_Z} ≤ C_b′·N_Z(S),
> uniformly in k, T and V. Here H_Z = Hess(𝔉_k(e^· Z; V))(0) (left-trivialised at base sites; BFT_B Setting GI without the Feynman
> term), 𝔐^∇_Z is BFT_B §12.0's covariant local-sup norm (transported differences, Campanato oscillations of values transported to
> the box corner along fixed axial paths in Z, residuals r^Z_j = the linearisation at Z of the root-map residual), and
> **N_Z(S) := inf over covariant slot representations S_l = d_{Z,l}^T G_l + j_l + (linearised-residual-type pairings ⟨s_l, r^Z_l(·)⟩)
> of COFUN_CC's N-expression**, with [G^c_0]_α taken covariantly (sup terms are Ad-invariant and need no transport).

*Which norm.* The orbit norm is forced: GSHARP55 Proposition GF-DEP (Codex-CONFIRMED) shows that no field bound can be uniform over
all admissible gauge fixings, already at Z = 1. A slice form follows from (b) on any slice whose projection along Ran Ξ_Z is bounded
in 𝔐^∇_Z; for S_E^Z that is (N1-c) (BFT_B §40.1), not proven at Z ≠ 1 (CODEX_REVIEW_GSHARP §8: "no background orbit-norm
equivalence"). **So the statement consumers can rely on is the orbit form (b); the slice form is (b) + (N1-c).**

*What (R2) presupposes.* BFT-0 at V (existence of the critical background Z(V)). On 𝒞_glob that is Theorem BA (BFT_A §3.9, PROVEN as an
implication of (H-lin^∇), (H-rem^∇), (FP♯′)); outside 𝒞_glob it is OPEN (needs (G♯-patch), BFT_A §3.10). (R2) adds nothing to that and
cannot be stated without it.

*Weighted form (not in scope).* The same with e^{m·dist} weights, 0 ≤ m ≤ m_Y, and weighted N_{Z,m}.

### 2.3 Lemma OC (the statement is frame-free). PROVEN-HERE
For a chain gauge ĥ (level-0 group-valued, acting on Z at every level through the roots and on V through ev^{(k)}ĥ):
H_{Z^ĥ} = M_ĥ H_Z M_ĥ^{−1}, Ξ_{Z^ĥ} = M_ĥ Ξ_Z (M^{fn}_ĥ)^{−1}, ‖M_ĥx‖_{𝔐^∇_{Z^ĥ}} = ‖x‖_{𝔐^∇_Z}, N_{Z^ĥ}(M_ĥ^{−T}S) = N_Z(S),
where (M_ĥx)(b) := Ad_{ĥ(base b)}x(b) (level-l links through the level-0 root of their base), M^{fn}_ĥ the same on functions.
*Proof.* Gauge invariance of 𝔉_k (TOWER-VAR) gives 𝔉_k(e^{M_ĥx}Z^ĥ; V^ĥ) = 𝔉_k(e^xZ; V), hence the first identity (differentiate twice;
this is HESSREL Lemma HR-1 at a general Z). Lemma CONJ (i)-(ii) (BFT_B §41.1) computed for a general background: d_{Z^ĥ}M^{fn}_ĥ =
M_ĥ d_Z (one line: Ad_{ĥ(y)Z(b)ĥ(y′)^{-1}}Ad_{ĥ(y′)} = Ad_{ĥ(y)}Ad_{Z(b)}), which gives the second. The norms are built from
Ad-invariant pointwise sizes of transported differences; transporting in Z^ĥ instead of Z rotates every transported value by the
same Ad_{ĥ(corner)}. ∎ **Consequence: (R2) at (Z, V) ⟺ (R2) at (Z^ĥ, V^ĥ) with the same constant. No frame or gauge enters the
statement; frames enter only proofs.** (bg55_ga A1 checks the M_G-intertwining exactly at a pure gauge, both models.)

### 2.4 Who consumes (R2), and in which form (located; quoted, not re-judged)
GSHARP55 §4.1 lists four consumers. At Z ≠ 1: **SF (a5-G♯) → HIST Theorem A5** ((G♯) at real critical chains; slice a choice); **B-NA-red**
(IFT for the SU(N) background, any linear slice with (FP♯′)); **BFT-3 locality / (N-bg) at V ≠ 1** (through H_{Z(V)}^{-1} applied to data
and to third-derivative sources; weighted). BFT-0/1/2 on 𝒞_glob do **not** consume (R2): Theorem BA's contraction is centred at the trivial
chain and inverts H_1 (BFT_A §3.9, "COMP with 𝔊_k := 𝓛^{-1}"). Outside 𝒞_glob, BFT-0 needs (G♯-patch), which is a statement about local
problems in local gauges, i.e. about (R2)-type estimates on boxes.

### 2.5 The background class is not a small-connection class
𝒦(ε) bounds the **curvature** (max_P|log V_P| ≤ ε), not the connection. Two consequences, both used below:
- On a torus of coarse side T, the holonomy of a loop of coarse size R is O(εR²) and is unconstrained once εR² ≳ 1; for flat V it is
  arbitrary (constant commuting links). So **no gauge makes log Z small on all of 𝒦(ε)** (SF's BNA-F4; HESSREL §H4.5; BFT_B §41.1 reading).
- 𝒞_glob(ε) (BFT_A §1.2: ‖B_k‖_D ≤ ε in one global gauge) is the subclass on which a global small-connection gauge exists. A flat V with
  holonomy θ around a cycle of coarse length T lies in 𝒞_glob(ε) iff (roughly) θ/T ≲ ε.
**Any transfer that is a single global perturbation of H_1 can therefore at best cover (gauge orbits of) 𝒞_glob-type backgrounds;
the rest of 𝒦(ε) needs a local-to-global step (§7).**

## 3. Exact identities at every critical background (Tier A; no smallness, no frame)

Setting: Z a critical point of E_Z(x) := 𝔉_k(e^xZ; V) in x (all levels l < k, x_k = 0), U_l(b) = e^{x_l(b)}Z_l(b) left-trivialised at the
base site; composite gauges g = e^{tλ} with g_l = ev^{(l)}g.

### 3.1 Lemma KER_Z. PROVEN-HERE. **H_Z Ξ_Z = 0 on Λ_0** (critical, not necessarily minimal, background).
*Proof.* For λ ∈ Λ_0 (so g is trivial at level k and V is not moved) and y ∈ X let x(s, t) be the coordinates of (e^{sy}Z)^{e^{tλ}}
relative to Z. Gauge invariance gives E_Z(x(s, t)) = E_Z(sy) for all small s, t, so ∇E_Z(x(s,t))·∂_tx(s,t) = 0. Differentiate in s at
(0, 0): H_Z(y, ∂_tx(0,0)) + ∇E_Z(0)·∂_s∂_tx(0,0) = 0. The second term vanishes at a critical point, and ∂_tx(0,0)(b) =
d/dt log(e^{tλ(y)}Z(b)e^{−tλ(y′)}Z(b)^{−1})|_0 = λ(y) − Ad_{Z(b)}λ(y′) = −(d_Zλ)(b). So H_Z(y, Ξ_Zλ) = 0 for every y. ∎
(No positivity is used; HESSREL Lemma HR-1 is the special case of a pure gauge.)

### 3.2 Lemma SF_Z (root charges of a response are the divergence of its own top multiplier current). PROVEN-HERE
Let F(x, v) := 𝔉_k(e^xZ; e^vV) (v a level-k 1-form, left-trivialised) and **b_Z(y) := −∂_x∇_vF(0,0)[y]** (a level-k 1-form, linear in y;
only the top soft term κ_{k−1}Σ_cφ̂_c(M̄(U_{k−1}); U_k) contributes). Then for every chain y with y_k = 0:
  **D_Z(H_Zy) := Ξ_Z^T H_Z y = ev^{(0→k)T} d_V^T b_Z(y)**  (as a level-0 function, pointwise),
so D_Z(H_Zy) is supported on the level-k roots, and for a cc_Z source S with response x, **q_Z(S) = d_V^T b_Z(x)** exactly.
*Proof.* Now let λ be an arbitrary level-0 function; g = e^{tλ} moves the data: 𝔉_k(U^g; V^{g_k}) = 𝔉_k(U; V). With x(s,t) as in 3.1 and
v(t) the coordinates of V^{e^{tλ_k}} (λ_k := ev^{(k)}λ), F(x(s,t), v(t)) = F(sy, 0). Differentiating in t and then in s at (0,0), and using
∇_xF(0,0) = 0: −H_Z(y, Ξ_Zλ) + ⟨∂_x∇_vF(0,0)[y], v′(0)⟩ = 0 with v′(0) = −d_Vλ_k (here Ξ_Zλ includes the root values of λ). Hence
⟨Ξ_Z^TH_Zy, λ⟩ = ⟨b_Z(y), d_Vλ_k⟩ = ⟨ev^{(0→k)T}d_V^Tb_Z(y), λ⟩ for every λ. ∎
*At Z = 1, V = 1* (quadratic part, φ̂ ≈ ½|ρ|²): b_Z(y) = κ_{k−1}r_{k−1}(y), which is COFUN_CC's Lemma SF ("D(Hx) = κ_{k−1}ev^{(0→k)T}d*r_{k−1}(x)").
*At Z ≠ 1* there is no total-charge constraint (⟨D_Z(H_Zy), 1⟩ = ⟨b_Z(y), d_V1⟩ and d_V1 ≠ 0 at a curved V), consistent with BFT_B §40.2
consequence 1. The size of b_Z(y) is κ_{k−1}(1 + O(ε))|r^Z_{k−1}(y)| + O(ρ_{k−1}(Z))|y_{k−1}| (from the second derivatives of φ̂ at the
background; **ARGUED**, constants not computed). **Status of the identity: PROVEN-HERE (exact, Tier A).** It is the background version of
the self-current of COFUN_CC §2.6, and it is the one root-charge current that exists at every background without any estimate.

### 3.3 Lemma FG_Z (orbit uniqueness and gauge-fixing independence). PROVEN-HERE given (N1-nd)
If Ker H_Z = Ran Ξ_Z (on {x_k = 0}), then for S ∈ cc_Z: Ran H_Z = Ann(Ker H_Z) = cc_Z (H_Z symmetric, finite dimension), so H_Zx = S is
solvable with solution set x_* + Ran Ξ_Z; for every linear Γ with ΓΞ_Z invertible on Λ_0 the Γ-response is the unique solution with
Γx = 0. The orbit, hence ‖[x]‖_{𝔐^∇_Z} and every Ξ_Z-invariant output, is Γ-independent. ∎ (BFT_A Lemma FG (iii) verbatim at Z; the only
input is the kernel clause, which §4 shows is an **output** of the transfer, not an extra hypothesis.)

## 4. T3 — the transfer mechanism: gauge-aligned congruence (Theorem GA)

### 4.1 Theorem GA. PROVEN-HERE (exact linear algebra; bg55_ga A2-A7 PASS, controls C1-C6 FIRE)
*Data.* A finite-dimensional real (or complex) space X; Λ := Λ_0; injective Ξ_1, Ξ_Z : Λ → X; symmetric H_1, H_Z : X → X* with
H_1Ξ_1 = 0 and H_ZΞ_Z = 0 (Lemma KER_Z). Norms: a response norm |||·|||_1 on X and its orbit seminorm [x]_1 := inf_λ|||x + Ξ_1λ|||_1 (a norm
on X/Ran Ξ_1); likewise |||·|||_Z, [·]_Z for Ξ_Z; source norms N on cc_1 and N_Z on cc_Z (cc_• := Ann(Ran Ξ_•)).
*Hypotheses.*
- **(B_1) [clause (b) at Z = 1].** Ker H_1 = Ran Ξ_1, and every solution of H_1x = S, S ∈ cc_1, has [x]_1 ≤ C_b·N(S).
- **(A1) [a bounded aligned congruence].** An invertible linear Υ : X → X and an invertible A : Λ → Λ with **ΥΞ_1 = Ξ_ZA**, such that
  [Υx]_Z ≤ t_+[x]_1 for all x, and N(Υ^TS) ≤ t_*N_Z(S) for all S ∈ cc_Z.
- **(A2) [small aligned defect].** E_Υ := Υ^TH_ZΥ − H_1 obeys N(E_Υx) ≤ δ_Υ[x]_1 for all x, with C_bδ_Υ < 1.
*Conclusions.*
- **(i)** E_ΥΞ_1 = 0 and Ξ_1^TE_Υ = 0: **E_Υ maps X/Ran Ξ_1 into cc_1** (whatever Υ is, provided it aligns).
- **(ii)** Υ^T maps cc_Z into cc_1.
- **(iii)** Ker H_Z = Ran Ξ_Z — **(N1-nd) at Z is an output.**
- **(iv)** For every S ∈ cc_Z, H_Zx = S is solvable, uniquely modulo Ran Ξ_Z, and **[x]_Z ≤ t_+t_*·C_b/(1 − C_bδ_Υ)·N_Z(S).**
*Proof.* (i) E_ΥΞ_1 = Υ^TH_ZΞ_ZA − H_1Ξ_1 = 0; E_Υ is symmetric, so Ξ_1^TE_Υ = (E_ΥΞ_1)^T = 0, i.e. Ran E_Υ ⊂ cc_1.
(ii) Ξ_1^TΥ^TS = (ΥΞ_1)^TS = A^TΞ_Z^TS = 0.
(iii)-(iv) Put H′ := Υ^TH_ZΥ = H_1 + E_Υ; H′Ξ_1 = 0. On Q := X/Ran Ξ_1 (normed by [·]_1) H_1 induces a bijection h_1 : Q → cc_1 (by (B_1),
Ran H_1 = Ann(Ker H_1) = cc_1), with ‖h_1^{-1}‖_{N→[·]_1} ≤ C_b; E_Υ induces e : Q → cc_1 with ‖e‖ ≤ δ_Υ (by (i) and (A2)). Then
h′ = h_1(1 + h_1^{-1}e) with ‖h_1^{-1}e‖_{Q→Q} ≤ C_bδ_Υ < 1, so h′ : Q → cc_1 is a bijection with ‖h′^{-1}‖ ≤ C_b/(1 − C_bδ_Υ). Hence
Ker H′ = Ran Ξ_1 and Ker H_Z = Υ Ker H′ = ΥRan Ξ_1 = Ran Ξ_ZA = Ran Ξ_Z (Υ^T invertible). For S ∈ cc_Z: H_Zx = S ⟺ H′(Υ^{-1}x) = Υ^TS,
and Υ^TS ∈ cc_1 by (ii); so u := Υ^{-1}x exists, is unique modulo Ran Ξ_1, and [u]_1 ≤ C_b(1 − C_bδ_Υ)^{-1}N(Υ^TS). Since Υ maps
u + Ran Ξ_1 onto x + Ran Ξ_Z, [x]_Z ≤ t_+[u]_1 ≤ t_+t_*C_b(1 − C_bδ_Υ)^{-1}N_Z(S). ∎

*Uniformity.* Every constant in (iv) is one of C_b, t_±, δ_Υ; (R2)(a)-(b) follow with C_b′ = t_+t_*C_b/(1 − C_bδ_Υ) **as soon as (A1)-(A2)
hold with k-, T-, V-uniform t_+, t_*, δ_Υ**. The proof is the same at complex V (BFT-2's ball) and in weighted norms (it is a Neumann series
in whatever pair (B_1) is stated in).

### 4.2 What Theorem GA does not need — checked against the recorded defects
- **No relative-Hessian series, no (FWD-0).** (A2) bounds the aligned defect absolutely in the pair (orbit-response → source). The
  Neumann factor is C_bδ_Υ; ‖H_1‖ never appears. HESSREL's (FWD-0) (HESSREL l.193) and its condition number Λ_0M_0 arose only because
  HESS-rel bounded E relative to ‖H_1‖. **CODEX_REVIEW_GAPZ F7's witness** (H_0 = diag(1, n), E = diag(−1, 0)) is a failure of the
  relative form; an absolute (A2) with C_bδ < 1 excludes it by definition.
- **No unaligned difference.** The literal difference H_Z − H_1 is not cc_1-valued (bg55_ga C3a/C3b FIRE: (H_Z − H_1)Ξ_1 ≠ 0 at a pure gauge
  and at a curved background), so it cannot be fed to the cc-inverse at all; this is the precise algebraic content of F7's "gauge covariance
  is conjugacy, not equality". After alignment the defect is cc_1-valued **identically** (bg55_ga A4, A4′).
- **Only the cc-inverse at Z = 1 is used** — never a full (general-source) inverse. Codex F7's corrected arrow ("full matched flat inverse +
  aligned relative perturbation with δ < 1 ⇒ background inverse") is therefore sharpened: with an **exact** alignment ΥΞ_1 = Ξ_ZA, the
  cc-inverse suffices, because E_Υ and Υ^T land in cc_1 automatically ((i), (ii)). This matters: CODEX_REVIEW_GSHARP §8 records that the
  general-source bound "N(Π_E^Ty) ≤ C‖y‖ does not follow" — GA never asks for it, provided (A1)-(A2) are proved for the chosen Υ.
- **No (CC-dec_Z).** Root charges at Z are never decomposed: Υ^T carries cc_Z sources into cc_1 (ii), and at Z = 1 the banked CC-INV handles
  cc_1 sources with their root charges (FLUX/DEC/TOP-cc at Z = 1). What replaces (CC-dec_Z) is the source half of (A1), N(Υ^TS) ≤ t_*N_Z(S).
- **No (EP-rec)_Z.** The field half at Z comes from the field half at Z = 1 (GF-E) through t_+; no covariant reconstruction is used.
- **No (N1-nd) as an input** ((iii)), and **no (GAP-Z)** as an input: (iv) *is* a (GAP-Z)-type statement on cc_Z, as an output.
- **No slot decomposition at Z.** REVIEW55_BFTB REFUTED-items 13 (S^G not composite-co-closed at curved Z) and 10/11 (Q_l^Z root covariance)
  concern slot-wise transport of the Z = 1 proofs; GA never splits a source at Z into slots. Where those defects reappear is inside the size of
  E_Υ (§6), not in the algebra.

### 4.3 Proposition GA-slice (the naive slice series is the special case Υ = 1 on a slice). PROVEN-HERE (exact)
Let Λ_W : X → Λ be any map with Λ_WΞ_1 = −1 (W := Ker Λ_W is then a complement of Ran Ξ_1; Λ_W = Λ_E gives S_E), and put
**Υ_W := 1 − (Ξ_Z − Ξ_1)Λ_W.** Then Υ_WΞ_1 = Ξ_Z (A = 1); Υ_W = 1 on W; Υ_W is invertible iff Λ_WΞ_Z is invertible on Λ; and for u ∈ W,
  **E_{Υ_W}u = Π_W^T(H_Z − H_1)u,  Π_W^T := 1 + Λ_W^TΞ_1^T,  Υ_W^TS = Π_W^TS for S ∈ cc_Z.**
*Proof.* Υ_W^T = 1 − Λ_W^T(Ξ_Z − Ξ_1)^T, and Ξ_Z^TH_Z = 0, Ξ_Z^TS = 0, Ξ_1^TH_1 = 0. ∎
*Reading.* With W = S_E, GA's series is exactly "solve the S_E-slice problem for H_Z by a Neumann series around the S_E-slice inverse of
H_1", and the two quantities GA must bound are N(Π_E^T(H_Z − H_1)u) and N(Π_E^TS) — i.e. the S_E completion Λ_E^TD_1(·) of the flat composite
divergence D_1 := Ξ_1^T of the perturbation and of the source. §6.4 shows by power count that this completion is **not** k-uniform at levels
l ≥ 1 (it reproduces the root-funnel spikes), so the S_E alignment is the wrong Υ for the multi-level problem; Theorem GA itself is unaffected.
(bg55_ga A3 checks Υ_WΞ_1 = Ξ_Z, A7 checks Υ_W invertible, both models/backgrounds where run.)

### 4.4 Corollary GA-PG ((R2) at every pure-gauge background, of any size). PROVEN as an implication
Let G be any chain gauge (level-0 SU(N)-valued, levels l ≥ 1 through the roots) and V = 1^{G_k}; by gauge covariance of the critical set
(and BFT-0's uniqueness modulo composite gauges trivial at level k) Z(V) = 1^G. Take **Υ := M_G, A := M^{fn}_G.** Then ΥΞ_1 = Ξ_ZA (Lemma OC
with Z = 1), E_Υ = M_G^TM_GH_1M_G^{-1}M_G − H_1 = **0 exactly** (Lemma OC: H_{1^G} = M_GH_1M_G^{-1}; M_G orthogonal), t_+ = t_* = 1 (Lemma OC:
M_G is an isometry from the flat to the covariant norms). Theorem GA gives (R2)(a)-(b) at Z = 1^G **with C_b′ = C_b, for every G, however
large.** Inputs: (B_1) = CC-INV (banked) + GF-E (CODEX_REVIEW_GSHARP item 2). ∎
This is the refutation test R-a of the PRE-STATED block, passed: **at every pure gauge the transfer is exact**, while the unaligned
difference is O(1) (bg55_ga C4 FIRES: H_Z − H_1 ≠ 0 at a pure gauge with all plaquette holonomies = 1; A6 PASS: E_{M_G} = 0 exactly). It also
shows that the background deviation that GA must price is **curvature plus the failure to choose Υ covariantly**, not the connection.

### 4.5 Check bg55_ga (record)
Criteria `checks/bg55_ga_criteria.md` written 01:05:26Z, before the script (`checks/bg55_ga.py`, written 01:08:33Z, one in-place restructuring
of its curved-background part at 01:09:38Z for speed — skinny products instead of a dense 540×540 triple product — before any run). **One run**,
01:09:45-01:09:46Z, `nice 10`, `python3 -I`, thread variables 1, exact ints/Fractions only; 1.40 s, 29.0 MB peak (`checks/bg55_ga_out.txt`,
`checks/bg55_ga_err.txt` = /usr/bin/time report, `checks/bg55_ga_time.txt`). No criterion edited.
- **PASS (exact), both models M1 (k = 1, T = 2, dim X = 216, dim Λ_0 = 96) and M2 (k = 2, T = 1, dim X = 540, dim Λ_0 = 240):** pre-checks
  (flat and covariant spanning-tree left inverses, H_1Ξ_1 = 0); A1 (Lemma OC/CONJ at PG: Ξ_ZM^{fn}_G = M_GΞ_1 and H^cov_Z = M_GH_1M_G^T);
  A2 (H_ZΞ_Z = 0, PG and CV); A3 (alignments M_G and Υ_W); A4 (E_ΥΞ_1 = 0 and Ξ_1^TE_Υ = 0); A5 (Υ^T maps 6 random cc_Z sources into cc_1);
  A6 (E_{M_G} = 0 exactly). M1 only: A4′ (full-matrix version at CV), **A7 (Υ_W invertible, rank 216/216, and x := Υ_Wu solves H_Zx = S
  exactly for 3 random cc_Z sources at PG and at CV, with u from an exact Bareiss solve of [H_1 + E_Υ + Λ_W^TΛ_W]u = Υ^TS)**.
- **All controls FIRE:** C1 (at CV the covariant quadratic form H^cov_Z has H^cov_ZΞ_Z ≠ 0: the B1/B2 defects are real in the model), C2
  (E_{Υ_W} ≠ 0 at PG, nnz 7504 / 26435), C3a/C3b, C4 (H_Z − H_1 ≠ 0 with every plaquette holonomy = 1), C5 (a random non-cc vector is not sent to
  cc_1), C6 (a non-left-inverse 2Λ_W breaks alignment and E_ΥΞ_1 ≠ 0).
- Informational I1: rank H_Z = 120 = dim X − dim Λ_0 at PG and CV (M1), i.e. Ker H_Z = Ran Ξ_Z there.
- **What it cannot decide** (stated in the criteria before running): no size, no uniformity, no d = 4 arithmetic; the CV H_Z is an artificial
  gauge-degenerate form (P_Z^TH^cov_ZP_Z), not a critical-point Hessian; Q = Q_ax, not lane A's S4′ average. It tests the algebra of Theorem
  GA and Proposition GA-slice, Lemma OC at a pure gauge, and that a wrong alignment or no alignment is detected.

## 5. T2 — (CC-dec_Z) and (EP-rec)_Z, built and checked against the recorded defects

### 5.1 (CC-dec_Z) in the direct form (COFUN_CC l.445: "at Z(V_k) every composite-co-closed source is a (CC-0)_Z source plus a datum with a bounded flux, up to priced defects")
**(a) Exact skeleton. PROVEN-HERE.** For a level-k current b let T^Z_b be the source y ↦ ⟨b, b_Z(y)⟩ (b_Z of Lemma SF_Z). Differentiating the
gauge identity ∇_xF·X_Uλ + ∇_vF·X_Vλ_k = 0 once in v at (0, 0) and using symmetry of mixed partials gives
  ⟨T^Z_b, Ξ_Zλ⟩ = ⟨𝒟_Z^T b, λ_k⟩,  **𝒟_Zμ := Hess_{vv}F(0,0)·d_Vμ − (∇_vF(0,0)·D_vX_Vμ)^♯**,
so D_Z(T^Z_b) = ev^{(0→k)T}𝒟_Z^Tb is root-supported. At Z = 1: 𝒟_1 = κ_{k−1}d (COFUN_CC Lemma TS/DEC). At Z: 𝒟_Z = κ_{k−1}d_V up to terms
proportional to the background's top fluctuation (∇_vF(0,0) is the background top force). Hence **S = S′ + T^Z_b with S′ (CC-0)_Z ⟺
𝒟_Z^T b = q_Z(S)** (q_Z(S)(X) := D_Z(S) at the root of X). Everything hinges on a bounded solution b.
**(b) The two candidate currents.**
- *Self-current (exact).* Lemma SF_Z gives q_Z(S) = d_V^Tb_Z(x(S)) — a current whose size is the response's own top multiplier. It exists
  for every background but is bounded only if the response is: circular for proving (R2).
- *Covariant face flux (explicit).* Φ^Z_l j(X, μ) := the sum over level-l links b leaving B_l(X) through its upper μ-face of T(b)j(b), T(b) the
  transport to the root of X along the fixed-order axial path in Z. The flat identity "block sum of d*j = net face flux" (COFUN_CC Lemma FLUX
  (i)) acquires an **interior-link defect** Δ_l(X) = Σ_{b interior}(T_{y′}Ad_{Z(b)}^{-1} − T_y)j(b) and a face-transport mismatch. With fixed-order
  axial transports the loop closed by an interior link is a strip of width 1 and own length ≤ (d−1)L^{k−l}, so |T_{y′}Ad^{-1} − T_y| ≤
  c_N(d−1)L^{k−l}·L^{−2(k−l)}f_l; with ≤ dL^{4(k−l)} interior links and |j|_own ≤ L^{−3(k−l)}π_l(j): **|Δ_l(X)| ≤ c_Nd(d−1)f_l·π_l(j_l) per
  level-k block** (face mismatch: loops of area ≲ L^{2(k−l)} own plaquettes, the same order). **ARGUED** (holonomy-area bound for lattice loops
  is standard; constants not computed).
**(c) Why the flux route does not close.** The residual root charge Δ is O(f_k)·c(S) **per site, with no sign structure**. A bounded b′ with
d_V^Tb′ = Δ requires the cut condition |Σ_{X∈A}Δ(X)| ≤ C|∂A| for every region A (Gale / max-flow min-cut, as COFUN_CC §2.2 uses it); a per-site
bound gives only C f_k|A|c(S), which exceeds C|∂A| on regions of coarse size ≳ 1/f_k. (PROVEN-HERE as a statement about what a per-site bound
can give.) By Lemma SF_Z, Δ = d_V^T(b_Z(x(S)) − Φ^Z(j)) does have a flux, of the size of the response's top multiplier. **So on the direct route
(CC-dec_Z) with a bounded datum is equivalent to the top-residual part of (R2) itself; it cannot be proved first.**
**(d) On the GA route it is not needed** (§4.2): Υ^T carries cc_Z into cc_1 and the banked CC-INV decomposes root charges at Z = 1. What replaces
it is (A1)'s source bound N(Υ^TS) ≤ t_*N_Z(S), analysed in §6.4.

### 5.2 (EP-rec)_Z (GSHARP55 §5.4), ingredient by ingredient
- *(i) EP-int at Z* (covariant Weitzenböck, interior Schauder in a frame). Needs the background C^{1,α}-small in a box frame. Corollary CL-iv
  supplies that for the lane's **lift Z^off** (BFT_B §25.5), not for the **critical background Z(V)**; for Z(V) it needs either the lift-centred
  BFT-0 (Z(V) = e^XZ^off(V), X small; OPEN outside 𝒞_glob) or a local Coulomb gauge (UHL) (BFT_A §3.10, OPEN). The Neumann step itself is
  Lemma FR-price, **NOT-VERIFIED** (REVIEW55_BFTB F13: ℓ²-relative size ≍ n·f unless the Coulomb structure is used) — I agree with F13.
- *(ii) LR-pot at Z.* Loops lie in B(X) ∪ B(X + e_μ) (BFT_A l.1118-1119); each picks up holonomy O(f). ARGUED (BFT_B §41.7 says the same).
- *(iii) Lemma Λ at Z* uses root covariance of Q^Z. **REVIEW55_BFTB REFUTED-item 11 is right about the operator Q_l^Z** (contour-holonomy spread
  ≠ 0 on straight-row towers), and its Finding 10 (c) is the load-bearing precision: the defect is bounded relative to the **values** lam_{l+1},
  not to d_Z ev λ. In Lemma Λ the values are those of the box gauge function, bounded by (N1-b)'s sup|λ^{E,Z}| ≤ 4C_E n(x); the defect then
  costs Σ_l CL^{−(k−l−1)}f_k·4C_E n(x) in coarse units — geometric. **GSHARP55's "That defect is summable in l": CONFIRMED with that precision**,
  and inheriting (i)'s status through (N1-b).
- *(iv) Q-hold at Z*: averages of transported translates; ARGUED.
- Item 13 (S^G not cc at Z) does not touch EP-rec (no sources).
**Verdict:** "(EP-rec)_Z … ARGUED — an outline only" — **CONFIRMED as the honest status** (agree with CODEX_REVIEW_GSHARP §8). "It does not need
(GAP-Z)" — **CONFIRMED** (a reconstruction). "No global patching is needed" — CONFIRMED for the reconstruction; but its inputs ‖x‖_{inv,Z},
N^Z_res(x) are the global gauge-invariant half at Z, so the global problem moves, it does not disappear. **On the GA route (EP-rec)_Z is not used.**

### 5.3 The task's defect list, item by item, against GA
- **REVIEW55_BFTB item 11 (root covariance of Q_l^Z).** Correct for Q_l^Z. But the Hessian at a critical background is built from the **true**
  linearisation of the soft fluctuation ρ_c = log(V^{-1}W_0(M̄_c(U_l))) (NA-alg (b)), and ρ is **exactly** covariant: M̄_c(U^g) =
  g(c_X)M̄_c(U)g(c_{X′})^{-1} (root-to-root contours), W_0(gMg′^{-1}) = gW_0g′^{-1}, V^g = g(c_X)Vg(c_{X′})^{-1}, so ρ(U^g) = Ad_{g(c_{X′})}ρ(U).
  Linearising at the background: **Dρ(z)·Ξ′_zλ = [λ(c_{X′}), ρ(z)] exactly** (PROVEN-HERE, one line). So on any route that uses the true Hessian
  (GA does), the "root-covariance defect" is the commutator with the **background fluctuation**, which Lemma TR's (TR-1) controls; the
  contour-spread defect of item 11 arises only on routes that replace D log M̄(z) by the transported average Q_l^Z (BGD, TRANSP).
- **REVIEW55_BFTB item 13 (S^G not composite-co-closed at curved Z).** Re-derived: D_Z(d_Z^TG) = (d_Zd_Z)^TG, nonzero by BGD (a) — **CONFIRMED**.
  Irrelevant to GA (no slot split at Z). In N_Z a G-slot need not be cc_Z (only the total source is). On a localisation route (§7) its bulk
  divergence, own size ≤ c_NC_NL^{−2(k−l)}f_k sup_own|G_l|, can be routed to the level-k roots by a covariant spreading current of coarse plain
  size O(f_k)‖G^c‖ — **no per-cube neutrality is needed, because root charges are allowed in cc_Z** (ARGUED; this answers the "per-cube
  neutrality ⟨G, d_Zd_Z1⟩ ≠ 0 … not automatic" of REVIEW55_BFTB Finding 11: it need not hold).
- **HESSREL / CODEX_REVIEW_GAPZ F7 (relative Hessian series; conjugacy not equality; FWD-0).** Excluded by construction (§4.2); exact at pure gauges
  (Corollary GA-PG).

## 6. The aligned defect on 𝒞_glob: what (A1)-(A2) need, term by term

### 6.1 Setting
V ∈ 𝒞_glob(ε) (BFT_A §1.2), global gauge; z := coordinates of the critical background in the trivial-chain chart, Z = e^z, with
**‖z‖_{𝔐^∇} ≤ η := C_0ε** (Theorem BA's conclusion; BFT-0 on 𝒞_glob is itself CONDITIONAL on (H-lin^∇), (H-rem^∇), (FP♯′)). Work with
H(z) := Hess_x𝔉_k(e^x; V)|_{x=z} and the gauge directions Ξ′_z at z in the same chart (H(z)Ξ′_z = 0 by Lemma KER_Z's proof); H_Z = J(z)^TH(z)J(z)
with J(z) the link-wise left-trivialisation Jacobian (1 + O(|z(b)|_own)), absorbed into Υ. H_1 is Setting LIN's quadratic form (independent of
the datum). D𝔑(z) := H(z) − H_1 is the Hessian difference in the fixed chart (the derivative of BFT_A's (H-rem^∇) remainder).

### 6.2 Corollary RW♯ (clause (b) at Z = 1 in the transport-weighted response norm). PROVEN as an implication
Put **|||x|||_♯ := ‖x‖_{𝔐^∇} + max_{0≤i≤k−2}L^{(1+θ)(k−1−i)}‖r^c_i(x)‖_∞ + N_res(x).** For every cc_1 source S in the N-class (B_k = 0):
  **‖[x]‖_{𝔐^∇} + max_i L^{(1+θ)(k−1−i)}‖r^c_i(x)‖_∞ + N_res(x) ≤ C_♯·N(S)**, uniformly in k ≥ 1, T ≥ 1.
*Proof.* Field part: GF-E (CODEX_REVIEW_GSHARP item 2). N_res: RHT-cc made absolute by TOP-cc (GSHARP55 §5.2 step 4; CODEX_REVIEW_GSHARP §3.1
re-derives it). Residual sup with the stronger weight: Lemma RT-cc (c) (CONFIRMED, REVIEW55_BFTB Finding 1) with Lemma TC's sup sizes (BFT_B §19.2,
valid for any current — KFACTOR_O55 Step 1), for 0 ≤ i ≤ k − 2, q = k − 1 − i:
  ‖r^c_i‖ ≤ κ_-^{-1}[‖s^c_i‖ + L^{−2q}(‖ρ^{RT}_{k−1}‖ + Σ_{l>i}(π_l(ĵ_l) + 6L^{k−l}‖G^c_l‖))],
and for S in the N-class: ‖s^c_i‖ ≤ L^{−θ}L^{−(1+θ)q}‖s‖_R; ‖ρ^{RT}_{k−1}‖ ≤ κ_+C_top N(S) + L^{−θ}‖s‖_R (TOP-cc); Σ_lπ_l(ĵ_l) ≤
(1 + 2d(1 − L^{−3})^{−1})|j|_Σ (Lemma FT (ii)), |j|_Σ ≤ K_θN(S); and Σ_{l>i}6L^{k−l}‖G^c_l‖ ≤ 6Σ_{l>i}L^{(1−θ)(k−l)}‖G‖_Y ≤
6L^{(1−θ)q}‖G‖_Y/(1 − L^{−(1−θ)}) (largest term at l = i + 1, θ < 1). Since L^{−2q} ≤ L^{−(1+θ)q}, every term is ≤ C·L^{−(1+θ)q}N(S). ∎
*Reading.* Responses at Z = 1 carry their residuals with own-unit decay rate 2 + θ (coarse rate 1 + θ), one θ above what 𝔐^∇ records; the
s- and G-slots cap the rate at 1 + θ, the plain currents and the top give 2. This is the form of KFACTOR_O55's "measure the residual in its
transport weight" that clause (b) supplies **for free** at Z = 1; it is needed in §6.3 (S2).

### 6.3 The terms of D𝔑(z)u, and their sizes in the pair (|||·|||_♯ → N)
Structure. Level 0: the Wilson part. Levels l ≥ 0: the soft part, which by **Lemma SG** (KFACTOR_OFF55 §2.1; identity CONFIRMED by HIGHER55 §2,
an Opus 5.5 check, no Codex check yet) is linear in Θ = e^ρ − 1 with analytic coefficients, and by the exact BCH factorisation
ρ_c = Ψ̃_c·r^{full}_c (r^{full}_c := log V − log M̄_c, Ψ̃ analytic, Ψ̃(0) = 1; f(h) := log(e^{−a}e^{a+h}) = ∫_0^1Df(th)dt·h) vanishes with the full
residual. Differentiating at z in direction u: Dρ(z)u = −Ψ̃(z)[r_l(u) + β_l(z, u)] + O(ρ(z))·u, with **β_l(z,·) = the derivative at z of the
second-order contour remainder of log M̄ (CEN2-small, BFT_A BA-4)**. Hence the soft part of D𝔑(z)u consists of, at each level:
| term | slot | own-unit size | N-size (k-, T-uniform?) | needs |
|---|---|---|---|---|
| W1 d^T(c_1(z,u)), c_1 = DF(z)u − du_0 (incl. CODEX GAPZ F8's ad_X/(e^{ad_X}−1) factor) | G_0 (sup + Hölder) | ≤ C|z_0||u_0| | ≤ Cη|||u|||_♯ ✓ | z ∈ C^{1,α} |
| W2 (∂_wc_1)^T(du_0 + c_1) | j_0 | ≤ C|z_0||du_0| | ≤ Cη|||u|||_♯ ✓ | — |
| W3 (D²F[u,·])^TF(z) | j_0 | ≤ C|u_0||F(z)| | ≤ Cη|||u|||_♯ ✓ | — |
| S1 κβ_l(z,u) | residual-type s_l | ≤ κp_L²·2CL·L^{−3(k−l)}η|||u||| | ‖·‖_R ≤ 2κCp_L²L^{θ−2}L^{−(1−θ)q}η ✓ geometric | **CEN2** (BA-4); with one contour instead of the S4′ average the weighted size grows like L^{θq} |
| S2 κ(∂_wβ_l(z,·))^Tr_l(u) (+ level-(l+1) part) | plain j_l | ≤ κCL·L^{−(k−l)}η·L^{−(2+θ)q}|||u|||_♯ | π_l ≤ κCL³L^{−θq}η|||u|||_♯ ✓ (Pc and Σ) | **|||·|||_♯** (Cor. RW♯); in plain 𝔐^∇: π_l ≤ κCL³η with **no decay**, Σ_l ≍ (k−1)η |
| S3 κ(D²ρ[u,·])^Tρ(z) (+ residual-type κO(ρ(z))u) | plain j_l, s_l | ≤ κC|u_l|·L^{−q}‖r^c_l(z)‖ | with (TR-1): π_l ≤ κCL²L^{−q}a_qη ✓, a_q = κ_-^{-1}[κ_+ + (2A_s + qA_j)η] | **(TR-1) at the background** (Lemma TR); with only the 𝔐^∇ weight: π_l ≤ κCL²η, **no decay** |
| higher order | all | O(η²)·(same structure) | ✓ by power count | SG's (LA-1)-(LA-3), ARGUED-standard |
Sizes: power counts **PROVEN-HERE** from the stated own-unit bounds (BA-4 polarised for β; SG's (LA-1) for the coefficients; RW♯ for r(u);
TR-1 for r(z)); the completeness of the term list and the analytic tails are **ARGUED** (they are BFT_A's (H-rem^∇) Lipschitz form, which BFT_A §3.9
itself labels ARGUED).
**Two findings, both new:**
- **(F-♯) The background transfer inherits the level-count currency issue (R4) and is cured by the same remedy.** In the plain 𝔐^∇ response norm the
  r(u)-linear term S2 has N_Σ-size ≍ (k − 1)η (upper bound; attained in order if u's residuals saturate the 𝔐^∇ weight at every level — ARGUED), so
  a Neumann series in (𝔐^∇ → N) would need (k − 1)η ≪ 1. In |||·|||_♯ it is k-uniform, and Corollary RW♯ shows clause (b) at Z = 1 already holds in
  |||·|||_♯. **So the transfer must be run in the transport-weighted response norm**, exactly as KFACTOR_O55 §(b)-(c) recommends for the contraction.
- **(F-TR) The background's own residual must carry Lemma TR's decay**: S3 is k-uniform only with (TR-1) at z (CONFIRMED at the quadratic level,
  CODEX_REVIEW_TR; higher order is HIGHER55's open obligation). (R2) therefore depends on HIGHER55's outcome through (TR-1), exactly as the critical-point
  row bounds do.

### 6.4 The completion step decides the alignment: S_E is the wrong Υ
By Proposition GA-slice, with Υ = Υ_W: E_Υu = D𝔑u + Λ_W^TD_1(D𝔑u) and Υ^TS = S + Λ_W^TD_1(S), D_1 := Ξ_1^T. **D_1 of each slot:** G-slots 0 (d^Td^T = 0
at Z = 1, exact); flat residual-type slots ⟨s, r_l(·)⟩: 0 for l ≤ k − 2 and root-supported at l = k − 1 (d^TQ^T = ev^Td^T, exact); **plain currents
j_l: ev^{(l)T}d^Tj_l ≠ 0** (the S2/S3 currents are BCH₂-row-type and not co-closed; BFT_A's V_l has d*V_l = d*R^B_l).
- **Level 0, W = S_E.** Λ_E^Td^Tj_0 = Σ_Xd(Δ^X_N)^{−1}(χ_X d^Tj_0) is a box-Neumann Hodge projection of j_0 plus the commutator −(∇χ_X)·j_0; with
  Schauder in C^α it is ≤ C(‖j^c_0‖_∞ + [j^c_0]_α) ≤ Cη|||u|||_♯ (W2, W3, S2/S3 level-0 parts are C^α because z ∈ C^{1,α} and N_res(u) ⊂ |||u|||_♯).
  **ARGUED** (box-Neumann Schauder; the LES-div type input).
- **Levels l ≥ 1, W = S_E: not k-uniform (power count).** ev^{(l)T}d^Tj_l is a field of point charges at the level-0 images of level-l sites, of own size
  ≤ 2dL^{−3(k−l)}π_l(j_l). Λ_E^T turns a point charge into the gradient of a lattice box-Neumann Green function at level 0, of own size ≍ the charge on
  the adjacent links, i.e. coarse plain size ≍ L^{3k}·2dL^{−3(k−l)}π_l = **2dL^{3l}π_l(j_l)** in the sup-measured (P0) slot. With S2's π_l this is
  ≍ κCL^{3+3l−θq}η, of order L^{3k}η at l = k − 1. **ARGUED** (needs no cancellation among charges within O(1) own distance and the O(1) size of the
  lattice Green-function gradient at distance 1; no explicit witness computed). This is the background form of the lane's recorded "root-funnel spikes
  in S_E are real" (BFT_B l.3575) and of CODEX_REVIEW_GSHARP §8 ("N(Π_E^Ty) ≤ C‖y‖ does not follow"). The same applies to Υ^TS for sources with level-l
  plain currents (the source half of (A1)).
- **What the alignment must do instead — named (ALIGN-ℓ), OPEN.** A left inverse Λ_W (Λ_WΞ_1 = −1) such that
  (α) ‖(Ξ′_z − Ξ_1)Λ_Wx‖_♯ ≤ Cη|||x|||_♯ and Λ_WΞ′_z invertible with bounded inverse (gives t_+, invertibility of Υ), and
  (β) the level-l values ev^{(l)}Λ_W(x) are computed from x_l (level-local), so that Λ_W^T completes a level-l charge **at level l** (gives t_*, δ_Υ).
  With (β), a level-l charge field d^Tj_l is completed by level-l block-Neumann corrections plus funnel transposes carrying block totals up the root
  tree; by Lemma FT (ii) the cascade costs Σ_{l′≥l}π_{l′} ≲ Σ_{l′≥l}π_l(j_l), and against S2's L^{−θq} decay this is Σ_q(q + 1)L^{−θq} < ∞ in N_Σ and
  bounded in ‖·‖_Pc (power count, ARGUED). **Candidate:** the per-level slice functional Γ_PL (GSHARP55 Lemma PL-adm, CODEX_REVIEW_GSHARP §8: CONFIRMED
  as algebra), Λ_PL := −(Γ_PLΞ_1)^{−1}Γ_PL, whose transpose completes level-i data with level-i funnels h_i^T (‖h_i^T‖_{ℓ^∞→ℓ^∞} ≤ 1) and level-i
  block-Neumann gradients; (β) holds by construction, **(α) is exactly GSHARP55 §5.5's open hole** ("how a level-i correction propagates to finer
  levels … is not written"; Codex: NOT-VERIFIED). The hard-scheme analogue is Balaban's axial-in-blocks + Landau gauge transformation u_k (CMP 99:75, as
  CMP 109 uses it; BALABAN_EXTRACT §4.1).
  *Precision on GSHARP55 §5.5 ("No live consumer needs the transfer").* That sentence is about transferring **responses** to the per-level slice, and it
  stands. What §6.4 finds is a different use: a level-local gauge function as the **alignment** of the background transfer, with S_E kept as the output
  slice.

### 6.5 Theorem R2-glob (the reduction on 𝒞_glob). PROVEN as a reduction; inputs listed with status
On 𝒞_glob(ε), ε ≤ ε_b: **(R2) (a)-(b) hold, in the |||·|||_♯ orbit norm, with C_b′ = (1 + Cη)²C_♯/(1 − C_♯Cη), provided:**
1. **BFT-0 on 𝒞_glob** with ‖z‖_{𝔐^∇} ≤ η = C_0ε — Theorem BA, CONDITIONAL on (H-lin^∇), (H-rem^∇), (FP♯′) [BFT_A §3.9];
2. **(TR-1) at z** — Lemma TR, CONFIRMED at the quadratic level (CODEX_REVIEW_TR); all orders = HIGHER55, open obligation;
3. **clause (b) at Z = 1 in |||·|||_♯** — Corollary RW♯ (PROVEN as an implication of banked CC-INV/TOP-cc, RT-cc, TC, FT and Codex-confirmed GF-E);
4. **CEN2** — BFT_A BA-4 (PROVEN; REVIEW_BFT_A_S1);
5. **the Hessian-difference expansion** (SG structure + analytic BCH tails = the Lipschitz form of (H-rem^∇)) — ARGUED;
6. **(ALIGN-ℓ)** — OPEN (S_E fails (β) by power count; Γ_PL satisfies (β), (α) open);
7. **level-0 Schauder completion** — ARGUED.
*Proof.* Theorem GA with Υ = Υ_W from (ALIGN-ℓ): (A1) from 6 (α) and the source half of the completion bound; (A2) from §6.3 (items 2-5) plus the
completion bound (6 (β), 7); C_♯Cη < 1 for ε ≤ ε_b. ∎
**Not claimed:** any of items 1, 2, 5, 6, 7 beyond their quoted status. The theorem moves (R2) on 𝒞_glob from "OPEN, with (CC-dec_Z), (EP-rec)_Z,
(N1-nd), (R♯_ω), G-pert and (G♯-patch^Ω) as inputs" (COFUN_CC §6.2; BFT_B §32.2) to "**one OPEN item, (ALIGN-ℓ), plus ARGUED expansions**", with
every other input banked or Codex-confirmed.

## 7. Outside 𝒞_glob: a local-to-global step is unavoidable

### 7.1 Why no single global alignment is available from frames (ARGUED; standard holonomy argument)
On 𝒦(ε) ∖ 𝒞_glob the connection is not small in any gauge (§2.5). A global Υ assembled from box frames, Υ := M_g with g = g_□ on box □, is exactly
orthogonal and aligned inside each box up to O(εℓ) (box side ℓ), but on a link crossing from □ to □′ the alignment mismatch is
(Z(b)g_{□′}(y′) − g_□(y))λ(y′), i.e. the transition function g_□^{-1}Zg_{□′} − 1, which is O(1) somewhere whenever the total flux is large:
near-identity transitions on all overlaps would bound the holonomy of a loop through m boxes by O(m·max transition), while a loop of coarse size R
has holonomy O(εR²) with R ~ m ℓ. So E_Υ = O(1) on the seams and the Neumann series of Theorem GA does not close. (Interpolating rotations
Σχ_□Ad_{g_□} can be singular where transitions are O(1).) Whether some other uniformly bounded global aligned congruence exists outside 𝒞_glob is
**OPEN**; I found no construction. Flat backgrounds with torus holonomy θ are in this regime on tori with θ/T ≳ ε; for T ≥ T_b with T_b large they
have connection ≤ 2π/T_b in a constant gauge, so GA applies with η ≲ 2π/T_b — a T_b depending only on (N, L, κ_±, α, θ) (ARGUED).

### 7.2 What the local-to-global step must provide — named (LOC-GA), OPEN
- **Local transfer** on boxes of side ℓ: GA with a frame alignment Υ_□ = M_{g_□}(1 + correction) — exact up to O(εℓ) inside the box (Corollary GA-PG
  says it is exact where Z is pure gauge).
- **Gluing with decay.** Gluing local *inverses* (parametrix, BFT_A BA-11) cuts sources off: ψ_□S is not cc_Z, so the local inverses would act on
  non-cc sources, i.e. need clause (c)-type general-source bounds (not available: (GE-T) expected false, BFT_B l.3575; CODEX_REVIEW_GSHARP §8). The
  alternative that keeps cc is a **local cc-decomposition at Z**, (LOC-cc_Z): S = Σ_□S_□ with S_□ ∈ cc_Z localised near □ and
  Σ_□e^{−m·dist}N_Z(S_□) ≤ C·N_{Z,m}(S). Its slot-wise ingredients: G-slots localise up to item 13's curvature-sized bulk divergence, repaired by routing
  to the level-k roots (§5.3, no per-cube neutrality needed); residual slots up to the exact commutator [λ, ρ(z)] (§5.3, TR-1-small); plain currents
  through the covariant face flux with the axial-strip defect O(f)π_l per block (§5.1 (b)). The parametrix errors are then summed with the decay of
  the weighted clause (b) at Z = 1.
- **Prerequisites:** (R3) = weighted clause (b) at Z = 1 (COFM55's CC-INV_m; Codex check running), and BFT-0 outside 𝒞_glob ((G♯-patch), BFT_A §3.10,
  OPEN). (LOC-GA) is the background counterpart of (G♯-patch) and of Balaban's random-walk construction of background propagators (CMP 99:389).
**Status of (R2) outside 𝒞_glob: OPEN**, with (LOC-GA) [⊃ (LOC-cc_Z)], (R3), BFT-0 outside 𝒞_glob, and the 𝒞_glob inputs of §6.5 applied box by box.

## 8. The analyticity route (Balaban's) — what it can and cannot do

- **(An-1) Cauchy estimates do not transfer an inverse bound from V = 1 to V ≠ 1.** A bound at one point of a holomorphic family gives no bound on a
  ball; one needs a derivative (or sup) bound on the ball. The derivative of the response in V is −H^{-1}(∂_VH_{Z(V)})H^{-1}, and ∂_VH_{Z(V)} in a
  preconditioned/aligned sense is (A2) in infinitesimal form. (PROVEN-HERE as a logical remark; trivial witness f(t) = (1 − t/t_*)^{-1}: f(0) = 1,
  unbounded as |t| → t_*.)
- **(An-2) What analyticity does give.** If BFT-0 is proved by a contraction on the complex data ball with BFT-1 bounds (BFT-2), all V-derivatives of
  Z(V) and E^br(V) at interior points are bounded by Cauchy, k-uniformly, without (R2). This is Balaban's route to (N-bg)/(H-C) (BALABAN_EXTRACT §7.3;
  M4) — **agree** with that section's reading. It gives **no decay** in the tree distance: BFT-3 needs either weighted (R2) or analyticity on polydiscs
  whose radii grow away from the observation point (Balaban's complexified localisation spaces, CMP 109 (1.10)-(1.18), LANE-READ).
- **(An-3) The source-parameter trick is GA with the slice-identity alignment.** On 𝒞_glob, differentiating the fixed point of
  Φ_t(x) = 𝓛^{-1}(NB + 𝔑(x; B) + tS) at t = 0 gives the slice response at Z with bound ‖𝓛^{-1}‖/(1 − Lip Φ) — but 𝓛^{-1} is the general-source
  inverse of Theorem BA's (H-lin^∇), the off-critical bound that is not available (CODEX_REVIEW_TOPCC item 5; CODEX_REVIEW_GSHARP §8). Restricted to
  cc_Z sources, the IFT identification is Proposition GA-slice's Υ_W, and it inherits §6.4's completion problem. **No new mechanism.**
- **(An-4) Analyticity is an input of (R2) at complex V**, not a substitute for it: Theorem GA runs verbatim on BFT-2's complex ball (all identities are
  algebraic; the Neumann series is in complexified norms) once (A1)-(A2) hold there.
- **Where the Balaban papers would help (specific questions, for the owner's fetch):**
  (i) CMP 99:75 — the axial-in-blocks + Landau gauge transformation u_k: is it the hard-scheme form of (ALIGN-ℓ) (a gauge function whose level-l values
  depend on level-l data), and how are its derivative bounds proved? (ii) CMP 99:389 — the random-walk construction of background propagators on
  localisation domains: how the gauge fixing makes local operators invertible on **general** sources (CMP 109's exponential gauge fixing replacing δ,
  BALABAN_EXTRACT §4.1), i.e. how the cc-cutoff problem of §7.2 is avoided; (iii) CMP 102 (1.2)-type regularity class with the |J| (covariant-divergence)
  clause — whether a second-order smallness of the background is needed for t_+ (𝒦(ε) has no |J| clause); (iv) CMP 102 Sect. C — the linearisation of
  the constraint by a change of variables, the hard-scheme analogue of the alignment Υ.

## 9. Findings on prior claims bearing on (R2) (one per claim; verdict, file + locating string, reason)

- **P1. BFT_B §32.1 (b) (l.3829-3831), "these bounds are independent of the gauge fixing, so (b) is a statement about the orbit" — must be
  restated in the orbit norm: CONFIRMED** (GSHARP55 GF-DEP, CODEX_REVIEW_GSHARP item 4). Added here: the orbit form is gauge- and frame-free at
  every background (Lemma OC), so (R2) can be stated without choosing a frame.
- **P2. GSHARP55 §5.4 "Status: ARGUED — an outline only" for (EP-rec)_Z: CONFIRMED as the honest status** (§5.2); "It does not need (GAP-Z)":
  **CONFIRMED**; ingredient (iii)'s "defect ≲ Cρ²_{l+1}f_k … summable in l": **CONFIRMED with precision** (value-relative, REVIEW55_BFTB F10 (c);
  needs (N1-b)'s sup bound on λ^{E,Z}); ingredient (i) at the **critical** background Z(V) (CL-iv is for Z^off): **NOT-VERIFIED**.
- **P3. GSHARP55 §0 item 2 (d) / §10 item 1, "At Z ≠ 1, (R1) is (EP-rec)_Z, inside (R2)": CONFIRMED as bookkeeping for the direct route.** On the
  GA route (EP-rec)_Z is not needed at all (field half transferred through t_+).
- **P4. COFUN_CC §6.2 (l.445), "(CC-dec_Z) … OPEN": CONFIRMED**, with the exact reason (§5.1 (c): no a-priori bounded current; on the direct route it is
  equivalent to the top-residual part of (R2)). **"every identity behind Lemmas FLUX/DEC/SF/TOP-cc must be re-established with Z-covariant operators"
  (same paragraph): NOT-VERIFIED as a necessity** — Lemma SF is re-established exactly here (SF_Z), and FLUX/DEC/TOP-cc are used only at Z = 1 on the
  GA route. (A new sufficient route does not refute the old one; it removes "must".)
- **P5. COFUN_CC §6.2 / BFT_B §40.3: (N1-nd) as an input of (R2): NOT-VERIFIED as an input.** On the GA route it is an **output** (Theorem GA (iii)).
  BFT_B §40.3's "consumed by BFT-0 rather than added to it" (l.4346) — **CONFIRMED in a stronger form** (an output of the perturbative transfer).
- **P6. REVIEW55_BFTB REFUTED-item 11 (l.624), BGD (b) for Q_ax vs lane A's Q_l^Z: CONFIRMED** (as a statement about Q_l^Z). **Precision (new):** the
  critical-point Hessian uses the true linearisation of ρ, which is exactly covariant (Dρ(z)Ξ′_zλ = [λ(c′), ρ(z)], §5.3), so item 11 bears only on routes
  that substitute Q_l^Z.
- **P7. REVIEW55_BFTB REFUTED-item 13 (l.628), S^G not composite-co-closed at curved Z: CONFIRMED** (re-derived from BGD (a)). Irrelevant to GA; on a
  localisation route repairable by root routing without per-cube neutrality (ARGUED, §5.3).
- **P8. REVIEW55_BFTB Finding 13, Lemma FR-price NOT-VERIFIED: agree** (not used by GA).
- **P9. HESSREL Lemma HR-1 / Corollary HR-2 (l.360-398): CONFIRMED** — re-derived as Lemma OC at Z = 1; bg55_ga C4 reproduces H_Z − H_1 ≠ 0 at a flat
  pure gauge (512-entry witness of HESSREL's own check is consistent), and A6 shows the **aligned** comparison vanishes exactly there.
- **P10. HESSREL FOR OTHER FILES item 3 (l.634-635), "Every perturbative transport off the trivial chain is controlled by the condition number Λ_0M_0,
  not by (G♯_0-field)'s M_0 alone": REFUTED as a universal sentence.** Theorem GA is a perturbative transport off the trivial chain whose controlling
  quantity is C_b·δ_Υ, an inverse bound times an **absolute** bound on the aligned defect in the pair; ‖H_1‖ never enters. The condition number arises
  only for perturbations bounded relative to ‖H_1‖ (HESS-rel's form), where HR-3 is right. *Correction:* "a perturbative transport is controlled by
  ‖H_1^{-1}‖_{cc→orbit}·‖E_Υ‖_{orbit→cc} for an aligned E_Υ; (FWD-0) is needed only for relatively-bounded perturbations." (Remark: in the
  (𝔐^∇ → N) pair the forward norm of H_1 is not k-uniform at θ > 0 — the residual-type source κr_l(x) carries ω_l = L^{θ(k−l)} — so a condition-number
  criterion would be empty there; ARGUED, natural representation only.)
- **P11. HESSREL §H6.2 item 1, "The route therefore does not avoid (UHL); it re-derives the need for it": CONFIRMED in direction** for backgrounds outside
  𝒞_glob (§7: a local-to-global step is unavoidable for any transfer from the trivial chain); on 𝒞_glob, GA needs no flat reference other than 1.
- **P12. BFT_B §32.2 Proposition BFT5-red (l.3837-3851), "(BFT-5_E) (a), (b) ⇐ (1) + (2) + (3) + (4)": NOT-VERIFIED as a reduction of clause (b)**
  (agree with REVIEW55_BFTB F9). Replacement on 𝒞_glob: Theorem R2-glob (§6.5); input (1) is now available (CC-INV banked + GF-E Codex-confirmed),
  input (3) (G-pert, one-gauge X_c-small) is replaced by GA, input (2) (R♯_ω) enters only as the Hessian-difference expansion inside (A2), input (4)
  (G♯-patch^Ω) only outside 𝒞_glob, as (LOC-GA).
- **P13. BFT_B §41.6 Theorem TRANSP "PROVEN as an implication … GIVEN exactly two inputs" and §41.5 (iii) "one obstruction": already REFUTED**
  (REVIEW55_BFTB F14, F15; CODEX_REVIEW_GAPZ F6) — **agree**. GA supersedes TRANSP's slot-wise transport: no slot is split at Z, no Q_l^Z is used.
- **P14. BALABAN_EXTRACT §7.3, "(N-bg)/(H-C) are … Cauchy-estimate corollaries of analyticity of the composite background": agree** (an architecture
  statement; §8 (An-2)), with the precision that Cauchy in sup norm gives no decay (BFT-3 needs more).

### 9.1 Codex verdicts used — agree or disagree, explicitly (files read as on disk at 01:20-01:28Z)
- **CODEX_REVIEW_GAPZ F7** (literal HESS-rel REFUTED; framed version NOT-VERIFIED; corrected arrow "full matched flat inverse + aligned relative
  perturbation with δ < 1 ⇒ background inverse"): **AGREE**, and refined: with an **exact** alignment ΥΞ_1 = Ξ_ZA the perturbation and the transferred
  sources are automatically cc_1, so the **cc-inverse** suffices (no full inverse), and the smallness must be absolute in the pair (Theorem GA).
- **CODEX_REVIEW_GAPZ F2** (M bounds response kernels, not an inverse): **AGREE**; not used. **F12** (curved translation-invariant backgrounds): **AGREE**;
  not used. **F8** (log-derivative factor): **AGREE**; it is a bounded analytic factor in W1 (§6.3) and changes no size.
- **CODEX_REVIEW_TOPCC item 3** (CC-INV banked) and "three additional parts" item 2 (curved background incl. CC-dec_Z NOT-VERIFIED): **AGREE** with both;
  the first is (B_1)'s gauge-invariant half, the second is why §5.1 treats (CC-dec_Z) as open on the direct route.
- **CODEX_REVIEW_GSHARP items 1, 2, 4** (flat EP-rec, GF-E, GF-DEP + orbit norm): **AGREE**; used as inputs of (B_1) and Corollary RW♯.
- **CODEX_REVIEW_GSHARP §8** ("background reconstruction NOT-VERIFIED"; "unrestricted projected-source closure NOT-VERIFIED: N(Π_E^Ty) ≤ C‖y‖ does not
  follow"): **AGREE with both**. The second is exactly the obstruction §6.4 finds for the S_E alignment at levels l ≥ 1, made quantitative by power count.
- **CODEX_REVIEW_TR** (Lemma TR CONFIRMED at the quadratic level; higher order NOT-VERIFIED): **AGREE**; it enters (R2) through (F-TR).

## 10. Errata to §1-§9 (append-only; written on the final read, 01:30Z)
- §6.4 (β): "by Lemma FT (ii) the cascade costs Σ_{l′≥l}π_{l′} ≲ Σ_{l′≥l}π_l(j_l)" — the bound that the cascade of block totals uses is **COFUN_CC
  Lemma FLUX (ii)** (face fluxes do not grow: |Φ_lj| ≤ π_l(j)); Lemma FT governs the funnel spreading of each root charge. Conclusion unchanged.
- §9 P9: "(512-entry witness of HESSREL's own check is consistent)" — I did **not** re-run or open HESSREL's hr1 check; read instead: bg55_ga C4 is an
  independent exact witness of the same phenomenon (H_Z − H_1 ≠ 0 at a flat pure gauge).
- §4.2: "(iv) *is* a (GAP-Z)-type statement" — loose: (iv) is an inverse bound on cc_Z sources in the orbit norm; (GAP-Z) as defined (BFT_B §38.1) is a
  lower bound on the slice. On a slice with bounded projection the two are equivalent up to C_Π; at Z ≠ 1 that needs (N1-c).

## 11. Summary table

### 11.1 Results of this file (status words; none has had a Codex check)
| id | statement (section) | status |
|---|---|---|
| N1 | Lemma OC: (R2) is gauge/frame-covariant; M_ĥ intertwines H, Ξ and is an isometry of the covariant norms (§2.3) | PROVEN-HERE (bg55 A1 at PG) |
| N2 | Lemma KER_Z: H_ZΞ_Z = 0 at every critical background (§3.1) | PROVEN-HERE |
| N3 | Lemma SF_Z: D_Z(H_Zy) = ev^{(0→k)T}d_V^Tb_Z(y), root-supported, exact (§3.2) | PROVEN-HERE (identity); size of b_Z ARGUED |
| N4 | Lemma FG_Z: orbit uniqueness, gauge-fixing independence at Z, given (N1-nd) (§3.3) | PROVEN-HERE |
| N5 | **Theorem GA** (gauge-aligned transfer): (B_1) + (A1) + (A2) ⟹ (N1-nd) at Z and (R2)(b) with C_b′ = t_+t_*C_b/(1 − C_bδ_Υ) (§4.1) | **PROVEN-HERE** (bg55 A2-A7 PASS, C1-C6 FIRE) |
| N6 | Proposition GA-slice: E_{Υ_W} = Π_W^T(H_Z − H_1) on W, Υ_W^TS = Π_W^TS (§4.3) | PROVEN-HERE (bg55 A3, A7) |
| N7 | **Corollary GA-PG**: (R2) holds at every pure-gauge background, any size, with the Z = 1 constant (§4.4) | **PROVEN as an implication** (CC-INV banked; GF-E Codex-confirmed) |
| N8 | Exact covariance Dρ(z)Ξ′_zλ = [λ(c′), ρ(z)] of the true soft linearisation (§5.3) | PROVEN-HERE |
| N9 | (CC-dec_Z) skeleton with 𝒟_Z (§5.1 a); cut-condition limit and circularity of the direct route (§5.1 c) | PROVEN-HERE |
| N10 | Covariant face-flux defect O(f_l)π_l per block with axial transports (§5.1 b) | ARGUED |
| N11 | **Corollary RW♯**: clause (b) at Z = 1 holds in the transport-weighted norm |||·|||_♯ (§6.2) | **PROVEN as an implication** |
| N12 | Term-by-term sizes of D𝔑(z) in (|||·|||_♯ → N) (§6.3 table) | power counts PROVEN-HERE; completeness/tails ARGUED |
| N13 | (F-♯): in plain 𝔐^∇ the r(u)-linear term carries a level count (k − 1)η; in |||·|||_♯ it is k-uniform (§6.3) | upper bound PROVEN-HERE (count); attainment ARGUED |
| N14 | (F-TR): (R2) needs (TR-1) at the background (§6.3) | PROVEN-HERE as a dependency (power count) |
| N15 | The S_E alignment is not k-uniform at levels l ≥ 1 (spikes ≍ 2dL^{3l}π_l) (§6.4) | ARGUED (power count; no witness) |
| N16 | (ALIGN-ℓ): a level-local alignment; Γ_PL satisfies (β) by construction, (α) = GSHARP55 §5.5's hole (§6.4) | **OPEN** (named) |
| N17 | **Theorem R2-glob**: (R2) on 𝒞_glob ⟸ items 1-7 of §6.5 (§6.5) | PROVEN as a reduction; one OPEN input (ALIGN-ℓ) |
| N18 | No global aligned Υ from frames outside 𝒞_glob (seam/holonomy argument) (§7.1) | ARGUED |
| N19 | (LOC-GA) ⊃ (LOC-cc_Z): the local-to-global step outside 𝒞_glob; prerequisites (R3), BFT-0 outside 𝒞_glob (§7.2) | **OPEN** (named) |
| N20 | Item-13 bulk divergence repairable by root routing, no per-cube neutrality (§5.3) | ARGUED |
| N21 | (An-1) Cauchy estimates cannot transfer an inverse bound; (An-3) the source-parameter trick is GA-slice (§8) | PROVEN-HERE (logical/identification) |

### 11.2 Verdicts on prior claims (§9)
| id | claim (file, locating string) | verdict |
|---|---|---|
| P1 | BFT_B §32.1 (b) "independent of the gauge fixing … about the orbit" — restate in the orbit norm | CONFIRMED |
| P2a | GSHARP55 §5.4 "Status: ARGUED — an outline only" | CONFIRMED |
| P2b | GSHARP55 §5.4 "It does **not** need (GAP-Z)" | CONFIRMED |
| P2c | GSHARP55 §5.4 (iii) "That defect is summable in l" | CONFIRMED with precision (value-relative; needs (N1-b)) |
| P2d | GSHARP55 §5.4 (i) EP-int at the critical background Z(V) via CL-iv | NOT-VERIFIED (CL-iv is for Z^off) |
| P3 | GSHARP55 §0 2(d)/§10 "(R1) … inside (R2) as (EP-rec)_Z" | CONFIRMED (bookkeeping, direct route) |
| P4a | COFUN_CC l.445 "(CC-dec_Z) … OPEN" | CONFIRMED (reason: §5.1 c) |
| P4b | COFUN_CC §6.2 "every identity behind FLUX/DEC/SF/TOP-cc must be re-established with Z-covariant operators" | NOT-VERIFIED as a necessity |
| P5a | (N1-nd) as an input of (R2) (COFUN_CC §6.2; BFT_B §40.3) | NOT-VERIFIED as an input (an output of GA) |
| P5b | BFT_B l.4346 "(N1-nd) … consumed by BFT-0 rather than added to it" | CONFIRMED (stronger: an output) |
| P6 | REVIEW55_BFTB REFUTED-item 11 (Q_l^Z root covariance) | CONFIRMED (+ precision N8) |
| P7 | REVIEW55_BFTB REFUTED-item 13 (S^G not cc at curved Z) | CONFIRMED |
| P9 | HESSREL Lemma HR-1 / Corollary HR-2 | CONFIRMED |
| P10 | HESSREL l.634-635 "Every perturbative transport off the trivial chain is controlled by the condition number Λ_0M_0" | **REFUTED** (Theorem GA; correction in §9 P10) |
| P11 | HESSREL §H6.2 "does not avoid (UHL); it re-derives the need for it" | CONFIRMED (in direction, outside 𝒞_glob) |
| P12 | BFT_B §32.2 Proposition BFT5-red as a reduction of clause (b) | NOT-VERIFIED (agree REVIEW55_BFTB F9); replaced on 𝒞_glob by N17 |
| P14 | BALABAN_EXTRACT §7.3 (N-bg)/(H-C) as Cauchy corollaries | CONFIRMED (in direction; no decay from sup-Cauchy) |
Not counted (agreement with an existing verdict): P8 (FR-price NOT-VERIFIED, REVIEW55_BFTB F13), P13 (TRANSP / "one obstruction" already REFUTED, F14/F15).

**Counts (§11.2): CONFIRMED 12 (P1, P2a, P2b, P2c, P3, P4a, P5b, P6, P7, P9, P11, P14), NOT-VERIFIED 4 (P2d, P4b, P5a, P12), REFUTED 1 (P10).**

## 12. For the lead — what changes

1. **(R2) has a transfer mechanism, and it is exact algebra (Theorem GA, PROVEN-HERE, checked).** Clause (b) at Z = 1 (CC-INV banked + GF-E
   Codex-confirmed) transfers to a background Z through any invertible Υ with ΥΞ_1 = Ξ_ZA: the aligned defect E_Υ = Υ^TH_ZΥ − H_1 and the transferred
   sources Υ^TS are composite-co-closed at Z = 1 **automatically**, so only the cc-inverse at Z = 1 is used; the Neumann factor is C_b·δ_Υ, with no
   forward bound on H_1 (no (FWD-0)), no relative-Hessian series, no slot split at Z. **(N1-nd) at Z becomes an output.** At every pure gauge
   (any size) Υ = M_G gives E_Υ = 0: (R2) holds there with the Z = 1 constant (Corollary GA-PG).
2. **(R2)'s open list changes.** Remove as prerequisites: (CC-dec_Z) (on the direct route it is circular — §5.1 (c)), (EP-rec)_Z, (N1-nd), G-pert,
   HESS-rel. On **𝒞_glob**: (R2) ⟸ BFT-0 on 𝒞_glob + (TR-1) at the background (HIGHER55) + Corollary RW♯ (proven) + CEN2 (proven) + ARGUED expansions
   (Lemma SG structure, BCH tails, level-0 Schauder completion) + **one OPEN item, (ALIGN-ℓ)**. **Outside 𝒞_glob**: additionally (LOC-GA) ⊃ (LOC-cc_Z),
   with (R3) and BFT-0 outside 𝒞_glob as prerequisites.
3. **HANDOFF critical path.** (a) The transfer must be run in the **transport-weighted response norm** |||·|||_♯ (residual weight L^{(1+θ)(k−1−j)}),
   else the background perturbation carries a level count (k − 1)η — the same currency issue as (R4), with the same cure (KFACTOR_O55 §(b)-(c));
   clause (b) at Z = 1 already holds in |||·|||_♯ (Corollary RW♯). (b) **HIGHER55 (TR-1 at all orders) is on (R2)'s path**, not only (R4)'s. (c) **S_E
   must not be used as the alignment** (power count: level-l completions become level-0 spikes ≍ L^{3l}π_l) — S_E stays the **output** slice. (d) The
   candidate alignment is the per-level slice functional Γ_PL (or Balaban's axial-in-blocks gauge, CMP 99:75): **GSHARP55 §5.5's open hole (regularity
   of the per-level gauge function across levels) becomes load-bearing for (R2)**.
4. **Statement of BFT-5 (b).** Use §2.2's (R2) (orbit norm, covariant source norm N_Z, k-, T-, V-uniform); it is frame-free (Lemma OC).
5. **One REFUTED sentence to stop propagating:** HESSREL FOR OTHER FILES item 3, "Every perturbative transport off the trivial chain is controlled by
   the condition number Λ_0M_0" — false as a universal sentence (Theorem GA); (FWD-0) is needed only for relatively-bounded perturbations. It should not
   be entered into BFT_A §3.11 as a required input.
6. **Tally: no change** (none of these is among PROOF's 105 counted items).
7. **Recommended Codex check, in this order:** Theorem GA + Proposition GA-slice + Corollary GA-PG (algebra; short); Lemma SF_Z; Corollary RW♯ (residual
   sums); the §6.4 power count that S_E fails as an alignment at levels ≥ 1 (the claim most likely to be contested); the §6.3 table.
8. **For the Balaban papers (owner's fetch):** §8's four specific questions (CMP 99:75 u_k as (ALIGN-ℓ); CMP 99:389's gauge-fixed local inverses on general
   sources as (LOC-GA); CMP 102's |J| clause; CMP 102 Sect. C's linearising change of variables as the hard-scheme Υ).

Files written by this worker: BGT55.md; checks/bg55_ga_criteria.md, checks/bg55_ga.py, checks/bg55_ga_out.txt, checks/bg55_ga_err.txt,
checks/bg55_ga_time.txt. No git command was run.
UTC end stamp: 2026-10-29T01:31:10Z

## 13. Outcome against the PRE-STATED targets and refutation tests (appended 01:33Z; content of §1-§12 unchanged)
- **T1** (statement): done, §2.2 (orbit norm, covariant N_Z, k-, T-, V-uniform; frame-free by Lemma OC).
- **T2** (CC-dec_Z, background EP-rec, against items 11, 13, F7): done, §5. (CC-dec_Z) direct form: exact skeleton PROVEN, bounded datum circular;
  (EP-rec)_Z: outline status CONFIRMED, ingredient (iii) CONFIRMED with precision, (i) at Z(V) NOT-VERIFIED. Both are **unnecessary on the GA route**.
- **T3** (mechanism): (a) frame conjugation + perturbation = Theorem GA with Υ = M_g(1 + correction); exact at pure gauges; on 𝒞_glob reduced to (ALIGN-ℓ);
  (b) analyticity: §8 — gives derivatives, not the transfer.
- **T4**: statuses in §11.1.
- **R-a (pure gauge exactness): TESTED, PASSED** — Corollary GA-PG; bg55_ga A6 (E_{M_G} = 0 exactly, both models) with C4 firing (unaligned difference ≠ 0).
- **R-b (CC-dec_Z not a decomposition): NOT TESTED numerically.** The exact skeleton identity D_Z(T^Z_b) = ev^T𝒟_Z^Tb needs a true critical background,
  which I did not construct in exact arithmetic; and the direct (CC-dec_Z) with a bounded datum turned out to be circular (§5.1 c), so there was no
  bounded decomposition to test. bg55_ga tests only GA's algebra.
- **R-c (non-uniform constants): OCCURS for the plain-𝔐^∇ version of the transfer** ((F-♯): level count (k − 1)η in S2; and without (TR-1) in S3), and
  **for the S_E alignment** (§6.4, L^{3l}); both are removed in the stated form (|||·|||_♯, (TR-1), (ALIGN-ℓ)), which is why those three appear as inputs.
- **R-d (silent GAP-Z / relative series): does not occur** — GA uses neither; (N1-nd) and a (GAP-Z)-type bound are outputs.
- **R-e (condition number needed): does not occur for GA** — the controlling quantity is C_b·δ_Υ (§4.2); HESSREL's universal sentence is refuted (P10).
- Kernel clause of (B_1): Ker H_1 = Ran Ξ_1 on {x_k = 0} is BFT_A Lemma FG (i) / the EP-opt kernel step (CODEX_REVIEW_GSHARP §1, "EP-opt: CONFIRMED");
  bg55_ga I1 is consistent in M1 (rank H_Z = rank H_1 = 120).

*Correction (appended 2026-10-29T01:31:57Z):* §13's heading time "01:33Z" was an estimate written before the clock was read; the `date -u` at that append was 2026-10-29T01:31:49Z. In §13's last bullet, "rank H_1 = 120" is inferred from A1 (H_Z = M_GH_1M_G^T at PG), not printed by the script.
