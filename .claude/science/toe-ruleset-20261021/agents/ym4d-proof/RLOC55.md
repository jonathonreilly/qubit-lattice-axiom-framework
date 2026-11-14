Reviewer model: claude-opus-5-5

# RLOC55 — premise (R): the banked source estimates, localised to individual densities (worker file, Opus 5.5)

UTC start: 2026-10-29T04:18:23Z (from `date -u` immediately before this file was created).
Role: worker (brief `queue/rloc.md`; shared rules `REVIEW_BRIEF_55.md` apply). No git. This file and `checks/rl55_*` are
the only files written. Append-only. Read before this section was written (no derivation yet): the brief, the shared rules,
CODEX_REVIEW_BFT4W.md (all 249 lines; it ends with its "Exactly what may be banked" list and the sentence naming (R) as
"Single most dangerous unverified input", so it is finished), BFT4W55.md §0-§3 and §6.1-§8 (headings "0. PRE-STATED" through
"8. What is not closed"), KFACTOR_OFF55.md l.1-330 ("PRE-STATED" through "3.6 Reading"), CODEX_REVIEW_KOFF.md l.1-560 and
l.700-754, PROOF.md l.1-35 ([S26-BANKED] incl. the "BFT-4 (a) on 𝒞_glob — CONFIRMED conditionally, with one named premise (R)"
bullet), HANDOFF.md (head).

## 0. PRE-STATED (statements only; written before any derivation)

**The premise under test** (brief, quoting PROOF.md [S26-BANKED] and CODEX_REVIEW_BFT4W §W1 / final item):
> (R): per-density / per-pair holomorphic estimates on properly defined LOCAL constraint sets — every bound of ROW^{(σ)} (a)-(b)
> and of Codex KOFF §4.3 (1)-(3) (and CB) holds as a bound on each individual local density and its derivatives, on a local
> constraint ball with an explicit boundary convention (fixed enlarged patch, or a restricted seminorm with an extension
> theorem), including the cutoff plain-current Hölder/routing bounds.

**Targets.**
- **T1 (provenance, one verdict per bound).** For each bound in (R) — ROW^{(σ)} (a): the BCH₂ row R^B_l, BA-6's residual part
  κ_lρ^{(2)}_l, CR-1's s^C_l, the Wilson q-bounds (Corollary WR (a)), the plain Wilson row R^W_0 and its pointwise Hölder seminorm;
  ROW^{(σ)} (b) and Codex KOFF §4.3: (1) |ρ_l − r_l| and its difference, (2) the plain soft current κ_lE_l at levels l and l + 1,
  (3) the residual slot κ_l(Ψ_l − r_l), the Wilson all-order estimates for G_0 and j_W (sizes and Hölder); CB: the routing of the
  plain rows by HR (iii)/(iv) — locate the actual proof (file + locating string; drift reported) and decide whether it is
  ALREADY LOCAL (it bounds one density's slot by input local quantities on a fixed neighbourhood, k-, T-independent in coarse
  units) or GLOBAL (it uses a global inverse, a global contraction, a global norm in an essential way, or a sum over densities
  that could cancel).
- **T2 (local statements).** Define, explicitly, (i) the densities and the slot representation of each Y_D; (ii) for each density
  (and each Hölder pair) a FIXED ENLARGED PATCH Ω_D (finite set of variables, coarse ℓ¹ radius independent of k, T) and a local
  seminorm ν_D on the variables of Ω_D whose unit ball contains the restriction of every x with ||x||_{(σ),hom} ≤ 1; (iii) the
  complex local constraint set 𝒦_D(r) := {ν_D ≤ r, |B_c| ≤ r}. State each bound of T1 as a bound on 𝒦_D(η) with its level factor,
  and prove it (as a corollary of a local proof, or by a new local proof where the existing proof is global).
