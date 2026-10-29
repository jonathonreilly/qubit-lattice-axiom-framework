Reviewer model: claude-opus-5-5

# FLOW55 — the coupling flow by the trivial-background + Ward-identity route: what it must deliver, what it needs, what it bypasses

Worker file (Opus 5.5, worker role; the binding rules of REVIEW_BRIEF_55 apply). This worker writes only this file and
`checks/fl55_*`. No git. Append-only after the PRE-STATED block. Labels: **PROVEN-HERE** (complete argument written here),
**CONDITIONAL** (implication proven here, inputs named with owner file and owner's status), **ARGUED** (reasoned, hole
named), **OPEN**, **IMPORTED-standard** (a textbook fact used without re-derivation, named). Statuses quoted from other files
are those files' labels unless this file says it re-derived them. Line numbers drift; every citation carries a locating
string.

## PRE-STATED (written 2026-10-29T00:28:57Z UTC)

*Honest provenance.* Before this block I read: REVIEW_BRIEF_55 (all); BALABAN_EXTRACT (all); FLOW.md §0-§21, §23, §29-§31,
§35-§36 (COV-GI statement, step (10), Reading), §43 (Lemma GH), §44 (Proposition GH-log statement), §74 (FINE-IR), §79-§80,
§88, §99, §103 (X4)-(X5), §107 Reading, §110 (all by bounded `sed` ranges); REVIEW_FLOW_S13 (bottom line, §2, §11, §12);
CODEX_REVIEW_OLDREV (header, FLOW inventory rows); HINT55 (its pre-statement — the file is otherwise empty); RLARGE §0
((F_R), F-mono); EXISTENCE H-Bal-1 (definition block); PROOF.md L4 (L4a, L4a-flow, L4a-Π) and Theorem N5-triv (statement);
LINEAR_PACKAGE §0-§1, §6, §10; REVIEW55_NORMS (§A, r55n-F6); REVIEW55_TUNIF §L; CODEX_REVIEW_TUNIF2 (decision);
HANDOFF (critical path items 5-6, process rules). Exploratory reasoning (not written down) preceded this block: in
particular I reasoned about an exact integration of the coarse-gauge orbit of the composite kernel, about a per-step
form of the one-loop coefficient, and about a would-be O(n/κ) "gauge-orientation tadpole". **No derivation, criteria file
or script of this file existed before this time stamp.** Everything below this block was written after it.

**Conventions (fixed now, not changed later).** FLOW §0: levels k = number of coarse-graining steps (k increases toward the
IR); u_k := 1/g_k² = 2N/g_std² (FLOW Lemma F-norm); u_{k+1} = u_k − β_k; β_0^std := 2N·2b_0 = 11N²/(12π²) per log L,
b_0 = 11N/(48π²). In the brief's index j (resolution; j = K − k, finer = larger j, the PROOF L4a convention) and standard
units the same recursion reads g_{j+1}^{-2} = g_j^{-2} + 2b_0 log L + (remainder)/(2N); the brief's sign is the
resolution-index sign. "Trivial background" = the configuration U ≡ 1 (V ≡ 1) and Taylor data there.

**Targets.**
- **T1 (consumers).** State exactly what the flow statement must deliver to (a) layer 1's induction (the per-level inputs
  (SF-g)_k, (RLF-δ)_k and FLOW's Lemma F-ind), (b) RLARGE (F_R) and EXISTENCE H-Bal-1 / (F) / X-NTAF / X-ND / W-AF1 /
  PROOF L4a-flow's E8.3/E7.0 condition, (c) the non-freeness witness of HINT55 (only its pre-statement exists): coupling
  interval, recursion form, error terms, additive constant R, volume uniformity, and which consumers need the universal
  slope versus only 0 < β_- ≤ β_+.
- **T2 (anatomy of FLOW).** Locate, by section and locating string, every place where FLOW's route to (F-1)-(F-4) uses a
  non-trivial background or inverts an operator that is not gapped by the soft term (the "unconstrained" H_⊥(U)^{-1});
  and every place where it does not.
- **T3 (design).** The alternative: compute the one-step coupling recursion at the trivial background and transport it to
  general small backgrounds with gauge Ward identities. Deliver: (a) the trivial-background definition and formula of the
  one-step coefficient; (b) the jet Ward identities at the trivial point and the statement that the marginal (dimension-4)
  parts of the cubic and quartic Taylor coefficients of a gauge-invariant, B_4-covariant local functional are fixed by its
  quadratic coefficient β (this is the "transport"); (c) exactly where a non-trivial background re-enters and which
  operator must be inverted there; (d) whether LINEAR_PACKAGE, Theorem N1-15 and (T-UNIF) supply what (a)-(c) need.
- **T4 (prove).** (a) A per-step reduction of FLOW's (F-1) to named trivial-background inputs. (b) An exact rewriting of the
  composite one-loop functional by integrating the level-n (coarse) gauge orbit of the composite kernel exactly, and its
  one-loop consequence at every background near 1, with the off-shell remainder identified and the part of it that carries
  an explicit n-growing factor shown to contribute nothing to β. (c) The leading coefficient: re-verify, by exact
  arithmetic, the chain that gives β_0^std = 2N·2b_0 log L per step from the soft scheme's one-loop integrand at the trivial
  background, and state precisely where κ enters and why it cannot change the coefficient of log L (given named inputs).
  (d) The remainder bound, CONDITIONAL on named inputs.
- **T5 (decide).** Does the route bypass FLOW's wall ((T-a1-M) = (T-b), the fine background-dependent inverse
  H_⊥(U)^{-1}; with (T-c)) entirely, partly, or not at all? Give the precise residue.

**What would count as a refutation of my own claims (fixed now).**
- R-1. Of "(F-2)-(F-4) never use a non-trivial background except through (SF-g)'s polydisc": any step in FLOW's proofs of
  Proposition F-rem, Theorem F-flow, Theorem F-tune or Lemma F-ind that inverts a background-dependent operator or evaluates
  a quantity at a non-trivial background other than through the hypothesis (SF-g).
- R-2. Of the per-step reduction: b_k depending on data other than the trivial-point jets of the tree tower of order ≤ 4 and
  fixed kernel data; or the one-step slice inverse at the trivial background failing to be uniform in k.
- R-3. Of the jet Ward identities / marginal-jet uniqueness: a nonzero hypercubic-covariant, Bose-symmetric or
  Bose-antisymmetric, degree-1 cubic symbol that is transverse on a leg (check fl55_4 finds dimension > 0), or an error in
  the BCH derivation exhibited by an explicit counterexample.
- R-4. Of the exact coarse-gauge orbit factorization: a failure of the covariance K_comp(V^h, U^g) = K_comp(V, U)
  (h = g at the level-n sites) for the soft chain, or of the product structure of the fine gauge group used.
- R-5. Of the tadpole lemma: the gauge-covariance identity (the transported h-covariance contracted with the second-order
  orbit commutator vanishes on every pure-gauge background) failing in an exact instance (check fl55_3), or its first-order
  form failing to annihilate gradients; or a kernel-decay estimate it uses being false.
- R-6. Of the leading-coefficient arithmetic: the Feynman-form ratio not equal to 11, or the 1/22 : 21/22 split, the 2N
  conversion, or the S³ angular averages failing in exact arithmetic (check fl55_1); or the value-function jet formulas
  failing on an exact polynomial example (check fl55_2).
- R-7. Of the decision: an item I classify as trivial-background ((T-a1)/(T-b) at orders ≤ 2 in the plane-wave amplitude)
  that provably needs H_⊥(U)^{-1} at a background of finite size for a reason other than the Cauchy-estimate technique
  FLOW chose; or a non-trivial-background object needed by the route that I failed to list.

**Checks planned (criteria files written before any script; exact rational / symbolic arithmetic in plain python —
`fractions`, `sympy` — no numpy, no floats in any verdict; nice 10; each with a designed-FAIL control).**
fl55_1 (leading-coefficient chain), fl55_2 (value-function jets), fl55_3 (gauge-covariance step of the tadpole lemma),
fl55_4 (marginal cubic jet uniqueness). Ids may be added; none removed.

---

# FINDINGS (appended from 2026-10-29T00:43Z, after the PRE-STATED block and after the four checks ran)

Check record (criteria files written 00:30-00:32Z, before any script; one correction to fl55_4_criteria J3, a sign
convention, made and logged in that file BEFORE any fl55_4 script existed; fl55_1.py had one edit (the real-part extraction
in B1) before its first and only run). Exact arithmetic only; nice 10; no lock needed (exact plain-python work).
| id | what | result |
|---|---|---|
| fl55_1 | leading-coefficient chain (a_2 ratio 11 = 12 − 1 for SU(2), SU(3); 2N·2b_0; 1/22 : 21/22; S³ averages; scalar channel 1/(24π²)) | 13/13 PASS, 4/4 controls fire (1.1 s, 66 MB) |
| fl55_2 | value-function jets: D³W = D³f[ζ³]; D⁴W = D⁴f[ζ⁴] − 3cᵀA⁻¹c | 4/4 PASS (E0, E3, E4 + overall), 2/2 controls fire (1.3 s) |
| fl55_3 | h-tadpole covariance: transported covariance kills the tadpole on pure gauge (exact zero, 18/18 links); first-order form annihilates gradients | 4/4 PASS, 2/2 controls fire (untransported tadpole nonzero on 18/18 links) (0.2 s) |
| fl55_4 | marginal cubic jet: {hypercubic, Bose-(anti)symmetric, leg-transverse, degree 1} = {0}; V^YM the unique particular solution | 3/3 PASS, 2/2 controls fire; dim{(H),(S−)} = dim{(H),(S+)} = 1 (0.3 s) |
Outputs: checks/fl55_{1,2,3,4}_out.txt (unaltered), *_err.txt (time/memory only).

## 0. Headline

1. **What every consumer needs (§1).** (i) A per-level statement at level k from data on [0, k] only: the one-step
   recursion u_{k+1} = u_k − b_k − ρ_k with |ρ_k| ≤ C_ρg_k² whenever g_0, …, g_k ∈ (0, γ_0], and the cumulative bracket
   (F_R)_{[0,k+1]}; (ii) an explicit β_- > 0 fixed before C_ρ and γ (FLOW Lemma F-ind's order) — RLARGE's n_♯, n_H, LF-n's
   convergence criterion and HINT55's sign all read β_-; (iii) explicit β_+ and R (they enter as e^{aR} factors; no consumer
   needs R = 0); (iv) volume uniformity (delivered by defining β in infinite volume, FLOW Def F-g + (SF-∞)); (v) the tuning
   theorem in H-Bal-1 form. The universal value β_0^std log L is needed only by W-AF1 / X-NTAF-sharp and by HINT55's
   leading-order value; PROOF's E8.3/E7.0 needs only β_+ < 6.1·β_0^std. **But (ii) itself — asymptotic freedom — needs
   b_∞ > 0, which cannot be had without computing the one-loop slope; no consumer can avoid the value problem.**
