lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T06:30Z

# CR, second round: closing the gaps of gates/cr-gate.md for library/cr-claude.md

Started 2026-11-06T18:30Z at commit e83525781, branch claude/ym4d-hard-route, FINISH row 398. Research text. Proved by Claude (Opus 5.5, max effort), not yet checked by the other model. No status. No computer-assisted step; no numerics were run.

**Credit.** The statement CR, the inside proof, the refined-minimiser identity and the inputs T1, AV, R, CUR, AX, COMP and (j) are from Ethan Sussman and Levent Alpoge's complete account (with Claude and Codex as authors of their text), commit 31a47c543775, cited as CA-I with raw-TeX line numbers (fetched to a scratch folder for this lane). The averaging, minimiser and response theory is Tadeusz Balaban's; CMP 98, 102 and 119 are read here from the local copies in `~/ym4d-papers` (printed pages rendered from the PDFs). The one-level ladder, Lemmas 1-9 and the numbering below are from `library/cr-claude.md` (Claude). The defects closed here are those of `gates/cr-gate.md` (Codex).

## 1. Scope and duplicate check

**Item.** FINISH row 398: close the gaps of `gates/cr-gate.md` for `library/cr-claude.md`. (1) The uniform circuit bound n_P of Lemma 6. (2) The identifications R and ROW, and the conditions SRC and SEP, for every outside consumer class of CA-I `4.12:prop-reblocking-outside` (CA-I 45085-45106, status "Proof outstanding"). Also apply the gate's written repairs (its sections 2-4). `cr-claude.md` is not edited.

**Duplicate check (rule 0a).** `library/open-core.md` lists CR as a core statement (lines 80-99) owned by this lane family. `library/l17c.md` has no entry for n_P, ROW, SRC or SEP. The FINISH rows that touch CR are 310 (`rb`), 322 (`open-core`), 348 (`cr-claude`), 353 (`crca`), 396 (`cr-gate`) and this row. None of them attacks n_P, ROW, R coverage, SRC or SEP. So no other row covers these lemmas.

**Outline check (rule 9).** CA-I 42980-42984 defines a plaquette of 𝕃(𝔅) as "an elementary closed circuit of 𝕃(𝔅)", with ∂D(P) "the ordered product of D along it". The account gives no other definition. The phrase occurs once in CA-I. Plaquettes of 𝕃(𝔅) are used only in (e) (CA-I 43046-43052), in T1's data condition (CA-I 43115-43119) and in the inside proof (CA-I 44236-44244). The account does not prove a bound on their length.

## 2. The circuit bound n_P (gate §3, Lemma 6): closed

### 2.1 What Balaban's plaquettes are