- **T3 (the slotwise linear cancellation).** Prove that every slot of the chosen representation of Y_D has zero x-derivative at
  (x, B) = (0, 0) slotwise (not only as a covector), as Lemma PW (P1) needs (Codex W1: "the missing local input must establish
  it slotwise").
- **T4 (Cauchy, d = 4, multilinear weights).** Check that the passage from 𝒦_D-bounds to vertex bounds has no loss depending on
  the number of variables of Ω_D (which is ~ (L^k)^4 for patches of coarse radius O(1)), on k or on T; and that the multilinear
  weights of H3 (c) are supplied.
- **T5 (cutoffs and routing).** The cutoff plain-current Hölder and routing bounds (HR (iii)/(iv) applied to η_Q-multiplied plain
  slots) as local statements: the routed current at a link reads only plain slots in that link's level-k cell, and its bound uses
  only per-density (per-pair) quantities.
- **T6 (assembly).** Either (R) PROVEN as an implication of named banked inputs (listed exactly), or the precise local estimate
  that fails, with a counterexample satisfying its hypotheses. Then the list of conditional banked items that become
  unconditional-on-(R) (i.e., whose remaining premises are the other named ones only).

**What would count as a refutation of (R) (or of a step of it).**
- **F1 (level factor not local).** A density D at depth q and a configuration in 𝒦_D(η) (any fixed patch radius) at which a slot
  exceeds c_Dλ_Dη² by a factor unbounded in k or q: the decay L^{−σq} (plain soft) or the residual normalisation is then a
  property of the aggregate, not of the density.
- **F2 (cross-density cancellation).** A bound in T1 whose proof needs cancellation between slots of different densities, with an
  explicit configuration where the individual slots are larger than the per-density bound allows.
- **F3 (non-local input).** A per-density bound whose proof needs a quantity not controlled by any fixed-radius local seminorm
  (e.g., a global Poincaré/gauge argument for potentials, a global Campanato bound, a global inverse).
- **F4 (slotwise linear term).** A slot of the representation with non-zero x-derivative at (0, 0).
- **F5 (Cauchy / quantifier).** A Cauchy or Schwarz loss growing with the number of variables, with k or with T; or a multilinear
  weight quantifier that the local bounds do not supply.
A step I cannot settle is reported NOT-VERIFIED with what is missing. Verdict vocabulary: CONFIRMED / NOT-VERIFIED / REFUTED for
claims inherited from files; for my own statements PROVEN-HERE (complete proof in this file), ARGUED, OPEN, FALSE (counterexample).
Numeric checks, if any: criteria file `checks/rl55_<n>_criteria.md` first, then the script, exact rational arithmetic only.

---

## 1. Read record and symbols pinned (appended 2026-10-29T04:42Z, after §0)

**Read, by locating string (bounded ranges; all files as on disk now).** Beyond the §0 list:
- BFT_A.md: §1 ("1.1 The composite problem" … "1.4 The pair"), §2 lemma statements (BA-1 … BA-12), §3.3 "BA-3", §3.4 "BA-4 (CEN2)",
  §3.5 "BA-5", §3.6 "BA-6", §6 "[RBA1-fix] F5" and "F6", §7.2 "Norms" (Campanato and pointwise seminorms), §7.3 "Lemma BL-C",
  §8.4 "BL-C: PROVEN-HERE", §12.0-12.1 ("Soft rows (second order, level l)", "Lemma CR-1"), §13.5 "Lemma CR-1: PROVEN-HERE",
  §26.0-26.1, §28.6 "Corollary WR".
- REVIEW_BFT_A_S6.md "Corollary WR (28.6 …)" (fix P6-2). PROOF.md "Lemma NA-alg (explicit su(N) algebra" (now at l.3232-3266;
  CODEX_REVIEW_HIGHER §8 recorded it at 3215-3250 — **drift +17**, content as reviewed), "Decision 4: the RG kernel"
  (M̄_c := (d!L^d)^{-1}Σ_σΣ_{y∈B(X)}T^σ_y), "Lemma TOWER-VAR".
- BFT_B.md §9.0 "Setting W", "Lemma W-cut" statement and §10.2 proof (η_Q has scale ½: |∂_μη_Q| ≤ 2).
- KFACTOR_OFF55.md §1-§3 (incl. "2.1 Lemma SG", "2.2 Proposition ROW^{(σ)}" with its erratum, "3.3 Lemma HR", "3.5 Proposition CB").
- CODEX_REVIEW_KOFF.md §1-§5 and "Exactly what may be banked" (complete; ends with item 7).
- CODEX_REVIEW_BFT34.md R3-R5; BFT34_55.md §1.1-1.4 ((H1)-(H3)_m, Lemma WD, Proposition TREE).
- HIGHER55.md §3-§4 ("3.1 A-priori own sizes" … "4.3 Proposition HS"); **CODEX_REVIEW_HIGHER.md, all** (complete: it ends with
  "Exactly what may be banked" item 5). This review was not in the brief's list; it is directly relevant because it already
  checked, cross-family, the per-density analytic inputs (its item 1: "existence of k-, T- and level-independent analytic
  constants … |ρ−r| ≤ C ε_l³η² … NC3 … FAC").
- checks/hg55_1_criteria.md and hg55_1_out.txt (exact d = 4 check of BA-4; CODEX_REVIEW_HIGHER §7 reproduced it).
- BFT4W55.md §3.4-§3.6, §6.2-§6.3, §7-§8, §10 (E2, E3, E7).

**Symbols (systemic defect 1 — every collision below was met in the read files).**
- **m := k − 1 − l** for a soft density at level l (fine variables x_l, coarse link c at level l + 1). **h := h_l := L^{−(k−l)} =
  L^{−(m+1)}**. Collisions: BFT4W55 writes this m as **q** ("q := k − 1 − l"); Codex KOFF §4.3 writes **q := k − l** and the same
  h; Codex HIGHER writes **h := k − 1 − l** (a depth, not my h) and **ε_l** for my h; BFT_A §7.2 writes ρ_l. I use only m, h.
- **σ ∈ (0, 1]** = KFACTOR_OFF55's residual-weight exponent. The S4′ axis orders, written σ in BFT_A/PROOF ("T^σ_y"), are written
  **𝔬** here. Lane B's "σ := 2^d s̄" is not used.
- **r** = radius of a local constraint set; **r_l(x)(c)** the linear residual (data-inclusive at the top, r_{k−1} = Qx_{k−1} − B);
  **r^hom** with x_k := 0. **ρ_c** = the nonlinear soft fluctuation log(V^{−1}W_0) (never a radius here).
- **η** = a global-ball radius (BFT4W55's); **η_*** = (R)'s local analytic radius; here it is **r_L** of Theorem LOC (§4).
- **N** = rank of SU(N). **N_c** = the support (level-l links used by the words) of the density at c (BFT_A's N(X, μ), HIGHER55's
  N_c). **N^{(σ)}** = the source norm. Incidence numbers are written **n_inc** (BFT4W55's "N_inc").
- **(R)** = the premise; HIGHER55's analytic radius "R" is written **ϱ_A** and its sup bound "S" is **S_A**; lane B's box side R
  is not used.
- **p_L := 5L − 4** (maximal word length, d = 4). **o := (L − 1)/2**. **n := L^k**.
- 𝔤 := su(N), **𝔤_ℂ := 𝔤 ⊗ ℂ = sl(N, ℂ)**, |·| the Hilbert-Schmidt norm (on 𝔤_ℂ: |X + iY|² = |X|² + |Y|², X, Y ∈ 𝔤), ||·|| the
  operator norm. Complex-bilinear pairing **⟨A, B⟩ := −tr(AB)** (= Re tr(A*B) on 𝔤); its dual norm on 𝔤_ℂ is |·| (𝔤_ℂ is
  *-closed, take a = A*/|A|).

---

## 2. T1 — where each bound of (R) is actually proved, and whether the proof is local (appended 2026-10-29T04:50Z)

Method: for each bound I located the proof by string, read it, and asked what the bound on ONE density's slot is made of.
"LOCAL" below means: the proof bounds the slot of a single density (or a single pair) by input local quantities read on a fixed
set of variables (of coarse diameter independent of k, T), uses no inverse, no contraction, no Poincaré/gauge argument, and no
cancellation between different densities. Every cancellation the proofs use is **inside one density** (or one routing block) and
is an algebraic identity, which holds slotwise.

| # | Bound in (R) | Actual proof (file, locating string) | What one density's slot is bounded by | Verdict |
|---|---|---|---|---|
| 1 | ROW^{(σ)} (a) BCH₂ row π_l(R^B_l) ≤ A_BL^{−σm}η² | KFACTOR_OFF55 "2.2 Proposition ROW^{(σ)}" → (★) = BFT_A "3.6 BA-6" ("of own size ≤ κ·2p_Ls_l·\|r_l\|"), row defined per c in BFT_A §12.0 ("⟨R^B_l, u_l⟩ := 2κ_l⟨r_l(x), B(x_l, u_l)⟩"), B = F6's bilinear form per c | 2κ\|r_l(c)\|·p_Ls_l(c): the residual at c and the own sizes on N_c | **LOCAL** |
| 2 | ROW (a) residual part κρ^{(2)} (BA-6 C_6) | BFT_A "3.4 BA-4 (CEN2)" (avg over (𝔬, y) of BCH₂ vanishes for direction-constant fields: an identity per c; exact in d = 4: hg55_1 A1; proof also Codex HIGHER §2 "B₂=L[D,A_μ]"), "3.5 BA-5" (no quadratic polar term; per c), "3.6 BA-6" ("δ ≤ (diam N(X, μ) ≤ 5L own steps)·L^{−2(k−l)}η (gradient bound)") | s_l, s_{l+1}, \|r_l(c)\| and δ = oscillation of x_l on N_c; δ is bounded by gradients along staircases, which lie in N_c itself (Lemma SUPP, §3.4; rl55_2 Q2) | **LOCAL** (no enlargement needed) |
| 3 | ROW (a) CR-1 s^C = (κ/2)[x_{l+1}, r_l] | BFT_A "13.5 Lemma CR-1" ("pointwise per level-(l+1) link"; ⟨r, [u_{l+1}, r]⟩ = 0 by ad-invariance at that link) | \|x_{l+1}(c)\|·\|r_l(c)\| | **LOCAL** |
| 4 | ROW (a) Wilson q: \|\|q^c\|\| ≤ 9η², [q^c]^∞_α ≤ 4C_qη² | BFT_A "3.3 BA-3" (\|q_p\| ≤ 9s²) per plaquette; "28.6 Corollary WR" (a) ("Let p′ = p + v … \|x_0(b_i + v) − x_0(b_i)\| ≤ \|v\|_1n^{−2}\|\|∇^cx^c_0\|\|_∞"), with REVIEW_BFT_A_S6 fix P6-2 | values on ∂p, ∂(p+v); gradients along a path from p to p+v | **LOCAL** — pair patch (Rect) needed |
| 5 | ROW (a) plain Wilson row R^W_0 and [R^{W,c}_0]^∞_α ≤ C_{W∞}η² | KFACTOR_OFF55 ROW (a) ("For the pointwise coarse Hölder seminorm, translate all factors together … (BL-C)"); BFT_A "8.4 BL-C" | ≤ 6 plaquettes per link; Hölder of the curl f_0 at the translated pair, which BL-C bounds by Campanato oscillations on boxes of side ≤ 1 **containing z or z′** (read off §8.4's proof: D_i(z), D_i(z′), B*) | **LOCAL** — pair patch incl. those boxes (Lemma LBC, §3.4) |
| 6 | ROW (b) / Lemma SG / (LA-1′) / (LA-2) / (LA-3), all orders | KFACTOR_OFF55 "2.1 Lemma SG" (identity per c; Codex KOFF §4.1, Codex HIGHER §4); (LA-1′) Codex KOFF §4.2 ("A_b(x) = W₀(x)⁻¹ ∂M(x)/∂x_b − Q_cb … vanishes at zero"); G − 1 = O(y²) per c (NA-alg (a), last bullet); (LA-2) HIGHER55 "3.5 (LA-2)" | product of a factor Θ_c (\|Θ\| ≤ 2\|ρ_c\|) and a coefficient vanishing at 0 (A_b, Z − id, G − 1), all functions of supp D_c | **LOCAL** |
| 7 | Codex KOFF §4.3 (1): \|ρ_l − r_l\| ≤ Ch³η², difference ≤ Ch³ηδ | CODEX_REVIEW_KOFF §4.3 ("All local variables, including the level-l+1 variable, are O_L(hη) … The quadratic part of ρ−r obeys the BA-4/F6 bound … Taylor's integral remainder …"); HIGHER55 Lemma C2 + CE | own sizes of the variables of D_c, δ, \|r_l(c)\| | **LOCAL** |
| 8 | (2): π_l(κE_l\|_l) + π_{l+1}(κE_l\|_{l+1}) ≤ C′L^{−σm}η² | CODEX_REVIEW_KOFF §4.3 ("SG, (LA-1′), and the derivative product rule now give, at both output levels") | as 6 + 7 | **LOCAL** |
| 9 | (3): L^{(2+σ)m}\|κ(Ψ − r)\| ≤ Cη² | CODEX_REVIEW_KOFF §4.3 ("Ψ−r=(ρ−r)+(Ψ−ρ) and Ψ−ρ=O(ρ³)") | as 7 | **LOCAL** |
| 10 | Codex KOFF §4.3 Wilson estimates (G_0 and j_W, sup and Hölder, all orders) | CODEX_REVIEW_KOFF §4.3 ("translate all its finitely many arguments together … BL-C gives n²F a pointwise C^α bound"); HIGHER55 "3.6 (LA-3) Wilson" | as 4-5 | **LOCAL** — pair patch |
| 11 | CB: J(P^TD^⊥𝔑^0) ≤ K_C(σ)η² (the routing of plain rows) | KFACTOR_OFF55 "3.5 Proposition CB" ("Divergence-form and residual-type sources have D^⊥ = 0 … for any representation"), HR (iii)/(iv) proofs in "3.3 Lemma HR" ("V_i(Z) = Σ_μΣ_{lines}[w(entry link) − w(exit link)] (exact …)") | the telescope is an **identity per block**; the bound uses sup of the plain current on the links crossing one block, or pair differences inside it; CB's J-bound is a sum of per-level sups of these per-block bounds | **LOCAL** per output link (Lemma RT, §7) |
| 12 | cutoff plain-current Hölder (F^σ: "the level-0 Hölder quotient grows by at most 2d·sup (η_Q has scale ½)") | BFT4W55 "6.2 Lemma F^σ" proof; η_Q from BFT_B "10.2 Lemma W-cut" (\|∂_μη_Q\| ≤ 2) | product rule on one pair | **LOCAL** |
| 13 | analyticity / complexification with k-, T-, l-independent constants | CODEX_REVIEW_KOFF §4.3 ("finite-dimensional analytic implicit-function theorem … Complexification gives the same assertion on a smaller complex polydisc"); HIGHER55 "3.2 Lemma AN" (banked: Codex HIGHER item 1) | per density, finitely many types | **LOCAL** by construction |

**Conclusion of T1.** Every proof behind (R) is already local; **no** proof in the list is global in the brief's sense (global
inverse, global contraction, or a sum that could cancel). The banked **statements** are aggregate (stated on the global ball),
and Codex W1 is right that statements alone cannot give (R) (its M a² − M a² example is valid logic). The **proofs** give (R)
once three things the sources leave implicit are written: (i) the local domains with a boundary convention (§3.4; only the
Wilson Hölder **pairs** need an enlarged patch — soft and single-Wilson densities need none, Lemma SUPP); (ii) the bounds re-run
on **complex** local sets (§3.3, §4); (iii) the **slotwise** vanishing of the linear term (§5). Hence the brief's suggested
route — exponential decay of the banked weighted inverse (H2W / CC-INV_m) plus a partition of unity — is **not needed and not
used**: no bound in (R) involves an inverse, and using one would have made (R) conditional on the lane-A linear package.

---

## 3. T2 — the objects: densities, slots, holomorphic continuation, patches and local seminorms (appended 2026-10-29T04:58Z)

### 3.1 Setting
Setting (K) of KFACTOR_OFF55 §1.1: d = 4, N ≥ 2, L ≥ 3 odd, κ_l ∈ [κ_−, κ_+], k ≥ 1, **T ≥ 3**, 0 < α < σ ≤ 1 (α enters only
Hölder/Campanato quantities). Complex configurations x = (x_0, …, x_{k−1}), x_j(b) ∈ 𝔤_ℂ; complex data B_c ∈ 𝔤_ℂ on level-k
links. Coarse units as BFT_A §1.3.

### 3.2 Densities and the slot representation (the one Theorem H3 uses: BFT4W55 §3.2 = KFACTOR_OFF55 SG + LA-3)
𝒟 := {D_p : p a level-0 plaquette} ∪ {D_c : c = (X, μ) a level-(l+1) link, 0 ≤ l ≤ k − 1}; **Y_D := H_Dx − ∇_xD**,
H_D := Hess_xD(0; 0); Y = Σ_DY_D (TOWER-VAR is a sum of these densities).
- **Wilson.** F_p := log(e^{x(b_1)}e^{x(b_2)}e^{−x(b_3)}e^{−x(b_4)}) = (dx_0)_p + q_p(x), D_p := 𝒲(F_p), 𝒲(F) := −tr(cosh F − 1)
  (= Re tr(1 − e^F) for F ∈ 𝔤), ∇𝒲(F) = sinh F − (1/N)tr(sinh F)·1 (gradient for ⟨·,·⟩; on 𝔤 it is Π(sinh F), HIGHER55
  §3.6); H_{D_p}x = d^T(dx_0)_p. Chain rule ∇_xD_p = d^T∇𝒲(F_p) + Σ_{b∈∂p}K_{p,b}^T∇𝒲(F_p), K_{p,b} := ∂q_p/∂x(b). Slots:
  **G_0(p) := (dx_0)_p − ∇𝒲(F_p) = −q_p − g_3(F_p)** (divergence form; g_3(F) := ∇𝒲(F) − F) and
  **j_p(b) := −K_{p,b}^T∇𝒲(F_p)**, b ∈ ∂p (plain, level 0).
- **Soft.** M := M̄_c(x_l) = (24L⁴)^{−1}Σ_{𝔬,y}T^𝔬_y (PROOF "Decision 4"; words of ≤ p_L letters e^{±x_l(b)}), W_0 = e^{X_0} the
  SU(N) maximiser of Re tr(W^{−1}M) (NA-alg (a)), v := x_{l+1}(c) (v := B_c if l = k − 1), V := e^v, ρ_c := log(V^{−1}W_0) =
  BCH(−v, X_0), Θ_c := e^{ρ_c} − 1, G_c := W_0^{−1}M; D_c := κ_lφ̂_c, φ̂_c = Re tr(W_0^{−1}M) − Re tr(V^{−1}M).
  **SG (exact; banked, Codex KOFF item 3 and Codex HIGHER item 3):** ∇_xD_c = κ_lR_c^TΨ_c + κ_lE_c with R_cx := r^hom_l(x)(c) =
  (Q_lx_l)(c) − x_{l+1}(c) (x_k := 0), **Ψ_c := Π(−Θ_c^*) = sinh ρ_c − (1/N)tr(sinh ρ_c)** (on 𝔤: −Θ* = 1 − e^{−ρ}, whose
  anti-Hermitian part is sinh ρ), and the plain current E_c with components
  ⟨E_c(b), a⟩ = −Re tr(Θ_cA_b[a]), **A_b[a] := W_0^{−1}∂_bM[a] − Q_{cb}a** (b ∈ N_c; (LA-1′), W_0 frozen);
  ⟨E_c(c), a⟩ = Re tr((Z[a] − a)Θ_cG_c) + Re tr(aΘ_c(G_c − 1)), Z[a] := V^{−1}∂_vV[a] (only l ≤ k − 2; at l = k − 1 the
  level-k component is data, not part of Y).
  (Derivation: SG's δσ_c = κ[−Re tr(ΘW_0^{−1}δM) + Re tr(ZΘG)]; split W_0^{−1}δM = Qδx_l + A[δx_l], Z = δv + (Z − δv),
  G = 1 + (G − 1); the two leading pieces give −Re tr(Θ·(R_cδx)) = ⟨Ψ_c, R_cδx⟩.) H_{D_c} = κ_lR_c^TR_c (φ̂ = −Re tr(ρG) −
  ½Re tr(ρ²G) − …, Re tr(ρG) ≡ 0, G = 1 + O(x²), ρ^{(1)} = R_cx at B = 0). Slots: **residual slot s_c := κ_l(r^hom_l(x)(c) −
  Ψ_c)** at c, **plain slot −κ_lE_c**.

### 3.3 Holomorphic continuation (Lemma HC) and dimension-free Cauchy (Lemma CE′)
For a density D let 𝔻_D(ϱ) := {every variable y_b of supp D (own units, B_c included for top densities) has |y_b| ≤ ϱ}.
**Lemma HC — PROVEN-HERE as a restatement of banked inputs.** There are ϱ_A ∈ (0, 1/(40p_L)] and S_A < ∞ depending only on
(N, L) such that for every k, every T ≥ 3, every l and every density D, each of X_0(c), ρ_c, Θ_c, Θ′_c := e^{−ρ_c} − 1, Ψ_c,
G_c, G′_c, A_b, A′_b, Z − id, s_c, E_c(·), F_p, q_p, g_3(F_p), K_{p,b}, G_0(p), j_p(b) is the restriction to real points of a
holomorphic function on 𝔻_D(ϱ_A), bounded there by S_A (operator-valued ones in operator norm on (𝔤_ℂ, |·|)). On 𝔻_D(ϱ_A) the
continuations satisfy SG, Re tr(ρ_cG_c) ≡ 0, tr ρ_c ≡ 0 and the slot formulas of §3.2, with Re tr Y read as ½(tr Y + tr Y^♮),
Y^♮ the continuation of Y^*: x_b^♮ = −x_b, W_0^♮ = W_0^{−1}, M^♮ = M̃ (the S4′ average of the reversed words in e^{∓x}),
Θ^♮ = Θ′, G^♮ = G′ := M̃W_0, Z[a]^♮ = −Z[a], A_b[a]^♮ = A′_b[a] := ∂_bM̃[a]·W_0 + Q_{cb}a.
*Proof.* (a) *Finitely many types.* Up to lattice translations and axis permutations a soft density has one word set (24L⁴
words, length ≤ p_L) on the links of Box(c) (§3.4), and **no two of them are identified on the torus**: Box(c) has 2L sites in
direction μ and L in the others (rl55_1 P2), the level-l torus has side TL^{k−l} ≥ 3L. A Wilson density has one type.
(b) M̄_c is a polynomial in the entries of e^{±x}. The stationarity equation Π(e^{−X}M) = 0 continues to
P(X, M) := ½(e^{−X}M − M̃e^X) − (1/(2N))tr(e^{−X}M − M̃e^X) = 0, holomorphic, with D_XP(0, 1) = −id on 𝔤_ℂ (tr δX = 0); the
holomorphic implicit-function theorem gives X_0 near M = 1, equal on real points to NA-alg's maximiser by its uniqueness in
{|X| ≤ 3y} (PROOF "Contraction on B := {|X| ≤ 3y}", "It is the global maximiser"). exp, log and BCH near 1, sinh, cosh are
holomorphic. (c) Take ϱ_A half the least radius and S_A the largest bound over the finitely many types. (d) Each identity has
holomorphic sides on the connected 𝔻_D(ϱ_A) that agree on its real points (a maximal totally real subspace), hence everywhere. ∎
This is Codex KOFF §4.3's argument and HIGHER55's Lemma AN (banked, Codex HIGHER item 1), with the HS-polydisc and the explicit
T ≥ 3 no-identification fact (Codex HIGHER's coordinate-repetition argument for T_{l+1} = 1 is not needed in Setting (K)).
**Lemma CE′ (Cauchy without dimension).** If f is holomorphic on 𝔻_D(ϱ_A), |f| ≤ S, and its Taylor series at 0 starts at
degree p, then |f(y)| ≤ 2S(s/ϱ_A)^p for s := max_b|y_b| ≤ ϱ_A/2; the degree-≥q tail obeys the same with q in place of p.
*Proof.* ζ ↦ f(ζy/s) is holomorphic on |ζ| ≤ ϱ_A (every variable of ζy/s has modulus ≤ |ζ|); its n-th Taylor coefficient is
the degree-n part P_n(y/s), so |P_n(y)| ≤ S(s/ϱ_A)^n (Cauchy, any norm on the target); sum over n ≥ p. ∎ **No factor depends on
the number of variables of D** (HIGHER55's CE-1 without its √(N²−1), which the HS-polydisc absorbs).

### 3.4 The boundary convention: patches, local seminorms, local constraint sets
**Local quantities** of a configuration (unweighted; each has a base point): V_j(b) := |x^c_j(b)| = L^{k−j}|x_j(b)|;
Gr_j(b, λ) := L^{2(k−j)}|x_j(b + e_λ) − x_j(b)| (= |∇^c_λx^c_j(b)|, b and b + e_λ parallel level-j links);
Ca_j(Bx, ν, λ) := ρ_{Bx}^{−α}Osc_2(∇^c_λx^c_{j,ν}; Bx) (Bx a lattice box of coarse side ρ_{Bx} ∈ [L^{−(k−j)}, 1]);
Re_j(c) := L^{(1+σ)(k−1−j)}|r^{c,hom}_j(c)| = L^{(2+σ)(k−1−j)}|r^hom_j(x)(c)|; and |B_c|.
**Each is ≤ ||x||_{(σ),hom}** (resp. ≤ ||B||_D): the norm is a max over j of sums of sups of exactly these.
- **(S) soft c = (X, μ):** Box(c) := {z : |z_ν − (c_X)_ν| ≤ o (ν ≠ μ), −o ≤ z_μ − (c_X)_μ ≤ o + L} (level-l sites).
  **Lemma SUPP below: supp D_c = N_c ∪ {c} with N_c = all level-l links with both endpoints in Box(c).** Patch := supp D_c.
  **ν_c(x) := max{V_l(b) : b ∈ N_c} ∨ max{Gr_l(b, λ) : b, b + e_λ ∈ N_c} ∨ V_{l+1}(c) [l ≤ k − 2] ∨ Re_l(c)**;
  𝒦_c(r) := {x|_{supp D_c} : ν_c(x) ≤ r} for l ≤ k − 2, and {(x|_{N_c}, B_c) : ν_c(x) ≤ r, |B_c| ≤ r} for l = k − 1.
- **(W) Wilson p:** ν_p(x) := max{V_0(b) : b ∈ ∂p} ∨ (the two gradient quantities of the two parallel pairs in ∂p);
  patch := ∂p = supp D_p; 𝒦_p(r) := {x|_{∂p} : ν_p(x) ≤ r}.
- **(P) Wilson pair (p, v),** v ∈ ℤ⁴ ∖ 0, |v|_∞ ≤ n: Rect(p, v) := the least lattice rectangle containing the vertices of p
  and of p + v; 𝔅(p, v) := the lattice boxes of coarse side in [1/n, 1] that contain the base point of a link of ∂p or of ∂p + v.
  **ν_{p,v}(x) := max{V_0(b), Gr_0(b, λ) : b (and b + e_λ) with both endpoints in Rect(p, v)} ∨ max{Ca_0(Bx, ν, λ) : Bx ∈
  𝔅(p, v)}**; its patch Ω_{p,v} := the links read by these quantities — a **fixed enlarged patch**, inside the coarse ℓ^∞-ball
  of radius 2 + 1/n about p; 𝒦_{p,v}(r) := {x|_{Ω_{p,v}} : ν_{p,v}(x) ≤ r}.
**Lemma RS (restriction) — PROVEN-HERE (immediate).** For all complex x, B and every D: ν_D(x) ≤ ||x||_{(σ),hom},
|B_c| ≤ ||B||_D; for a direction u, ν_D(u) ≤ max{input local quantities of u based in the patch of D}. Each ν_D is a seminorm on
the patch variables (Osc_2 is the L²(Bx)-norm of the mean-free part), a norm on supp D for (S) and (W) (it contains every value);
𝒦_D(r) is the r-ball of max(ν_D, |B_c|): 𝒦_D(r_1) + 𝒦_D(r_2) ⊂ 𝒦_D(r_1 + r_2) and t𝒦_D(r) = 𝒦_D(|t|r), t ∈ ℂ. ∎
**Lemma SUPP — PROVEN-HERE (every odd L ≥ 3; exact check rl55_2).** N_c equals Ω_c := {level-l links with both endpoints in
Box(c)}, and every monotone staircase of ν-links between two ν-links of N_c lies in N_c.
*Proof.* (⊂) Each leg of T^𝔬_y moves coordinates monotonically between c_X and y, between y and y + Le_μ, and between
c_Y = c_X + Le_μ and y + Le_μ, so every vertex lies in Box(c). (⊃) A μ-link based at z ∈ Box(c) with z + e_μ ∈ Box(c): take
y_ν = z_ν (ν ≠ μ) and y_μ ∈ [(c_X)_μ − o, (c_X)_μ + o] with y_μ ≤ z_μ ≤ y_μ + L − 1 (possible because
z_μ − (c_X)_μ ∈ [−o, o + L − 1]); the straight leg of T^𝔬_y contains it. A ν-link, ν ≠ μ, based at z with z, z + e_ν ∈ Box(c):
take an order 𝔬 with ν last and y_λ = z_λ (λ ≠ ν, μ), y_ν − (c_X)_ν = +o if z_ν ≥ (c_X)_ν and −o otherwise; if
z_μ − (c_X)_μ ≤ o put y_μ := z_μ, and the last (ν-)segment of the go-leg runs through z → z + e_ν; if z_μ − (c_X)_μ ≥ o + 1 put
y_μ := z_μ − L (then y_μ − (c_X)_μ ∈ [−o, o]), and the ν-segment of the return leg (at coordinates (y + Le_μ)_λ) contains it.
Staircases: Box(c) is a rectangle, so the rectangle spanned by two ν-links with both endpoints in Box(c) has the same property. ∎
rl55_2 (exact, d = 4): |N_c| = |Ω_c| = 459 (L = 3) and 4125 (L = 5) for all four μ, Q2 staircases inside N_c; control
(y = c_X only) gives 3, resp. 5 links. **These counts coincide with Codex HIGHER §1's independent enumeration ("459 distinct
cover links at L=3 … At L=5 … 4125").** *Consequence:* for soft and single-Wilson densities the "restricted seminorm"
convention needs **no extension theorem and no enlargement** — every constraint in ν_c reads only variables of supp D_c (the
gradient pairs and the oscillation staircases lie in N_c; the residual r_l(c) reads N_c and c). Only the Wilson **pairs** need
the fixed enlarged patch (P). **What the printed 𝒦_D of BFT4W55 §3.4 gets wrong:** it is described as a set of
"(x|_{supp D}, B|_{supp D})" constrained by "Campanato boxes meeting supp D" and "residuals at the coarse links of supp D" —
quantities that read variables outside supp D (a box meeting supp D in one site; the level-(l−1) residuals of the links of N_c).
As written it is not a subset of the supp-D variables (Codex W1's objection, confirmed). (S)/(W)/(P) above replace it; no
lower-level residual and no Campanato quantity is needed for any soft bound.
**Lemma LBC (BL-C is pair-local) — PROVEN-HERE (reading BFT_A §8.4's proof).** For a level-0 form H (one component, 𝔤_ℂ-valued)
and base points z, z′ with t := |z − z′|_∞ ∈ (0, 1] (coarse):
  |H(z) − H(z′)| ≤ [C_C·max{ρ_{Bx}^{−α}Osc_2(H; Bx) : Bx ∋ z or Bx ∋ z′, side ≤ 1} + 2·8^α max(|H(z)|, |H(z′)|)]·t^α,
C_C := 2^α(8·2^α/(2^α − 1) + 32·4^α). *Proof.* For t ≤ 1/8 the proof of BFT_A §8.4 uses only the dyadic boxes D_i(z) ∋ z,
D_i(z′) ∋ z′ (sides ≤ 2^Iε < 2t ≤ ¼) and one box B* ⊃ D_I(z) ∪ D_I(z′) of side 2^{I+2}ε ≤ 1; for t > 1/8 it uses only
|H(z)|, |H(z′)|. The step |m_D − m_B| ≤ (|B|/|D|)^{1/2}Osc_2(H; B) is Cauchy–Schwarz and holds for 𝔤_ℂ-valued H. ∎

---

*(Timestamp correction, written now: the headings of §2 ("04:50Z") and §3 ("04:58Z") were estimates typed ahead of the clock.
`date -u` printed 04:42:40Z before §1 was appended and 04:48:34Z before this line, so §2 and §3 were appended between those two
times. No other content depends on these times.)*

## 4. Theorem LOC — premise (R) in local form, with proof (appended after 2026-10-29T04:48:34Z)

> **Theorem LOC.** In Setting (K) there are r_L ∈ (0, ϱ_A/4] and C_L < ∞, depending only on (N, L, κ_+, α) (d = 4) — **not on
> k, T, l, the density, the pair, σ or v** — such that for every 0 < r ≤ r_L all functions below are holomorphic on the stated
> complex local sets and obey there (m := k − 1 − l, h := L^{−(m+1)}):
> - **(L0) local sizes.** On 𝒦_c(r): own |x_l(b)| ≤ hr (b ∈ N_c); |v| ≤ Lhr; for each ν and ν-links b, b′ ∈ N_c,
>   |x_l(b) − x_l(b′)| ≤ (5L − 5)h²r; |r^hom_l(x)(c)| ≤ L^{−(2+σ)m}r; contour logs ≤ 4p_Lhr; |ρ_c| ≤ 3r ≤ 1.
> - **(L1) nonlinear residual.** On 𝒦_c(r): **|ρ_c − r_l(x)(c)| ≤ C_Lh³r²** (r_l data-inclusive at l = k − 1). Hence the
>   residual slot obeys **L^{(2+σ)m}|s_c| ≤ C_L r²** for l ≤ k − 2 (the leading term carries L^{(σ−1)m} ≤ 1), and at the top
>   **|s_c − κ_{k−1}B_c| ≤ C_Lr²**, so |s_c| ≤ κ_+r + C_Lr².
> - **(L2) plain soft slot.** On 𝒦_c(r): **L^{3(k−l)}|E_c(b)| ≤ C_LL^{−σm}r²** (b ∈ N_c) and, for l ≤ k − 2,
>   **L^{3(k−l−1)}|E_c(c)| ≤ C_LL^{−σm}r²** (π-normalisation at the output's own level).
> - **(L3) Wilson.** On 𝒦_p(r): **n²|G_0(p)| ≤ C_Lr²**, **n³|j_p(b)| ≤ C_Lr²** (b ∈ ∂p).
> - **(L4) Wilson pairs.** On 𝒦_{p,v}(r), with t := |v|_∞/n ∈ [1/n, 1] and b ∈ ∂p:
>   **n²|G_0(p) − G_0(p + v)| ≤ C_Lr²t^α**, **n³|j_p(b) − j_{p+v}(b + v)| ≤ C_Lr²t^α**.
> - **(L5) slotwise linear cancellation.** Every slot of every Y_D, and every pair difference in (L4), has zero x-derivative
>   at (x, B) = (0, 0) (§5).
> - **(L6) energy densities (Lemma E2^σ's complex local input).** On 𝒦_c(r): |D_c| ≤ κ_+C_Φ|ρ_c|² with |ρ_c| ≤ |r_l(x)(c)| +
>   C_Lh³r² (l ≤ k − 2), and at the top |D_c(x; B) − D_c(0; B)| ≤ C_L(ν_c(x) + |B_c|)ν_c(x); on 𝒦_p(r): |D_p| ≤ C_Ln^{−4}r².
>
> Here "holomorphic on 𝒦_D(r)" means: the restriction of the holomorphic function of Lemma HC, since 𝒦_D(r) ⊂ 𝔻_D(ϱ_A/4).
> **Status: PROVEN-HERE as an implication of** Lemma HC (= banked Codex KOFF §4.3 / Codex HIGHER item 1), BA-4's constant-field
> identity (banked; Codex HIGHER item 1 "the paired S4′ centering cancellation"), BA-5's quadratic polar statement (banked; Codex
> HIGHER §2 "X₂ = Π(M₂ − M₁²/2) … X₂=avg B₂"), SG (banked), Lemma SUPP and Lemma LBC (§3.4), and NA-alg (a)-(b) as cited by them.

*Proof.* Fix r ≤ r_L, where r_L ≤ ϱ_A/4 is chosen at the end. Constants C_1, C_2, … depend only on (N, L, κ_+, α).

**(L0).** V_l(b) ≤ r gives own |x_l(b)| = L^{−(k−l)}V_l(b) ≤ hr; V_{l+1}(c) ≤ r gives |x_{l+1}(c)| = L^{−(k−l−1)}V_{l+1}(c) ≤ Lhr;
at the top |B_c| ≤ r = Lhr (h = 1/L). For ν-links b, b′ ∈ N_c the monotone staircase of ν-links between them lies in N_c (Lemma
SUPP) and has |b − b′|_1 ≤ 5L − 5 steps (the ν-link base points of Box(c) span (2L − 2) + 3(L − 1) in ℓ¹ for ν = μ and
(L − 2) + (2L − 1) + 2(L − 1) for ν ≠ μ; rl55_1 P3 found exactly 5L − 5 = 10, 20 at L = 3, 5); each step changes x_l by
h²·Gr_l ≤ h²r. Re_l(c) ≤ r gives |r^hom_l(x)(c)| ≤ L^{−(2+σ)m}r. A word has ≤ p_L letters of HS size ≤ hr; for complex letters
with Σ|z_a| ≤ ½, |Πe^{z_a} − 1| ≤ e^{Σ|z_a|} − 1 ≤ 2Σ|z_a| and |log(1 + Y)| ≤ 2|Y| for |Y| ≤ ½ (HS is submultiplicative), so
contour logs are ≤ 4p_Lhr. The bound on |ρ_c| follows from (L1) below once r_L(1 + C_ρ) ≤ 1.

**(L1).** By Lemma HC, ρ_c is holomorphic in the variables y = (x_l|_{N_c}, v) on 𝔻_c(ϱ_A), and s := max own|y| ≤ Lhr ≤ r
(Lh ≤ 1). Taylor at 0 (all degrees in y jointly): ρ_c = P_1 + P_2 + P_{≥3}.
- P_1 = (Q_lx_l)(c) − v = r_l(x)(c) (data-inclusive at the top): the first-order stationarity equation gives X_0^{(1)} = Π(M^{(1)})
  = M^{(1)} = (Q_lx_l)(c) (M^{(1)} is the average of the letter sums, in 𝔤_ℂ), and BCH^{(1)}(−v, X_0) = X_0^{(1)} − v.
- P_2 = avg_{𝔬,y}B_2(T^𝔬_y) − ½[v, (Q_lx_l)(c)], B_2(z_1…z_p) := ½Σ_{a<a′}[z_a, z_{a′}]: X_0^{(2)} = avg B_2 (Codex HIGHER §2's
  derivation — M₂ = avg(B₂ + Y₁²/2) and the Hermitian squares are killed by Π — re-derived: at second order the continued
  stationarity equation reads −X_0^{(2)} + M^{(2)} − M^{(1)}X_0^{(1)} + (X_0^{(1)})²/2 projected to 𝔤_ℂ = 0, i.e.
  X_0^{(2)} = Π(M^{(2)} − (M^{(1)})²/2) = Π(avg(B_2 + Y_1²/2) − (avg Y_1)²/2) = avg B_2, because Y_1² and (avg Y_1)² are
  Hermitian on real points and avg B_2 ∈ 𝔤), and BCH^{(2)}(−v, X_0) = X_0^{(2)} − ½[v, X_0^{(1)}].
  *Bound on P_2.* Fix one reference ν-link b_ν^* ∈ N_c per direction ν and write each letter z_a = z̄_a + δ_a with
  z̄_a := ±x_l(b_ν^*) (ν the letter's direction, sign of traversal); |δ_a| ≤ δ := (5L − 5)h²r by (L0), |z̄_a| ≤ hr. BA-4: avg B_2(z̄) = 0
  for direction-constant letters (an identity per c; d = 4 exact check hg55_1 A1, reproduced by Codex HIGHER §7; general proof
  Codex HIGHER §2: B_2 = L[D, A_μ] per word, avg_y D = 0). Per word, ½Σ_{a<a′}|[z_a, z_{a′}] − [z̄_a, z̄_{a′}]| ≤
  ½p_L(p_L − 1)δ(2hr + δ) (|[A, B]| ≤ 2|A||B| in HS). Hence |avg B_2| ≤ ½p_L²(5L)(2 + 5)h³r² = (35/2)Lp_L²h³r² (using
  (5L − 5)h ≤ 5). And [v, Q_lx_l] = [v, r_l(x)(c) + v] = [v, r_l(x)(c)], so ½|[v, Q_lx_l]| ≤ |v||r_l(c)| ≤ Lhr·L^{−(2+σ)m}r ≤
  L³h³r² for l ≤ k − 2 (L^{−(2+σ)m} ≤ L^{−2m} = L²h²) and ≤ r·2r = 2L³h³r² at the top (h = 1/L, |r^data| ≤ 2r).
- P_{≥3}: Lemma CE′ with q = 3 gives |P_{≥3}| ≤ 2S_A(s/ϱ_A)³ ≤ 2S_AL³ϱ_A^{−3}h³r³ ≤ 2S_AL³ϱ_A^{−3}h³r² (r ≤ 1).
So **|ρ_c − r_l(x)(c)| ≤ C_ρh³r², C_ρ := (35/2)Lp_L² + 2L³ + 2S_AL³ϱ_A^{−3}.**
Residual slot. tr ρ_c ≡ 0 (Lemma HC), so Ψ_c − ρ_c = (sinh ρ − ρ) − (1/N)tr(sinh ρ − ρ)·1 and |Ψ_c − ρ_c| ≤ 2|sinh ρ − ρ| ≤
2(sinh|ρ| − |ρ|) ≤ ½|ρ_c|³ for |ρ_c| ≤ 1 (|tr A·1|/N ≤ |A|; sinh t − t ≤ t³cosh(1)/6 ≤ t³/4). For l ≤ k − 2,
|ρ_c| ≤ L^{−(2+σ)m}r + C_ρh³r², and with (a + b)³ ≤ 4(a³ + b³):
  L^{(2+σ)m}|s_c| = κ_lL^{(2+σ)m}|r_l(c) − Ψ_c| ≤ κ_+[C_ρL^{−3}L^{(σ−1)m}r² + 2L^{−2(2+σ)m}r³ + 2C_ρ³L^{(2+σ)m}h⁹r⁶]
  ≤ κ_+(C_ρL^{−3} + 2 + 2C_ρ³)r²   (L^{(2+σ)m}h³ = L^{−3}L^{(σ−1)m} ≤ L^{−3}, L^{(2+σ)m}h⁹ ≤ L^{−9}, r ≤ 1).
At the top: r^hom(c) − Ψ_c = B_c + (r^data(c) − ρ_c) + (ρ_c − Ψ_c), and |ρ_c| ≤ |r^hom| + |B_c| + C_ρh³r² ≤ 3r (r ≤ 1/C_ρ),
so |s_c − κ_{k−1}B_c| ≤ κ_+(C_ρL^{−3} + 27/2)r².

**(L2).** By Lemma HC, ⟨E_c(b), a⟩ = −½[tr(Θ_cA_b[a]) + tr(A′_b[a]Θ′_c)] on 𝔻_c(ϱ_A), complex-linear in a. A_b and A′_b are
holomorphic in x_l|_{N_c} and vanish at 0 (at x = 0: W_0 = 1, ∂_bM[a] = Q_{cb}a, ∂_bM̃[a] = −Q_{cb}a), so by Lemma CE′ (p = 1,
applied to a ↦ A_b[a] with |a| ≤ 1) ||A_b||, ||A′_b|| ≤ 2S_Aϱ_A^{−1}s_l, s_l := max_{N_c}own|x_l| ≤ hr. And |Θ_c|, |Θ′_c| ≤
e^{|ρ|} − 1 ≤ 2|ρ_c|. With the dual norm of ⟨·,·⟩ (§1): **|E_c(b)| ≤ 4S_Aϱ_A^{−1}hr|ρ_c|** — the SG product structure: the
plain slot is (a coefficient of size s_l) × Θ_c, at every order. For l ≤ k − 2:
  L^{3(k−l)}|E_c(b)| = h^{−3}|E_c(b)| ≤ 4S_Aϱ_A^{−1}(h^{−2}L^{−(2+σ)m}r² + C_ρhr³) = 4S_Aϱ_A^{−1}(L²L^{−σm}r² + C_ρL^{−(m+1)}r³)
  ≤ 4S_Aϱ_A^{−1}(L² + C_ρ)L^{−σm}r²   (L^{−(m+1)} ≤ L^{−σm}, σ ≤ 1);
at the top (m = 0, |ρ_c| ≤ 3r): L³|E_c(b)| ≤ 12S_Aϱ_A^{−1}L²r². Level-(l + 1) component (l ≤ k − 2):
⟨E_c(c), a⟩ = ½[tr((Z[a] − a)Θ_cG_c) − tr(G′_cΘ′_c(Z[a] − a))] + ½[tr(aΘ_c(G_c − 1)) − tr((G′_c − 1)Θ′_ca)]. Z[a] =
∫_0^1e^{−sv}ae^{sv}ds gives |Z[a] − a| ≤ (e^{2|v|} − 1)|a| ≤ 4|v||a|; ||G_c||, ||G′_c|| ≤ 2; G_c − 1 and G′_c − 1 start at degree 2
(G^{(1)} = M^{(1)} − X_0^{(1)} = 0, G′^{(1)} = M̃^{(1)} + X_0^{(1)} = −Q_lx_l + Q_lx_l = 0), so ||G_c − 1||, ||G′_c − 1|| ≤
2S_Aϱ_A^{−2}s_l². Hence |E_c(c)| ≤ (16|v| + 4S_Aϱ_A^{−2}s_l²)|ρ_c| ≤ (16Lhr + 4S_Aϱ_A^{−2}h²r²)(L^{−(2+σ)m}r + C_ρh³r²), and with
L^{3(k−l−1)} = L^{−3}h^{−3} the leading term is 16L^{−2}h^{−2}L^{−(2+σ)m}r² = 16L^{−σm}r²; the other three terms are smaller by
at least a factor L^{−1}(1 + C_ρ + 4S_Aϱ_A^{−2}) r. So L^{3(k−l−1)}|E_c(c)| ≤ (16 + 4S_Aϱ_A^{−2}(1 + C_ρ) + 16C_ρ)L^{−σm}r².

**(L3).** On 𝒦_p(r): own |x_0(b)| ≤ n^{−1}r; (dx_0)_p is a signed sum of the two parallel differences in ∂p, so |(dx_0)_p| ≤
2n^{−2}r; q_p starts at degree 2 in the four link variables, so |q_p| ≤ 2S_Aϱ_A^{−2}n^{−2}r² (CE′); |F_p| ≤ 3n^{−2}r once
r_L ≤ ϱ_A²/(2S_A). g_3(F) = (sinh F − F) − (1/N)tr(sinh F − F)·1, |g_3(F)| ≤ 2(sinh|F| − |F|) ≤ |F|³/2 for |F| ≤ 1. Hence
n²|G_0(p)| ≤ 2S_Aϱ_A^{−2}r² + (27/2)n^{−4}r³. K_{p,b} vanishes at 0 (q is quadratic), so ||K_{p,b}|| ≤ 2S_Aϱ_A^{−1}n^{−1}r, and
|∇𝒲(F_p)| ≤ |F_p| + |g_3(F_p)| ≤ 2|F_p| ≤ 6n^{−2}r; so n³|j_p(b)| ≤ 12S_Aϱ_A^{−1}r².

**(L4).** On 𝒦_{p,v}(r), t = |v|_∞/n ∈ [1/n, 1]. (i) For each link b of ∂p the staircase of translates of b from b to b + v lies
in Rect(p, v) and has |v|_1 ≤ 4|v|_∞ = 4tn steps, each changing x_0 by n^{−2}Gr_0 ≤ n^{−2}r; so with X, X′ ∈ 𝔤_ℂ⁴ the link values
of p and p + v: |X − X′|_∞ ≤ 4tn^{−1}r, |X|_∞, |X′|_∞ ≤ n^{−1}r. (ii) q is the same function for p and p + v; on the segment
[X, X′] its derivative obeys ||Dq(Y)|| ≤ C_1|Y|_∞ (Dq is holomorphic and vanishes at 0; Cauchy on 𝔻(ϱ_A/2), then CE′), so
|q(X) − q(X′)| ≤ 4C_1tn^{−2}r²; and |g_3(F)| + |g_3(F′)| ≤ 27n^{−6}r³ ≤ 27n^{−2}t^αr³ (t ≥ 1/n ⇒ n^{−4} ≤ t^α). Hence
**n²|G_0(p) − G_0(p + v)| ≤ (4C_1 + 27)r²t^α** (t ≤ t^α). (iii) Similarly K := K_{p,b} is translation-covariant:
n³|j_p(b) − j_{p+v}(b + v)| ≤ n³[||K(X) − K(X′)||·|∇𝒲(F)| + ||K(X′)||·|∇𝒲(F) − ∇𝒲(F′)|]. First: ||K(X) − K(X′)|| ≤
C_2|X − X′|_∞ ≤ 4C_2tn^{−1}r, times 6n^{−2}r: ≤ 24C_2tr². Second: ||K(X′)|| ≤ 2S_Aϱ_A^{−1}n^{−1}r and |∇𝒲(F) − ∇𝒲(F′)| ≤
2|F − F′| (|Dg_3(F)| ≤ 3|F|² ≤ 1), |F − F′| ≤ |(dx_0)_p − (dx_0)_{p+v}| + |q(X) − q(X′)|. The curl is (dx_0)_p =
n^{−2}[H_{λν}(z) − H_{νλ}(z)] with H_{λν} := ∇^c_λx^c_{0,ν} and z the base point of p, so by **Lemma LBC** at the pair (z, z + v)
— whose boxes contain z or z + v, base points of links of ∂p, ∂p + v, hence belong to 𝔅(p, v), and whose |H(z)|, |H(z + v)| are
gradient quantities in Rect(p, v) — |(dx_0)_p − (dx_0)_{p+v}| ≤ 2n^{−2}(C_C + 2·8^α)rt^α. So the second term is
≤ 4S_Aϱ_A^{−1}(2C_C + 4·8^α + 4C_1)r²t^α, and **n³|j_p(b) − j_{p+v}(b + v)| ≤ C_3r²t^α**.
Note what (iii) needs and (ii) does not: the Hölder seminorm (Campanato, via LBC) of the gradient enters only the plain Wilson
pair, at quadratic order; the divergence pair needs values and gradients only (the cubic part is beaten by t ≥ 1/n).

**(L6).** BFT4W55 §6.3's holomorphic form D_c = κ_lΦ(ρ_c, G_c, G′_c), |Φ| ≤ C_Φ|ρ|² on |ρ| ≤ 1, ||G||, ||G′|| ≤ 3 (Codex
BFT4W W7: confirmed), is per density; insert (L1). At the top, ρ_c(x; B) − ρ_c(0; B) = (Qx_{k−1})(c) + [(ρ − r)(x; B) −
(ρ − r)(0; B)]; the bracket is holomorphic, of degree ≥ 2 in (x, B) and vanishes at x = 0, so (h = 1/L is a constant at the top)
Cauchy in ζ ↦ (ρ − r)(ζx; B) gives |bracket| ≤ C(ν_c(x) + |B_c|)ν_c(x); G, G′ depend on x only with ||G − 1||, ||G′ − 1|| ≤
Cν_c(x)²; the difference bound follows from Φ's Lipschitz form (BFT4W55 §6.3). Wilson: |D_p| ≤ √N(cosh 1 − 1)|F_p|² ≤ 9√Nn^{−4}r².

**Choice of r_L.** r_L := min{ϱ_A/4, ϱ_A²/(2S_A), 1/(1 + C_ρ), 1/(8p_L)}. Then 𝒦_D(r) ⊂ 𝔻_D(ϱ_A/4) (all own variables ≤ Lhr ≤ r,
|B_c| ≤ r), the contour logs are ≤ 1/2 and within NA-alg's domain (p_L·own size ≤ 1/20 since ϱ_A ≤ 1/(40p_L)), |ρ_c| ≤ 3r ≤ 1
(also ||ρ||_op < 2π/N, so tr ρ = 0 on real points), and |F_p| ≤ 1. C_L := the largest constant displayed above (times κ_+ where
a soft slot carries κ_l). Every constant is built from S_A, ϱ_A (functions of N, L), p_L, L, κ_+, C_C(α), 8^α — none from k, T,
l, σ, the position of the density, or the number of variables of a patch. ∎

**Remarks.** (a) *Level factor.* The decay L^{−σm} of the plain slot comes from the SG product |E| ≲ s_l|ρ_c| and the **local**
residual constraint |r_l(c)| ≤ L^{−(2+σ)m}r; a plain Taylor bound of E would give only h^{−3}·h²r² = L^{m+1}r² and would not
even be bounded (this is BFT_A F6's "GAP 1", and the reason (R) must be proved from the factorised structure, not from
analyticity alone — consistent with Codex HIGHER §4: "SG does not say that the soft plain rows vanish when the linear residual r
vanishes … LA-2 prices that defect"; the additive defect is the C_ρhr³ term above). (b) *Directions.* The bounds are on
configurations; derivative bounds (§6) are in directions measured by ν_D, which contains the gradient, so no improved bound in an
arbitrary single-link direction is claimed (Codex HIGHER §2: "It is not an improved bound on its derivative in an arbitrary
individual-link direction"). (c) *Wilson exception.* (L3)-(L4) have no level factor (λ = 1); this is Codex HIGHER item 2's
"full Wilson exception explicitly retained", and it is why the Wilson plain row must be routed by the Hölder route (§7).

---

## 5. T3 — Lemma ZL: the linear term vanishes slotwise (appended after 2026-10-29T04:51:25Z)

> **Lemma ZL — PROVEN-HERE.** For the representation of §3.2, every slot Φ of every Y_D (and every Wilson pair difference)
> satisfies D_xΦ(0; 0) = 0 — slot by slot, not only after summing the covector.

*Proof.* Residual slot s_c = κ_l(r^hom_l(x)(c) − Ψ_c): Ψ_c = ρ_c + O(|ρ_c|³) and the degree-1 part of ρ_c in (x, B) is
r_l(x)(c) = R_cx − [l = k − 1]B_c (§4 (L1), P_1); so the x-linear part of s_c is κ_l(R_cx − R_cx) = 0 (its B-linear part at the
top, κ_{k−1}B_c, is the data vertex, not an x-derivative). Plain slots: E_c(b) is a bilinear expression in (Θ_c or Θ′_c) and
(A_b or A′_b) (§4 (L2)), each factor vanishing at (0, 0); E_c(c) is a sum of products (Z − id)·Θ and Θ·(G − 1) with each factor
vanishing at 0; so both are of degree ≥ 2. Wilson: G_0(p) = −q_p − g_3(F_p) has degree ≥ 2; j_p(b) = −K_{p,b}^T∇𝒲(F_p) is a
product of two functions vanishing at 0. Pair differences are differences of such slots. ∎
*Why this is needed and why it is not automatic* (Codex W1: "A covector identity by itself would not prove that a chosen redundant
slot representation has zero derivative"). Σ_D(linear parts of the slots of Y_D) = Hx − Hess F(0)x = 0 holds for every
representation; but a representation could carry a linear term +ℓ in one slot and −ℓ in another (e.g. a pure-gauge rewriting
of a plain current as a residual source), and then Lemma PW's Schwarz step would fail for those slots. The SG representation
has no such pair: each slot is built from factors that vanish at the trivial chain. Lemma ZL is used only at (x, B) = (0, 0),
which is where PW's Schwarz step evaluates it (B is scaled together with x).

---

## 6. T4 — Cauchy in d = 4, without dimension loss; multilinear weights (Corollary PW′ = Lemma PW with the patch convention)

> **Corollary PW′ — PROVEN-HERE (from Theorem LOC, Lemma ZL, Lemma RS).** Let Φ be one of the normalised slots — soft, l ≤ k−2:
> L^{(2+σ)m}s_c (λ := 1), L^{3(k−l)}E_c(b) and L^{3(k−l−1)}E_c(c) (λ := L^{−σm}); top: s_c, L³E_c(b) (λ := 1); Wilson:
> n²G_0(p), n³j_p(b) (λ := 1); pairs: n²(G_0(p) − G_0(p + v))/t^α, n³(j_p(b) − j_{p+v}(b + v))/t^α (λ := 1) — with its density or
> pair D, and put M_Φ := C_Lλ(r_L + r_L²). For (x, B) with ν_D(x) ≤ η, |B_c| ≤ η, η ≤ r_L/2, directions u (B-component 0) and
> b, b_j ∈ 𝔤_ℂ:
> - **(P1)** |D_xΦ(x; B)[u]| ≤ (4M_Φ/r_L²)·η·ν_D(u) ≤ 4C_Lλ(1 + 1/r_L)·η·ν_D(u);
> - **(P2)** (top densities) |∂_{B_c}Φ(x; B)[b]| ≤ (2M_Φ/r_L)|b| ≤ 2C_L(1 + r_L)|b|;
> - **(P3)** for ν_D(x), |B_c| ≤ r_L/4: |D^p_xD^w_BΦ(x; B)[u_1..u_p; b_1..b_w]| ≤ M_Φ(2(p + w)/r_L)^{p+w}Π_iν_D(u_i)Π_j|b_j|.

*Proof.* By Theorem LOC, |Φ| ≤ M_Φ on 𝒦_D(r_L) (the r_L term only for top residual slots). (P1): for ν_D(u) = 1 put
g(t, z) := Φ(tx + zu; tB), |t| ≤ r_L/(2η), |z| ≤ r_L/2; by Lemma RS the argument lies in 𝒦_D(r_L), so g is holomorphic and
|g| ≤ M_Φ. h(t) := ∂_zg(t, 0) = D_xΦ(tx; tB)[u] obeys |h| ≤ 2M_Φ/r_L (Cauchy in z) and **h(0) = 0 (Lemma ZL)**; Schwarz on
|t| ≤ r_L/(2η) gives |h(1)| ≤ (2η/r_L)(2M_Φ/r_L). If ν_D(u) = 0 then u = 0 on the variables Φ depends on (ν_D contains every
value of supp D, and for pairs every value in Rect(p, v)), so D_xΦ[u] = 0; otherwise scale. (P2): Cauchy in the one variable
ζ ↦ Φ(x; B + ζb/|b|) on |ζ| ≤ r_L/2. (P3): Cauchy in the p + w distinct complex parameters of
Φ(x + Σz_iu_i; B + Σζ_jb_j), each on radius r_L/(2(p + w)) (the argument stays in 𝒦_D(r_L/4 + r_L/2)); a mixed derivative of
order one in each of distinct variables costs (radius)^{−(p+w)} with no factorial; then multilinearity. ∎
This is BFT4W55 §3.4's (P1)-(P3) with BFT4W55 §10 E2's corrected chain, with 𝒦_D(η_*) replaced by the patch balls of §3.4 and
η_* by r_L. **No step counts variables:** the Cauchy and Schwarz estimates are in 1, 1 or p + w complex parameters, while a pair
patch carries ~(2L^k)⁴ links. The dimension d = 4 enters only through C_L (p_L = 5L − 4, the words, the incidence counts) and
is fixed. **The level factor survives every derivative** because Cauchy and Schwarz divide only by the fixed radius r_L of the
local set, whose bound M_Φ already carries λ — this is where the level decay of the sources passes to the vertices.
**Multilinear weights.** Theorem H3 (c) needs, for an output local quantity at z and inputs u_i measured in weights e^{μF_i}:
ν_D(u_i) ≤ e^{−μF_i(z_i)}||u_i||_{(σ),μ,F_i} at the input base point z_i where the max in ν_D is attained, with d_1(z, z_i) ≤ ρ_S
(§7); data slots y_j lie in supp D, d_1(z, y_j) ≤ 10. With **F_i 1-Lipschitz and F ≤ Σ_iF_i + Σ_jd_1(·, y_j)** (Codex BFT4W W2's
corrected rule; the same-weight sentence of BFT4W55's Lemma LD is refuted there and is **not** used):
e^{μF(z)} ≤ Π_ie^{μF_i(z)}Π_je^{μd_1(z,y_j)} ≤ e^{(p+w)ρ_Sμ}Π_ie^{μF_i(z_i)}, which is H3 (c)'s factor.

---

## 7. T5 — routing, per output link, and the cutoff Hölder control (Lemma RT)

> **Lemma RT — PROVEN-HERE (HR's proofs read per block; = BFT4W55 Lemma PWR, re-derived).** Let w = (w_0, …, w_{k−1}) be any
> complex plain current and split w_0 = w_0^W + w_0^S. For a level-i link b′ (0 ≤ i ≤ k − 1) in the level-(i+1) block Y′, let
> Λ(b′) := the links with at least one endpoint in Y′ (Λ_l: those of level l). Then, with π_l(w)(b) := L^{3(k−l)}|w(b)|,
> **π_i((P^TD^⊥w)_i)(b′) ≤ 2dM_γ[max_{Λ_0(b′)}π_0(w_0^S) + Σ_{l=1}^{i}max_{Λ_l(b′)}π_l(w_l)] + dM_γL^{−α(k−i)}·
> max{|w_0^{W,c}(b) − w_0^{W,c}(b + L^ie_μ)|/(L^{i−k})^α : b, b + L^ie_μ ∈ Λ_0(b′)}**,
> M_γ = L^{d−1}(L − 1)/2. The right side reads w only on Λ(b′), inside the level-k cell of b′ (plus one own step).

*Proof.* P^TD^⊥w = P^TDw (HR (i): P^Tu does not depend on root values) = Σ_lP^Tev^{(l)T}d*w_l, and level-l charges produce no
current below level l (HR (ii)). For l ≤ i, (P^Tev^{(l)T}d*w_l)_i(b′) = Σ_{Z∈Y′, b′∈γ(Z)}V^{(l)}_i(Z) (≤ M_γ terms), and
V^{(l)}_i(Z) = Σ_μΣ_{lines}[w_l(entry) − w_l(exit)] over the dL^{(d−1)(i−l)} level-l lines crossing the level-i block of Z ⊂ Y′
(HR (iii)'s exact telescope — an identity for that one block); entry and exit links have an endpoint in the block, so lie in
Λ_l(b′). Sup route: |V^{(l)}_i| ≤ 2dL^{(d−1)(i−l)}max_{Λ_l}own|w_l|, hence π_i ≤ M_γL^{(d−1)(k−i)}·2dL^{(d−1)(i−l)}·
L^{−(d−1)(k−l)}max_{Λ_l}π_l(w_l) = 2dM_γmax_{Λ_l}π_l(w_l) (d − 1 = 3: π_l = L^{3(k−l)}own). Hölder route (l = 0, the Wilson
part): entry and exit of a line are parallel level-0 links L^i own steps = L^{i−k} coarse apart; |w(exit) − w(entry)| =
n^{−(d−1)}|w^c(exit) − w^c(entry)| ≤ n^{−(d−1)}·(pair quotient)·L^{−α(k−i)}; with dL^{(d−1)i} lines, π_i ≤ M_γL^{(d−1)(k−i)}·
dL^{(d−1)i}n^{−(d−1)}(·)L^{−α(k−i)} = dM_γ(·)L^{−α(k−i)}. Sum over l ≤ i. ∎
**Per-density input to RT.** For w = the plain slots of a derivative of Y: π_l(w_l)(b) ≤ Σ over the densities with a plain
component at b — **at most 8 soft densities of level l** (rl55_1 P5: max n_c = 8 = max n_box for L = 3, 5) **+ 1 density of
level l − 1** (its level-l component sits at b = its own c) — each bounded by Corollary PW′ with λ = L^{−σ(k−1−l)} (resp.
L^{−σ(k−l)} for the level-(l−1) density); the Wilson pair quotient of w_0^W at (b, b + v) is a sum of **2(d − 1) = 6 pair terms**
(the plaquettes containing b, each paired with its translate by v, which are the plaquettes containing b + v), each bounded by
PW′ for pairs. So the routed output at b′ is bounded by (λ-weighted) per-density / per-pair quantities read in the cell of b′.
**Level sums (CB, localised).** Summing RT's bound over output levels i with the per-density factors gives exactly CB's sums:
Σ_iΣ_{l≤i}L^{−σ(k−1−l)} = Σ_l(k − l)L^{−σ(k−1−l)} ≤ (1 − L^{−σ})^{−2} and Σ_iL^{−α(k−i)} ≤ (L^α − 1)^{−1}, k- and T-uniform for
σ > 0 (σ = 1 included); the soft level-0 slots go by the sup route with factor kL^{−σ(k−1)} ≤ sup_k kL^{−σ(k−1)} < ∞; the
Wilson plain row, which has no level factor (Theorem LOC (L3)), must and does go by the Hölder route. Codex KOFF item 4 confirmed
these sums for the aggregate; here they are per output link.
**Cutoffs (Lemma F^σ's "level-0 Hölder quotient grows by at most 2d·sup").** For w ↦ η_Q·w (slotwise, η_Q evaluated at link
positions): π_l(η_Qw_l)(b) ≤ π_l(w_l)(b) (0 ≤ η_Q ≤ 1), and for a pair (b, b′′), t := |m_b − m_{b′′}|_∞ ≤ 1:
|η_Q(m_b)w^c(b) − η_Q(m_{b′′})w^c(b′′)| ≤ |w^c(b) − w^c(b′′)| + 2dt|w^c(b′′)|, since |∂_μη_Q| ≤ 2 (scale ½, BFT_B §10.2 W-cut), so
the pair quotient of η_Qw^W_0 is ≤ (that of w^W_0) + 2d·π_0(w^W_0)(b′′) (t^{1−α} ≤ 1). Per pair, local. The divergence and
residual slots are multiplied slotwise and stay in their classes (D^⊥ = 0 slotwise: d*d* = 0, r(Ξλ) = 0; Codex BFT34 R5).
**Read radius.** Output at b′ → slots on Λ(b′) (coarse ℓ^∞ ≤ 1 + 1/n of b′) → soft patches Box(c) (ℓ^∞ extent ≤ 2Lh ≤ 2) or pair
patches (ℓ^∞ ≤ 2 + 2/n about p): every input local quantity used is based within ℓ^∞ 4, i.e. **ℓ¹ ≤ 16 < ρ_S = 20**; direct
slots: soft < 5, Wilson pair ≤ 4(2 + 2/n) ≤ 11. So BFT4W55's ρ_S = 20 (Lemma FR (iii)) holds with these patches.

---

## 8. T6 — Assembly: (R) PROVEN as an implication; what becomes unconditional-on-(R) (appended after 2026-10-29T04:53:02Z)

> **Theorem R (the premise (R), in a precise form) — PROVEN as an implication.** In Setting (K): for every density D ∈ 𝒟 and
> every Wilson pair (p, v), with the boundary convention of §3.4 — **restricted seminorm on supp D itself** for soft and single
> Wilson densities (no enlargement and no extension theorem is needed: Lemma SUPP), and the **fixed enlarged patch** of coarse
> ℓ^∞-radius ≤ 2 + 2/n for Wilson pairs — every slot of Y_D (and every pair difference) is holomorphic on the complex local
> constraint ball 𝒦_D(r_L) and obeys the per-density size bound c_Dλ_Dr² (top residual slots: κ_+r + C_Lr²), with **λ_D =
> L^{−σ(k−1−l)} for plain soft slots in π-normalisation and λ_D = 1 for residual slots (normalisation L^{(2+σ)(k−1−l)}), Wilson
> slots and Wilson pairs (normalisation t^{−α})** (Theorem LOC (L1)-(L4)); the linear term vanishes slotwise (Lemma ZL); hence
> the per-density derivative and multilinear vertex bounds (P1)-(P3) hold with dimension-free Cauchy constants (Corollary PW′);
> the routing of the plain slots — including the **cut-off** Wilson plain current's Hölder control — holds per output link and
> reads only the output's cell (Lemma RT); and the energy densities obey (L6). r_L > 0 and C_L < ∞ depend only on (N, L, κ_+, α)
> (σ enters only through λ_D), **not on k or T**; they are existence constants built explicitly from the banked analytic
> constants (ϱ_A, S_A), which, like Codex KOFF §4.3's, are not computed.
>
> **Inputs, exactly:** (i) PROOF.md Lemma NA-alg (a)-(b) (uniqueness and stationarity of the maximiser on the small real
> domain; tr ρ = 0) — the input of the banked SG; (ii) Lemma SG — banked (Codex KOFF item 3, Codex HIGHER item 3); (iii) local
> analyticity with k-, T-, l-independent constants — banked (Codex KOFF §4.3, Codex HIGHER item 1 = HIGHER55 Lemma AN), as
> Lemma HC; (iv) BA-4's constant-field identity and BA-5's quadratic polar statement — banked (Codex HIGHER item 1, Lemma C2),
> re-derived in §4 (L1); (v) BL-C's proof (BFT_A §8.4) — re-verified here line by line (dyadic means, 16 = 2⁴, B* of side ≤ 1,
> C_C) and read as pair-local (Lemma LBC); (vi) HR (i)-(v) — banked (Codex KOFF item 1); (vii) |∂_μη_Q| ≤ 2 (BFT_B §10.2) — for
> the cutoff clause only; (viii) Codex BFT4W W2's corrected multilinear weight rule — for the weighted multilinear use only.
> **No inverse, no contraction, no lane-A linear input, no (GV), no (EP) is used.** New in this file: the patches and seminorms
> with Lemma SUPP (exact check rl55_2), Lemma RS, Lemma LBC, Theorem LOC (complex, local), Lemma ZL, Corollary PW′, Lemma RT.

*Proof.* §3.3-§7. ∎ (Codex W1's three requirements — "genuine local, holomorphic slot bounds with uniform coefficients and
summable level profiles", "its slotwise first derivative at zero must vanish", "an explicit boundary convention" — are Theorem
LOC with RT's profiles, Lemma ZL, and §3.4 respectively.)

**Re-derivation of Theorem H3 on these inputs (spot-level, for the reviewer).** D_xS̃(x; B)u = Σ_DD_xY_D[u] − P^TD^⊥(Σ_D plain
slots of D_xY_D[u]). Each output local quantity at z: (G_0 at p) one density, (P1) with λ = 1; (G_0 Hölder quotient at
(p, p + v)) one pair, (P1) for pairs; (residual slot at c) one density (D^⊥ of residual/divergence slots is 0 slotwise, so routing
adds none), (P1) λ = 1; (plain slot at a level-i link) ≤ 8 + 1 soft densities (+ 6 Wilson at i = 0), (P1) with their λ, plus
the routed term of Lemma RT, whose inputs are again (P1)-bounded per density/pair. Every input enters through ν_D(u) ≤ the largest
input local quantity of u based within ρ_S = 20 of z (§7, "Read radius"). Lemma LD (base-point weights, unchanged: only its
multilinear sentence is replaced by W2's rule) then gives (a) for every μ ≥ 0 and 1-Lipschitz f; (b) from (P2) (outputs within
coarse ℓ¹ 10 of y); (c) from (P3) and §6's weight rule; (d) from HR (i) (P_cc linear, (x, B)-independent). The level sums are
those of §7. So **Theorem H3 (a)-(d) holds with k-, T-, μ-, f-independent constants** (the explicit K_1 of BFT4W55 §3.6 is
not certified, see F11 below; a finite K_1 is).

**What becomes unconditional-on-(R)** (each item keeps every other premise it had; nothing here is banked until Codex checks
this file):

| Item | Was | Becomes |
|---|---|---|
| **Theorem H3 (a)-(d)** (BFT4W55 §3) = (H3)_μ, (H3)^Lip_μ incl. multiplicative locality | CONDITIONAL on (R) | **PROVEN as an implication of the banked local inputs (i)-(vi), (viii) only** — no linear-package, (GV) or (EP) dependence |
| **Lemma F^σ** (BFT4W55 §6.2) | CONDITIONAL on (R) (Codex W7: "still needs the per-density local analytic derivative estimates in W1, including the cutoff plain-current Hölder control") | **PROVEN as an implication** of the same + (vii) |
| **Lemma E2^σ / Corollary E3^σ** (BFT4W55 §6.3) | energy implication CONFIRMED, "Assuming the named complex local estimate" (Codex W7) | that estimate is LOC (L1)/(L6): **PROVEN as an implication of (i)-(iv)** |
| **BFT-3, route C** (BFT34_55 Theorem BFT3-glob) | conditional on (H1), (H2)_μ, (H3)_μ | **conditional on (H1), (H2)_μ only** |
| **BFT-3, route T** (Proposition TREE) | conditional on (H1), (H2)^Lip_μ, (H3)^Lip_μ | **conditional on (H1), (H2)^Lip_μ only** ((H2)^Lip_μ: Corollary H2W, itself conditional on zero-weight local-torus bounds — Codex W6) |
| **Nonlinear decoupling family** (Construction BBcc, Lemmas Dcc, UQ, IDcc) | conditional on F^σ + named linear/Ward/projection inputs | **conditional on the named linear/Ward/projection inputs only** (with Codex W5's restriction of Dcc's norm claim to the cc source space) |
| **Theorem BFT4a-glob** (BFT-4 (a) on 𝒞_glob) | CONDITIONAL, with the W1 (= (R)) and W8 obligations (Codex W9) | **CONDITIONAL on its other inputs only:** K^{(σ)} with the lane-A linear package and (GV) (table inputs 1-2), (EP) at zero weight (3), CD (4), H2W's zero-weight local-torus response/projection bounds and the Ward/CCP inputs (W5-W6); and it must carry **W8's corrected all-torus prefactor C_all and the small-torus margin ε ≤ ρ_E/C_0** |

**Not changed by this file:** BFT-4 (b) (gauge-invariant pieces), anything off 𝒞_glob, the per-level branch identification, the
numerical values of r_L, C_L (existence only), PROOF.md's 105-item tally (lane-level result).

---

## 9. Check record (criteria before scripts; exact integer/Fraction arithmetic; no floats)
- **rl55_1** — criteria `checks/rl55_1_criteria.md` (written 04:36Z, before the script); script `checks/rl55_1.py`; one run
  04:37:12-04:37:15Z with `python3 -I -B`, output `checks/rl55_1_out.txt`, stderr `checks/rl55_1_err.txt` (empty), exit 0.
  **OVERALL PASS**, d = 4, L = 3 (1944 words per μ) and L = 5 (15000 words per μ): P1 every word vertex in Box(c); P2 Box(c) is
  exactly the bounding box; P3 max ℓ¹ diameter of used ν-link base points = 10 (L = 3), 20 (L = 5), i.e. **5L − 5 ≤ 5L − 4**,
  rectangle hulls inside Box(c); P4 average signed ν-letter count = L·[ν = μ] exactly; P5 incidence **max n_c = max n_box = 8**,
  max Σ_c freq_c(b) = 83/81 (L = 3), 629/625 (L = 5). Controls: K1 (lower-corner y-range) FIRES, K2 (lowered +μ face) FIRES,
  K3 (threshold 5L − 6) FIRES. *Could it have failed?* Yes: K1/K2 show P1 fails for a wrong box or uncentred words; K3 shows the
  P3 value is attained, not vacuous.
- **rl55_2** — criteria `checks/rl55_2_criteria.md` (written after rl55_1 ran, before rl55_2.py); script `checks/rl55_2.py`; one
  run 04:42:19-04:42:20Z, `python3 -I -B`, output `checks/rl55_2_out.txt`, stderr empty, exit 0. **OVERALL PASS**: Q1
  N_c = Ω_c (459 links at L = 3, 4125 at L = 5, all μ), Q2 staircases inside N_c; control K1 (y = c_X only: 3, resp. 5 links)
  FIRES. The counts equal Codex HIGHER §1's independent enumeration.
- *What the checks cannot decide:* anything analytic (sizes, holomorphy, Cauchy), k- or T-uniformity, the Wilson pair patches.
  They decide the boundary convention of the soft patch and the counting constants. All analytic claims rest on §3-§7.

---

## 10. Findings, claim by claim (verdict; file + locating string; reason)

- **F1. ROW^{(σ)} (a) BCH₂ row as a per-density bound — CONFIRMED.** KFACTOR_OFF55 "2.2 Proposition ROW^{(σ)}"; BFT_A "3.6 BA-6"
  ("of own size ≤ κ·2p_Ls_l·|r_l|"), §12.0 ("⟨R^B_l, u_l⟩ := 2κ_l⟨r_l(x), B(x_l, u_l)⟩"). The bound is 2κ|r_l(c)|·|B_c(x_l, ·)|,
  read on supp D_c. (In H3's representation this row is part of the quadratic Taylor part of the plain slot −κE, covered by (L2).)
- **F2. ROW (a) residual part κρ^{(2)} per density — CONFIRMED,** with the explicit path convention: δ is bounded along staircases
  inside N_c (Lemma SUPP; rl55_2), length ≤ 5L − 5 (rl55_1 P3). BFT_A "3.4 BA-4" identity per c re-derived in (L1) (via Codex
  HIGHER §2's per-word formula); BA-6's "5L" is a valid upper bound for the exact 5L − 5.
- **F3. CR-1 per density — CONFIRMED** (BFT_A "13.5 Lemma CR-1": the cancellation ⟨r, [u_{l+1}, r]⟩ = 0 is at one link).
- **F4. Wilson q, plain row, and their Hölder bounds per plaquette / per pair — CONFIRMED** (BFT_A "28.6 Corollary WR", KFACTOR_OFF55
  ROW (a) "translate all factors together", Codex KOFF §4.3 Wilson). Requires the pair patch (Rect + 𝔅(p, v)); BL-C is pair-local
  (Lemma LBC). New precision: the divergence pair needs only values/gradients (cubic part beaten by t ≥ 1/n); only the plain pair
  needs the Campanato seminorm (L4).
- **F5. ROW (b) / SG / (LA-1′) / (LA-2) all orders, per density, complex — CONFIRMED** (Theorem LOC (L1)-(L2)); the level factor
  comes from the SG product |E| ≲ s_l|ρ_c| and the **local** residual constraint, not from analyticity (Remark (a) of §4).
- **F6. Codex KOFF §4.3 (1)-(3) as per-density complex bounds — CONFIRMED** ((L1), (L2), (L1)'s residual slot).
- **F7. CB per output link — CONFIRMED** (Lemma RT; KFACTOR_OFF55 "3.5 Proposition CB", HR "V_i(Z) = Σ_μΣ_{lines}…"): the routing
  telescope is an identity per block; no cross-block or cross-density cancellation is used.
- **F8. Cutoff plain-current Hölder control — CONFIRMED** (Lemma RT, "Cutoffs"; BFT4W55 §6.2's "2d·sup" with |∂η_Q| ≤ 2).
- **F9. Slotwise vanishing of the linear term — PROVEN-HERE** (Lemma ZL). Codex W1's caveat holds in general; the SG
  representation satisfies it.
- **F10. BFT4W55 §3.4's 𝒦_D as printed ("(x|_{supp D}, B|_{supp D}) all of whose input local quantities … Campanato boxes meeting
  supp D, residuals at the coarse links of supp D") — REFUTED as a definition:** a Campanato box meeting supp D in one site, a
  gradient in a direction leaving supp D, or the level-(l−1) residual of a link of N_c reads variables outside supp D, so the
  condition is not a condition on x|_{supp D}. **Correct statement:** §3.4 — ν_c reads only supp D_c (values, gradient pairs
  inside N_c, r_l(c)); ν_p reads ∂p; pairs use the fixed patch Ω_{p,v}. With it, Lemma PW's (P1)-(P3) hold (Corollary PW′). This
  confirms Codex W1's boundary objection; it does not falsify any bound.
- **F11. Theorem H3 (BFT4W55 §3.1/§3.6) as an implication — CONFIRMED**, now with (R) proven; its read radius ρ_S = 20 holds with
  these patches (≤ 16 needed; Lemma FR (i)-(iii) CONFIRMED, rl55_1). **The explicit K_1 formula — NOT-VERIFIED** as an expression:
  its Hölder-route Wilson term dM_γc_W/(L^α − 1) needs the 2(d − 1) = 6 pair terms per link (and the level-(l − 1) neighbour
  density's component appears nowhere explicitly) unless c_W, N_inc are read as per-link sums; the existence of a finite
  k-, T-, μ-, f-independent K_1 is CONFIRMED. No decision depends on its value (uncomputed constants).
- **F12. Lemma PWR (BFT4W55 §3.5) — CONFIRMED** (= Lemma RT, per link; "All suprema are over the cell of b′" holds up to one own
  step beyond the level-(i+1) block).
- **F13. Lemma F^σ and E2^σ's complex local input — CONFIRMED as implications** of Theorem R (§8 table).
- **F14. BFT4W55's assertion that (R) is "a reading of those proofs; I found no step that uses a non-local quantity" —
  CONFIRMED** for the proofs (T1, all LOCAL). As a reading of the banked **statements** it was not valid (Codex W1's logic); the
  three missing ingredients are now supplied.
- **F15. The brief's suggested route (decay of the weighted inverse + partition of unity) — not needed;** no bound in (R) contains
  an inverse. (No verdict: it was a suggestion, not a claim.)
- **F16. My own Theorem LOC / Lemmas HC, CE′, SUPP, RS, LBC, ZL / Corollary PW′ / Lemma RT / Theorem R — PROVEN-HERE**
  (constants existence-level, as in the banked inputs).

## 11. Codex verdicts used — agree or disagree, explicitly (files as on disk now; all complete)
- **CODEX_REVIEW_BFT4W W1 (NOT-VERIFIED; (R) an added premise): AGREE** for the evidence it had (it did not read the source
  proofs). Its counterexample to aggregate→local is valid logic and does not apply to the per-density proofs. Its three named
  requirements are exactly what §3.4, §4-§5 and §7 supply. **W2 (multilinear LD sentence REFUTED; corrected rule): AGREE**, and
  only the corrected rule is used (§6). **W7: AGREE** (E2/E3 power count fine; F^σ needed (R)). **Final item ("Single most
  dangerous unverified input: (R)"): AGREE it was;** this file proves it, pending a Codex check.
- **CODEX_REVIEW_KOFF §4.2-§4.3 (LA-1 REFUTED, LA-1′; local analytic completion CONFIRMED): AGREE**; every step there is per
  density, and its "Complexification gives the same assertion on a smaller complex polydisc" is what Lemma HC makes explicit.
  Items 1 (HR) and 4 (CB): AGREE (re-derived per link in Lemma RT).
- **CODEX_REVIEW_HIGHER items 1-3 (local analyticity incl. torus identification, Lemma C2, LA-2, NC3, FAC; SG's precise meaning;
  the Wilson exception): AGREE.** Its 459/4125 enumeration agrees with rl55_2; its remark that the improved bound on â is not an
  improved derivative bound in single-link directions is respected (§4 Remark (b)).
- **CODEX_REVIEW_BFT34 R5 (slotwise multiplication keeps the divergence/residual classes; 216 routing): AGREE** (used in §7).

## 12. Summary table

| # | Claim | File / locating string | Verdict |
|---|---|---|---|
| F1 | ROW (a) BCH₂ row per density | KFACTOR_OFF55 "2.2 Proposition ROW"; BFT_A "3.6 BA-6" | CONFIRMED (local) |
| F2 | ROW (a) κρ^{(2)} per density, path convention | BFT_A "3.4 BA-4", "3.6 BA-6" | CONFIRMED (local; δ path in N_c) |
| F3 | CR-1 per density | BFT_A "13.5 Lemma CR-1" | CONFIRMED |
| F4 | Wilson q / plain row, sizes and Hölder, per pair | BFT_A "28.6 Corollary WR"; KOFF §4.3 Wilson | CONFIRMED (pair patch; BL-C local) |
| F5 | ROW (b)/SG/LA-1′/LA-2 all orders, complex, per density | KFACTOR_OFF55 "2.1 Lemma SG"; this file (L1)-(L2) | CONFIRMED |
| F6 | Codex KOFF §4.3 (1)-(3) per density, complex | CODEX_REVIEW_KOFF §4.3 | CONFIRMED |
| F7 | CB per output link | KFACTOR_OFF55 "3.5 Proposition CB"; Lemma RT | CONFIRMED |
| F8 | cutoff plain-current Hölder control | BFT4W55 "6.2 Lemma F^σ" | CONFIRMED |
| F9 | slotwise zero linear term | Lemma ZL | PROVEN-HERE |
| F10 | BFT4W55's printed 𝒦_D | BFT4W55 §3.4 "Local constraint sets" | REFUTED as a definition; corrected (§3.4) |
| F11 | Theorem H3 (implication); explicit K_1 | BFT4W55 "3.6 Proof of Theorem H3" | CONFIRMED; K_1 expression NOT-VERIFIED |
| F12 | Lemma PWR | BFT4W55 "3.5 Lemma PWR" | CONFIRMED |
| F13 | F^σ; E2^σ's complex local input | BFT4W55 §6.2-§6.3 | CONFIRMED as implications |
| F14 | "(R) is a reading of the proofs" | BFT4W55 §3.4 "Reading step (R)" | CONFIRMED for the proofs |
| F16 | Theorem R (= (R)) and its lemmas | this file §3-§8 | PROVEN-HERE (implication of banked local inputs) |
| — | rl55_1, rl55_2 | checks/rl55_{1,2}_* | PASS, all controls fire (geometry only) |

Counts (verdicts on others' claims): **CONFIRMED 12** (F1-F8, F11 implication, F12, F13, F14), **NOT-VERIFIED 1** (F11's explicit
K_1 expression), **REFUTED 1** (F10, a definition, corrected). My own statements: PROVEN-HERE (F9, F16).

## 13. For the lead (short)
1. **(R) is PROVEN as an implication** of banked local inputs only (NA-alg, SG, local analyticity/AN, BA-4/BA-5 = Lemma C2, HR,
   BL-C's proof, |∂η_Q| ≤ 2, and W2's corrected weight rule) — Theorem R, §8. Every source proof was already local (§2); what was
   missing was the domain, the complexification and the slotwise linear cancellation, now written. **No inverse is used**; the
   suggested H2W/partition-of-unity route is unnecessary.
2. **Boundary convention:** soft and single-Wilson densities need **no** enlarged patch — supp D_c is exactly all links of Box(c)
   (Lemma SUPP, exact check rl55_2, counts matching Codex HIGHER's); only Wilson Hölder **pairs** need a fixed patch of coarse
   ℓ^∞-radius ≤ 2 + 2/n (Campanato boxes via a pair-local BL-C).
3. **Correction:** BFT4W55 §3.4's printed 𝒦_D is not a set of supp-D variables (F10, Codex W1's objection) — replace by §3.4 here.
4. **If Codex confirms:** Theorem H3, Lemma F^σ and E2^σ's input become PROVEN implications of banked local inputs; BFT-3 routes C
   and T keep only (H1) + (H2)_μ / (H2)^Lip_μ; Theorem BFT4a-glob keeps only its linear/slice/projection/Ward inputs plus W8's
   corrected prefactor. **HANDOFF's BFT-4 row should then read "(a) on 𝒞_glob: conditional on the named linear/slice inputs;
   (R) proven (RLOC55)"; PROOF.md's [S26-BANKED] BFT-4 (a) bullet should drop "given (R)". The 105-item tally does not move.**
5. **Most dangerous step for the reviewer:** (L2)'s level factor — it needs the SG product structure on the **complex** domain
   (the ♮-continuations Θ′, A′_b of §3.3) and the local residual constraint; a plain Taylor bound would lose L^{m+1}. Second:
   Lemma ZL (slotwise, not covector-level).

## 14. Errata after a full re-read (appended last; nothing above is edited)
- **E1 (§3.4 (P)).** "inside the coarse ℓ^∞-ball of radius 2 + 1/n about p" reads **2 + 2/n**: the Campanato quantities on a box
  of 𝔅(p, v) read the gradient, i.e. one more own step beyond the box. §7 and §8 already use 2 + 2/n; no bound changes (the read
  radius stays ≤ 16 < ρ_S = 20).
- **E2 (§4 (L1) and (L3), a constant).** "sinh t − t ≤ t³cosh(1)/6 ≤ t³/4" is false as written (cosh(1)/6 > 1/4). Correct: on the
  sets used, |ρ_c| ≤ 3r_L ≤ 3/(8p_L) ≤ 3/88 and |F_p| ≤ 3n^{−2}r_L, so t ≤ ½ and sinh t − t ≤ t³cosh(½)/6 ≤ t³/5; hence
  |Ψ_c − ρ_c| ≤ (2/5)|ρ_c|³ ≤ ½|ρ_c|³ and |g_3(F)| ≤ ½|F|³ hold as stated. No other statement changes.
- **E3 (§4, the Lipschitz/difference forms of Codex KOFF §4.3 (1)-(3)).** They follow per density from Corollary PW′ (P1)
  integrated along the segment (𝒦_D(η) is convex, Lemma RS): Φ(x) − Φ(x′) = ∫_0^1D_xΦ(x′ + t(x − x′))[x − x′]dt, so
  |Φ(x) − Φ(x′)| ≤ 4C_Lλ(1 + 1/r_L)·η·ν_D(x − x′) on 𝒦_D(η), η ≤ r_L/2 — the per-density form of "difference ≤ C h³ηδ" (for Φ =
  ρ_c − r_l(c) normalised by h^{−3}) and of the Lipschitz rows used by K^{(σ)}.
- **E4 (§6).** M_Φ := C_Lλ(r_L + r_L²) presumes C_L ≥ κ_+ (top residual slots carry κ_{k−1}B_c); take C_L := max(κ_+, …).
- **E5 (check record).** `checks/rl55_2_criteria.md` says "written 2026-10-29T04:4xZ" (a placeholder I left); its filesystem
  mtime is 04:41Z (00:41 local), before `rl55_2.py` (04:42Z) and its run (04:42:19Z). rl55_1: criteria 04:36Z, script 04:37Z, run
  04:37:12Z. Final append of this file: after 2026-10-29T04:56:08Z.
