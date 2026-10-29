Reviewer model: claude-opus-5-5

# TSE55 — the Yang–Mills side of the non-freeness witness: two-sided asymptotic-freedom bound on the clover energy density e at n = 2

Author: Opus 5.5 worker (claude-opus-5-5), session 26. Deliverable of queue brief `tse.md`.
Writes only this file and `checks/ts55_*`. No git.

Coordinator amendment, 29 October 2026: the LGF paragraph and its status
references now consume the independently reviewed local scalar/free library.
These consumer edits await affected review; [their receipt](checks/full_proof_lgf_consumer_adoption.json)
records the original and amended source identities. Other TS hypotheses retain
their stated status.

## 0. PRE-STATED (written before any derivation; statements only)

UTC time at start: 2026-10-29 05:31:58 UTC (from `date -u`).

Targets (from the brief, to be made precise against NONFREE55 / OSLEAF55 / SRCAN55 by file + string):
- T1 (TS-e-up): λ_m⁸ · ω^c(O(f_λ), O(g_λ)) ≤ C₊ · u_{K−m}^{−κ}, κ > 0, at every short scale λ_m,
  as a conditional theorem from named inputs (per-step package STEP55; the flow (UIR^♮) or its
  two-sided-slope weakening; SRCAN55 SA-E1 / SA-K / Lemma V; a named large-field input (LF-dec)).
- T2 (TS-e-low): the same quantity ≥ c₋ · u_{K−m}^{−κ′}, at every short scale.
- T3: the leading term = the tree/one-loop image of e at the level-(K−m) background, computed EXACTLY
  (symbolic/rational arithmetic, LINEAR_PACKAGE symbols), with the running-coupling-ratio power made
  explicit; the remainder bounded conditionally by a further power of the running coupling.
- T4: T_NF for every limit point stated as an implication (NONFREE55 Theorem H-RED^e), every input named
  with its status.

What would count as a refutation / counterexample (each is a first-class result if found):
- R1: the leading (tree-level/one-loop) connected two-point function of e at separated smeared points
  vanishes identically, or has the wrong sign for the lower bound, so (TS-e-low) cannot come from it.
- R2: the leading term does not carry a negative power of u (e.g. it scales canonically with u^0, or the
  u-power cancels between the normalization of e and the propagator), so that κ ≤ 0 or κ′ ≤ 0 is forced
  under the stated normalization of O(f_λ).
- R3: κ′ < κ is impossible to arrange consistently with the upper bound (i.e. the two-sided bound is
  inconsistent, or the upper exponent forced by the remainder is weaker than the lower one in a way that
  destroys the log-suppression conclusion of SEP-e).
- R4: the remainder is NOT smaller than the leading term by a positive power of the running coupling
  under the named inputs (e.g. a large-field or non-local contribution of the same order survives).
- R5: Lemma V's mechanism (volume-uniform variance lower bound) does not transfer to separated points
  (coincident-point positivity only), in which case (TS-e-low) needs a different mechanism or input.
- R6: the statement of (TS-e-up)/(TS-e-low) in NONFREE55 is mis-normalised (wrong power of λ_m, wrong
  scaling dimension of e) relative to SEP-e, so that even a proof of both bounds would not feed H-RED^e.

---

# FINDINGS (appended from 2026-10-29T06:05Z; every section below was written after the PRE-STATED block)

## §1. Reading record, the object pinned exactly, symbol pins, Codex verdicts used

### 1.1 Read (large files by grep + bounded ranges only; locating strings, not line numbers, are authoritative)
- Briefs: queue `tse.md`; `REVIEW_BRIEF_55.md` (read twice: at 05:31Z and again at 05:47Z after it changed on disk — the change
  adds the output-size rule; this file follows it by appending section by section).
- NONFREE55.md in full (all 548 lines as on disk at 05:31Z, incl. errata E1–E6 and the §10 OSLEAF addendum).
- CODEX_REVIEW_NONFREE.md in full (299 lines; it ends with "Exactly what may be banked" items 1–6, complete).
- OSLEAF55.md §0, §1.1–§1.3 (Proposition FS, D1–D9, Lemmas P/DENSE/ACT, E0′–E3), §2 (Lemma RP-lat, Theorem CLOSURE-sep,
  (H_int-sep)), §3 ((X0), (X1), Lemma W, Theorem EXT, Proposition MIN, Proposition GROW), §6 (TR-0…TR-9, table T1–T18, C-T1…C-T8).
- CODEX_REVIEW_OSLEAF.md: PRE-STATED and findings F1–F3 (as on disk at 06:00Z; the file was still growing then).
- SRCAN55.md: §1 symbol table, §2.1 (the perturbed chain), §3.6 (Lemma SA-E1 + erratum E2, (LOC-e)), §3.7; headings of §2.2
  (SA-K), §2.6 (SA-F). CODEX_REVIEW_SRCAN.md items 7–10 and "Exactly what may be banked".
- SRCCD55.md §2.2, §2.3 (Lemma V, full proof), §3.1–§3.5 (SRC-κ, SRC-κ-LF, SRC-M, SRC-I, SRC-poly), §4 Propositions A and B.
- STEP55.md: PRE-STATED, §0, §1, §2.1–§2.4 (as on disk at 05:35Z), and §5 (Theorem CX, its hypothesis table, Proposition NZ-ret)
  as on disk at 06:00Z. STEP55 is still running; nothing below uses a statement of it except as a NAMED INPUT with that status.
- SRC2_55.md (PRE-STATED only, 54 lines, as on disk at 05:30Z; still running — coordinated with, not duplicated).
- HINT2_55.md R2.1–R2.4 (named bounds, H-RED♮, the flow chain L1–L11, the large-field discussion); CODEX_REVIEW_HINT2.md
  "Exactly what may be banked" and its F9/F10 rows.
- FLOW.md §7 (Theorem F-flow, Corollary F-ll), §8 (Theorem F-tune), §9 (Lemma F-ind), and line 25 / Lemma F-norm (u = β_Wilson).
- LINEAR_PACKAGE.md (frozen v1.1) §0–§12 in full.
- PROOF.md: banner + [S26-BANKED] block (by string), `Theorem N5-triv` (statement and proof), `Theorem RW` (pointer lines).
- ROTDEF.md §2.1–§2.2 (definition of e_a, O_a(f)).
**Not read:** BFT_A/BFT_B, PLD, HW, SF, HIST, RLARGE (only through the strings quoted in the files above); GV55 (SA-E1's input BFT-E
is used only through SRCAN55 and its Codex review). No claim below rests on an unread file without saying so.

