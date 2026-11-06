# VC1-5U-odd: the odd-m vacuum of L5-U

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (VC1_5U_ODD_REFEREE.md); the referee's edits E1-E11 are applied, with the prior-work credits of `prior/VC1_5U_ODD.md`.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The item enters `VC1_5.md` as its Amendment 1. The lead (Claude Opus 5.5, laptop) checked that each of E1-E11 is in the text and that the replaced text is gone; that is a text check, not a second referee.

This is a distillation of `VC1_5U_ODD_DRAFT.md`. It is a proposed amendment to `VC1_5.md`, not the amendment itself. The statements use its frozen law and results. They establish no retained status, physical vacuum selection, or continuation of the PS-7r sea.

**Proved, conditional on the frozen inputs.** Factor states have tail-trivial number shadows. A cell-symmetric P-witness has one site isotype. For odd `m`, quasi-invariant ice measures give stationary gauge-invariant states for the base tick, with filling 0 or 5. Their invariant-algebra purity is equivalent to tail triviality. ICE-T would therefore supply P-witnesses for every odd `m`. At `m=1,9`, a P-witness at either edge filling requires ICE-T⁻. For each R4 limit point `ω`, `ω∘E` is pure on the invariant algebra exactly when its ice law is tail-trivial. The `G`-invariant deterministic transition-system construction (A1) fails: all its paths are infinite. Theorems and proofs follow.

**GAP.** Neither ICE-T nor tail triviality of an R4 limit is proved. The latter is the remaining route-3 purity question for that particular limit, not a proof or disproof of purity. The random-transition and hierarchical-factor attacks have unproved steps. A3 does not address quasi-invariance. For A2, quasi-invariance and tail triviality follow from almost-sure finiteness of all trails (referee closure RC-A2); A2 is open exactly at A2-FIN. The proposed reading P remains subject to the check-3 caveat below.

**Open by name.** VC1-5U-odd; ICE-T, ICE-T⁻, ICE-U, ICE-QI; ICE-U(R4); A2-FIN; LW1-5U-Σc-odd; P-existence with a plaquette class on both laws; the PS-7r sea continuation of VC1; VC1-i; TM1-i; LW1-5U-PS7 (owner); LW1-5-BG; LW1-5-X; GA1-P-5; LW1-5-RQ (owner). Stability, excitations and energy density of full VC1 also remain open. ICE-T⁻ is a necessary condition at the edge cases stated above, not a resolution of those cases.

**Provenance.** Pass 3 editing session: Codex gpt-6.1-terra, effort high, codex-cli 0.165.0, session `01a1b12f-dda7-77b2-84f9-27f517148204`. Pass 1: `VC1_5U_ODD_DRAFT.md`, SHA-256 `ac69babc3a7ec80800f99a6e04bab6c4e1d61e41296e59816ae658b04c989de7`. Pass 2: Codex CLI `gpt-6.1-terra`, reasoning effort high, session `01a1b0b7-13c0-7e03-8487-757a52a85659` (from the run log). Checkout HEAD `f67ed2001d825432804712fd088edc1bd709993b`. Context: `TOE_ASSEMBLY.md` §§3.4–3.5, `LW1.md`, `VC1_5.md`, `LW1_5.md`, `LZ1.md`. Source hashes: `VC1_5.md` `7461113c411eeda4c932cf71887781007bd69786095afc7dd89bbaeec83c56a8`; `LW1_5.md` `7afb7ee2a52d91cd1cab23008c53373d710d0ce66252e1e5169ba8ca6009b20e`; `LZ1.md` `8dc59d4d4894fbd4971560cd1ac42bd7938cbf51b53aca57ad3076632daae1fe`. No numerical calculation is used as proof. The pass-1 literature inventory and its verification limits are in the draft; the present argument does not rely on those literature claims except where explicitly identified below.

## Prior work in the repository

Paths beginning `docs/` are relative to the repository root; the other paths are relative to this folder. The following are the missed inputs identified in `prior/VC1_5U_ODD.md`:

- `LW1U_DRAFT.md` Remark 6.1: the earlier factor-to-tail sketch for cube CAR site Born laws. Theorem 2.2 extends this antecedent to matter and link number shadows and factor invariant restrictions, with a different proof presentation.
- `docs/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md`: frozen zero-winding configurations on every even torus. `VC1_5.md` R4 sums over the full zero-flux sector; component-restricted Monte Carlo needs a comparison. `docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md` supplies no whole-sector mixing bound. These notes are unaudited.
- `docs/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md`: a fixed-cross-section transfer construction and explicit boundary decay, a bounded test case; uniform control in cross-section is not established. Unaudited.
- `docs/COULOMB_MEASURE_SELECTION_HARD_STATIC_ICE_RULES_ADMIT_EVERY_ICE_MEASURE_POSITIVE_RULES_SELECT_THE_UNIFORM_ONE_BOUNDED_THEOREM_NOTE_2026-09-22.md`: hard finite specifications admit every ice measure. `docs/DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md`: distinguishes annihilation, ground-space selection and preparation. Neither establishes infinite-volume selection or preparation; both are unaudited.
- `VC1_5U_ODD_REFEREE.md` RC-A2 and RC-A3b: A2-FIN implies ICE-T; a summable coding-radius tail, including a finite third moment under the stated orbit assumptions, suffices for tail triviality. Neither missing hypothesis is established.
- `VC1_5U_ODD_REFEREE.md` §2.3 note 3: the conditional records and LZ1 applications do not require ICE-T; they apply to every R4 limit point under their stated readings and hypotheses.

## 1. Definitions inferred by the distiller

