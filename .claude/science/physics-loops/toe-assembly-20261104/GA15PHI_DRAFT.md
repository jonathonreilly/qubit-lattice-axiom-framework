lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GA1-5-Φ: a flux-carrying propagating band in the five-mode gauge sector, pass 1

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of the TOE assembly under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-ga15phi2/`. A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| this checkout, branch `claude/toe-assembly` | `7da1a4174` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | listed in section 1 |

Files read in this checkout, by line. This folder: `prior/GA15PHI.md` lines 1-83 (all); `GA1_5.md` lines 1-385 (all; last changed `2d48e6bdc3`); `GA2_Y2.md` lines 1-57 and the theorem headings at lines 69-174; `TOE_ASSEMBLY.md` lines 231-237 (section 3.7, NN-a) and 395-399 (GA1); `LW1_5.md` lines 80-100 (both laws); `LZ1.md` lines 1-12 and 38-40 (D1 states); `Y2W_DRAFT.md` lines 1-30 (head format only).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U`, NN-a and the proposed reading R-Φ are read plainly. Section 5 records what the result says about R-Φ. It proposes no new reading for adoption.

**Working set used, by name.** PS-5 and PS-6r through the law `L5-U` of `LW1_5.md` (lines 94-100). PS-1 through the owner's NN-a text (`TOE_ASSEMBLY.md` line 235). Results used, ported with credit in section 1: `GA1_5.md` Theorem 2.1, Theorem 3.1, Theorem 6.1, Theorem 6.3, Lemma S1′, Proposition C, Proposition S-odd and the §3.9 identification step; the definitions of `GA1_5.md` §1 (D1 state, band, node, propagation, R-Φ); the D1 definition of `LZ1.md` line 40.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: Schur's lemma; isotypic decomposition of a unitary representation of a compact group; the fact that a unitary of finite order has eigenvalues that are roots of one scalar; the permutation representation of `S_3` on three points and its two-dimensional irreducible summand, used in Lemma 4.2. Literature is context only (section 2). No citation is load-bearing.

---

## 0. The question, quoted

`GA1_5.md` line 188 (section 7): "**GA1-5-Φ.** Is there a member of the proposed class and a D1 state with a propagating R-Φ band in `H_phys` on `L5-U[m]`?"

`GA1_5.md` line 59: "**Proposed R-Φ.** A band in `H_phys` is flux-carrying if its image is orthogonal to `closure π(𝒩)Ω`." Line 55 defines `𝒩` as "the union of local gauge-invariant operators commuting with every end number".

`GA1_5.md` line 57: "A band `(d,F,V)` is an isometry `F:L²(T³;C^d)→H` satisfying `T_βF=F e^{iK·β}` and `ŨF=F V(K)`, with continuous unitary `V`. A node has `V(K₀)=1` and `V` is `C¹` nearby; with `h=i log V`, propagation means some `∂_j h(K₀)≠0`."

`TOE_ASSEMBLY.md` line 235 (owner, NN-a): "Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s`, for `s∈𝒢=2Z³⋊O_{c₀}`. ... Gauge invariance and cell covariance are required of the complete update only."

**Answer in one paragraph.** For `m=2,…,8` the answer is yes: Theorem 4.5 (`m` even) and Theorem 4.6 (`m=3,5,7`). The layer is the neutral swap of `GA1_5.md` conjugated by one sublayer `G` of cube gates. Each cube gate turns the parity of two corner multiplicity qubits into a hexagonal electric flux loop. The band moves by `−2(1,1,1)` per tick, as the neutral band does. On every vector of the state's support its operator changes the end numbers by a hexagon cycle, so its vectors are orthogonal to every neutral vector. The same conjugation shows a limit of R-Φ: R-Φ is not invariant under conjugation by admissible gauge-invariant layers (section 5). For `m=1,9` the question stays open: Lemma 6.1 shows that the sector used for odd `m` is frozen there, and three attacks fail (section 6.1). `L5-O` and the electric half of GA1(a)(4) are not reached.

## 1. Prior work used

Ported with credit (this folder, commit `7da1a4174`). Each is restated where it is used and its proof step is named.

- `GA1_5.md` Theorem 2.1 (G1-G3): every link lies in exactly one tiling cube; the cube stabilizer in `𝒢` is the 24 proper rotations; the site stabilizer is cyclic of order three. Used in sections 3 and 4.2-4.4.
- `GA1_5.md` Theorem 3.1: "The proposed class defines gauge-invariant, cell-covariant quasi-local automorphisms"; and the class GA1-P-5 as defined in `GA1_5.md` §1. Used in Theorem 4.5(1).
- `GA1_5.md` Theorem 6.1 (R): for empty matter, `Ũπ(A)Ω=π(𝕍*A𝕍)Ω` with `𝕍=W_BW_E`. Used in Lemma 4.3, Theorem 4.5(3) and Lemma 6.1.
- `GA1_5.md` Theorem 6.3 and its §3.9 closure: the swap gates, their commutation, the stationary product state, and the motion `A_{2b}↦A_{2b−2(1,1,1)}`. Extended in Lemma 4.3 to a smaller support.
- `GA1_5.md` Lemma S1′ (referee closure): covariance of `W^{swap}`; and step (d), "two such induced maps agree up to a sign". Used in Lemma 4.3 and section 3.
- `GA1_5.md` Proposition C(ii) (referee closure): every member of GA1-P-5 compiles into finitely many NN-a layers. Used for admissibility.
- `GA1_5.md` §1 definitions: D1 state, band, node, propagation, R-Φ. Used as stated, not changed.

Read on `origin/main` at `f5af11cd01` (cited lines only; all four ledger rows are `unaudited` per the digest). None is used as a proof step.

- `docs/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md` lines 100-105: "`H_F-H_1-H_2=O(h^2)`". Section 6 uses it only to say which energy the electric half would have to name.
- `docs/U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md` lines 95-99: "the extended-lattice photon question" remains open. The construction below is an extended-lattice band. It is not a photon (section 5).
- `docs/ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION_BOUNDED_THEOREM_NOTE_2026-09-24.md` lines 97 and 101: `H_rot = K sum_e E_e^2 - J sum_p(W_p+W_p^dag)` and "Taking S to infinity first at fixed t,Delta would erase that coefficient." Context for section 6.
- `docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md` lines 61 and 69: its ordered limits start with "link spin `S\to\infty`", and it is "a prepared free-wave consistency construction". It needs growing registers. `L5-U` has fixed registers.

**Failed attempts on file, and the new step here.** `GA1_5.md` line 188 lists three attacks on GA1-5-Φ. Attack 1 (cube-supported gates are flat, Theorem 6.2) is respected: the layer here contains the swap, which is not cube supported. Attack 2 (disjoint covariant supports cannot move end charge between tilings) is respected: the flux here never leaves a cube of the even tiling; the swap carries the information between cubes. Attack 3 (one-qubit Clifford) is not used. The new step is conjugation of the neutral band by a cube sublayer that writes a corner parity into a flux loop (Lemma 4.4, Theorems 4.5 and 4.6). The digest's "missed inputs" are recorded in section 6.

**Prior work the digest missed.** None found in the files read. The digest records no prior result on conjugating a neutral band.

## 2. Literature

Searches run 2026-11-06 (WebSearch, standard and extended): emergent photons in quantum ice and quantum link models; Coulomb phases of `U(1)` quantum link models in 3+1 dimensions; gauge-invariant and Floquet cellular automata; QCA index theory. For each work below the arXiv abstract page was fetched, unless marked NOT VERIFIED. Only abstracts were fetched; no equation or theorem number of these works is used, so none is quoted. Nothing below is a proof step.

