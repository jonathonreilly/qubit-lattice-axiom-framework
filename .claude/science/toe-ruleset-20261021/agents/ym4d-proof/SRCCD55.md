Reviewer model: claude-opus-5-5

# SRCCD55 — the two short-distance inputs (CD) conditional decay and (SRC) source-inserted RG: precise statements, relation to BFT / Theorem RW / LINEAR_PACKAGE, what can be proved, what is missing

## PRE-STATED — 2026-10-29T00:50:49Z (UTC, from `date -u`; written before any derivation in this file)

**Role.** Opus 5.5 worker (model ID above, verbatim from my system prompt), effort max. Rules: scratchpad
`REVIEW_BRIEF_55.md` (worker; the rules apply). No git. I write only this file and `checks/sc55_*`. Append-only.
Inputs read before this pre-statement: REVIEW_BRIEF_55.md (all); ROTDEF.md (all, incl. errata E1-E10);
CODEX_REVIEW_ROTDEF.md (all, as on disk; it ends with "Exactly what may be banked", so it looks complete);
PANEL_P1.md (all); UNIV55.md (on disk it holds ONLY its PRE-STATED block, 55 lines, last modified 19:43 — no
derivation to align with yet); the PRE-STATED blocks of BGT55/GV55/HIGHER55/NODEA_RES55 (headers only, to detect
symbol collisions: "source" there means the critical-point source of the background-field equation, not an
observable source). Not yet read: EXISTENCE.md §4, REVIEW_S22.md "Statement (BFT)", PROOF.md N5 / Theorem RW,
LINEAR_PACKAGE.md. No derivation for this file has been written.

**Targets.**
- T1. State (CD) and (SRC) precisely, with quantifiers, from (i) ROTDEF's actual use (I4; SRC-E/O/W; Theorem 7.1
  steps 5-6) as amended by CODEX_REVIEW_ROTDEF Findings 3-5, and (ii) what OS0/H_reg needs (PANEL_P1 §1 table and §3
  item 1; EXISTENCE.md §4 "What needs more than stability"). Give the finite operator list and the norm.
- T2. Relate them to what the lane has: BFT-3 (locality, derivatives to order 4, exponential tree decay), BFT-4
  (polymer representation), PROOF's N5 / Theorem RW (random-walk covariance bounds), LINEAR_PACKAGE. Decide whether
  (CD) follows from the RG's conditional structure, and what source insertions add to BFT's induction.
- T3. Prove what can be proved, CONDITIONAL on named layer-1 inputs; state exactly what is missing. Align with UNIV55
  (only its pre-statement exists now; re-check before closing).
- T4. Rate: check whether SRC-O's O(g_bare²) mixing is consistent with ROTDEF §9 item 3's "at best logarithmic in a".

