lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# RCS-P16: covariant spinor-class sectors from straight strings, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of the TOE assembly item RCS-P16, under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

---

## H. Head: what this file is, sources read, working set used

**What this file is.** An author-side long draft. It grants no status and adopts no law, reading, specification or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means the argument is written out in full below and has not yet been distilled or refereed. No numerical check was run; nothing here is marked [check].

**Source revisions read.**

| Ref | Commit |
|---|---|
| branch `claude/toe-assembly` (this checkout) | `89723409b8265cb103db2ed318701bdf7d9a3da2` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `f5af11cd0102cfd0b51aef0911f600130bf5beb1` |

**Files read in this folder, by line.** `prior/RCSP16.md` (all). `RCS1.md` lines 1-229 (all: §0 status, §1 definitions, Theorems 1-8, Lemma 6, Corollary 9, R1-R4, §§5-8). `TOE_ASSEMBLY.md` lines 215-240 (§3.6 R-CS, §3.7 NN-a). `CG16B.md` lines 1-186 (all). `CG16B_REFEREE.md`, grep hits on RCS-P, Example S, R-16, band (lines 49-268). `CG16D.md` lines 1-159 (all). `CG16D_REFEREE.md` lines 210-260 (§§3-6). `CG16S_REFEREE.md` lines 85-150 (G3, RC-W, §4.2); `CG16S_RCW_CHECK.md` (all). `GA1_5.md` lines 1-30 and grep hits on Lemma U, Proposition C, Theorem 6.3, swap (lines 166-385). `LZ1.md` lines 1-70 (§0, §1 definitions, Theorems 2.1-2.2, Corollary 2.3). `LW1_5.md` lines 7, 126, 210-216 (tilings), 266-274 (B1-U lifts). `LW1.md` lines 30, 43 (free data, group `O`), 72 (base tick, E1 products), 118, 126. `LIT_QLM.md` lines 1-53 (quantum-link literature already verified in this folder).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and readings are read plainly. One reading question is recorded for the owner in §5.2; none is adopted.

**Working-set entries used, by name.** PS-1 through the owner's NN-a (`TOE_ASSEMBLY.md` §3.7, quoted in §3.3); D1 (`TOE_ASSEMBLY.md` §3.4) through `LZ1.md` §1 and `CG16B.md` Definition 5; R-CS^str with `χ_tot` over parity-sharp backgrounds, as the owner's named working candidate (`TOE_ASSEMBLY.md` §3.6), not adopted; R-16^str′ (`CG16B.md` §7), an owner candidate, not adopted. The law is the U(16)-rishon witness of `CG16B.md` Theorem 3.1. It is a frozen witness, not a working-set law.

**Results used, by name** (each rebuilt or quoted where used): `RCS1.md` Lemma 5.1, Theorem 5, Lemma 6, Corollary 9, R2; `CG16B.md` Theorem 3.1, Lemma NN-W, Proposition L, Example S, Theorem 6.2; `LZ1.md` §1 definitions; `LW1_5.md` B1-U; `LW1.md` E1; `CG16S_REFEREE.md` RC-W (only to state what it does not cover).

## 0. The question, quoted

`RCS1.md` §8 (frozen): "**RCS-P (open).** Does an update in LZ1's class, a locally gauge-invariant D1 state, and an axis `e` admit a covariant representation built from R-CS^str(e) sectors with a Clifford-node band? ... By Corollary 9, any example must have two non-disjoint sectors at distinct transverse positions, or a sector that is not quasi-equivalent to its tick transform."

`RCS1.md` §5, after Corollary 9: "In the representation constructed in Theorem 8(c), Theorem 5 with `q(x)=x_j/2` gives `N₁=N₂=N₃=0`; for other covariant representations built from these sectors the result does not rule out motion along the ray."

`CG16B_REFEREE.md` line 215: "Under R-16^str′ every `χ_tot`-odd string sector of an (F)-law with link-purity is spinor class (Proposition L(iii)). Whether one carries a band with a node and a nonzero leading generator is open; `RCS1.md` Corollary 9 constrains any example (Theorem 6.1)."

The lane brief fixes the target: decide whether some locally gauge-invariant D1 state and axis `e` admit a covariant representation built from straight-string sectors of spinor class (boundary-flux label, `χ_tot=−1`) with a band that has a node and a nonzero leading generator; work on the U(16)-rishon witness or on a D-reg law, with the update in LZ1's class and NN-a; if a band exists, say whether its node is a Clifford cone and whether RC-W forces a mirror partner.

**Which law.** This file works on the U(16)-rishon witness of `CG16B.md` Theorem 3.1, at `m=16`, at every pair of cube angles. D-reg is not used.

## 0.1 Outcome in one paragraph

**Decided: yes, by construction (Theorem A).** On the rishon witness at `m=16` and every pair of cube angles, there is an update in LZ1's class that meets NN-a, and a locally gauge-invariant D1 product state `ω'`, such that the covariant direct sum of the straight `+e_1` string sectors carries a band `V(K)=e^{iK_1}`. The band has nodes (the plane `K_1=0`) and leading generator `N=(−1,0,0)`; the sign of `N_1` and the place of the node plane are conventions, its existence and `N_1≠0` are not (§4.5). Every vector of the representation has `χ_tot=−1` and boundary label `−1`, so it is spinor class under R-16^str′ (Proposition L, rebuilt in §4.3). The string head moves along the ray, one cell per tick, and the string grows behind it. The update appends four layers to the base tick: the inverses of the two base cube layers, then two layers of cube gates built from projected hops at angle `π/8`. **The node is not a Clifford cone.** A one-dimensional band cannot have one in three dimensions (Lemma A.5). More: in `ω'` and in Example S's state, for every update in LZ1's class whose gates are matter-activated (Definition B), every band built from these ray sectors is flat in both transverse directions at each node (Proposition B, a port of `RCS1.md` Theorem 8(c) and Corollary 9). The failing step for a Clifford cone there is named: the far ray's transverse position is a conserved label that separates sectors. **RC-W forces no mirror partner here.** Its hypotheses fail (setting F has no links), and the band has no Weyl node to pair: its node set is a plane and its winding vanishes trivially (§4.6). **What this does not show.** The band is not a particle in the VC1 vacuum; the state is a frozen product state; the update cancels the base tick's own motion; and no Clifford node from straight-string spinor-class sectors is built. That last question is RCS1's RCS-P in its Clifford form; it stays open by name (FINISH).

## 1. Literature

**Searches run (WebSearch, 2026-11-07).** Fredenhagen–Marcu charged states and the dressed-dipole order parameter; Buchholz–Fredenhagen cone localization; toric-code cone-localized sectors (Naaijkens); Levin–Wen fermions at string ends; Senthil–Fisher fractionalization; Barata–Nill charged particles; Bagan–Lavelle–McMullan dressing; index theory of one-dimensional walks (Gross–Nesme–Vogts–Werner). Quantum-link and rishon literature is already verified in this folder (`LIT_QLM.md` §§1-5, Chandrasekharan–Wiese arXiv:hep-lat/9609042 and the rishon papers); it is credited, not re-fetched. No citation below is load-bearing. Every result used is proved in this file or in a frozen part of this folder.