- Hermele, Fisher, Balents, "Pyrochlore Photons: The U(1) Spin Liquid in a S=1/2 Three-Dimensional Frustrated Magnet", arXiv:cond-mat/0305401, Phys. Rev. B 69, 064404 (2004). Abstract: an effective `U(1)` gauge theory with a gapless linearly dispersing photon, checked at a soluble Rokhsar–Kivelson-type point. A ground-state, Hamiltonian result.
- Moessner, Sondhi, "Three dimensional resonating valence bond liquids and their excitations", arXiv:cond-mat/0307592, Phys. Rev. B 68, 184512 (2003). Abstract: a `U(1)` liquid on the cubic lattice with a gapless transverse photon mode.
- Shannon, Sikora, Pollmann, Penc, Fulde, "Quantum Ice: a quantum Monte Carlo study", arXiv:1105.4196, Phys. Rev. Lett. 108, 067204 (2012). Abstract: numerical evidence of a quantum liquid whose excitations follow the Maxwell action.
- Chandrasekharan, "Confinement, Chiral Symmetry Breaking and Continuum Limits in Quantum Link Models", arXiv:hep-lat/9809084, Nucl. Phys. Proc. Suppl. 73 (1999) 739. Abstract: the 3+1 phase diagram "suggests" a Coulomb phase at large but finite `j`.
- Banerjee, Huffman, Rammelmüller, "Exploring Bosonic and Fermionic Link Models on (3+1)-d tubes", arXiv:2201.07171, Phys. Rev. Research 4, 033174 (2022). Abstract: exact diagonalization on tubes; a Coulomb phase is proposed.
- Wiese, "Ultracold Quantum Gases and Lattice Systems: Quantum Simulation of Lattice Gauge Theories", arXiv:1305.1602 (Annalen der Physik topical issue). Review of quantum link models.
- Chandrasekharan, Wiese, "Quantum link models: A discrete approach to gauge theories", arXiv:hep-lat/9609042, Nucl. Phys. B 492 (1997) 455. NOT VERIFIED (search result only).
- Arrighi, Di Molfetta, Eon, "Gauge-invariance in cellular automata", arXiv:2004.03656. Abstract: definitions of gauge invariance and a gauging procedure for cellular automata.
- Sellapillay, Arrighi, Di Molfetta, "A discrete relativistic spacetime formalism for 1+1-QED with continuum limits", arXiv:2103.13150. Abstract: an exactly `U(1)` gauge-invariant circuit in 1+1 dimensions.
- Bisio, D'Ariano, Perinotti, "Quantum Cellular Automaton Theory of Light", arXiv:1407.6928, Annals of Physics 368 (2016) 177. Abstract: free Maxwell equations from two Weyl automata; the photon is a pair of fermions. Not a gauge-register model.
- Gross, Nesme, Vogts, Werner, "Index theory of one dimensional quantum walks and cellular automata", arXiv:0910.3675, Commun. Math. Phys. 310 (2012) 419. NOT VERIFIED (search result only). Not used.

**Bounded search finding.** No fetched abstract gives an exact Floquet band of a fixed-register gauge-invariant circuit in three dimensions. This is a finding about the searched abstracts, not a theorem. The photon results above concern ground states of Hamiltonians and are numerical or perturbative. The construction below concerns an exact band in a chosen stationary state. It does not bear on those ground-state questions.

## 3. Setting: the five-mode gauge sector of L5-U

The law is `L5-U[m]` of `LW1_5.md` lines 94-100. A link `ℓ` carries `Λ^m C^{10}`: five rishon modes at each end, fermionic among themselves; different links are ordinary tensor factors. `p_{ℓ,z}` is the rishon number at the end of `ℓ` at site `z`; `p_{ℓ,x}+p_{ℓ,y}=m`. The local group `U(5)_z` acts on the matter at `z` and on the `z`-ends of the six links at `z`. The tick is `U_B=W_BW_EM_oM_e`; the layer `W_B` is free; `W_E=∏_ℓ e^{−iτ_E(p_{ℓ,x}−m/2)^2}`.

In this section and in sections 4.1-4.4, `m=2p` is even and `1≤p≤4`; section 4.5 treats odd `m`. Throughout, `V=C^5`.

**Sectors and end spaces.** A *sector* of a finite link set fixes every end number. In a sector, a link register is the tensor product of its two end spaces `Λ^{p_{ℓ,x}}V⊗Λ^{p_{ℓ,y}}V`, in a fixed mode order. Let `σ*` be the sector with every end number `p`.

**Cubes and corners.** By `GA1_5.md` Theorem 2.1 every link lies in exactly one cube of the even or odd tiling. Both ends of a cube link are corners of that cube. At a corner `w` of a cube `C`, the three links of `C` at `w` give three *`C`-ends*. For a sector `σ` of `C`, put
\[
E^C_w[σ]=\textstyle\bigotimes_{3\ C\text{-ends at }w}Λ^{p_e}V=\bigoplus_μ V_μ\otimes M^{C,w}_μ[σ],\qquad M^{C,w}_μ[σ]=\operatorname{Hom}_{U(5)}(V_μ,E^C_w[σ]),
\]
with `μ` running over the irreducible types of `U(5)`. Then `H_C[σ]=⊗_{w∈C}E^C_w[σ]` is the register of the twelve links of `C` in `σ`. The group `∏_{w∈C}U(5)_w`, acting on the `C`-ends, is the part of the gauge group that acts on `H_C`. A *type tuple* `μ⃗` assigns a type to each corner.

**The end permutation group.** On `(Λ^pV)^{⊗3}` let `T_π`, `π∈S_3`, permute the three factors, with the fermionic sign `(−1)^{p·p}` for each exchange of two adjacent factors. This is a unitary representation of `S_3`. It commutes with `U(5)`. So `S_3` acts on each `M_μ=Hom_{U(5)}(V_μ,(Λ^pV)^{⊗3})`. A colour-preserving bijection between the end modes of two corners in configuration `(p,p,p)` induces, on that sector, `±T_π` for one `π` (`GA1_5.md` Lemma S1′(d): "two such induced maps agree up to a sign").

**Site classes.** The class of a site `z` is `z mod 2∈{0,1}^3`. In the even cube with base `2b`, the corner `2b+c` has class `c`. The two ends of each body diagonal of a cube have complementary classes `c` and `(1,1,1)−c`. For an even cube `C` with base `2b`, let `P_C={2b,2b+(1,1,1)}`, the diagonal of classes `000` and `111`. The six other corners form a closed path of six links of `C`,
\[
\mathrm{hex}_C:\ 2b+(1,0,0)\to 2b+(1,1,0)\to 2b+(0,1,0)\to 2b+(0,1,1)\to 2b+(0,0,1)\to 2b+(1,0,1)\to 2b+(1,0,0),
\]
the hexagon around `P_C`. Each step changes one coordinate, so each step is a link of `C`. Each hexagon corner has two hexagon links and one link to a corner of `P_C`.

**Rotations of a cube.** By `GA1_5.md` Theorem 2.1 the stabilizer of `C` in `𝒢` is the proper rotation group `O` of `C`, of order 24. The stabilizer of the diagonal `P_C` is `D_3`: the rotations `r^{±1}` by `2π/3` about the diagonal and three half-turns about axes perpendicular to it. The half-turns exchange the two ends of the diagonal. The rotation `r` fixes both ends of `P_C`, cycles the three `C`-ends at each, and maps `hex_C` to itself with its orientation. A half-turn maps `hex_C` to itself with the opposite orientation.

**The neutral swap.** `W^{swap}=S_oS_e` is the layer of `GA1_5.md` Theorem 6.3: each gate exchanges the star multiplicity factors of an antipodal pair `{v,a(v)}` of a cube, on matched sectors and equal star types, through the point-reflection identification `ι`.

## 4. Results

### 4.1 One cube

