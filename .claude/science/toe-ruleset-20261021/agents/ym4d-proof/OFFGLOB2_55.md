Reviewer model: claude-opus-5-5

# OFFGLOB2_55 — finishing the background-field theorem outside 𝒞_glob: the argued local lemmas, the identification clause, BFT-3 and BFT-4 (c₀), boxes, small tori

Worker file (Opus 5.5, worker role; the shared rules of REVIEW_BRIEF_55 apply). Brief: `scratchpad/queue/offglob2.md`, plus
the coordinator's scope message (BFT4B55 Theorem T0 / Lemma AVG: off 𝒞_glob the BFT-4 target is **(c₀)**, bounded local
holomorphic pieces on the gauge-invariant data class, with no invariance clause). Writes only this file and
`checks/o2_55_*`. No git. Append-only after this header.

## PRE-STATED (written 2026-10-29T04:31:24Z UTC, before any derivation; statements only)

Read before this block (reading only, nothing derived): REVIEW_BRIEF_55 (all); the brief; OFFGLOB55 (all 800 lines, incl.
errata E1-E6); BFT34_55 §0-§2.7; BFT4W55 (all, incl. §10 errata and §15); CODEX_REVIEW_BFT4W (all 249 lines; complete, ends
with "Exactly what may be banked"); NSL55 §2-§4.4; CODEX_REVIEW_NSL F3-F10 and banking (complete); REVIEW_S22 Part 5 (the BFT
statement); PROOF.md header incl. [S26-BANKED]; KFACTOR_OFF55 §1-§4; CODEX_REVIEW_KOFF §4.3, §5.3 and banking; PROOF.md
"Lemma N5-cov", "Lemma AX", "Theorem RW", "Theorem N5-sf0"; HANDOFF.md; BFT4B55 §1, §2.3 (Theorem T0), §3 (Lemma AVG).
CODEX_REVIEW_OFFGLOB.md did not exist at 04:31Z; I will re-check before relying on any OFFGLOB55 step and will not build on
anything it refutes.

**Targets** (each: a proof k- and T-uniform, or the precise obstruction with a counterexample).
- **A1 (W-comm)^σ and W-mult^σ off 𝒞_glob.** Cutoff multiplier and Hessian-commutator bounds at frame-patched data
  (configuration ỹ small in a frame, not the trivial chain), with contour-centred cutoff evaluation (BFT4W55 Convention C,
  binding by Proposition CORNER); decide whether the frame transfer (constant transition parts O(1), variations O(η)) costs
  anything beyond 1 + O(η).
- **A2 CONV (G- and s-slots) and (ND).** Background-cc sources in frame coordinates, made flat-cc at cost (1 + O(η)), k-uniformly;
  the non-criticality defect bound.
- **A3 RG and FP.** Frame rigidity (two frame-small representatives of one configuration differ by a constant times a small
  gauge) and frame patching on bounded boxes, with explicit dependence on the box size.
- **B1 identification clause of BFT-0 off 𝒞_glob** (Theorem ID frame-locally): per-level criticality, value recursion and
  per-level uniqueness modulo root-trivial gauges, for real data in the full curvature-small class.
- **B2 BFT-3 off 𝒞_glob** (n ≤ 4 derivatives of the critical point and of E_k^br with tree decay), with a stated gauge
  convention for the gauge-dependent object U_j.
- **B3 BFT-4 off 𝒞_glob = (c₀)**: E_k^br = S_W + c + Σ_XR(X), R(X) holomorphic and bounded on the class restricted to its
  support, local, *-connected, with a k-, T-uniform polymer norm; plus (H-inv) for E_k^br so that Lemma AVG applies.