### 1.2 The object, pinned exactly (coordinator's request of ≈06:05Z; Codex NONFREE R11 "most dangerous item")
Everything below — the targets (TS-e-up), (TS-e-low) and every theorem — concerns **one** object:
- the Wilson measure ω = ω_{K,R} on the hypercubic torus Λ_{a,R} = (aZ/RZ)⁴, a = L^{−K}, R ∈ 2ℕ, R ≥ R_0 (OSLEAF55 TR-0, TR-1);
  Wilson action S_W = u_0Σ_p s(U_p), s(U) := 1 − N⁻¹Re tr U, with **u_0 = g_bare(a; g_ref)^{−2} the bare coupling of OSLEAF55 TR-6**
  (F-tune's tuned trajectory at fixed renormalised coupling g_ref ∈ (0, g_sink]);
- the clover density **e_a(x) := (4a⁴)⁻¹Σ_{μ≠ν}Σ_{p∈clover_{μν}(x)}s(U_p)** (ROTDEF §2.2), no coupling factor;
- OSLEAF55 D8 with **Z(a) ≡ 1**: ê_a(x) := e_a(x) − ω(e_a(x)); for the two-point test F = f_λ⊗g_λ the lattice functional is
  S^{a,R}_2(f_λ⊗g_λ) = Σ_{x,y}a⁸f_λ(x)g_λ(y)ω(ê_a(x)ê_a(y)) = **Cov_ω(O(f_λ), O(g_λ))**, O(f) := Σ_xa⁴f(x)e_a(x).
  (Centring is irrelevant for the covariance; this is exactly CODEX_REVIEW_NONFREE R11's "for Z=1 its lattice value is exactly
  the TS connected covariance".)
- the witness value **W_m := λ_m⁸·Cov_ω(O(f_{λ_m}), O(g_{λ_m}))**, λ_m := L^{−m}, f_λ(x) := λ^{−4}f(x/λ), with one fixed pair
  f, g ∈ C_c^∞(R⁴), f, g ≥ 0, f, g ≢ 0, **D_− ≤ |x − y| ≤ D_+ for x ∈ supp f, y ∈ supp g** (0 < D_− ≤ D_+; NONFREE55 writes d, D),
  supports in a fixed ball B_{ρ_F} (so supp f_λ ∪ supp g_λ ⊂ B_{R/8} for every λ ≤ 1 once R ≥ R_0 ≥ 8ρ_F).
- the **matched level k := K − m** (level j has spacing ℓ_j := L^ja = L^{j−K}, so ℓ_k = λ_m), and u_k the chain's own effective
  coupling at level k (FLOW Def F-g, OSLEAF55 TR-3) along the same trajectory.
Nothing below changes the field, the normalisation Z ≡ 1, the trajectory, or the test pair. A Z(a) → 0 or ∞ would change the
limit field (NONFREE55 §10 item 3, CODEX_REVIEW_NONFREE R11); it is never used.

### 1.3 Symbol pins (systemic defect 1) — every collision this file meets, with its resolution
| symbol here | meaning here | collides with | resolution |
|---|---|---|---|
| u_j, g_j | **u_j = 1/g_j² with g = g_FLOW (the lane coupling): u = β_Wilson = 2N/g_std²** (FLOW l.25, Lemma F-norm) | PROOF §1 S3's g (= √(2N)g_FLOW: CODEX_REVIEW_OSLEAF F3); NONFREE55 §4.1's g (= g_std); ROTDEF's "u_0 = 1/g_bare²" (FLOW convention) | **g_std = √(2N)·g_FLOW** always; every formula below is in u; g_std appears only in §2.4's continuum check |
| κ_e, κ_e′ | the exponents of (TS-e-up), (TS-e-low) (NONFREE55's κ, κ′) | κ (soft-kernel stiffness, LINEAR_PACKAGE §1.3); κ_s, κ_0^{CE} (polymer decay / entropy); SRC-κ (a label) | the TS exponents are always subscripted e; κ alone is the kernel stiffness |
| ϑ | relative one-loop accuracy exponent of (PL-1L) (§5) | HINT2's ϑ (TS-up exponent), θ's everywhere | used only in (PL-1L) and §5–§6 |
| 𝔎_i | level-i slice of the free F-propagator (§2.2) | K_i = RG kernels (RLARGE "The exact chain"); K = top level | slices are always fraktur 𝔎; K alone is the top level |
| 𝔊^F, 𝔊^run | free F-propagator at coupling 1 (= P_ex) and the running-coupling propagator Σ_i𝔎_i/u_i | G (gauge group), G_s (KL kernels), G_i (images below) | fraktur 𝔊 for propagators; G_i, H_i are images |
| G_i, H_i | images E[O(f_λ)|U_i], E[O(g_λ)|U_i] (Proposition B's notation) | — | — |
| w_f(p) | plaquette weight ¼Σ_{x∈corners(p)}f_λ(x) (§2.1) | w (block weights of N5-triv), w_α (SRC-κ weights) | always subscripted by the test function |
| 𝔭_i(k) | geometric level weight (§5) | ϖ (path sums), p (plaquettes), p_W (white-noise cut), p (Balaban's large-field power) | fraktur 𝔭 |
| c_bub | 12(N² − 1)/π⁴ (the free bubble coefficient) | c_* (OSLEAF55 (X1)'s lattice multiple), c_1/C_1 (≥ 24 objects) | new name |
| I_8 | ∫∫f(x)g(y)\|x − y\|^{−8}dxdy (NONFREE55's I_γ at γ = 8) | — | — |
| μ_K, μ_1 | decay rates (level-i units) in (K-dec), (PL-1L) | m (level offset), m′, m_* (LINEAR_PACKAGE rates), m_cov (N5-triv) | μ always a rate, m always the level offset |
| D_−, D_+ | separation bounds of the test pair in units of λ | D = N² − 1 (STEP55), D (NONFREE55's upper separation) | N² − 1 is always written out |
| R | torus side (physical) | R_F (FLOW's additive flow error), R (STEP55's box side) | R_F always subscripted |
| γ | FLOW's coupling-domain threshold (TR-4) | NONFREE55's leading exponent γ of Theorem FS | the FS exponent is written γ_FS |
| d | lattice exterior derivative / dimension 4 | NONFREE55's d (separation) | separations are D_± |

### 1.4 Codex verdicts used, and my position on each (REVIEW_BRIEF_55: "saying so explicitly in either direction")
| Codex item (file, locating string) | Codex verdict | mine |
|---|---|---|
| NONFREE R10 "the core FS/SEP-e exclusion survives" + R2 (variance-corrected mixtures) + R3 (masses may enter leading terms) | CONFIRMED with repairs | **agree** (spot-checked FS's load-bearing step — no negative log powers in Wick products of the K_1 series, DLMF 10.31.1 form as Codex quotes — and SEP-e's two halves; §7). I use only the repaired statements |
| NONFREE R11 "H-RED^e is a valid conditional limit argument" (fixed m first, then K, R; κ′ ≥ κ forced) | CONFIRMED implication | **agree**; re-derived in §7.2 |
| NONFREE R1 "the boundary threshold is c > 6 (not c > 2) at p = 1/2" | REFUTED NONFREE55 §6.3 | **agree** (re-derived: Σ_n(U + bn)^{−c/2} ≍ U^{1−c/2} is o(U^{−2}) iff c > 6); used in (LF-dec), §6.4 |
| NONFREE R8 (Maxwell constants via B(z) = Λ²I(z), tr DDᵀ = 6/(π⁴r⁸)) and R13 (e = F²/(2u) with u = 2N/g_std², amplitude 12(N²−1)/(π⁴u²)) | CONFIRMED | **agree**; a third, independent route (closed tensor form (4d − 8)tr T² + 4(tr T)²) in §2.4 and check ts55_1 |
| NONFREE R13 "the anomaly-to-e operator identification is not banked" | NOT-VERIFIED | **agree**; nothing below uses e ∝ Θ |
| OSLEAF F3 "g_PROOF = √(2N) g_FLOW" | REFUTED OSLEAF55's dictionary | **agree** (both use s(U) = 1 − N⁻¹Re tr U; equality of Wilson coefficients forces it); pinned in §1.3 |
| SRCAN item 8 / bank 7 "E_tree = −∂_zS_tree; coefficient 6 (6/N in Frobenius norm)" | CONFIRMED / sign REFUTED | **agree** (§8 V5) |
| SRCAN item 9 / bank 8 "the a^{−4} singleton counterexample … scalar flow analyticity alone is not that control" | CONFIRMED | **agree**, and it reappears here as the canonical-localisation obligation (CSL) of §6.3 |
| SRCAN item 10 / bank 10 (bumps at scale δ force SA-K radii ∝ δ^α) | CONFIRMED | **agree**; consequence for the AF envelope in §4.4 |
| SRCAN bank 4 (SA-K, tree level, sup-plus-Wilson-Hölder class on 𝒞_glob, conditional) | CONFIRMED (scoped) | **agree**; used only for the tree-level part of (SRC-rel) at depth k (§4.4) |
| [S26-BANKED] "Proposition B and Lemma V CONFIRMED" (SRCCD55 + CODEX_REVIEW_SRCCD items 1–7) | CONFIRMED | **agree**; Proposition B re-derived in §3.1 (its proof is four lines); Lemma V's mechanism examined in §4.1 |
| HINT2 bank 3 "B-BR's positive total slope suffices for the summation/tuning argument" | CONFIRMED conditional | **agree**; this file needs only the pairwise bracket (FLOW-pw) that F-flow delivers from (B-BR) (§6.1) |

## §2. The leading term, exactly (brief item 2 (i))

### 2.1 The source is a coupling-field shift; the quadratic part of O(f). PROVEN-HERE (elementary; + banked identity)
- **Exact identity** (SRCCD55 Lemma V Step 0; [S26-BANKED] "the e-source changes only the Wilson coefficient"; re-derived: each
  plaquette lies in the clovers of its 4 corners, and the ordered pairs count its plane twice): O(f) = Σ_p h^f_□(p)s(U_p) with
  **h^f_□(p) := ½Σ_{x∈corners(p)}f(x)**. Hence ω(exp Σ_iz_iO(f_i)) is the Wilson integral with the bare coefficient shifted,
  u_0 → u_0 − Σ_iz_ih^{f_i}_□(p), plaquette by plaquette (SRCAN55 §2.1), and
  Cov_ω(O(f), O(g)) = ∂_{z_1}∂_{z_2}log ω(e^{z_1O(f)+z_2O(g)})|_0 is a mixed second derivative of the free energy in the coupling
  field. Every statement below about W_m is a statement about this one function.
- **Quadratic part.** For U_p = exp(iX_p), X_p Hermitian traceless with eigenvalues ξ_j: s(U_p) = N⁻¹Σ_j(1 − cos ξ_j) =
  (2N)⁻¹tr X_p² − (24N)⁻¹tr X_p⁴ + O(X⁶). Writing X_p = √(2N)Σ_aF^a_pt^a with tr(t^at^b) = δ^{ab}/2:
  **s(U_p) = ½Σ_a(F^a_p)² + O(|F_p|⁴)** (check ts55_1 A5, with a failing control at tr(t^at^b) = δ^{ab}). In the same normalisation
  of the links, U_b = exp(i√(2N)B^a_bt^a), one has F^a_p = (dB^a)_p + O(B²) and the Wilson action's quadratic part is
  **(u_0/2)Σ_a‖dB^a‖²**: N² − 1 independent copies of LINEAR_PACKAGE's abelian chain ("one real component", §1.1) at coupling u_0.
  (u_0 is FLOW's u = β_Wilson = 2N/g_std²; with u read as 1/g_std² the coefficient would be off by 2N — CODEX_REVIEW_NONFREE R13,
  nf55_b B1-F.)
- Therefore **O(f)^{(2)} = Σ_aΣ_pw_f(p)(F^a_p)²**, **w_f(p) := h^f_□(p)/2 = ¼Σ_{x∈corners(p)}f(x)**; Σ_pw_f(p) = 6Σ_xf(x) (each site
  is a corner of 24 plaquettes); w_f ≥ 0 when f ≥ 0.

### 2.2 The curvature chain, its slices 𝔎_i, and the running-coupling model 𝔊^run (definitions; PROVEN-HERE properties)
*Abelian linear chain at coupling 1, one colour, κ_i ≡ κ (TR-2: one κ for all levels).*
- F_0 ~ N(0, P_ex) on level-0 2-forms (P_ex := orthogonal projector onto exact 2-forms): this is the law of dB_0 under
  e^{−½‖dB_0‖²}dB_0 with flat (unfixed) gauge directions, which is what Haar measure linearises to.
- For i < K: **F_{i+1} := Q_2F_i + dξ_i/√κ**, ξ_i iid standard Gaussians on level-(i+1) links. This is the curvature of the soft
  kernel's output B_{i+1} = QB_i + ξ_i/√κ, because **d∘Q = Q_2∘d** (LINEAR_PACKAGE Lemma 2.2 (i): "dA′(P) = avg_{y∈B(X)}Φ_A(sq_y)",
  the straight-square flux; re-derived as STEP55 Lemma ST — the S4′ axial legs are a gradient d∘h, killed by d). So
  (F_0, …, F_K) is a Markov chain of gauge-invariant data.
- **Slices.** 𝔎_i := Cov(E[F_0|F_i] − E[F_0|F_{i+1}]) for i < K, 𝔎_K := Cov(E[F_0|F_K]). By the Markov property E[F_0|F_i, …, F_K] =
  E[F_0|F_i]; the Doob increments are orthogonal, and Gaussian, hence independent; so
  **Σ_{i=0}^{K}𝔎_i = Cov(F_0) = P_ex =: 𝔊^F** (the free lattice F-propagator at coupling 1) — exactly, on every torus.
- **What the slices are.** E[F_0|F_i] is the fine curvature of the level-i background (the Setting-SC minimiser with top level i:
  a Gaussian conditional mean is the minimiser of the quadratic form in the conditioned-out variables; flat gauge directions make it
  depend on F_i only — the minimiser's curvature is invariant under coarse gauge shifts because Q∘d = d∘ev). Cov(F_i | F_{i+1}) =
  d C_i dᵀ with C_i the gauge-fixed per-level fluctuation covariance of PROOF `Theorem N5-triv` (the operator with "the full
  effective energy E_i"). So **𝔎_i = (the level-i fluctuation of one RG step at the trivial background and coupling 1, seen in the
  fine curvature)** — the Gaussian part of exactly what Proposition B's per-step law (B2) integrates at step i.
- **Running model.** F^{run} := Σ_{i=0}^{K}u_i^{−1/2}ζ_i, ζ_i independent centred Gaussians with Cov ζ_i = 𝔎_i, N² − 1 independent
  colours; covariance **𝔊^run := Σ_{i=0}^{K}𝔎_i/u_i**, with u_i the chain's own couplings on the trajectory. At uniform coupling
  u_i ≡ u it is the free Wilson Gaussian at coupling u (𝔊^F/u). It is the RG-improved free field: each level's fluctuation carries
  its own level's coupling.

### 2.3 Proposition GT (the per-level one-loop terms; exact). PROVEN-HERE
For i < K put (with f = f_λ, g = g_λ in the weights)
  **Λ_i^{run} := λ⁸(N² − 1)Σ_{p,q}w_f(p)w_g(q)[4𝔊^run_{>i}(p,q)·𝔎_i(p,q)/u_i + 2𝔎_i(p,q)²/u_i²]**, 𝔊^run_{>i} := Σ_{j>i}𝔎_j/u_j,
  **Λ_K^{run} := 2λ⁸(N² − 1)Σ_{p,q}w_f(p)w_g(q)𝔎_K(p,q)²/u_K²**.
In the running model with 𝔉_i := σ(ζ_i, …, ζ_K) and Q_w := Σ_aΣ_pw(p)(F^{run,a}_p)²:
  (a) λ⁸E[Cov(E[Q_f|𝔉_i], E[Q_g|𝔉_i] | 𝔉_{i+1})] = Λ_i^{run} (i < K), λ⁸Cov(E[Q_f|𝔉_K], E[Q_g|𝔉_K]) = Λ_K^{run};
  (b) **Σ_{i=0}^{K}Λ_i^{run} = W^{lead} := 2λ⁸(N² − 1)Σ_{p,q}w_f(p)w_g(q)𝔊^run(p,q)²** (≥ 0 when f, g ≥ 0).
*Proof.* Write F^{run} = c + z with c := Σ_{j>i}u_j^{−1/2}ζ_j (𝔉_{i+1}-measurable) and z := u_i^{−1/2}ζ_i (independent of 𝔉_{i+1}).
Then E[Q_f|𝔉_i] = Q_f(c + z) + (an 𝔉_i-independent constant), and Q_f(c + z) = Q_f(c) + 2Σ_{a,p}w_f(p)c^a_pz^a_p + Q_f(z). Given 𝔉_{i+1},
Isserlis' theorem (odd moments vanish, Cov(z^a_pz^a_p′, z^b_qz^b_q′) by pairings) gives the conditional covariance
Σ_aΣ_{p,q}w_f(p)w_g(q)[4c^a_pc^a_q𝔎_i(p,q)/u_i + 2(𝔎_i(p,q)/u_i)²]; averaging, E[c^a_pc^b_q] = δ^{ab}𝔊^run_{>i}(p,q). The top term is
Wick for Q of a Gaussian. (b): with a_i := 𝔎_i/u_i entrywise, Σ_i(2a_i² + 4a_iΣ_{j>i}a_j) = 2(Σ_ia_i)². ∎
*Check ts55_2* (criteria first): on 12 random 4-level Gaussian models, each per-level value computed by brute-force exact moments
(not by the formula) equals Λ_i exactly and the sum equals the bubble; controls fired (4 → 2 breaks 12/12; dropping the top term
breaks 12/12). **The per-level terms have no sign** (negative values occur, e.g. −277184/945 at level 0 of model 12): only
the sum is a weighted sum of squares. This is why no per-level positivity argument can replace the global identity (b).

### 2.4 The free bubble coefficient c_bub = 12(N² − 1)/π⁴ (exact), and Lemma FREE
- **Tensor identity (PROVEN-HERE).** For any symmetric d × d matrix T put X_{μνρσ} := δ_{νσ}T_{μρ} − δ_{νρ}T_{μσ} − δ_{μσ}T_{νρ}
  + δ_{μρ}T_{νσ}. Expanding the square, the four diagonal terms give 4d·tr T², the six cross pairs give −tr T² four times and
  (tr T)² twice, so **Σ_{μνρσ}X² = (4d − 8)tr T² + 4(tr T)²**. With T = ∂∂|z|^{−2} = (8zzᵀ − 2|z|²1)/|z|⁶ in d = 4: tr T = 0 and
  tr T² = (64 − 32 + 16)/|z|⁸ = 48/|z|⁸, so Σ X² = 384/|z|⁸. The continuum F-F correlator of ½∫Σ_{μ<ν}F² is D = −X/(4π²)
  (Feynman gauge; gauge-independent: nf55_a A1, CODEX_REVIEW_NONFREE R8), so **Σ_{μ<ν,ρ<σ}D_{μν,ρσ}(z)² = ¼Σ_{μνρσ}D² =
  6/(π⁴|z|⁸)**. This is a third independent route to NONFREE55's 24/(π⁴|z|⁸) (nf55_a: symbolic differentiation; Codex R8:
  D = Λ²I(z)/(π²r⁴), tr DDᵀ = 6/(π⁴r⁸)). *Check ts55_1* (criteria first): A1 (identity and 384 at 8 rational points, T from the
  generic quotient rule), A2 (identity in d = 3 and 384 failing there), A3 (unordered sum = ¼), A4 (two amplitude routes both 12),
  A5 (generator normalisation) — all PASS; controls A1-F, A4-F, A5-F fired.
- **Amplitude.** For the free field at coupling u: Cov(O(f)^{(2)}, O(g)^{(2)}) = 2(N² − 1)Σ_{p,q}w_f(p)w_g(q)𝔊^F(p,q)²/u² (Wick, each
  colour separately). As a → 0 at fixed λ, w_f(p) → f_λ(x_p), the six planes at a site give Σ_{μ<ν,ρ<σ}D² = 6/(π⁴r⁸), and
  Riemann sums give **λ⁸Cov → c_bub·I_8/u², c_bub := 2·6(N² − 1)/π⁴ = 12(N² − 1)/π⁴**, I_8 := ∫∫f(x)g(y)|x − y|^{−8}dxdy ∈
  [‖f‖_1‖g‖_1D_+^{−8}, ‖f‖_1‖g‖_1D_−^{−8}] (> 0). Consistency: NONFREE55's e ≈ F^aF^a/(2u) with 48(N² − 1)/(π⁴r⁸) gives
  48/(2u)² = 12/u² (CODEX_REVIEW_NONFREE R13); the clover route (N² − 1)/32·16·24 = 12(N² − 1) agrees (ts55_1 A4).
- **(LGF) — locally proved scalar/free library; independent LAND review.**
  [LGF](LGF.md), equations (1)–(5), uses the positive graph Laplacian
  Δ = Σ_j(2I − S_j − S_j⁻¹) = 8(I − P), with counting inner product,
  λ(ξ) = 4Σ_j sin²(ξ_j/2), and c_4 = 1/(4π²). Explicitly,
  G(x) = (2π)⁻⁴∫_[−π,π]⁴ exp(iξ·x)/λ(ξ)dξ and
  G_T(x) = T⁻⁴Σ_{ξ∈(2π/T)Z⁴ mod 2π, ξ≠0} exp(iξ·x)/λ(ξ).
  The latter has counting mean zero and ΔG_T = δ_0 − T⁻⁴.
  Oriented differences are ∇_j⁺ = S_j − I and ∇_j⁻ = I − S_j⁻¹,
  with repeated indices allowed. For 0 ≤ m = |α| ≤ 2 and A = 2^1000,
  |∇^αG(x) − ∂^α(c_4|x|⁻²)| ≤ A|x|^(−3−m) for |x| ≥ 1;
  on the torus, for 1 ≤ |x| ≤ T/4, the bound is
  A|x|^(−3−m) + A T^(−2−m). Thus the torus corrections at orders
  zero, one and two are respectively T⁻², T⁻³ and T⁻⁴.
  For the zero-mean continuum torus Green function, the grouped image identity is
  K_T(z) = S_T(z) + C_T + |z|²/(8T⁴), 0 < |z| < T/2, where
  S_T(z) = Φ(z) + Σ_OΣ_{n∈O}[Φ(z+Tn) − Φ(Tn)] and Φ(z) = c_4|z|⁻²;
  O ranges over complete signed-permutation orbits of nonzero integer vectors.
  LGF equations (19)–(20), (29)–(32)
  supply the lattice Fourier-shell remainder and its alias constant −a_*T⁻⁴;
  no unregularized lattice image sum is used.
  LGF equations (37)–(41) prove the counting-norm Weitzenböck identity and
  𝔊^F = P_ex = dΔ_1⁻¹d* for the quadratic one-colour law at coupling one,
  with gauge and harmonic link modes contributing no curvature. For plaquette
  base points x_p, x_q and 1 ≤ r = |x_p − x_q| ≤ T/4,
  |𝔊^F(p,q) − D_{μν,ρσ}(x_p − x_q)| ≤ 2^1002(r⁻⁵ + T⁻⁴).
  Its squared-kernel error is bounded by 2^2010(r⁻⁹ + r⁻⁴T⁻⁴), as needed below.
  [The independent LGF review](REVIEW_LGF.md) confirms this library scope.
  This supplies only FREE's kernel input; its test-function sums and the other
  hypotheses of FREE and TS retain their separate scope.
- **Lemma FREE (PROVEN-HERE given (LGF)).** Let L_free := 2λ⁸(N² − 1)Σ_{p,q}w_f(p)w_g(q)𝔊^F(p,q)² (lattice, coupling 1). There are
  d_0 = d_0(f, g, L) and R_0 such that for K − m ≥ d_0 and R ≥ R_0: **½c_bubI_8 ≤ L_free ≤ (3/2)c_bubI_8.**
  *Proof.* Lattice distances between the supports are r ≥ D_−λ/a − 2 ≥ ½D_−L^{K−m} once L^{K−m} ≥ 4/D_−.
  Increase R_0 to at least 8(D_+ + 1), retaining the support condition of §1.2.
  Since λ ≤ 1 and a ≤ 1, r ≤ D_+λ/a + 2 ≤ T/4 for T = R/a. Thus the
  entire kernel comparison lies in LGF's stated torus range. By (LGF) and |D| ≤ C_Dr^{−4},
  |𝔊^F² − D²| ≤ C(r^{−9} + r^{−4}T^{−4}), and Σ_pw_f ≤ 12a^{−4}‖f‖_1 for a/λ small (Riemann), so the replacement error is
  ≤ C(f,g)[(a/λ)D_−^{−9} + D_−^{−4}(λ/R)⁴] (λ ≤ 1). Replacing w_f(p) by f_λ(x_p) costs a relative O(a‖∇f‖_∞/(λ‖f‖_∞))·…, and the
  Riemann sum of the smooth integrand f_λ(x)g_λ(y)|x − y|^{−8} on {|x − y| ≥ D_−λ} differs from the integral by a relative O(a/λ).
  Both errors are ≤ ½c_bubI_8 for L^{K−m} and R large. ∎ (The constants depend on f, g only through ‖f‖_{C¹}, ‖g‖_{C¹}, D_±.)

## §3. The multiscale bookkeeping (PROVEN-HERE, each from named lane statements)

### 3.1 Proposition B, re-derived (the exact level decomposition of W_m). CONFIRMED
SRCCD55 Proposition B ([S26-BANKED], check sc55_tel): the chain W_ch = e^{−S_W(U_0)}Π_{i<K}K_i(U_{i+1}, U_i) with ∫K_i dU_{i+1} = 1 is
Markov in the level index, so for bounded G, H of U_0, with G_i := E[G|U_i]: Cov(G, H|U_K) = Σ_{i<K}E[Cov(G_i, H_i|U_{i+1})|U_K].
*Re-derivation (load-bearing step).* The joint density factorises as (function of U_0..U_i)·(function of U_i..U_K), so
E[G|U_i, …, U_K] = G_i; the increments G_i − G_{i+1} are martingale differences for the decreasing filtration σ(U_i, …, U_K), so
cross terms vanish and the diagonal ones are Cov(G_i, H_i|U_{i+1}). ∎ With the law of total covariance at level K:
  **W_m = Σ_{i=0}^{K−1}λ⁸E[Cov(G_i, H_i | U_{i+1})] + λ⁸Cov(G_K, H_K)**,  G_i := E[O(f_λ)|U_i], H_i := E[O(g_λ)|U_i].   (3.1)
O(f_λ) is bounded on the finite lattice (0 ≤ e_a ≤ 24a⁻⁴, OSLEAF55 (X0)), so Proposition B applies. (3.1) is exact for the Wilson
measure on the trajectory; it involves only conditional expectations (images) and per-step conditional covariances — **never a
coincident-point variance of e** (NONFREE55 §6.2's requirement is met by construction).

### 3.2 Lemma KD — the slice bound (K-dec). PROVEN-HERE as an implication of pre-S24 lane theorems
**(K-dec)** There are M_K < ∞ and μ_K > 0, depending only on (N, L, κ), such that for all K, R, all level-0 plaquettes p, q
(base points x_p, x_q, ℓ¹ torus distance):
  |𝔎_i(p,q)| ≤ M_K·L^{−4i}·exp(−μ_K|x_p − x_q|_1/L^i)  (0 ≤ i < K),   |𝔎_K(p,q)| ≤ M_K·L^{−4K}.
*Proof from:* LINEAR_PACKAGE Lemma 4.4 (frozen v1.1; PROVEN, CONFIRMED by REVIEW_S16_S17): the fine curvature at offset u is
f_0 = 𝒦^{ax}_u(dB_k) with |K^{ax}_u(X)| ≤ M_ax e^{−m′|X|_1} for 0 < m′ < m_*′, uniformly in k, T, u; LINEAR_PACKAGE Lemmas 2.5, 2.7
(E_k depends on B_k only through dB_k; E_k ≥ c_E‖dB_k‖²); PROOF `Theorem N5-triv` (pre-S24 [S18]; reviewed in REVIEW_S18_S19 per
LINEAR_PACKAGE §9's status note): |C_i(b,b′)| ≤ c_N5e^{−m_cov d(b,b′)}, c_N5 := 2/γ_i + e^{4m_cov(L−1)}/‖w‖², uniformly in i, k, T.
I did not re-derive these three; the composition below is mine.
(i) i = 0: 𝔎_0 = Cov(F_0|F_1) = dC_0dᵀ, so |𝔎_0(p,q)| ≤ 16c_N5e^{2m_cov}e^{−m_cov|x_p−x_q|_1} (4 links per plaquette, link distance
≥ plaquette distance − 2). (ii) 1 ≤ i < K: E[dB_0(p)|F_i] = L^{−2i}Σ_Pk(p,P)F_i(P) with |k(p,P)| ≤ M_ax e^{−m′|X_p − X_P|_1} (X_p
the level-i block of p; dB_0 = n^{−2}f_0, n = L^i), and Cov(F_i|F_{i+1}) = dC_idᵀ. With μ := min(m′, m_cov) and the triangle
inequality, e^{−μ(a+b+c)} ≤ e^{−(μ/2)|X_p−X_q|_1}e^{−(μ/2)(a+c)}, and Σ_Pe^{−(μ/2)|X_p−X_P|_1} ≤ 6coth⁴(μ/4) (6 planes;
Σ_{x∈Z}e^{−t|x|} = coth(t/2)), so |𝔎_i(p,q)| ≤ L^{−4i}·576c_N5e^{2m_cov}M_ax²coth⁸(μ/4)·e^{2μ}e^{−(μ/2)|x_p−x_q|_1/L^i}
(|X_p − X_q|_1 ≥ |x_p − x_q|_1/L^i − 4). (iii) i = K: the u = 1 chain's B_K-marginal is ∝ e^{−E_K(B_K)}, a quadratic form in
F_K = dB_K that is ≥ c_E‖F_K‖², so Cov(F_K) ≤ (2c_E)⁻¹ on exact forms and its entries are ≤ (2c_E)⁻¹; hence
|𝔎_K(p,q)| ≤ L^{−4K}·18M_ax²coth⁸(m′/2)/c_E. Take μ_K := μ/2 and M_K the largest of the three constants. ∎
*Scope.* (K-dec) is about the free, trivial-background, coupling-1 chain only; it is the "linear" input of the leading term.

### 3.3 Lemma SUM (level sums with canonical weights). PROVEN-HERE (arithmetic of (FLOW-pw))
**(FLOW-pw)** b_−(n − j) − R_F ≤ u_j − u_n ≤ b_+(n − j) + R_F for 0 ≤ j ≤ n ≤ K, with b_± := β_±log L > 0, and u_j ≥ γ⁻² for all j
(FLOW Theorem F-flow on [0, K] along TR; TR-7 gives u_K − R_F ≥ γ⁻²). For the matched level k put
  **𝔭_i(k) := L^{4(k−i)}exp(−μ_1D_−L^{k−i}) (i < k),  𝔭_i(k) := L^{−8(i−k)} (k ≤ i ≤ K)**,  ū_i := u_{max(i,k)},
with μ_1 ∈ (0, μ_K/2]. **Lemma SUM.** If u_k ≥ 2R_F + 2 and s > 0: Σ_{i=0}^{K}ū_i^{−s}𝔭_i(k) ≤ C_SUM(s)·u_k^{−s}, with
C_SUM(s) := S_<(μ_1) + 2^s/(1 − L^{−8}) + γ^{2s}T_s/(1 − L^{−8}), S_<(μ) := Σ_{n≥1}L^{4n}e^{−μD_−L^n} (finite for every μ > 0),
T_s := sup_{u≥γ⁻²}u^sL^{−8⌈(u/2 − R_F)/b_+⌉} (finite).
*Proof.* i < k contributes u_k^{−s}S_<. For i = k + n: u_k − u_{k+n} ≤ b_+n + R_F, so u_{k+n} ≥ u_k/2 for n ≤ n_1 := ⌊(u_k/2 − R_F)/b_+⌋,
giving ≤ 2^su_k^{−s}Σ_nL^{−8n}; for n > n_1, u_{k+n} ≥ γ⁻² and Σ_{n>n_1}L^{−8n} ≤ L^{−8(n_1+1)}/(1 − L^{−8}) with
n_1 + 1 ≥ ⌈(u_k/2 − R_F)/b_+⌉, so that part is ≤ γ^{2s}T_su_k^{−s}/(1 − L^{−8}). ∎ *Check ts55_3* S1 (criteria first; 126 admissible
synthetic sequences, three (b_−, b_+, R_F) sets, s = 2, 3): PASS. **Control S1-F:** without the canonical weight L^{−8n} the same
sum, u_0²Σ_nu_n^{−2}, is 595 > 10 on the slowest admissible sequence — it grows like u_k/b_−: per-level O(u_i^{−2}) bounds without
canonical decay at coarse levels give **no** u_k^{−2} envelope (used in §4.3).

### 3.4 Lemma AF-cmp (running bubble = free bubble/u_k² up to O(u_k^{−3})). PROVEN-HERE from (K-dec) + (FLOW-pw)
Let p, q be plaquettes with w_{f_λ}(p)w_{g_λ}(q) ≠ 0 and L^k ≥ 4/D_−, so |x_p − x_q|_1 ≥ ½D_−L^k (lattice units). If u_k ≥ 2R_F + 2:
  **|𝔊^run(p,q) − 𝔊^F(p,q)/u_k| ≤ C_cmp·L^{−4k}/u_k²,   |𝔊^F(p,q)| ≤ C_G·L^{−4k},**
C_cmp := M_K[2Σ_{n≥1}(b_+n + R_F)L^{4n}e^{−μ_KD_−L^n/2} + 2Σ_{n≥0}(b_+n + R_F)L^{−4n} + γ²V], V := sup_{u≥γ⁻²}u·(b_+c(u) + R_F +
b_+/(1 − L^{−4}))L^{−4c(u)}/(1 − L^{−4}), c(u) := ⌈(u/2 − R_F)/b_+⌉; C_G := M_K[Σ_{n≥1}L^{4n}e^{−μ_KD_−L^n/2} + (1 − L^{−4})^{−1}].
*Proof.* 𝔊^run − 𝔊^F/u_k = Σ_i(1/u_i − 1/u_k)𝔎_i and |1/u_i − 1/u_k| ≤ (b_+|i − k| + R_F)/(u_iu_k) (FLOW-pw). For i = k − n < k:
u_i ≥ u_k − R_F ≥ u_k/2 and |𝔎_i| ≤ M_KL^{−4k}L^{4n}e^{−μ_KD_−L^n/2}. For i = k + n: split at n_1 as in Lemma SUM, with |𝔎_i| ≤ M_KL^{−4k}L^{−4n};
for n > n_1 use u_{k+n} ≥ γ⁻² and Σ_{n>n_1}(b_+n + R_F)L^{−4n} ≤ L^{−4(n_1+1)}(b_+(n_1+1) + R_F + b_+/(1 − L^{−4}))/(1 − L^{−4}), which is
decreasing in n_1 + 1 ≥ c(u_k); multiply and divide by u_k. The bound on 𝔊^F = Σ_i𝔎_i is the same sum without the coupling
factors. ∎ *Check ts55_3* S2 (coarse side, exact constants) and S3 (fine side, termwise, truncated at n ≤ 6 — see §9): PASS;
**control S2-F:** without the canonical weight L^{−4n}, u_0²Σ_n|1/u_n − 1/u_0| = 1573.7 ≫ 10·C_cmp = 11.3: the comparison is
O(u_k^{−2}) only because coarse slices are canonically suppressed.
**Consequence (the bubble).** With Σ_pw_f(p) ≤ 12a^{−4}‖f‖_1 (Riemann, a/λ small) and λ⁸a^{−8}L^{−8k} = 1:
  **|W^{lead} − L_free/u_k²| ≤ C_AF/u_k³,  C_AF := 288(N² − 1)‖f‖_1‖g‖_1·C_cmp(2C_G + C_cmp)**  (u_k ≥ max(1, 2R_F + 2)).   (3.4)
*Proof.* |𝔊^run² − (𝔊^F/u_k)²| ≤ |𝔊^run − 𝔊^F/u_k|·(|𝔊^run| + |𝔊^F|/u_k) ≤ C_cmpL^{−4k}u_k^{−2}·(2C_G + C_cmp)L^{−4k}u_k^{−1}; multiply by
2λ⁸(N² − 1)Σ_{p,q}w_fw_g. ∎

### 3.5 Lemma Λ-size (the one-loop terms are canonically small level by level). PROVEN-HERE from (K-dec) + (FLOW-pw)
There is A_Λ (depending on M_K, μ_K, D_±, ‖f‖_1, ‖g‖_1, N, L, b_±, R_F, γ) such that, for u_k ≥ 2R_F + 2 and every level i,
**|Λ_i^{run}| ≤ A_Λ·ū_i^{−2}·𝔭_i(k)** (with μ_1 ≤ μ_K/2).
*Proof.* For i = k − n < k: |𝔎_i| ≤ M_KL^{−4k}L^{4n}e^{−μ_KD_−L^n/2}, |𝔊^run_{>i}| ≤ C′L^{−4k}/u_k (the Lemma AF-cmp splitting applied to
Σ_{j>i}|𝔎_j|/u_j), u_i ≥ u_k/2, and L^{8n}e^{−μ_KD_−L^n} ≤ S_∞·L^{4n}e^{−μ_KD_−L^n/2}, S_∞ := sup_nL^{4n}e^{−μ_KD_−L^n/2}. For i ≥ k:
|𝔎_i| ≤ M_KL^{−4i}, |𝔊^run_{>i}| ≤ C″L^{−4i}/u_i (same splitting at level i; for u_i ≤ 2R_F + 2 use u_j ≥ γ⁻²). Multiply by
λ⁸(N² − 1)(Σw_f)(Σw_g) ≤ 144(N² − 1)‖f‖_1‖g‖_1a^{−8}λ⁸ and use λ⁸a^{−8}L^{−8i} = L^{−8(i−k)}. ∎

## §4. Four structural findings (each a first-class result; they shape the theorems of §5)

### 4.1 Proposition LV-sep — Lemma V's mechanism gives exactly zero at separated points. PROVEN-HERE (pre-stated R5: REALISED)
*Setting:* SRCCD55 Lemma V's (Wilson measure, R/a even, S := {(x, x + ae_1) : x ∈ (2aZ)⁴}, 𝔉 := σ(U_b : b ∉ S)).
**Statement.** If dist(supp f, supp g) > 4a then **E[Cov(O(f), O(g) | 𝔉)] = 0**, hence Cov(O(f), O(g)) = Cov(E[O(f)|𝔉], E[O(g)|𝔉]).
*Proof.* Lemma V Step 2 (no plaquette contains two links of S; given 𝔉 the U_b, b ∈ S, are independent): O(f) = Σ_{b∈S}ψ^f_b +
(𝔉-measurable), ψ^f_b := Σ_{p∋b}h^f_□(p)s(U_p), a function of U_b and 𝔉. Then Cov(O(f), O(g)|𝔉) = Σ_{b∈S}Cov(ψ^f_b, ψ^g_b|𝔉). For a
given b, ψ^f_b is non-constant in U_b only if a plaquette through b has a corner in supp f; all corners of the six plaquettes
through b lie within distance √5·a of each other; so for dist(supp f, supp g) > 4a at most one of ψ^f_b, ψ^g_b is non-constant
given 𝔉, and each summand vanishes. ∎
**Consequence.** Lemma V lower-bounds Var(O(f)) by E[Var(·|𝔉)], a sum of positive single-link conditional variances. At separated
supports that term is **identically zero**, and what remains, Cov(E[O(f)|𝔉], E[O(g)|𝔉]), carries no sign. The same happens for every
conditioning under which the two observables' non-measurable parts are conditionally independent — i.e. every conditioning on
fluctuations of range shorter than the separation. **So Lemma V's mechanism cannot give (TS-e-low)** (answer to brief item 1's
"check whether its mechanism gives (TS-e-low) at separated points": no). The only first-principles sign at separated points is
RP: for a reflected pair g = θf, f supported in {t > a}, Lemma RP-lat (OSLEAF55 §2) gives W_m = λ⁸ω(Θ(Â)Â) ≥ 0, Â := O(f_λ) −
ω(O(f_λ)) ∈ 𝔄_+ — a sign, not a magnitude. A positive lower bound of size u_k^{−2} needs the explicit leading term (§5).

### 4.2 Proposition FINE — the level-(K−m) image alone is not the leading term. PROVEN-HERE (structure); nonvanishing in toys
In the running model, the covariance of the level-k images is Cov(E[Q_f|𝔉_k], E[Q_g|𝔉_k]) = Σ_{i≥k}Λ_i^{run} =
2λ⁸(N² − 1)Σw_fw_g(𝔊^run_{≥k})², 𝔊^run_{≥k} := Σ_{j≥k}𝔎_j/u_j (Proposition GT applied from level k up). The rest of the one-loop
bubble is
  **W^{lead}_{fine,k} := Σ_{i<k}Λ_i^{run} = 2λ⁸(N² − 1)Σ_{p,q}w_fw_g[(𝔊^run)² − (𝔊^run_{≥k})²]**,
the fine-level (levels < K − m) per-step one-loop covariances — equivalently, the source–source term that the fine levels put into
the level-k one-loop effective generating function (the fine polymers meeting both supports). At uniform coupling it equals
u^{−2}·Φ_fine with Φ_fine a coupling-independent number fixed by (f, g, L, κ) and the lattice depth; with running couplings it is
u_k^{−2}Φ_fine(1 + O(u_k^{−1})) by the Lemma AF-cmp splitting. By (K-dec) |Φ_fine| ≤ C·L⁴e^{−μ_KD_−L/2}: small for widely separated
test functions, **but not smaller than the leading term by any power of the running coupling**. Toy instance (check ts55_2 G3):
u²·FINE_2 is u-independent and nonzero in 12/12 random models, and negative in some (e.g. −5376) — the level-k image covariance
can even exceed the full bubble. **Correction to brief item 2:** "(i) the leading term [is] the tree/one-loop image of e at the
level-(K−m) background … (ii) the remainder [is] smaller by a power of the running coupling" holds only if (i) includes the
fine-level one-loop source–source term, i.e. if the leading term is the whole one-loop bubble W^{lead} of Proposition GT. With the
tree-level image at level K − m alone, (ii) is false (the remainder contains u_k^{−2}Φ_fine). Taking D_− large does not rescue it:
the witness pair is fixed once for all m. Theorem TS below uses W^{lead}.

### 4.3 Canonical localisation above the source scale is necessary for κ_e = 2 and for (TS-e-low). PROVEN-HERE (route obstruction)
In (3.1) the levels i ≥ k are those at which both images sit inside one or two level-i blocks. Their natural per-level size is
λ⁸u_i^{−2}ℓ_i^{−8}λ⁸… — precisely, two images of total weight ‖f‖_1, ‖g‖_1 whose level-i energy densities are O(ℓ_i^{−4}u_i^{−1})
give a per-step covariance O(‖f‖_1‖g‖_1ℓ_i^{−8}u_i^{−2}), i.e. **λ⁸·(…) = O(L^{−8(i−k)}u_i^{−2})** — the canonical factor (λ/ℓ_i)⁸.
*Obstruction.* Without the factor L^{−8(i−k)}, per-level bounds C·u_i^{−2} sum to C·Σ_{n=0}^{m}u_{k+n}^{−2}, which does not tend to 0 as
m → ∞ (it is ≥ C·u_K^{−2} = C·g_ref⁴, and ts55_3's control S1-F shows u_k²·Σ growing like u_k/b_−). Abstract example: independent
bounded variables realising exactly c·u_i^{−2} at each coarse level meet every such per-level bound and have W_m ≥ c·g_ref⁴ for all m,
so (TS-e-up) fails for them. Hence **(CSL), canonical source localisation** — the level-i (i ≥ k) contributions carry L^{−8(i−k)} —
is an indispensable input of any per-level route to κ_e = 2 or to (TS-e-low) (the lower bound needs every remainder below
u_k^{−2}). *What supplies it.* Its tree-level part is **SRCAN55 Lemma SA-E1** (banked, with E2's constant 6 and Codex's sign
E_tree = −∂_zS_tree): the classical clover energy of the depth-r background obeys |E^{tree}_r[e(h)]| ≤ 6|supp h|ℓ_r^{−4}(2η_b + 9η_b²)²
— canonical: an image of a source of volume |supp h| ≍ λ⁴ is (λ/ℓ_r)⁴ times a full-block energy. This is exactly the role the brief
assigns SA-E1, and it is the only role it can play: an upper bound at tree level. The fluctuation part — that the one-loop and
higher corrections to the images, and their per-step fluctuations, also scale canonically with a coefficient 1 + O(u_r^{−ϑ}) — is
the (LOC-e)-type statement that CODEX_REVIEW_SRCAN item 9 showed does not follow from uniform activity bounds or from scalar flow
analyticity. **OPEN.** (Mechanism, ARGUED: e = −2∂S_W/∂u_0 per unit volume, and the marginal coupling's response ∂u_r/∂u_0 = 1 + O(g_r²)
— a two-loop effect, because the one-loop coefficient is u-independent — so the image of e at level r is the level-r density with
coefficient 1 + O(g_r²), not a power of u_0/u_r. This is the RG form of "Z_e → 1".)

### 4.4 The AF envelope needs the relative polydisc at depth K − m. PROVEN-HERE (two arithmetic facts)
- *(a) A fixed absolute source radius gives no envelope.* With SRCCD55 SRC-poly's ‖η‖_∞ ≤ r_0 and η = z_1f_λ + z_2g_λ, the radius is
  |z_i| ≤ r_0λ⁴/‖f_i‖_∞; Cauchy (Proposition A's argument) gives W_m ≤ C(S_0 + c_N(m + 1))‖f‖_∞‖g‖_∞/r_0² — growing like m ≍ log(1/λ).
  This is the "wrong direction" NONFREE55 §3.3 noted for SRC-κ's 𝔤_e. The envelope appears when the radius is **relative**:
  |z_i|‖f_i‖_∞ ≤ ε̂_*u_kλ⁴ (relative coupling shift ≤ 2ε̂_*u_k/u_j ≤ 4ε̂_* at every level j ≤ k, using u_j ≥ u_k − R_F) — §5.1.
- *(b) SA-K at depth K is the wrong depth for λ-concentrated sources.* SA-K's class requires the Wilson-coefficient Hölder seminorm
  in coarse units of the depth to be ≤ ε̂_*. At depth K (unit ℓ_ref = 1), two plaquettes at distance ≍ λ where f_λ differs by
  ≍ λ^{−4}‖f‖_∞ give [ε̂_0]_α ≳ g_0²|z|λ^{−4−α}‖f‖_∞, forcing |z| ≲ ε̂_*u_0λ^{4+α}; Cauchy then costs λ^{−2α} = L^{2αm} — fatal for an
  envelope (CODEX_REVIEW_SRCAN item 10's δ^α radii were adequate for OS0's power laws, not here; I agree with Codex and add this
  consequence). At depth k = K − m (unit λ) the seminorm is ≤ 2g_0²|z|λ^{−4}‖∇f‖_∞, so the relative polydisc is inside SA-K's class.
  Above level k the source is a localised perturbation of the level-k effective action, outside SA-K's scope (its composite starts
  at level 0): that is (CSL) again. **So SA-K supplies the tree-level part of the relative-polydisc analyticity up to depth K − m
  only.**

## §5. The conditional theorems (brief items 1–2 (ii))

All statements concern exactly the object of §1.2 (Wilson measure on TR, e_a of ROTDEF §2.2, Z ≡ 1, the fixed pair f, g ≥ 0,
k = K − m, u in FLOW's normalisation u = 1/g_FLOW² = 2N/g_std²).

### 5.1 Upper bound by Cauchy on the relative polydisc
**(SRC-rel) [OPEN; the relative-radius form of SRC2_55's target T1].** There are ε̂_* ∈ (0, 1], A_s < ∞, a polymer block side M,
κ_s > κ_0^{CE} (LINEAR_PACKAGE Theorem 5.1's entropy constant, in M-cube units) and c_1, independent of K, R, m, such that for all
K, R ≥ R_0, m with u_k ≥ 2R_F + 2, and all complex (z_1, z_2) in the **relative polydisc**
  𝔻_k := {|z_1|‖f‖_∞ ≤ ε̂_*u_kλ⁴, |z_2|‖g‖_∞ ≤ ε̂_*u_kλ⁴}:
  log ω(exp(z_1O(f_λ) + z_2O(g_λ))) = CT(z) + Σ_{r=0}^{K}Σ_{X∈𝒫_r}𝔞_r(X; z) + ℛ(z),
where CT is a sum of local terms of range ≤ c_1a, each depending on at most one of z_1, z_2; 𝒫_r is the set of connected unions of
level-r M-cubes; 𝔞_r(X; ·) is analytic on 𝔻_k, depends on z_1 (z_2) only if X meets supp f_λ (supp g_λ), and |𝔞_r(X; z)| ≤
A_se^{−κ_sd_r(X)} on 𝔻_k (d_r the touching-tree length in level-r M-cube units); ℛ (the top-level remainder) is analytic on 𝔻_k with
|ℛ(z) − ℛ(z_1, 0) − ℛ(0, z_2) + ℛ(0, 0)| ≤ A_s.
*How it differs from SRCCD55 SRC-poly:* the polydisc is relative (radius ∝ u_k, §4.4 (a)) instead of ‖η‖_∞ ≤ r_0, and U_K is
integrated (an IR remainder ℛ is allowed, only its mixed part is bounded) instead of conditioned on 𝒮_K.

**Theorem TS-up₁ (κ_e = 1). PROVEN as an implication of (SRC-rel) + (FLOW-pw).** For all K, R ≥ R_0 and m with u_k ≥ 2R_F + 2:
  **W_m ≤ C_+^{(1)}·u_{K−m}^{−1}**,  C_+^{(1)} := (‖f‖_∞‖g‖_∞/ε̂_*²)[4A_sK_0^{CE}(C_fe^{(κ_s−κ_0)c_M}S_0 + c_N(1 + (1 + R_F)/b_−)) + A_s],
with S_0 := Σ_{n≥1}L^{4n}e^{−(κ_s−κ_0)D_−L^n/M} < ∞, C_f := (diam(supp f)/M + 2)⁴, c_N := ((diam(supp f) + D_+)/M + 2)⁴, c_M a fixed
geometric constant (cube diameters), K_0^{CE} := sup_□Σ_{X∋□}e^{−κ_0d(X)} (Theorem 5.1 (g4) with Lemma CE-geo′).
*Proof.* Φ(z) := log ω(e^{z_1O(f_λ)+z_2O(g_λ)}) is analytic on 𝔻_k and Cov_ω(O(f_λ), O(g_λ)) = ∂_{z_1}∂_{z_2}Φ_c(0) for the doubly
connected part Φ_c(z) := Φ(z) − Φ(z_1, 0) − Φ(0, z_2) + Φ(0, 0). CT drops out of Φ_c (range c_1a < D_−λ); so does every polymer missing
one support. Cauchy on the bidisc: |∂_{z_1}∂_{z_2}Φ_c(0)| ≤ sup_{𝔻_k}|Φ_c|·‖f‖_∞‖g‖_∞/(ε̂_*²u_k²λ⁸). Bound sup|Φ_c| ≤
4Σ_rΣ_{X meets both}A_se^{−κ_sd_r(X)} + A_s. *Levels r < k:* a polymer meeting both supports has d_r(X) ≥ D_−L^{k−r}/M − c_M; at most
C_fL^{4(k−r)} level-r M-cubes meet supp f_λ; Σ_{X∋□}e^{−κ_0d(X)} ≤ K_0^{CE}; summing over r < k gives ≤ A_sK_0^{CE}C_fe^{(κ_s−κ_0)c_M}S_0.
*Levels r ≥ k:* at most c_N level-r M-cubes meet supp f_λ, so each level gives ≤ A_sK_0^{CE}c_N, and there are m + 1 such levels.
(FLOW-pw) with u_K > 0 gives m ≤ (u_k − u_K + R_F)/b_− ≤ (u_k + R_F)/b_−. Hence λ⁸|Cov| ≤ (‖f‖_∞‖g‖_∞/ε̂_*²)·[4A_sK_0^{CE}(C_f e^{…}S_0
+ c_N(1 + (u_k + R_F)/b_−)) + A_s]/u_k² ≤ C_+^{(1)}/u_k (u_k ≥ 1). ∎
*Remark.* κ_e = 1 > 0 is all NONFREE55's Lemma TS and H-RED^e need from the upper half. The coarse levels cost (m + 1)·u_k^{−2} ≍ u_k^{−1}
because the radius is set by the finest relevant level; **no canonical localisation is needed for κ_e = 1.**

**(CSL) [OPEN; tree-level part = SA-E1].** On 𝔻_k, for every r ≥ k, the doubly connected part of the level-r activities obeys
  sup_{𝔻_k}|Σ_{X meets both}[𝔞_r(X; z) − 𝔞_r(X; z_1, 0) − 𝔞_r(X; 0, z_2) + 𝔞_r(X; 0, 0)]| ≤ A_s(u_k/u_r)²L^{−8(r−k)}.
(It holds if each level-r activity depends on z only through a level-r effective source ε̂_r(z) with |ε̂_r| ≤ C(|z_1|‖f‖_1 +
|z_2|‖g‖_1)ℓ_r^{−4}/u_r and is analytic with bound A_s for |ε̂_r| ≤ ε̂_*: then Schwarz's lemma in each variable gives the displayed
factor. Its tree-level instance is SA-E1's canonical bound (§4.3).)
**Theorem TS-up₂ (κ_e = 2). PROVEN as an implication of (SRC-rel) + (CSL) + (FLOW-pw).** W_m ≤ C_+^{(2)}u_{K−m}^{−2}, with
C_+^{(2)} := (‖f‖_∞‖g‖_∞/ε̂_*²)[4A_sK_0^{CE}C_fe^{(κ_s−κ_0)c_M}S_0 + A_sC_SUM^{co}(2) + A_s], C_SUM^{co}(2) := 4/(1 − L^{−8}) + γ⁴T_2/(1 − L^{−8}).
*Proof.* As TS-up₁, with the r ≥ k sum replaced by A_su_k²Σ_{r≥k}u_r^{−2}L^{−8(r−k)} ≤ A_sC_SUM^{co}(2) (Lemma SUM's coarse part, s = 2). ∎

### 5.2 The two-sided bound
**(PL-1L) [OPEN; the named Yang–Mills input of this file].** There are ϑ ∈ (0, 1], A_1 < ∞ and μ_1 ∈ (0, μ_K/2] such that for all
K, R ≥ R_0, m with k = K − m ≥ d_0 and u_k ≥ 2R_F + 2, and every level 0 ≤ i ≤ K:
  **|λ⁸E[Cov(G_i, H_i | U_{i+1})] − Λ_i^{run}| ≤ A_1·ū_i^{−2−ϑ}·𝔭_i(k)**  (i < K),   **|λ⁸Cov(G_K, H_K) − Λ_K^{run}| ≤ A_1·ū_K^{−2−ϑ}·𝔭_K(k)**,
with G_i, H_i the exact images (3.1), Λ_i^{run} the explicit one-loop terms of Proposition GT built from (K-dec)'s slices and the
chain's own u_i, ū_i := u_{max(i,k)}, 𝔭_i(k) as in §3.3. In words: **each RG step's contribution to the e two-point function equals
its one-loop (Gaussian, running-coupling) value up to a relative O(u^{−ϑ}), with the per-step decay across the separation at fine
levels and canonical suppression at coarse levels.** Only the summed consequence |W_m − Σ_iΛ_i^{run}| ≤ A_1C_SUM(2 + ϑ)u_k^{−2−ϑ}
(Lemma SUM) is used below, so a summed form (PL-1L)_Σ suffices for the theorem; the per-level form is the producer-facing one (§6).

**Theorem TS (two-sided asymptotic-freedom bound at n = 2, κ_e = κ_e′ = 2). PROVEN as an implication of (PL-1L), (K-dec),
(FLOW-pw), (LGF).** Let c_bub := 12(N² − 1)/π⁴ and I_8 := ∫∫f(x)g(y)|x − y|^{−8}dxdy. Put
  U_* := max{2R_F + 2, 8C_AF/(c_bubI_8), (8A_1C_SUM(2 + ϑ)/(c_bubI_8))^{1/ϑ}},  m_0 := min{m : g_ref^{−2} + b_−m − R_F ≥ U_*},
and d_0, R_0 as in Lemma FREE (with also L^{d_0} ≥ 4/D_−). Then for every m ≥ m_0, K ≥ m + d_0 and R ≥ R_0,
  **¼·c_bub·I_8·u_{K−m}^{−2} ≤ W_m = λ_m⁸Cov_ω(O(f_{λ_m}), O(g_{λ_m})) ≤ (7/4)·c_bub·I_8·u_{K−m}^{−2}.**
That is (TS-e-low) with κ_e′ = 2, c_− = ¼c_bubI_8, and (TS-e-up) with κ_e = 2, C_+ = (7/4)c_bubI_8, for exactly the clover field
of OSLEAF55's algebra with Z ≡ 1, on F-tune's trajectory, uniformly in K ≥ m + d_0 and R ≥ R_0.
*Proof.* (1) (3.1): W_m = Σ_iλ⁸E[Cov(G_i, H_i|U_{i+1})] + λ⁸Cov(G_K, H_K). (2) (PL-1L) and Lemma SUM (s = 2 + ϑ):
|W_m − Σ_iΛ_i^{run}| ≤ A_1C_SUM(2 + ϑ)u_k^{−2−ϑ}. (3) Proposition GT (b): Σ_iΛ_i^{run} = W^{lead}. (4) (3.4): |W^{lead} − L_free/u_k²| ≤ C_AFu_k^{−3}.
(5) Lemma FREE: ½c_bubI_8 ≤ L_free ≤ (3/2)c_bubI_8. (6) For m ≥ m_0, TR-7 gives u_k ≥ g_ref^{−2} + b_−m − R_F ≥ U_*, so C_AFu_k^{−3} ≤
⅛c_bubI_8u_k^{−2} and A_1C_SUMu_k^{−2−ϑ} ≤ ⅛c_bubI_8u_k^{−2}; add. ∎
**Corollary TS-up (κ_e = 2 from upper bounds only).** If (PL-1L) is weakened to **(PL-up)**: |λ⁸E[Cov(G_i, H_i|U_{i+1})]| ≤
A_up·ū_i^{−2}𝔭_i(k) for every level (and the same for the top term), then W_m ≤ A_upC_SUM(2)·u_k^{−2} under (FLOW-pw) alone (no (K-dec),
no (LGF)). And (PL-1L) ⇒ (PL-up) with A_up := A_1 + A_Λ (Lemma Λ-size). PROVEN.

### 5.3 What the theorems use and do not use; quantifiers
- **Used:** Proposition B (banked); Proposition GT (exact); Lemma KD (pre-S24 lane theorems); Lemmas SUM, AF-cmp, Λ-size (arithmetic of
  FLOW-pw); Lemma FREE (the reviewed scalar/free (LGF) library); the named inputs. **Not used:** e ∝ Θ (CODEX_REVIEW_NONFREE R13: not banked), Lemma V, any
  coincident-point variance, any flowed observable, (ID♮), (MOM-E), any exact one-loop slope (only b_± > 0: the (B-BR)/(UIR^♮_br)
  weakening suffices — the TS bounds are stated in terms of the chain's own u_{K−m}, whatever its slope).
- **Quantifier order** (as H-RED^e needs, CODEX_REVIEW_NONFREE R11): m_0, d_0, R_0 and the constants depend on (N, L, κ, f, g, g_ref,
  b_±, R_F, γ) and on the inputs' constants — never on K or R. For fixed m the bounds hold for all K ≥ m + d_0, R ≥ R_0.
- **Consistency of the two exponents.** κ_e′ ≥ κ_e is forced (Codex R11); Theorem TS gives κ_e = κ_e′ = 2, which is the value
  NONFREE55 §3.3 expected [m] and which is the free-bubble scaling with the running coupling at the matched level.
- **Is the conclusion restated as an input?** (PL-1L) is a per-step statement (each level's contribution vs its one-loop value);
  the theorem's content is the multiscale assembly: the exact per-level identity (GT), the canonical summation (SUM), the
  running-vs-free comparison with only a two-sided bracket on u (AF-cmp), and the exact free coefficient (FREE). That said, I
  agree with the line of Codex reviews that **the substantive asymptotic-freedom work lives in the input** — here, one-loop accuracy
  of each RG step for the e-source plus canonical localisation; §6 says what it reduces to and what is missing.

## §6. The named inputs: exact statements, producers, statuses (brief item 1's input list)

### 6.1 (FLOW-pw) — CONDITIONAL (FLOW)
The pairwise bracket of §3.3 on [0, K] along the trajectory, with u_K − R_F ≥ γ⁻². Producer: FLOW Theorem F-flow ("for all 0 ≤ j ≤ n:
β_−(n − j)log L − R ≤ u_j − u_n ≤ β_+(n − j)log L + R", given (UNIV-1L), (SF-g), (RLF-δ) and g_0, …, g_{n−1} ≤ γ), applied on [0, K]
inside Theorem F-tune (which also needs (SF-cont), (SF-∞)); TR-7 for u_K − R_F ≥ γ⁻². (UNIV-1L) may be replaced by the two-sided
bracket (B-BR) ⇔ (UIR^♮_br) (HINT2_55 Remark B-BR; CODEX_REVIEW_HINT2 bank 3 — agree). OSLEAF55's C-T2 (γ ≤ γ_FI) and C-T3 ((A-Lip)
for (SF-cont) along the A5 sequence) apply. **This file needs only b_± > 0 and R_F < ∞; no exact one-loop slope.**

### 6.2 (K-dec) — PROVEN as an implication of pre-S24 lane theorems (Lemma KD)
LINEAR_PACKAGE Lemmas 2.5, 2.7, 4.4 (frozen v1.1) and PROOF Theorem N5-triv (pre-S24). Not session-24/25 material.

### 6.3 (LGF) — locally proved scalar/free library; independent LAND review
[LGF](LGF.md), equations (1)–(5), (19)–(20), (29)–(32), (37)–(41), supplies
§2.4's exact normalization, infinite-lattice and finite-torus estimates, and
free curvature kernel. [REVIEW_LGF](REVIEW_LGF.md) confirms those statements.
Only FREE consumes this input. No interacting estimate or other TS hypothesis
is discharged by that review.

### 6.4 (PL-1L) — OPEN. What it reduces to (ARGUED, not proven here), and what is missing
(PL-1L) is "each RG step reproduces its one-loop contribution to the e two-point function". It would follow from five per-step
ingredients; I give each with its producer and status. The reduction itself is ARGUED (the algebra of the leading term is
Proposition GT; the error propagation is the standard one, but I have not written it with the non-abelian, background-dependent
and large-field terms, so I do not claim it).
- **(P1) Per-step Gaussian dominance with the e-source as a spectator.** STEP55 Theorem CX (on disk 06:00Z; PROVEN there as an
  implication of (H1)–(H4)): ∫dμ_p(W)e^{−V_int} = exp Σ_YV^#(Y) with |V^#(Y)| ≤ C_1C_locH_Ve^{−(κ_2−3κ_0−3)d(Y)}, jointly holomorphic in
  the source coefficients ε̂ (SRCAN55 §2.1's class), uniformly in level, torus, region and holes; "small iff g_kp_W³ ≪ 1"
  (STEP55 §5.3, row (H2)). Applying Cauchy in the per-step source variables on the per-step relative polydisc turns this into:
  per-step covariance of the e-images = its Gaussian (one-loop) value + a remainder of relative size O(H_V) = O(u_i^{−1/2}p_W³),
  with the polymer decay across the separation. This gives **ϑ = ½ − 0** (up to the polylogarithm p_W³). Status: Theorem CX's
  hypotheses at levels ≥ 1 are CONDITIONAL/OPEN in STEP55's own table ((H1) at chart backgrounds ⟸ (HC_k) + (B2); (H2)'s inherited
  polymers OPEN (I6); Faddeev–Popov/Haar local expansion ARGUED). STEP55 is running and not Codex-reviewed: **NOT-VERIFIED here.**
- **(P2) Background dependence of the per-step covariance.** The Gaussian part at a small-field background V versus the trivial
  one: relative O(|curvature(V)|) = O(g_i) on typical backgrounds; level 0: PROOF Theorem N5-sf0 (pre-S24); levels ≥ 1: STEP55
  Proposition 1S-k, CONDITIONAL. OPEN at levels ≥ 1.
- **(P3) Image structure and canonical localisation (IMG)/(CSL).** G_i = (tree-level quadratic image) + const + (fluctuation
  corrections of relative size O(u_i^{−ϑ}) that scale canonically). Tree level: the quadratic image of a level-i field B_i is
  Σ_aΣ_pw_f(p)(L^{−2i}(𝒦^{ax}_{u(p)}dB^a_i)(p))² (LINEAR_PACKAGE Lemma 4.4); at constant coarse curvature F it equals the canonical
  level-i density with **coefficient exactly 1** (the zero-residual chain B_{j+1} := ∫_{S_c}B_j is critical — Lemma 2.3 (ii) gives
  QB_j = ∫_{S_c}B_j at constant curvature, so every r_j = 0 and the Euler–Lagrange equations of Lemma 3.1 hold since d*F = 0 —
  hence f_0 = F); its canonical size bound is SA-E1 (banked, CONDITIONAL on BFT-E). Fluctuation part: (LOC-e)-type, **OPEN**
  (CODEX_REVIEW_SRCAN item 9).
- **(P4) Leading-order coarse curvature two-point function (PS-lin).** E[c_pc_q] (paired gauge-covariantly) = 𝔊^run_{>i}(p,q)(1 +
  O(u^{−ϑ})) at separated p, q: Proposition B applied to the LINEAR images, top-down, from (P1)+(P2) for linear observables. ARGUED
  (an induction over levels that I have not written out).
- **(P5) Large fields (LF-dec), in the form this file needs:** Σ_{i≤K}|λ⁸E[Cov(G_i, H_i|U_{i+1}); 𝔏_i]| ≤ A_LF·u_k^{−2−ϑ}, where 𝔏_i
  is the event that a large-field cube of level ≤ i + 1 within distance ρ_i ≍ ℓ_{i+1} of supp f_λ ∪ supp g_λ, or a small-field cut
  failure of step i there, occurs. NONFREE55's polymer form ("at most Cλ⁻⁸θ(ℓ_j/λ)e^{−cp(g_j)²}", λ ≥ ℓ_j) implies the levels-≤-k part
  if the per-level factor is e^{−c(log(1/g_j))^{2p}} with **2p > 1** (superpolynomial in u_j, summable over the ≍ u_k/b_− levels with
  room to spare), or with 2p = 1 and **c > 6 + 2ϑ** (CODEX_REVIEW_NONFREE R1's corrected threshold c > 6, sharpened by the extra
  u_k^{−ϑ} that the lower bound needs: Σ_n(u_k + b_−n)^{−c/2} ≍ u_k^{1−c/2} ≤ u_k^{−2−ϑ} iff c ≥ 6 + 2ϑ). Levels > k additionally need the
  canonical factor L^{−8(i−k)}, which NONFREE55's statement (λ ≥ ℓ_j only) does not cover — **an amendment to NONFREE55's (LF-dec)**.
  The decoupling mechanism (no inverse power of ℓ_j/λ) is NONFREE55 §6.3's ARGUED one. **OPEN.**
**Summary for (PL-1L):** OPEN; ⟸ (P1)–(P5) [ARGUED]; the hard items are (P3)'s fluctuation part (canonical localisation, the same
object as SRCAN55's (LOC-e)), (P5), and Theorem CX's hypotheses at levels ≥ 1.

### 6.5 (SRC-rel) and (CSL) — OPEN; relation to SRC2_55
(SRC-rel) is SRC2_55's target T1 (source-inserted multiscale polymer representation with decaying activities) **with two changes**:
the source polydisc in relative units (radius ε̂_*u_kλ⁴ for sources at scale λ, i.e. a fixed fraction of the running coupling at the
source's scale), and U_K integrated with only the mixed part of the IR remainder bounded. Tree level up to depth K − m: SA-K (banked,
conditional) is in the right class (§4.4 (b)). Large fields: SRCCD55's SRC-κ-LF/SRC-I structure, with the relative radius. (CSL) is
the coarse-level canonical localisation (§4.3; tree level = SA-E1). **Coordination note for SRC2_55** (not a claim about its
results): T1 with an absolute radius gives OSLEAF55's (X1) but, by §4.4 (a), no AF envelope; if T1's radii can be taken relative
(∝ the running coupling at the source's scale), Theorem TS-up₁ turns it into (TS-e-up) with κ_e = 1 at no extra cost.

### 6.6 What is NOT an input (so nobody needs to supply it)
Any lower bound on an e-correlator (the lower bound is produced by Theorem TS from the explicit leading term); Lemma V (§4.1);
e ∝ Θ (§5.3); any statement about flowed fields; an exact one-loop slope; positivity of per-level contributions (they have no sign,
ts55_2); D_− large.

## §7. T_NF for every limit point, as an implication with every input named (brief item 3)

### 7.1 The statement
**Theorem T_NF^e (CONDITIONAL; PROVEN as an implication).** Let ω_j := ω_{K_j,R_j} (K_j → ∞, R_j ≥ R_0) be Wilson measures on
F-tune's trajectory at fixed g_ref ∈ (0, g_sink], with lattice functionals S^{(j)} of OSLEAF55 D8 for the clover field e_a with
Z ≡ 1, and let S be any limit point along a subsequence on which the values S^{(j)}_2(f_{λ_m}⊗g_{λ_m}) converge for every m
(guaranteed by (H_reg-sep) via CLOSURE-sep (a) and the dense-family extension — OSLEAF55 Theorem ALG (iii), CODEX_REVIEW_NONFREE R11).
Assume (FLOW-pw) [with TR-7], and either
  (A) (PL-1L) + (K-dec) + (LGF)  — then Theorem TS gives both halves with κ_e = κ_e′ = 2; or
  (B) for the upper half (SRC-rel) [Theorem TS-up₁, κ_e = 1] and for the lower half (PL-1L) + (K-dec) + (LGF) [Theorem TS].
Then the separated two-point function of S satisfies (AF-e) along λ_m, and hence **S is neither realisable by a nonnull Hermitian
scalar finite Wick polynomial (finitely many derivatives) in finitely many canonical free fields, nor by a finite mixture or an
(ENV)-mixture of such** (the declared class, with CODEX_REVIEW_NONFREE's repairs: masses may enter the leading term; connected
mixtures carry the variance term Var_ν(μ_α)).
*Proof.* Theorem TS (or TS-up₁ + TS) gives (TS-e) for m ≥ m_0, K ≥ m + d_0, R ≥ R_0 with constants independent of K, R. Lemma TS
(re-derived in §7.2) turns this into (TS-e°). H-RED^e (re-derived in §7.2) passes each fixed-m bound to S and gives (AF-e).
Corollary SEP-e (CODEX_REVIEW_NONFREE bank 1, PROVEN with the repairs) gives the conclusion. ∎

### 7.2 Re-derivations of the two NONFREE55 links used (both CONFIRMED)
- **Lemma TS** ((TS-e) + F-tune ⇒ (TS-e°)). TR-7: U_−(m) := g_ref^{−2} + b_−m − R_F ≤ u_{K−m} ≤ U_+(m) := g_ref^{−2} + b_+m + R_F, uniformly
  in K, R. Upper: λ_m⁸W-value ≤ C_+u_{K−m}^{−κ_e} ≤ C_+U_−(m)^{−κ_e} → 0 since b_− > 0. Lower: λ_m^{8−η}(…) = L^{ηm}·W_m ≥ L^{ηm}c_−U_+(m)^{−κ_e′} → ∞
  for every η > 0 (exponential beats polynomial). ∎ CONFIRMED (agrees with CODEX_REVIEW_NONFREE R11, incl. its symbol pin g = g_FLOW).
- **H-RED^e.** Fix m. The (TS-e) bounds hold for all K ≥ m + d_0, R ≥ R_0; along the subsequence the single value
  S^{(j)}_2(f_{λ_m}⊗g_{λ_m}) = W_m(ω_j)/λ_m⁸ converges (f_{λ_m}⊗g_{λ_m} ∈ 𝒟_2 — smooth, compact support off the diagonal — and for Z = 1
  its lattice value is exactly the covariance, §1.2), so the bounds pass to S. Only then let m → ∞. No exchange of limits, no
  uniform-in-m rate. ∎ CONFIRMED (agrees with Codex R11's quantifier analysis).

### 7.3 Every input of T_NF^e, with status (as of this file; nothing here is banked until Codex reviews it)
| input | statement (locator) | status | producer / owner |
|---|---|---|---|
| Theorem FS + Corollary SEP-e (repaired) | NONFREE55 §3.1–§3.2 + CODEX_REVIEW_NONFREE R2, R3, R10 | **PROVEN** (Codex bank 1) | NONFREE55 |
| H-RED^e, Lemma TS | NONFREE55 §3.3 | **PROVEN implications** (Codex bank 2; re-derived §7.2) | NONFREE55 |
| (H_reg-sep) convergence on {f_{λ_m}⊗g_{λ_m}} | OSLEAF55 CLOSURE-sep, Theorem EXT, (X0)+(X1) | **OPEN** ((X1) is SRC2_55's target) | SRC2_55 / OSLEAF55 |
| (FLOW-pw) + TR-7 | FLOW Theorems F-flow, F-tune; OSLEAF55 TR-4…TR-7, C-T2, C-T3 | **CONDITIONAL** on (UNIV-1L) or (B-BR) [⇔ (UIR^♮_br)], (SF-g), (RLF-δ), (SF-cont), (SF-∞), (A-Lip) | FLOW / UIR |
| Proposition B | SRCCD55 §4 | **PROVEN** ([S26-BANKED]; re-derived §3.1) | — |
| Proposition GT, Lemmas SUM, AF-cmp, Λ-size, FINE, LV-sep | this file §2.3, §3.3–§3.5, §4.1–§4.2 | **PROVEN-HERE** (checks ts55_2, ts55_3) | this file |
| exact coefficient c_bub = 12(N² − 1)/π⁴ | this file §2.4 | **PROVEN-HERE** (ts55_1; agrees with nf55_a and Codex R8/R13) | this file |
| (K-dec) | Lemma KD (§3.2) | **PROVEN as implication of pre-S24 lane theorems** (LINEAR_PACKAGE 2.5, 2.7, 4.4; PROOF N5-triv) | LINEAR_PACKAGE / PROOF |
| (LGF) | §2.4 | **Locally proved scalar/free library; independent LAND review** | [LGF](LGF.md), [review](REVIEW_LGF.md) |
| **(PL-1L)** | §5.2 | **OPEN**; ⟸ (P1)–(P5) **ARGUED** (§6.4) | STEP55 (P1, P2), SRC2_55/LOC-e (P3), (P4) induction, LF (P5) |
| (SRC-rel) [route (B) upper half only] | §5.1 | **OPEN** | SRC2_55 T1 in relative-radius form |
| (CSL) [only for κ_e = 2 via route (B)] | §5.1, §4.3 | **OPEN**; tree level = SA-E1 (banked, conditional on BFT-E) | SRC / LOC-e |
| (LF-dec) [inside (PL-1L) and (SRC-rel)] | §6.4 (P5), amending NONFREE55 §6.4 | **OPEN** (thresholds per Codex R1) | large-field lane |
**The single most dangerous item** (agreeing with CODEX_REVIEW_NONFREE's closing line): (TS-e-low) at every short scale. In this
file it is reduced, by a complete argument, to (PL-1L); the irreducible content of (PL-1L) is per-step one-loop accuracy for the
e-source **together with canonical localisation of the e-images above the source scale (P3) and large-field decoupling (P5)** —
§4.3 shows the canonical-localisation part cannot be dropped by any per-level route.

## §8. Verdicts on inherited claims this file touches (REVIEW_BRIEF_55 order; refutations count as much as confirmations)

- **V1 — NONFREE55 §3.3 Lemma TS** ("(TS-e) + (F-tune) ⇒ (TS-e°)"): **CONFIRMED** (re-derived §7.2).
- **V2 — NONFREE55 §3.3 Theorem H-RED^e**: **CONFIRMED** as an implication (re-derived §7.2; agree with CODEX_REVIEW_NONFREE R11,
  including its quantifier order and its pin g = g_FLOW in F-tune).
- **V3 — NONFREE55 §3.3 "Expected values [m]: κ = κ′ = 2 … W_λ ≈ (12(N² − 1)/π⁴)u(λ)^{−2}∫∫fg|x − y|^{−8}"**: **CONFIRMED as the
  leading term**, now as Theorem TS's content conditional on (PL-1L) + (K-dec) + (FLOW-pw) + (LGF), with u(λ) made precise: the
  chain's own effective coupling at the matched level K − m (any two-sided bracket on it suffices; the exact slope never enters).
  The coefficient 12(N² − 1)/π⁴ is re-derived by a third independent route (§2.4, ts55_1).
- **V4 — NONFREE55 §3.3 "(TS-e-up) is (κ-1) at n = 2 sharpened to an asymptotic-freedom envelope"**: **CONFIRMED, with a
  correction of mechanism**: the envelope is produced by the *relative* source polydisc (radius ∝ u_{K−m}), not by sharpening the
  weight 𝔤_e of SRC-κ as stated with SRCCD55's fixed radius r_0 — that radius gives W_m ≲ m (§4.4 (a)). With the relative radius,
  κ_e = 1 follows from (SRC-rel) alone (Theorem TS-up₁); κ_e = 2 needs (CSL) (Theorem TS-up₂) or (PL-up).
- **V5 — SRCAN55 Lemma SA-E1 (+ E2; Codex sign E_tree = −∂_zS_tree)**: **CONFIRMED** (re-derived the constant: Σ_p|h_□| ≤ ½·24·Σ_x|h| =
  12|supp h|a^{−4}, s ≤ |X|_op²/2, own plaquette logs ≤ L^{−2K}(2η_b + 9η_b²) by BA-3 [an input I did not re-verify], a^{−4}L^{−4K} =
  ℓ_ref^{−4}: 12·½ = **6**). Role clarified: it is the tree-level part of (CSL) (canonical scaling of images above the source scale,
  §4.3); it is an upper bound and cannot supply the leading term's value or sign. The exact tree-level quadratic image (with
  coefficient exactly 1 at zero coarse momentum) is §6.4 (P3).
- **V6 — SRCAN55 Proposition SA-K** (banked, tree level, ‖·‖_cf class on 𝒞_glob): scope **CONFIRMED with a limitation**: for sources
  concentrated at scale λ it applies at depth K − m, not at depth K (§4.4 (b)); consistent with CODEX_REVIEW_SRCAN item 10.
- **V7 — SRCCD55 Lemma V** (banked): the lemma is not re-derived here (I read its full proof and agree with its structure); its
  **mechanism gives exactly zero at separated points** (Proposition LV-sep, §4.1). So the brief's suggestion that it might give
  (TS-e-low) is answered **negatively** (pre-stated R5 realised).
- **V8 — NONFREE55 §6.4 (LF-dec)**: **CONFIRMED as the right type of input**, **with two amendments**: Codex R1's threshold (2p > 1, or
  c > 6 at 2p = 1 — I agree, and the lower bound needs c ≥ 6 + 2ϑ), and levels above the source scale (ℓ_j > λ) also need the
  canonical factor (λ/ℓ_j)⁸, which NONFREE55's statement (λ ≥ ℓ_j only) omits (§6.4 (P5)).
- **V9 — NONFREE55 §3.3 "By-product: (TS-e-low) at one fixed m supplies ROTDEF §2.2's missing non-vacuity guard … with Z_e ≡ 1"**:
  **CONFIRMED** (a reflected pair f, θf with f ≥ 0 supported in {t > a} is an admissible pair; Theorem TS at m = m_0 gives a bound
  ≥ ¼c_bubI_8U_+(m_0)^{−2} > 0 uniformly in K, R — conditional on Theorem TS's inputs).
- **V10 — The brief's structural claim** (item 2: leading term = "the tree/one-loop image of e at the level-(K−m) background";
  remainder "smaller by a power of the running coupling"): **REFUTED as literally stated** (Proposition FINE: with the level-(K−m)
  image alone, the remainder contains u_k^{−2}Φ_fine, the fine levels' one-loop source–source term, which is coupling-independent
  relative to the leading term and nonzero in toys); **CONFIRMED after correction**: leading term = the full one-loop bubble with
  running couplings, W^{lead} (Proposition GT), whose value is u_{K−m}^{−2}·L_free·(1 + O(u_{K−m}^{−1})) (Lemma AF-cmp).
- **V11 — HINT2_55 R2.4 "(TS-low): (SRC) at the coarse level plus anti-concentration of the level-k₀ fluctuation (its Gaussian part
  must dominate)"**: **CONFIRMED in spirit** for the new witness: (PL-1L) is exactly "Gaussian part dominates, step by step", plus
  canonical localisation (§4.3), which HINT2 did not list.
- **V12 — STEP55 Theorem CX and its (H2) row "small iff g_kp_W³ ≪ 1"**: **used only as the producer of ϑ ≈ ½** in the ARGUED
  reduction (§6.4 (P1)); **NOT-VERIFIED** here (STEP55 running, no Codex review on disk at 06:20Z).
- **V13 — OSLEAF55 TR-7 and FLOW Theorem F-flow's pairwise bracket**: the statements are as quoted (re-read); **CONFIRMED as
  conditional statements**; their inputs are not re-verified here.

## §9. Checks (criteria before scripts; exact arithmetic; all runs `nice -n 10 python3 -I`)
| id | criteria / script / output (UTC from `date -u`) | result | could it fail? what does it NOT decide? |
|---|---|---|---|
| ts55_1 | criteria completed 06:08:21Z; script written and run 06:08:51Z; `ts55_1_out.txt` | **PASS**: A1 (closed form and 384 at 8 rational points), A2 (identity in d = 3; 384 fails at 6/6 points there), A3 (unordered = ¼), A4 (both routes 12), A5 (generators; ½Σ(F^a)²); controls A1-F (wrong closed form differs at 8/8), A4-F (3 ≠ 12), A5-F (6/6 differ) fired | Yes: T comes from a generic quotient rule, S by brute force over 256 index tuples; a wrong tensor identity, coefficient or generator normalisation fails. It does not test (LGF) or anything Yang–Mills |
| ts55_2 | criteria completed 06:08:21Z; script written and run 06:09:38Z; `ts55_2_out.txt` | **PASS**: G1 (12 models: brute-force per-level values = Λ_i, sum = bubble), G3 (u²·FINE_2 u-independent, nonzero 12/12, negative in some); controls G1-F (4 → 2 breaks 12/12), G2-F (no top term breaks 12/12) fired | Yes: per-level values come from exact Gaussian moments of explicit polynomials, not from the formula. It tests Gaussian identities only, not (PL-1L) |
| ts55_3 | criteria completed 06:08:21Z (S2-F clarified in the criteria file before any script); script written and run 06:10:51Z; `ts55_3_out.txt` | **PASS**: S1, S2 on 126 admissible synthetic sequences × 12 levels × three (b_−, b_+, R_F) sets; controls S1-F (595 > 10) and S2-F (1573.7 > 11.3) fired | Yes: wrong constants or a wrong O(u_k^{−s}) claim would fail. **Disclosed deviation:** S3's pre-registered weight ω_n = L^{4n}2^{−L^n} is not representable exactly for n ≥ 7 (2^{−3^n}), so S3 was evaluated termwise with both sides truncated at n ≤ 6; the lemma's fine-side step is termwise, so the truncation tests the same inequality, but S3 is weak (it can fail only if u_{k−n} < u_k/2, i.e. if the bracket were violated). It does not test that Yang–Mills obeys (FLOW-pw) |
*What no check here tests:* (LGF); Lemma KD's imported constants; any Yang–Mills input ((PL-1L), (SRC-rel), (CSL), (LF-dec)); the ARGUED
reduction of §6.4.

## §10. Errata to this file (append-only; each overrides the text it names; found on a full re-read at ≈06:23Z)
- **E1 (§1.4, row "SRCAN item 9").** "(CSL) of §6.3" → read "(CSL) of §4.3, stated in §5.1 and §6.4 (P3)". (§6.3 is (LGF).)
- **E2 (§4.3, first paragraph).** "Their natural per-level size is λ⁸u_i^{−2}ℓ_i^{−8}λ⁸… — precisely," → read "Their natural per-level
  size is as follows:". The displayed conclusion λ⁸·(…) = O(L^{−8(i−k)}u_i^{−2}) is unchanged.
- **E3 (§3.3 control S1-F, and §4.3 "Obstruction").** "it grows like u_k/b_−" is wrong. Correct: Σ_{n=0}^{m}u_{k+n}^{−2} ≈
  ∫_{u_K}^{u_k}du/(b_−u²) → (b_−u_K)^{−1} — **the sum itself tends to a positive constant**, so u_k²·Σ grows like u_k²/(b_−u_K) (check:
  16.83²·(4(1/1.833 − 1/16.83) + 0.15) ≈ 595, the recorded S1-F value). The conclusion (no envelope without canonical decay) is
  unchanged and is in fact stronger than stated.
- **E4 (§7.2, Lemma TS).** "λ_m⁸W-value ≤ C_+u_{K−m}^{−κ_e}" → read "W_m ≤ C_+u_{K−m}^{−κ_e}" (W_m already contains λ_m⁸).
- **E5 (§6.4, addition to (P1)/(P2)) — coupling identification.** (PL-1L) also needs the per-step Gaussian part at level i to carry
  the coupling u_i up to a relative O(u_i^{−ϑ}): the effective action's quadratic coefficient is the chain's own u_i (TR-3), and the
  kernel stiffness is κu^{ker}_{i+1} with u^{ker}_{i+1} = u_i − b_i − ρ_i (TR-2, A5/FI-1), which differs from u_i by b_i = O(1), i.e. by a
  relative O(u_i^{−1}). So this costs nothing beyond (FLOW-pw) and FI-1's existence (CODEX_REVIEW_RLU item 2, conditional), but it is
  an ingredient and is listed here as **(P6)**. A relative O(1) mismatch would change the leading coefficient, not only the remainder.

## §11. Summary table — every claim of this file and every inherited claim touched, with its label / verdict

**11.1 Claims of this file**
| # | claim (section, locating string) | label |
|---|---|---|
| 1 | The object: W_m for ROTDEF's e_a, OSLEAF55 D8 with Z ≡ 1, F-tune's trajectory, matched level k = K − m; coupling dictionary g_std = √(2N)g_FLOW (§1.2–§1.3) | definition (coordinator's request met) |
| 2 | O(f) = Σ_ph^f_□s(U_p); quadratic part Σ_aΣ_pw_f(F^a_p)², w_f = ¼Σ_corners f (§2.1) | PROVEN-HERE (ts55_1 A5) |
| 3 | Curvature chain F_{i+1} = Q_2F_i + dξ_i/√κ is Markov; Σ_i𝔎_i = P_ex exactly; 𝔎_i = level-i fluctuation in the fine curvature (§2.2) | PROVEN-HERE |
| 4 | Proposition GT: per-level one-loop terms Λ_i^{run} sum exactly to the running bubble W^{lead}; per-level terms have no sign (§2.3) | PROVEN-HERE (ts55_2) |
| 5 | Σ_{μνρσ}X² = (4d − 8)tr T² + 4(tr T)²; Σ_{μ<ν,ρ<σ}D² = 6/(π⁴r⁸); c_bub = 12(N² − 1)/π⁴ (§2.4) | PROVEN-HERE (ts55_1; third independent route) |
| 6 | (LGF) (§2.4) | Locally proved scalar/free library; independent LAND review ([LGF](LGF.md), [review](REVIEW_LGF.md)) |
| 7 | Lemma FREE: ½c_bubI_8 ≤ L_free ≤ (3/2)c_bubI_8 for K − m ≥ d_0, R ≥ R_0 (§2.4) | PROVEN-HERE given (LGF) |
| 8 | Lemma KD = (K-dec) (§3.2) | PROVEN as an implication of LINEAR_PACKAGE 2.5/2.7/4.4 + PROOF N5-triv (pre-S24) |
| 9 | Lemma SUM (§3.3) | PROVEN-HERE (ts55_3 S1, control fired) |
| 10 | Lemma AF-cmp and (3.4): |W^{lead} − L_free/u_k²| ≤ C_AFu_k^{−3} with only a two-sided bracket on u (§3.4) | PROVEN-HERE (ts55_3 S2/S3, control fired) |
| 11 | Lemma Λ-size (§3.5) | PROVEN-HERE |
| 12 | Proposition LV-sep: Lemma V's mechanism gives exactly 0 at separated points (§4.1) | PROVEN-HERE (pre-stated R5 realised) |
| 13 | Proposition FINE: the level-(K−m) image alone is not the leading term; the fine one-loop source–source term is u_k^{−2}·Φ_fine, not coupling-small (§4.2) | PROVEN-HERE (structure); nonvanishing shown in toys (ts55_2 G3), ARGUED generic for the lane chain |
| 14 | Canonical localisation (CSL) is necessary for any per-level route to κ_e = 2 or (TS-e-low) (§4.3, with E3) | PROVEN-HERE (route obstruction + abstract example); its mechanism ARGUED |
| 15 | Fixed absolute source radius ⇒ W_m ≲ m, no envelope; relative radius ∝ u_k needed (§4.4 (a)) | PROVEN-HERE |
| 16 | SA-K at depth K forces radius ∝ λ^{4+α} (fatal); at depth K − m the relative polydisc is in SA-K's class (§4.4 (b)) | PROVEN-HERE (seminorm arithmetic) |
| 17 | Theorem TS-up₁: (SRC-rel) + (FLOW-pw) ⇒ (TS-e-up) with κ_e = 1 (§5.1) | PROVEN implication |
| 18 | Theorem TS-up₂: + (CSL) ⇒ κ_e = 2 (§5.1) | PROVEN implication |
| 19 | **Theorem TS: (PL-1L) + (K-dec) + (FLOW-pw) + (LGF) ⇒ ¼c_bubI_8u_{K−m}^{−2} ≤ W_m ≤ (7/4)c_bubI_8u_{K−m}^{−2} for m ≥ m_0, K ≥ m + d_0, R ≥ R_0** (§5.2) | PROVEN implication |
| 20 | Corollary TS-up: (PL-up) + (FLOW-pw) ⇒ κ_e = 2; (PL-1L) ⇒ (PL-up) (§5.2) | PROVEN |
| 21 | (PL-1L) ⟸ (P1)–(P6) (§6.4 + E5) | ARGUED (not proven) |
| 22 | Tree-level image at constant coarse curvature = canonical density with coefficient exactly 1 (§6.4 (P3)) | PROVEN-HERE (from LINEAR_PACKAGE Lemmas 2.3 (ii), 3.1; constant mode taken formally in infinite volume) |
| 23 | Large-field thresholds for the lower bound: 2p > 1, or c ≥ 6 + 2ϑ at 2p = 1; coarse levels need (λ/ℓ_j)⁸ (§6.4 (P5)) | PROVEN-HERE (arithmetic); amendment to NONFREE55 §6.4 |
| 24 | Theorem T_NF^e: every limit point of the Z ≡ 1 clover theory on TR is not realisable in the declared finite canonical-free class (nor finite / ENV mixtures), given the inputs of §7.3 (§7.1) | PROVEN implication; CONDITIONAL |
| 25 | Named inputs: (PL-1L), (SRC-rel), (CSL), (LF-dec) | OPEN |
| 26 | (FLOW-pw) + TR-7 | CONDITIONAL (FLOW F-flow/F-tune inputs) |

**11.2 Inherited claims touched (verdicts of §8)**
| item | verdict |
|---|---|
| V1 NONFREE55 Lemma TS | CONFIRMED |
| V2 NONFREE55 H-RED^e | CONFIRMED (agree Codex R11) |
| V3 NONFREE55 expected κ = κ′ = 2 and W ≈ (12(N² − 1)/π⁴)u^{−2}I_8 | CONFIRMED as the leading term (Theorem TS, conditional) |
| V4 NONFREE55 "(TS-e-up) is (κ-1) at n = 2 with an AF envelope" | CONFIRMED with corrected mechanism (relative radius) |
| V5 SRCAN55 SA-E1 (+E2, Codex sign) | CONFIRMED (constant 6 re-derived; BA-3 input not re-verified); role = tree-level (CSL) |
| V6 SRCAN55 SA-K scope for λ-sources | CONFIRMED with a limitation (depth K − m only) |
| V7 SRCCD55 Lemma V | NOT-VERIFIED here as to its own proof/constants (read, not re-derived; banked by Codex); its mechanism answered NEGATIVELY for separated points |
| V8 NONFREE55 §6.4 (LF-dec) | CONFIRMED as the input type, with two amendments (Codex R1 threshold; coarse-level canonical factor) |
| V9 NONFREE55 "(TS-e-low) at one m supplies ROTDEF's non-vacuity guard with Z_e ≡ 1" | CONFIRMED (conditional on Theorem TS's inputs) |
| V10 the brief's item-2 structure (level-(K−m) image + coupling-small remainder) | **REFUTED as literally stated**; CONFIRMED after correction (full one-loop bubble) |
| V11 HINT2_55 R2.4 "(TS-low) needs Gaussian-part dominance" | CONFIRMED in spirit (plus canonical localisation) |
| V12 STEP55 Theorem CX / "small iff g_kp_W³ ≪ 1" | NOT-VERIFIED (running file, no Codex review) — used only as the ARGUED producer of ϑ ≈ ½ |
| V13 OSLEAF55 TR-7 / FLOW F-flow pairwise bracket | CONFIRMED as conditional statements (re-read) |

## §12. For the lead (what should change in PROOF.md's tally / HANDOFF's critical path — recommendations; this worker edits neither)
1. **H_int's Yang–Mills side is now one named input.** (TS-e-up) and (TS-e-low) — for exactly the Z ≡ 1 clover field of OSLEAF55's
   algebra — follow, by a complete argument (Theorem TS), from **(PL-1L)** (per-step one-loop accuracy for the e-source, with
   per-step decay at fine levels and canonical suppression at coarse levels) plus linear/flow inputs that are pre-S24 lane theorems
   ((K-dec)), FLOW's conditional bracket ((FLOW-pw)) and the reviewed scalar/free lattice library (LGF). The upper half alone, with κ_e = 1
   (enough for H-RED^e), follows from **(SRC-rel)** — SRC2_55's target in relative-radius form — with no one-loop computation.
2. **Critical-path merge.** (PL-1L)'s irreducible pieces are (P3) canonical localisation of e-images above the source scale and (P5)
   large-field decoupling. (P3) is the same object as SRCAN55's (LOC-e) (the OS0 singleton, CODEX_REVIEW_SRCAN item 9). So the OS0
   singleton leaf and the non-freeness lower-bound leaf share **one** missing estimate; HANDOFF should list it once.
3. **Remove two hopes from any plan:** Lemma V's mechanism cannot give (TS-e-low) (Proposition LV-sep: it gives exactly 0 at
   separated points); and the "tree-level image at level K − m + coupling-small remainder" structure is false as stated
   (Proposition FINE) — the leading term is the full one-loop bubble (Proposition GT), whose value u_{K−m}^{−2}·L_free(1 + O(u^{−1}))
   needs only a two-sided bracket on the flow (Lemma AF-cmp).
4. **Coordination with SRC2_55.** An absolute source radius gives (X1) but no AF envelope (§4.4 (a)); if T1's radii are relative
   (∝ the running coupling at the source's scale), Theorem TS-up₁ gives (TS-e-up) immediately. SA-K must be applied at depth K − m for
   such sources (§4.4 (b)).
5. **NONFREE55 §6.4 (LF-dec)** should carry Codex R1's threshold (2p > 1, or c ≥ 6 + 2ϑ at 2p = 1 for the lower bound) and a
   canonical factor for levels above the source scale (§6.4 (P5)).
6. **Tally.** Nothing here moves the 105-item tally: every new item is a lane-level lemma or a conditional implication; the
   Yang–Mills inputs ((PL-1L), (SRC-rel), (CSL), (LF-dec)) are OPEN. Nothing should be banked before the Codex review.

**End of TSE55 (worker claude-opus-5-5).**

**Errata appended after §12 (append-only):**
- **E6 (§7.3 table, row (PL-1L); §6.4 "Summary for (PL-1L)").** "⟸ (P1)–(P5)" → read "⟸ (P1)–(P6)" (E5 adds the coupling
  identification (P6)).
- **E7 (§7.1, route (B)).** Route (B) still needs (PL-1L) for the lower half, so it is not weaker than (A) for T_NF^e; it matters
  only when (TS-e-up) is wanted on its own (then (SRC-rel) suffices, with κ_e = 1, consistent with κ_e′ = 2 ≥ κ_e as Codex R11 requires).
- Final append 2026-10-29T06:2xZ (see the `date -u` stamp of the reply); the file ends here.
- **E8.** "06:2xZ" in the line above: the E6/E7 append ran at 2026-10-29T06:24:49Z (`date -u` immediately after it); this line was appended at 2026-10-29T06:24:55Z. **End of TSE55 (claude-opus-5-5).**