**Lemma 4.1 (cube algebra and lifts).** Let `C` be a cube and `G_C=∏_{w∈C}U(5)_w` acting on `H_C=⊕_σH_C[σ]`.
1. `H_C=⊕_{μ⃗}V_{μ⃗}⊗M^C_{μ⃗}`, with `V_{μ⃗}=⊗_wV_{μ_w}` and `M^C_{μ⃗}=⊕_σ⊗_wM^{C,w}_{μ_w}[σ]`. An operator on `H_C` commutes with `G_C` if and only if it has the form `⊕_{μ⃗}1_{V_{μ⃗}}⊗x_{μ⃗}`, with `x_{μ⃗}` any operator on `M^C_{μ⃗}`. Every such operator, extended by the identity, commutes with every local gauge transformation.
2. For `R` in the stabilizer `O` of `C`, the lift of `R` restricts to an automorphism `Ad L_R` of `B(H_C)`, with `L_R` unitary. `R↦Ad L_R` is a group action. `L_R` maps `H_C[σ]` onto `H_C[Rσ]`. If `R` fixes a type tuple `μ⃗` (that is, `μ_{Rw}=μ_w`), then on `V_{μ⃗}⊗M^C_{μ⃗}` one has `L_R=Π_R⊗L^M_R`, where `Π_R` permutes the factors of `V_{μ⃗}` by `w↦Rw`.
3. If `R^n=1`, then `L_R^n` is a scalar `c`. Every eigenvalue of `L_R` is an `n`-th root of `c`, and so is every eigenvalue of `L^M_R` on any `L^M_R`-invariant subspace of `M^C_{μ⃗}`.

*Proof.* (1) In a sector, `E^C_w[σ]` decomposes into isotypic components; the tensor product over the eight corners gives the displayed sum. `G_C` acts by `⊗_wπ_{μ_w}` on `V_{μ⃗}` and trivially on `M^C_{μ⃗}`. The `V_{μ⃗}` are irreducible for `G_C` and pairwise inequivalent, since a type tuple fixes the irreducible representation of the product group. Schur's lemma gives the commutant. A gauge transformation at a site outside `C` does not act on `H_C`. At a corner `w`, `U(5)_w` acts on the `C`-ends and on factors outside `H_C`; an operator on `H_C` that commutes with the first part commutes with the whole.

(2) `LW1_5.md` line 261: "On each link send every rishon mode at its `z`-end to the same flavour at the `gz`-end of the image link. This is a permutation of ten rishon modes." `R` maps the links of `C` onto themselves. So the lift restricted to `B(H_C)` is the automorphism induced by a permutation of the 120 rishon modes of `C` together with the permutation of link factors. Such an automorphism is implemented by a unitary `L_R`, unique up to a phase. Composition of mode permutations is the permutation of the composite, so `Ad L_R Ad L_{R'}=Ad L_{RR'}`. Modes at `w` go to modes at `Rw`, so end numbers are transported and `L_RH_C[σ]=H_C[Rσ]`. If `R` fixes `μ⃗`, then `L_R` maps the `μ⃗`-isotypic component to itself and `L_Rγ(g)L_R^{-1}=γ(g∘R^{-1})` for `g∈G_C`. The operator `(Π_R^{-1}⊗1)L_R` then commutes with `G_C` on `V_{μ⃗}⊗M^C_{μ⃗}`; by (1) it is `1⊗L^M_R`.

(3) `Ad(L_R^n)=Ad L_{R^n}=id` on `B(H_C)`, so `L_R^n` commutes with every operator on `H_C` and is a scalar `c`. Then each eigenvalue `λ` of `L_R` satisfies `λ^n=c`. By (2), `(L^M_R)^n=c` on `M^C_{μ⃗}` because `Π_R^n=1`. □

**Lemma 4.2 (corner data).** Let `1≤p≤4` and `X_p=(Λ^pV)^{⊗3}` with the action `T` of `S_3`. For ends `a≠b` let `E_{ab}=∑_kf^†_{a,k}f_{b,k}` move one rishon of colour `k` from end `b` to end `a`. It commutes with `U(5)` and maps `X_p` into the configuration with `p+1` at `a` and `p−1` at `b`.
1. There is a type `μ_0` such that `M_{μ_0}=Hom_{U(5)}(V_{μ_0},X_p)` contains a two-dimensional `S_3`-invariant subspace `q` on which `S_3` acts by its irreducible two-dimensional representation. The three-cycle `T_{(123)}` has on `q` the two eigenvalues `ω,ω^2` (`ω=e^{2πi/3}`); a three-cycle is even, so `T_{(123)}` carries no fermionic sign.
2. There is a type `μ_1` and a line `L⊂M_{μ_1}` with `T_πL=L` for all `π`, such that `V_{μ_1}` occurs in `Λ^{p+1}V⊗Λ^{p−1}V⊗Λ^pV`, in every order of the three factors.
3. `L⊥q` when `μ_1=μ_0`.

*Proof.* (1) `dim Λ^pV=C(5,p)≥5`. Take two distinct basis vectors `y_1,y_2` of `Λ^pV`. The three vectors `T_π(y_1⊗y_1⊗y_2)` span a subspace on which `S_3` acts as the permutation representation on three points, up to the sign character. That representation contains the two-dimensional irreducible representation, and so does its product with the sign character. So the isotypic component `I` of `X_p` for the two-dimensional representation is nonzero. `T` commutes with `U(5)`, so `I` is a `U(5)`-subrepresentation. Take an irreducible summand `V_{μ_0}⊂I`. Then `Hom_{U(5)}(V_{μ_0},I)⊂M_{μ_0}` is a nonzero `S_3`-subrepresentation of isotypic type two-dimensional; take one irreducible copy `q` in it. On the two-dimensional representation of `S_3` a three-cycle has eigenvalues `ω,ω^2`.

(2) Pick colour sets `x_1,x_2,x_3` of size `p`: for `p≤3`, `x_i=Y∪\{i\}` with `Y` a set of `p−1` colours not in `\{1,2,3\}`; for `p=4`, `x_i=\{1,…,5\}∖\{i\}`. In both cases, for `i≠j` the set `x_j∖x_i` has exactly one element. Write `|x⟩` for the wedge monomial. For `ε=±1` put
\[
u_ε=\textstyle\sum_{π∈S_3}ε^{|π|}\,T_π\big(|x_1⟩⊗|x_2⟩⊗|x_3⟩\big),
\]
with `|π|` the number of transpositions. The six tensors `|x_{τ1}⟩⊗|x_{τ2}⟩⊗|x_{τ3}⟩` are distinct basis tensors, so `u_ε≠0`, and `T_πu_ε=±u_ε`. Apply `E_{12}` (ends 1, 2). On `|x_{τ1}⟩⊗|x_{τ2}⟩⊗|x_{τ3}⟩` it moves the one colour of `x_{τ2}∖x_{τ1}` and gives `±|x_{τ1}∪x_{τ2}⟩⊗|x_{τ1}∩x_{τ2}⟩⊗|x_{τ3}⟩`. This depends on `τ` only through the unordered pair `\{τ1,τ2\}` and through `τ3`. The two `τ` with the same `τ3` give the same basis tensor with signs `s,s'∈\{±1\}`; in `u_ε` it gets the coefficient `±(s+εs')`. For one of `ε=±1` this is nonzero. Fix that `ε`. Then `E_{12}u_ε≠0`.

Let `R_u` be the span of `U(5)u_ε`. It is a `U(5)`-subrepresentation, and `T_π` acts on it by the scalar `±1` with which it acts on `u_ε`. Since `E_{12}R_u≠0`, some irreducible summand `V'⊂R_u` has `E_{12}V'≠0`. Let `μ_1` be its type and `L=Hom_{U(5)}(V_{μ_1},V')`, a line in `M_{μ_1}` on which every `T_π` is a scalar. `E_{12}` restricted to `V'` is a nonzero intertwiner from an irreducible, so it is injective, and `V_{μ_1}` occurs in `Λ^{p+1}⊗Λ^{p−1}⊗Λ^p`. For another ordered pair `(a,b)`, `E_{ab}=±T_πE_{12}T_π^{-1}` for a permutation `π` with `π(1)=a,π(2)=b`, and `T_π^{-1}` is a scalar on `V'`. So `E_{ab}V'≠0`, and `V_{μ_1}` occurs in every order. A tensor product of representations is unchanged up to isomorphism by reordering its factors.

(3) `q` lies in the isotypic component of `M_{μ_0}` for the two-dimensional representation and `L` in that for a one-dimensional representation. Distinct isotypic components of a unitary representation are orthogonal. □