| Work | Fetched | What it says, quoted | Use here |
|---|---|---|---|
| P. Naaijkens, *Localized endomorphisms in Kitaev's toric code on the plane*, Rev. Math. Phys. 23 (2011) 347, arXiv:1012.3857 | abstract page and ar5iv text | Lemma 3.6: "the state ω_k^x only depends on x, but not on the path γ"; its proof: "one can use the plaquette operators to deform one path into another, provided the endpoints are the same". Definition 4.1: ρ is transportable if "for any cone Λ̂ there is a unitary equivalent endomorphism ρ̂ localized in Λ̂". | Contrast. In the toric code the string is invisible, so rays at different positions give equivalent sectors. In §4 the string is sharp, so transverse rays are disjoint. This is the hypothesis of `RCS1.md` Corollary 9 that a Clifford example must break. |
| M. Levin, X.-G. Wen, *Fermions, strings, and gauge fields in lattice spin models*, Phys. Rev. B 67 (2003) 245316, arXiv:cond-mat/0302460 | abstract page and ar5iv text | Abstract: "We argue that fermions always come in pairs and their creation operator always has a string-like structure". §V: "It is important to note that the position of this string is completely unobservable." Eq. (4): statistics from hopping operators, `t_il t_ki t_ij = e^{iθ} t_ij t_ki t_il`. | Context for string-made odd sectors and for what a deconfined example needs (an unobservable string). Not used in a proof. |
| T. Senthil, M. P. A. Fisher, *Z_2 gauge theory of electron fractionalization in strongly correlated systems*, arXiv:cond-mat/9910224 (journal per arXiv DOI 10.1103/PhysRevB.62.7850) | abstract page | "Fractionalization is obtained if they are uncondensed" (they: vortex configurations of the `Z_2` gauge field). | Context only. |
| K. Gregor, D. A. Huse, R. Moessner, S. L. Sondhi, *Diagnosing deconfinement and topological order*, New J. Phys. 13 (2011) 025009, arXiv:1011.4187 | abstract page | "One operator version of this diagnostic turns out to be the Fredenhagen-Marcu order parameter". | Context: the string-limit construction of R-CS^str is of Fredenhagen–Marcu type. |
| J. C. A. Barata, F. Nill, *Electrically and magnetically charged states and particles in the 2+1-dimensional Z_N-Higgs gauge model*, Commun. Math. Phys. 171 (1995) 27, arXiv:hep-th/9410229 | abstract page | Electric states are built "following ideas of Fredenhagen and Marcu"; "The existence of electrically and of magnetically charged particles is also established." | Context: the model the R-CS^str construction follows (`RCS1.md` §5). |
| E. Bagan, M. Lavelle, D. McMullan, *Charges from dressed matter: construction*, Ann. Phys. 282 (2000) 471, arXiv:hep-ph/9909257 | abstract page | "We construct locally gauge invariant charged fields which do create in and out Fock states." | Context: Dirac-type dressing, the alternative R-CS^Dirac of `RCS1.md` §7. Not used. |
| D. Gross, V. Nesme, H. Vogts, R. F. Werner, *Index theory of one dimensional quantum walks and cellular automata*, Commun. Math. Phys. 310 (2012) 419, arXiv:0910.3675 | abstract page | "Systems with trivial index are precisely those which can be realized by partitioned unitaries"; "the prototypes of systems with non-trivial index are shifts". | Remark in §4.6 only: the band of Theorem A acts as a shift; the remark explains why no index obstruction applies. Not used in a proof. |
| K. Fredenhagen, M. Marcu, *Charged states in Z_2 gauge theories*, Commun. Math. Phys. 92 (1983) 81 | **NOT VERIFIED** (no arXiv version; only the bibliographic listing was reached) | — | Credit only, as the origin of straight-string limits. |
| D. Buchholz, K. Fredenhagen, *Locality and the structure of particle states*, Commun. Math. Phys. 84 (1982) 1 | **NOT VERIFIED** (no arXiv version; the Project Euclid PDF returned no text) | — | Credit only, for cone localization of charges. |

**What the literature supplies, and what it does not.** The toric-code and Levin–Wen examples move string-made excitations in all directions because the string is unobservable in the ground state. The construction below is the opposite case: the string is a sharp physical object, the sectors are separated by where the ray runs, and the motion is along the ray only. No verified source treats straight-string spinor-class sectors of a `Spin(10)` quantum-link law; the construction and its proofs are native.

## 2. Prior work used

`origin/main` was read at `f5af11cd0102cfd0b51aef0911f600130bf5beb1` (two notes, by line, below). Paths without a prefix are in this folder.

| Prior result | Path | How it is used |
|---|---|---|
| Straight strings `B_{r,b}`, string states, R-CS^str(e) | `RCS1.md` §5 | The sectors of Theorem A are exactly these, on the witness. |
| Lemma 5.1 and Theorem 5 (conserved label gives directional flatness) | `RCS1.md` §4 | Proposition B(d), through Corollary 9. |
| Lemma 6 (asymptotic separation) | `RCS1.md` §5 | Transverse disjointness, Lemma A.3(c). |
| Theorem 8(c) (tick acts on a string state by a local unitary) | `RCS1.md` §5 | Ported to the witness in Proposition B(b). |
| Corollary 9 | `RCS1.md` §5 | Proposition B(d). |
| R2 (`χ_tot`, invariance under quasi-equivalence and sums) | `RCS1.md` R2 | Lemma A.3(b). |
| Rishon witness, its covariance; Theorem 6.2 strings | `CG16B.md` §3, §6 | The law and the strings. |
| Lemma NN-W (exact compilation of cube gates whose generator is a sum of even gauge-invariant edge terms) | `CG16B.md` §3 | NN-a for the appended layers, Lemma A.2(c). Extended: the generator here has projected edge terms. |
| Proposition L (centre values kept, `χ_tot=−1`, boundary label) | `CG16B.md` §6 | Lemma A.3(b). |
| Example S (positive string norms over a full/empty background) | `CG16B.md` §6 | Lemma A.3(a); the state `ω'` changes Example S's links of directions 2 and 3. |
| Static-label obstruction, Lemma N | `CG16D.md` §3 | Comparison: the label there is a finite defect; here it is the far ray. |
| RC-W | `CG16S_REFEREE.md` §3.1 | §4.6: its hypotheses fail here. |
| Swap-layer bands and Proposition C | `GA1_5.md` §6, §8 | Comparison: exact transport by gauge-invariant swap layers, there neutral and along `(1,1,1)`, here odd and along the ray. |
| Neutral Clifford bands | `LZ1I.md` | Comparison only. |
| Lift of each hop to the signed image hop | `LW1_5.md` lines 268-274 (B1-U) | Cell covariance of the appended layers, Lemma A.2(b). |
| Local automorphisms of infinite gate products | `LW1.md` E1 (line 72, "Products at infinite volume mean the local automorphisms of E1") | All infinite layers. |
| Charge motion without a band | `origin/main:docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md` lines 268-270: "It does not identify a single eigenvalue, a sharp particle pole, or a nonzero curvature of the lowest band." | Contrast: Theorem A gives an exact band, in a different law and state. |
| Mobile bosonic toric-code charges | `origin/main:docs/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md` lines 46-49: "a single Z on qubit a moves a vertex charge by 2 e_a. The charges are bosons, those of the 3D toric code." | Contrast: unobservable strings, charges move in all directions. |

**Prior work the digest missed.** (1) `RCS1.md` §5, the sentence after Corollary 9, leaves "motion along the ray" open explicitly (quoted in §0); this is the gap Theorem A fills. (2) `LW1_5.md` lines 268-274 prove covariance hop by hop ("the Hermitian hop maps to the signed image hop in either case"), not only for the summed cube generator; Lemma A.2(b) needs the termwise form.

**Failed attempts on file, and what is new here.** RCS1's A1 (frozen backgrounds) looked for transverse motion and found transverse flatness; Theorem A uses a frozen background too, and the new step is motion along the ray by an appended layer that the frozen background does not block. A1's flatness conclusion is kept and ported (Proposition B). RCS1's A2 (Dirac clouds) and the CG16D-NLP attempt (D-reg transfer breaks matchings) are not repeated. RCS1's A3 (loop condensation) is not attempted: Theorem A needs no fluctuating loops.

## 3. Setting: the witness, the law, the sectors

### 3.1 The law, quoted

`CG16B.md` Definition 1: "Sites are `Z³`, each with five CAR modes, ten Majoranas `γ_a`, and parity `P=(-i)^5γ_1⋯γ_10`. The site Hilbert space is `H=H_+⊕H_-`, each summand of dimension 16." Definition 2: "define S′ by `u=S_+⊕1`". `CG16B.md` §2: "put `E_{αi}=|α⟩⟨i|` from `H_-` to `H_+`."

`CG16B.md` Theorem 3.1 (the rishon witness): "On each link take 16 fermionic rishon modes at each end, commuting with matter, restricted to total number `m`, `1≤m≤31`. Let the endpoint representation be the second quantization of `S_+`. Define
`h_{xy}=Σ_i(Σ_α E_{y,αi}r^y_α)(Σ_β r^{x†}_β E^†_{x,βi})+h.c.`, `H_C=3^{-1/2}Σ_{(x,y)⊂C}η_i(x)h_{xy}`.
Use the two cube tilings and sign lifts of `LW1_5.md` §2, and no electric layer."

