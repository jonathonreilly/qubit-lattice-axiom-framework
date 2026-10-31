Reviewer model: claude-opus-5-5

# SRCAN55 — the analyticity route to SRC (source-inserted RG) — Opus 5.5 worker deliverable

UTC start: 2026-10-29T01:40:42Z
Write scope: this file and `checks/sa55_*` only. No git. Append-only.

## PRE-STATED (written before any derivation; statements only)

### Targets
- **T1 (perturbed RG).** Formulate the layer-1 RG with a complex, position-dependent coupling
  g(x) = g + δg(x) (or the equivalent perturbation of 1/g², whichever is the parameter the banked
  estimates actually carry), δg slowly varying and small on the scale set by the contraction margin.
  List every place the coupling enters BFT-0/1/2 (Theorem BFT-E on 𝒞_glob, GV55.md), the composite
  contraction (Theorem K^{(σ)} for 𝔉_k), and the soft kernel, and for each say whether the banked
  estimate survives uniformly on a complex polydisc — CONFIRMED / NOT-VERIFIED / REFUTED per entry.
- **T2 (Cauchy → SRC-κ).** Derive SRC-κ (separated conditional cumulant bounds, exponential decay at
  ℓ_ref, uniform in a, R, small coarse fields) from (analyticity on the polydisc) + (Cauchy estimates) +
  (a stated locality property), and say exactly which locality is needed and whether BFT-3 as drafted in
  BFT34_55.md supplies it.
- **T3 (scope).** State precisely what the route does NOT cover: large coarse fields (UNIV55 N3), SRC-M
  (the eight O(g_bare²) matching constants), the per-step RLF conditioning on U_K, and anything else found.

### What would count as a refutation of the route (or of a step of it)
- **R1 (generation).** If the 47 local gauge-invariant functionals of SRC-κ are NOT all obtained as
  derivatives of the effective action with respect to local couplings of terms the layer-1 RG already
  carries (or can carry within its banked norms), then "analyticity in g(x)" alone does not give SRC-κ
  for all 47; the route then needs sources for operators outside the coupling family, i.e. a different
  (larger) perturbation class.
- **R2 (non-analytic dependence).** If any banked estimate depends on the coupling non-analytically —
  e.g. through large/small-field indicator functions with g-dependent thresholds, a background field
  defined by a real minimisation of a g-dependent functional, |g| or Re(1/g²) positivity used with a
  margin that a complex perturbation of the stated size destroys, or a reflection-positivity /
  monotonicity step — then analyticity on the polydisc fails at that point unless that dependence is
  frozen (held at the unperturbed g) and the frozen version is shown still to close.
- **R3 (quantitative).** Cauchy's estimate on a polydisc of radius r per site costs r^{-n} for an
  n-point cumulant. If the admissible radius (set by the contraction margin) is too small relative to the
  sup bound of the perturbed effective action for the resulting cumulant bounds to have the size and
  uniformity SRC-κ demands (uniform in a and R; correct power of g), the route fails quantitatively, and
  I will say by how much.
- **R4 (locality).** If the exponential decay at ℓ_ref in SRC-κ needs a decay of the *derivative*
  structure (connected/truncated in the separated points) that analyticity + sup bounds do not supply
  without an additional cluster/polymer locality statement, then BFT-3-type locality is a genuine extra
  input and I will state it as such (not as "inherited automatically").
- **R5 (slowly varying / (F_R)).** If the slowly-varying condition is not compatible with Cauchy
  estimates at separated points (Cauchy needs independent per-site radii, slowly-varying constrains the
  perturbation to be smooth), the two requirements conflict and I will state the resolution or the gap.

### Verdict labels
CONFIRMED (I re-derived the load-bearing step), NOT-VERIFIED (could not settle; say what is missing),
REFUTED (give the correct statement and derivation). "The file says PROVEN" is not evidence.


## RESUMED 2026-10-29T02:46:09Z

Resumed by claude-opus-5-5 (same model ID as the first line; no extra model line needed). The previous run
stopped after the PRE-STATED block: the draft contains no derivations, so there is nothing of it to
re-verify and no errata so far. Everything below is new in this run. Inputs read before deriving are
listed in §0 with their locating strings.

---

## §0. Read record, provenance, Codex verdicts used (appended 2026-10-29 ≈03:20Z)