[check] `/tmp/toe-ga15phi2/check_corner.py` (exact integer arithmetic with explicit Fock signs, under one second, memory 56% free): for `p=1,2,3,4` the vector `u_ε` has six terms, and `E_{12}u_ε` has three nonzero terms for exactly one `ε` (`ε=+1` for odd `p`, `ε=−1` for even `p`) and vanishes for the other. This agrees with step (2). It guides; it does not prove.

### 4.2 The neutral band on a smaller support

**Choices.** Fix `μ_0,q` and `μ_1,L` as in Lemma 4.2. At the site `0` the stabilizer of `0` in `𝒢` is the order-three rotation about the body diagonal through `0` (`GA1_5.md` Theorem 2.1). Its lift cycles the three even ends at `0` and acts on `q_0⊂M^{0}_{μ_0}[σ*]` as `±T_{(123)}`. Let `e_+,e_-` be its unit eigenvectors in `q_0` (Lemma 4.2(1)), `Z_0=|e_+⟩⟨e_+|−|e_-⟩⟨e_-|` and `X_0=|e_+⟩⟨e_-|+|e_-⟩⟨e_+|`. The stabilizer maps `q_0` and `L_0` to themselves and commutes with `Z_0` (it acts on `e_±` by scalars). Transport `q_0,L_0,Z_0` to every site `z` by the lifts of `𝒢`: `q_z,L_z` lie in the multiplicity spaces of the three even ends at `z`, and `Z_z` is a well-defined operator. (𝒢 is site transitive and preserves the tilings.) Choose a type `λ_0` in `V_{μ_0}⊗V_{μ_0}` and a type `λ_1` in `V_{μ_1}⊗V_{μ_1}`.

**The state.** In `σ*` the ends at a site `z` form `E^e_z⊗E^o_z` (even triple, odd triple). Let `K_z` be the `λ`-isotypic part, for the diagonal `U(5)_z`, of
\[
(V_{μ}\otimes q_z)\otimes(V_{μ}\otimes M^{o,z}_{μ})\quad\text{if }z\text{ has class }000\text{ or }111\ (μ=μ_0,λ=λ_0),
\]
and of `(V_{μ_1}⊗L_z)⊗(V_{μ_1}⊗M^{o,z}_{μ_1})` otherwise (`λ=λ_1`). Let `ω` be empty matter times the product over sites of the normalized projections onto `K_z`, on the sector `σ*`.

**Lemma 4.3 (neutral band).** For `m=2p` even, every allowed `ε,μ,τ_E` and `U_B=W^{swap}W_EM_oM_e`:
1. `ω` is a locally gauge-invariant D1 state.
2. Let `A_0=1_{V_{μ_0}}⊗\widetilde X_0` on the `μ_0` component of the even ends at `0` in `σ*` (with `\widetilde X_0=X_0` on `q_0` and `0` on its complement in `M^0_{μ_0}`), the identity on the odd ends, and `0` on other types and sectors. Put `A_{2b}=τ_b(A_0)`, by the translation lift only. Then `A_{2b}` is gauge invariant and commutes with every end number, the vectors `u_b=π(A_{2b})Ω` are orthonormal, and `Ũu_b=u_{b−(1,1,1)}`.
3. `A_{2b}` acts only on the multiplicity factor `M^{2b}_{μ_0}` of the even ends at `2b`, and there `A_{2b}Z_{2b}=−Z_{2b}A_{2b}` on `q_{2b}`.

*Proof.* (1) Each `K_z` is invariant under `U(5)_z`, so each normalized projection is. Every end belongs to exactly one star, so the product is a state on the link algebra; with empty matter it is a state of the law's algebra, as in `GA1_5.md` line 145. It is invariant under local gauge transformations and so under each `Ad c_z`. Classes and the transported data are invariant under `2Z³`, so `ω` is even-translation invariant.

Stationarity. On `σ*`, `W_E` is the scalar `1`, since `(p−m/2)^2=0`. The matter gates act as the identity on empty matter (`GA1_5.md` Theorem 6.1, proof). A swap gate on a pair `\{v,a(v)\}` of one tiling acts on the star multiplicity factors of `v` and `a(v)` on matched sectors of equal type, through `ι`, and as the identity elsewhere (`GA1_5.md` line 141). The classes of `v` and `a(v)` are complementary, so both lie in `\{000,111\}` or both outside. So both stars have the same type, `λ_0` or `λ_1`, and the sector `σ*` is matched. The gate preserves `P_{K_v}⊗P_{K_{a(v)}}` if `ι(K_v)=K_{a(v)}`. Now `ι` is induced by a point reflection `P` through a cube centre. `P` lies in `2Z³⋊O_h` and preserves link parity. Choose `g∈𝒢` with `gv=a(v)`. Then `g^{-1}P` fixes `v` and permutes the even triple and the odd triple at `v`. By `GA1_5.md` Lemma S1′(d), the map it induces on the even ends is `±T_π` for some `π∈S_3`. `q_v` and `L_v` are `S_3`-invariant (Lemma 4.2), the full spaces `M^{o,v}_μ` are preserved, and colour-preserving maps keep types. So `ι(K_v)=L_g(K_v)=K_{a(v)}`, as subspaces. Each gate therefore fixes the product state, and so does each sublayer.

(2) `A_0` acts on a multiplicity factor and on one sector, so it commutes with `U(5)_0`, with every other gauge transformation and with every end number. `ω(A_{2b})=\tfrac12\operatorname{tr}_qX_0=0` and `ω(A^*_{2b}A_{2b})=\tfrac12\operatorname{tr}_q(X_0^*X_0)=1`. For `b≠b'` the product state gives `ω(A_{2b}^*A_{2b'})=\overline{ω(A_{2b})}ω(A_{2b'})=0`. The motion is `GA1_5.md` Theorem 6.3 with its §3.9 identification: on the support of the state, every pair has matched sectors and equal types, so conjugation by `S_o` and then `S_e` carries `A_{2b}` to the transport of `A_{2b}` through `ι_eι_o`. That composite is the translation by `−2(1,1,1)` up to a sign that conjugation removes. Theorem 6.1 then gives `Ũu_b=u_{b−(1,1,1)}`.

(3) By construction, and since `X_0` anticommutes with `Z_0` on `q_0` and both are transported by the same lift. □

### 4.3 The cube gate

Fix an even cube `C`, a diagonal `P=\{w_1,w_2\}` of `C`, and the rotation `r` about `P` and a half-turn `h` exchanging `w_1,w_2` (section 3). Let `μ⃗_P` put `μ_0` at `w_1,w_2` and `μ_1` at the six other corners. In `σ*` put, with `e_±(w)` the transported eigenvectors and `ℓ_P=⊗_{w∉P}L_w` (a line),
\[
v_{ss'}=e_s(w_1)\otimes e_{s'}(w_2)\otimes ℓ_P\in M^C_{μ⃗_P}[σ*],\qquad E_P=\operatorname{span}\{v_{++},v_{--}\},\quad X_P=\operatorname{span}\{v_{+-},v_{-+}\}.
\]
`E_P` and `X_P` are the even and odd parts for `Z_{w_1}Z_{w_2}`. Let `hex_P` be the hexagon of the six corners not in `P` and `σ_{P,±}=σ*±hex_P`: one rishon moved around `hex_P` in either sense. At each hexagon corner this changes the two hexagon ends from `(p,p)` to `(p+1,p−1)` or `(p−1,p+1)`; ends at `w_1,w_2` are unchanged. All end numbers stay in `[0,2p]`.

**Lemma 4.4 (cube gate).** There is a unitary `g_C` on `H_C` such that:
1. `g_C` commutes with `G_C` (so with every local gauge transformation), and `Ad L_R(g_C)=g_C` for every `R∈O`;
2. for each diagonal `P` of `C`, `g_C` fixes every vector of `V_{μ⃗_P}⊗E_P`;
3. `g_C` maps `V_{μ⃗_P}⊗X_P` onto a subspace `Ŷ_P` of `H_C[σ_{P,+}]⊕H_C[σ_{P,-}]`, and maps `Ŷ_P` onto `V_{μ⃗_P}⊗X_P`.