**What would count as a refutation, stated before deriving.**
- Of ROTDEF's formulation of the inputs:
  - R-a. SRC-E as written is not satisfiable with a non-vacuous normalization (CODEX_REVIEW_ROTDEF Finding 4 flags
    this: ν_K[(E_K G)²] + ν_K[Var(G|U_K)] = ω(G²) and Var(O_a f) ~ a⁻⁴ by ROTDEF's own power counting). If I can
    show that any Z_e making a separated correlator O(1) forces ω(O_a(f)²)/Z_e² → ∞, SRC-E is REFUTED as stated, and I
    must give the corrected (separated-support / coarse) moment statement that ROTDEF's proof actually uses.
  - R-b. CD as written (pointwise-in-x bound with ν_K-averaged prefactor, uniformly in a, R, s) is FALSE for some
    reason forced by the structure — e.g. the conditional measure given U_K is not massive in some direction (gauge
    zero modes, or large-field regions where the conditional fluctuation is not small), or the conditional covariance
    of two local functionals decays only polynomially because the coarse field is held fixed only through block
    averages (the fine field still has long-range modes inside a block-constant constraint?).
  - R-c. A term in ROTDEF's Theorem 7.1 that needs more than the stated CD/SRC (e.g. the insertion-side contact
    term of Codex Finding 3 is not covered by SRC-W's statement), so that the input list is incomplete.
- Of the claimed link to the lane's machinery:
  - R-d. "CD follows from the RG's conditional structure" is refuted if the lane's conditional covariance bounds
    (Theorem RW / N5 / BFT-3) are only for the linearised Gaussian measure at trivial background, or only in the
    small-field region, with no handle on the full conditional law, so that CD requires a new conditional
    cluster expansion (with large fields inside the fine scales) that the lane does not have.
  - R-e. "Source RG is linear in the sources" is refuted for the needed objects if the source-inserted effective
    action is needed to second order in the sources (two-point functions!) with the second-order coefficients
    (the contact/mixing terms) not controlled by a linear recursion.
- Of my own work: a check that cannot fail; a bound uniform only on the small-field set presented as uniform; a
  "source" (critical-point) / "source" (observable) collision; a statement whose quantifier order (sup over U_K
  inside or outside ν_K) differs from the consumer's.

**Labels.** PROVEN-HERE (complete argument in this file), CONDITIONAL (named inputs), ARGUED (stated gap), OPEN,
[m] (literature from memory, unverified). Verdicts on inherited claims: CONFIRMED / NOT-VERIFIED / REFUTED.

**Numeric checks.** Only if a number decides something; `checks/sc55_<id>_criteria.md` first, exact rational
arithmetic in plain python.

---

## 0. Result in one page (proofs and locators in §2-§9; every label is argued where the claim is made)

**(CD) is not an independent input; it is the off-diagonal part of (SRC).**
- *Exact structure (Proposition B, PROVEN-HERE; exact check `checks/sc55_tel` PASS, both controls fired).* The soft chain
  is a Markov chain in the level index. Hence, for fine observables G, H,
  **Cov(G, H | U_K) = Σ_{i<K} E[ Cov(E[G|U_i], E[H|U_i] | U_{i+1}) | U_K ]**, and the one-step conditional law
  P(dU_i | U_{i+1}) ∝ e^{-S_i(U_i)} K_i(U_{i+1}, U_i) dU_i is exactly the integrand of one RG step at fixed U_{i+1}.
  So conditional decay at the reference scale is assembled from **per-step** fluctuation decay (linear part: N5 / Theorem RW;
  nonlinear part: N6 + Theorem CE) applied to the level-i images, which the source-inserted RG controls.
- *Equivalently (Proposition A, PROVEN-HERE as an implication):* CD is the mixed second/third source derivative, at
  separated supports, of a polymer representation of the conditional source-inserted generating function (the conditional
  form of EXISTENCE's H-Bal-loc, which has **no unit-scale remainder** because U_K is not integrated).
- Nothing in either route uses the coarse law ν_K beyond local large-field probabilities. The rate is the soft-constraint
  mass at scale ℓ_ref: a conditional mass, not a physical gap (P1 §4's warning is respected: only conditioning is used).
- **The lane does not supply CD today.** PROVEN in the lane: the linear one-step covariance decay at the trivial background
  (every level) and at curvature-small backgrounds at level 0 (PROOF "N5 node", Corollary RW-triv, Theorem N5-sf0). OPEN:
  N6 (per-step polymer bound), N5 at levels ≥ 1 at general small backgrounds, all source-inserted versions, and the
  conditional large-field analysis. BFT-3 is a deterministic background-locality statement, not a covariance bound.
- "Uniformly in the coarse field" holds at best in **effective-distance** form (large-field coarse cubes count zero length);
  ROTDEF's ν_K-averaged form (I4) then follows from a coarse Peierls bound (Proposition C, PROVEN-HERE as implication),
  which on hypercubic tori is EXISTENCE's chessboard Lemma CBE + (RLF-3^dis).

**(SRC), stated precisely (§3).** One statement in four clauses: **SRC-κ** (conditional joint-cumulant bounds for a finite
operator list at mutually separated points: multiscale short-distance weight, exponential decay at scale ℓ_ref, uniform in
a, R and the small-field coarse field; effective-distance form for large coarse fields), **SRC-M** (matching: at most eight
finite H(4)-split constants, each O(g_bare²), with O(a²𝔏) remainders), **SRC-I** (coarse local integrability), and the
mechanism **SRC-poly** (conditional multiscale polymer representation, analytic in a complex e-source on a fixed polydisc),
which implies SRC-κ (Proposition A).
- **Finite operator list** 𝒪_rot: e_a; τ_ν, τ_{μν} (the observable's Ward variations; ROTDEF's t_ν, A_J are combinations);
  𝒯_{μν} (the identity's own current); 𝔴_{b,ν} (the Ward density). That is 1 + 4 + 16 + 10 + 16 = 47 real local
  gauge-invariant functionals per site, range ≤ 3a. Only e_a needs sources to all orders (two-point function, and OS0); the
  other 46 enter linearly (one insertion each).
- **Norm.** Sup norm on complex e-sources (polydisc of fixed radius r_0); pointwise conditional-cumulant weights
  Π_i w_{α_i}(δ_i)·e^{-m_c·tree/ℓ_ref} for the output; BFT-4-type polymer norm for the mechanism.

**Corrections to ROTDEF's inputs (each needed; none changes Theorem 7.1's conclusion).**
1. **SRC-E is REFUTED as a member of any non-vacuous input set.** Lemma V (PROVEN-HERE, unconditional for g_0 small;
   constants certified by `checks/sc55_vm`): **Var_ω(O_a(f)) ≥ 1.5·10⁻⁶ g_0⁴ a⁻⁴ (‖f‖²₂ − O(a))**, uniformly in the torus.
   SRC-E plus a non-vacuous normalisation of D would force the *unnormalised* separated correlator of e_a to diverge like
   g_0⁴a⁻⁴. That contradicts every polylogarithmic separated bound, in particular SRC-κ. ROTDEF uses only the replacement
   **SRC-E′** (coarse-image moments and separated conditional cumulants). This agrees with Codex Finding 4 and
   strengthens it from "proof obligation" to "inconsistency".
2. **SRC-W must carry an O(g_bare²) contact term** (Codex Finding 3; I agree). Call the result SRC-W′. Theorem 7.1's error
   already contains g_bare², so its conclusion is unchanged.
3. **CD's prefactor** must be built from coarse images, not conditional variances, and must be ν_K-averaged (Codex
   Finding 5; I agree). Under SRC-poly, coarse images are **quasi-local** (Proposition F). Strict locality is false in
   general (Codex's two-site example) and is not needed.

**OS0 / H_reg (§2.2, Proposition E).** OS0 needs SRC-κ for {e_a} at all orders, plus SRC-I. It needs **no decay of the
coarse law**, only bounded coarse cumulants of local functionals. It is posed in OS's non-coincident form (^0𝒮) [m], so
coincident-point contact renormalisation (EXISTENCE's H-src′-diag) is not needed for the OS axioms [m].
- **PANEL_P4 §2.1's local-moment hypothesis is FALSE for point-like dimension-4 composites** (Lemma V). Its label "OPEN"
  is right only for flowed fields.
- EXISTENCE X-SRC-GAP's ARGUED variance divergence is now PROVEN (Lemma V).

**What sources add to BFT's induction (§5.4).**
- (i) Marginal sources (e, 𝒯) are **variable coefficients**: a complex, position-dependent coupling field. BFT, N5, N6,
  RLF and (F_R) must therefore hold uniformly over a sup-norm ball of coefficient fields. This is the same "slowly varying
  coupling" technology as PANEL_P4's S⁴ route, S4(a).
- (ii) The first-order source dependence evolves by the linearisation DR_k of the RG step at the source-free trajectory,
  so it is **exactly linear**. Second order is linear with a quadratic inhomogeneity (triangular). All orders follow by
  Cauchy from analyticity on a polydisc. The pre-stated refutation R-e does not occur.
- (iii) The irrelevant insertions (t, A, bulk Ward density) need a **localisation operator** that extracts the finitely
  many H(4)-allowed marginal constants. BFT-4's single polymer norm does not do this.
- (iv) Field-independent source counterterms cancel in separated cumulants (EXISTENCE Lemma X-SRC-CT).
- (v) The background's response to an e-source is a **divergence-form source problem**, d*(2ηF(Z)), which is the lane's
  own G♯ source class (LINEAR_PACKAGE Theorem 6.8 at the trivial chain; BFT-5 at curved backgrounds).

**Rate (§7).** SRC-O's O(g_bare²) is consistent with a logarithmic rate: under (F_R), g_bare² ≍ 1/(β log(ℓ_ref/a)).
"At best logarithmic" is a property of the route's split into separate inputs, not of the defect. The observable-side ϑ_R
and the insertion-side c_R multiply the same H(4)-split structures. A single joint input (SRC-OW: their anisotropic
differences are O(a²𝔏)) would give a power rate. Symanzik power counting [m] predicts SRC-OW, but only by presupposing an
O(4)-invariant limit, so SRC-OW is OPEN. P1 does not need a rate.

**UNIV55 (§8).** On disk it holds only its pre-statement, so there is nothing to duplicate. The shared UV statement
(proposed here) is a per-block bound on the conditional coarse image of the bulk Ward density. By ROTDEF Lemma 5.3(ii) that
image equals E_K[Ξ_v log K_0] exactly, the conditional mean of the first kernel's response to the local rotation field. The
bound is the infinitesimal-rotation form of PANEL_P4's S2(ii) per-block universality. SRC-W′'s bulk part follows from it
plus CD and SRC-E′, by Cauchy–Schwarz per block, with no decay used (Proposition D).

---

## 1. Symbols (collision check, REVIEW_BRIEF_55 defect 1)

| Symbol here | Meaning here | Collides with (file: locating string) | Resolution |
|---|---|---|---|
| SRC | the observable-source-inserted RG of this file (ROTDEF I5) | LINEAR_PACKAGE "Lemma 6.5 (SRC-id and SRC-all": sources j_l of the **critical-point equation** | written "LP-SRC" when meant |
| "source" | an external field η coupled to a local gauge-invariant operator | BFT-5 clause (b) / HIGHER55 "S_full (the actual critical-point source)"; LINEAR_PACKAGE §1.3 "With sources (RTARGET §33)" j_l = d_l^*G_l | the latter are "critical-point sources" |
| η | complex e-source field on fine sites (EXISTENCE §10.3's coupling field) | BFT-1/RTARGET weights η? none found in the cited text | — |
| J | rotation generator in so(4) (ROTDEF) | ROTDEF also writes source "J" nowhere; EXISTENCE §10.3 uses h, η, z | sources are η, never J |
| m_c | CD decay rate, in units of 1/ℓ_ref (ROTDEF I4) | BFT-3 m_0 (background locality); PROOF Theorem RW m, m_cov (per-step covariance); LINEAR_PACKAGE m_*, m_*′ (tree-level response) | four distinct rates; relations stated in §5 |
| κ_n(·\|U_K) | conditional joint cumulant of order n | κ_j soft couplings (BFT data); κ, κ_0 polymer decay / entropy constants (Theorem CE) | cumulants always carry "(… \| U_K)" |
| 𝒮_K, 𝔏(U_K) | coarse small-field set; coarse large-field cube set (§3.1) | P1's 𝒮 (Schwartz); ROTDEF's 𝔏(a) (log factor) | log factor written 𝔏(a) with its argument |
| ϑ_R, c_R, Z_R | observable-side mixing (ROTDEF §4.2), insertion-side contact (Codex F3), current normalisation; R ∈ {1, 3, 6′} | — | — |
| w_α(δ) | short-distance weight of operator α | ROTDEF ω (state) | — |
| ℓ_r | L^r a, level-r spacing; ℓ_K = ℓ_ref = 1 | RLARGE "levels" convention (level 0 fine) | RLARGE convention, as ROTDEF |
| K | number of RG levels (ROTDEF, RLARGE) | K_i (soft kernels), K_0 (Theorem CE constant) | kernel K_i always indexed; Theorem CE constant written K_0^{CE} |
| u_0 | 1/g_bare² (Wilson coefficient) | u_k in (F_R) is the level-k inverse coupling | u_0 = level-0 member of (F_R)'s sequence (consistent) |

---

## 2. What the two consumers actually use

### 2.1 ROTDEF (read in full on disk, incl. errata E1-E10), as amended by CODEX_REVIEW_ROTDEF (read in full; complete)
Every place ROTDEF consumes CD or SRC, located by string. Lines are as on disk at 2026-10-29T00:50Z.
| Use | Locating string (ROTDEF line) | Object actually needed |
|---|---|---|
| U1 | Theorem 7.1 step 5, "By I4: \|ν_K(Cov(F_s,𝔗_r\|U_K))\|" (l.388-390) | ν_K-average of Σ_{x∈Sh} a⁴\|Cov(F̃_s, 𝒯_{μν}(x) \| U_K)\|, with x at distance ≥ r − ρ_F − 1 from supp F |
| U2 | step 6, "Cov_ω(F_s, 𝔅(v_r)) is bounded by SRC-W" (l.391) | the full covariance of F̃_s with the bulk 𝔅(v_r): contact region near supp F, bulk ball, shell corrections |
| U3 | step 6, "and 𝒞(s) by SRC-O" (l.391) | 𝒞(s) = Σ_x a⁴f_s(x)ω_c([(Jx)^νt_ν(x) + A_J(x)]Ō(g_s)) + (f↔g) + O(a²): two-point functions of t_ν, A_J at supp f with e_a at supp g |
| U4 | "ϑ₁ (§4.2) multiplies d/ds ω(F_s) itself. Under SRC-E that derivative is O(Z_e²)" (l.394) | \|dω(F̃_s)/ds\| = \|ω_c(O(Jf_s)O(g_s)) + ω_c(O(f_s)O(Jg_s))\|: **separated** two-point functions only |
| U5 | §8.1 "local moments plus Cauchy–Schwarz give only \|TQ_ν\| ≤ C Z_e²(r/ℓ_ref)⁴" | ν_K-second moments of the coarse images E_K F̃_s and E_K 𝒯(x) |
| U6 | I4's prefactor "ν_K(C_G) ≤ C Z_e²" (l.349) | a ν_K-integrable prefactor; Codex F5: "This averaged version is sufficient for the displayed proof" |
| U7 | §8.4 "Call this input **SRC-iso**" (l.496) | used only for the ARGUED scale-separation remark; not used by Theorem 7.1 |
Codex amendments that change the inputs:
- **F3** (CODEX_REVIEW_ROTDEF "## Finding 3"): a symmetry-allowed finite contact a²R_{7,ν}(x)e(y) ⊃ cδ(x−y)∂_μX_{μν}(y)
  survives on the insertion side and contributes c·Cov_ω(O_a(Jf), O_a(g)) and two stress structures. **I agree.** The
  dimension count is 7 + 4 − 2 = 9 = 4 + 5, the operator is V-valued, and inversion parity allows odd dimension in V.
  Summation by parts kills only the J^ν_μX_{μν} term, exactly as Codex writes. So U2 contains an O(g_bare²) contact term,
  by the same one-loop power counting as SRC-O (a² × a⁻² × g_0²).
- **F4** ("## Finding 4"): SRC-E's left side equals ω(G²), so it bounds fine-field second moments. **I agree.** I
  strengthen this to an inconsistency in §2.3.
- **F5** ("## Finding 5"): CD in ν_K-averaged form suffices; strict coarse locality is NOT-VERIFIED; the one-covariance
  reduction does not need it. **I agree.** Proposition F gives quasi-locality under SRC-poly.
- **E4** (ROTDEF §13): F_s is read as the centred product F̃_s. Every object above is for F̃_s.

### 2.2 OS0 / H_reg
- PANEL_P1 §3 item 1 ("CONDITIONAL — H_reg", l.56) asks for "Joint observable moments [with] cutoff- and
  volume-uniform continuity/growth bounds sufficient for OS0", convergence on a dense family, and renormalised identities.
  PANEL_P1 §1's table row "OS0: regularity" adds "control of coincident-point renormalization in the chosen formulation"
  and "growth in the number of insertions sufficient for the reconstruction theorem actually invoked".
- EXISTENCE §4 ("What needs more than stability", l.590):
  - X-MOM proves OS0 from an exponential-moment hypothesis H-src(Φ).
  - X-SRC-GAP (l.617) says H-src fails for dimension-4 composites (ARGUED) and that the right form is separated supports
    plus "UV stability with a position-dependent bare coupling g_0(x)".
  - §10.3 (l.1081-1135) formalises this as H-src′ (separated supports, inclusion–exclusion), Lemma X-SRC-CT (local
    counterterms drop out, PROVEN-HERE) and H-Bal-loc (a multiscale polymer representation of log Z[1/g_0² + η] with a
    unit-scale remainder R_K, |R_K| ≤ C_IR "in finite physical volume |T|"). Lemma X-SRC-RED (PROVEN-HERE | H-Bal-loc)
    derives H-src′ from it.
  - H-src′-diag (coincident points) is marked OPEN.
- PANEL_P4 §2.1 ("OS0 on R^4 needs no decay of correlations. PROVEN (implication)", l.111-118) assumes
  E|Φ(f)|^n ≤ A^n(n!)^βN(f)^n for f supported in a unit cube. It says the input "(local moment bounds for dimension-4
  composites or flowed fields) is UV ... and OPEN".
- **What OS0 needs, precisely (my reading; [m] where marked).** OS's axiom E0 places the Schwinger functions in the dual of
  ^0𝒮(R^{4n}), the test functions vanishing with all derivatives on coincident points [m: Osterwalder–Schrader 1973; P1 §7
  checked only OS II's introduction]. OS II adds the linear growth condition E0′ [m]. So OS0 for the point-like field e
  needs:
  - (a) **pointwise bounds on separated n-point functions** at all separations δ ≥ ca, with at most a power singularity
    δ^{−p_n} (p_n linear in n) and factorial growth in n, uniformly in a and R;
  - (b) convergence on a dense family.
  It does **not** need coincident-point counterterms (H-src′-diag) or exponential moments of smeared point-like
  composites. Fixed-δ H-src′ (EXISTENCE) is too weak by itself: δ-uniformity with an explicit power is needed. X-SRC-RED's
  sum Σ_r L^{4r}e^{−(κ−κ_0)δL^r/M} ~ δ^{−4} shows the multiscale representation delivers it.

### 2.3 Lemma V — the fine-field variance of the smeared clover density diverges (PROVEN-HERE)

**Setting.** Wilson measure ω on a hypercubic torus Λ = (aZ/RZ)⁴ with R/a even, SU(N), N ≥ 2, u_0 = 1/g_0². Here
O_a(f) = Σ_x a⁴f(x)e_a(x) as in ROTDEF §2.2, f ∈ C_c^∞ supported in one fundamental domain.

**Lemma V.** There is u_*(N) < ∞ such that for u_0 ≥ u_*(N), every such torus and every such f,
  **Var_ω(O_a(f)) ≥ (c_v/1152)·g_0⁴·a⁻⁴·[‖f‖²₂ − 24a‖∇f‖_∞‖f‖₁ − O_f(a^M)],   c_v := 8e^{−5}/π³,**
for every M. Here c_v/1152 ∈ [1.509·10⁻⁶, 1.510·10⁻⁶], certified in exact rational interval arithmetic by `checks/sc55_vm`
(criteria first; verdict PASS; its control, the false claim c_v ≥ 0.0018, was rejected).

*Proof.*
- **Step 0 (the observable is a sum of plaquette energies).** Each plaquette p lies in exactly the clovers of its 4 corners,
  and the ordered pairs (μ,ν) count its plane twice. Hence
  O_a(f) = Σ_p h(p)s(U_p), with h(p) := ½Σ_{x∈corners(p)}f(x).
  (For f ≡ 1 this gives 2Σ_p s(U_p), matching ROTDEF §2.2.)
- **Step 1 (a priori bound on E s(U_p); volume-uniform).**
  - Put Z(u) := ∫exp(−uΣ_p s(U_p))dU (Haar probability) and F(u) := −|P|⁻¹log Z(u), where |P| = 6|Λ| is the number of
    plaquettes. Then F(0) = 0. F ≥ 0 because s ≥ 0 gives Z ≤ 1. F is concave because log Z is a log-Laplace transform.
  - F′(u) = E_u[s(U_p)] for every p, since translations and H(4) act transitively on plaquettes of the hypercubic torus.
  - Concavity gives F′(u) ≤ (F(u) − F(u/2))/(u/2) ≤ 2F(u)/u.
  - Lower-bound Z on B_δ := {d(U_b, 1) ≤ δ ∀b}, with d the bi-invariant distance d(e^X, 1) = |X|_F (eigenphases in [−π, π]).
    There d(U_p, 1) ≤ 4δ, and s(e^X) = 1 − N⁻¹Σcos θ_j ≤ |X|²_F/(2N). So s(U_p) ≤ 8δ²/N.
  - Haar(B_δ) ≥ c_Nδ^{N²−1} for δ ≤ δ_N, because Haar measure has a smooth positive density in exponential coordinates.
    With 4|Λ| links:
    F(u) ≤ (2/3)[(N²−1)log(1/δ) + log(1/c_N)] + 8uδ²/N.
  - Take δ = u^{−1/2}. This gives F(u) ≤ ((N²−1)/3)log u + C_N, hence **E_u[s(U_p)] ≤ 2u⁻¹[((N²−1)/3)log u + C_N] → 0**,
    with no volume dependence.
  - Fix u_1(N) with E_u[s] ≤ 11/(12N) for u ≥ u_1.
- **Step 2 (a sparse set of conditionally independent links).**
  - Let S := {b = (x, x + ae_1) : x ∈ (2aZ)⁴ ∩ Λ}. A plaquette through b lies in a (1,ν) plane. Its other e_1-link is based
    at x ± ae_ν ∉ (2aZ)⁴, and its ν-links are not in S. So **no plaquette contains two links of S.**
  - Let 𝔉 := σ(U_b : b ∉ S). Given 𝔉, the (U_b)_{b∈S} are independent with laws
    μ_{u_0,Y_b}(dU) ∝ exp(u_0N⁻¹Re tr(UY_b))dU. Here Y_b := Σ_{p∋b}X_{p,b} (6 staples in d = 4) and U_p ~ U_bX_{p,b} up to
    inversion, which leaves Re tr fixed.
  - Correspondingly O_a(f) = Σ_{b∈S}ψ_b + (𝔉-measurable), with ψ_b := −N⁻¹Re tr(U_bY^h_b) + const and
    Y^h_b := Σ_{p∋b}h(p)X_{p,b}.
  - The law of total variance and conditional independence give **Var(O_a(f)) ≥ Σ_{b∈S}E[Var(ψ_b | 𝔉)].**
- **Step 3 (one link, through a circle subgroup).** Fix Y, Y^h and t := u_0. Let T := diag(i, −i, 0, …, 0) ∈ su(N); then
  C := {e^{sT}} is a closed circle subgroup.
  - Haar measure disintegrates over the left cosets CV with uniform ds/2π on each coset. So under μ_{t,Y} the conditional
    law of s given the coset is ∝ exp(tN⁻¹Re tr(e^{sT}VY))ds.
  - With w_j := (VY)_{jj}: Re[e^{is}w_1 + e^{−is}w_2] = Re[e^{is}z], where z := w_1 + w̄_2. So the conditional law is von Mises
    vM(κ, s_0) with **κ = t|z|/N**.
  - Likewise N⁻¹Re tr(e^{sT}VY^h) = A cos(s − s_h) + const, with A = |z^h|/N and z^h := (VY^h)_{11} + conj((VY^h)_{22}).
  - Under vM(κ, s_0), cos(s − s_0) and sin(s − s_0) are uncorrelated (odd symmetry). Hence
    **Var(ψ_b | 𝔉, coset) ≥ A²v(κ)**, with v(κ) := min(Var_κ cos θ, E_κ sin²θ) and θ ~ vM(κ, 0).
- **Step 4 (the coset amplitude is large on a likely event).**
  - For every U = e^{sT}V on the coset, Re(UY)_{11} + Re(UY)_{22} = Re(e^{is}z) ≤ |z|.
  - |(UY)_{jj}| ≤ ‖Y‖_op ≤ 6 and N⁻¹Re tr(U_bY_b) = 6 − Σ_{p∋b}s(U_p). Together these give
    |z| ≥ Re tr(UY) − 6(N−2) = 12 − NΣ_{p∋b}s(U_p) at the actual U_b. Also |z| ≤ 12.
  - So G_b := {Σ_{p∋b}s(U_p) ≤ 11/N} ⊂ {|z| ≥ 1}. By Markov and Step 1, P(G_b) ≥ 1 − 6E[s]N/11 ≥ 1/2 for u_0 ≥ u_1.
  - Next, ‖Y^h_b − h_bY_b‖_op ≤ 6ω_b with h_b := 2f(x_b) and ω_b := max_{p∋b}|h(p) − h_b| ≤ ½(2 + √2)a‖∇f‖_∞ ≤ 2a‖∇f‖_∞.
    Hence |z^h − h_bz| ≤ 12ω_b, and on {|z| ≥ 1}: **A ≥ (|h_b| − 12ω_b)₊/N.**
- **Step 5 (von Mises bounds; elementary, constants certified).** For κ ≥ 4:
  - Let B := {|θ| ≤ κ^{−1/2}} and A′ := {2κ^{−1/2} ≤ |θ| ≤ 3κ^{−1/2}}.
  - On B, cos θ ≥ 1 − 1/(2κ). On A′, cos θ ≤ 1 − 2/κ + 2/(3κ²). The gap is ≥ (3κ − 4)/(6κ²) + 1/κ ≥ 1/κ.
  - With density ∝ e^{κ(cos θ−1)}, the normaliser is ≤ π^{3/2}/√(2κ), because 1 − cos θ ≥ 2θ²/π² on [−π, π]. This gives
    P(B) ≥ 2√2e^{−1/2}/π^{3/2} ≥ 0.308 and P(A′) ≥ 2√2e^{−9/2}/π^{3/2} ≥ 0.00564.
  - Two-event bound: Var(X) = ½E(X − X′)² ≥ P(A′)P(B)·gap². So Var_κ cos θ ≥ c_v/κ².
  - Also E_κ sin²θ ≥ P(A′)sin²(2κ^{−1/2}) ≥ P(A′)·2.7/κ ≥ c_v/κ².
  - So **v(κ) ≥ c_v/κ² for κ ≥ 4.**
- **Step 6 (assembly).**
  - On {|z| ≥ 1}, κ ∈ [u_0/N, 12u_0/N], so for u_0 ≥ 4N we get v ≥ c_vN²/(144u_0²). With Step 4,
    A²v ≥ (|h_b| − 12ω_b)₊²c_v/(144u_0²).
  - Conditioning on 𝔉 ∨ σ(coset) inside Step 2's bound, and P(|z| ≥ 1) ≥ 1/2, give
    E Var(ψ_b|𝔉) ≥ (c_v/288)u_0⁻²(2|f(x_b)| − 24a‖∇f‖_∞)₊².
  - Sum over x_b ∈ (2aZ)⁴. The Riemann sum with cell 16a⁴ is exact to O(a^M) for C_c^∞ functions (Poisson summation).
  - u_*(N) := max(u_1(N), 4N, 1/δ_N²). ∎

**Consequences (each a verdict on an inherited item).**
- **(V-1) ROTDEF SRC-E (l.353): REFUTED as a member of any non-vacuous input set.**
  - Take any normalisation with sup_a Z_e⁻²Var(O_a(f)) ≤ C (SRC-E for G = O_a(f)). Lemma V then forces
    Z_e² ≥ c g_0⁴a⁻⁴‖f‖²/C.
  - Non-vacuity of D's normalisation means Z_e⁻²ω_c(O_a(θg)O_a(g)) ≥ c_0 > 0 for one reflected pair. ROTDEF §2.2's "Guard
    against a vacuous pass" requires it; it is not supplied there.
  - Together these force **|ω_c(O_a(θg)O_a(g))| ≥ c_0c g_0⁴a⁻⁴‖f‖²/C**: a power-law divergence of an *unnormalised*
    separated two-point function.
  - That contradicts any polylogarithmic bound on separated correlators of e_a, in particular SRC-κ below. So no input set
    containing SRC-E, SRC-κ (or any OS0 for e) and non-vacuity is consistent.
  - The same applies to SRC-E's clause for G = O_a(f)O_a(g). Its conditional variance contains Var(O_a(f)|U_K) times a
    separated factor.
  - **Repair:** SRC-E′ (§3.5). Every ROTDEF use, U4-U6, needs only SRC-E′.
- **(V-2) ROTDEF §11 row 25 ("Normalizing by Var(O_a(f)) would be vacuous (∼a⁻⁴ divergence)", ARGUED): CONFIRMED**, with one
  correction. The proven size is ≥ c g_0⁴a⁻⁴, i.e. a⁻⁴/log²(ℓ_ref/a) under (F_R), not a⁻⁴. The conclusion is unchanged.
- **(V-3) EXISTENCE X-SRC-GAP sub-point "its variance diverges like ε^{-4}∫f² … so H-src in exponential form fails"
  (ARGUED): CONFIRMED (now PROVEN).** For the u_0-weighted density there, Lemma V gives u_0²·c g_0⁴a⁻⁴ = c a⁻⁴.
- **(V-4) PANEL_P4 §2.1, "The input itself (local moment bounds for dimension-4 composites or flowed fields) is … OPEN":
  REFUTED for dimension-4 point-like composites.**
  - The implication in §2.1 is correct. Its hypothesis E|Φ(f)|² ≤ A²2^βN(f)², uniform in the cutoff, is **false** for
    Φ = Z⁻¹(O_a(f) − ω(O_a(f))) under every normalisation Z that keeps separated correlators non-vacuous. The argument is
    the same as V-1.
  - So for point-like composites, OS0 must go through §2.2(a) (separated, non-coincident form). Local moment bounds remain
    a possible (OPEN) route only for flowed fields.
  - The same correction applies to P4's §2 table cell "position-uniform local exponential-moment bounds for the local
    fields (H-src'/H-src-flow)". H-src′ is a separated-support statement, not a local moment bound.

---

## 3. Precise statements of (SRC) and (CD)

### 3.1 Setting (fixed; every quantifier explicit)
- **Data.** N ≥ 2; L ≥ 3 odd; soft couplings κ_j ∈ [κ_-, κ_+]. The soft chain is that of ROTDEF §5.1: RLARGE "The exact
  chain", with kernels from PROOF "Decision 4: the RG kernel", W_ch = e^{−S(U_0)}Π_{i<K}K_i(U_{i+1}, U_i) and
  ∫K_i dU_{i+1} = 1. Levels run 0 (fine, spacing a) to K (reference, spacing ℓ_ref = L^Ka = 1).
- **Tori.** Hypercubic, side R with R/a even and R/ℓ_ref ∈ ℕ. The coupling sequence is the chain's own, obeying (F_R) of
  RLARGE "Flow hypothesis (F_R)" (l.98) with g_K = g_ref ≤ min(g_thr, γ_0) fixed (ROTDEF I3).
- **Conditioning.** E_K := E[·|U_K], ν_K := law of U_K. κ_n(G_1, …, G_n | U_K) is the conditional joint cumulant.
- **Coarse small-field set and large-field cubes.** Fix the polymer block side M (in units of ℓ_ref). 𝒮_K is the set of
  U_K with max_P|log U_{K,P}|_op ≤ ε_0 (BFT's ε_0 at level K). For general U_K, 𝔏(U_K) is the set of level-K M-cubes
  containing a plaquette that violates this bound.
- **Distances.** dist is the Euclidean distance in physical units (ℓ_ref = 1). For two sets A, B,
  d_𝔏(A, B) := min over *-connected M-cube paths γ from A to B of #(γ \ 𝔏(U_K)), so large-field cubes cost zero length.
  tree(A_1, …, A_n) is the minimal spanning-tree length.

### 3.2 The finite operator list, its symmetry content, and the norms
For x a fine site (b a fine bond):
| Operator | Definition (locating string) | H(4)_x content | Range | How it enters |
|---|---|---|---|---|
| e_a(x) | clover energy density, ROTDEF §2.2 "e_a(x) := (4a⁴)⁻¹" | 1 | a | sources η to all orders (two-point functions; OS0) |
| τ_ν(x), τ_{μν}(x) | Ξ_ve_a(x) = Σ_bv^ν(m_b)θ_{b,ν}(x); τ_ν := Σ_bθ_{b,ν}, τ_{μν} := Σ_b(m_b−x)_μθ_{b,ν} (ROTDEF §4.2) | V (4); V⊗V = 1 ⊕ 3 ⊕ 6′ ⊕ A (16) | 2a | one insertion. ROTDEF's t_ν = τ_ν − ∇̄_νe_a and A_J = J^ν_μτ_{μν} are linear combinations |
| 𝒯_{μν}(x) | "the identity's own current", ROTDEF §4.3 and the supplement l.566. **Existence is part of SRC-M** | Sym²V = 1 ⊕ 3 ⊕ 6′ (10) | ≤ 3a | one insertion (shell flux 𝔗_r) |
| 𝔴_{b,ν} | 𝔚(v) = Σ_bΣ_νv^ν(m_b)𝔴_{b,ν}. This exists by ROTDEF §3.2 (Lin): ΞS and div Ξ read v only at midpoints, linearly | V per bond (4 bonds × 4) | 2a | one insertion (bulk 𝔅 and its contacts) |
Total: 1 + 4 + 16 + 10 + 16 = **47 real gauge-invariant local functionals per site**. Every one is smooth in U and
gauge invariant: for 𝔴 by ROTDEF §3.2 (G), for τ because Ξ_v commutes with gauge transformations and e_a is invariant.
For OS0 the minimal list is 𝒪_0 := {e_a}. It extends verbatim to any finite list of local gauge-invariant composites,
for example the pseudoscalar density.

**Norms.**
- (N1) e-sources: complex η on fine sites with ‖η‖_∞ ≤ r_0, a fixed radius independent of a and R. The source term
  Σ_xa⁴η(x)e_a(x) = Σ_p h_η(p)s(U_p) is a position-dependent shift of the Wilson coefficient u_0 by O(r_0). Relative to
  u_0 that is O(r_0g_0²), so the polydisc is natural.
- (N2) Linear insertions: no source norm is needed (pointwise in x).
- (N3) Output: pointwise conditional-cumulant bounds with weight W(x_1, …, x_n) := Π_iw_{α_i}(δ_i)·e^{−m_c tree_ℓ/ℓ_ref}.
  Here δ_i := min_{j≠i}|x_i − x_j|, w_α(δ) := δ^{−d_α}𝔤_α(δ), d_α is the canonical dimension (4 for e and 𝒯, 5 for
  τ_ν and 𝔴), and 𝔤_α is at most a fixed power of log(2 + ℓ_ref/δ). tree_ℓ is the spanning-tree length with all edges
  shorter than ℓ_ref set to zero.
- (N4) Mechanism: a BFT-4-type polymer norm, Σ_{X∋□}sup_{polydisc}|𝔞(X)|e^{κ_s d(X)}.

### 3.3 (SRC): the source-inserted RG down to the reference scale, conditional on U_K
**SRC-κ (the consumed form).** There are m_c > 0, C_0 < ∞, p ≥ 0 and a radius r_0 > 0, all depending only on
(N, L, κ_±, g_ref), such that the following holds for every a, every torus R and every U_K ∈ 𝒮_K:
- (κ-1) **e-cumulants, all orders.** For n ≥ 2 and fine sites x_1, …, x_n with mutual distances ≥ 4a:
  |κ_n(e_a(x_1), …, e_a(x_n) | U_K)| ≤ C_0^n(n!)^p·W(x_1, …, x_n).
- (κ-2) **One insertion.** For O_α ∈ {τ, 𝒯, 𝔴}, 0 ≤ n ≤ 2 further e-insertions, and all points mutually at distance ≥ 4a:
  |κ_{n+1}(O_α(x), e_a(x_1), …, e_a(x_n) | U_K)| ≤ C_0·w_α(δ_0)Π_iw_e(δ_i)·e^{−m_c tree_ℓ/ℓ_ref}.
- (κ-3) **Coarse images.** For each O ∈ 𝒪_rot, x ↦ E_K[O(x)] − ω(O(x)) is a function of U_K with
  |E_K[O(x)] − ω(O(x))| ≤ C_0 on 𝒮_K. It is **quasi-local**: changing U_K only on cubes at distance ≥ ρ from x changes it
  by ≤ C_0e^{−m_cρ}.

**SRC-κ-LF (large coarse fields).** For U_K ∉ 𝒮_K, (κ-1)–(κ-3) hold with every factor e^{−m_c·(length)} replaced by the
path sum
  𝒫(A, B; U_K) := Σ_{γ: A→B} Π_{Q∈γ} ϖ(Q),   ϖ(Q) := e^{C_LF} if Q ∈ 𝔏(U_K), e^{−m_cM} otherwise,
with γ ranging over *-connected M-cube paths (for trees, over spanning trees of such paths). The sup bounds in (κ-3) are
multiplied by e^{C_LF|𝔏(U_K) ∩ 𝒩(x)|}, with 𝒩(x) the M-neighbourhood of x.

**SRC-M (matching; the finitely many constants).** There are real constants, functions of (a, N, L, κ_±) only:
- observable side: ϑ_1, ϑ_3, ϑ_{6′} (ROTDEF §4.2);
- insertion side: c_1, c_3, c_{6′} (Codex F3);
- the normalisations of 𝒯's two traceless H(4) components: Z_3 = 1 + z_3, Z_{6′} = 1 + z_{6′}.

These satisfy **|ϑ_R| + |c_R| + |z_R| ≤ C g_bare²**, and the following hold in every conditional cumulant of SRC-κ
(arguments mutually at distance ≥ δ_c, a fixed multiple of a):
- (M-a) t_ν = ϑ_1∇̄_νe_a + ϑ_3∇̄_νS^{(3)}_{νν} + ϑ_{6′}∇̄_μS^{(6′)}_{μν} + ρ^t_ν and A_J = ρ^A_J. The remainders' cumulants obey
  SRC-κ's bounds multiplied by a²𝔏(a). Here S^{(3)}, S^{(6′)} are fixed lattice clover representatives of the
  diagonal-traceless and off-diagonal dimension-4 tensors, and 𝔏(a) := log^q(ℓ_ref/a).
- (M-b) **Contact.** For y in supp g, the 𝔅-density within δ_c of y has, against e_a(y), the contact
  Σ_Rc_R·(structure of Codex F3) + a remainder with SRC-κ bounds times a²𝔏(a).
- (M-c) **Bulk.** With 𝒯 the identity's own current (normalisations Z_R), every other part of the 𝔅-density has
  cumulants and coarse images bounded by a²𝔏(a)·(|v| + ℓ_ref|∂v|) times SRC-κ's bounds. Per level-K M-cube Q:
  ‖E_K[𝔅_Q] − ω(𝔅_Q)‖_{L²(ν_K)} ≤ C a²𝔏(a)·sup_Q(|v| + |∂v|).

**SRC-I (coarse local integrability; level K).** There is ε_LF > 0 with 80(e^{C_LF}ε_LF + e^{−m_cM}) < 1, such that for
every finite set A of level-K M-cubes:
  **P_ν(A ⊂ 𝔏(U_K)) ≤ ε_LF^{|A|}**, uniformly in a, R.

**SRC-poly (the mechanism; implies SRC-κ by Proposition A).** This is EXISTENCE's H-Bal-loc (l.1110) made conditional on
U_K. For every U_K ∈ 𝒮_K and every complex η with ‖η‖_∞ ≤ r_0:
  **log E_K[exp(Σ_xa⁴η(x)e_a(x))](U_K) = CT[η] + Σ_{r=0}^{K}Σ_{X∈𝒫_r}𝔞_r(X; η, U_K),**
where:
- CT[η] is a U_K-independent local functional of η with range ≤ c_1a. It holds the vacuum energy as a local function of
  η and the η-η contact terms.
- 𝒫_r is the set of connected unions of level-r M-cubes (side Mℓ_r).
- 𝔞_r(X; ·, U_K) is analytic, vanishes when η|_X = 0, depends only on η|_X and on U_K within Mℓ_ref of X, and satisfies
  |𝔞_r(X; η, U_K)| ≤ A_r e^{−κ_s d_r(X)} with κ_s > κ_0 (Theorem CE's entropy constant, in M-cube units).

The same holds with one linear insertion of O_α (the η-derivatives of the conditional one-point function of O_α in the
η-perturbed conditional state). **There is no unit-scale remainder: U_K is not integrated.** This is the difference from
H-Bal-loc's R_K[η], which was the only IR object there.

### 3.4 (CD) precisely
**CD-eff (pointwise in U_K; effective distance).** For F̃_s = Ō_a(f_s)Ō_a(g_s) (ROTDEF E4), every fine x with
dist(x, supp F) ≥ ℓ_ref, and every U_K:
  |Cov(F̃_s, 𝒯_{μν}(x) | U_K)| ≤ C_F·[1 + |E_KŌ_a(f_s)| + |E_KŌ_a(g_s)|]·𝒫(supp F, x; U_K),
and the same for the 𝔅-density in place of 𝒯. This is a corollary of SRC-κ and SRC-κ-LF, by the cumulant expansion of
the product in §4, Proposition D (i).

**CD-avg (ROTDEF I4, l.349; the form Theorem 7.1 uses).** For the same F̃_s and x:
  |Cov(F̃_s, 𝒯_{μν}(x)|U_K)| ≤ C_G(U_K)e^{−m′dist/ℓ_ref}, with ν_K(C_G) ≤ C uniformly in a, R and s.
This follows from CD-eff + SRC-I + SRC-E′(i) (Proposition C).

**What "uniformly in the coarse field" can mean.** Sup over **all** U_K with the plain distance (no 𝔏-discount) is
**not** claimed, and the lane cannot supply it. On a large-field coarse cube BFT gives no background (BFT is stated for
max|log V| ≤ ε_0). The conditional measure there may be multimodal across a bounded number of top levels. Correlations can
then cross a large-field cluster without decay, at bounded cost per cube. This is not a refutation, because no example is
constructed. It is why CD-eff discounts 𝔏(U_K), and why the averaged form is the right target.

### 3.5 Corrected forms of ROTDEF's I5 clauses
- **SRC-E′ (replaces SRC-E).**
  - (i) ν_K(|E_KŌ_a(f)|²) + ν_K(|E_KF̃_s − ω(F̃_s)|²) + ν_K(|E_K𝒯(x) − ω(𝒯(x))|²) ≤ C for f, g in a bounded subset of
    C_c^∞(B_{ρ_F}) with dist(supp f, supp g) ≥ d.
  - (ii) The separated conditional cumulants ν_K(|κ_2(O_a(f), O_a(g)|U_K)|) ≤ C. No conditional variance at coincident
    supports appears.
  - Under SRC-κ(+LF) and SRC-I, (i)-(ii) hold with Z_e ≡ 1 (Proposition D (ii)). Non-vacuity remains a separate input
    (P1's H_int).
- **SRC-O.** Unchanged in statement (|𝒞(s)| ≤ C[g_bare² + a²𝔏(a)]). It is now a consequence of SRC-κ + SRC-M(M-a) +
  SRC-E′ (Proposition D (iii)).
- **SRC-W′ (replaces SRC-W).** |Cov_ω(F̃_s, 𝔅(v_r))| ≤ C[g_bare² + a²𝔏(a)(r/ℓ_ref)⁵], where the g_bare² term is Codex
  F3's contact. It is a consequence of SRC-κ + SRC-M(M-b, M-c) + SRC-E′ (Proposition D (iv)).

---

## 4. Implications proven here (each PROVEN-HERE as an implication; the inputs are OPEN unless stated)

### Proposition A (SRC-poly ⇒ the decay part of SRC-κ, hence CD for e-observables and linear insertions)
**Statement.** Assume SRC-poly. Let h_1, …, h_n (n ≥ 2) satisfy |h_i| ≤ 1, with supports X_i at mutual distances
≥ δ > 2c_1a. Then for every U_K ∈ 𝒮_K:
  |κ_n(e(h_1), …, e(h_n) | U_K)| ≤ r_0^{−n}K_0^{CE}Σ_{r=0}^{K}A_r N_r(X_1)e^{−(κ_s−κ_0)(τ_r(X_1,…,X_n) − c)},
with e(h) := Σ_xa⁴h(x)e_a(x), N_r(X_1) the number of level-r M-cubes meeting X_1, and τ_r := tree(X_1, …, X_n)/(Mℓ_r).
The same bound, with r_0^{−n} replaced by r_0^{−(n−1)} and A_r by the insertion activities, holds for
κ_n(O_α(x), e(h_2), …, e(h_n) | U_K).
In particular the level-K term gives **CD at rate m_c = (κ_s − κ_0)/M per ℓ_ref**, and every level r < K decays faster at
distances ≫ ℓ_r.
**Proof.**
- (1) With η := Σ_iz_ih_i and |z_i| ≤ r_0, the supports are disjoint, so ‖η‖_∞ ≤ r_0. The analytic logarithm exists by
  SRC-poly, so E_K[exp Σz_ie(h_i)] ≠ 0 on the polydisc, and κ_n = ∂_{z_1}⋯∂_{z_n}log E_K[…]|_{z=0}.
- (2) CT[η] has range ≤ c_1a < δ/2, so each of its local terms involves at most one z_i: mixed derivative 0. This is
  EXISTENCE Lemma X-SRC-CT (i), re-derived. Likewise a polymer X missing some X_i depends only on η|_X, which does not
  contain that z_i: mixed derivative 0.
- (3) Cauchy for the (1, …, 1) mixed derivative on the polydisc: |∂_{z_1}⋯∂_{z_n}𝔞(0)| ≤ r_0^{−n}sup|𝔞|.
- (4) A connected X meeting every X_i has d_r(X) ≥ τ_r − c, where c absorbs the cube diameters.
- (5) Σ_{X∋□}e^{−κ_0d_r(X)} ≤ K_0^{CE}: Theorem CE's (g4) with Lemma CE-geo′ (LINEAR_PACKAGE §5).
- Sum over the cubes □ meeting X_1. ∎ This is the proof of EXISTENCE Lemma X-SRC-RED (l.1121) with the tree length kept
  instead of discarded, and with U_K held fixed, so there is no unit-scale remainder.

### Proposition B (telescoping conditional covariance; the RG's conditional structure, exactly)
**Statement.** Let W_ch(U_0, …, U_K) = e^{−S(U_0)}Π_{i<K}K_i(U_{i+1}, U_i) with every K_i ≥ 0 and ∫K_i dU_{i+1} = 1. Let
G, H be bounded functions of U_0, and put G_i := E[G|U_i] (so G_0 = G and G_K = E_KG). Then, for ν_K-a.e. U_K,
  **(B1) Cov(G, H | U_K) = Σ_{i=0}^{K−1} E[ Cov(G_i, H_i | U_{i+1}) | U_K ],**
and the law of U_i given U_{i+1} is **(B2) P(dU_i|U_{i+1}) ∝ e^{−S_i(U_i)}K_i(U_{i+1}, U_i)dU_i**, where e^{−S_i} is the
marginal density of U_i, i.e. the level-i effective density of the exact RG step e^{−S_{i+1}(V)} = ∫K_i(V, U)e^{−S_i(U)}dU.
**Proof.**
- *(Markov.)* The joint density is a product of a function of (U_0, …, U_i) and a function of (U_i, …, U_K). Hence
  (U_0, …, U_{i−1}) ⊥ (U_{i+1}, …, U_K) given U_i.
  - So E[G | U_i, …, U_K] = E[G | U_i] = G_i.
  - So the law of U_i given (U_{i+1}, …, U_K) depends on U_{i+1} only. Integrating out U_0, …, U_{i−1} gives (B2).
- *(Martingale differences.)* Let 𝔊_i := σ(U_i, …, U_K), a decreasing filtration, with G_i 𝔊_i-measurable and
  E[G_i|𝔊_{i+1}] = G_{i+1}.
  - Write G − G_K = Σ_{i<K}D^G_i with D^G_i := G_i − G_{i+1}, and E[D^G_i|𝔊_{i+1}] = 0.
  - For i < j, D^H_j is 𝔊_{i+1}-measurable, so E[D^G_iD^H_j|𝔊_K] = 0.
  - The diagonal terms give E[D^G_iD^H_i|𝔊_{i+1}] = Cov(G_i, H_i|𝔊_{i+1}) = Cov(G_i, H_i|U_{i+1}), by Markov.
  - Finally Cov(G, H|U_K) = E[(G − G_K)(H − H_K)|𝔊_K]. ∎
**Exact check.** `checks/sc55_tel` (criteria first): (B1) holds exactly in 25 random rational chains (50/50 equalities);
the Markov property holds; both controls fired (non-Markov chains break the Markov form; dropping the i = 0 term breaks it);
and the general tail-σ-algebra form holds in the non-Markov chains.

**Corollary B′ (CD from one-step bounds).** Suppose that for every level i, every U_{i+1} in the level-(i+1) small-field
set, and G, H with supports at distance D:
  |Cov(G_i, H_i | U_{i+1})| ≤ c_i(U_{i+1})·e^{−m_1D/ℓ_{i+1}},   with   E[c_i | U_K] ≤ C(ℓ_ref/ℓ_i)^p on 𝒮_K.
Then for D ≥ ℓ_ref, |Cov(G, H | U_K)| ≤ C′e^{−m_1D/ℓ_ref}, uniformly in K.
*Proof.* By (B1) the sum is ≤ Ce^{−m_1D/ℓ_ref}Σ_{j≥0}L^{(j+1)p}e^{−m_1(L^j−1)D/ℓ_ref}, with j := K − 1 − i. The series
converges uniformly in K for D ≥ ℓ_ref. ∎
*Reading.*
- Conditional decay at the reference scale is **assembled from per-step fluctuation decay** at every scale. Each per-step
  law (B2) is exactly the integrand the RG must analyse at step i.
- The per-step decay rate m_1 (in level-(i+1) units) is the soft-constraint mass. Its linear version is N5's per-step
  covariance (PROOF "Theorem RW", "Corollary RW-triv": rate m_cov, every level, trivial background; "Theorem N5-sf0": level
  0, curvature-small backgrounds).
- The images G_i must be quasi-local around supp G at scale ℓ_i: SRC to first order, Proposition F.
- (B1) never integrates over ν_K, so **no coarse-law information enters CD.**

### Proposition C (CD-eff + SRC-I + SRC-E′(i) ⇒ CD-avg, ROTDEF's I4)
**Statement.** Assume, for all U_K,
  |Cov(F̃, 𝒯(x)|U_K)| ≤ C_F[1 + |E_KŌ(f)| + |E_KŌ(g)|]·𝒫(supp F, x; U_K).
Assume also SRC-I with q := 80(e^{C_LF}ε_LF + e^{−m_cM}) < 1, and SRC-E′(i) for E_KŌ(f), E_KŌ(g). Then
  ν_K(|Cov(F̃, 𝒯(x)|U_K)|) ≤ C′_F N_∂(F)·q^{D_M/2}/(1 − q),   D_M := dist(supp F, x)/(Mℓ_ref) − 1,
with C′_F depending only on C_F and the SRC-E′ constant.
**Proof.**
- *(Path sum.)* For a fixed path γ, Π_{Q∈γ}ϖ(Q) ≤ Σ_{A⊂γ}e^{C_LF|A|}1_{A⊂𝔏}e^{−m_cM|γ\A|}: the left side is the
  A = γ∩𝔏 term and all terms are ≥ 0. Taking ν_K-expectations with SRC-I gives
  ν_K(Π_{Q∈γ}ϖ) ≤ (e^{C_LF}ε_LF + e^{−m_cM})^{|γ|}.
- There are ≤ N_∂(F)·80^ℓ *-connected paths of length ℓ starting at the N_∂(F) cubes meeting supp F (80 = 3⁴ − 1). The
  length is ≥ D_M. So ν_K(𝒫) ≤ N_∂(F)Σ_{ℓ≥D_M}q^ℓ.
- *(Prefactor.)* Cauchy–Schwarz: ν_K(|E_KŌ(f)|𝒫) ≤ ‖E_KŌ(f)‖_{L²(ν)}ν_K(𝒫²)^{1/2}.
- ν_K(𝒫²) is a double path sum. Expand the product over both paths and use SRC-I on the union of their large-field cubes:
  each cube in γ ∩ γ′ is counted once, with weight ≤ e^{2C_LF} or e^{−2m_cM}. This gives ν_K(𝒫²) ≤ N_∂(F)²(Σ_{ℓ≥D_M}q_2^ℓ)²
  with q_2 := 80(e^{2C_LF}ε_LF + e^{−m_cM}).
- **Correction to the displayed rate:** with q_2 in place of q (and assuming q_2 < 1) the bound reads
  ≤ C′_F N_∂(F)·max(q, q_2)^{D_M}/(1 − q_2). The exponent "D_M/2" displayed above is a conservative misprint and is
  withdrawn. ∎
- *Use.* Insert into Theorem 7.1 step 5: the shell sum Σ_{x∈Sh}a⁴|c(x)| ≤ Cr⁴ times the above gives
  Cr⁴e^{−m′(r−ρ_F−1)/ℓ_ref}, with m′ := −log max(q, q_2)/M. This is ROTDEF's term with m_c → m′.

### Proposition D (the corrected ROTDEF inputs follow from SRC-κ(+LF), SRC-M, SRC-I)
Each item is an implication. The inputs are OPEN.
- **(i) CD-eff.** Expand the conditional covariance of the product (all cumulants conditional on U_K):
  Cov(F̃, 𝒯(x)|U_K) = κ_3(O(f), O(g), 𝒯(x)) + E_KŌ(f)·κ_2(O(g), 𝒯(x)) + E_KŌ(g)·κ_2(O(f), 𝒯(x)).
  - This is the identity Cov(XY, Z) = κ_3(X, Y, Z) + E[X]κ_2(Y, Z) + E[Y]κ_2(X, Z).
  - The three supports are mutually separated: by d between f and g, and by ≥ ℓ_ref from x. So SRC-κ (κ-2) applies with
    the smeared e's, and SRC-κ-LF gives the path sum 𝒫. **No coincident-support conditional variance appears.** This is
    exactly what SRC-E's divergent clause was standing in for.
- **(ii) SRC-E′ and U4.** dω(F̃_s)/ds = ω_c(O(Jf_s), O(g_s)) + ω_c(O(f_s), O(Jg_s)).
  - By total covariance each term is ν_K(κ_2(·,·|U_K)) + Cov_ν(E_KŌ(·), E_KŌ(·)).
  - The first part is bounded by SRC-κ (κ-1) at separation d; the second by SRC-E′(i).
  - SRC-E′(i) itself: E_KŌ(f) = Σ_xa⁴f(x)[E_Ke_a(x) − ω(e_a(x))], bounded by SRC-κ (κ-3) with the LF factor, which is
    ν_K-integrable by SRC-I.
  - Hence ϑ_1's absorption ("ϑ₁ multiplies d/ds ω(F_s) itself", ROTDEF l.394) needs only SRC-E′.
- **(iii) SRC-O.** 𝒞(s) = ω(Ξ_{v_r}F̃_s) − dω(F̃_s)/ds (Codex F1's centred definition)
  = Σ_xa⁴f_s(x)ω_c([(Jx)^νt_ν(x) + A_J(x)]·Ō(g_s)) + (f↔g) + O(a²)·(separated two-point functions).
  - Insert (M-a). Each structure ω_c(∇̄X^{(R)}(x)Ō(g)) is bounded by SRC-κ (κ-2) plus SRC-E′(i).
  - Each remainder carries a²𝔏(a).
  - Hence |𝒞(s)| ≤ C[Σ_R|ϑ_R| + a²𝔏(a)] ≤ C[g_bare² + a²𝔏(a)].
- **(iv) SRC-W′.** Split 𝔅(v_r) into near (within δ_c of supp F), bulk (rest of {ψ_r ≡ 1}) and shell ({ψ_r ≠ 1}).
  - *Near:* (M-b) gives ≤ C[Σ_R|c_R| + a²𝔏(a)].
  - *Bulk, conditional part:* Σ_xa⁴|v(x)||κ(…, 𝔅-density(x)|U_K)| ≤ Ca²𝔏(a), since the factor e^{−m_c dist} absorbs
    |v| ≤ 2r.
  - *Bulk, coarse part:* |Cov_ν(E_KF̃, E_K𝔅_bulk)| ≤ ‖E_KF̃ − ω(F̃)‖_{L²(ν)}Σ_{Q⊂B_{2r}}‖E_K𝔅_Q − ω(𝔅_Q)‖_{L²(ν)}
    ≤ C·Cr⁴·a²𝔏(a)·r, by SRC-E′(i) and (M-c). **No decay of ν_K is used: the triangle inequality over r⁴ cubes is enough.**
  - *Shell:* the supplement's k ≥ 2 terms (ROTDEF l.566-580) have ∂^kv = O(r^{1−k}) and are covered by (M-c) in the same
    way, giving ≤ Ca²𝔏(a)r³.
  - Total ≤ C[g_bare² + a²𝔏(a)r⁵].
- **(v) Theorem 7.1 with the corrected inputs.** Steps 1-4 of ROTDEF's proof are exact identities (Codex F5 CONFIRMED them).
  Step 5 uses (i) + Proposition C. Step 6 uses (iii) and (iv). The conclusion is unchanged, with the same
  ε_UV = C_F[g_bare² + (a/ℓ)²𝔏(a)(r/ℓ)⁵ + (r/ℓ)⁴e^{−m′(r−ρ_F−1)/ℓ}]. ∎

### Proposition E (OS0 for the field e from SRC-κ(+LF) and SRC-I; no coarse decay)
**Statement.** Assume SRC-κ (κ-1) at all orders with C_0^n(n!)^p, SRC-κ-LF, and SRC-I. Put ê(x) := e_a(x) − ω(e_a(x)).
- (a) For n ≥ 2 and fine sites with mutual distances ≥ 4a:
  |κ_ω(ê(x_1), …, ê(x_n))| ≤ C_1^n(n!)^{p+1}Π_iw_e(δ_i), uniformly in a and R.
- (b) Hence for F ∈ ^0𝒮(R^{4n}) the lattice Schwinger functions S^a_n(F) := Σa^{4n}F(x)ω(Πê(x_i)) obey
  |S^a_n(F)| ≤ C_2^n(n!)^{p+2}‖F‖_{𝒮,4n+5}.
- (c) Along a subsequence (a_j, R_j) they converge for all n and all F in a countable dense set, and then for all F, with
  the same bounds.
**Proof.**
- (a) Brillinger's law of total cumulance [m, standard combinatorial identity]:
  κ_ω(X_1, …, X_n) = Σ_πκ_ν((κ(X_B|U_K))_{B∈π}).
  - Each Φ_B := κ(X_B|U_K) obeys SRC-κ with δ_i^B ≥ δ_i, since nearest-neighbour distances only grow in a sub-family,
    times an LF factor that is L^m(ν_K)-integrable by SRC-I.
  - Coarse cumulants satisfy |κ_ν(Φ_1, …, Φ_b)| ≤ C^bb!Π‖Φ_j‖_{L^b(ν)} (cumulants are signed sums of moments; Hölder).
  - The number of partitions is ≤ n!.
  - Everything is local, so the bound is R-uniform. Only **boundedness** of coarse cumulants is used, never their decay.
- (b) Moments are sums over partitions of products of cumulants, each bounded as in (a).
  - F vanishes with all derivatives on the diagonals. Taylor's theorem gives |F(x)| ≤ C‖F‖_{C^{4n+1}}δ_min^{4n+1}, which
    beats Πw_e(δ_i) ≤ δ_min^{−4n}𝔤^n. Schwartz decay of F handles infinity.
  - Configurations with some distance < 4a contribute ≤ a^{4n}·#·a^{4n+1}·‖e_a‖_∞^n, with ‖e_a‖_∞ ≤ Ca⁻⁴, so they are
    O(a).
- (c) Diagonal argument and continuity, as in EXISTENCE X-MOM (ii). ∎
**Status of the last step.** Matching (b)'s growth and Schwartz order to OS II's linear growth condition E0′ is ARGUED
[m: OS II as recalled; P1 §7 checked only its introduction]. Reflection positivity for e is separate. e_a is strictly local,
so positive-time smearings are positive-time lattice observables (ROTDEF §2.2 item 1).

### Proposition F (coarse images are quasi-local under SRC-poly; repairs Codex F5's NOT-VERIFIED item conditionally)
**Statement.** Under SRC-poly with one linear insertion, E_K[O_α(x)] − c_α = Σ_rΣ_{X∋x}𝔟_r(X; x, U_K). Each term depends
on U_K only within Mℓ_ref of X and obeys |𝔟_r| ≤ A_re^{−κ_sd_r(X)}. Hence changing U_K only on cubes at distance ≥ ρ from x
changes E_K[O_α(x)] by ≤ 2Σ_rA_rK_0^{CE}e^{−(κ_s−κ_0)(ρ/(Mℓ_r) − 1)}, which is ≤ Ce^{−m_cρ} for ρ ≥ ℓ_ref.
**Proof.** Only polymers reaching the changed cubes change. Count them with Theorem CE's (g4). ∎
*Remark.* Codex's two-site example (CODEX_REVIEW_ROTDEF F5, "E[X|V=1,W=1] = 2/3, E[X|V=1,W=−1] = 2/7") shows strict
locality is false in general. Quasi-locality is the correct replacement, and it is what DEC/TQ in ROTDEF §8 implicitly
presuppose ("an explicit sum of local coarse functionals").

---

## 5. Relation to the lane's machinery

### 5.0 The exact source recursion (PROVEN-HERE; this is "the RG is linear in the sources", made precise)
Put Φ_k(η) := log E[exp(Σ_xa⁴η(x)e_a(x)) | U_k], a function of U_k.
- By the tower property and the Markov property (Proposition B), **Φ_{k+1}(η) = log E[e^{Φ_k(η)} | U_{k+1}]** exactly, and
  Φ_0(η) = Σ_xa⁴η(x)e_a(x) is linear in η.
- Equivalently, **Φ_K(η) = −[S_K(U_K; η) − S_K(U_K; 0)]**, where S_K(·; η) := −log∫e^{−S(U_0)+⟨η,e⟩}Π_{i<K}K_i dU_0⋯dU_{K−1}
  is the level-K effective action of the source-perturbed chain. Both sides are the log of the same ratio of integrals at
  fixed U_K. **So SRC-poly is literally a locality statement about the source-dependence of the effective action**, and the
  conditional reading is automatic.
- Expanding at η = 0 (with Φ_k(0) = 0):
  - *First order:* Φ′_{k+1} = E[Φ′_k | U_{k+1}]. The first-order source term evolves by the one-step conditional mean, a
    **linear** map (the linearisation of the RG step at the source-free trajectory). Φ′_k[h] = E[e(h) | U_k] is the
    level-k image.
  - *Second order:* Φ″_{k+1} = E[Φ″_k | U_{k+1}] + Var(Φ′_k | U_{k+1}). This is linear in the second-order term plus a
    quadratic inhomogeneity: the one-step conditional covariance of the first-order terms, i.e. contact generation.
    Iterating from Φ″_0 = 0 gives exactly (B1). **Proposition B is the solved second-order source recursion.**
  - *Order n:* linear in Φ^{(n)}_k plus a polynomial in lower orders (the one-step conditional cumulants). This is a
    triangular system.
  - If Φ_k is analytic on a fixed polydisc uniformly in k, all orders follow from Cauchy estimates.
- **Pre-stated refutation R-e does not occur.** The second-order coefficients are governed by a linear recursion whose
  inhomogeneity is controlled by the first order.

### 5.1 BFT-3 and BFT-4 (REVIEW_S22.md "Statement (BFT)", l.387; read on disk)
- **BFT-3** ("|∂^nU_j(x)/∂V_k(y_1)⋯∂V_k(y_n)| ≤ C_0e^{−m_0 tree(x, y_1, …, y_n)}", n ≤ 4) bounds the **deterministic**
  background's dependence on the coarse field. In SRC it is the tree-level (classical) part of Proposition F's
  quasi-locality: at tree level E_K[O(x)] ≈ O(Z(U_K))(x), and its U_K-dependence decays at rate m_0 by BFT-3 with n = 1.
  **BFT-3 is not a covariance bound.** Cov(·,·|U_K) is a property of the fluctuation measure around the background, and its
  decay comes from BFT-5's Hessian through N5's inverse, not from BFT-3. P1 §4's "What the requested BFT actually targets"
  says the same ("Its exponential derivative locality concerns the conditional background construction"). **I agree.**
- **BFT-4** (E_k^br = S_W + R_k, ‖R_k‖_𝒜 := Σ_{X∋0}sup|R_k(X)|e^{m_0|X|} ≤ C_0) is the source-free **classical** part of
  SRC-poly's activities. By §5.0, SRC-poly needs:
  - (a) the η-dependent version: a complex, position-dependent Wilson coefficient u_0 − ηh, i.e. BFT^η;
  - (b) the fluctuation-determinant and interaction polymers (N6) and the large-field polymers (RLF), which BFT-4 does not
    contain (BFT is a statement about the branch action at small fields);
  - (c) the conditional reading, which is automatic (§5.0).
- BFT's own data are "(N, L, κ_±)" and its fields are small-field V_k. Hence SRC's uniformity "in the coarse field" from
  BFT covers 𝒮_K only, and §3.4's CD-eff/CD-avg split is forced.

### 5.2 N5 / Theorem RW / N6 / Theorem CE: the one-step decay of Corollary B′
- The one-step law (B2) is the integrand of RG step i at fixed U_{i+1}. Its Gaussian part is the gauge-fixed per-step
  covariance C_i = Õ_i^{−1}.
  - **Theorem RW** (PROOF l.5558) gives the random-walk expansion with entrywise decay in coarse distance (walk bounds
    (ii)): **PROVEN-HERE [S19]** at the trivial background for every level (Corollary RW-triv), and for the level-0
    operator at curvature-small backgrounds (Theorem N5-sf0, an existence theorem with crude constants: λ_min ≥ 6.6·10⁻¹⁰
    after Proposition RW-ℓ²).
  - Levels i ≥ 1 at general small backgrounds are **OPEN, narrowed** ("N5 node status [S20]-[S23]": level 1 for the
    critical branch; level ≥ 2 by Proposition NAH-ind, an implication).
  - These statuses are inherited and were **not** re-verified here. They are cited only to locate what is banked.
- For gauge-invariant images G_i, H_i, the leading term of Cov(G_i, H_i|U_{i+1}) is ⟨∇G_i, C_i∇H_i⟩ (Gaussian), so
  Corollary B′'s rate m_1 is N5's m_cov (in level-(i+1) units) at linear order.
- The **nonlinear** one-step decay needs:
  - **N6** ("L4a-form-soft polymer bound … OPEN for the soft kernel", PROOF l.2440);
  - **Theorem CE** (LINEAR_PACKAGE Theorem 5.1, re-proved Dimock, PROVEN with explicit constants; κ > 3κ_0 + 3 ≈ 457 in
    M-units, the reason for large blocks M);
  - the per-step large-field analysis held at fixed U_{i+1}.
- Which rate is which: m_0 (BFT-3, background), m_*′ (LINEAR_PACKAGE Theorem 4.2′, tree-level response maps; 0.0384 proven
  vs ≈ 1 located at κ = 1), m_cov (N5, per-step covariance), m_c (CD). ROTDEF needs only m_c > 0; any positive rate kills
  r⁴e^{−m_c r}. **No two-sided window arises here** (PLAN_S26 §12's rule): CD's constraints are one-sided (m_cM large;
  ε_LF small, i.e. g_ref small).

### 5.3 LINEAR_PACKAGE §6.2 (LP-SRC, critical-point sources) and the e-source
- In the abelian linearisation e ≈ ½|dB_0|², so the first variation of the e-source term at a background is
  δ⟨η, ½|dB_0|²⟩ = ⟨d_0^*(η dB_0), δB_0⟩. This is a **divergence-form critical-point source** j_0 = d_0^*G_0 with
  G_0 = η·dB_0 (that is, η f_0 in coarse units).
- So the background's first-order response to an e-source is exactly the LP-SRC problem of **Theorem 6.8 (G♯_0-soft)**:
  ‖r_{k−1}‖_{∞,m} ≤ C_topΣ_l‖G_l‖_{∞,m} + C_D‖B_k‖_{D,m}, uniformly in k and T. That is PROVEN in the package (not
  re-verified here), with ‖G_0‖_{∞,m} ≤ ‖η‖_∞‖f_0‖_{∞,m}.
- At curved non-abelian backgrounds the same role is played by BFT-5's (G♯) in the 𝔐-pair, whose norm already contains
  "nonlinear sources in a divergence-form norm Y" (REVIEW_S22 l.396-397). This is OPEN; see GV55/BGT55 (running, not read
  beyond their pre-statements).
- **This is a concrete bridge:** the observable-source RG reuses the lane's critical-point source estimates for the
  background, with G = 2ηF(Z) (non-abelian: the derivative of η·s(U_p)).
- The e-source also rescales the per-step Hessians by a relative O(r_0g_k²) ≤ O(r_0g_ref²). Theorem RW's hypotheses
  (RW1)-(RW2) are open conditions, so they survive for r_0 ≪ 1/g_ref². This is an ARGUED perturbation remark, not
  re-derived in RW's constants.

### 5.4 What source insertions add to BFT's induction (the honest list)
1. **Marginal sources = variable coefficients.** An e-source is a complex, position-dependent shift of the Wilson
   coefficient. By asymptotic freedom it persists as an O(1) shift of 1/g_k²(x) at every level (one-loop RG invariance of
   δ(1/g²)), so it does **not** become small. BFT, N5, N6, RLF and (F_R) must hold **uniformly over a sup-norm ball of
   coupling fields** with ‖η‖_∞ ≤ r_0 ≪ 1/g_ref². Sources for 𝒯's traceless components are anisotropic deformations
   (plane-dependent couplings for the diagonal 3; non-plaquette loops for the off-diagonal 6′).
   - This is the same technology as PANEL_P4's S⁴ route S4(a): "A slowly varying bare coupling. This is the same
     technology X-SRC-GAP needs for OS0" (PANEL_P4 l.314). **I agree with P4 on this sharing.**
   - It is also what (F_R)'s quantifier must accommodate: a position-dependent coupling flow.
2. **Linearity / triangularity** (§5.0): the first order is exactly linear (one-step conditional mean); higher orders are
   triangular.
3. **Localisation of irrelevant insertions.** t_ν, A_J and the bulk Ward density are classically O(a²). They generate
   O(g_0²) marginal components at the first steps (a² × a⁻² × g_0²), and the rest contracts. The lane must extract the
   finitely many H(4)-allowed marginal constants (SRC-M's ϑ_R, c_R, Z_R) with a localisation operator on the
   source-linearised RG, and contract the remainder. **BFT-4's single bound ‖R_k‖_𝒜 ≤ C_0 does not do this**, and BFT-4's
   optional strengthening "‖R_{k+1} − R_k‖_𝒜 ≤ C_0λ^k" is the source-free analogue of the contraction needed.
4. **Field-independent counterterms.** These are the vacuum energy as a local function of η (∝ a⁻⁴) and the η-η contacts
   (a⁻⁴η², a⁻²(∂η)², log(a)(∂²η)²). They are U_K-independent and local, and they cancel in separated cumulants (EXISTENCE
   Lemma X-SRC-CT (i); Proposition A step 2).
5. **No new symmetry input.** e_a, 𝔚, τ and 𝒯 are gauge invariant or covariant, and the kernels are gauge covariant
   (PROOF "Decision 4": "K(g|_roots·V, g·U) = K(V, U)"), so every conditional image is gauge invariant.

### 5.5 Verdict on the brief's question "does (CD) follow from the RG's conditional structure?"
**Yes, structurally; no, from what the lane has banked.**
- *Structurally:* (B1) is an exact identity that decomposes conditional decay into per-step decay of images. §5.0 shows the
  same identity is the solved second-order source recursion. Proposition A shows CD is a corollary of SRC-poly. None of
  this touches ν_K, so the conditional mass is not a physical mass gap (P1 §4's "PROVEN — Conditional locality is not full
  correlation decay", l.99, is consistent with this and not contradicted).
- *From the lane:* PROVEN pieces are the linear per-step covariance at trivial backgrounds and at level 0, Theorem CE,
  Lemma CBE (EXISTENCE), LP-SRC Theorem 6.8 (linear, trivial chain), and the exact identities here. OPEN pieces are BFT,
  N5 beyond level 0, N6, RLF and its conditional and source-inserted forms, (F_R) and its slowly varying form, and SRC-M.
- *The pre-stated refutations:*
  - **R-b** ("CD false for a structural reason") is **not** realised. Gauge zero modes are invisible to gauge-invariant
    observables (Phys/PG). Block-constant constraints give a uniform gap (LINEAR_PACKAGE Theorem 2.1:
    "Δ + aQ_str^†Q_str ≥ min(1/5, a/2)"). The large-coarse-field caveat is handled by CD-eff, not refuted.
  - **R-d** ("CD follows from the lane's bounds") **is realised in its literal form.** The lane's covariance bounds are
    linear and small-field only; the nonlinear per-step bound N6 is OPEN.

---

## 6. What is missing (a first-class result). Dependency order; lane names; status as inherited, not re-verified

To get SRC + CD for ROTDEF (orders ≤ 3: two e's and one insertion) and for OS0 (all orders in e):
- **(M1) SRC-poly at small coarse fields = the source-perturbed RG down to level K.** Needs:
  - **BFT^η**: BFT-0…5 uniformly for the bare actions Σ_p(u_0 − h_η(p))s(U_p) with complex ‖η‖_∞ ≤ r_0. BFT is the OPEN
    layer-1 target. The η-extension is a variable-coefficient perturbation of relative size O(r_0g²). ARGUED that it
    rides on BFT's own contraction ("one contraction for 𝔉_k in 𝔐").
  - **N5^η** (N5 beyond level 0: OPEN, narrowed) and **N6^η** (N6: OPEN for the soft kernel).
  - **Theorem CE**: PROVEN (re-proved Dimock).
  - **RLF^η in per-step form, conditional on the top field.** RLF v3 is OPEN/CONDITIONAL on RLARGE §4.2 rows 10-10f, and
    its (RLF-3′) is stated for the integrated chain (Z(𝔥) := ∫W·1_𝔥), not pointwise in U_K.
  - **(F_R)^η**: the flow with a position-dependent coupling. (F_R) is a hypothesis; FLOW55 is running; PANEL_P4 S4(a)
    needs the same.
- **(M2) SRC-κ-LF at large coarse fields**, i.e. the last j_0 levels at backgrounds of bounded but non-small own-unit
  curvature. This is **the same requirement as UNIV55's (N3)**. UNIV55 §2.4(B) PROVES (soft-kernel lower bound) that large
  coarse fields have probability bounded below uniformly in a, so they cannot be discarded. ROTDEF needs only the
  effective-distance/path-sum output (averaged), while UNIV55's Proposition T needs sup over V.
- **(M3) SRC-I at level K.**
  - On hypercubic tori it follows from EXISTENCE Lemma CBE (chessboard; PROVEN-HERE there, not re-verified here), applied
    with f_Q = 1{Q bad} on Q ∈ A (Theorem CB is its one-cube case), plus (RLF-3^dis), which is OPEN.
  - On S⁴ there is no chessboard (PANEL_P4 H3). Either action-based local large-field bounds are needed, or UNIV55's sup-V
    form, which avoids SRC-I at the price of (M2) in sup form.
- **(M4) SRC-M (matching).** Needs:
  - a localisation operator on the source-linearised RG (§5.0) that extracts the eight H(4)-split marginal constants;
  - their O(g_bare²) size: tree-level vanishing by ROTDEF §3.2 (C) plus one-loop power counting a² × a⁻² × g_0². ARGUED,
    not proved, consistent with Codex F4 ("Classical smooth-field consistency alone does not prove nonperturbative
    O(g_bare²) matching");
  - the O(a²𝔏) contraction of the remainders (the source analogue of BFT-4's optional "‖R_{k+1} − R_k‖_𝒜 ≤ C_0λ^k");
  - the existence of the identity's own current 𝒯 (Codex F5: "also part of SRC-W");
  - the per-block bound (M-c). By ROTDEF Lemma 5.3(ii), E_K[𝔅_Q] = E_K[(Ξ_v log K_0)_Q] exactly in the bulk, i.e. the
    conditional mean of the first kernel's response to a local rotation field. Codex F3's last paragraph names the precise
    obstacle: inside the conditional measure the block structure breaks H(4)_x, and "an equivariant coefficient depending
    on that data can carry the required indices".
- **(M5) OS0 specifics:** (κ-1) at all orders with factorial growth (multiscale), and the OS-II matching of Proposition
  E(b) [m].
- **(M6) Non-vacuity (P1's H_int):** a lower bound on ω_c(O_a(θg)O_a(g)). It is not part of SRC (SRC gives upper bounds
  only). Lemma V does not help here: variance is not a separated correlator.
- **(M7) Removed by this file (no longer needed):**
  - SRC-E (refuted; replaced by SRC-E′, a corollary);
  - strict coarse locality (replaced by Proposition F);
  - pointwise-over-all-U_K CD (replaced by CD-eff + SRC-I);
  - coincident-point counterterms for OS0 (H-src′-diag) [m];
  - local moment bounds for point composites (false, Lemma V).

---

## 7. The rate: is SRC-O's O(g_bare²) consistent with "at best logarithmic in a"?

- **Consistent: CONFIRMED.** (F_R) (RLARGE l.98) gives u_0 − u_K ∈ [β_−K log L − R_F, β_+K log L + R_F], with
  K log L = log(ℓ_ref/a). Hence
  g_bare² = 1/u_0 ∈ [(u_K + β_+log(ℓ_ref/a) + R_F)⁻¹, (u_K + β_−log(ℓ_ref/a) − R_F)⁻¹],
  so g_bare² ≍ 1/log(ℓ_ref/a). The UV error of Theorem 7.1, g_bare² + a²𝔏r⁵ + r⁴e^{−m′r} with r_j ≍ a_j^{−1/3}, is
  therefore ≍ 1/log(ℓ_ref/a), and ROTDEF §9 item 3 ("any quantitative OS1 rate is at best logarithmic in a") is correct
  **for the route as split into SRC-O and SRC-W′**.
- **The logarithm is an artefact of that split, not (on the standard picture) a property of the defect.**
  - *Exact reformulation (PROVEN-HERE, elementary).* ω is exactly lattice-translation invariant, so with C(z) the lattice
    connected correlator of e_a and Φ(w) := ∫f(u + w)g(u)du (smooth, supported in d ≤ |w| ≤ 2ρ_F), Poisson summation
    gives ω_c(Ō_a(f_s)Ō_a(g_s)) = Σ_{z∈aZ⁴}a⁴C(z)Φ(Q_s⁻¹z) + O(a^M).
  - So **the defect of the pair tests only the measure Σ_za⁴C(z)δ_z on the annulus d ≤ |z| ≤ 2ρ_F**, against the rotation
    orbit of one smooth function.
  - If C(z) = C_∞(|z|) + O(a²𝔏) uniformly on that annulus (a Symanzik-type statement [m]), a second Poisson summation
    gives D(s) = O(a²𝔏).
  - In ROTDEF's identity the observable-side ϑ_R (SRC-O) and the insertion-side c_R (Codex F3, SRC-W′) multiply the same
    three structures. The R = 1 combination multiplies D′ itself and is absorbed. Hence in such a theory the anisotropic
    differences of the remaining finite constants must cancel to O(a²𝔏).
- **Sharper input (OPEN): SRC-OW.** The H(4)-anisotropic parts of (ϑ_R − c_R) (with the matching current normalisations
  Z_R) are O(a²𝔏). With SRC-OW, Theorem 7.1's g_bare² term disappears, and the UV error becomes
  C[a²𝔏r⁵ + r⁴e^{−m′r}] ≤ Ca^{1/3}𝔏: a power rate.
  - **Status:** the Symanzik derivation presupposes an O(4)-invariant limit, so it is circular as a proof of OS1.
  - Perturbatively, O(4) invariance of the continuum limit to every order is Reisz's lattice power-counting theorem [m].
    The constants are cutoff-scale functions of g_0, so on that reading SRC-OW holds up to o(g_0^n) for every n. ARGUED
    [m]; not needed by P1, which requires no rate.
- **Independent agreement:** UNIV55 §2.4(E) finds logarithmic rates for its architecture too, and also expects O(a²) from
  Symanzik. On S⁴, UNIV55 §3.4 finds an O(g_0(a)²) dilation insertion. That is a different mechanism (Λ-matching of the
  coupling profile), and it is not removed by SRC-OW.

---

## 8. Alignment with UNIV55 (re-read in full at ≈01:30Z after it grew to 713 lines) and with the S⁴ route

**UNIV55 changed after my PRE-STATED.** It now holds Proposition T (sup-V conditional comparisons ⇒ fixed-volume
universality), §2.2 (the IR entry point is removing the volume factor), Theorem U (L1 + N1–N4 [+ N5 seam] ⇒ UNIV), and
§3.4, a global-Killing-field Ward route for S⁴_R. CODEX_REVIEW_UNIV.md holds only its PRE-STATED. Nothing below
duplicates UNIV55's derivations. These are the alignments:
- **(A1) This file's SRC is shared by three consumers, not two.**
  - UNIV55 §3.4's own correction ("condition on the coarse field V at ℓ_0 … Cov(O, O_6(x)) = E[Cov(O, O_6(x) | V)] +
    Cov(E[O|V], E[O_6(x)|V]) … three estimates, not one") needs exactly:
    - SRC-κ (κ-2): a separated conditional cumulant bound;
    - SRC-M (M-c)/(κ-3): conditional one-point images of the renormalised insertion;
    - SRC-M (M-b): contact near supp O.
  - So the S⁴ Ward route's (W1) **is** this file's SRC, without CD's decay (fixed R) and without SRC-I if sup-V bounds are
    used.
  - ROTDEF's flat route needs SRC + CD-decay + SRC-I. OS0 needs SRC-κ (κ-1) + SRC-I (Proposition E).
- **(A2) Agreement:** UNIV55 §2.4(B) (large coarse fields have probability ≥ c > 0 uniformly in a; BFT does not reach
  them) and UNIV55 E5 (Proposition T's hypotheses are properties of the U_K-pinned fine measures only). These are the same
  facts that force §3.4's CD-eff form here and that make SRC-poly's conditional reading remove H-Bal-loc's remainder R_K.
- **(A3) Disagreement (attribution, not classification):** UNIV55 §3.4's correction attributes conditional-covariance decay
  to "the constraint-induced locality of the conditional fine measure (UV, BFT-3-type)". BFT-3 is deterministic background
  locality. The decay of a conditional covariance is CD. Its inputs are N5/N6 + SRC (Propositions A, B), not BFT-3.
  **"UV" is right; "BFT-3-type" is not.**
- **(A4) Partial disagreement:** UNIV55 §3.4 says "No clustering, no coarse-law covariance, no CD-type input (ROTDEF
  needed CD only for torus-uniformity)". At fixed R, CD's **decay** is indeed not needed. A separated conditional cumulant
  bound (SRC-κ (κ-2)) **is**, as UNIV55's own correction shows: Σ_xa⁴|Cov(O, 𝔚_x|V)| over the sphere needs |Cov| bounded
  at separated points, and Cauchy–Schwarz with point-composite variances (a^{−6}-type, cf. Lemma V) is useless.
- **(A5) ROTDEF §9 item 2 ("SRC-W is (ARGUED) the infinitesimal, interior form of UNIV55's … universality"):
  NOT-VERIFIED in literal form; the precise relation is as follows.**
  - Both are statements about the U_K-pinned fine measure's response to rotation, per coarse block, with no coarse-law
    input.
  - SRC-M (M-c) bounds the conditional mean of the **field-space** rotation response on **one** lattice,
    E_K[(Ξ_v log K_0)_Q] = E_K[𝔚_Q], to O(a²𝔏).
  - UNIV55's (U-cond)/(U-dens) compare the conditional measures of **two** lattices related by a **finite** rational grid
    rotation.
  - Neither implies the other as stated: an infinitesimal grid rotation is not defined on a fixed lattice, and a finite
    comparison does not give the a²-sized derivative. A common lemma would be an (N1)-type two-theory or derivative
    contraction with the Ward density as the source, a special case of SRC-M.
- **(A6) The S⁴ route's S4(a) (slowly varying coupling) is SRC for e** (a source for e_a is a coupling variation;
  §3.2 (N1)). This is shared, as PANEL_P4 l.314 says. **I agree.**

---

## 9. Verdicts on inherited claims touched by this file (REVIEW_BRIEF_55 order: refutations count as much as positives)

| # | Inherited claim (file: locating string) | Verdict | Reason (section here) |
|---|---|---|---|
| H1 | ROTDEF I5 **SRC-E** ("There is a state-independent Z_e(a) > 0 with sup_{a,R}[ν_K(\|E_K G\|²) + ν_K(Var(G\|U_K))]/Z_e^{2·deg G} < ∞") | **REFUTED** as a member of any consistent non-vacuous input set | Lemma V + V-1 (§2.3). Correct statement: SRC-E′ (§3.5), a corollary of SRC-κ + SRC-I (Proposition D(ii)) |
| H2 | ROTDEF §11 row 25, "Normalizing by Var(O_a(f)) would be vacuous (∼a⁻⁴ divergence)" (ARGUED) | **CONFIRMED**, corrected size | Lemma V: ≥ c g_0⁴a⁻⁴, i.e. a⁻⁴/log² under (F_R) |
| H3 | ROTDEF I4 **CD** (averaged prefactor) as the input of Theorem 7.1 step 5 | **CONFIRMED as a sufficient formulation; NOT an independent input** | Proposition D(i) + Proposition C derive it from SRC-κ(+LF) + SRC-I + SRC-E′. Its truth is OPEN (§6) |
| H4 | ROTDEF **SRC-O** (\|𝒞(s)\| ≤ C_F Z_e²[g_bare² + (a/ℓ)²𝔏]) | statement **CONFIRMED** as what step 6 needs; the O(g_bare²) size **NOT-VERIFIED** (ARGUED) | Proposition D(iii); §6 (M4) |
| H5 | ROTDEF **SRC-W** (bulk ≤ C_F Z_e²(a/ℓ)²𝔏 r⁵) | **NOT-VERIFIED** as stated (it misses the contact) | Codex F3 (agreed); SRC-W′ carries g_bare²; Theorem 7.1's conclusion is unchanged (Proposition D(v)) |
| H6 | ROTDEF §6 "I4 and I5 are additional UV statements, absent from the lane, of the kind OS0 needs anyway" | **CONFIRMED**, refined | OS0 needs SRC-κ (κ-1) + SRC-I, not CD-decay or SRC-M (Proposition E). "Absent from the lane": agreed (BALABAN_EXTRACT §6.3: "not in Balaban's published series as readable") |
| H7 | ROTDEF I4 "Nearest: PROOF 'W1-loc (4D) [S9]: reduced' …, N5, N2-exp (linearised, trivial background)" | **partly CONFIRMED** | N5/Theorem RW is the nearest (per-step covariance; Corollary B′). N2-exp is a deterministic tree-level response, like BFT-3. W1-loc is a large-field localisation, not a covariance statement |
| H8 | ROTDEF §9 item 2 ("SRC-W is (ARGUED) the infinitesimal, interior form of UNIV55's …") | **NOT-VERIFIED** literally | §8 (A5): same family, different objects; a common lemma is named |
| H9 | ROTDEF §9 item 3 ("any quantitative OS1 rate is at best logarithmic in a") | **CONFIRMED** for the route as split | §7. That it is a property of the defect is not claimed by ROTDEF and is ARGUED false (Symanzik [m]) |
| H10 | EXISTENCE X-SRC-GAP: "its variance diverges like ε^{-4}∫f² … so H-src in exponential form fails" (ARGUED) | **CONFIRMED (now PROVEN)** | Lemma V (V-3) |
| H11 | EXISTENCE Lemma X-SRC-CT (i)-(ii) | **CONFIRMED** (re-derived) | Proposition A steps (2)-(3) |
| H12 | EXISTENCE Lemma X-SRC-RED | **CONFIRMED**, with two improvements | Its \|T\| factor can be replaced by the number of cubes meeting supp h_1 (root polymers there); its C_IR is absent in the conditional form (§3.3 SRC-poly; Proposition A) |
| H13 | PANEL_P4 §2.1: "The input itself (local moment bounds for dimension-4 composites or flowed fields) is UV … and OPEN", and the §2 table cell "position-uniform local exponential-moment bounds for the local fields (H-src'/H-src-flow)" | **REFUTED for point-like dimension-4 composites** (OPEN only for flowed fields) | Lemma V (V-4). Also H-src′ is a separated-support statement, not a local moment bound |
| H14 | PANEL_P1 §4 "PROVEN — Conditional locality is not full correlation decay" | **CONFIRMED** (law of total covariance, re-derived) | consistent with Proposition B |
| H15 | PANEL_P1 §4 "ARGUED — What the requested BFT actually targets" (BFT locality is conditional background construction, not a gap) | **CONFIRMED** | §5.1 |
| H16 | PANEL_P4 S4(a) "A slowly varying bare coupling. This is the same technology X-SRC-GAP needs for OS0" (l.314) | **CONFIRMED** | §5.4 item 1, §8 (A6) |
| H17 | UNIV55 §3.4 correction: conditional covariance "decays … by the constraint-induced locality of the conditional fine measure (UV, BFT-3-type)" | **NOT-VERIFIED** (attribution) | §8 (A3): the decay is CD (N5/N6 + SRC), not BFT-3. "UV": agreed |
| H18 | UNIV55 §3.4 "No clustering, no coarse-law covariance, no CD-type input (ROTDEF needed CD only for torus-uniformity)" | **REFUTED** in its literal "no CD-type input" | A separated conditional-cumulant bound (SRC-κ (κ-2)) is needed, as UNIV55's own correction shows (§8 (A4)). Decay is not needed at fixed R. I agree with the correction, except for its BFT-3 attribution (H17) |

**Codex verdicts used (CODEX_REVIEW_ROTDEF.md, complete on disk; read in full):**
- **F1** (centred 𝒞(s) := ω(Ξ F̃_s) − dω(F̃_s)/ds): AGREE; used in Proposition D(iii).
- **F3** (insertion-side contact; R2/P do not exclude all contacts): AGREE. The dimension count was re-checked (§2.1).
- **F4** (SRC-E bounds ω(G²); a "real additional proof obligation"): AGREE, and **strengthened** to an inconsistency given
  any polylogarithmic separated bound (Lemma V, V-1).
- **F5** (exact one-covariance reduction; CD averaged suffices; strict coarse locality NOT-VERIFIED, with the two-site
  example; Lemma 5.3 confirmed): AGREE on all four. Proposition F supplies quasi-locality under SRC-poly; strict locality
  is not needed.
- **F6** (the equivalence concerns the *normalised* torque; E6): AGREE; not otherwise used.
- **F2** (R2, parity, Lemma 4.1 confirmed; C7 narrower): AGREE. SRC-M's list of three H(4)-split structures rests on it.
- F7–F9: not used.

---

## 10. Summary table of every claim made in this file

| # | Claim | Where | Label |
|---|---|---|---|
| 1 | Lemma V: Var_ω(O_a(f)) ≥ (c_v/1152)g_0⁴a⁻⁴(‖f‖²₂ − O(a)), c_v = 8e^{−5}/π³, uniformly in the torus, u_0 ≥ u_*(N) | §2.3 | PROVEN-HERE (unconditional; constants certified by `sc55_vm`: PASS, control fired) |
| 2 | V-1: SRC-E + non-vacuity ⇒ unnormalised separated correlator ≥ c g_0⁴a⁻⁴ (contradicts any polylog separated bound) | §2.3 | PROVEN-HERE (implication) |
| 3 | What OS0 needs for point-like e: separated multiscale bounds in OS's ^0𝒮 form; no coincident-point counterterms | §2.2 | ARGUED [m: OS I/II as recalled] |
| 4 | Precise statements: SRC-κ, SRC-κ-LF, SRC-M (8 constants), SRC-I, SRC-poly; CD-eff, CD-avg; SRC-E′, SRC-W′ | §3 | statements (all OPEN as hypotheses) |
| 5 | The finite operator list 𝒪_rot: 47 real local gauge-invariant functionals per site; 𝒪_0 = {e_a} for OS0 | §3.2 | definitions/count |
| 6 | Proposition A: SRC-poly ⇒ conditional cumulant decay (CD at rate (κ_s − κ_0)/M) | §4 | PROVEN-HERE (implication) |
| 7 | Proposition B: Cov(G,H\|U_K) = Σ_iE[Cov(G_i,H_i\|U_{i+1})\|U_K]; one-step law = RG-step integrand | §4 | PROVEN-HERE (exact; `sc55_tel` PASS, both controls fired) |
| 8 | Corollary B′: per-step decay ⇒ CD at the reference scale, uniformly in K | §4 | PROVEN-HERE (implication) |
| 9 | Proposition C: CD-eff + SRC-I + images ⇒ CD-avg (ROTDEF I4) | §4 (+ erratum E3) | PROVEN-HERE (implication) |
| 10 | Proposition D: SRC-κ(+LF) + SRC-M + SRC-I ⇒ CD-avg, SRC-E′, SRC-O, SRC-W′, hence Theorem 7.1 unchanged | §4 | PROVEN-HERE (implications; inputs OPEN) |
| 11 | Proposition E: SRC-κ (κ-1) + SRC-I ⇒ R-uniform cumulant and ^0𝒮 Schwinger bounds, limits along subsequences; no coarse decay used | §4 | PROVEN-HERE (a)-(c) as implication; OS-II matching ARGUED [m] |
| 12 | Proposition F: coarse images quasi-local under SRC-poly | §4 | PROVEN-HERE (implication) |
| 13 | Source recursion Φ_{k+1} = log E[e^{Φ_k}\|U_{k+1}]; Φ_K = −ΔS_K; first order linear; higher orders triangular; (B1) = solved second order | §5.0 | PROVEN-HERE (exact) |
| 14 | BFT-3 is not a covariance bound; BFT-4 is the source-free classical part of SRC-poly | §5.1 | ARGUED (reading of the statement) |
| 15 | The e-source's first variation is a divergence-form critical-point source d*(η dB_0), i.e. LP-SRC/Theorem 6.8's class | §5.3 | PROVEN-HERE (abelian linear, one line); curved case ARGUED |
| 16 | What sources add to BFT's induction (five items) | §5.4 | ARGUED |
| 17 | Verdict: CD follows structurally from the RG's conditional structure; not from banked lane results; R-b not realised; R-d realised literally; R-e not realised | §5.5 | reduction PROVEN; inputs OPEN |
| 18 | Missing list (M1)-(M6); removed items (M7) | §6 | OPEN (first-class result) |
| 19 | Rate: consistent (g_bare² ≍ 1/log under (F_R)); Poisson reformulation of the pair defect; log rate is a split artefact; SRC-OW would give a^{1/3}𝔏 | §7 | consistency PROVEN-HERE; reformulation PROVEN-HERE; artefact claim ARGUED [m] |
| 20 | Alignment with UNIV55 (A1)-(A6) | §8 | ARGUED |

Counts of my own claims: PROVEN-HERE 13 rows (1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 15 linear part, 19 consistency and
reformulation); ARGUED 6 rows (3, 14, 16, 20, and the ARGUED parts of 15 and 19); statements/definitions 2 (4, 5);
reduction plus OPEN 2 (17, 18).
Inherited verdicts (§9, H1-H18): **CONFIRMED 11** (H2, H3, H6, H9, H10, H11, H12, H14, H15, H16, plus H4's statement
half); **NOT-VERIFIED 5** (H4's size half, H5, H7's W1-loc/N2-exp attribution, H8, H17); **REFUTED 3** (H1, H13, H18). H7 is
counted as partly CONFIRMED.

---

## 11. For the Codex reviewer: load-bearing steps, in the order to check

1. **Lemma V** (§2.3), in this order:
   - Step 1's concavity bound F′(u) ≤ 2F(u)/u and the Haar-ball lower bound;
   - Step 2's sparse set (no plaquette contains two S-links);
   - Step 3's circle-coset disintegration and the identity Re[e^{is}w_1 + e^{−is}w_2] = Re[e^{is}(w_1 + w̄_2)];
   - Step 4's bound |z| ≥ 12 − NΣ_{p∋b}s(U_p);
   - Step 5's von Mises constants (`checks/sc55_vm`);
   - V-1's logic: the contradiction needs only a polylogarithmic separated bound, not H-src′.
2. **Proposition B** and its check `checks/sc55_tel`. Do the controls test the right failure? Non-Markov chains must break
   the Markov form while the tail-σ-algebra form survives.
3. **§5.0**: Φ_K = −(S_K(·;η) − S_K(·;0)) exactly, and the second-order recursion reproducing (B1).
4. **Proposition A**: the counterterm and missing-support cancellations, and Cauchy for the (1, …, 1) mixed derivative.
5. **Proposition D(i)**: the cumulant expansion of Cov(XY, Z | U_K). Check that no coincident-support conditional variance
   enters ROTDEF's step 5.
6. **Proposition C** with erratum E3: the self-avoiding path sum, the set expansion, and SRC-I.
7. **§7**: the Poisson reformulation ω_c(F̃_s) = Σ_za⁴C(z)Φ(Q_s⁻¹z) + O(a^M), and that Φ is supported away from 0.

**Where I expect the strongest objections.**
- SRC-M is a large, unproved package. Its O(g_bare²) size is power counting, and (M-c) is exactly where Codex F3's
  conditional-measure H(4)-breaking bites.
- SRC-κ's short-distance weights w_α are stated, not derived. Proposition A gives the decay structure, not the weights.
- Lemma V's u_*(N) is not computed (it depends on the Haar-ball constant c_N). Only its existence is used.
- The OS0 formulation (^0𝒮, OS-II growth) rests on [m] recollection.

---

## 12. Errata from my own re-read (append-only; each item overrides the text it names)

- **E1 (§1 table, row "η").** "BFT-1/RTARGET weights η? none found in the cited text" is wrong and is withdrawn. η is
  heavily used in the lane: PROOF.md's η_1 names three objects (PROOF l.91-93, "η_1 is THREE symbols"), plus η_* and
  others. Here η is only the e-source field, EXISTENCE §10.3's coupling field. Write η_src wherever a lane η is in scope.
- **E2 (Lemma V, displayed bound).** The bracket's last term is −O_f(a²), not −O_f(a^M). The Riemann sum of |f| (Lipschitz,
  not smooth) is accurate to O(a), multiplied by 24a‖∇f‖_∞. Nothing else changes.
- **E3 (Proposition C).** The statement's "q^{D_M/2}" and the in-proof "Correction to the displayed rate" are both
  withdrawn and replaced by the following.
  - 𝒫 ranges over **self-avoiding** *-connected M-cube paths. The path-sum output of a polymer expansion can be bounded
    by such sums.
  - Bound the images pointwise by (κ-3)-LF, |E_KŌ(f)| ≤ C_0e^{C_LF|𝔏∩𝒩(f)|}, instead of using Cauchy–Schwarz.
  - Expanding over the large-field sets then gives
    ν_K(|Cov(F̃, 𝒯(x)|U_K)|) ≤ C_F(1 + e^{C_LF}ε_LF)^{|𝒩|}N_∂(F)(80q″)^{D_M}/(1 − 80q″), with
    q″ := e^{2C_LF}ε_LF + e^{−m_cM}. Each cube of 𝒩 ∩ γ carries e^{2C_LF} or e^{−m_cM}; each cube of 𝒩 \ γ carries
    ≤ 1 + e^{C_LF}ε_LF.
  - **SRC-I's smallness condition should read 80(e^{2C_LF}ε_LF + e^{−m_cM}) < 1.** It is still one-sided: ε_LF small
    (g_ref small), m_cM large (blocks).
  - The rate is m′ = −log(80q″)/M per ℓ_ref.
- **E4 (SRC-M preamble and Proposition D(iv)).** δ_c is a fixed **physical** distance (e.g. d/4), not a multiple of a.
  (M-b) is a statement about the entire near region, including its power-divergent short-distance part. Integrating
  a²(dim-7) against e over distances ≥ ca would give a⁻⁴·a² = a⁻². That is exactly the contact that (M-b) packages as
  Σ_Rc_R(structure) + O(a²𝔏). The bulk constants in D(iv) depend on δ_c.
- **E5 (§5.3).** "REVIEW_S22 l.396-397" should read l.394. The quoted phrase is correct.
- **E6 (§0, UNIV55 bullet).** "On disk it holds only its pre-statement, so there is nothing to duplicate" was true at my
  PRE-STATED (00:50Z). UNIV55 grew to 713 lines by ≈01:22Z and was re-read in full. §8 supersedes the §0 bullet. The §0
  substance (shared per-block statement; SRC-W′ bulk from per-block bound + CD + SRC-E′ by Cauchy–Schwarz, no decay)
  stands, with §8 (A5)'s caveat that ROTDEF's "infinitesimal form of UNIV55" is NOT-VERIFIED literally.
- **E7 (§3.3, SRC-κ (κ-3)).** "|E_K[O(x)] − ω(O(x))| ≤ C_0 on 𝒮_K" is in units ℓ_ref = 1. For O of canonical dimension
  d_O, the bound is C_0ℓ_ref^{−d_O}, independent of a.
- **E8 (§10 counts).** Row 15 is counted once under PROVEN-HERE (its linear part) and once under ARGUED (its curved
  part). Row 19 likewise (PROVEN consistency and reformulation; ARGUED artefact claim). So the per-row tallies overlap by
  two. This was intended, and is now said explicitly.

---

## 13. Closing statement (2026-10-29, after all derivations above)

**The two inputs are one.**
- (CD) is the separated-support part of (SRC). The bridge is an exact identity of the soft chain (Proposition B):
  conditional covariance at the reference scale is the sum over RG steps of one-step conditional covariances of
  conditional images. That identity is the solved second-order source recursion (§5.0).
- So CD needs no coarse-law information: per-step decay (N5/N6), source-inserted images, and a coarse Peierls bound.
- (SRC) is stated precisely (§3) as conditional cumulant bounds for a finite list of 47 local operators per site, plus
  eight O(g_bare²) matching constants and a coarse local-integrability clause. Its mechanism is EXISTENCE's H-Bal-loc
  made conditional on U_K, which **removes H-Bal-loc's only IR object, the unit-scale remainder**.

**OS0 needs only the e-part.**
- That is SRC-κ (κ-1) at all orders plus SRC-I, with no decay of the coarse law (Proposition E).
- OS0 cannot be had from local moment bounds of the point-like energy density. Their variance diverges like g_0⁴a⁻⁴
  (Lemma V, PROVEN unconditionally).
- The same lemma **refutes ROTDEF's SRC-E** as part of any non-vacuous input set. All ROTDEF uses survive on the corrected
  SRC-E′.

**Status.**
- The lane does not supply CD or SRC. The banked pieces are linear (N5-triv/Theorem RW, LP-SRC Theorem 6.8), the
  cluster-expansion engine (Theorem CE), and chessboard (Lemma CBE).
- The rest is OPEN. In dependency order:
  - BFT^η, N5^η, N6^η;
  - per-U_K conditional RLF^η;
  - (F_R) with a slowly varying coupling;
  - large coarse fields (= UNIV55's N3);
  - the matching package SRC-M.
- **The same SRC serves OS0, ROTDEF's flat-route OS1, UNIV55's S⁴ Ward route and P4's S4(a).** It should be one node on
  the critical path, not four.

**Rate.** SRC-O's O(g_bare²) is consistent with a logarithmic rate on ROTDEF's route. That logarithm is a feature of the
route's split into separate inputs. A sharper joint input would give a power rate. P1 needs none.

## 14. Further errata from a full re-read (append-only; 2026-10-29, after §13)

- **E9 (§2.1 table, U1-U3 line numbers).** ROTDEF's Theorem 7.1 step 5 ("5. Conditional shell term") is at l.389-391 and
  step 6 ("6. Cov_ω(F_s, 𝔅(v_r)) is bounded by SRC-W, and 𝒞(s) by SRC-O") is at l.392. "(l.388-390)" and "(l.391)" have
  drifted by one line. The locating strings are correct.
- **E10 (§0 item (v) and §5.3, "G = 2ηF(Z)").** This is a normalisation slip. With e ≈ ½|F|², the first variation of
  ⟨η, e⟩ is d*(ηF), so G = ηF(Z), as in the abelian line G_0 = η·dB_0. The overall constant depends on e_a's normalisation,
  and nothing depends on it.
- **E11 (§2.3 V-1, fourth bullet).** "The same applies to SRC-E's clause for G = O_a(f)O_a(g). Its conditional variance
  contains Var(O_a(f)|U_K) times a separated factor." **is withdrawn as unproved.** ω(F̃²) ≥ c·Var(O_a(f))Var(O_a(g)) would
  need a bound on Cov(Ō(f)², Ō(g)²), which is not supplied. The refutation of SRC-E uses only its G = O_a(f) clause. That
  suffices, since SRC-E asserts both clauses.
- **E12 (Proposition A: scope and a missing quantifier).**
  - (i) The conclusion "uniformly in K" needs **sup_r A_r < ∞**, which is to be read into SRC-poly.
  - (ii) Levels with ℓ_r ≫ diam(X_1 ∪ ⋯ ∪ X_n) contribute O(1) each, with no tree suppression. There are about
    log_L(ℓ_ref/diam) of them. That is a fixed number for ROTDEF's fixed smeared f, g (uniform in a), and a logarithm at
    short distances, consistent with 𝔤_α.
  - (iii) The sup-norm polydisc gives bounds for **smeared** observables. The pointwise δ^{−4}-per-point weights of (κ-1)
    need a scale-adapted source norm: level-r activities bounded in terms of each source's volume fraction of the cube.
    That is part of the SRC-κ hypothesis, not derived by Proposition A (as §11 already says).
  - ROTDEF's uses involve only smeared e's plus point insertions entering linearly, so (iii) does not affect
    Proposition D. Proposition E uses (κ-1) as a hypothesis.
- **E13 (§1 table, row "J").** The middle cell is garbled. It should read: "J is ROTDEF's rotation generator and is never
  used for a source here; sources are always η (EXISTENCE §10.3 uses h, η, z)."
- **E14 (§3.3, SRC-I).** The smallness condition displayed there is superseded by E3's 80(e^{2C_LF}ε_LF + e^{−m_cM}) < 1.

Final timestamp (UTC, from `date -u` at the end of writing): see the next line.
Completed: 2026-10-29T01:39:23Z
