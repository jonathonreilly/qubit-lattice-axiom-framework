Reviewer model: claude-opus-5-5

# SEAM55 — the sphere route's two distinctive inputs: seam transparency (N5) and the dilation cancellation (W0)

Worker: Opus 5.5 (model ID above, verbatim from the system prompt). Scope: write only this file and `checks/sm55_*`.
No git. Append-only after this header block. Brief: `scratchpad/queue/seam.md`; shared rules: `REVIEW_BRIEF_55.md`.

## PRE-STATED (written before any derivation; UTC 2026-10-29 03:58)

Read so far: SPHERE55.md (all, as on disk at 03:57 UTC; CODEX_REVIEW_SPHERE.md does not exist yet). Nothing derived.

**Targets.**

S1 (W0, dilation channel). For the sphere regulator of SPHERE55 (§1.3-§1.4), take the coupling profile
beta_Q = 2N/g_0(a Omega(z_Q))^2 where a |-> g_0(a) is the bare-coupling trajectory shared by every other input (the
same function the flow/UIR lane controls). Decide, with an explicit formula: (i) what the coefficient c_4(a;x) of the
dimension-4 trace operator in the boost Ward identity is, as a function of the trajectory's own error terms (to be named
as an input owned by the flow lane); (ii) to what order c_4 must vanish for the Ward identity of SPHERE55 Thm 3.6 (with
its E10 two-scale quantifiers) to close; (iii) whether the lattice's own scale response (measure term, a^{-2} mixing of
a^2 O_6 into F^2, curvature terms) is cancelled by the trajectory profile or leaves an obstruction.
Deliverable: a CONDITIONAL theorem "c_4 = O(rate)" with every input named, or an exhibited obstruction.

S2 (N5, seam transparency, separated form). For bulk observables at physical distance >= d_0 > 0 from the equator:
prove sup_s |Cov(F_s, 𝔖(v))|/Z_e^2 <= rate(a) -> 0 conditional on named UV inputs stated for ALL coarse fields, or
exhibit an obstruction. In particular: (i) what the conditional decay of SRCCD55 Proposition B (as Codex confirmed it,
not as SRCCD55 states it) gives across a macroscopic distance d_0 when measured in lattice units at each RG scale;
(ii) what the O(a) seam slab's own operator content (by dimension, on a 3-dimensional defect) costs in the two-scale
bound; (iii) whether the conditional-mean (oscillation) term of Lemma 3.5 can be controlled without coarse decorrelation.

S3 (assembly). H_Euc on the sphere route as an implication: every input with owner and status (CONFIRMED / OPEN /
REFUTED), the first point (if any) where an input is not UV.

**What would count as a refutation (of a step, of the route, or of an inherited claim).**

Q1 (W0). A dimension <= 4 contribution to the dilation channel whose coefficient is NOT a function of the local
running alone (so no profile cancels it): e.g. an O(1) remainder from the a^{-2} mixing that differs between the curved
regulator and the flat trajectory, a curvature x (dimension-2) term (none should exist gauge-invariantly; checking),
or a dependence on the gradient of the profile at first order that is not a total derivative. Also: the order of
cancellation the Ward identity needs being stronger than any trajectory precision available (e.g. needing c_4 = o(a^p)
while the trajectory is controlled only to o(g^2)), which would make W0 unattainable on the current flow lane.

Q2 (N5). An explicit admissible F and Killing v with |Cov(F, 𝔖(v))|/Z_e^2 bounded below as a -> 0 for the cube-based
prism seam; or a seam-localized operator of dimension <= 3 (field-dependent, gauge-invariant) not excluded by the
regulator's symmetries; or a proof that the oscillation term cannot be bounded without decay of coarse-field
correlations at distances >> l_0 (infrared). Also: conditional decay of Proposition B being too weak in lattice units
(e.g. a mass in units of l_0 rather than of a, so e^{-m d_0/l_0} = O(1)), which would leave the seam contribution O(1)
unless another mechanism is supplied.

Q3 (any inherited claim). A CONFIRMED/PROVEN label in SPHERE55, UNIV55, PANEL_P4 or SRCCD55 that my derivation
contradicts on a load-bearing step: I will state the correction and its derivation.

Labels: PROVEN-HERE (complete argument written here) / CONDITIONAL (on named inputs; implication proven here) / ARGUED
(stated gap) / NOT-VERIFIED / REFUTED. [m] = literature from memory, never load-bearing.

---

# FINDINGS (appended from 2026-10-29 04:4x UTC, after the PRE-STATED block, the two criteria files and both checks)

## 0. Inputs read (as on disk), Codex verdicts used, and two coordinator notices

- Read in full or in the named sections, after the PRE-STATED block: SPHERE55.md (all, 865 lines at 03:57 UTC);
  PANEL_P4.md §5 (S1-S5, H1-H6); UNIV55.md §2 (Proposition T, §2.1-§2.5), §3.1-§3.4 (Theorem U, N1-N4, the Ward
  architecture W0-W3); CODEX_REVIEW_P4.md §1-§4, §7-§8; CODEX_REVIEW_UNIV.md §7, §8, §11; SRCCD55.md §0, §3, §4
  (Propositions A-C); CODEX_REVIEW_SRCCD.md "Scope and disposition", §1, §3; ROTDEF.md §3-§5 (Prop. 3.2, §3.2, §4.1-§4.3,
  Lemma 5.3); UIR55.md header, §5-§8; CODEX_REVIEW_UIR.md (R1-R3 only: still being written at 03:53 UTC and later;
  its last lines are R3, mid-review); FLOW55.md §0-§1 (consumers of the flow); RLARGE.md "(F_R)"; PROOF.md "E7
  (trajectory Cauchy estimate)" (located by string; lines 4545-4562 at read time); HANDOFF.md (all);
  ASSEMBLY55.md §4 N4, N8, §7 F3-F6, F13-F15; CODEX_REVIEW_SRCAN.md §3, summary table, "Exactly what may be banked";
  **CODEX_REVIEW_SPHERE.md (all 337 lines; appeared 04:28 UTC; complete, ends with "Exactly what may be banked")**.
- **Coordinator notice 1 (≈04:30 UTC):** account for ASSEMBLY55 §7 F3-F6, F13-F14 — answered item by item in §4.
- **Coordinator notice 2 (≈04:37 UTC):** CODEX_REVIEW_SPHERE landed; read before building further. Done before any
  N5/W0 text below was written (only the chart-algebra check sm55_1, which does not depend on it, had been prepared).
  What it changes for this file: (i) crossing weights are incident-cell sums (its Finding 2), used in §2.4;
  (ii) the coordinate-sphere RP is PROVEN (Finding 4), used in §3; (iii) the pair theorem does not give a state's
  symmetry (Finding 7) — every theorem below is stated for a general F and the assembly uses a determining family;
  (iv) all-coarse-field quantifiers (Finding 11) — every input below is stated conditionally for every coarse field;
  (v) the nonvacuity test (Finding 12) — §2.1 and check sm55_2 address it; (vi) ℓ_0 is a chart scale whose physical
  value reaches 2ℓ_0 at the pole (Finding 10) — adopted below; (vii) no lower bound on physical crossing lengths
  (Finding 15) — §2.4.
- **Codex verdicts used, with my agreement (each argument read):** CODEX_REVIEW_SPHERE Findings 1, 2, 4, 5, 6, 7, 8, 9,
  10, 11, 12, 14, 15 — AGREE with every one I use (I re-derived F4's coordinate-plane RP and F5's classical profile
  variation independently before reading them; same results). CODEX_REVIEW_SRCCD §1 (Proposition B CONFIRMED;
  Corollary B′'s large-field step REFUTED) and §3 (Lemma V; the scoped SRC-E incompatibility) — AGREE.
  CODEX_REVIEW_P4 §1.1, §1.2, §2.3, §4.1-§4.3 — AGREE. CODEX_REVIEW_UNIV §7.1-§7.3, §8, §11 items 5, 7, 8 — AGREE.
  CODEX_REVIEW_SRCAN item 3/6 (SA-F upper propagation CONFIRMED, positive lower bound REFUTED without q_* < 1) —
  AGREE; §1.6 below shows W0 needs no lower propagation bound.
- **Not built on:** SPHERE55 §4.4 item 1 (refuted literally by CODEX_REVIEW_SPHERE F9); SRCCD55 Corollary B′ as stated;
  SRC-E (sphere) and U-mom (CODEX_REVIEW_SPHERE F12, ASSEMBLY55 F5); the constant-β seam weights (F2);
  any statement of CODEX_REVIEW_UIR beyond R1-R3.
- **Symbols (defect 1).** 𝔖 = SPHERE55's seam term −T_χ (never the action S); S = action; Θ = RG-invariant trace
  operator; ℓ_0 = the hierarchy's terminal CHART spacing (physical Ωℓ_0 ∈ [ℓ_0, 2ℓ_0]); ℓ_i = L^{i−n}ℓ_0 chart spacing of
  level i (n levels, ℓ_n = ℓ_0); V = U_n the level-n (reference) field; u = local inverse coupling in "u-units"
  (β_Q = 2N u); B_T := −dT/dlog s the slope of a profile rule T (s = local physical spacing); B_loc(u) := the local
  trace-channel coefficient (§1.4); ϑ^p_R (R ∈ {1, 3, 6′}, and ϑ^p_D) := the plaquette-density analogues of SRC-M's
  observable-side constants ϑ_R (SRCCD55 §3.3 "(M-a)"), which are defined there for the clover e_a — different objects;
  A(u) := slope of the shared flat trajectory. Collisions with SPHERE55 §8 (s, c, Θ, S) are resolved as stated here.

## 0.1 Result in one page (derivations in §1-§3; every label is argued where the claim is made)

**W0 (dilation channel).**
- PROVEN-HERE (sm55_1, exact; controls fire): for ANY profile rule u = T(log(aΩ)), v_c·∇u = −(div v_c/4)·T′ in each chart;
  the north representative of a boost is exactly −v_c; the physical spacing a(1 + |cos θ|) has a kink at the seam and
  the chart divergence of a boost flips sign there (chart artefacts confined to the χ-slab).
- PROVEN-HERE (algebra): the profile enters the Ward functional EXACTLY as the Ward variation of an action-density source,
  W_profile(v) = W_{u_0}(v) + Ξ_v(Σ_p η_p s(U_p)), η_p = β̂_p − 2Nu_0. Its dimension-4 content is (a) one scalar term per
  point, (div v)·[B_loc(u) − (1 + ϑ^p_1)B_T]·(action density) — the only H(4)-scalar, reflection-even dimension-4
  operator (banked R1) — and (b) a **traceless coupling-gradient term −Σ(∂_μη)v^ν[ϑ^p_3 S^(3) + ϑ^p_6′ S^(6′)]_μν, which no
  scalar profile can cancel** and which is present for ROTATIONS about the poles as well (v_J·∇u = 0 there, but this term
  is not). Both coefficients ϑ^p are O(g_bare²) under SRC-M-type matching. SPHERE55's operator table (§3.4) and its §6
  "rotation channel: dimension >= 6" omit (b).
- CONDITIONAL theorem (implication PROVEN-HERE): define the profile by the local trace coefficient,
  **dT/dlog s = −B_loc(T)/(1 + ϑ^p_1(T))** ("Ward profile"). Then the scalar term vanishes identically and every
  profile-induced dimension-4 term is O(g_bare²) (the traceless one) + O(a²𝔏(1 + R⁻²)), given one matching input
  **LCS-a** (an SRC-M clause for the trace channel, variable coefficients, all coarse fields; owner: SRC lane; OPEN).
  W0's rate is therefore **logarithmic**, for every profile, unless the traceless mixings are O(a²𝔏) (an SRC-OW-type
  statement, OPEN) — the sphere route does not escape the logarithmic rate SRCCD55 §7 found for the flat route.
