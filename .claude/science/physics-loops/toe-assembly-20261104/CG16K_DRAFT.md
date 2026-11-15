lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CG1-16-K: five neighbourhoods, the five dials as blocks of one-mode sites, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a scratch computation in `/tmp/toe-CG16K/`; one ran (section 2.3). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| this checkout, branch `claude/toe-assembly` | `15bc39079` |
| `origin/docs/consolidate-gauge-matter-registers` (read with `git show` only, after `git fetch -q`) | `7086189d1` |

**Files read, by line.** This folder, at `15bc39079`: `prior/CG16K.md` lines 1-94 (all); `TOE_ASSEMBLY.md` lines 13-24 (axioms), 120-135 (PS-5, PS-6), 201-250 (sections 3.4-3.8), 375-395 (MT1), 436-455 (CG1); `LW1_5.md` lines 1-20 (status), 32-139 (definitions, the two laws, C, C2, M, Q and G, R), 140-202 (U, S′, alternative A, F and K, mixed registers, SC, Σ), 258-275 (section 7, B1-U); `LW1.md` lines 7, 13, 30, 43, 72, 118-126, 209, 247, 401 (found by grep); `B5B.md` lines 5, 82, 103, 121, 129, 139 (found by grep); `ZM1.md` lines 5, 9, 12, 18, 49-59, 71-72, 243, 311, 319, 325, 347, 357, 359, 363, 370 (grep hits, read as printed); `Y2W_DRAFT.md` lines 1-30 (format only). Branch `origin/docs/consolidate-gauge-matter-registers`, folder `docs/`: `FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md` (#10014) lines 1-40 and 100-201; `SPIN10_MOTT_SITES_CARRY_NO_COMPOSITE_SIXTEEN_THE_CENTRE_FIXES_EVERY_FERMION_TO_THE_VECTOR_CLASS_BOUNDED_THEOREM_NOTE_2026-10-22.md` (#10027) lines 120-142; `GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` (below "G") lines 244-290 and 1133-1141 and the table rows at lines 1192-1204 (read), and grep hits at lines 21, 153, 590, 691-725, 979 and 987.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms and owner decisions are read plainly. Where a reading is needed, it is written as a candidate and four-tested (section 9).

**Working set used, by name.** Lattice, Qubit and Admissibility, as quoted in `TOE_ASSEMBLY.md` section 1.1. PS-1c (covariance read on cells; `LW1_5.md` lines 59-60). PS-5 in its fallback text (section 3.4) only as the comparison case. PS-6 and PS-6r. GA1-P-NN = NN-a (owner, 2026-11-06, section 3.7), read at the fine scale with one mode per site, as the lane brief directs. The two live five-mode laws `L5-U[m]` and `L5-O[S_+]` (`LW1_5.md` section 2; owner 2026-11-05, both live). ZM1-I1[a] (section 3.8) only to say where it does and does not enter. Results used, cited by name and path: `LW1_5.md` C, C2, M and M.1, Q and G, R, U, F and K, SC, B1-U and A2-5; `LW1.md` A2 and E1; `B5B.md` Theorems 3.1 and 3.3; `ZM1.md` Theorem Z3 (scope only).

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: the commutant of the proper cubic group in real `3 × 3` matrices (Lemma 4.2) and a covolume count (Theorem 4.3); orbit sizes of the proper cubic group on points of `R^3` (Lemma 4.1); characters of the proper cubic group `O` (Lemma 7.1); isotypic components and commutants (Lemma 7.2); Lie-algebra generation by Majorana monomials (Lemma 5.3); generation of a connected matrix group by one-parameter subgroups whose generators span its Lie algebra under brackets (Lemma 5.4, via the inverse function theorem). Literature is in section 2; no citation is load-bearing.

---

## 0. The question, quoted

The lane brief: decide whether five dials can be "(a) five spatially separate neighbourhoods (blocks) of sites, or (b) five collective modes of one O_h-symmetric block (decompose the block mode space into O_h irreps and ask which 5-dimensional invariant subspaces exist without a choice), such that some local, covariant, finite-register law on one-mode sites (NN-a at the fine scale) has an exact Spin(10) or U(5) frame group acting on those five modes at the block scale, or an emergent one in the sense of ZM1 zoom (ZM1-I1[a]) with the protection #10014 asks for." Also: "Check whether the orbit-size and Schur obstructions are scale-free (apply equally to blocks), and say exactly which step a block construction escapes or fails. Compare with the 7-star (Spin(14)) and 27-cube options of #10014."

The owner idea, verbatim from the brief (2026-11-07): "what about 5 blocks of sites then - 5 neighborhoods".

The obstructions under test, quoted from #10014 (lines 120-155):
- (O-1) "Point-group orbits around a site have sizes 1, 6, 8, 12, 24. Around any other centre all orbits are even. So no 5-site cluster is O_h-symmetric".
- (O-2) "The best 5-site tiling keeps 8/48: lopsided by 2.6 bits." Its search limits (line 200): "lattice tilings only; clusters within a 3^3 box; covariant blocks with index <= 30 and orbit radius^2 <= 9."
- (W5) "By Schur, the only Spin(2N)-invariant coupling between two clusters' Majorana vectors is the identity (W5). The hop must therefore be mode-diagonal, with displacement in the tiling lattice L." Then: "Nearest-neighbour hops on all three axes need e1, e2, e3 in L, which means L = Z^3 and N = 1."
- (W6) "A gauge-covariant hop would need K(5,5) of nearest-neighbour bonds, which is impossible (W6). Two sites share at most 2 neighbours."
- (E) "So Spin(10) on a spread cluster can be at most emergent. Protection by an approximate symmetry is the tuned smallness that M4 forbids."
- The open door: "unless a coarse-rung rule makes a cluster the "site" and redefines "neighbour" at that rung. That rule would still have to pick a lopsided 5-tiling (at best 8/48) with no reason."

The fine-scale gate rule, quoted from `TOE_ASSEMBLY.md` section 3.7 (NN-a): "A nearest-neighbour gate `g` is a unitary supported within `F_x`, `F_y` and `H_ℓ`, where `ℓ=(x,y)` and `y=x+e_i`. It acts identically outside those factors. Evenness means `[g,P_xP_y]=0` ... The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s` ... Gauge invariance and cell covariance are required of the complete update only." Here `F_x` is the one-mode site, `ΛC^1 = C^2`.

## 1. Prior work used

The digest `prior/CG16K.md` is written for the 16 question as a whole. Its one entry on clusters is the failed attempt "Build exact Spin(10) from spread one-mode clusters", with failing step "no nearest-neighbour inter-cluster coupling keeps Spin(2N>2) exact" (`G:590`). This file does not repeat that attempt. **The new step is the owner's NN-a decision of 2026-11-06** (`TOE_ASSEMBLY.md` section 3.7), which postdates #10014: gates need not be gauge invariant one by one. Section 5 shows that this step changes the answer.

Prior results used or extended, with paths (`G` = `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` on `origin/docs/consolidate-gauge-matter-registers`; `T/` = this folder):

1. **#10014** (`docs/FIVE_MODES_PER_SITE_..._2026-10-22.md`, lines 115-170; summary `G:590`, `G:691-725`). The obstructions O-1, O-2, W5, W6, E and the 7-star and 27-cube options. Section 4 tests each for scale-freeness. Section 8 compares the options.
2. **#9926** (`G:244-272`), **not in the digest**. Link registers built from one-mode fermion sites at the bond ends (rishons) give "an exact continuous U(1) (and exact SU(3) with the det term) on finitely many levels". The placement at block side `b = 3`: "with matter at the block centre and rishons at the six face centres, each axis reads matter(0)-rishon(1)-rishon(2)-matter(3) on adjacent fine sites, so the gauge-invariant hop is the product of two nearest-neighbour bilinears (psi_0^+ c_1)(c_2^+ psi_3), a 4-site line gate." Its boundary: "Supplied: the role assignment of fine sites (matter versus rishon)". This is the closest prior construction: an exact non-abelian gauge group on one-mode fine sites, by a supplied design. Section 5 extends it from SU(3) to U(5) and Spin(10), with collective dial modes, under NN-a.
3. **#10026** (`G:1199`), **not in the digest**. "every site orbit carries A1 exactly once"; "Schur-protected multiplets of a composite cluster can carry only SU(2) and SU(3) simple factors"; at `b = 5` the per-cluster algebra is "abelian once generic C4v-covariant matter-end pieces are added"; "No gauge group is forced by the update". Used in section 7 (the A1 count) and section 9 (what a block law supplies rather than derives).
4. **#10015** (`G:1195`), **not in the digest**. "No W(B4)-covariant cluster has 5 sites"; "Lattice covariance alone never protects a non-abelian internal frame built from one-mode sites." Section 5's frames are protected by the law's gauge structure, not by lattice covariance, so they are consistent with this.
5. **#10019** (`G:1197`), **not in the digest**. "The 2d half-link patterns of a site decompose under the cubic group as 1 + (d-1) + d, which is 1 + 2 + 3 at d = 3"; "But the labels turn with space"; "The Lee-sphere tiling by 7-site stars keeps only a C3." Used in sections 6-8.
6. **#10029** (`G:1200`), **not in the digest**. "the half-link 5 = E + T1"; "An emergent Spin(10) of free Weyl modes is always part of an emergent U(16)." Used in sections 7-8.
7. **#9894**, as corrected in `G:1134-1135`, **not in the digest**. For the plain corner action of a cube, "the rotation-invariant five-dimensional subspace A1 + A2 + T1"; "equal masses on T1 + A1 + A2, which give an exact SO(10) on that register, are a supplied choice." Used in section 7 (the `2^3` cube).
8. **#10039** (`G:1141`, `G:1203`), **not in the digest**. "7-site stars at 3Z^3" carry a fermionic charge "with all 24 rotations, through a non-monomial star-local gauge". A precedent for star blocks at `3Z^3` (section 8).
9. **#9953** (`G:1192`), **not in the digest**. "one spin-S register shared by every fine bond crossing a coarse face, with hops inside a block undressed, keeps the coarse Gauss law exactly". A precedent for registers at the block scale.
10. **#10027** (lines 120-142 of its note; `G:979-987`), with routes 1 and 2 tested in **#10038** and **#10045** (`G:1202`, `G:1204`). The centre theorem and its three routes. Section 8 shows that the block route inherits it unchanged.
11. **`T/LW1_5.md`** (frozen): C and C1, C2, M and M.1, Q and G, R, U, F and K, SC, B1-U, A2-5, S′ and alternative A. Section 5 transfers these to the dial algebra by an isomorphism; nothing is re-derived.
12. **`T/LW1.md`** (frozen): A2 (the cell group `𝒢 = 2Z^3 ⋊ O_{c_0}`; "a site's stabilizer has three elements") and E1 (infinite gate products as local automorphisms).
13. **`T/B5B.md`** (frozen): Theorems 3.1 and 3.3. Under the split-register hypotheses, frames on cells of `L_cube` act by site phases; "The mode image is `U(1)^8`" (`TOE_ASSEMBLY.md` section 3.4). These are statements about the law `L_cube`. Section 5 builds a different law; it does not contradict them.
14. **`T/ZM1.md`** (frozen): Definition Z, Theorem Z3 and its scope paragraph (line 359). Used in section 8.4 to locate the block route relative to the zoom.

Prior work the digest missed, added here: items 2-9.

## 2. Literature

### 2.1 Fetched and used as context

Each entry gives what was fetched and the line relied on. None is load-bearing: every step below is proved in this file.

1. S. Bravyi, A. Kitaev, "Fermionic quantum computation", arXiv:quant-ph/0003137, Ann. Phys. 298 (2002) 210-226. Abstract page and ar5iv text fetched. Section 2: "Physical operators are those which preserve the parity." Section 4: "We claim that the following gates are sufficient to represent any parity-preserving operator" (their Eq. (9)), closing with "We have proved that the gate set (9) is universal in the class of parity-preserving operators." Their proof is explicit, through a homomorphism from a universal qubit gate set (their Eq. (10)). Lemmas 5.3-5.4 below prove a variant natively: nearest-neighbour gates on a connected set of one-mode sites, with link registers attached. The route is different (Lie algebra plus the inverse function theorem).
2. D. Banerjee, M. Bögli, M. Dalmonte, E. Rico, P. Stebler, U.-J. Wiese, P. Zoller, "Atomic Quantum Simulation of U(N) and SU(N) Non-Abelian Lattice Gauge Theories", arXiv:1211.2242, Phys. Rev. Lett. 110 (2013) 125303. Abstract page and ar5iv text fetched. Their Eq. (3) writes the U(N) link as a rishon bilinear; "The rishon number is conserved locally on each link."; supplementary text: "both "quarks" and rishons are represented by the same fermionic atoms that hop between the sites of an optical lattice." This is the register form of `L5-U` (`LW1_5.md` line 94, `U_ℓ^{jk}=r^y_jr^{x†}_k`) and of #9926.
3. S. Chandrasekharan, U.-J. Wiese, "Quantum Link Models: A Discrete Approach to Gauge Theories", arXiv:hep-lat/9609042, Nucl. Phys. B 492 (1997) 455-474. Abstract page fetched: link variables are non-commuting operators on finite registers. Context for PS-6r.
4. E. Zohar, A. Farace, B. Reznik, J. I. Cirac, "Digital lattice gauge theories", arXiv:1607.08121, Phys. Rev. A 95 (2017) 023604. Abstract page and ar5iv text (first half) fetched. Introduction: "We will show how to build individual time steps that respect local gauge invariance". Their elementary operations use an auxiliary control; Sec. II.2.1, Eq. (44): the stator is undone so that "the auxiliary system is back in its initial state." Context: gauge-invariant steps compiled from few-body operations. Section 5 uses no auxiliary system and asks invariance of the complete update only, as NN-a states.
5. I. D. Kivlichan et al., "Quantum Simulation of Electronic Structure with Linear Depth and Connectivity", arXiv:1711.04789, Phys. Rev. Lett. 120 (2018) 110501. Abstract page fetched: a "fermionic swap network" runs a Trotter step on a linearly connected architecture. Context for routing modes by nearest-neighbour fermionic swaps (Lemma 5.3).
6. J. C. Halimeh, L. Homeier, A. Bohrdt, F. Grusdt, "Spin exchange-enabled quantum simulator for large-scale non-Abelian gauge theories", arXiv:2305.06373, PRX Quantum 5 (2024) 030358. Abstract page fetched: "enabled by two-body spin-exchange interactions realizing local emergent gauge-symmetry stabilizer terms." Context for the emergent (energetically protected) alternative, which section 8.4 contrasts with exact frames.
7. J. C. Baez, J. Huerta, "The Algebra of Grand Unified Theories", arXiv:0904.1556, Bull. Amer. Math. Soc. 47 (2010) 483-552. ar5iv text fetched. Section 3.2: "Λℂⁿ becomes a representation of Spin(2n), called the Dirac spinor representation"; the even and odd parts are "called left- and right-handed Weyl spinors, respectively." Context for the reading of the 16 as `Λ^{ev}C^5`.

### 2.2 Searched, not verified or not used

- D. Deutsch, A. Barenco, A. Ekert, "Universality in Quantum Computation", arXiv:quant-ph/9505018 (Proc. R. Soc. A, 1995). Abstract page found: "almost every gate that operates on two or more bits is a universal gate". The text of its Lie-algebra argument was **NOT VERIFIED**. Lemma 5.4 is proved natively and does not use it.
- J. H. Conway, E. M. Rains, N. J. A. Sloane, "On the existence of similar sublattices", arXiv:math/0207177 (Canad. J. Math. 51 (1999)). Found; no statement about cubic-invariant sublattices of `Z^3` was located. Not used; Lemma 4.2 is proved natively.
- F. Wilczek, A. Zee, "Families from spinors", Phys. Rev. D 25 (1982) 553: the reading #10014 calls "the Wilczek-Zee reading of Lambda(C^N)". **NOT VERIFIED** (not fetched). Not used.
- S. W. Golomb, L. R. Welch (perfect Lee codes), cited by #10014: **NOT VERIFIED**, not used.
- No fetched work states the scale-free index obstruction of section 4.2, or compiles U(5) or Spin(10) frames onto one-mode sites. This is a search result, not a claim of novelty.

### 2.3 Numerical checks

One guide check ran, after the proofs. At first `memory_pressure` reported "System-wide memory free percentage: 47%", below the 50 % rule, so the character computations of section 7 were done by hand first. Later it reported 55 %, and `check_iso.py` (in `/tmp/toe-CG16K/`, output `out_iso.txt`, under one second, a few MB, exact rational arithmetic) computed the `O` and `O_h` isotypic multiplicities of the six blocks of table 7.2 by averaging fixed-point counts against the character table. [check] It reproduces every entry of table 7.2, including the `O_h` rows for `4^3` and `5^3`. It guides; it proves nothing.

## 3. Setting and definitions

**3.1 Groups.** `O` is the group of determinant-one signed coordinate permutations, of order 24 (`LW1.md` line 43). `O_h = O × {±1}` has order 48. For a point `c` with all coordinates in `Z` or all in `Z + 1/2`, `O_c` is the set of maps `x ↦ c + Q(x−c)`, `Q ∈ O`; these preserve `Z^3`. A **cell group** is `G = Λ ⋊ O_c`, with `Λ` a finite-index sublattice of `Z^3` and `QΛ = Λ` for all `Q ∈ O`. PS-1c reads covariance on `𝒢 = 2Z^3 ⋊ O_{c_0}`, `c_0` a cube centre. The **linear part** of `x ↦ c + Q(x−c) + λ` is `Q`.

**3.2 Fine algebra.** Each site `x ∈ Z^3` carries one CAR mode `c_x`. For finitely supported `f ∈ ℓ^2(Z^3)` put `c^†(f) = Σ_x f(x) c_x^†` and `c(f) = c^†(f)^*`. Then `{c(f), c^†(g)} = ⟨f, g⟩`. For a subspace `V ⊆ ℓ^2(Z^3)`, `CAR(V)` is the C*-algebra generated by the `c(f)`, `f ∈ V`. Link registers are finite-dimensional ordinary tensor factors on chosen fine links; they commute with matter, as in `LW1_5.md` line 40. Write `𝔄` for the quasi-local algebra of matter and registers (`LW1.md` E1). A lattice map `g` acts on functions by `(g·f)(y) = f(g^{-1}y)`.

**3.3 Blocks and dials.** A **block structure** for a cell group `G` is the following data.
- A `G`-set `𝒳` of coarse sites. For each `X ∈ 𝒳`, a finite site set `supp X ⊂ Z^3`; the sets are pairwise disjoint and `g(supp X) = supp(gX)`.
- For each `X`, a five-dimensional subspace `V_X ⊆ ℓ^2(supp X)`, **the dials of `X`**, with `g·V_X = V_{gX}`.
- A **coarse cubic structure**: a bijection `κ: 𝒳 → Z^3` and a homomorphism `π: G → Z^3 ⋊ O_h` with `κ(gX) = π(g)κ(X)`, whose linear parts contain `O`. Coarse neighbours are pairs with `κ`-images at distance one.

Put `W = (⊕_X V_X)^⊥`, the **non-dial modes**. A site in no `supp X` is a **spectator**. Option (a) of the brief is the case where `V_X` has a basis of five vectors with pairwise disjoint supports `B_{X,1}, …, B_{X,5}` (five neighbourhoods); in option (a) the neighbourhoods are part of the data, and `G` maps neighbourhoods to neighbourhoods. They are **spatially separate** when the five centroids are distinct. Option (b) is the case where `V_X` is canonical (3.6) for the point group of `supp X`.

**3.4 Dial frames.** A **dial frame** at `X` is an automorphism of `𝔄` that maps `CAR(V_X)` onto itself and fixes `CAR(V_Y)` for every `Y ≠ X`, `CAR(W)`, and every register. This is `LW1_5.md`'s site frame (line 40, from B5B Definition F) with the site algebra replaced by the dial algebra. A **register change** is conjugation by a unitary on finitely many registers. A frame is **compatible** with a unitary `u` of `𝔄` if some register change `ρ` gives `(ρ∘φ)(u) = u`. The **Bogoliubov action** of `U(V_X) ≅ U(5)` sends `c^†(f) ↦ c^†(uf)` for `f ∈ V_X` and fixes `CAR(V_X^⊥)`. The ten Majoranas of `V_X` span a real space of dimension ten; `SO(10)` acts on it, and `Spin(10)` acts through `SO(10)` by automorphisms (`LW1_5.md` C).

**3.5 The law class.** A **fine block law** is a law with these properties.
1. One mode per fine site; finite registers on some fine links (the trivial register `C` is allowed).
2. NN-a at the fine scale: the update is a product of a fixed finite number of layers; each layer is a locally finite product of even unitaries, each supported on `F_x ⊗ F_y ⊗ H_ℓ` for a fine link `ℓ = (x, y)`, on pairwise disjoint edge triples.
3. Cell covariance: the update automorphism commutes with lifts `β_g`, `g ∈ G`. A lift sends `c_x ↦ θ_g(x) c_{gx}` with `|θ_g(x)| = 1`, and maps the register of `ℓ` onto the register of `gℓ` ("lifted by diagonal phases", `LW1.md` line 43). Superlattice cell groups are allowed; transitivity on fine sites, which PS-1c also asks, is not imposed here (section 5.4 shows what it costs).
4. Gauge: the update fixes each **block gauge generator**: the generator of the dial-frame action at `X` plus its register parts.
5. Movement: the update moves dials between coarse neighbours. Precisely, a coarse gate has faithful one-mode inflow at each coarse site in the sense of `LW1_5.md` M, read on the dial algebra.

The group `G_X` of dial frames at `X` compatible with the complete update is **the frame group at the block scale**. "Exact" means compatibility holds as an identity, at every angle. "Gate-wise at the coarse rung" means compatibility with each **coarse gate**, which in the fine law is a fixed finite product of fine layers.

**3.6 Canonical subspaces.** Let a finite group `H` act unitarily on a finite-dimensional space `E`. A subspace `V ⊆ E` is **canonical** if every element of `H` and every unitary on `E` commuting with `H` maps `V` onto itself. It is the formal content of "without a choice" in the brief. Lemma 7.2 shows that `V` is canonical exactly when it is a sum of `H`-isotypic components.

## 4. Scale-free obstructions: orbits, index, Schur

### 4.1 Orbits (O-1)

**Lemma 4.1 (orbit sizes).** Let `O` act on `R^3` by rotations about a point `c`. For `p ∈ R^3` the orbit `O·p` has size 1, 6, 8, 12 or 24, and size 1 exactly when `p = c`.

*Proof.* A rotation that fixes `c` and a point `p ≠ c` fixes the line through them pointwise, so it is a rotation about that line. The rotations of `O` about one line form a cyclic group. The rotation axes of `O` are the three coordinate axes (four rotations each, counting the identity), the four body diagonals (three each) and the six face diagonals (two each). Every other line carries only the identity. So the stabilizer of `p ≠ c` has order 4, 3, 2 or 1, and the orbit has size 24 divided by that order. ∎

**Corollary 4.1a.** No set of five distinct points of `R^3` is invariant under `O_c`.

*Proof.* The set is a union of orbits. At most one orbit, `{c}`, has odd size one. Neither 5 nor 4 is a sum of numbers from `{6, 8, 12, 24}`. ∎

The corollary is **scale-free**. It uses only that the five objects have distinct centroids and that isometries map centroids to centroids. So five spatially separate blocks cannot be permuted by a stabilizer that contains all of `O`. Whether this obstructs a block structure depends on the cell group. For PS-1c's cell group `2Z^3 ⋊ O_{c_0}`, "a site's stabilizer has three elements" (`LW1.md` A2, line 209). Its coarse sites are never fixed by all of `O`. Section 6 uses this escape.

### 4.2 The index theorem (O-2, strengthened)

**Lemma 4.2 (commutant of `O`).** A real `3 × 3` matrix `M` with `MQ = QM` for every `Q ∈ O` is a multiple of the identity.

*Proof.* The matrices `diag(−1,1,−1)`, `diag(1,−1,−1)` and `diag(−1,−1,1)` lie in `O`. For `a ≠ b` one of them has `−1` at `a` and `+1` at `b`; commuting with it gives `M_{ab} = −M_{ab}`, so `M` is diagonal. The cyclic coordinate permutation lies in `O` and makes the diagonal entries equal. ∎

**Theorem 4.3 (index; scale-free).** Let `G = Λ ⋊ O_c` be a cell group and take a block structure for `G` with a coarse cubic structure (3.3). Let `T ⊆ Λ` be the translations whose `π`-image has trivial linear part. Then the number of fine sites per coarse site,
`k_eff = [Z^3 : T] / |𝒳/T|`,
is the cube of a positive rational number, and a perfect cube when it is an integer. In particular `k_eff ∉ {5, 7, 16}`, and every coarse site has at least `k_eff − 5 ≥ 3` non-dial fine modes, inside its block or among spectators.

*Proof.* Write `Ψ(g) ∈ O_h` for the linear part of `π(g)`. `Ψ|_Λ` maps into a finite group, so `T = Λ ∩ ker Ψ` has finite index in `Λ`. Let `g ∈ G` have linear part `Q`. For `t ∈ T`, `gtg^{-1}` is the translation by `Qt`, and `Ψ(gtg^{-1}) = 1`, so `QT = T`. For `t ∈ T`, `π(t)` is the translation by a vector `τ(t)`, and `τ` is additive. It is injective: if `π(t)` is the identity, `t` maps each finite set `supp X` onto itself, and a nonzero translation fixes no nonempty finite set. Conjugating, `π(gtg^{-1})` is the translation by `Ψ(g)τ(t)`, so `τ(Qt) = Ψ(g)τ(t)`. Extend `τ` linearly to an invertible rational matrix `τ_Q`; then `τ_Q Q = Ψ(g)τ_Q`. Since `Ψ(g)` is orthogonal, `M = τ_Q^T τ_Q` satisfies `Q^T M Q = (Ψ(g)τ_Q)^T (Ψ(g)τ_Q) = M` for every `Q ∈ O`. By Lemma 4.2, `M = μ·1`, with `μ = |τ_Q e_1|^2` a positive rational. Hence `|det τ_Q| = μ^{3/2}`. Comparing covolumes, `|𝒳/T| = [Z^3 : τ(T)] = μ^{3/2}[Z^3 : T]`; the first equality holds because `κ` carries `T`-orbits on `𝒳` to `π(T)`-orbits on `Z^3`. So `k_eff = μ^{−3/2}`. It is a ratio of integers, so `√μ = μ^{3/2}/μ` is rational and `k_eff = s^3` with `s = 1/√μ`. If `k_eff` is an integer, write `s = u/v` in lowest terms; `v^3` divides `u^3`, so `v = 1`.
For the last claim, `T` acts freely on fine sites and on `𝒳`. For representatives `X_1, …, X_N` of `𝒳/T`, distinct sites of `∪_i supp X_i` lie in distinct `T`-orbits: if `y ∈ supp X_i` and `ty ∈ supp X_j`, then `supp(tX_i)` meets `supp X_j`, so `tX_i = X_j` by disjointness, hence `i = j` and `t = 0`. So `5N ≤ Σ_i |supp X_i| ≤ [Z^3 : T]`, that is `k_eff ≥ 5`. The smallest cube that is at least 5 is 8. ∎

The proof uses only that the fine cell group contains all of `O` and that `G` acts on the coarse lattice by isometries.

**What this proves about O-2.** #10014 searched "lattice tilings only" and found that "The best 5-site tiling keeps 8/48"; it also lists "Fully O_h-covariant tiling blocks up to size 30 have sizes 8, 16, 27." Theorem 4.3 removes the search limits and adds a constraint. If the coarse sites form a simple cubic lattice on which the cell group acts by isometries, the number of fine sites per coarse site is a perfect cube. So no partition of `Z^3` into five-site units, of any shapes and by any tiling, lattice or not, has this structure. The same holds for 7-site units; this strengthens #10014's "each such tiling keeps at most 6/48" and #10019's "The Lee-sphere tiling by 7-site stars keeps only a C3". Size 16 is excluded as well, so #10014's 16-site blocks do not carry a simple cubic coarse lattice of this kind. The theorem is **scale-free**: the fine units may be sites or blocks (Corollary 6.2). **What a block construction does with it:** it keeps non-dial modes. Theorem 4.3 does not forbid five dials; it forbids five dials being all the fine modes.

### 4.3 The Schur step (W5) and the bond graph (W6)

**Lemma 4.4 (Schur, scale-free).** Let `n ≥ 3` and let `M` be a real `n × n` matrix with `RM = MR` for every `R ∈ SO(n)`. Then `M = k·1`. Likewise a complex `N × N` matrix commuting with `U(N)` is scalar.

*Proof.* For `a ≠ b` choose `c ∉ {a, b}` and let `D` be the diagonal matrix with `−1` at `a` and `c` and `+1` elsewhere; `D ∈ SO(n)`. Then `(DM)_{ab} = −M_{ab}` and `(MD)_{ab} = M_{ab}`, so `M_{ab} = 0`. A signed permutation matrix of determinant one that swaps `a` and `b` then gives `M_{aa} = M_{bb}`. The unitary case is the same argument with diagonal phases and permutation matrices. ∎

So W5's first sentence holds for blocks: an invariant coupling between two blocks' dials under one common `Spin(10)` or `U(5)` is mode-diagonal. Its second step, "Nearest-neighbour hops on all three axes need e1, e2, e3 in L, which means L = Z^3 and N = 1", uses three further facts: each mode sits on one site, the clusters are translates of one another, and the coupling is one layer of nearest-neighbour bilinear terms. Under NN-a the third fails for every law of section 5. For collective dials the first fails too, and in Example 6.3 the second fails. A dial is a vector in `ℓ^2(supp X)`; the mode-diagonal coupling `Σ_j c^†_{Y,j} c_{X,j}` has the fine kernel `Σ_j φ_{Y,j} ⊗ \overline{φ_{X,j}}`, which is not nearest-neighbour; and NN-a lets its exponential be a product of nearest-neighbour gates (section 5). This step is **not scale-free**. It is the step the block construction escapes.

W6 ("A gauge-covariant hop would need K(5,5) of nearest-neighbour bonds") treats the gauged hop `Σ_{ab} γ^X_a U^{ab} γ^Y_b` as a sum of terms, each on one fine bond, that is invariant as a sum of one-bond terms. That is a per-gate invariance requirement, the alternative NN-b that the owner did not choose. The graph fact ("Two sites share at most 2 neighbours") is true and scale-free, but under NN-a nothing uses it. The conclusion E, "Spin(10) on a spread cluster can be at most emergent", rests on the second step of W5 and on W6. Theorem 5.1 shows it fails for NN-a laws.

| #10014 step | Scale-free? | Block construction |
|---|---|---|
| O-1, one cluster | yes (Cor. 4.1a) | escapes: PS-1c's coarse stabilizers have order 3; or dials are collective modes |
| O-2, tilings | yes, and stronger: fine sites per coarse site is a perfect cube (Thm 4.3) | forces at least 3 non-dial modes per coarse site; does not forbid five dials |
| W5, Schur | yes (Lemma 4.4) | harmless: the coarse hop is mode-diagonal at the coarse rung |
| W5, "N = 1" | no | escapes: dials are not single sites, and NN-a compiles the hop |
| W6, K(5,5) | graph fact yes; its use needs per-gate invariance | escapes under NN-a |
| E, "at most emergent" | follows from the two rows above | fails for NN-a laws (Theorem 5.1) |

## 5. The compilation theorem: exact frames at the block scale

### 5.1 Statement

Fix a coarse law `α_c`: the base tick `U_0 = W_E M_o M_e` of `L5-U[m]` or of `L5-O[S_+]` (`LW1_5.md` section 2), with any free data `ε, μ, τ_E`. A supplied plaquette layer is allowed if it is a finite-depth layer of gauge-invariant gates on coarse plaquettes. The coarse cell group is `𝒢 = 2Z^3 ⋊ O_{c_0}` with the lifts of B1-U and A2-5.

**Hypotheses on the block structure** (3.3), for a fine cell group `G` with `π: G → 𝒢` an isomorphism:
- (B0) *Translations.* `π` maps the translations of `G` onto the translations `2Z^3` of `𝒢`.
- (B1) *Equivariant dial bases.* Each `V_X` has an orthonormal basis `φ_{X,1}, …, φ_{X,5}` with `g·φ_{X,j} = φ_{gX,j}` for all `g ∈ G`. Equivalently, each `φ_{X_0,j}` is fixed by the stabilizer `G_{X_0}`, for one representative `X_0` per `G`-orbit, and the bases elsewhere are transported.
- (B2) *Bridges.* Each coarse link `ℓ` is assigned a fine link `b(ℓ)`, with `b(gℓ) = g·b(ℓ)` as unoriented links. For each coarse cube `C`, the union `S(C)` of the blocks of its eight coarse sites and of fine paths through the bridges of its twelve links is connected in the fine nearest-neighbour graph, and contains at least three sites. For two cubes of the same tiling, `S(C) ∩ S(C') = ∅`.

**Theorem 5.1 (compilation).** Under (B0)-(B2) there is a fine block law `α_f` (3.5) with these properties.
1. *It is the coarse law.* Let `ι` be the embedding `c_{X,j} ↦ c(φ_{X,j})` on matter and the identity from each coarse register to the register placed on its bridge. Then `α_f∘ι = ι∘α_c` on the coarse algebra, and `α_f` acts on `CAR(W)` by a chosen covariant dynamics that commutes with `ι` of the coarse algebra (the identity, or the walk of Remark 5.6).
2. *NN-a.* `α_f` is a product of a fixed finite number of fine layers of even nearest-neighbour gates on disjoint edge triples. Registers sit only on bridges.
3. *Covariance.* `α_f` commutes with the lifts `β_g` that send `c_x ↦ θ_g(X) c_{gx}` for `x ∈ supp X`, send `c_x ↦ c_{gx}` for spectators, and act on bridge registers by the coarse register lift of B1-U (rishon flavour permutation) or A2-5 (the Spin(20) lift on reversed links). Here `θ_g(X) = ±1` is the sign of the coarse lift at `X`: `d_g(gX)` of B1-U, built from `LW1.md` A2, or for `L5-O` the sign lift of A2-5 ("Site parity implements LW1's sign lift").
4. *Exact frames.* For `L5-U[m]`, every Bogoliubov dial frame of `U(V_X) ≅ U(5)`, with the corresponding register change of `LW1_5.md` U, is compatible with each coarse gate and with `α_f`, at every angle. For `L5-O[S_+]`, the same holds for the `SO(10)` action on the ten dial Majoranas, implemented by `Spin(10)` with the register change of Q and G.
5. *Upper bounds.* A dial frame compatible with each coarse gate is Bogoliubov on `V_X`. It lies in `U(5)` for `L5-U` outside the exceptional set of `LW1_5.md` M.1, and in `SO(10)` for `L5-O[S_+]` (R).
6. *Transfer.* Every statement of `LW1_5.md` about the coarse algebra and `α_c` holds for `ι` of the coarse algebra and `α_f`, with "site" read as "coarse site".

The proof is in 5.3, after three lemmas.

### 5.2 Three lemmas

**Lemma 5.2 (dial embedding).** Let `(φ_{X,j})` be orthonormal. Then the `c(φ_{X,j})` satisfy the CAR, and `ι` is an injective *-homomorphism of the coarse matter algebra onto `CAR(⊕_X V_X)`. An even element of `CAR(⊕_X V_X)` commutes with `c(w)` and `c(w)^*` for every `w ∈ W`.

*Proof.* `{c(f), c^†(g)} = ⟨f, g⟩` and `{c(f), c(g)} = 0` give the CAR for an orthonormal family. The unitary `e_{X,j} ↦ φ_{X,j}` from `ℓ^2(𝒳 × {1..5})` onto `⊕V_X` induces a Bogoliubov *-isomorphism of CAR algebras; on each finite set of modes this is an isomorphism of matrix algebras `M_{2^n}(C)`, and the quasi-local algebra is their norm closure. For `w ⊥ ⊕V_X`, `c(w)` anticommutes with every `c(f)` and `c(f)^*`, `f ∈ ⊕V_X`, hence commutes with every product of an even number of them. ∎

Fix a finite site set `S`, connected in the fine nearest-neighbour graph, with `|S| ≥ 3`, and registers `R_e` on a set `E` of fine links inside `S`. Write `H = Λ(C^S) ⊗ (⊗_{e∈E} R_e)`, `P_S` for the matter parity, and `𝔨` for the anti-Hermitian operators on `H` that commute with `P_S`. Let `𝔨_0 = {X ∈ 𝔨 : tr(X (P_S ⊗ 1)) = 0}` and `K_0` the unitaries `U` on `H` commuting with `P_S` whose determinants on the two parity sectors are equal. Let `𝒩` be the set of `iY`, where `Y` is Hermitian, commutes with `P_xP_y`, and is supported on `F_x ⊗ F_y`, or on `F_x ⊗ F_y ⊗ R_e` when `e = (x, y) ∈ E`, for a nearest-neighbour pair `x, y ∈ S`.

**Lemma 5.3 (Lie generation).** The real Lie algebra generated by `𝒩` is `𝔨_0`.

*Proof.* Use Majoranas `γ_a`, `a ∈ M = S × {1, 2}`. For `A ⊆ M` with `|A|` even, let `m_A` be the ordered product of the `γ_a`, `a ∈ A`, times the power of `i` that makes it Hermitian; `m_A^2 = 1` and `m_∅ = 1`. The operators `m_A ⊗ B`, `|A|` even, `B` Hermitian on the registers, span the Hermitian part of the even algebra over `R`. Two facts: for even `A, D`, `m_A m_D = (−1)^{|A∩D|} m_D m_A`; if `|A ∩ D|` is odd, `m_A m_D` is a unit multiple of `m_{A△D}`. Hence, for commuting register operators `X, Y`, `[i m_A ⊗ X, i m_D ⊗ Y]` is a nonzero real multiple of `i m_{A△D} ⊗ XY` when `|A ∩ D|` is odd.
1. *Quadratics.* `𝒩` contains `i m_{ab}` for `a, b` at one site or at neighbouring sites. `[i m_{ab}, i m_{bc}]` is a multiple of `i m_{ac}`. Since `S` is connected, every `i m_{ac}`, `a ≠ c ∈ M`, is generated.
2. *Moving an index.* For `a ∈ A`, `b ∉ A`, `[i m_{ab}, i m_A ⊗ X]` is a multiple of `i m_{(A∖a)∪b} ⊗ X`. So `i m_A ⊗ X` generates every `i m_{A'} ⊗ X` with `|A'| = |A| ≥ 2`.
3. *Raising the degree.* `𝒩` contains a quartic `i m_{A_0}` on one neighbouring pair. If `|A| = 2r ≤ 2|S| − 4`, choose a quartic `D` with `|A ∩ D| = 1`; the bracket with `i m_D ⊗ 1` gives degree `2r + 2` with the same `X`. So if one `i m_A ⊗ X` with `|A| = 2` is generated, every `i m_{A'} ⊗ X` with `2 ≤ |A'| ≤ 2|S| − 2` is (steps 2-3).
4. *Registers.* For `e ∈ E`, `𝒩` contains `i m_A ⊗ B_e` for `A` within the two sites of `e`, `|A| ∈ {0, 2, 4}`, and every Hermitian `B_e` on `R_e`. By steps 2-3 (bracketing with `i m_{ab} ⊗ 1`), all `i m_A ⊗ B_e` with `2 ≤ |A| ≤ 2|S| − 2` follow. For distinct `e_1, e_2` and a target `D`, take `d ∈ D`, `u ∉ D`, `A = {d, u}`, `D' = (D ∖ d) ∪ u`: `|A ∩ D'| = 1` and `A △ D' = D`, so `i m_D ⊗ B_1B_2` follows. Iterating, `i m_D ⊗ B` follows for every Hermitian `B` on `⊗R_e`, since products of Hermitian operators on distinct factors span the Hermitian operators of the tensor product over `R`.
5. *The two central degrees.* `[i m_D ⊗ X, i m_D ⊗ Y] = −1 ⊗ [X, Y]` gives `i·1 ⊗ B` for traceless `B`; `i·1 ⊗ 1` is a generator (a phase gate). For `A` and `M∖A` both of degree between 2 and `2|S| − 2`, `m_A` and `m_{M∖A}` commute and their product is `±m_M`, so `[i m_A ⊗ X, i m_{M∖A} ⊗ Y] = ∓m_M ⊗ [X, Y]`. This gives `i m_M ⊗ B`, `m_M = ±P_S`, for traceless `B`.

The span of all these is `𝔨_0`: it is every `i m_A ⊗ B` except the one direction `i P_S ⊗ 1`, which is the Hilbert-Schmidt complement of `𝔨_0` in `𝔨`. Conversely every element of `𝒩` lies in `𝔨_0`: for `Y` on a pair (and a register), `tr(Y(P_S ⊗ 1)) = tr(Y P_xP_y) · tr(P_{S∖\{x,y\}}) = 0`, because `S ∖ {x, y}` is nonempty and the parity of a nonempty set of modes is traceless. Brackets lie in `𝔨_0` because `P_S` is central in the even algebra, so `tr([U, V] P_S) = tr(U[V, P_S]) = 0`. ∎

**Lemma 5.4 (one-parameter generation).** Let `K` be a connected closed matrix group with Lie algebra `𝔨`, and let `X_1, …, X_m` generate `𝔨` as a Lie algebra. Then every element of `K` is a finite product of elements `exp(tX_i)`.

*Proof.* Let `H` be the subgroup generated by the `exp(tX_i)`. Let `V` be the real span of `Ad_h X_i`, `h ∈ H`. For `Y ∈ V`, `Ad_{exp(tX_i)} Y ∈ V` for all `t`; differentiating at `t = 0` gives `[X_i, Y] ∈ V`, since `V` is a closed subspace. So `V` contains every right-nested bracket of the `X_i`, and these span the generated Lie algebra (induction with the Jacobi identity). Hence `V = 𝔨`. Choose `h_j ∈ H` and indices `i_j` such that `Y_j = Ad_{h_j} X_{i_j}`, `j = 1..n`, form a basis of `𝔨`. The map `F(t) = Π_j h_j exp(t_j X_{i_j}) h_j^{-1} = Π_j exp(t_jY_j)` takes values in `H`. Near `t = 0`, `log F` is smooth with derivative `s ↦ Σ_j s_jY_j`, a bijection onto `𝔨`. By the inverse function theorem, `log F` maps a neighbourhood of `0` onto a neighbourhood `N` of `0` in `𝔨`. Since `exp` maps a neighbourhood of `0` in `𝔨` onto a neighbourhood of `1` in `K` (closed matrix groups), `H` contains a neighbourhood `U` of `1`. Then `H = ∪_{h∈H} hU` is open, its complement is a union of open cosets, and `K` is connected, so `H = K`. ∎

`K_0` is connected: given `(U_+, U_−)` with `det U_+ = det U_−`, pick `θ` with `e^{inθ} = det U_+`, `n` the common sector dimension; then `(U_+, U_−) = e^{iθ}(V_+, V_−)` with `V_± ∈ SU(n)`, and `U(1) × SU(n) × SU(n)` is connected. Its Lie algebra is `𝔨_0`. So Lemmas 5.3-5.4 give: **every element of `K_0` is a finite product of even nearest-neighbour gates inside `S`.**

### 5.3 Construction and proof of Theorem 5.1

By (B0), every coarse cube of one tiling is the `π`-image of a fine translate of one representative cube.

*Registers.* Put the register of each coarse link `ℓ` (`Λ^mC^{10}` for `L5-U[m]`, `S_+` of `Spin(20)` for `L5-O`) on the fine link `b(ℓ)`. Every other fine link carries `C`.

*Matter cube layers.* For a coarse cube `C`, the coarse gate `u_C = e^{∓i a H_C}` is an even unitary on the coarse modes of its eight sites and its twelve registers. So `ι(u_C)` is an even unitary on `H_{S(C)}`. It lies in `K_0` for `S = S(C)`: `ι(u_C) = exp(∓ia ι(H_C))`, and `tr(ι(H_C)(P_S ⊗ 1)) = 0`, because each hop term is a register operator times `c^†(f)c(g)` (or a Majorana product `γγ'`) between distinct coarse sites, and `tr(c_x^† c_y P_S) = 0` for `x ≠ y`, `tr(n_xP_S) = tr(n_xP_x)·tr(P_{S∖x}) = 0`. By Lemmas 5.3-5.4, `ι(u_C) = g_1 g_2 ⋯ g_N` with each `g_i` an even nearest-neighbour gate inside `S(C)`, touching only registers of bridges of `C`. Fix such a word for one representative cube of `𝒯_e`, and one for `𝒯_o`. For `i = 1..N`, the fine layer `L_{e,i}` is the product of the translates of `g_i` over the fine translations that carry the representative to the other cubes of `𝒯_e`. These act on disjoint edge triples by (B2). The gates `u_C` of one tiling are exact translates of each other, because the signs `η_i` are periodic under the even translations (`LW1.md` A2: "Even translations preserve its phases exactly"). Since gates of distinct cubes of one tiling are even with disjoint supports, they commute, and `ι(M_e) = L_{e,1} L_{e,2} ⋯ L_{e,N}`. The same holds for `𝒯_o`.

*Electric layer.* `ι(W_E)` is a product of single-register gates on bridges, one fine layer.

*The fine update.* `U_f = ι(W_E) (L_{o,1}⋯L_{o,N'}) (L_{e,1}⋯L_{e,N})`, followed or not by layers acting on `CAR(W)` (Remark 5.6). At infinite volume, products mean the local automorphisms of `LW1.md` E1.

*Proof of Theorem 5.1.*
1. `U_f = ι(W_E)ι(M_o)ι(M_e) = ι(U_0)`. So `α_f∘ι = ι∘α_c`. Each of the three factors is an even element of `ι` of the coarse algebra (the single fine gates are not), so by Lemma 5.2 it commutes with `CAR(W)`; `α_f` is the identity there unless layers of Remark 5.6 are added.
2. By construction.
3. In both laws the coarse lift sends `c_{X,j} ↦ θ_g(X)c_{gX,j}` and does not mix the five modes. The fine lift `β_g` sends `c_x ↦ θ_g(X)c_{gx}` for `x ∈ supp X`. By (B1), `β_g(c(φ_{X,j})) = θ_g(X) c(g·φ_{X,j}) = θ_g(X) c(φ_{gX,j})`, which is `ι` of the coarse lift. On bridge registers `β_g` is the coarse register lift, by `b(gℓ) = g·b(ℓ)`. So `β_g∘ι = ι∘β^c_{π(g)}`. The one-particle part of `β_g` is unitary and maps `⊕V_X` onto itself, so it maps `W` onto `W`. On `ι` of the coarse algebra, `β_gα_f = β_gια_cι^{-1} = ιβ^cα_cι^{-1} = ια_cβ^cι^{-1} = α_fβ_g`, using B1-U or A2-5 for `α_cβ^c = β^cα_c`. On `CAR(W)` both are the identity, or Remark 5.6 applies. The two subalgebras generate `𝔄`.
4. For `L5-U`, `LW1_5.md` U: "every `𝒢_x^T` commutes with every hop and electric gate." The dial frame `exp(i dΓ_X(T))`, `dΓ_X(T) = Σ_{jk} T_{jk} c^†(φ_{X,j})c(φ_{X,k})`, with the register change `exp(i Σ_{ℓ∋X} r^†_{ℓ,X}T r_{ℓ,X})`, is `exp(i ι(𝒢^T_X))`. It commutes with every `ι(u_C)` and with `ι(W_E)`, hence with `U_f`, for all angles. These elements exhaust the Bogoliubov action of the connected group `U(5)`. It is a dial frame in the sense of 3.4: `dΓ_X(T)` commutes with `c(f)` for `f ⊥ V_X`. For `L5-O`, Q and G give the same with `𝒢^{cd}_X`.
5. A dial frame at `X` preserves `ι` of the coarse algebra (it maps `CAR(V_X)` onto itself and fixes the rest). Pulled back by `ι`, it is a coarse site frame, and compatibility with `ι(u_C)` pulls back to compatibility with `u_C`. `LW1_5.md` M and M.1 ("Every compatible frame is Bogoliubov. If H also conserves total matter number, it is in U(5). The same holds for a compatible gate `e^{iaH}` when `a ∉ 𝓔(H)`") and R ("for `S_+`, the generator-level site frame group is `SO(10)`") give the bounds.
6. `ι` is an isomorphism onto its image that intertwines the ticks, the local gauge transformations and the lifts; a state of `𝔄` restricts to a state of the image, and a coarse state extends (for instance by an even product state on `CAR(W)`). ∎

**Remark 5.5 (bases that turn).** If `g·V_X = V_{gX}` holds but (B1) does not, then `g·φ_{X,j} = Σ_k u(g,X)_{kj} φ_{gX,k}` with `u(g,X) ∈ U(5)`. The geometric fine lift then acts on `ι` of the coarse algebra as the coarse lift followed by the local frame transformation `u(g,·)`. Since `α_c` commutes with every local gauge transformation, covariance survives if the fine lift acts on bridge registers by the coarse register lift followed by the register part of that gauge transformation. For `L5-O` this needs `u(g,X) ∈ SO(10)`, which holds because `U(5) ⊂ SO(10)`. The cost is a register lift that is not a flavour permutation. This is #10019's "the labels turn with space", absorbed by the exact gauge group.

**Remark 5.6 (non-dial modes).** Theorem 5.1 allows the identity on `CAR(W)`, which leaves the non-dial modes static. A covariant non-trivial choice inside the class: for each block, `A_X = P_W h_X P_W`, with `h_X` the fine nearest-neighbour hopping inside `supp X` and `P_W` the projection onto `W`. The layer `Π_X exp(−iε dΓ(A_X))` is covariant when `P_W` and `h_X` are invariant under the stabilizer `G_X`, is block-local and so compiles by Lemmas 5.3-5.4 with `S = supp X`, and commutes with `ι` of the coarse algebra because `A_X` annihilates `V_X`. A coupling `exp(−iκ N_X dΓ(P_W1_{supp X}P_W))` to the dial number `N_X = Σ_j c^†(φ_{X,j})c(φ_{X,j})`, a `U(5)` singlet, keeps the frames exact for the same reason. Motion of non-dial modes between blocks is not needed for Theorem 5.1 and is not built here.

### 5.4 PS-1c at the fine scale

PS-1c, quoted from `LW1_5.md` line 60: "the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre, and its symmetry group acts transitively on sites." The law class of 3.5 asks cell covariance under a superlattice cell group, not transitivity on fine sites. This section shows what transitivity at the fine scale would cost.

**Lemma 5.7 (small cubic sublattices).** An `O`-invariant sublattice of `Z^3` has index 1, 2 or at least 4. If its index is 2, it is `F = {x : x_1 + x_2 + x_3` even`}`.

*Proof.* Let `L` have index `k ∈ {2, 3}`; then `kZ^3 ⊆ L`, and `L/kZ^3` is an `O`-invariant subgroup of `(Z/k)^3` of index `k`. For `k = 3`, its orthogonal complement for the `O`-invariant dot product is an invariant line of `F_3^3`, spanned by some `v ≠ 0`. The three diagonal sign matrices of `O` map `v` to `±v` only if `v` has at most one nonzero coordinate, and the cyclic permutation then moves the line. So `k ≠ 3`. For `k = 2`, `L/2Z^3` is the kernel of a nonzero functional `a` on `F_2^3`, and invariance under all coordinate permutations forces `a = (1,1,1)`. So `L = F`. ∎

**Proposition 5.8 (fine transitivity).**
(a) For every fine block law of Theorem 5.1, the translations `Λ` of `G` have index `8k_eff ≥ 64` in `Z^3`. Each `G`-orbit of fine sites meets at most 24 classes mod `Λ`, so `G` has at least three orbits on fine sites. It is not PS-1c's cell group.
(b) Let any fine block law with a coarse cubic structure (3.3) be covariant under a cell group `G = Λ ⋊ O_c` that acts transitively on fine sites. Then `k_eff = 8`, and `π(Λ)` is either all coarse translations or the index-two lattice `F` of coarse translations.

*Proof.* (a) `π` maps `Λ` onto `2Z^3`, of index 8 in the coarse lattice, so `[Z^3 : Λ] = 8k_eff`, and `k_eff ≥ 8` by Theorem 4.3. (b) Transitivity gives `[Z^3 : Λ] ≤ |G/Λ| = 24`. In the proof of Theorem 4.3, take `g = s ∈ Λ`: then `τ(t) = Ψ(s)τ(t)` for all `t ∈ T`, so `Ψ(s)` fixes a full-rank lattice and `Ψ(s) = 1`. Hence `T = Λ` and `[Z^3 : Λ] = k_eff·[Z^3 : π(Λ)]`. Since `k_eff` is a perfect cube at least 8 and the product is at most 24, `k_eff = 8` and `[Z^3 : π(Λ)] ≤ 3`. The lattice `π(Λ)` is invariant under the linear parts of `π(G)`, which contain `O` (3.3). Lemma 5.7 gives the two cases. ∎

So a block route that also meets PS-1c's transitivity at the fine scale needs eight-site blocks and a coarse law covariant under all coarse translations, or under the index-two lattice `F`. The live laws are built and proved covariant for `2Z^3 ⋊ O_{c_0}` (B1-U, A2-5). For the free walk of `L5-U`, which is `V ⊗ 1_5` (A2-5), `LW1.md` A2 gives the isometry group "up to site phases" as "exactly 𝒢", whose translations are `2Z^3`. A coarse law with the larger covariance is the open item **CG16K-T** (FINISH), unless the owner reads PS-1c at the block rung (K-CELL, section 9).

**What Theorem 5.1 settles.** The target of the brief, for both live laws: a local, finite-register law on one-mode sites, NN-a at the fine scale and covariant under a superlattice cell group with all 24 rotations (not transitive on fine sites, 5.4), with an exact `U(5)` (from `L5-U[m]`) or `Spin(10)` (from `L5-O[S_+]`) frame group acting on five dial modes at the block scale. Exactness is gate-wise at the coarse rung and holds at every angle. By the transferred bounds, the gate-wise frame group on the dials is exactly `U(5)` outside the finite exceptional set of M.1 (with `LW1_5X.md`'s results at the exceptional angles, as frozen), and acts as `SO(10)` for `L5-O[S_+]` by R. It needs a block structure with (B0)-(B2). Sections 6 and 7 build such structures for options (a) and (b).

## 6. Option (a): five separate blocks

### 6.1 When (a) fails

**Corollary 6.1 (a fails at full-`O` coarse sites).** If some coarse site `X` is fixed by elements of `G` whose linear parts form all of `O`, its five neighbourhoods cannot have distinct centroids.

*Proof.* The stabilizer permutes the five neighbourhoods, hence their centroids. Its elements fix the centroid `c` of `supp X`, and their linear parts form `O`, so they act as `O_c`. Corollary 4.1a applies. ∎

**Corollary 6.2 (a fails when neighbourhoods form a cubic lattice).** Suppose the neighbourhoods themselves carry a cubic structure: a bijection `κ'` from the set of all neighbourhoods to `Z^3` with a homomorphism `π'` whose linear parts contain `O`. Then they cannot be grouped five at a time into coarse sites with a coarse cubic structure.

*Proof.* Let `T` be the translations of `G` whose images under `π'` and `π` both have trivial linear part; it has finite index. As in Theorem 4.3, `π'` and `π` give injective additive maps `τ'`, `τ` on `T` with `τ'(Qt) = Ψ'(g)τ'(t)` and `τ(Qt) = Ψ(g)τ(t)`, and their rational extensions satisfy `τ'^T_Q τ'_Q = μ'·1`, `τ_Q^T τ_Q = μ·1`. The neighbourhoods per `T`-cell number `μ'^{3/2}[Z^3 : T]` and the coarse sites `μ^{3/2}[Z^3 : T]`, so each coarse site has `(μ'/μ)^{3/2}` neighbourhoods. Both counts are integers, so `√(μ'/μ)` is rational and the ratio is the cube of a rational number. Five is not. ∎

Corollary 6.2 is the scale-free form of O-2 for option (a): blocks that tile like sites inherit the tiling obstruction of sites. **The escape is that neighbourhoods need not form a lattice of their own.** Inside the region of each coarse site they may sit in any arrangement invariant under the coarse site's stabilizer, with the remaining fine modes as non-dial modes (Theorem 4.3 requires at least three per coarse site).

### 6.2 When (a) works

Use the coarse cell group of both live laws, `𝒢 = 2Z^3 ⋊ O_{c_0}`. Its coarse sites have stabilizers of order three (`LW1.md` A2), the rotations about one body diagonal. Corollary 6.1 does not apply.

**Example 6.3 (five sites on a diagonal).** Take `n = 5`, a fine cube centre `c'`, the fine cell group `G = 10Z^3 ⋊ O_{c'}` and the coarse sites `X_σ = c' + (5/2)σ + 10Z^3`, `σ ∈ {±1}^3`; these are fine sites because `5/2` and the coordinates of `c'` are half-integers. The neighbourhoods of `X_σ` are the five single sites `p + kσ`, `k = −2, …, 2`, where `p` is the position of `X_σ`; the dials are `δ_{p+kσ}`.
- *Disjointness.* For `σ ≠ σ'`, a coordinate where they differ gives `(5/2 + k) = −(5/2 + k')`, so `k + k' = −5`, impossible for `|k|, |k'| ≤ 2`. Across translates, every coordinate of `(5/2 + k)σ` has modulus at most `9/2 < 5`.
- *(B1).* The stabilizer of `X_σ` is the order-three rotation group about the line through `p` along `σ` (this line passes through `c'`). It fixes every site `p + kσ`, so the dial basis is fixed and can be transported.
- *(B2).* For a coarse cube `C`, let `S(C)` be the fine box that contains its eight corners' dial sites, enlarged by two fine units. It is connected. Cubes of one tiling are ten fine units apart along each axis, and a rod reaches two units beyond its corner, so these boxes are disjoint and contain no dial site of a coarse site outside `C`. Bridges: the middle fine link of the segment between neighbouring corners, inside the box; this choice is covariant.
- *(B0).* The translations `10Z^3` map onto the coarse translations `2Z^3`.

Theorem 5.1 then gives exact `U(5)` or `Spin(10)` on five single-site neighbourhoods per coarse site. The cell group has all 24 proper rotations, about `c'`. Every coarse site points along its own body diagonal, as every site of `L_cube` has a stabilizer of order three. There are 960 spectators in each fine `10^3` cell. Theorem 5.1 alone leaves them static. The boxes `S(C)` of one tiling are `10^3` cubes that tile `Z^3`, so a layer of spectator hopping inside each box, Remark 5.6's construction with `W` the spectator modes, is covariant, compiles, and leaves the frames exact.

**Example 6.4 (1 + 1 + 3).** Take `n = 21` in place of 5 in Example 6.3, so `G = 42Z^3 ⋊ O_{c'}` and `p = c' + (21/2)σ`. The five neighbourhoods of `X_σ` are the fine `3^3` cubes centred at `p`, `p + 3σ` and `p − 3σ_ie_i`, `i = 1, 2, 3`; the dials are their normalised uniform vectors. The five cubes are pairwise disjoint (each pair of centres differs by at least 3 in some coordinate), and all lie within sup-distance 4 of `p`; coarse sites are at least 21 apart, so (B2) holds as in Example 6.3 with boxes enlarged by 4. The stabilizer fixes the first two centres and permutes the other three cyclically, so (B1) fails for those three dials. Remark 5.5 restores covariance with a register lift that includes the permutation, a `U(5)` element (an `SO(10)` element for `L5-O`). This is #10014's "site + 3 forward + diagonal (6/48)" pattern, with cubes in place of sites and spectators in place of a tiling.

### 6.3 Verdict on (a)

- **Proved:** option (a) is realizable. Under NN-a and PS-1c's cell group, five spatially separate neighbourhoods per coarse site carry an exact `U(5)` or `Spin(10)` (Theorem 5.1 with Example 6.3; with Example 6.4 through Remark 5.5).
- **Proved:** option (a) is impossible if a coarse site is a centre of all 24 rotations (Corollary 6.1), and if the neighbourhoods form a cubic lattice of their own (Corollary 6.2).
- **Scale-freeness, answered.** O-1 is scale-free but avoidable, because PS-1c's own cell group has no full-`O` site. O-2 is scale-free and stronger than stated, but it forces non-dial modes, not failure. #10014's "at best 8/48" referred to lattice tilings by translates. With non-dial modes allowed, the cell group keeps all 24 proper rotations.

## 7. Option (b): five collective modes of one block

### 7.1 Characters and orbits

**Lemma 7.1 (O-content of one orbit).** The classes of `O` are `E`, `8C_3`, `3C_2` (squares of the 4-fold rotations), `6C_4`, `6C_2'` (face-diagonal axes). The characters are

| | `E` | `C_3` | `C_2` | `C_4` | `C_2'` |
|---|---|---|---|---|---|
| `A_1` | 1 | 1 | 1 | 1 | 1 |
| `A_2` | 1 | 1 | 1 | −1 | −1 |
| `E` | 2 | −1 | 2 | 0 | 0 |
| `T_1` | 3 | 0 | −1 | 1 | −1 |
| `T_2` | 3 | 0 | −1 | −1 | 1 |

The permutation representation on an orbit with stabilizer `H` contains `ρ` with multiplicity `(1/|H|) Σ_{h∈H} χ_ρ(h)`. Hence, for orbits about a site or cube centre:
- centre, `H = O`: `A_1`;
- 6-orbit, `H = C_4`: `A_1 + E + T_1`;
- 8-orbit, `H = C_3`: `A_1 + A_2 + T_1 + T_2`;
- 12-orbit, `H = C_2'`: `A_1 + E + T_1 + 2T_2`;
- 24-orbit, `H = 1`: `A_1 + A_2 + 2E + 3T_1 + 3T_2`.

*Proof.* `T_1` is the defining representation (trace of the rotation matrix); `A_2` is the sign of the quotient of `O` by the rotation group `T` of the tetrahedron (`C_4` and `C_2'` lie outside `T`); `T_2 = T_1 ⊗ A_2`; `E` is fixed by dimension and orthogonality. The table rows are orthonormal, which checks it. The multiplicity formula is Frobenius reciprocity: `Hom_O(Ind_H^O 1, ρ) ≅ Hom_H(1, ρ|_H)`, whose dimension is the average of `χ_ρ` over `H`. The five rows then follow by averaging: for example, for `H = C_4 = {E, C_4, C_2, C_4^3}`, `T_1` gives `(3+1−1+1)/4 = 1` and `T_2` gives `(3−1−1−1)/4 = 0`. ∎

Two counts follow for any block that is a union of orbits. `A_1` occurs once per orbit; this is #10026's "every site orbit carries A1 exactly once". `A_2` occurs once per orbit whose stabilizer lies in `T`, that is, once per orbit of size 8 or 24.

**Lemma 7.2 (canonical subspaces).** Let a finite group `H` act unitarily on `E`, with isotypic decomposition `E = ⊕_ρ E_ρ`, `E_ρ ≅ C^{m_ρ} ⊗ ρ`. A subspace `V` is canonical (3.6) exactly when it is a sum of isotypic components.

*Proof.* An `H`-equivariant map sends `E_ρ` into `E_ρ` (Schur), so each `E_ρ` is canonical, and so are sums. Conversely let `V` be canonical. The projection `Π_ρ` onto `E_ρ` commutes with `H`, and `2Π_ρ − 1` is a unitary commuting with `H`, so `Π_ρV ⊆ V` and `V = ⊕_ρ Π_ρV`. Every unitary of the form `u ⊗ 1` on `C^{m_ρ} ⊗ ρ`, extended by the identity, commutes with `H`; such unitaries span `M_{m_ρ} ⊗ 1`. So `W = Π_ρV` is invariant under `M_{m_ρ} ⊗ 1` and under `1 ⊗ ρ(H)`. If `0 ≠ w = Σ_i e_i ⊗ w_i ∈ W`, pick `i` with `w_i ≠ 0`. Matrix units give `e_j ⊗ w_i ∈ W` for every `j`, and `ρ(H)` applied to `w_i` spans `ρ` by irreducibility. So `W = E_ρ`. ∎

### 7.2 Which blocks have a canonical five-dimensional dial space

Lemma 7.1 gives the `O`-isotypic dimensions (multiplicity times dimension). A canonical five-dimensional subspace is a set of components whose dimensions add to 5 (Lemma 7.2). For `O_h`, each component splits by the parity under inversion; the labels below come from polynomial bases (constants, `x² − y²`, `2z² − x² − y²` and `xy` are even; `x`, `xyz` and `x(y² − z²)` are odd), and the `O_h` lists of five-dimensional canonical subspaces are the same as for `O` in the first four rows.

| Block (sites) | `O`-isotypic dimensions | Canonical 5-dim subspaces under `O` | `O_h` labels |
|---|---|---|---|
| octahedron `{c ± e_i}` (6) | `A_1`:1, `E`:2, `T_1`:3 | `E ⊕ T_1` only (the sum-zero vectors) | `E_g ⊕ T_{1u}` |
| 7-star (7) | `A_1`:2, `E`:2, `T_1`:3 | `A_1^2 ⊕ T_1`, `E ⊕ T_1` | `A_{1g}^2 ⊕ T_{1u}`, `E_g ⊕ T_{1u}` |
| `2^3` cube (8) | `A_1`:1, `A_2`:1, `T_1`:3, `T_2`:3 | `A_1 ⊕ A_2 ⊕ T_1`, `A_1 ⊕ A_2 ⊕ T_2` | `1, xyz` plus `x,y,z` or plus `xy,yz,zx` |
| `3^3` cube (27) | `A_1`:4, `A_2`:1, `E`:4, `T_1`:9, `T_2`:9 | `A_1^4 ⊕ A_2`, `E^2 ⊕ A_2` | `A_{1g}^4 ⊕ A_{2u}`, `E_g^2 ⊕ A_{2u}` |
| `4^3` cube (64) | `A_1`:4, `A_2`:4, `E`:8, `T_1`:24, `T_2`:24 | none | none (`A_{1g}`:4, `A_{2u}`:4, `E_g`:4, `E_u`:4, `T_{1g}`:6, `T_{1u}`:18, `T_{2g}`:18, `T_{2u}`:6) |
| `5^3` cube (125) | `A_1`:10, `A_2`:5, `E`:20, `T_1`:45, `T_2`:45 | `A_2^5` only | `A_{2g} ⊕ A_{2u}^4`, `A_{2g} ⊕ E_u^2` |

*Derivations (by hand; table confirmed by the [check] of 2.3).* Octahedron: one 6-orbit. 7-star: centre plus a 6-orbit. `2^3`: one 8-orbit about the cube centre. `3^3`: centre, faces (6), edges (12), corners (8). `4^3`, about a cube centre: two 8-orbits (types `(½,½,½)`, `(3/2,3/2,3/2)`) and two 24-orbits (types `(3/2,½,½)`, `(3/2,3/2,½)`, trivial stabilizers). `5^3`: the orbits of types `0`, `(1,0,0)`, `(2,0,0)`, `(1,1,0)`, `(2,2,0)`, `(1,1,1)`, `(2,2,2)`, `(2,1,0)`, `(2,1,1)`, `(2,2,1)`; the last three have trivial stabilizers. Sum the rows of Lemma 7.1. For the `5^3` cube under `O_h`, each `O`-orbit is also an `O_h`-orbit; its `O_h`-stabilizer adds one improper element (`σ_z = i∘C_2` for `(2,1,0)`; `i∘C_2'` for `(2,1,1)` and `(2,2,1)`), and averaging `χ_{ρg}(ig) = χ_ρ(g)`, `χ_{ρu}(ig) = −χ_ρ(g)` gives `A_{2g}`:1, `A_{2u}`:4, `E_u`:4, `A_{1g}`:10, `E_g`:16, `T_{1g}`:9, `T_{1u}`:36, `T_{2g}`:27, `T_{2u}`:18 (total 125). The two five-dimensional sums are those listed.

**Reading.** "Without a choice" in the sense of Lemma 7.2 holds for the octahedron (one answer, `E ⊕ T_1`, #10029's and #10019's "half-link 5 = E + T1") and for the `5^3` cube under `O` (`A_2^5`). It fails for the 7-star, the `2^3` cube and the `3^3` cube (two answers each), and the `4^3` cube has none. The `2^3` row contains #9894's "A1 + A2 + T1".

### 7.3 Compatibility with the law's cell group

The live laws are covariant under `2Z^3 ⋊ O_{c_0}`, whose coarse-site stabilizer is the order-three rotation group about a body diagonal. Hypothesis (B1) of Theorem 5.1 asks that this stabilizer fix each dial vector.

**Proposition 7.3.** A canonical subspace of an `O`-symmetric block, centred at the coarse site, is pointwise fixed by an order-three rotation about the centre exactly when it lies in the sum of the `A_1` and `A_2` components.

*Proof.* On a component of type `ρ`, the order-three rotation acts with trace `m_ρ χ_ρ(C_3)`. It fixes the component pointwise exactly when it acts as the identity, that is, when the trace equals the dimension `m_ρ dim ρ`, that is, `χ_ρ(C_3) = dim ρ`. By the table this holds for `A_1` and `A_2` (`1 = 1`) and fails for `E` (`−1 ≠ 2`), `T_1` and `T_2` (`0 ≠ 3`). ∎

So among the blocks of 7.2, the canonical five-dimensional dial spaces with (B1) are exactly `A_1^4 ⊕ A_2` on the `3^3` cube and `A_2^5` on the `5^3` cube. On the `3^3` cube this removes the two-fold choice of 7.2: `E^2 ⊕ A_2` fails (B1). The octahedral and 7-star dials, which rotations turn, need the register lifts of Remark 5.5.

### 7.4 The construction K-27

**Data.** Fine cell group `G = 6Z^3 ⋊ O_{c'}`, `c'` a fine cube centre. Coarse sites: the fine `3^3` cubes `X` centred at the fine sites `p_X ∈ c' + (3/2)(1,1,1) + 3Z^3`. These cubes tile `Z^3`; there are no spectators. Coarse cubic structure: `κ(X) = (p_X − c' − (3/2)(1,1,1))/3`; `π` sends `G` onto `2Z^3 ⋊ O_{c_0}` with `c_0 = −(1/2)(1,1,1)`, and `6Z^3` onto `2Z^3` (B0). Dials, with `v = x − p_X ∈ {−1,0,1}^3`:
- `φ_{X,1} = δ_{p_X}` (centre);
- `φ_{X,2} = 6^{−1/2} Σ_{|v|_1 = 1} δ_x` (faces);
- `φ_{X,3} = 12^{−1/2} Σ_{|v|_1 = 2} δ_x` (edges);
- `φ_{X,4} = 8^{−1/2} Σ_{|v|_1 = 3} δ_x` (corners);
- `φ_{X,5} = 8^{−1/2} Σ_{|v|_1 = 3} v_1v_2v_3 δ_x` (the corner alternation; the two tetrahedra of corners carry opposite signs).

They are orthonormal: the first four have disjoint supports, and `Σ_{corners} v_1v_2v_3 = 0`. They span `A_1^4 ⊕ A_2` (Lemma 7.1: the four shell averages are the `A_1` vectors; `v_1v_2v_3` changes sign under `C_4` and `C_2'` and is fixed by `C_3` and `C_2`, which is `χ_{A_2}`).

**Hypotheses.**
- (B1). Take `p_X = c' + (3/2)σ`; the other coarse sites are translates. Its stabilizer consists of the maps `x ↦ c' + Q(x−c') + λ`, `λ ∈ 6Z^3`, with `Q(3/2)σ + λ = (3/2)σ`. This forces `(3/2)(σ − Qσ) ∈ 6Z^3`, so `Qσ = σ`: the stabilizer is the order-three group about the body diagonal through `p_X` and `c'`. By Proposition 7.3 it fixes every `φ_{X,j}`. Bases elsewhere are transported; on `φ_{X,5}` the transport may differ from the formula above by the sign `χ_{A_2}(Q)`, which is harmless.
- (B2). Bridge of the coarse link from `X` to `X + 3e_i`: the fine link from the face centre `p_X + e_i` to the face centre `p_X + 2e_i` of the neighbour. For a coarse cube `C`, `S(C)` is the union of its eight blocks, a fine `6^3` cube: connected, containing its twelve bridges, and disjoint from the `S(C')` of the other cubes of its tiling.

**Theorem 7.4 (K-27).** With these data, Theorem 5.1 gives a fine block law on one-mode sites, NN-a at the fine scale, cell covariant under `6Z^3 ⋊ O_{c'}` with lifts by diagonal signs on fine matter and the coarse register lifts on bridges, with an exact `U(5)` (from `L5-U[m]`, every `1 ≤ m ≤ 9`) or `Spin(10)` (from `L5-O[S_+]`) frame group acting on the five dials `A_1^4 ⊕ A_2` of every `3^3` block. Every fine site lies in a block; each block has 22 non-dial modes (`E^2 ⊕ T_1^3 ⊕ T_2^3`). ∎

The same construction with `5^3` blocks, `G = 10Z^3 ⋊ O_{c'}` and dials `A_2^5` also satisfies (B0)-(B2).

### 7.5 Verdict on (b)

- **Proved:** option (b) is realizable, with exact `U(5)` or `Spin(10)` on five collective modes of one block, with no spectators and with lifts by diagonal signs (Theorem 7.4).
- **Proved:** which five-dimensional subspaces exist without a choice, for the blocks examined (7.2), and which of them are compatible with the live laws' cell group (Proposition 7.3): exactly `A_1^4 ⊕ A_2` (on `3^3`) and `A_2^5` (on `5^3`).
- **Not removed:** the choice of block. `3^3` and `5^3` both qualify. The `3^3` cube is the smallest cube with a canonical, stabilizer-fixed five-dimensional subspace: `1^3` has only `A_1`, and `2^3` has `A_1 ⊕ A_2` of dimension 2. This minimality is a fact about cubes; it is not a rule, and section 9 tests it as a candidate.

## 8. What the block route inherits: protection, the 16, the zoom; the 7-star and the 27-cube

### 8.1 Protection

With `L5-O[S_+]` compiled (Theorem 7.4), the frame group on the five dials acts as `SO(10)`, the connected Bogoliubov group of the dials (R); this is #10014's `Spin(2N)` for `N = 5`. So #10014's condition (a), "the frame group is the full Spin(2N)", holds **for the dial space**. #10014's representation-level conclusions then apply to the dial content under its condition (b), which it calls "an inserted identification, borderline": "The anomaly, chirality and protection results are statements about the representation, so they survive unchanged." The protection is exact, because the frame group is exact. It is not "the tuned smallness that M4 forbids".

**Lemma 8.1 (non-dial modes give no dial mass).** An `SO(10)`-invariant Hermitian quadratic form in dial and non-dial Majoranas has no dial-non-dial terms.

*Proof.* Its dial-non-dial block `K` (ten rows) satisfies `RK = K` for every `R ∈ SO(10)`, since the non-dial modes are frame singlets. Each column of `K` is then a vector of `R^{10}` fixed by `SO(10)`, hence zero. ∎

Three limits stay as they were. W7: "Protection therefore needs the same parity half on every cluster, which is a uniformity rule." Under `L5-U`, Proposition D: "the no-mass condition does not select five". And #10014's selector, read on the whole block, concerns all 27 modes and so `Spin(54)`; the number five then comes from the choice of dial space (section 7), not from the selector.

### 8.2 The 16

Through `ι`, Theorem 5.1(6) transfers F and K, SC and Σ. One fact is new and short: the matter factor of the local centre implementer `ι(z_X)` is the scalar `−1` on the whole fine Fock space, since `exp(2πi(n − 1/2)) = −1` for a number operator `n` (F and K: "The site factor of `z_x` is scalar, so it acts trivially on matter"). So conjugation by `ι(z_X)` fixes dial and non-dial matter alike. So spinor class at `X` is decided by bridge-register content alone, exactly as in `LW1_5.md`. With end-pure registers every local operator is tensor class; with mixed registers, spinor-class operators change a centre sector that the tick conserves (SC: "A spinor-class charge does not move"). The non-dial modes add no spinor-class operators. **The block route changes the Qubit side of PS-5 and leaves the 16 side where it was:** LW1-5-16 and the owner reading R-CG1 are unchanged, and so are #10027's three routes.

One observation, not developed: blocks make room for more dials than five. A block structure with sixteen dials per coarse site, with a frame group `Spin(10)` acting on them through the half-spin representation, would make single fermions carry the 16; this is #10027's route 3 in block form. Theorem 4.3 allows it only with at least 11 non-dial modes per coarse site (27 is the smallest cube above 16). It needs a coarse law whose exact frame group is `Spin(10)` inside `U(16)`, for instance a `U(16)`-breaking, `Spin(10)`-invariant gate, in the way #9926's det term breaks `U(3)` to `SU(3)`. No such law is built here, and #10029 notes that "An emergent Spin(10) of free Weyl modes is always part of an emergent U(16)". Section 9 tests the choice.

### 8.3 The zoom

The brief allows "an emergent one in the sense of ZM1 zoom (ZM1-I1[a])". Theorem 5.1 gives exact frames, so the existence question does not need the zoom. Two precise remarks.
1. `ZM1.md` Definition Z asks (G1), "`Φ(G^{(1),T}_u) = sum_{x in S_u} G^T_x`", a map from coarse Gauss generators to sums of fine ones. The fine block laws here have no fine-rung Gauss generators: PS-6 is read at the block rung. Also `ι` intertwines one coarse tick with one fine tick, not with `L` fine ticks. So `ι` is not a ZM1 block map; ZM1-I1[a] is neither used nor touched.
2. `ZM1.md` Theorem Z3 shows that, under (G1)-(G2) and bounded coarse content, "a linear transported block average ... is never a coarse fermion field on PS-6r links once `8L^3 > (D - 1)/n_0`". The dials `c(φ_{X,j})` are linear and spread over up to 27 sites. There is no conflict, because Z3 needs fine Gauss laws. Whether a block route can also keep a Gauss law at the fine rung is not decided here.

The emergent alternative (energetic gauge protection, as in arXiv:2305.06373, or a coarse symmetry reached by a zoom) is not needed and is not built.

### 8.4 Comparison with the 7-star and the 27-cube

The two options of #10014, quoted: "The symmetric zoom alternative is the 7-star: Spin(14) on 64 = (16,(2,1)) + (16bar,(1,2)) under Spin(10) x Spin(4) (Z2). It is chiral under Spin(14) but carries mirror 16bars, and its tiling is lopsided too." And: "The smallest fully covariant passing block is 27 (the 3^3 cube, Spin(54)). That result is not a sensible world."

| Option | Fine sites per coarse site | Frame on | Lifts (Thm 5.1) | Coarse law needed | Non-dial modes |
|---|---|---|---|---|---|
| 7-star at `3Z^3`, all modes | 27 (Thm 4.3 excludes 7) | 7 modes, `Spin(14)` | turned (Remark 5.5): `2A_1 + E + T_1` is not fixed by the stabilizer | a seven-mode analogue of `L5-O`, not in the working set | 20 spectators |
| 27-cube, all modes | 27 | 27 modes, `Spin(54)` | turned: rotations permute the 27 sites | a 27-mode law, not in the working set | none |
| K-27, five dials (Thm 7.4) | 27 | 5 dials `A_1^4 ⊕ A_2`, `U(5)` or `Spin(10)` | diagonal signs | `L5-U[m]` or `L5-O[S_+]`, live | 22 per block |
| Example 6.3, five sites on a diagonal | 125 | 5 single sites, `U(5)` or `Spin(10)` | diagonal signs | `L5-U[m]` or `L5-O[S_+]`, live | 120 spectators |

What the comparison shows:
- Theorem 4.3 decides the tiling question for both of #10014's options: 7 is not a cube, so 7-stars need spectators; 27 is a cube, so 27-cubes tile with a simple cubic coarse lattice and all 24 rotations.
- On the same `3^3` block, the five-dial route (K-27) and the `Spin(54)` route differ only in which modes the frame acts on. That is a reading of "frame cell", the same reading that decides whether #10014's selector returns 5 or 27.
- Of the four rows, only the five-dial rows run on a law the working set already has. The 7-star row also keeps #10014's "mirror 16bars".

## 9. Candidates for the owner, four-tested

Nothing here is adopted. Test 1 fails a text that states or fixes a part's target; test 2 one that is open-ended; test 3 one that settles a downstream physics question by premise; test 4 one that adds structure or constants its own reasons do not need. P = pass, C = conditional, F = fail.

**K-NN (NN-a read at the fine scale).** "GA1-P-NN applies with `F_x = ΛC^1` on one-mode fine sites; the local gauge generators it names are those of the block rung." This is the reading the brief already directs.
- Test 1: P. It names no group, species or number.
- Test 2: P. Support, parity and depth are fixed as in GA1-P-NN.
- Test 3: C. It makes compiled laws nearest-neighbour laws, which is what turns #10014's "at most emergent" into exact (Theorem 5.1). That is the same compilation convention GA1-P-NN's own test 3 recorded as conditional.
- Test 4: P. It uses the existing factors.

**K-RUNG (PS-6 at the block rung).** "The internal frame of the dials of each coarse site is local. Each coarse link carries a register that transports dial frames between its two coarse sites. The update is unchanged when the dial frame at one coarse site and the registers on its coarse links are changed together. Each fine site keeps one mode." This is #10014's "coarse-rung rule that makes a cluster the "site"".
- Test 1: P as written. It names no group and no number.
- Test 2: F alone, C with K-DIAL. "The dials of each coarse site" is undefined until a dial rule fixes them.
- Test 3: P. The gauge group, the 16 and chirality stay open (8.2).
- Test 4: C. It adds a rung. Its reason, keeping Qubit while keeping non-abelian frames, needs some rung; Theorem 4.3 shows the non-dial modes it brings are forced, not added.

**K-DIAL (the dial rule).** "Blocks are the cubes of side three centred at sites. The dials of a block are the modes of the block that every proper rotation of the block about its centre multiplies by a phase."
- What it gives: the sum of the one-dimensional isotypic components, `A_1^4 ⊕ A_2`, five dials (Theorem 7.4). Every one-dimensional character of `O` is trivial on the order-three rotations (they lie in the commutator subgroup `T`), so (B1) holds automatically.
- Test 1: C. The text states no target. But the side three was chosen knowing it gives five: the same rule gives 1, 2, 5, 8 and 15 dials for sides 1 to 5. A target-free variant replaces "side three" by "the smallest cube centred at a site and larger than the site", which also gives side three. The owner should weigh that this variant was found by looking for five.
- Test 2: P. Closed.
- Test 3: P. It settles no dynamics, vacuum or charge question.
- Test 4: C. The 22 other modes of each block get no role from the rule's reasons. In K-27 none of them is decoupled from the dials at the level of fine sites: each fine site overlaps a dial, because every shell of the cube carries an `A_1` dial. Remark 5.6 gives them covariant dynamics if a role is wanted.

**K-SEL (the dial count from #10014's selector).** "The number of dials per coarse site is the smallest `N` for which the full `Spin(2N)` of `N` dials passes #10014's conditions (a)-(c); the dial space is a canonical, stabilizer-fixed subspace of that dimension of the smallest cube that has one."
- What it gives: `N = 5`, the `3^3` cube, dials `A_1^4 ⊕ A_2` (Proposition 7.3 makes the subspace unique on `3^3`).
- Test 1: C, for the reason D1 recorded for PS-5: "The constant 5 comes from #10014 under its conditions (a)-(c)". Condition (b) is "an inserted identification, borderline".
- Test 2: P. Test 3: P.
- Test 4: C. The same as K-DIAL.
- Under `L5-U` it does not apply: Proposition D says the selector "does not transfer to L5-U".

**K-CELL (PS-1c at the block rung).** "For a law with a block rung, PS-1c is read on coarse cells: the update is covariant under the translations of the lattice of `2 x 2 x 2` coarse cells and the proper rotations about each coarse cell centre, and its symmetry group acts transitively on coarse sites."
- Why it is needed: Proposition 5.8(a) shows that no law of Theorem 5.1 meets PS-1c's transitivity at the fine scale.
- Test 1: P. It names no target.
- Test 2: P with K-RUNG, which fixes the rung.
- Test 3: C. It decides by premise that transitivity on fine sites is not required. That is an axiom-level reading, not a physics result, and it is the reading the owner's note on superlattice cells points to: superlattice cells are "never a cost" (`TOE_ASSEMBLY.md`, PS-5).
- Test 4: P. It moves PS-1c's existing text up one rung and adds nothing.

**K-16 (recorded, failing).** "The frame group of a sixteen-dial block is `Spin(10)`, acting through the half-spin representation." Test 1: F. It names the group and the target. Not proposed.

**Combined reading.** K-NN, K-RUNG, K-CELL and K-DIAL (or K-SEL) together give a complete alternative to PS-5's Qubit bend: one mode per fine site, five dials per `3^3` block, either live law at the block rung (Theorem 7.4). Each piece passes or is conditional; none fails.

## FINISH

**Proved** (here, pass 1, not yet distilled or refereed).
1. *Orbits, scale-free* (Lemma 4.1, Corollary 4.1a). No five distinct points of `R^3` are invariant under the 24 rotations about a point. Five spatially separate blocks therefore fail at any coarse site fixed by all 24 rotations (Corollary 6.1).
2. *Index, scale-free* (Theorem 4.3, Corollary 6.2). If coarse sites form a simple cubic lattice on which a fine cell group with all 24 rotations acts by isometries, the number of fine sites per coarse site is a perfect cube. So 5, 7 and 16 are excluded, and every coarse site has at least three non-dial modes. The same holds one rung up: blocks that form a cubic lattice cannot be grouped five at a time.
3. *Schur and the bond graph* (Lemma 4.4, table in 4.3). W5's Schur step is scale-free. Its "N = 1" step and W6's K(5,5) step need one-mode-per-site clusters and per-gate invariance; NN-a removes the second.
4. *Compilation* (Lemmas 5.2-5.4, Theorem 5.1). Every even unitary on a connected set of one-mode sites with link registers, with equal determinants on the two parity sectors, is a finite product of nearest-neighbour gates. Hence both live laws, `L5-U[m]` and `L5-O[S_+]`, run on one-mode sites as NN-a laws with an exact `U(5)` or `Spin(10)` frame group on five dials per coarse site, cell covariant, with finite registers, and with every `LW1_5.md` result transferred through `ι`.
5. *Option (a)* (section 6). Realizable: five single sites on the diagonal of each coarse site's stabilizer, under the live laws' own cell group (Example 6.3); five `3^3` cubes in a 1 + 1 + 3 pattern with turned register lifts (Example 6.4, Remark 5.5).
6. *Option (b)* (section 7). Canonical means a sum of isotypic components (Lemma 7.2). The canonical five-dimensional subspaces of the octahedron, 7-star and `n^3` cubes, `n ≤ 5`, under `O` and `O_h` are listed in 7.2. Those fixed by the live laws' coarse-site stabilizer lie in `A_1 ⊕ A_2` (Proposition 7.3): exactly `A_1^4 ⊕ A_2` on `3^3` and `A_2^5` on `5^3`. K-27 (Theorem 7.4): `3^3` blocks tile `Z^3`, the dials `A_1^4 ⊕ A_2` carry an exact `U(5)` or `Spin(10)`, the lifts are diagonal signs, and there are no spectators.
7. *Inheritance* (Lemma 8.1, 8.2). Non-dial modes give the dials no invariant bilinear mass and add no spinor-class operators. The 16 question is unchanged.
8. *PS-1c at the fine scale* (Lemma 5.7, Proposition 5.8). No law of Theorem 5.1 acts transitively on fine sites. A block route that does needs eight-site blocks and a coarse law covariant under coarse translations of index at most two.

**Counterexamples.**
- To #10014's "So Spin(10) on a spread cluster can be at most emergent", read for NN-a laws: Theorems 5.1 and 7.4 give exact frames. #10014's own setting, a nearest-neighbour coupling invariant term by term, is not contradicted.
- To "The best 5-site tiling keeps 8/48", read as a bound on covariant arrangements once spectators are allowed: Example 6.3 keeps all 24 proper rotations. In #10014's own setting (lattice tilings, no spectators) Theorem 4.3 confirms the obstruction and extends it to all tilings.
- Narrowing, not a counterexample: #10014's "Fully O_h-covariant tiling blocks up to size 30 have sizes 8, 16, 27". With a simple cubic coarse lattice, size 16 is excluded (Theorem 4.3).

**Open by name.** **CG16K-T** (5.4): a coarse law with an exact `U(5)` or `Spin(10)` frame group, faithful hops and finite depth, covariant under all coarse translations or the index-two lattice `F`, with the 24 rotations. Only such a law could give a block route that also meets PS-1c's transitivity at the fine scale (Proposition 5.8(b)). Three attacks failed. (A) *Mutually commuting gates*, so that every order of layers is covariant: faithful hops on two links that share a site do not commute. (B) *The exponential of a covariant gauge-invariant Hamiltonian*: exactly covariant and gauge invariant, but not of finite depth, so not NN-a. (C) *Layer orders fixed by the point group*: a rotation about a site sends a cube of one two-tiling scheme to a cube of neither tiling (for `C_4` about `e_3`, `[0,1]^3 ↦ [−1,0]×[0,1]×[0,1]`), so the cube tick's layer order is not preserved. No counterexample is known. Owner questions: K-NN, K-RUNG, K-CELL, and K-DIAL or K-SEL (section 9). Inherited through `ι`, unchanged: LW1-5-T, LW1-5-X-B_m, LW1-5-X-O, LW1-5-16 with R-CG1, GA1-P-5 (plaquettes), VC1. Not attacked here, recorded as an observation only: a coarse law with exact `Spin(10)` inside `U(16)` on sixteen dials (8.2).

**What changes downstream.**
- **PS-5.** The fallback text bends Qubit. K-27 is an alternative that keeps one mode per fine site and runs either live law at the block rung, at the price of K-NN, K-RUNG, K-CELL and a dial rule. If the owner adopts them, the frame group no longer needs the Qubit bend, and every LW1-5 result transfers (Theorem 5.1(6)).
- **#10014's verdict** "The 5 does not come from site clusters without a lopsided choice. As a per-site multiplicity it bends the Qubit axiom." Under NN-a it narrows to: five dials come from blocks with exact frames and all 24 rotations; what remains is the choice of dial rule (section 9).
- **CG1, MT1-ii.** Unchanged. "the spinor 16 rather than the vector 10" stays open, with #10027's three routes; route 3 has a block form (8.2).
- **MT1-i.** Unchanged: the fine sites carry one CAR mode each, as in `L_cube`.
- **GA1, GA2.** `U(5)` and `Spin(10)` are available at the block rung on one-mode sites. ZM1-I1[a] is untouched (8.3).
- **PS-1c.** The block route needs PS-1c read at the block rung (K-CELL). At the fine scale its transitivity fails for every law built from the live laws (Proposition 5.8); the alternative is CG16K-T.
- **B5B.** Unchanged; it concerns `L_cube`.
