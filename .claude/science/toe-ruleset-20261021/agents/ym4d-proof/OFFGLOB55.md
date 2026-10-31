Reviewer model: claude-opus-5-5

# OFFGLOB55 — the background-field theorem outside the global small-field class 𝒞_glob

Worker file (Opus 5.5, session 26). Append-only. Writes only this file and `checks/og55_*`.

## PRE-STATED (written 2026-10-29 03:22 UTC, before any derivation; statements only)

**Targets.**
- **T1 (the class).** State the set 𝔅_k of backgrounds the RG must handle at level k: small field
  strength on every block, arbitrary holonomy, arbitrary local gauge frames; state the norm; state
  exactly which subset is 𝒞_glob.
- **T2 (UHL).** On boxes of bounded size (in block units): existence, uniqueness and regularity of a
  local gauge in which the background is close to Z = 1, with constants uniform in k, T and the box —
  or the precise obstruction.
- **T3 (patching).** From (UHL) + the CONFIRMED Corollary GA-PG / Lemma OC (CODEX_REVIEW_BGT), prove
  (G♯-patch) / (LOC-cc_Z) with transition functions, keeping every source composite-co-closed; decide
  whether BFT34_55's Proposition RW-cc routing survives transition functions.
- **T4 (assembly).** BFT-0/1/2 outside 𝒞_glob as an implication, every input named with its status.

**What would count as a refutation (of my own targets or of the lane's named route).**
- T1: a background produced by the RG at level k that is outside my 𝔅_k; or a mis-identification of
  𝒞_glob (e.g. "trivial holonomy on the torus ⇒ globally gauge-equivalent to near-1" failing).
- T2: a configuration on a box with small block field strength for which no gauge makes all links
  within the claimed constant of 1; a non-uniqueness of the gauge within the claimed neighbourhood;
  or a constant that grows with the box diameter, k, or T beyond what the class allows. (Expectation
  stated in advance: any such constant can be uniform only for boxes of bounded diameter in block
  units; the deviation from 1 scales like diameter × field strength.)
- T3: a source cut by a partition of unity that is not cc and cannot be re-routed; a transition-function
  step that breaks cc-ness or the gauge covariance of the norm; a decomposition constant C that grows
  with the volume or with the number of boxes.
- T4: any input I label PROVEN that is NOT-VERIFIED or REFUTED in an on-disk Codex review, or that
  depends on a REFUTED §6 statement of BGT55.
- A counterexample to any step is a first-class result and will be reported as such.

# FINDINGS (appended from 2026-10-29T04:01Z; everything below was written after the PRE-STATED block)

## §0. Read record, provenance, symbols pinned

**Read (located by string; line numbers as of 03:22-04:00Z, they drift).** REVIEW_BRIEF_55 (all); the brief `queue/offglob.md`
(all); CODEX_REVIEW_BGT.md (all 396 lines; complete — ends with "Exactly what may be banked" item 7); BGT55.md §1-§4, §6.5, §7, §8
(l.40-260, 395-460); PROOF.md header incl. [S26-BANKED] (l.1-36), "Lemma AX" (l.5521-5540), "Lemma N5-cov", "Theorem RW",
"Theorem N5-sf0" (l.5506-5700); REVIEW_S18_S19 "## Lemma AX (l.5183-5200): CONFIRMED"; HANDOFF.md (all); PLAN_S26.md l.1-60;
REVIEW_S22.md Part 5 (l.370-440, the BFT statement); BFT_A.md §1-§2 (l.1-98), §3.8-§3.11 (l.187-275); REVIEW_BFT_A_S1 l.325-345;
KFACTOR_OFF55.md §1 (l.66-130), §2.2 (l.173-206), §3.1-§3.6 (l.208-326), §4.1-§4.6 (l.330-424); GV55.md §3 (l.240-326);
CODEX_REVIEW_GV "Exactly what may be banked" (l.422-end); BFT34_55.md §1 (l.96-228), §2.3-§2.7 (l.289-425); CODEX_REVIEW_BFT34 R5-R7,
summary and banking (l.95-170, 237-end); NSL55.md §2-§3 (l.157-311), §10 (l.767-856); GSHARP55 §5.1, §5.4 (l.392-460, 555-581);
COFUN_CC §6.2 (l.430-450); REVIEW55_BFTB Findings 9, 11, 14, 15 (l.268-368); HESSREL §H6.1-§H6.2 (l.505-528); Goswami 2204.08252
(corpus) l.1-520 (method only; nothing copied). The owner's folder `~/Documents/balaban-cmp/` is **empty** (checked 03:2xZ), so no
Balaban CMP paper was read; every statement below attributed to Balaban's method is from the open expositions or is the lane's
own paraphrase, and is labelled so.

**Provenance of inputs I lean on.** Theorem GA, GA-PG, Lemma OC, KER_Z/SF_Z: CONFIRMED by Codex (CODEX_REVIEW_BGT items 1-5) —
I re-derived OC and KER_Z (two lines each, below where used) and agree. Theorem K^{(σ)} (KFACTOR_OFF55 §4.5) with CCP (a)-(d),
HR (i)-(v), ROW^{(σ)}, CB: CONFIRMED by Codex (CODEX_REVIEW_KOFF items 1-5, as recorded in PROOF [S26-BANKED] and in
CODEX_REVIEW_GV item 4), conditional on GV and the lane-A linear package; GV-E CONFIRMED (CODEX_REVIEW_GV item 2). Lemma AX:
CONFIRMED (REVIEW_S18_S19, a pre-session-24 review); re-derived below. RW-cc algebra, CCL's 216: CONFIRMED (CODEX_REVIEW_BFT34
item 3). NSL55's Theorem NSL: Opus 5.5, **Codex review running — NOT banked; used below only as a named input with that status.**