- The brief's candidate (the shared trajectory as profile) works iff the consistency **LCS-b**:
  B_loc/(1 + ϑ^p_1) = A (the trajectory's slope) to o(1) — a lattice Callan–Symanzik statement. Then the flow's error
  terms (ρ_k, b_k − b_∞, tuning stability) cancel identically and **no value b_∞ = β_0^std log L is needed**. Without
  LCS-b, |c_4| is bounded explicitly by the flow's error terms PLUS |B_loc/(1+ϑ^p_1) − b_∞/log L|. P4's two-loop profile
  needs instead the VALUE of B_loc (sm55_1 C7/X4: a 10% slope mismatch leaves c_4 → 1/11). The a⁻² mixing of a²O_6
  into F² is not an obstruction: it is part of B_loc, which the Ward profile matches by construction.
- LCS cannot be inferred from the trajectory's global properties ((F_R), F-tune, E7) without coarse decorrelation
  (ARGUED, §1.5): it must be proved as a local matching clause of the source-inserted RG.

**N5 (seam transparency, separated form).**
- PROVEN-HERE: the corrected two-scale bound (Lemma 3.5′), with ‖E[F|V] − ωF‖_{L²(ν)} in place of SPHERE55's
  (Var F)^{1/2}. Check sm55_2 (exact model, extending CODEX_REVIEW_SPHERE F12's blocks): at a normalization keeping a
  nonzero separated covariance (26/9), the corrected bound is n-uniform; the (Var F)^{1/2} form grows like n⁴.
- **Answer to the brief's question (PROVEN-HERE as a structural statement; exact model witness):** conditional decay at
  the soft-constraint mass, measured in each level's own lattice units, makes the contribution of every level with
  ℓ_{i+1} ≪ d_0 vanish (super-exponentially at the fine levels: e^{−m d_0/(2Lℓ_0 L^{−n})}), so the slab's lattice-scale
  content (valences, weights, the O(g/a) jump fluctuations, Var 𝔖 ~ R³a⁻⁵) never reaches F directly. **But it does NOT
  make the seam contribution vanish:** the top levels carry the a-independent factor e^{−m d_0/(2ℓ_0)}, and the coarse
  term Cov(E[F|V], E[𝔖|V]) has no decay at all. What vanishes N5 is the size of the seam flux's coarse images
  (conditional transparency). sm55_2: perfect conditional decay with Cov(F, J) = 70/27 (control Y1 fires); slab variance
  2n⁴ + 86/9 diverging while Cov(F, J) stays 70/27.
- CONDITIONAL theorem (implication PROVEN-HERE; §2.5): N5 holds with
  |Cov(F, 𝔖)| ≤ C(R, F)·(a/ℓ_0)^θ, given three inputs stated for EVERY coarse field and containing no fine-field moment:
  (N5-T*) conditional transparency at the reference scale; (N5-C) one-step conditional decay with transparency-weighted
  sizes, intermediate large fields included (Codex's repair of B′); (SRC-E′_∞) bounded coarse images of F.
  Power counting (ARGUED): θ = 1 for coarse images (dimension ≥ 5 seam flux, coefficient a), θ ≥ 1/2 for one-step
  fluctuation sizes (the two-sided mode's RMS (a/ℓ)^{1/2} at tree level), so N5 = O((a/ℓ_0)^{1/2}𝔏) conservatively.
- No obstruction found (§2.6). The single item carrying the whole of N5's content is (N5-T*) at ROUGH coarse fields.

**Assembly (§3):** H_Euc on the sphere route is an implication from W0 (LCS-a), W1, W3 (sup-over-V form), N5
(N5-T*, N5-C), SRC-E′_∞ — each for a determining ^0𝒮 family of finite products — plus layer 1 on K_a with a bounded
slowly varying profile, U-sep (replacing U-mom), U-alg, and a diagonal lemma DIAG, which is PROVEN-HERE as an
implication (§3.3). ASSEMBLY55's F3 is closed by Codex; F5's Lemma 3.5 part and F6 are repaired here; F4, F13, F14
(partly repaired), and F5's U-mom part remain named open leaves (§4).

---

## 1. W0 — the dilation channel

### 1.1 Exact chart algebra. PROVEN-HERE (checks/sm55_1: C1-C9 PASS, controls X1-X5 fire; criteria written first)
- South chart, boost v_c(x) = R²c + 2(c·x)x − |x|²c, Ω = 2R²/(R² + |x|²): div v_c = 8(c·x) and v_c·∇log Ω = −div v_c/4
  (C1); ∂_μv_ν − (div v/4)δ_μν is antisymmetric (C5: conformal Killing in the flat chart metric). Agrees with SPHERE55
  §1.1 (K3, K4) and CODEX_REVIEW_SPHERE F5.
- **North representative.** With φ(x) = R²x/|x|² (chart transition), Dφ(x)v_c(x) = −v_c(φ(x)) identically (C3; the
  sign is tested: X3 fires for +v_c). At |x| = R, Dφ is the reflection in the tangent hyperplane. So the north chart
  sees −v_c, as SPHERE55 §3.2 states.
- **Profile identity.** For ANY C¹ rule T and u(x) := T(log(aΩ(x))): v_c·∇u = −(div v_c/4)·T′(log aΩ) (C2; X1 fires for a
  wrong profile T(log aΩ²)). Writing B_T := −T′ (the profile's slope, > 0 for an asymptotically free rule):
  **v·∇u = (div v/4)·B_T** in each chart, for boosts; for rotations about the poles v_J·∇u = 0 (u is radial).
- **Kink.** In the polar angle θ from S, Ω_south = 1 + cos θ and Ω_north = 1 − cos θ (C4), so the physical spacing is
  a(1 + |cos θ|): minimal on the equator, one-sided θ-derivatives −a and +a there (X5 fires for the wrong north formula).
  The chart divergence flips sign across the equator (div v^N(y) = −8c·y, div v^S(x) = 8c·x, x = y on the equator): a
  chart artefact (the physical divergence of a Killing field is 0). Both live inside the χ-slab of width O(a), where
  Ξ_{v,χ} = 0, so they enter only N5 (§2.6 (c)).
- P4's two-loop rule: du/dlog s = −2β_0/(1 − β_1/(β_0u)) = −2β_0 − 2β_1/u − (2β_1²/β_0)/u² + O(u⁻³) (C6). CONFIRMS
  SPHERE55 §1.4 and CODEX_REVIEW_SPHERE F5.

### 1.2 What Theorem 3.6 needs from the dilation channel (implication PROVEN-HERE, with Lemma 3.5′ of §2.1)
For a local insertion Σ_x a⁴ w(x)J(x) with a c-number weight w: |Cov(F, Σ_x a⁴wJ)| ≤ ‖w‖_∞ 𝒲(F, J), where
𝒲(F, J) := Σ_x a⁴ [ν(|Cov(F, J(x)|V)|) + ‖E[F|V] − ωF‖_{L²(ν)}·inf_c sup_V |E[J(x)|V] − c|] is W1's quantity for J.
So the dilation and coupling-gradient terms of §1.3 vanish in Theorem 3.6 iff
  sup_x |c_4(a; x)|·𝒲(F, Θ̂) → 0  and  sup_x (|ϑ^p_3| + |ϑ^p_6′|)·sup(|∇u||v|)·𝒲(F, S^(R)) → 0
at fixed R. Any rate suffices if W1 bounds 𝒲 uniformly in a; if W1 only gives 𝒲 = O(𝔏(a)), the coefficients must be
o(1/𝔏(a)). No R-uniformity is needed (CODEX_REVIEW_SPHERE F14: a → 0 is taken first at each R).

### 1.3 The profile enters exactly as an action-density source; the full dimension-4 content. PROVEN-HERE (algebra)
**Exact linearity.** S = Σ_p β̂_p s(U_p) is linear in the weights, Ξ_{v,χ} acts on links only, and div Ξ_{v,χ} does not
depend on the couplings. Hence for every constant u_0, exactly,
  **W(v, χ) = W^{(u_0)}(v, χ) + Ξ_{v,χ} 𝒮_η,   𝒮_η := Σ_p η_p s(U_p),   η_p := β̂_p − 2N u_0,**
where W^{(u_0)} is the Ward functional of the constant-coupling action on the same complex. The profile's entire
effect on the Ward functional is the Ward variation of an action-density source η — the object whose matching
SRC-M (M-a) describes for the clover density, with f replaced by η. (With CODEX_REVIEW_SPHERE F2's incident-cell
weights, η_p = 2N[ū(p) − u_0], ū(p) the average of u over the four cubes at p; ū(p) = u(m_p) + O(a²∂²u) in the bulk.)
**Expansion.** Ξ_v s(U_p) is linear in the values v(m_b) at the midpoints of the links of p, and v is at most quadratic,
so (exactly, as for e_a in SPHERE55 §3.4 row T1) Ξ_v s_p = v^ν τ^p_ν + ∂_μv^ν τ^p_μν + ½∂_μ∂_ρv^ν τ^p_μρν at m_p. The H(4)
classification (banked: R1, R2, inversion parity P, Lemma 4.1) gives: the A-valued part of τ^p_μν has dimension ≥ 6
(coefficient a²); τ^p_μρν (three indices) is a c-number plus a²·(dimension 5); τ^p_ν = ∇̄_ν s̄ + t^p_ν with
t^p_ν = ϑ^p_1∇̄_ν s̄ + ϑ^p_3∇̄_ν S^(3)_νν + ϑ^p_6′∇̄_μ S^(6′)_μν + (dimension 7, coefficient a²); the trace part of τ^p_μν is
(4 + ϑ^p_D)s̄ + (dimension ≥ 6). Here s̄ is the site action density, S^(3), S^(6′) the diagonal-traceless and
off-diagonal dimension-4 tensors of SRC-M; the ϑ^p are finite mixings (dimension-5 total derivatives are the only
O(1) structures H(4) allows: Lemma 4.1).
**Summation by parts against η and the conformal Killing form.** For S symmetric traceless and v conformal Killing,
(∂_μv^ν)S_μν = (div v/4) tr S + w_μνS_μν = 0, and Σ_ν(∂_νv^ν)S^(3)_νν (no sum inside) = (div v/4)Σ_ν S^(3)_νν = 0 (the
diagonal of the antisymmetric w vanishes). So in Σ_x η v^ν ϑ∇̄_μS_μν = −ϑΣ_x[(∂_μη)v^ν + η∂_μv^ν]S_μν + O(a²) only the
gradient part survives. Collecting (local bookkeeping: expand at each x about u_0 := u(x), so the η·div v terms are
absorbed into the local trace coefficient):
  Ξ_v 𝒮_η = −(1 + ϑ^p_1)Σ_x a⁴(v·∇η) s̄ − Σ_x a⁴(∂_μη)v^ν[ϑ^p_3 S^(3) + ϑ^p_6′ S^(6′)]_μν + (dimension ≥ 6) + O(a²),
the traceless bracket meaning the H(4)-projected contractions above.
**Consequence (the full dimension-4 content of the dilation and coupling-gradient channels).** With LCS-a (§1.4) for
the constant-coupling trace channel and v·∇η = 2N(div v/4)B_T (§1.1):
  scalar:     Σ_x a⁴ (div v/4)·c_4(x)·Θ̂(x),   Θ̂ := 2N B_loc(u)s̄,   **c_4 := [B_loc(u) − (1 + ϑ^p_1(u))B_T]/B_loc(u)**;
  traceless:  𝔅_tl := −2N Σ_x a⁴ χ(∂_μu)v^ν[ϑ^p_3 S^(3) + ϑ^p_6′ S^(6′)]_μν.
- The scalar part is the only H(4)-scalar, reflection-even dimension-4 structure (R1: multiplicity 1; tr FF̃ is in the
  determinant representation and the dilation channel is reflection-even), so ONE function of x carries it: a scalar
  profile can cancel it.
- **The traceless part cannot be cancelled by any scalar profile** (it is in the 3 ⊕ 6′ representations; a profile
  changes only scalar coefficients). It vanishes classically (the classical variation is −¼∫(v·∇u)F², scalar only:
  CODEX_REVIEW_SPHERE F5) and arises only through the finite mixings ϑ^p_3, ϑ^p_6′.
- **It is present for rotations about the poles too:** v_J·∇u = 0 kills the scalar term, but (∂_μu)(Jx)^ν S_μν ≠ 0 (u
  radial: weight ∝ u′(r)Sym(x ⊗ Jx), traceless, nonzero off the axis). So on the profiled sphere the SO(4)_poles Ward
  identity is broken at order ϑ^p, not only by dimension-6 terms at order a². SPHERE55 §3.4 (row T2) and §6 ("holds for
  the rotation channel ... Hom_H(A, Sym² A) = 0") are incomplete in this respect: Hom_H(A, Sym²A) = 0 concerns
  operators built from the gauge field alone; with the background vector ∇u, the translation channel admits
  (∂_μu)·(traceless dimension-4 tensor), which is neither a total derivative of a gauge-field tensor (Lemma 4.1 does not
  apply) nor removable into 𝔖 (a position-dependent renormalization of 𝒯 reproduces the same term after summation by
  parts, because (∂_μv^ν)S_μν = 0).
- Other gradient terms of total dimension ≤ 4: (∂u)·(gauge-invariant dimension-3 vector): none; a(∂u)·(dimension-4
  operator with an odd number of free indices): excluded by P; so the next are a²(∇u)², a²∇∇u times dimension-4
  operators, O(a²/R²). The forward-difference Hessian term of the exact split, (a/2)Σχ(∂²_μv^ν)𝒯_μν =
  aΣχ[2c_ν𝒯_νν − c_νΣ_μ𝒯_μν] for boosts, is O(a|c|) times dimension-4 operators (W1's business; CODEX_REVIEW_SPHERE F5).

### 1.4 The input LCS (local Callan–Symanzik matching), stated precisely; owner and status
**(LCS-a) [matching; no value claimed].** For the hypercubic Wilson lattice with a bounded, slowly varying coupling
u(·) (|∇u| ≤ C/R, |∇∇u| ≤ C/R², u in the weak-coupling range of the shared trajectory), uniformly in a, x and for EVERY
coarse field V (large coarse fields with SRC-κ-LF's effective-distance discount, CODEX_REVIEW_SPHERE F11):
 (i) the trace-channel density D(x) := ω_μμ(x) − 𝒯_μμ(x) of the constant-coupling Ward functional (H(4)-scalar part of
     its first moment minus the trace of the identity's own current) equals 2N B_loc(u(x))s̄(x) + c(u) + ρ^D(x);
 (ii) the action-density source variation obeys §1.3's expansion with coefficients ϑ^p_R(u(x)), |ϑ^p_R| ≤ C g_bare²;
 (iii) u ↦ B_loc(u), ϑ^p_1(u) are Lipschitz, B_loc > 0, 1 + ϑ^p_1 > 0;
 and every remainder (ρ^D, the dimension ≥ 6 and O(a²) terms) has conditional cumulants and coarse images bounded by
 a²𝔏(a) times SRC-κ's bounds. Clause (ii) is SRC-M (M-a) for the action density with variable coefficients; clause (i)
 is a NEW SRC-M clause (call it (M-d), the trace channel), absent from SRCCD55 because ROTDEF's rotations have no
 dilation part. Uniqueness: B_loc(u) is determined by (i) (two values would make a marginal operator irrelevant).
 **Owner:** source-inserted RG lane (SRCCD55/SRCAN55 successors), with variable coefficients (ASSEMBLY55 F14/F15).
 **Status: OPEN. UV** (conditional on coarse fields; no fine-field moment; it passes CODEX_REVIEW_SPHERE F12's
 nonvacuity test because it constrains conditional cumulants and coarse images only).
**(LCS-b) [consistency; needed only for the trajectory profile].** B_loc(u)/(1 + ϑ^p_1(u)) = A(u) + o(1) relative, where
A is the slope of the shared flat trajectory: the lattice Callan–Symanzik statement that the local scale response
equals the running along the line of constant physics. Physically expected; OPEN; owner: SRC and flow lanes jointly.

### 1.5 Theorem W0 (the Ward profile). CONDITIONAL on LCS-a; implication PROVEN-HERE
**Statement.** Let T solve **dT/dlog s = −B_loc(T)/(1 + ϑ^p_1(T))** on [a, 2a] with T(a) := u_traj(a) (the equator
keeps the shared trajectory's coupling; any initial value works for W0), and let u(x) := T(log(aΩ(x))). Assume LCS-a.
Then, for every Killing field v of S⁴_R (boosts and rotations about the poles), the dimension-4 content of the dilation
and coupling-gradient channels of B(v, χ) is exactly 𝔅_tl (c_4 ≡ 0), and
  |Cov(F, dilation + coupling-gradient channels)| ≤ C sup_u(|ϑ^p_3| + |ϑ^p_6′|)·sup(|∇u||v|)·𝒲(F, S^(3,6′))
                                                   + C a²𝔏(a)(1 + R⁻²)·𝒲(F, ·),
which is O(g_bare²)·𝒲 = O(𝒲/log(ℓ_0/a)).
**Proof.** §1.3's exact decomposition; LCS-a (i)-(ii) at each x with u_0 = u(x); v·∇u = (div v/4)B_T with
B_T = B_loc/(1 + ϑ^p_1) by the choice of T gives c_4 ≡ 0; the remaining terms are 𝔅_tl and the remainders; apply §1.2.
Existence and uniqueness of T: LCS-a (iii) (Lipschitz ODE on a bounded interval). ∎
- **U-alg holds by construction:** B_loc, ϑ^p_1 are functions of u only (flat-lattice matching coefficients), and
  u_traj(a) is R-independent; so the rule s ↦ T(s) is R-independent.
- **Size of the profile.** T(a) − T(2a) = ∫ B_loc/(1+ϑ^p_1) dlog s ≈ 2b_0 log 2 in units u = 1/g² (≈ β_0^std log 2 in
  β-units: 0.26 for N = 2, 0.58 for N = 3): a bounded, slowly varying coefficient field, inside a fixed source polydisc
  if its radius exceeds this (SRCCD55 (N1)).
- **Rate.** Logarithmic (O(g_bare²)) because of 𝔅_tl, for EVERY profile; a power rate needs ϑ^p_3, ϑ^p_6′ = O(a²𝔏)
  (the action-density analogue of SRCCD55's SRC-OW, OPEN). The rate is irrelevant for Theorem 3.6 and for DIAG (§3.3).

### 1.6 The brief's candidate (trajectory profile) and P4's profile: what each needs
- **Trajectory profile** T = u_traj on [a, 2a] (L ≥ 3 > 2, so [a, 2a] lies inside one step [a, La]; interpolate linearly
  in log s, or use a continuous-a line of constant physics). Its slope is A, so c_4 = [B_loc − (1 + ϑ^p_1)A]/B_loc.
  - Under LCS-b: c_4 = (intra-step variation of A) = O(u⁻²) = O(g⁴) in a two-loop model (sm55_1 C8), plus 𝔅_tl as in
    §1.5. **The flow's error terms cancel identically** (they are inside A on both sides), and no value
    b_∞ = β_0^std log L is used.
  - Without LCS-b, the explicit dependence on the flow: with the lane's step relation A·log L = b^{(K)}_0 + ρ^{(K)}_0 +
    Δ_K (first step of the K-level chain, |ρ_0| ≤ C_ρ g_0² by (F_R), Δ_K := u^{(K)}_1 − u^{(K−1)}_0 the tuning-stability
    term of PROOF.md "E7.3 (tuning stability)"):
      |c_4| ≤ [ |B_loc/(1+ϑ^p_1) − b_∞/log L| + (|b^{(K)}_0 − b_∞| + C_ρ g_0² + |Δ_K − Δ_∞|)/log L ]·(1+ϑ^p_1)/B_loc
    (with Δ_∞ the limit of Δ_K if it exists; otherwise its oscillation enters). The first bracket term is LCS-b's
    content at leading order; the others are the flow's errors. So "a local dilation is compensated exactly by running,
    up to the trajectory's error" (the brief) is right **only given LCS-b**; the trajectory's own errors then drop out.
- **P4's two-loop profile (G-pert).** c_4 = [B_loc − (1 + ϑ^p_1)B_pert]/B_loc with B_pert = 2β_0 + 2β_1G² + ...; c_4 → 0
  needs B_loc/(1+ϑ^p_1) = 2β_0 + o(1): the VALUE of the local trace coefficient. sm55_1 C7: lim c_4 = (B_∞ − 2β_0)/B_∞;
  X4: a 10% leading mismatch leaves c_4 → 1/11 ≠ 0. With the first two coefficients matched, c_4 = O(G⁴) (C7) —
  SPHERE55's "formal order G⁴" is CONFIRMED as perturbative arithmetic, but no lane statement supplies the matching, and
  𝔅_tl = O(g²) dominates it anyway.
- **Ranking:** Ward profile (needs LCS-a) ⊂ trajectory profile (needs LCS-a + LCS-b) ⊂ G-pert (needs LCS-a + the value).

### 1.7 The suspected obstructions, examined
- **a⁻² mixing of a²O_6 into F² (the brief's example).** It is part of the lattice's scale response, i.e. of B_loc (and
  of ϑ^p_1), which the Ward profile matches by construction: **no residual**. It is a residual for any profile not built
  from B_loc (it is one source of the O(g²) mismatch of G-pert at the lane's one-loop precision).
- **The lattice's own scale response (measure term div Ξ).** Coupling-independent, entirely inside W^{(u_0)} (§1.3);
  its dimension-4 part is part of B_loc (it is the O(g²)-relative, one-loop-type piece of the trace channel).
- **Curvature.** The chart lattice is flat; curvature enters only through the profile and the observable maps. The
  Ward functional is a cutoff-scale object, so its gradient corrections are a²(∇u)², a²∇∇u = O(a²/R²); curvature effects
  at scales ℓ ≫ a (e.g. O(ℓ²/R²) corrections to the running at ℓ) belong to the SO(5)-invariant state, not to W, and
  must not be counted as breaking (a matching done with the flat normalization at the reference scale would wrongly show
  them as "c_4 = O(ℓ_0²/R²)"; LCS-a is stated at the cutoff scale for this reason). ARGUED.
- **Second-moment channel**: c-number + O(a²). **Forward-difference Hessian term**: O(a). **tr FF̃**: excluded.
- **The traceless coupling-gradient term 𝔅_tl**: genuine, O(g²), not cancellable by a scalar profile (§1.3). It is
  not an obstruction to Theorem 3.6 (o(1)); it fixes the rate at logarithmic.
- **Observable side (W3's dilation part).** By the same source computation with f in place of η: with a GLOBAL
  normalization Z_e(a) the observable side carries an O(g²) dilation defect (SPHERE55 row T1); with a LOCAL
  normalization Z_e(aΩ(x)) whose log-derivative is the observable's own trace coefficient (the observable-side analogue
  of the Ward profile), the scalar part cancels identically and only SRC-O's traceless mixings (O(g²)) remain.
  Recommended: local normalization (it is also an R-independent rule, as U-alg requires).

### 1.8 Why LCS must be proved locally (it does not follow from the trajectory). ARGUED
The trajectory's properties ((F_R), F-tune, E7/E7.3) are statements about the whole lattice theory under a uniform
change of (a, u). Turning them into a statement about the local Ward density requires a LOCALIZED dilation identity on
the flat torus, i.e. the Ward identity for ψ_r(x)·x with a cutoff ψ_r; its far-shell term is the dilation-current flux
through a shell at distance r from F, whose covariance with F is controlled only by coarse decorrelation — the same
infrared structure as ROTDEF's TQ. On the sphere there is no global dilation symmetry to compare with, and using the
sphere identity itself would be circular. So LCS-a (and LCS-b) must be proved directly as matching statements of the
source-inserted RG (UV), not deduced from the flow's global theorems.

### 1.9 Verdict on W0
- **CONDITIONAL theorem (Theorem W0, implication PROVEN-HERE):** with the Ward profile, W0 holds with residual O(g_bare²)
  (traceless) + O(a²𝔏), given LCS-a. **No obstruction found**; in particular the a⁻² mixing is not one.
- The brief's trajectory profile works iff LCS-b; then the flow's error terms cancel exactly and the value of b_∞ is not
  needed. P4's profile needs the value problem (UIR55's (UIR^♮) route) — strictly more.
- **New finding (first-class):** the profile induces an O(g²) traceless coupling-gradient insertion in BOTH the boost
  and the pole-rotation Ward identities, uncancellable by any scalar profile; W0's rate is therefore at best logarithmic
  on current inputs, as on the flat route.

---

## 2. N5 — seam transparency in separated form

Setting: 𝔖 = 𝔖(v, χ) = −T_χ (SPHERE55 §3.4, E9's index convention), for a fixed admissible χ of width δ = C_0a;
F ∈ 𝔉, the ^0𝒮 family: finite products F = Π_{k≤q} Õ(f_k) of centred smeared energy densities with mutually
separated supports, all at physical distance ≥ d_0 from the equator (chart distance ≥ d_0/2, since Ω ≤ 2), and their
transports F_s along a permitted path (CODEX_REVIEW_SPHERE F7's repair: the theorems below are stated for every such
F, not only q = 2). V := U_n is the level-n field (chart spacing ℓ_0; physical ≤ 2ℓ_0, CODEX_REVIEW_SPHERE F10).

### 2.1 Lemma 3.5′ (the two-scale bound with coarse images). PROVEN-HERE; checks/sm55_2 PASS
**Statement.** For bounded F, J: |Cov(F, J)| ≤ ν(|Cov(F, J|V)|) + ‖E[F|V] − ωF‖_{L²(ν)}·inf_{c∈ℝ} sup_V |E[J|V] − c|,
and ‖E[F|V] − ωF‖_{L²(ν)} ≤ inf_{c′} sup_V |E[F|V] − c′|.
**Proof.** Law of total covariance; Cov(E[F|V], E[J|V]) = E[(E[F|V] − ωF)(E[J|V] − c)] for every constant c; Cauchy–
Schwarz and ‖·‖_{L²(ν)} ≤ ‖·‖_∞. The second claim: ‖X − EX‖_2 ≤ ‖X − c′‖_2. ∎ (The constant c must be global, not
c(V): sm55_2 control Y2 fires for a pointwise c(V); this agrees with CODEX_REVIEW_SPHERE F6.)
**Relation to SPHERE55.** SPHERE55's Lemma 3.5 (and E6) bounds ‖E[F|V] − ωF‖_2 ≤ (Var F)^{1/2}. That is true but, for
the clover products of §3.3, (Var F)^{1/2} grows like a⁻⁴ at any normalization keeping a nonzero separated correlation
(Lemma V; CODEX_REVIEW_SRCCD §3; CODEX_REVIEW_SPHERE F12; ASSEMBLY55 F5). **Exact model (sm55_2;** X uniform on {0,1,2},
three blocks of n⁴ cells, H = n²ξ + X; extends CODEX_REVIEW_SPHERE F12): at normalization 1 the separated covariance is
Var(X²) = 26/9 for every n; Var F = 4n⁸ + 344n⁴/9 + 12482/81; ‖E[F|X] − EF‖_2 = 13√2/9 for every n. The corrected
bound is valid and n-independent for τ ∈ {1, 1/2, 1/10, 0} (T2); the (Var F)^{1/2} form is ≥ (7/3)n⁴τ (T3).
**Consequence.** SRC-E (sphere) is removed from the input list and replaced by
 **(SRC-E′_∞)** sup_V |E[F|V] − c_F| ≤ C_F Z_e^q (a conditional MEAN, for every coarse field; no fine-field moment).
In the model it holds with Z_e = 1 while the separated covariance stays 26/9: it passes the nonvacuity test that
SRC-E fails. (Whether SRC-E (sphere) itself is false for Yang–Mills needs a joint lower bound on two conditional
variances: NOT-VERIFIED here, as ASSEMBLY55 F5 also says; it is no longer needed.)
**On E10's shrinking scale.** With the coarse-image norm at scale s, ‖E[F|W_s] − ωF‖_2 ~ s⁻⁴ (two densities resolved at
s), so E10's thresholds a^{2/7}, a^{1/2}, |c_4|^{1/2} become a^{2/15}, a^{1/4}, |c_4|^{1/6} (sm55_1 C9; the exponent
arithmetic, given E10's power counting, which CODEX_REVIEW_SPHERE F6 rebuilt conditionally). Recommended instead:
s = ℓ_0 with Proposition B (§2.2), which needs no threshold at all.

### 2.2 Proposition B on the sphere chain. Exact (Codex-banked identity), applicable here
SRCCD55 Proposition B needs only a chain W_ch = e^{−S}Π_i K_i(U_{i+1}, U_i) with K_i ≥ 0 and ∫K_i dU_{i+1} = 1. SPHERE55
§1.6 (B1) supplies exactly this for the seam-adapted kernels (CODEX_REVIEW_SPHERE "seam-kernel bookkeeping",
CONFIRMED). So, with F_i := E[F|U_i], 𝔖_i := E[𝔖|U_i]:
  **Cov(F, 𝔖 | V) = Σ_{i<n} E[ Cov(F_i, 𝔖_i | U_{i+1}) | V ].**
Corollary B′ is NOT used as stated (CODEX_REVIEW_SRCCD §1 refuted its omission of intermediate large fields); the
per-step input below is stated for the full one-step law, as that review's repair requires.

### 2.3 The brief's question: does conditional decay across d_0, in lattice units, make the seam term vanish?
**Answer: no. It disposes of the fine levels only. PROVEN-HERE (structure) + exact model witness (sm55_2).**
- Per-step decay at the soft-constraint mass m_1 (level-(i+1) units) gives the level-i term the factor
  e^{−m_1(d_0/2)/ℓ_{i+1}}. Write j := n − 1 − i (levels below the reference level), so ℓ_{i+1} = L^{−j}ℓ_0 and the factor is
  **e^{−m_1(d_0/2ℓ_0)L^j}**. At the finest level (j = n − 1, ℓ_1 = La) it is e^{−m_1 d_0/(2La)}: super-exponentially small
  as a → 0, beating any power of a⁻¹ (in particular the slab's fine variance Var 𝔖 ~ (R/a)³a⁻⁸·a⁶ = R³a⁻⁵, its O(g/a)
  jump fluctuations (CODEX_REVIEW_SPHERE F9), the valence defects and the crossing weights). So **the slab's lattice-scale
  content never reaches F directly.**
- For each FIXED j the factor is **independent of a**. The top levels (j = 0, 1, …) contribute e^{−m_1 d_0/(2ℓ_0)}·(the one-
  step sizes of F_i and 𝔖_i at scale ~ ℓ_0), which do not vanish because of decay.
- The coarse term Cov(E[F|V], E[𝔖|V]) carries **no decay factor at all**; with UV inputs only it is bounded by
  ‖E[F|V] − ωF‖·osc_V E[𝔖|V] (Lemma 3.5′).
- Hence N5 holds iff the seam flux's images at scales comparable to ℓ_0 vanish as a → 0 — conditional transparency. Decay
  is neither sufficient (top levels; coarse term) nor used for the coarse term.
- **Exact model witness (sm55_2):** the "seam" functional J = O_D lives on a block disjoint from F's, so Cov(F, J | X) = 0
  for every X (perfect conditional decay), yet Cov(F, J) = 70/27 (control Y1 fires: "decay alone" fails); its fine
  variance Var J = 2n⁴ + 86/9 diverges while Cov(F, J) stays 70/27 (T4); with E[J|X] scaled by τ (transparency),
  Cov(F, J) = τ·70/27 exactly (K6). Not a Yang–Mills model; it decides the logic.
- **Non-model witness (consistent, ARGUED as in SPHERE55 E3):** the decoupled seam (all crossing weights 0) satisfies
  every decay requirement (cross-seam conditional covariances vanish identically), yet fails N5 for boosts through its
  boundary displacement response.

### 2.4 The O(a) slab's operator content: what it costs (power counting, ARGUED)
- **Once the field is single-valued across the seam**, the effective defect consists of the identity (a c-number: drops
  out of every covariance and every oscillation) and gauge-invariant local defect operators of dimension d ≥ 4 on the
  3-dimensional seam, with coefficients ~ a^{d−3}. Dimensions 1-3: none, except CS, excluded by the coordinate
  reflections θ_μ (SPHERE55 §4.3; CODEX_REVIEW_SPHERE F8, single-connection class). Two further candidates, checked here:
  the profile kink gives a·[∂_n u]·CS (excluded by θ_μ, which preserves the radial profile and reverses the seam's
  orientation) and a·[∂_n u]²... no: a²[∂_n u]·(dimension-4) (coefficient a²/R, harmless); a·∫_seam tr FF̃ is excluded by
  θ_eq (it fixes the seam pointwise and reverses the normal, so FF̃ is odd).
- The seam flux is the defect's displacement/tangential response: [T_nμ] = Σ_d λ_d ∂O_d, **dimension ≥ 5 with coefficient
  a**. So its coarse image at the reference scale, for a coarse field of bounded curvature, is O(a·(R/ℓ_0)³·ℓ_0⁻²)·𝔏 in
  units where E[F|V] = O(1): **θ = 1 for conditional means.**
- **Before single-valuedness: the two-sided mode** (CODEX_REVIEW_P4 §1.2): the interface term tr((D_ih)†D_ih), dimension
  2 on the seam — RELEVANT at the decoupled point, with bare coefficient ~ β̂_cross/a. With the correct incident-cell
  weights (CODEX_REVIEW_SPHERE F2), (3/4)β(2a) ≤ β̂_cross ≤ (3/2)β(a), and the bulk weight near the seam ≈ β(a), the
  tree-level stiffness ratio at scale ℓ is λ_seam(ℓ) = (β̂_cross/β_bulk)(ℓ/a) ≥ (3/4)(β(2a)/β(a))(ℓ/a) =
  (3/4)(1 − O(g²))(ℓ/a) → ∞ (E11's criterion, confirmed as arithmetic by CODEX_REVIEW_SPHERE F9). At equipartition the
  jump's typical size at scale ℓ relative to bulk fields is λ_seam(ℓ)^{−1/2} ~ (a/ℓ)^{1/2}; its effect on correlations
  (a thin layer's Kapitza resistance) is O(a/ℓ). **So θ ≥ 1/2 for one-step fluctuation sizes, θ = 1 for means**, at
  tree level. CODEX_REVIEW_SPHERE F9 is right that no finite soft-kernel step eliminates the mode (full support); the
  quantitative suppression is the core of N5-RG.
- The crossing chords have no uniform lower physical length (CODEX_REVIEW_SPHERE F15). The counts above use only the
  combinatorial structure, the weight bounds and the upper thickness 4a, so they are unaffected; N5-RG must not import
  estimates that assume uniformly regular cells.
- With a profile, "the identity's own current" must include the divergence part 𝒯^prof_μν := η(ϑ^p_1δ_μνs̄ + ϑ^p_3S^(3)
  + ϑ^p_6′S^(6′))_μν of the profile's source variation (§1.3); its shell flux enters 𝔖. Choosing u_0 := T(a) (the
  equator's coupling) makes η = O(B·a/R) on the shells, so this contribution is O(g²a/R): negligible.

### 2.5 Theorem N5 (separated form, with a rate). CONDITIONAL; implication PROVEN-HERE
**Inputs (each stated for EVERY coarse field V; none is a fine-field moment; owners and status in §3.2):**
- **(N5-T*) conditional transparency at the reference scale:** sup_V |E[𝔖|V] − c_𝔖| ≤ τ_*(a) → 0. (For boosts
  c_𝔖 = 0 is forced: E[𝔖|θ_eqV] = −E[𝔖|V].)
- **(N5-C) one-step decay with transparency-weighted sizes, intermediate large fields included:** for every level
  i < n and every V,
    E[ |Cov(F_i, 𝔖_i | U_{i+1})| | V ] ≤ Z_e^q Γ_F L^{p(n−i)} min{1, τ(L^{n−i}a/ℓ_0)} e^{−m_1(d_0/2)/ℓ_{i+1}},
  with τ(r) → 0 as r → 0 and constants Γ_F, p, m_1 > 0 independent of a.
- **(SRC-E′_∞)** sup_V |E[F|V] − c_F| ≤ C_F Z_e^q.
**Conclusion.**
  |Cov(F, 𝔖)|/Z_e^q ≤ Γ_F Σ_{j≥0} L^{p(j+1)} min{1, τ(L^{j+1}a/ℓ_0)} e^{−m_1(d_0/2ℓ_0)L^j} + C_F τ_*(a).
If τ(r) ≤ C r^θ and τ_*(a) ≤ C(a/ℓ_0)^{θ_*}: **|Cov(F, 𝔖)|/Z_e^q ≤ C(R, F)·(a/ℓ_0)^{min(θ, θ_*)}**, where
C(R, F) ≤ Γ_F C S_{p+θ} + C_F C with S_r := Σ_{j≥0} L^{r(j+1)}e^{−m_1(d_0/2ℓ_0)L^j} < ∞ (the super-exponential factor beats
the geometric one; the sum is dominated by small j). Uniform along any path F_s whose supports stay at distance ≥ d_0
from the equator, if the inputs are.
**Proof.** Lemma 3.5′ with J = 𝔖, then Proposition B for ν(|Cov(F, 𝔖|V)|) ≤ sup_V Σ_i E[|Cov(F_i, 𝔖_i|U_{i+1})| | V],
then (N5-C) with j = n − 1 − i. ∎
**Rate (ARGUED, §2.4):** θ_* = 1, θ ≥ 1/2 at tree level ⇒ **N5 = O((a/ℓ_0)^{1/2}𝔏(a)) conservatively, O(a𝔏(a)/ℓ_0) if
(N5-C)'s sizes are at correlation level**; constants depend on R (allowed: CODEX_REVIEW_SPHERE F14). Theorem 3.6 needs
only o(1). The withdrawn SPHERE55 rate (§4.4 item 2) is not resurrected: this rate comes from s = ℓ_0 + Proposition B, not
from a shrinking scale.

### 2.6 Obstruction search (a counterexample would be first-class). None found
- (a) Decoupled seam: excluded (positive weights ≥ (3/4)β(2a)); fails (N5-T*) while satisfying decay — consistent with
  §2.3. (b) Crossing weights vanishing faster than a/ℓ relative to the bulk would keep λ_seam bounded and fail; excluded by
  the weight bounds. (c) CS and the kink-induced a[∂_nu]CS: excluded by θ_μ; a∫FF̃ by θ_eq. (d) The two-sided mode:
  relevant at the decoupled point only; tree-level suppressed at ordinary weights; its nonperturbative suppression is
  N5-RG (open, not refuted). (e) Pole rotations: tangential flux; the staircase's H(4)-only anisotropy gives dimension-4
  defect operators with coefficient a: θ = 1. (f) Metric degeneration of crossing chords: irrelevant to the combinatorial
  measure (§2.4). (g) Rough coarse fields: no specific obstruction, but nothing banked reduces them to small fields (the
  bounded-curvature interpolation is existential, CODEX_REVIEW_SPHERE F11); (N5-T*) at rough V is the open heart of N5.
  (h) Profile-current shell terms: O(g²a/R). (i) Nonvacuity: no input is a fine-field moment (§2.1, sm55_2).

### 2.7 Verdict on N5
- **CONDITIONAL theorem with a rate** (Theorem N5): |Cov(F, 𝔖)|/Z_e^q = O((a/ℓ_0)^{1/2}𝔏) at fixed R, for every F in
  the ^0𝒮 family, from (N5-T*), (N5-C), (SRC-E′_∞), all stated for every coarse field.
- **The brief's mechanism (decay across a macroscopic distance at the soft-constraint mass) does not by itself make
  the seam contribution vanish**: it removes the fine levels; the vanishing comes from transparency of the seam's
  coarse images (N5-T*) and of its top-level one-step fluctuations (the τ factor in N5-C).
- The slab's operator content costs the factor (a/ℓ)^θ with θ = 1 for means and θ ≥ 1/2 for fluctuations, provided the
  field is single-valued at scales ≫ a, i.e. provided the two-sided mode is suppressed: that is the whole content of
  N5-RG. No counterexample.

---

## 3. Assembly: H_Euc on the sphere route, as an implication

### 3.1 The tree
**Consumed** (ASSEMBLY55 N4, N1F form): for each F in a countable determining family and each g in a countable dense
subgroup G_0 ⊂ E(4), |ω_{a_j,R_j}(F∘g⁻¹) − ω_{a_j,R_j}(F)| → 0 along one joint sequence; or (N1S form, CODEX_REVIEW_P4
§4.1, CODEX_REVIEW_SPHERE F14) fixed-R invariance on the pole cap followed by R → ∞.
**H_Euc (sphere) ⟸ (A) + (B) + (C):**
- **(A) Fixed-R local Killing invariance on the determining family.** For each R ≥ R_0, each F ∈ 𝔉 (§2's ^0𝒮 family,
  supports in the cap |z| ≤ K, z = 2x) and each permitted path (rotations about S; boosts keeping supports at distance
  ≥ d_0 from the equator): sup_s |ω_{a,R}(F_s) − ω_{a,R}(F_0)|/Z_e^q ≤ ε_R(F; a) → 0 as a → 0, constants allowed to
  depend on R.
  (A) ⟸ exact Ward identity and split (banked, CODEX_REVIEW_SPHERE F5) + integration in s (SPHERE55 Theorem 3.6, whose
  proof is F-independent) + Lemma 3.5′ (PROVEN-HERE) + for every F ∈ 𝔉: **W0** (Theorem W0 ⟸ LCS-a, + W1 for the Θ̂ and
  S^(3,6′) insertions), **W1**, **W3** (sup-over-V form), **N5** (Theorem N5 ⟸ N5-T*, N5-C, SRC-E′_∞) — each of these
  inputs in turn needs **layer 1 on K_a with the profile** (L1-sphere).
- **(B) R → ∞ transfer** (CONDITIONAL, banked as such: CODEX_REVIEW_SPHERE F14, bankable item 5): contraction geometry
  (PROVEN); θ_μ reflection positivity at every cutoff (PROVEN, CODEX_REVIEW_SPHERE F4) transported by the limit's SO(4)
  and translations; requires **U-sep** (position- and R-uniform separated-point moment bounds for the renormalized
  smeared density, replacing U-mom) with an ^0𝒮 version of the local-to-global/contraction lemma, and **U-alg**.
- **(C) DIAG** (§3.3, PROVEN-HERE as an implication): (A) with R-dependent constants + U-sep ⇒ the N1F joint-sequence form.
- **Not needed:** equatorial RP (used only by P4's S3 route); seam CONTACT estimates (observables never meet the seam);
  full finite-R SO(5) invariance; uniqueness, clustering, a gap; identification with a flat-torus selection (needed only
  under the strict reading of T_OS, PANEL_P4 H6 — the one item that is infrared in every reading).
- **First non-UV item in the implication: none.** Every input above integrates scales below ℓ_0 with the coarse field
  held fixed, for every coarse field (CODEX_REVIEW_SPHERE F11's operational sense) — or is a uniform local moment bound.

### 3.2 Inputs, owners, status (status as on disk 2026-10-29 ≈04:55 UTC)

| # | Input | Precise form | Owner | Status |
|---|---|---|---|---|
| 1 | Regulator K_a; incident-cell weights; RP for the equator and the four coordinate spheres | SPHERE55 §1-§2 with CODEX_REVIEW_SPHERE F2 | SPHERE55 | PROVEN (Codex F1, F2-corrected, F4) |
| 2 | Exact Ward identity, χ-independence, exact split W = B + 𝔖, no far shell | SPHERE55 §3.1-§3.4 | SPHERE55 | PROVEN (Codex F5; split is definitional) |
| 3 | Lemma 3.5′ (coarse-image two-scale bound) | SEAM55 §2.1 | SEAM55 | PROVEN-HERE; pending Codex |
| 4 | Theorem 3.6 for general F (integration of the identity) | SPHERE55 §3.5; F-independent proof | SPHERE55 | PROVEN as implication (Codex F6 for the pair; same proof) |
| 5 | W0 = Theorem W0 (Ward profile) | SEAM55 §1.5 | SEAM55 | CONDITIONAL on LCS-a; pending Codex |
| 5a | LCS-a: SRC-M clause (M-d) for the trace channel + (M-a) for the action density, variable coefficients, all V | SEAM55 §1.4 | SRC lane | OPEN (UV) |
| 5b | LCS-b (only if the shared trajectory is used as profile) | SEAM55 §1.4 | SRC + flow lanes | OPEN; not needed with the Ward profile |
| 6 | W1 for every F ∈ 𝔉: rotation channel (dim ≥ 6), translation (dim 7), contacts (CODEX_REVIEW_ROTDEF F3), O(a) Hessian term, Θ̂ and S^(3,6′) insertions, in 𝒲-form | SPHERE55 §3.5 with E10; SEAM55 §1.2 | SRC lane | OPEN |
| 7 | W3 in sup-over-V form, every F ∈ 𝔉, local Z_e(aΩ) normalization | CODEX_REVIEW_SPHERE F11; SEAM55 §1.7 | SRC lane | OPEN |
| 8 | N5 = Theorem N5 | SEAM55 §2.5 | SEAM55 | CONDITIONAL; pending Codex |
| 8a | N5-T* (conditional transparency at ℓ_0, every V) | SEAM55 §2.5 | sphere seam RG (N5-RG/N5-op) — unassigned | OPEN |
| 8b | N5-C: decay factor = SRC's real conditional decay incl. intermediate large fields; τ-factor = seam RG | SEAM55 §2.5 | SRC lane (decay) + seam RG (τ) | OPEN |
| 9 | SRC-E′_∞ (bounded coarse images of every F ∈ 𝔉, every V) | SEAM55 §2.1 | SRC lane (κ-3 with LF discount, all q) | OPEN |
| 10 | L1-sphere: BFT clauses, action-based large-field bounds (no chessboard), flow with a bounded slowly varying profile (SA-F upper propagation, position-dependent) on K_a | ASSEMBLY55 F13-F15; SPHERE55 §4.5 | BFT / large-field / flow lanes | OPEN |
| 11 | Contraction geometry and conditional transfer | CODEX_REVIEW_P4 §4.1; CODEX_REVIEW_SPHERE F14 | — | PROVEN (transfer conditional on 12, 13) |
| 12 | U-sep + ^0𝒮 contraction lemma (replaces U-mom, excluded in scope by Lemma V) | ASSEMBLY55 F5 repair | SRC lane / OS0 | OPEN |
| 13 | U-alg: R-independent observable maps and profile rule | SEAM55 §1.5, §1.7 | SEAM55 | PROVEN by construction, given LCS-a defines B_loc, ϑ^p_1 |
| 14 | DIAG | SEAM55 §3.3 | SEAM55 | PROVEN-HERE (implication); pending Codex |
| 15 | q-point (all n) versions of 6, 7, 8a-b, 9 | CODEX_REVIEW_SPHERE F7; ASSEMBLY55 F4 | SRC lane | OPEN (inside 6-9) |
| — | H_int: a uniformly SIGNED witness (outside H_Euc) | CODEX_REVIEW_SPHERE F13 | NONFREE | OPEN |

Most likely points of failure, in order: (i) **N5-T* at rough coarse fields** (the two-sided mode's suppression and the
seam's coarse image when the top levels are not weakly coupled); (ii) **LCS-a and W1 at rough coarse fields**; (iii)
**U-sep's nonvacuity** (separated-point bounds at a normalization keeping nonzero separated correlations — the R-limit
analogue of CODEX_REVIEW_SPHERE F12's danger; the fixed-R Ward part no longer depends on fine moments, §2.1).

### 3.3 DIAG (iterated limits give the joint-sequence form). PROVEN-HERE as an implication
**Setting.** 𝔉_0 = {F_k} a countable subfamily of 𝔉 (test functions from a countable dense set; supports in the pole
chart, mutually separated), G_0 = {g_k} a countable dense subgroup of E(4). For g ∈ E(4) let g_R be its sphere
counterpart: rotations about S act exactly; a translation by w is the boost exp(|w| v_{c(w)}) with c(w) = ŵ/(2R²) (unit
physical speed at S). Lattice observables are built from the pulled-back test functions in z = 2x.
**Hypotheses.** (H1) = (A): for each k there is R_0(k) such that for every R ≥ R_0(k), e_{R,k}(a) :=
|ω_{a,R}(F_k∘g_{k,R}⁻¹) − ω_{a,R}(F_k)| → 0 as a → 0 (the Ward paths realizing g_{k,R} keep supports at distance ≥ d_0 from
the equator once R ≥ R_0(k)). (H2) = U-sep at the lattice level: |ω_{a,R}(Π_i Õ(f_i)) − ω_{a,R}(Π_i Õ(f′_i))| ≤
A^q(q!)^b Σ_i p(f_i − f′_i) Π_{l≠i} max(p(f_l), p(f′_l)) for separated supports, with A, b, p independent of R ≥ R_0 and
a ≤ a_0(R).
**Conclusion.** There are R_j → ∞, a_j → 0 with |ω_{a_j,R_j}(F_k∘g_k⁻¹) − ω_{a_j,R_j}(F_k)| → 0 for every k; and along a
further subsequence ω_{a_j,R_j} converges on 𝔉_0 (H2 + diagonal extraction) to an E(4)-invariant limit.
**Proof.** |ω(F∘g⁻¹) − ω(F)| ≤ |ω(F∘g⁻¹) − ω(F∘g_R⁻¹)| + e_{R,k}(a). The first term is ≤ δ_{R,k} := q A^q(q!)^b max_i
p(f_i∘g⁻¹ − f_i∘g_R⁻¹)(max_l p)^{q−1}, and p(f∘g⁻¹ − f∘g_R⁻¹) = O_k(R⁻²) because the boost flow in z-coordinates is
z ↦ z + w + O(|w|K²/R²) in every C^m norm on compacts (SPHERE55 §5.2; CODEX_REVIEW_SPHERE F14): uniformly in a. Take
R_j := R_0 + j and a_j ≤ min(a_0(R_j), 1/j) with e_{R_j,k}(a_j) ≤ 1/j for the finitely many k ≤ j with R_0(k) ≤ R_j
(possible by H1, R-dependent constants allowed). For fixed k and j large: defect ≤ δ_{R_j,k} + 1/j → 0. The convergent
subsequence and the invariance of its limit follow from H2 (equicontinuity) and the vanishing defects. ∎
So ASSEMBLY55's F6 reduces to U-sep (row 12), which is F5's open leaf.

---

## 4. ASSEMBLY55's sphere-route mismatches (coordinator's request): repaired here, or a named open leaf

| ASSEMBLY55 item | What it says | Disposition after SEAM55 |
|---|---|---|
| **F3** — the flat limit uses θ_μ RP, proved by one line; SPHERE55 §1.5 vs §5.2 inconsistent | consumed RP ≠ banked RP | **CLOSED (not by me):** CODEX_REVIEW_SPHERE F4 PROVES RP for the equator and all four coordinate great spheres at every cutoff for the actual (incident-cell) weights. I re-derived the θ_μ argument before reading F4 (crossing chart edges between x_μ = ±a/2 form a matching in both charts; each prism square over such an edge reduces, after gauge-fixing its two chart edges, to C_w C_v⁻¹ = θ_μ(C_v)C_v⁻¹, a positive-kernel crossing term with weight ≥ 0): AGREE. SPHERE55's internal inconsistency is moot: §5.2's use is the operative one and is now banked. |
| **F4** — producers give two-point orbits; OS1 needs all n | order n | **NOT repaired; made explicit.** Theorems W0 and N5 here are stated for every F in the ^0𝒮 family (all q): W0's coefficients are F-independent; N5's inputs enter only through F's coarse images and one-step sizes. So separated-from-the-seam N5 suffices for all n (agree CODEX_REVIEW_SPHERE F7). **Open leaf:** the q-point versions of W1, W3, N5-C, SRC-E′_∞ (SRC lane; SRC-κ (κ-2) for all n). |
| **F5** — SRC-E and U-mom of the type Lemma V excludes | consistency | **Lemma 3.5 part REPAIRED here** (Lemma 3.5′, PROVEN-HERE; sm55_2 shows on an exact model that the repaired bound is n-uniform at a normalization keeping a nonzero separated covariance, while the Var F form grows like n⁴). SRC-E (sphere) is removed; SRC-E′_∞ (a conditional mean, every V) replaces it. None of W0's or N5's inputs is a fine-field moment. **U-mom part: open leaf** (U-sep + ^0𝒮 contraction lemma; SRC lane / OS0). |
| **F6** — iterated limits vs the joint sequence | quantifier order | **REPAIRED as an implication:** DIAG (§3.3, PROVEN-HERE) turns (A) with R-dependent constants (allowed, CODEX_REVIEW_SPHERE F14) plus U-sep into the N1F joint-sequence form. Residual leaf: U-sep (= F5's). |
| **F13** — RG producers live on tori; the sphere consumes them on K_a | domain | **NOT repaired.** The seam part of F13 is exactly my N5-T* and N5-C's τ-factor (N5-RG); the bulk part ((LOC-T): conditional estimates depend only on local geometry) is untouched. Added constraint from CODEX_REVIEW_SPHERE F15: N5-RG cannot import uniform-shape regular-cell estimates. **Open leaf** (row 10, 8a). |
| **F14** — constant-coupling flow produced; position-dependent profile consumed | trajectory | **PARTLY repaired.** ASSEMBLY55's proposed (FLOW-pos) ("a flow/locality theorem for slowly varying bare profiles (W0's c_4 → 0), with a lower propagation bound") is replaced, for W0, by LCS-a + the Ward profile: W0 needs NO lower propagation bound (that is a statement about persistence of marginal shifts, used elsewhere; CODEX_REVIEW_SRCAN item 3) and NO value of b_∞. What remains position-dependent is the variable-coefficient layer 1 (BFT, large fields, the flow's UPPER propagation for a bounded profile — SA-F, banked conditionally for constant shifts), shared with SRC's sources (F15's coefficient class). **Open leaves:** LCS-a (row 5a), L1-sphere (row 10). |

---

## 5. Errata to this file (append-only; each overrides the text it names). Found on re-derivation, ≈04:56 UTC

- **E1 (§0.1 W0 bullets 2-3, §1.3 "Summation by parts ..." and "Consequence", §1.4 (ii)-(iii), §1.5 statement and
  "Rate", §1.6, §1.9 last bullet; SUBSTANTIVE).** §1.3 treated the mixing coefficients ϑ^p_R as constants while
  differentiating η. They are matching coefficients of the state, ϑ^p_R(u(x)) at the local coupling (LCS-a's
  locality), and the constant-coupling part W^{(u_0)} also carries them at u(x). Redoing the summation by parts on the
  full action part Σ_x 2N u(x) v^ν[(1 + ϑ^p_1(u))∇̄_ν s̄ + ϑ^p_3(u)∇̄_ν S^(3)_νν + ϑ^p_6′(u)∇̄_μ S^(6′)_μν] (with the local
  current 𝒯(u(x)) carrying the divergence parts) gives, exactly up to the same remainders:
  - scalar: (div v/4)·2N[B_loc(u) − κ(u)B_T]·s̄ with **κ(u) := d[u(1 + ϑ^p_1(u))]/du** (not 1 + ϑ^p_1); B_loc(u) =
    u(ϑ^p_D − 4ϑ^p_1) + m̃ (m̃ from the measure term) is LCS-a (i)'s coefficient, unchanged;
  - traceless: **𝔅_tl = −2N Σ_x a⁴ χ (∂_μu) v^ν [ (uϑ^p_3)′ S^(3) + (uϑ^p_6′)′ S^(6′) ]_μν**, (uϑ)′ := d(uϑ(u))/du.
  Check of the bookkeeping on a linear profile u = u_0 + k·x: the source term gives −2Nk_μv^νϑ_R S, the constant-coupling
  part gives −2Nu_0ϑ_R′k_μv^ν S; the sum at u = u_0 is −2N(ϑ_R + uϑ_R′)k_μv^ν S. Consequences:
  1. The Ward profile is **dT/dlog s = −B_loc(T)/κ(T)**; c_4 ≡ 0 as stated. The trajectory profile needs LCS-b in the form
     B_loc/κ = A; G-pert needs B_loc/κ = 2β_0 + o(1). Rankings and conclusions of §1.6 unchanged.
  2. **Size of 𝔅_tl.** One-loop mixings are ϑ^p_R = c_R/u + O(u⁻²), so uϑ^p_R = c_R + O(1/u) and (uϑ^p_R)′ = O(u⁻²) =
     **O(g⁴) in perturbation theory** (the one-loop part drops out). Nonperturbatively, SRC-M-type bounds |ϑ| ≤ Cg² do NOT
     bound (uϑ)′ at all; LCS-a (ii) must therefore include **|d(uϑ^p_R)/du| ≤ C g_bare²** (true, e.g., if uϑ^p_R is
     analytic and bounded on discs |u′ − u| ≤ ρu, by Cauchy). With that clause 𝔅_tl = O(g²); perturbatively O(g⁴).
     Likewise κ = 1 + O(g⁴) perturbatively, and LCS-a (iii) should read: κ Lipschitz and κ > 0.
  3. Unchanged: 𝔅_tl is in the 3 ⊕ 6′ representations, so no scalar profile cancels it; it is present for pole rotations;
     SPHERE55's §3.4/§6 rotation-channel statement omits it. Changed: "W0's rate is logarithmic for every profile" now
     reads **"in the separate-bounds bookkeeping, logarithmic (O(g²) or O(g⁴))"**. A joint statement in which 𝔅_tl, the
     observable-side mixings and the contacts cancel together (an SRC-OW-type input extended by 𝔅_tl) is what a power
     rate would need; as SRCCD55 §7 found for the flat route, Symanzik counting predicts it only by presupposing the
     invariance being proved, so it stays OPEN. (Heuristic support for joint cancellation: a dimension-0 traceless tensor
     built from u and its derivatives does not exist, so no O(a⁰) effective-action term can produce 𝔅_tl; I do not
     claim this as a proof.)
- **E2 (§2.4 first bullet).** The fragment "and a·[∂_n u]²... no: a²[∂_n u]·(dimension-4) (coefficient a²/R, harmless)"
  should read: "and a²[∂_n u]·(dimension-4 defect operator), coefficient a²/R, harmless".
- **E3 (§2.4 last bullet; WITHDRAWN).** The "𝒯^prof" bookkeeping belongs to the global-u_0 decomposition corrected in E1.
  With the local current 𝒯(u(x)), 𝔖 is simply the net flux of the identity's own current, and no separate profile-current
  shell term arises; the "O(g²a/R)" estimate is withdrawn as moot. §2.6 (h) is withdrawn with it.
- **E4 (§0.1 N5 bullet 2).** The fine-level decay factor "e^{−m d_0/(2Lℓ_0 L^{−n})}" is e^{−m_1 d_0/(2La)} (ℓ_1 = La), as in §2.3.
- **E5 (§1.2).** In the second displayed condition read (uϑ^p_3)′, (uϑ^p_6′)′ for ϑ^p_3, ϑ^p_6′ (E1).
- **E6 (§0.1 W0 last bullet).** "(ARGUED, §1.5)" should read "(ARGUED, §1.8)".
- **E7 (§1.6, the explicit bound without LCS-b; SUBSTANTIVE for that bound only).** The first tower step of the K-level
  chain starts from the Wilson action, so its one-loop running is b^W := 𝔅(J_0) (FLOW55's b_k at k = 0, a fixed number
  independent of K and u), NOT a quantity tending to b_∞. Correct decomposition: A·log L = u^{(K)}_0 − u^{(K−1)}_0 =
  b^W + ρ^{(K)}_0 + Δ_K, with |ρ_0| ≤ C_ρg_0² ((F_R)) and Δ_K := u^{(K)}_1 − u^{(K−1)}_0 (tuning stability, PROOF.md
  "E7.3": the bare couplings differ by one marginal step up to O(L^{−κK})). Then, with κ from E1,
    |c_4| ≤ [ |B_loc/κ − (b^W + Δ_∞)/log L| + (C_ρ g_0² + |Δ_K − Δ_∞|)/log L ]·κ/B_loc,
  Δ_∞ := lim Δ_K. The first term is LCS-b at leading order (b^W + Δ_∞ is the bare running per step); the flow's error terms
  are ρ_0 and Δ_K − Δ_∞. The printed version with b_∞ and |b^{(K)}_0 − b_∞| is withdrawn (that difference does not vanish).
  The conclusion "right only given LCS-b; the trajectory's own errors then drop out" is unchanged.
- **E8 (§2.3, fourth bullet).** "Hence N5 holds iff ..." overstates: on this architecture N5 FOLLOWS from conditional
  transparency at scales comparable to ℓ_0, and the bound does not vanish without it (and the decoupled example fails
  N5); necessity in general is not proved.
- **E9 (§0.1 N5 last bullet).** "(N5-T*) at ROUGH coarse fields" should read "(N5-T*), together with N5-C's τ-factor at
  the top levels, at ROUGH coarse fields".
- **E10 (§3.3).** All observables in DIAG are the Z_e-normalized ones (Õ/Z_e), consistent with (A).
- **E11 (§1.9 last bullet; §1.7 "The traceless coupling-gradient term"; §3.2 row 13).** Read per E1: 𝔅_tl's coefficient
  is 2N(uϑ^p_R)′∂u — O(g²) under the analytic-in-u clause added to LCS-a, O(g⁴) in perturbation theory — and row 13's
  "B_loc, ϑ^p_1" reads "B_loc, κ". The qualitative findings (uncancellable by a scalar profile; present for pole rotations;
  omitted by SPHERE55; rate logarithmic in the separate-bounds bookkeeping) stand.

---

## 6. Verdicts on inherited claims touched by this file (REVIEW_BRIEF_55 order; refutations count as much as positives)

| # | Claim (file: locating string) | Verdict | Derivation / reason |
|---|---|---|---|
| H1 | SPHERE55 §1.1 "boosts: v_c(x) = R^2 c + 2(c.x) x - |x|^2 c", "div v_c = 8(c.x) = -4 v_c . grad log Omega", north field −v_c | **CONFIRMED** | sm55_1 C1, C3 (Dφ·v_c = −v_c∘φ identically), C5; agrees CODEX_REVIEW_SPHERE F5 |
| H2 | SPHERE55 §1.4 "du/dlog s = -2beta_0/(1 - beta_1/(beta_0 u))" and its expansion | **CONFIRMED** | sm55_1 C6 |
| H3 | SPHERE55 §3.4 T4 "delta S_cl = +(1/16) (dG^{-2}/dlog s) int (div v) F^a F^a" | **CONFIRMED** | §1.1 profile identity + classical variation (§1.3); agrees Codex F5 |
| H4 | SPHERE55 §3.4 T4 "c_4 proportional to (dG^{-2}/dlog s) - (dg^{-2}/dlog s)_exact" | **NOT-VERIFIED as stated** | the subtracted slope must be the LOCAL trace coefficient B_loc/κ (§1.3, E1); it equals the trajectory's step scaling only under LCS-b (§1.4), which is unproved |
| H5 | SPHERE55 §3.4 rows T2/T3 and §6 "holds for the rotation channel (SO(4)_poles ...)": on the PROFILED sphere the bulk breaking is dimension ≥ 6 | **REFUTED as complete** | §1.3 + E1: the translation channel carries 𝔅_tl = −2NΣχ(∂_μu)v^ν[(uϑ^p_3)′S^(3) + (uϑ^p_6′)′S^(6′)]_μν, dimension-4 operators with coefficient O(g²) (analytic bounds) / O(g⁴) (perturbative), nonzero for boosts AND pole rotations (weight ∝ u′(r)Sym(x⊗Jx) ≠ 0). Correction: rotation channel = dimension ≥ 6 (a²) + 𝔅_tl. Theorem 3.6's o(1) conclusion unaffected |
| H6 | SPHERE55 §3.4 "W0 (precise). sup_x |c_4(a; x)| -> 0" as the complete dilation-channel requirement | **REFUTED as complete** | it omits 𝔅_tl, which no scalar profile cancels. Correct W0: c_4·𝒲(F, Θ̂) → 0 AND (uϑ^p_R)′·sup|∇u||v|·𝒲(F, S^(R)) → 0 (§1.2, E5) |
| H7 | SPHERE55 §3.4 "UNIV55 wrote O(g_0(a)^2); with this profile the formal order is G^4" | **CONFIRMED as formal arithmetic; NOT-VERIFIED as a rate** | sm55_1 C7 (matched two coefficients ⇒ O(u⁻²)); no lane statement supplies the matching; G-pert needs the value of B_loc (X4); 𝔅_tl dominates anyway |
| H8 | SPHERE55 §3.5 "Lemma 3.5 (two-scale covariance bound)" | **CONFIRMED (inequality)** | law of total covariance + Cauchy–Schwarz; agree CODEX_REVIEW_SPHERE F6 (and E6's coefficient 1) |
| H9 | SPHERE55 §3.5 input "SRC-E (sphere): Var(F_s)/Z_e^4 bounded uniformly in a and s" | **NOT-VERIFIED (suspect); REPLACED** | Lemma V makes each factor's variance ~ a⁻⁴; falsity for the product needs a joint conditional-variance bound (agree ASSEMBLY55 F5). Not needed: Lemma 3.5′ + SRC-E′_∞ (§2.1; sm55_2) |
| H10 | SPHERE55 §5.4 "(U-mom) Position-uniform local moment bounds ... E|Phi(f)|^n <= A^n (n!)^b p(f)^n" | **REFUTED in scope** | at n = 2 it is a cutoff-uniform second moment of the smeared clover density; with a non-vacuous normalization and a polylog separated bound it contradicts Lemma V (CODEX_REVIEW_SRCCD §3 CONFIRMED that incompatibility). Correction: separated-point (^0𝒮) bounds U-sep (ASSEMBLY55 F5). CODEX_REVIEW_SPHERE F12 records NOT-VERIFIED/OPEN; consistent (it does not assume the separated upper bound) |
| H11 | SPHERE55 Theorem 3.6 (fixed-R restoration), as an implication | **CONFIRMED** for every F (proof is F-independent) with Lemma 3.5′ replacing Lemma 3.5; state-level symmetry needs the determining family (agree CODEX_REVIEW_SPHERE F7) |
| H12 | SPHERE55 §4.1 "Lemma 3.5 gives N5-cond ⇒ N5 with SRC-E. PROVEN-HERE (the implication)" | **CONFIRMED (implication); superseded** | valid given SRC-E; replaced by Theorem N5 (§2.5), which uses no fine moment |
| H13 | SPHERE55 §4.2 P1-P3, P4's factorization | **CONFIRMED** | P1 from χ-independence; P2 equivariance; P3 geometry; factorization exact; agree Codex "additional checks"; non-vanishing ARGUED (E3) |
| H14 | SPHERE55 §4.3 CS: θ_eq-even, excluded by θ_μ | **CONFIRMED** | re-derived (θ_μ reverses S³'s orientation; c(x) constant by small-gauge invariance); agree Codex F8 incl. its single-connection scope |
| H15 | SPHERE55 §4.4 item 1 "No jump mode survives the first RG step" | **REFUTED (literal)** | agree CODEX_REVIEW_SPHERE F9 (soft kernels have full support); replaced by §2.4's tree-level stiffness and RMS/mean counting |
| H16 | SPHERE55 §4.4 item 3 + E11 "(beta_cross/beta)(l/a)" criterion | **CONFIRMED (tree-level arithmetic)** | with Codex F2's weights: λ_seam ≥ (3/4)(β(2a)/β(a))(ℓ/a) → ∞ (§2.4); agree Codex F9 |
| H17 | SPHERE55 E10 power counting a²s⁻⁴, c_4s⁻², a s^{−7/2} and thresholds | **CONFIRMED (arithmetic)** | sm55_1 C9; agree Codex F6 (incl. s ∝ a^{1/2} ⇒ a^{−3/4}); with the coarse-image norm the thresholds become a^{2/15}, a^{1/4}, |c_4|^{1/6} |
| H18 | SPHERE55 §4.5 isolation N5-RG / N5-op / N5-CD | **CONFIRMED as an isolation; refined** | N5-CD alone does not give N5 (§2.3); the precise inputs are N5-T*, N5-C (§2.5) |
| H19 | SPHERE55 §1.3 "Crossing plaquette e x [0,1]: beta^ = (beta/4) k_e" | **REFUTED (agree Codex F2)** | incident-cell sums; bounds (3/4)β(2a) ≤ β̂_cross ≤ (3/2)β(a); used in §2.4 |
| H20 | SPHERE55 §6 "OS1 on this route is reduced to purely UV inputs" | **CONFIRMED in the operational sense** (Codex F11), with the corrected input list of §3.2 |
| H21 | UNIV55 §3.4 W0 "c_4 = O(g_0(a)^2) by P4's two-loop rule, if ... two-loop asymptotics" | **NOT-VERIFIED; refined** | G-pert needs the value of B_loc (sm55_1 X4); with the Ward profile c_4 ≡ 0 and the residual is 𝔅_tl |
| H22 | PANEL_P4 S4(a) "Gradient terms are irrelevant: pure YM has no gauge-invariant local operator of dimension < 4" | **CONFIRMED for the effective action; incomplete for the Ward identity** | no dimension ≤ 4 gradient term exists in S_eff; but the Ward functional's coupling-gradient terms are dimension 5 = 1 + 4 (marginal in the translation channel): the scalar one must be matched by the profile, the traceless one (𝔅_tl) is suppressed only by g^k |
| H23 | SRCCD55 Proposition B on the sphere chain | **CONFIRMED (applicability)** | needs only normalized nonnegative kernels: SPHERE55 §1.6 (B1); agree Codex SRCCD §1 |
| H24 | ASSEMBLY55 F5 (SRC-E, U-mom of the excluded type; repair by ‖E[F|W_s] − EF‖₂) | **CONFIRMED and implemented** | §2.1, sm55_2 |
| H25 | ASSEMBLY55 F14's proposed repair "(FLOW-pos) ... with a lower propagation bound" for W0 | **NOT NEEDED for W0** | W0 needs LCS-a, no propagation lower bound and no value (§1.5-§1.6); the variable-coefficient layer 1 remains needed |

## 7. Summary table of this file's own claims

| # | Claim | Status | Where |
|---|---|---|---|
| 1 | Chart algebra: div v_c, v·∇log Ω, conformal Killing form, north field −v_c, profile identity v·∇u = (div v/4)B_T | PROVEN-HERE (sm55_1 C1-C3, C5; controls fire) | §1.1 |
| 2 | Kink of the physical spacing; sign flip of the chart divergence at the seam | PROVEN-HERE (C4) | §1.1 |
| 3 | G-pert slope; its value-dependence; two-loop-model interpolation error O(u⁻²) | PROVEN-HERE (C6, C7/X4, C8) | §1.1, §1.6 |
| 4 | Exact linearity W = W^{(u_0)} + Ξ_v𝒮_η (profile = action-density source) | PROVEN-HERE | §1.3 |
| 5 | Dimension-4 content: one scalar coefficient c_4 = [B_loc − κB_T]/B_loc; traceless 𝔅_tl with coefficient (uϑ^p_R)′∂u; other gradient terms O(a²/R²); Hessian term O(a) | PROVEN-HERE as classification (E1-corrected); coefficients are inputs | §1.3, E1 |
| 6 | 𝔅_tl is uncancellable by a scalar profile and present for pole rotations | PROVEN-HERE (representation + explicit nonzero weight) | §1.3, E1 |
| 7 | Theorem W0 (Ward profile dT/dlog s = −B_loc/κ): c_4 ≡ 0, residual 𝔅_tl + O(a²𝔏) | CONDITIONAL on LCS-a (implication PROVEN-HERE) | §1.5, E1 |
| 8 | Trajectory profile needs LCS-b; explicit flow-error bound | PROVEN-HERE (decomposition; E7-corrected) | §1.6, E7 |
| 9 | G-pert needs the value of B_loc | PROVEN-HERE (C7, X4) | §1.6 |
| 10 | LCS not derivable from the trajectory's global properties without coarse decorrelation | ARGUED | §1.8 |
| 11 | Curvature effects at ℓ ≫ a are not in W; local Z_e normalization removes W3's scalar dilation defect | ARGUED | §1.7 |
| 12 | Lemma 3.5′ (coarse-image two-scale bound) | PROVEN-HERE (sm55_2 T2/T3, Y2) | §2.1 |
| 13 | SRC-E′_∞ replaces SRC-E and passes the nonvacuity test in an exact model | PROVEN-HERE (model) | §2.1 |
| 14 | E10's thresholds with the coarse-image norm: a^{2/15}, a^{1/4}, |c_4|^{1/6} | PROVEN-HERE (arithmetic given E10's counting) | §2.1 |
| 15 | Proposition B applies to the sphere chain | PROVEN-HERE (hypothesis check) | §2.2 |
| 16 | Conditional decay disposes of the fine levels but does not make the seam term vanish | PROVEN-HERE (structure) + exact witness (sm55_2 Y1, T4, K6) | §2.3, E8 |
| 17 | Slab operator content; θ = 1 (means), θ ≥ 1/2 (fluctuations) | ARGUED (power counting, tree level) | §2.4, E2, E3 |
| 18 | Tree-level stiffness with corrected weights λ_seam ≥ (3/4)(β(2a)/β(a))(ℓ/a) | PROVEN-HERE (arithmetic) | §2.4 |
| 19 | Theorem N5: |Cov(F, 𝔖)|/Z_e^q ≤ explicit sum ⇒ O((a/ℓ_0)^{min(θ,θ_*)}) | CONDITIONAL on N5-T*, N5-C, SRC-E′_∞ (implication PROVEN-HERE) | §2.5 |
| 20 | N5 rate O((a/ℓ_0)^{1/2}𝔏) | ARGUED (on top of 19) | §2.5 |
| 21 | No counterexample to N5 among nine candidates | ARGUED (list) | §2.6 (h withdrawn) |
| 22 | H_Euc (sphere) as an implication with inputs, owners, status | PROVEN-HERE as an assembly of cited implications | §3.1-§3.2 |
| 23 | DIAG | PROVEN-HERE (implication) | §3.3, E10 |
| 24 | ASSEMBLY55 F3 closed (Codex); F5 Lemma-3.5 part and F6 repaired; F4, F13, F14 (part), F5 U-mom part open | dispositions | §4 |
| 25 | Checks: sm55_1 9/9 PASS, 5/5 controls fired; sm55_2 8/8 PASS, 4/4 controls fired | PASS (criteria first; sm55_2's criteria erratum appended before its script) | checks/sm55_* |

**Counts (own claims):** PROVEN-HERE 15 (rows 1-6, 8, 9, 12-16, 18, 23; row 22 is an assembly), CONDITIONAL 2 (7, 19),
ARGUED 5 (10, 11, 17, 20, 21). **Inherited claims (§6):** CONFIRMED 15 (H1, H2, H3, H8, H11, H12, H13, H14, H16, H17,
H18, H20, H23, H24, plus H7's arithmetic), NOT-VERIFIED 4 (H4, H9, H21, H7's rate), REFUTED 5 (H5, H6, H10, H15, H19);
H22 split (CONFIRMED for the action, incomplete for the Ward identity); H25 "not needed".

## 8. Report to the lead (compact)

- **Model line:** claude-opus-5-5. Deliverable: this file; checks `checks/sm55_1_*` (chart algebra) and `checks/sm55_2_*`
  (two-scale bound / decay-vs-transparency model), both PASS with all controls firing, criteria written first.
- **W0 (owned here):** the profile enters the Ward functional exactly as an action-density source. Defining the profile by
  the local trace coefficient (dT/dlog s = −B_loc/κ, "Ward profile") cancels the scalar dilation term identically
  (Theorem W0, CONDITIONAL on one SRC-M-type matching clause LCS-a; owner SRC lane). The brief's trajectory profile works
  iff the lattice Callan–Symanzik consistency LCS-b holds; then the flow's error terms cancel and the value of b_∞ is not
  needed; P4's two-loop profile needs the value. The a⁻² mixing is not an obstruction (it is inside B_loc).
  **New:** an uncancellable traceless coupling-gradient term 𝔅_tl (coefficient (uϑ^p_R)′∂u: O(g²)/O(g⁴)) breaks the boost
  AND pole-rotation Ward identities on the profiled sphere; SPHERE55 omits it. It vanishes, so Theorem 3.6 survives, but
  the rate is logarithmic in the separate-bounds bookkeeping.
- **N5 (owned here):** Theorem N5 (CONDITIONAL; implication PROVEN): |Cov(F, 𝔖)| = O((a/ℓ_0)^{1/2}𝔏) at fixed R from
  N5-T* (transparency of the seam flux's coarse image, every coarse field), N5-C (one-step decay with transparency-
  weighted sizes, intermediate large fields included) and SRC-E′_∞. **Answer to the brief: decay at the soft-constraint
  mass, in lattice units, kills only the fine levels (super-exponentially); the top levels (factor e^{−m d_0/2ℓ_0}) and the
  coarse term do not decay, so the seam vanishes only through transparency of its coarse images** (exact model:
  perfect decay, covariance 70/27). Slab content: dimension ≥ 4 defect operators (CS excluded by θ_μ, FF̃ by θ_eq) ⇒ θ = 1
  for means; the two-sided mode's tree-level RMS gives θ ≥ 1/2. No counterexample; the open heart is N5-T* at rough
  coarse fields.
- **Assembly:** H_Euc (sphere) ⟸ W0 (LCS-a) + W1 + W3 (sup-V) + N5 (N5-T*, N5-C) + SRC-E′_∞ for a determining ^0𝒮 family
  + L1-sphere + U-sep + U-alg + DIAG (PROVEN-HERE). No non-UV input; the only IR item in any reading is the flat-selection
  identification (strict reading of T_OS only).
- **REFUTED items with corrections:** (H5) "rotation-channel breaking is dimension ≥ 6" on the profiled sphere → add 𝔅_tl;
  (H6) "W0 = sup|c_4| → 0" → add the 𝔅_tl condition; (H10) U-mom → U-sep (agree ASSEMBLY55 F5); (H15) "no jump mode
  survives the first step" → tree-level suppression only (agree Codex F9); (H19) (β/4)k_e → incident-cell sums (agree
  Codex F2).
- **For PROOF.md / HANDOFF (sphere-route row):** nothing moves to PROVEN. Pending-Codex new items: Lemma 3.5′, Theorem W0,
  Theorem N5, DIAG, 𝔅_tl, "decay ⇏ N5". Replace "construction + seam + UV items open" by: θ_μ RP banked (Codex F4);
  open = LCS-a (new SRC-M clause (M-d) + derivative bound on uϑ^p_R), W1/W3/N5-C/SRC-E′_∞ for all q (SRC lane), N5-T*
  (seam RG, unassigned), L1-sphere (variable coefficients on K_a), U-sep. Remove SRC-E and U-mom from the sphere input list.
  The trajectory-profile variant adds LCS-b; P4's profile adds the value problem.
- **Codex verdicts used:** CODEX_REVIEW_SPHERE F1, F2, F4-F12, F14, F15 — all AGREE; CODEX_REVIEW_SRCCD §1, §3 — AGREE;
  CODEX_REVIEW_P4 §1.1, §1.2, §2.3, §4.1-§4.3 — AGREE; CODEX_REVIEW_UNIV §7, §8, §11 — AGREE; CODEX_REVIEW_SRCAN item
  3/6 — AGREE (W0 needs only the upper propagation bound). CODEX_REVIEW_UIR is unfinished (R1-R3 read, not used).

## 9. Late erratum (append-only)
- **E12 (§1.3 "It is present for rotations", §6 H5, §7 row 6).** What is PROVEN is that the traceless coupling-gradient
  STRUCTURE is allowed by every symmetry of the regulator (H(4), θ_eq, θ_μ, gauge invariance) and has a nonzero geometric
  weight for boosts and pole rotations; its COEFFICIENT 2N(uϑ^p_R)′ is generically nonzero (two loops) but not computed
  here. H5's verdict is therefore "REFUTED as a classification" (SPHERE55's list of the bulk breaking's operator content
  omits an allowed dimension-4 structure); whether the coefficient vanishes is part of LCS-a.

End of SEAM55 (worker claude-opus-5-5), 2026-10-29 ≈05:00 UTC.