1. Use the quasi-local matter CAR and link algebra `A`, local gauge fixed algebra `A^gauge`, gauge average `E`, tick `α`, and cell lifts `β_g` of `VC1_5.md` §§1–2. The cell group is `G=2Z³ ⋊ O_{c0}`. Conditions (i), (ii), (iii) mean tick stationarity, local gauge invariance, and invariance under all stated cell lifts. A **P-witness** satisfies these conditions and proposed reading P: its restriction to `A^gauge` is pure. Proposed reading E means extremality among states satisfying (i)–(iii); F means that `π_ω(A)''` is a factor. No reading is adopted here. The frozen four-test assessment gives E four passes, with the qualification that E need not imply F; P passes tests 1, 2 and 4, and test 3 is conditional because P excludes half filling on this law. Proposed PS-7(h) requires the gauged vacuum itself to be half filled; it is unadopted, and this item does not supply a separate four-test assessment of it. Proposed PS-3h5 and the joint Born identification enter only the conditional record remark below; its check 3 is conditional and its other checks pass, as stated in `VC1_5.md` §1.
2. On `L5-U[m]`, `m∈{1,…,9}`, each site has matter number `N_x`, each link `ℓ=xy` has end numbers `p_{ℓ,x}+p_{ℓ,y}=m`, and `Q_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}`. Local `U(5)_x` is implemented by `Γ_x(u)`; `Γ_x(e^{iθ}I)=e^{iθQ_x}`. The gauge average and base tick have the properties in `VC1_5.md` Theorem 2.1 and `LW1_5.md` Theorem U. Angles satisfy `0≤μ<2ε<π`, `τ_E∈R`. No plaquette layer is included unless stated.
3. A **shadow** `κ_ω` is the joint Borel law of all commuting `N_x,p_{ℓ,z}`. Its compact configuration space `K_m` has `n_x∈{0,…,5}`, `max(0,m−5)≤p_{ℓ,z}≤min(5,m)`, and link sums `m`. Let `Λ_n=[−n,n]³∩Z³`. The outside σ-algebra is generated by `n_x` outside `Λ_n` and end numbers on links with no endpoint in `Λ_n`. The **tail** is the intersection of these σ-algebras. Tail-trivial means all its events have probability 0 or 1. Cylinder functional calculus and Riesz give the shadow.
4. For odd `m=2a+1`, `a∈{0,…,4}`, an **ice configuration** chooses a high end on each link, with exactly three high ends at each site. Arrows point to high ends. `Ω_ice` is its closed, compact, metrizable configuration space. `G` acts geometrically. Its tail uses arrows on links with no endpoint in `Λ_n`.
5. Given a finite link set `L` and assignments `β,β'`, the **replacement** `S_{β→β'}` changes `β` to `β'` where the result is ice. Its domain and range are clopen, and its inverse is `S_{β'→β}`. A measure is **quasi-invariant** if each replacement preserves null sets in both directions. It is **flip-invariant** if each replacement preserves measure.
6. **ICE-T** asks for a `G`-invariant, quasi-invariant, tail-trivial Borel probability measure on `Ω_ice`. **ICE-T⁻** drops quasi-invariance. **ICE-U** asks for a `G`-invariant, flip-invariant, tail-trivial measure. **ICE-QI** asks whether ICE-T⁻ implies ICE-T. ICE-U implies ICE-T, which implies ICE-T⁻. These are questions, not premises or readings proposed for adoption. The draft's four-test assessment passes all four for definitions 3–6 and for the transition systems below: they introduce fixed mathematical objects or explicit questions and do not settle a physics target by assumption.
7. A **transition system** pairs the six incident links at each site. Following the pairs partitions links into finite closed trails and bi-infinite trails. Orienting each trail consistently yields an ice configuration. A finite modification of an ice configuration changes finitely many arrows.

## 2. Constraints on P-witnesses

**Lemma 2.1 (local support and isotype).** A local `B∈A^gauge` conserves the total matter number on its matter support, is even, and commutes with even local elements of disjoint support. For every site, the `U(5)_x` isotypic projection
\[
P_\lambda(x)=d_\lambda\int_{U(5)}\overline{\chi_\lambda(u)}\,\Gamma_x(u)\,du
\]
is local and central in `A^gauge`. A state satisfying P selects exactly one isotype at each site. If it also satisfies (iii), the same isotype `λ` occurs everywhere and `Q_x=|λ|` sharply.

*Proof.* Gauge invariance gives `[Q_x,B]=0`. Sum `Q_x` over a finite set containing the support and both ends of its links. The internal link contribution is the scalar `m` per link; the outside contribution commutes with `B`. Thus `B` conserves its supported matter number and is even. Disjoint even CAR elements commute, as do the ordinary link factors.

Schur orthogonality makes the displayed integral the isotypic projection; finitely many occur on a finite star. It is invariant under conjugation by the site group, commutes with the other local groups, and commutes with every fixed observable. A pure state is sharp on central projections (`VC1_5.md` Theorem 3.1(a)). Their sum is one, so exactly one has expectation one. The lifts carry `P_λ(x)` to `P_λ(gx)` (`VC1_5.md` Theorem 2.2) and `G` is site-transitive. The central circle acts in `λ` as `e^{iθ|λ|}`. ∎

**Theorem 2.2 (shadow theorem).** For any `m`, constants and plaquette class, if `ω` on `A`, or its restriction to `A^gauge`, is a factor state, then `κ_ω` is tail-trivial.

*Proof.* Let `B` be the algebra whose GNS representation is a factor. The commuting number algebra is `C(K_m)`: all finite patterns satisfying the link constraints occur in the local Hilbert spaces. Its spectral measure `P` has scalar law `κ_ω`. If `T` is a tail event, for each `n` it is the inverse image of a Borel event in the outside coordinates. Uniqueness of spectral measures puts `P(T)` in the von Neumann algebra generated by those outside numbers. For sufficiently large `n` these even numbers commute with any chosen local element of `B`. Local invariant elements are dense in `A^gauge` by `VC1_5.md` Theorem 2.1; local elements are dense in `A`. Thus `P(T)` commutes with `π(B)`, while belonging to `π(B)''`. The factor property makes it 0 or 1. ∎

**Corollary 2.3.** If `ω` satisfies (iii) and P, its shadow is `G`-invariant, tail-trivial, and obeys `n_x+Σp_{ℓ,x}=q` at every site almost surely, for one integer `q`. If `m=1` and the filling is 0 or 5, its high-end arrow law is a `G`-invariant tail-trivial ice measure. Neither stationarity nor gauge invariance of `ω` is needed.

*Proof.* Purity gives a factor on the fixed algebra. Apply Theorem 2.2, covariance of the numbers, and `VC1_5.md` Theorem 5.3. At filling 0 or 5, boundedness makes `n_x` equal to 0 or 5 almost surely. For `m=1`, each link has one end of each number, and `q=3` or 8 forces three high ends at each site. Writing `ν` for the arrow law, by referee closure RC-T, `ν` is tail-trivial exactly when its shadow is (referee closure, VC1_5U_ODD_REFEREE.md). ∎

## 3. The ice sector

