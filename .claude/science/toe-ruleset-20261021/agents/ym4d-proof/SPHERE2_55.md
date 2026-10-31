Reviewer model: claude-opus-5-5

# SPHERE2_55 — the sphere route's two unassigned inputs: the trace-channel matching (LCS-a) and the seam at rough coarse fields (N5-T*)

Worker: Opus 5.5 (model ID above, verbatim from the system prompt). Scope: write only this file and `checks/s2_55_*`.
No git. Append-only after this header block. Brief: `scratchpad/queue/sphere2.md`; shared rules: `REVIEW_BRIEF_55.md`
(re-read after its 2026-10-29 output-size amendment; this file is appended section by section).

## PRE-STATED (written before any derivation; UTC 2026-10-29T05:3x, clock read by `date -u` in the same command)

Read before this block: SEAM55.md (all 715 lines, incl. errata E1-E12), CODEX_REVIEW_SEAM.md (all 238 lines; complete,
ends with "Exactly what may be banked"), SPHERE55.md (all 865 lines), CODEX_REVIEW_SPHERE.md (all 337 lines; complete),
SRCAN55.md §0-§4 (Proposition SA-K, Lemmas SA-J, SA-F, SA-CF, SA-TC, SA-TI, §4 list), CODEX_REVIEW_SRCAN.md (all 339 lines;
complete), UNIV55.md §1-§3.4 (Proposition T, Theorem U, the Ward architecture), SRCCD55.md §3, §5, §6, PROOF.md
[S26-BANKED] block (lines 5-48 at read time, located by the string "[S26-BANKED]"), HANDOFF.md, PLAN_S26.md §13-§15.
Nothing derived yet.

**Targets.**

P1 (LCS-a, statement). Write LCS-a as one precise clause: which coefficient (the s̄-coefficient B_loc(u) of the trace
density D of the constant-coupling Ward functional, and the action-source mixings ϑ^p_R(u) with κ_W = d[u(1+ϑ^p_1)]/du),
in which norm (tilted conditional one-point functions / conditional cumulants with separated e-insertions and coarse
images, with SRC-κ weights), uniformly over which coupling fields and which coarse fields (all V, large ones with the
SRC-κ-LF discount), and with which remainder size. Separate (a) the constant-coupling matching content, (b) the regularity
in u that the Ward-profile ODE and the traceless term need, (c) the variable-coefficient (coupling-locality) content.

P2 (LCS-a, the suggested proof route). Decide whether SA-K (complex position-dependent couplings, tree level, holomorphic)
plus Cauchy in the coupling field can identify B_loc "as the derivative of the effective action w.r.t. a local
log-scale/coupling change". If yes: prove it, with every consumed input named. If no: exhibit exactly which step fails
(a concrete computation or counterexample), and give the strongest correct replacement.

P3 (LCS-a, reductions). Prove as implications whatever parts of LCS-a follow from named inputs: (b) from complex-sector
bounds by Cauchy (including global existence of the Ward-profile ODE solution on the whole interval [a, 2a], the gap
CODEX_REVIEW_SEAM F4 named); (c) from constant-coupling matching plus conditional decay at real variable couplings;
and name, for (a), what it consumes among (F_R)/(UIR^♮)/(ρ-null), per-step N5/N6, large fields.

P4 (the product condition). State exactly what "the actual normalised insertion products vanish uniformly along each
path" (CODEX_REVIEW_SEAM F5 / banked item 2) requires for W0's residual channels (scalar remainder incl. contacts;
traceless 𝔅_tl), i.e. what W1 must supply, with the logarithmic bookkeeping explicit.

P5 (N5-T*). Classify the seam-localised local operators that can carry Killing flux, including those SEAM55 did not list
(normal-derivative structures, the profile kink, the incident-cell weight non-uniformity, the two-sided mode at the glued
point, orientation-dependent coefficients of the staircase), decide for each dimension ≤ 4 operator whether its
coefficient is nonzero and whether it must be tuned; then either prove N5-T* for every coarse field from named inputs
(with the large-field input named) or isolate the obstruction exactly.

P6 (assembly). H_Euc on the sphere route with every input named and its status after this file.

**What would count as a refutation (of a step, of the suggested route, or of an inherited claim).**

Q1. A load-bearing quantity in the trace channel that SA-K's tree-level object cannot see: e.g. the trace coefficient's
tree-level (background-evaluated) value differs from the coefficient the Ward profile needs by an amount that does not
vanish as a → 0. That would refute "SA-K + Cauchy identifies B_loc".
Q2. An exact example in which analyticity in the coupling with uniform bounds holds and the matching remainder does not
vanish (or a matching coefficient is not determined), refuting "Cauchy ⇒ matching".
Q3. A gauge-invariant seam operator of dimension ≤ 3 allowed by the regulator's exact symmetries (H(4) × <θ_eq>,
gauge invariance), or a dimension-4 seam operator whose coefficient is O(1) rather than O(a) (e.g. through mixing with a
lower-dimension seam operator), that carries Killing flux: either would force tuning or refute transparency.
Q4. An admissible coarse field V for which E[𝔖|V] provably does not tend to 0, or a proof that N5-T* cannot hold
uniformly over all V for this seam construction (e.g. a kernel-induced obstruction at short coarse crossing chords).
Q5. A CONFIRMED/PROVEN/banked statement of SEAM55, SPHERE55, SRCAN55 or their Codex reviews contradicted on a
load-bearing step by my derivation: I will state the correction and its derivation.

Labels: PROVEN-HERE (complete argument written here) / CONDITIONAL (implication proven here, inputs named) / ARGUED
(stated gap) / NOT-VERIFIED / REFUTED. [m] = literature from memory, never load-bearing. Check ids: `s2_55_*`.

---
**Clock correction (appended at once, before any derivation).** The PRE-STATED heading's "T05:3x" is wrong: the
`date -u` run in the same command that wrote the block printed **2026-10-29T05:47:48Z** (before and after the write).
That is the time of the PRE-STATED block.

# FINDINGS (appended from 2026-10-29T06:2x UTC, after the PRE-STATED block, three criteria files and three checks)

## 0. Inputs read (as on disk), Codex verdicts used, symbols

- Read in full after the PRE-STATED block: ROTDEF.md §2-§4 (the definition of Ξ_v: "𝔣^ν_b := (2a²)⁻¹[π(P^{+ν}_b) −
  π(P^{−ν}_b)]", "ξ_b(v) := −a Σ_{ν≠μ} v^ν(m_b) 𝔣^ν_b", "Ξ_v := ½(Ξ^left_v + Ξ^right_v)", property (C)); SRCCD55.md §3
  (SRC-κ, SRC-M (M-a)-(M-c), SRC-poly), §5.0-§5.4, §6 (M1)-(M7); UIR55.md §3.5-§3.6 ((ρ-null), Theorem UIR-T, Corollary
  b_∞); PROOF.md "Decision 4 is MADE" (located by string; line 604 at read time) and the κ_- ≤ κ_i ≤ κ_+ quantifier.
  The queue file of the SRC2_55 worker (running) was read only to avoid overlap; nothing of SRC2_55 is used.