2. **FLOW's wall is confined to (UNIV-1L), and it is created by two choices of FLOW's, not by the soft scheme (§2, Lemma
   W-loc).** FLOW's (F-2)-(F-4) are already "trivial background + Cauchy on a polydisc" (Balaban's M6 + M4 in the extract's
   numbering) and invert no unconstrained operator. Inside (UNIV-1L) a non-trivial background enters only because
   **(C1)** COV-GI / Lemma GH / GP-L / T-tel need H_Wilson·D_U = 0, which fails at the off-shell tower points near U = 1 (FLOW
   §79's (DEF)), so FLOW moved the definition of the coefficient to the constant Cartan flux U_f; and the unconstrained
   H_⊥(U)^{-1} enters only because **(C2)** FLOW's Woodbury/T-split representation splits the fine Wilson Hessian off the soft IR
   term. At the orders FLOW needs (≤ 2 in the plane-wave amplitude), (T-a1-M) and (T-b) are Taylor data at U = 1; only (T-c)
   (plane wave ↔ constant flux) is a genuinely non-trivial-background statement, and it exists only because of (C1).
3. **New exact identity: integrate the coarse-gauge orbit (§5).** Averaging the composite kernel over the level-n gauge group
   is exact (covariance + Haar), and it makes the fine exponent 𝒯_0 + Ψ_min fully gauge invariant, so its Hessian H^♮ at the
   tower is **exactly transverse at every background** — the hypothesis that forced FLOW onto U_f now holds identically.
   FLOW's regrouping Γ = G_⊥ + G_gh (Lemma GH) then holds off-shell with one extra term, the h-tadpole 𝔗′, and the n-growing
   coarse-gauge block of 𝒞_n (⟨v, 𝒞_nv⟩ ≥ (n/κ)|v|², COV-str (iv)) cancels by linear algebra alone. The h-tadpole is the only
   off-shell term with an explicit n/κ factor; evaluated with the trivial-background covariance it would shift u_n by an
   amount ∝ n/κ (a κ-dependent slope — failure mode FL-F2); evaluated with the correctly transported covariance it vanishes on
   every pure-gauge background exactly (fl55_3) and has β = 0 (Lemma K̄-tad). **Result: B_n = −β[G^♮_⊥,n] − β[G_gh,n] at the
   trivial background, for every n, with no critical-background hypothesis; β[G_gh,n] = −(1/22)β_0^std n log L exactly; hence
   (UNIV-1L) ⟺ (UIR^♮): sup_n|β[G^♮_⊥,n] + (21/22)β_0^std n log L| < ∞.**
4. **The Ward transport (§3).** Jet Ward identities at the trivial point (orders 2, 3, 4, from BCH) plus an exact finite
   classification (fl55_4) show: the marginal cubic and quartic Taylor parts of any gauge-invariant, B_4-covariant local
   functional F are β[F] times those of the Wilson action (Proposition JET-MARG). So the single trivial-background number β
   determines the whole marginal part. A non-trivial background re-enters only through the polydisc of (SF-g), where the
   operator to invert is the soft-constrained one-step covariance (gapped), never H_⊥(U)^{-1}.
5. **Per-step form (§4).** b_k is a one-step, gapped, trivial-point number b_k = 𝔅(J_k) of the tree jets
   J_k = (D², D³, D⁴)𝒯_k(1) (no second-order tower: Lemma ENV + U-tad). Given (TC) — k-uniform weighted bounds and geometric
   convergence of J_k, OPEN (D²: F-depth PROVEN; D³: N1-15 + T-UNIF give a k- and T-uniform but unweighted bound, CONFIRMED
   conditional; D⁴: nothing) — b_k → b_∞ and FLOW's (F-1) holds with β_0′ := b_∞/log L and an explicit R. **The value
   b_∞ = β_0^std log L is a multi-scale statement; no single one-step Gaussian integral at fixed L delivers it.**
6. **Leading coefficient (§6).** fl55_1 re-verifies the chain exactly. κ cannot change the coefficient of n log L: in the K̄
   form the only κ-dependent n-growing objects (the coarse-gauge block and its tadpole) cancel exactly or have β = 0, and κ
   enters what remains only through the n-uniform transverse block Π, i.e. through the IR constants of FLOW's residue lemma
   U-res. Conditional on (UIR^♮).
7. **Decision (§8): PARTLY.** The route removes every non-trivial-background object from FLOW's wall — U_f, the
   Nielsen-Olesen mode, (T-c), COV-GI-∞ / (L-loc2) on 𝒦_n / Lemma N-f, (DEF)/(GP) — and the unconstrained H_⊥(U)^{-1} never
   appears (the only fine inverse is the gapped (H^♮_⊥)^{-1}). It does NOT remove the trivial-background vector IR estimate
   (UIR^♮), which is FLOW's own crux ((V-IR) in the form (Q1)(d)) restated at U = 1. The remainder half (F-2) is unchanged:
   conditional on layer 1's polydisc (SF-g), the one place a non-trivial background is genuinely needed — through the
   soft-constrained one-step covariance at complex small backgrounds (N5-sf0 at level 0 PROVEN; levels ≥ 1 reduced to
   (NA-H_loc), OPEN).

## 1. T1 — what the flow statement must deliver to its consumers

Conventions of §PRE-STATED. "R" is FLOW's additive constant in (F_R). Quotes are from the files as on disk at 00:00-00:30Z.

| consumer (file, locating string) | statement consumed | needs from the flow |
|---|---|---|
| Layer-1 induction: FLOW §4 "(RLF-δ)_k: along the chain's own sequence (Def F-g), if g_0, …, g_k ∈ (0, γ_0] and (F_R) holds on [0, k]"; RLARGE §0 "(RLF-δ)_k … Derived at level k from data on levels [0, k] only, never from g_K"; FLOW §9 Lemma F-ind | the per-level inputs (SF-g)_k, (RLF-δ)_k at level k use only g_0, …, g_k ≤ γ_0 and (F_R)_{[0,k]} | a ONE-STEP statement at level k (u_{k+1} − u_k = −b_k − ρ_k, |ρ_k| ≤ C_ρg_k², from data on [0, k]); constants fixed in F-ind's order: β_- (from the one-loop data alone), R, then C_ρ (layer-1 constants may depend on β_-, R), then γ := min{γ_0, (β_0′log L/(2C_ρ))^{1/2}}; coupling interval (0, γ] ⊂ (0, γ_0] with γ_0 layer 1's threshold |
| RLARGE §0 "(F_R)_{[0,k]}: β_-(m − j)log L − R ≤ u_j − u_m ≤ β_+(m − j)log L + R"; Lemma F-mono "(i) u_k − u_{k+1} ≥ β_- log L − R"; "n_♯ := ⌊4/(a_♯β_-)⌋"; "n_H := ⌊(4 + c_B)/(aβ_-)⌋" | two-sided cumulative bracket; one-step lower bound; slopes | explicit 0 < β_- ≤ β_+, explicit R; R enters only as e^{aR} factors and g_k² ≤ 2g_{k+1}² for g_{k+1}² ≤ 1/(2R) |
| EXISTENCE H-Bal-1 "There are γ > 0, g_1 > 0 and 0 < β ≤ β′ such that for every g ∈ (0, g_1] and every K ≥ 0 there is a bare coupling g_0(ε, g)…"; "Volume uniformity … independent of the torus side M" | the tuned, two-sided, M-uniform flow (R = 0 form) | FLOW Theorem F-tune gives it with ±R; FLOW §19A records that every EXISTENCE use tolerates R; M-uniformity from Def F-g's infinite-volume β + (SF-∞) |
| EXISTENCE X-ND / X-MONTEL "g_{m,K} in a compact subinterval of (0, γ]", "g_min the K-uniform lower bound of H-Bal-1" | K-uniform lower bound on g_{m,K} | the upper half of the bracket (β_+, R) |
| EXISTENCE X-NTAF-sharp, wall W-AF1 "g_m² ~ 1/(2b_0 m log L)" | the universal slope | β_± → β_0^std as γ → 0, i.e. the VALUE b_∞ = β_0^std log L |
| PROOF L4 "They stay conditional on L4a-flow with β′ < 6.1·2b_0" (E8.3/E7.0) | slope upper bound | β_+ < 6.1·β_0^std (u-units) — a bound, not the exact value |
| HINT55 (pre-statement only; the file has no findings yet): "|W(ω_{a,R})| ≥ c > 0 at fixed renormalized coupling uniformly in volume", W_GF := f(t₂) − f(t₁) | the running between two fixed physical scales at a fixed renormalised coupling | F-tune (fixed renormalised coupling), a lower bound u_j − u_{j+m} ≥ β_-m log L − R > 0 between the two scales (so m > R/(β_- log L)), volume uniformity; the universal b_0 only for its "leading-order YM value" (its T3) |

**Summary of T1.** The flow statement must be FLOW's Theorems F-flow + F-tune in the form: there are γ ∈ (0, γ_0], explicit
β_- > 0, β_+ ≥ β_-, R ≥ 0, depending only on (N, L, κ) and layer-1 constants fixed after β_- and R, such that along the chain's
own sequence (i) one-step: |u_k − u_{k+1} − b_k| ≤ C_ρg_k² (+|δβ_k| ≤ g_k⁶) whenever g_0..g_k ≤ γ, (ii) cumulative (F_R), (iii)
tuning, (iv) all of it torus-independent. The sharp form (β_± → β_0^std) is extra. **Both forms need the per-step one-loop
numbers b_k to have a positive asymptotic slope with a bounded cumulative deviation — that is exactly (UNIV-1L), or (TC) plus
a value statement (§4).**

## 2. T2 — anatomy of FLOW: where a non-trivial background, and where an unconstrained inverse, enters

"Constrained" = gapped by the soft term (κQ^TQ, M^TΠM, 𝒞_n^{-1}); "unconstrained" = the bare Wilson Hessian (H, H_⊥, K_F)
inverted by itself. Every row was located by string in FLOW.md as on disk (md5 not taken; 539577 B).

| FLOW item (locating string) | background used | inverse used | role |
|---|---|---|---|
| Def F-g "u_{k+1} := β[S_{k+1}]"; β = "Σ_zz_1z_2Π^F_12(z), Π^F the Hessian at V = 1" | trivial (V = 1), infinite volume | none | the definition of the coupling |
| Lemma F-Π "(ii) Σ_z|z_1z_2||Π^F_12(z)| ≤ C_Π‖F‖_{κ_p}" | the polydisc D_α(X) (complex backgrounds within α of 1) — through the HYPOTHESIS of analyticity | none (Cauchy at 0) | remainder bound |
| Prop. F-rem "given (SF-g)_k and (RLF-δ)" | inside (SF-g) only; F-ren (ii) is a trivial-point alias argument | none | (F-2) |
| Theorems F-flow, F-tune, Lemma F-ind, Cor. F-ll | none (arithmetic, (SF-cont), (SF-∞)) | none | (F-3), (F-4) |
| F-tree, F-bg, F-ren, F-depth, F-tel, Lemma TOW (§31) | trivial point | one-step slice operator H_k + κQ^TQ on Σ_lin — constrained, gap uniform in k (N5-triv) | b_k, B_n = Σb_k |
| U-tad, U-dec, U-pair, U-red, U-loc′, U-res, U-Tay, U-cov-IR(′) (§16-§24) | trivial point | composite slice operator O_n ≥ γ_n > 0 at each n ((I4)) — constrained | reduction of B_n to a fine functional with a covariant IR term |
| COV-GI (§36) "uses only MJ = D …, HJ = 0, (S) and (N)"; Reading (b) "for β the identity is needed exactly at constant Cartan curvature" | U_f (critical) | H + M^TΠM — constrained | removes the n-growing coarse-gauge block |
| Lemma GH (§43) "Let U_0 be a critical point of 𝒯_0"; GH-log (§44); G-mag; Lemma N-f; COV-GI-∞; (L-loc2) "for all U ∈ 𝒦_n" | U_f, and the class 𝒦_n ∋ U_f | constrained | ghost group, its f² coefficient, the infinite-volume f² density |
| §79 "(DEF), the wall" → "[RFL10-fix S10-2] (DEF) is RETIRED … E_U ≡ 0 on the whole critical family U_f … that DEFINES c^tot_n := [f²]total_n(U_f)" | moves the target from U = 1 to U_f | — | **choice (C1)** |
| §79 caution "X_U ≥ 𝒞_n FAILS at U_f, because K_F(U_f) has the Nielsen-Olesen negative mode" | U_f | K_F^{-1} — unconstrained | the NO-mode caveat |
| §85 GP-L "At every critical U at which Δ_U, H_⊥ (on ker D_U^*) and Y_U are invertible … K_F^{-1} = H_⊥^{-1}P_⊥ + D_UΔ_U^{-2}D_U^*"; §96 T-tel "log det_⊥Ỹ^{(0)} = −log det_⊥H_⊥" | critical U (U_f) | **H_⊥^{-1} — unconstrained** | **choice (C2)**: the Woodbury/T-split representation |
| §99/§103 (T-a1), (T-a2) "first- and second-order plane-wave vertex symbols" | orders ≤ 2 in the amplitude ⇒ Taylor data at U = 1; FLOW proves them by Cauchy estimates on "the half-radius polydisc" (a technique) | constrained (𝒞-part); P_k(U)'s massless level poles | T-split vertex data |
| (T-a1-M) §103 (X5) "The M-part P_nM_UH_⊥(U)^{-1}P_⊥M_U^*P_n … needs the fine H_⊥(U)^{-1} expansion" | at orders ≤ 2: derivatives at U = 1 | H_⊥(1)^{-1} = (d^*d|_{ker d^*})^{-1} — unconstrained, massless | exists only inside (C2) |
| (T-b) §99 "needs the plane-wave density of the gapped fine operator H_⊥ + M̃^T(P_n𝒞_nP_n)^{-1}M̃" | plane-wave density = Taylor data at U = 1 | constrained ("gapped") | the T-split IR identity |
| (T-c) §99 "T-split exchange at U_f (plane wave ↔ constant field for the steps Φ^T_k, the NO mode in Ỹ^{(0)} …)" | **U_f, at finite flux** | H_⊥(U_f)^{-1} via Woodbury | exists only because of (C1) |

**Lemma W-loc (localisation of FLOW's wall): PROVEN-HERE (by inspection of the proofs cited above; refutable by exhibiting a
use I missed — R-1, R-7).** (a) FLOW's (F-2), (F-3), (F-4) use a non-trivial background only through the hypotheses (SF-g)
(polydisc analyticity of the step output), (SF-cont), (SF-∞), and invert no operator. (b) In FLOW's proof of (F-1) =
(UNIV-1L), every object is trivial-point Taylor data of constrained operators EXCEPT those introduced by (C1) [the target
c^tot_n defined at the critical constant Cartan flux U_f, forced because COV-GI/GH/GP-L/T-tel need H_Wilson D_U = 0, which
fails off-shell: §79 (DEF)] and (C2) [the Woodbury split that isolates the unconstrained H_⊥]. (c) In particular (T-a1-M) and
(T-b), at the orders FLOW states them (≤ 2 in the plane-wave amplitude), are statements about Taylor coefficients at U = 1;
the only statement that needs H_⊥(U)^{-1} at a background of finite size is (T-c), and the Nielsen-Olesen mode lives only
there. **So HANDOFF item 6's description "the fine background-dependent inverse H_⊥(U)^{-1}" should read: "(T-c) (finite-flux
U_f, with the NO mode) plus the U = 1 Taylor data (T-a1-M), (T-b) of FLOW's T-split; both exist because of the choices (C1),
(C2)."** (I agree with REVIEW_FLOW_S13 §12 that this is FLOW's biggest live wall; I disagree with its sentence "a resolvent on
the fine lattice at a non-trivial background, a genuinely new analytic object" as a description of (T-a1-M) at orders ≤ 2:
there it is the Taylor jet at U = 1 of H_⊥(U)^{-1}P_⊥(U), whose difficulty is the massless pole structure of H_⊥(1)^{-1} — the
fine-lattice analogue of what Lemma P-poles already did for the level projector P_k(U).)

