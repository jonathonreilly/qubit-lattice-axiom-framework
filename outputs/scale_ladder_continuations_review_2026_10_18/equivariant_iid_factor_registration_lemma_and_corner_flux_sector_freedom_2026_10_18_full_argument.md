# Complete corrected argument: Finite flux sectors, local encoding dimensions and supplied registrations

This is inspectable mathematical source. The canonical claim is limited to: §§4–6 dimension, finite HNF/flux/Pauli calculations and explicit registration examples.

**Deferred continuation:** §§2–3 terminal registration/Bragg exclusions and downstream formation conclusions pending their packet; old5³ embedding is historical context, not a live premise. Complete arguments are retained below, but terminal negative conclusions are not promoted until the required residual-matched packet is supplied and reviewed. This does not make the exact identities uncertain. Historical verification statements below describe the original campaign, not a fresh capture or audit verdict.


# No equivariant factor of iid noise registers a coarse block lattice; the corner flux is a free sector label of its local fermionization

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Sections 2–5 are exact (proofs, or exhaustive finite certificates on stated tori). Section 6 is numerical. The registration lemma was restated and confirmed by a fresh-context checker of the same model family; nothing has been independently reviewed outside that family. Nothing is adopted.
**Provenance:** campaign block C6 of the 2026-10-18 scale-ladder campaign ("what takes rung 0, one qubit per site plus formation, to rung 1, the corner model?"). Worker and checker were agents of the same model family as the note writer. The note writer consolidated their scripts into one runner. A fresh-context review (same model family) corrected the note writer's first draft of §5.2.

## Result up front

**No map from rung 0 to rung 1 is derived.** The corner model's 12-corner graph, its π-flux background and its block embedding are all supplied, and its flux pattern was chosen to meet design targets.

1. **Registration lemma (exact, §2).** A measurable, translation-equivariant function of iid noise on Z³ cannot pick out one coset of a coarse sublattice Λ of index m ≥ 2. Nor can it pick a position in R³/Λ′ for any lattice Λ′ that does not contain Z³. So no local observable has a Bragg peak off 2πZ³. Finitarity is not needed: the lemma is the standard fact that Bernoulli shifts are mixing, and have no nontrivial rotation factor.
2. **Formation consequence (§3).** iid-priority formation with an empty start and a translation-covariant rule (the class of the B3 note) cannot register the coarse block lattice of the corner model. Both hypotheses are load-bearing, and two trivial controls show it. A translation-invariant finite-depth circuit applied to a translation-invariant product state cannot register one either.
3. **Density bound (exact, §4).** A corner site needs 12 qubits. A registered embedding has index m ≥ 12. The smallest O-invariant index ≥ 12 is 16, and an O-equivariant linear placement has index k³ ≥ 27. The corollary "no fine-translation-covariant encoding exists" is **not** proved.
4. **The flux is a free sector label (exact, §5).** Local fermionization (BKSF on the corner graph) admits every consistent flux configuration as a sector, in any fixed dictionary convention. That includes all 16 uniform patterns on even tori. The corner pattern is selected only by design targets: the targets select {1011, 1111} and leave the triangle free.
5. **Energetics does not select it (numerical, §6).** At the node filling ν = 1 the corner pattern ranks 15th–16th of 16 uniform sectors.

## 1. Setting and conventions

- **Noise.** Ω = S^{Z³} with S a standard Borel space, μ = ν^{⊗Z³} the iid product law, and the shift (T^v ω)_y = ω_{y+v}.
- **Factor.** X = Φ(ω) ∈ A^{Z³}, where Φ is measurable and Φ(T^v ω) = θ^v Φ(ω) μ-a.s., and θ is the shift on A^{Z³}. Finitary coding is **not** assumed.
- **Registration (Definition).** Let Λ ⊂ Z³ be a sublattice of index m. A *Λ-registration* is a measurable o: Ω → Z³/Λ with o(T^v ω) = o(ω) − v for all v ∈ Z³, μ-a.s. A *continuous registration* to a lattice Λ′ ⊂ R³ is the same with values in R³/Λ′.
  - If the coarse sites are a set C(X) ⊂ Z³, read off X measurably and equivariantly (C(θ^v x) = C(x) − v), and C(X) is a single Λ-coset a.s., then o := C(Φ(ω)) mod Λ is a Λ-registration.
  - The same holds whenever the coset can be recovered from X as an a.s. limit, for example by a majority vote over cosets in growing boxes. A crystal with a zero-density or sparse uncorrelated set of defects, whose majority coset converges, therefore defines a registration.
