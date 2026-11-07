lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# KINV: the zoom's kinematic lemma K-INV, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as a pass-1 lane of the TOE assembly under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. No step rests on a computation. One `[check]` (section 8) is a scratch confirmation of two finite facts that the text proves by hand; it guides and never proves.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (the brief names `289a6a6b5`; HEAD was `fa803749e` when read, which adds only `prior/SGAP0.md` on top of it) | `fa803749e` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `f5af11cd0` |
| `origin/docs/consolidate-gauge-matter-registers` (read with `git show` only, after `git fetch -q`) | `7086189d1` |

Every result used lives in this folder. From the other two refs I read the two entries of `prior/KINV.md` that come closest to a K-INV construction; section 1 records what they give. The digest's other entries (state- and energy-adapted refinements, the Peter-Weyl note, the block-spin note, the YM H-BLOCK port) concern states, energies, fine-to-coarse compression or limiting states, not a coarse-to-fine invariant embedding; I used their digest summaries and did not reopen them.

Files read at that commit, by line (last-change commit in brackets). `prior/KINV.md` lines 1-92, all [`289a6a6b5`]. `ZM1INV.md` lines 1-185, all [`14600db35`]. `ZM1INV_REFEREE.md` lines 1-327, all [`f21a268c9`]. `GB1Z2L5.md` lines 1-127, all [`3de4558ac`]. `ZM1I1A.md` lines 1-156, all [`59cdde899`]. `ZM1.md` lines 1-110 (status with Amendments 1-4, definitions, Definition Z, Definition G, Theorem Z0) and 305-402 (section 5, attacks, scope) [`14600db35`]. `TOE_ASSEMBLY.md` lines 201-270 (sections 3.4-3.11) and 726-740 (section 11, the walls) [`dd158e6a2`]. `VC1_5.md` lines 1-70 (status, definitions, section 2 with Theorems 2.1-2.2, Theorem 3.1) and the statements at lines 84-92 (Theorem 4.2 with proof) and 124 (Theorem 5.5) [`727ad9884`]. `ZM1I1A_OWNER_CHECK.md` lines 1-36 (Astra's endpoint argument) [`2511de5dc`]. `ZM1INV_DRAFT.md` lines 45-50 (the pass-1 text of (INV-1)-(INV-4)) and line 155 [`64655facc`]. `Y2W_DRAFT.md` lines 1-40, for the file format only. On `origin/main`: `docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` lines 128-156. On `origin/docs/consolidate-gauge-matter-registers`: `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 284-312.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The owner texts ZM1-INV (section 3.9) and ZM1-I1[a] (section 3.8) and the retained Definition Z condition (Z-b) are read plainly. Where they leave a choice open (which automorphism a coarse rotation acts by; whether an O coarse law is allowed), the choice is named in the theorem's hypotheses and nothing is adopted.

**Working set used, by name.** PS-5, PS-6r and PS-7r only through the two five-mode laws `L5-U[m]` and `L5-O[S_+]` as frozen in `VC1_5.md` section 2; the owner decisions ZM1-I1[a] (section 3.8), ZM1-INV (section 3.9) and R-form as the owner confirmed it there ("Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁"). No axiom and no working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text where used: a character of a unital C*-algebra maps every self-adjoint element into its spectrum; matrix units split a unital C*-algebra as `M_n ⊗` (relative commutant); joint spectral projections of commuting self-adjoint elements with finite spectra; the norm of a product of even elements on disjoint finite regions (Jordan-Wigner order, as in `ZM1INV.md` R6); a projection within distance `<1` of `0` or `1` equals it. Literature is context only (section 2); no citation is load-bearing.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` section 3.9, the owner text ZM1-INV: "Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁ (R-form). Replace the full-algebra map by a unital injective *-homomorphism \(\Phi:\mathfrak A_1^G\longrightarrow\mathfrak A^G\). Retain cell covariance. Require exponential locality for every local invariant input, with support-radius-dependent constants. Use this \(\Phi\) in class (a). Impose no map on charged fields or Gauss generators."

The retained covariance is Definition Z's (Z-b), `ZM1.md` section 1.3: "(Z-b) *cell covariance*: each coarse cell translation and each proper cubic rotation about a coarse cell centre has a fine lift in the law's symmetry group (`LW1.md` A2, `MT1.md` Theorem 1) with `Phi o g_1 = g o Phi`, up to a global phase or global parity". The pass-1 text of ZM1INV keeps the rotations: "(INV-2) cell covariance: each coarse cell translation and each proper cubic rotation about a coarse cell centre has a fine lift `g` with `Φ∘g₁=g∘Φ`" (`ZM1INV_DRAFT.md` line 46).

The lemma, `ZM1INV.md` section 1 item 4: "**K-INV(m,m₁,L)** asks for that map with its covariance and locality, independently of states and updates. **K-INV(O; m₁, L)** asks for that map from a coarse `L5-U[m₁]` invariant algebra to the fine `L5-O` invariant algebra. **K-INV-O** is the analogous O-to-O question." Its open list, section 0: "**K-INV(m, m₁, L)**, `m` even, any `m₁∈{1,…,9}`, `L≥2`." and "**K-INV(O; m₁, L)** and **K-INV-O**."

Why it matters, `ZM1INV.md` Theorem 2.3: "For a locked U fine witness, even `m`, and its base tick, the target with coarse `m₁` holds exactly when K-INV holds for some `m₁∈{1,…,9}` and `L≥2`." With R1, this holds for every coarse `m₁`.

The lane brief: "decide K-INV on L5-U[m] (some m) and on L5-O[S_+]: construct such a map for some L >= 2, or prove none exists for a named class, naming the step", and "The character of the invariant algebra (GB1Z2L5 Theorem A) and the abelian structure it forces are new tools the three failed attacks did not use; say whether they help."

## 0.1 Outcome in one paragraph

**Decided for odd coarse registers; open for even ones after three new named attacks.** *Proved (Theorem P, section 4).* For odd `m₁` there is **no** unital `*`-homomorphism `Φ:𝔄₁^G[L5-U[m₁]]→𝔄^G` that is covariant under one proper cubic rotation about a coarse cell centre, when the fine law is `L5-U[m]` with `m` even or `L5-O[S_+]`. No locality and no injectivity are used, and `L` is arbitrary. So K-INV(m, m₁, L) is false for every even `m`, every odd `m₁` and every `L`, and K-INV(O; m₁, L) is false for every odd `m₁` and every `L`. The step: the fine locked character is invariant under every fine cell lift, so `χ₀∘Φ` is a coarse character invariant under the rotation by π about the axis through a coarse cell centre and the midpoint of a coarse link inside the cell; that rotation exchanges the two ends of the link, so the character gives both end numbers the same value, `m₁/2`; a character maps the end number into its spectrum, a set of integers. So the character **does help**: it gives this obstruction, together with the rotation part of cell covariance. No earlier K-INV result on file uses the rotation part of covariance. *Consequence.* In the locked even-`m` U vacua and the locked O vacua, ZM1-I1[INV] holds exactly when K-INV holds for some **even** `m₁` and `L≥2` (Corollary P2). With an odd coarse register, ZM1-I1[INV] has no instance for any fine vacuum, update or comparison class on these fine laws. *Open by name.* K-INV(m, m₁, L) with `m, m₁` even; K-INV(O; m₁, L) with `m₁` even; K-INV-O. Three new attacks fail there, each at a proved step: (A) covariant characters fail because the constant map `a↦χ₁(a)1` through the coarse locked character meets every K-INV condition except injectivity (Proposition T); (B) a good sector completed by a character on a defect projection fails at Lemma NGF: no K-INV map acts by a character on any nonzero invariant projection; (C) decimation that is equivariant for the coarse `U(1)` charge at representative sites fails at Theorem J: the joint spectrum of the two end charges of a coarse link forces representatives of neighbours to be fine neighbours, so `L=1`. The abelian structure beyond the character (no invertible `a,b` with `ab=λba`) adds nothing for K-INV, since both algebras have characters (section 5). No construction of a K-INV map is found.

## 1. Prior work used

All paths are in this folder at `fa803749e`. Each result is quoted where it is used.

| Result | Path | Use here |
|---|---|---|
| Locked even-`m` U and locked O witnesses restrict to characters on `𝔄^G` | `ZM1INV.md` Theorem 2.1 | Theorem P (the fine character `χ₀`); Proposition T (the coarse character). |
| Characters of every named law, odd `m` included | `GB1Z2L5.md` Theorem 2 | Section 5 (whether characters help). |
| Odd-`m` oriented character; it is not reversal invariant | `ZM1INV.md` R1 | Remarks after Theorem P (the odd coarse character exists but is not of the form `χ₀∘Φ`). |
| Reduction of ZM1-I1[INV] to K-INV in locked vacua | `ZM1INV.md` Theorem 2.3, R2 | Corollary P2 (restricted to even `m₁`). |
| Witnesses satisfy "(iii) invariance under all the stated cell lifts" | `VC1_5.md` Theorems 4.2, 5.5; section 1 item 5 | Lemma P0 (invariance of `χ₀` and `χ₁`). |
| Cell lifts carry end numbers to their images; end-exchanging reversals lie in the cell group | `VC1_5.md` Theorem 2.2 | Lemma P0; Theorem P. Extended: Theorem P uses one rotation about a cell centre and checks it exchanges the ends. |
| `E` commutes with lifts | `VC1_5.md` Theorem 2.1 | Lemma P0. |
| "Every invariant element is even under matter parity" | `GB1Z2L5.md` Theorem 6 (which credits `RCS1.md` Theorem 4) | Lemma NGF (evenness of `E` and of `Φ(τ_βP)`); Theorem J (evenness of star generators). |
| Shared-support bound and the Jordan-Wigner product step | `ZM1INV.md` R6 | Lemma NGF reuses the product step. |
| Good-sector isomorphism; "Extending this local good-sector action by zero is not unital" | `ZM1INV.md` Theorem 3.4 and the remark after it | Lemma NGF (extended: a character filler on any nonzero invariant projection also fails). |
| End-equivariant link decimation fails; one-link paths fail for `L≥2` (E1) | `ZM1INV.md` Theorem 3.3 | Theorem J (extended from link factors and end numbers to arbitrary maps and site charges; E1 reused). |
| Spectral-endpoint argument against G1-eq (one model's argument, not refereed) | `ZM1I1A_OWNER_CHECK.md` lines 13-32 | Theorem J is a two-site joint-spectrum form of the same idea; credited there. |
| Neutral matrix registers excluded | `ZM1INV.md` Theorem 3.2, R5 | Section 5 (context). |
| Nonzero uniformly local maps are unital | `GB1Z2L5.md` Theorem 6 | Remark after Theorem P (unitality is not an extra assumption). |
| One-dimensional even refinement: "a unital injective isometric *-map A_n -> A_(n+1)" with "rho_(l,m)rho_(m,n)=rho_(l,n)" | `origin/main:docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` lines 142-150 (ledger "unaudited", per the digest) | Context: a quasi-free refinement of free fermions in one dimension, with no gauge registers and no rotations; Theorem P does not apply to it and it does not supply a K-INV map. |
| 2+1D `Z_3` split: "each parent bond's electric value is the total of the 4 child bonds crossing its face"; a level-matched polar isometry "is covariant" | `origin/docs/consolidate-gauge-matter-registers:docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 308-311 ("author statements for review", per the digest) | Context: an isometry of Gauss-law state spaces, so `a↦VaV*` is a non-unital map, not a K-INV map. Its face-total rule is consistent with Theorem P: totals of integer fine fluxes are never half-integers (remark after Theorem P). |

**Prior work the digest missed.** Four inputs decide points here and are not in `prior/KINV.md`.
- `VC1_5.md` Theorem 2.2: "Every link has an end-exchanging reversal in `G` whose linear part transposes two axes", and the U lifts "carry Gauss generators and end numbers to their images". This is the symmetry Theorem P uses.
- `VC1_5.md` Theorems 4.2 and 5.5 with section 1 item 5: the locked witnesses satisfy "(iii) invariance under all the stated cell lifts". So the fine character is cell invariant, which Theorem P needs.
- `ZM1INV_DRAFT.md` line 46: pass 1 states (INV-2) with "each proper cubic rotation about a coarse cell centre". The distilled `ZM1INV.md` compresses this to "cell covariance" (referee row 5, P6). Theorem P depends on the rotations.
- `ZM1I1A_OWNER_CHECK.md` lines 13-32: Astra's spectral-endpoint argument against R-G1EQ. It is the closest prior to Theorem J.

**Failed attempts on file, not repeated.** Neutral matrix registers (`ZM1INV.md` Theorem 3.2, R5), end-equivariant link decimation (Theorem 3.3) and good-sector decimation with representative end data (Theorem 3.5). Theorem J and Lemma NGF below each attack a wider class than the corresponding failed attempt; the new step is named in each.

## 2. Literature read

Searches on 2026-11-07 (web search, then the arXiv abstract page of each entry marked "fetched"). Abstract pages were read through a fetch tool that summarizes and caps verbatim quotes; I did not read full texts. So every entry below is context. None is a proof input, and every result this file uses is proved in it.

| Work | arXiv | Status here | What it gives this lane |
|---|---|---|---|
| A. Brothier, A. Stottmeister, "Operator-algebraic construction of gauge theories and Jones' actions of Thompson's groups" (CMP 376 (2020)) | 1901.04940 | abstract fetched | Refinement maps for 1+1-dimensional gauge theories, built as inductive limits with a gauge group action. `ZM1I1A.md` RC-6 checked its eq. (2.1) map for finite groups (unital, injective, finite range, translation covariant). It is a one-dimensional analogue; it has no rotations and no finite rishon registers, so Theorem P's obstruction does not arise there. |
| V. Morinelli, G. Morsella, A. Stottmeister, Y. Tanimoto, "Scaling limits of lattice quantum fields by wavelets" (CMP 2021) | 2010.11121 | abstract fetched; first sentence: "We present a rigorous renormalization group scheme for lattice quantum field theories in terms of operator algebras." | The renormalization group as an inductive system of scaling maps between lattice field algebras, for free scalar fields. The template K-INV follows; not used. |
| T. J. Osborne, "Continuum Limits of Quantum Lattice Systems" | 1901.06124 | abstract fetched | A general procedure for effective continuum descriptions; context only. |
| L. S. Trezzini, A. Pizzamiglio, A. Bisio, P. Perinotti, "Renormalisation of Fermionic Cellular Automata" | 2511.23398 | abstract fetched; first sentence: "We present an exact renormalisation scheme for fermionic cellular automata on hypercubic lattices." | Tiles with retained subspaces; the subspace (non-unital) notion `ZM1.md` Attack 3 discussed. K-INV is unital, so not used. |
| J. I. Cirac, D. Pérez-García, N. Schuch, F. Verstraete, "Matrix Product Density Operators: Renormalization Fixed Points and Boundary Theories" (Ann. Phys. 378 (2017)) | 1606.00608 | abstract fetched | Renormalization fixed points of tensor-network states in one dimension; state-level, not an algebra embedding. Context. |
| D. Gross, V. Nesme, H. Vogts, R. F. Werner, "Index theory of one dimensional quantum walks and cellular automata" (CMP 310 (2012)) | 0910.3675 | abstract fetched | The index of locality-preserving automorphisms. A locality index is a candidate tool for the even-`m₁` case; no index for non-surjective embeddings is set up here. |
| H. C. Po, H. Watanabe, C.-M. Jian, M. P. Zaletel, "Lattice Homotopy Constraints on Phases of Quantum Magnets" | 1703.06882 | abstract fetched | Lieb-Schultz-Mattis-type constraints from the full space group, including point-group symmetries; the abstract's example is a half-integer moment on a site with even-order rotation symmetry. Theorem P has the same shape: an odd number `m₁` on a link whose midpoint is fixed by a rotation of order 2 that exchanges the ends rules out a symmetric character, the algebraic analogue of a symmetric product state. Analogy only; Theorem P is proved directly. |
| D. V. Else, R. Thorngren, "Topological theory of Lieb-Schultz-Mattis theorems in quantum spin systems" (PRB 101 (2020)) | 1907.08204 | abstract fetched | General LSM criterion with space-group symmetry. The fetched abstract does not state a Wyckoff-position criterion; context only. |
| A. Aaserud, D. E. Evans, "K-theory of AF-algebras from braided C*-tensor categories" | 1803.03227 | abstract fetched | Credits Renault, Wassermann, Handelman-Rossmann and Evans-Gould with "explicitly described the K-theory of certain unital AF-algebras". `𝔄^G` is AF; a K-theory route to K-INV without locality is context (section 5). |
| S. Knappe, G. Rudolph, M. Schmidt, "Stratified structure of the observable algebra of Hamiltonian lattice gauge theory" | 1909.10921 | abstract fetched | Observable algebras of lattice gauge theory on a finite lattice; different setting (compact Lie group links). Context. |
| A. Brothier, A. Stottmeister, "Canonical quantization of 1+1-dimensional Yang-Mills theory: an operator-algebraic approach" | 1907.05549 | NOT VERIFIED (search result only) | Context. |
| T. J. Osborne, A. Stottmeister, "Conformal field theory from lattice fermions" | 2107.13834 | NOT VERIFIED (search result only) | Context. |
| D. Handelman, W. Rossmann, "Actions of compact groups on AF C*-algebras" (Illinois J. Math. 29 (1985)); A. Wassermann's work on product-type actions; G. A. Elliott's classification of AF algebras (1976) | none | NOT VERIFIED (search results and memory only) | Context for section 5 only. |

**What the search did not find.** No construction of a unital, covariant, local embedding between gauge-invariant algebras of 3+1-dimensional lattice gauge theories with finite link registers, and no statement of Theorem P. This is a record of one search, not a nonexistence or novelty claim.

## 3. Setting and notation

1. **Laws.** As in `VC1_5.md` section 2: "`L5-U[m]` has the same matter modes and five rishon modes per end in the fixed total link number `m=1,...,9`; its local group is `U(5)`. Write `p_{ℓ,x}` for the end number, `N_x` for matter number and `Q_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}`. Thus `p_{ℓ,x}+p_{ℓ,y}=m` on each link." `L5-O[S_+]` has the same matter, ten rishon modes per link in the even sector `S_+`, and local group `Spin(10)`. `P_m={max(0,m−5),…,min(5,m)}` is the spectrum of one end number (`ZM1INV.md` section 1 item 6).
2. **Algebras.** `𝔄` is the fine quasi-local algebra and `𝔄^G` its fixed algebra under all local gauge transformations; `𝔄₁`, `𝔄₁^G` are the coarse ones (R-form: the coarse system is `L5-U[m₁]` on the coarse lattice, `1≤m₁≤9`). The end number `p_{ℓ,X}` is gauge invariant: `U(5)_X` acts on the `X`-end by unitaries that commute with the number of rishons at that end, `U(5)_Y` acts on the other end, and `p_{ℓ,X}=m₁−p_{ℓ,Y}`; no other site group acts on the link. So `p_{ℓ,X}∈𝔄₁^G`, with spectrum `P_{m₁}`.
3. **Coarse lattice.** `ZM1.md` section 1.1: a coarse cell `u∈Z³` is a block of `8L³` fine sites and "A coarse cell has 8 coarse sites `(u, r)`"; `X=(u,r)↦2u+r` identifies the coarse sites with `Z³`. In these coordinates the coarse cell `u` is the cube `2u+{0,1}³` and its centre is `c_u=2u+(1/2,1/2,1/2)`.
4. **Lifts.** `VC1_5.md` Theorem 2.2: "The U law has lifts with `c_{x,j}↦d_g(gx)c_{gx,j}` and `r^{ℓ,z}_j↦r^{gℓ,gz}_j`, where `d_g=±1` is LW1 A2's sign correction. They commute with `α`, carry Gauss generators and end numbers to their images, and compose up to site matter-sign automorphisms. The O lifts of B1-5 have the same properties, carrying end parities rather than end numbers to their images." I write `β_g` for such a lift. The coarse law, being the same construction, has the same lifts on the coarse lattice; I write `β¹_g`. A *fine lift* in the sense of (Z-b) is a fine `β_g`, possibly composed with a global phase or global parity automorphism.
5. **K-INV conditions.** (INV-1) `Φ:𝔄₁^G→𝔄^G` is a unital injective `*`-homomorphism. (INV-2) for each coarse cell translation and each proper cubic rotation `g₁` about a coarse cell centre there is a fine lift `g` with `Φ∘β¹_{g₁}=g∘Φ` on `𝔄₁^G`. (INV-3) exponential locality: for each `R₀` there are `C_{R₀},ξ` such that for `A∈𝔄₁^G` supported in a coarse ball of radius `R₀`, `Φ(A)` lies within `C_{R₀}e^{-R/ξ}‖A‖` of `𝔄(N_R)`, the fine region within distance `R` of the blocks of that ball (`ZM1INV_DRAFT.md` lines 45-47). K-INV(m, m₁, L) asks for (INV-1)-(INV-3) with a fine `L5-U[m]`, `m` even; K-INV(O; m₁, L) with a fine `L5-O[S_+]`.
6. **Characters.** A character of a unital C*-algebra `𝔅` is a nonzero `*`-homomorphism `χ:𝔅→ℂ`; then `χ(1)=1`.
7. **Locked characters.** For even `m=2k`, `χ₀^{e}` (resp. `χ₀^{f}`) is the restriction to `𝔄^G` of `ψ∘E`, where `ψ` is the product state with flavours `1,…,k` at both ends of every link and empty (resp. full) matter (`VC1_5.md` Theorem 5.5). On `L5-O`, `χ₀^{e}` (resp. `χ₀^{f}`) uses empty (resp. full) matter and links (`VC1_5.md` Theorem 4.2). `ZM1INV.md` Theorem 2.1: each "is a character on `𝔄^G`".

## 4. Results

### 4.1 Three small lemmas

**Lemma S (characters take spectral values on end numbers).** Let `χ` be a character of `𝔄₁^G` and `ℓ=(X,Y)` a coarse link. Then `χ(p_{ℓ,X})∈P_{m₁}`; in particular it is an integer.

*Proof.* In the finite algebra of the link factor, `p_{ℓ,X}=Σ_{q∈P_{m₁}} q E_q` with `E_q=[p_{ℓ,X}=q]` its spectral projections. Each `E_q` is a polynomial in `p_{ℓ,X}`, so it lies in `𝔄₁^G`, and `Σ_q E_q=1`, `E_qE_{q'}=δ_{qq'}E_q`. Then `χ(E_q)^2=χ(E_q)`, so `χ(E_q)∈{0,1}`; `Σ_qχ(E_q)=χ(1)=1`, so exactly one `q₀` has `χ(E_{q₀})=1`. Hence `χ(p_{ℓ,X})=Σ_q qχ(E_q)=q₀`. □

**Lemma P0 (the locked characters are invariant under every fine lift).** Let `χ₀` be one of the four locked characters of section 3 item 7. Let `g=γ∘β_h`, where `β_h` is a fine cell lift of the form in section 3 item 4 (any signs `d=±1`, any constant phase) and `γ` is the identity, a global phase automorphism `Ad(e^{iθN})` or the global parity automorphism `Ad((−1)^N)`. Then `χ₀(g(a))=χ₀(a)` for every `a∈𝔄^G` with `g(a)∈𝔄^G`.

*Proof.* `VC1_5.md` Theorems 4.2 and 5.5 state that the witnesses `ψ∘E` "satisfy (i)–(iii)", and item (iii) of its section 1 item 5 is "invariance under all the stated cell lifts". To cover every sign choice and `γ`, here is the direct argument for U. Fix a finite region `R`. The lift `β_h` sends each matter mode `c_{x,j}` to `±c_{hx,j}` (times a constant phase) and each rishon mode `r^{ℓ,z}_j` to `r^{hℓ,hz}_j`. So on `𝔄(R)` it is implemented by the unitary `H_R→H_{hR}` that sends each occupation-basis vector to a phase times the image configuration. The locked vector has empty (or full) matter and, on every link, the set `{1,…,k}` at both ends. Its image configuration has the same matter and, on every image link, `{1,…,k}` at both ends, whichever end goes where. So `ψ∘β_h=ψ` on `𝔄(R)`, hence on `𝔄`. `γ` is implemented by `e^{iθN}` or `(−1)^N`, of which the locked vector is an eigenvector; so `ψ∘γ=ψ`. Finally, for `b∈𝔄^G` the gauge average fixes `b`, so `χ₀(b)=ψ(E(b))=ψ(b)`. Apply this to `b=a` and to `b=g(a)`: `χ₀(g(a))=ψ(γ(β_h(a)))=ψ(a)=χ₀(a)`. For O, `VC1_5.md` Theorem 4.2's proof: "Lifts permute the site vacua or full vectors and the link vacua or full vectors up to phases, including under end exchange"; the same steps apply. □

**Lemma R (a rotation about a coarse cell centre that exchanges the ends of a link).** Fix a coarse cell `u`. Let `X=2u`, `Y=2u+e₁`, `ℓ=(X,Y)`, and define `ρ(2u+(x,y,z))=2u+(1−x,z,y)` on `Z³`. Then `ρ` is a proper cubic rotation by `π` about the cell centre `c_u`, and it maps `ℓ` to itself with `ρ(X)=Y`, `ρ(Y)=X`. Its coarse lift sends `p_{ℓ,X}` to `p_{ℓ,Y}`.

*Proof.* The linear part is `M=((−1,0,0),(0,0,1),(0,1,0))`, a signed permutation matrix with `det M=(−1)·(0·0−1·1)=1`; so `ρ` is a proper cubic rotation, and it maps lattice points to lattice points and nearest-neighbour links to links. `M²=1`, so `ρ²=id`: a rotation by `π`. `ρ(c_u)=2u+(1−1/2,1/2,1/2)=c_u`. `ρ(X)=2u+(1,0,0)=Y` and `ρ(Y)=2u+(0,0,0)=X`. The coarse lift (section 3 item 4) sends `r^{ℓ,X}_j` to `r^{ρℓ,ρX}_j=r^{ℓ,Y}_j`, so it sends `p_{ℓ,X}=Σ_jr^{ℓ,X†}_jr^{ℓ,X}_j` to `p_{ℓ,Y}`. □

`VC1_5.md` Theorem 2.2 already proves that every link has an end-exchanging reversal in the cell group; Lemma R picks one that is literally a rotation about a coarse cell centre, so (INV-2) applies to it with no composition of lifts.

### 4.2 Theorem P: odd coarse registers are excluded by covariance

**Theorem P.** Let `m₁` be odd. Let the fine law be `L5-U[m]` with `m` even, or `L5-O[S_+]`. Let `L≥1`. There is no unital `*`-homomorphism `Φ:𝔄₁^G[L5-U[m₁]]→𝔄^G` with `Φ∘β¹_ρ=g∘Φ` for some fine lift `g` (section 3 item 4), where `ρ` is the rotation of Lemma R.

*Proof.* Let `χ₀` be a locked character of the fine law. Put `χ₁=χ₀∘Φ`. It is a `*`-homomorphism to `ℂ`, and `χ₁(1)=χ₀(Φ(1))=χ₀(1)=1`, so it is a character of `𝔄₁^G`. By (INV-2) `g(Φ(b))=Φ(β¹_ρ(b))∈𝔄^G` for `b∈𝔄₁^G`, so Lemma P0 applies to `a=Φ(b)`. So
\[
\chi_1\circ\beta^1_\rho=\chi_0\circ\Phi\circ\beta^1_\rho=\chi_0\circ g\circ\Phi=\chi_0\circ\Phi=\chi_1 .
\]
By Lemma R, `χ₁(p_{ℓ,Y})=χ₁(β¹_ρ(p_{ℓ,X}))=χ₁(p_{ℓ,X})`. Since `p_{ℓ,X}+p_{ℓ,Y}=m₁·1`, `2χ₁(p_{ℓ,X})=m₁`. By Lemma S, `χ₁(p_{ℓ,X})` is an integer. So `m₁` is even, a contradiction. □

**Corollary P1.** For every even `m`, every odd `m₁` and every `L≥1`, K-INV(m, m₁, L) is false. For every odd `m₁` and every `L≥1`, K-INV(O; m₁, L) is false.

*Proof.* A K-INV map satisfies (INV-1) and (INV-2); (INV-2) includes `ρ`, a proper cubic rotation about a coarse cell centre. Theorem P excludes it. □

**Corollary P2 (the reduction now needs an even coarse register).** For a locked U fine witness, `m` even, with its base tick, the target ZM1-I1[INV] with coarse `m₁` holds exactly when K-INV(m, m₁, L) holds for some **even** `m₁∈{2,4,6,8}` and `L≥2`. For the locked O fine witnesses with a coarse `L5-U` law, the same holds with K-INV(O; m₁, L), `m₁` even. With an odd coarse `m₁`, ZM1-I1[INV] has no instance on these fine laws, for any fine state, update or comparison class.

*Proof.* `ZM1INV.md` Theorem 2.3 with R1 and R2 gives the equivalence for every `m₁`; Corollary P1 removes the odd ones. The last sentence: Theorem 2.3 says "Any instance of the target implies its kinematic map conditions, for every fine state and update", and Theorem P excludes those conditions with odd `m₁` whatever the state, update or comparison class. □

**Remarks.**
- *What Theorem P uses.* Only unitality, multiplicativity and covariance under the one rotation `ρ`. It uses no injectivity, no locality, no translation and no value of `L`. Unitality is not an extra assumption in practice: `GB1Z2L5.md` Theorem 6 shows that a nonzero map with uniform exponential locality and a separating block map "is unital, even if unitality is not assumed".
- *The phase or parity allowed in (Z-b).* Lemma P0 includes it, so "up to a global phase or global parity" changes nothing.
- *Translations alone give nothing.* `ZM1INV.md` R1 constructs, for odd `m₁`, a coarse character that "is invariant under cell translations" and "is not reversal invariant". So a translation-only reading of "cell covariance" would leave Theorem P empty. The theorem rests on the rotations in (Z-b) and in pass 1's (INV-2).
- *R1's open clause.* R1's consequence paragraph says: "If a later reading also demanded cell-lift invariance of `ω₁`, (c) would not suffice and the odd-`m₁` case would reopen." No such reading is needed for K-INV: (INV-2) itself makes `χ₀∘Φ` invariant under `β¹_ρ`. The odd coarse character exists; it cannot be of the form `χ₀∘Φ`.
- *A coarse action other than the lift.* For `m₁=5` the rishon particle-hole map sends `Λ⁵ℂ¹⁰` to itself and `p_{ℓ,X}` to `5−p_{ℓ,X}`. If some reading let the coarse rotation act through `β¹_ρ` composed with it, the composite would fix `p_{ℓ,X}` and the proof would give nothing. (Z-b) names the rotation, whose coarse action is the coarse law's lift; this file reads it so and adopts nothing. Likewise on the fine side: (Z-b) cites `LW1.md` A2 and `MT1.md` Theorem 1 for the lifts, which are lattice symmetries with sign lifts. If a reading let a fine lift include an internal symmetry that moves the locked characters (for example an empty-full particle-hole map on `L5-O`), Theorem P would need a fine character invariant under that lift; this file does not treat that reading.
- *Physical reading.* With `E_ℓ=p_{ℓ,X}−m₁/2`, an odd coarse register is a half-integer electric link, `E_ℓ∈Z+1/2`, and the end-exchanging rotation sends `E_ℓ` to `−E_ℓ`. A character invariant under it would need `E_ℓ=0`. The face-total split of the gauge-register consolidation note (section 1) shows the same arithmetic from the other side: totals of integer fine fluxes are integers. Theorem P does not assume any flux rule; it uses only the character.
- *Odd fine `m`.* An odd fine law has no character invariant under a fine end-exchanging reversal: the proof of Theorem P with `Φ=id` would give `p=m/2`. So Theorem P's route says nothing when the fine `m` is odd. K-INV as stated has even `m`.

### 4.3 Attack A on even coarse registers: covariant characters (Proposition T)

The natural continuation of Theorem P to even `m₁` is: find a fine character, invariant under fine lifts, whose pull-back no covariant coarse character can match. It fails at this step.

**Proposition T (the constant locked map).** Let `m₁` be even and let `χ₁` be the coarse locked character (section 3 item 7, on the coarse lattice, empty matter). Define `Φ_T(a)=χ₁(a)·1` for `a∈𝔄₁^G`. For every fine law (`L5-U[m]` with any `m`, or `L5-O[S_+]`) and every `L≥1`, `Φ_T` is a unital `*`-homomorphism `𝔄₁^G→𝔄^G` that satisfies (INV-2) for every coarse cell symmetry with every fine lift, and (INV-3) with zero error. It is not injective.

*Proof.* `χ₁` is a character (`ZM1INV.md` Theorem 2.1 applied to the coarse law), so `Φ_T` is a unital `*`-homomorphism into the scalars, which lie in `𝔄^G`. Lemma P0 applied to the coarse law gives `χ₁∘β¹_{g₁}=χ₁` for every coarse cell lift. Every fine automorphism `g` fixes scalars. So `Φ_T(β¹_{g₁}a)=χ₁(a)1=g(Φ_T(a))`. Scalars lie in every `𝔄(N_R)`, so (INV-3) holds with zero error. The kernel contains `1−[p_{ℓ,X}=m₁/2]`, which is nonzero because `P_{m₁}` has at least two elements. □

**Failing step of Attack A.** For even `m₁` the coarse locked character is invariant under every coarse cell lift. So unitality, multiplicativity, covariance and locality together are consistent for even `m₁`. Any refutation of K-INV with even `m₁` must use injectivity. The character obstruction of Theorem P is specific to odd `m₁`.

### 4.4 Attack B: a good sector completed by a character (Lemma NGF)

`ZM1INV.md` Theorem 3.4 gives an exact coarse link on the good sector of one path and says: "Extending this local good-sector action by zero is not unital; an infinite product of sector projections is not a quasi-local projection." The natural repair is to complete a good-sector map by a coarse character on the complement: `Φ(a)=ρ(a)+χ(a)(1−P_g)`, with `ρ` a `*`-homomorphism into the corner of a projection `P_g` and `χ` a coarse character. This is a unital `*`-homomorphism whenever `P_g∈𝔄^G`. It fails at the next lemma, for every choice of `P_g≠1` in `𝔄^G`, not only for infinite products of path projections.

**Lemma NGF (no character on a defect projection).** Let `Φ` satisfy (INV-1) and (INV-3). Let `E∈𝔄^G` be a nonzero projection and `P∈𝔄₁^G` a projection with `P∉{0,1}`, supported in a coarse ball of radius `R₀`. Then there is `r_*` such that `Φ(τ_βP)E∉{0,E}` for every coarse cell translation `β` with `|β|_∞≥r_*`. Here `τ_β` is the coarse translation automorphism. In particular there is no character `χ` of `𝔄₁^G` with `Φ(a)E=χ(a)E` for all `a`.

*Proof.* Fix `δ=1/10`. `E` is quasi-local and even (`GB1Z2L5.md` Theorem 6: "Every invariant element is even under matter parity"), so there are a finite fine region `R_E` and an even `e∈𝔄(R_E)` with `‖E−e‖≤δ` (take any approximant, then its even part `(e+θ(e))/2`; the parity automorphism `θ` fixes `E`, preserves `𝔄(R_E)` and is isometric). Choose `R` with `C_{R₀}e^{-R/ξ}≤δ`. The translate `τ_βP` is supported in the translated ball of the same radius `R₀`, and the constants of (INV-3) depend only on `R₀`. So `Φ(τ_βP)` is within `δ` of an element of `𝔄(N_R(β))`, where `N_R(β)` is the fine region within `R` of the blocks of the translated ball; take its even part `f_β`, again within `δ` because `Φ(τ_βP)` is even. For `|β|_∞` large, `N_R(β)` shares no factor with `R_E`. (No covariance is used.)

Suppose `Φ(τ_βP)E=cE` with `c∈{0,1}`. Then
\[
(f_\beta-c)e=(f_\beta-\Phi(\tau_\beta P))e+(\Phi(\tau_\beta P)-c)(e-E),
\]
because `(Φ(τ_βP)−c)E=0`. Here `‖e‖≤1+δ` and `‖Φ(τ_βP)−c‖≤1`, so `‖(f_β−c)e‖≤δ(1+δ)+δ<3δ`. Even elements on disjoint finite regions act as `A⊗1` and `1⊗B` in a Jordan-Wigner order (as in `ZM1INV.md` R6), so `‖(f_β−c)e‖=‖f_β−c‖‖e‖≥‖f_β−c‖(1−δ)`. Hence `‖f_β−c‖<3δ/(1−δ)` and `‖Φ(τ_βP)−c‖<δ+3δ/(1−δ)<1`. A projection within distance `<1` of `0` is `0`, and one within `<1` of `1` is `1`. So `Φ(τ_βP)=c·1=Φ(c·1)`, and injectivity gives `τ_βP=c·1`, hence `P=c·1`, a contradiction. □

**Corollary NGF1.** No K-INV map has the form `Φ(a)=ρ(a)+χ(a)(1−P_g)` with `P_g∈𝔄^G` a projection, `P_g≠1`, `ρ` a `*`-homomorphism with `ρ(1)=P_g`, and `χ` a coarse character.

*Proof.* `E=1−P_g≠0` and `ρ(a)E=ρ(a)P_gE=0`, so `Φ(a)E=χ(a)E`. Lemma NGF. □

**Failing step of Attack B (see also 4.5).** Lemma NGF. Every nonzero invariant projection, however it is localized, sees far-away coarse projections non-trivially. So a K-INV map is unital on every local sector separately: defects must be handled by a local modification of the map near each defect, never by one character on a defect projection. This is the exact content of GAP-GLOBAL ("a unital, globally compatible extension ... to defect sectors") that a construction must meet.

### 4.5 Attack C: decimation equivariant for the coarse charge (Theorem J)

The natural way to build `Φ` is to restrict a map of the full algebras that carries each coarse site's gauge action to a representative fine site. `ZM1INV.md` Theorem 3.3 refutes the link-wise version, which sends each coarse link factor into one fine path and matches end numbers. The class below drops the link-wise structure and asks only for the coarse `U(1)` charge.

**Class J.** A unital `*`-homomorphism `Ψ:𝔄₁→𝔄` of the full algebras, an injective map `X↦x_X` from coarse to fine sites with `x_{X+2b}=x_X+2Lb` for coarse cell translations `b`, and for each fine site `x` a self-adjoint `Q^F_x` in the algebra of the star of `x`, even, with finite spectrum, translation covariant (for example `Q_x` on U, or a Cartan generator of `Spin(10)_x` on O). Require, for every coarse `X` and real `θ`,
\[
\Psi\circ\mathrm{Ad}(e^{i\theta Q^{(1)}_X})=\mathrm{Ad}(e^{i\theta Q^F_{x_X}})\circ\Psi .\tag{J}
\]
A K-INV map is *of class J* if it is `Ψ|_{𝔄₁^G}` for such a `Ψ`.

**Theorem J.** If (J) holds at two coarse neighbours `X,Y`, then `x_X` and `x_Y` are fine neighbours. Consequently class J contains no map with `L≥2`, and no K-INV map with `L≥2` is of class J. This holds for every `m`, every `m₁` and for the O fine law.

*Proof.* Write `x=x_X`, `y=x_Y`, `Q¹_X=Q^{(1)}_X`.

*Step 1 (corrections commute with the image).* `Q¹_X` lies in the finite algebra of its star, so `Ψ(e^{iθQ¹_X})=e^{iθΨ(Q¹_X)}`. Apply (J) at `X` to `a=Q¹_X`: `Ψ(Q¹_X)` is fixed by `Ad(e^{iθQ^F_x})` for all `θ`, so it commutes with `Q^F_x` (differentiate at `θ=0`). Put `k_X=Ψ(Q¹_X)−Q^F_x`. Then `e^{iθk_X}=e^{−iθQ^F_x}e^{iθΨ(Q¹_X)}`, and (J) says this commutes with every `Ψ(a)`; differentiating at `θ=0`, `k_X∈Ψ(𝔄₁)'`. The same at `Y`. Further `[Ψ(Q¹_X),Q^F_y]=0` by (J) at `Y` applied to `a=Q¹_X` (which commutes with `Q¹_Y`), `[Q^F_x,Q^F_y]=0` (star generators at distinct sites commute), and `[Ψ(Q¹_X),Ψ(Q¹_Y)]=0`. So `Ψ(Q¹_X),Ψ(Q¹_Y),k_X,k_Y` commute pairwise. All four have finite spectra (`k_X` is a difference of two commuting elements with finite spectra).

*Step 2 (a matrix block and its commutant).* Let `F⊂𝔄₁` be the algebra of a finite coarse region containing the stars of `X` and `Y`. It is a full matrix algebra `M_n` (Jordan-Wigner, as in `ZM1I1A.md` Theorem 1's proof), and `Ψ` is injective on it (a nonzero homomorphism of `M_n` is injective). Let `e_{ij}=Ψ(E_{ij})` be the images of matrix units. *Claim:* if `0≠π∈Ψ(F)` and `0≠κ∈Ψ(F)'`, then `πκ≠0`. Indeed, write `π=Σπ_{ij}e_{ij}` with `π_{i₀j₀}≠0`; then `e_{1i₀}πκe_{j₀1}=π_{i₀j₀}e_{11}κ`. If `e_{11}κ=0`, then `κ=Σ_ie_{i1}e_{11}e_{1i}κ=Σ_ie_{i1}e_{11}κe_{1i}=0`. So `πκ≠0`.

*Step 3 (fine joint spectrum as a difference set).* Let `J₁` be the set of pairs `q` with `E¹_q:=[Q¹_X=q₁][Q¹_Y=q₂]≠0` in `F`, and `K` the set of pairs `κ` with `K_κ:=[k_X=κ₁][k_Y=κ₂]≠0`. Each `Ψ(E¹_q)K_κ` is a projection; they are pairwise orthogonal and sum to `1`; `Q^F_x=Σ(q₁−κ₁)Ψ(E¹_q)K_κ` and `Q^F_y=Σ(q₂−κ₂)Ψ(E¹_q)K_κ`. By injectivity `Ψ(E¹_q)≠0` for `q∈J₁`, and `K_κ∈Ψ(F)'`, so by the claim `Ψ(E¹_q)K_κ≠0` for all `q∈J₁`, `κ∈K`. Hence the set of pairs `(a,b)` with `[Q^F_x=a][Q^F_y=b]≠0` is exactly `J₁−K={q−κ}`.

*Step 4 (the coarse pair has no componentwise minimum).* Let `s=min P_{m₁}=max(0,m₁−5)`. The least value of `Q¹_X` is `6s` (empty matter, all six ends at `s`), and it occurs in `J₁`; likewise for `Q¹_Y`. But `(6s,6s)∉J₁`: `Q¹_X=6s` forces `p_{ℓ,X}=s` on the shared link `ℓ`, so `p_{ℓ,Y}=m₁−s` and `Q¹_Y≥m₁−s+5s=m₁+4s>6s`, because `m₁−2s=min(m₁,10−m₁)≥1`. So no element of `J₁` is componentwise below all others.

*Step 5 (non-adjacent representatives are impossible).* Suppose `x≠y` are not neighbours. Their stars share no factor, and `Q^F_x,Q^F_y` are even, so in a Jordan-Wigner order their spectral projections act as `A⊗1` and `1⊗B`; every product `[Q^F_x=a][Q^F_y=b]` with `a,b` in the spectra is nonzero. So the fine set of Step 3 is a product `σ_x×σ_y` and contains its componentwise minimum `(a₀,b₀)`. Write `(a₀,b₀)=q^*−κ^*` with `q^*∈J₁`, `κ^*∈K`. For every `q∈J₁`, `q−κ^*` lies in `σ_x×σ_y`, so `q−κ^*≥(a₀,b₀)=q^*−κ^*`, that is `q≥q^*`. This contradicts Step 4. `x=y` is excluded by injectivity of `X↦x_X`. So `x` and `y` are neighbours.

*Step 6 (density).* `ZM1INV.md` Theorem 3.3, second part: "Cell-translation covariance gives `x_{X+2e_i}=x_X+2Le_i`, whereas two coarse edges give a sum of two fine unit steps. This is impossible for `L≥2`." Steps 1-5 make `x_X,x_{X+e_i}` and `x_{X+e_i},x_{X+2e_i}` neighbours. □

**Failing step of Attack C.** Step 5: the end charges of a coarse link are anti-correlated through the link (Step 4), while charges at two non-adjacent fine sites are independent; a relative-commutant correction cannot turn a product set into a set without a corner.

*Relation to prior work.* Theorem J extends `ZM1INV.md` Theorem 3.3 from link-wise maps with end-number equivariance to arbitrary unital maps with site-charge equivariance; the new step is Step 2-3 (one matrix block and its commutant) in place of Theorem 3.3's factor-by-factor splitting. Astra's spectral-endpoint argument (`ZM1I1A_OWNER_CHECK.md` lines 13-32, one model's argument, not refereed) shows that G1-eq at all diagonal generators forces (G1) by equal endpoints at one site. Theorem J needs only the `U(1)` part and no equality of endpoints, and it uses two neighbouring sites. Both are statements about full-algebra maps; neither constrains a map defined only on `𝔄₁^G`.

## 5. Do the character and the abelian structure help?

**The character: yes, through covariance.** `ZM1INV.md` R5 already composed a K-INV map with the fine character: "For these fine laws every K-INV map makes `ω₀∘Φ` a character of `𝔄₁^G`. Such characters exist for every `m₁` (Theorem 2.1, R1) and for O, so R5 gives no obstruction to K-INV." The step R5 did not take is to carry the fine character's symmetry along. The fine locked character is invariant under every fine cell lift (Lemma P0), so by (INV-2) its pull-back is invariant under every coarse cell lift. Odd coarse registers have characters, but none invariant under an end-exchanging rotation (Theorem P). That is the obstruction. For even `m₁` the same step yields a necessary condition and no contradiction:

**Corollary P4 (balanced ends in the pulled-back character).** Let `m₁` be even and let `Φ` satisfy (INV-1)-(INV-2). For every coarse link `ℓ=(X,Y)` and each locked fine character `χ₀`, `χ₀(Φ([p_{ℓ,X}=m₁/2]))=1`.

*Proof.* `VC1_5.md` Theorem 2.2, applied to the coarse law, gives an end-exchanging reversal of `ℓ` in the coarse cell group: "Every link has an end-exchanging reversal in `G`". It is a composition of coarse cell translations and rotations about coarse cell centres; (INV-2) holds for each factor, hence for the composition, and each coarse lift carries end numbers to the image end. The proof of Theorem P then gives `χ₀∘Φ(p_{ℓ,X})=m₁/2`, and Lemma S gives `χ₀∘Φ([p_{ℓ,X}=m₁/2])=1`. □

So in the fine locked vacuum every image of a coarse balanced-end projection is sharp with value one. Proposition T shows this is all the character gives for even `m₁`.

**The abelian structure beyond the character: no.** `GB1Z2L5.md` Theorem 5: "`A^G` contains no invertible `a,b` satisfying `ab=λba` for scalar `λ≠1`." `𝔄₁^G` has a character too (`GB1Z2L5.md` Theorem 2 for the coarse law), so it has no such pair either, and the constraint "Φ maps such pairs to such pairs" is empty. The same holds for the non-unital `M₂` corners of `GB1Z2L5.md` Theorem 8: both algebras have them, and a coarse corner projection whose corner contains a unital `M₂` must map to a projection on which every fine character vanishes, which is consistent. Any argument that uses only "the fine algebra has a character" and no covariance gives nothing: for every `m` and `m₁` the constant map `a↦χ(a)1` through a coarse character `χ` is a unital `*`-homomorphism with exact locality. With covariance, the character gives exactly Theorem P for odd `m₁`, and only Corollary P4 for even `m₁` (Proposition T).

**Without covariance and locality.** `𝔄^G` and `𝔄₁^G` are AF algebras. Whether some unital injective `*`-homomorphism exists between them, with no covariance and no locality, is a question about their ordered `K₀` groups (Elliott's classification, NOT VERIFIED here; Aaserud-Evans arXiv:1803.03227 abstract for the `K`-theory of related AF algebras). It is not pursued: Theorem P shows covariance is where the odd case fails, and Lemma NGF shows locality is where the obvious completions fail.

## 6. The open lemma for even coarse registers

**K-INV-E (open).** For some even `m` (or the fine law `L5-O[S_+]`), some even `m₁∈{2,4,6,8}` and some `L≥2`, there is `Φ:𝔄₁^G[L5-U[m₁]]→𝔄^G` with (INV-1), (INV-2) and (INV-3). By Corollary P2 this is exactly what ZM1-I1[INV] needs in the locked even-`m` U and locked O vacua with the base tick. K-INV-O (an O coarse law) is a separate open variant; Theorem P does not touch it, because O end parities are equal at the two ends of a link, not complementary.

**Three new attacks, each failing at a proved step.**
- **A. Covariant characters.** Fails at Proposition T: for even `m₁` the constant map through the coarse locked character meets (INV-2), (INV-3), unitality and multiplicativity. Injectivity is the only condition it misses.
- **B. Good sector completed by a character.** Fails at Lemma NGF and Corollary NGF1: no K-INV map acts by a character on any nonzero invariant projection.
- **C. Decimation equivariant for the coarse charge.** Fails at Theorem J, Step 5: representatives of neighbours must be fine neighbours, so `L=1`.

They are distinct: A uses the character and covariance, B uses locality and injectivity, C uses a joint spectrum and density. The three earlier attacks on file (neutral matrix registers, `ZM1INV.md` Theorem 3.2 and R5; end-equivariant link decimation, Theorem 3.3; good-sector decimation with representative end data, Theorem 3.5) fail at their own steps; A, B and C each widen one of them. Under the lane rule K-INV-E is carried as a lemma on which these three attacks failed. That is not a proof that it fails.

**Constraints every K-INV-E map meets (proved).**
1. In each locked fine character, every coarse balanced-end projection maps to a sharp projection with value one (Corollary P4).
2. Every nonzero invariant projection sees far-away coarse projections non-trivially (Lemma NGF): defects must be absorbed locally.
3. Incompatible end-number projections of one coarse link cannot both be approximated to better than `1/4` on disjoint fine regions (`ZM1INV.md` R6).
4. The map is not the restriction of a full-algebra map that carries the coarse `U(1)` charges to representative fine sites (Theorem J).
5. Injectivity carries the content (Proposition T).

**A coarse-side tool for local defects.** Constraint 2 says a construction must modify itself near each fine defect. On the coarse side, central projections give homomorphic, local ways to freeze a site.

**Lemma CF (central freezing).** Let `X` be a coarse site, `t=min(5,m₁)`, and `Π_X` the spectral projection of the coarse charge `Q¹_X` for its largest value `5+6t`. Then `Π_X` is central in `𝔄₁^G`, the map `a↦Π_Xa` is a `*`-homomorphism of `𝔄₁^G` onto the corner `Π_X𝔄₁^G`, local in the sense that `Π_Xa` is supported in the support of `a` together with the star of `X`, and on the range of `Π_X` the matter at `X` is full and every end number at `X` equals `t`. For neighbours `X,Y`, `Π_XΠ_Y=0`.

*Proof.* `Q¹_X` generates the centre `U(1)` of `U(5)_X`, so every invariant element commutes with it and hence with its spectral projections, and `Q¹_X` is itself invariant; so `Π_X` is a central projection of `𝔄₁^G` and `a↦Π_Xa` is a `*`-homomorphism onto the corner. `Q¹_X=N_X+Σ_{ℓ∋X}p_{ℓ,X}` with `N_X≤5` and `p_{ℓ,X}≤t`, so `Q¹_X=5+6t` forces `N_X=5` and every `p_{ℓ,X}=t`. For a shared link, `p_{ℓ,X}=p_{ℓ,Y}=t` would need `2t=m₁`, false since `t>m₁/2` for `1≤m₁≤9`. □

In the corner of `Π_X` every link at `X` is frozen, with `m₁−t` rishons at the far end. A construction that freezes a coarse site wherever its fine block is defective would use such corners; Lemma CF shows the freezing itself is local and homomorphic. Whether the fine side can supply, in every fine configuration, a frozen-site pattern with these boundary data and a faithful realization elsewhere is K-INV-E itself; no such pattern is constructed here.

## 7. Readings

No reading, specification or definition is proposed or adopted. K-INV, K-INV(O; m₁, L), K-INV-O and K-INV-E are the open statements of `ZM1INV.md`, with K-INV-E their even-`m₁` part. Class J (section 4.5) is a class of maps that an attack tests, not a reading of the framework.

One dependence is recorded so the owner can see it. Theorem P uses the rotation part of cell covariance, with the coarse rotation acting by the coarse law's own lift. Call the opposite reading **R-TR**: "cell covariance" means coarse cell translations only. R-TR is not proposed. Under it Theorem P is empty, because the odd coarse character of `ZM1INV.md` R1 is translation invariant. Four tests, as a pass-1 assessment only: (1) P, it states no target; (2) P, it is closed; (3) C, it would re-admit odd coarse registers, and LZ1 and ST1 need the cubic rotations to act at the coarse scale, so the question would move downstream; (4) P, it removes structure rather than adding it. A second variant, letting a coarse rotation act through its lift composed with the rishon particle-hole map (possible only at `m₁=5`), would also evade Theorem P; it adds a map that (Z-b)'s reasons do not need (test 4 F) and is not proposed.

## 8. Check

`[check]` One scratch computation, `/tmp/toe-KINV/check_kinv.py`, run with `python3 -I` after `memory_pressure` reported 52 percent free; under one second, a few MB, no matrices. It confirms two finite facts that sections 4.1 and 4.5 prove by hand, and it proves nothing. (1) The map `(x,y,z)↦(1−x,z,y)` has determinant 1, maps the cube `{0,1}³` to itself, is an involution, and exchanges `(0,0,0)` and `(1,0,0)` (Lemma R). (2) For each `m₁=1,…,9`, the set of values of `(Q¹_X,Q¹_Y)` for two coarse neighbours, enumerated through matter numbers, the shared end number and the sums of the other five end numbers at each site, has least coordinates `(6s,6s)` and does not contain that corner (Theorem J, Step 4); also `2t>m₁` (Lemma CF). Output (`/tmp/toe-KINV/out.txt`):

```
det 1 maps cell to itself True involution True swaps X,Y True fixes centre True
m1 1 minQX 0 minQY 0 6s 0 corner in J1 False m1/2 in P False 2t>m1 True
m1 2 minQX 0 minQY 0 6s 0 corner in J1 False m1/2 in P True 2t>m1 True
m1 3 minQX 0 minQY 0 6s 0 corner in J1 False m1/2 in P False 2t>m1 True
m1 4 minQX 0 minQY 0 6s 0 corner in J1 False m1/2 in P True 2t>m1 True
m1 5 minQX 0 minQY 0 6s 0 corner in J1 False m1/2 in P False 2t>m1 True
m1 6 minQX 6 minQY 6 6s 6 corner in J1 False m1/2 in P True 2t>m1 True
m1 7 minQX 12 minQY 12 6s 12 corner in J1 False m1/2 in P False 2t>m1 True
m1 8 minQX 18 minQY 18 6s 18 corner in J1 False m1/2 in P True 2t>m1 True
m1 9 minQX 24 minQY 24 6s 24 corner in J1 False m1/2 in P False 2t>m1 True
```

The column "m1/2 in P" is the integrality fact behind Theorem P and Corollary P4: `m₁/2` is an end-number value exactly when `m₁` is even.

## FINISH

**Proved (pass 1, author-side, unrefereed).**
- Lemma S: a character of `𝔄₁^G` gives every end number a value in `P_{m₁}`. Lemma P0: the four locked fine characters are invariant under every fine cell lift, with any signs, and under global phase and parity. Lemma R: the rotation `(x,y,z)↦(1−x,z,y)` about a coarse cell centre exchanges the ends of a coarse link inside the cell.
- **Theorem P.** For odd `m₁`, no unital `*`-homomorphism `𝔄₁^G[L5-U[m₁]]→𝔄^G` is covariant under that rotation, when the fine law is `L5-U[m]` with `m` even or `L5-O[S_+]`. No injectivity, no locality and no value of `L` is used.
- Corollary P1: K-INV(m, m₁, L) is false for every even `m`, odd `m₁` and `L`; K-INV(O; m₁, L) is false for every odd `m₁` and `L`. Corollary P2: in the locked even-`m` U and locked O vacua, ZM1-I1[INV] holds exactly when K-INV holds for some even `m₁` and `L≥2`; with odd `m₁` it has no instance for any fine state, update or comparison class. Corollary P4: for even `m₁`, every map with (INV-1)-(INV-2) sends each coarse balanced-end projection to a projection of value one in each locked fine character.
- Proposition T: for even `m₁` the constant map through the coarse locked character meets every K-INV condition except injectivity.
- Lemma NGF and Corollary NGF1: under (INV-1) and (INV-3), every nonzero invariant fine projection sees far-away coarse projections non-trivially; no K-INV map is a good-sector map completed by a character on a defect projection in `𝔄^G`.
- Theorem J: a unital full-algebra map that carries the coarse `U(1)` charges to representative fine sites (any star generator with finite spectrum, U or O fine law) makes representatives of neighbours fine neighbours; with covariant representatives, `L=1`.
- Lemma CF: the top spectral projection of a coarse charge is central and freezes its site; cutting by it is a local `*`-homomorphism.

**Counterexamples.** Theorem P refutes K-INV(m, m₁, L) for each even `m` and odd `m₁`, and K-INV(O; m₁, L) for each odd `m₁`: no such map exists. This settles the odd-`m₁` half of `ZM1INV.md`'s open items "K-INV(m, m₁, L), m even, any m₁" and "K-INV(O; m₁, L)". No counterexample to K-INV-E or K-INV-O.

**Open by name.**
- **K-INV-E**: K-INV(m, m₁, L) with `m, m₁` even, and K-INV(O; m₁, L) with `m₁` even, `L≥2`. Three new attacks failed, each at a proved step: **A, covariant characters** (Proposition T); **B, good sector completed by a character** (Lemma NGF); **C, decimation equivariant for the coarse charge** (Theorem J, Step 5). The three earlier failed attacks stand: neutral matrix registers, end-equivariant link decimation, good-sector decimation with representative end data.
- **K-INV-O** (O coarse law). Theorem P does not reach it.
- K-INV with an odd fine `m` (outside `ZM1INV.md`'s statement); Theorem P's route gives nothing there.
- Inherited, unchanged: ZM1-I1[INV] in non-character vacua; the good-sector extension (GAP-GLOBAL), now constrained by Lemma NGF; fine-side test non-triviality; VC1 and its vacuum choice; ICE-T and ICE-U(R4); LZ1-i[ZM1a]; ZM1-G; Y1; H-BLOCK; R-CS with R-CS^str; MT1-S; ZM1(a)1 and full ZM1.

**What changes downstream.**
- ZM1 and ZM1-I1[INV]: on the fine laws `L5-U[m]` with `m` even and `L5-O[S_+]`, the coarse register must be even, `m₁∈{2,4,6,8}`. Theorem R's "for some `m₁∈{1,…,9}`" becomes "for some even `m₁`". `ZM1INV.md`'s open item "Coarse-state symmetry" no longer matters for K-INV with odd `m₁`, because the map itself cannot exist.
- K-INV lanes: work K-INV-E. A construction must absorb defects locally (Lemma NGF), must not be a restriction of a charge-equivariant decimation (Theorem J), and must make the pulled-back locked character balanced on every coarse link (Corollary P4). Lemma CF is a coarse-side tool for local freezing.
- Owner: Theorem P rests on the rotation part of (Z-b). The translation-only reading R-TR (section 7, not proposed) would make it empty.
- Charged sectors and Gauss generators: unchanged; they get no zoom from this map.
- No axiom, working-set entry, reading or frozen file changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. No other file is edited.