Conventions used below. A link is `ℓ=(x,y)` with `y=x+e_i`; `x` is its **source end**, `y` its **target end** (Example S's words). `p_{ℓ,z}` is the number of rishons at the `z`-end. `h_ℓ=h_{xy}`. The first term of `h_ℓ` moves the `H_+` content from `x` to `y` and one rishon from the `y`-end to the `x`-end; its adjoint does the reverse. `𝒯_e`, `𝒯_o` are the even and odd cube tilings; a direction-1 link with base coordinate `x_1` lies in an even or odd cube according to the parity of `x_1` (`LW1_5.md` line 216). The base tick is `U_0=M_oM_e`, `M_T=∏_{C∈𝒯_T}e^{-ia_TH_C}`, with real angles `a_e,a_o` (sign conventions as in `LW1.md` line 72; nothing below depends on them). `α(A)=U^*AU` for an update `U` (`LZ1.md` §1).

Centre and parity. `z_x=Z_x(−1)`; in the witness `z_x=−P_x∏_{ℓ∋x}(−1)^{p_{ℓ,x}}` (`CG16B.md` Example S). (F) holds and every link is link-pure, with endpoint centre product `(−1)^m` (`CG16B.md` Theorem 3.1 proof). Matter parity of a finite set is `P_Λ=∏_{x∈Λ}P_x`.

### 3.2 The update class and NN-a, quoted

`LZ1.md` §1: "A **gauge-invariant update of the same form** appends finitely many layers. Each layer is a family of finite-support gates that is closed under the even translations and has finitely many gates per cell. The gates of a layer commute pairwise, and each gate commutes with every local gauge transformation (`LW1.md` E1)." For the witness the base tick is `M_oM_e`.

NN-a (`TOE_ASSEMBLY.md` §3.7, owner 2026-11-06): "A nearest-neighbour gate `g` is a unitary supported within `F_x`, `F_y` and `H_ℓ`, where `ℓ=(x,y)` and `y=x+e_i`. ... Evenness means `[g,P_xP_y]=0` ... The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s`, for `s∈𝒢=2Z³⋊O_{c₀}`. ... Gauge invariance and cell covariance are required of the complete update only." As in `CG16B.md` Lemma NN-W, NN-a is read with the witness register in place of the chosen link register.

### 3.3 States, sectors, bands

D1, bands, nodes and `N_j` are those of `LZ1.md` §1 and `CG16B.md` Definitions 5-6. A covariant representation `(H,π,T,Ũ)` is `RCS1.md` Definition 5. Straight strings along `+e_1` from `x` are `CG16B.md` Theorem 6.2's
`B_{r,b}(x)=Σ_a E_{x,ai_0}(T_1⋯T_{2r})_{ab}`, `T_i=(r^{ℓ_i,y_{i−1}}_a r^{ℓ_i,y_i†}_b)_{ab}`, `y_i=x+ie_1`, `ℓ_i=(y_{i−1},y_i)`,
and the string states are `ω_r^{(x)}(A)=Σ_bω(B^*_{r,b}AB_{r,b})/Σ_bω(B^*_{r,b}B_{r,b})` on `𝔄^G` (`RCS1.md` §5). `χ_tot` is `RCS1.md` R2. The boundary label of a representation `π` over a background with `φ_Λ=ω(F_{∂Λ})∈{±1}` is the strong limit of `φ_Λπ(F_{∂Λ})` along finite `Λ` (`CG16B.md` Proposition L(iii)); under R-16^str′, spinor class means that the limit is `−1`.

**Definition B (matter-activated gate; new here, four-tested in §5).** A gate `g` whose support has site set `S` is *matter-activated* if `gΠ^-_S=Π^-_S`, where `Π^-_S=∏_{x∈S}(1−P_x)/2`; that is, `g` fixes every vector on which `P_x=−1` at every site of its support. An update is matter-activated if every gate of every layer is.

## 4. Results

Throughout §4 the law is the rishon witness with `m=16` and arbitrary real cube angles `a_e,a_o`.

### 4.1 The background state `ω'`

**The pairing vector.** Let `V=Λ^8(C^16)` and let `W:V⊗V→Λ^16(C^16)≅C` be the wedge map `u⊗v↦u∧v`. For every `g∈U(16)`, `W(Λ^8g⊗Λ^8g)=det(g)W`. Put `σ=W^*(1)/‖W^*(1)‖` (`W≠0`, so `W^*(1)≠0`). If `det g=1` and `g` is unitary, then `W(Λ^8g⊗Λ^8g)=W`; taking adjoints, `(Λ^8g⊗Λ^8g)^*W^*=W^*`, so `(Λ^8g⊗Λ^8g)σ=σ`.

**Definition of `ω'`.** Let `Φ'` be the product vector, as in `CG16B.md` Example S, with these factors. Matter is `|i_0⟩∈H_-` at every site. Every direction-1 link has all 16 rishons at its source end and none at its target end. Every link of direction 2 or 3 has end numbers `(8,8)`. At each site `y` and for `j=2,3`, the two `j`-ends at `y` (the `y`-ends of `(y−e_j,y)` and `(y,y+e_j)`) are in the vector `σ`. Let `ω'` be its vector state, and also its restriction to `𝔄^G`.

The `(8,8)` sector of one link is `Λ^8⊗Λ^8`, one factor per end, after a fixed ordering of the modes (source end first). The endpoint action at `y` is the second quantization of `S_+` on the `y`-end modes; it preserves their number, so it is even in those modes and acts on that sector as `Λ^8S_+(g)` on the `y`-end factor and as the identity on the other. Link registers of different links are ordinary tensor factors. So `Φ'` is a product over sites of vectors in the star spaces (matter at `y` and the six ends at `y`).

**Lemma A.1.** (a) `ω'` is locally gauge invariant and invariant under all translations. (b) `P_x=−1` and `z_x=+1` sharply at every site; so `ω'(P_Λ)=(−1)^{|Λ|}` and `ω'` is parity-sharp and sharp in every `z_x`. (c) Every matter-activated gate fixes `Φ'`. Hence `ω'` is stationary for every matter-activated update, and is a D1 state for it.

*Proof.* (a) `Z_y(g)=u_y(g)⊗∏_{ℓ∋y}ρ_{ℓ,y}(g)` acts on the star of `y` only. `u_y(g)=S_+(g)⊕1` fixes `|i_0⟩∈H_-`. A full end changes by `det S_+(g)=1` (`CG16B.md` Example S: "`tr(Π_+M^{ab})=0`"), and an empty end is fixed. The two `σ` factors are fixed by the paragraph above, since `S_+(g)` is unitary with determinant 1. Every translation maps each local factor to the same factor at the image site and preserves link directions and source ends.
(b) `P_x=−1` on `H_-`. The end numbers at `x` are `0,16,8,8,8,8`, all even, so `z_x=−P_x∏(−1)^{p_{ℓ,x}}=+1`. Products of commuting sharp involutions are sharp.
(c) At every site `P_x=−1`, so Definition B gives `gΦ'=Φ'` on the support's factor, hence on `Φ'`. For local `A`, `α(A)=Y^*AY` with `Y` a finite ordered product of gates (`LW1.md` E1); each fixes `Φ'`, so `ω'(α(A))=ω'(A)`. Gauge invariance implies invariance under every `Ad z_x`. □

**Lemma A.1′ (the base layers are matter-activated).** Every cube gate `e^{∓ia_TH_C}` of the base tick, and its inverse, is matter-activated.

*Proof.* Each summand of `h_ℓ` contains `E^†_{x,βi}=|i⟩⟨β|` or `E^†_{y,αi}`, which annihilate `H_-`. So `H_Cv=0` when every site of `C` has `P=−1`, and `e^{−itH_C}v=v` for every real `t`. □

### 4.2 The update

**Definition (projected hop and transport gate).** For a link `ℓ` let `Q_ℓ` be the projector of `H_ℓ` onto end numbers `(p_{ℓ,x},p_{ℓ,y})∈{(16,0),(15,1),(1,15),(0,16)}`. For a cube `C` put
\[
X_C=\sum_{\ell=(x,y)\subset C}\eta_i(x)\,Q_\ell h_\ell Q_\ell,\qquad t_C=e^{-i(\pi/8)X_C},\qquad S_T=\prod_{C\in\mathcal T_T}t_C .
\]
The update is the base tick followed by four appended layers, in this order: `M_o^{−1}`, `M_e^{−1}`, `S_o`, `S_e`. So
\[
U=S_eS_o\,M_e^{-1}M_o^{-1}\,M_oM_e=S_eS_o .
\]

**Lemma A.2.** (a) Each `t_C` is an even, gauge-invariant, matter-activated unitary supported on the matter of the eight sites of `C` and the twelve links of `C`. Gates of one tiling have disjoint supports. Each of `M_o^{−1}`, `M_e^{−1}`, `S_o`, `S_e` is a layer in LZ1's sense, so `U` is a gauge-invariant update of the same form. (b) Every cell lift `α_g`, `g∈𝒢`, maps `X_C` to `X_{gC}`; so `α_g` fixes each layer and commutes with the automorphism of `U`. (c) `U` meets NN-a read with the witness register. (d) `U` is matter-activated, so `ω'` is a D1 state for it.

*Proof.* (a) `p_{ℓ,x}+p_{ℓ,y}=16`, so `Q_ℓ` is a function of `p_{ℓ,x}`. The endpoint actions preserve end numbers, so `Q_ℓ` commutes with every `Z_z(g)`. `h_ℓ` is gauge invariant (`CG16B.md` Theorem 3.1) and even. So each term `η Q_ℓh_ℓQ_ℓ` is Hermitian, even and gauge invariant, and so are `X_C` and `t_C`. `Q_ℓ` acts on links only, so `Q_ℓv` has the same matter as `v`; by the proof of Lemma A.1′, `h_ℓQ_ℓv=0` when both ends of `ℓ` have `P=−1`. So `X_Cv=0` and `t_Cv=v` when every site of `C` has `P=−1`. Cubes of one tiling have disjoint sites and links, so their gates commute. Even translations preserve the tilings and the signs `η` (`LZ1.md` §1: "The even translations preserve the tilings and the parity-dependent signs"), so each family is closed under them; each has one gate per cell. The inverse layers have the same properties as the base layers.
(b) `LW1_5.md` line 268: the lift sends "`c_{x,j}↦d_g(gx)c_{gx,j}`" and "every rishon mode at its `z`-end to the same flavour at the `gz`-end of the image link". Line 274: "the Hermitian hop maps to the signed image hop in either case. The LW1 sign identity maps each `H_C` to `H_{gC}`". For the witness, `CG16B.md` Theorem 3.1's proof: "the signed site relabelling sends `E_{x,αi}` to `d_g(gx)E_{gx,αi}`; rishon modes are permuted, and a reversed link exchanges the displayed term and its adjoint." The sign identity (`LW1_5.md` line 268, from LW1 A2) is stated per edge: the signs "convert each transformed edge sign into the sign of the image edge, including reversed edges". So `α_g(η_i(x)h_ℓ)=η_{i'}(x')h_{gℓ}` for each edge, with `(x',x'+e_{i'})` the positively oriented image. The lift sends end numbers to the end numbers of the image ends, and the set defining `Q_ℓ` is symmetric under exchanging the two ends, so `α_g(Q_ℓ)=Q_{gℓ}`. Summing over the edges of `C` gives `α_g(X_C)=X_{gC}`. The group preserves each tiling (`LW1_5.md` line 274), so `α_g` permutes the gates of `S_T`; on each local observable only finitely many gates act (`LW1.md` E1), so `α_g` fixes the automorphism of `S_T`. The base layers and their inverses are covariant by `CG16B.md` Theorem 3.1. Hence `α_g` commutes with the automorphism of `U`.
(c) `CG16B.md` Lemma NN-W(a) proves, for a cube generator that is a sum of twelve terms, each an even gauge-invariant element of one edge-triple algebra, that the cube gate is "an exact finite product of unitaries" `e^{−it h}` of those terms; its proof (the analytic-subgroup and inverse-function argument, rebuilt there from `LW1.md` lines 198-205) uses only these properties of the terms and the finite dimension of the cube's space. The twelve terms `η Q_ℓh_ℓQ_ℓ` of `X_C` have them: each acts within `F_x`, `F_y`, `H_ℓ`. So each `t_C` is an exact finite word of even, gauge-invariant edge-triple gates. NN-W(b) schedules the words of one tiling in parallel on disjoint edge triples. The same holds for `M_T^{−1}` by NN-W itself. So `U` is a composition of finitely many NN-a layers, independent of volume. Every letter commutes with every local gauge transformation, so the complete update fixes every local gauge generator (differentiate `e^{it𝒢_x}` at `t=0`, as in NN-W(b)). With (b), all NN-a conditions hold.
(d) Every gate of `M_T^{−1}` is matter-activated by Lemma A.1′, and every `t_C` by (a). Lemma A.1(c) applies. □

**Remark (the base tick is cancelled).** `U=S_eS_o` as an automorphism: the first two appended layers undo the base tick. LZ1's class allows this, because the inverse of a base layer is itself a layer with every property the class asks. The conjugate update `U^♮=M_e^{−1}M_o^{−1}S_eS_oM_oM_e` (appended layers `S_o,S_e,M_o^{−1},M_e^{−1}`) is also in the class and keeps the base tick as its first step; it is not used below. Neither form keeps the base tick's own motion of the string head. Whether LZ1's class should exclude such layers is an owner question; §5.2 four-tests the restriction and finds that it fails test 2.

### 4.3 The straight-string sectors over `ω'`

Fix `x∈Z³` and write `y_k=x+ke_1`, `ℓ_k=(y_{k−1},y_k)`. Every link a string touches has direction 1, so the strings meet only links that are as in Example S.

**Lemma A.3.** (a) For every `r≥1`, `Σ_b‖B_{r,b}(x)Φ'‖^2=16^{2r+1}`. For every local `A`, `ω_r^{(x)}(A)` is constant in `r` once `y_{2r}` is outside the sites of `A`'s support; so `ω_x:=lim_rω_r^{(x)}` exists on `𝔄^G`. Its GNS triple is `(H_x,π_x,Ω_x)`.
(b) `π_x(z_y)=1` for every `y`; `χ_tot(π_x:ω')=−1`; and the boundary label of `π_x` is `−1`. The same holds for every representation quasi-equivalent to `π_x` and for direct sums of such.
(c) For each `t≥1`, `π_x(p_{ℓ_t,y_t})Ω_x=Ω_x`. If `(x'_2,x'_3)≠(x_2,x_3)`, then `π_{x'}(p_{ℓ_t,y_t})Ω_{x'}=0` for every `t`, and `π_x`, `π_{x'}` are disjoint.

*Proof.* (a) `(T_1⋯T_{2r})_{ab}=Σ_{a_1,…,a_{2r−1}}∏_kr^{ℓ_k,y_{k−1}}_{a_{k−1}}r^{ℓ_k,y_k†}_{a_k}` with `a_0=a`, `a_{2r}=b`. On `Φ'`, `r^{ℓ_k,y_{k−1}}_c` removes flavour `c` from a full source end and `r^{ℓ_k,y_k†}_d` adds `d` to an empty target end; each link is touched by one factor pair; `E_{x,ai_0}|i_0⟩=|a⟩`. So each index sequence gives a unit vector, and distinct sequences give distinct occupation patterns, hence orthogonal vectors. There are `16^{2r+1}` sequences. For a local `A` whose support lies in sites `y` with `y_1<x_1+k`, `k<2r`, sum over the unseen tail as in `RCS1.md` Theorem 8(b): tail patterns are orthogonal, `A` does not act on them, and every value of the boundary index has `16^{2r−k}` continuations. So the normalized expectation is the same for all `r` with `2r>k`. Local elements are dense and the states are bounded by one, so the limit is a state on `𝔄^G`.
(b) This is `CG16B.md` Proposition L(i)-(iii) with `ω=ω'`; its hypotheses hold: (F) and link-purity (§3.1), `ω'(z_y)=1` and `ω'(P_Λ)=(−1)^{|Λ|}` (Lemma A.1(b)), and each `B_{r,b}` commutes with `z_y` for `y≠y_{2r}` and is matter-odd with its matter at `x` (`CG16B.md` Theorem 6.2). Rebuilt in short: for fixed `y` and large `r`, `B^*z_yB=B^*Bz_y`, and Cauchy–Schwarz with `ω'((z_y−1)^2)=0` gives `ω_r(z_y)=1`; centrality of `z_y` in `𝔄^G` spreads the eigenvalue from `Ω_x` to `H_x`. For `x∈Λ`, `P_ΛB=−BP_Λ`, so `ω_r(P_Λ)=−(−1)^{|Λ|}`; every local `A∈𝔄^G` is even (`CG16B.md` Theorem 4.1(b)), so `(−1)^{|Λ|}π_x(P_Λ)=−1` on a dense set, hence strongly. The identity `∏_{y∈Λ}z_y=ε^{|Λ|}s_ΛP_ΛF_{∂Λ}` (`CG16B.md` Theorem 6.1) evaluated in `ω'` and in `π_x` gives `φ_Λπ_x(F_{∂Λ})=(−1)^{|Λ|}π_x(P_Λ)→−1`. Quasi-equivalence and sums: `RCS1.md` R2(a) for `χ_tot`; the same proof (uniformly bounded nets, Zorn decomposition) for the boundary label and for the scalar `π(z_y)`.
(c) In each term of `B_{r,b}(x)Φ'` the target end of `ℓ_t`, `t≤2r`, holds exactly one rishon, so `ω_x((p_{ℓ_t,y_t}−1)^2)=0` and `Ω_x` is an eigenvector with value 1. In `ω_{x'}` the link `ℓ_t` lies on a different line from every string link, so it is in its background state `(16,0)` and `p_{ℓ_t,y_t}=0` sharply. `p_{ℓ_t,y_t}` is gauge invariant, self-adjoint, bounded by 16, and its support escapes every finite set as `t→∞`. `RCS1.md` Lemma 6 gives disjointness. □

### 4.4 How an update acts on a string state

**Lemma A.4 (local action; port of `RCS1.md` Theorem 8(c)).** Let `𝒱` be a matter-activated update in LZ1's class, presented as layers `L_1,…,L_k` applied in this order, with automorphism `α_𝒱`. For each `x` there is a unitary `G_x∈𝔄^G`, a finite ordered product of gates of `𝒱`, such that `ω_x(α_𝒱(A))=ω_x(G_x^*AG_x)` for every local `A`. Hence `π_x∘α_𝒱` is unitarily equivalent to `π_x`.

*Proof.* Put `R_0={x}`. For `j≥1` let `g_j` be the product of the gates of `L_j` that meet `R_{j−1}` (finitely many: finite supports, finitely many gates per cell; they commute), and let `R_j` be `R_{j−1}` together with their sites. Put `G_x=g_k⋯g_1`; it is a finite product of gauge-invariant unitaries, so `G_x∈𝔄^G`.
Let `ψ=B_{r,b}(x)Φ'`. Every site other than `x` has `P=−1` in `ψ` (the far end `y_{2r}` changes only a link end). Fix local `A`; `α_𝒱(A)=Y^*AY`, where `Y=Y_k⋯Y_1` is the finite ordered product of the gates of `𝒱` in the backward light cone of `A` (`LW1.md` E1), `Y_j` from layer `j`. Induction on `j`: `Y_j⋯Y_1ψ` lies in the range of the projector `∏_{y∉R_j}(1−P_y)/2` and equals `g^A_j⋯g^A_1ψ`, where `g^A_j` is the product of the gates of `Y_j` that meet `R_{j−1}`. Indeed a gate of `Y_j` that misses `R_{j−1}` acts on a support where every site has `P=−1` on that range, so it acts as the identity there (Definition B, tensored with the identity elsewhere); a gate that meets `R_{j−1}` acts within the sites of `R_j`. So `⟨ψ,α_𝒱(A)ψ⟩=⟨g^Aψ,Ag^Aψ⟩` with `g^A=g^A_k⋯g^A_1`.
Let `h` be the set of gates of `G_x` in the backward light cone of `A` computed within `G_x`. The gates of `G_x` outside `h` cancel in `G_x^*AG_x`, so `G_x^*AG_x=h^*Ah` (ordered product). Each gate of `h` lies in the cone of `A` within `𝒱` (cones grow with the circuit) and meets the relevant `R_{j−1}`, so it lies in `g^A`; and the chains that put it in the cone use gates of `G_x`, which lie in `g^A`. So `h` is also the cone of `A` within `g^A`, and `(g^A)^*Ag^A=h^*Ah=G_x^*AG_x`.
Summing over `b` and normalizing, `ω_r^{(x)}(α_𝒱(A))=ω_r^{(x)}(G_x^*AG_x)` for all large `r`; let `r→∞` (Lemma A.3(a); both arguments are local). The last claim: `π_x(G_x)Ω_x` is a cyclic unit vector for `π_x` (`G_x` is unitary in `𝔄^G`), and its vector state is `ω_x∘α_𝒱`, whose GNS representation is `π_x∘α_𝒱`; uniqueness of GNS gives the equivalence. □

**Lemma A.4′ (one swap).** Let `ℓ=(w,v)` be a direction-1 link and let `ψ_v` be a string vector `B(v)Φ'` whose string starts at `v` and runs along `+e_1` (any length, any far index). Let `ψ'_w` be the string vector from `w` with one more link (`ℓ` first), the same later links and far index. Then `h_ℓψ_v=ψ'_w` and `h_ℓψ'_w=16ψ_v`. With `ψ̂=ψ/‖ψ‖` and `‖ψ'_w‖=4‖ψ_v‖`: `h_ℓψ̂_v=4ψ̂'_w`, `h_ℓψ̂'_w=4ψ̂_v`.

*Proof.* Write `ψ_v=Σ_aE_{v,ai_0}r^{ℓ',v}_a R_aΦ'`, `ℓ'=(v,v+e_1)`, `R_a` the later link operators, and `ψ'_w=Σ_{β,a}E_{w,βi_0}r^{ℓ,w}_βr^{ℓ,v†}_a r^{ℓ',v}_aR_aΦ'`. The first term of `h_ℓ` contains `E^†_{w,βi}`, which kills `|i_0⟩_w`; so only the adjoint term `K=Σ_{i,β,α}E_{w,βi}r^w_βr^{v†}_αE^†_{v,αi}` acts on `ψ_v`. On matter, `E^†_{v,αi}E_{v,ai_0}=δ_{αa}|i⟩⟨i_0|_v`, and then `E_{w,βi}|i_0⟩_w=δ_{ii_0}|β⟩_w`, so only `i=i_0` survives and `v` returns to `|i_0⟩`. Link operators commute with matter, so `Kψ_v=Σ_{β,a}E_{w,βi_0}r^{ℓ,w}_βr^{ℓ,v†}_ar^{ℓ',v}_aR_aΦ'=ψ'_w`, with the same operator order as in `ψ'_w`. On `ψ'_w` only the first term acts (the adjoint term needs `H_+` at `v`). Its matter part returns `w` to `|i_0⟩` and puts `|a⟩` at `v`. Its link part is `r^v_αr^{w†}_βr^{ℓ,w}_βr^{ℓ,v†}_a`: `r^{w†}_βr^w_β` is the number of flavour `β` at the full end, equal to 1, and `r^v_αr^{v†}_a=δ_{αa}` on the empty end. The sum over `β` gives 16. So `h_ℓψ'_w=16ψ_v`. The norms are `16^{n}` and `16^{n+1}` for strings of `n` and `n+1` contracted indices (Lemma A.3(a)). □

**Lemma A.4″ (the head moves two sites per tick).** Let `x_1` be even, `C` the odd cube containing `x`, `C'` the even cube containing `x−e_1`. For every string vector `ψ_x` from `x`, `t_{C'}t_Cψ̂_x=κ_xψ̂''_{x−2e_1}`, where `ψ''` has two more links and `κ_x=−η_1(x−e_1)η_1(x−2e_1)`. Consequently `ω_x(α_U(A))=ω_x(G_x^*AG_x)=ω_{x−2e_1}(A)` for local `A`, with `G_x=t_{C'}t_C`.

*Proof.* `x_1` even puts `(x−e_1,x)` in `C` and `x+e_1∉C`; `(x−2e_1,x−e_1)` lies in `C'` (`LW1_5.md` line 216). On `span{ψ̂_x,ψ̂'_{x−e_1}}`, the term of `X_C` for `ℓ=(x−e_1,x)` acts as `4η_1(x−e_1)σ_x` (Lemma A.4′; `Q_ℓ=1` on both vectors, whose `ℓ` has end numbers `(16,0)` and `(15,1)`). Every other term of `X_C` kills both vectors: a direction-1 edge of `C` off the string line has `P=−1` at both ends; a direction-2 or 3 edge has end numbers `(8,8)`, so `Q` on the right gives zero. So the span is invariant and `t_C=cos(π/2)−iη_1(x−e_1)sin(π/2)σ_x` there: `t_Cψ̂_x=−iη_1(x−e_1)ψ̂'_{x−e_1}`. The same argument in `C'` moves the head from `x−e_1` to `x−2e_1` with factor `−iη_1(x−2e_1)`. In the circuit `S_eS_o` the gates that Lemma A.4 collects are `t_C` and the eight even-cube gates meeting `C`; after `t_C` only `t_{C'}` meets a site with `P=+1`, so `G_x` acts on string vectors as `t_{C'}t_C`. `U=S_eS_o` as automorphisms (`LW1.md` E1), so Lemma A.4 applies to the circuit `S_eS_o`. Finally `ω_r^{(x)}(G_x^*AG_x)=ω_{r+1}^{(x−2e_1)}(A)`: `G_x` is unitary, the far ends coincide, and the norms match (`16^{2r+1}` times `16^2`); let `r→∞`. □

**Vector form.** Let `(H',π',Ω')` be the GNS triple of `ω'` on the field algebra `𝔄`. For a matter-activated update `𝒱`, `ω'` is `α_𝒱`-invariant (Lemma A.1(c)), so `Û_𝒱π'(A)Ω':=π'(α_𝒱^{−1}(A))Ω'` defines a unitary (the Schrödinger implementer); likewise `T̂_βπ'(A)Ω':=π'(τ_β(A))Ω'`. String vectors `ψ_{x,r,b}=π'(B_{r,b}(x))Ω'` live in `H'`. Then `Û_𝒱ψ_{x,r,b}=π'(G_x)ψ_{x,r,b}` for large `r`, and `T̂_βψ_{x,r,b}=ψ_{x+2β,r,b}`. *Proof.* `α_𝒱^{−1}(B)=YBY^*` with `Y` the finite circuit of the gates in the light cone of `B`; each gate fixes `Φ'`, so `π'(Y^*)Ω'=Ω'` and `Û_𝒱ψ=π'(Y)ψ`; the induction in the proof of Lemma A.4 gives `π'(Y)ψ=π'(G_x)ψ` (`Y` contains every gate of `G_x`, since the light cone of `B` contains `x`). Translations: `τ_β(B_{r,b}(x))=B_{r,b}(x+2β)` and `T̂_βΩ'=Ω'`. □ In particular, with `ψ̂` normalized and the far end fixed, `Û_Uψ̂_x=κψ̂_{x−2e_1}` for `x_1` even (Lemma A.4″): in the Schrödinger picture the head moves by `−2e_1` per tick and the string grows behind it. Here `κ=−η_1(x−e_1)η_1(x−2e_1)∈{±1}`, the same for all `x∈2Z³` (even translations preserve the signs).

### 4.5 The covariant representation and the band

For `c=(c_2,c_3)∈Z²` put `x_c=(0,2c_2,2c_3)`, and let `(H_c,π_c,Ω_c)` be the GNS triple of `ω_{x_c}` on `𝔄^G` (Lemma A.3(a)). For each `x∈2Z³` put `G^{(x)}=G_{x+2e_1}`, the unitary of Lemma A.4″ that moves the head from `x+2e_1` to `x`. Three identities for local `A` (Lemma A.4″ at `x+2e_1`, and translation covariance of strings and of `ω'`):
(i) `ω_{x+2e_1}(α(A))=ω_x(A)`; (ii) `ω_x(G^{(x)}AG^{(x)*})=ω_{x+2e_1}(A)`; (iii) `ω_{x+2β}(τ_β(A))=ω_x(A)`.

**Definition of the implementers.** On each `H_c`, with `x=x_c` and `G=G^{(x)}`:
`Ũπ_c(A)Ω_c=π_c(α(A))π_c(G^*)Ω_c`, `T_{e_1}π_c(A)Ω_c=π_c(τ_{e_1}(A))π_c(G^*)Ω_c`.
For `β_⊥=(0,β_2,β_3)`, `T_{β_⊥}:H_c→H_{c+(β_2,β_3)}`, `T_{β_⊥}π_c(A)Ω_c=π_{c+(β_2,β_3)}(τ_{β_⊥}(A))Ω_{c+(β_2,β_3)}`. Put `T_β=T_{e_1}^{β_1}T_{β_⊥}` on `H=⊕_{c∈Z²}H_c`, `π=⊕_cπ_c`.

**Lemma A.6.** `(H,π,T,Ũ)` is a covariant representation in the sense of `RCS1.md` Definition 5, and `ŨΩ_c=T_{e_1}Ω_c` for every `c`.

*Proof.* Isometry: by (ii) then (i), `‖π_c(α(A))π_c(G^*)Ω_c‖^2=ω_x(Gα(A^*A)G^*)=ω_{x+2e_1}(α(A^*A))=ω_x(A^*A)`; for `T_{e_1}` use (iii) in place of (i); for `T_{β_⊥}` use (iii). Dense range: `G^*` is a unitary of `𝔄^G`, so `π_c(G^*)Ω_c` is cyclic, and `α`, `τ_β` are automorphisms of `𝔄^G`. So all three extend to unitaries implementing `α`, `τ_{e_1}`, `τ_{β_⊥}`. `ŨΩ_c=T_{e_1}Ω_c=π_c(G^*)Ω_c` by definition.
Commutation. Two unitaries that implement the same automorphism and agree on a cyclic vector agree. `ŨT_{e_1}` and `T_{e_1}Ũ` both implement `α∘τ_{e_1}=τ_{e_1}∘α` (the update commutes with even translations). On `Ω_c`: `ŨT_{e_1}Ω_c=π_c(α(G^*)G^*)Ω_c` and `T_{e_1}ŨΩ_c=π_c(τ_{e_1}(G^*)G^*)Ω_c=π_c(G'^*G^*)Ω_c`, `G'=G^{(x+2e_1)}`. Let `D=α(G^*)G^*−G'^*G^*`. By Lemma A.3(a), `ω_x(D^*D)=lim_rΣ_b‖π'(D)ψ_{x,r,b}‖^2/16^{2r+1}`. In `H'`, with normalized vectors and fixed far end: `π'(G^*)ψ̂_x=κψ̂_{x+2e_1}` and `π'(G'^*)ψ̂_{x+2e_1}=κψ̂_{x+4e_1}` (Lemma A.4″, `κ` real). Also `π'(α(Z))=Û_U^*π'(Z)Û_U`, so `π'(α(G^*))ψ̂_{x+2e_1}=Û_U^*π'(G^*)Û_Uψ̂_{x+2e_1}=Û_U^*π'(G^*)κψ̂_x=Û_U^*ψ̂_{x+2e_1}=κψ̂_{x+4e_1}`, using the vector form twice. So `π'(D)ψ̂_x=0`, hence `ω_x(D^*D)=0` and the two vectors agree. `T_{e_1}T_{β_⊥}=T_{β_⊥}T_{e_1}` and `ŨT_{β_⊥}=T_{β_⊥}Ũ` follow the same way from `τ_{β_⊥}(G^{(x)})=G^{(x+2β_⊥)}` (translation covariance of the circuit): both sides map `Ω_c` to `π_{c'}(G^{(x_{c'})*})Ω_{c'}`. The transverse `T`'s compose exactly. So `T` is a unitary representation of `Z³` commuting with `Ũ`. `H` is separable, a countable sum of GNS spaces of a separable algebra. □

**Theorem A (a propagating spinor-class band from straight strings).** On the U(16)-rishon witness with `m=16`, at every pair of cube angles, take the update `U` of §4.2, the D1 state `ω'` of §4.1, the axis `e=e_1`, and the covariant representation `(H,π,T,Ũ)` of Lemma A.6. Then:
(a) each summand `π_c` is the GNS representation of a straight-string limit state along `+e_1`; summands with different `c` are disjoint (Lemma A.3(c));
(b) every vector of `H` has `χ_tot(π:ω')=−1` and boundary label `−1`, so `π` is spinor class under R-16^str′, and keeps the background centre value `π(z_y)=1` at every site (Lemma A.3(b));
(c) `u_b=T_bΩ_{(0,0)}` is orthonormal, `T_βu_b=u_{b+β}`, `Ũu_b=u_{b+e_1}`, and `F(Σ_bφ̂_be^{iK·b})=Σ_bφ̂_bu_b` defines a band `(1,F,V)` with `V(K)=e^{iK_1}`;
(d) its nodes are the plane `K_1=0`; at each node `N=(−1,0,0)`. So the band has a node and a nonzero leading generator.

*Proof.* (a), (b): cited lemmas. (c) `u_b` represents `ω_{2b}`: `T_{e_1}Ω_c=π_c(G^*)Ω_c` represents `A↦ω_x(GAG^*)=ω_{x+2e_1}(A)` by (ii), and `T_{e_1}^*Ω_c` represents `ω_x∘τ_{e_1}=ω_{x−2e_1}` by (iii); induct, and use `T_{β_⊥}` for the transverse part. Distinct `b` with distinct `(b_2,b_3)` lie in distinct summands. For equal `(b_2,b_3)` and `b_1≠b'_1`, `P_{2b}` is sharp `+1` in `ω_{2b}` (the head is in `H_+`) and `−1` in `ω_{2b'}` (string interiors and background have matter in `H_-`), so `u_b⊥u_{b'}`. `Ũu_b=T_bŨΩ_{(0,0)}=T_bT_{e_1}Ω_{(0,0)}=u_{b+e_1}` by Lemma A.6. `F` is an isometry by orthonormality and Parseval, `T_βF=FM_β`, and `ŨF(e^{iK·b})=u_{b+e_1}=F(e^{iK_1}e^{iK·b})`. (d) `V(K)=1` iff `K_1=0`; near it `h=i log V=−K_1`, so `N_j=∂_jh=−δ_{j1}`. □

**Conventions.** With `α(A)=U^*AU` (LZ1), `Ũ` is the inverse of the Schrödinger evolution, so the sign of `N_1` is a convention; the Schrödinger head velocity is `−e_1` cells per tick. Rephasing `T_{e_1}↦νT_{e_1}` or `Ũ↦μŨ` (`|μ|=|ν|=1`) changes `V` to `μν̄e^{iK_1}`: the node plane moves and `N` is unchanged. So the existence of a node and `N_1≠0` do not depend on the phase conventions that `ZM1_OBS.md` line 80 leaves open.

**Lemma A.5 (no Clifford cone in a one-dimensional band).** A band with `d=1` has no Clifford cone at any node.

*Proof.* The `N_j` are real numbers. `{N_i,N_j}=2v²δ_{ij}` with `v>0` needs `N_1^2=N_2^2=v^2>0` and `2N_1N_2=0`. □

**Corollary A.5′.** The node of Theorem A is not a Clifford cone. □

### 4.6 RC-W and mirror partners

`CG16S_REFEREE.md` §3.1, Lemma RC-W: "Let `V` be unitary on `H`, commuting with the cell translations, and equal to `L_m⋯L_1`. Each `L_k` is block-diagonal for some partition into blocks, each lying in at most `D` adjacent cells. ... Then `W₃[V]=0`." Its setting: "`H=ℓ²(Z³)⊗C^n`". Its use, §4.2 of that report: "Fix a content parity `σ` and a quasienergy at which the node set of `W_σ` is finite and consists of Weyl points. Then the net chirality there is zero. ... The theorem leaves three things open: gates that violate E, defects over a filled or entangled background, and node sets that are infinite or not all Weyl. Setting F has no links."

**Proposition C (RC-W forces no mirror partner for Theorem A's band).**
(a) The hypotheses of RC-W's pairing statement fail: the representation of Theorem A has links and a filled, entangled background (string sectors over `ω'`), not setting F; and the node set of the band is the plane `K_1=0`, which is infinite and contains no Weyl point.
(b) The conclusion `W₃=0` holds for the band anyway, trivially: for `d=1`, `V^{−1}dV=i\,dK_1` and `(V^{−1}dV)^{∧3}=0`.
(c) So RC-W neither requires a second band nor is contradicted by the absence of one.

*Proof.* (a) Setting F is a single-particle space `ℓ²(Z³)⊗C^n` with no link registers (quoted). The node set is `{K:e^{iK_1}=1}`. `CG16S.md` line 96 defines a Weyl point `K₀` by "`dim ker(V(K₀)−1)=2`", "a smooth rank-two spectral frame with `H=a1+b·σ`" and "`N` invertible". For Theorem A's band, `dim ker(V(K₀)−1)=1` at every node, so no node is a Weyl point. (b) Direct computation. (c) Follows. □

**Remark (not used).** On its image, `Ũ` acts as the shift `u_b↦u_{b+e_1}`. In one dimension, shifts are "the prototypes of systems with non-trivial index" (Gross–Nesme–Vogts–Werner, arXiv:0910.3675, abstract), and a walk with nontrivial index is not a product of partitioned unitaries. There is no conflict: the band's image is not invariant under the separate layers (after `S_o` the head sits at an odd site, outside `ran F`), and the string sector is not a walk on `ℓ²(Z)⊗C^n` with finite `n`, because the head's configuration space in `H_c` includes every string shape. The one-way motion is paid for by the growth of the string.

### 4.7 No Clifford cone for matter-activated updates over these backgrounds

**Proposition B.** Let `ω°` be `ω'` or Example S's state `ω_Φ` (`CG16B.md`), and let `𝒱` be any matter-activated update in LZ1's class on the rishon witness at `m=16` (examples: the base tick; `U` of §4.2; any composition of base layers, their inverses and layers of projected-hop gates). Take straight strings along `+e_1` (for `ω_Φ`, along any `+e_j`). Then:
(a) the string limits `ω_x` exist, and every representation quasi-equivalent to some `π_x`, and every direct sum of such, has `χ_tot=−1` and boundary label `−1`;
(b) each `π_x∘α_𝒱` is unitarily equivalent to `π_x`;
(c) `π_x` and `π_{x'}` are disjoint when `x`, `x'` lie on different lines along the axis;
(d) every band in every covariant representation whose observable representation is a direct sum of subrepresentations, each quasi-equivalent to some `π_x`, satisfies `V(K₀+se)=1` for small real `s` and both transverse axes `e`, at every node `K₀`. So the transverse `N_j` vanish and no node is a Clifford cone.

*Proof.* For `ω_Φ`: `CG16B.md` Example S gives matter `|i_0⟩∈H_-`, every link `(16,0)`, `P_y=−1` and `z_y=+1` sharply, and gauge and translation invariance; every matter-activated gate fixes `Φ`, as in Lemma A.1(c); strings along `+e_j` touch only `(16,0)` links of direction `j`. So the proofs of Lemmas A.3 and A.4 apply verbatim to both states; (a) is Lemma A.3(a),(b), (b) is Lemma A.4, (c) is Lemma A.3(c).
(d) is `RCS1.md` Corollary 9, whose proof is abstract; `CG16B.md` Theorem 6.1 records that it applies on (F)-laws "when its disjointness and tick-equivalence hypotheses hold", and (b), (c) are those hypotheses. Rebuilt in short, after `RCS1.md` Theorem 8(d): group the summands by the transverse position `c` of their line; by (c), summands in different groups are disjoint, so the closed spans `H^{(c)}` of the groups are mutually orthogonal and their projections are central in `π(𝔄^G)''`. `AdŨ` maps the central projection of a quasi-equivalence class to that of the class composed with `α^{−1}`; by (b) this is the same class, so `ŨH^{(c)}=H^{(c)}`. Translation covariance of the strings maps the class of `π_x` to that of `π_{x+2β}`, so `T_βH^{(c)}=H^{(c+2β_⊥)}`. `RCS1.md` Theorem 5 with `q(c)=c_2/2`, then `q(c)=c_3/2`, gives the two directional flatness statements (Lemma 5.1 there is rebuilt in `CG16D.md` Lemma N, steps 1-2). A Clifford triple with `v>0` would give `(N_2)^2=v^2≠0`. □

With both labels, `CG16D.md` §3 (after Lemma N) records that "Lemma N's argument gives `V=1` on `(K₀+span{e_2,e_3})` near the node"; the same holds here.

**The named failing step.** For matter-activated updates over these frozen backgrounds, a Clifford node fails at (c): the far ray's transverse position is a sharp, conserved label (`p` at the target ends far along the line) that separates sectors. Theorem A shows that nothing else fails: motion along the ray is possible. By `RCS1.md` Corollary 9, a Clifford example needs non-disjoint sectors at distinct transverse positions (a background in which the string's position is not observable, as in Naaijkens' Lemma 3.6 and Levin–Wen §V), or sectors that are not quasi-equivalent to their tick transforms (an update that acts on the far ray, so not matter-activated over these backgrounds).

## 5. Attacks and smuggle checks

### 5.1 Attacks on Theorem A (each fails at the named step)

- **T1, "LZ1 Theorem 2.2 already makes every odd band flat."** It concerns bands in the GNS space of a D1 state, split by finite centre patterns. Theorem A's representation is not a subrepresentation of the GNS of `ω'`: its `χ_tot` is `−1`, while every subrepresentation on `H_phys` of `ω'` has `χ_tot=+1` (`RCS1.md` R2(b)), and `χ_tot` is invariant under quasi-equivalence (R2(a)). Its centre pattern is trivial (`π(z_y)=1`), and it is odd because it is not finitely localized (`CG16B.md` Proposition L(iv)). The step that would transfer LZ1 Theorem 2.2, "the odd vectors carry a finite nontrivial pattern", fails.
- **T2, "CG16D Theorems 5-6 forbid motion of spinor-class sectors on link-pure registers."** Those theorems use CG16D's identity `∏z_x=(−1)^{|Λ|}(∏d_ℓ)Φ_Λ`, in which the matter factor of `z_x` is the scalar `−1` (bilinear embedding), so the flux is central. Under S′ the matter factor is `−P_x`, and the witness identity is `∏z=ε^{|Λ|}s_ΛP_ΛF_{∂Λ}` (`CG16B.md` Theorem 6.1). `P_Λ` is not central in `𝔄^G` (a hop across `∂Λ` changes it), so neither is `F_{∂Λ}`. The step "the boundary flux is a central label" fails. The digest's warning "Keep the two flux identities separate" applies.
- **T3, "`RCS1.md` Corollary 9 forbids the band."** It forbids transverse motion only. Theorem A's band has `N_2=N_3=0`, as Corollary 9 and Proposition B require.
- **T4, "the band uses the cancellation of the base tick, so it is not the law's motion."** True, and stated (Remark in §4.2). The update is in LZ1's class and meets NN-a (Lemma A.2). The base tick alone moves the string head in every direction allowed by the background, and whether some update that keeps that motion carries a band along the ray is not decided here.
- **T5, "the vectors `u_b` for different `b_1` lie in different superselection sectors."** They lie in one summand `H_c`: the head moves by local gauge-invariant unitaries (Lemma A.4″), so all head positions on one line give vector states of one GNS representation (Lemma A.6).

### 5.2 Four-test checks

Tests: (1) states or fixes a part's target; (2) open-ended, so a part can add to it; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need. P pass, C conditional, F fail.

| Item | 1 | 2 | 3 | 4 | Note |
|---|---|---|---|---|---|
| Definition B (matter-activated gate) | P | P | P | P | A closed hypothesis of Proposition B; the base layers satisfy it (Lemma A.1′). It is a class for a theorem, not a reading. |
| `ω'` and `U` as witnesses | — | — | — | — | Not proposed. They are an existence witness inside existing definitions (D1, LZ1's class, NN-a, R-CS^str, `χ_tot`, R-16^str′). As law or vacuum data they would fail test 1 (chosen for the target) and test 4 (the cancellation, the projectors `Q_ℓ` and the `(8,8)` links have no reason outside this question). |
| Restriction "appended layers may not invert base layers" (owner question only, not proposed) | P | F | C | F | Test 2: no closed boundary separates inverses from other layers; the conjugate form `U^♮` keeps the base tick first and still cancels it, and partial or sector-wise inverses are not covered. Test 3: it would remove Theorem A's witness without deciding whether another exists. Test 4: no reason on file asks for it. So the plain reading of LZ1's class stands. |

The readings used (R-CS^str with `χ_tot`, R-16^str′) are the owner's working candidates; they are used as stated and not adopted.

## FINISH

**Proved (author side, pass 1; not yet distilled or refereed).** On the U(16)-rishon witness at `m=16`, every pair of cube angles:
- Lemma A.1, A.1′: the product state `ω'` (direction-1 links full/empty, directions 2 and 3 at `(8,8)` in site singlets, matter in `H_-`) is locally gauge invariant, translation invariant, parity-sharp and sharp in every `z_x`, and is a D1 state for every matter-activated update; the base cube layers and their inverses are matter-activated.
- Lemma A.2: the update `U` (base tick, its inverse layers, then two layers of cube gates `e^{−i(π/8)X_C}` built from projected hops) is in LZ1's class, commutes with every cell lift, and meets NN-a read with the witness register.
- Lemma A.3: straight `+e_1` string limits over `ω'` exist; they have `χ_tot=−1`, boundary label `−1` (spinor class under R-16^str′) and background centre values; strings on different lines give disjoint sectors.
- Lemmas A.4, A.4′, A.4″: a matter-activated update acts on a string state by a local gauge-invariant unitary; the projected hop at angle `π/8` swaps the head across one link exactly; `U` moves the head by two sites per tick along the ray and grows the string.
- Lemma A.6 and **Theorem A**: the covariant direct sum of the ray sectors carries a band `V(K)=e^{iK_1}` with nodes on the plane `K_1=0` and `N=(−1,0,0)`. Existence of a node and `N_1≠0` do not depend on phase conventions.
- Lemma A.5, Corollary A.5′: the node is not a Clifford cone.
- Proposition C: RC-W forces no mirror partner for this band (its hypotheses fail; `W₃=0` trivially; no Weyl point).
- **Proposition B**: over `ω'` or Example S's `ω_Φ`, for every matter-activated update in LZ1's class, every band in every covariant representation built from these straight-string sectors is flat in both transverse directions at each node; no Clifford cone. Named failing step: the far ray's transverse position is a sharp conserved label that separates sectors.

**Counterexamples.** Theorem A refutes the statement "no locally gauge-invariant D1 state and axis admit a covariant representation built from straight-string spinor-class sectors with a band that has a node and a nonzero leading generator", for updates in LZ1's class that meet NN-a on the rishon witness. It fills the case `RCS1.md` §5 left open ("does not rule out motion along the ray").

**Open by name.** RCS-P in its Clifford form (`RCS1.md` §8, inherited): a Clifford node from straight-string sectors; Proposition B names the failing step over frozen backgrounds, and `RCS1.md` Corollary 9's two alternatives remain the only ones on file. MT1-S[R-CS^str] in the VC1 vacuum (inherited). R-CS and R-16^str′ (owner candidates, not adopted). CG16D-NLP (not worked here). Owner question, recorded and not proposed: whether LZ1's update class should exclude appended layers that undo base layers (§5.2; the restriction fails tests 2 and 4).

**What changes downstream.**
- *RCS-P / RCS-P16.* The "node with a nonzero leading generator" question is decided yes on the rishon witness (Theorem A). What remains is the cone, not motion: over frozen backgrounds with matter-activated updates, transverse flatness is forced (Proposition B).
- *MT1-S and LZ1's fermion clause.* A propagating `χ_tot`-odd band exists in a charged-sector representation in LZ1's class; it is one-dimensional, moves along one axis and is not a Clifford cone. Any route to MT1-S must make the string's transverse position unobservable (a fluctuating-string state; RCS1's A3) or act on the far ray.
- *CG1 / R-16^str′.* Spinor-class sectors in the boundary-flux sense can move; they need not be static.
- *RC-W (CG16-S).* Its mirror pairing does not reach charged-sector bands of this kind; a chiral claim about such bands needs its own argument.
- *LZ1's update class.* It is closed under appending inverses of base layers; results that depend on the base tick's own motion must say so.
- Nothing is adopted; no law, reading, axiom or working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
