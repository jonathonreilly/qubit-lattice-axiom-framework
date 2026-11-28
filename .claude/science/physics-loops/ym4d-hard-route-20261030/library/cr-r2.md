lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T06:30Z

# CR, second round: closing the gaps of gates/cr-gate.md for library/cr-claude.md

Started 2026-11-06T18:30Z at commit e83525781, branch claude/ym4d-hard-route, FINISH row 398. Original research text by Claude (Opus 5.5, max effort). `gates/cr-r2-gate.md` checked that revision and supplied written repairs. Codex applied those repairs in place for FINISH row 403 at checkout `c3112412a83475881c5c19fab42e547c50537859`. This edit is research text, not a new audit or independent proof check, and grants no status. No computer-assisted step; no numerics were run.

**Credit.** The statement CR, the inside proof, the refined-minimiser identity and the inputs T1, AV, R, CUR, AX, COMP and (j) are from Ethan Sussman and Levent Alpoge's complete account (with Claude and Codex as authors of their text), commit 31a47c543775, cited as CA-I with raw-TeX line numbers (fetched to a scratch folder for this lane). The averaging, minimiser and response theory is Tadeusz Balaban's; CMP 98, 102 and 119 were reported as read by the original author from local PDFs. Those papers are unavailable in this repair task; their quotations are retained from the repository and account, without independent PDF verification. The one-level ladder, Lemmas 1-9 and the numbering below are from `library/cr-claude.md` (Claude). The first-round repairs come from `gates/cr-gate.md` (Codex); the second-round qualifications and replacements come from `gates/cr-r2-gate.md` (Codex).

## 1. Scope and duplicate check

**Item.** FINISH row 398: close the gaps of `gates/cr-gate.md` for `library/cr-claude.md`. (1) The uniform circuit bound n_P of Lemma 6. (2) The identifications R and ROW, and the conditions SRC and SEP, for every outside consumer class of CA-I `4.12:prop-reblocking-outside` (CA-I 45085-45106, status "Proof outstanding"). Also apply the gate's written repairs (its sections 2-4). `cr-claude.md` is not edited.

**Duplicate check (rule 0a).** `library/open-core.md` lists CR as a core statement (lines 80-99) owned by this lane family. `library/l17c.md` has no entry for n_P, ROW, SRC or SEP. The FINISH rows that touch CR are 310 (`rb`), 322 (`open-core`), 348 (`cr-claude`), 353 (`crca`), 396 (`cr-gate`) and this row. None of them attacks n_P, ROW, R coverage, SRC or SEP. So no other row covers these lemmas.

**Source identification.** CA-I 42980–42984 defines an elementary closed circuit but does not identify its cells. CA-I 43013–43016 composes averages at interfaces; 43113–43127 imports the data test in that graph's terms. Four-factor squares on Balaban's homogeneous lattices do not by themselves identify the graph circuits after interface composition. Retain (EC) as an additional, unverified reading of those exact plaquettes. The quoted homogeneous-square examples support that reading but do not prove it.

## 2. The circuit bound n_P under the open identification (EC)

### 2.1 What Balaban's plaquettes are

