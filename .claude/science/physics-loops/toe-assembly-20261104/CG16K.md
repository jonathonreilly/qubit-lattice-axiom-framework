# CG1-16-K. Five neighbourhoods and collective block modes

## 0. Status

**Pass 2; not refereed or frozen.** The constructions below are conditional mathematics. They do not adopt a law, a reading, or an axiom, and do not establish CG1's physical family.

**Proved here, subject to the stated coarse-law inputs:** the orbit and commutant lemmas; a rational-cube density identity and the exclusion of equal-size 5-, 7-, and 16-site cubic coarse tilings; the connected-set even-gate compilation lemma; exact block-scale frame *actions* for the base ticks, with the explicit geometry below; the canonical-subspace classification and the table; and the singlet bilinear observation. The group on the CAR algebra is `SO(10)`, with a `Spin(10)` implementation, not a faithful `Spin(10)` action. These results do not impose fine-site transitivity.

**GAP.** Draft Theorem 4.3 deduces `k_eff >= 8` from `k_eff >= 5` and `k_eff` being a rational cube. This inference is false: `(7/4)^3` is between 5 and 8. The proof establishes the rational-cube identity, not its claimed general non-dial lower bound. The draft's proposed 11 non-dial modes for sixteen dials also does not follow. The transitivity conclusions have separate short repairs below. The draft's finite-gate upper bound for `L5-O` cites a generator-level result and is not established at arbitrary gate angles. The optional plaquette extension lacks a stated uniformly bounded compilation-support hypothesis. The broad transfer of every `LW1_5.md` statement is too strong without checking its hypotheses and meaning on the full fine algebra.

**Open by name.** CG16K-T; LW1-5-T; LW1-5-X-B_m; LW1-5-X-O; LW1-5-16 and R-CG1; GA1-P-5; VC1; CG1-i/P-HY; CG1-ii/P-COMP; MT1-ii; ZM1-I1[a]; RCS-P and MT1-S[R-CS^str]. K-NN, K-RUNG, K-CELL, K-DIAL and K-SEL are proposed readings, not decisions. K-16 fails its stated test and is not proposed. A sixteen-dial half-spin law and a fine-rung Gauss-law version are also open.

**Provenance.** Pass 1: `CG16K_DRAFT.md`, Claude Opus 5.5, 2026-11-07, reporting checkout `15bc39079` and source `7086189d1`. Pass 2: gpt-6.1-terra; effort and session id: see run log. No git commands were run in this pass; source freshness relative to remote refs was not checked. The local working-set and frozen notes are inputs, not independently re-certified here. A fresh referee is still required.

## 1. Definitions inferred by the distiller