- **Corner model (context, supplied).** The model is the one of the corner-fermion qubit-code note (`docs/CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md`) and the long-wavelength note (`docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`).
  - **Graph.** The vertices are the 12 perpendicular direction pairs {d, e} at each site. The on-site edges are the cuboctahedron edges, and the links join {a, b}@v to {−a, b}@v+a. Every vertex has degree 6. Per site there are 12 vertices and 36 edges.
  - **Faces.** Per site there are 6 squares (about the C4 axes), 8 triangles (octants), 3 plaquettes and 12 edge tubes.
  - **Flux labels.** A uniform pattern is written as four bits (square, triangle, plaquette, tube), with 1 = π in the *u-convention* H = −t1 Σ_onsite u c†c − t2 Σ_links u c†c + iλ Σ_triangles, where u = ±1. The repo corner model is u-pattern 1011 at t1 = −1.
  - **Standard convention.** The *standard flux* of a face is arg ∏(−h_e) for the hopping matrix elements h_e, so all-negative real hops carry flux 0. In this convention the corner model is 1111 (§5.4).

## 2. The registration lemma (exact)

**Theorem 1 (no finite registration).** Let (Ω, μ, T) be the iid shift on Z³, or any stationary Z³ system whose action is mixing. Then no Λ-registration exists for any sublattice Λ of index m ≥ 2.

*Proof.* Put A_c := o^{−1}(c) for c ∈ Z³/Λ.

- The covariance gives T^{−v}A_c = {ω : o(T^v ω) = c} = {o = c + v} = A_{c+v} (mod null sets).
- Invariance of μ gives μ(A_{c+v}) = μ(A_c). Since Z³ acts transitively on the m cosets, μ(A_c) = 1/m for every c.
- For v ∈ Λ, T^{−v}A_c = A_c. Mixing, μ(A ∩ T^{−v}B) → μ(A)μ(B) as |v| → ∞, applied along v ∈ Λ, gives 1/m = μ(A_c ∩ T^{−v}A_c) → 1/m². So 1/m ∈ {0, 1}, which is impossible for m ≥ 2. ∎

The iid shift is mixing by the standard cylinder-set approximation. Only ergodicity of the Λ-subaction is used, for every Λ, so "totally ergodic" would suffice. A registration read off X is o′∘Φ, so it suffices to work on Ω. The law of X is itself a factor of a Bernoulli shift, hence Bernoulli (Ornstein; Ornstein–Weiss for Z^d). That fact is context and is not used in the proof.

**Theorem 2 (no continuous registration; no Bragg peaks off 2πZ³).** Let (Ω, μ, T) be weakly mixing, for example iid. Let Λ′ ⊂ R³ be a lattice.

(a) If Z³ ⊄ Λ′, there is no measurable o: Ω → R³/Λ′ with o∘T^v = o − v a.s. If Z³ ⊂ Λ′, every such o is a.s. constant.

(b) For every g ∈ L²(μ), in particular every bounded local function of X, the spectral measure of g − E g under the Z³ action has no atoms. Equivalently, for k ∉ 2πZ³ the averages |B_n|^{−1} Σ_{x∈B_n} e^{−ik·x} g∘T^x → 0 in L² over boxes B_n.

*Proof.*

(a) Let k ∈ Λ′* := {k : k·λ ∈ 2πZ for all λ ∈ Λ′}. Then f_k := e^{ik·o} is a well-defined unimodular L² function with f_k∘T^v = e^{−ik·v} f_k, so it is an eigenfunction. Weak mixing means the only eigenfunctions are constants, with eigenvalue 1 (Koopman–von Neumann). Hence e^{ik·v} = 1 for all v ∈ Z³, that is k ∈ 2πZ³, for every k ∈ Λ′*. So Λ′* ⊂ 2πZ³, which by duality says Z³ ⊂ Λ′. If Z³ ⊂ Λ′, then o∘T^v = o for every v, and ergodicity makes o constant.

(b) By the mean ergodic theorem for the Z³ unitary action, the averages converge to the projection of g onto the eigenspace E_k := {f ∈ L² : f∘T^x = e^{ik·x} f for all x ∈ Z³}. For k ∉ 2πZ³, weak mixing gives E_k = {0}. Atoms of the spectral measure are exactly the eigenvalues, and these are absent on L²₀. ∎

Theorem 1 is the special case Λ′ = Λ ⊂ Z³ of Theorem 2(a), but needs only mixing along Λ. Bernoulli shifts in fact have countable Lebesgue spectrum, which is stronger than (b); this is not needed. For the B3 class, Theorem 2(b) is weaker than the B3 note's entire structure factor (C2). Its point is that it holds for **every** measurable equivariant factor, with no coding-radius tail.

**Converse and inheritance.** Suppose an ergodic system is not weakly mixing. Then it has a nonconstant eigenfunction f with |f| = 1 and f∘T^v = e^{−ik·v} f for some k ∉ 2πZ³. This is an equivariant map to the circle on which v acts by rotation through k·v: a registration of the phase k·x. So the absence of all such phase registrations is equivalent to weak mixing. Factors of a mixing (weakly mixing) system are mixing (weakly mixing), so Theorems 1–2 hold verbatim for the law of X itself.