**Symbols pinned (systemic defect 1).**
- **ε** = REVIEW_S22's BFT data parameter: max_P |log V^r_P| ≤ ε for the level-k data. Not BFT_A's ε_0, not NSL's ε's.
- **d(W, 1)** := min{|X| : X ∈ su(N), e^X = W}, |·| the Hilbert-Schmidt norm (Lemma AX's metric; bi-invariant, triangle
  inequality). For d(W, 1) < min(π, 2π/√N) the principal log is in su(N) and |log W| = d(W, 1) (AX's proof).
- **s** := ‖B_k‖_D (BFT_A §1.2): the data size **in one global gauge** — the parameter of every 𝒞_glob theorem (BFT-E, K^{(σ)}).
- **R** := box side (coarse units) of the frame cover; **R′ := 4R + 5** the enlarged box (N5-sf0's Ω^+ convention).
- **U** = a composite configuration (U_0, …, U_{k−1}) with top datum U_k = V; **Z** = a critical one. KFACTOR_OFF55's x (log
  coordinates at the trivial chain of a frame) is written **y** when it is a frame coordinate.
- **𝒦_y** := P_cc H^{log}_y + Γ^TΓ (§4; my name for the linearisation of the K^{(σ)} map; not a lane symbol).
- **P_U, P_cc^U** = the covariant hierarchical routing / projection at U (§3; new). P, P_cc (no superscript) = KFACTOR_OFF55's flat ones.
- **𝔑_k(R, α)** (data frame class, §1) and **𝔇_k(R, η)** (background frame class, §1.6) are new names; N5-sf0's 𝔑(α) is the
  level-0 analogue and is cited as such.
- I do not use the letters θ (class exponent of CC-INV stays θ), C_1, c_1 for anything new.

## §1. T1 — the class of backgrounds, the norm, and exactly which part is 𝒞_glob

### 1.1 Definitions
Level-k lattice = the coarse torus 𝕋_T (side T, unit spacing); d = 4, N ≥ 2, L ≥ 3 odd.
- **Data class (REVIEW_S22 Part 5, "Data"/"Claim").** 𝔅_k(ε) := {V : level-k links → SU(N) : d(V_P, 1) ≤ ε for every
  plaquette P}; complexified 𝔅^ℂ_k(ε, r) := {e^zV : V ∈ 𝔅_k(ε), z : links → su(N)⊗ℂ, |z|_∞ ≤ rε}. For ε < min(π, 2π/√N) this is
  literally REVIEW_S22's "max_P|log V^r_{k,P}| ≤ ε, |z|_∞ ≤ r_ℂε" (§0, d = |log|). No condition on links, holonomies, frames.
- **Global small class (BFT_A §1.2).** 𝒞_glob(s) := {V = e^B : max_c|B(c)| ≤ s} in ONE fixed global gauge, and its gauge
  saturation **𝒞*_glob(s) := ∪_g g·𝒞_glob(s) = {V : ∃ g with d((gV)_c, 1) ≤ s for every level-k link c}**. Because 𝔉_k is
  gauge invariant (TOWER-VAR) and every BFT conclusion transforms covariantly (Lemma OC, CODEX_REVIEW_BGT item 3 / §7; Lemma N5-cov),
  each 𝒞_glob theorem (BFT-E, Theorem BFT3-glob) holds verbatim on 𝒞*_glob(s) after transport by g. **The 𝒞_glob part of
  BFT's class is 𝔅^ℂ_k(ε, r_ℂ) ∩ 𝒞*_glob(ε_g), ε_g := the threshold of BFT-E** (GV55 "Theorem BFT-E", s ≤ ε_0 there).
- **Data frame class (new name; the level-k analogue of N5-sf0's 𝔑(α)).** For R ≥ 1, α > 0: 𝔑_k(R, α) := {V : for every coarse
  box Ω of side ≤ R′ = 4R + 5 there is a gauge g_Ω on the sites of Ω with d((g_ΩV)_c, 1) ≤ α for every link c ⊂ Ω}.
- **The norm in which "small" is measured** is d(·, 1) on links for data, and for backgrounds the frame-local 𝔐^{(σ)}-norm of
  §1.6 (KFACTOR_OFF55 §1.2's ‖·‖_{(σ)} restricted to a box, in a frame). Both are gauge-invariant notions (they quantify over g).

### 1.2 Lemma C1 (elementary metric facts) — PROVEN-HERE (standard; used throughout)
(a) d(AB, 1) ≤ d(A, 1) + d(B, 1), d(gAg^{−1}, 1) = d(A, 1), d(A^{−1}, 1) = d(A, 1) (bi-invariance: d(AB, 1) ≤ d(AB, A) + d(A, 1) =
d(B, 1) + d(A, 1)). (b) d(e^a, e^{a′}) ≤ |a − a′| for a, a′ ∈ su(N): the path t ↦ e^{a+t(a′−a)} has speed |dexp_{a_t}(a′ − a)|, and
dexp_X = (left translation)∘(1 − e^{−ad X})/ad X with ad X skew-adjoint for the HS product, whose eigenvalues iφ give
|(1 − e^{−iφ})/(iφ)| = |sin(φ/2)/(φ/2)| ≤ 1. ∎ (Part (a) is the fact REVIEW_S18_S19 confirmed inside Lemma AX.)

### 1.3 Lemma C2 (frames for the data = Lemma AX at level k) — CONFIRMED (re-derived; REVIEW_S18_S19 "Lemma AX … CONFIRMED")
Let Ω ⊂ 𝕋_T be a box of side ℓ sites, ℓ ≤ T − 1 (it does not wrap), and V ∈ 𝔅_k(ε) with 3(ℓ − 1)ε < min(π, 2π/√N). The complete
axial gauge from a corner o of Ω (g(x) := transport along the path o → x moving in coordinate 1, then 2, 3, 4) gives
**d((gV)_c, 1) ≤ 3(ℓ − 1)ε for every link c ⊂ Ω** (principal log in su(N), |log(gV)_c| equal to it).
*Re-derivation.* (gV)_c, c = (x, x + e_μ), is the holonomy of (tree path o → x)·c·(tree path o → x + e_μ)^{−1}; the two tree paths
differ by Σ_{ν>μ}(x_ν − o_ν) ≤ 3(ℓ − 1) plaquette moves inside Ω, each multiplying the holonomy by a conjugate of V_P^{±1}; Lemma C1 (a).
The su(N) statement: AX's "|X|² ≥ Σθ_j²" argument. ∎ Complex data e^zV: (g e^zV)_c = e^{Ad_g z_c}(gV)_c, and |log(e^Xe^Y)| ≤ 2(|X| + |Y|)
for |X| + |Y| ≤ ¼ (N5-sf0 (a)'s estimate), so the frame bound becomes 2(3(ℓ − 1)ε + r_ℂε).
**Consequence: 𝔅_k(ε) ⊂ 𝔑_k(R, 3(R′ − 1)ε) for T ≥ R′ + 1 = 4R + 6** (the level-k form of N5-sf0 (a)). Conversely
𝔑_k(R, α) ⊂ 𝔅_k(4α) (every plaquette lies in some Ω; Lemma C1 (a)). **So 𝔅_k and the frame class are the same class up to the
factor 12(R′ − 1): "curvature-small" = "small in a local frame on every box of bounded size".**

### 1.4 Lemma C3 (transition functions are near-constant, not near-identity) — PROVEN-HERE
Let g_Ω, g_{Ω′} be frames of V on boxes Ω, Ω′ (d((g_•V)_c, 1) ≤ α on their links) and t := g_Ω g_{Ω′}^{−1} on the sites of Ω ∩ Ω′.
(a) For every link c = (x, y) ⊂ Ω ∩ Ω′: **d(t(x)^{−1}t(y), 1) ≤ 2α.** *Proof.* With a := (g_{Ω′}V)_c, a′ := (g_ΩV)_c = t(x)a t(y)^{−1}:
t(y) = a′^{−1}t(x)a, so t(x)^{−1}t(y) = (t(x)^{−1}a′^{−1}t(x))·a and Lemma C1 (a) gives ≤ d(a′, 1) + d(a, 1). ∎
(b) Hence on a connected overlap of ℓ¹-diameter D, d(t(x_0)^{−1}t(x), 1) ≤ 2αD: **t = t(x_0)·(near-identity)**, with the constant
t(x_0) ∈ SU(N) **unconstrained** (it encodes the choice of base value of each frame and, around loops of boxes, the holonomy).
(c) The constants cannot in general all be made near 1: around a closed chain of boxes Ω_1, …, Ω_n = Ω_1 the product of the
constants equals, up to the near-identity parts, the holonomy of a loop through the boxes; when that loop is non-contractible or
encloses large flux (Proposition C4) the product is O(1). This is the precise sense of BGT55 §7.1's "transition function
g_□^{−1}Zg_{□′} − 1, which is O(1) somewhere": **O(1) in the constant part, O(α) in the variation** — see the verdict on BGT55
§7.1 in §8.

### 1.5 Proposition C4 (𝒞*_glob is a strict subclass; the size gap is √ε) — PROVEN-HERE
Let N ≥ 2, ε ∈ (0, 1/10], **R_ε := ⌈(√2π/ε)^{1/2}⌉** (so √2π/R_ε² ≤ ε). There is a real V ∈ 𝔅_k(ε) on every torus with
T ≥ 2R_ε + 2 (and on every box containing an R_ε × R_ε square of a coordinate 2-plane) such that **for every gauge g,
max_c d((gV)_c, 1) ≥ √2π/(4R_ε)** (≈ 0.527√ε as ε → 0). Hence V ∉ 𝒞*_glob(s) for s < √2π/(4R_ε).
*Proof.* E(φ) := exp(iφH), H := diag(1, −1, 0, …, 0) ∈ su(N); d(E(φ), 1) = √2|φ| for |φ| ≤ π (principal angles ±φ, AX's
|X|² ≥ Σθ_j² bound, attained by iφH). On the (x_1, x_2)-torus take two disjoint R_ε × R_ε squares Q_±, and the real 2-form Φ with
Φ_P = ±π/R_ε² on the plaquettes of Q_± and 0 elsewhere. Its total is 0, so Φ = dφ for a real 1-form φ (the discrete 2-torus has
one-dimensional second cohomology, detected by the total). Put V(x, μ) := E(φ(x_1, x_2, μ)) for μ = 1, 2 and V(x, μ) := 1 for μ = 3, 4.
Plaquettes in planes other than (1, 2) are 1 (φ does not depend on x_3, x_4); V_P = E(Φ_P) for (1, 2)-plaquettes, so
d(V_P, 1) = √2π/R_ε² ≤ ε. The holonomy of ∂Q_+ is E(Σ_{P⊂Q_+}Φ_P) = E(π) (abelian Stokes, exact for the real-valued φ), so
d(hol, 1) = √2π. In any gauge the holonomy is conjugated (d unchanged) and is a product of the 4R_ε link values of ∂Q_+, so
√2π ≤ 4R_ε·max_c d((gV)_c, 1) by Lemma C1 (a). For a box, Q_+ alone. ∎
**Corollary C5 (what 𝒞_glob covers).**
- (i) **𝔅_k(ε) ⊄ 𝒞*_glob(Cε) for every C ≥ 1 once √2π/(4R_ε) > Cε** (e.g. every ε ≤ 1/(4C²) at C ≥ 1, since then
  R_ε ≤ (√2π/ε)^{1/2} + 1 ≤ 1.13(√2π/ε)^{1/2}). So **no theorem whose constants are linear in the global potential size s (BFT-E,
  K^{(σ)}, Theorem BFT3-glob) can deliver BFT's bounds, which are linear in the curvature ε, on all of 𝔅_k(ε)**: on these data every
  gauge has s ≥ 0.47√ε ≫ ε.
- (ii) For ε ≥ 4ε_g² (roughly), the witness is outside 𝒞*_glob(ε_g) altogether, so BFT-E does not apply to it at all. BFT's class
  needs ε ≤ ε_0 with ε_0 a fixed constant; unless ε_0 is chosen below ≈ 4ε_g² (a choice no consumer of BFT has priced), 𝒞*_glob does
  not even contain 𝔅_k(ε_0).
- (iii) Positive statements. Every V ∈ 𝔅_k(ε) on a box of side ℓ with 3(ℓ − 1)ε ≤ s is in 𝒞*_glob(s) (Lemma C2). Every **flat** V on
  a torus is in 𝒞*_glob(3π√N/T) (Proposition C6). A V with nonzero lattice topological charge (Lüscher's admissible-field charge)
  is in no 𝒞*_glob(s) with s below the admissibility threshold (a small-link field is deformable to 1 through admissible fields) —
  **ARGUED (imports Lüscher's construction; not re-derived)**; such V exist in 𝔅_k(ε) on tori with T ≳ ε^{−1/2} (constant-curvature
  't Hooft-type fields with two flux planes) — ARGUED likewise. Neither item is used below.
- (iv) **What the RG produces.** The level-k data of the lane's soft RG are the level-k links themselves; the small-field condition is
  plaquette-wise, with no condition on holonomies. On the tori of the R⁴ limit (T → ∞ at fixed level) nothing confines the data to
  𝒞*_glob. **So the BFT must be proved on 𝔅^ℂ_k(ε, r_ℂ) itself; 𝒞*_glob(ε_g) is the strict subclass on which one frame suffices.**

### 1.6 Proposition C6 (flat data on tori) — PROVEN-HERE
If V is flat (all V_P = 1) on 𝕋_T, then V ∈ 𝒞*_glob(3π√N/T); and if V ∈ 𝒞*_glob(s) then d(h_μ, 1) ≤ Ts for its cycle holonomies
h_μ. If max_μ d(h_μ, 1) < min(π, 2π/√N) then min{s : V ∈ 𝒞*_glob(s)} = max_μ d(h_μ, 1)/T exactly.
*Proof.* Flatness makes the holonomy a homomorphism ℤ⁴ = π_1(𝕋_T) → SU(N) (lattice loops that are null-homotopic in the torus are
products of conjugated plaquettes), so the h_μ commute and are simultaneously diagonalisable: h_μ = diag(e^{iφ_{μ,j}}), φ ∈ (−π, π],
Σ_jφ_{μ,j} = 2πm_μ, |m_μ| ≤ N/2. Subtract 2π from |m_μ| of the angles (of the sign of m_μ) to get commuting X_μ ∈ su(N) with
e^{X_μ} = h_μ and |X_μ| ≤ 3π√N. W(x, μ) := e^{X_μ/T} is flat with the same holonomy homomorphism; two flat fields with the same
homomorphism are gauge-equivalent (g(x) := T_V(γ_x)T_W(γ_x)^{−1} is path-independent). So V ∈ 𝒞*_glob(max|X_μ|/T). Converse: the cycle
is a loop of T links, Lemma C1 (a). Exactness: in the stated regime the principal logs log h_μ are in su(N), commute (functions of
commuting matrices) and have |log h_μ| = d(h_μ, 1). ∎
This **confirms BGT55 §2.5's "a flat V with holonomy θ around a cycle of coarse length T lies in 𝒞_glob(ε) iff (roughly) θ/T ≲ ε"**
(exact in the stated regime) and §7.1's "connection ≤ 2π/T_b in a constant gauge" up to the constant (3π√N, not 2π, in general).

### 1.7 The background class (what BFT-0 must assert existence and uniqueness in)
For a composite configuration U = (U_0, …, U_{k−1}; V) and a box Ω (side ≤ R′, non-wrapping), a **frame of U on Ω** is a level-0
gauge ĝ on the level-0 sites of Ω whose restriction to the level-k roots is a data frame g_Ω (Lemma C2). Put y := log(U^{ĝ})
(principal logs, all levels, links in Ω) and ‖y‖_{(σ),Ω} := KFACTOR_OFF55's ‖·‖_{(σ)} with every sup and Hölder pair restricted to Ω.
**𝔇_k(R, η) := {U : for every box Ω of side ≤ R′ there is a frame ĝ_Ω with ‖log U^{ĝ_Ω}‖_{(σ),Ω} ≤ η}.**
- It is gauge invariant (frames transform), and it is **the background analogue of N5-sf0's 𝔑(α)**, with the level-0 sup norm
  replaced by the composite 𝔐^{(σ)} norm.
- On 𝒞*_glob(s), BFT-E's slice ball {x ∈ Ker Γ : ‖x‖_{(σ)} ≤ C_0s} lies in 𝔇_k(R, C_0s) (one global frame), so 𝔇 generalises the
  ball in which BFT-E asserts existence and uniqueness.
- BFT-1's gauge-invariant bounds follow from membership: by BA-3 in each frame, own plaquette logs of U_j ≤ L^{−2(k−j)}(2η + 9η²)
  and own soft fluctuations ≤ L^{−(2+σ)(k−1−j)}η + C_ρL^{−3(k−j)}η² (KFACTOR_OFF55 §1.4 (1a)-(1b)), in Hölder form within blocks.
**Target statement for BFT-0/1/2 off 𝒞_glob** (proved as an implication in §6): for V ∈ 𝔅^ℂ_k(ε, r_ℂ), ε ≤ ε_*, T ≥ T_*, there is a
critical point Z(V) ∈ 𝔇_k(R, C_0ε), unique modulo composite gauges trivial at level k in 𝔇_k(R, r_u) (r_u fixed), holomorphic in z;
constants independent of k and T.

**Erratum E1 (to Corollary C5 (i)-(ii), found on re-reading; the text above is left as written).** The displayed range "every
ε ≤ 1/(4C²) … R_ε ≤ 1.13(√2π/ε)^{1/2}" is wrong: at ε = 1/(4C²) the ceiling gives only R_ε ≤ 1.238(√2π/ε)^{1/2}, hence
s ≥ 0.426√ε, which beats Cε only for ε < 0.181/C². Correct statement: **for ε ≤ 1/(6C²) (C ≥ 1), (√2π/ε)^{1/2} ≥ 5.16, R_ε ≤
1.194(√2π/ε)^{1/2}, and every gauge has s ≥ 0.441√ε > Cε** (0.441² = 0.195 > 1/6). In (ii) read "ε ≥ 6ε_g² (with ε ≤ 1/6)":
then 0.441√ε ≥ 1.08ε_g > ε_g. The phrase "every gauge has s ≥ 0.47√ε" in (i) should read 0.44√ε. No conclusion changes.

## §2. T2 — (UHL): three different statements share the name; what is proved, what is false, what is needed

### 2.1 The three statements, pinned
- **(UHL-data)**: a frame for the **level-k data** on a box (BFT_A §3.10's "the background is 𝔐^∇-small in a local gauge" read for
  the data). This is Lemma C2 (= Lemma AX at level k): **PROVEN** (CONFIRMED pre-session-24, re-derived in §1.3).
- **(UHL-fine)**: BFT_A §3.10 (locating "**(UHL)** a lattice local Coulomb (Uhlenbeck-type) gauge on a coarse box of side 3ℓ"):
  for a **composite** configuration (level-0 own spacing n^{−1} := L^{−k} coarse) known only to have coarse curvature
  ‖F^c‖_∞ ≤ ε_0 and [F^c]_α, a gauge with ‖A^c‖ ≤ Cℓε_0 and ‖∇^cA^c‖ + [∇^cA^c]_α ≤ C(ε_0 + [F^c]_α), uniformly in k.
- **(FLAT-REF)**: HESSREL §H6.1's global statement (Z = Z^♭·(small) with Z^♭ flat, in one global gauge).

### 2.2 (FLAT-REF) fails on the √ε witness — PROVEN-HERE
If Z = Z^♭e^{y} with Z^♭ flat and max own|y| ≤ s′ in one global gauge, every **contractible** loop γ has d(hol_γ(Z), 1) ≤ |γ|s′
(flat holonomy of a contractible loop is 1; Lemma C1). Applied to the data level and Proposition C4's witness: s′ ≥ √2π/(4R_ε).
So (FLAT-REF) with s′ = O(ε) is false on 𝔅_k(ε) for small ε, exactly as 𝒞*_glob(Cε) is (Corollary C5 (i)). HESSREL's
"(FLAT-REF) is (UHL)-strength, and it is the wall" is therefore **too weak a description: (FLAT-REF) at size O(ε) is false;
at size O(√ε) it is not excluded by this witness, and no route has been shown to need less than O(ε)** (verdict in §8, P5).

### 2.3 Lemma U1 (the complete axial gauge at the finest level: sup and coarse C^α) — PROVEN-HERE
Let U be a level-0 field on a coarse box Ω of side ℓ (ℓn own steps), with own plaquette holonomies d(U_P, 1) ≤ n^{−2}ε_0, and let
F^c(P) := n²log U^g_P (g the complete axial gauge of Ω from its corner; U^g_P the holonomy of P based at its base corner) with
pointwise coarse Hölder seminorm [F^c]^∞_α over translates at coarse distance ≤ 1 (equivalent to the covariant Campanato version,
NSL55 §2 preamble, since transports along the axial tree are 1 in this gauge). Assume 3ℓε_0 ≤ ½. Then A := log U^g satisfies
  **(a) ‖A^c‖_∞ ≤ 1.1·3ℓε_0,   (b) [A^c]^∞_α ≤ 3.3ℓ[F^c]^∞_α + 1.1ε_0,**
uniformly in k (no power of n survives).
*Proof.* (i) *Exact product form.* In the complete axial gauge (directions reduced in the order 4, 3, 2), for a link
c = (x, x + e_μ) one has U^g_c = Π_{ν = 4, …, μ+1}Π_{y<x_ν}(U^g_{P_{ν,y}})^{−1}, an **ordered product of plaquette holonomies with no
conjugations**: each reduction step x_ν → x_ν − 1 uses one (μ, ν)-plaquette whose two ν-links are tree links (= 1) because all
coordinates beyond ν have already been reduced to the base; the ν-ribbon sits at x_{ν′} = 0 for ν′ > ν. (In d = 2 this is
U^g((a, h), e_1) = U_{P_{h−1}}^{−1}⋯U_{P_0}^{−1}.) At most Σ_{ν>μ}x_ν ≤ 3ℓn factors. (ii) (a): Lemma C1 (a) gives
d(U^g_c, 1) ≤ 3ℓn·n^{−2}ε_0 = 3ℓε_0/n ≤ ½; on d ≤ ½ the principal log is (1.1)-Lipschitz for d (‖(dexp_X)^{−1}‖ ≤ (|X|)/sin|X|
≤ 1.05 for |X| ≤ ½); multiply by n. (iii) (b): let c′ = c + re_λ, coarse distance ρ = r/n ≤ 1. If λ ≤ μ, or for the ν-ribbons with
ν ≠ λ, the factors of U^g_{c′} are the translates by re_λ of those of U^g_c (same order, same number); if λ > μ the λ-ribbon of c′
has r extra factors at its far end and the rest are translates. Bi-invariance gives d(Π a_i, Π b_i) ≤ Σ d(a_i, b_i) and
d(XYZ, XZ) = d(Y, 1); Lemma C1 (b) gives d(U_P, U_{P′}) ≤ |log U_P − log U_{P′}| = n^{−2}|F^c(P) − F^c(P′)| ≤ n^{−2}[F^c]^∞_αρ^α. Hence
d(U^g_c, U^g_{c′}) ≤ 3ℓn·n^{−2}[F^c]^∞_αρ^α + r·n^{−2}ε_0, and n·1.1·(that) ≤ 3.3ℓ[F^c]^∞_αρ^α + 1.1ε_0ρ with ρ ≤ ρ^α. ∎
**So the axial gauge already delivers the sup and the C^α halves of (UHL-fine), with ℓ-linear constants.**

### 2.4 Proposition U2 (the C^{1,α} half fails for the axial gauge, and only for it) — PROVEN-HERE (exact witness)
Abelian (H-direction of §1.5) level-0 field on the (1, 2)-plane with own curvature F(a, y) := n^{−2}Kn^{−α}(−1)^a (a = the x_1
column), K > 0. Then ‖F^c‖_∞ = Kn^{−α}, [F^c]^∞_α ≤ 2K (any two distinct columns are ≥ 1/n apart). **Axial gauge:**
A_1(a, h) = −Σ_{y<h}F(a, y), so the coarse gradient ∇^c_1A^c_1(a, h) = n²(A_1(a + 1, h) − A_1(a, h)) = ±2hKn^{−α}, which at
h = ℓn is **2ℓK·n^{1−α} = 2ℓK·L^{k(1−α)}** — BFT_A §3.10's loss, attained. **Coulomb gauge for the same field:** A_1 = 0,
A_2(a) := −(n^{−2}Kn^{−α}/2)(−1)^a satisfies A_2(a + 1) − A_2(a) = F(a) and d*A = ∂_2A_2 = 0; its coarse gradient is n²·n^{−2}Kn^{−α}
= Kn^{−α} and its coarse Hölder seminorm ≤ 2K: **bounded uniformly in k**. ∎ This **confirms** BFT_A §3.10's "Lemma AX's complete
axial gauge does not give this … loss L^{k(1−α)}" and REVIEW_BFT_A_S1's agreement, with an explicit field, and shows the loss is a
property of the gauge, not of the field.

### 2.5 Theorem U3 ((UHL-fine), reduced) — ARGUED; the precise missing pieces
(UHL-fine) on a box Ω of coarse side ℓ, uniformly in k, follows from:
1. Lemma U1 (sup + C^α of the axial potential) — PROVEN-HERE;
2. **EP-int / LES-div** (GSHARP55 §5.1 (b), "a_X satisfies d*a = 0 and da = dx_0 … LES-div plus Caccioppoli then bound the
   C^{1,α}(N′_X) norm of a_X by C_int times (the L² average of a_X + sup|f_0| + [f_0]_α)"; Codex GSHARP item 1 CONFIRMED) applied
   to the box-Coulomb potential a_X of the axial field: the L² term is ≤ the L² norm of the axial potential (projection
   property), i.e. ≤ Cℓε_0 by U1 (a); so the **linear** S_E projection of the axial field is coarse-C^{1,α} with bound
   C(ℓε_0 + [F^c]_α) — this part is an application of banked results (PROVEN as an implication, at the linearised level);
3. a **nonlinear bootstrap at the C^α level**: the nonlinear gauge action differs from the linear one by BCH terms [ξ, A] that
   are only C^α when A is (λ^E_X(A) ∈ C^{1,α} for A ∈ C^α), so NSL55's contraction (which needs n_0 = C^{1,α} smallness of its
   input, NSL55 §2 "(a), (b), (d)-(f) need only n_0(x) ≤ a_N") cannot be started from the axial field directly. The standard fix
   (Uhlenbeck): solve the gauge condition at the C^α level, then improve regularity from the curvature equation
   da + [a ∧ a] = F (the right side is C^α) by EP-int — **ARGUED, not written**;
4. NSL55 Theorem NSL to land in S_E^{(k)} with C^{1,α} bounds — Opus PROVEN-HERE, **Codex pending**.
The constants are linear in ℓ (U1) and cannot be uniform in the box side: by Proposition C4, on boxes of side ℓ ≳ ε^{−1/2} no gauge
has potentials O(ε). **"Uniform in the box" can only mean "uniform for boxes of bounded coarse side" — as pre-stated.**
Uniqueness: within the frame-local ♮-ball the slice gauge is unique given its values at the level-k roots (NSL (a)); the root values
are the data frame of Lemma C2, unique up to one constant per box — the constant part of the transition functions (Lemma C3).

### 2.6 Theorem U4 ((UHL-fine) is not an input of BFT-0/1/2 on the frame route) — PROVEN (as a statement about §6's proof)
In §6's construction the fine-level frame of each box is **not** produced from curvature information. It is inherited from a
configuration already known to be frame-locally 𝔐^{(σ)}-small (the depth-(k−1) background, §6.3), re-patched on larger boxes
(Lemma FP, §6.2), and put into the frame's S_E slice by NSL. The background's own coarse C^{1,α} smallness in each frame is then an
**output** (the a priori estimate, §6.4). (UHL-fine) is needed only to apply the local estimates to a configuration **not** produced
that way — e.g. to upgrade BFT-0's uniqueness from "in 𝔇_k(R, r_u)" to "among all critical points of curvature ≤ Cε", or for a BFT-5
consumer handed an arbitrary small-curvature background. For BFT-0/1/2 as REVIEW_S22 states them (existence, uniqueness in a ball,
regularity, analyticity) it is not consumed. The same holds for (SL-cov) (§6.6).

**Erratum E2 (to Lemma U1's proof (ii), loose justification; statement unchanged).** "‖(dexp_X)^{−1}‖ ≤ |X|/sin|X| ≤ 1.05 for
|X| ≤ ½" is not the right bound for the geodesic between two links. Correct reason: both endpoints are within 3ℓε_0/n ≤ 1/(2n) ≤ 1/6
of 1, so every point of the geodesic between them is within 1/3, where ‖(dexp)^{−1}‖ ≤ (1/3)/sin(1/3) < 1.02; the factor 1.1 in
(a)-(b) is therefore safe (and in (a) not even needed: |log W| = d(W, 1) in the su(N) regime). Also, Proposition C4 holds for
every ε ∈ (0, 1/6] (the proof never used ε ≤ 1/10), which is the range Erratum E1 uses.

## §3. T3, first half — covariant routing and the local cc-decomposition at ANY configuration (LOC-cc_U)

### 3.1 Setting (conventions of BGT55 §1-§3, KFACTOR_OFF55 §1.1)
U = (U_0, …, U_{k−1}; V) any composite configuration (not necessarily critical, small or real-analytic); tangent vectors and
sources left-trivialised at base sites. For a level-0 su(N)-valued λ and a level-l link b = (y → y′):
(Ξ_Uλ)_l(b) := Ad_{U_l(b)}λ(y′) − λ(y) (λ evaluated at level-l sites = their level-0 images). **D_U := Ξ_U^T**, i.e.
  **D_U(S)(z) = Σ_l [Σ_{b: y′(b)=z} Ad_{U_l(b)}^{−1}S_l(b) − Σ_{b: y(b)=z} S_l(b)]**,
D_U^⊥ := its restriction to the level-0 sites that are not level-k roots; **cc_U := Ker D_U^⊥** (BGT55's cc_Z: Ξ_Z^TS = 0 on Λ_0 = Λ_*).
At U = 1 these are KFACTOR_OFF55's D, D^⊥, cc.

### 3.2 Lemma HR_U (covariant hierarchical routing) — PROVEN-HERE (exact; check og55_1)
Use HR's geometry (KFACTOR_OFF55 §3.3: nested roots, R(Z) the root of the parent block of a level-j site Z, γ(Z) the level-j axial
path R(Z) = x_0 → x_1 → … → x_m = Z inside the block). For a level-j path γ put T_U(γ) := U_j(b_1)⋯U_j(b_m) (transport from x_0 to
x_m; under gauges T ↦ g(x_0)Tg(x_m)^{−1}) and T_{U,i}(γ) := U_j(b_i)⋯U_j(b_m). For a level-0 function u define recursively
  V^U_0 := u,   **V^U_{j+1}(Y) := Σ_{Z ∈ level-(j+1) block Y} Ad_{T_U(γ(Z))}V^U_j(Z)**   (placed at the root R_Y),
  **(P_U^Tu)_j(b_i(Z)) := Ad_{T_{U,i}(γ(Z))}V^U_j(Z)**  on the i-th link of γ(Z), summed over Z (0 ≤ j ≤ k − 1).
- **(i) Identity.** D_U(P_U^Tu) = u − Σ_X V^U_k(X)δ_{r_X}; in particular **D_U^⊥(P_U^Tu) = u^⊥** for every U.
- **(ii) Gauge covariance.** P_{U^g}^T(Ad_g u) = M_g P_U^T u (M_g = Ad_{g(base)} on links): routing commutes with frames.
- **(v) Bare charges, unchanged constant.** If u = ev^{(j)T}v then **J(P_U^Tu) ≤ (M_γ/(L − 1))·L^{d(k−j)}·sup|v|** — HR (v) verbatim.
*Proof.* (i) On a path with currents J_i on b_i, D_U receives Ad_{U(b_i)}^{−1}J_i at x_i and −J_i at x_{i−1}. With
J_i = Ad_{T_{U,i}}V(Z): at an interior x_i (0 < i < m) Ad_{U(b_i)}^{−1}Ad_{U(b_i)⋯U(b_m)}V − Ad_{U(b_{i+1})⋯U(b_m)}V = 0; at Z = x_m,
Ad_{U(b_m)}^{−1}Ad_{U(b_m)}V = V(Z); at x_0, −Ad_{T_U(γ)}V(Z). An empty path (Z = R(Z)) contributes V(Z) − V(Z) at the same site, and is
included in the sum defining V^U_{j+1}. So the level-j divergence is V^U_j(Z) at every level-j site minus V^U_{j+1}(Y) at each root
R_Y — HR (i)'s formula with V_{j+1} replaced by its transported version — and the telescoping over levels (HR's proof of (i),
unchanged: a site whose top level is J < k receives Σ_{j<J}(V^U_j − V^U_{j+1}) + V^U_J = V^U_0 = u) gives the claim. (ii)
T_{U^g}(γ) = g(x_0)T_U(γ)g(x_m)^{−1}, so every transported charge and current is rotated by Ad_{g(base)}. (v) Ad is an isometry, so
|V^U_i| ≤ Σ|V^U_{i−1}| and every count of HR (v)'s proof is unchanged. ∎
**No smallness, no flatness and no criticality of U is used.** (HR (iii)-(iv) — routing a *divergence* — do **not** transfer
verbatim: transporting the two ends of an interior link to the root along different axial paths leaves the holonomy defect
(Ad_{hol^{−1}} − 1)w(b) of a small loop. They are not needed below.)

### 3.3 Lemma CCL_U (cut-off charges of a cc_U source are bare charges, with the 𝒞_glob constants) — PROVEN-HERE
Let S ∈ cc_U have a covariant representation S = d_{U_0}^TG_0 + Σ_l⟨s_l, r^U_l(·)⟩ + j (BGT55 §2.2's N_Z slots in KFACTOR_OFF55's
σ-form: G at level 0 only; (d_Ux)(P) := d/dt log U_P(e^{tx}U)|_0 for the holonomy based at base(P); r^U_l := the linearisation at
U of the soft residual ρ_l). Let χ be a scalar cutoff with coarse gradient ≤ 1/ℓ_χ, acting slot-wise (M_χ: G(P) ↦ χ(m_P)G(P),
s(c) ↦ χ(m_c)s(c), j(b) ↦ χ(m_b)j(b); midpoints m). Then at every non-root site z
  **D_U(M_χS)(z) = Σ_slots (D_U(M_χ slot)(z) − χ(z)D_U(slot)(z))**   (because χ(z)D_U(S)(z) = 0),
and each bracket is a **bare charge**:
- (j) Σ_{b∋z}(χ(m_b) − χ(z))(transported ±j_l(b)): |·| ≤ (d/ℓ_χ)L^{−(k−l)}sup_own|j_l| — Codex BFT34 R5's bound, by Ad-invariance;
- (G) Σ_{P: base(P)=z}(χ(m_P) − χ(z))[log U_P, G_0(P)] (from the exact identity (d_UΞ_Uλ)(P) = [λ(base P), log U_P], the based
  holonomy being conjugated by g(base P)): |·| ≤ 6√2·n^{−1}ℓ_χ^{−1}·|log U_P|·|G_0(P)| ≤ 6√2 n^{−5}η_F|G^c_0|/ℓ_χ, η_F := sup_P n²|log U_P|;
- (s) Σ_{c: end(c)=z}(χ(m_c) − χ(z))[ρ_c(U), s_l(c)] at level-(l+1) sites (from the exact covariance ρ(U^g)(c) = Ad_{g(c_Y)}ρ(U)(c),
  NSL55 Lemma D / CODEX_REVIEW_BGT §4 in actual-generator form; sign immaterial for sizes): |·| ≤ 2d·L^{−(k−l−1)}ℓ_χ^{−1}|ρ_c||s_l(c)|.
Routing them with Lemma HR_U (v) costs, in J:
  **J ≤ (dM_γ/((L − 1)ℓ_χ))·J(j) + (6√2M_γ/((L − 1)nℓ_χ))·η_F‖G^c_0‖_∞ + (8dM_γ/((L − 1)ℓ_χ))·η_ρ·Σ_lL^{−(1+2σ)(k−1−l)}·‖s‖_{R(σ)},**
with η_ρ := max_l L^{(2+σ)(k−1−l)}sup_own|ρ_l(U)| (≤ 2η on 𝔇_k(R, η) in a frame: KFACTOR_OFF55 §1.4 (1b); ρ is covariant, so the sup
is frame-free). The first term is CCL's (216/ℓ_χ·¼ at d = 4, L = 3); the second is **n^{−1}-small**; the third is O(η), summable.
*Proof of the three identities.* (j): Codex BFT34 R5's computation with Ad_{U(b)}^{±1} inserted (isometries). (G): ⟨G_0, d_U(Ξ_Uλ)⟩
with U_P(U^{e^{tλ}}) = e^{tλ(z)}U_Pe^{−tλ(z)} at z = base(P) gives d/dt log(e^{tλ}e^{w}e^{−tλ}) = [λ(z), w], w := log U_P, so
D_U(d_U^TG_0)(z) = Σ_{P:base=z}[w_P, G_0(P)] (ad skew), and multiplying G_0(P) by χ(m_P) gives the bracket. (s): the same with
ρ(U^{e^{tλ}})(c) = Ad_{e^{tλ(c_Y)}}ρ(U)(c). Sizes: |[a, b]| ≤ 2|a||b|; |χ(m) − χ(z)| ≤ (half a link)·|∇χ|; own-unit conversions as in
KFACTOR_OFF55 §1.1. ∎

### 3.4 Proposition LOC-cc_U (BGT55 §7.2's (LOC-cc_Z), at every configuration) — PROVEN-HERE
Let {χ_□} be RW-cc's partition (BFT34_55 §2.5: Σχ_□ = 1, supp χ_□ ⊂ □^{(1)}, coarse gradient ≤ 4, so ℓ_χ = ¼). For S ∈ cc_U put
  **S_□ := P_cc^U(M_{χ_□}S),  P_cc^U := 1 − P_U^TD_U^⊥.**
Then: (a) **Σ_□S_□ = S**; (b) **every S_□ ∈ cc_U**; (c) supp S_□ ⊂ the coarse cells meeting □^{(1)}; (d) with C_loc :=
1 + 4 + 216 + 8·6√2·M_γ/((L − 1)n) + 32dM_γη_ρ/((L − 1)(1 − L^{−1})) (d = 4, L = 3: 221 + O(n^{−1}) + O(η_ρ)),
  **N^{(σ)}_U(S_□) ≤ C_loc·N^{(σ)}_U(S; □^{(1)})** (N restricted to representations' values on the cells of □^{(1)}; the "4" is
[χG]_α ≤ [G]_α + 4 sup|G|);
(e) for every m ≥ 0 and weight centre X_0, **Σ_□e^{−m·dist(□, X_0)}N^{(σ)}_U(S_□) ≤ C_loc·e^{2m}·K_R(m)·N^{(σ)}_{U,m}(S)**,
K_R(m) := sup_{X_0}Σ_□e^{−2m·dist(□, X_0)} (finite and T-independent for m > 0; K_R(0) = number of boxes, so at m = 0 the sum form
holds only with the max over □ in place of the sum).
*Proof.* (a) P_cc^U is linear and Σ_□M_{χ_□} = 1 on representations, so Σ_□S_□ = P_cc^US = S − P_U^TD_U^⊥S = S. (b) Lemma HR_U (i):
D_U^⊥(P_cc^Uw) = D_U^⊥w − D_U^⊥w = 0. (c) Supports of M_{χ_□}S and of the routing paths (one coarse cell per charge). (d) Lemma CCL_U
with ℓ_χ = ¼. (e) Local sups of S on □^{(1)} are ≤ e^{−m·dist(□^{(1)}, X_0)}× the weighted norm; sum over □. ∎
**Answer to the brief's question "keep every source composite-co-closed (cut-off sources are NOT cc)"**: the cut-off pieces are made
cc_U **exactly**, at every configuration, by routing their bare charges covariantly; the cost is BFT34_55's Lemma CCL constant
(216 → 221 with the G- and s-slot charges), now with no transition function at all: the routing uses U's own transports, which are
frame-free (Lemma HR_U (ii)).

### 3.5 Proposition RW-cc_Z (the cc walk at a critical background, with frames) — identities PROVEN-HERE; bounds as named
Let Z be a **critical** configuration, {□} RW-cc's boxes, ψ_□ RW-cc's cutoffs (= 1 on □^{(R/2)}, scale R/4), 𝕋_□ local tori with
root-preserving embeddings ι_□, and **frames ĝ_□** (§1.7) on □^{(R)}; let Z_□ be any configuration on 𝕋_□ that equals ι_*(Z^{ĝ_□})
on a neighbourhood of ι(supp ψ_□) (the transplanted background) and H_□ := its Hessian. For S ∈ cc_Z: y_□ := S_□ (§3.4),
u_□ := a response on 𝕋_□ to ι_*M_{ĝ_□}y_□ (any representative), P̃S := Σ_□ψ_□M_{ĝ_□}^{−1}ι^*u_□, c_□ := the commutator source,
R̃S := −Σ_□c_□. Then exactly as Proposition RW-cc (CODEX_REVIEW_BFT34 R5, confirmed at Z = 1):
(a) Σ_□y_□ = S, y_□ ∈ cc_Z; (b) ι_*M_{ĝ_□}y_□ ∈ cc_{Z_□} on 𝕋_□, so u_□ exists **iff** Ker H_□ = Ran Ξ_{Z_□} on 𝕋_□ ((N1-nd) on the
local torus — supplied on 𝒞*_glob-type local backgrounds by Proposition L2 (b) below); (c) H_Z(P̃S) = S − R̃S;
(d) **each c_□ ∈ cc_Z**: Ξ_Z^Tc_□ = Ξ_Z^TH_Z(ψ_□…) − Ξ_Z^Ty_□ = 0 − 0, by KER_Z (CODEX_REVIEW_BGT item 4: H_ZΞ_Z = 0 at a critical Z)
and (a). Frames enter only through ι_*M_{ĝ_□} and M_{ĝ_□}^{−1}, which are isometries of the covariant norms (Lemma OC; N5-cov).
**At a non-critical U (d) fails by exactly the term −(DΞ_U[ψ_□u_□])^T∇F(U)** (differentiate the gauge identity ⟨Ξ_Uλ, ∇F(U)⟩ = 0):
the walk then leaves cc_U by O(‖∇F(U)‖·‖u‖), which §5 absorbs with one more P_cc^U.
**Transition functions.** None appear in (a)-(d): the decomposition is covariant (§3.4), the local problems are solved in their own
frames, and the results are rotated back. Had one routed in each frame with the **flat** P^T of that frame (BFT34_55's literal
construction, transplanted), the pieces would be cc for the frame's pure gauge P_□ := 1^{ĝ_□^{−1}} instead of cc_Z; the mismatch is the
bare charge (K′_y^T·)^⊥ of KFACTOR_OFF55 CCP (c), whose routing costs ≤ 2dc_BernL^{d−1}·max_j‖y^c_j‖·J (≤ 127.44 × frame-local
potential at d = 4, L = 3): **the flat routing also works, up to an O(η) error, and constant transition rotations cost nothing**
(Ad_c commutes with d, d*, P^T). So BFT34_55's routing survives transition functions; the covariant form is simply cleaner.

**Erratum E3 (to §3.5 (b), found on re-reading).** "u_□ exists iff Ker H_□ = Ran Ξ_{Z_□}" is not enough as stated: Ran H_□ =
Ann(Ker H_□) contains cc_{Z_□} only if Ker H_□ ⊆ Ran Ξ_{Z_□}, and the inclusion Ran Ξ_{Z_□} ⊆ Ker H_□ (KER) needs Z_□ **critical on
𝕋_□** — which an exact transplant of Z near ψ_□ does not give (Z_□ is arbitrary away from the transplant region). The exact identities
(c)-(d) need both properties at once, and they are not compatible in general. **Consequence: Proposition RW-cc_Z's identity part (a),
(c), (d) stands for whatever local responses exist; existence and bounds of the local responses are not supplied by an exact local
inverse of H_□. §5 therefore uses the K^{(σ)} local operators 𝒦_y of §4, which need no criticality, and pays O(η + ‖∇F‖) errors.**

## §4. The local linear operators (the K^{(σ)} linearisation), and what they give at a critical point

### 4.1 Lemma L1 (𝒦_y is invertible on cc sources at every point of a fixed-radius ball, not only on the slice) — PROVEN as an implication
*Hypotheses* = Theorem K^{(σ)}'s (KFACTOR_OFF55 §4.5; banked conditionally, CODEX_REVIEW_GV item 4): 𝒞_glob on a torus of side ≥ 3,
data B with s := ‖B‖_D ≤ ε_0, Γ with ΓΞ = −1 on Λ_* and (GV^{(σ)})_Γ (GV-E, CODEX_REVIEW_GV item 2); G_♯ := G_inv(σ) + G_gv;
K_rows, K_C(σ) of §4.5. Put **r_lin := (8G_♯(K_rows + K_C))^{−1} − s/2** (also ≤ η_0 and < (2dc_BernL^{d−1})^{−1}).
For every y (anywhere in 𝔐^{(σ)}, **not** required to lie in Ker Γ) with ‖y‖_{(σ)} ≤ r_lin:
- (a) **𝒦_y := 𝓛_Γ − D_yS̃(y; B) = P_cc H^{log}_y + Γ^TΓ**, H^{log}_y := D∇F(y) the Hessian of F = 𝔉_k∘exp(·; B) at y, P_cc = 1 − P^TD^⊥;
- (b) for every cc f there is exactly one u with 𝒦_yu = f; **Γu = 0 and ‖u‖_{(σ)} ≤ 2G_♯N^{(σ)}(f)**; u is holomorphic in (y, B) on the
  polydisc where K^{(σ)}'s estimates hold (Codex KOFF §4.3: "Complexification gives the same assertion on a smaller complex polydisc").
*Proof.* (a) 𝔑^0(y) = Hy − NB − ∇F(y), so D_yS̃ = P_cc(H − H^{log}_y) = H − P_ccH^{log}_y (D^⊥(Hu) = ((HΞ)^Tu)^⊥ = 0). (b) K^{(σ)}'s
proof bounds the N^{(σ)}-Lipschitz constant of y ↦ S̃(y; B) by 2(K_rows + K_C)(‖y‖ + ‖y′‖ + s) **on the full ball** — ROW^{(σ)} and
Proposition CB are stated "for ‖x‖_{(σ)}, ‖x′‖_{(σ)} ≤ η", with no slice condition — so ‖D_yS̃(y)u‖_{N^{(σ)}} ≤ ‖u‖_{(σ)}/(2G_♯) for
‖y‖ ≤ r_lin. Every value D_yS̃(y)u is cc (CCP (a); D^⊥ is linear and (y, B)-independent). 𝓛_Γ^{−1} maps cc sources into Ker Γ with
norm ≤ G_♯ (LIN^{(σ)} + (GV^{(σ)})_Γ). So T := 𝓛_Γ^{−1}D_yS̃(y) has ‖T‖ ≤ ½ on all of 𝔐^{(σ)}, and 𝒦_yu = f ⟺ u = (1 − T)^{−1}𝓛_Γ^{−1}f
(𝓛_Γ is invertible on the whole finite-dimensional space). Γu = 0: D(Γ^Tμ) = (ΓΞ)^Tμ = −μ for μ ∈ Λ_*, so applying D^⊥ to 𝒦_yu = f
gives −Γu = D^⊥f − D^⊥(P_ccH^{log}u) = 0. Holomorphy: a Neumann series of holomorphic operators, uniformly convergent. ∎
*Scope note for Codex.* The banked statement (CODEX_REVIEW_GV item 4) is the contraction on the **slice** ball. Lemma L1 uses the
same estimate on the full ball and in all directions u; the claim is that K^{(σ)}'s proof never used Γy = 0 or Γu = 0 in the
Lipschitz bound. I checked ROW^{(σ)} (a)-(c), CB and §4.5's proof text for that; nothing else.

### 4.2 Proposition L2 (at a critical point: slice solutions, (N1-nd), and a slice-form background estimate on 𝒞_glob) — PROVEN as an implication
Let ȳ be a critical point of F with ‖ȳ‖_{(σ)} ≤ r_lin and **max_j‖ȳ^c_j‖_∞ ≤ η′ < (2dc_BernL^{d−1})^{−1}** (≥ 1/127.44 at d = 4,
L = 3; KFACTOR_OFF55 §4.6 erratum), and let K_ȳ be the infinitesimal composite gauge action at ȳ (K_ȳλ = d/dt log((e^ȳ)^{e^{tλ}})|_0,
λ ∈ Λ_*; KFACTOR_OFF55 §1.1, K_ȳ = −Ξ + K′_ȳ).
- **(a)** For every source f with **K_ȳ^Tf = 0** (f annihilates the background's gauge directions) there is exactly one u ∈ Ker Γ with
  **H^{log}_ȳu = f**, namely **u = 𝒦_ȳ^{−1}(P_ccf)**; hence ‖u‖_{(σ)} ≤ 2G_♯N^{(σ)}(P_ccf).
- **(b)** If ΓK_ȳ is invertible on Λ_* (NSL55 (f): M_FP(x) = Λ∘K_x = 1 + (‖·‖ ≤ ¼) for n_0(x) ≤ a_N, Opus PROVEN-HERE, Codex pending; or
  directly ΓK_ȳ = −1 + ΓK′_ȳ with ‖ΓK′_ȳ‖ < 1), then **Ker H^{log}_ȳ = K_ȳΛ_*** — **(N1-nd) at ȳ**.
- **(c)** For f a plain-current chain with K_ȳ^Tf = 0: J(P^TD^⊥f) ≤ 2dc_BernL^{d−1}η′·J(f), so N^{(σ)}(P_ccf) ≤ (1 + 127.44η′)N^{(σ)}(f).
*Proof.* (a) Existence: P_ccf is cc (HR (i)); u := 𝒦_ȳ^{−1}(P_ccf) has Γu = 0 and P_ccH^{log}_ȳu = P_ccf (Lemma L1), so g := H^{log}_ȳu − f
satisfies g = P^TD^⊥g. At a critical point H^{log}_ȳK_ȳ = 0 (differentiate ⟨∇F(y), K_yλ⟩ ≡ 0 at ȳ; the extra term carries ∇F(ȳ) = 0;
symmetry), so K_ȳ^Tg = −K_ȳ^Tf = 0, i.e. Ξ^Tg = K′^T_ȳg on Λ_*, i.e. D^⊥g = (K′^T_ȳg)^⊥. Hence g = P^T(K′^T_ȳg)^⊥ and CCP (c) gives
J(g) ≤ 2dc_BernL^{d−1}η′J(g) < J(g) unless g = 0 — **CCP (d)'s argument verbatim**. Uniqueness: two solutions in Ker Γ differ by w
with 𝒦_ȳw = P_ccH^{log}w = 0, so w = 0 by Lemma L1 (b). (b) "⊇" is KER at ȳ. "⊆": if H^{log}_ȳu = 0, put μ := −(ΓK_ȳ)^{−1}Γu and
u_s := u + K_ȳμ; then Γu_s = 0, H^{log}u_s = 0, and (a) with f = 0 gives u_s = 0. (c) D^⊥f = (K′^T_ȳf)^⊥ by K_ȳ^Tf = 0; CCP (c). ∎
**What this is, relative to BGT55's (R2).** On 𝒞*_glob, at the K^{(σ)} fixed point x* (critical, in the slice ball C_0s ≤ r_lin), (a)-(b)
are **(R2)(a)-(b) in slice form**: (N1-nd) at Z = e^{x*} and a uniform bound for the slice response to every background-cc source, in
the σ-pair, **with no alignment Υ and no S_E completion**. The two steps that separate it from BGT55's literal (R2) (covariant
orbit norm 𝔐^∇_Z, covariant source norm N_Z) are named below: **Lemma NE** (frame/covariant norm comparison) and **Lemma CONV**
(N^{(σ)}(P_ccJ^TS) ≤ C·N^{(σ)}_Z(S) for S ∈ cc_Z, J the dexp chart map). Proposition L2 (c) is CONV's plain-current slot.
The mechanism differs from Theorem GA's: GA works in the **orbit** norm, where the unaligned difference H_Z − H_1 cannot be fed to the
cc inverse (it is not cc-valued) and an exact alignment is needed; here the slice fixes the gauge, the difference is measured in the
**full** field norm (where K^{(σ)} already bounds it: Lemma L1), and the background-cc / flat-cc mismatch is the bare charge (K′^T·)^⊥,
which the **hierarchical** routing prices at O(η′) (CCP (c)) — the S_E completion Λ_E^T, whose spikes BGT55 §6.4 counts, never occurs.
This is the same replacement (Λ_E^T → P^T) that KFACTOR_OFF55 §3.6 made for the nonlinear contraction.

### 4.3 The two comparison lemmas (named inputs; ARGUED)
- **Lemma NE (norm equivalence in a frame).** If U^{ĝ} = e^y on Ω with ‖y‖_{(σ),Ω} ≤ η ≤ η_NE, then for tangent vectors v at U supported in
  Ω and their frame log-coordinates δy = J_y^{−1}M_ĝv: ‖δy‖_{(σ),Ω} ≤ (1 + C_NEη)‖v‖_{𝔐_U,Ω}, and conversely; likewise for sources with
  J_y^T. **Status: ARGUED** (transports along axial paths of coarse length ≤ 1 rotate by angles ≤ η; dexp = 1 + O(η); Hölder
  seminorms of products: NSL55 Lemma B's algebra). It is the comparison Codex BGT §6.4 lists as missing ("nor does it by itself compare
  the flat sharp norm with the covariant sharp norm after the J(z) chart change").
- **Lemma CONV (source conversion).** For S ∈ cc_U with covariant slots (G_0, s, j) and f := J_y^TM_ĝS: K_y^Tf = 0 and
  N^{(σ)}(P_ccf) ≤ (1 + C_CVη)N^{(σ)}_U(S). **Status: plain-current slot PROVEN (Proposition L2 (c)); G- and s-slots ARGUED** — the
  charges (K′^T_y d^TG_0)^⊥ are mostly the divergence of the plain current [y_0, G_0] (route by HR (iv), Hölder, k-uniform since
  [y^c_0]_α ≤ η) plus bare charges [dy_0, G_0] of own size n^{−4}η|G^c| (HR (v): O(η)); the s-slot charges are neutral within each
  level-(l+1) block up to the residual [r_l(y), ·] (route at level l only, cost ≲ L^{2+σ}L^{−σ(k−l)}η‖s‖, summable). Not written out.

### 4.4 Check og55_1 (record) — OVERALL PASS
Criteria `checks/og55_1_criteria.md` written 04:10:59Z, before the script `checks/og55_1_route.py` (written 04:12:12Z). **One run**,
04:12:48-04:12:53Z, `nice -n 10 python3 -I -B`, exact Fractions only, 5.22 s, 37 MB peak (`checks/og55_1_out.txt`,
`checks/og55_1_err.txt` = /usr/bin/time report). No criterion edited. Models M1 (d=2, k=2, T=1), M2 (d=2, k=2, T=2), M3 (d=2,
k=3, T=1), M4 (d=3, k=2, T=1), L = 3, generic curved backgrounds (random rational SO(3) = Ad(SU(2)) link matrices, Cayley form,
R^TR = I and det = 1 asserted exactly). **A0-A5 PASS in all four models (24/24)**: adjointness of D_U and Ξ_U; Lemma HR_U (i)
D_U(P_U^Tu) = u − Σ_XV^U_k(X)δ_{r_X}; HR_U (ii) covariance under a random rational gauge; LOC-cc_U (a)-(b) (S := P_cc^U(S_raw) is
cc_U, three rational partition pieces sum to S and are each cc_U); flat limit = KFACTOR_OFF55 HR's P^Tu. **All five controls fire in
all four models (20/20)**: flat routing at curved U leaves a piece non-cc_U (C1) and violates the identity (C2); a non-cc source is
not reproduced (C3); the wrong sign on reversed links (C4) and transport on the wrong side (C5) break the identity. *Cannot decide*
(stated before running): no norm bound, no G-/s-slot charges, no Hessian, no d = 4, no uniformity.

## §5. T3, second half — (G♯-patch) as a right inverse at every frame-locally small configuration

### 5.1 Setting
V ∈ 𝔅^ℂ_k(ε, r_ℂ) on 𝕋_T, T ≥ T_* := 4R + 6; RW-cc's product partition {□} (sides in [R, 2R)), χ_□ (§3.4), ψ_□ (= 1 on □^{(R/2)},
supp ⊂ □^{(R)}, coarse gradient ≤ 4/R), local tori 𝕋_□ of side 4R + 22 with root-preserving embeddings ι_□. Configurations U are
**global**; frames are only a device for estimates. For U ∈ 𝔇_k(R, η) fix frames ĝ_□ on Ω_□ := □^{(R+3)} (side ≤ R′) and write
y_□ := log U^{ĝ_□} (‖y_□‖_{(σ),Ω_□} ≤ η). Norms: **‖w‖_𝔇 := max_□‖frame-□ log-coordinates of w on Ω_□‖_{(σ)}** for tangent
vectors, **N_𝔇(f) := max_□N^{(σ)}(frame-□ representation of f on Ω_□)** for sources (frame-dependence is controlled by Lemma NE
and Lemma C3: constants rotate isometrically, near-identity parts cost 1 + O(η)). G(U) := ∇𝔉_k(U; V) left-trivialised (always in
cc_U by gauge invariance), DG(U)w := d/dt G(e^{tw}U)|_0. Local data on 𝕋_□: B̃_□ := ι_*(φ_□ log(g_□V)) and local configuration
ỹ_□ := ι_*(φ_□y_□), φ_□ = 1 on □^{(R+1)}, supported in Ω_□ (coarse scale 1). Lemma C2: ‖B̃_□‖_D ≤ s_R := 2(3(R′ − 1) + r_ℂ)ε.

### 5.2 Theorem GP (frame-patched right inverse) — PROVEN as an implication
*Inputs:* Lemma L1 on each 𝕋_□ (K^{(σ)} chain + GV-E, Codex-conditional); Lemma HR_U and Proposition LOC-cc_U (PROVEN-HERE, og55_1);
Lemma CONV and Lemma NE (§4.3, ARGUED; CONV's plain-current slot PROVEN); **(W-comm)^σ** — ‖[H^{log}_ỹ, ψ_□]u‖_{N^{(σ)}} +
‖[Γ, ψ_□]u‖_♮ ≤ (C_c/R)‖u‖_{(σ)} for ‖ỹ‖ ≤ r_lin (BFT34_55 §2.5, ARGUED there at ỹ = 0 with CODEX_REVIEW_BFT34 R6's exponent
correction L^{3+σ} → L^{4+σ}; the ỹ-dependent part is O(η/R) by the same local bounds) — **ARGUED**; **W-mult^σ** — ‖φu‖_{(σ)} ≤
C_M‖u‖_{(σ)} for cutoffs of coarse scale ≥ 1 (BFT34_55 §2.5, ARGUED); the non-criticality defect bound **(ND)**:
J(P_U^T(((DΞ_U[w])^TG(U))^⊥)) ≤ K_3N_𝔇(G(U))‖w‖_𝔇 (same mechanism as CONV; ARGUED).
*Statement.* There are R_GP, η_GP, β, depending only on (N, L, κ_±, α, θ, σ) and the input constants — **not on k, T** — such that
for R ≥ R_GP, s_R ≤ ε_0, and every U ∈ 𝔇_k(R, η) with η ≤ η_GP: the operator
  **𝒫_Uf := Σ_□ M_{ĝ_□}^{−1}J_{y_□}ψ_□ ι^*𝒦_□^{−1} ι_* P_cc (J_{y_□}^T M_{ĝ_□} P_cc^U(M_{χ_□}f)),   𝒦_□ := 𝒦_{ỹ_□} on 𝕋_□ (Lemma L1),**
satisfies, on cc_U, **E_U := P_cc^U DG(U)𝒫_U − 1 with N_𝔇(E_Uf) ≤ C_E(1/R + η + N_𝔇(G(U)))N_𝔇(f)**, and for C_E(1/R + η +
N_𝔇(G(U))) ≤ ½ the operator **R_U := 𝒫_U(1 + E_U)^{−1}** obeys **P_cc^UDG(U)R_U = 1 on cc_U and ‖R_Uf‖_𝔇 ≤ βN_𝔇(f)**, with
β := 2·5^d·2G_♯·C_loc·(1 + C_CVη)(1 + C_NEη)C_M. If U = Z is **critical**, DG(Z) maps into cc_Z, so **DG(Z)R_Z = 1 on cc_Z exactly.**
*Proof.* Fix f ∈ cc_U, f_□ := P_cc^U(M_{χ_□}f) ∈ cc_U, supported in □^{(2)}, Σ_□f_□ = f, N(f_□) ≤ C_loc N(f) (Proposition LOC-cc_U).
In frame □, f̂_□ := J^TM f_□ annihilates the background gauge directions K_{y} (cc_U in log coordinates); P_cc f̂_□ is flat-cc with
N^{(σ)}(P_ccf̂_□) ≤ (1 + C_CVη)N(f_□) (CONV). u_□ := 𝒦_□^{−1}ι_*P_ccf̂_□ exists, Γu_□ = 0, ‖u_□‖ ≤ 2G_♯(1 + C_CVη)C_locN(f) (Lemma L1;
ỹ_□ in the r_lin-ball by W-mult^σ for η small). From 𝒦_□u = P_ccf̂ and Γu = 0: H^{log}_ỹu = f̂ − P^TD^⊥f̂ + P^TD^⊥(H^{log}_ỹu); by the
gauge identity at ỹ (differentiate ⟨K_yλ, ∇F(y)⟩ ≡ 0), D^⊥(H^{log}_ỹu) = (K′^T_ỹH^{log}_ỹu − (DK_ỹ[u])^T∇F_□(ỹ))^⊥ — bare charges of
relative size O(η) and O(‖∇F_□(ỹ)‖) (on the core ∇F_□(ỹ) is the frame form of G(U); in the φ-transition region it is O(η)), routed
by CCP (c)/(ND). So H^{log}_ỹu_□ = f̂_□ + O(η + N(G))‖u_□‖. On supp ψ_□ ⊂ □^{(R)} ⊂ {φ = 1} the local and global Hessians agree
(finite range), and DG(U) = M^{−1}J^{−T}(H^{log}_y − Q_y[G(U)])J^{−1}M in frame □ (chart change of a Hessian off the critical set;
Q_y linear in G). Hence DG(U)M^{−1}Jψ_□u_□ = M^{−1}J^{−T}[ψ_□f̂_□ + [H^{log}, ψ_□]u_□ + O(η + N(G))‖u_□‖], and M^{−1}J^{−T}ψ_□f̂_□ =
f_□ (ψ_□ = 1 on supp f_□). Summing over □ (≤ 5^d nonzero ψ_□ at any point): DG(U)𝒫_Uf = f + [Σ commutators: ≤ 5^dC_c/R·‖u‖] +
[O(η + N(G))‖u‖]. Apply P_cc^U (it fixes f; it costs C_loc-type routing on the error terms, all of which are bare charges or
commutator sources with the CCL_U structure). The bound on E_U follows; the Neumann series gives R_U. At a critical Z, D_Z(DG(Z)w) =
−(DΞ_Z[w])^TG(Z) = 0, so DG(Z)R_Zf ∈ cc_Z and P_cc^U acts as 1 on it. ∎
**Corollary GP-R2 ((R2) / BFT-5 clause (b) off 𝒞_glob, frame-local σ-form) — PROVEN as an implication of the same inputs.** At every
critical Z ∈ 𝔇_k(R, η_GP): for every S ∈ cc_Z, **w := R_ZS solves H_Zw = S with ‖w‖_𝔇 ≤ βN_𝔇(S)**, uniformly in k, T; in
particular Ran H_Z ⊇ cc_Z, hence Ran H_Z = cc_Z and (H_Z symmetric) **Ker H_Z = Ran Ξ_Z ((N1-nd) at Z)** — because Ker H_Z =
Ann(Ran H_Z) = Ann(cc_Z) = Ran Ξ_Z (finite dimension; cc_Z = Ann(Ran Ξ_Z) on the pinned space). The orbit norm of the solution set is
≤ ‖w‖_𝔇; comparison with BGT55's covariant 𝔐^∇_Z needs Lemma NE.
*Remark (what replaced (LOC-GA)).* BGT55 §7.2 asked for a local **alignment** transfer glued with decay. Here no alignment is used
anywhere: the local inverses are the **slice** inverses 𝒦_□^{−1} of the K^{(σ)} linearisation at the frame coordinates (full-norm
Neumann series, Lemma L1), the cut pieces are made cc_U exactly by covariant routing (LOC-cc_U), and the frames enter only as
isometries. The walk is a one-step parametrix with a Neumann series in E_U (O(1/R + η)), so no decay (m > 0) is needed for
existence or for the m = 0 bound; weighted versions would follow from the weighted local estimates (COFM55 / GV-E_m) — not done.

## §6. T4 — assembly: BFT-0/1/2 on 𝔅^ℂ_k(ε, r_ℂ) (outside 𝒞_glob) as an implication

### 6.1 Theorem OFF (statement)
Fix d = 4, N ≥ 2, odd L ≥ 3, κ_±, 0 < α < θ ≤ σ ≤ 1, Γ = Γ_E (Γ^{(T)} on small local tori is not needed: 𝕋_□ has side ≥ 5).
There are R, ε_*, C_0, r_u depending only on these and on the constants of the inputs in §6.7 — **not on k or T** — such that for every
k ≥ 1, every coarse torus T ≥ T_* := 4R + 6 and every V ∈ 𝔅^ℂ_k(ε, r_ℂ) with ε ≤ ε_*:
- **(BFT-0)** 𝔉_k(·; V) has a critical point **Z(V) ∈ 𝔇_k(R, C_0ε)** (frames whose level-k root values are AX data frames); it is
  **unique modulo composite gauges trivial at level k among critical points in 𝔇_k(R, r_u)**;
- **(BFT-1)** for every j < k: own plaquette logs of Z_j ≤ L^{−2(k−j)}(2C_0ε + 9C_0²ε²), own soft fluctuations ≤ L^{−(2+σ)(k−1−j)}C_0ε +
  C_ρL^{−3(k−j)}C_0²ε² (gauge invariant; Hölder form within level-k blocks);
- **(BFT-2)** Z(V) (as the limit of the holomorphic iteration of §6.4, in fixed real frames) and 𝔉_k(Z(V); V) are holomorphic in z on
  |z|_∞ < r_ℂε, with BFT-1 there;
- **(BFT-5 (b), m = 0)** Corollary GP-R2 at Z(V).
It contains Theorem BFT-E (GV55) on 𝒞*_glob(ε_g) ∩ 𝔅_k(ε) as the one-frame case.

### 6.2 Two lemmas on frames (named inputs; ARGUED-standard)
- **Lemma RG (gauge rigidity).** If U^{ĝ_1} = e^{y_1}, U^{ĝ_2} = e^{y_2} on a connected box with ‖y_i‖_{(σ)} ≤ η, then h := ĝ_1ĝ_2^{−1} =
  c·e^{τ} with c ∈ SU(N) constant and ‖τ‖_♮ ≤ C_RGη. *Mechanism:* h(x)e^{y_2(b)}h(x′)^{−1} = e^{y_1(b)} gives d(h(x)^{−1}h(x′), 1) ≤
  |y_1(b)| + |y_2(b)| (Lemma C1/C3) and log(h(x)^{−1}h(x′)) = y_2(b) − Ad_{h(x)^{−1}}y_1(b) + BCH, whose coarse C^{1,α} norm is that of
  the y's; integrate. (NSL55 Lemma B's algebra is the same computation in the other direction.)
- **Lemma FP (frame patching on a box).** If U has η-small frames on every box of side R_s of a cover of a box Ω of side ≤ mR_s with
  overlaps of side ≥ 1, then U has a single C_FP(m)η-small frame on Ω (C_FP(m)η ≤ η_RG). *Mechanism:* Lemma RG on overlaps; absorb the
  constants c_{ij} along a spanning tree of the (simply connected) box graph; the remaining transitions are e^{τ_{ij}} times products of
  constants around cycles of boxes inside Ω, which are holonomies of contractible loops of length ≤ 4m·R_s, i.e. near 1; interpolate the
  near-identity transitions with a partition of unity in log coordinates; NSL to return to the S_E slice.
Both are the standard local-gauge technology (Uhlenbeck patching; Balaban's transition functions); they are not written out here.

### 6.3 The starting point: the depth induction (Balaban's convention) and Lemma U0
**Lemma U0 (PROOF.md "Lemma U0 (the exact lift)", CONFIRMED in REVIEW_S20)** gives, for level-k data V, the level-(k−1) field
V_0 := U^{(0)}(V) (interior links 1, crossing links V_c) with: M̄_c(V_0) = V_c exactly (ρ = 0); every fine plaquette 1 except block
corners, whose holonomy is V_P — **so V_0 ∈ 𝔅^ℂ_{k−1}(ε, r_ℂ) with the same ε** (complex part on crossing links); covariance under
block-constant extensions of level-k gauges. Induction hypothesis H(k−1): Theorem OFF at depth k − 1 (tori of side TL ≥ T_*).
- *Base k = 1.* U_0 := V_0 (one level). In the block-constant extension of an AX frame, U_0^{ĝ} = U^{(0)}(gV): crossing links ≤ α :=
  3(R′ − 1)ε, interior 0; in depth-1 coarse units sup ≤ Lα, gradient ≤ L²α, Hölder ≤ 2L^{2+α}α, residual r_0 = Q x_0 − B = 0 (each
  S4′ contour crosses one boundary). So U_0 ∈ 𝔇_1(R, C(L)α). G(U_0) = Wilson gradient at the corners only (U0 (iv)), a divergence-form
  source with G^c = O(L²α): N_𝔇(G(U_0)) ≤ C(L)α.
- *Step k ≥ 2.* H(k−1) for V_0 gives Z_{k−1}(V_0) ∈ 𝔇_{k−1}(R, C_0ε). **U_0 := (Z_{k−1}(V_0); V_0)** as a depth-k configuration. Its depth-k
  frames: patch the depth-(k−1) frames (boxes of side R at level k − 1 = R/L at level k) by Lemma FP (m ≈ L + 2); unit conversion
  depth k − 1 → k multiplies the 𝔐^{(σ)} components by at most L^{2+σ}; the level-(k−1) component V_0 is the base-case object. So
  **U_0 ∈ 𝔇_k(R, C_1ε), C_1 := C_FP(L + 2)L^{2+σ}C_0 + C(L)·3(R′ − 1)**. Its gradient: levels < k − 1 vanish (critical at depth k − 1);
  at level k − 1 the new soft term is stationary (ρ_{k−1} = 0, U0 (i)/(iv)), leaving the depth-(k−1) top multiplier, a level-(k−1) plain
  current of own size ≤ κ_+(1 + O(ε))·2C_0ε: **N_𝔇(G(U_0)) ≤ 2L³κ_+(1 + O(ε))C_0ε =: C_GC_0ε**.
**No smoothing of the lift is needed:** one rough level costs only fixed powers of L in depth-k units, and the depth-(k−1) background
supplies the smooth lower levels. This is the soft-scheme form of Balaban's convention (the depth-k background as a perturbation of the
depth-(k−1) one; cf. Goswami 2204.08252 §2-§3 "Lemma 3", method only).

### 6.4 Existence (Newton–Kantorovich with right inverses) — PROVEN as an implication
*Lemma NK (standard; re-derived).* Let G(U) ∈ cc_U for all U, and on 𝒩 := {U : d_𝔇(U, U_0) ≤ r} let R_U satisfy P_cc^UDG(U)R_U = 1,
‖R_U‖ ≤ β; let ‖G(e^{−v}U) − G(U) + DG(U)v‖ ≤ K_2‖v‖² for ‖v‖_𝔇 ≤ r, and N(P_U^TD_U^⊥(DG(U)w)) ≤ K_3N(G(U))‖w‖ ((ND)). Put
v_n := R_{U_n}G(U_n), U_{n+1} := e^{−v_n}U_n. Then N(G(U_{n+1})) ≤ (K_2β² + K_3β)N(G(U_n))², because DG(U)v = G(U) +
P_U^TD_U^⊥(DG(U)v) (from P_cc^UDGR = 1). If h := (K_2β² + K_3β)N(G(U_0)) ≤ ½ and 2βN(G(U_0)) ≤ r, the iterates stay in 𝒩
(Σ‖v_n‖ ≤ βN(G(U_0))Σ_n2^{1−2^n} ≤ 2βN(G(U_0))) and converge to Z with G(Z) = 0, d_𝔇(Z, U_0) ≤ 2βN(G(U_0)). ∎
Apply it with U_0 of §6.3 and Theorem GP's R_U on 𝒩 ⊂ 𝔇_k(R, C_1ε + r) (r := 2βC_GC_0ε): h ≤ (K_2β² + K_3β)C_GC_0ε ≤ ½ and
C_1ε + r ≤ min(η_GP, r_u) for ε ≤ ε_*(C_0, C_1). So **Z(V) exists in 𝔇_k(R, r_u)**.

### 6.5 Proposition AP (a priori estimate: every critical point in the r_u-ball is C_0ε-small) — PROVEN as an implication
Let Z ∈ 𝔇_k(R, r) be critical, r ≤ r_u, with frames in which y_□ ∈ S_E on Ω_□ (NSL in each frame; Opus PROVEN-HERE, **Codex pending**).
In frame □: H(ψ_□y_□) = ψ_□(NB_□ + 𝔑^0(y_□)) + [H, ψ_□]y_□ (finite range; criticality on Ω_□), a **flat-cc** source (D^⊥H = 0) — no
conversion lemma is needed here. Γ(ψ_□y_□) = [Γ, ψ_□]y_□ is supported where ∇ψ_□ ≠ 0; by KFACTOR_OFF55 Lemma OC, 𝓛_Γ^{−1}Γ^Tν = −Ξν.
So on 𝕋_□: ψ_□y_□ = 𝓛_Γ^{−1}P_cc[ψ_□(NB + 𝔑^0(y)) + [H, ψ_□]y] − Ξν, ν := [Γ, ψ_□]y_□, and Ξν = 0 on □^{(R/2 − 2)} (ν vanishes near
there). Hence on that core, with K^{(σ)}'s bounds (BL-4 data map, ROW/CB: ‖𝔑^0(y)‖ ≤ K(r)r with K(r) = O(r)) and (W-comm)^σ, W-mult^σ:
  ‖y_□‖_{(σ),core} ≤ G_♯[C_Ds_R + K(r)r + (C_c/R)r].
The cores of the boxes cover the torus; Lemma FP (bounded m) turns core bounds into Ω-bounds: r′ ≤ C_FP·G_♯[C_Ds_R + K(r)r + (C_c/R)r].
For R ≥ 4C_FPG_♯C_c and r_u with C_FPG_♯K(r_u) ≤ ¼: r′ ≤ C_FPG_♯C_Ds_R + ½r; iterating (same frames), **Z ∈ 𝔇_k(R, C_0ε) with
C_0 := 4C_FPG_♯C_D(3(R′ − 1) + r_ℂ)** — independent of C_1 and of k, T. ∎ This is what prevents the depth induction from accumulating.

### 6.6 Proposition UQ (uniqueness modulo gauge) — PROVEN as an implication
Let Z, Z′ ∈ 𝔇_k(R, r_u) be critical with the same data V. Frames with the same AX root values g_□; NSL puts both in each frame's S_E
slice: y_□, y′_□ (NSL (a): unique small gauge given root values). w_□ := y′_□ − y_□ ∈ S_E on Ω_□ (S_E is linear) and, both being critical,
H^{log}_{y_□}w_□ = O(r_u)·w_□ on Ω_□ (Lipschitz of ∇F). As in §6.5 with source [H, ψ]w + O(r_u)w and gauge part −Ξ[Γ, ψ]w:
‖w‖_core ≤ G_♯(C_c/R + K(r_u))‖w‖_Ω, and with Lemma FP, q := max_□‖w_□‖ ≤ ½q ⇒ **q = 0**: y_□ = y′_□ for every □. So Z′ = Z^{h_□} on Ω_□
with h_□ := ĝ′^{−1}_□ĝ_□, h_□ = 1 at the level-k roots. On overlaps h_□h_{□′}^{−1} stabilises Z; a gauge that fixes a configuration and is
1 at one site of a connected region is 1 there (parallel transport determines it), so the h_□ agree and glue to one composite gauge h,
trivial at level k, with Z′ = Z^h. ∎ (Lemma C3's O(1) constants never enter: both frames share the root values.)

### 6.7 Every input of Theorem OFF, with its status
| # | Input | Where | Status |
|---|---|---|---|
| 1 | Lemma AX at level k (data frames) | PROOF.md "Lemma AX"; §1.3 | **CONFIRMED** (REVIEW_S18_S19); re-derived here |
| 2 | Lemma U0 (exact one-level lift) | PROOF.md "Lemma U0 (the exact lift)" | **CONFIRMED** (REVIEW_S20 "Lemma U0 … CONFIRMED") |
| 3 | Theorem K^{(σ)} chain (ROW^{(σ)}, CB, CCP, HR, LIN^{(σ)}) + GV-E, on local tori | KFACTOR_OFF55 §2-§4; GV55 | **Codex CONFIRMED, conditional** on the lane-A linear package (CODEX_REVIEW_KOFF items 1-5, CODEX_REVIEW_GV items 2, 4) |
| 4 | Lemma L1 (full-ball linearisation) | §4.1 | **PROVEN as an implication of 3** (scope note for Codex: full ball vs slice ball) |
| 5 | Lemma HR_U, CCL_U, Proposition LOC-cc_U | §3.2-§3.4 | **PROVEN-HERE**; identities checked exactly (og55_1 PASS) |
| 6 | Theorem NSL in frames | NSL55 §2-§3 | Opus PROVEN-HERE; **Codex review running — NOT banked** |
| 7 | Lemma CONV (G-, s-slots), (ND) | §4.3, §5.2 | **ARGUED** (plain-current slot PROVEN, Prop. L2 (c)) |
| 8 | Lemma NE (frame vs covariant norms) | §4.3 | **ARGUED** (only for comparison with BGT55's covariant norms; §5-§6 are written in frame-local flat norms) |
| 9 | (W-comm)^σ at small frame backgrounds | BFT34_55 §2.5 + R6 correction | **ARGUED** |
| 10 | W-mult^σ | BFT34_55 §2.5 | **ARGUED** |
| 11 | Lemma RG, Lemma FP (frame rigidity and patching) | §6.2 | **ARGUED-standard** |
| 12 | Lemma NK | §6.4 | **PROVEN-HERE** (standard) |
| 13 | BA-3 (BFT-1 from the 𝔐-ball) | BFT_A §3.3 | **CONFIRMED** (REVIEW_BFT_A_S1) |
**Status of Theorem OFF: PROVEN as an implication of 1-13; its open content is items 6 (Codex pending), 7-11 (ARGUED, all local,
all of fixed finite range, none global).** Items 8 and the covariant reading of Corollary GP-R2 are needed only to translate into
BGT55's covariant norms. **Not needed on this route: (UHL-fine), (SL-cov), (FLAT-REF), (EP-rec)_Z = lane B's (N1), any alignment
(ALIGN-ℓ) / (LOC-GA), the smooth lift Z^sm as a separate construction (the depth-(k−1) background replaces it), and BFT on boxes with
boundary conditions.**
**Not delivered:** BFT-0's identification clause off 𝒞_glob (Theorem ID frame-locally — ARGUED to go through with NSL in frames, not
written); BFT-3/4 off 𝒞_glob; non-wrapping boxes with N5-sf0's boundary convention; T < T_* = 4R + 6.

**Erratum E4 (to §4.1 and §6, constants and conventions; found on re-reading against CODEX_REVIEW_KOFF §5.3).** (i) Codex's corrected
Theorem K (CODEX_REVIEW_KOFF "5.3 What the contraction statement actually earns") states the source bounds as N^{(σ)}(source) ≤ K(η + s)²,
N^{(σ)}(difference) ≤ K(η + η′ + s)‖x − x′‖_{(σ)} — for x, x′ in the ball, **with no slice condition**, which is what Lemma L1 needs; with
those constants read **r_lin := (4GK)^{−1} − s/2** (G = G_♯) in place of the printed K_rows/K_C form. (ii) Tangent vectors (differences) are
measured in the **homogeneous-data** norm (top residual Qu_{k−1}, data fixed), as Codex §5.3 prescribes. (iii) §6.5: Ξν vanishes on
□^{(R/2 − 3)} (not R/2 − 2), the extra unit being Λ_E's range. (iv) Ω_□ := □^{(R+3)} has side < 4R + 6, i.e. ≤ R′ = 4R + 5 in
blocks, matching N5-sf0's Ω^+_□ and T_0 = 4R_* + 6. (v) In Proposition AP and UQ, NSL is applied on 𝕋_□ to the cut-off ỹ_□ and the
resulting gauge is restricted to the region where φ_□ = 1 (minus Λ_E's range); radii shrink by a fixed number of coarse units. None of
these changes a conclusion.

## §7. Findings on prior claims (one per claim: verdict, file + locating string, reason)

- **P1. BFT_A §3.10, "*BA-11 (PAR): PROVEN-HERE.*"** — **CONFIRMED** (re-derived: 𝓛Par = 1 + E, ‖E‖ ≤ N_ov(C_c/ℓ)GC_ψ ≤ ½,
  Neumann; REVIEW_BFT_A_S1 agrees).
- **P2. BFT_A §3.10 / §2, "Outside 𝒞_glob: additionally (G♯-patch), reduced by BA-11/BA-12 to (COMM), (UHL) and (SL-cov)"** —
  **NOT-VERIFIED as a reduction** (and superseded): BA-11 needs local inverses 𝓖_□ bounded on the cut-off sources ψ_□f, which are not
  composite-co-closed, while every banked linear estimate is cc-only (BFT34_55 F4; CODEX_REVIEW_BFT34 R5: "cc-only linear estimates
  cannot simply be used on all raw cutoffs"); the reduction omits that requirement. Theorem GP (§5) replaces it, with the cut pieces
  made cc_U exactly (LOC-cc_U) and the local inverses the K^{(σ)} slice inverses; neither (UHL) nor (SL-cov) is an input.
- **P3. BFT_A §3.10, "Lemma AX's complete axial gauge does **not** give this … loss L^{k(1-α)} (it is fine only for C¹ curvature)"** —
  **CONFIRMED** with an exact witness (Proposition U2: axial coarse gradient 2ℓK·L^{k(1−α)}, Coulomb gauge for the same field ≤ 3K). Also
  sharpened: the axial gauge **does** give the C^α half uniformly in k (Lemma U1 (b)).
- **P4. BFT_A §3.10, "The smooth lift Z^sm … is the same construction ((UHL) on overlapping patches, glued by BA-11's partition): ARGUED"** —
  **NOT-VERIFIED** (no construction is given) and **not needed**: the depth-(k−1) background over Lemma U0's exact lift is a global,
  frame-locally small starting point (§6.3).
- **P5. HESSREL §H6.2 item 1, "(FLAT-REF) is (UHL)-strength, and it is the wall"** (with §H6.1's statement: Z(V) = g·(Z^♭e^a),
  Z^♭ flat, |a_j(b)|_own ≤ Cρ_jf_k) — **REFUTED as stated, for every C at small ε** (conditional only on Z(V) reproducing the data
  holonomy of a large square up to o(1), which BFT-1's soft-fluctuation bound gives): on Proposition C4's witness the level-(k−1) loop
  over ∂Q_+ (4R_εL links) has holonomy within C′R_εε of the data holonomy −1, while (FLAT-REF) forces it within 4R_εL·CL^{−1}ε = 4CR_εε of
  1; since d(−1, 1) = √2π and R_εε ≍ √ε → 0, contradiction for small ε. **(FLAT-REF) is a false global statement, not a wall of
  (UHL)-strength; (UHL) is local, and on boxes of bounded size it is plausible (Theorem U3).** The direction "HESSREL's route needs a
  global gauge statement" (BGT55 P11) stands.
- **P6. BGT55 §2.5, "the holonomy of a loop of coarse size R is O(εR²) and is unconstrained once εR² ≳ 1; for flat V it is arbitrary
  … So no gauge makes log Z small on all of 𝒦(ε)"** — **CONFIRMED**, quantitatively: Proposition C4 (every gauge has a link with
  d ≥ 0.44√ε on its witness), Proposition C6 (flat data).
- **P7. BGT55 §2.5, "A flat V with holonomy θ around a cycle of coarse length T lies in 𝒞_glob(ε) iff (roughly) θ/T ≲ ε"** —
  **CONFIRMED** (Proposition C6: exact, min s = max_μ d(h_μ, 1)/T when the holonomies are in the principal-log regime; ≤ 3π√N/T always).
- **P8. BGT55 §7.1, "A global Υ assembled from box frames … the transition function g_□^{-1}Zg_{□′} − 1, which is O(1) somewhere
  whenever the total flux is large … E_Υ = O(1) on the seams and the Neumann series of Theorem GA does not close"** — **CONFIRMED**, with
  the precise structure: transitions are near-**constant** (variation ≤ 2α per link, Lemma C3 (a)) with O(1) constant parts that cannot
  all be removed (Lemma C3 (c), Proposition C4). "Whether some other uniformly bounded global aligned congruence exists outside 𝒞_glob
  is OPEN" — status unchanged; **not needed** on the frame route (Theorem GP uses no alignment).
- **P9. BGT55 §7.1, "for T ≥ T_b … connection ≤ 2π/T_b in a constant gauge, so GA applies with η ≲ 2π/T_b"** — first clause
  **CONFIRMED** up to the constant (3π√N/T in general); "so GA applies" **NOT-VERIFIED** (GA's (A1)-(A2) at such backgrounds are R2-glob,
  NOT-VERIFIED per CODEX_REVIEW_BGT §6.4).
- **P10. BGT55 §7.2, "(LOC-cc_Z): S = Σ_□S_□ with S_□ ∈ cc_Z localised near □ and Σ_□e^{−m·dist}N_Z(S_□) ≤ C·N_{Z,m}(S)" and its
  slot-wise ingredients** — **PROVEN-HERE** (Proposition LOC-cc_U, at every configuration, constant C_loc ≈ 221 at d = 4, L = 3, plus the
  weighted sum (e)). Ingredients: "G-slots localise up to item 13's curvature-sized bulk divergence, repaired by routing to the level-k
  roots" — **CONFIRMED** (CCL_U (G): the cut charge is the exact bracket [log U_P, G_0(P)] times the cutoff difference, n^{−1}-small after
  routing); "residual slots up to the exact commutator [λ, ρ(z)]" — **CONFIRMED** (CCL_U (s)); "plain currents … with the axial-strip
  defect O(f)π_l per block" — **NOT NEEDED**: routing **bare** charges covariantly has no defect (HR_U (v) is exactly Ad-isometric);
  a defect appears only when routing a divergence (HR (iii)-(iv) at U), which LOC-cc_U never does.
- **P11. BGT55 §7.2, "Status of (R2) outside 𝒞_glob: OPEN, with (LOC-GA) [⊃ (LOC-cc_Z)], (R3), BFT-0 outside 𝒞_glob, and the 𝒞_glob inputs
  of §6.5 applied box by box"** — **superseded as a list of necessary inputs**: Corollary GP-R2 gives (R2) at m = 0 off 𝒞_glob in
  frame-local σ-form from Theorem GP's inputs; (R3) is needed only for m > 0; the §6.5 inputs (ALIGN-ℓ etc.) are not used.
- **P12. BGT55 §8 (An-3), "Restricted to cc_Z sources, the IFT identification is Proposition GA-slice's Υ_W, and it inherits §6.4's
  completion problem. **No new mechanism.**"** — **REFUTED** (the conclusion): the argument is right for Theorem BA's Feynman map, but
  KFACTOR_OFF55's cc-projected map Φ̃_Γ (CODEX_REVIEW_KOFF items 2, 5) linearises to 𝒦_x = P_ccH^{log}_x + Γ^TΓ (Lemma L1), whose
  completion is the hierarchical routing P^T, bounded by CCP (c) — not GA-slice's Λ_E^T; Proposition L2 gives (N1-nd) and the slice
  response at the critical point with no alignment and no S_E completion.
- **P13. NSL55 §10.2 item 3, "a background version needs the background-covariant slice estimate (lane B's (N1)), OPEN"** —
  **REFUTED as a necessity**: in a frame the background is a small field relative to the frame's trivial chain, and NSL applies verbatim to
  frame coordinates (flat S_E of the frame); only frames (Lemma C2, RG, FP) are needed. **CONFIRMED** that NSL as written is a trivial-chain
  statement.
- **P14. GV55 §3.3 item 2, "Off 𝒞_glob … (G♯-patch), (UHL), (SL-cov), the smooth lift Z^sm, and … (EP-rec)_Z = lane B's (N1) — OPEN"** —
  **CONFIRMED as a status list for the BA-11 route; REFUTED as a list of necessary inputs** (Theorem OFF needs only (G♯-patch) in the form of
  Theorem GP; (UHL), (SL-cov), Z^sm, (N1) are not inputs).
- **P15. GSHARP55 §5.4, "(EP-rec)_Z … Status: ARGUED — an outline only"** — **NOT-VERIFIED** (not attempted here; not needed on this route).
- **P16. REVIEW55_BFTB Finding 9, "(G♯-patch^Ω) narrowing: NOT-VERIFIED … the slice change is unnamed"** — **agree**: the slice changes from
  frame to frame; Theorem GP never forms a global slice (frame-local slices, responses patched by ψ_□, frames as isometries).
- **P17. BFT34_55 §2.7 E2 / CODEX_REVIEW_BFT34 R5, "each c_□ is cc"** — **CONFIRMED at Z = 1, and at any critical Z for exact local
  responses** (Proposition RW-cc_Z (d), by KER_Z); existence of exact local responses at a transplanted background is not available
  (Erratum E3), which is why §5 uses 𝒦_y.
- **P18. BFT34_55 §1.3 "Scope", "off 𝒞_glob, BFT-0 itself is OPEN ((G♯-patch), (UHL), (SL-cov), the smooth lift)"** — status, **superseded**
  by Theorem OFF (PROVEN as an implication; open content = NSL's Codex check + five local ARGUED lemmas).
- **P19. HANDOFF.md row "BFT off 𝒞_glob (large fields) | OPEN: (G♯-patch), (UHL), (SL-cov), (LOC-GA)"** — **REFUTED (label)**: the
  off-𝒞_glob problem is a **small-field** problem (curvature ≤ ε, holonomy and frames arbitrary); "large fields" is RLARGE's large-curvature
  regime. The input list is superseded as in P14.
- **P20. KFACTOR_OFF55 §1.4 (1c), "Outside 𝒞_glob the centre must carry the holonomy (Z^lift itself is excluded as a centre in every
  decaying norm by BA-2; the smooth lift Z^sm … is ARGUED) — unchanged and OPEN there"** — **CONFIRMED that no single global centre is
  available in the frame-free norms; superseded** by frame-local centres (the trivial chains of the frames) plus a global starting point
  from the depth induction. Consistent with BA-2: the k-fold lift is excluded, but **one** rough level (Lemma U0) costs only L^{2+σ} (§6.3).
- **P21. REVIEW_S22 Part 5 BFT data class ("max_P|log V^r_{k,P}| ≤ ε … |z|_∞ ≤ r_ℂε") read as "the RG's background class"** —
  **CONFIRMED** as the class the RG must handle on tori (§1.5 (iv)); it is the frame class 𝔑_k(R, ·) up to the factor 12(R′ − 1)
  (Lemma C2), and 𝒞*_glob is a strict subclass with a √ε gap (Proposition C4).

## §8. Codex verdicts used — agree or disagree, explicitly (files as on disk 03:22-04:20Z; each ends with "Exactly what may be banked")
- **CODEX_REVIEW_BGT** (396 lines, complete). Items 1-5 (GA, GA-slice, GA-PG, KER_Z/SF_Z with the corrected sign, OC, RW♯): **agree**; I
  re-derived OC and KER_Z where used (§3.5, §4.2) and use the actual-generator covariance only through sizes. §6.4 (R2-glob NOT-VERIFIED):
  **agree as a verdict on BGT55's route**; Proposition L2 is a different route (no alignment), which Codex's text does not exclude ("This
  review establishes neither impossibility nor target-equivalence"). §8's twisted-divergence counterexample to the ordinary cut condition:
  **agree**, and consistent with LOC-cc_U (covariant bare-charge routing needs no cut condition).
- **CODEX_REVIEW_BFT34** R5 (corrected RW-cc, every c_□ cc, CCL's 216/217): **agree** — CCL_U reproduces 216 for the plain-current slot.
  R6 (exponent L^{3+σ} → L^{4+σ}): **agree**; carried into (W-comm)^σ's status. R7 (RW-cc-walk's weight radius refuted): **agree**; not used
  (no weighted walk here).
- **CODEX_REVIEW_KOFF** items 1-5 and §5.3 (corrected Theorem K): **agree**; used for Lemma L1 through its source bounds on the full ball
  (Erratum E4 (i)). Item 5's "nonlinear gauge-orbit coverage NOT-VERIFIED" is exactly NSL's status here (input 6).
- **CODEX_REVIEW_GV** items 2 (GV-E) and 4 (K + GV-E contraction): **agree**, used as conditional inputs.
- No Codex review of NSL55 was on disk when I read (CODEX_REVIEW_NSL not found at 04:20Z); NSL enters as Opus-only.

**Erratum E5 (to §8's last bullet and to input 6 of §6.7 — a false statement of mine, corrected).** "No Codex review of NSL55 was on
disk when I read (CODEX_REVIEW_NSL not found at 04:20Z)" is **wrong**: I had not looked. `CODEX_REVIEW_NSL.md` exists (218 lines, file
time 23:57 local = 03:57Z, complete — it ends with "Exactly what may be banked" items 1-4 and its "single most dangerous" sentence). I
read it at 04:24Z. Its verdicts, and my agreement:
- **Item 2: NSL's real existence, small-gauge uniqueness, C_N = 4 + 3C_Λ and the Faddeev-Popov inverse, uniformly in k, T, j, σ —
  CONDITIONAL** on the uniform elliptic input (Lemma A (c): ‖Λ v‖_♮ ≤ C_Λ n_0(v), i.e. EP-bd's C^{1,α} → C^{2,α} bound, which Codex lists as
  "NOT-VERIFIED independently here" but which CODEX_REVIEW_GSHARP item 1 banked); holomorphy only in the complexified scaled norm.
  **Agree**; my uses of NSL (frame-local slice attainment in §6.5-§6.6, Lemma FP's last step, Theorem U3 item 4) are real-gauge,
  scaled-norm uses on frame coordinates, i.e. inside the banked scope. **Input 6 of §6.7 should read: "NSL — Codex CONFIRMED
  CONDITIONAL (CODEX_REVIEW_NSL item 2), on EP-bd (CODEX_REVIEW_GSHARP item 1)".**
- **F5: the fixed-datum symmetry group is larger than the root-trivial gauges** (constant conjugations stabilising V). **Agree.** It does
  not affect Proposition UQ, which asserts uniqueness modulo the root-trivial subgroup and uses only that a gauge stabilising a configuration
  and equal to 1 at a root is 1 on the connected region (the extra symmetries map the solution set to itself and are not quotiented).
- **F6's analyticity qualification** (no unweighted fine-link polydisc): **agree**; Theorem OFF's BFT-2 is stated for complex **data** z,
  through the holomorphic NK iteration, not through an NSL polydisc in fine links.
- Items 3-4 (K-U, ID at the trivial background on 𝒞_glob; Balaban's convention): agree; consistent with §6.7's "not delivered:
  identification clause off 𝒞_glob".
So the open content of Theorem OFF is items 7-11 of §6.7 (all ARGUED, all local) plus the conditional inputs 3 and 6.

## §9. Summary tables

### 9.1 Results of this file (status words; none has had a Codex check)
| Result | Where | Status |
|---|---|---|
| Lemma C1 (metric facts) | §1.2 | PROVEN-HERE |
| Lemma C2 (data frames = AX at level k) | §1.3 | CONFIRMED (re-derived; REVIEW_S18_S19) |
| Lemma C3 (transitions near-constant, constants O(1)) | §1.4 | PROVEN-HERE |
| Proposition C4 (𝒞*_glob strict; √ε gap) | §1.5 | PROVEN-HERE (constants per E1/E2) |
| Corollary C5 (what 𝒞_glob covers) | §1.5 | PROVEN-HERE (iii)'s topology remark ARGUED (imports Lüscher) |
| Proposition C6 (flat data on tori) | §1.6 | PROVEN-HERE |
| (FLAT-REF) at size O(ε) is false | §2.2, P5 | PROVEN-HERE (data level unconditional; composite level conditional on BFT-1 for Z(V)) |
| Lemma U1 (axial: sup + C^α, uniform in k) | §2.3 | PROVEN-HERE (E2) |
| Proposition U2 (axial C^{1,α} loss attained; Coulomb bounded) | §2.4 | PROVEN-HERE (exact witness) |
| Theorem U3 ((UHL-fine) reduced) | §2.5 | ARGUED (missing: nonlinear C^α bootstrap) |
| Theorem U4 ((UHL-fine), (SL-cov) not inputs of Theorem OFF) | §2.6 | PROVEN (as a statement about §6) |
| Lemma HR_U, Lemma CCL_U, Proposition LOC-cc_U | §3.2-§3.4 | PROVEN-HERE; identities exact-checked (og55_1 OVERALL PASS) |
| Proposition RW-cc_Z | §3.5 | identities PROVEN-HERE; existence of exact local responses not available (E3) |
| Lemma L1 (𝒦_y invertible on the full ball) | §4.1 | PROVEN as an implication of K^{(σ)} (Codex scope note; E4 (i)) |
| Proposition L2 ((N1-nd) + slice response at a 𝒞_glob critical point, no alignment) | §4.2 | PROVEN as an implication |
| Lemma NE, Lemma CONV, (ND) | §4.3, §5.2 | ARGUED (CONV plain-current slot PROVEN) |
| Theorem GP ((G♯-patch) as a right inverse), Corollary GP-R2 ((R2) off 𝒞_glob, m = 0, frame-local σ-form) | §5.2 | PROVEN as an implication (inputs incl. ARGUED (W-comm)^σ, W-mult^σ, CONV, ND) |
| Lemma RG, Lemma FP (frame rigidity / patching) | §6.2 | ARGUED-standard |
| Lemma NK (Newton–Kantorovich with right inverses) | §6.4 | PROVEN-HERE (standard) |
| Proposition AP (a priori), Proposition UQ (uniqueness mod gauge) | §6.5-§6.6 | PROVEN as implications |
| **Theorem OFF (BFT-0/1/2 + BFT-5 (b) at m = 0 on 𝔅^ℂ_k(ε, r_ℂ), tori T ≥ 4R + 6)** | §6.1-§6.7 | **PROVEN as an implication of §6.7's 13 inputs; open content: 7-11 ARGUED (local), 3 and 6 Codex-conditional** |

### 9.2 Verdicts on prior claims (§7)
| # | Claim (file, locating string) | Verdict |
|---|---|---|
| P1 | BFT_A §3.10 "BA-11 (PAR): PROVEN-HERE" | CONFIRMED |
| P2 | BFT_A "(G♯-patch), reduced by BA-11/BA-12 to (COMM), (UHL) and (SL-cov)" | NOT-VERIFIED (omits the cc requirement; superseded by Theorem GP) |
| P3 | BFT_A §3.10 "loss L^{k(1-α)}" of the axial gauge | CONFIRMED (exact witness) |
| P4 | BFT_A §3.10 "The smooth lift Z^sm … is the same construction" | NOT-VERIFIED (no construction; not needed) |
| P5 | HESSREL §H6.2 "(FLAT-REF) is (UHL)-strength, and it is the wall" | REFUTED ((FLAT-REF) is false at O(ε)) |
| P6 | BGT55 §2.5 "no gauge makes log Z small on all of 𝒦(ε)" | CONFIRMED (quantified: √ε gap) |
| P7 | BGT55 §2.5 flat "iff (roughly) θ/T ≲ ε" | CONFIRMED (exact in the principal-log regime) |
| P8 | BGT55 §7.1 frame-assembled Υ: "E_Υ = O(1) on the seams" | CONFIRMED (transitions near-constant, O(1) constants) |
| P9 | BGT55 §7.1 "connection ≤ 2π/T_b … so GA applies" | NOT-VERIFIED (clause 1 CONFIRMED up to constant; "GA applies" is R2-glob) |
| P10 | BGT55 §7.2 (LOC-cc_Z) and its slot ingredients | CONFIRMED — now PROVEN-HERE (LOC-cc_U); the plain-current "axial-strip defect" does not arise |
| P11 | BGT55 §7.2 "Status of (R2) outside 𝒞_glob: OPEN, with (LOC-GA) …" | CONFIRMED as status; input list superseded (Corollary GP-R2) |
| P12 | BGT55 §8 (An-3) "No new mechanism" | REFUTED (the cc-projected linearisation, Lemma L1/Prop L2) |
| P13 | NSL55 §10.2 item 3 "a background version needs … (N1)" | REFUTED as a necessity (frames suffice) |
| P14 | GV55 §3.3 item 2 off-𝒞_glob list "(G♯-patch), (UHL), (SL-cov), Z^sm, (EP-rec)_Z = (N1) — OPEN" | REFUTED as a list of necessary inputs (status list for the BA-11 route CONFIRMED) |
| P15 | GSHARP55 §5.4 "(EP-rec)_Z … ARGUED — an outline only" | NOT-VERIFIED (not needed here) |
| P16 | REVIEW55_BFTB Finding 9 "(G♯-patch^Ω) … NOT-VERIFIED … the slice change is unnamed" | CONFIRMED (agree) |
| P17 | BFT34_55 E2 / CODEX_REVIEW_BFT34 R5 "each c_□ is cc" | CONFIRMED (at Z = 1; at critical Z for exact local responses) |
| P18 | BFT34_55 §1.3 "off 𝒞_glob, BFT-0 itself is OPEN ((G♯-patch), (UHL), (SL-cov), the smooth lift)" | CONFIRMED as status; list superseded |
| P19 | HANDOFF row "BFT off 𝒞_glob (large fields)" | REFUTED (label: it is a small-field problem) |
| P20 | KFACTOR_OFF55 §1.4 (1c) "the centre must carry the holonomy … OPEN there" | CONFIRMED (no single global centre); superseded by frame-local centres |
| P21 | REVIEW_S22 BFT data class as the RG's class | CONFIRMED |
**Counts (prior claims P1-P21): CONFIRMED 12, NOT-VERIFIED 4, REFUTED 5.** New results (9.1) are not counted.

### 9.3 Outcome against the PRE-STATED targets and refutation tests
- **T1: met.** Class 𝔅^ℂ_k(ε, r_ℂ) (= the frame class up to 12(R′ − 1)); norm d(·, 1) for data, frame-local 𝔐^{(σ)} for backgrounds; the
  𝒞_glob part is 𝔅 ∩ 𝒞*_glob(ε_g), a strict subclass with a √ε size gap (Proposition C4). Refutation test (a background the RG produces
  outside 𝔅, or a mis-identification of 𝒞_glob): none found; the pre-stated possible failure "trivial holonomy on the torus ⇒ globally
  small" is moot — on boxes (no holonomy at all) the gap already appears.
- **T2: partly met.** (UHL-data) proved; the C^α half of (UHL-fine) proved uniformly in k; the C^{1,α} half reduced (ARGUED) with the
  obstruction located (a nonlinear C^α bootstrap of the slice gauge); the axial loss attained by an exact witness. The pre-stated
  expectation "uniform only for boxes of bounded diameter" is confirmed by Proposition C4. And (UHL-fine) is not an input of Theorem OFF.
- **T3: met for (LOC-cc_Z)** (PROVEN-HERE at every configuration, exact identities checked); **(G♯-patch) proved as an implication**
  (Theorem GP) with local ARGUED inputs. RW-cc routing survives transition functions (covariant routing needs none; flat routing costs
  O(η)). No pre-stated T3 refutation occurred (pieces cc exactly; constant C_loc independent of volume).
- **T4: met as an implication** (Theorem OFF, §6.7's table). Pre-stated T4 test: no input labelled PROVEN here is NOT-VERIFIED or REFUTED
  in an on-disk Codex review (checked against CODEX_REVIEW_BGT, _BFT34, _KOFF, _GV, _NSL); none of BGT55's REFUTED §6 statements is used.
- **First-class negative results:** (FLAT-REF) at O(ε) is false (P5); 𝒞*_glob(Cε) ⊊ 𝔅(ε) with the √ε gap (Proposition C4); BGT55 (An-3)'s
  "no new mechanism" is false (P12).

## §10. For the lead (nothing here is banked; Codex first)
1. **HANDOFF row "BFT off 𝒞_glob (large fields)"** → relabel "BFT off 𝒞_glob (small curvature, arbitrary holonomy/frames)"; status →
   "reduced (OFFGLOB55 Theorem OFF, PROVEN as an implication, unreviewed): BFT-0/1/2 and BFT-5 (b) at m = 0 on the full data class, tori
   T ≥ 4R + 6, uniformly in k, T, from the K^{(σ)}/GV-E chain on local tori and NSL (both Codex-conditional), LOC-cc_U (proved), and five
   local ARGUED lemmas — (W-comm)^σ, W-mult^σ, CONV (G-/s-slots) + (ND), frame rigidity/patching (RG, FP). (UHL), (SL-cov), (LOC-GA)'s
   alignment, a separate smooth lift Z^sm and lane B's (N1) are not needed on this route. Not delivered: identification clause off 𝒞_glob,
   BFT-3/4 off 𝒞_glob, boxes." Suggested owner: one worker for (W-comm)^σ + W-mult^σ (they also serve BFT-4's walk family, BFT34_55 §2.6),
   one for CONV + (ND) + Lemma FP; then Codex on Theorem GP/OFF.
2. **HANDOFF row "BFT-5 (b) background transfer"**: add "alignment-free slice-form route on 𝒞_glob: OFFGLOB55 Proposition L2 ((N1-nd) and the
   slice response at the K^{(σ)} critical point, σ-pair, from K^{(σ)}'s banked inputs + CCP (c)); ALIGN55's GA route is in the (♯, N) pair
   and is not superseded — the two pairs differ (N vs N^{(σ)}; CODEX_REVIEW_GV item 1's witness shows the gap). Codex should check L1/L2."
3. **HESSREL's (FLAT-REF)**: wherever PROOF/SESSION text calls it "the wall" or "(UHL)-strength", record that it is **false at size O(ε)**
   (OFFGLOB55 §2.2, P5); BGT55 P11's "CONFIRMED in direction" stays true only as "HESSREL's route needs a global statement".
4. **BGT55 §8 (An-3)**: "No new mechanism" → false (P12).
5. **NSL55 §10.2 item 3** and **GV55 §3.3 item 2**: replace "needs (N1)" / the off-𝒞_glob list by "needs frames (Lemma C2/RG/FP); see
   OFFGLOB55 §6.7".
6. **PROOF tally**: no change (lane-level). **Critical path**: the off-𝒞_glob BFT is no longer a paper-scale global wall; what remains is
   local, finite-range bookkeeping of the same kind as KFACTOR_OFF55's ROW/CB and BFT34_55's (W-comm)^σ — plus the Codex checks.
7. **Symbols**: 𝔑_k, 𝔇_k, 𝒦_y, P_U, C_loc, r_lin, β, C_FP, s_R are local to this file (not lane vocabulary); quote with §0's pins.
*Check record:* og55_1 only (criteria before script; one run; OVERALL PASS; §4.4). Files written: `OFFGLOB55.md`,
`checks/og55_1_criteria.md`, `checks/og55_1_route.py`, `checks/og55_1_out.txt`, `checks/og55_1_err.txt`. No git.

**Erratum E6 (to §6.5-§6.6, two steps stated too quickly; conclusions unchanged).** (i) Proposition AP: "iterating (same frames)" —
Lemma FP returns *new* (patched) frames, so read the argument as a single inequality for r_* := the infimum over admissible frame systems
of the frame-local size: r_* ≤ C_FPG_♯C_Ds_R + ½r_* whenever r_* ≤ r_u, hence r_* ≤ 2C_FPG_♯C_Ds_R = C_0ε. (ii) Proposition UQ:
"frames with the same AX root values" for Z and Z′ needs one more step: two data frames of the same V on a box differ at the roots by
t = c·e^{τ} with |∇τ| = O(α) (Lemma C3); compose Z′'s frame with c (an isometry) and with an S_E-extension of e^{τ} (Lemma RG / NSL), at
cost O(η) in the frame-local size. This is inside Lemma RG/FP's ARGUED scope (§6.7 item 11).

**Final status line (04:26Z).** Theorem OFF: PROVEN as an implication; open content = §6.7 items 7-11 (ARGUED, local) and the
Codex-conditional inputs 3 (K^{(σ)}/GV-E) and 6 (NSL, CODEX_REVIEW_NSL item 2). Counts on prior claims: CONFIRMED 12, NOT-VERIFIED 4,
REFUTED 5. Check og55_1: OVERALL PASS.