Fix odd `m=2a+1`. Put `w*=(6,…,6,3,0,…,0)`, with `a` entries 6. At the end with number `p`, occupy flavours `1,…,p`. On a link with high end `h`, the end `h` has number `a+1` and the other end has number `a`. On each link use source-end creators before target-end creators. For a finite arrow assignment `b`, write `|b⟩` for the product of these link vectors and empty matter. Link factors commute with matter and with other links. Write `H_x^j=G_x^{E_{jj}}` and `E_x^{jk}=G_x^{E_{jk}}`, `j<k`. `T↦G_x^T` is extended complex-linearly.

**Lemma 3.1 (weight space).** With all six incident links included, `N_x=0` and `H_x^j=w*_j` hold on a vector exactly when each occupation-basis component has empty matter at `x`, all six ends occupied in flavours `1,…,a`, exactly three occupied in flavour `a+1`, and none in the higher flavours. Every such component is killed by all `E_x^{jk}`, `j<k`.

*Proof.* All specified number operators are diagonal. Their eigenvalues force exactly those occupancies. Each raising term needs a higher occupied flavour and a lower unoccupied flavour, which cannot occur in an initial segment. ∎

**Lemma 3.2 (local action).** Let `B∈A^gauge` be local, with link support `L_B` and matter support `S_B`. Let `V_B` contain `S_B` and both ends of every link in `L_B`, and let finite `L` contain every link incident on `V_B`. On an arrow vector with three high ends at each site of `V_B`, `B` gives a finite linear combination of such arrow vectors, unchanged off `L_B`. Its matrix coefficient depends only on the initial and final arrows on `L_B`.

*Proof.* Lemma 2.1 keeps matter on `S_B` empty, and locality keeps the other matter empty. `B` commutes with all `H_x^j`. Lemma 3.1 therefore gives the initial-segment form at both ends of each link in `L_B`. The fixed odd link sum makes one end high and one low. The output has three highs at each site of `V_B`. Outside `L_B`, `B` is the identity; its matrix coefficient is the corresponding finite-support matrix element. ∎

**Lemma 3.3 (loop operators).** For a closed trail `C=(x_i,ℓ_i,x_{i+1})_{i=0}^{k−1}` with distinct links and `x_k=x_0`, define
\[
O_C=\sum_{j_0,\ldots,j_{k-1}=1}^5\prod_i
 r_{j_i}^{\ell_i,x_i\dagger}r_{j_{i+1}}^{\ell_i,x_{i+1}},\qquad j_k=j_0.
\]
It is gauge invariant. On an arrow vector it reverses `C` with a fixed sign `σ_C=±1` if `C` is directed toward each `x_{i+1}`, and otherwise vanishes. In fact `σ_C=+1` (referee closure RC-σ; referee closure, VC1_5U_ODD_REFEREE.md).

*Proof.* Link bilinears are even and commute on distinct links. At each visit to a site the creation and annihilation flavour indices contract, so the sum is invariant under the site's `U(5)`, including repeated visits. On an initial-segment vector, a nonzero term requires each creation index at least `a+1` and the same index, as an annihilation index at the preceding link, at most `a+1`. Thus all indices equal `a+1`. This term acts exactly when each arrow points along the trail. The sign is fixed by the link orientations and `a`, independent of the other arrows. ∎

**Lemma 3.4 (finite modifications).** If two ice configurations differ on finite `D`, the arrows on `D` in the first configuration form a balanced directed graph. It decomposes into link-disjoint directed closed trails. Reversing them successively remains in ice and gives the second configuration.

*Proof.* At each site the two ice constraints give equal numbers of incoming and outgoing changed links. Follow unused directed links until the starting site recurs, remove the closed trail, and repeat. Each reversal preserves the ice constraint. ∎

The end electric values in this sector are `p_{ℓ,src}−m/2=±1/2`; the loops and diagonal end numbers give the spin-1/2 U(1) quantum-link action on ice configurations. This identification is context; the following proofs use the explicit operators above.

## 4. States from ice measures