*Proof.* Step 1 (invariance of the data). `r` fixes `w_1,w_2` and is the stabilizer element of each in `𝒢`, so it preserves `q_{w_i}`, `Z_{w_i}` and maps each `L_w` to `L_{rw}`. `h` exchanges `w_1,w_2`; by the transport, `Ad L_h(Z_{w_1})=Z_{w_2}` and `Ad L_h(Z_{w_2})=Z_{w_1}`. Both fix `σ*` and `μ⃗_P`. So `E_P` and `X_P` are invariant under `L^M_r` and `L^M_h` (Lemma 4.1(2)). Each `v_{ss'}` spans a joint eigenline of `Z_{w_1},Z_{w_2}` in `q_{w_1}⊗q_{w_2}⊗ℓ_P`, so `L^M_rv_{ss'}=θ_{ss'}v_{ss'}`, and `L^M_hv_{ss'}` is a multiple of `v_{s's}`.

Step 2 (eigenvalues). On `σ*` the lift is induced by a mode permutation that sends the ends at each corner `w` to those at `rw`. So, up to one sign on the sector, `L^M_r` is the tensor product of the induced corner maps. Hence `θ_{ss'}=κa_sb_{s'}`, where `a_±` and `b_±` are the eigenvalues of the induced corner maps at `w_1` on `e_±(w_1)` and at `w_2` on `e_±(w_2)`; by Lemma 4.2(1) their ratio `ρ=a_+/a_-` is `ω` or `ω^2`. From `rh=hr^{-1}`, `Ad(L_rL_h)=Ad(L_hL_r^{-1})`, so `L_rL_h=cL_hL_r^{-1}` for a scalar `c`; on the block `μ⃗_P` the same holds for `L^M_r,L^M_h`, because `Π_rΠ_h=Π_hΠ_r^{-1}`. Apply both sides to `v_{s's}`: `θ_{ss'}θ_{s's}=c` for all `s,s'`. With `s=s'` and `s≠s'` this gives `a_+b_+=a_-b_-`, so `b_+/b_-=ρ^{-1}`. Therefore
\[
θ_{+-}/θ_{-+}=ρ^2\neq1 ,
\]
and `X_P` has two distinct eigenvalues of `L^M_r`.

Step 3 (target). In `σ_{P,+}` the corners `w_1,w_2` are unchanged. At each hexagon corner `μ_1` occurs (Lemma 4.2(2)). `r` maps `σ_{P,+}` to itself, so `N_+=⊗_{w∉P}M^{C,w}_{μ_1}[σ_{P,+}]` is a nonzero `L^M_r`-invariant space; let `φ` be a unit eigenvector in it. On `W_+=q_{w_1}⊗q_{w_2}⊗φ` the eigenvalues of `L^M_r` are, by the same tensor factorization, `κ'a_-b_-\{1,ρ,ρ^{-1},1\}`: all three cube roots of one number. By Lemma 4.1(3) (with `r^3=1`), every eigenvalue of `L^M_r` is a cube root of the same scalar. So both eigenvalues of `X_P` occur in `W_+`. Send each unit eigenvector of `X_P` to a unit eigenvector of `W_+` with the same eigenvalue. This is an isometry `f:X_P→W_+` with `L^M_rf=fL^M_r` on `X_P`.

Step 4 (one diagonal). Put `F=1_{V_{μ⃗_P}}⊗f`, extended by `0` on the complement of `V_{μ⃗_P}⊗X_P`. By Lemma 4.1(2) and Step 3, `Ad L_r(F)=F`. Put
\[
J_P=\tfrac1{\sqrt2}\big(F+\operatorname{Ad}L_h(F)\big).
\]
`F` maps into `H_C[σ_{P,+}]` and `Ad L_h(F)` into `H_C[hσ_{P,+}]=H_C[σ_{P,-}]`, since `h` reverses `hex_P`. The ranges are orthogonal, so the cross terms of `J_P^*J_P` vanish and `J_P^*J_P=\tfrac12(F^*F+\operatorname{Ad}L_h(F^*F))`. `F^*F` is the projection onto `V_{μ⃗_P}⊗X_P`, which `L_h` preserves (Step 1). So `J_P` is a partial isometry from `V_{μ⃗_P}⊗X_P` onto `Ŷ_P:=J_P(V_{μ⃗_P}⊗X_P)⊂H_C[σ_{P,+}]⊕H_C[σ_{P,-}]`. It commutes with `G_C`: `F` does by Lemma 4.1(1), and `L_h` maps `G_C` to itself. It is invariant under the stabilizer `D_3` of `P`: `Ad L_h(J_P)=J_P` since `h^2=1`, and `Ad L_r(\operatorname{Ad}L_hF)=\operatorname{Ad}L_h(\operatorname{Ad}L_{r^{-1}}F)=\operatorname{Ad}L_hF` since `rh=hr^{-1}`. `r` and `h` generate `D_3`.

Step 5 (all diagonals). `O` permutes the four diagonals transitively with stabilizer `D_3`. For `P'=RP` put `J_{P'}=\operatorname{Ad}L_R(J_P)`; this does not depend on the choice of `R`, by Step 4. The transport of `q,L,Z` (section 4.2) gives `L_R(V_{μ⃗_P}⊗X_P)=V_{μ⃗_{P'}}⊗X_{P'}` and `L_R(V_{μ⃗_P}⊗E_P)=V_{μ⃗_{P'}}⊗E_{P'}`, and `Ŷ_{P'}=L_RŶ_P` lies in the sectors `σ*±hex_{P'}`. The twelve spaces `V⊗E_{P'}`, `V⊗X_{P'}`, `Ŷ_{P'}` (four diagonals) are pairwise orthogonal. For one diagonal, `E_{P'}⊥X_{P'}` by parity. Otherwise: spaces in different sectors are orthogonal, and the eight sectors `σ*±hex_{P'}` are distinct from each other and from `σ*`; for `P'≠P''` and a corner `w∈P'∖P''`, the spaces for `P'` carry `q_w` (type `μ_0`) at `w` and those for `P''` carry `L_w` (type `μ_1`); these are orthogonal, by different types or, if `μ_0=μ_1`, by Lemma 4.2(3).

