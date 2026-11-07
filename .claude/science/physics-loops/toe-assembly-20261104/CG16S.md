# CG1-16-S. A site-count change around the 16

## 0. Status

**Pass 2, not refereed or frozen.** This is conditional mathematics on proposed point registers. It adopts no law, reading or axiom. The CG1 target and its physical vacuum remain open.

**Proved below.** Point registers encode finite configurations with at most one site per point. Their centre algebra gives spinor-class site changes; SC-odd ties their parity to site count. End-pure links freeze occupations under the complete gauge-invariant update. An explicit end-mixed register permits a local gauge-invariant transfer. A different link permits a gauge-invariant odd local singlet under SC-min. Under the specified D1 and link conditions, odd bands are flat at nodes. The smooth-unitary index formula is proved for isolated Weyl nodes. TM1's finite-observable results carry over under their hypotheses. A conditional coarse-centre spectrum result is proved for blocks of at least three points.

**GAPs.** The draft's finite-depth winding proof assumes its individual gate layers are translation covariant, while NN-a requires covariance only of the complete update. Its universal free-walk doubling conclusion is therefore unproved under NN-a. A recorded value need not be deterministic: permanence implies conditional persistence, not a probability-one Born marginal for a predetermined value. The coarse-centre argument needs link-purity, omitted from its statement, and does not apply to the owner's singleton embedding. The draft's proposed static-class identification is too broad: momentum independence does not imply tick eigenvalue 1. The construction of one moving gate does not itself establish a fully covariant moving law. Details and corrected claims appear below.

**Open by name.** CG1-i, CG1-ii, MT1-i, MT1-ii; MT1-S[R-CS^str], R-CS^str, VC1 including whether its vacuum is D1; LZ1-i and R-SC; TM1-i and the point-register form of PS-3h5; ZM1-I1[a]; GA1-P-5; adoption of SC-min or SC-odd, R-site or R-point, and L-point or L-site; propagation of the singlet composite; the free-walk winding question under NN-a. Neither a chiral 16 nor a universal exclusion for the whole proposed class is established.

**Provenance.** Pass 1: `CG16S_DRAFT.md`, Claude Opus 5.5, max; SHA-256 `c817ba9008cf1f1244f4a7c775f687816f7bdc3294ae30d63969f872d0a2b5f9`. Pass 2: Codex, requested model `gpt-6.1-terra`; actual model, effort and session id: see run log. `prior/CG16S.md` SHA-256 `70b216fee9e7b6289022ebc7b0338b008601cac8d5685ceb112143aff5d27215`; `TOE_ASSEMBLY.md` `6fda41c203ac95b5333a6a97e2a01a0d287feb065bbcb475644ac4ef0f86856a`. Context hashes: `LW1_5.md` `bdd5159f8585030b560b8f88c05010ad90aaf1aeb801a79dc9b06e963fdad518`; `RCS1.md` `0b2addf9efb30ce3770076c0613ea131a6d3c29e1246f39734ea37c2f210aecf`; `TM1.md` `27ad4fa60f5b2e8c4c245850559fe5b2f8ca87cd01a31d66485e0d95aa8c04e5`; `LZ1.md` `ecd65ab7c6854ecf23dc961916d97dff3c9504ad51af0ad826970dd37bcdecc9`; `ZM1.md` `19bb781d7923b0a6b647f260a0e9c4051f0221658189346db885cfa7b0f2f4bf`; `LW1.md` `78280bd620800eac671ddf6047d42e94c2ecf919d2f938909cc5595b168c09b9`. Source revisions of external branches are those reported in the draft, not independently refreshed; no git commands were run. The draft reports a floating-point scratch check of Theorem 7; this pass did not reproduce it. No independent referee or audit has checked this file.

## 1. Definitions inferred by the distiller

These precisify the draft; they are proposed, not adopted physics.