## 3. T3 — the trivial-background + Ward-identity route (design), and the Ward transport proven

### 3.1 The coupling is already defined at the trivial background
FLOW's Def F-g sets u_{k+1} := β[S_{k+1}], β the coefficient of the transverse p² term of the Hessian at V = 1 (L4a-Π,
PROVEN-HERE in PROOF, check c17(A)). This is the structure of CMP 109's (1.22)/(5.37) (BALABAN_EXTRACT §5 M6). So "compute
at the trivial background" is not a new definition; it is the instruction to evaluate b_k = −β[Γ_k] and B_n = −β[Γ_{0→n}]
**directly at V = 1**, never via an f² coefficient at a finite flux. What Ward identities must add: (a) transversality of
the 2-point function (L4a-Π (G); PROVEN); (b) that the marginal parts of the 3- and 4-point Taylor coefficients are fixed by
the same β — so the renormalised remainder S_{k+1} − u_{k+1}𝒯_{k+1} carries NO marginal part at orders 2, 3, 4 (Proposition
JET-MARG below, new); (c) Cauchy estimates on a polydisc for orders ≥ 5 (Lemma F-Π-type; this is where a non-trivial
background re-enters, §3.5).

### 3.2 Lemma WARD-J (jet Ward identities at the trivial point): PROVEN-HERE
*Setting.* F real-analytic near 1 in the link variables, gauge invariant (F(U^g) = F(U), U^g_b = g_xU_bg_y^{-1} for
b = (x, y)), Taylor coefficients F_m := D^mF(1) (symmetric m-linear) in the exponential chart U_b = e^{X_b}. ψ(z) := z/(1 − e^{−z})
= 1 + z/2 + z²/12 + O(z⁴). Write (dλ)_b := λ_y − λ_x and λ̄_b := λ_x + λ_y.
*Claim.* (W1) F_1 = 0; (W2) F_2[X, dλ] = 0; (W3) F_3[X, X, dλ] = −F_2[X, [X, λ̄]];
(W4) F_4[X, X, X, dλ] = −(3/2)F_3[X, X, [X, λ̄]] − ½F_2[X, [X, [X, dλ]]], for all X, λ (with [X, λ̄]_b := [X_b, λ̄_b]).
*Proof.* Linear BCH: log(e^Xe^{tB}) = X + tψ(ad_X)B + O(t²) and log(e^{tA}e^X) = X + tψ(−ad_X)A + O(t²) (both read off from
log(e^Xe^Y) = X + Y + ½[X, Y] + (1/12)([X,[X,Y]] + [Y,[Y,X]]) + …). Hence, for g = e^{tλ},
log(e^{tλ_x}e^{X_b}e^{−tλ_y}) = X_b + tΘ_b + O(t²), Θ_b = ψ(−ad_{X_b})λ_x − ψ(ad_{X_b})λ_y = −(dλ)_b − ½[X_b, λ̄_b] −
(1/12)[X_b, [X_b, (dλ)_b]] + O(X³). Invariance gives 0 = ∂_tF(e^{X+tΘ})|_0 = Σ_{m≥1}F_m[X^{m−1}, Θ]/(m − 1)!. Degree 0: F_1[dλ] = 0
(and F_1 = 0 outright by colour invariance, FLOW Lemma U-tad (i)). Degree 1: −F_2[X, dλ] = 0. Degree 2: −½F_3[X, X, dλ] −
½F_2[X, [X, λ̄]] = 0. Degree 3: −(1/6)F_4[X³, dλ] − ¼F_3[X, X, [X, λ̄]] − (1/12)F_2[X, [X, [X, dλ]]] = 0. Multiply out. ∎
(The signs depend on the side conventions; Proposition JET-MARG below uses only the STRUCTURE "F_m on a longitudinal leg =
a commutator expression in F_{m−1}, F_{m−2}", not the signs.)

### 3.3 Proposition JET-MARG (the marginal jets are fixed by β): PROVEN-HERE, with check fl55_4
*Setting.* d = 4. F as in §3.2, translation invariant, B_4-covariant (signed permutations of the axes), with exponentially
local Taylor kernels F_2, F_3, F_4 (so their symbols are analytic in the momenta). Call the *marginal part* of F_m the part of
its symbol of total momentum degree 4 − m (degree 2 for m = 2, 1 for m = 3, 0 for m = 4), i.e. the dimension-4 part.
*Claim.* The marginal parts of F_2, F_3, F_4 equal β[F] times those of the Wilson action Σ_ps(U_p).
*Proof.* m = 2 is L4a-Π. Put G := F − β[F]Σ_ps(U_p); G is gauge invariant, translation invariant, B_4-covariant, with
β[G] = 0, so its F_2-symbol is O(p⁴) (L4a-Π). (m = 3.) By Ad-invariance the colour structure of G_3 is f^{abc}T + d^{abc}S
(the invariant 3-tensors on su(N); d absent for N = 2). (W3) for G: the right side G_2[X, [X, λ̄]] has total momentum degree
≥ 4 (G_2's symbol is O(p⁴) in the momentum of its legs), while the left side's degree-2 part is the degree-1 part of G_3
contracted on one leg with the momentum of λ. Hence the degree-1 parts T^{(1)}, S^{(1)} satisfy the HOMOGENEOUS transversality
Σ_μp_μT^{(1)}_{μνρ}(p, q) ≡ 0 (and likewise S^{(1)}), are hypercubic covariant (B_4-covariance of F) and Bose antisymmetric
(T, since f is) resp. symmetric (S). Check fl55_4 computes, in exact arithmetic over the 512 coefficients of a general
degree-1 cubic symbol, that this space is {0} in both cases (J1, J2 PASS), and that without transversality it is
one-dimensional, spanned by V^{YM} (J4, J-c1). So G_3's marginal part is 0. (m = 4.) G_3's symbol is odd (point inversion) with
zero degree-1 part, hence O(p³); in (W4) for G the right side has degree ≥ 3, the left side's degree-1 part is the degree-0
tensor V := G_4^{(0)} contracted with the momentum of λ on one leg. So Σ_σV_{μνρσ}p_σ = 0 for all p, i.e. V = 0 (V is
momentum-independent; colour structure irrelevant). ∎
*What fl55_4 also shows.* V^{YM}_{μνρ}(p,q,r) = δ_μν(p − q)_ρ + δ_νρ(q − r)_μ + δ_ρμ(r − p)_ν obeys the inhomogeneous identity
Σ_μp_μV^{YM}_{μνρ} = (r²δ_νρ − r_νr_ρ) − (q²δ_νρ − q_νq_ρ) (J3), the continuum form of (W3) with the transverse quadratic form
(the overall sign is the convention of §3.2). The hypercubic-only structure δ_{μνρ}k_μ ("all indices equal") is excluded by
Bose symmetry (it would need the sign or trivial representation of S_3 inside the 2-dimensional span{p, q, r}/(p + q + r)),
which is why the hypercubic and O(4) answers coincide (J4: dimension 1, not 2).
*Corollary TRANSPORT: PROVEN-HERE (given the setting).* For the renormalised remainder 𝒮^ren_{k+1} := S_{k+1} − u_{k+1}𝒯_{k+1}
(β = 0 by Def F-g, β[𝒯_{k+1}] = 1 by F-tree), the marginal parts of its Taylor coefficients of orders 2, 3, 4 at the trivial
point vanish; if 𝒮^ren_{k+1} = Σ_XE(X) with each E(X) analytic on the polydisc D_α(X) and |E(X)| ≤ ‖E‖e^{−κ_pd(X)} there, the
order-≥5 Taylor remainder of E(X) at a real background with all |X_b| ≤ δα (δ < 1) is ≤ ‖E‖e^{−κ_pd(X)}δ⁵/(1 − δ) (one-variable
Cauchy along the ray). **This is the transport: the one coupling β determines the whole marginal part at every small
background; the rest is irrelevant (orders 2-4) or controlled by the polydisc (orders ≥ 5).** It is CMP 109's mechanism (M6
+ M4 of BALABAN_EXTRACT), here proven for the soft scheme's jets at orders ≤ 4. It is not a proof of the irrelevance
GAIN per subsequent step (L^{-2} per level), which is layer 1's (F-ren handles the quadratic level).

### 3.4 Where a non-trivial background re-enters, and which operator must be inverted there
Only in (SF-g) (FLOW §4): "Ẽ_k are the renormalised level-k polymers … evaluated at the tree background; E^{≥2}_k are level-(k+1)
polymers as in Lemma F-Π with ‖E^{≥2}_k‖_{κ_p} ≤ E_2g_k²". Lemma F-Π needs each polymer analytic on D_α(X), i.e. at complex
backgrounds within α of 1 on X. To prove (SF-g) one must Gaussian-integrate one RG step at such backgrounds, i.e. invert the
**one-step soft-constrained fluctuation operator** Õ_k(U, V) := slice compression of Hess_U(𝒯_k + κΣ_ck̃(V_c, M̄_c(·)))(U*)
(+ the slice term), gapped by κQ^TQ, with a random-walk expansion and complex weakening; and one needs the tree tower 𝒯_k
analytic on a k-uniform polydisc ((SF-bg), BFT-0 in analytic form). This is PROOF's node N5 and BFT, not FLOW's:
N5-triv (all levels, trivial background) CONFIRMED (REVIEW_S18_S19); Theorem RW (random walk, complex s-weakening at the
trivial background) and N5-sf0 (level 0 at curvature-small complex backgrounds: "gap, ℓ², ℓ¹, decay, analyticity on a complex
neighbourhood") PROVEN; levels i ≥ 1 at non-trivial backgrounds reduced to (NA-H_loc), OPEN, with per-level shrinking
thresholds ("NAH1-F4 OCCURS for the proven per-level induction", PROOF [S20]). **The operator is the constrained one; nowhere
does the Ward route need H_⊥(U)^{-1}.** (This matches BALABAN_EXTRACT §7.4, "Balaban always inverts the constrained
operator", which the extract itself flags as its inference from CMP 109's uses.)

### 3.5 What the lane's existing results supply
| needed by the route | supplied by | status (owner's / reviewer's) | gap |
|---|---|---|---|
| k-uniform gap and locality of the one-step slice inverse at U = 1 (the per-step propagator) | LINEAR_PACKAGE Prop. 6.2 (PG), Prop. 6.4; PROOF Theorem N5-triv ("uniformly in i ≥ 0, k ≥ 1 and T ≥ 2"; γ_i = γ_1 for i ≥ 1) | CONFIRMED (REVIEW_S18_S19; LINEAR_PACKAGE reviews) | none for this use (constants are crude: γ_i ≈ 1.3·10⁻¹⁰) |
| quadratic tree jet D²𝒯_k(1) bounded and convergent | FLOW Lemma F-depth (rate ≤ L^{-2}, symbol sup norm) | PROVEN, CONFIRMED (REVIEW_FLOW_S1_S2) | an exponentially weighted version (needed for second moments) is not written |
| cubic tree jet D³𝒯_k(1) k-uniform | Theorem N1-15 (+ NQ-1, + T-UNIF TU-5/TU-6): "N3(D³E_k^br(1)) ≤ 𝔚·L^{(d−4)k} + …", uniform in k and T | CONDITIONAL; CONFIRMED as conditional (REVIEW55_NORMS r55n-A4; REVIEW55_TUNIF (T-UNIF); CODEX_REVIEW_TUNIF2 "CONFIRMED as a conditional theorem") | N3 is an unweighted absolute row sum — no decay, so no second moments; a bound, not convergence; NORMS's E_k^br and FLOW's 𝒯_k are the same composite value function at the trivial point up to HIST's φ-vs-k̃ bookkeeping (FLOW §3.1 [RFL-fix]: derivatives of order ≤ 5 at 1 agree) — I did not re-verify NORMS's normalisation of the soft term (φ̂ = ½|ρ|² + O(ρ⁴), κ_j) against FLOW's κk̃ |
| quartic tree jet D⁴𝒯_k(1) (with the exchange term) | nothing | OPEN | the whole item |
| polydisc analyticity of the step output ((SF-g)) | N5-sf0 at level 0 only | PROVEN at level 0; OPEN at levels ≥ 1 | layer-1 paper-scale (N5, BFT-0 analytic, (N-bg)) |
**So LINEAR_PACKAGE, N1-15 and T-uniformity supply the trivial-background propagator and part of the cubic jet; they do not
supply the weighted/convergent jets the per-step value needs ((TC), §4), nor anything at a non-trivial background.**

## 4. T4(a) — the per-step reduction of (F-1)

### 4.1 Lemma ENV (value-function jets): PROVEN-HERE, with check fl55_2
*Setting.* f(U, V) C⁴ near (0, 0) on a finite-dimensional slice × data space, f_U(0, 0) = 0, A := f_UU(0, 0) invertible, U*(V)
the C³ critical family with U*(0) = 0, W(V) := f(U*(V), V), ζv := (DU*(0)v, v), c(v) := ∂_U(D³f(0)[ζv, ζv, ·]).
*Claim.* D²W(0)[v, v] = D²f[ζv, ζv]; D³W(0)[v³] = D³f(0)[(ζv)³]; D⁴W(0)[v⁴] = D⁴f(0)[(ζv)⁴] − 3c(v)ᵀA^{-1}c(v).
*Proof.* Along V = tv put z(t) := (U*(tv), tv), w(t) := f(z(t)). Differentiating f_U(z(t)) ≡ 0 gives D²f(z(t))[(h, 0), z′(t)] = 0
for all h, t (⋆). w′ = f_V[v]; w″ = D²f[z′, z′] + f_U[u″] = D²f[z′, z′]; w‴ = D³f[z′³] + 2D²f[(u″, 0), z′] = D³f[z′³] by (⋆), for all
t; w⁗(0) = D⁴f[z′⁴] + 3D³f[(u″(0), 0), z′, z′]; differentiating (⋆) once more at t = 0, D³f[(h, 0), z′, z′] + D²f[(h, 0), z″] = 0,
i.e. Au″(0) = −c(v). ∎ (The cubic statement is REVIEW55_NORMS r55n-A1's; both are FLOW TOW (5)'s formulas. fl55_2: E0, E3, E4
exact on a random rational quartic polynomial for five directions; dropping ζ's U-part or the exchange term fails.)

### 4.2 The per-step coefficient as a function of trivial-point jets
Apply Lemma ENV to FLOW §31's one-step problem F_k(U; V) = 𝒯_k(U) + κΣ_ck̃(V_c, M̄_c(U)) on the slice Σ_lin (TOW (2)): with
J_k := (D²𝒯_k(1), D³𝒯_k(1), D⁴𝒯_k(1)) and the k-independent kernel jets K := (∇^{≤4} of κΣk̃∘(id, M̄), D²(log𝒩′_1∘P∘M̄)) at the
trivial point (level units, uniform κ), the tower recursion is J_{k+1} = 𝔗(J_k; K) with D²𝒯_{k+1} = D²F_k[ζ²], D³𝒯_{k+1} =
D³F_k[ζ³], D⁴𝒯_{k+1} = D⁴F_k[ζ⁴] − 3cᵀC_k^{ph}c, ζ = (DX*, 1), DX* = −C_k^{ph}∂_V∇F_k, C_k^{ph} the slice inverse of
H_k + κQ^TQ (TOW (1)); and, from TOW (6),
  Hess Γ_k(1)[v, v] = ½tr(C_k^{ph}∇⁴F_k[(ζv)², ·, ·]) − ½tr(C_k^{ph}∇³F_k[ζv, ·, ·]C_k^{ph}∇³F_k[ζv, ·, ·]) + (slice/FP terms through
  D(projector)(1), D(P_res^U)(1)) + D²(log𝒩′_1∘P∘M̄)(1)[DX*v, DX*v],
where the term ½tr(C_k^{ph}∇³F_k[(D²X*(v, v), 0), ·, ·]) of TOW (6) is zero: it is the U-derivative at U = 1 of the global-colour
invariant function U ↦ ½log det(slice compression of Hess_UF_k(U; 1)) (V = 1 is fixed by global colour rotations, k̃(1, ·) and the
slice data are Ad-covariant), hence zero by Lemma U-tad (i). **So b_k = −β[Γ_k] =: 𝔅(J_k; K): a fixed function of the trivial-
point jets of order ≤ 4 and fixed kernel data, built from the gapped one-step inverse only.** (This makes precise BALABAN_EXTRACT
M6 "one marginal coupling, extracted at the trivial background" for the soft scheme: no background other than 1 enters b_k.)

### 4.3 Proposition PS (per-step convergence ⇒ (F-1)): CONDITIONAL on (TC); proof PROVEN-HERE
*Norms.* For an r-point tensor T on links of Z⁴ (level units), |||T|||_m := sup_{b_1}Σ_{b_2..b_r}|T(b_1, …, b_r)|e^{m·diam(b_1..b_r)}
(diam = ℓ¹ diameter of the base points); ‖J‖_m := max of |||·|||_m over the three jets.
*(TC) (tower-jet convergence).* There are m_0 > 0, C_J, C_T and θ ∈ (0, 1) with (TC-b) sup_k‖J_k‖_{m_0} ≤ C_J and (TC-c)
‖J_{k+1} − J_k‖_{m_0} ≤ C_Tθ^k.
*Claim.* Given (TC) and Theorem N5-triv: there is C_b with |b_{k+1} − b_k| ≤ C_bθ^k; b_∞ := lim b_k exists; for all 0 ≤ j ≤ n,
|Σ_{k=j}^{n−1}b_k − (n − j)b_∞| ≤ R_PS := C_b/(1 − θ)². So FLOW's (F-1) holds with β_0′ := b_∞/log L and R := R_PS — with NO
statement about the value of b_∞.
*Proof.* N5-triv: C_k^{ph} = C_k − dT_k^{-2}d^* is m-local with |||C_k^{ph}|||_m ≤ c_C for every m < m_cov, uniformly in k (γ_i = γ_1
for i ≥ 1, PROOF [S20]); fix m < min(m_0, m_cov). By the product rule (FLOW Lemma BL (i), (v)) every term of Hess Γ_k(1) is a
contraction of C_k^{ph}, J_k and K, hence its 2-point kernel Π_k is m′-local for m′ < m, and Π_k is Lipschitz in (C_k^{ph}, J_k):
C_{k+1}^{ph} − C_k^{ph} = C_{k+1}^{ph}(H_k − H_{k+1})C_k^{ph} on the common slice (resolvent identity), so |||Π_{k+1} − Π_k|||_{m′} ≤
c(c_C, C_J, K)‖J_{k+1} − J_k‖_{m_0}. Finally |β[F]| ≤ Σ_z|z_1z_2||Π^F_12(z)| ≤ (sup_z|z|²e^{−m′|z|})·|||Π^F|||_{m′}. Sum the geometric
series twice. ∎
*Status of (TC): OPEN.* Partial: D² — F-depth (PROVEN; symbol sup norm, rate L^{-2}; the m_0-weighted form is not written);
D³ — N1-15 + T-UNIF (k- and T-uniform bound in the unweighted N3 norm; CONFIRMED as conditional); D⁴ — nothing; convergence — D²
only. *Why (TC) is plausible (ARGUED):* by Proposition JET-MARG the marginal parts of J_k are pinned for all k (β[𝒯_k] = 1, F-tree),
so (TC-c) concerns only irrelevant parts; the main (K = 0) alias of the pullback by ζ multiplies a degree-m cubic part by L^{1−m}
and a degree-m quartic part by L^{−m} (m ≥ 3 resp. m ≥ 2 for irrelevant parts — odd/even by point inversion), i.e. contracts by
L^{−2}; every alias contribution to the cubic needs at least two nonzero aliases (K_1 + K_2 + K_3 ≡ 0 mod L), each O(|p|³) by F-bg;
the exchange term of D⁴ runs through the gapped C_k^{ph}, so it is irrelevant. The k-uniform bound is naturally obtained by
N1-15's composite method (single pullback through the k-level chain minimiser, geometric level sum A_soft = 1/L), which also
suggests convergence; neither the weighted version nor the quartic nor convergence is written.
*What PS does not give.* The value b_∞. The identity b_∞ = β_0^std log L is a statement about lim B_n/n, i.e. multi-scale; a
single one-step Gaussian integral at fixed L delivers only b_k (at depth k) or 𝔅(J_∞) (at the fixed point), not its value.

## 5. T4(b) — the exact coarse-gauge orbit average, and the one-loop regrouping at every background

### 5.1 Theorem K̄ (exact): PROVEN-HERE
*Setting.* FLOW Prop. U-dec: K_comp(V, U_0) := ∫Π_{0<k<n}dU_kΠ_{k<n}K_k(U_{k+1}, U_k), ∫K_comp(V, U_0)dV = 1. Covariance: for every
fine gauge transformation g, K_comp(V^{g|_n}, U_0^g) = K_comp(V, U_0), g|_n the restriction to the level-n sites (each one-step
kernel is covariant under the gauge transformations of its two levels, D4-norm; the intermediate levels are absorbed by Haar
invariance; for odd L level-n sites are sites of every level). G_n := Π_{level-n sites}SU(N) acts by V^h_c = h_xV_ch_y^{-1}. ρ_0 ≥ 0
any gauge-invariant integrable level-0 weight (e^{−u𝒯_0} at FLOW's one loop, or the actual density); Z_n(V) := ∫dU_0ρ_0K_comp.
*Claim.* (i) Z_n(V^h) = Z_n(V) for h ∈ G_n; (ii) Z_n(V) = |G_n|^{-1}∫dU_0ρ_0(U_0)K̄(V, U_0), K̄(V, U_0) := ∫_{G_n}dh K_comp(V^h, U_0);
(iii) K̄(V^{h′}, U_0^g) = K̄(V, U_0) for every h′ ∈ G_n and every fine g — K̄ is invariant under ALL fine gauge transformations of U_0,
separately from V.
*Proof.* (i) Take a fine g with g|_n = h; substitute U_0 = U′^g (Haar), use ρ_0(U′^g) = ρ_0(U′) and K_comp(V^h, U′^g) = K_comp(V, U′).
(ii) Average (i) over G_n; Fubini (compact, bounded). (iii) K_comp(V^h, U_0^g) = K_comp(V^{(g|_n)^{-1}h}, U_0) (covariance; (V^h)^k =
V^{kh}); integrate over h and use left Haar invariance; V^{h′}: right invariance. ∎
*Meaning.* The relative gauge orientation of V and the blocked field (the directions G_n = Ran D on which 𝒞_n grows like n/κ,
FLOW Lemma COV-str (iv)) is integrated exactly, before any expansion; what remains is a fully gauge-invariant problem for U_0.

### 5.2 Proposition K̄-1L (the regrouping G_⊥ + G_gh at every background): PROVEN-HERE at FLOW's one-loop (Laplace) level
*Setting.* FLOW's one-loop conventions (U-dec): uniform u, −log K_comp(V, U_0) = uΨ(U_0; V) + Λ(U_0, V) + O(1/u), Ψ ≥ 0 with
Ψ(U_0; 𝔪(U_0)) = 0, Λ(U_0, 𝔪(U_0)) = ½log det(2π𝒞(U_0)/u). On each torus, V near 1 (per-site densities in infinite volume as in FLOW).
Ψ_min(U_0; V) := min_{h near 1}Ψ(U_0; V^h), minimiser h*(U_0, V). W* := a minimiser of 𝒯_0 + Ψ_min(·; V) — its orbit is that of
FLOW's tower Φ_0(V) (at the tower D_V^*𝒞^{-1}r = 0, the coarse-gauge stationarity, so h* = 1 there, and min(𝒯_0 + Ψ_min) =
min_h min_{U_0}(𝒯_0 + Ψ(U_0; V^h)) = min_h𝒯_n(V^h) = 𝒯_n(V)). V′ := V^{h*(W*, V)}; ρ* := log(𝔪(W*)^{-1}V′) linkwise; 𝒞 := 𝒞(W*);
D := D_{V′} (level n); D_0 := D_{W*} (fine); P_⊥ := orthogonal projector onto ker D^*; H^♮ := Hess(𝒯_0 + Ψ_min(·; V))(W*).
*Claim.* (a) H^♮D_0 = 0 exactly, for every V near 1 (no criticality of 𝒯_0 is assumed). (b)
  Γ_{0→n}(V) = G^♮_⊥,n + G_gh,n + 𝔗′_n + Γ^dr_n + const,
  G^♮_⊥,n := ½log det_{ker D_0^*}H^♮ + ½log det_{ker D^*}(P_⊥𝒞P_⊥),   G_gh,n := ½log det(D_V^*D_V) − ½log det(D_0^*D_0),
  𝔗′_n := ½log det(𝔊_0 + R) − ½log det 𝔊_0,  𝔊_0 := D^*𝒞^{-1}D,  R := Hess_hΨ(W*; V^h)|_{h*} − 𝔊_0 (order ≥ 1 in ρ*),
  Γ^dr_n := Λ(W*, V′) − Λ(W*, 𝔪(W*)),
with det′ and kernel factors where covariantly constant 0-forms exist (invisible in per-site densities; as in FLOW Lemma GH (iv)).
(c) At V = 1, H^♮(1) + D_0D_0^* = d^*d + dd^* + Q^TΠQ = FLOW's O^♯_n(1) (Π := 𝒞^{-1} − 𝒞^{-1}D(D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1} =
P_⊥(P_⊥𝒞P_⊥)^+P_⊥); the two decompositions differ off-shell.
*Proof.* (a) 𝒯_0 + Ψ_min(·; V) is invariant under every fine gauge transformation (Ψ_min(U_0^g; V) = min_hΨ(U_0; V^{(g|_n)^{-1}h}) =
Ψ_min(U_0; V), the tree-level form of Theorem K̄ (iii)), and W* is a critical point; FLOW §79 (a)'s computation (differentiate
f((W*e^{sY})^{e^{tλ}}) = f(W*e^{sY}) at s = t = 0) gives ⟨Y, H^♮D_0λ⟩ = −∇f(W*)·(…) = 0. (b) Laplace in the joint variables (U_0, h)
for the integrand of Theorem K̄ (ii) with ρ_0 = e^{−u𝒯_0}: the joint Hessian at the saddle (W*, h*) has determinant
det(Hess_hΨ)·det(Schur complement), and the Schur complement is the Hessian of the partially minimised function, H^♮ (the
second-order envelope identity, FLOW §5.5); the one-loop prefactors Λ, ½log det Hess_hΨ are evaluated at the saddle. The U_0
integral has a fully gauge-invariant exponent with a critical orbit, so its one-loop factor is the quotient integral
½log det_{ker D_0^*}H^♮ − ½log det(D_0^*D_0) + const (the computation of FLOW Lemma GH (iii) with E = ker D_0^* ⊕ Ran D_0 and
vol(Ran D_0) = det(D_0^*D_0)^{1/2}vol(Λ); it applies because of (a), not because 𝒯_0 is critical). Λ(W*, V′) = ½log det 𝒞 +
Γ^dr_n + const (U-dec (i)). ½log det Hess_hΨ = ½log det 𝔊_0 + 𝔗′_n. The linear-algebra identity of FLOW §36 step (10) (Schur for
𝒞 > 0 and the polar decomposition of D: det 𝒞 = det_⊥(P_⊥𝒞P_⊥)·det(D^*D)/det(D^*𝒞^{-1}D) — valid for every 𝒞 > 0 and every D, it
uses no HJ = 0) gives ½log det 𝒞 + ½log det 𝔊_0 = ½log det_⊥(P_⊥𝒞P_⊥) + ½log det(D^*D), and det(D_{V′}^*D_{V′}) = det(D_V^*D_V)
(V′ is gauge equivalent to V). Collect. (c) At V = 1 the h-minimisation is the Gaussian Schur complement of Ψ's Hessian on
(U_0, h), M^T𝒞^{-1}M − M^T𝒞^{-1}D(D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1}M = M^TΠM, M = Q at U = 1. ∎
*Reading.* This is FLOW's Lemma GH (iv) ("Γ^{W0}_n + Γ^cov_n = G_⊥,n + G_gh,n") at EVERY background near 1, with H^♮ in place of
H + M^TΠM and one extra term 𝔗′_n. The n-growing coarse-gauge block 𝒞^♭_G of 𝒞_n entered only through ½log det 𝒞 + ½log det 𝔊_0
and cancelled identically. FLOW's off-shell defect (§79 (DEF)) does not appear as a separate object: the off-shell effects are
inside the legitimately gauge-invariant H^♮ and inside 𝔗′_n. *Remark (ARGUED, not load-bearing):* the coarse-gauge directions,
on which FLOW's composite-slice operator O_n loses its gap like κ/S_n ((I4)), are no longer fine directions in the K̄ form; on
ker D_0^*, H^♮(1) = d^*d + Q^TΠQ has only the IR scale ℓ^{-2} of U-cov-IR, so its gap is plausibly n-uniform in ℓ-scaled units.

### 5.3 Lemma K̄-tad (the h-tadpole has no marginal part): PROVEN-HERE given (G-dec) and U-loc′ (I3); algebraic core verified by fl55_3
*(G-dec) [IMPORTED-standard].* If g is analytic on a complex neighbourhood of T⁴, positive on T⁴∖{0}, and g(P) = c|P|²(1 + O(|P|²))
with c > 0, then G(x) := ∫_{T⁴}e^{iP·x}g(P)^{-1}dP/(2π)⁴ obeys |G(x)| ≤ C(1 + |x|)^{-2} and |∇G(x)| ≤ C(1 + |x|)^{-3} on Z⁴. Applied
to 𝔊_0(1) = d_n^*𝒞_n(1)^{-1}d_n (⊗ 1_colour): 𝒞_n(1) is local at each n (U-loc′ (I3)), so its symbol is analytic; 𝒞̂_n^{-1}(0) is
B_4-invariant, hence scalar, so ŝ^†𝒞̂_n^{-1}ŝ = c|P|²(1 + O(P²)). Constants depend on n; only fixed-n statements are used.
*Claim.* β[𝔗′_n] = 0 (transverse p² coefficient at V = 1, as a directional limit).
*Proof.* Write 𝔗′ = ½tr(𝔊_0^{-1}R^{(1)}[ρ*]) + 𝔗′_{≥2}, R^{(1)} the ρ*-linear part, 𝔗′_{≥2} of order ≥ 2 in ρ*; Ξ(V′, W)[ρ] :=
½tr(𝔊_0(V′, W)^{-1}R^{(1)}(V′, W)[ρ]), Ξ* := Ξ(V′(V), W*(V)). Hess 𝔗′(1)[v, v] = 2⟨Dρ*(1)v, DΞ*(1)v⟩ + 2⟨Dρ*(1)v, B·Dρ*(1)v⟩ (B the
kernel of 𝔗′_{≥2} at (1, 1)); the term ⟨D²ρ*(1)[v, v], Ξ*(1)⟩ vanishes since Ξ*(1) = 0 (at (1, 1) R^{(1)} carries the colour structure
[e_a, e_b] of the second-order orbit term −½[Ad(V′^{-1}_c)ν(x), ν(y)], contracted with the colour-diagonal 𝔊_0(1)^{-1};
Σ_a[e_a, e_a] = 0).
(1) Dρ*(1)'s symbol vanishes on level-n gradients (pure gauge is absorbed exactly by h* and W*) and is O(|P|²) on transverse v
(stationarity gives Π̂ρ̂ = Ĝ_n^{-1}v̂ with Ĝ_n^{-1} = O(P²) by F-tree; P_⊥𝒞_nP_⊥ bounded, COV-⊥ at the trivial point).
(2) Covariance: under a fine gauge transformation g (V′ → V′^{g|_n}, W → W^g), D_{V′} and 𝒞(W) (FLOW §16: "H^0 and 𝒞 are conjugated by
the level-n values of g") transform by Ad, so 𝔊_0^{-1} → G̃𝔊_0^{-1}G̃ᵀ (G̃ := ⊕_xAd(g_x)) and Ξ(V′^{g|_n}, W^g) = Ad·Ξ(V′, W). With
Ξ(1, 1) = 0, Ξ vanishes on the joint pure-gauge orbit, so DΞ(1) vanishes on its tangent: all pairs (d_nλ_n, d_0λ_0) with
λ_0|_n = λ_n. [fl55_3 P1/P2: exactly this, in an instance, with the second-order orbit commutator; P1-c/P2-c: without transport
the same quantity is nonzero.]
(3) DΞ*(1)'s kernel is ℓ¹: it is built from −𝔊_0^{-1}(δ𝔊_0)𝔊_0^{-1}, δ𝔊_0 = δD^*𝒞^{-1}D + D^*𝒞^{-1}δD + D^*δ(𝒞^{-1})D local with a lattice
derivative on at least one side, evaluated at the endpoints of a link c; by (G-dec) the kernel from a perturbation at b to c is
≤ C|b − c|^{-5} (G·∇G) or ≤ C|b − c|^{-6} (∇G·∇G), plus local terms; Σ_b|b|^{-5} < ∞ in d = 4. So its symbol K̂ is continuous.
(4) For transverse v the input (DV′(1)v, DW*(1)v) at level momentum P tends, as P → 0, to (a constant level-n field v̂, the
constant fine field v̂/ℓ) — the smooth component of the linear tower (F-bg) — which is the compatible pair of gradients of
λ_n(X) = X·v̂ and λ_0(x) = x·v̂/ℓ (λ_0(ℓX) = λ_n(X)). In infinite volume an ℓ¹ kernel annihilates it (approximate by compactly
supported compatible gauge directions; the cut-off layer has bounded amplitude where the ℓ¹ tail tends to 0). So K̂(P)·input =
o(1)|v̂| as P → 0.
(5) The symbol of Hess 𝔗′(1) is O(P²)·o(1) + O(P²)·O(log(1/|P|))·O(P²) (B's kernel ~ 𝔊_0^{-1}(x, y)² ~ |x − y|^{-4}) = o(|P|²);
its transverse p² coefficient lim_{t→0}e^†Π̂(tn)e/|ŝ(tn)|² is 0. ∎
*The would-be κ-dependent slope (illustration, [inference], not used).* With the untransported covariance Cov_1 = σ ⊗ 1, the
expectation of the second-order orbit term on a link with Ad(V′^{-1}_c) ≈ 1 − ad_{v_c} is −½σ(x, y)Σ_a(−v_c × e_a) × e_a = −σ(x, y)v_c
(SU(2) adjoint, cross-product form — the quantity fl55_3 P2-c evaluates and finds nonzero on gradients). Inserted in
−u⟨𝒞^{-1}ρ*, E[w_2]⟩ it gives uσ_nn⟨Ĝ_n^{-1}v, v⟩ = 2uσ_nn𝒯_n^{(2)}(v), with uσ_nn ~ (n/κ)·G(e) if 𝒞^♭_G is replaced by (n/κ)·1
(G(e) the level Green function at nearest-neighbour separation, ≈ 0.155 − 1/8 ≈ 0.030 for the plain 4D Laplacian): a coupling
shift linear in n with a κ-dependent coefficient, i.e. failure mode FL-F2. Lemma K̄-tad says this is an artefact of not
transporting the covariance. **This is the one place where a κ-dependent term could have reached the coefficient of n log L,
and it does not.**

### 5.4 Lemma GH0 (the ghost group at the trivial background): PROVEN-HERE given FLOW Lemma FINE-IR (§74; CONFIRMED,
REVIEW_FLOW_S10), Corollary VFINE-gh (§88; CONFIRMED, REVIEW_FLOW_S11) and Lemma F-bg
*Claim.* β[G_gh,n] at V = 1 equals −(1/22)β_0^std log ℓ (ℓ = L^n) exactly, for every n — FLOW's constant-flux value GH-log (d).
*Proof.* Colour-reduce to one Cartan direction (Lemma F-Π (i)); root sector α, a level Cartan plane wave of amplitude ε_n and level
momentum P. Level term ½log det(D_V^*D_V): ε_n²-density q_α²(P²/2)x_0(P)·½, x_0(P) = 2c_g log(1/P) + a_0 + O(P²log(1/P))
(FINE-IR; VFINE-gh). Fine term ½log det(D_0^*D_0) at W*(V): only the linear tower enters the 2-point function (U-tad); momentum
conservation pairs the smooth component with itself and aliases with aliases; aliases are O(P³) (F-bg) and contribute O(P⁶); the
smooth component is a fine Cartan plane wave of momentum P/ℓ and amplitude (ε_n/ℓ)(1 + O(P)); per level-n site (ℓ⁴ fine sites)
its ε_n²-density is ℓ⁴q_α²((P/ℓ)²/2)x_0(P/ℓ)ℓ^{-2}(1 + O(P))·½ = q_α²(P²/2)x_0(P/ℓ)(1 + O(P))·½ — the powers of ℓ cancel (the 4D
Laplacian's coupling is marginal) and it is the SAME function x_0 (both are the nearest-neighbour covariant Laplacian in their own
units). The difference is q_α²(P²/4)[x_0(P) − x_0(P/ℓ)] + O(P³log(1/P)) = −q_α²(P²/4)·2c_g log ℓ + O(P³log(1/P)): the finite parts a_0
cancel exactly and only the log of the scale ratio survives. Summed over roots and converted to u-units with FLOW's normalisation
(GH-log (d); arithmetic re-verified in fl55_1 B3) this is −(N²/(24π²))log ℓ = −(1/22)β_0^std log ℓ. ∎ (At U = 1 this needs only
FINE-IR, not G-mag (vi).)

### 5.5 Corollary K̄-β and the precise residue (UIR^♮): PROVEN-HERE given §5.2-§5.4 and FLOW Lemma U-pair (CONFIRMED-WITH-FIX,
REVIEW_FLOW_S1_S2) for Γ^dr
For every n ≥ 1, at the trivial background:
  **B_n = −β[G^♮_⊥,n] + (1/22)β_0^std n log L,**
because β[Γ^dr_n] = 0 (U-pair application (1), with the joint-saddle residual ρ* in place of r; hypothesis (e) by U-loc′) and
β[𝔗′_n] = 0 (§5.3). Hence
  **(UNIV-1L) ⟺ (UIR^♮): sup_n|β[G^♮_⊥,n] + (21/22)β_0^std n log L| < ∞.**
*(UIR^♮) in residue-lemma form.* Let J^♮_n be the p²-integrand at V = 1 of the fine unit [½log det(H^♮ + D_0D_0^*) − ½log det′Δ_{W*}]
(propagator (O^♮_n(1))^{-1} = (d^*d + dd^* + Q^TΠQ)^{-1}, FLOW's O^♯_n(1); vertices: the trivial-point jets of 𝒯_0 + Ψ_min and of
D_0D_0^*). By FLOW's U-res and VFINE-K/VFINE-L (§88: "½(−20) − ½ = −21/2", the transverse 21/22 of the 11), (UIR^♮) follows once
(R-a), (R-b) hold for J^♮_n with n-uniform constants and β[½log det_⊥(P_⊥𝒞_nP_⊥)] is n-uniformly bounded. Ingredients available
at U = 1: U-cov-IR′ (transverse propagator part, PROVEN), VC-T0 and VC-T1 (jets of 𝒞_n's transverse block, orders ≤ 2, given
(Π-loc)), Lemma P-poles (jets of the level projector), Lemmas Cartan-𝔪/Cartan-T (jets of the composite map), FINE-IR/VFINE-K
(massless log coefficients). **Missing: the estimate that combines them — the vector (U-IR)(a2) for the vertices of Ψ_min's
jets — and (s2⊥)'s root-sector bound. (UIR^♮) is OPEN.** It is FLOW's (V-IR)/(Q1)(d) restated at U = 1 for the off-shell-correct
transverse group, with (T-c), the Nielsen-Olesen mode, COV-GI-∞, (L-loc2) on 𝒦_n, Lemma N-f and (DEF)/(GP) removed.
*FLOW's T-split under K̄.* GP-L holds at every V with H^♮ ((H^♮ + D_0D_0^*)^{-1} = (H^♮_⊥)^{-1}P_⊥ + D_0Δ^{-2}D_0^*, since H^♮D_0 = 0), but
H^♮ already contains the IR term, so FLOW's Woodbury split (Wilson ⊕ IR term) is not available off-shell without re-introducing
the defect. In the K̄ organisation the only fine inverse is the gapped (H^♮_⊥(1))^{-1}; (T-a1-M), the unconstrained H_⊥(1)^{-1}, does
not arise. [ARGUED: a K̄-compatible level telescoping replacing T-tel has not been constructed; whether (UIR^♮) is easier
unsplit is not decided here.]

## 6. T4(c) — the leading coefficient

### 6.1 What is re-verified exactly (fl55_1, 13/13 PASS, 4/4 controls fire)
- **The 11.** For the background-Feynman operator −D²δ_μν + 2 ad F_μν on Lorentz ⊗ adjoint and the ghost −D² on the adjoint, with
  explicit structure constants (SU(2): Pauli/2; SU(3): Gell-Mann/2, entries in Q(√3)) and a random rational field strength:
  X_vec := (1/12)tr(Ω^vecΩ^vec) + ½tr(E²) and X_gh := (1/12)tr(ΩΩ) give (½X_vec − X_gh)/(−X_gh) = 11 exactly; diamagnetic part −1,
  paramagnetic part 12 (11/3 = 4 − 1/3); X_gh = −(N/12)Σ(F^a_μν)² with Σ_{cd}f_acdf_bcd = Nδ_ab. With the spin coupling 1 instead of 2
  the ratio is 2 (control). This is PROOF L4b's (½)a_2^vec − a_2^gh = (11/12)C_AF^aF^a, re-derived independently of check c2.
- **The conversion.** 1 − N^{-1}Re tr e^{itX} = t²tr(X²)/(2N) + O(t⁴) (exact series for explicit hermitian X, N = 2, 3), hence
  u = 2N/g_std² (FLOW Lemma F-norm); 2N·2b_0 = 11N²/(12π²) = β_0^std; the wrong 2N·b_0 (FLOW's old FN-1 slip) fails (control).
- **The split.** 2·(1/(48π²))/(11/(12π²)) = 1/22; (1/22)β_0^std = N²/(24π²); from C_{K_F} = −20 (units c_g): ½(−20) − 1 = −11 (the
  Feynman 11/3) and ½(−20) − ½ = −21/2, ratio 21/22 (FLOW §88's cross-checks).
- **The scalar channel.** S³ averages ⟨n_1²n_2²⟩ = 1/24, ⟨n_1⁴⟩ = 1/8, ⟨n_1²⟩ = 1/4 (exact Gaussian moments); FLOW §5.7's four
  leading terms average to −1/3, times the shell measure 1/(8π²), so β = 1/(24π²) per log(1/m) and c_Γ = 1/(48π²) = 2c_g; and FINE-IR's
  (2π²/24)(2π)^{-4} = 1/(192π²), 4/(192π²) = 1/(48π²). The product-of-marginals average 1/16 gives −1 (control).

### 6.2 Proposition KAPPA (κ cannot change the coefficient of n log L): CONDITIONAL on (UIR^♮); proof PROVEN-HERE
*Claim.* Given (UIR^♮) and FLOW's U-res, U-Tay/VFINE-K (CONFIRMED), for every κ > 0: B_n = β_0^std n log L + O_κ(1); κ enters only
the O(1) constant.
*Proof.* Corollary K̄-β: B_n = −β[G^♮_⊥,n] + (1/22)β_0^std n log L. G_gh,n contains no 𝒞, so its coefficient is κ-free (Lemma
GH0). β[G^♮_⊥,n] = ∫J^♮_n + (level group); the leading homogeneous part of J^♮_n is the massless background-Feynman transverse
integrand (no κ, no 𝒞), whose residue is −(21/22)β_0^std per log ℓ (VFINE-K/VFINE-L + fl55_1's arithmetic); by U-res the
coefficient of log ℓ is that residue and κ enters only (R-a), (R-b), which (UIR^♮) bounds uniformly in n. The κ-dependent objects
that grow with n — the coarse-gauge block 𝒞^♭_G (λ_max ~ n/κ) and its h-tadpole (naive size ∝ (n/κ)G(e)) — cancel identically
(§5.2) or have β = 0 (§5.3). ∎
*Per-step reading.* Given also (TC), b_∞(κ) = lim(B_{n+1} − B_n) = β_0^std log L for every κ > 0: at the fixed point of the tree
tower, the one-step Gaussian integral at the trivial background carries the universal coefficient exactly, and every κ-dependent
contribution of the one-step integral (the one-step coarse-gauge tadpole, the kernel vertices, log𝒩′_1, the finite parts of the
gapped one-step determinant) must cancel there. **This is the precise sense in which "2b_0 log L comes out of the one-step Gaussian
integral at the trivial background": it does, at the fixed point, as a consequence of the multi-scale statement (UIR^♮) (or of
UNIV-1L) — not as a property of a single step that can be checked in isolation at fixed L.**
*Not done.* No numerical evaluation of b_k, B_n or any 4D lattice integral (the brief's no-float rule; no exact method exists for
these transcendental integrals). FLOW's float checks f2, f3, f5/f5b (log slopes within 0.3-1% of the universal value in the
scalar/abelian channels, κ-spread 0.0034-0.0044) are consistent with KAPPA but are not verdicts under this brief.

## 7. T4(d) — the remainder bound, CONDITIONAL on named inputs (re-derivation of FLOW's Prop. F-rem)
*Statement.* If g_0, …, g_k ∈ (0, γ_0], then β_k := u_k − u_{k+1} = b_k + ρ_k with
  ρ_k = −β[ΣE^{≥2}_k] + δβ_k (sign: FLOW [RFL-fix FR-2]),  |ρ_k| ≤ C_ΠE_2g_k² + g_k⁶ ≤ C_ρg_k²,  C_ρ := C_ΠE_2 + 1 (g_k ≤ 1),
  C_Π := 64M⁶α^{-2}Σ_{n≥1}n³(6400e^{−κ_p})^{n−1},
given **(SF-g)_k** (FLOW §4: analytic polymer representation of the step output on D_α(X), ‖E^{≥2}_k‖_{κ_p} ≤ E_2g_k², constants
uniform in k, K, T, along the chain's own sequence), **(RLF-δ)_k** (|δβ_k| ≤ g_k⁶ from (F_R)_{[0,k]}), and FLOW Lemmas F-ren (ii),
F-Π. *Re-derivation (CONFIRMED):* Lemma F-Π (ii): the two-variable Cauchy estimate on the bidisc of radius α gives
|∂²F(X)(0)| ≤ α^{-2}‖F‖e^{−κ_pd(X)}; a link is in ≤ 16 M-cubes; ≤ 80^{2(n−1)} = 6400^{n−1} *-connected X of n cubes contain a given cube;
b_z ranges over ≤ 4M⁴n links; |z_1z_2| ≤ (Mn)²; d(X) ≥ n − 1; so Σ_z|z_1z_2||Π_12(z)| ≤ 16·4M⁴·M²·α^{-2}‖F‖Σ_nn·n²(6400e^{−κ_p})^{n−1} =
C_Π‖F‖. Then u_{k+1} − u_k = β[Γ_k] + β[ΣẼ_k∘Φ] + β[ΣE^{≥2}_k] + β[𝒮^{LF}_k] = −b_k + 0 + β[ΣE^{≥2}_k] − δβ_k. ∎
*What the Ward transport adds.* By Proposition JET-MARG, ΣE^{≥2}_k (gauge invariant, B_4-covariant, local) has no marginal cubic
or quartic part beyond β[ΣE^{≥2}_k] times the Wilson ones; so ρ_k is the COMPLETE marginal content of the higher-loop terms, and the
renormalised remainder carries no hidden marginal coupling at orders 3, 4. The polydisc (SF-g) is where the non-trivial
background enters (§3.4). Theorems F-flow and F-tune then follow by FLOW's arithmetic (CONFIRMED by REVIEW_FLOW_S1_S2; spot-checked
here: |u_j − u_n − (B_n − B_j)| ≤ Σ_{k=j}^{n−1}|ρ_k| ≤ (n − j)C_ργ², and C_ργ² ≤ ½β_0′log L gives β_0′/2 ≤ β_- ≤ β_0′ ≤ β_+ ≤ 3β_0′/2).
Symbol collisions met (systemic defect 1): κ_p (polymer decay) ≠ κ (soft kernel) ≠ Balaban's κ; α (polydisc radius, FLOW
§3) ≠ Balaban's α_0, α_1; M (FLOW's M-cubes) ≠ Balaban's M = L^m ≠ LINEAR_PACKAGE's package constant M ≠ the composite map M_U
of §5 (= D𝔪_n(U), FLOW's notation); E_2 (FLOW's higher-loop polymer constant) ≠ any E_k^br; R (FLOW's additive constant) ≠ R (the
ρ*-part of the h-Hessian in §5.2) — the latter is local to §5.

## 8. T5 — decision

**PARTLY.** Precisely:
- **Bypassed entirely** (given Theorem K̄, Proposition K̄-1L, Lemma K̄-tad, Lemma GH0, Corollary K̄-β — PROVEN here at FLOW's one-loop
  level, K̄-tad given the standard (G-dec)): (T-c); the constant-flux definition of the coefficient (c^tot_n at U_f); the Nielsen-Olesen
  mode; COV-GI's hypotheses at U_f, COV-GI-∞, Lemma N-f, (L-loc2) on the class 𝒦_n (only U = 1 jets are needed, which U-loc′ gives);
  G-mag (vi)'s role (Lemma GH0 needs only FINE-IR); FLOW's (DEF) and its replacement (GP); and every inverse of an unconstrained operator
  at a background U ≠ 1 — in particular H_⊥(U)^{-1} at finite background. The only fine inverse left is the gapped (H^♮_⊥(1))^{-1}.
- **Converted, not bypassed:** (T-a1-M) and (T-b). At the orders FLOW states them they were already Taylor data at U = 1; in the K̄
  organisation both are absorbed into one trivial-background statement, (UIR^♮). If FLOW keeps its Woodbury/T-split organisation,
  (T-a1-M) is the U = 1 pole bookkeeping of the massless H_⊥(1)^{-1} (the fine-level analogue of Lemma P-poles) and (T-b) is the U = 1
  plane-wave density of the gapped operator H_⊥ + M̃^T(P_n𝒞_nP_n)^{-1}M̃ — neither needs a non-trivial background.
- **Not bypassed:** (UIR^♮) — the trivial-background, n-uniform IR estimate for the gapped transverse group (FLOW's crux, restated); for
  the per-step alternative, (TC) (tree-level, trivial background) plus the slope part of (UIR^♮); and, for the remainder half of the
  theorem (not part of FLOW's wall), layer 1's polydisc (SF-g), whose operator is the soft-constrained one-step covariance at complex
  small backgrounds (N5 at levels ≥ 1, (NA-H_loc), BFT-0 analytic: OPEN).
- **Answer in one line.** The Ward-identity route removes the background-dependent half of FLOW's wall entirely and turns the rest into
  a single trivial-background IR estimate, (UIR^♮) ⟺ (UNIV-1L); it does not remove that estimate, and it cannot: the value b_∞ = β_0^std
  log L is a multi-scale statement that no trivial-background one-step identity, Ward or otherwise, can deliver.

## 9. FOR OTHER FILES (demands raised by this file; none applied — this worker writes only FLOW55.md and checks/fl55_*)
- **FLOW (lane C).** (1) After an independent review of §5, adopt the K̄ form — Theorem K̄ → Proposition K̄-1L → Lemma K̄-tad → Lemma
  GH0 → Corollary K̄-β — and restate the remaining wall as (UIR^♮) at U = 1; this retires (T-c), the U_f definition of c^tot_n, COV-GI-∞,
  (L-loc2) on 𝒦_n, Lemma N-f, (DEF)/(GP) and the Nielsen-Olesen caveat. (2) If the T-split is kept, restate (T-a1-M) and (T-b) as
  U = 1 Taylor statements; (T-a1-M) is then a fine-level P-poles lemma for H_⊥(U)^{-1}P_⊥(U) at U = 1. (3) The reviewer should re-derive
  K̄-1L's Schur/envelope step, the quotient step under (a), and K̄-tad steps (3)-(4) (decay; the P → 0 input) — see also §11 erratum 1.
- **HANDOFF, critical-path item 6** (after review): "FLOW: the wall is (UIR^♮), a trivial-background, n-uniform IR estimate for the
  transverse one-loop group (⟺ UNIV-1L); (T-c) and the Nielsen-Olesen mode are removable by integrating the coarse-gauge orbit
  (FLOW55 §5); (T-a1-M), (T-b) are U = 1 Taylor data."
- **Layer 1 (lane A / BFT / NORMS).** For the per-step route, (TC): an exponentially weighted version of Theorem N1-15, its quartic
  analogue including the tree exchange term, and convergence in k. For the remainder, (SF-g): N5 at levels ≥ 1 at complex backgrounds
  ((NA-H_loc)) and BFT-0 in analytic form. Symbol check requested: NORMS's soft normalisation (φ̂ = ½|ρ|² + O(ρ⁴), κ_j) against FLOW's
  κk̃ (§3.5 table).
- **PROOF.md L4a.** Consistent with BALABAN_EXTRACT B3-3: "β_j → 2b0 ln L" is not a one-step or a Balaban statement; it is (UNIV-1L).
- **HINT55.** The flow supplies (given (UNIV-1L) ⟺ (UIR^♮), plus layer 1's (SF-g), (RLF-δ), (SF-cont), (SF-∞)) explicit β_- > 0, β_+, R and
  F-tune, volume-uniformly; a witness built on the running between two scales needs them separated by m > R/(β_-log L) levels; its
  leading-order YM value needs the sharp slope.
- **EXISTENCE H-Bal-1 / (F).** The soft-scheme flow is FLOW's F-tune with ±R, conditional exactly on (UIR^♮) plus the four layer-1
  inputs above; nothing in it is supplied by a readable Balaban paper (BALABAN_EXTRACT B3-3, B3-8).

## 10. Summary table (claims of this file)
| # | claim | status here |
|---|---|---|
| 1 | Consumer requirements (§1) | stated with quotes; no proof needed |
| 2 | Lemma W-loc: (F-2)-(F-4) use no non-trivial background except via (SF-g); FLOW's non-trivial background and unconstrained inverse enter only via (C1), (C2); (T-a1-M), (T-b) at orders ≤ 2 are U = 1 data; only (T-c) needs finite flux | PROVEN-HERE (inspection; refutable by a missed use) |
| 3 | Lemma WARD-J (jet Ward identities W1-W4) | PROVEN-HERE |
| 4 | Proposition JET-MARG (marginal cubic/quartic jets = β × Wilson's) | PROVEN-HERE, with fl55_4 |
| 5 | Corollary TRANSPORT | PROVEN-HERE (given the polydisc for the order-≥5 part) |
| 6 | §3.4: the non-trivial background re-enters only via (SF-g); the operator is the constrained one-step covariance | PROVEN-HERE (logic) + status quotes |
| 7 | §3.5: what LINEAR_PACKAGE / N1-15 / T-UNIF supply | assessment (statuses quoted) |
| 8 | Lemma ENV | PROVEN-HERE, with fl55_2 |
| 9 | §4.2: b_k = 𝔅(J_k; K), no second-order tower | PROVEN-HERE (given TOW, U-tad) |
| 10 | Proposition PS: (TC) ⇒ (F-1) with β_0′ = b_∞/log L, R = C_b/(1 − θ)² | CONDITIONAL on (TC) (OPEN); proof PROVEN-HERE |
| 11 | Theorem K̄ (exact orbit average) | PROVEN-HERE |
| 12 | Proposition K̄-1L (G_⊥ + G_gh regrouping at every V; H^♮D_0 = 0) | PROVEN-HERE at FLOW's one-loop level |
| 13 | Lemma K̄-tad (β of the h-tadpole = 0) | PROVEN-HERE given (G-dec) [IMPORTED-standard] and U-loc′; core checked by fl55_3; see erratum 1 |
| 14 | Lemma GH0 (β[G_gh,n] at U = 1 = −(1/22)β_0^std log ℓ exactly) | PROVEN-HERE given FINE-IR, VFINE-gh, F-bg (CONFIRMED upstream) |
| 15 | Corollary K̄-β: B_n = −β[G^♮_⊥,n] + (1/22)β_0^std n log L; (UNIV-1L) ⟺ (UIR^♮) | PROVEN-HERE given 11-14 and U-pair |
| 16 | (UIR^♮) | OPEN |
| 17 | Proposition KAPPA (κ only in the O(1) constant) | CONDITIONAL on (UIR^♮) |
| 18 | §6.1 arithmetic chain (11 = 12 − 1; 2N·2b_0; 1/22 : 21/22; 1/(24π²)) | CONFIRMED by exact check fl55_1 |
| 19 | Remainder bound (Prop. F-rem, constant C_Π) | CONFIRMED (re-derived), CONDITIONAL on (SF-g), (RLF-δ) |
| 20 | Decision: PARTLY (§8) | — |

## 11. Reviews and Codex verdicts used; errata
- **CODEX_REVIEW_TUNIF2** ("(T-UNIF), with the stated repairs, is CONFIRMED as a conditional theorem"): **agree**, as far as it bears
  here (§3.5 uses only the conditional status of N1-15's k- and T-uniform N3 bound; I did not re-derive TU-5/TU-6).
- **CODEX_REVIEW_OLDREV**, FLOW rows: used only for context. I note its F2 (that (Π-loc)'s locality/analyticity follows from the
  direct-sum per-link structure and the analytic maximiser) bears on VC-T1's "given (Π-loc)" (§5.5 ingredients); I did not re-derive
  it and nothing here depends on it.
- **REVIEW_FLOW_S13 §12** ("The fine, background-dependent inverse H_⊥(U)^{-1} — i.e. (T-a1-M) together with (T-b)"): **agree** that it is
  FLOW's biggest live wall in FLOW's organisation; **disagree** with "a resolvent on the fine lattice at a non-trivial background, a
  genuinely new analytic object" as a description of (T-a1-M)/(T-b) at the orders stated (they are U = 1 Taylor data; the non-trivial
  background enters through (T-c) and (C1)); its "Runner-up … (T-c)" is, in this file's analysis, the genuinely background-dependent part.
- **REVIEW55_NORMS r55n-A1, r55n-A4; REVIEW55_TUNIF §L**: statuses of N1-15 quoted; my Lemma ENV agrees with r55n-A1's derivation.
- **BALABAN_EXTRACT §7.4, M6**: agree that FLOW's wall is route-specific; §2 here makes it precise (choices (C1), (C2)); the extract's
  "Balaban always inverts the constrained operator" is its own inference (its §13 erratum), and the route here needs only the constrained
  operator in any case.
- **Erratum 1 (to §5.3 steps (3)-(4), appended before this file was handed over).** Step (3) should read "DΞ(1) — the derivative of Ξ in
  its arguments (V′, W) — has an ℓ¹ kernel", not DΞ*(1): the chain-rule factor DV′(1) (V′ = V^{h*}) is non-local (it contains the massless
  level projector (D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1}), so DΞ*(1) itself need not be ℓ¹. Step (4) uses exactly what is true: for a transverse plane
  wave v̂ (P·v̂ = 0), DV̂′(1)(P)v̂ → v̂ as P → 0 (the correction D̂(D̂^†𝒞̂^{-1}D̂)^{-1}D̂^†𝒞̂^{-1}(v̂ − Q̂â) is O(|P|) because 𝒞̂_n^{-1}(0) is
  scalar and P·v̂ = 0, P·Q̂â = P·v̂ + O(P²)), and DŴ*(1)(P)v̂ → v̂/ℓ (F-bg); the continuous symbol D̂Ξ(P) then kills the limit pair. The
  conclusion of Lemma K̄-tad is unchanged.
- **Erratum 2 (to §3.3, m = 3).** The proof uses that G_3's symbol is odd under point inversion (links reverse, X → −X, three legs), so
  its expansion starts at degree 1 and the degree-2 part of G_3[X, X, dλ] is exactly the degree-1 part contracted with the λ-momentum;
  this is stated explicitly only in the m = 4 step.

**End of FLOW55 findings (worker claude-opus-5-5).**

## 12. Check provenance (appended 2026-10-29T00:54Z)
File mtimes (local clock, UTC−4h shown by `ls` as 20:31-20:35 on Oct 28 = 00:31-00:35Z): every criteria file precedes its script.
md5: fl55_1.py 60698fb767971472ec5beb997362a7ad; fl55_2.py 65e3fd9874b4ccf4e13e804d3228c953; fl55_3.py a19a41abb0927a79906302386f9c258c;
fl55_4.py af6f5870a13ae0df02bfef547358d08b. Each script was run exactly once (outputs unaltered); runs used < 70 MB and < 2 s each.
