Reviewer model: claude-opus-5-5

# HIGHER55 — the higher-order exact-source estimates for the gauge-invariant half of BFT-5 clause (b)

UTC start: 2026-10-29T00:15:57Z
Worker scope: WRITE ONLY this file and `checks/hg55_*`. No git.

## PRE-STATED (written before any derivation; statements only)

Targets.
- T1. From `CODEX_REVIEW_TR.md` (item 5) and `CODEX_REVIEW_TOPCC.md` (item 4), read in full as on disk now,
  state verbatim-anchored and precisely: (a) what object S_full is (the actual critical-point source at
  all orders), (b) the decomposition it must admit (composite-co-closed; (CC-0) at critical points is
  banked REFUTED, so no stronger co-closedness may be assumed), (c) the norm Ñ_Σ exactly as Codex
  defines it (file + locating string), (d) the inequality Ñ_Σ(S_full) ≤ C_* η² and the quantifiers
  (uniform in k, T; fields in ‖x‖_𝔐 ≤ C_0 η; m = 0; trivial background).
- T2. Prove (or fail to prove, with the exact missing step named) that the cubic-and-higher part
  R_{≥3} := S_full − S_lin − S_quad of the critical-point source satisfies a bound of the form
  Ñ_Σ(R_{≥3}) ≤ C η³ (hence ≤ C_* η² for η small), with C independent of k and T, using: analyticity in a
  complex ball + Cauchy estimates, the banked transport bound (TR-1), and the lane's existing
  second-order source lemmas (as listed in `KFACTOR_O55.md`). Three nonlinear sources must each be
  covered: BCH beyond second order, Wilson-action nonlinearity, soft-term nonlinearity.
- T3. Decide whether the level sum stays O(η²) uniformly in k, i.e. whether the higher-order terms
  carry level-to-level decay (a per-level geometric factor) or only a per-level O(η³) bound (which
  would reintroduce a factor k unless k η ≲ 1 or a decay is shown).
- T4. Conclude: whether full nonlinear COF-crit, NCE (i) and Corollary CC-CRIT are proven conditional on
  named banked inputs, and whether the gauge-invariant half of clause (b) at the trivial background,
  m = 0, is complete nonlinearly. Anything missing is to be stated precisely as a first-class result.

What would count as a refutation (of the positive claim "higher-order source estimate holds uniformly"):
- R1. An explicit admissible configuration family in the small ball (or an exact identity) for which
  Ñ_Σ(R_{≥3}) grows with k or with T at fixed η, or is not O(η³) / not ≤ C_* η².
- R2. A structural obstruction: R_{≥3} (or S_full) fails to be composite-co-closed in the sense Ñ_Σ
  requires, or its decomposition needs an input that is not banked.
- R3. The Ñ_Σ norm contains a weight or a dual/negative-order component that analytic-ball Cauchy
  estimates on the action cannot control (e.g. a norm on the co-closed part that is not dominated by a
  sup/analytic norm of the remainder), so the method T2 cannot apply in principle.
- R4. A higher-order term that is non-decaying across levels (no per-level contraction), so that the
  level sum of per-level O(η³) bounds yields k·η³ and uniformity in k fails without an additional
  input.
Any of R1-R4, if found, is reported as the result, with the correct statement.

---

## §0. Read record (appended 2026-10-29T00:58Z UTC; everything located by string)

- **CODEX_REVIEW_TR.md** (284 lines, whole; complete — ends with "Exactly what may be banked", item 6; SHA-256 4899db7f…ff37,
  equal to the hash CODEX_REVIEW_TOPCC records for it). **CODEX_REVIEW_TOPCC.md** (363 lines, whole; complete — ends with
  "Exactly what may be banked", item 5).