**Read in full:** REVIEW_BRIEF_55.md (scratchpad); the task brief (scratchpad `queue/go_SRCAN55.md`); SRCCD55.md (1017
lines, incl. errata E1-E14, "Completed: 2026-10-29T01:39:23Z"); CODEX_REVIEW_SRCCD.md (407 lines; it ends with its banking
list "7. NOT-VERIFIED: Proposition E …", so it looks complete).
**Read by string, bounded ranges:** PROOF.md l.1-46 (header incl. "[S26-BANKED]"), "Lemma TOWER-VAR" (l.6666 ff.), E_NA
(l.2539), "Decision 4 is MADE" (l.585), "Lemma CT♯" (l.5560), "Theorem RW" (l.5577), "Corollary RW-triv" (l.5637), "Theorem
N5-sf0" (l.5646); BFT_A.md l.1-60 ("1.1 The composite problem", "1.4 The pair"); KFACTOR_OFF55.md §1-§3.5 (l.66-316);
CODEX_REVIEW_KOFF.md §4.3 (l.321-416), §5.3 (l.491-547), banking list (l.714 ff.); GV55.md l.1-120, l.200-330 ("Theorem BFT-E
(assembly)", "3.3 What Theorem BFT-E does not give"); CODEX_REVIEW_GV.md banking list (l.422 ff.); BFT34_55.md l.1-430 (Lemma
WD, Theorem BFT3-glob, Proposition CX, §2.3-§2.7 incl. errata) — the file ends "File ends here.", so it is complete;
RLARGE.md l.40-130 ("Action normalisation", "The exact chain", "Indicators", "Thresholds", "Flow hypothesis (F_R)");
UNIV55.md l.325-375 ("(N1)"-"(N4)"); CODEX_REVIEW_FLOW55.md banking list (l.332 ff.); PANEL_P4.md l.280-335, l.445-460.
**Corpus (third-party; cited by arXiv id, never copied):** Dimock I (1108.1335) §2 p.13 eq. (103)-(104) and the sentence
after them (complex decoupling parameters s_□, |s_□| ≤ M^{1/2}, absorbed by the walk-expansion margin), §3.1 eq. (105)
(the tracked parameters ε_k, μ_k, λ_k); Dimock III (1304.0705) Remark after (226) ("can be adapted to treat correlation
functions", pointing to Balaban–O'Carroll); Dimock 2009.01156 closing remark 3 (source terms "should be possible");
Dimock 2204.07201 p.2 (local gauge-invariant perturbations ⟨dA, J⟩; "Uniform bounds on the generating function and
analyticity in J, j would give uniform bounds on correlation functions"). **Finding from the corpus:** the analyticity route is
the route the Balaban school itself names for correlation functions, but no corpus paper carries it out, and every
analyticity statement in the corpus is in the FIELDS or in decoupling parameters, never in the coupling. Nothing below rests on
the corpus; it is cited only to locate the technique.

**Provenance of what I build on.** Every lane result I use is either [S26-BANKED] with a complete Codex review (KOFF, GV,
SRCCD, FLOW55) or a session-19/20 PROOF result (Theorem RW, Lemma CT♯, N5-sf0) predating sessions 24-25. BFT34_55
(Opus 5.5) has no Codex review on disk; where I use it I say so and re-derive what is load-bearing.

**Codex verdicts used, agree/disagree (explicitly):**
- CODEX_REVIEW_SRCCD item 1 (Proposition B, exact source recursion CONFIRMED; "A uniform complex polydisc is a further
  analytic hypothesis, not a consequence of triangularity"): **AGREE**. This file is about exactly that further hypothesis.
- item 2 (separated-support counterterm cancellation and the mixed Cauchy estimate CONFIRMED; MST inequality REFUTED; two-set
  bound valid; "the fixed sup-norm source polydisc controls smeared observables, not the cutoff-independent pointwise weights
  in κ-1"; "Holding U_K fixed … does not prove … that its logarithm is uniformly analytic"): **AGREE on all four**, and §3.4
  below sharpens the third into a theorem-level obstruction (Lemma SA-CF) plus a mechanism (Lemma SA-J).
- item 3 (Lemma V CONFIRMED, coefficient ≥ 3/2000000): **AGREE**; used in Lemma SA-CF.
- item 4 (counts 47 and 8 CONFIRMED; κ-2's n = 0 clause unspecified): **AGREE**; §3.5 shows the 46 linear insertions need no
  sources of their own.
- item 5/§5 (Proposition C with E3 CONFIRMED in graph distance; Euclidean rate REFUTED): **AGREE**; used in Proposition SA-MOM.
- item 7/§7 (Proposition E NOT-VERIFIED: singleton, all-order LF moments, large-distance weight): **AGREE**; §3.6-§3.8 say
  which of the three the analyticity route touches and how.
- CODEX_REVIEW_KOFF item 5 + §5.3 (corrected Theorem K^{(σ)}, with the explicit thresholds) and CODEX_REVIEW_GV item 4
  (BFT-E on 𝒞_glob): **AGREE**; Proposition SA-K is a perturbation of exactly that corrected statement.
- CODEX_REVIEW_FLOW55 item 4 ((UIR^♮) NOT-VERIFIED): **AGREE**; Lemma SA-F is conditional on an analytic form of it.

## §1. Symbols pinned for this file (systemic defect 1; every collision checked by grep on the lane directory)

| Symbol here | Meaning here | Collides with | Resolution |
|---|---|---|---|
| η, h_η | the e-source field on fine sites; h_η(p) := ½Σ_{x∈corners(p)}η(x), so Σ_xa⁴η(x)e_a(x) = Σ_ph_η(p)s(U_p) (SRCCD55 Lemma V Step 0, Codex SRCCD §3 item 1) | PROOF η_1 (three objects), BFT's η (ball radius, KFACTOR_OFF55 §2.2) | the ball radius is written **η_b** below; the source is η or η_src |
| u_0(p) | the perturbed Wilson coefficient u_0 − h_η(p) (RLARGE "Action normalisation": u = 1/g², s(U) = 1 − N⁻¹Re tr U) | — | — |
| **ε̂ = (ε̂_0, ε̂_l)** | complex coefficient fields: ε̂_0 on level-0 plaquettes (Wilson term), ε̂_l on the level-(l+1) soft terms of the pair (l, l+1) | ε_0 (BFT small-field bound; K^{(σ)}'s data threshold), ε_1 (RLARGE cut), ε_* (N5 threshold, PROOF) | always hatted; thresholds for it are **ε̂_*, ε̂_RW** |
| ‖ε̂‖_cf | max_l‖ε̂_l‖_∞ + [ε̂_0]^∞_α (pointwise Hölder seminorm in level-k coarse units, separations from one fine step to one coarse unit, Codex KOFF §4.3's convention) | ‖·‖_♮ (FLOW55, GV55) | new name "cf" |
| r_src | radius of the sup-norm e-source polydisc (= SRCCD55's r_0) | PROOF COMP's r_0, Theorem RW's R | always "r_src" |
| r_z | polydisc radius in the smearing variables z_i (η = Σz_ih_i) | — | — |
| G_cc, K, C₀, η_* | Codex KOFF §5.3's constants: G_cc bounds the full cc response in 𝔐^{(σ)} (Codex's "G"), K the nonlinear-source constant, C₀ := max(2, 4G_cc), η_* the local analytic radius | G_0 (divergence-form source); K (number of levels), K_i (kernels) | subscripts kept |
| K_ε | the constant of Lemma SA-K1 (ε̂-weighted rows) | — | — |
| ω_hm(r) | 1 − (4/π)arctan r, a harmonic-measure exponent | ω = the Wilson state (ROTDEF, SRCCD55) | subscript "hm" always |
| 𝒰_ℂ, 𝒰_ℝ | sup of a mixed second derivative of the conditional generating function over the complex polydisc / the real cube | M (polymer block side), M_x (KFACTOR_OFF55) | calligraphic U |
| μ_R | a decay rate of real-tilted conditional covariances | m_c, m_0, m_cov, m_* (four rates, SRCCD55 §1) | new name |
| P_cc | 1 − P^TD^⊥ (BFT34_55's shorthand; HR routing) | — | — |
| g_k, u_k | the chain's own coupling sequence (RLARGE (F_R)); g_0 = g_bare, u_K = 1/g_ref² | g a gauge transformation (KFACTOR_OFF55) | gauge transformations are written g_□ only in quotes |

---

## §2. T1 — the perturbed RG: where the coupling enters, and which estimates survive

### 2.1 The perturbed chain, exactly (PROVEN-HERE; elementary)
- **The source enters in exactly one place.** With W_ch = e^{−S(U_0)}Π_{i<K}K_i(U_{i+1}, U_i) and the chain's kernels
  k^{(i)}_c(V; M) = e^{−κu_iφ_M(V)}/∫e^{−κu_iφ_M} (RLARGE "The exact chain"), the e-tilt is
  W_ch·exp(Σ_xa⁴η(x)e_a(x)) = e^{−Σ_p(u_0 − h_η(p))s(U_{0,p})}·Π_{i<K}K_i(U_{i+1}, U_i).
  The kernels are NOT changed: SRCCD55's exact identity Φ_K(η) = −(S_K(U_K; η) − S_K(U_K; 0)) and Proposition B (Codex SRCCD
  item 1, CONFIRMED) hold only for the chain with fixed kernels ("The kernel couplings u_i are parameters of W", RLARGE). So the
  e-source is **a complex, position-dependent shift of the bare Wilson coefficient, u_0 → u_0(p) := u_0 − h_η(p)**, and
  nothing else.
- **Relative size.** ε̂_0(p) := −h_η(p)/u_0 = −g_0²h_η(p), |h_η| ≤ 2‖η‖_∞. Under (F_R), u_0 ≥ u_K − R + β_−K log L, so
  |ε̂_0| ≤ 2r_src/(u_K − R + β_−K log L) → 0 as a → 0 at fixed r_src.
- **Step 0.** The integrand of RG step 0 at fixed U_1 is exp(−u_0[Σ_p(1 + ε̂_0(p))s(U_p) + κΣ_cφ_c]) up to the U_0-dependent
  kernel normalisation, which does not involve η. Dividing by u_0 (BFT_A §1.1: 𝔉_k is "E_NA, at g = 1 and with the factor N
  absorbed in κ_j"), the tree-level step-0 problem is the depth-1 composite with the Wilson term weighted by 1 + ε̂_0.
- **Steps i ≥ 1.** The level-i effective action of the tilted chain carries a position-dependent coupling u_i^η(x) on its
  local densities, while the kernel keeps κu_i. So the per-step background problem acquires a **mismatch** ε̂_i :=
  (u_i^η − u_i)/u_i between the effective coupling field and the fixed kernel coupling. For constant ε̂_i this is exactly
  κ_i → κ_i/(1 + ε̂_i). The mismatch is an OUTPUT of the source-inserted flow (§2.6), not an input. The composite whose
  critical point reproduces such a tower (the analogue of TOWER-VAR (a)) carries products of per-level ratios on its terms; I do
  not derive it. Call that missing statement **TOWER-VAR^η** (OPEN).
- **One perturbation class covers every reading.** In each case the perturbation is a complex multiplicative coefficient field
  on the local terms of the composite:
  **𝔉_k^{ε̂} := Σ_p(1 + ε̂_0(p))w(F_p) + Σ_{l<k}κ_lΣ_c(1 + ε̂_l(c))φ̂_c(M̄^{(l)}_c(U_l); U_{l+1}).**
  Plane-dependent ε̂_0 (sources for the diagonal components of 𝒯) are inside the class. The off-diagonal 6′ components of 𝒯
  and the dimension-5 τ, 𝔴 are not coefficient perturbations of 𝔉_k's terms; §3.5 shows they need no sources.
- **The two readings' sizes.** Bare: ε̂_0 = −g_0²h_η, as rough as η, |ε̂_0| ≤ 2r_srcg_0². Per-step renormalised:
  |ε̂_l| ≲ r_srcg_l² (§2.6), smooth at scale ℓ_l by construction.

### 2.2 Proposition SA-K — the composite contraction survives complex variable coefficients. PROVEN as an implication
**Lemma SA-K1 (the ε̂-weighted rows).** Setting of Codex KOFF §5.3 (= GV55 Theorem BFT-E's): d = 4, N ≥ 2, L ≥ 3 odd,
κ_l ∈ [κ_−, κ_+], 0 < α < σ ≤ 1 with θ₀ as there, 𝒞_glob, trivial centring, m = 0, T ≥ 3. Put
δF(x) := 𝔉_k^{ε̂}∘exp(x; B) − 𝔉_k∘exp(x; B). There is K_ε < ∞, depending only on (N, L, κ_±, α, σ) and the finite local
constants of Codex KOFF §4.3 and BL-C, such that for complex ε̂, complex B with s := ‖B‖_D ≤ η_b, and ‖x‖_{(σ)}, ‖x′‖_{(σ)} ≤
η_b ≤ η_*:
- (i) N^{(σ)}(∇δF(x)) + J(P^TD^⊥∇δF(x)) ≤ K_ε‖ε̂‖_cf(η_b + s);
- (ii) N^{(σ)}(∇δF(x) − ∇δF(x′)) + J(P^TD^⊥(∇δF(x) − ∇δF(x′))) ≤ K_ε‖ε̂‖_cf‖x − x′‖_{(σ)}.

*Proof.*
- **Exact decomposition.** ∇δF = d*[G^{ε̂}_0] + j^{ε̂}_W + Σ_lκ_l[R_l^T(ε̂_lΨ_l) + E^{ε̂}_l], with
  - G^{ε̂}_0 := ε̂_0·∇w(F), the FULL Wilson row (its linear part ε̂_0c_wdx_0 included);
  - j^{ε̂}_W := (Dq_x)^T(ε̂_0∇w(F));
  - E^{ε̂}_l := Σ_cε̂_l(c)E_{l,c}, the ε̂-weighted per-link plain currents of Lemma SG.
  This is the product rule for Σ_pε̂_0(p)w(F_p) with F_p = (dx_0)_p + q_p(x) (Codex KOFF §4.3's Wilson identity with a
  coefficient), plus Lemma SG's identity, which is proved link by link ("δσ_c = κ_l[…]", KFACTOR_OFF55 §2.1) and is
  multiplied by ε̂_l(c). The coefficients do not depend on x, so no derivative falls on them.
- **Divergence-form slot.** In coarse units (G^{ε̂}_0)^c = ε̂_0·n²∇w(F). On the ball, ‖n²∇w(F)‖_∞ + [n²∇w(F)]^∞_α ≤ C_Wη_b:
  BA-3 and BL-C give n²F a pointwise C^α bound O(η_b) (Codex KOFF §4.3), and ∇w(F) = c_wF + O(F³). With the product rule
  [fg]^∞_α ≤ ‖f‖_∞[g]^∞_α + [f]^∞_α‖g‖_∞, and Campanato ≤ C_Camp·pointwise Hölder:
  ‖(G^{ε̂}_0)^c‖_∞ + [(G^{ε̂}_0)^c]_α ≤ C_CampC_W(‖ε̂_0‖_∞ + [ε̂_0]^∞_α)η_b.
  **This is the only slot where [ε̂_0]^∞_α is unavoidable** (see the HR (iv) alternative below).
- **Residual slot.** L^{(1+σ)m}‖(κ_lε̂_lΨ_l)^c‖_∞ ≤ κ_+‖ε̂_l‖_∞L^{(1+σ)m}(‖r^c_l‖_∞ + ‖(Ψ_l − r_l)^c‖_∞) ≤
  κ_+‖ε̂‖_∞(η_b + s + Cη_b²). This uses Codex KOFF §4.3 (1) and (3); the top residual r_{k−1} = Qx_{k−1} − B carries the data
  s, in the homogeneous-data norm of Codex §5.3.
- **Plain slots.** The bounds behind Codex KOFF §4.3 (2) are proved per averaged word, with bounded incidence absorbed into an
  L-dependent constant ("Per-link frequency factors can be kept by differentiating each averaged word before summing").
  Multiplying each per-link term by |ε̂_l(c)| ≤ ‖ε̂‖_∞ gives π_l(κ_lE^{ε̂}_l|_l) + π_{l+1}(κ_lE^{ε̂}_l|_{l+1}) ≤
  C′‖ε̂‖_∞L^{−σm}(η_b + s)², summable over l. The Wilson plain row obeys π_0(j^{ε̂}_W) + [(j^{ε̂}_W)^c]^∞_α ≤
  C(‖ε̂_0‖_∞ + [ε̂_0]^∞_α)η_b² (Codex's Wilson bound with the product rule).
- **The cc correction.** Divergence-form and residual-type rows have D^⊥ = 0 (Proposition CB's proof: "d*d* = 0;
  d*Q_l^T = ev^Td*"). So D^⊥∇δF = D^⊥(plain rows) exactly. HR (iii) (soft plain rows, factor 2dM_γ(k − l)) and HR (iv)
  (Wilson plain row, factor dM_γ/(L^α − 1)) give
  J(P^TD^⊥∇δF) ≤ 2dM_γC′‖ε̂‖_∞(η_b + s)²/(1 − L^{−σ})² + dM_γC(‖ε̂_0‖_∞ + [ε̂_0]^∞_α)η_b²/(L^α − 1).
  *Alternative without Hölder for this row:* HR (iii) at l = 0 costs 2dM_γ·k·π_0(j^{ε̂}_W) ≤ 2dM_γk‖ε̂_0‖_∞Cη_b². For the bare
  coefficient ε̂_0 = −g_0²h_η, and k ≤ K, (F_R) with u_K ≥ R gives **k‖ε̂_0‖_∞ ≤ 2r_src·kg_0² ≤ 2r_src/(β_−log L)**:
  asymptotic freedom pays the level count. The divergence-form slot has no such alternative (Lemma SA-J).
- **(ii).** Every term is affine in its x-dependent factor, with the same local structure. Codex KOFF §4.3's difference bounds
  ((1)-(3) "with δ"; the Wilson "difference bounds Cηδ") give the same estimates with η_b² → η_bδ and η_b → δ. The LINEAR
  parts (ε̂_0c_wdx_0 and κ_lε̂_lr_l) produce the δ-terms without a factor η_b. That is why the Lipschitz constant is
  O(‖ε̂‖_cf) and not O(η_b). Collect the constants into K_ε. ∎

**Proposition SA-K.** In the setting of SA-K1, with Codex KOFF §5.3's G_cc, K, C₀ = max(2, 4G_cc) and data threshold ε₀
(each taken with 2G_cc in place of G_cc for complex sources, as GV55's BFT-2 step does), put
  **ε̂_* := min{C₀/(2G_ccK_ε(C₀ + 1)), 1/(4G_ccK_ε)}.**
Then, for every complex B with s ≤ ε₀ and every complex coefficient field with ‖ε̂‖_cf ≤ ε̂_*, uniformly in k ≥ 1 and T ≥ 3:
- **(a)** Φ̃^{ε̂}_Γ(x) := 𝓛_Γ^{−1}(S̃(x; B) − P_cc∇δF(x)) maps 𝔅 := {x ∈ Ker Γ : ‖x‖_{(σ)} ≤ C₀s} into itself with Lip ≤ ¾.
- **(b)** Its fixed point x*(B, ε̂) is the unique critical point of 𝔉_k^{ε̂}∘exp(·; B) in 𝔅 (slice-selected, as in Codex's
  corrected CCP).
- **(c)** BFT-1's weights (2, 2 + σ, 1) hold at x*(B, ε̂), with the unperturbed constants.
- **(d)** x* and the critical value 𝔉_k^{ε̂}(x*) are jointly holomorphic in (B, ε̂).
- **(e)** x*(0, ε̂) = 0 for every ε̂. Hence, by Cauchy, for every coefficient direction φ with ‖φ‖_cf ≤ 1, every n ≥ 1 and
  ‖ε̂‖_cf ≤ ε̂_*/2: ‖∂_t^nx*(B, ε̂ + tφ)|_{t=0}‖_{(σ)} ≤ n!(2/ε̂_*)^nC₀s.

*Proof.*
- **Every source is cc, whatever δF is.** S̃ is cc (CCP (a)), and P_cc u is cc for every u (HR (i): D^⊥(P^Tu) = u^⊥). No gauge
  invariance is used in this step.
- **Image and Lipschitz constant.** For x ∈ 𝔅, Codex §5.3 gives ‖Φ̃_Γ(x)‖ ≤ G_ccs + G_ccK(C₀ + 1)²s² ≤ C₀s/2 and
  Lip(Φ̃_Γ) ≤ ½. Note N^{(σ)}(P_cc u) ≤ N^{(σ)}(u) + J(P^TD^⊥u), since P^TD^⊥u is a plain current and J is N^{(σ)}'s plain
  slot. SA-K1 (i) with η_b = C₀s gives ‖𝓛_Γ^{−1}P_cc∇δF(x)‖ ≤ G_ccK_ε‖ε̂‖_cf(C₀ + 1)s ≤ C₀s/2, and SA-K1 (ii) gives a Lipschitz
  constant ≤ G_ccK_ε‖ε̂‖_cf ≤ ¼. So the image lies in 𝔅 and Lip ≤ ¾.
- **Fixed points are the critical points.** A fixed point x̃ lies in Ker Γ (Lemma FG (iii)) and satisfies M_{x̃}∇F^{ε̂}(x̃) = 0,
  with M_x := 1 − P^T(K′^T_x·)^⊥, by Lemma CD applied to F^{ε̂} := 𝔉_k^{ε̂}∘exp.
  - Lemma CD needs only K_x^T∇F^{ε̂}(x) = 0, i.e. invariance of F^{ε̂} under composite gauges trivial at level k.
  - Each w(F_p) is a class function of a plaquette holonomy, and each φ̂_c is composite-gauge invariant (PROOF Lemma N2-a (i)).
    The coefficients are fixed functions of position, which gauge transformations do not move.
  - For complex ε̂, the identity is affine in ε̂ and holds for real ε̂, hence for complex ε̂.
  - CCP (c)-(d) then apply verbatim: J(∇F^{ε̂}(x̃)) ≤ 2dc_BernL^{d−1}C₀s·J(∇F^{ε̂}(x̃)), which forces ∇F^{ε̂}(x̃) = 0. Codex's
    threshold 1/[2C_ccC₀] on ε₀ is unchanged. Conversely, a slice critical point in 𝔅 has D^⊥𝔑^{0,ε̂} = 0 and is fixed.
- **(c)** BA-3 and Codex (1) are statements about points of the ball.
- **(d)** Φ̃^{ε̂} is affine in ε̂ and holomorphic in (x, B) (Codex §4.3's local analytic completion; the complexified 𝓛_Γ^{−1}
  with 2G_cc). The iterates from x = 0 are jointly holomorphic and converge uniformly (Lip ≤ ¾), so the limit is holomorphic
  (BA-10's argument). The critical value is a holomorphic function evaluated at x*.
- **(e)** At x = 0 every term is stationary: ∇w(0) = 0, and every soft term is stationary at ρ = 0 in both arguments (TOWER-VAR
  (b), U0 (iv)). So 0 is the fixed point at B = 0. The derivative bound is Cauchy's estimate in t on |t| ≤ ε̂_*/2, with
  ‖x*‖ ≤ C₀s. ∎

*What SA-K is.* A theorem about the TREE-LEVEL object: BFT-0 (slice form), BFT-1 and BFT-2 on 𝒞_glob survive a complex
variable-coefficient perturbation of size ε̂_* in ‖·‖_cf, uniformly in k and T, with joint holomorphy in (B, ε̂). It is
conditional on exactly BFT-E's inputs (GV via GV-E, the lane-A linear package, Codex KOFF §4.3), plus the per-term structure
of Codex's row bounds and the Hölder product rule. The perturbation is absorbed by the contraction margin; no inverse other
than the unperturbed 𝓛_Γ^{−1} is used, so REVIEW_S22's anti-circularity clause is satisfied as in KFACTOR_OFF55 §1.3.
*What SA-K is not.* Not off 𝒞_glob; not the identification with E_k^br (NSL, and TOWER-VAR^η); not a statement about
fluctuation integrals.
*The one step I could not re-derive line by line.* That every constant behind Codex KOFF §4.3 (1)-(3) is a sum of per-term
absolute bounds, so that ε̂-weighting multiplies it by at most ‖ε̂‖_∞. Codex's text says so for the Wilson row and for the soft
words; I accept that reading and flag it for the Codex reviewer.

### 2.3 Lemma SA-J — the Hölder condition on ε̂_0 is genuine. Identity PROVEN-HERE; consequence ARGUED
**Identity.** Take the abelian quadratic composite with coefficients,
E(x) = ½Σ_pc_p(dx_0)_p² + Σ_l(κ_l/2)Σ_cc′_l(c)|(Q_lx_l − x_{l+1})(c)|². At any critical point, for every level-0 link b:
(d*(c·dx_0))(b) = −j_b, where j_b := (Q_0^T(κ_0c′_0r_0))(b) is the soft current at b.
- **d = 2.** Each link lies in exactly two plaquettes p_±, so **c_{p_+}F_{p_+} − c_{p_−}F_{p_−} = ∓j_b exactly** (F = dx_0).
- **d = 4.** Suppose c, c′ and the data are invariant under the translations parallel to a hyperplane {x_1 = t}. The
  gauge-invariant outputs (F, the residuals) are unique (PROOF Lemma N2-a, abelian: "the r_i and dB_0 are the same at every
  minimiser"), so they inherit that invariance. For a link b in direction ν ≠ 1, the plaquettes of the planes (μ, ν) with
  μ ≠ 1 contribute translates of the same value with opposite signs, which cancel. Hence
  **c(x_1)F_{1ν}(x_1) − c(x_1 − a)F_{1ν}(x_1 − a) = ±j_b**: the normal flux c·F_{1ν} is continuous up to the soft current.

**Consequence (ARGUED for the sizes).** Suppose the coefficient jumps by a relative amount δc across one fine step, at a place
where the curvature F is nonzero and the soft current is small compared with c·F. Then |F_+ − F_−| = |F||δc|(1 + O(δc)).
One fine step is L^{−k} coarse units, so the depth-k pointwise Hölder seminorm of the coarse curvature is
≳ |f||δc|L^{kα}.
- For a lattice-rough bare coefficient, δc ~ g_0²|Δh_η| ≳ r_src/(u_K + β_+K log L + R): logarithmic in ℓ_k/a, against a power.
- So **BFT-1's Campanato/Hölder clause cannot hold uniformly in k for lattice-rough coefficient fields, whatever the proof
  technique.**
- The smallness of the soft current is read off KFACTOR_OFF55's ball: own |r_0| ≤ L^{−(2+σ)(k−1)}η_b against own curvature of
  order L^{−2k}, a ratio of order L^{2+σ−σk}. This bounds the ball, not actual backgrounds from below, which is why the size
  part is only ARGUED.

**Reading.**
- The slowly-varying condition is needed already at layer 1 (tree level), not only for (F_R).
- It falls on ε̂_0 alone: the soft slots of N^{(σ)} are sup-norm slots.
- Per-site sources violate it. Smeared sources with fixed C^α test functions satisfy it asymptotically, because
  ε̂_0 = −g_0²h_η carries g_0². With η = Σ_iz_ih_i, |z_i| ≤ r_z and supports δ apart (ℓ_ref = 1):
  [ε̂_0]^∞_α ≤ 2g_0²r_z(max_i[h_i]^∞_α + 2δ^{−α}).
- **Repair for rough coefficients (not attempted).** A divergence-form problem with rough coefficients has a regular FLUX
  (1 + ε̂_0)F, not a regular curvature. A contraction measuring the flux's Campanato seminorm instead of the curvature's is the
  natural replacement. It needs a new linear estimate. OPEN.

### 2.4 Corollary SA-RW — per-step covariance with complex variable coefficients. PROVEN as an implication (abstract Δ; level 0)
**Statement.**
- Let K_0 := Õ_i be Corollary RW-triv's operator (trivial background, any level i, any k, T).
- Let Δ be any operator with |Δ| symmetric and entrywise |Δ| ≤ ‖ε̂‖_∞·Ĥ_i, where Ĥ_i is a fixed symmetric nonnegative block
  kernel with N_0(Ĥ_i), D_m(Ĥ_i), N_m(Ĥ_i) finite uniformly in i, k, T.
- Fix m < m_cov with 𝔇(m) < γ_i/2 strictly, and put **ε̂_RW := (γ_i/2 − 𝔇(m))/(D_m(Ĥ_i) + N_0(Ĥ_i)/2)**.

Then for ‖ε̂‖_∞ ≤ ε̂_RW, Theorem RW (i)-(v) hold for K = Õ_i + Δ with γ′ = γ_i − ‖ε̂‖_∞N_0(Ĥ_i) and S_m + ‖ε̂‖_∞N_m(Ĥ_i).
Every walk term, the inverse, its square root and the s-weakened forms are holomorphic in ε̂ (Lemma CT♯, last sentence).

*Proof.* Apply Lemma CT♯ (PROOF l.5560) to each compression: K_0 restricted to Ω is ≥ γ_i (Rayleigh quotient, as in RW-triv),
‖Δ_Ω‖ ≤ N_0(|Δ|) ≤ ‖ε̂‖_∞N_0(Ĥ_i) (Schur test with the symmetric majorant), and D_m(|Δ_Ω|) ≤ ‖ε̂‖_∞D_m(Ĥ_i). So CT♯'s
condition D_m(|K_0|) + D_m(|Δ|) ≤ (γ − δ)/2 holds by the choice of ε̂_RW. (RW2) follows by the triangle inequality. ∎

**Identification of Δ.**
- At level 0, Δ = Π[Σ_pε̂_0(p)Hess w_p + κ_0Σ_cε̂_0(c)Hess φ̂_c]Π is finite range. This holds at the trivial background and,
  with N5-sf0's local gauges, at curvature-small backgrounds. So Ĥ_0 exists: PROVEN.
- At levels i ≥ 1 the coefficients enter Õ_i through the minimised finer levels. An entrywise-decaying majorant ∝ ‖ε̂‖ is
  ARGUED: the derivative of a minimised quadratic form in its coefficients is the coefficient-weighted form at the minimiser,
  and the minimiser map decays by N5-triv's lemmas. Not written out.
- **No Hölder condition is needed**: walk expansions are ℓ^∞-type statements. Dimock I (1108.1335, p.13, after (104)) absorbs
  complex decoupling parameters |s_□| ≤ M^{1/2} in the same way, by the walk-expansion margin.
- N5 at levels ≥ 1 at general backgrounds is OPEN at ε̂ = 0 too; SA-RW does not change that.

### 2.5 Lemma SA-WD — coupling-locality of the background. PROVEN as an implication
**Inputs.**
- BFT34_55's (H1), (H2)_m and (H3)_m. (H1) is Codex-confirmed via KOFF/GV. The GV-E_m piece of (H2)_m is CONFIRMED by
  CODEX_REVIEW_GV item 6, which BFT34_55's table still lists as "pending". (H3)_m is ARGUED there.
- **(H3^{ε̂})_m (ARGUED, exactly as (H3)_m: every row has finite range).** For φ supported in Y with ‖φ‖_cf ≤ 1:
  N^{(σ)}_{m,dist(·,Y)}(P_cc∇_xδF_φ) ≤ e^{c_rm}S_φ(η_b + s). Here δF_φ is δF with ε̂ = φ.

**Statement.** On the domain of SA-K (with BFT3-glob's threshold ε₀(m)),
‖∂_φx*‖_{(σ),m,dist(·,Y)} ≤ 2e^{c_rm}G_♯(m)S_φ(η_b + s). Hence |∂_φx^c_j(b)| ≤ 2e^{c_rm}G_♯(m)S_φ(η_b + s)e^{−m·dist(b,Y)}.
Several coefficient directions: BB-C as in Theorem BFT3-glob, with rates m/n.

*Proof.* Lemma WD (BFT34_55 §1.2) verbatim, with ∂_φS̃^{ε̂} = −P_cc∇_xδF_φ in place of ∂_{B_y}S̃: both are cc, and the Neumann
series is the same. ∎

**What it gives, and what it does not.**
- The factor (η_b + s): the background's response to a coefficient change is proportional to the background, and vanishes at
  trivial data (SA-K (e)).
- SA-WD is the tree-level part of the coupling-locality that SRC needs: the classical part of Proposition F and of κ-3's
  quasi-locality, in the SOURCE variable, just as BFT-3 supplies it in the COARSE-FIELD variable.
- It gives no covariance decay (§3.7).

### 2.6 Lemma SA-F — the marginal perturbation stays bounded along the flow. PROVEN as an implication of (Flow-an) + (F_R)
**Setting.** A scalar recursion u_{j+1} = u_j + b_j(u_j) for the chain's own coupling (constant couplings), with (F_R) along
the unperturbed trajectory. Write c_j(u) := b_j(u) + β_0^{std}log L, the deviation from one loop.
**Hypothesis (Flow-an).** There are ρ ∈ (0, ½] and C_b < ∞ such that each b_j is holomorphic on |u − u_j| ≤ ρu_j, with
|c_j(u)| ≤ C_bg_j² there.
**Statement.** If |δu_0|·exp((2C_b/ρ)Σ_{j<K}g_j⁴) ≤ (ρ/2)(u_K − R), then the perturbed trajectory exists up to level K, with
**|δu_j| ≤ |δu_0|exp((2C_b/ρ)Σ_{i<j}g_i⁴)**, and **Σ_{j≤K}g_j⁴ ≤ (u_K − R)^{−2} + (β_−log L)^{−1}(u_K − R)^{−1}, uniformly in K.**
*Proof.*
- Cauchy on the disc of radius ρu_j/2 about any point within ρu_j/2 of u_j gives |c_j′| ≤ C_bg_j²/(ρu_j/2) = 2C_bg_j⁴/ρ.
- So |δu_{j+1}| = |δu_j + c_j(u_j + δu_j) − c_j(u_j)| ≤ |δu_j|(1 + 2C_bg_j⁴/ρ), as long as |δu_j| ≤ ρu_j/2.
- That proviso holds by induction, because u_j ≥ u_K − R by (F_R) (u_j − u_K ≥ β_−(K − j)log L − R ≥ −R).
- (F_R) also gives g_j² ≤ (u_K − R + β_−(K − j)log L)^{−1}. Then Σ_{m≥0}f(m) ≤ f(0) + ∫_0^∞f for decreasing f, and
  ∫_0^∞(A + Bt)^{−2}dt = 1/(AB). ∎

**Reading.**
- (Flow-an) is an ANALYTIC form of the open flow wall. It is not implied by (UIR^♮) as banked: Codex FLOW55 item 4 says "Its
  scalar bound does not imply the stronger integrand estimates", and (UIR^♮) is itself NOT-VERIFIED.
- By Cauchy, (Flow-an) gives |∂_ub_j| ≤ 2C_bg_j⁴/ρ: the analytic form of UNIV55 (N1)'s marginal equation
  m_{j+1} ≤ (1 + Cg_j⁴)m_j, whose "Σ_ig_i⁴ < ∞ on an AF trajectory" it shares.
- This is where asymptotic freedom makes a marginal source harmless. δ(1/g²) is RG-invariant at one loop (SRCCD55 §5.4 item 1),
  and its propagation is multiplied by Π_j(1 + O(g_j⁴)), which is summable.
- The admissible size is |δu_0| ~ ρ/(2g_ref²), matching SRCCD55's "r_0 ≪ 1/g_ref²". The relative coupling perturbation stays
  ≤ ρ/2 at every level.
- With a source, the chain is no longer at its own-coupling fixed point (RLARGE "a fixed-point condition (A5)"): the kernels
  keep u_j, while the effective coupling moves by δu_j. That mismatch is the soft coefficient ε̂_j of §2.1. It is covered at
  tree level by SA-K (needs ρ/2 ≤ ε̂_*) and at the linear per-step level by SA-RW. For RLARGE's FI-1/W-cb♯, which are proved at
  the fixed point, it is NOT-VERIFIED.
- **Position-dependent couplings.** The local flow plus gradient terms. The gradient terms are irrelevant by dimension counting
  (PANEL_P4 S4(a): "pure YM has no gauge-invariant local operator of dimension < 4", ARGUED there). OPEN, as SRCCD55 §6 (M1)
  "(F_R)^η" says.

**Erratum E1 to §2.3 (found on re-reading, appended at once; the text above is left as written).**
- The d = 4 bullet's argument is WRONG. The soft kernel's block structure (Q_l averages inside blocks) breaks fine translation
  invariance down to COARSE translations. So the plaquettes of the planes (μ, ν), μ ≠ 1, do not cancel pointwise, and the
  appeal to uniqueness is beside the point.
- **Corrected statement (exact; abelian quadratic, d = 4).** Let c depend only on x_1, one value per plaquette layer.
  - Sum the critical-point identity d*(c·dx_0)(b) = −j_b over ALL ν-links b of the periodic hyperplane {x_1 = t}, ν ≠ 1.
  - The (μ, ν) terms with μ ∉ {1, ν} telescope along the periodic direction μ to zero.
  - What remains is **c(t)F̄_{1ν}(t) − c(t − a)F̄_{1ν}(t − a) = −j̄_ν(t)**, with F̄, j̄ the averages over the slice.
  - Hence max over the slice of |F_{1ν}(t, ·) − F_{1ν}(t − a, ·)| ≥ |F̄_{1ν}(t) − F̄_{1ν}(t − a)|.
- The d = 2 identity and the Consequence/Reading paragraphs are unchanged, with F replaced by its slice average in d = 4.

### 2.7 T1 table — every place the coupling enters, and whether the estimate survives on a complex polydisc
| # | Where the coupling enters (file: locating string) | How it enters | Verdict (this file) |
|---|---|---|---|
| 1 | Bare Wilson coefficient (RLARGE "Action normalisation"; tilt of W_ch) | u_0 → u_0 − h_η(p); relative ε̂_0 = −g_0²h_η | exact (§2.1), PROVEN-HERE |
| 2 | Soft kernels k^{(i)}_c, their couplings κu_i and normalisations (RLARGE "The exact chain") | NOT perturbed: kernels fixed (needed for Proposition B and Φ_K = −ΔS_K) | exact, PROVEN-HERE (§2.1); the source enters steps i ≥ 1 as a mismatch ε̂_i (output of the flow) |
| 3 | 𝔉_k's Wilson term (BFT_A §1.1; KFACTOR_OFF55 §1.1) | coefficient 1 + ε̂_0 | CONFIRMED via Proposition SA-K, with [ε̂_0]^∞_α ≤ ε̂_* (Lemma SA-J: genuinely needed) |
| 4 | 𝔉_k's soft terms | coefficients 1 + ε̂_l | CONFIRMED via SA-K, sup norm only |
| 5 | CCP (a) "every source is cc" (KFACTOR_OFF55 §3.4) | perturbed source S̃ − P_cc∇δF | CONFIRMED (HR (i); no invariance needed) |
| 6 | Lemma CD (root-pinned) and CCP (c)-(d) | needs K_x^T∇F^{ε̂} = 0 | CONFIRMED (gauge invariance of the weighted terms; affine in ε̂) |
| 7 | Lemma SG, ROW^{(σ)}, Codex KOFF §4.3 (1)-(3) | per-link rows × ε̂_l(c), plus NEW linear rows | CONFIRMED as Lemma SA-K1, modulo the per-term reading flagged in §2.2 |
| 8 | Wilson rows (LA-3, Corollary WR (a), Codex's Wilson Hölder bounds) | ε̂_0∇w(F), (Dq)^T(ε̂_0∇w(F)) | CONFIRMED with [ε̂_0]^∞_α; the plain row alternatively by HR (iii) and k g_0² ≤ 1/(β_−log L) |
| 9 | Proposition CB (cc correction; HR (iii)/(iv)) | ε̂-weighted plain rows | CONFIRMED (SA-K1 (i)-(ii)) |
| 10 | Linear estimates: GV/GV-E, LIN^{(σ)}, TOP♯, data map | unperturbed 𝓛_Γ^{−1}; complexified with factor 2 | unchanged (inputs of BFT-E) |
| 11 | Contraction arithmetic (Codex KOFF §5.3) | extra image C₀s/2, extra Lipschitz ¼ | CONFIRMED (SA-K (a)): ε̂_* = min{C₀/(2G_ccK_ε(C₀+1)), 1/(4G_ccK_ε)} |
| 12 | BFT-1 (BA-3, Codex (1)) | statements about the ball | CONFIRMED (SA-K (c)) |
| 13 | BFT-2 (BA-10) | joint holomorphy in (B, ε̂) | CONFIRMED (SA-K (d)) |
| 14 | Slice Γ_E / Γ^{(T)}, Proposition SM | coupling-independent | unaffected |
| 15 | BFT-0 identification (NSL; E_k^br; TOWER-VAR (a)) | per-step coupling fields | NOT-VERIFIED (NSL as before; TOWER-VAR^η OPEN) |
| 16 | Per-step covariance (Theorem RW, CT♯, RW-triv, N5-sf0) | Hessian + ε̂-weighted Hessian | CONFIRMED as Corollary SA-RW for abstract Δ and at level 0; levels ≥ 1 ARGUED (and N5 there OPEN at ε̂ = 0) |
| 17 | Per-step polymer bound N6 | interaction terms with complex coefficients | NOT-VERIFIED (N6 OPEN at ε̂ = 0) |
| 18 | Large fields (RLARGE "Indicators", "Thresholds", the defect exponent) | thresholds ε_1 fixed, coupling-free; suppression e^{−au_k} uses Re u ≥ u_k(1 − ρ/2) | ARGUED to survive: indicators do not depend on η, so the decomposition is termwise analytic; bounds use |e^{−us}| = e^{−Re(u)s}. RLF itself OPEN |
| 19 | Chessboard/RP (Lemma CBE, SRC-I) | lost for complex AND for non-reflection-symmetric real couplings | NOT needed for the complex part: used only for the real coarse law ν_K (SRC-I), at η = 0 |
| 20 | Flow (F_R) and its fixed-point (own-coupling) condition | δu_j propagates; mismatch with fixed kernels | Lemma SA-F PROVEN as implication of (Flow-an) for constant shifts; position-dependent OPEN; FI-1/W-cb♯ at a mismatch NOT-VERIFIED |

---

## §3. T2 — from analyticity to SRC-κ: what Cauchy actually delivers, and which locality is needed

### 3.1 Lemma SA-CF (the Cauchy floor) — PROVEN-HERE. A counterterm must be removed before any uniform polydisc bound
**Statement.** Let X_1, X_2 be bounded real random variables (under any law, conditional or not), and
Φ(z) := log E[e^{z_1X_1 + z_2X_2}]. If Φ is holomorphic on the closed polydisc {|z_1| ≤ ρ_1, |z_2| ≤ ρ_2} with |Φ| ≤ A there,
then Var X_i ≤ 2A/ρ_i². Hence the Cauchy bound A/(ρ_1ρ_2) for |Cov(X_1, X_2)| is ≥ ½(Var X_1·Var X_2)^{1/2}.
*Proof.* z_1 ↦ Φ(z_1, 0) is holomorphic on |z_1| ≤ ρ_1 and bounded by A, and Var X_1 = ∂_1²Φ(0). Cauchy gives Var X_1 ≤
2!A/ρ_1²; the same holds for X_2. Then A/(ρ_1ρ_2) ≥ A·(Var X_1/2A)^{1/2}(Var X_2/2A)^{1/2}. ∎

**Consequences.**
- Cauchy estimates on the FULL log-generating function can never beat Cauchy–Schwarz by more than a factor 2.
- With Lemma V (Codex SRCCD item 3: Var_ω(O_a(f)) ≥ (3/2000000)g_0⁴a^{−4}(‖f‖₂² − O(a))), every polydisc on which the full
  unconditional generating function of (e(h_1), e(h_2)) is bounded by A gives a Cauchy bound
  ≥ (3/4000000)g_0⁴a^{−4}‖h_1‖₂‖h_2‖₂(1 − O(a)). Under (F_R) this is ≍ a^{−4}/log²(ℓ_ref/a).
- So **no a-uniform polydisc with an a-uniform bound exists for the full generating function.** The uniform statement must be
  made for Φ − CT, with the counterterm CT carrying the coincident divergence.
- Separated mixed derivatives do not see CT if each of its terms depends on η only in a ball of radius smaller than half the
  separation (Codex SRCCD item 2, CONFIRMED). SRC-poly's CT[η] is therefore NOT optional, and "uniform bounds on the generating
  function" in the corpus's sense (2204.07201 p.2) can only mean bounds after this subtraction.
- *Remark, not used.* SRC-poly asks CT to be U_K-independent. Contact terms proportional to e itself (the OPE term e(x)e(y) ⊃
  C_e(x − y)e(y)) would make the coincident part U_K-dependent. Proposition A needs only the range property, not
  U_K-independence. Not settled here.

### 3.2 Lemma SA-PC (pair Cauchy) and Lemma SA-TC (two constants) — PROVEN-HERE (elementary complex analysis)
**Lemma SA-PC.** Let Φ be holomorphic on the closed polydisc D := {|z_i| ≤ r_z, 1 ≤ i ≤ n}, n ≥ 2. Fix a pair i* ≠ j* and put
h := ∂_{i*}∂_{j*}Φ. Then |∂_1⋯∂_nΦ(0)| ≤ r_z^{−(n−2)}·sup_D|h|.
*Proof.* ∂_1⋯∂_nΦ(0) = ∂^{α}h(0), with α the indicator of the other n − 2 indices. Cauchy for a multi-index with all
α_i ≤ 1 has α! = 1. ∎ No n! appears, unlike BB-C (BFT34_55 §1.3), which allows repeated indices.

**Lemma SA-TC.** In the setting of SA-PC put 𝒰_ℂ := sup_D|h| and 𝒰_ℝ := sup_{D∩ℝ^n}|h|. Then for every r ∈ (0, 1),
  **|∂_1⋯∂_nΦ(0)| ≤ (r·r_z)^{−(n−2)}·𝒰_ℂ^{1−ω_hm(r)}·𝒰_ℝ^{ω_hm(r)},  ω_hm(r) := 1 − (4/π)arctan r.**
(ω_hm(½) ∈ [0.4096, 0.4098], certified by `checks/sa55_hm`; ω_hm(r) → 1 as r → 0.)
*Proof.*
- **Polarisation.** Let I be the n − 2 indices other than i*, j*. For ε ∈ {±1}^I put v_ε := Σ_{i∈I}ε_ie_i and
  g_ε(t) := h(tv_ε). Then ∂^Ih(0) = T(e_{i_1}, …, e_{i_{n−2}}) for the symmetric (n−2)-linear form T := D^{n−2}h(0), and
  g_ε^{(n−2)}(0) = T(v_ε, …, v_ε). The polarisation identity
  **T(e_{i_1}, …, e_{i_{n−2}}) = (2^{n−2}(n − 2)!)^{−1}Σ_ε(Π_iε_i)T(v_ε, …, v_ε)**
  is checked exactly in `checks/sa55_hm` (C1), including a designed-FAIL control.
- **One variable.** g_ε is holomorphic on |t| ≤ r_z (since |tv_ε|_∞ = |t|), with |g_ε| ≤ 𝒰_ℂ there and |g_ε| ≤ 𝒰_ℝ on the real
  diameter. On the upper half-disc, log|g_ε| is subharmonic, ≤ log 𝒰_ℝ on the diameter and ≤ log 𝒰_ℂ on the arc.
- So log|g_ε(t)| ≤ ω(t)log 𝒰_ℝ + (1 − ω(t))log 𝒰_ℂ, where ω is the harmonic measure of the diameter (maximum principle; the two
  corner points are polar). The lower half-disc is symmetric.
- **The harmonic measure.** ω(t) = 1 − (2/π)arg((r_z + t)/(r_z − t)). For t = r_z·re^{iθ}, 0 < θ < π:
  (1 + τ)/(1 − τ) = (1 − r² + 2ir sin θ)/|1 − τ|², so arg = arctan(2r sin θ/(1 − r²)) ≤ arctan(2r/(1 − r²)) = 2arctan r.
  Hence ω ≥ ω_hm(r) on the circle |t| = rr_z. The identity and the monotonicity are checked exactly in `checks/sa55_hm` (C3).
- **Cauchy and assembly.** Since 𝒰_ℝ ≤ 𝒰_ℂ, the bound 𝒰_ℝ^ω𝒰_ℂ^{1−ω} decreases in ω. So |g_ε| ≤ 𝒰_ℂ^{1−ω_hm}𝒰_ℝ^{ω_hm} on that
  circle, and Cauchy gives |g_ε^{(n−2)}(0)| ≤ (n − 2)!(rr_z)^{−(n−2)}𝒰_ℂ^{1−ω_hm}𝒰_ℝ^{ω_hm}. Sum the 2^{n−2} signs. ∎

**Reading.** Decay supplied on the REAL section alone is transferred to every order at the rate fraction ω_hm(r) (any value
< 1). The complex polydisc needs only a bound, with no decay and no positivity.

### 3.3 Proposition SA-S — smeared SRC-κ (e-part, all orders) from [complex uniform bounds] + [real CD]. PROVEN as an implication
**Setting.**
- U_K ∈ 𝒮_K. Real test functions h_1, …, h_n with ‖h_i‖_∞ ≤ 1, supports X_i at mutual distance ≥ δ.
- Φ(z; U_K) := log E_K[exp Σ_iz_ie(h_i)].

**Hypotheses.**
- **(A) Complex, no decay.** There are r_z > 0 and 𝒰_ℂ < ∞, uniform in a ≤ a_0, R and U_K ∈ 𝒮_K, such that
  E_K[exp Σ_iz_ie(h_i)] ≠ 0 on the closed polydisc |z_i| ≤ r_z, and sup over the polydisc of |∂_i∂_jΦ| ≤ 𝒰_ℂ for every pair i ≠ j.
- **(B) Real, decay.** For real z ∈ [−r_z, r_z]^n and every pair, |∂_i∂_jΦ(z)| ≤ C_ℝe^{−μ_Rd(X_i, X_j)}.
  - This is CD for the real-tilted conditional laws: soft chains with the real bare coupling u_0 − Σ_iz_ih_i(p), positive as
    long as 2r_z < u_0.

**Conclusion.** For every r ∈ (0, 1), with d_max := max_{i,j}d(X_i, X_j) ≥ 𝔱(X_1, …, X_n)/(n − 1):
  **|κ_n(e(h_1), …, e(h_n) | U_K)| ≤ (r·r_z)^{−(n−2)}·𝒰_ℂ^{1−ω_hm(r)}·C_ℝ^{ω_hm(r)}·e^{−ω_hm(r)μ_Rd_max}.**
*Proof.* Lemma SA-TC with the pair attaining d_max; then 𝒰_ℝ ≤ C_ℝe^{−μ_Rd_max}. ∎

**Remarks.**
- Constants grow geometrically in n; there is no n! for distinct indices. The rate is any fraction < 1 of μ_R in d_max, i.e.
  ω_hmμ_R/(n − 1) in spanning-tree length.
  - This avoids Codex SRCCD §2's MST-versus-Steiner problem entirely: only pair distances are used.
- **The hypotheses separate the two hard parts.**
  - (A) is a stability/analyticity statement for the complex-coupling RG, with no decay and no positivity.
  - (B) is CD at REAL position-dependent couplings, where Proposition B (Markov, Codex-confirmed), Corollary B′'s probabilistic
    averaging, and positivity are all available.
  - So "Cauchy estimates turn uniform bounds into separated cumulant bounds" holds in this precise sense: **decay must be
    proved at second order only, and only for real couplings; every higher order and every complex point need only uniform
    bounds.**
- **What (A) needs**, in T1's terms:
  - SA-K (tree level; PROVEN as implication) and SA-RW (linear per step; PROVEN at level 0 and for abstract Δ).
  - N5 at levels ≥ 1, N6 and RLF per step conditional on U_K, each with complex coefficients: OPEN (OPEN at ε̂ = 0 too).
  - (Flow-an) for SA-F; TOWER-VAR^η.
  - A volume-uniform bound on ∂_i∂_jΦ. This is a ROOTED summability statement: Φ − CT = Σ_X𝔞(X) with
    Σ_{X∋□}sup|𝔞(X)| ≤ A_root, after which the polymers meeting both supports contribute at most N(X_i)A_root. No decay of the
    activities is needed, only rooted summability: OPEN.
- **What (B) needs.** The original CD problem, uniformly over real slowly varying coupling fields (SRCCD55 §6 (M1)): OPEN.
- **Relation to SRCCD55's Proposition A.** If SRC-poly holds with DECAYING activities |𝔞_r(X)| ≤ A_re^{−κ_sd_r(X)}, decay comes
  from polymer geometry (Codex's two-set bound d_r ≥ dist/(Mℓ_r) − 4) and (B) is unnecessary. SA-S is the alternative when the
  complex-polydisc representation is only summable, not decaying.
- **Smearing class.** (A) requires SA-K's Hölder condition on ε̂_0 = −g_0²Σ_iz_ih_{i,η}, which holds once
  g_0² ≤ ε̂_*/(4r_z(max_i[h_i]^∞_α + 2δ^{−α})) (§2.3, Reading). That is a condition a ≤ a_0(δ, [h]_α, r_z), vacuous as a → 0
  for fixed test functions.

**Check record.** `checks/sa55_hm` (criteria `sa55_hm_criteria.md` written 03:27Z, before the script; run
`python3 -B sa55_hm.py`; output `sa55_hm_out.txt`):
- C1, the polarisation normaliser (2^p p!)^{−1}, holds exactly on 15 random symmetric forms, p ≤ 5. Its control, the
  normaliser without p!, fired at every p ≥ 2; it cannot fire at p = 1, where the two normalisers coincide, as pre-stated.
- C2 gives ω_hm(½) ∈ [0.409665529, 0.409665530] (outward rounding), with π ∈ [3.141592653589, 3.141592653590]. The control
  "ω_hm(½) ≥ ½" was rejected. Informational: ω_hm(¼) ∈ [0.688083478, 0.688083479], ω_hm(1/10) ∈ [0.873097930, 0.873097931].
- C3: the identities Re w = (1 − r²)/|1 − τ|² and Im w = 2r sin θ/|1 − τ|², Re w > 0, and the maximum at θ = π/2 equal to
  2r/(1 − r²) all hold on 27 rational samples. The wrong-formula control fired.
- **VERDICT: PASS.**
- **What it cannot decide:** the maximum principle step and anything about Yang–Mills (stated in the criteria).

### 3.4 Pointwise weights (κ-1's δ^{−4} per point): the analyticity route does NOT deliver them, and why
- **(a) The slowly-varying condition (Lemma SA-J).** Per-site sources violate [ε̂_0]^∞_α ≤ ε̂_* at every depth k with
  ℓ_k ≫ a. The lane's C^{1,α} BFT-1 clause FAILS for coefficient fields that are rough at the lattice scale (flux identity
  plus erratum E1). This is pre-stated refutation R5 realised.
- **(b) A point source is not a small perturbation.** a⁴e_a(x) = ½Σ_{p∋x}s(U_p) ∈ [0, 24] (Lemma V Step 0 with f = a^{−4}1_x;
  24 plaquettes have a corner at x). So z·e_a(x) shifts the Wilson coefficient of those 24 plaquettes by za^{−4}/2, a relative
  change of |z|a^{−4}g_0²/2.
  - A perturbative polydisc therefore has radius |z| ≲ a⁴u_0, and Cauchy returns the trivial bound a^{−4}g_0² per insertion.
  - Lemma SA-CF makes this sharp for the FULL generating function. The single-site variance is of order g_0⁴a^{−8}: this is
    ARGUED by the single-link conditional-variance argument of Lemma V Steps 2-6 and is not written out.
  - The resulting Cauchy bound exceeds the target w_e(δ)² = δ^{−8}𝔤² by a factor ≳ g_0⁴(δ/a)^8. This is pre-stated
    refutation R3 realised for pointwise weights, and that is the size of the shortfall.
- **(c) What would deliver them — the Markov/image route, not analyticity.**
  - Use Proposition B (Codex-confirmed): Cov(e_a(x), e_a(y) | U_K) = Σ_iE[Cov(I_i(x), I_i(y) | U_{i+1}) | U_K], with
    I_i(x) := E[e_a(x) | U_i].
  - If (P1) every image I_i(x), minus its U_i-independent part, is a level-i local function of size ≲ ℓ_i^{−4}𝔤 (canonical
    scaling at EVERY level),
  - and (P2) the per-step covariance of two level-i local functions at distance D obeys ≲ e^{−m_1D/ℓ_{i+1}} (Corollary B′'s
    hypothesis, at small fields; Codex SRCCD item 1 adds the large-field term),
  - then Σ_iℓ_i^{−8}e^{−m_1δ/ℓ_{i+1}} ≍ δ^{−8}: the pointwise weight at n = 2.
  - Higher n need the triangular higher-order recursion (SRCCD55 §5.0).
  - (P1) is the first-order source-linearised RG at every level: SRCCD55's "SRC to first order". It is OPEN. ARGUED reduction.
- **(d) Consequence for OS0: a scale window.** SA-S needs [ε̂_0]^∞_α small, i.e. test functions varying on scales
  δ ≥ δ_a := (4g_0²r_z·C/ε̂_*)^{1/α}. Under (F_R), δ_a ≍ (log(ℓ_ref/a))^{−1/α}.
  - OS0 in OS's ^0𝒮 form needs bounds on Whitney pieces at every scale δ ≥ ca. The window [ca, δ_a) is not covered.
  - It cannot be closed by the trivial bound ‖e_a‖_∞ ≤ Ca^{−4}: a piece at scale δ ≥ a contributes up to ~δ_a^{M+4}a^{−4n},
    which diverges, because δ_a ≫ a^{1/2}.
  - Closing it needs (c), or a contraction in a FLUX norm tolerating rough coefficients (§2.3, Reading), or TOWER-VAR^η with
    per-level smoothed coupling fields. All OPEN.
  - This window is a NEW obstruction for the analyticity route to OS0. It shrinks only logarithmically.

### 3.5 The 46 linear insertions (κ-2) need no sources of their own — Lemma SA-TI, PROVEN-HERE
**Statement.** For a bounded observable O and bounded X_1, …, X_m (any law, in particular E_K[·]), with
⟨O⟩_z := E[Oe^{Σz_iX_i}]/E[e^{Σz_iX_i}] on the set where the denominator does not vanish:
  **κ(O, X_1, …, X_m) = ∂_{z_1}⋯∂_{z_m}⟨O⟩_z|_{z=0}.**
*Proof.* ⟨O⟩_z = ∂_wlog E[e^{wO+Σz_iX_i}]|_{w=0}. Mixed derivatives of the joint log-generating function at 0 are the joint
cumulants, and the derivatives commute. ∎

**Consequence.**
- κ-2's |κ_{n+1}(O_α(x), e_a(x_1), …, e_a(x_n) | U_K)| is a mixed z-derivative of the e-TILTED conditional one-point
  function of O_α(x).
- So **pre-stated refutation R1 is NOT realised.** No couplings for τ, 𝒯 or 𝔴 are needed. The single scalar coupling field
  (the e-source) suffices, together with:
  - (A_O) a uniform bound, on the complex polydisc, on the tilted covariance Cov^{(z)}(O_α(x), e(h_j) | U_K) for the
    farthest j, with the pointwise weight w_α(δ_0) for the POINT insertion O_α(x);
  - (B_O) its real-tilt decay.
  - SA-TC then gives the rest.
- The pointwise weight w_α(δ_0) is again the image route's (P1), now for O_α: OPEN.
- The diagonal 𝒯 components (plane energies) also admit sources in SA-K's class, but they do not need them.

### 3.6 The singleton (κ-3 for e): tree level supplied, fluctuation part reduced to one input (LOC-e)
**Lemma SA-E1 (tree-level image of e). PROVEN as an implication of BFT-E (GV55 Theorem BFT-E; Codex GV item 4).**
- On BFT-E's domain at depth K (U_K = e^{B} ∈ 𝒞_glob(ε₀), s = ‖B‖_D, η_b = C₀s), the classical clover energy of the background,
  E^{tree}_K[e(h)] := Σ_ph(p)s(U^{bg}_p), obeys for ‖h‖_∞ ≤ 1:
  **|E^{tree}_K[e(h)]| ≤ 3·|supp h|·ℓ_ref^{−4}·(2η_b + 9η_b²)²**,
  uniformly in a, R. Here |supp h| is the physical volume, up to a boundary layer of one lattice spacing.
- It is the z-derivative at 0 of the tilted tree-level conditional action: by SA-K (d) and the envelope identity
  ∂_z[𝔉^{ε̂(z)}_K(x*(z))] = (∂_z𝔉^{ε̂(z)}_K)(x*), since ∇𝔉(x*) = 0 in all directions (CCP (d)). After restoring the factor u_0,
  the g_0² in ε̂_0 cancels.
- Its quasi-locality in U_K at tree level follows from Theorem BFT3-glob (n = 1) composed with the local energy density.
*Proof of the bound.*
- s(e^X) ≤ |X|_F²/(2N) ≤ |X|²_op/2 (Lemma V Step 1). Own plaquette logs are ≤ L^{−2K}(2η_b + 9η_b²) (BA-3).
- At most 6|supp h|a^{−4} plaquettes meet supp h; and a^{−4}L^{−4K} = ℓ_ref^{−4}. ∎ (The norm in BA-3's "own plaquette logs"
  is taken as the operator norm; with the Frobenius norm the 3 becomes 3N.)

**(LOC-e), the missing input (OPEN), stated precisely.**
- Statement: in a multiscale representation E_K[e(h)] = Σ_{r≤K}𝔦_r(h; U_K) whose level-r term depends on U_K only through the
  level-r background and fluctuation structure (for instance the η-derivatives of SRC-poly's level-r polymers), the
  oscillations satisfy
  **Osc_{U_K∈𝒮_K}𝔦_r(h; ·) ≤ c_r‖h‖_{L¹}ℓ_ref^{−4} with Σ_rc_r < ∞, uniformly in a and R.**
- Why sup bounds are not enough: with SRC-poly's sup bounds A_r alone, the sum over the ~|supp h|ℓ_r^{−4} level-r polymers
  meeting supp h diverges like a^{−4}. So (κ-3) does NOT follow from SRC-poly as stated (sup_rA_r < ∞), whereas κ-1 at n ≥ 2
  does (the polymers must reach a distant support).
- **Mechanism (ARGUED).**
  - Gauge invariance makes the level-r U_K-dependence quadratic in the level-r background curvature, which is (ℓ_r/ℓ_ref)⁴ in
    own units: canonical scaling.
  - Canonical scaling alone still leaves one O(1) term per level, i.e. log(ℓ_ref/a).
  - The summable coefficient is the η-derivative of the level-r coupling renormalisation. By (Flow-an) and Cauchy (Lemma SA-F),
    it is O(g_r⁴), because the one-loop coefficient is u-independent. Σ_rg_r⁴ < ∞.
  - The top-level term carries ∂u_K/∂u_0 = Π_r(1 + O(g_r⁴)) = O(1).
- This is the analyticity route's genuine contribution to Codex SRCCD §7's first gap: **the singleton is a statement about the
  coupling flow's derivative, which Cauchy controls once the flow is analytic.**

**Erratum E2 to Lemma SA-E1 (found on re-reading, appended at once; the text above is left as written).**
- The displayed constant 3 is wrong; it should be **6**, and the parenthetical about norms is backwards.
- The source of the error: I used h for both the test function and the plaquette weight. Correctly,
  e(h) = Σ_ph_□(p)s(U_p) with h_□(p) := ½Σ_{x∈corners(p)}h(x), so |h_□| ≤ 2.
- Σ_p|h_□(p)| ≤ ½·24·Σ_x|h(x)| ≤ 12|supp h|a^{−4}, and s ≤ |X|²_op/2 ≤ L^{−4K}(2η_b + 9η_b²)²/2.
- Hence **|E^{tree}_K[e(h)]| ≤ 6|supp h|ℓ_ref^{−4}(2η_b + 9η_b²)²**. If BA-3's plaquette-log norm is the Frobenius norm, the
  constant improves to 6/N (s ≤ |X|_F²/(2N)), not "3N". Check of the normalisation: f ≡ 1 gives Σ_p|h_□| = 12·#sites,
  matching Lemma V's "2Σ_ps(U_p)".

### 3.7 Which locality is needed — and why it is not BFT-3 (pre-stated R4 REALISED)
- **Analyticity plus uniform bounds produce no decay.** Φ(z_1, z_2) = z_1z_2 is entire and bounded on every polydisc, and its
  mixed derivative is 1 at every separation. BFT34_55's Proposition CX (re-read; its Lemma NC proof checked) is the stronger
  form: analyticity together with derivative decay at every fixed order does not give a polymer representation. So decay is a
  genuine extra input.
- **Decay can enter in exactly two ways.**
  - **(D1) A decoupling (polymer) representation with decaying activities.**
    - This is SRC-poly; then Proposition A gives decay, with Codex's two-set geometry.
    - In the Balaban school decay comes from analyticity in DECOUPLING parameters (complex bond weights s_b or s_□), not in
      the coupling: BFT34_55 §2.3 (the cluster identity: "per-cube smallness from analyticity in bond weights s_b … not from
      decay of field derivatives", re-derived there); Dimock I (1108.1335, p.13, after (104)).
    - The coupling η is then a spectator, carried along by the same contraction margins (§2).
  - **(D2) Real CD plus complex uniform bounds** (Proposition SA-S).
- **What BFT-3 is and supplies.** BFT-3 (BFT34_55's Theorem BFT3-glob, conditional on (H1)-(H3)_m) is deterministic locality
  of the BACKGROUND in the coarse field. It supplies:
  - the tree-level part of κ-3's quasi-locality in U_K (Lemma SA-E1);
  - through the same mechanism (Lemma WD), the tree-level coupling-locality SA-WD;
  - through its weighted linear estimates (H2)_m, the tree-level part of per-step decay.
- **What BFT-3 does not supply.** Any covariance decay, which comes from N5/N6 per step, assembled by Proposition B
  (Codex-confirmed). SRCCD55 §5.1 and §8 (A3) say the same; **I agree.** The brief's phrase "exponential decay inherited from
  BFT-3-type locality" is therefore accurate only for the tree-level parts.
- **Precisely what (D1) needs.** The source-inserted RG with a decoupling family jointly holomorphic in (s, η):
  - at tree level, BFT34_55 §2.6 (a)'s s-family (NOT-VERIFIED there, reduced to local ARGUED items) with ε̂ as a spectator.
    SA-K1's rows are local and their P_cc-projections stay cc (§2.2), so the transport is ARGUED;
  - at the linear fluctuation level, Theorem RW (iv)'s complex s-weakening with SA-RW;
  - beyond that, N6. All OPEN beyond what §2 proves.

### 3.8 Against Codex SRCCD §7's three OS0 gaps — what the route does to each
**First gap (singleton).**
- Tree level: supplied (SA-E1, with E2).
- Fluctuation level: reduced to (LOC-e), whose summability mechanism is the flow derivative (SA-F).
- Not closed.

**Second gap (uniform all-order LF moments) — Proposition SA-MOM (moment transfer), PROVEN-HERE as an inequality.**
- *Statement.* Suppose SA-S's (A) and (B) hold pointwise in U_K with measurable envelopes 𝒰_ℂ(U_K) and
  𝒰_ℝ(U_K) := sup_{real cube}|∂_{i*}∂_{j*}Φ|. Let b ≥ 1 and q > 1, put ω := 1/(bq) and r := tan(π(1 − ω)/4) ∈ (0, 1), so
  that ω_hm(r) = ω, and let 1/p + 1/q = 1. Then
  **ν_K(|κ_n(· | U_K)|^b) ≤ (r·r_z)^{−b(n−2)}·ν_K(𝒰_ℂ^{p(b−1/q)})^{1/p}·ν_K(𝒰_ℝ)^{1/q}.**
- *Proof.* SA-TC gives |κ_n|^b ≤ (rr_z)^{−b(n−2)}𝒰_ℂ^{b−1/q}𝒰_ℝ^{1/q}; apply Hölder. ∎
- For the products of j conditional cumulants in Brillinger's formula, take ω = 1/(jbq) per factor and use the generalised
  Hölder inequality.
- *Reading.* Codex's counterexample (E[P^{11}] ≥ 2^ℓ) concerns HIGH moments of the decaying path envelope. SA-MOM needs only
  its FIRST moment, which Proposition C/E3 controls (Codex SRCCD §5: "This first-moment argument is valid"), together with all
  moments of the NON-decaying complex envelope 𝒰_ℂ.
- If 𝒰_ℂ(U_K) ≤ C·exp(C_LF|𝔏(U_K) ∩ (𝒩(X_{i*}) ∪ 𝒩(X_{j*}))|), with 𝒩 fixed finite neighbourhoods, it is bounded by
  Ce^{2C_LFN_𝒩} deterministically and the gap closes.
- Whether 𝒰_ℂ has that LOCAL form at large coarse fields is OPEN. SRCCD55 §3.4's caveat ("Correlations can then cross a
  large-field cluster without decay, at bounded cost per cube") warns that a path-type envelope may be the truth, in which
  case SA-MOM does not help.
- So the gap is **reduced** — from uniform high moments of a decaying envelope to moments of a non-decaying one — **not
  closed.** Defining 𝒰_ℂ at large coarse fields at all needs UNIV55's (N3) with complex tilts.

**Third gap (large-distance weight).**
- The route does not change it. SA-S's decay is CONDITIONAL.
- The unconditional statement must not ask for coarse decay, and I agree with Codex's repair, the weight w_e(min(δ, ℓ_ref)).
- OS0 needs no decay (PANEL_P4 §2.1's implication; SRCCD55 Proposition E's "no coarse decay" intention).

**New for OS0: the scale window of §3.4 (d).** Smeared bounds from the route cover test-function scales
δ ≥ δ_a ≍ (log(ℓ_ref/a))^{−1/α} only. OS0 in ^0𝒮 form needs every scale down to ca.

---

## §4. T3 — what the analyticity route does NOT cover (a first-class list)

**(N-1) Large coarse fields (UNIV55 (N3); SRCCD55 (M2)).**
- SA-K and SA-RW live on 𝒞_glob / small fields.
- The complex envelope 𝒰_ℂ(U_K) is not even defined at large coarse fields without (N3) with complex tilts, and SA-MOM needs
  it there.
- The route adds nothing here.

**(N-2) SRC-M (the eight O(g_bare²) matching constants).** The route bounds cumulants; it does not extract marginal constants.
That still needs a localisation operator on the source-linearised RG (SRCCD55 §5.4 item 3). Moreover, **analyticity in the
coupling cannot by itself turn tree-level vanishing into O(g²)**. PROVEN-HERE, by example:
- f(w) := w^{1/2} (w = g²) is holomorphic and bounded on every sector {0 < |w| < ρ, |arg w| < θ < π} and tends to 0 at w = 0,
  but it is not O(w).
- Only a full disc around w = 0 would give O(w), by the Schwarz lemma. Uniform-in-a RG control is available at best on a
  sector near the positive axis (Re u > 0, |Im u| ≲ ρ Re u).
- So the O(g_bare²) size needs a genuine first-order computation with a uniform remainder, as SRCCD55 §6 (M4) says ("ARGUED,
  not proved"). I agree.

**(N-3) The per-step large-field analysis conditioned on U_K (RLF^η).**
- Not addressed.
- The route also makes one constraint unavoidable: chessboard/RP is unavailable both in the conditional measure and at complex
  or non-reflection-symmetric couplings. So the per-step large-field bounds inside the complex polydisc must be action-based
  (Balaban type).
- This is the same requirement as PANEL_P4's H3 on the sphere.
- RP/chessboard remains usable only for the real coarse law ν_K (SRC-I) at η = 0. That is all SA-MOM uses it for.

**(N-4) N5 at levels ≥ 1 (general small backgrounds) and N6 (per-step polymer bound).** OPEN at ε̂ = 0 already. The route
needs their complex-coefficient versions; SA-RW supplies the linear part at the trivial background and at level 0 only.

**(N-5) Off 𝒞_glob** (nontrivial holonomy; general curvature-small U_K). BFT-0 itself is OPEN there (GV55 §3.3 item 2).

**(N-6) The open inputs this file names.** TOWER-VAR^η (§2.1), (Flow-an) and the position-dependent flow (§2.6), (H3^{ε̂})_m
(§2.5, ARGUED), (LOC-e) (§3.6), the image scaling (P1) and per-step decay (P2) (§3.4 (c)), and the rooted summability in SA-S
(A) (§3.3).

**(N-7) Pointwise weights for κ-1 and κ-2, and the OS0 scale window [ca, δ_a)** (§3.4).

**(N-8) Non-vacuity** (PANEL_P1's H_int). SRC gives upper bounds only.

**(N-9) The sphere's S4(a).** Its real slowly varying coupling (f(g_0(x)) = aΛ_physΩ(x)/C_W, PANEL_P4 §5.2) has
δu = O(β_0·log Ω-ratios), bounded. That is inside SA-K's class at tree level, but only on hypercubic 𝒞_glob; the seam and the
curvature of the cells are outside.

**The scale of the coupling perturbation (the brief's "|δg| ≤ ρg² (or the right scale)").**
- The natural variable is u = 1/g², since the action is linear in it.
- The uniform polydisc is |δu| ≤ r_src with r_src ≲ ρ/(2g_ref²), fixed as a → 0 (Lemma SA-F). Equivalently, δg_0 = O(g_0³r_src)
  at the bare level, and the relative perturbation stays ≲ ρ/2 at every level.
- The brief's |δg| ≤ ρg², read at the bare level, means |δu| ≤ 2ρ/g_0 → ∞. By one-loop invariance δu persists, so at the
  reference level the relative perturbation would be ~2ρg_ref²/g_0 → ∞. **That scale is too large for uniformity; the right
  scale is δu = O(1).**

---

## §5. Verdicts — the pre-stated refutation tests, the brief's premise, and inherited claims

### 5.1 The five pre-stated tests (PRE-STATED block, R1-R5)
| Test | Realised? | Where | Short reason |
|---|---|---|---|
| R1 (generation: are the 47 coupling derivatives?) | **NOT realised** | §3.5, Lemma SA-TI | κ(O, X_1..X_m) = ∂_z^m⟨O⟩_z: the 46 linear insertions need only e-tilts, i.e. one scalar coupling field. Their POINTWISE weights are outside the route (image route (P1)) |
| R2 (non-analytic dependence) | **NOT realised** at every place checked (§2.7 rows 1-20) | §2.1-§2.7 | thresholds coupling-free; background by contraction, holomorphic; positivity margins relative O(ρ); RP/chessboard and probabilistic averaging are used only on the real section or for ν_K — exactly what SA-S/SA-TC keep them for |
| R3 (quantitative) | **NOT realised for smeared sources; REALISED for pointwise weights** | §3.3, §3.4 (b), Lemma SA-CF | radius r_src ~ ρ/(2g_ref²), uniform in a and R. Pointwise: any polydisc Cauchy bound on the full Φ is ≥ ½√(Var·Var); for point insertions it misses δ^{−8} by a factor ≳ g_0⁴(δ/a)^8 |
| R4 (locality is a genuine extra input) | **REALISED** | §3.7 | z_1z_2 has no decay; BFT34_55 Proposition CX. Decay needs (D1) a decoupling representation with decaying activities or (D2) real CD (SA-S). BFT-3 covers tree-level parts only |
| R5 (slowly varying vs per-site Cauchy radii) | **REALISED for pointwise sources; RESOLVED for smeared sources** | §2.3, §3.4 (a), (d) | per-site sources break BFT-1's Hölder clause (flux identity, E1); smeared sources carry independent z_i on fixed C^α test functions and satisfy the condition for a ≤ a_0. New consequence: the OS0 scale window [ca, δ_a) |

### 5.2 The brief's premise, verdict
**Premise.** "Cauchy estimates turn uniform bounds into separated cumulant bounds (SRC-κ) automatically, with exponential decay
inherited from BFT-3-type locality."
**Verdict: REFUTED as literally stated; the corrected statement is PROVEN as an implication.**
- "Automatically" fails: analyticity plus uniform bounds give no decay (z_1z_2). For the full generating function they give no
  a-uniform bound either (Lemma SA-CF + Lemma V).
- "Inherited from BFT-3": BFT-3 is deterministic background locality, so only the tree-level parts are inherited (§3.7).
- **Corrected statement (Proposition SA-S).** Cauchy (with polarisation and two constants) turns [uniform bounds on the complex
  polydisc for Φ − CT, with rooted summability] + [decay at SECOND order for REAL couplings] into separated cumulant bounds at
  ALL orders, for smeared e-observables. The constants are geometric in n, and the rate is any fraction < 1 of the real one.

### 5.3 Inherited claims touched (verdict; file + locating string; reason)
| # | Inherited claim | Verdict | Reason |
|---|---|---|---|
| I1 | SRCCD55 §5.0, "If Φ_k is analytic on a fixed polydisc uniformly in k, all orders follow from Cauchy estimates."; and §0 "(ii) … All orders follow by Cauchy from analyticity on a polydisc." | **CONFIRMED as a statement about derivative bounds; NOT-VERIFIED as a route to SRC-κ** | For Φ_k itself an a-uniform bound is inconsistent with Lemma V, given the total-variance identity and SRC-E′(i) (Lemma SA-CF; an exact implication). So the hypothesis must be read for Φ_k − CT, as SRC-poly does. Decay still needs (D1) or (D2) |
| I2 | SRCCD55 §0 "(i) … BFT, N5, N6, RLF and (F_R) must therefore hold uniformly over a sup-norm ball of coefficient fields" and §5.4 item 1 "uniformly over a sup-norm ball of coupling fields with ‖η‖_∞ ≤ r_0 ≪ 1/g_ref²" | **NOT-VERIFIED as stated; corrected** | A sup-norm ball is too large for BFT-1's Hölder clause (Lemma SA-J: exact flux identity; size comparison ARGUED). The right class is ‖ε̂‖_cf: sup norm, plus the Hölder seminorm of the Wilson coefficient only. For BFT-0/1/2 on 𝒞_glob that class is PROVEN to suffice (SA-K) |
| I3 | SRCCD55 §6 (M1) "BFT^η … ARGUED that it rides on BFT's own contraction ("one contraction for 𝔉_k in 𝔐")" | **CONFIRMED (now PROVEN as an implication) in the ‖·‖_cf class, on 𝒞_glob** | Proposition SA-K. The NSL/identification clause and off-𝒞_glob are not covered |
| I4 | SRCCD55 §5.3 "(RW1)-(RW2) are open conditions, so they survive for r_0 ≪ 1/g_ref². This is an ARGUED perturbation remark" | **CONFIRMED** (abstract Δ; level 0) | Corollary SA-RW via PROOF's own Lemma CT♯; levels ≥ 1 ARGUED |
| I5 | SRCCD55 §5.4 item 1 "By asymptotic freedom it persists as an O(1) shift of 1/g_k²(x) at every level … so it does not become small" | **CONFIRMED as an implication of (Flow-an), for constant shifts** | Lemma SA-F gives |δu_K|/|δu_0| ∈ [e^{−c}, e^c] with c = (2C_b/ρ)Σg_j⁴(1 + o(1)) < ∞; the lower bound uses the same estimate with the opposite triangle inequality. Position dependence OPEN |
| I6 | SRCCD55 E12 (iii) "The pointwise δ^{−4}-per-point weights of (κ-1) need a scale-adapted source norm: level-r activities bounded in terms of each source's volume fraction of the cube." | **NOT-VERIFIED (agree it is an extra input); clarified** | Lemma SA-CF and §3.4 (b): a point source is a relative-O(1) local coupling change at |z| ~ a⁴u_0. The volume-fraction hypothesis must therefore be a SIZE statement on that small polydisc, equivalent in content to canonical image scaling (P1), not an analyticity statement on a large polydisc |
| I7 | SRCCD55 §8 (A3) "BFT-3 is deterministic background locality. The decay of a conditional covariance is CD. Its inputs are N5/N6 + SRC (Propositions A, B), not BFT-3." | **CONFIRMED** | §3.7 |
| I8 | BFT34_55 §1.5 table, (H2)_m gauge-variant half "GV-E_m … Codex check pending" (also l.471-472) | **Stale citation (drift), not a mathematical verdict** | CODEX_REVIEW_GV item 6 CONFIRMED Proposition GV-E_m. So BFT3-glob's (H2)_m now rests on Codex-confirmed pieces plus (H3)_m [ARGUED] |
| I9 | BFT34_55 Proposition CX ("analyticity + BFT-3 (n ≤ 4) do NOT imply BFT-4") | **spot-checked, CONFIRMED in its load-bearing step** | Lemma NC's proof: Cauchy in distinct variables without factorial, and a lower bound on the connected polymer size by an Euler tour. I did not re-check the grid-counting arithmetic line by line |
| I10 | The brief's premise (§5.2) | **REFUTED literally; corrected (SA-S)** | §5.2 |

---

## §6. Summary table — every claim made in this file

| # | Claim | Where | Label |
|---|---|---|---|
| 1 | The e-source enters ONLY as the bare Wilson coefficient, u_0 → u_0 − h_η(p) (kernels fixed); relative size −g_0²h_η; at steps i ≥ 1 it appears as a mismatch between the effective coupling field and the fixed kernel coupling | §2.1 | PROVEN-HERE (elementary); TOWER-VAR^η OPEN |
| 2 | Lemma SA-K1: ε̂-weighted rows bounded by K_ε‖ε̂‖_cf(η_b + s), Lipschitz K_ε‖ε̂‖_cf | §2.2 | PROVEN as an implication (per-term reading of Codex KOFF §4.3 flagged) |
| 3 | Proposition SA-K: BFT-0 (slice), BFT-1, BFT-2 on 𝒞_glob survive complex coefficient fields with ‖ε̂‖_cf ≤ ε̂_*, uniformly in k, T; joint holomorphy; x*(0, ε̂) = 0; Cauchy bounds in ε̂ | §2.2 | PROVEN as an implication (of BFT-E's inputs) |
| 4 | Lemma SA-J: flux identity (d = 2 exact; d = 4 slice-averaged, erratum E1); hence BFT-1's Hölder clause fails for lattice-rough coefficients; the slowly-varying condition is needed at tree level, on ε̂_0 only | §2.3 + E1 | identity PROVEN-HERE; consequence ARGUED |
| 5 | Corollary SA-RW: Theorem RW for Õ_i + Δ, |Δ| ≤ ‖ε̂‖Ĥ, via Lemma CT♯; holomorphic in ε̂; no Hölder needed | §2.4 | PROVEN as an implication (abstract Δ; level 0); levels ≥ 1 identification ARGUED |
| 6 | Lemma SA-WD: coupling-locality of the background, ∝ (η_b + s)e^{−m·dist} | §2.5 | PROVEN as an implication ((H3^{ε̂})_m ARGUED) |
| 7 | Lemma SA-F: |δu_j| ≤ |δu_0|exp((2C_b/ρ)Σg⁴), Σ_jg_j⁴ ≤ (u_K − R)^{−2} + (β_−log L)^{−1}(u_K − R)^{−1} | §2.6 | PROVEN as an implication of (Flow-an) + (F_R); position dependence OPEN |
| 8 | T1 table: 20 places where the coupling enters, verdict per place | §2.7 | as listed (rows 3-9, 11-13 CONFIRMED via SA-K; row 16 partly; rows 15, 17 NOT-VERIFIED; 18 ARGUED; 19 not needed; 20 implication/OPEN) |
| 9 | Lemma SA-CF: Cauchy bound for a covariance ≥ ½√(Var·Var) on any bounded polydisc; with Lemma V, no a-uniform polydisc for the full generating function; CT is necessary | §3.1 | PROVEN-HERE |
| 10 | Lemma SA-PC: pair Cauchy, no n! for distinct indices | §3.2 | PROVEN-HERE |
| 11 | Lemma SA-TC: |∂_1⋯∂_nΦ(0)| ≤ (rr_z)^{−(n−2)}𝒰_ℂ^{1−ω_hm(r)}𝒰_ℝ^{ω_hm(r)}, ω_hm(r) = 1 − (4/π)arctan r | §3.2 | PROVEN-HERE; constants certified by `sa55_hm` (VERDICT PASS, three controls fired) |
| 12 | Proposition SA-S: smeared SRC-κ (e, all orders, decay ω_hmμ_R in d_max) from (A) complex uniform bounds + (B) real CD | §3.3 | PROVEN as an implication; (A) and (B) OPEN |
| 13 | Pointwise weights are not delivered: (a) Hölder obstruction; (b) a point source is a relative-O(1) local change, shortfall ≳ g_0⁴(δ/a)^8; (c) the Markov/image route (P1)+(P2) would deliver them; (d) OS0 scale window [ca, δ_a), δ_a ≍ (log ℓ_ref/a)^{−1/α} | §3.4 | (a) from #4; (b) ARGUED (single-site variance); (c) ARGUED reduction; (d) ARGUED |
| 14 | Lemma SA-TI: κ(O, X_1..X_m) = ∂_z^m⟨O⟩_z; the 46 linear insertions need no sources | §3.5 | PROVEN-HERE |
| 15 | Lemma SA-E1: tree-level image of e is canonical, ≤ 6|supp h|ℓ_ref^{−4}(2η_b + 9η_b²)² (E2) | §3.6 + E2 | PROVEN as an implication of BFT-E |
| 16 | (LOC-e): the needed fluctuation input for κ-3; SRC-poly's sup bounds alone give an a^{−4}-divergent singleton bound; mechanism O(g_r⁴) from (Flow-an) | §3.6 | statement OPEN; mechanism ARGUED |
| 17 | Analyticity + uniform bounds give no decay; decay enters only via (D1) decaying decoupling representations or (D2) real CD; BFT-3 supplies only tree-level parts | §3.7 | PROVEN (example) + reading (agrees with SRCCD55 (A3)) |
| 18 | Proposition SA-MOM: b-th moments of conditional cumulants need only the FIRST moment of the real decaying envelope and moments of the complex non-decaying one | §3.8 | inequality PROVEN-HERE; the reduction of Codex's LF-moment gap is conditional (local form of 𝒰_ℂ OPEN) |
| 19 | Tree-level vanishing + sector analyticity do not give O(g²) (w^{1/2}) | §4 (N-2) | PROVEN-HERE (trivial example) |
| 20 | The right coupling scale is δu = O(1), r_src ≲ ρ/(2g_ref²); the brief's |δg| ≤ ρg² at the bare level is too large | §4 | implication of SA-F (both bounds) |
| 21 | Corpus: the analyticity route is the one the Balaban school names for correlation functions; never carried out there; all corpus analyticity is in fields or decoupling parameters | §0 | reading (cited by arXiv id) |

**Counts of my own claims.**
- PROVEN-HERE: 1, 9, 10, 11, 14, 18 (inequality), 19, and the identity in 4 — 8 rows.
- PROVEN as an implication: 2, 3, 5, 6, 7, 12, 15, 20 — 8 rows.
- ARGUED: 4 (consequence), 13 (b)-(d), 16 (mechanism) — 3 rows.
- OPEN statements named: TOWER-VAR^η, (Flow-an), (H3^{ε̂})_m [ARGUED], (LOC-e), (P1), (P2), and SA-S's (A) and (B).
- Mixed rows: 8, 17, 21.
- Rows 4, 13, 16 and 18 are counted under two labels on purpose.

**Inherited verdicts (§5.3).**
- CONFIRMED 6: I1 (derivative-bound part), I3, I4, I5, I7, I9 (spot-check).
- NOT-VERIFIED 3: I1 (as a route to SRC-κ), I2, I6.
- REFUTED 1: I10, the brief's literal premise.
- Drift notes 1: I8.

**Codex verdicts used:** SRCCD items 1, 2, 3, 4, 5/§5, 7/§7; KOFF item 5 + §4.3, §5.3; GV items 4 and 6; FLOW55 item 4.
**I agree with every one.**

---

## §7. For the lead (short)

**What the analyticity route can and cannot do (the first-class result).**
- **CAN (proved as implications):**
  - The tree-level layer-1 RG (BFT-0 slice form, BFT-1, BFT-2 on 𝒞_glob; Theorem K^{(σ)}) is stable under complex,
    position-dependent coupling fields, uniformly in k and T, with joint holomorphy (Proposition SA-K).
  - So is the per-step Gaussian covariance at the trivial background and at level 0 (Corollary SA-RW).
  - A constant marginal shift propagates boundedly under an analytic flow (Lemma SA-F; Σg⁴ < ∞).
  - Cauchy, with polarisation and the two-constants theorem, converts [uniform complex bounds without decay] + [second-order
    decay for REAL couplings] into smeared SRC-κ at all orders (Proposition SA-S). That is the precise content of "Cauchy turns
    uniform bounds into separated cumulant bounds".
  - The 46 linear insertions need no sources (Lemma SA-TI).
  - The tree-level part of κ-3 for e is canonical (Lemma SA-E1).
- **CANNOT:**
  - give decay by itself (R4; BFT-3 gives only tree-level locality);
  - give pointwise weights (R3/R5: Lemma SA-CF, Lemma SA-J);
  - reach OS0's full ^0𝒮 test space: there is a scale window [ca, (log ℓ_ref/a)^{−1/α}) (§3.4 (d));
  - give SRC-M's O(g²) sizes (§4 (N-2));
  - touch large coarse fields or per-step conditional RLF.

**Changes the critical path should record (HANDOFF / the SRC node).**
1. Replace "BFT, N5, N6, RLF, (F_R) uniformly over a SUP-NORM ball of coupling fields" (SRCCD55 §0 (i), §5.4) by **the
   ‖·‖_cf ball**: sup norm plus the Hölder seminorm of the WILSON coefficient only. Lemma SA-J shows the sup-norm class is too
   large for BFT-1's Hölder clause.
2. BFT^η at tree level on 𝒞_glob is now an implication of BFT-E's inputs (Proposition SA-K; Codex check needed).
3. SRC splits into three separately attackable nodes:
   - **(A)** complex-coupling stability WITHOUT decay: SA-K and SA-RW done as implications; N5/N6/RLF complex, (Flow-an),
     TOWER-VAR^η and rooted summability OPEN;
   - **(B)** CD for REAL position-dependent couplings, where Proposition B and positivity are available: OPEN;
   - **(P1)/(LOC-e)** canonical first-order images at every level: OPEN. This is what pointwise weights, κ-2's point
     insertions, κ-3 and the OS0 window need.
4. Codex SRCCD §7's three OS0 gaps:
   - singleton → reduced to (LOC-e) plus the flow's O(g⁴) derivative;
   - all-order LF moments → reduced by Proposition SA-MOM to moments of a NON-decaying complex envelope; closed if that envelope
     has local LF dependence (OPEN);
   - large-distance weight → unchanged; Codex's w_e(min(δ, ℓ_ref)) repair is right.
5. The brief's premise ("automatically … decay inherited from BFT-3-type locality") is REFUTED as literally stated (§5.2).
6. Tally: no change. Everything here is lane-level.

**For the Codex reviewer, in order of load:**
- Proposition SA-K's bookkeeping, especially SA-K1's reliance on per-term absolute bounds behind Codex KOFF §4.3 (1)-(3).
- Lemma SA-TC's proof and `checks/sa55_hm`.
- Lemma SA-CF with Lemma V.
- Lemma SA-J's flux identities, including erratum E1.
- Lemma SA-F's arithmetic.
- §3.4 (d)'s window arithmetic.

---

## §8. Errata from a full re-read of §2-§7 (append-only; each item overrides the text it names)

**E3 (§3.4 (b), §5.1 row R3, §6 row 13 — which floor applies).**
- The shortfall factor "≳ g_0⁴(δ/a)^8" is the Cauchy floor (Lemma SA-CF) for the FULL generating function.
- Once CT is removed, that floor no longer applies. The obstruction is then the radius: a point source is a relative-O(1)
  change of the local coupling already at |z| ~ a⁴u_0, so Cauchy alone gives a^{−4}g_0² per point.
- It gives δ^{−4} per point only if the connected part's sup on that small polydisc is itself ≲ Π_i(a/δ_i)⁴. That is a SIZE
  input with the content of (P1), and analyticity cannot supply it.
- The verdict "R3 realised for pointwise weights" stands, for this reason.

**E4 (§3.6, "(κ-3) does NOT follow from SRC-poly as stated") — now PROVEN-HERE as a non-implication, by an abstract model.**
- Let the fine field be deterministic given U_K: on a region of size O(ℓ_ref), e_a(x) := (ψ(U_K)/r_src)Σ_{r≤K}A_rℓ_r^{−4},
  with ψ a bounded non-constant local function of U_K near the region and A_r ≡ A.
- Then log E_K[exp⟨η, e⟩] = ⟨η, e⟩ = Σ_rΣ_{□ level-r cube}𝔞_r(□; η, U_K), with
  𝔞_r(□; η, U_K) := ψ(U_K)A_rℓ_r^{−4}r_src^{−1}Σ_{x∈□}a⁴η(x).
- Each activity is analytic, depends only on η|_□ and on U_K near □, vanishes when η|_□ = 0, and is bounded by A·M⁴‖ψ‖_∞ on
  ‖η‖_∞ ≤ r_src. So SRC-poly holds with CT = 0 and sup_rA_r < ∞, and κ-1 holds trivially (all conditional cumulants of order
  ≥ 2 vanish).
- Yet E_K[e(h)] − ω(e(h)) = (ψ − ν_Kψ)r_src^{−1}AΣ_{r≤K}ℓ_r^{−4}∫h ~ a^{−4}.
- This is the same mechanism as Codex SRCCD §7's deterministic-field example, for the singleton. It is a statement about the
  implication, not about Wilson YM.

**E5 (§4 (N-2), "Only a full disc …").**
- Read: "a full disc around w = 0 suffices, by the Schwarz lemma; a sector does not (w^{1/2}). On a sector one needs an extra
  input, such as a first-order expansion with a uniform remainder."
- "Only" overstated the converse.

**E6 (§2.4, ε̂_RW — the gap must stay bounded below).**
- As printed, ε̂_RW gives only ‖ε̂‖N_0(Ĥ_i) ≤ γ_i, so γ′ = γ_i − ‖ε̂‖N_0(Ĥ_i) could be arbitrarily small.
- Correct definition: **ε̂_RW := min{(γ_i/2 − 𝔇(m))/(D_m(Ĥ_i) + N_0(Ĥ_i)/2), γ_i/(2N_0(Ĥ_i))}**, so that γ′ ≥ γ_i/2.
- Theorem RW also needs ε_R ≤ ½ with the perturbed constants. Re-choose R ≥ R^{ε̂}_triv :=
  ⌈(2/(aL))log(16S′_mcoth⁴(a/4)/γ′)⌉, with S′_m = S_m + ‖ε̂‖_∞N_m(Ĥ_i) and a = m − m_1 as in Theorem RW.
- With the uniform bounds on Ĥ_i this is uniform in i, k, T. The conclusion of SA-RW is unchanged.

**E7 (§3.4 (d), the reason in the third bullet).**
- "because δ_a ≫ a^{1/2}" should read "because δ_a decays only like a power of log(ℓ_ref/a), so δ_a^{M+4}a^{−4n} → ∞ for every
  fixed M".

**E8 (§5.3 row I1 — the verdict is sharpened: the HYPOTHESIS, read for Φ_k itself, is REFUTED, exactly).**
- Suppose Φ_K(zh; U_K), or Φ_K minus a U_K-INDEPENDENT linear term z·c, were holomorphic with an a-uniform bound A on an
  a-uniform disc |z| ≤ ρ, for all U_K.
- Cauchy bounds the second derivative: Var(e(h) | U_K) ≤ 2A/ρ².
- Cauchy bounds the first derivative: |E_Ke(h) − c| ≤ A/ρ, so Var_ν(E_Ke(h)) ≤ A²/ρ².
- The total-variance identity then gives Var_ω(e(h)) ≤ 2A/ρ² + A²/ρ², uniformly in a. This contradicts Lemma V (Codex SRCCD
  item 3: ≥ (3/2000000)g_0⁴a^{−4}(‖h‖₂² − O(a)), which diverges under (F_R)). No SRC-E′(i) is needed, unlike I1's table text.
- So: the implication "analytic on a fixed polydisc uniformly in k ⇒ all orders by Cauchy" is CONFIRMED (Cauchy). Its
  hypothesis, read for Φ_k itself (as SRCCD55 §5.0 defines Φ_k), is **REFUTED**. The correct statement puts the uniform bound
  on Φ_k − CT (SRC-poly), or, as in SA-S (A), only on the cross-support second derivatives, which are CT-free.
- I1's row therefore counts as one CONFIRMED (the implication) and one REFUTED (the hypothesis as a usable input). This
  replaces the NOT-VERIFIED half.

**E9 (§3.3 Proposition SA-S, two clarifications).**
- (A) bounds only the cross-support second derivatives ∂_i∂_jΦ, i ≠ j. These are CT-free automatically, so (A) does not
  conflict with Lemma SA-CF or E8, even though Φ itself is unbounded (extensive, a^{−4}).
- (B) is CD for real-tilted chains whose kernels are NOT re-tuned to the tilted couplings (the mismatch of §2.1 and §2.6). Only
  the real points tv_ε of the one-variable slices are used, a sub-cube of the real cube.

**Corrected counts after E3-E9.**
- My own claims: PROVEN-HERE becomes 9 rows (E4 adds the non-implication model). The other counts are unchanged.
- Inherited verdicts: CONFIRMED 6 (I1-implication, I3, I4, I5, I7, I9); NOT-VERIFIED 2 (I2, I6); **REFUTED 2 (I1-hypothesis
  read for Φ_k itself, by E8; I10, the brief's literal premise)**; drift 1 (I8).

**Everything else in §2-§7 stands as written.** In particular: Proposition SA-K and its threshold; Lemma SA-J's d = 2 identity
and, after E1, the slice-averaged d = 4 identity; Lemmas SA-CF, SA-PC, SA-TC, SA-TI; Proposition SA-S; Lemma SA-E1 after E2;
Lemma SA-F; Proposition SA-MOM.

Completed: see the next line (UTC, from `date -u` at the end of writing).
Completed: 2026-10-29T03:35:58Z
