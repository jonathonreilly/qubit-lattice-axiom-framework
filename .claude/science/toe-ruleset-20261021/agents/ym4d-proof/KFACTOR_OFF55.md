Reviewer model: claude-opus-5-5

# KFACTOR_OFF55 — the off-critical half of the level-count factor (BCH₂ rows R^B_l inside the composite contraction for 𝔉_k)

Author: Opus 5.5 worker (model ID above, verbatim from the system prompt). Worker rules of
REVIEW_BRIEF_55.md apply (no git; write only this file and checks/ko55_*; append-only; criteria
before scripts; exact arithmetic for verdicts; never fabricate a number, a line reference or a PASS).

## PRE-STATED (written 2026-10-28 23:40 UTC, before any derivation; statements only)

Inputs to be read before deriving: KFACTOR_O55.md (whole), CODEX_REVIEW_TR.md (if it exists when read),
REVIEW55_TUNIF.md (the θ_w^r > 2 correction and the (1c)-relative-to-Z^lift correction), NORMS.md §N6,
BFT_A.md COMP (CL-0)-(CL-4), REVIEW_S22.md l.385-435 (anti-circularity clause), PROOF.md header
[S26-BANKED]. All citations will be located by string; drifted line numbers will be reported.

Targets.
- (T1) State the lane's composite contraction for 𝔉_k (one contraction, per-level covariances never used
  as Newton inverses) with the residual measured in the transport weight θ_w^r (3 for data; 2+θ with
  nonlinear sources), BFT-1 (1c) stated relative to Z^lift.
- (T2) Prove: in that weight the BCH₂ rows R^B_l are summable along the iteration uniformly in k and T
  (no factor ∝ (k−1) appears), and the map still contracts, A = L^{4−θ_w^r−2θ_A} < 1, with the weights the
  lane actually delivers (θ_w^r, θ_A read from file, not assumed).
- (T3) Identify "the lane's existing off-critical remainder" (the input KFACTOR_O55 names as open) by
  file and string, and either bound it with present inputs or state exactly what is missing.
- (T4) Check consistency with PROOF.md [S26-BANKED]: (T-UNIF) repaired; (CO-fun) sup half on the
  composite class; (CC-0) at critical points REFUTED — (CC-0) is assumed nowhere here.

What would count as a refutation of the target claim ("off-critical, the factor is an artifact of the norm"):
- (R1) In the transport weight the row bound summed over l = 1..k−1 still grows with k (any lower bound
  ≳ (k−1)·c with c independent of k, from the same inputs), i.e. the rows are not summable.
- (R2) A = L^{4−θ_w^r−2θ_A} ≥ 1 for the delivered (θ_w^r, θ_A); or the delivered θ_w^r is ≤ 2 where the
  composite contraction needs > 2 (REVIEW55_TUNIF).
- (R3) The off-critical remainder can be bounded only by assuming (CC-0), the critical-point property
  (Lemma TR's hypothesis) inside the contraction (circular), or a per-level Newton inverse (REVIEW_S22
  anti-circularity clause).
Any of (R1)-(R3) is reported as such; an unclosed step is reported as NOT-VERIFIED with what it needs.

---

## §0. Read record (appended 2026-10-29T00:30Z UTC; everything located by string, line numbers as of this session)

- **KFACTOR_O55.md** — whole file (576 lines), including §4-A, §4-B, §9, §10 and both errata.
- **CODEX_REVIEW_TR.md** — whole file (284 lines; "Review completed: 2026-10-28 23:51:15 UTC"; it ends with a complete
  "Exactly what may be banked" list, so it is not unfinished). Read after my PRE-STATED and before any derivation here.
