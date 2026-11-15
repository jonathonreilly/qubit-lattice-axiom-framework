Reviewer model: claude-opus-5-5

# BFT4W55 — BFT-4's local inputs on 𝒞_glob, written out (worker file, Opus 5.5)

UTC start: 2026-10-29 02:46 (from `date -u` at session start).
Role: worker (brief `queue/bft4w.md`; shared rules `REVIEW_BRIEF_55.md` apply). No git. This file and
`checks/b4w55_*` are the only files written. Append-only.

## 0. PRE-STATED (written before any derivation)

Targets, in the order the brief sets:

T1. **(H3)_m** — weighted locality of the cc-projected source map (localised ROW^{(σ)}, CB, HR bounds),
    as a theorem with a complete proof using only the [S26-BANKED] inputs at the top of PROOF.md plus
    what is proved here.
T2. **(W-comm)^σ_J** and **W-mult^σ** — lane B's GAP-1 family in σ-weighted form, written in full; and
    the consequent m = 0 → m > 0 upgrade of BFT34_55's Corollary RW-cc-walk (independent route to GV-E_m).
T3. The σ-pair forms of lane B's (f) (localised remainder bounds) and (E3^∇) (per-cube cubic trapezoid
    defects), and the re-run of lane B §10.8 clause (d) (s ≡ 1 identity, splitting) on the P_cc-projected
    family, with constants uniform in the RG step k and in T.
T4. Assembly: BFT-4 (a) on 𝒞_glob as an implication, every input named with its status; items not closed
    named with the reason.

What would count as a refutation (of a target, or of the BFT34_55 reduction that feeds it):
R1. An explicit configuration / test function for which a stated weighted-locality bound fails by more
    than its constant (e.g. the cc-projection is not exponentially local at the claimed rate, or its decay
    rate is not uniform in k or in T): a counterexample to (H3)_m as stated.
R2. A commutator [W_σ, ·] or a weighted product that is not bounded by the claimed O(σ) (or claimed
    constant) uniformly in the lattice size/level — e.g. a non-local P_cc whose commutator with a weight
    e^{σ d} grows with the volume: a counterexample to (W-comm)^σ_J / W-mult^σ.
R3. A per-cube trapezoid defect or remainder that is not geometric per level, or whose constant grows
    with k or T: a counterexample to the σ-pair (f)/(E3^∇) forms.
R4. The s ≡ 1 identity of §10.8 (d) failing for the P_cc-projected family (the projection does not
    commute with the splitting, or produces a non-local term): a counterexample to the clause transfer.
R5. Any input that BFT34_55 or this file treats as banked but that is NOT in the [S26-BANKED] block, or
    that a Codex review refutes: the implication then fails to be an implication from banked inputs.
R6. A symbol collision (same symbol, two objects) on which a step depends: the step is NOT-VERIFIED
    until the objects are matched by file + locating string.

Verdict vocabulary (rules §5): CONFIRMED / NOT-VERIFIED / REFUTED for claims inherited from files; for my
own new statements: PROVEN-HERE (complete proof in this file), ARGUED (sketch only), OPEN, FALSE
(counterexample given).

---

## 1. Read record, inputs I may use, symbols pinned (appended 2026-10-29 ≈03:25Z; written after §0)

**Read (bounded ranges, located by string).** REVIEW_BRIEF_55.md (all); queue/bft4w.md (all); BFT34_55.md (all 670 lines);
PROOF.md l.1-40 ("[S26-BANKED]" block, all bullets through the 02:43Z batch); KFACTOR_OFF55.md §1-§4 ("1.1 Setting" through
"Exponent bookkeeping", l.66-424); CODEX_REVIEW_KOFF.md §4-§5 and "Exactly what may be banked" (l.267-550, 714-754);
COFM55.md §1-§2 (l.100-190); GV55.md §1-§4 (l.94-420); CODEX_REVIEW_GV.md "Exactly what may be banked"; CODEX_REVIEW_GSHARP.md
§1, §2.5, §6 and "Exactly what may be banked"; BFT_A.md l.18-60 ("1.1"-"1.4"), l.200-260 ("3.9 Theorem BA", "3.10 Outside
𝒞_glob", BA-11, BA-12 CEN1), l.380-440 ("GAP 1 (F3)", "[RBA1-fix] The corrected pair"), l.444-500 ("7.1 Setting LIN", "7.2
Norms", BL-1, BL-2 statement), l.598-616 ("8.2 BL-2: PROVEN-HERE"); BFT_B.md l.21-40 (§0), l.1029-1484 (§9-§10: Setting W,
(H-RW^∇)_k, W-ls/W-cut/W-mult/W-pair, Theorem RW^∇_k, Construction BB-bond_k, Theorem BB-mix_k, §10.9), l.1584-1640 (§12.0-
§12.1), l.1711-1780 (§13.1-§13.2: W-gauge0, RW^∇_k-Π), l.2016-2090 (§15.0-§15.1: Setting EΠ, EP-alg, EP-bd, EP-opt, EP-rec);
REVIEW_BFT_B_S3.md (C.2, D.2 and tally); BGT55.md (strings "RW♯"; not used); **CODEX_REVIEW_BFT34.md (all 262 lines; complete:
it ends with its "Exactly what may be banked" item 5; it appeared at 23:06 local mtime and I read it at ≈03:20Z, before any
derivation in §2 onward)**. Corpus (data only, cited by id + section, nothing copied): 1108.1335 §2.4 (random walk expansion
from local Neumann inverses and a parametrix with a quadratic partition of unity; commutator terms K_z of size O(M^{-1})),
§2.5 and §4.5 (weakened propagators G(s) = Σ_ω s^ω G_ω with complex |s_□| ≤ M^{1/2}; localisation by interpolation in s and
Cauchy bounds; Lemma 18: only connected Z survive; Lemma 20: tree-length inequality), §4.6 (cluster expansion);
1212.5562 §2.5 (multiscale random walk), §3.7 (a "more local minimizer" built from the weakened propagator), §3.13
(localisation lemma 3.15). These are the hard-scheme map of what §4-§7 below re-derive on the soft composite structures.

**What I build on (the brief: [S26-BANKED] plus what I prove).** From the [S26-BANKED] block of PROOF.md:
- **(K)** Theorem K^{(σ)} (corrected), with HR (i)-(v), CCP (a)-(d), SG, ROW^{(σ)} with (LA-1′) and Codex's local analytic
  completion, CB (σ > 0): Codex KOFF items 1-5 — **conditional on the named lane-A linear package and on (GV)**.
- **(GV)** Proposition GV-E (Codex GV item 2) and the corrected K + GV-E contraction ("Theorem BFT-E", Codex GV item 4):
  the unique full critical point x(B) in the slice ball, its (2, 2+σ, 1) regularity, holomorphy of x(B) and of the
  **composite critical value**; identification with the per-level E_k^br **NOT-VERIFIED** (Codex GV items 4-5, (NSL)).
- **(GVm)** Proposition GV-E_m (Codex GV item 6), with the small-torus factor corrected to e^{8μ} (Codex BFT34 R4).
- **(EP)** EP-alg algebra (Λ(Dμ) = −μ, Π_E = I + DΛ, ΛΠ_E = 0, X = S_E ⊕ 𝒢_0), Ker H = 𝒢_0, EP-opt, EP-bd at zero
  weight (‖Π_Ev‖_𝔐 ≤ C_Π‖v‖_𝔐 for every v, T ≥ 5, residuals unchanged), finite ℓ¹ reach of Π_E: Codex GSHARP item 1, §2.5, §6.
- **(CC)** CC-INV / LIN^{(σ)} (gauge-invariant half, cc sources, weight σ): Codex KOFF item 5; CC-INV_m, TOP-cc_m: Codex COFM
  items 2-3.