**What "registering" therefore cannot mean here.** Long-range positional order of a coarse lattice is excluded, including order with a sparse set of defects from which the coset is recoverable (§1). Local registration with a finite correlation length is allowed. Such configurations have no global coset and no Bragg peak.

## 3. Consequences

**Corollary 3 (B3-class formation).** Take B = ∅, jointly iid full site pairs (T,U), and a translation-covariant rule on Z³. Theorem 1 of the B3 note (`outputs/scale_ladder_continuations_review_2026_10_18/iid_priority_formation_finitary_factor_coding_radius_2026_10_18_full_argument.md`) makes X a (finitary) factor of iid noise. Theorems 1–2 then say that X registers no coarse block lattice: neither the 5Z³ blocks of the long-wavelength embedding, nor any index-m ≥ 2 sublattice, nor any non-integer period or offset.

**The hypotheses are load-bearing.** B3's Definition 1 allows both of the following, and each registers trivially (runner R3):

- (a) a deterministic periodic start slice, for example planted centres on 5Z³;
- (b) a position-dependent rule F_y that reads y mod 5, with coding radius 0.

In both cases the registration is supplied, not formed. A planted *finite* slice is forgotten away from it at the factorial rate (B3 Theorem 3), so it registers only a factorially thin layer.

**The flux background (interpretive remark, not a theorem).** The corner model's flux background is deterministic Z2 data, and a noise-blind rule can write it with coding radius 0. So B3 neither excludes it nor supplies it. On the fine lattice, though, writing per-face signs presupposes that the faces, and hence the coarse sites, are already placed relative to the fine sites. That needs a y-dependent, hence registering, rule, which lies outside Corollary 3's hypotheses. What B3 does exclude, from an empty start, is spontaneously selected background data, such as the sign of the chiral term. This holds under the symmetry condition of B3 §5 (C1): the label symmetry must commute with the rule and leave the full joint clock-mark law invariant; zero vector mean additionally needs a label action with no invariant vector.

**Corollary 4 (quantum analogue).** Let ψ = U φ^{⊗Z³}, where φ is a fixed one-site state. Let U be a finite product of D layers, each a product of commuting gates of range r, and each layer invariant under all Z³ translations.

- (i) ψ is translation invariant, so ⟨τ_x A⟩ does not depend on x: there is no Λ-periodic expectation pattern.
- (ii) By the strict light cone, ⟨AB⟩ = ⟨A⟩⟨B⟩ exactly whenever the supports of A and B are more than 2Dr apart. So ψ is mixing for every sublattice action, and it is not a nontrivial mixture of Λ-translates of one state.
- (iii) Consider a translation-invariant local measurement whose outcome projectors commute with each other and have range s. Its outcome field is a stationary (2Dr + s)-dependent random field, hence mixing, so Theorems 1–2 apply to it.

*Proof.* (i) and (ii) are the light-cone argument. In (iii), the outcome events in regions more than 2Dr + s apart are products of commuting projectors whose Heisenberg supports are disjoint, so they are independent. ∎ The runner checks (i) and (ii) exactly on a 12-qubit ring (R4); that is an illustration, not a proof.

**Not excluded.**

- Polycrystals: domain mosaics with local registration and no global coset.
- Defective or amorphous packings whose local order decorrelates (runner R1/R2 shows such packings).
- Fractional-translation encodings, in which a fine translation acts on the corner algebra as an automorphism that is not a coarse translation (open; §4).
- Corner fermions as emergent quasiparticles of a translation-invariant fine Hamiltonian. These escape the density bound because their modes are dressed and not a local subalgebra (open).
- Every route outside covariant empty-start formation: a supplied dictionary, deterministic periodic start slices, position-dependent rules, correlated or deterministic clocks, global conditioning, and spontaneous translation breaking in a ground state (a ground-state selection is not a factor of iid noise).

## 4. Dimension and density (exact)

**Proposition 5.** The even-parity algebra of n complex fermion modes is M_{2^{n−1}} ⊕ M_{2^{n−1}}. An injective unital *-representation must contain both summands, so it has dimension ≥ 2^n. On qubits it therefore needs at least n qubits.

Suppose a coarse model with 12 modes per coarse site is encoded in the one-qubit-per-site lattice so that, for every finite set A of coarse sites, the even algebra of their 12|A| modes acts faithfully on the qubits within distance r of A. Then a box of side ℓ holds at most (ℓ + 2r)³/12 coarse sites, and the coarse density is ≤ 1/12.

*Proof.* The algebra structure is standard. The runner checks dimension 2·(2^{n−1})² and a two-dimensional centre {1, parity} for n = 1…4 (D1). Apply this to 12|A| modes on (ℓ + 2r)³ qubits and let ℓ → ∞. ∎

