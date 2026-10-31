Reviewer model: claude-opus-5-5

# STEP55 — one RG step on the small-field region: conditional positivity, per-step cluster expansion, (BFT-coer)

Worker: Opus 5.5 (claude-opus-5-5), extra effort. Started 2026-10-29T04:49:01Z (UTC).
Scope (from the queue brief `step.md`): inputs I1 (a), I1 (b) and I2 named by `LARGE55.md`.
Write set: this file and `checks/st55_*` only. No git.

## 0. PRE-STATED (written before any derivation)

Targets.

- **T1 (I1 (a); N5 at levels >= 1).** At a chart background (the level-k critical background, small
  curvature) the one-step fluctuation quadratic form on the small-field region Lambda_k(h), possibly with
  holes, is positive-definite with a gap bounded below by a constant times the soft-constraint mass
  squared, the constant independent of k, T (the torus side), the region and the holes. Also: an exact
  account of why the LCONV55 "stripe" (a fine mode invisible to coarse levels with negative curvature)
  does not obstruct ONE-step positivity.
- **T2 (I1 (b); N6).** The one-step fluctuation integral on the small-field region has a convergent
  polymer (cluster) expansion around its Gaussian part, with local activities that are holomorphic in the
  background/coarse field on a complex neighbourhood and decay exponentially at a rate set by the
  soft-constraint mass, uniformly in k, T, region and holes; the coupling g_k enters only as a spectator
  (bounds uniform in g_k small), so the same expansion serves SRC's (D1) decaying-polymer route.
- **T3 (I2; BFT-coer).** At the trivial background, the minimal soft action compatible with given coarse
  data dominates the coarse Wilson quadratic form, with an explicit constant c_co computed in exact
  rational arithmetic from the LINEAR_PACKAGE symbols; then the chart perturbation of this statement
  using banked BFT inputs.

What would count as a refutation (each is a first-class result if found).

- R1 (against T1): an admissible region/hole configuration, or a chart background, at which the one-step
  fluctuation form (with the soft constraint) has a non-positive eigenvalue, or whose gap tends to 0 as
  k, T, the region or the holes vary; or a proof that the stripe mode of LCONV55 lies inside the
  one-step fluctuation space with negative curvature.
- R2 (against T2): any k-, T- or region-dependence of the decay rate or of the activity bounds that is
  not uniformly controlled; a non-local or non-holomorphic activity; or a needed smallness that is not
  supplied by the coupling or by a banked input.
- R3 (against T3): a coarse configuration whose minimal compatible soft action is smaller than every
  positive multiple of its coarse Wilson quadratic form (e.g. coarse curvature realisable at vanishing
  soft-action cost), or an exact-arithmetic c_co <= 0.
- Status discipline: any statement that rests on a not-yet-banked input is labelled CONDITIONAL with the
  input named; nothing is labelled PROVEN-HERE unless its load-bearing step is derived in this file.

## §0. Read record, provenance of inputs, coordinator notices (written ≈05:20Z, before any criteria file or script)

**Read (located by string; large files never read whole).** The queue brief `step.md`; REVIEW_BRIEF_55.md (all). LARGE55.md
(all, §0-§12 and closing; final at 04:46:59Z). CODEX_REVIEW_LARGE.md (all; its receipt says final at 05:12:23Z; read after the
coordinator's second notice). LCONV55.md (§0, A-I, FOR THE LEAD items 1-6) and CODEX_REVIEW_LCONV.md (all; R1-R10 and the
no-go gate). CODEX_REVIEW_NRES.md "Exactly what may be banked"; NODEA_RES55.md §3.1 (Theorem BL-TILT and BL-1..3). PROOF.md by
string: the banner and `[S26-BANKED]` block; `Lemma N5-sl`, `Lemma N5-coer`, `Lemma N5-loc`, `Theorem N5-triv`, `Setting N5-bg`,
`Lemma N5-cov`, `Lemma AX` (statement), `Lemma N5-an`, `Lemma CT♯`, `Theorem RW` (with the R1819/R20 fixes inside it),
`Corollary RW-triv`, `Theorem N5-sf0` (statement, proof, constants, "The threshold, evaluated", SF7-edit 3/4),
`Proposition N5-sf_i`, `Lemma NA-alg`, `Proposition NA-lev` items (b) `Lemma E-low`, (c), (d), `Theorem NAH1` (statement),
`Proposition NAH-ind` with `(BG-unif)`. LINEAR_PACKAGE.md (frozen v1.1) §0-§5. SRCAN55.md §1, §2.1, §2.4 (`Corollary SA-RW`),
§3.7, erratum E6. GV55.md, the BFT-0/1/2 block (string `(BFT-1)** with η := C_0s`). PLD.md §9.4, the paragraph
`(RLF-5) width (ARGUED, not counted)`. Scripts read for conventions only: `checks/lg55_2_s4p.py` (S4′ contour convention),
`checks/lc55_2_certify.py` l.1-140 (quaternion conventions). Corpus (data only, cited by id + section): 1108.1335 §4.4-§4.6
(Lemmas 17-21) and appendix Lemma 29.
**Not read:** NODEA55.md beyond what LCONV55/CODEX_REVIEW_NRES report of it; BFT_A/BFT_B, FLOW, SF, HW, HIST (only through the
strings above); KFACTOR_OFF55, BFT34_55, OFFGLOB55/OFFGLOB2_55 (used only through the [S26-BANKED] lines). No claim below
rests on an unread file; where an input is quoted from a summary line it is labelled so.

**Provenance rule applied.** A session-24/25 result is an input only if [S26-BANKED] or a CODEX_REVIEW_* "bankable" section
confirms it. Pre-S24 lane theorems (N5-triv, N5-coer, N5-sf0, RW, CT♯, NA-alg, E-low, PG, Theorem 5.1 of LINEAR_PACKAGE) are
cited as lane statements reviewed in sessions ≤ 23; where one is load-bearing for a new claim I re-derive its load-bearing
step here or say that I did not.

**Coordinator notices received while working (both addressed below).**
- (N1, ≈05:00Z) CODEX_REVIEW_LCONV landed: the stripe, bare-action counterexamples, exponential-chart obstruction and Lemma
  FOL's local identity CONFIRMED; no unrestricted (LC-1′) refutation, no universal convexity/Peierls no-go, no exact
  lowered-coupling identity banked. Corrections to use: width 2.09/τ; plaquette-cut units 22/3 → 11/6, c_*/8 → c_*/32;
  u_0β² = 1 at β = g_0. *Request:* state precisely which chart and metric my positivity is in, and why the stripe or any
  coarse-invisible direction cannot be negative there within one step. → §3.
- (N2, ≈05:15Z) CODEX_REVIEW_LARGE landed. *Request:* aim at "one normalised, history-compatible RG step on a chart with a
  hole: main-term price, geometric mismatch implication, normalised returned-activity analytic norm, reference comparison,
  failed returns"; and **address the zero-free normaliser explicitly** (Codex: KA bounds numerator and denominator from above
  only). → §4 (zero-free normaliser), §2 (main-term price), §6 (mismatch implication), §5 (normalised activities), §8.