- **CMP 98, p. 18.** "Plaquettes are oriented elementary squares of the lattice Ω ... The above definitions of bonds and plaquettes may be applied to an arbitrary lattice, e.g., to Ω^(j)." So on a lattice of level-j blocks, a plaquette is an elementary square: four bonds.
- **CMP 102, pp. 277-278.** The determining set is 𝔅_k = ∪_j Λ_j, with Λ_j = Ω_j^(j) \ Ω_(j+1)^(j). Sets of plaquettes are "sets of plaquettes with at least one corner belonging to Ω_j". The data condition (7) is |(∂V)(p') − 1| < ε_1 for p' ∈ 𝔅_k. Balaban explains: p' is an elementary square of the level-j lattice. If all four corners lie in Λ_j, then (∂V)(p') = V(∂p'). If a bond ⟨y,z⟩ of p' is not in Λ_j, then y, z ∈ Λ_(j−1), and that factor is replaced by a value V̄(y,z) built from the finer data. So every plaquette that T1's source reads has exactly four factors.
- **CMP 119 (2.2), (2.10)-(2.11), p. 255-256.** The determining set B = ∪_j Γ_j "is meant for sets of points, bonds and plaquettes"; M_B(U) = M^j(U) on Γ_j. Again the plaquettes are elementary squares of the homogeneous level-j lattices.

The account replaces Balaban's nested lattices by one partition 𝔅 into blocks, with a bond for each pair of adjacent blocks (CA-I 42966-42971). Its plaquettes are "elementary closed circuits" of that graph, with ∂D(P) the ordered product along the circuit. So the account's plaquettes are circuits of 𝕃(𝔅). The definition does not say which circuits. The next lemma shows that the literal graph reading (every simple cycle) is not available.

**Lemma 2.1 (the literal reading contradicts (e)).** Let a domain X be a ring of N ≥ 5 blocks B_0, …, B_(N−1) of one level, with B_i adjacent to B_(i±1) (indices mod N) and to no other block. Example: the perimeter of an r × r square of blocks in two coordinates, r ≥ 3, one block thick in the others. Suppose the cycle P = (z_0, z_1, …, z_(N−1), z_0) is a plaquette of 𝕃(𝔅) for 𝔅 = {B_i}. Then (c) and (e) of CA-I 43018-43052 cannot both hold.

*Proof.* Let B_0 = B_(N−1) + ℓe_μ. Fix g ∈ G with g ≠ 1. Let U = g on the bonds ⟨x, x+ηe_μ⟩ with x ∈ B_(N−1) and x+ηe_μ ∈ B_0, and U = 1 on every other bond of X. Let 𝔭 be a fine plaquette of X (four corners in X) that contains such a bond ⟨x, x+ηe_μ⟩. Let y = x + sηe_ν, ν ≠ μ, be its third corner. If y ∈ B_(N−1), then y + ηe_μ ∈ B_0, because equal adjacent blocks share a full face. Then 𝔭 contains two such bonds with opposite orientations, and its two ν-bonds carry 1, so ∂U(𝔭) = 1. If y ∉ B_(N−1), then y lies in the ν-neighbour B_(N−2) of B_(N−1), and y + ηe_μ lies in the ν-neighbour B_1 of B_0. Then B_(N−2) and B_1 are adjacent, which is false for N ≥ 5. Plaquettes without such a bond carry 1 on all four bonds. So ∂U(𝔭) = 1 for every plaquette 𝔭 of X. For i ≠ N−1 the carrier B_i ∪ B_(i+1) contains no bond from B_(N−1) to B_0. By locality and normalisation, M(U)(⟨z_i,z_(i+1)⟩) = M(1)(⟨z_i,z_(i+1)⟩) = 1. On the carrier B_(N−1) ∪ B_0, U equals 1^σ with σ = 1 on B_(N−1) and σ = g^(−1) on B_0. Extend σ by 1 to X. Locality and covariance give M(U)(⟨z_(N−1),z_0⟩) = M(1^σ)(⟨z_(N−1),z_0⟩) = σ(z_(N−1))σ(z_0)^(−1) = g. Hence ∂M(U)(P) = g and |∂M(U)(P) − 1| > 0. The hypothesis of (e) holds, since sup|∂U − 1| = 0. The right side of (e) is 0. □

So under any reading in which the account's input (e) holds, a plaquette of 𝕃(𝔅) is not an arbitrary simple cycle. This matters for CR: the read domains of K2 and K4 include collars around large-field regions. These collars are not simply connected. Under the literal reading, T1's data condition would require control of the holonomy of M(Ū) around such a collar, and the inside argument for (a) (CA-I 44236-44244, which uses (e)) would fail as well.

### 2.2 The identification and the bound

**Reading (EC).** Every plaquette P of 𝕃(𝔅) is a closed circuit of 𝕃(𝔅) through pairwise distinct blocks whose closed cubes contain a common point of ℝ^d. (EC) is a containment. It does not say that every such circuit is a plaquette, so it adds nothing to the class on which (e) and T1's condition are imposed.

Support. (i) Balaban's elementary square of a level-j lattice is the circuit of the four level-j blocks around a common (d−2)-face, so it has this property. (ii) At an interface between levels m and m+1, the circuits around a common (d−2)-face piece have three or four blocks, and they have it too. (iii) T1's source condition, CMP 102 (7), reads only elementary squares, each with four factors (§2.1). (iv) By Lemma 2.1, a circuit around a hole is not a plaquette under any reading in which (e) holds. The natural narrow reading (the circuits around a (d−2)-face piece, three or four rows) satisfies (EC).

Blocks are identified with closed cubes. Level-m cubes are anchored at the origin and have side ℓ_m ∈ ηℤ, so their corners lie in ηℤ^d.

**Lemma 2.2 (n_P = 2^d).** Let Q_1, …, Q_r be distinct closed blocks of a determining set that contain a common point x. Then r ≤ 2^d. Hence every plaquette under (EC) has at most 2^d rows, uniformly in k, X, 𝔅, the level function and the tower.

*Proof.* The domain is finite, so r is finite. For a sign vector s ∈ {±1}^d and t > 0, let O_s(t) := {y : 0 < s_μ(y_μ − x_μ) < t for all μ}. This is a nonempty open set. Let Q_i = ∏_μ [a_μ, a_μ + ℓ] with x ∈ Q_i. For each μ, x_μ < a_μ + ℓ or x_μ > a_μ, since ℓ > 0. Put s(i)_μ = +1 in the first case and −1 otherwise. The gap a_μ + ℓ − x_μ, resp. x_μ − a_μ, is then positive. Choose t > 0 below all these gaps, for all μ and all i. Then O_(s(i))(t) ⊂ Q_i. An open set inside a closed cube lies in its interior. Distinct blocks of a partition are distinct cubes of the nested L-adic families, so their interiors are disjoint. Hence i ↦ s(i) is injective, and r ≤ 2^d. □

So for d = 4, n_P = 16, with no dependence on L.

### 2.3 Repaired Lemma 6

**Lemma 6′ (replaces Lemma 6 of cr-claude.md).** Assume (EC). Put
$$\varepsilon_1':=(2+2^dC_{\rm RD}C_FL^2)\,\alpha_k\ell_q^2$$
and assume ε_1′ ≤ a_1 and B_3ε_1′ ≤ ε_0. Then U^(q+1) = U(𝔅^(q), D_W)^τ for a gauge τ.

*Proof.* The proof of cr-claude Lemma 6 applies word for word, with n_P replaced by 2^d. The only change is in the data condition. Let P be a plaquette of 𝕃(𝔅^(q)) with base point z_0. By Lemma 5, D_W = (e^{iB}D_0)^v. The ordered product around P gives ∂D_W(P) = v(z_0) ∂(e^{iB}D_0)(P) v(z_0)^{−1}. For unitary factors, |∏_i e^{iB_i}g_i − ∏_i g_i| ≤ Σ_i |e^{iB_i} − 1| ≤ Σ_i |B_i|. P has at most 2^d rows by Lemma 2.2. Hence |∂D_W(P) − 1| ≤ |∂D_0(P) − 1| + 2^d sup|B| ≤ 2α_kℓ_q^2 + 2^dC_RD F ℓ_(q+1)^2 = ε_1′. Here the first bound is (e) with SRC, and ℓ(P) ≤ ℓ_q because every block of 𝔅^(q) has level at most q. □

In the ceilings (8.1), replace n_P by 2^d. The gate's conditional verdict on the rest of Lemma 6 (COMP gives the inclusion of the constraint manifolds; criticality restricts; the refinement keeps T1's threshold) is unchanged. **Status of n_P: discharged under the reading (EC).** (EC) is a reading of CA-I 42982, supported by CMP 98 p. 18, CMP 102 p. 278 and Lemma 2.1. It is not a hypothesis on the consumers.