**Corollary 6.**

- (a) A *registered* embedding has coarse sites c + Λ with index m ≥ 12.
- (b) The exhaustive Hermite-normal-form enumeration of all 22 528 sublattices of index ≤ 32 finds O-invariant indices {1,2,4,8,16,27,32}. Consequently the smallest O-invariant index ≥ 12 is 16, realized by 2·D3. The all-index P/F/I classification is not established by this finite enumeration and is deferred; the minimum statement uses only the exhaustive range below 16 and the explicit index-16 witness.
- (c) If the placement x ↦ c + Mx of the cubic coarse lattice is O-equivariant, M R = R M for all R ∈ O, then M = k·I by Schur (D4), and m = k³ ≥ 27.
- **(b) versus (c).** In (b) only the *set* Λ is O-invariant. The 2·D3 lattice is O-invariant, but its basis matrix M does not commute with O: M⁻¹RM is integral but differs from R. A placement through it therefore carries the coarse rotation R to a different fine rotation, not to R itself. If coarse rotations about a coarse site are to be the same fine rotations about the corresponding fine site, as in the long-wavelength embedding, (c) applies and the bound is 27.

The older long-wavelength note describes a 5³ placement. That historical placement/range claim is not used here; the newer9702 corrected embedding discussion remains authoritative for its own supplied construction. The density argument above does not require that placement.

**Not proved.** The earlier corollary "no fine-translation-covariant encoding exists" is not proved. An encoding in which a fine translation acts as a non-translation automorphism of the coarse algebra is not excluded: compare a translation-invariant chain blocked by 12. Proposition 5 constrains only the density of a registered embedding.

## 5. The corner flux is a free sector label (exact)

### 5.1 Cycle space and uniform patterns (A1)

On the L-torus, V = 12L³, E = 36L³, and there are 29L³ faces.

- **Faces span the cycle space.** rank(faces) = E − V + 1 − 3, and three straight noncontractible loops complete the cycle space. Certified for L = 3, 4 by default, and L = 6 with `--full`.
- **Even L.** Every face relation contains an even number of faces of each type, so all 16 uniform patterns are realized by gauge fields, with the fluxes re-measured.
- **Odd L = 3.** The only odd type-parity is (square, plaquette), coming from a wrapped relation. Only the 8 patterns with square = plaquette are realized there. This is a torus-size effect.
- **Non-uniform sectors.** A random gauge field gives a consistent, non-uniform configuration, so sectors are not unique.
- **Infinite lattice.** The 4-periodic lift of each L = 4 gauge field realizes the corresponding uniform pattern on every face of the infinite corner graph.

### 5.2 Local fermionization fixes no flux (A2, A3)

The Bravyi–Kitaev superfast encoding is tested on the L = 3 corner graph with an explicit Pauli algebra including phases, under three conventions: the canonical index order, and two random vertex orders and labellings.

- **Edge operators.** S_e = X_e ∏_{l <_i e} Z_l ∏_{l <_j e} Z_l. They anticommute exactly when the two edges share one vertex.
- **Loop data.** For a face C, ∏_{e∈C} S_e = i^q B_C, where B_C is a bare tensor-product Pauli string. Put κ_C := i^{|C|} (∏ε) i^q, with ε_{jk} = sign(label k − label j).
- **Sectors.** The signed loop stabilizer of flux F is g_C = F_C κ_C B_C. The sector with flux F has every g_C = +1. Per face type, F is the free sign of the corner-code note's i^n F ∏A.

The results (exact):

- **Convention dependence.** κ itself, the formal flux of the "all bare strings = +1" assignment, depends on the conventions: two random conventions differ on 375 of 783 faces. In the canonical convention κ is not uniform on every face type. This is an L = 3, index-labelling observation only. It does not rule out a special symmetric convention.
- **Identity.** In all three conventions, for every basis face relation r, ∏_{C∈r} κ_C = σ_r, where ∏_{C∈r} B_C = σ_r I. Hence the group generated by the g_C contains no −I exactly when F satisfies every face relation, that is exactly when F is a consistent flux configuration. The runner tests uniform 1011, 1111 and 0000 and a random consistent F; all of them exist in every convention, and a single flipped face does not.
- **One dictionary sign flip (A3).** S_e → −S_e preserves every algebraic relation and leaves every B_C unchanged. It flips κ on exactly the faces through e, so it relabels sectors by F → F·(−1)^{[e∈C]}. Sign flips act transitively on the consistent sectors *as relabellings*.