1. `O` is the 24 proper signed coordinate permutations; `O_h = O × {±1}`. A fine cell group is `G = Λ ⋊ O_c`, where `Λ ⊂ Z³` is a finite-index `O`-invariant lattice and `c` is a site or cube centre. A coarse cubic structure is a bijection `κ: X → Z³` and a homomorphism `π: G → Z³ ⋊ O_h` intertwining the actions, whose linear parts contain `O`.
2. Each fine site carries one CAR mode. Finite link registers commute with matter. Coarse sites `X` have disjoint finite nonempty supports, transported by `G`, and orthogonal five-dimensional subspaces `V_X ⊂ ℓ²(supp X)`, also transported by `G`. Let `W = (⊕_X V_X)^⊥`. Sites outside every block are spectators; `W` also includes non-dial combinations inside blocks.
3. Five neighbourhoods means five specified disjoint supports of an orthonormal dial basis, permuted by `G`. They are spatially separate if their centroids are distinct. A collective dial space is **canonical** under a finite group `H` if it is invariant under `H` and under every unitary commuting with `H`. This is a proposed precise meaning of “without a choice”, not a physical selection rule.
4. A dial frame preserves `CAR(V_X)` and fixes all other dial CAR algebras, `CAR(W)`, and registers. Compatibility with a gate means that a finite register-only unitary change, composed with the frame, fixes that gate. `U(5)` acts by number-preserving Bogoliubov transformations; the ten dial Majoranas carry `SO(10)`, covered by `Spin(10)`.
5. A fine block law has finite link registers and a fixed finite number of layers of even unitaries on pairwise disjoint nearest-neighbour edge triples. Its complete update fixes its block Gauss generators and commutes with the stated fine cell lifts. The intermediate gates need not do either. This is the **proposed** application K-NN of NN-a to one-mode fine sites and block generators: the actual owner text in `TOE_ASSEMBLY.md` §3.7 explicitly names five-mode sites. The fine group used below is a superlattice cell group, not the full fine-site PS-1c transitivity assertion.
6. The coarse inputs are the base ticks `L5-U[m]`, `1 ≤ m ≤ 9`, and `L5-O[S_+]` of `LW1_5.md`, with their stated parameter and covariance hypotheses. Their finite registers, gauge generators and site-frame results are imported. The embedding `ι` sends coarse modes to an orthonormal dial basis and coarse link registers to selected fine bridge registers. It is a CAR *-isomorphism onto its image; even elements of the image commute with `CAR(W)`.
7. For the density theorem, `T` consists of translations in `Λ` whose `π`-images have trivial linear part, and `k_eff = [Z³:T]/|X/T|`. It is an average fine-site density per coarse site, including spectators, not necessarily an integer or the size of an individual block.

## 2. Orbit, density and Schur obstructions

**Theorem 2.1 (orbits).** The orbit of a point under `O_c` has size 1, 6, 8, 12 or 24; only `c` has orbit size 1. No invariant set of five distinct points exists.

*Proof.* A noncentral point's stabilizer consists of rotations about its line from `c`. The possible axis orders are 4, 3, 2 and 1. Orbit-stabilizer gives 6, 8, 12 and 24. An invariant set is a union of orbits and contains at most one singleton. □

Thus a coarse site with full `O` stabilizer cannot permute five neighbourhoods with distinct centroids: its stabilizer fixes the centroid of its finite support, and Theorem 2.1 applies. This holds at any length scale. `LW1.md` A2 already proves that the live coarse cell group's site stabilizer has order three, so that group avoids this particular premise.

**Lemma 2.2 (cubic commutant).** A real `3 × 3` matrix commuting with `O` is scalar.

*Proof.* The three diagonal half-turns kill off-diagonal entries; cyclic coordinate permutation equates the diagonal entries. □

**Theorem 2.3 (density).** Under Definitions 1–2 and 7, `k_eff` is a positive rational cube and is at least 5. If it is an integer, it is a perfect integer cube. In particular an equal-size partition into 5, 7 or 16 sites per coarse site is impossible under these hypotheses.

*Proof.* The finite point group makes `T` finite index. The image of `t ∈ T` is translation by `τ(t)`; `τ` is injective, because a nonzero translation cannot preserve any nonempty finite block. Let `A` be its rational linear extension. Conjugacy gives `AQ = Ψ(g)A` for an element `g` with linear part `Q`, where `Ψ(g)` is orthogonal. Thus `AᵀA` commutes with every `Q ∈ O`, and Lemma 2.2 gives `AᵀA = μI`, `μ ∈ Q_{>0}`. Comparing covolumes,
`|X/T| = [Z³:τ(T)] = μ^(3/2)[Z³:T]`, so `k_eff = μ^(-3/2)`. Since `μ` and `μ^(3/2)` are rational, `sqrt(μ)` is rational. If a rational cube is an integer its cube root is an integer. Finally, disjoint equivariant blocks supply at least five distinct fine-site orbits per coarse orbit, so `k_eff ≥ 5`. □

**GAP and correction.** The draft takes the smallest *integer* cube above 5 even when `k_eff` is not known to be integral. Neither `k_eff ≥ 8` nor three extra modes per coarse site follows in general. For an equal-size tiling the density is its integer block size, so the stated 5, 7 and 16 exclusions do follow. The same proof applied to two equivariant cubic structures shows that their ratio of site densities is a rational cube: hence five neighbourhoods per coarse site cannot themselves form a second cubic lattice with the specified full cubic covariance. This is a restriction on that class, not on all arrangements of five neighbourhoods.