- **PROOF.md** l.1-60 (header incl. "[S26-BANKED]"); l.3203-3240 ("Lemma NA-alg"); l.5520-5545 ("Lemma N5-an").
- **KFACTOR_O55.md** whole (576 lines; SHA-256 24ff96d1…6881 = the hash Codex reviewed). **COFUN_CC.md** §1, §3, §5, §6,
  §11-§12 (hash 2a399a7d…e035 = Codex's). **KFACTOR_OFF55.md** l.1-210, l.328-496, l.650-684 (read at 00:44-00:48Z after
  the coordinator's message; it was still growing then — final hash at 00:57Z: 6a47b654…3c159).
- **BFT_A.md**: §1 (l.18-47), §2-§3.11 (l.48-275), §7.1-7.2 (l.444-473), §12.0-12.1 (l.879-924), §13.5 CR-1 (l.1010-1023),
  §26.1 (l.2219-2246), §28.6 WR (l.2496-2509), §31.0-31.2 (l.2733-2832).
- **BFT_B.md**: §27.1-27.2 (l.3584-3600), §29.1-29.4 (l.3659-3740), §35.6 COF-crit (l.4106-4110), §36.5 NCE (l.4197-4213).
- **REVIEW_BFT_A_S1.md** l.1-40, l.120-245 (BA-3/BA-4/BA-5/BA-6 verdicts); **REVIEW_S13_S14.md** l.174-195 (NA-alg:
  CONFIRMED-WITH-FIX); **REVIEW_BFT_B_S2.md** l.296-312 (density analyticity = "routine but unwritten" N5-an♭-dens).
- **LINEAR_PACKAGE.md** l.49-110 (S4' contours, Setting SC, normalisation).
- Drift: none found against the line numbers quoted in the two Codex reviews and in KFACTOR_O55 §0 for the passages used.

## §1. (T1) The obligation, stated exactly

**Object.** At a critical point x* of F := 𝔉_k∘exp(·; B) (TOWER-VAR, BFT_A §1.1: 𝔉_k = S_W(U_0) + Σ_{l<k}κ_lΣ_cφ̂_c(M̄^{(l)}_c(U_l); U_{l+1}),
φ̂ = Re tr(W_0^{-1}M) − Re tr(V^{-1}M), NA-alg (b)), the **actual, all-orders critical-point source** is
  **S_full := 𝔑^0(x*; B) = Hx* − NB − ∇F(x*; B) = Hx* − NB**  (BFT_A §31.0 "Ungauged remainder"; CODEX_REVIEW_TR §1:
  "Exact for the full source S*=𝔑^0(x*;B), held fixed … composite co-closedness only" — CONFIRMED there; I re-derived it:
  ∇_z E_src(z; B, S_full)|_{z=x*} = Hx* − NB − S_full = ∇F(x*) = 0).
S_full is **composite-co-closed only**: (CC-0) at critical points is banked REFUTED ([S26-BANKED], CODEX_REVIEW_C2 item 4),
so D(S_full) = κ_{k−1}ev_k^Td*r_{k−1}(x*) may be nonzero at the level-k roots. Nothing below assumes more.

**What each Codex review requires** (verbatim anchors):
- CODEX_REVIEW_TR §3 ("The unproved source hypothesis is material"): the slot bounds were established "only for the quadratic
  source"; one must price **ΔS := S_full − S_2**, and "Even an `O(η³)` bound per level alone gives `O(kη³)`, which is not
  uniform at fixed `η`." Its **sufficient repair**: "an exact decomposition with no positive-level divergence slots, a uniform
  bound `||δs_i^c||≤C_s^(3)L^(−2m)η³`, and `Σ_lπ_l(δj_l)≤C_j^(3)η³`, together with the level-0 divergence-form bound"
  (m = k−1−i). Its error budget for TR-1 is E_i = ||δs^c_i|| + L^{−2m}{||δs^c_{k−1}|| + Σ_{l>i}[π_l(δj_l) + 2dΣ_aL^{−3(l−a)}π_a(δj_a)
  + 6L^{k−l}||δG^c_l||]} (§3, display "E_i ="). Item 5: "NOT-VERIFIED — promotion to full nonlinear COF-crit/NCE(i) from the
  present packet alone. Retain the higher-order exact-source obligation."
- CODEX_REVIEW_TOPCC item 4: "If the complete actual critical-point source is composite-co-closed and satisfies
  `Ñ_Σ(S_full)≤C_*η²`, bank the corresponding source-only η² bound for its linear response, including the whole invariant
  curvature tower and top residual", with (§5, "CC-CRIT and the separate TR review")
  **Ñ_Σ(S) = ||G^c_0||_∞ + [G^c_0]_α + Σ_lπ_l(j_l) + max_{1≤l<k}L^{θ(k−l)}||G^c_l||_∞ + ||s||_R** (empty max = 0 at k = 1),
  π_l(j) := L^{3(k−l)}sup_own|j| (coarse plain units; COFUN_CC §1 "Norms"), ||s||_R := max_lL^{θ(k−l)}L^{k−1−l}||s^c_l||_∞,
  [·]_α the Campanato seminorm (BFT_A §7.2), 0 < α < θ < 1.

**Quantifiers required:** C_* independent of k ≥ 1, T ≥ 1 and the gauge fixing Γ; trivial background (class 𝒞_glob, global
gauge), weight m = 0; every critical point with ||x*||_𝔐 ≤ η ≤ η_H (𝔐 = 𝔐^∇, BFT_A §1.4) — and, as CODEX_REVIEW_TR §2
records for CR-1, the data convention **||B_k||_D ≤ η** (automatic for BFT-0's fixed point, whose radius is C_0||B_k||_D with
C_0 = 2(1 + G_D) ≥ 1).

**Both reviews therefore need the same thing:** an exact slot representation of S_full (all orders) with (i) no positive-level
divergence slot, (ii) residual slots with own size O(L^{−3(k−l)})·η² (TR-1 needs ||s^c_i|| ≲ L^{−2m}η², Ñ_Σ needs ||s||_R ≲ η²),
(iii) plain currents whose **level sum** is O(η²) k-uniformly — which, since the BCH₂ row R^B_l has no level decay a priori,
can only come from transport (Lemma TR) for that row and from **a priori level decay** for everything else — and (iv) the
level-0 Wilson slots in sup + Hölder. §3-§6 prove exactly this.

## §2. KFACTOR_OFF55 Lemma SG, checked (coordinator's request; read 00:44-00:48Z, after my own route of §4 was derived)

Location: KFACTOR_OFF55.md "### 2.1 Lemma SG (exact factorisation of the soft gradient)".

**(SG-a) The identity δσ_c = κ_l[−Re tr(ΘW_0^{-1}δM) + Re tr(ZΘG)] — CONFIRMED.** Re-derived line by line:
δ[Re tr(W_0(M)^{-1}M)] = Re tr(W_0^{-1}δM) by stationarity of W_0 (NA-alg (a), first bullet; the variation of W_0 drops out);
δ[−Re tr(V^{-1}M)] = −Re tr(V^{-1}δM) + Re tr(ZV^{-1}M) with Z = V^{-1}δV; e^ρ = V^{-1}W_0 gives W_0^{-1} − V^{-1} = −ΘW_0^{-1}
and V^{-1}M = (1 + Θ)G; finally Re tr(ZG) = Re tr(ZH) + θRe(i tr Z) = 0 (tr(ZH) ∈ iℝ for Z ∈ su(N), H Hermitian; tr Z = 0).
Exact checks: **hg55_4 D1 (N = 3, non-scalar H) 16/16 exact through ε⁴, with a control that fires (D4: replacing the
maximiser by e^{Ȳ} breaks 16/16 comparisons at ε³)**; hg55_3 C1 was also 16/16 exact but its control could not fire on that
family (§8), so hg55_3 carries no weight for SG.

**(SG-b) "∇Σ_cσ_c = κ_lR_l^TΨ_l + κ_lE_l(x), Ψ_c = Π(−Θ_c^*) = ρ_c + O(|ρ_c|³)" — CONFIRMED.** −Θ^* = 1 − e^{−ρ}, Π kills the
Hermitian even powers. The split is exact at every x (E_l is defined as the remainder; I re-added the three brackets of its
definition and recovered SG-a).

**(SG-c) "every soft plain row, at every order, inherits whatever level decay the residual has" — CONFIRMED, with one
precision that is load-bearing.** E_l = (coefficient of size O(s_l), resp. O(s_{l+1} + y²) at level l+1)·Θ, and
Θ = r + (ρ − r) + O(ρ²). The r-part inherits the residual's decay; the (ρ − r)-part is an **additive** term whose a-priori
size O(L^{−3(k−l)}η²) (own) is geometric **only because of the S4' second-order cancellation (BA-4, "CEN2")**: without it
ρ − r = O(L^{−2(k−l)}η²), and the plain rows would carry a non-r-linear term of size O(η³) per level in coarse units — a level
count k·η³ at third order. hg55_2 B4 exhibits exactly this term on the lane's own soft density when the S4' average is
replaced by one contour (ε³ coefficients 1152, 576 of the plain current with r ≡ 0), and B3 shows it is absent with the
average. SG's (LA-2) does name BA-4's cancellation for the quadratic part, so SG is right; the point is that (LA-2) is not a
"local constant" issue only — it is the one place where a k-factor could re-enter at higher order (§5).

**(SG-d) Two notational precisions (neither changes a conclusion).** (1) In (LA-1) the coefficient is W_0^{-1}∂_bM̄_c with W_0
**frozen** (the envelope), not ∂_b(W_0^{-1}M̄_c) as typeset. (2) E_l has a **level-(l+1) plain part** (from Z − δx_{l+1} and
G − 1); on the 𝔐^∇ ball (σ = 0) it is, like R^B_l, O(η²) per level with no a-priori decay (π_{l+1} ≤ L^{3m}·2s_{l+1}·2|ρ| ≈
4L³η²), so at critical points its level sum needs transport (TR-1) exactly as R^B does. SG's Corollary SG-TR does feed TR-1
back ("feeding TR-1 back into Lemma SG"), so this is handled there; the route of §4 below avoids that level-(l+1) plain part
altogether (it is residual-type there), which is why I keep both.

**(SG-e) Erratum in ROW^{(σ)} (b)** (s_l² ≤ L^{−2(m+1)}η² in the level-(l+1) factor) — CONFIRMED necessary and correctly applied
by its author ("Erratum to 2.2 (b)").

**Verdict on SG: CONFIRMED (identity and both consequences); not wrong anywhere.** What it left undone is (LA-1)-(LA-3); §3
writes them out. Provenance note (already self-disclosed in KFACTOR_OFF55 §10 item 1): its §8/§9 heading times were written
ahead of the clock; content unaffected.

**Lemma TOP♯ (KFACTOR_OFF55 §4.1) — noted, spot-checked, not used.** I re-did its ℓ¹ count: own |(PY^{(b)})_l| ≤
L^{−(k−l)}C_FPe^{−m_wd}/κ_−, d·L^{4(k−l)} links per coarse cell, so Σ_{b'}|(PY)_l| ≤ dL^{3(k−l)}C_FPS_4/κ_− and
|⟨j_l, PY_l⟩| ≤ dC_FPS_4π_l(j_l)/κ_− — the arithmetic is right; its analytic input (Corollary FP, T ≥ 3) I did not re-check.
My conclusions use COFUN_CC's **Lemma TOP-cc** (Codex-CONFIRMED, T ≥ 1 via the small-torus lift) instead; TOP♯ corroborates it
for T ≥ 3, as KFACTOR_OFF55 §11 says. I agree with that §11 statement.

*Erratum to §2 (SG-d)(2), found on re-reading:* the a-priori level-(l+1) size is π_{l+1} ≤ L^{3m}·2L^{−m}η·2L^{−2m}η = **4η²**,
not "4L³η²" (s_{l+1} ≤ L^{−m}η, own |r_l| ≤ L^{−2m}η). The statement (O(η²) per level, no a-priori decay) is unchanged.

## §3. (T2, part 1) The local analytic inputs (LA), written out

**Symbols pinned for this file** (systemic defect 1): ε_l := L^{−(k−l)} (= BFT_A §7.2's ρ_l; not any lane ε); N_c := the
level-l links in the 24·81 S4' words of the level-(l+1) link c (BFT_A's N(X, μ)); n_c := max_b #{c : b ∈ N_c};
freq_c(b) := average over the words of c of the number of occurrences of b; c_L := max_bΣ_cfreq_c(b);
X_0(c) := log W_0(M̄_c(e^{x_l})) (NA-alg (a)); **â_c := X_0(c) − (Q_lx_l)(c)**; **ŵ_c := X_0(c) − x_{l+1}(c) = r_c + â_c**
(the nonlinear residual; x_k := B_k); **φ̃_c(x_l, ŵ) := φ̂(M̄_c(e^{x_l}); e^{X_0(c) − ŵ})**; **Ω̂_c := ∂_ŵφ̃_c** (not the
level sum Ω = Σω_l^{-1}); SG's Ψ_c is written SG-Ψ_c. Norms on su(N): Hilbert–Schmidt |·|, op-norm ||·||. B_2(z_1…z_p) :=
½Σ_{a<b}[z_a, z_b].

### 3.1 A-priori own sizes on the ball (from the definition of 𝔐^∇, BFT_A §1.4; CONFIRMED by re-reading)
For ||x||_𝔐 ≤ η ≤ 1 and ||B_k||_D ≤ η, every 0 ≤ l ≤ k − 1:
(S1) |x_l(b)| ≤ ε_lη and |x_{l+1}(c)| ≤ Lε_lη (l + 1 = k: |B_k| ≤ η = Lε_{k−1}η);
(S2) parallel level-l links: |x_l(b) − x_l(b')| ≤ |b − b'|_1ε_l²η (∇^cx^c_l = L^{2(k−l)} × own difference);
(S3) |r_l(x)(c)| ≤ L²ε_l²η (L^{k−1−l}||r^c_l||_∞ ≤ η, r^c_l = L^{k−1−l}r_l);
(S4) |(dx_0)_p| ≤ 2ε_0²η (BA-3, CONFIRMED REVIEW_BFT_A_S1 Part 3);
(S5) contour logs: y := max_word|log T| ≤ 2p_Lε_lη (BCH, all letters ≤ ε_lη, p_Lε_lη ≤ 1/40).
The analysis at level l therefore sees **local variables of own size ε_lη (x_l), Lε_lη (x_{l+1}), ε_l²η (r, ŵ)**.

### 3.2 Lemma AN (local analyticity with level-, k- and T-independent constants) — PROVEN-HERE (standard)
*Statement.* There are R ∈ (0, 1/(40p_L)] and S < ∞ depending only on (N, L) (d = 4) such that, for every k, T, l and c,
each of the following functions of finitely many real variables (real coordinates in an HS-orthonormal basis of su(N)):
â_c(x_l|_{N_c}); φ̃_c(x_l|_{N_c}, ŵ); ρ_c := log(e^{−x_{l+1}(c)}W_0) as a function of (x_l|_{N_c}, x_{l+1}(c)); the Wilson maps
q(a) := log(e^{a_1}e^{a_2}e^{−a_3}e^{−a_4}) − (a_1 + a_2 − a_3 − a_4) and g(a) := −q(a) − (∇𝒲(X(a)) − X(a)), X(a) :=
a_1 + a_2 − a_3 − a_4 + q(a), 𝒲(X) := Re tr(1 − e^X); and β(X, w) := log(e^{−(X−w)}e^X) − w — has a Taylor series at 0 that
converges absolutely on the closed complex polydisc 𝔻_R (every complexified real coordinate of modulus ≤ R), with sup ≤ S.
*Proof.* (i) *Finitely many types.* Up to lattice translations, axis permutations and reflections the word set of c is one of
finitely many: for T_{l+1} ≥ 2 the ≤ 2L·L³ sites of N_c are distinct on the level-l torus (side T_{l+1}L ≥ 2L; the straight
legs use 2L − 1 link positions in direction μ), so the function is the "generic" one; for T_{l+1} = 1 it is the generic one
composed with the fixed linear identification ι of word positions with torus links, which maps 𝔻_R into 𝔻_R (it copies
coordinates). Wilson functions have one type. (ii) *Real-analyticity at 0.* M̄_c is a polynomial in the entries of e^{±x}
(entire); the contour logs are analytic near 1. X_0(M) solves the real-analytic equation Π(e^{−X}M) = 0 (NA-alg (a),
"Stationarity"), whose X-derivative at (X, M) = (0, 1) is −id on su(N); the analytic implicit-function theorem gives a
real-analytic solution near M = 1, equal to NA-alg's fixed point by its uniqueness in |X| ≤ 3y. Hence â_c, φ̂ =
Re tr(e^{−X_0}M) − Re tr(e^{−v}M) (Re tr of products of exponentials, real-analytic), φ̃_c (v = X_0 − ŵ), ρ_c, q, g (𝒲 =
N − tr cosh X on anti-Hermitian X, entire) and β are real-analytic at 0. (iii) A real-analytic function of finitely many
variables has an absolutely convergent Taylor series on some polydisc; take R as half the least radius over the finitely
many types (and ≤ 1/(40p_L)), S the largest sup. ∎ R, S are **not computed** (as the lane's r_*, S_*, c_pol, C_q are not);
this agrees with PROOF.md Lemma N5-an's proof and with REVIEW_BFT_B_S2's "N5-an♭-dens … routine".

### 3.3 Lemma CE (Cauchy–Schwarz consequences) — PROVEN-HERE (standard)
Let f be a function of Lemma AN, z real with |z|_∞ := max_i|z_i| ≤ R/4.
(CE-1) If f's Taylor series starts at degree p, then |f(z)| ≤ 2S√(N²−1)(|z|_∞/R)^p, and the degree-≥q tail of f obeys the same
with p → q.
(CE-2) For a unit direction h in one link variable, if f starts at degree p ≥ 1: |D_hf(z)| ≤ (8S√(N²−1)/R)(2|z|_∞/R)^{p−1}.
(CE-3) If f(x, 0) = 0 and ∂_ŵf(x, 0) = 0 for all small real x, then f(x, ŵ) = ∫_0^1(1 − t)∂_ŵ²f(x, tŵ)[ŵ, ŵ]dt and
∂_ŵf(x, ŵ) = ∫_0^1∂_ŵ²f(x, tŵ)[ŵ]dt, with ∂_ŵ²f again of Lemma AN type on 𝔻_{R/2} (sup ≤ 8S/R²).
*Proof.* g(ζ) := f(ζz/|z|_∞) is holomorphic for |ζ| ≤ R (the point lies in 𝔻_R), bounded by S per component; its n-th Taylor
coefficient is the degree-n part P_n(z/|z|_∞), so |P_n(z)| ≤ S(|z|_∞/R)^n and Σ_{n≥p} ≤ 2S(|z|_∞/R)^p for |z|_∞ ≤ R/2. For
(CE-2) apply (CE-1) to D_hf, which is holomorphic on 𝔻_{R/2} with sup ≤ 2S/R (one-variable Cauchy on a disc of radius R/2)
and starts at degree p − 1. (CE-3) is Taylor's formula in ŵ with the two vanishing conditions; they hold for complex
arguments by the identity theorem. ∎

### 3.4 (LA-1) — PROVEN-HERE, explicit constants (real configurations, p_Ls_l ≤ 1/20, s_l := sup|x_l|)
(a) |W_0^{-1}∂_bM̄_c[u] − Q_{cb}u| ≤ 8p_Ls_l·freq_c(b)·|u| (W_0 frozen — the envelope). *Proof.* For a word T = Πe^{z_a},
∂_bT[u] = Σ_{a: link b}σ_aP_{<a}(∫_0^1e^{(1−s)z_a}ue^{sz_a}ds)P_{>a}; all factors are unitary and ||Πe^{z} − 1|| ≤ Σ|z|, so
each term differs from σ_au by ≤ p_Ls_l|u|; average over words: |∂_bM̄_c[u] − Q_{cb}u| ≤ freq_c(b)p_Ls_l|u| and
|∂_bM̄_c[u]| ≤ freq_c(b)|u|. Then ||W_0^{-1} − 1|| ≤ |X_0| ≤ 3y ≤ 6p_Ls_l. ∎
(b) For V = e^v and Z := V^{-1}δV: |Z − δv| ≤ ||v||·|δv|. *Proof.* Z = ∫_0^1e^{−sv}δve^{sv}ds and |e^{−sv}δve^{sv} − δv| ≤ 2s||v|||δv|. ∎
(c) ||G − 1|| ≤ 18.4y² (NA-alg (a), last bullet of its proof; CONFIRMED REVIEW_S13_S14 "G = H + iθ1, with ||H - 1|| ≤
||G - 1|| ≤ 18.4y²").
*Consequence for SG's E_l:* own |E_l(b)| ≤ 2κ_+·8p_Ls_lc_L·max_{c∋b}|Θ_c| (level l) and own |E_l(c)| ≤
κ_+(2s_{l+1} + 18.4y²)·|Θ_c| (level l + 1), |Θ| ≤ e^{|ρ|}|ρ| ≤ 2|ρ|. This is SG's (LA-1) with C_E ≤ 16.

### 3.5 (LA-2) — PROVEN-HERE (one CONFIRMED algebraic input, BA-4/BA-5, re-checked exactly)
**Lemma C2 (second-order structure; = BA-4 + BA-5, re-derived).** (i) â_c's degree-2 Taylor part is â^{(2)}_c(x) =
avg_{σ,y}B_2(T^σ_y(x)) = Ȳ^{(2)}_c. (ii) If x is constant in each direction on N_c, avg_{σ,y}B_2 = 0. (iii) For x in the
ball, |â^{(2)}_c(x)| ≤ ½p_L(p_L − 1)δ(2|x̄| + δ) ≤ **C_{a2}ε_l³η², C_{a2} := (35/2)Lp_L²**.
*Proof.* (i) X_0 = Ȳ + Π(K(X_0)) (NA-alg (a)); K's degree-2 terms are R_X^{(2)} = X²/2, E^{(2)} = avgY²/2 and −XȲ|_{X=Ȳ} = −Ȳ²,
all Hermitian (squares of anti-Hermitian matrices), so Π(K(X_0)) has no degree-2 part; and log T = Σz + B_2(z) + O(3).
(ii) BA-4's block computation (CONFIRMED REVIEW_BFT_A_S1 Part 4): with direction-constant letters the word's B_2 is
L[D, x̄_μ], D = Σ_νd_νx̄_ν linear in d = y − c_X, and avg_yd = 0 (L odd, c_X the block centre). (iii) Write z_a = z̄_a + δ_a
(z̄ the direction-constant value at a reference link of each direction); per pair |[z_a, z_b] − [z̄_a, z̄_b]| ≤ 2δ(2|x̄| + δ);
(ii) kills avg B_2(z̄); δ ≤ diam_1(N_c)·ε_l²η ≤ 5Lε_l²η by (S2), |x̄| ≤ ε_lη, and 5Lε_l ≤ 5. ∎ **hg55_1** checks (ii)
exactly on all 1944 words per direction at d = 4, L = 3 (24/24 exact zeros; control without the y-average fires) and the
(iii) bound on 24 non-constant fields.
**Consequences** (with Lemma CE): **|â_c| ≤ C_aε_l³η²**, C_a := C_{a2} + 2√(N²−1)SR^{−3} (the degree-≥3 tail is ≤
2√(N²−1)S(ε_lη/R)³ ≤ that·ε_l³η² for η ≤ 1); **|ŵ_c| ≤ C_wε_l²η**, C_w := L² + C_a; and, since β vanishes at w = 0 and at X = 0
(β(X, w) = ∫∫∂_X∂_wβ(sX, tw)[X, w]), |ρ_c − ŵ_c| = |β(X_0, ŵ_c)| ≤ C_β|X_0||ŵ_c| with C_β := 16√(N²−1)S/R², so
**|ρ_c − r_c| ≤ |â_c| + |β| ≤ C_ρε_l³η², C_ρ := C_a + 6p_LC_βC_w** — SG's (LA-2) in the form it uses.

### 3.6 (LA-3) Wilson — PROVEN-HERE
X_p := log U_p = (dx_0)_p + q_p(a_p), a_p the four link values; S_W = Σ_p𝒲(X_p); for anti-Hermitian X, ∇𝒲(X) = Π(sinh X) and
|∇𝒲(X) − X| ≤ sinh|X| − |X| ≤ |X|³ (|X| ≤ 1). By (S1), (S4) and |q| ≤ 9s_0² (BA-3's quoted S6 bound, CONFIRMED),
|X_p| ≤ 3ε_0²η (η ≤ 1/9). Exact slots: **G_0(p) := −(∇𝒲(X_p) − (dx_0)_p) = g(a_p)** (divergence form) and
**j^W_0(b) := −Σ_{p∋b}(∂_bq_p)^T∇𝒲(X_p)** (plain, level 0). Bounds, all orders:
||G^c_0||_∞ ≤ 9η² + 27ε_0⁴η³; [G^c_0]_α ≤ [G^c_0]^∞_α ≤ 4C_gη² (g starts at degree 2, so |g(a) − g(a')| ≤
C_gmax(|a|_∞, |a'|_∞)|a − a'|_∞ by (CE-2), and translating the four links by v, |v|_∞ = nδ_c ≤ n, moves them by ≤
4δ_cε_0η by (S2): WR (a)'s argument, CONFIRMED in CODEX_REVIEW_TR §5, now for the full g); π_0(j^W_0) ≤ 6·(8S√(N²−1)/R)(2/R)·
ε_0η·4ε_0²η·L^{3k} =: A_W^∞η². Degree ≥ 3 parts: ||δG^c_0||_∞ + [δG^c_0]^∞_α ≤ C_{G3}ε_0η³ (g − g^{(2)} starts at degree 3) and
π_0(δj^W_0) ≤ C_{W3}η³ (it contains (∂_bq^{(2)})^Tq_p, own ≲ ε_0·ε_0²η³: bounded, single level). ∎

## §4. (T2, part 2) The exact all-orders slot decomposition, by a second route (factorisation through ŵ)

This route was derived before the coordinator's message; it reaches SG's conclusion independently and slightly more sharply
(no level-(l+1) plain current; exact identification of the quadratic slots; Codex TR §3's sufficient repair in its literal
η³ form). Either route, with §3, suffices for §6.

### 4.1 Lemma NC3 (the soft density has no cubic term in the chart (x_l, ŵ)) — PROVEN-HERE
*Statement.* φ̃_c(x, ŵ) = ½|ŵ|² + φ̃_{4,c}(x, ŵ), where φ̃_4's Taylor series starts at degree 4, and φ̃_4(x, 0) = 0,
∂_ŵφ̃_4(x, 0) = 0 for all x.
*Proof.* φ̃(x, 0) = φ̂(M; W_0) = 0 identically, and ∂_ŵφ̃(x, 0) = 0 is the stationarity of W ↦ Re tr(W^{-1}M) at W_0 (NA-alg
(a)); both hold for ½|ŵ|² too. For the degrees: V^{-1}M = e^ρG, so φ̂ = −Re tr((e^ρ − 1)G) = −Re tr(ρG) − ½Re tr(ρ²G) −
(1/6)Re tr(ρ³G) − O(|ρ|⁴). The first term vanishes **identically** (SG's step: Re tr(ZG) = 0 for every Z ∈ su(N)). Degree
counts: ρ = log(e^{−(X_0−ŵ)}e^{X_0}) = ŵ + ½[ŵ, X_0] + (degree ≥ 3, each term containing ŵ); X_0 = Qx + O(2); G = 1 + (degree ≥ 2)
(G's degree-1 part is M^{(1)} − X_0^{(1)} = Qx − Qx = 0). Degree 2: −½Re tr(ŵ²) = ½|ŵ|². Degree 3: −½Re tr(ŵ[ŵ, X_0] +
[ŵ, X_0]ŵ)/2·2 = −½Re tr(ŵ²X_0 − ŵX_0ŵ) = 0 (cyclicity), −(1/6)Re tr(ŵ³) = 0 (tr of an anti-Hermitian matrix is imaginary),
and no term of ρ²G or ρG of degree 3 involves G − 1. ∎ **hg55_3 C3 checks this exactly at N = 3 (3/3: ε² coefficient
−½tr(w²), ε³ coefficient 0), with the control C4 firing (the linear-residual chart has a nonzero cubic term).**
*Consequences* (Lemma CE): with Ê_c := ∂_ŵφ̃_4(x_l, ŵ_c),
  **Ω̂_c = ŵ_c + Ê_c, |Ê_c| ≤ C_Ê max(|x_l|_∞, |ŵ_c|)²|ŵ_c|,  |∇_{x(b)}φ̃_c| ≤ C_φ max(|x_l|_∞, |ŵ_c|)|ŵ_c|²**
((CE-3) with ∂_ŵ²φ̃_4 of degree ≥ 2 and ∂_ŵ²∇_xφ̃_4 of degree ≥ 1; C_Ê, C_φ depend only on S, R, N).

### 4.2 Lemma FAC (exact slots of the full source) — PROVEN-HERE (chain rule; no estimate)
For every real configuration in the domain and every chain variation u (u_k = 0), with Φ_c(x_l, x_{l+1}(c)) =
φ̃_c(x_l, X_0(c) − x_{l+1}(c)) and DX_0(c)[u_l] = (Q_lu_l)(c) + Dâ_c[u_l]:
  DΦ_c[u] = ⟨Ω̂_c, r_c(u)⟩ + ⟨(Dâ_c)^TΩ̂_c + ∇_xφ̃_c, u_l⟩.
Subtracting the linear part κ_l⟨r_c(x), r_c(u)⟩ of H and adding the Wilson part of §3.6:
**𝔑^0(x; B) = (G_0; G_l = 0 for l ≥ 1; j_0 = j^W_0 + j^{soft}_0, j_l = j^{soft}_l; s_l), with**
  **s_l(c) := −κ_l(Ω̂_c − r_c) = −κ_l(â_c + Ê_c)   (level-(l+1) residual slot, 0 ≤ l ≤ k − 1),**
  **j^{soft}_l(b) := −κ_lΣ_{c: b∈N_c}[(∂_bâ_c)^TΩ̂_c + ∇_{x(b)}φ̃_c]   (level-l plain current),**
and G_0, j^W_0 of §3.6. There is **no** positive-level divergence slot and **no** level-(l+1) plain current: everything a
level-l soft term does at level l + 1 enters through ⟨s_l, r_l(u)⟩. (Signs: these are the slots of 𝔑^0 = Hx − NB − ∇F,
i.e. CODEX_REVIEW_TR §1's corrected sign convention.)

### 4.3 Proposition HS (all-orders sizes) and HS-3 (Codex TR §3's sufficient repair, literally) — PROVEN-HERE
Let η ≤ η_H := min{R/(4(1 + C_w)), 1/9}, ||x||_𝔐 ≤ η, ||B_k||_D ≤ η; k ≥ 1, T ≥ 1 arbitrary. Put
**S_2 := (G_0 = −q^{(2)}; j_0 = −R^B_0 − (∂q^{(2)})^Tdx_0; j_l = −R^B_l (1 ≤ l < k); s_l = −κ_lâ^{(2)}_l = −κ_lȲ^{(2)}_l)**,
R^B_l(b) := κ_lΣ_c(∂_bâ^{(2)}_c)^Tr_c(x) = BFT_A §12.0's BCH₂ row (⟨R^B_l, u_l⟩ = 2κ_l⟨r_l(x), B(x_l, u_l)⟩, since
Dâ^{(2)}_c[u] = 2B_c(x, u)); and **ΔS := 𝔑^0 − S_2**, i.e.
  δG_l = 0 (l ≥ 1), δG_0 = g − g^{(2)}, δs_l = −κ_l(â^{(≥3)}_c + Ê_c),
  δj_l(b) = −κ_lΣ_c[(∂_bâ_c − ∂_bâ^{(2)}_c)^Tr_c + (∂_bâ_c)^T(â_c + Ê_c) + ∇_{x(b)}φ̃_c] (+ δj^W_0 at l = 0).
Every term of ΔS has degree ≥ 3 in (x, B), so **S_2 is exactly the quadratic Taylor part of 𝔑^0** and ΔS its cubic-and-higher
remainder. Then, with m := k − 1 − l and constants depending only on (N, L, κ_+) through (R, S):
- **(HS-a) residual slots:** own |δs_l| ≤ κ_+C_{s3}ε_l³η³, i.e. **||δs^c_l||_∞ ≤ κ_+C_{s3}L^{−3}·L^{−2m}η³**, C_{s3} :=
  2√(N²−1)SR^{−3} + C_Ê(1 + C_w)²C_w. (Proof: (CE-1) for â^{(≥3)}; §4.1 for Ê with max(|x|, |ŵ|) ≤ (1 + C_w)ε_lη.)
- **(HS-b) plain currents:** own |δj^{soft}_l(b)| ≤ κ_+n_cC_{j3}ε_l⁴η³, i.e. **π_l(δj^{soft}_l) ≤ κ_+n_cC_{j3}L^{−(k−l)}η³**,
  C_{j3} := C_{D2}L² + C_{D1}(C_a + C_Ê(1 + C_w)²C_w) + C_φ(1 + C_w)C_w². (Proof, term by term: |∂_bâ − ∂_bâ^{(2)}| ≤ C_{D2}ε_l²η²
  ((CE-2), degree ≥ 2) times |r_c| ≤ L²ε_l²η; |∂_bâ| ≤ C_{D1}ε_lη times |â + Ê| ≤ (C_a + …)ε_l³η² — **this is the one term
  where Lemma C2's S4' cancellation is used: without it |â| ~ ε_l²η² and the product is ε_l³η³, i.e. O(η³) per level in coarse
  units**; |∇_xφ̃| ≤ C_φ(1 + C_w)C_w²ε_l⁵η³. Each sum over c has ≤ n_c terms.) Hence
  **Σ_{l=0}^{k−1}π_l(δj_l) ≤ [κ_+n_cC_{j3}/(L − 1) + C_{W3}]η³**, k- and T-uniformly.
- **(HS-c) level-0 divergence form:** ||δG^c_0||_∞ + [δG^c_0]_α ≤ C_{G3}ε_0η³ = C_{G3}L^{−k}η³ (§3.6).
- **(HS-d) identification with the lane's second-order slots.** S_2's residual slot κ_lȲ^{(2)}_l equals BA-6's κ_lρ^{(2)}_l
  plus CR-1's s^C_l: with ρ^{(2)} = Ȳ^{(2)} − ½[x_{l+1}, Q_lx_l] and Q_lx_l = r_l + x_{l+1},
  κρ^{(2)} + s^C = κȲ^{(2)} − (κ/2)[x_{l+1}, r_l] + (κ/2)[x_{l+1}, r_l] = κȲ^{(2)}: **the two commutator pieces cancel
  exactly** (the lane bounds them separately, which is valid but double-counts). The plain slot −R^B_l is BFT_A's BCH₂ row;
  the Wilson pair is BA-3/WR's q^{(2)} and (∂q^{(2)})^Tdx_0. So S_2 is "the quadratic slots" CODEX_REVIEW_TR refers to, up to
  its §1 sign.
- **(HS-0) the full source, all orders (what §6 uses):** own |s_l| ≤ κ_+(C_{a2} + C_{s3}η)ε_l³η² =: A_s^{own}ε_l³η², i.e.
  ||s^c_l|| ≤ A_s^∞L^{−2m}η² with **A_s^∞ := A_s^{own}L^{−3}**; ||s||_R ≤ A_s^∞L^θη²; π_l(R^B_l) ≤ A_Bη² with A_B := c_Bκ_+L²
  (the (★) bound, CONFIRMED in CODEX_REVIEW_TR §4); π_l(δj_l) ≤ C_Δη³ (C_Δ := κ_+n_cC_{j3} + C_{W3}); G_0 as in §3.6.
**This is exactly the sufficient repair of CODEX_REVIEW_TR §3:** no positive-level divergence slots (δG_l = 0), ||δs^c_i|| ≤
C_s^{(3)}L^{−2m}η³ with C_s^{(3)} = κ_+C_{s3}L^{−3}, Σ_lπ_l(δj_l) ≤ C_j^{(3)}η³ with C_j^{(3)} = κ_+n_cC_{j3}/(L − 1) + C_{W3},
and the level-0 divergence-form bound (HS-c). Its error budget is E_i ≤ L^{−2m}η³[2C_s^{(3)} + C_fC_Δ·(k-uniform)] — I bound
it in §6 without the sum over m: Σ_{l>i}[π_l(δj_l) + 2dΣ_aL^{−3(l−a)}π_a(δj_a)] ≤ C_fΣ_lπ_l(δj_l) ≤ C_fC_j^{(3)}η³.

### 4.4 Proposition HS-Lip (Lipschitz forms, for the off-critical contraction; not used in §6) — PROVEN-HERE (outline-complete)
For x, x' with ||x||_𝔐, ||x'||_𝔐 ≤ η ≤ η_H (common data), every bound of HS/HS-3 holds for the difference of the slots with
one factor η replaced by ||x − x'||_𝔐 (and constants doubled). *Proof.* (i) The S4' cancellation for differences: â^{(2)}(x) −
â^{(2)}(x') = B̂(x − x', x + x') with B̂ the polarisation of the averaged quadratic form; since that form vanishes on the
linear space of direction-constant fields, B̂ vanishes on pairs of them, so |avg B̂(u, v)| ≤ p_L²(|ū|δ_v + δ_u|v̄| + δ_uδ_v)
(REVIEW_BFT_A_S1 Part 5, CONFIRMED there), and u = x − x' has oscillation ≤ 5Lε_l²||x − x'|| by (S2). (ii) Every other term
is a product of Lemma-AN functions with known minimal degrees in (x_l, ŵ); write each as (analytic coefficient)·(ŵ or r
factors) as in §4.1-4.3 and apply the mean-value inequality on the segment (convex polydisc) with the derivative bounds of
(CE-2); |ŵ − ŵ'| ≤ |r − r'| + |â − â'| ≤ (L² + 2C_a)ε_l²||x − x'||. ∎ This supplies KFACTOR_OFF55 ROW^{(σ)} (b)'s
"Lipschitz constants: the same with η² replaced by 2η||x − x'||" in the 𝔐^∇ ball, and a fortiori in its σ-balls (which are
contained in it).

*Errata to §4 (on re-reading; statements unchanged):* (1) NC3's degree-3 line should read: ρ²'s degree-3 part is ŵρ_2 + ρ_2ŵ
with ρ_2 = ½[ŵ, X_0^{(1)}], so −½Re tr(ŵρ_2 + ρ_2ŵ) = −Re tr(ŵρ_2) = −½Re tr(ŵ²X_0 − ŵX_0ŵ) = 0 by cyclicity. (2) The
TR-1 error budget is, exactly, **E_i ≤ L^{−2m}η³[2C_s^{(3)} + C_fC_j^{(3)}]** (||δs^c_i|| ≤ C_s^{(3)}L^{−2m}η³, ||δs^c_{k−1}|| ≤
C_s^{(3)}η³, and the FT convolution summed over all a ≤ l gives the factor C_f = 1 + 2d/(1 − L^{−3})). (3) **HS-Lip's status is
ARGUED** (steps listed, term-by-term constants not written), not PROVEN; it is not used for any conclusion of this file.

## §5. (T3) Do the higher orders decay across levels? Where could a k-factor re-enter?

**Answer: yes — every cubic-and-higher slot decays geometrically across levels a priori, on the whole 𝔐^∇ ball, not only
at critical points; the only slot without a-priori level decay, at any order, is the second-order BCH₂ row R^B_l (linear in
the residual with an O(s_l) coefficient), and transport (Lemma TR) gives it decay at critical points.** Power count in own
units at level l (local variables x_l ~ ε_lη, x_{l+1} ~ Lε_lη, r, ŵ ~ ε_l²η; a plain current needs own size ≤ ε_l^{3+δ} to
decay in π_l, a residual slot ≤ ε_l^{2+θ} for ||·||_R and ≤ ε_l³ for TR-1):

| slot (§4.2/4.3) | own size on the 𝔐^∇ ball | in its norm | a-priori level decay | at a critical point |
|---|---|---|---|---|
| s^{(2)}_l = −κȲ^{(2)}_l | ≤ κC_{a2}ε_l³η² (S4' cancellation) | ||s^c_l|| ≤ ·L^{−3}L^{−2m}η² | L^{−2m} (TR-1 input) | same |
| δs_l (degree ≥ 3) | ≤ κC_{s3}ε_l³η³ | ·L^{−3}L^{−2m}η³ | L^{−2m} | same |
| R^B_l (degree 2, r-linear) | ≤ c_Bκε_l·|r_l| ≤ c_Bκ L²ε_l³η² | π_l ≤ A_Bη² | **none** | κ̂L^{−m} (TR-2) |
| δj_l (degree ≥ 3) | ≤ κn_cC_{j3}ε_l⁴η³ | π_l ≤ ·L^{−(k−l)}η³ | **geometric** | same |
| G_0, j^W_0 (Wilson, all orders) | ε_0²η², ε_0³η² | ≤ Cη² (sup + Hölder; π_0) | single level | same |
| G_l, l ≥ 1 | 0 | 0 | — | — |

**Where a k-factor would re-enter, and why it does not.** (a) If the S4' second-order cancellation failed (|â| ~ ε_l²η²), the
residual slot would be ε_l²η² (||s||_R ~ L^{θ(k−l)}: not even bounded) and (∂â)^Tâ would be ε_l³η³ own, i.e. O(η³) per level in
π_l — the k·η³ CODEX_REVIEW_TR warns of. Lemma C2 (BA-4), checked exactly in hg55_1, rules this out; hg55_2 B4 shows the
non-r-linear ε³ plain term appearing on the actual soft density as soon as the average is removed, and B3 shows it absent
with the average. (b) A cubic term in the soft density's ŵ-chart would put a degree-2, ŵ-quadratic, x-linear piece into
∇_xφ̃ — own ε_l·(ε_l²)²: still geometric; so even this would not re-introduce k (Lemma NC3 is needed only for the exact
identification S_2 = quadratic part, not for the decay). (c) Terms linear in r with a higher-order coefficient
((∂â − ∂â^{(2)})^Tr) are ε_l²·ε_l² own: geometric a priori. (d) Wilson: single level. (e) Funnel terms h_l^Tψ_l: FT (ii)
convolves the per-level sizes with L^{−3(l−a)} (CONFIRMED, CODEX_REVIEW_TR §2) and adds no level count.

**Off the critical set** (KFACTOR_OFF55's σ-balls, σ > 0): the same table with |r_l| own ≤ L^{−(2+σ)m}η gives π_l(R^B_l) ≤
A_BL^{−σm}η² and leaves every other row unchanged, so the level sum of all plain rows is ≤ [A_B/(1 − L^{−σ}) + A_W^∞ +
C_Δη/(L − 1)]η² a priori — **CONFIRMED: KFACTOR_OFF55 ROW^{(σ)} (b)-(c) sizes hold at all orders** (given §3, now written).
At σ = 0 the R^B row alone gives (k − 1)A_Bη²: the level-count factor off the critical set is exactly that one row in the
𝔐^∇ weight, at every order (KFACTOR_O55 §5, KFACTOR_OFF55 §2.2 (c)).

## §6. (T4) Consequences: Lemma TR, COF-crit, NCE (i) and CC-CRIT for the full nonlinear source

**Theorem TR∞ (Lemma TR for the actual critical-point source, all orders) — PROVEN as an implication.**
*Hypotheses.* d = 4, L ≥ 3 odd, κ_l ∈ [κ_−, κ_+], trivial background (𝒞_glob, global gauge), weight m = 0, any k ≥ 1, T ≥ 1;
η ≤ η_H; x* a critical point of 𝔉_k∘exp with ||x*||_𝔐 ≤ η and ||B_k||_D ≤ η.
*Inputs.* Step 0 (CODEX_REVIEW_TR §1, CONFIRMED; re-derived in §1); Lemma RT-cc (c), Lemma TC, Lemma FT (ii) and the TR-1
derivation for any actual source with G_l = 0 (l ≥ 1) (CODEX_REVIEW_TR §2 and "Exactly what may be banked" item 1); the (★)
row bound (CODEX_REVIEW_TR §4); Proposition HS (§4.3; or SG + §3 — §2, §3.4-3.5).
*Conclusion,* for 0 ≤ i ≤ k − 2, m = k − 1 − i, with A_j^∞ := C_f(A_B + A_W^∞ + C_Δη_H), C_f = 1 + 2d/(1 − L^{−3}) (= 121/13 at
d = 4, L = 3):
- **(TR∞-1)** ||r^c_i(x*)||_∞ ≤ κ_−^{−1}L^{−2m}η[κ_+ + (2A_s^∞ + mA_j^∞)η];
- **(TR∞-2)** π_i(R^B_i(x*)) ≤ A_Bη²·min{1, κ̂L^{−m}[1 + (2A_s^∞ + mA_j^∞)η/κ_+]} (also for i = k − 1 through the first argument);
- **(TR∞-4)** **Σ_{l=0}^{k−1}π_l(j_l(S_full)) ≤ K_Σ^∞η²**, K_Σ^∞ := A_Bκ̂[(L/(L−1))(1 + 2A_s^∞η_H/κ_+) + (L/(L−1)²)A_j^∞η_H/κ_+] +
  A_W^∞ + C_j^{(3)}η_H, independent of k, T and Γ.
*Proof.* By HS-0 the full source has no positive-level divergence slot, ||s^c_i|| ≤ A_s^∞L^{−2m}η², ||ρ_{k−1}|| ≤ κ_+η + A_s^∞η²,
and per level π_l(j_l) ≤ π_l(R^B_l) + π_l(δj_l) + 1_{l=0}π_0(j^W_0) ≤ (A_B + C_Δη + A_W^∞)η², so FT (ii) gives π_l(ĵ_l) ≤ A_j^∞η²;
CODEX_REVIEW_TR §2's derivation then gives TR∞-1 verbatim (equivalently: TR-1 with its error budget E_i ≤ L^{−2m}η³[2C_s^{(3)} +
C_fC_j^{(3)}] of §4). TR∞-2 is (★), π_i(R^B_i) ≤ c_Bκ_+L^{m+2}η||r^c_i||, with TR∞-1 substituted. TR∞-4: Σ_lπ_l(R^B_l) ≤
A_Bκ̂Σ_{m≥0}L^{−m}[1 + (2A_s^∞ + mA_j^∞)η/κ_+]η² (Σ L^{−m} = L/(L−1), Σ mL^{−m} = L/(L−1)², CONFIRMED there) plus
Σ_lπ_l(δj_l) ≤ C_j^{(3)}η³ (HS-b: geometric, a priori) plus π_0(j^W_0) ≤ A_W^∞η². ∎
**The level sum stays O(η²) uniformly in k: CONFIRMED** — the BCH₂ row by transport, every higher-order row by its own a-priori
geometric decay (§5), the Wilson rows at one level. Step 4 of KFACTOR_O55 (feeding back to remove the factor m) applies
unchanged and gives π_l(R^B_l) ≤ A_Bκ̂L^{−m}(1 + c'η/κ_+)η².

**Corollary CC-CRIT∞ — full nonlinear COF-crit, NCE (i) (composite-co-closed form) and CC-CRIT — PROVEN as an implication.**
*Statement.* Under TR∞'s hypotheses and 0 < α < θ < 1, the response x_rows := x* − x(B_k) to S_full (homogeneous data,
Hx_rows = S_full) obeys
  **||x_rows||_inv + ||f_0(x_rows)||_∞ + [f_0(x_rows)]^∞_α ≤ C_inv'·C_*η²,**
||x||_inv = max_j[||f_j||_∞ + [f_j]_α + L^{k−1−j}||r^c_j||_∞] (the whole curvature tower, sup and Hölder, and every residual
including the top one), **C_* := 9 + 27η_H + 4C_g + K_Σ^∞ + A_s^∞L^θ**, uniformly in k ≥ 1, T ≥ 1 and the gauge fixing Γ.
*Proof.* S_full is composite-co-closed (Step 0) and Lemma FAC is an exact slot representation of it, so
Ñ_Σ(S_full) = ||G^c_0||_∞ + [G^c_0]_α + Σ_lπ_l(j_l) + 0 + ||s||_R ≤ [(9 + 27η_H) + 4C_g + K_Σ^∞ + A_s^∞L^θ]η² (§3.6, TR∞-4, HS-0).
CODEX_REVIEW_TOPCC item 3 (Theorem CC-INV with Lemma TOP-cc and CC-FUN (c), "also holds … with the explicitly defined weaker
Ñ_Σ") and item 4 (its conditional critical-point consequence) give the bound; the outputs are those of the Setting-LIN^cc
minimiser for every Γ (Lemma FG (iii)). ∎
*Reading against the three named statements.* (i) **COF-crit** (BFT_B §35.6's displayed conclusion, ||f_0||_∞ + [f_0]^∞_α ≤
Cη² at every critical point): holds, source-only, without (CC-0) (its §35.6 proof stays REFUTED; the conclusion is now
proved by another route). (ii) **NCE (i)** (BFT_B §36.5 (i)): its conclusion — (NC-Γ) for every gauge fixing at every
critical point, m = 0, trivial background, k- and T-uniform — holds in the composite-co-closed form; its stated mechanism
"Lemma CD (i) gives (CC-0)" is replaced by composite co-closedness + TOP-cc/CC-INV. (iii) **CC-CRIT** (COFUN_CC §11.5): its
premise "N_Σ(S*) ≤ C_*η²" was established there only for the quadratic rows; it now holds for the complete source in Ñ_Σ.

**Named inputs of the whole chain** (status as banked/confirmed, none re-judged beyond what is stated):
(I1) CODEX_REVIEW_TR items 1, 2, 4 (Step 0; RT-cc, TC, FT; (★); summation; C2-COF sup form); (I2) CODEX_REVIEW_TOPCC
item 3 (CC-INV, TOP-cc, CC-FUN (a)-(c) — implications of the lane-A/LINEAR_PACKAGE inputs listed there: W0, GU, LIN0/BL-5,
BL-4 (with the REVIEW_BFT_A_S2 constant fix), BL-C, YH, TS, W, FP, TOPD, DF-cc, COF-size, LP Thm 4.2 (ii)); (I3) NA-alg (a)-(b)
(CONFIRMED-WITH-FIX, REVIEW_S13_S14), BA-3, BA-4/BA-5 (CONFIRMED, REVIEW_BFT_A_S1; re-derived here, hg55_1), the S6 plaquette
bound |q| ≤ 9s²; (I4) this file's Lemmas AN, CE, C2, NC3, FAC, Proposition HS/HS-3 and Theorem TR∞ — **PROVEN-HERE, unreviewed**.

## §7. What is still missing — stated precisely (first-class results)

1. **Review.** Nothing in §3-§6 is banked until a Codex reviewer checks it. Attack order I recommend: Lemma AN (i) (the
   finiteness of types, in particular the T_{l+1} = 1 identification and that one (R, S) serves all k, T); Lemma C2 (i)
   (no degree-2 part of Π(K(X_0)) — the step that makes â's quadratic part the S4' average); HS-b's term list (that every
   degree-≥3 plain term carries ε_l⁴); TR∞-4's constants.
2. **The analytic constants R, S are not computed**, hence neither are η_H, C_s^{(3)}, C_j^{(3)}, A_W^∞, C_*. They are
   independent of k, T and Γ (that is what the target asks), but the lane's two-sided feasibility windows (SMALLNESS_DAG's
   complex-width interface) will eventually need magnitudes; this file adds R, S to the existing uncomputed family (r_*, S_*,
   r_♭, c_pol, C_q).
3. **Off the critical set** nothing here is a contraction proof: KFACTOR_OFF55's Theorem K still needs (GV^{(σ)})_Γ (OPEN) and
   the Lipschitz forms (HS-Lip: ARGUED). This is outside "the gauge-invariant half of clause (b)", which is a statement at the
   critical point, but it is what the *construction* of the critical point (BFT-0) needs.
4. **Scope, unchanged:** trivial background (𝒞_glob), m = 0, gauge-invariant outputs. The rest of BFT-5 clause (b) — (R1) the
   gauge-variant field components ((G♯_0-field), OPEN), (R2) the background Z(V_k) incl. (CC-dec_Z) (OPEN), (R3) m > 0 (weighted
   COF/TOP-cc: OPEN beyond QH_m/W0_m) — is untouched (COFUN_CC §6.2; CODEX_REVIEW_TOPCC item 5).
5. **Existence** of a critical point in the ball is not addressed (BFT-0).
**Is the gauge-invariant half of clause (b) complete at the trivial background, m = 0, nonlinearly?** At critical points:
**yes, as an implication** — CC-INV (banked, linear) applied to the full exact source, whose Ñ_Σ is now bounded by C_*η²
k-, T- and Γ-uniformly (CC-CRIT∞) — **pending review of item 1**; with the scope of item 4 and the uncomputed constants of item 2.

## §8. Check record (criteria before scripts; exact integer/Fraction/Gaussian-rational arithmetic; no floats anywhere)

| id | criteria born | script born | run (UTC) | result |
|---|---|---|---|---|
| hg55_1 (CEN2 on the actual d = 4, L = 3 contours, 1944 words per direction) | 00:39:05Z | 00:39:41Z (one display line edited before the run: a float display removed) | 00:39:43-48Z | **PASS**: A1 24/24 exact zeros; A2 single words nonzero; A3 BA-4 ℓ¹ bound holds (max ratio 674438/80310285); A4 ε² coefficient 0 in 24/24, ε³ nonzero; **A5 control (no y-average) FIRES**; A6 Qx̄ = 3x̄_μ |
| hg55_2 (slot orders on the actual SU(2) soft density, d = 2) | 00:39:05Z | 00:41:25Z | 00:41:57-00:42:02Z | **PASS**: B1 Ω̂ = 2ε²ρ_2 + O(ε³); B2 plain current O(ε³) with ε³ coefficient = independently computed BCH₂-row value (e.g. −88/9 = −88/9, 16/3 = 16/3); B3 with r ≡ 0 plain O(ε⁴), Ω̂ O(ε³), non-vacuous; **B4 control (one contour) FIRES** (Ω̂ ε² coefficients −72, 72; plain ε³ coefficients 1152, 576 with r ≡ 0); B5 sanity |
| hg55_3 (SG identity and NC3 at N = 3) | 00:52:30Z | 00:53:40Z | 00:54:03-07Z | **FAIL as pre-registered (non-discriminating)**: C1 16/16 exact, C2 PASS, C3 PASS (ε³ coefficient 0 in 3/3), C4 control FIRES, **C5 control DOES NOT FIRE** |
| hg55_4 (SG identity at N = 3 on a discriminating family) | 00:55:18Z | 00:55:18Z (same second; the criteria heredoc precedes the script generation in one shell command) | 00:55:25-31Z | **PASS**: D1 16/16 exact through ε⁴; D2 16/16 non-vacuous; D3 maximiser sanity; **D4 control (non-maximiser e^{Ȳ}) FIRES 16/16** (first failing coefficient ε³: 34021/2187 vs 12220/2187) |

**hg55_3's failure, explained (post hoc; the verdict stays FAIL).** In its family x_l = εx̄_{dir} + ε²g every word has the same
order-ε log (Lx̄_μ), so Δ_j := Y_j − Ȳ = O(ε²) and the stationarity defect of e^{Ȳ}, Π(e^{−Ȳ}M) = −(1/12)avg[Δ, [Δ, Ȳ]] +
(1/6)avg Δ³ + …, is O(ε⁵) — beyond the truncation ε⁴, so C5 could not fire whatever the truth. The control was badly designed,
not the identity refuted. hg55_4 (new id, new criteria written first, motivation stated in them) repeats the comparison where
Δ = O(ε), and its control fires at ε³. hg55_3's C3/C4 pair (NC3 with its own control firing) is unaffected by C5; I still count
hg55_3 as FAIL overall, as pre-registered, and rely on it for NC3 only through C3/C4, saying so.
**What the checks cannot decide** (systemic defect 3): hg55_2-4 are at d = 2 (CEN2 itself is checked at d = 4 by hg55_1),
N ∈ {2, 3}, through ε⁴; none tests the analytic tails (Lemma CE), uniformity in k or T, or the linear theory (CC-INV, TOP-cc,
RT-cc) — those rest on proofs. Each gate can fail on its own object (A1/A4 if the average did not cancel; B2/B3 if a
non-r-linear ε³ plain term existed — B4 shows such a term is detectable; C3 if a cubic term existed — C4 shows one is
detectable; D1 if the envelope step or Re tr(ZG) = 0 failed — D4 shows a non-maximiser is detected).
Hashes (SHA-256): hg55_1.py b8db7399…c347, out 6341c06a…d762; hg55_2.py 6f0ae24a…efb1, out cb8b7b94…af45f; hg55_3.py
dcc94441…8bf5, out d6e2d2c9…3ec3a; hg55_4.py 71ea2984…0d4d, out 6f85c3eb…135; all *_err.txt empty.

## §9. Verdicts, agreement with Codex, and the summary table

### 9.1 Claims of others, with verdicts
| # | claim (file, locating string) | verdict | where |
|---|---|---|---|
| 1 | CODEX_REVIEW_TR §1 "criticality gives S*=Hx*−NB" (Step 0, composite co-closedness only) | **CONFIRMED** (re-derived) — agree | §1 |
| 2 | CODEX_REVIEW_TR §1: KFACTOR_O55 "Slots of S*" REFUTED "as a signed equality" | **CONFIRMED** — agree (norms unaffected) | §4.2 |
| 3 | CODEX_REVIEW_TR §2 / banked item 1: TR-1 for an actual source with the slot hypotheses | **CONFIRMED** as used — agree | §6 |
| 4 | CODEX_REVIEW_TR §3, item 5: full nonlinear promotion NOT-VERIFIED from that packet; the "sufficient repair" | **CONFIRMED** — agree; the repair is now supplied (HS-3) | §4.3 |
| 5 | CODEX_REVIEW_TR §3: "Even an O(η³) bound per level alone gives O(kη³)" | **CONFIRMED** as logic — agree; the actual higher-order rows decay geometrically, so it does not occur | §5 |
| 6 | CODEX_REVIEW_TR item 4 (C2-COF consequence with full-source bounds) | **CONFIRMED** as used — agree | §6 |
| 7 | CODEX_REVIEW_TOPCC §5 / item 4: Ñ_Σ and the conditional CC-CRIT; full nonlinear NOT-VERIFIED | **CONFIRMED** — agree; premise now supplied | §1, §6 |
| 8 | KFACTOR_OFF55 Lemma SG (identity) | **CONFIRMED** (hand; hg55_4 exact at N = 3) | §2 |
| 9 | KFACTOR_OFF55 SG consequences (i)-(ii) (gradient = κR^TΨ + κE_l, Ψ = ρ + O(ρ³)) | **CONFIRMED** | §2 |
| 10 | KFACTOR_OFF55 "every soft plain row, at every order, inherits whatever level decay the residual has" | **CONFIRMED with a load-bearing precision**: true up to an additive (ρ − r)-term that is geometric only by the S4' cancellation (hg55_2 B4) | §2, §5 |
| 11 | KFACTOR_OFF55 (LA-1)-(LA-3) ("ARGUED-standard") | statements **CONFIRMED**; proofs now written (§3) | §3 |
| 12 | KFACTOR_OFF55 Corollary SG-TR (full nonlinear Lemma TR given (LA)) | **CONFIRMED** (= Theorem TR∞) | §6 |
| 13 | KFACTOR_OFF55 ROW^{(σ)} (b)-(c), sizes at all orders, σ > 0 | **CONFIRMED** | §5 |
| 14 | KFACTOR_OFF55 ROW^{(σ)} (b), Lipschitz constants | **NOT-VERIFIED** (HS-Lip only ARGUED) | §4.4 |
| 15 | KFACTOR_OFF55 Lemma TOP♯ (T ≥ 3) | **NOT-VERIFIED** (ℓ¹ arithmetic re-done and right; FP input not re-checked; not used) | §2 |
| 16 | KFACTOR_O55 Lemma TR "(third order at the source's own ARGUED status)", "(+ higher order)" | **CONFIRMED** — the ARGUED step is now proved; TR-1..TR-4 hold for the full source with A_s → A_s^∞, A_j → A_j^∞ | §6 |
| 17 | BFT_A §3.9 table, row "third order … O(η³) with the same decays … ARGUED" | **CONFIRMED and sharpened**: residual-type third order has the second-order decay; plain third order decays geometrically (better than R^B) | §5 |
| 18 | BFT_A BA-4 / BA-5 (S4' second-order cancellation; X_0 = Ȳ + O(y³)) | **CONFIRMED** (re-derived; hg55_1) | §3.5 |
| 19 | BFT_A CR-1 (s^C residual-type) and BA-6 (κρ^{(2)} residual-type) | **CONFIRMED** each; **new: their commutator pieces cancel exactly** (net κȲ^{(2)}), so KFACTOR_O55's A_s and COFUN_CC §11.5's L^θ term are valid but not sharp | §4.3 (HS-d) |
| 20 | BFT_A Corollary WR (b) plain Wilson row "(∂q/∂x)^T(dx + q)" as the Wilson gradient | **CONFIRMED at second order**; it is the gradient of ½|log U_p|², not of Re tr(1 − U_p) — the omitted ∇𝒲(X) − X = O(|X|³) is now priced (§3.6) | §3.6 |
| 21 | COFUN_CC §11.5 Corollary CC-CRIT, "CONDITIONAL on Lemma TR and on Lemma TOP-cc" | **CONFIRMED**; its higher-order source premise is now discharged (CC-CRIT∞) | §6 |
| 22 | PROOF.md [S26-BANKED] Lemma TR bullet "NOT-VERIFIED: full nonlinear COF-crit / NCE (i)" | **CONFIRMED as of its writing**; should now read "PROVEN as an implication (HIGHER55), pending Codex review" | §9.3 |
**Counts (claims of others): CONFIRMED 20 · NOT-VERIFIED 2 (rows 14, 15) · REFUTED 0.**
Inputs used as banked and not re-judged: CODEX_REVIEW_TOPCC item 3 (CC-INV, TOP-cc, CC-FUN) and its lane-A/package inputs;
NA-alg (CONFIRMED-WITH-FIX); BA-3; the S6 bound |q| ≤ 9s².

### 9.2 Results of this file (status words; none has a Codex verdict)
| result | status | cross-check |
|---|---|---|
| Lemma AN (local analyticity, (R, S) independent of k, T, l, c) | PROVEN-HERE (standard; constants uncomputed) | = N5-an's method; REVIEW_BFT_B_S2 calls the density version routine |
| Lemma CE (Cauchy–Schwarz consequences) | PROVEN-HERE (standard) | — |
| (LA-1) explicit; (LA-2) |ρ − r| ≤ C_ρε_l³η²; (LA-3) Wilson all orders | PROVEN-HERE | (LA-2)'s S4' step: hg55_1 |
| Lemma C2 (â^{(2)} = S4' average of BCH₂; |â| ≤ C_aε_l³η²) | PROVEN-HERE (BA-4/BA-5 re-derived) | hg55_1 PASS |
| Lemma NC3 (no cubic term in the ŵ-chart) | PROVEN-HERE | hg55_3 C3 with C4 firing (N = 3) |
| Lemma FAC (exact slots; no level-(l+1) plain current; no positive-level G) | PROVEN-HERE (chain rule) | hg55_2 B1-B4 (order structure, N = 2) |
| Proposition HS / HS-3 (Codex TR §3's sufficient repair, literally) | PROVEN-HERE | hg55_2 B3/B4 (the third-order mechanism) |
| Proposition HS-Lip | ARGUED (not used) | — |
| Theorem TR∞ (TR-1, TR-2, TR-4 for the full source; level sum O(η²) k-uniform) | PROVEN as an implication | — |
| Corollary CC-CRIT∞ = full nonlinear COF-crit + NCE (i) (cc form) + CC-CRIT | PROVEN as an implication | — |

### 9.3 What should change in PROOF.md's tally / HANDOFF's critical path (no file edited by me)
1. **No tally move** (lane-level; the 105-item tally is not touched).
2. **[S26-BANKED], Lemma TR bullet:** after a Codex review of §3-§6, replace "NOT-VERIFIED: full nonlinear COF-crit / NCE (i) — the
   higher-order exact-source estimates remain an explicit obligation" by "full nonlinear COF-crit, NCE (i) (cc form) and
   CC-CRIT PROVEN as implications (HIGHER55 Theorem TR∞, Corollary CC-CRIT∞), k-, T-, Γ-uniform, trivial background, m = 0;
   local analytic constants R, S uncomputed". **Until that review, keep it NOT-VERIFIED.**
3. **HANDOFF critical path:** the higher-order exact-source obligation for the gauge-invariant half at Z = 1, m = 0 leaves the
   path (pending review). What remains for BFT-5 clause (b): (R1) gauge-variant components, (R2) background Z(V_k) incl.
   (CC-dec_Z), (R3) m > 0. What remains for BFT-0's construction: (GV^{(σ)})_Γ (OPEN) and the Lipschitz forms (HS-Lip, ARGUED);
   for the feasibility ledgers: the values of R, S.
4. Optional sharpening for the lane's constants: the second-order residual-type source is κȲ^{(2)} only (row 19).

UTC at end of writing: see the file's final stat. Files written: this file and checks/hg55_{1,2,3,4}_{criteria.md, .py,
out.txt, err.txt}. No git command was run; no other repository file was edited.

## §10. Final errata (after a full re-read of §0-§9; no conclusion changes)
1. §5 (b): the hypothetical x-linear, ŵ-quadratic cubic term would give ∇_xφ̃ ~ |ŵ|² ~ **ε_l⁴η²** own (no x-factor survives the
   x-derivative), not "ε_l·(ε_l²)²"; π_l ~ L^{−(k−l)}η²: still geometric, so the statement stands.
2. §4.3 (HS-b): C_{D2} is the (CE-2) constant of the degree-≥3 function â − â^{(2)}, whose sup on 𝔻_R is ≤ 2S (the degree-2
   Taylor polynomial is bounded by S there by Cauchy); with that, C_{D2} := 128√(N²−1)S/R³.
3. §4.4's heading "PROVEN-HERE (outline-complete)" is superseded by §4's erratum (3): **ARGUED**.
4. §1 quotes from CODEX_REVIEW_TR §3 and CODEX_REVIEW_TOPCC item 4 were re-checked against the files: verbatim.
Final stat follows this append.