**On the "natural vacuum" reading.** The worker read κ as the flux of a "natural vacuum". That reading is convention-bound. In the three generic conventions tested, some basis relation has σ_r = −1 (12, 84 and 66 of 137). So the all-bare-+1 assignment is not a consistent sector there. Hop-sign flips alone cannot repair this, because they change neither B_C nor σ_r. The vertex orderings, however, are part of the convention, and they do change σ_r. On L = 3 the runner finds, by local search, a translation-invariant ordering in which every σ_r = +1. The review found such orderings, translation-invariant ones included, on L = 3 and L = 4. In that convention the all-bare-+1 assignment is a consistent sector, and hop-sign flips of it make uniform 1011, 1111 and 0000 each the bare sector. So the check's statement that every consistent configuration is "the bare sector of some convention" holds on the tested tori, once the convention includes the vertex orderings. An earlier draft of this note said the opposite; that was wrong, and the review corrected it. The headline is unchanged. In any one fixed dictionary, the consistent flux configurations, and only those, are exactly the sectors. Which one is "bare" is set by the dictionary. The flux is a free sector label.

**Scope.** The reading "F is the encoded fermion's flux" uses the standard BKSF loop relation with this κ normalization. The identity above is what that reading requires; it is not re-derived here at the level of fermionic states. The A4 statements below are made directly at the fermion level and do not depend on it.

### 5.3 What does select the pattern: the design targets (A4)

The runner builds the fermion-level projective symmetry group on L = 4 by BFS sign propagation on the signed adjacency, for all 16 uniform u-patterns. Results (exact):