**Lemma 2.4 (Schur step).** A real matrix commuting with all of `SO(n)`, `n ≥ 3`, is scalar; a complex matrix commuting with `U(N)` is scalar.

*Proof.* Diagonal half-turns, respectively independent unitary phases, kill off-diagonal entries. Signed permutations, respectively permutations, equate diagonal entries. □

This reproduces #10014's common-frame mode-diagonal step at block scale. Its further inference from a mode-diagonal hop to `N=1` assumes a direct single fine-bond bilinear. The `K(5,5)` argument likewise addresses direct fine-bond couplings. NN-a permits a whole coarse gate to be a product of gauge-variant fine gates. The graph observation that two distinct cubic-lattice sites have at most two common neighbours remains true; it does not itself rule out such a compiled gate. The source's spread-cluster claim in its direct-coupling scope is not refuted.

## 3. Finite compilation and exact frame actions

**Theorem 3.1 (connected-set compilation).** Let `S` be a finite connected fine-site graph, `|S| ≥ 3`, with finite registers on edges. Every even unitary whose determinants on the two total-matter-parity sectors are equal is an exact finite product of even nearest-neighbour edge-triple unitaries.

*Proof.* Let `P` be total parity, and let `m_A` be Hermitian Majorana monomials of even degree. Their products with Hermitian register operators span the even Hermitian algebra. Edge gates contain all local quadratic monomials, a quartic on each edge, and arbitrary operators on its register. Brackets of overlapping quadratics generate every quadratic on connected `S`. Bracketing with quadratics replaces any one Majorana index; bracketing a degree `2r` monomial with a quartic sharing exactly one index raises the degree to `2r+2`, up to degree `2|S|-2`. The same operations carry each edge-register operator along. For different registers, brackets of monomials with one common Majorana multiply their commuting register factors, generating all register tensor products at every intermediate degree. Equal-degree brackets with the same matter monomial generate traceless register operators at matter degree zero; brackets of complementary monomials generate traceless register operators at full parity degree. Thus the generated Lie algebra is all even anti-Hermitians except the scalar parity direction `iP ⊗ 1`. Conversely every edge generator is orthogonal to that direction because at least one matter site lies outside the edge.

The corresponding group consists of parity-block unitaries with equal determinants. It is connected: factor out a common phase, leaving a pair of special unitary matrices. A subgroup generated by one-parameter subgroups whose generators span a connected matrix group's Lie algebra contains a neighbourhood of the identity: conjugates of those generators span the algebra, and the inverse function theorem applies to their product map. An open subgroup of a connected group is the whole group. Therefore each desired unitary is a finite product, exactly, not merely a limit. □

**Theorem 3.2 (conditional block compilation).** Suppose (i) `π` identifies the fine cell group with the coarse group `2Z³ ⋊ O_{c0}` and maps translations onto `2Z³`; (ii) each coarse site has a dial basis fixed by its stabilizer and transported to the other sites; and (iii) every coarse link has an equivariant fine bridge, while each coarse cube has a connected finite fine support containing its eight blocks and twelve bridges, disjoint from supports of other cubes in the same tiling. Assume these supports and bridge assignments are periodic with finitely many shapes. Then the base tick of either coarse law embeds as a finite-depth NN-a fine update. It acts on the dial and bridge algebra as the coarse tick, fixes `CAR(W)`, and has the corresponding exact local `U(5)` or `SO(10)` frame action with compensating register changes. It is covariant under the specified fine cell group.