Step 6 (the gate). Let `Π` be the projection onto `⊕_{P'}(V⊗X_{P'}⊕Ŷ_{P'})` and put
\[
g_C=1-Π-i\textstyle\sum_{P'}\big(J_{P'}+J_{P'}^*\big).
\]
On each `V⊗X_{P'}⊕Ŷ_{P'}`, `(J+J^*)^2=J^*J+JJ^*` is the identity, so `−i(J+J^*)` is unitary there; `g_C` is the identity on the complement. So `g_C` is unitary. It commutes with `G_C`, and by Step 5 `Ad L_R(g_C)=g_C` for all `R∈O`. It fixes `V⊗E_{P'}`, which is orthogonal to the range of `Π`. It maps `V⊗X_{P'}` onto `Ŷ_{P'}` by `−iJ_{P'}` and `Ŷ_{P'}` back by `−iJ^*_{P'}`. □


### 4.4 The flux-carrying band

Let `G=∏_{C∈T_e}g_C`, with `g_C` of Lemma 4.4 at the base cube and `g_{C}` at every even cube defined by transport with the lifts of `𝒢`. Put
\[
W'_B=G\,W^{swap}W_E\,G^*\,W_E^{-1},\qquad U'_B=W'_BW_EM_oM_e=G\,W^{swap}W_E\,G^*M_oM_e .
\]
Let `ω'(A)=ω(G^*AG)` for local `A`, with `ω` of section 4.2, and `A'_{2b}=GA_{2b}G^*`.

**Theorem 4.5 (GA1-5-Φ for even `m`).** Let `m∈\{2,4,6,8\}` and let `ε,μ,τ_E` be any allowed constants of `L5-U[m]`.
1. `W'_B` belongs to GA1-P-5. Under NN-a it is admissible: it compiles into finitely many nearest-neighbour layers (`GA1_5.md` Proposition C(ii)), and its automorphism fixes every local gauge generator and commutes with every cell lift.
2. `ω'` is a locally gauge-invariant D1 state of `U'_B`, with empty matter.
3. The vectors `u'_b=π'(A'_{2b})Ω'` are orthonormal, lie in `H_phys`, and satisfy `Ũ'u'_b=u'_{b−(1,1,1)}`. The map `F(\sum_bφ̂_be^{iK·b})=\sum_bφ̂_bu'_b` is a band `(1,F,V)` with `V(K)=e^{-iK·(1,1,1)}`. `V(0)=1`, so `K_0=0` is a node; near it `h(K)=i\log V(K)=K·(1,1,1)`, so every `N_j=∂_jh(0)=1`. The band propagates.
4. The image of `F` is orthogonal to `closure π'(𝒩)Ω'`: the band is flux-carrying in the sense of R-Φ.
5. On every vector of the support of `ω'`, `A'_{2b}` changes the end numbers on the links of the cube `C_e(2b)` by the nonzero 1-cycle `hex_P` or `−hex_P` (`P=\{2b,2b+(1,1,1)\}`): it maps the part in `σ*` into `σ*±hex_P` and the part in `σ*±hex_P` into `σ*`.

*Proof.* (1) The gates `g_C`, `C∈T_e`, act on disjoint link sets, so they commute. Each is link-only and gauge invariant (Lemma 4.4(1)). The family is invariant under `𝒢`, which maps even cubes to even cubes; a lift carries `g_C` to `g_{gC}`, because `g_C` is invariant under the stabilizer `O` of `C`. So `G` and `G^*` are sublayers of GA1-P-5. So are `S_o`, `S_e` (`GA1_5.md` Theorem 6.3, Lemma S1′) and `W_E^{±1}`, whose gates `e^{∓iτ_E(p_{ℓ,x}−m/2)^2}` are single-link functions of end numbers. A product of finitely many sublayers is a member of GA1-P-5, so `W'_B` is. Proposition C(ii) compiles it. Each sublayer's automorphism fixes the local gauge generators and commutes with the cell lifts, and so does the composite with the base tick (`LW1_5.md` B1-U).

(2) `G` is gauge invariant and commutes with the translations of `2Z³`, so `ω'` inherits gauge invariance, even-translation invariance and empty matter from `ω` (Lemma 4.3(1)). Stationarity: on empty matter `M_oM_e` acts as the identity from both sides (`GA1_5.md` Theorem 6.1, proof), so `U'_B` acts there as `𝕍'=G𝕍G^*` with `𝕍=W^{swap}W_E`. On a finite region containing the supports, `ρ'=GρG^*`, and `𝕍'ρ'𝕍'^*=G𝕍ρ𝕍^*G^*=GρG^*=ρ'` because `𝕍ρ𝕍^*=ρ` (Lemma 4.3(1)).

(3) `ω'(A'^*_{2b}A'_{2b'})=ω(A^*_{2b}A_{2b'})=δ_{bb'}`, and `A'_{2b}` is gauge invariant. Theorem 6.1 for the new layer gives `Ũ'π'(A)Ω'=π'(𝕍'^*A𝕍')Ω'`, and `𝕍'^*A'_{2b}𝕍'=G(𝕍^*A_{2b}𝕍)G^*`. The map `π(B)Ω↦π'(GBG^*)Ω'` is isometric, because `ω'(GB^*G^*GB'G^*)=ω(B^*B')`. Lemma 4.3(2) gives `π(𝕍^*A_{2b}𝕍)Ω=π(A_{2b−2(1,1,1)})Ω`, hence `Ũ'u'_b=u'_{b−(1,1,1)}`. Translation `T_β` maps `u'_b` to `u'_{b+β}` because `G` commutes with even translations. The band statements are then those of `GA1_5.md` line 147.


(4) and (5). Fix `b`, the cube `C=C_e(2b)` and `P=\{2b,2b+(1,1,1)\}`. On `C` the support of `ω` has type tuple `μ⃗_P`: the corners `2b,2b+(1,1,1)` have classes `000,111` and carry `q`; the others carry `L`. Take a finite region `R` containing `C`, the stars of its corners and the supports of the operators involved. In section 4.2 each `K_z` is the product of the multiplicity subspace `q_z` or `L_z` of its even ends with a subspace of the rest (the isotypic projection acts on `V`-factors only). Each star projection is a product of operators on separate factors, and a partial trace keeps such a product form. So the density matrix of `ω` on `R` factors as
\[
ρ=ρ_{\rm rest}\otimes\tfrac14\big(P_{E_P}+P_{X_P}\big),
\]
where `P_{E_P}+P_{X_P}` is the projection onto `q_{w_1}⊗q_{w_2}⊗ℓ_P⊂M^C_{μ⃗_P}[σ*]` and `ρ_{\rm rest}` is a density on all other factors (the `V`-factors of `C` and everything outside `C`). The gates of the other even cubes act on links outside `C`; they act on the other factors and commute with `g_C` and with functions of the end numbers of `C`. By Lemma 4.4, `g_C=1⊗\tilde g` on `V_{μ⃗_P}⊗M^C_{μ⃗_P}`, fixing `E_P` and mapping `X_P` onto `\tilde Y_P` (with `Ŷ_P=V_{μ⃗_P}⊗\tilde Y_P`). Hence
\[
ρ'=GρG^*=ρ'_{\rm rest}\otimes\tfrac14\big(P_{E_P}+P_{\tilde Y_P}\big),
\]
with `ρ'_{\rm rest}` the image of `ρ_{\rm rest}` under the other cubes' gates. Let `Q^0` be the projection onto the sector `σ*` of the links of `C` and `Q^1` the projection onto `σ_{P,+}` or `σ_{P,-}` there. They are functions of end numbers. The first term lies in the range of `Q^0` and the second in that of `Q^1`. So `ρ'=Q^0ρ'Q^0+Q^1ρ'Q^1`, and `ρ'` commutes with `Q^0` and `Q^1`.

Next, `A'_{2b}=g_CA_{2b}g_C^*`: the other gates commute with `A_{2b}`, which acts only on the even ends at `2b` (Lemma 4.3(3)). On the support of `ρ'`: a vector in `(\text{other factors})⊗E_P` is fixed by `g_C^*`; `A_{2b}` flips `Z_{2b}` and acts as the identity on the other factors, so it maps the vector into `(\text{other factors})⊗X_P`; `g_C` maps that into `(\text{other factors})⊗\tilde Y_P`. A vector in `(\text{other factors})⊗\tilde Y_P` is mapped by `g_C^*` into `(\text{other factors})⊗X_P`, by `A_{2b}` into `(\text{other factors})⊗E_P`, and is then fixed by `g_C`. This proves (5), and
\[
A'_{2b}Q^κρ'=Q^{1-κ}A'_{2b}Q^κρ'\qquad(κ=0,1).
\]
Let `N∈𝒩` be local. It commutes with every end number, hence with `Q^0,Q^1`. Then, on `R`,
\[
ω'(N^*A'_{2b})=\textstyle\sum_κ\operatorname{tr}\big(N^*Q^{1-κ}A'_{2b}Q^κρ'\big)=\sum_κ\operatorname{tr}\big(ρ'Q^κN^*Q^{1-κ}A'_{2b}\big)=\sum_κ\operatorname{tr}\big(ρ'N^*Q^κQ^{1-κ}A'_{2b}\big)=0 .
\]
The second step uses cyclicity and `[ρ',Q^κ]=0`; the third uses `[N,Q^κ]=0`. So each `u'_b` is orthogonal to `π'(N)Ω'` for every `N∈𝒩`, hence to the closure of their span. The image of `F` is the closed span of the `u'_b`. □


### 4.5 Odd `m` from 3 to 7

For odd `m` let `p_±=(m±1)/2` and use the translation swap `W^{swap,T}` and the sector `σ^→` (`p_{tail}=p_+`, `p_{head}=p_-` on every link) of Proposition S-odd (`GA1_5.md` §3.6). For `m∈\{3,5,7\}`, `p_±∈\{1,…,4\}`.