- **The PSG exists for all 16.** Symmetry alone therefore cannot select the flux.
- **C4.** C4⁴ = −1, and likewise axis-C2² = −1, exactly when square = π.
- **Translations.** Tx and Ty commute exactly when square = plaquette; otherwise they anticommute.
- **Fixed momenta.** An O-fixed momentum exists, among patterns with commuting translations and C4⁴ = −1, exactly for tube = π.
- **Selection.** Three properties of the corner-code and long-wavelength notes are read here as design targets: C4⁴ = −1 (the spin-1/2-class target), commuting translations, and an O-fixed momentum (in the long-wavelength note's pattern). They select exactly **{1011, 1111}**, and the triangle is free.
- **1011.** It has exactly two O-fixed momenta, differing by (π, π, π): (π/2)(1, −1, 1) and its negative in this gauge. The form of these momenta is gauge dependent.
- **With square = 0.** An O-fixed momentum exists iff tube = 0.

This is target selection, not derivation.

### 5.4 Gauge-invariant statement in the standard convention

The u-pattern 1011 at t1 = −1, with either sign of t2 and λ = 0, has standard flux **π through every elementary face** of all four types. The control t1 = +1 gives standard triangle flux 0, so the sign of t1 is load-bearing.

With the chiral term (t1 = −1, λ = −0.5), every face carries the standard phase π + arctan λ · Σ_e σ_e, summed over its on-site edges. Here σ_e = +1 (−1) when the face runs along (against) the det > 0 orientation of the triangle containing e, since each on-site amplitude is u(1 + iλσ). The runner finds |Σσ| = 4 for squares, 3 for triangles, 0 for plaquettes and 2 for tubes. So the oriented triangles carry π + 3 arctan λ, the squares π ∓ 4 arctan λ (outward-oriented: −, per the C7 check), the tubes π ∓ 2 arctan λ, and the plaquettes π. Reversing a face flips the sign. An earlier version gave only the triangle phase; the square and tube shifts were added after the C7 check (`.claude/science/physics-loops/scale-ladder-campaign-20261018/C7_check/ (unavailable historical pointer; not a proof premise)`). Once λ ≠ 0, labels such as "1011" are u-convention labels, not gauge-invariant fluxes. Square = π forces λ = 0. This is "gauge-invariant in the standard convention", not "convention-free": the label depends on the hop-sign convention, as §5.2 shows.

## 6. Energetics does not select it (numerical)

Hop-only Hamiltonians commute with every loop stabilizer, so they are block diagonal over flux sectors (as for the static fluxes of Kitaev's honeycomb model). Each sector is a free-fermion problem. The runner's `--energetics` part uses the following:

- a Bloch 2³ supercell on a 6³ K-grid, which is effective L = 12;
- an exact cross-check against direct L = 4 real-space diagonalisation (E0);
- the diamagnetic inequality (E2);
- the particle–hole identity E(F, ν) = E(F with the triangle flipped, 12 − ν) (E3);
- gauge consistency, repo 1011 at t1 = −1 against standard 1111 (E4).

| ν = 1, standard convention (corner = 1111) | rank of corner | E(corner) − E(0000) per site |
|---|---|---|
| \|t1\| = 1, t2 = 0.2 | 15 / 16 | +1.854 |
| \|t1\| = 1, t2 = 1.0 | 16 / 16 | +1.514 |
| repo convention, t1 = −1, t2 = 0.2, λ = −0.5 (corner = u-1011) | 6 / 16 | +0.497 above the best (0110) |

At t2 = 0.2 the order of 0000 and 0010 is unresolved: they differ by 2·10⁻⁴, at the K-grid level.

**Campaign evidence not reproduced by this runner** (worker logs `c6_B.log`, `c6_B5.log`, `c6_B6.log`; restricted sectors; greedy search):

- **Descent at ν = 1.** Greedy single-edge descent over period-2 sectors drives squares and triangles to about 0, while plaquette (~0.4–0.6) and tube (~0.3) remain. Earlier wording said the descent "goes to near flux-free"; that was corrected by the check.
- **ν = 7, t2 = 1.** 1111 is the best *uniform* pattern but is unstable: 192 of 288 period-2 flips lower it, and a non-uniform sector lies 0.125 per site lower.
- **ν = 8, t2 = 0.2.** 1111 is a local minimum among single flips, but 1101 is 1·10⁻⁴ below it.
- **ν = 6, t2 = 0.2.** A non-uniform sector lies 0.78 per site below the best uniform one.

Hop dynamics conserves flux, so a sector chosen at random at formation would stay frozen.

**Scope.** Free fermions; uniform and period-2 sectors only; hop magnitudes only. Repetition sectors are not modelled. The Lieb and Macris–Nachtergaele flux-phase rule does not apply, because the corner graph is not bipartite: it contains triangles.

## 7. What this establishes and what it does not

- **Established (exact).**
  - Theorems 1–2 and Corollaries 3, 4 and 6, under their stated hypotheses.
  - The A1–A4 certificates on the stated tori, and their infinite-lattice lift for the uniform patterns.
  - The standard-convention statement of §5.4.
- **Established (numerical).** The ν = 1 ranking in §6, in uniform sectors.
- **Not established.**
  - That no other formation reading registers the blocks. Every evasion route in §3 remains open.
  - That fractional-translation encodings, or emergent corner quasiparticles, are impossible.
  - That no special symmetric BKSF convention exists.
  - Any interacting or many-body energetics.
  - Any selection of the flux, the dictionary, the block lattice or the formation rule.
  - Any physical identification.

## 8. Runner evidence

`python3 scripts/equivariant_iid_factor_registration_lemma_and_corner_flux_sector_freedom_2026_10_18.py`

- **Default:** `TOTAL: PASS=37 FAIL=0`, 11 s (the 36-check version took 22–27 s at load average about 10 on 4 cores).
- **`--energetics --full`:** `TOTAL: PASS=47 FAIL=0`. This adds the L = 6 A1 certificate and the E0–E5 energetics. It took about 50 s on an otherwise idle 4-core machine (earlier 45-check version) and 435–574 s under heavy CPU contention (405 s for the 46-check version; 24 s for the current 47-check version on a lightly loaded machine).
- Seed 20261018 in both cases.

The checks fall into four groups.

- **R (illustrations and controls; Monte Carlo and exact statevector).**
  - R1: an iid-priority block packing (range 4, empty start, covariant) has max_Q |S(Q)| = 0.12–0.19 at L = 40 (about 256 centres), below 4/√N_c ≈ 0.25, against 1 for a registered lattice.
  - R2: a radius-2 equivariant factor has √N_c · max|S| ≈ 2.0–2.3 from L = 20 to 80, and balanced coset frequencies (χ² over 124 dof).
  - R3: the two controls register with |S| = 1.
  - R4: on a 12-qubit TI circuit, uniform ⟨Z_x⟩ to 4·10⁻¹⁶, and connected ⟨Z₀Z_r⟩ = 0 to 2·10⁻¹⁵ for r > 4.

  These illustrate Theorems 1–2 and Corollary 4. They do not prove them.
- **D (exact).** The even-algebra structure for n ≤ 4; the HNF enumeration of O-invariant sublattices (indices {1, 2, 4, 8, 16, 27, 32}, one each); the smallest index ≥ 12 being 16; and the commutant of O being the scalars.
- **A (exact).** A1 on L = 3, 4 (and 6); the A2 algebra, convention dependence, the identity ∏κ = σ, sector existence, and the translation-invariant ordering with a consistent bare sector; A3; the A4 PSG, target selection, fixed momenta and the standard-convention statements.
- **E (numerical, `--energetics`).** E0–E5 as in §6. The rank checks are structural (rank ≥ 15 and excess > 1.5; with the chiral term, not lowest). The printed campaign values come from two earlier implementations, the worker's and the check's, and are reproduced to the printed digits.

The runner also prints an N5 execution certificate.

## Historical checking narrative (not fresh evidence)

A fresh-context agent of the **same model family** checked the C6 findings. It is not an independent human reviewer. Its code is new: its own corner geometry, a `galois` GF(2) solver, a BFS projective symmetry group and Bloch sums. It reported 23 PASS, 0 FAIL. Files: `.claude/science/physics-loops/scale-ladder-campaign-20261018/C6_check/ (unavailable historical pointer; not a proof premise)` (`REPORT.md`, `chk_A.py`, `chk_B.py`, `chk_C.py`).

- **Confirmed.**
  - The supplied-clause list, with two clauses added: the U(1)-twisted rotation realization W and the hopping family.
  - A1 on L = 3, 4.
  - A3.
  - A4, by a different PSG method; the PSG exists for all 16.
  - The "π through every face" statement for t1 = −1, λ = 0.
  - The ν = 1 energetics, to 5·10⁻⁵.
  - The dimension bound as a density bound.
  - The registration lemma, which it restated without finitarity, with the load-bearing hypotheses and controls.
  - The quantum version.
- **Corrections applied here.**
  - The registration lemma restated (§2).
  - "Formation cannot produce the coarse rung" restricted to covariant rules from an empty start (§3).
  - "No fine-translation-covariant encoding exists" withdrawn (§4).
  - The index bound m ≥ 12 limited to registered embeddings, with smallest O-invariant index ≥ 12 equal to 16.
  - The descent wording corrected (§6).
  - "Convention-free" replaced by "gauge-invariant in the standard convention" (§5.4).
  - The square and tube shifts under the chiral term added to §5.4, with a runner check (the earlier text gave only the triangle phase; an omission, not an error).
  - The canonical-BK observation marked weak (L = 3, non-covariant labelling).
  - "Most block-favouring" dropped from the packing illustration.
- **Review of this note** (fresh-context, same model family; `.claude/science/physics-loops/scale-ladder-campaign-20261018/NOTE_C6_review/ (unavailable historical pointer; not a proof premise)`). Its verdict was "needs changes". It used new code, `rev_A2*.py` and `rev_D.py`, importing nothing from the runner. It confirmed Theorems 1–2, Corollaries 3, 4 and 6, the κ = σ identity and the sector statement, and the D enumeration. It found the note writer's first-draft §5.2 "correction" false as stated: vertex orderings exist, translation-invariant ones included, on L = 3 and L = 4, in which the all-bare-+1 assignment is consistent. So the check's "bare sector of some convention" statement stands on the tested tori. §5.2 and the runner now say this. The other changes in this revision are precision edits from that review.
- **Provenance of this runner.** The note writer consolidated it: the worker's geometry and GF(2) solver, the checker's BFS PSG idea, and new A2 identity/sector checks, D2–D4 and R4. It is not an independent implementation of the worker's A1, A3 or E code. The independent implementations are the checker's files above.

## Prior art and actual contribution

- **Known.**
  - **Ergodic theory.** Bernoulli shifts are mixing, and weak mixing excludes nonconstant eigenfunctions (Koopman–von Neumann); see for example Walters, *An Introduction to Ergodic Theory* (1982). Factors of Bernoulli shifts are Bernoulli (Ornstein, Adv. Math. 1970; Ornstein–Weiss, J. Analyse Math. 48, 1987, for amenable groups). Theorems 1–2 are the statement that a Bernoulli Z³-shift has a trivial Kronecker factor, written for the registration question.
  - **Finitary factors.** The language of finitary factors of iid noise is that of Holroyd–Schramm–Wilson (Ann. Probab. 45, 2017).
  - **Fermion–qubit encodings.** Bravyi–Kitaev (Ann. Phys. 298, 2002, the superfast encoding with loop constraints); Ball (PRL 95, 2005); Verstraete–Cirac (J. Stat. Mech. 2005); Chen–Kapustin–Radičević (Ann. Phys. 393, 2018) and Chen–Kapustin (PRB 100, 2019), where the encoded fermion's background is a choice tied to the dictionary.
  - **Emergent fermions and static flux sectors.** Levin–Wen (PRB 67, 2003); Kitaev (Ann. Phys. 321, 2006); O'Brien–Hermanns–Trebst (PRB 93, 2016) for 3D Kitaev models.
  - **Flux phase.** Lieb (PRL 73, 1994); Macris–Nachtergaele (J. Stat. Phys. 85, 1996).
  - **Projective symmetry groups.** Wen (PRB 65, 2002).
  - **Finite-depth circuits.** Light-cone clustering of finite-depth circuits is standard.

  These references are recalled. They were not re-verified in this session.
- **New here (application and certificates, not new mathematics of ergodic theory).**
  - The registration question for the scale ladder is put in exact form, with the load-bearing hypotheses and controls.
  - The density bound is specialised to the corner model: index ≥ 12, O-invariant ≥ 16, O-equivariant linear ≥ 27.
  - Exact finite certificates show that the corner model's flux is a free BKSF sector label in any fixed convention, including the κ = σ identity, sector existence for exactly the consistent F in any fixed dictionary, and a translation-invariant ordering whose bare sector is consistent, so that which F is "bare" is a dictionary choice.
  - The design-target selection {1011, 1111}.
  - The ν = 1 ranking.

## Historical packet proposal (promotion deferred)

- **N1 — routes, with markers.** The negative claims are (i) "no registration from covariant empty-start formation or from any equivariant factor of iid noise" and (ii) "local fermionization does not fix the flux, and ν = 1 energetics does not select it". Five distinct routes to the coarse rung were considered:
  1. **Equivariant factors of iid noise, including all of B3 with B = ∅.** ATTEMPTED; closed by proof (Theorems 1–2).
  2. **TI finite-depth circuits from TI product states.** ATTEMPTED; closed by proof (Corollary 4).
  3. **Local fermionization fixing the flux.** ATTEMPTED; closed by exact certificates (A1–A3): every consistent F is a sector in any fixed convention.
  4. **Symmetry selecting the flux.** ATTEMPTED; the PSG exists for all 16 patterns (A4), so symmetry does not select. Only the stated design targets select {1011, 1111}.
  5. **Energetics selecting the flux.** ATTEMPTED; numerical, free fermions, uniform sectors only. Not closed beyond that scope.

  Routes **not** closed, and outside the claims: fractional-translation encodings; emergent quasiparticles of a TI fine Hamiltonian; correlated clocks; global conditioning; spontaneous translation breaking in a ground state; a supplied dictionary; interacting energetics; a special symmetric BKSF convention.
- **N2 — walls.** The supplied clauses are the corner graph, the flux, the hop family, the twist W and the block embedding. They are listed as supplied, not as independent walls. Closing the registration question would not supply the flux, and conversely.
- **N3 — hidden conditions.** The word "registered" is defined (§1), and §4 restricts it to registered embeddings. The word "background" (flux background) means static supplied data, and that is stated. "Standard convention" is defined in §1. Measurability and equivariance of the factor are explicit hypotheses.
- **N4 — residual matching.** The B3 note is cited only for "empty start plus covariant rule gives a factor of iid noise" (its Theorem 1), and for forgetting of the start slice (its Theorem 3); these residuals match. The corner-code and long-wavelength notes are cited only for definitions, design targets and historical embedding context; no 5³ placement/range premise is used.
- **N5 — wording.**
  - "Registers" means a measurable equivariant coset or position choice, not local order.
  - "Free sector label" means every consistent configuration is a nonempty code sector on the stated tori, and every uniform one on the infinite lattice.
  - "Ranks near last" applies to uniform sectors at ν = 1 only.
  - The runner's N5 certificate lists the resolutions actually exercised.
- **N6 — partial-closure paths.** A supplied dictionary, or an owner-approved block-lattice primitive, would close the registration gap by premise rather than by derivation. Neither is adopted here. Each would be a new premise requiring owner approval.
- **N7 — steelman.** A hostile reviewer would say: "a fine-translation-covariant encoding, in which fine translations act on the 12-mode algebra by a non-translation automorphism, or an emergent corner fermion of a TI fine Hamiltonian, needs no registration at all. The lemma then misses the physically relevant route." This is correct, and it is out of domain. Both are listed as open, and nothing here excludes them. The terminal obligation for the first is to construct, or rule out, a locality-preserving TI encoding of the corner algebra at density 1/12.
- **N8 — cross-cycle echo.** This is consistent with the B3 note's conclusion that infrared content must be supplied, and with the long-wavelength note's statement that a uniform one-qubit rule producing the blocks is open. Neither is changed.

## Historical execution record (not a fresh capture)

```bash
python3 scripts/equivariant_iid_factor_registration_lemma_and_corner_flux_sector_freedom_2026_10_18.py
python3 scripts/equivariant_iid_factor_registration_lemma_and_corner_flux_sector_freedom_2026_10_18.py --energetics --full
```

Expected: `TOTAL: PASS=37 FAIL=0` (under 30 s; about 8 s of it is the A2 ordering search), and `TOTAL: PASS=47 FAIL=0` (about 1 min idle; 435–574 s under CPU contention). Requires numpy and scipy.

## Load-bearing sources and context

- iid-priority formation note (B3) (`outputs/scale_ladder_continuations_review_2026_10_18/iid_priority_formation_finitary_factor_coding_radius_2026_10_18_full_argument.md`) (upstream; Theorems 1 and 3 used).
- Corner-fermion qubit-code note (`docs/CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md`) (context: the supplied model, its default and design-target fluxes, and the PSG).
- Corner-fermion long-wavelength note (`docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`) (context: tube = π, the O-fixed momentum, and historical embedding context only, not a placement/range premise).
- Campaign evidence: `.claude/science/physics-loops/scale-ladder-campaign-20261018/C6_rung0_to_rung1/ (unavailable historical pointer; not a proof premise)` (worker) and `.../C6_check/` (check).