- **Codex verdicts used, with my agreement (each argument read):**
  - CODEX_REVIEW_SEAM (complete; ends with "Exactly what may be banked"): F1 (Lemma 3.5′ + model) AGREE; F2 (multilevel
    N5 sum; decay ⇏ transparency) AGREE, re-derived (Markov reverse property) and re-checked on exact chains (s2_55_2 G2);
    F3 (exponent 1/2 not a consequence; counterexample Cov = 1/(k+1) at a_k/ℓ_0 = 3^{−2k}) AGREE (re-derived); F4 (E1
    algebra, κ_W, scalar c_4 = 0, tensor structure, analytic O(g²)/formal O(g⁴), domain-margin gap) AGREE, and §1.5 below
    closes its domain-margin gap given sector analyticity; F5 (product condition; "iff" false; exact product −1) AGREE
    (re-derived); F6 (relative-o(1) LCS-b gives c_4 = 1/(u+2)) AGREE (re-derived: (1/u)/(1+2/u) = 1/(u+2)); F7 (slab
    parity PROVEN, exponents ARGUED) AGREE; F8 (DIAG needs the Cartesian product, paired H1 insufficient; counterexample
    Φ(z) = Xz_1) AGREE; F9 (separated products do not determine the full algebra) AGREE; F10 (H5, H6, H15, H19 survive;
    H10 NOT-VERIFIED on K_a) AGREE; F11, F12 AGREE (I use Codex's κ_W / κ_flow / κ_K and h_i notation below).
  - CODEX_REVIEW_SPHERE (complete): F1, F2 (crossing weights ¼Σ_cβ_c), F4 (five RP planes), F5, F6, F8 (CS), F9 (no
    finite-step jump elimination), F11 (all-coarse-field architecture; interpolation existential), F14, F15 (no lower
    physical chord length) — AGREE.
  - CODEX_REVIEW_SRCAN (complete): items 1-4 (SA-CF, SA-PC/TC, SA-F upper bound only, SA-K CONDITIONAL tree-level
    theorem in the sup-plus-Wilson-Hölder class on 𝒞_glob), 6, 7 AGREE; item 3's refutation of the positive lower
    propagation bound AGREE (I use no lower bound).
- **Symbols (defect 1; collisions resolved here, overriding any other file's usage inside this file).**
  - u := 1/g² ("u-units"); plaquette weights β_p = 2N u(p); S_u := Σ_p 2N u(p) s(U_p), s(U) := 1 − N⁻¹ Re tr U.
    (ROTDEF and SRCAN55 write the action as u_0 Σ_p s(U_p) with "u_0 = 1/g_bare²" and "the factor N absorbed"; their u_0 is
    not my u. No comparison below uses theirs.)
  - C_F := (N² − 1)/(2N) (Casimir of the fundamental for tr(T^aT^b) = δ^{ab}/2); β_0 := 11N/(48π²), so the one-loop running
    in u-units is du/dlog μ = 2β_0 = 11N/(24π²) (UIR55's β_0^std = 11N²/(12π²) is the same running in β-units: 2N·2β_0).
  - κ_W(u) := d[u(1 + ϑ^p_1(u))]/du (SEAM55 E1's κ); κ_flow (PROOF E7 contraction exponent) and κ_K (soft-kernel
    strength, Decision 4: k_c ∝ exp(−(κ_K/g_j²)[1 − N⁻¹Re tr(V_c⁻¹M̄_c)])) are different objects (Codex SEAM F12).
  - B_loc(u): the s̄-coefficient of the trace density D of the constant-coupling Ward functional (SEAM55 LCS-a (i));
    m̃: the measure term's share of it; B^fl := B_loc − m̃ (the action part's share). B_T := −T′ (profile slope).
  - Levels: i = 0 (fine) … n (reference); chart spacing h_i := aL^i, h_n = ℓ_0 (Codex SEAM F12's repair of "ℓ_i"). U_i is the
    level-i field, V := U_n. J_t ∈ ℕ is a NUMBER OF TOP LEVELS (§2.3), never a rotation generator or an insertion.
  - 𝔖 := SPHERE55's seam term −T_χ (never the action). I_i(U_i) := E[𝔖 | U_i] (the seam flux's level-i image).
  - Ξ′_λ: the λ-family of lattice Lie derivatives of §1.3 (λ ∈ ℝ a scheme parameter; not the stiffness λ_seam of SEAM55
    §2.4, not a flow derivative).
  - "dimension" of a seam operator: canonical mass dimension of the local operator integrated over the 3-dimensional seam;
    marginal on the seam = 3 (not 4).

## 0.1 Result in one page (derivations in §1-§3)

**LCS-a.**
- **PROVEN-HERE (exact, all configurations; s2_55_1 C1-C4 + s2_55_1b):** for ROTDEF's Ξ_v and every v quadratic in the chart
  coordinates, **div Ξ_v = −N C_F Σ_p (∂_μv^μ + ∂_νv^ν)(c_p) s(U_p)** (p in the (μ,ν)-plane, c_p its centre). For the
  conformal Killing fields of the chart this is **−div Ξ_v = 2N C_F Σ_p (div v/4)(c_p) s(U_p)**: the measure term of the Ward
  functional is EXACTLY an action-density source of strength C_F (zero for rotations), with no c-number part and no
  higher-dimension remainder.
- **Consequences (PROVEN-HERE as bookkeeping):** B_loc = C_F + u(ϑ^p_D − 4ϑ^p_1), and LCS-a (i) is implied by LCS-a (ii)
  extended by the trace component ϑ^p_D. **LCS-a is ONE SRC-M-type clause**: the matching of the lattice Lie derivative of the
  plaquette action density (vector part ϑ^p_{1,3,6′}, trace part ϑ^p_D), in tilted conditional form, for every coarse field.
- **The suggested route (SA-K + Cauchy identifies B_loc) does not deliver LCS-a's content.** SA-K is a tree-level theorem; at
  tree level the trace coefficient is exactly m̃ = C_F (the measure term; the action part is classically scale invariant).
  It is scheme dependent: for the admissible family Ξ′_λ (same (Lin), (G), (Loc), (H), (C) as ROTDEF's Ξ) the tree value is
  C_F − λ/N (s2_55_1 C5), i.e. **every real number**. The Ward-profile coefficient B_loc/κ_W is scheme independent given the
  Ward inputs for two schemes and a nonvacuous dilation insertion (implication PROVEN-HERE). So tree-level analyticity is
  right for at most one scheme and cannot identify it; under the expected one-loop asymptotics B_loc/κ_W → 2β_0 it is off
  by the factor C_F/(2β_0) = 12π²(N² − 1)/(11N²) ∈ (8.07, 10.77) (s2_55_1 C6). The one-loop fluctuation part is O(1).
  "The derivative of the effective action w.r.t. a local log-scale change" exists on the sphere chart only through the
  profile rule and equals −B_T × (s̄-image): it reproduces the profile's slope, not the Ward coefficient.
- **What Cauchy does give (PROVEN-HERE as implications):** (b) sector analyticity of B_loc and uϑ^p_R with uniform bounds ⇒
  all regularity LCS-a needs: |(uϑ^p_R)′| = O(g²), κ_W ≥ ½, B_loc/κ_W bounded Lipschitz, the Ward-profile ODE solvable on the
  WHOLE interval [log a, log 2a] inside the weak-coupling domain, and the profile inside SA-K's coefficient class (closes
  CODEX_REVIEW_SEAM F4's domain-margin gap, given the hypothesis); (c) the variable-coefficient (coupling-locality) content
  follows from the TILTED form of the constant-coupling clause, with no further input.
- **What (a) consumes (named):** the source-inserted RG with the Lie-derivative insertion (SRC-poly with linear insertions,
  i.e. per-step N5 linear covariance, N6, Theorem CE), a localisation of the marginal component per level (SRCCD55 (M4)),
  (F_R) in analytic form (Flow-an), which reduces through (UIR^♮) to (TC-b)_𝔍 + (ρ-null) (banked implications, inputs open),
  and per-step large fields conditional on the coarse field (RLF^η / SRC-κ-LF). **Not consumed:** the value b_∞, LCS-b, any
  one-loop number. Status: OPEN.
- **The product condition (P4):** scalar channel — the remainder's contact coefficient must vanish (O(g²) suffices, or it is
  absorbed in the local observable normalisation); traceless channel — W1 must bound the integrated S^(3,6′) insertion by
  o(log(ℓ_0/a)) (o(log²) under formal O(g⁴)), uniformly along the path; generic polylog SRC-κ weights do not suffice.

**N5-T*.**
- **Classification (PROVEN as symmetry/dimension; tree coefficients ARGUED):** no seam operator of dimension ≤ 3 survives
  (identity: c-number; CS: θ_μ; nothing else exists); the two-sided (gluing) operator has dimension 2 and a POSITIVE
  relevant coefficient ∝ β̂_cross/a (it drives to the glued, transparent defect; no tuning); dimension-4 seam operators
  (tangential and normal-tangential tr F², staircase-dependent anisotropic coefficients) DO have nonzero tree-level
  coefficients O(a·u) from the incident-cell weights, and need NO tuning: on a 3-dimensional defect dimension 4 is
  irrelevant (coefficient of mass dimension −1). The brief's suspected marginal dimension-4 seam operator does not exist.
- **Tower lemma (PROVEN-HERE; s2_55_2):** sup_V |E[X|V] − c| ≤ sup_{U_i} |E[X|U_i] − c| for every level i ≤ n. The
  conditional law of the top levels never enters an all-coarse-field conditional-mean clause.
- **Theorem N5′ (CONDITIONAL; implication PROVEN-HERE; s2_55_2):** N5 (qualitative o(1)) follows from (T-all)_J [N5-T*
  stated at the finer fixed scale ℓ_0L^{−J}, every J], (E′_J) [F's coarse image at level n − J bounded, every J] and (D)
  [pure one-step conditional decay below level n − J, no transparency weighting]. The top J levels contribute only through
  products of image oscillations, so neither decay nor "transparency-weighted fluctuation sizes" is needed there.
- **N5-T* itself: NOT proved; isolated.** Its content at any level is: small-field seam RG (irrelevance + gluing), the
  moderate-curvature levels below arbitrary coarse data (UNIV55's (N3), shared with the bulk), and the fate of wild
  coarse crossing data (ARGUED: absorbed by the soft kernel at finite cost rather than opening the seam; a design check on
  κ_K for seam links). No counterexample; no tuning obstruction.

**Assembly (§3):** H_Euc (sphere) ⟸ the banked construction/RP/Ward algebra + W0 (Ward profile ⟸ LCS-a = one SRC-M
clause) + W1 (with the product requirement) + W3 + N5 (Theorem N5′ or SEAM55's Theorem N5) + L1-sphere + U-sep + U-alg +
DIAG (Cartesian-product form) + a positivity/contact bridge from separated products to the full OS algebra (Codex SEAM F9,
the most dangerous). Nothing moves to PROVEN at the level of the YM inputs.

---

## 1. LCS-a — the trace-channel matching

### 1.1 Proposition M (the measure term is exactly an action-density source). PROVEN-HERE; s2_55_1 C1-C4, s2_55_1b
**Statement.** For ROTDEF §3.2's lattice Lie derivative Ξ_v = ½(Ξ^left_v + Ξ^right_v) on SU(N) lattice gauge fields, for every
configuration and every vector field v read at link midpoints:
  (D-link) div Ξ^left_b = div Ξ^right_b = (N C_F/a) Σ_{ν≠μ(b)} v^ν(m_b) [s(P^{+ν}_b) − s(P^{−ν}_b)];
  (D-plaq) div Ξ_v = (N C_F/a) Σ_p s(U_p)[v^ν(m_bot) − v^ν(m_top) + v^μ(m_left) − v^μ(m_right)]  (p in the (μ,ν) plane;
           bottom/top the two μ-links, left/right the two ν-links of p);
  (D-quad) if v is at most quadratic in x: **div Ξ_v = −N C_F Σ_p (∂_μv^μ + ∂_νv^ν)(c_p) s(U_p)** (no sums inside; c_p the
           centre of p); for the conformal Killing fields of the chart (∂_μv^μ = div v/4 for every μ):
  **−div Ξ_v = 2N C_F Σ_p (div v/4)(c_p) s(U_p)**, and it vanishes identically for rotations.
**Proof.**
1. *Casimir contraction.* For an orthonormal basis {T_α} of su(N) w.r.t. ⟨X, Y⟩ := −c tr(XY), completeness reads
   Σ_α (T_α)_{ab}(T_α)_{cd} = −(1/c)(δ_ad δ_cb − δ_ab δ_cd/N). With π(M) = (M − M†)/2 − tr(M − M†)/(2N)·1, T_α† = −T_α and
   tr T_α = 0: Σ_α tr(T_α π(T_α M)) = ½Σ_α[tr(T_αT_αM) + tr(T_α M† T_α)] = −(1/c)(N − 1/N) Re tr M, for every N×N matrix M
   (s2_55_1 C1, symbolic M, N = 2, 3; control X1: the Hermitian-part projection fails).
2. *Left half.* ξ^α_b = ⟨T_α, ξ_b⟩. Both plaquettes P^{±ν}_b are based at the start of b and begin with U_b, so the left
   derivative along U_b → e^{tT_α}U_b gives ∂^α_b π(P^{±ν}_b) = π(T_αP^{±ν}_b). Hence
   div Ξ^left_b = Σ_α ∂^α_b ξ^α_b = (c/2a) Σ_ν v^ν Σ_α[tr(T_απ(T_αP^{+ν})) − tr(T_απ(T_αP^{−ν}))]
   = −((N − 1/N)/2a) Σ_ν v^ν[Re tr P^{+ν} − Re tr P^{−ν}] = (N C_F/a) Σ_ν v^ν[s(P^{+ν}) − s(P^{−ν})], using Re tr P = N(1 − s(P))
   and N(N − 1/N)/2 = N C_F. The c's cancel: the result is basis independent, as a divergence must be.
3. *Right half.* Its plaquettes Q^{±ν}_b = U_b⁻¹(W^{±ν}_b)⁻¹ (P^{±ν}_b = U_bW^{±ν}_b) are the same plaquettes based at the far end,
   reversed: Q = U_b⁻¹P⁻¹U_b, so Re tr Q^{±ν} = Re tr P^{±ν}. Under U_b → U_be^{tT}: Q → e^{−tT}Q. ROTDEF's (C) fixes the sign
   of the right generator (both halves must generate the same first-order variation): ξ̃_b = −a Σ_ν v^ν·(−(2a²)⁻¹)[π(Q^{+ν}) −
   π(Q^{−ν})] (s2_55_1b D1; with the opposite sign the halves differ at first order, control D1x, and their divergences
   would cancel — s2_55_1 X2). The same Casimir computation gives div Ξ^right_b = div Ξ^left_b (s2_55_1 C2, four exact SU(2)
   data sets).
4. *Collection.* Each plaquette p of the (μ,ν) plane is P^{+ν} of its bottom μ-link, P^{−ν} of its top μ-link, P^{+μ} of its
   left ν-link and P^{−μ} of its right ν-link; summing (D-link) over b and regrouping by p gives (D-plaq) exactly
   (s2_55_1 C4: whole 3×3 SU(2) torus, arbitrary rational midpoint values, LHS by direct differentiation = RHS =
   110845769233/30661230600; control X4 fires).
5. *Quadratic collapse.* m_bot,top = c_p ∓ (a/2)ν̂ and m_left,right = c_p ∓ (a/2)μ̂; for v at most quadratic the odd part of
   v(c_p + h) − v(c_p − h) is exactly 2h·∇v(c_p), so the bracket is −a(∂_νv^ν + ∂_μv^μ)(c_p) (s2_55_1 C3 for the boost
   v_c; for v_c, ∂_μv^μ = 2c·x = div v_c/4 for each μ; control X3: a non-conformal quadratic field breaks the collapse). ∎
**Scope.** On the sphere the cut-off field χv is quadratic only where χ = 1; plaquettes meeting the transition shells
carry the lattice divergence of χv, a seam-layer term of SPHERE55's split (harmless for separated observables; it belongs
to B or 𝔖 according to the chosen current, SPHERE55 §4.2 P1). Inside the χ = 1 region the identity is exact.
**What it says.** The Jacobian of the lattice dilation is a pure action-density source with strength C_F per unit of
div v/4: it has no c-number part (it vanishes at s ≡ 0) and no higher-dimension remainder, at every configuration. SEAM55
§1.7's "measure term ... its dimension-4 part is part of B_loc (the O(g²)-relative, one-loop-type piece)" is CONFIRMED and
sharpened: all of it is dimension-4-type, and its coefficient is exactly m̃ = C_F.

### 1.2 Consequence: B_loc = C_F + u(ϑ^p_D − 4ϑ^p_1), and LCS-a is one SRC-M clause. PROVEN-HERE (bookkeeping)
The constant-coupling Ward functional is W^{(u)}(v) = Σ_p 2Nu Ξ_v s(U_p) − div Ξ_v. Expand Ξ_v s_p at m_p as in SEAM55 §1.3
(exact for quadratic v): Ξ_v s_p = v^ν τ^p_ν + ∂_μv^ν τ^p_μν + ½∂_μ∂_ρv^ν τ^p_μρν. Suppose (the matching statement)
  τ^p_ν = (1 + ϑ^p_1)∇̄_ν s̄ + ϑ^p_3 ∇̄_ν S^(3)_νν + ϑ^p_6′ ∇̄_μ S^(6′)_μν + ρ^τ_ν,   τ^p_μμ = (4 + ϑ^p_D) s̄ + c^p + ρ^D,
with A-valued and dimension ≥ 6 remainders. Summation by parts of the translation part (SEAM55 §1.3 with E1; Codex SEAM F4)
and Proposition M give the scalar dilation content of the PROFILED Ward functional as
  Σ_x a⁴ (div v/4)·2N [C_F + u(ϑ^p_D − 4ϑ^p_1) − κ_W(u) B_T] s̄ + (c-number) + remainders,
so **B_loc(u) = C_F + u(ϑ^p_D − 4ϑ^p_1)** exactly in terms of the source-variation coefficients; the measure part needs no
matching at all. Hence SEAM55's LCS-a (i) (a "NEW SRC-M clause (M-d)") is not an independent clause: it is implied by LCS-a
(ii) extended by the trace component ϑ^p_D of the same object. The Ward profile is
  **−T′(log s) = [C_F + T(ϑ^p_D − 4ϑ^p_1)(T)] / [1 + (Tϑ^p_1)′(T)]**.

### 1.3 LCS-a, stated exactly (target P1)
**(LCS-a).** Let 𝔟(a) := [u_traj(a) − M_u, u_traj(a) + M_u] (a fixed band M_u ≥ the profile span, §1.5) and the complex
sector Σ(a) := {z : |z − u| ≤ ρu for some u ∈ 𝔟(a)}, ρ ∈ (0, ½]. For the flat hypercubic Wilson lattice with constant bare
coupling z ∈ Σ(a), tilted by every source η of SRC's polydisc 𝒫 (‖η‖_∞ ≤ r_src, Wilson-Hölder class of SA-K; r_src at least
the profile span 2N·sup|B_loc/κ_W|·log 2), for every reference-level coarse field V (large V with SRC-κ-LF's path-sum
discount), every site x and every quadratic v:
- (L-a) the lattice Lie derivative of the plaquette action density has the matched expansion above, with coefficient
  functions ϑ^p_1, ϑ^p_3, ϑ^p_6′, ϑ^p_D of z only (and N, L, κ_K-range), holomorphic on Σ(a), |zϑ^p_R(z)| + |zϑ^p_D(z)| ≤ M
  uniformly in a;
- (L-b) every remainder (ρ^τ, ρ^D, the A-valued part, dimension ≥ 6) has tilted conditional cumulants with separated
  e-insertions (mutual distances ≥ δ_c) bounded by a²𝔏(a) × SRC-κ's weights (path sums for large V), and coarse images
  E[ρ(x)|V] − c bounded by a²𝔏(a)·C ℓ_0^{−6} for every V;
- (L-c) contact clause (as SRC-M (M-b)): within δ_c of an observable point y the remainders' contact with e_a(y) is
  c_con(z)·(H(4)-allowed contact structure at y) + (a²𝔏 × weights), with |c_con| ≤ C|z|⁻¹.
Output quantities: B_loc := C_F + z(ϑ^p_D − 4ϑ^p_1), κ_W := 1 + (zϑ^p_1)′, traceless coefficients (zϑ^p_R)′, R ∈ {3, 6′}.
**Which coefficient, which norm, which fields:** the coefficient of s̄ in the trace channel (equivalently ϑ^p_D and ϑ^p_1),
in the norm of tilted conditional cumulants and coarse images with SRC-κ weights × a²𝔏, uniformly over all coarse fields
(LF discount), all sources of the polydisc and the complex sector; no fine-field moment anywhere (it passes
CODEX_REVIEW_SPHERE F12's nonvacuity test for the same reason SEAM55's version did). This is SRCCD55's (M-a) for the plaquette
density s_p instead of the clover e_a, plus the trace component that rotations never needed.

### 1.4 The suggested route: SA-K + Cauchy cannot identify B_loc (target P2). Obstruction exhibited
**(a) The tree-level value is exactly C_F. PROVEN-HERE.** SA-K (CODEX_REVIEW_SRCAN item 4) controls the tree-level critical
point U^bg(V) and critical value of the composite with complex position-dependent coefficients. The tree-level coarse image
of the trace density is D(U^bg) = [action part on U^bg] + [measure part on U^bg]. The action part is classically scale
invariant: for smooth fields Σ_p 2NuΞ_vs_p = 2Nu∫[v·∂s̄ + (div v)s̄] + O(a²) = O(a²) for conformal v (the "4" of τ^p_μμ cancels
the "4" from summing (1 + 0)v·∇s̄ by parts; SEAM55 §1.3, CODEX_REVIEW_SPHERE F5). The measure part is exactly 2N C_F(div v/4)s̄
(Proposition M). So **B^tree = C_F**, and SA-K + Cauchy in the coupling field can only reproduce this number.
**(b) The tree-level value is scheme dependent, over all of ℝ. PROVEN-HERE (leading order; s2_55_1 C5).** Let Ξ′_λ replace
𝔣^ν_b by w^ν_b𝔣^ν_b with w^ν_b := 1 + λ[s(P^{+ν}_b) + s(P^{−ν}_b)] (the same w in both halves; s(Q^±) = s(P^±)). Ξ′_λ keeps
ROTDEF's (Lin), (G), (Loc), (H)/(T) (w is gauge invariant, local, symmetric under P^{+ν} ↔ P^{−ν}) and (C) (w = 1 + O(a⁴)).
Its divergence acquires Σ_ν(−av^ν)E^ν_b, E^ν_b := Σ_α𝔣^{ν,α}∂^α_b w^ν_b = −(λ/N)Re tr(𝔣^ν(P^{+ν} + P^{−ν})), and
E^ν_b = (λ/a²)[s(P^{+ν}) − s(P^{−ν})] + O(F⁴a⁶)/a² (exact through third order in the field, s2_55_1 C5; control X5). The
collection of §1.1 then gives −div Ξ′_λ = 2N(C_F − λ/N)Σ_p(div v/4)(c_p)s(U_p) + (classically O(a²)), while Ξ′_λS = ΞS +
O(a⁴)·ΞS classically. So **m̃(Ξ′_λ) = B^tree(Ξ′_λ) = C_F − λ/N**: 0 at λ = (N² − 1)/2, and any prescribed real value for a
suitable λ.
**(c) The Ward-profile coefficient is scheme independent. CONDITIONAL; implication PROVEN-HERE.** Exactly, for two admissible
schemes on the same profiled sphere theory, Cov(F, W′(v,χ) − W(v,χ)) = ω((Ξ′_{v,χ} − Ξ_{v,χ})F) (each Ward identity, subtracted).
Assume LCS-a for both schemes (coefficients (B, κ), (B′, κ′)), W1-type vanishing of every other channel of both, and
ω((Ξ′ − Ξ)F_s)/Z_e^q → 0 uniformly in s (a W3-type input: (Ξ′_λ − Ξ) carries the factor λ[s(P^+) + s(P^-)] at the observable's
links). Then for the profile T of either scheme, the scalar-channel mismatch insertion
Cov(F, Σ_x a⁴χ(div v/4)·2N[(B′ − κ′B_T) − (B − κB_T)](u(x)) s̄(x))/Z_e^q → 0. If the dilation insertion is nonvacuous (for some
F of the family and some boost, Cov(F, Σ_x a⁴χ(div v/4)w(x)·2N s̄(x))/Z_e^q stays bounded away from 0 for weights w bounded
away from 0 on the cap — the theory's local Λ responds to a local coupling change), then the Ward profile of one scheme is
asymptotically the Ward profile of the other: B′/κ′ − B/κ → 0 on the band. ∎
**(d) Conclusion.** By (b) the tree-level coefficients of Ξ and Ξ′_λ differ by λ/N; by (c) their Ward coefficients agree
asymptotically. So, given (c)'s inputs, **the fluctuation part B^fl = B_loc − m̃ is O(1) for every admissible scheme except
at most one value of λ, and nothing in a tree-level computation selects that value.** A tree-level (SA-K) identification of
B_loc is therefore not available. Under the expected one-loop asymptotics B_loc/κ_W → 2β_0 (LCS-b together with (F_R)'s
one-loop running, i.e. UIR55's Corollary b_∞ given (ρ-null) + (TC) — physics expectation, not banked), ROTDEF's scheme has
B^fl → 2β_0 − C_F < 0 and the tree-level profile would run C_F/(2β_0) = 12π²(N² − 1)/(11N²) times too fast: 8.07 (N = 2),
9.57 (N = 3), increasing to 12π²/11 < 10.77 (s2_55_1 C6, rational π enclosure; C_F > 2β_0 for all N ≥ 2). Its octave span in
β-units would be (N² − 1)log 2 = 2.08 (N = 2), 5.55 (N = 3), against the perturbative 0.26, 0.58 of SEAM55 §1.5, and the local
Λ_phys ∝ Ω^{C_F/(2β_0) − 1} would vary by a factor 2^{7.07} to 2^{9.77} between equator and pole: an O(1) boost violation.
**(e) "Derivative of the effective action with respect to a local log-scale change."** On the sphere chart the lattice has
no metric; the local physical spacing aΩ(x) enters ONLY through the profile rule u = T(log aΩ). So at fixed rule
δS_eff/δlog s(x) = T′·δS_eff/δu(x) = −B_T·2N E[s̄(x)|·]: the profile's own slope times the s̄-image. The Ward coefficient
B_loc is defined by the field transformation Ξ_v (a dilation of the configuration), which is not the derivative of the
action or effective action with respect to any lattice parameter. Identifying the two would assert B_loc = κ_WB_T, the
Ward-profile condition itself: circular. On the flat hypercubic hierarchy there is no local log-scale parameter at all
(uniform blocking; RG scale changes are discrete, log L per step, and global); the per-step running is the trajectory
slope A, and relating it to B_loc is LCS-b, which the Ward profile was designed to avoid.
**Verdict on the route.** For clause (a) of LCS-a (existence and identification of the trace coefficient): **does not work;
obstruction exhibited** (PROVEN-HERE: B^tree = C_F exactly and scheme dependent over ℝ; CONDITIONAL: the needed coefficient
differs from it by an O(1) fluctuation term). Analyticity cannot supply a matching statement in any case (SRCAN55 §4 (N-2),
f(w) = w^{1/2}; and an analytic bounded remainder need not be small). For clauses (b) and (c): Cauchy works (§1.5-§1.6).

**Precision to §1.4(c) (appended at once; it narrows what (c) needs for (d)).** The pointwise conclusion "B′/κ′ − B/κ → 0 on
the band" needs nonvacuity for LOCALISED weights. Part (d) needs only the CONSTANT-weight case: if both tree-level values
were correct (B = C_F + o(1) for Ξ and B′ = C_F − λ/N + o(1) for Ξ′_λ, with κ, κ′ = 1 + O(g²) by §1.5), then with Ξ's Ward
profile the Ξ′-scalar coefficient is −λ/N + o(1), a constant, and (c)'s exact identity forces
(λ/N)·Cov(F, Σ_x a⁴χ(div v/4)2N s̄(x))/Z_e^q → 0. So (d) holds under (c)'s inputs plus nonvacuity of the PLAIN dilation
insertion (some F of the family, some boost).

### 1.5 Lemma REG — what Cauchy in the coupling does give (target P3 (b)). PROVEN-HERE (elementary)
**Hypothesis (H_an)** (= the analyticity part of (L-a)): f_R(z) := zϑ^p_R(z) (R ∈ {1, 3, 6′}) and f_D(z) := zϑ^p_D(z) are
holomorphic on the sector Σ(a) with |f_R|, |f_D| ≤ M, uniformly in a.
**Conclusions**, for real u ∈ 𝔟(a) (the disc |z − u| ≤ ρu lies in Σ(a)):
- (i) |f′(u)| ≤ M/(ρu) and |f″(u)| ≤ 2M/(ρu)² for f ∈ {f_R, f_D} (Cauchy). In particular **|(uϑ^p_R)′| ≤ M/(ρu) = O(g²)**.
- (ii) κ_W = 1 + f_1′ ∈ [1 − M/(ρu), 1 + M/(ρu)]; κ_W ≥ ½ for u ≥ 2M/ρ.
- (iii) B_loc = C_F + f_D − 4f_1: |B_loc| ≤ C_F + 5M, |B_loc′| ≤ 5M/(ρu).
- (iv) G := B_loc/κ_W: |G| ≤ M_G := 2(C_F + 5M) and |G′| ≤ 4[(5M/(ρu))(1 + M/(ρu)) + 2(C_F + 5M)M/(ρu)²] ≤ C_G/u.
- (v) **Global solvability of the Ward-profile ODE.** For dT/dt = −G(T) on t ∈ [log a, log 2a] with T(log a) = u_0 := u_traj(a):
  if u_0 − M_G log 2 ≥ max(inf 𝔟(a), 2M/ρ) (true for a ≤ a_0, since u_traj(a) → ∞ and M_G, M, ρ are a-independent), the
  solution exists, is unique and C¹ on the WHOLE interval, and |T(t) − u_0| ≤ M_G log 2 =: M_u. (Picard–Lindelöf on the
  invariant interval [u_0 − M_u, u_0 + M_u], on which G is C¹ with |G′| ≤ C_G/(u_0 − M_u).)
- (vi) **The profile is in SA-K's class.** u(x) = T(log aΩ(x)) has |u − u_0| ≤ M_u, |∇u| ≤ M_G|∇log Ω| ≤ M_G/R
  (|∇log Ω| = 2|x|/(R² + |x|²) ≤ 1/R). The relative Wilson coefficient ε̂_0(p) := (β̂_p/2N − u_0)/u_0 (incident-cell averages
  of u, CODEX_REVIEW_SPHERE F2) obeys ‖ε̂_0‖_∞ ≤ M_u/u_0 and, at level k, [ε̂_0]^∞_α ≤ M_G h_k/(Ru_0); both → 0 as a → 0, so
  ‖ε̂‖_cf ≤ ε̂_* (CODEX_REVIEW_SRCAN item 4's class) for a ≤ a_0. The source-polydisc requirement of (L-a) is r_src ≥ 2N M_u.
- (vii) The traceless coefficient of 𝔅_tl obeys 2N|f_R′(u)||∇u||v| ≤ 2N M M_G|v|/(ρuR).
**Proof.** Cauchy's estimates on the disc of radius ρu; the quotient rule; Picard–Lindelöf with the a priori bound |T′| ≤ M_G. ∎
**Notes.** (1) This closes CODEX_REVIEW_SEAM F4's remaining gap ("reaching the entire log interval … needs a uniform bound on
B_loc/κ and an adequate domain margin") as an implication of (H_an). (2) The RELATIVE sector (radius ρu) is essential: SRC's
absolute source polydisc (radius r_src, fixed) gives only |f′| ≤ M/r_src = O(1), not O(g²). The sector is the natural domain
of uniform-in-a control (SRCAN55 §4 (N-2): "a sector near the positive axis (Re u > 0, |Im u| ≲ ρ Re u)"). (3) (H_an) does
not determine the limits of B_loc or ϑ^p_R as u → ∞ (a sector is not a disc around g² = 0; SRCAN55's w^{1/2} example).

### 1.6 Proposition CL — the variable-coefficient content follows from the tilted form (target P3 (c)). PROVEN-HERE (implication)
**Statement.** Assume (L-a)-(L-c) in the tilted form of §1.3, with r_src ≥ 2N M_u. For the profiled theory (plaquette
weights β̂_p = 2N·(incident-cell average of u)) and every bulk site x, the profiled measure is the constant-u(x) measure tilted
by h_x(p) := −2N(ū(p) − u(x)) (ū the incident-cell average), h_x ∈ 𝒫. Then the profiled Ward functional's local scalar and
traceless content at x is that of SEAM55 E1 with coefficients evaluated at u(x): scalar (div v/4)·2N[B_loc − κ_WB_T](u(x))s̄,
traceless −2N(∂_μu)v^ν[(uϑ^p_3)′S^(3) + (uϑ^p_6′)′S^(6′)]_μν, plus remainders a²𝔏(a) (from (L-b)) + O(a²|∇∇u| + a²|∇u|²) =
O(a²/R²) × dimension-4 structures.
**Proof.** Exact linearity (SEAM55 §1.3, CODEX_REVIEW_SEAM F4): W_u(v) = W^{(u(x))}(v) + Ξ_v𝒮_{−h_x}. In the tilted state (which
IS the profiled state), (L-a)-(L-c) at constant coupling u(x) give the operator content of W^{(u(x))} at x and of Ξ_vs_p for p
near x. h_x(p) vanishes at p = x and is O(|p − x||∇u|) nearby: its first Taylor order produces E1's κ_W(v·∇u) and 𝔅_tl terms
(the computation Codex SEAM F4 re-derived), its second order the O(a²/R²) terms. All local identities hold in the same
(profiled) measure, so summing them over x and summing by parts is exact on the finite lattice. ∎
**Reading.** The variable-coefficient clause of SEAM55's LCS-a ("variable (position-dependent) coefficients", ASSEMBLY55 F14/F15)
costs nothing beyond stating the constant-coupling clause uniformly over SRC's source polydisc. What remains is (a).

### 1.7 What clause (a) consumes; status (target P3, the brief's list)
A proof of (L-a)-(L-c) would run as follows; each step names the lane input it consumes.
1. Exact first-order source recursion for the images of the remainder insertions, I_{k+1} = E[I_k | U_{k+1}] (SRCCD55 §5.0;
   Markov chain of normalised soft kernels): PROVEN.
2. A localisation at each level splitting the image into a marginal component (a multiple of the level-k action-density
   image) and an irrelevant remainder: SRCCD55 (M4)'s "localisation operator on the source-linearised RG": OPEN.
3. One-step contraction of the irrelevant remainder by L^{−2}(1 + O(g_k²)): tree level from SA-K and SA-WD (CONDITIONAL;
   SA-WD's weighted constant NOT-VERIFIED, CODEX_REVIEW_SRCAN item 5); fluctuation level from the per-step covariance (N5:
   Theorem RW / CT♯ — banked at the trivial background and level 0, general levels OPEN), the per-step polymer bound N6
   (OPEN) and Theorem CE (banked).
4. Marginal propagation λ_k := ∂u_{k+1}/∂u_k = 1 + O(g_k⁴): (Flow-an) (analytic form of (F_R)); (F_R) ⟸ (UIR^♮) ⟸ (TC-b)_𝔍 at
   orders 3-4 + (ρ-null) (UIR55 Theorem UIR-T, FLOW55: banked as implications; inputs OPEN, (ρ-null) ARGUED).
5. ϑ^p_1, ϑ^p_D (hence B_loc, κ_W) are DEFINED as the values for which the summed marginal components of the translation and
   trace remainders vanish; existence needs the feed from irrelevant parts to be summable (Σ_k g_k²L^{−2k} < ∞ given 3).
6. All coarse fields: per-step large fields conditional on the coarse field (RLF^η, SRC-κ-LF): OPEN. For the coarse-image
   part of (L-b), the tower lemma (§2.2) allows stating it at any finer fixed scale ℓ_0L^{−J}.
7. The sector: steps 3-6 at complex couplings with |Im z| ≤ ρ Re z (N5^η, N6^η, RLF^η complex: OPEN; SA-K and SA-RW supply the
   tree level and the linear level-0 part).
**Not consumed:** the value b_∞ = β_0^std log L (UIR55 Corollary b_∞), LCS-b, any one-loop number, coarse decorrelation, the
coarse law. (UIR^♮)/(ρ-null) enter only through (F_R)/(Flow-an). **Status: OPEN; owner: SRC lane** (the same family as SRC-M
(M-a); if SRC2_55's quantum source hierarchy produces SRC-M, it should produce (L-a)-(L-c) for the plaquette density with the
trace component).

### 1.8 The product condition (target P4): what "the normalised insertion products vanish uniformly along each path" requires
Write 𝒲_s(F, J) := Σ_x a⁴|w(x)|[ν(|Cov(F_s, J(x)|V)|) + ‖E[F_s|V] − ωF_s‖_{L²(ν)}·osc_V E[J(x)|V]]/Z_e^q (SEAM55 §1.2, normalised).
With the Ward profile the scalar coefficient vanishes identically; W0's residual is
- **(P-sc) scalar remainder.** Split the insertion of the remainders at distance r from supp F_s into r < r_c, r_c ≤ r, with a
  scale r_c(a) → 0, a/r_c(a) → 0. Far part (r ≥ r_c): with the dimension-6 weight a²r^{−6}, Σ_x a⁴a²r^{−6} ≤ C a²r_c^{−2} → 0
  (with the generic weight down to r ~ a this sum is O(1): the power-divergent a² × a^{−2} contact, which must therefore be
  put in the contact clause). Near part: (L-c) integrated over the r_c-ball gives c_con × (an H(4)-allowed structure at the
  observable point) + O((a/r_c)²𝔏): its product with the separated covariance it multiplies vanishes iff c_con → 0 (|c_con| ≤
  C/u suffices, given a bounded separated covariance, SRC-E′(ii)-type) — or it is absorbed, together with the observable's own
  trace coefficient, in the LOCAL normalisation Z_e(aΩ(x)) of SEAM55 §1.7 (then it never appears). So (L-c) must be stated in
  this integrated form (as SRCCD55's (M-b) also must, for its dimension-6 part).
- **(P-tl) traceless channel 𝔅_tl.** Coefficient ≤ 2N M M_G|v|/(ρuR) = O(g²) (Lemma REG (vii)); insertion 𝒲_s(F, S^R) for the
  dimension-4 tensors S^(3), S^(6′). With generic SRC-κ weights r^{−4}𝔤(r), 𝔤 a power of log, the near-observable sum is
  ∫ r³r^{−4}𝔤(r)dr = O(log(ℓ_0/a)·𝔏(a)), and the product O(g²·log·𝔏) does NOT vanish. **Requirement on W1: 𝒲_s(F, S^R) =
  o(log(ℓ_0/a)) uniformly in s** (o(log²) suffices if (L-a) supplies the perturbative form f_R(z) = c_R + d_R/z + O(z^{−2}) with a
  differentiable uniform remainder, giving (uϑ^p_R)′ = O(g⁴)). ARGUED support: the single-contraction mixing S^R·e → S^R is
  O(g²) per unit of log, so 𝒲 = O(1) is expected (the symmetric traceless stress tensor of pure YM is conserved and
  non-anomalous; its two lattice H(4) components have finite normalisations Z_3, Z_6′ = 1 + O(g²)). This is a W1 obligation
  with an explicit logarithmic budget, not a consequence of LCS-a.
- **Uniformity along the path.** {F_s : |s| ≤ s_0} is the image of a compact set of test functions under a smooth flow
  (CODEX_REVIEW_SPHERE F14), so W1, W3 and (L-b)-(L-c) must hold uniformly over bounded C^m-sets of test functions with supports
  at distance ≥ d_0 from the equator; then the products vanish uniformly in s.
- These are SUFFICIENT conditions (CODEX_REVIEW_SEAM F5: the absolute-value bounds are not necessary).

### 1.9 Verdict on LCS-a
- **Stated exactly** (§1.3): one SRC-M-type clause for the lattice Lie derivative of the plaquette action density (vector and
  trace components), tilted, all coarse fields, sector-analytic, with an integrated contact clause.
- **PROVEN-HERE:** Proposition M (measure term exact, m̃ = C_F); B_loc = C_F + u(ϑ^p_D − 4ϑ^p_1); clause (i) ⟸ clause (ii)
  with ϑ^p_D; Lemma REG (regularity, κ_W ≥ ½, global ODE solvability, SA-K class); Proposition CL (variable coefficients from the
  tilted form); the scheme family Ξ′_λ with tree-level value C_F − λ/N.
- **CONDITIONAL (implication PROVEN-HERE):** scheme independence of the Ward profile; hence the fluctuation part is O(1).
- **Does not work (obstruction exhibited):** the suggested SA-K + Cauchy identification of B_loc.
- **OPEN:** clause (a) itself, consuming the inputs of §1.7; W1's logarithmic budget (P-tl).

---

## 2. N5-T* — the seam at rough coarse fields

### 2.1 Seam operators: complete local list, coefficients, tuning (target P5, Q3). PROVEN (symmetry/dimension); tree coefficients ARGUED
Setting: at scales ≫ a, bulk Yang–Mills on both sides of a 3-dimensional defect (the O(a) prism layer). Exact symmetries of the
regulator: gauge invariance; Γ_reg = H(4) × ⟨θ_eq⟩ (SPHERE55 §1.5); θ_eq fixes the seam pointwise and reverses the normal; the
four coordinate reflections θ_μ ∈ H(4) reverse the seam's orientation; the radial profile is Γ_reg-invariant. A seam operator of
canonical dimension d integrated over the seam has a coefficient of mass dimension 3 − d: marginal is d = 3, irrelevant d ≥ 4.
- **d = 0, identity** (seam "tension", power-divergent coefficient ~ a^{−3}): a c-number; Ξ acts on fields, so its Ward variation
  is 0, and it drops out of every covariance and every oscillation.
- **d = 1, 2, 3, single connection:** gauge-invariant local polynomials need two curvatures (d ≥ 4); tr F_μν = 0; the normal
  vector and normal derivatives cannot build a gauge-invariant scalar below d = 4 (n^μ∂_μ of a gauge-invariant scalar of
  dimension ≤ 2: none exists). The only exception is CS_3(A|_seam): coefficient constant by small-gauge invariance, θ_eq-EVEN,
  θ_μ-odd, hence excluded (SPHERE55 §4.3; CODEX_REVIEW_SPHERE F8; CODEX_REVIEW_SEAM F7). Position-dependent (staircase-
  pattern) coefficients multiply the same list and cannot create new operators below d = 4. Profile-induced candidates:
  (∂_nu)·(d = 2): none; (∂_nu)·CS: θ_μ-odd; excluded.
- **Two-sided structure (before single-valuedness): the gluing operator.** In the matching gauge (crossing links fixed to 1,
  SPHERE55 §2 step 1) the gauge-covariant jump J_i := A^S_i − A^N_i gives tr(J_iJ_i), d = 2 (RELEVANT), coefficient
  ∝ β̂_cross/a with β̂_cross ≥ (3/4)β(2a) > 0 (CODEX_REVIEW_SPHERE F2). Its dimensionless strength at scale ℓ is
  λ_seam(ℓ) = (β̂_cross/β)(ℓ/a) → ∞ (SEAM55 §2.4, tree level): the glued (transparent) defect is the IR attractor, the decoupled
  defect (β̂_cross = 0) the unstable fixed point, excluded by construction. **No tuning:** only the sign and non-vanishing of
  β̂_cross (relative to a/ℓ) matter, and both hold. (That no finite soft step removes the mode, CODEX_REVIEW_SPHERE F9, is not
  a tuning issue; it is the quantitative content of N5-RG.)
- **d = 4 (θ_eq-even):** tr F_ijF_kl λ^{ijkl}(x) and tr F_inF_jn λ^{ij}(x) (tangential–tangential, normal–tangential; anisotropic
  tensors allowed because the staircase breaks the tangent-space rotations); tr FF̃|_seam ∝ ε^{ijk}tr F_ijF_kn is θ_eq-odd and
  excluded. **Their coefficients are NONZERO at tree level** (ARGUED, generic): the classical action of the prism layer for a
  smooth single-valued field differs from a bulk layer of the same thickness, because the crossing weights are ¼Σ_cβ_c with
  k_e ∈ {3, 4, 5, 6}, the boundary squares carry (m_D + 2)/4 ∈ {3/4, 1, 5/4} of the bulk weight, and the crossing chords vary in
  (0, 4a) with no lower bound (F15); a flat terrace (k_e = 4, m_D = 2) is defect-free, corners are not, so the pattern average
  is generically ≠ 0 at order a·u. **No tuning is needed:** d = 4 is irrelevant on a 3-dimensional defect (coefficient ∝ a).
  Their Killing flux (displacement/tangential variation: d = 5 with coefficient a, or d = 4 times the extrinsic curvature 1/R
  with coefficient a) has coarse image O(a·u(ℓ)·ℓ^{−5}·R³) at background curvature ~ ℓ^{−2}: → 0 as a → 0 at fixed ℓ, R.
- **Mixing.** A d = 4 seam operator can mix only into lower-dimension seam operators — the identity (c-number), CS (forbidden),
  or, in the two-sided description, the gluing operator (a relative O(g²) shift of a positive relevant coupling). A codimension-1
  defect generates no bulk operator (locality), and the bulk-to-defect expansion of a bulk operator at distance r gives only
  O(a/r) corrections for the glued defect plus irrelevant terms. So no power-divergent mixing produces an O(1)-coefficient seam
  operator carrying Killing flux.
- **Answer to the brief's question.** A dimension-4 seam operator DOES have a nonzero coefficient (generically, at tree level,
  O(a·u)), and it need NOT be tuned: dimension 4 is irrelevant on the seam. The marginal seam dimension is 3, where the only
  candidate (CS) is excluded by θ_μ. **Q3 is not realised.** (A power RATE better than O(a/ℓ) would need Symanzik-type
  tree-level tuning of the d = 4 seam coefficients, e.g. via the seam weights; not needed for o(1).)

### 2.2 The tower lemma. PROVEN-HERE; s2_55_2 G1 (exact chains), Y1 (non-Markov control fires)
**Statement.** Let U_0 → U_1 → … → U_n be the seam-adapted soft chain (joint density ∝ e^{−S(U_0)}Π_iK_i(U_{i+1}|U_i), normalised
nonnegative kernels: SPHERE55 §1.6 (B1), CODEX_REVIEW_SPHERE "seam-kernel bookkeeping" CONFIRMED). For every bounded X(U_0), every
level k ≤ n and every constant c:
  (i) E[X | U_n] = E[ E[X | U_k] | U_n ];   (ii) sup_{U_n} |E[X|U_n] − c| ≤ sup_{U_k} |E[X|U_k] − c|;
  (iii) osc_{U_n} E[X|U_n] ≤ osc_{U_k} E[X|U_k];   (iv) ‖E[X|U_n] − EX‖_{L²} ≤ ‖E[X|U_k] − EX‖_{L²}.
**Proof.** Normalised forward kernels give the reverse Markov property (CODEX_REVIEW_SEAM F2): given U_k, (U_0, …, U_{k−1}) is
independent of (U_{k+1}, …, U_n); hence E[X | U_k, …, U_n] = E[X | U_k] and (i) is the tower property. A conditional expectation
is a positive normalised average and an L²-contraction: (ii)-(iv). Every conditional expectation is defined at EVERY
configuration because each soft factor is strictly positive (UNIV55 §2.1, "Well-posedness of sup_V"). ∎ (s2_55_2: exact
3-level chains; the non-Markov law with U_1 ⊥ U_0 and U_2 depending on U_0 violates (ii) at c = EX: E[X|U_1] ≡ 0, E[X|U_2] = ±4/5.)
**Consequence (general, for every lane).** Every "for all coarse fields" conditional-MEAN clause at the reference scale — N5-T*,
SRC-E′_∞, the coarse-image parts of W1, W3 and (L-b), SRC-κ (κ-3) — is implied by the same clause at any finer fixed scale
h_{n−J} = ℓ_0L^{−J}. The conditional law of the levels above n − J never enters such a clause. (It does not apply to conditional
COVARIANCES, nor to Proposition T's two-theory comparison, whose conditional laws differ between the theories.)

### 2.3 Theorem N5′ (alternative decomposition of N5). CONDITIONAL; implication PROVEN-HERE; s2_55_2 G2-G4
**Inputs** (F = F_s ranges over the path family of one element of the separated ^0𝒮 family; constants uniform in s):
- **(T-all)_J** τ_*(a; J) := inf_c sup_{U_{n−J}} |E[𝔖 | U_{n−J}] − c| → 0 as a → 0, for every fixed J ≥ 0. (For boosts the
  optimal c is 0: the chain is θ_eq-equivariant (SPHERE55 (B3)) and 𝔖 is θ_eq-odd (§4.2 P2), so the image is odd under the
  involution and sup|I − c| ≥ sup|I|.) (T-all)_0 is SEAM55's N5-T*; by the tower lemma (T-all)_J ⇒ (T-all)_{J′} for J′ ≤ J.
- **(E′_J)** ‖E[F_s | U_{n−J}] − ωF_s‖_{L²} ≤ C_F(J) Z_e^q for every J, uniformly in a ≤ a_0(J) (implied by the sup form
  sup_{U_{n−J}}|E[F_s|U_{n−J}] − c| ≤ C_F(J)Z_e^q, a no-fine-moment statement of SRC-E′_∞ type at the finer scale).
- **(D)** Σ_{i<n−J} E|Cov(F_{s,i}, 𝔖_i | U_{i+1})| ≤ δ_F(J) Z_e^q with δ_F(J) → 0 as J → ∞, uniformly in a ≤ a_0(J) (pure one-step
  conditional decay below the top J levels, averaged; e.g. SEAM55's N5-C WITHOUT its transparency factor,
  E[|Cov(F_i, 𝔖_i|U_{i+1})| | V] ≤ Z_e^qΓ_FL^{p(n−i)}e^{−m_1(d_0/2)/h_{i+1}}, gives δ_F(J) = Γ_FΣ_{j≥J}L^{p(j+1)}e^{−m_1d_0L^j/(2ℓ_0)}).
**Conclusion.** sup_s |Cov(F_s, 𝔖)|/Z_e^q → 0 as a → 0.
**Proof.** Total covariance at V = U_n: Cov(F, 𝔖) = E Cov(F, 𝔖 | V) + Cov(E[F|V], E[𝔖|V]). Coarse term: ≤ ‖E[F|V] − ωF‖_{L²} ·
inf_c sup_V|E[𝔖|V] − c| ≤ C_F(J)Z_e^q·τ_*(a; J) (tower (iv) for F, tower (ii) for 𝔖). Conditional term: Proposition B
(CODEX_REVIEW_SEAM F2) gives |E Cov(F, 𝔖|V)| ≤ Σ_{i<n} E|Cov(F_i, 𝔖_i|U_{i+1})|. For i ≥ n − J:
|Cov(F_i, 𝔖_i | U_{i+1})| = |E[(F_i − E[F_i|U_{i+1}])(𝔖_i − c) | U_{i+1}]| ≤ E[|F_i − E[F_i|U_{i+1}]| | U_{i+1}]·sup_{U_i}|𝔖_i − c|, so
E|Cov(F_i, 𝔖_i|U_{i+1})| ≤ ‖F_i − EF‖_{L²}·τ_*(a; J) ≤ C_F(J)Z_e^q τ_*(a; J) (the conditional expectation onto σ(U_{i+1}) is the
L²-projection, constants included; tower (ii), (iv) from level n − J to i). For i < n − J use (D). Hence
|Cov(F_s, 𝔖)|/Z_e^q ≤ (J + 1)C_F(J)τ_*(a; J) + δ_F(J); let a → 0 at fixed J, then J → ∞. ∎
**Comparison with SEAM55 Theorem N5 (both are valid sufficient conditions).** N5′ needs the transparency input in the stronger
form (T-all)_J for all J (N5-T* at every finer fixed scale), but only as a conditional MEAN, at running coupling ≤ g(ℓ_0L^{−J}),
as small as desired; its decay input (D) is pure CD below the top J levels (no "transparency-weighted fluctuation sizes",
no top-level decay) — the same kind of input W1 needs in the bulk. The top J levels, where the coupling is fixed, enter only
through products of image oscillations. No rate is claimed (CODEX_REVIEW_SEAM F3); with explicit power hypotheses
τ_*(a; J) ≤ C(J)(a/ℓ_0)^{θ_*} and the exponential tail of δ_F, one can optimise J(a) ~ log log(ℓ_0/a) for a rate.

### 2.4 What N5-T* contains at any reference scale: the obstruction isolated. ARGUED (mechanisms); inputs named
Fix a reference scale ℓ = h_{n−J} (any J; ℓ = ℓ_0 is SEAM55's case). N5-T*(ℓ) asks sup over ALL level data U at scale ℓ of
|E[𝔖 | U]| → 0 as a → 0. Its content splits into four parts, all at running coupling ≤ g(ℓ):
- **(α) Small-field seam RG (seam-specific).** For data small in own units near the seam, the levels between a and ℓ integrate
  fluctuations around a smooth background; §2.1's list leaves only the identity, the positive gluing operator and irrelevant
  d ≥ 4 operators, so the image is O(a·u(ℓ)ℓ^{−5}R³) at tree level (SEAM55 §2.4's θ = 1 count, CODEX_REVIEW_SEAM F7: ARGUED).
  The estimate needed is SPHERE55's N5-RG at small fields — BFT/N5/N6 on the seam lattice with non-rectangular blocks,
  valences 5-9, incident-cell weights, and crossing chords with no lower physical length (CODEX_REVIEW_SPHERE F15 forbids
  importing regular-cell estimates). OPEN.
- **(β) Moderate-curvature levels below rough data (shared with the bulk).** Data of own-unit curvature up to C_N at scale ℓ
  force curvature ≤ C_N L^{−2j} at the j-th level below; after j_* := ⌈log(C_N/ε_0)/(2 log L)⌉ levels the background is
  small-field. The j_* intermediate levels need BFT at bounded-but-not-small curvature: UNIV55's (N3) ("needs the constrained
  Hessian positive there: κ large against C_N"). At coupling ≤ g(ℓ) this is a CLASSICAL problem (existence, positivity and
  multiplicity of the constrained critical points for arbitrary bounded data) plus Gaussian-size fluctuations; several
  critical points are harmless for a conditional MEAN if each is smooth at the seam. OPEN; the same input is needed by every
  all-coarse-field clause (SRC-E′_∞, W1/W3 coarse images, (L-b)), so it is not a seam-specific obstruction.
- **(γ) Wild crossing data (seam-specific).** A coarse crossing variable far from the gauge-equivalent continuation of the
  neighbouring chart links (possibly on a short chord) must be answered by the finer field in one of three ways:
  (1) a jump field on the finer crossing links — spread over scale ℓ it costs ~ β̂_cross|Δh|²ℓ/a (the gluing operator is
  relevant), concentrated on one crossing link it costs at least the k_e ≥ 3 crossing plaquettes through that link, each of
  weight ≥ (3/4)β(2a), i.e. ≳ (9/2)N u·s(Δh); (2) disagreement with the coarse variable, at the soft kernel's finite cost
  κ_K u·s(Δh)·O(1); (3) a bulk-smooth realisation near the coarse vertex at scale ℓ, cost O(u(ℓ)θ²) (classical scale
  invariance in 4D, asymptotic freedom favouring the larger scale). For κ_K below the seam's own crossing stiffness
  (κ_K ≲ (9/2)N, an order-of-magnitude comparison), options (2)-(3) win: wild crossing data do not open the fine seam, which
  stays glued and smooth. ARGUED (tree-level energy comparison). **Design check (new):** a seam kernel much stiffer than that
  (κ_K ≫ 2N·k_e at seam links), or a hard δ-constraint, would make option (1) competitive and could force lattice-scale
  roughness at the seam for wild data — which would defeat N5-T* in its all-coarse-field form even though such data are
  improbable. The softness of the seam kernels is load-bearing for the sup form; N5-RG should verify the inequality for the
  chosen κ_K (the bulk Decision-4 range κ_− ≤ κ_K ≤ κ_+ is a free parameter, PROOF "Decision 4 is MADE").
- **(δ) Spontaneous large fields below (shared with the bulk).** Per-step Peierls-type bounds near the seam, uniform in the
  coarser field (RLF on the seam lattice, conditional form): OPEN.

### 2.5 Obstruction search (Q3, Q4). No counterexample
| # | Candidate | Outcome |
|---|---|---|
| 1 | gauge-invariant seam operator of d ≤ 3 allowed by Γ_reg | none: identity (c-number) and CS (θ_μ-odd) only (§2.1) |
| 2 | d = 4 seam operator requiring tuning | present (nonzero, O(a·u)) but irrelevant on the 3-dimensional seam: no tuning |
| 3 | gluing operator with zero or negative coefficient | excluded: β̂_cross ≥ (3/4)β(2a) > 0 for the actual incident-cell weights |
| 4 | power-divergent mixing into an O(1) seam operator carrying flux | only into the identity, CS (forbidden) or the gluing operator; no bulk operator is generated |
| 5 | profile kink at the seam | [∂_nu]·CS is θ_μ-odd; [∂_nu]·(d = 4) has coefficient a/R: irrelevant |
| 6 | short crossing chords (no lower bound, F15) | the lattice action is combinatorial (weights do not depend on chord length); wild data on short coarse chords: §2.4 (γ) |
| 7 | rough coarse data at the reference scale | the tower lemma moves the clause to any finer scale; content = §2.4 (β)-(δ), weak coupling, no top-level law |
| 8 | pole rotations (tangential flux) | anisotropic d = 4 coefficients × a: irrelevant (SEAM55 §2.6 (e)) |
| 9 | hard-constraint or very stiff seam kernel | would force fine roughness for wild data: a design condition, not a property of the soft construction (§2.4 (γ)) |
**Q3 and Q4 are not realised** for the soft-kernel construction. Nothing found requires tuning.

### 2.6 Verdict on N5-T*
- **Not proved.** It is not a tuning problem and not an infrared problem.
- **PROVEN-HERE:** the local operator classification's symmetry/dimension part (no marginal seam operator; d = 4 irrelevant;
  the gluing operator relevant with a positive coefficient); the tower lemma; Theorem N5′ (as an implication).
- **Isolated (§2.4):** N5-T* at any fixed scale = small-field seam RG (α) + moderate-curvature BFT at weak coupling (β, shared
  with every all-coarse-field clause) + the fate of wild crossing data (γ, ARGUED to be absorbed by the soft kernel, with a
  design check on κ_K at seam links) + spontaneous large fields (δ, shared). The non-perturbative top levels never enter
  (tower lemma); in Theorem N5′ the top J levels enter only through products of image oscillations.
- **The open heart of N5** (SEAM55's phrase) is therefore (α) + (γ): the seam lattice's RG at weak coupling, around arbitrary
  bounded data. Owner: the seam RG (N5-RG), unassigned.

**Erratum E1 (§2.4 (γ), reasoning of the concentrated-jump cost; appended at once).** "at least the k_e ≥ 3 crossing plaquettes
through that link" should read: "at least 3 crossing plaquettes through that link — a seam vertex v lies in some boundary
3-face of ∂D_a, whose three edges at v are seam edges, and each seam edge e ∋ v gives one crossing plaquette e × [0,1]
containing C_v — each of weight ≥ (3/4)β(2a)". k_e (the number of boundary 3-faces at an EDGE) is a different count. The
resulting bound ≳ (9/2)N u·s(Δh) is unchanged; it remains an order-of-magnitude comparison (ARGUED).

---

## 3. H_Euc on the sphere route: every input, owner, status after this file (target P6)

**Consumed** (ASSEMBLY55 N4; CODEX_REVIEW_ASSEMBLY R2): for every observable/group pair of countable families (the CARTESIAN
product, CODEX_REVIEW_SEAM F8), vanishing Euclidean defects along one joint sequence; then the flat limit at the pole.
**H_Euc (sphere) ⟸** (A) fixed-R local Killing invariance on the determining family + (B) the R → ∞ transfer + (C) DIAG, with:

| # | Input | Precise form (file: §) | Owner | Status after SPHERE2_55 |
|---|---|---|---|---|
| 1 | Regulator K_a, incident-cell weights ¼Σ_cβ_c, RP for the equator and four coordinate spheres | SPHERE55 §1-§2 + CODEX_REVIEW_SPHERE F2, F4 | — | PROVEN (banked) |
| 2 | Exact Ward identity, χ-independence, split W = B + 𝔖, no far shell | SPHERE55 §3.1-§3.4 | — | PROVEN (banked, Codex SPHERE F5) |
| 3 | Lemma 3.5′ (coarse-image two-scale bound) | SEAM55 §2.1 | — | PROVEN (banked, Codex SEAM F1) |
| 4 | Integration of the identity for every F (Theorem 3.6's implication) | SPHERE55 §3.5; F-independent | — | PROVEN as implication (banked) |
| 5 | Proposition M: −div Ξ_v = 2N C_F Σ_p(div v/4)(c_p)s(U_p) exactly; m̃ = C_F | this file §1.1 | — | PROVEN-HERE (s2_55_1, s2_55_1b); pending Codex |
| 6 | W0 = Theorem W0 with the Ward profile −T′ = [C_F + T(ϑ^p_D − 4ϑ^p_1)]/κ_W | SEAM55 §1.5 + E1; this file §1.2 | — | CONDITIONAL on 6a and on the product conditions 6c (banked as implication, Codex SEAM F4) |
| 6a | LCS-a = (L-a)-(L-c): ONE SRC-M clause (lattice Lie derivative of the plaquette density, vector + trace part; tilted; all V; sector-analytic; integrated contact clause) | this file §1.3 | SRC lane | OPEN; its regularity (Lemma REG) and variable-coefficient content (Proposition CL) PROVEN-HERE as implications (pending Codex); the SA-K + Cauchy route to its core does not work (§1.4) |
| 6b | LCS-b (only for the trajectory profile) | SEAM55 §1.4 | SRC + flow | not needed with the Ward profile |
| 6c | Products → 0 uniformly along paths: (P-sc) contact coefficient c_con → 0 or absorbed in Z_e(aΩ(x)); (P-tl) W1 bound 𝒲(F, S^(3,6′)) = o(log(ℓ_0/a)) | this file §1.8 | SRC lane (W1) | OPEN (requirement stated; ARGUED expected O(1)) |
| 7 | W1 for every F of the family (rotation dim ≥ 6, translation dim 7, contacts, O(a) Hessian term, Θ̂ and S^(3,6′) insertions), 𝒲-form, with 6c's log budget | SPHERE55 §3.5 + E10; SEAM55 §1.2 | SRC lane | OPEN |
| 8 | W3 in sup-over-V form with the local normalisation Z_e(aΩ(x)) | CODEX_REVIEW_SPHERE F11; SEAM55 §1.7 | SRC lane | OPEN |
| 9 | N5: SEAM55 Theorem N5 (N5-T* + N5-C + SRC-E′_∞) OR Theorem N5′ ((T-all)_J + (E′_J) + (D)) | SEAM55 §2.5; this file §2.3 | — | CONDITIONAL (SEAM55's banked, Codex SEAM F2; N5′ PROVEN-HERE as implication, pending Codex) |
| 9a | N5-T* / (T-all)_J: seam image uniformly small for all data at a (finer) fixed scale | SEAM55 §2.5; this file §2.3-§2.4 | seam RG (N5-RG) — unassigned; parts (β), (δ) shared with large-field/(N3) lanes | OPEN; no tuning, no IR content (§2.1, §2.5); content isolated as (α)-(δ) |
| 9b | Decay: N5-C (SEAM55) or (D) (pure CD below the top J levels, averaged) | SEAM55 §2.5; this file §2.3 | SRC lane (CD) | OPEN |
| 10 | SRC-E′_∞ (SEAM55) or (E′_J) (L² coarse image at level n − J) | SEAM55 §2.1; this file §2.3 | SRC lane | OPEN |
| 11 | L1-sphere: BFT clauses, action-based large fields (no chessboard), flow with the bounded slowly varying Ward profile on K_a; the seam lattice's RG | ASSEMBLY55 F13-F15; SPHERE55 §4.5 | BFT / large-field / flow lanes | OPEN; tree-level bulk part: the Ward profile is inside SA-K's class on hypercubic 𝒞_glob (Lemma REG (vi)); seam and off-𝒞_glob excluded |
| 12 | Contraction geometry and conditional R → ∞ transfer | CODEX_REVIEW_P4 §4.1; CODEX_REVIEW_SPHERE F14 | — | PROVEN conditionally (banked) |
| 13 | U-sep + ^0𝒮 contraction lemma (replaces U-mom) | ASSEMBLY55 F5 repair | SRC lane / OS0 | OPEN |
| 14 | U-alg: R-independent observable maps and profile rule | SEAM55 §1.5, §1.7 | — | holds by construction (B_loc, κ_W are flat-lattice functions of u; T(log a) = u_traj(a) is R-independent), given 6a |
| 15 | DIAG in the Cartesian-product form | SEAM55 §3.3 + CODEX_REVIEW_SEAM F8; CODEX_REVIEW_ASSEMBLY R2 | — | PROVEN (banked) |
| 16 | q-point (all q) versions of 7-10 | CODEX_REVIEW_SPHERE F7 | SRC lane | OPEN (inside 7-10) |
| 17 | Positivity/regularity/contact bridge from separated products to the full OS algebra | CODEX_REVIEW_SEAM F9; OSLEAF55 (running) | OS lane | OPEN — most dangerous |
| — | H_int: a uniformly signed non-freeness witness (outside H_Euc) | CODEX_REVIEW_SPHERE F13 | NONFREE55 | OPEN |

**First non-UV item: none.** Every input integrates scales below a fixed reference scale with the coarse field held fixed,
uniformly in it (CODEX_REVIEW_SPHERE F11's operational sense). The tower lemma sharpens this: every conditional-mean clause
may be stated at an arbitrarily fine fixed scale (running coupling as small as desired), and Theorem N5′ removes the need for
decay at the top levels. The only item that is not a Yang–Mills estimate at all, and the most dangerous, is row 17.
**Most likely points of failure, in order (updated):** (i) row 17 (the OS-algebra bridge); (ii) row 6a's core (a matching
statement whose fluctuation part is O(1) — §1.4 shows it cannot be read off at tree level) together with 6c's log budget;
(iii) row 9a's seam-specific parts (α), (γ); (iv) the shared moderate-curvature input (N3) behind every all-coarse-field clause.

---

## 4. Verdicts on inherited claims touched by this file (REVIEW_BRIEF_55 order; file + locating string)

| # | Claim (file: locating string) | Verdict | Derivation / reason |
|---|---|---|---|
| H1 | SEAM55 E1: "B_loc(u) = u(ϑ^p_D − 4ϑ^p_1) + m̃ (m̃ from the measure term)" | **CONFIRMED; sharpened** | Proposition M: for ROTDEF's Ξ, m̃ = C_F exactly (an exact action-density source, all configurations); s2_55_1 |
| H2 | SEAM55 §1.4: "clause (i) is a NEW SRC-M clause (call it (M-d))" | **CONFIRMED as sufficient; refined (not independent)** | §1.2: (i) follows from clause (ii) extended by the trace coefficient ϑ^p_D, given Proposition M; LCS-a is one clause |
| H3 | SEAM55 §1.4 (iii) and E1 item 1: "κ Lipschitz and κ > 0" (assumed) | **CONFIRMED as a consequence** | Lemma REG (ii)-(iv) from sector analyticity (H_an); B_loc > 0 is not needed for W0 (it only normalises c_4) |
| H4 | SEAM55 §1.5: "Existence and uniqueness of T: LCS-a (iii) (Lipschitz ODE on a bounded interval)" | **NOT-VERIFIED as written (agree CODEX_REVIEW_SEAM F4); repaired** | Lipschitz alone gives local existence; Lemma REG (v) gives the whole interval inside the domain from (H_an) |
| H5 | SEAM55 §1.5: "≈ β_0^std log 2 in β-units: 0.26 for N = 2, 0.58 for N = 3" | **CONFIRMED (arithmetic) as the perturbative value; not derived (agree Codex F4)** | 2N·2β_0·log 2 ∈ [0.2574, 0.2576] (N = 2), [0.5793, 0.5795] (N = 3), rational enclosures, s2_55_1 informational; the tree-level value would be (N² − 1)log 2 = 2.08, 5.55 |
| H6 | SEAM55 §1.7: measure term "its dimension-4 part is part of B_loc (it is the O(g²)-relative, one-loop-type piece of the trace channel)" | **CONFIRMED; sharpened** | it is ENTIRELY dimension-4-type, coefficient exactly C_F, no remainder (Proposition M) |
| H7 | SEAM55 §1.8: "LCS-a (and LCS-b) must be proved directly as matching statements of the source-inserted RG" | **CONFIRMED** | §1.4 (e): the only local log-scale derivative available is −B_T × (s̄-image); identifying it with B_loc is circular |
| H8 | SEAM55 §2.4: "Dimensions 1-3: none, except CS, excluded by the coordinate reflections θ_μ" and d ≥ 4 with coefficients a^{d−3} | **CONFIRMED; extended** | §2.1: gluing operator (d = 2, positive relevant), mixing, profile kink, anisotropic d = 4 tensors; d = 4 coefficients nonzero (ARGUED) but irrelevant |
| H9 | SEAM55 §2.5 Theorem N5 (implication) | **CONFIRMED (agree CODEX_REVIEW_SEAM F2)** | re-derived (reverse Markov + total covariance); s2_55_2 G2; Theorem N5′ is an alternative decomposition |
| H10 | SEAM55 §2.6 (g): "(N5-T*) at rough V is the open heart of N5" | **CONFIRMED that it is open; refined** | §2.4: the rough-V part is shared with every all-coarse-field clause and lives at weak coupling (tower lemma); the seam-specific heart is (α) + (γ) |
| H11 | SPHERE55 §3.4 T4: the lattice's scale response "appears as −(1/16)(dg^{-2}/dlog s)_exact (div v) F^a F^a (through the measure term and the a^{-2} mixing of the classical dimension-6 scalar)" | **NOT-VERIFIED (agree SEAM55 H4)** | the measure term's share is exactly C_F and scheme dependent (Ξ′_λ: C_F − λ/N); equality of the total with the exact running is LCS-b |
| H12 | SPHERE55 §6: "N5b / N5-RG at large coarse fields … This is the single most likely point of failure of the IR-freeness claim" | **CONFIRMED as a conditional statement; premise avoidable** | its "if only typical coarse fields" premise is avoided by the tower lemma; the large-field content is weak-coupling, not infrared |
| H13 | UNIV55 §3.4: "(W0) … c_4 = O(g_0(a)^2) by P4's two-loop rule" | **NOT-VERIFIED (agree SEAM55 H21)** | the two-loop rule matches B_loc only under LCS-b at one loop; the tree-level coefficient is C_F, 8-11 times 2β_0 |
| H14 | PROOF.md [S26-BANKED] sphere bullet: "scalar c_4 = 0 for the Ward profile T′ = −B_loc/κ_W" | **CONFIRMED** | re-derived with Proposition M: −T′ = [C_F + u(ϑ^p_D − 4ϑ^p_1)]/κ_W |
| H15 | CODEX_REVIEW_SEAM banked item 2: "Ward restoration additionally needs the actual normalized insertion products to vanish, uniformly along each path" | **CONFIRMED; made explicit** | §1.8: (P-sc) integrated contact clause; (P-tl) W1 log budget o(log(ℓ_0/a)) |
| H16 | Brief/HANDOFF premise: N5-T* + N5-C + SRC-E′_∞ ⇒ N5, "qualitative o(1); a rate only with explicit power hypotheses" | **CONFIRMED (agree Codex SEAM F2, F3)** | Codex F3's counterexample re-derived: Cov = 1/(k + 1) at a_k/ℓ_0 = 3^{−2k} |
| H17 | SEAM55 §3.3 DIAG with paired hypotheses "for each k … e_{R,k}(a) → 0" | **REFUTED as displayed (agree Codex SEAM F8); repair CONFIRMED** | paired errors do not control F_i under g_j; enumerate the Cartesian product (banked repair) |
| H18 | SEAM55 §1.2: "vanish in Theorem 3.6 iff" | **REFUTED (agree Codex SEAM F5)** | absolute bounds are sufficient, not necessary (J_1 = X, J_2 = −X) |
| H19 | CODEX_REVIEW_SEAM F4: domain margin "also needs a uniform bound on B_loc/kappa and an adequate domain margin" | **AGREE; closed conditionally** | Lemma REG (v), from (H_an) |
| H20 | CODEX_REVIEW_SEAM F6: relative-o(1) LCS-b gives c_4 = 1/(u + 2) | **AGREE** | (B_eff − A)/B_eff with A = 1 + 1/u, B_eff = 1 + 2/u is (1/u)/(1 + 2/u) = 1/(u + 2) |

Only spot-checked (agree, not re-derived in full): CODEX_REVIEW_SEAM F7's tree-level Gaussian jump arithmetic and F10's H19
cube enumeration; SEAM55 E7's corrected flow-error bound (agree with Codex F6's derivation).

## 5. Summary table of this file's own claims

| # | Claim | Status | Where / check |
|---|---|---|---|
| 1 | Proposition M: div Ξ_v = −N C_F Σ_p(∂_μv^μ + ∂_νv^ν)(c_p)s(U_p) for quadratic v; = −2N C_F Σ_p(div v/4)s(U_p) for conformal Killing v; exact, all configurations | PROVEN-HERE | §1.1; s2_55_1 C1-C4, s2_55_1b |
| 2 | B_loc = C_F + u(ϑ^p_D − 4ϑ^p_1); LCS-a (i) ⟸ (ii) + ϑ^p_D; Ward profile −T′ = [C_F + T(ϑ^p_D − 4ϑ^p_1)]/κ_W | PROVEN-HERE (bookkeeping) | §1.2 |
| 3 | LCS-a stated exactly as one SRC-M clause (L-a)-(L-c) | statement | §1.3 |
| 4 | Tree-level (SA-K-level) trace coefficient = C_F exactly | PROVEN-HERE | §1.4 (a) |
| 5 | Admissible scheme family Ξ′_λ; tree value C_F − λ/N (every real number) | PROVEN-HERE (leading order) | §1.4 (b); s2_55_1 C5 |
| 6 | Scheme independence of the Ward condition (and the constant-weight corollary) | CONDITIONAL (implication PROVEN-HERE) | §1.4 (c) + precision |
| 7 | The SA-K + Cauchy route cannot identify B_loc (fluctuation part O(1)) | REFUTED as a route (obstruction: rows 4-6) | §1.4 (d) |
| 8 | C_F/(2β_0) = 12π²(N² − 1)/(11N²) ∈ (8.07, 10.77); octave spans; Λ_phys ratio 2^{7.07…9.77} under a tree profile | PROVEN-HERE (arithmetic, rational enclosures) | §1.4 (d); s2_55_1 C6 |
| 9 | The "local log-scale derivative" is −B_T × (s̄-image); identifying it with B_loc is circular | PROVEN-HERE | §1.4 (e) |
| 10 | Lemma REG: sector analyticity ⇒ |(uϑ)′| = O(g²), κ_W ≥ ½, global ODE solvability, SA-K class | PROVEN-HERE | §1.5 |
| 11 | Proposition CL: variable-coefficient content from the tilted form | PROVEN-HERE (implication) | §1.6 |
| 12 | What clause (a) consumes (seven named inputs; b_∞, LCS-b not consumed) | ARGUED (proof plan) | §1.7 |
| 13 | Product conditions (P-sc), (P-tl) with the log budget | PROVEN-HERE (sufficient-condition bookkeeping); O(1) expectation ARGUED | §1.8 |
| 14 | Seam operator classification: no d ≤ 3; gluing positive relevant; d = 4 irrelevant; no tuning | PROVEN-HERE (symmetry/dimension, single-connection local class); nonzero d = 4 tree coefficients ARGUED | §2.1 |
| 15 | Tower lemma | PROVEN-HERE | §2.2; s2_55_2 G1, Y1 |
| 16 | Theorem N5′ | CONDITIONAL (implication PROVEN-HERE) | §2.3; s2_55_2 G2-G4 |
| 17 | Content of N5-T*: (α)-(δ); rough-data part weak-coupling and shared | ARGUED | §2.4 |
| 18 | Wild crossing data absorbed by the soft kernel; design check on κ_K at seam links | ARGUED (energy comparison, E1) | §2.4 (γ) |
| 19 | No counterexample among nine candidates (Q3, Q4 not realised) | ARGUED (list) | §2.5 |
| 20 | H_Euc (sphere) as an implication with inputs, owners, status | assembly of cited implications | §3 |
| 21 | Checks: s2_55_1 6/6 PASS, 6/6 controls fired (run 2; run 1 FAILED C5/X5 from a symbol-assumption bug, recorded); s2_55_1b PASS, control fired; s2_55_2 4/4 PASS + non-vacuity, control fired | PASS (criteria first) | checks/s2_55_* |

**Counts (own claims):** PROVEN-HERE 11 (rows 1, 2, 4, 5, 8, 9, 10, 11, 13, 14, 15); CONDITIONAL 2 (6, 16); ARGUED 4 (12, 17, 18,
19); REFUTED (a suggested route) 1 (7). **Inherited (§4):** CONFIRMED 13 (H1, H2, H3, H5, H6, H7, H8, H9, H10, H12, H14, H15,
H16), NOT-VERIFIED 3 (H4, H11, H13), REFUTED 2 (H17, H18 — both agreeing with Codex, no new inherited refutation); Codex
F4/F6 agreements H19, H20.

**Check provenance.** s2_55_1_criteria.md (06:16:59Z) precedes s2_55_1.py (first written 06:18:35Z). Run 1 printed C5 FAIL and
X5 DID-NOT-FIRE because the series variable t (and λ) were declared complex, so sp.re(·) split t into re(t), im(t); the
output is kept verbatim as checks/s2_55_1_out_run1.txt. The fix (both symbols real; commented in the script) touched no
criterion; run 2 (06:19:36Z) PASSES all gates with all controls firing. For s2_55_1b and s2_55_2 the criteria file and the
script were written in one shell command, criteria first (same-second mtimes; the order is by command sequence). Every
verdict-bearing comparison is exact (sympy/fractions); the printed floats are display only.

---

## 6. Report to the lead (compact)

- **Model line:** claude-opus-5-5. Deliverable: this file; checks `checks/s2_55_1*` (measure term, scheme family, numbers),
  `checks/s2_55_1b*` (classical sign of the right half of Ξ_v), `checks/s2_55_2*` (tower lemma, N5′ decomposition on exact
  chains). All PASS with every control firing; s2_55_1's first run failed two gates through a symbol-assumption bug, kept
  verbatim as `s2_55_1_out_run1.txt` and fixed without touching any criterion.
- **LCS-a (task 1).** (i) **New exact identity (Proposition M):** the Jacobian of ROTDEF's lattice Lie derivative is EXACTLY an
  action-density source, −div Ξ_v = 2N C_F Σ_p(div v/4)(c_p)s(U_p), at every configuration (zero for rotations). Hence
  B_loc = C_F + u(ϑ^p_D − 4ϑ^p_1), and LCS-a is ONE SRC-M clause — the matching of the lattice Lie derivative of the plaquette
  action density, vector and trace components, tilted, all coarse fields, sector-analytic, with an integrated contact clause
  (§1.3). (ii) **The suggested route fails for LCS-a's core:** SA-K is tree level, and at tree level the trace coefficient is
  exactly C_F; it is scheme dependent (admissible Ξ′_λ: C_F − λ/N, any real number), while the Ward-profile coefficient is
  scheme independent given the Ward inputs and a nonvacuous dilation insertion; so the fluctuation part is O(1) and no
  tree-level computation identifies B_loc. Under the expected one-loop asymptotics the tree profile would be 8.07-10.77
  times too steep. The only "local log-scale derivative" of the effective action is the profile's own slope times the
  s̄-image (circular). (iii) **What Cauchy gives (PROVEN-HERE):** Lemma REG — sector analyticity ⇒ |(uϑ^p_R)′| = O(g²), κ_W ≥ ½,
  the Ward-profile ODE solvable on the whole [log a, log 2a] inside the domain (closes Codex SEAM F4's margin gap), profile in
  SA-K's class; Proposition CL — the variable-coefficient content is free once the clause is stated over SRC's polydisc.
  (iv) **Consumed by the core (§1.7):** source-inserted RG with the Lie-derivative insertion (per-step N5 covariance, N6,
  Theorem CE), a per-level marginal localisation (SRCCD55 (M4)), (Flow-an) ⟸ (F_R) ⟸ (UIR^♮) ⟸ (TC-b)_𝔍 + (ρ-null), per-step
  large fields conditional on the coarse field, all in the complex sector. Not consumed: b_∞, LCS-b, any one-loop number.
  (v) **Product condition (§1.8):** scalar remainder — integrated contact clause, contact coefficient → 0 or absorbed into
  Z_e(aΩ(x)); traceless channel — W1 must bound the S^(3,6′) insertion by o(log(ℓ_0/a)) (generic polylog SRC-κ weights give
  O(g²·log·𝔏), which does not vanish).
- **N5-T* (task 2).** Not proved; not a tuning problem and not infrared. (i) No seam operator of dimension ≤ 3 survives;
  dimension-4 seam operators have nonzero O(a·u) tree coefficients but are irrelevant on the 3-dimensional seam (marginal = 3):
  **no tuning**; the gluing operator (d = 2) is relevant with a positive coefficient (drives to the transparent defect).
  (ii) **Tower lemma (PROVEN):** sup_V|E[X|V] − c| ≤ sup_{U_k}|E[X|U_k] − c| — every all-coarse-field conditional-mean clause
  (N5-T*, SRC-E′_∞, W1/W3 coarse images, (L-b)) can be stated at any finer fixed scale; the top levels' law never enters.
  (iii) **Theorem N5′ (implication PROVEN):** N5 from (T-all)_J (N5-T* at every finer fixed scale) + (E′_J) + (D) (pure
  conditional decay below the top J levels, no transparency weighting). (iv) **Isolation:** N5-T* = small-field seam RG (α) +
  moderate-curvature BFT at weak coupling (β, shared: UNIV55 (N3)) + absorption of wild crossing data by the soft kernel
  (γ, ARGUED; design check: seam kernels must not be stiffer than the seam's crossing stiffness, κ_K ≲ (9/2)N in order of
  magnitude; a hard constraint would break the all-coarse-field form) + spontaneous large fields (δ, shared).
- **Assembly (task 3):** §3 table. First non-UV item: none. Most likely failure points: the separated-products → OS-algebra
  bridge; LCS-a's core with W1's log budget; the seam-specific (α), (γ); the shared (N3).
- **REFUTED items with corrections:** (a) the suggested SA-K + Cauchy identification of B_loc → B_loc = C_F + B^fl with an O(1)
  scheme-dependent split; the trace coefficient must come from a fluctuation (matching) computation; (b) [agreeing with Codex]
  SEAM55 DIAG paired hypotheses → Cartesian product; SEAM55 "iff" → "is ensured if". No new refutation of a banked item.
- **For PROOF.md / HANDOFF (sphere-route row):** tally unchanged. Replace "open: LCS-a (trace-channel matching)" by "LCS-a = one
  SRC-M clause (Lie derivative of the plaquette density with its trace component; SRC lane — SRC2_55's hierarchy should
  produce it); measure term exact (C_F); tree-level/SA-K cannot supply B_loc; W1 needs a log budget for S^(3,6′)"; replace
  "N5-T* (seam RG at rough coarse fields)" by "N5-T*: rough-data part weak-coupling and shared ((N3), RLF); seam-specific heart
  = small-field seam RG + wild-crossing-data absorption (κ_K design check); Theorem N5′ removes top-level decay". Bank
  candidates after Codex: Proposition M, the scheme family + constant-weight scheme-independence corollary, Lemma REG,
  Proposition CL, the tower lemma, Theorem N5′, the seam classification's symmetry/dimension part.
- **Codex verdicts used:** CODEX_REVIEW_SEAM F1-F12 — AGREE with all (F4's domain gap closed conditionally, F5/F6/F8 re-derived);
  CODEX_REVIEW_SPHERE F1, F2, F4, F5, F6, F8, F9, F11, F14, F15 — AGREE; CODEX_REVIEW_SRCAN items 1-4, 6, 7 — AGREE (item 3: no
  lower propagation bound used). No disagreement.

End of SPHERE2_55 (worker claude-opus-5-5), 2026-10-29 ≈06:3x UTC.