1. The fixed point set is `Z³`, with the cell group `2Z³ ⋊ O_{c₀}`. A point has at most one site. Put `F=ΛC⁵=S_+⊕S_-`, the even and odd half-spin spaces, and `V=C|∅⟩⊕F`, with `|∅⟩` even. The restricted register is `V⁻=C|∅⟩⊕S_-`. Define `o=1−|∅⟩⟨∅|` and parity `P=|∅⟩⟨∅|+(−1)^N o`. Matter factors use graded tensor products; links are even ordinary factors. Extend the site Spin(10) action trivially to `|∅⟩`, and set its generators to zero there.
2. **SC-min**, proposed: use `V` at every point, finite link registers carrying commuting endpoint frame actions, and a finite-depth NN-a update of even nearest-neighbour gates. The complete update is locally gauge invariant and cell covariant. **SC-odd**, proposed: replace `V` by `V⁻`. NN-a does not require the individual gates or layers to be gauge invariant or covariant.
3. A link is **end-pure** if the lift of `−1∈Spin(10)` is scalar at each end. It is **link-pure** if the products of the two end lifts of `−1`, and of the two end factors of `ω=exp(iπ∑_j M^{2j−1,2j})`, are each scalar. These are different conditions. A centre pattern is the list of eigenvalues of the local centre adjoint implementers, equal to 1 outside finite support.
4. A **D1 state** is stationary, invariant under even translations and under every local centre adjoint action. Its GNS implementers fix the cyclic vector. Use the finite-fibre band and node definition of `LZ1.md` §1: a translation-intertwining isometry carries the tick to continuous `V(K)`, a node has `V(K₀)=1` and `V` is `C¹` nearby. R-loc is this proposed reading of physical species, not an adopted identification.
5. Setting **G** is the gauge-link setting of SC-min or SC-odd. Setting **F** has no links, global Spin(10), and even NN-a gates. In F, condition **E** says each gate preserves the local empty line and the local one-occupied-point subspace. This implies empty-background invariance and a one-site walk; it is stronger than merely saying the complete update has those properties.
6. For a homogeneous matter operator, `Δn` denotes its site-count change and `θ=±1` its fermion parity. A local matter operator is spinor class if its centre eigenvalue is `±i`, tensor class if `±1`. Operators without a definite `Δn` are understood by decomposition into homogeneous components.
7. **R-site**, proposed: occupied points are physical sites, so site creation changes the lattice axiom's reading. **R-point**, proposed: all points are sites; then the point algebra is `M₃₃(C)` rather than PS-5's `M₃₂(C)`. **L-point**, proposed: a record fixes the actual value at its point in later half-ticks. **L-site**, proposed: a record follows the moving site. None of these is adopted.
8. For the TM1 comparison, take the proposed PS-3g fixed algebra as the actual-value algebra, together with TM1's joint Born and record-formation premises. For ZM1 use its unital *-homomorphism and (G1), and specify the fine embedding set `S_u`; the owner's ZM1-I1[a] uses singletons.

## 2. Site count and the centre

**Theorem 1 (encoding; draft Lemma 3.1).** For finite `Λ`, the graded space of configurations with occupied subset `S⊆Λ` and content `F` at each occupied point is canonically `⊕_S ⊗̂_{x∈S}F_x ≅ ⊗̂_{x∈Λ}V_x`, equivariantly for the frames.

*Proof.* Expand the graded tensor product of the direct sums. Empty factors are even and contribute no signs. Frame actions agree on each summand. □

This is an encoding, not a uniqueness theorem for all possible changing-site models. Interstitials require a larger register. A unitary can empty a point while transferring information to its other support factors. The two axiom readings are R-site and R-point above.

**Theorem 2 (centre algebra; draft Lemma 3.2 and Corollary 3.3).** Put `z_x=exp(2πi M_x^{12})` and `ω_x=exp(iπ∑_j M_x^{2j−1,2j})`. On `V`,
\[
 z_x=(-1)^{o_x},\qquad ω_x=|∅⟩⟨∅|-i(-1)^{N_x}o_x,\qquad \prod_{x∈Λ}ω_x=(-i)^{N_s}(-1)^F.
\]
Thus `Ad(∏ω_x)A=(−i)^{Δn}θ(A)A`. On `V⁻`, `ω_x=|∅⟩⟨∅|+io_x` and `z_x=P_x`; hence `θ(A)=(−1)^{Δn}`. Filling or emptying one point is spinor class for either content parity. Under SC-min both even and odd such operators exist; SC-odd selects a fermionic half-spin site.