## 3. Geometry of the ladder sets

Notation of `cr-claude.md` §2: E is an outside consumer, X'' a read domain, 𝔅^(q) := 𝔅_E(q, X'') with block level b_q := min(q, c_E, t_(X'')), n ≤ q ≤ p. For a level function f put f_≤m := {x : f(x) ≤ m} and f_≥m := {x : f(x) ≥ m}. The consumer level c_E is read on the sites of X'' only. The tower t := t_(X'') is extended by t := −1 on the sites outside X''. The **width** of level i of f is W_i(f) := dist(f_≤(i−1), f_≥(i+1)), the Euclidean distance between site sets (+∞ if one set is empty). For the tower this includes the distance of t_≥(i+1) from the complement of X''. "Big block of level j" means a cube of side M_1ℓ_j from the grid M_1ℓ_jℤ^d. These grids are nested with the block grids ℓ_jℤ^d.

**Lemma 3.1 (widths and cubes pass to the minimum).** Let f be a level function on the sites of X'', and g a level function on all sites with g = −1 off X''. Put h := min(q, f, g) on X'' and h := −1 off X''. For every i < q, W_i(h) ≥ min(W_i(f), W_i(g)). Let 0 ≤ j ≤ q. If f_≥j coincides on X'' with a union F of big blocks of level j, and g_≥j is a union of big blocks of level j, then h_≥j is a union of big blocks of level j.

*Proof.* For i < q, h_≤(i−1) = f_≤(i−1) ∪ g_≤(i−1) and h_≥(i+1) = f_≥(i+1) ∩ g_≥(i+1). So dist(h_≤(i−1), h_≥(i+1)) is the smaller of dist(f_≤(i−1), h_≥(i+1)) ≥ W_i(f) and dist(g_≤(i−1), h_≥(i+1)) ≥ W_i(g). For 0 ≤ j ≤ q, g_≥j ⊂ X'', so h_≥j = f_≥j ∩ g_≥j = F ∩ g_≥j. Each grid cube lies inside or outside each union, so the intersection is a union of grid cubes. □

**Premises on the consumer and the tower.** These are properties of Balaban's constructions as the account quotes them. They are not proved here.

- **(G-c)** For every level i: W_i(c_E) ≥ Mℓ_i, and (c_E)_≥i coincides on X'' with a union of big blocks of level i. Source: CA-I 43454-43458 ("Each region of constant intermediate level is at least one layer of cubes of side Mℓ wide ... for the thin shells, and for the shells Γ''_j and the old collars, this width is part of their construction in [CMP 122a, §1]"); CA-I 37559-37560 (thin shells are one layer of M-cubes of their level); CMP 119 p. 256 (the domains Ω_j are unions of MR_j-cubes, with boundaries at least 2MR_j apart); CMP 102 p. 279 (M is a multiple of R_1M_1); CA-I 55632-55636, clause (P1) of a later section (the members of the label inside Z at a level i "are unions of level-i M-cubes").
- **(G-t)** The boundary tower t_(X'') is Balaban's minimal-determining-set tower (CMP 119 p. 256): (t)_≥j is a union of big blocks of level j, and W_j(t) ≥ LM_1ℓ_j. CA-I 43062-43064 names these towers as one of the three constructions that item (iii) abstracts.

The width (G-c) is not restricted to boxes in its source. The account restricts its separation statement (j) to boxes (CA-I 43442), but its justification of the widths (CA-I 43454-43458) cites the global construction.

**Corollary 3.2.** Assume (G-c) and (G-t), and let q ≤ p. For every j < q the layer {b_q = j} has width W_j(b_q) ≥ min(M, LM_1)ℓ_j. For every 0 ≤ j ≤ q the region Ω_j^(q) := (b_q)_≥j is a union of big blocks of level j. (By CMP 119 p. 256, W_j(t) ≥ LM_1ℓ_j is the bound dist(Ω_(j+1), Ω_j^c) ≥ M_1ℓ_(j+1) for its maximal domains.)

*Proof.* Lemma 3.1 with f = c_E and g = t_(X''). □

## 4. R: coverage of every ladder set (gate §2 Lemma 7, §6 row R)