Let `ν` be a quasi-invariant Borel probability measure on `Ω_ice`. For a replacement `S:D→D'`, set `R_S=dS_*(ν|_D)/dν` on `D'` and
\[
(V_S\psi)(c')=1_{D'}(c') R_S(c')^{1/2}\psi(S^{-1}c').
\]

**Lemma 4.1 (replacement calculus).** `V_S` is a partial isometry from `L²(D)` onto `L²(D')`, `V_S^*=V_{S^{-1}}`, and on one finite link set
\[
V_{\beta'\to\beta''}V_{\beta\to\beta'}
=V_{\beta\to\beta''}M_{1_{D(\beta,\beta')}}.
\]
Enlarging the link set partitions a replacement into the sum of its restrictions with unchanged extra arrows.

*Proof.* The change-of-variables identity gives the isometry and its range. The Radon–Nikodym chain rule gives the adjoint and composition; the latter domain is the intersection of the two admissibility domains. On refinement, domains partition disjointly and derivatives restrict to the corresponding pieces. ∎

For local `B∈A^gauge`, take `V_B,L` as in Lemma 3.2. Let `k_B(β',β)` be its arrow-vector coefficient if both assignments satisfy ice at every site of `V_B`, and zero otherwise. Define the finite sum
\[
\Theta(B)=\sum_{\beta,\beta'} k_B(\beta',\beta)V_{\beta\to\beta'}.
\]
Refinement makes this independent of a sufficiently large `L`.

**Theorem 4.2 (RK construction).** `Θ` extends to a unital representation of `A^gauge` on `L²(ν)`. The vector state `ω̂_ν(B)=⟨1,Θ(B)1⟩` extends by `ω_ν=ω̂_ν∘E` to a gauge-invariant state of `A`. For every allowed base-tick constant, it is stationary. If `ν` is `G`-invariant, it is cell invariant. It has filling 0, sharp `Q_x=3m`, isotype `w*`, and shadow equal to the image of `ν` under the high/low end-number map. The full-matter construction has the same properties with filling 5, sharp `Q_x=5+3m`, and isotype `w*+(1,1,1,1,1)`.

*Proof.* On local invariant algebras, linearity, `Θ(1)=1`, and `Θ(B^*)=Θ(B)^*` follow from the definition and Lemma 4.1. For a product use a common finite link set containing all links incident on both supports. Lemma 3.2 restricts intermediate vectors to arrow vectors, and the composition formula sums precisely their matrix coefficients. Hence `Θ(BB')=Θ(B)Θ(B')`. These finite-dimensional *-representations are contractive; local fixed elements are dense, giving the extension. `VC1_5.md` Theorem 2.1 gives the gauge-invariant extension.

Every cube hop kills empty matter; every electric gate has the same phase on all arrow vectors because its squared electric field is `1/4`. Thus each gate maps under `Θ` to a scalar and the base tick fixes the vector state. Gauge averaging commutes with the tick. A lift permutes arrow vectors without configuration-dependent signs: on end exchange the sign is `(-1)^{a(a+1)}=1`. The matter vacuum is fixed. If `ν` is invariant, the induced unitary on `L²(ν)` fixes 1 and intertwines the replacement operators, proving cell invariance. The number and shadow statements follow by diagonal action. Lemma 3.1 makes every arrow vector a highest-weight vector of weight `w*`; highest-weight theory gives its isotype.

For full matter, total matter conservation keeps the local matter full; raising operators kill it and add 1 to each weight. Each hop kills full matter because a creator acts at a filled site. Matter sign lifts act by a configuration-independent phase. The same arguments apply. ∎

**Theorem 4.3 (purity and tail).** `ω̂_ν` is pure on `A^gauge` if and only if `ν` is tail-trivial. The same holds for the full-matter construction. In that case `ω_ν` satisfies P and F.

*Proof.* Products of end-number projections give every cylinder multiplication projection `M_{1_[β]}`. Their action on 1 is dense in `L²(ν)`, so `(L²(ν),Θ,1)` is the GNS representation. An operator commuting with all cylinder multipliers is multiplication by an `h∈L∞(ν)`: apply it to 1 and use density and boundedness. By Lemma 3.3, commuting with each loop operator forces `h` to agree almost everywhere before and after each directed loop reversal. Lemma 3.4 and quasi-invariance extend this equality to every finite replacement.

For a finite `L`, average `h` over the finite fibre of all ice configurations with the same arrows off `L`. After removing finitely many null sets this average equals `h` almost everywhere and depends only on outside arrows. Taking a limsup of such versions along the increasing incident-link sets gives a tail-measurable version of each of `Re h` and `Im h`. If the tail is trivial, `h` is constant, so the GNS commutant is scalar and the state is pure.

Conversely, purity gives P, and Theorem 2.2 makes the number shadow tail-trivial. By referee closure RC-T, `ν` is tail-trivial exactly when its shadow is (referee closure, VC1_5U_ODD_REFEREE.md). The full-matter proof is identical. P implies F by `VC1_5.md` R1. ∎

Stationarity in this sector is kinematic for the base tick. A supplied plaquette layer can reverse trails and need not preserve these states; GA1-P-5 remains open.

## 5. Consequences and the R4 limit

**Theorem 5.1 (ICE-T suffices).** If ICE-T holds, every odd `m∈{1,3,5,7,9}` and every allowed choice of base-tick constants has two distinct P-witnesses, of filling 0 and 5. Their sharp charges and isotypes are those in Theorem 4.2. Both are factor states.

*Proof.* Apply Theorems 4.2–4.3 to an ICE-T measure. The matter number distinguishes the two states. ∎

**Theorem 5.2 (edge necessity).** If `m=1` or `9`, and a state satisfies (iii), P and has filling 0 or 5, then ICE-T⁻ holds. This does not require (i) or (ii), and holds for any plaquette class.

*Proof.* For `m=1` use Corollary 2.3. For `m=9`, each link has one end of number 4 and one of number 5. `VC1_5.md` Theorem 5.3 gives `q=27` or 32 at fillings 0 or 5, so exactly three ends at each site have number 5. Theorem 2.2 gives tail triviality of the shadow. Writing `ν` for the high-end arrow law, by referee closure RC-T, `ν` is tail-trivial exactly when its shadow is (referee closure, VC1_5U_ODD_REFEREE.md). ∎

For the other odd values of `m`, the same argument at filling 0 or 5 gives a cell-invariant tail-trivial law on divergence-free flows `p_{ℓ,src}−m/2∈Z+1/2` with absolute value at most `min(m,10−m)/2`. At fillings 1–4 the shadow can carry charges; no ice reduction is claimed.

**Theorem 5.3 (R4 limit).** Let `ω` be a local weak-* limit point of the finite-volume states of `VC1_5.md` R4 along a subsequence, and let `ν` be its ice arrow law. Then `ν` is `G`-invariant and flip-invariant, `ω|A^gauge=ω̂_ν`, and `ω∘E` is pure on `A^gauge` exactly when `ν` is tail-trivial. If `ν` is not tail-trivial, the restriction is not a factor state.

*Proof.* R4 uses the uniform vector sum over ice assignments of zero flux on even periodic boxes. For a local invariant `B`, Lemma 3.2 expresses its action by local ice replacements. Lemma 3.4 decomposes each replacement into directed closed trails inside a fixed non-wrapping region for sufficiently large boxes. Such trails have zero net crossing of every coordinate plane, so their reversals preserve the R4 flux sector. Thus the local expectation is the uniform average of the corresponding finite matrix coefficients, and each local replacement preserves the uniform finite-volume arrow law.

Cylinder probabilities converge along the chosen subsequence to `ν`; local replacement invariance passes to the limit and then from cylinders to Borel sets. R4 gives cell invariance. For a flip-invariant measure, every replacement Radon–Nikodym derivative is 1 on its range. The coefficient formula for `ω̂_ν` is therefore the same as the finite-volume limit, using equality of the measures of a replacement's domain and range. This proves the restriction identity. Theorem 4.3 gives the purity equivalence. By referee closure RC-T, `ν` is tail-trivial exactly when its shadow is (referee closure, VC1_5U_ODD_REFEREE.md). If the tail is nontrivial, Theorem 2.2 rules out a factor restriction. ∎

Thus **ICE-U(R4)** asks: "Some local weak-* limit point of the R4 states of `VC1_5.md` has a tail-trivial arrow law." It is exactly the missing tail-triviality step in that route and implies ICE-U. ICE-U as an abstract existence statement need not by itself identify a particular R4 limit.

**Conditional records.** For `ω_ν` with any `G`-invariant quasi-invariant `ν`, in particular `ω∘E` for every R4 limit point `ω` (Theorem 5.3), under PS-3c, PS-4, proposed PS-3h5 and the joint Born identification, the empty- and full-matter constructions form records of 0 and 5 respectively at every site at tick 1; each R4 limit gives records of 0. Their site numbers are sharp and constant at every tick, so the proof of `VC1_5.md` Corollary 5.6 applies. These readings are not adopted here.

**LZ1 consequence.** For `ω_ν` with any `G`-invariant quasi-invariant `ν`, in particular `ω∘E` for every R4 limit point `ω` (Theorem 5.3), the empty-matter state has non-character isotype `w*`. Its `su(5)` quadratic Casimir is positive, so some traceless Hermitian generator `T` has `ω_ν((G_x^T)²)>0`. The conditional conclusion of `LZ1.md` RC1(c)(iii) therefore applies. This does not prove a propagating physical excitation.

## 6. ICE-T: checks on proposed routes

**Lemma 6.1 (finite-resampling criterion).** Let independent random variables `ξ_i`, indexed by a countable set, determine an ice configuration `Y`. Suppose replacing any finite set of inputs by independent copies changes only finitely many arrows almost surely. Then the law of `Y` is tail-trivial.

*Proof.* A tail event is unchanged by finite arrow modifications. For finite input set `J`, its indicator is almost surely unchanged by resampling `J`, and the resampled output is independent of the original `ξ_J`. Thus the event is independent of every finite input σ-algebra, hence of the full input σ-algebra containing it. Its probability equals its square. ∎

**Proposition 6.2 (A1: deterministic transition systems).** Every `G`-invariant transition system consists of bi-infinite trails. Independently orienting its trails by fair coins gives a `G`-invariant ice law that is not tail-trivial.

*Proof.* The order-three site stabilizer cycles the even-cube incident triple and the odd-cube incident triple separately (`VC1_5.md` Theorem 2.2). An invariant pairing cannot pair two links in either triple: the 3-cycle maps such a pair to a different pair in the same triple, sharing a link with it, and a pairing contains at most one pair inside a 3-set. Thus it pairs `a_i` with `b_{i+k}` for fixed `k mod 3`. The explicit walk in the proof of `VC1_5.md` Theorem 6.1 shows that `k=0` gives straight lines; the other possibilities repeat with nonzero translation `(2,2,−2)` or `(2,−2,2)`. Every pair joins an even and an odd link, so every trail contains an even link. `G` is transitive on even links and permutes the trails, so all trails are infinite (`VC1_5.md` line 136). The group permutes them, preserving the independent fair-coin law. For one fixed trail, the event that its arrows agree with a chosen direction except on finitely many links is a tail event of probability `1/2`. ∎

**A2-FIN** asks: "For some stabilizer-invariant full-support law `ρ_0` on the 15 pairings at a site, the i.i.d. `G`-transported random transition system has only finite trails almost surely."

**A2: independent random transitions.** Choose pairings independently at sites from a transported stabilizer-invariant full-support law. Give links independent fair arrows and continuous independent labels. On each finite trail orient according to the arrow on its largest-label link. Conditional on every trail being finite almost surely, this construction is cell invariant and gives independent fair trail orientations. Resampling finitely many inputs affects finitely many trails before and after the change, all finite almost surely, so Lemma 6.1 gives tail triviality. **GAP:** almost-sure finiteness of all trails is not proved. The rule as written does not orient infinite trails. Given A2-FIN, the law is quasi-invariant and ICE-T follows (referee closure RC-A2; referee closure, VC1_5U_ODD_REFEREE.md). The GAP is exactly A2-FIN. Near a deterministic pairing law is not a proof of infinite trails for a full-support law.

**A3: the Bencs–Hrušková–Tóth factor.** Pass 1 reports that Theorem 1.2 of [Factor-of-iid Schreier decorations of lattices in Euclidean spaces](https://arxiv.org/abs/2101.12577) gives, for `d≥3`, a finitary automorphism-equivariant iid factor with finite monochromatic paths, and that forgetting colours gives a balanced orientation. On that reported theorem the resulting `Z³` ice law is `G`-invariant. **GAP:** the pass-1 source does not establish that finite input resampling changes only finitely many output arrows; finitary coding alone does not imply it (referee closure RC-A3a; referee closure, VC1_5U_ODD_REFEREE.md). If the coding radius `R` satisfies `Σ_ℓP(R_ℓ≥d(ℓ,J))<∞` for every finite `J`, for instance `E[R^3]<∞`, Lemma 6.1 gives tail triviality (referee closure RC-A3b; referee closure, VC1_5U_ODD_REFEREE.md; compare Galicza-Pete, arXiv:2406.09232, Proposition 4.3, `unchecked`). The hierarchy was not rebuilt here. Tail triviality and quasi-invariance are not established by this route. The literature statement is a pass-1 report, not an independent source verification in this distillation.

**A4: uniform ice / ICE-U.** An R4 limit is a candidate by Theorem 5.3. A suitable decay-of-boundary-influence estimate for the uniform specification would yield tail triviality, but no such estimate is proved here. Pass 1 reports a three-dimensional Coulomb-phase expectation from [Hermele, Fisher and Balents](https://arxiv.org/abs/cond-mat/0305401); that expectation is not a proof of ICE-U. Pass 1 also marked its claimed absence of a 3D height function unverified, and it is not used. ICE-QI remains open separately.

## 7. LW1-5U-Σc-odd

**Theorem 7.1 (necessary conditions).** Let `m` be odd and `ψ` be pure on `A`, invariant under all local gauge automorphisms and cell lifts.

(a) `ψ` satisfies (ii), (iii) and P.

(b) For one integer `k`, `ψ(Γ_x(u))=det(u)^k` at every site; its isotype is `det^k`, `Q_x=5k` sharply, and its filling is `5k−3m`. For `m=1,3,5,7,9` the possible fillings are respectively `2,1,0 or 5,4,3`.

(c) Its shadow is cell-invariant and tail-trivial.

(d) At `m=5`, `N_x` is sharp at 0 or 5, and its shadow is supported on divergence-free flows `p_{ℓ,src}−5/2`.

(e) No state `ω_ν` of Theorem 4.2 is such a pure gauge-invariant state on `A`; the same holds for its full-matter twin.

*Proof.* (a) A pure gauge-invariant state is extreme among gauge-invariant states, equivalent to P by `VC1_5.md` Theorem 2.1. (b) In the irreducible GNS representation, invariance under `Ad Γ_x(u)` gives a commutant unitary mapping the cyclic vector to `π(Γ_x(u)^*)Ω`; irreducibility makes it scalar. Thus the expectation is a continuous one-dimensional character of `U(5)`. Since `SU(5)` is perfect, every such character is `det^k`. The isotype projection and central circle give the stated isotype and charge. Site transitivity makes `k` common. `VC1_5.md` Theorem 5.3 gives the filling and the listed possibilities.

(c) Apply Corollary 2.3. (d) If the filling is 0 or 5, boundedness makes each `N_x` sharp there. The sharp Gauss charge is 15 or 20, so `Σ_{ℓ∋x}p_{ℓ,x}=15`, which is the zero-divergence condition after orienting links. (e) `w*` and `w*+(1,1,1,1,1)` have unequal entries, hence are not determinant characters. ∎

LW1-5U-Σc-odd remains open. At `m=5` its classical necessary condition is a cell-invariant tail-trivial divergence-free half-integer flow law. ICE-T would give such a law, but does not construct the needed `SU(5)`-singlet quantum state. In general singlet multiplicities exceed one, so the highest-weight scalar construction cannot simply be transferred.

## Referee closures imported for the proofs


Each closure is a complete argument from stated premises. Each is Lean-formalizable: finite combinatorics, countable products of finite or standard Borel spaces, and the standard theorems listed in the head. No `[check]` is a step of any closure.

### RC-T. Tail triviality across the shadow map (referee closure, VC1_5U_ODD_REFEREE.md)

**Lemma.** Let `Π=∏_{i∈I}X_i` be a countable product of finite sets. Let `I_1⊂I_2⊂…` be finite, and let `F_n` be the σ-algebra of the coordinates outside `I_n`. Let `Ω⊂Π` be Borel and write `F|_Ω={Ω∩E : E∈F}`. Then `(∩_nF_n)|_Ω=∩_n(F_n|_Ω)`.

*Proof.* The inclusion `⊂` is immediate. Let `T∈∩_n(F_n|_Ω)` and choose `T_n∈F_n` with `T=Ω∩T_n`. Put `T^*=∩_k∪_{n≥k}T_n`. For each `k`, `∪_{n≥k}T_n∈F_k`, because `F_n⊂F_k` for `n≥k`. So `T^*∈∩_kF_k`. Also `Ω∩T^*=∩_k∪_{n≥k}(Ω∩T_n)=T`. ∎

**Application.** Let `A:K_m→{0,1}^{links}` record on each link whether its source end is high (`p_{ℓ,src}>m/2`). Write `F^{arr}_n` for the σ-algebra of arrows on links with no endpoint in `Λ_n`. The arrow of such a link is a function of its own end numbers, so `A^{-1}(F^{arr}_n)⊂F^{out}_n`.
- (i) Let `κ` be a probability measure on `K_m` with `κ(A^{-1}(Ω_ice))=1`, and `ν=A_*κ`. If `κ` is tail-trivial, so is `ν`. Indeed, by the lemma a tail event of `Ω_ice` is `T=Ω_ice∩T^*` with `T^*∈∩_nF^{arr}_n`. Then `A^{-1}(T^*)` is a tail event of `K_m`, and `ν(T)=κ(A^{-1}(T^*))∈{0,1}`.
- (ii) Let `ι:Ω_ice→K_m` be the injective map of Theorem 4.2 (`n≡0`, `p=a+1` at high ends, `p=a` at low ends) and `κ=ι_*ν`. Then `A∘ι` is the identity of `Ω_ice`, so (i) applies. Conversely `ι^{-1}(F^{out}_n)⊂F^{arr}_n|_{Ω_ice}`, because `n_x∘ι` is constant. So for a tail event `U` of `K_m`, `ι^{-1}(U)` is a tail event of `Ω_ice` and `κ(U)=ν(ι^{-1}(U))`. Hence `ν` is tail-trivial exactly when `κ` is.

Corollary 2.3 (line 43) and Theorem 5.2 (line 120) use (i). Theorem 4.3 (line 108) and the factor clause of Theorem 5.3 (line 128) use (ii) in the direction "`κ` tail-trivial implies `ν` tail-trivial", the second by contraposition. The other direction of (ii) is recorded for completeness. ∎

### RC-σ. The sign of a loop operator (referee closure, VC1_5U_ODD_REFEREE.md)

Let `ℓ` have source end `s` and target end `t`, and let the trail of Lemma 3.3 run from `x_i` to `x_{i+1}` along `ℓ`, with high end `x_{i+1}`. Order creators source end first, as in the text.
- If `x_i=s`: the vector is `r^{s†}_1⋯r^{s†}_a r^{t†}_1⋯r^{t†}_{a+1}|0⟩`. The annihilator `r^t_{a+1}` passes `2a` creators (sign `+1`). The creator `r^{s†}_{a+1}` then passes `a` creators to its place (sign `(−1)^a`).
- If `x_i=t`: the vector is `r^{s†}_1⋯r^{s†}_{a+1} r^{t†}_1⋯r^{t†}_a|0⟩`. The annihilator `r^s_{a+1}` passes `a` creators (sign `(−1)^a`). The creator `r^{t†}_{a+1}` passes `2a` creators (sign `+1`).

Either way the bilinear on `ℓ` maps `|ℓ;x_{i+1}⟩` to `(−1)^a|ℓ;x_i⟩`. Operators on different links commute and act on separate tensor components, so no other sign arises. `Z^3` is bipartite, so `|C|` is even and `σ_C=(−1)^{a|C|}=+1`. `[check]` `check_linksign.py` agrees for `a=0,…,4`. ∎

### RC-6.2. Every `G`-invariant transition system, explicitly (referee closure, VC1_5U_ODD_REFEREE.md)

*Tilings.* The even cubes are `[0,1]^3+2n` (centres `c_0+2Z^3`), the odd cubes `[1,2]^3+2n`. The link `(x,x+e_j)` is an even-cube edge exactly when `x_j` is even. So at `x`, with `s_j(x)=(−1)^{x_j}`, the even link along axis `j` points in direction `s_j(x)e_j` and the odd link along axis `j` points in direction `−s_j(x)e_j`.

*Step 1 (group elements).* For `Q∈O` and `t∈Z^3`, `y↦Q(y−c_0)+c_0+2t` equals `y↦Qy+(c_0−Qc_0)+2t`. The vector `c_0−Qc_0` has entry 1 where `Q(1,1,1)` has entry `−1`, and entry 0 elsewhere. So `g_x(y)=Q_xy+x` lies in `G` whenever `Q_x(1,1,1)=s(x)`. The stabilizer of `0` is `{Q∈O : Q(1,1,1)=(1,1,1)}={1,h,h^2}`, with `h(y_1,y_2,y_3)=(y_2,y_3,y_1)`. `h` permutes the axes cyclically and fixes all signs, so it cycles `{+e_j}` (the even triple at `0`) and `{−e_j}` (the odd triple) separately.

*Step 2 (pairing at `0`).* Let a pairing at `0` be `h`-invariant. Suppose it contains a pair inside one triple. Its `h`-image is a different pair inside the same triple, and the two pairs share a vector. A pairing contains at most one pair inside a 3-set. This is a contradiction. So every pair is `{+e_j,−e_{σ(j)}}` for a permutation `σ`, and invariance makes `σ` commute with the 3-cycle of axes. Hence `σ(j)=j+k mod 3`, `k∈{0,1,2}`.

*Step 3 (pairing at `x`).* `G`-invariance makes the pairing at `x` the image under `Q_x` of the pairing at `0`. Write `Q_xe_j=s_{π(j)}(x)e_{π(j)}`. Then `1=det Q_x=sgn(π)s_1s_2s_3`, so `sgn π=ε(x):=(−1)^{x_1+x_2+x_3}`. The pair `{+e_j,−e_{j+k}}` goes to the even link along axis `π(j)` and the odd link along axis `π(j+k)`. Conjugating the shift `j↦j+k` by `π` gives `j↦j+ε(x)k`. So at `x` the even link along axis `i` is paired with the odd link along axis `i+ε(x)k`. This rule does not depend on the choice of `Q_x`. Each `k` gives one `G`-invariant system, and there are no others.

*Step 4 (trails).* `k=0`: at every site the two links along each axis are paired, so the trails are straight lines. `k=1`: start at `0` and leave along `+e_1`. The rule of step 3 gives the sites

| step | site | `ε` | arrived along | its type at the site | leaves along |
|---|---|---|---|---|---|
| 0 | `(0,0,0)` | `+1` | `+e_2`, from `(0,−1,0)` | odd, axis 2 | `+e_1` (even, axis 1) |
| 1 | `(1,0,0)` | `−1` | `+e_1` | even, axis 1 | `−e_3` (odd, axis 3) |
| 2 | `(1,0,−1)` | `+1` | `−e_3` | odd, axis 3 | `+e_2` (even, axis 2) |
| 3 | `(1,1,−1)` | `−1` | `+e_2` | even, axis 2 | `+e_1` (odd, axis 1) |
| 4 | `(2,1,−1)` | `+1` | `+e_1` | odd, axis 1 | `−e_3` (even, axis 3) |
| 5 | `(2,1,−2)` | `−1` | `−e_3` | even, axis 3 | `+e_2` (odd, axis 2) |
| 6 | `(2,2,−2)` | `+1` | `+e_2` | odd, axis 2 | `+e_1` (even, axis 1) |

At step 6 the walk enters `(2,2,−2)` through the translate of the link `((0,−1,0),0)` and leaves along the translate of `(0,e_1)`. Translation by `T=(2,2,−2)∈2Z^3` lies in `G` and preserves the system. The walk is deterministic and reversible, so its sites obey `x_{i+6}=x_i+T` for all `i∈Z`. If the trail were closed, the sequence of (site, incoming link) pairs would be periodic, which `x_{i+6n}=x_i+nT≠x_i` forbids. So the trail is bi-infinite. For `k=2` the rule of step 3 gives, in the same way, the sites `0,(1,0,0),(1,−1,0),(1,−1,1),(2,−1,1),(2,−2,1),(2,−2,2)` and `T=(2,−2,2)`; this is the `k=1` table with axes 2 and 3 exchanged. These are the two paths of `VC1_5.md` lines 132-133.

*All trails.* For every `k`, every pair joins an even link to an odd link, so every trail contains an even link. `G` is transitive on even links: it is site-transitive, and the stabilizer cycles the even triple. `G` permutes the trails. So every trail is the image under some `g∈G` of the trail through `(0,e_1)`, and is bi-infinite. ∎

`[check]` `check_pairings.py` confirms steps 1-4: stabilizer of order 3; 3 invariant pairings among 15; the pairing at `x` independent of the choice of `Q_x` on `[−3,3]^3`; drifts `(2,0,0)`-type for `k=0` (period 2) and `(±2,±2,±2)`-type for `k=1,2` (period 6) from all six directions at `0`.

### RC-A2. A2 gives ICE-T whenever all its trails are finite (referee closure, VC1_5U_ODD_REFEREE.md)

**Setting.** Let `ρ_0` be a probability law on the 15 pairings at `0`. Let it be invariant under the stabilizer `{1,h,h^2}` and have full support. Put `ρ_x=g_*ρ_0` for any `g∈G` with `g0=x`; stabilizer invariance makes this well defined. Let `τ_x∼ρ_x` (sites), `d_ℓ` uniform on the two ends of `ℓ`, and `u_ℓ` uniform on `[0,1]` (links), all independent. Write `ξ` for the whole input and `P` for its law.

**A2-FIN for `ρ_0`.** `P`(every `τ`-trail is finite) `=1`.

**Proposition RC-A2.** Assume A2-FIN for `ρ_0`. On the event that all trails are finite, let `F(ξ)` orient each `τ`-trail `γ` so that its link `ℓ^*(γ)` of largest label `u` points to `d_{ℓ^*}`. (Labels are distinct almost surely.) Then the law `ν` of `F(ξ)` is a `G`-invariant, tail-trivial, quasi-invariant Borel probability measure on `Ω_ice`. Hence ICE-T holds, and by Theorem 5.1 each odd `m` has P-witnesses at fillings 0 and 5.

*Proof.* (0) *Ice.* Each pair of `τ_x` joins two consecutive links of one consistently oriented trail, so it has one link with high end `x` and one without. Three pairs give three high ends at `x`. The trail through a link is determined by finitely many coordinates when it is finite, so `F` is Borel on the full-measure event.

(1) *`G`-invariance.* `G` acts on inputs by `(gξ)`: `τ'_{gx}=g(τ_x)`, `d'_{gℓ}=g(d_ℓ)`, `u'_{gℓ}=u_ℓ`. The input law is `G`-invariant, and `F(gξ)=gF(ξ)`. So `ν` is `G`-invariant.

(2) *Tail triviality.* Resample a finite set `J` of inputs. A `τ`-trail that visits no site of `J` and contains no link of `J` is also a trail after resampling, with the same `d` and `u` on it, so it keeps its orientation. Only the trails before or after resampling that visit a site of `J` or contain a link of `J` can change. There are finitely many, each finite almost surely (the resampled input has law `P`). Lemma 6.1 gives tail triviality.

(3) *Quasi-invariance.* Fix a replacement `S=S_{β→β'}`. Let `D_0` be the links where `β≠β'` and `V_0` their endpoints. Fix, for each pattern of three high and three low ends at a site, one pairing that matches each high end with a low end. For `ξ` with all trails finite and `c=F(ξ)∈dom S`, define `ξ'=Φ(ξ)`:
- `τ'_x` is the fixed pairing for the pattern of `S(c)` at `x`, for `x∈V_0`; `τ'_x=τ_x` otherwise;
- `u'=u`;
- `d'=d`, except on the largest-label link `ℓ^*` of each `τ'`-trail that visits `V_0`, where `d'_{ℓ^*}` is the high end of `ℓ^*` in `S(c)`.

(a) Every `τ'`-pair joins a high end and a low end of `S(c)`. At `x∈V_0` this holds by choice. At `x∉V_0` no link at `x` lies in `D_0`, so `S(c)=c` on the links at `x` and `τ'_x=τ_x`. So `S(c)` orients every `τ'`-trail consistently.
(b) Every `τ'`-trail is finite. A `τ'`-trail that avoids `V_0` is a `τ`-trail. A `τ'`-trail that visits `V_0` is a concatenation of segments; each segment starts with a link at `V_0` and follows pairings equal to those of `τ` until it returns to `V_0`. Each segment is part of one of the finitely many `τ`-trails through `V_0`, all finite. So there are finitely many segments, each finite.
(c) `F(ξ')=S(c)`. The `τ'`-trails through `V_0` are oriented by `d'` at their `ℓ^*`, which agrees with `S(c)`. The other `τ'`-trails are `τ`-trails avoiding `V_0`, with unchanged `d` and `u`; `F` orients them as `c` does, and `c=S(c)` on them.

Split the domain of `Φ` into countably many Borel pieces `Ξ_k`. On `Ξ_k`, fix the old and new values of `τ` on `V_0`, the set `M` of links where `d` is modified, and the old and new values of `d` on `M`. On `Ξ_k`, `Φ` is the restriction of the bijection `Ψ_k` that replaces these finitely many coordinates. `Ψ_k` multiplies `P` by `c_k=∏_{x∈V_0}ρ_x(τ'_x)/ρ_x(τ_x)`, which lies in `(0,∞)` by full support. Let `B⊂dom S` be Borel with `ν(B)>0`. Some `Ξ_k∩F^{-1}(B)` has positive probability. Its image under `Ψ_k` has positive probability and lies in `F^{-1}(S(B))` by (b) and (c). So `ν(S(B))>0`. The same argument for `S^{-1}` gives the converse. ∎

### RC-A3a. Finitary coding does not imply finite change (referee closure, VC1_5U_ODD_REFEREE.md)

Let `(ξ_n,η_n)_{n∈Z}` be i.i.d., `ξ_n` a fair bit, `η_n∈{1,2,…}` independent of it with `P(η_n≥k)=1/k`. Put `X_n=ξ_{n−1}⊕⋯⊕ξ_{n−η_n}`. Then `X_n` is determined by the inputs at the sites `n−η_n,…,n`, a finite window almost surely, so `X` is a finitary iid coding. Resample the input at `0`. With probability `1/2` the bit `ξ_0` changes. Then `X_n` changes for every `n≥1` with `η_n≥n`. These events are independent and `Σ_n1/n=∞`, so by the second Borel-Cantelli lemma infinitely many occur almost surely. So with probability `1/2` infinitely many outputs change. ∎

### RC-A3b. A coding-radius criterion for Lemma 6.1 (referee closure, VC1_5U_ODD_REFEREE.md)

Let `ξ=(ξ_v)_{v∈V}` be independent, with `V` countable and `d` a graph distance. Let `Y=(Y_ℓ)` take values in `Ω_ice`. Suppose there are Borel `R_ℓ` with the following property: for almost every `ξ`, `R_ℓ(ξ)<∞`, and `Y_ℓ(ξ'')=Y_ℓ(ξ)` for every `ξ''` that agrees with `ξ` at all `v` with `d(v,ℓ)≤R_ℓ(ξ)`. If `Σ_ℓP(R_ℓ≥d(ℓ,J))<∞` for every finite `J⊂V`, then resampling `J` changes finitely many arrows almost surely, and the law of `Y` is tail-trivial.

*Proof.* Let `ξ'` agree with `ξ` off `J`. If `R_ℓ(ξ)<d(ℓ,J)`, then `ξ'` agrees with `ξ` within distance `R_ℓ(ξ)` of `ℓ`, so `Y_ℓ(ξ')=Y_ℓ(ξ)`. By the first Borel-Cantelli lemma, almost surely only finitely many `ℓ` have `R_ℓ(ξ)≥d(ℓ,J)`. Lemma 6.1 applies. ∎

If the `R_ℓ` have one law on each of finitely many link orbits, `#{ℓ : d(ℓ,J)≤r}=O(r^3)` makes `E[R^3]<∞` sufficient on `Z^3`.


## 8. Scope and checks

The standard spectral theorem for compact configuration spaces, Riesz representation, Radon–Nikodym chain rule, the π-λ theorem, Stone-Weierstrass, the Borel-Cantelli lemmas, Schur orthogonality, `U(5)` highest-weight theory and perfectness of `SU(5)` are mathematical inputs. The cited frozen inputs are `VC1_5.md` Theorems 2.1, 2.2, 3.1(a), 5.3, the proof of 6.1, Corollary 5.6, R1, R4; `LW1_5.md` Theorem U and B1-U; `LZ1.md` RC1(c)(iii). They are not independently rederived here. Pass 1's literature search and its expressly unverified records are in the draft; no broad absence-of-literature claim is needed. The algebraic steps above were checked for domains, support and dependence on the measure. This distillation has had the fresh-session referee check in `VC1_5U_ODD_REFEREE.md`, but no independent audit. The referee closures have had only that one check.

No statement establishes that these edge-filling witnesses arise from the free sea, are stable, or have the excitations and energy density needed for VC1. Nothing here selects a law or adopts an axiom or reading. Both five-mode laws remain live under `TOE_ASSEMBLY.md` §3.5.