From CODEX_REVIEW_BFT34 (cross-family checked, not yet in the [S26-BANKED] block; I use only its "may be banked" items and
re-derive each use): item 3 (corrected RW-cc algebra, every commutator piece c_□ is cc, CCL's 216), item 5 (the connected-bond
combinatorial bound given an analytic splitting family). **Anything BFT34_55 claims that Codex BFT34 refutes (R2's σ = 1 sum,
R6's exponent, R7's weight radius and conjugation argument, R10's attachment cost) is not used.** Everything else from
BFT34_55, lane B and lane A that I use is re-derived below (or named as a premise).

**Symbols pinned (systemic defect 1).** Within this file:
- **μ ≥ 0** = the exponential spatial weight rate (BFT34_55's "m"; renamed per Codex BFT34 R2). **q := k − 1 − l** = a depth
  (integer). **m is not used.** w(z) := e^{μf(z)}, f a 1-Lipschitz function of coarse positions in the **ℓ¹** coarse torus
  distance d_1 (COFM55 §1). An ℓ^∞ radius a is an ℓ¹ radius ≤ 4a (d = 4; Codex BFT34 R7.1, Codex GSHARP §6).
- **σ ∈ (0, 1]** = KFACTOR_OFF55's residual-weight parameter (θ_w^r = 2 + σ). Lane B's BB-mix_k uses "σ := 2^ds̄" — renamed
  here **c_v := t_X2^ds̄** (the view constant). 0 < α < θ ≤ σ ≤ 1 throughout; θ₀ ∈ (α, σ], θ₀ < 1 as in GV55/Codex KOFF §5.1.
- **‖B‖_D** is written out (KFACTOR's "s"); **s = (s_b)** denotes only lane B's complex bond variables, s̄ their radius.
- **η** = a radius of a ball in 𝔐^{(σ)} (KFACTOR's ROW/CB bounds are in terms of η); cube cutoffs are always written with
  their cube, **η_Q**. h_l := L^{−(k−l)} (one own level-l step in coarse units).
- **K** = the finite local Lipschitz constant of Codex KOFF §5.3 ("N^(σ)(difference) ≤ K(η+η′+‖B‖_D)‖x−x′‖_(σ)"); lane B's
  polymer ratio 2^{41}/(s̄ − 1) is renamed **K_pol**.
- **R** = box side; **R(X)** = polymer activity; **R̃** = walk remainder; **R_k** := E_k^br − S_W.
- **G_♯** := G_inv(σ) + G_gv (K^{(σ)}'s response constant, cc sources, B = 0) — not BFT34_55's G_♯(m).
- **E_k^br** := 𝔉_k(x(B); B), the **composite critical value** (Balaban's convention; BFT34_55 §1.1; Codex GV item 4). Every
  BFT-4 statement below is about this object; its identification with the per-level E_k^br needs (NSL)_j (OPEN).
- **cc** := composite-co-closed, D^⊥(S) = 0 (KFACTOR_OFF55 §1.1); **P_cc := 1 − P^TD^⊥** (HR routing).
- **J(j) := Σ_l π_l(j_l)**, π_l(j) := L^{3(k−l)}·sup_own|j| (d = 4); weighted π_{l,μ}(j) := L^{3(k−l)}sup_b w(b)|j(b)|.
- Lane B's local-sup factors **t_X = 4** (𝔐-type norms: four sups per level) and **t_Y** (number of sup-type summands of
  the source norm, here t_N := 3 for ‖G^c_0‖_∞, [G^c_0], ‖s‖_{R(σ)}; J is treated separately, §2.3).

*(Timestamp correction for §1's heading: `date -u` immediately before that append printed 03:15:57Z, not ≈03:25Z.)*

---

## 2. Conventions, weighted norms, two transfer lemmas (appended 2026-10-29 ≈03:21Z)

### 2.1 Positions — Convention C (centred). Load-bearing; see Proposition CORNER (§4.2)
A level-j site Z (0 ≤ j ≤ k) is placed at the coarse position of its **level-0 image** (the centre of its level-j block):
pos(Z) := L^{−k}(L^jZ + ((L^j − 1)/2)𝟙). By HR's nesting (KFACTOR_OFF55 §3.3, "Roots are block centres, hence nested") the
level-0 image of a level-(j+1) site is the image of the central level-j site of its block, so pos is consistent across levels.
A link / plaquette sits at the midpoint / centre of its endpoints' positions; the level-(l+1) coarse link c = (X, μ) sits at
**m_c = pos(c_X) + (L/2)h_le_μ**, c_X the central level-l site of X's block — exactly the centre of its S4′ contour family.
Cutoffs φ act on displacements by (φx)_j(b) := φ(m_b)x_j(b) (j < k; x_k := 0), and on source representations **slotwise**
(Codex BFT34 R5: never on the raw covector): G_0(p) ↦ φ(m_p)G_0(p), s_l(c) ↦ φ(m_c)s_l(c), j_l(b) ↦ φ(m_b)j_l(b).
Two consequences used below: (i) ev^{(l)T}(φ·g) = φ·ev^{(l)T}g exactly (a level-l site and its level-0 image share their
position), which makes CCL's cancellation exact; (ii) the centring cancellation CEN1 (§4.1) holds exactly.
The lane's weight convention ("coarse position of a level-l object = L^{l−k}·(base point)", COFM55 §1) is the
**lower-corner** placement (Convention K). For the weights e^{μd_1} the two differ by < ½ coarse unit in ℓ^∞, i.e. a factor
≤ e^{2μ}, harmless. For the **cutoff action** they are not interchangeable at σ > 0 (Proposition CORNER).

### 2.2 Weighted norms (base-point form) and their comparison with COFM55's product form
w(z) := e^{μf(z)}, f 1-Lipschitz for the ℓ¹ coarse torus distance d_1, μ ≥ 0. Every local quantity is multiplied by w at
its **base point**: a value at its link/plaquette/coarse-link position; a gradient at the lower link; a Campanato oscillation
on a box B at the box corner z_B (COFM55's [H]_{α,m}); a pointwise Hölder quotient for an ordered pair (z, z′),
|z − z′|_∞ ≤ 1, at z. So, with ||H||_{∞,μ} := sup_z w(z)|H^c(z)|, [H]_{α,μ} := sup_B w(z_B)ρ^{−α}Osc_2(H^c; B) and
[H]^∞_{α,μ} := sup_{(z,z′)} w(z)|H^c(z) − H^c(z′)|/|z − z′|_∞^α:
- **||x||_{(σ),μ,f}** := max_{j<k}[ ||x^c_j||_{∞,μ} + ||∇^cx^c_j||_{∞,μ} + [∇^cx^c_j]_{α,μ} + L^{(1+σ)(k−1−j)}||r^c_j||_{∞,μ} ];
  "hom" means x_k := 0 in r_{k−1}; data-inclusive means r_{k−1} = Qx_{k−1} − B (Codex KOFF §5.3).
- **N^{(σ)}_{μ,f}(S)** := ||G^c_0||_{∞,μ} + [G^c_0]^∞_{α,μ} + ||s||_{R(σ),μ} + J_μ(j), ||s||_{R(σ),μ} := max_l L^{(1+σ)(k−1−l)}||s^c_l||_{∞,μ},
  J_μ(j) := Σ_l π_{l,μ}(j_l). At μ = 0 this is KFACTOR_OFF55's N^{(σ)} with the pointwise instead of the Campanato
  Hölder seminorm on G_0; the two are equivalent by BL-C (COFM55 §1, "equivalent … by BL-C").
- **Comparison with COFM55's product form** ||wG^c_0||_∞ + [wG^c_0]^∞_α (Codex BFT34 R2 asks for it explicitly). For
  |z − z′|_∞ ≤ 1, d_1(z, z′) ≤ 4|z − z′|_∞, so |w(z) − w(z′)| ≤ 4μe^{4μ}|z − z′|_∞w(z′), and since |z − z′|_∞^{1−α} ≤ 1,
  **[wG^c]^∞_α ≤ [G]^∞_{α,μ} + 4μe^{4μ}||G||_{∞,μ} and [G]^∞_{α,μ} ≤ [wG^c]^∞_α + 4μe^{4μ}||G||_{∞,μ}.** (Write
  wG(z) − wG(z′) = w(z)(G(z) − G(z′)) + (w(z) − w(z′))G(z′), and the same with the roles exchanged.) So every statement
  below in base-point form holds in COFM55's form with constants multiplied by at most 1 + 4μe^{4μ}.

### 2.3 Lemma LD (local domination transfers to weights) — PROVEN-HERE (elementary)
Let T be linear (or multilinear) between spaces carrying norms of the above kind (finite maxima/sums, over levels and
component types, of suprema of local quantities). Suppose that for every output local quantity Ω with base point z_Ω,
  Ω(Tu) ≤ Σ_κ a_{Ω,κ}·sup{ Ω′_κ(u) : Ω′_κ an input local quantity of type κ with d_1(z_Ω, z_{Ω′}) ≤ ρ },
with type coefficients a_{Ω,κ} ≥ 0 depending only on the type and level of Ω. Then every bound "output norm ≤ F(input
norms)" obtained from these pointwise inequalities by taking suprema, maxima and sums **holds verbatim in the weighted norms
with every input norm multiplied by e^{μρ}**. *Proof.* w(z_Ω) ≤ e^{μρ}w(z_{Ω′}) whenever d_1(z_Ω, z_{Ω′}) ≤ ρ (f is
1-Lipschitz); multiply the pointwise inequality by w(z_Ω) and take the same suprema/maxima/sums. ∎ For a p-linear T the
factor is e^{pμρ} and every input carries its own weight (§3, part (c)).
*What this lemma does not do* (Codex BFT34 R7.3): it never multiplies a field by e^{μf}; weights act on local quantities
only. Hence it needs no statement that e^{μf} preserves the cc class (it does not, Codex BFT34 R7.2).

### 2.4 Lemma OV (overlaps; J with level profiles) — PROVEN-HERE (elementary; lane B's W-ls with RW3-1, plus profiles)
(a) If ||·|| is a max over levels of a sum of t suprema of local quantities of read radius r_N (𝔐^{(σ)}: t_X = 4; the
three sup-type summands of N^{(σ)}: t_N = 3), and every ball B_∞(z, r_N) meets at most n of the supports of u_i, then
||Σ_iw_iu_i|| ≤ t·n·max_i|w_i|·max_i||u_i|| (weighted or not). (b) **J is a sum over k levels of suprema and is not
equivalent to a local-sup norm uniformly in k.** Instead: if π_{l,μ}((u_i)_l) ≤ b_l·M for all i and l, with Σ_l b_l =: B_b
independent of k, and each point lies in at most n supports, then J_μ(Σ_iw_iu_i) ≤ n·max|w_i|·M·B_b. *Proof.* (a) lane B
§10.1 termwise. (b) π_{l,μ}(Σ_iw_i(u_i)_l) ≤ n·max|w|·max_iπ_{l,μ}((u_i)_l) ≤ n·max|w|·b_lM; sum over l. ∎
(b) is what BFT34_55 called "W-ls for J with summable profiles"; below it is used **only** for the global walk (§5.3-5.4),
whose outputs come with explicit profiles (§4.4). The cube-indexed family (§6) uses finite sums and the triangle inequality,
so it never needs a profile.

---

## 3. Theorem H3 — (H3)_μ, its 1-Lipschitz form and the multilinear vertices (target T1) (appended ≈03:40Z)

### 3.1 Setting and statement
Setting (K) of KFACTOR_OFF55 §1.1 (𝒞_glob coordinates, trivial-chain centring, d = 4, L ≥ 3 odd, κ_l ∈ [κ_−, κ_+], k ≥ 1,
T ≥ 3, 0 < α < θ ≤ σ ≤ 1). F(x; B) := 𝔉_k(e^x; e^B) (TOWER-VAR), H := Hess_xF(0; 0), and
  **Y(x; B) := Hx − ∇_xF(x; B)** (represented slotwise, §3.2), **S̃(x; B) := P_ccY(x; B).**
This is KFACTOR's S̃: with 𝔑^0 := Hx − NB − ∇F, NB + 𝔑^0 = Y, and P^TD^⊥(𝔑^0) = P^TD^⊥(Y) because D^⊥(NB) = 0 (CCP (a)).
η_* := the fixed local analytic radius of Codex KOFF §4.3 (finite, not computed). Complex x with ||x||_{(σ),hom} ≤ η_*/4,
complex B with ||B||_D ≤ η_*/4; write η := ||x||_{(σ),hom} + ||B||_D.

> **Theorem H3.** There are finite constants K_1, S_1, V_{p,w} (depending on N, L, κ_±, α, θ, σ and the local analytic
> completion; **not on k, T, μ or f**) such that, with the absolute ℓ¹ read radius **ρ_S := 20**, for every μ ≥ 0 and every
> 1-Lipschitz f:
> - **(a) linear vertex:** ||D_xS̃(x; B)u||_{N^{(σ)},μ,f} ≤ e^{ρ_Sμ}K_1·η·||u||_{(σ),μ,f};
> - **(b) data vertex:** for every level-k link y and b ∈ su(N)⊗ℂ, ||∂_{B_y}S̃(x; B)[b]||_{N^{(σ)},μ,d_1(·,y)} ≤ e^{ρ_Sμ}S_1|b|;
> - **(c) multilinear vertices (p + w ≥ 2):** ||D^p_xD^w_BS̃(x; B)[u_1..u_p; b_1δ_{y_1}..b_wδ_{y_w}]||_{N^{(σ)},μ,F} ≤
>   V_{p,w}e^{(p+w)ρ_Sμ}Π_i||u_i||_{(σ),μ,F_i}Π_j|b_j| whenever F(z) ≤ Σ_iF_i(z) + Σ_jd_1(z, y_j) for all z;
> - **(d)** every value of every derivative in (a)-(c) is cc.
>
> (a) with f = d_1(·, y) together with (b) is BFT34_55's **(H3)_m** (m → μ, c_r → ρ_S, Λ(s) → K_1(2C_0 + 1)||B||_D on 𝔅);
> (a)-(c) for every 1-Lipschitz f are its **(H3)^Lip_m** including Proposition TREE's "multiplicative locality".
> **Status: PROVEN as an implication of the banked per-density bounds** (Codex KOFF items 1, 3, 4 with §4.3's local
> analytic completion; HR (i)-(v)); the one reading step is named in 3.4.

### 3.2 Density decomposition and slot representation (the banked structure, restated)
F = Σ_{D∈𝒟}D with 𝒟 = {level-0 Wilson plaquette densities D_p} ∪ {soft densities D_c := κ_lφ̂_c, c a level-(l+1) link,
0 ≤ l < k}; Y = Σ_DY_D, Y_D := H_Dx − ∇D(x; B), H_D := Hess D(0; 0). Slots (LA-3; Lemma SG with (LA-1′)):
- D_p: divergence slot G_0(p) = c_wdx_0(p) − ∇w(F_p) (= −c_wq_p + O(F³)); plain level-0 slot −(Dq_x)^T_p∇w(F_p) on ∂p.
- D_c (level l): residual slot s_l(c) = κ_l(r^{hom}_l(x)(c) − Ψ_c), Ψ_c = Π(−Θ_c^*), Θ_c = e^{ρ_c} − 1; plain slot −κ_lE_{l,c} at the
  level-l links of the contour support N(c) and at c. Only the top densities (l = k − 1) depend on B, D_c on B_c alone.
Each slot of Y_D sits at a base point of supp D and depends on (x, B) only through the variables of supp D. The divergence
and residual slots have D = 0 slotwise (⟨d*G, Ξλ⟩ = ⟨G, d dλ⟩ = 0; r_l(Ξλ) = 0), so D^⊥(Y) = D^⊥(plain slots)
(Codex BFT34 R5: slotwise multiplication keeps this).

### 3.3 Lemma FR (read radii) — PROVEN-HERE (counting)
(i) **diam_1(supp D) < 5** (coarse ℓ¹) for every density. A soft D_c, c = (X, μ) at level l + 1, reads the level-l links on
the contours c_X → y → y + Le_μ → c_X + Le_μ (y ∈ B(X)) and x_{l+1}(c); all lie in the box [c_X − h𝟙, c_X + h𝟙 + Le_μ]
(h := (L − 1)/2, own level-l units), whose ℓ¹ diameter is (2L − 1) + (d − 1)(L − 1) = (d + 1)L − d = 5L − 4 own steps, i.e.
(5L − 4)h_l ≤ (5L − 4)/L < 5 coarse (h_l ≤ L^{−1}). Wilson: < 2L^{−k}. [b4w55_1 P5 measures max_{c,a}|m_a − m_c|_1 = d + 1 own
steps in d = 2, 3, inside the bound d(L−1)/2 + L/2 = radius of this box about m_c.]
(ii) **Routing.** P^TD^⊥ maps a plain current at a link to charges at the incident sites (½h_l away) and routes each charge
inside its level-k cell (HR: γ(Z) lies in Z's parent block, all ancestors' blocks are nested in the cell), so every output
base point is within d_1 ≤ 4 + ½ of every input base point it reads.
(iii) Hence every output local quantity of S̃ (and of each derivative) with base point z reads (x, B) only at base points
within d_1 ≤ 5 + 5 = 10 of z; a pointwise Hölder partner adds ≤ 4 (|z − z′|_∞ ≤ 1), and an input Campanato box of side ≤ 1
adds ≤ 4: **every input local quantity used has its base point within ρ_S = 20 of z.** ∎

### 3.4 Lemma PW (pointwise vertex bounds from per-density size bounds) — PROVEN-HERE, given the reading step (R)
*Local constraint sets.* For a density D (or a pair D_p, D_p′ for a Hölder quotient) let 𝒦_D(r) be the set of complex
(x|_{supp D}, B|_{supp D}) all of whose input local quantities based in or at supp D (values, gradients, Campanato boxes meeting
supp D, residuals at the coarse links of supp D, each in the 𝔐^{(σ)} normalisation) are ≤ r, and |B_c| ≤ r. 𝒦_D(r) is the
r-ball of a seminorm on finitely many complex variables: 𝒦_D(r_1) + 𝒦_D(r_2) ⊂ 𝒦_D(r_1 + r_2), t𝒦_D(r) = 𝒦_D(|t|r).
*Reading step (R) — what the banked bounds say.* **Every bound of ROW^{(σ)} (a)-(b) and of Codex KOFF §4.3 (1)-(3) and its
Wilson estimates is a per-density (per-pair) bound on 𝒦_D(η), η ≤ η_*:** with the level factor λ_D := 1 for divergence and
residual slots in their own normalisation (residual: L^{(1+σ)q}|s^c_l(c)|, q = k − 1 − l) and λ_D := L^{−σq} for plain soft
slots in π-normalisation, each slot of Y_D (and each Wilson Hölder pair quotient) obeys |slot| ≤ c_Dλ_Dη² on 𝒦_D(η), except
the top residual slots, which carry the data linearly: |slot| ≤ c_D(η + η²). Locating strings: ROW^{(σ)} (a) "own size ≤ κ·2p_L
s_l·|r_l|" (a per-coarse-link bound in s_l = sup over N(c), |r_l(c)|); SG (b) "π_l(E_l|_l) ≤ L^{3(m+1)}C_Ec_Lp_LL^{−(m+1)}η·2|ρ|"
(per c, coefficient × Θ_c); Codex KOFF §4.3 (1) "|ρ_l−r_l| ≤ C h³η²" (per c), (2) per link, (3) per c, and the Wilson
estimates ("translate all its finitely many arguments together") per plaquette/pair. Each proof uses only the own-unit sizes of
the variables of one density — membership in 𝒦_D(η). (This is a reading of those proofs; I found no step that uses a
non-local quantity.)
*Claim.* For (x, B) ∈ 𝒦_D(η), η ≤ η_*/4, and directions u_i ∈ 𝒦_D(1) (B-component 0), b_j ∈ ℂ^{N²−1} at top links of supp D:
- (P1) |D_xY_D(x; B)[u]| ≤ 8c_Dλ_D·η·(1 + 1/η_*);
- (P2) |∂_{B_c}Y_D(x; B)[b]| ≤ 4c_D(1 + η_*)|b| (top densities D = D_c only; zero otherwise);
- (P3) |D^p_xD^w_BY_D(x; B)[u_1..u_p; b_1..b_w]| ≤ c_Dλ_D(η_* + η_*²)(2(p + w)/η_*)^{p+w}Π|b_j|.
*Proof.* (P1) Put g(t, z) := Y_D(tx + zu; tB) for |t| ≤ η_*/(2η), |z| ≤ η_*/2: the argument lies in 𝒦_D(η_*), so
|g| ≤ c_Dλ_D(η_*² + η_*) (the η_* term only for top residual slots). h(t) := ∂_zg(t, 0) = D_xY_D(tx; tB)[u] obeys
|h| ≤ 2c_Dλ_D(η_* + 1) by Cauchy in z, and **h(0) = D_xY_D(0; 0) = H_D − Hess D(0; 0) = 0**; Schwarz in t on the disc of
radius η_*/(2η) gives |h(1)| ≤ (2η/η_*)·2c_Dλ_D(η_* + 1) ≤ 4c_Dλ_Dη(1 + 1/η_*)·… ≤ 8c_Dλ_Dη(1 + 1/η_*). (P2) Cauchy in the
single complex block B_c on a disc of radius η_*/2. (P3) Cauchy in the p + w distinct variables z_i, ζ_j of
g(z, ζ) := Y_D(x + Σz_iu_i; B + Σζ_jb_jδ_{y_j}) on radii η_*/(2(p + w)): the argument stays in 𝒦_D(η_*/4 + η_*/2) ⊂ 𝒦_D(η_*);
for distinct variables Cauchy has no factorial. ∎
The **level factor λ_D survives every derivative**, because Cauchy and Schwarz only divide by fixed radii of the local
constraint set; this is where the σ-pair's level decay passes from the sources (ROW^{(σ)}) to the vertices.

### 3.5 Lemma PWR (routing is pointwise) — PROVEN (HR's proofs read per block; Codex KOFF item 1)
For a plain current j and a level-i link b′ in the level-(i+1) block Y′: (iii) from u = ev^{(l)T}d*w, |V_i(Z)| ≤
2dL^{(d−1)(i−l)}sup_{∂(block of Z)}|w| (exact boundary telescope, ko55_1 A3) and (P^Tu)_i(b′) = Σ_{Z∈Y′, b′∈γ(Z)}V_i(Z) over
≤ M_γ sites, so the π_i-normalised value at b′ is ≤ 2dM_γ·sup_{cell}(π_l-normalised |w|); (iv) for level-0 w the same with
sup|w| replaced by the pointwise Hölder quotient of w^c over entry/exit pairs in the blocks of Y′ and the factor L^{−α(k−i)};
(v) bare charges likewise. All suprema are over the cell of b′ (Lemma FR (ii)).

### 3.6 Proof of Theorem H3
D_xS̃(x; B)u = Σ_D D_xY_D[u] − P^TD^⊥(Σ_D plain slots of D_xY_D[u]). Each output slot at base point z:
- *G_0 at p, and its Hölder pairs:* (P1) for D_p (pair densities for the quotients): ≤ 8c_W(1 + 1/η_*)η·𝒩_z(u), where 𝒩_z(u)
  := the largest input local quantity of u based within ρ_S of z (𝒩_z(u) ≤ ||u||_{(σ)}).
- *Residual slot at c:* only D_c contributes (routing makes plain currents only): L^{(1+σ)q}|·| ≤ 8c_S(1 + 1/η_*)η·𝒩_z(u).
- *Plain slot at a level-i link b′:* direct terms from the ≤ N_inc densities containing b′ (N_inc ≤ 2(d − 1) Wilson + the
  soft densities whose support contains b′, a bounded number by the block geometry of Lemma FR (i)), each ≤ 8c_S(1+1/η_*)
  L^{−σ(k−1−l)}η·𝒩(u) in π-normalisation at its level, plus the routed terms of Lemma PWR.
Summing the plain slots over levels exactly as in CB's proof (Codex KOFF item 4: the only level sums are Σ_qL^{−σq},
Σ_q(q + 1)L^{−σq} and Σ_qL^{−αq}, all finite for σ > 0 **including σ = 1**; no residual slot is ever summed over levels,
in line with Codex BFT34 R2) gives at μ = 0
  N^{(σ)}(D_xS̃(x; B)u) ≤ K_1η||u||_{(σ)},  K_1 := 8(1 + 1/η_*)[c_W(2 + N_inc) + c_S + N_incc_S(1 + 2dM_γ/(1 − L^{−σ}))/(1 − L^{−σ})
                                                + dM_γc_W/(L^α − 1)],
and every inequality used is pointwise with read radius ρ_S (Lemma FR (iii)). Lemma LD gives (a) for every μ ≥ 0 and every
1-Lipschitz f. (b): ∂_{B_y}S̃[b] = P_cc(∂_{B_y}Y_{D_y}[b]); all output base points lie within 10 of y; (P2) and HR (iii)/(v) at
l = k − 1 (one level of routing) give the unweighted size S_1|b|, and d_1(·, y) ≤ 10 on the support gives the weight
e^{10μ} ≤ e^{ρ_Sμ}. (c): (P3) per density, routing as in (a) (linear), and Lemma LD's multilinear form: for an output base
point z, each u_i is read at base points z_i with d_1(z, z_i) ≤ ρ_S and each data slot y_j has d_1(z, y_j) ≤ 10, so
e^{μF(z)} ≤ Π_ie^{μF_i(z)}Π_je^{μd_1(z,y_j)} ≤ e^{(p+w)ρ_Sμ}Π_ie^{μF_i(z_i)}. (d): HR (i) gives D^⊥(P^Tv) = v^⊥, so
D^⊥(P_ccS) = 0 for every representation S; every derivative of S̃ is P_cc of a derivative of Y (P_cc is linear and does not
depend on (x, B)). ∎
**What this removes.** BFT34_55 §1.5 recorded (H3)_m as "ARGUED (the localised form … is not written anywhere)". With
Theorem H3, BFT34_55's Lemma WD and Theorem BFT3-glob (both Codex-confirmed as implications, Codex BFT34 R1, R3) depend
only on (H1) and (H2)_μ; Proposition TREE (Codex BFT34 R9, conditional) depends only on (H1) and (H2)^Lip_μ.

---

## 4. CEN1, the position convention, W-mult^σ and (W-comm)^σ_J (target T2, first half) (appended ≈03:50Z)

Q_l denotes the **linearised** root map of Setting LIN, Q_l = Q_str − d∘h_l (BFT_A BL-2 (b), "8.2 BL-2: PROVEN-HERE"):
(Q_lx)(c) = avg over axis orders σ and y ∈ B(X) of the signed sum of x over the contour c_X → y (axial, order σ) →
y + Le_μ (straight) → c_X + Le_μ (the go path translated by Le_μ, reversed) — the translate appears because h_l(X + e_μ)
uses the translates of the paths of h_l(X). Weights w_{c,a}; row sums Σ_a|w_{c,a}| ≤ p_L := L + d(L − 1) (straight legs L,
go and return legs ≤ d(L − 1)/2 each; = 5L − 4 at d = 4, inside BL-2's 5L); |m_a − m_c|_1 ≤ δ_*h_l with
δ_* := d(L − 1)/2 + L/2 (own steps); column sums Σ_c|w_{c,a}| ≤ c_col := 2d + L^{1−d} (straight part exactly L^{1−d}; a link
lies in the go paths of one block X′ only, used by the d links (X′, ·) and the return legs of the d links (X′ − e_ν, ν), each
with path fraction ≤ 1). **b4w55_1 P5** checks all three in d = 2, 3 exactly (measured: row max 43/9 and 499/81; column max 1;
radius d + 1 own steps).

### 4.1 Lemma CEN1 (second centring cancellation, exact) — PROVEN-HERE; exact check b4w55_1 P1 (d = 2, 3)
Under Convention C, for every level-(l+1) link c = (X, μ), every constant vector v and every direction-constant level-l field
x̄ (x̄(a) = x̄_{dir(a)}): **Σ_a w_{c,a}(v·(m_a − m_c))x̄_{dir(a)} = 0.**
*Proof.* Fix (σ, y) and put m_c = c_X + (L/2)e_μ (Convention C). Straight leg: Σ_{j<L}v·(y + (j + ½)e_μ − m_c)x̄_μ =
Lx̄_μ v·(y − c_X), because Σ_{j<L}(j + ½) = L²/2. Go leg G (c_X → y) and return leg (G + Le_μ, opposite orientation): each step
a ∈ G pairs with a + Le_μ, same direction, opposite sign, midpoint shifted by Le_μ, contributing −Lv_μ ε_a x̄_{dir(a)}; the sum
over G is −Lv_μ Σ_ν(y − c_X)_ν x̄_ν (net displacement). Total L[x̄_μ v·(y − c_X) − v_μ x̄·(y − c_X)], linear in y − c_X; the
average over y ∈ B(X) vanishes because c_X is the centre of B(X) (L odd). The σ-average is irrelevant. ∎
(This is BFT_A BA-12 "CEN1", re-derived with its implicit evaluation point made explicit: BA-12's "whose y-average is
Lχ(m_c)x̄_μ (avg y = c_X)" places m_c at the contour centre, i.e. Convention C. b4w55_1's controls K1 (y-range shifted by
e_0), K2 (corner positions) and K4 (one weight + 1/997) all make P1 fail.)

**Corollary CEN1-T (Taylor form).** For a C^{1,1} cutoff φ of scale ℓ (|∂φ| ≤ 1/ℓ, |∂²φ| ≤ 1/ℓ², coarse), every level-l
field x and every c: own |[Q_l, φ]x(c)| ≤ C_Qh_l³(||∇^cx^c_l||_∞/ℓ + ||x^c_l||_∞/ℓ²), **C_Q := 2p_Lδ_*²** (k-independent;
665.5 at d = 4, L = 3), where [Q_l, φ]x(c) := Σ_a w_{c,a}(φ(m_a) − φ(m_c))x(a).
*Proof.* Write φ(m_a) − φ(m_c) = ∇φ(m_c)·Δ_a + R_a, Δ_a := m_a − m_c, |R_a| ≤ ½ℓ^{−2}|Δ_a|_1² ≤ ½ℓ^{−2}δ_*²h_l²; and
x(a) = x̄_{dir(a)} + (x(a) − x̄_{dir(a)}) with x̄_ν := x(a*_ν) for a reference ν-link a*_ν in the support. By CEN1 the
∇φ·Δ_a x̄ part vanishes. |x(a) − x(a*)| ≤ 2δ_*·g, g := max own same-direction difference ≤ h_l²||∇^cx^c_l|| (∇^cx^c =
L^{2(k−l)}× own difference); |x(a)| ≤ h_l||x^c_l||. So |[Q_l, φ]x(c)| ≤ p_L[(δ_*h_l/ℓ)(2δ_*)h_l²||∇^cx^c|| +
(δ_*²h_l²/(2ℓ²))h_l||x^c||] ≤ 2p_Lδ_*²h_l³(||∇^cx^c||/ℓ + ||x^c||/ℓ²). ∎ (b4w55_1 P2 checks the corresponding bound
numerically-exactly in d = 2, 3 for quadratic φ; disclosed there as an implementation test.)

### 4.2 Proposition CORNER (the cutoff's evaluation point is load-bearing at σ > 0) — PROVEN-HERE; exact identity b4w55_1 P4
Under **Convention K** (every level-j site at L^{j−k}·(site index); so the level-(l+1) link c sits at m^K_c = m_c − ((L−1)/2)h_l𝟙
relative to its contour centre m_c):
(a) For every φ and every direction-constant x̄: [Q_l, φ]_Kx̄(c) = [Q_l, φ]x̄(c) + (φ(m_c) − φ(m^K_c))·Lx̄_μ, and for affine φ
the first term is 0 (CEN1), so **[Q_l, φ]_Kx̄(c) = ((L − 1)/2)h_l(∇φ·𝟙)·Lx̄_μ ≠ 0** (exact; P4).
(b) **W-mult^σ is false under Convention K for every σ ∈ (0, 1]:** sup_x||φx||_{(σ)}/||x||_{(σ)} ≥ (L − 1)L^{σ(k−1)−1}/(16ℓ′),
unbounded in k at fixed ℓ′, for cutoffs φ of scale ℓ′ with a point where |∇φ·𝟙| ≥ 1/(2ℓ′) (e.g. lane B's ψ_□ on its
transition annulus along one axis).
*Proof of (b).* Take a ∈ su(N), |a| = 1, and x_j(b) := h_ja for dir(b) = 1, 0 otherwise (0 ≤ j < k), x_k := 0. Then
x^c_j ≡ a on direction-1 links, ∇^cx^c_j = 0, r_j(x) = Lh_ja − h_{j+1}a = 0 for j ≤ k − 2 (Q maps constants to L times
themselves, BL-2 (b)), r_{k−1} = a: **||x||_{(σ),hom} = 2.** For a direction-1 link c at level l + 1 = 1 (q = k − 1) whose
contour box lies where |∇φ·𝟙| ≥ 1/(2ℓ′): r_0(φx)(c) = φ(m^K_c)r_0(x)(c) + [Q_0, φ]_Kx_0(c) = 0 + [Q_0, φ]x_0(c) +
(φ(m_c) − φ(m^K_c))·Lh_0a. The first is ≤ C_Qh_0³/ℓ′² by CEN1-T (∇^cx^c = 0); the second has modulus
≥ ((L − 1)/2)h_0·Lh_0·(1/(2ℓ′) − d²(L − 1)h_0/(2ℓ′²)) ≥ (L − 1)Lh_0²/(8ℓ′) once h_0 = L^{−k} is small. The residual leg of
||φx||_{(σ)} at j = 0 is L^{(1+σ)(k−1)}L^{k−1}|r_0(φx)| ≥ L^{(2+σ)(k−1)}(L − 1)L·L^{−2k}/(8ℓ′) − O(L^{−k}) =
(L − 1)L^{σ(k−1)−1}/(8ℓ′) − O(L^{−k}). Divide by ||x|| = 2. ∎
*Reading.* At σ = 0 the same ratio is (L − 1)/(16Lℓ′): lane B's W-mult (σ = 0) is convention-blind (consistent with its
proof, which never uses a cancellation). At σ > 0 it is not: BFT34_55's "W-mult^σ, which needs CEN1 for the residual leg"
is **true only with Convention C**. The convention is free (positions enter the banked estimates only through weights,
insensitive up to e^{2μ}), so I fix Convention C throughout. The same uncancelled term enters the natural representation of
(W-comm)^σ under K (its residual slot κ[Q, ψ]_Ku_l), with R(σ)-norm ~ L^{σq}; I have not examined whether some other
representation would rescue Convention K (not needed).

### 4.3 Proposition WM^σ (cutoffs on the σ-pair) — PROVEN-HERE (Convention C)
For a cutoff φ of scale ℓ ≥ ¼ and every complex chain x (x_k := 0), and every complex source representation S:
  **||φx||_{(σ),μ,f} ≤ e^{5μ}C^σ_M(ℓ)||x||_{(σ),μ,f},  C^σ_M(ℓ) := 1 + (2d + 1 + C_QL^{−3})/ℓ + (d + C_QL^{−3})/ℓ²;**
  **N^{(σ)}_{μ,f}(M_φS) ≤ C^Y_M(ℓ)N^{(σ)}_{μ,f}(S),  C^Y_M(ℓ) := 1 + d/ℓ.**
*Proof.* Levels j < k, q := k − 1 − j. (1)-(3): lane B §10.3 (1)-(3) (CONFIRMED in REVIEW_BFT_B_S3 C.2; re-derived: the
discrete product rule ∇^c(φx^c)(b) = φ(m_{b+e_ν})∇^cx^c(b) + h(b)x^c(b) with |h| ≤ 1/ℓ, and the Campanato product rule
Osc_2(fg; B) ≤ ||f||_∞Osc_2(g; B) + osc_∞(f; B)||g||_∞) give ||(φx)^c_j|| ≤ ||x^c_j||, ||∇^c(φx^c_j)|| ≤ ||∇^cx^c_j|| + ℓ^{−1}||x^c_j||,
[∇^c(φx^c_j)]_α ≤ [∇^cx^c_j]_α + (2d/ℓ)||∇^cx^c_j|| + (d/ℓ²)||x^c_j||. (4) Residual (Convention C):
r_j(φx)(c) = φ(m_c)r_j(x)(c) + [Q_j, φ]x_j(c), and by CEN1-T
  L^{(1+σ)q}||r^c_j(φx)|| ≤ L^{(1+σ)q}||r^c_j(x)|| + L^{(2+σ)q}C_QL^{−3(q+1)}(||∇^cx^c_j||/ℓ + ||x^c_j||/ℓ²),
and L^{(2+σ)q−3q−3} = L^{−3}L^{(σ−1)q} ≤ L^{−3} for σ ≤ 1 (a maximum over levels — no level sum, so σ = 1 is harmless; Codex
BFT34 R2). The top level j = k − 1 (x_k = 0) is the same formula. Sum (1)-(4) inside max_j. Sources: slotwise
multiplication does not increase sup-type slots, and for the pointwise Hölder slot |φG(z) − φG(z′)| ≤ |G(z) − G(z′)| +
(d/ℓ)|z − z′|_∞|G(z′)|. Weights: every inequality is pointwise; (4) reads x on the contour box of c (d_1 < 5), (3) inside its
box (Campanato with the corner weight; the sup factor costs e^{4μ}), so Lemma LD gives the factor e^{5μ} on 𝔐^{(σ)}; the
source bounds have read radius 0 (same base points). ∎

### 4.4 Proposition WC^σ ((W-comm)^σ_J, with an explicit level profile) — PROVEN-HERE (Convention C)
𝓑(u, x) := ⟨du_0, dx_0⟩ + Σ_{l<k}κ_l⟨r_l(u), r_l(x)⟩ — the Feynman-free Hessian of 𝔉_k at the trivial chain, B = 0, in Setting
LIN's normalisation (BFT_A §7.1 "E_src"), su(N) componentwise; displacements, u_k = x_k = 0. For a cutoff ψ of scale ℓ ≥ 1
put C_ψ(u)(x) := 𝓑(ψu, x) − 𝓑(u, ψx). Then **C_ψ(u) = π(C^♯_ψ(u)) exactly**, with the representation
- G_0(p) := Σ_{b∈∂p}ε_{p,b}(ψ(m_b) − ψ(m_p))u_0(b) (divergence slot, paired with dx_0);
- j^W_0(b) := −Σ_{p∋b}ε_{p,b}(ψ(m_b) − ψ(m_p))du_0(p) (plain, level 0);
- s_l(c) := κ_l([Q_l, ψ]u_l)(c) (residual slot, paired with r_l(x));
- j^S_l(a) := −κ_lΣ_cw_{c,a}(ψ(m_a) − ψ(m_c))r_l(u)(c) = −κ_l([Q_l, ψ]^Tr_l(u))(a) (plain, level l);
*Exactness.* d(ψu)(p) = ψ(m_p)du(p) + G_0(p) and r_l(ψu)(c) = ψ(m_c)r_l(u)(c) + ([Q_l, ψ]u_l)(c); the ψ(m_p)du·dx and
ψ(m_c)r(u)·r(x) terms cancel between 𝓑(ψu, x) and 𝓑(u, ψx), and transposing the remaining x-terms gives j^W_0 and j^S_l.
**b4w55_1 P3** checks the identity exactly (d = 2, 3, one root step plus a level-l plaquette term, arbitrary ψ-values, three
seeds); control K3 (drop j^S) fires. Any value ψ(m_p) gives a valid representation; m_p (plaquette centre) is the small one.
*Supports.* Every slot vanishes unless ψ is non-constant on the relevant plaquette or contour box: all slots lie in
(supp ∂ψ)^{(2)} (ℓ^∞; the contour box has ℓ^∞ extent < 2), inside lane B's (supp ∂ψ)^{(3)}, and read u only there.
*Bounds (k-, T-uniform; the J slot with an explicit profile).*
- ||G^c_0||_∞ ≤ 2||u^c_0||/ℓ and [G^c_0]^∞_α ≤ 2d||∇^cu^c_0||/ℓ + 2d||u^c_0||/ℓ² (|ψ(m_b) − ψ(m_p)| ≤ L^{−k}/(2ℓ) per edge; for
  two plaquettes at |z − z′|_∞ ≤ 1 the edge factors differ by ≤ d|z − z′|_∞/(2ℓ²)·L^{−k} and u^c differs by ≤ d|z − z′|_∞||∇^cu^c||);
- π_0(j^W_0) ≤ 2(d − 1)||∇^cu^c_0||/ℓ (2(d − 1) plaquettes per link, |du_0| own ≤ 2L^{−2k}||∇^cu^c_0||);
- **||s||_{R(σ)} ≤ κ_+C_QL^{−3}(1/ℓ + 1/ℓ²)||u||_{(σ)}** (CEN1-T exactly as in WM^σ (4));
- **π_l(j^S_l) ≤ b_l||u||_{(σ)}/ℓ with b_l := κ_+c_colδ_*L²·L^{−σ(k−1−l)}** (plus 2(d − 1) at l = 0 from j^W_0): own
  |j^S_l| ≤ κ_+c_col(δ_*h_l/ℓ)sup|r_l(u)|, sup_own|r_l(u)| = L^{−q}||r^c_l(u)|| ≤ L^{−(2+σ)q}||u||_{(σ)}, and
  L^{3(q+1)}·L^{−(q+1)}·L^{−(2+σ)q} = L^{2−σq}. **Profile sum B_c := Σ_lb_l·ℓ... = 2(d − 1) + κ_+c_colδ_*L²/(1 − L^{−σ}),**
  finite for every σ ∈ (0, 1] (σ = 1: 1/(1 − L^{−1})), and ≍ k at σ = 0 — this is lane A's GAP 1 (BFT_A "GAP 1 (F3)"),
  which therefore **dissolves in the σ-pair with the J slot**.
Hence **N^{(σ)}(C^♯_ψ(u)) ≤ (C^σ_c/ℓ)||u||_{(σ)}, C^σ_c := 2 + 4d + 2κ_+C_QL^{−3} + B_c**, with the level profile
π_l((C^♯_ψu)_l) ≤ (b_l + 2(d − 1)δ_{l0})||u||/ℓ; weighted: every slot is pointwise with read radius < 5, so the same with
e^{5μ} and ||u||_{(σ),μ,f} (Lemma LD), profile included.
*Exponent count vs Codex BFT34 R6.* R6 is right that BFT34_55's displayed own-unit bound L²·(L^{−(k−l)}/ℓ)|r_l(u)| converts to
L^{4+σ}L^{−σ(k−l)}, not L^{3+σ} (I re-did its arithmetic: 3n + 2 − n − (2 + σ)(n − 1) = 4 + σ − σn). My count is independent:
the column factor is c_col (L-independent) and the displacement factor δ_*h_l, giving κ_+c_colδ_*L^{2+σ}L^{−σ(k−l)}
≤ ((d + 1)/2)κ_+c_colL^{3+σ}L^{−σ(k−l)} (δ_* ≤ (d + 1)L/2). Both are upper bounds; neither is sharp (b4w55_1 measures column
sums ≤ 1); summability for σ > 0 is unaffected. **Agree with R6.**

---

## 5. The cc walk with the slice projection inside every piece; μ = 0 → μ > 0 (target T2, second half) (appended ≈04:00Z)

### 5.1 Lemma CCL′ (cc-localisation; re-derived) — PROVEN as an implication of HR (v); **agree with Codex BFT34 R5**
For cc y and a cutoff χ of scale ℓ (Convention C, slotwise M_χ): D^⊥(M_χy) = (Σ_lev^{(l)T}v_l)^⊥ with v_l := d*(χj_l) − χd*j_l,
|v_l| ≤ 2d·(h_l/(2ℓ))sup|j_l| = (d/ℓ)L^{−d(k−l)}π_l(j_l) (each incident link midpoint is half a step from the site), because the
G and residual slots have D = 0 slotwise and Σ_lev^{(l)T}(χ·d*j_l) = χ·D(y) (Convention C (i)) vanishes off the roots (y cc).
HR (v) (J(P^Tev^{(l)T}v) ≤ (M_γ/(L − 1))L^{d(k−l)}sup|v|) gives **J(P^TD^⊥(M_χy)) ≤ (dM_γ/((L − 1)ℓ))·J(y restricted to
links within ½h_l of supp χ)**; at d = 4, L = 3, ℓ = ¼ the factor is 216 (Codex R5: "216 … 1 + 216 = 217 including the
unchanged source" — I agree). With WM^σ on sources: **N^{(σ)}(P_ccM_χy) ≤ C_y(ℓ)N^{(σ)}(y), C_y(ℓ) := 1 + d/ℓ + dM_γ/((L − 1)ℓ)**
(233 at ℓ = ¼, d = 4, L = 3). Every step is pointwise with read radius ≤ 5 (routing inside cells), so the weighted form holds
with e^{5μ}.

### 5.2 Proposition RWE (the cc walk with Π_E inside each piece; exact algebra) — PROVEN-HERE
*Setting.* Global coarse torus 𝕋 of side T ≥ 4R + 14 with a product partition into boxes □ of sides in [R, 2R), R ≥ 16
(RW3-3's product partitions); χ_□ (Σ_□χ_□ = 1, supp ⊂ □^{(1)}, scale ¼), ψ_□ (= 1 on □^{(R/2)}, supp ⊂ □^{(R)}, scale R/4) as in
lane B's W-cut (the per-coordinate construction does not depend on the box side); local tori 𝕋_□ of side 4R + 22 with
coarse-lattice translations ι_□ (roots to roots) embedding □^{(R+6)} injectively. Π_E := the S_E projection on 𝕋 (T ≥ 5).
*Pieces*, for a cc source z on 𝕋:
  z_□ := P_cc(M_{χ_□}z);  u_□ := 𝓛^{−1}_{E,𝕋_□}(ι_{□*}z_□) (the S_E response on 𝕋_□, data 0);
  **P̃_□z := Π_E(ψ_□·ι_□^*u_□)** (Π_E applied on 𝕋);  **R̃_□z := −ι_□^*C^♯_{ψ_□}(u_□)** (WC^σ's representation);  P̃ := Σ_□P̃_□,
  R̃ := Σ_□R̃_□.
*Claims.* (a) Σ_□z_□ = z for cc z; every z_□ is cc and supported in □^{(2)}. (b) ι_*z_□ is cc on 𝕋_□, so u_□ exists and
𝓑_{𝕋_□}(u_□, v) = ⟨ι_*z_□, v⟩ for **every** v. (c) **𝓑_𝕋(P̃_□z, w) = ⟨z_□ − R̃_□z, w⟩ for every w**, hence 𝓑(P̃z, w) = ⟨z − R̃z, w⟩.
(d) Every R̃_□z is cc (box by box) and every P̃_□z ∈ S_E. (e) If R̃^nz → 0 and P̃Σ_{n≤N}R̃^nz converges, the limit is in S_E and
solves Hx = z: it is **the S_E response x_E(z)** (no further projection needed).
*Proof.* (a) P_cc is linear, Σ_□M_{χ_□}z = z slotwise, P_ccz = z for cc z, and P_ccS is cc for every S (HR (i)); routing stays
in the cells meeting □^{(1)}. (b) For λ′ ∈ Λ_*(𝕋_□) let λ := φ·ι^*λ′, φ a cutoff equal to 1 on (supp z_□)^{(3)} and supported in
the embedded region; λ vanishes at the level-k roots of 𝕋 (ι maps roots to roots; φ = 0 elsewhere), and Ξλ = ι^*Ξλ′ wherever
z_□ reads (Ξ is local), so ⟨ι_*z_□, Ξλ′⟩ = ⟨z_□, Ξλ⟩ = 0. Ker H_{𝕋_□} = 𝒢_0(𝕋_□) (Codex GSHARP §1), so ι_*z_□ ∈ Ran H and the S_E
response exists and solves against every test vector (EP-opt). (c) Π_Ev − v ∈ 𝒢_0 = Ker H (EP algebra), so
𝓑_𝕋(Π_E(ψι^*u), w) = 𝓑_𝕋(ψι^*u, w). The Hessian couples only variables within one density (ℓ^∞ extent < 2, Lemma FR), so
with w′ := w on □^{(R+3)}, 0 elsewhere, this is 𝓑_𝕋(ψι^*u, w′) = 𝓑_{𝕋_□}(ψu, ιw′) (□^{(R+6)} embeds) = 𝓑_{𝕋_□}(u, ψιw′) +
C_ψ(u)(ιw′). The first term is ⟨ι_*z_□, ψιw′⟩ by (b) = ⟨z_□, w⟩ (z_□ reads its test vector within □^{(4)}, where ψ = 1 for
R ≥ 8 and w′ = w). For the second: C_ψ(u)(·) reads its argument only on (supp ∂ψ)^{(2)} (a density on which ψ is constant
contributes ψ·Hess_D(u, ·) − Hess_D(u, ψ·) = 0), where w′ = w″ := w on □^{(R+6)}; so it equals ⟨C^♯_ψ(u), ιw″⟩ = ⟨ι^*C^♯_ψ(u), w⟩
(lane B's RW3-2 "x″-argument"; C^♯ sits in (supp ∂ψ)^{(2)} and reads within < 2). Sum over □ with (a). (d) Put w = Dλ,
λ ∈ Λ_*(𝕋), in (c): the left side is 0 (Dλ ∈ Ker H, 𝓑 symmetric) and ⟨z_□, Dλ⟩ = 0, so ⟨R̃_□z, Dλ⟩ = 0 — **Codex R5's
"Ξ^Tc_□ = 0 for each box", re-derived; agree.** P̃_□z ∈ S_E since ΛΠ_E = 0. (e) Partial sums lie in S_E and satisfy
𝓑(x_N, w) = ⟨z − R̃^{N+1}z, w⟩; the limit solves Hx = z in S_E, and S_E ∩ Ker H = S_E ∩ 𝒢_0 = {0} (X = S_E ⊕ 𝒢_0). ∎
*What putting Π_E inside buys.* Codex R5: "The Neumann sum, if bounded, produces a representative modulo the gauge kernel;
the S_E inverse additionally requires the final projection." With Π_E inside each piece (lane B's hard-slice design,
BFT_B §12.1 "P^Π_□y := Π(ψ_□·…)") the walk **is** the S_E inverse; this matters twice below: for the weighted estimate (no
global projection to control afterwards) and for the nonlinear family's s ≡ 1 point (§6.5), which must lie in the slice.

### 5.3 Theorem WALK^σ (μ = 0 bounds, k- and T-uniform) — PROVEN as an implication
*Inputs.* (CC) + (GV) on every torus of side ≥ 5 at data 0: ||x_E(S)||_{(σ)} ≤ G_♯N^{(σ)}(S) for cc S, G_♯ := G_inv(σ) + L·C_GV
(KFACTOR_OFF55 §4.2 LIN^{(σ)} with TOP♯; GV55 Proposition GV-E; Codex KOFF item 5, Codex GV item 2); (EP) EP-bd:
||Π_Ev||_{(σ)} ≤ (C_Π + 1)||v||_{(σ)} for every v (field legs by EP-bd on 𝔐^∇ ≤ 𝔐^{(σ)}; residual legs unchanged, Codex GSHARP
§2.5); this file's CCL′, WM^σ, WC^σ.
*Statement.* With n_R := 6^d (for R ≥ 14 a ball B_∞(z, 3) meets □^{(R+4)} for at most 6 boxes per coordinate), t_N = 3, t_X = 4:
  **N^{(σ)}(R̃z) ≤ ε_WN^{(σ)}(z),  ε_W := n_R(t_N + 1)(4C^σ_c/R)G_♯C_y(¼);**
  **||P̃z||_{(σ)} ≤ G_PN^{(σ)}(z),  G_P := n_Rt_X(C_Π + 1)C^σ_M(R/4)G_♯C_y(¼).**
Hence for R ≥ R^0_W := 8n_R(t_N + 1)C^σ_cG_♯C_y(¼) (ε_W ≤ ½): x_E(z) = P̃Σ_{n≥0}R̃^nz and ||x_E(z)||_{(σ)} ≤ 2G_PN^{(σ)}(z),
uniformly in k ≥ 1 and T ≥ 4R + 14.
*Proof.* Per box: N(z_□) ≤ C_y(¼)N(z) (CCL′, local); ||u_□||_{(σ),𝕋_□} ≤ G_♯N(ι_*z_□) = G_♯N(z_□) (the norms are suprema /
level sums of local quantities, preserved by the embedding of the support); N(R̃_□z) ≤ (4C^σ_c/R)||u_□|| with the profile
π_l((R̃_□z)_l) ≤ (4/R)(b_l + 2(d − 1)δ_{l0})||u_□|| (WC^σ at ℓ = R/4); ||P̃_□z|| ≤ (C_Π + 1)C^σ_M(R/4)||u_□|| (WM^σ, EP-bd).
Sum over boxes: Lemma OV (a) for the three sup-type slots and (b) for J (profile sum ≤ B_c ≤ C^σ_c). Neumann series as in
lane B §10.7 Step 4. ∎ (This reproduces, with worse constants, the bound (CC)+(GV) give directly; its point is the finite
range of every piece, used next.)

### 5.4 Corollary H2W ((H2)^Lip_μ from μ = 0 inputs) — PROVEN as an implication (the repaired form of BFT34_55's Corollary RW-cc-walk)
Let R ≥ R_W := 2R^0_W (so ε_W ≤ ¼), **D_W := 16R + 80**, **μ_W := ln 2/D_W**. For 0 ≤ μ ≤ μ_W, every 1-Lipschitz f (ℓ¹), every
cc source z, every k ≥ 1:
- T ≥ 4R + 14: **||x_E(z)||_{(σ),μ,f} ≤ 4G_P·N^{(σ)}_{μ,f}(z)**;
- 5 ≤ T < 4R + 14: ||x_E(z)||_{(σ),μ,f} ≤ e^{μ(8R+28)}G_♯N^{(σ)}_{μ,f}(z) (diam_1 ≤ 4⌊T/2⌋ ≤ 2T and the unweighted bound);
- T ∈ {3, 4} (the descended slice of (GV)): the unweighted bound times e^{8μ} (diam_1 ≤ 8; Codex BFT34 R4's correction).
The data clause follows (NB is a cc residual-type source with N^{(σ)}_{μ,f}(NB) ≤ c_N||B||_{D,μ,f}).
*Proof (box-indexed, scalar weights on cc pieces; no weighted operator on the cc class).* For each box, every base point of a
nonzero local quantity of R̃_□z or P̃_□z lies in O_□ := □^{(R+5)} (supports □^{(R+2)} resp. □^{(R+4)}, Hölder partners ≤ 1), and
every base point of z the box chain reads lies in I_□ := □^{(2)}. Both lie in □^{(R+5)}, whose ℓ^∞ side is ≤ 2R + 2(R + 5) and
ℓ¹ diameter ≤ 16R + 40 ≤ D_W. So, writing N(z|_I) for the unweighted local quantities of z based in I_□ (all that the box
chain reads):
  N_{μ,f}(R̃_□z) ≤ e^{μ sup_{O_□}f}N(R̃_□z) ≤ e^{μ sup_{O_□}f}(4C^σ_c/R)G_♯C_y(¼)N(z|_{I_□}) ≤ e^{μD_W}(4C^σ_c/R)G_♯C_y(¼)N_{μ,f}(z),
using N(z|_I) ≤ e^{−μ inf_I f}N_{μ,f}(z) and sup_O f − inf_I f ≤ D_W; the same for the profile and for P̃_□z. The unweighted
chain (M_χ, P_cc, the local inverse, C^♯, Π_E) is used verbatim on z and on the cc iterates R̃^nz (RWE (d)); weights touch only
the two ends. Lemma OV then gives N_{μ,f}(R̃z) ≤ e^{μD_W}ε_WN_{μ,f}(z) ≤ ½N_{μ,f}(z) and ||P̃z||_{(σ),μ,f} ≤ e^{μD_W}G_PN_{μ,f}(z);
sum the series. ∎
*Codex BFT34 R7, point by point — agree with all three, and this corollary is the repair, not BFT34_55's text.* (R7.1) The
reach is converted in ℓ¹: D_W = 16R + 80 ≥ 4·(4R + 20) covers product partitions (box sides < 2R) and R7.1's "coordinate
separation approaching 3R + 4"; the printed 2R + 6 is not used. (R7.2) No e^{μf}R̃e^{−μf} is formed; the cc algebra acts only on
cc objects, and the weights enter as one scalar per box through the read/write regions — R7's suggested "box-indexed
construction using scalar weights on already-cc pieces". (R7.3) Weights act on local quantities (Lemma LD); J uses explicit
profiles (Lemma OV (b), WC^σ); WM^σ and WC^σ are proven (§4); Π_E is inside each piece, so the output is the S_E field itself.
*Consequences.* (H2)^Lip_μ for the S_E response — both halves: gauge-invariant (including the σ-weighted residual leg, as a
maximum over levels) and gauge-variant — for 0 ≤ μ ≤ μ_W, **from μ = 0 inputs on local tori only**, uniformly in k, T and f.
With Theorem H3: Lemma WD, Theorem BFT3-glob (route C) and Proposition TREE (route T) hold for 0 < μ ≤ μ_W with this supply — an
independent route that uses neither COFM55's CC-INV_μ/TOP-cc_μ nor GV55's GV-E_μ. Range: μ_W = ln 2/(16R_W + 80) with
R_W ∝ C^σ_cG_♯C_y(¼); whether μ_W is larger or smaller than COFM55's m_Y ≤ 1.67·10⁻⁴ is undecided (G_♯, C_Π uncomputed).

---

## 6. The P_cc-projected bond family: (f)^σ, energy bounds, clause (d), identification (target T3) (appended ≈04:15Z)

### 6.1 Construction BBcc (lane B's BB-bond_k rebuilt on Proposition RWE)
*Geometry* (product partitions, RW3-3): R ≥ 16, M_c := 2R; the torus (T ≥ 4R + 14) is partitioned into cubes Q with sides in
[M_c, 2M_c) and boxes □ with sides in [R, 2R) refining them (≤ 3^d boxes per cube); Q(□) := the cube containing □; bonds 𝔅 :=
pairs of *-adjacent cubes (≤ 3^d − 1 = 80 neighbours); s ∈ ℂ^𝔅, s_{QQ} := 1, s_{QQ′} := s_{{Q,Q′}} for *-adjacent Q ≠ Q′, 0
otherwise; η_Q (Σ_Qη_Q = 1, supp ⊂ Q^{(2)}, scale ½; lane B W-cut); views **S_Q𝐀 := Σ_{Q′}s_{QQ′}A_{Q′}**.
*Linear part.* For cube-indexed sources 𝐳 = (z_Q) and chains 𝐀 = (A_Q):
  (𝐈(s)𝐲)_Q := Σ_{Q″}s_{QQ″}y_{Q″};  (𝐑̃(s)𝐳)_{Q′} := Σ_□s_{Q′Q(□)}R̃_□z_{Q(□)};  (𝐏̃(s)𝐳)_{Q′} := η_{Q′}·Σ_□s_{Q′Q(□)}P̃_□z_{Q(□)};
  **𝐊(s) := 𝐏̃(s)(1 − 𝐑̃(s))^{−1}𝐈(s)**, with R̃_□, P̃_□ of Proposition RWE (**Π_E inside each P̃_□**).
*Nonlinear part.* With Y(x; B) = Hx − ∇F(x; B) of §3.1, put g(B) := the part of −Y(0; B) linear in B (the data source NB up to
sign; a residual-type source at level k − 1, cc) and 𝔑(x; B) := −Y(x; B) − g(B) = ∇F(x; B) − Hx − g(B). Cube sources and map:
  **y_Q(𝐀) := P_ccM_{η_Q}[g(B) + 𝔑(S_Q𝐀; B)],  Φ_s(𝐀) := −𝐊(s)𝐲(𝐀),**  𝐀(s) := its fixed point.
*Energy (direct form — the σ-pair permits it, Lemma E2^σ).* **𝔈_Q(s) := Σ_{D∈𝒟_Q}[D(S_Q𝐀(s); B) − D(0; B)]** (𝒟_Q := densities
with base point in Q), ΔE(s) := Σ_Q𝔈_Q(s); for a cube set X, ΔE_X(s_X) := Σ_{Q∈X}𝔈_Q computed with every bond leaving X set to 0;
**R({Q}) := ΔE_{{Q}}, R(X) := Σ_{Γ connected, spanning X}∫_{[0,1]^Γ}∂^Γ_sΔE_X(s_Γ, 0)ds_Γ** (|X| ≥ 2).
Norms: |||𝐳||| := sup_QN^{(σ)}(z_Q), |||𝐀||| := sup_Q||A_Q||_{(σ),hom}. Everything in 6.1 is lane B's §9.5/§10.8 with three
changes: P_cc before every local inverse and on every nonlinear source; Π_E inside every P̃_□; the direct energy.

### 6.2 Lemma F^σ (lane B's (f), localised, in the σ-pair) — PROVEN as an implication (Theorem H3 at μ = 0 with cutoffs; banked ROW^{(σ)}, CB, HR)
For complex x, x′ with ||x||, ||x′|| ≤ η_*/8 (hom) and complex B with ||B||_D ≤ η_*/8, and every cube Q:
- N^{(σ)}(P_ccM_{η_Q}g(B)) ≤ c_g||B||_D (P_cc does nothing to a residual-type slot; M_η ≤ 1);
- N^{(σ)}(P_ccM_{η_Q}𝔑(0; B)) ≤ C_N||B||_D², N^{(σ)}(P_ccM_{η_Q}[𝔑(x; B) − 𝔑(x′; B)]) ≤ C_N(||x|| + ||x′|| + ||B||_D)||x − x′||;
- 𝔑 is holomorphic in (x, B); **locality**: P_ccM_{η_Q}𝔑(u; B) reads (u, B) only on (supp η_Q)^{(3)} (ℓ^∞: density extent < 2,
  routing within cells) and is supported in Q^{(3)}; every y_Q(𝐀) is cc (P_cc).
*Proof.* 𝔑(x) − 𝔑(x′) = −∫_0^1D_xY(x′ + t(x − x′))[x − x′]dt. The slots of M_{η_Q}D_xY[u] are η_Q-multiples of those of D_xY[u],
bounded pointwise by Lemma PW (P1); the cut-off plain slots are routed by HR (iii)/(iv) applied to w = η_Q·(plain row) —
sup-type slots do not grow under multiplication by η_Q ∈ [0, 1], and the level-0 Hölder quotient grows by at most 2d·sup
(η_Q has scale ½) — exactly as in §3.6. So C_N := (1 + 2d)K_1 works. 𝔑(0; B) = −Y(0; B) − g(B) has no constant and no linear
term in B (by the definition of g), and Schwarz in t ↦ (0; tB) on |t| ≤ η_*/(8||B||) gives the B² bound. ∎

### 6.3 Lemma E2^σ (per-cube energy, direct form) — PROVEN as an implication (Codex KOFF §4.3 (1), complexified) — and Corollary E3^σ
**Explicit holomorphic forms of the densities.** Wilson: on the real domain Re tr(1 − U_p) = N − ½tr(U_p + U_p^{−1}), so
D_p = −tr(cosh F_p − 1), F_p := log U_p = dx_0(p) + q_p(x) (BCH). Soft: with ρ := log(V^{−1}W_0(M)), G := W_0^{−1}M = H + iθ1
(NA-alg (a)), φ̂ = Re tr G − Re tr(e^ρG) = −Re tr((e^ρ − 1)G), and **Re tr(ρG) = 0** for ρ ∈ su(N) (Lemma SG's cancellation:
tr(ρH) ∈ iℝ, tr ρ = 0). Since Re tr X = ½tr(X + X*), ρ* = −ρ and G* = M*W_0 on the real domain,
  **D_c = κ_lΦ(ρ_c, G_c, G′_c),  Φ(ρ, G, G′) := −½tr((e^ρ − 1 − ρ)G + G′(e^{−ρ} − 1 + ρ)),  G′ := M̃W_0,**
where M̃ is the S4′ average of the reversed products of the inverse links (the holomorphic continuation of M*). The
continuation of Re tr(ρG), ½tr(ρG − G′ρ), vanishes on the real domain, hence identically on the connected complex polydisc;
so this formula is the holomorphic continuation of D_c. On |ρ| ≤ 1, |G|_op, |G′|_op ≤ 3: **|Φ| ≤ C_Φ|ρ|², C_Φ := 3e√N/2**
(|e^ρ − 1 − ρ|_HS ≤ ½|ρ|²e^{|ρ|}, |tr AB| ≤ |A|_HS√N|B|_op), and Φ(ρ, G, G′) − Φ(ρ_0, 1, 1) ≤ C(|ρ| + |ρ_0|)|ρ − ρ_0| +
C|ρ_0|²(|G − 1| + |G′ − 1|).
**Lemma E2^σ.** There are ρ_E > 0 and C_{E2} < ∞ (k-, T-independent) such that for complex x with ||x||_{(σ),hom} ≤ ρ_E and
complex B with ||B||_D ≤ ρ_E, and every cube Q:
  **|Σ_{D∈𝒟_Q}(D(x; B) − D(0; B))| ≤ C_{E2}|Q|(||x|| + ||B||_D)||x||,**  |Q| the coarse volume.
*Proof.* Wilson (6L^{4k}|Q| plaquettes): |F_p| ≤ L^{−2k}(2 + C||x||)||x|| (|dx_0| ≤ 2L^{−2k}||∇^cx^c_0||, |q| ≤ C|x_0|², own
|x_0| ≤ L^{−k}||x||), |D_p| ≤ √N(cosh 1 − 1)|F_p|² — total ≤ 6C_W|Q|||x||². Soft at level l ≤ k − 2 (4L^{4q}|Q| links,
q = k − 1 − l): D_c(0) = 0 and |D_c(x)| ≤ κ_+C_Φ|ρ_c|² with |ρ_c| ≤ |r_l(x)(c)| + Ch_l³||x||² (Codex KOFF §4.3 (1), "Complexification
gives the same assertion on a smaller complex polydisc") and |r_l(x)(c)| ≤ L^{−q}||r^c_l|| ≤ L^{−(2+σ)q}||x||_{(σ)}; so the level-l
total is ≤ 8κ_+C_Φ|Q|(L^{4q}L^{−2(2+σ)q}||x||² + C²L^{4q}L^{−6(q+1)}||x||⁴) = 8κ_+C_Φ|Q|(L^{−2σq}||x||² + C²L^{−6}L^{−2q}||x||⁴).
**Summed over q this is finite for every σ > 0** (1/(1 − L^{−2σ}); at σ = 0 it is k·8κ_+C_Φ|Q|||x||² — lane B's RW∇-F3, the
reason lane B needed the trapezoid form). Top level (4|Q| links): ρ_c(0; B) = −B_c exactly (W_0(1) = 1); ρ_c(x; B) − ρ_c(0; B) =
Qx_{k−1}(c) + [(ρ − r)(x; B) − (ρ − r)(0; B)], so |ρ(x) − ρ(0)| ≤ (1 + C(||x|| + ||B||))||x||; G, G′ depend on x only, with
|G − 1|, |G′ − 1| ≤ C||x||² (no linear term, Codex §4.3); hence |D_c(x; B) − D_c(0; B)| ≤ C_top(||x|| + ||B||)||x||. Sum. ∎
**Corollary E3^σ (lane B's (E3^∇) in the σ-pair).** For ||u|| ≤ ρ_E/3 and ||B||_D ≤ ρ_E:
|Σ_{D∈𝒟_Q}𝔇_D(u; B)| ≤ C_3|Q|·||u||³, 𝔇_D(u) := D(u) − D(0) − ½⟨∇D(0) + ∇D(u), u⟩, C_3 := 27C′_{E2}(ρ_E + ||B||)/(8ρ_E²).
*Proof.* g(z) := Σ_{D∈𝒟_Q}𝔇_D(zu) is holomorphic for |z| ≤ ρ_E/(1.5||u||) and vanishes to third order at 0 (for f(z) = D(zu),
𝔇 = f(z) − f(0) − ½z(f′(0) + f′(z)) = −½f_3z³ + O(z⁴)). On that circle Lemma E2^σ bounds Σ(D(zu) − D(0)), and the gradient
pairings ½|Σ⟨∇D(·), zu⟩| = ½|∂_tΣD(tzu)|_{t=0,1}| are bounded by Cauchy in t (radius ½) by the same lemma; Schwarz for g(z)/z³. ∎
*Reading.* In the σ-pair the per-cube energy is level-summable **directly**, so the trapezoid form and lane B's added Lemma
W-grad0 are no longer needed (the brief asked for (E3^∇)^σ: it holds, Corollary E3^σ, but Theorem BBcc uses E2^σ). The soft
cubic vertex is residual-carrying (Φ is quadratic in ρ), as BFT34_55 said; its level-geometric decay is the L^{−2σq} above.

### 6.4 Lemma Dcc (lane B's clause (d) re-run on the P_cc family) — PROVEN-HERE
Let ε_c := 9^d(4C^σ_c/R)G_♯C_y(¼) (per-box factor × ≤ 9^d boxes in the 3^d cubes of N(Q′)), G_c := C^σ_M(½)9^d(C_Π + 1)C^σ_M(R/4)G_♯C_y(¼),
𝔠 := (4/3)3^dG_c, and R_W(s̄) := 16·9^dC^σ_cG_♯C_y(¼)·s̄ (so s̄ε_c ≤ ¼ for R ≥ R_W(s̄)).
(i) **Holomorphy and bound.** 𝐈, 𝐑̃, 𝐏̃ are linear in s; |||𝐈(s)𝐲||| ≤ 3^ds̄|||𝐲|||, |||𝐑̃(s)𝐳||| ≤ s̄ε_c|||𝐳|||, |||𝐏̃(s)𝐳||| ≤ s̄G_c|||𝐳|||
(triangle inequality over **finitely many** terms — no W-ls and no level profile is needed for the cube family; each R̃_□, P̃_□
bound is Theorem WALK^σ's per-box bound, valid for every source since the box chain applies P_cc first; the η_{Q′} factor is
WM^σ at ℓ = ½, which needs Convention C). For s̄ε_c ≤ ¼ the Neumann series of (1 − 𝐑̃(s))^{−1} converges uniformly on |s_b| ≤ s̄
(norm ≤ 4/3), so 𝐊(s) is holomorphic on the open polydisc, continuous up to its boundary, and **|||𝐊(s)𝐲||| ≤ 𝔠s̄²|||𝐲|||**.
(ii) **s ≡ 1 identity.** For cube-supported cc 𝐲 (supp y_Q ⊂ Q^{(3)}): **Σ_{Q′}(𝐊(1)𝐲)_{Q′} = x_E(Σ_Qy_Q)**, the S_E response.
*Proof* (lane B §10.7 Step 5, distances rechecked for product partitions and Π_E). Call 𝐳 consistent with z if
M_{χ_□}z_{Q(□)} = M_{χ_□}z for every box. (α) 𝐈(1)𝐲 is consistent with Y := Σ_Qy_Q: y_{Q″} with Q″ ∉ N(Q(□)) is supported in
Q″^{(3)}, at ℓ^∞ distance ≥ M_c − 3 − 1 > 0 from □^{(1)} (non-adjacent cubes are ≥ M_c = 2R apart). (β) R̃_□ and P̃_□ read their
input only through M_{χ_□}·; if 𝐳 is consistent with z then M_{χ_{□′}}(𝐑̃(1)𝐳)_{Q(□′)} = M_{χ_{□′}}R̃z, because for Q(□) ∉ N(Q(□′))
the support □^{(R+2)} of R̃_□z is at distance ≥ 2R − (R + 2) − 1 > 0 from □′^{(1)}; by induction Σ_{n≤N}𝐑̃(1)^n𝐈(1)𝐲 is consistent
with Σ_{n≤N}R̃^nY. (γ) Σ_{Q′}(𝐏̃(1)𝐳)_{Q′} = Σ_{Q′}η_{Q′}Σ_{□:Q(□)∈N(Q′)}P̃_□z = Σ_{Q′}η_{Q′}P̃z = P̃z, since for Q(□) ∉ N(Q′) the
support □^{(R+4)} of P̃_□z (Π_E has ℓ^∞ reach 4, EP-alg) misses supp η_{Q′} ⊂ Q′^{(2)} (distance ≥ 2R − (R + 4) − 2 > 0).
Convergence: the cube series converges (s̄ε_c ≤ ¼ at s ≡ 1), and consistency gives M_{χ_□}R̃^nY = M_{χ_□}(𝐑̃(1)^n𝐈(1)𝐲)_{Q(□)}, so
Σ_nR̃^nY converges box by box; RWE (e) identifies P̃Σ_nR̃^nY with x_E(Y). ∎
(iii) **Splitting.** If s_b = 0 on every bond between two classes of cubes, every non-zero weight s_{QQ′} joins cubes of one class,
so 𝐈(s), 𝐑̃(s), 𝐏̃(s) and (1 − 𝐑̃(s))^{−1} map class-C components to class-C components using only weights inside C: (𝐊(s)𝐲)_{Q′}
depends only on the y_Q and s_b with Q, b in the class of Q′. ∎
*(d) also needs the family to stay cc for complex s:* cube components of 𝐈(s)𝐲 are cc combinations of cc sources; every R̃_□z
is cc for every z (RWE (d), applied to the cc source P_ccM_{χ_□}z); so every component of every iterate is cc — Codex BFT34
R5's "arbitrary scalar bond weights preserve cc", agreed.

### 6.5 Lemma UQ (a uniqueness ball not shrinking with ||B||) and Lemma IDcc ((I-id) for the family) — PROVEN as implications
**Lemma UQ.** With K the local Lipschitz constant of Codex KOFF §5.3, G_♯ the cc response constant and C_cc := 2dc_BernL^{d−1}
(c_Bern ≤ 59/100), put r_u := min(η_*/8, 1/(8G_♯K), 1/(2C_cc)) and b_u := min(η_*/8, 1/(4G_♯K)). For ||B||_D ≤ b_u, Φ̃_{Γ_E} has
Lip ≤ G_♯K(2r_u + ||B||_D) ≤ ½ on 𝔅_u := {x ∈ S_E : ||x||_{(σ),hom} ≤ r_u}, hence at most one fixed point there; every critical
point of F in 𝔅_u is a fixed point (CCP (d), converse half: ∇F(x̄) = 0 ⇒ D^⊥(𝔑^0(x̄)) = 0 by Lemma CD ⇒ S̃(x̄) = Hx̄ = 𝓛_{Γ_E}x̄);
so **x(B) (BFT-E) is the unique critical point of F in 𝔅_u** whenever ||B||_D ≤ min(b_u, r_u/C_0). ∎
**Lemma IDcc.** In Theorem BBcc's regime, A := Σ_{Q′}A_{Q′}(1) **= x(B)**.
*Proof.* At s ≡ 1, S_Q𝐀 = A on Q^{(5)} (the A_{Q′} with Q′ ∉ N(Q) live in Q′^{(2)}, at distance ≥ 2R − 7 > 0), so by F^σ's locality
Σ_Qy_Q(𝐀) = P_cc[g + 𝔑(A)]; the y_Q are cube-supported and cc, so Lemma Dcc (ii) gives **A = −x_E(P_cc[g + 𝔑(A)]) ∈ S_E** and
HA = −P_cc(g + 𝔑(A)) = −P_cc(∇F(A) − HA) = −P_cc∇F(A) + HA (D^⊥(HA) = 0 because HΞ = 0 on Λ_*). Hence P_cc∇F(A) = 0, i.e.
∇F(A) = P^TD^⊥(∇F(A)) = P^T(K′^T_A∇F(A))^⊥ (Lemma CD, root-pinned, [S26-BANKED]), i.e. M_A∇F(A) = 0, and CCP (c)
(J(P^T(K′^T_Ag)^⊥) ≤ C_cc max_j||A^c_j||·J(g), banked) gives ∇F(A) = 0 because max_j||A^c_j|| ≤ ||A|| ≤ t_X2^dr_s ≤ r_u ≤ 1/(2C_cc).
So A ∈ 𝔅_u is a critical point in S_E, and A = x(B) by Lemma UQ. (Lemma CD and CCP (c) are algebraic identities and Bernoulli
bounds, valid for complex A by continuation; real B gives real A anyway.) ∎
*Why Π_E inside matters here.* Without it the s ≡ 1 point is a critical point **not** in any slice, and identifying it with x(B)
would need nonlinear gauge-orbit coverage — NOT-VERIFIED (Codex KOFF item 5, Codex GV item 5). With Π_E inside, no orbit
statement is used.

### 6.6 Theorem BBcc (bounded polymers at every k, on 𝒞_glob, P_cc family) — PROVEN as an implication
*Hypotheses:* the banked inputs (K), (GV), (EP), Lemma CD (§1), and this file's CEN1, WM^σ, WC^σ, CCL′, RWE, WALK^σ, F^σ, E2^σ,
Dcc, UQ, IDcc. Put c_v := t_X2^ds̄, r_s := 4𝔠s̄²c_gε, and let ε_cc(s̄) > 0 be the largest ε with: C_Nε ≤ c_g; c_vr_s + ε ≤
min(η_*/8, ρ_E); 𝔠s̄²C_N(2c_vr_s + ε)c_v ≤ ½; t_X2^dr_s ≤ r_u; ε ≤ min(b_u, r_u/C_0, ε_0^{BFT-E}). (All k-, T-independent.)
*Statement.* For s̄ ≥ 2, R ≥ max(R_W(s̄), 16), product partitions, T ≥ 4R + 14, ε ≤ ε_cc(s̄) and every B ∈ 𝒫_ε (the complex
polydisc max_c|B_c| ≤ ε of (PD-glob)):
- **(i)** 𝐀(s) exists and is unique in |||𝐀||| ≤ r_s, is holomorphic in (s, B) for |s_b| < s̄, B ∈ int 𝒫_ε, and
  Σ_{Q′}A_{Q′}(1) = x(B);
- **(ii)** **E_k^br(B) = E_∅(B) + Σ_XR(X)** exactly (E_k^br := 𝔉_k(x(B); B), E_∅(B) := 𝔉_k(0; B) = κ_{k−1}Σ_cφ̂_c(e^{B_c}; 1));
  R(X) = 0 unless X is *-connected; R(X) depends on B only on X^{(5)}, is holomorphic, invariant under constant gauges, and
  covariant under the partition-preserving translations;
- **(iii)** |R(X)| ≤ C_RK_pol^{|X|−1}, C_R := 2^{40}C_E, K_pol := 2^{41}/(s̄ − 1), **C_E := C_{E2}(2M_c)⁴(c_vr_s + ε)c_vr_s**; for
  s̄ − 1 ≥ 2^{42}·80e·e^{m_0}: **sup_{Q_0}Σ_{X∋Q_0}sup_{𝒫_ε}|R(X)|e^{m_0|X|} ≤ 2e^{m_0}C_R**, uniformly in k and T.
*Proof.* (i) Components of 𝐊(s)𝐳 are η_{Q′}·(…), so Φ_s maps into {supp A_Q ⊂ Q^{(2)}}, where ||S_Q𝐀|| ≤ c_v|||𝐀||| (Lemma OV (a),
each ball B_∞(z, 3) meets ≤ 2^d sets Q′^{(2)}). With Lemma F^σ: |||Φ_s(0)||| ≤ 𝔠s̄²(c_gε + C_Nε²) ≤ r_s/2 and
|||Φ_s(𝐀) − Φ_s(𝐀′)||| ≤ 𝔠s̄²C_N(2c_vr_s + ε)c_v|||𝐀 − 𝐀′||| ≤ ½|||𝐀 − 𝐀′|||; Banach; holomorphy as a uniform limit of holomorphic
iterates (𝐊 holomorphic in s by Dcc (i), 𝔑 in (x, B)); the identification is Lemma IDcc. (ii) At s ≡ 1 every D ∈ 𝒟_Q reads its
argument within ℓ^∞ < 2 of Q, where S_Q𝐀 = A, so ΔE(1) = Σ_D[D(A) − D(0)] = E(A) − E(0) = E_k^br(B) − E_∅(B) (by (i)).
Splitting (Dcc (iii)) gives ΔE(s) = Σ_CΔE_C(s_C) when s vanishes between classes; the cluster identity (iterated
f(1) = f(0) + ∫∂_{s_b}f over the bonds; ∂^Γ kills every class term not depending on all bonds of Γ) leaves only Γ = ∅ and
connected Γ: E_k^br − E_∅ = Σ_XR(X), R(X) = 0 unless X is *-connected. B-locality: F^σ (reads B on (supp η_Q)^{(3)}) and the
densities (top densities read B_c within < 2 of Q). Constant gauges: every operator (P_cc, cutoffs, local S_E inverses, Π_E, C^♯,
𝔑) commutes with Ad_g, so uniqueness gives 𝐀(s)(Ad_gB) = Ad_g𝐀(s)(B), and each D is Ad-invariant. Translations: only those
preserving the cube and box partitions (RS3-6). (iii) For |s_b| < s̄: ||S_Q𝐀|| ≤ c_vr_s, so Lemma E2^σ gives |𝔈_Q| ≤ C_E (|Q| <
(2M_c)⁴) and sup|ΔE_X| ≤ |X|C_E. Cauchy in the |Γ| distinct bond variables on discs of radius s̄ − 1 − δ about [0, 1]^Γ (δ ↓ 0):
factor (s̄ − 1)^{−|Γ|}, |Γ| ≥ |X| − 1; at most 2^{40|X|} subsets of the ≤ 40|X| bonds internal to X (80 neighbours, each bond
shared); |X| ≤ 2^{|X|−1}: |R(X)| ≤ 2^{40}C_E(2^{41}/(s̄ − 1))^{|X|−1}. At most (80e)^{n−1} *-connected X of n cubes contain a given
cube; with 80e·e^{m_0}K_pol ≤ ½, Σ_{X∋Q_0}|R(X)|e^{m_0|X|} ≤ C_Re^{m_0}Σ_n2^{−(n−1)} = 2e^{m_0}C_R for **every** anchor Q_0. ∎
(The combinatorial core is the one Codex BFT34 R11 confirms under "V7's combinatorial core"; I re-derived it, agree, and state
it with the uniform-anchor norm that Codex BFT34 R8 asks for — lane B's one-anchor Σ_{X∋0} is vacuous without covariance.)
*Small tori.* For 5 ≤ T < 4R + 14 there are O(1) cubes; take the single polymer X := all cubes, R(X) := E_k^br − E_∅ =
Σ_D[D(x(B)) − D(0)], bounded by Lemma E2^σ with ||x(B)|| ≤ C_0ε: |R(X)|e^{m_0|X|} ≤ e^{m_0(T/M_c+1)⁴}C_{E2}T⁴(C_0 + 1)C_0ε² — bounded
uniformly in k (T bounded in terms of R). For T ∈ {3, 4} the same with the descended slice of (GV).

---

## 7. Assembly (target T4) (appended ≈04:25Z)

> **Theorem BFT4a-glob (BFT-4's bounded-polymer clause on 𝒞_glob, for the composite critical value).** Fix d = 4, N ≥ 2, L ≥ 3
> odd, κ_l ∈ [κ_−, κ_+], 0 < α < θ ≤ σ ≤ 1 (θ₀ as in GV55), Convention C, and m_0 > 0. Choose s̄ := 1 + 2^{42}·80e·e^{m_0},
> R := max(R_W(s̄), 16), M_c := 2R, ε := ε_cc(s̄). Then for every k ≥ 1, every coarse torus side T ≥ 3 and every B in the complex
> polydisc 𝒫_ε = {max_c|B_c| ≤ ε} (PD-glob):
> **E_k^br(B) = S_W(e^B) + R_k(B), R_k := (E_∅ − S_W) + Σ_XR(X),**
> with R(X) holomorphic on 𝒫_ε, depending on B only on X^{(5)}, zero unless X is *-connected, invariant under constant gauges, and
> **sup_{Q_0}Σ_{X∋Q_0}sup_{𝒫_ε}|R(X)|e^{m_0|X|} ≤ 2e^{m_0}C_R** (single-plaquette / single-link terms of E_∅ − S_W assigned to the cube
> of their base point add C_∅ := e^{m_0}(2M_c)⁴(6 sup_{𝒫}|D_p| + 4κ_+sup_{𝒫}|φ̂(e^{B_c}; 1)|), as in lane B's Corollary BFT4-poly_k).
> All constants depend only on (N, L, κ_±, α, θ, θ₀, σ, m_0) and the banked local constants — **not on k or T**. The pieces are
> **not** locally gauge invariant (E_∅ is a sum of single-link terms; lane B's [RBB3-fix BP3-1], unchanged).
> **Status: PROVEN as an implication** of the inputs below. Not yet checked by the other model family.

| # | Input | Where | Status |
|---|---|---|---|
| 1 | Theorem K^{(σ)} pieces: HR (i)-(v), CCP (a)-(d), SG, ROW^{(σ)} with (LA-1′) and the §4.3 local analytic completion, CB, TOP♯, LIN^{(σ)} | KFACTOR_OFF55; CODEX_REVIEW_KOFF items 1-5 | **[S26-BANKED]**, conditional on the lane-A linear package |
| 2 | (GV): GV-E, slice identity, the corrected K + GV-E contraction (x(B), its regularity and holomorphy, composite critical value) | GV55; CODEX_REVIEW_GV items 2-4 | **[S26-BANKED]** |
| 3 | (EP): EP-alg algebra, Ker H = 𝒢_0, EP-opt, EP-bd at zero weight, finite ℓ¹ reach of Π_E | BFT_B §15-16; CODEX_REVIEW_GSHARP item 1, §2.5, §6 | **[S26-BANKED]** |
| 4 | Lemma CD (root-pinned) | BFT_A §31.1; CODEX_REVIEW_C2 item 4 | **[S26-BANKED]** |
| 5 | Connected-bond combinatorics (cluster identity, 2^{40|X|}, (80e)^{n−1}) | lane B §6.5, §10.8; CODEX_REVIEW_BFT34 R11 / item 5 | Codex-confirmed; re-derived §6.6 |
| 6 | Lemma CEN1 + CEN1-T; Proposition CORNER (fixes Convention C) | §4.1-4.2 | PROVEN-HERE; exact check b4w55_1 P1, P2, P4 |
| 7 | WM^σ (W-mult^σ) | §4.3 | PROVEN-HERE (Convention C) |
| 8 | WC^σ ((W-comm)^σ_J, explicit profile; GAP 1 dissolves for σ > 0) | §4.4 | PROVEN-HERE (Convention C); identity checked b4w55_1 P3 |
| 9 | CCL′ | §5.1 | PROVEN as implication of HR (v); agrees with Codex BFT34 R5 |
| 10 | RWE (cc walk, Π_E inside), WALK^σ | §5.2-5.3 | PROVEN-HERE / implication of 1-3, 7-9 |
| 11 | Theorem H3 (localised source bounds) → Lemma F^σ ((f) in σ-pair form) | §3, §6.2 | PROVEN as implication of 1 + the reading step (R) of Lemma PW |
| 12 | Lemma E2^σ (per-cube energy, direct form); Corollary E3^σ ((E3^∇) in σ-pair form) | §6.3 | PROVEN as implication of 1 (Codex KOFF §4.3 (1) complexified) |
| 13 | Lemma Dcc (clause (d): holomorphy, s ≡ 1 identity, splitting) | §6.4 | PROVEN-HERE |
| 14 | Lemma UQ, Lemma IDcc ((I-id)) | §6.5 | PROVEN as implications of 1-4, 13 |

**Every item of BFT34_55's ARGUED list for BFT-4 (a) is now written:** (H3)_m → item 11; (W-comm)^σ_J → item 8; W-mult^σ → item 7;
σ-pair (f) → item 11; σ-pair (E3^∇) → item 12 (and superseded by E2^σ); §10.8 clause (d) on the P_cc family → item 13, with one
**design change** that the transfer needed and BFT34_55 did not have: Π_E inside every P̃_□ (without it (I-id) needs nonlinear
orbit coverage, NOT-VERIFIED).

**Consequences for BFT-3 on 𝒞_glob (no new input).**
- *Route C* (BFT34_55 Theorem BFT3-glob; Codex BFT34 R3: valid conditional locality, with its same-link E completion): its
  premise (H3)_μ is Theorem H3; its premise (H2)_μ is either the banked COFM55/GV55 chain (0 < μ ≤ m_Y) **or** Corollary H2W
  (0 < μ ≤ μ_W, from μ = 0 inputs). So BFT-3 on 𝒞_glob (n ≤ 4; rates μ/4 for x/U, μ/3 for E) is PROVEN as an implication of
  banked inputs on either supply.
- *Route T* (Proposition TREE, Codex BFT34 R9: conditional on (H2)^Lip_μ and multiplicative (H3)^Lip_μ): both are now supplied
  (Corollary H2W, Theorem H3 (c)), so the rates μ, 3μ/4, 2μ/3, 5μ/8 (U) and μ, 3μ/4, 2μ/3 (E) hold for 0 < μ ≤ μ_W.
- *All orders, order-independent rate:* Theorem BFT4a-glob plus lane B's Corollary BB-4c (iv) in Codex BFT34 R10's repaired form
  (attachment cost −3n/2, prefactor 81n!((N² − 1)^{1/2}/ρ_c)^ne^{3m_0n/4}C_0, rate m_0/(8M_c)) gives the E-part at every order on
  (PD-glob) — R(X) depends on B only on X^{(5)} ⊂ X^+ (M_c ≥ 5), which is what R10's proof uses. I did not re-derive R10's
  constants (spot-checked the geometry only).

---

## 8. What is not closed, and why (appended ≈04:25Z)

1. **Locally gauge-invariant pieces (BFT-4 (b)).** Not attempted. Lane B's route (Theorem BB-gi_k) needs (CovLift) — "[S26-BANKED]:
   the full nonlinear (CovLift) bound is NOT-VERIFIED" — plus (Mult-Y), (Pair-loc), (I-id)_Z. WC^σ's mechanism (σ-summable
   commutator rows) plausibly covers (Mult-Y), but I have not checked its statement. **Status: NOT-VERIFIED (OPEN).**
2. **BFT's class off 𝒞_glob (PD-curv).** Everything here is on the global-gauge polydisc (PD-glob); BFT-0 itself is OPEN off
   𝒞_glob ((G♯-patch), (UHL), (SL-cov), smooth lift). Unchanged.
3. **Identification with the per-level branch action.** E_k^br here is the composite critical value 𝔉_k(x(B); B) (Balaban's
   convention); its identification with PROOF's per-level tower needs (NSL)_j — NOT-VERIFIED (Codex GV items 4-5).
4. **Numbers.** η_*, K, c_D, C_Φ's domain, G_♯, C_Π, C_GV are finite but not computed (inherited from Codex KOFF §4.3's
   "No numerical value of its radius or higher Taylor constants is claimed" and the uncomputed package constants). Hence μ_W,
   R_W, ε_cc are existence statements; whether μ_W ≷ m_Y is undecided.
5. **The lane-A linear package.** Every banked input above is conditional on it (Codex KOFF item 5, Codex GV items 2/6).
6. **The reading step (R)** of Lemma PW ("every banked source bound is a per-density bound on its local constraint set") is a
   reading of the cited proofs, not a theorem proved here; it is the single place where Theorem H3 rests on an interpretation.
   A Codex check should test it on ROW^{(σ)} (a)'s BCH₂ row and Codex KOFF §4.3 (2).
7. **The optional strengthening ||R_{k+1} − R_k||_𝒜 ≤ C_0λ^k** — not addressed (lane B's B4-F1 obstruction in ||·||_𝒜 stands).
8. **No item of the brief's list turned out false.** The one false statement found is conventional: W-mult^σ (and the natural
   (W-comm)^σ representation) **fail under the lane's default lower-corner positions** (Proposition CORNER, with an explicit
   unbounded family); they hold under the centred convention, which is free to choose and is fixed here.

---

## 9. Check record (criteria before scripts; exact arithmetic) (appended ≈04:35Z)
- **b4w55_1** — criteria `checks/b4w55_1_criteria.md` (written 03:17:34Z, before any b4w55 script); script
  `checks/b4w55_1_cen1.py` (written 03:18:48Z); one run 03:19:13-03:19:25Z with `python3 -I -B`, output `checks/b4w55_1.out`
  (stderr `checks/b4w55_1_err.txt`: timing only). **OVERALL: PASS**, d = 2 and d = 3, L = 3, T_c = 4:
  P1 (CEN1 exact) 0 nonzero of 128 (d = 2) and of 1728 (d = 3) entries; P2 (Taylor bound, three seeds) holds, largest
  |comm|/bound 0.0107 / 0.0045 (informational: the bound is crude); P3 (exact commutator representation, three seeds) holds;
  P4 (Convention K leaves exactly ((L−1)/2)(b·𝟙)L x̄_μ ≠ 0) holds at every coarse link; P5: row max 43/9 ≤ 7 and 499/81 ≤ 9,
  column max 1 ≤ 13/3 and ≤ 55/9, max |m_a − m_c|_1 = 3 ≤ 7/2 and 4 ≤ 9/2. Controls: K1 (non-centred contours), K2 (corner
  positions in P1), K3 (drop j^S in P3), K4 (one weight + 1/997) **all fired**.
  *What it cannot decide (stated in the criteria):* k-uniformity, d = 4, the nonlinear S4′ contours, any 𝔐^{(σ)}/N^{(σ)} norm
  bound or analytic estimate. It decides the exact algebra on which CEN1, CORNER and WC^σ's representation rest, and three
  counting constants in d = 2, 3. *Could it have failed?* Yes: P1 fails under either control K1 or K2 (shown), and P4 would
  fail if the corner offset were not exactly ((L−1)/2)h_l𝟙 relative to the contour centre or if Q did not map constants to L×.
No other numeric work was done.

## 10. Errata to §1-§8 (appended ≈04:35Z after a full re-read; nothing above is edited)
- **E1 (§5.4 vs §6.4 — a symbol collision I introduced).** §5.4's walk threshold "R_W := 2R^0_W" (a number) and §6.4's cube-family
  threshold "R_W(s̄)" (a function of s̄) are different objects. **Read §5.4's R_W as R_H** (and μ_W = ln 2/(16R_H + 80)).
- **E2 (§3.4 (P1), the Schwarz chain).** Read: |h(1)| ≤ (2η/η_*)·2c_Dλ_D(η_* + 1) = 4c_Dλ_Dη(1 + 1/η_*) ≤ 8c_Dλ_Dη(1 + 1/η_*).
  The "·…" in the printed chain is a typo; the stated bound holds with a factor 2 to spare. (P2): Cauchy gives 2c_D(1 + η_*)|b|;
  the printed 4c_D(1 + η_*) is also valid.
- **E3 (§3.4 (P3)).** For general directions the right side carries Π_i𝒩_D(u_i) (the largest local quantity of u_i on supp D);
  the printed form is the normalised case u_i ∈ 𝒦_D(1). Multilinearity gives the general case.
- **E4 (§4.2 (a), full Convention K).** If every level sits at its lower corner, the level-l link midpoints also shift (by
  o_l := ((L^l − 1)/2)L^{−k}𝟙); the relative offset between c and its contour centre is still ((L − 1)/2)h_l𝟙 = o_{l+1} − o_l,
  and (a) holds with φ replaced by its translate φ(· − o_l) in the first term; the offset term is
  (φ(m_c − o_l) − φ(m_c − o_{l+1}))·Lx̄_μ. At l = 0 (used in (b)) o_0 = 0, so (b)'s proof is exactly as written.
- **E5 (§4.2 (b), an error term).** The centred commutator contributes C_Qh_0³/ℓ′² to |r_0(φx)|, i.e. **C_QL^{−(2+σ)}L^{(σ−1)k}/ℓ′²
  ≤ C_QL^{−3}/ℓ′²** to the σ-weighted residual leg — bounded, **not** O(L^{−k}) (at σ = 1 it is O(1)). Corrected conclusion:
  ||φx||_{(σ)}/||x||_{(σ)} ≥ (L − 1)L^{σ(k−1)−1}/(16ℓ′) − C_QL^{−3}/(2ℓ′²) − O(L^{(σ−1)k}), still unbounded in k for σ > 0.
- **E6 (§4.4, typo).** "B_c := Σ_lb_l·ℓ... =" reads **B_c := 2(d − 1) + Σ_lb_l ≤ 2(d − 1) + κ_+c_colδ_*L²/(1 − L^{−σ})**.
- **E7 (§6.3, an undefined constant).** C′_{E2} := 4C_{E2} (the gradient pairings at 0 and at zu add ≤ ½·2C_{E2}(·)·½ and
  ≤ ½·2C_{E2}(·)·1.5 respectively, by Cauchy in t of radius ½); and C_3 may be taken 2.25C′_{E2}(ρ_E + ||B||)/ρ_E² (the printed
  27/8 is a valid larger value).
- **E8 (complex sources; all of §5-§6).** The banked linear estimates (G_♯, EP-bd's C_Π) are for real sources/fields; for complex
  ones split real and imaginary parts: **read G_♯ → 2G_♯ and C_Π + 1 → 2(C_Π + 1) wherever a complex s, view or source enters**
  (GV55 §3.1 makes the same remark). Pointwise bounds (CEN1-T, WM^σ, WC^σ, E2^σ) hold for complex fields as written.
- **E9 (§5.3, a count).** n_R = 6^d is conservative; 4^d suffices for R ≥ 14 (a window of length 2R + 14 meets at most 4
  consecutive intervals of length ≥ R). No statement changes.
- **E10 (§2.1).** "the two differ by < ½ coarse unit in ℓ^∞" — the offset o_l < ½L^{l−k} ≤ ½ coarse unit per coordinate, i.e.
  ≤ 2 in ℓ¹, giving the factor ≤ e^{2μ} stated. Correct as written; recorded because §4.2 depends on the same offsets.

---

## 11. Findings, claim by claim (verdict; file + locating string; reason) (appended ≈04:45Z)

**Claims of others that this work rests on or settles.**
- **V1 — BFT34_55 §1.5 row "(H3)_m | finite range of every row of S̃ … ARGUED (… plausible, standard)". CONFIRMED** — Theorem H3
  (§3) proves it, with the 1-Lipschitz and multilinear forms, as an implication of the banked per-density bounds; one reading
  step (R) is named.
- **V2 — BFT34_55 §2.5 "(W-comm)^σ_J — ARGUED (GAP 1 dissolves in the σ-pair with the J slot)". CONFIRMED** under Convention C
  (WC^σ, §4.4): explicit representation (exactness checked b4w55_1 P3), R(σ)-slot by CEN1-T, J slot with profile
  b_l ∝ L^{−σ(k−1−l)}, k- and T-uniform for every σ ∈ (0, 1].
- **V2b — BFT34_55 §2.5 "π_l ≲ L^{3+σ}L^{−σ(k−l)}||u||/ℓ" as read off its displayed own-unit bound. REFUTED (arithmetic)**, agreeing
  with Codex BFT34 R6: from "own ≲ L²·(L^{−(k−l)}/ℓ)·|r_l(u)|_own" the conversion gives L^{4+σ}L^{−σ(k−l)}. My independent
  constant is κ_+c_colδ_*L^{2+σ}L^{−σ(k−l)}; summability for σ > 0 is unaffected.
- **V3 — BFT34_55 §2.5 "W-mult^σ, which needs CEN1 for the residual leg: r_j(ψx) = ψr_j + [Q, ψ]x_j and the σ-weight is again
  beaten by L^{−3(k−j)}" (ARGUED). CONFIRMED with a binding convention fix** (WM^σ, §4.3): true when cutoffs are evaluated at
  contour centres (Convention C); **false** under the lane's default lower-corner positions (Proposition CORNER: an explicit
  family with ratio ≥ (L − 1)L^{σ(k−1)−1}/(16ℓ′) − O(1), unbounded in k).
- **V4 — BFT34_55 §2.5 "Corollary RW-cc-walk — PROVEN as an implication … for every 1-Lipschitz f and every m < m_W :=
  log(1/ε_W)/(2R + 6) the conjugated walk converges … (H2)^Lip_m holds at the trivial chain … from m = 0 inputs only".
  REFUTED as printed**, agreeing with Codex BFT34 R7 on all three counts (ℓ^∞ reach used as an ℓ¹ radius; e^{μf}R̃e^{−μf} is not an
  endomorphism of the cc class; norm and final-projection estimates missing). **Correct statement: Corollary H2W** (§5.4):
  μ_W = ln 2/(16R_H + 80), Π_E inside every piece, box-indexed scalar weights — PROVEN as an implication here.
- **V5 — BFT34_55 §2.5 "Proposition RW-cc (exact)" with erratum E2 ("the single c_□ ARE cc"). CONFIRMED** (RWE (a)-(d), re-derived;
  agree with Codex BFT34 R5), and strengthened: with Π_E inside each piece the walk is the S_E inverse itself (RWE (e)).
- **V6 — BFT34_55 §2.5 "Lemma CCL … J(P^TD^⊥(χy)) ≤ (dM_γ/((L − 1)ℓ))·J(y)". CONFIRMED** (CCL′; 216 at d = 4, L = 3, ℓ = ¼;
  agree with Codex R5). Its exactness needs Convention C (§2.1 (i)); under Convention K Σ_lev^{(l)T}(χ d*j_l) ≠ χ·D(y) and an extra
  charge of the same order appears (same bound up to a factor; not pursued).
- **V7 — BFT34_55 §2.6 (a) "the nonlinear per-cube sources P_cc-projected as in KFACTOR_OFF55's S̃, so that at s ≡ 1 the fixed
  point is CCP (d)'s slice critical point". NOT-VERIFIED (a missing step).** With the RW-cc parametrix P̃y = Σ_□ψ_□ι^*u_□ the s ≡ 1
  point A′ solves HA′ = −P_cc(g + 𝔑(A′)), hence (P_cc + Lemma CD + CCP (c), §6.5) **is** a critical point of F, but it is not in
  Ker Γ (a cut-off local slice field is generically not in S_E), so CCP (d) does not apply, and identifying A′ with x(B) — or
  even E(A′) with E_k^br — needs nonlinear gauge-orbit coverage, NOT-VERIFIED (Codex KOFF item 5, Codex GV item 5). Repaired by
  the design change Π_E inside each piece (Lemma IDcc). I do not claim A′ ≠ x(B)-up-to-gauge.
- **V8 — BFT34_55 §2.6 (a) "the transfer of lane B's clause (d) (s ≡ 1 identity, splitting) to the P_cc-projected family [ARGUED:
  P_cc's routing stays inside the coarse cells it touches …]". CONFIRMED** (Lemma Dcc, distances rechecked for product partitions
  and Π_E's reach 4).
- **V9 — BFT34_55 §2.6 (a) "the σ-pair forms of lane B's (f) … and (E3^∇) … [ARGUED]". CONFIRMED** (Lemma F^σ; Corollary E3^σ),
  with the finding that in the σ-pair (E3^∇) and Lemma W-grad0 are unnecessary (Lemma E2^σ: the per-cube energy is
  level-summable directly).
- **V10 — BFT34_55 §2.6 (a) "status of (a): NOT-VERIFIED — reduced to the ARGUED items listed, all local". CONFIRMED as a
  reduction** (every listed item is now written), except that the reduction silently needed the design change of V7.
- **V11 — BFT_A BA-12 "CEN1 … PROVEN-HERE". CONFIRMED** (Lemma CEN1, exact; b4w55_1 P1), its evaluation point made explicit.
- **V12 — BFT_B §10.3 "Lemma W-mult: PROVEN-HERE, with a corrected constant" (σ = 0). CONFIRMED** (re-derived (1)-(4); it is
  convention-blind, CORNER's σ = 0 remark).
- **V13 — BFT_B §10.8 (iii) / BFT34_55 §2.3 combinatorial core (cluster identity, 2^{40}C_E(2^{41}/(s̄ − 1))^{|X|−1}, (80e)^{n−1}).
  CONFIRMED** (re-derived §6.6; agree with Codex BFT34 R11), stated with the uniform-anchor norm (Codex R8).
- **V14 — BFT_B §10.7 [RBB3-fix RW3-2] "x″-argument". CONFIRMED** (re-used in RWE (c)).
- **V15 — BFT_B §9.6 "RW∇-F3 (naive energy bound grows with k) … OCCURS". CONFIRMED at σ = 0** (Lemma E2^σ's level sum is k at
  σ = 0) and **does not occur at σ > 0**.
- **V16 — BFT34_55 §1.5 "HR's routing paths stay in one parent block per level, total coarse length ≤ d/2 = 2". CONFIRMED**
  (Σ_jd(L − 1)/2·L^{j−k} ≤ d/2); Lemma FR uses the cruder cell diameter.

**New results of this file (status, not verdicts).** N1 Lemma LD, N2 Lemma OV — PROVEN-HERE (elementary). N3 Theorem H3 — PROVEN
as an implication (reading step (R)). N4 Lemma CEN1 + CEN1-T — PROVEN-HERE (b4w55_1 P1, P2). **N5 Proposition CORNER — PROVEN-HERE
(b4w55_1 P4): W-mult^σ is false under lower-corner positions.** N6 WM^σ, N7 WC^σ — PROVEN-HERE (Convention C). N8 CCL′ —
implication of HR (v). N9 RWE — PROVEN-HERE. N10 WALK^σ, N11 Corollary H2W — implications. N12 F^σ, N13 E2^σ (+ E3^σ) —
implications. N14 Dcc — PROVEN-HERE. N15 UQ, N16 IDcc, N17 Theorem BBcc, **N18 Theorem BFT4a-glob** — implications. N19 BFT-3 on
𝒞_glob via routes C and T with the H2W supply — implication.

## 12. Summary table

| # | Claim (file, locating string) | Verdict / status | Where |
|---|---|---|---|
| V1 | BFT34_55 §1.5 "(H3)_m … ARGUED" | CONFIRMED (Theorem H3) | §3 |
| V2 | BFT34_55 §2.5 "(W-comm)^σ_J — ARGUED (GAP 1 dissolves …)" | CONFIRMED (Convention C) | §4.4 |
| V2b | BFT34_55 §2.5 exponent "L^{3+σ}L^{−σ(k−l)}" | **REFUTED** (arithmetic; = Codex R6) | §4.4 |
| V3 | BFT34_55 §2.5 "W-mult^σ, which needs CEN1 …" | CONFIRMED with binding convention fix (false under K) | §4.2-4.3 |
| V4 | BFT34_55 §2.5 "Corollary RW-cc-walk … m_W := log(1/ε_W)/(2R + 6)" | **REFUTED** as printed (= Codex R7); repaired as H2W | §5.4 |
| V5 | BFT34_55 §2.5 "Proposition RW-cc (exact)" + E2 | CONFIRMED (= Codex R5) | §5.2 |
| V6 | BFT34_55 §2.5 "Lemma CCL" | CONFIRMED (216; = Codex R5) | §5.1 |
| V7 | BFT34_55 §2.6 (a) "at s ≡ 1 the fixed point is CCP (d)'s slice critical point" | **NOT-VERIFIED** (missing orbit step; repaired by Π_E inside) | §6.5 |
| V8 | BFT34_55 §2.6 (a) clause-(d) transfer | CONFIRMED | §6.4 |
| V9 | BFT34_55 §2.6 (a) σ-pair (f), (E3^∇) | CONFIRMED (+ E2^σ makes (E3^∇) unnecessary) | §6.2-6.3 |
| V10 | BFT34_55 §2.6 (a) "reduced to the ARGUED items listed" | CONFIRMED as a reduction (modulo V7) | §7 |
| V11 | BFT_A BA-12 CEN1 | CONFIRMED (exact, b4w55_1 P1) | §4.1 |
| V12 | BFT_B §10.3 Lemma W-mult (σ = 0) | CONFIRMED | §4.3 |
| V13 | BFT_B §10.8 / BFT34_55 §2.3 combinatorial core | CONFIRMED (= Codex R11) | §6.6 |
| V14 | BFT_B RW3-2 x″-argument | CONFIRMED | §5.2 |
| V15 | BFT_B RW∇-F3 | CONFIRMED at σ = 0; absent at σ > 0 | §6.3 |
| V16 | BFT34_55 §1.5 routing length ≤ d/2 | CONFIRMED | §3.3 |
| N3 | Theorem H3 ((H3)_μ, 1-Lipschitz, multilinear) | PROVEN as implication (reading step (R)) | §3 |
| N4-N7 | CEN1, CORNER, WM^σ, WC^σ | PROVEN-HERE (b4w55_1 PASS) | §4 |
| N8-N11 | CCL′, RWE, WALK^σ, H2W ((H2)^Lip_μ from μ = 0) | implication / PROVEN-HERE | §5 |
| N12-N16 | F^σ, E2^σ/E3^σ, Dcc, UQ, IDcc | implication / PROVEN-HERE | §6 |
| N17-N18 | Theorem BBcc, **Theorem BFT4a-glob** | PROVEN as implication | §6.6, §7 |
| N19 | BFT-3 on 𝒞_glob, routes C and T, with the H2W supply | PROVEN as implication | §7 |
| — | b4w55_1 | PASS (all gates; all four controls fired) | §9 |

**Counts (claims of others): CONFIRMED 14 (V1-V3, V5, V6, V8-V16), NOT-VERIFIED 1 (V7), REFUTED 2 (V2b, V4).**

## 13. Codex verdicts used — agree or disagree, explicitly (files as on disk at ≈03:2xZ; all complete)
- **CODEX_REVIEW_KOFF items 1-5: AGREE.** Item 1 (HR): used pointwise (Lemma PWR). Item 2 (CCP (a)-(d)): used (c) and both
  halves of (d) (UQ, IDcc). Item 3 (SG, LA-1 REFUTED → LA-1′, local analytic completion): I re-checked the LA-1 refutation (at
  M = I, W_0 = M to first order, so δ(W_0^{−1}M) = 0 ≠ Q) — agree; the completion's per-density structure is my reading step (R).
  Item 4 (CB): its level sums used. Item 5 (corrected K^{(σ)}): K and G_♯ used.
- **CODEX_REVIEW_GV items 2-6: AGREE.** GV-E (G_gv), BFT-E (x(B), slice uniqueness, holomorphy, composite value) used; item 5
  (slice not preserved under restriction; NSL NOT-VERIFIED) is why E_k^br here is the composite value; item 6 (GV-E_m) is the
  alternative (H2)_μ supply, with Codex BFT34 R4's e^{8μ} small-torus correction.
- **CODEX_REVIEW_GSHARP item 1, §2.5, §6: AGREE** (EP algebra, Ker H = 𝒢_0, EP-opt, EP-bd at zero weight, finite ℓ¹ reach; I use
  only the unweighted EP-bd plus reach, never a weighted projection bound).
- **CODEX_REVIEW_C2 item 4 (Lemma CD, root-pinned):** used as banked via PROOF's [S26-BANKED] bullet; **I did not re-read
  CODEX_REVIEW_C2** (not verified by me beyond that bullet).
- **CODEX_REVIEW_COFM items 2-3:** used only as the alternative supply of (H2)_μ; agree as banked, not re-derived.
- **CODEX_REVIEW_BFT34:** R1 AGREE; R2 AGREE (μ vs q; no σ-residual level sum anywhere here; product-form comparison §2.2);
  R3 AGREE (same-link E completion carried in §7); R4 AGREE (e^{8μ}); R5 AGREE (re-derived; extended with Π_E inside); R6 AGREE
  (V2b); R7 AGREE on all three points (V4; H2W is the repair it proposes); R8 AGREE on the uniform-anchor norm (CX itself not
  used); R9 not used beyond Proposition TREE's premises; R10 AGREE on the geometry (spot-checked; constants not re-derived); R11
  AGREE. **No Codex verdict was found wrong.**

## 14. For the lead (short)
1. **BFT-4 (a) on 𝒞_glob, every k, every T: PROVEN as an implication** (Theorem BFT4a-glob) of [S26-BANKED] inputs plus this file —
   bounded, local, constant-gauge-invariant polymers for the composite critical value on the global-gauge polydisc. Not
   cross-family checked. BFT-4 (b) (locally gauge-invariant pieces; needs (CovLift)) and (c) (off 𝒞_glob) are unchanged.
2. **Every ARGUED input of BFT34_55's reduction is now written:** (H3)_m (Theorem H3), (W-comm)^σ_J and W-mult^σ (GAP 1 dissolves for
   σ > 0), σ-pair (f), (E3^∇) (and the stronger finding that the σ-pair needs no trapezoid form), clause (d) on the P_cc family.
3. **One design change was necessary** and BFT34_55 lacked it: the S_E projection Π_E inside every box piece of the walk. Without
   it the s ≡ 1 point of the family is a critical point outside the slice (V7, NOT-VERIFIED identification).
4. **One binding convention:** cutoffs must act at contour centres (Convention C). Under the lane's default lower-corner positions
   W-mult^σ is **false** (Proposition CORNER, unbounded family), for every σ ∈ (0, 1].
5. **(H2)^Lip_μ now has a second supply from μ = 0 inputs only** (Corollary H2W, the repaired RW-cc-walk; BFT34_55's printed
   corollary must not be banked — Codex R7). With Theorem H3 this makes BFT-3 on 𝒞_glob (route C, and route T's better rates) an
   implication of banked inputs on either supply.
6. **Suggested Codex check, in this order:** Proposition CORNER + Lemma CEN1 (short, exact); Lemma PW's reading step (R) on
   ROW^{(σ)} (a) and Codex KOFF §4.3 (2); WC^σ's J profile; RWE (e) + Lemma IDcc (the slice-inside design); Corollary H2W's
   read/write regions; Lemma E2^σ's holomorphic form of the soft density.
7. PROOF.md's tally counts its 105 items and does not move; HANDOFF's critical path should replace "BFT-4 (a): reduced to ARGUED
   local items" by "BFT-4 (a) on 𝒞_glob: implication (BFT4W55, pending Codex)", and record Convention C as binding.

*File ends here (appended 2026-10-29 ≈03:5xZ; see the final timestamp line).*

---

## 15. Timestamp corrections and a corpus map (appended last)
**Timestamps.** The "(appended ≈…Z)" headings of §2-§11 were written as guesses and are wrong. `date -u` immediately before each
append printed: §2 03:26:58Z; §3 03:29:35Z; §4 03:31:51Z; §5 03:33:52Z; §6 03:36:46Z; §7-§8 03:38:01Z; §9-§10 03:43:09Z;
§11-§14 03:44:47Z. Order of work: brief and rules read 02:46Z; §0 (PRE-STATED) written before any derivation; CODEX_REVIEW_BFT34
read in full ≈03:13-03:20Z, before §2; criteria b4w55_1 03:17:34Z → script 03:18:48Z → single run 03:19:13-03:19:25Z.
**Corpus map (data only; cited, not copied).** The hard-scheme analogues used as a map: Dimock 1108.1335 §2.4 (parametrix from
local Neumann inverses and a quadratic partition of unity; commutator terms of size O(M^{−1})) ↔ RWE/WALK^σ (local S_E inverses
on local tori, commutators O(1/R)); 1108.1335 §2.5, §4.5 (weakened propagators G(s) with complex |s_□| ≤ M^{1/2}, Cauchy in s,
connectedness of surviving polymers) ↔ Construction BBcc and the cluster identity of §6.6; 1212.5562 §3.7 (a "more local
minimizer" built from the weakened propagator) ↔ the family fixed point 𝐀(s); 1108.1335 §4.6 ↔ §6.6's polymer bound. Two
differences the soft composite setting forces and the corpus does not show: (i) the commutators must be **level-summable**
across the k levels of one composite operator (WC^σ's profile, which needs σ > 0 and Convention C), and (ii) the gauge slice
must be imposed **inside** each local piece (Π_E in P̃_□) so that the s ≡ 1 point is the slice critical point.