R is the second case of `4.4:not-response-bound` (CA-I 10162-10204): at a real minimiser base, for complex data in the polydisc of CMP 102 (172), the five members of CMP 102 (190), each times the power of ℓ matching its order, are bounded by C_H sup_(y') |B(y')| e^(−δ_H d(y,y')). Here d is "the weighted distance of [CMP 96, (2.46)]" (CA-I 10164), and C_H depends only on L and d. Its standing hypotheses are three. The sequence of regions is admissible. The determining set has the form {Γ_i} or B_p(X'') ∪ {Γ_i}_(i<p) (CA-I 10175-10178). The background lies in the regularity class of that set.

Admissibility is CMP 96 (2.1)-(2.2), p. 224, in the form of CMP 102 (1), p. 277: Ω_j is a union of big blocks of size M_1L^jη, and (L^jη)^(−1) dist(Ω_j^c, Ω_(j+1)) > w_adm, where w_adm (RM in CMP 96 and RM_1 in CMP 102) is fixed before M.

**Proposition 4.1 (R covers the ladder).** Assume (G-c), (G-t), the floor M > w_adm, and the reading (R-form) below. Then for every q with n ≤ q ≤ p, R applies to 𝔅^(q) at the base U^(q) = U(𝔅^(q), D_0^(q)), with constants C_H, δ_H independent of q, k, E, X'' and the tower.

- **(R-form), a reading.** 𝔅_E(q, X'') is a set of the form B_q(X'') ∪ {Γ_i}_(i<q) with Γ_i the consumer's level-i region. CA-I 43060-43064 says item (iii) abstracts exactly the sets B_p(X) ∪ {Γ_i}_(i<p) of CMP 122a, the towers of CMP 119 and the domains of CMP 109. The consumer level min(p, c_E, t) is the shell level c_E where c_E < p and the tower level min(p, t) elsewhere.

*Proof.* Admissibility: Ω_j^(q) is a union of big blocks of level j, and dist((Ω_j^(q))^c, Ω_(j+1)^(q)) = W_j(b_q) ≥ min(M, LM_1)ℓ_j by Corollary 3.2. This exceeds w_adm ℓ_j by the floor on M. For the tower part, LM_1 > w_adm is Balaban's own use of CMP 102 on the sets B_j(Ω) of CMP 119 (CMP 119 p. 256, "we will use all the results of [15]"). The base is real and lies in the regularity class: U^(q) is the minimiser given by T1(i); its data D_0^(q) = M_(𝔅^(q))(Ū) satisfy T1's condition with ε_1 = 2α_kℓ_q^2 by (e) and SRC, as in the inside argument for (a) (CA-I 44236-44244) read at slot q. The constants come from the statement of R. □

**Radius margin (gate §2, §5 item 3).** Fix ε̄_1 with ε̄_1 ≤ a_1 and B_3ε̄_1 ≤ ε_0, before the couplings. Read the polydisc of CMP 102 (172) at ε_1^(102) = ε̄_1: its logarithms range over |B'| < r_P := 2C_1ε̄_1 (CA-I 16567-16572). Require 2α_k ≤ ε̄_1. Then every base U^(q), whose data satisfy T1's condition with 2α_kℓ_q^2 ≤ ε̄_1, lies in the one fixed class. Require C_RD C_F α_k ≤ r_P/2 = C_1ε̄_1, so every datum B of Lemma 5 lies in the closed half polydisc. The radius is not shrunk from step to step.

**Stencil and derivative conventions.** On ξ^+ the layer of a point y of 𝔅^(q) has side ℓ_(b_q(y)) ≥ ℓ_n/L (CA-I 44271-44303, read at slot q ≥ n). The derivative in (190) is the covariant derivative at the base (CA-I 14842-14869 writes it as ∇_U; gate §6 row R). A fixed reference point in a row changes d by a bounded amount, absorbed in C_H′ (gate §2).

**Status of R.** Reduced to (R-form) and the geometric premises (G-c) and (G-t). Admissibility of every intermediate set, with its actual tower, is proved from them (Corollary 3.2, Proposition 4.1). The exact printed form of CMP 102 (190) is not rechecked here.

## 5. ROW is not needed (gate §2 Lemma 4(b), §3 Remark at 188, §6 row ROW)

`cr-claude.md` used ROW twice. In Lemma 4(b), it changed the partition to an auxiliary 𝔅_loc. In Lemma 5, it identified the rows that 𝔅^(q) and 𝔅^(q+1) share. Both uses are removed.

**Lemma 5.1 (interface rows have an anchored chain in the actual set).** Assume Corollary 3.2 for 𝔅^(q+1), with M_1 ≥ 2. Let ⟨Γ, γ⟩ be a row of 𝔅^(q+1) with Γ of level q+1 and γ of level q, sharing a face piece in {x_μ = c}, with γ on the +μ side (the −μ side is the same with −e_μ). Then there are ν ≠ μ and s ∈ {±1} with the following properties. Put Γ' := Γ + sℓ_(q+1)e_ν and γ_j := γ + jsℓ_qe_ν for 0 ≤ j ≤ L. Then Γ' is a level-(q+1) block of 𝔅^(q+1), each γ_j is a level-q block of 𝔅^(q+1), consecutive γ_j are adjacent, and γ_L is adjacent to Γ'.

*Proof.* Put R := (b_(q+1))_≥(q+1), the union of the level-(q+1) blocks. By Corollary 3.2, R is a union of big blocks of level q+1. Let A be the big block that contains Γ, so A ⊂ R. Let Ĝ := Γ + ℓ_(q+1)e_μ. The level-q grid cube γ meets Γ's +μ face in a face piece, so it lies in the first level-q layer of Ĝ. Hence Ĝ contains a block of level q, and Ĝ ⊄ R. Ĝ lies in one big block A^+. Since R is a union of grid big blocks and A^+ ⊄ R, A^+ contains no site of R. Hence Ĝ ⊄ A, Γ lies on the +μ face of A, and A^+ = A + M_1ℓ_(q+1)e_μ. A has side M_1ℓ_(q+1) ≥ 2ℓ_(q+1) in the direction ν ≠ μ. So one of Γ ± ℓ_(q+1)e_ν lies in A; call it Γ', with sign s. Then Γ' ⊂ R is a level-(q+1) block. Γ' also lies on the +μ face of A, so Ĝ' := Γ' + ℓ_(q+1)e_μ ⊂ A^+ contains no site of R. The cubes γ_j lie in the first level-q layer of Ĝ ∪ Ĝ' along the face, and γ_L lies in Ĝ'. Each site of γ_j is within distance ℓ_q of Γ ∪ Γ' ⊂ R. By Corollary 3.2, W_q(b_(q+1)) ≥ min(M, LM_1)ℓ_q > ℓ_q. So these sites are not in (b_(q+1))_≤(q−1), which contains the complement of X''. They are not in R either. Hence they lie in X'' and have level exactly q. A level-q block is a level-q grid cube, so each γ_j is a block. The adjacencies hold because the cubes are grid neighbours across full faces or face pieces. □

**Lemma 5.2 (replaces cr-claude Lemma 4(b); no ROW).** Assume the hypotheses of cr-claude Lemma 4(b) for a row c = ⟨z_Γ, z_γ⟩ of 𝔅^(q+1), and Lemma 5.1. Then |M_(𝔅^(q+1))(U)(c) − U(ρ_c)| ≤ C_b ℓ_(q+1)^2 F, with the same C_b = (π/3)d(2C_6 + 3c_Q).

*Proof.* Follow cr-claude Lemma 4(b) up to the configuration V := e^(iη𝔞')·1, where 𝔞' equals 𝔞 on the bonds of Γ ∪ γ and 0 elsewhere, and A := sup|𝔞'|. Apply (d) to V in 𝔅^(q+1) itself, not in an auxiliary set. Use the blocks of Lemma 5.1. The rows ⟨γ_j, γ_(j+1)⟩ (1 ≤ j < L) and ⟨Γ', γ_L⟩ are rows of 𝔅^(q+1). Their carriers contain no bond with both ends in Γ ∪ γ. So by locality and normalisation, M(V) = M(1) = 1 on them. Then (d) gives b = 0 on them, and u takes one value u_0 at z_(Γ'), z_(γ_L), …, z_(γ_1). The rows ⟨Γ, Γ'⟩ (level q+1) and ⟨γ, γ_1⟩ (level q) join blocks of equal level, so P6 applies: X_1 := M(V)(⟨Γ,Γ'⟩) and X_2 := M(V)(⟨γ,γ_1⟩) satisfy |X_1 − 1| ≤ C_6ℓ_(q+1)A and |X_2 − 1| ≤ C_6ℓ_qA. The rest of cr-claude's computation is unchanged and gives |M(V)(c) − 1| ≤ (2C_6 + 3c_Q)ℓ_(q+1)A. □

This also replaces the "Remark (if (d) holds only for the fixed determining sets)" of cr-claude §8, which the gate blocked: the isolated top block of the gate's example is excluded by the big-block structure of R's admissibility (Corollary 3.2). Without that structure the remark has no proof.

**Lemma 5's shared rows.** Rows of 𝔅^(q) that do not touch R_(q+1) have both blocks off R_(q+1). These blocks belong to both sets. The account's composition grant covers this case: "the averages of a configuration over the blocks of 𝔅_ν are determined by its averages over the blocks of 𝔅: on a re-blocked block through the averages over the blocks of 𝔅 that subdivide it, and trivially where the two sets coincide" (CA-I 44949-44953, the grant of CA-I 44874). Call the last clause **COMP(=)**: on a row whose two blocks are common to the coarser and the finer set, the two averages are equal. COMP(=) needs the common blocks to carry the same base points in both sets. This is reading **(BP)**: the base point of a block depends only on the block (CA-I 42968 writes z_B; Balaban's blocks B_k(y) are indexed by their centres, CMP 109 (0.3)). With COMP(=) and (BP), cr-claude's proof that B(c) = 0 off R_(q+1) goes through without ROW.

**Status of ROW: not used.** Lemma 4(b) now needs (d) only in the actual set 𝔅^(q+1). Lemma 5 needs only the account's own composition grant.

## 6. SEP, proved in R's own metric (gate §2 Lemma 7, §6 rows SEP)

R measures decay in the weighted distance of CMP 96 (2.46), p. 231, taken for the layers of the set at which R is applied:
$$d(y,y')=\inf_{\Gamma_{y,y'}}\sum_j(L^j\eta)^{-1}\,|\Gamma_{y,y'}\cap B^j(\Lambda_j)| ,$$
where B^j(Λ_j) is the region where the set has level j. So the length of a contour is weighted at each point by the inverse side of the block of the set there. No identification with the scaled block distance of CMP 122a (1.46) is needed.

**Lemma 6.1 (SEP).** Let n ≤ q ≤ p and let d be the distance (2.46) for the layers of 𝔅^(q). Let y, y' be sites of X'' with c_E(y) = n and c_E(y') ≥ m ≥ n+2. Then
$$d(y,y')\ \ge\ \sum_{i=n+1}^{m-1}\frac{W_i(c_E)}{\ell_i}\ -\ \frac1{L-1}.$$
Under (G-c), d(y, y') ≥ (m − n − 1)M − 1.

*Proof.* Split any contour into fine steps x_s → x_(s+1) of length η, s = 0, …, N−1, with x_0 = y and x_N = y'. A fine step lies in the union of the two closed cubes of the blocks of 𝔅^(q) containing x_s and x_(s+1). So it contributes at least η/ℓ(s) to the weighted length, where ℓ(s) is the larger side of those two blocks. Fix i with n < i < m. Let T_i be the first index with c_E(x_(T_i)) ≥ i+1, and S_i the last index before T_i with c_E(x_(S_i)) ≤ i−1. Both exist, since c_E(y) = n ≤ i−1 and c_E(y') ≥ i+1. For S_i < s < T_i, c_E(x_s) = i. Consider the steps s with S_i ≤ s ≤ T_i − 2. Both endpoints have c_E ≤ i. Since b_q ≤ c_E, both blocks have side at most ℓ_i, so each such step contributes at least η/ℓ_i. There are T_i − 1 − S_i ≥ |x_(T_i) − x_(S_i)|/η − 1 ≥ W_i(c_E)/η − 1 such steps. For such a step s, c_E(x_(s+1)) = i, so the step sets for different i are disjoint. Summing over i, and using Σ_(i≥1) η/ℓ_i = Σ_(i≥1) L^(−i) = 1/(L−1), gives the claim. Under (G-c), W_i(c_E)/ℓ_i ≥ M, and 1/(L−1) ≤ 1. □

(2.46) measures the distance of two sites through the blocks that contain them (CMP 96 p. 231: d(x, x') := d(y^j(x), y^(j')(x'))). Under (G-c), c_E is constant on every block of 𝔅^(q). Indeed, b_q is constant on a block, so c_E ≥ b_q there. For i > b_q, the block is a grid cube of level b_q < i, so it lies inside one big block of level i and hence inside or outside (c_E)_≥i. So Lemma 6.1 applies to the block centres as well.

The tower does not enter: finer blocks only raise the weight. The proof uses no box. Contours run in X'', the domain whose layers define (2.46). If (2.46) is read on the whole lattice, with the finest side η outside X'', put c_E := −1 at the sites outside X''. The same proof then applies: such sites are candidates for S_i, and the steps counted for i still have sides at most ℓ_i.

**Use in Lemma 7.** cr-claude §6 shows that both blocks of a row touching R_(q+1) have c_E ≥ q on all their sites. Lemma 6.1 with m = q gives d(y*, c) ≥ (q − n − 1)M − 1 for every such row c and every reference point in it. With the gate's form of the intermediate estimate,
$$N_B(y)\le e^{\delta_Hc_{\rm st}}\sup_{c\in{\rm supp}\,B}\{|B(c)|e^{-\delta_Hd(y^*,c)}\}\le e^{\delta_H(c_{\rm st}+1)}\,C_{\rm RD}F\ell_{q+1}^2\,e^{-\delta_HM(q-n-1)_+},$$
and an empty support gives 0. So Lemma 7 holds with
$$N_q:=C_{\rm RD}F\ell_{q+1}^2e^{-\delta_HM(q-n-1)_+},\qquad C_H':=C_He^{\delta_H(c_{\rm st}+1)},$$
and the floor (Φ_H) becomes **(Φ_H′)**: 2L e^(−δ_H M) ≤ 1, that is M ≥ log(2L)/δ_H. For Corollary 9 use 2L^2 e^(−δ_H M) ≤ 1. Both are one-sided floors on M by constants fixed before M (δ_H by CA-I 10170).

**Status of SEP: proved** from (G-c), for every intermediate set with its actual tower, in the metric that R uses. The constant of the gate's §5, w(M) ≥ aM, holds with a = 1 and an additive loss of 1, absorbed in C_H′.

## 7. SRC: scope per outside class (gate §3 row SRC, §6 row SRC)

Wording (gate §3): SRC is the sufficient source condition used in this proof. It is not claimed to be necessary.

**Lemma 7.1.** Suppose **(S)**: X'' ⊂ Y_4 and X'' ⊂ Z ∪ Ω_k^old. Then |∂Ū(𝔭) − 1| < α_kη^2 for every plaquette 𝔭 with all corners in X''. Every reading of Ū in the proof is of this kind.

*Proof.* The healed level is k on Z ∪ Ω_k^old (CA-I 43224-43225). The source clause (CA-I 43295-43299) gives the bound "on the part of Y_4 where 𝗇 = k ... for every plaquette there". The proof reads Ū in four places. (e) for D_0^(q) reads the plaquettes in the blocks of a plaquette of 𝕃(𝔅^(q)), and its hypothesis reads sup|∂Ū − 1| over X''. Lemmas 3-5 read the plaquettes with corners in carriers and in N. The inside argument for (a) and for n ≥ p reads the plaquettes of X'' (CA-I 44226-44244). All these blocks lie in X''. □

**The classes.** The account defines c_E through o and 𝖻 (CA-I 43361-43366). It specifies o on Ω_k^old and on the collars Z ∩ (Ω_m^old \ Ω_(m+1)^old), and 𝖻 on Ω_k^old ∪ (Z \ Z''_k), on the shells Γ''_m and on Γ''_j ∩ Z''_(k_0+1) (CA-I 43218-43236). Inside Z''_k, the consumer's set consists of the shells Γ''_i or old collars (CA-I 43543-43544), so the shells lie in Z''_k ⊂ Z. Hence c_E is specified only on Z ∪ Ω_k^old. Ū is defined on Y_4 only, so a read domain lies in Y_4.

| Class | Outside instance (CA-I 44993-45003) | (S) | (G-c) |
|---|---|---|---|
| K1: c_E ≡ j, p ≤ j | none: no point with c_E < p | not needed | not needed |
| K2: c_E = min(o, j) | old B^(j), k_0 < j < k, on cleaned collars or on B_5 | the collars and B_5 = Z ∩ (Ω_(k_0+1)^∼5 \ Ω_(k_0+1)) lie in Z | intermediate regions are old collars; on B_5 alone c_E ≡ k_0 and the ladder is constant (B = 0 at every step) |
| K3: c_E = o | last-step B^(k) | c_E is specified only on Z ∪ Ω_k^old | old collars |
| K4: c_E = 𝖻 | domains meeting Z''_k and Ω_k^old | 𝖻 is specified only on Z ∪ Ω_k^old | thin shells Γ''_m (one layer of M-cubes, CA-I 37559-37560) and shells Γ''_j |
| K5 | read through K1-K4 | inherits | inherits |

**Status of SRC: reduced to (S).** (S) holds for every outside class under one reading: a consumer's domain lies where the account specifies its level function, and in Y_4. This reading is not checked against CMP 122a/b, which are not in `~/ym4d-papers`. A fetch of CMP 122a from Project Euclid on 2026-11-06 stopped at a bot check, so it was not read. If an outside domain reached a point of healed level below k, SRC would fail there. The present proof would then not give (a) at ε_1 = 2α_kℓ_p^2.

## 8. The gate's other written repairs, applied

Each item cites the gate section. Line numbers "note n" refer to `cr-claude.md`.

1. **Lemma 5, q = 0 (gate §2).** Read the lower scale bound on N as max(η, ℓ_(q−1)). This only improves the estimate.
2. **Gauge step, note 166 (gate §4).** Replace the sentence by: "The norms |∂U − 1| and |J(U)| are gauge invariant (CA-I 42767-42768; J1, CA-I 42794)."
3. **Step-size sum, note 168-172 (gate §4).** For J' = p − n − 1, replace the display by
$$S\le C_{\rm RD}F\ell_n^2\Bigl[L^2+\mathbf 1_{J'\ge1}L^4+\sum_{j=2}^{J'}L^{j+3}2^{1-j}\Bigr]\le5L^{J'+3}C_{\rm RD}F\ell_n^2=5L^2C_{\rm RD}F\,\ell_n\ell_p .$$
For J' = 0 use L^2 ≤ 5L^3. For J' = 1 use L^2 + L^4 ≤ 5L^4. For J' ≥ 2 the geometric sum is at most 3L^(J'+3), and the first two terms cost at most 2L^(J'+3). With N_q of §6 the j-th term is unchanged, since e^(−δ_H M) ≤ (2L)^(−1) by (Φ_H′).
4. **Current step at n = 0 (gate §4).** Take ℓ = η, 𝖼 = 2B_3α_kℓ_q^2, ‖𝓗_q‖_η ≤ C_H′N_q and η^3|D*D𝓗_q(b)| ≤ C_H′N_q. CUR then gives |J(e^(iη𝓗_q)U^(q))(b) − J(U^(q))(b)| ≤ 2C_H′N_qη^(−3) ≤ 2L^3C_H′N_qℓ_n^(−3). For n ≥ 1 keep ℓ = ℓ_n/L ≥ η, as in the note.
5. **Corollary 9 (gate §4).** Use the floor 2L^2e^(−δ_H M) ≤ 1, which gives S ≤ 3L^4C_RD F ℓ_n^2. Add the ceiling 108L^10(C_H′)^2C_RD^2C_F^2α_k ≤ 1. The stronger floor implies (Φ_H′), so Theorem 8′ stays available.
6. **Remark at note 188 (gate §3).** Withdrawn. Lemma 5.1 replaces it.
7. **SRC wording (gate §3).** As in §7.
8. **Lemma 6 (gate §3).** Replaced by Lemma 6′ (§2.3).
9. **Lemma 4(b) and ROW (gate §2).** Replaced by Lemma 5.2 (§5).
10. **Lemma 7 (gate §2).** Source scope by Proposition 4.1. SEP by Lemma 6.1. Closed half polydisc by the radius margin of §4. The intermediate estimate is written without a free row variable (§6).
11. **The intermediate-level condition, note 149 (gate §4).** It is not needed. The determining-set hypothesis fixes 𝔅(q, X) "for every level function c on X of a space of this chapter and every level p" (CA-I 43055-43059). The proof uses only that each 𝔅^(q) exists, has the properties of item (iii), and is covered by R and T1. Proposition 4.1 and Lemma 6′ supply this at every q, whether or not q is a slot level of E.

## 9. The repaired theorem and the order of constants

**Ceilings (8.1′).** Those of cr-claude (8.1), with n_P replaced by 2^d and C_RD F ≤ r_P replaced by C_RD C_F α_k ≤ C_1ε̄_1; also 2α_k ≤ ε̄_1, α_k ≤ c_av, and for Corollary 9 the ceiling of §8 item 5. Each is an upper bound on α_k by constants fixed before the couplings.

**Theorem 8′ (CR for SU(2), explicit conditional form).** Let G = SU(2). Assume:

- (i) the account's inputs T1; AV (c), (d), (e), with (d) at interface rows being the account's interface averaging hypothesis; CUR; AX; the composition grant COMP, including its clause COMP(=) (CA-I 44874, 44949-44953); R, the second case of `4.4:not-response-bound` (CA-I 10175-10204);
- (ii) Balaban's CMP 98 Proposition 6 in anchored form, P6, for rows of equal level;
- (iii) the readings (EC) (§2), (R-form) (§4) and (BP) (§5);
- (iv) for the consumer E and the read domain X'': (G-c), (G-t) (§3) and the scope (S) (§7);
- (v) M_1 ≥ 2; the floors (Φ0)-(Φ2), M > w_adm, (Φ_H′) and (Φ_K); a fixed ε̄_1 with ε̄_1 ≤ a_1 and B_3ε̄_1 ≤ ε_0; the ceilings (8.1′).

Let E be a consumer with X' ∩ 𝒞 = ∅; no box is assumed. Let p be a slot level and X'' ⊂ X' a read domain. Then conclusions (a) and (b) of `4.12:prop-reblocking-inside` hold at (p, X''), with K_b = K_0M and K_0 = (π/3)(d−1)c_Qc_d(1+3L^2)·204. The constants are uniform in k, E, p, X'', its diameter, its number of blocks and its tower.

*Proof.* cr-claude Theorem 8, with these replacements: Lemma 4(b) by Lemma 5.2; ROW in Lemma 5 by COMP(=) and (BP); Lemma 6 by Lemma 6′; in Lemma 7, the coverage of R by Proposition 4.1, SEP by Lemma 6.1 and the polydisc by the radius margin of §4; SRC on X'' by Lemma 7.1; the step-size sum and the current step at n = 0 by §8 items 3-4. The gate checked every other step of Theorem 8 under these premises (gate §§2-4: ADVANCE, after the repairs listed in §8). □

**Coverage of the outside proposition.** CA-I 45085 assumes X' ∩ 𝒞 = ∅, failure to fit in a healed box of side 204M, and {c_E < p} ∩ X'' ≠ ∅. Theorem 8′ does not use the box condition. Under the readings of §7, every outside class (K2, K3, K4, and K5 through them) satisfies (S) and (G-c). K1 has no point with c_E < p. So under premises (i)-(iii), (G-t) and (v), Theorem 8′ gives (a) and (b) for every pair of the outside proposition.

**Order of constants (gate §5, updated).**

1. L, then the constants of AV, AX, P6, T1, R (C_H, δ_H, C_1), CUR and c_st. Then C_F, C_RD, C_H′, C_⋆ and 2^d are fixed, independent of M, depth and domain.
2. M_1 and w_adm, then M: (Φ0)-(Φ2); M > w_adm; M ≥ log(2L)/δ_H (or log(2L^2)/δ_H for Corollary 9); M ≥ C_⋆/(3L^2B_HK_0). Take the next permitted value above all floors. These are one-sided floors only.
3. ε̄_1, with ε̄_1 ≤ a_1 and B_3ε̄_1 ≤ ε_0. It does not depend on M.
4. N_* and the coupling ceiling: the account's (Γ_0)-(Γ_3) and (8.1′). The account's choice at CA-I 43618-43627 then applies.

No constant is chosen backward. n_P = 2^d is fixed in step 1.

## Result

**Kind.** Proof of steps that the account leaves outstanding (CA-I 45085, "Proof outstanding"), as an implication from named premises. Proved by Claude, not yet checked by the other model. It is not a check of their proof and not a correction of their text. There is no counterexample to CR.

**Verdicts on the gate's open items.**

1. **n_P (gate BLOCK on Lemma 6): closed.** Under the reading (EC), every plaquette of 𝕃(𝔅) has at most 2^d rows (Lemma 2.2), uniformly; n_P = 16 for d = 4. (EC) is supported by Balaban's definitions (CMP 98 p. 18; CMP 102 p. 278: T1's source reads only four-factor elementary squares). By Lemma 2.1, the literal graph reading of "elementary closed circuit" contradicts the account's own input (e). Lemma 6′ replaces Lemma 6.
2. **ROW: removed.** Lemma 5.2 proves the anchored interface bound in the actual set 𝔅^(q+1), with no auxiliary partition. It uses the chain of Lemma 5.1, which exists because R's admissibility makes the top region a union of big blocks. The shared rows of Lemma 5 use the account's own composition grant, clause COMP(=), with the reading (BP).
3. **R: coverage proved from geometry.** Every ladder set 𝔅_E(q, X''), with its actual tower, is an admissible sequence for R (Proposition 4.1). This follows from the widths and the cube structure of the consumer's level regions and of the tower (G-c, G-t), via Lemma 3.1, and the reading (R-form). The radius is a fixed ε̄_1 with a closed half polydisc.
4. **SEP: proved in R's own metric.** Lemma 6.1 bounds the weighted distance of CMP 96 (2.46) below by the widths of the intermediate consumer levels: d ≥ (m − n − 1)M − 1. It uses no box and no identification with CMP 122a (1.46), and the tower does not enter. The floor is (Φ_H′): M ≥ log(2L)/δ_H.
5. **SRC: reduced to the scope (S)**, X'' ⊂ Y_4 ∩ (Z ∪ Ω_k^old) (Lemma 7.1). (S) holds for K2, K3 and K4 (and K5 through them) under one reading: a consumer's domain lies where the account specifies its level function, and inside Y_4 (§7). K1 has no below-slot pair.
6. **The gate's other repairs** (sections 2-4: step-size sum at J' = 0, the current step at n = 0, the gauge sentence, the Corollary 9 ceiling, the explicit theorem, the order of constants) are applied in §8. The intermediate-level condition is not needed (§8 item 11).

**What is proved.** Theorem 8′: for G = SU(2), conclusions (a) and (b) of the inside proposition hold at every outside pair (p, X''), with K_b = K_0M and constants uniform in depth, domain, diameter and tower. The premises are (i)-(v) of §9.

**What stays open.**
- The other model's line-by-line check, first of Lemmas 2.1, 2.2, 5.1, 5.2 and 6.1, then of Proposition 4.1 and Lemma 7.1.
- Readings, each with its support quoted: (EC); (R-form); (BP); and, for (S), that outside domains lie where c_E is specified and inside Y_4.
- Source properties of Balaban's constructions, as the account quotes them and not checked here against CMP 122a/b (not in `~/ym4d-papers`): (G-c), the widths and the cube structure of shells and old collars; (G-t), the CMP 119 tower, including LM_1 > w_adm.
- Inputs not in this item: P6 for the account's averages and base points (gate §6); COMP, which is the account's grant.
- Clause (c) (consumer radii) and the real-factor corollary for outside consumers: not attempted (gate §6, last row).

**For the lead.** If the check passes, the K2 node of `library/t0-tree.md`, the CR row of `library/open-registry.md` and FINISH row 398 can record "CR proved as an implication; open: readings (EC), (R-form), (BP), (S); source properties (G-c), (G-t); P6; COMP". None of those files is edited here.
