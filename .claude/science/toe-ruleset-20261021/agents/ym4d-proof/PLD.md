# PLD: multi-defect Peierls large deviations for the soft RG, and returned clusters in the sea (lane E, session 1, 2026-10-27)

Status words as in PROOF.md: PROVEN-HERE (counted or not, said each time), ARGUED, OPEN, HYPOTHESIS, CONDITIONAL.
Imported items are never load-bearing for a PROVEN-HERE claim unless re-verified here. "given H" names every hypothesis
or earlier result a statement consumes.

Scope. Decision-4 soft RG (S4' contour averaging, normalised soft gauge-covariant kernel; PROOF L5 [S9]); levels, cubes
and action normalisation exactly as RLARGE.md §0 ((1/g_k²)Σ_p s(U_p), s(U) = 1 - N^{-1}Re tr U; EXISTENCE.md uses
(2N/g²)Σ(1 - N^{-1}Re tr U), i.e. the same measure with g² → 2Ng²; this file uses RLARGE's). Write access: this file,
PLD_LOG.md, checks/p*. Nothing in PROOF.md, RTARGET.md, LOG.md, RLARGE.md, FLOW.md, HIST.md or agents/ym4d-existence/ is
edited; proposed changes to them are listed in §12 for their owners.

Inputs read this session (read-only): RLARGE.md §0-§14 in full [read]; REVIEW_S16_S17.md l.280-410 and l.515-551 [read];
PROOF.md: Lemma W1-def, W1-size, W1-sym, W1-loc (2D, l.1433-1515), decision 4 and Lemma D4-norm (l.1533-1560), Lemma
W1-size', Lemma AG, hypothesis (DF), Corollary W1-LD-cond, (cl), W1-loc 4D status (l.1674-1757) [read]; PROOF.md entries
LF-count, R4D-iso, Theorem CE, inequality (B): [read-skim] through RLARGE §0-§7 and LINEAR_PACKAGE §5, which restate them
(their statements, not their proofs, are used; none is re-proved here); LINEAR_PACKAGE.md §1-§2, §6-§11 [read];
EXISTENCE.md §1 (l.77-96), X-LRP (l.279-288), §13 in full (l.1280-1620) [read]; REVIEW_X1_X2.md: grep only for
X-RP/CB/PLD [read-skim] (it reviews existence sessions 1-2; the session-4 items X-RP^S, Lemma CBE, Theorem CB, Lemma KN,
Corollary KN-step, Theorem CB-sg are not covered by it, i.e. unreviewed there).
**[RPLD-fix P-1] Provenance corrected (session 3).** The sentence above is wrong: REVIEW_X3_X4 (18:43 UTC, 2026-10-27)
reviewed these items: X-RP^S CONFIRMED-WITH-FIX (RX34-fix 1, the continuum-support class), Lemma KN CONFIRMED-WITH-FIX,
Lemma CBE, Theorem CB and Corollary KN-step CONFIRMED (as quoted in REVIEW_PLD_S1_S2 §2; REVIEW_X3_X4 itself not re-read
this session). Lemma CB-m's classes 𝔅_t lie in RX34-fix 1's corrected class (REVIEW_PLD_S1_S2, CB-m item). Every
"unreviewed" attached to these inputs below should be read with this correction.

---

## 0. Conventions fixed for this file
- **Chain and laws.** P_K := the joint law of (U_0, …, U_K) (U_0 ~ Wilson at g_0, U_{j+1} ~ K_j(·, U_j)), RLARGE §0 /
  EXISTENCE §13.1. Level k = after k steps (k = 0 bare). For level-k events only the marginal of (U_0, …, U_k) matters
  (the later kernels integrate to 1).
- **Tori.** Unless said otherwise the torus is the existence lane's: unit-lattice side ℓ = 4L^M (ES1), so the level-k torus
  has side n_k := 4L^{M+K-k} level-k sites and T_k = 4L^{M+K-k-1} level-k cubes per direction (both even). RLARGE admits
  every torus with side ≥ 3 blocks at level K; results below that use chessboard estimates are proven for this even family
  only (§12 item 1).
- **Bad, good, cut.** ζ_Q, χ_Q as RLARGE §0 (threshold ε_1, cube-interior plaquettes); G_k := ∩_Q{χ_Q = 1} (every
  level-k cube good). P_cut,k := P_K(· | G_k).
- **Disseminated quantities.** For a grid 𝒢 of congruent boxes (defined in §3), a box event f ∈ 𝔅_t and its reflected
  copies f^{[s]} (s ∈ 𝒢), Θ_ω(f) := ω(Π_{s∈𝒢}f^{[s]})^{1/|𝒢|}.
- Constants from earlier work used below: c_N (Haar ball: μ{||U - 1||_op ≤ δ} ≥ c_Nδ^{N²-1}, δ ≤ 1); A_d(L) = (d - 1)L(L - 1)/2
  (= 9 at d = 4, L = 3); c_1 := 1/(2(L² + 5.5A_d)) (= 1/117), from Corollary KN-step; η_1, ε_loc, a'', a_♯, n_♯ from RLARGE.

## 1. Targets (pre-stated 2026-10-27 23:00 UTC, before any derivation below and before the p1 criteria)

**T1 (PLD).** Prove, or reduce exactly to named statements, the multi-defect Peierls large-deviation bounds for the soft
RG at level k, in the two forms the consumers use:
- **(PLD-i)_k** [RLARGE §8.2 (PLD)_k (i)]: there are a_η > 0, C < ∞, independent of K, k, the torus and the coupling
  sequence (within (F), g_K ≤ g_0), such that for every finite set A of level-k plaquettes with pairwise disjoint
  1-neighbourhoods, P(||1 - U_k(p)||_op ≥ η_1 ∀p ∈ A) ≤ (C e^{-a_η/g_k²})^{|A|}.
- **(PLD-ii)_k** [RLARGE §8.2 (PLD)_k (ii)]: the same for the collar event {ε_♭(U; Q) > ε_loc} over any finite set 𝒜 of
  level-k cubes, with exponent a_♭.
- **(PLD-mod)_k** [EXISTENCE §13.6 (PLD^mod_dis)]: for every τ ∈ (0, ε_1] and every family A_p of reflected copies of a
  plaquette (one per super-block), the all-cut probability that all of A_p have ||1 - U_k(p')|| ≥ τ is
  ≤ (C_m e^{-a_mτ²/g_k²})^{|A_p|}, uniformly in K, k, the torus.
For each form: which measure (joint law P_K, all-cut law, per-history law of (I_k), fixed-V fluctuation law) the
statement is about, and whether the soft kernel's normalisation 𝒩 or the cut's normalisation costs a volume factor.
Routes: (a) chessboard reduction (Theorem CB of EXISTENCE §13.4, via X-RP^S) to all-blocks-bad events, priced by an
energy/entropy count (Wilson positivity, inequality (B), LF-count's arithmetic); (b) direct Peierls with the soft kernel's
positivity.
**Success:** (PLD-i), (PLD-ii), (PLD-mod) PROVEN-HERE with explicit a, C, uniform in k. **Partial success:** each form
reduced, by written proofs, to one named disseminated statement, with the cases that are proven (levels, models) and the
constants stated. **Valid failure outcomes:** (PLD-F1) the chessboard reduction does not apply to the measure a consumer
uses (named, with the reason); (PLD-F2) the energy/entropy count costs a factor that grows with the depth or the volume
(named and quantified); (PLD-F3) the soft kernel's normalisation 𝒩 costs a volume factor in route (b) (quantified).
**Not success:** a union bound presented as a product bound; any constant depending on K, k or the volume; a step that
uses (SF), (DF) or RLF itself without naming it.

**T2 (W1-ret').** After T1: state (W1-ret')_k (RLARGE §8.2) with all quantifiers in the form RLF-step consumes, and attack
the re-extraction after the sea average (REVIEW_S16_S17 R-6: "in a sea sample 𝔯 = O(g²)"). **Success:** the sea-averaged
returned activities written as c-number + one coupling shift + a remainder whose order is stated in terms of the
level-(k+1) field only, with every input named; (W1-ret') (c) (unreturned weights) reduced to (PLD). **Valid failure:**
the exact step that needs the small-field package named (which statement, which norm). **Not success:** "irrelevant"
asserted without saying in which norm.

**T3 (check p1; criteria file checks/p1_criteria.md before the script).** A numerical test of whichever T1 statement turns
out to carry a new uniform-in-depth constant, plus the elementary inequalities used.

---
# Derivations (written after §1)

## 2. Which measure each consumer uses (T1, first finding)
Four measures are in play; the routes below apply to different ones.
- (M1) **the joint law P_K** (torus-wide; reflection- and translation-invariant: EXISTENCE §13.1 (C), X-SYM^S).
- (M2) **the unnormalised cut functional** ω_G(F) := E_K[F·1_{G_k}], and **the all-cut law** P_cut,k = ω_G/P_K(G_k).
- (M3) **the per-history law** of (I_k) on Λ(𝔥) (RLARGE §8.1): P_K conditioned on a history 𝔥 and on the cut inside Λ(𝔥).
- (M4) **the fixed-V fluctuation law**: the law of U_k given U_{k+1} = V (with the cut), i.e. ∝ χ e^{-S_k(U)}K_k(V, U)dU;
  this is the ⟨·⟩_cut of Proposition CL (a) and the plugged sea of (DF).
Consumers. RLF-step step 6 prices new level-(k+1) bad cubes through Lemma RS: U_{k+1} is generated from U_k, so the
statement used is about (M1) (or (M2)), not (M4). (PLD)_k (ii) contains V = U_{k+1} (the coarse links C(Q) in ε_♭); for
(M4) it would be a property of the given V, not a probability; so it is a statement about (M1)/(M2). RLARGE §8.2 writes
"the all-cut level-k measure of (I_k) on Λ(𝔥)", i.e. (M3). The existence lane uses (M1) (Theorem CB) and (M2)
(Theorem CB-sg). Chessboard estimates need a reflection-invariant RP functional on the whole torus: (M1), (M2) only.
- **(PLD-F1) MET for (M3) and (M4).** 𝔥 and a fixed V are not reflection-symmetric, so Lemma CBE does not apply; and
  P_K(E | 𝔥) ≤ P_K(E)/P_K(𝔥) loses 1/P_K(𝔥), exponentially large in the size of 𝔥. Route (a) gives (M1)/(M2) statements;
  (M3)/(M4) need the (DF) route (§6) or a re-organisation of RLF-step that uses torus-wide probabilities (§12 item 2).
- **Normalisation of the cut (exact).** P_cut,k(E) = ω_G(E)/P_K(G_k) and P_K(G_k) = Z_∅/Z_K (definition; ∫K dV = 1). Given
  Proposition CL (a) at level k (which at effective levels is given (H-pos)_k), Z_K/Z_∅ = ⟨Ξ⟩_cut, so the normalised and
  unnormalised forms differ by exactly ⟨Ξ⟩_cut^{1/|𝒢|} per box. A bound on P_K(G_k) from below by crude means costs a
  factor per fine site (§5.3); so the hypotheses below are stated for ω_G (unnormalised), which is what Theorem CB-sg's
  proof actually uses: there P(∩_s f^{[s]}) = ω_G(all copies bad) (EXISTENCE §13.6, proof of CB-sg).

## 3. Lemma CB-m (multi-box chessboard reduction for the soft chain): PROVEN-HERE | X-RP^S, Lemma CBE, (C), (L), translation invariance
*Given* (EXISTENCE §13, PROVEN-HERE there, session 4, not yet independently reviewed; proofs re-read here [read], §0):
X-RP^S (reflection positivity of P_K for block-boundary planes), Lemma CBE (chessboard estimate; IMPORTED-AND-REVERIFIED
there), the reflection covariance (C) and locality (L) of §13.1, invariance of the law of (U_0, …, U_j) under level-j
lattice translations (Theorem CB's proof).
*Grids.* (G-a) For level j ≤ k: the **2-grid of offset o** ∈ {0,1}⁴: boxes o + 2y + {0,1}⁴ of level-j sites (n_j/2 per
direction, even). (G-b) **Cube grids**: boxes of b⁴ level-k cubes (b ∈ {1, 2}), cube offset in {0, …, b-1}⁴ (T_k/b per
direction, even). 𝔅_t := bounded measurable functions of the fine links in t, of the level-i links (i ≤ j for (G-a);
i ≤ k + 1 for (G-b)) whose cells (all ancestors' cells, by (L)) lie in t; a level-(k+1) link lies in 𝔅_t iff both endpoint
blocks (level-k cubes) lie in t.
*Claim.* Let ω ∈ {P_K} for (G-a), ω ∈ {P_K, ω_G, P_cut,k} for (G-b). For f_t ∈ 𝔅_t with 0 ≤ f_t ≤ 1:
  ω(Π_tf_t) ≤ Π_tΘ_ω(f_t),  Θ_ω(f) := ω(Π_{s∈𝒢}f^{[s]})^{1/|𝒢|}.
In particular, for any D ⊂ 𝒢 and events E_t ∈ 𝔅_t: ω(∩_{t∈D}E_t) ≤ Π_{t∈D}Θ_ω(1_{E_t}) (take f_t := 1 off D; Θ_ω(1) =
ω(1)^{1/|𝒢|} ≤ 1).
*Proof.* Lemma CBE needs, for each pair of antipodal planes between box layers, an involutive automorphism θ with
θ(𝔅_t) = 𝔅_{θt}, ω∘θ = ω and ω(θ(F)^*F) ≥ 0 for F in the algebra of one half; its inequality is homogeneous of degree 1 in
ω, so ω need not be normalised. (G-a): the planes between 2-boxes are planes between level-j sites, i.e. boundaries of
level-(j-1) cubes (planes of P_{K-j}); 𝔅_t consists of soft variables of levels ≤ j whose cells are on one side; X-RP^S
gives RP for P_K (the marginal of (U_0..U_j) suffices; later variables integrate out); (C) gives θ(𝔅_t) = 𝔅_{θt} and
θ-invariance. (G-b): the planes are between level-k cubes (planes of P_{K-k-1}); level-(k+1) links lie on one side iff
both endpoint cubes do; X-RP^S as before. For ω_G: 1_{G_k} = Π_Qχ_Q, every cube lies on one side and θ maps cubes to
cubes; χ_{θQ}(U) = χ_Q(θU) because θ maps interior plaquettes to interior plaquettes and ||1 - W||_op is invariant under
W ↦ W^{-1} and conjugation. With χ_+ := Π_{Q⊂+}χ_Q, 1_{G_k} = θ(χ_+)χ_+, so ω_G(θ(F)^*F) = E_K[θ(Fχ_+)^*(Fχ_+)] ≥ 0 by
X-RP^S (Fχ_+ is a positive-side function), and ω_G∘θ = ω_G. P_cut,k = ω_G/ω_G(1). Then Lemma CBE. ∎
*Remark.* For (G-a) the box events may involve only levels ≤ j: a level-(j+1) link joining two level-(j+1) sites has cells
of side L, which a 2-box of level-j sites does not contain; such events need (G-b).

**Corollary CB-m.1 (sparse families are dominated by dense ones).** (G-a), ω = P_K, level j. For a plaquette q and a
2-grid o such that q is interior to a box t(q) of the grid, put Θ_j(q, τ) := P_K(||1 - U_j(q^{[u]})||_op ≥ τ ∀u ∈ 𝒢_o)^{1/|𝒢_o|},
and **Θ_j(τ) := max over o and q of Θ_j(q, τ)** (by translation invariance there are 24 cases: 4 transverse positions × 6
orientations). Let 𝒢' be any grid of boxes of side b ≥ 2 (level-j sites; n_j/b even) and q interior to a box t' of 𝒢'. Then
  P_K(||1 - U_j(q^{[u']})|| ≥ τ ∀u' ∈ 𝒢') ≤ Θ_j(τ)^{|𝒢'|}.
More generally, for any set A of level-j plaquettes each interior to a box of ONE 2-grid o, at most one per box,
P_K(∀p ∈ A: ||1 - U_j(p)|| ≥ τ) ≤ Θ_j(τ)^{|A|}.
*Proof.* The second statement: Lemma CB-m on grid o with f_u := 1{the A-plaquette in u is bad} (1 if none); each f_u's
canonical copies are those of a plaquette interior to a 2-box, so Θ(f_u) ≤ Θ_j(τ). First statement: choose the 2-grid
offset o'_α in each direction so that t(q) ⊂ t' (possible since q is interior to t' and b ≥ 2: in the plaquette's two
directions t(q) is forced and lies in t'; in a transverse direction α take {x_α, x_α + 1} or {x_α - 1, x_α}, whichever lies
in t'). A reflection of 𝒢' is x ↦ 2c - x with 2c odd; it maps a 2-box {a, a + 1} to {2c - a - 1, 2c - a}, and
2c - a - 1 ≡ a (mod 2); so every 𝒢'-copy of q is interior to a box of the same 2-grid o', copies in distinct 𝒢'-boxes lie
in distinct 2-boxes (t(q) ⊂ t'), and the second statement applies. ∎

**Corollary CB-m.2 (plaquette families with disjoint neighbourhoods).** For every finite set A of level-j plaquettes with
pairwise disjoint 1-neighbourhoods and every τ: P_K(||1 - U_j(p)||_op ≥ τ ∀p ∈ A) ≤ Θ_j(τ)^{|A|/16}.
*Proof.* p = (x; μ, ν) is interior to a box of the 2-grid o iff o_μ ≡ x_μ and o_ν ≡ x_ν (mod 2); assign each p one such o,
giving classes A_o (16 offsets). Two plaquettes in one 2-box have all vertices within sup-distance 1, so their
1-neighbourhoods meet; hence at most one per box. Hölder with 16 factors: P(∩_A) = E[Π_o1_{∩A_o}] ≤ Π_oP(∩_{A_o})^{1/16}
≤ Π_oΘ_j^{|A_o|/16}. ∎

## 4. Proposition PLD-0 (the bare level): PROVEN-HERE | X-LRP, Lemma CBE, inequality (B)
*Claim.* At level 0 (P_K's marginal on U_0 is the Wilson measure at g_0, any even torus as in §0), for g_0 ≤ 1 and every
τ ∈ (0, 2]:
  Θ_0(τ) ≤ C_0g_0^{-p_0}e^{-τ²/(2Ng_0²)},  C_0 := e^{768}c_N^{-64},  p_0 := 64(N² - 1).
Hence (PLD-i)_0: for A with disjoint 1-neighbourhoods, P(||1 - U_0(p)|| ≥ τ ∀p ∈ A) ≤ (C_0g_0^{-p_0}e^{-τ²/(2Ng_0²)})^{|A|/16};
and for every family A_p of copies of one plaquette in a grid of boxes of side ≥ 2 (in particular CB-sg's super-blocks),
ω_G(all of A_p bad) ≤ P_W(all of A_p bad) ≤ (C_0g_0^{-p_0}e^{-τ²/(2Ng_0²)})^{|A_p|} (Corollary CB-m.1).
*Proof.* Lemma CB-m (G-a) at j = 0 is Lemma CBE with X-LRP (fine link mid-planes). Fix a pattern q in a 2-box and let E be
the event that all n_B := |𝒢| copies are bad. Z[E] := ∫_Ee^{-(1/g²)Σ_ps(U_p)}dU ≤ e^{-n_Bτ²/(2Ng²)}: every term of the
action is ≥ 0, each copy has s ≥ ||1 - U||²_op/(2N) ≥ τ²/(2N) (inequality (B)), Haar mass 1. Z ≥ ∫_{||U_b - 1||_op ≤ g ∀b}
e^{-S}: there ||1 - U_p||_op ≤ 4g, so s(U_p) = ||1 - U_p||²_HS/(2N) ≤ ||1 - U_p||²_op/2 ≤ 8g² and S/g² ≤ 8 per plaquette; with
4 links and 6 plaquettes per site and 16 sites per box, Z ≥ [(c_Ng^{N²-1})^{64}e^{-768}]^{n_B}. Divide and take the
n_B-th root. ∎
*Remark (where the volume factor sits).* The entropy factor is per FINE site ((c_Ng^{N²-1})^{-4}e^{48}); it is harmless at
level 0 because the box has 16 sites. Any bound for a level-k event obtained by the same count at level 0 pays it for the
L^{4k} fine sites of a level-k box (§5.3).

## 5. One-step transfer and finite depth; why it does not give uniformity

### 5.1 Proposition PLD-step: PROVEN-HERE | Lemma KN, Corollary KN-step, Lemma RS (R1)-(R2), Lemma CB-m, Corollary CB-m.1
*Given* (EXISTENCE §13.6, PROVEN-HERE there, unreviewed; both proofs re-checked line by line here [read]: the identity for
R := W'^{-1}M̄ - 1, the bound (e^δ - 1)² + δ²e^δ ≤ 3δ² for δ ≤ 1/4, Re tr((1 - Z^{-1})(1 + R)) ≥ ¼x² for x ≥ 12√Nδ², the
D4-norm (2) lower bound on 𝒩, |θ| ≤ (π/3)|e^{iθ} - 1| on the principal arc, the telescoping and the constant c_1):
**Lemma KN** and **Corollary KN-step in conditional form**: for t ≤ t_N := 1.5/√N and g_{k-1}² ≤ κ, for every U_{k-1},
  P(||1 - U_k(P)||_op ≥ t | U_{k-1}) ≤ 1{η_P(U_{k-1}) ≥ c_1t} + w_{k-1}(t),  w_i(t) := 4ec_N^{-1}(κ/g_i²)^{N²-1}e^{-κt²/(256Ng_i²)},
η_P := max ||1 - U_{k-1}(q)||_op over the level-(k-1) plaquettes q with all vertices in U_4(P). (KN-step's proof is a bound
on the conditional kernel probability on {η_P < c_1t}; its two conditions t ≤ 1/(106√NA_d²c_1²) = 1.59/√N and
(π/3)A_dc_1t ≤ 1/4 (t ≤ 3.1) hold for t ≤ t_N at L = 3.)
*Claim.* With n_U := 24L⁴ (≥ the number of plaquettes with all vertices in U_4(P)), for every k ≥ 1 and t ∈ (0, t_N]:
  Θ_k(t) ≤ w_{k-1}(t) + n_U·Θ_{k-1}(c_1t).
*Proof.* Fix a 2-grid 𝒢 of level-k sites and a pattern p; p_u its copy in u. A 2-box of level-k sites is a box of side 2L
level-(k-1) sites, and U_4(p_u) (the level-(k-1) blocks of p_u's four corners) lies in u. Given U_{k-1}, the level-k links
are independent (product kernel), and distinct p_u have disjoint link sets, so
P_K(∩_u{p_u bad} | U_{k-1}) = Π_uP(p_u bad | U_{k-1}) ≤ Π_u(w + 1{η_{p_u} ≥ c_1t}). Expand the product and take the
expectation: P_K(∩_u{p_u bad}) ≤ Σ_{S⊂𝒢}w^{|𝒢∖S|}P_K(∩_{u∈S}{η_{p_u} ≥ c_1t}). For each u ∈ S, 1{η_{p_u} ≥ c_1t} ≤
Σ_{q⊂U_4(p_u)}1{q bad at c_1t}; expanding gives ≤ n_U^{|S|} choice functions u ↦ q_u. For each choice, {q_u bad} ∈ 𝔅_u
(level-(k-1) links in u), and Lemma CB-m on the same grid 𝒢 viewed at level k - 1 (its planes are between level-k sites,
i.e. between level-(k-1) cubes, where X-RP^S holds for level-(k-1) functions) gives P_K(∩_{u∈S}{q_u bad}) ≤
Π_{u∈S}Θ_𝒢(q_u), and Θ_𝒢(q_u) ≤ Θ_{k-1}(c_1t) by Corollary CB-m.1 (𝒢 has side 2L ≥ 2 in level-(k-1) sites). So the sum is
≤ Σ_Sw^{|𝒢∖S|}(n_UΘ_{k-1}(c_1t))^{|S|} = (w + n_UΘ_{k-1}(c_1t))^{|𝒢|}. Take the |𝒢|-th root and the max over patterns. ∎

### 5.2 Corollary PLD-fin (every fixed depth): PROVEN-HERE (counted with PLD-step) | PLD-0, PLD-step
For k ≥ 0, t ∈ (0, t_N], g_0 ≤ 1, g_i² ≤ κ, and 0 < g_0 ≤ g_1 ≤ … ≤ g_k (the order (F) gives):
  Θ_k(t) ≤ Σ_{m=0}^{k-1}n_U^mw_{k-1-m}(c_1^mt) + n_U^kΘ_0(c_1^kt) ≤ (k + 1)n_U^k·B_0·e^{-a_kt²/g_k²},
  B_0 := max{4ec_N^{-1}(κ/g_0²)^{N²-1}, C_0g_0^{-p_0}},  a_k := c_1^{2k}·min{κ/(256Nc_1²), 1/(2N)}  (= c_1^{2k}/(2N) for κ ≥ 0.01).
Hence (PLD-i)_k holds at every FIXED k for P_K, with a_η = a_kη_1²/16 and C = ((k + 1)n_U^kB_0)^{1/16} (Corollary CB-m.2).
**[RPLD-fix F-1] The constant is polynomial in 1/g_0, not a constant.** B_0 contains g_0^{-p_0} and (κ/g_0²)^{N²-1}, so C
contains g_0^{-p_0/16}(κ/g_0²)^{(N²-1)/16}. At fixed k it is absorbed as follows. The upper half of (F) gives
g_0^{-2} ≤ g_k^{-2}(1 + β_+k log L·g_k²) ≤ (1 + β_+k log L)g_k^{-2} (g_k ≤ 1), so g_0^{-p} ≤ (1 + β_+k log L)^{p/2}g_k^{-p}. For
a' < a, g^{-p}e^{-a/g²} ≤ C'e^{-a'/g²} with C' := (p/(2e(a - a')))^{p/2} (the maximum of x^{p/2}e^{-(a-a')x}, x = 1/g²). So
(PLD-i)_k holds with any a'_η < a_η and a constant C(k, a_η - a'_η), at every fixed k (check p3 C).
*Proof.* Iterate 5.1 (thresholds only decrease, so t ≤ t_N is kept); then 1/g_i² ≥ 1/g_k² in every exponent and
1/g_i² ≤ 1/g_0² in every prefactor; c_1^{2m}κ/(256N) ≥ c_1^{2k}·κ/(256Nc_1²) for m ≤ k - 1. ∎

### 5.3 Why route (a) and route (b) stop here (route obstructions, not no-gos)
- **(PLD-F2) MET for the threshold-transfer recursion: the exponent decays geometrically with depth.** a_k ≤ c_1^{2k}/(2N),
  while (F) gives only 1/g_{k-m}² - 1/g_k² ≤ β_+m log L. The m-th term of 5.2 is ≥ n_U^m exp(-κc_1^{2m}t²(1/g_k² +
  β_+(m + 1)log L)/(256N)) **[RPLD-fix F-2: a lower bound on the term needs the UPPER half of (F), β_+; session 1 wrote
  β_- here]**; since c_1^{2m}m → 0, the terms do not decay in m and the sum is not bounded uniformly in k. The loss
  c_1 per level is not slack in the transfer: it comes from the square bound (R2) (constant L², attained, c32 A5) and the
  ribbon bound (R1) (A_d, attained, c32 A5), i.e. from coherent level-(k-1) configurations. Those configurations are
  expensive in total, not per plaquette: L⁴ level-(k-1) plaquettes of size t/L² carry action ~ t²/g² per level-k cube, the
  d = 4 marginality of Lemma 2.2 (A1). A pointwise transfer prices one plaquette; it cannot see that total.
- **(PLD-F2) MET for a one-level energy/entropy count at the fine level.** Pricing a level-k disseminated event at level 0
  as in §4 needs Z ≥ (entropy per fine site)^{#sites}: per level-k 2-box this is (c_N^{-1}g_0^{-(N²-1)})^{64L^{4k}}e^{768L^{4k}},
  against an energy gain per box of at most a constant times 1/g_0² (the cost of the event in the fine Wilson action; under
  (F) the target exponent a/g_k² is even smaller, 1/g_k² ≤ 1/g_0² - β_-k log L). The count therefore fails once
  64(N² - 1)L^{4k}log(1/g_0) exceeds a constant times 1/g_0², i.e. for k ≳ (log(1/g_0²) - log log(1/g_0) - C)/(4 log L). (The typical fine action in a level-k box is itself ~ L^{4k}g_0²·(N² - 1)/4,
  so even the deterministic statement "a level-k large field forces fine action ≥ c" does not help: the fine field's
  action in the box is dominated by fluctuations that cancel in block averages.) The cancellation is a concentration
  property of block averages of the fine field: the small-field package.
- **(PLD-F3) does NOT occur: the normalisation 𝒩 costs no volume factor, and no 1/g² per link from 𝒩.** [RPLD-fix F-3:
  this is a statement about 𝒩 only; in a Peierls map the kernel NUMERATOR still changes by e^{O(κ/g²)·mismatch} per link.] Write
  σ(M) := N^{-1}max_{V∈SU(N)}Re tr(V^{-1}M). Then exactly
    k_c(V, U) = exp(-(κ/g²)[σ(M̄_c) - N^{-1}Re tr(V^{-1}M̄_c)])/𝒩̃(M̄_c),  𝒩̃(M) := ∫exp(-(κ/g²)[σ(M) - N^{-1}Re tr(V^{-1}M)])dV,
  (multiply numerator and denominator by e^{(κ/g²)(1-σ)}), and e^{-1}c_N(g²/κ)^{N²-1} ≤ 𝒩̃ ≤ 1 (D4-norm (2): a Haar ball around
  the maximiser; the integrand is ≤ 1). So the shrinkage 1 - σ(M̄) cancels exactly and a local Peierls modification of U_j
  on a region R changes the normalisations of the next kernel by at most the factor (ec_N^{-1}(κ/g_j²)^{N²-1})^{n(R)}, n(R)
  the number of level-(j+1) links whose contours meet R: a polynomial factor per affected link, of the same type as the
  g^{-p} entropy factor. In route (b) a Peierls map for a level-k defect must nevertheless act on every level 0, …, k - 1
  in the defect's region (otherwise the kernel K_{j-1}(U_j, U_{j-1}) penalises a smoothed U_j against a rough M̄(U_{j-1})),
  and at level 0 it meets the fine entropy count of the previous item. So route (b) stops at the same place as route (a),
  for the Wilson measure's entropy, not for 𝒩.

## 6. The reduction of (PLD-i), (PLD-ii), (PLD-mod) to one disseminated statement, and its linear-functional form

**Hypothesis (PLD-dis)_k (the remaining wall; HYPOTHESIS).** There are a_d > 0, C_d < ∞, p_d ≥ 0, independent of K, k,
the torus and the coupling sequence (within (F), g_K ≤ g_0), such that for every τ ∈ (0, ε_1]:
  Θ_k(τ) ≤ C_dg_k^{-p_d}e^{-a_dτ²/g_k²}  (2-grids, P_K), and Θ^G_k(τ) ≤ C_dg_k^{-p_d}e^{-a_dτ²/g_k²},
where Θ^G_k(τ) := max over super-block grids (2⁴ cubes) and plaquettes q interior to a super-block of
ω_G(all copies of q bad)^{1/|𝒢|}. (PLD-0 is the case k = 0 with a_d = 1/(2N), p_d = p_0; PLD-fin gives k ≤ k_0 with a_d
depending on k_0.) [RPLD-fix B6: "the coupling sequence (within (F))" must read "the soft chain's own effective coupling
sequence (A5), or sequences in (F) with β_- ≥ β_1 - o(1)" (PLD-AF (W-F3); §15.6 E1); this applies wherever this file
writes "within (F)", including T1 and (SG)_k.]

**Hypothesis (SG)_k (a sufficient linear-functional form; HYPOTHESIS).** There are σ_*, m_* (independent of K, k, the torus,
the coupling sequence) such that for every finite set A of level-k plaquettes and every s = (s_p) ∈ su(N)^A,
  E_K[1_{G_k}·exp(Σ_{p∈A}⟨s_p, F_p⟩_HS)] ≤ exp(σ_*²g_k²|s|²/2 + m_*g_k|s|_1),
F_p := a measurable logarithm of U_k(p) with eigenvalues in (-π, π] (the principal one on G_k for cube-interior p),
|s|² := Σ_p|s_p|²_HS, |s|_1 := Σ_p|s_p|_HS. Also (SG)_k^{full}: the same with 1_{G_k} omitted.
**[RPLD-fix F-4] F_p must be su(N)-valued.** The principal logarithm of U ∈ SU(N) lies in u(N), not su(N): its trace is
2πi·m, m ∈ Z, and m ≠ 0 at -1 ∈ SU(2) and at the non-trivial central elements of SU(N). Paired with s_p ∈ su(N) it is seen
only through its traceless part, and at U = ω·1 that part is 0 while ||1 - U|| > 0. Replace the definition by:
F_p := TL(U_k(p)), where TL is the measurable su(N)-valued logarithm of **Lemma TL** (§15.1): e^{TL(U)} = U, tr TL(U) = 0,
||TL(U)||_op ≤ 3π, and TL(U) is the principal logarithm whenever ||1 - U||_op < 2 sin(π/N). Then
||1 - U||_op ≤ ||1 - U||_HS ≤ |TL(U)|_HS still holds (eigenvalues: |1 - e^{iθ}| ≤ |θ| for real θ). On G_k, for cube-interior p,
||1 - U_k(p)||_op < ε_1 < 2 sin(π/N) once ε_1 < 2 sin(π/N) (implied by RLARGE §1A's R1819-fix 8 compatibility condition
ε_1 ≤ the N5 threshold), so the ω_G statements are unaffected; the (SG)^{full} statements on P_K use TL.

**Lemma HS (Gaussian linearisation): PROVEN-HERE (elementary).** (SG)_k implies, for every finite set A of level-k
plaquettes (no disjointness needed) and every τ > 0,
  ω_G(|F_p|_HS ≥ τ ∀p ∈ A) ≤ (C_HSe^{-τ²/(4σ_*²g_k²)})^{|A|},  C_HS := (2√2e^{m_*²/(2σ_*²)})^{N²-1};
the same for P_K under (SG)_k^{full}. Since ||1 - U||_op ≤ ||1 - U||_HS ≤ |TL(U)|_HS (eigenvalues: |1 - e^{iθ}| ≤ |θ|), the
same bound holds for the events ||1 - U_k(p)||_op ≥ τ. [RPLD-fix F-4: |log U| replaced by |TL(U)|.] The proof uses only
that the measure is a positive finite measure and Fubini; it applies verbatim to any probability measure satisfying the
(SG) inequality, in particular to the per-history measure of §15.3.
*Proof.* Let ξ be a standard Gaussian vector on su(N)^A ≅ R^{(N²-1)|A|} (orthonormal HS basis), independent. For λ > 0,
e^{λΣ_p|F_p|²} = E_ξe^{√(2λ)⟨ξ, F⟩}. By Fubini (all terms ≥ 0) and (SG)_k with s = √(2λ)ξ,
E_K[1_Ge^{λΣ|F_p|²}] ≤ E_ξexp(λσ_*²g²|ξ|² + √(2λ)m_*g|ξ|_1). At λ := 1/(4σ_*²g²) the exponent is |ξ|²/4 + c|ξ|_1,
c := m_*/(√2σ_*), and |ξ|_1 = Σ_p|ξ_p|_HS ≤ Σ_{p,a}|ξ_{p,a}|. For one standard coordinate,
E e^{ξ²/4 + c|ξ|} = (2π)^{-1/2}·2∫_0^∞e^{-(ξ - 2c)²/4}dξ·e^{c²} ≤ (2π)^{-1/2}·2√(4π)e^{c²} = 2√2e^{c²}. So
E_K[1_Ge^{λΣ|F_p|²}] ≤ (2√2e^{c²})^{(N²-1)|A|}. Markov: 1_GΠ_p1{|F_p| ≥ τ} ≤ 1_Ge^{λ(Σ|F_p|² - |A|τ²)}. ∎

**Proposition PLD-red: PROVEN-HERE | Lemma CB-m, Corollaries CB-m.1-2, Lemma KN, Lemma RS (R1), Lemma HS.**
- (i) (PLD-i)_k for P_K ⇐ (PLD-dis)_k: P_K(∀p ∈ A: ||1 - U_k(p)|| ≥ η_1) ≤ (C_dg_k^{-p_d}e^{-a_dη_1²/g_k²})^{|A|/16} (CB-m.2).
- (ii) (PLD-ii)_k for P_K ⇐ (PLD-dis)_k at the threshold η_♭ := 3ε_loc/(4(1 + 1.2A_d)) (= 0.0636ε_loc at L = 3): for every
  finite set 𝒜 of level-k cubes,
    P_K(ε_♭(U; Q) > ε_loc ∀Q ∈ 𝒜) ≤ (n_RΘ_k(η_♭)^{1/16} + 8w_♭)^{|𝒜|/7⁴},  n_R := 6(3L)⁴,
    w_♭ := ec_N^{-1}(κ/g_k²)^{N²-1}e^{-κε_loc²/(64Ng_k²)}.
  So a_♭ = min{a_dη_♭²/16, κε_loc²/(64N)}/7⁴, up to the polynomial prefactors.
- (iii) (PLD-mod)_k in unnormalised form ⇐ (SG)_k, for every family (copies or not): ω_G(||1 - U_k(p')|| ≥ τ ∀p' ∈ A) ≤
  (C_HSe^{-τ²/(4σ_*²g_k²)})^{|A|}; and (SG)_k ⇒ (PLD-dis)_k with a_d = 1/(4σ_*²), C_d = C_HS, p_d = 0 (Lemma HS).
  **[RPLD-fix F-5]** Precisely: (SG)_k gives the ω_G half (Θ^G_k) and (SG)_k^{full} gives the P_K 2-grid half (Θ_k); the
  implication "(SG)_k ⇒ (PLD-dis)_k" needs both, i.e. read "(SG)_k + (SG)_k^{full} ⇒ (PLD-dis)_k" here, in §8 and in §11.
*Proof of (ii).* Greedy: 𝒜' ⊂ 𝒜 with pairwise cube sup-distance ≥ 4, |𝒜'| ≥ |𝒜|/7⁴; monotonicity. For Q ∈ 𝒜' take
U° := U in the definition of ε_♭ (RLARGE §5): ε_♭ ≤ max_{p⊂N_1(Q)}||1 - U_p|| + max_{c∈C(Q)}||V_c - S_c(U)||, V := U_{k+1}. For
c ∈ C(Q) the contours of c lie in its two endpoint blocks ⊂ N_1(Q); on {max_{p⊂N_1(Q)}||1 - U_p|| < η_♭}, Lemma RS (R1) and
|θ| ≤ (π/3)|e^{iθ} - 1| give δ_c := max_i||X_i|| ≤ (π/3)A_dη_♭ ≤ 1/4 (T_i = S_ce^{X_i}), and ||W'_c - S_c|| = ||e^{X̄} - 1|| ≤
1.14δ_c ≤ 1.2A_dη_♭. So if also ||V_c - W'_c||_HS < ε_loc/4 for all c ∈ C(Q), then ε_♭ < η_♭(1 + 1.2A_d) + ε_loc/4 = ε_loc.
Given U_k, the level-(k+1) links are independent; the sets C(Q), Q ∈ 𝒜', are disjoint (distance ≥ 4); on the small
event, Lemma KN (t := ε_loc/4 ≥ 12√Nδ_c², true since δ_c ≤ 0.6ε_loc and ε_loc ≤ (ε_1²/(4Nb_1))^{1/2} ≤ 1/(36√N),
using ε_1 ≤ 2 and b_1 ≥ n_P = 1296 at L = 3, RLARGE §5) gives conditional probability ≤ 8w_♭ that some
c ∈ C(Q) (|C(Q)| = 8) has ||V_c - W'_c||_HS ≥ ε_loc/4. Hence, as in 5.1, P(∩_{𝒜'}) ≤ Σ_{S⊂𝒜'}(8w_♭)^{|𝒜'∖S|}
P(∀Q ∈ S ∃p ⊂ N_1(Q) bad at η_♭) ≤ Σ_S(8w_♭)^{|𝒜'∖S|}n_R^{|S|}max_{choices}P(∩_{Q∈S}{p_Q bad}); the chosen p_Q lie in
N_1(Q)'s at distance ≥ 4 cubes, so their 1-neighbourhoods are disjoint, and CB-m.2 bounds the last factor by
Θ_k(η_♭)^{|S|/16}. ∎ (Statements (i), (iii): CB-m.2 and Lemma HS.)
*Remarks.* (1) **[RPLD-fix B2: narrowed; session 1 called this a "correction" to RLARGE §8.2's sketch, which overstated
it.]** RLARGE l.603-604 asks for "(DF3') for general linear functionals with ℓ¹ control … and a union bound over disjoint
supports". Read with its first half this is the joint-exponential-moment route: (DF3') for Σ_p⟨s_p, F_p⟩ plus a union
bound over a net of directions s, at a cost C^{|A|}; it does give a product bound, and it is the same route as (SG) +
Lemma HS with a net in place of Gaussian averaging (§15.3, Lemma HS-net, writes it out). What stands: a family of
one-point bounds (LD) does not imply a product bound, and the phrase "union bound over disjoint supports" is ambiguous;
the product bound comes from the joint exponential moment, not from the union bound.
(2) **Polynomial prefactors suffice for the existence lane.** Corollary H-Bal-3T^S needs C_me^{-a_mp(g)²/N} ≤ g²/2 with
p(g) = (log 1/g)^{p_*}, p_* > 1/2; C_dg^{-p_d}e^{-a_dp(g)²/N} ≤ g²/2 also holds for small g, since p(g)²/log(1/g) → ∞.
(3) **Normalised forms.** P_cut,k(E) = ω_G(E)·⟨Ξ⟩_cut (§2); a per-cube bound log⟨Ξ⟩_cut ≤ C N_ke^{-a/g_k²} (RLF's own bulk
statement at level k) turns every unnormalised bound into a normalised one with C → Ce^{Ce^{-a/g_k²}}.

## 7. Proposition PLD-lin (the linearised soft chain: uniform in depth): PROVEN-HERE (model statement) | Lemma 2.2 (A1, LINEAR_PACKAGE, CONFIRMED)
*Model (LS).* Levels 0, …, k as LINEAR_PACKAGE §1.1, one real component per copy (N² - 1 independent copies), each level in
its own units. B_0: the centred Gaussian on (ker d)^⊥ ⊂ level-0 1-forms with density ∝ exp(-||dB_0||²/(2γ_0²)), so F_0 := dB_0
is centred Gaussian on im d with covariance γ_0²·1_{im d}. Independent noises ξ_i ~ N(0, s_i²·1) on level-(i+1) links, and
B_{i+1} := Q_rootB_i + ξ_i. (This is the quadratic part of the normalised soft chain: the kernel exponent
(κ/g²)(1 - N^{-1}Re tr e^X) = (κ/(2Ng²))|X|²_HS + O(X⁴) gives s_i² = Ng_i²/κ per HS-orthonormal component, the Wilson action
γ_0² = Ng_0², and 𝒩 cancels the shrinkage, §5.3, so the kernel is centred at the linearised mean Q_root.)
*Claim.* F_k := dB_k is centred Gaussian with ||Cov F_k||_op ≤ σ_k² := γ_0² + 16Σ_{i<k}s_i²L^{-2(k-1-i)}. Hence for every
finite set A of level-k plaquettes (no disjointness) and τ > 0,
  P(|F_k(P)| ≥ τ ∀P ∈ A) ≤ (2^{(N²-1)/2}e^{-τ²/(4σ_k²)})^{|A|}   (|·| the HS norm over the N² - 1 copies).
With the SU(N) values and g_i ≤ g_{k-1} ≤ g_k: σ_k² ≤ Ng_0² + 16Ng_{k-1}²/(κ(1 - L^{-2})) ≤ Ng_k²(1 + 18/κ) at L = 3, uniformly
in k, the volume and the UV cutoff.
*Proof.* (1) **Identity.** Q_root = Q_str - d∘h (LINEAR_PACKAGE §1.2; re-verified here: avg_{σ,y}∫ over the contour
P^σ(c_X → y)·S_y·P^σ(c_Y → y + Le_μ)^{-1} splits into h(X) + (Q_strA)(X, μ) - h(X + e_μ), because the far-end path is the
translate by Le_μ and y + Le_μ runs over B(X + e_μ)). And Q_str∘d = d∘avg (avg := the block mean of a 0-form; the line sums
telescope: L^{-4}Σ_{y∈B(X)}(λ(y + Le_μ) - λ(y))). So d∘Q_root = d∘Q_str and, inductively, d∘Q_root^m = d∘Q_str^m
(d∘Q_str∘(d∘h) = d∘d∘avg∘h = 0). (2) **Contraction of the noise.** Q_str (one step, own units) has entries
c_{(X,μ),(z,μ)} = L^{-4}#{(y, j): y ∈ B(X), j < L, y + je_μ = z} ≥ 0 with row sums L and column sums L^{-3} (for fixed z and
j, y = z - je_μ lies in exactly one block); Schur's test gives ||Q_str||² ≤ L·L^{-3} = L^{-2} (equality for constant fields).
On a torus, ||d||² ≤ ||d*d + dd*|| = ||Δ|| ≤ 4·4 = 16. So ||dQ_root^m|| = ||dQ_str^m|| ≤ 4L^{-m}. (3) **The fine part.** By
Lemma 2.2 (i), dQ_rootA = M dA with M linear, and by (ii) ||MF|| ≤ ||F|| for F ∈ im d (d = 4); M maps im d into im d (MdA =
d(Q_rootA)). So the composite M^{(k)} restricted to im d has norm ≤ 1 and Var⟨G, M^{(k)}F_0⟩ ≤ γ_0²||G||². (4) **Sum.**
F_k = M^{(k)}F_0 + Σ_{i<k}dQ_root^{k-1-i}ξ_i, independent terms; Var⟨G, F_k⟩ ≤ (γ_0² + Σ_is_i²·16L^{-2(k-1-i)})||G||². (5) **The
bound.** Per copy, E exp(λΣ_{P∈A}F_P²) = det(1 - 2λΣ_A)^{-1/2} with Σ_A ≤ σ_k² (a principal block of the covariance); at
λ = 1/(4σ_k²) each eigenvalue of 2λΣ_A is ≤ ½, so the determinant factor is ≤ 2^{|A|/2}; multiply over copies; Markov on
{Σ_P|F_P|² ≥ |A|τ²}. (6) 16/(1 - 1/9) = 18. ∎
*What it shows.* (a) The injected noise reaches level-k curvature only through d∘Q_str^m: its pure-gauge part (d∘h) has no
curvature and the straight average contracts by L^{-1} per level, so the noise contributions form a geometric series. The
log-divergence of EXISTENCE §13.6's recursion ||Σ_{k+1}|| ≤ ||Σ_k|| + 24g_k²/κ comes from tracking the curvature alone: it
forgets that the earlier noise curvature is exact and is contracted again at every later step. (b) The soft kernel costs
the factor (1 + 18/κ) in the variance, not a depth or volume factor (with LINEAR_PACKAGE Prop. 7.1 (A2), the deterministic
case, as the κ → ∞ limit). (c) It is the Gaussian instance of (PLD-dis)_k and of (SG)_k^{full} (σ_*² = N(1 + 18/κ), m_* = 0),
not a statement about SU(N): it is the target that the non-perturbative argument has to reproduce. [RPLD-fix F-5: the
model satisfies (SG)_k^{full} only; the ω_G form needs the cut, which the linear model has no analogue of.] [Session 3,
§15.2: the model has no running, and that is exactly where SU(N) differs for smooth s; the ℓ¹ term of (SG) is
load-bearing there.]

## 8. What remains for T1, exactly (the wall (PLD-dis) / (SG))
- **What is proven:** the reduction of every multi-defect form to one disseminated quantity per level (§3, §6), the bare
  level (§4), every fixed depth with depth-dependent constants (§5), the linearised soft chain uniformly (§7).
- **What is not:** (PLD-dis)_k uniformly in k for SU(N). Its content is a concentration statement for block averages of
  the Wilson field, uniform over scales; §5.3 shows that positivity of the action, the kernel and chessboard estimates do
  not supply it (the obstruction is the entropy of the fine fluctuations, which only cancels in block averages).
- **Two halves of (SG)_k (ARGUED; not counted).** Write U_k as the image of (U_0, X_0, …, X_{k-1}), X_i := log(W'^{-1}V) the
  kernel deviations at step i, conditionally sub-Gaussian given the past by Lemma KN (with the shift 12√Nδ²).
  - *Noise half.* On small-field histories the level-k curvature is Lipschitz in X_i with constant C·4L^{-(k-1-i)}(1 + Cε)^{k-1-i}
    (the non-linear version of §7 (2)), so a martingale (Azuma-type) bound for conditionally sub-Gaussian increments gives
    the noise part of (SG)_k with proxy ~ Σ_iL^{-2(k-1-i)}Ng_i²/κ, uniformly in k. What is missing: the non-linear Lipschitz
    bound (the non-abelian form of d∘Q_root = d∘Q_str, i.e. that the pure-gauge part of a kernel deviation carries no
    curvature at later levels), and the large-field histories (RLF itself).
  - *Wilson half.* The remaining term is the m-fold block average of the bare field U_0 under the Wilson measure, i.e. a
    concentration bound for smeared fine curvature at scale L^k. In the downward (RG) organisation it is the statement
    that the fluctuation field's curvature d𝒞W has no low-momentum component (the kernel pins block averages): the dual
    of §7 (a), a symbol-level property of the soft fluctuation covariance, which is node N5. The crude downward recursion
    σ_k²g_k² ≤ σ_{k+1}²g_{k+1}² + C_0²g_k² (interpolation has operator norm 1 at p → 0 in d = 4) diverges like the depth, for
    the same reason as in (a).
- So (PLD) is "[s given SF]" in a sharper sense than RLARGE §11 item 2 states: given (DF1)-(DF2) at every level and the
  low-momentum suppression of d𝒞 (N5), (SG)_k follows by the downward recursion with a summable noise term [ARGUED]; and
  (SG)_k ⇒ (PLD-dis)_k ⇒ (PLD-i), (PLD-ii), (PLD-mod) [PROVEN].

## 9. T2: returned clusters in the fluctuating sea (W1-ret')

### 9.0 The statement (from RLARGE §8.2, all quantifiers; the form RLF-step step 3 consumes)
Level k; V ∈ 𝒱_{k+1} (a level-(k+1) field in the small-field domain of node A); ⟨·⟩_V := the fixed-V fluctuation law (M4),
∝ 1_{G_k}e^{-S_k(U)}K_k(V, U)dU on the sea region. Pointwise in a cut sample D = (U, V), Theorem R1 (i) (cutoff n_♯) gives
log Ξ(D) = Σ_xΣ_{N≤n_♯}Σ_{S∋x}𝓖^{(N)}_S(D)/|S| + (tail N > n_♯), over defect configurations with n ≤ n_♯.
**(W1-ret')_k.** There are g-independent a > 0, κ_d > 0, C and field-independent numbers c̄_0^{sea}(g_k), δβ_k^{sea} with
|c̄_0^{sea}| + |δβ_k^{sea}| ≤ Cg_k^{-6}e^{-a/g_k²}, such that for every K, k, torus and V ∈ 𝒱_{k+1}:
(a) log⟨e^{Σ_x𝒢_x}⟩_V = N_kc̄_0^{sea} + δβ_k^{sea}Σ_Ps(V_P) + Σ_Xℛ^{sea}(X; V), 𝒢_x := Σ_{N≤n_♯}Σ_{S∋x}𝓖^{(N)}_S/|S|;
(b) each ℛ^{sea}(X; ·) is gauge invariant, C³, depends on V in X up to e^{-κ_dd} tails, and is an irrelevant activity in the
norm of the small-field package, with the complex extension of (RLF-5);
(c) defect configurations with n(𝒟) > n_♯ carry weights ≤ (Ce^{-a/g_k²})^{n(𝒟)}.

### 9.1 Proposition SHADOW: the (H-ch) clause of RLARGE §1A's defect definition is incompatible with (c) and (RLF-3). PROVEN-HERE | RLARGE §1A, §7.2 definitions, D4-norm, ||M̄_c||_op ≤ 1
*Claim.* Let k ≥ 1, n_c := n_♯, ε_♮ and R_* = (n_c + 2)L as in RLARGE §7.2, Q_0 a level-k cube, p a plaquette interior to
Q_0 and b one of its links. Then
  P_cut,k(the *-component of collar-bad cubes containing Q_0 has ≥ (2n_c + 1)⁴ cubes) ≥ ¼e^{-3κε_♮/g_{k-1}²}.
Hence no bound "weight of a defect configuration 𝒟 ≤ (Ce^{-a/g_k²})^{n(𝒟)}" that dominates its cut-law probability can
hold for small g_k: for 6400Ce^{-a/g_k²} ≤ ½ such weights sum, over the configurations containing Q_0 with ≥ (2n_c + 1)⁴
cubes, to ≤ 2(6400Ce^{-a/g_k²})^{(2n_c+1)⁴} ((g3) count), which is < ¼e^{-3κε_♮/g_{k-1}²} once g_k is small.
**[RPLD-fix F-6: direction of the coupling comparison.]** Session 1 wrote "(g_{k-1} ≤ g_k)" here; that inequality makes
e^{-3κε_♮/g_{k-1}²} smaller than e^{-3κε_♮/g_k²}, i.e. it weakens the lower bound, so it cannot give the comparison. The
comparison uses the UPPER half of (F): 1/g_{k-1}² ≤ 1/g_k² + β_+ log L, so ¼e^{-3κε_♮/g_{k-1}²} ≥ ¼L^{-3κε_♮β_+}e^{-3κε_♮/g_k²},
and 2(6400Ce^{-a/g_k²})^{(2n_c+1)⁴} < ¼L^{-3κε_♮β_+}e^{-3κε_♮/g_k²} for all small g_k as soon as (2n_c + 1)⁴a > 3κε_♮ (and
6400Ce^{-a/g_k²} ≤ ½). This holds with enormous room (n_c ~ 10¹³, ε_♮ ≤ ε_loc/3 < 0.007).
**[RPLD-fix F-7: the bridge.]** "Weight that dominates its cut-law probability" means: in the (I_k) representation the
probability (under the level-k cut law) of the event that the defect configuration of the sample contains 𝒟 is (Σ of the
weights of the histories containing 𝒟)/Z, and these weights are ≥ 0 (they are integrals of e^{-S}·indicators). So a bound
on the weights of the configurations containing Q_0 with ≥ (2n_c + 1)⁴ cubes bounds that probability from above; this is
the reading used by RLARGE's (P1) and by EXISTENCE's (RLF-3^dis).
*Proof.* Let F := {some plaquette among p and the plaquettes containing b has ||1 - U_k||_op > ε_♮}. Fix R ∈ SU(N) with
||1 - R||_op = 3ε_♮ (ε_♮ ≤ ε_loc/3 ≤ ε_1/12) and T: U_k(b) ↦ U_k(b)R (other variables fixed); T is a Haar-preserving
bijection. In the joint law of (U_0, …, U_k), U_k(b) enters only through k_b(U_k(b), M̄_b(U_{k-1})), and the exponent changes by
(κ/g_{k-1}²)N^{-1}|Re tr((R^{-1} - 1)U_k(b)^{-1}M̄_b)| ≤ (κ/g_{k-1}²)·3ε_♮ (|N^{-1}tr(AB)| ≤ ||A||_op||B||_op, ||M̄|| ≤ 1); 𝒩(M̄_b)
does not change. On F^c ∩ G_k: the plaquette p becomes ||1 - (TU)_p|| ≥ ||1 - R|| - ||1 - U_p|| > ε_♮, and every plaquette
containing b stays ≤ 4ε_♮ < ε_1, so T(F^c ∩ G_k) ⊂ F ∩ G_k. Hence P_K(F ∩ G_k) ≥ e^{-3κε_♮/g_{k-1}²}P_K(F^c ∩ G_k), so
P_cut(F) ≥ min{¼, ¾e^{-3κε_♮/g_{k-1}²}}. On F some plaquette with ||log U|| ≥ ||1 - U|| > ε_♮ lies within fine sup-distance 2 of
p, hence in B̂_*(c_Q) for every cube Q within cube sup-distance n_c of Q_0 (nL + L + 2 ≤ R_* for n ≤ n_c, L ≥ 3), so (H-ch)
fails on all these (2n_c + 1)⁴ boxes and these cubes are collar-bad and *-connected. ∎
*What fails and what does not.* The ε_♭ clause is local (it involves N_1(Q) and C(Q) only) and is priced by (PLD-ii)
(PLD-red (ii)). The (H-ch) clause is non-local (radius R_* = (n_♯ + 2)L, with n_♯ ~ 10¹³ for the crude constants): one
moderately rough plaquette (> ε_♮, still cut-good) makes ~(2n_♯)⁴ cubes "defective" at the price of one plaquette.
**Fix (proposed to RLARGE; §12 item 3).** (i) Collar-badness by the local clause only, with U° := the sample's own links:
σ_Q := 1{max_{p⊂N_1(Q)}||1 - U_p|| ≤ ε_loc/2 and max_{c∈C(Q)}||V_c - S_c(U)|| ≤ ε_loc/2}; then σ_Q = 1 for all Q ∈ Y implies
ε_♭(U; Y) ≤ ε_loc for the cluster Y (N_1(Y) = ∪N_1(Q), C(Y) = ∪C(Q)), which is what Proposition CL (c) needs for a cluster
with σ ≡ 1 on Y (this answers REVIEW_S16_S17 R-3a's coupling objection: one global U°, the sample, serves every cube).
**[RPLD-fix B4: session 1 wrote "which is all Proposition CL (c) and Theorem R1 (i) need, without (H-ch)"; withdrawn as
overstated.]** R1 (i)'s convergent gas and the pointwise 𝒢_x of §9.0 need CL (c) for EVERY cluster in the gas. Under the
fix, CL (c) holds only for clusters with σ ≡ 1 on Y; returned collar-bad configurations (σ_Q = 0 for some Q, n ≤ n_♯) have
no CL (c) bound, so §9.0's pointwise expansion does not cover them. Repair (proposed; not written as a proof here):
(α) define 𝒢_x from the σ-restricted gas, i.e. Theorem R1 (i) with σ in place of (H-ch) (Lemma 7.2-0's proof verbatim,
with the hypothesis "ε_♭ ≤ ε_loc on the support" supplied by σ ≡ 1); (β) put the returned collar-bad configurations into
(SC)_k explicitly, as an additional activity family 𝓗^{cb}_X(V) := the sea average of their frozen weights, with its own
bound: given (PLD)_k (ii) on the per-history law (§15.3, with its status there), Σ_{X∋x}|𝓗^{cb}_X| ≤ Σ_{n≥1}80^{2(n-1)}(C_♭e^{-a_♭/g_k²})^{n} per cube
(bound on the weights; their smoothness in V is part of (SC)_k). This closes REVIEW_S18_S19 G5 by σ_Q, not by a box-local
(H-ch).
(ii) Do no Taylor extraction in the level-k sample (R1 (ii)-(iii) are not applied pointwise); extract after the sea
average, in V, at the trivial datum V = 1 (§9.2-9.3), so that the extracted numbers are defined for every V and the chart
condition enters only the BOUND on the remainder. (The alternative, counting defects by "primary" rough cubes with their
own Peierls exponent a_♮ ∝ ε_♮², is circular as stated: ε_♮ ≤ r_1(R_*) shrinks polynomially in R_* ∝ n_♯, while n_♯ ≥
4/(a_♮β_-) grows like 1/ε_♮²; ARGUED, not written.)

### 9.2 Lemma W1R-sym (symmetry survives the sea average): PROVEN-HERE | (C), gauge covariance of the kernel, invariance of S_k
*Claim.* Let 𝒢_x(U, V) be the localised graded logarithm of 9.0 (or any family {F_S} of functions of D = (U, V) with
F_S(R·D) = F_{R^{-1}S}(D) for R in the stabiliser B_4 of the block centre c_x, and gauge invariant). Put
F^{sea}_x(V) := log⟨e^{Σ_y𝒢_y}⟩_V localised by any B_4-covariant base-point rule, or simply A_x(V) := ⟨Σ_{S∋x}F_S/|S|⟩_V. Then
A_x(R·V) = A_x(V) for R ∈ B_4 about c_x, A_{x+a}(τ_aV) = A_x(V) for level-(k+1) lattice translations, and A_x(g·V) = A_x(V)
for every coarse gauge transformation g. The same holds for log⟨e^{Σ_y𝒢_y}⟩_V (a torus-wide functional) under all three.
*Proof.* S_k is invariant under the lattice symmetries of the torus that preserve the block structure up to level k + 1 and
under fine gauge transformations (exact chain: μ_K is, the kernels are covariant by (C) and decision 4's covariance, and
∫ preserves invariance); 1_{G_k} is (the cuts are B_4-symmetric); K_k(R·V, R·U) = K_k(V, U) ((C)); K_k(g|_roots·V, g·U) =
K_k(V, U) (PROOF L5 [S9]). Change variables U = R·U' (Haar invariant) in numerator and denominator of ⟨·⟩_{R·V}:
⟨Φ(·, R·V)⟩_{R·V} = ⟨Φ(R·U', R·V)⟩_V. With Φ = Σ_{S∋x}F_S/|S| and F_S(R·D) = F_{R^{-1}S}(D), the sum over S ∋ x is permuted
(R fixes c_x, so x ∈ R^{-1}S ⟺ x ∈ S, |R^{-1}S| = |S|). Translations: the same with τ_a. Gauge: extend g to a fine gauge
transformation agreeing with g at the roots. ∎ (For the hypercubic part the torus must have equal sides; EXISTENCE ES1
allows a different time side ℓ_0, for which B_4 is replaced by its subgroup preserving the time axis, and GT-lat' (ii)'s
scalar conclusion then needs the irreducibility of Λ²R⁴ under that subgroup, which fails: §12 item 4.)

### 9.3 Lemma W1R-tay (re-extraction at level k + 1, no ε_V): PROVEN-HERE | GT-lat' (RLARGE §4), W1R-sym
**[RPLD-fix F-8]** Locality of A_x in a box B̂ is a HYPOTHESIS of this lemma. ⟨·⟩_V is a torus-wide measure, so A_x(V) is
not local in general; locality is supplied only by (SC1) in Proposition W1R. The scalar conclusion uses GT-lat' (ii)'s
clause "if a finite family {F_i} is permuted by D ↦ R·D for every R ∈ B_4, then Σ_iQ_{F_i}(Φ) = c̄·Σ_a||Φ_a||²_HS"
(RLARGE l.233-234), applied at level k + 1 with B_4 the stabiliser of the site x (the one-element family {A_x}, invariant
by W1R-sym).
*Claim.* Let A_x be as in 9.2 and suppose it depends on V only inside a box B̂ of radius R_0 (level-(k+1) units) about the
site x, and is C³ on GT-lat's chart ball {ε_2(V) ≤ r_1(R_0)} with K_A := GT-lat's derivative constant. Apply GT-lat' with
the level-(k+1) links as the fine links and C := ∅ (no coarser links; ε_V := 0). Then, for V in the chart ball,
  A_x(V) = A_x(1) + δβ^{(x)}·Σ_{P based at x}s(V_P) + R_x(V),  δβ^{(x)} := 2N·(1/6)tr t^{A_x}  [RPLD-fix F-8: typo "/1" removed],
  |R_x(V)| ≤ C(R_0)K_A𝔯^♭_x(V) + C'K_Aε_2(V)⁴,  𝔯^♭ := ε_2ε_3 + ε_3² + ε_2³ (of V on B̂),
where t^{A_x} is the 6 × 6 matrix of GT-lat' (i), which is scalar by W1R-sym and GT-lat' (ii) (the one-element family {A_x}
is invariant), and A_x(1), δβ^{(x)} do not depend on x (translation covariance) or on V. Summing over x:
  Σ_xA_x(V) = N_{k+1}·A_0(1) + δβ^{sea}Σ_Ps(V_P) + Σ_xR_x(V),  δβ^{sea} := δβ^{(0)}.
*Proof.* GT-lat' (i)-(ii) with C = ∅; Φ_x(V) = (log V_{(x;a)})_a are the plaquette logs AT x, so the identification
Σ_a||Φ_{x,a}||²_HS = 2NΣ_{P based at x}s(V_P) + O(N²ε_2⁴) is exact up to the quartic term (R4D-iso step 4: 1 - N^{-1}Re tr e^Y =
||Y||²_HS/(2N) + O(Y⁴)); every level-(k+1) plaquette has exactly one base point. ∎
*What this changes against pointwise R1 (iii) (REVIEW_S16_S17 R-6).* The pointwise remainder of R1 (iii) contains
ε_V = max||log(V_cS_c(U)^{-1})||, the mismatch between the coarse link and the fine straight transporter of the SAME sample:
it is the soft residual, O(g_k/√κ) in every sample, and it is not a function of the next-level field. After the sea average
at fixed V it is integrated out: R_x depends on V only, and its Taylor expansion at V = 1 has no constant term, and its
quadratic part differs from the Ad-invariant form of the base plaquettes by terms bounded by ε_2ε_3 + ε_3² (curvature times
a lattice difference of curvature, or two differences), i.e. terms of power-counting dimension ≥ 5 in d = 4.
*What it does not change (honest order).* In a level-(k+1) sea sample ε_3(V) ~ ε_2(V) ~ g_{k+1}, so 𝔯^♭ = O(g_{k+1}²) still:
the remainder is not small relative to the extracted quadratic part sample by sample. "Irrelevant" can only mean: of
power-counting dimension ≥ 5, and contracted by the next steps of the small-field package in its norm (node A4). This is a
requirement on (SF), named:
**(SF-irr)_{k+1} (HYPOTHESIS; part of node A).** Activities at level k + 1 that are gauge invariant, local with e^{-κ_dd}
tails, C³ on the chart ball with derivative constant K, and bounded there by K𝔯^♭ (+ quartic), and bounded by K elsewhere
in the cut-good domain, are admissible irrelevant activities of the small-field package at level k + 1, with norm ≤ CK.
(The clause "elsewhere in the cut-good domain" is the middle regime g p(g) ≲ ε_2(V) < ε_1, where no Taylor chart is
available: RLARGE's large-field threshold ε_1 is g-independent, so this regime belongs to (SF), not to RLF.)

### 9.4 What feeds 9.3: the sea expansion at fixed V (named hypothesis)
**(SC)_k (HYPOTHESIS; the fixed-V form of (DF1)-(DF4) with Theorem CE, cf. W1-loc (cl) [S9, ARGUED]).** For V ∈ 𝒱_{k+1}:
log⟨e^{Σ_x𝒢_x}⟩_V = Σ_X𝓗^{sea}_X(V), X polymers of level-(k+1) cubes, with (SC1) 𝓗^{sea}_X depends on V only in a fixed
fattening of X, is gauge invariant, and the family is covariant (𝓗^{sea}_{RX}(R·V) = 𝓗^{sea}_X(V), R in the lattice
symmetry group); (SC2) Σ_{X∋x}sup_{chart}|∂^q𝓗^{sea}_X|e^{κ_dd(X)} ≤ Cg_k^{-p}(Λ/g_k²)^qe^{-a/g_k²} for q ≤ 3; (SC3) the
GT-lat' constants of the boxes of X grow at most like e^{κ'd(X)} with κ' < κ_d.
**Proposition W1R (CONDITIONAL): (W1-ret')_k (a)-(b) ⇐ (SC)_k + (SF-irr)_{k+1}.** Put A_x := Σ_{X∋x}𝓗^{sea}_X/|X|. By (SC1) and
9.2 it is invariant under B_4 about x, under translations and gauge; apply 9.3 to each 𝓗^{sea}_X/|X| on the box of X and
sum with (SC2)-(SC3): c̄_0^{sea} := Σ_{X∋0}𝓗^{sea}_X(1)/|X|, δβ_k^{sea} := 2N·(1/6)Σ_{X∋0}tr t^{𝓗_X}/|X| (scalar after summing the
B_4-permuted family, GT-lat' (ii)), with |c̄_0^{sea}| + |δβ_k^{sea}| ≤ C'g_k^{-6-p}e^{-a/g_k²}, and remainder Σ_xR_x obeying the
bounds of (SF-irr). [The derivation is the one of R1 (iii), at level k + 1 with C = ∅; written above; its inputs are the
hypotheses.] [RPLD-fix B4: session 1 added "(W1-ret') (a) needs no (H-ch) at level k at all under fix 9.1 (ii)"; withdrawn.
What is true: the EXTRACTION (9.3) needs no (H-ch) and no ε_V. The sea expansion (SC)_k still needs the σ-restricted gas
and the collar-bad family of §9.1's repair (α)-(β).] **[RPLD-fix, review: W1R]** (SC)_k is close in strength to
(W1-ret') (a)-(b) themselves; what Proposition W1R proves is the bookkeeping: symmetry survives the sea average, and the
extraction can be done at V = 1 with a remainder depending on V only.
- **(RLF-5) width (ARGUED, not counted).** The frozen activity r_Y = Num_Y/Den_Y is entire in the data (an integral of the
  entire function e^{-S}K over a compact set), with |Num^ℂ| ≤ e^{C|Y|ρκ/g²}·(real bound) on a complex neighbourhood of width ρ;
  the only obstruction to analyticity is Den_Y^ℂ = 0. Den_Y is an integral over cut-good inner configurations, and
  log Den^ℂ - log Den = log⟨e^{iφ + O(ρ²κ/g²)}⟩ with φ linear in the imaginary part and of size (κ/g²)ρ·(inner residual); if the
  inner residual is sub-Gaussian at scale g/√κ (a finite-region small-field statement, R4D-iso type), |⟨e^{iφ}⟩| ≥ ½ for
  ρ ≤ cg/√κ. Then |r^ℂ_Y| ≤ 2e^{C|Y|√κ/g}·C_r^{|Y|}g^{-p_r|Y|}e^{-ε_1²|Y|/(4Ng²)}: the width is O(g/√κ) and the e^{O(1/g)} growth is
  absorbed by the large-field factor. Whether width O(g) is the width node A's norm requires is fixed by node A.

### 9.5 (W1-ret') (c): the torus-wide probabilistic form. PROVEN-HERE (counted with PLD-red) | PLD-red (ii)
With collar-badness by σ_Q (fix 9.1 (i)), every cube Q of a defect configuration 𝒟 (bad, or σ_Q = 0) has a plaquette in
N_1(Q) with ||1 - U|| > ε_loc/2, or (bad) one ≥ ε_1, or a coarse link c ∈ C(Q) with ||V_c - S_c(U)|| > ε_loc/2. Split at
η_♭' := ε_loc/(4.8A_d) (≤ η_♭): if every plaquette of N_1(Q) is < η_♭', then δ_c ≤ (π/3)A_dη_♭' ≤ 0.22ε_loc, ||W'_c - S_c|| ≤
1.2A_dη_♭' = ε_loc/4, so ||V_c - W'_c||_HS > ε_loc/4, and Lemma KN applies with t = ε_loc/4 (12√Nδ_c² ≤ 0.58√Nε_loc² ≤ ε_loc/4 as
ε_loc ≤ 1/(36√N)). The rest of the proof of PLD-red (ii) is verbatim, with η_♭' for η_♭. So
  P_K(every cube of 𝒟 is defective) ≤ (n_RΘ_k(η_♭')^{1/16} + 8w_♭)^{n(𝒟)/7⁴}  for every finite cube set 𝒟,
and given (PLD-dis)_k this is (Ce^{-a_c/g_k²})^{n(𝒟)} with a_c := min{a_dη_♭'²/16, κε_loc²/(64N)}/7⁴ (polynomial prefactors
absorbed for g_k small). This is the form the existence lane's reading of RLF-3 uses (torus-wide P_K). The per-history
weight form of (c) inside RLF-step is (HIST)'s, not proven here; Proposition SHADOW shows it is false with the (H-ch)
clause and this subsection shows the local clause is consistent with it.

## 10. Check p1 (criteria first: checks/p1_criteria.md; script checks/p1_pld.py; output checks/p1_out.txt; record checks/p1_time.txt)
**All parts PASS, first and only run** (2.6 s, peak RSS 97 MB, load 4.4, 38% memory free, numeric lock, nice 10, threads 1;
python3 without -I, user-site numpy; no external files).
- G (validity): dot tests ≤ 2e-17; Q_root(dλ) = d(ev λ) to 4e-14.
- A: λ_max(Q_strQ_str^T) = 0.111111111111111 = L^{-2} at T = 2 and 3: Schur's bound is attained (constant fields).
- B: dQ_root = dQ_str to 5e-15; Q_root = Q_str - dh to 3e-15.
- C: λ_max(Σ_k) = 16, 16.724, 16.792 (T = 2, k = 1, 2, 3) against the bound 16, 17.778, 17.975 and the additive 16, 32, 48;
  increments 0.724, 0.067 (ratio ≈ 1/10.7, close to L^{-2}): the noise covariance saturates geometrically, as §7 states.
  T = 3: 12, 12.741. λ_max(dd^T) = 16 at T = 2 (attained), 12 at T = 3.
- D: ratios 0.50, 0.64, 0.92, 0.99999 (c = 0, ¼, 1, 3): the constant 2√2e^{c²} is sharp as c grows.
- E: max ||1 - e^X||_HS/||X||_HS = 0.99999997 over 4000 samples.
- F (informational): the m-th exponent of Corollary PLD-fin is 3.9·10⁻³, 9·10⁻²⁴, 2·10⁻⁴⁴ (m = 0, 5, 10): the finite-depth
  constants degrade geometrically (§5.3).
Scope: p1 tests the linear model and elementary inequalities; it tests nothing about SU(N), Lemma CB-m or SHADOW.

## 11. Outcome against the pre-stated targets (§1)
- **T1: PARTIAL SUCCESS as pre-stated.** Every multi-defect form is reduced, by written proofs, to one disseminated
  quantity per level: (PLD-i) and (PLD-ii) for P_K ⇐ (PLD-dis)_k (Lemma CB-m, Corollaries CB-m.1-2, PLD-red (i)-(ii)); (PLD-mod)
  in unnormalised form ⇐ (SG)_k (Lemma HS), and (SG)_k ⇒ (PLD-dis)_k. Proven cases: the bare level (PLD-0, a = 1/(2N) per
  plaquette at fixed threshold τ, C_0 = e^{768}c_N^{-64}, p_0 = 64(N² - 1), exponent /16 for disjoint-neighbourhood families);
  every fixed depth (PLD-fin, a_k = c_1^{2k}/(2N), C = (k + 1)n_U^kB_0); the linearised soft chain uniformly in depth (PLD-lin,
  exponent τ²/(4N(1 + 18/κ)g_k²), C = 2^{(N²-1)/2}, no disjointness). Failure modes: **(PLD-F1) MET** for the per-history and
  fixed-V measures (M3)/(M4) (chessboard needs a reflection-invariant torus functional); **(PLD-F2) MET** for both the
  threshold-transfer recursion (geometric exponent loss c_1² per level, attained by coherent configurations) and the
  one-level fine count (entropy per fine site, a factor (Cg_0^{-p})^{L^{4k}} per level-k box); **(PLD-F3) does NOT occur**:
  the normalisation 𝒩 cancels the shrinkage exactly and costs only a polynomial factor per affected coarse link. The wall
  is (PLD-dis)_k uniformly in k for SU(N), a concentration statement for block averages of the Wilson field (§8).
- **T2: PARTIAL, with one negative finding.** (W1-ret') stated with all quantifiers (§9.0). **Proposition SHADOW:** with
  RLARGE §1A's (H-ch) clause, (c) and (RLF-3) are false for small g (one rough plaquette, probability ≥ ¼e^{-3κε_♮/g²},
  creates a defect configuration of ≥ (2n_♯ + 1)⁴ cubes); fix proposed (local collar clause σ_Q; extraction only after the
  sea average). Under the fix: symmetry and re-extraction at level k + 1 PROVEN (W1R-sym, W1R-tay; the remainder depends on
  V only, contains no ε_V, and its quadratic part is of dimension ≥ 5); (a)-(b) CONDITIONAL on (SC)_k and (SF-irr)_{k+1}
  (Proposition W1R); (c) in torus-wide form PROVEN ⇐ (PLD-dis)_k (§9.5). Honest order (as REVIEW_S16_S17 R-6 says): in a
  level-(k+1) sample the remainder is still O(g²) relative; "irrelevant" means dimension ≥ 5 in the (SF) norm, named as
  (SF-irr). The exact step that needs the small-field package: (SC)_k (the fixed-V sea expansion with covariant polymers)
  and the norm of node A.
- **T3: MET.** p1, criteria first, all PASS.
- Not-success items avoided: no union bound is used as a product bound (session 1 added "and RLARGE §8.2's sketch is
  corrected, §6 Remark (1)"; **[RPLD-fix B2] withdrawn**: the sketch read as joint exponential moment + net is a valid
  route, §6 Remark (1) as narrowed); no constant depends on K, k (except PLD-fin, which says so) or the volume; every use of (SF)-type input is named
  ((PLD-dis), (SG), (SC), (SF-irr)).

## 12. Proposed changes for the owners of other files (not made here)
1. **RLARGE §8.2 (PLD)_k and EXISTENCE §13.6 (PLD^mod_dis):** state the measure. Proposed: (M1)/(M2) torus-wide, in
   unnormalised form ω_G (what CB-sg's proof uses), on the even-torus family; polynomial prefactors C_dg^{-p_d} allowed
   (they suffice for Corollary H-Bal-3T^S, §6 Remark (2)). Replace "a union bound over disjoint supports" by "a chessboard
   estimate (Lemma CB-m) or a joint exponential moment ((SG), Lemma HS)".
2. **RLF-step (RLARGE §8.3):** steps 4 and 6 consume (PLD) for the per-history law (M3), which route (a) does not reach
   (PLD-F1). Either restate those steps with torus-wide probabilities (as the existence lane does), or route (PLD) for (M3)
   through (SG) proven per history from (DF).
3. **RLARGE §1A item 2 (two thresholds):** drop "(H-ch) fails on Q's box" from collar-badness (Proposition SHADOW); use
   σ_Q (§9.1 (i)); move the Taylor extraction after the sea average (§9.1 (ii), §9.3). [RPLD-fix B4: session 1 ended
   this item with "R1 (i) then needs no (H-ch)"; withdrawn. R1 (i) then needs the σ-restricted gas, and the returned
   collar-bad configurations enter (SC)_k as their own activity family (§9.1 repair (α)-(β)).]
4. **Tori.** Chessboard results here hold for the even tori of EXISTENCE ES1 (side 4L^M); RLARGE's "every torus with
   side ≥ 3 blocks" is not covered; and if the time side differs (ES1 allows it), B_4 shrinks to the subgroup fixing the time
   axis, under which Λ²R⁴ is not irreducible (it splits into the electric and magnetic triplets), so GT-lat' (ii) gives two
   coupling shifts, not one. RLARGE's torus should be hypercubic, or the anisotropic shift must be allowed.

## 13. Status and tally contribution (lane E, session 1; reviewed by REVIEW_PLD_S1_S2: 0 GAP, 0 WRONG among counted items; fixes applied session 3, [RPLD-fix])
- **PROVEN-HERE [E1], counted (7):** Lemma CB-m (with Corollaries CB-m.1, CB-m.2); Proposition PLD-0; Proposition PLD-step
  (with Corollary PLD-fin); Lemma HS with Proposition PLD-red (and §9.5); Proposition PLD-lin (a model statement: the
  linearised soft chain); Proposition SHADOW; Lemmas W1R-sym + W1R-tay (one item).
- **CONDITIONAL:** Proposition W1R ((W1-ret') (a)-(b) ⇐ (SC)_k + (SF-irr)_{k+1}).
- **New named hypotheses:** (PLD-dis)_k (the wall), (SG)_k (sufficient form), (SC)_k, (SF-irr)_{k+1}.
- **ARGUED (not counted):** §8's two halves of (SG) (noise half by a martingale bound; Wilson half = N5's low-momentum
  suppression); §9.1's circularity of the primary-defect alternative; §9.4's (RLF-5) width O(g/√κ).
- **Not closed:** (PLD) and (W1-ret') stay inside RLF-step as named hypotheses, now reduced as above. Imported inputs used
  as given and re-read here: X-RP^S, Lemma CBE, Lemma KN, Corollary KN-step (EXISTENCE §13, unreviewed there), X-LRP
  (IMPORTED-AND-REVERIFIED there), Lemma 2.2 (A1, CONFIRMED), GT-lat' and Lemma RS (RLARGE, confirmed by REVIEW_S16_S17),
  D4-norm (2), inequality (B).
- **Tally (proposal for the ledger owner):** +7 PROVEN-HERE (unreviewed), 0 OPEN items closed, 0 new top-level OPEN items
  (the new hypotheses sit inside L5's RLF reduction).

---
# Session 2 (2026-10-27, lane E)

Inputs read this session (read-only): this file §0-§13 [read]; PLD_LOG [read]; EXISTENCE.md §14 in full (l.1732-1962:
Lemmas GS-1, GS-2, Theorem GS, Corollary PLD-G^S, X-KER^S) and §15.0-§15.2 (l.1966-2156: Lemmas NA-1, NA-2, Proposition
NA-3, Theorem NA-GS1, (NA-R2), the bias verdict) [read]; EXISTENCE l.818-830 (X-NTAF-sharp, W-AF1, W-AF2) [read]; PROOF.md
S19 block l.5200-5393 (Lemma N5-an, CT♯, Theorem RW, Corollary RW-triv, Theorem N5-sf0, Proposition N5-sf_i, target C)
[read]; RLARGE.md §0-§1 (l.40-80, flow hypothesis (F)) [read]; LINEAR_PACKAGE.md: only as restated in §7 and in EXISTENCE
§14 (Lemma 2.2 (A1), Lemma 2.4 (IT), §1.2 (R)) [read-skim; frozen, not re-read this session].

## 14.0 Targets (pre-stated 2026-10-27 23:36 UTC, before any session-2 derivation and before checks/p2_criteria.md)

**T4 ((PLD-dis)_k uniformly in k, SU(N)).** Prove (PLD-dis)_k (§6) with a_d, C_d, p_d independent of K, k, the torus
and the coupling sequence, or name the exact wall with the precise loss term. Routes (any): (a) small-field/large-field
split with the LF-count arithmetic of the depth recursion; (b) transfer to the fine field (Theorem GS's identity: soft
gauge-invariant content = straight average) and fine-field concentration via the Wilson measure's chessboard bounds;
(c) Brascamp-Lieb / log-Sobolev in the small-field chart.
- **Success:** (PLD-dis)_k PROVEN-HERE uniformly.
- **Partial success:** (PLD-dis)_k reduced, by written proofs, to statements that are each strictly narrower than
  (PLD-dis)_k (named, with all quantifiers and the measure), with at least one reduction step that is an exact
  equivalence or an implication in both directions, so that the remaining wall is located and not merely renamed.
- **Valid failure outcomes:** (W-F1) a proven necessary condition showing that (PLD-dis)_k, as quantified in §6,
  contains an open statement of another node (named); (W-F2) for each route attempted, the per-level loss term written
  as an explicit expression in (k, g_k, β_±, L, N, κ), with the exact summability condition it violates; (W-F3) a
  quantifier of (PLD-dis)_k (the coupling sequence, the measure, the threshold range) that must change for the
  statement to be consistent.
- **Not success:** a recursion whose constants depend on k presented as uniform; a union bound used as a product
  bound; an energy (Cauchy-Schwarz) bound that pays the fine entropy per level without saying so; any use of (SF),
  (DF), RLF, node A or the flow (F) beyond its lower/upper bracket without naming it.

**T5 (check p2; criteria file checks/p2_criteria.md written before checks/p2_*.py).** Test numerically the new exact
constants and inequalities that T4's written proofs use (identities of the linear block map, flow arithmetic, the tail
integration), nothing about SU(N) measures.

# Session 2 derivations (written after §14.0 and after checks/p2_criteria.md)
**[RPLD-fix B3] The parenthesis above is not supported by the record and is corrected here (not rewritten).**
checks/p2_criteria.md (mtime 23:38:33 UTC) already contains session-2 results (w_P = L^{-4}m(z_μ)m(z_ν), Σw² = 361/729,
the closed form of PLD-AF (ii)), so derivation sketches preceded the criteria; and this file's last session-2 write
(mtime 23:44:49 UTC) precedes the "00:10 UTC" end time in PLD_LOG. The order supported by the file times is: §14.0
targets (logged 23:36 UTC) → derivation sketches (unwritten or not separately saved) → p2 criteria (23:38:33) → p2 script
(23:39:31) → p2 run (output 23:40:24) → §14.1-§14.9 write-up (finished by 23:44:49). See PLD_LOG, session-3 correction.
The checks test identities and arithmetic only, so no conclusion changes.

Notation: X_u := ||1 - U_k(q_u)||_op for the copies q_u (u ∈ 𝒢) of a level-k plaquette pattern q in a 2-grid 𝒢 of
level-k sites (§3 (G-a)); B_u := {X_u ≥ τ}; Θ_k(τ) as in Corollary CB-m.1; P_W := the Wilson measure at g_0 (P_K's
U_0-marginal); R_u := the fine sites whose level-k ancestor lies in u (a box of 2L^k fine sites per direction).

## 14.1 Proposition PLD-AF ((PLD-dis) contains an AF upper bound): PROVEN-HERE | Lemma CB-m, inequality (B)
*Claim.* Suppose (PLD-dis)_k holds at level k (2-grid part) with constants (a_d, C_d, p_d). Then for every level-k
plaquette P, with B := C_dg_k^{-p_d}:
(i) P_K(||1 - U_k(P)||_op ≥ τ) ≤ Be^{-a_dτ²/g_k²} for τ ∈ (0, ε_1];
(ii) E_K||1 - U_k(P)||²_op ≤ (g_k²/a_d)(1 + log₊B) + 4Be^{-a_dε_1²/g_k²}, hence
  E_K[s(U_k(P))] ≤ (g_k²/(2a_d))(1 + log₊(C_dg_k^{-p_d})) + 2C_dg_k^{-p_d}e^{-a_dε_1²/g_k²}.
*Proof.* (i) P is interior to a box t of some 2-grid; Lemma CB-m with f_t := 1{P bad}, f_{t'} := 1 (t' ≠ t) gives
P_K(P bad) ≤ Θ(f_t) ≤ Θ_k(τ). (ii) With X := ||1 - U_k(P)||_op ∈ [0, 2], E X² = ∫_0^2 2tP(X ≥ t)dt. For τ_0 ≤ ε_1,
∫_0^{τ_0} ≤ τ_0², ∫_{τ_0}^{ε_1} ≤ B∫_{τ_0}^∞2te^{-a_dt²/g²}dt = (g²/a_d)Be^{-a_dτ_0²/g²}, ∫_{ε_1}^2 ≤ (4 - ε_1²)P(X ≥ ε_1) ≤
4Be^{-a_dε_1²/g²}. Take τ_0² := (g²/a_d)log₊B if this is ≤ ε_1² (the middle term is then ≤ g²/a_d); otherwise bound
∫_0^{ε_1} by ε_1² ≤ (g²/a_d)log B. Finally s(U) = ||1 - U||²_HS/(2N) ≤ ||1 - U||²_op/2. ∎ (Check p2 E: the closed form
dominates the numerical tail integral in all 18 cases.)
*Reading.* **(W-F1) MET.** Uniform-in-k (PLD-dis) contains the statement "the soft chain's level-k block plaquette is
≤ C g_k²log(1/g_k), uniformly in k", i.e. an AF upper bound (with a logarithm) for soft block plaquettes, measured against
the coupling sequence. The law of U_k is fixed by g_0 and the kernel couplings g_0, …, g_{k-1}; the bound compares this
output with the sequence's g_k. So (PLD-dis) cannot be proved by any argument that does not, in effect, control the
running of the block-plaquette scale between levels 0 and k: this is the content of EXISTENCE's "AF upper bound" item
and of W-AF2 (EXISTENCE l.828: "a Gaussian comparison for block observables in the small-field region, uniform in the
depth"), and of node A5 / (F) in RLARGE §0.
**(W-F3) MET (the coupling-sequence quantifier).** §6 states (PLD-dis) "uniformly in the coupling sequence within (F)".
In RLARGE's normalisation the one-loop rate is β_1 := 4Nb_0 = 11N²/(12π²) (0.3715 for SU(2), 0.8359 for SU(3); the
value that reproduces RLARGE's n_* = 382 and 255, check p2 D). Granting one-loop perturbation theory for block plaquettes
[STANDARD perturbative fact, not re-derived; ARGUED here]: E s(U_k(P)) ≥ c g̃_k² with 1/g̃_k² = 1/g_0² - β_1k log L + O(log k).
For a sequence in the bracket with 1/g_0² - 1/g_k² ≤ β_+k log L and β_+ < β_1, at fixed g_k the one-loop value satisfies
1/g̃_k² ≤ 1/g_k² - (β_1 - β_+)k log L + O(log k) → -∞: the soft chain's level-k scale leaves the weak-coupling range
while g_k stays fixed, so the block plaquette is not O(g_k²log(1/g_k)) and (ii) fails for large k. So (PLD-dis) is consistent only for sequences running at least as fast as the soft chain itself: the
quantifier must be "for the soft chain's own effective coupling sequence" (node A5's object, as EXISTENCE §15.2 reads (F):
"a statement about the effective couplings g̃_k of the soft chain"), or "for sequences in (F) with β_- ≥ β_1 + o(1)", not
"for every sequence in the bracket". The proposed wording is in §14.9. **[RPLD-fix B6]** (i) Read "β_- ≥ β_1 - o(1)" for
"β_- ≥ β_1 + o(1)" above (the sequence must run at least as fast as the chain, up to o(1)). (ii) The same argument reaches
beyond (PLD-dis): RLF itself is quantified "for every coupling sequence with g_K ≤ g_0 obeying (F)" (RLARGE §1A, l.124-125)
and EXISTENCE's (RLF-3^dis) "independent of … the coupling sequence (within (F), g_K ≤ g_RLF)" (EXISTENCE l.1536-1538). For a
sequence with β_+ < β_1, one-loop running [ARGUED] puts the level-k field at strong coupling relative to g_k for large k,
bad cubes then have probability O(1), not e^{-a/g_k²}, and both quantifiers are inconsistent. The precise amendment is
§15.6 item E1; it applies to every consumer of (F), not only to (PLD-dis).

## 14.2 Lemma CONE and Theorem SPLIT ((PLD-dis) is a statement about the fine Wilson measure): PROVEN-HERE | (L) of §13.1, product kernels, X-LRP, Lemma CBE, (C)
**Lemma CONE.** For u ∈ 𝒢 let cone(u) be the set of level-j links (1 ≤ j ≤ k) whose two endpoint level-j sites have
their fine blocks in R_u. Given U_0, the families (U_j(c))_{c∈cone(u)}, u ∈ 𝒢, are conditionally independent, and the
conditional law of the family of u depends on U_0 only through U_0|_{R_u} (the fine links with both ends in R_u). Hence
p_u(U_0) := P_K(B_u | U_0) is a function of U_0|_{R_u}, p_{θu}(θU_0) = p_u(U_0) for every reflection θ of the grid, and
for every S ⊂ 𝒢: P_K(∩_{u∈S}B_u) = E_W[Π_{u∈S}p_u].
*Proof.* The joint density of (U_1, …, U_k) given U_0 is Π_{j<k}Π_{c of level j+1}k_c(U_{j+1}(c); M̄_c(U_j)) (Markov chain,
product kernel). M̄_c depends only on the level-j links in c's two endpoint blocks (the contours of c lie there; §6 proof
of PLD-red (ii), (L) of §13.1); for c ∈ cone(u) these are links of cone(u) (j ≥ 1) or fine links in R_u (j = 0). Integrate
out the links outside ∪_ucone(u) from the top level down: a level-k such link occurs only in its own factor, which
integrates to 1 (∫k_c dV = 1); once all such links of levels > j are gone, the factors containing a non-cone level-j link
are only its own, which integrates to 1 (no cone factor at level j + 1 depends on it). What remains is
Π_uΠ_{c∈cone(u)}k_c, each factor a function of cone(u) and U_0|_{R_u}. B_u depends only on the four links of q_u, which
lie in cone(u) since q_u is interior to u. Covariance: (C) (the chain is invariant under the lattice symmetries acting on
all levels, and θ maps the copy in u to the copy in θu). Last identity: E[Π1_{B_u}] = E[E[Π1_{B_u} | U_0]]. ∎
**Theorem SPLIT.** For λ > 0 let D_u(τ, λ) := {U_0 : p_u(U_0) > e^{-λ}} (a fine-field event in R_u) and
  Θ^W_k(τ, λ) := max over 2-grid offsets and patterns of P_W(∩_{u∈𝒢}D_u(τ, λ))^{1/|𝒢|}.
Then (i) Θ_k(τ) ≤ e^{-λ} + Θ^W_k(τ, λ), and (ii) Θ^W_k(τ, λ) ≤ e^{λ}Θ_k(τ). Consequently, for every a' > 0:
(PLD-dis)_k with (a_d, C_d, p_d) ⇒ Θ^W_k(τ, a'τ²/g_k²) ≤ C_dg_k^{-p_d}e^{-(a_d-a')τ²/g_k²}; and conversely
Θ^W_k(τ, a'τ²/g_k²) ≤ C_Wg_k^{-p_W}e^{-a_Wτ²/g_k²} for all τ ⇒ (PLD-dis)_k (2-grid part) with a_d = min{a', a_W},
C_dg^{-p_d} = 1 + C_Wg^{-p_W}.
*Proof.* (ii) Π_up_u ≥ e^{-λ|𝒢|}Π_u1_{D_u}; take E_W (Lemma CONE) and the |𝒢|-th root. (i) p_u ≤ e^{-λ} + 1_{D_u}, so
Π_up_u ≤ Σ_{S⊂𝒢}e^{-λ|𝒢∖S|}Π_{u∈S}1_{D_u}. The boxes R_u form a grid of the fine torus with boundaries on fine link
mid-planes, 2L^{M+K-k} (even) boxes per direction; X-LRP gives RP of P_W for these planes, and Lemma CBE with f_u := 1_{D_u}
(u ∈ S), 1 otherwise (the canonical copies of 1_{D_u} are the 1_{D_s} by covariance) gives P_W(∩_{u∈S}D_u) ≤ Θ^W_k^{|S|}.
Summing: E_W[Π_up_u] ≤ (e^{-λ} + Θ^W_k)^{|𝒢|}. ∎
*Remarks.* (1) No soft-chain RP (X-RP^S) is used: after Lemma CONE only the Wilson measure's RP enters. (2) For ω_G only
(i) is claimed: 1_{G_k} ≤ Π_u1_{G(u)} (G(u): the level-k cubes inside the super-block u good; cubes in no u dropped), and the
same proof with p^G_u := P_K(G(u) ∩ B_u | U_0) and super-block grids gives Θ^G_k(τ) ≤ e^{-λ} + Θ^{W,G}_k(τ, λ). (3) What this
does: route (b) made exact. The kernel noise and the soft averaging enter only through the definition of the fine-field
events D_u; the dissemination (all copies at once) is priced by the Wilson measure's own chessboard estimate.

## 14.3 Proposition NH-WH (the noise half and the Wilson half; an equivalence modulo the noise half): PROVEN-HERE | SPLIT
Let φ_u(U_0) := E_K[X_u | U_0] (the noise-smoothed block plaquette; the soft analogue of F̃ = E[F | U_0] of X-KER^S).
- **(NH)_k (noise half; HYPOTHESIS for SU(N)).** There are a_N > 0, C_N such that for every fine field U_0 and
  τ ∈ (0, ε_1]: P_K(X_u - φ_u(U_0) ≥ τ/2 | U_0) ≤ C_Ne^{-a_Nτ²/g_k²}.
- **(WH)_k (Wilson half; HYPOTHESIS).** Θ^W_φ(τ) := max P_W(∩_{u∈𝒢}{φ_u ≥ τ/2})^{1/|𝒢|} ≤ C_Wg_k^{-p_W}e^{-a_Wτ²/g_k²},
  τ ∈ (0, ε_1].
*Claim.* (a) (NH)_k + (WH)_k ⇒ (PLD-dis)_k (2-grid part) with a_d = min{a_N, a_W}, C_dg^{-p_d} = C_N + C_Wg^{-p_W}.
(b) (PLD-dis)_k ⇒ (WH)_k with a_W = a_d/16, p_W = p_d + 1, C_W = 16e^{a_d/16}max{C_d, 1} (g_k ≤ 1). No (NH) is needed for (b).
[RPLD-fix, cosmetic: D_u is defined with a strict ">", so the inclusion below uses λ = log(16/τ) (P ≥ τ/8 > τ/16), and the
constants 8 become 16; session 2 had log(8/τ) and 8.]
*Proof.* (a) On {φ_u < τ/2}: p_u = P(X_u ≥ τ | U_0) ≤ P(X_u - φ_u ≥ τ/2 | U_0) ≤ C_Ne^{-a_Nτ²/g²} =: ε. So
p_u ≤ ε + 1{φ_u ≥ τ/2}; expand and apply CBE as in SPLIT (i). (b) X_u ≤ 2, so φ_u ≤ τ/4 + 2P(X_u ≥ τ/4 | U_0); on
{φ_u ≥ τ/2}, P(X_u ≥ τ/4 | U_0) ≥ τ/8 > τ/16, i.e. {φ_u ≥ τ/2} ⊂ D_u(τ/4, log(16/τ)). SPLIT (ii): Θ^W_φ(τ) ≤ (16/τ)Θ_k(τ/4) ≤
(16/τ)C_dg^{-p_d}e^{-a_dτ²/(16g²)}. For τ ≥ g this is ≤ 16C_dg^{-p_d-1}e^{-a_dτ²/(16g²)}; for τ < g the stated right side is
≥ 16max{C_d, 1}g^{-p_d-1} ≥ 1. ∎ [RPLD-fix: 8 → 16, log(8/τ) → log(16/τ).]
**So, given (NH)_k, (PLD-dis)_k ⟺ (WH)_k** (exponent changed by at most a factor 16, prefactor by g^{-1}). (NH) concerns the
conditional law given the fine field (no Wilson measure); (WH) concerns the Wilson measure only, for one explicit
fine-field functional. By 14.1 and (b), (WH)_k contains the AF upper bound.
**Linear soft chain (model; PROVEN-HERE | PLD-lin).** In model (LS) of §7 with X_u := |F_k(q_u)| (HS norm over the N² - 1
copies), F_k = G + η with G := M^{(k)}F_0 a function of B_0 and η := Σ_idQ_root^{k-1-i}ξ_i independent of B_0, centred
Gaussian with ||Cov η||_op ≤ σ_η² := 16Σ_is_i²L^{-2(k-1-i)} ≤ 18Ng_k²/κ (§7 step (4), (6)). Jensen: φ_u ≥ |G + Eη| = |G|, so
X_u - φ_u ≤ |η|, and §7 step (5) with one plaquette gives P(|η| ≥ τ/2) ≤ 2^{(N²-1)/2}e^{-τ²/(16σ_η²)}: **(NH)_k holds in
the model with a_N = κ/(288N), C_N = 2^{(N²-1)/2}**, uniformly in k. (WH)_k also holds in the model: φ_u ≤ |G| + E|η|, and
for τ ≥ 4E|η| the event {φ_u ≥ τ/2} lies in {|G| ≥ τ/4}, which §7 step (5) applied to G (covariance ≤ Ng_0² ≤ Ng_k² on the
copies, no disjointness needed) prices at (2^{(N²-1)/2}e^{-τ²/(64Ng_k²)})^{|𝒢|}; for τ < 4E|η| ≤ 4((N² - 1)σ_η²)^{1/2} the
bound holds after enlarging C_W by the g-independent factor e^{a_W·288N(N²-1)/κ}. (The model has no running; §7 (3).)
**SU(N): what (NH) needs (ARGUED; inputs named).** (NH-i) per-kernel sub-Gaussianity of the injected deviation given the
past (SU(2): the central law μ_t of Lemma NA-1 (c), t = κ|M̄|/g²; its angle has density ∝ sin²θe^{-t(1-cos θ)} and
1 - cos θ ≥ 2θ²/π², so it is sub-Gaussian at scale t^{-1/2}; N ≥ 3: the kernel is not central, NA-1 remark); (NH-ii) a
synchronous-coupling Lipschitz bound of X_u in the level-j injections with ℓ²-weight ≤ Cρ^{k-1-j}, ρ < 1: the non-linear
form of ||dQ_str^m|| ≤ 4L^{-m} modulo gauge (root covariance maps exact gauge directions to exact gauge directions and
X_u is gauge invariant, so only the straight part, of norm L^{-1}, and O(ε) background corrections remain); (NH-iii) the
same bound across rough spots of the background, which the next proposition shows cannot be excluded.

**Proposition ROUGH (the fine background in a deep cone is not small-field): PROVEN-HERE | Wilson measure, Haar invariance.**
For ε ∈ (0, 1] and every fine plaquette p: P_W(||1 - U_0(p)||_op ≥ ε) ≥ ½e^{-12ε/g_0²}. Hence the expected number of fine
plaquettes with ||1 - U_0(p)|| ≥ ε in the fine block of one level-k site is ≥ 3L^{4k}e^{-12ε/g_0²}, and under the upper
half of (F) (1/g_0² ≤ 1/g_k² + β_+k log L) it is ≥ 3e^{-12ε/g_k²}L^{(4-12εβ_+)k}, which → ∞ as k → ∞ at fixed g_k whenever
ε < 1/(3β_+) (e.g. ε < 0.89 at β_+ = β_1 for SU(2), ε < 0.39 for SU(3)).
*Proof.* Fix a link b of p and R ∈ SU(N) with ||1 - R||_op = 2ε; T: U_0(b) ↦ U_0(b)R preserves Haar. Each of the 6
plaquettes containing b changes its action term by ≤ g_0^{-2}N^{-1}|Re tr(A(R' - 1))| ≤ 2ε/g_0² (A unitary, R' a conjugate
of R^{±1}), so dP_W∘T ≥ e^{-12ε/g_0²}dP_W. If ||1 - U_0(p)|| < ε then ||1 - (TU_0)(p)|| > 2ε - ε, so T maps F^c into F,
F := {||1 - U_0(p)|| ≥ ε}; hence P_W(F) ≥ e^{-12ε/g_0²}(1 - P_W(F)). A level-k site's fine block has 6L^{4k} plaquettes. ∎
(The constant 12 is crude, the threshold linear in ε; the point is the exponent's coefficient of k.)
*Consequence.* Any proof of (NH) that conditions on "every fine plaquette in the cone is below ε" pays a union bound
whose expectation is ≥ 3e^{-12ε/g_k²}L^{(4-12εβ_+)k}: it diverges with the depth. The chessboard estimate prices
intersections, not unions, so it does not help here. (NH-iii) is therefore exactly the weighted influence bound through
rough spots that EXISTENCE (NA-R2) names ("a large field at one ancestor link enters the block plaquette with an
influence weight O(L^{-3n})"; GS-2 (a): coefficient ≤ s^{-3}, s = L^n): an influence bound for the polar averages that
holds at every background, not only small-field ones, uniformly in the depth. OPEN.

## 14.4 Route (a): the exact loss terms (W-F2)
**Proposition LD-arith: PROVEN-HERE (arithmetic) | (F).** Consider any recursion of the PLD-step form
Θ_k(t) ≤ w_{k-1}(t) + nΘ_{k-1}(ct) with w_i(t), Θ_0(t) ≤ Be^{-αt²/g_i²} (n ≥ 1, c ∈ (0, 1]). Its iterate is
  Σ_{m<k}n^mBe^{-αc^{2m}t²/g_{k-1-m}²} + n^kBe^{-αc^{2k}t²/g_0²}.
(i) If c < 1 the iterate is not bounded uniformly in k: by the upper half of (F) the m-th term is
≥ n^mB·exp(-αc^{2m}t²(1/g_k² + β_+(m + 1)log L)), and c^{2m}(m + 1) → 0, so the terms tend to infinity with m (n ≥ 2) or
stay ≥ Be^{-o(1)} (n = 1).
(ii) If c = 1, the m-th term is ≤ Be^{-αt²/g_k²}(nL^{-αt²β_-})^{m+1}/n, so the iterate is ≤ Be^{-αt²/g_k²}/(n(1 - nL^{-αt²β_-}))
uniformly in k iff αt²β_- log L > log n (and it diverges if αt²β_+ log L < log n). For PLD-step n = n_U = 24L⁴, so
log n_U/log L = 4 + log 24/log L = 6.893 at L = 3. **[RPLD-fix F-9; session 1-2 text: "With α ≤ 1/(2N) (inequality (B)
is attained) … only for N ≥ 38 … and at the thresholds actually used (η_1, η_♭ ≤ ε_1/4) for no N"; corrected.]**
Inequality (B) gives the exponent 1/(2N) as a lower bound only; it is NOT attained in SU(N) at finite N (det = 1 forces at
least two eigenvalues to move): for SU(2), s = ||1 - U||²_op/2, twice (B); in general the minimal s at given operator norm
is ≈ ||1 - U||²_op/(2(N - 1)), so the sharp bare exponent is α ≈ 1/(2(N - 1)) (1/N for SU(2)). With α = 1/(2(N - 1)),
t ≤ 2 and β_- ≤ β_1, αt²β_- ≤ 11N²/(6π²(N - 1)) = 0.1858N²/(N - 1), which exceeds 6.893 iff N ≥ 37. At the thresholds used,
t ≤ ε_1/4 ≤ ½: αt²β_1 ≤ 11N²/(96π²(N - 1)) ≈ 0.0116N, which exceeds 6.893 only for N ≥ 593 (N ≥ 594 with α = 1/(2N)); at t = η_1 = c_1ε_1 ≤ 2/117
only for N ≥ 507954 (check p3 C2). So: not for N below these values, i.e. not uniformly in N, and in
particular not for SU(2), SU(3). The conclusion for those groups stands: even a transfer with no threshold loss would not
be summable for single-plaquette descent, **so route (a)'s answer to the LF-count question is no for SU(2), SU(3)** (the
per-level entropy L⁴ beats the flow's suppression L^{-αt²β}, as in LF-count's single-cube case).
[RPLD-fix, counting: LD-arith and Proposition GR are arithmetic (RLARGE §8.4's precedent); the counted item is Lemma LC.]
**Lemma LC (linear cost transfer; the c_1 loss is not a property of the linearised measure): PROVEN-HERE | Q_str, Stokes.**
In own units, for a level-(k-1) abelian 1-form A and a level-k plaquette P = (X; μ, ν):
  (dQ_strA)(P) = Σ_qw_P(q)(dA)(q),  w_P(q) = L^{-4}m(z_μ)m(z_ν),  m(t) := min(t + 1, 2L - 1 - t),
q running over the level-(k-1) plaquettes of orientation (μ, ν) with base point z = LX + (z_μ, z_ν, z_⊥),
0 ≤ z_μ, z_ν ≤ 2L - 2, z_⊥ ∈ [0, L)². Σ_qw_P(q) = L² and ||w_P||² = (2L² + 1)²/(9L⁴) (= 361/729 = 0.4952 at L = 3). Hence
  min{||F||² : F ∈ im d, (MF)(P) = τ} = τ²/||Πw_P||² ≥ 9L⁴τ²/(2L² + 1)² (= 2.019τ² at L = 3).
*Proof.* (Q_strA)(X, μ) = L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ) (§7 (2)); pairing y ∈ B(X) with y + Le_μ ∈ B(X + e_μ) and
y + Le_ν ∈ B(X + e_ν), (dQ_strA)(P) = L^{-4}Σ_{y∈B(X)}(line integral of A around the L × L square with corner y in the
(μ, ν)-plane) = L^{-4}Σ_y Σ_{q in that square}(dA)(q) (Stokes). A plaquette q with base z lies in the square of y iff
y_μ ≤ z_μ ≤ y_μ + L - 1, the same for ν, and y_⊥ = z_⊥: m(z_μ)m(z_ν) choices. Sums: Σ_tm(t) = L², Σ_tm(t)² = L(2L² + 1)/3,
times L² transverse positions and L^{-4} resp. L^{-8}. Minimum: τ = ⟨w_P, F⟩ = ⟨Πw_P, F⟩ ≤ ||Πw_P|| ||F|| for F ∈ im d, with
equality at F ∝ Πw_P. ∎ (Check p2 A: identity to 1.3e-15 on T = 2, 3, sums exact. p2 B, informational: ||Πw_P||² =
0.144 (T = 2), 0.181 (T = 3), i.e. the minimal fine cost is 7.0τ², 5.5τ² on these tori.)
*Reading.* PLD-step prices a level-k deviation at threshold t by a level-(k-1) deviation at c_1t, i.e. at quadratic cost
c_1²t² (117² ≈ 1.4·10⁴ times cheaper). In the linearised measure-transfer an isolated level-k deviation costs at least
2.02 times MORE one level down. So the geometric exponent loss of §5 is entirely the pointwise (max-norm) transfer, (R1)-(R2)
evaluated on the worst coherent configuration, not a property of the measure. Smooth (constant-curvature) deviations are
cost-preserving exactly (d = 4 marginality: L⁴ plaquettes of size τ/L² cost τ²); isolated ones gain. What remains is the
non-linear correction to the transfer, which must be summable over levels: §14.5.

## 14.5 Proposition GR (the marginal direction: the precise loss term): PROVEN-HERE (arithmetic) | (F)
*Claim.* Let v_0, …, v_k ≥ 0 (think: the variance of a smooth block-curvature functional in the Wilson half) with
v_0 ≤ Ag_0² and v_{j+1} ≤ (1 + cg_j²)v_j, c ≥ 0. Put θ := c/(β_- log L). Under the lower half of (F):
  v_k ≤ Ag_k²·(g_k²/g_0²)^{θ-1},  g_k²/g_0² ≥ 1 + β_-k log L·g_k².
So the bound is uniform in k (v_k ≤ Ag_k²) iff θ ≤ 1. Conversely, if v_{j+1} ≥ (1 + cg_j²)v_j and v_0 ≥ A'g_0², then under the
upper half of (F) and with θ_+ := c/(β_+ log L):
  v_k ≥ A'g_k²·e^{-c²g_k²/(2β_- log L)}·((1 + β_+(k + 1)log L·g_k²)/(1 + β_+ log L·g_k²))^{θ_+}/(1 + β_+k log L·g_k²),
which → ∞ as k → ∞ at fixed g_k if θ_+ > 1. If instead the recursion is relative to the sequence,
v_{j+1}/g_{j+1}² ≤ (1 + δ_j)v_j/g_j², then v_k ≤ (v_0/g_0²)g_k²Π_j(1 + δ_j): uniform iff Σ_jδ_j < ∞; δ_j = O(g_j⁴) suffices,
since Σ_{j<k}g_j⁴ ≤ g_k²/(β_- log L).
*Proof.* Π_{j<k}(1 + cg_j²) ≤ exp(cΣ_{j<k}g_j²) and, with n := k - j ∈ [1, k] and 1/g_j² ≥ 1/g_k² + β_-n log L,
Σ_{j<k}g_j² ≤ ∫_0^k dn/(1/g_k² + β_-n log L) = (β_- log L)^{-1}log(1 + β_-k log L·g_k²) ≤ (β_- log L)^{-1}log(g_k²/g_0²)
(the last step is (F) at j = 0). So v_k ≤ Ag_0²(g_k²/g_0²)^θ. Lower bound: log(1 + x) ≥ x - x²/2,
Σg_j² ≥ ∫_1^{k+1}dn/(1/g_k² + β_+n log L), Σg_j⁴ ≤ ∫_0^∞dn/(1/g_k² + β_-n log L)² = g_k²/(β_- log L), and
g_0² ≥ g_k²/(1 + β_+k log L·g_k²). The relative form is the same telescoping. ∎ (Check p2 C: the upper bound holds in
all 90 cases; at θ = 1/2, 1 R_k := g_0²Π/g_k² ≤ 1 (θ = 1: 0.984, 0.938 at k = 10⁵); at θ = 3/2 R_k grows as predicted,
R(10⁵)/R(10⁴) = 3.153 against 3.154.)
*Reading (the precise loss term of every route that propagates a Gaussian bound level by level).* A per-level variance
growth (1 + cg_j²) in the marginal direction costs the factor (g_k²/g_0²)^{c/(β_- log L) - 1} ≈ (1 + β_-k log L·g_k²)^{θ-1}: a
POWER of the depth, not a geometric factor. Uniformity needs c ≤ β_- log L. The true per-level growth of the block-plaquette
scale is the flow itself (c_true = β_1 log L at one loop, ARGUED). With a bracket β_- ≤ β_1 ≤ β_+ (A5's form) the condition
c_true ≤ β_- log L forces β_- = β_1 to leading order; with the sequence defined by the flow, the relative form needs
Σδ_j < ∞, i.e. the per-level growth must match the sequence's own increment to O(g_j⁴). Either way the proof must
compute the one-loop coefficient of the block-plaquette variance growth sharply (as an upper bound): this is W-AF1
(EXISTENCE l.825, "β = β' = 2b_0 log L + o(1)") in the form the Wilson half needs, with an O(g²)-relative error allowed per
level only if it is summable.

## 14.6 Route (c) and the location of the wall (ARGUED, uncounted)
- **Brascamp-Lieb / log-Sobolev.** For the fine Wilson measure in a small-field chart, any BL or LSI constant valid on a
  whole cone gives fluctuations of φ_u at the scale g_0²·||Π(M^{(k)})^Te_P||² (the free value, PLD-lin step (3)): no
  running. By 14.1 and one-loop this is too small for SU(N) at large k, so the non-convexity of the Wilson action (which
  produces the running) must defeat any uniform convexity constant; for the level-k marginal itself, a BL bound needs
  uniform convexity of S_k at scale 1/g_k² in a chart, i.e. node A. Route (c) relocates the wall to node A; it does not
  remove it.
- **Where the wall now sits (exact).** (PLD-dis)_k ⟺ (WH)_k modulo (NH)_k (14.3); (NH)_k is uniform in the linear model and
  reduces for SU(N) to (NH-i)-(NH-iii), of which (NH-iii) (influence through rough spots, uniform in depth) is the OPEN core
  (= EXISTENCE's (NA-R2) influence bound); (WH)_k is a Wilson-measure LD statement at scale g_k for the noise-smoothed block
  plaquette, which contains the AF upper bound (14.1), and whose level-by-level proof must have the sharp one-loop
  coefficient (14.5); the large-deviation range τ ∈ [g_kp(g_k), ε_1] costs nothing extra in the linearised transfer
  (Lemma LC), and the non-linear corrections there are expected to be geometric in the levels (a deviation of size τ at
  level k is carried coherently only by the last O(log(τ/g_k)/log L) levels, where corrections are O(τL^{-2m})): ARGUED,
  not written.

## 14.7 Check p2 (criteria first: checks/p2_criteria.md; script checks/p2_pld.py; output checks/p2_out.txt; record checks/p2_time.txt)
**All parts PASS, first and only run** (0.6 s, peak RSS 80 MB, load 3.1, 48% memory free, numeric lock, nice 10,
threads 1; python3 without -I, user-site numpy; no external files).
- A: dQ_strA = ⟨w, dA⟩ to 1.3e-15 (T = 2, 3, 3 seeds, 6 orientations); Σw = 9, Σw² = 361/729 exact to 1e-15.
- B: ||Πw||² = 0.1435 (T = 2), 0.1812 (T = 3) ≤ 0.4952; CG residual ≤ 8e-14.
- C: Proposition GR's upper bound in all cases; uniform for θ ≤ 1; growth exponent at θ = 3/2 as predicted (3.153 vs 3.154).
- D: β_1 = 0.37151 (SU(2)), 0.83590 (SU(3)); n_* = 382, 255 reproduced; log(24L⁴)/log L = 6.8928. Disclosed: the
  informational "smallest N" item carried a spurious factor 4 (criteria and script alike); corrected post-run value
  N ≥ 38 (p2_time.txt); the PASS condition is unaffected.
- E: tail-integration closed form dominates in all 18 cases.
Scope: p2 tests the linear block map and arithmetic only; it tests nothing about SU(N), Lemma CONE, SPLIT or ROUGH.

## 14.8 Outcome against the pre-stated targets (§14.0)
- **T4: PARTIAL SUCCESS as pre-stated, with (W-F1), (W-F2), (W-F3) all met.** Not proven: (PLD-dis)_k uniformly for SU(N).
  Proven: (1) **SPLIT** — (PLD-dis)_k is equivalent (exponents up to any a' < a) to a disseminated LD bound for the fine
  Wilson measure alone, for the events D_u; the dissemination is priced by the Wilson measure's chessboard estimate, with
  no soft-chain RP needed (Lemma CONE). (2) **NH-WH** — given the noise half (NH)_k, (PLD-dis)_k ⟺ (WH)_k (a two-sided
  implication), so the wall is located, not renamed; (NH)_k holds uniformly in the linear soft chain (a_N = κ/(288N)).
  (3) **PLD-AF** (W-F1) — (PLD-dis)_k contains the AF upper bound E s(U_k(P)) ≤ Cg_k²log(1/g_k); the coupling quantifier must
  be the soft chain's own effective sequence (W-F3; ARGUED via one-loop). (4) **ROUGH** — the deep fine background is not
  small-field (expected rough count ≥ 3e^{-12ε/g_k²}L^{(4-12εβ_+)k}), so (NH) needs an influence bound through rough spots
  (= (NA-R2)). (5) Loss terms (W-F2): threshold-transfer recursion non-uniform for c < 1 and, even lossless, summable only
  if αt²β_- log L > log(24L⁴) (never at the used thresholds); the c_1² loss is the max-norm transfer only (Lemma LC: the
  linear measure-transfer gains ≥ 2.02 per isolated level); the marginal-direction loss of a level-by-level Gaussian
  propagation is (g_k²/g_0²)^{c/(β_- log L)-1}, uniform iff the per-level growth coefficient is ≤ β_- log L (Proposition GR),
  i.e. W-AF1's sharp coefficient as an upper bound.
- **T5: MET.** p2, criteria first, all PASS; one informational arithmetic slip disclosed.
- Not-success items avoided: no union bound used as a product bound (ROUGH is used only to show a union bound fails); no
  constant depends on k or the volume except where said (PLD-fin, Proposition GR's displayed loss); (F) is used only
  through its lower/upper bracket, each use named; node A, (SF), (DF), RLF are not used.

## 14.9 Proposed changes for the owners of other files (not made here) and status
1. **(PLD-dis) quantifier (this file §6, RLARGE §8.2, EXISTENCE §13.6 (PLD^mod_dis)):** replace "uniformly in the coupling
   sequence within (F)" by "for the soft chain's effective coupling sequence (node A5), or for sequences in (F) whose lower
   rate is ≥ the soft chain's own one-loop rate" (14.1 (W-F3)). [RPLD-fix B6: this applies to RLF and (RLF-3^dis) too;
   §15.6 E1.]
2. **EXISTENCE (NA-R2) and this file's (NH-iii)** are the same missing estimate (a depth-uniform influence bound for the
   polar averages through rough spots); proposed to be tracked as one item. [Session 3: merged statement (INF), §15.5.]
3. **EXISTENCE's AF upper bound / W-AF2:** (WH)_k (14.3) is a precise Wilson-measure form of it with Gaussian tails, and by
   14.3 (b) it is implied by (PLD-dis)_k; proposed to be listed as the Wilson half of (PLD).
- **PROVEN-HERE [E2], counted (5, unreviewed):** Proposition PLD-AF; Lemma CONE with Theorem SPLIT (one item); Proposition
  NH-WH (with its linear-model instance); Proposition ROUGH; Lemma LC with Propositions LD-arith and GR (one item:
  the loss-term arithmetic).
- **New named hypotheses:** (NH)_k (noise half; inputs (NH-i)-(NH-iii)), (WH)_k (Wilson half). (PLD-dis)_k is now
  "(NH)_k + (WH)_k", with (WH)_k ⟸ (PLD-dis)_k.
- **ARGUED (uncounted):** the one-loop consistency reading (W-F3); the (NH) route (NH-i)-(NH-ii); route (c)'s relocation to
  node A; the coherent-descent picture for τ ∈ [g p(g), ε_1].
- **Tally proposal:** +5 PROVEN-HERE (unreviewed), 0 OPEN items closed, 0 new top-level OPEN items ((NH), (WH) sit inside
  (PLD-dis), which sits inside RLF-step).

---
# Session 3 (2026-10-28, lane E)

Inputs read this session (read-only): REVIEW_PLD_S1_S2.md in full [read]; this file §0-§14.9 in full [read]; PLD_LOG
[read]; RLARGE.md §0 (l.40-56), §1A (l.95-150), §4 head (l.210-242), §8.1-§8.5 (l.564-696) [read]; HIST.md §6 (l.302-376),
§8 (l.529-565) [read]; REVIEW_HIST_S1.md l.206-259, l.455-469 (CF verdict, fix H-2, (I_k^E)) [read]; PROOF.md S19 block
l.5200-5392 (Lemma N5-an, CT♯, Theorem RW, Corollary RW-triv, Theorem N5-sf0, Proposition N5-sf_i) and l.3405-3420
((NA-H)) [read]; EXISTENCE.md l.1530-1540 ((RLF-3^dis)), l.2100-2145 (Theorem NA-GS1 end, bias verdict, (NA-R2)),
l.2244-2258 ((H-lin^S)) [read].

## 15.0 Targets (pre-stated 2026-10-28 00:15 UTC, after reading the review and the inputs above and after an unwritten
exploratory pass that chose them; before any written session-3 derivation and before checks/p3_criteria.md)

**T6 (binding fixes).** Apply REVIEW_PLD_S1_S2's B1-B4 and the PLD-owned parts of B6-B9, each tagged [RPLD-fix], in place
where the text is wrong and summarised in §15.1; withdraw the three overclaims; state the proposed (F)-quantifier
amendment for RLARGE and EXISTENCE without editing them; append an honest process-gap correction to PLD_LOG (no history
rewritten). **Success:** every item of the review's "Binding fixes" list that PLD owns is applied or explicitly routed.

**T7 (architecture: (PLD)_k as an output of RLF-step).** (a) State (SG)_k on the per-history measure (M3) precisely
(measure, sets, quantifiers, constants), and list which layer-1 inputs ((I_k^E), (SF)_k, N5-sf0 / Theorem RW, (NA-H_loc))
are meant to give it and what each gives. (b) Prove (SG)_k ⇒ (PLD)_k (i)-(ii) on (M3), with explicit constants, using no
reflection positivity. (c) Attempt (SG)_k at levels 0 and 1. (d) State one merged estimate replacing (NH-iii) and (NA-R2).
- **Success:** (b) PROVEN-HERE with constants; (a) and (d) stated with all quantifiers; (c) PROVEN at level 0 from N5-sf0
  plus named standard inputs, and level 1 reduced to (NA-H_loc).
- **Partial success:** (b) PROVEN; (c) reduced to named statements with the missing step for each level identified.
- **Valid failure outcomes:** (SG-F1) (SG)_k in the stated form is not an in-step output of level-k inputs (named reason,
  with the part that is); (SG-F2) N5-sf0 does not give (SG)_0 by itself (the missing step named); (SG-F3) a quantifier of
  (SG)_k must change for consistency (named).
- **Not success:** a Gaussian covariance bound presented as an exponential-moment bound; any use of RP on (M3); any
  constant depending on K, k, the torus or the history.

**T8 (check p3; criteria file checks/p3_criteria.md before checks/p3_*.py).** Test the new elementary statements
numerically: the su(N)-valued logarithm, the net/Gaussian bounds of T7 (b) against exact probabilities in a model with a
negative control, and the corrected arithmetic of T6.

# Session 3 derivations (written after §15.0 and after the in-place fixes; before checks/p3_criteria.md)

## 15.1 T6: the fixes, and Lemma TL

**Where each binding item went** (all tagged [RPLD-fix] in place):
| Item | Place | Change |
|---|---|---|
| P-1 | header (Inputs) | X-RP^S, CBE, KN, KN-step, CB were reviewed by REVIEW_X3_X4 |
| F-1 | §5.2 | polynomial 1/g_0 factor of PLD-fin stated and absorbed at fixed k |
| F-2 | §5.3 | β_- → β_+ (a lower bound on the m-th term needs (F)'s upper half) |
| F-3 | §5.3 | "no 1/g² per link" is "from 𝒩"; the kernel numerator still changes |
| F-4 | §6 (SG), Lemma HS | F_p := TL(U_p), su(N)-valued (Lemma TL below) |
| F-5 | §6 PLD-red (iii), §7 | (SG)_k + (SG)_k^{full} ⇒ (PLD-dis)_k (both halves) |
| B2 | §6 Remark (1), §11 | "correction" of RLARGE §8.2 withdrawn; narrowed |
| F-6 | §9.1 | SHADOW comparison via (F)'s upper half; condition (2n_c + 1)⁴a > 3κε_♮ |
| F-7 | §9.1 | the bridge: nonnegative history weights / Z = cut-law probability |
| B4 | §9.1, §9.4, §12 item 3 | "R1 (i) needs no (H-ch)" withdrawn; σ-restricted gas + collar-bad family in (SC)_k |
| F-8 | §9.3 | locality of A_x is a hypothesis (supplied by (SC1)); GT-lat' (ii) clause cited; typo |
| W1R | §9.4 | (SC)_k is close in strength to (W1-ret') (a)-(b); W1R proves bookkeeping |
| B3 | session-2 heading, PLD_LOG | ordering and timestamps corrected by an appended note |
| F-9 | §14.4 | (B) not attained; N ≥ 37; "for no N" → not uniformly in N; LD-arith, GR uncounted |
| B6 | §6, §14.1, §14.9 | (F)-quantifier amendment; reaches RLF and (RLF-3^dis): §15.6 E1 |
| cosmetic | §14.3 (b) | D_u strict: log(16/τ), constants 16 |
| B5, B7, B8, B9 | §15.6 | routed to RLARGE / EXISTENCE as proposed edits |

**Lemma TL (an su(N)-valued logarithm): PROVEN-HERE (elementary; used by fix F-4; not counted).** There is a Borel map
TL: SU(N) → su(N) with (i) e^{TL(U)} = U and tr TL(U) = 0; (ii) ||TL(U)||_op ≤ 3π; (iii) ||1 - U||_op ≤ ||1 - U||_HS ≤
|TL(U)|_HS; (iv) TL(U) = log U (principal) on the open set O_N := {||1 - U||_op < 2 sin(π/N)}, where TL is continuous,
Ad-covariant and odd (TL(U^{-1}) = -TL(U)).
*Proof.* Write U = W diag(e^{iθ_1}, …, e^{iθ_N})W^*, θ_j ∈ (-π, π]. det U = 1 gives Σθ_j = 2πm with m ∈ Z, |m| ≤ N/2. If m > 0
replace the m largest θ_j by θ_j - 2π ∈ (-3π, -π]; if m < 0 replace the |m| smallest by θ_j + 2π ∈ (π, 3π); call the result θ'.
Then Σθ'_j = 0 and X := W diag(iθ')W^* ∈ su(N) has e^X = U, ||X||_op ≤ 3π. So the set Γ(U) := {X ∈ su(N) : e^X = U,
||X||_op ≤ 3π} is nonempty and compact, and its graph is closed (exp is continuous); a closed-graph correspondence into a
compact metric space is upper hemicontinuous, hence weakly measurable, and the Kuratowski-Ryll-Nardzewski theorem
[STANDARD] gives a Borel selection X(U) ∈ Γ(U). On O_N every |θ_j| = 2arcsin(||1 - e^{iθ_j}||/2) < 2π/N, so |Σθ_j| < 2π and
m = 0: the principal logarithm is in Γ(U), and it is continuous, Ad-covariant and odd there. Put TL := principal log on
O_N and TL := X off O_N (Borel, O_N open). (iii): eigenvalue-wise |1 - e^{iθ'_j}| = 2|sin(θ'_j/2)| ≤ |θ'_j|, and ||·||_op ≤
||·||_HS. ∎ (Check p3 A: central elements, -1 ∈ SU(2), near-central and Haar samples for N = 2, 3, 4; the principal log's
trace at central elements is 2πim ≠ 0, the negative control.)

## 15.2 T7 (a): the per-history measure, (SG)_k stated precisely, and what each input gives

**The measures (made precise).** Fix level k, a history 𝔥 ∈ ℋ_k and the exterior data ω (every variable of the (I_k)
summand of 𝔥 other than the level-k links of Λ(𝔥)). Write w_𝔥(U; ω) ≥ 0 for that summand as a function of the level-k
links U of Λ(𝔥) (nonnegative by fix F-7: an integral of e^{-S}·indicators).
- (M3) **per-history law:** μ_{𝔥,ω}(dU) := Z_{𝔥,ω}^{-1}1_{G_k(Λ(𝔥))}(U)w_𝔥(U; ω)dU (every level-k cube of Λ(𝔥) good).
- (M3^+) **stage-k joint law (RS ordering, before the level-(k+1) indicators are inserted):** μ^+_{𝔥,ω}(dU dV) :=
  μ_{𝔥,ω}(dU)K_k(V, U)dV, V the level-(k+1) links whose contours lie in Λ(𝔥). Given U, the links of V are independent (product
  kernel). Events in U alone have the same probability under μ^+ and μ.
- **Interior sets.** 𝒫°(𝔥): level-k plaquettes with all four links in Λ(𝔥). 𝒬°(𝔥): level-k cubes Q with N_1(Q) ⊂ Λ(𝔥) (then
  the contours of C(Q) lie in Λ(𝔥) too). Plaquettes and cubes near ∂Λ(𝔥) are (HIST)'s boundary terms (e^{B_0} per boundary
  cube), not (PLD)'s.
- X_p := TL(U_p) (Lemma TL); |s|² := Σ|s_p|²_HS, |s|_1 := Σ|s_p|_HS.

**(SG^{ph})_k (per-history Gaussian concentration; HYPOTHESIS).** There are σ_*, m_* < ∞, independent of K, k, the torus, 𝔥, ω
and the coupling sequence (the chain's own, §15.6 E1), such that for all finite A ⊂ 𝒫°(𝔥) and all s ∈ su(N)^A:
  E_{μ_{𝔥,ω}}exp(Σ_{p∈A}⟨s_p, X_p⟩_HS) ≤ exp(½σ_*²g_k²|s|² + m_*g_k|s|_1).
**(SG^{net})_k (the form RLF-step consumes; weaker).** The same inequality only for s_p = t·u_p with |u_p|_HS = 1 and
0 ≤ t ≤ ε_1/(σ_*²g_k²).
**(SG^{fl})_k (fixed-V fluctuation form; HYPOTHESIS, a clause of (SF)_k's output).** There are a measurable background map
V ↦ 𝔟(V) (a level-k field on Λ(𝔥), given ω) and σ_fl, m_fl (uniform as above) such that, with Y_p := X_p(U) - X_p(𝔟(V)) ∈ su(N),
for every finite A ⊂ 𝒫°(𝔥), every V ∈ 𝒱^{sf}(A) := {every level-(k+1) plaquette within level-(k+1) distance R_bg of A has ||1 - V_P||_op < ε_1} (R_bg the
localisation radius of 𝔟 in (BG)_k)
(a cut-good neighbourhood; all plaquettes, not only cube-interior ones), every unit (u_p) and 0 ≤ t ≤ ε_1/(σ_fl²g_k²):
  E_{μ^+}[exp(tΣ_{p∈A}⟨u_p, Y_p⟩) | V] ≤ exp(½σ_fl²g_k²t²|A| + m_flg_kt|A|).

**Finding 1 (SG-F3; the ℓ¹ term is load-bearing). Remark G-IR: exact for Gaussian models; the SU(N) reading ARGUED.**
(1) For a centred Gaussian vector X on su(N)^A, a unit u and e := (u)_{p∈A}, with v := Var⟨e, X⟩/|A| (the per-plaquette
aligned variance): log E e^{t⟨e,X⟩} = ½t²v|A| exactly, so (SG^{net}) with constants (σ_*, m_*) holds at t = ε_1/(σ_*²g²) iff
v ≤ σ_*²g² + 2m_*σ_*²g³/ε_1. Hence no Gaussian model whose aligned variance exceeds σ_*²g²(1 + 2m_*g/ε_1) satisfies (SG^{net}).
(2) [ARGUED, one loop] For SU(N) the aligned variance of a smooth family (all (μ,ν)-plaquettes of a region of side ℓ, in
level-k units) is ≈ g(ℓ)² with 1/g(ℓ)² ≈ 1/g_k² - β_1 log ℓ, which exceeds σ_*²g_k² once β_1g_k²log ℓ > 1 - σ_*^{-2}; on the torus
ℓ reaches L^{K-k}, so this happens for K - k large at fixed g_K (the continuum limit). Then (SG) with m_* = 0 fails for
small amplitudes t (where the Gaussian approximation is right), and (SG) can hold only because (a) the ℓ¹ term absorbs
amplitudes t ≲ 2m_*g_k/(g(ℓ)² - σ_*²g_k²), and (b) at larger t the tilt induces a background curvature ≈ tg² per plaquette,
around which the running is cut off at the field-strength scale (background-field running), so the effective variance is
≈ g_k²(1 + O(g_k²log(1/(tg_k²)))), not g(ℓ)². So (SG) is consistent with AF only through its ℓ¹ term and a non-Gaussian
large-deviation mechanism; and by (1) **no proof of (SG^{net})_k by Gaussian domination with the true two-point function can
work for aligned (smooth) families.** (PLD-lin's linear model has no running, so it does not see this.)

**Finding 2 (SG-F1 MET: (SG^{ph})_k and (SG^{net})_k are not in-step outputs; (SG^{fl})_k is).**
- μ_{𝔥,ω} is an exact projection of the full chain: its density is the level-k marginal, in which every coarser scale is
  present but none is integrated. For aligned s, E exp⟨s, X⟩ is a ratio of two level-k partition functions on Λ(𝔥) and
  contains the remaining K - k levels (Finding 1 (2)). (I_k) + (SF)_k at step k do not control it.
- **Proposition INH below (PROVEN)**: cut-good level-(k+1) fields carry coherent level-k curvature ≥ η_1 = c_1ε_1 with zero
  kernel mismatch. So under μ^+ the size of aligned functionals of U is driven by V, whose law is a level-(k+1) quantity.
- What is in-step is the fixed-V form (SG^{fl})_k: it is a statement about the conditional law of U given V (M4 restricted to
  the history), centred at 𝔟(V), i.e. (DF3') for general linear functionals with ℓ¹ control. It needs nothing about levels
  > k and no RP.

**What each layer-1 input gives (for (SG^{fl})_k).**
| Input | Status | What it gives |
|---|---|---|
| (I_k^E) (REVIEW_HIST_S1 fix H-2: chain-energy main term E_k(U)/g̃_k² + polymers small in a background-field norm) | not yet stated (HIST owner) | w_𝔥 as a bounded perturbation of the chain-energy Gibbs density; fixes 𝔟(V) := the minimiser of E_k + the kernel term given V (background field) |
| Theorem N5-sf0 (level 0), Prop. N5-sf_i ⇐ (NA-H_loc)_i (i ≥ 1) | PROVEN [S19, unreviewed] / OPEN | the fluctuation operator Õ_i(𝔟(V), V) on 𝔑(α_*): invertible, gap λ_min ≥ γ'(1 - ε_R)/(8coth⁴(m/2)), decay, walk expansion, analyticity: the second-order (Gaussian) part of (SG^{fl})_i |
| (SF)_k = (DF1)-(DF4) + Theorem CE | OPEN (node A) | the cluster expansion that turns covariance bounds into exponential moments on the torus-wide fixed-V law |
| (TH) threshold compatibility | definitional (RLARGE §1A R1819-fix 8) | ε_1 ≤ ε_* in matching units, so that 𝒱^{sf} and cut-good U lie in N5's class 𝔑(α_*); soft residual |ρ_c| > ε_* is a kernel-mismatch event (Lemma KN, in-step) |
| (BG)_k (background map regularity) | OPEN (part of (SF)/N2) | 𝔟(V) local with exponential tails and curvature ‖X(𝔟(V))‖ ≤ C_IL^{-2}max_{P nearby}‖X_P(V)‖ (+ quadratic) |

## 15.3 T7 (b): (SG) ⇒ (PLD)_k on the per-history measure, without RP

**Lemma HS-net: PROVEN-HERE (elementary).** Let μ be a probability measure, A finite, X_p (p ∈ A) Borel su(N)-valued, D := N² - 1,
and suppose that for all unit (u_p) ∈ (S^{D-1})^A and all t ∈ [0, t_1]:
  E_μexp(tΣ_{p∈A}⟨u_p, X_p⟩) ≤ exp(½σ²g²t²|A| + mgt|A|).
Then for every δ ∈ (0, 1], θ := 1 - δ²/2, and every τ > 0 with θτ/(σ²g²) ≤ t_1:
  μ(|X_p|_HS ≥ τ ∀p ∈ A) ≤ ((1 + 2/δ)^De^{mθτ/(σ²g)}e^{-θ²τ²/(2σ²g²)})^{|A|} ≤ ((1 + 2/δ)^De^{m²/σ²}e^{-θ²τ²/(4σ²g²)})^{|A|}.
At δ = ½: θ = 7/8, (1 + 2/δ)^D = 5^D, exponent (49/256)τ²/(σ²g²) in the second form.
*Proof.* Let 𝒩 be a maximal δ-separated subset of the HS unit sphere of su(N); the balls of radius δ/2 about its points are
disjoint and lie in the ball of radius 1 + δ/2, so |𝒩| ≤ (1 + 2/δ)^D, and by maximality every unit v has u ∈ 𝒩 with
|u - v| ≤ δ. For X ≠ 0 and v := X/|X|: ⟨u, X⟩ = |X|(1 - |u - v|²/2) ≥ θ|X| (|u| = |v| = 1). Choosing u_p as the first such point
of a fixed enumeration (Borel), {∀p: |X_p| ≥ τ} ⊂ ∪_{(u_p)∈𝒩^A}{Σ_p⟨u_p, X_p⟩ ≥ θτ|A|}. Union over the |𝒩|^{|A|} direction
patterns, and Markov with t := θτ/(σ²g²) ≤ t_1: each term is ≤ exp(|A|(½σ²g²t² + mgt - θτt)) = exp(|A|(mθτ/(σ²g) -
θ²τ²/(2σ²g²))). Second form: mθτ/(σ²g) ≤ θ²τ²/(4σ²g²) + m²/σ² (ab ≤ a²/4 + b², a = θτ/(σg), b = m/σ). ∎
*Remark.* The union is over a NET of directions (|𝒩|^{|A|}, a C^{|A|} factor); the product bound comes from the joint
exponential moment. This is RLARGE §8.2's sketch, read as in §6 Remark (1).

**Proposition PLD-SG ((PLD)_k on the per-history measure from (SG^{net})_k): PROVEN-HERE | Lemma HS-net, Lemma TL, Lemma KN,
Lemma RS (R1), the threshold algebra of PLD-red (ii) and §9.5.** Assume (SG^{net})_k on μ_{𝔥,ω} with (σ_*, m_*). Put g := g_k,
C_net := 5^De^{m_*²/σ_*²}, a(τ) := 49τ²/(256σ_*²), w_♭ := ec_N^{-1}(κ/g²)^De^{-κε_loc²/(64Ng²)}, n_R := 6(3L)⁴. Then, uniformly in
K, k, the torus, 𝔥, ω:
- (i) for every finite A ⊂ 𝒫°(𝔥) (no disjointness needed) and every τ ∈ (0, ε_1]:
  μ_{𝔥,ω}(||1 - U_p||_op ≥ τ ∀p ∈ A) ≤ (C_nete^{-a(τ)/g²})^{|A|}.
  At τ = η_1 this is RLARGE's (PLD)_k (i) on (M3) with a_η = 49η_1²/(256σ_*²), C = C_net; at τ = η_q it is HIST's (PLD-q)_k.
- (ii) for every finite 𝒜 ⊂ 𝒬°(𝔥), with η_♭ = 3ε_loc/(4(1 + 1.2A_d)) and whenever the base below is ≤ 1:
  μ^+_{𝔥,ω}(ε_♭(U; Q) > ε_loc ∀Q ∈ 𝒜) ≤ (n_RC_nete^{-a(η_♭)/g²} + 8w_♭)^{|𝒜|/7⁴},
  i.e. (PLD)_k (ii) on (M3^+) with a_♭ = min{a(η_♭), κε_loc²/(64N)}/7⁴ up to the polynomial prefactor (κ/g²)^D.
- (iii) (the per-history weight form of (W1-ret') (c), local collar clause σ_Q of §9.1): for every finite cube set
  𝒟 ⊂ 𝒬°(𝔥), μ^+_{𝔥,ω}(σ_Q = 0 ∀Q ∈ 𝒟) ≤ (n_RC_nete^{-a(η_♭')/g²} + 8w_♭)^{|𝒟|/7⁴}, η_♭' = ε_loc/(4.8A_d). (Under μ_{𝔥,ω} every
  level-k cube of Λ(𝔥) is good, so the defective cubes of 𝒟 are collar-bad ones.)
*Proof.* (i): {||1 - U_p||_op ≥ τ} ⊂ {|X_p|_HS ≥ τ} (Lemma TL (iii)); Lemma HS-net with δ = ½, t_1 = ε_1/(σ_*²g²) (θτ/(σ_*²g²) ≤ t_1
since θ < 1, τ ≤ ε_1). (ii): verbatim the proof of PLD-red (ii) (greedy 𝒜' with cube distance ≥ 4, |𝒜'| ≥ |𝒜|/7⁴; U° := U;
Lemma RS (R1); Lemma KN at t = ε_loc/4 with conditional probability ≤ 8w_♭ given U, using that under μ^+ the links of V are
independent given U; subset expansion over S ⊂ 𝒜' and n_R^{|S|} choice functions), with one change: the last factor
μ(∩_{Q∈S}{p_Q bad at η_♭}) is bounded by (i) at τ = η_♭ applied to the set {p_Q : Q ∈ S} ⊂ 𝒫°(𝔥) (distinct plaquettes, in
disjoint N_1(Q)), instead of CB-m.2. So the sum is ≤ Σ_S(8w_♭)^{|𝒜'∖S|}(n_RC_nete^{-a(η_♭)/g²})^{|S|} = (8w_♭ + n_RC_nete^{-a(η_♭)/g²})^{|𝒜'|},
and the base is ≤ 1. (iii): §9.5 verbatim with η_♭' and the same change. ∎
*What changed against PLD-red.* No reflection positivity, no even-torus restriction, no 1/16 Hölder loss in (i), no
disjointness in (i), and the measure is the one RLF-step consumes. The price is the hypothesis: (SG^{net})_k on (M3), which
Finding 2 says is not an in-step output for aligned families. The in-step version follows.

**Proposition INH (cut-good coarse fields carry coherent fine curvature above η_1): PROVEN-HERE | Proposition CF (HIST §6,
CONFIRMED by REVIEW_HIST_S1).** d = 4, L ≥ 3 odd, SU(2) (any SU(N) by the block embedding), on Z⁴. For every ε_1 ∈ (0, 0.517]
and every ε ∈ [1.001L²c_1ε_1, ε_1) (non-empty since L²c_1 = L²/(2(L² + 5.5A_d)) < 1) there are a level-(k+1) field V and a
level-k field U with: every level-(k+1) plaquette has ||1 - V_P||_op ≤ ε < ε_1 (V is cut-good everywhere); V_c = W_0(M̄_c(U)) on
every level-(k+1) link (every kernel factor at its maximum: zero mismatch); every level-k plaquette has ||1 - U_p|| ≤ ε, and
every level-k (1,2)-plaquette has ||1 - U_p||_op ≥ c_1ε_1 = η_1; all finer levels of the chain below U are at curvature
≤ εL^{-2(k-i)}.
*Proof.* Proposition CF with its top level k + 1 and θ := 2arcsin(ε/2) ≤ 2arcsin(0.2585) < π/6: the level-(k+1) (1,2)-plaquette
is e^{iθσ_3}, so ||1 - V_P|| = 2sin(θ/2) = ε, the other planes are 1; the level-k (1,2)-plaquette is e^{iθL^{-2}σ_3}, so
||1 - U_p||_op = 2sin(θ/(2L²)) ≥ (θ/L²)(1 - θ²/(24L⁴)) ≥ (ε/L²)(1 - 1.5·10⁻⁴) ≥ 1.001c_1ε_1(1 - 1.5·10⁻⁴) > c_1ε_1, using θ ≥ ε and
θ² ≤ 0.275; zero mismatch is CF (1); the finer levels are CF (2). ∎ (Check p3 C: the inequality on a grid of (ε_1, ε).)
*Reading.* RLARGE's η_1 = c_1ε_1 lies below the coherent curvature L^{-2}ε that a cut-good V can carry down with zero kernel
cost. So no in-step (fixed-V) bound can make {all level-k plaquettes of a region ≥ η_1} small uniformly over cut-good V;
the probability of such V is the issue, and it is a level-(k+1) quantity. (CF is on Z⁴; on a torus the same holds in any
region not wrapping it, which is all the statement is used for.)

**Proposition PLD-desc (one-step descent: the in-step part of (PLD)_k): PROVEN-HERE | Lemma HS-net, Lemma TL.** Assume
(SG^{fl})_k. Put C_fl := 5^De^{m_fl²/σ_fl²}, a_fl(τ) := 49τ²/(256σ_fl²), g := g_k. For finite A ⊂ 𝒫°(𝔥), τ ∈ (0, ε_1] and V, let
B_V := {p ∈ A : |X_p(𝔟(V))|_HS ≥ τ/2} (a measurable function of V). Then
  μ^+(||1 - U_p||_op ≥ τ ∀p ∈ A, V ∈ 𝒱^{sf}(A)) ≤ E_{μ^+}[1_{𝒱^{sf}(A)}(V)·(C_fle^{-a_fl(τ/2)/g²})^{|A∖B_V|}].
In particular, with τ_bg(A) := sup_{V∈𝒱^{sf}(A)}max_{p∈A}|X_p(𝔟(V))|_HS: for τ ≥ 2τ_bg(A), B_V = ∅ and
  μ^+(||1 - U_p||_op ≥ τ ∀p ∈ A, V ∈ 𝒱^{sf}(A)) ≤ (C_fle^{-a_fl(τ/2)/g²})^{|A|}   (in-step; no RP; no level > k).
*Proof.* On {|X_p(U)| ≥ τ} with p ∉ B_V: |Y_p| ≥ |X_p(U)| - |X_p(𝔟(V))| > τ/2. So the event is contained in
{V ∈ 𝒱^{sf}(A)} ∩ {|Y_p| ≥ τ/2 ∀p ∈ A∖B_V}. Condition on V and apply Lemma HS-net to the conditional law and the family
(Y_p)_{p∈A∖B_V} at threshold τ/2 (its hypothesis is (SG^{fl})_k for the subset A∖B_V; θ(τ/2)/(σ_fl²g²) ≤ ε_1/(σ_fl²g²)); then
take the expectation over V. ∎
*Reading (where the remainder goes).* The term with B_V ≠ ∅ is an event of the coarse field: "the background of V has
|X_p(𝔟(V))| ≥ τ/2 on B". Under (BG)_k it implies level-(k+1) plaquettes near B with ||X_P(V)|| ≥ L²τ/(2C_I), i.e. a level-(k+1)
deviation at a threshold larger by L²/(2C_I). By INH and the CF reading, τ_bg ≳ L^{-2}ε_1 for the zero-mismatch background
(ARGUED identification of 𝔟(V) with the CF preimage: on large regions the kernel pins coherent curvature exactly), so the
in-step regime τ ≥ 2τ_bg does NOT contain RLARGE's η_1 = c_1ε_1 (c_1 = 1/117 < 2/L² = 2/9). Iterating the descent, the
thresholds grow by L²/(2C_I) per level until they exceed 2τ_bg, after m_τ levels: (L²/(2C_I))^{m}c_1 ≥ 2C_IL^{-2}, i.e.
m_τ = 3 at L = 3 if C_I = 1 (check p3 C) [ARGUED; C_I < L²/2 is part of the OPEN (BG)_k; the product structure across the
m_τ levels needs the ℓ² (aggregate) transfer of Lemma LC, not the max-norm one, ARGUED].
**Hence: (PLD)_k at RLARGE's thresholds is an output of steps k, …, k + m_τ, not of step k alone.** At step k only the
fluctuation part (PLD-desc) and the thresholds τ ≥ 2τ_bg are in-step outputs. This is the architecture consequence (§15.6
E4).

## 15.4 T7 (c): levels 0 and 1

**Level 0.** (M3) with 𝔥 = ∅ is the all-cut Wilson law (normalised (M2)), which is reflection symmetric; the existence
lane's chessboard results (PLD-0) apply to it, but (SG^{ph})_0 and (SG^{net})_0 for aligned families contain every scale of
the Wilson measure (Finding 1 (2)), so they are not available at level 0 either. The target is (SG^{fl})_0: the fixed-V law
μ_V(dU_0) ∝ 1_cut e^{-S_W(U_0)/g_0²}K_0(V, U_0) on a history region, which is N5-sf0's setting.
- **What Theorem N5-sf0 gives (quoted; PROOF l.5297-5335).** For (U, V) ∈ 𝔑(α_*) and T ≥ T_0: Õ(U, V) + t invertible for all t ≥ 0;
  the covariance and its square root have the walk expansion; |C(U, V)|(b, b') ≤ c_Ce^{-m_1d(b,b')}; for real (U, V) ∈ 𝔑(α_*),
  Õ(U, V) > 0 with gap λ_min(Õ) ≥ γ'(1 - ε_R)/(8coth⁴(m/2)); entries holomorphic on 𝔑(α_*); walk terms background-local.
- **Its consequence for (SG^{fl})_0 (the Gaussian part; PROVEN as arithmetic from the quoted bounds, not counted).** For the
  centred Gaussian with covariance g_0²C(𝔟(V), V) on the slice, the linearised fluctuation curvature Y^{lin} = D_𝔟A (D_𝔟 the
  covariant plaquette derivative at 𝔟) has, for every s, Var⟨s, Y^{lin}⟩ ≤ g_0²||C||·||D_𝔟||²|s|² ≤ g_0²·(8coth⁴(m/2)/(γ'(1 - ε_R)))
  ·16(1 + O(α_*))|s|², up to the normalisation constant of the action (a factor depending only on N) (||C|| ≤ 1/λ_min; ||D_𝔟||² ≤ ||d||²(1 + O(α_*)) ≤ 16(1 + O(α_*)), §7 (2)). So the Gaussian part obeys
  (SG^{fl})_0 with m = 0 and σ_fl² = 128coth⁴(m/2)(1 + O(α_*))/(γ'(1 - ε_R)): uniform, astronomically large (γ' ≈ γ_0/2 ~ 10⁻⁸, §S19
  threshold), and harmless: only finiteness is used.
- **What is missing for (SG^{fl})_0 itself (SG-F2 MET: N5-sf0 does not give it alone).**
  (G0-1) *Covariance → exponential moment for the non-Gaussian fixed-V law.* Route: a chart in which the law on a box with
  frozen exterior has density e^{-H} with Hess H ≥ ρ/g_0² on a convex domain containing the cut-good set, then
  Bakry-Émery ⇒ log-Sobolev ⇒ Herbst [STANDARD]: E e^{f - Ef} ≤ e^{g_0²Lip(f)²/(2ρ)}. N5-sf0 gives Õ(U, V) ≥ λ_min at every real
  background of 𝔑(α_*), i.e. the Hessian at the base point of each chart; still to be written: (a) the chart Hessian at a
  point x of a fixed box chart differs from Õ(U(x), V) by BCH connection terms of size ≲ |∇H|·|x| ≲ (ε/g_0²)·α_*, which must be
  ≤ λ_min/(2g_0²) [ARGUED; same scale as N5-sf0's threshold]; (b) the Haar Jacobian and the slice/Faddeev-Popov factor FP_U
  (whose background dependence N5 does not address, PROOF l.5348-5349) have Hessians O(1), negligible against 1/g_0² [ARGUED];
  (c) the domain: Lemma AX's box gauges give convex boxes {|A_b| ≤ α_*} containing the cut-good set when 10p_Lℓε_1 ≤ α_*;
  conditioning on the (non-convex) cut costs 1/μ(cut | box) ≤ exp(|box|·Ce^{-c/g_0²}) per box.
  (G0-2) *Box → per-history region (torus-wide):* the walk expansion (Theorem RW (iv)-(v)) decouples the Gaussian part;
  the non-Gaussian part needs (DF1)-(DF4) with Theorem CE, i.e. (SF)_0.
  (G0-3) *(TH):* ε_1 ≤ ε_*, the cut extended to all plaquettes near A, soft residual |ρ_c| ≤ ε_* (its violation is a
  kernel-mismatch event priced in-step by Lemma KN at e^{-κε_*²/(256Ng_0²)}).
  (G0-4) *The mean:* |E[Y_p | V]| ≤ m_flg_0 (a one-loop shift, O(g_0²)) [ARGUED].
- **Status at level 0:** (SG^{fl})_0 ⇐ N5-sf0 [PROVEN, S19] + (G0-1) [standard tools + two ARGUED estimates] + (G0-2) [(SF)_0]
  + (G0-3) [definitional] + (G0-4) [ARGUED]. Partial: the second-order part is proven; the passage to exponential moments
  and the torus-wide decoupling are named.

**Level 1.** The fixed-V law of U_1 given U_2 has density ∝ 1_cut e^{-S_1(U_1)}K_1(U_2, U_1) with S_1 = -log∫e^{-S_0}K_0, so:
- the Gaussian part needs N5 at level 1 at non-trivial backgrounds: Proposition N5-sf_1 ⇐ **(NA-H_loc)_1** (a localised (NA-H):
  the level-1 operator's background dependence, the Schur complement over level 0, is close to the abelian one; PROOF
  l.5351-5358; OPEN; **dependency on session 20**), and N5-sf_i's conclusions exclude locality, which (G1-2) needs: the
  localisation of Hess E_1^{NA}'s background dependence must come with (NA-H_loc)_1;
- (I_1^E) is needed to identify Hess S_1 with Hess E_1^{NA}/g̃_1² + polymer Hessians that are O(1) in the chart (HIST owner);
- (G1-1), (G1-2) = (SF)_1, (G1-3), (G1-4): as at level 0.
**Status at level 1:** (SG^{fl})_1 ⇐ (NA-H_loc)_1 [OPEN, session 20] + (I_1^E) [not yet stated] + (G1-1)-(G1-4).

## 15.5 T7 (d): one estimate for (NH-iii) and (NA-R2)

*Setting.* The chain as an adapted process: 𝔉_i := σ(U_0, …, U_i). For a level-k plaquette P and an observable Φ in
𝔒_P := {⟨u, TL(U_k(P))⟩ : |u| = 1} ∪ {s(U_k(P))} (smooth on the principal domain) or Φ = ||1 - U_k(P)||_op (Lipschitz), let
φ_i := (log(W_0(M̄_c(U_i))^{-1}U_{i+1}(c)))_c (the level-(i+1) injection; given 𝔉_i its law is the product kernel's) and
h_i(φ) := E[Φ | 𝔉_i, φ_i = φ]; the Doob increments are D_i := h_i(φ_i) - E[h_i(φ_i) | 𝔉_i], Φ - E[Φ | 𝔉_0] = Σ_{i<k}D_i;
n := k - 1 - i.

**(INF)_k (depth-uniform influence bound for the soft chain; OPEN; replaces (NH-iii) of §14.3 and EXISTENCE's (NA-R2), and
hence (H-lin^S), NA-R2's second reading).** There are C_I < ∞ and ρ ∈ (0, 1), independent of K, k, i, the torus, the coupling
sequence (the chain's own, §15.6 E1) and the background, such that for every P, Φ, i < k and every 𝔉_i (no small-field
restriction: rough spots included):
- (INF-i) h_i is Lipschitz in ℓ² with constant ≤ C_Iρ^n, and for Φ ∈ 𝔒_P it is C² with ||∇²h_i||_op ≤ C_Iρ^n;
- (INF-ii) at the flat fine background (U_0 ≡ 1), the first-order coefficient a_i := ∇h_i(0) obeys
  ||a_i|² - |a_i^{lin}|²| ≤ C_IL^{-2n}σ̄²(n + 1), a_i^{lin} the linear soft chain's coefficient (Theorem NA-GS1 / GS), σ̄² := max_jσ_j².
*Why one estimate.* (NH-iii) asks for the Lipschitz influence of injections through rough backgrounds, uniformly in depth;
(NA-R2) asks for the second-order remainder of the same influence at the flat background. Both are properties of the maps
h_i; (INF-i) is the first-order part at every background, (INF-ii) the background stability of its coefficient. The
expected value of ρ is L^{-1}(1 + O(ε)) on small-field backgrounds (§7 (2): ||dQ_str^m|| ≤ 4L^{-m}); what is open is ρ < 1
through rough spots (ROUGH shows they are present) and away from Lemma PM's regime.
**Lemma AZ ((INF-i) + kernel log-Sobolev ⇒ (NH)_k): PROVEN-HERE | Herbst's argument, LSI tensorisation [STANDARD].** Suppose
(NH-i') the law of φ_i given 𝔉_i satisfies a log-Sobolev inequality with constant c_Kg_i²/κ (∫f²log(f²/∫f²) ≤ 2c∫|∇f|²; it
tensorises over the independent links of the product kernel). Then for Φ as above, every 𝔉_0 and r > 0:
  P(Φ - E[Φ | 𝔉_0] ≥ r | 𝔉_0) ≤ exp(-r²κ(1 - ρ²)/(2c_KC_I²g_k²)),
so (NH)_k (§14.3) holds with a_N = κ(1 - ρ²)/(8c_KC_I²), C_N = 1, uniformly in k.
*Proof.* Herbst: under LSI(c), E e^{λ(f - Ef)} ≤ e^{cλ²Lip(f)²/2} for every λ; so E[e^{λD_i} | 𝔉_i] ≤ e^{λ²b_i²/2} with
b_i² := c_Kg_i²C_I²ρ^{2n}/κ. Tower property from the top: E[e^{λΣ_{i<k}D_i} | 𝔉_{k-1}] = e^{λΣ_{i<k-1}D_i}E[e^{λD_{k-1}} | 𝔉_{k-1}] ≤
e^{λΣ_{i<k-1}D_i}e^{λ²b_{k-1}²/2}; iterating, E[e^{λ(Φ - E[Φ|𝔉_0])} | 𝔉_0] ≤ e^{λ²Σb_i²/2}. Markov at λ = r/Σb_i². Finally
Σ_ib_i² ≤ c_KC_I²κ^{-1}Σ_{n≥0}g_{k-1-n}²ρ^{2n} ≤ c_KC_I²g_k²/(κ(1 - ρ²)), since g_i ≤ g_k for i < k. (NH)_k: r = τ/2. ∎
(Herbst's argument is the displayed two-line computation from LSI applied to f = e^{λf/2}; tensorisation is standard;
neither is re-proved here. (NH-i') is ARGUED for SU(2) (the central law μ_t has a uniformly log-concave angle density away
from the antipode at scale t^{-1/2}) and open for N ≥ 3 (non-central kernel).)
**(INF) ⇒ (NA-R2): ARGUED (not written).** Martingale orthogonality gives E[Φ²] = Σ_iE[D_i²] at the flat background (E Φ = 0 by
Proposition NA-3 for Φ = ⟨u, TL⟩); a second-order Taylor expansion of h_i with (INF-i)'s Hessian bound and the symmetry
φ ↦ -φ of μ_t gives E[D_i²] = σ_i²E|a_i|² + O(C_I²ρ^{2n}σ_i⁴); (INF-ii) replaces |a_i|² by |a_i^{lin}|² at the cost
C_IL^{-2n}σ̄²(n + 1)σ_i²; summing over i and using 1 - N^{-1}Re tr e^X = |X|²/(2N) + O(|X|⁴) gives (NA-R2)'s right side.
**Track as one item:** (INF)_k, with (NH)_k ⇐ (INF-i) + (NH-i') [PROVEN, Lemma AZ] and (NA-R2) ⇐ (INF) [ARGUED].

## 15.6 PROPOSED RLARGE v2 EDITS (exact changes for the integrator; not made here)
**RLARGE.md**
- **E1 (F)-quantifier [B6].** §0 "Flow hypothesis (F)" (l.52-53): add "(F) is used only for the soft chain's own effective
  sequence (g̃_k) (node A5), or, as a sufficient bracket, for sequences with β_- ≥ β_1 - o(1), β_1 := 11N²/(12π²) in this
  file's normalisation [one-loop basis ARGUED, PLD §14.1]; since the kernel couplings enter the chain's running through the
  noise O(g_i²/κ), 'the chain's own sequence' is a fixed-point condition (A5's content)". §1A Theorem RLF (l.124-125; also §1 l.67): replace
  "every coupling sequence with g_K ≤ g_0 obeying (F)" by "the soft chain's own effective coupling sequence, with g_K ≤ g_0
  (or every sequence obeying (F) with β_- ≥ β_1 - o(1))". The same in §8.2 (PLD) (l.599-604) and §8.3.
- **E2 [B5].** §1A item 2 (l.108-109): in "bad (ζ_Q = 1) or collar-bad (ε_♭(U; Q) > ε_loc, or (H-ch) fails on Q's box)",
  delete ", or (H-ch) fails on Q's box", and define collar-bad by σ_Q = 0 with σ_Q := 1{max_{p⊂N_1(Q)}||1 - U_p|| ≤ ε_loc/2 and
  max_{c∈C(Q)}||V_c - S_c(U)|| ≤ ε_loc/2} (PLD §9.1 (i); Proposition SHADOW is the reason).
- **E3 [B4].** §7.2 Theorem R1 (i) and the localised logarithm used in §8.2 (W1-ret') (a): use the σ-restricted gas (Lemma
  7.2-0 with "σ ≡ 1 on the support" in place of (H-ch)); list the returned collar-bad configurations (σ_Q = 0, n ≤ n_♯) as
  an explicit activity family of (W1-ret') (a) / (SC)_k with the bound of PLD §9.1 repair (β); do not apply R1 (ii)-(iii)
  pointwise in the sample; extract at V = 1 after the sea average (PLD §9.3, Lemma W1R-tay).
- **E4 [B7, as qualified by §15.3].** §8.2 (PLD)_k (l.599-604), replace the item by:
  "(PLD)_k is not a hypothesis. Its in-step part is an output of (SF)_k: **(SG^{fl})_k** (PLD §15.2: fixed-V Gaussian
  concentration of the fluctuation curvature Y = X(U) - X(𝔟(V)), net form with an ℓ¹ term, on the per-history stage-k law
  μ^+_{𝔥,ω}) is a clause of (SF)_k's output, and Proposition PLD-desc gives the per-history product bounds at every threshold
  τ ≥ 2τ_bg in-step, with Proposition PLD-SG's constants. RLARGE's thresholds η_1 = c_1ε_1 and η_♭ lie below 2τ_bg
  (Proposition INH), so for them the remainder of PLD-desc is a level-(k+1) event on the background curvature, priced after
  m_τ further steps (look-ahead; m_τ = 3 at L = 3 if C_I = 1, ARGUED)." Also replace "and a union bound over disjoint supports"
  by "and a union bound over a net of directions (PLD Lemma HS-net)".
- **E5.** §8.3 title and hypothesis list: "(PLD)_k" → "(SG^{fl})_k [a clause of (SF)_k] + (BG)_k + the look-ahead pricing of
  PLD-desc". Step 4: "(W1-ret')_k (c) … ((PLD)_k (ii) for the collar-bad cubes …)" → "… (PLD-SG (iii) for the in-step part,
  PLD-desc for the inherited part, priced m_τ steps later in (HIST)'s assembly)". Step 6: "(PLD)_k (i)" → "PLD-desc at
  τ = η_1 (in-step part) + inherited part as in step 4". Rationale: the unreturned weights and RS's pricing are consumed only
  by the final summation (P1)/HIST-sum, so evaluating them after m_τ more steps changes no other step; this is the minimal
  change. The alternative (A), fluctuation-relative level-k defects, would make (PLD)_k fully in-step but breaks Lemma RS's
  dichotomy (Proposition CF: a bad level-(k+1) plaquette with no fluctuation and no mismatch at any level), so it needs a new
  RS; not recommended without that.
- **E6.** §8.5 and §11 weights: "(PLD) [s given SF]" → "(SG^{fl}) [s given SF and (I_k^E)], (BG) [s, part of (SF)/N2], look-ahead
  bookkeeping [s]"; add (INF) [P?, OPEN] as the merged (NH-iii)/(NA-R2) item if RLARGE tracks the noise half.
- **E7 [B9].** §0 "Tori": require hypercubic tori (equal sides) wherever Lemma W1R-sym / GT-lat' (ii) gives ONE coupling
  shift; with a different time side the time-preserving subgroup splits Λ²R⁴ into electric and magnetic triplets and two
  shifts are needed. Note that the per-history route (PLD-SG, PLD-desc) uses no RP, so RLF-step no longer needs the even
  tori of the chessboard results; those stay in the existence lane.
- **E8.** §1A R1819-fix 8 already requires ε_1, ε_loc ≤ the N5 threshold; add: "also ε_1 < 2 sin(π/N) (so that the principal
  logarithm of cut-good plaquettes is traceless, PLD Lemma TL), and the cut controls every plaquette used as an N5 background
  (not only cube-interior ones) near the sets where (SG^{fl}) is applied".
**EXISTENCE.md (owner)**
- **X1 [B8].** X-RP^S class (l.1410-1411 at review time; the "closed union" wording is at l.1439-1440 of the current file): "closed union … in the OPEN half-space" → "all descendant sites strictly on the
  positive side" (the literal reading excludes Theorem CB's own interior plaquettes).
- **X2.** (RLF-3^dis) (l.1536-1538): quantifier as E1.
- **X3.** Record (PLD^mod_dis) uniform as downstream of A5 (PLD-AF), not an independent wall.
- **X4.** Track (NA-R2) and (H-lin^S) as one item with PLD's (NH-iii): (INF)_k, PLD §15.5.
**HIST.md (owner).** (I_k^E) (REVIEW_HIST_S1 fix H-2) is an input of (SG^{fl})_k (§15.2 table); its statement should fix the
background map 𝔟(V) used there.

## 15.7 Check p3 (criteria checks/p3_criteria.md, written after §15.1-§15.5 and before the script; script checks/p3_pld.py; output checks/p3_out.txt; record checks/p3_time.txt)
**All parts PASS, one run** (1.1 s, 90 MB; lock waited 00:27-00:32 UTC; load 3.1, 34% free; nice 10, threads 1). Two
pre-run script edits and two in-tolerance items are disclosed in p3_time.txt.
- A (Lemma TL, N = 2, 3, 4, 6610 samples including all central elements and -1): ||e^{TL} - U|| ≤ 1.0e-11, |tr TL| ≤ 7.9e-15,
  ||1 - U||_HS ≤ |TL|_HS, ||TL||_op ≤ 3π, TL = principal log on O_N. Negative control A6: the principal log has |tr| ≥ 1 at every
  non-trivial central element.
- B: the HS-net bound is ≥ 103 × the exact probability and the Gaussian-ξ bound ≥ 21.9 × in all 108 Gaussian cases; the
  prefactor-1 negative control is violated (the check discriminates); the net has 34 ≤ 125 points (covering 0.87439 vs 0.875,
  within the sampling tolerance); G-IR's Gaussian CGF and threshold algebra confirmed.
- C: N ≥ 37 (C1); smallest N = 593/594 at t = ½ and 507954/507955 at t = 2/117 (C2, as now written in §14.4); the F-1 constant
  to 6e-16; INH on grids for L = 3, 5 (min ratio 1.001, i.e. the margin is the stated 1.001); descent depth m_τ = 3, 4, 5 for
  C_I = 1, 1.5, 2 at L = 3 (informational); the SHADOW condition (F-6).
Scope: nothing about SU(N) lattice measures, (SG), (SF), N5 or (INF) is tested.

## 15.8 Outcome against the pre-stated targets (§15.0) and tally
- **T6: MET.** Every PLD-owned binding fix applied in place with [RPLD-fix] (table in §15.1); the three overclaims withdrawn;
  B5-B9 routed (§15.6); process gap recorded in PLD_LOG as an appended correction (no history rewritten).
- **T7: PARTIAL SUCCESS, with SG-F1, SG-F2 and SG-F3 all met.**
  - (b) PROVEN: Lemma HS-net and Proposition PLD-SG: (SG^{net})_k on the per-history law ⇒ (PLD)_k (i), (ii), (PLD-q)_k and
    the per-history (W1-ret') (c) weights, with explicit constants (C_net = 5^{N²-1}e^{m_*²/σ_*²}, a(τ) = 49τ²/(256σ_*²)), no RP,
    no even-torus restriction, no disjointness in (i).
  - (a) stated precisely: (SG^{ph}), (SG^{net}), (SG^{fl}) on (M3)/(M3^+). **SG-F3:** the ℓ¹ term is load-bearing (Remark G-IR:
    exact for Gaussians; with one-loop running, m_* = 0 is inconsistent, and no Gaussian-domination proof with the true
    two-point function can give (SG^{net}) for aligned families). **SG-F1:** (SG^{ph})/(SG^{net}) are not in-step outputs (they
    contain all coarser scales; Proposition INH); the in-step form is (SG^{fl})_k, and Proposition PLD-desc gives (PLD)_k
    in-step only at thresholds τ ≥ 2τ_bg. RLARGE's η_1 = c_1ε_1 is below that, so (PLD)_k at RLARGE's thresholds is an output
    of steps k, …, k + m_τ (look-ahead; m_τ = 3 at L = 3 if C_I = 1, ARGUED). This qualifies REVIEW_PLD_S1_S2's recommendation
    4(a): "derive (PLD)_k in-step from (SG)_k" holds for the fluctuation part only.
  - (c) **SG-F2:** N5-sf0 gives the second-order (Gaussian) part of (SG^{fl})_0 uniformly (σ_fl² ≍ 128coth⁴/γ'); the passage to
    exponential moments needs (G0-1) (Bakry-Émery in a box chart, two ARGUED estimates), (G0-2) = (SF)_0, (G0-3), (G0-4).
    Level 1 additionally needs (NA-H_loc)_1 (session 20's target) and (I_1^E).
  - (d) (INF)_k stated: one estimate replacing (NH-iii) and (NA-R2) (and (H-lin^S)); Lemma AZ PROVEN: (INF-i) + kernel LSI ⇒
    (NH)_k with a_N = κ(1 - ρ²)/(8c_KC_I²); (INF) ⇒ (NA-R2) ARGUED.
- **T8: MET.** p3, criteria first, all PASS.
- Not-success items avoided: no covariance bound is presented as an exponential-moment bound (N5-sf0's part is labelled the
  Gaussian part); no RP on (M3); no constant depends on K, k, the torus or the history.
- **PROVEN-HERE [E3], counted (2, unreviewed):** (1) Lemma HS-net with Proposition PLD-SG; (2) Proposition PLD-desc with
  Proposition INH. Not counted: Lemma TL (part of fix F-4), Lemma AZ (standard Azuma-Herbst assembly), Remark G-IR (Gaussian
  algebra; SU(N) reading ARGUED), the level-0 Gaussian-part arithmetic.
- **New named items:** (SG^{fl})_k (in-step, a clause of (SF)_k), (BG)_k (background map regularity, C_I < L²/2), (INF)_k
  (merged; OPEN), (G0-1)-(G0-4), (NH-i') (kernel LSI). Withdrawn as stand-alone targets: (SG^{ph})_k as an in-step output.
- **Tally proposal:** +2 PROVEN-HERE (unreviewed); 0 OPEN items closed; (NH-iii) and (NA-R2) merged into one OPEN item
  (INF) (net change 0 if the ledger tracked them as one already, -1 otherwise); no new top-level OPEN item.
- **Next (recommendation):** review §15.2-§15.3 (PLD-SG, PLD-desc, INH and the SG-F1 reading); then (BG)_k's C_I in the
  linear model (a session-scale computation that decides the look-ahead depth), before any RLARGE v2 integration.

---
# Session 4 (2026-10-28, lane E)

Inputs read this session before the pre-statement (read-only): REVIEW_RLARGE_V3.md in full; RLARGE.md v3 l.40-123 (§0),
l.186-246 (§1.2), l.281-336 (§2), l.337-470 (§3, §4.1), l.467-546 (§4.2-§4.3); HW.md l.76-430 (§2-§6), l.607-873 (§13-§15.3),
l.918-1018 (§18-§19); PLD.md §0-§1, §9, §15.0-§15.3 (this file); REVIEW_PLD_S3.md l.1-60, l.215-520; SF.md §7.1 (CE-exp),
§13.1 head (HALO, SH, CE-Q-col statement), §16.2 (KF, DX-rel), §20.1, §23.1; REVIEW_SF_S7.md head; HIST.md §4 (CL^J), §5
(R1^J, R1_Λ), §6 (H-pos^J, CF), §8, §14.1, §25.6; PROOF.md: grep only for N5-sf0 / N5-sf_i / RW / S4' (line locations; the
statements are used as quoted by RLARGE v3 and REVIEW_PLD_S3, not re-read). HW.md is being edited concurrently by lane H for
(LI^U); this file treats (LI^U) as a named hypothesis in the form REVIEW_RLARGE_V3 S-1 states it.

## 16.0 PRE-STATED (session 4) — statements only (written 2026-10-28 10:14 UTC, before any session-4 derivation and before
checks/p4_criteria.md)

**Setting for §16.** Bad-only defects D_j = {ζ = 1} (RLARGE §2.2; HW §13 preamble); history-independent D_j; SU(2) (SU(N ≥ 3)
needs (KS-N)); (F_R) with g_K² ≤ 1/(2R); u_j = 1/g_j². Laws: **ℛ^A_𝔥** := the laws μ_{R_{S,E'}} with R_{S,E} ∈ ℛ_𝔥^↑ ∪ {R(𝔥)}
and E' ⊇ E (closure of RLARGE §3.2's family under HW's Lemma DECL). For μ = μ_R, the **future tilt** at level k is
H^μ_k(U_k) := ∫K_k(U_{k+1}, U_k)1_{R,k+1}h_{k+1}(U_{k+1})dU_{k+1} (h_{k+1} as HW §5.2), and the **past law** ν^μ_k is the law of
(U_0, …, U_k) under e^{-S_0}Π_{i<k}K_iΠ_{j≤k}1_{R,j} (normalised); then μ restricted to (U_0, …, U_k) is ν^μ_k tilted by H^μ_k.
**(LI^U)** [named hypothesis; owner HW; REVIEW_RLARGE_V3 S-1]: for every μ ∈ ℛ^A_𝔥, every k, every finite set S of level-k
cubes and all U, U' differing only on the level-k links read by S's windows and collars,
H^μ_k(U) ≤ exp(c_U(|S| + Σ_{m>k}|sh_m(S)|))·H^μ_k(U').

**T9 (THEOREM NA-PRICE, the in-step returned price; the target).** State and prove, or reduce to one named minimal statement:
there are a_A, a_ret > 0, C_A, c_sf < ∞ and θ with max{6θ, 24θ}(1 + 2Rg_K²) < 1, independent of g, K, T, k, 𝔥 and the law,
such that for every μ ∈ ℛ^A_𝔥 and every level k ≥ 0:
- **(i) (SDP)^A:** μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·exp(2c_U(|S| + Σ_{m>k}|sh_m(S)|)) for every finite set S of level-k cubes;
- **(ii) (SF-cap)^A_θ** in HW §15 / §18.1's form (fine moment on defect-free columns, uniformly under conditioning on finer
  defects in other columns), with c_sf explicit in terms of certified small-field constants where they exist;
- **(iii) a_ret:** an explicit formula for the exponent of the returned-cluster bounds of (SC)_k (PLD §9.4, (SC2)) in terms of
  ε_1, κ, c_pr, the certified small-field constants (σ_fl, C_fl via N5 / RW-ℓ²) and the kernel constants, together with the
  V-domain on which it holds; and the relation between a_ret and a_A (REVIEW_RLARGE_V3 K12: "a_ret − (tilt allowance) ≥ θa_bad");
- **(iv) law:** every statement is under μ ∈ ℛ^A_𝔥 ⊃ {μ_{R(𝔥)}} (the law of RLARGE v3 §3); where a step is naturally under the
  forward/past law ν^μ_k or PLD's μ^+_{𝔥,ω}, the exact conversion through (LI^U) is written, with its cost.
Inputs allowed: SF's small-field package (CE-exp, CE-Q-col, DX-rel and the certified constants), (SG^{fl})_k + PLD-desc + HS-net,
CL^J/R1^J (HIST), KS/KS-chain, DECL, Lemma CH/CAP/TE/W-bad (HW), (CLS-min), (LI^U). Uniform in k.
- **Success:** (i)-(iv) PROVEN-HERE (conditional only on (LI^U), (CLS-min) and named small-field statements), a_A, a_ret explicit.
- **Partial success:** a conditional theorem whose ONE new hypothesis is named, stated with all quantifiers, shown to be
  strictly weaker than (SDP)^A itself or of a different kind (single-level, deterministic, or small-field), and shown sufficient;
  a_A, a_ret explicit modulo that hypothesis.
- **Valid failure outcomes:** (NP-F1) (SDP)^A is not obtainable from the allowed inputs by any argument that reads the finer
  field only through the listed small-field bounds (the exact obstruction named, e.g. LOOP-const in a new guise); (NP-F2) no
  uniform a_ret > 0 exists on the V-domain (SC)_k is stated on (counterexample family named), with the restricted domain on
  which it does; (NP-F3) the law conversion through (LI^U) costs a factor that is not absorbable (quantified).
- **Not success:** an exponent or constant depending on k, K, T or 𝔥; a fixed-V price of a bad coarse cube (FV); a column
  induction (LOOP-const) presented as uniform; any use of (H-w′), HIST-sum or (RLF-3′) at levels ≥ k (REVIEW_RLARGE_V3 S-2).

**T10 (K12: does (BG)_k return to the critical path through (SC)_k?).** Decide, with a written argument: (a) yes, which part of
(BG)_k (localisation radius R_bg; curvature constant C_I; on which V-domain) enters a_ret, and through which statement; or (b) no,
with the route that avoids it.

**T11 (check p4; criteria file checks/p4_criteria.md before checks/p4_*.py).** Exact or certified arithmetic for the explicit
constants of T9 (a_A, a_ret and the inequalities they need), a numerical test of every new elementary inequality on SU(2) samples
with a negative control, and a model check of any recursion claimed uniform (with the LOOP-const case as negative control).

# Session 4 derivations (written after §16.0, from 10:16 UTC; before checks/p4_criteria.md)

**Index convention for §16.** Q is a level-k cube (k ≥ 1); "Q bad" means ζ_Q(U_k) = 1; the stage-(k-1) kernel K_{k-1}(U_k, U_{k-1})
= Π_ck_c has stiffness κu_{k-1}; ℓ(Q) := the n_int links of int Q (level k). The column energy F^col_Q(U_{k-1}) and the windows are
HW §4's with the level index shifted by one (HW writes them for level-(k+1) cubes and U_k). Y^f_Q := 24u_kF^col_Q(U_{k-1}).
G_Q := {no level-(k-1) cube under Q is in D_{k-1}} (81 cubes). sh(S) := Σ_{m>k}|sh_m(S)| (union form, HIST §7.1), and
‖S‖_sh := |S| + sh(S). For SU(2), M̄_c(U_{k-1}) = r_cŴ_c (r_c = ||M̄_c||_op ∈ [0, 1]), W_0(M̄_c) = Ŵ_c, φ_c = r_c(1 - cos α_c) =
r_c||V_c - Ŵ_c||²_op/2 (HW Lemma KS (a)); so φ_{M̄_c}(W_0(M̄_c)) = 0.

## 16.1 Lemma FT (future-tilt conversion for kernel events): PROVEN-HERE (counted) | (LI^U), Lemma DECL, Lemma TD (product kernel)
*Claim.* Let μ = μ_R ∈ ℛ^A_𝔥, k ≥ 1, T a finite set of level-k cubes, R' := R with T declared at level k (so μ' := μ_{R'} ∈ ℛ^A_𝔥),
and F ≥ 0 a bounded measurable function of (U_0, …, U_{k-1}). Put c_T := c_U‖T‖_sh. Then
  E_μ[1{T ⊂ D_k}·F] ≤ e^{4c_T}·E_{μ'}[Π_{Q∈T}p_K(Q | U_{k-1})·F],  p_K(Q | U_{k-1}) := ∫Π_{c∈ℓ(Q)}k_c(V_c; M̄_c(U_{k-1}))ζ_Q(V)dV_{ℓ(Q)}.
*Proof.* (1) DECL (HW §13.1) with F riding along: on {T ⊂ D_k}, 1_R = 1_{R'} (the declared cubes are defects), so
E_μ[1{T ⊂ D_k}F] = Z(R')E_{μ'}[1{T ⊂ D_k}F]/Z(R) ≤ E_{μ'}[1{T ⊂ D_k}F] (Z(R') ≤ Z(R), (m1)). (2) Write μ' on (U_0, …, U_k) as the past
law ν' := ν^{μ'}_k tilted by H' := H^{μ'}_k (§16.0). Let U^ref be U_k with the links ℓ(T) := ∪_{Q∈T}ℓ(Q) replaced by 1. These are
links read by T's windows, so (LI^U) gives e^{-c_T}H'(U^ref) ≤ H'(U_k) ≤ e^{c_T}H'(U^ref). (3) Under ν', given (U_0, …, U_{k-1}),
U_k has density ∝ Π_ck_c·1_{R',k}(U_k). With T declared and bad-only defects, 1_{R',k} reads no link of ℓ(T) (DECL, second
claim), and the factors 1_{R',j}, j < k, read levels ≤ k - 1. So, given (U_0, …, U_{k-1}) and U_k off ℓ(T), the links ℓ(T) have
the product density Π_{c∈ℓ(T)}k_c, and ζ_Q, Q ∈ T, reads only ℓ(Q). Since H'(U^ref) and F do not read ℓ(T):
  E_{ν'}[1{T ⊂ D_k}F·H'(U^ref)] = E_{ν'}[Π_{Q∈T}p_K(Q | U_{k-1})·F·H'(U^ref)]
(the ℓ(Q) are disjoint, so the kernel probability factorises; Lemma TD). (4) Numerator: E_{ν'}[1{T⊂D_k}FH'(U_k)] ≤ e^{c_T}·
(the line of (3)) ≤ e^{2c_T}E_{ν'}[ΠpK·F·H'(U_k)] (H'(U^ref) ≤ e^{c_T}H'(U_k)). Denominator: E_{ν'}[H'(U_k)] is the normalisation
of μ' itself. Dividing: E_{μ'}[1{T ⊂ D_k}F] ≤ e^{2c_T}E_{μ'}[Π_Qp_K(Q | U_{k-1})F]. With step (1), e^{2c_T} ≤ e^{4c_T}. ∎
*Remark (sharper constant).* The proof gives e^{2c_T}; e^{4c_T} is kept as the stated allowance (two uses of (LI^U) if the
reference is chosen differently). *Remark (what is converted).* Only the top-level kernel event of the cubes of T is converted;
every factor F of the finer fields stays under the same relaxed law μ' ∈ ℛ^A_𝔥. No fixed-V law is used (FV is respected).

## 16.2 Lemma FV-law (fixed-coarse-field laws carry no future tilt): PROVEN-HERE (elementary, not counted)
For μ = μ_R and every k, the conditional law of (U_0, …, U_k) given (U_{k+1}, …, U_K) is that of the past law ν^μ_{k+1} given
U_{k+1}: ∝ e^{-S_0}Π_{i≤k}K_iΠ_{j≤k+1}1_{R,j}. *Proof.* The factors of W·1_R that read levels > k + 1 are functions of
(U_{k+1}, …, U_K) only (bad-only: 1_{R,j} reads U_j; K_i, i ≥ k + 1, read U_i, U_{i+1}); they cancel in the conditional law. ∎
*Consequence.* Every fixed-V statement used below ((SG^{fl}), PLD-desc, the sea law ⟨·⟩_V of (SC)) is the same under μ ∈ ℛ^A_𝔥 as
under the forward chain with the past constraints; (LI^U) is not needed for them. It is needed only where a probability of a
coarse event is read under μ (Lemma FT). This is the exact conversion asked for in T9 (iv). **[RPLD4-fix FV-1, recommended]**
FV-law removes the tilt, not the pattern dependence: the past constraint factors 1_{R,j}, j ≤ k, of a relaxed or declared
R_{S,E} are not those of PLD's per-history measures. So the Consequence holds provided (SG^{fl}), PLD-desc and the sea law hold
uniformly over the past constraint patterns of ℛ^A_𝔥 (REVIEW_RLARGE_V3 S-4).

## 16.3 Lemma KD (kernel dichotomy): PROVEN-HERE (counted with FT) | Lemma KS (a), (c) [SU(2)], unitarity
Define the **centre set** 𝒞(U_{k-1}) := {level-k cubes Q : some c ∈ ℓ(Q) has r_c < ½, or all r_c ≥ ½ and some interior plaquette
P of Q has ||1 - V^0_P||_op ≥ ε_1/2}, V^0_c := Ŵ_c = W_0(M̄_c(U_{k-1})) (c ∈ ℓ(Q)). Then for every λ ∈ [0, 1):
  p_K(Q | U_{k-1}) ≤ 1{Q ∈ 𝒞(U_{k-1})} + p_mis,  p_mis := n_int(1 - λ)^{-3/2}e^{-λκu_{k-1}ε_1²/256}.
*Proof.* Let Q ∉ 𝒞. For an interior plaquette P with ||1 - V_P|| ≥ ε_1: telescoping the product of four unitaries,
||1 - V_P|| ≤ ||1 - V^0_P|| + Σ_{c∈∂P}||V_c - V^0_c||, so some c ∈ ∂P ⊂ ℓ(Q) has ||V_c - Ŵ_c|| > ε_1/8, hence φ_c ≥ ½·(ε_1/8)²/2 =
ε_1²/256 (r_c ≥ ½). So {ζ_Q = 1} ⊂ ∪_{c∈ℓ(Q)}{φ_c ≥ ε_1²/256}. For one link, Markov and KS (c):
∫k_c1{φ_c ≥ t} ≤ e^{-λκu_{k-1}t}∫k_ce^{λκu_{k-1}φ_c} ≤ (1 - λ)^{-3/2}e^{-λκu_{k-1}t}, uniformly in M̄_c. Union over the n_int links. ∎
(The exponent is the mismatch branch at the finer coupling, as RS (R4); it needs no quietness: degenerate M̄ is moved into 𝒞.)

## 16.4 Lemma CW (centre window): CONDITIONAL ⇐ (CLS-min) (counted with FT) | HW Lemma TE (i)-(ii), RS (R1), inequality (B)
Assume ε_1 ≤ min{1/(4A_d), t_pr}. If Q ∈ 𝒞(U_{k-1}) then **F^col_Q(U_{k-1}) ≥ a_bad/4**, hence Y^f_Q ≥ 6a_badu_k.
*Proof.* (a) Some r_c < ½ (c ∈ ℓ(Q)). M̄_c is the mean of the S4' transporters T^σ_y, so ½ > r_c ≥ ||T_1|| - max_i||T_i - T_1||, and
some T_i has ||T_i - S_c|| > ¼. By RS (R1) (RLARGE App. A §6), δ_c ≤ A_dη, so some level-(k-1) plaquette p with all vertices in c's
two endpoint blocks has ||1 - U_{k-1}(p)|| > 1/(4A_d). Both endpoint blocks are level-(k-1) cubes under Q (c ∈ int Q), so the terms
of the cone 𝒞(p) are column terms of Q (as in HW Observation SAT), all ≥ 0, and F^col_Q(U_{k-1}) ≥ ℰ_p(U_{k-1}) ≥
c_pr·min{1/(16A_d²), t_pr²} ≥ c_prε_1² = a_bad (TE (ii) at level k - 1 ≥ 1; at k - 1 = 0, ℰ_p = s(U_0(p)) ≥ ||1 - U_0(p)||²/(2N) by
(B), and c_pr ≤ 1/(2N)). (b) All r_c ≥ ½ and ||1 - V^0_P|| ≥ ε_1/2 for an interior P. ℰ_P depends on V only through V|_{∂P}, and
∂P ⊂ ℓ(Q). TE (ii) at level k for the field V^0 on ∂P: ℰ_P(V^0) ≥ c_pr·min{ε_1²/4, t_pr²} = a_bad/4. TE (i) with U = U_{k-1}:
ℰ_P(V^0) ≤ κΦ_{∂P}(U_{k-1}, V^0) + ℰ^<_P(U_{k-1}) = ℰ^<_P(U_{k-1}), because φ_{M̄_c}(Ŵ_c) = 0. ℰ^<_P is the infimum of a sub-sum of the
(nonnegative) column terms of Q, so ℰ^<_P ≤ F^col_Q. ∎
*Reading.* The coherent background (CF/INH: zero mismatch, cut-good finer fields) lands in (b) and is priced through the
column energy, i.e. by (CLS-min), with no background map. **[RPLD4-fix CW-1]** ~~A returned finer defect in Q's column lands
in (a) or (b) as well, because it raises F^col_Q (SAT); that is the only place where it enters (§16.6).~~ (false: the split
(a)/(b) is on Q ∈ 𝒞, a property of the kernel centre, not of F^col.) Corrected: a column with a returned finer defect is in 𝒞
or not. If not, KD prices Q by the kernel mismatch, whatever the finer defect. If so, CW still gives F^col_Q ≥ a_bad/4, but
(SF-cap)'s factor 1_{G_Q} excludes the column. This is the only place a returned finer defect enters (§16.6). [Whether a
returned finer defect at threshold can put Q in 𝒞 at all is computed in §17 (check p5 B), not assumed.]

## 16.5 Theorem NA-PRICE (i): (SDP)^A. CONDITIONAL (implication PROVEN-HERE; counted) | FT, KD, CW, (SF-cap)^{A,+}_θ, (J-NS^dir)
**Inputs (named).**
- **(SF-cap)^{A,+}_θ** [node A; the small-field half; HW §18.1's (SF-cap)^A for arbitrary finite sets of cubes, with its
  "uniformly under conditioning on finer defects in other columns" written out]: for every μ ∈ ℛ^A_𝔥, k ≥ 1, finite set A of level-k
  cubes, A' ⊂ A and bounded F ≥ 0 measurable with respect to (U_0, …, U_{k-1}) restricted to the columns of A',
    E_μ[Π_{Q∈A∖A'}e^{θY^f_Q}1_{G_Q}·F] ≤ c_sf^{|A∖A'|}e^{c_f‖A∖A'‖_sh}E_μ[F],  24θ(1 + 2Rg_K²) < 1.
  (F = Π_{A'}1_{G^c_Q} is HW's form, with c_f = 0.)
- **(J-NS^dir)** [node A; NEW; the saturated case, stated directly]: for every μ ∈ ℛ^A_𝔥, k ≥ 1 and finite set S_1 of level-k cubes,
    μ(∩_{Q∈S_1}({Q ∈ 𝒞(U_{k-1})} ∩ G^c_Q)) ≤ (C_nse^{-a_nsu_k})^{|S_1|}e^{c_ns‖S_1‖_sh},  a_ns ≥ θa_bad.
  In words: a level-k cube whose kernel centre is bad (or degenerate) while its finer column contains a returned defect.
**Claim.** Under (F_R) with g_K² ≤ 1/(2R), SU(2), bad-only defects, ε_1 ≤ min{1/(4A_d), t_pr}, (LI^U), (CLS-min), (SF-cap)^{A,+}_θ and
(J-NS^dir): for every μ ∈ ℛ^A_𝔥, k ≥ 1 and finite set S of level-k cubes,
  **μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·e^{c_A‖S‖_sh},**
  **a_A := min{λκε_1²/256, 6θa_bad, a_ns},  C_A := 3·max{n_int(1 - λ)^{-3/2}e^{λκε_1²R/256}, c_sf, C_ns},  c_A := 4c_U + c_f + c_ns,**
for any fixed λ ∈ (0, 1). **[RPLD4-fix C-1/NA-2]** With §16.7's corrected c_f = 2c_U this is **c_A = 6c_U + c_ns**, not the
2c_U pre-stated in §16.0 (i) (l.1306): a disclosed deviation. Its consequence: REL-seq absorbs the depth term 38416c_A(K-1-j)
at n_H ((n_♯ + 1)aβ_-log L ≥ 38416·(depth coefficient)), so n_H grows by the factor (6c_U + c_ns)/(2c_U) ≥ 3 against the target.
(Session-4 text had c_f = 2c_U(1 + Δ_sh), i.e. c_A ≈ 6·10⁶c_U; that placement was wrong, see §16.7.) [§17.2 removes the 4c_U and
c_f tilt terms altogether under HW's session-4 law.] In particular a_A ≥ θa_bad: 6θa_bad ≥ θa_bad; λκε_1²/256 ≥ θa_bad because θa_bad ≤ c_prε_1²/24 and
c_pr ≤ 24λκ/256 (true at λ = ½ for κ ≥ 1.19·10⁻⁵ with c_pr = 1/(640·53²) = 5.56248·10⁻⁷; the "5.5625·10⁻⁷" quoted in
REVIEW_RLARGE_V3 is its rounding, p4 E1); a_ns ≥ θa_bad by hypothesis. So HW's
a = min{θa_bad, a_A} = θa_bad is unchanged. **[RPLD4-fix NA-4/K-1]** This puts the whole K12 content into the hypothesis
a_ns ≥ θa_bad of (J-NS^dir); it is not an output.
*Proof.* Pointwise, {S ⊂ D_k} ⊂ ∪_{S'⊂S}E(S'), E(S') := ∩_{Q∈S∖S'}{Q bad, Q ∉ 𝒞} ∩ ∩_{Q∈S'}{Q ∈ 𝒞}, and split S' = S_0 ⊔ S_1 by
G_Q / G^c_Q. Fix (S', S_0, S_1); T := S∖S'. The event ∩_{Q∈S'}(…) is a function F of U_{≤k-1} on the columns of S'. Lemma FT with
this F (and the factor 1{Q ∉ 𝒞} for Q ∈ T, also a function of U_{k-1}, folded into p_K): μ(E) ≤ e^{4c_U‖T‖_sh}·
E_{μ'}[Π_{Q∈T}p_K(Q|U_{k-1})1{Q∉𝒞}·F] ≤ e^{4c_U‖T‖_sh}p_mis^{|T|}μ'(F) (KD). Then F = Π_{S_0}1{Q∈𝒞}1_{G_Q}·Π_{S_1}1{Q∈𝒞}1_{G^c_Q},
and on {Q ∈ 𝒞}, 1 ≤ e^{θY^f_Q}e^{-6θa_badu_k} (CW); (SF-cap)^{A,+} with A = S', A' = S_1 and F_1 := Π_{S_1}1{Q∈𝒞}1_{G^c_Q} gives
μ'(F) ≤ (c_sfe^{-6θa_badu_k})^{|S_0|}e^{c_f‖S_0‖_sh}μ'(F_1), and (J-NS^dir) under μ' ∈ ℛ^A_𝔥 bounds μ'(F_1). The kernel exponent:
u_{k-1} ≥ u_k - R ((F_R)), so p_mis ≤ n_int(1 - λ)^{-3/2}e^{λκε_1²R/256}e^{-λκε_1²u_k/256}. Shadow sums are monotone, so
‖T‖_sh, ‖S_0‖_sh, ‖S_1‖_sh ≤ ‖S‖_sh. Summing over the 3^{|S|} triples: μ(S ⊂ D_k) ≤ e^{c_A‖S‖_sh}Π_{Q∈S}(b_1 + b_2 + b_3) with each
b_i ≤ (C_A/3)e^{-a_Au_k}. ∎
**Level 0.** D_0: a level-0 cube is bad iff an interior plaquette has ||1 - U_0(p)|| ≥ ε_1. There is no kernel; the same Chernoff
with X_Q = u_0Σ_{p⊂int Q}s(U_0(p)) ≥ u_0ε_1²/(2N) ((B)) and the level-0 Wilson moment under μ (HW §6 "Level 0", OPEN) gives
(SDP)^A_0 with a_A^{(0)} = θ_0ε_1²/(2N) ⇐ (LI^U) + (LCR)_0 (§16.7). Not written further. **[RPLD4-fix NA-1]** So the theorem
covers k ≥ 1 only; level 0 (asked by §16.0 T9 "every level k ≥ 0") is a sketch, not proven.
**Status line.** NA-PRICE (i) is an implication: PROVEN-HERE, conditional on (LI^U) [HW], (CLS-min) [SQ], (SF-cap)^{A,+} [node A]
and (J-NS^dir) [node A, new]; k ≥ 1 only. No (H-w′), HIST-sum or (RLF-3′) is used at any level (S-2 check (d): the proof reads levels k - 1, k
only, plus the future through (LI^U)). **[RPLD4-fix NA-3]** ~~It is not derived from (SDP)^A at level k - 1 (LOOP-const
respected).~~ It is not derived from (SDP)^A_{k-1}; the cross-level content is the hypothesis (J-NS^dir), whose trivial and
recursive proofs are LOOP-const (§16.6).

## 16.6 The wall: (J-NS^dir). Proposition WALL: PROVEN-HERE (arithmetic about bounds, not counted)
(J-NS^dir) is the only input of §16.5 in which a returned finer defect appears (CW's Reading). Three facts locate it.
- **(a) The trivial bound reproduces LOOP-const.** μ(Q ∈ 𝒞, G^c_Q) ≤ μ(G^c_Q) ≤ Σ_{x under Q}μ(x ∈ D_{k-1}), fed by (SDP)^A at level
  k - 1, gives the recursion C_A(k)e^{-a_Au_k} ≥ 81C_A(k-1)e^{-a_Au_{k-1}}, i.e. C_A(k) ≥ 81L^{-a_Aβ_+}e^{-a_AR}C_A(k-1): HW Lemma
  LOOP-const with G = 81L^{-a_Aβ_+}e^{-a_AR} > 1 (a_Aβ_+ log L ≈ 10⁻⁸⁶ ≪ log 81). So η = 1 is the LOOP-const case.
- **(b) A contracting recursive form closes the constants but not the union-form shadow allowance.** Suppose instead
  **(J-NS^rec_η)** [RPLD4-fix W-1: per choice function, not with a max]: for every choice function Q ↦ x_Q (x_Q one of the 81
  level-(k-1) cubes under Q), μ(∩_{Q∈S_1}({Q ∈ 𝒞} ∩ {x_Q ∈ D_{k-1}})) ≤ η^{|S_1|}·μ(x_Q ∈ D_{k-1} ∀Q ∈ S_1); the event
  ∩_{S_1}({Q ∈ 𝒞} ∩ G^c_Q) is bounded by the sum over the 81^{|S_1|} choice functions. (With a max over choices no 81 would
  appear and the closing condition would read 3ηe^{aR} < 1; the per-choice form is what gives 243ηe^{aR} < 1.) Then §16.5's proof
  with (SDP)^A at level k - 1 gives, per cube, b_3 ≤ 81ηC_A(k-1)e^{a_AR}e^{-a_Au_k}·(shadow factor), and the constants close
  (C_A(k) ≤ C_A for all k) iff 243ηe^{a_AR} < 1 (check p4 D). But the shadow factor of level k - 1 is e^{c(k-1)‖x(S_1)‖_sh}, and for
  |S| ≥ 2 with S∖S' ≠ ∅ the level-k bound carries e^{4c_U·sh(S∖S')}·e^{c(k-1)·sh(x(S_1))}. Deep shadows of nearby cubes coincide
  (Lemma H-geo (iii): ≤ 38416 cubes per level, independent of n), so in the union form this is ≥ e^{(4c_U + c(k-1))·D} with D the
  common depth term, while the target is e^{c(k)·D}: **c(k) ≥ c(k-1) + 4c_U, linear growth in k.** With per-cube shadow sums the
  recursion closes (the excess sh(x_Q) - sh(Q) ≤ 81 + 2401·32·80·Σ_{m≥1}3^{-m} ≈ 3.07·10⁶ is depth-free and goes into η), but
  Lemma REL-seq consumes (SDP)^A with S = a step animal 𝒟 in the UNION form (the depth term 38416c(K - 1 - j) counted once, HW
  §13.2 (3)); per-cube sums would need aβ_-log L ≥ 38416c per cube, false at a ≈ 10⁻⁸⁶. **So a column recursion, even a
  contracting one, cannot deliver the (SDP)^A that REL-seq consumes, unless (LI^U)'s allowance is depth-free.** (J-NS) must be
  proven non-recursively (the direct form), or (LI^U) must be strengthened to a depth-free allowance (LI^U_loc): H(U) ≤ e^{c_U|S|}H(U').
- **(c) What (J-NS^dir) asserts physically, and its deterministic half.** A returned finer cluster changes the kernel centre of Q
  only through the S4' contours that pass through it. **Lemma DIL-1 (PROVEN-HERE, elementary, not counted).** Let U, U° be
  level-(k-1) fields that differ only on a link set E, and for a level-k link c let f_c(E) be the fraction of the S4' contours
  (σ, y) of c that use a link of E, and ℓ_c(E) := max over contours of the number of E-links on it. Then
  ||M̄_c(U) - M̄_c(U°)|| ≤ f_c(E)ℓ_c(E)max_{e∈E}||U_e - U°_e||, and for SU(2), if r_c(U°) > 0, ||Ŵ_c(U) - Ŵ_c(U°)|| ≤
  2||M̄_c(U) - M̄_c(U°)||/r_c(U°). *Proof.* Contours avoiding E have equal transporters; for the others, telescoping the product
  of unitaries changes it by ≤ ℓ_c·max||U_e - U°_e||; average. SU(2): ||M/r - M°/r°|| ≤ ||M - M°||/r° + ||M||·|1/r - 1/r°| ≤
  2||M - M°||/r° (|r - r°| ≤ ||M - M°||, ||M|| = r). ∎ **[RPLD4-fix W-2, recommended]** As used below, DIL-1 reads the link
  deviation of a field compared with an ARBITRARY U°, which is gauge-dependent (a single plaquette at curvature ε_1 can appear
  as an O(ε_1) deviation on a whole line of links in axial gauge). The gauge-covariant form is Lemma DIL-L (§17.3), with U°
  the kernel-centre completion; the "thin cluster" reading below is superseded by §17.3-§17.4. So a thin cluster (small f_cℓ_c) of link deviation δ moves V^0_P by
  ≤ 8f_*ℓ_*δ/r° (f_*, ℓ_* the maxima over c ∈ ∂P), and cannot make Q ∈ 𝒞 unless δ ≥ r°ε_1/(16f_*ℓ_*) or the completion U° is
  already near-𝒞. When 16f_*ℓ_* < r°, this is a raised threshold δ > ε_1, i.e. a finer defect at a higher price (gain factor
  (r°/(16f_*ℓ_*))² in the exponent). The probabilistic half — that the completion U° can be chosen as the cut-good completion of
  the R-operation (CL^J's W_0 caps) and priced by (SF-cap) jointly with the cluster's own frozen activity — is the content of
  (J-NS^dir) that is not proven here. [inference] For thick clusters (f_c not small) the gain is absent, as for CF.

## 16.7 Theorem NA-PRICE (ii): (SF-cap)^{A,+}. CONDITIONAL (reduction PROVEN-HERE; not counted) | (LI^U), HW §6 main-term reduction
**(LCR)_{k-1}** [node A; small-field; "local coupling response", HW §6, ARGUED there]: for every μ ∈ ℛ^A_𝔥, k ≥ 1, A, A', F as in
(SF-cap)^{A,+}, and every bounded G ≥ 0 that does not read the level-(k-1) links in the columns of A∖A',
  E_{ν^{μ}_{k-1}}[Π_{Q∈A∖A'}exp(λ_fu_{k-1}Σ_{x∈col Q}𝓔^{an}_{k-1,x}(U_{k-1}))1_{G_Q}·F·G] ≤ c_lcr^{|A∖A'|}E_{ν^μ_{k-1}}[F·G],
  λ_f := 24θ(1 + 2Rg_K²) < 1,
with 𝓔^{an}_{k-1,x} the main-term densities of (I_{k-1}^E)″ (HIST §25.6 (a″)), on G_Q (Q's column defect-free).
**Claim.** (LI^U) (with S := the 81|A∖A'| level-(k-1) cubes of the columns of A∖A', at level k - 1) + (LCR)_{k-1} + HW §6's reduction
F^col_Q(U_{k-1}) ≤ Σ_{x∈col Q}𝓔^{an}_{k-1,x}(U_{k-1}) on G_Q [PROVEN given (I_{k-1}^E)'s localisation; uncounted, HW] ⇒ (SF-cap)^{A,+}_θ with
  ~~c_sf := e^{2·81c_U}c_lcr,  c_f := 2·c_U·(1 + Δ_sh)~~ **[RPLD4-fix C-1]** **c_sf := e^{2c_U(81 + Δ_sh)}c_lcr,  c_f := 2c_U**
  (Δ_sh = 3073361: the depth-free excess of the column's shadow over Q's, §16.6 (b), p4 E4). The (LI^U) allowance for S = the
  81|A∖A'| column cubes is c_U(81|A∖A'| + sh(S)) with sh(S) ≤ sh(A∖A') + Δ_sh|A∖A'| (the excess is additive and depth-free, p4
  D2b), so Δ_sh is a per-cube constant and belongs in c_sf, not in the depth coefficient. [§17.2: under HW's session-4 law this
  reduction needs no (LI^U) at all.]
*Proof.* u_k ≤ u_{k-1} + R = u_{k-1}(1 + Rg_{k-1}²) ≤ u_{k-1}(1 + 2Rg_K²) ((F_R); g_{k-1}² ≤ 2g_K²), so
θY^f_Q = 24θu_kF^col_Q ≤ λ_fu_{k-1}F^col_Q ≤ λ_fu_{k-1}Σ_x𝓔^{an}_{k-1,x}. The integrand is a function
of the level-≤(k-1) fields; write μ restricted to U_{≤k-1} as ν^μ_{k-1} tilted by H^μ_{k-1}, and replace H^μ_{k-1} by its value at
the field with the column links of A∖A' set to 1 (two uses of (LI^U), as in FT (2)-(4)); the replaced tilt is a G as in (LCR). ∎
*Status of (LCR).* At level 0 it is the local coupling response of the cut Wilson measure; "OPEN as stated even for the plain
Wilson measure uniformly in u_0" (HW §6). Its Gaussian value (1 - λ_f)^{-dof/2} per column is the ARGUED heuristic (HW §6); the
certified stage-0 small-field package (CE-exp, CE-Q-col, DX-rel) is a representation of the stage-0 integral with
certified CE constants, and it does not contain an inhomogeneous-coupling statement. So c_lcr is not certified; (SF-cap)^{A,+}
stays OPEN, reduced to (LCR) (one named small-field statement, no large-field content: G_Q removes the finer defects, and the
defect-carrying columns are F, which (LCR) only conditions on).

## 16.8 Theorem NA-PRICE (iii): a_ret. Proposition CC (no uniform a_ret on the full cut-good domain) and the chart formula
**Proposition CC (coherent continuation): (a) PROVEN-HERE (elementary, not counted); (b) ARGUED.** SU(2), d = 4, L ≥ 3 odd,
ε_1 ≤ 0.05/L², stage k (HIST §4 indexing: Q a level-(k+1) cube, CL^J's frozen activity r^J_Q(D) = Num/Den). (a) For every
δ ∈ (0, ε_1/8] there is a datum D — U_k cut-good, U_{k+1} off int Q cut-good (every other level-(k+1) cube good), U_{k+2} the
kernel centres — with
  r^J_Q(D) ≥ c_N^{n_int}(δ/16)^{3n_int}·e^{-κ(u_kn_int + 4·8u_{k+1}ℓ_Q²/0.49)δ²/2}·(0.7 - ℓ_Qδ)^{3·8/2},
ℓ_Q := the maximal number of int Q links on one S4' contour of a level-(k+2) link (≤ d(L - 1)/2 + L: the axial path plus
the leg, RS (R1)'s contour shape; ≤ 7 at d = 4, L = 3), and 4·8 counts the ≤ 8 links of C(Q) (HIST §4). At δ = g_k this is ≥ c·g_k^{3n_int}
with c > 0 independent of g. Hence **no bound r^J_Q(D) ≤ Cg^{-p}e^{-a/g²} with a > 0 holds uniformly over cut-good data.**
*Proof.* Proposition CF (HIST §6) with top level k + 2 and θ chosen so that the level-(k+1) (1,2)-plaquettes have ||1 - V_P|| =
ε := ε_1 - δ/8 (possible: θ ≤ L²ε·1.01 ≤ π/6); let x^0 be its level-(k+1) links on int Q, and D its remaining fields. Every
level-(k+1) cube is then good (ε < ε_1), U_k is cut-good (curvature ≤ ε/L²), and every kernel factor of w^J_Q is at its maximum
at x^0 (CF (1)), with M̄ = mS, m ≥ cos(π/4) > 0.7 (CF proof). r^J_Q = P_w(ζ_Q = 1)/P_w(χ_Q = 1) ≥ P_w(ζ_Q = 1), P_w := w/∫w. Upper
bound: ∫w ≤ sup w; the int Q factors are bounded by 1/𝒩(b_c) (b_c fixed by D), and the C(Q) factors by 1/𝒩(κu_{k+1}) (1/𝒩 is
increasing, b ≤ κu). Lower bound on A := {x : ||x_c - x^0_c|| ≤ δ ∀c ∈ int Q, ζ_Q(x) = 1}: the int Q factors are ≥ e^{-κu_kδ²/2}/𝒩(b_c)
(φ ≤ ||x - x^0||²/2); for c' ∈ C(Q) (≤ 8 links) Lemma DIL-1 gives ||M̄_{c'}(x) - M̄_{c'}(x^0)|| ≤ ℓ_Qδ, so r_{c'}(x) ≥ 0.7 - ℓ_Qδ,
1/𝒩(κu_{k+1}r) ≥ r^{3/2}/𝒩(κu_{k+1}) (KS (c) with 1 - λ = r), and φ_{c'} ≤ r(2ℓ_Qδ/0.7)²/2. Haar(A): fix an interior (1,2)-plaquette
P_* and a link c_* of it; rotate x_{c_*} by e^{iφτ} with φ = δ/2 along the axis of the (conjugated) holonomy of P_* (this raises
||1 - V_{P_*}|| by ≥ (δ/2)cos(θ/2) - O(δ²) ≥ 0.45δ), and allow every link (c_* included) to vary in an op-ball of radius δ/16 around
these values: then ||1 - V_{P_*}|| ≥ ε + 0.45δ - 4δ/16 = ε_1 + 0.075δ > ε_1 and ||x_c - x^0_c|| ≤ δ/2 + δ/16 < δ; the Haar measure
of the product of balls is ≥ (c_N(δ/16)³)^{n_int}. Multiply. (CF is on Z⁴; on a torus the same construction holds in any region
not wrapping it, as for INH.) ∎
(b) [ARGUED] At fixed V equal to the CF level-(k+1) field outside int Q, the sea law ⟨·⟩_V of (SC)_k concentrates near the CF
preimage (the background identification of PLD §15.3, ARGUED there), so the sea-averaged activity is ≥ c'g^{p'} as well, and
**(SC2)'s bound cannot hold with a uniform a on the whole cut-good domain 𝒱_{k+1}**; it can hold on the GT-lat chart
{ε_2(V) ≤ r_1}, where the coherent continuation stays below ε_1 by a margin. ~~This is outcome **(NP-F2), met.**~~
**[RPLD4-fix CC-2]** Relabelled: **frozen counterexample to (SF-irr)'s off-chart clause PROVEN; sea-averaged ARGUED; (SC)_k
unaffected** (NP-F2 as pre-stated, "no uniform a_ret on the V-domain (SC)_k is stated on", is NOT met: (SC)_k is stated sup over
the chart). It does not
contradict PLD §9.4, whose (SC2) is stated "sup_{chart}"; it contradicts (SF-irr)_{k+1}'s clause "bounded by K elsewhere in the
cut-good domain" with K ∝ e^{-a/g²}, i.e. RLARGE (RLF-2)'s reading of the returned remainders off the chart.
**[RPLD4-fix CC-1, recommended]** The lower bound of (a) is polynomial (g^{648} at n_int = 216), so it beats Cg^{-p}e^{-a/g²}
only when g² ≲ a/((648 + p)ln(1/g)): ≈ 3·10⁻⁹⁶ for a = a_ret. It bites at the operating point (g² ≤ 2.5·10⁻¹⁵² from DX′); at
g² = 10⁻⁹⁴ it would not.

**a_ret on the chart (the explicit formula; per-cube prices PROVEN as cited, the expansion (SC)_k itself still HYPOTHESIS).**
**[RPLD4-fix A-1, recommended]** a_ret below is "the per-cube price entering (SC)_k's expansion, conditional on (SC)_k"; "PROVEN
as cited" applies only to the three component prices (α)-(γ). On the
chart, a returned configuration at stage k is one of: (α) a quiet, collar-good bad cluster: CL^J (c), exponent
a_J = κε_1²/(2048N) per cube (HIST §4, PROVEN, CONFIRMED by REVIEW_HIST_S1); (β) a non-quiet sea cube (a level-k plaquette ≥ η_q
under the cube): at fixed chart V, PLD-desc with τ = η_q and Lemma HS-net, exponent a_fl(η_q/2) = 49η_q²/(1024σ_fl²) per plaquette,
valid when τ ≥ 2τ_bg on the chart, i.e. **r_ch := max_{P near A}||X_P(V)|| ≤ L²η_q/(4C_I)** ((BG)_k's curvature clause at
near-trivial V, see §16.9); (γ) a collar-mismatch cube (σ_Q = 0 through its coarse-link clause): Lemma KN at t = ε_loc/4,
exponent κε_loc²/(64N) (PLD-SG (ii)). So
  **a_ret := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}**  (per cube; (SC)_k's cluster expansion may lose a fixed factor),
in u_k-units, on the chart {ε_2(V) ≤ min(r_1, r_ch)}. Certified inputs: σ_fl² = 16(1 + O(α_*))/λ_min with the level-0 gap λ_min
of the session-23 class, λ_min ≥ 3.17·10⁻³ (RLARGE §0, as quoted there; SF Proposition CI-0 gives λ_min(Õ_0) ≥ 4.23·10⁻³), so
σ_fl² ≤ 5.05·10³(1 + O(α_*)) (the Gaussian part only: REVIEW_PLD_S3 L0-1 and SG-F2, (G0-1)-(G0-4) still OPEN); η_q = min{ε_1/(2L²),
ε_1/(256NA_d), δ_0/A_d} = ε_1/4608 at N = 2, L = 3 when δ_0/A_d does not bind. **The binding entry is (β):** a_ret ≈ 4.47·10⁻¹³ε_1²
≈ 8.0·10⁻⁷·a_bad (check p4 E), ≈ 2·10⁻⁹¹ at ε_1 = 6.7·10⁻⁴⁰. Levels k ≥ 1 need σ_fl at level k (N5 level-uniformity, BFT).
**a_ret versus a_A (K12).** On the route of §16.5, a_A is produced forward (FT + KD + CW + (SF-cap) + (J-NS)) and does not pass
through the sea activities; ~~so REVIEW_RLARGE_V3's inferred requirement "a_ret − (tilt allowance) ≥ θa_bad" is **not needed**.~~
**[RPLD4-fix K-1]** but that route is conditional on (J-NS^dir) with a_ns ≥ θa_bad, which is the price of a coarse centre over
a returned defect; Proposition CC shows a returned defect has no exponential price of its own on cut-good data. So **K12 is
reduced to (EG): an energy-graded in-step price of centre-moving returned clusters. Without (EG), θ ≤ a_ret/a_bad ≈ 8·10⁻⁷**
(n_H × ≈ 5·10⁴). Plan constants with θ ≈ 8·10⁻⁷ until (EG) is in hand. a_ret
enters only (RLF-0)/(RLF-δ) (|c̄_0| + |δβ_k| ≤ Cg^{-p}e^{-a_ret/g²} ≤ g⁶), where any a_ret > 0 suffices; it sets the coupling
ceiling g_K² ≲ a_ret/((12 + p)log(1/g_K)) ≈ 10⁻⁹⁴ (check p4 E), below the n_H ceiling 2.7·10⁻⁹¹ (REVIEW_RLARGE_V3 Part 4) and far
above DX′'s 2.5·10⁻¹⁵²/C_Ω. Had K12's requirement been imposed, θ would drop to ≈ 8·10⁻⁷ and n_H would grow by ≈ 5·10⁴.

## 16.9 T10: (BG)_k and the critical path (K12), decided
- **Not through (SDP)^A.** §16.5 uses no background map: the coherent background is priced by (CLS-min) through Lemma CW.
  (REG-min) remains (BG)_k's cone-local sup form on (CLS-min)'s side (SQ, row 9), unchanged.
- **Yes, through a_ret, in a restricted form.** (β) needs B_V = ∅ in PLD-desc on the chart: the curvature clause of (BG)_k
  (|X(𝔟(V))| ≤ C_IL^{-2}max||X_P(V)||) and the localisation radius R_bg (the domain 𝒱^{sf}(A) of (SG^{fl})), **only at near-trivial
  V** (curvature ≤ r_ch). There 𝔟(V) is the implicit-function perturbation of the trivial background, so this restricted (BG)_k
  follows from the fluctuation operator at the trivial background (gap and exponential decay) plus analyticity [inference: the
  trivial-background operator is LINEAR_PACKAGE's, and BFT's trivial-background clauses are the ones REVIEW_BFT_A_S5 calls
  complete for the soft-RG source class at m = 0; not checked here]. Full BFT-3 on the whole cut-good domain is **not** needed,
  and would not help: Proposition CC shows that no uniform a_ret exists there in any case.
- **Off the chart** the returned remainders need a different admissibility notion than (SF-irr)'s uniform K (e.g. a weighted
  bound r ≤ e^{-a u}e^{wuℰ(V)} absorbed by the level-(k+1) main term [inference, not proven]); this is a node-A norm decision of
  the same kind as S4-5, recorded as **(SF-irr^off)** for the owner.

## 16.10 Check p4 (criteria checks/p4_criteria.md 10:30:39 UTC, md5 ccef5a1d…, before the script; script checks/p4_pld.py
10:31:57 UTC; output checks/p4_out.txt; record checks/p4_time.txt)
- One run under the numeric lock (acquired 10:33:57 after a wait, released 10:34:15 by one rmdir); load 2.95; nice 10; BLAS threads 1;
  17.5 s, 69 MB; exit 0; no process left.
- **SUMMARY: FAIL: E1; all other criteria PASS.** E1 failed as written because the criterion compared the exact c_pr = 1/(640·53²)
  = 5.562477·10⁻⁷ with the rounded quoted value 5.5625·10⁻⁷ at 1e-10 relative tolerance (difference 4.1·10⁻⁶). This is a criterion
  defect, disclosed, not a mathematical failure; nothing was re-run ~~or edited~~ **[RPLD4-fix P-1]**: no criterion and no script
  was edited; PLD.md l.1411-1412 was edited after the run to quote the exact c_pr (PLD_LOG l.67).
- Rigorous: A1 (quadrature: the KS (c) Chernoff tail used in Lemma KD holds on the grid; max exact/bound 0.65), A2, A3, B1, B2 (sampled
  identities/inequalities, 0 violations), D1 (recursion arithmetic: bounded iff 243ηe^{aR} ≤ 1; η = 1 gives 1.7·10⁹⁵⁴ at k = 400,
  the LOOP-const side), D2a/b/d (exact shadow sets in Z⁴: monotonicity sh_m(x) ⊇ sh_m(Q), excess 256 ≤ Δ_sh = 3073361, H-geo (iii)),
  E2-E5. Negative controls: A1n (the prefactor-free tail bound fails), B1n (factor 1 in the polar Lipschitz bound fails, 2847 times),
  C1n (centre 10σ below threshold: 0 hits in 10⁵). Evidential: C1/C2 (4-link toy of Proposition CC (a): P(bad) = 0.516 at a centre
  δ/8 below threshold, illustrative ε_1 = 0.02), D2c.
- Numbers used in §16.8: σ_fl² = 5047.3 (λ_min = 3.17·10⁻³) / 3782.5 (4.23·10⁻³); a_fl/ε_1² = 4.465·10⁻¹³ / 5.958·10⁻¹³; a_J/ε_1² =
  2.441·10⁻⁴; a_KN/ε_1² = 1.460·10⁻⁴; a_ret/a_bad = 8.03·10⁻⁷ / 1.07·10⁻⁶; a_ret(ε_1 = 6.7·10⁻⁴⁰) = 2.00·10⁻⁹¹; (RLF-δ) ceilings
  g_K² ∈ [7.6·10⁻⁹⁵, 1.03·10⁻⁹⁴]; a_A/a_bad → 0.25 as θ ↑ 1/24 (the 6θa_bad entry binds).

## 16.11 Outcome against the pre-stated targets (§16.0) and tally
- **[RPLD4-fix ARCH-1] T9 (i): NP-F1 MET** (raw-law column pricing = LOOP-const in a new guise, Proposition WALL), **with
  NA-PRICE (i) kept as a valid conditional implication** (k ≥ 1). "PARTIAL SUCCESS" is withdrawn: (J-NS^dir) is two-level,
  probabilistic and large-field, and is HW §15.3's open non-saturating split renamed; it fails the pre-stated bar of §16.0
  (l.1317-1319). Cause, recorded: §16.0's list of allowed inputs (l.1314-1315) omitted node A's R-operated representation
  ((I_{k-1}^E)″ two-field form, (W1-ret′^J)_{k-1} (c), (SC)_{k-1}, R1^J's gas), so NP-F1 was the outcome actually met with
  those inputs. Proposed node-A route (REVIEW_PLD_S4 Part 3), taken up in §17: (LCR^punct)_{k-1} + (EG)_{k-1} + lasso DIL-1.
  NP-F2: see the CC-2 relabel below. The struck session-4 line follows.
- ~~**T9: PARTIAL SUCCESS** (the pre-stated partial outcome), with **(NP-F2) MET** and an (NP-F3)-type finding for recursive proofs.~~
  - (i) **(SDP)^A: CONDITIONAL** ⇐ (LI^U) + (CLS-min) + (SF-cap)^{A,+}_θ + **(J-NS^dir)** (Theorem NA-PRICE (i), §16.5; implication
    PROVEN-HERE), with a_A = min{λκε_1²/256, 6θa_bad, a_ns} ≥ θa_bad, C_A = 3max{n_int(1 - λ)^{-3/2}e^{λκε_1²R/256}, c_sf, C_ns},
    c_A = 4c_U + c_f + c_ns [RPLD4-fix C-1: = 6c_U + c_ns ≠ the pre-stated 2c_U; n_H × ≥ 3], uniform in k, under the one law μ ∈ ℛ^A_𝔥 of RLARGE v3 §3. **The ONE new hypothesis is (J-NS^dir)**:
    the price of a level-k cube whose kernel centre is bad (or degenerate) while its finer column holds a returned defect. It is
    of a different kind than (SDP)^A in that it concerns only the saturated case and only the centre event (a level-(k-1)
    function), and it is sufficient; it is not shown to be strictly weaker in logical strength.
  - The exact wall (Proposition WALL): η = 1 in (J-NS) is LOOP-const; a contracting recursion closes the constants iff
    243ηe^{aR} < 1 but compounds (LI^U)'s union-form shadow allowance (c(k) ≥ c(k-1) + 4c_U), which Lemma REL-seq cannot afford.
    **Minimal missing input:** (J-NS^dir), or alternatively (J-NS^rec_η) with 243ηe^{aR} < 1 PLUS a depth-free (LI^U_loc). Its
    deterministic half is Lemma DIL-1 (proven); the open half is a joint (two-level) activity bound for a returned cluster under
    a bad coarse centre, i.e. HW §15.3's "non-saturating window split", now with a precise statement and owner (node A).
  - (ii) **(SF-cap)^{A,+}: CONDITIONAL** ⇐ (LI^U) + (LCR)_{k-1} + HW §6's main-term reduction (§16.7); c_sf = ~~e^{162c_U}c_lcr~~ e^{2c_U(81+Δ_sh)}c_lcr, c_f = 2c_U [RPLD4-fix C-1];
    c_lcr not certified (the certified stage-0 package contains no inhomogeneous-coupling statement).
  - (iii) **a_ret = min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}** on the chart {ε_2(V) ≤ min(r_1, L²η_q/(4C_I))}; the binding
    entry is the (SG^{fl}) fluctuation price at η_q/2: a_ret ≈ 8.0·10⁻⁷a_bad (λ_min = 3.17·10⁻³; Gaussian part of σ_fl only).
    **Proposition CC [RPLD4-fix CC-2: not "(NP-F2)"; frozen counterexample to (SF-irr)'s off-chart clause PROVEN, sea-averaged
    ARGUED, (SC)_k unaffected]: no uniform a_ret > 0 on the full cut-good domain** (frozen part PROVEN-HERE, sea part ARGUED); so
    (SF-irr)'s off-chart clause / (RLF-2)'s off-chart reading needs a node-A decision (SF-irr^off).
  - (iv) Law: Lemma FT (kernel events, cost e^{4c_U‖T‖_sh}, union form, ~~ONE application~~ **[RPLD4-fix FT-1] (LI^U) on the set
    T, used twice (e^{2c_T})**) and Lemma FV-law (fixed-V statements carry
    no tilt) give the exact conversions; PLD's μ^+_{𝔥,ω} enters only a_ret, where no conversion is needed.
  - Not-success items avoided: no exponent depends on k, K, T or 𝔥; no fixed-V price of a bad coarse cube; no column induction is
    claimed uniform (it is shown not to close in the union shadow form); no (H-w′), HIST-sum or (RLF-3′) is used.
- **T10: (BG)_k part DECIDED; K12 part NOT decided [RPLD4-fix K-1].** (BG)_k is **not** on (SDP)^A's path (Lemma CW prices the coherent background through (CLS-min)). It **is** on
  a_ret's path in a restricted form: its curvature clause C_I and radius R_bg at near-trivial V only (§16.9), which is expected to
  follow from the trivial-background fluctuation operator [inference]. ~~K12's inferred requirement a_ret − (tilt) ≥ θa_bad is not
  needed on this route (a_A is produced forward); imposing it would cost θ ≈ 8·10⁻⁷.~~ **[RPLD4-fix K-1]** K12 is NOT decided: it
  is reduced to (EG), an energy-graded in-step price of centre-moving returned clusters; without (EG), θ ≤ a_ret/a_bad ≈ 8·10⁻⁷.
- **T11: MET with one disclosed criterion defect** (E1, a rounded input compared at 1e-10).
- **PROVEN-HERE [E4], counted (2, unreviewed):** (1) Lemma FT with Lemma KD (law conversion + kernel dichotomy); (2) Theorem
  NA-PRICE (i) as an implication, with Lemma CW (CONDITIONAL ⇐ (CLS-min)). Not counted: Lemma FV-law, Lemma DIL-1, Proposition
  WALL (arithmetic about bounds), Proposition CC (a) (elementary; (b) ARGUED), the (SF-cap) reduction of §16.7.
- **New named items:** (J-NS^dir) [node A, P — the wall], (J-NS^rec_η), (LI^U_loc) [HW, alternative], (SF-cap)^{A,+} (the written-out
  form of HW's (SF-cap)^A), (LCR)_k [node A, small-field], (SF-irr^off) [node A norm decision]. **Tally proposal:** +2 PROVEN-HERE
  (unreviewed); 0 OPEN items closed; rows 10b and 10c of RLARGE §4.2 are reduced to (J-NS^dir) and (LCR); ~~K12 decided~~ K12
  reduced to (EG) [RPLD4-fix K-1]. Reviewed (REVIEW_PLD_S4): [E4] (1) CONFIRMED (FT-1 cosmetic); [E4] (2) CONFIRMED-WITH-FIX
  (C-1, CW-1, NA-3); 0 GAP, 0 WRONG among counted items; the outcome labels were WRONG (fixed: ARCH-1, K-1, CC-2).

## 16.12 Proposed changes for other owners (not made here)
- **RLARGE (integrator).** Row 10b: (SDP)^A ⇐ (LI^U) + (CLS-min) + (SF-cap)^{A,+} + (J-NS^dir) (PLD §16.5); add row (J-NS^dir) [node A, P]
  and row (LCR)_k [node A]; row 10c: ⇐ (LI^U) + (LCR) (PLD §16.7). Row 2 / K12: a_ret := PLD §16.8's formula on the chart; ~~strike the
  requirement "a_ret − (tilt allowance) ≥ θa_bad" for the HW route~~ **[RPLD4-fix K-1] (proposal withdrawn: K12 is reduced to
  (EG), not struck)**. Row 8: (BG)_k load-bearing only in the restricted chart form
  for a_ret (§16.9). (RLF-2): restrict "admissible irrelevant polymer … bounded elsewhere in the cut-good domain" to the chart, and
  record (SF-irr^off) with Proposition CC. Check (a): "the tilt enters (SDP)^A only through (LI^U), ~~applied once~~ [RPLD4-fix FT-1:
  used twice on the set T], at the top kernel
  event (Lemma FT)". Check (d) (REVIEW_RLARGE_V3 S-2): §16.5 reads levels k - 1, k and the future only through (LI^U).
  [All row proposals of this bullet are superseded by §17.8.]
- **HW (lane H).** (LI^U) as consumed here: the union-form allowance is affordable for ~~ONE application~~ [RPLD4-fix FT-1: one use
  per cube of S, i.e. (LI^U) on the set T used twice, e^{2c_T}] (Lemma FT); any
  recursive proof of (J-NS) needs the depth-free (LI^U_loc) (§16.6 (b)). The family ℛ^A_𝔥 (closure under DECL) is the one Lemma FT
  needs (LI^U) on. **[RPLD4-fix C-2, recommended]** HW's form of (SF-cap) "with c_f = 0" is not deliverable through (LI^U):
  HW's CAP-dec must carry e^{c_f‖·‖_sh} (REVIEW_RLARGE_V3 S-1). [Superseded by §17.2: under HW's session-4 law no (LI^U) is used
  and c_f = 0 is delivered exactly.]
- **Node A / SF.** (LCR)_k is the small-field statement behind (SF-cap); (J-NS^dir) is the large-field statement; the certified
  stage-0 package (CE-exp, CE-Q-col, DX-rel) enters neither directly. σ_fl at levels ≥ 1 (for a_ret) needs N5 level-uniformity.

# Session 5 (2026-10-28, lane E)

Binding input: REVIEW_PLD_S4.md (md5 of PLD.md it reviewed: def1982d…; 8 binding fixes). Read for this session (read-only):
REVIEW_PLD_S4 (all); PLD.md §9, §16; PLD_LOG.md; RLARGE.md v3 §1.2, §2-§4.2, App. A §6 (Lemma RS); HW.md §4 (tower energies, TE),
§15 (SAT, CAP-dec), §20-§28 (Lemma TILT, FP, NR, Theorem LI^U-0, Cor. LI-0, Prop. LI-pw, REL-boot, TEL-f, (SDP)^{A,far},
(SF-cap)^{A,far}, (E1)/(E2), (CRC-1)); REVIEW_HW_S2 §5; HIST §4 (CL^J), §5 (R1^J, R1_Λ); SF §6.1 (CE-exp statements), §12.1
(CE-Q-col statement); PROOF S4/S4' (l.587-600, the contour family).

## 17.0 PRE-STATED (session 5) — statements only (written before any session-5 derivation, before any [RPLD4-fix] edit and
before checks/p5_criteria.md)

**T12 (the binding fixes).** Apply REVIEW_PLD_S4's eight binding fixes in place in §16, each tagged [RPLD4-fix <name>]: ARCH-1
(T9 (i) relabelled NP-F1 MET, the implication kept; "PARTIAL SUCCESS" withdrawn; §16.0's omission of the R-operated
representation recorded), NA-3, CW-1, C-1/NA-2, W-1, K-1, CC-2, FT-1; and the recommended ones (W-2 pointer, FV-1, NA-1, A-1,
CC-1, C-2, P-1). No conclusion of §16 is strengthened by these edits.

**T13 (NA-PRICE^E: (SDP)^A rebuilt on the extracted representation; the target).** Setting of §16 (SU(2); bad-only,
history-independent defects; (F_R) with g_K² ≤ 1/(2R); Q a level-k cube, k ≥ 1, finer field U_{k-1}). Laws: the ones HW's
session-4 route consumes (HW §24.2-§24.3): for an admissible 𝔥, A ⊂ 𝒰_{k+1} and S a set of level-k cubes in the columns of A,
the weighted past law ν = ν^{(k),w}_k (w a bounded function of U_k on L^far_k(𝔥)), and whatever declared/conditioned versions of
it the proof needs (to be named exactly). Deliver, with all quantifiers:
- (a) **the law conversion**: the price of the kernel event of S under ν, with its exact cost in the per-level slice
  s_k(𝔥) := Σ_{(j,𝒟), j≤k}|sh_k(𝒟)| (HW §24.3), or a proof that it is free; whether (LI^U) is consumed at all;
- (b) **piece (1), small field**: the moment of the coarse centre's column energy on columns from which the returned finer
  clusters are removed (punctured / completed columns), proven from SF's certified package (CE-exp, CE-Q-col) where it
  applies, else reduced to one named small-field statement (LCR^punct)-type, stated exactly;
- (c) **piece (2), large field**: an energy-graded price for returned clusters that move the coarse centre, from CW +
  (CLS-min) + the kernel (KS (c)), proven where possible, else reduced to one named statement (EG)-type, stated exactly;
- (d) **piece (3)**: a gauge-covariant ("lasso") form of DIL-1, proven, with the dilution constant made explicit;
- (e) **the interfaces**: (SDP)^A, (SF-cap)^A and a_ret written in the form RLARGE v3 §3.3 and HW TEL-f / §24.3 consume
  ((SDP)^{A,far}, (SF-cap)^{A,far}, allowance in the slice s_k(𝔥), a_A ≥ θa_bad or the θ it forces), with a_A, C_A, c_A explicit.
- **Success:** (SDP)^{A,far} at every level k ≥ 1 PROVEN-HERE conditional only on (CLS-min) and named small-field statements of
  the kind of (b) (no hypothesis containing a level-(k-1) defect probability or a large-field event), constants explicit and
  independent of g, K, T, k, 𝔥, no column induction.
- **Partial success:** as above but with ONE further named hypothesis that is single-level and either deterministic,
  small-field, or a kernel/energy statement at one level (not a two-level probability), shown sufficient; constants explicit
  modulo it.
- **Valid failure outcomes:** (NP-F1′) every argument from the allowed inputs that prices the coarse centre over a returned
  finer defect re-creates LOOP-const (the exact mechanism named, with the step where the recursion enters); (NP-F4) the
  extracted-representation route needs a statement about the actual (un-R-operated) finer field that is of the same kind as
  (SDP)^A one level down (named, with the reason the R-operated variable does not suffice); (NP-F5) the dilution constant of
  the S4' centre map for a defect in an endpoint block is not < 1/2 (computed), so "diluted / thin" clusters do not exist in
  the needed sense and piece (1) is empty for them.
- **Not success:** an exponent or constant depending on k, K, T or 𝔥; a fixed-V price of a bad coarse cube; a recursion over
  levels presented as uniform without a contraction factor and a check that no allowance compounds; any use of (H-w′),
  HIST-sum or (RLF-3′) at levels ≥ k; any input that is (J-NS^dir) renamed.
- Inputs allowed: those of §16.0 PLUS the R-operated representation (RLARGE v3 §4.1 (I_{k-1}^E)″ (d″), HIST §4 CL^J (a)-(e),
  §5 R1^J / R1_Λ, PLD §9 W1R / (SC) / (SF-irr) as named hypotheses), HW §21-§24 (Lemma TILT, FP, NR, Theorem LI^U-0, Cor. LI-0,
  TEL-f) and Lemma RS (RLARGE App. A §6). Uniform in k.

**T14 (check p5; criteria file checks/p5_criteria.md before checks/p5_*.py).** (A) Exact/certified arithmetic for every
explicit constant of T13. (B) A computation, for the actual S4' family (PROOF S4': all d! orders, all y ∈ B(X), uniform mean)
at d = 4, L = 3, of the linearised (abelian) response of a coarse centre plaquette to a link perturbation supported in the
interior links of one endpoint block: the per-link weights and the dilution constants in sup-curvature and ℓ²-curvature form,
with a negative control (a perturbation known to shift the centre with weight 1, or a gauge perturbation known to give 0).
(C) Sampled SU(2) tests of every new elementary inequality, with a negative control. Informational where not exact.

# Session 5 derivations (written after §17.0, after the [RPLD4-fix] edits and after the check p5 ran; from 11:36 UTC)

Order disclosure: checks/p5_criteria.md (11:30:24 UTC) and the p5 run (11:32:22-11:32:27 UTC) came BEFORE this text; the
derivations below existed as an unwritten sketch when the criteria were fixed (p5_criteria.md "Order disclosure"). §17.4 (c)-(d)
and §17.5 use the p5 B numbers.

## 17.1 T12: the binding fixes (record)
Applied in place in §16, tagged [RPLD4-fix …]: CW-1 (§16.4 Reading), C-1/NA-2 (§16.5 c_A, §16.7 c_sf/c_f, §16.11 (i)-(ii)), NA-4/K-1
(§16.5), NA-1 and NA-3 (§16.5 level 0 and status line), W-1 ((J-NS^rec_η) per choice function, §16.6 (b)), W-2 pointer (§16.6 (c)),
FV-1 (§16.2), CC-2 and CC-1 (§16.8), A-1 (§16.8), K-1 (§16.8, §16.11 T10, §16.12), P-1 (§16.10), ARCH-1 (§16.11 T9: **NP-F1 MET,
the implication NA-PRICE (i) kept**, "PARTIAL SUCCESS" withdrawn, §16.0's omitted input recorded), FT-1 (§16.11 (iv), §16.12),
C-2 (§16.12). Every edit weakens or corrects a session-4 claim; none strengthens one.

## 17.2 T13 (a): the law conversion is exact on HW's route. Lemmas GEO, FT^far, COL-DEC: PROVEN-HERE (counted, one item)
**The consumed laws (HW §24.2-§24.3, Cor. LI-0 (b)).** For an admissible 𝔥 and a level k, ν^{(k)}_k is the past law of levels ≤ k:
density ∝ e^{-S_0}Π_{i<k}K_iΠ_{j≤k}1_{R(𝔥),j}Π_{k'<k}Φ_{k'} (Φ_{k'} = Π_{Q″∈𝒰_{k'+1}}e^{θmin{π_{Q″},Y^f_{Q″}}} reads U_{k'} on the links with
both endpoints in the level-k' column of Q″). For a link set L_G and a bounded G ≥ 0 that is a function of U_k on L_G, put
ν_G := G·ν^{(k)}_k/E[G]. HW's (E1) law is ν_w with L_w = L^far_k(𝔥). Notation (PLD convention, Q a level-k cube): for a set S of
level-k cubes, X_k(S) := the level-k links with an endpoint at a site of a cube of S (ℓ(S) = interior links, plus the crossing
links); L^∂_{k-1}(S) := the level-(k-1) links with an endpoint in a level-(k-1) cube under a cube of S.
**Standing condition (C_S):** S ∩ 𝒰_k = ∅, and S lies in the level-k part of the columns of 𝒰_m for some m > k. (By DJ and H-nest
(iii), REVIEW_HW_S2 §5.4, a history cube's column lies in the small-field regions of all finer levels, so (C_S) holds for HW's
S and, one level down, for every set of level-(k-1) cubes under S.)

**Lemma GEO.** (i) A level-k link reads U_{k-1} on a link of L^∂_{k-1}(S) only if it lies in X_k(S). (ii) If S is in the columns of
A ⊂ 𝒰_{k+1}, then X_k(S) ∩ L^far_k(𝔥) = ∅. (iii) With S declared at level k (R′ := R(𝔥) with S added to the level-k defects;
HW Lemma DECL), 1_{R′,k} reads no link of X_k(S). (iv) Under (C_S), Φ_{k-1} reads no link of L^∂_{k-1}(S).
*Proof.* (i) A level-k link c reads a level-(k-1) link only if both its endpoints lie in c's two endpoint blocks (HIST l.964);
a link of L^∂(S) has an endpoint in a block b under some Q ∈ S, so b is an endpoint block of c, i.e. c has an endpoint at the
site b of Q. (ii) The endpoint cubes of a link of X_k(S) are Q ∈ S and Q itself or a face neighbour Q′; π(Q) ∈ A ⊂ 𝒰_{k+1} and
π(Q′) ∈ N_1(π(Q)) (|⌊u/L⌋ - ⌊v/L⌋| ≤ 1 for |u - v| ≤ 1), so both lie in N_1(𝒰_{k+1}) ⊂ A_{k+1}(𝔥), and a far link needs an
endpoint cube x with π(x) ∈ S^{(k+1)}(𝔥) = all ∖ A_{k+1}(𝔥). (iii) Bad-only defects: 1_{R′,k} reads ζ_{Q′} only for undeclared
Q′ ∈ S^{(k)}(𝔥), i.e. U_k on ℓ(Q′); ℓ(Q′) ∩ X_k(S) = ∅ for Q′ ∉ S (sites are partitioned among cubes), and crossing links are
interior to no cube. (iv) Φ_{k-1} reads links with both endpoints in the level-(k-1) column of some Q″ ∈ 𝒰_k; Q″ ∉ S, so no such
link has an endpoint under a cube of S. ∎

**Lemma FT^far (kernel events, exact).** Let k ≥ 1, S satisfy (C_S), ν = ν_G with L_G ∩ X_k(S) = ∅, ν′ := ν_G with S declared at
level k, and F ≥ 0 bounded measurable in (U_0, …, U_{k-1}). Then
  E_ν[1{S ⊂ D_k}·F] ≤ E_{ν′}[Π_{Q∈S}p_K(Q | U_{k-1})·F]   (p_K as in §16.1).
*Proof.* On {S ⊂ D_k}, 1_{R,k} = 1_{R′,k} (declared cubes count as defects) and 1_{R′} ≤ 1_R pointwise (HW (m1)), so the
numerator of E_ν[1{S ⊂ D_k}F] equals that of E_{ν′}[1{S ⊂ D_k}F] and Z_{ν′} ≤ Z_ν. Under ν′, given (U_0, …, U_{k-1}) and U_k off
ℓ(S), the only factors reading U_k on ℓ(S) are the kernel factors Π_{c∈ℓ(S)}k_c (GEO (iii); G does not read X_k(S) ⊃ ℓ(S); Φ_{k′},
k′ < k, read levels < k). So ℓ(S) has the product density Π_ck_c(·; M̄_c(U_{k-1})), ζ_Q reads only ℓ(Q), and integrating ℓ(S)
gives Π_Qp_K(Q | U_{k-1}) exactly (Lemma TD). ∎ **No (LI^U), no shadow allowance: c_T = 0.**

**Lemma COL-DEC (the coarse tilt does not read the defect columns).** In FT^far's setting, the marginal of ν′ on (U_0, …, U_{k-1})
is G′·ν^{(k-1)}_{k-1}/E[G′] with G′ := Φ_{k-1}·H′, H′(U_{k-1}) := ∫K_{k-1}(U_k; U_{k-1})1_{R′,k}(U_k)G(U_k)dU_k, and **G′ does not read
U_{k-1} on L^∂_{k-1}(S)**. Consequently, given (U_0, …, U_{k-2}) and U_{k-1} off L^∂_{k-1}(S), the law of U_{k-1} on L^∂_{k-1}(S) under
ν′ is ∝ Π_{e∈L^∂(S)}k^{(k-2)}_e(U_{k-1}(e); M̄_e(U_{k-2}))·1_{R,k-1}(U_{k-1}) (k ≥ 2): the product kernel times the level-(k-1) constraint.
*Proof.* H′ = ∫Π_ck_c·1_{R′,k}G dU_k; 1_{R′,k}G does not read X_k(S) (GEO (iii) and the hypothesis on L_G), so the links of X_k(S)
integrate out (∫k_c = 1); the remaining k_c, c ∉ X_k(S), do not read L^∂(S) (GEO (i)). Φ_{k-1}: GEO (iv). The other factors of
ν^{(k-1)}_{k-1} reading U_{k-1} are K_{k-2} (a product over links) and 1_{R,k-1}. ∎

**Corollary LAW (what this removes; not counted separately).**
- (a) Session 4's Lemma FT holds on HW's route with e^{4c_T} replaced by 1: the instance of (LI^U) it used holds exactly there.
  [Note: S's cubes are constrained at level k in general, i.e. this is the case of HW Proposition LI-pw (pointwise (LI^U) is
  false on constrained columns); declaring S is what makes it exact: after declaration nothing coarser reads ℓ(S).]
- (b) §16.7's reduction becomes exact: under ν′, (SF-cap)^{A,+} on S_0 ⊂ S (F a function of the other columns) is (LCR)_{k-1} in
  the G′-form of §16.7 ("G does not read the column links"), with **c_sf = c_lcr, c_f = 0**. The same holds for HW's own
  (SF-cap)^{A,far} on history columns (G = w, Cor. LI-0 (b)).
- (c) **The obstruction of Proposition WALL (b) is removed.** Every recursive use of the argument one level down (cubes x under
  S, laws of the form G′·ν^{(k-1)}_{k-1}) stays inside the same family with L_{G′} ∩ X_{k-1}(x-set) = ∅ (COL-DEC; (C_S) for the
  x-set), and carries no allowance. So a contracting column recursion has level-uniform constants iff 324ηe^{aR} ≤ 1 (§17.4,
  Prop. CD (b); 243 with §16.6's three branches), with no growth c(k) ≥ c(k-1) +
  4c_U: there is no c_U on this route.
- (d) The S-4 uniformity (REVIEW_RLARGE_V3) is reduced to: uniformity over declarations at levels k and k-1 inside the columns of
  S (finitely many patterns, all inside the proof).

## 17.3 T13 (d), piece (3): the gauge-covariant DIL-1. Lemma DIL-L: PROVEN-HERE (counted with MD, §17.4)
S4' family Γ_c of a level-k link c (PROOF S4′: all d! axis orders σ and all y in the first endpoint block, uniform mean),
M̄_c(U) := |Γ_c|^{-1}Σ_{(σ,y)}T^σ_y(U) (the arithmetic mean of D4-norm). f_c(e) := |Γ_c|^{-1}Σ_{(σ,y)}(number of traversals of e by
T^σ_y); F_c := Σ_ef_c(e)²; F_* := max_cF_c.
**Claim.** (i) For level-(k-1) fields U, U°: ||M̄_c(U) - M̄_c(U°)|| ≤ Σ_ef_c(e)||U_e - U°_e|| ≤ (F_c·Σ_{e:f_c(e)>0}||U_e - U°_e||²)^{1/2}.
(ii) **Kernel-centre completion.** Let E be a set of level-(k-1) links, U° := U off E and U°_e := Ŵ_e := W_0(M̄_e(U_{k-2})) on E, and
δ_e := ||U_e - Ŵ_e||. Then δ_e is invariant under every chain gauge transformation (U_{k-1} and the kernel centres transform by
the same h(x_e)·h(y_e)^{-1}), and for SU(2) with r_e := ||M̄_e(U_{k-2})||: δ_e² = 2φ_e/r_e, φ_e := φ_{M̄_e}(U_e) the kernel exponent
(KS (a)). Hence, if r_e ≥ r_* on E: **||M̄_c(U) - M̄_c(U°)||² ≤ (2F_c/r_*)·Σ_{e∈E}φ_e**: moving a coarse centre costs kernel
energy, in the gauge-invariant currency the kernel itself charges.
(iii) **Centre-moving criterion.** Put 𝒞° := {Q : some c ∈ ℓ(Q) has r_c < 5/8, or all r_c ≥ 5/8 and some interior P has
||1 - V^0_P|| ≥ ε_1/4}. If Q ∈ 𝒞(U) and Q ∉ 𝒞°(U°), then some c ∈ ℓ(Q) has ||M̄_c(U) - M̄_c(U°)|| > 5ε_1/256 (5ε_1/256 ≤ 1/8 since ε_1 ≤ 6.4).
*Proof.* (i) Telescoping a product of unitaries along each contour (||U^{-1} - U°^{-1}|| = ||U - U°||), then the mean; then
Cauchy-Schwarz. (ii) Covariance: D4-norm. The identity: φ_M(V) = r(1 - cos α) = r||V - Ŵ||²/2 (KS (a); p5 C2: 1.8·10⁻¹⁵).
(iii) If some r_c(U) < ½ while r_c(U°) ≥ 5/8: |r - r°| ≤ ||M - M°|| gives > 1/8 ≥ 5ε_1/256. Otherwise all r_c(U) ≥ ½,
r_c(U°) ≥ 5/8, and some P has ||1 - V^0_P(U)|| ≥ ε_1/2 > ε_1/4 > ||1 - V^0_P(U°)||; telescoping four unitaries (p5 C3) gives
Σ_{c∈∂P}||Ŵ_c(U) - Ŵ_c(U°)|| > ε_1/4, so some c has ||ΔŴ_c|| > ε_1/16, and the polar bound of DIL-1 (factor 2, r° ≥ 5/8) gives
||ΔM̄_c|| > (5/8)(ε_1/16)/2 = 5ε_1/256 (p5 A1). ∎
**Constants (p5 B; computed in exact rationals, printed to 6 digits).** At d = 4, L = 3: F_c = 0.412894 for each of the four links of a coarse plaquette (F_* = 0.412894);
max_e|W_e| = 2/81. So in (ii)-(iii) a centre-moving completion difference has Σ_Eφ_e > (r_*/(2F_*))(5ε_1/256)² = 4.62·10⁻⁴·r_*ε_1².
**Answer to W-2.** The objection (axial gauge spreads a single-plaquette defect along a line) concerns a comparison with an
arbitrary U°. With the kernel-centre completion, δ is chain-gauge invariant; a level-(k-1) gauge transformation not induced from
level k-2 is not a symmetry of the chain (it changes the kernel factors), so the "line" representation is a different field with
a different kernel energy, priced accordingly. What is gauge-covariant is therefore the *kernel-energy* form (ii), not the
link-count form "f_cℓ_cδ" of §16.6 (c).
**The curvature (lasso) form, computed (p5 B; linear order, abelian).** For the actual S4' family, the linearised centre-plaquette
functional F_P = A_{c_1} + A_{c_2} - A_{c_3} - A_{c_4} is divergence-free (gauge invariant, B1, exact), local to the four corner
blocks (B2), and gives F_P = 9b = L²b for a uniform field b (B3, exact; positive control), 0 for gauge perturbations (B4). For a
perturbation A supported on the interior links of corner blocks:
- **sup-curvature form:** max{F_P(A) : |φ_p(A)| ≤ 1 on every plaquette touching the support} = **2.037 (one corner block),
  6.716 (all four)** (LP, primal = dual to 1e-7; B5). The LP fails to be bounded for a non-gauge-invariant functional (B7,
  negative control).
- **ℓ²-curvature form:** max{F_P(A) : Σ_pφ_p(A)² ≤ 1} = **0.1512 (one corner block), 0.2811 (all four)** (B5, residual ≤ 1e-15).
**Reading.** There is no sup-form dilution: a cluster that fills a corner block coherently moves the centre plaquette by about
twice its maximal curvature (it carries its share of the coarse flux, B3's L²b). By the pre-registered rule (B6), **(NP-F5) is
MET at linear order in the sup form**: "thin cluster, raised threshold" (§16.6 (c), REVIEW_PLD_S4 Part 3 branch 1 with γ < ½)
does not exist for clusters measured by their maximal curvature. What exists is **energy-graded** dilution: a perturbation in
the corner blocks moves F_P by at most 0.2811·(its curvature energy Σφ²)^{1/2} (0.1512 if it lies in one block). This answers the
review's lasso question with a computed constant; it also shows that the "~ε_1/L² per level" reading of SAT-1 (HW §15, INH, CF)
is not a sup-form statement about clusters inside endpoint blocks [linear order; not a statement about HW's text beyond that].

## 17.4 T13 (b)-(c): NA-PRICE^E. The split of (J-NS^dir) by defect type
For a level-k cube Q and its finer column, split the defects of the column by the finer kernel centre:
- a **mismatch defect** of Q: a level-(k-1) cube x under Q with x ∈ D_{k-1} and x ∉ 𝒞_{k-1}(U_{k-2}) (its own kernel centre is good);
- a **centre defect** of Q: x ∈ D_{k-1} ∩ 𝒞_{k-1}(U_{k-2}).
G^c_Q ⊂ {Q has a mismatch defect} ∪ {Q has a centre defect}.

**Lemma MD (mismatch defects are priced at the kernel rate, exactly): PROVEN-HERE (counted with DIL-L, item [E5] (2)).** Let k ≥ 2,
S_md a set of level-k cubes satisfying (C_S), ν a law of the form ν′ of COL-DEC (or any G′·ν^{(k-1)}_{k-1} with L_{G′} ∩
L^∂_{k-1}(S_md) = ∅), and F ≥ 0 bounded measurable in U_{≤k-2} and U_{k-1} off L^∂_{k-1}(S_md). Then
  E_ν[Π_{Q∈S_md}1{Q has a mismatch defect}·F] ≤ (81·p′_mis)^{|S_md|}·E_{ν″}[F],  p′_mis := n_int(1 - λ)^{-3/2}e^{-λκu_{k-2}ε_1²/256},
ν″ := ν with the chosen cubes declared at level k-1.
*Proof.* Union over the choice functions Q ↦ x_Q (81^{|S_md|} terms). For one choice T := {x_Q}: the x_Q satisfy (C_S) one level
down, X_{k-1}(T) ⊂ L^∂_{k-1}(S_md) is not read by G′ or F, so Lemma FT^far at level k-1 (with F·Π1{x_Q ∉ 𝒞_{k-1}}, a function of U_{k-2}
and F's variables) gives ≤ E_{ν″}[Π_xp_K(x | U_{k-2})1{x ∉ 𝒞_{k-1}}·F], and Lemma KD at level k-1 bounds each factor by p′_mis. ∎
(u_{k-2} ≥ u_k - 2R by (F_R), so p′_mis ≤ n_int(1 - λ)^{-3/2}e^{2λκε_1²R/256}e^{-λκε_1²u_k/256}.)

**(J-NS^cd)_k [node A; the residual; replaces (J-NS^dir)]:** for every law ν of COL-DEC's form, every set S_cd of level-k cubes
satisfying (C_S), and every bounded F ≥ 0 measurable in the level-≤(k-1) fields on the columns of the other cubes of S,
  E_ν[Π_{Q∈S_cd}1{Q ∈ 𝒞_k(U_{k-1}), Q has a centre defect}·F] ≤ (C_cde^{-a_cdu_k})^{|S_cd|}e^{c_cd s_k(𝔥)}E_ν[F].
In words: a coarse kernel centre that is bad while a finer cube under it is bad AND has a bad kernel centre of its own.

**Theorem NA-PRICE^E (i): CONDITIONAL (implication PROVEN-HERE; counted [E5] (3)) ⇐ (CLS-min), (SF-cap)^𝔉_{k-1}, (J-NS^cd)_k.** Here
(SF-cap)^𝔉_{k-1} is §16.5's (SF-cap)^{A,+}_θ with "μ ∈ ℛ^A_𝔥" replaced by "every law of COL-DEC's form" (equivalently, by Cor. LAW
(b), (LCR)_{k-1} in §16.7's G-form, with c_sf = c_lcr, c_f = 0). Under (F_R) with g_K² ≤ 1/(2R), SU(2), bad-only defects,
ε_1 ≤ min{1/(4A_d), t_pr}, k ≥ 2, for every admissible 𝔥, every set S of level-k cubes satisfying (C_S) (e.g. in the columns of A ⊂ 𝒰_{k+1}), and
**every law ν_G with L_G ∩ X_k(S) = ∅ (in particular HW's (E1) law ν^{(k),w}_k, any w)**:
  **ν(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·e^{c_A s_k(𝔥)},  a_A := min{λκε_1²/256, 6θa_bad, a_cd},  c_A := c_cd,**
  **C_A := 4·max{n_int(1 - λ)^{-3/2}e^{λκε_1²R/256}, c_sf, 81n_int(1 - λ)^{-3/2}e^{2λκε_1²R/256}, C_cd}.**
*Proof.* Pointwise {S ⊂ D_k} ⊂ ∪({S ⊂ D_k} ∩ E(T, S_0, S_md, S_cd)) over the 4^{|S|} ordered partitions, E := ∩_T{Q bad, Q ∉ 𝒞_k} ∩ ∩_{S_0}{Q ∈ 𝒞_k, G_Q}
∩ ∩_{S_md}{Q has a mismatch defect} ∩ ∩_{S_cd}{Q ∈ 𝒞_k, Q has a centre defect} (cubes with both kinds of defect are put in S_cd; the
factor 1{Q ∈ 𝒞_k} is dropped for S_md, an upper bound). FT^far with 1{S ⊂ D_k} (declare all of S at level k; the indicator of E is a function of
U_{≤k-1}), then p_K ≤ 1 for Q ∉ T and KD for Q ∈ T: ≤ p_mis^{|T|}E_{ν′}[…], p_mis ≤ n_int(1 - λ)^{-3/2}e^{λκε_1²R/256}e^{-λκε_1²u_k/256}. Under ν′ (COL-DEC's form):
(J-NS^cd)_k with F := the S_0- and S_md-indicators (functions of their own columns); then (SF-cap)^𝔉_{k-1} with CW on S_0 (1 ≤
e^{θY^f_Q - 6θa_badu_k} on 𝒞_k), F := the S_md-indicators; then Lemma MD. Each of the four per-cube factors is ≤ (C_A/4)e^{-a_Au_k}. ∎
**What is new against §16.5.** (1) the law is exactly HW's consumed law, with no (LI^U) and no tilt allowance (c_A has no 4c_U or
c_f term; the allowance is node A's, in the slice s_k(𝔥)); (2) the mismatch-defect part of (J-NS^dir) is PROVEN (Lemma MD: the
returned finer defect is priced by its own kernel at rate λκε_1²/256, not by the coarse centre; no recursion, no 81^k: the 81
is per Q, once); (3) the residual (J-NS^cd) contains only centre defects.

**Proposition CD (where the residual sits): (a), (b) PROVEN-HERE (not counted); (c) ARGUED.**
- (a) *Trivial bound = LOOP-const.* Dropping {Q ∈ 𝒞_k}, a centre defect x satisfies x ∈ 𝒞_{k-1} ∩ G_x (priced by CW + (SF-cap)^𝔉_{k-2}
  at rate 6θa_badu_{k-1}) or x ∈ 𝒞_{k-1} ∩ G^c_x, which is §16.6's event one level down: b(k) ≤ 81[c e^{-6θa_badu_{k-1}} + b(k-1)],
  i.e. η = 1, LOOP-const (Proposition WALL (a)).
- (b) *A contracting per-choice form now suffices.* If, for every choice function, E_ν[Π_{S_cd}1{Q ∈ 𝒞_k}1{x_Q centre defect}F] ≤
  η^{|S_cd|}E_ν[Π1{x_Q ∈ 𝒞_{k-1} ∩ D_{k-1}}F] with 324ηe^{a_AR} ≤ 1 (4 branches × 81 choices; §16.6's 243 had 3 branches), then
  (J-NS^cd)_k with C_cd = 81ηe^{a_AR}C_A ≤ C_A/4 follows from the theorem at level k - 1 with the same constants (Cor. LAW (c): no
  allowance compounds) — an induction on k whose base (level 1) is not covered. This is the (J-NS^rec_η) route of §16.6 (b), which session 4 had to
  reject only because of (LI^U)'s union-form allowance.
- (c) *What η < 1/243 requires, and why the review's branch 1 does not give it* [ARGUED; linear order]. η is the conditional price of
  the coarse centre given a centre defect below it. Split the column by the completion (REVIEW_PLD_S4 Part 3): either the completed
  column makes Q ∈ 𝒞° (priced by the completion's column energy, a punctured-column small-field moment (LCR^punct)), or the defects
  move the centre plaquette by ≥ ε_1/4. By §17.3 the second needs, at linear order, curvature energy ≥ (ε_1/(4·0.2811))² = 0.79ε_1²
  in the corner blocks (≥ 2.73ε_1² if in one block) and is NOT excluded by any sup-form threshold (R_∞ ≈ 2.04 per block). A centre
  defect follows a bad finer centre, i.e. its kernel energy is small (DIL-L (ii) gives no price); its energy sits in the deeper
  coherent field. So η < 1/243 needs an **energy-graded** price of the centre-defect configuration at level k-1 (the review's (EG)),
  and that price is an energy-graded defect probability at level k-1 — a statement of the same kind as (SDP)^A one level down.
  Two physical facts bound the recursion it starts [ARGUED, abelian]: coherent (smooth) chains preserve curvature energy from level
  to level (4D scale invariance; B3: flux L²b) but multiply curvature by L² per level, so a chain of coherent centre defects has
  depth ≤ log(2/ε_1)/log L² ≈ 41.6 at ε_1 = 6.7·10⁻⁴⁰; localised chains lose energy (ℓ² dilution 0.151 per block). Neither is a proof.

## 17.5 T13 (b): piece (1), the small field
- **Where it is needed.** On the route of §17.4 the small-field input is (SF-cap)^𝔉_{k-1} on DEFECT-FREE columns only (S_0), i.e.
  (LCR)_{k-1} in G-form with c_sf = c_lcr (Cor. LAW (b)). Mismatch-defect columns need no small-field moment at all (Lemma MD).
  A punctured-column moment (LCR^punct) enters only inside the centre-defect analysis (Proposition CD (c)), where it is not enough.
- **(LCR^punct)_{k-1}** [node A; small-field; named for the record]: for laws of COL-DEC's form, every set B of level-(k-1) cubes
  under Q and every F as in (J-NS^cd): E[e^{λ_fu_{k-1}Σ_{x∈col Q∖B}𝓔^{an}_{k-1,x}}·1{D_{k-1} ∩ col Q = B}·F] ≤ c_p·E[1{D_{k-1} ∩ col Q = B}·F]
  (the column's small-field moment with the defect set conditioned on and punctured out).
- **From the certified package?** No. CE-exp / CE-Q-col (SF §6.1, §12.1) are cluster expansions of the stage-0 cut-good integral
  with certified constants; they contain no inhomogeneous-coupling (moment) statement and no conditioning on returned defects.
  [inference] The natural route is CE-exp^k's activity form with the λ_f-tilt as an extra polymer of size λ_f per main-term
  density, i.e. a coupling shift u → (1 - λ_f)u inside the expansion; that needs the CE constants to be uniform in u on
  [(1 - λ_f)u, u], which CE-exp^k's hypotheses (N5-unif, L-loc) do not state. Not written.
- **c_lcr:** not certified (unchanged from §16.7); the Gaussian value (1 - λ_f)^{-dof/2} per column remains the ARGUED heuristic.

## 17.6 T13 (e): the interfaces in the consumed form
- **(SDP)^{A,far}_θ at level k (HW §24.3 H7):** Theorem NA-PRICE^E (i), for every far weight w (HW's (E1) form), allowance in the
  slice s_k(𝔥) with c_A = c_cd (+ node A's allowance inside (SF-cap)^𝔉 if it carries one); the tilt contributes nothing. Levels
  k ≥ 2; k = 1 needs the level-0 analogue of MD (Wilson level, no kernel: (LCR)_0, OPEN) and is not covered.
  **a_A = min{λκε_1²/256, 6θa_bad, a_cd}.** The first two entries are ≥ θa_bad (κ ≥ 1.19·10⁻⁵ at λ = ½, §16.5); so **a_A ≥ θa_bad ⟺
  a_cd ≥ θa_bad**, and HW keeps a = θa_bad iff the residual's exponent does.
- **(SF-cap)^{A,far}_θ at level k (HW H6):** ⇐ (LCR)_k in G-form with G = w (directly: w does not read the level-k history columns,
  Cor. LI-0 (b)), c_sf = c_lcr, c_f = 0 exactly; (LCR) not certified.
- **a_ret (RLARGE (RLF-0)/(RLF-δ)):** §16.8's chart formula unchanged, a_ret ≈ 8.0·10⁻⁷a_bad (binding entry (β)); it does not enter
  a_A on this route. **K12** now reads: θ ≤ a_cd/a_bad; if the centre-defect price is only threshold-type (a_ret-type), θ ≈ 8·10⁻⁷
  (n_H × ≈ 5·10⁴). An energy-graded centre-defect price is the mechanism identified here for keeping θ ↑ 1/24; others are not excluded.
- **Kernel-energy grading available now (DIL-L):** a returned cluster that moves the centre BY ITS MISMATCH costs
  e^{-λκu_{k-2}·(r_*/(2F_*))(5ε_1/256)²} (Chernoff with KS (c), on the event that the cubes carrying E are defects, declared as in
  Lemma MD so that the product-kernel law of COL-DEC applies); this beats θa_bad iff κ ≥ κ_eg := 2.01·10⁻⁴ (r_* = ½, λ = ½,
  θ = 1/24; p5 A2). It is not needed by Theorem NA-PRICE^E (MD prices mismatch defects directly, at the larger rate) and is
  recorded for (EG)'s mismatch half.

## 17.7 Check p5 (criteria checks/p5_criteria.md, 11:30:24 UTC, md5 755218e7…; script checks/p5_pld.py; output p5_out.txt; record
p5_time.txt)
- One run under the numeric lock (acquired 11:32:22 with no wait, released 11:32:27 by one rmdir); load 3.40; nice 10; BLAS threads
  1; 4.1 s, 257 MB; exit 0; no process left. **SUMMARY: ALL PASS.** The criteria header's "≈11:33 UTC" is an estimate written before
  the clock was read (file mtime 11:30:24); disclosed in p5_time.txt, header not edited.
- Exact: B1-B4 (gauge invariance, locality, uniform-field positive control F_P = 9b, gauge negative control), A1. Numerical
  certificate: B5 (LP primal = dual; least-squares residual ≤ 1e-15). Negative controls: B7 (non-gauge-invariant functional:
  LP unbounded), C1n (DIL-L with f/2 violated in 6 of 300 samples). Evidential: C1 (DIL-L (i), 0/300 violations, max ratio
  0.864), C2, C3. Decision rule B6: **NP-F5 MET at linear order (sup form)**.
- Scope: linearised (abelian) S4' geometry at d = 4, L = 3 and elementary SU(2) inequalities. Nothing about the measure,
  (CLS-min), (SF-cap), (LCR), (J-NS^cd) or the nonabelian centre map beyond linear order.

## 17.8 Outcome against the pre-stated targets (§17.0) and tally
- **T12: MET** (§17.1).
- **T13: (NP-F4) MET for the centre-defect part, with a strict reduction and two proven pieces; (NP-F5) MET at linear order for
  the sup-form dilution.** Not success, not the partial bar: the remaining hypothesis (J-NS^cd) is two-level and probabilistic.
  - (a) **MET, PROVEN:** the law conversion is exact on HW's route (FT^far, COL-DEC): (LI^U) is not consumed, the tilt
    allowance is 0, and recursions compound nothing (Cor. LAW (c)): Proposition WALL (b)'s obstruction is gone.
  - (b) piece (1): needed only on defect-free columns, = (LCR)_{k-1} in G-form, c_sf = c_lcr (not certified; the certified CE
    package does not contain it, §17.5). (LCR^punct) named; it does not suffice for centre defects.
  - (c) piece (2): split by defect type. **Mismatch defects: PROVEN (Lemma MD)**, rate λκε_1²/256, no recursion. Centre defects:
    the residual **(J-NS^cd)_k**, exactly stated (§17.4); its trivial bound is LOOP-const; a contracting per-choice form now
    suffices (no compounding); η < 1/243 needs an energy-graded centre-defect price, a statement of (SDP)'s kind one level down
    (NP-F4).
  - (d) piece (3): **DIL-L PROVEN** (kernel-energy form, gauge-covariant, F_* = 0.4129); the curvature (lasso) form computed at
    linear order: sup form 2.04 / 6.72 (no dilution: NP-F5), ℓ² form 0.151 / 0.281 (energy-graded dilution).
  - (e) interfaces written (§17.6): a_A = min{λκε_1²/256, 6θa_bad, a_cd}, C_A, c_A = c_cd explicit; a_A ≥ θa_bad ⟺ a_cd ≥ θa_bad.
- **T14: MET** (ALL PASS; B6 outcome reported).
- **Counted, PROVEN-HERE (unreviewed): [E5] (1)** Lemmas GEO + FT^far + COL-DEC (exact law conversion on HW's route); **[E5] (2)**
  Lemma DIL-L with Lemma MD (gauge-covariant kernel-energy dilution; mismatch defects priced exactly); **[E5] (3)** Theorem
  NA-PRICE^E (i) as an implication ⇐ (CLS-min) + (SF-cap)^𝔉_{k-1} + (J-NS^cd)_k. Not counted: Cor. LAW, Proposition CD (a)-(b)
  (and (c) ARGUED), the p5 B numbers (computation), §17.5.
- **New named items:** (J-NS^cd)_k [node A; replaces (J-NS^dir)], (SF-cap)^𝔉 (the law family of COL-DEC), (LCR^punct) [node A,
  small-field, recorded], 𝒞° (the reduced centre set). (J-NS^dir) and (J-NS^rec_η) are superseded by (J-NS^cd) and Proposition CD (b).
  **Tally proposal: +3 PROVEN-HERE (unreviewed); 0 OPEN items closed; row 10b's residual narrowed from (J-NS^dir) to (J-NS^cd).**

## 17.9 Proposed changes for other owners (not made here)
- **RLARGE (integrator).** Row 10b: (SDP)^A ⇐ (CLS-min) + (SF-cap)^𝔉 + (J-NS^cd) (PLD §17.4), in HW's (E1) law with no tilt allowance;
  row (J-NS^cd) [node A, P] replaces session 4's (J-NS^dir) proposal; row 10c: (SF-cap)^{A,far} ⇐ (LCR) in G-form, c_f = 0; check (a):
  "the tilt does not enter (SDP)^A on the HW route" (FT^far). K12: θ ≤ a_cd/a_bad (§17.6). Keep "(BG)_k restricted" for a_ret (§16.9).
- **HW (lane H).** H6/H7 as in §17.6; the S-1 / (LI^U) question for node A's inputs is answered on the HW route by GEO + DECL
  (exact); Proposition LI-pw's mechanism is neutralised for S by declaring S. HW §15 SAT-1's "~ε_1/L² per level" dilution: at
  linear order the sup-form response of a coarse centre plaquette to a corner-block cluster is ≈ 2.04 × its maximal curvature
  (p5 B5), so the reading needs an energy (ℓ²) qualifier [for the HW owner to check against INH/CF].
- **Node A / SF / review.** The open target for (SDP)^A is (J-NS^cd): an energy-graded price of a coarse centre over a finer centre
  defect; Proposition CD (b) states the contracting form that would suffice. (LCR)_k remains the small-field input.

# Session 6 (2026-10-28, lane E)

Read for this session before the pre-statement (read-only, nothing written): DRIVE_BRIEF (session 24); HANDOFF.md;
PLD.md §16 (session 4) and §17 (session 5) in full, plus §15.4 pointers; PLD_LOG.md; REVIEW_PLD_S4.md in full (binding);
REVIEW_PLD_S3.md l.320-380 (the Arch-1/Arch-2/Arch-3 architecture verdict, binding: the PLD-desc "Reading" / look-ahead
architecture is WRONG and is not rebuilt on here); HW.md §18.1-§19 (the (SDP)^A / (SF-cap)^A / interface rows), §24.2-§24.3
(TEL-f, TF-1, (SDP)^{A,far}/(SF-cap)^{A,far}, (E1), E1-1, (E2), E2-1, Lemma SL, wall (CRC-1)), §25 (check (d)), §30-§33
(the column-relaxed family 𝔉_𝔥, Theorem LI^U-0′, Lemma SH-att, Lemma COL, **(E2^𝔉)_{θ,ρ}**, Theorem CRC-2T, §30.5
Cor. CRC-HW, §30.6 arithmetic, §30.7 the residual (W-𝔉)); REVIEW_HW_S4.md l.320-384 (E1-1, **X-1 cross-lane for PLD**,
E2-1, the (CRC-1) verdict); RLARGE.md v3 l.386-404 (the (M-f^A)/(SF-cap)^A/(SDP)^A consumer block), l.86-96 (a, a_bad,
c_pr, t_pr, ε_1 ≲ 6.7·10⁻⁴⁰), l.490-495 (rows 9, 10b, 10c); grep only for c_lcr / (LCR) / ε_1 / t_pr across the lane files
(line locations). An unwritten exploratory pass chose the targets below; no session-6 text, criteria or script existed
when it ran, and the derivations of §18.2-§18.7 existed only as an unwritten sketch at the moment §18.0 was written.

## 18.0 PRE-STATED (session 6) — statements only (written 2026-10-28 12:28 UTC, `date -u`; THE FIRST EDIT OF THIS SESSION:
before any session-6 derivation, before checks/p6_criteria.md, and before any session-6 check)

**This section cites nothing produced in session 6.** File stat of PLD.md *before* this append: 211079 bytes, 1966 lines,
md5 35b33c8fb3702f9de47d0afbdb7edf9a, mtime 2026-10-28 08:03:19 local (= the file REVIEW_PLD_S5 is to review; identical to
PLD_LOG's session-5 closing stat). Session 6 APPENDS ONLY: it alters no line of §0-§17, because REVIEW_PLD_S5 is being
written concurrently against §17.

**Setting.** That of §16-§17 (SU(2); bad-only, history-independent defects; (F_R) with g_K² ≤ 1/(2R); Q a level-k cube,
k ≥ 1, finer field U_{k-1}; ε_1 ≤ min{1/(4A_d), t_pr}; a_bad = c_pr ε_1², c_pr = 1/(640·53²); max{6θ, 24θ}(1 + 2Rg_K²) < 1).
Laws: the COL-DEC family of §17.2 and, newly in scope, HW's column-relaxed family 𝔉_𝔥 of HW §30.1 with its weights
h^{R,1}_j (HW Theorem LI^U-0′) and its finer spectators F_<.

**T15 (the two walls, together; the target).** Both open walls that reduce to node-A pricing are in scope:
(α) **(J-NS^cd)_k** (PLD §17.4), the residual of Theorem NA-PRICE^E (i); (β) **(E2^𝔉)_{θ,ρ}** (HW §30.3), the good-buffer
screening input of Theorem CRC-2T, asked uniformly over 𝔉_𝔥. Deliver, with all quantifiers:
- **(a)** (E2^𝔉) restated in PLD's own language, and a verdict — supplies / supplies in part / does not touch — for each of
  session 5's Lemmas GEO, FT^far, COL-DEC, DIL-L, MD and Theorem NA-PRICE^E (i) against it, with the exact quantifier,
  weight-class and set-class differences named;
- **(b)** the induction-on-levels test for (J-NS^cd): either a proof via Proposition CD (b) (with the contraction factor,
  the base case, and a check that no constant or allowance compounds), or a precise statement of where the induction
  breaks, naming the minimal missing input and the direction in which it fails;
- **(c)** a search for ONE statement that yields both (α) and (β); if found, stated exactly, with the implications proven,
  with its logical strength against the hypotheses it replaces stated plainly (stronger / weaker / incomparable), and with
  the resulting hypothesis list for (SDP)^{A,far} and for (E2^𝔉);
- **(d)** the match check: Theorem NA-PRICE^E (i)'s delivered statement against (i) HW §24.3's (SDP)^{A,far}_θ, (ii)
  HW §30.3's (E2^𝔉), (iii) RLARGE v3 row 10b's (SDP)^A_θ — allowance form, weight class, set class, level range — with
  every mismatch reported as a finding, and what Theorem NA-PRICE^E becomes if (J-NS^cd) is discharged;
- **(e)** the **c_lcr** verdict: what actually depends on c_lcr (value vs existence vs uniformity), either a certificate or
  the precise statement of what a certificate must deliver, and an explicit list of any statement now labelled PROVEN in
  this file or quoted from it that in fact rests on the uncertified value.
- **Success:** (α) and (β) both reduced to ONE named single-level statement that is not a two-level defect probability,
  with the implications PROVEN-HERE from (CLS-min) and that statement alone, constants explicit and independent of
  g, K, T, k, 𝔥 and the pattern, and the delivered statements in the form HW and RLARGE consume.
- **Partial success:** the same with the one statement still containing a large-field clause, or covering only one of
  (α), (β), or with the level range short of k ≥ 1; or a proof of (b) that closes (J-NS^cd) with a named contraction.
- **Valid failure outcomes:** **(NP-F6)** the level induction of Proposition CD (b) cannot close, the exact obstruction
  named and shown not to be removable by any pointwise certificate available in §16-§17 (CW, DIL-L, KD, MD);
  **(NP-F7)** no single statement covers both walls, with the structural reason (the two walls quantify over different
  weight classes or different set classes) and a counter-instance; **(NP-F8)** (E2^𝔉) as stated in HW §30.3 is not
  deliverable by node A because its set class (far level-j cubes Y) lies outside the class on which PLD's law conversion
  is exact, with the minimal enlargement of HW's hypothesis named and its cost in HW's own constants computed;
  **(NP-F9)** the far-weight uniformity asked by PLD §16.7's (LCR) / §17.2 Cor. LAW (b) is not available (REVIEW_HW_S4
  X-1), so the session-5 interface deliveries that quantify over every far weight w must be restated.
- **Not success:** an exponent or constant depending on k, K, T or 𝔥; a fixed-V price of a bad coarse cube; a level or
  column recursion presented as uniform without an explicit contraction factor AND an explicit check that no allowance
  compounds; any use of (H-w′), HIST-sum or (RLF-3′) at levels ≥ k; any rebuild on the PLD-desc "Reading" / look-ahead
  architecture (REVIEW_PLD_S3 Arch-1/2/3); any input that is (J-NS^cd) or (J-NS^dir) renamed; claiming a statement
  PROVEN whose constant is c_lcr or any other uncertified constant.

**T16 (status discipline for session 6).** Every item added in §18 carries one of PROVEN-HERE / ARGUED / CONDITIONAL
(with the named input) / OPEN, and every status CHANGE to a session-4 or session-5 item is recorded as a change, with the
direction (upgrade / downgrade) stated, in §18.8. Downgrades are reported in the same place as upgrades.

**T17 (check p6; criteria file checks/p6_criteria.md written BEFORE checks/p6_*.py).** Exact integer / rational arithmetic
only (plain python, `fractions.Fraction`, single thread, no BLAS, no numeric lock needed per the session-24 brief):
(A) every explicit constant of T15 (c); (B) the geometric counts the one-ring enlargement of T15 (d)/(NP-F8) costs in
HW §30's constants (b_n, b_D, g²_CRC, n_♯), computed from HW's own recorded formulas; (C) the a_A ≥ θa_bad inequalities at
λ = ½ with the exact c_pr = 1/1797760; (D) the geometric series Σ_{i≥1}L^{k-i} against L^k at L = 3; with a negative
control for each of (B) and (C). No criterion may contain a constant derived in session 6.

**T18 (requests for other owners).** Everything session 6 wants changed in RLARGE.md, HW.md, SQ.md, HIST.md, SF.md or
PROOF.md is written only as a request in §18.9 "FOR OTHER FILES (session 6; not edited)". No file but PLD.md, PLD_LOG.md
and checks/p6_* is touched; no git command is run.

# Session 6 derivations (written after §18.0, from 12:30 UTC; §18.1-§18.9 were written BEFORE checks/p6_criteria.md,
which contains no constant derived in this session; the order is disclosed in §18.10 and in PLD_LOG)

**Index convention for §18.** That of §16 ("Index convention for §16"), with HW §30's objects added: 𝔉_𝔥 (the column-relaxed
family, HW §30.1), Col(y)/[y] (open/closed column), "y is R-free" (its OPEN column, levels > level(y), is unconstrained in R),
h^{R,F}_j (the future weight of HW §21-§22, insensitive to level-j links whose endpoint cubes are all R-free by HW Theorem
LI^U-0′), ν^{R,F}_j (the past law of levels ≤ j of R with the finer spectators F_< inserted), ν^w := wν/E_ν[w].
N_1(X) := the ℓ^∞ index-neighbourhood of a set X of cubes of one level (|N_1(X)| ≤ 3^d|X| = 81|X| at d = 4, L = 3).
X_j(S) := the level-j links with an endpoint at a site of a cube of S (interior links ℓ(S) plus crossing links);
ℓ*(S) := the level-j links with BOTH endpoint sites in cubes of S; L^∂_{j-1}(S) := the level-(j-1) links with an endpoint in a
level-(j-1) cube under a cube of S (all as §17.2).

## 18.1 T15 (a): (E2^𝔉) in PLD's language, and what session 5 supplies

**(E2^𝔉)_{θ,ρ} restated (HW §30.3, verbatim content, PLD indexing).** For R ∈ 𝔉_𝔥, a level j ≥ k_0, a finite set Γ of
level-(j+1) cubes and a finite set Y of level-j cubes outside col_j(Γ) with col_j(Γ) ∪ Y R-free, with ν := ν^{R,F}_j and
w := h^{R,1}_j:
  E_{ν^w}[Π_{Q∈Γ}e^{θmin{π_Q, Y^f_Q}}·1{Y ⊂ D_j}·1{Buf^R_ρ(col_jΓ ∪ Y) ∩ D_j = ∅}] ≤ C_fc^{|Γ|}(C_Ae^{-a_Au_j})^{|Y|}e^{c_A‖col_jΓ ∪ Y‖_sh},
with π_Q = a_badu_{j+1}, Y^f_Q = 24u_{j+1}F^col_Q(U_j), G_Q = {no level-j cube under Q is in D_j}, ρ = 3L - 1 = 8, and
C_fc, C_A, a_A ≥ θa_bad, c_A independent of g, K, T, 𝔥 and of the pattern R.

**What it demands, in PLD's terms (three separable demands).** Apply HW's own Lemma CAP (ii)-(iii) / CAP-dec pointwise, per
Q ∈ Γ: e^{θmin{π_Q,Y^f_Q}} ≤ e^{θY^f_Q}1_{G_Q} + e^{θπ_Q}1_{G^c_Q} and 1_{G^c_Q} ≤ Σ_{x∈col_jQ}1{x ∈ D_j} (81 terms); expand the
product over Γ into 2^{|Γ|} ordered partitions Γ = Γ_0 ⊔ Γ_1 and each Γ_1-factor into its 81 choices x: Γ_1 → col_j(Γ_1); and
drop the buffer indicator (it is ≤ 1, so it only WEAKENS the demand — see the Remark below). Then (E2^𝔉) follows from:
- **(D1) the (SF-cap) half at level j+1**: E_{ν^w}[Π_{Q∈Γ_0}e^{θY^f_Q}·F] ≤ c_sf^{|Γ_0|}e^{c‖·‖_sh}E_{ν^w}[F], with
  F := the Γ_1- and Y-indicators (functions of the level-≤j fields off Γ_0's columns);
- **(D2) the (SDP) half at level j**, for the ONE set S := Y ⊔ x(Γ_1) of level-j cubes: ν^w(S ⊂ D_j) ≤ (C_Ae^{-a_Au_j})^{|S|}e^{c_A‖·‖_sh},
  jointly with (D1) in the SAME expectation (CAP-dec's combination, HW §15);
- **(D3) a_A ≥ θa_bad**, which is what converts the uncapped factor e^{θπ_Q} = e^{θa_badu_{j+1}} ≤ e^{θa_badR}e^{θa_badu_j} into the
  constant C_fc = c_sf + 81C_Ae^{θa_badR}.
**So (E2^𝔉) is not a new kind of object: it is (SF-cap) + (SDP) at one level, combined by CAP-dec, under HW's own weighted
past law — with two differences from everything PLD has proven, both in the QUANTIFIERS, not in the mechanism.**
*Remark (the buffer is not a hypothesis that helps the statement, it is a restriction of its scope).* 1{Buf ∩ D_j = ∅} ≤ 1,
so (E2^𝔉) is WEAKER than the same bound without it. A proof is therefore free to ignore the buffer; what the buffer can do
is make the bound TRUE, by cutting down the configurations the weight w is allowed to charge (HW §24.3: "the real content of
(E2) is screening"). §18.7 says exactly where in the proof the buffer has to be used, and §18.3 shows that for the LAW
CONVERSION a different and cheaper hypothesis — one ring of R-free cubes — suffices and is exact.

**Verdict on each session-5 item against (E2^𝔉).**

| session-5 item (§17) | supplies (E2^𝔉)? | exactly why |
|---|---|---|
| **Lemma GEO (i), (iii), (iv)** | **supplies**, unchanged | pure geometry + bad-only + declaration; §18.2 shows only the clause S ∩ 𝒰_k = ∅ of (C_S) is used by them |
| **Lemma GEO (ii)** | **does not apply** | it derives X_j(S) ∩ L^far_j(𝔥) = ∅ from "S is in the columns of A ⊂ 𝒰_{j+1}". (E2^𝔉)'s Y is FAR by construction (not R-free before the relaxation, hence not in a history column: §18.2 Proposition FAR). GEO (ii) is the step §18.3 must replace |
| **Lemma FT^far** | **supplies after its hypothesis is weakened** | its stated hypothesis L_G ∩ X_j(S) = ∅ is NOT met by w = h^{R,1}_j: HW Theorem LI^U-0′ makes w insensitive only to links all of whose endpoint cubes are R-free, and a crossing link from Y to a non-R-free neighbour has a non-free endpoint cube and lies in X_j(Y) ∖ ℓ(Y). Its PROOF uses only ℓ(S) (§18.2 Lemma FT^far′), so the top-level conversion is available for HW's weight as it stands |
| **Lemma COL-DEC** | **does NOT supply as stated** | it genuinely needs L_G ∩ X_j(S) = ∅: its proof integrates the X_j(S) links out (∫k_c = 1), and a k_c that survives reads U_{j-1} on L^∂_{j-1}(S) by GEO (i). With w reading crossing links, the push-down to level j-1 is contaminated on the boundary blocks of S's cubes (80 of the 81 at L = 3), which is where Lemma MD's choice function lives. **Repaired by Lemma BUF (§18.3), not by weakening** |
| **Lemma DIL-L** | **does not touch (E2^𝔉)** | it is a deterministic statement about moving a COARSE KERNEL CENTRE. (E2^𝔉) contains no centre event. DIL-L is wall (α)'s tool only |
| **Lemma MD** | **supplies in part, conditionally** | it is a tool inside (D2); it needs COL-DEC (hence Lemma BUF) and it needs a kernel at level j-1, i.e. j ≥ 2, so it does not reach (E2^𝔉) at j = k_0 ≤ 1 |
| **Theorem NA-PRICE^E (i)** | **is exactly (D2), on the wrong set class and under an input expected false** | it delivers (SDP) for S satisfying (C_S) under laws ν_G with L_G ∩ X_k(S) = ∅. (E2^𝔉)'s S = Y ⊔ x(Γ_1) fails (C_S)'s column clause for the Y part, and the "any w" quantifier of §17.4 is the (E1) sup form that REVIEW_HW_S4 E1-1/X-1 expect FALSE (§18.7, §18.9 M-4) |
| **(SF-cap)^𝔉_{j} = (LCR)_j in G-form** | **is exactly (D1)**, with the same two quantifier problems | §17.6 already delivers (SF-cap)^{A,far} this way; X-1 is the objection |
| **Cor. LAW (a)-(d)** | **supplies (D3)'s bookkeeping and the no-compounding fact** | Cor. LAW (c) is correct and is what makes a level recursion free of allowance growth (used in §18.5) |

**Net verdict for T15 (a).** Session 5 supplies the ARCHITECTURE of (E2^𝔉) completely — the decomposition (D1)+(D2)+(D3) is
CAP-dec plus §17's own lemmas — and supplies the top-level law conversion for HW's weight after a hypothesis is weakened
that its own proof never used. It does NOT supply (i) the SET class (far Y), (ii) the push-down COL-DEC for HW's weight,
(iii) the level range (j ≥ 1 rather than j ≥ 2), or (iv) the two open halves (D1), (D2) themselves. **(i)-(iii) are closed in
§18.2-§18.4 and §18.6; (iv) is the single remaining wall (§18.6, §18.7).**

## 18.2 T15 (a) repair, part 1: the condition (C_S′), Lemma FT^far′, Proposition FAR. PROVEN-HERE (counted, one item [E6] (1))

**Audit of (C_S) (which clause each of §17.2's lemmas actually uses).** (C_S) of §17.2 is "S ∩ 𝒰_k = ∅, AND S lies in the
level-k part of the columns of 𝒰_m for some m > k". Reading §17.2's proofs:
- GEO (i): no clause (pure geometry: a level-k link reads U_{k-1} only in its two endpoint blocks).
- GEO (iii): no clause (bad-only defects + S declared).
- GEO (iv): **the first clause only.** Its proof is "Φ_{k-1} reads links with both endpoints in the level-(k-1) column of
  some Q″ ∈ 𝒰_k; Q″ ∉ S, so no such link has an endpoint under a cube of S". The step needs exactly S ∩ 𝒰_k = ∅, plus the
  disjointness of the level-(k-1) columns of distinct level-k cubes (a partition of sites, §0).
- GEO (ii): **the second clause**, essentially (it is the statement that S's links are not far).
- FT^far, COL-DEC: GEO (i), (iii), (iv) only.
**So define (C_S′): S ∩ 𝒰_k = ∅.** Then **GEO (i), (iii), (iv), Lemma FT^far and Lemma COL-DEC all hold under (C_S′) in place
of (C_S)**, with their proofs unchanged. (C_S) ⇒ (C_S′). GEO (ii) is the only part of §17.2 that needs the column clause, and
§18.3 replaces it for far sets.

**Lemma FT^far′ (the kernel-event conversion, hypothesis weakened to the interior links): PROVEN-HERE.** Let k ≥ 1, S a
finite set of level-k cubes satisfying (C_S′), ν = ν_G a law of §17.2's form with
  **L_G ∩ ℓ(S) = ∅**   (only the links INTERIOR to the cubes of S; crossing links are allowed),
ν′ := ν_G with S declared at level k, and F ≥ 0 bounded measurable in (U_0, …, U_{k-1}). Then
  **E_ν[1{S ⊂ D_k}·F] ≤ E_{ν′}[Π_{Q∈S}p_K(Q | U_{k-1})·F].**
*Proof.* Step 1 of §17.2's proof is unchanged: on {S ⊂ D_k} the declared cubes count as defects, so 1_{R,k} = 1_{R′,k}, and
1_{R′} ≤ 1_R pointwise (HW (m1)) gives Z_{ν′} ≤ Z_ν and equality of the numerators. Step 2 integrates the links of ℓ(S) at
fixed (U_0, …, U_{k-1}) and U_k off ℓ(S). The factors of ν′'s density that could read U_k on ℓ(S) are: (a) the kernel factors
Π_{c∈ℓ(S)}k_c(·; M̄_c(U_{k-1})); (b) 1_{R′,k}, which reads no link of X_k(S) ⊇ ℓ(S) by GEO (iii); (c) the spectators Φ_{k′},
k′ < k, which read levels < k; (d) G, excluded by the hypothesis L_G ∩ ℓ(S) = ∅. Nothing else is present (a past law of
levels ≤ k has no K_k and no coarser constraint). So, conditionally, the links of ℓ(S) carry the product density Π_{c∈ℓ(S)}k_c,
and ζ_Q reads only ℓ(Q) ⊂ ℓ(S) (bad-only: interior plaquettes, §16.3); Lemma TD gives the factorisation into Π_Qp_K(Q|U_{k-1}). ∎
*What is new.* §17.2's stated hypothesis L_G ∩ X_k(S) = ∅ is strictly stronger than its own proof uses, and the difference is
exactly the crossing links — exactly where HW's weight w = h^{R,1}_j fails it (§18.1). **So the top-level kernel-event
conversion is available for HW's weight with no repair at all, no (LI^U), and cost 1.** What is NOT repaired this way is the
push-down: Lemma COL-DEC does use the X_k(S) hypothesis (§18.1), and §18.3 supplies it instead of weakening it.

**Proposition FAR (HW's far sets and history-cube columns satisfy (C_S′)): PROVEN-HERE (elementary, counted with FT^far′).**
Let 𝔥 be admissible and R ∈ 𝔉_𝔥, so S_R ⊂ S_{R(𝔥)} (HW §30.1: R = R_{S(𝔥)∖𝒞}).
- **(i)** If a level-j cube y is NOT R-free then y ∉ 𝒰_j. Hence every set Y of non-R-free level-j cubes satisfies (C_S′).
- **(ii)** If Γ is a set of level-(j+1) cubes with Γ ∩ A_{j+1}(𝔥) = ∅ (in particular Γ ⊂ S^{(j+1)}(𝔥): HW's animals and far
  defects), then col_j(Γ) ∩ 𝒰_j = ∅, so every S ⊂ col_j(Γ) satisfies (C_S′). The same holds for Γ = 𝒰_{j+1} by HW Lemma DJ
  and H-nest (iii) (a history cube's descendants at finer levels lie in the small-field regions), which is §17.2's own
  justification of (C_S).
*Proof.* (i) Write A_m(𝔥) := Σ(Ω^c_{m-1}) ∪ N_1(𝒰_m) (HW §22, l.1076), S^{(m)}(𝔥) = all ∖ A_m(𝔥), and recall 𝒰_m ⊂ Ω^c_m and
H-nest (i): Σ(Ω^c_{m-1}) ⊂ Ω^c_m. Claim: y ∈ 𝒰_j ⇒ π^{m-j}(y) ∈ A_m(𝔥) for every m > j. Induction on m: for m = j + 1,
y ∈ 𝒰_j ⊂ Ω^c_j gives π(y) ∈ π(Ω^c_j) ⊂ Σ(Ω^c_j) = the first part of A_{j+1}(𝔥) (Σ(X) = N_1(π(X)) ⊇ π(X)). For the step,
π^{m-j}(y) ∈ Σ(Ω^c_{m-1}) ⊂ Ω^c_m (H-nest (i)), so π^{m+1-j}(y) ∈ π(Ω^c_m) ⊂ Σ(Ω^c_m) ⊂ A_{m+1}(𝔥). Hence no pair
(m, π^{m-j}(y)), m > j, lies in S_{R(𝔥)} ⊇ S_R, i.e. y is R-free. Contrapositive: y not R-free ⇒ y ∉ 𝒰_j.
(ii) Let x ∈ col_j(Γ), i.e. π(x) ∈ Γ. If x ∈ 𝒰_j then by (i)'s claim π(x) ∈ A_{j+1}(𝔥), contradicting Γ ∩ A_{j+1}(𝔥) = ∅. ∎
*Reading.* (i) is the exact sense in which "far" and "history" are complementary: HW's species-1 polymers (non-R-free level-j
defects) are automatically outside 𝒰_j, so the only clause of (C_S) that PLD's law conversion uses is free for them. The
clause that is NOT free is GEO (ii), and it is the weight, not the set, that it is about.

## 18.3 PROVENANCE BREAK: REVIEW_PLD_S5 landed mid-session, and what it changes

**Record (honest ordering).** §18.0 (12:28:16 UTC), §18.1 and §18.2 were written WITHOUT REVIEW_PLD_S5.md, which did not
exist when this session started reading. The lead delivered it at ≈ 12:45 UTC, after §18.2 was appended. §18.1 and §18.2 are
left exactly as written; nothing in them is adjusted after the fact. From §18.4 on, the review's binding fixes B1-B6 are
adopted. The two independent passes agree where they overlap, and the review is the earlier authority on §17:
- **S5-6 = §18.1/§18.2's FT^far observation, independently.** The review: "The hypothesis L_G ∩ X_k(S) = ∅ is stronger than
  the proof uses: only L_G ∩ ℓ(S) = ∅ is consumed. … the gap between the two is precisely where (E2^𝔉) lives." §18.2 states
  and proves that lemma (FT^far′). The review notes the gap; §18.2 supplies the statement. Credit to the review for the
  priority.
- **S5-26 reason 2 = §18.1's COL-DEC/GEO (ii) row, independently.** Same mechanism, same conclusion.
- **S5-26 reason 2's set clause is SHARPER in §18.2 than in the review.** The review says Y "violates (C_S)" and treats that
  as part of the obstruction. §18.2 shows that **(C_S)'s column clause is not used by GEO (i), (iii), (iv), FT^far or
  COL-DEC** — only S ∩ 𝒰_k = ∅ is, which Proposition FAR proves HW's far Y satisfies automatically. So (C_S) is NOT an
  obstruction for (E2^𝔉); **GEO (ii) alone is**, i.e. the obstruction is about the WEIGHT, not about the SET. That is what
  makes §18.4's repair possible and cheap.
- **S5-8/B1 (buffered weights) is a constraint §18.1-§18.2 did not impose.** Adopted from §18.4 on, with the review's own
  verification: the buffer indicator is a function of U_k on the interiors of cubes at level-(k+1) index distance ≥ 2 from A,
  hence disjoint from X_k(S), so FT^far, FT^far′, GEO and COL-DEC are unaffected by it. **No statement below is asserted for
  all far weights.**
- **S5-9/S5-10/B2 (union allowance) is adopted**: every allowance below is the union form ‖·‖_sh, never the slice s_k(𝔥).
  §18.5 supplies the one displayed line B2 (b) asks for.
- **S5-20/B3 (F-conditioned form) is adopted**: everything below is stated as E_ν[(…)·F] ≤ (…)E_ν[F].
- **S5-27/B4 (name clash) is adopted**: PLD's (SF-cap)^𝔉 is written **(SF-cap)^{COL}** below (the COL-DEC law family), and the
  new hypothesis of §18.6 carries no 𝔉 superscript. HW's 𝔉_𝔥 and (E2^𝔉) keep their meaning.
- **S5-13**: §17.3's "max_e|W_e| = 2/81" holds only over the links interior to a corner block; over supp W the maximum is
  1/27. Nothing in §18 uses either number.
- **S5-25**: the review finds no status error on c_lcr in §17. §18.8's independent audit agrees, and adds what a certificate
  must deliver and one number that is NOT a c_lcr matter.
- **The review's (d)** names the biggest live wall as "(J-NS^cd) restricted to buffered far weights — specifically its (EG)
  content", with branch 1 of REVIEW_PLD_S4 Part 3 dead by computation and branch 2 "still not attempted". §18.5 (c) attempts
  branch 2 and finds one definite thing about it; §18.6 offers a route that does not pass through it.

## 18.4 T15 (a) repair, part 2: Lemma BUF, and the cost of the extra ring. PROVEN-HERE (counted with §18.2, item [E6] (1))

**Lemma BUF (one ring of R-free cubes restores GEO (ii) for far sets, exactly): PROVEN-HERE.** Let 𝔥 be admissible,
R ∈ 𝔉_𝔥, j ≥ 0, and 𝒜 a finite set of level-j cubes such that **every cube of N_1(𝒜) is R-free**. Put w := h^{R,1}_j. Then
  **L_w ∩ X_j(𝒜) = ∅.**
*Proof.* Let c ∈ X_j(𝒜): one endpoint site of c lies in a cube y ∈ 𝒜. The other endpoint site lies in y or in a cube y′ with
ℓ^∞ index distance 1 from y (|u − v| ≤ 1 for a nearest-neighbour link, and the level-j cubes partition the sites). So both
endpoint cubes of c lie in N_1(𝒜) and are R-free. By HW Theorem LI^U-0′ with A := X_j(𝒜) and F ≡ 1 (the spectator
hypothesis is vacuous at F ≡ 1), h^{R,1}_j(U) = h^{R,1}_j(U′) whenever U and U′ agree off X_j(𝒜). ∎
**Consequences (each immediate).** Let S be a finite set of level-j cubes with N_1(S) R-free and S ∩ 𝒰_j = ∅ ((C_S′), which
Proposition FAR gives for HW's far Y and for col(Γ) under a non-relaxed Γ). Then:
- **(a)** ν^w = ν_G with G := w satisfies FT^far's FULL hypothesis L_G ∩ X_j(S) = ∅, so **Lemma FT^far applies verbatim**
  (FT^far′ is not even needed here; it is needed only if one declines to buy the ring).
- **(b) Lemma COL-DEC applies**: the marginal of ν′ (:= ν^w with S declared at level j) on U_{≤j-1} is G′·ν^{(j-1)}_{j-1}/E[G′]
  with G′ = Φ_{j-1}·H′ not reading U_{j-1} on L^∂_{j-1}(S). Its first clause (which is all that is used below) needs only
  j ≥ 1; the explicit product-kernel display of §17.2 needs j ≥ 2.
- **(c)** Hence the whole of §17.2-§17.4 (Cor. LAW, DIL-L, MD where j ≥ 2, Theorem NA-PRICE^E (i)) is available **under HW's
  own weight on FAR sets**, which S5-26 reason 2 records as unavailable. The pattern family is not an obstruction either:
  Lemma BUF is applied ONCE, to R ∈ 𝔉_𝔥, BEFORE the declaration, and the declaration does not change the weight — FT^far and
  COL-DEC carry the same G through, and their other inputs (HW Lemma DECL, (m1), GEO) hold for every R_{S,E}. **This answers
  S5-26 reason 1 for the law conversion** (it does not answer it for the two open halves, which §18.6 states over 𝔉_𝔥).
- **(d)** Compatibility with B1: the buffer indicator 1{Buf^R_ρ(col S) ∩ D_j = ∅} may be multiplied into w freely; it reads
  interiors of cubes at distance ≥ 2 (level-(j+1) index), disjoint from X_j(S), so (a)-(c) are unaffected (review S5-26's own
  one-line verification). Below, "buffered weight" means w times that indicator, and all statements are for buffered weights
  only.
**What the hypothesis costs, and whether HW can buy it.** HW §30.3 asks only "col(Γ) ∪ Y R-free"; Lemma BUF asks
"N_1(col(Γ) ∪ Y) R-free", one ring more. Inside Theorem CRC-2T the ring is BUYABLE, at a bounded cost in HW's own constants:
in step (4), replace R″ := R′^{-Col(Y)} by
  **R‴ := R′^{-(Col(Y) ∪ Col(N_1(col 𝒟 ∪ Y)))}.**
- *It stays in the family.* Col(X) is upward closed by definition and a union of upward-closed sets is upward closed; the set
  is finite (finite torus). So R‴ ∈ 𝔉_𝔥, and 1_{R′} ≤ 1_{R‴} pointwise ((m1)).
- *It is bought by HW's own induction hypothesis*, since N(R′) < N(R): ρ^F_{R′}(Col(N_1(col 𝒟 ∪ Y))) ≤ exp(c_U·#_{R′}(·)) and
  #_{R′}(Col(Z)) ≤ Σ_{r≥1}|π^r(Z)| ≤ ‖Z‖_sh for Z := N_1(col 𝒟 ∪ Y).
- *The geometric price is one factor 81.* ‖N_1(X)‖_sh ≤ 81‖X‖_sh, because |N_1(X)| ≤ 3^d|X| = 81|X| and
  sh_m(N_1(X)) ⊂ N_1(sh_m(X)) (iterate HW Lemma SL's step Σ(N_1(X)) = N_1(π(N_1(X))) ⊂ N_1(N_1(π X)) = N_1(Σ(X))), so
  |sh_m(N_1(X))| ≤ 81|sh_m(X)|. Hence the extra factor is ≤ e^{81c_U‖col 𝒟 ∪ Y‖_sh}, and step (4)'s own
  e^{c_U‖col 𝒟 ∪ Y‖_sh} becomes e^{82c_U‖col 𝒟 ∪ Y‖_sh}.
- *Net effect on HW §30.4's constants*: **c_+ = c_A + c_U becomes c_+′ = c_A + 82c_U**, and b_n, b_D, x_*, ε_2 are affine in
  (c_+, c_U), so every one of HW's three activity conditions (S1), (S2), (T) survives with b_n, b_D larger by at most the
  factor (c_A + 82c_U)/(c_A + c_U) ≤ 82, i.e. **g²_CRC smaller by ≤ 82 and n_♯ larger by ≤ 82** (check p6 B computes the
  exact numbers from HW's own recorded formulas). These are g-independent constants, so this is a lower g_0 and a bigger
  n_♯, not a loss of uniformity — HW §30.6's own reading of b_n.
- *Nothing else in CRC-2T moves.* Y is determined relative to R′ before the extra relaxation, so step (4)'s decomposition is
  unchanged; and Buf^{R‴}_ρ ⊂ Buf^{R″}_ρ (fewer non-free cubes), so the buffer clause of E_Y becomes WEAKER and the inclusion
  {Y(c) = Y} ⊂ E_Y survives. Step (5)'s peel only gains (more cubes unconstrained).
**Status.** Lemma BUF: PROVEN-HERE. The affordability of the ring inside Theorem CRC-2T: PROVEN-HERE as arithmetic about
HW's recorded formulas (it is a request to the HW owner, §18.12, not an edit of HW.md; HW must re-run its own step (4) with
R‴ to confirm nothing else in its proof reads R″).

**[§18.3 timing correction, appended not edited.]** §18.3 says the review landed "at ≈ 12:45 UTC". That time was written
before the clock was read and is wrong: the §18.3+§18.4 append completed at 12:40:59 UTC (`date -u`), so the review landed
BETWEEN the §18.2 append and 12:40:59 UTC, and no later time is supportable. The §18.3 line is left as written, per the
append-only rule for this file; this correction is the record. (Same discipline as PLD_LOG's [RPLD-fix B3] entry.)

## 18.5 T15 (b): does induction on levels close (J-NS^cd)? Proposition CHAIN. PROVEN-HERE (structure/arithmetic about the
available certificates; not counted) — outcome **(NP-F6) MET**

Throughout: (J-NS^cd)_k is read in its B1/B2/B3 form — buffered far weights, union allowance ‖S_cd‖_sh, F-conditioned.

**(a) The direction in the handoff's suggestion is not available.** The suggested shape was "assume (SDP) at level i + 1
(coarser), price the level-i configuration using it". It cannot be run, for a reason that is not a technicality:
**{Q ∈ 𝒞_k(U_{k-1})} is not a level-k defect event.** 𝒞_k is a function of the FINER field U_{k-1} (§16.3), and the only
implication Lemma KD supplies runs the other way: Q ∉ 𝒞_k ⇒ p_K(Q | U_{k-1}) ≤ p_mis. The converse inclusion
{Q ∈ 𝒞_k} ⊂ {Q ∈ D_k} is **false**: a kernel centre with an interior plaquette at exactly ‖1 − V^0_P‖ = ε_1/2 and kernel
fluctuations of size (κu_{k-1})^{-1/2} ≪ ε_1 leaves Q GOOD with probability → 1 as g → 0 (this is the same elementary fact
that p4's negative control C1n measured: a centre 10σ below threshold gave 0 hits in 10⁵). So no (SDP) at any level, coarse
or fine, bounds ν(Q ∈ 𝒞_k); the centre event has to be priced by its ENERGY (Lemma CW), not by a defect probability. **The
only admissible direction is Proposition CD (b)'s, fine → coarse.**

**(b) In CD (b)'s direction the induction has no base, and the base is exactly the level the theorem cannot reach.**
CD (b) derives (J-NS^cd)_k from Theorem NA-PRICE^E (i) at level k − 1. NA-PRICE^E is proven for k ≥ 2 (Lemma MD applies
FT^far at level k − 1, which needs a kernel there). So the lowest instance the induction can even state is (J-NS^cd)_3 from
level 2, and **(J-NS^cd)_2 requires NA-PRICE^E at level 1, which requires the level-0 analogue of MD and (LCR)_0, both OPEN**
(§16.5 "Level 0", §17.6). This is §17.4's own disclosure and review S5-22's "CD (b) closes nothing today"; it is recorded
here as the FIRST of three independent reasons, because it is fatal on its own and independent of η.

**(b′) The allowance does NOT compound, and the line review B2 (b) asks for is available. PROVEN-HERE.** For S a set of
level-k cubes and any choice function x: S → col_{k-1}(S) (one level-(k-1) cube under each Q ∈ S),
  **‖x(S)‖_sh ≤ ‖S‖_sh + (1 + Δ_sh)·|S|,  Δ_sh = 3073361, depth-free.**
*Proof.* ‖X‖_sh := |X| + Σ_{r≥1}|sh_{lev(X)+r}(X)| (HW §30.2). Here |x(S)| = |S|. Since π(x_Q) = Q, the extra finest shadow
level is sh_k(x(S)) = Σ(x(S)) = N_1(π(x(S))) = N_1(S); for r ≥ 1, sh_{k+r}(x(S)) = Σ^r(N_1(S)). By p4 D2a (exact shadow sets
in Z⁴) sh_m(x_Q) ⊇ sh_m(Q) for every m, and by §16.6 (b) / p4 D2b the TOTAL excess per cube is depth-free,
Σ_m(|sh_m(x_Q)| − |sh_m(Q)|) ≤ Δ_sh = 3073361 (the measured value is 256). Writing E_Q^{(m)} := sh_m(x_Q) ∖ sh_m(Q),
  sh_m(x(S)) = ∪_{Q∈S}sh_m(x_Q) ⊂ sh_m(S) ∪ ∪_{Q∈S}E_Q^{(m)},
so |sh_m(x(S))| ≤ |sh_m(S)| + Σ_{Q∈S}|E_Q^{(m)}|; summing over m gives Σ_m|sh_m(x(S))| ≤ Σ_m|sh_m(S)| + Δ_sh|S|, and adding
|x(S)| = |S| gives the claim. ∎
*Consequence.* In the UNION currency ‖·‖_sh, CD (b)'s recursion carries c(k) = c(k − 1) exactly (the Δ_sh|S| term is
per-cube and goes into C_cd, as §16.7 already placed it), so **Corollary LAW (c) is correct and review item B2 (b) is
discharged.** In the slice currency s_k(𝔥) the recursion does not type-check at all (review S5-9 (a)), which is a second,
independent reason to work in ‖·‖_sh. **So compounding is NOT the obstruction. η is.**

**(c) η < 1/324 is not obtainable from any certificate in §16-§17, and the reason is that the certificates are NESTED, not
additive.** Pointwise, the event of (J-NS^cd)_k at a cube Q with witness x (level k − 1) gives two certificates:
  (E_k)   F^col_Q(U_{k-1}) ≥ a_bad/4      (Lemma CW at level k, from Q ∈ 𝒞_k);
  (E_{k-1}) F^col_x(U_{k-2}) ≥ a_bad/4    (Lemma CW at level k − 1, from x ∈ 𝒞_{k-1}).
These do not add. Lemma CW's branch (b) proves (E_k) by ℰ_P(V^0) ≤ κΦ_{∂P}(U_{k-1}, V^0) + ℰ^<_P(U_{k-1}) = ℰ^<_P(U_{k-1})
(HW Lemma TE (i), zero mismatch at the kernel centre) and ℰ^<_P ≤ F^col_Q, i.e. **(E_k) is a lower bound on a sum that
already CONTAINS the finer cone terms** (TE (iii)'s column-term identification), and (E_{k-1}) is a lower bound on a
sub-sum of that same tower one level down. Hence the two together certify
  F^col_Q(U_{k-1}) ≥ a_bad/4,  **not** a_bad/2,
and the price available from them is ONE factor e^{-6θa_bad u_k}, not two. Iterating down a chain Q ⊃ x_{k-1} ⊃ … ⊃ x_{k-m}
of centre defects multiplies the COMBINATORIAL cost by 81^m (the choice functions, per level, CD (b)'s own counting) and the
PRICE by 1. So **η = 1 is not an artefact of a crude union bound; it is what the available pointwise certificates give.**
This is the precise, inequality-level content of §17.4 (c)'s sentence "its energy sits in the deeper coherent field".

**(d) The one additive currency is identically zero on the event.** Lemma DIL-L (ii) is genuinely additive across levels: it
charges Σ_{e∈E}φ_e, the KERNEL energy, and the kernel energies of different levels are exponents of different kernel
factors, hence add under the product-kernel law COL-DEC supplies. But a **centre** defect is by definition a cube whose own
kernel centre is bad, so φ_e = 0 on its blocks is admissible (the field may sit AT its own centre and still be bad), and
DIL-L (ii) returns the bound 0. §17.6's grading (rate λκu_{k-2}(r_*/(2F_*))(5ε_1/256)², requiring κ ≥ κ_eg = 2.0069·10⁻⁴,
exactly as review S5-5 recomputed it) is therefore (EG)'s MISMATCH half, which Lemma MD already prices at the strictly
larger rate λκε_1²/256. **The additive currency and the event are disjoint. That is the whole difficulty in one line.**

**(e) The favourable sub-case has a huge pointwise certificate that cannot be cashed.** [ARGUED; abelian, linear order.]
On a COHERENT chain the curvature multiplies by L² per level upward (p5 B3, exact: F_P = L²b = 9b for a uniform field b), so
a chain of depth m forces coarse curvature ≥ L^{2m}ε_1 and, by CW's branch (b) at that threshold,
F^col_Q ≥ c_pr min{(L^{2m}ε_1)², t_pr²} = L^{4m}a_bad while L^{2m}ε_1 ≤ t_pr. Already at m = 1 the implied price
e^{-6θ·81·a_bad u_k} = e^{-486 a u_k / (θ a_bad / a)} ≈ e^{-4.9·10¹⁰} (at the recorded a = θa_bad ≈ 1.0·10⁻⁸⁶, g_K² ≈ 10⁻⁹⁴,
so a u_k ≈ 10⁸) annihilates the 324 per level, and the chain's depth is g-independently bounded by
m ≤ log(2/ε_1)/(2 log L) ≈ 41.4 (ε_1 ≲ 6.7·10⁻⁴⁰ is a g-independent threshold, RLARGE §0 under (TH-ch″)), so even
81^{41.4} ≈ 10^{79} is a constant. **But cashing F^col_Q ≥ L^{4m}a_bad requires a moment of e^{θY^f_Q} on a column that
CONTAINS a defect, and that is exactly the factor 1_{G_Q} that (SF-cap)^{COL} excludes.** So the sub-case where the physics
is most favourable funnels into the SAME single missing object as the sub-case where it is least favourable.

**(f) Branch 2 of REVIEW_PLD_S4 Part 3, attempted (the (EG) route the review calls unattempted): ONE definite finding.**
Branch 1 (thin cluster, raised threshold) is dead by computation (p5 B6, (NP-F5) MET; review S5-15 confirmed it
independently with R_∞(U4) ≥ 3.33). So every centre defect must be priced by branch 2: an energy-graded in-step activity
  |ρ_Y| ≤ C^{|Y|}e^{-a_eg u_{k-1}·ℰ_+(Y)/ε_1²},  ℰ_+(Y) := Y's energy ABOVE ITS COMPLETION  (REVIEW_PLD_S4 l.248-259).
**Finding (EG-cur) [PROVEN-HERE as a disjunction; the currency question is decided, the lemma it needs is named].**
(EG) is stated with an unqualified "energy above its completion", and the two candidate currencies give OPPOSITE verdicts:
- **In the KERNEL-energy currency** (ℰ_+ := Σ_{e}φ_e, the quantity DIL-L (ii) charges and the only one the kernel factors
  themselves grade), **(EG) is VACUOUS on exactly the configurations (J-NS^cd) is about**: by (d), a centre defect admits
  φ_e = 0, so ℰ_+ = 0 and the bound degenerates to |ρ_Y| ≤ C^{|Y|}. §17.6's "kernel-energy grading available now" is
  therefore not branch 2's half, as §17.6 itself says.
- **In the CURVATURE-energy currency** (ℰ_+ := Σ_pφ_p(A)², A := the difference from the kernel-centre completion U° of
  DIL-L (ii)), the DETERMINISTIC half EXISTS and is computed: §17.3's ℓ²-lasso constants give
  **Σ_pφ_p(A)² ≥ (ε_1/(4·0.2811))² = 0.791ε_1²** for a centre-moving cluster spread over the four corner blocks, and
  **≥ (ε_1/(4·0.1512))² = 2.735ε_1²** if it lies in one block (review S5-22 reproduces both). So branch 2 is not empty.
**What is therefore needed, exactly, and it is one lemma, not a programme:**
- **(EG-link) [node A; OPEN; NEW, named here]:** for a level-(k-1) cube x ∈ D_{k-1} ∩ 𝒞_{k-1} under Q, with U° the
  kernel-centre completion of DIL-L (ii) on x's blocks, the CL^J / R1^J in-step activity of x is graded by the CURVATURE
  energy of U − U°: |ρ_x| ≤ C·e^{-a_eg u_{k-1}Σ_pφ_p(U − U°)²/ε_1²}, with a_eg·0.791 ≥ θa_bad.
- The two currencies are linked only if U° is a local MINIMISER of the curvature energy on x's blocks. U° is by construction
  the mode of the KERNEL (the S4′ centre), and nothing in §16-§17 identifies it with a curvature minimiser. **That
  identification — kernel mode = local curvature minimiser, to within a constant factor in the quadratic form — is the
  precise missing ingredient of branch 2.** It is a deterministic, single-level, small-field statement about the S4′ centre
  map, i.e. of the SAME kind as DIL-L and computable by the same linear-order machinery as p5 B. It is NOT attempted here.
- Proposition CC does not refute (EG-link): in CC's coherent datum the realised field sits a distance δ from the completion,
  so Σφ_p(A)² ~ δ² is small and (EG) predicts no price, which is what CC exhibits (§16.8, and REVIEW_PLD_S4 l.259 says the
  same). **CC and (EG-link) are consistent; CC bites only on threshold-graded activities.**

**(g) Verdict on T15 (b): (NP-F6) MET.** Induction on levels does not close (J-NS^cd). Three independent reasons, in
increasing depth: **no base case** (b); **no contraction from the available certificates** (c)+(d), because CW's certificates
across levels are nested and the one additive certificate vanishes on centre defects; and even the favourable coherent
sub-case **cannot cash its certificate** (e). Compounding is NOT a reason: in the union currency the allowance does not
compound ((b′), which discharges review item B2 (b)). The minimal missing inputs are, exactly and alternatively:
**(EG-link)** (branch 2, the kernel-mode/curvature-minimiser identification, §18.5 (f)) **or** the single defect-tolerant
moment **(CEM^{COL})** of §18.6, which needs no currency conversion and no level recursion at all.

## 18.6 PROVENANCE BREAK 2 (REVIEW_HW_S5 landed), and T15 (c) part 1: the union-form attached-patch allowance, stated.
Proposition PATCH: PROVEN-HERE (elementary, counted with §18.2/§18.4 as item [E6] (1))

**Record.** The lead delivered REVIEW_HW_S5's essentials between the §18.5 append (12:42:20 UTC) and this one. §18.0-§18.5
are left exactly as written. REVIEW_HW_S5 itself was NOT read in full here (its content is used only as the lead relayed it,
and is labelled [relayed] where it is load-bearing). Three undeclared deltas between HW §30.3's (E2^𝔉) and node A's actual
statements are relayed, plus the (CRC-1) status and one narrowing in node A's favour. §18.6 answers them; §18.7 gives the
single statement.

### 18.6.1 The object HW's gas needs, in PLD's language
**Definition (attached patch, patch allowance).** For a level j, a finite set Γ of level-(j+1) cubes and a finite set Y of
level-j cubes, the **attached patch** is **P(Γ, Y) := col_j(Γ) ∪ Y** (a set of level-j cubes), and its union-form shadow sum
is ‖P‖_sh := |P| + Σ_{r≥1}|sh_{j+r}(P)| (HW §30.2's ‖·‖_sh, union form, levels ≤ K − 1). HW §30.3 asks node A's allowance in
the form **e^{c_A‖P(Γ, Y)‖_sh}**, one depth term for the WHOLE patch.

**Proposition PATCH: PROVEN-HERE (elementary).**
- **(i) Monotonicity, and the reconciliation.** ‖·‖_sh is monotone under inclusion of sets of one level: sh_{j+1}(X) = Σ(X) =
  N_1(π(X)) is monotone (X ⊂ X′ ⇒ π X ⊂ π X′ ⇒ N_1(π X) ⊂ N_1(π X′)); iterating, sh_{j+r}(X) ⊂ sh_{j+r}(X′) for all r, and
  |X| ≤ |X′|; so ‖X‖_sh ≤ ‖X′‖_sh. Consequently, for **every** set S of level-j cubes with S ⊂ P(Γ, Y) — in particular
  **S := Y ⊔ x(Γ_1)** for any Γ_1 ⊂ Γ and any choice function x: Γ_1 → col_j(Γ_1), which is the set the CAP-dec expansion of
  §18.1 produces — **e^{c‖S‖_sh} ≤ e^{c‖P(Γ, Y)‖_sh}.** So a node-A statement delivered in the union form **on its own set**
  lands in HW's patch currency with no further hypothesis and no new geometric lemma. (This is §16.5's own monotonicity step,
  l.1432-1433, applied across the interface.)
- **(ii) The slice does not reconcile, in either direction.** There is no inequality between s_k(𝔥) and ‖S‖_sh: HW SL-1's own
  example (a history with components only at level k + 1) gives s_k(𝔥) = 0 while ‖S‖_sh ≥ |S| ≥ 1; and a deep history with
  |S| = 1 gives s_k(𝔥) arbitrarily large while ‖S‖_sh is bounded by 1 + 81 + 256(K − j − 2). **So REVIEW_PLD_S5's B2 is not
  cosmetic, and the two reviews' convergence on the currency is correct: the slice is simply the wrong object.**
- **(iii) The thing that must NOT appear is PER-CUBE depth.** For a single DETACHED level-j cube y,
  ‖{y}‖_sh = 1 + Σ_{r≥1}|sh_{j+r}({y})| ≈ 1 + 81 + 256(K − j − 2) (the 4⁴-block stabilisation: Σ(y) is 81 cubes, and from
  then on π compresses a 4⁴ block to ≤ 2⁴ and N_1 re-expands it to 4⁴ = 256; §16.6 (b), p4 D2b, HW §30.2 Reading), i.e. it
  contains a term LINEAR IN THE DEPTH K − j. HW's gas can afford Y at all only because Lemma SH-att merges an ATTACHED
  cluster's shadows into the patch's: ‖P ∪ Y‖_sh ≤ 6561‖P‖_sh + c_att(ρ)|Y| with c_att(8) = 1229313, depth-free in |Y|.
  **So the requirement on node A is not about the SIZE of the allowance constant. It is that the allowance be attached to the
  PATCH — one depth term for the whole of it — and never to the individual cubes of Y.**
- **(iv) Where the requirement actually lands (the finding).** Theorem NA-PRICE^E (i) (§17.4) and Theorem NA-PRICE^{E+}
  (§18.7) **generate no allowance of their own**: on the HW route the law conversion is exact (Cor. LAW (a): c_T = 0; Lemma
  FT^far's "No (LI^U), no shadow allowance"), Lemma KD is pointwise, Lemma CW is pointwise, and Lemma MD contributes only the
  per-cube factor 81 and (by §18.5 (b′)) a per-cube depth-free Δ_sh. **Every allowance in the delivered bound is TRANSMITTED,
  unchanged, from the small-field hypothesis.** Therefore the union-form attached-patch allowance is **a clause of the
  HYPOTHESIS, not a theorem about the patch**, and that is why no statement in PLD §16-§17 has the shape REVIEW_HW_S5 is
  looking for: the shape has to be written into the moment, where PLD has so far written none.
- **(v) What it would take, exactly.** Node A owes the small-field moment with its allowance in one of
  - **(P0) no allowance at all** (c = 0), which is what Cor. LAW (b) already delivers on the exactly-converted law
    ("c_sf = c_lcr, c_f = 0"), or
  - **(P1) a per-cube constant only**, e^{c|A∖A′|}, absorbed into c_sf^{|A∖A′|} (sufficient because ‖P‖_sh ≥ |P| ≥ |A∖A′|),
  and must NOT be in either of
  - **(P2) per-cube union-form sums** e^{cΣ_{Q∈A∖A′}‖{Q}‖_sh} (the per-cube depth term of (iii); unaffordable, §16.6 (b)), or
  - **(P3) the slice** s_k(𝔥) (not convertible, (ii)).
  **So "what it would take" is: prove the moment under the exactly-converted law and state it with a per-cube constant and
  no shadow sum.** Nothing else is needed on PLD's side; (i) does the conversion. **And if the moment comes with (P0), node A
  delivers c_A = 0, which is STRICTLY STRONGER than HW asks and strictly better for HW's own constants: c_+ = c_A + c_U
  drops to c_U, so b_n = 531441·38418·c_+ + 38417c_U and b_D = 38416(531441c_+ + c_U) drop by the factor
  (c_A + c_U)/c_U, and g²_CRC = a/(b_n + aR + log(12800C_ℓ)) rises by it** (check p6 B2).
  *Status.* Proposition PATCH: PROVEN-HERE. The moment itself: OPEN, and it is §18.7's single statement.

### 18.6.2 The three undeclared deltas, answered; and the TF-1 switch
Each is relayed from REVIEW_HW_S5 by the lead, and answered from PLD's side only.
- **Delta 1 (allowance currency).** Answered by Proposition PATCH: PLD can meet HW's patch form, and what node A actually
  owes is (P0) or (P1), not HW's union form as such. **Renegotiation request (§18.12): (E2^𝔉) should state its allowance
  requirement as "node A's moment carries at most a per-cube constant", with ‖P‖_sh derived by monotonicity, so that the two
  lanes stop quoting incomparable currencies.** The delta is then declared and closed.
- **Delta 2 (level coverage, and the level-0 clause).** PLD covers **k ≥ 2** as of §17 and **k ≥ 1** as of §18.7; level 0 is
  OPEN in both ((LCR)_0 / the level-0 Wilson window moment, §16.5 "Level 0", §17.6). HW's level-0 clause reads "with
  Π_{Q∈Γ}e^{θX_Q} for Γ a set of level-0 cubes (Wilson window moment), Y at level 0" — with Γ and Y at the SAME level, while
  the body of (E2^𝔉) has Γ at level j + 1 and Y at level j. **Confirmed mis-levelled from PLD's side**; the consistent
  reading is Γ at level 0 with the Wilson window X_Q and NO Y (there is no level −1), or Γ at level 1 with Y at level 0.
  Either way **PLD delivers neither today**, and this is a two-level hole at the bottom of the tower that TEL-f needs
  (review S5-21 (ii)). Not closed here; recorded as the second-largest residual after the moment (§18.11).
- **Delta 3 (F_< is a free unquantified symbol) — FREE on PLD's side, and that is good news.** HW §30.1 fixes F_< as "a
  bounded weight that is a function of U_0, …, U_{k_0-1}" with all relaxations at levels ≥ k_0 + 1 and j ≥ k_0. So F_< reads
  only levels ≤ k_0 − 1 ≤ j − 1, i.e. **strictly finer than the level-(k−1) column links that FT^far, COL-DEC and the
  moment's G-hypothesis are about** (with k := j + 1, those are level-j links; F_< reads levels ≤ j − 1). In FT^far and
  COL-DEC such a weight is one of the factors "Φ_{k′}, k′ < k, which read levels < k" and is excluded by the same line of the
  proof. Hence **(E2^𝔉) may be quantified "for every bounded measurable F_< ≥ 0 of U_{<k_0}" at zero cost to PLD's law
  conversion**, and node A's statements should be written that way. Request in §18.12.
- **The TF-1 switch (HW §30.5 uses FINER-first telescoping on the (E2) route) is NOT a regression for node A.** PLD §17.2
  builds its law with the finer capped spectators already in: "ν^{(k)}_k is the past law of levels ≤ k: density
  ∝ e^{-S_0}Π_{i<k}K_iΠ_{j≤k}1_{R(𝔥),j}Π_{k′<k}Φ_{k′}", and Lemma GEO (iv) is precisely the clause that handles Φ_{k-1}
  (the Φ_{k′} with k′ < k − 1 read levels < k − 1 and sit inside ν^{(k-1)}_{k-1}). This is the identification review S5-26
  calls "correct and useful". **So switching TF-1 off reinstates no node-A law mismatch: the law PLD §17 is written for IS
  HW's finer-first law, not the coarse-first one.** What TF-1 was protecting is a different thing — the (E1) form of the
  weight — and that is dead for other reasons (E1-1). Reported back rather than absorbed, as asked, with this verdict.
- **(CRC-1) status (relayed): dissolved as a wall but CONDITIONAL on (E2^𝔉).** Accepted, and the consequence is recorded in
  §18.11: the single statement of §18.7 is then RLARGE's critical-path item 1, and it is node A's, i.e. this lane's.
- **One narrowing in node A's favour (relayed, and it changes what must be proven).** HW §24.3 doubted that a good buffer can
  screen, because bad-only goodness reads only the INTERIOR plaquettes of the buffer cubes, so far curvature can sit on the
  straddling plaquettes (the LI-pw mechanism). REVIEW_HW_S5 finds the doubt does not transfer: LI-pw is **pointwise**, while
  (E2^𝔉) is an **expectation**, and the measure suppresses the straddling configurations at cost e^{-c/g_j²}. **Accepted, and
  used in §18.7: it means the screening content of the moment is a DECOUPLING under the measure, not a deterministic
  geometric statement about buffer-good configurations.** §18.7 (c) states the decoupling.

## 18.7 T15 (c): ONE statement for both walls. (CEM^{COL}), Theorem NA-PRICE^{E+}, Corollary E2-RED, Proposition ONE.
Implications PROVEN-HERE (counted, item [E6] (2)); the statement itself OPEN

### 18.7.0 The law class, written out (B1-compliant: no sup over weights)
**Definition 𝔏^buf_k(R, 𝒜) (generators, not a sup).** Fix an admissible 𝔥, R ∈ 𝔉_𝔥, k ≥ 1, and a finite set 𝒜 of level-k
cubes with **N_1(𝒜) R-free** and **𝒜 ∩ 𝒰_k = ∅**. 𝔏^buf_k(R, 𝒜) is the set of laws on (U_0, …, U_{k-1}) obtained by the
following three steps, and by nothing else:
1. take the past law ν^{R′,F_<}_m of levels ≤ m of a pattern R′ equal to R with finitely many cubes of 𝒜 ∪ col_{k-1}(𝒜)
   DECLARED at level k or k − 1, for m ∈ {k − 1, k}, with any bounded measurable F_< ≥ 0 of U_{<k_0} inserted (k_0 ≤ k − 1);
2. weight it by the **buffered far weight** w := h^{R,1}_m·1{Buf^R_ρ(𝒜_m) ∩ D_m = ∅}, where 𝒜_k := 𝒜, 𝒜_{k-1} := col_{k-1}(𝒜),
   ρ = 3L − 1 = 8 (HW §30.3) — **and by no other weight**;
3. take the marginal on (U_0, …, U_{k-1}).
By **Lemma BUF** (at level m, applied to 𝒜_m, whose N_1 is R-free) together with **Lemma COL-DEC** (first clause, m ≥ 1) and
**Lemma GEO (i), (iii), (iv)** under (C_S′) (Proposition FAR), every law ν ∈ 𝔏^buf_k(R, 𝒜) satisfies
  **L_ν-weight ∩ L^∂_{k-1}(𝒜) = ∅**,
i.e. it is of COL-DEC's form with respect to 𝒜: no factor of its density reads U_{k-1} on the level-(k-1) links with an
endpoint under a cube of 𝒜. (The buffer indicator is compatible: it reads interiors of cubes at level-(k+1) index distance
≥ 2 from 𝒜, hence disjoint from X_k(𝒜) — review S5-26's one-line verification, and §18.4 (d).)
*Why this class and not §17.4's.* §17.4 quantifies over **every** ν_G with L_G ∩ X_k(S) = ∅, which contains HW's (E1) and is
expected FALSE (HW [RHW4-fix E1-1], review S5-8). 𝔏^buf_k is generated by HW's own weights only. **Nothing below is asserted
for all far weights.**

### 18.7.1 The single statement
**(CEM^{COL})_k [node A; NEW; OPEN; "column energy moment on COL-DEC laws"].** There is c_cem < ∞, independent of
g ≤ g_0, k, K, T, 𝔥, R, 𝒜, A, A′, F and F_<, such that for every admissible 𝔥, every R ∈ 𝔉_𝔥, every k ≥ 1, every finite set
A of level-k cubes with N_1(A) R-free and A ∩ 𝒰_k = ∅, every A′ ⊂ A, every ν ∈ 𝔏^buf_k(R, A), and every bounded measurable
F ≥ 0 of the level-≤(k-1) fields OFF the columns of A ∖ A′,
  **E_ν[Π_{Q∈A∖A′}e^{θY^f_Q}·F] ≤ (c_cem)^{|A∖A′|}·E_ν[F],   24θ(1 + 2Rg_K²) < 1,**
with Y^f_Q := 24u_kF^col_Q(U_{k-1}) (HW §4's column energy, level index shifted as in §16).
**The ONLY difference from (SF-cap)^{COL}_{k-1} (= §16.7's (LCR) in G-form, = §17.4's (SF-cap)^𝔉 renamed per B4) is that the
factor Π_{Q}1_{G_Q} is ABSENT: the moment is asked on every column, defect-carrying ones included.** Four properties, each
load-bearing and each checkable against §17.0's pre-stated bar:
- **single level**: Y^f_Q is a functional of U_{k-1} alone, and the law is a law of level ≤ k − 1. No level-(k-1) defect
  probability occurs anywhere in it, so it is NOT "(SDP)^A one level down" and NOT (J-NS^cd) renamed;
- **a moment, not a probability**: it is of exactly the kind already named as node A's small-field input since §16.7;
- **allowance (P1), i.e. per-cube and no shadow sum**: by Proposition PATCH (v) this is what the interface needs, and it is
  what Cor. LAW (b)'s c_f = 0 already achieves for the G_Q-restricted version;
- **defect-tolerant**: the one thing it adds.

**Theorem NA-PRICE^{E+} (i): (SDP)^{A,far} at every level k ≥ 1, F-conditioned, in the union currency, for buffered far
weights. CONDITIONAL (implication PROVEN-HERE; counted [E6] (2)) ⇐ (CLS-min) + (CEM^{COL})_k.**
Under the standing setting of §18.0 ((F_R) with g_K² ≤ 1/(2R), SU(2), bad-only history-independent defects,
ε_1 ≤ min{1/(4A_d), t_pr}, max{6θ, 24θ}(1 + 2Rg_K²) < 1), for every admissible 𝔥, every R ∈ 𝔉_𝔥, every **k ≥ 1**, every
finite set S of level-k cubes with **N_1(S) R-free** and **S ∩ 𝒰_k = ∅**, every ν ∈ 𝔏^buf_k(R, S)-generating law at level k
(i.e. ν = ν^w of step 2 before the marginal), and every bounded measurable F ≥ 0 of the level-≤(k-1) fields off the columns
of S:
  **E_ν[1{S ⊂ D_k}·F] ≤ (C_Ae^{-a_Au_k})^{|S|}·E_ν[F],**
  **a_A := min{λκε_1²/256, 6θa_bad},  C_A := 2·max{n_int(1 − λ)^{-3/2}e^{λκε_1²R/256}, c_cem},  c_A := 0,**
for any fixed λ ∈ (0, 1); and **a_A ≥ θa_bad unconditionally** (6θa_bad ≥ θa_bad; and λκε_1²/256 ≥ θa_bad at λ = ½ whenever
κ ≥ 256c_pr/12 = 1/84270 = 1.18666·10⁻⁵, with the exact c_pr = 1/(640·53²) = 1/1797760, check p6 C1).
*Proof.* Pointwise, since every Q ∈ S is bad on {S ⊂ D_k},
  1{S ⊂ D_k} ≤ Σ_{T⊂S}Π_{Q∈T}1{ζ_Q = 1}1{Q ∉ 𝒞_k(U_{k-1})}·Π_{Q∈S∖T}1{Q ∈ 𝒞_k(U_{k-1})}
(2^{|S|} subsets T; for Q ∈ S ∖ T the factor 1{ζ_Q = 1} ≤ 1 is dropped — review S5-19's wording repair applied: the only
U_k-dependent factors kept are the 1{ζ_Q = 1}, Q ∈ T). Fix T and put **F_T := Π_{Q∈S∖T}1{Q ∈ 𝒞_k}·Π_{Q∈T}1{Q ∉ 𝒞_k}·F**, a
function of U_{k-1} and of F's variables, hence of U_{≤k-1}.
(1) *Law conversion, exact.* N_1(S) R-free and Lemma BUF give L_w ∩ X_k(S) = ∅ for the buffered w, so Lemma FT^far applies
verbatim (no (LI^U), no allowance, Cor. LAW (a)). Declaring S at level k (ν ↦ ν′):
  E_ν[Π_{Q∈T}1{ζ_Q = 1}·F_T] ≤ E_{ν′}[Π_{Q∈T}p_K(Q | U_{k-1})·F_T].
(2) *Kernel branch.* Lemma KD with the 1{Q ∉ 𝒞_k} factors of F_T: p_K(Q | U_{k-1})1{Q ∉ 𝒞_k} ≤ p_mis, and
u_{k-1} ≥ u_k − R ((F_R)) gives p_mis ≤ n_int(1 − λ)^{-3/2}e^{λκε_1²R/256}·e^{-λκε_1²u_k/256}.
(3) *Centre branch, pointwise.* Lemma CW (CONDITIONAL ⇐ (CLS-min)): on {Q ∈ 𝒞_k}, F^col_Q ≥ a_bad/4, so Y^f_Q ≥ 6a_badu_k and
1 ≤ e^{θY^f_Q}e^{-6θa_badu_k}. Hence
  E_{ν′}[F_T] ≤ e^{-6θa_badu_k·|S∖T|}·E_{ν′}[Π_{Q∈S∖T}e^{θY^f_Q}·F′],  F′ := Π_{Q∈T}1{Q ∉ 𝒞_k}·F.
(4) *The moment.* By Lemma COL-DEC (first clause; k ≥ 1) the marginal of ν′ on U_{≤k-1} lies in 𝔏^buf_k(R, S); F′ is
measurable off the columns of S ∖ T (1{Q ∉ 𝒞_k} for Q ∈ T reads M̄_c, c ∈ ℓ(Q), whose S4′ contours stay in the endpoint
blocks under Q, and T ∩ (S∖T) = ∅; review S5-19 checked exactly this measurability). So (CEM^{COL})_k with A := S, A′ := T
gives E_{ν′}[Π_{S∖T}e^{θY^f_Q}F′] ≤ c_cem^{|S∖T|}E_{ν′}[F′] ≤ c_cem^{|S∖T|}E_{ν′}[F] (drop the indicators, F ≥ 0).
(5) *Assemble.* E_{ν′}[F] ≤ E_ν[F] by step (1)'s DECL/(m1) chain applied to F alone (Z_{ν′} ≤ Z_ν, equal numerators on the
declared event; or directly 1_{R′} ≤ 1_R). Each of the two per-cube factors is ≤ (C_A/2)e^{-a_Au_k}, so summing the 2^{|S|}
subsets gives Π_{Q∈S}(b_1 + b_2) ≤ (C_Ae^{-a_Au_k})^{|S|}, times E_ν[F]. ∎
**What this removes against §17.4 (five things).** (1) No (J-NS^cd) — the centre branch is priced directly by the moment.
(2) No Lemma MD, hence no factor 81 per cube and **no restriction k ≥ 2: level 1 is covered**, since the proof needs a kernel
at level k only (review S5-21 (ii)'s hole shrinks from two levels to one). (3) No level recursion of any kind, so RLARGE's
requirement "never derived from (SDP)^A at level k − 1" is met by construction, not by moving content into a hypothesis
(§17.4's NA-3 problem). (4) No defect-type split, so the four-branch 4^{|S|} count drops to 2^{|S|} and C_A's four-way max
drops to two. (5) **c_A = 0**, i.e. allowance (P0): by Proposition PATCH (v) this is strictly stronger than HW asks and lowers
HW's own b_n, b_D (check p6 B2). The statement is F-conditioned (B3), in the union currency with c_A = 0 (B2), and for
buffered weights only (B1).

**Corollary E2-RED ((E2^𝔉′) from the same single input): CONDITIONAL (implication PROVEN-HERE; counted with [E6] (2)) ⇐
(CLS-min) + (CEM^{COL}).** Let **(E2^𝔉′)_{θ,ρ}** be HW §30.3's (E2^𝔉)_{θ,ρ} with three declared changes: its hypothesis
"col(Γ) ∪ Y R-free" strengthened to **"N_1(col_j(Γ) ∪ Y) R-free"** (§18.4, buyable inside Theorem CRC-2T at ≤ ×82 on b_n,
b_D, n_♯); F_< universally quantified (§18.6.2 Delta 3, free); and Γ ∩ A_{j+1}(𝔥) = ∅ or Γ = 𝒰_{j+1} (Proposition FAR (ii),
true for CRC-2T's animals and for Cor. CRC-HW). Then (E2^𝔉′) holds with
  **C_fc := c_cem + 81·C_Ae^{θa_badR},  C_A, a_A as in Theorem NA-PRICE^{E+},  a_A ≥ θa_bad,  c_A = 0,**
i.e. with exactly HW §30.3's constant C_fc = c_sf + 81C_Ae^{θa_badR} at c_sf := c_cem.
*Proof.* Write k := j + 1. Per Q ∈ Γ, HW Lemma CAP (ii)-(iii) pointwise: e^{θmin{π_Q,Y^f_Q}} ≤ e^{θY^f_Q}1_{G_Q} +
e^{θπ_Q}1_{G^c_Q}, and 1_{G^c_Q} ≤ Σ_{x∈col_j Q}1{x ∈ D_j} (81 terms); π_Q = a_badu_{j+1} ≤ a_bad(u_j + R) by (F_R), so
e^{θπ_Q} ≤ e^{θa_badR}e^{θa_badu_j}. Expand into the 2^{|Γ|} ordered partitions Γ = Γ_0 ⊔ Γ_1 and the 81^{|Γ_1|} choice
functions x, and drop the buffer indicator (≤ 1; it may equally be kept inside w, §18.7.0 step 2). For a fixed (Γ_0, Γ_1, x)
put **S := Y ⊔ x(Γ_1)**, a set of level-j cubes with S ⊂ P(Γ, Y) = col_j(Γ) ∪ Y, so N_1(S) is R-free by hypothesis and
S ∩ 𝒰_j = ∅ by Proposition FAR ((i) for Y, (ii) for x(Γ_1)). Then
  E_{ν^w}[Π_{Γ_0}e^{θY^f_Q}·1{S ⊂ D_j}] ≤ c_cem^{|Γ_0|}·E_{ν^w}[1{S ⊂ D_j}]  by (CEM^{COL})_{j+1} with A := Γ_0 ∪ Γ_1,
A′ := Γ_1 and F := 1{S ⊂ D_j} (measurable on the level-≤j fields; for Q ∈ Γ_0 the columns are disjoint from x(Γ_1) by the
partition, and from Y since Y lies outside col_j(Γ)), the law being in 𝔏^buf_{j+1}(R, Γ_0) by Lemma BUF at level j applied to
col_j(Γ_0);
  E_{ν^w}[1{S ⊂ D_j}] ≤ (C_Ae^{-a_Au_j})^{|S|}  by Theorem NA-PRICE^{E+} at level j with F := 1.
Collecting, each Q ∈ Γ contributes ≤ c_cem + 81e^{θa_badR}C_Ae^{(θa_bad − a_A)u_j} ≤ c_cem + 81C_Ae^{θa_badR} = C_fc, using
a_A ≥ θa_bad; and each y ∈ Y contributes C_Ae^{-a_Au_j}. The allowance is e^{0} ≤ e^{c_A‖P(Γ,Y)‖_sh} for any c_A ≥ 0
(Proposition PATCH (i) is not even needed, since c_A = 0). ∎

**Proposition ONE (one statement for both walls): PROVEN-HERE (logic).** Assume (CLS-min). Then (CEM^{COL})_k implies
- **(a) (SF-cap)^{COL}_{k-1}** (§16.7's (LCR) in G-form / §17.4's (SF-cap)^𝔉 renamed), with c_sf = c_cem and c_f = 0:
  multiply the integrand by Π_Q1_{G_Q} ≤ 1;
- **(b) (J-NS^cd)_k** (§17.4), with C_cd = c_cem, **a_cd = 6θa_bad ≥ θa_bad**, and allowance e^{0}: pointwise
  1{Q ∈ 𝒞_k, Q has a centre defect} ≤ 1{Q ∈ 𝒞_k} ≤ e^{θY^f_Q}e^{-6θa_badu_k} by Lemma CW;
- hence **(c) Theorem NA-PRICE^E (i) of §17.4** (whose three inputs are (CLS-min), (SF-cap)^{COL}, (J-NS^cd)) **and Theorem
  NA-PRICE^{E+} of §18.7**, and
- **(d) (E2^𝔉′)** by Corollary E2-RED.
**So both open walls of this session's scope — (J-NS^cd) (wall α) and (E2^𝔉) (wall β) — reduce to the single statement
(CEM^{COL}) plus (CLS-min).** Moreover (b) gives a_cd = 6θa_bad, so **K12 reads θ ↑ 1/24 with a_A = a_bad/4** (check p6 C2),
and the fallback θ ≈ a_ret/a_bad ≈ 8·10⁻⁷ (n_H × ≈ 5·10⁴) is no longer forced.
**Logical strength, stated plainly (this is a consolidation, not a discharge).** (CEM^{COL}) is, as far as anything here
shows, **STRICTLY STRONGER** than the conjunction (SF-cap)^{COL} + (J-NS^cd) it replaces: it implies both, and nothing here
derives it from them. So:
- **(J-NS^cd) is NOT discharged, and Theorem NA-PRICE^E (i) stands exactly as session 5 left it.** §18.7 is an ALTERNATIVE
  route with one hypothesis instead of two, offered for the four reasons below, and the lane now carries both.
- Reasons it is nevertheless the better target: (1) it is single-level and contains no defect probability, so it passes
  §17.0's "not success" list and RLARGE's "never from (SDP)^A at level k − 1", which (J-NS^cd) does not; (2) it is the same
  KIND of object as the input node A has owed since §16.7, so it adds no new category of difficulty; (3) it makes
  a_A ≥ θa_bad unconditional and settles K12; (4) it covers k = 1 and carries c_A = 0, i.e. exactly the interface currency
  §18.6 shows is needed. Against it: it is stronger, and if it is FALSE the lane must come back to branch 2 / (EG-link)
  (§18.5 (f)). §18.7.2 says what is known about whether it is false.

### 18.7.2 What (CEM^{COL}) reduces to, and whether it is false. Proposition SPLIT: PROVEN-HERE (logic; not counted)

**Proposition SPLIT.** (CEM^{COL})_k follows, with c_cem = c_1·c_2, from two statements that share no variable:
- **(CEM-1)_k [the moment; single level, NO far field, NO probability]:** for every R ∈ 𝔉_𝔥, k ≥ 1, A, A′, F as in
  (CEM^{COL}) and the UNWEIGHTED past law ν_0 := ν^{R′,F_<}_{k-1} (step 1 of §18.7.0, w ≡ 1),
    E_{ν_0}[Π_{Q∈A∖A′}e^{θY^f_Q}·F] ≤ c_1^{|A∖A′|}E_{ν_0}[F].
- **(CEM-2)_k [the decoupling; the screening content]:** for the same data and the buffered far weight w of §18.7.0 step 2,
    E_{ν_0}[Π_{Q∈A∖A′}e^{θY^f_Q}·w·F]·E_{ν_0}[F] ≤ c_2·E_{ν_0}[Π_{Q∈A∖A′}e^{θY^f_Q}·F]·E_{ν_0}[w·F].
*Proof.* E_{ν^w}[Πe^{θY^f}F]/E_{ν^w}[F] = (E_{ν_0}[Πe^{θY^f}wF]/E_{ν_0}[wF]) ≤ c_2·(E_{ν_0}[Πe^{θY^f}F]/E_{ν_0}[F]) ≤ c_2c_1^{|A∖A′|}. ∎

**(CEM-1): what it is and what it needs.** It is exactly **(LCR)_{k-1} with the factor 1_{G_Q} deleted**. Its two ingredients
are named and neither involves the far field:
- **(a) the main-term reduction OFF G_Q.** HW §6's F^col_Q(U_{k-1}) ≤ Σ_{x∈col Q}𝓔^{an}_{k-1,x}(U_{k-1}) is stated and proven
  only on G_Q (defect-free column), because the representation (I^E_{k-1})″ has main-term densities only on small-field
  regions. Off G_Q the needed inequality is F^col_Q ≤ Σ_{x∈col Q∖B}𝓔^{an}_{k-1,x} + Σ_{x∈B}(the R-operated large-field energy
  of x), B := D_{k-1} ∩ col Q. **Nothing in PLD §16-§17 or HW §6 writes this**, and it is the first thing a proof of
  (CEM-1) must write. It is a statement about ONE representation at ONE level, deterministic.
- **(b) the coupling response for the full representation.** With (a), the moment becomes a coupling shift
  u_{k-1} → (1 − λ_f)u_{k-1} inside the FULL (small-field + R-operated) representation, λ_f = 24θ(1 + 2Rg_K²) < 1. For the
  small-field part this is (LCR) verbatim; for the R-operated part it is the requirement that CL^J/R1^J's activity bounds be
  uniform in u on [(1 − λ_f)u, u]. §17.5 already recorded that CE-exp^k's hypotheses (N5-unif, L-loc) **do not state** that
  uniformity. **So (CEM-1) = (LCR) + the reduction (a) + u-uniformity of the activity bounds on [(1 − λ_f)u, u].** All three
  are single-level and small-field-or-representation statements. This is the honest content of "(EG) and (LCR^punct) merged".
- *Relation to the Gaussian heuristic.* The unweighted moment's expected value is (1 − λ_f)^{-dof/2} per column with
  dof = 3n_int·81 = 52488 at SU(2), d = 4, L = 3, i.e. log c_1 ≈ 26244·log(1/(1 − λ_f)) ≈ 1.82·10⁴ at λ_f = ½ (check p6 D1).
  That is far below every ceiling it has to respect (§18.8), so (CEM-1)'s difficulty is entirely its PROOF, not its size.

**(CEM-2): the screening content, and why the buffer-good EVENT alone cannot supply it. [the sharp negative]**
(CEM-2) is a correlation bound between the future likelihood h^{R,1} (restricted to buffer-good far fields) and the column
energy functional, under the past law. Two facts fix its difficulty:
- **(α) Without it, the statement is FALSE at the recorded thresholds, and the arithmetic is the same one in two guises**
  (REVIEW_HW_S4 X-1; HW [RHW4-fix E1-1]). If a weight may condition the far field on a configuration whose conditional mean
  forces column curvature of order ε_1, the moment behaves as e^{λ_fu_{k-1}ℰ_*} with u_{k-1}ℰ_* of order u·ε_1²; at the
  recorded g_K² ≈ 10⁻⁹⁴ and ε_1 ≈ 6.7·10⁻⁴⁰, **u·ε_1² = 4.49·10¹⁵** (check p6 A2), so the moment is e^{10¹⁵⁺} and no
  g-independent c_cem exists. For a g-independent constant the FORCED mean column energy must be O(g_K²), i.e. forced
  curvature ≲ g_K ≈ 10⁻⁴⁷.
- **(β) Buffer-goodness bounds the curvature only by ε_1, and the gap is exactly the same number.** "No defect in the buffer"
  means every INTERIOR plaquette of every buffer cube has ‖1 − V_P‖ < ε_1 = 6.7·10⁻⁴⁰. The ratio of what is needed to what is
  given is (ε_1/g_K)² = **4.49·10¹⁵** — the identical quantity as in (α) (check p6 A2 verifies the identity
  u·ε_1² = (ε_1/g_K)² at u = 1/g_K²). **So the good-buffer EVENT is not the mechanism of (CEM-2): a g-independent constant
  cannot be extracted from a curvature bound at the defect threshold.** What must do the work is that w = h^{R,1} is a
  LIKELIHOOD and not an adversary — i.e. typicality under the chain measure, not a configuration-space bound.
- **(γ) The relayed narrowing is consistent with (β) and points the same way.** REVIEW_HW_S5 [relayed] narrows HW §24.3's
  pessimism: HW doubted screening because bad-only goodness ignores the straddling plaquettes (the LI-pw mechanism), and the
  reviewer observes that LI-pw is **pointwise** while (E2^𝔉) is an **expectation**, the offending configurations costing
  e^{-c/g_j²}. That is precisely the typicality route of (β): the straddling configurations are rare under the measure, not
  excluded by the event. **Taken together, (β) and (γ) say: (CEM-2) is a decay-of-correlations / decoupling estimate for the
  past law between a far region and a column separated by one R-free ring, with the buffer indicator as a convenience and
  not as the mechanism.** That is the same KIND of object as R1^J's gas convergence and as the (CRC-1) assessment in
  REVIEW_HW_S4 ("a volume-uniform decoupling or cluster estimate … the obstruction is the representation, not convergence").
- **(δ) What is NOT available, so that nobody re-walks it.** A purely geometric/deterministic screening lemma ("a buffer with
  interior curvature < ε_1 forces column curvature ≲ g") is excluded by (β): the two thresholds differ by 4.49·10¹⁵ and ε_1
  is g-independent while g_K is not, so no inequality between them can hold uniformly in g. And **Lemma SCR-type footprint
  shrinking is not a decoupling**: conditioning on U_{k-1}, the level-k links interior to an R-free region are conditionally
  independent with kernels centred at M̄_c(U_{k-1}), so the far weight has NO direct footprint there (this is Lemma BUF +
  COL-DEC, already proven), and the lattice-unit footprint of the pushed-down weight shrinks by Σ_{r≥1}L^{k-r} = L^k/(L − 1)
  = L^k/2 < L^k at L = 3 (check p6 E1), so one R-free ring of level-k cubes screens the footprint at EVERY finer level. **But
  the correlation remains**, because the past law is not a product measure: the far weight biases U_{k-1} OUTSIDE the region
  and U_{k-1} inside is coupled to it through the level-(k-1) kernel and 1_{R,k-1}. Recorded so that "the footprint shrinks"
  is never mistaken for "the weight decouples". [The shrinking statement needs, beyond one level, the closed columns [𝒜]
  relaxed — upward closed, hence inside 𝔉_𝔥, but feeding back into (CRC); it is used in NO counted item here.]

**Verdict on whether (CEM^{COL}) is false.** Its (CEM-1) half is not known to be false and its expected size is tiny; its
(CEM-2) half is FALSE if the weight class is widened to all far weights ((α), which is HW's E1-1 and review X-1), and is
OPEN for the buffered class {h^{R,1}_m·1{Buf good}} that §18.7.0 fixes. **No counterexample to (CEM^{COL}) as stated is
known, and §18.7.2 (β) shows precisely which route to it cannot work.** Status: **OPEN**, split into (CEM-1) (OPEN, three
named single-level ingredients) and (CEM-2) (OPEN, a decoupling estimate).

## 18.8 T15 (e): the c_lcr verdict

**(i) What actually depends on c_lcr (traced through the lane files as they stand).**
  c_lcr → c_sf (§16.7: c_sf = e^{2c_U(81+Δ_sh)}c_lcr; §17.2 Cor. LAW (b) on the HW route: **c_sf = c_lcr exactly**)
        → C_A (§16.5, §17.4: C_A = 4·max{…, c_sf, …}; §18.7: C_A = 2·max{…, c_cem}) and
          C_fc = c_sf + 81C_Ae^{θa_badR} (HW §15/§18.1, RLARGE l.391)
        → C_ℓ = (1 − λ_*)^{-3n_int/2}C_fc (HW §30.4)
        → HW's x_* = C_Ae^{a_AR + c_+c_att(ρ)}e^{-a_A/g_K²} and ε_2 = 6400^{n_♯}(2C_ℓe^{b_n+aR}e^{-a/g_K²})^{n_♯+1}
        → the activity conditions (S1) Δ_ρ²x_* ≤ ½, (S2) ε_2 ≤ ½ and 2ε_2 ≤ c_U, and the ceiling
          g²_CRC = a/(b_n + aR + log(12800C_ℓ)).
**In every one of these, c_lcr enters only through log c_lcr, additively, against b_n ≈ 2.04·10¹⁰·c_+ (HW §30.6).** Hence:
- **The VALUE of c_lcr is NOT load-bearing.** g²_CRC changes by the factor (1 + log c_lcr/b_n)^{-1}: at HW's recorded
  b_n = 20416938755·c_+ ≈ 2.04·10¹⁰c_+, a c_lcr as large as **e^{10⁹}** moves g²_CRC by under 5% (check p6 B3), and the
  Gaussian heuristic's own value gives log c_lcr ≈ 1.82·10⁴ (check p6 D1), thirteen orders below even that. The negative
  control: log c_lcr = 10¹¹ WOULD bind (it moves g²_CRC by a factor ≈ 5.9), so the non-bindingness is a real inequality and
  not a tautology (check p6 B3n).
- **What IS load-bearing is EXISTENCE and UNIFORMITY**, in a list every item of which is used somewhere: g ≤ g_0 (the whole
  smallness regime), k (level-uniform constants, RLARGE row 10b, HW §18.1 "the SAME constant at every level"), K and T
  (volume), 𝔥 and **R ∈ 𝔉_𝔥** (REVIEW_RLARGE_V3 S-4, REVIEW_HW_S4 CR-2, HW §30.7's open node-A question), the sets A, A′, the
  conditioning function F, the inserted F_< (§18.6.2 Delta 3), and **the weight class**.
- **And the weight-class uniformity is NOT available in the form §16.7 states it** (REVIEW_HW_S4 X-1 + HW E1-1 + review
  S5-8): over all G that do not read the column links, no finite g-uniform c_lcr exists, by §18.7.2 (α)'s arithmetic. **So a
  certificate is impossible for (LCR) as written, independently of any analytic work.** That is a defect of the statement,
  not of the constant.

**(ii) The certificate target, stated exactly (what a certificate must deliver).** A proof of
  E_ν[Π_{Q∈A∖A′}exp(λ_fu_{k-1}Σ_{x∈col Q}𝓔^{an}_{k-1,x})·1_{G_Q}·F] ≤ c_lcr^{|A∖A′|}·E_ν[F]
with (1) λ_f = 24θ(1 + 2Rg_K²) < 1; (2) **the law class 𝔏^buf_k(R, A∖A′) of §18.7.0** — generated by HW's own buffered far
weights, NOT a sup over G; (3) uniformity in g ≤ g_0, k ≥ 1, K, T, 𝔥, R ∈ 𝔉_𝔥, A, A′, F, F_<; (4) the allowance in form
(P0) or (P1) of Proposition PATCH (v) — per-cube at worst, no shadow sum, never the slice; (5) the numerical side condition
**log c_lcr ≤ 10⁹** (so HW's (S1)/(S2) ceilings move by < 5%). Clauses (2) and (4) are new asks and are the ones §16.7 and
§17.6 get wrong; (5) is generous by thirteen orders. **The analytic content is clause (3)'s g-uniformity on the class (2),
i.e. (CEM-2) restricted to defect-free columns.**

**(iii) Statements that rest on the uncertified VALUE: none. The audit, item by item.**
- §16.7 Theorem NA-PRICE (ii), §17.2 Cor. LAW (b), §17.4 Theorem NA-PRICE^E (i), §17.6's two interface lines, §17.8 (b),
  §18.7's Theorem NA-PRICE^{E+} and Cor. E2-RED: **all labelled CONDITIONAL on a named input containing the constant**, with
  "c_lcr not certified" said explicitly in §16.7, §16.11 (ii), §17.5 and §17.8 (b). **No mislabel.** This agrees with
  REVIEW_PLD_S5 S5-25 ("no status error in PLD S5"; "I found nothing claimed PROVEN that rests on c_lcr"), reached here by an
  independent trace.
- **But one statement does rest on something worse than an uncertified constant, and it is a STATUS DOWNGRADE this session
  records:** §17.2 Cor. LAW (b) and §17.6's "(SF-cap)^{A,far}_θ at level k (HW H6): ⇐ (LCR)_k in G-form with G = w
  (directly…), c_sf = c_lcr, c_f = 0 exactly", and §17.4's parenthesis "(in particular HW's (E1) law ν^{(k),w}_k, **any w**)",
  are delivered from (LCR) quantified over a class for which no finite g-uniform constant exists ((i) last bullet). The
  IMPLICATIONS are valid; the INPUT is not merely uncertified but **expected false in that generality**. This is exactly
  review binding fix B1, reached independently here, and §18.7 restates everything on 𝔏^buf_k. **§17 is not edited (it is
  under review); the downgrade is recorded here and requested in §18.12.**
- **One number that is NOT a c_lcr matter, flagged because it is larger than any c_lcr effect.** §16.8 computes σ_fl² =
  16(1 + O(α_*))/λ_min with **λ_min ≥ 3.17·10⁻³** (sourced to RLARGE §0 and SF Proposition CI-0's 4.23·10⁻³). REVIEW_PLD_S3's
  binding fix **L0-1** instructs that wherever an N5-sf0 "gap" is quoted the numbers are λ_min ≈ 7·10⁻⁸² (product-rule m) or
  **≥ γ′(1 − ε_R)/9 ≈ 6.6·10⁻¹⁰** via Proposition RW-ℓ² (PROOF l.5322-5325). The two quote DIFFERENT sources, so L0-1 may or
  may not govern §16.8 — a question for the SF / PROOF owners, not decidable in this lane. **If it does, a_ret falls by the
  factor 3.17·10⁻³/6.6·10⁻¹⁰ = 4.80·10⁶** (check p6 D2), so a_ret/a_bad ≈ 8.03·10⁻⁷ becomes **≈ 1.67·10⁻¹³**, the K12
  fallback θ falls with it and n_H rises by 4.8·10⁶. **Not resolved here, not used here, and §18.7's a_A = min{λκε_1²/256,
  6θa_bad} does not depend on a_ret at all** — which is a further reason to prefer the §18.7 route: on it, the a_ret
  question stops being load-bearing for θ. Request in §18.12.

## 18.9 T15 (d): the match check, and what NA-PRICE^E becomes if (J-NS^cd) is discharged

| clause | RLARGE v3 row 10b / §3 | HW §24.3 (after SL-1) | HW §30.3 (E2^𝔉) | PLD §17.4 / §17.6 delivers | PLD §18.7 delivers |
|---|---|---|---|---|---|
| law | every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}} | ν^{(k),w}_k, w = h_k | ν^{R,F}_j weighted by h^{R,1}_j, every R ∈ 𝔉_𝔥, F_< free | every ν_G with L_G ∩ X_k(S) = ∅, **any w** | 𝔏^buf_k(R, S): HW's buffered weights only, every R ∈ 𝔉_𝔥, F_< quantified |
| set | every S ⊂ Λ_k | S under A ⊂ 𝒰_{k+1} | **far Y** ⊔ Γ's column, Γ at level j+1 | S with (C_S) | S with N_1(S) R-free and (C_S′) — covers far Y |
| allowance | "c_A·shadow sums" | ‖S‖_sh (union; slice STRUCK) | c_A‖col Γ ∪ Y‖_sh (patch) | **s_k(𝔥)** (slice) | **c_A = 0** |
| levels | every k | k ≥ 0 + level-0 clause | j ≥ k_0 + a (mis-levelled) level-0 clause | **k ≥ 2** | **k ≥ 1** |
| exponent | a_A ≥ θa_bad | a_A ≥ θa_bad | a_A ≥ θa_bad | a_A ≥ θa_bad ⟺ a_cd ≥ θa_bad | a_A ≥ θa_bad unconditional |
| form | probability | probability | one joint expectation | unconditioned probability | F-conditioned |
| joint with (SF-cap) | via CAP-dec | via CAP-dec | **built in** | not written | Cor. E2-RED |

**Findings (each a mismatch, each reported as such).**
- **M-1 (allowance; binding).** §17.4 l.1848/l.1856 and §17.6 deliver the per-level slice s_k(𝔥); HW struck it [SL-1] for the
  union form and HW §30.3 wants the patch form; by Proposition PATCH (ii) the slice is **incomparable** to both. §18.7
  delivers c_A = 0, which satisfies every one of the three. (Independently found here and in review S5-9/S5-10/B2, and in
  REVIEW_HW_S5 from the other side — the two reviews converging on the currency is correct.)
- **M-2 (set class; binding) — and the sharpening.** HW §30.3 asks the price of a **far** set Y. PLD §17's (C_S) does not
  cover it and GEO (ii) fails there (review S5-26 reason 2). **Sharpening (§18.2, §18.4): (C_S) is NOT the obstruction** —
  only its clause S ∩ 𝒰_k = ∅ is used by GEO (i), (iii), (iv), FT^far and COL-DEC, and Proposition FAR proves HW's far Y
  satisfies it automatically. The obstruction is GEO (ii), i.e. the WEIGHT, and **Lemma BUF closes it exactly** for one extra
  R-free ring, which Theorem CRC-2T can buy for ≤ ×82 on b_n, b_D, n_♯ (§18.4, check p6 B1).
- **M-3 (level range).** RLARGE and HW ask every k ≥ 0; §17 delivers k ≥ 2; §18.7 delivers k ≥ 1. **Level 0 remains OPEN**
  ((LCR)_0 / the Wilson window moment), and HW's own level-0 clause of (E2^𝔉) is mis-levelled (§18.6.2 Delta 2). TEL-f needs
  every level, so the interface is **not** delivered. This is the largest residual after (CEM^{COL}) itself.
- **M-4 (weight class; binding, and it cuts against PLD).** §17.4/§17.6's "any w" is STRONGER than HW asks and is expected
  FALSE (E1-1, X-1, §18.7.2 (α)). §18.7 restricts to 𝔏^buf_k. The sup-form statement is not to be proven.
- **M-5 (RLARGE only).** Row 10b still asks for every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}} and every S ⊂ Λ_k — which neither HW §24.3 nor
  HW §30.3 now asks, and which neither §17 nor §18 delivers. The row needs restating to the (E2^𝔉′) form.
- **M-6 (form).** HW's (E2^𝔉) is ONE joint expectation; §17.4's theorem is an unconditioned probability. Review B3 and §18.7
  state the F-conditioned form, which is what CAP-dec and (E2^𝔉) actually consume.
- **M-7 (F_< unquantified).** Free on PLD's side, §18.6.2 Delta 3; a declaration fix in HW, not a cost.

**What Theorem NA-PRICE^E becomes if (J-NS^cd)_k is discharged (with C_cd, a_cd ≥ θa_bad, allowance c_cd).** Its statement is
unchanged in form and becomes **(SDP)^{A,far}_θ in HW §24.3's shape**:
  E_ν[1{S ⊂ D_k}F] ≤ (C_Ae^{-a_Au_k})^{|S|}e^{c_cd‖S‖_sh}E_ν[F],  a_A = min{λκε_1²/256, 6θa_bad, a_cd} ≥ θa_bad,
  C_A = 4max{n_int(1−λ)^{-3/2}e^{λκε_1²R/256}, c_sf, 81n_int(1−λ)^{-3/2}e^{2λκε_1²R/256}, C_cd},
for **k ≥ 2**, S satisfying (C_S), and laws of COL-DEC's form — once M-1, M-4 and M-6 are applied (union currency, buffered
weights, F-conditioned). **But that is NOT (E2^𝔉), and four further items are needed, which is the main structural answer of
this session:** (1) the far-set class (M-2: Proposition FAR + Lemma BUF + the extra R-free ring, §18.2-§18.4); (2) the
allowance in a form the interface can read (M-1: Proposition PATCH, so (P0)/(P1) in the hypothesis); (3) the JOINT
combination with the (SF-cap) half in one expectation (M-6, M-7: Cor. E2-RED via CAP-dec); (4) levels k = 1 and 0 (M-3).
**So discharging (J-NS^cd) alone would not deliver what HW consumes.** §18.2-§18.4 supply (1) and (2) and half of (4)
(k = 1, through §18.7); (3) follows from §18.7; level 0 stays OPEN.

## 18.10 T17: check p6 (criteria checks/p6_criteria.md 12:50:40 UTC, md5 d6e90f4899385fbec5f668d033a2efeb, written BEFORE
the script; script checks/p6_pld.py 12:51:17 UTC, md5 12db2379…; output checks/p6_out.txt; stderr checks/p6_err.txt;
record checks/p6_time.txt)

- One run, 12:51:26 UTC, 0.04 s, 14.7 MB, exit 0, nice 10, one thread, `python3 -I`, no numpy/BLAS, load 2.52 at launch.
  **The numeric lock was NOT taken**, and deliberately: the brief exempts exact rational/symbolic arithmetic in plain python,
  and p6 imports only `fractions`, `math`, `sys` (no numpy, no linear algebra, no sampling). Justification recorded in
  checks/p6_time.txt. No re-run, no trap, no pkill, no process left.
- **SUMMARY AS RUN: FAIL: F2. All other criteria PASS, including every negative control (A3, B3n, E1n).**
- **The F2 failure, reported as a failure.** F2 asked for the exact identity 81 + 2401·32·80·Σ_{m≥1}3^{-m} = Δ_sh = 3073361
  with the INFINITE series; the script formed the finite partial sum Σ_{m=1}^{199} = ½ − 3^{-199} as an exact Fraction and
  demanded exact equality, which cannot hold. **This is a SCRIPT defect, not a mathematical failure and not a criterion
  defect.** Nothing was re-run and no file was edited after the run. The post-hoc hand arithmetic
  (2401·32·80/2 + 81 = 3073280 + 81 = 3073361) is recorded in p6_time.txt and **labelled post-hoc; F2 is NOT counted as
  passed.** §18.5 (b′)'s proof does not use the numerical value of Δ_sh, only that it is finite and depth-free, which
  §16.6 (b) and p4 D2b supply, so no statement in §18 moves.
- **Rigorous and load-bearing (all PASS):** A1 (exact c_pr = 1/1797760 = 5.562478·10⁻⁷, κ_min = 1/84270 = 1.186662·10⁻⁵);
  **A2** (the identity u·ε_1² ≡ (ε_1/g_K)² at u = 1/g_K², and its value **4.489·10¹⁵** at the recorded g_K² = 10⁻⁹⁴,
  ε_1 = 6.7·10⁻⁴⁰ — this is §18.7.2 (α)/(β)'s number, and the identity is why the two guises of the obstruction are the same
  quantity); **B1** (b_n(1,1) = 20416938755 exactly, reproducing HW's "≈ 2.04·10¹⁰c_+"; the one-extra-ring cost of §18.4 is
  exactly ×82 on both b_n and b_D); **B2** (g²_CRC = 4.8979·10⁻⁹⁷ at c_+ = 1, reproducing HW §30.6's recorded 4.9·10⁻⁹⁷ to
  0.0%; and ÷82.0000 after the ring); **B3** (log c_lcr = 10⁹ shifts g²_CRC by 1.0490, i.e. < 5%); **C1** (the a_A ≥ θa_bad
  equivalence holds with equality at κ_min, strictly at κ = 1, and FAILS at κ_min/2 — so the inequality is sharp);
  **C2** (a_A/a_bad = **1/4** exactly at θ = 1/24, κ = 1, λ = ½, i.e. the 6θa_bad entry binds; κ_crit = 1/14045 =
  7.119972·10⁻⁵); **C3** (the 2-branch assembly of §18.7, 0 violations); **E1** (the geometric series identity and the strict
  bound Σ_{r=1}^{i}L^{k-r} = (L^k − L^{k-i})/(L−1) ≤ L^k/2 < L^k at L = 3, all k ≤ 30); **F1** (the detached-cube union-form
  shadow sum is 82 + 256(K−j−2), linear in the depth — Proposition PATCH (iii)); **G1** (m_* = 41.3678 and the coherent
  one-level price exponent 6L⁴a/g_K² = 4.86·10¹⁰ ≫ m_*·log 324 = 239.14, i.e. §18.5 (e)'s price beats the 324-per-level count
  over the whole admissible chain depth, by eight orders).
- **Negative controls (all behaved as designed):** A3 (at ε_1 := g_K the A2 quantity is exactly 1, so §18.7.2's gap is the
  gap and not an artefact of the formula); B3n (log c_lcr = 10¹¹ WOULD bind, shift 5.8979 — so B3 is a real inequality);
  E1n (at L = 2 the shrinking bound FAILS at (k, i) = (2, 2), so L ≥ 3 is load-bearing in §18.7.2 (δ)).
- **Informational / conditional:** D1 (dof = 3n_int·81 = 52488, Gaussian log c_1 = 18190.95 at λ_f = ½ — the heuristic's own
  value, thirteen orders below §18.8 (ii)(5)'s side condition 10⁹, and NOT a proven constant); D2 (the λ_min ratio
  3.17·10⁻³/6.6·10⁻¹⁰ = 4.8030·10⁶, so a_ret/a_bad would become 1.6719·10⁻¹³ **if** REVIEW_PLD_S3's L0-1 governs §16.8's
  λ_min — a question for the SF/PROOF owners, §18.8 (iii), with no claim attached).
- **Scope.** Arithmetic about recorded constants and about bounds PLD/HW already state. p6 tests NOTHING about the lattice
  measure: not (CLS-min), not (LCR), not (CEM^{COL})/(CEM-1)/(CEM-2), not (E2^𝔉), not (J-NS^cd), not Theorem CRC-2T, and
  nothing nonabelian. In particular **no number in p6 is evidence for or against the single open statement of §18.7.**

## 18.11 T16 + outcome against the pre-stated targets (§18.0), status changes, and tally

**T15 (a): MET.** (E2^𝔉) is restated in PLD's language and decomposed into (D1) + (D2) + (D3) (§18.1), with a per-item
verdict for GEO, FT^far, COL-DEC, DIL-L, MD, NA-PRICE^E (i) and Cor. LAW. Verdict: session 5 supplies the ARCHITECTURE and
the top-level conversion, and not the set class, the push-down for HW's weight, the level range or the two open halves —
**which is REVIEW_PLD_S5 S5-26's verdict, reached independently (§18.3 records the provenance), with one sharpening: (C_S)
is not the obstruction, GEO (ii) is** (§18.2, §18.9 M-2). **(NP-F8) MET**, with the minimal enlargement named (one R-free
ring) and its cost computed in HW's own constants (×82; p6 B1, B2).
**T15 (b): (NP-F6) MET.** Induction on levels does not close (J-NS^cd). Three independent reasons (§18.5): no base case; no
contraction, because CW's certificates across levels are NESTED not additive and the one additive currency (DIL-L (ii)'s
kernel energy) is identically zero on centre defects; and the favourable coherent sub-case cannot cash its (huge, p6 G1)
pointwise certificate. **Compounding is NOT a reason: §18.5 (b′) PROVES the union-form excess line
‖x(S)‖_sh ≤ ‖S‖_sh + (1 + Δ_sh)|S| that review item B2 (b) asked for, so Cor. LAW (c) is correct in the union currency.**
Branch 2 of REVIEW_PLD_S4 attempted (§18.5 (f)): **finding (EG-cur)** — (EG) is VACUOUS in the kernel-energy currency and
non-empty in the curvature-energy currency, and the single missing ingredient is the identification of the S4′ kernel mode
with a local curvature minimiser, named **(EG-link)** and left OPEN.
**T15 (c): PARTIAL SUCCESS as pre-stated, and the honest qualifier.** ONE statement, **(CEM^{COL})_k** (§18.7.1), yields
both walls: Proposition ONE derives (SF-cap)^{COL}, (J-NS^cd), Theorem NA-PRICE^E (i), the new Theorem NA-PRICE^{E+} and
(E2^𝔉′) from it plus (CLS-min). It is single-level, a moment, defect-tolerant, carries allowance (P0) (c_A = 0) and covers
k ≥ 1. **It is STRICTLY STRONGER than the two hypotheses it replaces** — stated plainly in §18.7's "Logical strength" —
so this is a consolidation, not a discharge; **(J-NS^cd) is not discharged and Theorem NA-PRICE^E (i) stands as session 5
left it.** The pre-stated "Success" bar (which required the implications from (CLS-min) and the one statement ALONE, which
is met, AND that it not be a two-level defect probability, which is met) is reached except that the statement is stronger
than the conjunction; §18.0 did not require weakness, so **T15 (c) is recorded as the pre-stated Partial success, with the
strength disclosed**, not as Success.
**T15 (d): MET.** Seven mismatches M-1…M-7 (§18.9), the three-way table, and the exact statement of what NA-PRICE^E becomes
if (J-NS^cd) is discharged — together with the finding that **discharging it alone would still not deliver (E2^𝔉)**, four
further items being needed, of which §18.2-§18.7 supply three and a half.
**T15 (e): MET.** §18.8: the value of c_lcr is NOT load-bearing (it enters only as log c_lcr against b_n ≈ 2.04·10¹⁰c_+;
p6 B3/B3n), existence + uniformity are, the weight-class uniformity is unavailable in §16.7's form so **no certificate for
(LCR) as written is possible**, and the certificate target is stated in five clauses. **No statement labelled PROVEN rests
on the uncertified value** (independent audit, agreeing with review S5-25) — but §17.2 Cor. LAW (b), §17.4's "any w" and
§17.6's two interface lines rest on an input **expected false in that generality**, which is a status DOWNGRADE recorded
below. One number flagged that is larger than any c_lcr effect (the λ_min / a_ret question, p6 D2).
**T16: MET** (this section; the status changes are listed with their direction). **T17: MET with one disclosed FAIL**
(F2, a script defect; §18.10). **T18: MET** (§18.12; nothing outside PLD.md, PLD_LOG.md and checks/p6_* was written).

**Counted, PROVEN-HERE (unreviewed): 2 items.**
- **[E6] (1)** The interface repair, one item: **(C_S′)** (the clause audit of (C_S)), **Lemma FT^far′** (FT^far under
  L_G ∩ ℓ(S) = ∅), **Proposition FAR** (i)-(ii) (HW's far sets and animal columns satisfy (C_S′)), **Lemma BUF** (one R-free
  ring ⇒ L_w ∩ X_j(𝒜) = ∅, so FT^far and COL-DEC apply to HW's own weight on FAR sets) and **Proposition PATCH** (the
  allowance-currency reconciliation: monotonicity, the slice's incomparability, the per-cube-depth prohibition, and the
  localisation of the patch allowance into the hypothesis).
- **[E6] (2)** **Theorem NA-PRICE^{E+} (i)** as an implication ⇐ (CLS-min) + (CEM^{COL}), with **Corollary E2-RED**
  ((E2^𝔉′) from the same input) and **Proposition ONE** (both walls from the one statement).
**Not counted:** §18.5's Proposition CHAIN (structure/arithmetic about the available certificates) including the union-form
excess line (b′) and the branch-2 finding (EG-cur); Proposition SPLIT (§18.7.2, logic); §18.8's audit; §18.9's table.
**ARGUED (uncounted):** §18.5 (e) (the coherent-chain curvature growth and its depth bound; abelian, linear order).
**OPEN, newly named here:** **(CEM^{COL})_k** [node A; the single residual], split into **(CEM-1)_k** (the defect-tolerant
unweighted moment: (LCR) + the main-term reduction off G_Q + u-uniformity of the activity bounds on [(1−λ_f)u, u]) and
**(CEM-2)_k** (the decoupling / screening estimate for the buffered far weight); **(EG-link)** [node A; the branch-2
ingredient]; **𝔏^buf_k(R, 𝒜)** (the B1-compliant law class) and **(E2^𝔉′)** (HW's (E2^𝔉) with the three declared changes).
**Renamed per review B4:** (SF-cap)^𝔉 → **(SF-cap)^{COL}**.

**Status CHANGES to earlier items, with direction.**
- **DOWNGRADE.** §17.2 Cor. LAW (b), §17.4's parenthesis "any w", §17.6's "(SDP)^{A,far} for every far weight w" and
  "(SF-cap)^{A,far} ⇐ (LCR)_k in G-form": the implications stand, the INPUT is expected false in that generality
  (§18.7.2 (α); HW E1-1; reviews X-1 and S5-8). Everything in §18 is restated on 𝔏^buf_k.
- **DOWNGRADE.** §17.4/§17.6's allowance in the slice s_k(𝔥) does not deliver HW's H7 or HW's (E2^𝔉): the slice is
  incomparable to both (Proposition PATCH (ii)).
- **UPGRADE.** The far-set class and the push-down for HW's weight, recorded as missing by review S5-26, are supplied
  (Proposition FAR + Lemma BUF), at a computed cost in HW's constants.
- **UPGRADE.** The union-form excess line review B2 (b) left open is PROVEN (§18.5 (b′)).
- **UPGRADE.** Level 1 is covered by Theorem NA-PRICE^{E+} (§17 covered k ≥ 2); the bottom hole shrinks from two levels to
  one. Level 0 remains OPEN.
- **UPGRADE (conditional).** K12: on the §18.7 route a_cd = 6θa_bad, so θ ↑ 1/24 with a_A = a_bad/4 (p6 C2), and the
  fallback θ ≈ 8·10⁻⁷ (n_H × ≈ 5·10⁴) is no longer forced; a_ret stops being load-bearing for θ, which also defuses the
  λ_min question of §18.8 (iii).
- **NO CHANGE.** (J-NS^cd), Theorem NA-PRICE^E (i), Lemma MD, Lemma DIL-L, the p5 numbers and (NP-F5) all stand.
**Tally proposal: +2 PROVEN-HERE (unreviewed); 0 OPEN items closed.** Row 10b's residual is EITHER (J-NS^cd) (session 5,
unchanged) OR (CEM^{COL}) (session 6, one hypothesis instead of two, and the only one of the two that also delivers
(E2^𝔉′)); the lane carries both routes and the integrator chooses.

**The single biggest remaining obstruction in this scope, named.** **(CEM-2)**: a decoupling estimate, under the past law of
a pattern in 𝔉_𝔥, between HW's buffered far weight h^{R,1}_m·1{buffer good} and the coarse column-energy functional
F^col_Q(U_{k-1}), across one R-free ring. It is the whole screening content of (E2^𝔉); it is NOT obtainable from the
buffer-good event alone, because the event bounds curvature by ε_1 while a g-independent constant needs it bounded by
≈ g_K, and those differ by the factor 4.489·10¹⁵ (p6 A2, A3). Everything else in the lane is proven, or reduces to
(CEM-1), which is three named single-level small-field/representation statements.

## 18.12 FOR OTHER FILES (session 6; not edited)

Nothing below is applied anywhere. Session 6 wrote only PLD.md (appended), PLD_LOG.md (appended) and checks/p6_*. No git
command was run; no commit, push or PR; no axiom or CL edit.

**To the PLD owner (next session's in-place [RPLD5-fix] pass; §17 is deliberately untouched here because REVIEW_PLD_S5 was
being written against it).**
1. Apply review B1-B6 as the review states them. §18 is already written in the B1/B2/B3/B4-compliant form, so §18 needs no
   change: use §18.7.0 for the law class, §18.6.1 for the allowance currency, §18.7's theorem statement for the
   F-conditioned form, and (SF-cap)^{COL} for the renamed input.
2. Record in §17.6 and §17.9 the DOWNGRADE of §18.11 (the "any w" / (E1) quantifier and the slice currency), and in §17.3
   the review's S5-13 correction (max_e|W_e| = 1/27 over supp W, 2/81 only over the interior links of a corner block).
   Nothing in §18 uses either number.
3. §17.4's (J-NS^cd) and Theorem NA-PRICE^E (i) should carry the union allowance ‖S‖_sh and the F-conditioned form; §18.5
   (b′) supplies the excess line B2 (b) asks for, ready to quote.

**To the HW owner (lane H) — four requests, all cheap, one of them a renegotiation.**
1. **Buy one extra R-free ring in Theorem CRC-2T step (4)**: replace R″ := R′^{-Col(Y)} by
   R‴ := R′^{-(Col(Y) ∪ Col(N_1(col 𝒟 ∪ Y)))}. It is upward closed, hence in 𝔉_𝔥; it is bought by CRC-2T's own induction
   hypothesis since N(R′) < N(R); the geometric price is one factor 81 (‖N_1(X)‖_sh ≤ 81‖X‖_sh, from Lemma SL's own step
   Σ(N_1(X)) ⊂ N_1(Σ(X))), so step (4)'s e^{c_U‖·‖_sh} becomes e^{82c_U‖·‖_sh} and c_+ = c_A + c_U becomes c_A + 82c_U.
   **Exact cost (check p6 B1, B2): b_n and b_D grow by exactly ×82 and g²_CRC falls by exactly ×82.0000 (4.8979·10⁻⁹⁷ →
   5.9731·10⁻⁹⁹ at c_+ = 1); n_♯ grows by ×82.** g-independent, so a lower g_0 and a bigger n_♯, not a loss of uniformity.
   **Why: without the ring, h^{R,1}_j may read the crossing links of X_j(Y), GEO (ii) fails and Lemma COL-DEC breaks, so
   node A has no product-kernel law one level down for far cubes (review S5-26 reason 2). With the ring, Lemma BUF (§18.4)
   makes the whole of PLD §17.2-§17.4 available on far sets.** HW must re-run its own step (4)-(5) with R‴ to confirm that
   nothing else in its proof reads R″ specifically; §18.4 checks only the parts of CRC-2T it quotes.
2. **Renegotiate (E2^𝔉)'s allowance clause.** By Proposition PATCH (§18.6.1), what node A can and should owe is "the
   small-field moment carries at most a PER-CUBE constant and no shadow sum" (form (P0) or (P1)); HW's union-form patch
   allowance e^{c_A‖col Γ ∪ Y‖_sh} then follows by monotonicity, because every set node A prices is a subset of the patch.
   State it that way so the lanes stop quoting incomparable currencies. **And note the gain: §18.7 delivers c_A = 0, so
   c_+ = c_A + c_U drops to c_U and HW's own b_n, b_D fall by the factor (c_A + c_U)/c_U, g²_CRC rising by it.**
3. **Quantify F_< universally** in (E2^𝔉) ("for every bounded measurable F_< ≥ 0 of U_{<k_0}"). It is free on node A's side:
   F_< reads only levels ≤ k_0 − 1 ≤ j − 1, i.e. strictly finer than the links FT^far, COL-DEC and the moment's G-hypothesis
   are about, and in those proofs it is one of the "Φ_{k′}, k′ < k" factors already excluded (§18.6.2 Delta 3).
4. **Fix the level-0 clause of (E2^𝔉)**, which is mis-levelled: the body has Γ at level j + 1 and Y at level j, while the
   clause puts both at level 0. The consistent readings are Γ at level 0 with the Wilson window X_Q and no Y, or Γ at level 1
   with Y at level 0. Node A delivers neither today (§18.9 M-3): k = 1 is covered by §18.7, k = 0 is OPEN.
5. **Reported back, not absorbed (as the lead asked): the TF-1 switch-off is NOT a node-A regression.** PLD §17.2 builds its
   past law with the finer capped spectators Φ_{k′}, k′ < k, already inserted, and Lemma GEO (iv) is exactly the clause that
   handles Φ_{k-1}. So HW §30.5's finer-first order IS the law PLD §17 is written for (review S5-26 says the same). What
   TF-1 protected was the (E1) form of the weight, which is dead for other reasons (E1-1). No action needed beyond deleting
   the worry.

**To the RLARGE integrator.**
1. **Row 10b.** Two routes, both node A's, and the row should name both: (i) (SDP)^{A,far} ⇐ (CLS-min) + (SF-cap)^{COL} +
   (J-NS^cd) (PLD §17.4; k ≥ 2); (ii) (SDP)^{A,far} ⇐ (CLS-min) + **(CEM^{COL})** (PLD §18.7; k ≥ 1, c_A = 0, a_A ≥ θa_bad
   unconditional, and it also delivers (E2^𝔉′) by Cor. E2-RED). Route (ii) has ONE hypothesis and is the only one that
   reaches HW's (E2^𝔉); its hypothesis is strictly stronger. Add rows **(CEM^{COL})** [node A, P], **(CEM-1)**, **(CEM-2)**
   and **(EG-link)** [node A].
2. **Row 10b's quantifiers are stale** (§18.9 M-5): it asks every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}} and every S ⊂ Λ_k, which neither
   HW §24.3 nor HW §30.3 asks and neither PLD §17 nor §18 delivers. Restate it to HW's (E2^𝔉′) form.
3. **The requirement "never derived from (SDP)^A at level k − 1"** (RLARGE l.396-404, quoting HW §18.1) needs a ruling for
   one case: Proposition CD (b)'s CONTRACTING level induction (324ηe^{a_AR} ≤ 1) is convergent, not LOOP-const, so it is not
   obviously what the prohibition is aimed at. §18.5 does not rely on the ruling either way (CD (b) fails for three other
   reasons), but if the ruling is "prohibited" then CD (b) should be struck from the route list rather than left open.
4. **K12.** On route (ii), θ ↑ 1/24 with a_A = a_bad/4 and the fallback θ ≈ a_ret/a_bad ≈ 8·10⁻⁷ is not forced; a_ret then
   enters only (RLF-0)/(RLF-δ), where any a_ret > 0 suffices. Record both readings against the chosen route.
5. **Critical path.** With (CRC-1) dissolved-but-conditional on (E2^𝔉) [relayed from REVIEW_HW_S5], item 1 of the critical
   path is **(E2^𝔉)**, i.e. node A's; §18.7/§18.11 name its single residual as **(CEM-2)** plus **(CEM-1)**.

**To the SF / PROOF owners (one question, and it is bigger than any c_lcr effect).**
PLD §16.8 computes σ_fl² = 16(1 + O(α_*))/λ_min with λ_min ≥ 3.17·10⁻³, sourced to RLARGE §0 and SF Proposition CI-0
(4.23·10⁻³). REVIEW_PLD_S3's binding fix **L0-1** instructs that wherever a "gap" of N5-sf0 is quoted the numbers are
λ_min ≈ 7·10⁻⁸² or ≥ γ′(1 − ε_R)/9 ≈ 6.6·10⁻¹⁰ via Proposition RW-ℓ² (PROOF l.5322-5325). **Does L0-1 govern §16.8's
λ_min, or are the two quoting genuinely different operators?** If it governs, a_ret falls by ×4.8030·10⁶ (p6 D2), so
a_ret/a_bad ≈ 8.03·10⁻⁷ becomes ≈ 1.67·10⁻¹³, the K12 fallback θ falls with it, and n_H rises by the same factor. Not
decidable in this lane; not used in §18 (route (ii)'s a_A does not involve a_ret at all).

**To the next reviewer of this lane (REVIEW_PLD_S6), the three places to attack first.**
1. **Is (CEM^{COL}) false?** §18.7.2 (α) shows the sup-over-weights version is; §18.7.2 (β) shows the buffer-good event
   cannot supply the constant. Look for a buffered weight h^{R,1} and a pattern R ∈ 𝔉_𝔥 under which the conditional mean
   column energy is bounded below by a g-independent multiple of ε_1². If one exists, route (ii) dies and the lane returns
   to branch 2 / (EG-link).
2. **Is Lemma BUF's ring enough?** It gives L_w ∩ X_j(𝒜) = ∅ for N_1(𝒜) R-free. Check that nothing else in PLD §17.2-§17.4,
   used on far sets, silently needs GEO (ii) itself rather than its consequence, and that Proposition FAR (ii)'s hypothesis
   Γ ∩ A_{j+1}(𝔥) = ∅ really covers every Γ that Theorem CRC-2T feeds (its animals, and 𝒰_{j+1} in Cor. CRC-HW).
3. **Is Proposition ONE's strength claim right?** It asserts (CEM^{COL}) ⇒ (SF-cap)^{COL} + (J-NS^cd) and no converse. Try
   the converse: does the pair, plus (CLS-min) and the kernel lemmas, give back the defect-tolerant moment? If it does, the
   consolidation is free and §18.7's "strictly stronger" disclosure should be withdrawn in PLD's favour.

# Session 7 (2026-10-28, lane E)

Read for this session before the pre-statement (read-only, nothing written): the session-24 DRIVE_BRIEF; HANDOFF.md
(post-session-24 rewrite) in full; **PLD.md §18 (session 6) in full, §16.5-§16.8 and §17.2-§17.6 as pointed to from §18**;
PLD_LOG.md's session-6 entries; **HW.md §0 (conventions), §4 (tower energies, Lemma TE, Lemma W-bad, Lemma DJ), §21-§22
(Lemma TILT, Lemma FP, Lemma NR, Theorem LI^U-0, Corollary LI-0), §23 (Proposition LI-pw), §30.1-§30.4 (𝔉_𝔥, Theorem
LI^U-0′, Lemma SH-att, Lemma COL, (E2^𝔉)), §34 (session-6 targets), §37 ((E2^𝔉′) restated, the level clause (0a)/(0b), the
seven deltas, the TF-2 both-positions record, the §24.3 narrowing), §38 (the eleven errata), §40 (outcomes), §41 (FOR OTHER
FILES)**; REVIEW_PLD_S5.md and REVIEW_HW_S5.md (both binding) in the parts §18 and §37 quote; REVIEW_PLD_S4.md's branch 1 /
branch 2 of Part 3; SESSION24_RESULTS.md's PLD-s6 and HW-s6 entries. An unwritten exploratory pass chose the targets below;
no session-7 text, criteria or script existed when it ran.

## 19.0 PRE-STATED (session 7) — statements only (written 2026-10-28 14:03 UTC, `date -u`; THE FIRST EDIT OF THIS SESSION:
before any session-7 derivation, before checks/p7_criteria.md, and before any session-7 check)

**This section cites nothing produced in session 7.** File stat of PLD.md *before* this append: 312681 bytes, 2931 lines,
md5 4a6a0f251567738cebf28cfdaac352ea, which is PLD_LOG's session-6 closing stat exactly. Session 7 **APPENDS ONLY**: it
alters no line of §0-§18, and it writes nothing outside PLD.md, PLD_LOG.md and checks/p7_*.

**Setting.** That of §18.0, unchanged: SU(2); bad-only, history-independent defects; (F_R) with g_K² ≤ 1/(2R);
ε_1 ≤ min{1/(4A_d), t_pr}; a_bad = c_pr ε_1², c_pr = 1/(640·53²); max{6θ, 24θ}(1 + 2Rg_K²) < 1, and λ_f := 24θ(1 + 2Rg_K²).
Laws: the class 𝔏^buf_k(R, 𝒜) of §18.7.0. Objects: (CEM^{COL})_k, (CEM-1)_k, (CEM-2)_k of §18.7.1-§18.7.2; HW's (E2^𝔉′) and
its level-0 readings (0a) (Γ at level 0, Wilson window, Y = ∅) and (0b) (Γ at level 1, Y at level 0) of HW §37.

**T19 (the target). (CEM-2) and (CEM-1), by the mechanism §18.7.2 (β)/(γ) and REVIEW_HW_S5 both name — the weight's
typicality under the measure, not the buffer-good event.** Deliver, with all quantifiers:
- **(a) (CEM-2).** Either a proof, or a reduction of it to a strictly smaller named statement, by one of the two routes the
  brief names: (i) a large-deviation / Chebyshev split in which the non-decoupling configurations are paid for by the
  measure, or (ii) a conditional-independence / Markov structure across the R-free ring. For whichever route is taken,
  state exactly what is PROVEN, what the residual is, and **the price in the lane's own currency** (a per-cube constant, a
  single constant, or an allowance), together with an explicit comparison against the 4.489·10¹⁵ that §18.7.2 (α)/(β) price
  the EVENT route at. Any claim that the mechanism closes (CEM-2) must come with the residual named and its status.
- **(b) (CEM-1), one part at a time**: (LCR); the main-term reduction off G_Q; u-uniformity of the activity bounds on
  [(1 − λ_f)u, u]. For each: PROVEN, reduced (to what), or untouched (why). A proof that two of the three are the same
  statement, or that one of them is not needed, counts as progress and is to be stated as such.
- **(c) the restated (LCR)**, in the form (CEM-1) actually consumes, with every quantifier, replacing the form §16.7 states
  (for which §18.8 (i) proves no certificate is possible), and with a statement of which of §18.8 (ii)'s five certificate
  clauses the restatement keeps, drops or replaces.
- **(d) the level-0 clause.** Decide which of HW §37's (0a) and (0b) is the weaker, and attack it: either deliver it, or
  reduce it to a named statement whose SIZE and KIND are stated (single-level / finite-dimensional / paper-scale).
- **(e) the single remaining obstruction to (SDP)^A**, named, with its kind and its owner.
- **Success:** (CEM-2) PROVEN from (CLS-min) and single-level small-field inputs already named in §16-§18, with constants
  explicit and independent of g, K, T, k, 𝔥, R and the pattern; or (CEM^{COL}) replaced by ONE statement strictly weaker
  than it which implies it and which is not (CEM-2) renamed.
- **Partial success:** a PROVEN reduction of (CEM-2) to a named statement that is strictly smaller than (CEM-2) (fewer
  quantifiers, a probability rather than a moment, a first moment rather than an exponential moment, one scalar rather than
  a product over cubes, or weight-free rather than weighted), with the reduction's price computed; or the same for (CEM-1);
  or (0a)/(0b) reduced to a finite-dimensional statement.
- **Valid failure outcomes:** **(NP-F10)** the Markov / conditional-independence structure across the R-free ring does not
  exist, with the exact factor of the past law's density that breaks it; **(NP-F11)** the typicality route closes (CEM-2)
  only at a price that is not in an admissible currency (k-, K-, T-, 𝔥- or volume-dependent), with the price computed and
  the dependence exhibited; **(NP-F12)** the restated (LCR) is not consumable by (CEM-1) because the consumer needs a
  quantifier the restatement drops, with the consumer's own line quoted; **(NP-F13)** (0a) and (0b) are both strictly
  harder than the k ≥ 1 case for a named structural reason (no finer level to condition on), with the reason proven.
- **Not success:** a constant or exponent depending on k, K, T, 𝔥 or the volume presented as uniform; a per-level or
  per-ring recursion presented as convergent without an explicit convergence factor AND an explicit check that nothing
  compounds; any statement quantified over ALL far weights or over a sup of weights (§18.7.2 (α), review B1); any use of
  the slice currency s_k(𝔥); any input that is (CEM-2), (J-NS^cd) or (CEM^{COL}) renamed; claiming PROVEN for a statement
  whose constant is c_lcr, c_cem, c_1, c_2 or any other uncertified constant; any rebuild on the PLD-desc "Reading" /
  look-ahead architecture (REVIEW_PLD_S3 Arch-1/2/3).

**T20 (status discipline).** Every item added in §19 carries exactly one of PROVEN-HERE / ARGUED / CONDITIONAL (with the
named input) / OPEN, and every status CHANGE to a session-4, -5 or -6 item is recorded as a change with its direction in
§19.10. Downgrades are reported in the same place as upgrades. Indicative power counting is labelled indicative and is
never counted.

**T21 (check p7; criteria file checks/p7_criteria.md written BEFORE checks/p7_*.py, containing NO constant derived in
session 7).** Exact rational / Decimal arithmetic only (plain python, `fractions`, `decimal`, single thread, no BLAS, no
numpy, no numeric lock per the session-24 brief's exemption): (A) the recorded identity u·ε_1² = (ε_1/g_K)² = 4.489·10¹⁵ of
p6 A2 re-formed independently, and the margin (1 − λ_f)·u·ε_1² at λ_f = ½; (B) the equipartition value
(dof/2)·log(1/(1 − λ_f)) at dof = 52488 and λ_f = ½ against p6 D1's recorded 18190.95, and against §18.8 (ii) (5)'s side
condition 10⁹; (C) the one-step coupling ratio u_k/u_{k-1} ≤ (1 − Rg_k²)^{-1} ≤ 1 + 2Rg_K² under Rg_K² ≤ ½, as an exact
rational inequality at the recorded R and g_K²; (D) the outward-ring sum Σ_{r≥1} r^{d-1}·r^{-2(d-2)} at d = 4 (the
indicative power count of the boundary-charge regress), compared against a convergent control at d = 5. Each criterion is
labelled PRE-REGISTERED (outcome unknown when written) or CONFIRMATORY (a check of something proven earlier in the
session), with a negative control for (B) and (D).

**T22 (requests for other owners).** Everything session 7 wants changed in HW.md, RLARGE.md, PROOF.md, NORMS.md, SQ.md or
HANDOFF.md is written only as a request in §19.11 "FOR OTHER FILES (session 7; not edited)". No file but PLD.md, PLD_LOG.md
and checks/p7_* is touched. **No git command is run.**

# Session 7 derivations (written after §19.0, from 14:06 UTC; §19.1-§19.8 were written BEFORE checks/p7_criteria.md, which
contains no constant derived in this session; the order is disclosed in §19.9 and in PLD_LOG)

**Index convention for §19.** That of §16-§18, with the following written out once, because every statement below depends
on exactly which variables each functional reads. Levels are HW §0's: the level-m field U_m lives on the **level-m links**,
whose endpoints are **level-m sites**; a **level-m cube** Q is the L^d block of level-m sites (81 at d = 4, L = 3), so Q has
**n_int = 216** interior level-m links ℓ(Q) (both endpoints at sites of Q) and 81 **level-(m−1) descendants**
col_{m-1}(Q) (one level-(m−1) cube per level-m site of Q). region(Q) := the set of unit cells under Q. For a set 𝒳 of
level-m cubes, ℓ(𝒳) := ∪_{Q∈𝒳}ℓ(Q), and
  **𝔏_{m}(𝒳) := the level-m links both of whose endpoint sites lie in cubes of 𝒳**
(so ℓ(𝒳) ⊂ 𝔏_m(𝒳), the difference being the links crossing between two cubes of 𝒳). Chain data (HW §0, quoted and used
below, not re-derived): W = e^{-S_0(U_0)}Π_{m<K}K_m(U_{m+1}, U_m), S_0 = u_0Σ_p s(U_0(p)), K_m = Π_c k^{(m)}_c with
k^{(m)}_c(V; M) = e^{-κu_mφ_M(V)}/∫e^{-κu_mφ_M}, u_m = 1/g_m², and the equalised chain energy
E(chain) = Σ_p s(U_0(p)) + κΣ_mΦ_m(U_m, U_{m+1}), Φ_m(U, V) = Σ_cφ_{M̄_c(U)}(V_c).

## 19.1 What each functional reads (Lemma READ), and a gap in §18.7.0's use of Lemma BUF

Fix k ≥ 1, a finite set A of level-k cubes, A′ ⊂ A, and write **S := A ∖ A′**. The objects of (CEM^{COL})_k are
  **Z := Π_{Q∈S}e^{θY^f_Q},  Y^f_Q = 24u_kF^col_Q(U_{k-1});  w := h^{R,1}_m·1{Buf^R_ρ(𝒜_m) ∩ D_m = ∅};  F.**

**Lemma READ: PROVEN-HERE (elementary; it is bookkeeping, counted with Lemma DLR below).**
- **(i) Z reads U_{k-1} on 𝔏_{k-1}(col_{k-1}(S)) and on nothing else.** By HW §4, F^col_Q(U_{k-1}) is the infimum over
  (U_0, …, U_{k-2}) of the chain terms of levels ≤ k−1 in Q's column, whose **level-(k−1) terms are the kernel terms
  κφ_{M̄_c(U_{k-2})}(U_{k-1,c}) of the level-(k−1) links c with both endpoints in Q's level-(k−1) descendants**, i.e.
  c ∈ 𝔏_{k-1}(col_{k-1}(Q)); all other terms are functions of (U_0, …, U_{k-2}), over which the infimum is taken. The
  infimum of a family of functions of U_{k-1}|_{𝔏_{k-1}(col_{k-1}Q)} is such a function.
- **(ii) The columns of distinct level-k cubes are disjoint**, and so are the sets 𝔏_{k-1}(col_{k-1}(Q)) — because the
  level-(k−1) cubes under distinct level-k cubes are distinct and the level-(k−1) sites are partitioned among the
  level-(k−1) cubes. Hence Z factorises over Q ∈ S into functions of disjoint blocks of U_{k-1}.
- **(iii) 1_{R,k-1} factorises per level-(k−1) cube**, each factor 1{ζ_x = 0} reading U_{k-1} on ℓ(x) only (bad-only
  defects, interior plaquettes). For x ∉ col_{k-1}(S), ℓ(x) ∩ 𝔏_{k-1}(col_{k-1}(S)) = ∅.
- **(iv) Φ_{k-1} reads no link of 𝔏_{k-1}(col_{k-1}(S)) when S ∩ 𝒰_k = ∅.** Φ_{k-1} = Π_{Q″∈𝒰_k}e^{θmin{π_{Q″},Y^f_{Q″}}}
  reads U_{k-1} on 𝔏_{k-1}(col_{k-1}(Q″)) by (i); Q″ ∈ 𝒰_k and S ∩ 𝒰_k = ∅ give Q″ ∉ S, and (ii) gives disjointness. [This
  is Lemma GEO (iv)'s content, rebuilt in the present notation; it uses only the clause (C_S′) of §18.2.]
- **(v) F_< reads no link of U_{k-1} at all**, since F_< is a function of U_0, …, U_{k_0-1} with k_0 ≤ k − 1.
- **(vi) The weight.** By HW Theorem LI^U-0′, h^{R,1}_m(U_m) is insensitive to the level-m links **all of whose endpoint
  cubes are R-free**, and the buffer indicator reads interior plaquettes of non-R-free cubes at level-(m+1) index distance
  ≥ 2 from 𝒜_m. So **w reads no link of 𝔏_m(𝒜_m) provided every cube of N_1(𝒜_m) is R-free** (a level-m link with an
  endpoint site in a cube of 𝒜_m has both endpoint cubes in N_1(𝒜_m)). This is Lemma BUF of §18.4.

**Finding (BUF-CC) [a gap in §18.7.0, with its repair and its price]: PROVEN-HERE.**
§18.7.0 applies Lemma BUF "at level m, applied to 𝒜_m, whose N_1 is R-free", with 𝒜_k := 𝒜 and **𝒜_{k-1} := col_{k-1}(𝒜)**,
under the hypothesis "**N_1(𝒜) R-free**" stated at level k. **That hypothesis does not give what Lemma BUF needs at
m = k − 1.** By HW §30.1, a level-m cube x is R-free iff its **open** column {(i, π^{i-m}(x)) : m < i ≤ K − 1} misses S_R.
For a level-(k−1) cube x with π(x) = Q, the open column of x is {(k, Q)} ∪ (the open column of Q). Hence
  **x is R-free ⟺ Q is R-free AND (k, Q) ∉ S_R ⟺ the CLOSED column [Q] misses S_R.**
"N_1(𝒜) R-free" is the open-column statement for the level-k cubes of N_1(𝒜) and says nothing about the pairs (k, Q)
themselves. Since N_1(col_{k-1}(𝒜)) ⊆ col_{k-1}(N_1(𝒜)), Lemma BUF at m = k − 1 requires
  **(RING-cc): [N_1(𝒜)] ∩ S_R = ∅ — every pair (i, π^{i-k}(Q)), i ≥ k, Q ∈ N_1(𝒜), is unconstrained (closed column).**
*Repair.* Replace the hypothesis "N_1(𝒜) R-free" by (RING-cc) throughout §18.7.0, §18.7.1 and Theorem NA-PRICE^{E+}. Nothing
else in §18.2-§18.7 changes: (RING-cc) ⇒ N_1(𝒜) R-free, and Proposition FAR (i)-(ii), Lemma FT^far′ and Lemma COL-DEC use
only (C_S′).
*Price, and it settles a cross-lane disagreement.* The relaxation that buys (RING-cc) inside Theorem CRC-2T′ step (4) is of
the **closed** column [N_1(·)] rather than the open one Col(N_1(·)). HW §41 item 4 (Lemma RING) prices the open column at
**×17** on c_U, with the explicit reason "Only the OPEN column enters #_{R′}, so the m = 0 term never appears"; for the
closed column the m = 0 term **does** appear, and HW's own two inequalities give it exactly:
  #_R([N_1(X)]) = |N_1(X) ∩ S^{(lev)}_R| + #_R(Col(N_1(X))) ≤ 81|X| + 16Σ_{r≥1}|sh_r(X)| ≤ 81‖X‖_sh,
using |N_1(X)| ≤ 3^d|X| = 81|X| (r = 0) and HW Lemma RING's |sh_r(N_1X)| ≤ 2^d|sh_r(X)| = 16|sh_r(X)| for r ≥ 1. So step
(4)'s e^{c_U‖·‖_sh} becomes e^{82c_U‖·‖_sh} and **c_+ = c_A + 82c_U**, not c_A + 17c_U. **HANDOFF's open cross-lane
disagreement "HW's Lemma RING says ×17, PLD says ×82" is therefore settled, and both lanes are right about different
objects: ×17 is correct for the OPEN column (Lemma BUF at level k), ×82 for the CLOSED column (Lemma BUF at level k − 1),
and the proof of (CEM^{COL})/(E2^𝔉′) needs the level-(k−1) application, hence ×82.** HW §41 item 4's instruction "Please
re-read §18.4's ×82 as ×17" is to be withdrawn for the level-(k−1) use; §18.4's own ×82 stands. Request in §19.11.
*Why this is not avoidable by using the level-k weight only.* If w is taken at m = k (w = h^{R,1}_k(U_k), §18.7.0's other
generator), then step 3's marginal on (U_0, …, U_{k-1}) converts it into a level-(k−1) weight: by HW Lemma TILT (i),
  ∫dU_k K_{k-1}(U_k, U_{k-1})1_{R′,k}(U_k)h^{R,1}_k(U_k) = h^{R″,1}_{k-1}(U_{k-1})
for the pattern R″ carrying R's constraints at levels ≥ k together with R′'s at level k (**Lemma MARG, PROVEN-HERE**:
Fubini and TILT (i) verbatim, the level-k constraint being one of TILT's 1_{R,k+1}-factors one level down). So both
generators of 𝔏^buf_k produce a level-(k−1) future weight, and (vi) is applied at m = k − 1 in both cases. **This also
tidies §18.7.0: its two generators collapse to one form, {h^{R″,1}_{k-1}·(a buffer factor)}.**

## 19.2 Route (ii) of T19 (a): the Markov structure across the R-free ring. Lemma DLR and Theorem W-FREE.
PROVEN-HERE (counted, item [E7] (1))

Throughout §19.2-§19.6: k ≥ 1, 𝒜 a finite set of level-k cubes with **(RING-cc)** and 𝒜 ∩ 𝒰_k = ∅, 𝒜′ ⊂ 𝒜, S := 𝒜 ∖ 𝒜′,
ν ∈ 𝔏^buf_k(R, 𝒜) the marginal law on (U_0, …, U_{k-1}) of §18.7.0, written ν = ν^w_0 with ν_0 := ν^{R′,F_<}_{k-1} the
unweighted past law and w the (now single, by Lemma MARG) buffered level-(k−1) future weight. Write
  **𝔏 := 𝔏_{k-1}(col_{k-1}(S)),  𝔊 := σ(all variables of ν_0 except U_{k-1}|_𝔏).**

**Lemma DLR (the far weight is eliminated exactly, not estimated): PROVEN-HERE.**
- **(i) (the factor audit)** The only factors of ν_0's density that read U_{k-1} on 𝔏 are
  (α) the kernels of K_{k-2}: Π_{c∈𝔏}k^{(k-2)}_c(U_{k-1,c}; M̄_c(U_{k-2})), one per link, and
  (β) the constraint factors Π_{x∈col_{k-1}(S)∩S^{(k-1)}_{R′}}1{ζ_x = 0}, one per level-(k−1) cube, each reading ℓ(x) ⊂ 𝔏.
  Nothing else does: ν_0 = ν^{R′,F_<}_{k-1} has density ∝ e^{-S_0}Π_{i<k-1}K_iΠ_{m≤k-1}1_{R′,m}Π_{k′<k-1}Φ_{k′}F_<, so its
  **top kernel is K_{k-2} and its top capped spectator is Φ_{k-2}, a function of U_{k-2}**; 1_{R′,m} for m ≤ k − 2 reads
  levels ≤ k − 2; Lemma READ (iii) removes the level-(k−1) constraint factors of cubes outside col_{k-1}(S); Lemma READ (v)
  removes F_<. (If one works instead with the level-k law before §18.7.0's marginal, the extra factors are Φ_{k-1},
  removed by Lemma READ (iv) under (C_S′), and K_{k-1}, whose kernels read U_{k-1}|_𝔏 only through M̄_c, c ∈ X_k(S); both
  cases are covered.)
- **(ii) (the weight and the conditioning are 𝔊-measurable)** w reads no link of 𝔏_{k-1}(col_{k-1}(𝒜)) ⊇ 𝔏 by Lemma
  READ (vi) under (RING-cc); F is a function of the level-≤(k−1) fields off the columns of S, hence reads no link of 𝔏.
- **(iii) (the conditional law is local and factorised)** By (i), conditionally on 𝔊 the variables U_{k-1}|_𝔏 have law
    **P_S(dU_{k-1}|_𝔏 ; U_{k-2}) ∝ Π_{c∈𝔏}k^{(k-2)}_c(dU_{k-1,c}; M̄_c(U_{k-2}))·Π_{x}1{ζ_x = 0},**
  which depends on 𝔊 **only through U_{k-2} restricted to region(S)** — because M̄_c(U_{k-2}) reads U_{k-2} only in c's two
  endpoint blocks (HW Lemma FP), which for c ∈ 𝔏 are level-(k−2) cubes under cubes of col_{k-1}(S) — and which
  **factorises over Q ∈ S**, by Lemma READ (ii) (disjoint link blocks) and the per-cube form of (β).
- **(iv) (the identity)** Therefore, with
    **ζ_Q(U_{k-2}|_{region(Q)}) := ∫e^{θY^f_Q}dP_Q / ∫dP_Q ∈ [1, ∞)  and  ζ := Π_{Q∈S}ζ_Q,**
  (P_Q the Q-factor of P_S), one has ζ = E_{ν_0}[Z | 𝔊] and hence, for every ν = ν^w_0 ∈ 𝔏^buf_k(R, 𝒜),
    **E_ν[Z·F] = E_ν[ζ·F]  and  E_{ν_0}[Z·wF] = E_{ν_0}[ζ·wF].**
*Proof.* (i), (ii) are the audits above. (iii) is the definition of a conditional density: divide the joint density by its
integral over U_{k-1}|_𝔏 and cancel every factor not reading 𝔏. (iv) is the tower property, legitimate because wF is
𝔊-measurable by (ii) and Z is a function of U_{k-1}|_𝔏 by Lemma READ (i). ∎

**Theorem W-FREE ((CEM-2) is not an ingredient of (CEM^{COL}); the weight enters only through one local functional):
PROVEN-HERE.** Under (RING-cc) and 𝒜 ∩ 𝒰_k = ∅, for every ν ∈ 𝔏^buf_k(R, 𝒜) and every admissible F,
  **(CEM^{COL})_k holds with constant c_cem ⟺ E_ν[ζ·F] ≤ c_cem^{|S|}E_ν[F],**
with ζ = Π_{Q∈S}ζ_Q the explicit, bounded, **product** functional of U_{k-2}|_{region(S)} of Lemma DLR (iv). In
particular:
- **(a) the far weight h^{R,1} does not appear in ζ at all**, and no decoupling, correlation or mixing estimate between the
  weight and the column energy is required: the separation across the R-free ring is a **Markov** statement, exact, with
  cost 1, and (RING-cc) is exactly the hypothesis that makes it exact;
- **(b) (CEM-2) as stated in §18.7.2 is therefore not the obstruction it was named as.** Proposition SPLIT's factorisation
  (CEM^{COL}) = (CEM-1)·(CEM-2) is valid but **lossy**: it estimates the ratio E_{ν^w}[ZF]/E_{ν^w}[F] by comparing it to
  the unweighted ratio, where Lemma DLR computes it exactly. What survives of (CEM-2) is **only** the ν^w-law of
  U_{k-2}|_{region(S)} — i.e. one level down, one region, and a first-level-of-conditioning question, not a correlation
  inequality;
- **(c) and the gain is one level of regress, not a discharge.** ζ_Q is a moment of exactly the same shape as Y^f_Q's
  moment, one level finer and conditioned. §19.3-§19.5 say what that buys and what it does not.
**Remark (the honest negative, so that (a) is not over-read). ζ_Q is NOT bounded pointwise in U_{k-2}, and that is the
whole residual.** On a configuration whose kernel centres {M̄_c(U_{k-2})}_{c∈𝔏_Q} force column curvature of order ε_1, the
conditional law P_Q is concentrated where F^col_Q ≳ c_prε_1², so ζ_Q ≳ e^{24θc_prε_1²u_k} = e^{24θa_badu_k}, and at the
recorded a·u_k ≈ 10⁸ (§18.5 (e)) this is e^{10⁸⁺}; letting the forced curvature be O(1) gives ζ_Q ≤ e^{24θu_k·n_Q} and no
better. **So §18.7.2 (α)'s negative transfers verbatim to the ess-sup of ζ_Q, and route (ii) does not by itself close
anything: it relocates the whole difficulty into the ν^w-law of one local functional.** That relocation is what §19.3
exploits.

## 19.3 The action trade: Lemma DOM and Theorem AT. PROVEN-HERE (counted, item [E7] (2))

**Notation (the chain's own action, written out).** With no kernel normalisers,
  **𝔄(U_0, …, U_K) := u_0Σ_ps(U_0(p)) + Σ_{m<K}κu_mΦ_m(U_m, U_{m+1}),  Φ_m(U, V) = Σ_cφ_{M̄_c(U)}(V_c)** (HW §0),
so that W = e^{-𝔄}·Π_{m,c}(∫e^{-κu_mφ_{M̄_c}})^{-1}, the normalisers being functions of the finer field only. For a level-k
cube Q define its **column action below level k**
  **𝔄^col_Q := u_0Σ_{p∈col_0(Q)}s(U_0(p)) + Σ_{i=1}^{k-1}κu_{i-1}Σ_{c∈𝔏_i(col_i(Q))}φ_{M̄_c(U_{i-1})}(U_{i,c}),**
i.e. **exactly the terms of 𝔄 that HW §4's definition of F^col_Q counts, each at the coupling the chain itself charges it.**
By HW Lemma DJ the sets of terms of distinct level-k cubes are disjoint, so 𝔄^col_S := Σ_{Q∈S}𝔄^col_Q is a sub-sum of 𝔄.

**Lemma DOM (the moment's exponent is λ_f times the chain's own column action): PROVEN-HERE.** Assume (F_R) with
0 < β_- ≤ β_+ and Rg_K² ≤ ½ (the standing setting). Then for every k ≥ 1, every level-k cube Q and every
(U_0, …, U_{k-1}),
  **θ·Y^f_Q = 24θ·u_k·F^col_Q(U_{k-1}) ≤ λ_f·𝔄^col_Q(U_0, …, U_{k-1}),  λ_f := 24θ(1 + 2Rg_K²).**
*Proof.* F^col_Q(U_{k-1}) is an **infimum** over (U_0, …, U_{k-2}) of the equalised column terms (HW §4), so it is bounded
above by the value of that sum at the **actual** fields:
  F^col_Q(U_{k-1}) ≤ Σ_{p∈col_0(Q)}s(U_0(p)) + Σ_{i=1}^{k-1}κΣ_{c∈𝔏_i(col_i Q)}φ_{M̄_c(U_{i-1})}(U_{i,c}).
Multiply by u_k and compare term by term with 𝔄^col_Q, whose corresponding terms carry u_0 and u_{i-1}: the ratio is
u_k/u_i for some 0 ≤ i ≤ k − 1. By (F_R)'s lower bound with β_- > 0, u_i − u_k ≥ β_-(k − i)log L − R ≥ −R, so
u_i ≥ u_k − R > 0 and
  u_k/u_i ≤ u_k/(u_k − R) = 1/(1 − Rg_k²) ≤ 1 + 2Rg_k² ≤ 1 + 2Rg_K²,
using 1/(1 − x) ≤ 1 + 2x for x ≤ ½, Rg_k² ≤ Rg_K² ≤ ½ (g_k ≤ g_K for k ≤ K, (F_R)) — this is RLARGE l.106 (i)-(ii)'s own
step. Multiplying the term-by-term comparison by 24θ gives the claim. ∎
**Reading, and why this is the right currency.** λ_f = 24θ(1 + 2Rg_K²) is **not** a convenient abbreviation: it is exactly
the one-step coupling slack, and the standing side condition **λ_f < 1 says precisely that the moment's exponent is
strictly below the chain's own action in the column**. The κ of the kernel exponent and the κ of the equalised energy
cancel identically — so the side condition is λ_f < 1 and **not** λ_f < κ, which I checked because κ is only ever bounded
below in this lane (κ ≥ 1/84270, p6 C1); the check is negative and is recorded so that nobody re-imposes a κ.

**Theorem AT (action trade: the moment is a local coupling-lowering ratio): PROVEN-HERE.** For λ ∈ [0, 1) and a nonneg
bounded G, define the lowered partition function
  **𝒵[λ; G] := ∫ e^{-(𝔄 - λ𝔄^col_S)}·𝔑·1_{R′}·F_<·G,  𝔑 := Π(the original kernel normalisers),**
over the variables of ν_0 (levels ≤ k − 1), so that 𝒵[0; G] = E_{ν_0}[G]·Z_{ν_0}. Then:
- **(i)** E_{ν_0}[Z·G] ≤ E_{ν_0}[e^{λ_f𝔄^col_S}·G] = 𝒵[λ_f; G]/𝒵[0; G]·E_{ν_0}[G];
- **(ii)** λ ↦ log 𝒵[λ; G] is convex, real-analytic on [0, 1) when G ≢ 0, with
    **d/dλ log 𝒵[λ; G] = E_{λ,G}[𝔄^col_S],  E_{λ,G} := the expectation under the law ∝ e^{-(𝔄-λ𝔄^col_S)}𝔑1_{R′}F_<G;**
- **(iii) hence, for every nonneg G and in particular for G := wF,**
    **E_{ν^G_0}[Z] ≤ exp(∫_0^{λ_f}E_{λ,G}[𝔄^col_S]dλ).**
*Proof.* (i) is Lemma DOM exponentiated (Z = Π_Qe^{θY^f_Q} ≤ e^{λ_f𝔄^col_S} pointwise) and the definition of 𝒵. (ii)
𝔄^col_S is bounded (a finite sum of bounded terms: s and φ are bounded on compact groups), so 𝒵[λ; G] is finite and its
λ-derivative may be taken inside; the derivative of the log is the expectation of 𝔄^col_S under the λ-tilted law, and
convexity is the variance. (iii) is (i) and (ii) integrated, since log(𝒵[λ_f]/𝒵[0]) = ∫_0^{λ_f}(d/dλ)log𝒵. ∎
**Remark (the normalisers are harmless, and that is why this is exact).** Lowering the coupling in the exponent does not
change 𝔑, which is a function of the finer fields only; so 𝒵[λ; ·] is a genuine one-parameter exponential family in λ with
sufficient statistic 𝔄^col_S, and (ii) is the standard identity for such a family. No representation, no main-term
expansion and no small-field restriction is used anywhere in §19.3.

## 19.4 T19 (b)-(c): (ACT), the collapse of (CEM-1)'s three ingredients, and the restated (LCR).
Implications PROVEN-HERE (counted with §19.3, item [E7] (2)); the statement itself OPEN

**(ACT)_k [node A; NEW; OPEN; "column-action moment"].** There is c_act < ∞, independent of g ≤ g_0, k ≥ 1, K, T, 𝔥,
R ∈ 𝔉_𝔥, 𝒜, 𝒜′, F and F_<, such that for every datum as in §19.2 and every ν = ν^w_0 ∈ 𝔏^buf_k(R, 𝒜),
  **E_{ν_0}[e^{λ_f𝔄^col_S}·wF] ≤ c_act^{|S|}·E_{ν_0}[wF],   λ_f = 24θ(1 + 2Rg_K²) < 1.**

**Proposition ACT-EQ: PROVEN-HERE.**
- **(i) (ACT)_k ⇒ (CEM^{COL})_k with c_cem = c_act**, by Theorem AT (i) and Lemma DLR (which is not even needed for this
  direction).
- **(ii) (ACT)_k is EXACTLY equivalent to a mean-action bound**: by Theorem AT (ii), with G := wF,
    **log(E_{ν_0}[e^{λ_f𝔄^col_S}G]/E_{ν_0}[G]) = ∫_0^{λ_f}E_{λ,G}[𝔄^col_S]dλ,**
  so (ACT)_k holds with log c_act = λ_f·B iff **E_{λ,G}[𝔄^col_S] ≤ B|S|** on average over λ ∈ [0, λ_f]; a per-λ bound is
  sufficient and the averaged one is necessary. **This is an identity, not an estimate.**
- **(iii) (ACT)_k is STRICTLY STRONGER than (CEM^{COL})_k.** The converse of (i) fails, and for a structural reason worth
  recording: F^col_Q is an **infimum** over the finer fields, so a bound on the moment of u_kF^col_Q does not bound the
  mean of 𝔄^col_Q — the infimum discards exactly the finer-field excess that 𝔄^col_Q charges. So §19.4 offers a second
  route to (CEM^{COL}), not a reformulation of it, and the lane carries both. (Same discipline as §18.7's "consolidation,
  not a discharge".)

**Proposition CEM1-COLLAPSE (the three named ingredients of (CEM-1) collapse to one, and two of them are not needed on
this route): PROVEN-HERE (logic about the two routes; not counted).** (CEM-1)_k of §18.7.2 is (ACT)_k with w ≡ 1 up to
(iii)'s strengthening, and §18.7.2's three ingredients fare as follows.
- **(a) "the main-term reduction OFF G_Q" is NOT NEEDED.** §18.7.2 (a) asks for F^col_Q ≤ Σ_{x∈col Q∖B}𝓔^{an}_{k-1,x} +
  Σ_{x∈B}(R-operated large-field energy) and records that "nothing in PLD §16-§17 or HW §6 writes this, and it is the
  first thing a proof of (CEM-1) must write". **Lemma DOM writes a different and sufficient inequality that needs no
  representation at all**: F^col_Q is already defined (HW §4) as an infimum of the chain's own terms, so bounding it by
  those terms at the actual fields is immediate, holds on and off G_Q alike, and involves neither 𝓔^{an} nor the
  small-field/large-field split. **So ingredient (a) is a requirement of the representation route only.**
- **(b) "the coupling response for the full representation"** becomes, on this route, the mean-action bound of (ii) — no
  representation, no activities.
- **(c) "u-uniformity of the activity bounds on [(1 − λ_f)u, u]"** is **not a separate hypothesis on this route**: the
  interval is the integration variable of the identity (ii), and what must be uniform is the mean column action, not any
  activity bound. §17.5's recorded worry that CE-exp^k's hypotheses (N5-unif, L-loc) "do not state" that uniformity is
  therefore a defect of the representation route, not of (CEM-1).
- **Net: on the (ACT) route (CEM-1)'s three ingredients collapse to ONE statement — a mean column-action bound, uniform in
  λ ∈ [0, λ_f] and in everything else — at the price of (iii)'s strengthening.** This is the answer to T19 (b).

**The restated (LCR). (LCR^act)_m [NEW; replaces §16.7's (LCR) and §18.8 (ii)'s certificate target]: OPEN.**
There is B < ∞ such that for every m ≥ 1, every R ∈ 𝔉_𝔥 with 𝒜 satisfying (RING-cc) and 𝒜 ∩ 𝒰_m = ∅, every 𝒜′ ⊂ 𝒜,
every bounded measurable F ≥ 0 of the level-≤(m−1) fields off the columns of S := 𝒜 ∖ 𝒜′, every bounded measurable
F_< ≥ 0 of U_{<k_0}, every w of §18.7.0's (single, by Lemma MARG) buffered form, and every λ ∈ [0, λ_f]:
  **E_{λ,wF}[𝔄^col_S] ≤ B·|S|,   uniformly in g ≤ g_0, m, K, T, 𝔥, R, 𝒜, 𝒜′, F, F_<, λ.**
**Against §18.8 (ii)'s five certificate clauses, one by one.**
1. **λ_f < 1: KEPT**, and now visibly structural (Lemma DOM: it is the statement that the moment's exponent is below the
   chain's own action). It appears as the length of the λ-interval, not as a coupling shift inside a representation.
2. **"the law class 𝔏^buf_k, not a sup over G": KEPT but DEMOTED.** By Lemma DLR the weight does not enter the conditional
   law of the column variables at all, so the class matters only through the **law of U_{m-1}|_{region(S)}** it induces.
   §18.8 (i)'s fatal objection — that no finite g-uniform constant exists over all G not reading the column links — does
   not apply to a **first moment** of 𝔄^col: §18.7.2 (α)'s arithmetic bounds a conditional **exponential** moment from
   below, and the restatement asks no exponential moment of the far field. (What it does ask is §19.5's (BCH-1).)
3. **uniformity in g, m, K, T, 𝔥, R, 𝒜, 𝒜′, F, F_<: KEPT in full, and extended to λ.** This is the whole analytic content.
4. **"the allowance in form (P0) or (P1)": DROPPED as a clause, and satisfied.** A first-moment bound carries no
   allowance; exponentiating by (ii) gives log c_act = λ_f B, a per-cube constant, i.e. **form (P0) with c_A = 0** in
   Proposition PATCH (v)'s classification. Nothing in §19.3-§19.4 introduces a shadow sum or a slice.
5. **"log c_lcr ≤ 10⁹": KEPT, restated as B ≤ 10⁹/λ_f**, i.e. **B ≤ 2·10⁹ at λ_f = ½**. The equipartition value of B is
   dof/(2(1 − λ)) ≤ dof = 52488 at λ ≤ ½ (§19.5), thirteen orders below the ceiling (check p7 B).
**So the restatement keeps clauses 1, 3 and 5, demotes clause 2 and discharges clause 4** — and, unlike §16.7's form, it is
not refuted by §18.8 (i), because it is a first moment and not an exponential one. **It is the form (CEM-1) consumes**:
(ACT)|_{w≡1} ⇒ (CEM-1) by Proposition ACT-EQ (i) with w ≡ 1.

## 19.5 CORRECTION (appended, not edited): (ACT) as stated in §19.4 is WITHDRAWN, and the repair. PROVEN-HERE for the
repair; the withdrawal is ARGUED and binding on §19.4

**This section corrects §19.4, written 14:12 UTC, before any check. §19.4 is left exactly as written (the file is
append-only); this is the correction of record, and it is binding: no later section uses (ACT) or Proposition
CEM1-COLLAPSE (a) in the form §19.4 states them.** The defect was caught by applying §19.0's own "Not success" clause
("a constant or exponent depending on k … presented as uniform") to my own statement.

**The defect, exactly.** (ACT) is stated with **𝔄^col_S, the chain's ACTUAL action in the column**. That functional
contains the term u_0Σ_{p∈col_0(Q)}s(U_0(p)) — the bare action of **every fine plaquette in the column of Q** — and
region(Q) contains 81^{k+1} unit cells at d = 4, L = 3. So 𝔄^col_Q is **extensive in the column's fine volume**, and the
lane's own equipartition bookkeeping (the bookkeeping that produces p6 D1's dof) gives
E_{ν_0}[𝔄^col_Q] ≍ (3/2)·(number of column degrees of freedom) ≍ 81^{k+1}; Jensen then gives
  **E_{ν_0}[e^{λ_f𝔄^col_Q}] ≥ e^{λ_fE_{ν_0}[𝔄^col_Q]} ≍ e^{c·λ_f·81^{k+1}},**
which is not bounded by any k-uniform c_act. **Status of the refutation: ARGUED** — it rests on the equipartition lower
bound for E[𝔄^col_Q], which is not proven here — but it is decisive enough to withdraw the hypothesis, because a route
whose own heuristic value is e^{81^k} must not be carried. **(ACT) is WITHDRAWN.** Lemma DOM itself is unaffected (it is a
correct pointwise inequality); what was wrong was to exponentiate it against a measure, because **Lemma DOM throws away
exactly the infimum that makes F^col small.**

**Lemma DOM′ (the repair; the minimised column action): PROVEN-HERE.** Define, for a level-k cube Q and a level-(k−1)
field,
  **𝔞^col_Q(U_{k-1}) := inf_{(U_0,…,U_{k-2})}[u_0Σ_{p∈col_0(Q)}s(U_0(p)) + Σ_{i=1}^{k-1}κu_{i-1}Σ_{c∈𝔏_i(col_i Q)}φ_{M̄_c(U_{i-1})}(U_{i,c})],**
the same sum as 𝔄^col_Q but **minimised over the finer fields** — i.e. HW §4's F^col_Q with each term carried at the
coupling the chain charges it. Then, under the standing setting,
  **θ·Y^f_Q = 24θu_kF^col_Q(U_{k-1}) ≤ λ_f·𝔞^col_Q(U_{k-1}),  λ_f = 24θ(1 + 2Rg_K²),**
and 𝔞^col_Q is **not extensive in the column's fine volume**: it vanishes on every U_{k-1} that admits a zero-energy finer
completion, and in general it is the minimal action cost of the coarse configuration.
*Proof.* Lemma DOM's term-by-term comparison u_k·(term) ≤ (1 + 2Rg_K²)·(u_i-weighted term) is pointwise in the finer
fields; take the infimum over the same variables on both sides. The vanishing statement is immediate from the definition
(a completion with all terms zero gives infimum 0). ∎

**What survives, and what does not.**
- **Theorem AT survives verbatim with 𝔄^col_S replaced by 𝔞^col_S**, because 𝔞^col_S is bounded and the only property used
  is that λ ↦ ∫e^{-(𝔢 - λ𝔞^col_S)} is an exponential family with sufficient statistic 𝔞^col_S, where **𝔢** is whatever
  exponent the relevant law has. So the identity
    **log(E_{ν^G}[e^{λ_f𝔞^col_S}]) = ∫_0^{λ_f}E_{λ,G}[𝔞^col_S]dλ**
  holds, and with it the reduction "the moment is the integral of a MEAN". **This is the part of §19.4 that stands.**
- **(ACT′)_k [the repaired statement; node A; OPEN]:** E_{ν_0}[e^{λ_f𝔞^col_S}·wF] ≤ c_act^{|S|}E_{ν_0}[wF], equivalently
  (identically) **E_{λ,wF}[𝔞^col_S] ≤ B|S| for λ ∈ [0, λ_f] on average**, with log c_act = λ_f B. (ACT′) ⇒ (CEM^{COL})_k
  with c_cem = c_act by Lemma DOM′, and (ACT′) is still strictly stronger than (CEM^{COL}) for §19.4 (iii)'s reason.
- **Proposition CEM1-COLLAPSE (a) is WITHDRAWN: §18.7.2's ingredient (a) IS needed, and §18.7.2 was right.** The reason is
  now sharp and is the useful part of the correction. The trade e^{λ_f𝔞^col} against the measure requires comparing
  𝔞^col_Q — the **minimised** column action — with the exponent of the law of U_{k-1} **after the finer levels have been
  integrated out**. Those differ by the fluctuation (determinant/entropy) terms:
    −log(level-(k−1) marginal density) = 𝔞^{total}(U_{k-1}) − log(the finer fluctuation integral at U_{k-1}),
  and the statement that the marginal's exponent **dominates** 𝔞^col locally and uniformly, with the fluctuation terms
  bounded per degree of freedom, is **exactly the small-field representation (I^E)″ and §18.7.2 (a)'s main-term
  reduction.** So the representation cannot be bypassed; what Lemma DOM′ does buy is that the inequality to be proven is
  between two **actions** (the minimised column action and the marginal's exponent) rather than between F^col and a sum of
  activity energies 𝓔^{an}, and that it is needed **on and off G_Q alike with the same statement** — which is what
  §18.7.2 (a) asked for and nobody had written.
- **Proposition CEM1-COLLAPSE (b)-(c) stand**: on the identity route, (b) is the mean bound and (c) is the integration
  variable, so **(CEM-1)'s ingredients (b) and (c) are ONE statement and not two**. The honest tally for T19 (b) is
  therefore **three ingredients → two**: (a) the main-term/representation domination (unchanged, still OPEN, still the
  first thing to write) and (b+c) one mean-action bound uniform on [0, λ_f].
- **The restated (LCR) of §19.4 stands with 𝔄^col replaced by 𝔞^col**: call it **(LCR^act′)_m**, with clauses 1, 3, 5 kept,
  clause 2 demoted and clause 4 discharged exactly as §19.4 states. In clause 5 the bound is B ≤ 10⁹/λ_f = 2·10⁹ at
  λ_f = ½, and the equipartition value of B for 𝔞^col is dof/(2(1 − λ)) with dof the number of level-(k−1) group degrees
  of freedom the column's top terms involve; at the lane's recorded **dof = 3n_int·81 = 52488** (p6 D1) the identity gives
  log c_act = (dof/2)log(1/(1 − λ_f)) = **18190.95 at λ_f = ½ — p6 D1's recorded value, exactly** (check p7 B1). **So
  §18.7.2's "Gaussian heuristic" is not a Gaussian approximation at all: it is the equipartition value of an exact
  identity, and this session identifies it as such.** (Which geometric count dof = 3n_int·81 is — the level-(k−1) links of
  𝔏_{k-1}(col_{k-1}Q) or a two-level count — is a question for the owner of §18.7.2, request in §19.11; the identity does
  not depend on the answer, only the number does.)

## 19.6 T19 (a): the typicality mechanism, priced; and the status of (CEM-2). Proposition TRADE and Theorem OUT:
PROVEN-HERE (counted, item [E7] (3)); the residual (BCH-1) OPEN

**Proposition TRADE (what the measure buys that the event cannot, priced in both currencies): PROVEN-HERE (elementary
probability; the numbers are arithmetic about recorded constants, check p7 A).** Let 𝔟 ≥ 0 be any functional measured in
**action units** (so that the measure's own suppression of {𝔟 > t} is at rate e^{-t}).
- **(i) The event route.** "No defect in the buffer" bounds the field: every interior plaquette of every buffer cube has
  ‖1 − V_P‖ < ε_1, so the forced column action it permits is 𝔟 ≤ C·n·u·ε_1² = C·n·(ε_1/g_K)², the identity p6 A2 records
  at **4.489·10¹⁵**. Through the identity of §19.5 this gives log c_act ≥ λ_f·4.489·10¹⁵ = **2.245·10¹⁵ at λ_f = ½**,
  against §18.8 (ii) clause 5's admissible ceiling log c ≤ 10⁹: **the event route misses the ceiling by a factor
  2.245·10⁶ in the LOG** (check p7 A2). That is a sharper statement of §18.7.2 (α)/(β) than "it differs by 4.489·10¹⁵":
  in the first-moment currency the miss is 2.2·10⁶ in the exponent, not e^{10¹⁵}.
- **(ii) The measure route.** If ν(𝔟 > t) ≤ Ce^{-t} for all t ≥ 0, then
    **E_ν[𝔟] ≤ 1 + log⁺C  and  E_ν[e^{λ𝔟}] ≤ 1 + Cλ/(1 − λ) for λ < 1,**
  the second by the layer-cake ∫_0^∞λe^{λt}ν(𝔟 > t)dt. **So the price of typicality is 1/(1 − λ_f) per cube in the
  exponential currency and 1 + log⁺C in the first-moment currency** — at λ_f = ½ a factor 2, and in the log a quantity of
  size log C, i.e. equipartition-sized (≈ dof/2 ≈ 5·10⁴), **eleven orders below the event route's 2.245·10¹⁵ and five
  orders below the ceiling.**
- **(iii) Why the thresholds cancel, structurally.** The event bounds the FIELD at the g-independent threshold ε_1, and
  converting a field bound into an action bound costs the factor u = 1/g_K² — which is where 4.489·10¹⁵ = (ε_1/g_K)² comes
  from. The measure prices the same configuration in ACTION units, where the suppression rate is **the same u** that
  multiplies it; so u cancels and only (1 − λ_f) and a degree-of-freedom count survive. **This is the whole content of
  "the mechanism must be the weight's typicality, not the event", and it is why §18.7.2 (δ)'s "no inequality between ε_1
  and g_K can hold uniformly in g" is true and yet not fatal.**

**Theorem OUT (the outside decomposition: the weight survives only in a first moment): PROVEN-HERE.** Let
𝔉_out := σ(all fields of ν_0 restricted to the links not touching region(S)). Under (RING-cc) and the reading of
(CEM^{COL})'s hypothesis that **F is a function of the level-≤(k−1) fields off the columns of S at every level** (which is
what the two consumers supply: Cor. E2-RED's F = 1{Y ⊔ x(Γ_1) ⊂ D_j} reads interiors of cubes disjoint from col(Γ_0), and
Theorem NA-PRICE^{E+} step (4)'s F′ = Π_{Q∈T}1{Q ∉ 𝒞_k}·F reads blocks under T, disjoint from S ∖ T — §18.7's own
measurability check):
- **(i)** w and F are 𝔉_out-measurable (Lemma READ (vi) for w under (RING-cc); hypothesis for F);
- **(ii)** hence, for every λ ∈ [0, λ_f], E_{λ,wF}[·|𝔉_out] = E_λ[·|𝔉_out] and
    **E_{λ,wF}[𝔞^col_S] = E_{λ,wF}[ E_λ[𝔞^col_S | 𝔉_out] ];**
- **(iii)** therefore (ACT′)_k, hence (CEM^{COL})_k, follows from the conjunction
  - **(EQ-bc)_k [conditional equipartition with the boundary charge; WEIGHT-FREE and LAW-CLASS-FREE; OPEN]:** there are
    B_0 < ∞ and an 𝔉_out-measurable charge 𝔟_Q ≥ 0 such that E_λ[𝔞^col_Q | 𝔉_out] ≤ B_0 + 𝔟_Q, ν_0-a.s., for every
    λ ∈ [0, λ_f] and every Q ∈ S;
  - **(BCH-1)_k [the boundary charge's first moment under the weighted law; OPEN]:**
    E_{λ,wF}[Σ_{Q∈S}𝔟_Q] ≤ B_1·|S| for every λ ∈ [0, λ_f],
  with B = B_0 + B_1 and log c_act = λ_f(B_0 + B_1).
*Proof.* (i) is the audit. (ii) wF is 𝔉_out-measurable, so it cancels between numerator and denominator of the conditional
expectation; then the tower property. (iii) is (ii) plus (EQ-bc) plus (BCH-1), and then §19.5's identity. ∎
**What the charge must be, stated honestly.** 𝔟_Q cannot be the ess-inf of 𝔞^col_Q given 𝔉_out: 𝔞^col_Q is a functional of
the INSIDE variables and the conditional law has full support, so that ess-inf is 0 and (EQ-bc) would collapse to the
uniform-in-boundary-condition bound that §18.7.2 (α) refutes. The charge has to be the **boundary-forced conditional
free-energy excess**, 𝔟_Q := 𝔉_Q(bc) − inf_{bc′}𝔉_Q(bc′) with 𝔉_Q(bc) := −log∫e^{−𝔄^{in}(·, bc)}d(inside fields).
**Supplying that definition and proving (EQ-bc) with it is part of (EQ-bc) and is not done here.** This is the one place
where §19.6 states less than it would like, and it is stated as such.

**Status of (CEM-2) after §19.2-§19.6.**
- **(CEM-2) as stated in §18.7.2 is NOT an ingredient of (CEM^{COL}) and should not be attacked as one.** Theorem W-FREE
  computes the weighted ratio exactly where Proposition SPLIT estimates it; §18.11's "single biggest remaining
  obstruction" is therefore mis-named, and the correct residual is (BCH-1). **This is a downgrade of §18.7.2's SPLIT from
  "the reduction" to "a lossy reduction", recorded in §19.10.**
- **(BCH-1) is strictly smaller than (CEM-2), in four named ways:** a **first** moment, not an exponential one; **one
  scalar per cube** (the boundary charge), not a product of column-energy moments; a functional of the **outside** field
  only, not a joint functional of inside and outside; and **no comparison of two laws** — (CEM-2) is a correlation
  inequality between two expectations, (BCH-1) is a single expectation. **A reduction of an OPEN item to a sharper OPEN
  item, which is the honest unit of progress here.**
- **Two routes to (BCH-1), both priced, neither taken.**
  - **(ρ1) the outward regress.** Bound 𝔟_Q by the action in the adjacent collar, then apply (EQ-bc) in the collar, and so
    on outward. Each ring r contributes its own equipartition term times the forcing factor of that ring. **Indicative
    power count** (labelled indicative, not a proof): a boundary perturbation at level-(k−1) distance r forces interior
    amplitude ∼ r^{-(d-2)}, hence interior action ∼ r^{-2(d-2)}, and the ring carries ∼ r^{d-1} sources, so the regress
    sums Σ_{r≥1}r^{d-1-2(d-2)} = Σ_{r≥1}r^{3-4} = Σ r^{-1} at **d = 4: logarithmically divergent**, against
    Σ r^{-2} < ∞ at d = 5 (check p7 D, with the d = 5 control). **So the naive outward regress is MARGINAL in exactly the
    d = 4 sense that NORMS §N5 and the brief's D3 diagnosis identify** (the d = 4 cubic vertex is marginal; the
    Bianchi/derivative cancellation is what takes K_p from 2.27 to ≈ 0.12). The regress therefore has to be resummed by
    the same cancellation, and that is not a local repair.
  - **(ρ2) relax the ring in the weight, and pay with (CRC).** Pointwise, **w ≤ w^{-𝒞}** for every upward-closed 𝒞
    (HW (m1): 1_R ≤ 1_{R^{-𝒞}} increases the future probability, and Buf^{R^{-𝒞}}_ρ ⊆ Buf^R_ρ weakens the buffer clause),
    and with 𝒞 := [N_1(col_{k-1}(𝒜))] the relaxed weight w^{-𝒞} is blind to the ring by Theorem LI^U-0′. One then
    conditions on the fields outside region(N_1(S)) and pays the ratio E_λ[w^{-𝒞}F]/E_λ[wF] ≤ e^{c_U#_R(𝒞)} ≤
    e^{82c_U‖S‖_sh} by (CRC) — which **Theorem CRC-2T′ step (4) already buys from its own induction on N(R)**, because
    N(R^{-𝒞}) < N(R). **Three costs, all g-independent and all declared:** (1) the closed-column price of Finding
    (BUF-CC), ×82 not ×17; (2) **c_A = 0 is given up**: the allowance becomes e^{82c_U‖P‖_sh}, i.e. exactly the union-form
    patch allowance HW §30.3/§37 asks for — so this route stays inside HW's budget but loses §18.7's (5) strictly-stronger
    claim; (3) the consumers' F reads the ring (both of them do), so the conditioning needs F off the columns of N_1(S),
    which costs a **colouring/Hölder step**: split S into χ ≤ 5^d = 625 classes at mutual ℓ^∞ distance ≥ 3 and apply
    Hölder with exponent χ, which requires **χλ_f < 1, i.e. θ < 1/(24·625) ≈ 6.7·10⁻⁵** — a tightening of §18.7's
    θ ↑ 1/24, though still far above the previously-feared fallback θ ≈ 8·10⁻⁷. **Status: ARGUED as a route (the steps are
    named and priced; the (CRC) non-circularity condition is "the relaxation must be of a pattern with strictly fewer
    constrained pairs, so CRC-2T′'s own induction supplies it", which is exactly how §18.4/§35.6 already buy the ring).
    NOT a proof, and the circularity risk is declared: if an integrator ever lets (CRC) be bought from (E2^𝔉′) at the SAME
    N(R), this route is circular.**

## 19.7 T19 (d): the level-0 clause. (0a) is the weaker, and Theorem L0 reduces it to one finite-dimensional statement.
PROVEN-HERE (the implication and the dimension count; counted, item [E7] (4)); (W0-EQ) OPEN

**Which of (0a), (0b) is weaker: (0a), and strictly. PROVEN-HERE.** HW §37's readings are **(0a)** Γ a set of level-0
cubes with the Wilson window Π_{Q∈Γ}e^{θX_Q} and **Y = ∅**, and **(0b)** Γ at level 1 with Y at level 0.
- (0a) contains **no Y-factor**, hence no defect probability at all: it is a pure moment.
- (0b) contains the factor (C_Ae^{-a_Au_0})^{|Y|} for Y at level 0, i.e. it requires **(SDP) at level 0**. Every route to
  (SDP) in this lane (Lemma FT^far, Lemma MD, Theorem NA-PRICE^{E±} step (1)) converts a defect event into a kernel event
  by integrating the level-m links at fixed U_{m-1}; at m = 0 **there is no U_{-1} and no kernel to integrate**, which is
  exactly what §16.5 "Level 0" and §17.6 record as OPEN. So (0b) ⇒ (0a)'s difficulty plus a strictly additional OPEN item.
**Hence (0a) is the one to attack, and T19 (d)'s "pick whichever is weaker" is answered: (0a).**

**Theorem L0 ((0a) is an exact mean-energy statement about the bare Wilson measure on one block): PROVEN-HERE.** At level
0, HW §4 defines F^col_A(U_0) := Σ of the level-0 plaquettes in A **with no infimum**, and HW Lemma W-bad's level-0 window
is X_Q := u_0Σ_{p⊂int Q}s(U_0(p)). Since S_0 = u_0Σ_ps(U_0(p)) (HW §0), we have **θX_Q = θ·𝔄^{int Q} exactly** — Lemma DOM′
holds at level 0 as an **identity**, with θ in place of λ_f and with **no (F_R) factor at all** (there is no coarser
coupling to compare). Consequently, with ν_0 the bare law (density ∝ e^{-S_0}1_{R,0}F_<, and F_< ≡ 1 since k_0 ≤ 0) and
w = h^{R,1}_0 the level-0 future weight:
- **(i) (exact identity)** E_{ν^{wF}_0}[Π_{Q∈Γ}e^{θX_Q}] = exp(∫_0^θ E_{λ,wF}[Σ_{Q∈Γ}𝔄^{int Q}]dλ) — Theorem AT with
  equality, since the domination is an identity;
- **(ii) (DLR, no finer level needed)** e^{-S_0} is a nearest-neighbour Gibbs density, so with
  𝔉_out := σ(U_0 off ∪_{Q∈Γ}int Q) the conditional law of U_0|_{int Q} given 𝔉_out is the Wilson measure on int Q with the
  observed boundary data, times the factor 1{ζ_Q = 0} if Q ∈ S^{(0)}_R — **the kernel's Markov property of §19.2 is
  replaced by the bare measure's own DLR property**, and w, F are 𝔉_out-measurable exactly as in Theorem OUT ((RING-cc) at
  level 0 reads: every cube of N_1(Γ) has unconstrained closed column);
- **(iii) (the reduction)** therefore **(0a) ⟸ (W0-EQ) + (BCH-0)**, where
  - **(W0-EQ) [OPEN; finite-dimensional]:** there are B_0 < ∞ and a boundary charge 𝔟^{(0)}_Q (the conditional free-energy
    excess of §19.6) such that, for every boundary datum, every λ ∈ [0, θ] and every level-0 cube Q,
    E_λ[u_0Σ_{p⊂int Q}s(U_0(p)) | 𝔉_out] ≤ B_0 + 𝔟^{(0)}_Q;
  - **(BCH-0)** = (BCH-1) at level 0, the same residual as at every other level;
  with log C_fc^{(0)} = θ(B_0 + B_1).
- **(iv) (the size and kind of (W0-EQ), computed)** (W0-EQ) is a statement about **one L^d = 3⁴ block**: int Q has
  **n_int = 216** links, so **648 real dimensions**; the gauge transformations that fix the boundary datum are those at
  sites all of whose 8 incident links are interior, i.e. at the **single centre site** of a 3⁴ block, giving **3 gauge
  directions and 645 transverse ones**. So (W0-EQ) is a **Laplace-asymptotics statement on a fixed 645-dimensional
  transverse section of a compact manifold, uniform over the compact space of boundary data, at couplings ≥ (1 − θ)u_0**.
  Its equipartition value is B_0 = 645/(2(1 − λ)) ≤ 645 for λ ≤ ½, giving
    **log C_fc^{(0)} = (645/2)·log(1/(1 − θ)) = 13.73 at θ = 1/24** (check p7 C2), i.e. C_fc^{(0)} ≈ 9.0·10⁵ — twelve
  orders inside §18.8 (ii) clause 5's ceiling.
*Proof.* (i) and (ii) are Theorems AT and OUT specialised, with the two substitutions named; (iii) is Theorem OUT (iii);
(iv) is the dimension count (216 interior links of a 3⁴ block: 2·3³ = 54 per direction, ×4; one interior site) and the
identity of (i) at the equipartition value. ∎
**Consequence for the pre-stated failure mode. (NP-F13) is REFUTED, by my own pre-statement's standard.** §19.0 listed as
a valid failure outcome "(0a) and (0b) are both strictly harder than the k ≥ 1 case for a named structural reason (no
finer level to condition on)". **That reason does not hold**: at level 0 the bare Wilson measure supplies the DLR property
directly, and in one respect level 0 is **easier** than k ≥ 1 — Lemma DOM′ is an identity there, with no (F_R) slack and
no infimum, so the extensivity defect of §19.5 cannot occur. **The honest ranking is: (0a) is the single most tractable
instance of the whole family, and it has been left OPEN because it was mis-levelled (HW §37) and nobody separated it from
(0b).** The residual (BCH-0) is the same residual as everywhere else, so (0a) adds nothing new beyond (W0-EQ).
**Status.** (0a) ⟸ (W0-EQ) + (BCH-0): **PROVEN-HERE as an implication.** (W0-EQ): **OPEN, single-level,
finite-dimensional (645 transverse dimensions), no RG, no representation, no history — session-scale, not paper-scale.**
(0b): **OPEN and strictly harder**, needing a level-0 (SDP) that this lane has no route to.

## 19.8 T19 (e): the hypothesis chain for (SDP)^A after session 7, and the single remaining obstruction

**The chain, written out with every input named and its owner.**
  (SDP)^{A,far}_θ at level k ≥ 1, F-conditioned, union currency, buffered weights
    ⇐ Theorem NA-PRICE^{E+} (i) (§18.7, implication PROVEN there)
    ⇐ (CLS-min) [OPEN; owner SQ/HIST via (REG-min) or (AE)] + (CEM^{COL})_k + **(RING-cc)** [new, §19.1; bought inside
      Theorem CRC-2T′ step (4) at **×82** on c_U]
  (CEM^{COL})_k ⇐ **Lemma DOM′** [PROVEN-HERE, §19.5] + **(ACT′)_k**
  (ACT′)_k ⟺ a mean-𝔞^col bound on λ ∈ [0, λ_f] [**identity**, Theorem AT, PROVEN-HERE]
    ⇐ **(EQ-bc)_k** [OPEN; **weight-free and law-class-free**; = the small-field moment node A has owed since §16.7, in
      the action currency; its own residual input is §18.7.2 (a)'s representation domination, unchanged] +
      **(BCH-1)_k** [OPEN; the only statement in the whole chain that still mentions the far weight].
**Everything else in the chain is proven or is arithmetic.** (CEM-2) does not appear: Theorem W-FREE removes it.

**The single remaining obstruction, named: (BCH-1)** — the **first moment, under the buffered-weighted past law, of the
boundary-forced conditional free-energy excess of a level-k cube's column**, uniformly in g, k, K, T, 𝔥, R ∈ 𝔉_𝔥, 𝒜, 𝒜′,
F, F_< and λ ∈ [0, λ_f]. KIND: a single scalar per cube, a first moment, a functional of the outside field alone, no
comparison of two laws. OWNER: node A (this lane). It is **strictly smaller than (CEM-2)** in the four ways listed in
§19.6, and it is the whole of what the far weight still costs.

**And it is removable, at a declared price.** Route (ρ2) of §19.6 removes (BCH-1) entirely — pointwise (m1) monotonicity
w ≤ w^{-𝒞}, the ring relaxation bought from Theorem CRC-2T′'s own induction on N(R), and a colouring/Hölder step —
leaving
  **(SDP)^A ⇐ (CLS-min) + (RING-cc) + ONE weight-free, law-class-free, single-level statement (EQ-bc),**
with **no decoupling estimate, no correlation inequality and no statement about h^{R,1} anywhere in the chain.** The
three prices, all g-independent and all computed: ×82 instead of ×17 on c_U (Finding (BUF-CC), p7 F1); **c_A = 0 given up
in favour of the union-form patch allowance e^{82c_U‖P‖_sh}**, which is exactly what HW §30.3/§37 asks for (so the route
stays inside HW's budget, but §18.7 (5)'s "strictly stronger than HW asks" claim is lost on it); and θ ≤ 1/(24·5^d)
= 6.67·10⁻⁵ (p7 E1), which tightens §18.7's θ ↑ 1/24 but stays **80 times above** the previously-feared fallback
θ ≈ 8·10⁻⁷. **Status of route (ρ2): ARGUED (steps named and priced, not proven), with the circularity condition
declared.**

## 19.9 T21: check p7 (criteria checks/p7_criteria.md 14:20:23 UTC, md5 ceaf6aa8f145413a3dd4f35ea673c955, 5869 bytes,
written BEFORE the script; script checks/p7_pld.py 14:20:56 UTC, md5 d182f1d6f8d662bec4066e38d4b6cf30; output
checks/p7_out.txt; stderr checks/p7_err.txt; record checks/p7_time.txt)

- **Order, disclosed.** §19.0 (14:03:44 UTC) was the first edit. §19.1-§19.8 were written next, 14:06-14:22 UTC, and
  **before** checks/p7_criteria.md existed. The criteria file was then written (14:20:23), then the script (14:20:56),
  then the single run (14:21). **No constant derived in session 7 appears in a PASS/FAIL condition**; every number in the
  criteria file is sourced inline to RLARGE / HW / PLD sessions ≤ 6 or is pure lattice geometry. Two criteria (A2, C2)
  are reproductions of hand arithmetic written earlier in §19.6/§19.7 and are **labelled CONFIRMATORY, not
  pre-registered**, per [RHW5-fix W5-1]; the other eleven are PRE-REGISTERED.
- One run, 14:21 UTC, 17.51 s, 19.6 MB, exit 0, nice 10, one thread (OMP/OPENBLAS/MKL/VECLIB = 1),
  PYTHONDONTWRITEBYTECODE=1, `python3 -I`, load 2.99/2.58/2.31 at launch. **The numeric lock was NOT taken**, and
  deliberately: the brief exempts exact rational/symbolic arithmetic in plain python, and p7_pld.py imports only
  `fractions`, `decimal`, `sys` (no numpy, no BLAS, no linear algebra, no sampling). Justification in
  checks/p7_time.txt. No re-run, no trap, no pkill, no process left.
- **SUMMARY AS RUN: 13 criteria, 0 FAIL. All four negative controls (A3, B2, C1n, D2) behaved as designed.**
- **The load-bearing result is B1.** (dof/2)·ln(1/(1 − λ_f)) at dof = 52488, λ_f = ½ computes to **18190.954606**
  against p6 D1's independently recorded **18190.95** (diff 0.0046). §18.7.2 calls that number "the Gaussian
  heuristic's own value"; §19.5's identity says it must be the **equipartition** value of an exact partition-function
  identity, and it is. **This is the one number in p7 that tests a session-7 claim rather than reproducing arithmetic,
  and it passes against an externally recorded value.**
- Also PASS, and used in §19: **A1** (u·ε_1² ≡ (ε_1/g_K)² exactly, value 4.489·10¹⁵ = p6 A2's recorded value, re-formed
  from ε_1 = 67/10⁴¹ and g_K² = 10⁻⁹⁴); **A2** (margin 2.2445·10¹⁵; the event route misses §18.8 (ii) clause 5's ceiling
  by **2.2445·10⁶ in the log**, which is §19.6 (i)'s sharpening); **B3** (the equipartition B = 52488 sits **4.58
  decades** inside the restated ceiling 10⁹/λ_f = 2·10⁹); **C1** (the exact rational step 1/(1 − x) ≤ 1 + 2x of
  Lemma DOM, 0 violations on x ∈ {2⁻¹…2⁻¹⁰}); **C2** (the level-0 window log C_fc^{(0)} = **13.7254756**, §19.7 (iv));
  **D1** (the d = 4 ring exponent is −1 and the partial-sum increments match ln 10 to 0.02%, i.e. **logarithmically
  divergent**); **E1** (χ = 625, θ_max = 6.6667·10⁻⁵ > 8·10⁻⁷); **F1** (1 + 3^d = 82 and 1 + 2^d = 17 at d = 4, the
  closed- and open-column ring prices of Finding (BUF-CC), differing by exactly 81/16).
- **Negative controls.** **A3**: with ε_1 := g_K the A1 quantity is exactly 1, so the 4.489·10¹⁵ is a statement about the
  two thresholds and not about the formula (p6 A3, reproduced). **B2**: the identity vanishes at λ = 0 and gives
  362574.26 at λ = 1 − 10⁻⁶, so the λ-dependence is the claimed one. **C1n**: the inequality 1/(1 − x) ≤ 1 + 2x **FAILS**
  at x = 3/4 (4 vs 5/2), so Rg_K² ≤ ½ is load-bearing in Lemma DOM′. **D2**: at d = 5 the same exponent formula gives −2
  and the partial sum converges to π²/6 within 10⁻⁵, so D1's divergence is a property of d = 4 and not of the script.
- **Scope, stated as narrowly as it is.** p7 is arithmetic about constants recorded in earlier sessions and about
  inequalities PLD/HW already state. It tests **nothing** about the lattice measure: not (CLS-min), not (LCR^act′), not
  (EQ-bc), not (BCH-1)/(BCH-0), not (W0-EQ), not (CEM^{COL})/(CEM-1)/(CEM-2), not (E2^𝔉′), and nothing nonabelian.
  **No number in p7 is evidence for or against any open statement of §19**, and D1/D2 are an INDICATIVE power count that
  proves nothing about the regress — they only show that the count PLD §19.6 (ρ1) performs is marginal at d = 4 and
  convergent at d = 5.

## 19.10 T20 + outcome against the pre-stated targets (§19.0), status changes, and tally

**T19 (a): PARTIAL SUCCESS as pre-stated, by route (ii), and the pre-stated failure mode (NP-F10) is NOT met.** The
Markov / conditional-independence structure across the R-free ring **exists and is exact**: Lemma DLR computes
E_ν[Z·F] = E_ν[ζ·F] with the far weight eliminated at cost 1, and Theorem W-FREE states the consequence —
**(CEM-2) as stated in §18.7.2 is not an ingredient of (CEM^{COL}) and is not to be attacked as one.** The residual is
**(BCH-1)**, strictly smaller than (CEM-2) in four named ways (§19.6). The typicality mechanism is **priced**:
1/(1 − λ_f) per cube in the exponential currency, 1 + log⁺C in the first-moment currency, against the event route's
4.489·10¹⁵ — which in the first-moment currency misses the admissible ceiling by **2.2445·10⁶ in the log** (p7 A2), a
sharper statement than §18.7.2's. The structural reason the thresholds cancel is §19.6 (iii). **(NP-F11) is also not
met**: every price computed is g-independent and in an admissible currency (per-cube constants, or the union-form patch
allowance HW already asks for).
**T19 (b): MET, with a self-correction.** (CEM-1)'s three ingredients become **two**: (a) the representation domination
is **unchanged and still OPEN** — §19.4's claim that it is unnecessary was WITHDRAWN in §19.5, with the sharp reason
(the trade compares 𝔞^col with the exponent of the level-(k−1) **marginal**, and the fluctuation terms between them are
exactly the representation's content); (b) and (c) **merge into one** mean-action bound uniform on λ ∈ [0, λ_f], because
the u-interval is the integration variable of an exact identity and not a separate hypothesis on activity bounds.
**T19 (c): MET.** **(LCR^act′)_m** (§19.4, with §19.5's 𝔞^col substitution): a **first-moment** statement, with clauses
1, 3, 5 of §18.8 (ii) kept, clause 2 demoted (the weight does not enter the column's conditional law at all) and
clause 4 discharged (a first moment carries no allowance; exponentiating gives form (P0)). It is **not refuted by
§18.8 (i)**, whose impossibility argument bounds a conditional **exponential** moment from below and says nothing about a
first moment — which is the exact sense in which §16.7's (LCR) needed restating. **(NP-F12) is not met**: (LCR^act′) is
consumable, by Proposition ACT-EQ (i) with w ≡ 1.
**T19 (d): MET, and the pre-stated (NP-F13) is REFUTED.** **(0a) is strictly weaker than (0b)** (proof in §19.7: (0b)
needs a level-0 (SDP), for which this lane has no route, there being no U_{-1} to integrate). **Theorem L0** reduces
(0a) to **(W0-EQ)**, a Laplace-asymptotics statement on **one 3⁴ block, 648 dimensions, 645 transverse after the single
interior site's gauge directions**, uniform over the compact space of boundary data, at couplings ≥ (1 − θ)u_0 — plus the
same (BCH-0) residual as every other level. Its equipartition value gives **log C_fc^{(0)} = 13.7254756** (p7 C2),
twelve orders inside the ceiling. **Level 0 is the most tractable instance in the family, not the hardest**: Lemma DOM′
is an identity there, with no (F_R) slack and no infimum, so §19.5's extensivity defect cannot occur, and the bare
Wilson measure's own DLR property replaces the kernel's Markov property.
**T19 (e): MET** (§19.8): the chain is written out, and the single remaining obstruction is **(BCH-1)** — removable
altogether by route (ρ2) at three computed prices, after which **(SDP)^A ⇐ (CLS-min) + (RING-cc) + one weight-free
single-level statement**.
**T20: MET** (this section). **T21: MET, 0 FAIL** (§19.9; two criteria honestly labelled CONFIRMATORY rather than
pre-registered). **T22: MET** (§19.11; nothing outside PLD.md, PLD_LOG.md and checks/p7_* was written; no git command
was run).

**Counted, PROVEN-HERE (unreviewed): 3 items.**
- **[E7] (1) The read/Markov package:** **Lemma READ** (the exact read-sets of Z, 1_{R,k-1}, Φ_{k-1}, F_<, w),
  **Finding (BUF-CC)** (the closed-column gap in §18.7.0's use of Lemma BUF, its repair (RING-cc), and the ×82-not-×17
  price, which settles HANDOFF's open cross-lane disagreement), **Lemma MARG** (§18.7.0's two generators collapse to one
  level-(k−1) future weight), **Lemma DLR** (the exact elimination of the far weight by the chain's Markov property) and
  **Theorem W-FREE** ((CEM-2) is not an ingredient; the weight enters only through one local product functional).
- **[E7] (2) The action-trade package:** **Lemma DOM** and **Lemma DOM′** (the moment's exponent is λ_f times the
  chain's own — minimised — column action, with λ_f = 24θ(1 + 2Rg_K²) rebuilt from (F_R) and the κ's shown to cancel),
  **Theorem AT** (the moment is a local coupling-lowering ratio, and its log is the integral of a MEAN), **Proposition
  ACT-EQ**, **Proposition TRADE** (the typicality price, both currencies), **Theorem OUT** (the outside decomposition:
  (ACT′) ⇐ (EQ-bc) + (BCH-1)), and the restated **(LCR^act′)**. **Includes the withdrawal of (ACT) and of Proposition
  CEM1-COLLAPSE (a) (§19.5), which is part of the counted item, not an erratum to it.**
- **[E7] (3) The level-0 reduction:** **Theorem L0**, the strict ordering (0a) < (0b), the 645-dimensional count, and the
  refutation of (NP-F13).
**Not counted:** §19.6's route (ρ1) power count (INDICATIVE) and route (ρ2) (ARGUED); §19.5's refutation of (ACT)
(ARGUED, resting on an unproven equipartition lower bound); §19.8's chain table.
**OPEN, newly named here:** **(RING-cc)** (the closed-column ring hypothesis); **(ACT′)_k** (the column-action moment);
**(LCR^act′)_m** (the restated (LCR)); **(EQ-bc)_k** (conditional equipartition with the boundary charge; weight-free);
**(BCH-1)_k** / **(BCH-0)** (the boundary charge's first moment under the weighted law — **the single obstruction**);
**(W0-EQ)** (the level-0 one-block mean-energy statement).

**Status CHANGES to earlier items, with direction.**
- **DOWNGRADE.** §18.7.2's **Proposition SPLIT** is demoted from "the reduction of (CEM^{COL})" to **a lossy reduction**:
  it estimates by comparison a ratio that Lemma DLR computes exactly. Consequently **§18.11's "single biggest remaining
  obstruction = (CEM-2)" is superseded**; the obstruction is (BCH-1). (CEM-1) and (CEM-2) remain well-posed statements;
  they are no longer the route of record.
- **DOWNGRADE.** §18.7.0's law class, §18.7.1's (CEM^{COL}) and Theorem NA-PRICE^{E+}'s hypothesis "**N_1(𝒜) R-free**" is
  **insufficient**: Lemma BUF at level k − 1 needs the **closed** column, (RING-cc) (Finding (BUF-CC)). The implications
  of §18.7 all stand with the strengthened hypothesis; the hypothesis is to be restated.
- **DOWNGRADE (cross-lane).** HW §41 item 4's instruction "Please re-read §18.4's ×82 as ×17" is **withdrawn for the
  level-(k−1) application**: HW's Lemma RING is correct for the OPEN column, and the proof needs the CLOSED one, where
  the price is ×82 (p7 F1). **§18.4's own ×82 stands.** HANDOFF's cross-lane disagreement 1 is thereby settled, with both
  lanes right about different objects.
- **DOWNGRADE (self, same session).** **(ACT)** as stated in §19.4 → **WITHDRAWN** (§19.5), with the extensivity
  argument; Proposition CEM1-COLLAPSE (a) → withdrawn with it.
- **UPGRADE.** **(CEM-2) → not needed** (Theorem W-FREE), replaced by the strictly smaller (BCH-1).
- **UPGRADE.** **(CEM-1): three named ingredients → two**, (b) and (c) being one statement.
- **UPGRADE.** §18.7.2's "Gaussian heuristic" **log c_1 ≈ 1.82·10⁴** → **identified as the equipartition value of an
  exact identity**, reproduced to 0.0046 (p7 B1). It is no longer a heuristic; what is open is the mean-action bound, not
  the arithmetic.
- **UPGRADE.** The **level-0 clause (0a)** → reduced to one finite-dimensional statement with a computed window constant;
  **(0a) < (0b)** strictly; and level 0 is reclassified from "the largest residual after the moment" (HW §37, §18.9 M-3)
  to **the most tractable instance of the family**. (0b) stays OPEN and strictly harder.
- **UPGRADE.** §18.7.0's two weight generators → **one** (Lemma MARG).
- **UPGRADE (conditional).** If route (ρ2) is taken, **no statement in the (SDP)^A chain mentions the far weight**.
- **NO CHANGE.** (CLS-min); §18.7.2 (a)'s representation domination (still OPEN, still the first thing to write);
  Lemmas CW, KD, MD, DIL-L; Proposition FAR; Lemma BUF as a lemma; Proposition PATCH; (EG-link); (J-NS^cd); Theorem
  NA-PRICE^E (i); every p4/p5/p6 number.
**Tally proposal: +3 PROVEN-HERE (unreviewed); 0 OPEN items closed.** Row 10b's residual on route (ii) is no longer
(CEM^{COL}) as a single statement but the pair **(EQ-bc) + (BCH-1)**, of which the first is weight-free and the second is
removable by route (ρ2) at a computed price.

**The single biggest remaining obstruction in this scope, named.** **(BCH-1)**: the first moment, under the
buffered-weighted past law of a pattern in 𝔉_𝔥, of the boundary-forced conditional free-energy excess of a level-k
cube's column, uniformly in g, k, K, T, 𝔥, R, 𝒜, 𝒜′, F, F_< and λ ∈ [0, λ_f]. It is the **only** item left in the
(SDP)^A chain whose statement mentions the far weight; it is one scalar per cube and a first moment; and route (ρ2)
removes it at the price of c_A = 0, ×82, and θ ≤ 6.67·10⁻⁵. **Everything else reduces to (CLS-min) and to (EQ-bc), a
weight-free, law-class-free, single-level small-field statement whose level-0 case is 645-dimensional.**

## 19.11 FOR OTHER FILES (session 7; not edited)

Nothing below is applied anywhere. Session 7 wrote only PLD.md (appended), PLD_LOG.md (appended) and checks/p7_*. **No
git command of any kind was run**; no commit, push or PR; no axiom or CL edit; no numeric lock taken or released; no
other lane's file touched, read-only access only.

**To the PLD owner (next session's in-place pass).**
1. **Restate §18.7.0, §18.7.1 and Theorem NA-PRICE^{E+}'s hypothesis as (RING-cc)** (the closed column of N_1(𝒜)
   unconstrained), per Finding (BUF-CC). The implications are unaffected; only the hypothesis moves. Record the ×82 price
   there, not ×17.
2. **Record that §18.11's named obstruction is superseded**: (CEM-2) is not an ingredient of (CEM^{COL}) (Theorem
   W-FREE), and the residual is (BCH-1). Keep (CEM-1)/(CEM-2) as well-posed statements but not as the route of record.
3. **Replace §16.7's (LCR) by (LCR^act′)** (§19.4 as corrected in §19.5) in every interface line, and delete §18.8 (ii)
   clause 4 as a separate ask (a first moment carries no allowance).
4. **§18.7.2's dof = 3n_int·81 = 52488 needs its geometric count stated.** p7 B1 confirms that this dof reproduces
   p6 D1's 18190.95 through the equipartition identity, but §18.7.2 does not say which set of links it counts. My reading
   is that it is the level-(k−1) group degrees of freedom the column's top terms involve; if it is instead a two-level
   count, the identity is unchanged and only the number moves. Please state the count.

**To the HW owner (lane H) — three items, one of them a reversal of §41 item 4.**
1. **The ring price is ×82, not ×17, for the application node A actually makes.** HW §41 item 4's Lemma RING
   (|sh_r(N_1X)| ≤ 2^d|sh_r(X)|, r ≥ 1) is correct, and so is its reason "only the OPEN column enters #_{R′}, so the
   m = 0 term never appears" — **but node A's Lemma BUF is applied at level k − 1, to col_{k-1}(𝒜), and a level-(k−1)
   cube is R-free only if the CLOSED column of its level-k parent is unconstrained** (Finding (BUF-CC): the open column
   of a level-(k−1) cube contains the pair (k, π(x))). With the closed column the m = 0 term does appear and HW's own two
   inequalities give #_R([N_1X]) ≤ 81|X| + 16Σ_{r≥1}|sh_r(X)| ≤ 81‖X‖_sh, i.e. **c_+ = c_A + 82c_U** (p7 F1: 1 + 3^d = 82
   against 1 + 2^d = 17, ratio exactly 81/16). **So please re-instate ×82 for the level-(k−1) use, keep ×17 for the
   level-k use, and withdraw §41 item 4's instruction to node A.** This also settles HANDOFF's open cross-lane
   disagreement 1: both lanes were right about different objects. Consequences for §35.7's table: g²_CRC and n_♯ move by
   82/17 = 4.82 relative to the session-6 figures on the level-(k−1) row.
2. **The level-0 clause (0a) is the tractable one, and it is now reduced.** §37 records (0a) and (0b) as "OPEN on both
   sides, the largest residual after the moment". §19.7's Theorem L0 reduces **(0a)** to one finite-dimensional
   statement — mean plaquette energy on a single 3⁴ block, 645 transverse dimensions, uniform in the boundary datum, at
   couplings ≥ (1 − θ)u_0, with the boundary free-energy excess subtracted — plus the same (BCH-0) residual as every
   other level, and computes the resulting window constant log C_fc^{(0)} = 13.73 (p7 C2). **(0b) is strictly harder**
   (it needs a level-0 (SDP), for which there is no U_{-1} to integrate). **Please state (E2^𝔉′)'s level-0 clause as (0a)
   only**, and drop (0b): node A has a route to (0a) and none to (0b).
3. **§37's own diagnosis is confirmed and sharpened.** §37 ends with "ν^w(·) ≤ ν(·)/E_ν[w] … so (E2^𝔉′) fails unless
   conditioning on the coarser constraints costs no volume factor — a positivity-of-density statement with a boundary
   allowance". §19.2's Lemma DLR shows that **no such positivity is needed for the column's conditional law**: the far
   weight factors out exactly by the chain's Markov property across one R-free ring, at cost 1. The positivity
   requirement survives **only** for the boundary charge's first moment, (BCH-1) — and route (ρ2) discharges even that
   from CRC-2T′'s own induction, at the patch allowance e^{82c_U‖P‖_sh} that §37 already asks for. **So §37's "that is
   the exact residual of the whole HW route, and it is one statement, owned by node A" is right, and the statement is
   (BCH-1), not (CEM-2).**

**To the RLARGE integrator.**
1. **Row 10b, route (ii)** should name its hypotheses as **(CLS-min) + (RING-cc) + (EQ-bc) + (BCH-1)**, not
   (CLS-min) + (CEM^{COL}); and should record that (BCH-1) is removable by route (ρ2) at the price c_A = 0 → the patch
   allowance, ×82, and θ ≤ 6.67·10⁻⁵. Add rows **(RING-cc)**, **(ACT′)**, **(LCR^act′)**, **(EQ-bc)**, **(BCH-1)**,
   **(BCH-0)**, **(W0-EQ)** [all node A], and mark **(CEM-2)** as *not on the route of record* (not refuted; superseded).
2. **K12 needs both readings recorded.** On route (ii) without (ρ2), §18.7's θ ↑ 1/24 stands. **With (ρ2) the colouring
   step forces θ ≤ 1/(24·5^d) = 6.67·10⁻⁵** (p7 E1) — still 80× above the feared fallback θ ≈ 8·10⁻⁷, so n_H rises by
   ≤ 5^d = 625 rather than by ≈ 5·10⁴. Please record the pair, not a single number.
3. **The critical-path item 1 label should change** from "(E2^𝔉′): good-buffer screening" to "**(EQ-bc) + (BCH-1)**: a
   conditional equipartition bound for the column action, plus the boundary charge's first moment", because §19.2 shows
   the screening content is a **Markov** statement that is already proven, not an estimate to be obtained.

**To the owners of NORMS.md / PROOF.md (one connection, offered as a question, not a claim).**
§19.6's route (ρ1) — the outward regress for the boundary charge — is **logarithmically divergent at d = 4 under naive
power counting and convergent at d = 5** (p7 D1/D2, labelled INDICATIVE). That is the same marginality NORMS §N5 proves
for the per-level route ("the d = 4 cubic vertex is marginal, so A ≥ 1 in every scale-covariant norm") and the same one
the brief's D3 diagnosis attributes to counting every fine leg at its sup size. **Question for those owners: is the
Bianchi/derivative cancellation that takes K_p^sharp from 2.27 to ≈ 0.12 on closed inputs the same resummation the
boundary-charge regress needs?** If it is, (BCH-1) and the constants problem are one problem and should be worked once;
if it is not, (ρ1) is a dead route and (ρ2) is the only one. I cannot decide this from inside this lane.

**To the lead (HANDOFF.md).**
- **Cross-lane disagreement 1 is settled** (item 1 to HW above): ×17 open column, ×82 closed column, the proof needs the
  closed one. It can come off the "left open on purpose" list.
- **The critical-path entry 3 should be rewritten.** It currently reads "(CEM-1) and (CEM-2), plus the level-0 clause".
  The honest replacement after session 7: *"(EQ-bc) — a conditional equipartition bound for the column action, weight-free
  and law-class-free — plus (BCH-1), the boundary charge's first moment under the weighted law, which route (ρ2) can
  remove at a computed price. (CEM-2) is not an ingredient (PLD Theorem W-FREE). The level-0 clause is reduced to one
  645-dimensional one-block statement (PLD Theorem L0) and is the most tractable instance, not the largest residual."*
- **For the next review's brief, three places to attack first:** (i) **Lemma DLR (i)'s factor audit** — it is the whole
  basis of the session and a single missed factor of the past law's density breaks it; (ii) **§19.5's withdrawal of
  (ACT)** — the extensivity refutation rests on an unproven equipartition lower bound, so a reviewer should decide
  whether the withdrawal was necessary or over-cautious; (iii) **Finding (BUF-CC)** — it reverses a binding instruction
  in HW §41 and changes a constant two lanes quote, so it should be re-walked independently against HW §30.1's own
  definition of "R-free".