*Proof.* Orthonormality gives the CAR embedding. Place each coarse register on its bridge. Each embedded cube Hamiltonian is even and quadratic in matter, with register coefficients. Its trace against total parity on the connected support is zero: every quadratic term leaves at least one of the many matter modes outside its support, or has zero occupation-diagonal trace. Its exponential has equal parity-sector determinants. Theorem 3.1 compiles it exactly. Translate a fixed finite word over the disjoint supports of each tiling; this gives finitely many fine layers independent of volume. Register-only electric gates form a layer. Infinite products define local automorphisms as in `LW1.md` E1. The whole embedded tick fixes `CAR(W)` because it is even.

Transported bases and bridge registers intertwine fine lifts with coarse lifts, including the coarse site signs. The coarse update's covariance then gives fine covariance on the embedded algebra; both sides agree on `CAR(W)`. The embedded coarse Gauss generators commute with each complete coarse gate, giving the exact frame action and register compensation at every angle. The conclusion imports the named gauge identities of `LW1_5.md` U, Q and G. □

The `U(5)` gate-wise upper bound transfers only under `LW1_5.md` M/M.1's faithful-inflow and exceptional-angle hypotheses. The draft cites `LW1_5.md` R for an `SO(10)` finite-gate upper bound, but R is stated at generator level; that does not by itself classify all frames of an exponential at arbitrary angles. The exact subgroup action above remains proved. A supplied plaquette layer needs its own bounded-support, finite-colouring and parity-determinant checks; Theorem 3.2 makes no unconditional claim about it. Only results whose hypotheses survive `ι` transfer to the embedded subsystem; statements about full fine states, locality, observables or all fine frames require separate checks. The centre and sector results quoted in §6 have that restricted meaning.

For bases that rotate by a cocycle `u(g,X) ∈ U(5)`, the same construction can use the corresponding local gauge compensation on bridge registers, provided those register lifts form a consistent group action. This is the draft's proposed turned-lift construction; its group-law and bridge orientation must be checked in each example. It is not needed for K-27.

**Theorem 3.3 (transitivity constraints).** For the block structures of Theorem 3.2 the specified fine cell group is not transitive on fine sites. More generally, if a cell group with the cubic structures of §1 is transitive on fine sites, then `k_eff = 8` and its coarse translation image is either all `Z³` or the index-two even-sum lattice `F`.

*Proof.* Translations commute, so the linear part of every image of `Λ` fixes the full-rank lattice `τ(T)` pointwise. It is the identity, hence `T=Λ`. For Theorem 3.2, `π(Λ)=2Z³`, so `[Z³:Λ]=8k_eff`. Write `k_eff=(p/q)³` in lowest terms. Since the index is the integer `(2p/q)³`, `q` divides 2. If `q=1`, `k_eff ≥ 5` gives `p≥2` and index at least 64; if `q=2`, `p³/8 ≥ 5` gives `p≥5` and index at least 125. One `G`-orbit meets at most 24 classes modulo `Λ`, so transitivity fails.

For a transitive group, `[Z³:Λ] ≤ 24`. Write `k_eff=(p/q)³`; if `m=[Z³:π(Λ)]`, then `[Z³:Λ]=mp³/q³`, so `q³` divides `m` and the index is a positive multiple of `p³`. Since `k_eff ≥5`, `p≥2`; the index bound forces `p=2`, and then `q=1`. Thus `k_eff=8` and `m≤3`. An `O`-invariant sublattice of index 2 is `F`: mod 2 the defining nonzero functional must be permutation-invariant. Index 3 is impossible: its invariant normal line over `F_3` would have to be fixed by all diagonal half-turns, forcing a coordinate line, which a cyclic permutation moves. □

This repairs the draft's conclusions without its invalid integer-density inference. It does not prove that a larger symmetry group of a particular update cannot act transitively, nor that a suitable coarse law exists.

## 4. Five separate neighbourhoods