- **REVIEW55_TUNIF.md** W1-W10 (l.318-430). **NORMS.md** §N6-§N7 (l.500-680; the soft condition is the string "Soft
  condition at θ_A = 1"). **THETAW.md** l.596-616 (BFT-1 (1a)-(1c)). **REVIEW_S22.md** l.370-432 (Part 5: the BFT
  statement; the anti-circularity clause is the string "Anti-circularity:" at l.422-423 — inside the brief's l.385-435).
- **PROOF.md**: header l.1-40 (incl. "[S26-BANKED]" l.5-13); COMP l.6667-6693 (string "Proposition COMP (the composite
  contraction)"); Lemma NA-alg l.3207-3222.
- **BFT_A.md**: §1 (l.18-47); §2-§3.11 (l.48-275; §3.9 "Theorem BA" l.205-231, the contraction Φ(x) = 𝓛^{-1}(NB + 𝔑(x; B)));
  [RBA1-fix] F6 and the corrected pair (l.360-436); §7.1-7.3 (l.444-574: Setting LIN, BL-1..BL-7); [RBA2-fix] B2-B4
  (l.814-834); §12.0-12.2 (l.879-942: BCH₂ row, CR-1, SPD, TS, W, LR-pot, FP); §23.8-23.9 (Lemma RH, CO-upR); §26.0-26.2
  (l.2199-2265: Ξ, Λ_0, composite co-closedness, Lemma FG, NC); §31.0-31.1 (l.2752-2813: K_x, K'_x, 𝔑^0, Lemma CD).
- **BFT_B.md**: §18.0-18.1 (l.2453-2528); §27 (l.3571-3640); §29 (l.3655-3750: RT-cc, FT, RHT-cc, RHT-V); §31 (l.3775-3822:
  Proposition NCR, (CO-fun), the off-critical remainder); §36 (l.4132-4212: GT-split, GT-loc, GT-ell, NCE).
- **CODEX_REVIEW_C2.md** whole; **REVIEW_BFT_B_S9_S10.md** l.1-120; **REVIEW_BFT_A_S8.md** l.540-600 ("The biggest live
  wall in lane A"); **REVIEW_BFT_A_S3.md** l.1-60; **REVIEW_BFT_A_S5.md** l.20-45; **REVIEW_BFT_A_S6.md** l.1-60;
  **HANDOFF.md** l.80-170.
- Drift found: none against the brief's REVIEW_S22 range. KFACTOR_O55's own errata are taken as applied.
- Sign convention (CODEX_REVIEW_TR §1, which I accept): with BFT_A §31.0's 𝔑^0 := Hx − NB − ∇(𝔉_k∘exp), the BA-6 / §12.0
  rows (defined as contributions to the positive gradient) enter 𝔑^0 with a common minus sign. Every estimate below is a
  norm estimate and is unaffected; I write rows without that sign.

---

## §1. (T1) The contraction, stated

### 1.1 Setting and notation (all from the sources; nothing new)
d = 4, L ≥ 3 odd, κ_l ∈ [κ_-, κ_+], κ̂ := κ_+/κ_-, depth k ≥ 1, coarse torus side T ≥ 3, n := L^k. Class 𝒞_glob(ε) of BFT_A
§1.2 (data V_k = e^{B_k}, s := ||B_k||_D ≤ ε in one global gauge), trivial-chain centring (C-glob), m = 0 (no exponential
weights), trivial background. Chains x = (x_0, …, x_{k−1}), x_k := B_k; r_l(x) := Q_lx_l − x_{l+1}; coarse units
x^c_j = L^{k−j}x_j, r^c_j = L^{k−1−j}r_j, f_j := (dx_j)^c, plain currents π_l(j) := L^{3(k−l)}·sup_own|j| (BFT_A §1.3, §7.2).
F(x) := 𝔉_k∘exp(x; B) (TOWER-VAR; BFT_A §1.1). H, N: Hessian and data map at x = 0; **𝔑^0(x; B) := Hx − NB − ∇F(x; B)**
(BFT_A §31.0). Composite gauges: Ξλ := (dλ, d ev^{(1)}λ, …, d ev^{(k−1)}λ) for level-0 functions λ; Λ_0 := functions
constant on the level-k roots, **Λ_* := functions vanishing on the level-k roots** (Λ_0/const ≅ Λ_*). Composite
divergence **D(S) := Ξ^TS = Σ_l ev^{(l)T}d*S_l**; **D^⊥(S)** := its restriction to the non-root sites. S is
**composite-co-closed (cc)** iff D^⊥(S) = 0 (the total ΣD(S) = 0 is automatic); (CC-0) := D(S) = 0 everywhere is
**never assumed below** (REFUTED at critical points, [S26-BANKED]). Gauge fixing (BFT_A §26.0): Γ linear with ΓΞ a
bijection of Λ_0/const onto Ran Γ and 𝓛_Γ := H + Γ^TΓ invertible. Below always **ΓΞλ = −λ for λ ∈ Λ_*** (true for Γ_E,
Lemma GE (a), and for the tent-axial Γ_tent(x) := Σ_Xχ_Xλ_X(x) of BFT_A §12.0, since λ_X(Ξλ)(z) = −(λ(z) − λ(c_X)) = −λ(z)
and Σ_Xχ_X = 1). Lemma CD (BFT_A §31.1; banked in its root-pinned form, CODEX_REVIEW_C2 item 4): for every x,
**D^⊥(𝔑^0(x; B)) = −(K'^T_x∇F(x; B))^⊥**, K'_x := K_x − K_0 the x-dependent part of the infinitesimal composite gauge
action in log coordinates.

### 1.2 The transport-weighted pair, as a one-parameter family
For **σ ∈ [0, 1]** (σ = 0 is 𝔐^∇ of BFT_A §1.4; σ = 1 is 𝔐^♯ of KFACTOR_O55 §5 (c)):
- **𝔐^{(σ)}:** ||x||_{(σ)} := max_{0≤j<k}[ ||x^c_j||_∞ + ||∇^cx^c_j||_∞ + [∇^cx^c_j]_α + L^{(1+σ)(k−1−j)}||r^c_j||_∞ ].
  The residual weight is **θ_w^r = 2 + σ in own units** (L^{(1+σ)m}·||r^c|| = L^{(2+σ)m}·sup_own|r|, m := k − 1 − j).
  Gauge-invariant part: ||x||_{inv,(σ)} := max_j[ ||f_j||_∞ + [f_j]_α + L^{(1+σ)(k−1−j)}||r^c_j||_∞ ].
- **Source functional** on explicit representations S ≅ (G_0 at level 0 only; residual-type s_l, 0 ≤ l < k; plain
  currents j_l, 0 ≤ l < k) — no positive-level divergence slot is ever needed, because TOWER-VAR has curvature only at
  level 0 (CODEX_REVIEW_C2 §5) and I keep every row whole:
  **N^{(σ)}(S) := ||G^c_0||_∞ + [G^c_0]_α + ||s||_{R(σ)} + J(j),  ||s||_{R(σ)} := max_l L^{(1+σ)(k−1−l)}||s^c_l||_∞,
  J(j) := Σ_{l=0}^{k−1} π_l(j_l).**
  (R(σ)) is BFT_A's (R) slot with source exponent θ_R = σ: ω^R_lL^{k−1−l}||s^c_l|| = L^{θ(m+1)}L^m||s^c_l||, so
  **||s||_R ≤ L^θ||s||_{R(σ)} whenever θ ≤ σ** (KFACTOR_O55 §5 (f) is the case σ = 1; CONFIRMED). The plain slot is
  the coarse SUM J, which is what (C2-COF) consumes (CODEX_REVIEW_C2 §4, "N := ||G_0^c||_∞+[G_0^c]_α+||G||_Y+||s||_R+J").
- Parameters: **0 < α < θ ≤ σ ≤ 1** (α < θ for LIN0/(C2-COF); θ ≤ σ for the inclusion above). σ = 1 allows every θ ∈ (α, 1).

### 1.3 The map: the lane's Feynman contraction and the cc-projected contraction
- **Feynman (the lane's):** Φ_Γ(x) := 𝓛_Γ^{-1}(NB + 𝔑^0(x; B)) (BFT_A §3.9, Lemma CD (ii)); fixed point ⟺ ∇F + Γ^TΓx = 0.
- **cc-projected (this file):** with the hierarchical routing P^T of Lemma HR (§3.3),
  **Φ̃_Γ(x) := 𝓛_Γ^{-1}( NB + 𝔑^0(x; B) − P^T D^⊥(𝔑^0(x; B)) ).**
  By Lemma CD, P^TD^⊥(𝔑^0(x)) = −P^T(K'^T_x∇F(x))^⊥, so, with **M_x := 1 − P^T(K'^T_x·)^⊥** (an explicit local-hierarchical
  operator, no inverse),
  **Φ̃_Γ(x) = x − 𝓛_Γ^{-1}( M_x∇F(x) + Γ^TΓx ),**
  i.e. COMP's Newton map with 𝔊_k = 𝓛_Γ^{-1} (composite) and the gradient preconditioned by M_x. Every source that
  𝓛_Γ^{-1} meets is cc (Proposition CCP (a)), so every iterate lies in the slice Ker Γ.
- **COMP correspondence** (PROOF l.6667-6693 "(CL-0)"-"(CL-4)", re-pointed to BFT-0/1/2 in 𝔐): (CL-0) = 𝓛_Γ^{-1} maps cc
  sources into Ker Γ with 𝓛_Γ^{-1}H = 1 there (Lemma FG (iii)); (CL-1) = the data map (BL-4); (CL-2) = the Lipschitz
  bound of x ↦ 𝔑^0(x) − P^TD^⊥(𝔑^0(x)) in N^{(σ)} (§2-§3) composed with the linear estimate for cc sources (§4);
  (CL-3) = BA-3 plus §1.4; (CL-4) = BA-9 in Balaban's convention (unchanged; its (CMP) only improves at σ > 0 because the
  depth-j residual weight is L^{−(2+σ)(k−j)} times the depth-k one).
- **Anti-circularity (REVIEW_S22 l.422-423, "one contraction for 𝔉_k in 𝔐 … may not use the per-level covariances C^{(j)}
  as Newton inverses"): SATISFIED.** The only inverse is the composite 𝓛_Γ^{-1}; P^T and K'^T_x are explicit
  finite-range maps; no per-level C^{(j)} appears.

### 1.4 BFT-1 in this pair (what the ball ||x||_{(σ)} ≤ η delivers; (1c) relative to the centre)
(1a) own plaquette logs of e^{x_j} ≤ L^{−2(k−j)}(2η + 9η²) (BA-3; θ_w^c = 2, the maximum, NORMS "There is NO slack in the
curvature exponent"). (1b) own soft fluctuations |ρ_j| ≤ |r_j| + |ρ_j − r_j| ≤ L^{−(2+σ)(k−1−j)}η + C_ρL^{−3(k−j)}η²
(second order: BA-6's C_6; third and higher: (LA-2) of §2), i.e. **θ_w^r = 2 + σ (= 3 at σ = 1)**. (1c) **own |x_j| ≤
L^{−(k−j)}η for the displacement x relative to the centre** — the trivial chain on 𝒞_glob, where the fixed point has
η ≤ C_0s with s the data size in the global gauge. This is the "linear response's potential bounded by the data's size"
reading that REVIEW55_TUNIF W6 prescribes; it is **not** a bound on the background's potentials by its curvature (false
on a torus with holonomy, W6 / Codex F13). Outside 𝒞_glob the centre must carry the holonomy (Z^lift itself is excluded
as a centre in every decaying norm by BA-2; the smooth lift Z^sm of BFT_A §3.10 is ARGUED) — unchanged and OPEN there.
θ_A ≤ 1 is a hard cap (REVIEW55_TUNIF W8), so (1c) is the best possible potential clause.

---

## §2. (T2, first half) The rows in the σ-ball: summable uniformly in k and T for every σ > 0

### 2.1 Lemma SG (exact factorisation of the soft gradient) — PROVEN-HERE as an identity, given NA-alg (a)-(b)
*Setting* (PROOF l.3207-3222, Lemma NA-alg; BFT_A §1.1). For a level-(l+1) coarse link c: M := M̄_c(x_l) (the S4' average
of the contour products), V := e^{x_{l+1}(c)} (V := e^{B_k(c)} if l = k−1), W_0 := W_0(M) the SU(N) maximiser of Re tr(W^{-1}M),
G := W_0^{-1}M = H + iθ·1 (NA-alg (a)), ρ := log(V^{-1}W_0) (NA-alg (b)), and σ_c := κ_lφ̂(M, V) with
φ̂ = Nφ = Re tr(W_0^{-1}M) − Re tr(V^{-1}M). Put **Θ := e^{ρ} − 1** and Z := V^{-1}δV ∈ su(N).
*Claim.* For every variation, **δσ_c = κ_l[ −Re tr(Θ W_0^{-1}δM) + Re tr(Z Θ G) ].**
*Proof.* Envelope: W_0 maximises Re tr(W^{-1}M) (NA-alg (a), "Stationarity"), so δ[Re tr(W_0(M)^{-1}M)] = Re tr(W_0^{-1}δM).
Next δ[−Re tr(V^{-1}M)] = −Re tr(V^{-1}δM) + Re tr(V^{-1}δV V^{-1}M) = −Re tr(V^{-1}δM) + Re tr(Z V^{-1}M). From the
definition of ρ, V^{-1} = e^{ρ}W_0^{-1}, so W_0^{-1} − V^{-1} = −ΘW_0^{-1} and V^{-1}M = e^{ρ}G; hence
Re tr(ZV^{-1}M) = Re tr(ZΘG) + Re tr(ZG), and Re tr(ZG) = Re tr(ZH) + θRe tr(iZ) = 0 (tr(ZH) ∈ iℝ for Z anti-Hermitian,
H Hermitian; tr Z = 0). ∎
*Consequences (exact).* (i) **The whole soft gradient at step l is linear in Θ_c**, |Θ| ≤ e^{|ρ|}|ρ|, with coefficients
analytic in the link variables (||W_0^{-1}|| = 1, ||G|| ≤ 2 on NA-alg's domain). (ii) At x = 0 (W_0 = G = 1, δM = (Q_lδx_l)(c)
to first order, Z = δx_{l+1}(c)) the coefficient map is the linear residual map: −Re tr(Θ·(R_lδx)(c)) = ⟨Ψ_c, (R_lδx)(c)⟩
with **Ψ_c := Π(−Θ_c^*)** (Π the projection onto su(N) for Re tr(A*B), as in NA-alg), and Ψ_c = ρ_c + O(|ρ_c|³) because
−Θ^* = ρ − ρ²/2 + ρ³/6 − … and Π annihilates the Hermitian even powers. Therefore, exactly,
  **∇_x Σ_cσ_c = κ_l R_l^TΨ_l + κ_l E_l(x),**
where E_l(x) (a plain current at levels l and l+1) is the gradient of
Σ_c[ −Re tr(Θ_c(W_0^{-1}δM_c − (Q_lδx_l)(c))) + Re tr((Z_c − δx_{l+1}(c))Θ_cG_c) + Re tr(δx_{l+1}(c)Θ_c(G_c − 1)) ].
*Local analytic inputs (named; finite-dimensional, k-independent by construction since every contour word has ≤ p_L links;
ARGUED-standard, constants not computed):*
- **(LA-1)** On NA-alg's domain (contour logs ≤ 1/20): |∂(W_0^{-1}M̄_c)/∂x_b − Q_{cb}| ≤ C_Ep_Ls_l·freq_c(b),
  |Z_c − δx_{l+1}(c)| ≤ C_Es_{l+1}|δx_{l+1}(c)|, ||G_c − 1|| ≤ C_Ey² (NA-alg (a) gives ||H − 1|| ≤ 18.4y²), where
  s_l := sup_own|x_l|, y ≤ p_Ls_l the contour-log size, freq_c(b) the frequency of b in the words of c, Σ_cfreq_c(b) ≤ c_L.
  Hence **own |E_l(x)(b)| ≤ C_Ec_Lp_Ls_l·max_{c∋b}|Θ_c|** (level l) and **|E_l(x)(c)| ≤ C_E(s_{l+1} + p_L²s_l²)|Θ_c|**
  (level l+1).
- **(LA-2)** |ρ_c − r_c(x)| ≤ C_6L^{−3(k−l)}η² + C_3(p_Ls_l + s_{l+1})³ in the 𝔐^∇-ball: the quadratic part is BA-6's
  ρ^{(2)} bound (PROVEN, via BA-4's S4' cancellation and the gradient component); the cubic Taylor remainder needs no
  cancellation, because **any cubic expression in own link variables of size ≤ L^{−(k−l)}η is ≤ C·L^{−3(k−l)}η³ — already
  the transported size**.
- **(LA-3)** Wilson: S_W = Σ_pw(F_p), F_p := log U_∂p = (dx_0)_p + q_p(x), w a class function with ∇w(F) = c_wF + O(|F|³);
  so ∇S_W = d*(∇w(F)) + (Dq_x)^T∇w(F) exactly, the nonlinear divergence-form row G_0 := ∇w(F) − c_wdx_0 = c_wq + O(|F|³)
  and the plain Wilson row R^W_0 := (Dq_x)^T∇w(F) obey the second-order bounds of 2.2 up to O(η³) with the same units.
*Why it matters (this answers CODEX_REVIEW_TR §3's "higher-order exact-source obligation" structurally).* Codex TR's
concern was that per-level O(η³) bounds would sum to O(kη³). By Lemma SG every soft plain current, at every order, is
E_l(x) = (coefficient of size ≲ s_l)·Θ_l and Θ_l ≈ ρ_l ≈ r_l + (transported-size error): so **every** soft plain row
inherits whatever level decay the residual has. The exact decomposition has no positive-level divergence slot (Codex's
first condition), residual-type part κ_l(Ψ_l − r_l) with |Ψ − r| ≤ |Ψ − ρ| + |ρ − r| (Codex's second), and plain parts
E_l (Codex's third) — only the constants (LA-1)-(LA-3) remain.

### 2.2 Proposition ROW^{(σ)} (sizes and Lipschitz constants in the σ-ball)
Let ||x||_{(σ)}, ||x'||_{(σ)} ≤ η ≤ η_0 := 1/(20p_L) (so all contour logs are ≤ 1/20; BFT_A §3.3), m := k − 1 − l. Own sizes in
the ball: s_l ≤ L^{−(m+1)}η, sup_own|r_l| = L^{−m}||r^c_l|| ≤ L^{−(2+σ)m}η.
**(a) Second order — PROVEN (re-derived here; KFACTOR_O55 ROW♯ is the case σ = 1).**
- BCH₂ row: by (★) π_l(R^B_l) ≤ c_Bκ_+L^{3(k−l)}s_l sup_own|r_l| (BA-6: "of own size ≤ κ·2p_Ls_l·|r_l|", c_B = 2p_L;
  conversion CONFIRMED in CODEX_REVIEW_TR §4): **π_l(R^B_l(x)) ≤ c_Bκ_+L^{3(m+1)}L^{−(m+1)}L^{−(2+σ)m}η² = A_BL^{−σm}η²,
  A_B := c_Bκ_+L²**; by bilinearity in (x_l, r_l(x)), **π_l(R^B_l(x) − R^B_l(x')) ≤ 2A_BL^{−σm}η||x − x'||_{(σ)}**.
- BA-6's residual part s_l = κ_lρ^{(2)}_l (own ≤ κC_6L^{−3(m+1)}η²): ||s||_{R(σ)} ≤ κ_+C_6L^{−3}max_mL^{(σ−1)m}η² = κ_+C_6L^{−3}η²;
  Lipschitz 2κ_+C_LipL^{−3}η||x − x'|| (F6, "C_Lip := 35Lp_L²").
- CR-1's s^C_l = (κ_l/2)[x_{l+1}, r_l] (residual type, CONFIRMED REVIEW_BFT_A_S3): own ≤ κ_+L^{−m}ηL^{−(2+σ)m}η, so
  ||s^C||_{R(σ)} ≤ κ_+max_mL^{−m}η² = κ_+η²; Lipschitz 2κ_+η.
- Wilson, level 0: ||q^c||_∞ ≤ 9η², [q^c]_α ≤ 4C_qη² (Corollary WR (a); CODEX_REVIEW_TR §5). Plain row at second order
  R^W_0 = (Dq_2)^T(dx_0), q_{2,p} = ½Σ_{a<a'}[y_a, y_{a'}] over the 4 links of p: each link lies in 2(d−1) = 6 plaquettes,
  each contributing ≤ ½·3 terms ad_{y_a}^T(dx_0)_p with |ad_y^TF| ≤ 2|y||F|, so own |R^W_0(b)| ≤ 18 sup|x_0|·sup|dx_0| and
  **π_0(R^W_0) ≤ 18||x^c_0||_∞||f_0||_∞ ≤ 36η²** (n³ = n·n²; ||f_0|| ≤ 2||∇^cx^c_0||). For the pointwise coarse Hölder
  seminorm, translate all factors together: [R^{W,c}_0]^∞_α ≤ 18([f_0]^∞_α||x^c_0|| + ||f_0||[x^c_0]^∞_α), with
  [x^c_0]^∞_α ≤ d||∇^cx^c_0|| (ℓ¹ paths, separations ≤ 1) and [f_0]^∞_α ≤ 2(C_C[∇^cx^c_0]_α + 2·8^α||∇^cx^c_0||) (BL-C), so
  **[R^{W,c}_0]^∞_α ≤ C_{W∞}η², C_{W∞} := 18(2C_C + 4·8^α + 2d)**; Lipschitz 2C_{W∞}η (bilinear).
**(b) All orders — PROVEN given (LA-1)-(LA-3).** With Lemma SG and |Θ| ≤ 2|ρ|, |ρ| ≤ L^{−(2+σ)m}η + C_ρL^{−3(m+1)}η²:
π_l(E_l|_l) ≤ L^{3(m+1)}C_Ec_Lp_LL^{−(m+1)}η·2|ρ| ≤ A_EL^{−σm}η²(1 + C_ρη), A_E := 2C_Ec_Lp_LL²; and
π_{l+1}(E_l|_{l+1}) ≤ L^{3m}C_E(L^{−m}η + p_L²η²)·2|ρ| ≤ A_E'L^{−σm}η²(1 + C_ρη), A_E' := 2C_E(1 + p_L²η_0);
||κ(Ψ − r)||_{R(σ)} ≤ κ_+(C_6L^{−3} + C_3' η)η². Lipschitz constants: the same with η² replaced by 2η||x − x'||_{(σ)}
(analyticity on a k-independent own-unit polydisc per word).
**(c) The level sums.** J(all plain rows at x) ≤ [36 + (A_B or A_E + A_E')/(1 − L^{−σ})]η², and the Lipschitz analogue with 2η.
**Uniform in k and T for every σ > 0. At σ = 0 (the 𝔐^∇ ball) the same computation gives (k − 1)A_Bη² + 36η²: the
level-count factor is exactly the σ = 0 endpoint of this family**, as KFACTOR_O55 §5 (a)-(b) argued. With σ = 1 the
ratio is L^{−1} = 1/3.

*Erratum to 2.2 (b) (self-check right after writing).* In the level-(l+1) bound the factor written "(L^{−m}η + p_L²η²)" must
read **(L^{−m}η + p_L²L^{−2(m+1)}η²)** (s_l² ≤ L^{−2(m+1)}η²); with it the second term is 2p_L²L^{−2}L^{−(1+σ)m}η³, so
A_E' := 2C_E(1 + p_L²L^{−2}η_0) and the conclusion is unchanged. (With the uncorrected factor the term would grow like
L^{(1−σ)m} for σ < 1.)

---

## §3. (T3) "The lane's existing off-critical remainder": what it is, why it cannot be bounded on the lane's route, and why the contraction does not need it

### 3.1 Lemma OC (the off-critical remainder, exactly) — PROVEN-HERE
For every chain source S and every gauge fixing Γ with ΓΞ = −1 on Λ_*, put μ := D^⊥(S) ∈ Λ_* (zero at the level-k roots).
Then
  **𝓛_Γ^{-1}S = x^{cc}(S + Γ^Tμ) + Ξμ,**
where S' := S + Γ^Tμ is cc and x^{cc}(S') := 𝓛_Γ^{-1}S' lies in Ker Γ with Hx^{cc} = S' (so its gauge-invariant outputs are
those of the Setting-LIN^cc critical point, Γ-independent). For the rescaled fixing cΓ (c > 0) the corrected source S' is
the same and the pure-gauge part is Ξμ/c².
*Proof.* (1) For λ ∈ Λ_*: ⟨S', Ξλ⟩ = ⟨D(S), λ⟩ + ⟨μ, ΓΞλ⟩ = ⟨μ, λ⟩ − ⟨μ, λ⟩ = 0 (λ vanishes on the roots, so
⟨D(S), λ⟩ = ⟨μ, λ⟩); the total charge of a divergence is 0. (2) 𝓛_Γ(x^{cc} + Ξμ) = S' + HΞμ + Γ^TΓΞμ = S' − Γ^Tμ = S
(HΞμ = 0 for μ ∈ Λ_*, Lemma FG (i); Γx^{cc} = 0, Lemma FG (iii)). (3) (cΓΞ)^T(cΓΞ) = c² on Λ_*, so the gauge parameter is
μ/c² and −(cΓ)^T(cΓ)Ξ(μ/c²) = Γ^Tμ. ∎
It contains Lemma GE (c) (Γ = Γ_E; BFT_B §31.3 (R1)) and Proposition GT-split (only D^⊥ enters) as special cases.
**Identification.** At an iterate of the Feynman map, S = NB + 𝔑^0(x) and μ = D^⊥(𝔑^0(x)) = −(K'^T_x∇F(x))^⊥ (Lemma CD) —
first order in the Newton residual ∇F(x), which is O(η), not small, at a generic point of the ball; in the Lipschitz
estimate S = 𝔑^0(x) − 𝔑^0(x'). **"The lane's existing off-critical remainder" (KFACTOR_O55 §5 (g), (i); BFT_B §31.3,
§36.5 (ii)) is therefore exactly two objects: (R-inv) the response to the explicit correction Γ^Tμ — what Proposition
NCR's ⟨D^⊥(S), λ^Γ_*⟩ pairs; its residual half is KFACTOR_O55's "♯-weighted residual pairing", its curvature half the
other half of (NC-Γ) off the critical set — and (R-gv) the pure gauge Ξμ/c² in the iterate's gauge-variant components.**
(KFACTOR_O55 §5 (i) names only the residual half of (R-inv); the curvature half is needed on that route as well — BFT_B
§36.5 (ii) — and is hidden in its "(H-lin^∇) [whatever its status]".)

### 3.2 On the lane's (Feynman, Γ_E) route it cannot be bounded with present inputs, at any σ
Lemma ΓT-op (e) (BFT_B §25.1 (e), used in §36.4) prices Γ_E^Tμ through ||μ||_∞ and the pinned box charges
Q_X(μ) = ⟨χ^5_Xμ⟩: π_0(Γ_E^Tμ) ≤ 5^d[(M_n/4)n³||μ||_∞ + 2^dC_∞n³max_X|Q_X(μ)|]. Here μ = d*R^W_0 + Σ_lev^{(l)T}d*R^B_l + …
is a divergence of plain rows, so a sup bound gives only n⁴||μ||_∞ ≲ 2d·n·(n³sup|R^W_0|), growing like n, and without box
neutrality n³max|Q_X| is not O(η²) either. So on this route the remainder needs exactly the lane's named inputs —
**(NEUT-box) (BFT_B §34.1, §36.4) plus a k-uniform bound on n⁴||D^⊥(S)||_∞ along the iteration, or (GT-sup) ⟸
(Y-sup^loc) (whose reduction is NOT-VERIFIED, REVIEW_BFT_B_S9_S10 S10-14)** — and none is proven. **The transport weight
changes none of it**: σ shrinks the rows; it does not change Γ_E^T, which carries each box's net charge to its level-k root
in one level-0 step. Check ko55_1 A4' shows that mechanism in a d = 2 model (same charges, same normaliser): single-level
routing costs ρ_single = 1, 3, 12, 39, 120 (≈ n/2) for k = 1..5, hierarchical routing ρ_hier = 1, 5/3, 17/9, 53/27, 161/81 (→ 2).
(R-gv) depends on the normalisation and vanishes in the hard-slice limit c → ∞; at c = 1 the only available bound on the
iterate's level-0 coarse potential near a level-(k−1) root is n·2dL^{−3}π_{k−1}(R^B_{k−1}), not k-uniform (that it is
attained for generic rows is ARGUED, not shown). **Verdict on the Feynman route: NOT boundable with present inputs; what
it needs is stated above.**

### 3.3 Lemma HR (hierarchical routing) — PROVEN-HERE; ko55_1 A1-A3 verify (i)-(iv) exactly on small lattices
*Definitions.* Roots are block centres, hence **nested**: the level-0 image of a level-(j+1) root is the level-j root of the
central level-j sub-block (L^{j+1}Y + (L^{j+1} − 1)/2 = L^j(LY + (L − 1)/2) + (L^j − 1)/2). For a level-j site Z (0 ≤ j < k) let
R(Z) be the root of its parent's block (a level-j site) and γ(Z) the level-j axial path from R(Z) to Z (fixed coordinate
order; it stays in the block; γ(Z) = ∅ iff Z = R(Z)). For a level-0 function u put V_j(Z) := Σ_{z ∈ level-j block of Z}u(z) and
  **(P^Tu)_j := Σ_Z V_j(Z)·γ(Z)** (a plain level-j current), 0 ≤ j ≤ k − 1.
P^T is the transpose of (PX)(z) := Σ_{j<k}⟨X_j, γ(Z_j(z))⟩ (Z_j(z) the level-j ancestor of z), and **P(Ξλ) = λ for every
λ ∈ Λ_*** (each term is λ(z_j) − λ(z_{j+1}), z_j the level-0 image of Z_j(z); the sum telescopes to λ(z) − λ(r) = λ(z)).
M_γ := the largest number of sites of one block whose paths use a given link **= L^{d−1}(L − 1)/2** (27 at d = 4, L = 3;
computed exactly in ko55_1 A2). Plain coarse units in d dimensions: π_j := L^{(d−1)(k−j)}·sup_own.
*Statements.*
- **(i) Identity.** D(P^Tu) = u − Σ_X(Σ_{z∈cell X}u(z))δ_{r_X}; in particular **D^⊥(P^Tu) = u^⊥**, and P^Tu does not depend on
  the values of u at the level-k roots.
- **(ii) Vanishing.** If u = ev^{(l)T}w then (P^Tu)_j = 0 for j < l.
- **(iii) Sup route.** If u = ev^{(l)T}d*w (w a level-l 1-form), then for l ≤ i < k: |V_i| ≤ 2dL^{(d−1)(i−l)}sup_own|w| and
  π_i((P^Tu)_i) ≤ 2dM_γπ_l(w); hence **J(P^Tu) ≤ 2dM_γ(k − l)π_l(w)**.
- **(iv) Hölder route (level 0).** If u = d*w, w a level-0 1-form with pointwise coarse Hölder seminorm [w^c]^∞_α of
  w^c = n^{d−1}w, then π_i((P^Tu)_i) ≤ dM_γ[w^c]^∞_αL^{−α(k−i)}; hence **J(P^Tu) ≤ dM_γ[w^c]^∞_α/(L^α − 1)**.
- **(v) Bare charges.** If u = ev^{(j)T}v, v any level-j function, then **J(P^Tu) ≤ (M_γ/(L − 1))·L^{d(k−j)}·sup|v|**.
*Proofs.* (i) A path is a unit current from start to end, so with d*v(Z) = Σ_μ[v(Z − e_μ, μ) − v(Z, μ)]:
d*γ(Z) = δ_Z − δ_{R(Z)}, hence d*(P^Tu)_j = V_j − Σ_YV_{j+1}(Y)δ_{R_Y}. Place by ev^{(j)T} and sum: at a level-0 site z that is
an image exactly at levels 0..J the sum telescopes to V_0(z) = u(z) if J < k and to u(r_X) − V_k(X) if z = r_X. A root value
u(r_X) enters only blocks whose level-j representative is a root, whose path is empty. (ii) For j < l a level-j block holds at
most one image of a level-l site, and then its level-j representative is a root (nesting), so its path is empty.
(iii) Summing d*w over the L^{i−l}-box of level-l sites telescopes along each of the L^{(d−1)(i−l)} lines in each direction
μ: **V_i(Z) = Σ_μΣ_{lines}[w(entry link) − w(exit link)]** (exact; ko55_1 A3), so |V_i| ≤ 2dL^{(d−1)(i−l)}sup|w|; each link
carries ≤ M_γ contributions; multiply by L^{(d−1)(k−i)} and use sup_own|w| = L^{−(d−1)(k−l)}π_l(w). (iv) On each line the
entry and exit links are L^i own steps = L^{i−k} coarse apart along one axis, so |w(exit) − w(entry)| ≤
n^{−(d−1)}[w^c]^∞_αL^{−α(k−i)}; then π_i ≤ L^{(d−1)(k−i)}M_γdL^{(d−1)i}n^{−(d−1)}[w^c]^∞_αL^{−α(k−i)} = dM_γ[w^c]^∞_αL^{−α(k−i)},
and Σ_{i=0}^{k−1}L^{−α(k−i)} ≤ 1/(L^α − 1). (v) |V_i| ≤ L^{d(i−j)}sup|v| (i ≥ j); π_i ≤ M_γL^{d(k−j)}L^{−(k−i)}sup|v|;
Σ_{i≥j}L^{−(k−i)} ≤ 1/(L − 1). ∎
*Contrast.* Routing the same charges to the level-k root through level-0 links only (the shape of Γ_E^T's compensation
term and of Γ_tent^T) has no bound of type (iii)-(iv): ko55_1 A4'.

### 3.4 Proposition CCP (the cc-projected iteration) — PROVEN-HERE (given Lemma CD in its banked root-pinned form, (GI))
Let Γ be a gauge fixing with ΓΞ = −1 on Λ_*, S̃(x) := NB + 𝔑^0(x; B) − P^TD^⊥(𝔑^0(x; B)), Φ̃_Γ(x) := 𝓛_Γ^{-1}S̃(x).
- **(a) Every source is cc.** D^⊥(NB) = 0 (the data enter only through the top residual and r_{k−1}(Ξλ) = d ev^{(k)}λ = 0
  for λ ∈ Λ_*), and D^⊥(P^TD^⊥(𝔑^0)) = D^⊥(𝔑^0) by HR (i). Hence Φ̃_Γ(x) ∈ Ker Γ, HΦ̃_Γ(x) = S̃(x), and its gauge-invariant
  outputs are those of the Setting-LIN^cc critical point with source S̃(x), whatever Γ is (Lemma FG (i), (iii)).
- **(b) Form.** Φ̃_Γ(x) = x − 𝓛_Γ^{-1}(M_x∇F(x) + Γ^TΓx), M_x := 1 − P^T(K'^T_x·)^⊥ (Lemma CD; 𝔑^0 = Hx − NB − ∇F).
- **(c) The M_x estimate.** If own |x_j(b)| ≤ ½ for all links, then for every chain g:
  **J(P^T(K'^T_xg)^⊥) ≤ 2d·c_Bern·L^{d−1}·max_j||x^c_j||_∞·J(g),  c_Bern := Σ_{n≥1}|B_n|/n! ≤ 59/100** (Bernoulli numbers;
  exact, ko55_1 B; symbol chosen to avoid the collision with (★)'s c_B).
  *Proof.* K_X(a, c) := d/dt|_0 log(e^{ta}e^Xe^{−tc}) = ψ_−(ad_X)a − ψ_+(ad_X)c with ψ_−(z) = z/(e^z − 1), ψ_+(z) = z/(1 − e^{−z})
  (from d/dt e^{Z} = e^{Z}((1 − e^{−ad_Z})/ad_Z)Z'), K_0(a, c) = a − c, and the Taylor coefficients of ψ_± − 1 have absolute
  values |B_n|/n!. With ||ad_X|| ≤ 2|X| ≤ 1: |K'_X(a, c)| ≤ 2c_Bern|X|(|a| + |c|) — exact, all orders. Transposing,
  K'^T_xg = Σ_jev^{(j)T}u_j with |u_j(Z)| ≤ Σ_{b∋Z}2c_Bern|x_j(b)||g_j(b)| ≤ 4dc_Bern·sup_own|x_j|·sup_own|g_j|; HR (v) gives
  J(P^Tev^{(j)T}u_j) ≤ (M_γ/(L−1))L^{d(k−j)}·4dc_BernL^{−(k−j)}||x^c_j||·L^{−(d−1)(k−j)}π_j(g_j) = 2dc_BernL^{d−1}||x^c_j||π_j(g_j). ∎
- **(d) Fixed points are exactly the slice critical points.** If max_j||x^c_j|| ≤ η' < (2dc_BernL^{d−1})^{−1} (≥ 1/126.4 at
  d = 4, L = 3), every fixed point x̃ of Φ̃_Γ has Γx̃ = 0 and ∇F(x̃) = 0; every critical point x̄ of F with Γx̄ = 0 in that
  region is a fixed point.
  *Proof.* x̃ = 𝓛_Γ^{-1}S̃(x̃) ∈ Ker Γ by (a). Then (b) gives M_{x̃}∇F(x̃) = 0, i.e. ∇F(x̃) = P^T(K'^T_{x̃}∇F(x̃))^⊥, and (c)
  gives J(∇F(x̃)) ≤ 2dc_BernL^{d−1}η'J(∇F(x̃)) < J(∇F(x̃)) unless ∇F(x̃) = 0 (J is a norm on chains). Conversely ∇F(x̄) = 0
  gives D^⊥(𝔑^0(x̄)) = 0 (Lemma CD), so S̃(x̄) = NB + 𝔑^0(x̄) = Hx̄ = 𝓛_Γx̄. ∎
- **Scope.** BFT-0's "unique modulo composite gauges trivial at level k" additionally needs every critical point of the ball
  to be gauge-equivalent to one in Ker Γ — a nonlinear slice statement of (FP♯') type, unchanged by this file. The
  nonlinear Faddeev-Popov hypothesis of Lemma CD (ii) ("Γ_EK_x is a bijection") is replaced in (d) by the explicit
  estimate (c).

### 3.5 Proposition CB (the correction is k- and T-uniform in the σ-ball) — PROVEN at second order; all orders given (LA)
For ||x||_{(σ)}, ||x'||_{(σ)} ≤ η ≤ η_0 and 0 < σ ≤ 1:
  **J(P^TD^⊥(𝔑^0(x))) ≤ K_C(σ)η²,  J(P^TD^⊥(𝔑^0(x)) − P^TD^⊥(𝔑^0(x'))) ≤ 2K_C(σ)η||x − x'||_{(σ)},**
  **K_C(σ) := dM_γC_{W∞}/(L^α − 1) + 2dM_γA_B/(1 − L^{−σ})²** (all orders: A_B → A_E + A_E', plus the level-(l+1) parts, same form).
*Proof.* Divergence-form and residual-type sources have D^⊥ = 0 (d*d* = 0; d*Q_l^T = ev^Td*), so for any representation
D^⊥(𝔑^0) = D^⊥(plain rows) exactly. The Wilson plain row is routed by HR (iv) with ROW^{(σ)} (a)'s [R^{W,c}_0]^∞_α ≤ C_{W∞}η²;
each R^B_l by HR (iii): Σ_l2dM_γ(k − l)π_l(R^B_l) ≤ 2dM_γA_BΣ_{m=0}^{k−1}(m + 1)L^{−σm}η² ≤ 2dM_γA_Bη²/(1 − L^{−σ})². Lipschitz:
P^TD^⊥ is linear, and ROW^{(σ)} gives the Lipschitz bounds of the rows. ∎
**At σ = 0 the same proof gives Σ_l(k − l)A_Bη² ≍ k²A_Bη²: the transport weight is essential to the cc-projection too.**
(σ = 1, L = 3: Σ_m(m + 1)3^{−m} = 9/4 exactly; 1/(3^{1/4} − 1) < 3.165 — ko55_1 C.)

### 3.6 Reading
With Γ_hier := −P (a valid gauge fixing: Γ_hierΞλ = −λ on Λ_*; Ker H ∩ Ker Γ_hier = 0), Lemma OC's correction is
Γ_hier^Tμ = −P^TD^⊥(S): **Φ̃_Γ is the Feynman iteration in the multiscale axial gauge Γ_hier, re-projected into a slice
Γ of one's choice.** The gauge-invariant outputs see only Γ_hier's hierarchical routing (bounded, Proposition CB); the iterates
stay in Ker Γ (no pure-gauge spikes); Γ remains free for the gauge-variant estimate. The (TENT-Q)/(NEUT-box)/(GT-sup)
obstruction is a property of Γ_E's single-level routing, not of the problem. This answers REVIEW_BFT_A_S8's open question 1
("Does the contraction's linear solve have to meet non-composite-co-closed sources at all?"): **no**; and "the remainder
bound it needs" is Proposition CB. Lemma RC's *Reading* (L^{2k−3}η²) concerns Γ_E-responses to non-cc sources, which the
cc-projected iteration never forms.

---

## §4. (T2, second half) The contraction contracts, k- and T-uniformly, with the weights actually delivered

### 4.1 Lemma TOP♯ (the top residual of a cc response) — PROVEN as an implication; T ≥ 3
Fix 0 < m_w < m_*' (the rate of Proposition W / Corollary FP). For every cc source S ≅ (G_0, s, j) with homogeneous data and
every level-k link b:
  **|r_{k−1}(x(S))(b)| ≤ C_{LIN0}(||G^c_0||_∞ + [G^c_0]_α + ||s||_R) + C_top·J(j),  C_top := 4C_FP(m_w)S_4(m_w)/κ_-,**
S_4(m) := e^{4m}((1 + e^{−m})/(1 − e^{−m}))^4, uniformly in k and T ≥ 3.
*Proof.* By Lemma FG (ii)-(iii), r_{k−1}(x)(b) = ⟨S, Y^{(b)}⟩ for EVERY representative of the top probe (the response to
s_{k−1} = δ_b), because S is cc and representatives differ by Ξλ, λ ∈ Λ_0. Split S = S^{G,s} + S^j. S^{G,s} has no plain
currents and D(S^{G,s}) = ev_k^Td*s_{k−1} is root-supported, so it is a level-wise Setting-LIN source and Corollary LIN0
(CONFIRMED, REVIEW_BFT_A_S6) bounds its top residual by C_{LIN0}(||G||_Y + ||s||_R). For S^j (cc, being S − S^{G,s}) use the
tent-axial representative PY^{(b)}: by Lemma TS (BFT_A §12.2) Y^{(b)} is the source-free minimiser with data δ_b/κ_{k−1}, so
Corollary FP (CONFIRMED, REVIEW_BFT_A_S3: "Step 3 (TS, W, Λ, LR-pot, FP): CONFIRMED") gives ||(PY^{(b)})^c_l||_{∞,m_w} ≤
C_FP(m_w)/κ_- with weights centred at b, i.e. own |(PY^{(b)})_l(b')| ≤ L^{−(k−l)}C_FPe^{−m_w d(b',b)}/κ_-. Summing over the
d·L^{d(k−l)} level-l links of each coarse cell and over cells (cell diameter ≤ d coarse units, absorbed by e^{4m_w}; the sum
over a T-torus is at most the sum over Z⁴): Σ_{b'}|(PY^{(b)})_l(b')| ≤ dL^{(d−1)(k−l)}C_FPS_4(m_w)/κ_-. Hence
|⟨j_l, (PY^{(b)})_l⟩| ≤ sup_own|j_l|·dL^{3(k−l)}C_FPS_4/κ_- = 4C_FPS_4π_l(j_l)/κ_- (d = 4); sum over l. ∎
*Status change.* This is KFACTOR_O55's **Remark TOP-crit**, there ARGUED with three items unchecked ("Corollary FP's
constants, the T ≥ 3 proviso …, or the normalisation of Y^{(b)}"); all three are settled above (FP CONFIRMED; T ≥ 3 is FP's
and LR-pot's scope and inside BFT's T ≥ T_0; normalisation from Lemma TS). It supplies the top-response term that
(C2-COF)'s Hölder line and Proposition TW keep.

### 4.2 Proposition LIN^{(σ)} (gauge-invariant half of the linear estimate, cc sources, weight σ) — PROVEN as an implication
For 0 < α < θ ≤ σ ≤ 1, every cc source S ≅ (G_0, s, j) and data B_k, the cc response x obeys
  **||x||_{inv,(σ)} ≤ G_inv(σ)·[ ||B_k||_D + N^{(σ)}(S) ],**  G_inv(σ) independent of k and T ≥ 3.
*Proof, component by component.*
(1) *Residuals (Proposition TW at weight σ; KFACTOR_O55 §5 (e) is σ = 1).* Lemma RT-cc (c) + Lemma TC (both CONFIRMED,
REVIEW_BFT_B_S9_S10; transpose-column count re-done in CODEX_REVIEW_TR §2) with no positive-level G: for 0 ≤ i ≤ k − 2,
||r^c_i|| ≤ κ_-^{−1}[||s^c_i|| + L^{−2m}(||ρ_{k−1}||_∞ + Σ_{l>i}π_l(ĵ_l))], ρ_{k−1} = κ_{k−1}r_{k−1} − s_{k−1}. Lemma FT (ii)
gives Σ_lπ_l(ĵ_l) ≤ C_fJ, C_f = 1 + 2d/(1 − L^{−3}) = 121/13. Multiply by L^{(1+σ)m}:
  **L^{(1+σ)m}||r^c_i|| ≤ κ_-^{−1}[ ||s||_{R(σ)} + L^{(σ−1)m}(κ_+||r_{k−1}||_∞ + ||s_{k−1}||_∞ + C_fJ) ],**
and ||r_{k−1}|| is bounded by Lemma TOP♯. Data: BL-4's L^{k−1−i}||r^c_i|| ≤ κ̂L^{−(k−1−i)}||r_{k−1}|| gives the σ-weight with
constant κ̂ (σ ≤ 1). **The residual exponent delivered is 2 + σ — with nonlinear residual-type sources included, because
they sit in (R(σ)) (ROW^{(σ)} (a)); this is (C2) θ_w^r ≤ 2 + θ_R with θ_R = σ, at equality.**
(2) *f_0.* (C2-COF) (BANKED, conditional on its lane-A inputs; CODEX_REVIEW_C2 §4): ||f_0||_∞ ≤ C·N,
N = ||G^c_0||_∞ + [G^c_0]_α + ||G||_Y + ||s||_R + J ≤ (1 + L^θ)N^{(σ)}(S) (||s||_R ≤ L^θ||s||_{R(σ)} as θ ≤ σ); and
||f_0||_∞ + [f_0]^∞_α ≤ C[N + κ_+||r^c_{k−1}||_∞], the last term by Lemma TOP♯. Data: BL-4.
(3) *f_j, j ≥ 1.* Theorem CO-upR / Lemma RH (BFT_A §23.8-23.9; CONFIRMED, REVIEW_BFT_A_S5): f_j = 𝒜^{(0→j)}f_0 − R_j with
||R_j||, [R_j]_α ≤ Σ_{i<j}4L^{α(k−j)}L^{2(k−1−i)}sup_own|r_i| (the sup with the factor L^{α(k−j)} dropped). With
L^{2m}sup_own|r_i| = L^m||r^c_i|| ≤ L^{−σm}B_res (B_res the bound of (1)) and k − 1 − i ≥ k − j:
L^{α(k−j)}L^{−σ(k−1−i)} ≤ L^{−σ(j−1−i)} (α < σ), so ||R_j|| + [R_j]_α ≤ 8B_res/(1 − L^{−σ}); 𝒜^{(0→j)} is a probability
average (BL-2 (d)) and CO-upR controls its Hölder seminorm by f_0's. ∎

### 4.3 Potentials (θ_A = 1 delivered) — in the tent-axial slice, PROVEN as an implication
Lemma LR-pot at m = 0 (CONFIRMED, REVIEW_BFT_A_S3; T ≥ 3; C_1 = 775, C_2 = 40, C_3 = 205) holds **for every configuration**:
||(Px)^c_j||_∞ ≤ C_1||f_0||_∞ + C_2||B_k||_D + C_3Σ_{i<k}||r^c_i||_∞. With Σ_i||r^c_i|| ≤ (1 − L^{−(1+σ)})^{−1}||x||_{inv,(σ)}:
for x ∈ Ker Γ_tent, **max_j||x^c_j||_∞ ≤ C_1||f_0|| + C_2||B_k||_D + C_3(1 − L^{−(1+σ)})^{−1}||x||_{inv,(σ)}** — θ_A = 1, the hard cap
(REVIEW55_TUNIF W8). *But* Γ_tent is not a slice for the gradient components: its potential at a link is a path-averaged
curvature flux through strips of coarse length ≤ 1, so its coarse gradient picks up ≍ n^{1−α}[f_0]_α — BFT_A §3.10's
axial-gauge loss "L^{k(1−α)}" (ARGUED here).

### 4.4 The one OPEN input of the contraction
**(GV^{(σ)})_Γ** — the gauge-variant half for cc sources in ONE slice: a gauge fixing Γ (ΓΞ = −1 on Λ_*) and G_gv < ∞,
independent of k and T, such that for every cc source S and data B_k the response x ∈ Ker Γ obeys
max_j(||x^c_j||_∞ + ||∇^cx^c_j||_∞ + [∇^cx^c_j]_α) ≤ G_gv[||B_k||_D + N^{(σ)}(S)].
It is BFT_A §3.11's "(G♯_0-field^∇) … OPEN; needs … a slice whose potentials are coarse-C^{1,α}", restricted to cc sources
and read at weight σ — **pre-existing, not created by this file and not related to the level count.** Two facts bear on
it: potentials are delivered in Γ_tent (4.3) but not gradients; and REVIEW_BFT_A_S3's counterexample to LR-grad ("A rough
exact residual r_{j−1} = dψ forces [∇^cx^c]_α ≳ L^{α(k−j)}||x||_inv in every gauge") **does not survive at σ ≥ α**: the same
mechanism gives own |dψ| = |r_{j−1}| ≤ L^{−(2+σ)(k−j)}||x||_{inv,(σ)}, a coarse gradient ≲ L^{2(k−j)}·L^{−(2+σ)(k−j)} =
L^{−σ(k−j)}, and an own-scale Hölder quotient ≲ L^{(α−σ)(k−j)}, bounded (ARGUED). This removes the known obstruction; it
does not prove (GV).

### 4.5 Theorem K^{(σ)} (the composite contraction in the transport-weighted pair) — PROVEN as an implication of (GV^{(σ)})_Γ [OPEN] and, beyond second order, (LA-1)-(LA-3) [ARGUED-standard]
*Hypotheses.* §1.1's setting (𝒞_glob, trivial background, m = 0, T ≥ 3); 0 < α < θ ≤ σ ≤ 1; Γ with ΓΞ = −1 on Λ_* and
(GV^{(σ)})_Γ.
*Conclusion.* There are ε_0 > 0 and C_0 < ∞ depending only on (N, L, κ_±, α, θ, σ) and the named constants — **not on k
or T** — such that for s = ||B_k||_D ≤ ε_0 the map Φ̃_Γ sends 𝔅 := {x ∈ Ker Γ : ||x||_{(σ)} ≤ C_0s} into itself with
Lip ≤ ½; its fixed point is the unique critical point of 𝔉_k∘exp in 𝔅; BFT-1 holds with (θ_w^c, θ_w^r, θ_A) = (2, 2 + σ, 1)
in the form of §1.4; BFT-2 holds by BA-10's argument (Φ̃_Γ is holomorphic in (x, B): P^TD^⊥ is linear). **No level-count
factor and no off-critical remainder occur: the only level sums in any constant are Σ_mL^{−σm}, Σ_m(m + 1)L^{−σm} and
Σ_mL^{−αm}.**
*Proof.* Let G_♯ := G_inv(σ) + G_gv bound the 𝔐^{(σ)}-norm of the Ker Γ response to a cc source (4.2, 4.4; potentials also by
4.3 when Γ = Γ_tent). The source map x ↦ S̃(x) has N^{(σ)}-Lipschitz constant ≤ 2(K_rows + K_C(σ))(||x|| + ||x'|| + s) on the
ball, with K_rows := 9 + 4C_q + κ_+(C_6L^{−3} + 1) + C_LipL^{−3}κ_+ + 36 + A_B/(1 − L^{−σ}) at second order (ROW^{(σ)} (a); the
B-dependence of the top soft term contributes O(s), as in NA-IFT's "Lip ≤ C(||x|| + ||x'|| + s)") and K_C(σ) of
Proposition CB; at all orders A_B → A_E + A_E' (ROW^{(σ)} (b)). All sources are cc (CCP (a)), so
Lip(Φ̃_Γ) ≤ 2G_♯(K_rows + K_C)(2C_0 + 1)s and ||Φ̃_Γ(0)||_{(σ)} ≤ G_♯(||B_k||_D + Cs²). Take C_0 := 4G_♯ and ε_0 so small
that 2G_♯(K_rows + K_C)(2C_0 + 1)ε_0 ≤ ½, Cε_0 ≤ 1 and C_0ε_0 ≤ min(η_0, (2dc_BernL^{d−1})^{−1}); Banach gives the fixed
point, and CCP (d) makes it the slice critical point and gives uniqueness among slice critical points in 𝔅. ∎

### 4.6 Exponent bookkeeping: the "A" of the task, with the delivered weights
Delivered: θ_w^c = 2 (BA-3; 4.2 (2)-(3)); θ_w^r = 2 + σ (4.2 (1) with (R(σ))); θ_A = 1 (4.3 / (GV); hard cap). The rows'
level ratio: π_l(R^B_l) ∝ L^{((d−1) − θ_A − θ_w^r)(k−l)}L^{θ_w^r} (R^B_l ∝ x_l·r_l, π_l = L^{(d−1)(k−l)}sup_own), exponent
3 − 1 − (2 + σ) = **−σ**. NORMS §N7's soft-vertex ratio A = L^{d−θ_w^r−2θ_A} = L^{4−(2+σ)−2} = **L^{−σ}**: the two counts
differ by θ_A − 1 and coincide at the delivered θ_A = 1. **A = L^{−σ} < 1 ⟺ σ > 0 ⟺ θ_w^r > 2** (REVIEW55_TUNIF W5 (a)),
**and at σ = 1 (θ_w^r = d − 1 = 3): A = 1/L = 1/3** — the A_soft of Theorem N1-15 ((T-UNIF), banked) and NORMS l.662's
"margin exactly one power of L". The θ-window is 0 < α < θ ≤ σ ≤ 1 (BL-5 (a) has "no upper restriction on θ", so θ_R = σ = 1
is admissible; the (R)-slot exponent 2 + θ of REVIEW55_TUNIF W4 is 2 + θ_R).

*Erratum to 3.4 (d) (self-check).* The rigorous threshold from ko55_1 B (c_Bern ≤ 59/100) is
(2dc_BernL^{d−1})^{−1} ≥ 1/(216·0.59) = 1/127.44 at d = 4, L = 3; the "≥ 1/126.4" I wrote uses the displayed value
c_Bern = 0.58476 and is true but not certified by an exact gate. Read **≥ 1/127.44**.

---

## §5. (T4) Consistency with what is banked, and with the Codex reviews

1. **[S26-BANKED] (T-UNIF), repaired.** No conflict. Theorem N1-15 bounds D³E_k^br(1) in N3 norms; this file bounds the
   Lipschitz constant of the composite map in 𝔐^{(σ)}. Same exponent triple (2, 3, 1) at σ = 1 and the same ratio 1/L
   (4.6). This file does not use NQ-1: θ_A = 1 comes from LR-pot in Γ_tent (4.3) or is part of (GV^{(σ)})_Γ.
2. **[S26-BANKED] (CO-fun), sup half on the composite class.** Used exactly as banked in 4.2 (2), conditional on its named
   lane-A inputs. The Hölder half keeps the top-response term in the bank; **this file bounds that term (Lemma TOP♯, T ≥ 3)**
   — a new step, not yet reviewed by Codex; until it is, read 4.2 (2)'s Hölder clause as conditional on TOP♯.
3. **[S26-BANKED] (CC-0) at every critical point REFUTED.** Never assumed. CCP needs only D^⊥ = 0 and creates level-k root
   charges on purpose (HR (i)); (C2-COF) prices root charges through J (CODEX_REVIEW_C2 §3-§4). Lemma CD is used only in its
   banked root-pinned form, D^⊥(𝔑^0) = −(K'^T_x∇F)^⊥ (CCP (b), (d)).
4. **[S26-BANKED] GZ-SLOT/GZ-FALSE, NLOC NL-3′, a_RS.** Not touched (trivial background; no NLOC or RLARGE input).
5. **CODEX_REVIEW_TR.** I agree with every verdict, in particular its §1 sign correction (applied), §2 (RT-cc/TC/FT give the
   extra power; CONFIRMED by me in 4.2 (1)), §4 (summation sound), and its §3/item 5 NOT-VERIFIED (the full nonlinear
   source). **Corollary SG-TR (PROVEN given (LA-1)-(LA-3)):** Lemma SG supplies the "sufficient repair" CODEX_REVIEW_TR §3
   writes down — an exact decomposition of 𝔑^0 with no positive-level divergence slot, residual-type part κ_l(Ψ_l − r_l) with
   ||κ(Ψ − r)^c_i|| ≤ A_s'L^{−2m}η² in the 𝔐^∇-ball (|Ψ − ρ| ≤ C|ρ|³, |ρ − r| by (LA-2)), and plain parts E_l with
   π_l ≤ A_Eη², π_{l+1} ≤ A_E'η² per level — so TR-1 holds for the full nonlinear source; feeding TR-1 back into Lemma SG gives
   π_l(E_l) ≲ L²L^{−(k−1−l)}η²(1 + O((k − l)η)) for the full plain rows, so their sum is k-uniform. This narrows Codex TR's
   NOT-VERIFIED item 5 to the local analytic constants (LA); it does not bank anything and must itself be reviewed.
6. **CODEX_REVIEW_C2.** Used: (C2-COF) (§4 there), CD on root-pinned directions (§6), the terminal-slot correction
   D(S^s) = ev_k^Td*s_{k−1} (§4). AGREE with all three; I did not re-run its enumeration.
7. **KFACTOR_O55 §5.** (b) diagnosis CONFIRMED (𝔐^∇'s residual exponent is 2; responses deliver 2 + σ). (c) definitions:
   σ = 1 of §1.2. (d) ROW♯ at second order CONFIRMED (re-derived, ROW^{(σ)} (a)). (e) Proposition TW CONFIRMED (re-derived,
   4.2 (1)), its top-residual input now Lemma TOP♯. (f) inclusions CONFIRMED (need θ ≤ σ; σ = 1 there). (g) "BFT-0 in
   (𝔐^♯, 𝒴^♯) ⟸ … + the off-critical NCR remainder [OPEN] + …": **SUPERSEDED** — the contraction can be run without that
   remainder (CCP + HR + CB); what remains is (GV^{(σ)})_Γ and (LA). Its sentence "In this pair the plain-row level sum is
   k-uniform; the level-count factor occurs nowhere" is CONFIRMED (rows and, with the extra (m + 1), the routing correction).
   (i) "The exact missing object … Proposition TW off the critical set, i.e. the ♯-weighted residual pairing …":
   **REFUTED as the missing object** — on the Feynman route it omits the curvature half (BFT_B §36.5 (ii)), and on the
   cc-projected route neither half is needed.
8. **REVIEW55_TUNIF.** W5 (a) (requirement θ_w^r > 2 strictly): CONFIRMED (4.6). W4 ("θ_w^r = 3 is data-only; 2 + θ with
   residual-type sources"): CONFIRMED with a precision — the cap is 2 + θ_R, θ_R the (R)-slot exponent; θ_R = 1 is admissible
   (BL-5 (a)) and the nonlinear residual-type rows fit (R(1)) (ROW^{(σ)} (a)), so θ_w^r = 3 is delivered with them too.
   W6 ((1c) must be stated for the displacement relative to the holonomy-carrying centre / by the data size): CONFIRMED and
   adopted (§1.4).
9. **BFT_B §31.3, §36.5 (ii)** ("(NC-Γ) for Γ_E, off the critical set, reduces to … (TENT-Q) + (NEUT-box) … OPEN"):
   CONFIRMED as a statement about the Feynman/Γ_E route (Lemma OC re-derives its (R1) for every Γ with ΓΞ = −1). Its
   (TENT-Q) face is already dissolved by the banked whole-class (C2-COF); the remaining face is not on the contraction's path.
10. **REVIEW_BFT_B_S9_S10** "the contraction that is supposed to construct that fixed point needs the estimate at
    non-critical iterates, which is the OPEN half": CONFIRMED for the Feynman iteration; **not true of Φ̃_Γ**, whose linear
    solves meet only cc sources.
11. **REVIEW_BFT_A_S8, "The biggest live wall in lane A", question 1**: answered — no; the remainder bound it asks for is
    Proposition CB.
12. **PROOF.md tally.** No tally claim; every result here is lane-level.

---

## §6. What remains, exactly

1. **(GV^{(σ)})_Γ — OPEN; the only open input of Theorem K^{(σ)} at second order.** The gauge-variant half (potentials and
   their coarse C^{1,α}) of the linear estimate for **cc** sources in ONE slice Γ. Pre-existing (BFT_A §3.11's
   (G♯_0-field^∇)), independent of the level count. Known: potentials in Γ_tent (4.3); Γ_tent fails gradients at Hölder
   regularity (ARGUED); the LR-grad counterexample is defused at σ ≥ α (ARGUED). Natural candidate: an elliptic slice
   (Γ_E), where gradients are Schauder-controlled within boxes — not attempted here.
2. **(LA-1)-(LA-3) — local analytic Taylor bounds** (contour BCH and its derivative, NA-alg's maximiser and soft kernel, the
   Wilson class function) on a fixed own-unit neighbourhood, constants depending on (N, L, d) through p_L — ARGUED-standard.
   Needed only beyond second order; Lemma SG has already made the level structure of every order exact.
3. **Inherited, unchanged:** Corollary WR (a)'s named hypothesis (REVIEW_BFT_A_S6 "CONFIRMED-WITH-FIX (a hypothesis must be
   named)"); BFT-0's "unique modulo composite gauges" quantifier (a nonlinear slice statement of (FP♯') type); (CL-4)
   identification with the per-level tower (BA-9, Balaban's convention); the scope 𝒞_glob / trivial background / m = 0 /
   T ≥ 3 (outside 𝒞_glob: (G♯-patch), (UHL), (SL-cov), the smooth lift; m > 0: BFT-3).
4. **Not remaining for BFT-0:** the level-count factor (σ > 0), and the off-critical remainder (TENT-Q)/(NEUT-box)/(GT-sup)/
   (Y-sup^loc) — these stay relevant to any statement about Feynman-gauge responses to non-cc sources, e.g. BFT-5 as worded
   for "a general source" (BFT_B §27.5), but not to the construction of the critical point.
5. **Reviews this file needs before anything is banked** (attack in this order): CCP (d) (injectivity of M_x in J, and that
   fixed points are critical — the only place the Ward identity enters); Lemma HR (iii)-(iv) (flux identity, multiplicity
   M_γ, the (k − l) count); Proposition CB (the Wilson-row Hölder route; the Σ(m + 1)L^{−σm} sum); Lemma TOP♯ (FP's weighted
   bound and the ℓ¹ sum); Lemma SG (the envelope step and Re tr(ZG) = 0); Corollary SG-TR.

---

## §7. Check record — ko55_1

- Files (`TZ=UTC stat`, birth | modification): **checks/ko55_1_criteria.md 00:22:05Z | 00:22:52Z** (one append-only
  AMENDMENT 1 at 00:22:52Z, before the script existed: it replaced the registered A4 — whose test current was divergence-free,
  making A4 vacuous, and whose control compared un-normalised growth — by A4'); **checks/ko55_1.py 00:24:30Z | 00:24:30Z**;
  **checks/ko55_1_out.txt 00:24:39Z | 00:24:40Z**; **checks/ko55_1_err.txt** (contains only the three `/usr/bin/time -p`
  lines, real 1.41 s; no Python error). All 2026-10-29. Criteria-before-script holds for the original and the amendment.
  SHA-256: criteria 75f6b04a…432ed, script 534469aa…31e1c, out de6f6fda…5d31, err da480eaf…0a4b.
- Exact integer/Fraction arithmetic in every verdict; floats only in display lines. Python run with `-I`.
- **Results (verbatim verdicts): A1 PASS (8 lattices, d ∈ {2, 4}, up to 6561 sites, 0 mismatches); A1-ctl PASS (corner
  routing fires in all 8 cases, skip-level-1 fires in all 6 cases with k ≥ 2); A2 PASS (M_γ = 3 and 27 = L^{d−1}(L−1)/2
  exactly; vanishing below l; flux and current bounds; largest observed current/bound ratio 1/2); A3 PASS (flux identity in
  every level-i block, 6 lattices); A4' PASS ((a) ρ_hier = 1, 5/3, 17/9, 53/27, 161/81 ≤ 3 = dM_γ/(L−1) for k = 1..5;
  (b) ρ_single = 1, 3, 12, 39, 120, ratio ρ_single(5)/ρ_single(2) = 40 ≥ 10); B PASS (S_60 + tail ≤ 59/100, S_60 ≈ 0.58476);
  C PASS (Σ(m + 1)3^{−m} < 9/4 with exact closed form for M ≤ 400; (1316/1000)^4 < 3). OVERALL PASS.**
- **Discriminating power (systemic defect 3).** A1 and A3 are exact identities that fail under a wrong routing or wrong
  nesting (A1-ctl exhibits two such failures). A2 can fail on the multiplicity or the flux count. A4' (a) is a rigorous instance
  of HR (iv) at α = 1 and could fail; A4' (b) is a control that fires. B and C can fail on the constants. **What ko55_1 does
  NOT test:** any nonlinear Yang-Mills estimate, the linear response theory (TW, (C2-COF), TOP♯, LR-pot), Lemma SG, (LA), or
  CCP (d); those rest on the proofs above and the cited lemmas. A4' uses axial single-level routing as a stand-in for the
  shape of Γ_E^T's compensation term; it is an illustration of the mechanism, not a measurement of Γ_E.

---

## §8. Answers to the four targets, and the summary table (written 2026-10-29T00:50Z UTC)

**T1 (the contraction stated).** §1: the lane's composite contraction in the family 𝔐^{(σ)}, σ ∈ (0, 1] (residual weight
θ_w^r = 2 + σ; σ = 1 is the transport weight 3 of NORMS / [S24-fix 3]; the (R)-slot exponent θ_R = σ makes the delivered
exponent 2 + σ *with* nonlinear residual-type sources), source functional N^{(σ)} (plain currents priced by their coarse sum
J, as (C2-COF) needs), the cc-projected map Φ̃_Γ = x − 𝓛_Γ^{-1}(M_x∇F + Γ^TΓx) (one composite inverse; anti-circularity
satisfied), BFT-1 with (1c) for the displacement relative to the centre / by the data size (W6).
**T2 (rows summable; contraction contracts).** ROW^{(σ)}: Σ_lπ_l(rows) ≤ [36 + A_B/(1 − L^{−σ})]η² and the Lipschitz analogue,
k- and T-uniform for every σ > 0 (second order PROVEN; all orders given (LA)); the level-count factor is exactly the σ = 0
endpoint. Theorem K^{(σ)}: Lip(Φ̃_Γ) ≤ ½ on a k-, T-independent ball, with A = L^{−σ} (= 1/3 at σ = 1) computed from the
delivered (θ_w^c, θ_w^r, θ_A) = (2, 2 + σ, 1) — conditional on (GV^{(σ)})_Γ.
**T3 (the off-critical remainder).** Identified exactly (Lemma OC): the response to Γ^TD^⊥(S) plus the pure gauge ΞD^⊥(S)/c².
On the lane's Feynman/Γ_E route it **cannot be bounded with present inputs** at any σ; it needs (NEUT-box) plus a k-uniform
bound on n⁴||D^⊥(S)||_∞ along the iteration, or (GT-sup) ⟸ (Y-sup^loc) (reduction NOT-VERIFIED). **It is not needed:** the
cc-projected iteration (CCP) meets only cc sources, its fixed points are exactly the slice critical points, and its
correction P^TD^⊥ is bounded k- and T-uniformly in the σ-ball (Lemma HR, Proposition CB). The remaining open input of the
contraction is the pre-existing gauge-variant half (GV^{(σ)})_Γ.
**T4 (consistency).** §5: consistent with every [S26-BANKED] item; (CC-0) never used; Lemma CD only root-pinned; (C2-COF)'s
sup half used as banked and its Hölder top term now supplied by TOP♯ (to be reviewed).

| # | Claim (file, locating string) | Verdict / status | Where |
|---|---|---|---|
| N1 | Lemma SG: δσ_c = κ[−Re tr(ΘW_0^{-1}δM) + Re tr(ZΘG)], soft gradient = κR^TΨ + κE_l exactly | **PROVEN-HERE** (identity, given NA-alg (a)-(b)); bounds given (LA-1)-(LA-3) | 2.1 |
| N2 | ROW^{(σ)} (a): second-order rows, sizes and Lipschitz, decay L^{−σm} | **PROVEN** (re-derived from BA-6, F6, CR-1, WR (a), (★)) | 2.2 |
| N3 | ROW^{(σ)} (b): all orders | **PROVEN given (LA)** | 2.2 |
| N4 | Lemma OC: 𝓛_Γ^{-1}S = x^cc(S + Γ^TD^⊥S) + ΞD^⊥S | **PROVEN-HERE** | 3.1 |
| N5 | Feynman/Γ_E off-critical remainder not boundable with present inputs; needs (NEUT-box) + n⁴‖D^⊥‖ bound, or (GT-sup) | **status statement** (what is missing), with A4' illustration | 3.2 |
| N6 | Lemma HR (i)-(v): hierarchical routing identity and bounds | **PROVEN-HERE**; ko55_1 A1-A3 exact on small lattices | 3.3 |
| N7 | Proposition CCP (a)-(d): cc sources; Φ̃ = x − 𝓛^{-1}(M_x∇F + Γ^TΓx); J-bound of P^TK'^T; fixed points = slice critical points | **PROVEN-HERE** (given Lemma CD root-pinned, (GI)); ko55_1 B for c_Bern | 3.4 |
| N8 | Proposition CB: J(P^TD^⊥𝔑^0) ≤ K_C(σ)η², Lipschitz 2K_Cη, k-, T-uniform for σ > 0; ≍ k² at σ = 0 | **PROVEN** (second order); all orders given (LA) | 3.5 |
| N9 | Φ̃_Γ = Feynman iteration in Γ_hier = −P, re-projected | **PROVEN** (from N4) | 3.6 |
| N10 | Lemma TOP♯ (top residual of cc responses ≤ C(‖G‖ + ‖s‖) + C_top·J), T ≥ 3 | **PROVEN as an implication** (FP, FG, TS, LIN0) | 4.1 |
| N11 | Proposition LIN^{(σ)} (gauge-invariant half, cc sources) | **PROVEN as an implication** (RT-cc, TC, FT, (C2-COF), TOP♯, BL-4, CO-upR/RH) | 4.2 |
| N12 | Potentials (θ_A = 1) in Γ_tent from LR-pot | **PROVEN as an implication** | 4.3 |
| N13 | Γ_tent fails the gradient components at Hölder regularity | **ARGUED** | 4.3 |
| N14 | LR-grad's counterexample defused at σ ≥ α | **ARGUED** | 4.4 |
| N15 | Theorem K^{(σ)} | **PROVEN as an implication of (GV^{(σ)})_Γ [OPEN]** (+ (LA) beyond second order) | 4.5 |
| N16 | A = L^{−σ}; row ratio = NORMS's A at θ_A = 1; = 1/3 at σ = 1 | **PROVEN** (exponent arithmetic) | 4.6 |
| N17 | Corollary SG-TR: Lemma TR for the full nonlinear source | **PROVEN given (LA)** | §5.5 |
| O1 | KFACTOR_O55 §5 (a): in the 𝔐^∇ pair the level-count factor is real for the contraction | **CONFIRMED as an upper bound** (ROW^{(0)}); its attainment (ARGUED there) **NOT-VERIFIED**, not needed | 2.2 (c) |
| O2 | KFACTOR_O55 §5 (b): 𝔐^∇'s residual exponent 2 is one power below what responses deliver | **CONFIRMED** | 4.2 (1) |
| O3 | KFACTOR_O55 §5 (d): Proposition ROW♯ (second order) | **CONFIRMED** | 2.2 (a) |
| O4 | KFACTOR_O55 §5 (e): Proposition TW | **CONFIRMED** (top input now TOP♯) | 4.2 (1) |
| O5 | KFACTOR_O55 §5 (f): inclusions | **CONFIRMED** (needs θ ≤ σ) | 1.2 |
| O6 | KFACTOR_O55 §5 (g): "In this pair the plain-row level sum is k-uniform; the level-count factor occurs nowhere" | **CONFIRMED**; the reduction it is part of is **SUPERSEDED** (no off-critical input needed) | 3.4-3.5 |
| O7 | KFACTOR_O55 §5 (i): "The exact missing object … the ♯-weighted residual pairing … of Proposition NCR" | **REFUTED** as the missing object | 3.1, §5.7 |
| O8 | KFACTOR_O55 Remark TOP-crit | **CONFIRMED and upgraded** to PROVEN-as-implication (TOP♯) | 4.1 |
| O9 | KFACTOR_O55 §5 (h): no carrier input is the missing object | **CONFIRMED** (spot-check: CCP uses none) | 3.4 |
| O10 | REVIEW55_TUNIF W5 (a): requirement θ_w^r > 2 strictly | **CONFIRMED** | 4.6 |
| O11 | REVIEW55_TUNIF W4 / THETAW (1b): θ_w^r = 3 data-only, 2 + θ with residual-type sources | **CONFIRMED with a precision** (2 + θ_R; θ_R = 1 admissible) | 4.2 (1) |
| O12 | REVIEW55_TUNIF W6: (1c) relative to the holonomy-carrying centre / data size | **CONFIRMED**, adopted | 1.4 |
| O13 | NORMS §N7: A = L^{d−θ_w^r−2θ_A}, A < 1 ⟺ θ_w^r + 2θ_A > d | **CONFIRMED**; equals the row ratio iff θ_A = 1 | 4.6 |
| O14 | BFT_B §31.3 / §36.5 (ii): off-critical (NC-Γ) for Γ_E reduces to TENT-Q + NEUT-box, OPEN | **CONFIRMED** for the Feynman/Γ_E route; off BFT-0's path | 3.1-3.2 |
| O15 | REVIEW_BFT_B_S9_S10: the contraction needs the estimate at non-critical iterates (the OPEN half) | **CONFIRMED** for the Feynman map; false for Φ̃_Γ | 3.4 |
| O16 | REVIEW_BFT_A_S8 "biggest live wall" Q1 and "the remainder bound it needs is written nowhere" | **answered**: no non-cc sources needed; the bound is Proposition CB | 3.6 |
| O17 | BFT_A §3.11: (G♯_0-field^∇) OPEN | **CONFIRMED** (still open; it is (GV^{(σ)})_Γ restricted to cc sources) | 4.4 |
| O18 | HANDOFF item 5: the factor k is "UPSTREAM of (TENT-Q), (NEUT-box) and (Y-sup^loc) … attack the factor k first" | **REFUTED** (factor absent for σ > 0; those items are off BFT-0's path) | §8 |
| C1 | CODEX_REVIEW_TR, all six banked items, incl. §3/item 5 NOT-VERIFIED | **AGREE**; item 5 narrowed to (LA) by N17 (to be reviewed) | §5.5 |
| C2 | CODEX_REVIEW_C2 items 1 and 4 ((C2-COF); CD root-pinned, (CC-0) refuted) | **AGREE** | §5.2-5.3, §5.6 |

**Counts over the claims of others (O1-O18):** CONFIRMED 14 (O1 as a bound, O2, O3, O4, O5, O6 sentence, O8, O9, O10, O11, O12,
O13, O14, O15, O17 — counting O6 and O17 once each: 14 with O16 excluded), REFUTED 2 (O7, O18), NOT-VERIFIED 1 (O1's
attainment clause), answered/superseded 1 (O16). Codex verdicts used: 2 files, AGREE with both.

*Errata to §8 and §2.1 (self-check after writing the table).* (1) The CONFIRMED count over O1-O18 is **15** (O1 as a bound,
O2, O3, O4, O5, O6's sentence, O8, O9, O10, O11, O12, O13, O14, O15, O17), not "14": totals are CONFIRMED 15 / REFUTED 2
(O7, O18) / NOT-VERIFIED 1 (O1's attainment clause, a split row counted under its first verdict) / answered 1 (O16).
(2) **Symbol collision (systemic defect 1) inside this file:** §2.1's soft term "σ_c := κ_lφ̂(M, V)" collides with the weight
parameter σ of §1.2 (and the lane's S4' order index in "avg_{σ,y}"). Read the soft term as **𝔰_c**; every other σ in this
file is the weight parameter.

---

## §9. For the lead (written 2026-10-29T00:55Z UTC)

**Bottom line.** The off-critical half is now a theorem modulo one PRE-EXISTING input, and the "off-critical remainder" is not
that input. (a) In the transport-weighted family 𝔐^{(σ)} (residual weight θ_w^r = 2 + σ; σ = 1 is the weight 3 NORMS and
[S24-fix 3] ask for), every BCH₂ row — and, by the exact factorisation Lemma SG, every soft plain row at every order — carries
L^{−σ(k−1−l)}: Σ_lπ_l ≤ [36 + A_B/(1 − L^{−σ})]η², Lipschitz likewise; the level-count factor is exactly the σ = 0 endpoint
(𝔐^∇). A = L^{4−θ_w^r−2θ_A} = L^{−σ} with the delivered (2, 2 + σ, 1); = 1/3 at σ = 1. (b) The lane's off-critical remainder
is, exactly, the response to the correction Γ^TD^⊥(S) of a non-composite-co-closed source (Lemma OC, generalising Lemma GE (c)
and GT-split). On the lane's Feynman/Γ_E route it cannot be bounded with present inputs at any σ — it needs (NEUT-box) plus a
k-uniform n⁴||D^⊥|| bound, or (GT-sup) ⟸ (Y-sup^loc). (c) **It is not needed.** The cc-projected iteration
Φ̃_Γ(x) = x − 𝓛_Γ^{-1}(M_x∇F + Γ^TΓx), M_x = 1 − P^T(K'^T_x·)^⊥ with P^T a hierarchical (level-by-level) routing of the off-root
composite divergence, (i) feeds 𝓛_Γ^{-1} only composite-co-closed sources (so every iterate is in the slice and every
gauge-invariant output is given by the banked cc theory: TW, (C2-COF), LIN0), (ii) has exactly the slice critical points as
fixed points (via the banked root-pinned Lemma CD and an explicit bound ||P^TK'^T_x||_{J→J} ≤ 2dc_BernL^{d−1}η' — this replaces
Lemma CD (ii)'s nonlinear Faddeev-Popov hypothesis), and (iii) costs a correction bounded k- and T-uniformly in the σ-ball
(Proposition CB; ≍ k² at σ = 0). It is the Feynman iteration of the multiscale axial gauge Γ_hier = −P, re-projected into any
slice. (d) **Theorem K^{(σ)}: the composite contraction closes with k-, T-independent radius and threshold, given
(GV^{(σ)})_Γ** — the gauge-variant half (potentials and their coarse C^{1,α}) of the linear estimate for cc sources in one
slice, i.e. BFT_A §3.11's (G♯_0-field^∇), OPEN since session 1 and unrelated to the level count — plus, beyond second order,
the local analytic constants (LA). Potentials (θ_A = 1) are delivered in the tent-axial slice by LR-pot; the known LR-grad
obstruction is defused at σ ≥ α (ARGUED); gradients remain open. Bonus: Lemma TOP♯ proves KFACTOR_O55's ARGUED Remark
TOP-crit (top residual of cc responses ≤ C·N, T ≥ 3), supplying the top-response term that the banked (C2-COF) Hölder line
keeps; Corollary SG-TR narrows CODEX_REVIEW_TR's NOT-VERIFIED item 5 (full nonlinear Lemma TR) to the constants (LA).

**Counts (claims of others, §8 O1-O18): CONFIRMED 15 / NOT-VERIFIED 1 / REFUTED 2** (+1 answered: O16). New results
(N1-N17): PROVEN-HERE 5 (SG identity, OC, HR, CCP, Γ_hier reading), PROVEN 3 at second order (ROW^{(σ)} (a), CB, exponent
arithmetic), PROVEN as implications 5 (TOP♯, LIN^{(σ)}, potentials in Γ_tent, Theorem K given (GV), N3/N17 given (LA)),
ARGUED 2 (Γ_tent gradient failure; LR-grad obstruction defused), status statement 1 (N5). Check ko55_1: OVERALL PASS
(criteria and one pre-script amendment before the script; limits stated in §7).

**Every REFUTED item, with its correction.**
1. KFACTOR_O55 §5 (i), "The exact missing object, for the next worker … Proposition TW off the critical set, i.e. the ♯-weighted
   residual pairing ⟨D(S), λ^Γ_*⟩ of Proposition NCR" → on the Feynman route the curvature half of the same remainder is
   equally missing (BFT_B §36.5 (ii)); and on the cc-projected route neither half is needed: the missing object for the
   contraction is (GV^{(σ)})_Γ.
2. HANDOFF item 5, "The level-count factor k, which is UPSTREAM of (TENT-Q), (NEUT-box) and (Y-sup^loc) … attack the factor k
   first" → for σ > 0 the factor does not occur in the contraction (ROW^{(σ)}, CB) and is removed at critical points (Lemma TR;
   KFACTOR_O55); (TENT-Q), (NEUT-box), (Y-sup^loc), (GT-sup) are not on BFT-0's path (CCP).

**What should change in HANDOFF's critical path (pending a Codex review of this file — attack order in §6.5).**
- HANDOFF item 5 → *"Level-count factor: removed at critical points (Lemma TR, KFACTOR_O55; full nonlinear source given (LA),
  KFACTOR_OFF55 Corollary SG-TR) and in the contraction by the transport-weighted pair 𝔐^{(σ)}, σ ∈ (0, 1] (A = L^{−σ}, 1/3 at
  σ = 1). The contraction is run as the cc-projected iteration Φ̃_Γ (KFACTOR_OFF55 §3.4), which meets only composite-co-closed
  sources, so the off-critical (NC-Γ) remainder — (TENT-Q)/(NEUT-box)/(GT-sup)/(Y-sup^loc) — is off BFT-0's path. BFT-0/1/2 on
  𝒞_glob (trivial background, T ≥ 3) then rest on (GV^{(σ)})_Γ = (G♯_0-field^∇) for cc sources in one slice [OPEN], plus (LA)."*
- The (NC-Γ)-off-critical items stay on the list only for statements about Feynman-gauge responses to general sources (BFT-5 as
  worded in BFT_B §27.5).
- **PROOF.md tally: no change** (all lane-level). PROOF.md's BFT bookkeeping could record: "COMP's (CL-2) in 𝔐^{(σ)} for the
  cc-projected map: sources PROVEN at second order (KFACTOR_OFF55 ROW^{(σ)}, CB); linear half for cc sources: invariant PROVEN as
  an implication (LIN^{(σ)}), gauge-variant OPEN ((GV^{(σ)})_Γ)."

**Codex verdicts used.** CODEX_REVIEW_TR (complete; 23:51:15 UTC): **AGREE** with all six banked items; its item 5 NOT-VERIFIED
stands until Corollary SG-TR is reviewed. CODEX_REVIEW_C2 items 1 ((C2-COF) whole-class, top term retained) and 4 ((CC-0)
refuted; CD root-pinned): **AGREE**; used exactly in those forms.

---

## §10. Final errata and provenance (appended after a full re-read of §0-§9)

1. **Header times.** The times in the headings of §0 ("00:30Z"), §8 ("00:50Z") and §9 ("00:55Z") were written ahead of the
   clock and are wrong. Actual order (UTC, 2026-10-29): PRE-STATED 2026-10-28T23:40Z; criteria 00:22:05Z (amendment 00:22:52Z);
   script 00:24:30Z; run 00:24:39-40Z; §0-§9 appended between ≈00:26Z and 00:41:04Z (the `date` at the end of §9's append);
   this §10 after that. The authoritative time is the file's final `stat`.
2. **CCP (a), self-contained.** "Φ̃_Γ(x) ∈ Ker Γ and HΦ̃_Γ(x) = S̃(x)" is the one-line argument of BFT_B §29.4 (stated there as
   following from Lemma FG (iii)): for x := 𝓛_Γ^{-1}S with S cc and every λ ∈ Λ_0, ⟨Γx, ΓΞλ⟩ = ⟨𝓛_Γx, Ξλ⟩ − ⟨Hx, Ξλ⟩ =
   ⟨S, Ξλ⟩ − 0 = 0, and ΓΞ maps Λ_0 onto Ran Γ, so Γx = 0 and Hx = S.
3. **Scope of "PROVEN-HERE".** Lemma HR, Lemma OC, Proposition CCP and the identity of Lemma SG are complete written proofs in
   this file, unreviewed; ko55_1 checks HR (i)-(iv) exactly on finite lattices only (d ∈ {2, 4}, k ≤ 4 for the identity), which
   is evidence, not a proof for all k.
4. **No repository file other than KFACTOR_OFF55.md and checks/ko55_1_{criteria.md, .py, out.txt, err.txt} was written by
   this worker; no git command was run.**

## §11. Addendum — two files that appeared while I worked (read after §0-§10 were written)

- **CODEX_REVIEW_TOPCC.md** (Codex review of COFUN_CC.md; PRE-STATED 23:45:02 UTC; file complete through "Exactly what may be
  banked"). It **CONFIRMS** COFUN_CC's **Lemma TOP-cc** ("‖r^c_{k−1}(S)‖_∞ ≤ C_top^cc·N(S)" for every Setting LIN^cc source,
  m = 0, trivial background) as an implication of the lane-A inputs ("TOP-cc supplies the formerly missing top bound"). My
  Lemma TOP♯ (4.1) is the same statement proved by a shorter route (each level's plain current paired with the level-l
  component of the tent-axial representative, bounded by Corollary FP), whereas TOP-cc pairs the co-closed level-0 image with
  the 𝒩-minimal representative and the rest through residual pairings. **I AGREE with Codex TOPCC's verdict on TOP-cc**; the
  two proofs corroborate each other, and §5 item 2's caveat ("to be reviewed") is lifted to: the Hölder top term is supplied
  by the CONFIRMED Lemma TOP-cc (and independently by TOP♯). Codex TOPCC also repeats CODEX_REVIEW_TR's NOT-VERIFIED for the
  full nonlinear source ("Even a separate bound of order η³ per level would not by itself give a k-uniform level sum at fixed
  η") — I agree; Lemma SG is my structural answer (every soft plain row is linear in Θ ≈ ρ, so it inherits the residual's
  level decay at every order), pending the constants (LA) and a review. Its REFUTED item (axial-order dependence of source
  responses is not confined to root charges) does not touch this file: Lemma HR uses one fixed coordinate order and claims no
  order independence.
- **HIGHER55.md** (another Opus 5.5 worker, started 2026-10-29T00:15:57Z; only its PRE-STATED existed when read) targets
  exactly CODEX_REVIEW_TR item 5 / CODEX_REVIEW_TOPCC item 4, and its T3 asks "whether the higher-order terms carry
  level-to-level decay". **Lemma SG (§2.1) and Corollary SG-TR (§5 item 5) answer T3 structurally: yes, through the exact
  factor Θ_c = e^{ρ_c} − 1 in every soft gradient row; the per-level O(η³) worry does not arise.** The two files were not
  coordinated; the lead may want HIGHER55 to check Lemma SG rather than re-derive it.