- **B4 boxes** (non-wrapping boxes with N5-sf0's boundary convention), **B5 tori T < 4R + 6** if a consumer needs them.
- **C assembly**: BFT-0..4 ((a)/(c₀)) on REVIEW_S22's full small-field data class as an implication, every input named with
  its status (banked / Codex-conditional / proved here / ARGUED / OPEN).

**What would count as a refutation** (of my targets or of the lane's route through OFFGLOB55).
- A1: a frame-patched configuration (curvature ≤ ε) and a cutoff of scale ℓ for which the σ-weighted multiplier or commutator
  ratio grows with k or T, or exceeds 1 + C/ℓ + Cη by a k-dependent factor (e.g. because the background-dependent linearised
  root map Q_ỹ breaks the first-moment cancellation that CEN1 proves at ỹ = 0).
- A2: a background-cc source whose flat-cc conversion costs a k-dependent factor (e.g. a bare charge of the G-slot of own size
  not small enough to survive HR (v)'s L^{d(k−j)} routing weight), or a level sum that is not summable.
- A3: two frames of one configuration on a box whose transition is not (constant)×(small), or a box cover whose cycle
  holonomies are not near 1 (contractible loops of large area), with the box size at which this happens.
- B1: a real datum in the class with two critical points in the frame-local ball that are not root-trivially gauge equivalent,
  or a level where per-level criticality fails.
- B2: a frame change or gauge convention under which the derivative bound loses the exponential tree decay or a k-, T-uniform
  constant.
- B3: an obstruction to defining the pieces on the whole gauge-invariant class restricted to a large (e.g. non-simply-connected)
  support — a piece that must be unbounded or undefined at small-curvature data with holonomy around a loop of the support; or
  failure of (H-inv) for E_k^br.
- B4/B5: a boundary convention or a torus size at which the small-field problem is not solvable by the same mechanism.
- C: any input I label PROVEN that an on-disk Codex review marks NOT-VERIFIED or REFUTED, or that depends on a refuted step.
A counterexample to any step is a first-class result and will be reported as such.

Vocabulary: PROVEN-HERE (complete argument here), PROVEN as an implication (of named inputs), ARGUED (reason, hole named),
OPEN, FALSE (counterexample). For others' claims: CONFIRMED / NOT-VERIFIED / REFUTED.

# FINDINGS (appended from 2026-10-29T04:40Z; everything below was written after the PRE-STATED block)

## §0. Symbols pinned, inputs and their status

**Symbols (systemic defect 1; every one located by file + string).**
- ε := REVIEW_S22's data parameter (max_P|log V^r_{k,P}| ≤ ε); d(W,1) := min{|X| : e^X = W} (OFFGLOB55 §0).
- ‖·‖_{(σ)}, N^{(σ)} := KFACTOR_OFF55 §1.2 ("1.2 The transport-weighted pair"); ‖·‖_{(σ),Ω}, N^{(σ)}_Ω := the same with every sup
  and Hölder pair restricted to links/plaquettes/contours inside Ω (OFFGLOB55 §1.7). ‖ξ‖_♮, n_0, η(x) := NSL55 §0.
- 𝔇_k(R, η), frames ĝ_Ω, y_Ω := log U^{ĝ_Ω} := OFFGLOB55 §1.7; R′ := 4R + 5; Ω_□ := □^{(R+3)}.
- 𝒦_y := P_ccH^{log}_y + Γ^TΓ (OFFGLOB55 §4.1; local name). P_U, P^U_cc, D_U, cc_U := OFFGLOB55 §3.1-§3.2.
- C^σ_M(ℓ), C^Y_M(ℓ) := BFT4W55 "Proposition WM^σ"; C^σ_c := BFT4W55 "Proposition WC^σ"; C_Q := 2p_Lδ_*² (BFT4W55
  "Corollary CEN1-T"; 1331/2 at d = 4, L = 3, Codex BFT4W W3). Convention C := BFT4W55 §2.1 (contour-centred positions).
- K := the local Lipschitz constant of Codex KOFF §5.3; G := the cc response constant (G_♯); η_* := the fixed local analytic
  radius of Codex KOFF §4.3; C_cc := 2d(59/100)L^{d−1} (≤ 127.44 at d = 4, L = 3).
- New local names (this file only): C_RG, C_FP, κ_W (frame window), 𝔉-objects carry OFFGLOB55's names.

**Inputs and their status (as on disk at 04:40Z).**
| Input | Status |
|---|---|
| K^{(σ)} chain: HR (i)-(v), CCP (a)-(d), SG, ROW^{(σ)}, CB, TOP♯, LIN^{(σ)}, corrected Theorem K (Codex KOFF §5.3) | [S26-BANKED], conditional on the lane-A linear package |
| GV-E, BFT-E (x(B), slice uniqueness, holomorphy, composite value) | [S26-BANKED] (Codex GV items 2-4) |
| EP algebra, EP-bd at weight 0, finite reach of Π_E | [S26-BANKED] (Codex GSHARP item 1) |
| NSL, Corollary K-U, Theorem ID (I1)-(I4) at the trivial background on 𝒞_glob | [S26-BANKED] conditional (Codex NSL items 2-3; SC repair F3, subgroup wording F5) |
| CEN1, CORNER, WM^σ, WC^σ (Convention C) | [S26-BANKED] PROVEN (Codex BFT4W items 1, W3-W4) |
| RWE, H2W, Dcc, IDcc, E2^σ, BBcc, BFT4a-glob | [S26-BANKED] conditional on (R) (Codex BFT4W W5-W9) |
| (R): per-density local holomorphic estimates | NOT-VERIFIED (Codex BFT4W W1); RLOC55 running |
| Lemma WD, Theorem BFT3-glob (route C) | [S26-BANKED] conditional (Codex BFT34 items 1-5) |
| OFFGLOB55 (Theorem OFF, GP, LOC-cc_U, L1, L2, AP, UQ) | Opus only; CODEX_REVIEW_OFFGLOB absent at 04:40Z |
| BFT4B55 Theorem T0, Lemma AVG | Opus only; Codex launching |

**Read after §0 was written (06:0xZ), and decisive for the order of work below.** CODEX_REVIEW_OFFGLOB.md (340 lines, complete:
ends with "Exactly what may be banked" items 1-6 and "Not banked") and CODEX_REVIEW_BFT4B.md R3, R4, R8, R9 and banking (283 lines,
complete). OFFGLOB55's Theorem OFF is **not banked**: F6 (slot cutoffs are representation-dependent, so GP's operator was never
defined), F7 (real-frame AP is false on complex pure gauges — exact SU(2) counterexample), F8 (UQ's q ≤ q/2 needs a *relative,
root-preserving* patching estimate that single-field FP does not give), F9 (ND must be priced through the aggregate Ward identity,
with the sign +DK^T∇F). Banked from it (Codex OFFGLOB items 1-5): AX/class inclusions, C4, corrected C6, U1 (3.3ε_0), U2, real
covariant routing and exact cc localisation for a supplied representation (coefficient 221 + (324√2/n)η_F + 2592η_ρ; G-charge [G, w]),
conditional L1/L2 (ΓK_y = **+1** + ΓK′_y), the one-level lift, the abstract NK recurrence, smooth frame-log W-mult, the corrected
summable flat commutator counts. **I build only on these, on the [S26-BANKED] items of §0, and on what I prove here.** The
order below follows the coordinator's message: §1 frames (rigidity, patching, relative patching), §2 the complex convention, §3 the
parametrix on representations, §4 the repaired nonlinear theorem, then identification, BFT-3, BFT-4 (c₀), boxes, assembly.

## §1. Frames: rooted rigidity, root matching, merging, patching, relative patching

### 1.0 Conventions for this section
- **Cells and roots.** A *box* Ω is a product of coarse intervals that is a union of closed level-k cells (coarse unit cubes) and does
  not wrap (side ℓ(Ω) ≤ T − 1). Its roots are the level-k roots (level-0 images of cell centres) of its cells; every level-0 site of Ω
  is within coarse ℓ¹-distance d/2 of the root of its cell, joined to it by a level-0 axial path inside the cell.
- **Frames.** A frame of U on Ω is a real gauge ĝ : level-0 sites of Ω → SU(N) (acting on level j through ev^{(j)}, on the datum
  through its root values); y := log U^{ĝ} on every link of every level inside Ω, datum included; its **size** is ‖y‖_Ω :=
  ‖y‖_{(σ),Ω} (pointwise Hölder version, NSL55 §0, data-inclusive top residual). Two frames ĝ, ĝ′ (possibly of different
  configurations) are **root-matched on Ω** if ĝ = ĝ′ at every root of Ω.
- **The gauge action** is NSL55's: (x^g)_i(b) = log(g_i(b^−)e^{x_i(b)}g_i(b^+)^{−1}), (x^g)^{g′} = x^{g′g}; U^{hĝ} = (U^{ĝ})^h.
- **Imported tools (all CONFIRMED by Codex NSL F6, conditional only on NSL's elliptic input, which §1 never uses):** NSL55 Lemma B
  — the identity (B0) (x^{e^ξ})^c_i = x^c_i − (Ξξ)^c_i + G_{h_i}(u_i, x^c_i, (Ξξ)^c_i), u_i := ξ at the base site, and the bounds
  (B1)-(B2) with the absolute constant K_G ≤ 1403.1 (Codex NSL F4) on max(‖u‖, ‖a‖, ‖β‖) ≤ R_B := 1/(20C_alg), C_alg = 8, in the
  Banach-algebra norm ‖·‖_{1,α;i}; (B0)-(B2) are algebraic/majorant statements valid for **every** level-0 ξ (Λ_* is used in NSL only
  for Lemma A (b), (c) and for r_{j−1}(Ξμ) = 0). Lemma A (d)'s averaging bound ‖(Ξξ)^c_i‖_{1,α;i} ≤ ‖ξ‖_♮ likewise holds for every ξ.
  NSL55 Lemma C (|Δ_l| ≤ C_Δ[h_l³η(y)² + h_lη(y)|r_l(y)|], η(y) the sup+gradient size, no residual hypothesis) and Lemma D
  (the exact covariance ρ_l(U^g)(c) = Ad(g(c_Y))ρ_l(U)(c) for **every** composite gauge, roots included, and its weighted bound).
  Notation: a := sup|·| of an object on Ω; η(·) := NSL's sup+gradient size (datum included).

### 1.1 Lemma RG′ (rooted frame rigidity) — PROVEN-HERE
*Statement.* There are η_RG > 0 and C_RG < ∞ depending only on (N, d, α) such that: if ĝ_1, ĝ_2 are **root-matched** frames of
the same U on a box Ω with sizes ≤ η ≤ η_RG, then h := ĝ_1ĝ_2^{−1} = e^{τ} on Ω with τ = 0 at every root of Ω and
**‖τ‖_{♮,Ω} ≤ C_RGη** — no dependence on k, T or the side of Ω.
*Unrooted form.* If only ĝ_1(r_0) = ĝ_2(r_0)·c^{−1}… more simply: for any frames, h = c·e^{τ} with c := h(r_0) at one root r_0,
τ(r_0) = 0, ‖τ‖_♮ − ‖τ‖_∞ ≤ C_RGη and ‖τ‖_∞ ≤ C_RG·D_Ω·η, D_Ω the coarse ℓ¹ diameter of Ω, provided D_Ωη ≤ η_RG.
*Proof.* (i) *Linkwise relation.* For a level-0 link b = (x, x′) ⊂ Ω, e^{y_1(b)} = h(x)e^{y_2(b)}h(x′)^{−1}, hence
h(x)^{−1}h(x′) = e^{−Ad(h(x)^{−1})y_1(b)}e^{y_2(b)} and d(h(x)^{−1}h(x′), 1) ≤ |y_1(b)| + |y_2(b)| ≤ 2η/n (own units, n = L^k;
bi-invariance, OFFGLOB55 Lemma C1, Codex-confirmed). Every site is joined to its cell's root r(x) (where h = 1) by ≤ dn/2 fine
steps, so d(h(x), 1) ≤ dη < π: τ := log h (principal) is defined, |τ| ≤ dη. (ii) *A uniform analytic generator.* Put
F(τ, w) := log(e^τe^w) − τ and, for coarse values Y = (Y_1, Y_2) ∈ su(N)²,
  **Φ_n(τ, Y) := n·F(τ, log(e^{−Ad(e^{−τ})Y_1/n}e^{Y_2/n})).**
By (i), ∇^c_μτ(x) = n(τ(x + e_μ) − τ(x)) = Φ_n(τ(x), y^c_1(x, μ), y^c_2(x, μ)) exactly (y^c := n·y at level 0). Expanding,
Φ_n(τ, Y) = ψ(ad_τ)(Y_2 − Ad(e^{−τ})Y_1) + n^{−1}Φ̂_n(τ, Y) with ψ(z) = z/(1 − e^{−z}) and Φ̂_n a convergent series whose
coefficients are bounded **uniformly in n ≥ 1** (every BCH word of degree m in Y/n carries n^{1−m} ≤ 1 for m ≥ 1, as in Lemma B's
G_h); Φ_n(τ, 0) = 0. So on the fixed polydisc |τ| ≤ ¼, |Y| ≤ 1 there is an absolute C_Φ with |Φ_n| ≤ C_Φ|Y|, |∂_τΦ_n| ≤ C_Φ|Y|,
|∂_YΦ_n| ≤ C_Φ, and second derivatives ≤ C_Φ, uniformly in n. (iii) *Bounds.* ‖∇^cτ‖_∞ ≤ C_Φ·2η. Second differences:
∇^c_ν∇^c_μτ(x) = n[Φ_n(τ(x + e_ν), Y(b + e_ν)) − Φ_n(τ(x), Y(b))], and the mean-value inequality gives
|∇^c_ν∇^c_μτ| ≤ sup|∂_τΦ_n|·|∇^c_ντ| + sup|∂_YΦ_n|·|∇^c_νY| ≤ C_Φ·2η·2C_Φη + C_Φ·2η. The Hölder quotient of ∇^c∇^cτ over pairs at
coarse distance ≤ 1 is bounded the same way by the Hölder quotients of ∇^cY (≤ 2η) and Lipschitz/Hölder quotients of the
first-order factors (≤ C(η + η²)), using the second-derivative bound of Φ_n. No bootstrap is used: every quantity is an explicit
analytic function of (τ, Y) evaluated pointwise. (iv) *Rooted sup.* τ = 0 at roots, so |τ(x)| ≤ (d/2)‖∇^cτ‖_∞ ≤ dC_Φη.
Unrooted: the same with τ := log(c^{−1}h), c = h(r_0), and the path from r_0, of coarse length ≤ D_Ω. (v) *Higher levels* need no
separate argument: U_j^{ĝ_1} = (U_j^{ĝ_2})^{h} with h evaluated at level-0 images, so h is determined by level 0. ∎

### 1.2 Lemma RM (root matching) — PROVEN-HERE
*Statement.* There are c_RM > 0, C_RM < ∞ (depending on N, d, L, α, σ) such that: if ĝ_1, ĝ_2 are frames of the same U on a box Ω
with sizes ≤ η and D_Ωη ≤ c_RM, then there is a frame ĝ_2′ of U on Ω^− (Ω shrunk by one coarse unit on each face), **root-matched
to ĝ_1 on Ω^−**, of the form ĝ_2′ = c·e^{θ}ĝ_2 with c ∈ SU(N) constant, θ = I_Ω(τ_r), and size ≤ C_RMη.
*Proof.* At roots r, r′ joined by a level-k link c, e^{y_{1,k}(c)} = h(r)e^{y_{2,k}(c)}h(r′)^{−1}, so d(h(r)^{−1}h(r′), 1) ≤
|y_{1,k}(c)| + |y_{2,k}(c)| ≤ 12η (the datum obeys ‖y_k‖_D ≤ (p_L/L + 1)‖y‖ ≤ 6‖y‖, NSL55 §3.6). With c := h(r_0) and
τ_r := log(c^{−1}h) on roots: first differences ≤ C·12η, |τ_r| ≤ CD_Ωη. Let I_Ω be the quintic-tent interpolation of root values of
the cells of Ω (NSL55 §0's I with χ^5 of coarse scale 1), which is exact at roots of Ω^− and obeys, on Ω^−,
‖I_Ωu‖_∞ ≤ sup|u| and ‖∇^cI_Ωu‖_∞ + ‖∇^c∇^cI_Ωu‖_∞ + [∇^c∇^cI_Ωu]^∞_α ≤ C_χ·max_{neighbouring roots}|u(r) − u(r′)| (because
Σ_X∇χ_X = 0, so derivatives see only differences). Then θ := I_Ω(τ_r) has ‖θ‖_♮ ≤ C(D_Ω + 1)η and ‖Ξθ‖_{1,α;i} ≤ Cη, and
y_2′ := log U^{ĝ_2′} = Ad(c)(y_2)^{e^{θ′}} with θ′ := Ad(c^{−1})θ. Lemma B (B1) on every level i < k (hypothesis
4‖θ‖_♮ ≤ R_B: from D_Ωη ≤ c_RM) gives ‖(y_2′)^c_i‖_{1,α;i} ≤ η + Cη + 5K_GC(D_Ω + 1)η(5C(D_Ω + 1)η + η) ≤ C′η; at level k the same
algebra with h = 1 (G_1) bounds the new datum by Cη; the weighted residual legs, by Lemma D (exact covariance at every level,
roots included, then absorption), are ≤ 3η + 2C_ΔL^{−3}(η(y_2)² + η(y_2′)²) ≤ 4η. ∎

### 1.3 Lemma MG (merging two frames across a slab) — PROVEN-HERE
*Setting.* Boxes A, B with A ∪ B a box and O := A ∩ B a box that is a *slab* in a direction μ: its μ-width w ≥ 8 and its
extent in the other directions equals that of A ∪ B; ρ_O := D_O/w (D_O its ℓ¹ diameter). A smooth cutoff φ(x_μ) with φ = 1 on the
quarter of O adjacent to A ∖ O, φ = 0 on the quarter adjacent to B ∖ O, and coarse C^{2,1} norms |∇φ| ≤ 4/w, |∇²φ| ≤ 32/w²,
|∇³φ| ≤ 256/w³. A base root r_0 ∈ O.
*Construction (deterministic given (ĝ_A, ĝ_B, φ, r_0)).* h := ĝ_Aĝ_B^{−1} on O, c := h(r_0), τ̃ := Ad(c)·log(c^{−1}h) (so
ĝ_A = e^{τ̃}ĝ_B′ on O with ĝ_B′ := cĝ_B, τ̃(r_0) = 0), and
  **ĝ := ĝ_A on A ∖ O,  ĝ := e^{φτ̃}ĝ_B′ on O,  ĝ := ĝ_B′ on B ∖ O.**
It is consistent (φ = 1 next to A ∖ O gives ĝ_A; φ = 0 next to B ∖ O gives ĝ_B′), and **its root values are functions of the root
values of ĝ_A, ĝ_B alone** (c, and τ̃ at roots, are computed from h at roots).
*Statement.* There are c_MG > 0, C_MG < ∞ (depending on N, d, L, α, σ and an upper bound ρ̄ ≥ ρ_O) such that if ĝ_A, ĝ_B are
frames of U on A, B of sizes ≤ η and D_{A∪B}η ≤ c_MG, then ĝ is a frame of U on A ∪ B of size ≤ C_MGη.
*Proof.* Off O nothing changes (ĝ_B′ differs from ĝ_B by a constant: y_B′ = Ad(c)y_B, an isometry of every leg). On O,
y = (y_B′)^{e^{φτ̃}}. By the unrooted Lemma RG′ on O: ‖∇^cτ̃‖_{1,α;0} ≤ C_RGη, ‖τ̃‖_∞ ≤ C_RGD_Oη. Product rule:
‖φτ̃‖_∞ ≤ C_RGD_Oη, ‖∇^c(φτ̃)‖_∞ ≤ C_RGη(1 + 4ρ_O), ‖∇^c∇^c(φτ̃)‖_∞ + [∇^c∇^c(φτ̃)]^∞_α ≤ C_RGη(1 + 8/w + 64ρ_O/w + …)
≤ C(1 + ρ̄)η. Hence ‖φτ̃‖_♮ ≤ C(D_O + 1 + ρ̄)η ≤ R_B/4 for D_{A∪B}η ≤ c_MG, and ‖Ξ(φτ̃)‖_{1,α;i} ≤ C(1 + ρ̄)η at every level
(Lemma A (d) averaging). Lemma B (B1) at each level i < k:
  ‖y^c_i − (y_B′)^c_i + (Ξ(φτ̃))^c_i‖_{1,α;i} ≤ 5K_G·C(D_O + 1 + ρ̄)η·(5C(D_O + 1 + ρ̄)η + η) ≤ η,
so the potential legs are ≤ (2 + C(1 + ρ̄))η. Datum: the same algebra on the root lattice (h = 1). Weighted residual legs: Lemma D
(exact covariance, absorption) gives ≤ 3η + 2C_ΔL^{−3}(η(y_B′)² + η(y)²) ≤ 4η. ∎
*Remark (why the sup of τ̃ is harmless).* τ̃ grows linearly with the distance from r_0 (that is the holonomy of the configuration
seen between two frames), but it enters the new potentials only through ∇(φτ̃) = φ∇τ̃ + τ̃∇φ, and |τ̃∇φ| ≤ C_RGD_Oη·4/w =
4C_RGρ_Oη: a slab of bounded aspect ratio ρ_O costs a bounded factor, whatever its absolute size. The absolute size enters only
through the smallness condition D_{A∪B}η ≤ c_MG (BCH convergence), never through a constant.

### 1.4 Lemma FP (single-field patching onto Ω_□) — PROVEN-HERE
*Setting.* RW-cc's product partition {□} (sides in [R, 2R)), cores K_□ := □^{(R/2−3)}, Ω_□ := □^{(R+3)} (side ≤ 4R + 5 ≤ R′),
R ≥ 24. For a fixed □, the boxes □′ whose cores meet Ω_□ form a product family with at most 6 intervals per coordinate;
consecutive cores overlap in slabs of width R − 6 ≥ 18, and every slab used below has ρ_O ≤ ρ̄ := 8d (its extent in the other
directions is < 6R + 6d and R − 6 ≥ 3R/4).
*Statement.* There are c_FP > 0 and C_FP < ∞ depending only on (N, d, L, α, σ) — **not on R, k, T** — such that: if U has, on
every core K_□′ meeting Ω_□, a frame of size ≤ η, and Rη ≤ c_FP, then U has a frame on Ω_□ of size ≤ C_FPη. The patched frame is
produced by a deterministic sequence of at most 6^d merges (Lemma MG) along directions 1, …, d, with prescribed base roots and
cutoffs, and C_FP := C_MG(ρ̄)^{5d}.
*Proof.* Merge the ≤ 6 cores of each row in direction 1 consecutively (≤ 5 merges, each a slab of width ≥ R − 6, aspect ≤ ρ̄), then
the resulting row unions in direction 2 (their overlaps are again slabs of width ≥ R − 6, aspect ≤ ρ̄), and so on; restrict the
final frame to Ω_□. Each merge multiplies the size bound by C_MG; along each direction the merges are sequential (≤ 5), giving
C_MG^{5d}. Every merged region has ℓ¹ diameter ≤ d(6R + 6), so Rη ≤ c_FP := c_MG/(7d) gives the hypothesis of every MG step. ∎
*Scope.* FP needs no cycle condition and no holonomy hypothesis: the regions merged are boxes, each merge is across one slab, and
the constants absorbed (c at r_0) are those of a tree (the merge order). Holonomy around loops inside Ω_□ is not small in absolute
terms (it is O(R²κ), κ the coarse curvature), but it never has to be: it shows up only as the growth of τ̃ across a slab, which
Lemma MG's remark prices at 4C_RGρ̄η.

**Erratum E1 (to §1.2-§1.4, found on re-reading Lemma B's (B1); statements corrected, mechanism unchanged).** Lemma B's (B1)
majorant charges the gauge's *sup* through ‖u_i‖ ≤ 4‖ξ‖_♮ in both factors, so with ‖ξ‖_∞ ≲ Dη the remainder is
≲ K_G(Dη)², and absorbing it into O(η) needs **D²η small**, not Dη small. Read: Lemma RM's hypothesis **D_Ω²η ≤ c_RM**;
Lemma MG's **D_{A∪B}²η ≤ c_MG**; Lemma FP's **R²η ≤ c_FP** (c_FP := c_MG/(7d)²). Every constant C_RM, C_MG, C_FP stays
independent of R, k, T. (For real gauges the sup of ξ is in fact harmless — Ad(e^u) is an isometry and the BCH coefficients of
log(e^u e^{−u−β}) are bounded for |u| ≤ π/2 — so the weaker Dη condition is provable by splitting x^{e^ξ} = log(e^{Ad(e^u)x}e^Z),
Z := log(e^ue^{−u−β}); I do not need it: R is fixed before ε and the smallness ε ≤ ε_*(R) absorbs any power of R.) The
statement of Lemma RG′ is also cleaner read as: **(rooted)** ‖τ‖_♮ ≤ C_RGη; **(unrooted)** for any two frames h = c·e^τ with
c = h(r_0), τ(r_0) = 0, ‖τ‖_♮ − ‖τ‖_∞ ≤ C_RGη and ‖τ‖_∞ ≤ C_RGD_Ωη, provided D_Ωη ≤ η_RG (the phrase "If only ĝ_1(r_0) = …"
in §1.1 is a false start and carries no content).

### 1.5 Lemmas C′ and D′ (difference versions of NSL55 Lemmas C, D) — PROVEN-HERE
*Lemma C′.* There are η_1′ > 0, C_Δ′ < ∞ (depending on N, L) such that for depth-j configurations y, y′ (same depth, data
included) with η(y), η(y′) ≤ η_1′, every l < j and every level-(l+1) link c (own units, h_l = L^{l−j}):
  **|Δ_l(y)(c) − Δ_l(y′)(c)| ≤ C_Δ′[h_l³(η(y) + η(y′))η(y − y′) + h_lη(y)|r_l(y)(c) − r_l(y′)(c)| + h_l|r_l(y′)(c)|η(y − y′)].**
*Proof.* NSL55 Lemma C's decomposition (Codex NSL F6 item 3-4): Δ = â + β(X_0, ŵ), X_0 = Q_ly_l + â, ŵ = r_l(y) + â, where â is a
convergent series in the contour variables whose degree-2 part avg B₂ is a centred symmetric bilinear form and whose tail is cubic.
Polarisation: avg B₂(y) − avg B₂(y′) = avg B₂(y − y′, y + y′); the centring argument of Codex NSL F6 item 3 (direction-constant
arguments give zero; each variation costs one factor h_l∇) bounds a centred bilinear form by C h_l³η(u)η(v) for arguments u, v,
so |â(y) − â(y′)| ≤ Ch_l³(η(y) + η(y′))η(y − y′) (tail: Cauchy on the fixed polydisc of local variables, which are O(h_l·η)).
β is analytic on a fixed polydisc with β(X, 0) ≡ 0 ≡ β(0, w), hence |∂_Xβ(X, w)| ≤ C|w|, |∂_wβ(X, w)| ≤ C|X| and
|β(X, w) − β(X′, w′)| ≤ C(|w||X − X′| + |X′||w − w′|). Insert |X_0| ≤ 2p_Lh_lη, |X_0 − X_0′| ≤ 2p_Lh_lη(y − y′) + |â − â′|,
|ŵ − ŵ′| ≤ |r_l(y) − r_l(y′)| + |â − â′|, |ŵ| ≤ |r_l(y)| + Ch_l³η². ∎
*Lemma D′.* For real x, x′ and real composite gauges g = e^ξ, g′ = e^{ξ′} with η(x), η(x′), η(x^g), η(x′^{g′}) ≤ η_2′ :=
min(η_1′, 1/(4C_Δ′)), every l < j, with weight w_l := L^{(1+σ)(j−1−l)}, own-to-coarse factor L^{j−1−l}:
  **w_l‖r^c_l(x^g) − r^c_l(x′^{g′})‖_∞ ≤ 3w_l‖r^c_l(x) − r^c_l(x′)‖_∞ + C_D′[L^{−3}(η(x) + η(x′) + η(x^g) + η(x′^{g′}))·
  (η(x − x′) + η(x^g − x′^{g′})) + (w_l‖r^c_l(x′)‖_∞)·(η(x − x′) + η(x^g − x′^{g′}) + 2 sup|ξ − ξ′|_{level-(l+1) sites})].**
*Proof.* From the exact covariance, r_l(x^g) = Ad(g(c_Y))[r_l(x) + Δ_l(x)] − Δ_l(x^g), and the same primed. Subtract:
r_l(x^g) − r_l(x′^{g′}) = Ad(g(c_Y))[Δr + ΔΔ] + (Ad(g(c_Y)) − Ad(g′(c_Y)))[r_l(x′) + Δ_l(x′)] − [Δ_l(x^g) − Δ_l(x′^{g′})].
Ad of a real element is an isometry; |Ad(e^a) − Ad(e^{a′})| ≤ 2|a − a′|. Bound ΔΔ and the last bracket by Lemma C′; the term
h_lη(x^g)|r_l(x^g) − r_l(x′^{g′})| is absorbed into the left side (C_Δ′h_lη ≤ ¼). Multiply by L^{(2+σ)(j−1−l)} (own form of
w_l): the h_l³ terms give L^{(σ−1)(j−1−l)−3} ≤ L^{−3} (σ ≤ 1) — a maximum over levels, no level sum; the h_l|r(x′)| terms give
h_l·(w_l‖r^c_l(x′)‖), and h_l ≤ 1. Lemma C bounds |Δ_l(x′)| ≤ Ch_l³η² + Ch_lη|r_l(x′)|, giving the ξ − ξ′ term. ∎

### 1.6 Lemma RM* (root matching across two configurations with the same data) — PROVEN-HERE
If U, U′ have the **same datum** V on a box Ω, and ĝ, ĝ′ are frames of U, U′ on Ω of sizes ≤ η with D_Ω²η ≤ c_RM, then
ĝ′_* := c·e^{θ}ĝ′ (c constant, θ = I_Ω(τ_r)) is a frame of U′ on Ω^− of size ≤ C_RMη, **root-matched to ĝ on Ω^−**.
*Proof.* Lemma RM's proof uses the two frames only through their data: e^{y_k(c)} = ĝ(r)V_cĝ(r′)^{−1} and
e^{y′_k(c)} = ĝ′(r)V_cĝ′(r′)^{−1} give d(t(r)^{−1}t(r′), 1) ≤ |y_k(c)| + |y′_k(c)| ≤ 12η for t := ĝĝ′^{−1} at roots; the size
estimate of ĝ′_* uses only U′'s own frame and the bounds on θ. ∎
*Consequence used in §4.* **Root-matched frames of two configurations with the same datum have identical frame data:**
y_k = y′_k on Ω^−. All their differences live at levels < k.

### 1.7 Lemma RFP (relative, root-preserving patching) — PROVEN-HERE. *This is the estimate Codex OFFGLOB F8 asks for.*
*Setting.* As in Lemma FP. U, U′ real composite configurations with the same datum. On every core K_□′ meeting Ω_□, frames
ĝ_□′ of U and ĝ′_□′ of U′, **root-matched on K_□′** (pairwise, same index; no relation is assumed between different cores), of
sizes ≤ η, with q := max_□′‖y′_□′ − y_□′‖_{K_□′} (σ-norm of the difference of frame coordinates, data-inclusive; by §1.6 the data
parts coincide). Let G, G′ be the frames on Ω_□ produced from the two families by Lemma FP's merge sequence **with the same base
roots r_0 and the same cutoffs φ at every merge**.
*Statement.* There are c_RFP > 0 and C_RFP < ∞ depending only on (N, d, L, α, σ) — not on R, k, T — such that if R²η ≤ c_RFP:
**(a) G and G′ are root-matched on Ω_□; (b) ‖log U′^{G′} − log U^{G}‖_{Ω_□} ≤ C_RFP·q; (c) both have size ≤ C_FPη.**
*Proof.* One merge (Lemma MG) at a time; induct over the merge sequence.
(a) The merge's constant c = h(r_0) and c′ = h′(r_0) coincide, because ĝ_A = ĝ′_A and ĝ_B = ĝ′_B at roots. For the same reason
h = h′ at every root of O, so τ̃ = τ̃′ at every root of O, so φτ̃ = φτ̃′ at roots: the merged frames have equal root values.
(b) *Transition difference.* Write Δτ := τ̃′ − τ̃ on O; it vanishes at every root of O. From ∇^cτ̃ = Φ_n(τ̃, Y), ∇^cτ̃′ =
Φ_n(τ̃′, Y′) (Lemma RG′ (ii)) with Y = (y_A, Ad(c)y_B), |Y′ − Y| ≤ q_A + q_B:
|∇^cΔτ| ≤ sup|∂_τΦ_n|·|Δτ| + sup|∂_YΦ_n|·|Y′ − Y| ≤ 2C_Φη·(d/2)‖∇^cΔτ‖_∞ + 2C_Φq, hence ‖∇^cΔτ‖_∞ ≤ 4C_Φq when dC_Φη ≤ ½; second
differences and their Hölder quotients likewise (second derivatives of Φ_n bounded uniformly in n); and ‖Δτ‖_∞ ≤ (d/2)‖∇^cΔτ‖_∞
(rooted). So **‖Δτ‖_♮ ≤ C′q with no dependence on the slab's size** — the root matching is exactly what removes it.
*Potential legs.* On O, y = (y_B′)^{e^{φτ̃}}, y′ = (y′_B′)^{e^{φτ̃′}} with y_B′ = Ad(c)y_B, y′_B′ = Ad(c)y′_B. By (B0) at level i:
Δy^c_i = Δ(y_B′)^c_i − (Ξ(φΔτ))^c_i + [G(u′, a′, β′) − G(u, a, β)], and (B2) bounds the bracket by
K_G[(‖u‖ + ‖β‖ + ‖u′‖ + ‖β′‖)‖a′ − a‖ + (‖u‖ + ‖a‖ + ‖β‖ + ‖u′‖ + ‖a′‖ + ‖β′‖)(‖u′ − u‖ + ‖β′ − β‖)] ≤ K_G·C(D_O + 1)η·Cq,
using ‖u‖ ≤ C(D_O + 1)η (Lemma MG), ‖u′ − u‖ ≤ ‖φΔτ‖ ≤ C′q, ‖β′ − β‖ = ‖Ξ(φΔτ)‖ ≤ C′(1 + 4d/w)q. With D_Oη ≤ 1/(K_GC) the
potential legs of Δy are ≤ C″q.
*Residual legs.* Lemma D′ with x = y_B′, x′ = y′_B′, g = e^{φτ̃}, g′ = e^{φτ̃′}: the weighted residual difference is ≤
3q + C_D′[L^{−3}·4C_MGη·(q + C″q) + C_MGη·(q + C″q + 2C′q)] ≤ 4q for η small.
*Off the slab* the differences are those of the inputs (Ad(c) is an isometry). So one merge maps (q_A, q_B) to
≤ C_RMG·max(q_A, q_B), C_RMG := max(C″ + 1, 4); along the sequence, C_RFP := C_RMG^{5d}. (c) is Lemma FP. ∎
*What this supplies for uniqueness (used in §4.4).* Given two root-matched core-frame families, the patched Ω-frames are
root-matched and their coordinate difference is controlled by the **core** differences with an R-independent constant. The
gauge-alignment cost that Codex F8 says must be "proportional to ‖Z′ − Z‖" is exactly ‖Δτ‖_♮ ≤ C′q; it is proportional to q,
not O(η), **because root matching pins Δτ to zero at every root of every overlap.**

## §2. The complex convention (repairs Codex OFFGLOB F7)

### 2.1 F7 re-derived — CONFIRMED (agree with Codex)
k = 1, N = 2, V = 1, h(z_0) = exp(tH) (H = diag(1, −1)) at one non-root level-0 site, h = 1 elsewhere, U_b := h(b^−)h(b^+)^{−1}.
Every plaquette holonomy is 1 (pure gauge), every S4′ path joins level-1 roots where h = 1, so every path transport and the
residual are 1 and 0: U is a complex critical configuration with real data. On an incident link U_b has singular values e^{±t};
real gauges are unitary and do not change singular values, so in **every real frame** |log| ≥ t on that link (‖exp Y‖_op ≤
e^{‖Y‖_op}). Hence no real-frame a priori estimate "size ≤ C_0ε" can hold on complex configurations, and complex critical points
are not unique modulo real gauges. Codex's conclusion stands; OFFGLOB55's E5 reading is untenable.

### 2.2 The convention adopted in this file
1. **Frames are real (SU(N)) and are chosen only for real configurations.** AP, UQ, the identification clause and every
   frame-patching statement (§1, §4.3-§4.5, §5) are about **real** data and **real** configurations.
2. **Complex configurations occur only as complex perturbations of a real critical configuration Z^r = Z(V^r), written in
   fixed real frames of Z^r** (complexified log coordinates y_□ + δy_□, δy_□ complex; transitions between the fixed frames are
   the fixed real ones of Z^r). No frame is ever chosen as a function of a complex configuration, and no complex gauge acts.
3. **Complex data** e^zV^r (|z|_∞ ≤ r_ℂε): existence by the NK iteration of §4.2 run in the fixed real frames of Z^r from
   U_0 := Z^r; every iterate is holomorphic in z (fixed frames, holomorphic local operators), so the limit Z(e^zV^r) is
   holomorphic in z (uniform limit). **Complex uniqueness is not claimed** (it would be modulo complexified root-trivial gauges;
   F7's U is 1^h with h root-trivial in SL(2, ℂ), consistent with that reading). No consumer found in REVIEW_S22's "Who needs which
   part" uses uniqueness at complex data; BFT-2 needs holomorphy, which the construction gives directly.
4. **E_k^br at complex data** is E(z) := 𝔉_k(Z(e^zV^r); e^zV^r), holomorphic in z. It is independent of all choices (frames,
   cutoffs, starting point): for real z ∈ su(N)^{links} small, the iteration stays real, its limit is a real critical point in
   the real frame-local ball, hence (real UQ, §4.4) gauge-equivalent to the real Z(e^zV^r), so E(z) equals the real value; two
   holomorphic functions of z agreeing on a real neighbourhood of 0 agree on the connected complex polydisc (identity theorem).
5. **Why F7's configuration does not contradict this convention.** For V = 1, Z^r = 1 and the NK continuation at z = 0 is 1
   itself; F7's U is another complex critical point near 1, which the convention neither excludes nor needs to.

## §3. A parametrix defined on source representations, with an explicit error representation (repairs Codex F6, F9)

### 3.1 Representations, pairings, norms
- **Covariant representations at U.** Rep := {S = (G_0, s, j)}: G_0 on level-0 plaquettes (left-trivialised at base(P)), s_l on
  level-(l+1) links (at the root endpoint where ρ_l is covariant), j_l on level-l links (at the tail) — su(N)⊗ℂ-valued. The
  **pairing** with left-trivialised tangent vectors v (U ↦ e^{tv}U):
  **π_U(S)(v) := Σ_P⟨G_0(P), D log U_P[v]⟩ + Σ_{l,c}⟨s_l(c), Dρ_l(U)(c)[v]⟩ + Σ_{l,b}⟨j_l(b), v_l(b)⟩**
  (log U_P the based holonomy; ρ_l the soft fluctuation, NSL55 Lemma D). Exact covariance: π_{U^g}(Ad_gS)(Ad_gv) = π_U(S)(v).
  So a representation is frame-free; its slots rotate by Ad under gauges, with no correction term.
- **Flat representations in a frame.** In frame log coordinates y (U^ĝ = e^y) a flat representation S′ pairs with log-tangent
  vectors δy by **π^{fl}(S′)(δy) := ⟨G_0′, dδy_0⟩ + Σ_l⟨s_l′, r_l(δy)⟩ + Σ_l⟨j_l′, δy_l⟩** (flat d, linear residual) — the pairing of
  KFACTOR_OFF55's N^{(σ)}, independent of y.
- **Norms (fixed real frames ĝ_□ of a reference real configuration; §4 fixes them).** For covariant S:
  **N_𝔇(S) := max_□N^{(σ)}_{Ω_□}(Ad_{ĝ_□}S)** (KFACTOR_OFF55's functional on the rotated slots, pointwise Hölder seminorm on G_0,
  restricted to Ω_□). For tangent vectors: **‖v‖_𝔇 := max_□‖J_{y_□}^{−1}Ad_{ĝ_□}v‖_{(σ),Ω_□}** — measured in **log coordinates**
  (homogeneous data). *Why log coordinates:* the left-trivialised components of v have the wrong residual: for direction-constant
  y, v one finds r_l(J_yδ) − r_l(δ) = ½(Q_l[y_l, δ_l] − [y_{l+1}, δ_{l+1}]) + … ≈ ½(L − L²)[y_μ, δ_μ] (Q maps constants to L×), own
  size ≍ h_l²η‖δ‖, i.e. **σ-weight L^{σq}** (q = k − 1 − l): unbounded. In log coordinates the residual is the linearised covariant
  fluctuation up to DΔ (Lemma C′), which is bounded. So every tangent norm below is a log-coordinate norm; J_y appears only inside
  compositions J^{−1}_{y′}Ad J_y = D(gauge action), whose σ-boundedness follows from the covariance of ρ (Lemma D′).
- **Frame changes cost 1 + O(η).** On Ω_□ ∩ Ω_□′ the fixed frames of the reference configuration differ by t = c·e^{τ} with c
  constant and ‖τ‖_♮ − ‖τ‖_∞ ≤ C_RGη (Lemma RG′, unrooted). Sup slots and J are Ad-invariant; the pointwise Hölder seminorm of a
  rotated G_0 changes by ≤ 2‖∇^cτ‖_∞‖G^c_0‖_∞. So the two frames' N^{(σ)} agree within a factor 1 + 2C_RGη. For log-tangent
  vectors the change of frame is the differential of the gauge action at y, D(x ↦ x^t)(y): its potential legs are controlled by
  Lemma B (B2) (Lipschitz in x), its residual legs by Lemma D′ with ξ = ξ′: factor ≤ 3 + Cη on residual legs **of differences**
  — so frame changes of tangent vectors cost a fixed factor C_t (≤ 4), not 1 + O(η). This is harmless: ‖·‖_𝔇 is a maximum
  over frames and every bound below is proved frame by frame.

### 3.2 Three explicit representation maps (CONV′, SC-cut, base change) — PROVEN-HERE
Throughout: real frame coordinates y on Ω with ‖y‖_{(σ),Ω} ≤ η ≤ η_C (or complex y in the fixed-frame complex ball of §2),
representations supported inside Ω^{−3}; h_l = L^{−(q+1)}, q = k − 1 − l; own sizes |s_l| ≤ L^{−(2+σ)q}‖s‖_{R(σ)},
|G_0| = n^{−2}|G^c_0|, |y_l| ≤ h_lη, |r_l(y)| ≤ L^{−(2+σ)q}η.
**(a) CONV′ (covariant → flat).** Φ_y(S) := (AdG_0, Ads + s^Δ, Adj + j^q + j^Δ) with
j^q := (Dq(y))^T(AdG_0) (q_P(y) := log of the frame holonomy of P minus dy_0(P), the BCH remainder of four links),
s^Δ := (∂_wβ)^T(Ads), j^Δ := (Dâ + ∂_Xβ·DX_0)^T(Ads) (Lemma C′'s decomposition Δ = â + β(X_0, ŵ)). Then
**π^{fl}(Φ_y(S))(δy) = π_U(S)(Ad^{−1}J_yδy) exactly, and N^{(σ)}(Φ_y(S) − AdS) ≤ C_CVη·N^{(σ)}(AdS).**
*Proof.* Exactness: D log U_P[J_yδy] in the frame is DF_P(y)[δy] = dδy_0(P) + Dq_P(y)[δy]; Dρ_l(U)[J_yδy] in the frame is
Dρ_l(y)[δy] = r_l(δy) + DΔ_l(y)[δy] (ρ covariant, r linear). Sizes: q_P is a convergent BCH series of degree ≥ 2 in four link
variables, so |∂q_P/∂y(b)| ≤ C|y_0| ≤ Cη/n and π_0(j^q) ≤ n³·2(d − 1)·Cη n^{−1}·n^{−2}|G^c_0| = Cη‖G^c_0‖_∞. |∂_wβ| ≤ C|X_0| ≤
Ch_lη, so ‖s^Δ‖_{R(σ)} ≤ Cη‖s‖. j^Δ: |∂â/∂y(a)| ≤ Ch_l²η per contour link (â is a centred series of degree ≥ 2 in variables of
own size h_lη), |∂_Xβ| ≤ C|ŵ| ≤ C(|r_l(y)| + h_l³η²); with ≤ p_L links per contour and ≤ c_col contours per link,
π_l(j^Δ_l) ≤ L^{3(q+1)}C p_Lc_col(h_l²η + L^{−(2+σ)q}η)L^{−(2+σ)q}‖s‖ ≤ CL³η‖s‖(L^{−(1+σ)q} + L^{−(1+2σ)q}), and the level-(l+1)
part (through y_{l+1} in ŵ) likewise; Σ_q is finite for σ > 0. ∎ Φ_y is invertible with the same bound (solve for the slots).
**(b) SC-cut (physical cutoff vs slot cutoff).** For a flat S′ and a cutoff ψ of coarse scale ℓ ≥ 1 (Convention C):
**ψ·π^{fl}(S′) = π^{fl}(M_ψS′ + K^♯_ψS′)**, where (ψ·f)(δy) := f(ψδy), M_ψ multiplies slots at their positions, and
K^♯_ψS′ := (0, 0, [d, ψ]^TG_0′ + Σ_l[Q_l, ψ]^Ts_l′) with [d, ψ]δy(P) := Σ_{b∈∂P}ε_{P,b}(ψ(m_b) − ψ(m_P))δy(b),
[Q_l, ψ]δy(c) := Σ_aw_{c,a}(ψ(m_a) − ψ(m_c))δy(a). **N^{(σ)}(K^♯_ψS′) ≤ (C_SC/ℓ)N^{(σ)}(S′)**, C_SC := d + c_colδ_*L²/(1 − L^{−σ}).
*Proof.* d(ψδy) = ψ(m_P)dδy + [d, ψ]δy and r_l(ψδy) = ψ(m_c)r_l(δy) + [Q_l, ψ]δy_l (WM^σ's identity; Codex BFT4W W4). Sizes:
|ψ(m_b) − ψ(m_P)| ≤ 1/(2nℓ), so π_0([d, ψ]^TG′_0) ≤ n³·2(d − 1)·n^{−2}|G^c|/(2nℓ) ≤ d‖G^c‖/ℓ; the residual commutator is WC^σ's
j^S count with r(u) replaced by s: π_l ≤ c_colδ_*L²L^{−σq}‖s‖/ℓ. ∎
**(c) Base change and chart maps.** For U′ = e^{v}U (v small) there is an explicit linear ℬ_{U→U′} : Rep → Rep with
π_{U′}(ℬS) = π_U(S) and N_𝔇(ℬS − S) ≤ C_B‖v‖_𝔇N_𝔇(S); and for the chart term of §3.4 an explicit 𝒥_y[w] with
π^{fl}(𝒥_y[w]S′) = (DJ_y[w])^T(π-form of S′) and N^{(σ)}(𝒥_y[w]S′) ≤ C_J‖w‖N^{(σ)}(S′).
*Proof.* Both covectors are of the form δ ↦ π(S)(B(w, δ)) with B linkwise bilinear (second derivatives of log U_P, of ρ_l and of
the exponential chart), own size ≤ C|w||δ|. As covectors in δ: the G-slot gives plain level-0 currents of own size
≤ C|G_0||w_0| ⇒ π_0 ≤ C‖G^c‖‖w‖; the s-slot gives ⟨s, r_l(B)⟩ + ⟨s, DΔ[B]⟩, i.e. plain currents at levels l, l + 1 of own size
≤ C|s_l||w_l| ⇒ π_l ≤ Cp_LL²L^{−σq}‖s‖‖w‖ (summable) plus a residual-slot correction ≤ Ch_lη|s|; the j-slot gives ⟨j, B(w, ·)⟩ with
π_l ≤ h_l‖w‖π_l(j). (As *sources* these bilinear residual terms are harmless; only as *tangent residuals* would they carry
L^{σq}, cf. §3.1.) ∎

### 3.3 Lemma KC (CONV's G- and s-slots) and Lemma DKC (ND) — PROVEN-HERE
*The exact identity.* With the gauge action of §1.0, K_yλ(b) = d/dt log(e^{tλ(b^−)}e^{y(b)}e^{−tλ(b^+)}) =
ψ_−(ad_{y(b)})λ(b^−) − ψ_+(ad_{y(b)})λ(b^+) (KFACTOR_OFF55 CCP (c)); since ψ_− − ψ_+ = −z and λ(b^+) = λ(b^−) + (dλ)(b),
  **K_yλ(b) = −[y(b), λ(b^−)] − ψ_+(ad_{y(b)})(dλ)(b),  K′_yλ(b) = −[y(b), λ(b^−)] − (ψ_+(ad_{y(b)}) − 1)(dλ)(b)**  (K_0 = −Ξ),
and, differentiating in y along u,
  **DK_y[u]λ(b) = −[u(b), λ(b^−)] − Dψ_+(ad_{y(b)})[ad_{u(b)}](dλ)(b).**
Each is "a commutator with λ at the tail" plus "a linkwise operator applied to dλ". Transposing against a flat representation S
therefore produces **bare charges** plus **divergences of plain currents**, which is the structure HR (iii)-(v) prices.
**Lemma KC.** For real (or fixed-frame complex) y with ‖y‖_{(σ),Ω} ≤ η ≤ η_C and a flat S supported in Ω^{−3}:
  **J(P^T(K′^T_y π^{fl}(S))^⊥) ≤ C_KC·η·N^{(σ)}(S),**  C_KC depending only on (N, d, L, α, σ, κ_+), finite for σ > 0.
*Proof, slot by slot.* (G) For a plaquette P with base x and boundary links b_i (signs ε_i), write λ(b_i^−) = λ(x) + (sum of dλ
along ∂P from x to b_i^−, ≤ 2 links): (dK′_yλ)(P) = −[(dy_0)(P), λ(x)] + ⟨linear in dλ on ∂P⟩. Hence ⟨G_0, dK′_yλ⟩ =
⟨c_G, λ⟩ + ⟨w_G, dλ⟩ with **c_G(x) := Σ_{P: base P = x}[G_0(P), dy_0(P)]** (a level-0 bare charge, own size ≤ 2d²n^{−2}|G^c|·
n^{−2}‖∇^cy^c_0‖) and w_G a level-0 plain current of own size ≤ C|G_0||y_0| ≤ Cn^{−3}η|G^c| whose coarse field w^c_G = n³w_G has
pointwise Hölder seminorm ≤ C([G^c]^∞_α‖y^c_0‖ + ‖G^c‖[y^c_0]^∞_α) ≤ CηN(S) ([y^c]^∞_α ≤ d‖∇^cy^c‖ at separations ≤ 1). HR (v) at
level 0: J(P^Tc_G) ≤ (M_γ/(L − 1))n⁴·Cn^{−4}η‖G^c‖; HR (iv): J(P^Td*w_G) ≤ dM_γ[w^c_G]^∞_α/(L^α − 1). Both are Cη·N(S) with no
power of n. (The naive bound — c_G as an arbitrary charge of own size |G||y| — would cost n·η; the split is what removes n.)
(s) For a level-(l+1) link c with tail root c_X: Q_l(K′λ)_l(c) = −[(Q_ly_l)(c), λ(c_X)] + Σ_aw_{c,a}(−[y(a), λ(a^−) − λ(c_X)]
− (ψ_+ − 1)(dλ)(a)), and (K′λ)_{l+1}(c) = −[y_{l+1}(c), λ(c_X)] − (ψ_+ − 1)(dλ)(c). Since Q_ly_l − y_{l+1} = r_l(y):
⟨s_l(c), r_l(K′λ)(c)⟩ = ⟨[s_l(c), r_l(y)(c)], λ(c_X)⟩ + ⟨w_s, dλ⟩, with λ(a^−) − λ(c_X) a sum of dλ along the contour (≤ p_L
links). The bare charge has own size ≤ |s_l||r_l(y)| ≤ L^{−2(2+σ)q}η‖s‖; HR (v) at level l + 1: J ≤ (M_γ/(L − 1))L^{4q}·that =
(M_γ/(L − 1))L^{−2σq}η‖s‖. The current w_s has level-l own size ≤ Cp_L²|s_l||y_l| (π_l ≤ Cp_L²L²L^{−σq}η‖s‖) and a level-(l+1) part
of own size ≤ C|s_l||y_{l+1}|; HR (iii) costs (k − l)·2dM_γ·π: Σ_q(q + 1)L^{−σq} < ∞. (j) CCP (c):
J(P^T(K′^T_yj)^⊥) ≤ C_cc max_l‖y^c_l‖J(j). Sum: C_KC := C(1 + Σ_q(q + 1)L^{−σq}). ∎
**Lemma DKC (the non-criticality defect, Codex F9's "chart-coordinate ND").** For y as above, a log-tangent vector u on the local
torus and a flat representation S_a:  **J(P^T((DK_y[u])^Tπ^{fl}(S_a))^⊥) ≤ C_KC·‖u‖_{(σ)}·N^{(σ)}(S_a).**
*Proof.* Identical, with (y, ψ_+ − 1) replaced by (u, Dψ_+[ad_u]): the G-charge is [G_0(P), du_0(P)], the s-charge [s_l(c), r_l(u)(c)]
(|r_l(u)| ≤ L^{−(2+σ)q}‖u‖), the currents have own sizes C|G||u_0|, C|s||u_l|. ∎
*Remark.* KC is what OFFGLOB55 §4.3 called CONV's "G- and s-slots — ARGUED"; DKC is its (ND) in the chart form that Codex F9
requests ("including derivatives of dexp" — here entering only through Dψ_+, bounded on the fixed polydisc).

### 3.4 The parametrix and its exact error representation — Proposition PAR (PROVEN as an implication)
*Setting.* Fixed real frames ĝ_□ on Ω_□ (§4 says of what); U real, or complex in the fixed-frame ball (§2), with frame
coordinates y_□ := log U^{ĝ_□}, max_□‖y_□‖_{Ω_□} ≤ η; RW-cc geometry (R ≥ 24 even, product partition, χ_□ of scale ¼ with
supp ⊂ □^{(1)}, ψ_□ = 1 on □^{(R/2)} of scale R/4, φ_□ = 1 on □^{(R+1)} supported in Ω_□ of scale 1; local tori 𝕋_□ of side
4R + 22, root-preserving ι_□), Convention C throughout. Transplants ỹ_□ := ι_*(φ_□y_□) with datum ι_*(φ_□y_{□,k}).
*Inputs.* (P1) L1 on each 𝕋_□: 𝒦_ỹ := P_ccH^{log}_ỹ + Γ^TΓ is invertible on flat-cc sources with ‖𝒦_ỹ^{−1}‖ ≤ 2G_♯ and
Γ𝒦_ỹ^{−1} = 0, for ‖ỹ‖ ≤ r_lin (Codex OFFGLOB F5: CONFIRMED as an implication of the corrected full-ball K/GV estimates;
[S26-BANKED] conditional on the lane-A package). (P2) The aggregate source bounds on 𝕋_□ (Codex KOFF §5.3, banked): the
natural representation Y of Hx − ∇F(x; B) obeys N^{(σ)}(Y(x) − Y(x′)) ≤ K(η + η′ + s)‖x − x′‖, hence its derivative
ℋY_x[w] := D_xY(x)[w] obeys **N^{(σ)}(ℋY_x[w]) ≤ K(2‖x‖ + s)‖w‖**. (P3) WM^σ, WC^σ (flat, Convention C; Codex BFT4W W3-W4,
banked PROVEN). (P4) Covariant routing HR_U and exact cc localisation for a supplied representation (Codex OFFGLOB item 3, with
the corrected coefficient C_loc := 1 + 4d + 4dM_γ/(L − 1) + (324√2/n)η_F + 2592η_ρ at ℓ_χ = ¼). (P5) §1 (RG′), §3.2, §3.3.
*Definition* (linear in S; defined on representations, not on source vectors — this is the repair of F6). For S ∈ Rep with
π_U(S) ∈ cc_U:
  f_□ := P^U_cc(M_{χ_□}S)  (covariant, exactly cc_U, N_𝔇(f_□) ≤ C_loc N_𝔇(S));
  f̂_□ := Φ_{y_□}(Ad_{ĝ_□}f_□)  (flat, K_y-annihilating);   p̂_□ := P_cc f̂_□ := f̂_□ − (0, 0, P^TD^⊥π^{fl}f̂_□)  (flat-cc);
  u_□ := 𝒦_{ỹ_□}^{−1}ι_{□*}p̂_□;   **𝒫_US := Σ_□Ad^{−1}_{ĝ_□}J_{y_□}(ψ_□ι^*_□u_□).**
*Proposition PAR.* Let S_G be **any** representation of G(U) := ∇𝔉_k(U; V) (π_U(S_G) = G(U)). Then, exactly,
  **DG(U)𝒫_US = π_U(S) − π_U(ℰ_U[S; S_G]),  ℰ_U[S; S_G] := −Σ_□Ad^{−1}_{ĝ_□}Φ^{−1}_{y_□}(e_□),**
  **e_□ := M_ψg_□ + C^♯_ψ(u_□) + M_ψℋY_ỹ[u_□] + K^♯_ψℋY_ỹ[u_□] − ℋY_ỹ[ψu_□] − 𝒥_y[ψu_□](Φ_yAd_{ĝ}S_G)**  (ψ = ψ_□, y = y_□),
where g_□ := H^{log}_ỹu_□ − f̂_□ is a **plain chain** (no G- or s-slot) and C^♯_ψ is WC^σ's representation. Moreover, for
R ≥ 24, η ≤ η_P (and r_lin's hypothesis), with constants depending only on (N, d, L, κ_±, α, θ, σ) and the input constants:
  **‖𝒫_US‖_𝔇 ≤ βN_𝔇(S),  N_𝔇(ℰ_U[S; S_G]) ≤ C_E(1/R + η + N_𝔇(S_G))N_𝔇(S).**
*Proof.* (i) *f_□ is cc_U and the pieces add up.* HR_U (i): D^⊥_U(P^U_ccX) = 0 for every X; Σ_□M_{χ_□}S = S slotwise, so
Σ_□π_U(f_□) = π_U(S) − P^T_UD^⊥_Uπ_U(S) = π_U(S) because π_U(S) ∈ cc_U. (ii) *K_ỹ^Tf̂ = 0 on 𝕋_□.* f_□ annihilates Ξ_Uλ for
λ ∈ Λ_*; in frame log coordinates Ξ_U ↔ K_y; transplanting, a test function λ′ ∈ Λ_*(𝕋_□) is replaced by φ′·ι^*λ′, which vanishes
at the global roots (ι maps roots to roots), and f̂ reads only where φ = 1. So D^⊥π^{fl}f̂ = (K′^T_ỹπ^{fl}f̂)^⊥ and, by KC,
N^{(σ)}(p̂ − f̂) ≤ C_KCηN^{(σ)}(f̂). (iii) *The local equation and the defect g.* L1: Γu = 0 and P_ccH^{log}_ỹu = p̂, so P_ccg = 0,
i.e. g = P^TD^⊥g: a plain chain. The derivative of the Ward identity ⟨K_xλ, ∇F(x)⟩ ≡ 0 gives K^T_ỹH^{log}_ỹu = −(DK_ỹ[u])^Ta,
a := ∇F_□(ỹ) (the local gradient on 𝕋_□); with K^T_ỹf̂ = 0 and K = −Ξ + K′: **D^⊥g = (K′^T_ỹg + (DK_ỹ[u])^Ta)^⊥** (Codex F9's
sign), so (1 − P^T(K′^T_ỹ·)^⊥)g = P^T((DK_ỹ[u])^Ta)^⊥ and, by CCP (c) on the plain chain g and Lemma DKC,
J(g) ≤ (1 − C_ccη)^{−1}C_KC‖u‖N^{(σ)}(S_a) for any flat representation S_a of a. Choose S_a by splitting a = ψ′·a + (1 − ψ′)·a
(ψ′ = 1 on supp ψ + 5, supported where φ = 1): ψ′·a is the frame form of ψ′·G(U), represented by M_{ψ′}Φ_yAdS_G + K^♯_{ψ′}(…)
(SC-cut), of norm ≤ C N_𝔇(S_G); (1 − ψ′)·a is represented through the natural representation of ∇F(ỹ) = Hỹ − NB̃ − (Y − …),
of norm ≤ Cη (P2). So **J(g) ≤ C(N_𝔇(S_G) + η)‖u‖.** (iv) *The pulled-back identity.* Differentiating ∇F_□(y) = J^T_yAd G(U)
gives J^T_yAd DG(U)[Ad^{−1}J_yw] = H^{log}_yw − (DJ_y[w])^TAd G(U). With w = ψu, H^{log} = H − D_xY, H(ψu) = ψ·Hu + C_ψ(u) and
H^{log}_yu = f̂ + g on supp ψ (finite range: H^{log}_y = H^{log}_ỹ there):
  pull-back of DG(U)(piece_□) = f̂ + ψ·g + [ψ·D_xY(y)[u] − D_xY(y)[ψu]] + C_ψ(u) − (DJ_y[ψu])^TAdG(U),
using ψ·f̂ = f̂ (f̂ reads only where ψ = 1). Each term has the representation listed in e_□ (ψ·g = π^{fl}(M_ψg) for a plain chain;
SC-cut for ψ·D_xY[u]; WC^σ for C_ψ; §3.2 (c) for the chart term). Push forward with Ad^{−1}Φ^{−1}_y (CONV′, exact) and sum with (i).
(v) *Bounds.* ‖u_□‖ ≤ 2G_♯(1 + C_KCη)(1 + C_CVη)C_locN_𝔇(S) (L1, KC, CONV′, P4); ‖ψu‖ ≤ C^σ_M(R/4)‖u‖ ≤ C^σ_M(1)‖u‖ (WM^σ);
N(C^♯_ψ(u)) ≤ (4C^σ_c/R)‖u‖ (WC^σ at scale R/4); N(ℋY_ỹ[·]) ≤ K(2C^σ_M(1)η + 6η)‖·‖ (P2, ‖ỹ‖ ≤ C^σ_M(1)η, datum ≤ 6η); K^♯_ψ costs
4C_SC/R; 𝒥 costs C_J‖ψu‖N(S_G); (iii) for g. Each e_□ is supported in Ω_□ and each Ω_□′ meets ≤ n_R := 6^d of them; frame changes
cost 1 + 2C_RGη on representations and a fixed factor C_t on tangent vectors (§3.1). Collecting: β := n_RC_tC^σ_M(1)·
2G_♯(1 + C_KCη)(1 + C_CVη)C_loc and C_E := n_R(1 + 2C_RGη)(1 + C_CVη)·C·2G_♯C_loc(4C^σ_c + 4C_SC + K + C_J + C_KC). **No constant
depends on R** (WM^σ and WC^σ improve with R; the commutator gives the 1/R). ∎

### 3.5 Corollary GP′ (the bounded compatible error operator; exact right inverse and (N1-nd) at a real critical point) — PROVEN as an implication
Let Z be real and critical (G(Z) = 0) with fixed-frame size ≤ η, and put Rep_cc(Z) := {S ∈ Rep : π_Z(S) ∈ cc_Z}, normed by N_𝔇.
Take S_G := 0 in PAR and write ℰ_Z := ℰ_Z[·; 0].
- **ℰ_Z is a linear endomorphism of Rep_cc(Z)**: π_Z(ℰ_ZS) = π_Z(S) − DG(Z)𝒫_ZS, and DG(Z) maps into cc_Z at a critical point
  (D^⊥_Z(DG(Z)w) = −((DΞ_Z[w])^TG(Z))^⊥ = 0 — the aggregate Ward identity of Codex F9).
- **N_𝔇(ℰ_ZS) ≤ C_E(1/R + η)N_𝔇(S) ≤ ½N_𝔇(S)** for R ≥ 4C_E and η ≤ 1/(4C_E).
- Hence **R_Z := 𝒫_ZΣ_{m≥0}ℰ_Z^m** obeys **DG(Z)R_ZS = π_Z(S)** (telescoping: DG(Z)𝒫_Zℰ^m_ZS = π_Z(ℰ^m_ZS) − π_Z(ℰ^{m+1}_ZS)) and
  **‖R_ZS‖_𝔇 ≤ 2βN_𝔇(S)** for every S ∈ Rep_cc(Z), uniformly in k and T.
- Every f ∈ cc_Z has a representation (e.g. the plain one, (0, 0, f)), so Ran H_Z ⊇ cc_Z; H_Z is symmetric at a critical point and
  Ran Ξ_Z ⊆ Ker H_Z, so **Ker H_Z = Ann(cc_Z) = Ran Ξ_Z: (N1-nd) at Z** (Codex F9: the finite-dimensional deduction CONFIRMED).
This is the object Codex OFFGLOB banked only "once a genuine bounded compatible error operator has been constructed": ℰ_Z is
constructed, linear, defined on the representation space, and bounded there. The bound for a **given** physical source is in
terms of the norm of the representation supplied with it — the honest form of BFT-5 (b) at m = 0 off 𝒞_glob (frame-local σ-pair).

## §4. Theorem OFF′ — BFT-0/1/2 off 𝒞_glob, repaired (real uniqueness via relative patching; complex data by continuation)

### 4.1 Statement
Fix d = 4, N ≥ 2, odd L ≥ 3, κ_±, 0 < α < θ ≤ σ ≤ 1 (θ₀ as in GV55), Convention C, Γ = Λ (S_E) on local tori. Cores are
K_□ := □^{(R/2−6)} (side ≥ 2R − 12; consecutive cores overlap in slabs of width R − 12); Lemma FP's proof applies verbatim to
**any** box Ω of side ≤ R′ = 4R + 5 covered by the cores meeting it (≤ 6 per coordinate, slab aspect ≤ 8d for R ≥ 48), and to the
depth-change geometry of §4.3 (boxes of side R′/L covering a box of side R′, ≤ 2L + 2 per coordinate), with constants C_FP and
C_FP(L). **𝔇_k(R, η)** := real configurations with a frame of size ≤ η on every box of side ≤ R′ (OFFGLOB55 §1.7).
> **Theorem OFF′.** There are R (even, ≥ 48), ε_*, C_0, r_u, r_ℂ > 0 depending only on (N, L, κ_±, α, θ, σ) and the constants of
> the inputs in §4.7 — **not on k or T** — such that for every k ≥ 1, every coarse torus T ≥ T_* := 4R + 6 and every V = e^zV^r
> with V^r ∈ 𝔅_k(ε) real, ε ≤ ε_*, |z|_∞ ≤ r_ℂε:
> - **(i) real existence and a priori bound.** For z = 0, 𝔉_k(·; V^r) has a real critical point Z(V^r) ∈ 𝔇_k(R, C_0ε).
> - **(ii) real uniqueness.** Every real critical point Z′ ∈ 𝔇_k(R, r_u) of 𝔉_k(·; V^r) is Z(V^r)^h for a composite gauge h trivial
>   at level k (in particular Z′ ∈ 𝔇_k(R, C_0ε)).
> - **(iii) BFT-1** in every frame: own plaquette logs of Z_j ≤ L^{−2(k−j)}(2C_0ε + 9C_0²ε²), own soft fluctuations ≤
>   L^{−(2+σ)(k−1−j)}C_0ε + C_ρL^{−3(k−j)}C_0²ε² (gauge-invariant quantities; Hölder form within blocks).
> - **(iv) complex data, BFT-2.** In fixed real frames of Z(V^r), the iteration of §4.2 started at Z(V^r) with data e^zV^r converges
>   to a complex critical point Z(e^zV^r), holomorphic in z, with fixed-frame size ≤ 2C_0ε; E(z) := 𝔉_k(Z(e^zV^r); e^zV^r) is
>   holomorphic in z and equals the real composite value at real z (§2.2 item 4). No complex uniqueness is asserted.
> - **(v) BFT-5 (b) at m = 0** at Z(V^r): Corollary GP′ (exact right inverse on representations; (N1-nd)).

### 4.2 Proposition NK′ (Newton–Kantorovich carried on representations) — PROVEN as an implication
*Setting.* Fixed real frames ĝ_□ of a real U_0 with max_□‖log U_0^{ĝ_□}‖ ≤ η_0; S_0 ∈ Rep with π_{U_0}(S_0) = G(U_0) and
N_𝔇(S_0) ≤ ν_0. *Iteration:* v_n := 𝒫_{U_n}S_n, U_{n+1} := e^{−v_n}U_n,
  **S_{n+1} := ℬ_{U_n→U_{n+1}}(ℰ_{U_n}[S_n; S_n]) + T^{rep}_n,**
with T^{rep}_n the representation of the Taylor remainder T_n := G(U_{n+1}) − G(U_n) + DG(U_n)v_n given by the lemma below.
*Invariant:* π_{U_n}(S_n) = G(U_n) for all n (induction: G(U_{n+1}) = π_{U_n}(S_n) − DG(U_n)v_n + T_n = π_{U_n}(ℰ[S_n; S_n]) + T_n by
PAR, = π_{U_{n+1}}(S_{n+1}) by the definition of ℬ and T^{rep}).
*Lemma T (Taylor remainder on representations).* Let S^{nat}(U) be the natural covariant representation of G(U) —
G_0(P) = ∇w(log U_P) (exact: S_W = Σ_Pw(log U_P)); soft: s_l(c) = κ_l∂_ρφ̂_c and the plain parts κ_l(∂_Gφ̂_c)∘DG_c (Lemma SG's
factorisation, covariant form). With U_t := e^{−tv}U and X(t) := ℬ_{U_t→U_1}S^{nat}(U_t),
T = π_{U_1}(∫_0^1(1 − t)X″(t)dt) =: π_{U_1}(T^{rep}), and **N_𝔇(T^{rep}) ≤ K_2‖v‖²_𝔇** for ‖v‖_𝔇 ≤ c_T.
*Proof.* π_{U_1}(X(t)) = G(U_t) for every t, so T = G(U_1) − G(U_0) − d/dt|_0G(U_t) = π_{U_1}(X(1) − X(0) − X′(0)), Taylor with
integral remainder. X is holomorphic in t on |t| ≤ c_T/‖v‖_𝔇 (in fixed frames U_t has complexified coordinates log(e^{−tAdv}e^{y}),
within the complex ball where (P2) holds), with N_𝔇(X(t)) ≤ C there (natural representations are O(η + s); ℬ bounded, §3.2 (c)).
Cauchy for Banach-valued holomorphic functions: N_𝔇(X″(t)) ≤ 2C‖v‖²/c_T² on [0, 1]. ∎
*Statement.* If C_E(1/R + 2η_0) ≤ ¼, C_2ν_0 ≤ ¼ with C_2 := (1 + C_Bβν_0)C_E + K_2β², and 2C_tβν_0 ≤ η_0, then
N_𝔇(S_{n+1}) ≤ ½N_𝔇(S_n), Σ_n‖v_n‖_𝔇 ≤ 2βν_0, every U_n has fixed-frame size ≤ 2η_0, and U_n → Z with **G(Z) = 0** and
d_𝔇(Z, U_0) ≤ 2C_tβν_0.
*Proof.* PAR with S_G = S_n: N(ℰ[S_n; S_n]) ≤ C_E(1/R + η_n + N(S_n))N(S_n); ℬ costs 1 + C_B‖v_n‖; Lemma T: K_2β²N(S_n)². Hence
N(S_{n+1}) ≤ [C_E(1/R + 2η_0) + C_2N(S_n)]N(S_n) ≤ ½N(S_n) inductively; ‖v_n‖ ≤ βN(S_n) ≤ β2^{−n}ν_0; fixed-frame coordinates move
by ≤ C_tΣ‖v_n‖. G(U_n) = π_{U_n}(S_n) → 0 and π_U is continuous in U. ∎
*What this repairs.* Codex F10: NK needs "compatible source representations, fixed or uniformly compared charts, and a controlled
domain for R_U". Here the representations are carried explicitly (S_n), the charts are the fixed real frames of U_0, and only the
parametrix 𝒫 (never an inverse on an abstract source space) is applied; convergence is linear (rate ½), which suffices.

### 4.3 The starting point: depth induction (Lemma U0; Codex OFFGLOB F10 "one-level lift CONFIRMED")
*Base k = 1.* U_0 := U^{(0)}(V) (exact lift: interior links 1, crossing links V_c). In the block-constant extension of an AX data
frame (OFFGLOB55 Lemma C2, Codex-confirmed) every box of side ≤ R′ has a frame of size ≤ C(L)·3(R′ − 1)ε (sup ≤ Lα, gradient
≤ L²α, Hölder ≤ 2L^{2+α}α, residual 0 since every S4′ contour crosses one block boundary). G(U_0) has the natural representation
G_0(P) = ∇w(log V_P) at block-corner plaquettes only (soft gradient 0: ρ ≡ 0), N_𝔇 ≤ C(L)ε.
*Step k ≥ 2.* Hypothesis H(k − 1): Theorem OFF′ (i) at depth k − 1 on the torus of side TL ≥ T_* for the datum V_0 := U^{(0)}(V)
(V_0 ∈ 𝔅_{k−1}(ε): corner plaquettes are V_P). Put **U_0 := (Z_{k−1}(V_0); V_0)** as a depth-k configuration.
- *Frames.* A depth-(k − 1) frame of size ≤ C_0ε on a box of side R′ (level-(k − 1) units) is a depth-k frame of the same box
  (side R′/L in level-k units) of size ≤ max(3L³C_0ε, ‖w‖_{T;v}) (NSL55 Lemma SC (b) with Codex NSL F3's repaired factor
  C_up ≤ 3L³), where w = the level-(k − 1) datum (now a potential level) and v = the level-k datum in that frame:
  ‖w‖_{T;v} ≤ 20L³‖w‖_D + ‖v‖_D ≤ 20L³·6C_0ε + p_L·6C_0ε (Lemma SC (c); M̄_c(V_0) = V_c exactly, so the level-k frame datum is an
  average of ≤ p_L frame links of V_0). Lemma FP in the depth-change geometry then gives frames of size ≤ **C_1ε, C_1 :=
  C_FP(L)·130L³C_0** on every box of side ≤ R′ (level k), provided (R′)²C_1ε ≤ c_FP.
- *Residual representation.* Levels < k − 1 of G(U_0) vanish (Z_{k−1}(V_0) is critical for 𝔉_{k−1}(·; V_0) and 𝔉_k splits as
  𝔉_{k−1}(x_{<k−1}; x_{k−1}) + κ_{k−1}Σ_cφ̂_c(M̄_c(x_{k−1}); V), BA-1); the new soft term is stationary at V_0 (ρ = 0, W_0 = V,
  G = 1: ∂_ρφ̂ = −Re tr(dρ) = 0, ∂_Gφ̂ = 0). What is left is the level-(k − 1) covector ∂_{x_{k−1}}𝔉_{k−1}(Z_{<k−1}; x_{k−1}) — the
  depth-(k − 1) top multiplier κ_{k−2}∂_Vφ̂, of own size ≤ κ_+|ρ_{k−2}|(1 + O(ε)) ≤ κ_+C_0ε(1 + O(ε)) — represented as a **plain
  current at level k − 1**: S_0 := (0, 0, j_{k−1}), π_{U_0}(S_0) = G(U_0) exactly, **N_𝔇(S_0) ≤ L³κ_+(1 + O(ε))C_0ε =: C_GC_0ε.**
*Existence at depth k.* NK′ with these frames, η_0 := C_1ε, ν_0 := C_GC_0ε: for ε ≤ ε_* the hypotheses hold and Z := lim U_n is
a real critical point (real data, real parametrix: every iterate is real) with fixed-frame size ≤ (C_1 + 2C_tβC_G C_0)ε ≤ r_u.
Proposition AP′ (next) resets its size to C_0ε, **which is what keeps the induction from accumulating** (C_0 does not depend on
C_1 or on k).

### 4.4 Proposition AP′ (a priori estimate, real) — PROVEN as an implication
*Statement.* Let Z be a real critical point of 𝔉_k(·; V^r), V^r ∈ 𝔅_k(ε) real, with Z ∈ 𝔇_k(R, r), r ≤ r_u. Then
**Z ∈ 𝔇_k(R, C_0ε), C_0 := 12C_FPG_♯C_A(R′ − 1)**, C_A := C^Y_M(1) + 4C_SC + c_N + 1.
*Proof.* (1) *Data-adapted frames.* On each Ω_□ choose an AX data frame g^{AX}_□ of V^r (OFFGLOB55 Lemma C2: data size
≤ 3(R′ − 1)ε) and root-match Z's frame to it (Lemma RM*, (R′)²r ≤ c_RM): a frame of Z on Ω_□^− of size ≤ C_RMr whose datum is the
AX datum, ‖y_k‖_D ≤ 3(R′ − 1)ε =: s_R/2. (2) *Local slice.* Transplant ỹ := ι_*(φ_□y) to 𝕋_□ (‖ỹ‖ ≤ C^σ_M(1)C_RMr ≤ r_N);
Theorem NSL (Codex NSL item 2, conditional) gives ξ ∈ Λ_*(𝕋_□), ‖ξ‖_♮ ≤ 2C_Λ‖ỹ‖, with ỹ^{e^ξ} ∈ S_E(𝕋_□). Since Λ reads x_0 within
coarse distance 3 and ι maps roots to roots, y^S := y^{e^ξ} is a frame of Z (root-matched to g^{AX}, same datum) on
□^{(R+1−3)} satisfying the S_E condition there, of size ≤ C_NC^σ_M(1)C_RMr. (3) *Local equation.* Criticality in the frame:
Hy^S = NB^S + 𝔑^0(y^S) = π^{fl}(Y^{nat}(y^S)) on vectors supported in that region (𝔑^0 := Hx − NB − ∇F). Let ψ^A := 1 on
□^{(R/2)}, supported in □^{(R−8)}, scale ≥ R/4 (R ≥ 32). As a configuration on 𝕋_□ with datum ψ^AB^S:
H(ψ^Ay^S) − N(ψ^AB^S) = π^{fl}(X_A),  X_A := M_{ψ^A}Y^{nat}(ỹ^S) + K^♯_{ψ^A}Y^{nat}(ỹ^S) + C^♯_{ψ^A}(y^S) + (the SC-cut commutator of
the data slot), so **N(X_A) ≤ C_A(c_Ns_R + K(C_NC^σ_M(1)C_RMr + s_R)²) + (4C^σ_c/R)C_NC^σ_M(1)C_RMr** (P2 on 𝕋_□ restricted —
restriction by a smooth cutoff costs C^Y_M — SC-cut, WC^σ at scale R/4). (4) *Slice defect.* Λ(ψ^Ay^S) = [Λ, ψ^A]y^S =: ν,
supported in (supp∇ψ^A)^{(3)}, ν ∈ Λ_*; Lemma OC (𝓛_Γ^{−1}Γ^Tν = −Ξν; Codex KOFF item 6, CONFIRMED) gives
ψ^Ay^S = 𝓛_Γ^{−1}[π^{fl}(X_A) + N(ψ^AB^S)] − Ξν, and the bracket is flat-cc (a Hessian image plus a data source). The banked
linear estimate (LIN^{(σ)} + GV-E on 𝕋_□, side 4R + 22 ≥ 5) bounds the response by G_♯(‖ψ^AB^S‖_D + N(X_A)). On K_□ = □^{(R/2−6)}
both ψ^A = 1 and every local quantity of Ξν vanishes, so **‖y^S‖_{(σ),K_□} ≤ G_♯[s_R + N(X_A)].** (5) *Patch.* Lemma FP (general box
form): Z has a frame of size ≤ C_FPG_♯[s_R + N(X_A)] on every box of side ≤ R′. (6) *Infimum.* Let r_* be the least r such that Z
has frames of size ≤ r on all boxes of side ≤ R′ (attained: frames range over a compact group, size is continuous). Steps (1)-(5)
applied to an optimal system give r_* ≤ A + θ_Ar_* + C_FPG_♯C_AK(C_NC^σ_M(1)C_RM)²r_*², A := C_FPG_♯(1 + C_Ac_N + C_AKs_R)s_R,
θ_A := C_FPG_♯·4C^σ_cC_NC^σ_M(1)C_RM/R. For R ≥ 8C_FPG_♯C^σ_cC_NC^σ_M(1)C_RM (θ_A ≤ ½) and r_u with the quadratic term ≤ ¼r_*:
r_* ≤ 4A ≤ C_0ε. ∎
*What is used.* NSL (banked conditional), OC, LIN^{(σ)} + GV-E (banked conditional), P2 aggregate bounds (banked conditional),
WC^σ, WM^σ (banked PROVEN), SC-cut, RM*, FP (§1, §3.2). **Not used: the parametrix, (R), any complex object.** This replaces
OFFGLOB55's Proposition AP (whose complex reading Codex F7 refuted, and whose "iterating (same frames)" E6 already withdrew).

### 4.5 Proposition UQ′ (real uniqueness modulo root-trivial gauges) — PROVEN as an implication. *Answers Codex F8.*
*Statement.* Let Z, Z′ be real critical points of 𝔉_k(·; V^r) (same real datum) in 𝔇_k(R, r_u). Then Z′ = Z^h for a composite
gauge h equal to 1 at every level-k root.
*Two auxiliary facts.* (N-Lip) For depth-k configurations x, x′ on a torus with ‖x‖, ‖x′‖ ≤ r_N, NSL's gauges obey
‖ξ(x) − ξ(x′)‖_♮ ≤ 4C_Λn_0(x − x′). *Proof:* ξ(x) = Ψ_x(ξ(x)) with Ψ_x(ξ) = −Λ(x_0) − Λ(R_0(x, ξ)) (NSL55 Lemma E);
‖Ψ_x(ξ) − Ψ_{x′}(ξ)‖_♮ ≤ C_Λ[n_0(x − x′) + K_G(‖u‖ + ‖β‖)n_0(x − x′)] ≤ 2C_Λn_0(x − x′) by Lemma A (c) and (B2) in the a-slot, and
Lip_ξΨ_x ≤ ½ on the ρ_N-ball; so ‖ξ(x) − ξ(x′)‖ ≤ 2·2C_Λn_0(x − x′). ∎ (S-Lip) The slice representatives then obey
‖x^{e^{ξ(x)}} − x′^{e^{ξ(x′)}}‖_{(σ)} ≤ C_SL‖x − x′‖_{(σ)} (potential legs: (B0) + (B2); residual legs: Lemma D′, with
sup|ξ − ξ′| ≤ ‖ξ − ξ′‖_♮).
*States.* An **admissible state** is a pair of frame systems ({ĝ_□}, {ĝ′_□}) of (Z, Z′) on the cores K_□ (all □) with (a) ĝ_□ = ĝ′_□
at every root of K_□, (b) both of size ≤ ρ_S on every core. Its defect is q := max_□‖y′_□ − y_□‖_{K_□} (by §1.6 the data parts
coincide, so q measures levels < k). ρ_S is fixed below.
*Nonempty.* By AP′, Z, Z′ ∈ 𝔇_k(R, C_0ε); on each core root-match both to the same AX data frame of V^r (Lemma RM*): sizes
≤ C_RMC_0ε ≤ ρ_S once ρ_S ≥ C_RMC_0ε.
*One step (the map Σ).* Given an admissible state: (1) patch both families to Ω_□ by Lemma FP with the same base roots and cutoffs:
by **Lemma RFP**, the patched frames are root-matched, of sizes ≤ C_FPρ_S, with coordinate difference ≤ C_RFPq. (2) Transplant both
to 𝕋_□ and apply NSL (Λ_*-gauges: root matching survives): sizes ≤ C_NC^σ_M(1)C_FPρ_S =: ρ_1 ≤ r_N, difference ≤ C_SLC^σ_M(1)C_RFPq.
(3) Local equation for the difference w := y′^S − y^S (same datum, both critical, both in the local S_E slice): Hw = π^{fl}(Y^{nat}(y′^S)
− Y^{nat}(y^S)) on the region, so, as in AP′ (3)-(4) with ψ^A and Lemma OC,
**‖w‖_{(σ),K_□} ≤ G_♯[C^Y_M(1)(1 + 4C_SC/R)K(2ρ_1 + s_R) + 4C^σ_c/R]·‖w‖_{(σ),□^{(R−8)}} =: θ_U‖w‖_{region}**
(the Lipschitz half of (P2) for the transplants, whose difference is φ_□·(y′^S − y^S)). (4) The same step for each configuration
separately (AP′ (3)-(4)) bounds the new core sizes by G_♯[s_R + C_A(c_Ns_R + K(ρ_1 + s_R)²) + (4C^σ_c/R)ρ_1] ≤ ρ_S when
ρ_S ≥ 4G_♯(1 + C_Ac_N)s_R and R, ρ_S as below. So Σ maps admissible states to admissible states (restrict the slice frames to the
cores) and **q(Σ(state)) ≤ θ_UC_SLC^σ_M(1)C_RFP·q(state) ≤ ½q(state)** for R ≥ 16G_♯C^σ_cC_SLC^σ_M(1)C_RFP and
G_♯C^Y_M(1)(1 + 4C_SC/R)K(2ρ_1 + s_R)C_SLC^σ_M(1)C_RFP ≤ ¼.
*Conclusion.* Let q_* := inf q over admissible states; the set is compact (products of SU(N) at finitely many sites, closed
conditions) and q is continuous, so q_* is attained, and q_* ≤ q_*/2 gives q_* = 0: an admissible state with y′_□ = y_□ on every
core, i.e. Z′^{ĝ′_□} = Z^{ĝ_□} on K_□ at every level, i.e. Z′ = Z^{h_□} on K_□ with h_□ := ĝ′^{−1}_□ĝ_□, equal to 1 at the roots of
K_□. On K_□ ∩ K_□′ (connected, containing roots) h_□h_□′^{−1} fixes Z and equals 1 at a root; a gauge fixing a configuration is
determined along links (g(x′) = U_b^{−1}g(x)U_b), so it is 1 on the overlap. The h_□ glue to one level-0 gauge h, 1 at every root,
with Z′ = Z^h at every level. ∎
*Why this is the estimate F8 asked for.* The relative estimate "max_□‖y′_□ − y_□‖_Ω ≤ C_rel max_□‖y′_□ − y_□‖_core" is Lemma RFP,
for **matched, root-fixed** frames, with C_rel = C_RFP independent of R; the gauge-alignment cost proportional to ‖Z′ − Z‖ is
RFP's ‖Δτ‖_♮ ≤ C′q (zero at every root of every overlap). The infimum is over states that the step maps into themselves (sizes
reset by (4)), which is the admissibility Codex F10 asks of E6's repair. NSL is never used to *prove* that the two configurations
lie on one orbit — only to put each into its own local slice, after which the orbit comparison is the q-contraction.

### 4.6 Complex data (BFT-2) and BFT-1 — PROVEN as an implication
*Complex data.* Fix V^r and Z^r := Z(V^r) with real frames of size ≤ C_0ε (AP′). With data e^zV^r, G(Z^r; e^zV^r) is supported on
the top soft terms; in a real frame z is rotated isometrically, and the top multiplier's representation (a level-(k − 1) plain
current plus a top residual slot) has N_𝔇 ≤ C_zr_ℂε. Run NK′ in the **fixed** real frames of Z^r, all ingredients complexified:
L1 holds on a complex polydisc (Codex KOFF §4.3, "Complexification gives the same assertion on a smaller complex polydisc");
Φ_y, KC, DKC, ℬ, 𝒥 and Lemma T are analytic/linear in the complex coordinates; covariant routing with complex transports costs
|Ad(e^{y})| ≤ e^{2|Im y|} per link, and along a hierarchical routing path Σ_j(own |Im y_j|) ≤ Σ_jL^{−(k−j)}·C r_ℂε ≤ Cr_ℂε, so C_loc
acquires a factor e^{Cr_ℂε}; every frame stays fixed and real. For r_ℂε ≤ ν_0 the iteration converges; each iterate is holomorphic in
z, the convergence is uniform, so **Z(e^zV^r) and E(z) := 𝔉_k(Z(e^zV^r); e^zV^r) are holomorphic** on |z|_∞ < r_ℂε, with fixed-frame
size ≤ C_0ε + 2C_tβC_zr_ℂε ≤ 2C_0ε. At real z the iteration is real and its limit is, by UQ′, gauge-equivalent to Z(e^zV^r) — so
E(z) is the real composite value there, and by the identity theorem E is the unique holomorphic continuation (§2.2 item 4).
*BFT-1.* In every frame of size ≤ C_0ε (real) or fixed-frame size ≤ 2C_0ε (complex): BA-3 (REVIEW_BFT_A_S1, CONFIRMED) and the
banked σ-ball bounds (KFACTOR_OFF55 §1.4 (1a)-(1b) with Codex KOFF §4.3 (1)) give the gauge-invariant per-level bounds of §4.1 (iii);
their Hölder forms within blocks are read off the frame norm. Real frames are unitary, so the plaquette spectra and |ρ| are
frame-independent; for complex configurations the bounds are stated in the fixed real frames (as BFT-2's "BFT-1 holds there").

### 4.7 Every input of Theorem OFF′, with its status
| # | Input | Where | Status |
|---|---|---|---|
| 1 | Lemma AX at level k / data frames (OFFGLOB55 Lemma C2) | PROOF "Lemma AX"; OFFGLOB55 §1.3 | Codex OFFGLOB item 1: PROVEN (banked class inclusions) |
| 2 | Lemma U0 (exact one-level lift) | PROOF "Lemma U0 (the exact lift)" | CONFIRMED (REVIEW_S20); Codex OFFGLOB F10/item 5 |
| 3 | K^{(σ)} chain on local tori: aggregate source bounds (P2), CCP (c), HR (i)-(v), LIN^{(σ)}, TOP♯ | KFACTOR_OFF55; Codex KOFF items 1-5 | [S26-BANKED], conditional on the lane-A linear package |
| 4 | GV-E (gauge-variant half), corrected contraction | GV55; Codex GV items 2-4 | [S26-BANKED] |
| 5 | L1 (𝒦_y invertible on the full ball, complexified) | OFFGLOB55 §4.1 | Codex OFFGLOB F5/item 4: CONDITIONAL on 3-4 |
| 6 | Theorem NSL (real, scaled norm) | NSL55 §2-§3 | [S26-BANKED] conditional (Codex NSL item 2) on the elliptic input EP-bd |
| 7 | Lemma OC | KFACTOR_OFF55 §3.1 | Codex KOFF item 6: CONFIRMED (algebra) |
| 8 | WM^σ, WC^σ (Convention C) | BFT4W55 §4 | [S26-BANKED] PROVEN (Codex BFT4W W3-W4) |
| 9 | Covariant routing, exact cc localisation for a supplied representation, coefficient C_loc | OFFGLOB55 §3.2-§3.4 | Codex OFFGLOB items 3 (with F4's coefficient) |
| 10 | NSL55 Lemmas A (d), B, C, D (algebra and bounds) | NSL55 §3.1-§3.5 | Codex NSL F6: CONFIRMED (conditional only through Lemma A (c), unused in §1) |
| 11 | Lemmas RG′, RM, RM*, MG, FP, C′, D′, RFP | §1 | PROVEN-HERE |
| 12 | CONV′ (a), SC-cut (b), ℬ and 𝒥 (c); KC, DKC | §3.2-§3.3 | PROVEN-HERE |
| 13 | PAR, GP′, NK′ with Lemma T, AP′, UQ′ | §3.4-§4.5 | PROVEN as implications of 1-12 |
**Status of Theorem OFF′: PROVEN as an implication of inputs 1-10 (banked or Codex-confirmed, several conditional on the lane-A
linear package and on NSL's elliptic input) and of this file's §1-§4 (not yet Codex-checked).** Premise (R) is **not** an input:
every analytic bound used is either an aggregate bound on a local torus (P2, LIN, GV-E), a per-plaquette/per-contour analytic fact
already banked (local analytic completion, Codex KOFF §4.3), or an explicit power count proved here. No alignment, no (UHL-fine),
no (SL-cov), no smooth lift, no lane-B (N1). *Not delivered by OFF′:* complex uniqueness (no consumer found); boxes and T < T_*
(§8); BFT-3, BFT-4, the identification clause (§5-§7).

**Erratum E2 (to §3.2 (a), §3.1, §4.4, §4.7; found on re-reading; conclusions unchanged).**
(i) §3.2 (a), j^Δ: a single link a enters â(c) through the contours containing it, so |∂â(c)/∂Y(a)| ≤ Cw_{c,a}p_Lh_lη (not h_l²η:
the centring cancels only in the *value* of the averaged quadratic, not in a single-link derivative). Then
π_l(j^Δ) ≤ L^{3(q+1)}·Cc_colp_Lh_lη·L^{−(2+σ)q}‖s‖ = Cc_colp_LL²L^{−σq}η‖s‖ — **still summable for σ > 0**; the ∂_Xβ part is
≤ CL³(L^{−(1+2σ)q} + L^{−(1+σ)q−3})η‖s‖. C_CV changes by a factor, nothing else.
(ii) §3.1: N_𝔇 is the maximum over □ of N^{(σ)} restricted to Ω_□^{−5} (every slot is measured in the frame of a box containing its
density and read region with margin 5; every density lies in some Ω_□^{−5}). The frames live on Ω_□.
(iii) §4.4: read **C_0 := 25C_FPG_♯(1 + C_Ac_N)(R′ − 1)**, valid once C_AKs_R ≤ 1/24 (the printed 12C_FPG_♯C_A(R′ − 1) did not
match 4A/ε).
(iv) §4.7, "Premise (R) is not an input" — precise form: §3-§4 use (a) aggregate bounds on local tori, restricted to sub-regions
(restriction never increases a sup-slot or J), and (b) **per-plaquette / per-contour** analytic facts on a fixed polydisc of the
finitely many local link variables — analyticity of W_0 and of the slot functions, the centred value bound |â| ≤ Ch³η², β's
vanishing on both axes, and first/second derivatives in single link variables bounded by the own sizes — which Codex itself
reconstructed (CODEX_REVIEW_KOFF §4.3 first two paragraphs; CODEX_REVIEW_NSL F6 items 3-4). They do **not** use (R)'s step "an
aggregate σ-ball bound implies the same bound per density on a local constraint set", which is what Codex BFT4W W1 left
NOT-VERIFIED. Whether that distinction survives a Codex check is the first thing to test (§11).

## §5. BFT-0's identification clause off 𝒞_glob (target B1) — Theorem ID′, PROVEN as an implication of Theorem OFF′

### 5.1 Objects (Balaban's convention, BA-9; NSL55 §4.0 transplanted to frames)
For 1 ≤ j ≤ k and a real level-j field w on the same fine torus (level-j coarse side T_j = TL^{k−j} ≥ T_*) with w ∈ 𝔅_j(ε_*)
(level-j plaquette logs ≤ ε_*): **Z_j(w)** := Theorem OFF′'s depth-j critical point (defined up to 𝒢^{(j)} := composite gauges trivial at
the level-j roots); **E^cb_j(w)** := 𝔉_j(Z_j(w); w) (well defined: 𝔉_j is 𝒢^{(j)}-invariant for every datum, NSL55 In-4, and UQ′ makes
Z_j(w) unique up to 𝒢^{(j)}); E^cb_0 := S_W; **F^cb_j(w, v)** := E^cb_j(w) + κ_jΣ_cφ̂_c(M̄^{(j)}_c(w); v); **U^cb_j(v)** := the level-j
component of Z_{j+1}(v); **𝒢^{rt}_j** := level-j gauges equal to 1 at the level-(j+1) roots (a subgroup of the invariance group of
F^cb_j(·, v) — Codex NSL F5: not the whole group). The **level-j ball** is frame-local:
  **𝔹_j(v) := {w real : every box of side ≤ R′ (level-(j+1) units) carries a level-j gauge g with
  ‖(w^g)^c‖_{1,α;j} + ‖Q_jw^g − v^{g|roots}‖_∞ ≤ r_B}** (the level-j part of the depth-(j+1) frame norm, NSL55's ‖·‖_{T;v} in a frame).

### 5.2 Theorem ID′ — statement
There are ε_ID, r_B, ε_lev, ε_tow > 0 (depending only on the constants of OFF′ and on L) such that, on every torus T ≥ T_*, for
every k ≥ 1:
- **(I1′) restriction.** For real V ∈ 𝔅_k(ε), ε ≤ ε_ID, Z := Z_k(V) and 1 ≤ j < k: (Z_0, …, Z_{j−1}) = Z_j(Z_j)^h with h ∈ 𝒢^{(j)}.
- **(I2′) per-level criticality and value.** For j ≥ 0 and real v ∈ 𝔅_{j+1}(ε_lev): U^cb_j(v) is a critical point of F^cb_j(·, v) and
  **E^cb_{j+1}(v) = F^cb_j(U^cb_j(v), v)**. The identity extends to complex v = e^zv^r (|z| ≤ r_ℂε_lev) by holomorphic continuation.
- **(I3′) per-level uniqueness.** U^cb_j(v) ∈ 𝔹_j(v), and every real critical point w ∈ 𝔹_j(v) of F^cb_j(·, v) equals U^cb_j(v)^h with
  h ∈ 𝒢^{rt}_j; conversely every such gauge transform is critical with the same value.
- **(I4′) the tower.** For real V ∈ 𝔅_k(ε_tow), U_j := Z_j (j < k), U_k := V: each U_j is a critical point of F^cb_j(·, U_{j+1}) in
  𝔹_j(U_{j+1}), unique there modulo 𝒢^{rt}_j, and **E^cb_k(V) = 𝔉_k(Z; V) = S_W(U_0) + Σ_{j<k}κ_jΣ_cφ̂_c(M̄^{(j)}_c(U_j); U_{j+1})**.
With E^br := E^cb this is REVIEW_S22's BFT-0 second bullet on the **full** small-curvature class (arbitrary holonomy), with "unique"
read modulo 𝒢^{rt}_j and "its level-j ball" = 𝔹_j(U_{j+1}) (a frame-local ball of fixed radius r_B).

### 5.3 Proof
*Down-scaling.* A depth-k frame of size ≤ η on a box of side R′ (level k) restricts to depth-j frames on the boxes of side R′ in
level-j units (side R′L^{j−k} ≤ R′ in level-k units) of size ≤ L^{−(k−j)}(1 + C_T)η (NSL55 Lemma SC (a), confirmed by Codex NSL F7;
it scales potentials, gradients, Hölder quotients and weighted residuals, and the depth-j top residual is the depth-k r_{j−1}).
*(I1′).* BA-1 (𝔉_k(x; B) = 𝔉_j(x_{<j}; x_j) + terms in x_j, …, B; Codex NSL F7) makes Z_{<j} a real critical point of 𝔉_j(·; Z_j);
BFT-1 (OFF′ (iii)) gives Z_j ∈ 𝔅_j(3L^{−2(k−j)}C_0ε) ⊂ 𝔅_j(ε_*); down-scaling gives Z_{<j} ∈ 𝔇_j(R, L^{−1}(1 + C_T)C_0ε) ⊂ 𝔇_j(R, r_u)
for ε ≤ ε_ID := Lr_u/((1 + C_T)C_0). UQ′ at depth j (radius r_u fixed, **independent of the size of the cut datum Z_j** — the
point of Codex GV §5.3's ball objection) gives the claim.
*(I2′).* j = 0: F^cb_0(·, v) = 𝔉_1(·; v) and U^cb_0(v) = Z_1(v). j ≥ 1: with y := Z_{j+1}(v), w_0 := y_j, (I1′) at depth j + 1 gives
Y := y_{<j} = Z_j(w_0)^g, g ∈ 𝒢^{(j)}. *Differentiability:* for w near w_0, OFF′ (iv) at depth j (data w = e^{δ}w_0, fixed real frames
of Z_j(w_0)) gives a real-analytic family of critical points Z_j(w), so E^cb_j is real-analytic near w_0 and, Z_j(w) being a full
critical point, **dE^cb_j(w) = ∂_w𝔉_j(Z_j(w); w)** (envelope). At w_0, 𝔉_j(Z_j(w_0)^g; w) = 𝔉_j(Z_j(w_0); w) for **every** w (g fixes
level j; In-4), so ∂_w agrees and d_wF^cb_j(w_0, v) = ∂_{x_j}𝔉_{j+1}(y; v) = 0 (BA-1; y critical). Value:
E^cb_{j+1}(v) = 𝔉_{j+1}(y; v) = 𝔉_j(Y; w_0) + κ_jΣφ̂(w_0; v) = F^cb_j(w_0, v). Complex v: both sides are holomorphic in z on a
common polydisc (OFF′ (iv) at depths j and j + 1; U^cb_j(e^zv^r) holomorphic in fixed real frames, of size ≤ C·r_ℂε_lev) and agree
for real z, hence everywhere (identity theorem in several variables, as Codex NSL F7 checked for the trivial background).
*(I3′).* Membership: Z_{j+1}(v)'s frames restricted to level j are frames of U^cb_j(v) of size ≤ C_0ε_lev ≤ r_B. Uniqueness: let
w ∈ 𝔹_j(v) be real and critical for F^cb_j(·, v). In a frame from 𝔹_j(v), w is small in C^{1,α}, so its level-j plaquette logs are
≤ Cr_B ≤ ε_* and Z_j(w) exists. Root-match (Lemma RM* at depth j: the level-j sites play the role of roots, the datum is w) a depth-j
OFF′-frame of Z_j(w) to the 𝔹_j(v)-gauge g on each box: the result is a depth-(j + 1) frame of **Y := (Z_j(w), w)** whose level-j
part is w^g, of size ≤ C_RM max(3L³C_0ε_*, r_B) after the up-scaling of §4.3 (C_up ≤ 3L³) and Lemma FP in the depth-change
geometry. By the envelope identity, Y is a full critical point of 𝔉_{j+1}(·; v) (lower levels: Z_j(w) critical for 𝔉_j(·; w); top:
∂_w𝔉_{j+1}(Z_j(w), w; v) = d_wF^cb_j(w, v) = 0). So Y ∈ 𝔇_{j+1}(R, r_u) for r_B, ε_* small, and UQ′ at depth j + 1 gives
Y = Z_{j+1}(v)^{g′}, g′ ∈ 𝒢^{(j+1)}; reading level j, w = U^cb_j(v)^h with h := ev^{(j)}g′ ∈ 𝒢^{rt}_j. Converse: for h ∈ 𝒢^{rt}_j,
F^cb_j(w^h, v) = F^cb_j(w, v) (M̄ is covariant with root values 1; E^cb_j(w^h) = E^cb_j(w) because Z_j(w^h) = Z_j(w)^{ĥ} for any
level-0 extension ĥ, by UQ′), so criticality and value transfer.
*(I4′).* ‖Z_{j+1}‖ in the level-(j+1) data class is ≤ 3C_0ε_tow ≤ ε_lev (BFT-1); (I1′) at depth j + 1 and the computation of (I2′)
give criticality and the value; membership and uniqueness are (I3′); telescope with BA-1. ∎

### 5.4 What is and is not identified
- **Delivered:** the composite-action tower in Balaban's convention on the full small-curvature class, real data, every torus
  T ≥ T_*, uniformly in k, T, j; the complex recursion (I2′). This is P13 of OFFGLOB55 ("local frames suffice and NSL applies in frame
  coordinates") **proved**, with the caveat Codex OFFGLOB F13 raised: frames, relative patching and the complex convention were the
  missing pieces, and they are §1-§4 here.
- **Not delivered (unchanged from 𝒞_glob):** uniform identification with independently prescribed higher-level BR1 actions E^br_j
  (Codex NSL F8: NOT-VERIFIED, "the single most dangerous remaining identification"); complex (I1′)/(I3′)/(I4′); boxes (§8).

## §6. BFT-3 off 𝒞_glob (target B2) — Theorem BFT3-off, PROVEN as an implication (gauge-invariant form)

### 6.1 The gauge question, and the statement
On 𝒞_glob, U_j is the slice representative in one global gauge, so "∂^nU_j(x)/∂V(y_1)⋯" is meaningful. Off 𝒞_glob the background is
defined modulo 𝒢^{(k)} and no global gauge exists (Proposition C4); the derivative of a gauge-dependent object needs a local gauge
convention. I prove the clause for (a) E_k^br and (b) every **gauge-invariant local function** of the background, and record (c) the
local-slice-coordinate form as ARGUED. Data derivatives are in left-trivialised coordinates: V = e^zV^r, ∂/∂z_y, y a level-k link.
> **Theorem BFT3-off.** Under Theorem OFF′'s hypotheses, with μ_W := ln 2/D_W, D_W := 4(4R + 6) + 8 (an ℓ¹ bound for the diameter
> of Ω_□ plus read radii), for all z with |z|_∞ ≤ r_ℂε/2, every n ≥ 1 (in particular n ≤ 4), all level-k links y_1, …, y_n:
> - **(a)** |∂E/∂z_{y}| ≤ C_1^E and, for n ≥ 2, **|∂^nE/∂z_{y_1}⋯∂z_{y_n}| ≤ C^E_n·e^{−(μ_W/(n−1))𝔱(y_1, …, y_n)}**;
> - **(b)** for every O_x — a function of the background's links within coarse distance r_O of x, invariant under 𝒢^{(k)} (real, hence by
>   continuation complex-infinitesimal), holomorphic and bounded by M_O on the fixed-frame complex ball — **|∂^nO_x(Z(e^zV^r))/
>   ∂z_{y_1}⋯∂z_{y_n}| ≤ C^O_n·e^{−(μ_W/n)𝔱(x, y_1, …, y_n)}**, C^O_n ≤ C(n)M_Oe^{μ_Wr_O};
> - C^E_n, C^O_n, μ_W independent of k and T. Examples of O_x: tr of Wilson loops near x; |ρ_l(c)|², tr(ρ_l(c)^m); |log U_{j,P}|²;
>   the plaquette spectra. These carry BFT-1's and (BG)_k's curvature information.
> - **(c) ARGUED:** the same for the frame coordinates of Z near x in the local S_E slice of a box containing x (NSL's fixed point
>   ξ(x) = Ψ_x(ξ(x)) is a finite-range contraction — Λ reads x_0 within 3, R_0 is pointwise — so its dependence on far data decays
>   like 2^{−dist/3}; I have not written the bookkeeping).
(n ≤ 4 rates: (a) μ_W, μ_W/2, μ_W/3; (b) μ_W/4 at n = 4 — route C. Route T's better rates need the 1-Lipschitz forms, not redone here.)

### 6.2 Proposition GPW (weighted exact right inverse, box-indexed scalar weights) — PROVEN as an implication
For a 1-Lipschitz f (ℓ¹ coarse) and μ ≥ 0 let N_{𝔇,μ,f} and ‖·‖_{𝔇,μ,f} be N_𝔇, ‖·‖_𝔇 with every local quantity multiplied by
e^{μf(base point)} (BFT4W55 §2.2's base-point form; J_μ := Σ_lπ_{l,μ}). At a (real or fixed-frame complex) critical Z of §4:
**N_{𝔇,μ,f}(ℰ_ZS) ≤ e^{μD_W}C_E(1/R + η)N_{𝔇,μ,f}(S), ‖𝒫_ZS‖_{𝔇,μ,f} ≤ e^{μD_W}βN_{𝔇,μ,f}(S),** hence for 0 ≤ μ ≤ μ_W and
C_E(1/R + η) ≤ ¼: **‖R_ZS‖_{𝔇,μ,f} ≤ 4βN_{𝔇,μ,f}(S)**, uniformly in k, T, f.
*Proof.* Each piece e_□ and each 𝒫-piece reads S only through local quantities based in I_□ := □^{(4)} (M_{χ_□} and covariant routing
stay in the cells meeting □^{(1)}) and is supported in O_□ := Ω_□ (ψ_□-cutoff; M_ψg, C^♯_ψ, the ℋY terms and Φ^{−1} have read radius
≤ 5). The unweighted chain is used verbatim (PAR, at S_G = 0); weights enter only at the two ends:
N_μ(e_□) ≤ e^{μ sup_{O_□}f}N(e_□) ≤ e^{μ sup_{O_□}f}C_E(1/R + η)N(S|_{I_□}) ≤ e^{μ(sup_O f − inf_I f)}C_E(…)N_μ(S), and
sup_O f − inf_I f ≤ diam_ℓ¹(Ω_□) + 8 ≤ D_W. Sum over the ≤ n_R pieces meeting a box (finite sum; no profile needed). This is the
mechanism Codex BFT4W W6 CONFIRMED for H2W ("box-indexed construction using scalar weights on already-cc pieces"); here the
pieces are representation-valued and ℰ_Z is linear on Rep_cc(Z), so no weighted operator on the cc class is formed. ∎

### 6.3 Proof of Theorem BFT3-off
*First derivatives.* z ↦ Z(e^zV^r) is holomorphic in fixed real frames (OFF′ (iv)); G(Z(z); z) ≡ 0 gives DG(Z)[∂Z/∂z_y] =
−∂_{z_y}G =: −π_Z(S_y), with S_y the representation of the top-soft-term derivative at y (a top residual slot plus level-(k − 1)
plain currents on the S4′ contours of y; N_𝔇(S_y) ≤ C_S, supported within coarse distance 2 of y). GP′ (complexified — PAR's proof
is algebraic and its bounds hold on the fixed-frame complex ball; the annihilator argument uses only the complex-bilinear symmetry
of H_Z) gives DG(Z)R_ZS_y = π_Z(S_y), so ∂Z/∂z_y + R_ZS_y ∈ Ker DG(Z) = Ran Ξ_Z ((N1-nd)). A 𝒢^{(k)}-invariant O_x has
DO_x[Ξ_Zλ] = 0, so **∂O_x/∂z_y = −DO_x[R_ZS_y]**. GPW with f := d_1(·, y) and μ = μ_W: |DO_x[R_ZS_y]| ≤
C M_O·‖R_ZS_y‖_{𝔇 near x} ≤ CM_Oe^{μ_Wr_O}·4βe^{μ_W·2}C_S·e^{−μ_Wd_1(x, y)} (Cauchy for the bounded holomorphic O_x gives
|DO_x[w]| ≤ CM_O‖w‖ on the region it reads). For E: E(z) = 𝔉_k(Z(z); z) and G(Z) = 0 give **∂E/∂z_y = Ψ_y(Z) := ∂_{z_y}𝔉_k(Z; z)**
(envelope), a gauge-invariant function of Z within coarse distance 2 of y, bounded by C_1^E; then ∂²E/∂z_y∂z_{y′} =
∂_{z_{y′}}Ψ_y|_Z − DΨ_y[R_ZS_{y′}], whose first term vanishes unless y′ shares y's top soft term, so
|∂²E/∂z_y∂z_{y′}| ≤ C^E_2e^{−μ_Wd_1(y, y′)}.
*Higher orders (route C).* Both first-derivative bounds hold at **every** point of the polydisc |z|_∞ ≤ r_ℂε (GPW at every complex
critical point of §4.6). BFT34_55's Lemma BB-C (re-derived there; Codex BFT34 R1/R3 CONFIRMED) — Cauchy on the polydisc of
per-coordinate radius r_ℂε/(2(N² − 1)^{1/2}) about a point of the half polydisc, with the star/pair spanning-tree bounds
𝔱 ≤ n·max_id(x, y_i), 𝔱 ≤ (n − 1)max d(y_i, y_j) — gives (a) and (b) with C(n) ≤ (n − 1)!(4(N² − 1)^{1/2}/(r_ℂε))^{n−1}·(first-order
constant). The ε^{−(n−1)} is a fixed number once ε is fixed (BFT's constants may depend on ε_0). ∎

### 6.4 Consumer remarks (not proofs)
- FLOW's (SF-bg) is BFT-3 at V = 1, z = 0 — on 𝒞_glob, banked (Codex BFT34). Nothing new needed.
- RLARGE's (BG)_k (PLD l.1023: "𝔟(V) local with exponential tails and curvature ‖X(𝔟(V))‖ ≤ C_IL^{−2}max_{P nearby}‖X_P(V)‖")
  asks for gauge-invariant quantities (curvature norms) — form (b) — **but** on V that are small-field only within R_bg of a region
  (PLD l.987-988: "every level-(k+1) plaquette within level-(k+1) distance R_bg of A has ‖1 − V_P‖_op < ε_1"). Theorem BFT3-off is on
  the global small-field class; it does not define 𝔟(V) when V has large-field regions elsewhere. A **localised** background (defined
  from V near A, compared with the global one by BFT3-off's exponential tails) is needed there — a separate statement (Balaban's
  localised background fields); I name it, I do not prove it: **(LOC-bg)**.

## §7. BFT-4 off 𝒞_glob = (c₀) (target B3; coordinator's scope, with CODEX_REVIEW_BFT4B R3/R4/R8/R9)

### 7.1 Targets
- **(c₀)** (BFT4B55 §1, Codex BFT4B item 6): E_k^br = S_W + c + Σ_XR(X) on the gauge-invariant class 𝒦_BFT (interior), R(X)
  holomorphic and bounded on 𝒦_BFT restricted to a bounded neighbourhood of X, zero unless X is *-connected, with
  sup_{Q_0}Σ_{X∋Q_0}‖R(X)‖e^{m_0|X|} ≤ C_pol uniformly in k, T. No invariance clause.
- **(H-inv)** for E_k^br, so that Lemma AVG (Codex BFT4B item 1, PROVEN) turns any (c₀) into locally gauge-invariant pieces — with
  Codex's correction: **factor 2 in HIST's centred norm** sup|R(X)(W) − R(X)(1)| (R3's SU(2) counterexample to factor 1).
- **The consumer bridge** (Codex BFT4B R4/R9, "most dangerous"): identification of a (c₀) localisation of the **global** critical
  value with the consumer's own objects (HIST (I_k^E)″: localized cone minimisers, assigned densities, free boundary).

### 7.2 Proposition HINV — (H-inv) holds on the whole class — PROVEN as an implication of Theorem OFF′
*Real data.* For a real level-k gauge g (any, not only root-trivial) and real V ∈ 𝔅_k(ε): let ĝ be any level-0 extension of g.
Z(V)^{ĝ} is a real critical point of 𝔉_k(·; V^g) (composite gauge invariance, NSL55 In-4) and lies in 𝔇_k(R, C_0ε) (frames transform
with ĝ). By UQ′ it is Z(V^g) up to 𝒢^{(k)}, so **E_k^br(V^g) = 𝔉_k(Z(V)^{ĝ}; V^g) = 𝔉_k(Z(V); V) = E_k^br(V).** *Complex data.*
(e^zV^r)^g = e^{Ad z}(V^r)^g with Ad z := (Ad(g(b^−))z_b); for fixed real g, z ↦ E((e^zV^r)^g) − E(e^zV^r) is holomorphic and
vanishes for real z, hence identically (§2.2 item 4's identity-theorem argument). So E_k^br is invariant under the full real gauge
group on the complex class (the real-gauge invariance AVG needs; complex gauges are not needed). S_W is invariant. ∎

### 7.3 Why BFT4a-glob does not transfer "frame by frame" — the precise obstruction (PROVEN-HERE as stated)
BFT4W55's family sums cube components in **one chart**: views S_Q𝐀 = Σ_{Q′}s_{QQ′}A_{Q′}, A_{Q′} displacements from the trivial chain
of the global gauge; the s ≡ 1 identity Σ_QA_Q(1) = x(B) (Lemma IDcc) uses that the chart is linear.
*(i) Frame charts are not linearly related.* Two real frames of one configuration differ on an overlap by t = c·e^{τ} (Lemma RG′,
unrooted), and coordinates transform by the **nonlinear** gauge action y ↦ y^t = Ad(c)(y)^{e^τ}, with the pure-gauge offset
(0)^{e^τ} = −Ξτ + O(τ²) ≠ 0. A sum of frame-transported pieces Σ_{Q′}s_{QQ′}(A_{Q′})^{t_{QQ′}} is neither linear in 𝐀 nor, at
s ≡ 1, the coordinate expression of one configuration.
*(ii) Constant-transition frame systems do not exist in general.* If all transitions were constant (τ ≡ 0), every contractible
loop γ through a chain of overlaps would satisfy d(hol_γ, 1) ≤ |γ|·η (telescoping against the constant transitions, as in
OFFGLOB55 §2.2), while a loop of coarse size ρ encloses flux ≍ ρ²κ (κ the coarse curvature); Proposition C4's construction (Codex
OFFGLOB item 1, PROVEN) gives configurations with ρ²κ ≫ ρη once ρ ≫ η/κ. So "frames related by constants" — which would make (i)
linear and exact — is FLAT-REF at the overlap scale, false in general (P5, Codex F13 CONFIRMED).
*(iii) Consequence.* A frame-free formulation is forced: cube components must be **left-trivialised tangent vectors at one global
real reference configuration U_ref** (sums of tangent vectors at a fixed point are linear and frame-free), and U_ref must be a
**local** function of V, or the pieces R(X) are not local. The available global configurations are not local: Z^lift is rough
(BA-2: excluded in every decaying norm), the depth-induction start U_0 contains Z_{k−1}(V_0) (a global object), and Z(V) itself is
the unknown. (CovLift)/Z^sm would serve but is NOT-VERIFIED ([S26-BANKED]).

### 7.4 Theorem C0-red — (c₀) reduced to one local input (GL); status REDUCED (not proved)
**(GL) a local reference configuration.** A map V ↦ U_ref(V) on the complex class with: (i) *locality*: U_ref on a coarse cell is a
function of V within coarse distance D_ref (a constant multiple of R); (ii) holomorphy in V (real on real V); (iii) U_ref ∈ 𝔇_k(R, C_refε)
(real V; fixed-frame complex ball for complex V); (iv) a representation S_ref of G(U_ref) with N_𝔇(S_ref) ≤ ν_refε, ν_ref small
enough for NK′ at the scale of §4.2.
**Claim (C0-red).** OFF′'s inputs + (GL) ⇒ (c₀) on the full class, with R(X) depending on V within coarse distance D_ref + 6R of X
and with E_k^br = S_W + Σ_X R(X) after absorbing the local sums 𝔉_k(U_ref; V) − S_W(V) into singleton pieces.
*Construction (frame-free bond family at U_ref).* (1) Box pieces: PAR's 𝒫_□ and ℰ_□ at U := U_ref with S_G := S_ref (fixed real frames of
U_ref; linear in their argument, finite range, independent of the unknown). (2) The cc-projected equation: A ↦ e^AU_ref (A a
left-trivialised tangent vector at U_ref); with 𝔑(A) := G(e^AU_ref) − G(U_ref) − DG(U_ref)A, represented by Lemma T,
  A = −R^{cc}P^{U_ref}_cc[S_ref + T^{rep}(A)],  R^{cc} := 𝒫Σ_n(P^{U_ref}_ccℰ)^n,
where P^{U_ref}_ccℰ is bounded because the charges of π(ℰS) are the aggregate-Ward charges ((DΞ[𝒫S])^TG(U_ref))^⊥, routed by the
covariant form of Lemma DKC at cost C‖𝒫S‖N(S_ref). A fixed point is a critical point: P^{U_ref}_ccG(e^AU_ref) = 0 forces
G = P^T_{U_ref}((D_{U_ref} − D_{e^AU_ref})^TG)^⊥, and the covariant analogue of CCP (c) (a K′-type charge of size ‖A‖, Lemma KC's
algebra) gives J(G) ≤ C‖A‖J(G), so G(e^AU_ref) = 0. (3) Cube family exactly as BFT4W55 Construction BBcc, with views
S_Q𝐀 := Σ_{Q′}s_{QQ′}A_{Q′} — **sums of tangent vectors at one point, hence linear and frame-free** (the obstruction of 7.3 is gone) —
and 𝐑̃ := the bond-weighted P^{U_ref}_ccℰ-pieces, 𝐏̃ := the bond-weighted 𝒫-pieces. Holomorphy in s and the splitting property
(Lemma Dcc (i), (iii)) transfer because every piece has finite range and U_ref is local (GL (i)). (4) s ≡ 1: A := Σ_QA_Q(1) is a fixed
point of (2), hence e^AU_ref is critical, real for real V, of frame size ≤ (C_ref + C)ε ≤ r_u, so **UQ′ identifies it with Z(V) up
to 𝒢^{(k)}** and 𝔉_k(e^AU_ref; V) = E_k^br (complex V: identity theorem) — UQ′ replaces BFT4W55's slice-uniqueness Lemma IDcc, and
no Π_E-inside design is needed. (5) Per-cube energy 𝔈_Q(s) := Σ_{D∈𝒟_Q}[D(e^{S_Q𝐀}U_ref) − D(U_ref)] (gauge-invariant densities):
in a real frame of U_ref the first-order term is ⟨∇D(U_ref), ·⟩ with |∇D| ≤ Cη per density (U_ref is not critical), so
|𝔈_Q| ≤ C|Q|(η + r_s)r_s by Lemma E2^σ's proof in the frame (Codex BFT4W W7: the power count and the complex Cauchy argument
CONFIRMED). (6) Cluster expansion and polymer bound: Codex BFT4W W9 / BFT34 R11 (CONFIRMED combinatorics), uniform anchor.
*Status.* Steps (1), (2) (the identity part) and (4) are proved here (they are PAR, Lemma T, KC/DKC and UQ′); steps (3), (5), (6) are
BFT4W55 §6 with PAR's pieces substituted for RWE's — **ARGUED** (each estimate has the same form; I have not rewritten them). The
genuinely missing input is **(GL)**.

### 7.5 (GL): what it is and why it is plausible — ARGUED
Candidate: for each box □ let g^{AX}_□ be the **holomorphic** axial transport frame of V from a fixed corner of Ω_□ (a polynomial in the
links, so holomorphic; real on real V; data size ≤ 3R′ε + r_ℂε by Lemma C2); B̃_□ := ι_*(φ_□log V^{g^{AX}_□}) is 𝒞_glob-type data on
𝕋_□; BFT-E on 𝕋_□ (banked) gives the local critical point x_□ = x(B̃_□), holomorphic and local in V. Glue the local critical
configurations by Lemma FP-type merges after aligning their gauges on overlaps by NSL. Then (i)-(iii) hold, and (iv) holds **if**
two local critical points whose data agree on a box agree in the middle up to Ce^{−μ dist}ε in compatible gauges — **(LUD), local
uniqueness with decay**, an exponential-locality statement for local critical points on 𝒞_glob-type local tori (from the weighted
linear estimates on 𝒞_glob — banked COFM55/GV-E_m, or H2W — plus the difference equation; the transplant boundary is where the
data differ). With (LUD), N(S_ref) ≲ e^{−μR/4}ε·C(R), and ν_ref is small for R large. **Status: ARGUED; (LUD) not written.**

### 7.6 (H-inv) + AVG and the consumer bridge
- Given (c₀), Proposition HINV and Lemma AVG give locally gauge-invariant pieces, **with the uncentred constant unchanged and the
  centred constant (HIST's sup|R(W) − R(1)|) at most doubled** (Codex BFT4B R3). Domain coverage of each consumer's own domain
  (HIST's polar domains, N5's box witnesses) is a separate radius comparison (Codex BFT4B R8 gives sufficient scalar conditions,
  e.g. 2√N arcsin(ε_1) ≤ ε_0, α_E ≤ r_ℂε_0) — not done here.
- **The bridge (LOC-min) — OPEN, stated precisely.** HIST's (I_k^E)″ uses the analytic continuation of a **localized free-boundary
  infimum** on cones with assigned densities and boundary terms (Codex BFT4B R4, R9). A (c₀) localisation of the **global** critical
  value serves it only together with: *for every cone C of bounded size, the localized free-boundary minimiser on C equals the
  restriction of Z(V) up to O(e^{−μ dist(·, ∂C)}) in a frame, and the localized cone energy equals Σ_{X⊂C}R(X) plus boundary polymers
  supported within O(1) of ∂C.* This needs (a) a free-boundary box version of Theorem OFF′ (§8: OPEN) and (b) (LUD). I have proved
  neither.

## §8. Boxes (B4) and small tori (B5)

### 8.1 Non-wrapping boxes with "N5-sf0's boundary convention" — OPEN, with the missing input named
*What the convention is.* Theorem N5-sf0 is a **torus** theorem (T ≥ T_0); its boxes Ω^+_□ (side ≤ (4R_* + 5) blocks) enter only
through **Dirichlet compressions** K_{Ω_□} of the torus operator (PROOF "Theorem RW", (RW1)). For the nonlinear BFT on a box Λ no
convention is stated anywhere I found; the consumers want different ones: HIST (I_k^E) — **free boundary** on cones (Codex BFT4B
R4); RLARGE local regions — **Dirichlet-type** (exterior fixed, possibly large-field); SPHERE55's seam — mixed (ASSEMBLY55 F21).
*What §1-§4 give.* Every step is local: frames, merges, RFP, CONV′, KC, DKC, PAR's pieces, AP′'s and UQ′'s local estimates all act on
boxes of side ≤ R′ through local tori. So for a box Λ the whole argument runs verbatim on the **interior** (boxes □ with
Ω_□ ⊂ Λ at distance ≥ R′ from ∂Λ). For boxes □ meeting the boundary layer, PAR needs a local inverse L1 **on a box with the chosen
boundary condition** — every banked linear estimate (LIN^{(σ)}, GV-E, TOP♯, CC-INV, COF) is on tori. *Missing input:* **(BL-D) /
(BL-F)** — the K^{(σ)}/GV-E linear package (σ-pair, cc sources, k-uniform) on boxes with Dirichlet resp. free boundary conditions,
plus the slice functional Λ adapted to the boundary. With it, the frame route gives the box BFT by the same proof. One trivial case
is available: Dirichlet data equal to the restriction of a torus critical point Z(V) have Z|_Λ as the box critical point (UQ′ on the
torus gives uniqueness among configurations that agree with Z outside Λ and are frame-locally small). **Status: OPEN.**

### 8.2 Tori with T < T_* = 4R + 6 — not needed for BFT as stated; OPEN off 𝒞_glob, with the obstruction named
- REVIEW_S22's BFT asks for tori of side ≥ T_0 with T_0 depending only on (N, L, κ_±); T_* := 4R + 6 with R fixed by §4 is such a T_0,
  and the depth induction only uses TL ≥ T_*. **So BFT itself needs no T < T_*.** (Symbol warning: this T_* is not N5-sf0's
  T_0 = 4R_* + 6; R and R_* are different box scales.)
- On 𝒞_glob, tori 3 ≤ T < 5 are covered by the descended slices (GV55 / Codex GV item 3; NSL55, T ∈ {3, 4}).
- Off 𝒞_glob on a torus of side T < T_*: contractible lattice loops have area ≤ T², so the data are within O(T²ε) of a flat
  connection on each contractible patch, but the cycle holonomies h_μ are arbitrary (Proposition C6, Codex-confirmed). If
  max_μd(h_μ, 1) ≲ Tε the data are in 𝒞*_glob(CTε) and the banked theorems apply; otherwise the background is near a **flat
  connection with nontrivial holonomy**, where the linear package is not on file (CODEX_REVIEW_BGT: "flat connections with
  nontrivial holonomy need a separate argument"). A consumer needs this only if the RG is run until the coarse torus is smaller
  than T_*; I found none in REVIEW_S22's "Who needs which part". **Status: OPEN, not needed by BFT as stated.**

**Erratum E3 (to §8.1's "one trivial case").** Z|_Λ is **a** Dirichlet box critical point when the exterior data are Z's, but its
uniqueness does **not** follow from UQ′: a Dirichlet critical point W glued to Z outside Λ is critical only in the interior
directions (densities straddling ∂Λ see W and Z), so the glued configuration is not a torus critical point. Read: "Z|_Λ is a box
critical point; uniqueness is part of (BL-D)."

## §9. Assembly: BFT-0..4 on REVIEW_S22's full small-field data class, as an implication

Data class: V = e^zV^r, V^r real with max_P|log V^r_P| ≤ ε ≤ ε_*, |z|_∞ ≤ r_ℂε (REVIEW_S22 "Statement (BFT)"), every torus T ≥ T_*,
every k ≥ 1. Constants depend on (N, L, κ_±, α, θ, σ) and the input constants only.
| Clause (REVIEW_S22) | Delivered form off 𝒞_glob | Where | Status |
|---|---|---|---|
| BFT-0, first bullet (existence; uniqueness mod composite gauges trivial at level k) | real data: Z(V) ∈ 𝔇_k(R, C_0ε), unique mod 𝒢^{(k)} among real critical points in the **frame-local** ball 𝔇_k(R, r_u) (REVIEW_S22's global slice ball {e^XZ^lift, X ∈ S_k} does not exist off 𝒞_glob: Prop. C4, §7.3 (ii)); complex data: existence by continuation, **uniqueness not claimed** (F7) | OFF′ (i), (ii), (iv) | PROVEN as an implication |
| BFT-0, second bullet (identification) | Theorem ID′ (I1′)-(I4′), Balaban's convention, real data; complex (I2′) | §5 | PROVEN as an implication; uniform identification with independently prescribed BR1 actions **NOT-VERIFIED** (as on 𝒞_glob) |
| BFT-1 | (θ_w^c, θ_w^r) = (2, 2 + σ), gauge-invariant per-level bounds, Hölder in blocks | OFF′ (iii) | PROVEN as an implication |
| BFT-2 | Z(e^zV^r), E(z) holomorphic in z in fixed real frames; E is the unique continuation of the real composite value | OFF′ (iv), §2.2 | PROVEN as an implication |
| BFT-3 (n ≤ 4, and every n) | E-part and every gauge-invariant local functional; rates μ_W/n (resp. μ_W/(n − 1)), μ_W = ln 2/D_W | §6 | PROVEN as an implication; frame-coordinate (local-slice) form ARGUED |
| BFT-4 (a)/(c₀) | (c₀) **REDUCED** to (GL) (local reference) + BFT4W55 §6 transplanted to PAR pieces; (H-inv) proved; local invariance via AVG (centred factor 2) | §7 | (c₀) **OPEN** (reduced); HINV PROVEN as an implication; consumer bridge (LOC-min) **OPEN** |
| BFT-5 (b), m = 0 and weighted | exact right inverse on representations (GP′); weighted for μ ≤ μ_W (GPW); (N1-nd) | §3.5, §6.2 | PROVEN as an implication |
| Boxes | interior: verbatim; boundary layer needs (BL-D)/(BL-F) | §8.1 | OPEN |
| Tori T < T_* | not needed by BFT as stated; near nontrivial flat holonomy unknown | §8.2 | OPEN (no consumer found) |
**Inputs** (all named in §4.7): banked K^{(σ)}/GV-E/LIN^{(σ)} package and L1 (conditional on the lane-A linear package); NSL
(conditional on EP-bd); OC; WM^σ, WC^σ; covariant routing/LOC (Codex OFFGLOB item 3); NSL's Lemmas B-D; per-contour local
analyticity (Codex KOFF §4.3, NSL F6); this file's §1-§6 (Opus 5.5 only, **no Codex check yet**). **Not inputs:** (R) (in the sense
of Codex BFT4W W1 — see E2 (iv)), alignment, (UHL-fine), (SL-cov), Z^sm/(CovLift) (except as one candidate for (GL)), lane-B (N1).

## §10. Findings on prior claims (verdict; file + locating string; reason)
- **Q1. OFFGLOB55 §6.2 "Lemma RG (gauge rigidity) … ARGUED-standard"** — **CONFIRMED** (now PROVEN-HERE as Lemma RG′, §1.1), with
  the precise form: derivative parts of τ are O(η) uniformly; the sup part is O(D_Ωη) unless the frames are root-matched, in which
  case it is O(η) with no box-size factor. The cited mechanism "integrate" is replaced by the explicit uniform generator Φ_n.
- **Q2. OFFGLOB55 §6.2 "Lemma FP (frame patching on a box) … ARGUED-standard"** — **CONFIRMED** (PROVEN-HERE as Lemma FP via Lemma
  MG, §1.3-§1.4), with constants independent of R and the smallness R²η ≤ c_FP (E1). Its sketch's "products of constants around
  cycles of boxes … near 1" is true in the regime but not needed: merging across slabs in a fixed order is a tree; holonomy enters
  only as τ̃'s growth across a slab (§1.3 Remark).
- **Q3. OFFGLOB55 §6.6 "Proposition UQ … PROVEN as an implication"** — **REFUTED as a proof** (agree with Codex OFFGLOB F8: the step
  q ≤ ½q needs a relative estimate single-field FP does not give). The conclusion (real case) is **PROVEN here as UQ′** (§4.5) from
  the relative, root-preserving Lemma RFP (§1.7).
- **Q4. OFFGLOB55 §6.5 "Proposition AP … PROVEN as an implication" on the complex class with real frames** — **REFUTED** (agree with
  Codex F7; re-derived §2.1). Real form: **PROVEN here as AP′** (§4.4), with AX-root-matched frames and an infimum over frame systems
  that is attained.
- **Q5. OFFGLOB55 §5.2 "Theorem GP … PROVEN as an implication"** — **NOT-VERIFIED as stated** (agree with Codex F6/F9: the operator was
  not defined on source vectors). **Replaced** by PAR/GP′ (§3.4-§3.5): defined on representations, exact error representation,
  bounded compatible error operator ℰ_Z.
- **Q6. OFFGLOB55 §4.3 "Lemma CONV … G- and s-slots ARGUED"** — **CONFIRMED** (PROVEN-HERE as Lemma KC, §3.3). OFFGLOB55's sketch
  ("mostly the divergence of the plain current [y_0, G_0] (route by HR (iv)) plus bare charges [dy_0, G_0] of own size
  n^{−4}η|G^c|") is exactly KC's (G) split; the s-slot split (bare [s, r(y)] + level-l currents) is new here.
- **Q7. OFFGLOB55 §5.2 "(ND) … ARGUED"** — **CONFIRMED** (PROVEN-HERE as Lemma DKC, chart form, Codex F9's sign).
- **Q8. OFFGLOB55 §4.3 "Lemma NE … ARGUED"** — **NOT-VERIFIED and not needed**: §3-§4 compare frames only through RG′ (1 + O(η) on
  representations, a fixed C_t on log-tangent vectors); no comparison with the covariant 𝔐^∇_Z norm is used.
- **Q9. OFFGLOB55 §5.2 "(W-comm)^σ … the ỹ-dependent part is O(η/R) by the same local bounds — ARGUED"** — **NOT-VERIFIED, and not
  needed**: PAR prices the background-dependent part [H^{log}_y − H, ψ] at O(η) from the aggregate source bounds (no 1/R gain is
  required: E_U's bound already carries η).
- **Q10. OFFGLOB55 §5.2 "W-mult^σ … ARGUED"** — **CONFIRMED** (WM^σ is a statement about every chain, applied in frame log coordinates;
  Codex OFFGLOB item 5 banks "smooth frame-log W-mult").
- **Q11. OFFGLOB55 §7 P13 "NSL applies verbatim to frame coordinates … only frames (Lemma C2, RG, FP) are needed"** — **CONFIRMED now**
  (Codex F13 had NOT-VERIFIED it for lack of frames, relative patching and the complex convention — supplied by §1, §2, §4.5);
  delivered as Theorem ID′ (§5).
- **Q12. OFFGLOB55 §6.7 "Not delivered: BFT-0's identification clause off 𝒞_glob; BFT-3/4 off 𝒞_glob; … boxes; T < T_*"** —
  status update: identification **PROVEN as an implication** (§5); BFT-3 **PROVEN as an implication** in gauge-invariant form (§6);
  BFT-4 (c₀) **reduced** (§7); boxes **OPEN** (§8.1); T < T_* **not needed by BFT**, OPEN (§8.2).
- **Q13. BFT4B55 §2.3 "Theorem T0 … PROVEN-HERE"** — **NOT-VERIFIED** as a consumer-closure claim (agree with Codex BFT4B R4, R17).
  Its Lemma AVG: CONFIRMED (Codex item 1) and used; its Remark 4 "(H-inv) for E_k^br … is part of what BFT-0 off 𝒞_glob must
  deliver" — **delivered** (Proposition HINV, §7.2).
- **Q14. BFT4B55 §2.2 K4 / §5.2 "with the same bounds"** — **REFUTED in the centred norm** (agree with Codex BFT4B R3: factor 2).
- **Q15. BFT34_55 §1.3 "Scope … off 𝒞_glob, BFT-0 itself is OPEN ((G♯-patch), (UHL), (SL-cov), the smooth lift)"** — status
  **superseded** for real data (OFF′, pending Codex); the list is not a list of necessary inputs (none of the four is used).
- **Q16. BFT4W55 §8 item 2 "BFT's class off 𝒞_glob (PD-curv) … BFT-0 itself is OPEN off 𝒞_glob"** — status superseded as Q15; the
  BFT-4 part off 𝒞_glob remains OPEN (§7: reduced to (GL)).
- **Q17. HANDOFF row "BFT off 𝒞_glob … five local lemmas ARGUED; identification clause, BFT-3/4, boxes open"** — update: the five
  ARGUED lemmas are proved or shown unnecessary (Q1, Q2, Q6, Q7, Q8-Q10); identification and BFT-3 delivered as implications;
  BFT-4 reduced; boxes open.

## §11. Codex verdicts used — agree or disagree, explicitly (files as on disk 06:0xZ; each complete, ending with its banking list)
- **CODEX_REVIEW_OFFGLOB.** F1 (C2/C4/C6; C6's gauge order T_W^{−1}T_V): **agree** (C6 not used). F2 (HR_U/LOC algebra): **agree**, used
  (P4). F3 (U1's 1.1 → 3.3): **agree** (U1 not used). F4 (CCL/LOC signs and coefficient 221 + (324√2/n)η_F + 2592η_ρ): **agree**,
  used as P4's C_loc; I did not re-derive the 324√2 and 2592 (NOT-VERIFIED by me; only their finiteness matters). F5 (L1/L2;
  ΓK_y = +1 + ΓK′_y): **agree** — re-derived: K_y = −Ξ + K′_y and ΓΞ = −1 give ΓK_y = 1 + ΓK′_y. F6 (slot cutoffs not intrinsic):
  **agree**; it is why §3 works on representations. F7 (complex AP false): **agree**, re-derived (§2.1). F8 (UQ needs a relative
  estimate): **agree**; answered by RFP/UQ′. F9 (Ward sign +DK^T∇F; aggregate projection): **agree**; used in PAR (iii) and GP′.
  F10 (lift and abstract NK sound; induction needs AP reset and relative estimates): **agree**; §4.3-§4.5. F11 (ALIGN not retired):
  **agree** — nothing here addresses ALIGN's full N pair. F12 (leftovers priced): **agree**; KC/DKC/RG′/FP/RFP are my answers to its
  table. F13-F14: **agree**.
- **CODEX_REVIEW_NSL** F3 (SC's 84 > 81; C_up ≤ 3L³ survives), F5 (𝒢^{rt} is a subgroup, not the invariance group), F6 (NSL, Lemmas
  B-D CONFIRMED, real scaled-norm), F7 (ID (I1)-(I4), complex I2, fixed-radius uniqueness): **agree**, all used (§1, §4.3, §5).
- **CODEX_REVIEW_BFT4W** W3-W4 (CEN1, CORNER, WM^σ, WC^σ), W6 (box-indexed weights — used in GPW), W7 (E2^σ power count), W9
  (cluster combinatorics; V2b/V4/V7): **agree**. W1 ((R) NOT-VERIFIED): **agree**; E2 (iv) explains why I believe §3-§4 avoid it —
  for Codex to test. W8 (small-torus prefactor): agree (not used).
- **CODEX_REVIEW_BFT4B** R1 (AVG), R3 (centred factor 2, SU(2) counterexample), R4/R9 (consumer bridge GAP), R8 (invariance ≠
  coverage): **agree**; §7.6.
- **CODEX_REVIEW_KOFF** §4.3 (local analytic completion, per-contour), §5.3 (corrected K), items 1-6: **agree**, used.
- **CODEX_REVIEW_BFT34** R1/R3 (Lemma WD, route C, BB-C), R5 (RW-cc algebra), R11: **agree**, used in §6.3.
**No Codex verdict was found wrong.**

## §12. Summary table

### 12.1 Results of this file (status words; none has had a Codex check)
| Result | Where | Status |
|---|---|---|
| Lemma RG′ (rooted/unrooted rigidity, uniform generator Φ_n) | §1.1, E1 | PROVEN-HERE |
| Lemmas RM, RM* (root matching, same configuration / same data) | §1.2, §1.6 | PROVEN-HERE |
| Lemma MG (merge across a slab), Lemma FP (patching, R-independent constant) | §1.3-§1.4, E1 | PROVEN-HERE |
| Lemmas C′, D′ (difference versions of NSL C, D) | §1.5 | PROVEN-HERE |
| **Lemma RFP (relative, root-preserving patching; C_RFP independent of R)** | §1.7 | PROVEN-HERE |
| Complex convention; F7 re-derived | §2 | PROVEN-HERE (convention + verification) |
| CONV′, SC-cut, ℬ/𝒥 maps; **Lemma KC** (CONV G/s-slots); **Lemma DKC** (ND) | §3.2-§3.3, E2 | PROVEN-HERE |
| **Proposition PAR** (parametrix on representations, exact error representation) | §3.4 | PROVEN as an implication |
| **Corollary GP′** (bounded compatible error operator; exact right inverse; (N1-nd)) | §3.5 | PROVEN as an implication |
| Proposition NK′ + Lemma T | §4.2 | PROVEN as an implication |
| Depth-induction start | §4.3 | PROVEN as an implication |
| **AP′** (real a priori estimate), **UQ′** (real uniqueness via RFP) | §4.4-§4.5 | PROVEN as implications |
| **Theorem OFF′** (BFT-0/1/2 + BFT-5 (b) off 𝒞_glob; real uniqueness; complex existence/holomorphy) | §4 | PROVEN as an implication (§4.7) |
| **Theorem ID′** (identification clause off 𝒞_glob, Balaban convention) | §5 | PROVEN as an implication |
| **Theorem BFT3-off** (E-part + gauge-invariant local functionals), Proposition GPW | §6 | PROVEN as implications; slice-coordinate form ARGUED |
| Proposition HINV ((H-inv) on the full class) | §7.2 | PROVEN as an implication |
| Obstruction to frame-by-frame transfer of BFT4a-glob | §7.3 | PROVEN-HERE (as stated) |
| Theorem C0-red ((c₀) ⇐ (GL) + transplanted BFT4W55 §6) | §7.4 | identity steps PROVEN; estimate steps ARGUED; (c₀) OPEN |
| (GL) via local critical points + (LUD) | §7.5 | ARGUED |
| (LOC-min) consumer bridge | §7.6 | OPEN (stated) |
| Boxes (BL-D)/(BL-F) | §8.1, E3 | OPEN (missing input named) |
| Tori T < T_* | §8.2 | not needed by BFT; OPEN |

### 12.2 Verdicts on prior claims (§10)
| # | Claim | Verdict |
|---|---|---|
| Q1 | OFFGLOB55 Lemma RG ARGUED | CONFIRMED (proved: RG′) |
| Q2 | OFFGLOB55 Lemma FP ARGUED | CONFIRMED (proved: FP) |
| Q3 | OFFGLOB55 Proposition UQ "PROVEN as an implication" | REFUTED as a proof (= Codex F8); conclusion proved as UQ′ |
| Q4 | OFFGLOB55 Proposition AP on the complex class | REFUTED (= Codex F7); real form proved as AP′ |
| Q5 | OFFGLOB55 Theorem GP | NOT-VERIFIED as stated (= Codex F6/F9); replaced by PAR/GP′ |
| Q6 | OFFGLOB55 CONV G-/s-slots ARGUED | CONFIRMED (proved: KC) |
| Q7 | OFFGLOB55 (ND) ARGUED | CONFIRMED (proved: DKC) |
| Q8 | OFFGLOB55 Lemma NE ARGUED | NOT-VERIFIED (not needed) |
| Q9 | OFFGLOB55 (W-comm)^σ at frame backgrounds "O(η/R)" | NOT-VERIFIED (not needed; O(η) suffices) |
| Q10 | OFFGLOB55 W-mult^σ off 𝒞_glob | CONFIRMED |
| Q11 | OFFGLOB55 P13 "frames suffice; NSL in frame coordinates" | CONFIRMED (now supplied: §1-§5) |
| Q12 | OFFGLOB55 §6.7 "Not delivered: …" | CONFIRMED as status then; superseded as listed |
| Q13 | BFT4B55 Theorem T0 | NOT-VERIFIED (= Codex R4/R17) |
| Q14 | BFT4B55 "with the same bounds" (centred) | REFUTED (= Codex R3: factor 2) |
| Q15 | BFT34_55 §1.3 off-𝒞_glob scope list | CONFIRMED as status then; superseded |
| Q16 | BFT4W55 §8 item 2 | CONFIRMED as status then; superseded for BFT-0, not for BFT-4 |
| Q17 | HANDOFF row "BFT off 𝒞_glob" | CONFIRMED as status then; update in §13 |
**Counts (prior claims Q1-Q17): CONFIRMED 10, NOT-VERIFIED 4, REFUTED 3.** Every REFUTED agrees with an on-disk Codex verdict.

## §13. For the lead (nothing here is banked; Codex first)
1. **The item Codex called most dangerous is proved here:** Lemma RFP (§1.7) — relative, root-preserving frame patching with an
   R-independent constant — and with it **UQ′** (real uniqueness modulo root-trivial gauges, §4.5) by a q-contraction over an
   admissible, compact, self-mapped set of matched frame states. The mechanism: root matching pins the transition difference Δτ to
   zero at every root of every overlap, so the alignment cost is O(q), not O(η).
2. **GP's interface defect is repaired** (§3): the parametrix is defined on representations; PAR gives an *exact* error representation;
   at a critical point ℰ_Z is a bounded linear endomorphism of Rep_cc(Z) (Corollary GP′) — the object Codex OFFGLOB item 5 made the
   condition for banking GP's Neumann/kernel consequences. NK is run on representations (NK′), with linear convergence.
3. **The complex convention is fixed** (§2): real frames for real configurations only; complex data by holomorphic continuation in fixed
   real frames; E_k^br is the unique continuation of the real value; no complex uniqueness is claimed (F7's configuration is consistent
   with this).
4. **OFFGLOB55's five ARGUED lemmas:** RG, FP → proved (RG′, MG, FP); CONV G/s-slots → proved (KC); (ND) → proved (DKC, chart form,
   Codex's sign); W-mult^σ → confirmed; (W-comm)^σ "O(η/R)" and NE → **not needed** (PAR prices the background part at O(η) from
   aggregate bounds). New and possibly the first thing for Codex to test: E2 (iv)'s claim that §3-§4 use only aggregate bounds and
   per-contour analytic facts Codex itself reconstructed — **not** premise (R).
5. **Delivered as implications (pending Codex):** Theorem OFF′ (BFT-0/1/2 + BFT-5 (b) on the full small-curvature class, real
   uniqueness, complex holomorphy), Theorem ID′ (identification clause off 𝒞_glob, Balaban convention), Theorem BFT3-off (E-part and
   gauge-invariant local functionals, rates μ_W/n), Proposition HINV ((H-inv) for E_k^br on the whole class).
6. **Not delivered, with the precise missing input:** BFT-4 (c₀) — reduced (Theorem C0-red) to **(GL)**, a *local* reference
   configuration (candidate: glued local 𝒞_glob-type critical points, needing **(LUD)**), plus BFT4W55 §6 transplanted to PAR pieces
   (ARGUED); §7.3 proves why a direct frame-by-frame transfer cannot work. The HIST consumer bridge **(LOC-min)** is OPEN and needs a
   free-boundary box theorem. **Boxes:** OPEN, missing **(BL-D)/(BL-F)** (the linear package with Dirichlet/free boundary). **Tori
   T < T_*:** not needed by BFT as stated (T_* := 4R + 6 is an admissible T_0); OPEN near nontrivial flat holonomy. **RLARGE's (BG)_k**
   needs a background for data small-field only near a region — a localised background **(LOC-bg)** that no global-class BFT provides.
7. **Suggested Codex order:** (a) Lemma RFP and UQ′ (§1.7, §4.5); (b) PAR's identity (iii)-(iv) and the representation maps of §3.2
   (CONV′ incl. E2 (i), SC-cut, ℬ/𝒥); (c) KC/DKC's exact identity K′_yλ(b) = −[y(b), λ(b^−)] − (ψ_+(ad_{y(b)}) − 1)(dλ)(b) and the
   (G)/(s) splits; (d) AP′'s use of RM* + NSL + OC; (e) E2 (iv) vs Codex BFT4W W1; (f) Theorem ID′'s (I3′) depth-(j + 1) frame
   construction.
8. **PROOF tally:** no change (lane-level). **HANDOFF row "BFT off 𝒞_glob":** "Theorem OFF′ (OFFGLOB2_55, pending Codex): BFT-0/1/2,
   BFT-5 (b), identification (ID′), BFT-3 (gauge-invariant form) on the full small-curvature class as implications; open: BFT-4 (c₀)
   reduced to (GL)+(LUD), (LOC-min), boxes (BL-D/F), (LOC-bg)". **HANDOFF row "BFT-4":** replace "OFFGLOB2_55 on (c₀) (running)" by
   "(c₀) reduced to (GL) (OFFGLOB2_55 §7), (H-inv) proved; open."
*Check record:* no numeric check was run. I considered an exact finite check of KC's (G)/(s) splits and judged it unable to decide
(the per-plaquette split is linear algebra that cannot fail once the λ(base)-coefficient is defined as the response to constant λ;
the content of KC is the absence of a power of n, which a d = 2, k ≤ 3 run would only illustrate). No `checks/o2_55_*` files exist.
Files written: this file only. No git.

*Final status line (appended after `date -u`).*
Final status line timestamp: 2026-10-29T06:40:05Z — Theorem OFF′, ID′, BFT3-off, HINV: PROVEN as implications (pending Codex); RFP/UQ′/PAR/GP′/KC/DKC: PROVEN-HERE or as implications; (c₀): reduced to (GL); boxes: OPEN. Prior claims: CONFIRMED 10, NOT-VERIFIED 4, REFUTED 3.