**Example 4.1 (five sites on a diagonal).** Let `c'` be a fine cube centre and `G=10Z³ ⋊ O_{c'}`. Take coarse positions `p=c'+(5/2)σ+10Z³`, `σ∈{±1}³`, and dials at `p+kσ`, `k=-2,-1,0,1,2`. Their centroids are distinct. For distinct signs in one `10³` cell, equality would require `k+k'=-5`, impossible. Across cells, every coordinate relative to `c'` has magnitude at most `9/2`, so the sites remain disjoint. The order-three stabilizer of `p` fixes all five sites. Coarse positions are spaced by 5; use the middle fine edge of each coarse link as its bridge. The box containing the rods at the eight corners of a coarse cube is a connected `10³` box; boxes in one tiling are disjoint and contain those bridges. Thus Theorem 3.2 applies. There are 40 dial sites and 960 spectators per fine `10³` cell. □

This exhibits exact actions on five single-site neighbourhoods with all 24 proper rotations in the specified superlattice cell group. It does not establish fine-site transitivity. The draft also proposes five `3³` neighbourhoods in a `1+1+3` arrangement with coarse spacing 21: centres `p`, `p+3σ`, and `p-3σ_i e_i`. Their uniform modes are disjoint and the stabilizer cyclically permutes the last three. This arrangement fails the fixed-basis hypothesis of Theorem 3.2; its turned-register lift needs the separate consistency check stated above. It is not a second established application of that theorem here.

## 5. Collective dials and cubic representations

**Lemma 5.1 (orbit representations).** With class order `E, 8C3, 3C2, 6C4, 6C2'`, the irreducible characters of `O` are

| | E | C3 | C2 | C4 | C2' |
|---|---:|---:|---:|---:|---:|
| A1 | 1 | 1 | 1 | 1 | 1 |
| A2 | 1 | 1 | 1 | -1 | -1 |
| E | 2 | -1 | 2 | 0 | 0 |
| T1 | 3 | 0 | -1 | 1 | -1 |
| T2 | 3 | 0 | -1 | -1 | 1 |

The permutation representations of the centre and of orbits of size 6, 8, 12 and 24 are, respectively,
`A1`; `A1+E+T1`; `A1+A2+T1+T2`; `A1+E+T1+2T2`; `A1+A2+2E+3T1+3T2`.

*Proof.* `T1` is the defining rotation representation, `A2` is the sign of the quotient by the tetrahedral subgroup, `T2=T1⊗A2`, and the remaining character follows by orthogonality. The multiplicity of `ρ` in an orbit with stabilizer `H` is `|H|^-1 Σ_{h∈H} χρ(h)`. Apply this to stabilizers `O`, `C4`, `C3`, face-axis `C2'`, and the identity. □

The once-per-orbit `A1` count is already recorded in the repository as #10026, in `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` (pass-1 source revision; not available as a checked-out file here). The octahedral `E+T1` and the corner-cube `A1+A2+T1` are also recorded there as #10029/#10019 and corrected #9894, respectively. These citations report the prior source, not an independent check of its current revision.

**Lemma 5.2 (canonical subspaces).** A canonical subspace in Definition 3 is exactly a sum of complete isotypic components.

*Proof.* Every equivariant unitary preserves each isotypic component. Conversely, the unitary `2Πρ-1` separates each isotypic projection. Within `C^{mρ}⊗ρ`, the commutant contains all multiplicity-space unitaries; their linear span gives all matrix units. The group action is irreducible on `ρ`. Invariance under both therefore forces the component to be zero or the whole isotypic space. □

**Theorem 5.3 (finite block census).** The following table lists all canonical five-dimensional subspaces for the stated action. Superscripts denote multiplicities, not powers.

| block | `O` isotypic dimensions `(A1,A2,E,T1,T2)` | canonical 5-spaces under `O` | under `O_h` |
|---|---|---|---|
| 6-site octahedron | `(1,0,2,3,0)` | `E+T1` | `E_g+T1_u` |
| 7-star | `(2,0,2,3,0)` | `A1²+T1`; `E+T1` | `A1_g²+T1_u`; `E_g+T1_u` |
| `2³` cube | `(1,1,0,3,3)` | `A1+A2+T1`; `A1+A2+T2` | `1,xyz` plus `x,y,z` or `xy,yz,zx` |
| `3³` cube | `(4,1,4,9,9)` | `A1⁴+A2`; `E²+A2` | `A1_g⁴+A2_u`; `E_g²+A2_u` |
| `4³` cube | `(4,4,8,24,24)` | none | none |
| `5³` cube | `(10,5,20,45,45)` | `A2⁵` | `A2_g+A2_u⁴`; `A2_g+E_u²` |