**Theorem 4.6 (GA1-5-Φ for `m=3,5,7`).** For `m∈\{3,5,7\}` and all allowed `ε,μ,τ_E`, items 1-5 of Theorem 4.5 hold with `W^{swap,T}` in place of `W^{swap}`, `σ^→` in place of `σ*`, and a cube sublayer `G` built below.

*Proof.* Only the changes are listed; every other step is that of sections 4.2-4.4.

(a) *Corners in `σ^→`.* In the even cube with base `2b`, the corner `2b` has its three `C`-ends at tails, configuration `(p_+)^3`; the corner `2b+(1,1,1)` has `(p_-)^3`; the corners of classes `100,010,001` have one head and two tails; those of classes `011,101,110` have two heads and one tail. The stabilizer of `σ^→|_C` in `O` is the group `C_3` of rotations about the diagonal `P=\{2b,2b+(1,1,1)\}`; its orbit is the eight sectors `σ^s|_C` of `GA1_5.md` §3.6. A sector of the orbit is fixed by its corner charges: the corner with charge `3p_+` is its all-tails corner.

(b) *Corner data.* Lemma 4.2(1) for `p_+` and for `p_-` gives `μ_0^±,q^±`. Let `r` be the rotation about `P`; it is the stabilizer in `𝒢` of `2b` and of `2b+(1,1,1)`. Label the eigenvectors `e_±` of `r` on `q^+` at `0` with ratio `ρ=a_+/a_-`, and those on `q^-` at `(1,1,1)` so that the ratio is `ρ^{-1}`. This is a choice of labels. Transport `q^±,Z^±` to every corner of every even cube in every sector of the orbit by the lifts of `𝒢`; the stabilizer of a site in `𝒢` is the rotation about its diagonal, which commutes with `Z^±`. At a hexagon corner the two hexagon ends are both tails or both heads. Moving one rishon around `hex_P` changes them from `(p_+,p_+)` to `(p_+±1,p_+∓1)`, or from `(p_-,p_-)` to `(p_-±1,p_-∓1)`. For `m≥3` all end numbers stay in `[0,5]` and each link total stays `m`. On the source configuration `E_{ab}` (the two hexagon ends `a,b`) is nonzero, so, as in Lemma 4.2(2), some irreducible summand is not killed by `E_{ab}` and its type occurs in the moved configuration. Take such a type `μ_1` and any line `L` at the corner of class `100` (one head, two tails), and `μ_1'`, `L'` at the corner of class `011`; transport by `r` and by `2Z³`. (No stabilizer condition arises: the stabilizer of a hexagon corner in `𝒢` does not fix `σ^→|_C`.)

(c) *State.* Choose `λ_0` in `V_{μ_0^+}⊗V_{μ_0^-}`, and for each pair `\{c,(1,1,1)−c\}` of other classes a type in the product of the two even-end types of the pair. At a site of class `000` put `q^+` (type `μ_0^+`) on the even ends and the translate by `−(1,1,1)` of `q^-` on the odd ends; at class `111` put `q^-` on the even ends and the translate by `(1,1,1)` of `q^+` on the odd ends; at the other classes put the lines `L` (classes `100,010,001`) and `L'` (classes `011,101,110`) on the even ends and, on the odd ends, the translate of the even data of the complementary class by the partner's translation vector `a(v)−v`. The even and odd partners of a site give vectors that differ by an element of `2Z³`, and all data are `2Z³`-periodic, so this is consistent. Take the isotypic part for the chosen type and the normalized projection, as in section 4.2. The translation identifications `τ_{±(1,1,1)}` of `W^{swap,T}` map the even ends of a star to the odd ends of its partner (`GA1_5.md` §3.6, "Gate"), so `ι^T(K_v)=K_{a(v)}` by construction, with no `S_3` condition. `W_E` is the scalar `e^{-iτ_E/4}` on `σ^→`. The rest of Lemma 4.3 and Proposition S-odd give a D1 state and the neutral band `u_b`, `Ũu_b=u_{b−(1,1,1)}`.

(d) *Gate.* `X_P` and `E_P` are defined as in section 4.3 in `σ^→`. By the label choice, the eigenvalues of `L^M_r` on `X_P` are `κa_-b_-ρ` and `κa_-b_-ρ^{-1}`, which are distinct; on `q^+⊗q^-⊗φ` in `σ^→+hex_P` they are `κ'a_-b_-\{1,ρ,ρ^{-1},1\}`. So a `C_3`-equivariant isometry `f` exists as in Step 3. Put `J_0=1⊗f`, extended by `0`, and `J=∑_{R∈O/C_3}\operatorname{Ad}L_R(J_0)`. The eight source sectors `Rσ^→|_C` are distinct, and so are the eight target sectors `R(σ^→+hex_P)|_C`. A target is not a source: equal corner charges would force the same coset by (a), and then `R\,hex_P=0`. So `J` is a partial isometry, `O`-invariant, commuting with `G_C`. Define `g_C` from `J` as in Step 6. It fixes `V⊗E_P` and exchanges `V⊗X_P` with `JV⊗X_P⊂H_C[σ^→±hex_P]`.

(e) *Conclusion.* Steps (1)-(5) of Theorem 4.5 apply verbatim with `σ^→` for `σ*`. □


## 5. What the result says about R-Φ

**Proposition 5.1 (conjugation).** Let `W_B∈`GA1-P-5, let `ω` be an empty-matter D1 state of `U_B=W_BW_EM_oM_e`, and let `G` be a finite product of GA1-P-5 sublayers. Put `W'_B=GW_BW_EG^*W_E^{-1}` and `ω'=ω∘\operatorname{Ad}G^*`. Then `W'_B∈`GA1-P-5, `ω'` is an empty-matter D1 state of `U'_B=W'_BW_EM_oM_e`, and `Φ:π(A)Ω↦π'(GAG^*)Ω'` extends to a unitary `H→H'` that maps `H_phys` onto `H'_phys` and satisfies `ΦŨ=Ũ'Φ`, `ΦT_β=T'_βΦ`. So every band `(d,F,V)` of `ω` gives a band `(d,ΦF,V)` of `ω'` with the same fibre.

*Proof.* Steps (1)-(3) of Theorem 4.5 use nothing else about `G`. `Φ` is isometric on local vectors and its range contains every `π'(B)Ω'`, since `B=G(G^*BG)G^*`. `A` is gauge invariant if and only if `GAG^*` is. □

**R-Φ is not invariant under Φ.** The band of Lemma 4.3 has image inside `closure π(𝒩)Ω`, because its vectors are `π(A_{2b})Ω` with `A_{2b}∈𝒩`. Its image under `Φ` is the band of Theorem 4.5, which is orthogonal to `closure π'(𝒩)Ω'`. So R-Φ depends on the band and on the end-number grading in one frame. It is not a property of a layer and a state up to conjugation by admissible gauge-invariant layers.

**What the band of Theorem 4.5 is not.** It has `d=1` and the one-way fibre `e^{−iK·(1,1,1)}`. It has no Clifford cone and no pair of polarizations. It moves only along `−(1,1,1)`. It is the conjugate, by one cube sublayer, of the neutral swap band. The flux it carries is a hexagonal loop inside one cube, attached to a multiplicity flip at a corner. `GA1_5.md` line 180 says of the neutral band: "It demonstrates that the abstract physical-band criterion alone does not identify a gauge boson." Theorem 4.5 shows the same for the criterion with R-Φ added.

**No new reading is proposed.** A criterion that separates the bands of Lemma 4.3 and Theorem 4.5 would have to be invariant under `Φ`, or would have to fix the frame by a physical requirement. Either choice is the owner's. This file states the fact and proposes neither.


## 6. `m=1,9`, `L5-O` and the electric half

### 6.1 `m=1` and `m=9`