**Codex verdicts used, and whether I agree (per the brief; each is re-judged where I touch it).**
| Codex item | verdict | mine |
|---|---|---|
| CODEX_REVIEW_LARGE F1: the exact conditional action at fixed V is S(U) + Σ_c[tφ_{M_c(U)}(V_c) + log 𝒩_t(M_c(U))]; omitting log 𝒩 is an algebraic defect | REFUTED (LARGE55's "total soft action") | **agree**; re-derived in §3.1 (the log 𝒩 term is O(1)-smooth in U once centred; Lemma NZ-R, §4) |
| CODEX_REVIEW_LARGE F2: MIS bounds ψ ≥ δ, not geometric curvature; log-mean vs arithmetic-mean maps differ | CONFIRMED / NOT-VERIFIED interface | **agree**; the interface is proved in §6 (Lemma GMI, via NA-alg (a)) |
| CODEX_REVIEW_LARGE F3: KA gives upper envelopes only; the mixture D(V) = [k_t(V;H) + k_t(V;−H)]/2 vanishes at r = asinh(π/(2t)) | KA CONFIRMED; returned-activity inference REFUTED | **agree** with both; I re-derive the mixture zero (§4.4) and show it cannot occur for a single normaliser (§4) |
| CODEX_REVIEW_LARGE F9: PRICE needs local charge allocation, boundary/tail control, the normalised main term; same-a absorption of t^q REFUTED | NOT-VERIFIED / REFUTED | **agree**; §2.4 supplies local charge allocation at the linear level with no tails |
| CODEX_REVIEW_LCONV R6: with coarse fields frozen, the kernel adds curvature κu r|b|² of the same coupling order on the stripe's slow direction | CONFIRMED (point) | **agree**; it is the mechanism of §3, computed exactly in §3.5 (check st55_2) |
| CODEX_REVIEW_LCONV R9: LCONV55 G2 "one-step conditional convexity holds" is an unproved promotion | REFUTED (promotion) | **agree as to LCONV55's text**; at level 0 the needed theorem already exists pre-S24 (N5-sf0 (b)), see §3.3 |
| CODEX_REVIEW_LCONV R2/R5: the explicit stripe vector and RQ_cyl = −96τ²(2 + s⁻²)/(27 + 96τ²) | CONFIRMED | **agree**; reused (transplanted to a torus) in check st55_2 |
| CODEX_REVIEW_NRES item 2: BL-TILT under H-convexity, D1-D4 | CONFIRMED | **agree**; used only as a named consumer (§3.6) |

## §1. Symbols pinned for this file (systemic defect 1; collisions named)

| symbol here | meaning here | collides with (file, string) | resolution |
|---|---|---|---|
| d, G, N, D | d = 4; G = SU(N), N ≥ 2; D := N² − 1 | Ξ below replaces the lane's "G" for 2-forms | G is never a 2-form here |
| L | block side, odd, ≥ 3 | — | — |
| k | the top level of a composite (Setting SC: levels 0..k, coarse field B_k); in §3 the level of the one-step problem | K = UV cutoff (RLARGE) | k ≤ K always |
| κ_i, κ_± | kernel stiffness of stage i, κ_− ≤ κ_i ≤ κ_+ (LINEAR_PACKAGE §1.3) | κ_0^{CE} = 16 log 12800 (LINEAR_PACKAGE Thm 5.1); κ_d (polymer decay); LCONV55's κ = \|n_2\| − tail | the last three are written κ_0^{CE}, κ_d, and never used |
| u_i, t_i | u_i = 1/g_i² (RLARGE "Action normalisation"), t_i := κ_iu_i | t_0 in LCONV55 G1 (a plaquette cut) | t_i is always a stiffness here |
| Q, Q_str, h, ev | linearised S4′ root map Q = Q_str − d∘h, straight average, slice functional, root evaluation (LINEAR_PACKAGE §1.2) | Q_str also names a "stripe"-free object in some files (systemic list) | as LINEAR_PACKAGE §1.2 |
| Q_2 | **new**: the 2-form map (Q_2F)(X;μν) := L⁻⁴Σ_{y∈B(X)}Σ_{p∈sq_y^{μν}}F(p), sq_y^{μν} := the L × L square of plaquettes at y | — | — |
| Ξ, Ξ_i | **new**: a level-k 2-form ("certificate") and Ξ_i := (Q_2ᵀ)^{k−1−i}Ξ (Ξ_{k−1} = Ξ, Ξ_{−1} = (Q_2ᵀ)^kΞ) | — | — |
| c_co(k), c_co | **new**: c_co(k) := [2 + 32Σ_{m=0}^{k−1}L^{−2m}/κ_{k−1−m}]⁻¹, c_co := [2 + 32L²/(κ_−(L² − 1))]⁻¹ | LARGE55 §6.2 uses c_co for the *unknown* constant of (BFT-coer); c_E (LINEAR_PACKAGE Lemma 2.7) | here c_co is this explicit number; c_E is quoted only as c_E |
| φ_M, ψ_M, φ_min | φ_M(V) := 1 − N⁻¹Re tr(V⁻¹M) (LARGE55 §0, uncentred); φ_min(M) := min_V φ_M; ψ_M := φ_M − φ_min ≥ 0 (centred) | NA-alg (b)'s "φ" is the CENTRED ψ; N5-bg's φ̂ := Nφ uses NA-alg's φ | φ is uncentred, ψ centred, everywhere here |
| 𝒩_t, 𝒩̃_t | 𝒩_t(M) := ∫e^{−tφ_M(V)}dV (Decision 4); 𝒩̃_t(M) := e^{tφ_min(M)}𝒩_t(M) = ∫e^{−tψ_M} ∈ (0, 1] | — | — |
| W_0(M), 𝔯(M) | the maximiser of Re tr(W⁻¹M) on SU(N) (NA-alg (a)); 𝔯(M) := W_0(M)⁻¹M = H_M + iθ_M1 | NA-alg writes this matrix "G" | renamed 𝔯 |
| s(V) | N⁻¹Re tr(1 − V) = (2N)⁻¹‖1 − V‖²_HS for V ∈ SU(N) (LARGE55 §0) | a (price exponent), a := m − m_1 (RW) | s is never a price |
| ρ_c | mismatch log(V_c⁻¹W_0(M̄_c(U))) (NA-alg (b), N5-sf0) | ρ(ε) (NAH1), ρ (KA-1 width) | the canonical width is ϱ |
| ϱ | canonical complex width: link width ϱg/√κ (KA-1's r = ρg/√κ) | — | — |
| 𝔖(ε) | real (U, V) with every level-k plaquette log ≤ ε (HS, principal log) and every \|ρ_c\| ≤ ε (N5-sf0 (a)'s class) | ε_0 (BFT/LARGE55 chart radius), ε_1 (RLARGE cut), ε_* (N5-sf0 threshold) | ε_* is quoted as N5-sf0's; my chart radius is ε_ch |
| G_fl | fluctuation gauge group {g : g(c_X) = 1 for every root} at the varied level | — | — |
| 𝒬_U | **new**: D(W_0∘M̄)(U), the linearised covariant averaging at a background (left-trivialised) | — | at U = 1 it is Q ⊗ 1 |
| β, τ | stripe link angle, τ = tan(β/2) (LCONV55 C0) | β_± (flow slopes), β_Wilson | β is the stripe angle only in §3.5 |

## §2. T3 / I2 — (BFT-coer): linear coercivity at the trivial background, local form, explicit c_co; then the chart

### 2.1 Setting (LINEAR_PACKAGE §1.1-§1.3, Setting SC, restated so that nothing below depends on memory)
Levels i = 0, …, k (k ≥ 1); level i is the torus Λ_i of side T·L^{k−i} in its own units; B(X) = LX + {0, …, L−1}⁴ is the
level-i block of the level-(i+1) site X, c_X = LX + o (o = (L−1)/2) its root. Fields B_i are real 1-forms on the links of Λ_i
(one Lie-algebra component; su(N) is D independent copies). ‖·‖, ⟨·,·⟩ are ℓ² over links or over plaquettes (each unoriented
plaquette once); d* := dᵀ. The **chain energy** is E(B_0, …, B_{k−1}; B_k) := ½‖dB_0‖² + Σ_{i<k}(κ_i/2)‖r_i‖², r_i := QB_i − B_{i+1},
and E_k(B_k) := inf over B_0, …, B_{k−1} (a minimiser exists). Q = Q_root, with the exact identity Q = Q_str − d∘h, where
(Q_strA)(X, μ) := L⁻⁴Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ) and h(A)(X) := avg_{σ,y}∫_{P^σ(c_X→y)}A (LINEAR_PACKAGE §1.2). This is the
quadratic part of the tree-level exponent of the soft normalised kernel (LINEAR_PACKAGE §1.3: "The normalisation 𝒩 cancels
the shrinkage |M̄| < 1, so only the distance from the polar part is charged" — consistent with CODEX_REVIEW_LARGE F1 once the
centred exponent ψ is used; see §3.1 and §4.3).

### 2.2 Four elementary lemmas (each PROVEN-HERE; re-derived from the definitions, not from the ledger)
**Lemma ST (straight intertwining).** d∘Q = Q_2∘d on 1-forms, with (Q_2F)(X; μν) := L⁻⁴Σ_{y∈B(X)}Σ_{a,b=0}^{L−1}F(y + ae_μ + be_ν; μν).
*Proof.* d∘Q = d∘Q_str − d∘d∘h = d∘Q_str. For P = (X; μν), dA′(P) = A′(X, μ) + A′(X + e_μ, ν) − A′(X + e_ν, μ) − A′(X, ν) with
A′ = Q_strA. Reindex the second term by y′ = y + Le_μ (a bijection B(X) → B(X + e_μ)) and the third by y″ = y + Le_ν: all four
become L⁻⁴Σ_{y∈B(X)} of the straight segments of the boundary of the square y + [0, L]e_μ + [0, L]e_ν, oriented
counter-clockwise; discrete Stokes on that square gives L⁻⁴Σ_yΣ_{a,b<L}dA(y + ae_μ + be_ν; μν). ∎ (The S4′ axial legs never
enter: they are the gradient d∘h, killed by d. So no contour-pairing argument is needed at linear order.)
**Lemma Q2 (Schur).** ‖Q_2F‖ ≤ L^{(4−d)/2}‖F‖, i.e. **‖Q_2‖ ≤ 1 at d = 4**. *Proof.* Q_2 connects plaquettes of one orientation;
with multiplicity, the weights of a row P sum to L⁻⁴·L⁴·L² = L² and those of a column p to L⁻⁴·#{(a, b)} = L⁻⁴·L² (for each (a, b)
the point y = z_p − ae_μ − be_ν lies in exactly one block); Schur: ‖Q_2‖² ≤ L²·L^{2−d}. ∎ (Equality is attained by constant
2-forms of one orientation at d = 4, so the bound is sharp; this is LINEAR_PACKAGE Lemma 2.2's L^{4−d}, re-derived.)
**Lemma CC (co-closed contraction).** (i) ‖Q_str‖ ≤ L⁻¹. (ii) Qᵀd* = d*Q_2ᵀ on 2-forms and d*Qᵀ = evᵀd* on 1-forms. (iii) If s is a
level-(i+1) 1-form with d*s = 0, then Qᵀs = Q_strᵀs, ‖Qᵀs‖ ≤ L⁻¹‖s‖, and d*(Qᵀs) = 0.
*Proof.* (i) Q_strA(X, μ) is L⁻⁴ times a sum of L⁵ terms, so |Q_strA(X, μ)|² ≤ L⁻³Σ_{y∈B(X), j<L}A_μ(y + je_μ)²; summing over X
counts every fine μ-link exactly L times (y ↦ y + je_μ is a bijection for each j): ‖Q_strA‖² ≤ L⁻²‖A‖². (ii) Transpose Lemma ST,
and transpose Q∘d = d∘ev on 0-forms (every contour of (X, μ) runs from c_X to c_{X+e_μ}, so Q(dλ)(X, μ) = λ(c_{X+e_μ}) − λ(c_X)).
(iii) Qᵀ = Q_strᵀ − hᵀd*, and the last factor vanishes on s; norms of an operator and its transpose agree; d*Qᵀs = evᵀd*s = 0. ∎
**Lemma DS.** ‖d*Ξ‖² ≤ 4d‖Ξ‖² = 16‖Ξ‖² on every torus. *Proof.* In Fourier, (dA)^_{μν} = ν_μÂ_ν − ν_νÂ_μ with ν_α = e^{ip_α} − 1,
and the Lagrange identity Σ_{μ<ν}|ν_μÂ_ν − ν_νÂ_μ|² = (Σ|ν_α|²)|Â|² − |Σν̄_αÂ_α|² ≤ 4d|Â|² gives ‖d‖ ≤ 2√d; ‖d*‖ = ‖d‖. ∎

### 2.3 Lemma CERT (an exact dual certificate) and Theorem LC
**Lemma CERT.** For every chain (B_0, …, B_k) and every level-k 2-form Ξ, with Ξ_i := (Q_2ᵀ)^{k−1−i}Ξ (a level-(i+1) 2-form,
i = −1, …, k−1):
  **⟨dB_k, Ξ⟩ = ⟨dB_0, Ξ_{−1}⟩ − Σ_{i=0}^{k−1}⟨r_i, d*Ξ_i⟩,**   and   **d*Ξ_i = (Qᵀ)^{k−1−i}d*Ξ.**
*Proof.* ⟨dB_{i+1}, Ξ_i⟩ = ⟨dQB_i, Ξ_i⟩ − ⟨dr_i, Ξ_i⟩ = ⟨Q_2dB_i, Ξ_i⟩ − ⟨r_i, d*Ξ_i⟩ = ⟨dB_i, Ξ_{i−1}⟩ − ⟨r_i, d*Ξ_i⟩ (Lemma ST);
telescope from i = k − 1 to 0. The second identity is Lemma CC (ii) iterated. ∎
**Theorem LC (linear coercivity, trivial background; PROVEN-HERE).** For every k ≥ 1, every torus side T and every chain,
  **E(B_0, …, B_{k−1}; B_k) ≥ c_co(k)‖dB_k‖²,  c_co(k) := [2 + 32Σ_{m=0}^{k−1}L^{−2m}/κ_{k−1−m}]⁻¹ ≥ c_co := [2 + 32L²/(κ_−(L² − 1))]⁻¹,**
hence E_k(B_k) ≥ c_co‖dB_k‖² uniformly in k, T and the κ_i ∈ [κ_−, κ_+].
*Proof.* Every intermediate form (Qᵀ)^jd*Ξ is co-closed (d*d* = 0 and Lemma CC (iii)), so ‖d*Ξ_i‖ ≤ L^{−(k−1−i)}‖d*Ξ‖ ≤
4L^{−(k−1−i)}‖Ξ‖ (Lemmas CC (iii), DS), and ‖Ξ_{−1}‖ ≤ ‖Ξ‖ (Lemma Q2). By Lemma CERT and Cauchy–Schwarz,
  |⟨dB_k, Ξ⟩| ≤ [½‖dB_0‖² + Σ_i(κ_i/2)‖r_i‖²]^{1/2}·[2‖Ξ_{−1}‖² + Σ_i(2/κ_i)‖d*Ξ_i‖²]^{1/2} ≤ E^{1/2}·c_co(k)^{−1/2}‖Ξ‖.
Take Ξ := dB_k. ∎
**Why there is no level-count factor (the mechanism, stated exactly).** Q_2 is marginal at d = 4 (‖Q_2‖ = 1, sharp), so the fine
curvature term costs a k-independent 2‖Ξ‖²; each residual r_i is paired with (Qᵀ)^{k−1−i}d*Ξ, which is co-closed, and on
co-closed forms the S4′ funnels drop out and Q_strᵀ contracts by L⁻¹ per level (Lemma CC); the level sum Σ_mL^{−2m} = L²/(L² − 1)
converges. A one-level induction cannot see this: from |⟨dB_{i+1}, Ξ⟩| ≤ ‖dB_i‖‖Ξ‖ + 4‖r_i‖‖Ξ‖ one gets only
c_{i+1} = c_i/(1 + 16c_i/κ_i), which decays like κ/(16i) — the level-count factor that the multi-level certificate removes.
**Values (exact; check st55_1 recomputes them).** κ ≡ 1, L = 3: c_co(1) = 1/34, c_co(2) = 9/338, c_co(∞) = c_co = **1/38**. LINEAR_PACKAGE
Lemma 2.7's c_E = 2κ/(π²(κ + 4π²R̄)), R̄ = 1 + κ̂/(L² − 1) + κ/9, equals 0.004069 there; so **c_co/c_E ≈ 6.47** (the rational interval is
in st55_1). The measured per-mode minima of E_k/‖dB_k‖² recorded in PROOF `Lemma E-low` (c31 E, floating point, κ ≡ 1, at
p = (π, π, π, π)) are 0.0310, 0.0297, 0.0296 for k = 1, 2, 3, against c_co(1) = 0.02941, c_co(2) = 0.02663, c_co(3) = 0.02635: the
bound is below every measured value and within 5 % of the k = 1 one. (A sharpness anchor computed exactly, independent of c31,
is check st55_1 C.)
**Consequence for N5 at the trivial background (PROVEN as an implication).** Lemma N5-coer's proof uses E-low only through
E_i(A) ≥ c_E‖dA‖² (PROOF `Lemma N5-coer`, step (2) via NA-lev (c)). Theorem LC supplies the same inequality with c_co, so for every
level i ≥ 1: **γ_i^♯ = min{2c_1L⁻²min(c_co, κ_−/2), ν_N}** (c_1 = 1/(3.5·10⁶), PG's constant, unchanged): at κ ≡ 1, L = 3 this is
2c_1/(9·38) ≈ 1.67·10⁻⁹ in place of 2.58·10⁻¹⁰ (×6.47). The bottleneck stays PG's c_1 (PROOF records the measured trivial gap 0.0397,
2.5·10⁶ above γ_0): Theorem LC removes the E-low part of that loss, not the PG part. Level 0 is unchanged (E_0 = ½‖dA‖², c_E = ½).

### 2.4 Theorem LC-loc (local charge allocation, no tails) — the form PRICE needs (PROVEN-HERE)
For a set 𝒮 of level-k plaquettes put Ξ := 1_𝒮·dB_k and define the **cone** of 𝒮: cone_{−1}(𝒮) := supp Ξ_{−1} (level-0 plaquettes)
and cone_i(𝒮) := supp d*Ξ_i (level-(i+1) links), 0 ≤ i < k. Let E_{cone(𝒮)} := ½Σ_{p∈cone_{−1}}|dB_0(p)|² + Σ_i(κ_i/2)Σ_{c∈cone_i}|r_i(c)|².
Then for every chain:
  **E_{cone(𝒮)} ≥ c_co(k)·Σ_{P∈𝒮}|dB_k(P)|².**
*Proof.* The pairings in Lemma CERT only read the chain on the supports, so Cauchy–Schwarz may be taken with the restricted
energy, and ‖Ξ‖² = Σ_𝒮|dB_k|². ∎
**Geometry.** One application of Q_2ᵀ maps a plaquette at z (orientation μν) to plaquettes with base points in Lz + [0, 2L − 2] in
the μ and ν directions and Lz + [0, L − 1] in the other two. Iterating, the level-(k − m) support of a single P = (X; μν) has
base points in L^mX + [0, 2L^m − 2]e_μ + [0, 2L^m − 2]e_ν + [0, L^m − 1]e_⊥: **the cone of P lies, at every depth, in the four
level-k blocks of P's corners (the 2 × 2 block square of P in its plane), never further.** A plaquette lies in the cones of ≤ 4
coarse plaquettes; a link in ≤ 216 (crude: 6 orientations × 3·3·2·2 base positions of the closed box).
**What this gives PRICE (CODEX_REVIEW_LARGE F9's request "a consistent decomposition E = E_S + E_rest").** For the *global*
minimising tower (no separate region, no boundary condition), E_k(B_k) = E_{cone(𝒮)} + E_{rest} with E_rest ≥ 0 the densities
outside the cone, and E_{cone(𝒮)} ≥ c_co ε_cl²·#{P ∈ 𝒮} when every P ∈ 𝒮 has |dB_k(P)| ≥ ε_cl. One certificate charges all of 𝒮
at once, so overlapping cones cost nothing; the charge of 𝒮 lives inside the 2 × 2 block squares of 𝒮 (no exponential tail).
On a region with holes the same holds for every 𝒮 whose 2 × 2 block squares avoid the holes, for the region's own minimising
tower. *Scope:* this is the **linear main term at the trivial background**; the nonlinear chart version is §2.5, and the
post-normalisation price (CODEX_REVIEW_LARGE F9's a_eff) is not touched here.

### 2.5 Theorem LC-chart (the nonlinear chart perturbation in PRICE form; PROVEN as an implication from BFT-0/1 on 𝒞_glob)
**The point that makes it short.** Lemma CERT is *linear* in the link logarithms. Take the critical tower x* = (U_0*, …, U*_{k−1})
of the tree-level composite 𝔉_k(·; V) := Σ_ps(U_0(p)) + Σ_{j<k}κ_jΣ_cψ_{M̄_c(U_j)}(U_{j+1,c}) (U_k := V; arithmetic S4′ mean M̄, centred
ψ — the composite of SRCAN55 §2.1 at ε̂ = 0 with φ̂ = Nψ), in a global gauge, and put A_j := log U_j* (principal logs, su(N)-valued).
The identity of Lemma CERT holds verbatim for (A_0, …, A_k) with the *linear* residuals r_j := QA_j − A_{j+1}. The nonlinearity
enters only through three comparisons, each a local BCH estimate:
- (a) fine plaquettes: |log U_0*(p) − dA_0(p)| ≤ 32a_0²; coarse plaquettes: |log V_P − dA_k(P)| ≤ 32a_k²;
- (b) residuals: with ρ_j(c) := log(U*_{j+1}(c)⁻¹W_0(M̄_c(U_j*))) (the kernel's own mismatch), |r_j(c) − ρ_j(c)| ≤ 19(p_L²a_j² + |ρ_j(c)|²);
- (c) energies: s(e^X) ≥ (2N)⁻¹|X|²(1 − |X|²/12) and ψ ≥ (2N)⁻¹|ρ|²(1 − 18.4y² − √N e^{|ρ|}|ρ|) (NA-alg (b)),
where a_j := max_b|A_j(b)| (HS) and y ≤ 1.1p_La_j bounds the contour logs. *Proof of (a)-(b).* For X_1, …, X_n with S := Σ|X_i|_HS ≤ ¼,
|log(e^{X_1}⋯e^{X_n}) − ΣX_i| ≤ S²e^S/2 + S²e^{2S}/(2(1 − Se^S)) ≤ 2S² (power series; HS is submultiplicative). (a) is n = 4. For (b):
each contour log Y = log T^σ_y obeys |Y − Σ_{b∈T}±A_b| ≤ 2p_L²a² (n ≤ p_L = 5L − 4 links, LINEAR_PACKAGE "every contour has ≤ p_L
links"), so |Ȳ_c − QA(c)| ≤ 2p_L²a²; NA-alg (a) gives |log W_0(M̄_c) − Ȳ_c| ≤ 9.2y²; then U*_{j+1}(c) = W_0e^{−ρ_c} and n = 2 BCH give
|A_{j+1}(c) − log W_0 + ρ_c| ≤ 2(|log W_0| + |ρ_c|)²; collect with (x + y)² ≤ 2x² + 2y² (the constants are crude). ∎
**Hypothesis (BFT-1, as banked).** [S26-BANKED] Theorem K^(σ) / GV55 Theorem BFT-E, on 𝒞_glob (data V = e^{B} with s := ‖B‖_D in one
global gauge, s ≤ ε_0, T ≥ 3, k-, T-uniform constants): the unique slice critical point x* has, with η := C_0s,
a_j ≤ L^{−(k−j)}η, level-j plaquette logs ≤ L^{−2(k−j)}(2η + 9η²), |ρ_j| ≤ L^{−(2+σ)(k−1−j)}η + CL^{−3(k−j)}η² (GV55, string
"(BFT-1)** with η := C_0s"; read there, not re-derived; I assume its ρ is the arithmetic-mean mismatch of (b), as the composite
of SRCAN55 §2.1 uses M̄).
**Theorem LC-chart.** Under that hypothesis, with p_Lη ≤ 1/40, let 𝒮 be any set of level-k plaquettes with |log V_P|_HS ≥ ε_cl for
every P ∈ 𝒮. Then the tree-level energy of the critical tower carried by the cone of 𝒮 (§2.4) obeys
  **N·𝔉^{tree}_{cone(𝒮)}(x*) ≥ (1 − θ_s)·c_co(k)·|𝒮|·(ε_cl − C_♮η²)₊²,  C_♮ := 32 + C_tot,  C_tot := 64 + 48C_R′/(L(L − 1)),
  C_R′ := 19(p_L² + 2L^{4+2σ}),**  θ_s := the relative errors of (c) (≤ 2·10⁻² when p_Lη ≤ 1/40, √Nη ≤ 10⁻²).
In particular, if ε_cl ≥ 2C_♮C_0²ε_0², the price is ≥ ¼(1 − θ_s)c_co ε_cl² per plaquette of 𝒮 — **local, with no tails, uniform in
k and T.**
*Proof.* Fix P ∈ 𝒮 and use Ξ^{(P)} := 1_P·dA_k. The remainder pairings of Lemma CERT, written for the logs, are
⟨dA_0 − log U_0*, Ξ_{−1}⟩ − Σ_j⟨r_j − ρ_j, d*Ξ_j⟩. On the cone of P there are ≤ 4L^{4k} fine plaquettes and ≤ 144L^{4(k−1−j)} level-(j+1)
links (§2.4 geometry, closed boxes); by (a), (b) and BFT-1, |r_j − ρ_j| ≤ C_R′L^{−2(k−j)}η², so ‖dA_0 − log U_0*‖_{cone} ≤ 32L^{−2k}η²·2L^{2k}
= 64η² and ‖r_j − ρ_j‖_{cone_j} ≤ 12C_R′L^{−2}η², while ‖Ξ_{−1}‖ ≤ |Ξ^{(P)}| and ‖d*Ξ_j‖ ≤ 4L^{−(k−1−j)}|Ξ^{(P)}| (Lemmas Q2, CC, DS).
Summing over j (geometric): remainder ≤ C_totη²|dA_k(P)|. By linearity the remainder of Ξ := Σ_{P∈𝒮}Ξ^{(P)} is ≤ C_totη²Σ_P|dA_k(P)|
≤ C_totη²|𝒮|^{1/2}‖Ξ‖. The main pairings are bounded as in Theorem LC by (E^{nl}_{cone})^{1/2}c_co(k)^{−1/2}‖Ξ‖ with
E^{nl} := ½‖log U_0*‖² + Σ(κ_j/2)‖ρ_j‖² on the cone. Hence ‖Ξ‖ ≤ c_co^{−1/2}(E^{nl}_{cone})^{1/2} + C_totη²|𝒮|^{1/2}, and
‖Ξ‖ ≥ (ε_cl − 32η²)|𝒮|^{1/2} by (a). Finally E^{nl} ≤ N(1 + θ_s)𝔉^{tree} on the cone by (c). ∎
**What is and is not claimed.** (i) This is the *tree-level* composite at its critical tower (Balaban's main term), not the
normalised effective density; the log-normaliser terms are O(1) per link and u-independent (§4.3, Lemma NZ-R), and their
background dependence is a one-loop correction of relative size O(1/u_j) per level — it is the coupling flow's business (the
δβ_j of (LF-UV)), not the price's. (ii) Global coercivity 𝔉_k(V) ≥ c Σ_P|log V_P|² for *all* chart V needs η *local* to each cone
(BFT-1 with BFT-3 locality); with the global η the remainder carries |𝒮|^{1/2} and is useless for sparse curvature — **NOT-VERIFIED**
in that form; the PRICE form above does not need it. (iii) Off 𝒞_glob (holes with holonomy, large tori without a global small gauge)
the hypothesis is not banked (OFFGLOB55: "Theorem OFF NOT (GAP)"); there the theorem is conditional on BFT-0/1 on the region.
(iv) The parameter order it imposes: ε_cl ≥ 2C_♮C_0²ε_0², compatible with LARGE55 E15's ε_cl ≤ ε_0/((1 + 4C_δ)L²) iff
ε_0 ≤ [2C_♮C_0²(1 + 4C_δ)L²]⁻¹ — a smallness condition on ε_0 only (no cycle).

## §3. T1 / I1 (a) — one-step conditional positivity: the exact action, the chart and metric, why the stripe cannot obstruct

### 3.1 The exact one-step action (CODEX_REVIEW_LARGE F1 incorporated)
The soft chain is Markov in the level index with exact kernels ([S26-BANKED] SRC Proposition B). Given U_{k+1} = V, the law of
U = U_k has density ∝ ρ_k(U)·Π_ck_{t_k}(V_c; M̄_c(U)) with k_t(V; M) = e^{−tφ_M(V)}/𝒩_t(M) = e^{−tψ_M(V)}/𝒩̃_t(M) (centre the
exponent: e^{−tφ} = e^{−tφ_min}e^{−tψ} and 𝒩_t = e^{−tφ_min}𝒩̃_t). Hence, exactly,
  **S_eff(U; V) := −log ρ_k(U) + Σ_c[t_kψ_{M̄_c(U)}(V_c) + log 𝒩̃_{t_k}(M̄_c(U))] + const(V).**
At level 0, −log ρ_0 = u_0Σ_ps(U_p), so S_eff = (u_0/N)[S_W(U) + κ_0Σ_cφ̂_c] + Σ_clog 𝒩̃_{t_0}(M̄_c(U)) with S_W = Re tr Σ(1 − U_p) and
φ̂ := Nψ — PROOF `Setting N5-bg`'s normalisation. So
  **Hess S_eff = (u_0/N)·H_tree + H_𝒩,  H_tree := Hess[S_W + κ_0Σ_cφ̂_c],  H_𝒩 := Hess Σ_clog 𝒩̃_{t_0}(M̄_c(U)).**
LARGE55 §3 (h1)'s "S + Σκuφ" omitted Σlog 𝒩 (CODEX_REVIEW_LARGE F1: **agree**). What the omission costs is quantified in §4.3:
log 𝒩̃_t(M) depends on M only through the polar-free matrix 𝔯(M) = W_0(M)⁻¹M and is O(1)-smooth there uniformly in t (Lemma
NZ-R), so ‖H_𝒩‖ ≤ C_𝒩(N, L) on the chart, u-independent: relative to (u_0/N)H_tree it is O(N C_𝒩/u_0) = O(g_0²). *Explicitly for
SU(2)* (§4.4): 𝒩̃_t(M) = e^{−t|M|}·2I_1(t|M|)/(t|M|), |M| the quaternion norm, so log 𝒩̃ = −(3/2)log(t|M|) + O(1) + O(1/(t|M|)): the
normaliser cancels the O(t) shrinkage term and leaves an O(1) function of the contour variance. The background of S_eff differs
from the tree-level background by O(1/u). **Every positivity statement below is for (u_0/N)H_tree; the exact Hessian is then
positive once u_0 ≥ 2NC_𝒩/λ, λ the tree-level gap — a weak-coupling condition, not a new smallness of the chart.**

### 3.2 The chart and the metric (answer to coordinator notice N1)
- **Variables.** Only the level-k field U = U_k; the coarse field V = U_{k+1} is FIXED (conditioning); finer levels are already
  integrated into ρ_k.
- **Metric and chart.** The product of bi-invariant (Hilbert–Schmidt) metrics on SU(N)^{links}; coordinates: left-trivialised
  exponential coordinates at the *current* configuration, U_b → e^{A_b}U_b, A ∈ ⊕_bsu(N) (PROOF `Setting N5-bg`). For a product of
  bi-invariant metrics these are Riemannian normal coordinates at that point, so the coordinate Hessian there **is the
  Riemannian Hessian**, at critical and non-critical points alike.
- **Gauge.** The fluctuation gauge group G_fl := {g : g(c_X) = 1 at every root} acts isometrically and preserves S_eff(·; V)
  (M̄_c(g·U) = g(c_X)M̄_c(U)g(c_{X+e_μ})⁻¹ = M̄_c(U)). Two equivalent ways to remove it: (i) **chart-free:** the Riemannian Hessian
  of the quotient U/G_fl, which equals the Riemannian Hessian on G_fl-horizontal vectors (O'Neill: for an invariant f and a
  horizontal X, Hess f(X^h, X^h) = Hess f̄(X, X), because ∇_{X^h}X^h = (∇̄_XX)^h; no gradient term) — this is the object of LCONV55 C2;
  (ii) **the consumer's chart:** the lane's gauge-fixed operator Õ(U, V) = Π_U[H_tree + D_UP_res^UD_Uᵀ]Π_U + (1 − Π_U) (linear slice
  h_U = 0 plus residual fixing), whose inverse minus (1 − Π_U) is the per-step covariance. At a critical point (the background)
  (i) and (ii) have the same inertia (NA-crit/NA-FP); at a non-critical point (e.g. the stripe) both are stated below.
- **Contrast with LCONV55 Theorem NC.** NC is about the *joint* chain (coarse fields free) in level-0-normal horizontal slices;
  its negative directions are *following* directions τ = (τ_0, 𝒬τ_0, 𝒬²τ_0, …), along which every kernel contributes exactly zero
  (Lemma FOL, CONFIRMED by Codex R6). A following direction is not a direction of the one-step problem: there V is fixed, so the
  same τ_0 moves 𝒬τ_0 away from V and the kernel charges it (Codex R6's κu r|b|²).

### 3.3 Lemma PSD (the kernel's Hessian at zero mismatch, exactly; PROVEN-HERE)
Fix V and a coarse link c, and let U be a point where W_0(M̄_c(U)) is the unique, non-degenerate maximiser (NA-alg (a): contour
logs ≤ y ≤ 1/20 in some gauge) and the mismatch vanishes, V_c = W_0(M̄_c(U)). Then for every tangent vector v,
  **Hess_U φ̂_c[v] = tr(ρ′*ρ′H_c) ≥ (1 − 18.4y²)·|𝒬_Uv(c)|²_HS,  ρ′ := Ad(V_c⁻¹)𝒬_Uv(c),**
where 𝔯(M̄_c) = H_c + iθ_c1 (NA-alg (a)) and 𝒬_U := D(W_0∘M̄)(U) (left-trivialised). In particular the kernel's Hessian is ≥ 0 and
vanishes exactly on the coarse-invisible directions ker 𝒬_U.
*Proof.* Along a curve U(t), put ρ(t) := log(V_c⁻¹W_0(M̄_c(U(t)))) (traceless, ρ(0) = 0) and 𝔯(t) := 𝔯(M̄_c(U(t))) = H(t) + iθ(t)1
(stationarity of W_0 at every t). Then φ̂_c = Re tr((1 − e^{ρ})𝔯) exactly (NA-alg (b)'s identity times N). Re tr(ρ𝔯) = Re tr(ρH) −
θ·Im tr ρ = 0 for every t (ρ anti-Hermitian traceless, H Hermitian), so φ̂_c = −Re tr((e^ρ − 1 − ρ)𝔯) = −½Re tr(ρ²𝔯) + O(|ρ|³);
with ρ(t) = tρ′ + O(t²), φ̂_c″(0) = −Re tr(ρ′²𝔯(0)) = tr(ρ′*ρ′H) − Re(iθ tr ρ′²) = tr(ρ′*ρ′H) (tr ρ′² is real). λ_min(H) ≥ 1 − 18.4y²
(NA-alg (a)). Finally V_c⁻¹W_0(t) = V_c⁻¹e^{t𝒬v + O(t²)}V_c, so ρ′ = Ad(V_c⁻¹)𝒬_Uv(c), and Ad is an isometry. ∎
*Away from zero mismatch* the same computation gives an extra term −Re tr(dexp_ρ(ρ″)𝔯) + (terms with 𝔯′, 𝔯″) whose size is
O(|ρ_c|)·(local norm of v)² — so Hess φ̂_c ≥ (1 − 18.4y² − C_ρ|ρ_c|)|𝒬_Uv(c)|² − C′_ρ|ρ_c|·‖v‖²_{contours of c} with C_ρ, C′_ρ depending on
(N, L) through the real-analyticity of W_0 (NA-alg (a), N5-an); the constants are not computed here.
**Reading.** In the one-step chart every coarse-visible direction pays at least κ_0(1 − 18.4y²)|𝒬_Uv|² — the *soft-constraint
mass* — and every coarse-invisible direction (𝒬_Uv = 0) sees only the main term.

### 3.4 Proposition OSS ("one step sees one scale" — exact, at the trivial background; PROVEN-HERE)
Take the constant holonomy direction τ_0 := c·e_μ on level 0 (dτ_0 = 0; it is the zero-curvature limit of the stripe's negative
directions, LCONV55 D1/C4: "the three wall-to-wall holonomy directions"). Q_root(const) = L·const exactly (every contour of (X, μ)
has net μ-displacement L and net zero in the other directions; check st55_1 C0).
- **One-step (V fixed):** the tree-level Hessian d*d + κ_0QᵀQ has Rayleigh quotient **κ_0‖Qτ_0‖²/‖τ_0‖² = κ_0L⁻²** on τ_0 (‖Qτ_0‖² =
  L²c²·#level-1 μ-links, ‖τ_0‖² = c²·L⁴·#level-1 μ-links).
- **Joint chain with levels 0..K free and level K + 1 fixed, along the following direction τ = (τ_0, Qτ_0, …, Q^Kτ_0):** every kernel
  but the top one vanishes on τ, so the Hessian is κ_K‖Q^{K+1}τ_0‖², and with ‖Q^lτ_0‖² = L^{−2l}‖τ_0‖² the Rayleigh quotient is
  **κ_KL^{−2(K+1)}/Σ_{l=0}^{K}L^{−2l} → 0** (K → ∞).
So the same holonomy direction has an O(1) one-step mass κ_0/L² (= κ_0/9 at L = 3) and an arbitrarily small joint mass.
LCONV55's stripe adds a negative term of size ≈ −c_strβ²‖τ_0‖² (spin coupling of charged modes; second order in the fine field;
c_str ≈ 2-7 in β² units by LCONV55 C2-C4, i.e. 11/6 … 7/32·… in plaquette-cut units per Codex R8): **it beats the joint mass
for every β once K is large, and never beats the one-step mass while c_strβ² < κ_0/L² (up to the O(β) corrections computed
in §3.5).** This is the precise content of "one step sees one scale": with V fixed, every direction with a non-zero block
average (scale ≥ one block) carries the kernel's mass, and the only directions without it are coarse-invisible (scale < one
block), where the main term's within-block Poincaré gap acts.

## §4. The zero-free normaliser (coordinator notice N2; CODEX_REVIEW_LARGE F3's "most dangerous" item)

Two different objects must be kept apart: (A) the **single kernel normaliser** 𝒩_t(M̄_c(U)) — it sits in the denominator of every
normalised kernel, so analyticity of anything in the FINE field (the one-step integrand, sources entering through u_0, the
coupling as a spectator) needs it zero-free; (B) the **denominators of normalised returned activities**, integrals over inner
configurations of superpositions of kernels — CODEX_REVIEW_LARGE F3's mixture is of this type. §4.1-§4.3 settle (A) on a FIXED
(t-independent) complex neighbourhood; §4.4 re-derives Codex's mixture zero; §5.4 reduces (B) to the per-step cluster expansion.

### 4.1 Lemma INV (complex Haar invariance; PROVEN-HERE, elementary)
If f is holomorphic on a neighbourhood of SU(N)·SL(N, ℂ) in M_N(ℂ) (in particular entire) and g ∈ SL(N, ℂ), then
∫_{SU(N)}f(gV)dV = ∫_{SU(N)}f(Vg)dV = ∫_{SU(N)}f(V)dV.
*Proof.* Polar decomposition g = k·e^{iX}, k ∈ SU(N), X ∈ su(N); Haar invariance handles k. Put F(σ) := ∫f(e^{iσX}V)dV and
h_σ(V) := f(e^{iσX}V). For Y ∈ su(N), ∫(D_Yh_σ)(V)dV = d/dε∫h_σ(e^{εY}V)dV = 0 (left invariance), where D_Yh(V) := d/dε h(e^{εY}V)|_0;
since h_σ is holomorphic, Y ↦ D_Yh_σ is complex-linear, so ∫D_{iX}h_σ = i∫D_Xh_σ = 0. And F′(σ) = ∫(D_{iX}f)(e^{iσX}V)dV =
∫(D_{iX}h_σ)(V)dV (e^{εiX} commutes with e^{iσX}) = 0. So F(1) = F(0). Right multiplication: the same with f(V·). ∎

### 4.2 The holomorphic normaliser and its polar recentring
For (M, M̃) ∈ M_N(ℂ)² put Φ(V; M, M̃) := 1 − (2N)⁻¹[tr(V⁻¹M) + tr(M̃V)] and 𝒩_t(M, M̃) := ∫_{SU(N)}e^{−tΦ(V; M, M̃)}dV — entire in
(M, M̃), equal to Decision 4's 𝒩_t(M) on real data M̃ = M*. The fine-field continuation is M = M̄_c(U^ℂ) := avg_jT_j(U^ℂ),
M̃ = M̃_c(U^ℂ) := avg_jT_j(U^ℂ)⁻¹ (holomorphic in U^ℂ ∈ SL(N, ℂ)^{links}, equal to M̄_c(U), M̄_c(U)* on real U since T⁻¹ = T*).
**Corollary INV.** For every W ∈ SL(N, ℂ): 𝒩_t(M, M̃) = 𝒩_t(W⁻¹M, M̃W). (Φ(V; M, M̃) = Φ(W⁻¹V; W⁻¹M, M̃W); apply Lemma INV.)
**Lemma PR (complex polar recentring; PROVEN-HERE).** Let M_0 be real with NA-alg (a)'s data M_0 = W_0𝔯_0, 𝔯_0 = H_0 + iθ_01,
δ_0 := ‖𝔯_0 − 1‖_op ≤ 1/40, and (M, M̃) = (M_0 + δM, M_0* + δM̃) with |δ| := ‖δM‖_op + ‖δM̃‖_op ≤ 1/40. Then there is a unique
Y ∈ sl(N, ℂ) with ‖Y‖_op ≤ 2|δ| such that, with W := W_0e^Y, 𝔯 := W⁻¹M = 1 + E and 𝔯̃ := M̃W = 1 + Ẽ, **the traceless part of
E − Ẽ vanishes**: E − Ẽ = 2iϑ1, ϑ ∈ ℂ; moreover ‖E‖, ‖Ẽ‖ ≤ δ_0 + 3.3|δ| and |ϑ| ≤ δ_0 + 3.3|δ|.
*Proof.* With A := W_0⁻¹M, Ã := M̃W_0 (‖A − 1‖, ‖Ã − 1‖ ≤ δ_0 + |δ|), the condition is P_0[e^{−Y}A − Ãe^Y] = 0 (P_0 the traceless
projection, ‖P_0‖ ≤ 2). Since P_0(A − Ã) = P_0(W_0⁻¹δM − δM̃W_0) (P_0(2iθ_01) = 0), the condition reads Y = Ψ(Y) :=
½P_0[(A − Ã) − Y(A − 1) − (Ã − 1)Y + R(Y)], R(Y) := (e^{−Y} − 1 + Y)A − Ã(e^Y − 1 − Y), ‖R(Y)‖ ≤ 1.05‖Y‖²e^{‖Y‖}. On ‖Y‖ ≤ 2|δ|:
‖Ψ(Y)‖ ≤ |δ| + 2(δ_0 + |δ|)·2|δ| + 4.3|δ|² ≤ 2|δ|, and Lip(Ψ) ≤ 2(δ_0 + |δ|) + 4.4·2|δ| ≤ ½. Banach's fixed point; the bounds on
E = e^{−Y}A − 1, Ẽ = Ãe^Y − 1 follow from ‖e^{±Y} − 1‖ ≤ 2.1|δ|·1.06. ∎

### 4.3 Lemma NZ (zero-free normaliser on a fixed neighbourhood, uniformly in t; PROVEN-HERE with the geometric constant K_N)
*Constants.* s(V) := N⁻¹Re tr(1 − V) on SU(N). Two facts: (i) **|Im tr V| ≤ C_Ns(V)** with C_2 = 0 and C_N := N(N² + 2)/2
(eigenvalue angles θ_j, Σθ_j ∈ 2πZ: |Σ sin θ_j − sin Σθ_j| ≤ Σ_j4|sin(θ_j/2)||sin(Θ_{j−1}/2)| with Θ_{j−1} the partial sums, by the
two-angle identity sin a + sin b − sin(a + b) = 4 sin(a/2) sin(b/2) sin((a + b)/2); then |sin(Θ/2)| ≤ Σ|sin(θ_i/2)| and
Σ(1 − cos θ_j) = 2Σsin²(θ_j/2)); (ii) **A_N := sup_{λ>0}λE_λ[s] < ∞**, E_λ the law ∝ e^{−λs(V)}dV (for λ ≤ ½ trivially ≤ 1; for
λ ≥ ½ by integration by parts with the two-sided Haar-volume bounds c′_Nr^{D/2} ≤ Haar{s ≤ r} ≤ C′_Nr^{D/2}, r ≤ 2:
A_N ≤ e(C′_NΓ(D/2 + 2) + 2)/c′_N; for SU(2), A_2 = sup_λ[λ(1 − I_0(λ)/I_1(λ)) + 2], whose λ → ∞ limit is 3/2 = D/2). Put
**K_N := A_N2^{A_N+1}** — then E_λ[λs·e^{ελs}] ≤ K_N for every λ > 0 and 0 ≤ ε ≤ ½ (from d log Z_1/dλ = −E_λ[s] ≥ −A_N/λ, i.e.
Z_1((1 − ε)λ)/Z_1(λ) ≤ (1 − ε)^{−A_N}, and E_λ[λs e^{ελs}] = (1 − ε)⁻¹(Z_1((1 − ε)λ)/Z_1(λ))·E_{(1−ε)λ}[(1 − ε)λs]).
**Statement.** In the setting of Lemma PR put ε_E := ‖(E + Ẽ)/2‖_op + C_N|ϑ|/N ≤ (1 + C_N/N)(δ_0 + 3.3|δ|). Then for every t > 0
  **𝒩_t(M, M̃) = e^{tc_0/(2N)}·𝒩_t(1, 1)·Z,  c_0 := tr E + tr Ẽ,  |Z − 1| ≤ K_Nε_E.**
Hence, if (1 + C_N/N)(δ_0 + 3.3|δ|) ≤ 1/(2K_N): 𝒩_t(M, M̃) ≠ 0, log 𝒩_t is holomorphic there, and the **centred** normaliser
𝒩̃_t := e^{tφ_min^ℂ}𝒩_t, φ_min^ℂ := Φ(W; M, M̃) = −c_0/(2N) (the holomorphic continuation of φ_min), obeys
  **|log 𝒩̃_t(M, M̃) − log 𝒩_t(1, 1)| ≤ 2K_Nε_E ≤ log 2·(4/3),  uniformly in t > 0.**
*Proof.* By Corollary INV, 𝒩_t(M, M̃) = 𝒩_t(1 + E, 1 + Ẽ). Expand: Φ(V; 1 + E, 1 + Ẽ) = s(V) − c_0/(2N) + R(V) with
R(V) := (2N)⁻¹[tr((1 − V⁻¹)E) + tr(Ẽ(1 − V))] = (2N)⁻¹[tr(E_s(2 − V − V*)) + iϑ tr(V − V*)], E_s := (E + Ẽ)/2 (the two ϑ-terms combine
because E − Ẽ = 2iϑ1 — **this is where the recentring is used: no term linear in log V survives**). On SU(N), 2 − V − V* ≥ 0 with
trace 2Ns(V), so |tr(E_s(2 − V − V*))| ≤ 2N‖E_s‖s(V); and |tr(V − V*)| = 2|Im tr V| ≤ 2C_Ns(V). So |R| ≤ ε_Es(V) and
Z := E_t[e^{−tR}] obeys |Z − 1| ≤ E_t[t|R|e^{t|R|}] ≤ ε_EE_t[ts e^{ε_Ets}] ≤ K_Nε_E. Finally φ_min^ℂ = Φ(1; 1 + E, 1 + Ẽ) =
−c_0/(2N), so 𝒩̃_t = 𝒩_t(1, 1)Z, and |log Z| ≤ 2|Z − 1| for |Z − 1| ≤ ½. ∎
**What this settles.** (1) **The single normaliser has no zeros on a fixed complex neighbourhood of the chart, uniformly in t**:
in the fine field, U^ℂ = (e^{Z_b}U_b) with ‖Z_b‖_op ≤ α moves (M, M̃) by |δ| ≤ 2(e^{p_Lα} − 1) (each transporter has ≤ p_L factors),
so Lemma NZ holds on the link width **α_NZ := (1/p_L)log(1 + r_NZ/2), r_NZ := min{1/40, (1/(2K_N(1 + C_N/N)) − δ_0)/3.3}** — a
g-independent width (positive as soon as δ_0 < 1/(2K_N(1 + C_N/N)); on the chart δ_0 ≤ 18.4y² is as small as one likes).
The canonical width ϱg/√κ is far inside it. (2) **The normalised kernel is holomorphic (no poles) on that neighbourhood**;
its modulus still grows like e^{O(tα²)} there (the real part of s(W⁻¹V) can be as low as −O(|Im Y|²)), the same structure as
Lemma KA — so *bounds* are g-independent only at canonical width (or when paid by an activity's price), while *holomorphy* holds
at fixed width. (3) **Lemma NZ-R (the normaliser's Hessian is O(1), u-independent).** On the real chart, f_c(U) :=
log 𝒩̃_t(M̄_c(U)) − log 𝒩_t(1, 1) is the restriction of a function holomorphic on the link polydisc of radius α_NZ and bounded
there by 2K_Nε_E ≤ 1; Cauchy's estimate gives |∂_A∂_{A′}f_c| ≤ 2/α_NZ² for unit directions A, A′ on any two links, every t.
With N5-loc's "a fine link lies in contours of ≤ 8 coarse links" and n_c := the number of links read by one coarse link's
contours, **‖H_𝒩‖_{N_0} ≤ C_𝒩 := 16n_c/α_NZ²**, independent of t and of u. This is the bound §3.1 uses: the exact one-step
Hessian is (u_0/N)H_tree + O(C_𝒩), so CODEX_REVIEW_LARGE F1's correction changes the gap by O(g_0²) only.

### 4.4 The two exact SU(2) facts (checks of the mechanism; derivations elementary)
- **The SU(2) normaliser in closed form.** For SU(2), averages of SU(2) matrices are real quaternions; with V ↔ v ∈ S³ and the
  complexified quaternions m, m̃ of (M, M̃), tr(V⁻¹M) + tr(M̃V) = 2v·(m + m̃), and ∫_{S³}e^{v·x}dσ(v) = Σ_n(x·x)^n/(4^nn!(n + 1)!) =
  2I_1(√(x·x))/√(x·x). So **𝒩_t(M, M̃) = e^{−t}·Φ_2(t²ς), Φ_2(w) := 2I_1(√w)/√w, ς := (m + m̃)·(m + m̃)/4**; on real data ς = |m|²
  and 𝒩̃_t = e^{−t|m|}2I_1(t|m|)/(t|m|) (the formula quoted in §3.1). Φ_2 is entire and vanishes exactly at w = −j_{1,n}² (zeros of
  I_1 at ±ij_{1,n}, j_{1,1} ≈ 3.83): **the SU(2) normaliser vanishes only where t²ς lies on the negative real axis beyond
  −j_{1,1}²; on the chart ς ≈ 1, so Re ς > 0 is a zero-free neighbourhood of size O(1)** — consistent with Lemma NZ's fixed width.
- **Codex's mixture zero, re-derived (AGREE).** For D(V) := ½[k_t(V; H) + k_t(V; −H)] with H = diag(i, −i) ∈ SU(2): φ_{±H}(V) =
  1 ∓ q(V), q(V) := ½Re tr(V⁻¹H), and 𝒩_t(H) = 𝒩_t(−H) (bi-invariance), so D = e^{−t}cosh(tq(V))/𝒩_t(H) on SU(2). Continue V = e^X,
  X = diag(r, −r): ½tr(e^{−X}H) = ½(ie^{−r} − ie^{r}) = −i sinh r, so D ∝ cos(t sinh r), which vanishes at **r = asinh(π/(2t))** while
  each numerator does not. The zero comes from two kernels whose centres ±H are at distance O(1), interfering at imaginary
  displacement O(1/t). It is a statement about superpositions with spread centres (object (B)), not about a normaliser
  (object (A)), which by Lemma NZ has no zeros within a fixed distance.

### 3.5 The stripe in the one-step chart, exactly (check st55_2; criteria first; all gates PASS, both controls fired)
SU(2), L = 3, κ_0 = 1, fine torus side 6, V ≡ 1, stripe S(3, β) (direction-1 links exp(i a(x_0 mod 3)σ_3), a = (β, 0, −β)),
τ = tan(β/2). Subspaces: S_{(0)} (fields depending only on x_0 mod 3; 36 dims) and S_{(0,1)} (on (x_0, x_1) mod 3; 108 dims), and
H_red := their G_fl-horizontal parts (exactly the part orthogonal to the in-class gauge directions, by averaging over the
translations that fix the class; dims 28 and 82 at τ > 0). Normalisation: S_W = ΣRe tr(1 − U_p), φ̂ = Nψ, Euclidean |v|².
- **G0** zero mismatch: every M̄_(0,μ) is a positive scalar, r = (1 + 2cos3β)/3 in the stripe direction (2733299/3090903 at
  τ = 1/10, reproducing LCONV55 C1 and Codex R4), 1 otherwise — so V ≡ 1 is the stripe's following field and Lemma PSD applies.
- **G1** the bare Hessian along Codex R2's vector v_C (transplanted to the torus) is **exactly −27648τ²(2 + s⁻²)** (= 2 × 432 cells ×
  Codex's per-cell −32τ²(2 + s⁻²)), and v_C ∈ H_red. RQ_bare(v_C) = −0.00852, −0.0528, −0.2047 at τ = 1/50, 1/20, 1/10
  (decimal readings of the exact rationals in st55_2_out.txt; ≈ −21τ², i.e. 2 × Codex's −10.67τ²).
- **G2** the bare Hessian is negative on H_red at every tested τ > 0 (the joint chain's Hessian along the following lift of
  v_C, by Lemma FOL).
- **G3** the one-step Hessian H_cond = H_bare + κ_0H_ker is **positive definite on H_red(0) and on H_red(0, 1) at τ = 1/50 and
  τ = 1/20**, with certified lower bounds on its minimum Rayleigh quotient **0.191 (τ = 1/50) and 0.062 (τ = 1/20)**, against
  **0.222 = 2κ_0/L²** at τ = 0 (the kernel's pinning of the constant holonomies, Proposition OSS in this normalisation).
- **Reported, no prediction made: at τ = 1/10 (β ≈ 0.199, plaquette angles up to 2β ≈ 0.40) H_cond is NOT positive definite on
  either subspace**, although RQ_cond(v_C) = +0.029 > 0: the optimised stripe direction beats the kernel's mass there.
- Controls: C1 (κ_0 = 1/10, τ = 1/20) H_cond not PSD (v_C certifies) — fired; C2 (τ = 0) bare PSD with a 12-dimensional kernel
  (the constant holonomies) and H_cond PD — as designed.
**Reading (quantitative "one step sees one scale").** On the stripe's own subspaces the kernel's mass 2κ_0/L² (= κ_0L⁻² in HS
units) is eroded by the stripe at a rate ≈ (60-80)τ² (from the certified bounds: 0.222 − 0.191 ≤ 78τ² at τ = 1/50, 0.222 − 0.062 ≤
64τ² at τ = 1/20), so positivity on these subspaces holds for τ ≲ 0.06√κ_0 (β ≲ 0.12√κ_0) and fails by τ = 0.1 at κ_0 = 1. This
is the explicit form of LARGE55 §5.4's "cβ² < κ" (Codex LCONV R8's caution about units applies: here β is the link angle, the
plaquette-norm cut is ≈ 2β). It is not a defect of the one-step method: the lane's chart radii are ~10⁻¹³/C_Δ (N5-sf0) or below,
far inside the window; it is a **quantified lower bound on how small the chart must be**, which no earlier file stated.
*Scope of the check.* It tests the stripe's subspaces only, not the full space; the full-space statement for small enough β
is Theorem 1S-0 (a). The exact one-step Hessian adds H_𝒩 = O(1) (§4.3), i.e. a relative O(g_0²) change, not included here.

### 3.6 Theorem 1S-0 (level 0: one-step conditional positivity on the whole small-field class, regions with collars)
(a) **[Tree level; CONFIRMED — pre-S24 Theorem N5-sf0 (b) with Proposition RW-ℓ², load-bearing step re-derived.]** For T ≥ T_0 and
every real (U, V) ∈ 𝔖(ε), ε ≤ ε_*, λ_min(Õ(U, V)) ≥ λ_* := γ′(1 − ε_R)/9 > 0. *Re-derivation of the positivity step:* on each
R_*-box the compression of Õ is, in N5-cov's local gauge, Õ(1, 1)_{Ω_□} + Δ_□ with Õ(1, 1)_{Ω_□} ≥ γ_0 (Rayleigh, N5-triv/N5-coer) and
‖Δ_□‖ ≤ C_Δα_* < γ_0 (N5-an), so CT♯ gives (RW1); with (RW2) the walk series for (Õ + t)⁻¹ converges for every t ≥ 0, so no
eigenvalue of the real symmetric Õ reaches 0 — positivity. I agree with REVIEW_S18_S19's CONFIRMED-WITH-FIX; the constants
r_*, S_* (hence C_Δ, ε_*) are existence constants, not computed. **This is the theorem LCONV55 §G2 lacked (Codex LCONV R9:
"no one-step theorem … is proved here" — correct of LCONV55, but it existed at level 0 since session 19).** It covers
non-critical points: the stripe S(3, β) with V ≡ 1 has plaquette logs ≤ 2√2β (HS) and zero mismatch, so it is in 𝔖(2√2β) and
Õ(stripe, 1) ≥ λ_* once 2√2β ≤ ε_*.
(b) **[Exact action; PROVEN as an implication from (a) and Lemma NZ-R.]** The exact gauge-fixed one-step Hessian
(u_0/N)Õ + Π_UH_𝒩Π_U is ≥ (u_0/N)λ_* − C_𝒩 > 0 for u_0 > NC_𝒩/λ_*, uniformly in T ≥ T_0 and on all of 𝔖(ε).
(c) **[Regions, collars, holes; PROVEN as an implication under (FILL), NOT-VERIFIED otherwise.]** Let Λ be a union of level-0
blocks with a collar of width ≥ 2 blocks, so that every entry Õ(b, b′), b, b′ ∈ Λ, reads only fields in Λ⁺ (PROOF `Setting
N5-bg`: entries read the blocks at ℓ^∞ distance ≤ 2). (FILL): the fields on Λ⁺ extend to a real configuration in 𝔖(ε) on the
whole torus. Under (FILL), the compression Õ_Λ satisfies Õ_Λ ≥ λ_* (Rayleigh), uniformly in Λ and its holes. (FILL) holds when
every hole H with its collar is a box B whose collar admits a gauge with links ≤ a, a small (set the H-links to 1 in that gauge:
plaquettes in B are ≤ 32a² + 4a by BCH). It can FAIL when the collar of a hole carries holonomy around a loop that is not
contractible in Λ⁺ (in d = 4: a loop linking a closed 2-surface inside H — e.g. a frozen centre-vortex sheet); then no small
extension exists and neither the compression argument nor N5-sf0's local-gauge proof applies. **Positivity on such regions is
NOT-VERIFIED** (I expect it to hold — Dirichlet data and κ-pinning do not create zero modes — but have no proof; a covering
argument works only for amenable π_1). This is a genuine gap in "uniformly in the holes", stated precisely.
(d) **[What is not claimed.]** Nothing here is explicit in r_*, S_*; the explicit window of §3.5 is on subspaces only.

### 3.7 Levels k ≥ 1 (N5 at levels ≥ 1): reduction, the trivial-background case, and the exact missing input
**Proposition 1S-k (PROVEN as an implication).** At a level-k background (bg, V) put Õ_k := Π[Hess 𝓔_k(bg) + κ_kHess Σφ̂_c(V; M̄_c(·))
+ fixing]Π + (1 − Π) (N5-sf_i's operator with the main term 𝓔_k). Suppose
- (HC_k) Hess 𝓔_k(bg)[δ] ≥ (1 − θ)c_co‖D_{bg}δ‖² − θ′‖δ‖² on the level-k slice (Hessian-form coercivity of the main term), and
- the one-level inputs at (bg, V): zero or small mismatch (Lemma PSD with its O(|ρ|) term), and PG transferred to the covariant
  one-level Phys at n = L (finite-dimensional per block; NA-lev (d)'s "argued" step).
Then Õ_k ≥ ½min((1 − θ)c_co, κ_k(1 − 18.4y²)/4)c_1L⁻² − θ′ − O(|ρ| + y²) − (PG transfer error), and the exact one-step Hessian adds
O(C_𝒩) (Lemma NZ-R). *Proof.* NA-lev (c)-(d)'s argument with (HC_k) in place of E-low and Lemma PSD in place of the expansion
|Q_UA − Def|² (which Lemma PSD makes exact at zero mismatch). ∎
**(HC_k) at the trivial background: PROVEN** — it is Theorem LC (Hess E_k = 2E_k's form; θ = θ′ = 0), so N5 at the trivial background
holds at every level with the improved γ_i^♯ of §2.3.
**(HC_k) on the chart: ARGUED, with the missing input named exactly.** Write Hess 𝓔_k(bg)[δ] = min over the finer variables of the
multilevel Hessian at the critical tower x* (Schur complement; needs one-step positivity at all finer levels — an induction in
k). Lower-bound the multilevel Hessian term by term: the Wilson part ≥ ½|D_0δ_0|²(1 − C|F_0|) − C|F_0||δ_0|² (spin term, level 0 only);
each kernel part ≥ κ_j(1 − 18.4y_j² − C|ρ_j|)|L_jδ|² − Cκ_j|ρ_j||δ|²_{loc} (Lemma PSD); then the certificate of Lemma CERT in its
gauge-covariant form, whose defect is proportional to the background curvature. Evaluate the error terms at the minimising
extension δ*_j of δ: with BFT-1 (curvature ≤ C_1L^{−2(k−j)}η, mismatch ≤ C_1L^{−(2+σ)(k−1−j)}η) and **(B2) ‖δ*_j‖_{ℓ²} ≤ C_2L^{k−j}‖δ‖**, the
three error sums are ≤ Cη‖δ‖² (spin, one level), Σ_jL^{−(2+σ)(k−j)}L^{2(k−j)} = O(1) (mismatch; **summable because σ > 0**), and
Σ_jL^{−2(k−j)}L^{k−j} = O(1) (certificate defects): no level-count factor. (B1) = BFT-1 is banked conditionally on 𝒞_glob;
**(B2) is the missing input**: the ℓ² form, with the sharp own-units weight L^{k−j}, of the derivative of the background map
V ↦ x*(V). It would follow from BFT-2 (Cauchy in sup norm gives ‖∂x*_j‖_{∞→∞} ≤ C_0L^{−(k−j)}, the θ_A = 1 weight) together with an
exponential locality of that derivative carrying the same weight (a BFT-3-type statement); I have not checked that BFT34_55's
banked locality has this weight. **Status: ARGUED; the uniform-in-k one-step positivity at chart backgrounds at levels ≥ 1
remains CONDITIONAL on (B2), on BFT-0/1 off 𝒞_glob for regions with holes, and on the per-block PG transfer.** This sharpens
PROOF's (BG-unif): only a *lower* Hessian bound with summable defects is needed, not (BG-unif)(iv)'s two-sided Lipschitz bound,
and the k-uniformity mechanism is the same as in Theorem LC (co-closed contraction + σ > 0).

## §5. T2 / I1 (b), N6 — the per-step cluster expansion: an implication with every hypothesis named

### 5.1 Setting (the soft-scheme transcription of Dimock 1108.1335 §4.4-§4.6; cited as the template, not as an input)
One step at level k on a region Λ (a union of R-boxes □ of side R level-k blocks), at a background (bg, V) — real, or complex in
a domain 𝔇 (backgrounds in a complex neighbourhood of the chart; complex source coefficients ε̂ of SRCAN55 §2.1). Fluctuations
U = e^{A}bg, gauge-fixed on the slice; A := (N/u_k)^{1/2}𝒞W with 𝒞 = Õ_k^{−1/2} restricted to the slice and W the white noise. The
small-field restriction is put on the white noise, **χ(W) := Π_b1{|W_b| ≤ p_W}** (Dimock's χ^w_k; a product), and dμ_p(W) :=
Π_b[1{|W_b| ≤ p_W}dγ(W_b)]/γ(|W| ≤ p_W)^{|Λ|} is a **product probability measure** (γ the standard Gaussian on su(N) ≅ R^D). Its
complement {some |W_b| > p_W} is a coupling-scaled cut failure: by LARGE55 NOFREEZE (bankable per CODEX_REVIEW_LARGE item 2 as
arithmetic) such failures must be returned in-step; they are not part of this expansion. The non-Gaussian part
V_int(A; bg, V, ε̂) := S_eff(e^{A}bg; V) − S_eff(bg; V) − ⟨∇S_eff, A⟩ − (u_k/2N)⟨A, Õ_kA⟩ + (Faddeev–Popov and Haar-Jacobian terms)
− (the inherited polymers of ρ_k) collects everything else.

### 5.2 Theorem CX (one-step polymer representation; PROVEN as an implication)
**Hypotheses.**
- (H1) [covariance with decoupling] 𝒞(s), s ∈ ℂ^𝒫, is Theorem RW (iv)'s s-weakened square root (a *field* interpolation, per
  PROOF's R1819-fix RW-1): holomorphic on {|s_□| ≤ s̄}, s̄ε_R < 1, with row sums Σ_{b′}|𝒞(s)|(b, b′) ≤ C_𝒞 there; and if s_□ = 0 for every
  □ ∉ Z, then (𝒞(s)W)_b for b in Z depends on W only on Z^♯ := Z ∪ {boxes within the Ω-range R + 1 of Z} (RW (iv)-(v): every walk
  term reads W on its last box and every intermediate box carries a factor s).
- (H2) [interaction] V_int = Σ_XV_X over R-box polymers X; V_X depends on A only in X; holomorphic on 𝒟_A := {|A_b| ≤ p_A ∀b} and
  in the parameters (bg, V, ε̂) ∈ 𝔇; |V_X| ≤ H_Ve^{−κ_Vd(X)} there (d(X) as in LINEAR_PACKAGE Theorem 5.1).
- (H3) [domain compatibility] (N/u_k)^{1/2}C_𝒞p_W ≤ p_A.
- (H4) [rates] κ_2 := min{κ_V, log(s̄ − 1)/(2√d)} − κ_0^{CE} − log 2·16 − 1 > 3κ_0^{CE} + 3 and C_locH_V ≤ c_0(κ_2) (Theorem 5.1's c_0).
**Conclusion.** ∫dμ_p(W)e^{−V_int((N/u_k)^{1/2}𝒞W)} = exp(Σ_YV^#(Y)), the sum over R-box polymers Y ⊂ Λ, with V^#(Y) depending on
(bg, V, ε̂) only through their restriction to Y^♯, holomorphic on 𝔇, and
  **|V^#(Y)| ≤ C_1C_locH_Ve^{−(κ_2 − 3κ_0^{CE} − 3)d(Y)},**
with C_loc, C_1 depending only on (d, κ_0^{CE}) — uniformly in k, T, Λ and its holes (the region enters only through which
polymers exist), and in the coupling except through H_V and (H3).
*Proof.* (1) Localisation (the interpolation of Dimock 1108.1335 (225)-(228)): for each Y, V_Y(𝒞(1)W) = Σ_{Z⊃Y}∫_{[0,1]^{Z−Y}}ds
∂_{s_{Z−Y}}[V_Y(𝒞(s)W)]|_{s_{Z^c}=0, s_Y=1} (the one-variable identity f(1) = f(0) + ∫_0^1f′ applied in each s_□, □ ∉ Y; terms with
s_□ = 0 outside Z). By (H1) the Z-term reads W only on Z^♯. Put V_loc(Z) := Σ_{Y⊂Z} of these terms. (2) Bounds: for complex
|s_□| ≤ s̄ on Z − Y, (H1) and (H3) keep 𝒞(s)W inside 𝒟_A on the support of μ_p, so V_Y(𝒞(s)W) is holomorphic there and bounded by
H_Ve^{−κ_Vd(Y)} (H2); Cauchy on the polydisc of radius s̄ − 1 about each |s_□| ≤ 1 gives |∂_{s_{Z−Y}}V_Y| ≤ (s̄ − 1)^{−|Z−Y|}H_Ve^{−κ_Vd(Y)}.
Each added box raises the touching-tree length by ≤ 2√d (in box units), so d(Z) ≤ d(Y) + 2√d|Z − Y| and the product of the two
factors is ≤ H_Ve^{−min(κ_V, log(s̄−1)/(2√d))d(Z)}; the sum over Y ⊂ Z (≤ 2^{|Z|} ≤ 2^{16(1+d(Z))} terms, Lemma CE-geo′) costs
e^{16 log 2(1 + d(Z))}. The same for the fattening Z ↦ Z^♯ (each Z^♯ arises from ≤ 2^{|Z^♯|} sets Z). (3) LINEAR_PACKAGE Theorem 5.1
(pre-S24, reviewed) applies to the product measure μ_p with H(X) := −Σ_{Z: Z^♯ = X}V_loc(Z), giving the representation and the
bound. Holomorphy in the parameters: every finite-volume step is a finite sum/integral of holomorphic functions with uniform
bounds, and Theorem 5.1's exponentiation is an analytic identity on a closed polydisc (its step 3). ∎
**Coupling as a spectator (SRCAN55 §3.7 (D1)).** The coupling and the sources enter only through V_X's size H_V and through
(H1)'s operator (SA-RW: Õ + Δ(ε̂), |Δ| ≤ ‖ε̂‖Ĥ, CONFIRMED for abstract Δ and at level 0, CODEX_REVIEW_SRCAN item 3 per [S26-BANKED]);
the representation is jointly holomorphic in (s, ε̂, background) with the same constants. **This is exactly the decaying-polymer
representation (D1) asks for, at the linear-plus-interaction level of one step — as an implication.**

### 5.3 The hypotheses' instances, with status
| hypothesis | instance | status |
|---|---|---|
| (H1) at the trivial background, every level | Corollary RW-triv (pre-S24 PROVEN); constants improved via γ_i^♯ (§2.3) | PROVEN (lane) |
| (H1) at level 0, every chart background, complex 𝔑(α_*) | Theorem N5-sf0 (b) with RW (iv) (pre-S24 PROVEN, CONFIRMED-WITH-FIX) | PROVEN (lane), existence constants |
| (H1) at levels ≥ 1, chart backgrounds | Proposition N5-sf_i ⟸ (NA-H_loc); here reduced to (HC_k) + (B2) (§3.7) | CONDITIONAL |
| (H1) on regions with holes | Theorem 1S-0 (c) under (FILL) | CONDITIONAL; NOT-VERIFIED for twisted holes |
| (H2) explicit local terms of S_W + κΣφ̂ (cubic and higher) | Taylor remainders on |A_b| ≤ p_A: O(u_k|A|³) = O(N^{3/2}u_k^{−1/2}(C_𝒞p_W)³) per link ⇒ small iff g_kp_W³ ≪ 1 (the coupling-scaled cut of LARGE55 §2.3) | elementary; constants not written |
| (H2) normaliser terms Σ_clog 𝒩̃_{t_k}(M̄_c) | Lemma NZ: holomorphic on the fixed width α_NZ ≫ g p_W, variation ≤ 2K_Nε_E per coarse link | PROVEN-HERE |
| (H2) Faddeev–Popov determinant, Haar Jacobian in exponential coordinates | NA-FP / FPq (pre-S24); their local expansion is not written | ARGUED |
| (H2) inherited polymers of ρ_k | node A's inductive hypothesis (R_m)(a) (LARGE55 §6.1) | OPEN (I6) |
| (H4) rates | needs log s̄ ≳ 2√d·460: R ≥ R_* + (2/(aL))·O(10³) with a ≍ the covariance rate (certified m_4 = 2.57·10⁻⁵ at level 0) | arithmetic; astronomically large but k-, T-free |
**Decay "at the soft-constraint mass".** The polymer rate in level-k units is ≍ (κ_2 − 3κ_0^{CE} − 3)/R, and R ≍ (log s̄)/(m_covL) — so
the rate is a fixed fraction of the covariance decay rate m_cov, which CT♯ ties to the gap γ_k (D_m ≤ γ/2), which is set by
min(c_co, κ/2)·c_1 — the soft-constraint mass in the proven sense. The located (unproven) rate is ≈ √κ (LINEAR_PACKAGE §4 table).

### 5.4 Proposition NZ-ret (zero-free normalised returned activities; PROVEN as an implication)
Let r_Y = Num_Y/Den_Y be a normalised returned activity whose denominator is a small-field one-step integral of the type of
Theorem CX on the inner region of Y, with boundary data V on Y's collar. If Theorem CX's hypotheses hold uniformly for complex V
in a domain 𝔇_V (e.g. the canonical tube, link width ϱg/√κ, where Lemma KA-1 bounds the numerators by e^{(ϱ²/2)cosh r} per link),
then **Den_Y(V) = N_χexp(Σ_{X⊂Y}V^#(X; V)) ≠ 0 on 𝔇_V**, with |log Den_Y(V^ℂ) − log Den_Y(V)| ≤ 2C_1C_locH_VΣ_{X⊂Y}e^{−κ″d(X)} ≤ C|Y|H_V.
*Proof.* Theorem CX's conclusion is an exponential of a convergent sum. ∎
**What this does and does not settle.** It moves CODEX_REVIEW_LARGE F3's "most dangerous" item from "unproved" to "an
implication of the per-step cluster expansion with complex boundary data" — which is how Balaban's method obtains it, and what
PLD §9.4 argued ("if the inner residual is sub-Gaussian at scale g/√κ") — and Lemma NZ removes the separate worry about the
single kernel normaliser. Codex's mixture (§4.4) is excluded because it is not a small-field integral around one background:
its two centres are O(1) apart, so no Gaussian domination at scale g/√κ holds for it. **The remaining input is Theorem CX's
hypotheses at levels ≥ 1 with complex boundary data (H1, H2: OPEN/CONDITIONAL as tabulated) — not a separate zero-free
statement.**

## §6. The geometric mismatch implication (CODEX_REVIEW_LARGE F2's open interface) — Lemma GMI (PROVEN-HERE, elementary)

**Setting.** A level-(j+1) plaquette P = (X; μν) with boundary links c_1..c_4; R_P := the 2 × 2 square of level-j blocks
B(X), B(X + e_μ), B(X + e_ν), B(X + e_μ + e_ν) (every contour of every c_i stays in it: contours of (Y, λ) lie in B(Y) ∪ B(Y + e_λ));
U a level-j field with every plaquette inside R_P obeying |log U_p|_HS ≤ f; W_c := W_0(M̄_c(U)) (polar part of the ARITHMETIC
contour mean, Decision 4's kernel centre); V any level-(j+1) field on ∂P.
**Statement.** Put a := 3(2L − 1)f (Lemma AX's gauge on the box of side 2L), assume p_La ≤ 1/40 and 3(2L − 1)f < min(π, 2π/√N).
- (i) **Following-field curvature:** |log hol_W(P)|_HS ≤ ε_f′ := L²f + (32L² + 109p_L²)a² = L²f[1 + 9(2L − 1)²(32L² + 109p_L²)f/L²].
- (ii) **Some link must mismatch:** if ‖1 − V_P‖_op ≥ ε_cl > ε_f′, then max_{c∈∂P}‖V_c − W_c‖_op ≥ (ε_cl − ε_f′)/4.
- (iii) **The kernel's own exponent sees it:** for every c, ψ_c(V_c) := φ_{M̄_c}(V_c) − φ_min(M̄_c) ≥ (1 − θ_y)(2N)⁻¹‖V_c − W_c‖²_HS with
  θ_y := 18.4y²(1 + C_N/N), y ≤ 1.1p_La (C_N of §4.3). Hence some c ∈ ∂P has **ψ_c ≥ δ_GMI := (1 − θ_y)(ε_cl − ε_f′)²/(32N)**, and
  δ_GMI ≥ (1 − θ_y)ε_cl²/(128N) when ε_f′ ≤ ε_cl/2 (the **strict chart margin**: f ≲ ε_cl/(2L²)).
*Proof.* (i) In the AX gauge every link of R_P has |A_b| := |log U_b| ≤ a. As in §2.5 (b): X_c := log W_c satisfies
|X_c − QA(c)| ≤ 13.2p_L²a² (BCH on contours, ≤ 2p_L²a², plus NA-alg (a)'s |X_0 − Ȳ| ≤ 9.2y²) and |X_c| ≤ 1.33p_La; n = 4 BCH gives
|log hol_W(P) − Σ±X_{c_i}| ≤ 2(5.3p_La)²; Σ±QA(c_i) = d(QA)(P) = Q_2(dA)(P) (Lemma ST, componentwise), |Q_2(dA)(P)| ≤ L²max_p|dA(p)|
(row sum L²), |dA(p) − log U_p| ≤ 32a². Collect. (ii) hol_V(P) − hol_W(P) telescopes over four unitary factors (and
‖V⁻¹ − W⁻¹‖ = ‖V − W‖), so ‖hol_V − hol_W‖ ≤ Σ_c‖V_c − W_c‖; and ‖1 − hol_W‖_op ≤ ‖log hol_W‖_op ≤ ε_f′. (iii) ψ = N⁻¹Re tr((1 − U′)𝔯)
with U′ := V⁻¹W and 𝔯 = H + iθ1 (cyclicity), = N⁻¹[tr(H(1 − (U′ + U′*)/2)) + θ Im tr U′] ≥ s(U′)(λ_min(H) − |θ|C_N/N) (1 − (U′ + U′*)/2 ≥ 0;
|Im tr U′| ≤ C_Ns(U′)); λ_min(H) ≥ 1 − 18.4y², |θ| ≤ 18.4y² (NA-alg (a)); s(U′) = (2N)⁻¹‖V − W‖²_HS ≥ (2N)⁻¹‖V − W‖²_op. ∎
**Corollary GMI-price (pointwise, no conditioning).** Every kernel factor obeys k_c(V_c; M̄_c(U)) ≤ ec_N⁻¹t^De^{−tψ_c(V_c)} at every
configuration (LARGE55 Lemma TL's proof; CONFIRMED by Codex F2). So on {bad P over cut-small fine fields} the integrand itself
carries ≤ 4ec_N⁻¹t^D·e^{−tδ_GMI} (sum over the four choices of the mismatching link) — **a pointwise price, so CODEX_REVIEW_LARGE
F2's warning that MIS under the plain law "does not give a density bound conditional on an arbitrary future V" does not
arise in an integrand-level (pointwise) induction.** With t = κu_j and CODEX_REVIEW_LARGE F9's a_eff rule, the usable exponent is
a_mis,eff < κε_cl²(1 − θ_y)/(128N) (the t^D prefactor is absorbed only by lowering the exponent: (κu)^De^{−au} ≤ C·e^{−a_eff u}).
**What it settles.** Codex's three requirements in F2 — "quantitative nondegeneracy of M" (NA-alg (a)'s y ≤ 1/20, implied by
p_La ≤ 1/40), "a strict chart margin" (ε_f′ ≤ ε_cl/2), "an explicit implication from a bad coarse plaquette to a link with
ψ ≥ δ" (δ_GMI) — and the averaged-logs vs arithmetic-mean transfer (NA-alg (a)'s 9.2y², inside (i)). At M = 0 (Codex's example)
the hypothesis p_La ≤ 1/40 fails, as it must: the lemma is a chart statement.

## §7. Toward the coordinator's milestone (one normalised, history-compatible step on a chart with a hole): what this file
## supplies and what is still open
| component | supplied here | status |
|---|---|---|
| main-term price, local charge allocation | Theorem LC-loc (linear, exact, no tails); Theorem LC-chart (tree level, PRICE form, BFT-1 on 𝒞_glob) | PROVEN / PROVEN as implication |
| the normalised main term | §3.1 + Lemma NZ-R: the log-normaliser is O(1)-smooth and u-independent; its background dependence is a one-loop δβ-type correction | PROVEN (bound); its renormalisation is the flow's |
| geometric mismatch implication | Lemma GMI + pointwise price | PROVEN-HERE |
| one-step positivity on a chart with a hole | Theorem 1S-0 (c) at level 0 under (FILL); levels ≥ 1 CONDITIONAL on (B2) | PROVEN as implication / CONDITIONAL; twisted holes NOT-VERIFIED |
| normalised returned-activity analytic norm, zero-free | Lemma NZ (normaliser, fixed width); Proposition NZ-ret (denominators ⟸ Theorem CX with complex boundary data) | PROVEN / PROVEN as implication |
| reference comparison (I5) | Theorem CX gives the reference's log as local polymers, so a cone's lateral boundary costs ≤ C·H_V per boundary box per level — a constant c_B = O(H_V), as LARGE55 E13 says; but boundary polymers READ cone variables, so COL's exact integration must be redone with those polymers expanded | ARGUED; the COL-compatibility step is OPEN |
| failed returns (Codex F9) | not addressed | OPEN |

## §8. Check record (criteria written and hashed before each script; plain python, exact arithmetic; stderr empty)

**st55_1 — Theorem LC and its lemmas.** `checks/st55_1_criteria.md` (sha256 70d412bb…, written 05:38:47Z, before the script) →
`checks/st55_1_lc.py` (597754e5…; patched once before its first and only run: a no-op expression cleaned and a faster offset table
for Q_2 — disclosed; no earlier run exists) → `checks/st55_1_out.txt` (e3480d26…), `checks/st55_1_err.txt` (empty); 05:42:06Z →
05:43:02Z, 55.8 s, exit 0.
- A1-A5 PASS (two seeds each): Q_root = Q_str − d∘h; d∘Q = Q_2∘d; d*Qᵀ = evᵀd*; Qᵀd* = d*Q_2ᵀ; Lemma CERT exactly at k = 1 (sides 6 → 2)
  and k = 2 (sides 18 → 6 → 2). A-ctl ((L−1)-squares) fails as designed.
- B1 PASS (random ratios ≤ 1; equality 1 for a constant one-orientation 2-form — Q_2's L^{4−d} = 1 is sharp). B2 PASS (on co-closed
  forms Q_rootᵀ = Q_strᵀ exactly, d*(Qᵀs) = 0, ratio ≤ 1/9; equality 1/9 for constants). **B2-ctl fired: ‖Q_rootᵀδ_c‖² = 277/729 ≈
  0.380 > 1/9** — without co-closedness the funnels (first-link weight 10/81) break the contraction, so co-closedness is
  load-bearing. B3 PASS (≤ 16, equality for the staggered transverse mode).
- **C1 PASS: E_1 − (1/34)‖dB_1‖² ⪰ 0 on every character sector of the side-2 coarse torus (fine side 6, κ_0 = 1)** — by translation
  and S_4 covariance this is the complete statement of Theorem LC at k = 1 on that torus; C0 (flat sector costs 0) holds; C3 (the
  0 ↔ 1 permuted sector agrees exactly) holds; **C2 fired: the bound with 1/30 fails at p = (π, π, π, π)**.
- Report: the exact Rayleigh quotient at p = (π, π, π, π) is **199017/6430226 = 0.030950…** — independent exact confirmation of PROOF
  `Lemma E-low`'s float record 0.0310 (c31 E), 5.2 % above c_co(1) = 1/34.
- D: c_co(1..3, ∞) = 1/34, 9/338, 81/3074, 1/38; c_E ∈ [0.004069, 0.004070]; **c_co/c_E ∈ [6.4665, 6.4672]**; γ^♯_i (i ≥ 1) from
  ≥ 2.58·10⁻¹⁰ to 1.67·10⁻⁹.
*Could it have failed?* Yes: C1 is a PSD test of exact 4 × 4 Schur complements computed from 244 × 244 exact LDLᵀ; with 1/30 it fails
(C2), and the measured minimum sits only 5 % above 1/34. A, B have firing controls.

**st55_2 — the stripe in the one-step chart.** `checks/st55_2_criteria.md` (ca8736af…, written 05:47:31Z, before the script) →
`checks/st55_2_stripe.py` (9ce51959…) → `checks/st55_2_out.txt` (c6cdfa33…), `checks/st55_2_err.txt` (empty); a first launch
failed before running (`timeout` absent on macOS, exit 127, no output — disclosed); run 05:49:37Z → 05:50:22Z, 44.4 s, exit 0.
Results in §3.5: G0, G1, G2, G3 PASS; C1, C2 as designed; **τ = 1/10: H_cond not PD on either subspace (reported)**. Decimal
values quoted in §3.5 were read from the exact rationals after the run with a float conversion (reading only; no verdict uses it).
*Could it have failed?* Yes: G1 equates an independently assembled Hessian to Codex's closed form; G3 is an exact PD test that
does fail at τ = 1/10 and at κ_0 = 1/10.

## §9. Verdicts on inherited claims touched by this file (file + locating string; reason)
- **IV1 — LARGE55 §6.2 "(BFT-coer) — the only new nonlinear input (OPEN, s…)":** linear trivial-background version **PROVEN-HERE**
  (Theorem LC, c_co = 1/38 at κ ≡ 1, L = 3; local form LC-loc); tree-level chart version in PRICE form **PROVEN as an implication**
  from BFT-1 on 𝒞_glob (LC-chart); the global chart form **NOT-VERIFIED** (needs BFT-1 with local η).
- **IV2 — LARGE55 "Lemma PRICE (implication; PROVEN-HERE, one line)":** the decomposition E = E_S + E_rest with E_S ≥ c_coε_cl²|S| that
  CODEX_REVIEW_LARGE F9 found unspecified is now supplied at tree level (LC-loc, LC-chart: one certificate, no tails, cone inside
  the 2 × 2 block squares). **CONFIRMED as an implication in that form**; Codex F9's a_eff and post-normalisation caveats stand (agree).
- **IV3 — LARGE55 §3 (h1) "expand the total soft action S + Σκuφ":** CODEX_REVIEW_LARGE F1 REFUTED it; **agree**; corrected in §3.1 (centred ψ
  plus log 𝒩̃, the latter O(1)-smooth: Lemma NZ-R).
- **IV4 — LARGE55 §3 (h2) and §5.4 "one-step conditional positivity (LCONV55 §G2, ARGUED)":** level 0 **CONFIRMED** (pre-S24 N5-sf0 (b),
  positivity step re-derived; stripe checked exactly) **with a chart-size condition** (§3.5: fails at τ = 1/10, κ_0 = 1, L = 3 on the
  stripe's subspaces); levels ≥ 1 **CONDITIONAL** on (B2); holes **CONDITIONAL** on (FILL), twisted holes NOT-VERIFIED.
- **IV5 — LARGE55 lg-17 "One-step positivity and Peierls windows are compatible":** **CONFIRMED in mechanism and now quantified**:
  the one-step window on the stripe's subspaces is β ≲ 0.12√κ_0 (L = 3); the Peierls side needs u_kε_cl² ≫ 1 with ε_cl inside the
  chart — compatible for g ≪ ε_cl ≪ 0.1√κ (and much smaller charts are used anyway).
- **IV6 — LCONV55 §G2 "Joint convexity fails; one-step conditional convexity holds" (ARGUED; CODEX_REVIEW_LCONV R9: unproved
  promotion):** **agree with R9 as to LCONV55's text**; the mathematical statement is **TRUE at level 0 for small charts** (N5-sf0 (b),
  gauge-fixed form, existence constants; exactly at the stripe for τ ≤ 1/20) and **FALSE for O(0.1) fields** (τ = 1/10, κ_0 = 1): "holds
  on the region" must carry a chart radius ≲ 0.1√κ.
- **IV7 — CODEX_REVIEW_LCONV R6 (frozen coarse fields add κu r|b|² curvature of the same coupling order):** **agree**; Lemma PSD gives
  it exactly, κ tr(ρ′*ρ′H), and st55_2 evaluates it (RQ_ker ≈ 2κ_0/L²).
- **IV8 — CODEX_REVIEW_LARGE F3 (mixture zero at r = asinh(π/(2t)); KA gives no denominator lower bound):** **agree** (re-derived §4.4);
  the single normaliser has no zeros on a fixed width (Lemma NZ); denominators are reduced to Theorem CX (NZ-ret).
- **IV9 — CODEX_REVIEW_LARGE F2 (geometric mismatch interface NOT-VERIFIED):** **agree that LARGE55 did not prove it; it is proved here**
  (Lemma GMI, with the averaged-log vs arithmetic-mean transfer through NA-alg (a)), pending a Codex check.
- **IV10 — LINEAR_PACKAGE Lemma 2.7 (E-low, c_E = 0.004069):** **CONFIRMED** as a valid bound (its dual-reduction proof not re-derived;
  Theorem LC dominates it by ×6.47 and is independent of the dual reduction).
- **IV11 — PROOF `Lemma N5-coer` γ_i:** structure **CONFIRMED**; for i ≥ 1 improved by c_E → c_co (×6.47); the PG constant c_1 remains the
  bottleneck.
- **IV12 — PROOF `Theorem N5-sf0` (b):** positivity logic **CONFIRMED** (re-derived); constants existence-only (agree with
  REVIEW_S18_S19); valid for T ≥ T_0.
- **IV13 — PLD §9.4 "(RLF-5) width (ARGUED…)":** **CONFIRMED as a reduction** — its sub-Gaussian hypothesis is what Theorem CX supplies;
  holds as an implication where CX's hypotheses hold (level 0, trivial background); OPEN at levels ≥ 1.
- **IV14 — SRCAN55 §3.7 "(D1)… beyond that, N6. All OPEN beyond what §2 proves.":** Theorem CX supplies N6's per-step structure **as an
  implication** (jointly holomorphic in (s, ε̂, background)); its hypotheses are tabulated in §5.3.
- **IV15 — PROOF `Proposition NAH-ind` "(BG-unif)" as the uniformity input:** **refined** — a *lower* Hessian bound (HC_k) with (B2)
  suffices (§3.7, ARGUED); (BG-unif)(iv)'s two-sided Lipschitz form is not needed for positivity.
- **IV16 — LCONV55 §G1 "the convexity window and the Peierls window are disjoint":** concerns the joint chain; not applicable to one
  step (agree with LARGE55 IV14 and with Codex LCONV R8 that it is not an exact consequence of order notation).

## §10. Errata from a full re-read of §0-§9 (append-only; each item overrides the text it names)
- **S0 (order).** §3.5-§3.7 were appended after §4 (the stripe check finished after §4 was written); read the file as §2, §3.1-§3.4,
  §4, §3.5-§3.7, §5, …
- **S1 (§2.5 (b) and the theorem's constants).** Re-collecting the three BCH/NA-alg terms gives |r_j − ρ_j| ≤ 22(p_L²a_j² + |ρ_j|²), not
  19(…); hence C_R′ := 22(p_L² + 3L^{4+2σ}) (the 3 absorbs 1 + C²η² ≤ 3/2), and θ_s ≤ 3·10⁻² (not 2·10⁻²) under p_Lη ≤ 1/40, √Nη ≤ 10⁻².
  NA-alg (b)'s cubic coefficient gives (2√N/3)e^{|ρ|}|ρ| in (c); the printed √N e^{|ρ|}|ρ| is a valid weaker form. No conclusion changes.
- **S2 (§3.2 (ii), "same inertia").** Read: at a critical point the tree-level Hessian vanishes on G_fl-orbit directions and is
  G_fl-invariant, so positivity of the gauge-fixed Õ (slice + fixing, the fixing positive on the Λ_res-orbit directions) and of the
  quotient Hessian are equivalent — the standard Faddeev–Popov argument (PROOF NA-crit/NA-FP), not re-derived here.
- **S3 (§3.4, garbled sentence).** "c_str ≈ 2-7 in β² units …, i.e. 11/6 … 7/32·… in plaquette-cut units per Codex R8" reads: LCONV55's
  certified negative Rayleigh quotients are −(22/3)β² (torus, P = 3), −4.0β², −2.86β² (P = 5, 7) and ≈ −2.3β² (cylinder) — in LCONV55's
  normalisation, which equals the HS-normalised lane Hessian per unit |A|²_HS; in plaquette-cut units t_0 ≈ 2β they are divided by 4
  (Codex R8: 22/3 → 11/6, c_*/8 → c_*/32). The one-step mass in the same units is κ_0/L², so the threshold is β ≈ (κ_0/(9·7.33))^{1/2} ≈
  0.12√κ_0 at L = 3 — consistent with §3.5.
- **S4 (§3.5, "Reading").** The certified numbers bound the erosion of the one-step mass from ABOVE (≤ 78τ², ≤ 64τ²); what is
  established is positivity at τ ≤ 1/20 and its failure at τ = 1/10 (κ_0 = 1). "τ ≲ 0.06√κ_0" is an interpolation (ARGUED), and the √κ_0
  scaling an extrapolation from the structure (bare part κ-independent, kernel part ∝ κ_0), not computed.
- **S5 (§4.1).** "holomorphic on a neighbourhood of SU(N)·SL(N, ℂ) in M_N(ℂ)" reads "holomorphic on an open set of M_N(ℂ) containing
  SL(N, ℂ) (e.g. GL(N, ℂ), where the integrands, which contain V⁻¹, live)".
- **S6 (§4.3 (ii)).** The A_N bound reads A_N ≤ e(C′_NΓ(D/2 + 2) + 2((D + 2)/(4e))^{(D+2)/2})/c′_N (the "+2" was sup_λ2λ^{D/2+1}e^{−2λ} only
  for small D). C_N = N(N² − N + 2)/2 already suffices (the printed N(N² + 2)/2 is valid). The final bound reads
  |log 𝒩̃_t − log 𝒩_t(1, 1)| ≤ min(2K_Nε_E, log 2), not "≤ log 2·(4/3)".
- **S7 (§4.3 (3), Lemma NZ-R).** Block norms of a D-dimensional link space carry a factor D: C_𝒩 := 16Dn_c/α_NZ².
- **S8 (§5.2 (H4) and §5.3).** (H4) needs log(s̄ − 1)/(2√d) > 4κ_0^{CE} + 16 log 2 + 4 ≈ 620, i.e. log s̄ ≳ 2.5·10³ (the table's "2√d·460"
  is wrong; the conclusion "astronomically large R, k- and T-free" stands). The fattening Z ↦ Z^♯ also costs a fixed factor c_fat in
  the rate (d(Z^♯) ≤ c_fat(1 + d(Z))): read κ_2 as κ_2/c_fat throughout Theorem CX. H_V is a per-R-box size: the cubic terms give
  H_V ≍ R⁴L⁴N^{3/2}g_k(C_𝒞p_W)³, so (H4)'s smallness needs g_k ≪ (R⁴L⁴p_W³)⁻¹ — again k- and T-free.
- **S9 (§5.4).** Den_Y also carries the main-term factor e^{−S_eff(bg)} and the Gaussian normalisation det(Õ)^{−1/2}; both are
  non-vanishing on complex backgrounds where CT♯ applies (spectrum in Re z ≥ γ′ > 0). The displayed formula holds up to those
  factors.
- **S10 (§6).** R_P is contained in a box of side 2L (not equal to it); the hypothesis "every plaquette inside R_P" reads "every
  plaquette inside that box", which is what Lemma AX needs. In Corollary GMI-price read: the kernel factor of the mismatching link
  obeys k_{c*} ≤ ec_N⁻¹t^De^{−tδ_GMI} pointwise; summing over which of the four links mismatches costs a factor ≤ 4.
- **S11 (§2.5 (iv)).** The compatibility condition uses LARGE55 E15's C_δ (L1e(b)'s constant), which CODEX_REVIEW_LARGE F11 notes was
  stated in PROOF for L ≥ 9; at L = 3, 5 Lemma GMI (i) supplies the needed bound directly (ε_f′ ≈ L²f), so E15's role is taken by GMI.

**IV17 (found on the re-read; added to §9).** LCONV55 §G2 "deficit ≈ u_0cβ² against ≈ κu_0, with β ≤ ε_1 ≪ √κ" and LARGE55 §5.4 "cβ² < κ
(kernel beats the stripe deficit)": **REFUTED in the constant, mechanism CONFIRMED.** The mass the kernel puts on the stripe's slow
(holonomy) directions is κ_0u_0/L² per unit |A|²_HS (Proposition OSS; st55_2: 2κ_0/L² in Euclidean-v units), not ≈ κu_0. Correct
condition: c_strβ² < κ_0/L² with c_str ≈ 7.33 (LCONV55's P = 3 torus value, HS units) — about L² = 9 times more restrictive at L = 3;
st55_2 confirms the corrected form (positive at τ = 1/20, not at τ = 1/10, κ_0 = 1).

## §11. Summary table — every claim made or judged in this file
| id | claim (place) | verdict / status |
|---|---|---|
| st-1 | Lemmas ST, Q2 (‖Q_2‖ ≤ L^{(4−d)/2}, sharp), CC (co-closed contraction L⁻¹), DS (‖d*‖² ≤ 4d) (§2.2) | PROVEN-HERE; exact checks st55_1 A, B with firing controls |
| st-2 | Lemma CERT (exact dual certificate) (§2.3) | PROVEN-HERE; exact at k = 1, 2 (st55_1 A5) |
| st-3 | Theorem LC: E_k ≥ c_co(k)‖dB_k‖², c_co = [2 + 32L²/(κ_−(L² − 1))]⁻¹ = 1/38 at κ ≡ 1, L = 3 (§2.3) | PROVEN-HERE; complete exact check at k = 1 on the side-2 coarse torus (st55_1 C1); exact minimum 199017/6430226 |
| st-4 | one-level induction gives only c_i ~ κ/(16i) (why the multi-level certificate is needed) (§2.3) | PROVEN-HERE (elementary) |
| st-5 | γ_i^♯ (i ≥ 1) improves ×6.47 (c_E → c_co) (§2.3) | PROVEN as an implication (N5-coer pre-S24) |
| st-6 | Theorem LC-loc: local charge allocation, no tails, cone inside the 2 × 2 block square (§2.4) | PROVEN-HERE |
| st-7 | Theorem LC-chart: tree-level price per bad plaquette ≥ ¼(1 − θ_s)c_coε_cl² if ε_cl ≥ 2C_♮C_0²ε_0² (§2.5, S1) | PROVEN as an implication from BFT-1 on 𝒞_glob |
| st-8 | global chart form of (BFT-coer) for all chart V | NOT-VERIFIED (needs BFT-1 with local η) |
| st-9 | exact one-step action S_eff with centred ψ and log 𝒩̃ (§3.1) | PROVEN-HERE (elementary; agrees with Codex F1) |
| st-10 | Lemma PSD: kernel Hessian at zero mismatch = tr(ρ′*ρ′H) ≥ (1 − 18.4y²)\|𝒬_Uv\|², zero exactly on coarse-invisible directions (§3.3) | PROVEN-HERE (zero-mismatch case); the O(\|ρ\|) correction ARGUED (constants not computed) |
| st-11 | Proposition OSS: one-step mass κ_0/L² vs joint mass κ_KL^{−2(K+1)}/ΣL^{−2l} on the holonomy direction (§3.4) | PROVEN-HERE |
| st-12 | stripe in the one-step chart: G0-G3 at τ = 1/50, 1/20; NOT PD at τ = 1/10 (κ_0 = 1, L = 3) on the stripe's subspaces (§3.5) | PROVEN (exact, st55_2); window interpolation ARGUED (S4) |
| st-13 | Theorem 1S-0: (a) level-0 positivity on all of 𝔖(ε_*) (§3.6) | CONFIRMED (pre-S24 N5-sf0 (b), positivity step re-derived) |
| st-13b | (b) exact action incl. H_𝒩; (c) regions with collars and holes under (FILL) | PROVEN as implications; twisted holes NOT-VERIFIED |
| st-14 | Proposition 1S-k (levels ≥ 1) ⟸ (HC_k) + one-level inputs; (HC_k) at the trivial background (§3.7) | PROVEN as an implication; trivial case PROVEN |
| st-14b | (HC_k) on the chart ⟸ BFT-1 + (B2) with summable defects | ARGUED; (B2) OPEN |
| st-15 | Lemma INV (complex Haar invariance) (§4.1) | PROVEN-HERE |
| st-16 | Lemma PR (complex polar recentring) (§4.2) | PROVEN-HERE |
| st-17 | Lemma NZ: single normaliser zero-free on a fixed link width α_NZ, \|log 𝒩̃_t − log 𝒩_t(1,1)\| ≤ min(2K_Nε_E, log 2), every t (§4.3, S6) | PROVEN-HERE (K_N via the Haar-volume constants c′_N, C′_N; explicit for SU(2)) |
| st-18 | Lemma NZ-R: ‖H_𝒩‖_{N_0} ≤ 16Dn_c/α_NZ², u-independent (§4.3, S7) | PROVEN-HERE |
| st-19 | SU(2): 𝒩_t = e^{−t}Φ_2(t²ς), zeros only at t²ς = −j_{1,n}² (§4.4) | PROVEN-HERE (classical Bessel facts) |
| st-20 | Codex's mixture zero at r = asinh(π/(2t)) (§4.4) | CONFIRMED (re-derived) |
| st-21 | Theorem CX: one-step polymer representation, uniform in k, T, Λ; coupling as spectator; jointly holomorphic (§5.2, S8) | PROVEN as an implication |
| st-22 | Proposition NZ-ret: normalised returned-activity denominators zero-free where CX holds with complex data (§5.4, S9) | PROVEN as an implication |
| st-23 | Lemma GMI: bad coarse plaquette over cut-small fine fields ⇒ ψ_c ≥ (1 − θ_y)ε_cl²/(128N) on some link; pointwise price (§6, S10) | PROVEN-HERE |
| st-24 | reference comparison: c_B = O(H_V) per boundary box per level; COL-compatibility with boundary polymers (§7) | ARGUED / OPEN |
| st-25 | failed returns (§7) | OPEN (not addressed) |
| IV1-IV17 | inherited claims (§9 and IV17) | CONFIRMED: IV2, IV4 (level 0, with chart condition), IV5, IV6 (level 0, small charts), IV7, IV8, IV10, IV11, IV12, IV13 (as a reduction); REFUTED: IV3 (with Codex F1), IV17 (constant: κ_0/L², not κ); NOT-VERIFIED / CONDITIONAL: IV1's global chart form, IV4 and IV6 at levels ≥ 1, IV9 pending Codex (now PROVEN-HERE), IV14 (supplied as an implication), IV15 (ARGUED refinement), IV16 (not applicable) |

**Counts.** New claims: PROVEN-HERE 15 (st-1, 2, 3, 4, 6, 9, 10, 11, 15, 16, 17, 18, 19, 23, and st-12 as exact check); PROVEN as an
implication 7 (st-5, 7, 13b, 14, 21, 22, and st-13b's (c) under (FILL) counted once); CONFIRMED 2 (st-13, st-20); ARGUED 2 (st-14b,
st-24); NOT-VERIFIED 2 (st-8, twisted holes in st-13b); OPEN 2 ((B2) in st-14b, st-25). Inherited: CONFIRMED 10, REFUTED 2, NOT-VERIFIED
or conditional 5. **No REFUTED item deletes banked work**: IV3 agrees with Codex F1; IV17 corrects a constant in two Opus 5.5 files whose
qualitative conclusion stands.

## §12. For the lead
1. **I2 / (BFT-coer), linear: PROVEN, explicit, local.** A dual certificate (Lemma CERT: ⟨dB_k, Ξ⟩ = ⟨dB_0, (Q_2ᵀ)^kΞ⟩ − Σ_i⟨r_i,
   (Qᵀ)^{k−1−i}d*Ξ⟩) gives E_k(B_k) ≥ c_co‖dB_k‖², **c_co = [2 + 32L²/(κ_−(L² − 1))]⁻¹ = 1/38 at κ ≡ 1, L = 3** — 6.47 × LINEAR_PACKAGE's
   c_E, k- and T-uniform because Qᵀ contracts co-closed forms by L⁻¹ per level while Q_2 is exactly marginal at d = 4. The exact
   complete check at k = 1 (st55_1) finds the true minimum 199017/6430226 ≈ 0.03095, 5 % above the bound. **Local form (LC-loc):** the
   charge of any set of coarse plaquettes sits inside their 2 × 2 block squares, no tails — the decomposition PRICE needed
   (CODEX_REVIEW_LARGE F9). **Chart, PRICE form (LC-chart):** proven as an implication from BFT-1 on 𝒞_glob (banked conditionally),
   with constraint ε_cl ≥ 2C_♮C_0²ε_0². The global chart form needs local BFT bounds (NOT-VERIFIED). Consequence: γ_i^♯ (i ≥ 1) × 6.47.
2. **I1 (a) / one-step positivity.** Chart and metric (notice N1): left-trivialised normal coordinates at the current point,
   product bi-invariant metric, V fixed, G_fl removed either chart-free (quotient Riemannian Hessian = Hessian on horizontal
   vectors) or by the lane's slice + fixing. In that chart the kernel's Hessian at zero mismatch is exactly κ tr(ρ′*ρ′H) — positive on
   every coarse-visible direction, zero on coarse-invisible ones (Lemma PSD) — and the holonomy directions where LCONV55's stripe
   lives carry the one-step mass κ_0/L² instead of the joint chain's κL^{−2(K+1)} (Proposition OSS). **Level 0 is already a theorem**:
   pre-S24 N5-sf0 (b) gives the gap on the whole small-field class, stripes included (positivity logic re-derived: CONFIRMED); the
   exact action's log-normaliser adds only O(1) (Lemma NZ-R), so CODEX_REVIEW_LARGE F1 costs O(g_0²). **Exactly at the stripe
   (st55_2): positive at τ = 1/50, 1/20 (certified margins 0.191, 0.062 vs 0.222), NOT positive at τ = 1/10** (κ_0 = 1, L = 3): the chart
   must satisfy roughly β ≲ 0.12√κ_0 — and LCONV55/LARGE55's "deficit against ≈ κu_0" overstates the mass by L² (IV17, REFUTED in the
   constant). Holes: proven under (FILL); **holes whose collar carries holonomy around a linked surface (frozen centre vortices) are
   NOT-VERIFIED** — a precise gap in "uniformly in the holes". Levels ≥ 1: reduced to (HC_k), a *lower* Hessian bound; trivial
   background PROVEN (Theorem LC); on the chart ARGUED with one missing input **(B2): the ℓ² derivative bound of the background map
   with the sharp weight L^{k−j}** — this replaces (BG-unif)(iv) on the critical path.
3. **Zero-free normaliser (notice N2).** **Lemma NZ: the single kernel normaliser 𝒩_t(M̄(U)) has no zeros on a FIXED, g-independent
   complex link width, uniformly in t**, and its centred log is bounded there by min(2K_Nε_E, log 2) — proof: complex Haar invariance
   (Lemma INV) + complex polar recentring (Lemma PR) + a sub-Gaussian moment bound; explicit for SU(2) (𝒩_t = e^{−t}·2I_1/·, zeros only
   on the negative real axis of t²ς). Codex's mixture zero is CONFIRMED but concerns superpositions with O(1)-separated centres; the
   **normalised returned-activity denominators are zero-free wherever the per-step cluster expansion holds with complex boundary
   data (Proposition NZ-ret)** — so Codex's "most dangerous" item is reduced to Theorem CX's hypotheses at levels ≥ 1, not a separate
   statement.
4. **I1 (b) / N6: Theorem CX (implication).** The per-step polymer representation, uniform in k, T, region and holes, coupling as a
   spectator, jointly holomorphic in (s, ε̂, background) — exactly SRCAN55 §3.7's (D1) at one step. Instances: level 0 and the
   trivial background PROVEN (lane); levels ≥ 1 CONDITIONAL (st-14b); Faddeev–Popov/Jacobian expansions ARGUED; inherited polymers OPEN
   (I6). The rate is a fixed fraction of the covariance rate (proven tiny, located ≈ √κ); R and g_0 thresholds are astronomically
   large/small but k- and T-free.
5. **Geometric mismatch (Codex F2): Lemma GMI PROVEN** — over cut-small fine fields (f ≲ ε_cl/(2L²)), a coarse plaquette with
   ‖1 − V_P‖ ≥ ε_cl forces ψ_c ≥ (1 − θ_y)ε_cl²/(128N) on one of its links; the price is pointwise (TL's kernel bound), so F2's
   conditioning concern does not arise; the log-mean/arithmetic-mean transfer is NA-alg (a)'s 9.2y².
6. **What PROOF.md / HANDOFF should change (lead's decision; nothing edited here; all pending Codex).** No tally change. HANDOFF's
   I1 row: *"level 0 = N5-sf0 (b) + Lemma NZ-R; levels ≥ 1 ⟸ (HC_k) ⟸ BFT-1 + (B2); twisted holes NOT-VERIFIED; chart constraint
   β ≲ 0.12√κ_0 (L = 3)"*. I2 row: *"linear (BFT-coer) PROVEN, c_co = 1/38 (STEP55 Theorem LC/LC-loc); chart PRICE form ⟸ BFT-1 on
   𝒞_glob"*. Codex's most-dangerous item (zero-free normalised activities): *"normaliser: PROVEN (Lemma NZ); denominators ⟸ Theorem CX
   with complex data"*. N5 node: γ_i^♯ improved; the (NA-H)/(BG-unif) input sharpened to (B2). Milestone status per §7: reference
   comparison ARGUED (COL-compatibility with boundary polymers OPEN), failed returns OPEN.
7. **Codex verdicts used:** CODEX_REVIEW_LARGE F1, F2 (as to LARGE55), F3, F9 — agree; CODEX_REVIEW_LCONV R2, R5, R6 — agree; R9 — agree
   as to LCONV55's text, with the note that the level-0 theorem existed pre-S24 (N5-sf0 (b)); CODEX_REVIEW_NRES item 2 — agree. No
   disagreement with any Codex verdict.
8. **Counts:** new claims — PROVEN-HERE 15, PROVEN as an implication 7, CONFIRMED 2, ARGUED 2, NOT-VERIFIED 2, OPEN 2; inherited —
   CONFIRMED 10, REFUTED 2 (IV3 with Codex F1: the "total soft action" omits log 𝒩 — corrected in §3.1; IV17: the one-step mass is
   κ_0/L², not ≈ κ — corrected condition c_strβ² < κ_0/L²), NOT-VERIFIED/conditional 5.

## Closing provenance
Model: claude-opus-5-5 (first line). Files written by this worker: `STEP55.md`; `checks/st55_1_criteria.md`, `checks/st55_1_lc.py`,
`checks/st55_1_out.txt`, `checks/st55_1_err.txt`; `checks/st55_2_criteria.md`, `checks/st55_2_stripe.py`, `checks/st55_2_out.txt`,
`checks/st55_2_err.txt`. No git command was run. The Balaban-method corpus was read as data only (1108.1335 §4.4-§4.6 and Lemma 29);
nothing from it is copied beyond short attributed references to equation numbers.

## §13. Addendum — st55_3: the one-step positivity window at the stripe, bracketed (supersedes erratum S4's interpolation)
`checks/st55_3_criteria.md` (sha256 ef8f1d5e…, written 06:07:47Z, before the script) → `checks/st55_3_window.py` (fa08df22…; it
executes st55_2_stripe.py's definitions unchanged, not its main loop) → `checks/st55_3_out.txt` (see shasum in the tool record),
`checks/st55_3_err.txt` (empty); 06:08:08Z → 06:10:15Z, 126.8 s, exit 0. **All predictions held (PASS):**
| κ_0 | last PD grid τ | first non-PD grid τ | bracket for β_c = 2 arctan τ_c |
|---|---|---|---|
| 1/4 | 1/35 | 1/30 | (0.057, 0.067) |
| 1 | 1/17 | 1/16 | (0.118, 0.125) |
| 4 | 1/9 | 1/8 | (0.222, 0.249) |
Monotone in τ for every κ_0; ratios of bracket midpoints τ_c(4)/τ_c(1) = 578/297 ≈ 1.95 and τ_c(1/4)/τ_c(1) = 1768/3465 ≈ 0.51 —
**the √κ_0 scaling is now an exact-arithmetic observation on three values, not an extrapolation.** Controls: τ = 0 PD for every κ_0;
τ = 1/4 not PD for κ_0 ∈ {1/4, 1}. **Corrected reading of §3.5 / S4:** on the stripe's subspace H_red(0) (SU(2), L = 3) the one-step
Hessian is positive definite iff τ < τ_c(κ_0) with τ_c(κ_0) ≈ 0.061√κ_0 (bracketed above), i.e. stripe link angles β < β_c ≈ 0.12√κ_0 —
**a certified lower bound on how small the chart must be for one-step positivity, independent of every existence constant.** It is
a statement on one 28-dimensional subspace (the one where LCONV55's mechanism lives); the full space can only lower β_c further.
- **S12 (§13 table).** For κ_0 = 4 the β-bracket is (0.221, 0.249) (2 arctan(1/9) = 0.2213…), not (0.222, 0.249). The st55_3_out.txt
  sha256 is 6048d9d1…; st55_3_err.txt is empty.
- **S13 (§12 item 2, §11 st-12).** With §13, the window statement is certified: β_c ∈ (0.118, 0.125) at κ_0 = 1 and β_c ∝ √κ_0 on
  three values (L = 3, SU(2), on H_red(0)); "roughly β ≲ 0.12√κ_0" in §12 now reads as this bracket.
**Provenance amendment.** Files written also include `checks/st55_3_criteria.md`, `checks/st55_3_window.py`, `checks/st55_3_out.txt`,
`checks/st55_3_err.txt`. No git command was run. Final at the `date -u` below.
Thu Oct 29 06:11:04 UTC 2026