- **CMP 98, p. 18.** "Plaquettes are oriented elementary squares of the lattice Ω ... The above definitions of bonds and plaquettes may be applied to an arbitrary lattice, e.g., to Ω^(j)." So on a lattice of level-j blocks, a plaquette is an elementary square: four bonds.
- **CMP 102, pp. 277-278.** The determining set is 𝔅_k = ∪_j Λ_j, with Λ_j = Ω_j^(j) \ Ω_(j+1)^(j). Sets of plaquettes are "sets of plaquettes with at least one corner belonging to Ω_j". The data condition (7) is |(∂V)(p') − 1| < ε_1 for p' ∈ 𝔅_k. Balaban explains: p' is an elementary square of the level-j lattice. If all four corners lie in Λ_j, then (∂V)(p') = V(∂p'). If a bond ⟨y,z⟩ of p' is not in Λ_j, then y, z ∈ Λ_(j−1), and that factor is replaced by a value V̄(y,z) built from the finer data. So every plaquette that T1's source reads has exactly four factors.
- **CMP 119 (2.2), (2.10)-(2.11), p. 255-256.** The determining set B = ∪_j Γ_j "is meant for sets of points, bonds and plaquettes"; M_B(U) = M^j(U) on Γ_j. Again the plaquettes are elementary squares of the homogeneous level-j lattices.

The account replaces Balaban's nested lattices by one partition 𝔅 into blocks, with a bond for each pair of adjacent blocks (CA-I 42966-42971). Its plaquettes are "elementary closed circuits" of that graph, with ∂D(P) the ordered product along the circuit. So the account's plaquettes are circuits of 𝕃(𝔅). The definition does not say which circuits. The next lemma shows that the literal graph reading (every simple cycle) is not available.

**Lemma 2.1 (the literal reading contradicts (e)).** Let a domain X be a ring of N ≥ 5 blocks B_0, …, B_(N−1) of one level, with B_i adjacent to B_(i±1) (indices mod N) and to no other block. Example: the perimeter of an r × r square of blocks in two coordinates, r ≥ 3, one block thick in the others. Suppose the cycle P = (z_0, z_1, …, z_(N−1), z_0) is a plaquette of 𝕃(𝔅) for 𝔅 = {B_i}. Then (c) and (e) of CA-I 43018-43052 cannot both hold.

*Proof.* Let B_0 = B_(N−1) + ℓe_μ. Fix g ∈ G with g ≠ 1. Let U = g on the bonds ⟨x, x+ηe_μ⟩ with x ∈ B_(N−1) and x+ηe_μ ∈ B_0, and U = 1 on every other bond of X. Let 𝔭 be a fine plaquette of X (four corners in X) that contains such a bond ⟨x, x+ηe_μ⟩. Let y = x + sηe_ν, ν ≠ μ, be its third corner. If y ∈ B_(N−1), then y + ηe_μ ∈ B_0, because equal adjacent blocks share a full face. Then 𝔭 contains two such bonds with opposite orientations, and its two ν-bonds carry 1, so ∂U(𝔭) = 1. If y ∉ B_(N−1), then y lies in the ν-neighbour B_(N−2) of B_(N−1), and y + ηe_μ lies in the ν-neighbour B_1 of B_0. Then B_(N−2) and B_1 are adjacent, which is false for N ≥ 5. Plaquettes without such a bond carry 1 on all four bonds. So ∂U(𝔭) = 1 for every plaquette 𝔭 of X. For i ≠ N−1 the carrier B_i ∪ B_(i+1) contains no bond from B_(N−1) to B_0. By locality and normalisation, M(U)(⟨z_i,z_(i+1)⟩) = M(1)(⟨z_i,z_(i+1)⟩) = 1. On the carrier B_(N−1) ∪ B_0, U equals 1^σ with σ = 1 on B_(N−1) and σ = g^(−1) on B_0. Extend σ by 1 to X. Locality and covariance give M(U)(⟨z_(N−1),z_0⟩) = M(1^σ)(⟨z_(N−1),z_0⟩) = σ(z_(N−1))σ(z_0)^(−1) = g. Hence ∂M(U)(P) = g and |∂M(U)(P) − 1| > 0. The hypothesis of (e) holds, since sup|∂U − 1| = 0. The right side of (e) is 0. □

So under any reading in which the account's input (e) holds, a plaquette of 𝕃(𝔅) is not an arbitrary simple cycle. This excludes the indiscriminate simple-cycle reading; it does not prove (EC), or exclude every contractible circuit without a common point. The claim about collars' topology is not needed for this example.

### 2.2 The identification and the bound

**Open identification (EC).** Every plaquette P of 𝕃(𝔅) used by AV(e) and T1 is a closed circuit of 𝕃(𝔅) through pairwise distinct blocks whose closed cubes contain a common point of ℝ^d. (EC) is a containment. It does not say that every such circuit is a plaquette.

The quoted homogeneous-square examples support that reading but do not prove it. Four-factor squares do not identify the account's graph circuits after interface composition. (EC) remains an additional, unverified source identification.

Blocks are identified with closed cubes. Level-m cubes are anchored at the origin and have side ℓ_m ∈ ηℤ, so their corners lie in ηℤ^d.

**Lemma 2.2 (n_P = 2^d).** Let Q_1, …, Q_r be distinct closed blocks of a determining set that contain a common point x. Then r ≤ 2^d. Hence every plaquette under (EC) has at most 2^d rows, uniformly in k, X, 𝔅, the level function and the tower.

*Proof.* The domain is finite, so r is finite. For a sign vector s ∈ {±1}^d and t > 0, let O_s(t) := {y : 0 < s_μ(y_μ − x_μ) < t for all μ}. This is a nonempty open set. Let Q_i = ∏_μ [a_μ, a_μ + ℓ] with x ∈ Q_i. For each μ, x_μ < a_μ + ℓ or x_μ > a_μ, since ℓ > 0. Put s(i)_μ = +1 in the first case and −1 otherwise. The gap a_μ + ℓ − x_μ, resp. x_μ − a_μ, is then positive. Choose t > 0 below all these gaps, for all μ and all i. Then O_(s(i))(t) ⊂ Q_i. An open set inside a closed cube lies in its interior. Distinct blocks of a partition are distinct cubes of the nested L-adic families, so their interiors are disjoint. Hence i ↦ s(i) is injective, and r ≤ 2^d. □

So for d = 4, n_P = 16, with no dependence on L.

### 2.3 Repaired Lemma 6

**Lemma 6′ (replaces Lemma 6 of cr-claude.md).** Assume (EC), SRC, Lemma 5 and COMP, with AV(e) and T1 on the same action domain. Put
$$\varepsilon_1':=(2+2^dC_{\rm RD}C_FL^2)\,\alpha_k\ell_q^2$$
and assume ε_1′ ≤ a_1 and B_3ε_1′ ≤ ε_0. Then U^(q+1) = U(𝔅^(q), D_W)^τ for a gauge τ.

*Proof.* The proof of cr-claude Lemma 6 applies word for word, with n_P replaced by 2^d. The only change is in the data condition. Let P be a plaquette of 𝕃(𝔅^(q)) with base point z_0. By Lemma 5, D_W = (e^{iB}D_0)^v. The ordered product around P gives ∂D_W(P) = v(z_0) ∂(e^{iB}D_0)(P) v(z_0)^{−1}. For unitary factors, |∏_i e^{iB_i}g_i − ∏_i g_i| ≤ Σ_i |e^{iB_i} − 1| ≤ Σ_i |B_i|. P has at most 2^d rows by Lemma 2.2. Hence |∂D_W(P) − 1| ≤ |∂D_0(P) − 1| + 2^d sup|B| ≤ 2α_kℓ_q^2 + 2^dC_RD F ℓ_(q+1)^2 = ε_1′. Here the first bound is (e) with SRC, and ℓ(P) ≤ ℓ_q because every block of 𝔅^(q) has level at most q. □

In the ceilings (8.1), replace n_P by 2^d. The gate's conditional verdict on the rest of Lemma 6 (COMP gives the inclusion of the constraint manifolds; criticality restricts; the refinement keeps T1's threshold) is unchanged. **Status of n_P:** the uniform bound is proved under (EC); identification of the source's plaquettes remains open. Calling (EC) a reading rather than a consumer hypothesis does not discharge it.

## 3. Geometry of the ladder sets

Notation of `cr-claude.md` §2: E is an outside consumer, X'' a read domain, 𝔅^(q) := 𝔅_E(q, X'') with block level b_q := min(q, c_E, t_(X'')), n ≤ q ≤ p. For a level function f put f_≤m := {x : f(x) ≤ m} and f_≥m := {x : f(x) ≥ m}. The consumer level c_E is read on the sites of X'' only. The tower t := t_(X'') is extended by t := −1 on the sites outside X''. The **width** of level i of f is W_i(f) := dist(f_≤(i−1), f_≥(i+1)), the Euclidean distance between site sets (+∞ if one set is empty). For the tower this includes the distance of t_≥(i+1) from the complement of X''. "Big block of level j" means a cube of side M_1ℓ_j from the grid M_1ℓ_jℤ^d. These grids are nested with the block grids ℓ_jℤ^d.

**Lemma 3.1 (widths and cubes pass to the minimum).** Let f be a level function on the sites of X'', and g a level function on all sites with g = −1 off X''. Put h := min(q, f, g) on X'' and h := −1 off X''. For every i < q, W_i(h) ≥ min(W_i(f), W_i(g)). Let 0 ≤ j ≤ q. If f_≥j coincides on X'' with a union F of big blocks of level j, and g_≥j is a union of big blocks of level j, then h_≥j is a union of big blocks of level j.

*Proof.* For i < q, h_≤(i−1) = f_≤(i−1) ∪ g_≤(i−1) and h_≥(i+1) = f_≥(i+1) ∩ g_≥(i+1). So dist(h_≤(i−1), h_≥(i+1)) is the smaller of dist(f_≤(i−1), h_≥(i+1)) ≥ W_i(f) and dist(g_≤(i−1), h_≥(i+1)) ≥ W_i(g). For 0 ≤ j ≤ q, g_≥j ⊂ X'', so h_≥j = f_≥j ∩ g_≥j = F ∩ g_≥j. Each grid cube lies inside or outside each union, so the intersection is a union of grid cubes. □

**Premises on the consumer and the tower.** These are open source properties to be matched on every actual read domain. Widths below remain Euclidean.