*Proof.* Decompose into orbits and sum Lemma 5.1. The `3³` cube has centre, face, edge and corner orbits; `4³` has two 8-orbits and two 24-orbits; `5³` has one centre, two each of 6-, 12- and 8-orbits, and three 24-orbits. Lemma 5.2 reduces the answer to subset sums of the isotypic dimensions. For inversion, use even/odd functions on each orbit. For `4³` the split dimensions are `A1_g:4, A2_u:4, E_g:4, E_u:4, T1_g:6, T1_u:18, T2_g:18, T2_u:6`; none sum to five. For `5³` they are `A1_g:10, A2_g:1, A2_u:4, E_g:16, E_u:4, T1_g:9, T1_u:36, T2_g:27, T2_u:18`. The two subset sums shown are exhaustive. □

The draft reports an exact-rational character script in `/tmp/toe-CG16K/check_iso.py` reproducing its table. This pass did not rerun it; the proof above uses character averages. Two canonical answers do not give a unique dial rule, even though both are defined without choosing a basis.

**Proposition 5.4 (order-three stabilizer).** A canonical `O`-subspace is pointwise fixed by a body-diagonal order-three rotation exactly when it lies in the sum of its `A1` and `A2` components. In the table the fixed five-spaces are `A1⁴+A2` on `3³` and `A2⁵` on `5³`.

*Proof.* For an isotypic component, pointwise fixing is equivalent to its character at `C3` equalling its dimension. The character table gives this precisely for `A1` and `A2`. Apply the subset sums in Theorem 5.3. □

**Theorem 5.5 (K-27).** Let fine `3³` cubes centred at `p_X` tile `Z³`, with `G=6Z³ ⋊ O_{c'}` and coarse centres `p_X ∈ c'+(3/2)(1,1,1)+3Z³`. On each cube use the four normalised shell sums for the centre, six faces, twelve edges and eight corners, and the normalised corner alternation `v1v2v3/√8`. Then these five dials support the exact frame actions of Theorem 3.2; each cube has 22 non-dial modes and there are no spectators.

*Proof.* The first four vectors have disjoint support; the alternation is orthogonal to the corner sum and has norm one. They span `A1⁴+A2`. The coarse stabilizer is the order-three rotation about the body diagonal through `c'` and `p_X`, which fixes all five vectors. Transport the basis: the fifth vector may acquire an `A2` sign, which is part of the transported basis. Neighbouring blocks share a face; use the fine edge joining their face centres as bridge. The eight blocks of a coarse cube form a connected `6³` box, disjoint from others in its tiling. Fine translations by `6Z³` map to coarse translations by `2Z³`. Theorem 3.2 applies. □

The same geometry with side-five cubes and `A2⁵` satisfies the fixed-stabilizer condition and uses the same bridge construction. Side three is the smallest site-centred odd cube larger than a site, and the smallest cube in the listed census with a canonical stabilizer-fixed five-space; neither fact supplies a physical selection rule.

## 6. Protection, the 16, and the zoom

**Lemma 6.1.** An `SO(10)`-invariant Hermitian quadratic form has no cross term between the ten dial Majoranas and frame-singlet non-dial Majoranas.

*Proof.* Each column of its cross matrix is a vector fixed by all of `SO(10)`, hence zero. □

The conditional representation-level protection of #10014 is not a physical particle result: it assumes its parity-half Weyl-species identification. Uniformity of the parity half remains an extra rule. `LW1_5.md` Proposition D already proves that the corresponding no-mass criterion does not select five for the U-law. The full 27-mode block is not a five-mode system; selecting the five-dimensional dial subspace is supplied structure.