*Proof.* On `F`, `M^{2j−1,2j}=n_j−1/2`. Thus the five factors give `(−i)^5(−1)^N=−i(−1)^N`, and the `2π` rotation gives `−1`. Both act as 1 on `|∅⟩`. Multiply the commuting factors and compare source and target eigenspaces. Under SC-odd the content parity is odd, giving the last identities. □

These centre identities and the spinor-class test are already proved in the supplied model of `docs/A_SITE_COUNT_CHANGE_BY_ONE_CARRIES_THE_SPIN10_SPINOR_SO_UNDER_THE_ODD_SITE_RULE_EVERY_FERMION_IS_A_MOBILE_SITE_DEFECT_WHILE_ITS_CONES_STAY_VECTOR_LIKE_BOUNDED_THEOREM_NOTE_2026-10-22.md` (#10038 A2–A4, source branch and status in the draft); see also the fixed-site result #10027 B in `docs/SPIN10_MOTT_SITES_CARRY_NO_COMPOSITE_SIXTEEN_THE_CENTRE_FIXES_EVERY_FERMION_TO_THE_VECTOR_CLASS_BOUNDED_THEOREM_NOTE_2026-10-22.md`. These are author-side supplied-model results, not retained status. SC-odd is sufficient to make every one-site spinor defect fermionic; it is not necessary for an individual odd-content defect under SC-min.

**Theorem 3 (pinning and transfer; draft Propositions 3.4–3.6).** For a Spin(10) law with end-pure links, the complete gauge-invariant update conserves every `o_x`. The same is true gatewise if each gate is gauge invariant. `L5-O`'s `S_+` is end-pure. Conversely, the following end-mixed, link-pure register admits an even local gauge-invariant transfer:
\[
R=\mathbb C r_0\oplus(S_+\otimes S_+^*)\oplus(S_-\otimes S_-^*).
\]
For orthonormal bases `B_σ`, define
\[
T^σ={1\over4}\sum_{s,s'\in B_σ}(|∅⟩⟨s|)_x\widehat\otimes(|s'⟩⟨∅|)_y\otimes|s\otimes s'^*⟩⟨r_0|,\quad h=\sum_σ(T^σ+T^{σ*}).
\]
The gate `exp(−iπh/2)` transfers an occupied point at `x` to `y` and changes the link from `r₀`. Under SC-odd keep only `σ=−`.

*Proof.* The local gauge element `z_x` is `(−1)^{o_x}` times scalar end factors. The full update fixes it, so it fixes `o_x`; the same reasoning applies to an individually invariant gate. `LW1_5.md` §S1–S4 gives end-purity for `S_+`. In the transfer, the endpoint contractions pair a representation with its dual, so they are invariant. The matter parity is unchanged. Each `T^σ` maps an orthonormal source basis to orthonormal images because `dim S_σ=16` and `16/4²=1`. Its source and range are orthogonal. Therefore `h` exchanges each source with its image and its exponential transfers it up to `−i`. Both products of endpoint centre factors are 1 on every summand, so the register is link-pure. □

The transferred state leaves link excitation behind; no claim of an independently moving bare charge follows. **GAP:** one gate is not yet a proof that a finite-depth, fully cell-covariant law implements nontrivial motion under all SC-min conditions. Also, the draft's claim about *every* NN-a gate is too strong: only the whole update is required to be invariant.

**Theorem 4 (site-count selection and counterexample).** Under SC-odd an even homogeneous operator has even `Δn`. An even matter-only operator invariant under global Spin(10) has `Δn≡0 mod 4`. With links, the latter restriction can fail: under SC-min let `R=C r₀⊕F`, with Spin(10) at `x` acting on `F` and the other end trivial. Then `∑_{s∈B_+}(|s⟩⟨∅|)_x⊗|r₀⟩⟨s|` is even, gauge invariant and has `Δn=1`.

*Proof.* The first two statements follow from Theorem 2 and invariance under the global centre. In the example, the matter creation and link annihilation form the invariant pairing of `S_+` with its dual; `S_+` is even. □

The matter-only restriction is already #10038 A7/C0 in the path above; it must not be extended to arbitrary gauge links. Under the `U(5)` frame, `|∅⟩` and the Fock vacuum have the same trivial representation, so their even exchange is frame invariant without a link. `S_-=Λ¹⊕Λ³⊕Λ⁵` is not one irreducible U(5) multiplet.

**Four-test assessments, proposed.** The draft rates SC-min P/P/P/C: it fixes a closed register without naming species or chirality, while motion requires further link structure. It rates SC-odd F/P/F/C: its selection has the fermionic defect as its stated reason, restricts content and removes the one-mode odd-odd hop. These are judgments for the owner, not theorem status. In particular SC-odd alone does not prove propagating particles or CG1.

**Prior removed-site comparison.** The draft reports `docs/CANDIDATE_LAWS.md` CL-2 and `docs/CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md` as permanent record-related removals/graph holes; `docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md` uses vacancy for absence of a record on a fixed site. Its scale-ladder B3 source calls a hole a formation output. #10038 E1 adds 56 sites per cube, centre neutral modulo four. These comparisons use the draft's reported source reads; they do not establish a universal repository-wide novelty claim.

## 3. Gauge links and D1 bands

**Theorem 5 (flat odd nodes; draft Theorem 4.2).** In setting G assume either (a) SC-odd, Spin(10), link-pure registers and local centres `ω_x`, or (b) U(5), either point register, link operators preserving total rishon number, and centres `exp(iπQ_x)`. For any D1 state, the GNS space decomposes into finite-support centre-pattern eigenspaces. Its odd sector lies in the nontrivial-pattern subspace. On that subspace, translations and the tick take the form `L²(T³;K)`, `M_β`, and `1⊗W`. Every finite-fibre odd band is identically 1 on a connected `C¹` neighbourhood of a node.

*Proof.* Local centre actions commute, have finite order, commute with the complete tick and transform covariantly under even translations. Average a local operator over the finite centre group on a set containing its matter support and both ends of its links. This splits it into finitely many centre eigenoperators, trivial outside that set. Apply them to the D1 cyclic vector and use density and orthogonality.

In (a), the product of centre actions over that set acts on a homogeneous matter component as `i^{Δn}` and trivially on links by link-purity. Odd components have odd `Δn`, hence nontrivial pattern. In (b), the product is matter parity: both link ends contribute and total rishon number is preserved. A finite nonempty pattern has no nonzero translation stabilizer. Choose orbit representatives; translations identify the nontrivial-pattern space with `ℓ²(Z³;K)`, while the tick acts identically on every translate. Fourier transform gives `1⊗W`. For a finite-fibre band, its fibre eigenvalues lie almost everywhere in the countable point spectrum of `W`. The `C¹` traces of powers of the band matrix are constant on a connected neighbourhood by the countable-range/Fubini argument in `LZ1.md` Theorem 2.2. At a node all eigenvalues equal 1, so unitarity gives the result. □

This extends the already proved pattern and flat-node results in `LZ1.md` Theorems 2.1–2.2; the supplied D1 state need not be VC1. It excludes an odd propagating Clifford node only in the proposed finite-fibre R-loc reading. It does not rule out dressed sectors or prove that every propagating 16 must use R-CS^str. **GAP:** `1⊗W` need not equal 1. Only its eigenvalue-1 part is tick-fixed and belongs to the LZ1-SC static class; flat nodes at eigenvalue 1 are fixed on their node neighbourhood.

**Theorem 6 (odd invariant under SC-min; draft Proposition 4.2.3).** On a link `R'=C r₀⊕(S_+⊗S_-)`, the local operator
\[
A=\sum_{s∈B_+,t∈B_-}(|s⟩⟨∅|)_x\widehat\otimes(|t⟩⟨∅|)_y\otimes|r₀⟩⟨s\otimes t|
\]
is nonzero, gauge invariant and odd; the link is link-pure.

*Proof.* At each end the matter factor is contracted with its dual link factor. The two matter creations have opposite parities, so the product is odd. Both end lifts of `−1` multiply to 1; the `ω` eigenvalues `−i` and `+i` also multiply to 1, as on `r₀`. □

Thus the fixed-site statement `RCS1.md` Theorem 4 and the parity identity in `LZ1.md` §1 do not extend unchanged to all SC-min registers. The operator is a gauge singlet, not a CG1 spinor field. Whether it propagates is open. Under SC-odd and link-purity, the character argument in Theorem 5 shows every local invariant operator is even; norm closure extends this to the invariant quasi-local algebra.

## 4. Free walks and chirality

Let `V:T³→U(d)` be smooth and set `W₃[V]=(24π²)⁻¹∫tr(V⁻¹dV)³`. At a quasienergy-zero Weyl point `K₀`, assume `dim ker(V(K₀)−1)=2`, a smooth local logarithm `H=i log V`, and a smooth rank-two spectral frame with `H=a1+b·σ`, `a(K₀)=b(K₀)=0`. Put `N_{ij}=∂_i b_j(K₀)`. Require `N` invertible and `|∇a·n|<|Nn|` for every unit `n`. The chirality is `χ=sign det N`. These assumptions isolate a non-over-tilted node. At quasienergy `μ`, replace `V` by `e^{iμ}V`.

**Theorem 7 (draft Theorem F).** If `Z₀={K:1∈spec V(K)}` is finite, there are local indices with `∑ ind(K₀)=W₃[V]`; at a Weyl point `ind(K₀)=−χ(K₀)`. Hence, if all points of `Z₀` are Weyl points, `∑χ=−W₃[V]`. The same holds at `μ`, provided its corresponding node set is finite and has the stated type.

*Proof.* The form `ω₃=(24π²)⁻¹tr(g⁻¹dg)³` is closed: the Maurer–Cartan identity gives `d tr θ³=−tr θ⁴=0`, the last equality by graded cyclicity. On `C={U:1∉spec U}`, the logarithm `L` with eigenvalues in `(0,2π)` defines `Φ(t,U)=exp(itL(U))`. The homotopy formula gives a two-form `β` with `dβ=ω₃|_C`. Delete small balls around `Z₀` and apply Stokes. The limits of the individual negative boundary integrals exist because `V*ω₃` is bounded on shrinking shells; their sum is `W₃`.

At a Weyl point the tilt condition makes the two local energies positive and negative on a small surrounding sphere. The logarithm `L(V)` tends, in `C¹` on that sphere, to `2πΠ` on the doublet, where `Π=(1+\widehat{Nn}·σ)/2`; the complementary block becomes independent of the sphere. For `g=1+(e^{2πit}−1)Π`, direct multiplication gives
\[
\operatorname{tr}(g^{-1}dg)^3=-3|1-e^{2πit}|^2(2π i\,dt)\operatorname{tr}(ΠdΠdΠ).
\]
Its integral is `−c₁(Π)` with `c₁=(i/2π)∫tr(ΠdΠdΠ)`. The degree of `n↦\widehat{Nn}` is `χ`, and `c₁(Π)=−χ`; the boundary integral is therefore `χ` and its negative is `−χ`. A scalar phase does not change `V⁻¹dV`. □

The draft reports `check_F.py` numerical checks of the sign and normalization for two specific maps, yielding `W₃=0, ∑χ=0` and `W₃=−1, ∑χ=1`; those calculations were not rerun here and are not proofs. The draft relates this formula to Bessho–Sato, arXiv:2006.04204, Eq. (15); this pass did not independently inspect that paper. Nonzero winding leaves a Floquet loophole, so Theorem 7 alone does not establish doubling.

**Theorem 8 (one-site walk; draft Lemma 4.4.1).** In setting F under E, the empty product state is invariant and the GNS one-site subspace is invariant. The induced walk is a finite product of disjoint local one-site unitaries and, because the complete tick is cell translation covariant, its Bloch matrix is a finite-range trigonometric polynomial of size `8 dim F` (with `F=S_-` for SC-odd).

*Proof.* Each gate fixes its local empty vector up to `λ_g` and preserves the local one-site subspace. The normalized induced action is `λ_g⁻¹g` on that subspace and identity outside the gate. A disjoint layer acts as their direct sum. The empty product state is invariant under each gate automorphism, and finite depth gives finite range. The full update commutes with even translations, giving the Bloch representation. □

**Theorem 9 (conditional winding and doubling; corrected draft Theorems H and 4.5).** Add the hypothesis that the one-site gate layers in Theorem 8 individually have a finite-periodic, translation-covariant decomposition. Then `W₃[V]=0`. If the individual gates commute with a compact group fixing the empty vector, each isotypic multiplicity walk has zero winding. If only the complete walk commutes with the group, `∑_ρ dim(ρ) W₃[V_ρ]=0`. For Spin(10), even gates, SC-min or SC-odd and E, each half-spin block has `V_σ=1_{S_σ}⊗W_σ` and `W₃[W_σ]=0`. If the node set of `W_σ` at a given quasienergy is finite and consists of the Weyl points defined above, their net chirality is zero.

*Proof.* Take a Hermitian logarithm of each local one-site unitary, repeating the choice by translations. Exponentiating it from zero to one gives a finite-range periodic homotopy of each layer and of their product. The closed three-form gives homotopy invariance of `W₃` and the identity has winding zero. If the gates commute with the group, choose logarithms by functional calculus, so the homotopy respects each isotypic decomposition. Otherwise block additivity gives the dimension-weighted identity. Evenness preserves content parity on the one-site space; each parity-restricted periodic circuit is null-homotopic. The complete Spin(10) action is irreducible on `S_σ`, so Schur's lemma gives `V_σ=1⊗W_σ` and `W₃[V_σ]=16W₃[W_σ]`. Apply Theorem 7. □

**GAP in draft Theorem H.** Its step “choose `A_g` on one gate per cell-group orbit and transport it” presupposes that the gate decomposition is itself periodic/covariant. NN-a supplies covariance of the *complete* update only. A product may be symmetric although its factors are not, so the written homotopy need not have any Bloch matrix at intermediate times. This is a missing proof, not a counterexample to zero winding. Theorems H and 4.5 under NN-a alone and the claimed universal mirror conclusion remain open. Condition E also excludes general defects over a filled or entangled background. A finite toy with an invariant staggered gap is already reported in the #10038 path above; its result does not prove the general statement.

## 5. Records, zoom and downstream costs

**Theorem 10 (actual values; draft Lemma 5.1 and Proposition 5.2).** Under proposed PS-3g with Spin(10), the fixed point algebra on `V` is spanned by the projectors onto `∅`, `S_+`, `S_-`; on `V⁻` it is spanned by the empty and occupied projectors. Given the remaining TM1 hypotheses, `TM1.md` Theorems 1–5 apply to a covariant finite-spectrum even observable whose spectral projectors are these projectors.

*Proof.* `C`, `S_+`, `S_-` are pairwise inequivalent irreducibles, so Schur's lemma gives the fixed algebras. The projectors are even and covariant under lifts preserving the empty state and half-spin sectors. TM1's arguments use the stated finite observable, its disagreement projections, stationarity, covariance and their other explicit hypotheses; the proof is already in `TM1.md` Theorems 1–5. □

**Theorem 11 (record permanence; correction to draft Proposition 5.3).** In a history measure obeying L-point, if a record at `x` forms at `t` with random value `R_x`, then on the event of that record `ξ_{2n}(x)=R_x` for all `n≥t`, almost surely. If the event has probability 1 and `R_x=v` almost surely, the Born marginal obeys `ω'∘α^n(Π_x(v))=1` for all `n≥t`. More generally the later marginal is the distribution of `R_x`, not necessarily a point mass.

*Proof.* The first statement is L-point. Apply the Born marginal and take probabilities. □

**GAP:** the draft treats “`x` records value `v`” as an unconditional almost-sure event. A record may have a random Born value. For example, a stationary identity tick on a perfectly correlated mixture of all-empty and all-occupied configurations can record at every point while the one-point occupation remains non-sharp. Persistence still holds sample by sample. Under TM1 case (E), for a local excitation `ω'=ω(O*·O)/ω(O*O)`, a tick-1 disagreement witness `α(D)` commuting with `O` has zero expectation in `ω'` if it has zero expectation in `ω`: Cauchy–Schwarz and positivity imply `ω(O*O α(D))=0`. Finite range makes this true outside a bounded neighbourhood of `supp O`. Thus those points record at tick 1 and their *realized* values persist under L-point. To infer a bounded defect relative to a background history one needs a specified coupling or sharp background values; the draft does not provide one. L-site would require a rule identifying and transporting records with sites; the point-register law does not specify one. Named site labels are one possible additional mechanism, not a proved necessity. These are costs to TM1-i, not a resolution of it.

**Theorem 12 (coarse centres; corrected draft Proposition 5.4).** Under SC-odd with Spin(10), let a unital block homomorphism satisfy ZM1 (G1) for `S_u` with `|S_u|≥3`. Assume all fine links internal to `S_u` are link-pure and the endpoint actions on boundary links are as defined above. Then the spectrum of the coarse centre `ω_u^{(1)}` contains all four elements of `μ₄`, up to a common phase. A coarse SC-odd point whose incident endpoint factors of `ω` are each scalar has only two centre eigenvalues, so it cannot satisfy these hypotheses.

*Proof.* Functional calculus and (G1) give `Φ(ω_u^{(1)})=∏_{x∈S_u}ω_x`. Internal link contributions are scalar. Choose a joint eigenvector of the commuting boundary end actions; this fixes one phase. The matter configurations with `0,1,2,3` occupied points contribute `1,i,−1,−i`. A unital *-homomorphism cannot enlarge the image spectrum beyond the source spectrum, so all four appear in the coarse centre. A coarse star with scalar `ω` endpoint factors contributes a scalar times `{1,i}`. End-purity for `−1` alone does not imply this stronger condition: a direct sum of the trivial and vector representations has the same `−1` eigenvalue on both summands but different `ω` eigenvalues. □

**GAP and scope.** The draft omitted fine internal link-purity from its theorem statement. It also inferred scalar `ω` endpoint action from end-purity for `−1`; the trivial-plus-vector register above is a counterexample. Its result also does not apply to the owner's ZM1-I1[a] singleton embedding (`TOE_ASSEMBLY.md` §3.8); `|S_u|≥3` is a different proposed embedding. Theorem 3 applies to a law with all coarse links end-pure, not to each individual link; it does not prove that every coarse link of a moving-site law must be end-mixed. ZM1-I1[a] compares invariant observables. Theorem 6 shows that its comparison class can include odd singlets under SC-min; whether their correlations propagate is open. Under the hypotheses of Theorem 5(a), invariant observables are even. Any tail-matching conclusion also requires the explicit ZM1-I1[a] success conditions; see `ZM1_OBS.md` Lemma ER as cited in the assembly.

## 6. Prior evidence and remaining interpretation

`prior/CG16S.md` identifies #10027's fixed-finite-site obstruction and #10038's logged supplied-model site-count test in `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` (author statements for review). `LW1_5.md` Theorem SC already pins spinor-class discrepancy for its specified register setting. `LZ1.md` Theorems 2.1–2.2 already prove flat odd nodes for its original laws. `RCS1.md` Theorem 4 proves matter-evenness for its original laws; Theorem 6 shows why its hypotheses matter. The digest also records the subgroup and twisted-family operator results in `CH1.md` and `CH1_5U.md`, and the free-field limitation in `MT1.md`; none supplies a physical light chiral spectrum. The physical Standard Model subgroup target need not require an exact microscopic Spin(10) multiplet.

The draft's further literature list is contextual: arXiv:1806.09296, 1806.06868, 1306.1934, 2505.07900, 0910.3675, 1812.09183, 1311.4956, 1307.7726, 1805.10330, 1502.04368 and 1809.11171. The draft reports abstract searches, not independent verification here. Its references to Nielsen–Ninomiya, Friedan, Suslin, Swan, Bass–Heller–Swan, Atiyah–Bott and Pressley–Segal are expressly unverified; they carry no proof in this item. The draft's section 1 refers to a section 4.6 and Lemmas W and U, but its actual section 4 ends at 4.5. Those alleged proofs and any claims depending on them are not present and are not imported.