- **(G-c)** For every level i, retain two separate clauses: W_i(c_E) ≥ Mℓ_i; and (c_E)_≥i coincides on X'' with a union of aligned big blocks of level i. The width sentence is at **CA-I 43520–43524**: “Each region of constant intermediate level is at least one layer of cubes of side Mℓ wide”. It supports widths of the named shells and collars. CA-I 37559–37565 also supplies the thin-shell width and the healed region. Neither passage proves that every restricted consumer superlevel set has the particular global big-block extension required by (G-c). CA-I 55632–55636 is a hypothesis about specified label members; it is not a universal cubicality assertion about these consumers. Retain the width and aligned-cubicality clauses of (G-c), separately, as source properties to be matched on every read domain. The outline's separated-sequence and localisation assertions (SA 9593–9599, 9776–9789) are indexed as definitions/sketches, not a completed proof of this matching.
- **(G-t)** The actual tower has the advertised aligned superlevel cubes and widths: (t)_≥j is a union of big blocks of level j, and W_j(t) ≥ LM_1ℓ_j. It must also satisfy **LM_1 > w_adm in the admissibility distance**. The floor M > w_adm cannot establish that second inequality. CA-I 43060–43064 only says that the determining-set hypothesis abstracts several constructions. It does not identify every actual tower with the particular CMP 119 tower.

**Distance convention.** Use the same distance on both sides of the admissibility inequality. Widths here are Euclidean, whereas SA 9596 and 10116 state separation in sup-distance. If that is the imported convention, use dist_infinity ≥ dist_2/√d and require **both M > √d w_adm and LM_1 > √d w_adm**. Otherwise formulate the admissibility threshold in the same distance as the width premises. This norm choice remains part of the open tower/source matching.

**Corollary 3.2.** Assume (G-c) and (G-t), and let q ≤ p. For every j < q the layer {b_q = j} has width W_j(b_q) ≥ min(M, LM_1)ℓ_j. For every 0 ≤ j ≤ q the region Ω_j^(q) := (b_q)_≥j is a union of big blocks of level j. (By CMP 119 p. 256, W_j(t) ≥ LM_1ℓ_j is the bound dist(Ω_(j+1), Ω_j^c) ≥ M_1ℓ_(j+1) for its maximal domains.)

*Proof.* Lemma 3.1 with f = c_E and g = t_(X''). □

## 4. R: coverage of every ladder set (gate §2 Lemma 7, §6 row R)