For the O-law the matter part of the local central implementer is scalar `-1`: each factor `exp(2πi(n-1/2))` is `-1`. It therefore fixes dial and non-dial matter under conjugation. The `LW1_5.md` F/K and SC conclusions on tensor classes and conserved centre sectors apply to the embedded coarse algebra under their original register and gate hypotheses. Mixed end registers can contain spinor-class operators, but the cited construction alone gives no mobile charge. The digest `prior/CG16K.md` identifies the earlier centre obstruction in `docs/SPIN10_MOTT_SITES_CARRY_NO_COMPOSITE_SIXTEEN_THE_CENTRE_FIXES_EVERY_FERMION_TO_THE_VECTOR_CLASS_BOUNDED_THEOREM_NOTE_2026-10-22.md` and the existing subgroup-family operators in `CH1.md` Theorem F. It also records `MT1.md` Theorem 11's free vector content. These do not prove a light chiral 16; the digest's three escape routes remain open.

A sixteen-dial block carrying the half-spin representation is a proposed route, not a construction. An exact `Spin(10)` subgroup of `U(16)` and a suitable law would have to be built. The density theorem excludes an equal-size 16-site cubic tiling, but does not prove the draft's general 11-non-dial lower bound.

The embedding here intertwines one coarse tick with one fine tick and supplies block, not fine-site, Gauss generators. It is not a ZM1-I1[a] block map, which compares one coarse tick with `L` fine ticks and requires its stated gauge embedding and observable estimates. `ZM1.md` Z3 excludes certain linear transported averages under its fine Gauss and finite-register hypotheses; those hypotheses are absent here. Neither result decides the other.

For comparison: a 7-star placed at `3Z³` uses 27 fine sites per coarse site with 20 spectators; a hypothetical full seven-mode frame is `Spin(14)` and retains the source's mirror-16-bar issue. A full `3³` block has 27 modes and a proposed full `Spin(54)` frame. Both need corresponding coarse laws and turned lifts. K-27 instead uses five dials and 22 other modes with the existing five-mode base laws. The diagonal example uses 125 fine sites per coarse site, five dials and 120 spectators. These are supplied constructions, not a selection among them.

## 7. Proposed readings and remaining questions

The following are pass-1 readings and its four-test assessments, not adopted premises. Tests ask, in order, whether the text avoids stating a target, is closed, avoids settling downstream physics by premise, and avoids unnecessary added structure. `P` means pass, `C` conditional, `F` fail. These checks are assessments, not theorems.

| Name | Proposed content | Pass-1 tests | Scope of check |
|---|---|---|---|
| K-NN | Apply NN-a to one-mode fine sites and block Gauss generators. | P, P, C, P | The compilation convention admits the constructed exact frame action. The owner text itself names five-mode sites. |
| K-RUNG | Read local frames, link transport and gauge invariance at a coarse dial rung, retaining one mode at each fine site. | P, F alone/C with a dial rule, P, C | The dial space is undefined without a rule; the rung is supplied. The draft's claim that at least three extra modes are forced in general is not established. |
| K-DIAL | Use side-three site-centred cubes and the modes transformed by a phase under every proper block rotation. | C, P, P, C | These modes are `A1⁴+A2`. Side three was chosen knowing it gives five. The smallest site-centred cube larger than one site gives the same choice, but was found with that knowledge. The 22 other modes need a role. |
| K-SEL | Choose the smallest `N` passing #10014's supplied conditions, then the smallest cube with a canonical stabilizer-fixed `N`-space. | C, P, P, C | It gives five and K-27 only under #10014's conditions, including its inserted Weyl-species reading. It does not transfer to the U-law (`LW1_5.md` D). |
| K-CELL | Read PS-1c covariance and transitivity at the coarse rung. | P, P with K-RUNG, C, P | This explicitly changes which rung must be transitive; it is a proposed axiom-level reading. |
| K-16 | Specify `Spin(10)` on sixteen dials in its half-spin representation. | F, not further assessed | It names the target group and representation; not proposed. |

