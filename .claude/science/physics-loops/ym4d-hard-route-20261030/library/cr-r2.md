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

**Reading (EC).** A plaquette P of 𝕃(𝔅) is a closed circuit of 𝕃(𝔅) through pairwise distinct blocks whose closed cubes contain a common point of ℝ^d.

Support. (i) Balaban's elementary square of a level-j lattice is the circuit of the four level-j blocks around a common (d−2)-face, so it satisfies (EC). (ii) At an interface between levels m and m+1, the circuits around a common (d−2)-face piece have three or four blocks, and they satisfy (EC). (iii) T1's source condition, CMP 102 (7), reads only elementary squares, each with four factors (§2.1). (iv) Lemma 2.1 excludes long circuits. (EC) is the largest class with these properties that is fixed by local geometry. Any narrower reading (only the circuits around a (d−2)-face piece) is contained in it, so the bound below covers it too.

Blocks are identified with closed cubes. Level-m cubes are anchored at the origin and have side ℓ_m ∈ ηℤ, so their corners lie in ηℤ^d.

**Lemma 2.2 (n_P = 2^d).** Let Q_1, …, Q_r be distinct closed blocks of a determining set that contain a common point x. Then r ≤ 2^d. Hence every plaquette under (EC) has at most 2^d rows, uniformly in k, X, 𝔅, the level function and the tower.

*Proof.* For a sign vector s ∈ {±1}^d and small t > 0, let O_s(t) := {y : 0 < s_μ(y_μ − x_μ) < t for all μ}. This is an open set. Let Q_i = ∏_μ [a_μ, a_μ + ℓ] with x ∈ Q_i. For each μ, x_μ < a_μ + ℓ or x_μ > a_μ, since ℓ > 0. Put s_μ = +1 in the first case and −1 otherwise. Then O_s(t) ⊂ Q_i for t < ℓ. An open set inside a closed cube lies in its interior. The cubes of a partition have disjoint interiors, so two distinct Q_i cannot contain the same O_s(t). There are 2^d sign vectors. □

So for d = 4, n_P = 16, with no dependence on L.

### 2.3 Repaired Lemma 6

**Lemma 6′ (replaces Lemma 6 of cr-claude.md).** Assume (EC). Put
$$\varepsilon_1':=(2+2^dC_{\rm RD}C_FL^2)\,\alpha_k\ell_q^2$$
and assume ε_1′ ≤ a_1 and B_3ε_1′ ≤ ε_0. Then U^(q+1) = U(𝔅^(q), D_W)^τ for a gauge τ.

*Proof.* The proof of cr-claude Lemma 6 applies word for word, with n_P replaced by 2^d. The only change is in the data condition. Let P be a plaquette of 𝕃(𝔅^(q)) with base point z_0. By Lemma 5, D_W = (e^{iB}D_0)^v. The ordered product around P gives ∂D_W(P) = v(z_0) ∂(e^{iB}D_0)(P) v(z_0)^{−1}. For unitary factors, |∏_i e^{iB_i}g_i − ∏_i g_i| ≤ Σ_i |e^{iB_i} − 1| ≤ Σ_i |B_i|. P has at most 2^d rows by Lemma 2.2. Hence |∂D_W(P) − 1| ≤ |∂D_0(P) − 1| + 2^d sup|B| ≤ 2α_kℓ_q^2 + 2^dC_RD F ℓ_(q+1)^2 = ε_1′. Here the first bound is (e) with SRC, and ℓ(P) ≤ ℓ_q because every block of 𝔅^(q) has level at most q. □

In the ceilings (8.1), replace n_P by 2^d. The gate's conditional verdict on the rest of Lemma 6 (COMP gives the inclusion of the constraint manifolds; criticality restricts; the refinement keeps T1's threshold) is unchanged. **Status of n_P: discharged under the reading (EC).** (EC) is a reading of CA-I 42982, supported by CMP 98 p. 18, CMP 102 p. 278 and Lemma 2.1. It is not a hypothesis on the consumers.