**Lemma 6.1 (the sector `σ^→` is frozen for `m=1,9`).** Let `m∈\{1,9\}` and let `P` be the projection onto `σ^→` on the links of a finite region. Every local link-only gauge-invariant operator `A` satisfies `AP=PAP`. Hence, in every empty-matter D1 state carried by `σ^→`, `H_phys=closure π(𝒩)Ω`, and no nonzero band in `H_phys` is flux-carrying in the sense of R-Φ. Conjugation by a GA1-P-5 sublayer keeps a state carried by `σ^→` carried by `σ^→`.

*Proof.* Write `A=∑_δA_δ`, where `A_δ` changes each tail number `p_{ℓ,tail}` by `δ_ℓ`. A link-only gauge-invariant operator commutes with `Q_z` and with `N_z`, hence with `∑_{ℓ∋z}p_{ℓ,z}`. Since `p_{ℓ,head}=m−p_{ℓ,tail}`, each `δ` with `A_δ≠0` satisfies `∑_{ℓ\,out\,of\,z}δ_ℓ=∑_{ℓ\,into\,z}δ_ℓ` at every site. In `σ^→`, `p_{ℓ,tail}` is at its maximum: `1` of `m=1`, and `5` of five modes for `m=9`. So `A_δP≠0` needs `δ_ℓ≤0` for all `ℓ`. Put `f=−δ≥0`. If `f≠0`, pick `ℓ_1=(z_0,z_1)` with `f_{ℓ_1}>0`. At `z_1` the outgoing sum of `f` equals the incoming sum, which is positive, so some `ℓ_2=(z_1,z_1+e_j)` has `f_{ℓ_2}>0`. Repeating gives an infinite path along increasing coordinates inside the finite support of `f`, a contradiction. So `AP=A_0P=PA_0P=PAP`. Now `PAP` is gauge invariant and commutes with every end number, so it lies in `𝒩`. With `ω(N_x)=0`, `GA1_5.md` Theorem 6.1 makes `H_phys` the closed span of the `π(A)Ω=π(PAP)Ω`, which lies in `closure π(𝒩)Ω`. A band orthogonal to that closure and inside `H_phys` is zero. A sublayer's gates are local link-only gauge-invariant unitaries, so on a finite region they map the range of `P` into itself. □

**Open by name: GA1-5-Φ[`m=1,9`].** Is there a GA1-P-5 member and a D1 state with a propagating R-Φ band on `L5-U[1]` or `L5-U[9]`? Three distinct attacks failed.
- A1 (Theorem 4.5's route). It needs a sector matched by the point-reflection swap and uniform under translations. For odd `m` none exists: `GA1_5.md` line 180, "For odd `m`, no cell-invariant *sharp uniform end-number sector* of this form exists". The failing step is the matched sector.
- A2 (Theorem 4.6's route). It starts from the S-odd state on `σ^→`. Lemma 6.1 shows that every conjugate of such a state has `H_phys=closure π(𝒩)Ω`. The failing step is the conversion: no gauge-invariant gate changes the flux of `σ^→`.
- A3 (a non-uniform matched sector). Take the `2Z³`-periodic sector, invariant under point reflection through `c_0`, that puts in each cube the rishons of the six links at the two corners of its `000`-`111` diagonal `P_C` at those corners, and the rishons of the six hexagon links cyclically around `hex_C`. It is matched for `W^{swap}`, and for `m=1` the diagonal corners carry `q` (`p=1`, type `(2,1)`). In a cube, the cycle condition of Lemma 6.1's proof at the two diagonal corners forces every feasible change to vanish on the diagonal links; so the only nonzero feasible change inside the cube is the one-way hexagon move. That move maps the sector onto its image under a half-turn, which is a source sector of any `O`-covariant gate. At the hexagon corners the configuration has the single type `V` with one-dimensional multiplicity. So the target space of Lemma 4.4, Step 3, equals the half-turn image of the source space, and the gate cannot fix one and exchange the other. The failing step is orthogonality of target and source.
For `m=9` the particle-hole map of each end (`Λ^kV↔Λ^{5−k}V`) carries all three statements over. These are failed constructions, not an impossibility proof. Gates on several cubes, or states with matter, are not covered.

### 6.2 `L5-O` (GA1-5-O)

Not reached. Proposition 5.1 needs a neutral band to conjugate, and none is known on `L5-O[S_+]`: `GA1_5.md` §7 lists three failed attacks on GA1-5-O. Theorem 4.5 does not bear on it.

### 6.3 The electric half of GA1(a)(4)

Not reached. The band of Theorem 4.5 is an exact one-way mode in one chosen stationary state. It carries no energy functional. An electric statement would first have to name its energy: a supplied layer generator, or the tick's conserved Floquet generator, which differ (`docs/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md` line 105, on `origin/main`: "`H_F-H_1-H_2=O(h^2)`"). It would also need states whose end-number distribution varies with the field: `GA1_5.md` Theorem 5.1 shows that on the coherent magnetic family "`ω_V(f(p_x,p_y))` is independent of `V`". The growing-register mechanism on main (section 1) does not transfer to the fixed register `C(10,m)`.


## FINISH

**Proved here (pass 1, not yet distilled or refereed), conditional on the law `L5-U[m]` of `LW1_5.md`, the class GA1-P-5, the owner's NN-a and the definitions of `GA1_5.md` §1.**
- Lemma 4.1: the gauge-invariant algebra of one cube and the factorization of the lifts on it.
- Lemma 4.2: corner data (a two-dimensional `S_3` multiplicity `q`, a type `μ_1` that survives a corner move) for `p=1,…,4`.
- Lemma 4.3: the neutral swap band on a smaller support with two corner qubits per cube (extends `GA1_5.md` Theorem 6.3).
- Lemma 4.4: an `O`-invariant gauge-invariant cube gate that fixes the even corner parity and writes the odd parity into a hexagonal flux loop.
- **Theorem 4.5 (`m=2,4,6,8`) and Theorem 4.6 (`m=3,5,7`): GA1-5-Φ holds.** For all allowed `ε,μ,τ_E` there are a member `W'_B` of GA1-P-5, admissible under NN-a, and a locally gauge-invariant empty-matter D1 state with a band in `H_phys` whose image is orthogonal to `closure π(𝒩)Ω'`. Its fibre is `V(K)=e^{−iK·(1,1,1)}`, with a node at `K=0` and every `N_j=1`. Its operator changes the end numbers by a hexagon cycle on every vector of the state's support.
- Proposition 5.1: conjugation by GA1-P-5 sublayers carries bands to bands with the same fibre; R-Φ is not invariant under it.
- Lemma 6.1: for `m=1,9` the sector `σ^→` is frozen: every empty-matter D1 state on it has `H_phys=closure π(𝒩)Ω`.

**Counterexamples.** None to a stated claim. Section 5 records that R-Φ, as proposed in `GA1_5.md` line 59, is met by a conjugate of a neutral band.

**Open by name.**
- GA1-5-Φ[`m=1,9`]: three failed attacks, A1-A3 of section 6.1 (no uniform matched sector; `σ^→` frozen, Lemma 6.1; target equals rotated source in the cyclic sector).
- GA1-5-O: not reached; needs a neutral band on `L5-O` first (`GA1_5.md` §7).
- The electric half of GA1(a)(4): not reached (section 6.3).
- A frame-independent notion of flux content (section 5): an owner question if wanted; nothing is proposed here.

**What changes downstream.**
- GA1-5: the item "GA1-5-Φ" of the open list can be answered for `m=2,…,8` once this file is refereed. The answer does not identify a gauge boson; it shows that R-Φ does not separate a flux-carrying mode from a conjugated neutral mode.
- LZ1: the band is a further propagating physical band with `N_j=1`. It lies in `ker(Ũ−1)^⊥`, since `V(K)≠1` off a null set. It is one-way, so it says nothing about a common Clifford cone.
- EW1, VC1: nothing changes. The state is a chosen stationary state, not the VC1 vacuum, and no massless photon is identified.
- GA2/Y2-W, ZM1_OBS: nothing changes; no energy, coupling or correlator comparison is made.
- No law, reading, class, vacuum or axiom is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