**GAP in K-DIAL wording.** Vectors individually multiplied by a phase by every rotation form a union of character subspaces, not in general a vector space: a nonzero `A1` vector plus a nonzero `A2` vector is not an eigenvector of a `C4` rotation. The corrected dial space is the *linear span* of those vectors, equivalently the sum of all one-dimensional isotypic components. With that correction its dimensions are 1, 2, 5, 8 and 15 for side lengths 1–5, by Theorem 5.3. Every fine site of K-27 overlaps at least one shell-sum dial, although the 22-dimensional orthogonal complement is fixed by the base construction. A block-local quadratic acting within that complement can be made covariant and compiled on a connected block; any claimed dynamics must state its own support and covariance conditions. A dial-number coupling is compatible with U(5), but not thereby proved compatible with the full O-law `SO(10)`.

**CG16K-T (open).** Find a coarse finite-depth law with faithful hops and an exact `U(5)` or `Spin(10)` frame action, all cubic rotations, and coarse translations equal to `Z³` or `F`, sufficient for a fine-transitive block realization. Theorem 3.3 gives necessary translation options under its specified hypotheses; it does not establish sufficiency or exclude other symmetry structures. The draft records three failed approaches: (A) it found faithful shared-site hops need not commute, defeating its commuting-layer proposal; (B) an exponential of a covariant Hamiltonian is not shown to have an exact finite-depth decomposition; (C) the particular two-cube tiling is not preserved by all rotations about a site, for example `[0,1]³` rotates to `[-1,0]×[0,1]×[0,1]`. These are failures of those constructions, not a no-go. No counterexample to CG16K-T is established.

The inherited open names are LW1-5-T, LW1-5-X-B_m, LW1-5-X-O, LW1-5-16 and R-CG1, GA1-P-5, and VC1. CG1-i/P-HY and CG1-ii/P-COMP still require physical hypercharge identification and law-fixed completion. MT1-ii requires physical family carriers; `RCS1.md`'s R-CS^str is a working candidate, with RCS-P and MT1-S[R-CS^str] open. `ZM1-I1[a]` remains open with its owner-selected `p=2` comparison. The construction gives no chiral spectrum, mirror gap, deconfined phase, vacuum, continuum theory, or empirical prediction.

## 8. Prior work and check boundary

The digest `prior/CG16K.md` records the earlier failed direct inter-cluster coupling (`docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`, #10014 summary), the fixed-site centre obstruction (#10027), the static-centre and odd-site tests (#10045 and #10038), and the existing `CH1.md`, `MT1.md`, `RCS1.md` and hypercharge results. They are prior results in their own scopes, not results newly derived here. `B5B.md` Theorems 3.1 and 3.3 already prove the `U(1)^8` cell-mode image for `L_cube` under their split-register hypotheses; this different law does not override them. `LW1.md` A2 and E1 supply the coarse cell geometry and infinite-layer interpretation. `LW1_5.md` supplies the two gauge laws and their named frame and sector results. `ZM1.md` Z3 supplies the separate finite-link obstruction under its explicit hypotheses. The repository paths named by the digest may refer to its captured source rather than the present checkout; no current-main claim follows from this pass.

Pass 1 reports a literature search including Bravyi–Kitaev on parity-preserving computation, Banerjee et al. and Chandrasekharan–Wiese on quantum links, Zohar et al. on digital gauge steps, Kivlichan et al. on swap networks, Halimeh et al. on energetic protection, and Baez–Huerta on spinor representations. It marked Deutsch–Barenco–Ekert's Lie argument, the similar-sublattice result, Wilczek–Zee, and perfect Lee codes unverified or unused. These are context only; the arguments above do not rely on those citations. This distillation did not refetch the literature or rerun the draft's scratch check. A fresh referee should check the full compilation proof, the exact covariance and bridge lifts, the representation table, and the imported coarse-law hypotheses before freezing.
