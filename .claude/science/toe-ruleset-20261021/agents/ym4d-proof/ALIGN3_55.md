Reviewer model: claude-opus-5-5

# ALIGN3_55 — finishing the background transfer (R2) in the log chart (worker file, Opus 5.5)

UTC start: 2026-10-29 06:12 (from `date -u`).
Role: worker (not reviewer); the shared rules of REVIEW_BRIEF_55.md apply. Writes only this file and `checks/a3_55_*`.

## PRE-STATED (written before any derivation)

Targets, in the brief's order:
- T1. A periodic (torus) harmonic/path alignment whose completion identity holds, with constant
  fields handled correctly (must explain/avoid Codex's |M(1)| >= 1/153 obstruction on nine coarse knots).
- T2. Full periodic (P2-tw)_log.
- T3. (AC)_log: the gauge-generator bound in the log chart.
- T4. A restricted source-infimum: state and prove the restricted representation cost the consumers need.
- T5. Covariant output conversions: log-chart flat-sharp -> N pair to the norms BFT-5 clause (b)'s
  consumers read, in DICT55's conventions.
- T6. Assemble (R2) on C_glob as an implication with every input named and its status.

What counts as a refutation / negative result (each is first-class):
- R-T1: an explicit periodic configuration (exact rationals) where every admissible choice in the stated
  class violates the completion identity, or where constants cannot be both reproduced and annihilated
  as the identity requires.
- R-T2: a periodic field for which the claimed (P2-tw)_log inequality fails at the stated constant, or a
  missing term (zero-mode / holonomy / twist) that the bound cannot absorb.
- R-T3: a gauge generator whose log-chart norm exceeds the claimed bound, or a chart/currency mismatch.
- R-T4: a source for which the restricted cost is not attained/finite, or a consumer that needs the
  unrestricted infimum.
- R-T5: a conversion that runs in the wrong direction, loses a factor not tracked, or reads a norm
  different from the one DICT55 pins.
- R-T6: any input of (R2) that is unnamed, REFUTED, or circular.
A claim I cannot settle is NOT-VERIFIED with what is missing stated; nothing here is banked until Codex checks it.

---

# FINDINGS (appended from 2026-10-29T06:3xZ; everything below was written after the PRE-STATED block)

## 0. Read record, inputs, symbol pins

**Read (located by string; line numbers as on disk 06:12-06:35Z).** REVIEW_BRIEF_55.md and the task brief (queue/align3.md) in full;
ALIGN2_55.md in full (737 lines; last line "UTC stamp of this erratum: 2026-10-29T05:27Z" — complete); CODEX_REVIEW_ALIGN2.md in full (328 lines;
last line "Closing UTC: 2026-10-29T05:58:43+00:00" — complete, ends with "Exactly what may be banked"); ALIGN55.md §1-§2 (l.65-139), §4
(l.204-243), §5.4-§6 (l.292-395); CODEX_REVIEW_ALIGN.md PRE-STATED, F1-F3 and "Exactly what may be banked" (l.245-252); BGT55.md §2
(l.73-136), §6.1-§6.3 (l.317-366); CODEX_REVIEW_BGT.md "Exactly what may be banked" (l.387-395); DICT55.md §1 C1-C10, §2 O1-O3, O6-O15
(l.94-300, 368-520), FL2-FL6 (l.684-730), §12 (l.1191-1234); REVIEW_S22.md l.385-433 (the BFT statement); SF.md §6.2 (l.676-725);
PROOF.md "Proposition B-NA-red" (l.3425-3480); BFT_A.md §7.2 (l.452-475), BL-6 (l.528-540, 680-730); BFT_B.md §12.0 (l.1586-1608), §15.0
(l.2015-2045); checks/a2_55_lp.py l.1-120 (the s3 mask and the model's stencil-with-own-path implementation). No arXiv paper was needed.

**Symbol pins (systemic defect 1).** As ALIGN2_55 §0, plus:
- **Λ_*** = level-0 su(N)-functions vanishing at the level-k roots (KFACTOR_OFF55/DICT55 O7 canonical); never Λ_0.
- **K_ȳ = −Ξ_1 + K′_ȳ** the log-chart gauge generator at ȳ (DICT55 C4: K_0 = −Ξ). **K′** never denotes a detail kernel here.
- **𝒥 := ψ_−(ad_ȳ)** link-wise, left-trivialised → log (ALIGN2 §2.2's convention, which Codex ALIGN2 F4 pins): **S = 𝒥^T f, f = 𝒥^{−T}S,
  Ξ_Z = −𝒥^{−1}K_ȳ** (Codex F4's corrected directions; ALIGN2's "S = J^{−T}f" and "Ξ_Z = ∓JK" are NOT used).
- **r_j(x) := Q x_j − x_{j+1}** (DICT55 C2; Q = Q_root, the S4′ contour average, DICT55 O1). **B** below denotes Q_root acting on level-m 1-forms
  when it appears inside an operator identity (Codex ALIGN2 F10's "B_m"); the charge vector is written **q_m** (F10's split of ALIGN2's "Q_m").
- **N_1(f)** := inf over flat (log-chart) slot representations ℛ of f of N_ℛ(f), N_ℛ = COFUN_CC's N-expression with ‖G‖_Y over ALL levels
  (ω_0 = 1, ω_l = L^{θ(k−l)}), ‖j^c_0‖_∞, ‖j‖_Pc = max_{l≥1}L^{θ(k−l)}π_l(j_l), ‖s‖_R = max_l L^{θ(k−l)}L^{k−1−l}‖s^c_l‖_∞ (DICT55 O11; ALIGN55 §1).
  **N_0(f)** (new, §4) := the same infimum restricted to representations with G_l = 0 for l ≥ 1. **N^{(σ)}** = KFACTOR_OFF55's (DICT55 O11).
- **|||·|||_{1,♯}** = ‖·‖_{𝔐^∇} + max_{i≤k−2}L^{(1+θ)(k−1−i)}‖r^c_i‖_∞ + N_res (BGT55 §6.2, banked RW♯ pair); **[u]_{1,♯}** := inf over Ran Ξ_1;
  **[u]_{ȳ,♯}** (new) := inf_{μ∈Λ_*}|||u + K_ȳμ|||_{1,♯} — the flat ♯ norm of the log-chart orbit at ȳ. **‖μ‖_𝒞** = ALIGN55 §4's C^{1,θ} gauge norm.
- **C_CV** (ALIGN2 §1.4) is the P_cc-completion constant only; the chart constants are **C_NC, C_SC** here (Codex F11's split; "C_SC" replaces
  ALIGN2's chart use of "C_CV").
- **h, q**: q := k − 1 − l (depth); ρ_l := L^{−(k−l)} (mesh). Codex F8's "h" = ρ_l. **ρ_l(ȳ)** (the background's soft residual) is always
  written with its argument.
- **The torus side T** (coarse units, level k) is never a transpose; transposes are ^T on operators only. Level-l side N_l := T·L^{k−l}.

## 1. Item (1) — the periodic harmonic/path repair: Λ_LP by the method of images. PROVEN-HERE

### 1.1 Diagnosis of Codex ALIGN2 F5/F10 (agree), and what it actually forbids
Codex F5's supplement: with periodic weights a^per(y,Y) **merged per periodic node** and **one lattice path per node**, M(1) = (3960 + 27Σa_jn_j)/1377 ≠ 0
on nine coarse knots (3960 ≡ 18 mod 27), so dM(1) ≠ 0 and the factorisation dM = 1 − S_1Q + Ñd is impossible. I agree (re-derived in §1.6, Part I).
The obstruction is **integrality**: any path-average operator on the torus has the form Mx(y) = Σ_Y⟨c_{y,Y}, x⟩ with c_{y,Y} a real 1-chain,
∂c_{y,Y} = a^per(y,Y)([y] − [Y]). The left-inverse identity Md = 1 − S_0R only sees the boundaries, so it holds for every such choice. On a constant
ν-form, M(const_ν)(y) = Σ_Y w_ν(c_{y,Y}), w_ν the real ν-winding (homology class) of the chain. **"M kills constants" is d real linear conditions per y.**
With one lattice path per node, w_ν(c_{y,Y}) ∈ a^per(y,Y)·(displacement + N_lℤ): Codex's residue argument shows the conditions can fail. With real
chains they are always solvable, and the infinite-lattice operator supplies a canonical solution: **keep every image of every coarse node with its
own lifted path** (the "unmerged lifted weights with separate winding paths" Codex F5 names as possibly changing the construction).

### 1.2 Definition PER (method of images)
Infinite-lattice data (level l, own units, level-l sites ℤ^d, level-(l+1) sites Lℤ^d = block centres, Convention C): s an interpolatory L-adic
scheme of Construction CP (BFT_B §15.0: finite or exponentially decaying mask, constants reproduced), here reproducing polynomials of degree ≤ p = 3
per coordinate; S_0^∞ := s^{⊗d} with weights a(y,Y); S_1^∞ := CP's derived tensor scheme (dS_0^∞ = S_1^∞d); B^∞ := Q_root (the order-paired centred
S4′ contour average, DICT55 O1/C3; finite range; B^∞d = dR, B^∞(const_μ) = L·const_μ); axial paths γ(Y→y) in the fixed coordinate order 1, …, d;
  **M^∞x(y) := Σ_{Y∈Lℤ^d} a(y,Y)∫_{γ(Y→y)}x.**
(KD) decay: |a(y,Y)| ≤ A_0e^{−κ_s|y−Y|_∞} — trivially for the finite s3 mask (ALIGN55 §5.4; support |y−Y|_∞ ≤ 5 at L = 3, read from a2_55_lp.py's
table S3), and with κ_s = ln(2+√3)/L for the cubic spline (cardinal coefficients c_i = √3(√3−2)^{|i|}, ALIGN2 §2.6, Codex F5 CONFIRMED).
Torus Λ_l = (ℤ/N_lℤ)^d, N_l = TL^{k−l} (a multiple of L for l < k). For an Lℤ^d-covariant kernel K^∞ with (KD)-type decay, its **periodisation**
K^per(y, y′) := Σ_{n∈ℤ^d}K^∞(ŷ, ŷ′ + N_ln). Put **M_l := (M^∞)^per, S_0 := (S_0^∞)^per, S_1 := (S_1^∞)^per, B := (B^∞)^per**, and
**Λ_LP^img x := λ_0, λ_k := 0, λ_l := S_0λ_{l+1} − M_lx_l** (ALIGN2 §2.4's recursion with M_l replaced).
For the spline, S_0 is exactly ALIGN2's periodic cubic-spline subdivision (the cardinal interpolant of periodic data is a periodic cubic spline with
the same samples; periodic spline interpolation is unique — circulant (1,4,1)/6, eigenvalues ≥ 1/3; Codex F5 CONFIRMED). For s3, a2_55_lp.py's
Model.M already keeps one relative path per stencil entry, i.e. it **is** the image construction (each stencil offset o is a lift with its own path).
**Only the merged single-path spline M of ALIGN2 §2.4/§2.6 is replaced.**

> **Lemma PER-1 (images).** For Lℤ^d-covariant kernels with (KD)-type decay: (i) K^per acting on torus fields equals K^∞ acting on their periodic
> lifts; (ii) (K_1K_2)^per = K_1^perK_2^per, (dK)^per = dK^per, (Kd)^per = K^perd; (iii) every ℓ¹ row or column sum of K^per is ≤ the corresponding
> sum of K^∞ — so every constant below is independent of T and k; (iv) a finite-range K^∞ gives K^per supported within the same torus distance.
*Proof.* (i) absolute convergence and N_lℤ^d ⊂ Lℤ^d-invariance; (ii) from (i) (composition of lifts is the lift of the composition; d is local and
translation-invariant); (iii) |Σ_nK^∞(ŷ, ŷ′ + N_ln)| ≤ Σ_n|K^∞(ŷ, ŷ′ + N_ln)| and the images of distinct ŷ′ are distinct; (iv) definition. ∎

> **Lemma PER-2 (the periodic path average).** For every k, T and l < k:
> (a) M_ld = 1 − S_0R on level-l functions; (b) M_lx vanishes at level-(l+1) sites and RS_0 = 1, so ev^{(l)}Λ_LP^img x = λ_l, Λ_LP^img x ∈ Λ_*, (H)
>   holds, and **Λ_LP^imgΞ_1 = −1** (ALIGN2 LP-1 (ii)-(iv) verbatim); transpose level-locality c_m = −M_m^TS^{(m→0)T}q, M_m^TR^T = 0 (LP-1 (v));
> (c) **M_l annihilates every constant 1-form** (every harmonic 1-form of the torus);
> (d) in d = 1, **M_l = M^{merged}∘(1 − h)** for every single-path choice M^{merged}, h(x) := the constant form with the mean of x;
> (e) **sup|M_lx_l| ≤ C_D·ρ_{l+1}^{2+α}·(‖∇^cx^c_l‖_∞ + [∇^cx^c_l]^∞_α), C_D := 2L^{−(2+α)}m_{2+α}, m_β := sup_yΣ_Y|a(y,Y)||y − Y|_1^β** (finite: s3 a
>   finite sum; spline by (KD)); with BL-C ([·]^∞_α ≤ C_C[·]_α + 2·8^α‖·‖_∞) this is ≤ C′_Dρ_{l+1}^{2+α}‖x‖_{𝔐^∇}, C′_D := C_D(1 + C_C + 2·8^α).
*Proof.* (a) On ℤ^d, ∫_γdν = ν(y) − ν(Y) for any path and Σ_Ya(y,Y) = 1, so M^∞dν̂ = (1 − S_0^∞R)ν̂; lift (PER-1 (i)). (b) a(y,·) = δ_y at coarse y
(interpolatory) and γ(y→y) is empty; the rest is ALIGN2 LP-1's one-line proofs, which use only (a), (b) (Codex F2 CONFIRMED that algebra).
(c) On ℤ^d, M^∞ of the constant ν-form c is c·Σ_Ya(y,Y)(y − Y)_ν = c(y_ν − Σ_Ya(y,Y)Y_ν) = 0 by linear reproduction (absolutely convergent by (KD));
lift. (d) M_l − M^{merged} vanishes on exact forms by (a) for both; M_l kills constants by (c); Ω¹(T¹) = dΩ⁰ ⊕ ℝ·1. Hence M_l − M^{merged} =
(M_l − M^{merged})∘h = −M^{merged}∘h. (e) M_lx(y) = M^∞x̂(ŷ) = Σ_Ŷa(ŷ,Ŷ)∫_{γ(Ŷ→ŷ)}(x̂ − P_ŷ), P_ŷ the affine Taylor 1-form of x̂ at ŷ (a polynomial 1-form
of degree ≤ 1 ≤ p − 1 on ℤ^d, killed by M^∞: ALIGN2 LP-2 (a), Codex F2 CONFIRMED). Own units: x = ρ_lx^c and an own difference over one step is
ρ_l²∇^cx^c, so a link at ℓ¹ distance D from ŷ has |x̂ − P_ŷ| ≤ ρ_l²D·ω(Dρ_l), ω(s) := the oscillation of ∇^cx^c over coarse ℓ¹ separation s, ≤ s^α[∇^cx^c]^∞_α
for s ≤ 1 (ℓ^∞ ≤ ℓ¹), ≤ 2‖∇^cx^c‖_∞ for s > 1. A path of D_Y := |ŷ − Ŷ|_1 links therefore contributes ≤ ρ_l²D_Y²ω(D_Yρ_l), and for D_Y > ρ_l^{−1} one has
1 < (D_Yρ_l)^α, so |M_lx(y)| ≤ ρ_l^{2+α}m_{2+α}([∇^cx^c]^∞_α + 2‖∇^cx^c‖_∞) and ρ_l = L^{−1}ρ_{l+1}. ∎
**Remark (why (e) needs the sup term).** Codex F5's witness has zero gradient seminorm and non-zero merged detail; with images, (c) kills it. The
pointwise seminorm of the lane is defined only at coarse separations ≤ 1 (BFT_A §7.2), so the Taylor tail beyond coarse distance 1 (present for s3 at
the top two levels and for the spline at every level, exponentially small) is paid by ‖∇^cx^c‖_∞ — a component of 𝔐^∇. ALIGN2 LP-2 (b)'s
seminorm-only display is therefore replaced by (e); on the infinite lattice with a global seminorm the two agree.

### 1.3 The completion identity on the torus (the identity Codex F10 refuted for the merged operator)
> **Lemma PER-3 (local Stokes filling).** Put E^∞ := dM^∞ − 1 + S_1^∞B^∞ on level-m 1-forms of ℤ^d, and for a link b let Z_b := Σ_eE^∞(b,e)·e (the
> b-row of E^∞ as a 1-chain). Then (i) ∂Z_b = 0; (ii) with p_b := tail of b and the **axial ladder** strip(e, p) (the ≤ |tail(e) − p|_1 plaquettes, signs
> ±1, between the axial path from p to tail(e) and its e-translate beyond the switch coordinate, so that ∂strip(e,p) = γ(p→tail e) + e − γ(p→head e)),
> the 2-chain **F_b := Σ_eZ_b(e)·strip(e, p_b)** has ∂F_b = Z_b and |F_b(P)| ≤ Σ{|Z_b(e)| : |e − p_b|_∞ ≥ |P − p_b|_∞ − 1}; (iii) with
> **Ñ^∞(b, P) := F_b(P)** one has **E^∞ = Ñ^∞d** on 1-forms of at most polynomial growth, and, periodising (PER-1),
>   **dM_m = 1 − S_1B + Ñ_md on the torus, Ñ_m := (Ñ^∞)^per,**
> with Ñ^∞ finite-range for s3 and (KD)-decaying for the spline; **A_Ñ := sup_PΣ_b|Ñ_m(b,P)| ≤ dL^d·sup_bΣ_e|Z_b(e)||tail(e) − p_b|_1 < ∞**, k-, T-uniform.
*Proof.* (i) Transposing (a) on ℤ^d gives ∂M^{∞T} = 1 − R^TS_0^{∞T} on 0-chains; Bd = dR and dS_0 = S_1d give ∂B^{∞T} = R^T∂ and ∂S_1^{∞T} = S_0^{∞T}∂.
So ∂E^{∞T} = (1 − R^TS_0^{∞T})∂ − ∂ + R^TS_0^{∞T}∂ = 0 on (summable) 1-chains, and Z_b = E^{∞T}δ_b. (ii) The two axial paths from p to the ends of e
agree up to the switch coordinate ν of e; beyond it they run along translates of the same segment, so their difference with e closes a ladder,
filled by one plaquette per segment link. Then ∂F_b = Σ_eZ_b(e)(γ(p→t_e) + e − γ(p→h_e)) = Z_b − Γ_p(∂Z_b) = Z_b (Γ_p[z] := γ(p→z), linear).
The ladder of e lies in the bounding box of p and e. (iii) (E^∞x)(b) = ⟨Z_b, x⟩ = ⟨∂F_b, x⟩ = ⟨F_b, dx⟩ (convergent by the decay of F_b); periodise.
For A_Ñ group b into its dL^d classes mod Lℤ^d and use covariance F_{b+Lz}(P + Lz) = F_b(P). ∎
**What replaces Codex's harmonic premise.** No separate "E vanishes on harmonic forms" input is used: the chain identity (i) holds on the
contractible ℤ^d, and E_m(const) = 0 on the torus is then a consequence (it also follows directly from PER-2 (c) and S_1B(const) = const). For the
merged operator, E^{merged} − E_m = d(M^{merged} − M_m) does not vanish on constants (Codex F5), so no Ñ exists — consistent.
> **Corollary PER-4 (the divergence-completion identity, F10's conditional form now unconditional for Λ_LP^img).** For a level-l current w and
> w_l := w, w_{m+1} := S_1^Tw_m (m ≥ l), and every chain x with x_k = 0:
>   **⟨Λ_LP^{img,T}(ev^{(l)T}d^Tw), x⟩ = −⟨w, x_l⟩ + Σ_{m=l}^{k−1}⟨w_{m+1}, r_m(x)⟩ − Σ_{m=l}^{k−1}⟨Ñ_m^Tw_m, dx_m⟩,  r_m(x) = Bx_m − x_{m+1}.**
*Proof.* c_m = −M_m^TS^{(m→l)T}d^Tw = −M_m^Td^Tw_m (S_0^Td^T = d^TS_1^T) = −(dM_m)^Tw_m = −w_m + B^TS_1^Tw_m − d^TÑ_m^Tw_m; pair with x_m, sum over
m ≥ l and telescope Σ_m(−⟨w_m, x_m⟩ + ⟨w_{m+1}, Bx_m⟩) = −⟨w_l, x_l⟩ + Σ_m⟨w_{m+1}, Bx_m − x_{m+1}⟩ + ⟨w_k, x_k⟩, x_k = 0. (Codex F10's own algebra,
with its factorisation hypothesis now supplied by PER-3.) ∎

### 1.4 (P1′) on the torus — PROVEN for the spline instance
> **Proposition P1′(img).** Spline instance, every odd L ≥ 3, 0 < α < θ ≤ 1, every k ≥ 1, T ≥ 1: **‖Λ_LP^imgx‖_𝒞 ≤ C_𝒞‖x‖_{𝔐^∇} ≤ C_𝒞|||x|||_{1,♯}**,
> C_𝒞 := C′_D·max{A_0/(1 − L^{−(2+α)}), A_1L^{2+α}/(L^{1+α} − 1), L^{2+α}[dA_2/(1 − L^{−α}) + 2A_1/(1 − L^{−1−α})]}, (A_0, A_1, A_2) = (3^d, 6·3^{d−1}, 12·3^{d−1}).
*Proof.* λ_l = Σ_{m≥l}S^{(m→l)}μ_m with μ_m = −M_mx_m vanishing on level-(m+1) sites and |μ_m| ≤ C′_Dρ_{m+1}^{2+α}‖x‖_{𝔐^∇} (PER-2 (b), (e)); the
periodic spline HB with these amplitudes is Codex ALIGN2 F9's banked reconstruction ("HB reconstruction holds uniformly on infinite and periodic
lattices given its detail amplitudes, with the safe norm-specific constants in F9") — the three displayed constants are F9's. ∎
**Scope.** The s3 instance has PER-1..PER-4 and (e) (finite range), but its HB needs the compatible finite-level C^{1,θ} reconstruction bounds
(Codex F11 item 4) — **NOT-VERIFIED**; it is used below only for exact algebraic checks.
*Erratum to P1′(img) (immediately, on re-reading):* ‖·‖_𝒞 is the SUM sup + ∇ + [∇]_θ, so read **C_𝒞 := C′_D·[A_0/(1 − L^{−(2+α)}) +
A_1L^{2+α}/(L^{1+α} − 1) + L^{2+α}(dA_2/(1 − L^{−α}) + 2A_1/(1 − L^{−1−α}))]** (sum, not max). Nothing else changes.

### 1.5 Check a3_55_per (record)
Criteria `checks/a3_55_per_criteria.md` written 06:43:45Z, before the script `checks/a3_55_per.py` (written 06:44-06:48:46Z; two pre-run edits to the
script only: E made lazy, and II2's S_1B(const) evaluated as S_1(B(const)) instead of forming the matrix product — same quantity). **One run**,
06:48:46-06:48:55Z, `nice -n 10 python3 -I -B`, Fractions/ints only, 4.3 s, 198 MB (`checks/a3_55_per_out.txt`; `checks/a3_55_per_err.txt` = stamps +
/usr/bin/time). No criterion edited. **I0-I4 PASS; II1-II4 PASS; III1-III2 PASS; controls CI1, CI2, CF1-CF4, CIII1, CIII2 all FIRE; OVERALL PASS.**
What it decides:
- **I0** reproduces Codex F5 by independent arithmetic: the nine-knot row (1102, 521, −126, 34, −10, 6, −14, 50, −186)/1377, the five-knot row, and the
  merged shortest-path values −8/9 (3 knots), 40/99 (5 knots), **8/153** (9 knots; 1377·8/153 − 3960 = −3888 ∈ 27ℤ, consistent with F5's |M(1)| ≥ 1/153).
- **I1**: the image operator kills constants at every fine site for 3, 5, 9 knots — e.g. at y = 1, nine knots: Σ_Ja(y − 3J) = 3960/1377 and
  27·Σ_Jm_1(1,J) = 27·440/4131 = 3960/1377: **the image first moments cancel exactly the residue Codex's integrality argument isolates.**
- **I2-I4**: left inverse, the 1D completion identity dM − 1 + S_1B = 0 on every 1-form, and PER-2 (d) (M^img = M^merged∘(1 − h)) — exact;
  CI1: the merged operator violates the completion identity at 3, 5 and 9 knots (Codex F10's contradiction, reproduced); CI2: the n = 0 paths
  alone do not kill constants (the image moment term is what does it).
- **II1-II2** (d = 2, s3, tori of coarse side 3 and 5, fine sides 9, 15, 27, 45; the side-9 level wraps the stencil): M(const) = 0, Md = 1 − S_0R,
  Bd = dR, dS_0 = S_1d, S_1B(const) = const, as exact matrix identities.
- **II3** (PER-3): the rows Z_b of E^∞ (built on ℤ², no torus) are cycles for all 18 link classes; their fillings F_b are exact with ℓ^∞ radius 6
  about the link; and the torus matrix E_torus = d0·M − 1 + S_1·B, **built independently from the torus operators**, equals the periodised Ñ·d1
  entrywise at fine sides 9 (wrapping), 27 and 15. CF4: a non-derived S_1 destroys the cycle property.
- **II4** (PER-4): the hierarchical divergence-completion identity holds exactly (k = 2, T = 3, l = 0, 1, three seeds); CF3: without the Ñ term it fails.
- **CF1/CF2**: the merged operator on the wrapping torus neither kills constants nor admits Ñ — Codex's obstruction in d = 2.
- **III1-III2** (the CEN2 core of §3's LA-pol): for constant fields in a step-3 nilpotent algebra, the order-paired centred S4′-type average has
  **no quadratic term** (log M̄ = 3tA_0 + O(t³)) and the quadratic term of log(e^{−V}M̄) is −½[V_1, c_1 − V_1], zero at zero mismatch; CIII1/CIII2:
  lower-corner offsets or a single contour leave a quadratic term (the cancellation is forced by centring + averaging, not automatic).
*Cannot decide* (stated before running): d = 4; any norm or uniform constant (A_Ñ, C_D, C_𝒞); the spline in d ≥ 2; the LA-pol inequality itself;
su(N) beyond the universal nilpotent algebra; the W_0 projection; weights.

### 1.6 Verdict on item (1)
**The periodic harmonic/path repair exists and is proven (PER-1..PER-4, P1′(img)):** keep every image of every coarse node with its own lifted
path. Then M kills all torus harmonic 1-forms, the left inverse and hierarchy are unchanged, the detail bound holds on the torus with the sup of
the gradient added (PER-2 (e)), the completion identity dM = 1 − S_1B + Ñd holds with an explicit local Stokes filling (PER-3), and the
divergence-completion identity of ALIGN2 §2.5 (B) holds unconditionally (PER-4). **Codex F5/F10 stand as refutations of the merged single-path
operator; they do not extend to the image operator** (I1, I3, II3 exhibit the cancellation on Codex's own nine-knot data). No torus-size
restriction enters (PER-1 (iii)); T ≥ 1 suffices for the algebra.

## 2. Item (2) — full periodic (P2-tw)_log for Λ_LP^img. PROVEN as an implication, in the window α + θ ≤ 1

> **Theorem P2-tw(img).** d = 4, odd L ≥ 3, 0 < α < θ ≤ σ ≤ 1 with **α + θ ≤ 1** (lane A's own window "0 < α ≤ θ ≤ 1 − α", BFT_A §7.1; contains
> (α, θ) = (¼, ½)). Let ȳ ∈ Ker Γ_E be the BFT-E critical point on 𝒞_glob with η := ‖ȳ‖_{(σ)} ≤ η_tw, and Λ_W := Λ_LP^img (spline instance;
> s3 has the same algebra). For every log-chart source f with **K_ȳ^Tf = 0** and every flat representation ℛ = (G_l; j_l; s_l)_{l<k} of f
> (positive-level G_l allowed):
>   **N_1(Λ_W^Tτ′(f)) ≤ C_tw·η·N_ℛ(f)**, hence **N_1(Λ_W^Tτ′(f)) ≤ C_twη·N_1(f)**, τ′(f) := Ξ_1^Tf (= K′^T_ȳf),
> C_tw = C(d, L, α, θ, σ, A_M, A_1, C_{S1}, A_Ñ, C_Ψ, n_ov, C_ρ) — independent of k ≥ 1, T ≥ 1 and of the background beyond η.
**Constants (all column ℓ¹ sums, periodisation-stable by PER-1 (iii)).** A_M := sup_bΣ_y|M(y,b)| ≤ L^d·max_rΣ_Y|a(r,Y)||r − Y|_1; A_1 :=
sup_nL^{−dn}·(column sum of S_0^{(n)}) ≤ 3^d for the spline (S_0^{(n)} = samples of the cardinal interpolant by nesting, Σ_iB_3(i/N − s) = N by
Poisson summation since B̂_3(ξ) = (sin πξ/πξ)^4 vanishes at non-zero integers, Σ|c_j| = 3); C_{S1} := sup_nL^{−(d−1)n}·(column sum of S_1^{(n)})
≤ 3^d for the spline (direction-ν factor = the total variation of H(t) := Σ_{j≥1}L_card(t − j), and H′ = Σ_mc_{m−1}B_2(t − m + ½) gives TV(H) ≤ Σ|c| = 3;
the other d − 1 factors are A_1's); A_Ñ from PER-3. C_Ψ, n_ov: ALIGN2 §1.4 Step 4's local analytic constants (LA-loc), C_ρ: KFACTOR_OFF55 §1.4 (1b).

*Proof.* **Step 0 (the charge).** K_ȳ = −Ξ_1 + K′_ȳ and K_ȳ^Tf = 0 give τ′(f) = Ξ_1^Tf = K′^T_ȳf, i.e. τ′(f)(λ) = f(K′_ȳλ) for λ ∈ Λ_*, with the exact
log-chart generator (K′_ȳλ)_l(b) = −[ȳ_l(b), λ̄_l(b)] − ½Φ(ad_{ȳ_l(b)})dλ_l(b), λ_l = ev^{(l)}λ (ALIGN2 §1.4 Step 1; Codex ALIGN2 F7 CONFIRMED, "the
log-chart generator"). Own sizes from ‖ȳ‖_{(σ)} ≤ η (KFACTOR_OFF55 §1.4, Codex KOFF item 5): |ȳ_l| ≤ ρ_lη, |dȳ_l(P)| ≤ 2ρ_l²η, |ρ_l(ȳ)| ≤
L^{−(2+σ)q}(η + C_ρη²), ‖Φ(ad_{ȳ_l})‖ ≤ 0.68ρ_l²η² (η ≤ ½). Input sizes (own): |G_l| ≤ ρ_l²‖G^c_l‖ with ‖G^c_l‖ ≤ ω_l^{−1}N_ℛ; |j_l| = L^{−3(k−l)}π_l(j_l),
π_l ≤ L^{−θ(k−l)}N_ℛ (l ≥ 1), π_0 ≤ N_ℛ; |s_l| ≤ L^{−θ(q+1)−2q}‖s‖_R (q = k − 1 − l).
**Step 1 (exact charge decomposition, slot by slot).** Each slot of ℛ contributes point charges and level-wise divergences d^Tw:
| slot | point charges (own size a, sites) | divergence currents (own size, level) |
|---|---|---|
| G_l (every l) | −[G_l(P), dȳ_l(P)] at plaquette bases: a ≤ 2d(d−1)ρ_l⁴η‖G^c_l‖, level l | w_A^{(l)}: ≤ 4(d−1)ρ_l³η‖G^c_l‖; w_B^{(l)}: ≤ 0.7(d−1)ρ_l⁴η²‖G^c_l‖ (level l) |
| j_l | −½Σ_{b∋y}[j_l(b), ȳ_l(b)]: a ≤ 2dρ_lη|j_l|, level l | −½Φ(ad_{ȳ_l})^Tj_l: ≤ 0.34ρ_l²η²|j_l| (level l) |
| s_l | ±[ρ_l(ȳ), s_l] at level-(l+1) sites: a ≤ 2dL^{−(2+σ)q}(η + C_ρη²)|s_l|; second-order part: a ≤ 2n_ovC_ΨL^{−2q}η²|s_l| (levels l, l+1) | ω_l: ≤ n_ovC_ΨL^{−q}η|s_l| (level l); ω_{l+1}: ≤ C_ΨL^{−q}η|s_l| (level l+1) |
The G-row is ALIGN2 CONV-P Step 3 at level l (the algebra is level-blind; checked exactly at level 0 by a2_55_conv II, coefficient mass 2(d − 1));
the j-row is the λ̄-part of K′ (two endpoints, 2d links per site, |[A,B]| ≤ 2|A||B|); the s-row is CONV-P Step 4 (exact soft covariance
Dρ_l(ȳ)[K_ȳλ] = ±[λ(c_Y), ρ_l(ȳ)] — CODEX_REVIEW_BGT item 4 — plus LA-loc), as Codex F7 confirmed it.
**Step 2 (completion of a point charge).** For q of own size ≤ a on level-l′ sites, c_m = −M_m^TS^{(m→l′)T}q (m ≥ l′; PER-2 (b)), own |c_m| ≤
A_MA_1L^{4(m−l′)}a. Its plain cost at output level m (Pc weight L^{θ(k−m)}π_m; at m = 0 the P0 weight L^{3k} ≤ L^{(3+θ)k}) is ≤ L^{(3+θ)(k−m)}A_MA_1L^{4(m−l′)}a.
Inserting the table: G_l: ≤ 2d(d−1)A_MA_1·L^{−(1−θ)(k−m)}·η‖G^c_l‖; j_l: ≤ 2dA_MA_1·L^{−(1−θ)(k−m)}·ηπ_l(j_l); s_l (l′ = l+1): ≤ 2dA_MA_1(η + C_ρη²)
L^{−(1−θ)(k−m)}L^{−(σ+θ)q−θ}‖s‖_R, and its second-order part ≤ 2n_ovC_ΨA_MA_1L^{4}·L^{−(1−θ)(k−m)}L^{−θq}η²‖s‖_R. (Exponent bookkeeping: d = 4,
(3 + θ)(k − m) + 4(m − l′) − 4(k − l′) = −(1 − θ)(k − m).)
**Step 3 (completion of a divergence d^Tw at level l′)** — PER-4: the plain current −w at level l′, residual slots s′_m := w_{m+1}, curvature slots
G′_m := −Ñ_m^Tw_m (m = l′, …, k − 1), with own |w_m| ≤ C_{S1}L^{3(m−l′)}|w|, so (π := π_{l′}(w))
  plain: L^{θ(k−l′)}π (P0: π if l′ = 0);   R: ‖s′‖_R ≤ C_{S1}L^θ·max_mL^{−(1−θ)(k−1−m)}π ≤ C_{S1}L^θπ;
  Y: ‖G′^c_m‖_∞ ≤ A_ÑC_{S1}L^{−(k−m)}π, and the level-m Campanato seminorm ≤ ρ_m^{−α}‖G′^c_m‖_∞ (Osc_2 ≤ sup, boxes of side ≥ ρ_m), so
  **ω_m(‖G′^c_m‖ + [G′^c_m]_α) ≤ 2A_ÑC_{S1}L^{(θ+α−1)(k−m)}π** (m ≥ 1; ω_0 = 1 gives ≤ 2A_ÑC_{S1}L^{−(1−α)k}π at m = 0).
**Step 4 (sum).** Output slots are max over output levels of sums over input levels l ≤ m (and l′ ∈ {l, l+1}):
- point-charge plain costs: Σ_{l≤m}L^{−(1−θ)(k−m)}·(input slot at l) ≤ L^{−(1−θ)(k−m)}[(1 + (L^θ − 1)^{−1})(2d(d−1)‖G‖_Y + 2d(‖j^c_0‖ + ‖j‖_Pc)) + C_s‖s‖_R]·A_MA_1η,
  C_s := Σ_q[2d(1 + C_ρη)L^{−(σ+θ)q−θ} + 2n_ovC_ΨL⁴L^{−θq}η] < ∞;
- divergences from G_l, l ≥ 1 (π ≤ 4(d−1)ηL^{−θ(k−l)}‖G‖_Y): plain ≤ 4(d−1)η‖G‖_Y, R ≤ 4(d−1)C_{S1}L^θη‖G‖_Y, Y ≤ 8(d−1)A_ÑC_{S1}L^{(θ+α−1)(k−m)−θ(k−l)}η‖G‖_Y
  ≤ 8(d−1)A_ÑC_{S1}L^{(α−1)(k−m)}η‖G‖_Y (k − l ≥ k − m) — **no window needed**;
- divergences from s_l (π_l(ω_l) ≤ n_ovC_ΨL^{3−θ}L^{−θq}η‖s‖_R, π_{l+1}(ω_{l+1}) ≤ C_ΨL^{−θ}L^{−θq}η‖s‖_R): plain ≤ n_ovC_ΨL³η‖s‖_R (one input level per output
  level), R ≤ C_{S1}L^θ(n_ovL³ + 1)C_Ψη‖s‖_R/(1 − L^{−θ}), Y ≤ 2A_ÑC_{S1}L^{2θ}(n_ovL³ + 1)C_Ψη‖s‖_R/(1 − L^{−θ}) (same exponent argument) — no window;
- Φ-divergences (j_l, G_l): carry an extra ρ_l²η ≤ L^{−2(k−l)} — negligible, absorbed;
- **the divergence of G_0 (w_A^{(0)}, π_0 ≤ 4(d−1)η‖G^c_0‖, no decay):** plain (P0) ≤ 4(d−1)η‖G^c_0‖, R ≤ 4(d−1)C_{S1}L^θη‖G^c_0‖, and
  **Y ≤ 8(d−1)A_ÑC_{S1}L^{(θ+α−1)(k−m)}η‖G^c_0‖ — bounded uniformly in k exactly when α + θ ≤ 1.**
Every term is ≤ (constant)·η·N_ℛ(f), uniformly in k, T; take the infimum over ℛ on the right (the left side does not depend on ℛ). ∎
**The window, and why it is not an artefact of a careless bound.** By PER-3/PER-4, d^TG′_m = (B^TS_1^T − 1)w_m − M_m^T… is fixed by the operator; for a
smooth w_m the current (B^TS_1^T − 1)w_m is L-periodic with mean zero and O(1) relative oscillation (B^T spreads a coarse value over contour links
non-uniformly), so EVERY 2-form G′ with that divergence oscillates at the block scale, and its level-m Campanato seminorm is ≍ ρ_{m+1}^{−α}·sup —
adding d^T(3-forms) cannot change d^TG′. For the level-0 Wilson divergence (no L^{−θ(k−l)} decay in its input weight ω_0 = 1) the cost of this
representation is therefore L^{(θ+α−1)(k−m)} at level m. For α + θ > 1 I have neither a cheaper representation nor a lower bound for the
infimum N_1: **(P2-tw)_log at α + θ > 1 is NOT-VERIFIED** (not refuted). Lane A works at (¼, ½).
**Status.** PROVEN as an implication of: BFT-1 sizes of ȳ (Codex KOFF item 5, conditional on the lane-A package); the exact K′ formula and the
CONV-P charge decomposition (Codex F7, CONFIRMED / conditional on LA-loc); PER-1..PER-4 (§1, PROVEN-HERE, a3_55_per PASS); the spline constants
A_1, C_{S1} ≤ 3^d (proved above), A_M, A_Ñ finite (proved; not evaluated numerically). **This is Codex ALIGN2's "single most dangerous unverified
item"; its periodic obstruction (F5/F10) is removed by §1, and the k-uniform cost bookkeeping is closed in the stated window.**
