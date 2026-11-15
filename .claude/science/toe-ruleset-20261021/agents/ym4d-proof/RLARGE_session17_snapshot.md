# RLARGE: the 4D large-field R-operation for the soft-kernel RG (session 17, 2026-10-27)

Scope. Balaban's large-field renormalisation (CMP 122 (1989) 175-202 and 355-392) is [not-read]; no open source states
it (literature/NOTES.md §10: OSTI abstracts [read-abs]; Dimock II p.31 Remark 3 [read]: the R-operation "converts some
large field contributions back to small field contributions" and is "not necessary" for φ⁴_3). Nothing below is
attributed to Balaban. Everything here is for the decision-4 kernel (S4' contour averaging, normalised soft
gauge-covariant constraint; PROOF.md L5 [S9]). Status words as in PROOF.md: PROVEN-HERE (counted or not, said each time),
ARGUED, OPEN, HYPOTHESIS. Imported items are never load-bearing for a PROVEN-HERE claim.

Inputs used (PROOF.md, read by offset this session): LF-count (L6loc [S6]); R2D-iso, R4D-iso, GT (L5 [S7]-[S8]);
D4-norm, GT-lat, R4D-lat, BG-sum, W1-size', W1-LD-cond, (DF) (L5 [S9]); Theorem CE and Lemma CE-geo' (L5 [S10]-[S11]);
the (DF) sub-DAG N1-N12; inequality (B) and E8*/E8** (L6loc); L6; RTARGET.md §0-11 (in particular §7, the W2
pre-statement); REVIEW_S15_CONVERGENCE (critical path, node B-W2); LINEAR_PACKAGE.md §9-10.

File order. §0-§2 were written at 2026-10-27 20:58 UTC, after reading the inputs and after the lead's exploratory
reasoning in this session, BEFORE any written derivation in §3 onward and before the c32 criteria and script. §0-§2 are
not edited after the derivations start; outcomes are pointers in §9, added afterwards.

---

## 0. Conventions fixed for this file

- **Levels.** Level k = after k RG steps; k = 0 is the bare (finest) lattice, k = K the unit lattice. (This matches
  LF-count's N_k = L^{4(K-k)}|T| count; it is the reverse of Setting S1's "resolution" index.) U_k is the level-k field on
  Λ_k, d = 4, L ≥ 3 odd, G = SU(N), N ≥ 2.
- **Action normalisation** (R4D-iso's): s(U) := 1 - N^{-1}Re tr U ∈ [0, 2]; level-k Wilson term (1/g_k²)Σ_p s(U_p).
  Inequality (B): s(U) = ||1 - U||²_HS/(2N) ≥ ||1 - U||²_op/(2N).
- **The exact chain.** e^{-S_0} := Wilson at g_0; e^{-S_{k+1}(V)} := ∫K_k(V, U)e^{-S_k(U)}dU, with the normalised soft kernel
  K_k = Π_c k_c, k_c = exp(-(κ/g_k²)[1 - N^{-1}Re tr(V_c^{-1}M̄_c(U))])/𝒩_k(M̄_c(U)) (D4-norm). ∫K_k dV = 1, so
  Z_K = ∫e^{-S_k}dU_k for every k. The joint law of (U_0, …, U_k) is a Markov chain.
- **Level-k cubes.** A level-k cube □ is a level-k block (L⁴ level-k sites; one level-(k+1) site); N_k := L^{4(K-k-1)}|T|
  cubes. Small-field indicator χ_□ := Π_{p⊂int □}1{||1 - U_k(p)||_op < ε_1} (R4D-iso's cut); ζ_□ := 1 - χ_□.
- **Flow hypothesis (F)** (the AF flow, OPEN as A5 / L4a-flow; the lower half is the one used for summability):
  β_-(k - j) log L ≤ 1/g_j² - 1/g_k² ≤ β_+(k - j) log L for 0 ≤ j ≤ k ≤ K, with 0 < β_- ≤ β_+.
- **Polymers.** A level-k cluster Y is a nonempty *-connected set of level-k cubes (cubes adjacent iff their closures
  meet); |Y| := its number of cubes. *-separated clusters are at cube distance ≥ 2.

## 1. Target 1: the statement RLF (pre-stated)

**What a 4D large-field R-operation must deliver** (the reconstruction target LF-count names, in the soft setting):

**Theorem RLF (target; OPEN).** There are g-independent constants ε_1 > 0, a > 0, κ_d > 0, C, an integer n_* ≥ 0 with
(n_* + 1)aβ_- > 4, and g_0 > 0 such that for every K, every torus T (side ≥ 3 blocks at level K) and every coupling
sequence with g_K ≤ g_0 obeying (F):

- **(RLF-0) Counterterms.** For each level k and each cluster shape Y with |Y| ≤ n_* (shapes up to translation), there
  are a field-independent number c_0(Y; g_k) and a field-independent Ad-invariant quadratic form T_Y(g_k) on
  su(N) ⊗ Λ²R⁴, with |c_0(Y; g_k)| + ||T_Y(g_k)|| ≤ C^{|Y|}e^{-a|Y|/g_k²}, depending only on (Y, g_k, L, N, κ, ε_1) and on
  the shape class (translation covariant; B_4-covariant). The marginal parts combine per level into ONE coupling shift
  δβ_k := Σ_{[Y]}t̄_{[Y]}(g_k) (B_4-orbit averages), with Σ_k|δβ_k| ≤ Ce^{-a/g_K²} uniformly in K and |δβ_k| ≤ g_k^6.
- **(RLF-1) Exact factorisation of the vacuum part.** Z_K = exp(Σ_{k<K}Σ_{Y: |Y|≤n_*}c_0(Y; g_k)) · Z_K^{ren}, where the
  inner sum runs over all placements of all shapes at level k (so the prefactor is a field-independent c-number,
  Σ_k O(N_k e^{-a/g_k²}), the only K-divergent quantity, which LF-count shows to be divergent).
- **(RLF-2) Returned (recycled) contributions.** In Z_K^{ren} every level-k cluster of ≤ n_* bad cubes with a small-field
  collar is returned to the small-field region: its contribution is the remainder R(Y) after subtracting c_0 and the
  T_Y-term, with |R(Y)| ≤ C^{|Y|}e^{-a|Y|/g_k²}·𝔯_k(Y) and 𝔯_k(Y) the GT-lat remainder functional of the level-(k+1)
  background on Y's box, and with exponential tails e^{-κ_d d(X)} in its dependence on the far field; and per final
  unit cell, Σ_{k}Σ_{Y in the cell}|R(Y)| ≤ C sup_k(C e^{-a/g_k²}) uniformly in K (summable against L^{4(K-k)}).
- **(RLF-3) Unreturned large fields.** Clusters with |Y| > n_* (and clusters whose collar is not small-field) stay
  large-field regions, nested as in Dimock II (small-field regions decrease with k), with weights
  ≤ Π_Y(Ce^{-a/g_k²})^{|Y|}, and Σ over all such histories ≤ exp(C|T|e^{-(n_*+1)a/g_K²}).
- **(RLF-4) Output.** |log Z_K^{ren} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} uniformly in K (any a' < a), where Z_K^{sf} is the
  small-field partition function of the soft RG with couplings shifted by δβ_k. Together with the small-field package
  (node A), this is L6-soft modulo the vacuum c-number of (RLF-1).
- **Composition.** With **LF-count**: the divergent per-level sum of LF-count sits entirely in the c-number of (RLF-1).
  With **R4D-iso**: the case |Y| = 1, frozen exterior, is R4D-iso/R4D-lat/D4-norm (c_0 = log(1 + ρ_0), T_Y = c_ρ-term).
  With **Theorem CE**: at level K the remainders R(Y) and the unreturned large-field polymers are activities H(X) obeying
  |H(X)| ≤ H_0e^{-κd(X)} with κ > 3κ_0 + 3 (≈ 457 in M-units) and H_0 ≤ c_0(κ), for g_K small enough (to be made
  explicit).

## 2. Targets 2 and 3 (pre-stated)

**Target 2: the two-scale case, frozen exterior (W2, extending R4D-iso).** Levels j < k. A level-k cell Δ that is
large-field at level k (some level-k plaquette in Δ has ||1 - U_k(P)|| ≥ ε_1), containing level-j clusters (bad at level j).
Frozen exterior: all variables outside the clusters are given. Claims to prove, with constants stated:
- (T2a) A renormalised identity for each inner cluster with FIXED constants (defined at the trivial background, so
  independent of the level-k field), generalising R4D-iso from one cube to a cluster of ≤ n_* cubes (adjacent cubes allowed).
- (T2b) A bound for the sum of the inner remainders over all inner levels j < k, uniform in j, k and in the size of the
  level-k field, under a precisely stated regularity hypothesis on the frozen data.
- (T2c) A bound pricing the level-k large field by the level-(k-1) variables (one step only; never iterated).
- (T2d) The status of RTARGET §7's failure modes W2-F1 (no smooth background), W2-F2 (inner vacuum depends on the outer
  field), W2-F3 (history combinatorics), each MET / AVOIDED / CIRCUMVENTED-with-a-named-hypothesis.
- Not success: a statement for an isolated single cube only (that is R4D-iso); constants that are not stated.

**Target 3: the inductive step over scales, sea fluctuating.** Assume a representation (I_k) of e^{-S_k} at level k of the
RLF form. Prove (I_{k+1}) as far as possible, conditional only on NAMED hypotheses (each a precise statement: (DF) at
level k, large deviations of the sea, BG-b, the flow (F), history bookkeeping), and prove unconditionally the level
summations (vacuum, coupling shifts, remainders, unreturned clusters). Output: a precise list of what remains, each item
with its inputs and its weight (P = paper-scale, s = session-scale).

**Failure modes (each a valid, precisely named outcome).** (RLF-F1) the per-cube exponent of a cluster of n bad cubes is
not proportional to n (then no finite n_*); (RLF-F2) the cluster counterterms are not field-independent or not
B_4-reducible to a single coupling shift; (RLF-F3) the remainders need the regularity of the large (level-k) field;
(RLF-F4) the outer large field cannot be priced by one step of the chain.

**Check c32** (criteria file first): the re-seeding constants of target (T2c) on explicit SU(2) configurations in d = 4
(L = 3), including configurations that attain the constants; the truncated-cluster combinatorics of (T2a); the n_*
arithmetic (informational, one-loop rate).

---
# Derivations (written after §0-§2)

## 3. The R-operation in the soft setting: what it is (definition-level, exact)

The soft kernel makes the RG an exact Markov chain with positive integrand, so the R-operation can be formulated as an
exact rewriting of one RG step, with no constraint fibres (W3 absent). Fix a level j and write U for the level-j field,
V for the level-(j+1) coarse links, e^{-S}(U) := e^{-S_j(U)}·K_j(V, U) for the step-j integrand (bare form: S_j = Wilson
at g := g_j, as in R4D-iso; effective levels: §8).

- **Notation.** For a set B of level-j cubes, int(B) := the links with both ends in one cube of B; C(B) := the coarse
  links with an endpoint block in B (≤ 8|B|); w_B(U_{int B}; D) := exp(-(1/g²)Σ_{p∩int B≠∅}s(U_p))·Π_{c∈C(B)}k_c, where
  D := U restricted to the links outside int(B), together with V. Every factor of e^{-S} that involves an int(B) link is in
  w_B, so e^{-S} = w_B·w_rest with w_rest independent of U_{int B}.
- **Frozen cluster activity.** r_B(D) := Num_B/Den_B, Num_B := ∫Π_{Q∈B}ζ_Q w_B dU_{int B}, Den_B := ∫Π_{Q∈B}χ_Q w_B dU_{int B}.
  For |B| = 1 this is R4D-iso's ρ (with the D4-norm kernel).
- **The R-operation at level j** (definition). Expand Π_Q(χ_Q + ζ_Q) = Σ_BΠ_{Q∈B}ζ_QΠ_{Q∉B}χ_Q, pass to the frozen activities
  (Proposition CL (a)), take the logarithm of the resulting hard-core gas (Theorem R1 (i)), and split each connected
  term of total cube number N ≤ n_* into (its value at trivial data: a c-number) + (its Ad-invariant quadratic part: after
  B_4-averaging, a coupling shift) + (a remainder of irrelevant order). The c-numbers are the vacuum counterterm, the
  quadratic parts are "returned" to the small-field action as the coupling shift δβ_j, and the remainders are small
  local insertions. Terms with N > n_* are kept unrenormalised (they are summable: Lemma LF-n). This is the soft-kernel
  form of "converting large-field contributions back to small-field contributions" (Dimock II p.31 [read]); whether it
  coincides with Balaban's construction is unknown [CMP 122 not-read].

## 4. Lemma GT-lat' (lattice Taylor lemma without point symmetry; B_4 orbit averages): PROVEN-HERE [S17]

*Setting.* As GT-lat (PROOF L5 [S9]): box B̂ = {|x_μ| ≤ R_0} about a block centre 0, R̂ its links, complete-axial tree
paths π_x from 0, P̂_p := log(hol(π_x)U_p hol(π_x)^{-1}), Φ(D) := (P̂_{(0;μ,ν)})_{μ<ν}, ε_2, ε_3 as there. Two changes:
(1) C is ANY finite set of coarse links c (straight segments of length L between block centres inside B̂), not
necessarily from 0 or B_4-symmetric; ε_V := max_{c∈C}||log(V_cS_c^{-1})||_op, S_c the straight fine transporter along c.
(2) F is C³ on {ε_2 + ε_V ≤ r_1} and invariant under all gauge transformations of the data; **no B_4 or ι invariance**.

*Claim.* (i) Put Q_F(Φ) := ½D²F̃_rad(0)(𝓛Φ, 𝓛Φ) (GT's radial chart, 𝓛 GT's linear map). Then Q_F is Ad-invariant, so
Q_F(Φ) = Σ_{a,b}t^F_{ab}⟨Φ_a, Φ_b⟩_HS for a real symmetric 6 × 6 matrix t^F (a, b label the planes μ < ν), and
  |F(D) - F(1) - Q_F(Φ(D))| ≤ C K_F 𝔯(D),  𝔯 := ε_2(ε_3 + ε_V) + (ε_3 + ε_V)² + ε_2³,
with K_F as in GT-lat and C = C(R_0, C).
(ii) For R ∈ B_4 (about 0), (R·D) the rotated data and F∘R(D) := F(R·D): t^{F∘R} = Λ²(R)^T t^F Λ²(R). If a finite family
{F_i} is permuted by D ↦ R·D for every R ∈ B_4, then Σ_iQ_{F_i}(Φ) = c̄·Σ_a||Φ_a||²_HS with c̄ := (1/6)Σ_i tr t^{F_i}.

*Proof.* (i) GT-lat steps 1-3 hold with one addition. In tree gauge a coarse link c from x to x' has S_c = hol of the
closed loop π_x c π_{x'}^{-1}, which bounds a lattice surface of at most A(R_0) plaquettes in B̂ (the box's 2-complex is
simply connected; the count is combinatorial). As for U_b in GT-lat step 1, ||log S_c|| ≤ Cε_2 and
log S_c = Σ±P̂_{p_i} + O(ε_2²). Use the tree coordinate Y_c := log V_c; then ||Y_c|| ≤ ε_V + Cε_2 + Cε_Vε_2. For the
reference data put V^Φ_c := S_c(D^Φ) (so ε_V(D^Φ) = 0). Since log S_c(D) - log S_c(D^Φ) = Σ±(P̂_{p_i}(D) - P̂_{p_i}(D^Φ)) +
O(ε_2²) and ||P̂_p(D) - P̂_p(D^Φ)|| ≤ ε_3 + Cε_2² (GT-lat step 2), |Y_c(D) - Y_c(D^Φ)| ≤ C(ε_V + ε_3 + ε_2²). So step 2's two
estimates |Z(D) - Z(D^Φ)| ≤ C(ε_3 + ε_2² + ε_V), |Z(D^Φ)| ≤ Cε_2 hold. Step 3 is unchanged: a constant gauge
transformation acts on every tree coordinate (links and coarse links) by Ad, so DF̃(0) = 0. Step 4 without B_4: F(D^Φ) =
F̃_rad(𝓛Φ) = F(1) + Q_F(Φ) + R_3 with |R_3| ≤ CK_Fε_2³; D²F̃_rad(0) is Ad-invariant and 𝓛 is Ad-equivariant, so Q_F is
Ad-invariant. Ad-invariant symmetric bilinear forms on su(N) ⊗ R⁶ are ⟨·,·⟩_HS ⊗ t, because su(N) is absolutely
irreducible under Ad (End_Ad(su(N)) = R), exactly as in GT step 5. Combine as in GT-lat step 5.
(ii) GT-lat step 4 proves R·(𝓛Φ) = 𝓛(Λ²(R)Φ) exactly on the lattice (coarse straight links map to coarse straight links).
Hence Q_{F∘R}(Φ) = Q_F(Λ²(R)Φ), i.e. t^{F∘R} = Λ²(R)^Tt^FΛ²(R). If the family is permuted, T := Σ_it^{F_i} commutes with
Λ²(R) for every R ∈ B_4. Λ²R⁴ is absolutely irreducible under B_4 (GT step 5; c19 P1), so T = (tr T/6)·1. ∎

*Remark.* (i) is the general (non-symmetric) cluster version of GT-lat: a cluster of cubes has no point symmetry, and its
quadratic part is a general Ad-invariant form. (ii) says the B_4-orbit sum of the shapes restores a single invariant.

## 5. Proposition CL (frozen cluster activities): PROVEN-HERE [S17]

*Setting.* §3, bare form at level j (Wilson at g, normalised soft kernel D4-norm), g ≤ min(1, √κ). Constants:
n_ℓ := 4L³(L - 1) (links with both ends in one block), n_P := 6n_ℓ, A_d(L) := (d - 1)L(L - 1)/2 (Lemma RS), p_L := 5L - 4
(contour length, NA-lev), r := ε_1/16, c_N the Haar-ball constant (μ{||U - 1|| ≤ δ} ≥ c_Nδ^{N²-1}, δ ≤ 1),
  b_1 := n_P + 12κ(1 + A_d(L))²,  b_0 := 16n_P + 12κp_L²,  ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}.
For a cluster Y, N_1(Y) := the sites of the blocks of Y and of their *-neighbours, and the **completion parameter**
  ε_♭(D; Y) := min over U° ∈ SU(N)^{int Y} of [max_{p ⊂ N_1(Y)}||1 - U°_p||_op + max_{c∈C(Y)}||V_c - S_c(U°)||_op]
(U° completes D on int(Y); the minimum is attained by compactness).

*Claims.*
- (a) **Exact Fubini identity.** For every set B of cubes, Z_B/Z_∅ = ⟨r_B⟩_cut, where Z_B := ∫Π_{Q∈B}ζ_QΠ_{Q∉B}χ_Q e^{-S},
  ⟨·⟩_cut is the all-cut probability measure, and r_B is evaluated on the sample's links outside int(B). Hence
  Z/Z_∅ = ⟨Ξ⟩_cut with Ξ(U) := Σ_B r_B(U) (the frozen gas, evaluated on one sample).
- (b) **Factorisation.** If Y_1, …, Y_m are the *-components of B, then r_B = Π_ir_{Y_i}.
- (c) **Size, per cube uniform.** If ε_♭(D; Y) ≤ ε_loc then, for every *-connected Y of ANY size,
  r_Y(D) ≤ (C_r g^{-p_r} e^{-ε_1²/(4Ng²)})^{|Y|},  p_r := (N² - 1)(n_ℓ + 16),
  C_r := e^{b_0r²}c_N^{-(n_ℓ+8)}e^8κ^{8(N²-1)}r^{-(N²-1)n_ℓ}.
- (d) **Derivatives.** In the tree (or any local Lie) coordinates z of the data, for q ≤ 3 and coordinates z_1..z_q,
  |∂_{z_1}···∂_{z_q}r_Y| ≤ B_q(Λ_1/g²)^q r_Y, Λ_1 := 6 + κ(2 + C_𝒩) (C_𝒩 from D4-norm (3)), B_q combinatorial.
- (e) **Invariance.** r_Y is invariant under all gauge transformations of D, covariant under translations and under B_4
  about any block centre: r_{RY}(R·D) = r_Y(D).

*Proof.* (a) Z_B = ∫(Π_{Q∉B}χ_Q)w_rest·Num_B: the indicators χ_Q, Q ∉ B, involve only interior plaquettes of Q, hence no
int(B) link. Integrating the all-cut integrand over U_{int B} gives (Π_{Q∉B}χ_Q)w_rest·Den_B. So
Z_B = ∫(Π_{Q∉B}χ_Q)w_rest Den_B·r_B = Z_∅⟨r_B⟩_cut, because r_B depends only on links outside int(B). Sum over B (finite). ∎
(b) For *-separated Y, Y': a plaquette meeting int(Q) has all vertices within sup-distance 1 of the sites of Q, while the
sites of non-touching blocks are at sup-distance ≥ L + 1 ≥ 4; so no plaquette meets both int(Y) and int(Y'). A coarse link's
contours lie in its two endpoint blocks, which touch; so no coarse link is in C(Y) ∩ C(Y'). Hence w_B = Πw_{Y_i} in
disjoint variables, and the indicators factorise. ∎
(c) *Numerator.* On Π_{Q∈Y}ζ_Q every Q ∈ Y has an interior plaquette p_Q with ||1 - U_{p_Q}|| ≥ ε_1, so by (B)
s(U_{p_Q}) ≥ ε_1²/(2N). The p_Q are distinct (disjoint interiors) and all other Wilson terms are ≥ 0, so the Wilson factor is
≤ e^{-|Y|ε_1²/(2Ng²)}. Each k_c ≤ e c_N^{-1}(κ/g²)^{N²-1} (D4-norm (2)), |C(Y)| ≤ 8|Y|, Haar mass 1. *Denominator.* Let U°
attain ε° := ε_♭(D; Y) ≤ ε_loc; restrict to the caps ||U_b - U°_b|| ≤ rg (b ∈ int Y). A plaquette meeting int(Y) has
≤ 4 interior links, so ||1 - U_p|| ≤ ε° + 4rg ≤ ε_1/4 + ε_1/4 < ε_1: every χ_Q = 1, and s(U_p) ≤ ½||1 - U_p||² ≤
(ε°)² + 16r²g²; there are ≤ n_P|Y| such plaquettes. Each kernel term is the mean over contours of
1 - N^{-1}Re tr(V_c^{-1}T^σ_y(U)) ≤ ½||V_c - T^σ_y(U)||² (unitary words; D4-norm's linearity remark), and
||V_c - T^σ_y(U)|| ≤ ||V_c - S_c(U°)|| + ||S_c(U°) - T^σ_y(U°)|| + ||T^σ_y(U°) - T^σ_y(U)|| ≤ ε° + A_d(L)ε° + p_Lrg, by the
ribbon bound of Lemma RS (all plaquettes of the two endpoint blocks lie in N_1(Y)) and p_L ≤ 5L - 4 links per contour.
With (x + y + z)² ≤ 3(x² + y² + z²) and 𝒩 ≤ 1: g²S ≤ |Y|(b_1(ε°)² + b_0r²g²) on the caps. Haar caps give
(c_N(rg)^{N²-1})^{n_ℓ|Y|}. Divide; b_1(ε°)² ≤ ε_1²/(4N) gives the exponent ≥ |Y|ε_1²/(4N). ∎
(d) The data enter polynomially through the Wilson terms (each link in ≤ 6 plaquettes, |∂s(U_p)| ≤ 1) and through the
kernel (|∂ of (κ/g²)(1 - N^{-1}Re tr V^{-1}M̄)| ≤ κ/g² per contour-mean; log 𝒩 by D4-norm (3)); the indicators do not
depend on D. Derivatives of the ratio of two positive integrals with D-independent indicators are joint cumulants of
bounded variables under two probability measures, as in R4D-iso step 3. ∎
(e) As R4D-iso step 1 (change of variables on int(Y), Haar invariance; the S4' family and the cuts are B_4-symmetric, L1
re-checks). ∎

*Remark.* (c) is uniform in |Y| because the denominator caps are placed around a completion of the given data, not
around 1 in a tree gauge (whose constants grow with the box). It is the frozen form of the Peierls bound that LF-count's
failure mode (RLF-F1) asks about: **the exponent of a frozen cluster of n bad cubes is ≥ n·ε_1²/(4N) (minus a polynomial
g-loss per cube).** RLF-F1 is AVOIDED in the frozen setting.

## 6. Lemma RS (one-step re-seeding of a coarse large field): PROVEN-HERE [S17]

*Setting.* One soft step from level i to level i + 1 (any i; no hypothesis on S_i). A level-(i+1) plaquette
P = (X; μ, ν) with coarse links c_1 = (X, X+e_μ), c_2 = (X+e_μ, X+e_μ+e_ν), c_3 = (X+e_ν, X+e_μ+e_ν), c_4 = (X, X+e_ν);
V_P := V_{c_1}V_{c_2}V_{c_3}^{-1}V_{c_4}^{-1}. U_4 := the union of the four blocks B(X), B(X+e_μ), B(X+e_ν), B(X+e_μ+e_ν);
η := max{||1 - U_p||_op : p a fine plaquette with all vertices in U_4}. S_c the straight transporter between the block
centres; δ_c := max_{σ,y}||T^σ_y - S_c||_op over the S4' contours of c.

*Claim.*
- (R1) **Ribbon bound.** δ_c ≤ A_d(L)η, A_d(L) := (d - 1)L(L - 1)/2 (= 9 for d = 4, L = 3); hence ||M̄_c - S_c|| ≤ A_d(L)η.
- (R2) **Square bound.** ||1 - S_P|| ≤ L²η, S_P := S_{c_1}S_{c_2}S_{c_3}^{-1}S_{c_4}^{-1}; hence
  ||1 - V_P|| ≤ L²η + Σ_{i=1}^4||V_{c_i} - S_{c_i}||.
- (R3) **Dichotomy.** Put η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}. If ||1 - V_P|| ≥ ε_1 then either η ≥ η_1, or η < η_1
  and some c ∈ ∂P has ||V_c - S_c|| ≥ ε_1/8.
- (R4) **Kernel branch, unconditional.** For every U with δ_c(U) ≤ A_d(L)η_1 and g² ≤ κ,
  ∫_{||V_c - S_c|| ≥ ε_1/8} k_c(V_c, U) dV_c ≤ e c_N^{-1}(κ/g²)^{N²-1} e^{-κε_1²/(256Ng²)},
  and for distinct coarse links the bound multiplies (k = Π_ck_c is a product of conditional densities).
- (R5) **Plaquette branch.** On {η ≥ η_1} some plaquette of U_4 has s(U_p) ≥ η_1²/(2N) (inequality (B)).

*Proof.* (R1) Lasso: if a closed loop ℓ is built by successively attaching plaquettes, hol(ℓ) = Π_iw_iU_{p_i}^{±1}w_i^{-1},
and ||ab - 1|| ≤ ||a - 1|| + ||b - 1|| for unitaries gives ||hol(ℓ) - 1|| ≤ Σ_i||U_{p_i} - 1||. Now T^σ_yS_c^{-1} is the holonomy
of the loop γ·leg(y)·(γ + Le_μ)^{-1}·leg(c_X)^{-1}, where γ = s_1…s_m is the order-σ axial path c_X → y and leg(z) the
straight path z → z + Le_μ; S4' pairing (the same σ at both ends) and translation covariance of P^σ make the far-end path
the translate γ + Le_μ. With γ_t := s_1…s_t and ℓ_t := γ_t·leg(z_t)·(γ_t + Le_μ)^{-1}·leg(c_X)^{-1}, inserting
hol(leg(z_{t-1}))^{-1}hol(γ_{t-1})^{-1}hol(γ_{t-1})hol(leg(z_{t-1})) = 1 gives
hol(ℓ_t) = hol(γ_{t-1})R_thol(γ_{t-1})^{-1}·hol(ℓ_{t-1}), R_t := the holonomy of the 1 × L rectangle spanned by s_t and
leg(z_{t-1}); ℓ_0 is trivial. If s_t is along ±μ the rectangle is degenerate (a back-tracking path) and R_t = 1 exactly.
Otherwise R_t is a product of L conjugated plaquettes. The axial path has Σ_{α≠μ}|y_α - (c_X)_α| ≤ (d - 1)(L - 1)/2 steps off
the μ-direction. All rectangles lie in B(X) ∪ B(X + e_μ) ⊂ U_4. So δ_c ≤ A_d(L)η, and M̄_c is a mean of the T^σ_y. (R2) S_P
is the holonomy of the L × L square through the four block centres, a product of L² conjugated plaquettes of U_4; then
telescope V_P against S_P (unitaries). (R3) If η < η_1 and all four ||V_c - S_c|| < ε_1/8, (R2) gives ||1 - V_P|| <
L²η_1 + ε_1/2 ≤ ε_1. (R4) |N^{-1}tr A| ≤ ||A||_op and (B) give 1 - N^{-1}Re tr(V^{-1}M̄) ≥ [1 - N^{-1}Re tr(V^{-1}S)] -
||M̄ - S|| ≥ ||V - S||²_op/(2N) - δ_c. D4-norm (2) gives 𝒩(M̄) ≥ e^{-(κ/g²)(1 - N^{-1}Re tr V_0^{-1}M̄)}e^{-1}c_N(g²/κ)^{N²-1}
with V_0 the maximiser, and 1 - N^{-1}Re tr(V_0^{-1}M̄) ≤ 1 - N^{-1}Re tr(S^{-1}M̄) ≤ ||M̄ - S|| ≤ δ_c (S is a candidate). So
k_c ≤ e c_N^{-1}(κ/g²)^{N²-1}exp(-(κ/g²)[||V_c - S_c||²/(2N) - 2δ_c]); on the event the bracket is ≥ ε_1²/(128N) -
2A_d(L)η_1 ≥ ε_1²/(256N). Haar mass 1. (R5) (B). ∎

*What RS buys (RLF-F4).* A level-(i+1) large field is pointwise reduced to level-i objects, across ONE step: either a
kernel mismatch, priced unconditionally by the normalised soft kernel at the FINER coupling g_i (1/g_i² ≥ 1/g_{i+1}² under
(F)), or a level-i plaquette ≥ η_1, priced by the level-i action (bare level: Wilson positivity; effective levels: the
large-deviation hypothesis (PLD) of §8). This is the soft-kernel form of the one-step regularity of Dimock QED Lemma 23
(NOTES §4 [read]); it is never iterated, so E8*-ob's obstruction does not apply. The pairing of contour orders (S4') is
what makes the far-end path a translate; without it the ribbon bound needs the area between two different axial paths
(c32 A controls this). **RLF-F4 is AVOIDED.**

*Constants (d = 4, L = 3).* A_4 = 9, L² = 9, η_1 = min{ε_1/18, ε_1²/(4608N)}; kernel exponent κε_1²/(256N).

## 7. Theorem R1 (frozen one-level R-operation) and Theorem TS (two scales, frozen exterior): PROVEN-HERE [S17]

### 7.1 Lemma LF-n (cluster-count arithmetic; not counted)
Under (F), with w_i := Ce^{-a/g_i²} and integers n ≥ 1: L^{4(K-i)}w_i^n ≤ C^ne^{-na/g_K²}L^{(4 - naβ_-)(K-i)}. Hence
Σ_{i≤K}L^{4(K-i)}w_i^n ≤ C^ne^{-na/g_K²}/(1 - L^{4-naβ_-}) whenever naβ_- > 4, and (LF-count, the other half) the sum diverges as
K → ∞ when w_i ≥ e^{-a/g_i²} per n-cluster and naβ_+ ≤ 4. *Proof.* Substitute 1/g_i² ≥ 1/g_K² + β_-(K - i)log L. ∎
**Definition.** For 0 < a'' < ε_1²/(4N): **n_* := ⌊4/(a''β_-)⌋**, so (n_* + 1)a''β_- > 4. n_* is g- and K-independent.
Consequence: only clusters of total cube number ≤ n_* need counterterms; LF-count's divergence comes from them alone.

### 7.2 Theorem R1 (one level, frozen background)
*Setting.* Level j, bare form, a frozen full configuration D (all level-j links and the level-(j+1) coarse links) such that
(H-loc) ε_♭(D; Q) ≤ ε_loc for every cube Q, and (H-ch) ε_2 + ε_V ≤ ε_♮ on the box B̂_*(x) of radius R_* := (16n_* + 2)L about
every block centre x, where ε_♮ := min{r_1(R_*), ε_loc/3} (r_1 = GT-lat's chart radius for R_*). Fix a'' ∈ (0, ε_1²/(4N)),
a_1 := ε_1²/(4N) - a'', κ := 4κ_0 + 3 with Theorem CE's [S11] κ_0 = 16 log 12800, κ_1 := κ - κ_0 - 2, and c_0(κ), B, C_K, K_0
those of Theorem CE [S11]. Gas polymers: for a cluster Y, Ŷ := Y + {0, 1}⁴ (cube coordinates).
*Hypothesis on g (G1):* θ := 2(C_rg^{-p_r}e^{-a_1/g²})^{1/16} ≤ C_Kc_0(κ)e^{-2κ_1}, and g ≤ min(1, √κ).

*Claims.*
- (i) **The gas and its logarithm.** Ξ(D) = Σ_{families of polymers with pairwise disjoint X_i}Π_iz_{X_i}, with
  z_X := Σ_{Y: Ŷ=X}r_Y(D). log Ξ(D) = Σ_XΣ_{N≥1}𝓗^{(N)}_X(D), absolutely convergent, where 𝓗^{(N)}_X collects the terms of
  Theorem CE's 𝓗_X (step 3) whose clusters (Y_1, …, Y_n) have Σ|Y_i| = N, and
  |𝓗^{(N)}_X| ≤ e^{-a''N/g²}·2κ_0Bc_0(κ)e^{-κ_0d(X)}.
- (ii) **Taylor form.** For N ≤ n_* and x ∈ X: 𝓗^{(N)}_X(D) = 𝓗^{(N)}_X(1) + Q^{(N)}_{X,x}(Φ_x(D)) + R^{(N)}_{X,x}(D) with
  Q^{(N)}_{X,x} = Σt⟨Φ_a, Φ_b⟩ Ad-invariant and |R^{(N)}_{X,x}| ≤ C_*g^{-6}e^{-a''N/g²}𝔯_x(D), 𝔯_x := 𝔯 on B̂_*(x), C_* = C(n_*, L, N, κ).
- (iii) **Assembly.** With N_j the number of level-j cubes,
  log Ξ(D) = N_jc̄_0(g) + δβ_j·Σ_p s(U_p) + Σ_xℛ_x(D),
  c̄_0(g) := Σ_{N≤n_*}Σ_{X∋0}𝓗^{(N)}_X(1)/|X|,  δβ_j := (2N/L⁴)·(1/6)Σ_{N≤n_*}Σ_{X∋0}tr t^{(N)}_{X,0}/|X|,
  |c̄_0| ≤ C e^{-a''/g²},  |δβ_j| ≤ C_*g^{-6}e^{-a''/g²},  |ℛ_x| ≤ C_*g^{-6}e^{-a''/g²}𝔯_x + 2κ_0Bc_0K_0e^{-a''(n_*+1)/g²}.
  c̄_0 and δβ_j are field-independent numbers depending only on (g, L, N, κ, ε_1, a'', n_*); the sum Σ_p runs over all
  level-j plaquettes.

*Proof.* (i) **Hard core = disjointness.** For cube sets, Ŷ ∩ Ŷ' ≠ ∅ iff some x ∈ Y, x' ∈ Y' have x - x' ∈ {0,1}⁴ - {0,1}⁴ =
{-1, 0, 1}⁴, i.e. iff Y and Y' touch or overlap (torus side ≥ 3). The *-components of B are pairwise *-separated
*-connected sets, and a family of pairwise *-separated *-connected sets is the set of components of its union; so
B ↦ (components) is a bijection onto families with pairwise disjoint Ŷ_i. With (b), Σ_BΠr = Σ_{disjoint}Πz_X. Ŷ is
*-connected (a polymer), |Ŷ| ≤ 16|Y|, d(Ŷ) ≤ 2(|Ŷ| - 1) (a spanning tree of centre-to-centre segments, each ≤ √4 = 2), and
#{Y : Ŷ = X} ≤ 2^{|X|}. **Grading.** Put r'_Y := e^{a''|Y|/g²}r_Y and z'_X := Σ_{Ŷ=X}r'_Y. By (c), |z'_X| ≤
2^{|X|}max(C_rg^{-p_r}e^{-a_1/g²})^{|Y|} ≤ θ^{|X|} (|Y| ≥ |X|/16, base < 1). By (G1) and C_Kc_0(κ) ≤ 1,
θ^{|X|} ≤ C_Kc_0e^{-2κ_1|X|} ≤ C_Kc_0e^{-κ_1d(X)}: z' lies in Theorem CE's polydisc 𝔻 with H_0 = c_0(κ). CE steps 3-4
(PROVEN, L5 [S10]-[S11]; they are statements about P(z) = Σ_{disjoint}Πz on 𝔻 for any z ∈ 𝔻) give log P = Σ_X𝓗_X with
Σ_n(1/n!)Σ|ρ^T|Π|z'_{X_i}| ≤ 2κ_0Bc_0e^{-(κ-3κ_0-3)d(X)} = 2κ_0Bc_0e^{-κ_0d(X)}. Expanding each z_X back into its r_Y and
grouping by N = Σ|Y_i|, every term of 𝓗^{(N)}_X is a term of the majorant times e^{-a''N/g²}. Σ_{X∋□}e^{-κ_0d(X)} ≤ K_0 ((g4)
[S11]) gives absolute convergence. ∎(i)
(ii) 𝓗^{(N)}_X is a finite polynomial in the r_Y (finitely many tuples with Σ|Y_i| = N, ∪Ŷ_i = X) and depends on D only on
B̂_*(x) (|X| ≤ 16N ≤ 16n_*). Each r_Y is gauge-invariant, C^∞, and obeys (d). By the product rule and the majorant of (i),
K_F ≤ C(n_*)(Λ_1/g²)³e^{-a''N/g²}2κ_0Bc_0 on the chart ball, which (H-ch) ⊂ (H-loc) by ε_♭ ≤ 3(ε_2 + ε_V) ≤ ε_loc (||1 - U_p|| ≤
||log U_p||, ||V_c - S_c|| ≤ 2ε_V). Apply GT-lat' (i) with C = all coarse links in B̂_*(x). ∎(ii)
(iii) Write Σ_X𝓗^{(N)}_X = Σ_X(1/|X|)Σ_{x∈X}𝓗^{(N)}_X and use (ii) at each x ∈ X. The c-numbers: by translation invariance
Σ_xΣ_{X∋x}𝓗^{(N)}_X(1)/|X| = N_jc̄_0^{(N)}. The quadratic parts at a fixed x: the family {𝓗^{(N)}_X : X ∋ x, N ≤ n_*} is
permuted by B_4 about x ((e) and covariance of the gas), so by GT-lat' (ii) Σ_{X∋x}Q^{(N)}_{X,x}(Φ_x)/|X| = c̄_1Σ_a||Φ_{x,a}||²_HS,
c̄_1 the stated trace sum (x-independent by translation). **Identification with the Wilson action:** let B_x := the
plaquettes with base point in block x (6L⁴ plaquettes; the B_x partition all plaquettes). For p ∈ B_x,
s(U_p) = ||P̂_p||²_HS/(2N) + O(N²||P̂_p||⁴) (1 - N^{-1}Re tr e^Y = ||Y||²_HS/(2N) + O(Y⁴), R4D-iso step 4), and
|‖P̂_p‖²_HS - ‖Φ_{x,a(p)}‖²_HS| ≤ 2Nε_2ε_3. Summing over B_x (L⁴ base points per plane):
Σ_{p∈B_x}s(U_p) = (L⁴/(2N))Σ_a||Φ_{x,a}||² + O(L⁴(ε_2ε_3 + ε_2³)). So Σ_xc̄_1||Φ_x||² = δβ_jΣ_ps(U_p) + O(c̄_1Σ_x𝔯_x).
Collect R^{(N)}, this identification error, and Σ_{N>n_*} (bounded by (i), summed with K_0) into ℛ_x. The bounds on c̄_0 and
δβ_j follow from (i)-(ii) (N ≥ 1). ∎

*Reading.* Under (H-loc)+(H-ch), the whole level-j large-field gas is exactly e^{c-number}·e^{δβ_jΣs}·e^{Σℛ}: every
cluster of ≤ n_* bad cubes is "returned" (its relevant and marginal content becomes a vacuum constant and ONE uniform
coupling shift), and what is left is a local remainder of irrelevant order 𝔯 plus an unrenormalised tail of order
e^{-a''(n_*+1)/g²} per cube, which Lemma LF-n sums. **RLF-F2 is AVOIDED** (frozen): the counterterms are
field-independent, and B_4-averaging over shapes plus the base-point partition B_x reduce all marginal parts to one
coupling shift of the uniform Wilson action.

### 7.3 Theorem TS (two scales; the level-k field may be large; frozen exterior)
*Setting.* Levels j < k. Δ := one level-(k-1) cube (one level-k site; so Δ lies in a level-k cell that may be large-field
at level k). A frozen multi-level background: for each inner level i ∈ [j, k-1], a full configuration D_i (level-i links
and level-(i+1) coarse links, the latter = the level-(i+1) links of D_{i+1}). For i = k-1-n (n ≥ 0) and every level-i cube
Q meeting Δ, let ε_•(Q) be R4D-iso/GT-lat's parameters of D_i on Q's box, and assume **BG-b relative to level k-1**:
  (b1) ε_2(Q) + ε_V(Q) ≤ M_2σ_n², σ_n := L^{-n}, with M_2 ≤ ε_TS := min{ε_loc/3, ε_♮};
  (b2) Σ_nō_n ≤ M_3, ō_n := σ_n^{-2}L^{-4n}Σ_{Q∈𝒬_n(Δ)}(ε_3 + ε_V)(Q).
**No hypothesis is made on the level-k field** (it may have ||1 - U_k(P)|| ≥ ε_1 at Δ). The inner integrands are of bare
form at each inner level (frozen model; effective levels: §8). (G1) holds at every inner coupling g_i.

*Claims.*
- (TS-a) **Fixed counterterms.** At each inner level i the large-field gas of Δ's level-i cubes satisfies Theorem R1 with
  the constants c̄_0(g_i), δβ_i of 7.2, which do not depend on the level-k field or on any datum.
- (TS-b) **Inner remainders, uniformly in j, k.** Σ_{i=j}^{k-1}Σ_{x∈𝒬_i(Δ)}|ℛ_x| ≤ C_TS[w_{k-1}(3M_2M_3 + M_2³/(1 - L^{-2}))
  + e^{-a''(n_*+1)/g_{k-1}²}/(1 - L^{4-(n_*+1)a''β_-})], with w_i := C_*g_i^{-6}e^{-a''/g_i²} and C_TS = C(n_*, L, N, κ).
- (TS-c) **Outer suppression, one step.** If Δ's level-k cell has a plaquette P with ||1 - U_k(P)|| ≥ ε_1, then by Lemma RS
  applied to the step k-1 → k: either some level-(k-1) plaquette in U_4(P) has s ≥ η_1²/(2N) (cost e^{-η_1²/(2Ng_{k-1}²)} in
  the level-(k-1) Wilson weight in the bare model), or a mismatch event of conditional probability
  ≤ e c_N^{-1}(κ/g_{k-1}²)^{N²-1}e^{-κε_1²/(256Ng_{k-1}²)}, uniformly in everything (Lemma RS (R4)).
- (TS-d) Both suppressions are kept in product form: the inner levels contribute exp(N-weighted c-numbers + coupling
  shifts + (TS-b)) and the outer large field contributes the factor of (TS-c); neither needs the other.

*Proof.* (TS-a) Theorem R1 at level i needs (H-loc) and (H-ch) for D_i near Δ; both follow from (b1) with σ_n ≤ 1 and
M_2 ≤ ε_TS. (TS-b) **Box merging.** For the box B̂_*(x), ε_2(B̂_*) = max_{Q⊂B̂_*}ε_2(Q) (conjugation does not change
||log U_p||), ε_V(B̂_*) = max ε_V(Q), and ε_3(B̂_*) ≤ C(R_*)max_{Q⊂B̂_*}(ε_3(Q) + ε_2(Q)²): compare the base plaquette of
B̂_* with those of a chain of ≤ 2R_*/L + 1 overlapping cube boxes; consecutive base plaquettes differ by ≤ ε_3 + Cε_2² after
transport, and changing the transport path conjugates by a holonomy h with ||h - 1|| ≤ (area)ε_2, which moves a
plaquette log of size ε_2 by ≤ 2||h - 1||ε_2. Then with ε_3 ≤ 2ε_2 and (b1), every product in 𝔯_x is bounded by
C(n_*)Σ_{Q⊂B̂_*(x)}[3M_2σ_n²(ε_3 + ε_V)(Q) + M_2³σ_n⁶] (max ≤ sum). Each Q lies in ≤ (2R_*/L + 1)⁴ boxes. Sum over
x ∈ 𝒬_n(Δ) and use L^{4n}σ_n⁴ = 1 (the d = 4 marginality, as in BG-sum): the level-n total is ≤ C[3M_2ō_n + M_2³σ_n²]·w_i,
with w_i ≤ w_{k-1} (g_i ≤ g_{k-1}). Sum over n with (b2). The tail: |𝒬_n(Δ)| = L^{4n} cubes, each ≤ 2κ_0Bc_0K_0
e^{-a''(n_*+1)/g_{k-1-n}²}; Lemma LF-n. (TS-c) Lemma RS (R3)-(R5) at the step k-1 → k; the kernel branch is unconditional
(R4); the plaquette branch is a pointwise lower bound on the level-(k-1) Wilson term. (TS-d) The inner statements use
only the inner data; the outer one uses only the step k-1 → k. ∎

### 7.4 Outcome against RTARGET §7 and §2's failure modes (frozen exterior)
- **W2-F1 (no smooth background inside a multi-scale large region): CIRCUMVENTED, with a named hypothesis.** The inner
  renormalisation at level i needs only (H-loc)+(H-ch), level-i statements about level-i data; the summation over inner
  levels needs BG-b relative to the LAST level at which the region is small-field (k - 1), never the large level-k field.
  The Taylor parameter is ε_•(level-i data), not a smooth family. Hypothesis: BG-b at level k-1 (= node N2/BG-reg).
- **W2-F2 (inner vacuum depends on the outer field): AVOIDED by construction.** c̄_0(g_i), δβ_i are defined at the trivial
  datum.
- **W2-F3 (history combinatorics): AVOIDED in the frozen setting.** Per level, the sum over large-field sets is a hard-core
  polymer gas, exponentiated by CE steps 3-4; clusters with N ≤ n_* carry counterterms, N > n_* are summable (LF-n); inner
  levels decouple from the outer one (TS-d). Across levels in the fluctuating integral it is the bookkeeping (HIST) of §8.
- **RTARGET §7 form.** The "alternatively" form is met in the frozen setting, with the correction that renormalisation is
  level by level relative to the next coarser small-field level; "both suppressions kept" holds in the product form
  (TS-d) rather than as e^{-a/g_j²}e^{-a/g_{j+1}²} per inner cube (inner cubes are renormalised and need no outer factor).
- RLF-F1 AVOIDED (Proposition CL (c)); RLF-F2 AVOIDED (R1 (iii)); RLF-F3 AVOIDED (TS-b uses no level-k regularity);
  RLF-F4 AVOIDED (Lemma RS).
- **Scope (not success items, as pre-stated):** frozen exterior (the sea is a fixed configuration); bare-form inner
  integrands; the smallness (H-loc) holds everywhere near Δ (in the real integral it fails with density e^{-c/g²}: §8).

## 8. Target 3: the inductive step over scales, sea fluctuating

### 8.1 The inductive representation (I_k)
**(I_k).** There are a field-independent number 𝒱_k, a coupling g̃_k (the flow (F) shifted by Σ_{i<k}δβ_i), and a
decomposition
  e^{-S_k(U)} = e^{𝒱_k}·Σ_{𝔥∈ℋ_k}1_𝔥(U)·exp(-(1/g̃_k²)Σ_{p⊂Λ(𝔥)}s(U_p) + Σ_{X⊂Λ(𝔥)}E_k(X; U))·ℒ_𝔥(U),
where 𝔥 ranges over histories (the unreturned large-field regions created at levels < k, nested as in Dimock II
(145)-(148)), Λ(𝔥) is the level-k small-field region, E_k are small-field polymers in the norm of the small-field
package (irrelevant parts contracted; they include the returned remainders ℛ of earlier levels), and ℒ_𝔥 is the
large-field factor, |ℒ_𝔥| ≤ Π_{i<k}Π_{Y unreturned at i}(C_ℓe^{-a''/g_i²})^{|Y|}·e^{B_0|∂Ω(𝔥)|} (boundary terms O(1) per
boundary cube, as Dimock II (218) [read]).
(I_0) holds with 𝒱_0 = 0, ℋ_0 = {∅}, E_0 = 0, g̃_0 = g_0.

### 8.2 Named hypotheses (each a precise statement; none is proven here)
- **(F)** the flow, §0 (node A5 / L4a-flow).
- **(SF)_k, the small-field package at level k** = (DF1)-(DF4) of PROOF L5 [S9] for the level-k sea with the action of
  (I_k), plus the L4a-form contraction of irrelevant polymers: nodes N2, N4, N5, N6 (A1-A4). It includes **(H-pos)_k**:
  Σ_{X∋Q}sup|E_k(X)| ≤ E_0 per cube and the C³ bounds of E_k in the data, so that Proposition CL and Theorem R1 hold at
  level k with C_r → C_re^{2E_0}, Λ_1 → Λ_1 + E_0 (the proofs use only positivity of the Wilson part, a per-cube bounded
  perturbation, and C³ bounds; ARGUED, not written).
- **(PLD)_k, Peierls large deviations of the level-k sea.** For the all-cut level-k measure of (I_k) on Λ(𝔥): (i) for any
  finite set A of plaquettes with pairwise disjoint 1-neighbourhoods, P(||1 - U_p|| ≥ η_1 ∀p ∈ A) ≤ (C e^{-a_η/g_k²})^{|A|};
  (ii) for any finite set 𝒜 of cubes, P(ε_♭(U; Q) > ε_loc ∀Q ∈ 𝒜) ≤ (C e^{-a_♭/g_k²})^{|𝒜|}; a_η, a_♭ > 0 g-independent,
  uniformly in |A|, |𝒜|, T. For |A| = 1 (resp. |𝒜| = 1) this is W1-LD-cond's (LD) [proven ⇐ (DF1-3')]; the multi-point
  form needs (DF3') for general linear functionals with ℓ¹ control (N9 for general c) and a union bound over disjoint
  supports.
- **(W1-ret)_k, returned clusters in the fluctuating sea.** Let 𝔊 := the gas of §7 split as r_Y = r_Y^s + r_Y^ℓ with
  r_Y^s := r_Y·1{ε_♭(U; Q) ≤ ε_loc for Q ∈ N(Y), and (H-ch) on the boxes of Y}. Then
  log⟨exp(Σ_X[𝓗_X(z^s) - 𝓗_X(z^s)(1)])·(the r^ℓ-part)⟩_cut is a convergent polymer expansion in the coarse field V
  with activities local up to e^{-κ_d d} tails, C³ in V, gauge- and B_4-covariant, and with the r^ℓ-polymers carrying
  (C e^{-min(a'', a_♭)/g_k²})^{|cubes|}. This is the multi-defect (strong) form of W1-loc, for clusters; for one cube it is
  W1-loc's (LD) + (cl) (PROVEN ⇐ (DF) for (LD); (cl) ARGUED [S9]).
- **(HIST)_k, history bookkeeping for the soft kernel.** The analogue of Dimock II Theorem 3.1 (pp. 29-31 [read]): after
  the step, the unreturned regions of level k join the history (Ω_{k+1} ⊂ Ω_k for the small-field regions), the polymers
  that cross into new large regions become boundary terms bounded by e^{B_0} per boundary cube, the level-k variables
  inside unreturned regions are integrated with the crude bound ∫K_k dV = 1 (exact normalisation of the soft kernel), and
  the characteristic functions are localised (Dimock Rome p.57: "a difficult technical problem" [read-skim]).

### 8.3 Proposition RLF-step: (I_k) + (F) + (SF)_k + (PLD)_k + (W1-ret)_k + (HIST)_k ⇒ (I_{k+1}), with
𝒱_{k+1} = 𝒱_k + 𝒱^{sf}_k + N_kc̄_0^{sea}(g_k), 1/g̃_{k+1}² = flow(1/g̃_k²) + δβ_k^{sea}, and the same constants
(C_ℓ, B_0, E_0, a'', n_*) at every level. **Status: CONDITIONAL; the step below is a proof modulo the named hypotheses,
with every new estimate it uses proven in §4-§7 or below.**
1. *Exact.* Insert Π_Q(χ_Q + ζ_Q) on Λ(𝔥); Proposition CL (a)-(b) (with (H-pos)) gives Z-integrand/Z_∅-integrand = ⟨Ξ⟩_cut
   with the frozen gas Ξ, pointwise in the sea sample.
2. *Frozen R-step.* On the locally small part r^s, Theorem R1 (pointwise in the sample) gives the c-numbers, the coupling
   shift and the remainders ℛ, with the constants of §7 (PROVEN, under (H-pos)).
3. *Sea average.* (W1-ret)_k turns ⟨·⟩_cut of 2 into the sea-averaged form: c̄_0^{sea}(g_k) := the sea-averaged c-number
   at trivial coarse field (field-independent; it differs from c̄_0 by sea corrections of the same order), δβ_k^{sea}
   likewise, and returned remainders that are irrelevant small-field polymers at level k + 1 (fed into E_{k+1}).
4. *Unreturned clusters.* The r^ℓ-part and the N > n_* tail form new large-field regions at level k with weight
   ≤ (C_ℓe^{-a''/g_k²})^{|cubes|} ((PLD)_k (ii) + Proposition CL (c) for the frozen factor + W1-size' with the plug for the
   collar event).
5. *Small-field step.* (SF)_k integrates the level-k sea on Λ(𝔥) minus the new regions with the shifted action, producing
   E_{k+1}, 𝒱^{sf}_k and the flow.
6. *New level-(k+1) large fields.* At the next step, a bad level-(k+1) plaquette is reduced by Lemma RS (PROVEN) to a
   level-k kernel mismatch (unconditional, (R4)) or a level-k plaquette ≥ η_1 ((PLD)_k (i)).
7. *Bookkeeping.* (HIST)_k.

### 8.4 What is proven unconditionally in the induction (the level summations; PROVEN-HERE as arithmetic, not counted)
- **(P1) Unreturned clusters are summable.** Per unit volume, Σ_kN_kΣ_{n>n_*}(80e)^n(C_ℓe^{-a''/g_k²})^n ≤
  C|T|e^{-(n_*+1)a''/g_K²} for g_K ≤ g_0, by Lemma LF-n and #{*-connected sets ∋ □ of size n} ≤ 80^{2(n-1)} ((g3)). The same
  holds for the RS-generated level-(k+1) large fields: their per-cube factor is e^{-a_RS/g_k²} with
  a_RS := min{a_η, κε_1²/(256N)} at the FINER coupling, and clusters of them with n > 4/(a_RSβ_-) are summable.
- **(P2) Coupling-shift budget.** Σ_k|δβ_k| ≤ C_*Σ_kg_k^{-6}e^{-a''/g_k²} ≤ C'e^{-a'''/g_K²}/(1 - L^{-a'''β_-}) (any a''' < a''),
  uniformly in K; and |δβ_k| ≤ g_k⁶ for g_k ≤ g_0. So the returned marginal parts do not disturb the AF flow at the order
  that L4a-flow controls (the one-loop and two-loop terms are O(1), O(g_k²) in 1/g² units).
- **(P3) Vacuum.** 𝒱_K - Σ_k𝒱^{sf}_k = Σ_kN_kc̄_0^{sea}(g_k), a field-independent number, ≥ 0 at leading order and divergent
  as K → ∞ exactly when LF-count says (it carries all clusters N ≤ n_*); it cancels in normalised expectations and in
  Z_K/Z_K^ref with matching constants. This is (RLF-1).
- **(P4) Consistency of the nesting.** The counterterms extracted at level k are defined at the trivial datum and are never
  revised at later levels: a level-m unreturned region (m > k) containing returned level-k clusters keeps their
  c-numbers (they are part of the global constant) and carries their remainders as boundary/inside polymers bounded by
  e^{B_0} per cube, which the level-m suppression (C_ℓe^{-a''/g_m²})^{n}, n > n_* or collar-bad, absorbs ((P1) with
  C_ℓ → C_ℓe^{B_0}). No re-renormalisation of earlier constants is needed (W2-F2 at the inductive level).
- **(P5) Composition with Theorem CE at level K.** Unreturned polymers X (in level-K cubes) have activity
  ≤ (C_ℓe^{-a''/g_K²})^{|X|}. Put H_0 := C_ℓe^{-a''/(2g_K²)} and κ := a''/(8g_K²). If C_ℓe^{-a''/(2g_K²)} ≤ 1 then
  (C_ℓe^{-a''/g_K²})^{|X|} ≤ H_0e^{-(a''/(2g_K²))|X|} ≤ H_0e^{-κd(X)} (d(X) ≤ 2|X|, with room to spare). Theorem CE [S11]
  needs κ > 3κ_0 + 3, i.e. **g_K² < a''/(8(3κ_0 + 3)) ≈ a''/3654**, and H_0 ≤ c_0(κ); since c_0(κ) ≥ c(κ_0)e^{-2κ} =
  c(κ_0)e^{-a''/(4g_K²)} (each of its three entries is ≥ a κ_0-dependent constant times e^{-2κ}), the second condition holds
  once C_ℓe^{-a''/(4g_K²)} ≤ c(κ_0). Both are explicit smallness conditions on g_K. The returned remainders and the
  small-field polymers need N6's rate (κ > 457 in M-units, M ≳ 1.2·10⁴), which is node A4.

### 8.5 How far the induction goes
- **Closed (in the frozen setting, every level):** the R-operation of one level as an exact rewriting (§3, CL (a)-(b)),
  its estimates (CL (c)-(e), R1), its two-scale form (TS), the one-step pricing of coarse large fields (RS), and all
  level summations (P1)-(P5).
- **Conditional (sea fluctuating):** Proposition RLF-step, modulo (SF), (PLD), (W1-ret), (HIST), (F).
- **Hence:** RLF ⇐ (F) + (SF)_k + (PLD)_k + (W1-ret)_k + (HIST)_k for all k (uniform constants), by induction on k with
  (I_0) and (P1)-(P5); (RLF-4) then follows from (I_K), (P1), (P5) and Theorem CE at level K. This is a reduction of the
  4D large-field R-operation (node B-W2, weighted P×2) to the small-field package plus three named large-field
  statements, of which two are multi-defect forms of statements already proven for one defect.

## 9. Check c32 (criteria first: checks/c32_criteria.md; script checks/c32_rlarge.py; record checks/c32_time.txt)
**All four parts PASS, first and only runs** (laptop, load ≤ 2.5, ≥ 36% free, peak RSS ≤ 41 MB, ≤ 4 s each).
- **A (Lemma RS, SU(2), d = 4, L = 3):** A1-A4 hold on 15 random configurations (t = 0.01-0.2) and three sharp ones. Random
  fields use the constants loosely (max ribbon ratio 1.99 of the proven 9; square 0.80 of 9). **A5 sharpness:** a constant
  abelian flux in the planes (α, 0) gives ribbon ratio 8.99997 and a flux in (0, 1) gives square ratio 8.99997, so
  A_4(3) = 9 and L² = 9 are attained (the area counts are exact, not overcounts). **A6:** with additional flux in the planes
  (1,2), (1,3), (2,3), UNPAIRED contour orders reach 14.9999 > 9 while the S4'-paired ones stay at 9.0000: the S4' pairing
  is load-bearing for the ribbon constant.
- **B (hard core):** B1 fattening ⇔ touching on 4000 pairs in (Z/6)⁴ (1961 touching), B2 components ↔ disjoint fattened
  families (2000 + 2000 instances), B3 the t^N coefficients of log Ξ_T are exactly extensive (c_N/T equal for T = 12, 14, 16 to
  ≤ 2e-12, N ≤ 4): the graded logarithm is local, as Theorem R1 (i) uses.
- **C (arithmetic, one-loop rate [inference]):** n_* = 382 (SU(2), ε_1 = 0.5), 95 (ε_1 = 1), 23 (ε_1 = 2); SU(3): 255, 63, 15.
  So **for every admissible ε_1 (≤ 2) the R-operation is needed (n_* ≥ 15), and n_* is finite and g-independent.** RS at
  N = 2, κ = 1, ε_1 = 0.5: η_1 = 2.7·10⁻⁵, plaquette exponent η_1²/4 = 1.8·10⁻¹⁰, kernel exponent 4.9·10⁻⁴; CL: ε_loc = 3.5·10⁻³.
  These are g-independent but very small (crude constants, recorded as such).
- **D (GT-lat' (ii)):** the full B_4 average of 20 random t is (tr t/6)·1 to 1e-12; the rotation-only average is
  non-scalar in 20/20 (reflections needed, as in c19 P1).

## 10. Outcomes against the pre-stated targets (§1-§2)
- **Target 1 (RLF stated): MET.** §1 states RLF with all quantifiers in the soft setting; §8.4 (P3), (P5) and §7 give its
  composition with LF-count (the divergence is exactly the vacuum c-number of clusters N ≤ n_*), with R4D-iso (|Y| = 1,
  frozen), and with Theorem CE (explicit condition g_K² < a''/(8(3κ_0 + 3)) for the unreturned polymers). One correction to
  §1 found in the derivation: (RLF-2)'s per-cell summation of the returned remainders is not a separate large-field
  estimate; once returned they are irrelevant small-field polymers, and their summation is the small-field package's
  contraction (node A4). BG-sum/TS-b is its frozen-background shadow.
- **Target 2 (two-scale, frozen exterior): MET as pre-stated, in the frozen setting** (Proposition CL, Theorem R1, Theorem
  TS, Lemma RS, Lemma GT-lat'). Constants are stated (§5-§7, c32 C). W2-F1 CIRCUMVENTED with BG-b at the last small-field
  level; W2-F2 AVOIDED; W2-F3 AVOIDED (frozen); RLF-F1-F4 AVOIDED. Not success items as pre-stated: frozen sea, bare-form
  integrands, local smallness everywhere near Δ.
- **Target 3 (inductive step): PARTIAL, as pre-stated allowed.** Proposition RLF-step is a proof of (I_k) ⇒ (I_{k+1})
  modulo five named hypotheses; the level summations (P1)-(P5) are proven unconditionally; RLF ⇐ the hypotheses for all k
  by induction (§8.5).

## 11. Exact remaining walls (weights: P = paper-scale, s = session-scale)
1. **(SF)_k, the small-field package at every level** (N2 BG-reg, N4, N5, N6; L4a-form with the contraction of irrelevant
   polymers; it contains (H-pos)): unchanged, [P×3-4] (A1-A4 of the critical path). The R-operation adds to it only the
   requirement that returned remainders (C³ in the data, of order 𝔯) be admissible polymer activities.
2. **(PLD)_k, Peierls large deviations of the sea** (§8.2): multi-point forms of W1-LD-cond's (LD). Inputs: (DF3') for
   general linear functionals with ℓ¹ control (N9 generalised), W1-size' with a product plug over disjoint defects
   (proven for one defect). [s, given (SF)].
3. **(W1-ret)_k, returned clusters in the fluctuating sea** (§8.2): the strong (multi-defect) W1 for clusters of total size
   ≤ n_* plus the collar split. Inputs: (DF4), Theorem CE with the frozen activities as single-block factors (Proposition
   CL supplies their size and derivatives), the corridor localisation of W1-cl (argued [S9]). [s to P].
4. **(HIST)_k, history bookkeeping for the soft kernel** (§8.2): the analogue of Dimock II Theorem 3.1 (nested regions,
   boundary terms, localisation of the characteristic functions). [P: the size of Dimock II; CMP 122 II's "localization,
   exponentiation" by its title].
5. **(F), the flow** (A5) and the compatibility |δβ_k| ≤ g_k⁶ (proven, P2). [P].
6. **(H-pos) for Proposition CL and Theorem R1 at effective levels:** ARGUED (bounded per-cube perturbation), not written. [s].
7. **Constants.** η_1 and ε_loc are tiny (c32 C). η_1 comes from the linear δ_c term in RS (R4); for near-unitary M̄ the
   deviation is quadratic, which would improve η_1 to O(ε_1/L²). Not needed for correctness. [s, optional].
Not a wall: W3 (the main path has no constraint fibres; RLF's kernel branch is unconditional because the soft kernel is a
normalised conditional density).

## 12. Status and tally contribution
- PROVEN-HERE [S17] (unreviewed), counted: **Lemma GT-lat'** (§4); **Proposition CL** (§5, with the Fubini identity and the
  per-cube-uniform size bound); **Theorem TS** (§7, counted with Theorem R1 and the box-merging step); **Lemma RS** (§6).
  Not counted: Lemma LF-n and (P1)-(P5) (arithmetic); §3 (definition); the c32 instances.
- CONDITIONAL: Proposition RLF-step (§8.3). ARGUED: (H-pos) extension of CL/R1 to effective levels.
- OPEN: RLF (§1) itself, now reduced to the walls of §11 (inside L5; no new top-level item).
- L5 stays IMPORTED-NOT-YET-REVERIFIED (CMP 122 not read); RLF is the re-derivation target that would replace it.
- Tally: 64/2/7/24 + 1 → **68 / 2 / 7 / 24 + 1 comparison-branch.**

