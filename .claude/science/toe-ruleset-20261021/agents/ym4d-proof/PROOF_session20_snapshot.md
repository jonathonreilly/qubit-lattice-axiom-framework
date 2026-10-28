# YM4 existence via the Balaban RG: lemma ledger (sessions 1-20, 2026-10-26/28)

**Session-20 header (REVIEW_S18_S19 fixes; LINEAR_PACKAGE v1.1; (NA-H_loc) at level 1).** REVIEW_S18_S19.md (an independent
hostile review of sessions 18-19; it confirmed 71 / 2 / 7 / 24 + 1) is applied first; every fix is tagged **[R1819-fix]**
(pointer list at the head of [S20], end of file). Targets pre-stated in RTARGET.md §44 at 23:58 UTC (2026-10-27), before any
session-20 derivation; the c36 criteria before the c36 script. No REVIEW file or earlier snapshot was edited. All new items
are at the end of this file ([S20]) and unreviewed.
- **Fixes:** R_g orientations; gap sizes stated wherever N5-sf0's "gap" appears; N5-sf0 labelled an existence theorem;
  RW (iv) narrowed (bounds, holomorphy, 𝒞(1) = K^{-1/2}, decoupling; 𝒞(s)² is not a covariance); (NA-H_loc) presupposes the
  level-i minimiser; γ_i doubles (A_P ⊥ dλ); RLARGE F1/F2/G5 ((R1-loc) named)/compatibility; **W0-1: c35 C2 redone in exact
  rationals (c36 C PASS), so Lemma N5-w0's rate is now computer-assisted.** LINEAR_PACKAGE.md FROZEN v1.1 (errata only).
- **Proposition RW-ℓ² PROVEN** (no count change): λ_min ≥ γ'(1 - ε_R)/9 at every curvature-small background (was ≈ 4·10⁻⁵¹;
  now ≈ 6.6·10⁻¹⁰, within ×18 of γ').
- **Theorem NAH1 PROVEN** (with Lemmas U0, FPq, N5-an♭, BR1, SC1, LOC and Corollary N5-sf1): (NA-H_loc) at level 1 for the
  critical branch U(V) of the level-0 problem (exact lift + sup-norm contraction with N5-sf0's covariance; Hess E_1^br =
  F_BB - F_BACF_AB; localised covariance comparison), hence N5 at level 1. E_1^br = E_1^NA needs (MIN_1) ⊂ B-NA.
- **Constants level 0 → 1:** the measured trivial gap does not shrink (0.039849 → 0.039712, c36 D); the proven one shrinks
  once by 2c_E; the proven background threshold shrinks by ≈ 10⁻⁴⁰ per level in the per-level form (Proposition NAH-ind:
  NAH1-F4 occurs for the per-level induction; uniformity needs (BG-unif), multi-scale background regularity ⊂ B-NA).
- c36: A, C, D PASS; B FAIL as pre-registered at the larger background (t = 0.05 passes). **Tally after session 20:
  72 / 2 / 7 / 24 + 1.**


**Session-19 header (N5 at small-field backgrounds; the random-walk expansion).** Targets pre-stated in RTARGET.md §42 at
22:30 UTC, before any session-19 derivation; the c35 criteria before the c35 script. No REVIEW file, earlier snapshot,
LINEAR_PACKAGE.md or RLARGE.md was edited. All new items are at the end of this file ([S19]) and unreviewed.
- **Theorem RW PROVEN** (with Lemma CT♯ and Corollary RW-triv): a Dirichlet-compression random-walk expansion of K^{-1},
  (K + t)^{-1} and K^{-1/2} for any operator whose box compressions obey a Combes-Thomas bound; walk-length suppression
  ε_R^n with ε_R explicit; complex s-weakening with exact decoupling; locality of walk terms. At the trivial background it
  holds at every level i, uniformly in i, k, T.
- **Theorem N5-sf0 PROVEN** (with Lemmas N5-cov, AX, N5-an): N5 for the level-0 fluctuation operator at every background with
  plaquette curvature and soft fluctuation ≤ ε_* (curvature-only hypothesis; local axial gauges glued by the walk
  expansion), T ≥ T_0: gap, decay, ℓ²/ℓ¹, holomorphy on a complex neighbourhood, background-local walk terms. ε_* is explicit
  up to the analyticity constants r_*, S_* of Lemma N5-an (which exist, not computed); it is astronomically small.
  **[R1819-fix SF-2/SF-3] An existence theorem (r_*, S_* not computed). The "gap" proven in session 19 is ≈ 7·10⁻⁸²
  (product rule) or ≈ 4·10⁻⁵¹ (with N5-w0); session 20's Proposition RW-ℓ² raises it to ≥ γ'(1 - ε_R)/9 ≈ 6.6·10⁻¹⁰.**
- **Levels i ≥ 1:** Proposition N5-sf_i, an implication from (NA-H_loc) (a localised (NA-H) ⊂ B-NA, OPEN); not counted.
- **Target C:** Lemma N5-w0 (exact w at L = 3: ν_w = 30/13; computer-assisted level-0 rate m_cov^num = 1.9·10⁻¹⁰, ×4.9·10⁷)
  **[R1819-fix W0-1: in session 19 a numerical verification only; made computer-assisted in exact rationals by c36 C (S20)]**;
  no rigorous γ improvement; measured γ(Õ_0) = 0.0398 (2.5·10⁶ × γ_0) and γ^LB = 8.14·10⁻³ = 2c_E (6.3·10⁷ × γ_i).
- c35: A, B, C PASS. **Tally after session 19: 71 / 2 / 7 / 24 + 1.**


**Session-18 header (REVIEW_S16_S17 fixes; the large-field repair; LINEAR_PACKAGE frozen).** REVIEW_S16_S17.md (an
independent hostile review of sessions 16 and 17) is applied first; every fix is tagged **[R1617-fix]**. Targets were
pre-stated in RLARGE.md §13 at 21:47 UTC, before any session-18 repair text and before the c33 criteria. The session-16
wind-down plan was reversed by the owner on 2026-10-27 ("keep after it"; LOG session 18 records the source). No REVIEW
file or earlier snapshot was edited.
- **[R1617-fix] RLARGE.md repaired** (its session-17 text is kept as RLARGE_session17_snapshot.md). Theorem R1 (iii)'s B_4
  step re-localised on the unfattened supports of cluster tuples, so the family at a base point is genuinely permuted by
  B_4 (R-3b); cluster size bounds from (H-ch) (R-3a); torus wrap (R-4); TS's hypotheses on the region R1 uses, with
  g² < a''/3 (R-5); "remainder of irrelevant order" narrowed to BG-b-regular frozen data (R-6; in a sea sample the
  remainder is O(g²) and is re-extracted after the sea average); RLF amended in RLARGE §1A (two-threshold R-operation,
  Z_ref defined, (SF-last), complex fields; §1 kept verbatim, numbering unchanged, (RLF-5) added); the four unnamed
  inductive-step gaps named ((H-pos) [P], (H-Mayer), (W1-ret') with the re-extraction, (SF-last)); (P4) ARGUED; CL-1.
- **c33** (criteria first): B PASS (d = 4: the repaired localisation is invariant under all 384 elements of B_4, the
  session-17 one is not); A FAIL as pre-registered on one seed (a double-precision cancellation in the brute-force
  logarithm; a 40-digit post-run diagnostic confirms the identity), with the invariance criteria A2/A3 holding.
- **LINEAR_PACKAGE.md: all REVIEW_S16_S17 fixes applied; FROZEN v1 (2026-10-27).** Its session-16 text is kept as
  LINEAR_PACKAGE_session16_snapshot.md.
- **[R1617-fix 10] Tally:** the review's corrected count after session 17 is **67 / 2 / 7 / 24 + 1** (TS/R1 at GAP). With
  R-3a, R-3b, R-4, R-5 written, TS/R1 is counted again (PROVEN-HERE [S18-repair], unreviewed): 68 / 2 / 7 / 24 + 1.
- **N5 at the trivial background [S18]** (target pre-stated in RTARGET §40): Theorem N5-triv PROVEN (unreviewed), at the
  end of this file; check c34 PASS. **Tally after session 18: 69 / 2 / 7 / 24 + 1.**

**Session-16 header (wind-down session 1 of 2 for the linear/abelian package).** REVIEW_S15_CONVERGENCE.md (an
independent hostile review of session 15 plus a convergence audit of sessions 5-15) has been applied first; every fix is
marked **[R15-fix]**. Session-16 additions are marked **[S16]** (in L5, with notes in L2, the (DF) sub-DAG and the tally).
Targets were pre-stated in RTARGET.md §38 at 20:26 UTC, after the lead's exploratory reasoning and before any written
session-16 derivation or check script; the c31 criteria were written before the script. No REVIEW file or earlier
snapshot was edited. No new SU(N) obligation is opened (owner decision 2026-10-27, as relayed by the session brief).
- **[R15-fix] Fixes 1-6 applied.** (1) Theorem G♯_0-soft: the "attained by coherent sources" and "supplied by the soft
  remainders" sentences labelled ARGUED. (2) Proposition NA-lev: headline narrowed everywhere to "the top-level per-step
  defect has no n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA" (this header, the S15 header, L2, L5
  (a) and (d), the tally; LOG l.729 and RTARGET §37 annotated, not edited); Def indexed by coarse links (81 holds either
  way); explicit smallness η̄ ≲ 1.9·10⁻⁷ (κ ≡ 1, δ_H = 0; c31 E3). (3) (G♯_0-fine): k ≥ 3 needed for LES-div at R = n, with
  the k = 1, 2 cases handled by a finite-scale bound; (G♯_0-fine-up) stated as a displayed inequality. (4) RTARGET §37
  annotated. (5) c31 E: Lemma E-low instances (symbol level: the exact minimum is 7.3-9.1 × c_E; chain level ≥ 7.3 × c_E).
  (6) LOG l.666 and l.700 annotated. No status changes.
- **Lemma F-df_0: PROVEN [S16].** The fine-curvature response f_0 of the linearised chain has an exponentially local
  representative as a function of the coarse curvature F on ALL 2-forms: |K| ≤ (2M/(m_*' - m'))e^{-m'|X|_1} for every
  m' < m_*', uniformly in k, T, u. Mechanism: the analytic B_k-symbol 𝔅 of f_0 satisfies 𝔅·ν = 0 (gauge invariance), and
  an explicit analytic Koszul factorisation 𝔅 = h∘(ν∧·) with one-variable divided differences in e^{ip_α} - 1 keeps the
  strip. So both gauge-invariant outputs (r_{k-1}, f_0) have exponential F-kernels. c31 F PASS (identity ≤ 5e-16).
- **LINEAR_PACKAGE.md [S16]**: the self-contained write-up of the linear/abelian package (setting, statements with exact
  hypotheses and constants, proofs or pointers, check inventory, what it is not, open items with paper/session weights).
- **Governance correction [S16].** REVIEW_S15_CONVERGENCE (c) reads the owner's order "Balaban Z^4 standard first, then
  D4" as hard-constraint first; the owner's meaning is the Z^4 LATTICE before the D4 lattice (session brief, 2026-10-27).
  Decision 4 (soft vs hard kernel) is not covered by that order either way. Recorded in LOG session 16.
- c31: E PASS; F PASS.
- **Tally:** 63/2/7/24 + 1 (after fixes, unchanged) → **64 / 2 / 7 / 24 + 1 comparison-branch** (+F-df_0).

**Session-15 header.** REVIEW_S13_S14.md (an independent hostile review of sessions 13 and 14) has been applied first;
every fix is marked **[R1314-fix]**. Session-15 additions are marked **[S15]** (in L5, with notes in L2 and the tally).
Targets were pre-stated in RTARGET.md §33-36 at 19:29 UTC, after the fixes and the lead's exploratory reasoning, and
before any written session-15 derivation or check script; the c30 criteria were written before the script (one
pre-script correction, disclosed). No REVIEW file or earlier snapshot was edited.
- **[R1314-fix] All 13 binding fixes applied.** Scope residues (l.634-636 "levels n ≥ 1"; the S12 header's "non-analytic
  part" annotated as superseded by N2-exp); valid (η, r_0) pairs for N2-exp (0.0111 at r_0 = 0.57; 0.0077 at 0.37; 0.0117 at
  0.65; κ̂ = 16: 0.0037, 0.0082) with the f_0 "≤ 0.15φ" condition in η_*'s definition, and for N2-exp' (0.0384 at 0.70; 0.0273
  at 0.37; 0.0306 at 0.90; κ̂ = 16: 0.0140, 0.0226, 0.0216), all verified in 30-digit arithmetic (c30 A); the periodicity
  step replaced by the periodic-meromorphic + Riemann-extension argument; "true rate" → "located rate (numerical, not
  proven)", fit ranges 0.93-0.97 / 0.88-0.93; "what N6 consumes" labelled ARGUED, with the new OPEN Lemma F-df_0; NA-alg (b)
  given ||ρ||_op < 2π/N; NA-FP scoped to the Hessian (Gaussian) level, its composite linearised covariance and composite
  onto-ness written out; SRC-id's f_0 half written out (c30 B); B-NA-red's (FP♯) replaced by the combined (FP♯') with the
  Lagrange step (Lemma NA-crit'), its norms fixed by RTARGET §33; BNA-F2 labelled argued; RTARGET §32 annotated (§27
  partially met, §29(a) met except background independence, §30 values); c29's tolerance record appended. **The m_*' value
  becomes 0.0384 (was 0.0385); no status changes; tally after fixes 60/2/7/24 + 1, unchanged.**
- **(G♯)_0, soft half: PROVEN [S15]** (Theorem G♯_0-soft, with Lemmas SRC-all, REC, KF). For divergence-form sources at
  every level (j_l = d^*G_l), in exponentially weighted coarse-unit sup norms with level weights ω (RTARGET §33):
  ||r||_{X_s} ≤ C_s(Ω||G||_Y + ||B_k||_D), uniformly in k, T, with explicit C_s in terms of N2-exp's M. Mechanism: Green
  reciprocity makes the source-to-r map the transpose of the proven exponential data-to-curvature maps. G0-F1 occurs: each
  source level contributes O(1), so Ω = Σω_l^{-1} < ∞ is needed (the marginal count; supplied by the irrelevant soft
  remainders at levels ≥ 1).
- **(G♯)_0, fine half: reduced [S15].** Lemma LES-div (lattice Campanato step with divergence-form source) PROVEN; with it,
  the fine-curvature Hölder bound for level-0 sources reduces to a local-energy input (LED-src), OPEN. Sources at levels
  ≥ 1 reach the fine level through rough transports: a separate OPEN item. G0-F2 occurs (no sup-only bound); G0-F3
  undecided.
- **[R15-fix: headline narrowed; was "NA-F2 is an artefact of the direct n = L^k step"] The top-level per-step defect
  has no n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA [S15]** (Proposition NA-lev, with Lemma E-low).
  N4's fluctuation operator is the one-level operator (n = L) with fine energy E_i. Its soft defect (indexed by coarse
  links) obeys ||Def||² ≤ 81(5L - 4)(e^{2η̄} - 1)²||A||² with no n; E_k ≥ c_E||dB_k||² (c_E ≈ 0.0041 at κ ≡ 1) gives the
  per-level abelian gap. The (NA) gap is OPEN through (NA-H) (the SU(N) Hessian of E_i, the Schur complement over all
  finer levels, inside B-NA) and a written per-block perturbation; explicit smallness η̄ ≲ 1.9·10⁻⁷ (κ ≡ 1, δ_H = 0).
- **(R♯) stated precisely [S15]** in the §33 norms ((R♯_ω): divergence-form plus a plain level-0 current, ω_0 = 1,
  ω_l = L^{θ(k-l)}); argued, not proven.
- c30: A PASS; B PASS; C PASS; D informational.
- **Tally:** 60/2/7/24 + 1 → **63 / 2 / 7 / 24 + 1 comparison-branch** (+G♯_0-soft, +LES-div, +NA-lev; no OPEN item is fully
  discharged; new OPEN sub-items recorded: F-df_0, G♯_0-plain, LED-src, G♯_0-fine-up, NA-H).

**Session-14 header.** No review of session 13 exists yet (the [S13] order's item 1 is carried). Session-14 additions
are marked **[S14]** (in L5, with notes in L2, L3g(a)-slice, the (DF) sub-DAG and the tally). Targets were pre-stated
in RTARGET.md §27-31 at 17:32 UTC, after the lead's exploratory reasoning and two scratch arithmetic probes for target D
(scratchpad dconsts*.py; not checks), and before any written derivation or check script. The c29 criteria were written
before the script. No REVIEW file or earlier snapshot was edited.
- **B-NA is NOT closed; it is reduced [S14].** Proposition B-NA-red (a proven implication with explicit threshold
  ε_0 = min(ρ_0/(2(1 + G_D)), 1/(16GC(1 + G_D)²), 1/(10G_wC_w(1 + G_D)))) derives the SU(N) chain's critical point,
  its second-order distance from the linear one, and the decay of its response at every rate m ≤ m_G, from two inputs
  that are OPEN: (G♯) a multi-scale Schauder-type bound for the gauge-fixed linearised chain on general sources, and
  (R♯) the remainder bound in the same norms. Failure modes [R1314-fix: BNA-F1 and F3 established, F2 argued (scaling
  count)]:
  - BNA-F1: N2-lin/N2-exp control only the B_k-data kernels, and the non-linear remainder is a general source;
  - BNA-F2: in coarse-unit sup norms the fine-level Wilson remainder scales like nX² (scaling count), so a Schauder
    pair (C^{1,α}/C^{0,α}) is needed;
  - BNA-F3: the complete local (block-axial) gauge moves the coarse field onto sparse crossing links, so the gauge must
    be the smooth covariant multi-level slice, whose (G♯) contains a multi-level physical gap.
  Proven ingredients: Lemma NA-alg (explicit su(N) polar-maximiser and soft-density bounds), Lemmas NA-crit and
  NA-inv, Proposition NA-IFT, and Lemma SRC-id (a fine source acts as the effective datum -Q^{(k)}Δ^{-1}j, and the
  K = 0 symbol's 1/φ cancels exactly by screening, β - κ|W|² = φR). The SU(N) N2-E / N2-lin / N2-exp analogues are
  conditional on (G♯), (R♯), (FP♯) (not counted).
- **(NA) for N4: identity half PROVEN, gap OPEN [S14].** Proposition NA-FP [R1314-fix: an identity at the Hessian
  (Gaussian) level at a critical background, invariant under the LINEAR action A ↦ A + D_Uλ; not the non-linear
  Faddeev-Popov identity, whose determinant depends on A]: at every critical SU(N) background the
  Hessian annihilates the covariant gauge directions D_UΛ (NA-inv), the covariant slice functional h_U obeys
  h_U(D_Uλ) = M_Uλ - λ(c) exactly, χ_U = (h_U, P_res^UD_U^*) is admissible for EVERY background, and FP-ab applies
  verbatim; the composite slice too. New: the Faddeev-Popov constant FP_U depends on the background. The (NA) gap is
  OPEN: the linearised soft residual contains a defect, a |f|-weighted average of individual far-root funnel traces
  that the slice does not kill and that costs ε^{-1}||∇A||² (NA-F2). Two routes are recorded.
- **m_* is 3.5× sharper [S14]** (Theorem N2-exp', Lemma EXP-strip'): the first-order changes of the real-on-R blocks
  are imaginary, so the lower bounds move at second order. m_*' = 0.0384 at L = 3, κ ≡ 1 (0.0273 at κ = 0.25, 0.0306 at
  κ = 4) [R1314-fix: rounded down to values valid at the stated r_0; c30 A]; N6's block size M ≳ 457/m_*' ≈ 1.2·10⁴ (was 4.1·10⁴). The located rate is still ≈ 25 times larger.
- c29: A PASS; B PASS; C VALID (C1 FAILED as pre-registered on a size threshold, D(0.1) = 0.110 > 0.1, with the
  predicted O(t) scaling, slope 1.04; C2 PASS: the non-abelian response part decays at 0.78 of the linear rate); D PASS.
- **Tally:** 57/2/7/24 + 1 → **60 / 2 / 7 / 24 + 1 comparison-branch** (+NA-alg, +NA-FP, +SRC-id; N2-exp strengthened
  to N2-exp' without a count change; no OPEN item is fully discharged).

**Session-13 header.** REVIEW_S11_S12.md (an independent hostile review of sessions 11 and 12) has been applied first;
every fix is marked **[R1112-fix]**. Session-13 additions are marked **[S13]** (in L5, with notes in L2, L3g(a)-slice,
the (DF) sub-DAG and the tally). Targets were pre-stated in RTARGET.md §24-25, after the lead's exploratory reasoning
(on paper) and before any written derivation or script; the c28 criteria were written before the script, with one
pre-script addendum (disclosed). No REVIEW file or earlier snapshot was edited.
- **[R1112-fix] All 11 binding fixes applied.** The Dimock citation (§4.7, l.1672); an appended annotation in
  checks/c21_criteria.md withdrawing the "is false" reading; decision 4 labelled "by inference from" the TOE-ruleset
  delegation, with the reason the "(put it in the CL …)" parenthesis is read as governing TOE rules, not proof methods;
  CE-geo' narrowed to the upper inequality of (122) (Dimock: d = 3); N2-a's SU(N) statement made set-valued; Lemma WA
  for every a > 0 and the p = 0 remark replaced by F̂(0) = 0; "only power-tail bounds"; the BG-b scope (levels n ≥ 1,
  small coarse curvature) and "for the linearised chain" restored in the header, N2 status and tally; PG-ext's
  "Collect" split written out (4.241·10⁵, 160); the c26 c/T fit labelled informational; the N2 kernels vs the N5
  covariance kept separate. No status changes.
- **N2-exp is PROVEN [S13]** (Theorem N2-exp): the linearised soft-chain response is exponentially local, uniformly in
  k and T. The 1/φ of the fine Green's function cancels exactly in every response symbol (Lemma EXP-id), so 𝓡̂ and the
  B_k-symbols of r and f_0 are analytic near p = 0. Explicit perturbation bounds (Lemmas EXP-real, EXP-strip) give a
  strip of width m_*(L, κ_±) > 0: m_* = 0.0111 at L = 3, κ ≡ 1 (crude). The nearest complex singularity, located
  numerically, gives the located rate (numerical, not proven) [R1314-fix: was "true rate"] ≈ 0.98 (≈ √κ scaling).
  - Exponential: F ↦ r on all 2-forms; B_k ↦ r and B_k ↦ f_0. Not exponential: the unrestricted f_0 extension
    (|x|^{-4}) and the session-12 F-representative 𝒦̂_u + Π_coex (power tail seen). N6 consumes the B_k-kernels.
  - Decision 4: failure mode EXP-F1 does not occur; nothing to flag against the soft kernel from the linear response.
  - c28: A VALID; B FAILED as pre-registered on a float tie at the sharp point p = 0 (β_μ(0) = b_* exactly; -5.6e-16);
    C1, C2 PASS; C3, C4 FAILED as pre-registered (pre-asymptotic fit window); D PASS.
- **(IT') is PROVEN [S13]** (Lemma IT-line, Proposition PG^{(k)}): the composite slice functional obeys
  ε²|h^{(k)}|² ≤ (4L²/(L - 1))||A||²_B with no trace loss, so the physical gap holds for the composite slice,
  C_IT(3) ≤ 3.6·10⁶, uniformly in k and T.
- **Tally:** 55/2/7/24 + 1 after the fixes (unchanged) → **57 / 2 / 7 / 24 + 1 comparison-branch** (+N2-exp,
  +PG^{(k)}).

**Session-12 header.** No new review file exists, so session 11 is still unreviewed. Session-12 additions are
marked **[S12]** (in L5, with notes in L2, L3g(a)-slice, the (DF) sub-DAG and the tally). Targets were pre-stated in
RTARGET.md §20-22: after the lead's exploratory reasoning in this session, but before any written derivation and
before any script. The c26/c27 criteria were written before the scripts. One c26 addendum was written after Parts A-B
and before Part C was coded (disclosed). No REVIEW file or earlier snapshot was edited.
- **[R910-fix13] Decision 4's delegation, quoted.** The owner's words, as recorded in the lead's memory file
  feedback_no_permission_except_axioms.md, are now in the decision-4 record (session-9 header). Label: decision 4 is a
  proof-technique choice made by the lead, applied BY INFERENCE from the owner's TOE-ruleset delegation [R1112-fix]; it
  is not an axiom or CL change (reason in the session-9 record).
- **N2's linear half is complete [S12].** Theorem N2-lin proves (H2) sup|r_{k-1}| ≤ C_R sup|dB_k|, (H1)
  sup|f_0| ≤ C_f sup|dB_k| and (LED), uniformly in k and the torus. The route has three parts:
  - Lemma IT-str: a composite of straight averages is the direct straight average;
  - Lemma LED-dual: the minimiser is determined by its co-closed top residual r, which minimises ½⟨r, Pr⟩ + ⟨r, B_k⟩
    with P = Σ_m(κ-ratios)Q^mQ^{mT} + κG_k, and E_k = (κ/2)⟨r, Pr⟩;
  - the explicit coarse symbol of this problem (Lemma LED-symb), whose non-analytic part at p = 0 is homogeneous of
    degree 2 (for r) or 1 (for f_0, after adding Π_coex, which vanishes on closed data), so the kernels are ℓ¹
    (Lemma WA, Proposition LED-unif). [R1314-fix: superseded by N2-exp [S13]: "degree 2/1" is an upper bound on the
    regularity loss only; the r and B_k-symbols are analytic (N2-exp); only F-representatives of f_0 carry a
    non-analytic term.]
  So BG-b holds for the linearised soft chain with no further hypothesis [R1112-fix: scope restored] for the levels
  n ≥ 1 (the n = 0 term needs the current step's residual) and at small coarse curvature (BG-b (b1) needs
  M_2 ≤ ε_*).
  - c26 A: every identity holds to ≤ 4e-13 against the LSMR chain (d = 2, 3, 4).
  - c26 B/C: the kernel norms are k-stable (N_r → 2.727; N_f^rep → 10.25).
  - Q7 FAILED as pre-registered: the T-growth ratio was 1.104 against 1.1. The increments fit a summable c/T tail.
- **The N4 physical gap is PROVEN [S12]** (Proposition PG): ||dA||² + κ||QA||² ≥ c_PG||A||² on Phys, with
  c_PG = min(1, κ)/(3.5·10⁶), uniformly in n and T, so O_FP ≥ min(c_PG, 4) on H_0. Three ingredients:
  - the exactly co-closed face fluxes control the coarse co-closed part;
  - the root components cost only the point capacity, 8ε²;
  - the line trace of h loses only ε^{-1}.
  c27: identities and constants PASS. E3 FAILED as pre-registered: one sub-check's normalisation is ~0/0 on the
  pure-gauge vector; the absolute error is 1e-15.
- **Not attempted:** B-NA (RTARGET §22).
- **Tally:** 53/2/7/24 + 1 → **55 / 2 / 7 / 24 + 1 comparison-branch** (+N2-lin, +PG).


**Session-11 header.** REVIEW_S9_S10.md (an independent hostile review of sessions 9 and 10) has been applied first.
Every fix is marked **[R910-fix]**. Session-11 additions are marked **[S11]** (in L5, with notes in L2, L3g(a)-slice,
Theorem CE, the (DF) sub-DAG and the tally). Targets were pre-stated in RTARGET.md §16-18 before the derivations; the
c23/c24/c25 criteria and the c21 addendum were written before the scripts. No REVIEW file or earlier snapshot was edited.
- **[R910-fix] All 13 fixes applied.**
  - **Proposition CE-κ is a quantifier-order remark.** Dimock's statement places c_0 = c_0(d) before κ, while his own
    proof (p.40) notes "(So c0 does depend on κ.)"; his paper fixes κ, so none of his results is affected. Every
    "Thm 27 is false" phrasing is withdrawn (header, L5, tally, RTARGET §15; LOG gets an appended correction).
  - The touching-tree reading of (119) is stated, with why (305) and (122) presuppose it. The Möbius step is
    replaced by the six-bond finite-difference argument (c21 I4: exact to 60 digits).
  - "Discrepancy 2" is retracted: Dimock's polymers are face-connected, so it is a definitional difference. The c21
    value at h = 0.01 is corrected (1.0003 was noise; 0.9997 in 60-digit arithmetic). c21 is re-run with a
    bound-check print: 14/14.
  - Constants and scope: the CE-cx inherited constants; N6's κ requirement; BG-b-lin's factor 2, its n = 0 edge case
    and the κ̂/κ_{k-1}-only constants; "for every critical point" deleted in CR (ii); LES small radii; "iff" → "if"
    in BG-sum; "(linearised)" in the elliptic-gap scope.
  - **D4-obs is a new OPEN item.** (DF3') gets its Cauchy margin and the |t| ~ 1/g remark. B-NA (iii) must be
    reconciled with the R3-fix.
  - Checks: c20's pre-run edit is disclosed; c22's Q2 non-discrimination at t ≤ 0.1 and its non-t² deviations are
    stated, and the "S is a maximum" explanation is labelled unverified. Decision 4's delegation in the owner's
    words was not available in any file read; the honest label stands.
- **N2, linear half [S11].** The reviewer's first lemma holds. The top residual and the fine curvature are bounded by
  the coarse CURVATURE, not by the field size:
  - Lemma N2-a, exact: they are functions of the gauge orbit and vanish on every flat class, for the abelian and the
    SU(N) chains;
  - Lemma N2-E, quantitative: E_k ≤ C_E(1 + κ_+)||dB_k||², uniformly in k and the torus, via a cubical-Whitney test
    chain and the centring cancellation of CR (ii); this gives the ℓ² forms of (H1) and (H2);
  - Proposition N2-red: (H1) + (H2) in sup form ⇐ (LED), a local energy bound, with Lemma LES-sup.
  (LED) is not proven. The failing step is named: the per-level cutoff commutator is marginal in d = 4. c23: in Part B
  (SU(2)) a large pure gauge leaves R_top unchanged to 9 digits, and a flat field of size 1.1 times the data changes
  R_top by 8% (Q4-Q6 PASS); in Part A, Q1/Q2 PASS and the pre-registered Q3 FAILED on its design (the values
  decrease in k).
- **N4, abelian [S11].** Lemma FP-ab and its application. The legitimate fixed-b gauge fixing is δ(h) plus a Feynman
  term on the residual group Λ_res, with an A- and b-independent constant. L3g(a)-slice's double fixing with the full
  Δ is NOT an identity: it carries an explicit Gaussian weight in 2N_c - 1 coarse divergence moments. The uniform gap
  of the legitimate operator ⟺ a physical gap on Phys (OPEN). c24: the gap is positive at every tested size (0.27-0.43
  vs 1.0 for the Δ version).
- **κ_0 [S11].** Lemma CE-geo': |X| ≤ 2^d + 2^{d-1}√d·d(X) (d = 4: 16(1 + d)), proving the upper inequality of
  Dimock's (122) (there d = 3) in stronger form [R1112-fix]. Hence κ_0 = 16 log 12800 ≈ 151.3 (was ≈ 3064), and N6 must deliver κ > ≈ 457 (was ≈ 9.2·10³). c25: no
  violation in 6045 instances.
- **Tally:** 49/2/7/23 + 1 → **49/2/7/24 + 1** after the fixes (+D4-obs) → **53 / 2 / 7 / 24 + 1 comparison-branch**
  after session 11 (+CE-geo', +N2-E, +N2-red, +FP-ab).

**Session-10 header.** No review file was produced after session 9, so this session has no review fixes; the
session-9 order's item 1 (a hostile review of session 9) is NOT done here and is carried, and no REVIEW file or earlier
snapshot was edited. Session-10 additions are marked **[S10]** (all in L5, plus notes in L2 and the tally). Targets were
pre-stated in RTARGET.md §12-14 before the derivations, and the c21/c22 criteria files were written before the scripts.
- **Theorem CE [S10] (PROVEN-HERE): Dimock I Thm 27, re-verified in corrected form.** The full proof is written with
  explicit d = 4 constants:
  - κ_0 = 324 log 12800 ≈ 3064 and K_0 = e^{κ_0/4}/6400 ([S11]: sharpened to κ_0 = 16 log 12800 ≈ 151.3,
    K_0 = e^{κ_0}/6400, by Lemma CE-geo');
  - c_0(κ) ∝ e^{-2κ}, with a κ-independent prefactor C_1.
  It includes the tree-graph bound (323) (Lemma TG, Penrose partition, with a complete proof) and a rigorous
  formal-series → analytic-identity step. **Proposition CE-κ [R910-fix]: a quantifier-order remark.** Dimock's statement places
  c_0 = c_0(d) before κ ("a constant c0 depending only on the dimension"), while his own proof (p.40) notes "(So c0
  does depend on κ.)"; his paper fixes κ, so none of his results is affected. Proposition CE-κ (a nearest-neighbour
  Ising instance, under the touching-tree reading of (119) that Dimock's (305) and (122) presuppose) shows that the
  κ-dependence is necessary. Four textual discrepancies (1, 3, 4, 5) are repaired, and one definitional difference is
  recorded (our *-connected polymers vs Dimock's face-connected ones); none affects the uses. c21: 13/13 PASS
  (14/14 after the [S11] reporting fix and the new exact check I4).
- **BG-reg [S10]: narrowed to the membership hypotheses (H1) + (H2).** PROVEN-HERE:
  - Lemma LES: the lattice elliptic step, Hölder-α Campanato form;
  - Lemma CR: constant reproduction;
  - Lemma J-str: at critical points of the soft chain, the S4' funnel part of the soft current vanishes EXACTLY, and
    the fine current is bounded in coarse units by the top residual, uniformly in the depth;
  - Proposition BG-b-lin: BG-b for the linearised soft chain ⇐ (H1) fine-curvature sup + (H2) top-residual sup, the
    soft analogue of CMP 109 (1.2).
  The non-abelian transfer is argued (via A1-NA(1) and BCH). c22 (SU(2), 4D, one-step soft minimiser): VALID; the Noether identity and the absence of funnel concentration in the soft current hold (Q1, Q2 PASS); the non-abelian deviations from the linear regime are ≤ 8% up to t = 0.4, but the pre-registered monotonicity sub-criterion Q3 FAILED.
- **(DF) sub-DAG [S10].** The remaining wall of W1-loc and BG-reg is exactly {N2 soft L2 with (H1)/(H2), N4 (FP), N5
  soft covariance, N6 soft polymer bound}. (DF3') ⇐ (DF1) + Theorem CE + an ℓ¹ covariance bound (argued).
- **Tally:** 46/2/7/23 + 1 → **49 / 2 / 7 / 23 + 1 comparison-branch** (+Theorem CE, +Lemma LES, +Proposition
  BG-b-lin).

**Session-9 header.** REVIEW_S7_S8.md has been applied first; every fix is marked **[R78-fix]**. Session-9 additions
are marked **[S9]**. Targets were pre-stated in RTARGET.md §9-10 before the derivations.
- **Decision 4 is MADE [S9]** (by the session-9 lead, under authority delegated by the owner; not an owner ruling and
  not a CL or axiom change). The lane KEEPS S4'-contour averaging with the SOFT gauge-covariant constraint as its RG
  transformation (precise kernel: L5 [S9], Lemma D4-norm). Balaban's (0.4) with the hard δ(M(U)V^{-1}) constraint is a
  **comparison branch**, not on the critical path. Consequences: L1e-(0.4) and W3 move to the comparison-branch list
  (listed, not counted as blocking OPEN for the main theorem); the main theorem must be proven for the soft-constraint
  RG, so every statement imported from Balaban's hard-constraint papers (L1d, L2, L3g, L4a, L5, L6) must be re-verified
  for the soft version before it can be load-bearing.
  - **[R910-fix13] (session 12) The owner's delegation, quoted.** Source: the lead's memory file
    feedback_no_permission_except_axioms.md, read in session 12, which records dated owner messages. These are the
    owner's words as recorded there; no primary transcript was read here.
    - Owner, 2026-10-21: "you dont need to ask permissions unless we are editing the axioms".
    - Owner, 2026-10-23: "remember that you can set whatever works for the TOE here, you dont need to ask me (put it in
      the CL until we have a working TOE)".
    - **Label.** Decision 4 is a proof-technique choice (which RG kernel the existence proof uses), made by the lead
      and applied **by inference from** this standing delegation [R1112-fix]: the delegation, as recorded, is for "the
      TOE ruleset work" and the CL register; it does not literally name proof-method choices, and extending it to one
      is the lead's inference. It is not an axiom change and not a CL change: nothing about it was added to the
      CL register, since it chooses a method of proof, not a rule of the TOE. It is not an owner ruling on decision 4
      itself.
    - **[R1112-fix] Why the 10-23 parenthesis "(put it in the CL until we have a working TOE)" is not applied.** That
      parenthesis is read, deliberately, as governing rules of the TOE (the things the CL register holds: candidate
      laws the physics is built from). Decision 4 changes no physical rule: the continuum theory sought (4D SU(N)
      Yang-Mills) is the same under either RG kernel, and the kernel is a device of the proof. So it is recorded here,
      in the proof ledger, not in the CL. This is a reading of the owner's words, not something the words state; if
      the owner reads the parenthesis as covering method choices, the record moves to the CL with no change of
      content.
- **[R78-fix]** All nine REVIEW_S7_S8 fixes applied: 2D wall cost a ≈ ε_1² with window ε_1 ≲ (4π/(N-2))^{1/2}; O(3)
  lattice-dislocation caveat; R2D-iso's A_B on the exterior-ring (Γ-Γ) bonds; new OPEN item BG-reg and the
  [conditional on BG-reg] tags; W1-sym/W1-red/W1-loc seam fix; W1-loc restated (polynomial g-loss, direct Φ_0 terms);
  headers; c18c sentence removed; c19's 20 → 5 Ad-element edit disclosed. **c19b** (reflection-odd control, criteria
  first): 5/6 — the point of the control holds (c_SD = +2.000, c_ASD = -2.000: without reflections a second invariant
  appears), and the pre-registered s²-rate window Q3 FAILED (convergence is clean, but the rate ratio is outside
  [3, 5] at s = 0.2 on three backgrounds).
- **BG-reg [S9]: part (a) discharged, part (b) narrowed.** Lemma GT-lat and Proposition R4D-lat (PROVEN-HERE): the
  lattice Taylor lemma with gauge-invariant lattice parameters (ε_2, ε_3, ε_V) replaces the smooth s-families. No
  interpolation lemma is needed. Lemma BG-sum (arithmetic): the level-summed remainder is bounded if [R910-fix: was "iff (sufficient)"; BG-sum proves sufficiency only] the
  background obeys BG-b = sup coarse-unit curvature + summable mean oscillation over sub-cubes. BG-b is the
  U_k(ε_0)-membership half of L2 (CMP 109 (1.2): curvature AND |J| < ε_0), plus a lattice elliptic step; for the
  soft-constraint S4' minimiser it is not proven. Check c20 (criteria first, linearised abelian 2D model): VALID;
  the S4' soft background classifies SUMMABLE (mean-oscillation ratio ≈ 1/L, no axial concentration).
- **W1-loc (4D) [S9]: reduced.** Lemma W1-size' (PROVEN-HERE): an exact size reduction to the holed sea, with no
  released-measure probability. Under the Dimock-form hypothesis (DF) for the holed sea and Dimock I Thm 27, (LD) follows
  (Anderson sub-Gaussianity of truncated Gaussians, proven here, plus a tilt argument). (cl) is argued via localisation
  with a corridor of width O(log 1/g), which costs only a polynomial g-loss. **Exact remaining wall for W1-loc:**
  (DF) = the small-field package (L2 background with decay, L3g covariance with random-walk expansion, gauge fixing,
  L4a-form polymer bound) for the soft RG, together with re-verifying Thm 27 (its tree-graph bound (323) is stated
  without proof in Dimock I).
- Lemma **D4-norm** (PROVEN-HERE): R4D-iso holds verbatim for the normalised soft kernel, the exact RG step.
- **Tally:** 43/2/7/24 after the review (adds BG-reg) → **43/2/7/23 + 1 comparison-branch** after decision 4 →
  **46/2/7/23 + 1 comparison-branch** after session 9 (+GT-lat, +D4-norm, +W1-size').

**Session-8 header.** Session-8 additions are marked **[S8]** (all in L5). Targets were pre-stated in RTARGET.md §5-7
before any derivation. No review file was produced after session 7, so there are no review fixes in this session.
- **Lemma GT** (gauge-invariant Taylor lemma): for every gauge-, B_4- and ι-invariant C⁶ function of lattice data along
  a smooth radial-gauge background, order s² vanishes (semisimplicity), odd orders vanish (ι), and order s⁴ is
  c·Σ||F_μν(0)||² (Λ²R⁴ is absolutely irreducible under B_4; no ε·F·F term). PROVEN-HERE.
- **Proposition R4D-iso** (moved from OPEN): one isolated 4D SU(N) cube, frozen exterior, soft constraint, plaquette
  cut priced by inequality (B): ρ = ρ_0 + δβA_B + O(e^{-a/g²}s⁶), a < ε_1²/(4N), s_0 g-independent. PROVEN-HERE, met as
  pre-stated. For isolated cubes **on smooth s-family backgrounds** [R78-fix], LF-count's 4D divergence sits entirely
  in the field-independent ρ_0 **[conditional on BG-reg, hence on L2]** [R78-fix]; [S9] after GT-lat: conditional on
  BG-b only.
- **Check c19** (criteria first): 10/10 PASS (B_4 character norm 1; one invariant form; GT on three SU(2) function
  families, one exactly integrated; B_4-broken and ι-broken controls show the check has power).
- **W1 (2D, fluctuating sea): partial.** Lemmas W1-def (exact defect identity), W1-size (exact size reduction to a
  collar large deviation) and W1-sym (symmetry + locality ⇒ renormalised form) PROVEN-HERE (**counted as one item**
  [R78-fix]). The exact remaining wall **for the weak (single-defect) form** [R78-fix] is the new OPEN item **W1-loc** =
  (W1-LD) collar large deviations + (W1-cl) exponential clustering of the block-pinned small-field sea. Both are
  small-field-sea statements (the 2D analogue of L4a-form / CMP 116), not large-field ones. **[R78-fix]** The strong form
  also needs a multi-defect expansion in a non-ultralocal sea (W1-F3, inside L5). W1-loc is restated in L5 [R78-fix]
  and, in 4D, in L5 [S9].
- W2 pre-stated only (RTARGET §7).


**Session-7 header.** REVIEW_S5_S6.md has been applied first; every fix is marked **[R56-fix]**. Session-7 additions
are marked **[S7]**.
- Fixes: A1 (supremum, not attained); A2 (E8** only, E8* corollary withdrawn); L4a-Π phase sign and the (1.21)
  citation; A1-NA(1) ((c) by concavity, principal branch, coarse side ≥ 3, c_N = c√N); A1-NA(k) and L1d [S6] restricted
  to S4' iterates (new OPEN L1e-(0.4)); the L4a-form torus side (4L^M vs 2L^m); LF-count in Balaban's normalisation
  (β'_B ≈ 4Nb_0, threshold a_B > 43/N², "ε_1 small enough", conditional on the one-loop rate); c18b declared outside
  the lemma's regime; new in-regime check c18c (pre-registered; 16/16).
- One-cube R-operation: the target was pre-stated in RTARGET.md before the derivation. The 2D wall was verified
  (~~every single-bond cut for 3 ≤ N ≤ 8~~ **[R78-fix]** every ε_1 ≲ (4π/(N-2))^{1/2}, linearised, with cost a ≈ ε_1²;
  the O(3) instanton is exactly marginal for the continuum bound; on the lattice, dislocations make aβ' < 2 [m]). **Proposition R2D-iso** proves the
  target for an isolated cube. The full R-operation's remaining walls are named: W1 (localisation in a fluctuating
  sea), W2 (nested multi-scale large fields), W3 (hard constraints and branch sets). The 4D transfer is OPEN item
  R4D-iso.
- Literature: CMP 198 (1998) is the low-temperature d ≥ 3 N-vector series, not a 2D UV template.

**Session-6 header (CMP 109 reading session).** Session-6 additions are marked **[S6]**. No review file was produced
after session 5, so there are no [R5-fix] items. The owner supplied Balaban, CMP 109 (1987) 249-301. It was read in
full. Its notes, with page and equation numbers, are in `literature/NOTES.md` §9; the open-source search for the
large-field results is in §10.

Main findings:
- CMP 109 is **small-field only**.
- It **defers two things**: the localisation/cluster-expansion half of its own inductive theorem (to CMP 116, "II.
  Cluster expansions"), and the coupling-flow theorem (Theorem 2, (0.31)) to "a separate paper".
- It cites, without reproving, everything from CMP 98/99/102 that L1d, L2 and L3g need.
- Balaban's link average (0.4) equals our S4' up to the pairing of the coordinate orders at the two ends (c17(B)).
- Balaban's background small-field condition (1.2) is L1e's hypothesis, **[R56-fix]** for S4' iterates and up to the
  √N norm conversion; for Balaban's own (0.4) it needs L1e-(0.4) (OPEN).

Upgrades:
- None of L1d, L2, L3g, L4a is upgraded wholesale.
- **L4a-Π** (the definition of β_j from the polarisation tensor, CMP 109 §5) is re-derived: PROVEN-HERE.
- L1d is narrowed.
- The open item A1-NA is proven in its one-step form, A1-NA(1), together with a k-uniform corollary on the L1e domain
  (for S4' iterates [R56-fix]).
- **Proposition LF-count** names the exact 4D wall: the unrenormalised per-level large-field count diverges. This is
  why the R-operation (L5) is load-bearing, and no open source states it.

**Session-5 header (reading and re-verification session).** REVIEW_S4.md has been applied first; every fix is marked
**[R4-fix]**. Session-5 additions are marked **[S5]**. Dimock's open expositions of Balaban's method were read (source
notes with page and equation references: `literature/NOTES.md`). The mapping onto L1d, L2, L3g, L4a, L5 and L6, and the
E8** reassessment, are in the [S5] block of L6loc. No Balaban CMP body has been read; every Balaban statement is still
[unverified-exact-statement]. **Correction:** Dimock's "RG according to Balaban" I-III treats scalar φ⁴ in d = 3, not
scalar QED; QED in d = 3 is his separate series (arXiv:1512.04373, 1712.10029, 2009.01156, overview 2204.07201).

**Session-4 header.** REVIEW_S3.md has been applied first; every fix is marked **[R3-fix]**. Session-4 additions are
marked **[S4]**. From session 4 the single off-D extension defining V^(m) and O at every level is S4'' with the odd
branch rule (section S4); the session-3 "failed link := 1" extension is withdrawn.

**Session-3 header.** REVIEW_S2.md has been applied first; every fix is marked **[R2-fix]**. Session-3 additions are
marked **[S3]**.

**Session-2 header.** REVIEW_S1.md (independent hostile review of the session-1 snapshot) has been applied: every fix
is marked **[R1-fix]** in place. Session-2 additions are marked **[S2]**. Two general caveats from the review apply to
the whole file:
- **Checks test instances, not uniformity.** Each check in checks/ verifies a stated identity or inequality on finitely
  many configurations and sizes. Uniformity in n, k, K, M or the background rests on the written proofs alone.
- **The citation upgrades** marked [v-R1] were confirmed by the reviewer's web search, not by me.

**Goal (owner).** Derive, independently, the existence of 4D pure SU(N) Yang-Mills as a continuum limit of lattice gauge
theory satisfying the Osterwalder-Schrader (OS) axioms. No mass gap is claimed.

Probe document only. No PR, no CL edit, no axiom edit. The lemma DAG follows
`../openai-balaban-review/review.md` section 6 (L1-L10, F1-F4, C1-C4), refined below.

## Status legend
- **PROVEN-HERE**: the complete argument is written in this file.
- **IMPORTED-AND-REVERIFIED**: exact citation and statement; hypotheses checked on our setting; the load-bearing step
  re-derived here, or checked exactly or numerically (named check).
- **IMPORTED-NOT-YET-REVERIFIED**: a named obligation. It never supports a PROVEN claim.
- **OPEN**: the missing estimate is stated.

## Citation key
- **[v]**: title, journal, volume and pages confirmed by web search this session (bibliographic data only; the paper
  bodies are paywalled and were NOT read).
- **[v-abs]**: the abstract or introduction was read.
- **[m]**: from memory, not confirmed.
- **[unverified-citation]**: the attribution is plausible, but the exact reference was not confirmed.

- **[S6] [read]**: read in the primary text; **[read-abs]**: abstract only; **[v-crossref]**: bibliographic data from
  the Crossref API.

**[S6] Caveat update.** Statements attributed to CMP 109 and tagged [read] are transcribed from the paper (NOTES §9).
What CMP 109 says about CMP 98/99/102 is [read, second-hand]. Every other Balaban statement remains as below.

**Global caveat.** Every statement attributed to Balaban below paraphrases the *structure* of his programme. The exact
theorem statements (norms, constants, hypotheses) were not read. Each is therefore `[unverified-exact-statement]`, and
re-verifying it is part of the obligation.

---

## 0. Target, and how it decomposes

**T_fin (finite volume).** On the torus T^4_M (side L^M in resolution-0 units), the lattice measures along a tuned
sequence of bare couplings converge, as the lattice spacing L^-K → 0, to a limit state on a gauge-invariant observable
algebra. The limit is non-trivial and reflection positive, with the torus symmetries.

**T_OS (the owner's target).** There is a state on an E(4)-covariant algebra of gauge-invariant observables on R^4. It
arises as such a limit, satisfies OS0-OS3 (OS4 clustering is listed separately in L9d), and is not a free theory.

Structural findings of this session:
1. **Existence of limit points of block laws is cheap; existence of the theory is not.** At every fixed resolution the
   RG variables live in a compact space, so limit points of the *block laws* exist by compactness alone: L7a and L8a,
   proven here, at finite and at infinite volume, with no infrared control. [R1-fix] These limit points are not yet a
   theory: without E8 the per-resolution limits need not be consistent (A_* ν_{m+1} ≠ ν_m is possible), mass may sit on
   the arbitrary off-D extension, and non-triviality has the L7.0 gap. The content of the theorem lies elsewhere:
   - (a) the limit is non-trivial and consistent across resolutions (needs Balaban's local large-field suppression, L6loc;
     [S3] in the scale-local form E8*, since the "all steps succeed" form is false along AF sequences, E8.3);
   - (b) uniqueness, i.e. convergence of the whole sequence (estimate E7);
   - (c) Euclidean invariance and OS0 regularity on a *local* field algebra (L9b, L9c).
2. **The infrared strong coupling is not an obstruction to the existence of limit points of block laws** (section L8).
   [R1-fix: the session-1 wording "not an obstruction to existence" was overstated.] It obstructs uniqueness of the
   infinite-volume state, clustering and the mass gap. Through uniqueness it also obstructs route γ1 to OS1 on R^4, so
   it may well obstruct existence of the OS theory itself.
3. **Euclidean invariance is the hard core.** On T^4 it is false: the torus breaks O(4). On R^4 it cannot be obtained
   by averaging over rotations, because averaging destroys reflection positivity (remark R9.1). It needs either
   universality (orientation independence, which rests on E7-type estimates) or a second, rotation-covariant observable
   family identified with the block family.

---

## 1. Setting (fixed for the whole document)

- **S1 Lattice.** Fix an integer L ≥ 3, odd. Balaban takes L sufficiently large [m]. The resolution-j lattice is
  Λ_{j,M} = (L^-j Z / L^M Z)^4, in physical units with the resolution-0 spacing equal to 1. The UV cutoff is the
  resolution K, with spacing ε_K = L^-K.
- **S2 Group.** G = SU(N), N ≥ 2. The links are U_b ∈ G on oriented bonds, with U_{-b} = U_b^dag.
- **S3 Wilson action.** S_K(U) = β_K Σ_p (1 - N^-1 Re tr U_p), with β_K = 2N/g_K^2. The measure is
  dμ_K = Z_K^-1 e^{-S_K} Π_b dU_b, with Haar measure dU_b.
- **S4 Averaging (L1).** Fine blocks B(X) have side L in lattice units, and their roots are the block centres c_X (L is
  odd).
  - Paths: T_y = P(c_X → y) · [L straight steps from y in direction μ] · P(c_Y → y + L e_μ)^dag, where P is the
    complete-axial transporter (move in coordinate 1, then 2, 3, 4).
  - Coarse link: U'(X, X + e_μ) = T_{c_X} exp(L^-4 Σ_{y∈B(X)} log(T_{c_X}^-1 T_y)), with the principal logarithm.
  - The map is defined on the small-field domain D = {||T_{c_X}^-1 T_y - 1|| < 1 for all y}.
  - The iterate A^{K-m} gives the resolution-m field V^(m). [Balaban-type; whether it equals the CMP 98 definition is
    unverified.]
- **S4' [S3] Order-averaged averaging (adopted from session 3; S4 kept as the fixed-order special case).**
  - For each of the d! coordinate orders σ, let P^σ be the complete-axial transporter moving in the coordinates in
    the order σ, and T^σ_y = P^σ(c_X → y) · S_y · P^σ(c_Y → y + L e_μ)^dag, with S_y the straight leg of L steps.
  - The reference T^σ_{c_X} = S_{c_X} (the straight transporter c_X → c_Y) does not depend on σ.
  - U'(X, X + e_μ) = S_{c_X} exp( (1/d!) Σ_σ L^-d Σ_{y∈B(X)} log(S_{c_X}^-1 T^σ_y) ), on the domain
    D' = {||S_{c_X}^-1 T^σ_y - 1|| < 1 (D'_N: < 2 sin(π/N) for N ≥ 7) for all σ, y}.
  - **S4'' (everywhere-defined version).** Off D', replace the averaged log X̄ by its traceless part X̄ - (tr X̄/N)·1,
    with the principal log (arg ∈ (-π, π)). **[R3-fix] Odd branch rule (session 4):** if Z has an eigenvalue exactly -1,
    its log is set to 0. Then log(Z^-1) = -log Z and log(WZW^-1) = W log(Z) W^-1 hold for EVERY Z (Z^-1 and WZW^-1 have
    eigenvalue -1 iff Z does), so the L9a' reversal computation, gauge covariance and permutation covariance hold
    everywhere, with no null-set proviso. S4'' is SU(N)-valued and measurable everywhere, equals S4' on D'_N, and is
    discontinuous only on the branch set (some Z with eigenvalue -1). **S4'' with this rule is the single map that defines
    V^(m) and the observable algebra O at every level from session 4 on**; the session-3 extension "failed link := 1"
    of L8b/L8c is withdrawn (REVIEW_S3 fix 4). Used in S5' (L6loc).
  - **Re-checks of the dependent lemmas for S4' (done here).**
    - L0 (locality, iterated roots): every P^σ stays in its block. Unchanged.
    - L1a: each log(S_c^-1 T^σ_y) is conjugated by g(c_Y); so is the average. L1b: an average of traceless
      anti-Hermitian logs is traceless anti-Hermitian. L1c: linear in the path set, so it holds with the order average.
    - L1e: the proof used only (1) Z_y has ≤ (d+2)L links and (2) the ribbon decomposition, which holds for any order
      because axial paths of order σ are translation covariant and split into one segment per coordinate. Same
      constants.
    - L9a': a coordinate reflection preserves every order σ, maps the σ-path set onto itself, and maps the reference
      S_{c_X} to the reversed reference. The reversal computation is unchanged.
    - **New: axis permutations.** A permutation π of the axes maps order-σ paths to order-(π∘σ) paths and straight legs to
      straight legs; the order set is permutation invariant and the reference is order-free. Hence
      V^(m)[πU] = π V^(m)[U] (on D', and everywhere for S4''). This repairs L8b.
    - Check c8 (12/12, 2 s): gauge covariance, SU(N), pure gauge, axis-permutation covariance (error 1e-15; the
      fixed-order S4 control fails at 0.1), reflection covariance, for SU(2) and SU(3) on the even fine torus of side 6.
  - **Torus side [S3].** From session 3 the fine torus side is taken EVEN, 2L^{K+M} (coarse side 2L^M in resolution-0
    units). All blocks still tile. A block-boundary reflection plane then has a block-boundary antipode, so L8c needs
    only the pure link reflection of L9a (L9a-m remains valid for odd sides), and the chessboard estimate E8.1 applies.
  - **Torus side [S4].** From session 4 the fine side is 4L^{K+M}, so every level-m side 4L^{M+m} is divisible by 4;
    the coarse chessboard E8*-red needs an even number of 2-site cells per direction. Every S3 statement holds verbatim.
- **S5 Renormalisation condition (RC).** [R2-fix: aligned with L7.0.] RC is read with the continuous cut-off observable
  w̃ = ζ · (1 - N^-1 Re tr V^(0)_p) of L7.0. At each K, tune β_K so that E_{K,β_K}[w̃] = w*, which is possible for every
  w* ∈ (0, w̃_0(K)) (L7.0). A single w* for all K needs E7.0. [S3, R3-fix] Section L6loc shows that, for N = 2, 3, 4,
  E7.0 restricted to the AF window fails (sequences with β_K ≤ λ_c K), so this RC is replaced by S5' (L6loc); for
  N ≥ 5 it is undecided.
- **S6 Observables.** O_m(X) is the set of continuous, gauge-invariant f(V^(m)|_X) for X a finite union of
  resolution-m blocks, extended measurably off D. The algebra is O = ∪_m O_m.
- **S7 OS axioms (target).**
  - OS0: regularity / temperedness.
  - OS1: E(4) invariance.
  - OS2: reflection positivity.
  - OS3: permutation symmetry (automatic for these bosonic observables).
  - OS4: clustering.

---

## 2. Lemma ledger

### L0. Locality and consistency of the averaged fields: PROVEN-HERE
**Statement.**
- (i) V^(m)(X, X + e_μ) depends only on the fine links inside B^(m)(X) ∪ B^(m)(X + e_μ), the two resolution-m blocks.
- (ii) Under a fine gauge transformation g, V^(m)(X, Y) → g(c^(m)_X) V^(m)(X, Y) g(c^(m)_Y)^dag. Here c^(m) are the
  iterated roots: the centre of a block of side L^{K-m} is a fine site, because L is odd.
- (iii) A(V^(m+1)) = V^(m) holds identically on D (D_N for N ≥ 7, see L1b) (definition of the iterate).
- (iv) Every f ∈ O_m(X) is gauge invariant, bounded, and measurable with respect to the links in X.

**Proof.**
- (i) For one step: the axial paths P stay inside their own block. The straight leg runs from y ∈ B(X) to
  y + L e_μ ∈ B(X + e_μ), and its μ-coordinate stays in [X_μ L, X_μ L + 2L - 1], so it passes only through the two
  blocks. Induct on the number of steps; at each step the two coarse blocks contain the fine blocks used.
- (ii) Every T_y has the endpoints c_X and c_Y, so T_y → g(c_X) T_y g(c_Y)^dag. The rest is L1a, applied
  inductively, with the coarse gauge transformation g|_roots.
- (iii) By definition.
- (iv) f is a gauge-invariant function of the coarse field, which by (ii) transforms covariantly; locality is (i). ∎

### L1. Gauge-covariant averaging
- **L1a. Covariance: PROVEN-HERE.** U'[g·U] = g(c_X) U'[U] g(c_Y)^dag, and D is gauge invariant.
  - Proof: T_{c_X}^-1 T_y → g(c_Y) (T_{c_X}^-1 T_y) g(c_Y)^dag. The principal log commutes with unitary conjugation,
    the norm is conjugation-invariant (so D is invariant), and the exp of the averaged log is conjugated by g(c_Y).
    Multiply by T_{c_X} → g(c_X) T_{c_X} g(c_Y)^dag. ∎
  - Check c1(a): error 6e-16 for SU(2) and 6e-15 for SU(3), with random g on all fine sites.
- **L1b. SU(N)-valued; pure gauge goes to pure gauge: PROVEN-HERE.**
  - **Domain.** Take D_N = {||T_{c_X}^-1 T_y - 1|| < 2 sin(π/N) for all y}. For N ≤ 6 the bound 1 of S4 suffices
    (2 sin(π/6) = 1); for N ≥ 7 use D_N. [R1-fix: session 1 wrote "N ≤ 5" here and "fails for N ≥ 7" in LOG; the
    correct threshold is N ≤ 6.] D_N shrinks like 1/N, so any claim uniform in N must track it.
  - **Proof.** Each Z_y = T_{c_X}^-1 T_y ∈ SU(N) has eigenvalues e^{iθ_j}. The domain condition gives |θ_j| < 2π/N
    (for N ≤ 6, the bound 1 gives |θ_j| < π/3 ≤ 2π/N).
    - So the principal log is i·diag(θ_j) in the eigenbasis, anti-Hermitian, with trace iΣθ_j.
    - det Z_y = 1 gives Σθ_j ∈ 2πZ, and |Σθ_j| < 2π, so Σθ_j = 0.
    - The average of traceless anti-Hermitian matrices is traceless anti-Hermitian, its exponential lies in SU(N), and
      T_{c_X} ∈ SU(N).
  - Pure gauge: U_b = g_x g_y^-1 gives T_y = g(c_X) g(c_Y)^-1 for all y, all the logs vanish, and
    U' = g(c_X) g(c_Y)^-1. ∎
  - Check c1(b, c) for SU(2) and SU(3).
- **L1c. Linearisation: PROVEN-HERE.**
  - If U_b = exp(i t a_b) with ||a_b|| ≤ 1, then log U' = i t L^-4 Σ_y (Σ_{b∈Γ_y} a_b) + O(t^2), where Γ_y is the
    path of T_y. This is Balaban's abelian averaging Q applied to the line integrals.
  - Proof: BCH gives log T_y = i t Σ_{Γ_y} a_b + O(t^2) and log(T_{c_X}^-1 T_y) = log T_y - log T_{c_X} + O(t^2).
    Average, and add log T_{c_X} back at order t. ∎
  - [R1-fix] Check c1(d) compares log U' with avg_y log T_y, **not** with the averaged line integrals stated above. Those
    two differ at O(t^2) (the second-order BCH commutators cancel in the first, so log U' = avg log T_y + O(t^3)), which
    is why the halving ratio is about 4. The session-1 reading "second order, better than the claim" was a misreading of
    which identity was tested. The lemma itself stands on the BCH proof; the line-integral form is untested by c1(d).
  - The O(t^2) constant depends on L through the path lengths; no uniformity in L is claimed.
- **L1d. Regularity on Balaban's spaces of regular configurations: IMPORTED-NOT-YET-REVERIFIED.**
  - Content: analyticity of A on D; derivative bounds; the coarse small-field condition implied by the fine one with
    L-dependent constants; the composition of k steps controlled uniformly in k.
  - Sources: Balaban, "Averaging operations for lattice gauge theories", CMP 98 (1985) 17-51 [v]; "Spaces of regular
    gauge field configurations on a lattice and gauge fixing conditions", CMP 99 (1985) 75-102 [v-R1].
  - [R2-fix] The session-2 line "the k-uniform sup-curvature part of this obligation is now proven" is WITHDRAWN. L1e
    below is a theorem about *smooth* backgrounds (F small in physical units). Balaban's small-field conditions are
    dimensionless (||1 - U_p|| ≲ p(g_k) g_k at each scale, so F ~ ε^-2 there), and L1e says nothing about them. The
    fine-to-coarse small-field propagation of L1d is untouched by L1e.
  - Finite diagnostic c1(e): one coarse plaquette has F_coarse ≈ 0.14-0.2 F_fine,max for smooth SU(2) and SU(3) fields.
  - Obligation: a k-uniform version with explicit constants.
  - **[S5]** Abelian analogue [read]: Dimock arXiv:1712.10029 Theorem 1 (p.43, eq. 327), multiscale regularity with
    constant C_0 M p_j, described there as "abelian versions of non-abelian results" in CMP 99 (1985) 75-102 and CMP 102
    (1985) 277-309. What transfers: per-level dimensionless small-field conditions; gauge equivalence on enlarged cubes
    to a regular field. What is abelian-specific: linear averaging, gauge-potential RG variables. Status unchanged.
  - **[S6] CMP 109 [read] narrows L1d.** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
    - **Lemma B-avg [S6]: PROVEN-HERE (elementary).** Balaban's averaged link is CMP 109 (0.4) or (0.12). (0.4) is S4' with the two contour families
      averaged *independently*; S4' pairs them by order. With the same pairing the two are identical, by the conjugation
      identity exp(avg log(TS^{-1}))S = S exp(avg log(S^{-1}T)) (check c17(B): error ≤ 6e-16 in d = 3, 4). With
      independent pairing they agree at linear order and differ at second order (c17(B), ratio 3.96).
    - **Transfer of the CMP 98 results.** CMP 109 asserts that "all results of the paper [12] are valid" for (0.4) and
      (0.12) (p.254). It does not axiomatise link averages, so the transfer to S4' itself is NOT covered by any
      statement read. Either adopt (0.4) verbatim (L0, L1a-c, L8b and L9a' carry over by the same proofs, and A1 holds
      because the linearisations coincide), or keep S4' and prove the CMP 98 results for it.
      **[S9] Decision 4 (made by the session-9 lead under delegated authority): keep S4', with the soft constraint of
      L5 [S9] (Lemma D4-norm) as the RG kernel.** So the CMP 98 results must be proven for S4' (soft), and the (0.4)
      route is a comparison branch. [R910-fix13] The delegation is now quoted in the owner's words (as recorded in the lead's
      memory file) in the session-9 header; decision 4 = a proof-technique choice by the lead under that standing
      delegation, not an axiom or CL change.
    - **L1d(i), fine regular ⇒ coarse regular, k-uniformly.** This is now covered on Balaban's own domain. CMP 109
      (1.2) (p.260) defines the background small-field domain as |U(∂p) - 1| < ε_0η², η = L^{-k}, i.e. curvature
      F < ε_0 in units of the current coarse lattice. **That is L1e's hypothesis F ≤ F_0** [R56-fix: for S4' iterates and up to √N; see below]. L1e(b) then gives
      |V(∂p') - 1| ≤ (1 + 4C_δ)F, uniformly in k (d = 4, L ≥ 9 odd). Balaban states the same implication with the
      constant 2 ("By Proposition 2 [12]", p.260) and assumes L > 11. So the R2-fix sentence "L1e says nothing about
      Balaban's small-field conditions" is narrowed: it is true for the fluctuating RG variables (their threshold ε_1
      sits at the level's own scale, NOTES §9.5), and false for the background-field domain (1.2), which is precisely
      L1e's domain. Our constant 1 + 4C_δ (≈ 29 at L = 9) is worse than 2. Nothing downstream needs 2.
    - **[R56-fix] GAP in the narrowing above; scope restated.** L1e is proven for S4/S4' iterates only. Balaban's
      (0.4) averages the two contour families *independently* (Lemma B-avg), and L1e's ribbon step (the translate
      γ + s_je_μ of the SAME-order axial path) does not apply when the two ends use different orders σ ≠ σ': the loop
      is then the ribbon times a loop formed by two axial paths with the same endpoints. Also, Balaban's |·| uses the
      normalised trace (tr 1 = 1), so "|U(∂p) - 1| < ε_0η²" matches L1e's operator-norm F ≤ F_0 only up to the √N
      norm conversion. Corrected statement: **L1d(i) is covered on (1.2) for S4' iterates, up to the √N norm
      conversion; for Balaban's (0.4) it needs L1e for (0.4), the two-axial-path ribbon variant (new OPEN item
      "L1e-(0.4)", expected easy: C_A → ~2C_A, not written).** The bold sentence above is to be read with this
      restriction. **[S9] After decision 4, L1e-(0.4) is a comparison-branch item** (needed only to read Balaban's own
      statements on (0.4)); the main path uses S4' iterates, where L1e is proven.
    - **What remains of L1d (still imported, from CMP 98 and 99:75-102):**
      - analyticity on the complexified spaces U^c_j(X, α_0, α_1) (NOTES §9.4, conditions (i)-(iv));
      - the second-order quantity J = D*_U η^{-2} π Im ∂U in (1.2), which L1e does not control;
      - the converse (V regular ⇒ U_k(V) ∈ U_k(ε_0)), which is L2;
      - Proposition 5 of CMP 89:411-445 (derivatives of averaging operations).

- **L1e. [S2] Iterated averaging stays uniformly close to straight fine transport, for smooth backgrounds:
  PROVEN-HERE.** [R2-fix: scope.] The hypothesis F ≤ F_0 ≈ 0.08 (d = 4, L = 9) is in *physical* units, i.e.
  ||1 - U_p|| ≤ 0.08 ε^2 at the fine scale. It describes classical smooth fields such as the backgrounds U(V) of L2. It
  does not describe typical Wilson configurations or Balaban's small-field regime (see L1d), exactly as L3s(d).
  - **Setting.** Fine spacing ε = L^-k in physical units, so unit blocks have side 1. Put V^(k) = U and
    V^(j) = A(V^(j+1)) (S4 applied on the resolution-(j+1) lattice), with s_j = L^-j.
    - For a resolution-j link b = (X, X + e_μ), let S_b be the fine straight transporter between the fine roots c^(j)_X
      and c^(j)_X + s_j e_μ. These roots are fine sites; the iterated root offset is (L^{k-j} - 1)/2.
    - F := max over fine plaquettes p in the region of ||1 - U_p|| / ε^2.
    - Define δ_j := max_b ||V^(j)_b - S_b|| / s_j^2, so that δ_k = 0.
    - Constants: c := 4 arcsin(1/4) = 1.0107, C_A := (d-1)/2, and ρ := (1 + c(d+2)) / L.
  - **Claim (recursion), for every odd L.** If every Z_y used at level j obeys ||Z_y - 1|| ≤ 1/2, then
    δ_j ≤ ρ δ_{j+1} + c C_A F.
  - **Corollary (uniform in k).** Let L > 1 + c(d+2) (= 7.07 in d = 4, so L ≥ 9), and put C_δ := c C_A / (1 - ρ). If
    F ≤ F_0 := 1 / (2(C_A + (d+2) C_δ / L)), then for all k and all j ≤ k:
    - (a) the domain hypothesis holds at every level, and δ_j ≤ C_δ F;
    - (b) coarse curvature: ||1 - V^(j)_p|| ≤ s_j^2 (1 + 4 C_δ) F, so F_j ≤ (1 + 4C_δ) F uniformly in k;
    - (c) every V^(j) lies in D (indeed ||Z_y - 1|| ≤ 1/2 < 1). For SU(N) membership via L1b we also need
      1/2 < 2 sin(π/N), i.e. N ≤ 12. For N ≥ 13, replace 1/2 by τ_N/2 throughout, which shrinks F_0 by a factor ~ 1/N.
    - The proof uses only unitarity and the spectral log, so it holds for every SU(N), with c computed at the threshold
      used.
  - **Proof of the recursion.**
    - Write V = V^(j)_b = T_c exp(X̄), where X̄ = avg_y log Z_y and Z_y = T_c^-1 T_y are products of resolution-(j+1)
      links. Let T^S and Z^S be the same products with every V^(j+1) link replaced by its S.
    - T_c is the straight product of L links, and T^S_c = S_b. For unitaries, ||Π A_i - Π B_i|| ≤ Σ ||A_i - B_i||.
      Hence ||T_c - S_b|| ≤ L δ_{j+1} s_{j+1}^2 = δ_{j+1} s_j^2 / L.
    - Z_y contains at most 2L + d(L-1) ≤ (d+2)L links: two axial legs of at most d(L-1)/2 links each, and two straight
      legs. Hence ||Z_y - Z^S_y|| ≤ (d+2) δ_{j+1} s_j^2 / L.
    - **Ribbon bound: ||Z^S_y - 1|| ≤ C_A s_j^2 F.**
      - Z^S_y is the fine holonomy of γ σ_y (γ + s_j e_μ)^-1 σ_c^-1. Here γ is the fine realisation of the
        resolution-(j+1) axial path c_X → y, σ is the straight μ-leg of length s_j, and γ + s_j e_μ is the axial path
        c_Y → y + s_j e_μ, because axial paths are translation covariant.
      - Insert σ_p σ_p^-1 at each corner p of γ. The loop becomes a product of conjugated rectangle loops, one per
        segment γ_ν.
      - For ν = μ the rectangle is degenerate and collinear, so its holonomy is exactly 1.
      - For ν ≠ μ it is a planar |γ_ν| × s_j grid. Its boundary holonomy is a product of conjugated plaquettes (row by
        row: each row is a ladder, as in L3s(i)), so its norm is ≤ |γ_ν| s_j F.
      - Finally |γ_ν| ≤ ((L-1)/2) s_j / L < s_j / 2. Summing over ν ≠ μ gives ≤ (d-1) s_j^2 F / 2.
    - **Log and exp bounds.**
      - If ||Z - 1|| ≤ 1/2, then ||log Z|| ≤ c ||Z - 1||. Z is normal, |e^{iθ} - 1| = 2 sin(|θ|/2), and
        2 arcsin(x/2)/x is increasing, with value c at x = 1/2.
      - For anti-Hermitian X, ||e^X - 1|| ≤ ||X||, and ||X̄|| ≤ max_y ||log Z_y||.
    - **Combine.** ||V - S_b|| ≤ ||T_c - S_b|| + ||e^{X̄} - 1||
      ≤ s_j^2 [δ_{j+1}/L + c(C_A F + (d+2) δ_{j+1}/L)]. Divide by s_j^2. ∎
  - **Proof of the corollary.** Induct downward from δ_k = 0.
    - If δ_{j+1} ≤ C_δ F, then ||Z_y - 1|| ≤ s_j^2 (C_A + (d+2) C_δ / L) F ≤ 1/2, using s_j ≤ 1 and F ≤ F_0. So the
      recursion applies, and δ_j ≤ ρ C_δ F + c C_A F = C_δ F.
    - (b): S_p is the fine holonomy of a planar s_j × s_j square, so ||1 - S_p|| ≤ s_j^2 F. Add the four link errors.
    - (c) is the domain bound. ∎
  - **Check c5** (SU(2); d = 2, 3, 4; L = 3, 5, 7, 9; k = 2-3). The recursion and the domain hold in every small-field
    case.
    - Measured δ_j/F lies in 0.01-0.08, far below the bound c C_A ≈ 1.5 (d = 4).
    - In the L = 3 cases (ρ > 1, not covered by the corollary) the measured δ_j grows roughly additively in the number of
      levels: 0.028, 0.057, 0.083 in d = 3 with k = 3. So uniformity in k at small L is genuinely not shown.
    - These are instances, not uniformity tests.
  - **What remains of L1d:** all of it for non-smooth fields (Balaban's small-field regime), plus analyticity in U,
    derivative and Hölder bounds, and the large-field side. c5 never instantiates d = 4 with L ≥ 9 (every d = 4 case has
    L = 3, ρ = 2.35), so the corollary rests on the proof alone (REVIEW_S2 re-derived it).

### L2. Background field (constrained minimiser): IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** For V in the coarse small-field domain, the Wilson action restricted to {U : A(U) = V}
  has a unique minimiser U(V) near the identity in a suitable axial/Landau gauge. U(V) is analytic in V and
  exponentially localised.
- **Source.** Balaban, "The variational problem and background fields in renormalization group method for lattice gauge
  theories", CMP 102 (1985) 277-309 [v-R1].
- **Obligation.** An SU(2) Newton/continuation check of uniqueness on an 8^4 torus, plus a written contraction argument.
- **[S5]** Abelian analogue [read]: the minimiser is a linear operator, A^min = H_k A_{k+1}, axial and Landau versions
  gauge equivalent (arXiv:2204.07201 p.6, eqs. 22-25); exponential decay of H_k is imported by Dimock from CMP 95, 96, 99
  (1512.04373 Lemma 9, "we sketch the proof"). The non-linear existence/uniqueness/analyticity problem has no abelian
  counterpart. Status unchanged.
- **[S6] The exact imported statement, as CMP 109 cites it [read, second-hand].** Status unchanged:
  IMPORTED-NOT-YET-REVERIFIED. Theorem 1 of CMP 102:277-309 is quoted by CMP 109 as follows. For V on T_1^{(k)} with
  |V(∂p') - 1| < ε_0', "there exists exactly one regular, critical orbit of the functional U → A(U),
  U : Ū^k = M^k(U) = V ... and it is a minimal orbit" (p.260; also p.256). The condition on V with B_3^{-1}ε_0 implies
  U_k(V) ∈ U_k(ε_0) (p.260). CMP 109 also uses, from the same paper: Sect. F (local coordinates U_k = exp iηH),
  Sect. G (multiscale minimisers U_n), and Proposition 9 / (190) (exponential decay of δH/δB, rate δ_0). None is
  reproved in CMP 109.
  - **New tree-level consequence (conditional on the regularity half of L2, and [R56-fix] on L1e-(0.4) plus the √N
    norm conversion, since V = M^k(U_k(V)) uses Balaban's (0.4)).** If U_k(V) lies in the L1e domain, which
    is what (1.2) + Theorem 1 [15] assert, then Corollary A1-NA(k) (L6loc [S6]) gives
    A_coarse(V) ≤ e^{C_7F} A(U_k(V)), uniformly in k. Equivalently, the background's fine Wilson action is at least
    e^{-C_7F} times the coarse Wilson action of V. This is the gauge analogue of Dimock III Lemma 20 (fine action ≥
    c_0 × coarse action), with c_0 → 1 in d = 4. It does not touch existence, uniqueness or analyticity, which remain
    the import.
- **[S9] Decision 4 and L2.** CMP 102's Theorem 1 is about the hard constraint (0.4). The main path needs the
  soft-constraint version: the tree-level minimiser of fine action + soft S4' constraint terms (L5 [S9], D4-norm), with
  the intermediate block variables also minimised. Status unchanged (IMPORTED-NOT-YET-REVERIFIED), now with the target
  "soft version". The part of L2 that BG-reg needs is isolated in L5 [S9] as **BG-b**: sup coarse-unit curvature of the
  background on sub-cubes plus summable mean oscillation, which is the U_k(ε_0)-membership half (CMP 109 (1.2):
  |U(∂p) - 1| < ε_0η² AND |J| < ε_0, J = D*_Uη^{-2}π Im ∂U) plus a lattice elliptic step. W1-loc (4D) needs, in addition,
  L2's exponential decay of the background in the block variables (part of hypothesis (DF)).
- **[S10]** For the linearised soft chain, BG-b ⇐ (H1) + (H2) is now PROVEN (L5 [S10], Proposition BG-b-lin, with Lemmas
  LES, CR and J-str). So the part of soft L2 that BG-reg needs is exactly the membership pair (H1) (sup fine curvature
  in coarse units) + (H2) (sup top soft residual). By Lemma J-str, (H2) controls CMP 109's |J| condition. The (DF)
  sub-DAG node N2 records the whole soft-L2 target. Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
- **[S11]** For the linearised soft chain: Lemma N2-a (the residual and the fine curvature are functions of the gauge
  orbit and vanish on every flat class; also for SU(N)), Lemma N2-E (E_k ≤ C_E(1 + κ_+)||dB_k||², uniformly in k: the
  ℓ² forms of (H1)/(H2) from the coarse curvature, not the field size) and Proposition N2-red ((H1) + (H2) ⇐ (LED)),
  all PROVEN-HERE (L5 [S11]). The remaining linear statement is (LED). Status unchanged.
- **[S12]** (LED) and the sup forms (H1) + (H2) are PROVEN for the linearised soft chain (L5 [S12], Theorem N2-lin, via
  a dual reduction to the top residual and an ℓ¹ symbol bound, uniform in k and the torus). So BG-b holds for the
  linearised chain at small coarse curvature, unconditionally, [R1314-fix] for the levels n ≥ 1 (the n = 0 term needs the
  current step's residual). The soft-L2 obligation is now the SU(N) chain (B-NA,
  SU(N) analogues of N2-E and N2-lin) and decay for complex data (N10). Status unchanged.
- **[S13]** The linearised response is exponentially local (L5 [S13], Theorem N2-exp): the B_k ↦ (r, f_0) kernels and
  the F ↦ r kernel decay like e^{-m_*|X|_1}, m_* = m_*(L, κ_±) > 0 explicit (0.0111 at L = 3, κ ≡ 1), uniformly in k
  and T; the located singularity gives the located rate (numerical, not proven) [R1314-fix] ≈ 0.98 at κ = 1. The soft-L2 obligation is now the SU(N) chain
  (including an SU(N) N2-exp) and the non-linear analytic dependence for N10. Status unchanged.

- **[S14]** The SU(N) chain is reduced, not proven (L5 [S14], Proposition B-NA-red): B-NA follows from a multi-scale
  Schauder-type estimate (G♯) for the gauge-fixed linearised chain on general sources and the matching remainder bound
  (R♯), both OPEN; the algebra (NA-alg), the gauge-fixing step (NA-crit) and the screening identity for fine sources
  (SRC-id) are proven. The proven strip width is now m_*' = 0.0384 at κ ≡ 1 (Theorem N2-exp') [R1314-fix: was 0.0385]. Status unchanged.
- **[S15]** The soft half of (G♯) at the trivial background is PROVEN (L5 [S15], Theorem G♯_0-soft): the soft residuals
  of the linear chain respond to divergence-form sources at every level with exponentially weighted, k- and T-uniform
  bounds, given summable level weights (the marginal count). The fine half is reduced to a local-energy input (LED-src)
  via Lemma LES-div; the top-level per-step NA defect has no n-loss (Proposition NA-lev) [R15-fix: was "NA-F2 does not
  occur in the per-level setting"; the multi-level uniformity is carried by (NA-H) ⊂ B-NA]. Status unchanged.
- **[S16]** Lemma F-df_0 is PROVEN (L5 [S16]): the fine-curvature response of the linearised chain has an exponentially
  local representative as a function of the coarse curvature on all 2-forms (rate any m' < m_*'), so both gauge-invariant
  outputs (r_{k-1}, f_0) have exponential F-kernels. The linear package is written up in LINEAR_PACKAGE.md. Status unchanged.
### L3. Fluctuation propagators uniform in small-field backgrounds

#### L3s. Scalar multi-scale covariance in SU(N) backgrounds: PROVEN-HERE (a strictly weaker analogue of Balaban's bound)
[R1-fix] This is a scalar, weaker analogue of Balaban's propagator bounds. Its constants are uniform in n = 1/ε. Scope:
- (a) Session 1 proved it for the *direct* axial average only. [S2] Corollary L3s' below extends it to both forms of the
  iterated average, which closes R3.1.
- (b) It covers scalar 0-forms only: no gauge fixing, any unitary representation. The gauge-field (1-form) analogue is
  L3g, which is OPEN, and session 2 found an obstruction there (L3g-ob).
- (c) It gives only L^2 operator-norm bounds on block-localised pieces. The pointwise kernel bound that follows,
  |G(x,y)| ≤ (2/m) ε^-4 e^{-μρ}, is not uniform. No derivative or Hölder bounds are proved.
- (d) The hypothesis "F small" holds for smooth backgrounds such as the minimisers U(V) of L2, not for typical Wilson
  configurations, where F ~ g/ε^2. *Applying* L3s therefore needs L2 and L1d (imported).
- (e) It is quantitative: for a = 1 it needs F < 1/3.

**Setting.**
- d = 4 and n ≥ 1, with spacing ε = 1/n. The torus is Λ = (εZ/TZ)^4, partitioned into unit cubes B, each with n^d
  sites.
- φ ∈ ℓ^2(Λ, C^N), with ⟨φ, ψ⟩ = ε^4 Σ_x φ_x^dag ψ_x. The proof uses only unitarity, so any unitary representation
  works.
- Root: c_B has offsets r_0 = ⌊(n-1)/2⌋, and r = ⌈(n-1)/2⌉ ≤ n/2 is the largest coordinate distance from the root.
  P(c → y) is the complete-axial transporter inside B.
- ⟨φ, -Δ_A φ⟩ = ε^2 Σ_{bonds b=(x,y)} |φ_x - U_b φ_y|^2.
- (Q_A φ)(B) = ε^4 Σ_{y∈B} P(c_B → y) φ_y, with ||Qφ||^2 = Σ_B |(Qφ)(B)|^2.
- H_A = -Δ_A + a Q_A^dag Q_A, with a > 0.
- F := max over plaquettes p inside the blocks of ||1 - U_p|| / ε^2 (operator norm).
- A_max := max over intra-block bonds of ||1 - U_b^ax|| / ε, where U^ax is the field in the complete axial gauge of
  each block.

**Claims.** Every constant is independent of n, T, N and of the background.
- (i) A_max ≤ (d-1) r ε F ≤ (d-1) F / 2.
- (ii) H_A ≥ m := min(2, a) - d A_max^2 ≥ min(2, a) - d (d-1)^2 F^2 / 4, which is min(2, a) - 9 F^2 in d = 4.
- (iii) Suppose m > 0 and μ ∈ (0, 1/ε] satisfies (CT) (1 - η) m - 1.55 d μ^2 - a (η + η^2) ≥ m/2, with
  η = e^μ - 1. Then for all subsets Δ, Δ' ⊂ Λ,
  ||1_Δ H_A^-1 1_Δ'|| ≤ (2/m) exp(-μ ρ_∞(Δ, Δ')),
  where ρ_∞ is the ℓ^∞ torus distance in physical units.

**Proof of (i).**
- Gauge transform by g(x) = P(c_B → x) on each block. The blocks partition Λ, so this is one gauge transformation. It
  makes every tree link equal to 1 and sends the non-tree link b = (x, x + e_μ) to the holonomy of the loop
  P(c → x) b P(c → x + e_μ)^dag.
- The two axial paths agree in coordinates 1, ..., μ-1. They differ by one step in coordinate μ, then run in parallel
  through coordinates μ+1, ..., d.
- So the loop bounds a ladder of Σ_{ν>μ} |x_ν - c_ν| ≤ (d-1) r plaquettes, each entering as a lasso (a conjugated
  plaquette).
- For unitaries, ||Π V_i - 1|| ≤ Σ ||V_i - 1||, and conjugation preserves the norm. Hence
  ||U_b^ax - 1|| ≤ (d-1) r ε^2 F. Divide by ε and use r ε ≤ 1/2. Bonds in the last direction μ = d are tree bonds. ∎

**Proof of (ii).**
- In the gauge of (i), H_A is unitarily equivalent to the operator with U → U^ax. Because P^ax = 1, Q_A becomes the
  plain block average Q_0. Dropping the inter-block bonds (each term ≥ 0):
  ⟨φ, H φ⟩ ≥ Σ_B [ ||∂_A φ||_B^2 + a |Q_0 φ(B)|^2 ], with ||∂_A φ||_B^2 = ε^2 Σ_{b⊂B} |φ_x - U_b^ax φ_y|^2.
- **Step 1.** Split (φ_x - U φ_y)/ε = (φ_x - φ_y)/ε - (U - 1) φ_y / ε. The triangle inequality in ℓ^2(bonds) gives
  ||∂_A φ||_B ≥ ||∂φ||_B - A_max √d ||φ||_B, since each site is the forward end of at most d intra-block bonds.
  Then (x - y)^2 ≥ x^2/2 - y^2 (or the right side is negative) gives
  ||∂_A φ||_B^2 ≥ (1/2) ||∂φ||_B^2 - d A_max^2 ||φ||_B^2.
- **Step 2 (Poincaré, eq. P).** ||φ||_B^2 ≤ (1/4) ||∂φ||_B^2 + |Q_0 φ(B)|^2.
  - The Neumann grid Laplacian on {0, ..., n-1}^d with spacing ε has eigenvalues Σ_i (4/ε^2) sin^2(π k_i / (2n)),
    with cosine eigenvectors.
  - For k ≠ 0 the eigenvalue is at least (4/ε^2) sin^2(π/(2n)) ≥ (4/ε^2)(1/n)^2 = 4, using sin x ≥ 2x/π on [0, π/2].
  - Decompose φ = φ̄ + φ^⊥ with φ̄ the block mean, which equals Q_0 φ(B) because the block volume is 1. Then
    ||φ̄||_B^2 = |Q_0 φ|^2 and ||φ^⊥||^2 ≤ (1/4) ⟨φ^⊥, -Δ_N φ^⊥⟩ = (1/4) ||∂φ||_B^2. The cross terms vanish.
- **Step 3.** (1/2) x + a y ≥ min(2, a) (x/4 + y) ≥ min(2, a) ||φ||_B^2. Subtract d A_max^2 ||φ||_B^2 and sum over B. ∎

**Proof of (iii) (Combes-Thomas, in the form uniform in ε).**
- Let f(x) = ρ_∞(x, Δ'), which is 1-Lipschitz, and H_μ = e^{μf} H e^{-μf}.
- **Kinetic part.** For a bond, with z = φ_x^dag U φ_y and t = μ(f_x - f_y), |t| ≤ με ≤ 1, the off-diagonal terms give
  real part -2 cosh(t) Re z. Compared with t = 0, the change is ≥ -2 (cosh t - 1) |z| ≥ -(cosh t - 1)(|φ_x|^2 + |φ_y|^2).
  Summing over the 2d bonds at each site, the kinetic real part is
  ≥ ⟨φ, -Δ_A φ⟩ - 2d (cosh(με) - 1) ε^-2 ||φ||^2 ≥ ⟨φ, -Δ_A φ⟩ - d cosh(1) μ^2 ||φ||^2.
- **Block part.** In block B, write e^{±μ f(y)} = e^{±μ f(c_B)} (1 + s_±(y)), with |s_±| ≤ e^{μ/2} - 1 ≤ η. Let
  w = Q_A φ(B) and r_± = ε^4 Σ_y P s_± φ_y. Then |r_±| ≤ η ||φ||_B (Cauchy-Schwarz, block volume 1), and
  ⟨Q e^{μf} φ, Q e^{-μf} φ⟩_B = ⟨w + r_+, w + r_-⟩. Its real part is
  ≥ |w|^2 - 2η |w| ||φ||_B - η^2 ||φ||_B^2 ≥ (1 - η) |w|^2 - (η + η^2) ||φ||_B^2.
- **Combine.** Re ⟨φ, H_μ φ⟩ ≥ (1 - η) ⟨φ, H φ⟩ - [1.55 d μ^2 + a (η + η^2)] ||φ||^2 ≥ (m/2) ||φ||^2 under (CT).
  The numerical range then gives ||H_μ^-1|| ≤ 2/m.
- Finally 1_Δ H^-1 1_Δ' = (1_Δ e^{-μf}) H_μ^-1 (e^{μf} 1_Δ'), with ||1_Δ e^{-μf}|| ≤ e^{-μ ρ_∞(Δ, Δ')} and
  e^{μf} 1_Δ' = 1_Δ'. ∎

**Check c3.**
- n = 1, 2, 3, i.e. ε = 1, 1/2, 1/3, with smooth and rough SU(2) backgrounds at F = 0.1-0.3 and a large rough field.
  (i) and (ii) hold in every case.
- The free gap is exactly 1 = min(2, a) for a = 1: (P) is sharp on constants.
- The spectrum is gauge invariant.
- (iii) on n = 2, T = 4, F = 0.2: m_lb = 0.931, proven μ = 0.147. The block-block norms are ≤ 0.038 × the bound. The
  measured decay rate is 1.78 per unit length.

**Remark R3.1 (perturbed transports): PROVEN-HERE.** [R2-fix: this is the session-1 remark promoted to a counted item,
not new session-2 work.] Suppose Q' uses unitary transports V'_y with
||V'_y - P(c → y)|| ≤ θ for all y.
- Then |Q' φ| ≥ |Q_A φ| - θ ||φ||_B, by Cauchy-Schwarz with block volume 1. So a|Q'φ|^2 ≥ (a/2)|Q_A φ|^2 - a θ^2 ||φ||_B^2.
- Step 3 with a/2 gives H' ≥ m' := min(2, a/2) - d A_max^2 - a θ^2.
- (iii) holds verbatim with m' in place of m. The block part used only unitarity of the transports and Cauchy-Schwarz.

**Corollary L3s'. [S2] Iterated scalar averaging: PROVEN-HERE (closes the session-1 C_path obligation).**
The iterated scalar average is Q_k φ(B) = ε^d Σ_y W_y φ_y. Each y has a unique ancestor chain
c_B = c^(0) → c^(1)(y) → ... → c^(k)(y) = y, and W_y is the product of stage transports along it. Stage i is a
resolution-i axial path inside the level-(i-1) block. Two versions:
- **(I) Stage paths realised by fine links: θ_I ≤ C_path F, with C_path = d(d-1)/4 (= 3 in d = 4), for every L and k.**
  - Proof: in the unit-block axial gauge of L3s(i), ||W_y - P(c → y)|| = ||W^ax_y - 1||.
  - The composite path has physical length < d/2: per coordinate and per stage at most ((L-1)/2) L^-i, and summing over
    i gives < 1/2.
  - So it has < d/(2ε) fine bonds, each with ||U^ax_b - 1|| ≤ (d-1) ε F / 2 by L3s(i). Multiply. ∎
- **(II) Stage transports by the averaged fields V^(i) (Balaban's natural choice): θ_II ≤ [d(d-1)/4 + d C_δ/(2(L+1))] F.**
  - This holds under the hypotheses of L1e (L ≥ 9 in d = 4, F ≤ F_0).
  - Proof: compare with (I) link by link. Stage i has ≤ d(L-1)/2 links, each within C_δ s_i^2 F of its S, by L1e.
    Then Σ_{i≥1} d((L-1)/2) C_δ L^-2i = d C_δ / (2(L+1)). ∎
- **Consequence.** H' = -Δ_A + a Q_k^† Q_k ≥ min(2, a/2) - 9F^2 - a C_path'^2 F^2 in d = 4, and (iii) holds with this
  gap. Both are uniform in k.
- **Check c5(P).** Measured θ_I/F and θ_II/F are 0.01-0.08, against the bounds 0.5 (d = 2), 1.5 (d = 3) and 3 (d = 4).

**Scope.** L3s is scalar and has no gauge fixing. Balaban's operator acts on 1-forms. See L3g.

#### L3g. Gauge-field fluctuation operator: IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** The covariance (Δ_k,A + a Q_k^dag Q_k)^-1 on Lie-algebra-valued 1-forms, in the
  background L2 with Balaban's gauge fixing, has uniform exponential decay and uniform Hölder/derivative bounds. It has
  a random-walk expansion analytic in the background.
- **Sources.** CMP 95 (1984) 17-40 [v]; CMP 96 (1984) 223-250 [v]; CMP 99 (1985) 389-434 [v].
- **Re-verification route (the L3s method).**
  - (a) A Hodge-Poincaré inequality on unit blocks:
    ||A||_B^2 ≤ C_H (||dA||_B^2 + ||d^* A||_B^2) + |Q_0 A|^2, uniform in ε. This is a discrete de Rham/Poincaré
    statement on a cube, a finite matrix problem for each n, and needs a uniform-in-n proof.
  - (b) The Weitzenböck curvature term ad F is bounded by F under the small-field condition, so it shifts the gap by
    O(F).
  - (c) Combes-Thomas exactly as in (iii).
  - (d) Derivative bounds, which do not follow from (iii) and need a separate local-regularity argument.
- (a) and (d) are the open sub-estimates.
- **[S5]** Abelian analogue [read-skim]: 1512.04373 Lemmas 6, 9, 11 (p.24, 29, 31): random-walk expansions on M-blocks
  for the Landau-gauge Green's function, the minimiser and C_k, C_k^{1/2}, with decay Ce^{-γd}; proofs sketched, citing
  CMP 95, 96, 99, 116. In QED the gauge covariance is background independent, so the background-dependence of L3g is
  not covered. Status unchanged.
- **[S6] What CMP 109 uses from L3g, and its gauge fixing [read].** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
  - Inputs it cites:
    - the operators H_{1,j} and Δ_1 ("defined in Sect. D [13]", CMP 99:389-434);
    - the fluctuation covariance C^{(k)} = (C*Δ^{(k)}C)^{-1} on {Q̃B = 0}, built from (3.156) [13] with the δ gauge
      fixing replaced by the exponential one (p.267-268);
    - Δ_j from (1.66) of CMP 95 (p.291);
    - the exponential decay of δH/δB, Proposition 9 (190) of CMP 102.
    None is reproved.
  - **Gauge fixing, relevant to L3g-ob.** The fluctuation integral carries the block constraint δ(Q̃B') (sharp, (0.17),
    (1.4)) together with a Euclidean-invariant **exponential block-axial gauge on the order-averaged contour variables**,
    exp(-(1/g_k²)Σ_{y,x≠y}[1 - Re tr U(y,x)]) ((0.14), (0.17); U(y,x) as in (0.11)). The estimates use the Landau
    gauge, reached by the transformation u_k of CMP 99:75-102 (p.265).
  - Linearised, the axial term penalises every averaged root-to-x path integral, which is a strictly stronger
    condition than our slice h(A) = 0 (L3g(a)-slice). This confirms L3g-ob's conclusion that a Q-adapted gauge fixing
    absorbs the root (point-source) part. Whether Balaban's combination has a uniform gap is the content of CMP 99:389,
    [not-read].

**L3g(a)-block. [S2] Block Hodge-Poincaré inequality, absolute boundary conditions: PROVEN-HERE.**
- **Statement.** On the bonds of a unit block {0, ..., n-1}^d with spacing ε = 1/n, let d_B be the block-restricted
  exterior derivative and d_B^* its adjoint (Neumann, i.e. absolute). For R- or Lie-algebra-valued 1-forms A:
  ||A||_B^2 ≤ (1/λ_n) (||d_B A||_B^2 + ||d_B^* A||_B^2), with λ_n = 4n^2 sin^2(π/(2n)) ∈ [4, π^2).
  No averaging term is needed.
- **Proof.**
  - The block's cubical cochain complex is the graded tensor product of d copies of the 1D path complex
    C^0 = R^n → C^1 = R^{n-1}, with the derivative scaled by 1/ε and uniform weights.
  - For graded tensor products, the mixed terms d_i d_j^* + d_j^* d_i (i ≠ j) vanish. So the Hodge Laplacian is
    Δ = Σ_i 1 ⊗ ... ⊗ Δ^(i) ⊗ ... ⊗ 1, each factor acting in its own degree.
  - A 1-form component in direction μ lies in C^1_μ ⊗ (⊗_{ν≠μ} C^0_ν). Its spectrum is λ^(1)_{k_μ} + Σ_{ν≠μ} λ^(0)_{k_ν}.
  - In 1D, the nonzero spectra of d d^* (on C^1) and d^* d (on C^0) coincide: (4/ε^2) sin^2(πk/(2n)), for k = 1, ..., n-1
    on C^1 and k = 0, ..., n-1 on C^0.
  - So the minimum is (4/ε^2) sin^2(π/(2n)) = λ_n ≥ 4, by sin x ≥ 2x/π. ∎
- **Check c6(A).** λ_min equals the formula to 1e-8 for d = 2, 3, 4 and n ≤ 8.
- **Why this does not close L3g.** Unlike ||dφ||^2, the global ||d^* A||^2 is a sum over *sites* of combinations that
  include inter-block bonds. It does not split as Σ_B ||d_B^* A_B||^2, so the L3s block-dropping step fails for the
  gauge-fixing term. The global gap must be obtained another way.

**L3g-ob. [S2] Obstruction for S4's complete-axial contours: OPEN (heuristic argument plus numerical confirmation; not
proven).**
- **Mechanism.** The linearised S4 average (L1c) is (QA)(X, μ) = n^-d Σ_y ∫_{Γ_y} A. All the axial legs out of the root
  c_X start along the coordinate-1 line through c_X. After averaging over y, Q contains a line functional
  ℓ_X(A_1) = ∫ w(x_1) A_1(x_1, c_2, ..., c_d) dx_1 with w = O(1). It enters as f(X) - f(X + e_μ), with f(X) = ℓ_X(A_1).
- **Size.** A line has zero H^1-capacity in d = 4 (codimension 3). So ||ℓ||^2_{H^-1} ~ n: a tube test function of
  radius ε has H^1 energy ~ 4πε and line integral O(1). In d = 3 it is ~ log n; in d = 2 it is bounded.
  - c6(B') measures ||Q_row||^2_{H^-1} = 0.196, 0.261, 0.334 at n = 3, 5, 7 (d = 4). The excess over the straight-leg
    part is 0.097, 0.167, 0.242, about 0.034 n, so linear.
  - The same quantity is 0.214 → 0.236 (d = 3, n = 3 to 15, log-like) and constant at 0.307 (d = 2). The straight-leg
    part alone is bounded in every d.
- **Heuristic consequence (not proven).** In Feynman gauge, M = d^*d + dd^* + aQ^†Q has no gap uniform in (n, T) in
  d = 4.
  - Trial A = dφ + σ, with φ of wave number k and σ = Σ_X φ(c_X) τ_X. Here τ_X are cheap tube profiles with
    ℓ_X(τ_X) = 1, which cancel the coarse gradient in QA.
  - The Rayleigh quotient is ≈ k^2 + C/(n k^2), so inf_T λ_min ≲ 2 (C/n)^{1/2}. This needs T ≳ n^{1/4}.
  - On the T = 2 torus of c6 the only low modes are the constants, which are exact eigenvectors with eigenvalue a
    (c6(B)). Their coarse "gradient" cannot be cancelled on a torus, so the effect is invisible at T = 2.
  - The cross-term estimates are not written out. Status: heuristic.
- **Gauge artifact, recorded so that it is not misread.** c6(C) restricts to the complete-axial gauge inside blocks
  without fixing the residual coarse gauge. Then λ_min ≈ 0.95 a/n even in d = 2. This comes from coarse pure-gauge modes
  on the inter-block faces (||A||^2 ~ n, |QA|^2 ~ 1, dA = 0), not from a coercivity failure.
- **What it means.** The scalar L3s is unaffected: its transports are unitary multipliers, not linearised line
  integrals. For the gauge field, a uniform L^2 gap needs one of:
  - contours spread so that each averaging functional is uniformly in H^-1 (the root funnel is the only problem, since
    the straight-leg part is fine);
  - a gauge fixing under which the funnel terms vanish *together with* a coarse gauge fixing;
  - Balaban's own construction, whose exact contour and gauge choices remain [unverified-exact-statement].
- **Caveat on spreading (heuristic).** Spreading cannot fully cure this. Any root-based covariant average has a
  linearised current J with div J = δ_{c_X} - δ_{c_Y}. Its gradient part has |Ĵ|^2/k^2 ~ k^-4 at large k, so
  ||J||^2_{H^-1} ≥ c log n in d = 4, whatever the contours. Equivalently, on pure gauge A = dφ, QA evaluates φ at points,
  and in d = 4 point evaluation is log-unbounded on H^2.
  - So a uniform Feynman-gauge L^2 gap needs a gauge fixing adapted to Q, one that absorbs the point-source part.
  - My unverified guess is that this is Balaban's choice [unverified-exact-statement]. The line part (~n) can be removed
    by spreading; the log part needs the gauge.
- **[S2] Literature cross-check: Dimock, "Covariant axial gauge", arXiv:1410.2798 [v-abs + body via a summarising fetch;
  data only].** This is an abelian treatment following Balaban.
  - [R2-fix] REVIEW_S2 read the abstract and HTML body (published: Lett. Math. Phys. 2015, DOI
    10.1007/s11005-015-0763-0). It is abelian, single-scale, mainly d = 3, so the weight is L^-d (not L^-4). Q sums A
    over paths parallel to the coarse bond, one per fine site, with no centre legs.
  - Covariance is Q ∂λ = ∂ Q λ with the *averaged* scalar gauge function, not a root value.
  - The centre (tree) paths appear only in the gauge-fixing operator τ, averaged over the d! coordinate orders. The gauge
    fixing is δ(τA); Q_k λ = 0 constrains the Faddeev-Popov parameter; Landau uses δ(R_k δ𝒜) and Feynman uses
    exp(-½ α^-1 ⟨δ𝒜, R_k δ𝒜⟩). Balaban is reported to have "averaged over various trees
    to regain the covariance" and to have used exponential gauge fixing in the YM papers.
  - Consistency with L3g-ob: the straight-leg, averaged-gauge form is precisely the part c6 found uniformly H^-1
    bounded, and the Q_k λ = 0 constraint is a Q-adapted gauge fixing of the kind L3g-ob says is needed.
  - [R2-fix] **What carries over to SU(N) and what does not.**
    - Does NOT carry over: the covariance Q∂λ = ∂Qλ with a block-*averaged* gauge function. A nonabelian covariant map
      whose coarse gauge group acts at points (here the roots c_X) necessarily linearises to root covariance,
      Q(dλ) = λ(c_Y) - λ(c_X). So the point-source (log) part of L3g-ob is unavoidable for any such map, by the caveat
      above. The session-2 phrase "revise S4 toward averaged gauge functions" is withdrawn for SU(N).
    - Carries over: straight legs (or spread funnels), which remove the ~n line part, and a Q-adapted gauge term R_k in
      place of the plain dd^*. [S3] L3g(a)-slice below makes this exact at the linearised level: Q_root = Q_str - d h.
    - Order averaging: in Dimock it acts on τ (the gauge fixing), not on Q. For L8b it is an analogy, not the repair.
      The S4' order-averaged map of [S3] has to re-prove L1e and L9a' itself (done in S4' below).
  - So the line part of the obstruction is specific to S4's complete-axial funnels; the point part is intrinsic to root
    covariance and is handled by the gauge slice, not by the averaging.
- **Revised L3g(a) target.** Prove the gap for M_Q = d^*d + (gauge term adapted to Q) + aQ^†Q, with spread contours,
  where the gauge term fixes the components of A that Q sees as point sources. The S4 contours plus the plain Feynman
  term are probably not the right object in d = 4.

**L3g(a)-glob. [S3] Global Hodge-Poincaré inequality for the straight-leg average (abelian, flat, linearised): PROVEN-HERE.**
- **Setting.** Fine torus Λ = (εZ / TZ)^d, ε = 1/n, T ≥ 2 an integer, unit blocks B(X), X ∈ (Z/TZ)^d. Real (or
  Lie-algebra-valued, componentwise) 1-forms A_μ(z) on the bonds (z, z + εe_μ); ⟨A, A'⟩ = ε^d Σ_{z,μ} A_μ(z)A'_μ(z).
  - Straight-leg average (Dimock-type): (Q_str A)(X, μ) = n^-d Σ_{x∈B(X)} ε Σ_{j=0}^{n-1} A_μ(x + jεe_μ), i.e. the block
    average of the unit-length straight line integrals from x to x + e_μ. ||Q_str A||^2 = Σ_{X,μ} |(Q_str A)(X, μ)|^2.
  - ⟨A, ΔA⟩ := ||dA||^2 + ||d^*A||^2.
- **Claim.** ||A||^2 ≤ 5 ⟨A, ΔA⟩ + 2 ||Q_str A||^2. Hence Δ + a Q_str^† Q_str ≥ min(1/5, a/2), uniformly in n, T and d.
- **Proof.**
  - (1) *Lattice Weitzenböck.* On the flat torus the forward and backward differences commute, so summation by parts gives
    ||dA||^2 + ||d^*A||^2 = Σ_{μ,ν} ||∂_ν A_μ||^2: the 1-form Laplacian is the scalar Laplacian on each component (check
    c9(A), exact). The problem splits into d scalar problems, one per component f = A_μ.
  - (2) *Density form.* (Q_str A)(X, μ) = ε^d Σ_z ω_X(z) f(z), with ω_X(z) = ε c(z_μ - X_μ n) on the slab
    S_X = B(X) ∪ B(X + e_μ) and 0 elsewhere, where c(t) = min(t + 1, 2n - 1 - t) for 0 ≤ t ≤ 2n - 2 (a tent along μ, a
    box across). Then ∫ω_X = ε^{d+1} n^{d-1} Σ_t c(t) = 1 and ω_X ≤ εn = 1. So ω_X is a probability density with
    ||ω_X||_∞ ≤ 1, and ||ω_X||_2^2 ≤ ||ω_X||_∞ ∫ω_X ≤ 1. (Check c9(B0).)
  - (3) *Slab Poincaré.* S_X is a Neumann grid of 2n × n^{d-1} sites, spacing ε, volume 2. Its first nonzero
    eigenvalue is min((4/ε^2) sin^2(π/(4n)), (4/ε^2) sin^2(π/(2n))) ≥ 4n^2 (1/(2n))^2 = 1 (sin x ≥ 2x/π). With f̄ the
    slab mean, ||f - f̄||^2_S ≤ ||∂f||^2_S (intra-slab bonds).
  - (4) *Averaging defect.* |ω(f) - f̄| = |∫ω (f - f̄)| ≤ ||ω||_2 ||f - f̄||_S ≤ ||f - f̄||_S. Then
    ||f||^2_S = 2|f̄|^2 + ||f - f̄||^2_S ≤ 4|ω(f)|^2 + 4|ω(f) - f̄|^2 + ||f - f̄||^2_S ≤ 4|ω(f)|^2 + 5||∂f||^2_S.
  - (5) *Covering.* For T ≥ 2 each fine point lies in exactly two slabs S_X (direction μ fixed), and each intra-slab bond in
    at most two. Summing (4) over X: 2||f||^2 ≤ 4 Σ_X |(Q_str A)(X, μ)|^2 + 10 ||∂f||^2. Sum over μ and use (1). ∎
- **Check c9(B)** (d = 2, 3, 4; n ≤ 16, 6, 5; T ≤ 8, 6, 4; a = 1, 0.2, 0.02): measured λ_min = a in every case (the
  constants are the minimisers at these sizes), above the bound min(1/5, a/2). These are instances, not uniformity.
- **Check c9(C).** ||ω||^2_{H^-1} = ω^T (Δ+1)^-1 ω in d = 4 is 0.110, 0.099, 0.096, 0.094, 0.093 at n = 2..6: bounded,
  where the root-based S4 linearisation grew like 0.034 n (c6(B')).
- **Scope.** Abelian, flat background, direct (one-level) average with n = L^k fine sites per block. The iterated
  composite of straight averages, and the nonabelian background-covariant version, are not covered (see L3g(a)-slice).

**L3g(a)-slice. [S3] The root-based average is the straight average up to a coarse exact 1-form dh(A) [R3-fix: not a
"coarse gauge transformation"; h depends on A, and the identity is linearised and abelian only: the nonabelian straight
average is not even covariant, so there is no nonlinear SU(N) analogue]; gap on a gauge slice (abelian, linearised):
the inequality on H_0 is PROVEN-HERE; its use as a fluctuation gap is CONDITIONAL on (FP), which is OPEN.**
- **Identity (exact).** For S4 or S4', with h(X) := avg_σ avg_{y∈B(X)} ∫_{P^σ(c_X → y)} A, the linearised average is
  Q_root A = Q_str A - d h, i.e. (Q_root A)(X, μ) = (Q_str A)(X, μ) - (h(X + e_μ) - h(X)).
  - Proof: ∫_{T^σ_y} A = ∫_{P^σ(c_X→y)} A + ∫_{S_y} A - ∫_{P^σ(c_Y→y+Le_μ)} A. Average over (σ, y). The last term averages
    to h(Y) because y ↦ y + Le_μ is a bijection B(X) → B(Y) and axial paths are translation covariant. ∎
  - Check c8(f): exact (error ≤ 2e-16) for U(1) small fields, where the S4/S4' map is exactly linear, for both S4' and S4.
- **What this explains.** The L3g-ob funnel terms are entirely in the coarse exact part d h (linearised, abelian). They never change the
  gauge-invariant content of Q (for instance its coarse curl dQ_root A = dQ_str A).
- **Slice.** H_0 := {A : h(A) = 0}. Every gauge orbit meets H_0: h(A + dλ) = h(A) + Q_0λ - λ(c), and the map
  λ ↦ Q_0λ - λ(c) is onto coarse scalars (take λ = s_X on B(X) minus its root, 0 at the root: the image is
  s_X(1 - n^-d)). On H_0, Q_root = Q_str, so by L3g(a)-glob
  ⟨A, (Δ + a Q_root^† Q_root) A⟩ ≥ min(1/5, a/2) ||A||^2 for all A ∈ H_0, uniformly in n, T.
- **Open (stated exactly).**
  - (FP) That the gauge-fixed fluctuation integral can be written with the δ(h) slice plus a Feynman term on the residual
    gauge group {λ : Q_0λ = λ(c)}, with a background-independent (abelian) or controlled (nonabelian) Faddeev-Popov
    factor. In the abelian case the factor is A-independent by linearity; this is plausible but not written out.
    **[S11] Written (Lemma FP-ab, L5 [S11]).** The A- and b-independence holds for the legitimate fixing δ(h) plus the
    Feynman term ½||P_resd*A||² on the residual group Λ_res = {λ : λ(c_X) = 0, Σ_{B(X)}λ = 0}. The double fixing with the
    full Δ = d*d + dd* is not an identity: it carries the explicit Gaussian weight W(A) in 2N_c - 1 coarse divergence
    moments. So the slice gap below transfers to the legitimate operator O_FP iff the physical gap on Phys holds
    (OPEN; c24 supports it at small sizes). **[S12] The physical gap is PROVEN (L5 [S12], Proposition PG):
    O_FP ≥ min(c_PG, 4) on H_0, c_PG = min(1, κ)/(3.5·10⁶), uniformly in n and T.** So the abelian linearised (FP) is
    complete for the direct S4' slice.
  - (NA) The nonabelian background version: covariant Weitzenböck with curvature terms of size O(F), a slab version of
    L3s(i) (axial gauge on 2-block slabs, A_max ≤ (d-1)F), and the R3.1 perturbation for transported densities. Each
    piece has an L3s analogue; the combination is not written.
  - (IT) Iterated straight averages: the composite density must stay a probability density with a uniform sup bound on
    an O(1) slab. Not checked. **[S12] Straight part settled exactly (Lemma IT-str, L5 [S12]):** the composite of m one-step
    straight averages IS the direct straight average of side L^m. What remains is (IT'): the gap on the slice of the
    composite root map, whose slice functional is h^{(m+1)} = Mh^{(m)} + hQ_root^{(m)}. **[S13] (IT') PROVEN
    (L5 [S13], Lemma IT-line, Proposition PG^{(k)}):** the composite slice functional obeys
    ε²|h^{(k)}(X)|² ≤ (4L²/(L - 1))||A||²_{B(X)}, uniformly in k, and the physical gap holds for the composite slice
    with C_IT(L) ≤ 3.6·10⁶ at L = 3. (IT) is settled for the abelian linearised step.
    **[S14] Identity half PROVEN (L5 [S14], Proposition NA-FP):** at every critical SU(N) background the Hessian
    annihilates D_UΛ, h_U(D_Uλ) = M_Uλ - λ(c) exactly, and χ_U = (h_U, P_res^UD_U^*) is admissible for every background,
    so FP-ab applies verbatim (direct and composite slices); the constant FP_U now depends on the background. The (NA)
    GAP is OPEN: the linearised soft residual carries a |f|-weighted average of individual far-root funnel traces (the
    defect) that the slice does not kill (NA-F2); routes (R1) enlarged covariant slice, (R2) smooth/rough split.
- **Effect on L3g-ob.** L3g-ob stands as stated (plain Feynman gauge with the root-based Q has no uniform gap,
  heuristically), but it is now explained as a coarse exact-form artifact, and it is removed by the slice. [R3-fix] The
  revised L3g(a) target is met in the abelian linearised case CONDITIONAL on (FP): the slice gap uses Δ = d*d + dd* on
  top of δ(h), a double gauge fixing whose legitimacy is exactly (FP).

### L4. Small-field effective actions and the coupling flow
- **L4a. Structure: IMPORTED-NOT-YET-REVERIFIED.**
  - After k steps, on the small-field region the density is exp(-(1/g_k^2) S_W(V) - Σ_X E_k(X, V)), with polymer
    activities obeying |E_k(X)| ≤ C g_k^{?} e^{-κ d_X}. [The exponent and the norms are unverified.]
  - The coupling recursion, indexed by **resolution** j (finer = larger j), is 1/g_{j+1}^2 = 1/g_j^2 + β_j, with
    β_j → 2 b0 ln L. The coupling grows toward the IR, i.e. as j decreases. [R1-fix: session 1 indexed this by "steps" k,
    which gives the wrong sign if k counts coarse-graining steps.]
  - Sources: CMP 109 (1987) 249-301 [v]; CMP 116 (1988) 1-22 [v]; CMP 119 (1988) 243-285 [v].
  - **[S5]** d = 3 templates [read]: Dimock I Theorem 14 (p.23, eqs. 176-182) and QED Proposition 1 / Theorem 1
    (2009.01156 p.6-8, eqs. 29-30, 37-40). Same structure (density = exp(-action + polymer sum), normalised polymers,
    ||E_k(X)|| ≤ coupling^{1/4-} e^{-κ d_M(X)}), but super-renormalizable: no marginal coupling flow. The 4D content (the
    marginal coupling recursion, its β_j) is not covered. Status unchanged.
  - **[S6] CMP 109 read: L4a is split** (NOTES §9.4-9.8).
    - **L4a-form (IMPORTED-NOT-YET-REVERIFIED; exact statement now [read]).** Theorem 3 (p.264): there are constants
      κ_0, M(κ), γ, ε_0, ε_1, α_0, α_1 such that, if κ ≥ κ_0, M ≥ M(κ) and 0 < g_k ≤ γ for all k ≤ K, the small-field
      actions satisfy the inductive assumptions (1.1)-(1.22). These are:
      - the form (1.3);
      - E^{(j)} = Σ_{X∈D_j} E^{(j)}(X), analytic on U^c_j(X, α_0, α_1), with |E^{(j)}(X)| ≤ E_0 e^{-κd_j(X)} (1.18).
        There is NO positive power of g, so the session-1 placeholder "C g_k^{?}" was wrong in form;
      - gauge and Euclidean invariance.
      After the β-subtraction, the renormalised terms obey |V^{(j)}(X)| ≤ O(1)(L^jη)^{4+α} e^{-κd_j(X)} (0.29). This
      gives the k-uniform bulk bound (0.30).
      - **CMP 109 does not complete this proof.** The localisation and cluster expansion of (2.13) are deferred to
        "the next paper" (p.298), CMP 116 (1988) 1-22, "II. Cluster expansions" [v-crossref, not-read].
      - Its hypotheses, where they can be checked: G = SU(N) is compact, semisimple and in U(N); d = 4; L odd, but
        Balaban needs "L odd > 11", while our L1e needs L ≥ 9 and the checks use L = 3. **[R56-fix]** The torus side
        does NOT match: Balaban's torus has side 2L^m, ours (since session 4) has unit-lattice side 4L^M, and
        4L^M ≠ 2L^m for odd L. Whether his proofs are side-agnostic is [unverified].
      - The averaging hypothesis holds only up to the S4'/(0.4) pairing difference (L1d [S6]).
    - **L4a-flow (IMPORTED-NOT-YET-REVERIFIED; deferred by the source).** Theorem 2 (p.259) covers SU(2) only, "the
      restriction ... is superficial". For small γ and g there is a bare g_0(ε,g) with g_k ∈ ]0,γ], g_K = g, and
      1/g² + β(K - k) log L ≤ 1/g_k² ≤ 1/g² + β'(K - k) log L, with unspecified constants 0 < β ≤ β' (0.31). "A proof
      of this theorem ... will be given in a separate paper" [not-read].
      - **Correction:** PROOF.md's "β_j → 2b_0 ln L" is NOT stated in CMP 109. It is the perturbative expectation
        [inference]. CMP 109 gives only the two-sided logarithmic form.
      - The sign of (0.18) (1/g_0² = 1/g_1² + β_1, k counting coarse-graining steps) confirms the [R1-fix] convention
        of L4c, with j = K - k.
      - The E8.3/E7.0 corollaries need λ_K := 2N·β' log L below the λ_c of E8.3 (λ_c/λ_AF ≈ 6.1 for SU(2)). (0.31)
        alone does not give this, since β' is unspecified. They stay conditional on L4a-flow with β' < 6.1·2b_0.
    - **L4a-Π (the β-function as the coefficient of the transverse polarisation tensor): PROVEN-HERE [S6]**, below.
- **L4a-Π. [S6] Transverse structure of a gauge-invariant lattice polarisation tensor: PROVEN-HERE.** (A re-derivation
  of CMP 109 §5, (5.6)-(5.42), by a direct Taylor argument rather than Balaban's Laurent decomposition.)
  - **Setting.** Π_μν(z), z ∈ Z^d, d ≥ 2, real, with Σ_z e^{δ|z|}|Π_μν(z)| < ∞ for some δ > 0. It is the bond-bond
    kernel of a quadratic form, Π_μν(x - y) = Π(⟨x, x+e_μ⟩, ⟨y, y+e_ν⟩), extended to reversed bonds by oddness.
    Assume:
    - (S) symmetry, Π_μν(z) = Π_νμ(-z);
    - (H) hypercubic covariance, as induced by the action of the signed permutations on bonds, CMP 109 (5.4), (5.6),
      (5.7);
    - (G) transversality, Σ_μ Π_μν(x - y) evaluated against (dλ)_μ vanishes for all λ, CMP 109 (5.9).
    (G) holds when Π is the Hessian at 0 of a gauge-invariant functional. In CMP 109 it is derived from the Ward
    identity (4.15).
    **[R56-fix]** The scalar colour form (Π ∝ δ_ab, so that Π_μν is a single real kernel) is justified by CMP 109
    (1.21) [read, NOTES §9.4].
  - **Centred transform.** Π̃_μν(p) := Σ_z exp(-ip·(z + (e_μ - e_ν)/2)) Π_μν(z). This is the Fourier transform in the
    difference of bond midpoints. It is analytic in the strip |Im p| < δ.
  - **Claim.**
    Π̃_μν(p) = β (δ_μν Σ_κ s_κ² - s_μ s_ν) + R_μν(p), where s_κ = 2 sin(p_κ/2), R is analytic and R = O(|p|⁴), and
    β = Σ_z (z_1 + ½)(z_2 - ½) Π_12(z) = Σ_z z_1 z_2 Π_12(z) (CMP 109 (1.22)).
  - **Proof.**
    - (H) in midpoint coordinates. A coordinate reflection ε maps the midpoint of bond (x, μ) to the reflected
      midpoint, and multiplies the bond variable by ε_μ (orientation). Hence Π̃_μν(εp) = ε_μ ε_ν Π̃_μν(p).
      Permutations give Π̃_{πμ,πν}(πp) = Π̃_μν(p).
    - Reflecting all axes gives Π̃(-p) = Π̃(p). Reality gives Π̃(-p) = conj Π̃(p). So Π̃ is real and even, and its
      Taylor series at 0 has only even orders: Π̃ = A + Q(p) + O(p⁴), with A constant and Q quadratic.
    - **Order 0.** For μ ≠ ν, reflecting axis μ alone gives A_μν = -A_μν = 0. Permutations give A_μμ = a for all μ.
    - **Order 2.**
      - For μ ≠ ν, Q_μν is odd in p_μ, odd in p_ν and even in every other variable, so Q_μν = c p_μ p_ν, with c
        independent of (μ, ν) by permutations.
      - Q_μμ is even in each variable, so Q_μμ = b p_μ² + e Σ_{κ≠μ} p_κ².
    - **(G) in Fourier form.** (dλ)^_μ(p) = (e^{ip_μ} - 1)λ̂ = i s_μ e^{ip_μ/2}λ̂. Collecting the midpoint phases,
      (G) reads Σ_ν Π̃_μν(p) s_ν(p) = 0 for all p.
      - At order p: Σ_ν A_μν p_ν = a p_μ = 0, so a = 0.
      - At order p³ (using s_ν = p_ν + O(p³) and A = 0): c p_μ Σ_{ν≠μ} p_ν² + b p_μ³ + e p_μ Σ_{κ≠μ} p_κ² = 0 for all
        p. Hence b = 0 and c = -e.
    - So Q_μν(p) = e(δ_μν |p|² - p_μ p_ν). Set β := e = -c = -∂_1∂_2 Π̃_12(0) = Σ_z m_1 m_2 Π_12(z), with
      m = z + (e_1 - e_2)/2.
    - Replacing p by s(p) changes Q by O(p⁴). R := Π̃ - β(δ s² - s s^T) is analytic and O(p⁴).
    - Equality of the centred and uncentred second moments: (z_1 + ½)(z_2 - ½) = z_1 z_2 + ½(z_2 - z_1) - ¼. Here
      Σ_z Π_12 = Π̂_12(0) = 0. The first moments vanish because the uncentred Π̂_12 = e^{+i(p_1-p_2)/2}Π̃_12 [R56-fix: sign of the phase; harmless since Π̃_12 = O(p²)] =
      -βp_1p_2 + O(p³) has no linear term. ∎
  - **What it re-verifies, and what it does not.** It re-verifies the load-bearing algebra of CMP 109 §5: the marginal
    part of any symmetric, gauge-invariant quadratic local functional is a multiple β of the lattice Wilson quadratic
    form, and β is the mixed second moment (1.22). It does not compute β_j for the actual RG step, i.e. Π from the
    fluctuation integral (2.13), nor show that β_j → 2b_0 log L. That is L4a-flow, plus the one-loop identification of
    L4b.
  - **Check c17(A)** (8/8 with part B; 0.7 s, 39 MB; first run). Functionals: the plaquette action, plaquettes +
    1×2 rectangles, and three random closed lattice loops symmetrised over the 384-element hypercubic group (d = 4).
    - Π̃(0) = 0 and the transversality hold to ≤ 5e-14.
    - The centred, uncentred (1.22) and diagonal extractions of β agree to 1e-12. Plaquette c_0 = 1 gives β = 1; with
      rectangles c_1 = -1/12, β = c_0 + 8c_1 = 1/3 exactly.
    - |R(2t)|/|R(t)| = 16.00, i.e. R = O(p⁴); R ≡ 0 for the pure plaquette.
    - These are instances; the proof above is general.
- **L4b. One-loop coefficient b0 = 11N/(48π^2): IMPORTED-AND-REVERIFIED.**
  - **Hypotheses (imported).**
    - The Seeley-DeWitt coefficient a2 = tr[(1/12) Ω_{μν} Ω_{μν} + (1/2) E^2] for -(D^2 + E) in 4D (Vassilevich,
      Phys. Rept. 388 (2003) 279-360 [v]).
    - The background-field Feynman-gauge fluctuation operator -D^2 δ_{μν} + 2i ad F_{μν}, with adjoint ghosts -D^2
      [v-R1: Abbott, NPB 185 (1981) 189-203].
  - **Derivation (here).**
    - (1/2) a2_vec - a2_gh = [(1/2)(4·(1/12)·(-C_A) + (1/2)·4 C_A) + (1/12) C_A] F^a F^a = (11/12) C_A F^a F^a.
    - With UV proper-time cutoff Λ and IR scale μ: Γ ⊃ -(16π^2)^-1 ln(Λ^2/μ^2)(11/12) C_A ∫ F^a F^a.
    - Against S = (4g^2)^-1 ∫ F^a F^a this gives 1/g^2(μ) = 1/g_0^2 - (11/3) C_A (16π^2)^-1 ln(Λ^2/μ^2), so
      d(1/g^2)/d ln μ = 2 b0 with b0 = 11 C_A/(48π^2) and C_A = N.
    - The sign gives infrared growth (asymptotic freedom).
  - **Check c2(A).** Exact to 1e-12 for SU(2), SU(3) and SU(4).
  - **Lattice universality of the two log coefficients that enter (c2(B)):**
    - E^2: the slope of ∫_BZ (ω + m^2)^-2 against ln(1/m^2) is 1.0056 → 1.0017 times 1/(16π^2).
    - Ω^2: unit-charge lattice scalar in constant flux on a 64^2 torus; the slope is 0.94-1.10 times 1/(96π^2). This
      is a finite diagnostic, finite-size limited.
  - **Not covered.** That Balaban's lattice β_k → 2 b0 ln L is part of L4a, not reverified.
- **L4c. AF recursion arithmetic: PROVEN-HERE.**
  - Statement: let 1/g_{j+1}^2 = 1/g_j^2 + β_j, with |β_j - β| ≤ C g_j^2, β = 2 b0 ln L > 0, and C g_0^2 ≤ β/2. Then:
    - (a) 1/g_0^2 + jβ/2 ≤ 1/g_j^2 ≤ 1/g_0^2 + 3jβ/2;
    - (b) Σ_j g_j^{2+δ} < ∞ for every δ > 0;
    - (c) Σ_j g_j^2 = ∞.
  - Proof: by induction, g_j ≤ g_0, so β/2 ≤ β_j ≤ 3β/2; sum to get (a). (b) and (c) follow by comparison with
    Σ j^{-1-δ/2} and Σ j^-1. ∎
  - **Consequence used in L7b (heuristic, [R1-fix] softened):** per-scale error *bounds* of order g_j^2 are not
    summable. So a convergence proof by summing absolute per-scale bounds needs geometric decay L^{-κ(j-m)}, or
    O(g_j^{2+δ}). O(g^2) errors could still telescope or cancel; this is not excluded.

### L5. Large-field R-operation: IMPORTED-NOT-YET-REVERIFIED
- **Sources.** CMP 122 (1989) 175-202 [v-abs: "the basic step of the R operation"]; CMP 122 (1989) 355-392 [v].
- **Content (paraphrase).** Large-field regions are suppressed by exp(-c p(g_k)^2 / g_k^2) per unit block, with
  p(g) = (-log g)^p, and are localised and exponentiated.
- **[S5]** The R-operation is in NO open exposition: Dimock II p.31 Remark 3 [read] ("This difficult step is not
  necessary for this model"); none in QED either. What Dimock does have [read] is the per-level large-field factor
  without recycling: e^{-c_2 p_j^2} per M-cube in his normalisation (III Lemma 13, eq. 166) and e^{-p_j} per cube in QED
  (Lemma 23, eq. 471), with no 1/g^2. The "/ g_k^2" in the paraphrase above is therefore convention-dependent and
  unverified. Status unchanged; L5 can only be re-verified from CMP 122 (1989) 175-202 and 355-392.
- **[S6]** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
  - CMP 109 contains no large-field estimate ("the simplifying assumption that integrals are restricted to small
    fields", p.250).
  - Its small-field thresholds are:
    - fixed ε_0 on the background curvature (1.2);
    - fixed ε_1 on the dimensionless fluctuation B' ((2.9); alternatively g_kε_1/γ_k).
    So the excluded fluctuations cost ~ε_1²/g_k² in action. This is not the p(g)² form of the old paraphrase, whose
    "/g_k²" question is therefore moot for CMP 109's own cut.
  - CMP 122 abstracts [read-abs, OSTI; NOTES §10]: Part I "construct[s] the renormalization operation of the
    expressions connected with the large field regions"; Part II completes "the proof of the ultraviolet stability of
    four-dimensional pure gauge field theories".
  - **Why L5 is load-bearing in d = 4 and not in d = 3: Proposition LF-count (L6loc [S6], PROVEN-HERE).** The
    unrenormalised per-level large-field count of Dimock's template diverges along any flow of the form (0.31) whenever
    the excluded configurations cost a/g_k² with aβ' ≤ 4. **[R56-fix]** In Balaban's normalisation this covers every
    ε_1 below an explicit bound, ε_1 ≲ (8/(||Δ||β'_B))^{1/2} with β'_B ≈ 4Nb_0 [inference, conditional on the
    one-loop rate and on L4a-flow; not "every small-field threshold" unconditionally]. So L5 must
    deliver *renormalised* large-field contributions, with per-level weights summable against L^{4(K-k)}. No open
    source states such a bound (NOTES §10).
- **[S7] One-cube R-operation: target pre-stated in RTARGET.md (written before the derivation), attacked in d = 2.**
  Status of L5 unchanged: IMPORTED-NOT-YET-REVERIFIED. New: Proposition R2D-iso (PROVEN-HERE) and the OPEN item R4D-iso.
  - **d = 2 has the same wall (RTARGET §0).** LF-count's arithmetic with N_k ∝ L^{2(K-k)} gives divergence whenever
    aβ' ≤ 2. With the one-loop O(N) rate β' ≈ (N-2)/(2π) [m; inference for the lattice rate] and a single-bond cut
    ~~(cost a = ε_1²/2 ≤ 2), every threshold is in the divergent window for 3 ≤ N ≤ 8~~. **[R78-fix]** ε_1²/2 is the cut
    bond's own term, a lower bound; the divergence needs an upper bound on the cheapest excluded configuration, whose
    cost is a ≈ ε_1²/(2R_eff) = ε_1² (linearised; R_eff = 1/2 between neighbours of Z²; REVIEW_S7_S8 computed
    cost/ε_1² = 1.0115, 1.0007, 1.0001 on 11², 41², 101² boxes). "a ≤ 2 for any cut" is deleted (antiparallel bond:
    ≈ 2 + π²/2). Corrected window: every ε_1 ≲ (4π/(N-2))^{1/2} [linearised; inference on the one-loop rate]. The wall
    is present in d = 2 for small ε_1, by the same mechanism. Sanity check: the O(3) instanton
    (a = 4π) gives aβ' = 2 = d exactly, i.e. the known log-divergent small-instanton gas of the lattice O(3) model [m].
    **[R78-fix] caveat:** with the standard lattice action, lattice-scale Q = 1 "dislocations" have action below the
    continuum 4π [m, Berg-Lüscher 1981; not re-read], so on the lattice aβ' < 2 strictly and the divergence there is
    geometric, not marginal.
  - **Literature correction.** Balaban CMP 198 (1998) 493-534 is the large-field operation of his LOW-TEMPERATURE
    N-vector series (d ≥ 3, an infrared problem) [read-abs, Rutgers record; search snippets for CMP 167/182/196], not a
    2D UV construction. The full-lattice UV analysis of the 2D O(N) model was open as of 1999, "so far only performed in
    the hierarchical case" (Kopper, CMP 202 (1999) 89-126, math-ph/9902020, introduction [read-skim]). So there is no
    open (or known closed) 2D template to compare with; d = 2 is a testbed, not a solved case.
  - **Proposition R2D-iso (one-cube, one-step renormalised large-field bound, isolated cube, d = 2): PROVEN-HERE [S7].**
    - *Setting* (RTARGET §1): 2D O(N), N ≥ 2; block □ of L×L sites, L odd, centred at 0; exterior neighbours Γ (4L
      sites) frozen at m_y; soft block-spin term (κ/2g²)|Φ - L^{-2}Σ_{x∈□}n_x|²; interior-bond cut
      χ = Π 1{|n_x - n_x'| < ε_1}; ρ := ∫(1-χ)e^{-S}dσ / ∫χe^{-S}dσ. Background family m_y(s) = n(sy),
      Φ(s) = L^{-2}Σ_{x∈□}n(sx), with n : R² → S^{N-1}, |∂^α n| ≤ 1 for 1 ≤ |α| ≤ 4. ~~B := the nearest-neighbour bonds
      of □ ∪ Γ~~ **[R78-fix]** B := the Γ-Γ bonds (the L - 1 nearest-neighbour bonds along each side of the exterior
      ring; corners excluded, as Γ excludes them), so b = 2(L - 1) bonds per direction. B is D_4- and
      point-reflection symmetric, and A_B(m) := Σ_B(1 - m_y·m_y') is a function of the data m alone, as RTARGET §2
      pre-stated. (The session-7 B included bonds with an end inside □, where A_B used the continuum interpolant n; that
      is not a function of the data.)
    - *Claim* = (R2D) as pre-stated: for every a < ε_1²/4 there are C, s_0, g_0 depending on (L, N, κ, ε_1, a) only with
      ρ(s) = ρ_0(g) + δβ(g)A_B(m(s)) + R(s), 0 ≤ ρ_0 ≤ Ce^{-a/g²}, |δβ| ≤ Ce^{-a/g²} (both background-independent),
      |R(s)| ≤ Ce^{-a/g²}s⁴, for all g ≤ g_0, all n, all |s| ≤ s_0. The same holds for log(1 + ρ).
    - *Proof.*
      1. **Size.** Numerator: on {χ = 0} some interior bond has 1 - n_x·n_x' = ½|n_x - n_x'|² ≥ ε_1²/2, and every term of
         S is ≥ 0, so the numerator is ≤ e^{-ε_1²/(2g²)} (σ has mass 1). Denominator: restrict to the caps
         |n_x - n(0)| ≤ rg, r := ε_1/4, g ≤ 1; there χ = 1. Using |n(sy) - n(0)| ≤ s|y|_1 ≤ sL and
         |Φ(s) - n(0)| ≤ sL, and (u + v)² ≤ 2u² + 2v², S ≤ C_0 + Bs²/g² on the caps, with C_0 = C_0(L, κ, ε_1) and
         B := (4L + κ)L². Cap measures are ≥ c_N(rg)^{N-1}. Hence ρ(s) ≤ C_1 g^{-(N-1)L²} e^{-(ε_1²/2 - Bs²)/g²}, and
         for |s| ≤ s_0 := ε_1/(2√B): ρ(s) ≤ C_1 g^{-(N-1)L²} e^{-ε_1²/(4g²)}. (s_0 is g-independent: (F4) avoided.)
      2. **Derivatives.** χ does not depend on s; S does, polynomially through m(s) and Φ(s). Since
         ∂_s^j(n_x·m_y(s)) = n_x·(y·∇)^j n(sy), |∂_s^j S| ≤ Λ_j/g² with Λ_j ≤ (4L + 4κ)(2L)^j. By Faà di Bruno,
         |∂_s^q e^{-S}| ≤ B_q(Λ/g²)^q e^{-S} for g ≤ 1, with Λ := (4L + 4κ)2L. The integrands are ≥ 0 and the
         indicator is s-independent, so |Num^{(q)}| ≤ B_q(Λ/g²)^q Num, |Den^{(q)}| ≤ B_q(Λ/g²)^q Den, and by the
         quotient rule |ρ^{(q)}(s)| ≤ B'_q(Λ/g²)^q ρ(s). (No analyticity is needed: (F1) avoided, because the soft
         constraint is polynomial in Φ.)
      3. **Evenness.** The point reflection ι : x ↦ -x maps □, Γ, the interior bonds and B to themselves and preserves
         dσ, S's form and χ. Since m_{-y}(s) = m_y(-s) and Φ(-s) = Φ(s) (re-index x ↦ -x), ρ(-s) = ρ(s). (The family
         with s < 0 is the family of n∘(-1), which obeys the same bounds.) So ρ'(0) = ρ'''(0) = 0, and Taylor gives
         ρ(s) = ρ(0) + ½ρ''(0)s² + R_4(s), |R_4| ≤ (s⁴/24)sup_{|σ|≤s}|ρ^{(4)}(σ)|. ((F2) avoided.)
      4. **Vacuum part.** At s = 0 the background is constant, m_y = Φ = n(0). Rotating the integration variables
         (σ is O(N)-invariant), ρ(0) = ρ_0(g) does not depend on n(0).
      5. **Marginal part.** ρ is a smooth O(N)-invariant function of (m, Φ) ∈ (R^N)^Γ × R^N (S is polynomial in m, Φ).
         At the constant point e := n(0), the stabiliser O(N-1) forces the gradient components to be ∥ e (γ_y e, γ_Φ e)
         and the Hessian on e^⊥-components to be h_{yy'}·(u·v). Put u_μ := ∂_μn(0) ∈ e^⊥ and
         w_{μν} := ∂_μ∂_νn(0), with e·w_{μν} = -u_μ·u_ν (differentiate n·n = 1 twice). Then m'_y(0) = Σ_μ y_μu_μ,
         Φ'(0) = 0 (Σ_{x∈□}x = 0), m''_y(0) = Σ y_μy_νw_{μν}, and
         ρ''(0) = Σ_{μν}T_{μν} u_μ·u_ν, T_{μν} := Σ_{y,y'}h_{yy'}y_μy'_ν - Σ_yγ_y y_μy_ν - γ_Φ L^{-2}Σ_{x∈□}x_μx_ν.
         T depends on g and the fixed data only. The square's symmetry group D_4 maps the geometry to itself, so
         ρ''(0)[n∘R] = ρ''(0)[n], i.e. T = RTR^T for R ∈ D_4. D_4 acts irreducibly on R², so T = c(g)·1:
         ρ''(0) = c Σ_μ|∂_μn(0)|². ((F3) avoided: one marginal operator.)
      6. **Identification with A_B.** A_B(m(s)) = ½Σ_B|n(sy) - n(sy')|² is even in s (B is ι-symmetric), so
         A_B(m(s)) = (s²/2)·bΣ_μ|∂_μn(0)|² + R_B(s) with |R_B| ≤ C_B s⁴ (fourth derivatives ≤ 1). Put δβ := c/b and
         R := R_4 - δβR_B. **[R78-fix]** With B = the Γ-Γ bonds (b = 2(L - 1)): every bond of B joins two data sites,
         the expansion |n(sy + se_μ) - n(sy)|² = s²|∂_μn(0)|² + (odd in s) + O(s⁴) holds with C_B = C_B(L), and the
         odd terms cancel over the ι-symmetric B; steps 6-7 go through verbatim with this b.
      7. **Bounds.** |c| ≤ |ρ''(0)| for a test background with |∂_1n(0)| = 1, ∂_2n(0) = 0, so |c| ≤ B'_2(Λ/g²)²sup ρ.
         With step 1, every term is ≤ C g^{-(N-1)L²-8}e^{-ε_1²/(4g²)}s^{0,0,4}, and g^{-p}e^{-ε_1²/(4g²)} ≤
         C_a e^{-a/g²} for a < ε_1²/4 and g ≤ g_0. For log(1 + ρ): it is even in s, smooth in ρ ≥ 0, and the same
         steps apply with c → c/(1 + ρ_0). ∎
    - *Consequence (the RTARGET §2 summation; arithmetic) **[conditional on BG-reg, hence on L2]** [R78-fix]: it applies
      R2D-iso, a theorem about smooth s-families, to RG backgrounds, which are lattice fields. [S9] The 4D lattice
      replacement is GT-lat/R4D-lat (L5 [S9]); the 2D analogue is argued there, not written.* A level-j cube seen from level k has s = L^{-(k-j)}; there
      are L^{2(k-j)} of them per level-k cell, so the field-dependent remainders sum to ≤ C Σ_{j≤k}L^{-2(k-j)}w_j ≤
      C' sup w, uniformly in k, K. The δβ shifts sum to Σ_j|δβ(g_j)| ≤ Ce^{-a/g²}Σ_nL^{-aβn} < ∞ along the flow, and are
      ≪ g_j⁴. **So, for isolated cubes, LF-count's divergence sits entirely in the field-independent vacuum part ρ_0**,
      which is removed by the normalisation constants (as log Z^{(j)}(1), E^{(j)}(1) are in CMP 109 (1.3)). It
      cancels in normalised expectations and in Z_K/Z_K^ref with matching constants, which is why it is "uniform in K":
      it is cancelled, not bounded.
    - *What R2D-iso does NOT give (the exact walls of the full R-operation, now named):*
      - **W1 (localisation in a fluctuating sea).** The exterior is frozen. In the real integral the neighbours are
        small-field integration variables that respond to the large-field defect. A proof needs a polymer/cluster
        expansion with the large-field cube as a defect, giving ρ_full(□) = local terms with exponential tails and the
        same s-derivative bounds. This is Dimock's "difficult technical problem" of localising the characteristic
        functions (Rome p.57 [read]) and Balaban's CMP 122 II "Localization, exponentiation" [not-read].
      - **W2 (nested, multi-scale large fields).** Step 5 expands around a smooth background. Inside a region that is
        large-field at several consecutive scales the background is not smooth and the expansion has no small
        parameter. R2D-iso covers only cubes whose ~~coarse neighbourhood is small-field~~ **[R78-fix]** background is a
        smooth s-family (a small-field lattice background gives no derivative bounds; that is BG-reg).
      - **W3 (hard constraints).** With a normalised block spin, or Balaban's δ(M(U)V^{-1}) with log-based M, the
        V-dependence enters through the fibre of M. Large fluctuations reach M's branch set (an eigenvalue -1 of some
        Z_y: the off-D set of E8/S4''), where M is not smooth, so step 2 fails as written. The soft constraint avoids
        this; Balaban's δ-constraint would need a fibre-smoothness lemma on the large-field event, or a separate
        (E8*-type) probability bound for the branch set. **[S9] After decision 4, W3 is a comparison-branch wall**: the
        main path uses the soft kernel (D4-norm), which is smooth everywhere.
  - **4D SU(N): what changes (item R4D-iso, OPEN [S7]; [S8] now PROVEN-HERE, see Proposition R4D-iso below; the
    bracketed OPEN content is discharged by Lemma GT).** The isolated-cube statement transfers with these changes:
    - *Cut and positivity.* Use a gauge-invariant plaquette cut |1 - U_p| < ε_1. By inequality (B) its cost is
      s(U_p) ≥ ε_1²/(2N) (Balaban normalisation: a_B ≥ ε_1²/2 with tr 1 = 1). Wilson terms are ≥ 0, so step 1 holds with
      p = dim of the cube's link variables (no gauge fixing is needed for a compact group with frozen exterior). Balaban's
      own cut is on the gauge-fixed fluctuation B' and is not gauge invariant by itself, a difference to track.
    - *Constraint.* A soft gauge-covariant constraint, e.g. (κ/g²)Σ_cΣ_Γ[1 - N^{-1}Re tr(V(c)^{-1}U(Γ))] over the
      contours of (0.4), is polynomial in V and U, so step 2 holds verbatim. With Balaban's δ-constraint, W3 applies.
    - *Symmetry structure (the one new lemma).* Steps 3-4 transfer: point reflection gives evenness in s, and
      G-conjugation plus gauge invariance give a constant vacuum part. Step 5 must become a gauge-invariant Taylor lemma
      for background links U_b(s) = P exp(is∫_bA(s·)): order s² vanishes, since the only candidate is linear in F and
      tr F = 0 with no hypercubic-invariant linear form; order s⁴ is c·Σtr F_μνF_μν, because Λ²R⁴ is irreducible under
      the hyperoctahedral group B_4 and reflections exclude ε^{μνρσ}tr F_μνF_ρσ, while tr(DDF) = 0; odd orders vanish.
      The remainder is then O(s⁶) and sums against L^{4(k-j)} (α = 2). [The B_4 irreducibility and the order-s² and
      order-s⁴ classification are argued here, not yet written as a proof for general analytic gauge-invariant
      functions of links. This is the OPEN content of R4D-iso, together with s_0 for the 4D cube.]
    - W1 and W2 are unchanged in 4D. W3 is sharper, because Balaban's (0.4) uses log in the averaging itself.
- **[S8] Session 8: targets pre-stated in RTARGET.md §5-7 before the derivations. Status of L5 unchanged:
  IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE: Lemma GT, Proposition R4D-iso (moved from
  OPEN), Lemma W1-sym (with W1-def and W1-size). New OPEN: W1-loc. Check c19 (10/10).
  - **Lemma GT (gauge-invariant Taylor lemma): PROVEN-HERE [S8].**
    - *Setting* (RTARGET §6). Data D = a finite B_4- and ι-symmetric set of lattice links around the site 0 (and, for
      R4D-iso, the coarse links V(c), c = (0, ±Le_μ)), each carrying a G-valued variable, G = SU(N), N ≥ 2. Background:
      a smooth su(N)-connection A on R⁴ in radial gauge x^μA_μ(x) = 0, ||∂^αA_μ||_op ≤ 1 for 1 ≤ |α| ≤ 6; A^{(s)}(y)
      := sA(sy); D(s) := the parallel transporters of A^{(s)} along the straight segments of the data (convention
      U' = UA along the path; gauge action U_b → h(x)U_bh(y)^{-1}, A → hAh^{-1} - (dh)h^{-1}).
    - *Claim.* Let F be C⁶ near the trivial configuration 1 and along the family, and invariant under (i) all
      gauge transformations of the data, (ii) B_4 (signed permutations about 0, which contains ι = -1). Put
      f(s) := F(D(s)). Then f is even; f'(0) = f''(0) = f'''(0) = 0; f^{(4)}(0)/24 = c_F Σ_{μ<ν}||F_μν(0)||²_HS
      with c_F independent of A; and |f(s) - f(0) - c_F s⁴Σ||F_μν(0)||²| ≤ (s⁶/720)sup_{|σ|≤|s|}|f^{(6)}(σ)|.
    - *Proof.*
      1. **Radial gauge is no loss.** Every smooth A is gauge-equivalent to a radial-gauge one (Fock-Schwinger); the
         transporters of h·A are h(x)U_bh(y)^{-1}; (h·A)^{(s)} = h(s·)·A^{(s)}. So f is the same in every gauge, by (i).
      2. **Order of the data.** In radial gauge A(0) = 0 and ∂_μA_ν(0) + ∂_νA_μ(0) = 0 (differentiate x^νA_ν = 0
         twice), so ∂_νA_μ(0) = ½F_νμ(0). Hence A^{(s)}(y) = s²y^ν∂_νA(0) + O(s³), and for small s the data logs
         X_b(s) := log D_b(s) obey X_b(s) = s²X_b^{(2)} + O(s³), with (first Magnus term; path-ordering corrections are
         O(|A^{(s)}|²) = O(s⁴)) X_b^{(2)} = ∫_0^1(x + te_μ)^ν dt·½F_νμ(0) = ½x^νF_νμ(0) for b = (x, x + e_μ) (F_μμ = 0),
         and X^{(2)} = 0 for the coarse segments (0, ±Le_μ). So X^{(2)} = 𝓛(Φ) with Φ := F(0) ∈ su(N) ⊗ Λ²R⁴, 𝓛 linear.
      3. **Order s² vanishes (no relevant term).** F̃(X) := F(exp X) near 0. Constant gauge transformations fix 1 and
         act by Ad, so F̃∘Ad_h = F̃, hence DF̃(0)∘Ad_h = DF̃(0): each component of DF̃(0) is an Ad-invariant element of
         su(N)* ≅ su(N), i.e. central, i.e. 0 (G semisimple; cf. CMP 109 (4.14) [read, NOTES §9.6]). With X(0) = X'(0)
         = 0, Faà di Bruno gives f'(0) = 0, f''(0) = DF̃(0)X''(0) = 0, and f^{(4)}(0) = DF̃(0)X^{(4)}(0) +
         3D²F̃(0)(X''(0), X''(0)) = 12 D²F̃(0)(𝓛Φ, 𝓛Φ).
      4. **Evenness (odd orders vanish).** (ι^*A)_μ(x) := -A_μ(-x) is radial, its transporters are the ι-image of
         those of A (orientation reversed), and A^{(-s)} = ι^*(A^{(s)}). By (ii) for ι, f(-s) = f(s).
      5. **One invariant at order s⁴.** Q(Φ) := ½D²F̃(0)(𝓛Φ, 𝓛Φ) = f^{(4)}(0)/24. D²F̃(0) is Ad-invariant (step 3) and
         𝓛 is Ad-equivariant, so Q is Ad-invariant. For R ∈ B_4, R·A := (x ↦ RA(R^{-1}x)) is radial, its data are the
         R-permuted data, (R·A)^{(s)} = R·(A^{(s)}), and (R·A)'s curvature at 0 is Λ²(R)Φ; by (ii), Q∘Λ²(R) = Q. Now:
         - *Λ²R⁴ is absolutely irreducible under B_4.* The sign flips diag(ε) act on e_μ∧e_ν by ε_με_ν; the six lines
           have pairwise distinct characters of (Z_2)⁴ (the flip of coordinate k negates e_μ∧e_ν iff k ∈ {μ,ν}), so a
           (complex) endomorphism commuting with B_4 is diagonal in this basis; the permutations act transitively on the
           six pairs, so its diagonal is constant. (c19 P1: character norm 1; the rotation subgroup gives 2, i.e.
           self-dual ⊕ anti-self-dual, so the reflections are needed.)
         - su(N) is absolutely irreducible under Ad (its complexification sl(N,C) is irreducible).
         - Invariant endomorphisms of V ⊗ W under G_1 × G_2 are End_{G_1}(V) ⊗ End_{G_2}(W) = R. Hence every Ad × B_4
           invariant symmetric bilinear form on su(N) ⊗ Λ² is a multiple of Σ_{μ<ν}⟨Φ_μν, Φ'_μν⟩_HS (c19 P2: dimension 1
           for SU(2)). So Q(Φ) = c_F Σ_{μ<ν}||Φ_μν||²_HS. In particular ε^{μνρσ}tr Φ_μνΦ_ρσ (odd under reflections) is
           excluded: (R4-F2) avoided.
      6. Taylor with Lagrange remainder at order 6, odd terms and f''(0) zero. ∎
    - *What GT uses:* only gauge invariance, B_4 and ι invariance, and C⁶. It does not use positivity or the
      specific F; it applies to ρ, to log(1 + ρ) and to A_B alike.
  - **Proposition R4D-iso (one isolated 4D SU(N) cube, frozen exterior, one step): PROVEN-HERE [S8] (moved from OPEN).**
    - *Setting* = RTARGET §6: cube □ of L⁴ sites (L odd ≥ 3) centred at the site 0; integration over the interior links
      (Haar); frozen data = the other links of plaquettes meeting the interior, the contour links of the neighbouring
      blocks, and V(c); action S = (1/g²)[Σ_{p∩int≠∅}(1 - N^{-1}Re tr U_p) + κΣ_t(1 - N^{-1}Re tr W_t)], W_t the
      closed words U(Γ)U([x,x'])U(Γ')^{-1}V(c)^{-1} over Balaban's axial families (all orders, both ends; B_4-symmetric);
      cut χ = Π_{p⊂int}1{||1 - U_p||_op < ε_1}; ρ := ∫(1-χ)e^{-S}/∫χe^{-S}; f(s) := ρ(D(s)).
    - *Claim* = (R4D) as pre-stated: for every a < ε_1²/(4N) there are C, s_0, g_0 depending on (L, N, κ, ε_1, a) only
      with ρ(s) = ρ_0(g) + δβ(g)A_B(D(s)) + R(s), 0 ≤ ρ_0 ≤ Ce^{-a/g²}, |δβ| ≤ Ce^{-a/g²} (background-independent),
      |R(s)| ≤ Ce^{-a/g²}s⁶, for g ≤ g_0, all A as in GT, |s| ≤ s_0. The same for log(1 + ρ).
    - *Proof.*
      1. **Invariances.** Gauge: a gauge transformation of the data at sites outside the interior, together with the
         same transformation h_0 of the V(c) at 0 and the change of variables U_int → h·U_int (Haar invariance), leaves
         S, χ and dU_int invariant; so ρ(h·D) = ρ(D). B_4 and ι: the cube, the data, the word family and χ are
         B_4-symmetric about 0. Smoothness: S is a polynomial in the matrix entries, χ is data-independent, the
         denominator is > 0; so ρ is C^∞.
      2. **Size, priced by inequality (B).** On {χ = 0} some interior plaquette has ||1 - U_p||_op ≥ ε_1, and by (B)
         (1 - N^{-1}Re tr U_p) ≥ ||1 - U_p||²_op/(2N) ≥ ε_1²/(2N); all terms of S are ≥ 0 and Haar has mass 1, so the
         numerator is ≤ e^{-ε_1²/(2Ng²)}. Denominator: restrict to ||U_b - 1||_op ≤ rg (b interior), r := ε_1/8, g ≤ 1;
         there every interior plaquette has ||1 - U_p|| ≤ 4rg < ε_1, so χ = 1. By step 2 of GT and ||A^{(s)}(y)|| ≤
         s²|y|_1 on the data region, every data variable obeys ||D_b(s) - 1|| ≤ C_L s², C_L = O(L²). Each term of S has
         1 - N^{-1}Re tr W ≤ ½||1 - W||²_op ≤ ½(ℓ_W(rg + C_Ls²))² ≤ ℓ_W²(r²g² + C_L²s⁴), ℓ_W the word length. So
         S ≤ C_0 + Bs⁴/g² on the balls, C_0 = C_0(L, κ, ε_1), B = B(L, κ). Haar balls: μ{||U - 1|| ≤ δ} ≥ c_Nδ^{N²-1}
         (δ ≤ 1) [elementary]. With p := (N²-1)·#(interior links): ρ(s) ≤ C_1g^{-p}e^{-(ε_1²/(2N) - Bs⁴)/g²}, and for
         |s| ≤ s_0 := (ε_1²/(4NB))^{1/4} (g-independent; (R4-F4) avoided): ρ(s) ≤ C_1g^{-p}e^{-ε_1²/(4Ng²)}.
      3. **Derivatives.** The data are transporters of A^{(s)}, smooth in s with ||∂_s^jD_b(s)|| ≤ C_j(L) for |s| ≤ 1
         (smooth dependence of U' = Ua(t;s) on the parameter, a(t;s) = A^{(s)}(x + te_μ), with ||∂_s^ja|| ≤ C_j(L) from
         the bounds on A; unitarity) [elementary]. So |∂_s^jS| ≤ Λ_j/g², and exactly as in R2D-iso step 2 (positive
         integrands, s-independent indicator, quotient rule) |f^{(q)}(s)| ≤ B'_q(Λ/g²)^qρ(s), q ≤ 6.
      4. **Structure.** GT applies to f (step 1): f(s) = ρ(0) + c_ρs⁴Σ||F_μν(0)||² + R_f, |R_f| ≤ (s⁶/720)sup|f^{(6)}|.
         ρ_0 := ρ(0) is the trivial-data value, background-independent. A_B := Σ_{p∈B}(1 - N^{-1}Re tr U_p) over the
         plaquettes B of the data region (B_4- and ι-symmetric, n_B per plane) is itself gauge- and B_4-invariant, so by
         GT A_B(D(s)) = c_Bs⁴Σ||F_μν(0)||² + R_B with c_B = n_B/(2N) (1 - N^{-1}Re tr e^Y = ||Y||²_HS/(2N) + O(Y⁴);
         c19 P8: 9 = 36/4 for SU(2)) and |R_B| ≤ C'_Bs⁶. Put δβ := c_ρ/c_B, R := R_f - δβR_B.
      5. **Bounds.** Test connection A_ν(x) = ½x^μF⁰_μν with F⁰_12 = -F⁰_21 = T, ||T||_op = 1, ||T||²_HS = 2, other
         components 0 (radial, ||∂A|| ≤ ½, higher derivatives 0): |c_ρ| ≤ sup|f^{(4)}|/48. With steps 2-3 every term is
         ≤ Cg^{-p-12}e^{-ε_1²/(4Ng²)}·{1, 1, s⁶}, and g^{-q}e^{-ε_1²/(4Ng²)} ≤ C_ae^{-a/g²} for a < ε_1²/(4N), g ≤ g_0.
         log(1 + ρ) satisfies the hypotheses of GT directly, with the same bounds. ∎
    - *Consequence (arithmetic) **[conditional on BG-reg, hence on L2]** [R78-fix]. The proof above is correct; this
      paragraph applies it to lattice RG backgrounds, which needs BG-reg. [S9] Replaced on lattice backgrounds by
      R4D-lat + BG-sum (L5 [S9]): conditional on BG-b only, with α = 1 in place of 2.* A level-j cube against a level-k background has s = L^{-(k-j)}; L^{4(k-j)} such cubes
      per level-k cell give Σ_{j≤k}L^{4(k-j)}L^{-6(k-j)}Cw_j ≤ C'sup w (α = 2), uniformly in k, K. The δβ shifts sum
      along the flow (Σ_n e^{-a/g²}L^{-aβn} < ∞) and are ≪ g_j⁴. So **in 4D, for isolated cubes, LF-count's divergence
      sits entirely in the field-independent ρ_0**, removed by normalisation, exactly as in d = 2. All four failure
      modes R4-F1..F4 are avoided as pre-stated.
    - *Scope.* Frozen exterior (W1), smooth background (W2), soft constraint (W3) and the gauge-invariant cut on
      interior plaquettes (Balaban's cut is on the gauge-fixed B'; difference still tracked) are as pre-stated "not
      success" items. c19 tests GT on explicit instances, including an exactly integrated single-link function; it does
      not evaluate the cube integral ρ itself.
  - **Check c19 (criteria checks/c19_criteria.md, written before checks/c19_gauge_taylor.py): 10/10 PASS** (first run,
    18 s, 64 MB, load 1.9, 36% free memory, nice 10, BLAS threads 1; output checks/c19_out.txt).
    - P1 Λ² character norm under B_4 = 1 (rotation subgroup: 2). P2 dim of Ad × B_4-invariant forms on su(2)⊗Λ² = 1.
    - Six radial-gauge SU(2) backgrounds (abelian, self-dual F(0), anti-self-dual F(0), three generic), box |x_μ| ≤ 1.
      F1 (Wilson sum), F2 (squares, 1×2 rectangles, adjacent-plaquette products), F3 (Σ over the 8 star links of the
      exact single-link Haar integral log[I_1(2β|K_b|)/(β|K_b|)]):
      evenness |f(0.2) - f(-0.2)| ≤ 4e-12 (P3 at s = 0.4, 0.2, 0.1); (f(s)-f(0))/s⁴ converges like s² (difference ratios 3.80-4.23); c_F universal to relative spread
      ≤ 5e-8 (c = 9.0000000, -77.999999, -2.1185381), self-dual and anti-self-dual agreeing; remainder ratios
      R(0.1)/R(0.05) = 63.4-64.6 (s⁶); gauge invariance under a non-radial gauge ≤ 3e-12.
    - Controls have power: plane-(1,2)-only sum (B_4 broken) gives c spread 0.80 across backgrounds; half-space sum
      (ι broken) has an odd part 1e-3..1e-2 at s = 0.2 scaling like s⁵ (ratios 27.8-36.5; criterion met on 4 of 6
      backgrounds, required on 1).
    - **[R78-fix] Disclosure.** Before its first and only run, the c19 script was edited (12:38:38 UTC per the session-8
      transcript, REVIEW_S7_S8 (5)). The edit removed a stray line, replaced sampled B_4 elements by the B_4 generators,
      and **reduced the random Ad elements in P2 from the pre-registered 20 to 5**. The last change deviates from the
      criteria file. It was not disclosed in session 8, and is disclosed now (also appended to checks/c19_criteria.md).
      The reviewer judged it mathematically harmless: 5 generic elements generate a dense subgroup, and the gap is 6.6e14.
    - **[R78-fix] Check c19b (reflection-matters control; criteria checks/c19b_criteria.md written before
      checks/c19b_reflection_control.py): 5/6, overall FAIL as pre-registered** (15 s, 37 MB, load 2.0, 36% free memory,
      nice 10, BLAS threads 1; output checks/c19b_out.txt). Control: the clover density Q_ε = Σε^{μνρσ}(-½)Re tr(C_μνC_ρσ)
      at 0, which is gauge-, rotation- and ι-invariant and reflection-odd.
      - Q1 (gauge, ≤ 6e-17), Q2 (ι-even, ≤ 4e-17) and Q4 (reflection-odd: Q(R·A) = -Q(A) to 5e-18) PASS.
      - **Q5 PASS, which is the control's point:** c_SD = +1.9999999936, c_ASD = -1.9999999762. A rotation-invariant
        function that is odd under reflections has a second order-s⁴ invariant, so c_SD ≠ c_ASD. c19's agreement
        c_SD = c_ASD (to 5e-8) is therefore evidence that the reflection hypothesis of GT is load-bearing.
      - Q6 PASS: G = F1 + Q_ε has c spread 0.43 across backgrounds (universality fails).
      - **Q3 FAIL:** the pre-registered rate window [3, 5] for |r(0.2) - r(0.1)|/|r(0.1) - r(0.05)| was missed on 3 of
        5 backgrounds (5.15, 17.3, 2.70). A disclosed post-run diagnostic (scratchpad s9/c19b_diag_out.txt; different
        random backgrounds, since the generator state differs) shows r(s) converging to a finite limit, with successive
        difference ratios approaching 4 only at s ≤ 0.1 (e.g. 0.066/0.016 = 4.1, 0.019/0.005 = 3.9). So Q_ε has no
        order-s² term. The failure is in the rate criterion at s = 0.2, where s⁸ terms of the clover function are not yet
        negligible. The criterion is not edited.
  - **W1 in d = 2 (RTARGET §5): partial. The exact wall is named (W1-loc). Three lemmas PROVEN-HERE [S8].**
    - **Lemma W1-def (exact defect identity).** In Setting W1, fix any states (cut/released) of the blocks ≠ □_0. Let
      Z^{cut}, Z^{rel} be the integrals with χ_0, resp. 1, for □_0, and ⟨·⟩_cut the probability measure of Z^{cut}.
      Then Z^{rel}/Z^{cut} = 1 + ⟨ρ_□(n_Γ, Φ_0)⟩_cut, with ρ_□ exactly R2D-iso's function of the exterior ring
      m = n_Γ and Φ_0. *Proof.* S = S_□(n_□; n_Γ, Φ_0) + S_rest, with S_rest independent of n_□ (crossing bonds only join
      □ to Γ); integrate n_□ first (Fubini): Z^{rel} = ∫(rest)(Den_□ + Num_□) = ∫(rest)Den_□(1 + ρ_□). ∎ So the
      fluctuating-exterior defect is R2D-iso's ρ averaged over the conditioned sea; F(Φ) := log(1 + ⟨ρ_□⟩_cut), and
      ∂_{Φ_c}⟨ρ_□⟩_cut = -(κ/g²)Cov_cut(ρ_□, Φ_c - L^{-2}Σ_{x∈c}n_x) for c ≠ □_0: derivatives are truncated
      correlations of ρ_□ with block averages. **[R78-fix]** Higher Φ_c-derivatives (c ≠ □_0) are pure cumulants,
      ∂_{Φ_{c_1}}···∂_{Φ_{c_q}}log⟨e^{...}⟩ = (-κ/g²)^q × (joint cumulant of the X_{c_j} := Φ_{c_j} - L^{-2}Σ_{x∈c_j}n_x and
      ρ_□), because ∂²S/∂Φ_c∂Φ_{c'} = (κ/g²)δ_{cc'} is constant. W1-red relies on this. Derivatives with some c_j = □_0
      also hit ρ_□'s direct dependence on Φ_0 (see W1-loc, restated).
    - **Lemma W1-size (exact size reduction).** Let δ_0 := ε_1/(2√(4L + κ)) and E := {n_Γ : no e ∈ S^{N-1} has
      |n_y - e| ≤ δ_0 for all y ∈ Γ and |Φ_0 - e| ≤ δ_0}. Then, with P_rel the measure of Z^{rel},
      ⟨ρ_□⟩_cut ≤ [C_1g^{-(N-1)L²}e^{-ε_1²/(4g²)} + P_rel(E)] / (1 - P_rel(E)).
      *Proof.* On E^c, R2D-iso step 1 with caps around e gives S ≤ C_0 + (4L + κ)δ_0²/g² (crossing bonds ½(rg + δ_0)²,
      constraint (κ/2)(δ_0 + rg)², (u+v)² ≤ 2u² + 2v²), hence ρ_□ ≤ C_1g^{-(N-1)L²}e^{-ε_1²/(4g²)}. On E:
      ⟨ρ_□1_E⟩_cut = Z^{rel}[□_0 large, E]/Z^{cut} ≤ Z^{rel}[E]/Z^{cut} = P_rel(E)(1 + ⟨ρ_□⟩_cut). Rearrange. ∎
      So the size half of W1 is exactly a collar large-deviation bound for the sea, not a property of the cube.
    - **Lemma W1-sym (symmetry + locality ⇒ renormalised form, for functions of the whole block-spin field).** Block torus
      Λ_T (T odd, representatives |c_μ| ≤ (T-1)/2, □_0 at 0). Let F be C⁴ on a neighbourhood of the family below,
      (i) O(N)-invariant, (ii) invariant under the stabiliser D_4 of 0 (which contains ι), and (iii) for 0 ≤ q ≤ 4
      |∂_{c_1,i_1}···∂_{c_q,i_q}F| ≤ C_qw e^{-κ_d max_j|c_j|_1} on the family (κ_d: decay rate; κ stays the constraint
      strength; RTARGET §5's decay "κ" is this κ_d). Family Φ_c(s) = n(sc), |∂^αn| ≤ 1
      (1 ≤ |α| ≤ 4), |s| ≤ s_0. Then F(Φ(s)) = f_0 + δβA_B(Φ(s)) + R(s), f_0 independent of n, |f_0|, |δβ| ≤ C'w,
      |R| ≤ C'ws⁴, C' depending on (C_q, κ_d, N, B) only, uniform in T.
      *Proof.* (1) |Φ_c^{(j)}(s)| = |(c·∇)^jn(sc)| ≤ |c|_1^j, so by Faà di Bruno |f^{(q)}| ≤ Σ C_kN^{k/2}w·S_k with
      S_k ≤ kΣ_R(2R+1)^{2k}R^qe^{-κ_dR} < ∞, T-independent. (2) Φ(-s) = Φ(s)∘ι, so f is even. (3) f(0) = F(e,…,e) is
      independent of e by (i). (4) At the constant point the O(N-1) stabiliser makes DF_c = γ_ce and the Hessian on
      e^⊥ equal to h_{cc'}(u·v); with u_μ := ∂_μn(0), e·∂_μ∂_νn(0) = -u_μ·u_ν, f''(0) = Σ_{μν}T_μνu_μ·u_ν,
      T_μν = Σ_{cc'}h_{cc'}c_μc'_ν - Σ_cγ_cc_μc_ν (absolutely convergent by (iii)). (5) Test backgrounds
      n(x) = cos(a·x)e + sin(a·x)v, |a_μ| ≤ 1, realise u_μ = a_μv; D_4 maps [-1,1]² to itself and (ii) gives
      T_sym = σT_symσ^T; D_4 is absolutely irreducible on R² (sign flips separate the axes, the swap equates them),
      so f''(0) = tΣ_μ|u_μ|². (6) A_B as in R2D-iso step 6 with b_B bonds per direction; δβ := t/b_B, R := R_4 - δβR_B. ∎
      R2D-iso steps 3-7 are the special case F = ρ with finitely many arguments.
      **[R78-fix] Seam.** On the block torus the family Φ_c(s) = n(sc) over the representatives |c_μ| ≤ (T-1)/2 is not
      periodic: across the seam |Φ_c - Φ_{c'}| can be O(sT), so the family leaves D_reg(ε_0) and (iii) "on the family"
      cannot be supplied there. Restriction: n is constant outside a ball of radius R_0 about 0 with sR_0 < T/2 (so the
      family is constant across the seam), or n(s·) is T-periodic. The lemma as a calculus statement is unaffected
      (the proof never uses periodicity); its use in W1-red needs the restriction.
    - **Corollary W1-red.** If W1-loc (below) holds, the weak (single-defect) form of (W1) holds with w = Ce^{-a/g²},
      uniformly in T, **for the seam-safe families above** [R78-fix]: (i), (ii) hold for F = log(1 + ⟨ρ_□⟩_cut)
      (S, σ and the cuts are O(N)- and D_4-invariant), and W1-loc is (iii). **[R78-fix]** W1-loc's polynomial g-loss is
      allowed: W1-sym's C' is linear in the C_q, and C g^{-p}e^{-a/g²} ≤ C'e^{-a'/g²} for a' < a.
    - **W1-loc (OPEN, the exact W1 wall for the weak (single-defect) form [R78-fix]; a statement about the small-field
      sea only; [S9] the main-path version is the 4D restatement in L5 [S9], and this 2D version is the testbed).** In Setting W1 with every block
      ≠ □_0 cut, there are C_q, κ_d, a, s_0, g_0 > 0 depending on (L, N, κ, ε_1) only such that for g ≤ g_0, all T and
      Φ = Φ(s), |s| ≤ s_0:
      - (W1-LD, size) P_rel(E) ≤ Ce^{-a/g²} (by W1-size this gives the q = 0 bound);
      - ~~(W1-cl, decay) the joint truncated correlations of ρ_□ with q ≤ 4 block averages Φ_{c_j} - L^{-2}Σ_{x∈c_j}n_x
        are ≤ C_qe^{-a/g²}(g²/κ)^q e^{-κ_d max_j|c_j|_1} under ⟨·⟩_cut (this is (iii) for q ≥ 1).~~
      - **[R78-fix] Restated.** The (g²/κ)^q gain is dropped: it is probably unattainable (by Gaussian integration by
        parts, Cov(ρ_□, X_c) ~ Σ_y⟨∂_{n_y}ρ⟩C(n_y, X_c) with ∂ρ ~ ρ/g² and C ~ g²/κ, i.e. no gain), and it is
        unnecessary (W1-sym tolerates any polynomial g-loss). The direct Φ_0-dependence of ρ_□ is included. The family
        is seam-safe (as in W1-sym), and s_0 ≲ δ_0 is required (otherwise the neighbouring Φ_c alone push the collar into
        E). **(W1-cl, restated)** for 1 ≤ q ≤ 4 and blocks c_1, …, c_q (c_j = □_0 allowed):
        |∂_{c_1,i_1}···∂_{c_q,i_q} log(1 + ⟨ρ_□⟩_cut)| ≤ C_q g^{-p_q} e^{-a/g²} e^{-κ_d max_j|c_j|_1}. By W1-def these
        are combinations of joint cumulants of ρ_□ and the X_{c_j} under ⟨·⟩_cut, times (κ/g²)^{q'}, and of the mixed
        cumulants of ∂^k_{Φ_0}ρ_□; |∂^k_{Φ_0}ρ_□| ≤ C(Λ/g²)^kρ_□ by the R2D-iso step-2 argument gives the k-th direct term.
      - [S9] The size half is better stated through Lemma W1-size' (L5 [S9]): (W1-LD) is then a large-deviation bound
        for the sea with □_0 removed, with no released-measure probability.
      *Why it is not proven here.*
      - W1-LD needs the sea's stiffness at the δ_0 scale. The cheap route, local exponential moments ⟨e^{tS_c}⟩ via
        frozen-exterior bounds (Hölder: ∫χe^{-(1-t)S_c} ≤ Z_c^{1-t}, then R2D-iso's cap bound for Z_c), regenerates
        ⟨e^{t'S_{c'}}⟩ on the neighbouring blocks with t' = Mt, M ≈ 2(4L + κ)C_P·deg ≫ 1 (C_P the block Poincaré
        constant). The recursion does not close. [Route obstruction, not a no-go.]
      - W1-cl is exponential clustering of the block-pinned low-temperature O(N) sea, i.e. the small-field cluster
        expansion, the 2D analogue of L4a-form (Balaban defers it to CMP 116, NOTES §9.6) and of Dimock I Lemma 21.
      - (W1-F3, as pre-stated) Dimock I Thm 27 (NOTES §1) needs an ultralocal measure. The sea is ultralocal only after
        the Gaussian change of variables with the random-walk-expanded covariance (the L3 machinery). So the
        multi-defect strong form (W1-a/b) is not reached either.
      - Illustration [N = 2 only, outside the target's N ≥ 3; argument sketched, not counted]: if ε_1 < √2 and
        □'s cut also covers its crossing bonds, a winding-1
        exterior ring with all exterior bonds < ε_1 (L large) forces Den = 0, i.e. ρ = ∞, since bond angles < π/2 give zero
        vorticity on every plaquette of □, so □'s boundary loop, and with it the exterior ring, has winding 0. So no size bound uniform over the small-field exterior exists in general.
        The collar must enter jointly, as in W1-size.
    - **Outcome vs RTARGET §5.** Strong form (W1-a/b/c): not reached. Weak form: reduced exactly to W1-loc
      (W1-def + W1-size + W1-sym). Failure modes met: W1-F1 in the precise form W1-LD; W1-F2 = W1-cl; W1-F3 as stated.
      W1-F4 avoided (s_0 and a are g-independent in every reduction step).
    - **4D.** [S9: superseded by the 4D restatement in L5 [S9] (W1-size', W1-LD-cond, hypothesis (DF)).] W1-def and W1-size transfer verbatim (Fubini; caps; inequality (B) for the numerator). W1-sym's 4D
      analogue is GT with the decay-summability step (1) [argued, not written; not counted]. W1-loc's 4D form is the
      clustering of the 4D small-field sea, i.e. L4a-form/L3g territory.
  - **W2** is pre-stated only (RTARGET §7); not attacked.
- **[S9] Session 9: decision 4, BG-reg, W1-loc in 4D. Targets pre-stated in RTARGET.md §9-10. Status of L5 unchanged:
  IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE: Lemma D4-norm, Lemma GT-lat (with Proposition R4D-lat), Lemma W1-size'
  (with Corollary W1-LD-cond). BG-reg stays OPEN, narrowed to BG-b. W1-loc stays OPEN, restated in 4D and reduced to
  (DF) + Thm 27. Check c20 (VALID; model background SUMMABLE).
  - **Decision 4: the RG kernel.** For a coarse link c = (X, X + e_μ), let M̄_c(U) := (d!L^d)^{-1}Σ_σΣ_{y∈B(X)}T^σ_y(U)
    be the mean of the S4' contour transporters (S4' pairing: the same order σ at both ends). ||M̄_c||_op ≤ 1. The kernel is
    K(V, U) := Π_c k_c,  k_c := exp(-(κ/g²)[1 - N^{-1}Re tr(V_c^{-1}M̄_c(U))]) / 𝒩(M̄_c(U)),
    𝒩(M) := ∫_{SU(N)} exp(-(κ/g²)[1 - N^{-1}Re tr(V^{-1}M)]) dV,
    and e^{-S_{k+1}(V)} := ∫K(V, U)e^{-S_k(U)}dU. Then ∫K(V, U)dV = 1 for every U, so the step is exact (Z is preserved).
    It is gauge covariant: under a fine gauge transformation g, M̄_c → g(c_X)M̄_cg(c_Y)^{-1}, and Haar invariance gives
    𝒩(hMh'^{-1}) = 𝒩(M); so K(g|_roots·V, g·U) = K(V, U). The term N^{-1}Re tr(V^{-1}M̄) is the mean over contours of
    N^{-1}Re tr(V^{-1}T^σ_y), by linearity of the trace. So R4D-iso's constraint Σ_t(1 - N^{-1}Re tr W_t) is this one with
    κ rescaled by the number of contours. The S4' paired family is B_4-symmetric (L1 re-checks: axis permutations and
    reflections map the order set to itself), so R4D-iso applies to it.
  - **Lemma D4-norm (the normalised kernel): PROVEN-HERE [S9].** R4D-iso holds verbatim for the normalised kernel, i.e.
    with the interior integrand e^{-S} replaced by e^{-S}Π_{c at □}𝒩(M̄_c)^{-1}. The constants are the same, except that
    the power of g^{-1} grows by 2(N²-1)·#{c at □}. The same holds for R4D-lat below.
    *Proof.*
    (1) *Invariance and smoothness.* log 𝒩(M) is invariant under M → hMh'^{-1}, so it is gauge invariant. It is
        B_4-invariant because the family is. 𝒩 > 0 is the integral of an entire function of the entries of M, so it is
        C^∞.
    (2) *Size.* The integrand of 𝒩 is ≤ 1, so 𝒩 ≤ 1, and the denominator lower bound of R4D-iso step 2 only improves.
        For the numerator: let V_0 maximise Re tr(V^{-1}M) over SU(N), and φ(V) := N^{-1}[Re tr(V_0^{-1}M) -
        Re tr(V^{-1}M)] ≥ 0. Since |tr(XM)| ≤ N||X||_op||M||_op and ||V_0^{-1} - V^{-1}||_op = ||V - V_0||_op, φ(V) ≤
        ||V - V_0||_op. Hence 𝒩(M) ≥ e^{-(κ/g²)(1 - N^{-1}Re tr V_0^{-1}M)}·e^{-1}c_N(g²/κ)^{N²-1} (a Haar ball of radius
        g²/κ ≤ 1). So k_c = e^{-(κ/g²)φ(V_c)}/∫e^{-(κ/g²)φ} ≤ e c_N^{-1}(κ/g²)^{N²-1}. The numerator bound of R4D-iso
        step 2 therefore holds with this polynomial factor per coarse link.
    (3) *Derivatives.* M̄_c depends on s through the frozen contour links. d/ds log 𝒩 = ⟨(κ/(g²N))Re tr(V^{-1}∂_sM̄)⟩
        under the probability measure ∝ the integrand of 𝒩. The q-th derivative is a sum over set partitions of joint
        cumulants of the bounded variables (κ/(g²N))Re tr(V^{-1}∂_s^jM̄), each ≤ (κ/g²)C_j(L). So |∂_s^q log 𝒩| ≤
        B_q(Λ'/g²)^q for g ≤ 1. By Faà di Bruno, R4D-iso step 3 holds with Λ → Λ + Λ'. The integrands are still positive
        and the indicator is still s-independent.
    (4) GT applies by (1). ∎
    - *D4-obs [R910-fix: now an OPEN item on the main path, counted in the tally].* Under the soft kernel the RG
      variables V are auxiliary random variables. They
      are not the S4'' iterates V^(m) that define the observable algebra O (S6). S6 is unchanged: every observable is a
      function of the fine U, and its expectation is an integral over U. The RG representation re-expresses the
      integrand only. Comparing the block laws of the soft V with those of S4''(U) (which L7a/L8a use) is an extra step
      that the main theorem will need. [R910-fix] REVIEW_S9_S10 classified it as a proof obligation created by
      decision 4: **OPEN item D4-obs** = compare the block laws of the soft RG variables V with those of S4''(U) used by
      L7a/L8a, or run the RG with observable sources.
  - **BG-reg [S9] (RTARGET §9).**
    - **Lemma GT-lat (lattice Taylor lemma): PROVEN-HERE [S9].**
      *Setting.* Box B̂ := {|x_μ| ≤ R_0} around the site 0. For R4D-iso, R_0 = (3L-1)/2, which contains every data link.
      R̂ := the links with both ends in B̂. C := a B_4-symmetric set of straight segments c from 0 of length L (the
      coarse links), carrying V_c. Data D = ((U_b)_{b∈R̂}, (V_c)_{c∈C}). π_x := the complete-axial path from 0 to x (move
      in coordinate 1, then 2, 3, 4). These paths form a spanning tree of B̂. For a plaquette p = (x; μ, ν) ⊂ B̂ (μ < ν),
      h_p := hol(π_x)U_p hol(π_x)^{-1} is the plaquette transported to 0, and P̂_p := log h_p (principal log). Put
      Φ_μν(D) := P̂_{(0;μ,ν)}, and
        ε_2(D) := max_p||P̂_p||_op,  ε_3(D) := max_p||P̂_p - Φ_{μν(p)}(D)||_op,  ε_V(D) := max_c||log(V_cS_c^{-1})||_op,
      where S_c is the straight fine transporter along c. Under a gauge transformation h_p, Φ and V_cS_c^{-1} are all
      conjugated by g(0), so ε_2, ε_3 and ε_V are gauge invariant.
      *Claim.* There are r_1, C depending on R_0 only with the following property. Let F be C³ on {ε_2 + ε_V ≤ r_1} and
      invariant under gauge transformations of the data and under B_4. Then on that set
        |F(D) - F(1) - c_F Σ_{μ<ν}||Φ_μν(D)||²_HS| ≤ C K_F [ε_2(ε_3 + ε_V) + (ε_3 + ε_V)² + ε_2³],
      where c_F is Lemma GT's constant and K_F := sup(||D²F̃|| + ||D³F̃||) over the chart ball |Z| ≤ Cr_1 (tree and
      radial charts, F̃ = F∘exp).
      *Proof.*
      1. **Tree gauge.** Some gauge makes hol(π_x) = 1 for every x ∈ B̂. In it, for b = (x, x + e_μ) ∈ R̂,
         U_b = hol(γ_b), with γ_b := π_x b π_{x+e_μ}^{-1} a closed loop at 0 in B̂. The 2-complex of the box is simply
         connected, so in the free group on the γ's each γ_b is a finite product Π_i w_i r_i^{±1} w_i^{-1} of conjugates of
         the transported plaquette loops r_i = π_{x_i}∂p_iπ_{x_i}^{-1}. The number of factors and the conjugator lengths
         are bounded by C(R_0), since R̂ is a fixed finite complex.
         Products and conjugations of unitaries give ||U_b - 1|| ≤ Σ_i||h_{p_i} - 1|| ≤ Cε_2. Then BCH, with Ad_{hol(w_i)}
         = 1 + O(Cε_2), gives X_b := log U_b = Σ_i ±P̂_{p_i} + E_b with ||E_b|| ≤ Cε_2². The decomposition is
         combinatorial, so it is the same word for any data.
         The straight segments c are tree paths: the complete-axial path to ±Le_μ moves in coordinate μ only. So in tree
         gauge S_c = 1 and V_c = exp(Y_c), with ||Y_c|| ≤ ε_V.
      2. **Reference data.** Let D^Φ := (exp(𝓛Φ), V_c := S_c(exp 𝓛Φ)), Φ := Φ(D), where 𝓛 is GT's map: (𝓛Φ)_b =
         ½x^νΦ_νμ for b = (x, x + e_μ). On the lattice d(𝓛Φ)_p = Φ_μν exactly, because the curl of ½x^ρΦ_ρμ around the
         unit plaquette is ½(Φ_μν - Φ_νμ). By BCH and transport, P̂_p(D^Φ) = Φ_{μν(p)} + O(C|Φ|²). Since |Φ| ≤ ε_2,
         ||P̂_p(D) - P̂_p(D^Φ)|| ≤ ε_3 + Cε_2². In tree coordinates Z = (X, Y), step 1 gives
         |Z(D) - Z(D^Φ_tree)| ≤ C(ε_3 + ε_2² + ε_V) and |Z(D^Φ_tree)| ≤ Cε_2. (Y(D^Φ) = 0 because V^Φ_c = S_c.)
      3. **No linear term.** Constant gauge transformations preserve the tree gauge and act on Z by Ad. So, exactly as in
         GT step 3, each component of DF̃(0) is an Ad-invariant element of su(N)*, hence 0. Therefore
         |F(D) - F(D^Φ)| ≤ sup|D²F̃|·|Z - Z^Φ|(|Z^Φ| + |Z - Z^Φ|) ≤ CK_F(ε_3 + ε_2² + ε_V)(ε_2 + ε_3 + ε_V).
      4. **The quadratic term is GT's.** F(D^Φ) = F̃_rad(𝓛Φ) = F(1) + Q(Φ) + R_3, with Q(Φ) := ½D²F̃_rad(0)(𝓛Φ, 𝓛Φ)
         and |R_3| ≤ CK_Fε_2³. (DF̃_rad(0) = 0 as in step 3.) The lattice map is exactly B_4-equivariant,
         R·(𝓛Φ) = 𝓛(Λ²(R)Φ). For Re_μ = +e_{μ'} this is immediate. For Re_μ = -e_{μ'} the image link is reversed, and the
         value -½x^νΦ_νμ matches 𝓛(Λ²(R)Φ) on the forward link because Φ_μμ = 0. Coarse straight links map to coarse
         straight links. So Q is Ad × B_4-invariant, and GT step 5 gives Q = c_FΣ||Φ_μν||², with the same c_F (GT's
         c_F is defined by this Q, since X^{(2)} = 𝓛Φ there).
      5. Combine steps 3 and 4. Use ε_2²(ε_2 + ε_3 + ε_V) ≤ ε_2³ + ε_2(ε_3 + ε_V) for ε_2 ≤ 1. ∎
      *Remarks.* GT-lat needs only C³; it needs neither ι separately nor a smooth family. The s-family GT is the case
      ε_2 ~ s², ε_3 ~ s³, ε_V = 0. There GT-lat gives s⁵ where GT gives s⁶: GT-lat trades the power that ι supplies
      for the absence of smoothness. **This discharges BG-reg (a). No interpolation lemma between lattice and smooth
      backgrounds is needed.**
    - **Proposition R4D-lat (counted with GT-lat): PROVEN-HERE [S9].** Let ρ be R4D-iso's weight with the D4-norm kernel.
      There is ε_* = (ε_1²/(4NB))^{1/2} (B from R4D-iso step 2; ε_* is g-independent) such that for every a < ε_1²/(4N)
      and g ≤ g_0, and for all data D with ε_2 + ε_V ≤ ε_* (in a chart ball):
        ρ(D) = ρ_0 + δβ·A_B(D) + R(D),  |R(D)| ≤ Ce^{-a/g²}[ε_2(ε_3 + ε_V) + (ε_3 + ε_V)² + ε_2³],
      with ρ_0 and δβ the SAME background-independent numbers as in R4D-iso. The same holds for log(1 + ρ).
      *Proof.*
      - Size: in tree gauge ||U_b - 1|| ≤ Cε_2 and ||V_c - 1|| ≤ ε_V. R4D-iso step 2 then holds with C_Ls² replaced by
        C(ε_2 + ε_V), and gives ρ ≤ C_1g^{-p}e^{-ε_1²/(4Ng²)} on the chart ball.
      - Derivatives: the data are smooth in Z with bounded derivatives on the ball. So R4D-iso step 3 (with D4-norm (3))
        gives |∂_Z^qρ̃| ≤ B_q(Λ/g²)^qρ̃ for q ≤ 3, and hence K_ρ ≤ Cg^{-p-6}e^{-ε_1²/(4Ng²)}.
      - GT-lat for ρ and for A_B (K_{A_B} = O(1)) gives c_ρΣ||Φ||² and c_BΣ||Φ||². These are R4D-iso's c_ρ and c_B, so
        δβ := c_ρ/c_B is unchanged and |δβ| ≤ Ce^{-a/g²}. Put R := R_ρ - δβR_B. ∎
      *2D analogue (argued, not written, not counted).* The same proof works for R2D-iso: use the exponential chart of
      S^{N-1} at a common direction, O(N) invariance in place of gauge invariance, and R2D-iso step 5 in place of GT
      step 5.
    - **Lemma BG-sum (the level summation on lattice backgrounds; arithmetic, not counted).** Fix k and a level-k cell.
      For n = k - j ≥ 0 let 𝒬_n be its L^{4n} level-j cubes, σ_n := L^{-n}, and let ε_•(Q) be the parameters of Q's
      data. **Hypothesis (BG-b).** There are M_2 ≤ ε_* and M_3, uniform in k, K and the cell, such that:
      - (b1) ε_2(Q) + ε_V(Q) ≤ M_2σ_n² for every Q (sup curvature in level-k units);
      - (b2) Σ_{n≥0} ō_n ≤ M_3, where ō_n := σ_n^{-2}L^{-4n}Σ_{Q∈𝒬_n}(ε_3 + ε_V)(Q) is the mean coarse-unit
        oscillation.
      Then Σ_nΣ_{Q∈𝒬_n}|R(Q)| ≤ C sup_jw_j(3M_2M_3 + M_2³Σ_nσ_n²), uniformly in k and K.
      *Proof.* ε_3 ≤ 2ε_2, so (ε_3 + ε_V)² ≤ 2M_2σ_n²(ε_3 + ε_V). Hence |R(Q)| ≤ w_j[3M_2σ_n²(ε_3 + ε_V)(Q) +
      M_2³σ_n⁶]. Sum over 𝒬_n and use σ_n⁴L^{4n} = 1 (the d = 4 marginality): the level-n total is
      w_j[3M_2ō_n + M_2³σ_n²]. Sum over n. ∎
      In d = 4 the scale factors cancel exactly, so the summability is carried by the background's mean oscillation
      alone. Smooth families have ō_n ~ σ_n (α = 1). Hölder-α curvature has ō_n ≲ σ_n^α. BV with polylogarithmic growth
      in n also suffices. The δβ and ρ_0 parts are as in R4D-iso's Consequence.
      *Linear part of ε_V (argued, not counted).* If V_c is the polar part of the mean contour M̄_c of the background,
      then log(V_cS_c^{-1}) at linear order in a constant curvature is the average flux through the ribbons between the
      S4' contours and the straight segment. That average vanishes, because the block is centred and the S4' order set
      is reflection-symmetric (the ribbons of y and of its mirror image have opposite oriented areas). So for such
      backgrounds ε_V is of oscillation order, plus the soft-constraint residual |V_c - polar M̄_c|.
    - **What BG-b is, inside L2.** (b1) is the first condition of CMP 109 (1.2), |U(∂p) - 1| < ε_0η² (curvature < ε_0
      in units of the current coarse lattice; NOTES §9.4), applied to the background on sub-cubes. (b2) follows from the
      second condition of (1.2), |J| < ε_0 with J = D*_Uη^{-2}π Im ∂U (a bound on the covariant divergence of the
      curvature), together with dF = 0 (Bianchi). The route is a lattice elliptic estimate: osc over a cube of size r
      ≤ Cr(1 + log(1/r))(sup|F| + sup|J|), which gives ō_n ≲ σ_n(1 + n). That estimate is a discrete Calderón-Zygmund
      / Green's-function bound [m; not written]. So **BG-b = the U_k(ε_0)-membership half of L2 (CMP 102 Theorem 1, as
      CMP 109 p.260 cites it) + a lattice elliptic step + a bound on the soft residual.** For the hard constraint (0.4),
      CMP 109 states the membership as a consequence of CMP 102 [read, second-hand]. For the soft S4' minimiser it is not
      proven.
    - **Attempt for the soft S4' minimiser (this session): not proven. What was established:**
      - (i) the exact form needed (BG-b; Lemma BG-sum);
      - (ii) the vanishing of ε_V's linear part by symmetry (argued);
      - (iii) a model diagnostic, check c20.
      The obstruction is local (per-cell) regularity of a nonlinear multiscale minimiser. Minimality gives only global
      energy bounds. The per-cell sup bound (b1) and the oscillation bound (b2) need a Caccioppoli/elliptic analysis
      of the Euler-Lagrange equation D*_UF = J_soft. Here J_soft is the soft residual carried back along the S4'
      contours, whose adjoint puts O(1) weight on the axial legs through block centres. That analysis is CMP 102's
      content, now needed for the soft kernel.
    - **Check c20 (criteria checks/c20_criteria.md written before checks/c20_bg_regularity.py): VALID** (V1 τ-stability
      ≤ 3.8e-7 with CG converged; V2 controls C1 smooth / C2 multi-level jumps / C3 rough classified as expected).
      Run: 104 s, 391 MB, load 2.0, 36% free memory, nice 10, BLAS threads 1; output checks/c20_out.txt. A pre-run
      smoke test checked the averaging operator only: gauge covariance error 4e-16, constant fields mapped to L·value.
      [R910-fix] Disclosure: REVIEW_S9_S10's audit of the session-9 transcript found one pre-run code edit (a
      diagonal-term line, at 13:22:02 UTC) after the criteria and script and before the only run (13:22:27). It was
      not disclosed in session 9.
      Model: linearised abelian 2D, soft-constraint chain minimiser with the S4' contour family, κ_i = κL^{-2i}.
      - **Finding: SUMMABLE in all three runs.** The mean-oscillation ratios A_j/A_{j+1} are 0.338, 0.343, 0.363 (L = 3,
        κ = 1), 0.342, 0.358, 0.458 (L = 3, κ = 10) and 0.208, 0.233 (L = 5). These are ≈ 1/L, like the smooth control
        (0.33-0.47; 0.20-0.32), i.e. Lipschitz-type decay.
      - The maximal oscillation G_j decays similarly, so it is not a mean-only effect.
      - sup|f_0|/max|dB_n| = 1.07, 2.85, 2.10.
      - The level-0 oscillation is not concentrated at the level-n centre lines: share 0.130 vs cube fraction 0.143;
        0.120 vs 0.143; 0.078 vs 0.078. So the axial weight of Q^T does not roughen the background in this model.
      - Scope: an abelian linear 2D instance. It supports BG-b for S4' (failure mode BG-F3 not seen). It does not test
        ε_V, the non-abelian minimiser, or 4D.
    - **BG-reg status: OPEN, narrowed to BG-b** (main path, soft kernel). The Consequence paragraphs of R2D-iso and
      R4D-iso are now conditional on BG-b, with α = 1.
  - **W1-loc in 4D [S9] (RTARGET §10).**
    - **Lemma W1-size' (exact size reduction to the plugged holed sea): PROVEN-HERE [S9].** Setting W1 (2D) or W1-4D.
      Write □_0's interior integral as Den_□(D) + Num_□(D), where Den = ∫χ_0w, Num = ∫(1 - χ_0)w, and w is □_0's
      interior integrand (in 4D including the D4-norm factors), a function of the data D. Let w_ref(D) > 0 be any
      measurable reference weight. Let Z^open_w := ∫(rest)·w_ref(D) be the integral with □_0's interior integral
      replaced by w_ref, and ⟨·⟩_w its probability measure. Every other block stays cut. Then for every event E in the
      data:
        ⟨ρ_□⟩_cut ≤ sup_{E^c}ρ_□ + [sup_E(Num/w_ref)]·P_w(E) / ([inf_{E^c}(Den/w_ref)]·P_w(E^c)).
      *Proof.* Z^rel - Z^cut = ∫(rest)Num. Split it: ∫_{E^c}(rest)Den·ρ ≤ sup_{E^c}ρ·Z^cut, and
      ∫_E(rest)w_ref(Num/w_ref) ≤ sup_E(Num/w_ref)·Z^open_wP_w(E). Also Z^cut ≥ inf_{E^c}(Den/w_ref)·Z^open_wP_w(E^c).
      Divide. ∎ This replaces W1-size's P_rel, a probability under the released measure, by a probability under a
      defect-free sea.
      **Choice w_ref := sup_{U_int}w(U_int; D)** (the classical plug), with E := {ε_2 + ε_V > ε_*} (4D; in 2D, the
      collar off every common direction by δ_0). Then:
      - sup(Num/w_ref) ≤ 1, since Haar measure has mass 1;
      - on E^c the maximiser U* of w satisfies e^{-S(U*)}Cg^{-q} ≥ w(U*) ≥ w(1) ≥ e^{-Bε_*²/g²}, using D4-norm (2) and
        𝒩 ≤ 1. So g²S(U*) ≤ ε_1²/(4N) + O(g² log(1/g)), and by inequality (B) every interior plaquette has
        ||1 - U_p|| ≤ ε_1/√2 + o(1). Then χ = 1 on the ball ||U - U*|| ≤ rg. Since U* is an interior critical point and
        |D² log w| ≤ C/g² (R4D-iso step 3), Den/w_ref ≥ c(rg)^pe^{-Cr²};
      - sup_{E^c}ρ ≤ Cg^{-p}e^{-ε_1²/(4Ng²)} (R4D-lat).
      Hence **⟨ρ_□⟩_cut ≤ Cg^{-p}e^{-ε_1²/(4Ng²)} + Cg^{-p'}P_w(E)/P_w(E^c)**. The background cost cancels against
      w_ref, so no exponentially small denominator appears.
    - **Lemma AG (Anderson sub-Gaussianity; elementary, not counted).** Let γ be the standard Gaussian on R^m, K a
      centred ball, and μ := γ|_K/γ(K). Then E_μe^{⟨v,W⟩} ≤ e^{|v|²/2}.
      *Proof.* E_μe^{⟨v,W⟩} = e^{|v|²/2}γ(K - v)/γ(K). The Gaussian density is symmetric decreasing, and 1_K is the
      symmetric decreasing rearrangement of 1_{K-v}, so γ(K - v) ≤ γ(K) by the Hardy-Littlewood inequality. ∎
      For a product μ* = Π_xμ*_x and ℓ = Σ_x⟨c_x, W(x)⟩ this gives E_{μ*}e^{tℓ} ≤ e^{t²|c|²/2}.
    - **Hypothesis (DF) (Dimock form of the plugged holed sea; NOT proven; it is the small-field package).**
      - (DF1) After gauge fixing and a change of variables, ⟨G(D)⟩_w = ∫G(𝒟(W))e^{Σ_XH(X,W)}dμ*(W) /
        ∫e^{Σ_XH}dμ* for bounded measurable G. Here μ* = Π_xμ*_x, each μ*_x the standard Gaussian on R^m restricted to a
        centred ball (the radius may depend on g) and normalised.
      - (DF2) 𝒟(W) = 𝒰·exp(ig𝒞W) on the data region, in tree gauge. 𝒰 is the background, with
        ε_2(𝒰) + ε_V(𝒰) ≤ ε_*/4, and V is background. 𝒞 is linear with Σ_x||𝒞(b,x)||² ≤ C_0² for each data link b
        (C_0 g-independent).
      - (DF3') Sub-Gaussian linear functionals under the interacting measure: for ℓ = ⟨e, (𝒞W)_b⟩ (e a unit vector in
        su(N)) and real t, log E e^{tℓ} ≤ (1 + η)t²C_0²/2 + |t|m_0, with η ≤ 1 and m_0 g-independent. With H = 0 this is
        Lemma AG (η = m_0 = 0). With H ≠ 0 it follows from Dimock I Thm 27 by tilting μ* site by site: the tilted measure is
        ultralocal with the same support, and log Ξ_t - log Ξ_0 is a sum over polymers meeting supp c. This is
        [argued, not written]; it needs control of the tilted means and Thm 27's tree-graph bound.
      - (DF4) For (cl): smooth dependence of 𝒰, 𝒞 and H on the background V with exponential decay in the distance, and a
        random-walk expansion of 𝒞 (Dimock I Lemma 6 type) that survives complex s-weakening.
    - **Corollary W1-LD-cond (counted with W1-size'): (DF1), (DF2), (DF3') ⇒ (LD).**
      - Proof: ε_2 + ε_V ≤ ε_*/4 + C_1g max_b||(𝒞W)_b|| (C_1 = C(R_0)). So E ⊂ ∪_{b,a}{|ℓ_{b,a}| > u}, with
        u := 3ε_*/(4C_1√(N²-1)g) and ℓ_{b,a} the components of (𝒞W)_b. Chernoff with (DF3') gives
        P(±ℓ > u) ≤ exp(-(u - m_0)²/(4C_0²)). A union over the n_D(N²-1) pairs gives
        P_w(E) ≤ 2n_D(N²-1)e^{-(u-m_0)²/(4C_0²)}, so P_w(E) ≤ Ce^{-a_LD/g²} and P_w(E^c) ≥ ½ for g ≤ g_0, for every
        a_LD < (3ε_*/(4C_1√(N²-1)))²/(4C_0²).
      - By W1-size', **⟨ρ_□⟩_cut ≤ Cg^{-p}e^{-a/g²}, a := min(ε_1²/(4N), a_LD)**, uniformly in T. a and every constant
        are g-independent ((W4-F4) avoided).
      - The non-convexity obstruction of session 8 (the cut sea is not log-concave in n or U) does not arise: in Dimock
        form the truncation is a product of balls in W, and Lemma AG holds for it. ∎
    - **(cl), argued (not counted).** log(1 + ⟨ρ⟩_cut) = log⟨(Num + Den)/w_ref⟩_w - log⟨Den/w_ref⟩_w. Each is the log of
      the expectation of a positive function of the data near □_0. V_c-derivatives act on 𝒰, 𝒞, H, w_ref and the direct
      dependence (DF4).
      - Localise the data's dependence on W by the s-weakened random-walk expansion of 𝒞 (Dimock I (221)-(226), Lemmas
        18-19).
      - The real-analyticity radius of Num in the data is only O(g²): the large-field configurations make ∂_DS ~ 1/g².
        So the cubes within a corridor of width r(g) = O(log(1/g)/(γM)) of □_0 are kept fixed (s = 1), and only cubes
        beyond it are interpolated. The tail is then ≤ g^{-p}e^{-γMr}× the main term.
      - The fixed corridor Z_0 is one block of a coarser ultralocal partition, and Thm 27 applies with the localised
        insertion as a single-block factor. log⟨G⟩ is then local, and its V_c-derivatives come only from polymers that
        join Z_0 to c, giving e^{-κ_d d(c, □_0)}.
      - The corridor costs e^{κ_dr(g)} = g^{-O(1)}, a polynomial loss, which the restated (cl) allows. So (W4-F2) occurs
        only in this harmless form.
      - Needs: (DF4), Thm 27 (imported), and the derivative/tilt form of its bounds.
    - **Outcome vs RTARGET §10.**
      - (LD) is reduced exactly to (DF1)-(DF3'), by a complete argument (W1-size' + AG + Chernoff).
      - (cl) is argued under (DF4) + Thm 27.
      - Failure modes:
        - (W4-F1) MET: (DF) is not available from what is proven. It is the small-field package for the soft RG: the L2
          background with decay, the L3g covariance with random-walk expansion, gauge fixing (FP), and the L4a-form
          polymer bound. All are imported from hard-constraint papers and none is re-verified.
        - (W4-F2) met only as a polynomial g-loss.
        - (W4-F3) MET: Thm 27 is load-bearing for (DF3') and (cl). Steps 1-3 of its proof were re-read (Dimock I
          App. B, pp.39-42: Mayer expansion, ultralocal factorisation, polymer-gas exponentiation). Step 4 rests on the
          tree-graph bound (323), "one can show …", which is not proven there [read]. Classical: Penrose [m]. So Thm 27
          is IMPORTED-NOT-YET-REVERIFIED, used inside an OPEN item only.
        - (W4-F4) avoided.
    - **W1-loc status: OPEN, restated in 4D (main path) and reduced: (LD) ⇐ (DF1-3'); (cl) ⇐ (DF4) + Thm 27.** The
      large-field defect adds nothing beyond W1-size' (proven) and AG (proven). **Exact wall: (DF), i.e. the small-field
      package for the soft RG, plus re-verifying Thm 27.**
      - **[S10]** Thm 27 is replaced by Theorem CE (PROVEN-HERE, L5 [S10]), so (W4-F3) is discharged. The exact wall of
        W1-loc is now (DF) alone, i.e. the nodes {N2, N4, N5, N6} of the (DF) sub-DAG (L5 [S10]).
      - The strong (multi-defect) form: ultralocality (W1-F3) is supplied by (DF). Clusters of adjacent released blocks
        remain: there R4D-lat's data are not small-field, which is W2 territory. This stays inside L5.

- **[S10] Session 10: Theorem CE (Dimock I Thm 27, re-verified in corrected form), BG-b for the linearised soft chain,
  the (DF) sub-DAG. Targets pre-stated in RTARGET.md §12-14. Status of L5 unchanged: IMPORTED-NOT-YET-REVERIFIED.**
  New PROVEN-HERE: Theorem CE (with Lemmas CE-geo and TG); Lemma LES (lattice elliptic step); Proposition BG-b-lin
  (with Lemmas CR and J-str). [R910-fix] Thm 27's statement says c_0 depends on d only; its proof says (p.40) "So c0 does depend on κ".
  Proposition CE-κ shows the κ-dependence is necessary. This corrects the statement's quantifiers, as the author's
  remark does. Dimock's proof and his application (κ fixed) are unaffected. The corrected form is Theorem CE. BG-reg stays OPEN, narrowed to the membership hypotheses (H1)+(H2) plus the written non-abelian
  bookkeeping. Checks c21 (13/13 PASS) and c22 (below).
  - **Theorem CE (cluster expansion; RTARGET §12).**
    - *Setting CE.* d = 4, and M = 1 after scaling (every statement is M-independent, as in Dimock I App. A). Unit
      cubes □_x = x + [-½, ½]⁴, x in a torus (Z/TZ)⁴ with T ≥ 3. A **polymer** X is a nonempty set of cubes whose union
      is connected (equivalently *-connected: cubes adjacent iff they intersect). Face-connected polymers are a
      subclass, and every bound below holds a fortiori for them. X ∩ Y ≠ ∅ means a common cube. |X| := the number of
      cubes. **d(X)** := the infimum of the lengths of connected finite unions of segments contained in ∪X that meet
      every cube of X (Dimock (119)). **[R910-fix] Reading of (119).** This is the touching-tree reading: the
      tree must meet every CLOSED cube of X, possibly at a boundary point only, so a face-adjacent pair has d = 0.
      Dimock's own proof presupposes it: in (305) "For each pair add a line in □ joining the point in τi to the point
      in τj. This line has length at most M" needs the τ_i to meet □ at arbitrary points, and the 3^d in (122) is a
      touching-count constant (Lemma CE-geo' [S11] proves it). Under the other possible reading (a Steiner tree on the
      cube centres) a face-adjacent pair has d = 1; REVIEW_S9_S10 computed that Proposition CE-κ's instance then fails,
      and the κ-dependence of c_0 is not needed. Every statement below is for the touching reading. Fields Φ = (Φ(x)) live on sites; every site is in exactly one cube (half-open
      convention), with at most m sites per cube. μ = Π_xμ_x is a product probability measure. H(X, Φ) is measurable,
      complex allowed, and depends on Φ|_X only.
    - **Lemma CE-geo (explicit d = 4 constants): PROVEN-HERE.** Put A := 81 = 3⁴, a := log 12800,
      **κ_0 := 324a ≈ 3064.1** and **K_0 := e^{κ_0/4}/6400**.
      - (g1) |X| ≤ A(1 + 4d(X)). *Proof.* Let τ be a connected union of segments meeting every cube of X, with length ℓ.
        Choose a maximal set P ⊂ τ of points with pairwise sup-distance > ½ (finite, τ is compact). The closed sup-balls
        of radius ½ around P cover τ. Each is a closed box of side 1, and it meets at most 3 lattice cubes per coordinate
        (T ≥ 3), so at most 81 cubes; hence |X| ≤ 81|P|. If |P| ≥ 2, the open sup-balls of radius ¼ around P are
        disjoint. τ is connected and leaves each of them, so τ has Euclidean length ≥ ¼ inside each. Thus
        |P| ≤ max(1, 4ℓ) ≤ 1 + 4ℓ. Take the infimum over τ. ∎ (Dimock's (122) asserts |X| ≤ 3^d(1 + d(X)) and quotes it
        from [22] without proof; only the weaker form (g1) is used here. [S11] Lemma CE-geo' proves the stronger
        |X| ≤ 2^d + 2^{d-1}√d·d(X), hence the upper inequality of (122) (Dimock: d = 3) [R1112-fix], and lowers κ_0 to 16 log 12800 ≈ 151.3.)
      - (g2) If X_1, …, X_n are polymers, Y := ∪X_i, and some tree τ on {1, …, n} has X_i ∩ X_j ≠ ∅ for every edge
        {i, j} ∈ τ (repetitions allowed), then Y is a polymer and **d(Y) ≤ Σ_i d(X_i) + 2(n - 1)**. *Proof.* Take
        near-optimal trees τ_i in ∪X_i. For each edge {i, j} ∈ τ, X_i and X_j share a cube □; join a point of τ_i ∩ □ to
        a point of τ_j ∩ □ by a segment inside □, of length ≤ diam □ = √4 = 2. The union is connected, lies in ∪Y and
        meets every cube of Y. ∎ (Dimock's (305) has M(n - 1): it bounds each joining segment by M. In d = 3 or 4 a
        segment inside an M-cube can have length up to √d·M, so (305) needs √d in place of 1. Discrepancy 1; it only
        changes constants.)
      - (g3) #{X ∋ □ : |X| = n} ≤ 80^{2(n-1)}. *Proof.* The adjacency graph of cubes has degree ≤ 3⁴ - 1 = 80. A
        polymer containing □ has a spanning tree, and a depth-first traversal from □ is a closed walk of length 2(n - 1)
        that determines it. ∎ (Dimock's (292) counts with (2d)^{2(n-1)}, i.e. face-connected polymers. For our *-connected
        polymers 3^d - 1 replaces 2d. **[R910-fix] This is not a discrepancy in Dimock:** his polymers are
        face-connected (§3.1: "□j and □j+1 have a d − 1 = 2 dimensional face in common"), so (2d)^{2(n-1)} is right
        for his definition. It is a definitional difference: Setting CE chose the larger *-connected class.)
      - (g4) Σ_{X∋□} e^{-a|X|} ≤ e^{-a}Σ_{m≥0}(6400e^{-a})^m = 2e^{-a} = 1/6400. By (g1), d(X) ≥ |X|/324 - ¼, so
        Σ_{X∋□} e^{-κ_0d(X)} ≤ e^{κ_0/4}Σ_{X∋□} e^{-a|X|} ≤ K_0.
      - (g5) Σ_{X∩Y≠∅} e^{-κ_0d(X)} ≤ K_0|Y| and Σ_{X⊂Y} e^{-κ_0d(X)} ≤ K_0|Y| (sum (g4) over the cubes of Y). Also
        |Y| ≤ 81 + 324d(Y) ≤ κ_0(1 + d(Y)), and 1 + 4d ≤ 4e^d.
    - **Lemma TG (tree-graph inequality = Dimock (323)): PROVEN-HERE.** For a connected graph g on {1, …, n} put
      ρ^T(g) := Σ_{G ⊆ g, G spanning and connected} (-1)^{|E(G)|}. This is Dimock's (317) for the overlap graph g of
      (Y_1, …, Y_n), since ζ - 1 = -1 exactly on overlapping pairs. Then **ρ^T(g) = (-1)^{n-1}·#{T : R(T) = ∅}**, where T
      runs over the spanning trees of g. Hence |ρ^T(g)| ≤ #{spanning trees of g}.
      *Proof (Penrose's partition scheme).* Root every tree at vertex 1. For a spanning tree T with depths d_T and parents
      p_T, call an edge {i, j} ∈ g \ T admissible if d_T(i) = d_T(j), or d_T(j) = d_T(i) + 1 and i > p_T(j). R(T) := the
      set of admissible edges. For a spanning connected G ⊆ g, let d_G be the graph distance to 1 in G, and let T(G) be
      the tree in which each j ≠ 1 is joined to the smallest-label G-neighbour i with d_G(i) = d_G(j) - 1. By induction
      on the depth, T(G) is a spanning tree with d_{T(G)} = d_G.
      - (⇒) T(G) ⊆ G. Every edge {i, j} of G has |d_G(i) - d_G(j)| ≤ 1. If the depths are equal, the edge is admissible.
        If d_G(j) = d_G(i) + 1 and {i, j} ∉ T(G), then i is a G-neighbour of j one level up, different from
        p_{T(G)}(j), so by the minimum rule i > p_{T(G)}(j): admissible. Hence G ⊆ T(G) ∪ R(T(G)).
      - (⇐) Let G = T ∪ S with S ⊆ R(T). Then d_G ≤ d_T. Every edge of G joins vertices whose d_T differ by ≤ 1, so
        along any path from 1, d_T grows by ≤ 1 per step, and d_T ≤ d_G. So d_G = d_T. For j ≠ 1, the G-neighbours of j
        at depth d(j) - 1 are p_T(j) and the i's of type-(b) edges in S, all with i > p_T(j). So T(G) = T.
      So the spanning connected subgraphs are partitioned into the intervals [T, T ∪ R(T)], and
      Σ_{G∈[T, T∪R(T)]}(-1)^{|E(G)|} = (-1)^{n-1}(1 - 1)^{|R(T)|} = (-1)^{n-1}·1[R(T) = ∅]. Sum over T. ∎
      (c21 G1-G4: exact on every connected labelled graph with n ≤ 5, with the partition property itself tested, and on
      K_6 plus 300 random 6-vertex graphs; ρ^T(K_n) = (-1)^{n-1}(n-1)!.)
    - **Theorem CE (Dimock I Thm 27, corrected form): PROVEN-HERE.** In Setting CE, suppose that on supp μ
      |H(X, Φ)| ≤ H_0e^{-κd(X)} for every polymer X, with **κ > 3κ_0 + 3** and
        **H_0 ≤ c_0(κ) := min{ log 2, (8AK_0)^{-1}e^{-2(κ-κ_0)}, (8B)^{-1}e^{-2(κ-3κ_0-2)} }**,
      where C_K := 8e^{1/4}AK_0 and B := C_Ke^{κ_0}K_0. Then ∫exp(Σ_XH(X))dμ = exp(Σ_YH#(Y)), where H#(Y) depends only
      on {H(X) : X ⊂ Y}, H#(Y) = 0 unless Y is a polymer, and
        **|H#(Y)| ≤ C_1H_0e^{-(κ-3κ_0-3)d(Y)},  C_1 := 2κ_0B = 16e^{1/4}Aκ_0K_0²e^{κ_0}.**
      The prefactor C_1 depends on d only. **c_0 must depend on κ** (Proposition CE-κ below); c_0(κ) ∝ e^{-2κ} here.
      **[S11]** With Lemma CE-geo' the same statement holds with κ_0 := 16 log 12800 ≈ 151.3, K_0 := e^{κ_0}/6400,
      C_K := 32eK_0, the second entry of c_0 replaced by (32K_0)^{-1}e^{-2(κ-κ_0)}, and B, C_1 defined as above from these;
      the hypothesis becomes κ > 3κ_0 + 3 ≈ 457 (L5 [S11]).
      *Proof.* The torus is finite, so every sum below is finite unless said otherwise.
      - Step 1 (Mayer; Dimock (300)-(307), re-derived). With f_X := e^{H(X)} - 1, Π_X(1 + f_X) = Σ_{{Y_j} disjoint}
        Π_jK(Y_j), where K(Y) := Σ_{n≥1}(1/n!)Σ_{(X_1,…,X_n)}Πf_{X_i}, the sum over ordered n-tuples of DISTINCT
        polymers that are overlap-connected with ∪X_i = Y. (Group the collections of distinct polymers by the
        overlap-connected components; their unions are disjoint and the decomposition is unique.) For |z| ≤ log 2,
        |e^z - 1| ≤ e^{|z|} - 1 ≤ |z|/log 2 ≤ 2|z|. Put κ' := κ - κ_0. By (g2), Π_ie^{-κd(X_i)} ≤
        e^{-κ'(d(Y)-2(n-1))}Π_ie^{-κ_0d(X_i)}. Drop every constraint except X_i ⊂ Y and use (g5):
        |K(Y)| ≤ e^{-κ'd(Y)}e^{-2κ'}Σ_{n≥1}u^n/n! ≤ e^{-κ'd(Y)}·2H_0K_0|Y|e^u, with u := 2H_0K_0e^{2κ'}|Y|.
        The second condition on H_0 and (g1) give u ≤ |Y|/(4A) ≤ ¼ + d(Y). With |Y| ≤ 4Ae^{d(Y)}:
        **|K(Y)| ≤ C_KH_0e^{-κ_1d(Y)}, κ_1 := κ - κ_0 - 2**, on supp μ. K(Y) depends only on Φ|_Y.
      - Step 2 (integration; (308)-(310)). Disjoint Y_j carry independent fields, so ∫Π_jK(Y_j)dμ = Π_jK#(Y_j), with
        K#(Y) := ∫K(Y)dμ and |K#(Y)| ≤ C_KH_0e^{-κ_1d(Y)}. Hence Ξ = P(K#), where P(z) := Σ_{{Y_j} disjoint}Π_jz_{Y_j}
        is a polynomial in the variables z = (z_Y), Y a polymer, with P(0) = 1.
      - Step 3 (exponentiation as an analytic identity; this replaces Dimock's "formal series, afterwards convergence").
        Let 𝓗(z) := Σ_Y𝓗_Y(z), 𝓗_Y(z) := Σ_{n≥1}(1/n!)Σ_{(Y_1,…,Y_n): ∪Y_i=Y}ρ^T(g(Y_1,…,Y_n))Π_iz_{Y_i}, where ρ^T := 0
        when the overlap graph g is disconnected. Dimock's computation (313)-(322) (the ζ-product, the expansion into
        graphs, the grouping by connected components and the exponential formula) was re-checked line by line. It is
        an identity in the ring of formal power series C[[z]], because each coefficient involves finitely many terms. So
        exp(𝓗) = P as formal power series. Step 4 shows that 𝓗 converges absolutely and uniformly on the closed
        polydisc 𝔻 := {|z_Y| ≤ r_Y := C_KH_0e^{-κ_1d(Y)}}. So 𝓗 is holomorphic in the interior of 𝔻 and continuous on
        𝔻. exp(𝓗) and P are holomorphic there and have the same Taylor series at 0, so they agree on the connected
        interior, and on 𝔻 by continuity. Put z = K# ∈ 𝔻: Ξ = exp(Σ_YH#(Y)) with H#(Y) := 𝓗_Y(K#). H#(Y) involves only
        Y_i ⊂ Y, hence only H(X) with X ⊂ Y. It vanishes unless the overlap graph is connected, i.e. unless Y is a
        polymer.
      - Step 4 (convergence; (323)-(333), re-derived). Fix Y and n ≥ 2. By Lemma TG, |ρ^T(g)| ≤ #{trees τ ⊆ g}, and
        τ ⊆ g(Y_1, …, Y_n) iff Y_i ∩ Y_j ≠ ∅ along τ. So
        Σ_{∪Y_i=Y}|ρ^T|Π|z_{Y_i}| ≤ Σ_τΣ_{(Y_i): ∪=Y, overlaps along τ}Π_ir_{Y_i}.
        Put κ_3 := κ_1 - 2κ_0 = κ - 3κ_0 - 2 > 1. By (g2) along τ, Π_ie^{-κ_1d(Y_i)} ≤ e^{-κ_3(d(Y)-2(n-1))}
        Π_ie^{-2κ_0d(Y_i)}. Root τ at 1 and relax the constraints to Y_1 ⊂ Y and Y_j ∩ Y_{p(j)} ≠ ∅. Sum the leaves
        inwards. A vertex with c children has accumulated |Y_j|^c, and
        Σ_{Y_j∩Z≠∅}e^{-2κ_0d(Y_j)}|Y_j|^c ≤ c!Σe^{-2κ_0d(Y_j)}e^{|Y_j|} ≤ c!e^{κ_0}Σe^{-κ_0d(Y_j)} ≤ c!e^{κ_0}K_0|Z|,
        using x^c ≤ c!e^x, |Y_j| ≤ κ_0(1 + d(Y_j)) and (g5). The root gives c_1!e^{κ_0}K_0|Y|. So the τ-sum is
        ≤ (e^{κ_0}K_0)^n|Y|Π_jc_j!, with c_1 = d_1 and c_j = d_j - 1 for j ≠ 1. (Dimock's (329) writes |Y_1|^{d_1-1} at
        the root; the root has d_1 children. Discrepancy 3; it costs a factor ≤ n.) By Cayley's formula with degrees,
        Σ_τd_1Π_j(d_j - 1)! ≤ (n - 1)(n - 2)!·binom(2n-3, n-1) ≤ (n - 1)!4^{n-1}. Divide by n!:
        (1/n!)Σ_{∪Y_i=Y}|ρ^T|Π r_{Y_i} ≤ κ_0BH_0(4BH_0e^{2κ_3})^{n-1}e^{-(κ_3-1)d(Y)},
        using |Y| ≤ κ_0e^{d(Y)}. The same bound holds for n = 1, since |z_Y| ≤ C_KH_0e^{-κ_1d(Y)} ≤ κ_0BH_0e^{-(κ_3-1)d(Y)}.
        The third condition on H_0 gives 4BH_0e^{2κ_3} ≤ ½. Summing over n, |𝓗_Y(z)| ≤ 2κ_0BH_0e^{-(κ-3κ_0-3)d(Y)}
        uniformly on 𝔻, with absolute convergence. ∎
      - *Exponent bookkeeping vs Dimock.* (325) defines κ_2 := κ - κ_0 - 1, but (310) gives the exponent κ - κ_0 - 2.
        The final κ_2 - 2κ_0 - 1 = κ - 3κ_0 - 3 requires κ_2 = κ - κ_0 - 2 (discrepancy 4, a typo). (326) drops the
        factor e^{(κ_2-2κ_0)(n-1)} that (305) produces. It can be absorbed into "(O(1)H_0)^n" only if that O(1) may depend
        on κ (discrepancy 5). Isolating the n = 1 term, as above, keeps the prefactor C_1 κ-independent. The κ-dependence
        then sits in c_0 alone, consistent with the proof's own remark on p.40, "So c0 does depend on κ" [read].
    - **Proposition CE-κ (the quantifier in Thm 27's statement must be κ-dependent, as Dimock's proof remarks):
      PROVEN-HERE [R910-fix: retitled; a quantifier-order remark, not an error in Dimock's mathematics].** Under the
      touching-tree reading of (119) there are no constants c_0, C_1 depending on d only such that, for every
      κ > 3κ_0 + 3, the conclusion of Theorem CE holds with SOME family H# that is local (H#(Y) depends only on
      {H(X) : X ⊂ Y}) and vanishes off polymers. *Attribution.* Thm 27's statement says c_0 depends on d only; its
      proof says (p.40) "So c0 does depend on κ". This proposition shows the κ-dependence is necessary, which corrects
      the statement's quantifiers, as the author's remark does. Dimock's proof and his application (κ fixed once,
      "κ ≥ 10(κ0 + 1) which we assume", in his §4.7 "scaling" (after (243)), l.1672 of the extracted text [R1112-fix:
      was "in the proof of his Lemma 21, l.2731"]) are
      unaffected.
      *Proof [R910-fix: the six-bond finite-difference argument of REVIEW_S9_S10 replaces the Möbius step, which
      presumed facts about H# that the bare existence statement does not give].* Suppose such c_0, C_1 exist. Fix a
      torus T ≥ 3 in d = 4, one site per cube, σ_x = ±1 uniform. Let Y_6 be a 2 × 3 rectangle of cubes in a coordinate
      2-plane and E_6 its six outer (boundary-cycle) bonds, all face-adjacent pairs. For S ⊆ E_6 put
      H_S({x, y}) := hσ_xσ_y for {x, y} ∈ S and H_S := 0 otherwise. A face-adjacent pair has d = 0 (a point of the
      common face meets both closed cubes), so every H_S obeys the hypothesis with H_0 = h, for EVERY κ.
      - *No branch ambiguity.* Take κ ≥ 4κ_0 + 3 and h ≤ c_0 small, depending on T. Then
        |Σ_YH#_S(Y)| ≤ C_1h·T⁴K_0 (every polymer contains a cube; (g4)) and |log Ξ_S| ≤ 4h² are both < π, so
        Ξ_S = exp(Σ_YH#_S(Y)) forces Σ_YH#_S(Y) = log Ξ_S for every S.
      - *Finite difference.* Δ := Σ_{S⊆E_6}(-1)^{6-|S|}log Ξ_S = Σ_YΣ_S(-1)^{6-|S|}H#_S(Y). If Y misses a bond b ∈ E_6
        (does not contain both of its cubes), then H#_S(Y) does not depend on whether b ∈ S, so pairing S with S△{b}
        cancels its contribution. Every cube of Y_6 is an endpoint of a bond of E_6, so only Y ⊇ Y_6 survive. For them
        d(Y) ≥ 1 (a tree meeting both outer columns has length ≥ 1), so
        |Δ| ≤ 64C_1hΣ_{Y∋□_0}e^{-(κ-3κ_0-3)d(Y)} ≤ 64C_1hK_0e^{-(κ-4κ_0-3)} → 0 as κ → ∞, with h fixed.
      - *Exact value.* e^{hσσ'} = cosh h(1 + tσσ'), t := tanh h, so Ξ_S = cosh(h)^{|S|}Σ_{G ⊆ S even}t^{|G|}. The only
        even subgraphs of the 6-cycle are ∅ and the cycle, so Ξ_S = cosh(h)^{|S|}(1 + t⁶·1[S = E_6]). The term
        |S| log cosh h is a sum of one-bond functions and is killed by the alternating sum. Hence Δ = log(1 + t⁶) > 0,
        independent of κ. Contradiction. ∎
      (c21 I4 checks Δ = log(1 + tanh(h)⁶) to 60 digits at h = 0.01, 0.03, 0.1.)
      *For Dimock's own H# of (312)* the Möbius inversion of session 10 is also valid, since K(Y) = 0 unless Y ⊆ Z, and
      gives H#(Y_6) = t⁶ + O(t⁸). Exact instance (c21 I1, I2, [S11] 60-digit arithmetic; [R910-fix] the session-10
      value 1.0003 at h = 0.01 was double-precision cancellation noise): |H#(Y_6)|/h⁶ = 0.9997, 0.9973, 0.9703 at
      h = 0.01, 0.03, 0.1; |H#(Y_4)|/h⁴ = 0.9999, 0.9988, 0.9867. Heuristically, 2 × n rectangles give H# ≈ h^{2n} with d ≈ n - 2, which suggests that a valid c_0(κ)
      must be ≲ e^{-κ/2}. Theorem CE's e^{-2κ} is sufficient. Closing the gap is not needed.
    - **Remark CE-cx (complex tilts; for (DF3') and (cl)).** Steps 1-4 use μ only through the product structure and
      through |∫Kdμ_Y| ≤ ||μ_Y||·sup_{supp}|K|. So Theorem CE holds for complex product measures with every μ_x(1) = 1,
      the same support, and ||μ_x|| ≤ e^δ. The changes are κ → κ - δmκ_0 and C_K → C_Ke^{δmκ_0}, from
      Π_{x∈Y}||μ_x|| ≤ e^{δm|Y|} and (g5). One line; counted with Theorem CE. **[R910-fix] Inherited constants.**
      B and C_1 inherit C_K → C_Ke^{δmκ_0} (B → Be^{δmκ_0}, C_1 → C_1e^{δmκ_0}); c_0(κ)'s third entry becomes
      (8Be^{δmκ_0})^{-1}e^{-2(κ-δmκ_0-3κ_0-2)}, while its first two entries are unchanged (Step 1 does not involve μ);
      the κ-condition becomes κ - δmκ_0 > 3κ_0 + 3, and the decay rate is κ - δmκ_0 - 3κ_0 - 3.
    - **Check c21** (criteria checks/c21_criteria.md before checks/c21_cluster_expansion.py): **13/13 PASS**, in 6.1 s,
      31 MB peak, load 1.6, 35% free memory, nice 10, BLAS threads 1. Output: checks/c21_out.txt.
      - G1-G4: Lemma TG, as above.
      - M1-M3: the Mayer grouping identity, by direct enumeration of all 2^15 polymer collections on a 2 × 3 grid with
        a three-valued asymmetric field, matched an independent subset recursion for every Z and every configuration
        (max relative error 1.4e-15); the integration step matched to 6.6e-16; K was supported on the 40 connected sets.
      - S1-S3: the Möbius-inverted exact log vanished off connected sets (1e-15). The truncated cluster series
        converged to it: max errors 6.3e-4, 3.8e-5, 2.0e-6, 1.4e-7 at orders 1-4, against max|H#| = 1.7e-2.
      - I1-I3: Proposition CE-κ, as above.
    - **Status: Theorem CE PROVEN-HERE.** [R910-fix] Dimock I Thm 27's statement says c_0 depends on d only; its proof
      says (p.40) "So c0 does depend on κ"; Proposition CE-κ shows that the κ-dependence is necessary. This corrects the
      statement's quantifiers, as the author's remark does; Dimock's proof and his application (κ fixed) are
      unaffected. His proof, with the four textual discrepancies (1, 3, 4, 5) repaired and the definitional
      difference (polymer class) recorded, proves Theorem CE. Every use in this file (W1-loc (cl), (DF3')) fixes κ
      first, so the corrected form suffices. **Thm 27 is no longer an unverified import anywhere in the file**: it is
      replaced by Theorem CE. (W4-F3 is discharged.)
  - **BG-b for the soft chain (RTARGET §13).**
    - *Setting SC (linearised soft chain).* d = 4. Levels i = 0, …, k; the level-i lattice is a torus in its own units
      (spacing 1). B_i are real 1-forms (one colour component; around the trivial background su(N) linearises to N² - 1
      independent copies). Q is the linearised S4' map from level i to level i + 1 (Q_root of L3g(a)-slice, with the
      S4' order average). The chain energy is
        E = ½||dB_0||² + Σ_{i<k}(κ_i/2)||QB_i - B_{i+1}||²,  B_k given,
      with κ_- ≤ κ_i ≤ κ_+. This is the quadratic part of the tree-level exponent of the normalised soft kernel
      (decision 4): the normalisation 𝒩 cancels the |M̄|-shrinkage, so only the distance of V_{i+1} from the polar part
      of M̄ is charged. Residuals r_i := QB_i - B_{i+1} (level-(i+1) 1-forms); κ̂ := max_iκ_{k-1}/κ_i. Coarse-unit
      curvature f_i := L^{2(k-i)}dB_i, and σ_n := L^{-n}, n = k - i. A critical point is any stationary point; a
      minimiser exists (a finite-dimensional quadratic form ≥ 0).
    - **Lemma CR (constant reproduction): PROVEN-HERE.**
      - (i) In coarse units d(QB)/L² is an average: f-values at level i + 1 are Σ_pŵ_P(p)f(p) with ŵ := w/L² ≥ 0 (A1's
        weights), row sums 1, column sums exactly L^{-4} and max_pŵ_P(p) ≤ L^{-4}. *Proof.* By A1(i)-(ii), w_P has row
        sums L², column sums L^{2-d}, and w_P(p) ≤ L^{-d}·L·L. ∎ Composite averages 𝔄_{i→j} (j > i) are again
        probability weights on same-plane plaquettes, supported within L^j of P (fine units), with column sums
        ≤ L^{-4(j-i)} and max ≤ L^{-4(j-i)}: max(ŵρ) ≤ maxŵ · colsum(ρ), then induct.
      - (ii) For every B [R910-fix: "for every critical point" deleted; (ii) holds for all B], and for any constant
        2-form F: QB(c) - ∫_{S_c}B = avg_{σ,y}Σ_{p∈Rib(σ,y)}
        ±(dB - F)(p). Hence |QB(c) - ∫_{S_c}B| ≤ 2L(L-1)·max_{p∈window(c)}|dB(p) - F_{plane(p)}|. *Proof.*
        ∫_{T^σ_y} - ∫_{S_c} is the flux through the ribbon swept by translating the axial path γ = P^σ(c_X → y) by
        Le_μ: a lattice surface of |γ|·L ≤ 2(L-1)L plaquettes. For a constant F, the flux of that loop is
        L·Σ_ν F_{νμ}(y - c_X)^ν, which is linear in y - c_X. Its average over the centred block vanishes (L odd). ∎ So the
        linear part of ε_V vanishes on constant curvature, by centring alone; the reflection symmetry that session 9
        argued for is not needed.
    - **Lemma J-str (the soft current has no funnel part): PROVEN-HERE.** At every critical point of Setting SC:
      - (a) d*r_i = 0 for every i (the coarse divergence at level i + 1).
      - (b) r_{i-1} = (κ_i/κ_{i-1})Q_str^Tr_i, and **J_0 := d*dB_0 = -κ_0Q_str^Tr_0**, where Q_str is the straight-leg
        average of L3g(a)-glob in own units.
      - (c) sup|r_i| ≤ (κ_{k-1}/κ_i)L^{-3(k-1-i)}sup|r_{k-1}|, and **sup|J_0| ≤ κ_{k-1}L^{-3k}sup|r_{k-1}|**. In coarse
        units (J^c = L^{3k}J) this is **sup|J^c_0| ≤ κ_{k-1}sup|r_{k-1}|, uniformly in k**.
      *Proof.*
      - The Euler-Lagrange equations: d*dB_0 + κ_0Q^Tr_0 = 0, and κ_{i-1}r_{i-1} = κ_iQ^Tr_i for 1 ≤ i ≤ k - 1.
      - Root covariance (L3g(a)-slice) gives Q∘d = d∘ev, with ev the restriction to the roots. Hence d*Q^T = ev^Td*.
      - Apply d* to the level-0 equation; d*d* = 0, so ev^Td*r_0 = 0, and d*r_0 = 0 since ev^T is injective. Apply d* to
        the level-i equation: κ_{i-1}d*r_{i-1} = κ_i ev^Td*r_i. Induct for (a).
      - L3g(a)-slice: Q = Q_str - d∘h exactly, so Q^T = Q_str^T - h^Td*. On co-closed r the funnel term h^Td*r vanishes,
        which is (b).
      - (c): for a fine link b = (z, μ), Q_str((X, μ), b) = L^{-4}#{(y, j) : y ∈ B(X), 0 ≤ j < L, y + je_μ = z} ≥ 0, and
        Σ_XQ_str((X, μ), b) = L·L^{-4}, since each j has exactly one y. So ||Q_str^T||_{∞→∞} = L^{1-d} = L^{-3}.
        Telescope the κ-ratios. ∎
      - *Meaning.* The S4' funnels (L3g-ob's line part) drop out of the soft current EXACTLY at critical points, so
        (BG-F5) does not occur at the linearised level. This explains c20's finding of no axial-line concentration; the
        same identity holds in d = 2. The bound is marginal in d = 4: L^{-3k} from Q_str^T against L^{3k} from the units.
    - **Lemma LES (lattice elliptic step, Campanato form): PROVEN-HERE.** Let F be a real 2-form on the plaquettes of
      Z⁴. Suppose that on a box Q_R(x_0) (side R ≥ 16): dF = K, d*F = J, |F| ≤ F_0, |J| ≤ J_0, |K| ≤ K_0 (componentwise).
      Then for every α ∈ (0, 1) there is an absolute C_α such that for every x ∈ Q_{R/2}(x_0) and 1 ≤ ρ ≤ R/4,
        Osc_2(F; Q_ρ(x)) := (ρ^{-4}Σ_{μ<ν}Σ_{y∈Q_ρ(x)}|F_μν(y) - F̄_μν|²)^{1/2} ≤ C_α(ρ/R)^α(F_0 + R(J_0 + K_0)).
      *Proof.* Use forward differences ∂_ρ and backward differences ∂_ρ⁻, with Δ := Σ_ρ∂_ρ⁻∂_ρ.
      1. *Componentwise Poisson equation.* Forward and backward differences commute, so (dd* + d*d)F = -ΔF on every
         component, by direct computation (as in L3g(a)-glob (1), now on 2-forms). Hence u := F_μν solves
         -Δu = ∂_μJ_ν - ∂_νJ_μ + (d*K)_μν, a sum of first differences of fields bounded by J_0 + K_0.
      2. *Splitting.* On a box Q_r ⊂ Q_R, write u = w + h. Here w = 0 off the interior and -Δw = (the source) inside.
         Summation by parts gives ||∇w||_2 ≤ 4r²(J_0 + K_0), and the Dirichlet Poincaré inequality gives
         ||w||_2² ≤ Cr⁶(J_0 + K_0)². h is discrete-harmonic inside Q_r.
      3. *Harmonic decay.*
         - Caccioppoli (summation by parts against η²(h - c)): Σ_{Q_s}|∇h|² ≤ C(s' - s)^{-2}Σ_{Q_{s'}}|h - c|².
         - Differences of harmonic functions are harmonic, so ≤ 5 iterations give ||∂_S∂_eh||_{2,Q_{r/4}} ≤
           Cr^{-|S|-1}||h - c||_{2,Q_r}.
         - The discrete Sobolev bound sup_Q|v| ≤ Σ_{S⊆{1..4}}n^{|S|-4}Σ_Q|∂_Sv| (the 1D bound
           |v(x)| ≤ n^{-1}Σ|v| + Σ|∂v|, tensorised over the 4 coordinates), with Cauchy-Schwarz, gives
           sup_{Q_{r/4}}|∇h| ≤ Cr^{-3}||h - h̄_r||_{2,Q_r}.
         - So Σ_{Q_ρ}|h - h̄_ρ|² ≤ C(ρ/r)⁶Σ_{Q_r}|h - h̄_r|² for ρ ≤ r/4.
      4. *One-step inequality.* With φ(ρ) := Σ_{Q_ρ(x)}|u - ū_ρ|² (concentric boxes), steps 2-3 give
         φ(ρ) ≤ A(ρ/r)⁶φ(r) + B_0(J_0 + K_0)²r⁶ for all 1 ≤ ρ ≤ r ≤ R/4. For r/4 < ρ ≤ r the bound is trivial.
         [R910-fix] So is the range r ≤ r_* for any absolute r_* (r_* = 20 suffices for steps 2-3): there
         φ(ρ) ≤ φ(r) ≤ A(ρ/r)⁶φ(r) once A ≥ r_*⁶, since ρ ≥ 1. All radii are integers ≥ 1, so this settles the
         integer-radii question.
      5. *Iteration lemma.* Suppose φ ≥ 0 is nondecreasing and φ(ρ) ≤ A(ρ/r)^aφ(r) + Br^b for ρ ≤ r ≤ R_1, with b < a.
         Then φ(ρ) ≤ C(A, a, b)(ρ/R_1)^b(φ(R_1) + BR_1^b).
         - Pick τ ≤ ½ with Aτ^a ≤ τ^{(a+b)/2}. Iterate along r_m = τ^mR_1 to get φ(r_m) ≤ τ^{mb}C(φ(R_1) + BR_1^b).
         - Fill in between the r_m by monotonicity.
         - Apply this with a = 6, b = 4 + 2α, B r⁶ ≤ (B R_1^{2-2α})r^{4+2α}, R_1 = R/4 and φ(R_1) ≤ 6R_1⁴F_0². ∎
      Constants are absolute (d = 4) and were not computed.
    - **Proposition BG-b-lin (BG-b for the linearised soft chain): PROVEN-HERE.** In Setting SC, let (B_i) be a critical
      point, and assume
      - **(H1)** sup_p|f_0(p)| ≤ F_0 (fine curvature in coarse units);
      - **(H2)** sup|r_{k-1}| ≤ R_top (top soft residual).
      Then BG-b holds, uniformly in k and the torus, **[R910-fix] for the levels n = k - j ≥ 1**, with
      M_2 = (1 + 2L²)(F_0 + 6κ̂R_top) + κ̂L³R_top and M_3 = C(L, α)(F_0 + (κ_{k-1} + κ̂)R_top), for any fixed α ∈ (0, 1).
      (b1) needs M_2 ≤ ε_*, i.e. small F_0 and R_top.
      **[R910-fix] Edge case n = 0 (j = k).** Then ρ_k = 5L^{k+1} > R/4, so step 4 does not apply, and ε_V needs r_k,
      the residual of the current RG step, which the chain does not contain. The n = 0 term is bounded by the sup form
      (b1), with (H2) extended to the current step's residual. **Constants.** Only κ̂ and κ_{k-1} enter; Setting SC's
      lower bound κ_- is not needed, so the c20 model scaling κ_i = κL^{-2i} (which violates it) is still covered.
      *Proof.*
      1. *Level recursion.* B_{i+1} = QB_i - r_i gives f_{i+1} = 𝔄f_i - ϱ_i, with ϱ_i := L^{2(k-i-1)}dr_i. By J-str (c),
         sup|ϱ_i| ≤ 4L^{2(k-i-1)}sup|r_i| ≤ 4κ̂L^{-(k-1-i)}R_top. Iterating, f_j = 𝔄_{0→j}f_0 - Σ_{i<j}𝔄_{i+1→j}ϱ_i.
      2. *(b1).* sup|f_j| ≤ F_0 + 4κ̂R_topΣ_{i<j}L^{-(k-1-i)} ≤ F_0 + 6κ̂R_top (L ≥ 3, by CR (i)). For a level-j cube Q,
         ε_2(Q) ≤ σ_n²sup|f_j| (abelian, so transport is trivial). ε_V(Q) ≤ 2L(L-1)σ_n²sup|f_j| + sup|r_j|, by CR (ii) with
         F = 0, and sup|r_j| ≤ κ̂L³σ_n³R_top. Sum the two bounds.
      3. *(b2).* With D_Q the data region (side ≤ 3L at level j; it contains the ribbons of the coarse links at Q):
         ε_3(Q) ≤ σ_n²osc_{D_Q}f_j, and CR (ii) with F := f_j at a point of D_Q gives
         ε_V(Q) ≤ 2L(L-1)σ_n²osc_{D_Q}f_j + κ̂L³σ_n³R_top. So
         ō_n ≤ (1 + 2L²)·mean_Q osc_{D_Q}f_j + κ̂L³σ_nR_top.
         - osc_{D_Q}f_j ≤ osc_{D_Q}(𝔄_{0→j}f_0) + 12κ̂R_topσ_n, by step 1.
         - For P, P' in D_Q (same plane), |𝔄f_0(P) - 𝔄f_0(P')| ≤ 2L^{-4j}Σ_{p∈U}|f_0(p) - c| ≤ 1250L⁴Osc_2(f_0; U) [R910-fix: factor 2], by CR (i)
           and Cauchy-Schwarz. Here U is the fine box of side ρ_j := 5L^{j+1} containing both supports.
      4. *Elliptic step.* Apply LES to F = L^{-2k}f_0 (fine units), with R := 20L^k and ρ_j ≤ R/4. The hypotheses hold
         everywhere, on the periodic extension to Z⁴: dF = 0, |F| ≤ L^{-2k}F_0, and |J| ≤ κ_{k-1}L^{-3k}R_top by J-str (c).
         This gives Osc_2(f_0; U) ≤ C_α(Lσ_n/4)^α(F_0 + 20κ_{k-1}R_top).
      5. Σ_nσ_n^α = (1 - L^{-α})^{-1} and Σ_nσ_n < 2, so Σ_nō_n ≤ M_3. ∎
      - *What it shows.* The two non-(H) ingredients of session 9's BG-b are now proven for the linearised soft chain:
        the lattice elliptic step (LES; Hölder-α, any α < 1, in place of the log-Lipschitz form guessed in session 9),
        and the soft-residual bound (J-str, CR). (H1) + (H2) is exactly the soft analogue of CMP 109 (1.2): (H1) is the
        curvature condition |U(∂p) - 1| < ε_0η², and by J-str (c), (H2) implies the current condition |J| < ε_0, with
        J = d*F.
    - **Non-abelian transfer (B-NA): argued, not counted.** For SU(N) critical points with coarse curvature ≤ ε_0:
      - (i) *Recursion.* A1-NA(1) steps 3-4 give, in the axial gauge of W_P, log V'_P = Σ_pw_P(p)X^{ax}_p + O(C_4φ_P²).
        polar(M̄_c) differs from S4'(V)_c by exp(O(C(L)ε_2³)): the Hermitian part of the mean goes into |M̄|. So step 1
        holds with an extra ϱ^{NA}_i, |ϱ^{NA}_i| ≤ C(L)σ_n²F_0² in coarse units, which is summable like ϱ_i.
      - (ii) *Elliptic step.* In the tree gauge of the box Q_R (R = 20L^k), |a_b| ≤ CRφ = O(L^{-k}F_0). The lattice
        Bianchi identity (holonomy around a 3-cube = 1) and the Wilson Euler-Lagrange equation give, by BCH,
        dX = K and d*X = J_soft + J' with |K|, |J'| ≤ C(|a||X| + |X|²) = O(L^{-3k}F_0²). LES with K then holds with
        J_0 + K_0 → κ_{k-1}R_top + CF_0² in coarse units.
      - (iii) *J-str.* The Noether identity D*_Vr = 0 at critical points is exact non-abelian: the Wilson action's gradient
        is gauge-orthogonal identically, and the soft term is invariant under fine gauge transformations at the roots
        combined with coarse gauge transformations of V (c22 Q1). The decomposition Q = Q_str - d∘h holds up to Ad-
        transports 1 + O(|a|) on one block, so the funnel remainder is ≤ C(L)|a||r|, i.e. O(F_0R_top) in coarse units.
      - [R910-fix] When (iii) is written it must be reconciled with the L3g(a)-slice R3-fix: there is no nonlinear SU(N)
        analogue of Q = Q_str - d∘h as an identity. (iii) uses a perturbative tree-gauge expansion with Ad-transports
        1 + O(|a|) on one block; that is an estimate, not an identity, and has to be stated as one.
      - What remains: writing (i)-(iii) with constants. No new mechanism is expected; (BG-F6) was not seen in c22.
    - **Check c22** (criteria checks/c22_criteria.md before checks/c22_soft_su2_4d.py; SU(2), d = 4, 9⁴ fine torus,
      L = 3, κ = 1): **VALID** (V1 all four runs converged to |g|/|g0| ≤ 1e-7 in 117-565 iterations; V2 control
      power R_ax(Q_root^T r_ctrl) = 9.57 vs R_ax(Q_str^T r_ctrl) = 0.89; V3 start-config N1 = 1.48). Findings:
      **Q1 PASS** (Noether identity at the minimiser: N1 = 1.0e-8, 1.3e-7, 4.5e-7, 1.2e-6 at t = 0.02, 0.1, 0.2, 0.4,
      at the gradient-tolerance level); **Q2 PASS** (R_ax(J) = 1.00, 1.01, 1.04 (1.17 at t = 0.4) against the J-str
      prediction R_ax(Q_str^T r_min) ≈ 1.00, while the funnel-carrying Q_root^T r_min grows to 1.34, 2.08, 4.38: the
      residual is covariantly but not plainly co-closed, and the current still shows no funnel concentration, as
      B-NA (iii) argues; [R910-fix] at t ≤ 0.1 Q2 has no discriminating power: there the funnel-carrying alternative
      Q_root^T r_min itself has R_ax = 1.016, 1.343, under the 1.5 threshold, so only t = 0.2 (Q_root^T r_min = 2.08
      vs J = 1.04) genuinely tests B-NA (iii); V2's control power is against a generic r, not against this
      alternative); **Q3 FAIL as pre-registered**: deviations from the linear regime are small (dev_S = 0.016,
      0.013, 0.078; dev_O = 0.022, 0.033, 0.052 at t = 0.1, 0.2, 0.4), but the monotonicity sub-criterion
      dev_S(0.2) ≥ dev_S(0.1) failed (an UNVERIFIED explanation [R910-fix: labelled]: S is a maximum, whose nonlinear
      correction may change sign, as in c18). The criterion is not edited. [R910-fix] The deviations do not scale like
      t²: dev_O = 0.022, 0.033, 0.052 grows by 1.5×, not 4×, from t = 0.1 to 0.2. So c22 shows that the NA deviations
      are small, not that they have the O(ε_0²) form claimed in B-NA (i)-(ii). Informational: at κ = 1 the soft term dominates (ES/EW ≈ 5-7) and the mean residual ≈ 1.26t, of the
      size of the data, so R_top is comparable to the coarse curvature here (consistent with (H2) being a smallness
      hypothesis on the same scale ε_0, not an extra gain). Run: 394 s, 573 MB peak, load 1.8, 38% free memory, nice 10,
      BLAS threads 1; two pre-run smoke tests disclosed in checks/c22_time.txt. Scope: one step (n = 1), one κ, one
      data field; it tests J-str's mechanism and the size of NA corrections, not the multi-level summability.
    - **BG-reg status: OPEN, narrowed to the membership hypotheses (H1) + (H2) for the soft minimiser** (plus the
      non-abelian bookkeeping B-NA (i)-(iii)). The lattice elliptic step and the soft residual are done (linearised).
      (H1) + (H2) are the sup-norm/localisation content of L2 for the soft kernel (CMP 102's role). Energy
      minimality gives them only in L², globally. A Caccioppoli/hole-filling argument for the chain would need the
      exponential decay of the soft background map, i.e. the same content.
  - **(DF) dependency sub-DAG [S10] (RTARGET §14).** Nodes are precise statements; "⇐" lists the inputs; [A]/[B] marks
    what sessions-10 targets A/B discharged.
    - **N1. Thm 27 → Theorem CE**: PROVEN-HERE [A]. Used by N7, N9.
    - **N2. L2-soft**: for coarse data V with coarse curvature ≤ ε_0, the soft chain minimiser exists, is unique up to
      gauge, depends smoothly on V with exponential decay, and satisfies (H1) + (H2). OPEN (soft analogue of CMP 102
      Thm 1 + Sect. F-G). **[S11] Linear half narrowed to (LED)**: gauge-orbit lemma N2-a (abelian and SU(N)),
      k-uniform ℓ² forms of (H1)/(H2) (Lemma N2-E, Corollary N2-ℓ²), and (H1) + (H2) ⇐ (LED) (Proposition N2-red),
      all PROVEN-HERE (L5 [S11]). OPEN: (LED), and the SU(N) versions. **[S12] (LED), (H1), (H2) PROVEN for the
      linearised chain** (Theorem N2-lin). OPEN: the SU(N) versions, and smooth dependence with decay for complex data.
      **[S13] Exponential decay PROVEN for the linearised chain** (Theorem N2-exp: B_k-kernels and the F ↦ r kernel,
      rate m_*(L, κ_±) > 0 uniform in k and T). OPEN: the SU(N) versions and the non-linear analytic dependence.
      **[S14] Reduced** (Proposition B-NA-red): the SU(N) chain follows from (G♯) + (R♯) (+ (FP♯)), OPEN; NA-alg,
      NA-crit, NA-IFT, SRC-id PROVEN. Failure modes BNA-F1-F3 established. Strip width m_*' (Theorem N2-exp').
    - **N3. BG-b ⇐ (H1) + (H2)**: PROVEN-HERE for the linearised chain [B] (LES, CR, J-str, BG-b-lin); non-abelian
      transfer argued. So BG-b ⇐ N2 + N3.
    - **N4. (FP) gauge fixing** for the soft fluctuation integral (δ(h) slice + residual Feynman term + Faddeev-Popov
      control): OPEN (the L3g(a)-slice completion). **[S11] Abelian identity PROVEN** (Lemma FP-ab and its
      application, L5 [S11]): the legitimate fixing is δ(h)·e^{-½||P_resd*A||²}, with an A- and b-independent
      constant. The double fixing with the full Δ carries an explicit Gaussian weight W. OPEN: the physical gap on Phys
      (equivalent to the uniform gap of O_FP on H_0); (NA); (IT). **[S12] The physical gap is PROVEN** (Proposition PG,
      c_PG = min(1, κ)/(3.5·10⁶), uniform in n and T). OPEN: (NA); (IT') (the slice of the composite root map; IT-str
      settles the straight part). **[S13] (IT') PROVEN** (Proposition PG^{(k)}). OPEN: (NA).
      **[S14] (NA) identity PROVEN** (Proposition NA-FP, every critical background, direct and composite slices).
      OPEN: the (NA) gap, and the background dependence of the Faddeev-Popov constant FP_U.
    - **N5. L3g-soft covariance**: 𝒞 := (Hessian of the soft action at the background, gauge-fixed)^{-1/2}. Needed: a
      uniform gap (abelian linear: L3g(a)-glob/slice PROVEN; (NA), (IT) OPEN), the ℓ² bound Σ_x||𝒞(b,x)||² ≤ C_0², an
      ℓ¹ bound Σ_x||𝒞(b,x)|| ≤ C_1', and a random-walk expansion that survives complex s-weakening. OPEN. [S12] Its
      abelian one-level gap is now available (Proposition PG); still needed: (NA), (IT'), the ℓ¹ bound, the
      random-walk expansion. [S13] (IT') is PROVEN (PG^{(k)}); still needed: (NA), the ℓ¹ bound and the random-walk
      expansion for the soft Hessian covariance (a different object from the N2-exp response kernels).
      [S14] The covariant fixing is legitimate at every critical background (NA-FP); still needed: the (NA) gap, the
      ℓ¹ bound and the random-walk expansion.
      [S18] Trivial background PROVEN (Theorem N5-triv). [S19] Random-walk expansion with complex s-weakening PROVEN at the
      trivial background, every level (Theorem RW, Corollary RW-triv); level-0 operator at curvature-small backgrounds
      PROVEN (Theorem N5-sf0, T ≥ T_0); levels i ≥ 1 reduced to (NA-H_loc) (Proposition N5-sf_i). Still OPEN.
      **[R1819-fix SF-2/SF-3]** N5-sf0 is an existence theorem (r_*, S_* not computed); its proven gap was ≈ 7·10⁻⁸²
      (≈ 4·10⁻⁵¹ with N5-w0), and is ≥ γ'(1 - ε_R)/9 ≈ 6.6·10⁻¹⁰ by Proposition RW-ℓ² [S20]. **[S20]** Level 1 for the
      critical branch: Theorem NAH1 ((NA-H_loc)_1) and Corollary N5-sf1; level i ≥ 2: Proposition NAH-ind (implication).
      ⇐ N2, N4.
    - **N6. L4a-form-soft polymer bound**: the interaction is Σ_XH(X, W) with |H(X)| ≤ H_0e^{-κd(X)} on the truncation
      ball, analytic in the background. OPEN for the soft kernel (hard: IMPORTED-NOT-YET-REVERIFIED, CMP 116).
      ⇐ N2, N5. **[R910-fix] Requirement from Theorem CE:** N6 must deliver the decay rate κ > 3κ_0 + 3 in M-units
      (≈ 9.2·10³ with session 10's κ_0 = 324 log 12800; ≈ 457 with the [S11] κ_0 = 16 log 12800, Lemma CE-geo') and
      H_0 ≤ c_0(κ) ∝ e^{-2κ}. As in Dimock, the rate is maintained by reblocking: his (243) gives the rate
      L(κ - 5κ_0 - 5) after one block step, and "κ ≥ 10(κ0 + 1) which we assume" keeps it ≥ κ.
      **[S13]** The linear background response has coarse-unit rate m_* (Theorem N2-exp), i.e. m_*M in M-units; on its
      own this allows κ > 457 only for M ≳ 457/m_* (≈ 4·10⁴ proven; ≈ 470 at the located rate 0.98, κ = 1).
      **[S14]** With Theorem N2-exp', M ≳ 457/m_*' ≈ 1.2·10⁴ (κ ≡ 1).
      **[S16]** Lemma F-df_0 (L5 [S16]) gives the F-kernel of f_0 (exponential, rate m' < m_*'), so N6's linear interface
      (exponential F-kernels for r_{k-1} and f_0) is proven for the linearised chain; N6 itself stays OPEN.
    - **N7. (DF1)** (Dimock form with an ultralocal truncated Gaussian μ*) ⇐ N4, N5, N6. OPEN.
    - **N8. (DF2)** ⇐ N2 (ε_2(𝒰) + ε_V(𝒰) ≤ ε_*/4 is BG-b (b1) at one level, so N3) + N5 (ℓ²). OPEN only through N2,
      N5.
    - **N9. (DF3')** ⇐ N7 + N8 + N1 (with Remark CE-cx) + N5 (ℓ¹) + [H_0ρ_W bounded, ρ_W the truncation radius].
      *Argued [S10]:*
      - Tilt μ* site by site with the real weights e^{t⟨c_x, W(x)⟩}. Then log E e^{tℓ} = Σ_x log Z_x(t) +
        (log Ξ_t - log Ξ_0).
      - Lemma AG bounds the first sum by t²C_0²/2.
      - Theorem CE applies to both Ξ_t and Ξ_0 (probability measures with the same support). H# is holomorphic in the
        activities on the polydisc of step 3, so Cauchy estimates give
        |log Ξ_t - log Ξ_0| ≤ CH_0Σ_x min(2, |t||c_x|ρ_W) ≤ C H_0ρ_W||c||_1|t|.
      - This yields (DF3') with m_0 = CH_0ρ_W C_1' and η = 0.
      - The Thm 27 dependence of (DF3') is discharged [A]; the remaining inputs are N7, N5's ℓ¹ bound and H_0ρ_W = O(1).
      - [R910-fix] *Cauchy margin.* Theorem CE's bound holds on the closed polydisc 𝔻 only. Run Theorem CE with
        r_Y → 2r_Y (H_0 → H_0/2 in its hypotheses), so that the activities of Ξ_t and Ξ_0 lie in the half-radius
        polydisc; Cauchy's estimate on the doubled polydisc then gives the Lipschitz bound on 𝔻.
      - [R910-fix] *Range of t.* W1-size' uses (DF3') with |t| ~ 1/g, so the argument must hold there. The real tilts
        give probability measures, and the min(2, |t||c_x|ρ_W) form keeps each site's change bounded; this is to be
        checked line by line when N9 is written.
    - **N10. (DF4)** ⇐ N2 (smooth, exponentially decaying V-dependence) + N5 (random walk with complex s) + N6
      (analytic in V). OPEN.
    - **N11. W1-LD** ⇐ W1-size' (PROVEN) + AG (PROVEN) + N7 + N8 + N9.
    - **N12. W1-cl** ⇐ N10 + N1 (PROVEN [A]) + the corridor localisation (argued [S9]).
    - **Critical path:** N2 (soft L2) feeds N3, N5, N6, N8 and N10. N4 (FP) feeds N5. N5 and N6 are the L3g/L4a-form
      content. After this session the wall of W1-loc and BG-reg is exactly {N2, N4, N5, N6}, the small-field package
      for the soft RG. No cluster-expansion import and no (linearised) [R910-fix] elliptic-regularity gap remain on
      these two items; the non-abelian elliptic step is B-NA (ii), argued only.

- **[S11] Session 11: N2 linear half, N4 abelian, the sharper polymer-size bound. Targets pre-stated in RTARGET.md
  §16-18 before the derivations; the c21 addendum and the c23/c24/c25 criteria were written before the scripts.
  Status of L5 unchanged: IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE: Lemma CE-geo' (polymer size; sharper
  Theorem CE constants); Lemma N2-E (with Lemma N2-a and Corollary N2-ℓ²); Proposition N2-red (with Lemma LES-sup);
  Lemma FP-ab (with its soft-step application). Checks c21 (re-run, 14/14), c23, c24, c25.
  - **Lemma CE-geo' (polymer size, touching-tree reading; proves the upper inequality of Dimock's (122), stated
    there with d = 3 [R1112-fix]): PROVEN-HERE.** Let τ be a connected
    finite union of segments in the torus (R/TZ)^d, of total length ℓ, and N(τ) the number of closed unit cubes
    □_k = k + [-½, ½]^d that τ meets. Then
      **(g1') N(τ) ≤ 2^d + 2^{d-1}√d·ℓ;** hence |X| ≤ 2^d + 2^{d-1}√d·d(X), and in d = 4, **|X| ≤ 16(1 + d(X))**.
    Since 2^d ≤ 3^d and 2^{d-1}√d ≤ 3^d, this implies the upper inequality of Dimock's (122), |X|_M ≤ 3^d(1 + d_M(X)),
    which he quotes from [22] without proof (his (122) is stated with d = 3). [R1112-fix] (122) also has a lower
    inequality, d_M(X) ≤ |X|_M; it is NOT proven here and is not used anywhere in this ledger. The proof below in fact
    gives the sharper N(τ) ≤ 2^d + 2^{d-1}Σ_jℓ_j|u_j|_1 (u_j the unit direction of segment j).
    *Proof.* Order the segments s_1, …, s_m so that each s_j meets s_1 ∪ … ∪ s_{j-1} (possible because τ is
    connected), and lift them one at a time to R^d, each attached at a lift of its meeting point. The lift τ̃ is
    connected, has length ℓ, and maps onto τ. A cube □_k meets τ iff some lattice translate of it meets τ̃, so N(τ) is
    at most the number of k ∈ Z^d with dist_∞(k, τ̃) ≤ ½. For each such k, k + [-½, ½]^d ⊂ τ̃ + K, K := [-1, 1]^d, and
    these boxes have disjoint interiors. So N(τ) ≤ vol(τ̃ + K). Put τ_j := lift of s_1 ∪ … ∪ s_j. Then
    τ_j + K = (τ_{j-1} + K) ∪ (s̃_j + K), and s̃_j + K ⊃ p + K with p ∈ s̃_j ∩ τ_{j-1}. For a segment of length ℓ_j and
    direction u, vol(s̃_j + K) = vol(K) + ℓ_j·vol_{d-1}(proj_{u^⊥}K) (Cavalieri), and the projection of [-1, 1]^d onto
    u^⊥ has volume 2^{d-1}|u|_1 ≤ 2^{d-1}√d. So vol(τ_j + K) ≤ vol(τ_{j-1} + K) + 2^{d-1}√d·ℓ_j, and vol(τ̃ + K) ≤
    2^d + 2^{d-1}√d·ℓ. Take the infimum over τ for |X|. ∎ The constant is sharp at ℓ = 0 (a point at a cube corner
    meets 2^d cubes). No assumption T ≥ 3 is needed.
    *New Theorem CE constants (d = 4).* Re-run the proof of Theorem CE with (g1') in place of (g1). (g2)-(g3) are
    unchanged, and a = log 12800 as before.
    - (g4') d(X) ≥ |X|/16 - 1, so with **κ_0 := 16a ≈ 151.3**: Σ_{X∋□}e^{-κ_0d(X)} ≤ e^{κ_0}Σ_{X∋□}e^{-a|X|} ≤
      **K_0 := e^{κ_0}/6400**.
    - (g5') |Y| ≤ 16(1 + d(Y)) ≤ κ_0(1 + d(Y)), and 1 + d ≤ e^d.
    - Step 1: the second condition becomes H_0 ≤ (32K_0)^{-1}e^{-2(κ-κ_0)}. It gives u ≤ |Y|/16 ≤ 1 + d(Y), so
      |K(Y)| ≤ 2H_0K_0·16(1 + d)e^{1+d}e^{-κ'd} ≤ C_KH_0e^{-κ_1d(Y)}, with **C_K := 32eK_0** and κ_1 = κ - κ_0 - 2.
    - Step 4 is unchanged in form: it uses only |Y| ≤ κ_0(1 + d(Y)) and (g5'). B := C_Ke^{κ_0}K_0 and C_1 := 2κ_0B.
      The third condition is (8B)^{-1}e^{-2(κ-3κ_0-2)}.
    So Theorem CE holds with κ_0 ≈ 151.3 in place of 3064.1. The hypothesis becomes **κ > 3κ_0 + 3 ≈ 457** (was
    ≈ 9.2·10³), and the rate is κ - 3κ_0 - 3. Remark CE-cx and Proposition CE-κ hold verbatim with the new constants.
    **Node N6 must now deliver κ > 3κ_0 + 3 ≈ 457 in M-units.**
    Check c25 (criteria first): exact cube counts for 6045 random and adversarial segment unions in d = 2, 3, 4. Q1
    PASS: no violation. The largest ratio N/(2^d + 2^{d-1}√d·ℓ) is 1.0000 (the corner point), and the largest
    N/(3^d(1 + ℓ)) is 0.44, 0.30, 0.20 in d = 2, 3, 4. 7.5 s, 40 MB.
  - **N2, linear half (RTARGET §16).**
    - *Setting.* Setting SC [S10], d = 4, κ_i ≤ κ_+. Level i lives on Λ_i = (Z/T_iZ)^4, T_i = TL^{k-i}, in its own units.
      The levels are nested: a level-(i+1) site X is the level-i site LX + o, o = (L-1)/2. Hence a level-i site x has
      coarse coordinate p_i(x) = (x - o_i)/L^{k-i}, o_i = (L^{k-i} - 1)/2. The level-k lattice is the vertex set of
      the cubical torus (R/TZ)^4, and every level-i cell lies in a closed coarse cube. E(B_0, …, B_{k-1}; B_k) is the
      chain energy, and E_k(B_k) := inf over B_0, …, B_{k-1}.
    - **Lemma N2-a (gauge-orbit lemma): PROVEN-HERE (counted with N2-E).**
      - (abelian) Minimisers exist. The residuals r_i and dB_0 are the same at every minimiser and depend linearly
        on B_k. E_k, the r_i and dB_0 depend on B_k only through dB_k, and they vanish when dB_k = 0. This includes
        the non-exact flat classes, so the field size of B_k (pure gauge or constant) can be arbitrary.
      - (SU(N)) For the soft chain with the tree-level exponent of the normalised kernel (D4-norm):
        E_NA := S_W(U) + Σ_i(κ_i/g²)Σ_cφ_c, with φ_c := N^{-1}[max_{W∈SU(N)}Re tr(W^{-1}M̄_c) - Re tr(V_{i+1,c}^{-1}M̄_c)]
        ≥ 0. For every gauge-invariant quantity (the φ_c, the plaquette traces), the SET of its values over the global
        minimisers is an invariant of the coarse gauge orbit of V_k [R1112-fix: was "at every global minimiser … is a
        function of the coarse gauge orbit"; uniqueness of the global minimiser up to the chain gauge group is not
        shown for SU(N), and at small curvature it is part of the OPEN SU(N) N2]. If V_k is flat, the minimum is 0, so every φ_c = 0 and every plaquette is 1.
      *Proof (abelian).*
      - E is a convex quadratic polynomial bounded below, so it attains its infimum.
      - The minimisers are x* + ker(Hess). For v in that kernel, the quadratic part vanishes, so dv_0 = 0 and
        Qv_i = v_{i+1} (v_k = 0). Hence the r_i and dB_0 do not depend on the minimiser.
      - The minimisers solve the normal equations M^T(Mx - NB_k) = 0. These are linear in (x, B_k), so solutions add
        and the residual vector Mx - NB_k is additive in B_k.
      - If dB_k = 0, Lemma N2-E gives E_k(B_k) = 0, so every term vanishes. By additivity, adding a closed B' to B_k
        changes no residual and no dB_0. ∎
      *Proof (SU(N)).*
      - (i) Covariance. A fine gauge transformation at level i whose root values are the level-(i+1) transformation
        maps M̄_c → g(c_X)M̄_cg(c_Y)^{-1} and V_{i+1,c} likewise, so φ_c is invariant; S_W is invariant. A coarse h on
        Λ_k lifts level by level (constant on each block), giving a bijection between the chains for V_k and for V_k^h
        that preserves E_NA and every gauge-invariant quantity.
      - (ii) Flatness. If every plaquette of V_k is 1, transport is path-independent on the universal cover, and the
        holonomies H_μ around the torus cycles commute (the commutator loop is contractible). Commuting unitaries are
        simultaneously diagonalisable: H_μ = Wexp(iΘ_μ)W^{-1}, with Θ_μ real diagonal and tr Θ_μ = 0 (det = 1; shift
        one angle by 2π). The constant field D_μ := Wexp(iΘ_μ/T)W^{-1} is flat with the same based holonomies, so
        V_k = D^h for a coarse gauge h (h(x) := transport of V_k from the base point to x, times the inverse transport
        of D).
      - (iii) Zero-energy lift. Put U_b := Wexp(iΘ_μ/(TL^k))W^{-1} on every fine link in direction μ, and
        V_i := Wexp(iΘ_μ/T_i)W^{-1} on every level-i link. Everything commutes, so S_W = 0. Every S4' contour from c_X
        to c_Y has net displacement Le_μ, so M̄_c = Wexp(iΘ_μL/T_i)W^{-1} = V_{i+1,c} ∈ SU(N), whose maximiser is
        V_{i+1,c} itself; so φ_c = 0. Hence E_NA = 0 is the global minimum, and every global minimiser has all
        terms 0. ∎
      So the set of values of R_top over global minimisers [R1112-fix] is invariant under V_k → V_k^h for coarse gauge
      transformations of any size, and R_top vanishes at every global minimiser on every flat class, whatever the
      holonomy. This is the exact half of "R_top is bounded by the curvature, not by
      |log V|". The quantitative half follows.
    - **Lemma N2-E (curvature energy bound): PROVEN-HERE.** For every B_k, uniformly in k ≥ 1 and the torus (L ≥ 3
      odd, d = 4):
        **E_k(B_k) ≤ C_E(1 + κ_+)||dB_k||²,  C_E := 1.2·10⁸** (absolute; not optimised).
      *Construction (cubical Whitney forms).* On a coarse cube C = n + [0, 1]^4 and a j-face f = n + a + span{e_μ : μ ∈ I}
      (|I| = j, a ∈ {0, 1}^4, a_μ = 0 for μ ∈ I), put w_f := Π_{ν∉I}φ_{a_ν}(x_ν - n_ν)dx_I with φ_0(s) = 1 - s and
      φ_1(s) = s. For a coarse j-cochain c, W(c)|_C := Σ_{f⊂C}c(f)w_f. Then:
      - (W1) the tangential traces agree on shared faces, so W(c) is a piecewise-polynomial form with continuous
        tangential traces;
      - (W2) dW = Wd, because W is the tensor product of the 1D cochain map (v_0, v_1) ↦ v_0φ_0 + v_1φ_1, e ↦ e dt;
      - (W3) ∫_fW(c) = c(f);
      - (W4) on C, |W(c)_I(x)| ≤ M_I(C) := max_{f⊂C of type I}|c(f)| (a convex combination), and
        |W(c)_I(x) - W(c)_I(y)| ≤ 2(4 - j)M_I(C)|x - y|_∞.
      R_i is the de Rham map to the level-i lattice, R_iω(σ) := ∫_σω. By (W1) and Stokes on each closed cube,
      dR_iW = R_iWd, and R_kW = id by (W3).
      *Test chain.* B̃_i := R_iW(B_k) for 0 ≤ i ≤ k, so B̃_k = B_k. Write M_C := max_{P⊂C}|dB_k(P)| over the 24
      coarse plaquettes of C.
      - *Fine action.* dB̃_0 = R_0W(dB_k), so a fine plaquette p ⊂ C has |dB̃_0(p)| ≤ L^{-2k}M_C. Assign each fine
        plaquette to one closed cube containing it: at most 24L^{4k} per cube. Each coarse plaquette lies in at most 4
        cubes, so ||dB̃_0||² ≤ 24Σ_CM_C² ≤ 96||dB_k||².
      - *Residuals.* Fix 0 ≤ i ≤ k - 1, m := k - 1 - i, and a level-(i+1) link c. Since S_c (the straight level-i path
        from c_X to c_Y) is the segment c, B̃_{i+1}(c) = ∫_cW(B_k) = ∫_{S_c}B̃_i. So r̃_i(c) = QB̃_i(c) - ∫_{S_c}B̃_i.
        Lemma CR (ii) holds for every B [R910-fix], so for any constant F,
        |r̃_i(c)| ≤ 2L(L-1)max_{p∈window(c)}|dB̃_i(p) - F_{plane(p)}|. The window lies in a closed box Ω_c of sup-side
        2L^{-m} (coarse units). Take F_I := L^{-2(m+1)}W(dB_k)_I(x_c) with x_c ∈ Ω_c. Then |dB̃_i(p) - F_I| ≤
        L^{-2(m+1)}osc_{Ω_c}W(dB_k)_I, so |r̃_i(c)| ≤ 2L^{-2m}osc_{Ω_c}. By (W4):
        - if Ω_c lies in one closed cube C, osc ≤ 8L^{-m}M_C, so |r̃_i(c)| ≤ 16L^{-3m}M_C;
        - otherwise osc ≤ 2M'_c, so |r̃_i(c)| ≤ 4L^{-2m}M'_c. Here M'_c is the max of M_{C'} over the cubes C' meeting
          Ω_c, all of them within ℓ^∞-distance 3 of C (≤ 7⁴ cubes).
        A closed cube contains at most 4(L^m + 1)⁴ ≤ 64L^{4m} level-(i+1) links. The links assigned to C whose box is
        not inside C have their base site within 4 grid layers of ∂C, and there are at most 1024L^{3m} of them. Hence
        ||r̃_i||² ≤ Σ_C[64·256L^{-2m}M_C² + 1024·16L^{-m}Σ_{C'∼C}M_{C'}²] ≤ 4·10⁷L^{-m}Σ_CM_C²
        ≤ 1.6·10⁸L^{-m}||dB_k||².
      - Summing, Σ_m L^{-m} ≤ 3/2, and E_k ≤ E(B̃) ≤ 48||dB_k||² + (κ_+/2)(3/2)·1.6·10⁸||dB_k||² ≤ 1.2·10⁸(1 + κ_+)||dB_k||². ∎
      Only κ_i ≤ κ_+ is used. The per-level residual bound decays like L^{-m}, so no level-count factor appears: this
      is how the marginal d = 4 scaling (L^{-4m} fewer links against L^{2m}-larger per-link values, by (W4)) is beaten
      by the centring cancellation of CR (ii) away from coarse faces (failure mode N2-F2 avoided).
    - **Corollary N2-ℓ² (ℓ² forms of (H1) and (H2)).** At every minimiser,
      κ_{k-1}||r_{k-1}||² ≤ Σ_iκ_i||r_i||² ≤ 2C_E(1 + κ_+)||dB_k||², and L^{-4k}Σ_p|f_0(p)|² = ||dB_0||² ≤
      2C_E(1 + κ_+)||dB_k||². So the top residual and the fine curvature are bounded in ℓ² by the coarse curvature,
      uniformly in k and the torus; failure mode N2-F1 is excluded.
    - **Proposition N2-red ((H1) + (H2) ⇐ (LED)): PROVEN-HERE.** Let Ĉ be the 3⁴ block of coarse cubes around a coarse
      cube C, and E_loc(C) the part of the minimiser's chain energy carried by fine plaquettes and level-(i+1) links in
      Ĉ. Suppose **(LED)** sup_CE_loc(C) ≤ C_loc·sup|dB_k|². Then
      - **(H2)** sup|r_{k-1}| ≤ (2C_loc/κ_{k-1})^{1/2}sup|dB_k|;
      - **(H1)** sup|f_0| ≤ C_H[(2C_loc)^{1/2} + κ_{k-1}(2C_loc/κ_{k-1})^{1/2}]sup|dB_k|, for k ≥ 2, with C_H absolute.
      For k = 1 the trivial bound sup|f_0| ≤ L²(2C_loc)^{1/2}sup|dB_k| holds.
      - **Lemma LES-sup.** Under LES's hypotheses on Q_R(x_0) with R ≥ 16, but without an a priori sup bound:
        sup_{Q_{R/2}(x_0)}|F| ≤ C[(R^{-4}Σ_{Q_R(x_0)}|F|²)^{1/2} + R(J_0 + K_0)].
        *Proof.* LES step 5 uses only φ(R_1), and φ(R_1) ≤ Σ_{Q_{R_1}}|F|². So with b = 4 + 2α,
        ρ^{-4}φ(ρ) ≤ C(ρ/R_1)^{2α}[R_1^{-4}φ(R_1) + R_1²(J_0 + K_0)²]. Telescope ū over the boxes Q_{⌈2^{-j}R_1⌉}(x),
        down to the one-site box, where ū = F(x): |ū_{ρ/2} - ū_ρ| ≤ 4(ρ^{-4}φ(ρ))^{1/2}, a geometric series in
        (ρ/R_1)^α. Add |ū_{R_1}| ≤ (R_1^{-4}Σ|F|²)^{1/2}, with R_1 = R/4. ∎
      *Proof of the proposition.* (H2): for c ⊂ C, (κ_{k-1}/2)|r_{k-1}(c)|² ≤ E_loc(C). (H1): apply LES-sup to the fine
      F = dB_0 on the box of side R = 3L^k around C (R ≥ 16 for k ≥ 2). There dF = 0, and by J-str (c),
      |d*F| = |J_0| ≤ κ_{k-1}L^{-3k}sup|r_{k-1}|. Also R^{-4}Σ|F|² ≤ (3L^k)^{-4}·2E_loc(C). Multiply by L^{2k}:
      sup_C|f_0| ≤ C[(2E_loc(C))^{1/2}/9 + 3κ_{k-1}sup|r_{k-1}|]. Insert (H2). ∎
    - **(LED) attempt: not proven. Exact failing step.** The hole-filling route compares the minimiser with
      B_i' := dλ_i + χ(B_i - dλ_i), with a coarse cutoff χ (gradient 1/R) and compatible gauges (ev λ_i = λ_{i+1},
      λ_k = 0). It needs the commutators [Q, χ](B_i - dλ_i) to cost ≤ θ·E_annulus with θ < 1, uniformly in k. In a
      gauge with |B_i - dλ_i| ~ L^{-(k-i)}b per level-i link (b the coarse field scale), the naive bound is
      κ_iL^{-2m}R^{-2}L²||B_i - dλ_i||² ~ R^{-2}L²b² per coarse cell and per level. Summed over the k levels this is
      O(kR^{-2}L²b²), not O(b²): the marginal d = 4 count again. Beating it needs one of:
      - the centring cancellation of [Q, χ] on gauge-fixed fields that are smooth on the level-(i+1) scale (then each
        level costs L^{-2m}, as in N2-E);
      - or a multiscale Poincaré inequality in a smooth gauge, Σ_iκ_iL^{-2(k-i)}||B_i - dλ_i||²_{Ω} ≤ CR²E_{Ω'}, with
        C uniform in k.
      Both are regularity statements of the kind being proven, so (LED) is the remaining wall of N2's linear half.
      The same marginality appears in the naive lower bound: telescoping f_{i+1} = 𝔄f_i - ϱ_i gives only
      ||dB_k||² ≤ (k + 1)C(1 + κ_-^{-1})E_k. So a Combes-Thomas argument, which needs a k-uniform coercivity, also stops at the same
      point. Numerics (c23 I2, d = 2 only): the response to curvature at one coarse link has a local-energy decay rate
      of 6.83, 3.48, 2.77, 2.65 per coarse unit at k = 1, 2, 3, 4. It stabilises, consistent with a k-uniform (LED);
      this is not evidence for d = 4.
    - **Check c23** (criteria checks/c23_criteria.md before checks/c23_n2_residual.py).
      - **Part A** (abelian chain, LSMR; d = 2, T = 9, k = 1..4, up to 1.2·10⁶ unknowns; d = 4, 9⁴, k = 1): VALID
        (V1, V2 PASS: E_k ≤ E_W everywhere, R_kW = id exactly).
        - **Q1 PASS** (gauge orbit: max|Δr_top|/max|r_top| ≤ 4.5e-11 with |λ| ~ 50 and constants ~ 10 added).
        - **Q2 PASS** (closed data: E/|B|² ≤ 4.4e-25).
        - **Q3 FAIL as pre-registered.** The criterion compared max_k with 1.5× the k = 2 value; it fails because the
          k = 1 value is the largest. E_W/||dB||² = 0.0795, 0.0298, 0.0254, 0.0241 (data R) and 0.0610, 0.0105, 0.0062,
          0.0038 (data S), and the true E_k/||dB||² = 0.0586, 0.0144, 0.0024, 0.0003 (R). These decrease in k (d = 2 is
          not marginal). There is no growth, but the criterion as written FAILED, and it is not edited.
        - d = 4, k = 1: E_1/||dB||² = 0.056 (R), 0.054 (S), against E_W/||dB||² = 0.27, 0.29.
        - I1: sup|r_top|/sup|dB| = 0.17, 0.046, 0.0094, 0.0011 and sup|f_0|/sup|dB| = 1.07, 2.48, 3.70, 4.05 (d = 2,
          k = 1..4; the latter is saturating); 0.43 and 0.14 in d = 4, k = 1.
        - 65.7 s, 469 MB.
      - **Part B** (SU(2), d = 4, c22 machinery, t = 0.1): VALID (V3, all four converged).
        - **Q4 PASS:** with a Haar-random coarse pure gauge (field size Φ = 2.94 vs 0.34), E and R_top agree to all 9
          printed digits (3.56405808, 0.268296).
        - **Q5 PASS:** with a constant flat diagonal field times the data (Φ = 1.10 vs 0.34, coarse curvature
          C = 0.81 vs 0.49), R_top = 0.289 vs 0.268, a ratio 1.08, against 0.5Φ-ratio 1.62 and 2C-ratio 3.27. The
          residual stays at the curvature scale, not the field-size scale.
        - **Q6 PASS:** the flat field alone (holonomy angles up to 0.9) gives E = 2.7e-11 and R_top = 6.7e-7. The
          gauge-naive start reached the flat lift.
        - 256 s, 473 MB.
      - One pre-run smoke test of the geometry pieces at a tiny size (disclosed in checks/c23_time.txt); no edits after
        it.
    - **N2 status: OPEN, narrowed to (LED)** (plus B-NA (i)-(iii) for SU(N), and the SU(N) analogue of N2-E).
      - PROVEN for the linearised chain: the exact gauge-orbit half (abelian and SU(N)), the ℓ² forms of (H1) and
        (H2) with k-uniform constants (N2-E), and (H1) + (H2) ⇐ (LED) (N2-red).
      - So BG-b ⇐ (LED), by N2-red and BG-b-lin. Existence and linear dependence are trivial in the linear case.
        Uniqueness holds modulo the chain gauge group, by N2-a.
  - **N4, abelian (RTARGET §17).**
    - **Lemma FP-ab (linear Faddeev-Popov): PROVEN-HERE.** Let 𝒱 = R^n and let Λ = R^m act by A ↦ A + Γλ, with Γ
      injective. Let I ≥ 0 be measurable and invariant, with ∫_{(ΓΛ)^⊥}I < ∞. Let χ = (χ_1, χ_2) : 𝒱 → R^{m_1} ⊕ R^{m_2},
      m_1 + m_2 = m, be linear and **admissible** (χΓ invertible). Then
        ∫_𝒱 I(A)δ(χ_1(A))e^{-½|χ_2(A)|²}dA = (2π)^{m_2/2}|det χΓ|^{-1}det(Γ^TΓ)^{1/2}∫_{(ΓΛ)^⊥}I(A_⊥)dA_⊥.
      The constant does not depend on A or on any parameter inside I. For complex F, apply this to |F| for
      integrability, then use linearity.
      *Proof.* Change variables A = A_⊥ + Γλ (Jacobian det(Γ^TΓ)^{1/2}); I(A) = I(A_⊥). Then
      ∫dλ δ(χ_1A_⊥ + (χΓλ)_1)e^{-½|χ_2A_⊥ + (χΓλ)_2|²} = (2π)^{m_2/2}|det χΓ|^{-1} by the substitution μ = χΓλ and a
      shift. Fubini. ∎
    - **Application to the soft step at fixed b.** Take I(A) = F(A)e^{-½||dA||² - (κ/2)||QA - b||²}.
      - *The symmetry group.* Q∘d = d∘ev (root covariance), so A ↦ A + dλ preserves I iff ev λ is constant (F
        invariant). Modulo constants the group is Λ := {λ : λ(c_X) = 0 ∀X}, acting freely through Γ = d|_Λ. It is
        exactly the degeneracy of the Gaussian part: dv = 0 and Qv = 0 force v = dλ with ev λ constant, because a
        constant 1-form h has Qh = Lh.
      - *Legitimate fixing.* χ := (h, P_resd*), where h is L3g(a)-slice's functional and P_res is the orthogonal
        projector onto Λ_res := {λ ∈ Λ : Σ_{B(X)}λ = 0 ∀X}. The dimensions match: N_c + (N_f - 2N_c) = dim Λ. χΓ is
        injective: h(dλ) = Q_0λ - λ(c) = Q_0λ, so h(dλ) = 0 puts λ in Λ_res; then P_resΔ_0λ = 0 gives
        ||dλ||² = ⟨λ, P_resΔ_0λ⟩ = 0, so λ = 0. So the fixing **δ(h)·e^{-½||P_resd*A||²}** gives the true integral
        times a constant that depends only on (n, T, L). It does not depend on A, b, κ or F. The slice alone is not
        admissible: the Λ_res orbits are non-compact.
      - *L3g(a)-slice's double fixing δ(h)e^{-½||d*A||²} is NOT legitimate as an identity.* On the H_0-representative,
        ∫_{Λ_res}e^{-½||d*A + Δ_0λ||²}dλ = c·W(A), where W(A) := e^{-½||(1-Π_r)d*A||²} and Π_r is the orthogonal
        projector onto Δ_0(Λ_res). W is invariant along the residual orbits but is not constant. (1 - Π_r) has rank
        2N_c - 1 on mean-zero scalars: its range is Δ_0^{-1}(span{δ_{c_X}, 1_{B(X)}}) ∩ 1^⊥. For example, a
        block-constant ψ that is not constant gives dψ ∈ H_0 with (1 - Π_r)Δψ ≠ 0. So the double fixing computes
        ∫I·W, with an explicit Gaussian weight in 2N_c - 1 coarse divergence moments of A, not ∫I.
      - *The legitimate fluctuation operator and its gap.* In the legitimate gauge, the Gaussian part has
        **O_FP := d*d + κQ^TQ + dP_resd* on H_0**. On H_0 write A = A^ph + dλ with λ ∈ Λ_res and A^ph ⊥ dΛ_res, i.e.
        P_resd*A^ph = 0. Then Qdλ = d ev λ = 0 and the cross terms vanish, so
        ⟨A, O_FPA⟩ = ||dA^ph||² + κ||QA^ph||² + ||P_resΔ_0λ||².
        Functions in Λ_res have zero block means, so the Neumann block Poincaré inequality (coarse units, first
        eigenvalue ≥ 4) gives ||P_resΔ_0λ||² ≥ 4||dλ||². So: **O_FP has a uniform gap on H_0 iff the physical gap
        holds: ||dA||² + κ||QA||² ≥ c||A||² on Phys := {A : h(A) = 0, d*A ∈ span(δ_{c_X}, 1_{B(X)})}, uniformly in n and
        T.** L3g(a)-slice gives this with ||d*A||² added on the left. On Phys, ||d*A||² is exactly the lost term, the
        2N_c root-and-block divergence components.
    - **Check c24** (criteria checks/c24_criteria.md before checks/c24_fp_gap.py; dense generalised eigenproblems,
      H_0 by a 10⁷-relative penalty): VALID.
      - V1 PASS: λ_min(O_Δ on H_0) = 1.0000 at every size (≥ 1/5, as L3g(a)-slice proves).
      - **Q1 PASS** (admissibility): λ_min(O_FP on H_0) > 0 at every size.
      - I1: λ_min(O_FP) = 0.349, 0.288, 0.271, 0.265 in d = 2 (T = 4, n = 3, 5, 7, 9); 0.426, 0.365 in d = 3 (T = 3,
        n = 3, 5); 0.359 in d = 4 (T = 2, n = 3). In d = 2 the decrements shrink (0.061, 0.016, 0.006), consistent with
        a positive limit. Small sizes cannot show uniformity, least of all the d = 4 logarithmic regime.
      - 177 s, peak 1.69 GB. A dense-to-sparse builder rewrite was made before the only run, for memory; it is
        disclosed in checks/c24_time.txt.
    - **N4 status.** (FP) as an identity is PROVEN (Lemma FP-ab and its application): the legitimate abelian fixing is
      δ(h) plus a Feynman term on Λ_res, with an A- and b-independent constant. The L3g(a)-slice "double gauge fixing"
      is corrected: it carries the explicit weight W. The remaining part of the L3g(a)-slice completion's (FP) is the
      **physical gap on Phys** (OPEN; c24 supports it at small sizes). (NA) and (IT) are unchanged. N5 needs N2 (LED)
      and this gap.

- **[S12] Session 12: (LED) and the sup forms of N2's linear half; the N4 physical gap. Targets pre-stated in
  RTARGET.md §20-22. They were written after the lead's exploratory reasoning in this session, but before any written
  derivation and before any session-12 script. The c26/c27 criteria were written before the scripts. One c26 addendum
  was written after Parts A-B and before Part C was coded (disclosed). Status of L5 unchanged:
  IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE (both unreviewed):
  - Theorem N2-lin, with Lemmas IT-str, LED-dual, LED-symb, WA and Proposition LED-unif counted with it;
  - Proposition PG, with Lemmas PG-flux, PG-orbit, PG-ext and PG-line counted with it.
  Checks c26 (A VALID; Q1-Q4, Q5, Q6, V3 PASS; Q7 FAIL as pre-registered) and c27 (E1, E2, E4-E6 PASS; E3 FAIL as
  pre-registered, a normalisation flaw in one sub-check).
  - **N2, linear half: the sup forms (RTARGET §20).** Setting SC, d = 4, L ≥ 3 odd, κ_- ≤ κ_i ≤ κ_+, coarse torus
    side T ≥ 1, level-i quantities in own units, n := L^k.
    - *Notation.* Q_str^{(s)} is the direct straight average of block side s:
      (Q_str^{(s)}A)(X, μ) = s^{-4}Σ_{y∈sX+{0..s-1}⁴}Σ_{j<s}A_μ(y + je_μ). CoCl_0 is the space of co-closed coarse 1-forms
      with zero mean, and Closed is the space of closed coarse 1-forms (exact plus constant), so CoCl_0^⊥ = Closed.
    - **Lemma IT-str (composite straight averages): PROVEN-HERE.** The composite of m one-step straight averages (block
      side L each) equals Q_str^{(L^m)}, and likewise for the transposes.
      *Proof.*
      - Take m = 2. The level-(i+1) link (Y + je_μ, μ) carries avg_{y∈B(Y+je_μ)}∫_y^{y+Le_μ}. The translation
        y ↦ y + jLe_μ maps B(Y) onto B(Y + je_μ), so Σ_{j<L} of these is avg_{y∈B(Y)}∫_y^{y+L²e_μ}.
      - Average over Y ∈ B(X). The level-i blocks of the sites of one level-(i+1) block tile L²X + {0..L²-1}⁴, each
        level-i site once, with weight L^{-4}·L^{-4} = (L²)^{-4}.
      - Induct on m. ∎
      - Two consequences for the root maps:
        - Q_root = Q_str - dh at each level and Q_str d = dM, so a composite of root maps equals Q_str^{(L^m)} plus a
          coarse exact form.
        - On co-closed inputs, the transposes agree: (Q_root^T)^m r = Q_str^{(L^m)T}r, because Q_root^T preserves
          co-closedness (d*Q^T = ev^Td*) and Q_root^T = Q_str^T on co-closed forms (J-str).
      - This settles the straight-average half of (IT) exactly. The composite slice functional is not covered (IT',
        below).
    - **Lemma LED-dual (dual reduction): PROVEN-HERE.** Let (B_i) minimise the chain energy, r := r_{k-1}, and
        P := Σ_{m=0}^{k-1}(κ_{k-1}/κ_{k-1-m})Q_str^{(L^m)}Q_str^{(L^m)T} + κ_{k-1}G_k,  G_k := Q_str^{(n)}Δ^{-1}Q_str^{(n)T},
      where Δ is the fine Hodge Laplacian, inverted off the constants. Then:
      - (i) r_i = (κ_{k-1}/κ_i)Q_str^{(L^{k-1-i})T}r, J_0 = -κ_{k-1}Q_str^{(n)T}r, and dB_0 = dΔ^{-1}J_0;
      - (ii) r ∈ CoCl_0 and B_k + Pr ∈ Closed;
      - (iii) r is the unique minimiser over CoCl_0 of ½⟨s, Ps⟩ + ⟨s, B_k⟩, and **E_k(B_k) = (κ_{k-1}/2)⟨r, Pr⟩**.
      *Proof.*
      - (i) is J-str (a)-(b) with IT-str. J_0 = d*dB_0 is co-closed and orthogonal to the harmonic forms, and
        d*d = Δ on co-closed forms, so B_0 - Δ^{-1}J_0 is closed.
      - (ii), co-closedness: J-str (a).
      - (ii), zero mean: J_0 ∈ Ran d* is orthogonal to the constants h. Also ⟨Q_str^{(n)T}r, h⟩ = n⟨r, h⟩, because
        Q_str^{(n)}h = nh in own units. Hence ⟨r, h⟩ = 0.
      - (ii), B_k + Pr ∈ Closed: iterate B_{i+1} = QB_i - r_i. Q_root maps closed forms to closed forms (Qd = d ev,
        and Q(const) = L·const since h(const) = 0 by centring). By IT-str, modulo Closed,
        B_k ≡ Q_str^{(n)}Δ^{-1}J_0 - Σ_iQ_str^{(L^{k-1-i})}r_i = -Pr, using (i).
      - (iii): the functional is strictly convex on CoCl_0, since P ≥ I by the m = 0 term. Its stationarity condition
        is Ps + B_k ∈ CoCl_0^⊥ = Closed. For the energy, Σ_i(κ_i/2)||r_i||² = (κ_{k-1}/2)⟨r, 𝒮'r⟩ by (i), with 𝒮' the
        m-sum, and ½||dB_0||² = ½⟨J_0, Δ^{-1}J_0⟩ = (κ_{k-1}²/2)⟨r, G_kr⟩. ∎
      - c26 A confirms (i)-(iii) to ≤ 2e-13 on nine tori (d = 2, 3, 4; k ≤ 3; including non-constant κ_i).
    - **Lemma LED-symb (coarse symbols): PROVEN-HERE.** Every operator in LED-dual is diagonal in the components and
      invariant under coarse translations. Define
      - D_s(θ) := s^{-1}Σ_{j<s}e^{-iθj/s};
      - W_{s,μ}(θ) := Π_αD_s(θ_α)·D_s(θ_μ);
      - φ_s(θ) := Σ_α4s²sin²(θ_α/2s), the fine Laplacian in coarse units;
      - θ_K := p + 2πK for p ∈ T⁴ = (R/2πZ)⁴.
      Then
        P̂_μ(p) = Σ_m(κ_{k-1}/κ_{k-1-m})L^{-2m}Σ_{K∈(Z/L^m)⁴}|W_{L^m,μ}(θ_K)|² + κ_{k-1}Σ_{K∈(Z/n)⁴}|W_{n,μ}(θ_K)|²/φ_n(θ_K).
      All summands are 2πs-periodic, so each K-sum runs over one period. Put ν_μ(p) := e^{ip_μ} - 1, F := dB_k and
      F̂_{νμ} = ν_νb̂_μ - ν_μb̂_ν. Then
        **r̂_μ(p) = -P̂_μ^{-1}Σ_νP̂_ν^{-1}ν̄_νF̂_{νμ} / Σ_ν|ν_ν|²P̂_ν^{-1}** (p ≠ 0), and r̂(0) = 0.
      The coarse-unit fine curvature f_0 = n²dB_0 at the fine sites nX + u, u ∈ {0..n-1}⁴, is Σ_Y𝒦_u(X - Y)F(Y), with
        𝒦̂_u(p)_{ρσ} = -κ_{k-1}Σ_{K∈(Z/n)⁴}e^{iθ_K·u/n}[ν^{(n)}_ρW_{n,σ}r̂_σ - ν^{(n)}_σW_{n,ρ}r̂_ρ](θ_K)/φ_n(θ_K),
        ν^{(n)}_ρ(θ) := n(e^{iθ_ρ/n} - 1).
      *Proof.*
      - Decimation identities: for Q(X, b) = w(b - nX), (QMQ^T)^(p) = n^{-4}Σ_Kŵ(q_K)M̂(q_K)ŵ(q_K)^* with q_K = θ_K/n,
        and (Q^Tr)^(q) = ŵ(q)r̂(nq). Here ŵ_μ(q) = nW_{n,μ}(nq) and Δ̂(q) = φ_n(nq)/n².
      - The constrained minimisation of LED-dual (iii) is solved at each p, with one multiplier for Σ_μν̄_μr̂_μ = 0. ∎
      - c26 A: the formulas reproduce the LSMR r and f_0 to ≤ 4e-13, at every fine offset. The Laplace-integral
        evaluation of the alias sums (1/φ = ∫e^{-tφ}dt, which factorises over directions) agrees with the direct sums
        to ≤ 2e-13.
    - **Lemma WA (homogeneous-type symbols have ℓ¹ kernels): PROVEN-HERE.** Let h be 2π-periodic on R⁴ and C⁵ on
      T⁴∖{0}, with |∂^αh| ≤ M on {|p| ≥ ½} for all |α| ≤ 5. Suppose that on {0 < |p| ≤ 1}, h = h_0 + h_1, where
      |∂^αh_0| ≤ M and |∂^αh_1(p)| ≤ M|p|^{a-|α|} for all |α| ≤ 5, with some a > 0 [R1112-fix: was "a ∈ (0, 1]";
      the proof below works for every a > 0, and LED-unif uses a = 2]. Then
      Σ_{X∈Z⁴}|ȟ(X)| ≤ C(a)M. The kernel on (Z/TZ)⁴ (the inverse discrete transform of h on the grid (2π/T)Z⁴) is the
      periodisation of ȟ, so it obeys the same bound.
      *Proof.*
      - Take a smooth χ with χ = 1 on |p| ≤ ½ and support in |p| ≤ 1, and put ψ_j(p) := χ(2^jp) - χ(2^{j+1}p).
        Split h = (1 - χ)h + χh_0 + Σ_{j≥0}ψ_jh_1.
      - The first two pieces are periodic and C⁵. Five integrations by parts give |ȟ(X)| ≤ CM(1 + |X|)^{-5}, which is
        summable in d = 4.
      - The j-th piece is supported in 2^{-j-2} ≤ |p| ≤ 2^{-j}, where |∂^α(ψ_jh_1)| ≤ CM2^{-ja}2^{j|α|}. So
        |(ψ_jh_1)ˇ(X)| ≤ CM2^{-ja}2^{-4j}min(1, 2^{5j}|X|^{-5}), and the ℓ¹ norm of the piece is ≤ CM2^{-ja}. Sum over j.
      - Periodisation is Poisson summation, valid since Σ|ȟ| < ∞. [R1112-fix: the sentence "h(0) is the limit h_0(0)"
        is withdrawn.] The value of the finite-T operator at p = 0 (there r̂(0) = 0) need not equal the limit of h, and
        it does not matter: the p = 0 mode is irrelevant, since F̂(0) = 0 for F = dB_k. ∎
    - **Proposition LED-unif (uniform symbol bounds): PROVEN-HERE.** Let Π_coex := C(p)^†C(p)/ψ(p), where C(p) is the
      coarse lattice d on 2-forms and ψ := Σ_α|ν_α|²; Π_coexF̂ = 0 whenever dF = 0. Then Lemma WA's hypotheses hold:
      - for the entries of 𝓡̂ (F̂ ↦ r̂), with a = 2;
      - for the entries of 𝒦̂_u + Π_coex, with a = 1.
      M depends only on (L, κ_-, κ_+), uniformly in k ≥ 1, T and u.
      *Proof.*
      - (1) *One-dimensional facts, uniform in s ≥ 3.*
        - From D_s(θ) = (1 - e^{-iθ})/(s(1 - e^{-iθ/s})) and |s(1 - e^{-iθ/s})| = 2s|sin(θ/2s)| ≥ 2|θ|/π on
          |θ| ≤ πs: |∂^aD_s(θ)| ≤ C_a(1 + |θ|)^{-1} for a ≤ 6.
        - |D_s(θ)| ≥ 2/π on |θ| ≤ π. |D_s|² is even and real-analytic on |θ| ≤ 3π/2 with uniformly bounded
          derivatives, and |D_s|² = 1 - (1 - s^{-2})θ²/12 + O(θ⁴).
        - On [-πs, πs]⁴: φ_s ≥ (4/π²)|θ|² and |∂^α(1/φ_s)| ≤ C_α|θ|^{-2-|α|}. Also |ν^{(s)}_ρ(θ)| ≤ |θ_ρ|, with
          bounded derivatives.
      - (2) *Alias sums.* Take representatives θ_K ∈ [-πn, πn]⁴. For K ≠ 0:
        - the summands of P̂ and their p-derivatives of order ≤ 6 are ≤ CΠ_α(1 + |θ_α|)^{-2}(1 + |θ_μ|)^{-2}(1 + |θ|)^{-2};
        - those of 𝒦̂_u are ≤ CΠ_α(1 + |θ_α|)^{-1}(1 + |θ_σ|)^{-1}(1 + |θ|)^{-1}. The phase contributes |u/n| ≤ 1 per
          derivative.
        Both bounds are summable over K ∈ Z⁴. For the second, the sum over the three directions other than σ is
        bounded by a constant times Σ_j j^{-2}(1 + log j)². The m-sum in P̂ converges geometrically: the m-th term,
        with its derivatives, is ≤ Cκ̂L^{-2m}. Hence:
        - on |p| ≤ 1, P̂_ν = κ_{k-1}|W_{n,ν}(p)|²/φ_n(p) + R_ν(p), with R_ν ≥ 0, even, smooth, with uniform C⁶ bounds;
        - P̂_ν is smooth on {|p| ≥ ½} with uniform bounds;
        - 1 ≤ P̂_ν ≤ C|p|^{-2} (the m = 0 term gives the lower bound).
      - (3) *𝓡̂ near 0.*
        - P̂_ν^{-1} = φ_ng_ν with g_ν := (κ_{k-1}|W_{n,ν}|² + φ_nR_ν)^{-1}, which is even and smooth with uniform C⁶
          bounds, and g_ν(0) = 1/κ_{k-1}. Hence 𝓡̂ = -(φ_n/D_g)·g_μg_νν̄_ν, with D_g := Σ_ν|ν_ν|²g_ν.
        - Write φ_n/D_g = κ_{k-1} + u/v with u := φ_n - κ_{k-1}D_g and v := κ_{k-1}D_g. Both are even and smooth, and
          their quadratic Taylor terms are both |p|². So |∂^αu| ≤ C|p|^{4-|α|} for |α| ≤ 4, and ∂⁵u is bounded.
        - v ≥ c|p|², |∂^αv| ≤ C|p|^{2-|α|} for |α| ≤ 2, and higher derivatives are bounded.
        - The quotient rule gives |∂^α(u/v)| ≤ C|p|^{2-|α|} for |α| ≤ 5: type a = 2.
        - Away from 0, P̂_ν ≥ 1 and D ≥ ψ·min_νP̂_ν^{-1} ≥ c, so 𝓡̂ is smooth there with uniform bounds.
      - (4) *𝒦̂_u near 0.*
        - The K ≠ 0 part is (uniformly C⁵)·r̂, hence of WA type.
        - On |p| ≤ 1, the K = 0 part is e^{ip·u/n}Σ[ν_ρc_{ρσ}X_σ - ν_σc_{σρ}X_ρ]/D_g. Here X_σ := Σ_λg_λν̄_λF̂_{λσ},
          c_{ρσ} := κ_{k-1}ρ̃_ρW_{n,σ}g_σ = 1 + O(|p|), and ρ̃_ρ := ν^{(n)}_ρ/ν_ρ is smooth with ρ̃(0) = 1.
        - Replace c_{ρσ} by 1 and g_λ by g := g_1. What remains is Π_exF̂·(1 + O(|p|²)) with Π_ex := ν∧(ν̄⌟·)/ψ. The
          replaced terms are O(|p|³)|F̂| analytic numerators over D_g ≥ c|p|², so they are of type a = 1.
        - The flat lattice identity dd* + d*d = ψ on 2-forms gives Π_ex + Π_coex = I. So 𝒦̂_u + Π_coex =
          e^{ip·u/n}I + (1 - e^{ip·u/n})Π_coex + (type a ≥ 1) near 0, and it is smooth away from 0. ∎
      - **Why Π_coex is needed (failure mode LED-F2 for the naive extension).** Extended to all 2-forms F, the f_0 map
        contains the degree-0 projector Π_ex, whose kernel ~|x|^{-4} is not summable. c26 B shows this: N_f = 4.5, 5.5,
        6.3 at T = 12, 16, 20, with each value k-stable. On closed F the projector term is absent.
      - [R1112-fix] The proof above gives only ℓ¹ / power-tail BOUNDS, not exponential decay: type a = 2 is an upper
        bound on the regularity loss, and the non-analyticity of u/v was not shown. Whether the r map is exponentially
        local was open after session 12 (numerically it appeared to be); see Theorem N2-exp [S13] below.
        N10 (DF4) needs smooth dependence with decay for complex data, and that stays OPEN.
    - **Theorem N2-lin (sup forms for the linearised soft chain): PROVEN-HERE.** For every B_k, uniformly in k ≥ 1
      and T:
        **(H2) sup|r_{k-1}| ≤ C_R sup|dB_k|,  (H1) sup|f_0| ≤ C_f sup|dB_k|,**
      with C_R and C_f depending only on (L, κ_±). They come from the absolute constants of Lemma WA, which were not
      computed. Consequently:
      - sup|r_i| ≤ κ̂L^{-3(k-1-i)}C_R sup|dB_k| and sup|J^c_0| ≤ κ_{k-1}C_R sup|dB_k|, by J-str (c);
      - **(LED)** holds: E_loc(C) ≤ C_loc sup|dB_k|², with C_loc := 243C_f² + 183κ̂κ_+C_R².
      *Proof.*
      - r = 𝓡_T∗F and f_0(n· + u) = (𝒦̂_u + Π_coex)ˇ_T∗F, using Π_coexF = 0 (dF = 0). Young's inequality with
        Lemma WA and Proposition LED-unif gives (H1) and (H2).
      - (LED): Ĉ contains ≤ 486L^{4k} fine plaquettes, each with |dB_0| = L^{-2k}|f_0|, and ≤ 324L^{4(k-1-i)} level-(i+1)
        links. Hence E_loc(C) ≤ 243 sup|f_0|² + Σ_m162(κ_{k-1}²/κ_{k-1-m})L^{-2m}sup|r|². ∎
      - So BG-b holds for the linearised chain by Proposition BG-b-lin, with F_0 = C_f sup|dB_k| and
        R_top = C_R sup|dB_k|, for the levels n ≥ 1 and at small coarse curvature. Proposition N2-red and Lemma LES-sup
        are no longer needed for this, but stay valid.
    - **Check c26** (criteria checks/c26_criteria.md, with an addendum written before Part C; disclosures in
      checks/c26_time.txt).
      - **Part A: VALID; Q1-Q4 PASS.** The dual and symbol formulas match the LSMR chain to ≤ 4e-13, including d = 4,
        T = 2, k = 2 (IT-str in d = 4) and non-constant κ_i.
      - **Part B** (d = 4, L = 3).
        - N_r = 2.857, 2.741, 2.729, 2.727, 2.727, 2.727 at κ = 1, T = 16, k = 1..6.
        - κ = 0.25: 5.72 → 5.36; κ = 4: 1.276 → 1.248 (k = 1..5).
        - At k = 5: 2.714 (T = 12) and 2.729 (T = 20).
        - Q5 and Q6 PASS. But the Part B N_f is the kernel of the extension to all F, and it grows with T (see above).
      - **Part C.** The representative 𝒦̂_u + Π_coex reproduces the LSMR f_0 on closed F to 3e-13 (V3 PASS).
        - N_f^rep = 8.91, 9.79, 10.09, 10.20, 10.24, 10.25 at T = 16, k = 1..6.
        - At k = 5: 9.74, 10.24, 10.54, 10.75 for T = 12, 16, 20, 24.
        - **Q7 FAILED as pre-registered.** The T = 24 to T = 12 ratio is 1.104 > 1.1. The k-part passes.
        - [R1112-fix: informational reading, not a criterion] The T-increments 0.50, 0.31, 0.21 fit c/T, consistent
          with a summable |x|^{-5} tail, as the a = 1 term would give. A |x|^{-4} tail would grow like log T. The
          criterion is not edited. Part B's "axis slope(3..7)" values are log-log slopes taken up to x ≈ T/2 and are
          κ-dependent; they are not tail exponents and are not cited as such.
      - Timings: 5 s, 53 s, 79 s; peak RSS 850 MB.
    - **N2 status [S12]. The linear half of N2 is PROVEN:**
      - existence (trivial) and uniqueness modulo the chain gauge group (N2-a);
      - the ℓ² bounds (N2-E);
      - the sup forms (H1)-(H2) and (LED) (Theorem N2-lin).
      So BG-b holds for the linearised soft chain at small coarse curvature, for the levels n ≥ 1 (the n = 0 term needs
      the current step's residual) [R1112-fix], with no further hypothesis.
    - **N2 stays OPEN** for:
      - the SU(N) chain: B-NA (i)-(iii), plus SU(N) analogues of N2-E and N2-lin;
      - the smooth dependence with decay for complex data (N10).
  - **N4: the physical gap (RTARGET §21).** One linearised abelian soft step in coarse units, d = 4, ε = 1/n (n odd ≥ 3),
    coarse torus side T ≥ 2:
    - ⟨A, A⟩ = ε⁴Σ|A|², with d, d* carrying 1/ε, and ||∇A||² := Σ_{μ,ν}||∂_νA_μ||² = ||dA||² + ||d*A||² (L3g(a)-glob (1));
    - Q = Q_root, which equals Q_str on H_0; M is the block mean on scalars;
    - B(X) = nX + ε{0..n-1}⁴ in fine coordinates, with root c_X at its centre.
    - **Lemma PG-flux: PROVEN-HERE.** Let F(A)(X, μ) := ε³Σ_{z∈B(X), z_μ in the top layer}A_μ(z) be the flux from B(X) into
      B(X + e_μ). Then:
      - (a) d*A = 0 implies d_c^*F(A) = 0;
      - (b) ||Q_strA - F(A)||² ≤ 4Σ_μ||∂_μA_μ||² ≤ 4||∇A||² for every A.
      *Proof.*
      - (a) Sum d*A over the sites of B(X). Internal bonds cancel, leaving Σ_μ[F(X - e_μ, μ) - F(X, μ)] (up to the
        normalisation ε^{-1}).
      - (b) Fix (X, μ) and a transverse column; let a(t) be its μ-bond values on the slab B(X) ∪ B(X + e_μ),
        t = 0..2n-2. The column's part of Q_strA is ε³Στ(t)a(t), with tent weights τ ≥ 0 summing to 1, and its part of
        F is ε³a(n-1). So the difference is ε³Στ(t)(a(t) - a(n-1)).
      - |a(t) - a(n-1)| ≤ εΣ_{t'}|∂_μa(t')| ≤ ε(2n)^{1/2}(Σ_{t'}|∂_μa|²)^{1/2}. Cauchy-Schwarz over the n³ columns gives
        |Q_strA - F|²(X, μ) ≤ 2||∂_μA_μ||²_{slab}.
      - Each bond lies in at most two slabs (T ≥ 2). ∎
    - **Lemma PG-orbit: PROVEN-HERE.** For A ∈ H_0, let ψ := Δ^{-1}d*A (mean zero) and A_c := A - dψ. Put r_X := ψ(c_X),
      m := Mψ, and E(r, m) := min{||dφ||² : φ(c_X) = r_X, Mφ = m}. Then:
      - inf_{λ∈Λ_res}||A + dλ||² = ||A_c||² + E(r, m);
      - r - m = h(A_c).
      *Proof.*
      - A_c is co-closed, hence orthogonal to every exact form.
      - {ψ + λ : λ ∈ Λ_res} is exactly the set of φ with φ(c_X) = ψ(c_X) and Mφ = Mψ.
      - h(dψ) = Mψ - ev ψ and h(A) = 0. ∎
      - The physical gap is equivalent to: inf_{orbit} ≤ C(||dA||² + ||QA||²) on H_0. The Phys element of each orbit is
        its minimal-norm element, and dA and QA are constant on Λ_res-orbits.
    - **Lemma PG-ext (cheap extension): PROVEN-HERE.** E(r, m) ≤ 4.25·10⁵||d_cm||² + 160ε²Σ_X|r_X - m_X|².
      *Construction.*
      - φ̃ := the multilinear interpolation of m with nodes at the c_X.
        - Each fine difference quotient is a convex combination of the ≤ 16 coarse differences on the ≤ 2 dual cubes
          that the bond meets. Each coarse edge is used by ≤ (2n + 1)³(n + 2) bonds.
        - So ||dφ̃||² ≤ 22||d_cm||² for n ≥ 3.
        - The block-mean defects δ_X := m_X - Mφ̃(X) satisfy Σ|δ_X|² ≤ 216||d_cm||². This uses |δ_X| ≤ max over the 3⁴
          neighbours of |m_Y - m_X|, coarse paths of ≤ 4 edges, and ≤ 54 boxes per edge.
      - φ_1 := φ̃ + Σ_Xδ_Xβ_X, with β_X := b_nΠ_μsin(π(j_μ + 1)/(n + 1)) on B(X) and Mβ_X = 1.
        - b_n = (n/cot(π/(2(n+1))))⁴ ≤ (π/2)⁴, and ||dβ_X||² = ε²λ_DΣβ² ≤ (π/2)^{10}(n + 1)²/n² ≤ 163.
        - Each bond meets ≤ 2 bumps, so ||Σδ_Xdβ_X||² ≤ 2·163Σδ².
      - φ := φ_1 + Σ_Xa_Xγ_X, with a_X := r_X - φ_1(c_X) and γ_X := (1_{c_X} - n^{-4}β_X)/(1 - n^{-4}β_X(c_X)).
        - Mγ_X = 0, γ_X(c_X) = 1, and ||dγ_X||² ≤ 20ε². The point spike costs 8ε² in d = 4.
        - |a_X|² ≤ 2|r_X - m_X|² + 2b_n²|δ_X|², since φ̃(c_X) = m_X.
      - Collect, with ε² ≤ 1/9. [R1112-fix: the split, written out.] By |a + b + c|² ≤ 4|a|² + 4|b|² + 2|c|²
        (weights 4, 4, 2 on φ̃, bumps, spikes; 1/4 + 1/4 + 1/2 = 1), and ≤ 2 spikes per bond:
        ||dφ||² ≤ 4·22||d_cm||² + 4·2·163·216||d_cm||² + 2·2·20ε²Σ_X|a_X|²
        ≤ [88 + 281664 + 2·2·20·2·(π/2)⁸·216/9]||d_cm||² + 2·2·20·2·ε²Σ|r_X - m_X|²
        = 4.241·10⁵||d_cm||² + 160ε²Σ|r_X - m_X|² ≤ 4.25·10⁵||d_cm||² + 160ε²Σ|r_X - m_X|². ∎
    - **Lemma PG-line (line trace of h): PROVEN-HERE.** Let C_3 := sup_n max_{s_0}|f(s_0) - f̄|²/Σ|∇f|² over the 3D
      Neumann cubes of side n (lattice units). Then C_3 ≤ 14, and for every A and every block,
        ε²|h(A)(X)|² ≤ 8ε²||A||²_{B(X)} + 8C_3ε||∇A||²_{B(X)}  (block-internal differences).
      *Proof.*
      - *C_3.* Expand in the Neumann cosine basis. Then |φ_k(s_0)|² ≤ 8/n³ and λ_k ≥ 4|k|²/n², so
        C_3 ≤ (2/n)Σ_{k≠0}|k|^{-2} ≤ (2/n)·7(n - 1) < 14 (shells |k|_∞ = j have ≤ 7j² points).
      - *Paths.* Each axial path P^σ(c_X → y) has ≤ 4 legs. Each leg lies on one μ-line of the block and has ≤ n bonds.
        Cauchy-Schwarz gives |∫_PA|² ≤ 4εΣ_legsΣ_{line}A_μ².
      - *Lines.* On each transverse 3D slice, A_μ(s_0)² ≤ 2n^{-3}Σ_{slice}A_μ² + 2C_3Σ_{slice}|∇_⊥A_μ|² (lattice units).
      - Converting units gives |∫_PA|² ≤ 8||A||²_B + 8C_3ε^{-1}||∇A||²_B. Apply Jensen over the paths (σ, y). ∎
    - **Proposition PG (physical gap): PROVEN-HERE.** For A ∈ H_0, inf_{λ∈Λ_res}||A + dλ||² ≤ 3.5·10⁶(||dA||² + ||QA||²).
      Hence, uniformly in n (odd ≥ 3) and T ≥ 2:
      - **||dA||² + κ||QA||² ≥ c_PG||A||² on Phys, with c_PG := min(1, κ)/(3.5·10⁶);**
      - **O_FP ≥ min(c_PG, 4) on H_0**, by Lemma FP-ab's decomposition with the Poincaré constant 4.
      *Proof.* Let A ∈ H_0.
      - (1) By L3g(a)-glob applied to the co-closed A_c, ||A_c||² ≤ 5||dA||² + 2||Q_strA_c||².
      - (2) On H_0, QA = Q_strA = Q_strA_c + d_cMψ. Put G := QA - (Q_strA_c - F(A_c)) = F(A_c) + d_cMψ.
        - The two terms of G are orthogonal on the coarse torus, since d_c^*F(A_c) = 0 by PG-flux (a).
        - By PG-flux (b) and ||∇A_c||² = ||dA||², ||G|| ≤ ||QA|| + 2||dA||, so ||F(A_c)||, ||d_cMψ|| ≤ ||QA|| + 2||dA||.
      - (3) Hence ||Q_strA_c|| ≤ ||QA|| + 4||dA||, and ||A_c||² ≤ 69||dA||² + 4||QA||².
      - (4) By PG-orbit, PG-ext and PG-line (r - m = h(A_c)), and with ||d_cm||² ≤ 2||QA||² + 8||dA||² and ε ≤ 1/3:
        inf ≤ ||A_c||²(1 + 1280/9) + 4.25·10⁵(2||QA||² + 8||dA||²) + 427C_3||dA||² ≤ 3.5·10⁶(||dA||² + ||QA||²). ∎
      - What beats the three failure modes:
        - (PG-F1): the root components cost only the point capacity, 8ε², not the n² of the naive ||d*A||² route.
        - (PG-F2): the coarse co-closed part is controlled through the face fluxes F, which are exactly co-closed, so no
          torus Poincaré constant enters.
        - (PG-F3): the line trace of h loses ε^{-1}, and the capacity's ε² absorbs it.
      - The constant is crude. c24 measured λ_min(O_FP) = 0.27-0.43.
    - **Check c27** (criteria checks/c27_criteria.md before the script; disclosures in checks/c27_time.txt).
      - E1, E2, E4, E5, E6 PASS:
        - d_c^*F(A_c) ≤ 9e-14;
        - the PG-flux (b) ratio ≤ 0.013;
        - C_3(n) ≤ 0.683 for n ≤ 24 (the bound 14 is crude);
        - b_n/(π/2)⁴ ≤ 0.91, C_β/163 ≤ 0.49, ||dγ||²/(20ε²) ≤ 0.42, ||dφ̃||²/(22||d_cm||²) ≤ 0.02;
        - the line-trace ratio ≤ 6e-4.
      - **E3 FAILED as pre-registered.** The orbit identity holds to ≤ 7e-15. But the sub-check "r - m = h(A_c)" was
        normalised by max|r - m|, which is ~1e-16 for the pure-gauge test vector (there r = m). The post-run absolute
        errors are ≤ 1.1e-15 (disclosed). The criterion is not edited.
      - I1: the largest tested inf_orbit/(||dA||² + ||QA||²) is 2.80.
      - 15 s, 350 MB.
    - **N4 status [S12].** The abelian, linearised, one-level gauge fixing is complete:
      - the legitimate fixing (FP-ab), and the uniform gap of O_FP on H_0 (Proposition PG), uniform in n and T.
      The L3g(a)-slice completion stays OPEN for:
      - (NA), the SU(N) background version;
      - (IT'), the gap on the slice of the composite root map. The composite slice functional obeys
        h^{(m+1)} = Mh^{(m)} + hQ_root^{(m)}. PG-line was proven for the direct S4' funnel only. IT-str settles the
        straight part.
      N5 now needs (NA), (IT'), the ℓ¹ covariance bound and the random-walk expansion. It no longer needs N2's linear
      half or the abelian gap as one-level inputs. [R1112-fix] Keep the objects separate: N2 concerns the chain-response
      kernels (B_k ↦ r, f_0); N5 concerns the covariance of the actual soft Hessian (the inverse of the fluctuation
      operator). N5's ℓ¹ covariance bound and random-walk expansion are still fully OPEN, and the N2 kernel results
      do not supply them.
  - **B-NA (RTARGET §22): not attempted in session 12.** It remains as stated in L5 [S10]/[S11].
- **[S13] Session 13: exponential locality of the linearised soft chain (N2-exp); the composite slice (IT'). Targets
  pre-stated in RTARGET.md §24-25, after the lead's exploratory reasoning (on paper) and before any written session-13
  derivation or script. The c28 criteria were written before the script (one pre-script addendum, disclosed). Status
  of L5 unchanged: IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE (both unreviewed):
  - Theorem N2-exp, with Lemmas EXP-id, EXP-real, EXP-strip and Corollary N2-exp-b counted with it;
  - Proposition PG^{(k)}, with Lemma IT-line counted with it.
  Check c28: A (identities) VALID; B FAILED as pre-registered on a floating-point tie at the sharp point p = 0 (all other
  sub-checks hold with margin); C: C1, C2 PASS, C3 and C4 FAILED as pre-registered (a pre-asymptotic fit window);
  D PASS.
  - **N2-exp (RTARGET §24).** Setting and notation of LED-dual and LED-symb (d = 4, L ≥ 3 odd, n = L^k ≥ 3,
    κ_- ≤ κ_i ≤ κ_+, κ := κ_{k-1}, κ̂ := κ_+/κ_-). Work on the cube Q := [-π, π]⁴ and its complex neighbourhoods
    S_η(Q) := {z = x + iy : x ∈ Q, |y_α| ≤ η}; the K = 0 alias is θ = z itself. The building blocks, each the analytic
    continuation of its real form:
    - δ(w) := D_n(w)D̄_n(w) = Σ_{|l|<n}(n - |l|)n^{-2}e^{-iwl/n} (entire; = |D_n(w)|² on R), D̄_n(w) := n^{-1}Σ_{j<n}e^{iwj/n};
    - φ_α(w) := 2n²(1 - cos(w/n)) (entire), φ := Σ_αφ_α; Δ_α(w) := 2(1 - cos w) = ν_αν̄_α with ν̄_α := e^{-iz_α} - 1;
    - the identity **Δ_α = φ_αδ_α** (entire functions; it holds on R since |D_n(θ)|² = 4sin²(θ/2)/(4n²sin²(θ/2n)));
    - a := κΠ_αδ_α; A_μ := Σ_{m=0}^{k-1}(κ/κ_{k-1-m})S_{L^m}(z_μ), with S_s(w) := s^{-1}Σ_{r<s}(t_r² + t_{r+s}² +
      2t_rt_{r+s}cos w), t := the tent (uniform ∗ uniform) on {0..2s-2}, so t_r + t_{r+s} = 1/s and S_1 ≡ 1;
    - Z_μ := Σ_{K≠0}Π_αδ(z_α + 2πK_α)·δ(z_μ + 2πK_μ)/φ^{(K)}(z), φ^{(K)}(z) := Σ_αφ_α(z_α + 2πK_α),
      K_α ∈ {-(n-1)/2, …, (n-1)/2} (a finite sum);
    - R_μ := A_μ + κZ_μ, **β_μ := aδ_μ + φR_μ**, **Ψ := 1 - Σ_μφ_μR_μ/β_μ**, **Σ := Σ_μΔ_μ/β_μ**.
    - **Lemma EXP-id (exact form of the symbols): PROVEN-HERE.** On Q ∖ {0}: P̂_μ = β_μ/φ, D = φΣ, and aΣ = φΨ
      identically. Hence, for the entries ν ≠ μ (F̂_{νμ} ↦ r̂_μ),
        **𝓡̂_{μ,(νμ)} = -aν̄_ν/(β_μβ_νΨ) = -φν̄_ν/(β_μβ_νΣ)**,
      and on closed data F = db the B_k-symbols are
        **r̂_σ = -φb̂_σ/β_σ + ν_σ·(a/(β_σΨ))Σ_νν̄_νb̂_ν/β_ν,**
      and the K = 0 alias term of f_0 (Lemma LED-symb) is
        **κe^{ip·u/n}{ΠD·[ν^{(n)}_ρD_σb̂_σ/β_σ - ν^{(n)}_σD_ρb̂_ρ/β_ρ] + (ΠD/Ψ)ν^{(n)}_ρν^{(n)}_σ(R_σ/β_σ - R_ρ/β_ρ)Σ_νν̄_νb̂_ν/β_ν},**
      with ΠD := Π_αD_n(p_α). In each formula every factor is analytic near p = 0: **the 1/φ of the fine Green's
      function cancels exactly.**
      *Proof.*
      - P̂_μ: the K = 0 alias of the G-term is κ|W_{n,μ}(p)|²/φ(p) = κΠ_αδ_α·δ_μ/φ = aδ_μ/φ; the K ≠ 0 aliases are κZ_μ;
        the m-sum is A_μ (S_symbol(s) = s^{-2}Σ_K|D_s(θ_K)|⁴ = s^{-1}Σ_r|t_r + t_{r+s}e^{-ip}|² by Parseval on Z/s, and
        Σ_K|D_s(θ_K)|² = 1). So P̂_μ = (aδ_μ + φR_μ)/φ.
      - D = Σ_νΔ_νP̂_ν^{-1} = φΣ. aΣ = Σ_μaφ_μδ_μ/β_μ = Σ_μφ_μ(β_μ - φR_μ)/β_μ = φΨ, using Δ_μ = φ_μδ_μ.
      - 𝓡̂ = -P̂_μ^{-1}P̂_ν^{-1}ν̄_ν/D (LED-symb) = -φν̄_ν/(β_μβ_νΣ) = -aν̄_ν/(β_μβ_νΨ).
      - r̂ on closed data: r̂_σ = -P̂_σ^{-1}(b̂_σ - ν_σt) with t := Σ_νP̂_ν^{-1}ν̄_νb̂_ν/D (c26 r_from_b, equivalent to
        LED-symb's formula when F = db); substitute P̂^{-1} = φ/β and D = φ²Ψ/a.
      - f_0, K = 0: insert r̂_σ = -(φ/β_σ)(b̂_σ - ν_σt) into -κe^{ip·u/n}[ν^{(n)}_ρW_σr̂_σ - ν^{(n)}_σW_ρr̂_ρ]/φ. The b̂ part
        loses its 1/φ at once. The t part carries t = (a/(φΨ))Σν̄b̂/β, so it needs the bracket
        [ν^{(n)}_ρW_σν_σ/β_σ - (ρ ↔ σ)] to be divisible by φ. With 1/β_σ = 1/(aδ_σ) - φR_σ/(aδ_σβ_σ) and
        ν_σD_σ/δ_σ = ν_σ/D̄_σ = ν^{(n)}_σ (D̄_n(p) = (1 - e^{ip})/(n(1 - e^{ip/n}))), the bracket equals
        ΠD·[ν^{(n)}_ρν^{(n)}_σ - ν^{(n)}_σν^{(n)}_ρ]/a - (φ/a)ΠD·ν^{(n)}_ρν^{(n)}_σ(R_σ/β_σ - R_ρ/β_ρ); the first term is 0. ∎
      - The K ≠ 0 alias terms of f_0 are (finite sums of terms analytic in the strip below)·r̂.
      - c28 A: all four formulas reproduce c26's symbols (built independently from c26's Laplace G) to ≤ 2.2e-13 on 12
        (T, k, κ) cases (d = 4, k ≤ 3, including non-constant κ_i). At p = 0 the analytic values are finite
        (Ψ(0) = 1, β_μ(0) = κ).
    - **Lemma EXP-real (real-axis bounds on Q): PROVEN-HERE.** For x ∈ Q:
      - (R1) 1 ≥ δ(x_α) ≥ max(4/π², 1 - x_α²/12); (R2) (4/π²)x_α² ≤ φ_α(x), Δ_α(x) ≤ x_α², |sin x_α| ≤ √Δ_α;
      - (R3) 1 ≤ A_μ ≤ 1 + κ̂/(L² - 1); 0 ≤ Z_μ ≤ 1/9; so 1 ≤ R_μ ≤ R̄ := 1 + κ̂/(L² - 1) + κ/9;
      - (R4) β_μ ≥ b_* := min(κ, 24/π²), β_μ ≥ φ, and β_μ ≤ Γβ_ν with Γ := max(π²/4, R̄);
      - (R5) for |x| ≤ r_0 < √6: Ψ(x) ≥ Ψ_U := κ(1 - r_0²/6)/(κ + r_0²R̄); (R6) ψ(x) := Σ_μΔ_μ ≥ (4/π²)|x|².
      *Proof.*
      - (R1): |D_n(x)|² = sin²(x/2)/(n²sin²(x/2n)) ≥ sinc²(x/2), and sinc²s ≥ max(1 - s²/3, 4/π²) on |s| ≤ π/2.
      - (R3): S_s(0) = s^{-1}Σ_r(t_r + t_{r+s})² = s^{-2} and S_s ≥ 0, so the m ≥ 1 terms sum to ≤ κ̂Σ_{m≥1}L^{-2m}.
        For K ≠ 0 some |θ_α| ∈ [π, πn], so φ^{(K)}(x) ≥ 4n²sin²(π/2n) ≥ 9 (n ≥ 3); and Σ_KΠ_αδ(x_α + 2πK_α) = 1 by
        Parseval on Z/n, with δ_μ ≤ 1.
      - (R4): aδ_μ ≥ κΠ(1 - u_i) ≥ κ(1 - (|x|² + x_μ²)/12) ≥ κ(1 - |x|²/6) and φ ≥ (4/π²)|x|²; the minimum of
        κ(1 - t/6) + (4/π²)t over t ∈ [0, 6] is min(κ, 24/π²), and for t ≥ 6, φ ≥ 24/π². Γ: aδ_μ ≤ a ≤ (π²/4)aδ_ν and
        φR_μ ≤ R̄φR_ν.
      - (R5): on R, Ψ = Σ_μ(φ_μ/φ)·aδ_μ/β_μ (by EXP-id), a convex combination; aδ_μ/β_μ = 1/(1 + φR_μ/(aδ_μ)) and
        aδ_μ ≥ κ(1 - r_0²/6), φ ≤ r_0². (Ψ(0) = 1.) ∎
    - **Lemma EXP-strip (complex perturbation bounds): PROVEN-HERE.** Let z = x + iy ∈ S_η(Q), η ≤ 0.1,
      ε := e^η - 1, ε' := (π²/4)ε. Then:
      - (P1) |δ(z_α) - δ(x_α)| ≤ ε and |δ(z_α)| ≤ e^η; hence |aδ_μ(z)/aδ_μ(x) - 1| ≤ e_5 := (1 + ε')⁵ - 1;
      - (P2) |φ_α(z) - φ_α(x)| ≤ (η² + 2η√φ_α(x))cosh η, and the same for Δ_α with √Δ_α;
      - (P3) |A_μ(z) - A_μ(x)| ≤ κ̂ε/(L² - 1);
      - (P4) |Z_μ(z) - Z_μ(x)| ≤ c_Z := [εe^{4η} + 4e^{3η}ε(1 + e^η)]/(9λ) + e_Z/(9λ), λ := 1 - 4η²cosh²η/9,
        e_Z := (4η²/9 + 4η/3)cosh η; so |R_μ(z) - R_μ(x)| ≤ e_R := κ̂ε/(L² - 1) + κc_Z;
      - (P5) |β_μ(z) - β_μ(x)| ≤ ρ_β β_μ(x), ρ_β := e_5 + (4η²/b_* + 4η/√b_*)cosh η·(R̄ + e_R) + e_R;
      - (P6) for |x| ≤ r_0: |Ψ(z) - Ψ(x)| ≤ e_Ψ := [(4η² + 4ηr_0)cosh η(R̄ + e_R) + r_0²e_R]/((1 - ρ_β)b_*) +
        ρ_β/(1 - ρ_β);
      - (P7) for |x| ≥ r_0: Re Σ(z) ≥ (ψ(x)/min_μβ_μ(x))·br_V, br_V := 1/((1 + ρ_β)Γ) - (4η²/ψ_0 + 4η/√ψ_0)cosh η/(1 - ρ_β),
        ψ_0 := 4r_0²/π².
      *Proof.*
      - (P1): δ(z) - δ(x) = Σ_lw_le^{-ixl/n}(e^{yl/n} - 1) with w_l ≥ 0, Σw_l = 1, |l/n| < 1. |δ(z)| ≤ |D_n(z)||D̄_n(z)| ≤
        e^{|y|}·1. The ratio bound uses δ(x) ≥ 4/π² for each of the five factors.
      - (P2): φ_α(z) - φ_α(x) = 2n²[cos a(1 - cosh b) + i sin a sinh b] (a = x/n, b = y/n), with |sin a| ≤ 2|sin(a/2)| =
        √φ_α/n, cosh s - 1 ≤ (s²/2)cosh s and sinh s ≤ s cosh s.
      - (P3): each m-term is α_s + β_scos z_μ with 0 ≤ β_s ≤ S_s(0) = L^{-2m}, and |cos z - cos x| ≤ ε.
      - (P4): Parseval on Z/n for the shifted sequences gives, for each direction, Σ_{K_α}|δ(z_α + 2πK_α)| ≤ e^η and
        Σ_{K_α}|δ(z_α + 2πK_α) - δ(x_α + 2πK_α)| ≤ ε(1 + e^η) (write δ = DD̄ and use Cauchy-Schwarz with
        Σ_K|D(z_K) - D(x_K)|² = n^{-1}Σ_j(e^{yj/n} - 1)² ≤ ε²). Telescoping the five-factor products gives
        Σ_K|N_K(z) - N_K(x)| ≤ εe^{4η} + 4e^{3η}ε(1 + e^η). For K ≠ 0, Re sin²(a + ib) ≥ sin²a - sinh²b gives
        |φ^{(K)}(z)| ≥ φ^{(K)}(x) - 4η²cosh²η ≥ λφ^{(K)}(x) (φ^{(K)}(x) ≥ 9), and (P2) for each alias gives
        |Δφ^{(K)}|/φ^{(K)}(x) ≤ e_Z. Finally Σ_KN_K(x)/φ^{(K)}(x) = Z_μ(x) ≤ 1/9.
      - (P5): Δβ = Δ(aδ_μ) + Δφ·R(z) + φ(x)ΔR; divide by β ≥ max(b_*, φ, aδ_μ) and use √φ/max(b_*, φ) ≤ 1/√b_*.
      - (P6): Ψ = 1 - Σq_μ, q_μ := φ_μR_μ/β_μ; |q_μ(z) - q_μ(x)| ≤ |Δ(φ_μR_μ)|/|β_μ(z)| + q_μ(x)ρ_β/(1 - ρ_β), with
        Σ_μq_μ(x) ≤ 1, Σ_μ√φ_μ ≤ 2√φ ≤ 2r_0 and |β_μ(z)| ≥ (1 - ρ_β)b_*.
      - (P7): Δ_μ(z)/β_μ(z) = (Δ_μ(x) + e_μ)/(β_μ(x)(1 + f_μ)), |f_μ| ≤ ρ_β, |e_μ| ≤ (η² + 2η√Δ_μ)cosh η; Re(1/(1 + f)) ≥
        1/(1 + ρ_β) on the disc |f| ≤ ρ_β < 1; β_μ ≤ Γmin_νβ_ν; Σ_μ√Δ_μ ≤ 2√ψ; ψ ≥ ψ_0 by (R6). ∎
    - **Theorem N2-exp (exponential locality of the linearised soft chain): PROVEN-HERE.** Define η_*(κ, κ̂, L) as
      the largest η ≤ 0.1 for which, for some r_0 ∈ (0, √6), ρ_β ≤ ½, e_Ψ ≤ Ψ_U/2, br_V ≥ ½/((1 + ρ_β)Γ) and
      [R1314-fix: the f_0 condition, used in the proof below, is now part of the definition] (4η²/ψ_0 + 4η/√ψ_0)cosh η ≤ 0.15, and put
      **m_* := min_{κ∈[κ_-, κ_+]} η_*(κ, κ̂, L) > 0.** Then, uniformly in k ≥ 1, T and the fine offset u:
      - (i) 𝓡̂ (F ↦ r, on ALL 2-forms F), and the B_k-symbols B_k ↦ r and B_k ↦ f_0, extend analytically to the strip
        {|Im p_α| < m_*} and are bounded there by a constant M = M(L, κ_±);
      - (ii) hence every entry of the infinite-lattice kernels obeys **|K(X)| ≤ M e^{-m'|X|_1} for every m' < m_***, and
        the torus kernels are their periodisations (|K_T(X)| ≤ M'Σ_{j∈Z⁴}e^{-m'|X + Tj|_1}).
      - Values (L = 3, κ_i ≡ κ, so κ̂ = 1) [R1314-fix: valid (η, r_0) pairs; the session-13 pairs had η rounded up past
        the bisection value for the printed r_0]: η_* = 0.0111 (κ = 1, r_0 = 0.57), 0.0077 (κ = 0.25, r_0 = 0.37), 0.0117
        (κ = 4, r_0 = 0.65). With κ̂ = 16: 0.0037 (κ = 0.25, r_0 = 0.25), 0.0082 (κ = 4, r_0 = 0.60) (was 0.0083, which
        exceeds the bisection value 0.00826). Every condition, including the f_0 one, holds at each pair in 30-digit
        arithmetic (c30 A). The constant is crude (see c28 C).
      *Proof.*
      - By EXP-strip, for η ≤ η_* and z ∈ S_η(Q): |β_μ(z)| ≥ ½β_μ(x) > 0; Ψ(z) ≠ 0 where |x| ≤ r_0, since
        |Ψ(z)| ≥ Ψ_U - e_Ψ ≥ Ψ_U/2; Re Σ(z) > 0 where |x| ≥ r_0. Every building block is analytic on S_η(Q) (finite
        sums of entire functions; φ^{(K)}(z) ≠ 0 for K ≠ 0 by (P4)).
      - Define g := -aν̄_ν/(β_μβ_νΨ) where Ψ ≠ 0 and g := -φν̄_ν/(β_μβ_νΣ) where Σ ≠ 0. The two agree where both are
        defined, since aΣ = φΨ (EXP-id). So g is analytic on S_η(Q), and g = 𝓡̂ on Q ∖ {0}; at p = 0 both are 0
        (ν̄(0) = 0, and r̂(0) = 0 by LED-symb).
      - Periodicity [R1314-fix: replaces the session-13 gluing sentence, which did not prove a gluing]: each alias
        term is 2πn-periodic in each variable and the K-sum runs over the residues mod n, so P̂_μ, D and 𝓡̂ (built from
        the full alias sums, LED-symb) are 2π-periodic meromorphic functions on C⁴. g = 𝓡̂ on S_η(Q) off a null set
        (the zero set of a denominator), and g is bounded there; so 𝓡̂ is locally bounded on the strip {|Im p_α| ≤ η}
        (cover it by 2π-translates of S_η(Q)), and a locally bounded meromorphic function is analytic (Riemann
        extension). Hence g continues to the full strip and is 2π-periodic. The same holds for the f_0 symbols, since
        e^{i(p + 2πK)·u/n} is n-periodic in K for integer u.
      - Where |x| ≥ r_0 the f_0 formula of LED-symb (with its 1/φ) is used directly: |φ(z) - φ(x)| ≤
        (4η²/φ + 4η/√φ)cosh η·φ(x) ≤ 0.15φ(x) by the definition of η_* (φ(x) ≥ 4r_0²/π²), so φ(z) ≠ 0 there.
      - The same argument applies to the B_k-symbols, which (EXP-id) are built from the same blocks, from ΠD, D_σ, ν^{(n)}
        (entire), and, for f_0, from the K ≠ 0 alias terms e^{iθ_K·u/n}ν^{(n)}_ρW_σ(θ_K)/φ^{(K)}: these are finite sums,
        analytic on the strip, and bounded uniformly in n and u by e^{cη} times the real-axis majorant of LED-unif (2)
        (|D_n(w)| ≤ e^η min(1, π/|Re w|) on |Re w| ≤ πn, |e^{iθ_K·u/n}| ≤ e^{4η}).
      - Uniform bound M: on S_η(Q), |a| ≤ κe^{4η}, |ν̄| ≤ 2 + ε, |β_μ| ≥ b_*/2, |Ψ| ≥ Ψ_U/2 (near 0), and near |x| ≥ r_0,
        with β_0 := min_νβ_ν(x) ≥ max(φ(x), b_*): |φ(z)|/(|β_μβ_ν||Σ(z)|) ≤ 4(φ(x) + |Δφ|)/(β_0ψ_0br_V) ≤
        4(1 + |Δφ|/b_*)/(ψ_0br_V). These depend only on (L, κ_±).
      - Paley-Wiener (periodic form): for h analytic and bounded by M on {|Im p_α| ≤ m'}, shifting each p_α-contour by
        +i·m'·sign(X_α) (convention K(X) = (2π)^{-4}∫e^{ip·X}ĥ) gives |ȟ(X)| ≤ Me^{-m'|X|_1}. The torus kernel is the periodisation (Poisson; LED-unif). ∎
    - **Corollary N2-exp-b (which kernel is exponential).**
      - **Exponential (proven):** 𝓡 (F ↦ r_{k-1}) on all 2-forms, with no closed-data restriction; the B_k-kernels
        B_k ↦ r_{k-1} and B_k ↦ f_0 (each fine offset u); by J-str (c), also B_k ↦ r_i and B_k ↦ J^c_0.
      - **Power tail (not exponential):** the unrestricted extension of the f_0 map to all 2-forms, F ↦ 𝒦̂_uF̂, contains
        the degree-0 projector Π_ex (LED-unif, failure mode LED-F2; a |x|^{-4} tail). The session-12 F-representative
        𝒦̂_u + Π_coex is not shown exponential: its (1 - e^{ip·u/n})Π_coex term is non-analytic at p = 0 for u ≠ 0;
        c28 C5 sees a power-law tail (log-log slope ≈ 5.6-6.0 at u = (1, 0, 0, 0)). Whether some other F-representative
        of f_0 is exponential is not decided here (a local analytic representative exists by the Koszul exactness of
        the lattice de Rham complex at p = 0; a global one is not constructed).
      - **What N6 consumes [R1314-fix: ARGUED, not proven].** N6 bounds the activities as functions of the RG field variable, the coarse field B_k
        (V_k), and their analyticity in it; the background enters through the minimiser's dependence on B_k. So N6
        consumes the B_k-kernels, which are exponential with rate m_*, together with the sup bounds of Theorem N2-lin
        in terms of dB_k (gauge invariance). The F-kernel of r is also exponential. The non-exponential F-representatives
        of f_0 are not needed. [R1314-fix] This is an argument, not a proof: exponential decay in the gauge-variant B_k
        plus sup bounds in dB_k is not exponential locality in the curvature. To make it a statement N6 can use, one of
        the following is needed:
        - **Lemma F-df_0 [S16: PROVEN-HERE, L5 [S16], in the form of the parenthesis below: an exponentially local
          extension of F ↦ f_0 to ALL 2-forms; the dΠ_ex route sketched here is not used] (was OPEN):** the map F ↦ df_0 (the fine CURVATURE response, as a function of the coarse
          curvature F on ALL 2-forms) has an exponentially decaying kernel, uniformly in k, T, u (plausible: dΠ_ex = 0 on
          1-forms removes the degree-0 term, and d(1 - e^{ip·u/n})Π_coex = (1 - e^{ip·u/n})d is analytic); with r done
          (𝓡 on all F, proven), this gives exponential F-kernels for both gauge-invariant outputs N6 uses;
        - or a localisation lemma (local axial gauge plus cut-off), stated in L5 [S14] only as argued.
      - **How the rate enters N6.** In M-block units the kernel rate is m_*M. Theorem CE needs κ > 3κ_0 + 3 ≈ 457 in
        M-units, so the linear response alone permits it only for M ≳ 457/m_* (≈ 4·10⁴ with the proven m_* at κ = 1;
        ≈ 470 with the located singularity m ≈ 0.98). This is a necessary input, not N6 itself: N6 also needs N5 and the
        non-linear chain.
    - **Check c28** (criteria checks/c28_criteria.md, with a pre-script addendum; disclosures in checks/c28_time.txt).
      - **Part A: VALID.** EXP-id's four formulas match c26 to ≤ 2.2e-13 (12 cases). Z by an independent Laplace
        quadrature matches exact alias sums to 1.4e-15.
      - **Part B: FAILED as pre-registered, on one sub-check.** At 9 (κ, n) cases (κ = 1, 0.25, 4; n = 3, 9, 27; complex
        points with |y_α| ≤ η_*, including |y_α| = η_*), every perturbation bound holds with margin: |ΔZ|/c_Z ≤ 0.052,
        |Δβ|/(ρ_ββ) ≤ 0.13, |ΔΨ|/e_Ψ ≤ 0.06, Re Σ/(lower bound) ≥ 5.6, β_μ/β_ν ≤ 0.5Γ. The failing sub-check is
        "β_μ(x) ≥ b_*" at n = 27, κ ∈ {1, 0.25}: at the pre-registered point x = 0 the bound is sharp (β_μ(0) = κ = b_*
        exactly), and float rounding gives β_μ(0)/b_* - 1 = -5.6e-16 (post-run diagnostic). The criterion is not edited.
      - **Part C (κ = 1, axis profiles).** C1 PASS: every fitted rate (1.26-1.71 per coarse unit) is ≥ m_* = 0.0111 [R1314-fix: a consistency check only; any
        positive rate passes].
        C2 PASS: k-stable within 1.10. **C3 and C4 FAILED as pre-registered.** The fit window x ∈ [3, T/2 - 2] is
        pre-asymptotic: the local rate falls from ≈ 2.0 (x = 1) towards its limit, so the fitted rate drifts with T
        (𝓡: 1.60, 1.43, 1.33 at T = 16, 24, 32, k = 1), and at T = 32 it is 1.28 times the nearest complex zero of
        Den := Ψ·Πβ, Im w = 1.0365 at p = (iw, 0, 0, 0) (k = 1). Post-run, informational: a three-parameter fit
        log K = c - mx - αlog x on the reviewer's T = 32 profile gives m ≈ 0.93-0.97 (α ≈ 2.6-2.9) at k = 1 and
        0.88-0.93 at k = 3 [R1314-fix: ranges now include all six fits, 0.950, 0.972, 0.934 and 0.906, 0.930, 0.884], against the located zeros Im w = 1.036, 0.987, 0.982 (k = 1, 2, 3). The located zero
        scales like √κ: 0.50, 0.48 (κ = 0.25) and 2.46, 2.37 (κ = 4), for k = 1, 2. So the located rate (numerical, not proven) [R1314-fix] is ≈ √(κ/R_ν(0)),
        the "mass" of the soft constraint, about 90 times the proven m_*.
      - C5 (informational): the f_0 B_k-kernel decays at fitted rates 1.26-1.40 (u = 0 and u = (1, 0, 0, 0), k = 1, 2);
        the representative 𝒦̂_u + Π_coex (u = (1, 0, 0, 0)) flattens to a power tail (log-log slope 5.6-6.0; a power
        law fits better than an exponential).
      - Timings: A 2 s, B 4 s, C 21 s, D 2 s; peak RSS 0.66 GB (C; peak footprint 1.2 GB).
    - **N2 status [S13].** The linearised soft chain is now fully local: (H1), (H2), (LED) in sup form (N2-lin) and
      exponential decay of the B_k-response with a k- and T-uniform rate (N2-exp). For the linear maps, "complex data"
      adds nothing (they are complex-linear). **N2 stays OPEN** for the SU(N) chain (B-NA (i)-(iii), the SU(N)
      analogues of N2-E, N2-lin and N2-exp) and for the non-linear (small-curvature) analytic dependence that N10 needs.
      **Decision 4 is not affected adversely:** failure mode EXP-F1 does not occur; the soft kernel's response is
      exponentially local.
  - **IT' (RTARGET §25): the composite slice.** One linearised abelian soft step whose averaging is the k-fold composite
    Q^{(k)} := Q_root ∘ … ∘ Q_root (fine spacing ε = L^{-k}, n = L^k), Q^{(m)} = Q_str^{(L^m)} - dh^{(m)},
    h^{(m+1)} = Mh^{(m)} + hQ^{(m)} (L3g(a)-slice, IT-str). Lattice units: a_b := ∫_bA (so ||A||²_B = ε²Σ_{b⊂B}a_b²).
    - **Lemma IT-line (the composite slice functional): PROVEN-HERE.**
      - (a) h^{(k)}(dλ) = Mλ - λ(c_X), with c_X the fine centre of B(X) (nested centres coincide, L odd).
      - (b) Unrolled form: h^{(m+1)}(A)(X) = h^{(m)}(A)(Y_c(X)) + avg_{σ, Y∈B(X)}∫_{P^σ(Y_c→Y)}Q_str^{(L^m)}A, with Y_c(X)
        the central level-m site of B(X); so h^{(k)}(X) = Σ_{m=0}^{k-1}H_m(X), H_m the level-m funnel term inside the
        central level-(m+1) block Z_{m+1} ⊂ B(X).
      - (c) **|h^{(k)}(A)(X)|² ≤ (4L²/(L - 1))Σ_{b⊂B(X)}a_b²**, i.e. ε²|h^{(k)}(X)|² ≤ (4L²/(L - 1))||A||²_{B(X)},
        uniformly in k. No gradient term and no ε^{-1} trace loss (compare PG-line).
      *Proof.*
      - (a) Induction: h^{(m+1)}(dλ) = M(M^{(m)}λ - ev^{(m)}λ) + h(d ev^{(m)}λ) = M^{(m+1)}λ - ev^{(m+1)}λ, using
        Q^{(m)}d = d ev^{(m)} and h(dμ) = Mμ - ev μ.
      - (b) h(Q^{(m)}A)(X) = avg∫_PQ_str^{(L^m)}A - avg_Y[h^{(m)}(Y) - h^{(m)}(Y_c)], and avg_Yh^{(m)}(Y) = Mh^{(m)}(X).
      - (c) A level-m link value of Q_str^{(L^m)}A is V_l = L^{-4m}Σ_{y}Σ_{j<L^m}a(y + je_μ). Cauchy-Schwarz, with each
        fine bond of the slab B_m(Y) ∪ B_m(Y + e_μ) met by ≤ L^m pairs (y, j), gives |V_l|² ≤ L^{-2m}Σ_{slab}a².
        An axial path from Y_c to Y ∈ B(Z_{m+1}) has ≤ 2(L - 1) links, all internal to Z_{m+1}, and each fine μ-bond
        lies in ≤ 2 slabs of internal level-m μ-links. So |H_m|² ≤ avg_P|P|Σ_{l∈P}|V_l|² ≤ 4(L - 1)L^{-2m}Σ_{B(X)}a²,
        and |h^{(k)}| ≤ Σ_m|H_m| ≤ 2√(L - 1)·(L/(L - 1))(Σ_{B(X)}a²)^{1/2}. ∎
    - **Proposition PG^{(k)} (physical gap for the composite slice): PROVEN-HERE.** For A ∈ H_0^{(k)} := {h^{(k)} = 0},
      inf_{λ∈Λ_res}||A + dλ||² ≤ C_IT(L)(||dA||² + ||Q^{(k)}A||²), C_IT(L) := 3.4·10⁶ + 69 + 44160L²/(L - 1)
      (≤ 3.6·10⁶ at L = 3). Hence, uniformly in k ≥ 1 and T ≥ 2: **||dA||² + κ||Q^{(k)}A||² ≥ (min(1, κ)/C_IT)||A||² on
      Phys^{(k)}**, and the legitimate composite-slice operator obeys O_FP^{(k)} ≥ min(min(1, κ)/C_IT, 4) on H_0^{(k)}.
      *Proof.* The residual group is PG's Λ_res = {λ(c_X) = 0, Mλ = 0} by IT-line (a), and FP-ab applies verbatim
      (it uses only h^{(k)}(A + dλ) = h^{(k)}(A) + Mλ - λ(c)). On H_0^{(k)}, Q^{(k)} = Q_str^{(n)}, so PG steps (1)-(3)
      (L3g(a)-glob, PG-flux) hold unchanged: ||A_c||² ≤ 69||dA||² + 4||QA||². PG-orbit holds with r - m = h^{(k)}(A_c).
      PG-ext is unchanged. In step (4), IT-line (c) replaces PG-line: 160ε²Σ_X|r_X - m_X|² ≤ 160(4L²/(L - 1))||A_c||².
      So inf ≤ ||A_c||²(1 + 640L²/(L - 1)) + 4.25·10⁵(2||QA||² + 8||dA||²), and the coefficients are
      69(1 + 640L²/(L - 1)) + 3.4·10⁶ on ||dA||² and 4(1 + 640L²/(L - 1)) + 8.5·10⁵ on ||QA||². ∎
      - **(IT') is settled** for the abelian linearised step. The composite funnel is better behaved than the direct one:
        at each level the path integrals run over averaged fields, so the slice functional never concentrates on lines.
      - c28 D (d = 4, L = 3, k = 2, n = 9, coarse T = 2): D1 recursion = unrolled form to 1.6e-14; D2 h^{(2)}(dλ) =
        Mλ - λ(c) to 2.4e-14; D3 Q^{(1)}Q^{(1)} = Q_str^{(9)} - dh^{(2)} to 4.4e-16; D4 max ratio of IT-line (c) ≤ 1e-4
        (printed 0.0001) over 8 fields (the bound is crude). PASS.
    - **N4 status [S13].** The abelian linearised gauge fixing is complete for both the direct and the composite S4'
      slices (FP-ab, PG, PG^{(k)}). OPEN: (NA), the SU(N) background version.

- **[S14] Session 14: the SU(N) chain (B-NA reduced, not closed); (NA) for N4 (the covariant Faddeev-Popov identity
  PROVEN, the gap OPEN); a sharper m_* (×3.5). Targets pre-stated in RTARGET.md §27-31 at 17:32 UTC, after the
  lead's exploratory reasoning and two scratch arithmetic probes for target D (scratchpad, not checks), and before any
  written derivation or check script. The c29 criteria were written before the script. Status of L5 unchanged:
  IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE (all unreviewed): Lemma NA-alg; Proposition NA-FP (with Lemmas
  NA-inv and NA-crit counted with it); Lemma SRC-id. Strengthened (no count change): Theorem N2-exp' (Lemma
  EXP-strip'). Proposition B-NA-red is a proven implication whose hypotheses are OPEN; B-NA itself stays OPEN.
  Check c29: A PASS, B PASS, C VALID (C1 FAILED as pre-registered on a size threshold), D PASS.
  - **Lemma NA-alg (explicit su(N) algebra for the normalised soft kernel): PROVEN-HERE.** Norms are Hilbert-Schmidt,
    ||·|| is the operator norm, Π is the orthogonal projection (for Re tr(A*B)) onto su(N).
    - (a) *SU(N) maximiser of an average.* Let M = Σ_jw_je^{Y_j}, w_j ≥ 0, Σw_j = 1, Y_j ∈ su(N), |Y_j| ≤ y ≤ 1/20,
      Ȳ := Σw_jY_j. Then Re tr(W^{-1}M) has a unique maximiser W_0 over SU(N); W_0 = e^{X_0} with
      **|X_0 - Ȳ| ≤ 9.2y²**, and G := W_0^{-1}M = H + iθ·1 with H Hermitian, θ ∈ R, ||H|| ≤ 1, |θ| ≤ 1,
      **||H - 1|| ≤ 18.4y²**.
    - (b) *Soft density.* For V ∈ SU(N) with ρ := log(V^{-1}W_0) (principal) and **[R1314-fix] ||ρ||_op < 2π/N** (so the
      eigenvalue angles θ_j of ρ satisfy |Σθ_j| < 2π and Σθ_j ∈ 2πZ, hence tr ρ = 0; without it, e.g. N = 3 with all
      eigenvalues e^{2πi/3}, tr ρ ≠ 0 and a linear θ-term survives; in the intended small-|ρ| use it is automatic), the
      tree-level soft density
      φ := N^{-1}[Re tr(W_0^{-1}M) - Re tr(V^{-1}M)] satisfies
      **|φ - |ρ|²/(2N)| ≤ (9.2y²/N)|ρ|² + e^{|ρ|}|ρ|³/(3√N).**
      So the normalised kernel charges exactly |log(V^{-1}W_0)|²/(2N) up to relative errors O(y² + |ρ|): the |M̄|
      shrinkage (the contour variance) enters only at relative order y².
    *Proof.*
    - (a) *Stationarity.* Along W e^{tZ}, Z ∈ su(N), d/dt Re tr(e^{-tZ}W^{-1}M) = -Re tr(ZW^{-1}M), and Re tr(ZK) = 0
      for Hermitian K. So W = e^X is stationary iff Π(e^{-X}M) = 0.
    - *Fixed-point form.* Put E := Σw_j(e^{Y_j} - 1 - Y_j), |E| ≤ e^y - 1 - y ≤ 0.53y², and R_X := e^{-X} - 1 + X,
      |R_X| ≤ (|X|²/2)e^{|X|}. Then e^{-X}M = 1 + (Ȳ - X) + K(X), K(X) := R_X + E + (R_X - X)(Ȳ + E). Since Π(1) = 0
      and Ȳ - X ∈ su(N), stationarity is X = Φ(X) := Ȳ + Π(K(X)).
    - *Contraction on B := {|X| ≤ 3y}.* There |R_X| ≤ 4.5e^{0.15}y² ≤ 5.23y², and
      |(R_X - X)(Ȳ + E)| ≤ (3y + 5.23y²)(y + 0.53y²) ≤ 3.35y², so |K| ≤ 9.11y² ≤ 9.2y² and |Φ(X)| ≤ y + 9.2y² ≤ 3y. For X, X' ∈ B,
      |R_X - R_{X'}| ≤ (e^{3y} - 1)|X - X'| ≤ 3.24y|X - X'| and |(R_X - X - R_{X'} + X')(Ȳ + E)| ≤ (1 + 3.24y)(1.03y)|X - X'|,
      so Lip(Φ) ≤ 4.5y ≤ 0.23. Hence Φ has a unique fixed point X_0 ∈ B, and |X_0 - Ȳ| = |Π(K(X_0))| ≤ 9.2y².
    - *It is the global maximiser.* A global maximiser W_* exists (SU(N) compact) and is stationary. From
      Re tr(W_*^{-1}M) ≥ Re tr M and M = 1 + Δ_M, |Δ_M| ≤ e^y - 1 ≤ 1.03y: N - Re tr W_* ≤ |W_*^{-1} - 1||Δ_M|, and
      |W - 1|² = 2(N - Re tr W) for unitary W. So |W_* - 1| ≤ 2|Δ_M| ≤ 2.06y ≤ ½, and |log W_*| ≤ 4arcsin(¼)·2.06y ≤ 2.1y
      (A1-NA(1) step 1). So log W_* ∈ B and W_* = e^{X_0}.
    - *G.* Stationarity says that the anti-Hermitian part of G is a multiple of 1: G = H + iθ1. ||H||, |θ| ≤ ||G|| ≤
      ||M|| ≤ 1. ||H - 1|| ≤ ||G - 1|| ≤ |Ȳ - X_0| + |K(X_0)| ≤ 18.4y².
    - (b) V^{-1} = e^ρW_0^{-1}, so φ = N^{-1}Re tr((1 - e^ρ)G). Expand: Re tr(ρH) = 0 (ρ anti-Hermitian, H Hermitian);
      -½Re tr(ρ²H) = ½tr(ρ*ρH) = ½|ρ|² + ½tr(ρ*ρ(H - 1)), with |tr(ρ*ρ(H - 1))| ≤ ||H - 1|||ρ|²; tr ρ = 0 and tr ρ² is
      real, so the θ-part is θΣ_{m≥3}Im tr(ρ^m)/m! (tr ρ = 0 by the hypothesis ||ρ||_op < 2π/N); and |tr(ρ^mH)|, |tr ρ^m| ≤ √N|ρ|^m. Sum: the remainder is
      ≤ N^{-1}√N·2(e^{|ρ|} - 1 - |ρ| - |ρ|²/2) ≤ e^{|ρ|}|ρ|³/(3√N). ∎
    - Use: in Lie-algebra coordinates, every term of E_NA is an explicit function of local link variables, with the
      quadratic part of Setting SC and remainders bounded by (a)-(b), A1-NA(1) step 1 (BCH, 9s²) and step 3 (contours).
  - **Lemma NA-crit (gauge-fixed critical points): PROVEN-HERE (counted with NA-FP).** Let S be C¹ on a manifold 𝒳
    with a smooth group action, S invariant, and τ_x: 𝔤 → T_x𝒳 the infinitesimal action. Let Γ: 𝒳 → R^m be C¹ and x a
    critical point of S + ½|Γ|². If 𝔉_x := DΓ(x)∘τ_x: 𝔤 → R^m is onto, then Γ(x) = 0 and x is a critical point of S.
    *Proof.* Invariance gives dS(x)∘τ_x = 0. Criticality gives dS(x)[v] + ⟨Γ(x), DΓ(x)v⟩ = 0 for all v; with v = τ_xλ,
    ⟨Γ(x), 𝔉_xλ⟩ = 0 for all λ, so Γ(x) ⊥ Ran 𝔉_x = R^m. ∎ (This is the step that removes a Feynman-type gauge-fixing
    term from a background-field problem, given the Faddeev-Popov operator.)
  - **Lemma NA-inv (the Hessian at a critical background is gauge invariant): PROVEN-HERE (counted with NA-FP).**
    Setting: one soft step; fine configurations U, coarse V fixed; S(U) := S_W(U) + κΣ_cφ_c(V; M̄_c(U)) (or any C²
    functional invariant under 𝒢_V := {g : g(c_X) = 1 ∀X}). Left trivialisation U_b → e^{A_b}U_b; for b = (x → y),
    **(D_Uλ)_b := Ad(U_b)λ(y) - λ(x)**, so the orbit of e^{sλ} through U has tangent -D_Uλ. Λ := {λ : λ(c_X) = 0}. If U is a
    critical point of S, the Hessian H_U of A ↦ S(e^AU) at A = 0 satisfies **H_U(D_Uλ, ·) = 0 for every λ ∈ Λ.**
    *Proof.* f(A) := S(e^AU). The curve A(s) := log((e^{sλ}·U)U^{-1}) (componentwise) has A(0) = 0 and A'(0) = -D_Uλ, and
    every e^{A(s)}U = e^{sλ}·U is critical (S invariant), so df(A(s)) = 0 for all s. Differentiate at s = 0:
    d²f(0)(A'(0), ·) = 0. ∎ Off critical backgrounds the identity fails at the order of the gradient (NA-F1); c29 D3
    measures this.
  - **Proposition NA-FP (covariant Faddeev-Popov identity at an SU(N) critical background, at the Hessian (Gaussian)
    level): PROVEN-HERE.** [R1314-fix: scope. (iii) is an identity for the Gaussian integral at a critical background,
    invariant under the LINEAR action A ↦ A + D_Uλ. It is not the non-linear Faddeev-Popov identity, where the orbit is
    A ↦ log(e^{λ}·e^AU)U^{-1} and the determinant depends on A; Gribov copies are relevant at large fields.]
    Notation (one direct S4' step, any background U, V):
    - for an axial path P = (c = x_0 → x_1 → … → x_m = y) put T_j := U(x_0→x_1)⋯U(x_{j-1}→x_j), with U(x→x') := U_b for a
      forward link b = (x, x') and U_b^{-1} for a backward one, and
      **ℓ_P(A) := Σ_jAd(T_{j-1})ã_j, ã_j := A_b (forward), -Ad(U_b^{-1})A_b (backward)**;
    - **h_U(A)(X) := avg_{σ, y∈B(X)}ℓ_{P^σ(c_X→y)}(A)**, **M_Uλ(X) := avg_{σ,y}Ad(T^σ(c_X ← y))λ(y)** (T^σ the full
      transport along P^σ); at U = 1 these are L3g(a)-slice's h and the block mean M;
    - Λ_res^U := {λ ∈ Λ : M_Uλ = 0}, P_res^U its orthogonal projector, D_U^* the adjoint of D_U.
    Then:
    - (i) **h_U(D_Uλ) = M_Uλ - λ(c)** for every λ and every background (exact);
    - (ii) Γ := D_U|_Λ is injective, M_U: Λ → su(N)^{N_c} is onto, and χ_U := (h_U, P_res^UD_U^*) is admissible
      (χ_UΓ invertible) for EVERY background U;
    - (iii) if U is a critical point of S, then for every measurable F ≥ 0 invariant under A ↦ A + D_Uλ (λ ∈ Λ), with
      I(A) := F(A)e^{-½H_U(A,A)} and ∫_{(ΓΛ)^⊥}I < ∞,
        ∫I(A)δ(h_U(A))e^{-½||P_res^UD_U^*A||²}dA = FP_U·∫_{(ΓΛ)^⊥}I,  FP_U := (2π)^{m_2/2}|det χ_UΓ|^{-1}det(Γ^TΓ)^{1/2},
      a constant independent of A and F (m_2 = dim Λ_res^U).
    *Proof.*
    - (i) Along P, Ad(T_j)λ(x_j) - Ad(T_{j-1})λ(x_{j-1}) = Ad(T_{j-1})[Ad(U(x_{j-1}→x_j))λ(x_j) - λ(x_{j-1})], which is
      Ad(T_{j-1})(D_Uλ)_b for a forward link and -Ad(T_{j-1})Ad(U_b^{-1})(D_Uλ)_b for a backward one. So ℓ_P(D_Uλ) =
      Ad(T_P)λ(y) - λ(c) (telescoping). Average over (σ, y).
    - (ii) D_Uλ = 0 means λ(x) = Ad(U_b)λ(y) on every link, so λ is determined by its value at one site by parallel
      transport; λ(c_X) = 0 forces λ = 0. M_U is onto: for y = c_X + e_μ every P^σ(c_X → y) is the single link b, so
      M_U(vδ_y)(X) = |B|^{-1}Ad(U_b)v. Hence dim Λ_res^U = dim Λ - (N² - 1)N_c and the dimensions of χ_U's target and of Λ
      agree. If χ_U(D_Uλ) = 0 then M_Uλ = 0 by (i), so λ ∈ Λ_res^U, and ||D_Uλ||² = ⟨λ, P_res^UD_U^*D_Uλ⟩ = 0, so λ = 0.
    - (iii) By NA-inv, H_U(A + D_Uλ) = H_U(A), so I is invariant under the free linear action A ↦ A + Γλ. Lemma FP-ab
      applies verbatim with this Γ and χ = χ_U (linear). ∎
    - **What it settles and what it leaves.** The legitimate covariant fixing exists at every critical background,
      exactly as in the abelian case (FP-F3 does not occur). Two things are new and NOT settled:
      - the constant FP_U depends on the background (in the abelian case it does not): it is a Faddeev-Popov
        determinant, a function of V through U = U(V), which must be shown local and analytic in V (an N6/N10-type item);
      - the physical gap on Phys_U := {h_U = 0} ∩ (D_UΛ_res^U)^⊥ (the (NA) gap) is OPEN; see below.
    - *Composite slice.* With intermediate fields V^{(m)} := the S4' images of U and h^{(m+1)}_U := M_{V^{(m)}}h^{(m)}_U +
      h_{V^{(m)}}Q^{(m)}_U, the exact covariance W_0(M̄(g·U)) = g(c_X)W_0(M̄(U))g(c_Y)^{-1} linearises to
      Q^{(m)}_UD_U = D_{V^{(m)}}ev^{(m)}, and IT-line (a)'s induction gives h^{(k)}_U(D_Uλ) = M^{(k)}_Uλ - λ(c) with
      M^{(m+1)}_U := M_{V^{(m)}}M^{(m)}_U. Steps (ii)-(iii) are unchanged. So NA-FP holds for the composite slice too.
      **[R1314-fix] The two steps written out.**
      - *Linearised covariance (sign convention of NA-inv).* Q^{(m)}_U is the left-trivialised derivative,
        (Q^{(m)}_UA)_b := d/dt|_{t=0} log(V^{(m)}(e^{tA}U)_bV^{(m)}(U)_b^{-1}). Take g_s := e^{sλ} (any fine λ). By NA-inv,
        g_s·U = e^{A(s)}U with A(0) = 0, A'(0) = -D_Uλ. By the exact covariance, iterated over the levels (nested centres,
        L odd), V^{(m)}(g_s·U)_b = e^{sλ(c_x)}V^{(m)}_be^{-sλ(c_y)} for the level-m link b = (x → y), c_x the fine centre of
        x. So d/ds|_0 log(V^{(m)}(g_s·U)_bV^{(m)}_b^{-1}) = λ(c_x) - Ad(V^{(m)}_b)λ(c_y) = -(D_{V^{(m)}}ev^{(m)}λ)_b. The left
        side is Q^{(m)}_U(A'(0)) = -Q^{(m)}_UD_Uλ. Hence Q^{(m)}_UD_U = D_{V^{(m)}}ev^{(m)}, for every λ.
      - *Onto-ness of M^{(k)}_U: Λ → su(N)^{N_c}.* Write F_m for all su(N)-valued functions on the level-m sites. Claim:
        M^{(m)}_U(Λ) = F_m for 1 ≤ m ≤ k. For m = 1: each level-1 block contains L⁴ ≥ 81 fine sites and at most one coarse
        centre c_X; for y in the block of Y, not a coarse centre, vδ_y ∈ Λ,
        with M_U(vδ_y)(Y) = |B|^{-1}avg_σAd(T^σ(c_Y ← y))v and M_U(vδ_y)(Y') = 0 for Y' ≠ Y (disjoint blocks). Choose y := c_Y + e_1
        (adjacent to the level-1 centre; level-1 centres are L ≥ 3 apart, so it is no level-1, hence no coarse, centre): every P^σ(c_Y → y) is the single link, so
        M_U(vδ_y) = |B|^{-1}Ad(U_b)v·δ_Y, which is onto F_1 component by component. For m ≥ 1, M_{V^{(m)}}: F_m → F_{m+1}
        is onto by the same single-link argument (no constraint at level m), so M^{(m+1)}_U(Λ) = M_{V^{(m)}}(F_m) = F_{m+1}.
        At m = k this is onto su(N)^{N_c}. (The review's remark is correct: for the DIRECT composite, paths to a fine
        neighbour of c_X are not single links; the factorisation avoids that.) Then (ii)'s dimension count and χ_U
        injectivity go through verbatim with M^{(k)}_U, Λ_res^{U,(k)} := ker M^{(k)}_U ∩ Λ.
  - **(NA) gap: OPEN, with the obstruction located.** At a critical background the Hessian's soft part is κ|δρ_c|² +
    (terms with ρ_c and the |M̄| shrinkage, of relative size O(|ρ| + y²) by NA-alg). Write each contour transport as
    T_j = W_0e^{η_j} (|η_j| ≤ a ribbon flux, O(|f|) in coarse units). Linearising, δρ_c is the transported Q_U A minus
    **the defect Ad(W_0)·avg_j[(Ad(e^{η_j}) - 1)ℓ_{P_{Y,j}}(A)]**, a y-weighted average of individual funnel traces at the
    far root, with weights of size |f|. The slice h_U = 0 kills the unweighted average only. Individual root-axis line
    traces cost ε^{-1}||∇A||²_B (PG-line, sharp in 4D), and ||∇A||² is not controlled by the Hessian on Phys. So
    PG's orbit argument does not transfer by perturbation uniformly in n (failure mode NA-F2). Two routes are
    recorded, neither carried out:
    - (R1) enlarge the covariant slice by the weighted funnel moments that the defect contains (the residual group
      has (N² - 1)(n⁴ - 1) parameters per block, so 4(N² - 1) more conditions per block are available), then redo PG's
      orbit argument covariantly (PG-flux, PG-orbit, PG-ext, PG-line with Kato's inequality |∇|A|| ≤ |∇_UA|);
    - (R2) a smooth/rough split: the defect is relatively bounded on fields smooth at an intermediate scale, and rough
      fields pay ||dA||².
    The perturbative parts that do transfer uniformly: ||(D_U - d)λ|| ≤ 2√d·|a^c|_∞e^{2ε|a^c|}||λ|| in a global small-field
    gauge U = e^a (a^c := n·a, coarse units); and (argued, not written) the PG-orbit minimiser λ = φ - ψ obeys
    ||λ|| ≤ C||A|| uniformly in n (Neumann block Poincaré for ψ - φ̃, the bumps by ||d_cm||, the spikes have L² norm O(ε²)).
    c29 D checks (i) and NA-inv.
  - **Lemma SRC-id (fine sources enter the linearised chain as effective coarse data): PROVEN-HERE.** Setting SC with a
    fine source: critical points of E - ⟨j, B_0⟩, j a co-closed fine 1-form with zero mean (the gauge-orthogonality
    condition for a level-0 source). Then:
    - (i) J-str (a), (c) and the recursion r_{i-1} = (κ_i/κ_{i-1})Q^Tr_i hold unchanged; at level 0,
      **d*dB_0 = j - κ_0Q^Tr_0**, so dB_0 = dΔ^{-1}(j - κ_0Q^Tr_0);
    - (ii) **r_{k-1}(j; B_k) = r_{k-1}(0; B_k - Q^{(k)}Δ^{-1}j)**, Q^{(k)} the composite root map (equivalently
      Q_str^{(n)}, since r depends on the data mod Closed): the source is the non-local effective datum
      -Q^{(k)}Δ^{-1}j;
    - (iii) (symbol level, co-closed j, LED-symb/EXP-id notation, ĵ_ν := ĵ_ν(p/n), W̄_ν := ΠD̄·D̄_ν) the K = 0 alias
      of Q^{(k)}Δ^{-1}j is cW̄_νĵ_ν/φ (c the decimation constant of LED-symb), singular like |p|^{-2}·|ĵ|, but the K = 0
      part of the resulting r̂ (the data map applied to the effective datum -Q^{(k)}Δ^{-1}j) is analytic:
        **r̂^{(0)}_σ = c[W̄_σĵ_σ/β_σ + ν_σ(ΠD̄/(β_σΨ))Σ_νν̄^{(n)}_νR_νĵ_ν/β_ν],**
      and the K = 0 part of j ↦ f̂_0 is analytic too: the factor ĵ_σ - (aδ_σ/β_σ)ĵ_σ = (φR_σ/β_σ)ĵ_σ cancels the 1/φ of
      Δ^{-1} (**screening: β - κ|W|² = φR**), and the ν_σ-part carries φ through δ_σ/β_σ - δ_ρ/β_ρ = (φ/a)(R_ρ/β_ρ - R_σ/β_σ).
    *Proof.*
    - (i) The Euler-Lagrange equations: d*dB_0 + κ_0Q^Tr_0 = j and κ_{i-1}r_{i-1} = κ_iQ^Tr_i. d*j = 0, so J-str's
      divergence argument is unchanged. dB_0 = dΔ^{-1}d*dB_0 (Hodge) and d*dB_0 = j - κ_0Q^Tr_0.
    - (ii) Iterate B_{i+1} = QB_i - r_i: modulo Closed, B_k ≡ Q^{(k)}Δ^{-1}j - Pr as in LED-dual (ii). So r ∈ CoCl_0 solves
      LED-dual's problem with B_k replaced by B_k - Q^{(k)}Δ^{-1}j, whose minimiser is unique. The zero-mean condition is
      unchanged since ⟨j, h⟩ = 0.
    - (iii) Insert ĝ^{(0)}_ν = -cW̄_νĵ_ν/φ into EXP-id's data map r̂_σ = -φb̂_σ/β_σ + ν_σ(a/(β_σΨ))Σ_νν̄_νb̂_ν/β_ν. The first term
      loses 1/φ at once (the j-part of r̂ is the data map applied to -ĝ). For the second, ν̄_νW̄_ν = ΠD̄·ν̄_νD̄_ν = ΠD̄·ν̄^{(n)}_νδ_ν (the entire identity ν̄^{(n)}D = ν̄), and
      δ_ν/β_ν = a^{-1}(1 - φR_ν/β_ν); the term Σ_νν̄^{(n)}_νĵ_ν is (a multiple of) the K = 0 alias of d*j, which is 0. What
      remains carries φ. For f_0: with the adjoint normalisation (the one for which the G-term of P̂ is
      κΣ_K|W_{n,μ}(θ_K)|²/φ(θ_K), LED-symb), (Q^Tr)^ has K = 0 part c^{-1}W_σr̂_σ, and κ|W_σ|² = aδ_σ; insert into
      n²dΔ^{-1}(j - κQ^Tr) and use W_σν_σ = ΠD·ν^{(n)}_σδ_σ. ∎
      **[R1314-fix] The f_0 half written out** (re-derived by the review; c30 B checks each line at complex points). Put
      S := Σ_νν̄^{(n)}_νR_νĵ_ν/β_ν, so r̂^{(0)}_σ = c[W̄_σĵ_σ/β_σ + ν_σΠD̄·S/(β_σΨ)]. Two entire identities are used:
      κW_σW̄_σ = κΠδ·δ_σ = aδ_σ, and W_σν_σ = ΠD·D_σν_σ = ΠD·ν^{(n)}_σδ_σ (from ν^{(n)}D̄ = ν, so ν^{(n)}δ = νD).
      1. *Screening line.* The K = 0 part of the level-0 current is
         ĵ_σ - κc^{-1}W_σr̂^{(0)}_σ = (1 - aδ_σ/β_σ)ĵ_σ - aν^{(n)}_σ(δ_σ/β_σ)S/Ψ = (φR_σ/β_σ)ĵ_σ - aν^{(n)}_σ(δ_σ/β_σ)S/Ψ,
         using κΠDΠD̄ = a and β_σ - aδ_σ = φR_σ.
      2. *Curl line.* Apply the fine-d symbol (ν^{(n)}_ρ·_σ - ν^{(n)}_σ·_ρ) and divide by φ (the K = 0 part of Δ^{-1}). The
         first term gives φ(ν^{(n)}_ρR_σĵ_σ/β_σ - ν^{(n)}_σR_ρĵ_ρ/β_ρ); the second gives
         -(aS/Ψ)ν^{(n)}_ρν^{(n)}_σ(δ_σ/β_σ - δ_ρ/β_ρ) = -(S/Ψ)·φ·ν^{(n)}_ρν^{(n)}_σ(R_ρ/β_ρ - R_σ/β_σ), since
         δ/β = (1 - φR/β)/a. Both carry φ, which cancels the 1/φ:
         **f̂^{(0)}_{0,ρσ} = (const)·e^{ip·u/n}[ν^{(n)}_ρR_σĵ_σ/β_σ - ν^{(n)}_σR_ρĵ_ρ/β_ρ - (S/Ψ)ν^{(n)}_ρν^{(n)}_σ(R_ρ/β_ρ - R_σ/β_σ)]**,
         (const) the normalisation n²·c-factors of LED-symb; every factor is analytic near p = 0 (EXP-strip/EXP-strip').
    - c29 A: (ii) and (i) hold to ≤ 1.1e-12 against LSMR chains with a source (d = 4: k = 1, 2; d = 2: k = 2, 3,
      non-constant κ_i), and the algebraic identity in (iii) to 1.1e-12 at complex points (n = 3, 9, 27); along
      p = (s, 0, 0, 0), s = 0.4 → 0.01, the input |ĝ^{(0)}| grows from 6.2 to 1.0·10⁴ while |r̂^{(0)}| stays at 1.0.
    - **What it does and does not give.** It is the first step of the general-source estimate (G♯) below: a level-0
      source acts on r through the same analytic symbols as data, after an exact screening cancellation. It does NOT
      give sup bounds of the fine-level response f_0 to j: the K ≠ 0 aliases of dΔ^{-1}j are the short-distance
      Biot-Savart kernel (|x|^{-3}), whose per-offset alias sums are not absolutely summable uniformly in n, so the
      fine-level bound needs a real-space localisation (a finite-range split of Δ^{-1}), not done here.
  - **Proposition NA-IFT (quantitative implicit function step): PROVEN (standard; not counted).** Let X, Y, D be Banach
    spaces, 𝓛: X → Y linear with ||𝓛^{-1}|| ≤ G, N: D → Y linear with ||𝓛^{-1}N|| ≤ G_D, and 𝔑(x; B) with
    ||𝔑(0; B)|| ≤ Cs² and ||𝔑(x; B) - 𝔑(x'; B)|| ≤ C(||x|| + ||x'|| + s)||x - x'|| for ||x||, ||x'|| ≤ ρ_0, s := ||B||_D.
    If s ≤ min(ρ_0/(2(1 + G_D)), 1/(16GC(1 + G_D)²)), then 𝓛x = NB + 𝔑(x; B) has a unique solution with
    ||x|| ≤ 2(1 + G_D)s, and **||x - 𝓛^{-1}NB|| ≤ 9GC(1 + G_D)²s²**. If in addition the same bounds hold in weighted
    norms (constants G_w, G_{D,w}, C_w, with ||D_B𝔑||_w ≤ C_w(||x|| + s)) and s ≤ 1/(10G_wC_w(1 + G_D)), then
    **||∂x/∂B||_{D_w→X_w} ≤ 2G_{D,w} + 6G_wC_w(1 + G_D)s**.
    *Proof.* Put r := 2(1 + G_D)s and Φ(x) := 𝓛^{-1}(NB + 𝔑(x; B)). On ||x|| ≤ r: ||Φ(x)|| ≤ G_Ds + GC(r + s)² ≤
    G_Ds + 9GC(1 + G_D)²s² ≤ (G_D + 9/16)s ≤ r, and Lip(Φ) ≤ GC(2r + s) ≤ 5GC(1 + G_D)s ≤ 5/16. Banach's fixed point
    theorem; ||x - 𝓛^{-1}NB|| = ||𝓛^{-1}𝔑(x; B)|| ≤ GC(r + s)². For the derivative, ∂x/∂B = (1 - 𝓛^{-1}D_x𝔑)^{-1}
    𝓛^{-1}(N + D_B𝔑), with ||𝓛^{-1}D_x𝔑||_w ≤ G_wC_w(2r + s) ≤ ½ (Neumann series). ∎
  - **Proposition B-NA-red (B-NA reduced to two linear-analytic inputs): PROVEN as an implication; B-NA stays OPEN.**
    Data V_k = exp(B_k) in a global small-field gauge (||B_k||_D := max_c|B_k(c)| ≤ ε; the flat classes with
    non-trivial holonomy are covered separately by N2-a's constant lift, failure mode BNA-F4). Let 𝒮 be a linear chain
    gauge slice with a Feynman term ½||Γ_gfx||² on its residual group, 𝓛 the Hessian of E_lin + ½||Γ_gfx||² on 𝒮, N the
    linear data map, and ||·||_X, ||·||_Y norms on chain configurations and sources, with weighted versions (weights
    e^{±m d(·, X_0)}, 0 ≤ m ≤ m_G, any X_0). Suppose, uniformly in k and T:
    - (G♯) ||𝓛^{-1}||_{Y→X} ≤ G, ||𝓛^{-1}N||_{D→X} ≤ G_D, and the weighted analogues G_w, G_{D,w};
    - (R♯) 𝔑(x; B_k) := ∇(E_NA∘exp + ½||Γ_gf·||²)(x) - 𝓛x - NB_k satisfies NA-IFT's bounds with constants C, C_w on
      ||x||_X ≤ ρ_0;
    - (FP♯) the Faddeev-Popov operator DΓ_gf(x)∘τ_x is onto for ||x||_X ≤ ρ_0.
    **[R1314-fix] Corrections (binding).** (1) *The combined operator.* NA-IFT solves ∇(E + ½||Γ_gfx||²) = 0 INSIDE the
    slice 𝒮 = {h = 0}; NA-crit needs criticality in every direction, including the gauge directions transverse to 𝒮. So
    (FP♯) is replaced by
    - **(FP♯')** the combined map 𝔉_x: λ ↦ (Dh(x)τ_xλ, DΓ_gf(x)τ_xλ) is onto (target R^q × R^m) for ||x||_X ≤ ρ_0,
    and NA-crit by **Lemma NA-crit' (Lagrange form): PROVEN-HERE (counted with NA-FP).** Let S, τ be as in NA-crit, h:
    𝒳 → R^q C¹ with Dh(x) onto, 𝒮 := {h = 0}, and x ∈ 𝒮 critical for (S + ½|Γ|²)|_𝒮. If 𝔉_x is onto, then Γ(x) = 0 and
    dS(x) = 0 on all of T_x𝒳. *Proof.* Lagrange: there is μ ∈ R^q with dS(x)[v] + ⟨Γ(x), DΓ(x)v⟩ = ⟨μ, Dh(x)v⟩ for all
    v ∈ T_x𝒳. Invariance gives dS(x)τ_xλ = 0; with v = τ_xλ, ⟨(-μ, Γ(x)), 𝔉_xλ⟩ = 0 for all λ, so (-μ, Γ(x)) ⊥ Ran 𝔉_x
    = R^q × R^m: μ = 0 and Γ(x) = 0, and then dS(x) = 0. ∎ With (FP♯') and NA-crit', the conclusion below stands.
    (2) *The norms.* ||·||_X, ||·||_Y, ||·||_D are now those of RTARGET §33: X = ||·||_{X_c} (with its Hölder version),
    Y = the divergence-form source norm ||·||_Y (Hölder version ||·||_{Y,α}) with level weights ω, D = ||·||_{D,m}; the
    weighted versions are the same norms with m > 0; the slice is the per-level covariant slice (h^{(i)}_U = 0 at each
    level, Feynman terms on the residual groups). (G♯) at U = 1 is (G♯_0-field) of §33; see L5 [S15].
    Then for **||B_k||_D ≤ ε_0 := min(ρ_0/(2(1 + G_D)), 1/(16GC(1 + G_D)²), 1/(10G_wC_w(1 + G_D)))** there is a critical
    point of E_NA (NA-crit with (FP♯)), unique in the slice ball of radius 2(1 + G_D)||B_k||_D; ||x_NA - x_lin||_X ≤
    9GC(1 + G_D)²||B_k||_D²; and the response kernels decay with every rate m ≤ m_G, with constants at most
    2G_{D,w} + 6G_wC_w(1 + G_D)ε_0 (no loss in the rate; the loss is in the constant).
    *Proof.* NA-IFT and NA-crit. ∎
    - **Why this is a reduction and not B-NA (the failure modes, established).**
      - (BNA-F1) *The proven linear kernels are data kernels.* N2-lin and N2-exp control B_k ↦ (r, f_0) only. The
        remainder is a general source at every level (at level 0, a co-closed current). SRC-id shows that such a
        source acts as the non-local datum -Q^{(k)}Δ^{-1}j; its r-response is analytic (screening), its fine-level
        f_0-response is the short-distance Biot-Savart kernel plus a screened part. So (G♯) is a new estimate, not a
        corollary of N2-exp.
      - (BNA-F2) *Sup norms do not close (scaling count, argued).* In coarse units (x^c_i := L^{k-i}x_i, currents
        j^c_i := L^{3(k-i)}j_i) the level-0 Wilson remainder ⟨dx, ∂q⟩ + ⟨q, ∂dx⟩ + ⟨q, ∂q⟩ (q the BCH remainder of a plaquette)
        is of size |x|·|dx| in own units; for a field with no derivative control (|dx|_own ~ |x|_own = X/n) this is
        nX² in current units, not O(X²). With one derivative controlled it is O(X²) (marginal, as expected for 4D
        Yang-Mills), and the soft remainders at level i are O(L^{-(k-i)}) or O(X³) (irrelevant or cubic). The linear
        inverse then has to gain one derivative, which fails between C⁰ spaces (∇²Δ^{-1} is a Calderón-Zygmund kernel).
        The natural pair is a coarse-unit Schauder pair: X = C^{1,α} (level-weighted), Y = C^{0,α} currents.
      - (BNA-F3) *The gauge must be smooth.* The complete local gauge (axial/tree gauge in each block at each level)
        is exact and local, but it moves the coarse field onto the sparse crossing links: their own-unit size is
        |B_k| at every level, i.e. n|B_k| in coarse units at level 0, so it is incompatible with X = C^{1,α} uniformly in
        n. A smooth complete gauge is the covariant multi-level slice (h^{(i)}_U = 0 at each level plus Feynman terms on
        the residual groups); its (G♯) contains a multi-level physical gap of PG/PG^{(k)} type, and at non-trivial
        backgrounds the (NA) gap. So B-NA and (NA) share one missing estimate.
    - **B-NA status: OPEN, narrowed to (G♯) (a lattice multi-scale Schauder estimate for the gauge-fixed linearised
      chain, uniformly in k and T, with exponential weights) and (R♯) (the remainder bound in the same Schauder pair,
      expected from NA-alg and the scaling count, not written).** Every algebraic, gauge-fixing and fixed-point step is
      proven (NA-alg, NA-crit, NA-inv, NA-IFT, B-NA-red), and SRC-id is the screening identity that (G♯) needs.
  - **SU(N) analogues of N2-E, N2-lin, N2-exp (target B): conditional, not counted.** Under (G♯), (R♯), (FP♯) and
    ||B_k||_D ≤ ε_0, Proposition B-NA-red gives:
    - (N2-lin, SU(N)) sup|r|, sup|f_0| ≤ C_out(G_D + 9GC(1 + G_D)²||B_k||_D)||B_k||_D, C_out the norm of x ↦ (r, f_0) on X
      (in the D-norm of a global small-field gauge, not yet in terms of the curvature);
    - (N2-exp, SU(N)) the response kernels decay at every rate m ≤ m_G (the linear B_k-kernels at m < m_*'), with
      constants ≤ 2G_{D,w} + 6G_wC_w(1 + G_D)ε_0;
    - (N2-E, SU(N)) E_NA ≤ E_lin(x_lin) + O(G_D³C||B_k||_D³), by expanding E_NA∘exp at x_NA with NA-alg.
    The curvature forms need a localisation, argued only: put V_k in axial gauge on a coarse ball of radius R around
    the observation point and cut the gauge function off smoothly to the global gauge at radius R ~ m^{-1}log(ε/sup|F|);
    the cut-off shell costs O(ε), since |∇χ|·|λ_ax| ~ R^{-1}·Rε.
  - **Theorem N2-exp' (a sharper strip; target D): PROVEN-HERE (strengthens N2-exp, no count change).** Setting and
    building blocks of N2-exp. For z = x + iy ∈ S_η(Q) put c_η := cosh η - 1, s_η := sinh η, c_φ := 18(cosh(η/3) - 1),
    σ_φ := 6 sinh(η/3), and keep c_Z, λ from EXP-strip (P4).
    - **Lemma EXP-strip' (sector bounds): PROVEN-HERE.** For η ≤ 0.1 with λ > 0:
      - (S1) |Re δ(z_α) - δ(x_α)| ≤ c_η, |Im δ(z_α)| ≤ s_η·min(1/3, |x_α|/6);
      - (S2) aδ_μ(z) = aδ_μ(x)·me^{iθ} with m_- := (1 - α_1)⁵ ≤ m ≤ m_+ := ((1 + α_1)² + s_η²g_1²)^{5/2} and |θ| ≤ θ_a :=
        5arctan(s_ηg_1/(1 - α_1)), where α_1 := (π²/4)c_η and g_1 := π²/12;
      - (S3) Re φ_α(z) - φ_α(x) ∈ [-c_φ, 0], |Im φ_α(z)| ≤ σ_φ√φ_α(x); |Re Δ_α(z) - Δ_α(x)| ≤ 2c_η, |Im Δ_α(z)| ≤ 2s_η√Δ_α(x);
      - (S4) |Re R_μ(z) - R_μ(x)| ≤ e_RR := κ̂c_η/(L² - 1) + κc_Z, |Im R_μ(z)| ≤ e_RI := κ̂s_η/(L² - 1) + κc_Z;
      - (S5) (1 - ρ_R)β_μ(x) ≤ Re β_μ(z) ≤ (1 + ρ_R^+)β_μ(x) and |Im β_μ(z)| ≤ ρ_Iβ_μ(x), with
        ρ_R := 1 - m_-cos θ_a + e_RR + 4c_φ(R̄ + e_RR)/b_* + 2σ_φe_RI/√b_*, ρ_R^+ := m_+ - 1 + e_RR + 2σ_φe_RI/√b_*,
        ρ_I := m_+sin θ_a + e_RI(1 + 4c_φ/b_*) + 2σ_φ(R̄ + e_RR)/√b_*;
      - (S6) for |x| ≤ r_0: |Ψ(z)| ≥ Ψ_L := 1 - (r_0² + 4c_φ + 2σ_φr_0)(R̄ + e_RR + e_RI)/((1 - ρ_R)b_*);
      - (S7) for |x| ≥ r_0: Re Σ(z) ≥ (ψ(x)/min_νβ_ν(x))·br'_V, br'_V := (1 - ρ_R)/(D_2Γ) - [8c_η(1 + ρ_R^+)/ψ_0 +
        4s_ηρ_I/√ψ_0]/(1 - ρ_R)², D_2 := (1 + ρ_R^+)² + ρ_I², ψ_0 := 4r_0²/π²; and Re φ(z) ≥ φ(x) - 4c_φ.
      The point: the first-order (in η) changes of these real-on-R functions are imaginary, so the real parts, and
      hence every lower bound, move only at second order, except through the crude c_Z.
      *Proof.*
      - (S1) δ(w) = Σ_lw_le^{-iwl/n} with w_l = (n - |l|)/n² symmetric, so Re δ(x + iy) = Σw_lcos(xl/n)cosh(yl/n) and
        Im δ = -Σw_lsin(xl/n)sinh(yl/n). |l/n| < 1 gives the first bound. sinh(t s) ≤ t sinh s (t ∈ [0, 1]), Σw_l|l| =
        (n² - 1)/(3n) and Σw_ll² = (n² - 1)/6 give |Im δ| ≤ s_η min(1/3, |x|/6).
      - (S2) Each of the five factors is δ(x_j)(1 + u_j), with Re(1 + u_j) ≥ 1 - α_1 (δ ≥ 4/π², R1) and |Im u_j| ≤ s_ηg_1,
        since min(1/3, |x|/6)/max(4/π², 1 - x²/12) ≤ π²/12 on [-π, π]. Arguments add and moduli multiply.
      - (S3) Re φ_α - φ_α(x) = -2n²cos(x/n)(cosh(y/n) - 1), with cos(x/n) ∈ [½, 1] and 2n²(cosh(η/n) - 1) decreasing in n
        (n ≥ 3); |Im φ_α| = 2n²|sin(x/n)|sinh(|y|/n) ≤ 2·√φ_α(x)·3sinh(η/3), using n|sin(x/n)| ≤ √φ_α and n sinh(η/n)
        decreasing. Δ_α likewise, with |sin x| ≤ √Δ_α.
      - (S4) A_μ = Σ_m(κ/κ_{k-1-m})(α_s + β_scos z_μ), 0 ≤ β_s ≤ L^{-2m}, S_1 ≡ 1; Re cos(x + iy) - cos x = cos x(cosh y - 1),
        Im cos(x + iy) = -sin x sinh y. Z by (P4).
      - (S5) Re β = Re aδ + Re φ Re R - Im φ Im R. Use (S2)-(S4), Re φ ≤ φ(x), Re R ∈ [R - e_RR, R + e_RR] ⊂ (0, R̄ + e_RR],
        Σ_α√φ_α ≤ 2√φ, and divide by β(x) ≥ max(b_*, φ(x), aδ_μ(x)) (R4), with √φ/β ≤ 1/√b_*. Im β likewise, with
        |Re φ| ≤ φ(x) + 4c_φ.
      - (S6) Ψ = 1 - Σ_μφ_μR_μ/β_μ; |β_μ(z)| ≥ Re β_μ(z) ≥ (1 - ρ_R)b_*; Σ_μ|φ_μ(z)| ≤ φ(x) + 4c_φ + 2σ_φ√φ(x) and φ(x) ≤ |x|².
      - (S7) Re(Δ_μ/β_μ) = (Re Δ_μRe β_μ + Im Δ_μIm β_μ)/|β_μ|². Bound the positive part Δ_μ(x)(1 - ρ_R)β_μ(x) over
        |β_μ|² ≤ D_2β_μ(x)², and the negative parts 2c_η(1 + ρ_R^+)β_μ(x) + 2s_η√Δ_μ(x)ρ_Iβ_μ(x) over
        |β_μ|² ≥ (1 - ρ_R)²β_μ(x)². Sum with β_μ ≤ Γmin_νβ_ν (R4), Σ_μ√Δ_μ ≤ 2√ψ and ψ ≥ ψ_0 (R6). Re φ: from (S3). ∎
    - **Statement.** Let η'_*(κ, κ̂, L) be the largest η ≤ 0.1 for which some r_0 gives θ_a ≤ π/2, ρ_R ≤ ½, Ψ_L ≥ 1/10,
      br'_V ≥ (1 - ρ_R)/(4D_2Γ) and 4c_φ ≤ ψ_0/2, and **m_*' := min_{κ∈[κ_-,κ_+]}η'_*.** Then the conclusions (i)-(ii) of
      Theorem N2-exp hold with m_*' in place of m_*.
      - Values (L = 3, κ_i ≡ κ) [R1314-fix: the session-14 values 0.0385 (r_0 = 0.70) and 0.0307 (r_0 = 0.90) exceed the
        bisection values at those r_0 (0.03845, 0.03068), and the κ̂ = 16 values were rounded up by < 0.3%; all are now
        rounded down, and every condition holds at each pair in 30-digit arithmetic, c30 A]: **η'_* = 0.0384 (κ = 1,
        r_0 = 0.70)**, 0.0273 (κ = 0.25, r_0 = 0.37), 0.0306 (κ = 4, r_0 = 0.90); with κ̂ = 16: 0.0140 (κ = 0.25, r_0 = 0.24),
        0.0226 (κ = 1, r_0 = 0.47), 0.0216 (κ = 4, r_0 = 0.67). (Best values over r_0, reviewer's scan: 0.03854, 0.02750,
        0.03077.) Against N2-exp: 3.5× (κ = 1), 3.5×
        (κ = 0.25), 2.6× (κ = 4); 3.8× and 2.6× at κ̂ = 16.
      *Proof.* As for N2-exp, with (S5)-(S7) in place of (P5)-(P7): |β_μ(z)| ≥ ½β_μ(x); Ψ ≠ 0 where |x| ≤ r_0 (|Ψ| ≥ 1/10);
      Re Σ > 0 where |x| ≥ r_0; φ(z) ≠ 0 there (Re φ ≥ ψ_0/2); φ^{(K)} ≠ 0 for K ≠ 0 (λ > 0). The uniform bound M uses
      |Ψ| ≥ Ψ_L, |β| ≥ b_*/2 and Re Σ ≥ (ψ/β_min)br'_V in place of Ψ_U/2 and br_V; the two-formula definition of g,
      periodicity at ∂Q and the Paley-Wiener step are unchanged. ∎
      - **N6.** M ≳ 457/m_*' ≈ 1.2·10⁴ at κ ≡ 1 (was 4.1·10⁴). The located rate (≈ 0.98, c28 C) is still ≈ 25 times
        larger. What limits m_*' now: the crude Z-bound c_Z (first order, ≈ 1.3η) and the first-order Im β (ρ_I ≈ 10.7η)
        entering br'_V through 4s_ηρ_I/√ψ_0. A point-dependent bound or a direct second-order treatment of Z would be the
        next step.
      - c29 B: every inequality of (S1)-(S7) holds at complex points (n = 3, 9, 27; κ = 0.25, 1, 4; κ̂ = 16 at k = 2),
        including the sharp ones ((S3) at x = 0, |y_α| = η: ratio 1.000); the lower bounds of (S6)-(S7) hold with margins
        ≥ 4.8.
  - **Check c29** (criteria checks/c29_criteria.md, written before the script; disclosures in checks/c29_time.txt).
    - **Part A: PASS.** SRC-id (ii) and (i) hold to ≤ 1.1e-12 against LSMR chains with a fine source (d = 4: k = 1, 2;
      d = 2: k = 2, 3 with κ = (0.5, 2, 1)); the algebraic identity of (iii) to 1.1e-12 at complex points (n = 3, 9, 27).
    - **Part B: PASS.** Every inequality of EXP-strip' (S1)-(S7) at complex points with |y_α| ≤ η'_*; the sharp ones
      reach ratio 1.000 (Re φ_α at n = 3, x = 0, |y_α| = η); the lower bounds of (S6)-(S7) hold with margins ≥ 4.8.
    - **Part C: VALID** (SU(2), d = 4, κ = 1, c22 geometry; all minimisations converged to |g|/|g_0| ≤ 1e-9).
      - C-V2 PASS: D(0.025) = 0.027, so c26's linear chain is the t → 0 limit of the SU(2) residual.
      - **C1 FAILED as pre-registered** on its size sub-criterion: the slope is p = 1.04 (D = O(t): the non-linear part
        of ρ is second order, as B-NA predicts), but D(0.1) = 0.110 > 0.1. D(t)/t = 1.089, 1.091, 1.101, 1.145, 1.220
        (t = 0.025 … 0.3): the second-order coefficient is ≈ 1.09 for a datum with max|X| = O(1). The 0.1 threshold
        was a guess; it is not edited. Informational: E/t² = 277.11 → 264.32 against E_lin = 277.19.
      - C2 (coarse 4⁴, background t = 0.2, localised datum, s = 0.01): C2-V, C2a, C2b PASS. Profiles at d = 0, 1, 2:
        non-abelian part 0.145, 0.068, 0.0092; linear 0.705, 0.104, 0.021. Rates m_NA = 1.38, m_lin = 1.77; the
        non-abelian part is 0.21 of the linear kernel and decays at 0.78 of its rate (two coarse units only).
    - **Part D: PASS.** D1: the telescoping identity h_U(D_Uλ) = M_Uλ - λ(c) holds to 1.9e-15 at the critical U* and
      at a random U. D2: at U*, |H_UD_Uλ|/|D_Uλ| is 3.7e-8 of the median |H_Uv|/|v|. D3 (control): at the non-critical
      start configuration it is 1.9e-2, so NA-inv's criticality hypothesis is needed (NA-F1).
    - Resources: A 3 s / 0.48 GB; B 4.6 s / 0.10 GB; C 1645 s / 1.09 GB; D 94 s / 0.39 GB. One job at a time, nice 10,
      BLAS threads 1, load ≤ 3.5, ≥ 42% free.

- **[S15] Session 15: (G♯)_0 at the trivial background (soft half PROVEN, fine half reduced); [R15-fix: was "NA-F2 is an artefact of the
  direct n = L^k step"] the top-level per-step defect has no n-loss (per-level defect bound PROVEN; the multi-level
  uniformity is carried by (NA-H) ⊂ B-NA); (R♯) stated in the new norms. Targets pre-stated in RTARGET.md
  §33-36 at 19:29 UTC, after the [R1314-fix] edits and the lead's exploratory reasoning in this session, and before any
  written session-15 derivation or check script. The c30 criteria were written before the script (one pre-script
  correction, disclosed). Status of L5 unchanged: IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE (all unreviewed):
  Theorem G♯_0-soft (with Lemmas SRC-all, REC and KF counted with it); Lemma LES-div; Proposition NA-lev (with Lemma
  E-low counted with it). Check c30: A PASS, B PASS, C PASS, D informational.
  - **Norms.** Those of RTARGET §33, verbatim: coarse-unit values H^c = L^{2(k-l)}H (level-l 2-forms), r^c_i = L^{k-1-i}r_i,
    f_0 = n²dB_0; coarse ℓ¹ torus distance d; w = e^{md(·,X_0)}; ||v||_{∞,m} = sup w|v^c|; level weights ω_0 = 1, ω_l ≥ 1,
    Ω = Σ_lω_l^{-1}; divergence-form sources j_l = d_l^*G_l (d_l^* := d_l^T, so j_l is co-closed with zero mean) with
    ||G||_Y = max_lω_l||G_l||_{∞,m}; ||B_k||_{D,m} = ||B_k||_{∞,m}; ||r||_{X_s} = max_iL^{k-1-i}||r_i||_{∞,m}; the
    Campanato seminorm [·]_{α,m} at coarse scales 1/n ≤ ρ ≤ 1. Throughout, M = M(L, κ_±) is Theorem N2-exp's (or N2-exp''s)
    strip bound for the B_k-kernels of r_{k-1} and of f_0 (every offset u; every component pair), 0 ≤ m < m' ≤ m_*',
    μ := m' - m, and S(μ) := Σ_{Z∈Z⁴}e^{-μ|Z|_1} = coth⁴(μ/2).
  - **Lemma SRC-all (sources at every level): PROVEN-HERE.** In Setting SC with sources j_l (co-closed, zero mean) at
    levels 0 ≤ l ≤ k-1, let (B_i) be a critical point of E_j, s_i := κ_ir_i, s := s_{k-1}, and write Q^{(a→b)} :=
    Q_{b-1}⋯Q_a (the chain's root maps; identity if a = b). Then:
    - (i) d*s_i = 0 for every i, and **s_i = (Q^{(i+1→k)})^Ts - Σ_{l=i+1}^{k-1}(Q^{(i+1→l)})^Tj_l**;
    - (ii) **J_0 := d*dB_0 = j_tot - (Q^{(0→k)})^Ts**, j_tot := j_0 + Σ_{l≥1}(Q^{(0→l)})^Tj_l, and dB_0 = dΔ^{-1}J_0;
    - (iii) **r_{k-1}(j; B_k) = r_{k-1}(0; B_k - g_eff)**, g_eff := Q^{(0→k)}Δ^{-1}j_tot +
      Σ_{i=0}^{k-2}κ_i^{-1}Q^{(i+1→k)}Σ_{l=i+1}^{k-1}(Q^{(i+1→l)})^Tj_l (the effective datum; it reduces to SRC-id (ii)
      when only j_0 ≠ 0).
    *Proof.* The Euler-Lagrange equations are d*dB_0 + Q_0^Ts_0 = j_0 and s_{i-1} = Q_i^Ts_i - j_i (1 ≤ i ≤ k-1). (i): apply d*
    to the level-0 equation: d*Q_0^T = ev^Td* (root covariance) and d*j_0 = 0 give ev^Td*s_0 = 0, so d*s_0 = 0 (ev^T
    injective); induct upward with d*j_i = 0. Unrolling the recursion gives the formula. (ii): insert (i) at i = 0 into the
    level-0 equation; dB_0 = dΔ^{-1}d*dB_0 (Hodge). (iii): B_{i+1} = Q_iB_i - s_i/κ_i gives
    B_k = Q^{(0→k)}B_0 - Σ_iκ_i^{-1}Q^{(i+1→k)}s_i. Modulo Closed (which every Q_i preserves), B_0 ≡ Δ^{-1}J_0. Insert (i)-(ii);
    the s-terms are Q^{(0→k)}Δ^{-1}Q^{(0→k)T}s + Σ_iκ_i^{-1}Q^{(i+1→k)}Q^{(i+1→k)T}s = Pr (LED-dual's P, with s = κ_{k-1}r; on
    co-closed inputs Q_root^T = Q_str^T, and Q_root - Q_str is exact, IT-str). So B_k + Pr ≡ g_eff mod Closed. Zero mean of r:
    ⟨(Q^{(0→k)})^Ts, h⟩ = ⟨j_tot - J_0, h⟩ = 0 for constant h, and Q^{(0→k)}h = nh. Hence r ∈ CoCl_0 solves LED-dual's
    problem for the data B_k - g_eff, whose minimiser is unique. ∎ c30 C1/C2: ≤ 3.1e-10 against MINRES chains with random
    sources at every level (d = 2: k = 2, 3, including κ = (0.5, 2, 1); d = 4: k = 1, 2).
  - **Lemma REC (Green reciprocity): PROVEN-HERE (counted with G♯_0-soft).** Let (B_i) be critical for (B_k = 0, j) with
    j_l = d_l^*G_l, and (B'_i) critical for (B'_k, j = 0). Then **κ_{k-1}⟨r_{k-1}, B'_k⟩ = Σ_{l=0}^{k-1}⟨G_l, d_lB'_l⟩**. So the
    source-to-r map is the transpose of the data-to-curvature maps: r_{k-1}(j; 0) = κ_{k-1}^{-1}Σ_l𝒦_l^TG_l, 𝒦_l: B_k ↦ d_lB_l.
    *Proof.* Let ℰ(B, δ) := ⟨dB_0, dδ_0⟩ + Σ_iκ_i⟨Q_iB_i - B_{i+1}, Q_iδ_i - δ_{i+1}⟩ (symmetric bilinear, top components
    included). Criticality of B: ℰ(B, δ) = Σ_{l<k}⟨j_l, δ_l⟩ - κ_{k-1}⟨r_{k-1}, δ_k⟩ for every δ (the last term is the
    δ_k-derivative; it is absent when δ_k = 0). Criticality of B': ℰ(B', δ) = 0 whenever δ_k = 0. Take δ := B (B_k = 0) in
    the second, δ := B' in the first, and use symmetry: 0 = Σ_l⟨j_l, B'_l⟩ - κ_{k-1}⟨r_{k-1}, B'_k⟩, and
    ⟨d_l^*G_l, B'_l⟩ = ⟨G_l, d_lB'_l⟩. d_lB'_l is gauge invariant, so any critical B' may be used. ∎ c30 C3: ≤ 4.3e-9.
  - **Lemma KF (B_k-kernels of the curvatures at every level): PROVEN-HERE (counted with G♯_0-soft).** Let
    f_l := L^{2(k-l)}d_lB_l (coarse units; f_0 as before). The kernel of B_k ↦ f_l obeys, for every level-l plaquette P and
    coarse link (X, μ), **|K_{f_l}(P; X, μ)| ≤ M_f e^{-m'd(P, X)}, M_f := Me^{8m'}(1 + 6κ̂)**, uniformly in k, T, l.
    *Proof.* (1) r_i = (κ_{k-1}/κ_i)(Q_str^{(i+1→k)})^Tr_{k-1} (LED-dual (i)); Q_str has non-negative entries with
    Σ_X Q_str((X, μ), b) = L^{-3} per step (J-str (c)), and the composite template of a coarse link lies within coarse
    ℓ¹ distance 3Σ_{j≥0}L^{-j} ≤ 4.5 of it. So |K_{r_i}(b; X)| ≤ κ̂L^{-3(k-1-i)}Me^{4.5m'}e^{-m'd(b, X)}. (2) BG-b-lin step 1:
    f_l = 𝔄_{0→l}f_0 - Σ_{i<l}𝔄_{i+1→l}ϱ_i, ϱ_i := L^{2(k-1-i)}dr_i, with 𝔄 probability averages (Lemma CR (i)) supported
    within coarse distance 1.5. |dr| ≤ 4 max|r| over a plaquette's boundary. Hence
    |K_{f_l}| ≤ e^{1.5m'}[Me^{4m'} + 4κ̂Me^{6m'}Σ_{i<l}L^{-(k-1-i)}]e^{-m'd} ≤ Me^{8m'}(1 + 6κ̂)e^{-m'd} (Σ_{i<l}L^{-(k-1-i)} ≤ 3/2
    for L ≥ 3; the offset of a fine plaquette inside its coarse cell is absorbed into e^{4m'}). ∎
  - **Theorem G♯_0-soft (the abelian multi-scale bound for the soft outputs, general sources): PROVEN-HERE.** In Setting SC
    with sources j_l = d_l^*G_l and data B_k, d = 4, uniformly in k ≥ 1, T, X_0 and the level weights:
    - (a) **||r_{k-1}||_{∞,m} ≤ C_top Σ_l||G_l||_{∞,m} + C_D||B_k||_{D,m} ≤ C_topΩ||G||_Y + C_D||B_k||_{D,m}**, with
      C_top := 6M_f e^{4μ}S(μ)/κ_{k-1} and C_D := 4M S(μ);
    - (b) for every i, **L^{k-1-i}||r_i||_{∞,m} ≤ κ_i^{-1}e^{5m}[κ_{k-1}L^{-(k-1-i)}||r_{k-1}||_{∞,m} + 6Σ_{l>i}||G_l||_{∞,m}]**;
    - hence **||r||_{X_s} ≤ (e^{5m}/κ_-)[κ_+(C_topΩ||G||_Y + C_D||B_k||_{D,m}) + 6Ω||G||_Y]** =: C_s(Ω||G||_Y + ||B_k||_{D,m}).
    *Proof.* (a) By linearity r(j; B_k) = r(0; B_k) + r(j; 0). Data part: N2-exp(ii) (torus kernel = periodisation), with
    e^{md_T(X, X_0)} ≤ e^{m|Z|_1}e^{md_T(Y, X_0)} for every lift Z of X - Y: Σ_{Y,ν}|K_T(X; Y, ν)|e^{md_T(X,Y)} ≤ 4MS(μ). Source
    part: by REC, r(X, μ) = κ_{k-1}^{-1}Σ_lΣ_PL^{-2(k-l)}K_{f_l}(P; X, μ)G_l(P), and G_l = L^{-2(k-l)}G^c_l. With KF and
    w(X) ≤ e^{md(X,P)}w(P): w(X)|r(X)| ≤ κ_{k-1}^{-1}Σ_lL^{-4(k-l)}M_f||G_l||_{∞,m}Σ_Pe^{-μd(P,X)}, and Σ_P (six planes, L^{4(k-l)}
    level-l sites per coarse cell, a plaquette in cell Y has d(P, X) ≥ |Y - X|_1 - 4, torus sums dominated by Z⁴ sums as
    above) ≤ 6L^{4(k-l)}e^{4μ}S(μ). (b) SRC-all (i): κ_ir_i = κ_{k-1}(Q^{(i+1→k)})^Tr_{k-1} - Σ_{l>i}(Q^{(i+1→l)})^Td_l^*G_l. First
    term: ||Q_str^T||_{∞→∞} = L^{-3} per step (r_{k-1} co-closed). Second term: Lemma CR (i) gives d∘Q = W∘d on 1-forms, with
    W ≥ 0 of column sums L^{2-d} = L^{-2}, the same W for Q_root and Q_str (they differ by an exact form); transposing,
    Q^Td^* = d^*W^T, so (Q^{(i+1→l)})^Td_l^*G_l = d_{i+1}^*(W^{(i+1→l)})^TG_l with |d^*H| ≤ 2(d - 1)max|H| = 6max|H| and
    ||W^T||_{∞→∞} = L^{-2} per step. Supports shift by ≤ 4.5 coarse units in total, giving e^{5m}. In coarse units:
    L^{k-1-i}·L^{k-1-i}|r_i| ≤ κ_i^{-1}e^{5m}[κ_{k-1}L^{-(k-1-i)}|r_{k-1}| + 6Σ_{l>i}L^{2(k-1-i)}L^{-2(l-1-i)}L^{-2(k-l)}|G^c_l|], and the
    L-powers in the last term cancel. ∎ c30 C4 checks the transport bound (d = 4 ratio 0.30; d = 2 uses L^{(2-d)m}).
    - **What it settles (G0-F1, G0-F4).** G0-F4 does not occur: the bound is for the gauge-invariant soft outputs in
      gauge-invariant source norms, with no slice. **G0-F1 occurs, and is the marginal count:** each source level
      contributes O(1) to the proven bound for r [R15-fix: ARGUED, not shown: "the bound is attained in order of magnitude
      by sources coherent at the coarse scale"; no such source is exhibited], so with ω ≡ 1 the bound grows linearly in the
      number of source levels; it is uniform exactly when Ω < ∞, e.g. ω_l = L^{θ(k-l)} (l ≥ 1) [R15-fix: ARGUED: "which is
      what the soft remainders at levels l ≥ 1 provide (BNA-F2: O(L^{-(k-l)}) or cubic)" rests on BNA-F2, itself argued; the
      theorem is unconditional in ω and does not use this sentence]. The level-0
      source (the Wilson remainder) has ω_0 = 1. c30 D (random-sign sources, informational): sup|r^c_{k-1}|/sup|G^c_l| =
      0.026 (k = 1) and 0.0020, 0.061 (k = 2; l = 0, 1) in d = 4; random signs cancel across the L^{4(k-l)} plaquettes of a
      cell, so these are typical, not worst-case, values.
    - **Scope.** Divergence-form sources only. A plain (non-divergence) level-0 current with sup|j^c_0| bounded is not
      covered: its representative G_0 = dΔ^{-1}j_0 is the fine Biot-Savart potential, non-local. The plain-current r-response
      (SRC-id's screened K = 0 symbol plus its K ≠ 0 aliases, as a fine-to-coarse kernel) is **Lemma G♯_0-plain: OPEN**.
  - **Lemma LES-div (lattice Campanato step, divergence-form source): PROVEN-HERE.** Let u be real on Z⁴ with
    -Δu = Σ_a∂_a^-g_a + h on a box Q_R(x_0), R ≥ 16 (∂^- backward differences, Δ as in LES). Put
    ψ(x; ρ) := Σ_{Q_ρ(x)}|∇u - (∇u)_{Q_ρ(x)}|², [g]_{α;Q} := sup_{Q_ρ(y)⊂Q}ρ^{-α}(ρ^{-4}Σ_{Q_ρ(y)}|g - ḡ|²)^{1/2}, H_0 := sup_{Q_R}|h|.
    Then for every α ∈ (0, 1) there is an absolute C_α such that for x ∈ Q_{R/2}(x_0) and 1 ≤ ρ ≤ R/4,
      **ρ^{-4}ψ(x; ρ) ≤ C_α(ρ/R)^{2α}[R^{-4}ψ(x; R/4) + R^{2α}[g]²_{α;Q_R} + R^{2}H_0²]**,
    i.e. the Campanato seminorm of ∇u at scales ≤ R/4 is ≤ C_α[R^{-α}(R^{-4}ψ(R/4))^{1/2} + [g]_α + R^{1-α}H_0].
    *Proof.* LES's steps with one change of degree. On Q_r(x) ⊂ Q_R, split u = w + v, w := 0 off the interior and
    -Δw = Σ∂^-_a(g_a - ḡ_a) + h inside (the constant ḡ drops out of ∂^-). Testing with w (summation by parts) and the
    Dirichlet Poincaré inequality (||w||_2 ≤ Cr||∇w||_2): ||∇w||_2 ≤ ||g - ḡ||_{2,Q_r} + Cr||h||_{2,Q_r}, so
    ||∇w||_2² ≤ C(r^{4+2α}[g]² + r^6H_0²). v is discrete-harmonic inside, so each ∂_av is harmonic on the box shrunk by one,
    and LES step 3 gives Σ_{Q_ρ}|∇v - (∇v)_ρ|² ≤ C(ρ/r)^6Σ_{Q_r}|∇v - (∇v)_r|² (ρ ≤ r/4). Hence
    ψ(ρ) ≤ 2C(ρ/r)^6(2ψ(r) + 2||∇w||²) + 2||∇w||² ≤ A(ρ/r)^6ψ(r) + B'(r^{4+2α}[g]² + r^6H_0²), and r^6H_0² ≤ R^{2-2α}H_0²r^{4+2α}.
    LES step 5 (a = 6, b = 4 + 2α, R_1 = R/4; small radii as in LES step 4) gives the claim. ∎ Constants absolute
    (d = 4), not computed, as in LES. This is the lattice form of the Schauder step C^{0,α} (divergence form) → C^{1,α}.
  - **(G♯_0-fine): reduced, not proven.** At the fine level, take the Coulomb representative B := Δ^{-1}J_0 (co-closed;
    dB = dB_0), so componentwise -ΔB = J_0 = d^*G_tot - κ_{k-1}(Q^{(0→k)})^Tr_{k-1} (SRC-all (ii); G_tot :=
    G_0 + Σ_{l≥1}(W^{(0→l)})^TG_l, by Q^Td^* = d^*W^T). This is LES-div's form with g := G_tot (componentwise) and
    h := -κ_{k-1}(Q^{(0→k)})^Tr_{k-1}, |h| ≤ κ_{k-1}L^{-3k}sup|r_{k-1}| (J-str (c)). Apply LES-div with R := n (one coarse unit)
    and convert to coarse units (f_0 = n²dB, G^c = n²G, ρ_c = ρ/n; |F_μν| ≤ |∂_μB_ν| + |∂_νB_μ|): for every coarse box,
      **[f_0]_{α, coarse scales ≤ 1/4} ≤ C_α[E_∇^{1/2} + [G^c_tot]_α + κ_{k-1}sup|r_{k-1}|]**,
      E_∇ := n^{-4}Σ_{Q_{n/4}}|n²∇B - mean|² (the coarse-unit L² oscillation of the Coulomb potential's gradient over the coarse
    box), with every factor of n cancelling (n^{2+α}·n^{1-α}·L^{-3k} = 1 for the h-term). The r-term is controlled by
    Theorem G♯_0-soft. **But [G^c_tot]_α is controlled by ||G||_{Y,α} only for level-0 sources:** the transported coarse
    potentials (W^{(0→l)})^TG_l (l ≥ 1) carry the A1 weight pattern, which is rough at the fine scale (Campanato size
    ~ n^α|G^c_l| at ρ_c = 1/n); moving them into h instead gives a plain current of coarse size ~ 6L^k|G^c_l|, also not
    uniform. So:
    - **for level-0 sources (G_l = 0, l ≥ 1): (G♯_0-fine) ⇐ (LED-src)**, a weighted local-energy bound
      sup_Xw(X)E_∇(X)^{1/2} ≤ C(||G||_{Y,α} + ||B_k||_{D,m}), uniformly in k and T, together with the analogous bound for the
      coarse-box mean of f_0 (the sup part of ||f_0||_{X_f,α}); (LED-src) is OPEN;
    - **for sources at levels l ≥ 1: a separate OPEN item (G♯_0-fine-up).** Below the lowest source level l_min the
      sub-chain is a pure data problem with data B_{l_min} (no sources there), so N2-lin/N2-exp of that sub-chain give
      sup|f_0| ≤ C_f sup|f_{l_min}| (coarse units); this moves the question to the curvature response at level l_min,
      which is not proven. [R15-fix: stated as a displayed inequality.] With l_min := min{l : G_l ≠ 0} ≥ 1 (so G_0 = 0):
        **(G♯_0-fine-up)  ||f_0||_{X_f,α} ≤ C_up(||G||_Y + ||B_k||_{D,m}),  uniformly in k ≥ 1, T, X_0,**
      in the RTARGET §33 norms, C_up = C_up(L, κ_±, m, α); i.e. (G♯_0-fine) restricted to sources with G_0 = 0, where the
      transported potentials (W^{(0→l)})^TG_l are rough at the fine scale. Its sup part reduces, by the sub-chain remark
      above, to **sup_P w(P)|f_{l_min}(P)| ≤ C(||G||_Y + ||B_k||_{D,m})** (level-l_min curvature in level-k coarse units),
      which is not proven either. Deferred (REVIEW_S15_CONVERGENCE (d) step 2).
    - [R15-fix] **Range of k.** The use of LES-div at R = n needs n ≥ 16, i.e. k ≥ 3 at L = 3. For k = 1, 2 (n = 3, 9)
      LES-div is not needed: every scale 1/n ≤ ρ ≤ 1 of the Campanato seminorm is one of finitely many, and
      ρ^{-α}Osc_2(f_0; Q_ρ) ≤ n^{2+α}Osc_2(f_0; Q_1) ≤ 9³Osc_2(f_0; Q_1) (an L² average over a sub-box of volume fraction
      ≥ n^{-4} is at most n² times the average over the coarse box), so the reduction to the coarse-box L² oscillation holds
      with a constant independent of k for these two values.
    What is established about (LED-src):
    - **G0-F2 occurs** (as expected): no sup-norm-only bound. The local part of J ↦ dΔ^{-1}J on divergence-form sources is the
      fine Riesz projector Π_ex (kernel ~ |x|^{-4}, LED-unif), which is not bounded on ℓ^∞; Hölder control of G_tot is
      needed, and LES-div supplies the local step.
    - **G0-F3 is undecided.** The long-range part of the f_0 response to fine sources is the curvature-curvature Green
      function of the chain. The pieces are not separately exponential (the r-part dΔ^{-1}Q^{(0→k)T}κr has a 1/φ K = 0
      symbol on general co-closed r; the Π_exG_tot part has a power tail); their sum is the screened object, as in EXP-id
      and SRC-id (iii), but the source-to-f_0 symbol with K ≠ 0 aliases has not been shown analytic in a strip.
    - (G♯_0-fine) is also needed for (G♯_0-field) and for (R♯) (the remainder needs C^{1,α} control of the field).
  - **(G♯_0-field): not attempted.** It needs, in addition, the abelian multi-level (per-level slice) physical gap, which
    is not PG^{(k)} (that is a one-step composite) — see Proposition NA-lev (c) for the one-level version.
  - **Proposition NA-lev (the per-level (NA) defect has no trace loss; the per-level abelian gap): PROVEN-HERE.**
    *Which operator.* In the soft chain (Setting SC; decision 4) each RG step has a one-level kernel, block side L. The
    fluctuation integral of step i + 1 is over the level-i field A with the action E_i(A) + κ_i·(soft term of the one-level
    map Q: level i → i+1), where E_i is the effective chain energy with top level i (the Schur complement of levels
    0, …, i-1; LED-dual with k → i). So N4's fluctuation operator is the one-level operator, n = L, whose "fine" energy is
    E_i, not the direct n = L^k step of NA-FP's notation (by construction of Setting SC; the direct step is the special case
    i = 0, where E_0 = ½||dA||² and n = L as well). In level-i own units:
    - (a) *Defect bound.* Let U be a level-i background, W_0 the polar part of the averaged contour transports of a block,
      T_j = W_0e^{η_j} the individual contour transports, η̄ := max_j|η_j| (a background quantity; for a small-field background
      η̄ ≤ (number of plaquettes of the ribbon, ≤ 2L(L - 1))·max_p|log U_p|·(1 + O(max_p|log U_p|)) by the non-abelian Stokes
      expansion, argued). For the linearised soft defect Def(A)(X) := Ad(W_0)avg_j[(Ad(e^{η_j}) - 1)ℓ_{P_j}(A)] of L5 [S14],
      with P_j ranging over the one-level template contours (each with ≤ p_L := 5L - 4 links):
        **||Def(A)||² ≤ 81p_L(e^{2η̄} - 1)²||A||²** (ℓ² norms over level-i links and coarse sites), uniformly in i, k, T.
      [R15-fix: indexing.] Def lives on COARSE LINKS (X, μ) (one value per coarse link, as the soft term does); the text's
      "coarse sites" is corrected. The constant 81 holds under either indexing: per coarse link, a fine link lies in
      N(X, μ) for at most 8 pairs (X, μ) (templates stay in the blocks X and X + μ), and 8 ≤ 81 (REVIEW_S15_CONVERGENCE).
      *Proof.* Ad is an isometry and ||ad_η||_op ≤ 2|η|, so |(Ad(e^η) - 1)v| ≤ (e^{2|η|} - 1)|v|. |ℓ_P(A)| ≤ Σ_{b∈P}|A_b| ≤
      p_L^{1/2}(Σ_{b∈P}|A_b|²)^{1/2}. |avg_jv_j|² ≤ avg_j|v_j|², and avg_jΣ_{b∈P_j}|A_b|² ≤ Σ_{b∈N(X)}|A_b|², N(X) the links of the
      templates of X's coarse links (the block of X and its neighbours). Each link lies in N(X) for ≤ 3⁴ = 81 sites X. ∎
      **[R15-fix: headline narrowed; was "So NA-F2 is an artefact of the direct n = L^k step."] The top-level per-step
      defect has no n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA.** In the direct step the contours have
      ~5n links and the bound becomes ε^{-1}||∇A||²-type (PG-line); here every contour has ≤ 5L - 4 links, and the TOP-LEVEL
      defect is relatively bounded by 9(5L)^{1/2}(e^{2η̄} - 1) with no n. But E_i^{NA} is the Schur complement over all i
      finer levels of the SU(N) chain, and its Hessian contains a soft defect of the same type at every finer level; that
      multi-level uniformity has not gone away, it is inside (NA-H).
    - (b) **Lemma E-low (the effective energy controls the curvature): PROVEN-HERE (counted with NA-lev).** At the trivial
      background, for every B_k (Setting SC, any k ≥ 1, T):
        **E_k(B_k) ≥ c_E||dB_k||², c_E := 2κ_{k-1}/(π²(κ_{k-1} + 4π²R̄))** (R̄ of EXP-real (R3); c_E ≈ 0.0041 at κ ≡ 1, L = 3).
      [R15-fix: instance] c31 E (session 16): the exact per-mode minimum of E_k/||dB_k||² is 0.0310, 0.0297, 0.0296 (κ ≡ 1;
      k = 1, 2, 3; at p = (π, π, π, π)), 7.3-7.6 times c_E, and 0.0524 = 9.1 c_E at κ = (0.5, 2); chain-level (LSMR, d = 4)
      ratios ≥ 0.0297 (≥ 7.3 c_E) and the single-mode chain ratio equals the symbol value to ≤ 7e-15.
      *Proof.* By LED-dual (iii) and LED-symb, E_k = κ_{k-1}·max_{s∈CoCl_0}[-½⟨s, Ps⟩ - ⟨s, B_k⟩]; at each p ≠ 0 the constraint
      is ν^*ŝ = 0, and the Lagrange dual gives E_k = (κ_{k-1}/2)Σ_p min_t Σ_μP̂_μ^{-1}|b̂_μ - ν_μt|² (the minimising t gives
      r̂ = -P̂^{-1}(b̂ - νt), as in EXP-id). P̂_μ^{-1} = φ/β_μ (EXP-id) with β_μ = aδ_μ + φR_μ ≤ κ_{k-1} + 4π²R̄ (δ ≤ 1, R_μ ≤ R̄,
      φ ≤ |x|² ≤ 4π² on Q). min_tΣ_μ|b̂_μ - ν_μt|² = |F̂|²/ψ (Lagrange identity, F̂ = ν∧b̂), and φ/ψ ≥ 4/π² (R2). So each p
      contributes ≥ (κ_{k-1}/2)(4/π²)|F̂(p)|²/(κ_{k-1} + 4π²R̄); p = 0 has F̂ = 0. Parseval. ∎
    - (c) *Per-level abelian gap.* At the trivial background, the level-i fluctuation form (half the Hessian)
      E_i(A) + (κ_i/2)||QA||² obeys, on the one-level Phys (slice h = 0 of L3g(a)-slice at n = L, the residual group fixed as
      in FP-ab): **E_i(A) + (κ_i/2)||QA||² ≥ min(c_E, κ_i/2)·c_1||A||²_B**, c_1 := 1/(3.5·10⁶) (Proposition PG at κ = 1, whose
      constant is n-uniform, so in particular valid at n = L), in PG's normalisation (||A||²_B = L^{-2}Σ_ba_b² at one level),
      uniformly in i, k, T. *Proof.* Lemma E-low with k → i gives E_i(A) ≥ c_E||dA||² (the 2-form energy in own units equals
      PG's coarse-normalised one in d = 4); E_i is invariant under A ↦ A + dλ (it depends on its data mod Closed), so FP-ab
      applies; then E_i + (κ_i/2)||QA||² ≥ min(c_E, κ_i/2)(||dA||² + ||QA||²) and Proposition PG at n = L. ∎
    - (d) *What the per-level (NA) gap now reduces to.* At a small-field SU(N) background, the per-level fluctuation form
      is ½Hess E_i^{NA} + (κ_i/2)|Q_UA - Def(A)|² + (NA-alg corrections of relative size O(|ρ| + y²)). By (a)-(c) and
      |Q_UA - Def|² ≥ ½|Q_UA|² - |Def|², it is ≥ ½min(c_E, κ_i/4)c_1||A||²_B on the covariant one-level Phys_U provided
      (NA-H) ||Hess E_i^{NA} - Hess E_i||_{op} ≤ δ_H (the SU(N) effective energy's Hessian is close to the abelian one; part of
      B-NA, OPEN), the covariant orbit decomposition at n = L transfers by perturbation (finite-dimensional per block, n = L
      fixed; written only as "argued" in L5 [S14], OPEN as a written step), and the explicit smallness
      δ_H + (κ_i/2)L²·81p_L(e^{2η̄} - 1)² + O(|ρ| + y²) ≤ ½min(c_E, κ_i/4)c_1 (L² converts ℓ² to PG's ||·||²_B). No
      condition depends on n = L^k, i, k or T. **[R15-fix] Explicit smallness:** with δ_H = 0 and κ ≡ 1 (L = 3, p_L = 11,
      c_E = 0.004069, c_1 = 1/(3.5·10⁶)) the defect condition alone needs **η̄ ≲ 1.9·10⁻⁷** (c31 E3: 1.904·10⁻⁷), i.e. by the
      argued Stokes bound a background plaquette angle ≲ 1.6·10⁻⁸ in level-i units. It is uniform, so it is not a defect of
      the statement, but it shows that PG's constant c_1 sets the small-field threshold.
      **Status [R15-fix: narrowed; was "no longer an n-uniformity problem"]: the (NA) gap is OPEN. The top-level per-step
      defect has no n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA, plus a written per-block
      perturbation.**
  - **(R♯) stated in the §33 norms (target C).** For the SU(N) chain in Lie-algebra coordinates around the trivial
    background, in the per-level covariant slice, write the gradient remainder as 𝔑 = (𝔑_0, …, 𝔑_{k-1}) (level-l
    currents). **(R♯_ω):** for ||x||_{X_c,α} + ||B_k||_{D,m} ≤ ρ_0, there are level-l 2-forms 𝔊_l(x) and a plain level-0
    current 𝔥_0(x) with 𝔑_0 = d_0^*𝔊_0 + 𝔥_0 and 𝔑_l = d_l^*𝔊_l (l ≥ 1) such that
      max_lω_l||𝔊_l||_{∞,m} + [𝔊_0]_{α,m} + ||𝔥_0||_{∞,m} ≤ C_R(||x||_{X_c,α} + ||B_k||_{D,m})²,
    with Lipschitz bounds C_R(||x|| + ||x'|| + ||B_k||)||x - x'|| in the same norms, ω_0 = 1 and ω_l = L^{θ(k-l)} (l ≥ 1) for
    some θ ∈ (0, 1]. Status of its parts:
    - the level-0 Wilson term: the BCH plaquette remainder q_p (|q_p| ≤ 9s² in A1-NA(1) step 1, s the link size, PROVEN S6)
      gives 𝔊_0 ⊇ q(x) (divergence form: the variation of Σ_p⟨dx, q⟩ in its dx-slot) and 𝔥_0 ⊇ (∂q/∂x)^T(dx + q), of size
      |x||dx| in own units = O(||x||²_{X_c}) in coarse units (scaling count of BNA-F2, now in these norms): argued, not written;
    - the soft remainders at levels l ≥ 1 (NA-alg (a)-(b): O(y²) and O(|ρ|³) relative terms): of size L^{-(k-l)} or cubic in
      coarse units (BNA-F2), which fixes θ = 1 at best: argued, not written;
    - the plain current 𝔥_0 requires Lemma G♯_0-plain (OPEN) on the linear side; this is the reason it is listed separately.
    So (R♯_ω) is a precise statement, not a proven one; the inputs B-NA-red needs are now (G♯_0-field) with
    (G♯_0-fine) ⇐ (LED-src), Lemma G♯_0-plain, (R♯_ω), and (FP♯').
  - **Check c30** (criteria checks/c30_criteria.md, written before the script; disclosures in checks/c30_time.txt).
    - **Part A: PASS.** Every condition of η_* (now including the f_0 condition) and of η'_* holds at each corrected pair in
      30-digit arithmetic; bisection margins at the stated r_0 are +0.00004 to +0.00073.
    - **Part B: PASS.** The SRC-id f_0 lines at complex points (n = 3, 9, 27; κ = (0.5, 2) included): B1 4.4e-15, B2 3.1e-15,
      B3 5.2e-13.
    - **Part C: PASS.** SRC-all and REC against MINRES chains with random sources at every level: C1 ≤ 3.1e-10, C2 ≤ 9.7e-11,
      C3 ≤ 4.3e-9; C4 transport-bound ratios ≤ 0.33 (vacuous at k = 1).
    - **Part D (informational):** the soft constants quoted under Theorem G♯_0-soft; at d = 4, k = 2 a level-1 source gives
      L^{k-1-i}sup|r^c_i|/sup|G^c| = 4.64 at i = 0 against the proven 6/κ_0 = 6 of (b) (random-sign sources).
    - Resources: A 0.6 s, B 0.7 s, C 7 s / 0.51 GB, D 2.5 s / 0.51 GB; one job at a time, nice 10, BLAS threads 1, load ≤ 2.8,
      ≥ 43% free.

- **[S16] Session 16 (wind-down session 1 of 2 for the linear/abelian package): REVIEW_S15_CONVERGENCE job-1 fixes
  ([R15-fix]); Lemma F-df_0; c31; the write-up LINEAR_PACKAGE.md. Targets pre-stated in RTARGET.md §38 at 20:26 UTC,
  after the lead's exploratory reasoning (on paper; it found the route of Lemma F-df_0) and before any written
  session-16 derivation or check script. The c31 criteria were written before the script. Status of L5 unchanged:
  IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE (unreviewed): Lemma F-df_0. No new SU(N) obligation is opened.
  - **Lemma F-df_0 (an exponentially local F-representative of the fine-curvature map): PROVEN-HERE.** Setting and
    notation of Theorems N2-exp/N2-exp' (d = 4, L ≥ 3 odd, n = L^k, κ_- ≤ κ_i ≤ κ_+); coordinates α = 1, …, 4;
    ν_α(p) := e^{ip_α} - 1. Fix a fine offset u. Let 𝔅(p) be the B_k-symbol of f_0 at offset u: for every plane (ρ, σ),
    f̂_0(n· + u)_{ρσ}(p) = Σ_v𝔅^v_{ρσ}(p)b̂_v(p) (LED-symb; a T-independent function of p, sampled on each torus grid). By
    Theorem N2-exp' (i), every entry of 𝔅 is analytic and 2π-periodic on S := {|Im p_α| < m_*' ∀α}, with |𝔅| ≤ M there,
    M = M(L, κ_±). For a function g on S define
    - (E_{<α}g)(p) := g(0, …, 0, p_α, …, p_4) (the first α - 1 coordinates set to 0; E_{<1} = id), so E_{<α+1} = E_α∘E_{<α}
      with E_α the evaluation at p_α = 0;
    - (T_αg)(p) := (g(p) - (E_αg)(p))/ν_α(p_α), extended by continuity to p_α ∈ 2πZ;
    and for α < β the 6-vector (over output planes) **h_{αβ} := T_αE_{<α}𝔅^β**, with h_{βα} := -h_{αβ}, h_{αα} := 0. Let
    𝒦^{ax}_u be the linear map on coarse 2-forms with symbol F̂ ↦ Σ_{α<β}h_{αβ}(p)F̂_{αβ}(p). Then, uniformly in k ≥ 1, T
    and u:
    - (i) **𝒦^{ax}_u(dB_k) = f_0(n· + u) for every B_k** (every torus side T): 𝒦^{ax}_u is an extension to ALL coarse 2-forms
      of the fine-curvature map F ↦ f_0, which is defined on exact F only;
    - (ii) for every 0 < m' < m_*', every entry of h is analytic and 2π-periodic on {|Im p_α| ≤ m'} with
      **|h| ≤ M_ax := max(2, (π/2)e^{m'}/(m_*' - m'))·M ≤ 2M/(m_*' - m')**, hence every entry of the infinite-lattice kernel
      obeys **|K^{ax}_u(X)| ≤ M_ax e^{-m'|X|_1}**, and the torus kernel is its periodisation;
    - (iii) with Corollary N2-exp-b (𝓡: F ↦ r_{k-1} is exponential on all 2-forms), both gauge-invariant outputs of the
      linearised chain, r_{k-1} and f_0, have exponentially decaying kernels as functions of the coarse curvature F on
      all 2-forms, at every rate m' < m_*' (= 0.0384 at L = 3, κ ≡ 1).
    *Proof.*
    - (0) *Gauge invariance of the symbol.* f_0 depends on B_k only through dB_k (Lemma N2-a), so b̂ = νt̂ gives f̂_0 = 0:
      Σ_vν_v(p)𝔅^v(p) = 0 at every grid point p ≠ 0 of every torus. The union of the grids over T is dense in [-π, π]⁴ and
      both sides are analytic on S, so **Σ_vν_v𝔅^v ≡ 0 on S**.
    - (1) *E and T preserve analyticity, periodicity and bounds.* E_{<α} evaluates some variables at the real point 0 ∈ S,
      so E_{<α}g is analytic and periodic in the remaining variables on the same strip, with sup not increased. For T_α,
      fix the other variables and write g(w), w = p_α, analytic and 2π-periodic on |Im w| < m_*', |g| ≤ M. In the strip
      ν(w) = e^{iw} - 1 vanishes exactly at w ∈ 2πZ, with simple zeros, and g(w) - g(0) vanishes there too (periodicity);
      so T_αg is analytic (removable singularities) and periodic. Bound on |Im w| ≤ m', with Re w reduced to [-π, π]:
      - if |Re w| ≥ π/2: Re e^{iw} = e^{-Im w}cos(Re w) ≤ 0, so |ν(w)| ≥ 1 and |T_αg| ≤ 2M;
      - if |Re w| ≤ π/2: g(w) - g(0) = w∫_0^1g'(tw)dt (the segment stays in |Im| ≤ m'), |g'| ≤ M/(m_*' - m') (Cauchy on
        discs of radius m_*' - m'), and ν(w) = iw∫_0^1e^{itw}dt with Re∫_0^1e^{itw}dt = ∫_0^1e^{-tIm w}cos(tRe w)dt ≥
        e^{-m'}∫_0^1cos(tπ/2)dt = (2/π)e^{-m'}, so |ν(w)| ≥ (2/π)e^{-m'}|w| and |T_αg| ≤ (π/2)e^{m'}M/(m_*' - m').
      Each h_{αβ} uses one T and one E, so (ii)'s bound holds; m' ≤ m_*' ≤ 0.1 gives (π/2)e^{m'} ≤ 2 and 1/(m_*' - m') ≥ 1.
    - (2) *Factorisation.* For every v, **𝔅^v = Σ_μν_μh_{μv}**. Telescope: 𝔅^v = Σ_{α<v}(E_{<α} - E_{<α+1})𝔅^v + E_{<v}𝔅^v,
      and (E_{<α} - E_{<α+1})g = (1 - E_α)E_{<α}g = ν_αT_αE_{<α}g, so the first sum is Σ_{α<v}ν_αh_{αv}. For the last
      term apply E_{<v} and E_{<v+1} to (0); since ν_μ(0) = 0 for μ < v and ν_μ (μ ≥ v) does not depend on the evaluated
      variables: ν_vE_{<v}𝔅^v + Σ_{μ>v}ν_μE_{<v}𝔅^μ = 0 and Σ_{μ>v}ν_μE_{<v+1}𝔅^μ = 0. Subtracting,
      ν_vE_{<v}𝔅^v = -Σ_{μ>v}ν_μν_vT_vE_{<v}𝔅^μ = -ν_vΣ_{μ>v}ν_μh_{vμ}; divide by ν_v (an identity of analytic functions
      off the null set {ν_v = 0}, hence everywhere): E_{<v}𝔅^v = Σ_{μ>v}ν_μh_{μv}. (For v = 4 this reads E_{<4}𝔅^4 = 0.)
    - (3) *(i).* With (dB)^_{αβ} = ν_αb̂_β - ν_βb̂_α: Σ_{α<β}h_{αβ}(ν_αb̂_β - ν_βb̂_α) = Σ_vb̂_vΣ_μν_μh_{μv} (antisymmetry of h)
      = Σ_v𝔅^vb̂_v = f̂_0 at every grid point p ≠ 0; at p = 0 both sides vanish (F̂(0) = 0 for exact F; f̂_0(0) = 0 since
      r̂(0) = 0 and the alias terms vanish there, LED-symb).
    - (4) *(ii)-(iii).* Paley-Wiener (periodic form, as in Theorem N2-exp) gives the kernel bound from (1); periodisation is
      Poisson summation (as in Lemma WA). (iii) adds Corollary N2-exp-b. ∎
    - *Remarks.* (a) The representative is not unique (any two differ on non-closed F only). It is neither the Coulomb
      representative 𝔅∘d^*/ψ nor the session-12 𝒦̂_u + Π_coex; those are non-analytic at p = 0 (power tails, LED-unif and
      c28 C5). This answers Corollary N2-exp-b's open question: an exponentially local global F-representative of f_0
      exists, explicitly. (b) It depends on the order of the coordinates; the average over the 24 orders is again a
      representative with the same bound and is permutation covariant. (c) What is proven is the statement in the
      parenthesis of the [R1314-fix] note (an exponential kernel for the fine-curvature response as a function of the
      coarse curvature on ALL 2-forms); the route via dΠ_ex sketched there is not used, and the name is kept. (d) This
      supplies the linear input that Corollary N2-exp-b's ARGUED note "what N6 consumes" asked for; how N6 uses it is part
      of N6 (OPEN), which also needs N5 and the non-linear chain. (e) c31 F: the factorisation identity (2)-(3) holds on
      the actual f_0 B_k-symbol to ≤ 5.0e-16 (relative) at 4 cases (T = 8; k = 1, 2; u = 0, (1, 0, 0, 0), (2, 1, 0, 0)),
      with gauge invariance (0) to ≤ 3.7e-16; PASS. The strip bound (ii) is not tested numerically.
  - **Check c31** (criteria checks/c31_criteria.md, written before the script; disclosures in checks/c31_time.txt).
    - **Part E: PASS.** E1 (symbol level, exact per-mode minimum of E_k/||dB_k||² over closed data): 0.03095, 0.02974,
      0.02963 at κ ≡ 1 (T = 16, 16, 12; k = 1, 2, 3), i.e. 7.6, 7.3, 7.3 × c_E = 0.004069, attained at p = (π, π, π, π);
      0.05242 = 9.1 × c_E (0.005791) at κ = (0.5, 2). E2 (chain level, LSMR, d = 4; (T, k) = (3, 1), (2, 2), (2, 2) with
      κ = (0.5, 2)): random data 0.049-0.088, the minimising single mode 0.0408, 0.0297, 0.0524, every ratio ≥ 7.3 c_E; the
      single-mode chain ratio equals the symbol value to ≤ 6.5e-15; normal-equation residuals ≤ 6.2e-14. E3: c_E =
      0.0040691; the NA-lev smallness η̄ ≤ 1.904·10⁻⁷, plaquette angle ≤ 1.587·10⁻⁸.
    - **Part F: PASS** (above).
    - Resources: E 7.9 s / 457 MB; F 0.6 s / 71 MB; one job at a time, nice 10, BLAS threads 1, load ≤ 4.2 before each
      run, ≥ 34% free; run without -I (disclosed, as c29/c30).

### L6. UV stability: IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** exp(-E_- |T|) ≤ Z_K / Z_K^ref ≤ exp(E_+ |T|), uniformly in K, with bulk dependence on
  the torus size.
- **Dimock's scalar analogue [v-abs, introduction read]:** torus (L^-N Z / L^M Z)^3, bounds "uniform in the ultraviolet
  cutoff N and with bulk dependence on the volume parameter M" (Dimock, arXiv:1212.5562; see also 1108.1335 and
  1304.0705; part III proves "convergence of the expansion" for the stability bound, not of correlations).
- **Correction to review.md §1.** "Small physical volume" is probably a misreading. The restriction is that the
  coupling be small at the stopping scale; the torus side in stopping-scale units is arbitrary (M is arbitrary). Status:
  pending the Balaban primary text.
- **[S5]** Upgraded to [read]: Dimock I Theorem 1 (p.2, eq. 7) and III Corollary 1 (p.33, eq. 225) give
  exp(∓λ^η Vol(T_M)) bounds for all M, N (φ⁴_3, arbitrary volume); QED Theorem 2 (2009.01156 p.8, eq. 42) gives
  1/2 ≤ Z/Z(0) ≤ 3/2 in unit volume, "works equally well for any finite volume" (2204.07201 p.2-3). For 4D SU(N): still
  IMPORTED-NOT-YET-REVERIFIED (CMP 109/116/119/122 bodies not read).
- **[S6]** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
  - CMP 109 [read] proves only the small-field half, and only modulo CMP 116 for the localisation. Its bulk bound
    (0.30), |E_k(U_k)| ≤ O(1)(1 - L^{-α})^{-1}M^{-4}|T_1^{(k)}|, is the small-field form of L6, conditional on
    L4a-form.
  - The torus in (0.1) has side 2L^m in unit-lattice units, with m arbitrary. So, as in Dimock's φ⁴_3, nothing in CMP
    109 restricts the physical volume to be small. This answers the review.md §1 question at the level of the
    small-field theorem; it does not settle it for the full L6.
  - Theorem 1 assumes only 0 < g_k ≤ γ, not asymptotic freedom (p.259).

### L6loc. Local, volume-uniform large-field suppression: E8 as stated is FALSE for SU(2), SU(3) with D (fixed bare g: unconditionally; tuned g: conditional on L4a) [S3, R3-fix]; the fine-scale local bound is PROVEN-HERE; the scale-local replacement E8* is OPEN (fixed-depth cases PROVEN-HERE [S4])
- **Estimate E8 (session-1 form).** There is δ(g) → 0 as g → 0 such that, for every K ≥ m, every M, and every
  resolution-m block B, μ_{K,M}(some averaging step K → m leaves D inside B) ≤ δ(g).
- **[S3] Verdict.** E8 in this form fails: Proposition E8.3 below proves that, along any sequence with β_K ≤ λK and λ
  below an explicit λ_c, the probability that some *first* step (K → K-1) leaves the domain inside B tends to 1. The AF
  rate of the tuned coupling (imported, L4a) lies below λ_c for SU(2) and SU(3) with the domain D. **[R3-fix]** The
  session-3 text also said "for every N with the τ_N/2 thresholds"; that concerns the stronger event "all steps within
  τ_N/2", which is not E8 and not what E7.0 needs. For SU(4) with D the crude bound is undecided; for N ≥ 6, t = 1 is
  inadmissible in the conditional lemma; D_N (N ≥ 7) is not covered. **[R3-fix] Reading of "g".** If g in E8 is a fixed
  bare coupling, E8 is false unconditionally (a fixed β is ≤ λK for all large K, so sup_K μ = 1). If g is the running
  coupling along the tuned sequence, the failure needs β_K ≤ λ_c K, i.e. the imported L4a rate: false conditional on L4a.
  Lattice-scale domain failures are dense in physical space in the continuum limit: their
  number per unit physical volume grows like L^{(4 - a)K} with a < 4. So "all steps succeed" is the wrong event, and the
  right object is a per-scale-block (Peierls-type) bound, E8* below.

**Setting for E8.1-E8.3.** Wilson SU(N) action S3 on a fine torus Λ = (Z/2mZ)^4 in lattice units (even side, as in the
[S3] torus convention; m ≥ 1), at any β ≥ 0. Cells C_t = t + [0,1]^4 (closed unit cubes), t ∈ Λ. For η > 0,
G_t := 1[max_{p ⊂ C_t} ||1 - U_p|| ≥ η] ("cell t is η-bad"). h_N(δ) := Haar{U : ||U - 1|| ≤ δ}.

**E8.1. Chessboard bound at the cutoff scale: PROVEN-HERE (given L9a, site reflection, on the even torus).** [R3-fix:
attribution] This is a special case of the Fröhlich-Israel-Lieb-Simon chessboard estimate (J. Fröhlich, R. Israel,
E. H. Lieb, B. Simon, "Phase transitions and reflection positivity. I", CMP 62 (1978) 1-34 [v-R4]); the special case is re-derived below, so nothing rests on the citation.
- **(i)** For every set R of cells, μ(all cells of R are η-bad) ≤ q̄(η)^{|R|}, with q̄(η) := μ(all cells η-bad)^{1/|Λ|}.
- **(ii)** For every δ ∈ (0, 1/2]: q̄(η) ≤ exp(-βη^2/(8N) + 48βδ^2) h_N(δ)^-4.
- **(iii)** h_N(δ) ≥ (κ_N δ)^{N^2-1} for δ ≤ 1/2, with κ_N > 0; for SU(2), h_2(δ) ≥ (8/(3π^3)) δ^3. With δ^2 = 1/(8β)
  (β ≥ 1/2), SU(2): q̄(η) ≤ e^6 (3π^3/8)^4 (8β)^6 e^{-βη^2/16}. In terms of g^2 = 2N/β the decay is e^{-η^2/(4g^2)}.
- **Proof of (i) (chessboard estimate, special case re-derived).**
  - Equivariance: a reflection θ through a site plane maps cell C_t onto a cell C_{t'} and its plaquette set onto that of
    C_{t'}, and ||1 - U_p|| is invariant under the orientation reversal U_p → U_p^dag-conjugates. So θ(G_t) = G_{t'}.
  - Regularise: G^ε_t := G_t + ε. For H ⊂ Λ put a(H) := E[Π_{t∈H} G^ε_t] and ρ(H) := a(H)/a(Λ)^{|H|/|Λ|} > 0.
  - Doubling inequality. Let θ be the site reflection through x_j = k (and its antipode x_j = k + m), with halves
    Λ_± of m cell-slabs each. Write Π_{t∈H} G^ε_t = A·θ(B), with A = Π_{H∩Λ_+} G^ε (measurable on the closed positive
    half, which includes the plane links) and B = θ(Π_{H∩Λ_-} G^ε). RP (L9a, site reflection) gives the Cauchy-Schwarz
    inequality E[Aθ(B)] ≤ E[Aθ(A)]^{1/2} E[Bθ(B)]^{1/2}. Here E[Aθ(A)] = a(H_+), with H_+ := (H∩Λ_+) ∪ θ(H∩Λ_+), and
    similarly a(H_-); |H_+| + |H_-| = 2|H|. Hence ρ(H) ≤ ρ(H_+)^{1/2} ρ(H_-)^{1/2}.
  - So if H maximises ρ over the finite set of subsets, then H_+ and H_- are maximisers too.
  - Reaching a constant pattern. In direction 1, let P_s be the transverse pattern of slab s; a reflection maps P_s to
    the mirrored slab unchanged. Take a maximal cyclic run of equal consecutive P_s, of length ℓ < 2m, and reflect
    through the plane at its end, keeping the half that contains the run. The new maximiser has a run of length
    ≥ 2 min(ℓ, m) > ℓ. Iterate until the pattern is constant in direction 1. Reflections in directions 2, 3, 4 preserve
    constancy in direction 1; repeat. The end is a maximiser that is ∅ or Λ, and ρ(∅) = ρ(Λ) = 1.
  - So ρ ≤ 1, i.e. a(H) ≤ a(Λ)^{|H|/|Λ|}. Let ε → 0 (dominated convergence). ∎
- **Proof of (ii).** If every cell is bad, there are at least |Λ|/4 distinct bad plaquettes, since a plaquette lies in
  at most 4 closed unit cubes (2 choices in each of the 2 transverse directions). With eigenvalues e^{iθ_j},
  1 - N^-1 Re tr U = N^-1 Σ(1 - cos θ_j) ≥ ||1 - U||^2/(2N). So on that event S ≥ β(|Λ|/4)η^2/(2N); Haar has mass 1.
  For the denominator, restrict to all links in the δ-ball: then ||1 - U_p|| ≤ 4δ and 1 - N^-1 Re tr U_p ≤ 8δ^2 for all
  6|Λ| plaquettes, so Z ≥ e^{-48βδ^2|Λ|} h_N(δ)^{4|Λ|}. Take the |Λ|-th root. ∎
- **Proof of (iii).** For X ∈ su(N), ||e^X - 1|| ≤ ||X||, so exp maps the operator-norm δ-ball of su(N) into the
  δ-ball of SU(N). exp is injective on ||X|| < π with a continuous positive Haar Jacobian on ||X|| ≤ 1/2, and the
  Lebesgue volume of the δ-ball is v_N δ^{N^2-1}. SU(2): class angle θ (eigenvalues e^{±iθ}) with density (2/π) sin^2 θ and ||U - 1|| = 2 sin(θ/2);
  h_2(δ) = (θ_δ - sin θ_δ cos θ_δ)/π with θ_δ = 2 arcsin(δ/2) ≥ δ, and sin θ ≥ 2θ/π gives ≥ (8/(3π^3))δ^3. ∎
- **Check c10(A)** (exact 2D U(1), tori 4×4 and 6×4, 90 cases): μ(R bad) ≤ q̄^{|R|} holds (max ratio 1.0000, attained at
  R = Λ). In 2D U(1) the plaquettes are exchangeable, so this tests the inequality, not the geometry. c10(B): the SU(2)
  ball bound holds with ratio ≈ 2.3-2.5.

**E8.2. One-step local ratio bound for S4': PROVEN-HERE (given E8.1).**
- Let b' = (X, X + e_μ) be a first-step coarse link (blocks of side L in lattice units) and F_{b'}(t) the event that some
  Z^σ_y = S_{c_X}^-1 T^σ_y (any order σ, any y ∈ B(X)) has ||Z^σ_y - 1|| ≥ t. Put A_L := (d-1)L(L-1)/2 (= 9 for L = 3,
  d = 4).
- **Claim.** μ(F_{b'}(t)) ≤ 2L^4 q̄(t/A_L). For first-step links b'_1, ..., b'_r whose two-block regions are pairwise
  site-disjoint, μ(all F_{b'_i}(t)) ≤ (2L^4 q̄(t/A_L))^r. Both are uniform in the volume and in K.
- **Proof.** The ribbon decomposition of L1e in lattice units: the loop of Z^σ_y is a product of conjugated plaquettes of
  the planar grids between γ (the order-σ axial path, inside B(X)) and γ + Le_μ, all inside the two-block region, and
  there are Σ_{ν≠μ} |γ_ν| L ≤ A_L of them. So ||Z^σ_y - 1|| ≤ A_L max_p ||1 - U_p||, and F_{b'}(t) forces some plaquette in
  the region with ||1 - U_p|| ≥ t/A_L; assign it to the cell whose lower corner is the plaquette's lower corner (≤ 2L^4
  cells). Union bound, then E8.1(i). For r links, sum over one cell per link; disjoint regions give distinct cells. ∎
- With β = 2N/g^2 this is the per-block e^{-c/g^2} bound: μ(F_{b'}(t)) ≤ C_N(L, β) exp(-t^2/(4A_L^2 g^2)), where C_N is
  polynomial in β. For L = 3, t = 1: c = 1/324. Explicit but small.
- **Check c10(E):** max over all 24 orders and 81 y of ||Z - 1|| = 0.673 ≤ 9 × 0.507 for one random SU(2) field.
- **Scope.** First step only. E8.1 uses RP of the *fine* Wilson measure under site reflections. For j < K-1 the law of
  V^(j+1) is RP only under block-boundary (link-plane) reflections (L8c); a site reflection through a block mid-plane
  cuts a block, so the coarse chessboard argument does not go through as it stands. OPEN.

**E8.3. Lower bound: lattice-scale failures are dense: PROVEN-HERE (the inequality); the AF reading is CONDITIONAL on the
imported AF rate (L4a).**
- **Lemma (second order at the maximum).** For W ∈ C^{N×N} with ||W|| ≤ w and f(U) = Re tr(UW), let U_* maximise f over
  SU(N). Then f(U_*) - f(U_* e^X) ≤ (N w/2) ||X||^2 for all X ∈ su(N).
  - Proof: the first variation Re tr(U_* X W) vanishes for all X ∈ su(N) (interior maximum). The remainder is
    -Re tr(U_*(e^X - 1 - X)W), with ||e^X - 1 - X|| ≤ ||X||^2/2 (X normal, |e^{iθ} - 1 - iθ| ≤ θ^2/2) and
    |tr(MW)| ≤ ||M|| ||W||_1 ≤ N ||M|| ||W||. ∎ For a Wilson staple sum, w = 2(d-1), giving N(d-1)||X||^2. Check c10(C):
    max ratio 0.74.
- **Lemma (conditional lower bound).** Let b be a fine link and condition on all other links. The conditional law of U_b
  is ∝ exp((β/N) Re tr(U_b W)) dHaar, with W the staple sum. For any R' ∈ SU(N), t > 0 and δ ∈ (0, 1/2] with t + 3δ ≤ 2 (SU(2)), resp. t + 3δ < 2 sin(π/N) (N ≥ 3, so that
  the principal logs below are traceless by L1b and the first lemma applies):
  P(||U_b - R'|| ≥ t | rest) ≥ q_-(β) := h_N(δ) exp(-β(d-1) x^2), x := 2 arcsin((t + 3δ)/2).
  - Proof: let U_* maximise f. If ||U_* - R'|| ≥ t + δ, take the set A' = U_* · Ball(1, δ). Otherwise U_* = R' e^Z with
    Z normal. In the eigenbasis of Z put Y = i a diag(1, -1, 0, ...), with |a| chosen and signed so that the top
    eigenphase ζ_1 of Z + Y has modulus w_0 = 2 arcsin((t + 2δ)/2) [R3-fix: ζ_1 is chosen as an eigenphase of Z of
    largest modulus, and sign(0) := +1]: a = sign(ζ_1)(w_0 - |ζ_1|), so |a| ≤ w_0 and the
    shifted second eigenphase also has modulus ≤ w_0. Y commutes with Z, so W_0 := U_* e^Y = R' e^{Z+Y}
    has ||W_0 - R'|| ≥ t + 2δ. Take A' = W_0 · Ball(1, δ) ⊂ {||U - R'|| ≥ t}.
  - In both cases each U ∈ A' is U_* e^{X'} with ||e^{X'} - 1|| ≤ t + 3δ, so ||X'|| ≤ x. Haar(A') = h_N(δ), and
    ∫ e^{(β/N) f} ≤ e^{(β/N) f(U_*)}, so P ≥ h_N(δ) e^{-(β/N) N(d-1) x^2} by the first lemma. ∎
  - Check c10(D) (SU(2), 18 random (W, R') cases, 4e5-sample MC): the bound holds in every case (max lb/p = 1.2e-4); it
    is very far from sharp.
- **Proposition E8.3.** Fix t ∈ (0, 2) and δ as above. Let B be a resolution-m block, with fine side L^{K-m}. Then
  μ_{K,β}(no first-step failure F_{b'}(t) inside B) ≤ exp(-q_-(β) L^{4(K-m-1)}/3) for K - m ≥ 2.
  - Proof: take the first-step links b' = (X, X + e_1) with X_1 even and X, X + e_1 inside B. Their two-block regions
    are disjoint, and there are ⌊s/2⌋ s^3 ≥ s^4/3 of them, s = L^{K-m-1} ≥ 3. In each, choose y_0 with a transverse coordinate
    different from c_X and y_{0,1} ≤ c_{X,1}, and let b be the last fine link of the straight leg S_{y_0}. Then b occurs
    exactly once in Z^{σ_0}_{y_0} (it is not on S_{c_X}, not in the axial path inside B(X), and not in the axial path in
    B(X + e_1), which reaches y_0 + Le_1 from above or not at all in coordinate 1), and in no other chosen Z. Writing
    Z = A U_b B, the event ||Z - 1|| ≥ t is ||U_b - A^-1 B^-1|| ≥ t. Condition successively on all links but b_r, then
    b_{r-1}, ...: the other events do not involve U_{b_r}, so each factor is ≤ 1 - q_-. Use 1 - q ≤ e^{-q}. ∎
- **Corollary (AF window).** If β_K ≤ λK with 3 λ x^2 < 4 ln L, then L^{4K} q_-(β_K) → ∞, so for each fixed m and B the
  probability that some first-step averaging inside B fails tends to 1 as K → ∞.
  - With the AF rate β_K ≈ 4N b0 K ln L (imported, L4a; b0 = 11N/(48π^2)), the condition reads 3 x^2 · 4N b0 < 4.
  - In the limit δ → 0 (c10(F)): with t = 1 (the S4 domain, N ≤ 6) the value is 1.22 (SU(2)) and 2.75 (SU(3)), so dense;
    SU(4) gives 4.89, undecided by this crude bound. [R3-fix] The relevant threshold for E7.0 is t = 3τ_N/4 (ζ = 0
    only when some ||Z - 1|| ≥ 3τ_N/4); recomputed (check c13(R)): 0.659 (N = 2), 1.482 (3), 2.635 (4), 4.117 (5),
    5.929 (6), 6.000 (7), 6.097 (10), → 6.19 (N → ∞). So dense for N = 2, 3, 4 only; N ≥ 5 undecided. (The session-3
    values at t = τ_N/2 bound the wrong event: {all < τ_N/2} ⊂ {all < 3τ_N/4}.)
- **Consequences.**
  - **E7.0 fails in the AF window for N = 2, 3, 4 [R3-fix].** E_K[w̃] ≤ E_K[ζ] ≤ μ(no failure at threshold **3τ_N/4**
    in the four resolution-0 blocks of p) → 0 along every sequence with β_K ≤ λK, 3λx^2 < 4 ln L, x = 2 arcsin(3τ_N/8).
    So the RC of S5 at fixed w* > 0 forces β_K > λK eventually: a bare coupling weaker than the AF rate (for SU(2),
    λ_c/λ_AF ≈ 6.1 at δ → 0; session 3 wrote 14, from the wrong threshold). For these N, S5 is not a viable
    renormalisation condition along AF-rate sequences. E7.0 as stated (sup over all β) is NOT falsified; only its
    AF-window restriction is (it is not excluded for β ≫ K, which is not the physical regime). For N ≥ 5: undecided.
  - **E8 as stated is FALSE** for SU(2) and SU(3) with D: unconditionally if g is a fixed bare coupling, and
    conditional on L4a's rate if g is the tuned running coupling (see the verdict above). SU(4) with D: undecided.
  - The session-3 off-D extension "failed link := 1" is then not harmless: it would be used on a dense set of fine
    links. [R3-fix] It is withdrawn; the single extension used from session 4 on is S4'' with the odd branch rule (S4).

**S5'. [S3] Repaired renormalisation condition: per-K tuning PROVEN-HERE; K-uniformity reduced to a β = 0 Haar
statement (E7.0', OPEN).**
- Use the everywhere-defined map S4'' and the plain observable w(V^(0)_p) = 1 - N^-1 Re tr V^(0)_p, with no cut-off.
  Tune E_{K,β_K}[w(V^(0)_p)] = w*.
- **Per K: PROVEN-HERE.** w ∘ V^(0) is bounded and measurable, so β ↦ E_{K,β}[w] is continuous (dominated convergence).
  As β → ∞ the measure concentrates on the flat set (Laplace), where every Z = 1; w ∘ V^(0) is continuous on a
  neighbourhood of the flat set (far from the branch set) and vanishes on it (zero-winding argument of L7.0), so
  E_{K,β}[w] → 0. At β = 0 the value w_0(K) := E_Haar[w(V^(0)_p)] is > 0. IVT: every w* ∈ (0, w_0(K)) is attained.
- **E7.0' (OPEN, now a pure Haar statement):** liminf_K w_0(K) > 0. It no longer involves large-field suppression:
  at β = 0 the fine links are i.i.d. Haar. [R3-fix] E7.0' is SUFFICIENT for a K-uniform w*, not equivalent to it
  (sup_β E_{K,β}[w] may exceed w_0(K)).
- **[R3-fix] Open, unflagged in session 3: AF compatibility of S5'.** Nothing shows that the S5'-tuned β_K follow the
  AF rate. By E8.3, first-step outputs are out of domain on a dense set at AF couplings, and S4'' then averages
  out-of-domain logs; S5' could force β_K ≫ AF by a mechanism like the one that defeats S5. "Repair" was premature:
  S5' is a candidate RC whose per-K tuning is proven and whose AF compatibility is OPEN (estimate E7.0'-AF).
  - Check c12 (finite diagnostic, SU(2), L = 3, MC): w_0 = 0.996 ± 0.017 (K = 1, S4''), 0.993 ± 0.008 (K = 1, fixed
    order), 0.980 ± 0.013 (K = 2, fixed order), 1.03 ± 0.02 (K = 2, S4'', 2 samples). About 77.5% of the first-step Z lie
    outside ||Z - 1|| < 1 at β = 0, so the extension S4'' is used almost everywhere there. Two values of K say nothing
    about the liminf. [R3-fix] The K = 2 S4'' value rests on 2 configurations; its error bar (from 96 correlated
    plaquettes) is not credible. The 77.5% matches exact Haar: Z is Haar unless y differs from c_X only in coordinate μ
    (Z ≡ 1, 3 of 81 sites), and P_Haar(||U - 1|| ≥ 1) = 0.8045, so 78/81 × 0.8045 = 0.775 (REVIEW_S3).
  - Heuristic (not a proof): at β = 0 the out-of-domain logs are spread over the ball of radius π, so the averaged log is
    small and V ≈ the reference, and the coarse plaquette is close to the holonomy of a large loop of nearly independent
    Haar links, whose trace has mean 0. That would give w_0 → 1. The dependence between overlapping paths is what a
    proof has to control.
- **[S4] Lemma H0 (crossing-link structure): PROVEN-HERE.** Let b = (X, X + e_μ) be a coarse link of one S4''-step. For
  each transverse line ℓ (the L^{d-1} lines in direction μ through B(X)), let u_ℓ be the unique link of the straight legs
  S_y, y ∈ ℓ, that crosses the face between B(X) and B(X + e_μ) (the same link for all y ∈ ℓ). Then:
  - (a) for y on the centre line ℓ_0, every Z^σ_y ≡ 1 identically (all axial paths from c_X to y are straight, and T^σ_y
    backtracks to S_{c_X});
  - (b) for ℓ ≠ ℓ_0 and y ∈ ℓ, Z^σ_y = S_{c_X}^-1 α_{yσ} u_ℓ β_{yσ}, with α, β products of in-block links (L0), and
    u_ℓ occurs in no other Z of b, in no Z or reference of any other coarse link, and not in S_{c_X};
  - (c) u_{ℓ_0} occurs only in S_{c_X} (and in the identically trivial Z of (a)).
  - Proof: straight legs cross exactly one block face, at the transverse position of their line; axial paths stay in
    their block (L0); distinct coarse links own distinct faces. ∎
- **[S4] Lemma H1 (one step from i.i.d. Haar): PROVEN-HERE.** If the input links are i.i.d. Haar on SU(N), the S4''
  output (odd branch rule) is V'_b = W_b e^{X̄_b} with W_b := S_{c_X}, and:
  - (i) the W_b are i.i.d. Haar (products of L i.i.d. Haar links over pairwise disjoint link sets);
  - (ii) E||X̄_b||_HS^2 ≤ m_N (L^{d-1} - 1) / L^{2(d-1)}, with m_N := E_Haar||Π_0 log U||_HS^2 (Π_0 the traceless
    projection; m_2 = 2π^2/3 - 1 = 5.58; m_N ≤ Nπ^2);
  - (iii) w_0(K = 1) ≥ 1 - 4 (m_N (L^{d-1} - 1))^{1/2} / L^{d-1}.
  - Proof. X̄ = avg_{(y,σ)} Π_0 log Z^σ_y in both branches of S4'' (on D' each log is already traceless, L1b). Let G be
    the σ-algebra of all links except {u_ℓ : ℓ ≠ ℓ_0}. Given G, the u_ℓ (ℓ ≠ ℓ_0) are i.i.d. Haar (product measure),
    so by H0(b) each Z^σ_y with y ∈ ℓ is conditionally Haar, and E[Π_0 log Z | G] = 0 (Haar is inversion invariant,
    and Π_0 log is odd for every Z by the odd branch rule). The line averages W_ℓ := (1/n) Σ_{y∈ℓ,σ} Π_0 log Z^σ_y
    (n = d! L^d) are conditionally independent and centred, and the centre line contributes 0 (H0(a)). By Jensen within
    a line, E[||W_ℓ||^2 | G] ≤ (L d!/n)^2 m_N = m_N L^{-2(d-1)}. Summing over the L^{d-1} - 1 lines gives (ii).
    For (iii): W_p := W_1 W_2 W_3^-1 W_4^-1 is Haar by (i), so E N^-1 Re tr W_p = 0, and
    |N^-1 Re tr V'_p - N^-1 Re tr W_p| ≤ ||V'_p - W_p|| ≤ Σ_i ||e^{X̄_i} - 1|| ≤ Σ_i ||X̄_i||_HS; Cauchy-Schwarz and (ii). ∎
  - The bound (iii) is useful only when 16 m_N (L^{d-1}-1) < L^{2(d-1)}. **[R4-fix]** The range L ≥ 5 below is for SU(2)
    only; m_N grows with N (m_N ≤ Nπ^2), so larger N needs larger L. For SU(2), d = 4, L ≥ 5 (w_0(1) ≥ 0.16 at L = 5,
    ≥ 0.49 at L = 7); it is vacuous at L = 3, where c12 measures 0.996.
  - Check c14 (H1a-c, 12/12): measured E||X̄||_HS^2 = 0.043 (bound 0.199; d = 4, L = 3), 0.186 (0.551; d = 3, L = 3),
    0.044 (0.214; d = 3, L = 5), 0.637 (1.240; d = 2, L = 3); the straight-transporter plaquette is Haar within 4 s.e.
- **[S4] Why H1 does not iterate, and the sufficient reduction (OPEN).** After one step the field is W e^{X̄}, not Haar,
  and H1's proof uses exactly that the crossing links are conditionally Haar. What survives at every level is H0's
  independence: conditional on all fine links except one designated fine crossing link per level-j crossing link, the
  level-j crossing links are conditionally independent (each is a function Φ_b(u*_b; G) of its own designated fine
  link, by H0(b)-(c) applied at each level). What is lost is centring: the conditional law λ_b = Φ_b#Haar need not be
  Haar (in the domain, Φ_b is nearly constant: the averaged log pulls V toward the mean of the T's).
  - **E7.0'-TV (sufficient condition, OPEN).** If, for every K, the conditional laws λ_b of the level-1 crossing links
    (the input of the last step 1 → 0) satisfy TV(λ_b, Haar) ≤ τ, then the H1 argument at the last step
    gives w_0(K) ≥ 1 - 4(√((m_N + 2τNπ^2)/L^{d-1}) + 2πτ√N) - 2τ (bias of each centred term ≤ 2τ||Π_0 log||_∞ ≤ 2τπ√N; the bias adds
    coherently over lines, the centred part as in H1). So E7.0' ⇐ E7.0'-TV with τ small and L large. Neither the TV
    closeness nor its K-uniformity is proven.
  - Diagnostic c14 (d = 2, L = 3, β = 0; no criterion): w_0(K) = 0.994 ± 0.014, 1.030 ± 0.027, 0.985 ± 0.030,
    0.998 ± 0.034, 0.905 ± 0.067 for K = 1..5 (400/100/60/40/12 samples; coarse torus side 2); first-run values with 4
    samples at K ≥ 3 kept in c14_out_firstrun.txt. Consistent with w_0 ≈ 1, nothing about the liminf, and d = 2 only.
- **Price.** S4'' is discontinuous on the branch set. Weak-limit arguments that pass A through the limit (consistency
  A_*ν_{m+1} = ν_m) need ν_{m+1}-small mass near the branch set *at level m+1*. That is exactly E8*.
- **Why not a physical-size Wilson loop as RC.** It is continuous and K-uniformly tunable (value 1 at β = 0), but its
  perimeter self-energy (∝ g^2 × length/ε in 4D) drives it to 0 along AF sequences, so it has the same defect as S5.
  This is a heuristic remark, not a proof.

**E8* (replacement for E8; OPEN).** For every K ≥ m + 1, every M and every resolution-m link b, with δ_0 > 0 fixed:
μ_{K,M}(the step m+1 → m at b is within δ_0 of failing, i.e. some ||Z^σ_y - 1|| ≥ τ - δ_0) ≤ ε(g_m), with ε(g) → 0 as
g → 0, plus the Peierls form μ(all of b_1, ..., b_r) ≤ ε(g_m)^r for links with disjoint regions. Here g_m is the running
coupling at resolution m. E8.2 is E8* at m = K - 1 with ε = 2L^4 q̄(t/A_L). The difficulty is the coarse levels, where
neither the Wilson form nor site-reflection RP is available for the law of V^(m+1).
- **What E8* buys.** Consistency A_*ν_{m+1} = ν_m of the limit points (S4'' is continuous off the branch set), and,
  with E7.0', a K-uniform RC.
- **Plausible route (not verified).** Ratios of constrained to unconstrained partition functions, as in Balaban's polymer
  representation, where they differ only by polymers touching b; the per-scale weight e^{-c p(g_m)^2}. The session-1
  sum Σ_j L^{4j} e^{-c p(g_j)^2} < ∞ is NOT the relevant condition (it would control "all steps succeed", which E8.3 shows
  is false); the relevant condition is per-scale smallness of ε(g_j) with polymer entropy, which holds for any p > 0.

**[S4] E8* at depth k ≥ 1: fixed-depth bounds PROVEN-HERE, the reduction of all depths to a homogeneous constrained-stability
statement PROVEN-HERE, general depth OPEN.** Notation: the step m → m-1 is the (k+1)-th averaging step, k = K - m (E8.2 is
k = 0). F_b(t) := {some Z^σ_y of the step m → m-1 at the level-(m-1) link b has ||Z - 1|| ≥ t}; Z is built from V^(m).
Constants: A_L = (d-1)L(L-1)/2, c = 4 arcsin(1/4) = 1.0107, C_1 := L^2 + 4cA_L (= 45.4 for d = 4, L = 3).
Torus convention [S4]: the fine side is 4L^{K+M}, so the level-m side 4L^{M+m} is divisible by 4 at every level (the S3
"even" convention is a special case of what E8.1 needs, and every S3 statement holds verbatim).

- **Lemma E8*-sup (one step, deterministic): PROVEN-HERE.** Let R be a union of level-j blocks and suppose every level-j
  plaquette with all links in the two-block regions of the level-(j-1) links inside R satisfies ||1 - V_p|| ≤ η, with
  A_L η ≤ τ_N/2 (τ_N = min(1, 2 sin(π/N)); **[R4-fix]** session 4 wrote 1/2, which is enough only for N ≤ 12: at N = 13
  the central element e^{2πi/13}·1 has ||Z - 1|| = 0.479 ≤ 1/2 but its principal log has trace 2πi, so S4'' ≠ S4'). Then every level-(j-1) plaquette whose four links have their two-block regions inside R satisfies
  ||1 - V'_p|| ≤ C_1 η.
  - Proof. Ribbon (L1e/E8.2; an identity valid for every lattice gauge field): ||Z^σ_y - 1|| ≤ A_L η ≤ τ_N/2 [R4-fix], so every
    step is in D'_N, S4'' = S4' (L1b), and ||log Z|| ≤ c ||Z - 1|| (θ/(2 sin(θ/2)) is increasing in θ and equals c where 2 sin(θ/2) = 1/2). Hence
    ||X̄|| ≤ cA_L η and ||U' - S_c|| = ||e^{X̄} - 1|| ≤ cA_L η for each coarse link. For a coarse plaquette, the straight
    transporters close to the holonomy S_p of an L×L square of level-j plaquettes, a product of L^2 conjugated
    plaquettes, so ||1 - S_p|| ≤ L^2 η (telescoping with unitaries). Telescoping again,
    ||V'_p - S_p|| ≤ Σ_{i=1}^4 ||U'_i - S_i|| ≤ 4cA_L η. ∎ (τ_N/2 ≤ 1/2, so c computed at 1/2 still bounds the log.)
  - **[R4-fix] Alternative.** Keep A_L η ≤ 1/2 for all N and use ||Π_0 X|| ≤ 2||X|| in S4''; then C_1 = L^2 + 8cA_L.
- **Proposition E8*-k (fixed depth): PROVEN-HERE (given E8.1).** For every k ≥ 0, every K ≥ k + 1, every M and every
  level-(m-1) link b (m = K - k), with t ≤ 1:
  μ_{K,M}(F_b(t)) ≤ 2L^{d(k+1)} q̄(t / (A_L C_1^k)),
  and for links b_1, ..., b_r with pairwise disjoint fine regions, μ(all F_{b_i}(t)) ≤ (2L^{d(k+1)} q̄(t/(A_L C_1^k)))^r.
  Uniform in K and M; q̄ is the fine chessboard constant of E8.1 at β_K.
  - Proof. If every fine plaquette in the fine region of b (two level-(m-1) blocks, 2L^{d(k+1)} fine sites) has
    ||1 - U_p|| < η_0 := t/(A_L C_1^k), then by k applications of E8*-sup (the domain hypothesis of the j-th application, j = 0..k-1,
    is A_L C_1^j η_0 = t C_1^{j-k} ≤ t/C_1 ≤ τ_N/2 [R4-fix: this needs t ≤ C_1 τ_N/2, automatic for t ≤ 1 unless
    sin(π/N) < 1/C_1, i.e. N ≳ 140 at L = 3, d = 4]; L0 keeps all
    regions nested inside the fine region of b), every level-m plaquette in the region of b is < t/A_L, so by the ribbon
    every Z of the step is < t: F_b(t) fails. Contrapositive, union over the ≤ 2L^{d(k+1)} fine cells whose lower corner
    lies in the region, then E8.1(i); disjoint regions give distinct cells. ∎
  - With E8.1(iii): μ(F_b(t)) ≤ 2L^{d(k+1)} poly(β) exp(-β t^2 / (8N A_L^2 C_1^{2k})). This is small iff
    β ≫ A_L^2 C_1^{2k} (k log L + log β), i.e. for the top k ≤ k_*(β) ≈ log β / (2 log C_1) levels only. Along an AF-rate
    sequence (β_K ~ K, imported L4a) that is ~ log K / (2 log C_1) levels out of K: a vanishing fraction.
- **Proposition E8*-ob (the deterministic induction is sharp): PROVEN-HERE.** For U(1) ⊂ SU(2) (or SU(N)) with constant
  flux η per (1,2)-plaquette (one flux quantum, η = 2π/S^2 on the fine torus of side S), the level-k coarse field has
  constant flux exactly L^{2k} η per coarse (1,2)-plaquette while L^{2k-2}A_L η < π/3, so
  ||1 - V^(m)_p|| / max ||1 - U_p|| = sin(L^{2k}η/2)/sin(η/2) ~ L^{2k}.
  - Proof. All transporters lie in one U(1), so they commute and log Z = i(enclosed signed flux)·σ_3 inside the principal
    branch. Loop fluxes are gauge invariant and, for constant field strength, depend only on the loop's shape, so the
    averaged log of link (X, X+e_μ) depends only on μ; in a coarse plaquette the four averaged logs cancel in pairs and
    the coarse flux is the straight square's flux L^2 η. The coarse field again has constant flux; induct. ∎
  - Check c13(B): flux L^2η and L^4η reproduced to 1e-9 (d = 3, L = 3, ratios 9.00, 80.48). Check c13(A): the sup lemma
    holds on random small fields (ratio 0.46 at one step, 0.19 at two, against C_1 = 33.3, C_1^2 = 1106); random
    roughness contracts under averaging, coherent flux grows by L^2 per step.
  - **Consequence.** Any argument that bounds a level-m failure through the fine-plaquette sup in a region needs a fine
    threshold ≲ t L^{-2k} and hence β ≳ L^{4k}. The deterministic route cannot give E8* at depths k ≳ log β.
  - **Energy-entropy reading (heuristic, not proven).** A coherent level-m flux φ costs Wilson action ~ β φ^2 (scale-free:
    Σ_p ||1 - U_p||^2 ≥ φ^2 in the abelian linearised case, by Cauchy-Schwarz over the L^{2k} parallel spanning surfaces),
    but the typical fluctuation energy in a level-m block is ~ L^{dk}/β. Energy bounds alone therefore also need
    β ≳ L^{4k}. Separating the coarse-mode cost from the fluctuation free energy is the multiscale effective action
    (L4-L6), not a shortcut around it.
  - **[R4-fix] Scope of E8*-ob.** It rules out only inductions through the fine-plaquette sup (sup-to-sup bounds have
    constant ≥ L^{2k}). Inductions on other quantities (L^2-type norms, polymer norms, level-wise probabilistic
    re-seeding) are NOT excluded.
- **Proposition E8*-red (coarse chessboard; reduction of every depth to a homogeneous bound): PROVEN-HERE (given L8c with
  S4'' and L9a).** Fix m. For s ∈ {0,1}^d let F_s be the family of level-m cells C_t = t + {0,1}^d, t ∈ s + 2Z^d (2^d
  level-m sites each; the cell event may use the level-m links with both ends in C_t). Let G_C(η) := 1[some level-m
  plaquette in C has ||1 - V_p|| ≥ η] and q̄_m(η) := ν_m(G_C(η) for every C ∈ F_0)^{1/n_c}, n_c = (2L^{M+m})^d, ν_m the law
  of V^(m) under μ_{K,M}. Then:
  - (i) ν_m(all C ∈ R bad) ≤ q̄_m(η)^{|R|} for every set R of cells of one family;
  - (ii) μ(F_b(t)) ≤ 2L^d q̄_m(t/A_L) for every level-(m-1) link b, and μ(all F_{b_i}(t)) ≤ (2L^d)^r q̄_m(t/A_L)^{r/2^d} for
    links with pairwise disjoint regions.
  - Proof of (i). The planes of F_s's cell boundaries are level-m link planes (resolution-m block boundaries = fine link
    planes, L odd). There are 2L^{M+m} cells per direction (even), and the antipode of a boundary plane (shift 2L^{M+m})
    is again a boundary plane, so each reflection splits the torus into two halves of L^{M+m} cell-slabs. ν_m is RP for
    these reflections for bounded measurable F (not only continuous f as in L8c): F∘V^(m) is a bounded measurable
    function of the positive-half fine links (L0), V^(m)[θU] = θV^(m)[U] everywhere (S4'' odd rule), and the fine
    link-plane RP of L9a holds for bounded measurable gauge-invariant F (its written proof uses only integrals of F
    against the gauge-fixed product measure; G_C is gauge invariant because ||1 - V_p|| is conjugation invariant) and θ(G_C) = G_{θC} (V[θU] = θV[U];
    ||1 - V_p|| is invariant under the orientation reversal). The E8.1(i) maximiser/run-doubling argument then applies
    verbatim with cells C ∈ F_s; translation invariance (L8b) gives the same q̄_m for every s. ∎
  - Proof of (ii). Ribbon at level m: F_b(t) ⊂ ∪_p {||1 - V_p|| ≥ t/A_L} over level-m plaquettes in the region of b; each
    such p lies in the cell with its lower corner, of one of the families; ≤ 2L^d lower corners; union bound and (i)
    with |R| = 1. For r links: union over one lower corner per link; for each choice, the largest single-family subset
    has ≥ r/2^d distinct cells. ∎
  - **What it buys.** E8* at every depth follows from the HOMOGENEOUS, translation-invariant bound
    **E8\*\* (constrained stability; OPEN):** q̄_m(η) ≤ ε(g_m) for fixed η > 0, uniformly in K ≥ m and M, with ε(g) → 0
    as g → 0. It is a ratio of partition functions, Z_K(every level-m cell of F_0 contains an η-large coarse plaquette)
    / Z_K ≤ ε^{n_c}: a statement of the same type as UV stability (L6), with the large-field constraint imposed in every
    cell. Whether Balaban's large-field estimates (L5) give it is [unverified-exact-statement]. E8*-k is the trivial
    bound q̄_m(η) ≤ (2L^k)^d q̄(η/C_1^k) (choose one fine cell per coarse cell; E8.1(i)), consistent with (ii).
- **Status of E8* after [S4].** PROVEN-HERE for each fixed depth k (constants uniform in K, M; useful for β ≫ C_1^{2k});
  for depths k ≳ log β it is reduced (sufficient condition) to E8**, OPEN. E8*-ob shows the induction through the
  fine-plaquette sup cannot close the general case [R4-fix]. Literature [S4]: Project Euclid (CMP back volumes) returned a bot-detection page
  (Incapsula); not bypassed. Dimock, "Ultraviolet stability for QED in d = 3", arXiv:2009.01156 [v-R4; body read-skim in S5, see L6loc [S5] and literature/NOTES.md]: abstract read
  ("an ultraviolet stability bound in a fixed finite volume", Balaban's formulation, weak coupling); body not read; no
  E8**-type statement in the abstract.

**[S5] Literature re-verification and E8** reassessment (session 5).** Source notes with page and equation references are
in `literature/NOTES.md`; tags there are [read] / [read-skim] / [not-read]. Every Dimock statement below was read in the
arXiv text. Every Balaban statement is still [not-read].

- **What E8** is, after reading. No source I read states E8** (a probability bound on a level-m constrained event) as a
  theorem. Dimock bounds densities and partition functions, never such a probability. The mechanism that would prove
  it is, however, stated explicitly in two places:
  - **Dimock III (arXiv:1304.0705), Lemma 13 (p.24, eq. 166).** In every cube where the level-j small-field condition on
    the level-j RG variables fails, the level-j effective action supplies e^{-c_2 p_j²}. The proof (p.25) goes through
    Lemma 20 (p.35, eq. 246): fine free action ≥ c_0 × the coarse gradient energy of the block variables. Theorem 2 and
    Corollary 1 (p.33) then sum the histories.
  - **Dimock QED (arXiv:2009.01156), Lemma 23 (p.64, eq. 471).** The gauge-field version. A large field at level k+1
    forces |dA_k| ≥ (CM)^{-1} p_{k+1} nearby, by ONE step of the regularity bound (478). The cost is charged to that
    level's own action ½||dA_k||², through ζ ≤ exp(-p + (CM)² p^{-1} ||dA_k||²) (479).
  - In both, **the sup bound crosses exactly one level and is never iterated**: each level re-seeds from its own action.
    That is the escape from E8*-ob, which rules out only iterated sup-to-sup inductions [R4-fix]. It is also why, in
    Balaban's set-up, the small-field conditions are dimensionless per level.
  - [Inference, not read] In d = 4 the dimensionless conditions allow fine field strengths up to ~L^{2(k-j)} at depth
    k - j; QED p.8, eq. 41 has L^{(3/2)(k-j')} in d = 3. That is exactly the L^{2k} growth of the E8*-ob constant-flux
    field, so that field is a *small-field* configuration at the coarse level. It is an obstruction to the sup
    induction, not to Balaban's.
- **Verdict on E8**.** E8** is NOT new content. It is the probability-level form of "large-field suppression per level
  (L5-type) + stability of the remaining integral (L6-type)", and it would follow from Lemma E8**-dens below once the
  level-m effective density obeys (D_m). It is NOT marked IMPORTED, because no source states it. Its status is
  **OPEN (import target: corollary of L5 + L6)**. The scalar template (Dimock III, Lemma 13 + Theorem 2) and the abelian
  template (QED, Lemma 23 + Theorem 2) are [read]. The 4D SU(N) source would be Balaban CMP 122 (1989) 175-202 and
  355-392, with CMP 116 (1988) 1-22 and CMP 119 (1988) 243-285 [not-read].
  - **Caveat.** Balaban's RG variables are his own averaging (CMP 98 (1985) 17-51 [not-read]). Dimock's QED averages the
    gauge potential linearly, with block axial gauge fixing (2009.01156, p.2, eq. 4). Whether either equals S4' is
    unverified. A (D_m) for Balaban's variables transfers to S4' only through a comparison of the two maps.
- **Lemma E8**-dens (reduction of E8** to an effective-density bound): PROVEN-HERE.**
  - Setting.
    - Let ν_m, the law of V^(m), have density ρ_m with respect to product Haar on the n_ℓ = d·|Λ_m| level-m links.
    - **(D_m):** ρ_m(V) ≤ e^{C_+ n_ℓ} Π_{C∈F_0} w_C(V|_C), where 0 ≤ w_C ≤ 1, and w_C ≤ ω whenever C is η-bad.
  - Claim: q̄_m(η) ≤ e^{d 2^d C_+} ω.
  - Proof.
    - ν_m(every C ∈ F_0 bad) = ∫ Π_C 1[C bad] ρ_m dHaar ≤ e^{C_+ n_ℓ} ω^{n_c}. This uses Haar mass 1, and the fact that
      the cells of F_0 have disjoint link sets.
    - n_ℓ = d 2^d n_c. Take the n_c-th root. ∎
  - **Gibbs case.** Take w_C = exp(-a Σ_{P⊂C} (1 - N^{-1} Re tr V_P)). By (B) below, ω = e^{-aη²/(2N)}. So E8** holds
    with ε(g) = exp(d 2^d C_+ - aη²/(2N)), provided a(g_m)η²/(2N) - d 2^d C_+(g_m) → ∞. For example, a ~ c/g_m² and
    C_+ = O(1 + log(1/g_m)), where the log is the Gaussian normalisation.
  - **Balaban-type case.** Suppose the factor is per M-cube, ≤ e^{-c p(g_m)²} whenever the cube is large-field (Dimock
    III Lemma 13 form). A cube containing a bad 2-cell is large-field once η exceeds the level-m small-field threshold.
    Then q̄_m ≤ exp(d 2^d C_+ + (2/M)^d (C - c p(g_m)²)) → 0.
  - (B) **[S5] Inequality, PROVEN-HERE.** 1 - N^{-1} Re tr U = ||1 - U||_HS²/(2N) ≥ ||1 - U||_op²/(2N). Expand
    ||1 - U||_HS² = 2N - 2 Re tr U; then HS ≥ op. Check c16(B).
- **Lemma A1 (abelian averaging is action-contracting, sharp constant L^{4-d}): PROVEN-HERE.** For real link fields A on
  the fine torus, linearise S4' to A'(X, X+e_μ) := avg_{σ,y} A(T^σ_y). The same holds for compact U(1) whenever every
  loop flux involved lies in the principal branch, by the E8*-ob argument. Then:
  - (i) dA'(P) = avg_{y∈B(X)} Φ_A(sq_y), where sq_y is the straight L×L square with lower corner y in the plane of P.
  - (ii) Σ_P |dA'(P)|² ≤ L^{4-d} Σ_p |dA(p)|². **[R56-fix]** The constant L^{4-d} is the supremum over torus sizes,
    approached by long-wavelength modes; it is not attained for real A on a torus (a constant F is closed but not in
    Ran d, since its flux through a coordinate 2-torus is nonzero). Equality is attained for compact U(1) with a
    quantised constant flux inside the principal branch.
  - Proof of (i).
    - Pair the four links of P with the SAME σ and translated y: y, y + Le_μ, y + Le_ν, y.
    - The axial legs P^σ(c_{X+e_μ} → y + Le_μ) at the end of link 1 and at the start of link 2 coincide. In the abelian
      sum they cancel, and likewise at the other corners.
    - What remains is c_X → y, the square, and y → c_X. The flux of that loop is Φ(sq_y).
    - Averaging is linear, so the pairing is legitimate. ∎
  - Proof of (ii) (Schur test).
    - The weight of fine plaquette p in row P is w_P(p) = L^{-d} #{(y, a, b) : y ∈ B(X), y + a e_μ + b e_ν = p}.
    - It vanishes unless p_⊥ = y_⊥ (one value per transverse coordinate). In each in-plane coordinate it is a tent of
      height ≤ L.
    - Row sums: Σ_p w_P(p) = L^{-d} · L^d · L² = L².
    - Column sums: summing the tents over in-plane blocks gives L per coordinate, so Σ_P w_P(p) = L^{-d} · L · L = L^{2-d}.
    - Hence ||M||² ≤ L² · L^{2-d} = L^{4-d}. Constant row and column sums make the constant vector extremal for M on
      all plaquette fields; on Ran d it is approached, not attained [R56-fix]. ∎
  - Iterating, the level-m action is ≤ L^{(4-d)k} times the fine action. **In d = 4 the coarse action never exceeds the
    fine action, at any depth.** Contrast E8*-ob, where the sup grows like L^{2k}: the constant-flux field has equal
    action at every level. **[R56-fix]** "Equal action at every level" holds for the quadratic action only; for the
    cos action of compact U(1) the ratio of that mode is 0.81 at the c18b flux.
  - Cross-check with Dimock [read]: in d = 3 the per-step constant L is exactly the growth e_k² = L^k e_0² of the
    dimensionless QED coupling (2009.01156, p.2, eq. 7). For this linear map, "super-renormalizable" and "marginal" are
    the cases L^{4-d} > 1 and = 1.
  - This is the gauge analogue, in the dual direction, of Dimock III Lemma 20 (fine action ≥ c_0 × coarse gradient
    energy).
  - Check c16(A1): the identity holds to 1e-14 (d = 2, 3, 4; L = 3). ||M||² = 9, 3 and 1.000000 = L^{4-d} exactly. A
    two-step d = 2 run gives ratios ≤ L². The check is 11/11, 3 s, 69 MB.
- **Proposition A2 (E8** for the 4D Gaussian abelian model, all depths, uniform in K, M): PROVEN-HERE.**
  - Model. Noncompact abelian gauge field. The law of F = dA is N(0, β^{-1} Π_{Ran d}) on the fine plaquettes, i.e.
    e^{-(β/2)||dA||²} with any complete gauge fixing. Levels are built with the linearised S4'.
  - Claim. Let d = 4, and call a level-m cell bad if some plaquette in it has |F^(m)_P| ≥ η. Then for every set R of
    cells of one family:
    μ(every C ∈ R bad) ≤ (2^{n_pc/2} e^{-βη²/4})^{|R|}, where n_pc = C(d,2) 2^{d-2} = 24.
    So E8** holds with ε = 4096 e^{-βη²/4}, in the |F^(m)_P| ≥ η form, at every depth; the chessboard RP step is not
    even needed. **[R56-fix: scope]** The session-5 sentence "Through E8*-red(ii) this gives E8* at every depth" is
    WITHDRAWN: E8* and E8*-red(ii) concern the compact S4''/S4' steps and their domain events, and the noncompact
    Gaussian averaging is linear with no domain. An E8* statement for this model would need E8* defined through the
    compact embedding U = e^{iA}, plus a proof that the compact domain events are controlled by the linear F^(m) (they
    are while every flux stays in the principal branch, itself an E8*-type event). Not done. (The badness notions are
    compatible: ||1 - e^{iF}|| ≤ |F|.)
  - Proof.
    - By A1, F^(m) = M_m F with ||M_m|| ≤ 1.
    - Let Φ be the vector of the r = n_pc |R| level-m plaquettes of the cells in R. It is Gaussian with covariance
      C = β^{-1} M_R Π M_R^T, and ||C|| ≤ β^{-1}.
    - On the event, choose one bad plaquette per cell (the cells are disjoint). Then Q := |Φ|² ≥ |R| η².
    - For s = β/4: E e^{sQ} = det(1 - 2sC)^{-1/2} ≤ (1 - 2s/β)^{-r/2} = 2^{r/2}.
    - Markov: μ ≤ e^{-β|R|η²/4} 2^{r/2}. ∎
  - In d < 4 the same proof gives β_eff = β L^{(d-4)k}: the free coupling grows, as it should in a super-renormalizable
    model.
  - **What A2 shows, and what it does not.**
    - It shows that E8** is consistent and natural: it holds at every depth in the free 4D theory, where E8*-ob's
      sup-growth is present.
    - It also shows that the right quantity is the action (an L² object), not the sup. This is the "inductions on other
      quantities" escape that REVIEW_S4 flagged.
    - It is not SU(N). There the coupling runs, and the measure is non-Gaussian: the fluctuation integral replaces β_K by
      ~β_m. That replacement is L3g + L4a + L6, and (D_m) packages it.
- **A1-NA (OPEN, new).** For SU(N) with S4', on small-field configurations:
  Σ_P (1 - N^{-1} Re tr V'_P) ≤ (1 + o(1)) L^{4-d} Σ_p (1 - N^{-1} Re tr U_p).
  - The ribbon estimate of E8*-sup gives only C·L². The abelian cancellation of the axial legs is exact only at linear
    order; nonabelian legs conjugate.
  - This is the classical (tree-level) half of (D_m). Its likely Balaban counterpart is the variational analysis of CMP
    102 (1985) 277-309 [not-read].
  - **[S6] Status: proven in the one-step form A1-NA(1) below (OPEN → PROVEN-HERE), with a k-uniform corollary on the
    L1e domain.**

**[S6] Lemma A1-NA(1) (one-step non-abelian action bound, local form): PROVEN-HERE.**
- **Setting.**
  - Any d; one averaging step, S4' or Balaban's (0.4) (their linearisations coincide, L1d [S6]); G = SU(N).
  - For a fine plaquette p, let X_p = log U_p (principal), with |·| the Hilbert-Schmidt norm. **[R56-fix: branch]**
    "Principal" means every eigen-angle in (-π, π]; it is NOT the S4'' odd branch rule, under which a plaquette with
    an eigenvalue -1 would get X_p = 0, satisfy φ_R ≤ φ_0 and still have s(U_p) ≥ 2/N, breaking (b) and (c).
  - **[R56-fix]** Hypothesis: the coarse torus side is ≥ 3 coarse sites, so that W_P does not wrap (S4 [S4] gives side
    ≥ 4; c18's coarse side 2 violates it, which is harmless for a check).
  - For a coarse plaquette P, let W_P be the union of the 4 fine blocks at its corners. It contains every path used by
    P's four links (L0), and it is a box, so it is simply connected. Let W̃_P be its fine plaquettes.
  - For a set R of coarse plaquettes, put R̃ := ∪_{P∈R} W̃_P and φ_R := max_{p∈R̃} |X_p|.
- **Claim.** There are φ_0 = φ_0(L, d, N) > 0 and C_6 = C_6(L, d, N) < ∞ such that, if φ_R ≤ φ_0:
  - (a) Σ_{P∈R} |log V'_P|² ≤ (L^{4-d} + C_6φ_R) Σ_{p∈R̃} |X_p|²;
  - (b) the same with |X|² replaced by the Wilson density s(U) := 1 - N^{-1} Re tr U on both sides, with C_6 enlarged.
    In d = 4: Σ_{P∈R} s(V'_P) ≤ (1 + C_6φ_R) Σ_{p∈R̃} s(U_p).
  - (c) **One-step large-field transfer (dichotomy).** If Σ_{P∈R} s(V'_P) ≥ η, then either some p ∈ R̃ has
    |X_p| > φ_0, so that s(U_p) ≥ φ_0²(1 - φ_0²/12)/(2N), or Σ_{p∈R̃} s(U_p) ≥ η/(1 + C_6φ_0) (d = 4).
- **Proof.**
  1. **Elementary bounds.**
     - (BCH) If x_1, ..., x_n are anti-Hermitian with s := Σ|x_i| ≤ 1/4, then |log(e^{x_1}⋯e^{x_n}) - Σ x_i| ≤ 9s².
       Indeed, Y := Πe^{x_i} - 1 has |Y - Σx_i| ≤ e^s - 1 - s ≤ s² and |Y| ≤ e^s - 1 ≤ 2s ≤ ½. Then
       |log(1+Y) - Y| ≤ |Y|²/(1 - |Y|) ≤ 8s², using the power series of the principal log for |Y| < 1. The HS norm
       is submultiplicative.
     - If |Z - 1| ≤ ½, then |log Z| ≤ c|Z - 1| with c = 4 arcsin(1/4) (L1e).
     - |e^X - 1| ≤ |X|.
  2. **Local gauge.** Fix P and put the links of W_P in complete axial gauge from a corner of the box. As in L3s(i)
     (ladder of lassos), each a_b := log U^{ax}_b satisfies |a_b| ≤ c·(d-1)·2L·max_{p∈W̃_P}|X_p| =: C_1φ_P.
     Gauge transformations conjugate plaquette holonomies, so |X_p^{ax}| = |X_p|. They also conjugate V'_P (L1a, L0),
     so |log V'_P| is unchanged.
  3. **Linearisation of the coarse plaquette.**
     - Each Z_y used by P's links is a product of ≤ (d+2)L link exponentials e^{±a}. By (BCH),
       log Z_y = (signed sum of the a's on its path) + r_y, with |r_y| ≤ 9((d+2)LC_1φ_P)².
     - So X̄_b = ℓ_b(a) + r̄_b, with |r̄_b| bounded by the same constant.
     - V'_P is a product of 4L straight-link exponentials and four exponentials e^{±X̄_b}. By (BCH),
       log V'_P = Λ_P(a) + R_P, with |R_P| ≤ C_2φ_P² for φ_P ≤ φ_0.
     - Λ_P is the abelian linearised S4' plaquette of the field a, so by Lemma A1(i) Λ_P = avg_y Σ_{p∈sq_y}(da)_p.
     - φ_0 is chosen so that every (BCH) application has s ≤ 1/4 and every Z_y lies in D'_N (so S4'' = S4').
  4. **Fine plaquettes.** (da)_p is the sum of the four link logs, and log U^{ax}_p is the log of their product. By
     (BCH), |(da)_p| ≤ |X_p| + 9(4C_1φ_P)². Hence |Λ_P| ≤ Σ_p w_P(p)|X_p| + L²C_3φ_P², with the A1 weights
     w_P ≥ 0 and row sum L².
  5. **Collect.**
     - |log V'_P| ≤ Σ_p w_P(p)|X_p| + C_4φ_P².
     - φ_P² ≤ φ_R φ_P ≤ φ_R (Σ_{p∈W̃_P}|X_p|²)^{1/2}.
     - With (u + v)² ≤ (1 + φ)u² + (1 + 1/φ)v², φ := φ_R ≤ 1:
       - Σ_{P∈R}(Σ_p w_P|X_p|)² ≤ L² · L^{2-d} Σ_{p∈R̃}|X_p|² by the Schur test of A1(ii). The row sums are L² and the
         column sums, restricted to P ∈ R, are ≤ L^{2-d}.
       - Σ_{P∈R} C_4²φ² Σ_{p∈W̃_P}|X_p|² ≤ C_4² n_W φ² Σ_{p∈R̃}|X_p|², where n_W ≤ 4·d(d-1)/2 bounds how many W_P
         contain a given p.
     - This gives (a) with C_6 = L^{4-d} + 2C_4² n_W.
  6. **(b).** For U = e^X ∈ SU(N) with eigen-angles θ_j:
     - s(U) = N^{-1}Σ_j(1 - cos θ_j), and |X|² = Σθ_j²;
     - (θ²/2)(1 - θ²/12) ≤ 1 - cos θ ≤ θ²/2.
     - So |X|²(1 - φ²/12)/(2N) ≤ s(U) ≤ |X|²/(2N). Use the upper form on the coarse side and the lower form on the fine
       side. The factor (1 - φ_0²/12)^{-1} ≤ 1 + φ_0²/6 is absorbed into C_6.
  7. **(c) [R56-fix: proof replaced].** If φ_R ≤ φ_0, (b) gives η ≤ (1 + C_6φ_R)Σ_{p∈R̃}s(U_p) ≤ (1 + C_6φ_0)Σ s(U_p).
     Otherwise some p ∈ R̃ has |X_p|² = Σ_jθ_j² > φ_0², with θ_j ∈ (-π, π] (principal branch). Put t_j := θ_j² ∈ [0, π²]
     and f(t) := 1 - cos√t. f is increasing and concave on [0, π²] (f'(t) = sin√t/(2√t), and sin x/x decreases on
     (0, π]), with f(0) = 0, so f(t)/t is non-increasing. Take φ_0 ≤ π. If some t_j ≥ φ_0², then f(t_j) ≥ f(φ_0²).
     Otherwise every t_j < φ_0², so f(t_j) ≥ t_j f(φ_0²)/φ_0², and Σ_j f(t_j) ≥ (Σ_jt_j) f(φ_0²)/φ_0² > f(φ_0²). In
     both cases N s(U_p) = Σ_j f(t_j) ≥ 1 - cos φ_0 ≥ (φ_0²/2)(1 - φ_0²/12). The SU(N) constraint Σθ_j = 0 only
     shrinks the feasible set, so it does not affect the lower bound. (Session 6's "contrapositive of (b) plus step 6"
     was not a proof: step 6's lower bound needs every |θ_j| ≤ φ, which fails exactly in this branch.) ∎
  - **[R56-fix] Norm conversion used by A1-NA(k).** For ||1 - V||_op ≤ ½, |log V|_HS ≤ √N||log V||_op ≤
     c√N||1 - V||_op, so c_N = c√N with c = 4 arcsin(1/4).
- **Remarks.**
  - C_6 is finite and computable but grows with L. No attempt was made to optimise it.
  - (c) is the non-abelian, action-form analogue of the one-step mechanism of Dimock QED Lemma 23 (NOTES §4): a
    coarse large field forces either a fine large field or fine action, across ONE step.
  - The sharp leading constant L^{4-d} (= 1 in d = 4) is inherited from A1.
- **Check c18** (SU(2), d = 4, L = 3, fine 6⁴ → coarse 2⁴; 11 s, 422 MB; first run kept as c18_out_firstrun.txt).
  - 6 PASS / 2 FAIL. Criterion (i) R(t_min) ≤ 1 holds for all four fields: smooth abelian, two smooth non-abelian,
    rough.
  - The two FAILs are of the pre-registered criterion (ii), "log-log slope of |R(t) - R(t_min)| ≥ 0.9" (slopes 0.53 and
    0.71). The deviation is non-monotone in t (a linear and a quadratic part of opposite sign), so the slope test was
    ill-posed. The bounded quantity |R - R_0|/φ is ≤ 0.006.
  - Weakness: on a 2⁴ coarse torus these fields have ratios 0.001-0.04, far from the extremal value 1. So c18 does not
    probe the sharp constant.
- **Check c18b** (POST HOC, added after c18; 6 s, 404 MB).
  - Near-extremal background: one flux quantum of constant abelian field in a plane (the A1 extremal mode; ratio
    R(0) = 0.8126, below 1 because of compact-U(1) curvature at this flux), times a smooth non-abelian perturbation.
  - |R(t) - R(0)| ≤ 0.45t for t ≤ 0.04, and the deviation is quadratic (R decreases).
  - 1/1 PASS on its post-hoc criterion. It is an instance, not a test of C_6.
  - **[R56-fix]** c18b lies OUTSIDE A1-NA(1)'s small-φ regime: the coarse plaquette angle is π/2 (9 × 0.1745 per
    eigen-angle), far beyond the coarse-level BCH condition; R(0) = 0.81 is the cos nonlinearity at angle π/2, not a
    near-extremal ratio; and its criterion "C < 10" is effectively unfalsifiable. **It is not a test of the lemma.**
    The pre-registered in-regime test is c18c (below).
- **Check c18c [S7, R56-fix] (in-regime, pre-registered in checks/c18c_criteria.md before the script was written;
  first run; 16/16 PASS; 0.96 s, 66 MB).** SU(2), S4', L = 3; d = 2 with coarse side 5 and d = 3 with coarse side 3;
  principal-branch logs; HS norms; U = exp(tH), H = lowest Fourier modes (abelian τ_3 part plus a smooth τ_1/τ_2 part
  of relative size 0.3), t = 0.0025-0.02. R_ab is computed independently from the abelian linearised S4'.
  - Near-extremal: R_ab/L^{4-d} = 0.789 (d = 2) and 0.508 (d = 3) ~~, the largest available on these tori~~ **[R78-fix]:
    the "largest available" claim is deleted; no scan was done**. R_ab is the
    same for both seeds because every component sits on a lowest axial mode, all of which share one eigenvalue of M.
  - In regime: fine φ ≤ 2.2e-2 and coarse |log V'_P| ≤ 0.13.
  - Key step confirmed on these instances: R_log(t) → R_ab, and D(t) = |R_log - R_ab|/φ decreases linearly in φ.
    So the non-abelian correction is O(φ²) here, below the lemma's O(φ), and it is negative (R_log < R_ab ≤ L^{4-d}).
    The reported C_rep = 0, i.e. R ≤ L^{4-d} at every t. |R_s - R_log| ≤ 1.6e-3.
  - Limitation: because L^{4-d} is a supremum that finite tori do not reach (A1 [R56-fix]), the gap L^{4-d} - R_ab
    (21%, 49%) exceeds the non-abelian deviation, so the inequality is not stressed at its exact edge. What is tested
    is that the leading constant is the abelian one, with a correction vanishing as φ → 0, inside the regime.

**[S6] Corollary A1-NA(k) (k-uniform classical action bound on the L1e domain, for S4' iterates): PROVEN-HERE.**
- **[R56-fix: scope]** Proven for **S4' iterates** V^{(j)} = A(V^{(j+1)}) only, because L1e is proven only for S4/S4'.
  The readings "= Balaban's background domain (1.2)" and the minimiser reading below apply it to V = M^k(U_k(V)) with
  Balaban's (0.4) (independent pairing), and need (i) the OPEN item L1e-(0.4) (two-axial-path ribbon variant, L1d
  [R56-fix]) and (ii) the √N conversion between Balaban's normalised-trace |·| and our operator norm. Until then they
  are conditional.
- **Setting.** d = 4 and the hypotheses of L1e: L ≥ 9 odd, F ≤ F_0; level-m torus side ≥ 3 coarse sites. Add F ≤ F_1 := φ_0/(c_N(1 + 4C_δ)), where c_N
  converts ||1 - V_p||_op into |log V_p|_HS (c_N = c√N).
- **Claim.** For all k and all j < k: A(V^{(j)}) ≤ exp(C_6 c_N (1 + 4C_δ) F/(L² - 1)) · A(V^{(k)}), where A is the
  Wilson action Σ s(·) on the respective lattice.
- **Proof.**
  - By L1e(b), the level-(j+1) plaquettes obey |log V^{(j+1)}_p| ≤ c_N(1 + 4C_δ)F L^{-2(j+1)} =: φ_{j+1} ≤ φ_0. By
    L1e(c), every step is in D'.
  - Apply A1-NA(1)(b) with R = all plaquettes at each step: A(V^{(j)}) ≤ (1 + C_6φ_{j+1}) A(V^{(j+1)}).
  - Multiply over the steps and use Σ_{i≥1}L^{-2i} = 1/(L² - 1). ∎
- **What it gives.**
  - On L1e's domain, for S4' iterates (on Balaban's (1.2) for (0.4) only conditionally on L1e-(0.4) and the √N
    conversion [R56-fix]), the classical Wilson action never grows
    under blocking by more than a factor 1 + O(F), uniformly in the number of steps. This is the k-step, non-abelian
    form of A1 in d = 4.
  - For the minimiser U_k(V) (L2 [S6]) it reads A_coarse(V) ≤ e^{C_7F} A(U_k(V)), with C_7 := C_6c_N(1 + 4C_δ)/(L² - 1).
    [R56-fix] This reading is conditional on L2, on L1e-(0.4) (V = M^k(U_k(V)) uses Balaban's M), and on the √N
    conversion.
- **Wall for fluctuating fields.** For general configurations the per-step factors 1 + C_6φ_j multiply. With
  Balaban-type per-level thresholds φ_j ~ g_j, Σ_j g_j = ∞ along (0.31) (compare L4c(c)), so no k-uniform iterated
  bound follows. This is consistent with Balaban/Dimock, who never iterate: they re-seed at each level from that level's
  own action (S5 finding 2). A1-NA(1)(c) is exactly the one-step input of that re-seeding.

**[S6] Proposition LF-count (the unrenormalised per-level large-field count diverges in d = 4): PROVEN-HERE (the
arithmetic); the interpretation is labelled.**
- **Template [read].** Dimock, Rome lectures p.39 (224)-(228) (NOTES §10). Each level-k M-cube in the large-field
  region carries a factor w_k ≤ 1. The sum over large-field regions is bounded by Π_□(1 + w_k) ≤ exp(Σ_k N_k w_k),
  where N_k = (L^kε)^{-4}M^{-4}|T| is the number of level-k M-cubes, and |T| the physical volume. A uniform-in-K bulk
  bound needs C_K := Σ_{k=0}^K L^{4(K-k)} w_k bounded uniformly in K.
- **Claim.**
  - Let g_k obey the upper half of (0.31), 1/g_k² ≤ 1/g² + β'(K - k) log L, and let w_k ≥ e^{-a/g_k²} for some
    a > 0. Then C_K ≥ e^{-a/g²} Σ_{n=0}^K L^{(4 - aβ')n}, which diverges as K → ∞ whenever aβ' ≤ 4.
  - Conversely, if w_k ≤ e^{-a/g_k²} and the lower half of (0.31) holds with aβ > 4, then C_K ≤ e^{-a/g²}/(1 - L^{4-aβ}).
  - In d = 3 (g_k² = g²L^kε, CMP 109 p.259), w_k = e^{-a/g_k²} gives a convergent C_K for every a > 0.
- **Proof.** Substitute: L^{4n}e^{-a(1/g² + β'n log L)} = e^{-a/g²}L^{(4-aβ')n}. The other cases are the same
  geometric or double-exponential sums. ∎
- **Interpretation (labelled).**
  - [inference] For a per-cube large-field factor to be a valid bound, w_k must be at least of the order of the
    Boltzmann weight of the cheapest configuration the small-field indicator excludes, e^{-a/g_k²}. For CMP 109's
    fluctuation cut |B'| < ε_1, that cost is a ≤ ½||Δ^{(k)}|| ε_1² = O(ε_1²).
  - **[R56-fix: one normalisation, Balaban's.]** CMP 109's action is (1/g_k²)Σ[1 - Re tr U] with tr 1 = 1 (NOTES
    §9.1), so 1/g_B² = 2N/g_std², and the perturbative rate in (0.31) is β'_B ≈ 2N·2b_0 = 4Nb_0 = 11N²/(12π²) ≈
    0.0929N² [inference; (0.31) leaves β' unspecified]. The cost a = ½||Δ^{(k)}||ε_1² is also in Balaban's
    normalisation ((2.10)). Divergence (aβ' ≤ 4) then holds when a_B ≤ 4/β'_B = 48π²/(11N²) ≈ 43.1/N² (10.8 for
    SU(2), 4.8 for SU(3)), i.e. for **ε_1 ≲ (8/(||Δ||β'_B))^{1/2}**; with ||Δ|| ≈ 16 this is ε_1 ≲ 1.16 (SU(2)), 0.77
    (SU(3)), falling like 1/N. So the statement holds **for ε_1 small enough** (which is what Balaban assumes),
    conditional on the one-loop rate [inference]; it is NOT shown for O(1) thresholds. The session-6 numbers "a > 86/N,
    a > 43 for SU(2)" mixed normalisations and were a factor 2N too strict; WITHDRAWN. At large N the per-bond
    cheapest-configuration estimate also ignores the N² fluctuation entropy.
  - The single instanton (a = 8π² in the normalisation of L4b) gives aβ' = 11N/3 > 4 for N ≥ 2 (the product aβ' is
    normalisation-independent). So genuinely non-perturbative excursions are summable. The divergence sits in the
    intermediate window O(ε_1²) ≲ a_B ≲ 4/β'_B.
  - [heuristic] Probabilistic counterpart: the level-k fluctuation has variance ∝ g_k², so the expected number of
    threshold-violating bonds per unit physical volume at level k is ~L^{4(K-k)}e^{-cε_1²/g_k²} → ∞. So fine-scale
    "large fields" are dense in d = 4, not rare. The PROVEN counterpart is E8.3: a first step leaves D in a fixed block
    with probability → 1, conditional on the AF rate.
- **Consequence: the exact wall of the reconstruction.**
  - In d = 4 the large-field regions cannot be bounded as rare excursions and then discarded, as in Dimock's d = 3
    template. Their contribution to log Z must itself be renormalised: the vacuum-energy and β_j·A counterterms must be
    applied in large-field regions too, so that the per-cube contribution at level k becomes summable against
    L^{4(K-k)}, as the small-field V^{(j)} are in (0.29)-(0.30).
  - Dimock's description of the R-operation ("converts some large field contributions back to small field
    contributions", II p.31 [read]) and the CMP 122 abstracts [read-abs] are consistent with this being its job. The
    exact statement is [not-read].
  - The same wall blocks E8**/(D_m): E8**-dens needs a K-uniform C_+. The classical part is now proven (A1-NA(1),
    A1-NA(k)). The fluctuation normalisation (L3g, L4a, L6) and the renormalised large-field bound (L5) are not.

**[S6] Large-field reconstruction: outcome.**
- **Route (a), open sources.** No open-access work states Balaban's 4D large-field bound or the R-operation (NOTES
  §10).
  - Found and read: Dimock's Rome lectures (d = 3 counting template, p.39); BFKT 1609.00968 p.4 (per-point extraction
    is "routine" for positive actions, which the Wilson action is); Jaffe-Witten (descriptive); the OSTI abstracts of
    CMP 122.
  - Project Euclid was bot-blocked and not bypassed.
- **Route (b), re-derivation.** Done: the per-level large-field extraction for the bare Wilson action (A1-NA(1)(c),
  plus inequality (B), plus E8**-dens).
  - **Wall (exact):** a renormalised large-field bound, i.e. per-level large-field contributions with the
    vacuum-energy and coupling counterterms applied inside large-field regions, summable against L^{4(K-k)}.
    Proposition LF-count proves that the unrenormalised version cannot be summed in d = 4 for every ε_1 below an
    explicit bound, conditional on the one-loop rate [R56-fix; inference]. The next attempt should construct this renormalisation for a single isolated large-field cube at level
    k in the 4D SU(N) model (a one-cube R-operation), not a further reduction.

**[S5] What the non-abelian 4D version needs beyond Dimock** (each item: what Dimock has [read], and the Balaban source
[not-read]).
1. **Non-abelian averaging and regular-configuration spaces (L1d).**
   - Dimock: only abelian regularity, 1712.10029 Thm 1 (p.43, eq. 327). Dimock calls it "abelian versions of non-abelian
     results" in CMP 99 (1985) 75-102 and CMP 102 (1985) 277-309.
   - Needed: CMP 98 (1985) 17-51 and CMP 99 (1985) 75-102.
2. **Non-linear constrained minimiser (L2).**
   - Dimock: in abelian theories it is a linear operator H_k (2204.07201, p.6, eqs. 22-25). So there is no abelian
     counterpart of the existence, uniqueness and analyticity problem.
   - Needed: CMP 102 (1985) 277-309.
3. **Background-dependent fluctuation propagators (L3g).**
   - Dimock: in QED the gauge propagator is background independent. Its bounds (1512.04373, Lemmas 6, 9, 11) are
     themselves "sketched" with citations to Balaban.
   - Needed: CMP 95 (1984) 17-40, CMP 96 (1984) 223-250 and CMP 99 (1985) 389-434.
4. **Marginal-coupling flow and the small-field effective action in 4D (L4a).**
   - Dimock: only super-renormalizable flows. φ⁴_3 has λ_k = L^k λ_0 (I, eq. 106; Theorem 14, eqs. 179-182). QED has
     e_k = L^{k/2} e_0, and "there are no marginal terms" (2204.07201, p.13).
   - Exponents in the d = 3 analogues: ||E_k(X)|| ≤ e_k^{1/4-7ε} e^{-κ d_M(X)} (QED Prop. 1, eq. 30), and
     β < 1/4 - 10ε (φ⁴, II eq. 212).
   - Needed: CMP 109 (1987) 249-301, CMP 116 (1988) 1-22 and CMP 119 (1988) 243-285.
5. **R-operation (L5).**
   - Dimock: absent from every exposition. "This difficult step is not necessary for this model" (II, p.31, Remark 3);
     QED has none either.
   - Needed: CMP 122 (1989) 175-202 and CMP 122 (1989) 355-392.
6. **UV stability in 4D (L6).** This is the assembly of 1-5.
   - 3D templates: φ⁴_3 III Corollary 1 (p.33, eq. 225), with arbitrary M and bulk dependence; QED Theorem 2 (p.8,
     eq. 42), unit volume, "works equally well for any finite volume" (2204.07201, p.2-3). The 3D pure-gauge template is
     CMP 102 (1985) 255-275 [not-read].
   - The review.md §1 "small physical volume" question is settled for φ⁴_3 (M arbitrary, [read]) but still open for 4D YM.
7. **Scalar coercivity source:** CMP 89 (1983) 571-597 (Dimock III Lemma 20's citation).

- **[S2] Literature status of E8** (Dimock II, arXiv:1212.5562, full-text HTML read via a summarising fetch: data only,
  paraphrased; scalar φ^4 in 3D, not gauge).
  - Large-field regions are defined by characteristic functions χ, ζ with thresholds p_k = (-log λ_k)^p (§1, eq. 10).
  - Each large-field cube contributes e^{-O(1) p_0^2}, so a region Ω^c carries e^{-O(1) p_0^2 |Ω^c|_M}.
  - The result is a sum over decreasing regions Ω_1 ⊃ Ω_2 ⊃ ..., with exponentially decaying polymer activities.
  - **No local, volume-uniform probability bound of E8 type is stated** in the part read (the first 100k of 159k
    characters).
  - So E8 is NOT already in Dimock I-II as a stated result. The structure (a *local density-level* suppression, plus
    local polymers) is exactly what the E8 route needs: a ratio Z(B forced large)/Z ≤ e^{-c p^2} × (polymer
    correction). Whether Balaban's gauge papers state it is unknown [unverified-exact-statement]; their bodies were not
    read. **[S5]** Superseded by the direct reading of Dimock II-III and QED (NOTES.md): the absence of an E8-type
    probability statement is confirmed in the parts read; the density-level mechanism is Dimock III Lemma 13.

### L7. The continuum limit on T^4_M
- **L7.0. Tuning at each fixed K: PROVEN-HERE. Tuning to a K-independent w*: GAP (OPEN, estimate E7.0).**
  [R1-fix: session 1 claimed a fixed w* for all K; that does not follow.]
  - **Definitions.** RC is read with the continuous cut-off observable w̃ = ζ · (1 - N^-1 Re tr V^(0)_p). Here
    ζ ∈ [0, 1] is a continuous gauge-invariant function. It equals 1 when every averaging step inside the four
    resolution-0 blocks of p satisfies ||Z_y - 1|| ≤ τ_N/2, and 0 when some step has ||Z_y - 1|| ≥ 3τ_N/4.
    - τ_N := min(1, 2 sin(π/N)). [R1-fix] For N ≥ 13 the session-1 thresholds 1/2 and 3/4 did not imply D_N.
  - **Statement (per K).** For each K, β ↦ E_{K,β}[w̃] is continuous on [0, ∞) and tends to 0 as β → ∞. Its value
    w̃_0(K) at β = 0 is > 0. Hence every w* ∈ (0, w̃_0(K)) is attained at that K.
  - **The gap.** At β = 0 the links are i.i.d. Haar. ζ = 1 needs about L^{4K} of the Z_y, many with disjoint supports, to
    lie in a fixed ball. So w̃_0(K) → 0 super-exponentially in K, and even sup_β E_{K,β}[w̃] ≥ c > 0 uniformly in K is
    unproven.
  - **Estimate E7.0 (OPEN).** There are c > 0 and β-ranges such that sup_β E_{K,β}[w̃] ≥ c for all K. Its content is a
    large-field suppression statement, of L6/E8 type: with high probability all averaging steps stay in the domain.
    The RC, L7c and LOG decision 1 all need E7.0.
  - **[S3, R3-fix] E7.0 restricted to the AF window is FALSE for N = 2, 3, 4** (E8.3, consequences, threshold 3τ_N/4):
    sup_{β ≤ λK} E_{K,β}[w̃] → 0 for 3λx^2 < 4 ln L. E7.0 itself (sup over all β) is not falsified. The
    cut-off RC is replaced by S5' (L6loc), whose per-K tuning is PROVEN and whose K-uniformity is the Haar statement
    E7.0' (OPEN).
  - **Proof.**
    - Continuity: dominated convergence on the compact configuration space (the integrand is continuous and bounded,
      and the density is continuous in β).
    - w̃_0 > 0: w̃ is continuous, non-negative, and positive on a non-empty open set.
    - β → ∞: by Laplace's principle on the compact space, μ_β concentrates on the flat set {U_p = 1 for all p}.
      - On a flat configuration every Z_y is the holonomy of a null-homotopic loop (zero winding on the torus), so
        Z_y = 1, ζ = 1, and U' = T_{c_X}.
      - Every coarse plaquette is the holonomy of a null-homotopic loop, so it equals 1 and w̃ = 0. This includes flat
        configurations with non-trivial torus holonomy.
      - [R1-fix] Session 1 wrote "contractible union of blocks". That fails when the coarse torus has side ≤ 2; zero
        winding is the correct reason.
    - w̃ is continuous, so E_β[w̃] → 0. Conclude by the intermediate value theorem. ∎
  - That the tuned β_K lies in Balaban's regime for small w* is part of L4a and L6 (imported).
- **L7a. Subsequential limits at every resolution: PROVEN-HERE (content-free alone).**
  - Statement: for any sequence β_K, there is a subsequence along which, for every m, the law ν_{K,m} of V^(m) (a
    probability measure on the compact space C_m = G^{links of Λ_{m,M}}) converges weakly.
  - Proof: Prokhorov on a compact metric space, then a diagonal argument over m ∈ N. ∎
- **L7b. Convergence of the whole sequence: OPEN. The first open estimate of the DAG is E7.**
  - **E7 (trajectory Cauchy estimate).** Assume RC with w* ≤ w_*(N, L). There are κ > 0 and C < ∞ such that for all
    K ≥ m ≥ 0, M ≥ 0, every union X of resolution-m blocks, and every gauge-invariant f : C_m(X) → C with
    ||f||_∞ ≤ 1:
    |E_{K+1}[f(V^(m))] - E_K[f(V^(m))]| ≤ C |X|_m L^{-κ(K-m)},
    where |X|_m is the number of resolution-m blocks in X.
  - E7 is summable in K, so it gives convergence of all of O, with cutoff effects O(ε^κ). It is stated for the
    observable expectations so that it does not depend on Balaban's internal norms.
  - **Sub-estimates (all OPEN).**
    - **E7.1 (one-step comparison).** The (K+1)-theory after one step equals a Wilson action at the tuned coupling plus
      an irrelevant remainder R. R must be measured in Balaban's polymer norm, with size O(g^{2+δ}) or carrying
      L^{-κ}. L4c shows that O(g^2) is not enough.
    - **E7.2 (contraction).** The linearised RG map on Balaban's space of effective actions contracts the irrelevant
      directions by L^{-κ} per step, uniformly for g ≤ g_*, including across the large-field/small-field interface. The
      marginal direction is fixed by RC.
    - **E7.3 (tuning stability).** The tuned β_{K+1} and β_K differ by an amount the marginal flow absorbs, with error
      O(L^{-κK}).
    - **E7.4 (from norms to observables).** A polymer-norm difference of the effective densities on X gives an L^1
      difference of the X-marginals. This is a cluster-expansion ratio bound that uses L6loc.
  - **Note.** In the Dimock/Balaban scalar expositions only the stability bound is proved. No correlation-function
    convergence was found in the abstracts read.
  - **[S2] Toy test of E7 / E7.2: Migdal-Kadanoff SU(2), d = 4, b = 2 (check c7). FINITE DIAGNOSTIC, toy only.**
    - **Map.** Bond moving w → w^{b^2}, then decimation a_n → a_n^{b^2} on the character coefficients. This is an exact
      block map of a hierarchical model [m: A. A. Migdal, Sov. Phys. JETP 42 (1975) 413 and 743; L. P. Kadanoff,
      Ann. Phys. 100 (1976) 359; exactness for gauge models unverified], and an uncontrolled approximation of
      the real 4D RG.
    - **E7 analogue holds.** Tune a_1 = a* after K steps; the tuned resolution-0 weights converge geometrically in K.
      - The per-step ratio of D_K is 0.067 at a* = 0.6 and 0.0636 at a* = 0.9, tending to b^-4 = 1/16 at weak coupling.
      - Four bare families converge to the same limit with the same rate: Wilson, Wilson + adjoint, a large-field bump
        (factor 3 at θ > 2.2), and heat kernel.
      - The tuned β_K grows linearly in K (asymptotic-freedom-like). The implied MK coefficient 0.0457 is close to
        11·2/(48π^2) = 0.0464. This is not claimed as anything.
    - **Rate explained (derived here at leading order in small t; heuristic, since the re-expansion step is not controlled).**
      - Near a heat kernel K_t, a quartic-Casimir deviation u enters log w as (u/t^2) f(θ/√t).
      - Bond moving multiplies log w by p = b^{d-2} and maps t → t/p. Re-expanded on the new width, it gives
        u → u/p^3.
      - Decimation multiplies both t and u by b^2.
      - In d = 4 (p = b^2): t is marginal and u → u b^-4. The measured 1/16 matches.
      - In the real 4D RG the leading irrelevant (dimension-6) operators contract only like L^-2. So the MK rate is
        faster than the expected true κ = 2 (up to logs).
    - **Large fields in the toy.** The bump's effect falls from 7.6e-5 (K = 1) to 2.2e-9 (K = 3) at a* = 0.6. The power
      w^{b^2} suppresses large θ super-exponentially. [R2-fix] This sub-test is VACUOUS: the bump is a pointwise
      deformation that the power w^p kills trivially (at a* = 0.9 its effect is 1e-15). It tests nothing about large-field
      regions. The [S3] toy c11 has spatial large-field regions.
    - **Limits of the toy.** MK has no spatial large-field regions, no small-field/large-field interface, and no
      polymer tails. So it confirms only that the E7 *structure* (RC fixes the marginal direction; everything else
      contracts geometrically; the bare large-field shape is irrelevant) is consistent in an exact block map. It is NOT
      evidence for E7.2 in 4D Wilson theory, and in particular not across the interface.
  - **[S3] Toy test with spatial large-field regions: inhomogeneous MK tree (check c11). FINITE DIAGNOSTIC, toy only.**
    - **Model.** A hierarchical lattice: each node at depth k has 16 children (2^4 sub-blocks). Bond moving sums the
      children's log weights within each of the 4 decimation slots, and decimation multiplies the 4 slot coefficient
      vectors. With all leaves equal this is c7 exactly (T0: 7e-16). Leaves in a region R carry a strong-coupling bare
      weight (β_R = 0 Haar, or 0.5); the rest carry the tuned Wilson weight (homogeneous RC, a* = 0.6). Interface nodes
      have mixed leaves. Criteria were pre-registered in the script before the first run.
    - **T1 (PASS).** A fixed fine-size Haar defect (2^4 leaves straddling every dyadic boundary) affects the root by
      2.1e-3, 1.4e-4, ..., 2.7e-9 at K = 3..8, with per-step ratio 0.066: the volume factor b^-4 = 1/16 again.
    - **T2 (PASS).** A fixed *physical* strong-coupling region (box with 1/16-dyadic corners, β_R = 0.5): the tuned root
      converges in K. The Cauchy differences are 6.9e-4, 6.6e-6, 6.9e-8, 4.6e-9 (ratios 0.0095, 0.0105, 0.066), with
      limit a_1 = 0.590749 against 0.6 without the region. So the E7 structure survives a deterministic large-field
      region of fixed physical size in this toy.
    - **T3 (pre-registered FAIL; a finding).** The per-node sup-norm contraction Δ(parent)/max Δ(children) between runs
      K = 7 and 8 is 0.070 at exterior nodes but **0.667 at interface nodes** (86 node classes), above the
      pre-registered 0.5. The first-run output is kept as checks/c11_out_firstrun.txt; the criterion is NOT changed.
    - **T3b (diagnostic, hypothesis written before running, FALSIFIED).** I predicted the factor a_1(ext slot)^3 → 1 as
      a* → 1, from a lone small-field child that bond moving does not dilute. The measured worst interface ratio is
      0.667, 0.604, 0.617, 0.603 at a* = 0.6, 0.8, 0.9, 0.95, i.e. flat and well below the prediction (0.74 → 0.96). The
      mechanism is not identified.
    - **Reading for E7.2.** In this toy the contraction across the interface is uniform in the coupling but about 10×
      weaker per step than in the bulk (≈ 2/3 vs ≈ 1/16). The global Cauchy rate is still geometric (T2), because
      interface nodes are a vanishing fraction of each level. If the same holds in 4D, E7.2 needs a norm that tolerates
      a slower interface contraction, weighted by the interface's volume fraction, rather than a uniform per-block
      contraction constant. This is a heuristic reading of a toy.
    - **Limits.** Exactly local by construction (a tree): no polymers, no configurations, no random large-field regions.
      The regions here are deterministic bare inhomogeneities, not fluctuations. **[R3-fix]** The box corners are
      1/16-dyadic, so every node at depth ≥ 4 is pure and interface nodes exist only at depths ≤ 3: the toy never
      iterates an interface contraction and cannot say whether the slow factor compounds. "Vanishing fraction" above
      means "finitely many levels". The [S4] check c15 addresses both the mechanism and compounding.
  - **[S4] Mechanism of the slow interface contraction (check c15: 5 PASS / 3 FAIL, 5 s; first run kept as
    c15_out_firstrun.txt). FINITE DIAGNOSTIC, toy only.**
    - **Mechanism (identified).** At an interface node, a decimation slot holding j small-field children and 4 - j
      near-Haar (log w ≈ 0) children performs bond moving with power j instead of b^{d-2} = 4: locally the node is an MK
      step of effective dimension d_eff = 2 + log_2 j. The irrelevant deviation then contracts by ≈ b^2/j^3 at leading
      order (the c7 rate argument with p = j).
    - **Evidence.** A synthetic parent (4 slots of j copies of the c11 exterior node plus 4 - j exact Haar children)
      reproduces the c11 interface class with RRSS slots exactly (0.5266 vs 0.5266, j = 2). The exterior class (0.0704
      vs j = 4: 0.0691) misses the pre-registered 1e-3 tolerance, so H1 is recorded as FAIL. Synthetic ratios
      r(j = 1..4) = 1.12, 0.53, 0.21, 0.069 (a* = 0.6) and 1.20, 0.45, 0.19, 0.065 (a* = 0.9): ordered and coupling-flat
      within 14% (H2, H3 PASS), which explains the flatness that falsified the session-3 hypothesis. The worst c11 class
      (0.667) has interface children, so it is a mixture of j = 2 slots and interface sub-slots.
    - **Prediction confirmed (H4, H5).** A small-field box inside a strong sea has j = 1 slots at its corners. Predicted:
      no per-node contraction. Measured worst ratio 1.1201 (> 1) at a node with slots RRSR × 4, reproduced exactly by the
      synthetic j = 1 model. (Process: H5 first FAILED from a script bug, the synthetic reference being a strong-region
      node in the complement geometry, giving 0; fixed and rerun; the first output is kept.)
    - **Compounding (REVIEW_S3 point 6; H6 FAIL, H6' FAIL, H7 PASS).** Half-space strong region x_2 < 1/3 (non-dyadic,
      so interface nodes exist at every depth). The root response to an adjoint-character perturbation of the first
      small-field leaf layer, divided by the response to the same perturbation of a bulk layer at x_2 = 2/3, is
      0.91, 1.00, 0.92, 1.01, 0.94 for K = 6..10: flat, not increasing (H6 FAIL). Both decay by ≈ 1/2 per K, i.e. like the
      layer volume 2^-K: the root response is dominated by the marginal (coupling) component, which MK averages over
      children (REVIEW_S3's alternative). H7 PASS: the interface response decays (steps 0.47-0.56). H6' (added after the
      first run): removing the component along the tuned family's tangent gives residual ratios 25.4, 5.6, 3.3, 3.3, 2.9,
      decreasing, so FAIL, and the bulk residual itself is erratic (steps 2.47, 1.18, 0.55, 0.59). A single tangent does
      not isolate an irrelevant subspace for a position-dependent perturbation, so H6' is inconclusive by construction.
      INFO: a boundary normal to a decimation coordinate screens completely (the interface-layer response is 0 to double
      precision), because a strong slot makes the parent near-Haar.
    - **[R4-fix] Downgraded.** c15 is a FINITE DIAGNOSTIC, not a proof. The 0.5266 match is a bookkeeping identity (the
      synthetic parent recomputes the c11 slot arithmetic on the same children). The leading-order law b^2/j^3 fits
      poorly (j = 1: predicted 4, measured 1.12; j = 3: predicted 0.148, measured 0.21); only the ordering (H2) is
      supported. The claim "E7.2 needs a geometry-weighted norm" is WITHDRAWN: (1) rests on the j = 1 corners, which
      (3) calls an MK artefact, and the face/bulk rates L^-1, L^-2 are both < 1, so a uniform per-block contraction at
      the slower rate is not excluded; in 4D interfaces arise from random large-field regions handled by L5, whose polymer
      norms are already geometry-weighted. What remains is a toy-informed design note: "the contraction constant should
      be the face rate, or weighted by type". H6 (no compounding beyond the volume fraction) is the useful toy-only
      finding. The original text follows for the record.
    - **Design note for E7.2 (was "Decision", session 4).**
      - (1) A contraction constant that is uniform per block is FALSE in the toy (j = 1 corners: 1.12-1.20 > 1). So E7.2
        cannot be stated as "every block's irrelevant part contracts by L^-κ". It must be stated in a norm that weights
        deviations by their geometric type (bulk, face, corner), or summed over a region with volume weights.
      - (2) In this toy, the influence of an interface on the root does not compound beyond its volume fraction (H6, H7).
      - (3) Real 4D (heuristic, dimension counting only): gauge-invariant local operators have dimension ≥ 4, so a
        face-localised one scales like L^{3-4} = L^-1 per step and a corner-localised one like L^{2-4}. The MK j = 1
        non-contraction has no counterpart in this counting: it is an MK slot artefact (a lone child is an undiluted
        lower-dimensional system). The slower face rate (L^-1 against the bulk L^-2) is generic and must be built into
        E7.2's norm.
      - Not a threat to E7.2 as a statement about expectations; a constraint on its proof.
- **L7c. Non-triviality at resolution 0: CONDITIONAL on E7.0 (moved from PROVEN-HERE). [R1-fix]**
  - w̃ is a function of the fine field, not of V^(0). What holds is E_K[w(V^(0)_p)] ≥ E_K[w̃] = w*, since w ≥ w̃ ≥ 0
    on D. The session-1 "= w*" was wrong.
  - The inequality passes to the limit because w is continuous.
  - So, given a K-uniform w* (E7.0), the limit is not concentrated on pure gauge. [S3] E7.0 fails in the AF window;
    under S5' the same argument needs E7.0' and, to pass w ∘ V^(0) through the limit, E8* at level 1 (w ∘ S4'' is
    discontinuous on the branch set). This is weak; the meaningful version
    is L10.

### L8. Infinite volume
- **L8a. Subsequential limits as M → ∞: PROVEN-HERE.** The laws of V^(m) restricted to any fixed bounded region form a
  tight family on a compact space. By Tychonoff the product over all links of Λ_{m,∞} is compact, so a diagonal
  subsequence (M_i, K_i) converges for every m. ∎
- **L8b. Invariance: PROVEN-HERE in a narrowed form. [R1-fix: the session-1 statement was WRONG]**
  - The limits are invariant under resolution-m lattice translations (period L^-m), and under coordinate reflections
    through block-aligned hyperplanes (by L9a'), for every m along the subsequence.
  - Proof: weak limits of invariant measures are invariant. The torus measures are invariant, and the block map
    commutes with these operations: translations preserve every finer grid, and reflections are covered by L9a',
    which holds everywhere for S4'' with the odd branch rule [R3-fix; session 3 cited the withdrawn "failed link := 1"
    extension here], so V^(m)[θU] = θV^(m)[U] holds everywhere. ∎
  - **Axis permutations are NOT symmetries of the block laws under S4.** S4 fixes the path order 1, 2, 3, 4, so for a
    permutation R, V^(m)[RU] ≠ R V^(m)[U] in general.
  - **[S3] With S4' (order-averaged): the full hypercubic group.** V^(m)[πU] = πV^(m)[U] for axis permutations π
    (S4' re-checks; c8(d)), everywhere for S4'' [R3-fix]. The torus measures are invariant
    under π (the torus side is the same in every direction). So the limits are invariant under resolution-m translations,
    block-aligned reflections and axis permutations about a block centre: the hypercubic group at every resolution.
    PROVEN-HERE (same weak-limit argument). L3s' is unaffected (it uses its own scalar average).
- **L8c. RP is preserved: PROVEN-HERE, given L9a (incl. the mixed reflection L9a-m) and L9a'.**
  - For continuous f supported in a positive half-space union of blocks (for the mixed reflection: excluding the block
    cut by the fixed site plane Π_s, which is a block mid-plane [R2-fix]), ⟨θ(f)^* f⟩ ≥ 0 holds at every (K, M) and is a
    closed condition under weak limits. ∎
  - [R1-fix (a)] The fine torus side L^{K+M} is odd. A reflection through a block-boundary link plane therefore fixes the
    antipodal *site* plane: it is a mixed reflection, and L9a-m covers it.
  - [R1-fix (b), superseded by R3-fix] The measurable extension of the block map off D must be θ-covariant. Sessions 2-3
    set failed coarse links to 1. From session 4 the extension is S4'' with the odd branch rule (S4), which is
    θ-covariant everywhere by the L9a' computation (it uses only log(Z^-1) = -log Z and conjugation covariance, which
    the odd rule makes exact for all Z), and local (L0). So V^(m)[θU] = θ V^(m)[U] holds everywhere.
- **L8d. Uniformity: OPEN.** Non-triviality and consistency in infinite volume need E8 (L6loc) uniform in M.
- **The obstruction, stated exactly.**
  - The RG stops at resolution 0, where g is small. What remains is a lattice gauge theory with compact variables,
    strongly coupled at large distances.
  - Existence of limit points needs no infrared control: L8a is pure compactness.
  - The infrared coupling growth blocks:
    - (1) uniqueness of the infinite-volume state, i.e. independence of the subsequence and of the boundary conditions;
    - (2) clustering (OS4);
    - (3) the mass gap;
    - (4) through (1), the universality route to rotation invariance (L9b-β).
- **What the OpenAI claim must have done (inference, not fact).** Either:
  - (A) stay on T^4. Then OS1 fails, so "OS axioms" would have to be read as torus axioms. Or
  - (B) take infinite-volume limit points by compactness, as here, and solve L9b without uniqueness. Or
  - (C) prove uniqueness on R^4, which seems to require IR control comparable to a mass gap, which is not claimed.
  - (B) is the most consistent with "existence, no mass gap".

### L9. The OS axioms
- **L9a. RP of the Wilson action, link reflection and site reflection: IMPORTED-AND-REVERIFIED.**
  - **Source.** Osterwalder-Seiler, "Gauge field theories on a lattice", Ann. Phys. 110 (1978) 440 [v-R1, via a citing
    paper].
  - **[R4-fix] Scope.** RP holds for bounded measurable gauge-invariant F of the positive-half links, not only continuous
    ones: the written proof integrates F against the gauge-fixed product Haar measure and uses no continuity. E8*-red
    uses this extension.
  - **L9a-m. [S2, R1-fix] Mixed reflection on an odd torus: PROVEN-HERE (re-derived).**
    - Setting: θ fixes one link plane Π_l and, antipodally, one site plane Π_s. Assume side ≥ 3, so the two are distinct.
    - Gauge-fix the crossing links at Π_l to 1, by a gauge transformation on the positive-half sites adjacent to Π_l.
      It does not touch Π_s.
    - The links inside Π_s (call them W) are θ-fixed. Links from Π_s into either half belong to that half. Plaquettes
      inside Π_s are functions of W alone.
    - Then e^{-S} = h(W) e^{A_+(U_+, W)} θ(e^{A_+}) Π_{crossing p at Π_l} exp((β/N) Re tr(G_p θ(G_p)^†)), with A_+ real.
    - Expanding the crossing factors as in L9a and using Haar product structure, for every W:
      ∫ θ(F) F̄ e^{-S} dμ(·|W) = h(W) Σ_α c_α |∫ F Ḡ_α e^{A_+} dμ_+(·|W)|^2 ≥ 0, with c_α ≥ 0.
    - The equality uses that θ preserves the measure and fixes W, and that A_+ is real. Integrating over W ≥ 0 gives
      RP. ∎
    - Not separately checked numerically: c4 covers only pure link and pure site reflections.
  - **Proof re-derived (link reflection θ: t → 1 - t, on T^4 or Z^4).**
    - The links crossing the reflection plane(s) are pairwise disjoint edges and contain no loop. A gauge
      transformation supported on the positive half sets them to 1; it leaves gauge-invariant positive observables and
      the measure unchanged.
    - Then e^{-S} = e^{A_+} θ(e^{A_+}) Π_{crossing p} exp((β/N) Re tr(W_p θ(W_p)^dag)), where A_+ is positive-half
      measurable and W_p is a positive-half link.
    - Re tr(W θ(W)^dag) = Σ_{ab} Re(W_ab conj(θW_ab)) is a sum of terms G θ(Ḡ) + c.c.
    - Expanding the exponential gives a non-negative combination of products G_α θ(Ḡ_α). The Haar measure factorises
      as dμ_+ dμ_-, and θ is measure preserving.
    - So ⟨θ(F) F̄⟩ = Σ_α c_α |∫ F G_α e^{A_+} dμ_+|^2 ≥ 0, with c_α ≥ 0 when β ≥ 0. ∎
    - Site reflection is analogous. The plane variables are shared, and the plaquettes in the plane belong to both
      halves; split their weight symmetrically.
  - **Check c4.**
    - Exact enumeration for Z2 on 4×2: the RP matrix is PSD, minimum eigenvalue ≥ -2e-17, for both reflections. The
      non-RP control has minimum eigenvalue -1.5e-2 (link) and -1.7e-3 (site).
    - The SU(2) and SU(3) kernels exp(β Re tr W V^dag) are PSD for β ≥ 0 and not PSD for β = -1.
  - **Note.** β < 0 is *not* a usable negative control for Z2 (observed PSD; presumably a π-flux relabelling, not
    proven).
- **L9a'. Block observables are reflection covariant: PROVEN-HERE.**
  - Statement: for a reflection through a resolution-m block-boundary hyperplane, θ maps O_m(X) to O_m(θX), and
    V^(m)[θU] = θ(V^(m)[U]), with link orientation reversed in the reflected direction.
  - Proof: the complete-axial path between two sites is determined by its endpoints and the fixed order of directions.
    A coordinate reflection preserves that order and maps monotone segments to monotone segments, so it maps
    complete-axial paths to complete-axial paths.
  - For L odd the block centres map to block centres when the plane is a block boundary. Straight legs map to straight
    legs (reversed when the reflected coordinate is μ).
  - Directions other than the reflected one: the path set maps bijectively onto the path set of the reflected link,
    the reference maps to the reference, and the identity is exact.
  - **Reversal (reflected direction μ).** Let the reflected link run from X' to X' + e_μ.
    - Its paths are the images of the original reversed paths T̃_{y} = T_{y-Le_μ}^-1, for y ∈ B(X + e_μ).
    - Its reference is T̃_{c_Y} = T_{c_Y - Le_μ}^-1 = T_{c_X}^-1, because c_Y = c_X + L e_μ.
    - Write Z_y = T_{c_X}^-1 T_y. Then T_{c_X} T_y^-1 = T_{c_X} Z_y^-1 T_{c_X}^-1, and the reversed average is
      T_{c_X}^-1 exp(avg log(T_{c_X} Z_y^-1 T_{c_X}^-1)) = T_{c_X}^-1 T_{c_X} exp(-avg log Z_y) T_{c_X}^-1 = U'^-1.
    - This uses log(W Z W^-1) = W log(Z) W^-1 and log(Z^-1) = -log Z (principal branch on D; for every Z under the odd
      branch rule of S4'' [R3-fix], so the identity extends to S4'' everywhere). ∎
  - **Check c1(f).** Exact to 1e-15 for SU(2) and SU(3), for both the reflected and an unreflected direction.
  - A draft of this lemma wrongly flagged a reference asymmetry; the computation above removes it, see LOG.
- **L9b. Euclidean invariance (OS1): OPEN. This is the hard core.**
  - (α) On T^4 it is false by geometry.
  - (β) Continuum translations. Only translations by multiples of L^-K are exact symmetries. Translation by a general
    vector needs grids offset by fine-lattice vectors. **Estimate E9.1:** for f ∈ O_m(X) with Lipschitz constant 1,
    |E_K[f(V^(m)_{grid+a})] - E_K[f(V^(m)_{grid})]| ≤ C |X|_m (L^m |a|)^γ, uniformly in K, for some γ > 0. E9.1 plus
    L8b gives exact R^4 translation invariance of the limit.
  - (γ) Rotations. There is no lattice rotation beyond the hypercubic group.
    - **Remark R9.1:** averaging the limit over SO(4) gives invariance but destroys RP. A convex combination of
      measures that are RP with respect to different planes is not RP with respect to a fixed plane in general. This is
      not a proof of impossibility, only of the failure of the naive route.
    - **Route γ1 (universality).** The limit on a common continuum state space is independent of the lattice
      orientation. This needs E7 plus discretisation independence, and in infinite volume probably uniqueness (blocked,
      see L8).
    - **Route γ2 (two families).** A rotation-covariant family, e.g. gradient-flow observables at flow time t > 0
      [m: Lüscher, JHEP 08 (2010) 071; reviewer: consistent, not web-confirmed], provides OS1. The block family provides OS2. One must prove that both generate the same
      limit state, i.e. a 4D state space à la Cao-Chatterjee (3D: arXiv:2111.12813 [v]; CMP 405 (2024), no. 1, art. 3, DOI
      10.1007/s00220-023-04870-y [v-R2]). Flowed observables
      are not exactly local, so they cannot carry RP themselves.
- **L9c. OS0 regularity: OPEN.** The block observables are bounded, so their Schwinger "functions" are bounded, but
  they are not distributions in local fields. OS reconstruction needs a local field algebra with E(4) action. This is
  tied to γ2. E9.1 and E7 are the needed uniform estimates.
- **L9d. Clustering (OS4): OPEN.** Whether RP survives the ergodic decomposition of a translation-invariant RP state is
  [unverified]. Without a gap or uniqueness this is not available.

### L10. Non-triviality (not a free theory): OPEN
The target is a short-distance statement: for example, a connected 4-point function of resolution-m linearised fields,
or the β-function seen in O, differs from the free value at order g_m^4. It needs E7-level control.

### QCD and the GUT (carried from review.md; not attacked)
- **F1.** RP for Wilson fermions: IMPORTED-NOT-YET-REVERIFIED (Osterwalder-Seiler 1978 [unverified-citation]).
- **F2-F4:** OPEN.
- **C1-C4:** OPEN.

---

## 3. Tally (after session 20)
**[S20] Tally: 72 / 2 / 7 / 24 (main path) + 1 comparison-branch item.**
- **REVIEW_S18_S19 confirmed 71 / 2 / 7 / 24 + 1** (TS/R1, N5-triv, RW, N5-sf0 CONFIRMED or CONFIRMED-WITH-FIX; 0 GAP, 0 WRONG).
- **PROVEN-HERE: 72** (71 + 1 [S20], unreviewed): **Theorem NAH1** ((NA-H_loc) at level 1 for the critical branch; Lemmas U0,
  FPq, N5-an♭, BR1, SC1, LOC and Corollary N5-sf1 counted with it). Not counted: Proposition RW-ℓ² (strengthens RW (iii) and
  N5-sf0); the exact-rational redo of Lemma N5-w0; Proposition NAH-ind (an implication); the [R1819-fix] edits; c36.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7**; **OPEN (main path): 24**; comparison branch: unchanged
  (N5 stays OPEN: (MIN_1), levels i ≥ 2 via (BG-unif), small tori, FP_U; see the [S20] N5 node status).

**[S19] Tally: 71 / 2 / 7 / 24 (main path) + 1 comparison-branch item (superseded by [S20] above).**
- **PROVEN-HERE: 71** (69 + 2 [S19], unreviewed): **Theorem RW** (with Lemma CT♯ and Corollary RW-triv counted with it) and
  **Theorem N5-sf0** (with Lemmas N5-cov, AX, N5-an counted with it). Not counted: Proposition N5-sf_i (an implication from
  the OPEN (NA-H_loc)); Lemma N5-w0 (strengthens N5-triv at i = 0, no count change); measured γ values; c35.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7**, unchanged.
- **OPEN (main path): 24**, unchanged (N5 stays OPEN: levels i ≥ 1 at non-trivial backgrounds via (NA-H_loc), small tori,
  FP_U; see the [S19] N5 node status).
- **Comparison branch:** unchanged.

**[S18] Tally: 69 / 2 / 7 / 24 (main path) + 1 comparison-branch item (superseded by [S19] above).**
- **After REVIEW_S16_S17 (session 17 corrected): 67 / 2 / 7 / 24 + 1.** S16: Lemma F-df_0 CONFIRMED (64). S17: four RLARGE
  items counted, of which three confirmed: **Lemma GT-lat'** (lattice Taylor lemma without point symmetry, general coarse
  links, B_4 orbit averages; CONFIRMED), **Proposition CL** (exact Fubini identity, factorisation over *-components,
  per-cube-uniform frozen size bound; CONFIRMED-WITH-FIX, CL-1 applied), **Lemma RS** (one-step re-seeding of a coarse large
  field; CONFIRMED); and **Theorem TS + Theorem R1** (counted as one item): GAP (R1 (iii)'s B_4 step false as written; TS's
  hypothesis region too small).
- **PROVEN-HERE: 68** (67 + 1 [S18-repair], unreviewed): **Theorem TS + Theorem R1, repaired** (RLARGE §7.2-§7.3: tuple
  localisation on unfattened supports, Lemma 7.2-0, torus-wrap term, TS on Δ_*). This is the review's own restoration
  condition (R-3a, R-3b, R-4, R-5 written); the repaired text has not been reviewed.
  - Not counted: Remark 7.2-B (the value of the coupling shift is unchanged under any translation-class-normalised
    localisation; ARGUED level); (P1)-(P3), (P5) (arithmetic); (P4) (ARGUED); c33.
- **PROVEN-HERE: 69** (68 + 1 [S18], unreviewed): **Theorem N5-triv** (end of file; with Lemmas CT, N5-sl, N5-coer,
  N5-loc counted with it): the per-level gauge-fixed soft fluctuation covariance at the trivial background is
  exponentially local, with N5's ℓ² and ℓ¹ bounds, explicit constants, uniformly in i, k, T. Not counted: c34.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged.
- **OPEN (main path): 24**, unchanged (N5 stays OPEN: general backgrounds and the random-walk expansion remain). Inside L5,
  RLF (RLARGE §1A) is reduced, conditionally, to (F), (SF), (H-pos) [P],
  (H-Mayer), (PLD), (W1-ret'), (HIST) [P], (SF-last).
- **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.

**[S16] Tally after session 16 (superseded by [S18] above):**
**[S16] Tally: 64 / 2 / 7 / 24 (main path) + 1 comparison-branch item.** The REVIEW_S15_CONVERGENCE fixes (step 1,
[R15-fix]) change no count: the review confirmed every counted S15 item (0 GAP, 0 WRONG; two CONFIRMED-WITH-FIX
wording/label fixes) and the 63 / 2 / 7 / 24 + 1 tally.
- **PROVEN-HERE: 64** (63 + 1 [S16], unreviewed):
  - **Lemma F-df_0**: an exponentially local extension of the fine-curvature map F ↦ f_0 to all coarse 2-forms,
    |K| ≤ (2M/(m_*' - m'))e^{-m'|X|_1} for every m' < m_*', uniformly in k, T, u (explicit analytic Koszul factorisation).
  - Not counted: the c31 instances (E-low at symbol and chain level; the NA-lev arithmetic).
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged.
- **OPEN (main path): 24.** No top-level OPEN item is discharged. Narrowed content: as in [S15] below, with Lemma F-df_0
  removed from BG-reg/N2's list, the NA-lev scope narrowed ([R15-fix]: the multi-level uniformity is carried by
  (NA-H) ⊂ B-NA), and (G♯_0-fine-up) now a displayed inequality.
- **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.
- **[R15-fix] Progress metric.** REVIEW_S15_CONVERGENCE (a)-(b) shows the flat 24 is a counting artefact; the critical-path
  DAG with paper-scale / session-scale weights (reproduced in LINEAR_PACKAGE.md §10) is the honest progress measure.

**[S15] Tally (superseded by [S16] above): 63 / 2 / 7 / 24 (main path) + 1 comparison-branch item.** After the REVIEW_S13_S14 fixes (step 1) the
tally is 60/2/7/24 + 1, unchanged: no fix changes a count (the review confirmed every S13/S14 item, 0 GAP, 0 WRONG).
- **PROVEN-HERE: 63** (60 + 3 [S15], all unreviewed):
  - **Theorem G♯_0-soft** (with Lemmas SRC-all, REC, KF): ||r||_{X_s} ≤ C_s(Ω||G||_Y + ||B_k||_{D,m}) for divergence-form
    sources at every level, uniformly in k, T (RTARGET §33 norms);
  - **Lemma LES-div**: the lattice Campanato step with a divergence-form source (C^{0,α} → C^{1,α}, absolute constants);
  - **Proposition NA-lev** (with Lemma E-low): the per-level soft defect bound with no n-loss, E_k ≥ c_E||dB_k||², and the
    per-level abelian gap.
  - Counted with NA-FP (no count change): Lemma NA-crit' (Lagrange form) [R1314-fix].
  - Not counted: the (G♯_0-fine) reduction, the (R♯_ω) statement, the c30 diagnostics.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged.
- **OPEN (main path): 24.** No OPEN item is fully discharged. Narrowed content:
  - **BG-reg / N2 (B-NA)**: inputs now (G♯_0-field) (needs the multi-level per-level-slice gap), (G♯_0-fine) ⇐ (LED-src)
    for level-0 sources plus (G♯_0-fine-up) for sources at levels ≥ 1, Lemma G♯_0-plain (plain level-0 currents), (R♯_ω),
    (FP♯'); (G♯_0-soft) is proven; N10's non-linear analytic dependence; Lemma F-df_0 for N6's interface [S16: PROVEN];
  - **The L3g(a)-slice completion ((NA))**: the per-level gap reduces to (NA-H) (inside B-NA) and a written per-block
    perturbation [R15-fix: was "(no n-uniformity issue left)"; the top-level per-step defect has no n-loss, and the
    multi-level uniformity is carried by (NA-H) ⊂ B-NA]; FP_U(V)'s locality and analyticity;
  - **W1-loc**: its (DF) = {N2 (as above), N4 ((NA-H), per-block perturbation, FP_U), N5, N6}; **D4-obs**: unchanged.
- **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.

**[S14] Tally (superseded by [S15] above): 60 / 2 / 7 / 24 (main path) + 1 comparison-branch item.** No review fixes this session (session 13 is
unreviewed).
- **PROVEN-HERE: 60** (57 + 3 [S14], all unreviewed):
  - **Lemma NA-alg**: the SU(N) maximiser of an average of near-identity unitaries (|X_0 - Ȳ| ≤ 9.2y², ||H - 1|| ≤
    18.4y², y ≤ 1/20) and the two-sided soft-density bound |φ - |ρ|²/(2N)| ≤ (9.2y²/N)|ρ|² + e^{|ρ|}|ρ|³/(3√N);
  - **Proposition NA-FP**: the covariant Faddeev-Popov identity at every critical SU(N) background (direct and
    composite slices), **at the Hessian (Gaussian) level [R1314-fix]**, with Lemmas NA-inv and NA-crit counted with it;
  - **Lemma SRC-id**: fine sources as the effective datum -Q^{(k)}Δ^{-1}j; exact K = 0 screening of 1/φ in the r- and
    f_0-symbols.
  - Strengthened, not counted: Theorem N2-exp' (with Lemma EXP-strip'), m_*' = 0.0384 at κ ≡ 1 [R1314-fix].
  - Not counted: Propositions NA-IFT (standard) and B-NA-red (an implication with OPEN hypotheses); the conditional
    SU(N) N2 analogues; the c29 diagnostics.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged.
- **OPEN (main path): 24.** No OPEN item is fully discharged. Narrowed content:
  - **BG-reg / N2**: the SU(N) chain is reduced to (G♯) (a multi-scale Schauder estimate for the gauge-fixed
    linearised chain on general sources, smooth covariant slice, exponential weights) and (R♯) (the remainder in the
    same norms); plus the non-linear analytic dependence (N10) and the curvature (localised) forms;
  - **The L3g(a)-slice completion**: (NA) is narrowed to the covariant physical gap and the background dependence of
    FP_U; the identity is proven;
  - **W1-loc**: its (DF) = {N2 ((G♯), (R♯); N10), N4 ((NA) gap, FP_U), N5, N6};
  - **D4-obs**: unchanged.
- **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.

**[S13] Tally (superseded by [S14] above): 57 / 2 / 7 / 24 (main path) + 1 comparison-branch item.** After the REVIEW_S11_S12 fixes (step 1) the
count is 55 / 2 / 7 / 24 + 1, unchanged: the reviewer confirmed all six [S11]/[S12] items (three with fixes, applied as
[R1112-fix]).
- **PROVEN-HERE: 57** (55 + 2 [S13], both unreviewed):
  - **Theorem N2-exp**: exponential decay, rate m_*(L, κ_±) > 0 uniform in k and T, of the linearised soft-chain
    kernels F ↦ r and B_k ↦ (r, f_0). Lemmas EXP-id, EXP-real, EXP-strip and Corollary N2-exp-b are counted with it.
  - **Proposition PG^{(k)}**: the physical gap for the composite S4' slice, C_IT(L) = 3.4·10⁶ + 69 + 44160L²/(L - 1).
    Lemma IT-line is counted with it.
  - Not counted: the c28 diagnostics and the located singularity.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged.
- **OPEN (main path): 24.** No OPEN item is fully discharged. Narrowed content:
  - **BG-reg / N2**: the linearised chain is complete (N2-lin + N2-exp); remaining: B-NA (i)-(iii), the SU(N) analogues
    of N2-E, N2-lin and N2-exp, and the non-linear analytic dependence (N10).
  - **The L3g(a)-slice completion**: (FP) and (IT') are complete in the abelian linearised case; (NA) remains.
  - **W1-loc**: its (DF) = {N2 (SU(N); non-linear analytic dependence, N10), N4 ((NA)), N5, N6}.
  - **D4-obs**: unchanged.
- **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.

**[S12] Tally (superseded by [S13] above): 55 / 2 / 7 / 24 (main path) + 1 comparison-branch item.** There are no review fixes this session,
except fix 13 [R910-fix13], which changes no status.
- **PROVEN-HERE: 55** (53 + 2 [S12]). The [S11] and [S12] items are unreviewed.
  - **Theorem N2-lin**: (H1), (H2) in sup form and (LED) for the linearised soft chain, uniformly in k and T.
    Lemmas IT-str, LED-dual, LED-symb and WA, and Proposition LED-unif, are counted with it.
  - **Proposition PG**: the N4 physical gap, c_PG = min(1, κ)/(3.5·10⁶), so O_FP ≥ min(c_PG, 4) on H_0. Lemmas
    PG-flux, PG-orbit, PG-ext and PG-line are counted with it.
  - Not counted: the c26/c27 diagnostics.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged.
- **OPEN (main path): 24.** The count is unchanged, because no OPEN item closes completely. Narrowed content:
  - **BG-reg**: (LED) is proven for the linearised chain [R1112-fix], so BG-reg is now B-NA (i)-(iii), plus the SU(N) analogues of N2-E and N2-lin.
  - **The L3g(a)-slice completion**: the abelian (FP) is complete (FP-ab + PG). (NA) and (IT') remain. (IT)'s
    straight part is settled by IT-str.
  - **W1-loc**: its (DF) = {N2 (SU(N); decay for complex data, N10), N4 ((NA), (IT')), N5, N6}.
  - **D4-obs**: unchanged.
- **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.
- **Decision 4 governance [R910-fix13].** The owner's delegation is now quoted, as recorded in the lead's memory file:
  - 2026-10-21: "you dont need to ask permissions unless we are editing the axioms";
  - 2026-10-23: "remember that you can set whatever works for the TOE here, you dont need to ask me (put it in the CL
    until we have a working TOE)".
  Decision 4 is a proof-technique choice by the lead, applied by inference from this TOE-ruleset delegation
  [R1112-fix] (the delegation does not literally name proof-method choices). It is not an axiom or CL change: the
  "(put it in the CL …)" parenthesis is read as governing TOE rules, and a proof kernel is not one (session-9 record).

**[S11] Tally (superseded by [S12] above).** Two numbers, in order.
- **After the REVIEW_S9_S10 fixes (step 1): 49 / 2 / 7 / 24 (main path) + 1 comparison-branch item.** The added OPEN
  item is **D4-obs** [R910-fix] (compare the soft RG variables' block laws with S4''(U), or run the RG with observable
  sources). The reviewer confirmed all six [S9]/[S10] PROVEN-HERE items (two with fixes, applied as [R910-fix]).
- **After session 11's work: 53 / 2 / 7 / 24 (main path) + 1 comparison-branch item.**
  - **PROVEN-HERE: 53** (49 + 4 [S11], all unreviewed):
    - **Lemma CE-geo'** (|X| ≤ 2^d + 2^{d-1}√d·d(X) under the touching-tree reading; proves the upper inequality of
      Dimock's (122), stated there with d = 3 [R1112-fix]; Theorem CE
      with κ_0 = 16 log 12800 ≈ 151.3, so N6 must deliver κ > ≈ 457 instead of ≈ 9.2·10³);
    - **Lemma N2-E** (k-uniform curvature energy bound for the linearised soft chain), with Lemma N2-a (gauge-orbit
      lemma, abelian and SU(N)) and Corollary N2-ℓ² counted with it;
    - **Proposition N2-red** ((H1) + (H2) ⇐ (LED)), with Lemma LES-sup counted with it;
    - **Lemma FP-ab** (linear Faddeev-Popov), with its soft-step application (the legitimate fixing, the explicit
      weight W of the double fixing, and the reduction of the O_FP gap to the physical gap) counted with it.
    - Not counted: the (LED) attempt (the failing step is named); the c23/c24/c25 diagnostics.
  - **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged.
  - **OPEN (main path): 24**, the same items with narrowed content:
    - **BG-reg** is now (LED) + B-NA (i)-(iii);
    - the **L3g(a)-slice completion**: its (FP) part is now the physical gap on Phys; (NA) and (IT) are unchanged;
    - **W1-loc** depends on (DF) = {N2 (now (LED) + SU(N)), N4 (now the physical gap + (NA), (IT)), N5, N6};
    - **D4-obs** is new [R910-fix].
  - **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.
  - **Decision 4 governance [R910-fix 13].** REVIEW_S9_S10 asks for the owner's delegation in the owner's own words.
    No file read in session 11 contains them, so they were not obtained. The honest label stands: "session-9 lead,
    delegated authority; not an owner ruling".

**[S10] Tally (superseded by [S11] above): 49 / 2 / 7 / 23 (main path) + 1 comparison-branch item.** There are no
review fixes this session.
- **PROVEN-HERE: 49** (46 + 3 [S10], all unreviewed; the [S9] items are also still unreviewed):
  - **Theorem CE**, with Lemma CE-geo, Lemma TG (= Dimock (323)), Proposition CE-κ and Remark CE-cx counted with it.
    It is the corrected, fully proven form of Dimock I Thm 27. [R910-fix] Thm 27's statement says c_0 depends on d
    only; its proof says (p.40) "So c0 does depend on κ"; Proposition CE-κ shows the κ-dependence is necessary (a
    quantifier-order correction, as the author's remark makes; his proof and application are unaffected).
  - **Lemma LES** (the lattice elliptic step, Hölder-α Campanato form, with dF = K allowed).
  - **Proposition BG-b-lin**, with Lemma CR (constant reproduction) and Lemma J-str (no funnel part in the soft
    current at critical points; the fine current is bounded in coarse units) counted with it.
  - Not counted: the non-abelian transfer B-NA (argued); the (DF3') tilt argument (argued); the (DF) sub-DAG
    (bookkeeping).
- **IMPORTED-AND-REVERIFIED: 2** (unchanged). Thm 27 was never a tally item. It is now replaced by a PROVEN-HERE
  theorem, so it no longer appears as an import anywhere.
- **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1), unchanged. L2's soft target is narrowed to (H1)
  + (H2) for BG-reg, and node N2 records it.
- **OPEN (main path): 23** (unchanged count). Two items changed in content:
  - **BG-reg** is narrowed to (H1) + (H2) for the soft minimiser, plus the written non-abelian bookkeeping;
  - **W1-loc** now depends on (DF) only ({N2, N4, N5, N6}); the Thm 27 import is gone.
- **Comparison branch: L1e-(0.4) (OPEN); W3 (wall in L5)**, unchanged.

**[S9] Tally (superseded by [S10] above).**
**[S9] Tally.** Three numbers, in order.
- **After the REVIEW_S7_S8 fixes (step 1): 43 / 2 / 7 / 24.** The added OPEN item is **BG-reg**. The reviewer
  confirmed R2D-iso, GT and R4D-iso, three of them with fixes, all applied as [R78-fix].
- **After decision 4: 43 / 2 / 7 / 23 on the main path, + 1 comparison-branch item.** L1e-(0.4) moves to the comparison
  branch. W3 is a wall inside L5, not a tally item; it moves to the comparison branch too.
- **After session 9's work: 46 / 2 / 7 / 23 (main path) + 1 comparison-branch item.**
  - **PROVEN-HERE: 46** (43 + 3 [S9], all unreviewed):
    - Lemma D4-norm (R4D-iso for the normalised soft kernel);
    - Lemma GT-lat with Proposition R4D-lat (the lattice Taylor lemma; discharges BG-reg (a));
    - Lemma W1-size' with Corollary W1-LD-cond (exact size reduction to the plugged holed sea; (LD) ⇐ (DF1-3')).
    - Not counted: BG-sum (arithmetic); Lemma AG (elementary, used inside a reduction); the 2D analogue of R4D-lat,
      the (cl) reduction and the ε_V linear-part cancellation (argued only).
  - **IMPORTED-AND-REVERIFIED: 2** (unchanged).
  - **IMPORTED-NOT-YET-REVERIFIED: 7** (L1d, L2, L3g, L4a, L5, L6, F1).
    - **[S9, decision 4]** L1d, L2, L3g, L4a, L5 and L6 are hard-constraint imports. The obligation is now their
      soft-kernel versions.
    - Dimock I Thm 27 is named as an import inside W1-loc, not as a separate tally item. Its tree-graph bound (323) is
      unproven in the text read.
  - **OPEN (main path): 23.** E8*, E8**, E7.0', E7.0'-TV, E7.0'-AF, the L3g(a)-slice completion (FP, NA, IT), L7b, L7c,
    L3g-ob, L8d, L9b, L9c, L9d, L10, F2, F3, F4, C1, C2, C3, C4, together with:
    - **W1-loc**, restated in 4D [S9] and reduced to (DF) + Thm 27;
    - **BG-reg**, narrowed to BG-b [S9].
  - **Comparison branch (listed, not counted as blocking): L1e-(0.4) (OPEN); W3 (wall in L5).**
  - Flagged for the next review to classify: Remark D4-obs (soft RG variables vs the S4'' observables).

**[S8] Tally (superseded by [S9] above): 43 / 2 / 7 / 23.** + Lemma GT, + Proposition R4D-iso (OPEN → PROVEN-HERE), + Lemma W1-sym (with W1-def and
W1-size, which are short exact identities/inequalities and are counted with it); OPEN: - R4D-iso, + W1-loc.
- **PROVEN-HERE: 43** (40 + 3 [S8]). The [S8] items and R2D-iso [S7] are unreviewed.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L5 unchanged: walls W1-loc, W2, W3).
- **OPEN: 23**: the session-7 list with R4D-iso removed and **W1-loc** added (W1-LD: P_rel(collar off a common direction
  by δ_0 = ε_1/(2√(4L+κ))) ≤ Ce^{-a/g²}; W1-cl: truncated correlations of ρ_□ with q ≤ 4 block averages
  ≤ C_qe^{-a/g²}(g²/κ)^qe^{-κ_d max|c_j|}; uniform in the torus).

**[S7] Tally (superseded by [S8] above).**
**[S7] Tally.** After the REVIEW_S5_S6 fixes (step 1): **39 / 2 / 7 / 22** (the added OPEN item is L1e-(0.4)). After
session 7's new work: **40 / 2 / 7 / 23**: + Proposition R2D-iso (PROVEN-HERE, isolated cube, d = 2; L5 [S7]); + R4D-iso
(OPEN, the 4D isolated-cube step, L5 [S7]). L5 itself stays IMPORTED-NOT-YET-REVERIFIED (walls W1-W3).
- **PROVEN-HERE: 40** (34 + 5 [S6] + 1 [S7]). REVIEW_S5_S6 confirmed all 39 earlier items (6 with fixes, applied as
  [R56-fix]); R2D-iso is new and unreviewed.
  - From sessions 1-3 (24, all confirmed by REVIEW_S3 as inequalities/identities): L0, L1a, L1b, L1c, L3s (weaker
    analogue), L4c, L7.0 (per K), L7a, L8a, L8b, L8c, L9a', L1e (smooth backgrounds only), R3.1 (promoted remark), L3s',
    L3g(a)-block (unused), L9a-m, S4' re-checks (now everywhere, with the odd branch rule [R3-fix]), L3g(a)-glob,
    L3g(a)-slice (the inequality on H_0; its use as a fluctuation gap is CONDITIONAL on (FP) [R3-fix]), E8.1, E8.2,
    E8.3 (inequality), S5' per-K tuning.
  - New in session 4 (6): Lemma E8*-sup; Proposition E8*-k (E8* at every fixed depth, uniform in K, M); Proposition
    E8*-ob (sharpness of the deterministic induction); Proposition E8*-red (coarse chessboard: every depth reduced to the
    homogeneous E8**); Lemma H0 (crossing-link structure); Lemma H1 (one step from Haar; w_0(1) bound for L ≥ 5, d = 4, SU(2) only [R4-fix]).
  - New in session 5 (4): Lemma E8**-dens (E8** ⇐ an effective-density bound (D_m)); inequality (B); Lemma A1 (abelian
    S4' averaging contracts the action, sharp constant L^{4-d}, = 1 in d = 4); Proposition A2 (E8** and E8* at every depth
    for the 4D Gaussian abelian model, ε = 4096 e^{-βη²/4}). (B) is elementary and is counted for bookkeeping only.
  - New in session 6 (5): L4a-Π (transverse structure of the polarisation tensor; β as the mixed second moment, a
    re-derivation of CMP 109 §5); Lemma B-avg (Balaban's (0.4) with diagonal order pairing = S4', conjugation identity,
    c17(B); elementary, counted for bookkeeping); Lemma A1-NA(1) (one-step non-abelian action bound with the sharp
    leading constant L^{4-d}, local form and large-field dichotomy; moved from OPEN); Corollary A1-NA(k) (k-uniform on
    the L1e domain, for S4' iterates [R56-fix]; on Balaban's (1.2) only conditionally on L1e-(0.4) and the √N
    conversion); Proposition LF-count (the unrenormalised large-field count diverges in d = 4 for every ε_1 below an
    explicit bound, ε_1 ≲ (8/(||Δ||β'_B))^{1/2} [R56-fix; inference, conditional on the one-loop rate]; the arithmetic
    only, its interpretation labelled).
  - New in session 7 (1): Proposition R2D-iso (2D O(N), one isolated cube, one step: the renormalised large-field
    weight is vacuum part + δβ·A_B + O(e^{-a/g²}s⁴); proven against the pre-stated RTARGET.md).
  - Soft or content-free alone: L7a, L8a-c, L7.0/S5' per-K.
- **IMPORTED-AND-REVERIFIED: 2.** L4b (b0) and L9a (Wilson RP, link and site reflections). The chessboard estimate is
  attributed to Fröhlich-Israel-Lieb-Simon, CMP 62 (1978) 1-34 [v-R4], but the special case used is re-derived, so it is not an import.
- **IMPORTED-NOT-YET-REVERIFIED: 7.** L1d, L2, L3g, L4a (its AF rate feeds the E8.3 corollary), L5, L6, F1. **[S5]** No
  status change: Dimock's abelian/scalar d = 3 analogues of L1d, L2, L3g, L4a, L6 were read and their transfer analysed
  (L6loc [S5] block); none of them re-verifies a 4D SU(N) statement, and the R-operation (L5) has no open exposition.
  Citation upgrades: L6's Dimock analogue [v-abs] → [read]. **[S6]** CMP 109 read in full (NOTES §9). Still no
  status change, for stated reasons: CMP 109 defers L4a-form's localisation to CMP 116 and L4a-flow (Theorem 2) to an
  unnamed later paper, and cites CMP 98/99/102 for L1d/L2/L3g without reproving them. Narrowings: L1d's
  background-regularity part is L1e on Balaban's domain (1.2); L4a's β-definition is split off as L4a-Π (PROVEN-HERE);
  L4a's "β_j → 2b_0 ln L" is corrected to CMP 109's two-sided (0.31) with unspecified β, β'.
- **OPEN: 23** (22 - A1-NA [S6] + L1e-(0.4) [R56-fix] + R4D-iso [S7]). **L1e-(0.4)**: L1e for Balaban's (0.4) with independent pairing (two-axial-path ribbon variant; needed by the A1-NA(k) (1.2)/minimiser readings and by decision 4). **R4D-iso**: the 4D SU(N) isolated-cube step (gauge-invariant Taylor lemma; soft constraint or fibre smoothness). **[S8] R4D-iso moved to PROVEN-HERE (soft constraint); fibre smoothness under Balaban's δ-constraint stays in W3.** Carried: E8* at depths k ≳ log β (fixed depths proven [S4]); E8** (constrained stability, sufficient for E8* at
  all depths; **[S5] reclassified: OPEN, import target = corollary of L5 + L6, not new content**; its sufficient form
  (D_m) is not counted separately); ~~A1-NA~~ (proven [S6] as A1-NA(1)); E7.0'; E7.0'-TV (new [S4], sufficient for E7.0'); E7.0'-AF (new [R3-fix]: AF compatibility of
  the S5'-tuned couplings); the L3g(a)-slice completion (FP, NA, IT); L7b (E7, E7.1-E7.4); L7c (conditional); L3g-ob
  (heuristic); L8d; L9b (E9.1, γ); L9c; L9d; L10; F2; F3; F4; C1; C2; C3; C4.
- **Retired as false [R3-fix: narrowed].** E8 with the domain D, for SU(2) and SU(3): unconditionally if g is a fixed
  bare coupling; conditional on L4a's AF rate if g is the tuned coupling. E7.0 restricted to the AF window, for
  SU(2), SU(3), SU(4) (threshold 3τ_N/4; SU(2) λ_c/λ_AF ≈ 6.1). N ≥ 5 (E7.0) and N ≥ 4 (E8 with D) are undecided. The
  session-3 "all N" statement concerned the stronger event "all steps within τ_N/2" and is withdrawn as a statement
  about E8.

**First open estimate: E8** (constrained stability) [S5: an import target, not a research target].** Z_K(every level-m 2-cell contains an η-large coarse plaquette) /
Z_K ≤ ε(g_m)^{n_c}, uniformly in K and M. By E8*-red it implies E8* at every depth. E8*-k proves E8* at depths
k ≲ log β / (2 log C_1), and E8*-ob shows that no induction through the fine-plaquette sup reaches deeper [R4-fix]. E8** is homogeneous and
translation invariant, of the same type as Balaban's UV stability bound. It is upstream of: the consistency of the limit
points; passing S5' through the limit; L7c; and E7.4. E7.0' is the second open estimate, independent of E8**: H1 does
the first step, and E7.0'-TV is a sufficient reduction.
**[S5]** E8** holds in the 4D Gaussian abelian model at every depth (A2), so the statement is natural and is NOT blocked
by the E8*-ob mechanism; for SU(N) it is the probability form of Balaban's per-level large-field bound plus stability
(the Dimock III Lemma 13 + Theorem 2 template), via E8**-dens. Further progress on it is reading Balaban CMP 122, not new
reductions.
**[S6]** CMP 109 is read, and confirms that E8** cannot come from it: it is small-field only. Proposition LF-count shows
that in d = 4 the per-level extraction (now proven at tree level, A1-NA(1)(c)) cannot be summed without renormalising
the large-field regions. So E8** waits on L5's renormalised large-field bound: CMP 122, or a reconstruction of a one-cube
R-operation.

## 4. Next session
**[S16] Order for session 17 (wind-down session 2 of 2; owner decision 2026-10-27: no new SU(N) obligations).**
1. **Review first: a hostile review of session 16**, scoped to load-bearing items: the [R15-fix] applications (fixes
   1-6); Lemma F-df_0 (the gauge-invariance step (0) on the strip, the divided-difference bound in (1), the telescoping in
   (2), the antisymmetry bookkeeping in (3)); c31 (criteria vs script vs output; the -I disclosure); LINEAR_PACKAGE.md
   against PROOF.md line by line (every statement, constant and pointer; every check outcome as pre-registered).
2. **Finish the linear package, cheap items only** (REVIEW_S15_CONVERGENCE (d) step 2): (LED-src) and the abelian
   multi-level per-level-slice gap, giving (G♯_0-fine) for level-0 sources and (G♯_0-field). If either does not fall in
   the session, it stays OPEN in LINEAR_PACKAGE.md §7; do not chase it. (G♯_0-fine-up) and Lemma G♯_0-plain stay deferred.
3. Update LINEAR_PACKAGE.md (fixes from item 1; any item 2 result) and freeze it.
4. Then (session 18, per the owner decision): the soft-vs-hard cost audit (REVIEW_S15_CONVERGENCE (d) step 3), then pause
   the lane until CMP 102, 116, 119, 122 I-II are available.

**[S15] Order for session 16.** (Session 16 did: item 1 was done by REVIEW_S15_CONVERGENCE and applied ([R15-fix]); item 5's
Lemma F-df_0; the write-up LINEAR_PACKAGE.md. Items 2-4 and the rest of item 5 are not pursued under the wind-down
decision, except as listed in the [S16] order.)
1. **Review first: a hostile review of session 15**, checking: the [R1314-fix] applications (all 13); Lemma SRC-all
   (the effective datum, the zero-mean step); Lemma REC (the bilinear identity with the top components); Lemma KF (the
   support and L-power bookkeeping, e^{8m'}); Theorem G♯_0-soft (the Σ_P count, the transport bound via CR (i)'s W for
   Q_root, the claim that G0-F1 is attained by coherent sources); Lemma LES-div (the energy step with h, the degree of
   the harmonic decay); the (G♯_0-fine) reduction (the n-cancellations, the roughness of transported coarse sources);
   Proposition NA-lev (which operator N4 uses; the defect counting 81, p_L; Lemma E-low's dual formula and constant);
   c30 (criteria vs script vs output; the pre-script C4 correction; no -I).
2. **(LED-src) and (G♯_0-fine-up)**: the curvature response to sources. Suggested: the symbol route of EXP-id/SRC-id for
   the source-to-f_0 map including K ≠ 0 aliases, with a finite-range split of the fine Δ^{-1} for the short-distance
   part; or a gauge-invariant weighted energy (Combes-Thomas-type) estimate from E-low and PG.
3. **(G♯_0-field)**: the abelian multi-level per-level-slice gap (PG at every level with the effective energies E_i, via
   E-low), then the Hölder field bound.
4. **(NA-H)** and the written per-block covariant perturbation at n = L; then Lemma G♯_0-plain and (R♯_ω).
5. Lemma F-df_0 (N6 interface); N5; N6 last; D4-obs (OPEN). Owner requests: CMP 122 I-II, CMP 116, CMP 102.

**[S14] Order for session 15.** (Session 15 did: item 1 was done by REVIEW_S13_S14 and applied; item 2 partly
((G♯)_0 soft half proven; fine half reduced); item 3 changed by the per-level finding (NA-lev). Item 4 is carried.)
1. **Review first: a hostile review of sessions 13 AND 14** (session 13 is still unreviewed; its list is the [S13] order
   below). For session 14 it should check:
   - Lemma NA-alg: the fixed-point constants (5.23, 0.53, 3.35, 9.2, 4.5y), the global-maximiser step, and (b)'s
     expansion (the √N factors, the θ-part);
   - Lemmas NA-crit, NA-inv and Proposition NA-FP: the left-trivialisation sign, the telescoping with backward links,
     the onto-ness of M_U, the dimension count, the composite-slice covariance;
   - Lemma SRC-id: the effective datum mod Closed, the K = 0 algebra, the adjoint normalisation used for f_0;
   - Lemma EXP-strip' (S1)-(S7) line by line and the η'_* arithmetic (c29 strip2_consts);
   - Propositions NA-IFT, B-NA-red: the constants, and whether BNA-F1-F3 are stated correctly (BNA-F2 is a scaling
     count, labelled argued);
   - c29 (A-D): criteria vs script vs output, and the C1 and other FAILs.
2. **(G♯), the linear core of B-NA and of the (NA) gap.** A multi-scale Schauder-type estimate for the gauge-fixed
   linearised chain on general sources. Suggested order:
   - the one-level case first (k = 1, n = L fixed): tree or covariant slice, Combes-Thomas from an explicit gap, sup
     bounds (n fixed, so no Schauder issue), giving an unconditional B-NA(1) with explicit constants;
   - then the fine-level Biot-Savart part of SRC-id in real space (a finite-range split of Δ^{-1}), for k-uniformity.
3. **(NA) gap**: route (R1) (enlarged covariant slice, covariant PG with Kato's inequality) or (R2) (smooth/rough split);
   and the locality/analyticity of the Faddeev-Popov constant FP_U(V).
4. **N5** (ℓ¹ bound, random-walk expansion). m_*: a point-dependent EXP-strip' or a second-order Z bound (optional).
   N6 last. D4-obs (OPEN). Owner requests: CMP 122 I-II, CMP 116, CMP 102.

**[S13] Order for session 14.** (Session 14 did: items 2 (reduced, not closed), 3 ((NA) identity; gap open) and 5 (m_*'). Items 1 (review of session 13) and 4 (N5) are carried.)
1. **Review first: a hostile review of session 13.** It should check:
   - the [R1112-fix] applications (all 11);
   - Lemma EXP-id: the K = 0 / K ≠ 0 split of P̂, the identity Δ = φδ, aΣ = φΨ, and the f_0 cancellation
     (ν_σ/D̄_σ = ν^{(n)}_σ and the 1/β_σ expansion);
   - Lemma EXP-real (R1)-(R6) and Lemma EXP-strip (P1)-(P7), line by line, and the η_* arithmetic (c28_exp.py consts);
   - Theorem N2-exp: the two-formula definition of g, periodicity at ∂Q, the f_0 K ≠ 0 majorant in the strip, the
     constant M, and the Paley-Wiener step;
   - Corollary N2-exp-b: the claim about what N6 consumes;
   - Lemma IT-line (the unrolled form and the slab counting) and Proposition PG^{(k)}'s arithmetic;
   - c28 (A-D): criteria vs script vs output; B's tie failure; C3/C4's window failure and the post-run fits.
2. **The SU(N) chain.** B-NA (i)-(iii) with constants, and the SU(N) analogues of N2-E, N2-lin and N2-exp. Route:
   contraction around the flat lift (N2-a (iii)), using the linear exponential kernels of Theorem N2-exp (the
   non-linear terms are local polynomials in the curvature, so exponential locality should propagate).
3. **(NA) for N4**: the covariant Weitzenböck version with curvature terms O(F), for the direct and composite slices.
4. **N5** (the soft Hessian covariance: ℓ¹ bound, random-walk expansion), now with the abelian gap for both slices.
5. A sharper m_* (optional): the located rate is ≈ 90 times the proven one; N6's block size M ≳ 457/m_* depends on it.
   N6 last. D4-obs (OPEN). Owner requests: CMP 122 I-II, CMP 116, CMP 102.

**[S12] Order for session 13.** (Session 13 did: the review fixes (the review was REVIEW_S11_S12); N2-exp (the
reviewer's strategic target, in place of item 2's order); item 3's (IT'). Items 2 (SU(N)), 3's (NA) and 4 are carried.)
1. **Review first: a hostile review of sessions 11 AND 12** (session 11 is still unreviewed). For session 12 it should
   check:
   - fix 13 (the quotes, and the label);
   - Lemma IT-str (the tiling and weights), and its use on co-closed transposes;
   - Lemma LED-dual: the mod-Closed bookkeeping of Q_root composites, the zero-mean step, the energy identity;
   - Lemma LED-symb: the decimation normalisations, the Lagrange formula, and the f_0 Bloch formula with phases;
   - Lemma WA (the dyadic argument and the periodisation);
   - Proposition LED-unif: the alias-sum bounds uniform in n, the u/v quotient estimate, and step (4)'s reduction
     to Π_ex + Π_coex = I with the sign conventions;
   - Theorem N2-lin's constants;
   - Proposition PG: the face-flux identity, the column Cauchy-Schwarz, the orbit identity, PG-ext's constants
     (C_I = 22, C_δ = 216, C_β = 163, C_γ = 20), PG-line's C_3 ≤ 14, and the final arithmetic;
   - c26 (A, B, C; the addendum and Q7's FAIL) and c27 (E3's FAIL): criteria vs script vs output.
   For session 11: the list in the [S11] order below.
2. **The SU(N) chain.** B-NA (i)-(iii) with constants, and the SU(N) analogues of N2-E and N2-lin. Route: contraction
   around the flat lift (N2-a (iii)), using the linear ℓ¹ kernels of Theorem N2-lin.
3. **(IT') and (NA) for N4.** (IT'): the physical gap for the slice of the composite root map. (NA): the covariant
   Weitzenböck version with curvature terms O(F).
4. **N5** (ℓ¹ covariance, random-walk expansion). Also N10's question: whether the response kernels admit an
   exponentially decaying representative on exact data. The kernels proven here have power-tail BOUNDS [R1112-fix:
   was "have power tails"].
5. N6 last (κ > 3κ_0 + 3 ≈ 457). D4-obs (OPEN). Owner requests: CMP 122 I-II, CMP 116, CMP 102. (Decision 4's
   delegation is now quoted; that request is closed.)

**[S11] Order for session 12.** (Session 12 did: fix 13; item 2 ((LED), in full for the linearised chain); item 3 (the
physical gap). Item 1, the review of session 11, was not done and is carried; item 4 (B-NA) was not attempted.)
1. **Review first: a hostile review of session 11.** It should check:
   - the [R910-fix] applications (all 13);
   - Lemma CE-geo': the segment-by-segment lift on the torus, the Cavalieri step, the projection volume 2^{d-1}|u|_1,
     and the re-derived Theorem CE constants (κ_0 = 16a, K_0 = e^{κ_0}/6400, C_K = 32eK_0);
   - Lemma N2-a (SU(N)): the flat-to-constant gauge equivalence on the lattice torus, and the zero-energy lift;
   - Lemma N2-E: the Whitney properties (W1)-(W4), the use of CR (ii) with F at a point of Ω_c, the counting
     constants, and the claim that no factor of k appears;
   - Proposition N2-red and Lemma LES-sup (the Campanato telescoping without a sup hypothesis);
   - Lemma FP-ab and its application: admissibility of (h, P_resd*), the weight W of the double fixing, the
     O_FP ⟺ physical-gap reduction (the Poincaré constant 4);
   - checks c21 (the reporting edit and I4), c23 (Part A Q3 FAIL, Part B), c24, c25: criteria vs script vs output.
2. **(LED)** for the linearised soft chain, uniformly in k. Candidate routes:
   - (a) the centring cancellation of [Q, χ] on gauge-fixed fields that are smooth on the level-(i+1) scale;
   - (b) a k-uniform multiscale Poincaré inequality in a smooth gauge;
   - (c) the chain is translation invariant on each level, so use the Fourier symbol of the response dB_k ↦ (r_i, dB_0)
     and its analyticity in a strip, uniformly in k (Paley-Wiener; the cleanest for the linear chain).
   A d = 4, k = 2 decay diagnostic, if memory allows.
3. **The physical gap on Phys (N4):** ||dA||² + κ||QA||² ≥ c||A||² on {h = 0, d*A ∈ span(δ_{c_X}, 1_{B(X)})},
   uniformly in n and T.
4. **B-NA (i)-(iii) with constants**, and the SU(N) analogue of N2-E around flat backgrounds (c23 Part B supports it).
5. N5 after (LED) and the physical gap; N6 last (it must deliver κ > 3κ_0 + 3 ≈ 457).
6. D4-obs (OPEN). Owner requests unchanged: CMP 122 I-II, CMP 116, CMP 102, and decision 4's delegation in the
   owner's own words.

**[S10] Order for session 11.** (Session 11 did: the REVIEW_S9_S10 fixes (the review itself was done separately, as
REVIEW_S9_S10.md); item 2 as N2's linear half, narrowed to (LED); item 4's N4 abelian part; and the optional κ_0
sharpening.)
1. **Review first: a hostile review of sessions 9 AND 10** (session 9 was never reviewed). For session 10 it should
   check:
   - Theorem CE: the constants chain (g1)-(g5), the step-1 condition on H_0, the step-4 tree sum (root factor, Cayley
     count), the analytic-identity step;
   - Lemma TG (the Penrose (⇐) direction);
   - Proposition CE-κ (the t⁶ coefficient; whether d(pair) = 0 is the right reading of Dimock's (119));
   - Lemma LES (Caccioppoli and the discrete Sobolev constants, the iteration lemma on integer radii);
   - Lemma J-str (the EL/divergence induction, and the claim that the normalised kernel's tree-level exponent
     linearises to Setting SC);
   - Proposition BG-b-lin (the data-region/ribbon containment, the composite-average density bound, the use of LES on
     the periodic extension);
   - c21 and c22: criteria vs script vs output (including c22's Q3 FAIL).
   For session 9: the session-9 list in the [S9] order below.
2. **N2 (soft L2): (H1) + (H2).** Sup bounds for the soft chain minimiser from coarse curvature ≤ ε_0. Route:
   - exponential decay of the linear soft background map (composite form with the coarse metric Γ^{-1}; Combes-Thomas);
   - then the non-abelian case by contraction around it;
   - c22-type diagnostics with stronger κ and two levels if memory allows.
3. **B-NA (i)-(iii) with constants**, which turns Proposition BG-b-lin into the SU(N) statement.
4. **N4 (FP) and N5** (soft covariance: the gap with (NA) and (IT), ℓ¹/ℓ² bounds, random-walk expansion).
5. Remark D4-obs; owner request unchanged (CMP 122 I-II, CMP 116, CMP 102).

**[S9] Order for session 10.** (Session 10 did items 2, 3 (via Theorem CE) and part of 4 (the (DF) sub-DAG), as
targets A-C set by the session lead. Item 1, the review, was not done; it is carried as item 1 of the [S10] order.)
1. **Review first.** A hostile review of session 9. It should check:
   - the [R78-fix] applications;
   - Lemma D4-norm (the 𝒩 lower bound, and the cumulant derivative bound);
   - Lemma GT-lat: the tree-gauge Stokes step with its C(R_0) constants; the exact lattice equivariance of 𝓛; whether
     ε_V should be split into its linear part and the rest;
   - R4D-lat;
   - Lemma W1-size' (the w_ref choice; the plaquette bound at the maximiser of w);
   - Corollary W1-LD-cond (the Chernoff constants);
   - the c19b criteria vs script vs output (Q3's FAIL, and the post-run diagnostic);
   - the c20 criteria vs script vs output (the chain model, the κ_i scaling, the controls' power);
   - whether "BG-b = U_k(ε_0)-membership + elliptic step + soft residual" is a faithful reading of CMP 109 (1.2).
2. **BG-b for the soft S4' minimiser.**
   - (a) The lattice elliptic step (osc ≤ Cr(1 + log 1/r)(sup|F| + sup|J|)) in the abelian case, written.
   - (b) The Euler-Lagrange structure of the soft chain minimiser (J_soft along the S4' contours).
   - (c) A c20-type diagnostic for the non-abelian SU(2) minimiser in d = 3 or 4 (small, one job). It should also
     measure ε_V.
3. **(DF3') with interaction.** Write the tilt argument from Thm 27, and decide whether to re-prove the tree-graph bound
   (323) (Penrose / Brydges-Kennedy), which would upgrade Thm 27 to IMPORTED-AND-REVERIFIED.
4. **The small-field package for the soft kernel (DF1, DF2, DF4).** This is the main-path wall. Start with the soft
   analogue of L2's background (existence, uniqueness, decay) at tree level.
5. Remark D4-obs: compare the soft-RG block laws with S4''(U).
6. Owner request unchanged: CMP 122 I-II (decisive for L5), CMP 116, CMP 102 (now for comparison with the soft
   version).

**[S8] Order for session 9.** (Done in session 9: review fixes as [R78-fix]; decision 4; BG-reg; W1-loc in 4D.)
1. **Review first.** A hostile review of sessions 7-8: R2D-iso; RTARGET §5-6 vs Lemma GT, R4D-iso and the W1 lemmas
   (were the targets met as pre-stated? the radial-gauge step 1, the B_4 irreducibility argument, the R4D-iso size step
   with the data-region constant C_L, W1-size's rearrangement); c19 criteria vs script vs output.
2. **W1-loc, size half first (W1-LD).** A local stability estimate for the pinned sea that does not go through
   frozen-exterior cap bounds (those amplify by M ≫ 1): e.g. a global Gaussian-domination / convexity bound in a chart
   around the background (the Hessian is ≥ c/g² by the block Poincaré inequality, L3 step 2, up to O(ε_1) corrections),
   with Brascamp-Lieb or Helffer-Sjöstrand for the deviation tails, then Helffer-Sjöstrand + Combes-Thomas for W1-cl.
   Imports allowed, re-verified on the pinned O(N) sea.
3. **W2**, against RTARGET §7 as pre-stated.
4. **L1e-(0.4)** (easy), and the R4D-iso cut: Balaban's gauge-fixed B' cut vs our gauge-invariant plaquette cut.
5. Owner request unchanged: CMP 122 I-II (decisive for L5), CMP 116.

**[S7] Order for session 8.**
1. **Review first.** A hostile review of session 7: the [R56-fix] applications; c18c (criteria file vs script vs
   output); RTARGET.md vs Proposition R2D-iso (was the target met as pre-stated? steps 2, 5, 7 in particular); the CMP
   198 reclassification; the 4D transfer claims in R4D-iso.
2. **R4D-iso.** Write the gauge-invariant Taylor lemma (order s² vanishes; order s⁴ = c·Σ tr F²; odd orders vanish)
   for smooth gauge-invariant functions of the links of a cube with frozen exterior, then the 4D isolated-cube bound
   with a soft constraint and a plaquette cut.
3. **W1 in d = 2 first.** Unfreeze the exterior: a one-step polymer expansion of the small-field sea with one
   large-field defect, giving ρ_full(□) as local terms with the R2D-iso s-derivative bounds. A failure with the exact
   step named is a valid outcome.
4. **L1e-(0.4)** (easy): the two-axial-path ribbon variant.
5. **Owner request, unchanged:** CMP 122:175-202 and 355-392 (L5: decisive, and it should show how Balaban handles
   W1-W3); CMP 116:1-22; the Theorem 2 paper; CMP 102/98/99. CMP 198 is NOT a 2D template (low-temperature d ≥ 3), so
   it is dropped from the request unless the owner wants the R-operation's structure in a simpler model anyway.
6. Decision 4 (adopt (0.4) vs keep S4') and the carried items E7.0'-TV, E7.0'-AF, (FP). **[S9] Decision 4 made: keep S4' with the soft kernel (L5 [S9]).**

**[S6] Order for session 7** (done in session 7: review applied as [R56-fix]; one-cube target in RTARGET.md; R2D-iso).
1. **Review first.** No hostile review of session 5 or session 6 exists. A REVIEW_S6 should check L4a-Π, A1-NA(1) and
   A1-NA(k) (constants, the axial-gauge locality step, and the Schur restriction to R), LF-count's hypotheses, and the
   NOTES §9 transcriptions against the page images.
2. **One-cube R-operation (reconstruction target named by LF-count).** For a single level-k M-cube in which the
   fluctuation cut |B'| < ε_1 fails, inside a small-field sea, construct the renormalised contribution: subtract the
   vacuum-energy and β_k·A counterterms computed from the small-field flow, and bound the remainder by
   O((L^kε)^{4+α})·(weight), using A1-NA(1)(c) for the action and L4a-Π for the marginal part. A failure with the exact
   wall named is a valid outcome.
3. **Owner request, unchanged, narrowed by CMP 109's deferrals:** CMP 122:175-202 and 355-392 (L5, decisive);
   CMP 116:1-22 (L4a-form's localisation, "II. Cluster expansions"); the paper with Theorem 2's proof (CMP 119:243-285 is
   the likely candidate, [not-read]); then CMP 102:277-309, 98:17-51, 99:75-102 and 99:389-434.
4. **Decision for the owner, not taken here:** adopt Balaban's (0.4) verbatim in place of S4', so that CMP 109's "all
   results of [12] are valid" applies, or keep S4' and prove the CMP 98 results for it. The re-checks needed for (0.4)
   are listed in L1d [S6].
5. Carried: E7.0'-TV, E7.0'-AF, (FP).

**[S5] Binding order (REVIEW_S4 strategy): obtain and read before any new reduction.**
1. **Owner action: Balaban PDFs.** Ask the owner to place in `literature/` (open sources do not contain them):
   - CMP 122 (1989) 175-202 and 355-392: Large field renormalization I, II. This is L5, and it decides E8**.
   - CMP 109 (1987) 249-301, CMP 116 (1988) 1-22 and CMP 119 (1988) 243-285. These are L4a and L6.
   - CMP 102 (1985) 277-309 (L2, and A1-NA's likely counterpart) and CMP 98 (1985) 17-51 (whether his averaging equals
     S4').
   - Then CMP 95 (1984) 17-40, CMP 96 (1984) 223-250, CMP 99 (1985) 75-102 and 389-434 (L3g, L1d).
   - Optionally CMP 102 (1985) 255-275 (the 3D pure-gauge template) and Imbrie's Les Houches 1984 lectures.
2. **On receipt:** a line-level comparison of E8** / (D_m) against the CMP 122 large-field bound, in the
   NOTES.md format.
3. **Until then (low cost, no new reductions):**
   - A1-NA: a numerical diagnostic of the non-abelian action ratio on small-field SU(2) configurations.
   - The compact (Villain) U(1) version of A2.
4. E7.0'-TV, E7.0'-AF and (FP) are carried, with lower priority.

**Carried from session 4 (superseded order):**
1. ~~E8** abelian analogue~~ done as A2 [S5]. The SU(N) two-scale version waits for item 1 above.
2. **E7.0'-TV.** Bound the TV distance between Haar and the conditional crossing-link law Φ#Haar at β = 0, at level
   K - 1 first. This needs a Jacobian bound of S ↦ S e^{X̄(S)} away from the branch set.
3. **E7.0'-AF.** Test numerically whether S5'-tuned β_K grow at the AF rate (small K, d = 4, L = 3), as a diagnostic.
4. **(FP) and the SU(N) slice.** The abelian Faddeev-Popov identity for δ(h) plus the residual group; then decide whether
   the slice operator should be d*d + aQ^†Q rather than Δ.
5. ~~E7.2 norm~~ dropped [R4-fix] (REVIEW_S4 (2)).

---

**[S17] Pointer: the 4D large-field R-operation (node B-W2) — see RLARGE.md (session 17; targets pre-stated there in
§0-§2 at 20:58 UTC before any derivation; c32 criteria before the script).** PROOF.md is otherwise unchanged this session.
- Theorem RLF (the target the R-operation must deliver, soft kernel, all quantifiers; composes with LF-count, R4D-iso,
  Theorem CE) is stated (RLARGE §1) and stays OPEN inside L5 (L5 itself unchanged: IMPORTED-NOT-YET-REVERIFIED).
- PROVEN-HERE [S17], unreviewed: **Lemma GT-lat'** (lattice Taylor lemma without point symmetry, general coarse links,
  B_4 orbit averages); **Proposition CL** (exact Fubini identity Z_B/Z_∅ = ⟨Π r_{Y_i}⟩_cut, factorisation over
  *-components, per-cube-uniform frozen size bound r_Y ≤ (C_rg^{-p_r}e^{-ε_1²/(4Ng²)})^{|Y|}); **Theorem TS** (with Theorem
  R1: the frozen one-level R-operation — the large-field gas is a hard-core polymer gas exponentiated by Theorem CE steps
  3-4; clusters of total size N ≤ n_* := ⌊4/(a''β_-)⌋ give field-independent vacuum constants and ONE uniform coupling
  shift δβ_j; the remainders are of irrelevant order and sum over inner levels uniformly under BG-b at the last
  small-field level, whatever the level-k field) **[R1617-fix R-6: read "the remainders are of order 𝔯(D); this is
  irrelevant, and they sum over inner levels uniformly, for BG-b-regular FROZEN data at the last small-field level; in a
  sea sample 𝔯 = O(g²) and the remainders are re-extracted after the sea average (RLARGE §7.2 Reading, §8.2 (W1-ret')).
  R-3b: R1 (iii)'s B_4 step as written in session 17 was false; repaired in session 18 (RLARGE §7.2 (iii))]**; **Lemma RS** (one-step re-seeding of a coarse large field: ribbon
  constant (d-1)L(L-1)/2, square L²; the kernel branch is priced unconditionally by the normalised soft kernel).
- CONDITIONAL: Proposition RLF-step ((I_k) ⇒ (I_{k+1}) modulo (SF), (PLD), (W1-ret), (HIST), (F)); the level summations are
  proven. c32 A-D PASS.
- **Tally (after session 17): 68 / 2 / 7 / 24 (main path) + 1 comparison-branch** (+GT-lat', +CL, +TS, +RS; no top-level
  OPEN item discharged; B-W2's content is now the walls listed in RLARGE §11). **[R1617-fix: REVIEW_S16_S17 corrected
  this to 67 (TS/R1 at GAP); session 18 restores 68 by the repair; see the [S18] tally in §3.]**

---

**[S18] N5 at the trivial background (node N5 of the (DF) sub-DAG, L5 [S10]; target pre-stated in RTARGET.md §40 at
22:11 UTC, before this text).** Everything here is at the trivial background, linearised (one real colour component),
in level-i own units with unit-weight ℓ² norms on links; g = 1 (the covariance scales by g²).

- **Setting N5-0.** Levels i ≥ 0 of Setting SC with κ_- ≤ κ_j ≤ κ_+; coarse torus T ≥ 2 (so every level-i torus has side
  ≥ 2L). The level-i fluctuation form is ½⟨A, O_i^{gi}A⟩ := E_i(A) + (κ_i/2)||QA||², with E_i(A) = ½⟨A, H_iA⟩ the effective
  chain energy with top level i (H_0 := d*d). The gauge fixing is FP-ab's δ(h)e^{-½||P_resd*A||²} at n = L (h the slice
  functional of the step i → i+1; Λ_res := {λ : λ(c_X) = 0, Σ_{B(X)}λ = 0 ∀X}, P_res its orthogonal projector). So the
  Gaussian fluctuation measure is δ(h(A))e^{-½⟨A, O_iA⟩}dA with **O_i := H_i + κ_iQ^TQ + dP_resd***, and its covariance is
  **C_i := Π(ΠO_iΠ|_{ker h})^{-1}Π**, Π the orthogonal projector onto H_0 = ker h; **𝒞_i := C_i^{1/2}** is N5's 𝒞.
  Positions: a link sits at its base point; d := the ℓ¹ torus distance of positions. For a nonnegative kernel K put
  N_m(K) := sup_xΣ_yK(x, y)e^{md(x,y)} and D_m(K) := sup_xΣ_yK(x, y)(e^{md(x,y)} - 1). N_m is submultiplicative, and for
  K_1K_2K_3 (entrywise products of absolute values) D_m(K_1K_2K_3) ≤ D_m(K_1)N_m(K_2)N_m(K_3) + N_0(K_1)D_m(K_2)N_m(K_3) +
  N_0(K_1)N_0(K_2)D_m(K_3) (from e^{m(a+b+c)} - 1 ≤ (e^{ma} - 1)e^{m(b+c)} + (e^{mb} - 1)e^{mc} + (e^{mc} - 1)).

- **Lemma CT (Combes-Thomas, explicit): PROVEN-HERE [S18].** Let 𝒢 be finite with a pseudometric d, and K a real
  symmetric matrix on ℓ²(𝒢) with K ≥ γ > 0. If D_m(|K|) ≤ γ/2, then for every t ≥ 0 and x, y:
  |(K + t)^{-1}(x, y)| ≤ (2/(γ + t))e^{-md(x,y)}, and |K^{-1/2}(x, y)| ≤ (2/√γ)e^{-md(x,y)}.
  *Proof.* Fix y_0, f := d(·, y_0), E := e^{mf} (diagonal). E(K + t)E^{-1} - (K + t) has kernel K(x, y)(e^{m(f(x)-f(y))} - 1),
  of absolute value ≤ |K(x, y)|(e^{md(x,y)} - 1); by the Schur test (|K| symmetric) its norm is ≤ D_m(|K|) ≤ γ/2 ≤ (γ + t)/2.
  Since ||(K + t)^{-1}|| ≤ 1/(γ + t), E(K + t)E^{-1} = (K + t)(1 + (K + t)^{-1}[E(K + t)E^{-1} - (K + t)]) is invertible with
  inverse norm ≤ 2/(γ + t), and its inverse is E(K + t)^{-1}E^{-1}. Taking the (x, y_0) entry: |(K + t)^{-1}(x, y_0)|e^{mf(x)}
  ≤ 2/(γ + t). For the square root, K^{-1/2} = π^{-1}∫_0^∞t^{-1/2}(K + t)^{-1}dt and ∫_0^∞t^{-1/2}(γ + t)^{-1}dt = π/√γ. ∎

- **Lemma N5-sl (the slice projector is block-local; inf-sup): PROVEN-HERE [S18].** h(A)(X) = ⟨w_X, A⟩, w_X supported on
  the links with both ends in B(X) (a complete-axial path from c_X to y ∈ B(X) stays in the box spanned by c_X and y), and
  w_X is the translate of one vector w. Hence hh^T = ||w||²·1, **Π = 1 - h^Th/||w||²** has range ≤ 4(L - 1) (inside one
  block), and
  ||w|| ≥ (L - 1)/(8L), Σ_b|w(b)| ≤ 2(L - 1), max_b|w(b)| ≤ 1.
  *Proof.* Blocks are disjoint, so hh^T is diagonal. Let b_0 := (c_X, c_X + e_1). Every pair (σ, y) with σ(1) = 1 (6 of the
  24 orders) and y_1 > (c_X)_1 ((L - 1)/2·L³ sites) uses b_0 forwards, and no path from c_X uses b_0 backwards; so
  w(b_0) ≥ 6·((L - 1)/2)L³/(24L⁴) = (L - 1)/(8L). The path length is |y - c_X|_1 ≤ 2(L - 1), which bounds Σ_b|w(b)|; a path
  uses a link at most once, so |w(b)| ≤ 1. ∎ Consequently N_0(|Π|) ≤ n_Π := 1 + 2(L - 1)/||w||² ≤ 1 + 128L²/(L - 1) and
  D_m(|Π|) ≤ (e^{4m(L-1)} - 1)(n_Π - 1).

- **Lemma N5-coer (coercivity on the slice; failure mode N5-F1 does not occur): PROVEN-HERE [S18].** For every i, k, T:
  **O_i ≥ γ_i on H_0, γ_i := ½min{2c_1L^{-2}min(c_E^-, κ_-/2), ν_N}**, where c_1 = 1/(3.5·10⁶) and c_E^- := min_{κ∈[κ_-,κ_+]}c_E
  (Proposition NA-lev (c) / Lemma E-low), and ν_N := 2(1 - cos(π/L)) (= 1 at L = 3), the Neumann gap of the block.
  *Proof.* Let A ∈ H_0. (1) *Decomposition.* T := P_resΔ_0 restricted to Λ_res is symmetric and ⟨λ, Tλ⟩ = ||dλ||²; for
  λ ∈ Λ_res (zero mean on each block), ||dλ||² ≥ Σ_X||dλ||²_{inside B(X)} ≥ ν_N||λ||², so T ≥ ν_N and is invertible. Let
  λ := T^{-1}P_resd*A and A_P := A - dλ. Then h(dλ)(X) = avg_y λ(y) - λ(c_X) = 0, so h(A_P) = 0, and P_resd*A_P = 0, i.e.
  d*A_P ∈ span(δ_{c_X}, 1_{B(X)}) = Λ_res^⊥: A_P ∈ Phys. (2) *Gauge-invariant part.* E_i is invariant under A ↦ A + dλ, and
  Q(dλ) = d(ev λ) = 0 since λ(c_X) = 0; so ⟨A, O_i^{gi}A⟩ = ⟨A_P, O_i^{gi}A_P⟩ ≥ 2min(c_E, κ_i/2)c_1L^{-2}||A_P||² by NA-lev (c)
  (stated there in PG's normalisation ||A||²_B = L^{-2}Σ_ba_b²). (3) *Fixing part.* P_resd*A = P_resd*A_P + Tλ = Tλ, and
  ||Tλ||² ≥ ν_N⟨λ, Tλ⟩ = ν_N||dλ||² (T ≥ ν_N on Λ_res). (4) ⟨A, O_iA⟩ ≥ c'||A_P||² + ν_N||dλ||² ≥ ½min(c', ν_N)||A||²
  (||A||² ≤ 2||A_P||² + 2||dλ||²). ∎
  **[R1819-fix 9, optional sharpening, applied] γ_i doubles: O_i ≥ γ_i^♯ := 2γ_i = min{2c_1L^{-2}min(c_E^-, κ_-/2), ν_N} on H_0.**
  In step (4), A_P ⊥ dλ: ⟨A_P, dλ⟩ = ⟨d*A_P, λ⟩ = 0, since d*A_P ∈ Λ_res^⊥ (step (1)) and λ ∈ Λ_res; so ||A||² = ||A_P||² + ||dλ||²
  and ⟨A, O_iA⟩ ≥ min(c', ν_N)||A||². This matches PG's "O_FP ≥ min(c_PG, 4) on H_0" with no ½. Every later number in
  [S18]-[S19] that uses γ_i (γ_0 = 1.587·10⁻⁸, γ_i = 1.29·10⁻¹⁰ at κ ≡ 1, L = 3) remains valid as written (a smaller lower
  bound); where session 20 uses the sharpened value it writes γ^♯.

- **Lemma N5-loc (exponential locality of O_i; failure mode N5-F2 does not occur): PROVEN-HERE [S18].** Fix m' < m_*' and
  let M be Theorem N2-exp''s constant for the map B ↦ r (explicit from its displayed bounds). With p_L = 5L - 4:
  N_0(|O_i|) ≤ S_O := max{4κ_+M coth⁴(m'/2), 24} + 16κ_+p_L + 32, and for 0 < m < m'
  D_m(|O_i|) ≤ E_O(m) := max{4κ_+M[coth⁴((m' - m)/2) - coth⁴(m'/2)], 24(e^{2m} - 1)} + (e^{mp_L} - 1)(16κ_+p_L + 32),
  uniformly in i, k, T.
  *Proof.* (H_i) For i ≥ 1, LED-dual gives E_i = (κ_{i-1}/2)⟨r, Pr⟩ with r = r_{i-1}(B) the minimiser of ½⟨s, Ps⟩ + ⟨s, B⟩
  over co-closed zero-mean s; stationarity tested at s = r gives ⟨r, Pr⟩ = -⟨r, B⟩, so E_i(B) = -(κ_{i-1}/2)⟨𝓡_iB, B⟩ with
  𝓡_i the linear map B ↦ r_{i-1}, and H_i = -κ_{i-1}(𝓡_i + 𝓡_i^T)/2; by Theorem N2-exp' (ii) (k → i) its infinite-lattice entries are ≤ Me^{-m'|X|_1}, and with 4 link directions
  per position and Σ_{z∈Z⁴}e^{-a|z|_1} = coth⁴(a/2) the weighted row sums are as stated; the torus kernel is the
  periodisation, whose weighted row sums in the torus metric are no larger **[R1819-fix 9: N2-exp (ii) writes the torus
  bound with its own constant M' (PROOF l.2784); "no larger" holds for the periodisation, so for the torus read M := the
  larger of M and M' (the statement and every later use are unchanged with that reading)]**. For i = 0, H_0 = d*d: range 2, row sums ≤ 24
  (6 plaquettes per link, 4 links per plaquette). (κ_iQ^TQ) A fine link lies in contours of ≤ 8 coarse links, at most twice
  per contour (RLARGE §5 (d), CL-1), so Σ_c|Q(c, b)| ≤ 16; Σ_b|Q(c, b)| ≤ p_L (contour length); so N_0(|Q^TQ|) ≤ 16p_L, with
  range ≤ p_L (the ℓ¹ diameter of two adjacent blocks). (dP_resd*) Row sums: d (links → sites) 2, P_res ≤ 2 (it is 1 minus the
  projector onto span(δ_c, 1_B), whose rows have absolute sum ≤ 1), d* (sites → links) 8: ≤ 32; range ≤ 4L - 2 ≤ p_L. ∎

- **Theorem N5-triv (the gauge-fixed soft fluctuation covariance at the trivial background is exponentially local, with
  ℓ² and ℓ¹ bounds): PROVEN-HERE [S18], unreviewed.** Put Õ_i := ΠO_iΠ + (1 - Π). Let m_cov be the largest m ∈ (0, m') with
  𝔇(m) ≤ γ_i/2, where, with δ_Π(m) := (e^{4m(L-1)} - 1)(n_Π - 1) and p_m := n_Π + δ_Π(m),
    𝔇(m) := δ_Π(m)[1 + (S_O + E_O(m))p_m + n_ΠS_O] + n_ΠE_O(m)p_m
  (the product rule above with Lemmas N5-sl, N5-loc); 𝔇 is continuous with 𝔇(0) = 0, so m_cov > 0,
  and m_cov depends only on (L, κ_±, c_E^-, M, m'). Then, uniformly in i ≥ 0, k ≥ 1 and T ≥ 2, for all links b, b':
  - (i) |C_i(b, b')| ≤ (2/γ_i + e^{4m_cov(L-1)}/||w||²)e^{-m_cov d(b,b')};
  - (ii) |𝒞_i(b, b')| ≤ (2/√γ_i + e^{4m_cov(L-1)}/||w||²)e^{-m_cov d(b,b')};
  - (iii) (N5's ℓ² bound) Σ_{b'}𝒞_i(b, b')² = C_i(b, b) ≤ 1/γ_i; (N5's ℓ¹ bound) for 0 ≤ m'' < m_cov,
    Σ_{b'}|𝒞_i(b, b')|e^{m''d(b,b')} ≤ 4coth⁴((m_cov - m'')/2)(2/√γ_i + e^{4m_cov(L-1)}/||w||²).
  *Proof.* Π commutes with Õ and Õ = ΠO_iΠ ⊕ 1 on ker h ⊕ (ker h)^⊥; by Lemma N5-coer, Õ ≥ min(γ_i, 1) = γ_i. So
  Õ^{-1} = C_i + (1 - Π) and Õ^{-1/2} = 𝒞_i + (1 - Π). Õ is symmetric, and |Õ| ≤ |Π||O_i||Π| + |1 - Π| entrywise, and D_m(|Π||O_i||Π|) +
  D_m(|1 - Π|) ≤ 𝔇(m) by the product rule with N_m(|Π|) ≤ p_m, D_m(|Π|), D_m(|1 - Π|) ≤ δ_Π(m) (Lemma N5-sl) and
  N_m(|O_i|) ≤ S_O + E_O(m) (Lemma N5-loc). Lemma CT at m = m_cov bounds Õ^{-1} and Õ^{-1/2}; |(1 - Π)(b, b')| =
  |w(b)w(b')|/||w||² ≤ 1/||w||², supported on d ≤ 4(L - 1), which gives the second terms. (iii): 𝒞_i is symmetric with
  𝒞_i² = C_i, and C_i(b, b) ≤ ||C_i|| ≤ 1/γ_i; the ℓ¹ sum from (ii), 4 directions per position and coth⁴. ∎
  *What it is and is not.* This is N5's gap + ℓ² + ℓ¹ content at the trivial background, for the per-level operator with
  the full effective energy E_i (not only d*d), uniform in i, k, T, with every constant traced to proven ledger items
  (NA-lev (c), Lemma E-low, Proposition PG, N2-exp', LED-dual, FP-ab). It is NOT: N5 at a general small-field background
  (the background-dependent, non-abelian Hessian; (NA-H) ⊂ B-NA, OPEN); the random-walk expansion with complex
  s-weakening that N10 needs (OPEN; Combes-Thomas gives decay, not analytic background dependence); sharp (γ_i ≈ 1.3·10⁻¹⁰
  at κ ≡ 1, L = 3, so m_cov is tiny). The displayed 𝔇 is a crude explicit bound; any bound obtained from the product
  rule serves.
- **Check c34** (criteria first; checks/c34_*): A PASS (||w|| = 0.378 ≥ 1/12, ||w||² = 0.143, Σ|w| = 2.67, max|w| = 10/81,
  support inside the block); B PASS (Neumann gap of {0,1,2}⁴ = 1; λ_min(P_resΔ_0|Λ_res) = 1 on (Z/6)⁴; h(dλ) = 0 to 6e-16 on
  Λ_res); C PASS (Lemma CT's bounds on 24/24 random instances, ratios ≤ 0.48). The full O_i is not instantiated.
- **N5 node status [S18].** OPEN; its trivial-background abelian case is PROVEN (Theorem N5-triv). Still needed: the (NA)
  gap at small-field backgrounds (via (NA-H)), the background-dependent ℓ¹ bound (a perturbation of N5-triv once (NA-H)
  holds), and the random-walk expansion with complex weakening.

---

**[S19] N5 at small-field backgrounds; the random-walk expansion; level-0 constants (node N5 of the (DF) sub-DAG; targets
pre-stated in RTARGET.md §42 at 22:30 UTC, before this text; c35 criteria before the c35 script).** Notation of Setting
N5-0 and Theorem N5-triv. New: block-valued kernels. Fields A ∈ ℋ := ⊕_b su(N) (real, HS inner product), complexified
ℋ_C := ⊕_b su(N)⊗C; for an operator K on ℋ_C, |K|(b, b') := ||K(b, b')||_op (the su(N)⊗C block), and N_m, D_m of |K| as in
Setting N5-0. M_m(K) := sup_{b,b'}|K|(b, b')e^{md(b,b')}. For kernels, |(AB)(x, y)|e^{md(x,y)} ≤ Σ_z|A|(x, z)e^{md(x,z)}|B|(z, y)e^{md(z,y)},
so M_m(AB) ≤ N_m(A)M_m(B) and N_m(AB) ≤ N_m(A)N_m(B). For a set Ω of links, 1_Ω is the coordinate projection and
K_Ω := 1_ΩK1_Ω on ℓ²(Ω) (the compression). Σ_{b'}e^{-c d(b,b')} ≤ 4coth⁴(c/2) on every level-i torus (4 directions per
position; torus spheres are no larger than Z⁴ spheres).

- **Setting N5-bg (the level-0 fluctuation operator at a background).** Level i = 0 of Setting SC: fine links b of the
  level-0 torus (side TL), coarse links c = (X, X + e_μ), κ_0 ∈ [κ_-, κ_+], g = 1. A background is a pair (U, V), U on fine
  links, V on coarse links, SU(N)-valued (real background) or SL(N, C)-valued (complex background). Left-trivialised
  coordinates U_b → e^{A_b}U_b. With NA-FP's h_U, M_U, D_U, Λ, Λ_res^U, P_res^U (orthogonal projector onto Λ_res^U):
    O(U, V) := Hess_A|_{A=0}[S_W(e^AU) + κ_0Σ_cφ̂_c(V; M̄_c(e^AU))] + D_UP_res^UD_U^T,
    Π_U := 1 - h_U^T(h_Uh_U^T)^{-1}h_U,  Õ(U, V) := Π_UO(U, V)Π_U + (1 - Π_U),
    C(U, V) := Õ(U, V)^{-1} - (1 - Π_U),  𝒞(U, V) := Õ(U, V)^{-1/2} - (1 - Π_U),
  with S_W(U) := Σ_pRe tr(1 - U_p) and φ̂ := Nφ (φ of NA-alg (b), the normalised soft kernel; the factor N makes the
  trivial-background Hessian κ_0Q^TQ). Transposes are for the real bilinear form; for complex backgrounds every object is
  the holomorphic continuation of the real formula (see Lemma N5-an). At (U, V) = (1, 1): Õ(1, 1) = Õ_0 ⊗ 1_{su(N)}, with
  Õ_0 N5-triv's operator at i = 0 (S_W's quadratic part is ½||dA||²; M̄(e^A) = 1 + QA + O(A²) and W_0 = e^{QA + O(A²)}, so
  φ̂ = ½|QA|² + O(A³); h_1 = h, M_1 = block mean, D_1 = d; c35 A2 confirms the tensor structure numerically for SU(2)).
  On ran Π_U, Õ = Π_UOΠ_U, so C is the covariance of the gauge-fixed Gaussian δ(h_U)e^{-½⟨A,OA⟩}dA (the Hessian (Gaussian)
  level of NA-FP; at a critical background NA-FP (iii) makes this fixing legitimate; for N5's bounds criticality is not
  used). The variables of an entry Õ(b, b') are the links and coarse links of the blocks at coarse ℓ^∞ distance ≤ 2 from
  the block of b, and Õ(b, b') = 0 unless the blocks of b, b' are at ℓ^∞ distance ≤ 1 (so d(b, b') ≤ r_1 := 8L - 4).
  (Wilson: plaquettes through b and b'; soft: contours of coarse links touching the block of b or of b'; fixing: D_U,
  P_res^U act within a block and its neighbours; Π_U is block-diagonal.)

- **Lemma N5-cov (gauge covariance; failure mode N5bg-F3 does not occur): PROVEN-HERE [S19].** For g: sites → SU(N) put
  (gU)_b := g(x)U_bg(x + e_μ)^{-1}, (gV)_c := g(c_X)V_cg(c_{X+e_μ})^{-1}, (R_gA)_b := Ad(g(x))A_b (block-diagonal, orthogonal).
  Then O(gU, gV) = R_gO(U, V)R_g^{-1}, Π_{gU} = R_gΠ_UR_g^{-1}, hence Õ, C, 𝒞 transform the same way and every block norm
  |Õ(U, V)|(b, b'), |C|(b, b'), |𝒞|(b, b') is gauge invariant. For complex backgrounds and real g the same holds.
  *Proof.* S(e^{R_gA}gU) = S(g·(e^AU)) for S_W (e^{Ad(g(x))A_b}g(x)U_bg(y)^{-1} = g(x)e^{A_b}U_bg(y)^{-1}) and for the soft term,
  because M̄_c(g·U) = g(c_X)M̄_c(U)g(c_Y)^{-1} (the exact covariance used in NA-FP's composite slice), W_0 is covariant (unique
  maximiser, Re tr(W^{-1}M) invariant under (W, M) ↦ (aWb^{-1}, aMb^{-1})), and φ(gV; g·M) = φ(V; M); so the Hessians satisfy
  H_{gU} = R_gH_UR_g^{-1}. For the slice: in ℓ_P(A) = ΣAd(T_{j-1})ã_j, T'_{j-1} = g(c)T_{j-1}g(x_{j-1})^{-1} and ã'_j =
  Ad(g(x_{j-1}))ã_j (forward: directly; backward: ã = -Ad(U_b^{-1})A_b with A'_b = Ad(g(x_j))A_b and U'^{-1}_b = g(x_{j-1})U_b^{-1}
  g(x_j)^{-1}), so ℓ'_P(R_gA) = Ad(g(c))ℓ_P(A) and h_{gU}R_g = A_gh_U with A_g := ⊕_XAd(g(c_X)) orthogonal; hence
  Π_{gU} = R_gΠ_UR_g^{-1}. Likewise D_{gU}(Ad_gλ) = R_gD_Uλ, M_{gU}Ad_g = A_gM_U, Ad_g preserves Λ, so P_res^{gU} =
  Ad_gP_res^UAd_g^{-1}. Complex backgrounds: both sides are holomorphic in (U, V) for fixed real g and agree on the real
  backgrounds (a totally real set), so they agree. ∎ c35 A1 (SU(2), Haar g, t = 0.1): ||C(gU)R_ge - R_gC(U)e||/||C(U)e|| =
  2.4e-14, λ_min equal to 3.8e-14.

- **Lemma AX (curvature-small backgrounds are locally near 1): PROVEN-HERE [S19].** Let Λ_ℓ be a box of side ℓ sites in the
  level-0 torus with ℓ ≤ TL - 1 (it does not wrap), and suppose every plaquette p with all links in Λ_ℓ has |log U_p| ≤ ε
  (HS norm, principal log in su(N)) with 3(ℓ - 1)ε < min(π, 2π/√N). Then there is g: Λ_ℓ → SU(N) with
  |log(gU)_b| ≤ 3(ℓ - 1)ε for every link b with both ends in Λ_ℓ (principal log, in su(N)). If moreover |ρ_c| ≤ ε for the
  coarse links c with both blocks in Λ_ℓ (ρ_c := log(V_c^{-1}W_0(M̄_c(U))), NA-alg (b)) and 3p_L(ℓ - 1)ε ≤ 1/20, then
  |log(gV)_c| ≤ 9p_L(ℓ - 1)ε + ε for those c. In particular all these links are ≤ α(ε, ℓ) := 10p_Lℓε.
  *Proof.* Complete axial gauge from the corner o: T(x) the transport along the path o → x moving first in coordinate 1,
  then 2, 3, 4; g(x) := T(x) gives (gU)_b = T(x)U_bT(y)^{-1}, the holonomy of the closed loop (tree path to x)·b·(tree path to y)^{-1}.
  Tree links give 1. For b = (x, x + e_μ) the two paths o → y differ by moving the final e_μ-step back past the e_ν-runs
  with ν > μ: Σ_{ν>μ}(x_ν - o_ν) ≤ 3(ℓ - 1) elementary plaquette moves inside Λ_ℓ. Each move multiplies the holonomy by a
  conjugate of a plaquette holonomy U_p^{±1} (telescoping T(γ_{j-1})T(γ_j)^{-1}). On SU(N) with the bi-invariant metric of the
  HS inner product, d(W, 1) = min{|X| : X ∈ su(N), e^X = W} ≤ |log W| when log W ∈ su(N), d is bi-invariant and satisfies the
  triangle inequality, so d((gU)_b, 1) ≤ 3(ℓ - 1)ε. For W ∈ SU(N) with eigenvalue angles θ_j ∈ (-π, π], every X ∈ su(N) with
  e^X = W has |X|² ≥ Σθ_j², so the principal log obeys (Σθ_j²)^{1/2} ≤ d(W, 1) < π: no eigenvalue -1, and |Σθ_j| ≤ √N·d < 2π with
  Σθ_j ∈ 2πZ gives Σθ_j = 0, i.e. log W ∈ su(N) with |log W| ≤ 3(ℓ - 1)ε. Coarse links: each S4' contour transport T_j of c (in
  the gauge g) is a product of ≤ p_L links, so |log T_j| ≤ y := 3p_L(ℓ - 1)ε ≤ 1/20; NA-alg (a) gives W_0 = e^{X_0} with
  |X_0| ≤ |Ȳ| + 9.2y² ≤ 3y; W_0 and ρ are gauge covariant, (gV)_c = W_0(M̄_c(gU))e^{-ρ^g_c} with |ρ^g| = |ρ| ≤ ε, so
  d((gV)_c, 1) ≤ 3y + ε, and the principal log is in su(N) with the same bound as before. ∎

- **Lemma N5-an (local analyticity of the background operator): PROVEN-HERE [S19] (existence of the constants; not
  computed).** There are r_* ∈ (0, 1/(20p_L)] and S_* < ∞, depending only on (N, L, κ_±), such that for every entry (b, b') of
  Õ(U, V) and of Π_U: as a function of the logs (u_e, v_c) ∈ su(N)⊗C of its variables (Setting N5-bg), the entry is
  holomorphic on the polydisc 𝔻_* := {|u_e|, |v_c| ≤ r_*}, bounded there by S_* in block norm, and equal at u = v = 0 to the
  trivial value Õ_0(b, b')⊗1, resp. Π(b, b')⊗1. Consequently (Schwarz's lemma on ζ ↦ F(ζz/|z|_∞), |ζ| ≤ r_*) for max|u|, |v| ≤ α ≤ r_*,
  the block-norm deviation is ≤ (2S_*/r_*)α, and with n_1 := 4·(3L)⁴ (the links with base in the 3⁴ blocks around a block) and
  **C_Δ := 2S_*n_1/r_*:** N_0(|Õ(U, V) - Õ(1, 1)|) ≤ C_Δα and N_m(|Õ(U, V) - Õ(1, 1)|) ≤ e^{mr_1}C_Δα; the same for Π_U.
  *Proof.* Each entry is a finite composition of: entire functions of e^{±u} (Wilson Hessian; h_U, M_U, D_U, whose entries
  are polynomials in the entries of Ad of the link variables); inverses of h_Uh_U^T and of M_UP_ΛM_U^T, which at U = 1 equal
  ||w||²·1 and a block-diagonal positive matrix (M_1 is onto, NA-FP (ii)), hence holomorphic near 0; and the soft term,
  whose real-analyticity near 0 follows from NA-alg (a): W_0 = e^{X_0(M)} with X_0 the fixed point of Φ_M(X) = Ȳ + Π(K(X)),
  which is real-analytic in (X, M) with Lip_X Φ ≤ 0.23 on |X| ≤ 3y, so X_0 is real-analytic in M (analytic implicit function
  theorem; 1 - D_XΦ invertible), and M̄_c(e^AU) is a polynomial in the link entries; φ̂ is then real-analytic in (A, u, v) near
  0, and so is its A-Hessian at A = 0 as a function of (u, v). A real-analytic function on a neighbourhood of 0 in R^p
  continues holomorphically to a polydisc around 0 with a finite sup. Up to translation by L there are finitely many entry
  types (the trivial structure is L-periodic and each entry's variables lie in a fixed pattern of 5⁴ blocks), so one r_*,
  S_* serve for all; they do not depend on T once T ≥ 5 (no wrapping of the pattern). r_* ≤ 1/(20p_L) keeps NA-alg (a)'s
  hypothesis. ∎ *What is not done:* r_*, S_* are not computed; they enter only C_Δ and the threshold below. The Wilson
  part has an explicit constant (|δHess_p(A, A')| ≤ (e^{4α} - 1)(Σ_{j∈p}|A_j|)(Σ_{j∈p}|A'_j|) per plaquette, from the
  12 + 4·2 insertion terms of tr P and tr P^{-1}, so N_0 ≤ 24(e^{4α} - 1)), but the soft and slice parts do not.

- **Lemma CT♯ (Combes-Thomas for complex perturbations, block kernels, with the square root): PROVEN-HERE [S19].** Let
  K_0 be real symmetric on ℓ²(𝒢; su(N)⊗C) with K_0 ≥ γ > 0, and Δ an operator with |Δ| symmetric, ||Δ|| ≤ δ < γ, and
  D_m(|K_0|) + D_m(|Δ|) ≤ (γ - δ)/2. Then K := K_0 + Δ satisfies, for every t ≥ 0 and x, y:
  ||(K + t)^{-1}|| ≤ 1/(γ - δ + t), |(K + t)^{-1}|(x, y) ≤ (2/(γ - δ + t))e^{-md(x,y)}; the spectrum of K lies in
  {Re z ≥ γ - δ}; K^{-1/2} := π^{-1}∫_0^∞t^{-1/2}(K + t)^{-1}dt satisfies (K^{-1/2})² = K^{-1}, |K^{-1/2}|(x, y) ≤ (2/√(γ - δ))e^{-md(x,y)},
  and K^{-1/2} is the positive square root of K^{-1} when K is real symmetric. If Δ = Δ(z) depends holomorphically on
  parameters z with these bounds uniform, (K + t)^{-1} and K^{-1/2} are holomorphic in z.
  *Proof.* K + t = (K_0 + t)(1 + (K_0 + t)^{-1}Δ) with ||(K_0 + t)^{-1}Δ|| ≤ δ/(γ + t) < 1 gives the norm bound (Neumann series), and
  ||(K - z)^{-1}|| < ∞ for Re z < γ - δ in the same way. With f = d(·, y_0), E = e^{mf}: E(K + t)E^{-1} - (K + t) has block kernel
  K(x, y)(e^{m(f(x)-f(y))} - 1), and by the Schur test on the symmetric majorant |K|(x, y)(e^{md(x,y)} - 1) its norm is
  ≤ D_m(|K_0|) + D_m(|Δ|) ≤ (γ - δ + t)/2; so E(K + t)E^{-1} = (K + t)(1 + X') with ||X'|| ≤ ½, inverse norm ≤ 2/(γ - δ + t), and the
  (x, y_0) block of E(K + t)^{-1}E^{-1} is e^{mf(x)}(K + t)^{-1}(x, y_0). The integral converges absolutely in every entry by
  the decay bound and ∫_0^∞t^{-1/2}(γ - δ + t)^{-1}dt = π/√(γ - δ). For z ∉ (-∞, 0], z^{-1/2} (principal) = π^{-1}∫t^{-1/2}(z + t)^{-1}dt,
  so by the holomorphic functional calculus (Fubini over the Riesz integral; σ(K) ⊂ {Re z > 0}) K^{-1/2} = (z^{-1/2})(K), whose
  square is K^{-1}; for K real symmetric positive it is the spectral square root. Holomorphy: (K(z) + t)^{-1} is holomorphic,
  and the t-integral converges locally uniformly. ∎ (Lemma CT is the case Δ = 0.)

- **Theorem RW (random-walk expansion with Dirichlet-compressed block inverses): PROVEN-HERE [S19].** *Setting.* A level-i
  torus (coarse side T); a partition 𝒫 of the coarse torus into boxes □ with sides in [R, 2R) (R ≥ 1, T ≥ R: R - 1 boxes per
  direction of side R and one of side R + (T mod R), or similar); Ω_□ := the links based in blocks at coarse ℓ^∞ torus
  distance ≤ R from □ (so d(x, y) ≥ RL + 1 whenever y ∈ □ and x ∉ Ω_□); 1_□ the links based in □. K an operator on
  ℓ²(links; su(N)⊗C) such that, for some m > 0, γ' > 0, S_m < ∞:
  - (RW1) for every □ and t ≥ 0, K_{Ω_□} + t is invertible and |(K_{Ω_□} + t)^{-1}|(x, y) ≤ (2/(γ' + t))e^{-md(x,y)};
  - (RW2) N_m(|K|) ≤ S_m.
  Fix m_1 ∈ [0, m), a := m - m_1, and put **ε_R := (8S_m/γ')coth⁴(a/4)e^{-aRL/2}**. For t ≥ 0 let G_□(t) := (K_{Ω_□} + t)^{-1}
  (extended by zero), P(t) := Σ_□G_□(t)1_□, R_□(t) := -1_{Ω_□^c}KG_□(t)1_□, R(t) := Σ_□R_□(t), and for a walk ω = (□_0, …, □_n)
  T_ω(t) := G_{□_0}(t)1_{□_0}R_{□_1}(t)⋯R_{□_n}(t). If ε_R < 1, then for every t ≥ 0:
  - (i) (K + t)P(t) = 1 - R(t), N_{m_1}(Σ_□|R_□(t)|) ≤ ε_R(t) := (8S_m/(γ' + t))coth⁴(a/4)e^{-aRL/2} ≤ ε_R, and K + t is invertible with
    **(K + t)^{-1} = Σ_{n≥0}P(t)R(t)^n = Σ_ωT_ω(t)** (absolutely convergent);
  - (ii) **walk bounds:** M_{m_1}(Σ_{|ω|=0}|T_ω(t)|) ≤ 2/(γ' + t), and for n ≥ 1, M_{m_1}(Σ_{|ω|=n}|T_ω(t)|) ≤ (8coth⁴(a/2)/(γ' + t))ε_R(t)^n
    (entrywise sums of block norms); the truncation after n_0 steps errs by ≤ (8coth⁴(a/2)/(γ' + t))ε_R^{n_0+1}/(1 - ε_R) in M_{m_1}, and
    N_{m_1}((K + t)^{-1}) ≤ 8coth⁴(a/2)/((γ' + t)(1 - ε_R));
  - (iii) **square root:** K^{-1/2} := π^{-1}∫_0^∞t^{-1/2}(K + t)^{-1}dt = Σ_ω𝒯_ω, 𝒯_ω := π^{-1}∫t^{-1/2}T_ω(t)dt, (K^{-1/2})² = K^{-1},
    M_{m_1}(Σ_{|ω|=n}|𝒯_ω|) ≤ 2/√γ' (n = 0) and ≤ (8coth⁴(a/2)/√γ')ε_R^n (n ≥ 1); if K is real symmetric it is positive
    definite, λ_min(K) ≥ γ'(1 - ε_R)/(8coth⁴(m/2)), and K^{-1/2} is its positive square root;
  - (iv) **complex s-weakening:** for s = (s_□) ∈ C^𝒫 with |s_□| ≤ s̄, s̄ε_R < 1, K^{-1}(s; t) := P(t)(1 - Σ_□s_□R_□(t))^{-1}
    = Σ_ωs_ωT_ω(t), s_ω := Π_{j=1}^ns_{□_j}, is holomorphic in s, equals (K + t)^{-1} at s ≡ 1, obeys (ii) with ε_R → s̄ε_R, and
    **decouples:** if s_□ = 0 for every □ ∉ 𝒴, then K^{-1}(s; t)1_{□'} = G_{□'}(t)1_{□'} for every □' ∉ 𝒴 (supported in Ω_{□'});
    𝒞(s) := π^{-1}∫t^{-1/2}K^{-1}(s; t)dt has the same properties with the (iii) bounds (s̄ε_R in place of ε_R), and
    𝒞(s)1_{□'} = (K_{Ω_{□'}})^{-1/2}1_{□'} for □' ∉ 𝒴;
    **[R1819-fix RW-1: "the same properties" is too broad and is withdrawn. For s ∉ {0, 1}^𝒫, K^{-1}(s; t) is not the
    resolvent of a fixed operator (P(t), R(t) depend on t), so 𝒞(s)² ≠ K^{-1}(s; 0) in general, 𝒞(s) is not symmetric, and
    it is not positive for real s ∈ (0, 1). What carries over, and all that is claimed: 𝒞(s) is holomorphic in s; it obeys
    the (iii) M_{m_1}-bounds walk length by walk length with s̄ε_R in place of ε_R; 𝒞(1) = K^{-1/2}; and the column
    decoupling above. This is the form a Balaban-type use needs, with the fluctuation field written A = 𝒞(s)Z, Z white
    noise (s-interpolation of the field, not of a covariance); 𝒞(s)² is not claimed to be a covariance.]**
    **[R1819 remark RW-2: a cluster expansion in s needs s̄ ≫ 1 (Cauchy gains), i.e. s̄ε_R ≪ 1; with N5-sf0's R_* (ε_R ≤ ½)
    only s̄ < 2 is available. For that use R must be chosen larger: s̄ε_R ≤ θ needs R ≥ R_* + (2/(aL))log(s̄/(2θ))
    (ε_R(R) ≤ ½e^{-aL(R - R_*)/2}); the theorem allows any R, N5-sf0's stated R_* does not.]**
  - (v) **locality:** T_ω(t) depends on K only through the compressions K_{Ω_{□_j}} and the blocks 1_{□_{j-1}}K1_{Ω_{□_j}};
    if K(x, z) = 0 whenever the blocks of x, z are at ℓ^∞ distance > 1, then T_ω ≠ 0 only if each □_{j-1} contains a block at
    ℓ^∞ distance R + 1 from □_j (at most 7⁴ choices of □_{j-1} given □_j), and T_ω depends only on the entries of K with an index
    in ∪_jΩ_{□_j}.
  *Proof.* (K + t)G_□ = (1_Ω + 1_{Ω^c})(K + t)1_ΩG_□ = 1_Ω + 1_{Ω^c}KG_□ (1_{Ω^c}t1_Ω = 0). Multiplying by 1_□ on the right and
  summing over □ (1_Ω1_□ = 1_□, Σ1_□ = 1) gives (i)'s identity. For x ∉ Ω_□, y ∈ □: |R_□(t)|(x, y) ≤ Σ_{z∈Ω}|K|(x, z)(2/(γ' + t))e^{-md(z,y)}
  ≤ (2/(γ' + t))e^{-md(x,y)}N_m(|K|) (d(x, y) ≤ d(x, z) + d(z, y)); y lies in one □, so Σ_□|R_□|(x, y) ≤ (2S_m/(γ' + t))e^{-md(x,y)}1[d(x, y) > RL],
  and N_{m_1} ≤ (2S_m/(γ' + t))e^{-aRL/2}Σ_ye^{-ad/2} ≤ ε_R(t). N_0 is the ℓ^∞ → ℓ^∞ operator bound, so 1 - R(t) is invertible
  and (K + t)P(1 - R)^{-1} = 1; finite dimension gives (K + t)^{-1} = P(1 - R)^{-1} = ΣPR^n, and expanding R^n gives the walks. (ii):
  entrywise Σ_{|ω|=n}|T_ω| ≤ |P|(Σ_□|R_□|)^n; M_{m_1}(|P|) ≤ 2/(γ' + t), N_{m_1}(|P|) ≤ (2/(γ' + t))·4coth⁴(a/2), M_{m_1}(Σ_□|R_□|) ≤
  (2S_m/(γ' + t))e^{-aRL} ≤ ε_R(t), and M(AB^n) ≤ N(A)N(B)^{n-1}M(B). (iii): integrate (ii) against π^{-1}t^{-1/2} (ε_R(t) ≤ ε_R and
  ∫t^{-1/2}(γ' + t)^{-1} = π/√γ'); σ(K) ∩ (-∞, 0] = ∅ because K + t is invertible for t ≥ 0, so the functional-calculus argument of
  CT♯ applies; real symmetric K has real eigenvalues μ with μ + t ≠ 0 for all t ≥ 0, so μ > 0, and ||K^{-1}|| ≤ N_0(|K^{-1}|) (Schur,
  K^{-1} symmetric) ≤ 8coth⁴(m/2)/(γ'(1 - ε_R)) by (ii) at m_1 = 0. (iv): R(s; t)^n = Σs_{□_1}⋯s_{□_n}R_{□_1}⋯R_{□_n}, and the bounds
  are those of (ii) with each R_□ multiplied by |s_□| ≤ s̄; R_□1_{□'} = 0 for □ ≠ □' and s_{□'}R_{□'} = 0, so R(s)1_{□'} = 0,
  (1 - R(s))^{-1}1_{□'} = 1_{□'} and K^{-1}(s)1_{□'} = P1_{□'} = G_{□'}1_{□'}; integrating in t gives 𝒞(s)1_{□'} = π^{-1}∫t^{-1/2}G_{□'}(t)dt
  1_{□'} = (K_{Ω_{□'}})^{-1/2}1_{□'} (CT♯'s functional calculus on ℓ²(Ω_{□'})). (v): by inspection of R_□ = -1_{Ω^c}K1_ΩG_□1_□
  and the product 1_{□_{j-1}}R_{□_j}; the count: such □_{j-1} meet the box of side < 4R + 2 around □_j, which meets ≤ 7 boxes of
  side ≥ R per direction. ∎ c35 B (d = 2 abelian model, T = 12, L = 3): ÕP = 1 - R to ≤ 6e-15; measured q = N_0(|R|) = 1.39
  (R = 1, no convergence), 0.377 (R = 2), 0.106 (R = 3); truncation errors e_n fall geometrically (R = 3: 3.0e-3, 9.1e-5, 9.9e-7,
  3.0e-8, …, 3.8e-15 at n = 12) and stay ≤ 0.078 × the (ii)-type bound with the measured norms; decoupling (iv) exact (0.0) at
  complex s = 0.5 + 0.5i; the walk-expanded square root (iii) agrees with the exact one to 7e-14. The PROVEN ε_R with the
  measured constants is ≥ 10⁵ at these R (CT's condition D_m ≤ γ/2 forces m ≲ 0.01 here): the theorem's constants, not the
  mechanism, are what is crude.

- **Corollary RW-triv (the random-walk expansion at the trivial background, every level): PROVEN-HERE [S19] (counted with
  Theorem RW).** For every i ≥ 0, k, T, Theorem RW applies to K = Õ_i (N5-triv) with γ' = γ_i, m = m_cov, S_m := p_m²(S_O + E_O(m)) +
  (n_Π - 1)e^{4m(L-1)}: (RW1) because compressions of Õ_i ≥ γ_i are ≥ γ_i (Rayleigh quotient) and D_m(|(Õ_i)_Ω|) ≤ D_m(|Õ_i|) ≤ 𝔇(m) ≤
  γ_i/2, so Lemma CT applies to each compression; (RW2) by Lemmas N5-sl, N5-loc and the product rule. With m_1 := m_cov/2 and
  R ≥ R_triv := ⌈(4/(m_covL))log(16S_mcoth⁴(m_cov/8)/γ_i)⌉ one has ε_R ≤ ½; so Õ_i^{-1}, Õ_i^{-1/2}, hence C_i = Õ_i^{-1} - (1 - Π) and
  𝒞_i = Õ_i^{-1/2} - (1 - Π) (Π commutes with Õ_i; 1 - Π is block-local), have walk expansions with walk-length suppression
  2^{-n}, the s-weakened forms, and the decoupling property, uniformly in i, k, T. (No wrapping condition is needed: if
  T < 2R + 1, Ω_□ is the whole torus, R(t) = 0 and the expansion is the single term.)

- **Theorem N5-sf0 (N5 at small-field backgrounds for the level-0 fluctuation operator): PROVEN-HERE [S19]; CONFIRMED-WITH-FIX
  by REVIEW_S18_S19. [R1819-fix SF-3] It is an existence theorem: ε_* and T_0 depend on the analyticity constants r_*, S_* of
  Lemma N5-an, which exist and are not computed, so ε_* is explicit only up to C_Δ = 2S_*n_1/r_* (and up to r_* when
  α_* = r_*). [R1819-fix SF-2] The gap proven in (b) is λ_min ≥ γ'(1 - ε_R)/(8coth⁴(m/2)) ≈ 7·10⁻⁸² (product-rule m) or
  ≈ 4·10⁻⁵¹ (N5-w0's m), 43-73 orders of magnitude below γ_0. Proposition RW-ℓ² [S20] (below) improves it to
  λ_min ≥ γ'(1 - ε_R)/9 ≈ 6.6·10⁻¹⁰, within a factor 18 of γ' (≈ 1.19·10⁻⁸); everywhere a "gap" of N5-sf0 is quoted, these
  are the numbers.**
  *Constants.* γ_0 := c_1min(1/2, κ_-/2)/L² (Lemma N5-coer at i = 0, where c_E = 1/2 since E_0 = ½||dA||²; ν_N ≥ 1
  **[R1819-fix: ν_N ≥ 1 holds at L = 3; for every L the minimum in N5-coer is the c_1 term, so γ_0 is as stated]**); 𝔇_0, S_O^{(0)} :=
  24 + 16κ_+p_L + 32 and E_O^{(0)}(m) := 24(e^{2m} - 1) + (e^{mp_L} - 1)(16κ_+p_L + 32) are N5-triv's at i = 0 (H_0 = d*d has range 2, so
  no m' < m_*' constraint), m_cov^{(0)} the largest m with 𝔇_0(m) ≤ γ_0/2. Fix m ∈ (0, m_cov^{(0)}) and m_1 ∈ (0, m), a := m - m_1; put
    α_* := min{r_*, (γ_0/2 - 𝔇_0(m))/(C_Δe^{mr_1})},  γ' := γ_0 - C_Δα_* (≥ γ_0/2),  S'_m := N_m(|Õ_0|) + e^{mr_1}C_Δα_*,
    ε_R := (8S'_m/γ')coth⁴(a/4)e^{-aRL/2},  R_* := the least R with ε_R ≤ ½,  T_0 := 4R_* + 6,
    **ε_* := α_*/(10p_L(4R_* + 5)L).**
  *Background classes.* 𝔑(α) := the complex backgrounds (U, V) such that for every □ of the R_*-partition there is a real
  gauge g_□ on Ω^+_□ (the blocks at coarse ℓ^∞ distance ≤ R_* + 3 from □) with |log(g_□U)_e|, |log(g_□V)_c| ≤ α for all links and
  coarse links inside Ω^+_□. *Statement.* Let T ≥ T_0. (a) Every real (U, V) with |log U_p| ≤ ε for all plaquettes and |ρ_c| ≤ ε
  for all coarse links, ε ≤ ε_*, lies in 𝔑(α_*); and 𝔑(α_*) contains the complex neighbourhood {(e^zU, e^{z'}V) : (U, V) real with
  10p_L(4R_* + 5)Lε ≤ α_*/4, |z_e|, |z'_c| ≤ α_*/8} (z, z' ∈ su(N)⊗C). (b) For every (U, V) ∈ 𝔑(α_*), Theorem RW holds for
  K = Õ(U, V) with (γ', m, S'_m) and R = R_*: Õ(U, V) + t is invertible for all t ≥ 0; C(U, V), 𝒞(U, V) have the walk expansions
  of RW (i)-(iv) (with (1 - Π_U) subtracted), so, uniformly in k (level 0 is k-independent apart from κ_0) and T ≥ T_0:
  - |C(U, V)|(b, b') ≤ c_Ce^{-m_1d(b,b')}, |𝒞(U, V)|(b, b') ≤ c_𝒞e^{-m_1d(b,b')}, with c_C := 2/γ' + 8coth⁴(a/2)ε_R/(γ'(1 - ε_R)) + c_Πe^{4m_1(L-1)},
    c_𝒞 the same with γ' → √γ' in the first two terms, c_Π := max|w|²/||w||² + C_Δα_* (the (1 - Π_U) entries, range 4(L - 1));
  - (N5's ℓ¹) N_{m''}(|𝒞|) ≤ 8coth⁴(a/2)/(√γ'(1 - ε_R)) + (ν_w + C_Δα_*)e^{4m''(L-1)} for 0 ≤ m'' ≤ m_1 **[R1819-fix SF-4:
    ν_w here means N5-sl's n_Π - 1 for general L, or its exact value 30/13 at L = 3 (Lemma N5-w0 C1)]**; (N5's ℓ²)
    Σ_{b'}|𝒞|(b, b')² ≤ M_0(𝒞)N_0(|𝒞|) **[S20: for real backgrounds also ≤ 9(N² - 1)/(γ'(1 - ε_R)), Proposition RW-ℓ²]**;
  - for real (U, V) ∈ 𝔑(α_*): Õ(U, V) > 0, so C ≥ 0 is the gauge-fixed covariance and 𝒞 its positive square root; gap
    λ_min(Õ) ≥ γ'(1 - ε_R)/(8coth⁴(m/2)) **[R1819-fix SF-2: ≈ 7·10⁻⁸² / 4·10⁻⁵¹ at the evaluated constants; S20:
    ≥ γ'(1 - ε_R)/9 by Proposition RW-ℓ²]**;
  - (analyticity, for RLF-5/N10) every entry of C, 𝒞, of each walk term and of the s-weakened 𝒞(s) is holomorphic on 𝔑(α_*)
    (uniform limits of holomorphic functions), with the bounds above **[R1819-fix SF-5: read "holomorphic on a neighbourhood of
    each point of 𝔑(α)" for every α < α_*: 𝔑(α_*) is defined by closed conditions plus the existence of gauges, and N5-an's
    holomorphy holds on the open polydisc of radius r_* ≥ α_*, so it covers a neighbourhood of 𝔑(α) for α < α_* (and of
    𝔑(α_*) itself when α_* < r_*); in the form N10/(RLF-5) uses, the entries are holomorphic in (z, z') on (a)'s parametrised
    neighbourhood z ↦ (e^zU, e^{z'}V), |z_e|, |z'_c| < α_*/8]**;
  - (locality) each walk term T_ω depends on (U, V) only through its restriction to ∪_jΩ^+_{□_j} (RW (v) with the variable
    pattern of Setting N5-bg), and walks are R_*-box-connected in the sense of RW (v).
  *Proof.* (a) Each Ω^+_□ is a box of side ≤ (4R_* + 5) blocks < T, so it does not wrap; Lemma AX with ℓ = (4R_* + 5)L gives the
  gauges, with 10p_Lℓε ≤ α_* ≤ r_* ≤ 1/(20p_L) implying AX's hypotheses. For the complex neighbourhood, |log(e^Xe^Y)| ≤ 2(|X| + |Y|)
  for |X| + |Y| ≤ ¼ (|e^Xe^Y - 1| ≤ e^{|X|+|Y|} - 1 and |log(1 + W)| ≤ |W|/(1 - ||W||)), and conjugation by real g preserves |z|. (b) (RW1):
  for □, gauge g = g_□: by Lemma N5-cov, K_{Ω_□} = R_g^{-1}(Õ(gU, gV))_{Ω_□}R_g **[R1819-fix SF-1: was R_g(·)R_g^{-1}; N5-cov gives
  Õ(gU, gV) = R_gÕ(U, V)R_g^{-1}; harmless, R_g is block-diagonal orthogonal]**, and (Õ(gU, gV))_{Ω_□} = (Õ(1, 1))_{Ω_□} + Δ_□ where Δ_□'s
  entries involve only variables inside Ω^+_□ (Setting N5-bg), all ≤ α_*; by Lemma N5-an, ||Δ_□|| ≤ N_0(|Δ_□|) ≤ C_Δα_*, D_m(|Δ_□|) ≤
  (e^{mr_1} - 1)C_Δα_*, and |Δ_□| is symmetric (Õ is symmetric for the bilinear form, its continuation complex symmetric).
  (Õ(1, 1))_{Ω_□} ≥ γ_0 (compression of Õ_0 ⊗ 1 ≥ γ_0, N5-triv) and D_m(|(Õ(1, 1))_Ω|) ≤ 𝔇_0(m). The choice of α_* gives
  𝔇_0(m) + (e^{mr_1} - 1)C_Δα_* ≤ (γ_0 - C_Δα_*)/2, so CT♯ gives (RW1) with γ' (R_g is block-diagonal orthogonal, so block norms and d are
  unchanged). (RW2): the row of b ∈ □ has block norms equal to those of Õ(g_□U, g_□V) (Lemma N5-cov), whose entries differ from
  Õ_0's by Lemma N5-an; so N_m(|Õ(U, V)|) ≤ N_m(|Õ_0|) + e^{mr_1}C_Δα_* = S'_m. Then Theorem RW with R = R_* (ε_R ≤ ½). The bounds:
  RW (ii)-(iii) at m_1, plus the (1 - Π_U) entries from Lemma N5-an; Π_U commutes with Õ (Õ = Π_UOΠ_U ⊕ 1), so the functional
  calculus of Õ^{-1/2} respects ran Π_U ⊕ ran(1 - Π_U) and 𝒞 = Õ^{-1/2} - (1 - Π_U). ℓ²: Σ_{b'}|𝒞|(b, b')² ≤ sup|𝒞|·Σ_{b'}|𝒞|(b, b').
  Positivity and the gap: RW (iii). Analyticity: each G_□(t) is holomorphic on 𝔑(α_*) by CT♯ (holomorphic dependence of Δ_□ in
  local coordinates), so each T_ω is; the walk series and the t-integral converge uniformly (bounds independent of the point),
  and the torus is finite. Locality: RW (v). ∎
  *The threshold, evaluated (κ ≡ 1, L = 3, p_L = 11, r_1 = 20; arithmetic with expm1, c35_time.txt).* γ_0 = 1.587·10⁻⁸. With
  N5-triv's product-rule 𝔇_0 (slope 2.01·10⁹): m_cov^{(0)} = 3.95·10⁻¹⁸; taking m := m_4 (𝔇_0(m_4) = γ_0/4) = 1.97·10⁻¹⁸ and m_1 = m/2:
  α_* = min(r_*, γ_0/(4C_Δe^{mr_1})) ≈ 3.97·10⁻⁹/C_Δ, R_* ≈ 1.4·10²⁰, T_0 ≈ 5.7·10²⁰, **ε_* ≈ 2.1·10⁻³²/C_Δ** (when α_* < r_*).
  With Lemma N5-w0 (target C, below) in place of the product rule: m = 9.66·10⁻¹¹, S'_m ≈ 25.5, R_* ≈ 1.7·10¹², T_0 ≈ 6.9·10¹²,
  **ε_* ≈ 1.7·10⁻²⁴/C_Δ**. These are uniform but astronomically small; the measured level-0 gap (target C) is 2.5·10⁶ times γ_0,
  and on (Z/6)⁴ the SU(2) model gap survives to plaquette angles ≈ 0.2 (c35 A).
  *What it is and is not.* It is N5's gap, ℓ², ℓ¹, exponential decay, analyticity on a complex neighbourhood, and the
  random-walk expansion with complex s-weakening, for the level-0 fluctuation operator at every background whose plaquette
  curvature and soft fluctuation are ≤ ε_*, uniformly in T ≥ T_0, with a curvature-only hypothesis (no global small-field
  gauge: the local gauges are glued by the walk expansion; flat backgrounds with non-trivial holonomy on large tori are
  included). It is NOT: the level-i statement for i ≥ 1 (below, conditional); a statement for tori with T < T_0 (there a global
  small-field gauge is needed, failure mode BNA-F4's flat classes); explicit in r_*, S_*; sharp (the threshold is far below any
  physically relevant scale; target C). The background's criticality is not used; NA-FP (iii) is what makes the fixing
  legitimate at a critical background, and the background dependence of FP_U (NA-FP) is not addressed.

- **Proposition N5-sf_i (levels i ≥ 1): PROVEN as an implication; not counted.** Let (NA-H_loc)_i be: there are r_H > 0 and a
  function δ_H(α, m) → 0 (α → 0) such that the level-i operator Õ_i(U, V) (Hessian of E_i^{NA} + κ_i soft term at (U, V), slice
  and residual term as in Setting N5-bg) is complex symmetric and holomorphic on 𝔑_i(α) (defined with level-i boxes and a
  fattening r_H), and for every □ and gauge g_□ of 𝔑_i(α): N_m(|(R_gÕ_i(U, V)R_g^{-1} - Õ_i(1, 1))_{Ω_□}|) ≤ δ_H(α, m)
  **[R1819-fix SF-1: was R_g^{-1}Õ_iR_g; R_gÕ_i(U, V)R_g^{-1} = Õ_i(g_□U, g_□V)]** and
  N_m(|Õ_i(U, V)|) ≤ N_m(|Õ_i|) + δ_H(α, m) (with Õ_i(1, 1) = Õ_i ⊗ 1, N5-triv). Then the conclusions (b) of Theorem N5-sf0 hold at
  level i with γ_i, any m < m_cov, and α_* replaced by any α with 𝔇(m) + 2δ_H(α, m) ≤ γ_i/2 (the same proof: CT♯ with
  ||Δ_□|| ≤ δ_H, Theorem RW), except the locality statement (Hess E_i^{NA} is not finite range; a localisation of its background
  dependence is part of what (NA-H_loc) would have to come with). (NA-H_loc) is a localised form of (NA-H) ⊂ B-NA: OPEN.
  **[R1819-fix 7] (NA-H_loc)_i is not only a Hessian estimate:** it is a statement about Hess E_i^{NA} at (U, V), and E_i^{NA}
  is defined by minimising the lower levels, so it presupposes the level-i SU(N) background minimiser, its regularity and
  its exponential locality (B-NA / N2 / L2). It sits inside B-NA, not next to it. Session 20 proves the level-1 case for the
  critical branch (Theorem NAH1, [S20] below), and states what level i needs (Proposition NAH-ind).

- **Target C (γ and the rate): what is sharper, what is proven, what is measured.**
  - **Lemma N5-w0 (exact slice vector and level-0 first moment, L = 3): PROVEN-HERE [S19] (computer-assisted; strengthens
    N5-triv at i = 0, no count change).** **[R1819-fix W0-1: as written in session 19 the rate was a numerical verification
    (double precision, heuristic 10⁻⁹ margin, float zero test), not a computer-assisted proof. Session 20 redid C2 in exact
    rational arithmetic on Z⁴ (check c36 C, criteria first): every row of Õ_0 vanishes exactly outside the 3⁴ blocks around
    the reference block (support distance ≤ 11), Õ_0 is exactly symmetric there, **N_0(|Õ_0|) = 10462237/410670 = 25.47602**,
    **max_bΣ_{b'}|Õ_0(b, b')|d(b, b') = 449171/10935 = 41.07645**, and the exact rational inequalities
    (449171/10935)·m(1 + 40m) ≤ γ_0/2 at m = 1.93·10⁻¹⁰ and ≤ γ_0/4 at m_4 = 9.66·10⁻¹¹ hold (e^{20m} ≤ 1 + 40m). So the rate
    m_cov^num = 1.93·10⁻¹⁰ and m_4 = 9.66·10⁻¹¹ are now computer-assisted in exact arithmetic, and N5-sf0's second threshold
    (≈ 1.7·10⁻²⁴/C_Δ) stands on the same footing as the product-rule one.]** In exact rational arithmetic (c35 C1): ||w||² = 104/729, Σ|w| = 8/3, max|w| = 10/81,
    so N_0(|1 - Π|) = ν_w := max|w|·Σ|w|/||w||² = 30/13 (N5-sl's bound: ≤ 576). The rows of Õ_0 (κ = 1; 324 link types, computed
    on the coarse torus T = 3 and lifted to Z⁴ distances; range one block, validated on T = 5 to 0 and 6e-15) give
    N_0(|Õ_0|) ≤ 25.476 and max_bΣ_{b'}|Õ_0(b, b')|d(b, b') ≤ 41.077 (floating point, a priori margin 10⁻⁹ relative; c35 C2).
    Since e^x - 1 ≤ xe^x and d ≤ r_1 = 20 on the support, D_m(|Õ_0|) ≤ 41.077·m·e^{20m}; so Lemma CT holds at
    **m_cov^num = 1.93·10⁻¹⁰** (D ≤ γ_0/2), against N5-triv's product-rule m_cov^{(0)} = 3.95·10⁻¹⁸ (×4.9·10⁷). [Disclosed: c35 C2
    printed the product-rule value as 1.0093·10⁻¹⁷; that number is a float-cancellation artefact of exp(x) - 1 at x ~ 10⁻¹⁷ in
    the script; the expm1 value is 3.9457·10⁻¹⁸ (post-run arithmetic, c35_time.txt). C2's criterion is unaffected (margins
    ≥ 10⁷).] The same exact-w improvement applies to every level i in N5-triv's 𝔇 (n_Π - 1 → 30/13), not evaluated here.
  - **γ: no cheap rigorous improvement found.** γ_i is set by PG's c_1 = 1/(3.5·10⁶). A Bloch-fibre minimum is a measurement:
    **γ_meas(Õ_0) = 0.03985** (min over (2π/8)Z⁴, at K = (π, π, π, π); Bloch construction validated to 1.5e-14; the SU(2) model
    on (Z/6)⁴ gives the same 0.039849, c35 A2) against γ_0 = 1.59·10⁻⁸ (ratio 2.5·10⁶); for the lower-bound operator
    2c_E·d*d + κQ^TQ + dP_resd* (which, by Lemma E-low, bounds Õ_i from below at every level i): **γ_meas^LB = 8.138·10⁻³ = 2c_E**
    (at K = (0, 0, 0, π)) against N5-triv's γ_i = 1.29·10⁻¹⁰ (ratio 6.3·10⁷). A rigorous all-K lower bound by a Lipschitz grid is
    out of reach in 4D at these gaps (step ~ γ/Lip), so this is recorded as measured only. The measured equality γ^LB = 2c_E
    suggests that the proven loss is entirely in c_1 (the orbit/PG step), not in the per-mode energy: a sharper PG constant is
    the lever. Measured decay at the trivial background (T = 5, fit r = 4..20): m_meas ≈ 0.43 against m_cov^num = 1.9·10⁻¹⁰.

- **Check c35** (criteria first, checks/c35_criteria.md; run record checks/c35_time.txt). **A PASS** (SU(2), (Z/6)⁴, model
  level-0 operator with κ|Q_UA|² in place of the full soft Hessian): Wilson Hessian vs finite differences 3.9e-8; NA-FP (i)
  1.1e-14; gauge covariance 2.4e-14; trivial SU(2) = abelian ⊗ 1 (λ_min 0.0398492, 2.6e-15); linear response
  Δ_{0.003}/Δ_{0.001} = 3.000-3.008 at every distance (analytic dependence); decay slope unchanged to 4 digits for t ≤ 0.01;
  informational: λ_min = 0.0398, 0.0397, 0.0382, 0.0237, -0.065 at t = 0, 0.01, 0.03, 0.1, 0.3 (max plaquette angles 0, 0.023,
  0.068, 0.22, 0.66), ||Õ(U_t) - Õ(1)|| ≈ 5.7t (a measured C_Δα with α = t). **B PASS** (above). **C PASS** (above). Peak
  memory footprints 0.46, 1.17, 1.17 GB (< 1.2 GB).

- **N5 node status [S19].** OPEN, narrowed. PROVEN: the trivial background at every level (N5-triv [S18]) with its random-walk
  expansion and complex s-weakening (Theorem RW, Corollary RW-triv); the level-0 operator at every curvature-small background
  on tori T ≥ T_0, with gap, ℓ², ℓ¹, decay, analyticity on a complex neighbourhood, background-local walk terms and
  s-weakening (Theorem N5-sf0). Still needed: levels i ≥ 1 at non-trivial backgrounds, which Proposition N5-sf_i reduces to
  (NA-H_loc) (a localised (NA-H) ⊂ B-NA); small tori T < T_0; explicit r_*, S_*; the background dependence of FP_U; the
  cluster-expansion uses ((H-Mayer), N7/(DF1)).

---

**[S20] REVIEW_S18_S19 fixes; the ℓ² gap; (NA-H_loc) at level 1 by the Schur complement (targets pre-stated in RTARGET.md
§44 at 23:58 UTC on 2026-10-27, before this text; c36 criteria before the c36 script).**

- **[R1819-fix] Where each binding fix of REVIEW_S18_S19 now sits.** SF-1: N5-sf0 proof (b) and Proposition N5-sf_i (R_g
  orientation). SF-2: N5-sf0 heading, its (b) gap line, the S19 header and the N5 node (gap sizes stated; Proposition RW-ℓ²
  below). SF-3: N5-sf0 heading (existence theorem) and RTARGET §43 (annotation, §43 text not edited). SF-4, SF-5: N5-sf0 (b).
  RW-1, RW-2: Theorem RW (iv). W0-1: Lemma N5-w0 (below, after c36 C). Fix 7: Proposition N5-sf_i. Fix 8: RLARGE.md (F1 in
  §7.2 Setting; F2 in §1A and §7.2 (iv); G5 as (R1-loc), §8.2 (W1-ret') (d) and §8.3 step 2; the N5 ↔ RLARGE threshold
  compatibility and the c_RS dependence of n_♯ in §1A item 1). Fix 9 (optional, both applied): γ_i doubles by
  orthogonality (Lemma N5-coer), M' in Lemma N5-loc. Fix 10: LINEAR_PACKAGE.md FROZEN v1.1 (errata, change log §12; the v1
  text kept as LINEAR_PACKAGE_v1_snapshot.md). No fix changes a count.

- **Proposition RW-ℓ² (the ℓ² form of the walk expansion; repairs the gap loss of SF-2): PROVEN-HERE [S20] (strengthens
  Theorem RW (iii) and Theorem N5-sf0 (b); no count change).** In the setting of Theorem RW, let μ_𝒫 := max_x#{□ : x ∈ Ω_□},
  and assume in addition to (RW1)-(RW2)
  - (RW1-n) ||(K_{Ω_□} + t)^{-1}||_{ℓ²→ℓ²} ≤ 1/(γ' + t) for every □ and t ≥ 0.
  Then for every t ≥ 0: ||P(t)|| ≤ μ_𝒫^{1/2}/(γ' + t), ||R(t)|| ≤ ε_R(t), and **||(K + t)^{-1}|| ≤ μ_𝒫^{1/2}/((γ' + t)(1 - ε_R))**.
  If K is real symmetric, **λ_min(K) ≥ γ'(1 - ε_R)/μ_𝒫^{1/2}**. For the partitions of Theorem RW (box sides in [R, 2R)),
  **μ_𝒫 ≤ 3^d = 81**.
  *Proof.* Each G_□(t)1_□f is supported in Ω_□, so pointwise |Σ_□(G_□1_□f)(x)|² ≤ #{□ : x ∈ Ω_□}·Σ_□|(G_□1_□f)(x)|² (Cauchy-Schwarz),
  and summing over x, ||P(t)f||² ≤ μ_𝒫Σ_□||G_□1_□f||² ≤ μ_𝒫(γ' + t)^{-2}Σ_□||1_□f||² = μ_𝒫(γ' + t)^{-2}||f||². For R(t): RW (i)'s
  proof gives the block-norm majorant Σ_□|R_□(t)|(x, y) ≤ (2S_m/(γ' + t))e^{-md(x,y)}1[d(x, y) > RL], which is symmetric in
  (x, y); the Schur test bounds ||R(t)|| by its row sum ≤ (2S_m/(γ' + t))e^{-mRL/2}·4coth⁴(m/4) ≤ ε_R(t) (e^{-aRL/2}coth⁴(a/4)
  decreases in a, and a ≤ m). So (K + t)^{-1} = P(t)(1 - R(t))^{-1} (RW (i)) has the stated norm, and for real symmetric K > 0
  (RW (iii)) λ_min = ||K^{-1}||^{-1}. Multiplicity: x ∈ Ω_□ iff in every direction μ the block coordinate x_μ is within torus
  distance R of the interval I_μ(□); the intervals of one direction are disjoint with lengths ≥ R, and if k of them meet a
  window of 2R + 1 consecutive points, the k - 2 inner ones lie in the window minus its two end points, so (k - 2)R ≤ 2R - 1
  and k ≤ 3 (for R = 1 all intervals have length 1 and k = 3); a window covering the whole circle (2R + 1 ≥ T) meets
  ⌊T/R⌋ ≤ 3 intervals. ∎
  *Where it applies.* (RW1-n) holds for Corollary RW-triv (compressions of Õ_i ≥ γ_i, Rayleigh) and for Theorem N5-sf0
  (CT♯ gives ||(K_{Ω_□} + t)^{-1}|| ≤ 1/(γ_0 - C_Δα_* + t) = 1/(γ' + t); R_g is orthogonal). Hence in N5-sf0 (b), for real
  backgrounds: **λ_min(Õ(U, V)) ≥ γ'(1 - ε_R)/9 ≥ γ_0/36** (≈ 6.6·10⁻¹⁰ at κ ≡ 1, L = 3, against γ_0 = 1.59·10⁻⁸ and the
  session-19 bound ≈ 4·10⁻⁵¹), **||C(U, V)|| ≤ 9/(γ'(1 - ε_R))**, and N5's ℓ² bound Σ_{b'}|𝒞|(b, b')² ≤
  Σ_{b'}||𝒞(b, b')||²_HS ≤ (N² - 1)||𝒞||² ≤ 9(N² - 1)/(γ'(1 - ε_R)) (𝒞 = Π_UÕ^{-1/2}Π_U). With the same argument,
  **N_0(|(K + t)^{-1}|) ≤ μ_𝒫((N² - 1)n_Ω)^{1/2}/((γ' + t)(1 - ε_R))**, n_Ω := max_□#(links of Ω_□) ≤ d((4R + 1)L)^d (each row
  of G_□ has ≤ n_Ω blocks, so Σ_y|G_□|(x, y) ≤ n_Ω^{1/2}(Σ_y||G_□(x, y)||²_HS)^{1/2} ≤ ((N² - 1)n_Ω)^{1/2}||G_□||; and N_0(|P|) ≤ μ_𝒫max_□N_0(|G_□|), N_0((1 - R)^{-1}) ≤ (1 - ε_R)^{-1}). This sup-norm bound is
  used below (it beats RW (ii)'s 8coth⁴(a/2)/(γ'(1 - ε_R)) by ~10¹⁴ at N5-sf0's evaluated constants).

- **[R1819-fix W0-1] Lemma N5-w0 in exact arithmetic (RTARGET §44 B; check c36 C, criteria first).** C2 redone on Z⁴ with
  every entry a rational: exact zero pattern (3⁴ blocks, support distance ≤ 11), exact symmetry, N_0(|Õ_0|) = 10462237/410670,
  first moment 449171/10935 = 41.0764518, and the rate inequalities at m = 1.93·10⁻¹⁰ (D_m ≤ γ_0/2) and m_4 = 9.66·10⁻¹¹
  (≤ γ_0/4) as exact rational inequalities. The double-precision values of c35 C2 agree to 1e-10 relative. N5-w0's rate is
  computer-assisted (exact) from session 20 on (see the annotation at the lemma).

**[S20] (NA-H_loc) at level 1 by the Schur complement (RTARGET §44 A).** Notation of Settings N5-0, N5-bg; d = 4, L ≥ 3
odd, levels 0 → 1 → 2. Level-1 backgrounds are pairs (V, W): V on level-1 links (= the coarse links of the level-0 step),
W on level-2 coarse links. The level-0 problem is F(U, V) := S_W(U) + κ_0Σ_cφ̂_c(V; M̄_c(U)) (Setting N5-bg's functional),
f_V(A) := F(e^AU^(0)(V), V) in the chart at the lift below, and the gauge group of the level-0 problem at fixed V is the
fluctuation group 𝒢_V = {g : g(c_X) = 1} (Lemma NA-inv). 𝔅_1(ε) := the real (V, W) with |log V_P| ≤ ε for every level-1
plaquette and |ρ_C(V, W)| ≤ ε for every level-2 coarse link C (ρ_C := log(W_C^{-1}W_0(M̄_C(V))), the level-1 soft
fluctuation). Throughout, (γ', m, m_1, a, S'_m, R_*, T_0, α_*, ε_*) are Theorem N5-sf0's level-0 constants, and

  𝔠_∞ := min{8coth⁴(a/2), 81((N² - 1)n_Ω)^{1/2}}/(γ'(1 - ε_R)) + ν_w + C_Δα_*   (n_Ω at R = R_*; the numbers below use N = 2),

a bound for N_0(|C(U, V)|) on 𝔑(α_*) (RW (ii) at m_1 = 0, or Proposition RW-ℓ²'s sup-norm bound, plus the (1 - Π_U) part).

- **Lemma U0 (the exact lift): PROVEN-HERE [S20].** For a level-1 field V (any SU(N) or SL(N, C) values) define U^(0)(V) on
  level-0 links b = (x, x + e_μ): U^(0)_b := 1 if x and x + e_μ lie in the same block, and U^(0)_b := V_{(X, μ)} if x ∈ B(X),
  x + e_μ ∈ B(X + e_μ). Then:
  - (i) **M̄_c(U^(0)(V)) = V_c exactly** for every level-1 link c, so ρ_c(U^(0)(V), V) = 0 (W_0(V_c) = V_c for V_c ∈ SU(N));
  - (ii) every fine plaquette of U^(0) has holonomy 1, except the block-corner plaquettes (x, μ, ν) with x_μ ≡ x_ν ≡ L - 1
    (mod L), whose holonomy is the level-1 plaquette holonomy V_P of (X, μ, ν), X the block of x;
  - (iii) (covariance) for every level-1 gauge G, U^(0)(GV) = Ĝ·U^(0)(V), Ĝ(x) := G(X) for x ∈ B(X);
  - (iv) **the gradient of F(·, V) at U^(0) comes from the corner plaquettes only:** ||∇_AF(e^AU^(0), V)|_{A=0}||_∞ ≤ 6ε_V,
    ε_V := max_P|log V_P| (block norm, HS on su(N)), for real V.
  *Proof.* (i) In the S4' contour T^σ_y = P^σ(c_X → y)·S_y·P^σ(c_Y → y + Le_μ)^† the two axial legs stay inside B(X), resp.
  B(Y) (the complete-axial path stays in the box spanned by its end points), so they are 1, and the straight leg S_y crosses
  exactly one μ-boundary (from B(X) to B(Y)), on which U^(0) = V_c: T^σ_y = V_c for every (σ, y), and M̄_c = V_c. (ii) A
  plaquette with no crossing link is 1; with exactly one crossing direction μ its two μ-links are crossing links of the same
  level-1 link and its ν-links are interior: V_cV_c^{-1} = 1; at a corner the four links are the four level-1 links of V_P.
  (iii) Interior links: G(X)1G(X)^{-1} = 1; crossing links: G(X)V_cG(X + e_μ)^{-1} = (GV)_c. (iv) By (i) and NA-alg (b), the
  soft term φ̂ = Nφ, φ = N^{-1}[Re tr(W_0^{-1}M) - Re tr(V^{-1}M)], is stationary in M at V = W_0(M) (the first-order change of
  Re tr(W_0(M)^{-1}M) in M is Re tr(W_0^{-1}δM), W_0 being a maximiser), so its A-gradient vanishes at A = 0. For the Wilson
  term, |d/ds Re tr(1 - e^{sX}W)|_{s=0}| = |Re tr(XW)| ≤ |X||(W - W^†)/2|_HS ≤ |X||log W| for W = a conjugate of U_p
  (eigenvalue angles: Σsin²θ_j ≤ Σθ_j²); a link lies in 2(d - 1) = 6 plaquettes and only corner plaquettes are ≠ 1. ∎
  c36 A (SU(2), d = 4, T = 2, t = 0.7, Haar coarse gauge): A PASS: ||M̄_c - V_c|| ≤ 7.5e-14, non-corner plaquettes ≤ 1.3e-15, the 864 corner plaquettes equal V_P exactly, covariance
  3.2e-16, |ρ_c| ≤ 5.0e-14.

- **Lemma FPq (quantitative Faddeev-Popov invertibility): PROVEN-HERE [S20].** Let c_D(L) be the lowest eigenvalue of the
  graph Laplacian of the grid {0, …, L - 1}^d with a Dirichlet condition at the centre (c_D(3) ≥ 2663/31250 = 0.085216 (float 0.0852175), certified by an
  exact rational LDLᵀ, scratch consts.py), s_M(1) := (L^d - 1)^{1/2}/L^d (= 0.1104 at L = 3) and ||D|| ≤ 2√d. Then for every
  background U:
  - (i) (Kato) **||D_Uλ||² ≥ c_D||λ||²** for every λ ∈ Λ;
  - (ii) if in every block a gauge makes the links with both ends in the block ≤ α_b, with η_M := e^{4(L-1)α_b} - 1 ≤
    L^{d/2}s_M(1)/2, then the singular values of M_U on Λ ⊖ ker M_U are ≥ s_M(1)/2 =: s_M, and **χ_UΓ_U (NA-FP (ii)) obeys
    ||λ|| ≤ K_FP||χ_UΓ_Uλ||, K_FP := max{(2/c_D)(1 + √c_D/(4√d)), (1 + 4√d/√c_D)/s_M}** (K_FP ≤ 514.5 at L = 3, d = 4).
  *Proof.* (i) |(D_Uλ)_b| = |Ad(U_b)λ(y) - λ(x)| ≥ ||λ(y)| - |λ(x)|| (Ad orthogonal), so ||D_Uλ||² ≥ ||df||² for the scalar
  f := |λ| ≥ 0, which vanishes at every block centre; keep only the links inside blocks and use the Dirichlet gap on each
  block. (ii) Per block, M_Uλ = L^{-d}Σ_y[avg_σAd(T^σ(c_X ← y))]λ(y); in the block gauge each transport is a product of
  ≤ 2(L - 1) links, ||Ad(T) - 1|| ≤ e^{2|log T|} - 1 ≤ η_M, and λ ↦ L^{-d}Σ_yλ(y) has norm L^{-d/2}; at U = 1, M_1M_1^* =
  (L^d - 1)L^{-2d}, so all singular values are s_M(1), and they move by ≤ η_ML^{-d/2} ≤ s_M(1)/2 (Weyl). Block norms and
  singular values are gauge invariant (NA-FP's covariance). Write χ_UΓ_Uλ = (a, ν), a = M_Uλ (NA-FP (i)), ν = P_res^UD_U^*D_Uλ,
  λ = λ_r + λ_⊥ with λ_r ∈ Λ_res^U = ker M_U. Then ||a|| ≥ s_M||λ_⊥|| and ⟨λ_r, ν⟩ = ||Dλ_r||² + ⟨Dλ_r, Dλ_⊥⟩ ≥
  ||Dλ_r||(||Dλ_r|| - ||D||||λ_⊥||). If ||λ_⊥|| ≤ √c_D||λ_r||/(2||D||), then ||ν|| ≥ ||Dλ_r||²/(2||λ_r||) ≥ c_D||λ_r||/2 and
  ||λ|| ≤ (1 + √c_D/(2||D||))||λ_r||; otherwise ||λ|| ≤ (1 + 2||D||/√c_D)||λ_⊥|| ≤ (1 + 2||D||/√c_D)||a||/s_M. ∎

- **Lemma N5-an♭ (analyticity constants for the joint Hessian): PROVEN-HERE [S20] (existence; not computed; same proof as
  Lemma N5-an).** There are r_♭ ∈ (0, 1/(20p_L)] and S_♭ < ∞, depending only on (N, L, κ_±), such that every entry of the
  gradient and of the joint (A, B)-Hessian of (A, B) ↦ F(e^Ae^uU, e^Be^vV) (u, v the logs of the local link variables) and every
  entry of h_U, D_U, P_res^U (Setting N5-bg's slice/fixing objects, at level 0 and, with the same functions, at level 1) is
  holomorphic in (A, u, B, v) on the closed polydisc of radius r_♭ and bounded there by S_♭ in block norm. Hence (two-point
  Schwarz on ζ ↦ F(z + ζ(z' - z)/|z' - z|_∞), |ζ| ≤ r_♭/2) every such entry is Lipschitz with constant 4S_♭/r_♭ in the sup norm
  of its variables on the polydisc of radius r_♭/2, and with n_1 = 4(3L)⁴: **C_♭ := 4S_♭n_1/r_♭** bounds the N_0-Lipschitz
  constant of Hess f, of the joint Hessian and of the level-1 slice/fixing operators, and the entrywise deviations from the
  trivial values at (u, v) of size α ≤ r_♭/2 are ≤ (2S_♭/r_♭)α (N_0 ≤ C_♭α/2). *Proof.* That of Lemma N5-an: finite
  compositions of entire functions, of the inverses (h_Uh_U^T)^{-1}, (M_UP_ΛM_U^T)^{-1} (holomorphic near U = 1), and of the
  analytic implicit function X_0(M) of NA-alg (a); the chart A ↦ e^Ae^uU is entire; finitely many entry types modulo
  translation. ∎ We may and do take r_♭ ≤ r_*, and C_Δ ≤ C_♭.

- **Lemma BR1 (the critical branch of the level-0 problem at curvature-small V): PROVEN-HERE [S20].** Let T ≥ T_0 and put
  r(ε) := 12𝔠_∞ε,
    ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }.
  For every real level-1 field V with ε_V ≤ ε ≤ ε_br:
  - (i) there is a unique A* = A*(V) in {A ∈ ker h_{U^(0)} : ||A||_∞ ≤ r(ε)} with Π_{U^(0)}[∇f_V(A) + D_0P_0D_0^*A] = 0
    (D_0 := D_{U^(0)}, P_0 := P_res^{U^(0)});
  - (ii) **U(V) := e^{A*}U^(0)(V) is a critical point of F(·, V)** (no fixing term), and P_0D_0^*A* = 0;
  - (iii) (U(V), V) satisfies N5-sf0 (a) with ε' := (1 + 36p_L𝔠_∞)ε ≤ ε_*: |log U(V)_p| ≤ ε + 4r(ε), |ρ_c(U(V), V)| ≤ 3p_Lr(ε);
    so N5-sf0 (b) and Proposition RW-ℓ² hold at (U(V), V); in particular U(V) is a non-degenerate local minimum of F(·, V)
    modulo 𝒢_V (Õ(U(V), V) ≥ γ'(1 - ε_R)/9 > 0);
  - (iv) U(GV) = Ĝ·U(V) for every level-1 gauge G (Lemma U0 (iii)), so E_1^br(V) := F(U(V), V) is gauge invariant;
  - (v) V ↦ A*(V) extends holomorphically to the complex neighbourhood {e^zV : |z_c| ≤ α_*/8, V real, ε_V ≤ ε_br/4}, with the
    same bounds; E_1^br is holomorphic there.
  *Proof.* (U^(0)(V), V) has ρ = 0 and plaquettes ≤ ε_V ≤ ε_* (Lemma U0), so it is in 𝔑(α_*) and C_0 := C(U^(0), V) exists with
  N_0(|C_0|) ≤ 𝔠_∞; C_0 is the inverse of Π_0O_0Π_0 on ker h_0 (O_0 = Hess f_V(0) + D_0P_0D_0^*, Setting N5-bg), so
  C_0Π_0O_0x = x for x ∈ ker h_0. Put Φ(A) := A - C_0Π_0[∇f_V(A) + D_0P_0D_0^*A] on ker h_0. For A, A' ∈ ker h_0 in the ball,
  Φ(A) - Φ(A') = C_0∫_0^1[Hess f_V(0) - Hess f_V(A_s)](A - A')ds (C_0Π_0 = C_0), and by Lemma N5-an♭ (in the local AX gauge of
  each row, whose links are ≤ 3(3L - 1)ε ≤ r_♭/6, with ||A||_∞ ≤ r ≤ r_♭/2; block norms are gauge invariant)
  N_0(|Hess f_V(A_s) - Hess f_V(0)|) ≤ C_♭r. So Lip(Φ) ≤ 𝔠_∞C_♭r = 12𝔠_∞²C_♭ε ≤ ½, and ||Φ(A)||_∞ ≤ ||Φ(0)||_∞ + r/2 ≤
  6𝔠_∞ε_V + r/2 ≤ r (Lemma U0 (iv)). Banach's fixed point theorem gives (i). (ii) is Lemma NA-crit with Lagrange multipliers:
  Φ(A*) = A* means ∇f_V(A*) + D_0P_0D_0^*A* = h_0^Tμ for some μ. Gauge invariance of F under 𝒢_V gives ⟨∇f_V(A*), τλ⟩ = 0,
  τλ := -dexp_{A*}^{-1}(D_{U(V)}λ) (the orbit tangent in the chart; dexp_A = (e^{ad_A} - 1)/ad_A), for every λ ∈ Λ. So
  ⟨(ν, -μ), 𝔉λ⟩ = 0 with ν := P_0D_0^*A*, 𝔉λ := (P_0D_0^*τλ, h_0τλ) = -χ_0dexp_{A*}^{-1}D_{U(V)}λ. At A* = 0 this is -χ_0Γ_0,
  and ||λ|| ≤ K_FP||χ_0Γ_0λ|| (Lemma FPq at U^(0), whose block links are ≤ 3(L - 1)ε by AX on each block). The perturbation:
  ||χ_0|| ≤ ||h_0|| + ||D_0|| ≤ (2(L - 1))^{1/2} + 2√d ≤ 6 (L = 3; Schur on h_0's block norms, ≤ the unsigned path weights,
  row sums ≤ 2(L - 1), column sums ≤ 1), ||dexp_A^{-1} - 1|| ≤ 0.59·2|A| for |A| ≤ ½ (the series z/(1 - e^{-z}) - 1 = z/2 +
  z²/12 - …, Σ|b_n| ≤ 0.59 on |z| ≤ 1), ||Ad(e^{A}) - 1|| ≤ e^{2|A|} - 1 ≤ 3.5|A|, so ||dexp^{-1}D_{U(V)} - D_0|| ≤ 1.2r·2√d +
  3.5r·√d ≤ 12r (each site heads d links), and ||𝔉 + χ_0Γ_0|| ≤ 72r ≤ 1/(2K_FP) (ε ≤ 1/(1728𝔠_∞K_FP)). So 𝔉 is injective, hence onto (dim Λ = dim of
  χ_0's target, NA-FP (ii)), and ν = 0, μ = 0, ∇f_V(A*) = 0; the left-trivialised gradient at U(V) is dexp^{-T}∇f_V = 0.
  (iii) A plaquette holonomy of U(V) differs from that of U^(0) by four left factors e^{A*_b} (conjugated), so the
  bi-invariant distance moves by ≤ 4r; each S4' transporter of c moves by ≤ p_Lr, M̄_c(U(V)) = V_c·avg_je^{Y_j} with
  |Y_j| ≤ p_Lr ≤ 1/20, and NA-alg (a) with the covariance W_0(MV) = W_0(M)V gives |ρ_c| = |X_0| ≤ 3p_Lr. The non-degeneracy is
  N5-sf0 (b) and Proposition RW-ℓ². (iv) Uniqueness: h, P_res, D at Ĝ·U^(0) are R_Ĝ-conjugates of those at U^(0) (Lemma
  N5-cov) and f_{GV}(R_ĜA) = f_V(A), so A*(GV) = R_ĜA*(V). (v) For complex V in the stated neighbourhood, U^(0)(V) is in
  N5-sf0 (a)'s complex neighbourhood, every bound above holds with the complex class 𝔑(α_*), Φ is holomorphic in (A, V) and
  a uniform contraction, so its fixed point is holomorphic (uniform limit of the holomorphic iterates). ∎
  *Not shown:* that U(V) is the global minimiser of F(·, V) (B-NA's uniqueness at one level; named **(MIN_1)**). E_1^br is
  the critical-branch value; E_1^NA := min_UF = E_1^br on 𝔅_1(ε_br) iff (MIN_1) holds. c36 B (d = 2 SU(2) model, exact N = 2 soft density, Haar coarse gauge): at t = 0.05 the
  contraction from the lift converges in 16 steps to residual 6.5e-14; the limit is critical without the fixing (gradient
  1.8e-14) with ||P_res D^*A*|| = 2.2e-14 (B1). At t = 0.15 (max coarse plaquette angle 0.78) it diverges: **B FAIL as
  pre-registered** (a post-run diagnostic, disclosed, finds convergence up to angles ≈ 0.6; BR1 is a small-ε statement).

- **Lemma SC1 (the Hessian of the branch value is the Schur complement of N5-sf0's covariance): PROVEN-HERE [S20].** For V
  as in Lemma BR1, with all derivatives at (U(V), V) in left-trivialised coordinates (A on level-0 links, B on level-1
  links; F_AA = Hess f, F_AB the mixed block, F_BB the B-Hessian) and C := C(U(V), V) of Setting N5-bg:
    **H_1(V) := Hess_B E_1^br(e^BV)|_{B=0} = F_BB - F_BA C F_AB.**
  The right side does not depend on the weight of the residual fixing term, nor on the slice (any admissible χ_U).
  *Proof.* Write U(e^BV) = e^{a(B)}U(V) (a real-analytic, a(0) = 0, Lemma BR1 (v)) and g(a, B) := F(e^aU(V), e^BV). Criticality
  of every U(e^BV) gives ∂_ag(a(B), B) = 0 (the chart gradient is dexp^T of the left-trivialised one). Hence
  E(B) := g(a(B), B) has E'' = g_BB + g_Ba a'(0) and g_aa a'(0) = -g_aB. g_aa = F_AA at the critical U(V) annihilates D_UΛ (Lemma
  NA-inv), and g_aB(·) ⊥ D_UΛ (differentiate ⟨∂_ag(0, B), D_Uλ⟩ = 0, gauge invariance at every B). Moreover ker F_AA = D_UΛ:
  if F_AAv = 0, admissibility (NA-FP (ii)) gives λ with v_0 := v - D_Uλ ∈ ker h_U and P_res^UD_U^*v_0 = 0; then Ov_0 = 0 with
  O = F_AA + D_UP_res^UD_U^*, so Π_UOΠ_Uv_0 = 0 and v_0 = 0 (Õ(U(V), V) > 0, Lemma BR1 (iii)). So a'(0) is determined modulo
  ker F_AA, against which g_aB is orthogonal; choose the representative x ∈ ker h_U with P_res^UD_U^*x = 0: Ox = F_AAx = -g_aB,
  Π_UOΠ_Ux = -Π_Ug_aB, x = -Cg_aB. So E''(0) = F_BB - ⟨F_AB, CF_AB⟩. Any other fixing weight w or admissible χ changes x only by
  an element of D_UΛ, against which F_AB is orthogonal. ∎ At (V, W) = (1, 1): U(1) = 1 and H_1(1) = κ_0(1 - κ_0QC_0Q^T)⊗1, the
  abelian Hess E_1 of Lemma N5-loc (= -κ_0sym(𝓡_1)); c36 D1 checks this against LED-dual's symbol (c31 E). c36 B2 (t = 0.05): the fourth-order finite-difference
  second derivative of the re-solved E^br along 6 random level-1 directions agrees with ⟨B, (F_BB - F_BACF_AB)B⟩ to ≤ 2.1e-7; B3:
  ||Hess(D_Uλ)||/||λ|| = 2.4e-11 at the branch, and changing the fixing weight 1 → 3 changes the Schur result by 1.3e-14.

- **Lemma LOC (localisation of the background covariance): PROVEN-HERE [S20].** Let (U, V) ∈ 𝔑(α_*) be real, Λ' a set of
  level-0 links and g a gauge on a non-wrapping box containing the variables of every entry Õ(b, b') with b or b' in Λ', such
  that in the gauge g all these variables are ≤ α' ≤ α_*. Put K := R_gÕ(U, V)R_g^{-1}, K^0 := Õ(1, 1), and suppose the
  links b, b' have ℓ¹ distance ≥ D from every link outside Λ'. Then
    |K^{-1} - (K^0)^{-1}|(b, b') ≤ A_inα'e^{-m_1d(b,b')} + A_oute^{-m_1D/2},
    A_in := 16coth⁴(a/2)e^{m_1r_1}C_Δ/(γ'γ_0),  A_out := 32coth⁴(m_1/4)·c_K(S'_m + N_0(|Õ_0|))/γ',  c_K := c_C + c_Π.
  The same holds for C = K^{-1} - (1 - Π) up to the term |Π_U - Π|(b, b') ≤ (2S_*/r_*)α'1[d(b, b') ≤ 4(L - 1)].
  *Proof.* Let Δ := K - K^0 and K^♮ := K^0 + 1_{Λ''}Δ1_{Λ''} (Λ'' := the links whose entries' variables are inside the gauge
  box, ⊃ Λ'). N_0(|1_{Λ''}Δ1_{Λ''}|) ≤ C_Δα' and D_m ≤ (e^{mr_1} - 1)C_Δα', so CT♯ (as in N5-sf0 (b)) gives |(K^♮)^{-1}|(x, y) ≤
  (2/γ')e^{-md(x,y)}, hence N_{m_1}(|(K^♮)^{-1}|) ≤ 8coth⁴(a/2)/γ'. (i) (K^♮)^{-1} - (K^0)^{-1} = -(K^♮)^{-1}(1_{Λ''}Δ1_{Λ''})(K^0)^{-1}, and
  M_{m_1}(ABC) ≤ N_{m_1}(A)N_{m_1}(B)M_{m_1}(C) with M_{m_1}((K^0)^{-1}) ≤ 2/γ_0: the A_in term. (ii) K^{-1} - (K^♮)^{-1} =
  -K^{-1}(K - K^♮)(K^♮)^{-1}; K - K^♮ vanishes on Λ'' × Λ'' and has range r_1, so every term Σ_{z,z'}|K^{-1}|(b, z)|K - K^♮|(z, z')
  |(K^♮)^{-1}|(z', b') has z or z' outside Λ'', at distance ≥ D from b or from b'. With |K^{-1}|(b, z) ≤ c_Ke^{-m_1d(b,z)} (N5-sf0 (b))
  and splitting e^{-m_1d} = e^{-m_1d/2}e^{-m_1d/2}: the sum is ≤ 2·c_K·4coth⁴(m_1/4)·N_0(|K - K^♮|)·(2/γ')e^{-m_1D/2}, and
  N_0(|K - K^♮|) ≤ N_0(|K|) + N_0(|K^0|) ≤ S'_m + N_0(|Õ_0|). ∎

- **Theorem NAH1 ((NA-H_loc) at level 1, for the critical branch): PROVEN-HERE [S20], unreviewed.** Let Õ_1(V, W) be the
  level-1 operator of Proposition N5-sf_i at i = 1 with E_1^NA replaced by E_1^br:
    Õ_1(V, W) := Π_V[H_1(V) + κ_1Hess_B(Σ_Cφ̂_C(W; M̄_C(e^BV)))|_{B=0} + D_VP_res^VD_V^*]Π_V + (1 - Π_V) =: Π_V𝒪_1Π_V + (1 - Π_V),
  so that Õ_1(1, 1) = Õ_1 ⊗ 1 with Õ_1 N5-triv's operator at i = 1 (Lemma SC1 at the trivial background). Put μ_1 := Lm_1 (the
  level-0 decay rate in level-1 units) and fix 0 < m ≤ μ_1/2 and the level-1 partition size R^{(1)} (in the use below,
  R^{(1)} is the R of Theorem RW for Õ_1-type operators with S'_m := N_m(|Õ_1|) + γ_1/4, fixed before ε). For ρ ≥ 1 (level-1
  units) and D ≥ 1 (level-0 units) let
    ℓ_1(ρ, D) := 2ρ + 2⌈D/L⌉ + 4,  α := 3ℓ_1ε,  α' := 2(α + r(ε)),
    S_F := 32κ_+p_L,  n_ρ := d(2ρ + 1)^d·(2L)^{2d} (level-0 entry pairs of a near row),
    δ_Sch(ε; ρ, D) := C_♭α' + e^{16m}[C_♭α'·4c_Ccoth⁴(m_1/4)S_F + S_F²A_inα'·4coth⁴(m_1/4)]
                     + e^{16m + mρ}S_F²A_out n_ρe^{-m_1D/2} + 4S_F²c_Ke^{16μ_1}coth⁴(μ_1/8)e^{-μ_1ρ/4},
    δ_𝒪 := C_♭α'e^{mr_1} + δ_Sch,  p'_m := N_m(|Π|) + C_♭α'e^{mr_1},  S_𝒪 := N_m(|𝒪_1^0|) (Lemma N5-loc at i = 1),
    **δ_H^{(1)}(ε, m; ρ, D) := p'_m²δ_𝒪 + C_♭α'e^{mr_1}(2 + 2p'_m(S_𝒪 + δ_𝒪)).**
  Take ρ(ε) := max(⌈(4/μ_1)log(1/ε)⌉, d(4R^{(1)} + 5)L) (so ρ ≥ the level-1 ℓ¹ diameter of every Ω^{+(1)}_□) and D(ε) := ⌈(2/m_1)(mρ(ε) + log(n_{ρ(ε)}/ε))⌉; then the two exponential terms are ≤ (const)ε,
  ℓ_1 = O(log(1/ε)/m_1), α' = O(ε log(1/ε)), and **δ_H^{(1)}(ε, m) := δ_H^{(1)}(ε, m; ρ(ε), D(ε)) = O(ε log(1/ε)) → 0**, with a
  constant explicit in the ledger's constants and the existence constants (r_*, S_*, r_♭, S_♭). Let ε_H be the largest
  ε ≤ ε_br such that 3ℓ_1(ρ(ε), D(ε))ε ≤ min(α_*/4, r_♭/6) and α'(ε) ≤ α_*, and let
  T_0^{(1)} := ⌈ℓ_1(ρ(ε_H), D(ε_H))/L⌉ + 1. Then for every T ≥ max(T_0, T_0^{(1)}) and (V, W) ∈ 𝔅_1(ε), ε ≤ ε_H:
  - (a) Õ_1(V, W) is real symmetric and extends to a complex symmetric operator, holomorphic in (z, z') on
    {(e^zV, e^{z'}W) : |z|, |z'| ≤ α_*/8} (Lemma BR1 (v), Lemma SC1, Lemma N5-an♭);
  - (b) for every level-1 R^{(1)}-box □ there is a level-1 gauge g_□ (Lemma AX on the box of side ℓ_1 around □, restricted)
    with N_m(|(R_{g_□}Õ_1(V, W)R_{g_□}^{-1} - Õ_1(1, 1))_{Ω^{(1)}_□}|) ≤ δ_H^{(1)}(ε, m);
  - (c) N_m(|Õ_1(V, W)|) ≤ N_m(|Õ_1|) + δ_H^{(1)}(ε, m).
  That is, (NA-H_loc)_1 of Proposition N5-sf_i holds for the branch, with the curvature class 𝔅_1(ε) in place of 𝔑_1(α).
  *Proof.* (a) Lemma BR1 (v) (holomorphy of U(V)), SC1 (H_1 is the Schur complement of holomorphic entries; C(U(V), V) is
  holomorphic, N5-sf0 (b)), N5-an♭ (the level-1 soft, slice and fixing parts); symmetry of Hessians and of C. (b) Fix □ and a
  level-1 box Λ_1 of side ℓ_1 whose central part of side ℓ_1 - 2⌈D/L⌉ - 4 contains Ω^{+(1)}_□ (and, for (c), the ball of radius
  ρ around a given link). Λ_1 does not wrap (T ≥ T_0^{(1)}), so Lemma AX at level 1 gives g with V's links and W's coarse links in
  Λ_1 bounded by 3ℓ_1ε = α (AX's smallness conditions hold since α ≤ min(α_*/4, r_♭/6) ≤ 1/(20p_L)). In the block-constant
  extension ĝ, U^(0)(V) has links ≤ α in the blocks of Λ_1 (Lemma U0 (iii)), and U(V) = e^{A*}U^(0) has links ≤ 2(α + r) = α'
  (|log(e^Xe^Y)| ≤ 2(|X| + |Y|), Lemma BR1 (i), with R_ĝA* in place of A*). Let Λ'' be the level-0 links in the blocks of Λ_1.
  (1) *Products.* Π_V𝒪_1Π_V - Π^0𝒪_1^0Π^0 = ΔΠ·𝒪_1Π_V + Π^0Δ𝒪_1Π_V + Π^0𝒪_1^0ΔΠ; N_m is submultiplicative, N_m(|ΔΠ|) ≤
  C_♭α'e^{mr_1}/2 ≤ C_♭α'e^{mr_1} (N5-an♭ at level 1; Π_V is level-1-block-diagonal), N_m(|Π_V|) ≤ p'_m: this gives the
  formula for δ_H^{(1)} from any bound δ_𝒪 for N_m(|Δ𝒪_1|) restricted to the rows in question. (2) *Finite-range parts of 𝒪_1*
  (level-1 soft Hessian, D_VP_res^VD_V^*): deviation ≤ C_♭α'e^{mr_1}/2 (N5-an♭). (3) *The Schur part.* In the gauge,
  ΔH_1 = ΔF_BB - [ΔF_BA·C·F_AB + F_BA^0·ΔC·F_AB + F_BA^0·C^0·ΔF_AB], all at (U(V), V) vs (1, 1). F_BB is diagonal in c (each φ̂_c
  depends on V_c only), N_0(|ΔF_BB|) ≤ C_♭α'/2. F_AB(·, c) is supported in the two blocks of c; its trivial value is -κ_0Q^T, so
  N_0(|F_AB|), N_0(|F_BA|) ≤ max(16κ_+, κ_+p_L) + C_♭α'/2 ≤ S_F, and N_0(|ΔF_AB|), N_0(|ΔF_BA|) ≤ C_♭α'/2. For c, c' with
  d_1(c, c') ≤ ρ inside the central part, the level-0 links b, b' of their supports lie in Λ'' at ℓ¹ distance ≥ D from its
  complement, so Lemma LOC (with α' ≤ α_*) gives |ΔC|(b, b') ≤ A_inα'e^{-m_1d_0(b,b')} + A_oute^{-m_1D/2}. Distances:
  L·d_1(c, c') ≤ d_0(b, b') + 2·d(2L - 1) ≤ d_0 + 16L at d = 4, so e^{md_1} ≤ e^{16m}e^{(m/L)d_0} and also e^{md_1} ≤ e^{mρ}
  on the near part; N_{m/L}(|C|) ≤ c_C·4coth⁴((m_1 - m/L)/2) ≤ 4c_Ccoth⁴(m_1/4) (m/L ≤ m_1/2). Summing the three terms over
  the ≤ n_ρ entries of the near part gives the first three terms of δ_Sch (the A_out term counted entrywise with the weight e^{mρ}, the decaying terms through N_{m/L}).
  (4) *Far part* (only in (c); in (b) every pair in Ω^{(1)}_□ is near, since ρ(ε) ≥ the level-1 ℓ¹ diameter of Ω^{+(1)}_□, and
  n_ρ bounds the number of entries in a row): for d_1(c, c') > ρ only H_1(V) is non-zero,
  |H_1(V)|(c, c') ≤ S_F²c_Ke^{-m_1(Ld_1 - 16L)} (|C| ≤ c_Ke^{-m_1d_0}, N5-sf0 (b) at (U(V), V), Lemma BR1 (iii)), and
  Σ_{d_1>ρ}e^{-(μ_1 - m)d_1} ≤ 4coth⁴(μ_1/8)e^{-μ_1ρ/4} (μ_1 - m ≥ μ_1/2): the last term of δ_Sch. In (c),
  |Õ_1(V, W)|(c, c') ≤ |Õ_1^0|(c, c') + |ΔÕ_1|(c, c') on the near part, with block norms gauge invariant. (5) *Choice of
  ρ, D.* e^{-μ_1ρ/4} ≤ ε by ρ(ε); A_out n_ρe^{mρ}e^{-m_1D/2} ≤ A_outε by D(ε); since ρ, D = O(log(1/ε)) (m ≤ μ_1/2 and
  log n_ρ = O(log ρ)), α = 3ℓ_1ε = O(ε log(1/ε)). ∎
  *Remark (failure modes of RTARGET §44).* NAH1-F1 does not occur: the level-0 slice/residual bookkeeping enters only through
  Lemma FPq (Kato + the block mean), which is uniform in the background and in T; the level-1 coarse gauge acts on the
  level-0 problem through block-constant gauges (Lemma U0 (iii)), which preserve the level-0 slice and fixing (Lemma N5-cov).
  NAH1-F2 does not occur: the lift is global and exact (Lemma U0), and the contraction is in sup norm with T-independent
  constants. NAH1-F3 does not occur: Lemma LOC localises the background dependence of C, with an exponentially small
  remainder in the margin D. NAH1-F4: see Proposition NAH-ind.

- **Corollary N5-sf1 (N5 at level 1, critical branch): PROVEN-HERE [S20] (counted with Theorem NAH1).** Let ε_*^{(1)} := the
  largest ε ≤ ε_H with 𝔇_1(m) + 2δ_H^{(1)}(ε, m) ≤ γ_1/2 (𝔇_1 N5-triv's 𝔇 at i = 1, m < m_cov^{(1)}). For (V, W) ∈ 𝔅_1(ε),
  ε ≤ ε_*^{(1)}, and T ≥ max(T_0, T_0^{(1)}, 4R^{(1)} + 6): the conclusions (b) of Theorem N5-sf0 hold for Õ_1(V, W) with γ_1 in
  place of γ_0, γ'_1 := γ_1 - 2δ_H^{(1)}, the level-1 R^{(1)}-partition and rate m, and Proposition RW-ℓ²'s gap
  λ_min(Õ_1(V, W)) ≥ γ'_1(1 - ε_R)/9, except the finite-range locality of walk terms (H_1(V) is not finite range; its
  background dependence is localised by Lemma LOC up to e^{-m_1D/2} remainders, not by a support statement).
  *Proof.* Proposition N5-sf_i's proof (CT♯ with ||Δ_□|| ≤ δ_H, Theorem RW, Proposition RW-ℓ²) with Theorem NAH1 (b)-(c) in place
  of (NA-H_loc)_1. ∎ For E_1^NA := min_UF (rather than the branch) the same holds under (MIN_1).

- **Proposition NAH-ind (the inductive form for level i; RTARGET §44 A (6)): PROVEN as an implication; not counted.** For
  i ≥ 1 let **(I_i)** be: on the curvature class 𝔅_i(ε_i) (level-i plaquettes and level-(i+1) soft fluctuations ≤ ε_i, plus
  the complex neighbourhood of radius α_*/8), (a) the conclusions of Corollary N5-sf1 hold at level i for the branch operator
  Õ_i, with constants (γ'_i, m^{(i)}, m_1^{(i)}, S'^{(i)}, R^{(i)}, c_C^{(i)}) and the sup-norm bound N_0(|C^{(i)}|) ≤ 𝔠_∞^{(i)};
  (b) the region form of Theorem NAH1 (b) at level i (in the AX gauge of any non-wrapping box, the entries of Õ_i at depth
  ≥ D deviate from Õ_i(1, 1) by Lemma-LOC-type bounds, with constants (A_in^{(i)}, A_out^{(i)})); (c) E_i^br is holomorphic on
  the complex neighbourhood, and the N_0-Lipschitz constant of its Hessian in the chart at the lift is ≤ C_♭^{(i)}. (I_0) holds
  with E_0^br := S_W (N5-sf0, LOC, N5-an♭). Then (I_i) ⇒ (I_{i+1}) with
    ε_{i+1} ≤ ε_i/(1 + 36p_L𝔠_∞^{(i)})  (and the ε_br-, ε_H- and ε_*^{(1)}-type conditions at level i + 1),
    C_♭^{(i+1)} ≤ K_3(S_F²(𝔠_∞^{(i)})³C_♭^{(i)} + S_F𝔠_∞^{(i)}C_♭),
  and (γ'_{i+1}, m^{(i+1)}, S'^{(i+1)}, R^{(i+1)}) obtained from N5-triv at level i + 1 with δ_H^{(i+1)} ≤ γ_{i+1}/4, provided
  m^{(i+1)} ≤ Lm_1^{(i)}/2 (K_3 an absolute constant from the product rule of three-fold derivatives).
  *Proof.* Lemmas U0 and FPq are level-independent (the lift and the S4' identity; Kato and the block mean). Lemma BR1 at
  level i uses (I_i) (a) for the inverse and (c) for the Lipschitz step, with the same r = 12𝔠_∞ε and the same transversality
  argument; Lemma SC1 is algebraic (it uses only criticality, the gauge invariance of E_i^br under the level-i fluctuation
  group, which follows from BR1 (iv) at level i, and admissibility); Lemma LOC uses (I_i) (a)-(b); Theorem NAH1's proof uses
  LOC and N5-an♭ for the finite-range level-(i+1) soft, slice and fixing parts (the same functions at every level). The
  Lipschitz constant of the new Hessian: differentiate H_{i+1} = F_BB - F_BACF_AB along V, with ∂C = -C(∂O)C and the branch
  derivative ∂_VU = -CF_AB (N_0 ≤ 𝔠_∞S_F); ∂O contains the third derivatives of E_i^br (≤ C_♭^{(i)} times ∂_VU) and of the soft
  term (≤ C_♭). ∎
  **Answer to RTARGET §44 (5)-(6) and failure mode NAH1-F4.**
  - *The trivial-background gap does not shrink per level.* γ_i = γ_1 for every i ≥ 1 (N5-triv: c_E^- is i-independent); the
    only change is the one-time factor γ_1/γ_0 = 2c_E^-/(2·½) = 2c_E^- = 8.14·10⁻³ at κ ≡ 1 (level 0 has E_0 = ½||dA||², c_E = ½).
    Measured (c36 D): γ_meas(Õ_1) = 0.039712 against γ_meas(Õ_0) = 0.039849 on the same (2π/4)Z⁴ grid (both at K = (π, π, π, π)): ratio 0.9966, i.e. the true trivial-background gap does not shrink from level 0 to level 1 at all; the proven ratio 2c_E = 8·10⁻³ is entirely a loss of the bound (Lemma E-low's c_E and PG's c_1), and the proven γ_1 is 3.1·10⁸ below the measured one.
  - *The operator constants do not shrink per level,* conditionally: (γ'_i, m^{(i)}, S'^{(i)}, R^{(i)}) depend on the lower level
    only through δ_H^{(i)} ≤ γ_i/4 and the inherited decay rate Lm_1^{(i-1)} > m^{(i)}, both level-independent requirements.
  - *The background threshold shrinks, and the Lipschitz bound grows, by a fixed factor per level in this per-level form:
    NAH1-F4 OCCURS for the proven per-level induction.* ε_{i+1} ≤ ε_i/(1 + 36p_L𝔠_∞^{(i)}), and the bound for C_♭^{(i+1)} is
    S_F²(𝔠_∞^{(i)})³ times that for C_♭^{(i)}, which feeds back into ε_br. With the proven constants
    𝔠_∞ ≈ 2.0·10³⁷ at N5-w0's constants (1.3·10⁵³ at the product rule; Proposition RW-ℓ²'s sup-norm bound, the coth⁴ form gives 4·10⁵¹), so 1 + 36p_L𝔠_∞ ≈ 7.8·10³⁹ per level, so after k levels the curvature threshold is ≤ ε_0·(36p_L𝔠_∞)^{-k}. This is not a constants artefact
    that a sharper PG constant would remove: the sup-norm Newton step used here costs N_0(|C|) ≥ ||C|| = 1/λ_min(Õ) per level
    (C symmetric; Schur), which is
    ≈ 25 at the measured level-0 gap (c35 C3) and ≈ 25.2 (1/0.03971) at level 1 (c36 D), against the factor L² by which the
    own-units curvature of a smooth background actually drops per level.
  - *What uniformity needs* (named, not proven): **(BG-unif)** a multi-scale bound for the whole background map
    V_k ↦ (U_{k-1}(V_k), …, U_0(V_k)) in sup norm, with level-independent constants and own-units curvature at level j of
    order L^{-2(k-j)}×(top curvature) (the non-linear version of Theorem N2-lin + Proposition BG-b-lin, LINEAR_PACKAGE §3, whose
    linear constants C_R, C_f are uniform in k), together with the third-derivative bounds of E_j^br in the same norms (the
    non-linear (R♯) of Proposition B-NA-red). These are B-NA's background-field content [P; cf. CMP 102]. Given (BG-unif),
    the per-level steps of this section (BR1 without its Newton loss, SC1, LOC, NAH1, N5-sf1) are level-independent, and
    (NA-H_loc)_i would follow for all i with uniform constants.

- **Constants, level 0 against level 1 (RTARGET §44 A (5); κ ≡ 1, L = 3, d = 4, N = 2 where it matters).**

| | level 0 | level 1 | change |
|---|---|---|---|
| proven trivial gap γ_i (N5-coer; ×2 with γ^♯) | 1.587·10⁻⁸ | 1.29·10⁻¹⁰ | ×2c_E = 8.1·10⁻³, once (γ_i = γ_1 for all i ≥ 1) |
| measured trivial gap (c35 C3 / c36 D, Bloch, grid (2π/4)Z⁴) | 0.039849 | 0.039712 | ×0.9966 |
| measured decay of the Hessian part | finite range (d*d) | H_1 rate ≈ 1.02 per level-1 unit (c36 D3) | — |
| N_0, first moment of the trivial Õ_i rows | 25.476, 41.076 (exact) | 23.87, 50.56 (measured, torus side 12) | ×0.94, ×1.23 |
| first-moment rate (γ_i/2)/moment with the proven γ_i | 1.93·10⁻¹⁰ | 1.28·10⁻¹² (measured moment) | ×6.6·10⁻³ (the γ ratio) |
| sup-norm covariance bound 𝔠_∞ (N5-w0 constants) | 2.0·10³⁷ | — (needs N5-sf1's constants) | — |
| curvature threshold | ε_* (N5-sf0) | ≤ ε_*/(1 + 36p_L𝔠_∞) ≈ ε_*/7.8·10³⁹ (BR1), then ε_H, ε_*^{(1)} | ×≤ 1.3·10⁻⁴⁰ |
| proven gap at a background (RW-ℓ²) | ≥ γ'(1 - ε_R)/9 ≈ 6.6·10⁻¹⁰ | ≥ γ'_1(1 - ε_R)/9 ≈ 5·10⁻¹² | ×2c_E |

  Reading: the true gap does not shrink (×0.997); the proven trivial gap shrinks once, by 2c_E, and then not at all; the
  proven background threshold shrinks by ≈ 10⁻⁴⁰ in one level, and by a fixed factor per level in the per-level form
  (Proposition NAH-ind). The factor is set by the sup-norm Newton step (N_0(|C|) ≥ 1/λ_min ≈ 25 even at the true gap, times
  36p_L), not by c_1 alone.

- **Check c36** (criteria first, checks/c36_criteria.md; record checks/c36_time.txt). **A PASS** (exact lift). **B FAIL as
  pre-registered** (t = 0.05: B1-B3 hold, B2 ≤ 2.1e-7; t = 0.15: the contraction diverges; diagnostic: converges to plaquette
  angles ≈ 0.6). **C PASS** (W0-1 in exact rationals). **D PASS** (H_1 by the Schur formula reproduces c31 E's per-mode
  minimum 0.030950 and annihilates the gauge mode to 9.7e-14; γ_meas(1) = 0.039712 vs γ_meas(0) = 0.039849). Peak RSS 733 MB
  (footprint 957 MB).

- **N5 node status [S20].** OPEN, narrowed. PROVEN in addition: level 1 at curvature-small backgrounds for the critical
  branch (Theorem NAH1, Corollary N5-sf1), with E_1^br in place of E_1^NA (identification = (MIN_1) ⊂ B-NA); the background
  gap at level 0 and level 1 within a factor 18 of γ' (RW-ℓ²). Still needed: (MIN_1); levels i ≥ 2 with uniform constants,
  which Proposition NAH-ind reduces to (BG-unif) (multi-scale background regularity, B-NA's background-field part); small
  tori; explicit r_*, S_*, r_♭, S_♭; FP_U's background dependence; the cluster-expansion uses.