R is the second case of `4.4:not-response-bound` (CA-I 10162-10204): at a real minimiser base, for complex data in the polydisc of CMP 102 (172), the five members of CMP 102 (190), each times the power of ℓ matching its order, are bounded by C_H sup_(y') |B(y')| e^(−δ_H d(y,y')). Here d is "the weighted distance of [CMP 96, (2.46)]" (CA-I 10164), and C_H depends only on L and d. Its standing hypotheses are three. The sequence of regions is admissible. The determining set has the form {Γ_i} or B_p(X'') ∪ {Γ_i}_(i<p) (CA-I 10175-10178). The background lies in the regularity class of that set.

Admissibility is CMP 96 (2.1)-(2.2), p. 224, in the form of CMP 102 (1), p. 277: Ω_j is a union of big blocks of size M_1L^jη, and (L^jη)^(−1) dist(Ω_j^c, Ω_(j+1)) > w_adm, where w_adm (RM in CMP 96 and RM_1 in CMP 102) is fixed before M.

**Proposition 4.1 (R covers the ladder, conditionally).** Assume (G-c), (G-t), the admissibility floor on M in the distance convention of §3, and the open identification (R-form) below. Retain SRC, AV(e), T1 and the smallness conditions, including the fixed-radius conditions below. Assume these identifications and conditions for every intermediate q with n ≤ q ≤ p. Then R applies to 𝔅^(q) at the regular real base U^(q) = U(𝔅^(q), D_0^(q)), with constants C_H, δ_H independent of q, k, E, X'' and the tower.

- **(R-form), an open identification.** The shell regions are truncated by the actual tower; assume that the resulting set, including its rows, interfaces and base conventions, is the stated `B_q(X'') union {Gamma_i}_{i<q}` system of R. CA-I 43060–43064 does not prove this identification.

*Proof.* Admissibility: Ω_j^(q) is a union of big blocks of level j, and dist_2((Ω_j^(q))^c, Ω_(j+1)^(q)) = W_j(b_q) ≥ min(M, LM_1)ℓ_j by Corollary 3.2. In the same distance this exceeds w_adm ℓ_j by both inequalities of §3. If admissibility uses sup-distance, dist_infinity ≥ dist_2/√d and both norm-converted inequalities give the required strict bound. The tower inequality is an open part of (G-t); the later floor on M does not supply it. The base is real and lies in the regularity class: U^(q) is the minimiser given by T1(i); its data D_0^(q) = M_(𝔅^(q))(Ū) satisfy T1's condition with ε_1 = 2α_kℓ_q^2 by (e) and SRC, as in the inside argument for (a) (CA-I 44236–44244) read at slot q, with the stated smallness conditions. With (R-form), admissibility, and this regular real base, CA-I 10175–10204 supplies R uniformly. This checks the implication; it does not independently verify Balaban's five-member response formula. □

**Radius margin (gate §2, §5 item 3).** Fix a positive uniform ε̄_1 in the admitted real-base class, respecting any further radius restrictions of the identified R source, with ε̄_1 ≤ a_1 and B_3ε̄_1 ≤ ε_0, before the couplings. Read the polydisc of CMP 102 (172) at ε_1^(102) = ε̄_1: its logarithms range over |B'| < r_P := 2C_1ε̄_1 (CA-I 16567-16572). Require 2α_k ≤ ε̄_1. Then every base U^(q), whose data satisfy T1's condition with 2α_kℓ_q^2 ≤ ε̄_1, lies in the one fixed class. Require C_RD C_F α_k ≤ r_P/2 = C_1ε̄_1, so every datum B of Lemma 5 lies in the closed half polydisc. The radius is uniform over the pairs and is not reselected at each rung. Dependence on already chosen size parameters, including M, is allowed.

**Stencil and derivative conventions.** On ξ^+ the layer of a point y of 𝔅^(q) has side ℓ_(b_q(y)) ≥ ℓ_n/L (CA-I 44271-44303, read at slot q ≥ n). The derivative in (190) is the covariant derivative at the base (CA-I 14842-14869 writes it as ∇_U; gate §6 row R). A fixed reference point in a row changes d by a bounded amount, absorbed in C_H′ (gate §2). Keep the uniform stencil/reference-point constant among the constants of this identified response system. Use the real-base second-order member, not the independent-current replacement (CA-I 14842–14866).

**Status of R.** The implication uses (R-form), (G-c), (G-t), SRC, AV(e), T1, the stated smallness conditions and the distance convention. They must hold for every intermediate ladder with its actual tower. Corollary 3.2 and Proposition 4.1 give admissibility and R coverage from these premises. The exact printed form of CMP 102 (190) is not independently rechecked here.

## 5. ROW is not needed (gate §2 Lemma 4(b), §3 Remark at 188, §6 row ROW)

`cr-claude.md` used ROW twice. In Lemma 4(b), it changed the partition to an auxiliary 𝔅_loc. In Lemma 5, it identified the rows that 𝔅^(q) and 𝔅^(q+1) share. The auxiliary-partition use is removed; the required common-row equality is retained explicitly in COMP(=) and (BP).

**Lemma 5.1 (interface rows have an anchored chain in the actual set).** Assume Corollary 3.2 for 𝔅^(q+1), with M_1 ≥ 2. Let ⟨Γ, γ⟩ be a row of 𝔅^(q+1) with Γ of level q+1 and γ of level q, sharing a face piece in {x_μ = c}, with γ on the +μ side (the −μ side is the same with −e_μ). Then there are ν ≠ μ and s ∈ {±1} with the following properties. Put Γ' := Γ + sℓ_(q+1)e_ν and γ_j := γ + jsℓ_qe_ν for 0 ≤ j ≤ L. Then Γ' is a level-(q+1) block of 𝔅^(q+1), each γ_j is a level-q block of 𝔅^(q+1), consecutive γ_j are adjacent, and γ_L is adjacent to Γ'.

*Proof.* Put R := (b_(q+1))_≥(q+1), the union of the level-(q+1) blocks. By Corollary 3.2, R is a union of big blocks of level q+1. Let A be the big block that contains Γ, so A ⊂ R. Let Ĝ := Γ + ℓ_(q+1)e_μ. The level-q grid cube γ meets Γ's +μ face in a face piece, so it lies in the first level-q layer of Ĝ. Hence Ĝ contains a block of level q, and Ĝ ⊄ R. Ĝ lies in one big block A^+. Since R is a union of grid big blocks and A^+ ⊄ R, A^+ contains no site of R. Hence Ĝ ⊄ A, Γ lies on the +μ face of A, and A^+ = A + M_1ℓ_(q+1)e_μ. A has side M_1ℓ_(q+1) ≥ 2ℓ_(q+1) in the direction ν ≠ μ. So one of Γ ± ℓ_(q+1)e_ν lies in A; call it Γ', with sign s. Then Γ' ⊂ R is a level-(q+1) block. Γ' also lies on the +μ face of A, so Ĝ' := Γ' + ℓ_(q+1)e_μ ⊂ A^+ contains no site of R. The cubes γ_j lie in the first level-q layer of Ĝ ∪ Ĝ' along the face, and γ_L lies in Ĝ'. Each site of γ_j is within distance ℓ_q of Γ ∪ Γ' ⊂ R. By Corollary 3.2, W_q(b_(q+1)) ≥ min(M, LM_1)ℓ_q > ℓ_q. So these sites are not in (b_(q+1))_≤(q−1), which contains the complement of X''. They are not in R either. Hence they lie in X'' and have level exactly q. A level-q block is a level-q grid cube, so each γ_j is a block. The adjacencies hold because the cubes are grid neighbours across full faces or face pieces. □

**Lemma 5.2 (replaces cr-claude Lemma 4(b); no ROW).** Assume the hypotheses of cr-claude Lemma 4(b) for a row c = ⟨z_Γ, z_γ⟩ of 𝔅^(q+1), and Lemma 5.1. Then |M_(𝔅^(q+1))(U)(c) − U(ρ_c)| ≤ C_b ℓ_(q+1)^2 F, with the same C_b = (π/3)d(2C_6 + 3c_Q).

*Proof.* Follow cr-claude Lemma 4(b) up to the configuration V := e^(iη𝔞')·1, where 𝔞' equals 𝔞 on the bonds of Γ ∪ γ and 0 elsewhere, and A := sup|𝔞'|. Apply (d) to V in 𝔅^(q+1) itself, not in an auxiliary set. Use the blocks of Lemma 5.1. The rows ⟨γ_j, γ_(j+1)⟩ (1 ≤ j < L) and ⟨Γ', γ_L⟩ are rows of 𝔅^(q+1). Their carriers contain no bond with both ends in Γ ∪ γ. So by locality and normalisation, M(V) = M(1) = 1 on them. Then (d) gives b = 0 on them, and u takes one value u_0 at z_(Γ'), z_(γ_L), …, z_(γ_1). The rows ⟨Γ, Γ'⟩ (level q+1) and ⟨γ, γ_1⟩ (level q) join blocks of equal level, so P6 applies: X_1 := M(V)(⟨Γ,Γ'⟩) and X_2 := M(V)(⟨γ,γ_1⟩) satisfy |X_1 − 1| ≤ C_6ℓ_(q+1)A and |X_2 − 1| ≤ C_6ℓ_qA. The rest of cr-claude's computation is unchanged and gives |M(V)(c) − 1| ≤ (2C_6 + 3c_Q)ℓ_(q+1)A. □

This also replaces the "Remark (if (d) holds only for the fixed determining sets)" of cr-claude §8, which the gate blocked: the isolated top block of the gate's example is excluded by the big-block structure of R's admissibility (Corollary 3.2). Without that structure the remark has no proof.

**Lemma 5's shared rows.** Rows of 𝔅^(q) that do not touch R_(q+1) have both blocks off R_(q+1). These blocks belong to both sets. The account's composition grant covers this case: "the averages of a configuration over the blocks of 𝔅_ν are determined by its averages over the blocks of 𝔅: on a re-blocked block through the averages over the blocks of 𝔅 that subdivide it, and trivially where the two sets coincide" (CA-I 44949-44953, the grant of CA-I 44874). Call the last clause **COMP(=)**: on a row whose two blocks are common to the coarser and the finer set, the two averages are equal. COMP(=) needs the common blocks to carry the same base points in both sets. This is reading **(BP)**: the base point of a block depends only on the block (CA-I 42968 writes z_B; Balaban's blocks B_k(y) are indexed by their centres, CMP 109 (0.3)). With COMP(=) and (BP), cr-claude's proof that B(c) = 0 off R_(q+1) goes through without ROW. The notation z_B alone does not prove this consistency across partitions; (BP) remains open. Nothing here proves COMP.

**Status of ROW: no separate assumption.** Lemma 4(b) now needs (d) only in the actual set 𝔅^(q+1), with P6 and the chain of Lemma 5.1. Lemma 5 uses COMP(=) and (BP) for its common rows.

## 6. SEP, proved in R's own metric (gate §2 Lemma 7, §6 rows SEP)

R measures decay in the weighted distance of CMP 96 (2.46), p. 231, taken for the layers of the set at which R is applied:
$$d(y,y')=\inf_{\Gamma_{y,y'}}\sum_j(L^j\eta)^{-1}\,|\Gamma_{y,y'}\cap B^j(\Lambda_j)| ,$$
where B^j(Λ_j) is the region where the set has level j. So the length of a contour is weighted at each point by the inverse side of the block of the set there. No identification with the scaled block distance of CMP 122a (1.46) is needed. CA-I 152251–152265 prints this metric over admissible contours; CA-I 147850 says each layer uses that layer's lattice bonds. SA 9602–9605 and 10119–10127 distinguish the more permissive ambient path distance.

**Lemma 6.1 (SEP for contours contained in X'').** Assume (G-c). Let n ≤ q ≤ p and let d be the distance (2.46) for the layers of 𝔅^(q), restricted here to contours contained in X''. Let y, y' be sites of X'' with c_E(y) = n and c_E(y') ≥ m ≥ n+2. Then
$$d(y,y')\ \ge\ \sum_{i=n+1}^{m-1}\frac{W_i(c_E)}{\ell_i}\ -\ \frac1{L-1}.$$
Under (G-c), d(y, y') ≥ (m − n − 1)M − 1.

*Proof.* Split any contour into fine steps x_s → x_(s+1) of length η, s = 0, …, N−1, with x_0 = y and x_N = y'. A fine step lies in the union of the two closed cubes of the blocks of 𝔅^(q) containing x_s and x_(s+1). So it contributes at least η/ℓ(s) to the weighted length, where ℓ(s) is the larger side of those two blocks. Fix i with n < i < m. Let T_i be the first index with c_E(x_(T_i)) ≥ i+1, and S_i the last index before T_i with c_E(x_(S_i)) ≤ i−1. Both exist, since c_E(y) = n ≤ i−1 and c_E(y') ≥ i+1. For S_i < s < T_i, c_E(x_s) = i. Consider the steps s with S_i ≤ s ≤ T_i − 2. Both endpoints have c_E ≤ i. Since b_q ≤ c_E, both blocks have side at most ℓ_i, so each such step contributes at least η/ℓ_i. There are T_i − 1 − S_i ≥ |x_(T_i) − x_(S_i)|/η − 1 ≥ W_i(c_E)/η − 1 such steps. For such a step s, c_E(x_(s+1)) = i, so the step sets for different i are disjoint. Summing over i, and using Σ_(i≥1) η/ℓ_i = Σ_(i≥1) L^(−i) = 1/(L−1), gives the claim. Under (G-c), W_i(c_E)/ℓ_i ≥ M, and 1/(L−1) ≤ 1. □

(2.46) measures the distance of two sites through the blocks that contain them (CMP 96 p. 231: d(x, x') := d(y^j(x), y^(j')(x'))). Under (G-c), c_E is constant on every block of 𝔅^(q). Indeed, b_q is constant on a block, so c_E ≥ b_q there. For i > b_q, the block is a grid cube of level b_q < i, so it lies inside one big block of level i and hence inside or outside (c_E)_≥i. So Lemma 6.1 applies to the block centres as well.

**Exterior repair (SEP*).** Extending c_E = −1 outside X'' changes its widths. For two distant cubical components with consumer levels n and m ≥ n+2, the original intermediate widths are their separation. The extension makes them small at the high component's boundary. Thus the last-low site outside X'' need not be separated from the first-high site by the original W_i. This refutes the extension's inference, not CR or SEP itself.

The following is the gate's written repair (lines 84–124), copied verbatim. Its “note 123” denotes the fine-step argument in the preceding proof. Assume (G-c), (G-t), compatible block geometry and the specified contour weights.

Here is a sufficient repair that also covers paths leaving the domain. It uses the existing (G-t), and weakens the separation constant by the fixed factor `L+1`. It avoids adding a contour-confinement assumption to R.

For `n<i<m`, put

\[
A_i=\{x\in X'':c_E(x)\le i-1\},\qquad
v_i(x)=\min\{W_i(c_E),\operatorname{dist}_2(x,A_i)\},\qquad
V(x)=\sum_{i=n+1}^{m-1}\ell_i^{-1}v_i(x).
\]

Define these functions on the whole fine lattice. Both sets defining each width are nonempty because of the endpoints. At the low endpoint `V(y)=0`; at the high endpoint

\[
V(y')=\sum_{i=n+1}^{m-1}W_i(c_E)/\ell_i.
\]

Each `v_i` changes by at most `eta` on a fine step. At an interior site of consumer level `j`, it equals its cap for `i<j` and zero for `i>j`. Interior neighbouring sites have consumer levels differing by at most one: a jump of two would contradict `W_i>=M ell_i>eta` at the intervening index. Thus on a step with equal endpoint levels `j`, only `v_j` can change. On a step between levels `j` and `j+1`, only `v_j,v_(j+1)` can change, and

\[
|\Delta V|\le\eta(\ell_j^{-1}+\ell_{j+1}^{-1})
=(L+1)\eta/\ell_{j+1}.
\]

Terms outside the displayed index range are simply absent. Since `b_q<=c_E`, the weighted step length is at least `eta/ell_j` in the first case and `eta/ell_(j+1)` in the second. These are the same fine-step lower bounds used at note 123.

For a step touching the exterior, its inside endpoint, if any, has tower level zero. Otherwise (G-t) at level zero would give distance at least `LM_1 eta>eta` from that endpoint to the exterior. Such a step therefore has weight one, as do wholly exterior steps under the proposed finest-scale exterior convention. On it,

\[
|\Delta V|\le\sum_{i=n+1}^{m-1}\eta/\ell_i
\le 1/(L-1)\le1.
\]

Summing these inequalities over a subdivided admissible contour and taking the infimum proves the sufficient replacement

\[
d(y,y')\ge\frac1{L+1}\sum_{i=n+1}^{m-1}\frac{W_i(c_E)}{\ell_i}
\ge\frac{M}{L+1}(m-n-1).
\tag{SEP*}
\]

It also holds when only contours inside `X''` are allowed. Passing to block reference points uses the already checked blockwise constancy of `c_E`. No run or finite enumeration is used.

**Use in Lemma 7.** cr-claude §6 shows that both blocks of a row touching R_(q+1) have c_E ≥ q on all their sites. Apply (SEP*) with m = q. For the near levels use nonnegativity of the distance. Set

\[
w_*:=M/(L+1),\qquad
N_q=C_{\rm RD}F\ell_{q+1}^2e^{-\delta_Hw_*(q-n-1)_+}.
\]

The note's `C_H'=C_H exp(delta_H(c_st+1))` is still sufficient; the extra `1` is now harmless slack. Keep the supremum over the support of `B`, with value zero for empty support. The floors are

\[
M\ge\frac{L+1}{\delta_H}\log(2L),
\quad\text{or}\quad
M\ge\frac{L+1}{\delta_H}\log(2L^2)
\text{ for Corollary 9}.
\tag{Phi-H*}
\]

The intermediate response estimate retains the support supremum:
$$N_B(y)\le e^{\delta_Hc_{\rm st}}\sup_{c\in{\rm supp}\,B}\{|B(c)|e^{-\delta_Hd(y^*,c)}\}\le e^{\delta_H(c_{\rm st}+1)}\,C_{\rm RD}F\ell_{q+1}^2\,e^{-\delta_Hw_*(q-n-1)_+}.$$
An empty support gives 0. Lemma 7 uses N_q above and C_H′ := C_H exp(δ_H(c_st+1)); the extra 1 is harmless slack.

Then the previous gate's response estimate and all subsequent sums apply unchanged. If R's actual contours are proved confined to `X''`, the original stronger SEP bound and smaller floor can instead be retained. The unrestricted reading does not follow from the old exterior extension; (SEP*) supplies the needed implication without that claim.

**Status of SEP.** There is no separate SEP assumption after (SEP*), which follows from (G-c), (G-t), compatible block geometry and the specified contour weights. Use (Phi-H*) throughout; the tower enters the exterior-step argument.

## 7. SRC: scope per outside class (gate §3 row SRC, §6 row SRC)

Wording (gate §3): SRC is the sufficient source condition used in this proof. It is not claimed to be necessary.

**Lemma 7.1.** Suppose **(S)**: X'' ⊂ Y_4 and X'' ⊂ Z ∪ Ω_k^old. Then |∂Ū(𝔭) − 1| < α_kη^2 for every plaquette 𝔭 with all corners in X''. Every reading of Ū in the proof is of this kind.

*Proof.* The healed level is k on Z ∪ Ω_k^old (CA-I 43224-43225). The source clause (CA-I 43295-43299) gives the bound "on the part of Y_4 where 𝗇 = k ... for every plaquette there". The proof reads Ū in four places. (e) for D_0^(q) reads the plaquettes in the blocks of a plaquette of 𝕃(𝔅^(q)), and its hypothesis reads sup|∂Ū − 1| over X''. Lemmas 3-5 read the plaquettes with corners in carriers and in N. The inside argument for (a) and for n ≥ p reads the plaquettes of X'' (CA-I 44226-44244). All these blocks lie in X''. □

**The classes.** The account specifies the consumer level functions through o and 𝖻 (CA-I 43361–43367). A level function's listed values do not prove that every consumer domain is contained in the listed regions. Retain (S) for each actual pair. Likewise, shell names do not discharge either clause of (G-c).

| Class | Coverage and retained obligations |
|---|---|
| K1: c_E ≡ j, p ≤ j | No below-slot pair: c_E = j and p ≤ j exclude it (CA-I 43350, 43361–43363). |
| K2: c_E = min(o, j) | CA-I 43243–43245 puts B_5 in Z and gives o = k_0 there. If the entire read domain lies in this band, the ladder for q ≥ k_0 is constant and B = 0. For an entire cleaned-collar domain, retain its inclusion in the source-controlled region and its (G-c) properties. Localisation “on” a collar does not by itself locate every read carrier. |
| K3: c_E = o | c_E = o is specified at CA-I 43365. The required full-domain inclusion (S) and old-collar geometry remain source properties. |
| K4: c_E = 𝖻 | c_E = 𝖻 is specified at CA-I 43366. Meeting Z''_k and Ω_k^old does not imply containment in their union, or in Y_4. Retain (S), both clauses of (G-c), and the actual tower matching. |
| K5 | It inherits the obligations of each constituent read, by CA-I 43367; it supplies no independent shortcut. |

The examples at CA-I 44995–45003 do not assert these inclusions for all classes. **Status of SRC: reduced to (S).** Lemma 7.1 proves SRC once (S) is supplied; the claimed all-consumer supply of (S) is still open. Both clauses of (G-c) remain separate premises on each actual read domain.

## 8. The gate's other written repairs, applied

In this section, “gate” means `gates/cr-gate.md`; the second-round amendments come from `gates/cr-r2-gate.md` §7. Line numbers “note n” refer to `cr-claude.md`.

1. **Lemma 5, q = 0 (gate §2).** Read the lower scale bound on N as max(η, ℓ_(q−1)). This only improves the estimate.
2. **Gauge step, note 166 (gate §4).** Replace the sentence by: "The norms |∂U − 1| and |J(U)| are gauge invariant (CA-I 42767-42768; J1, CA-I 42794)."
3. **Step-size sum, note 168-172 (gate §4).** For J' = p − n − 1, replace the display by
$$S\le C_{\rm RD}F\ell_n^2\Bigl[L^2+\mathbf 1_{J'\ge1}L^4+\sum_{j=2}^{J'}L^{j+3}2^{1-j}\Bigr]\le5L^{J'+3}C_{\rm RD}F\ell_n^2=5L^2C_{\rm RD}F\,\ell_n\ell_p .$$
For J' = 0 use L^2 ≤ 5L^3. For J' = 1 use L^2 + L^4 ≤ 5L^4. For J' ≥ 2 the geometric sum is at most 3L^(J'+3), and the first two terms cost at most 2L^(J'+3). With N_q of §6 the j-th term is unchanged, since e^(−δ_H w_*) ≤ (2L)^(−1) by (Phi-H*).
4. **Current step at n = 0 (gate §4).** Take ℓ = η, 𝖼 = 2B_3α_kℓ_q^2, ‖𝓗_q‖_η ≤ C_H′N_q and η^3|D*D𝓗_q(b)| ≤ C_H′N_q. CUR then gives |J(e^(iη𝓗_q)U^(q))(b) − J(U^(q))(b)| ≤ 2C_H′N_qη^(−3) ≤ 2L^3C_H′N_qℓ_n^(−3). For n ≥ 1 keep ℓ = ℓ_n/L ≥ η, as in the note. Retain the full incident-plaquette stencil for n ≥ 1.
5. **Corollary 9 (gate §4).** Use the floor 2L^2e^(−δ_H w_*) ≤ 1, which gives S ≤ 3L^4C_RD F ℓ_n^2. Add the ceiling 108L^10(C_H′)^2C_RD^2C_F^2α_k ≤ 1. Use the log(2L^2) version of (Phi-H*). The stronger floor implies its log(2L) version, so Theorem 8′ stays available. This gives the stated unit-scale estimates; it does not verify all consumer-radius comparisons.
6. **Remark at note 188 (gate §3).** Withdrawn. Lemma 5.1 replaces it.
7. **SRC wording (gate §3).** As in §7.
8. **Lemma 6 (gate §3).** Replaced by Lemma 6′ (§2.3).
9. **Lemma 4(b) and ROW (gate §2).** Replaced by Lemma 5.2 (§5).
10. **Lemma 7 (gate §2).** Source scope by Proposition 4.1 with its explicit source and tower qualifications. SEP by (SEP*) with (Phi-H*). Closed half polydisc by the radius margin of §4. The intermediate estimate is written without a free row variable (§6).
11. **The intermediate-level condition, note 149 (gate §4).** No consumer slot at each intermediate q is needed. CA-I 43055–43059 supplies a determining set at every level. Retain (R-form), the geometric hypotheses and R/T1 admission for **each** such set. Proposition 4.1 and Lemma 6′ apply only under these premises at every q, whether or not q is a slot level of E.

## 9. The repaired theorem and the order of constants

**Ceilings (8.1′).** Those of cr-claude (8.1), with n_P replaced by 2^d and C_RD F ≤ r_P replaced by C_RD C_F α_k ≤ C_1ε̄_1; also 2α_k ≤ ε̄_1, α_k ≤ c_av, and for Corollary 9 the ceiling of §8 item 5. Each is an upper bound on α_k by constants fixed before the couplings.

**Theorem 8′ (CR for SU(2), explicit conditional form).** Let G = SU(2). Assume:

- (i) the account's determining-set hypothesis (CA-I 43055–43059) and inputs T1; AV (c), (d), (e), with (d) at interface rows being the account's interface averaging hypothesis; CUR; AX; the composition grant COMP, including its clause COMP(=) (CA-I 44874, 44949-44953); R at regular real minimiser bases, the second case of `4.4:not-response-bound` (CA-I 10175-10204);
- (ii) Balaban's CMP 98 Proposition 6 in anchored form, P6, for rows of equal level;
- (iii) the readings (EC) (§2), (R-form) (§4) and (BP) (§5);
- (iv) for every actual consumer/read pair and every intermediate level: (G-c), (G-t) (§3), (R-form) (§4) and the scope (S) (§7), with the compatible block geometry and contour weights of (SEP*); retain both clauses of (G-c) and actual tower matching;
- (v) M_1 ≥ 2; the floors (Φ0)–(Φ2), the admissibility floor on M and the early tower inequality of §3 in the required distance, (Phi-H*) and (Φ_K); a positive uniform ε̄_1 in the admitted real-base class, with ε̄_1 ≤ a_1 and B_3ε̄_1 ≤ ε_0, and any further radius restrictions of the identified R source; the ceilings (8.1′).

Let E be a consumer with X' ∩ 𝒞 = ∅; no box is assumed. Let p be a slot level and X'' ⊂ X' a read domain. Then conclusions (a) and (b) of `4.12:prop-reblocking-inside` hold at (p, X''), with K_b = K_0M and K_0 = (π/3)(d−1)c_Qc_d(1+3L^2)·204. The constants are uniform in k, E, p, X'', its diameter, its number of blocks and its tower.

*Proof.* cr-claude Theorem 8, with these replacements: Lemma 4(b) by Lemma 5.2; ROW in Lemma 5 by COMP(=) and (BP); Lemma 6 by Lemma 6′; in Lemma 7, the coverage of R by Proposition 4.1, SEP by (SEP*) with (Phi-H*) and the polydisc by the radius margin of §4; SRC on X'' by Lemma 7.1; the step-size sum and the current step at n = 0 by §8 items 3-4. Under (S), AV(e), T1 and the two-layer scale give the exact existence parameter and both above-slot estimates (CA-I 44226–44303). For n < p, the clarified R coverage and (SEP*) with (Phi-H*) give the checked curvature/current iteration; the ceilings and absorption by Φ_K give the two below-slot constants (CA-I 44179–44185). The inherited calculations remain those checked by the previous gate, with these explicit substitutions (`gates/cr-r2-gate.md` §7). □

**Coverage of the outside proposition.** CA-I 45085 assumes X' ∩ 𝒞 = ∅, failure to fit in a healed box of side 204M, and {c_E < p} ∩ X'' ≠ ∅. Theorem 8′ does not use the box condition. K1 has no below-slot pair. For every actual read pair and every intermediate level, retain (S), (G-c), (G-t) and (R-form), together with the other premises of Theorem 8′. The class table does not establish these properties for all consumers. The theorem gives (a) and both cases of (b) conditionally; it does not prove the outside proposition from its printed hypotheses.

**Order of constants (second-round gate §8, verbatim).** The following order and qualification are copied from `gates/cr-r2-gate.md`, lines 173–178. Its §3 supplies the norm conversion retained in §3 above.

1. Fix `L` and the earlier construction parameters. Choose `M_1>=2` and the required gap parameters in their prescribed order. Then fix T1, AV, AX, P6, R and CUR constants, the admissibility threshold, and the response stencil/reference constant. Establish the tower part of admissibility here: `LM_1>w_adm`, or the norm-converted version in §3. This is an open part of (G-t), not something a later choice of `M` can fix.
2. Fix `C_F,C_RD,C_H',C_star,K_0` and `n_P=2^d`. Choose the next permitted `M` above the old floors, the admissibility floor, (Phi-H*) and `C_star/(3L^2 B_H K_0)`. These are finite one-sided lower bounds with earlier coefficients. For the stronger corollary use the `log(2L^2)` floor. If the admissibility distance is sup-distance and the width premises remain Euclidean, use `M>sqrt(d) w_adm` as well.
3. Fix a positive uniform `bar epsilon_1` in the admitted real-base class, with `bar epsilon_1<=a_1` and `B_3 bar epsilon_1<=epsilon_0`; set `r_P=2C_1 bar epsilon_1`. It must be fixed before the couplings and uniform over the pairs, not reselected at each rung. Independence from `M` is unnecessary; dependence on already chosen size parameters is allowed. Respect any further radius restrictions of the identified R source.
4. Choose `N_*` and the coupling ceiling for the account's Gamma conditions and (8.1′), including `2 alpha_k<=bar epsilon_1` and `C_RD C_F alpha_k<=r_P/2`. Add the Corollary 9 ceiling only when using that corollary. All coefficients are now fixed. CA-I 43618–43627 gives the stated uniform small-coupling choice.

Thus the additional `M` floors and coupling ceilings create no backward dependency, upper bound on `M`, or depth-dependent constant. This does **not** verify that the actual tower has sufficient width for the response theorem. In particular, if `w_adm` depends on `M_1`, increasing `M_1` cannot simply be assumed to make `LM_1>w_adm`; that relation needs its source identification.

## Result

The following final implication and open-premise table are copied verbatim from `gates/cr-r2-gate.md` §9, lines 182–199. Section references within this passage refer to that gate. This repair edit grants no status.

**As printed: REVISE. After the repairs written here: ADVANCE the conditional SU(2) implication. BLOCK unconditional identification with CA-I 45085.** The implication gives (a) and both cases of (b), with the account's `K_b`, uniformly in depth and read domain. It assumes the account's determining-set hypothesis and inputs T1, AV (including the interface hypothesis), R at real minimiser bases, CUR and AX. Those are cited inputs, not results discharged by this check.

The additional open premises are exactly these, with their scope made explicit:

| Premise | Remaining obligation |
|---|---|
| **(EC)** | Identify every plaquette used by AV(e) and T1 with the common-point, distinct-block class. Under it, the new proof supplies `n_P=16`. |
| **(R-form)** | Identify every intermediate ladder, with its tower, rows, averaging maps, reference conventions and regular real base, with R's source system. The false untruncated-shell explanation is removed. |
| **(BP)** | Common blocks have the same base points in the two ladders. |
| **(S)** | Every actual read domain lies wholly in `Y_4 intersect (Z union Omega_k^old)`. Under it, Lemma 7.1 supplies SRC. |
| **(G-c)** | All required consumer superlevel sets have the aligned big-block extensions and widths. Shell names and inside-box separation alone do not supply this for all outside pairs. |
| **(G-t)** | The actual tower has the aligned superlevel cubes and widths, with enough width in the response theorem's admissibility norm. Keep the early inequality specified in §§3 and 8. |
| **P6** | The anchored equal-level bound applies to the account's chosen averages and base points. SA 7265–7283 supports its form but is indexed as sketched; this check does not discharge the source identification. |
| **COMP, including COMP(=)** | The account's refinement-composition grant applies to these actual ladders and gives equality on common rows. It remains a grant. |

There is no separate ROW assumption after §4. There is no separate SEP assumption after the written repair (SEP*), which follows from (G-c), (G-t), the compatible block geometry and the specified contour weights. Its stronger floor is compatible with the account's order. This advances the conditional argument by supplying `n_P`, anchoring and SEP; it does not prove that every outside consumer satisfies the antecedent.

**Clause (c) and the real-factor corollary remain open.** Neither the original outside proposition nor Theorem 8′ exports (c). CA-I 44803–44843 requires the consumer-radius conclusion and identification of the real factors of all four composites on the relevant domains. The level-`k` restriction at CA-I 43437–43440 belongs to inside boxes and cannot be transferred to arbitrary outside domains. No repaired estimate here establishes those remaining comparisons or identifications.

## Change log — FINISH row 403

Applied at checkout `c3112412a83475881c5c19fab42e547c50537859`. Gate lines below refer to `gates/cr-r2-gate.md`, Git blob `bef9610e0cec1ec90c471984dd0bea79285a0d5e`. The pre-edit note is Git blob `e70aea6ac016af0bc483232513100c776945e2d6`. The inherited `cr-claude.md` and `cr-gate.md` match the revisions identified by that gate. Only `library/cr-r2.md` is edited; no prompt, registry, tree or status file changes. Verification here checks repair coverage and exact copied text, not mathematical discharge. The open obligations and next source-matching decisions are in the Result above.

| Gate line(s) | Repair applied |
|---|---|
| 7–13, 151, 165 | Update provenance and scope; distinguish the original check from this repair edit. |
| 11, 151 | Preserve credit while qualifying unavailable Balaban PDF quotations. |
| 17 | Make the circuit/source identification explicitly open. |
| 29 | Remove the unconditional “closed” heading. |
| 19 | Limit the cycle counterexample to what it excludes; remove the collar-topology claim. |
| 17, 21, 29 | Retain (EC) as an open antecedent; remove unsupported interface identification. |
| 23–29 | Expose the premises used by the repaired data-admission lemma. |
| 29 | State the conditional circuit-bound result without discharging (EC). |
| 35 | Correct the (G-c) width locator to CA-I 43520–43524 and the thin-shell/healed-region locator to CA-I 37559–37565. |
| 35 | Keep (G-c) widths and aligned extensions as separate open properties on every read domain; qualify CA-I 55632–55636 and the outline assertions. |
| 37 | Make actual-tower matching and its early LM_1 admissibility inequality explicit in (G-t). |
| 46 | State the Euclidean/sup-distance conversion and require both norm-converted inequalities when applicable. |
| 37–50, 160 | Qualify Proposition 4.1 by all source, tower, admission and intermediate-level premises. |
| 48 | Replace the false untruncated-shell explanation with the gate’s written (R-form) text. |
| 37–50 | Repair admissibility reasoning and keep the response formula as a cited input. |
| 50, 175 | Keep a uniform real-base radius chosen before couplings, allowing prior size dependence. |
| 50 | Specify the response derivative member and retain the uniform stencil/reference constant. |
| 39–50, 160 | Carry the complete conditional R coverage into its status statement. |
| 58, 153 | Distinguish removing broad ROW from retaining common-row equality. |
| 58 | Keep (BP) and COMP(=) as open readings/grants. |
| 54–58, 153 | State precisely which common-row premises remain. |
| 78 | Keep the admissible-contour metric distinct from ambient and CMP 122a distances. |
| 80–82 | Restrict the original stronger SEP argument to contours inside the read domain. |
| 82–124 | Remove the failed exterior extension; insert the gate’s SEP* proof verbatim, retaining the counterexample to the old inference. |
| 126–133 | Substitute w_* = M/(L+1) in N_q and the response estimate; preserve C_H′, the support supremum and the empty-support convention. |
| 133–141 | Replace the theorem and Corollary 9 floors by the two Phi-H* bounds. |
| 143, 197 | Retain the stronger confined-contour option only conditionally; state the repaired SEP antecedents. |
| 64, 74 | Remove inference of full-domain inclusion from level-function values or shell names; leave all-consumer (S) open. |
| 69 | Qualify K2 by whole-domain containment in B_5 or the source-controlled cleaned collar, retaining (G-c). |
| 70 | Retain K3 full-domain (S) and old-collar geometry as source properties. |
| 71 | Remove K4 containment inferred from meeting regions; retain (S), both (G-c) clauses and actual tower matching. |
| 72 | Make K5 inherit each constituent read’s obligations. |
| 156 | Propagate the repaired decay factor into the unchanged step-size sum. |
| 157 | Keep the full current stencil explicit at positive levels. |
| 158 | Use the stronger SEP* corollary floor and preserve the limit of the unit-scale conclusion. |
| 159 | Propagate qualified R coverage and SEP* into the replacement list. |
| 160 | Keep the intermediate-level quantifier and admission premises explicit. |
| 160, 182 | Include the determining-set hypothesis and real-base scope in Theorem 8′. |
| 37–50, 163–165 | Carry every pair/rung premise, norm-qualified floor and uniform radius into Theorem 8′. |
| 156–163 | Use the repaired response and separation hypotheses for both cases of the theorem. |
| 64–74, 164–165 | Remove the all-consumer source-discharge claim. |
| 169, 173 | Put M_1 and gap parameters before the determined variational constants; retain the early tower admissibility obligation. |
| 174 | Include Phi-H*, the admissibility floor and the absorption floor in the later choice of M. |
| 175 | Choose the positive uniform real-base radius after size parameters and before couplings. |
| 176 | Choose N_* and coupling ceilings after all their coefficients. |
| 178 | Keep tower-width matching open even when w_adm depends on M_1. |
| 165, 182 | Replace the old Result and suggested record with the verbatim conditional verdict and cited-input scope. |
| 184–195 | Copy the complete open-premise table verbatim. |
| 197 | Copy the absence of separate ROW/SEP premises and the conditional all-consumer limit verbatim. |
| 199 | Copy the open clause (c) and real-factor corollary scope verbatim. |
