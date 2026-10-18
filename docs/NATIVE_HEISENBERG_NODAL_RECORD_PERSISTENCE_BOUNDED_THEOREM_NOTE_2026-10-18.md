---
claim_id: native_heisenberg_nodal_record_persistence_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "For the supplied homogeneous nearest-neighbour Heisenberg model and stated encoded preparations, exact invariant sectors preserve pure local qubit rays on mirror planes while other physical qubits evolve nontrivially. Results comprise finite periodic one-excitation sectors, a self-adjoint positive-bond dynamics on the finite-excitation representation over Z3 with exact odd half-space and orthant intertwiners, an explicit nonstationary two-excitation code on C4 x C_L x C_M for even L>=6 and M>=3, and an actual-Z3 correlated persistence sector for every finite excitation number with a self-adjoint direct-sum extension. Physical Record admissibility, formation, Hamiltonian selection, preparation, readout, noise robustness and the earlier arbitrary-input operation remain unsupplied."
upstream_dependencies: []
runner: scripts/native_heisenberg_nodal_record_persistence_2026_10_18.py
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact persistence under explicitly supplied dynamics and encoded preparation; no derivation of those physical premises."
target_claim_id: null
target_blocker_text: "Connect the constructions to native dynamics and remove supplied physical assumptions."
source_of_blocker_text: user_goal
next_trace_action: "Establish a native preparation or formation interface for the encoded sectors."
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
artifact_role: theorem
bare_retained_allowed: false
audit_required_before_effective_retained: true
---

# Native Heisenberg evolution preserves plane records in explicit moving sectors

**Type:** bounded_theorem. **Status:** proposed_retained; actual current surface is conditional-support, unaudited. This is an author proposal for the bounded conditional theorem, not a retained physical identification. Selective checks are identified below.

A homogeneous nearest-neighbour qubit Hamiltonian can preserve specified local pure states without repeatedly projecting onto them. This note exhibits exact invariant sectors with that property and nontrivial remaining motion. The sectors require specially encoded preparations. They are not the full space of arbitrary states outside the fixed planes.

The one-excitation result uses standard magnon and reflection identities; no historical novelty is claimed for them. The contribution is an explicit persistence interface, its complete physical output and actual infinite-lattice domain. The coordinate-antisymmetry many-magnon mechanism used below is established work, explicitly attributed in section4A; no new general many-body solution is claimed. Nothing here selects a physical Hamiltonian, forms a Record, prepares the encoded input, derives readout probabilities, or implements the earlier arbitrary-input operation W.

## 1. Premises and the persistence interface

Supply ordinary qubit tensor composition, Schrödinger evolution under the displayed Hamiltonian, and a common pure one-qubit ray q with a chosen perpendicular vector. Write these as up and down. Uniform internal rotation changes q without changing any Heisenberg bond. The selected model belongs to the J family of the current covariant-generator source; K=D=0 is a supplied choice, not a theorem of the minimal axioms.

On a finite simple cubic torus G, let

    H_raw=J sum_{edges {v,w}} sigma_v.sigma_w, J nonzero,
    E0=J|E|=3JN, N=|G|.

All ordinary nearest-neighbour edges have the same coupling. The all-up product Omega has energy E0. No extra edge, onsite pin, bath, observation cadence or auxiliary physical factor is supplied. Coordinates called encoded inputs below are a mathematical parametrization of subspaces of these same physical qubits.

The persistence statement concerns an isometry B and an explicit self-adjoint H_eff satisfying

    H B=B H_eff,   P_R B=B,                               (1)

where P_R fixes the plane qubits to q and is identity on the others. The conclusion is

    exp(-itH)B=B exp(-itH_eff),
    P_R exp(-itH)B=exp(-itH)B                              (2)

for all real t. Every physical output factor is retained in (2). The equations extend by identity on every passive reference, and hence apply to arbitrary encoded states, mixtures and reference entanglement.

For the framework interpretation, additionally supply that these initial fixed rays are law-admissible Records. The mathematics then establishes their persistence in the stated sector. Pure-state factorization alone does not establish admissibility, an event of formation, empirical readout or the meaning of a physical Record. Without that bridge, (2) is a theorem about fixed local qubit rays.

The older Record-field and compass-carving notes assumed permanence through PHP. This note replaces that mechanism only inside its explicit invariant sectors. It does not validate the old arbitrary-live-input compression as an autonomous evolution, and does not transplant its conclusions to the compass carving.

## 2. Finite one-excitation theorem

Let

    G=C_(2m) x C_Ly x C_Lz,
    m>=2, Ly>=3, Lz>=3,
    R={x=0 or x=m}.

The stated sizes make the ordinary periodic nearest-neighbour graph simple and degree6. Let |v> be the physical configuration with one down spin at v and all other spins up. Since sigma.sigma=2 SWAP-I, the one-excitation space is invariant. On that space the exact full Hamiltonian is

    H_1=E0 I-2J L_G,                                     (3)

where L_G=6I-A_G. Indeed, each of the six unlike-spin incident bonds changes the vacuum diagonal by -2J and exchanges the flip with amplitude +2J. Thus the full diagonal is E0-12J, with hopping +2J to every neighbour. All other bonds retain their vacuum energy; E0 is not dropped from the physical unitary.

Reflection F:(x,y,z)->(-x,y,z) is an automorphism of this actual graph, and homogeneous H commutes with its site permutation. This does not posit a new improper-rotation axiom. Its odd one-excitation sector consists of amplitudes

    f(-x,y,z)=-f(x,y,z).

They vanish on both fixed planes and remain odd forever.

More explicitly let the encoded Hilbert space be l2({1,...,m-1} x Z_Ly x Z_Lz). Define V by putting f/sqrt(2) on this strip, its negative mirror on x=m+1,...,2m-1, and zero on R. The two supports are disjoint, so V is an isometry. Define

    L_D=6I-A_{path(m-1)}-A_{C_Ly}-A_{C_Lz},

with each adjacency acting on its own coordinate. Its boundary diagonal remains6; it is not the degree-reduced graph Laplacian of the strip. At x=0,m the two incident amplitudes cancel, at x=1,m-1 the missing neighbour amplitude is zero, and at interior sites the ordinary hopping identity holds. These cases prove

    H_raw V=V(E0 I-2J L_D).                              (4)

Every plane qubit is therefore exactly q for all time and all encoded inputs. The code dimension is (m-1)LyLz. Its Laplacian eigenvalues are

    2[1-cos(pi l/m)]+2[1-cos ky]+2[1-cos kz],
    l=1,...,m-1,
    ky=2pi a/Ly, kz=2pi b/Lz.                           (5)

Distinct eigenvalues occur for every allowed size, including m=2, so the sector supports nonstationary superpositions. The vacuum can be adjoined as a separate invariant line with energy E0. For a superposition of vacuum and excited code, retain the direct-sum effective Hamiltonian and their actual relative phase.

## 3. Actual Z3 dynamics and infinite-plane theorem

For the infinite lattice use the actual **positive bond model**

    H_pos=j sum_{nearest-neighbour e}(I-sigma_v.sigma_w)
         =2j sum_e(I-SWAP_e), j>0.                      (6)

The supplied representation is the incomplete tensor product around the common q vacuum. An orthonormal basis is |S>, with S any finite subset of Z3, and the Hilbert space is the direct sum of H_n=l2({S:|S|=n}), n>=0. This representation and background are premises, not a derivation of a thermodynamic phase.

On |S>, only edges with exactly one endpoint in S contribute. A crossing edge gives 2j(|S>-|S triangle {v,w}>). On the n-excitation sector this is 2j L_n, the Laplacian of the configuration graph whose vertices are n-element subsets and whose edges move one occupied vertex to an adjacent unoccupied vertex. Its degree is at most6n.

For finitely supported amplitudes,

    <f,L_n f>=sum_{unordered configuration edges {S,T}}
                                      |f(S)-f(T)|^2.

The bound |a-b|^2<=2(|a|^2+|b|^2) gives 0<=L_n<=12n I. Equivalently the adjacency and degree operators each have norm at most6n. Thus H_n=2jL_n extends to a bounded positive self-adjoint operator with norm<=24jn, and H_0=0.

Define

    D(H_pos)={psi: sum_n ||H_n psi_n||^2<infinity},
    H_pos psi=(H_n psi_n)_n.                            (7)

The blockwise inverses (H_n+/-i)^-1 have norm<=1, and H_n(H_n+/-i)^-1 also has norm<=1. Their direct sums map into (7) and invert H_pos+/-i. This proves self-adjointness; positivity is sectorwise. The unitary group is the direct sum of exp(-itH_n).

Finite linear combinations of configurations form an operator core. First truncate the sector sum, which converges in graph norm by (7); then approximate in each retained sector by finite-support vectors, using bounded H_n. Finite spatial support is not claimed to persist under finite-time evolution.

This construction realizes the declared local interactions. Any local spin operator A preserves the finite-configuration core, where

    [H_pos,A]=sum_{e meeting supp A}[2j(I-SWAP_e),A].     (8)

All other bonds commute with A. The right side is a finite bounded sum. For graph-core approximants psi_k to psi in D(H_pos), A psi_k and H_pos A psi_k converge by (8). Closedness then shows A psi belongs to D(H_pos), with the same commutator identity there. No formal subtraction of two divergent infinite sums is needed.

At n=1, H_1=2j L_Z3 is bounded by24j. The odd subspace under x->-x is reducing. Let V_infty take l2(x>=1) to its normalized odd extension across x=0. The same coefficient check as above gives

    H_pos V_infty=V_infty 2j L_D,infty,                  (9)

where L_D,infty has diagonal6, hopping -1 among half-space neighbours, and no edge through x=0. At x=1 the diagonal is still6. The map includes both reflected physical packets; neither is traced out. Boundedness extends the identity from finite support to all l2 inputs and exponentiates for all real t. Include vacuum as an orthogonal code line of energy0 if desired.

Every plane-site local projector onto q acts identically on this code and its evolved image. Hence every finite subset of x=0 has a pure product q reduced state, uncorrelated with the remaining system and any passive reference. This is the meaning of infinite-plane factorization here; no infinite product is asserted to be a local observable. All encoded l2 inputs already have bounded energy and second energy moment because H is bounded on this code. Finite-support half-space packets exhibit genuine propagation to their neighbours.

One can impose oddness under two or three commuting coordinate reflections. Extend from an orthant with sign equal to the product of reflected coordinate signs and normalization2^(-k/2). Every fixed coordinate plane remains q; the effective orthant operator again has diagonal6 and hopping -1. This is the same construction with additional nodal boundaries.

**Energy convention.** On a finite graph,

    H_pos=j|E|I-j sum_e sigma_v.sigma_w.

This explicit affine relation transfers invariant-subspace conclusions, with its scalar retained in any coherent output comparison. In infinite volume the raw unshifted vacuum energy diverges. Equation (6) defines the vacuum-zero positive model in the stated representation; it is not asserted equal to a divergent raw sum minus a finite scalar. No absolute phase or energy calibration from an earlier engineered compiler is imported. Arbitrary thermal or finite-density representations outside this construction are not covered.

## 4. A nonstationary two-excitation theorem

Return to the finite raw Hamiltonian on

    G=C_4 x C_L x C_M,
    L even, L>=6, M>=3,
    N=4LM, E0=12JLM, R={x=0 or x=2}.                    (10)

At each transverse cell i=(y,z), the two live sites x=1,3 form a mirror pair. Define normalized states on these physical qubits

    t_i=|up up>,
    s_i=(|down up>-|up down>)/sqrt(2).

Write |i,j> for singlets at two distinct cells i,j, t at all other live cells, and q at every record-plane site. It has exactly two physical spin flips. Define an encoded isometry B from C^M tensor C^M by

    B|z,w>=(1/sqrt(L)) sum_(y mod L) (-1)^y
                                |(y,z),(y+2,w)>.        (11)

For L>=6, an unordered occupied-cell pair has a unique orientation with forward row separation2: reverse identification would require 4=0 modulo L. Different (y,z,w) therefore give orthogonal physical configurations, proving that B is an isometry. The logical coordinates z,w are ordered by that orientation; no distinguishable extra particles are postulated. The two occupied cells never neighbour each other, even when z=w.

**x bonds.** All four x bonds at cell i sum to

    J(sigma_(0,i)+sigma_(2,i)).(sigma_(1,i)+sigma_(3,i)).

The live sum annihilates s_i. On t_i with the record sites up, these four bonds have their unchanged total energy4J. Each singlet therefore changes x energy by -4J with no record transition. The two singlets give -8J. Record–record transverse bonds retain their J vacuum contributions.

**Transverse bonds.** For adjacent transverse cells,

    h_ij=J[sigma_(1,i).sigma_(1,j)+sigma_(3,i).sigma_(3,j)].

Direct SWAP action gives the full physical identities

    h_ij|t,t>=2J|t,t>,
    h_ij|s,t>=2J|t,s>,
    h_ij|t,s>=2J|s,t>.                                 (12)

An adjacent |s,s> need not stay in the t/s span. It does not occur as an input term in (11). Each singlet has four distinct incident transverse edges, so the two have eight edges with one s and one t endpoint. Relative to the vacuum, (12) gives -16J on the diagonal and singlet hopping amplitude2J. Thus for each term in (11), the full action is

    (H_raw-E0)|i,j>=-24J|i,j>
                 +2J sum_(i'~i)|i',j>
                 +2J sum_(j'~j)|i,j'>.                 (13)

All record factors remain present in this identity. Some y hops create adjacent-singlet amplitudes; these must cancel before invariance follows.

Put W_d(z,w)=sum_y(-1)^y |(y,z),(y+d,w)>. The first singlet's +y hop on W_2 is -W_1 after reindexing; the second singlet's -y hop is +W_1. The first singlet's -y hop is -W_3; the second's +y hop is +W_3. Even L preserves the sign at wraparound. These are physical-vector cancellations, so they remain valid when W_3 has redundant descriptions at L=6. Every y hop, including the dangerous W_1 amplitude, cancels.

z hops retain (11). With A_M the simple cycle adjacency,

    H_raw B=B H_2,
    H_2=(E0-24J)I+2J(A_M tensor I+I tensor A_M).          (14)

This exact intertwiner proves all-time invariance and the complete physical output identity (2). In the positive-bond convention on the same finite graph, the corresponding effective operator is

    H_2,pos=24j I-2j(A_M tensor I+I tensor A_M).

The raw-code eigenvalues are

    E0-24J+4J[cos(2pi a/M)+cos(2pi b/M)].                (15)

They are not all equal for M>=3 and J nonzero. Arbitrary M^2-dimensional encoded superpositions therefore support nontrivial motion, including arbitrary reference entanglement, while every plane qubit remains exactly q. The surviving coordinates have noninteracting effective motion. No interacting-matter or arbitrary-density theorem is implied.

## 4A. Actual-Z3 persistence for every finite excitation number

The coordinate-antisymmetry mechanism is established: Bibikov, [Bethe ansatz for two-magnon scattering states in 2D and 3D Heisenberg-Ising ferromagnets](https://arxiv.org/html/1705.04117), section7.3, equations192–195, constructs multi-magnon products with a positive even number of antisymmetric coordinate factors. That mechanism cancels adjacent-pair terms. We specialize it to normalizable inputs with individual x oddness, and prove the physical embedding, domains and fixed-plane interface directly. The cited section was read; the full paper was not independently reviewed. This attribution is not an imported theorem dependency for the proof below.

For fixed n>=1, reorder the ordered-particle Hilbert space l2((Z3)^n) as l2(Z_x^n) tensor l2(Z_y^n) tensor l2(Z_z^n). Let h_o be the closed odd subspace of l2(Z) under x->-x. Set

    C_n = wedge^n(h_o) tensor wedge^n(l2(Z)) tensor Sym^n(l2(Z)).

Exterior and symmetric powers carry their usual normalized subspace embeddings into ordered tensor powers; there is no extra Fock carrier. Reorder coordinates back to positions. Under a simultaneous permutation pi of the particle labels, the x and y factors each acquire sign(pi), while z is unchanged. Their product is invariant. Hence every vector in C_n is a bosonic ordered wavefunction.

It vanishes when any two x coordinates coincide or any two y coordinates coincide. Every collision and every nearest-neighbor pair has at least one of these equalities. It also vanishes if any x coordinate is0, since every x tensor factor is odd. These statements hold by continuous evaluation on the discrete l2 basis, not by a pointwise convention on continuum representatives.

Define the map B_n to the physical n-spin-flip configuration space by

    (B_n f)({v_1,...,v_n}) = sqrt(n!) f(v_1,...,v_n).

The value is ordering independent. Collision amplitudes are zero and each distinct unordered configuration has n! ordered representatives, so B_n is an isometry. Its range is closed.

The free ordered operator is K_n=2j sum_i L_Z3^(i), bounded positive with norm<=24jn. Separability of the cubic Laplacian means it is the sum of the x, y and z coordinate Laplacians. The x sum preserves the exterior power of h_o; the y sum preserves its exterior power and the z sum its symmetric power. Thus C_n is reducing for K_n, and K_n f has the same collision, adjacent-pair and plane zeros.

On a distinct configuration S, let a(S) count its occupied nearest-neighbor edges. The actual crossing-edge degree is6n-2a(S). The physical full-spin H_n=2jL_config has diagonal2j[6n-2a(S)] and amplitude -2j for each allowed one-particle move. In the free formula the diagonal is12jn; forbidden moves land on collisions, where f is zero. Consequently, on collision-free symmetric wavefunctions,

    H_n B_n f = B_n K_n f - 4j a(S)(B_n f)(S)

where the last expression denotes multiplication in the configuration basis. For f in C_n, that last product is zero because every adjacent-pair configuration has zero amplitude. Therefore

    H_n B_n = B_n (K_n restricted to C_n).

The equality extends from finite-support determinant tensors to all of C_n by boundedness. Exponentiation proves the complete physical output identity for every real time and every encoded input/passive reference. Every plane qubit x=0 remains q; finite subsets factor as pure products from the full remainder. No projected generator is applied.

The construction is nonzero for every finite n: take x factors delta_k-delta_-k for k=1,...,n, y factors delta_0,...,delta_(n-1), and all z factors delta_0. Antisymmetrize x and y and normalize. The physical seed has2^n n! configurations, each with equal magnitude. These are finite-support states. Their K_n action has nonzero z-hopped amplitudes outside the initial support, so they are not eigenvectors; actual motion is nontrivial. No thermodynamic limiting sequence or nonnormalizable plane wave is required.

One may take the Hilbert direct sum over n, including vacuum. Each range reduces the bounded H_n, hence the direct sum reduces the previously defined self-adjoint H. Its operator domain is the inherited condition sum_n||K_n f_n||^2<infinity. The condition sum_n n^2||f_n||^2<infinity is sufficient, not necessary. All-time unitary persistence holds on every normalizable direct-sum input, while finite energy moments require their corresponding domain conditions. This is not a finite-density thermodynamic representation or generic many-body initial state.

This sector's effective motion is free subject to strong coordinate correlations. It removes the finite periodic geometry and restriction to at most two excitations from this construction, not the supplied H, its scale, polarized representation or specially correlated preparation. It does not establish interacting matter, Record formation, readout, robustness, autonomous loading, halt or a previous compiler interface. Scalar conventions remain those of the actual positive-bond infinite model, not a finite subtraction from a divergent raw Hamiltonian.

The independent check in the publication packet reconstructs normalization, domains and the full intertwiner. Separately authored sparse ordered-versus-unordered controls on actual Z3 agree through two generator actions for n=1,2,3. No periodic truncation is used. These fixtures do not replace the all-n proof above.

## 5. Counterexamples and exact scope

**Global reflection oddness at two excitations is insufficient.** On C_6 x C_3 x C_3, let a=(1,0,0), b=(1,1,0), and prepare (|a,b>-|Fa,Fb>)/sqrt(2) with all other spins up. Initially the two fixed planes contain no flip. A single full H_raw action moves either flip to x=0, yielding four distinct plane-occupied configurations, each of amplitude magnitude2|J|/sqrt(2). The squared first-action plane leakage is8J^2. Hence the one-excitation argument cannot be extended by parity alone. This does not contradict the stronger singlet/staggered preparation (11).

**An instantaneous boundary kernel is not an invariant code.** Every product of t/s mirror cells initially annihilates the plane-flip coupling, but live-layer interactions can move it out of that kernel. The exact finite controls retain the adjacent-singlet input |s_(0,0)s_(1,0)>. Its first-action plane leakage vanishes, whereas its normalized squared second-action leakage is256 at J=1 on each listed two-excitation fixture. Thus checking only P_R H psi=H psi is not enough; the full orbit must stay in the kernel. This exact fixture is implementation evidence for the stated input, not a classification of dark many-body states.

**Preparation and geometry are load-bearing.** Removing (-1)^y from (11) makes the two y-hop routes add. The n=2 theorem assumes L even and at least6; L=4 needs a different orientation/normalization analysis, and odd L loses the staggered periodic cancellation. Generic products of the two-excitation codes are not asserted invariant because collisions can introduce adjacent singlets.

No nonzero spectral gap isolating these codes from all other states is established. Exact symmetry and encoded preparation supply the invariance. In the one-excitation setting odd sine and even cosine modes can share energies, so a gap must not be inferred from the word protected. Generic symmetry-breaking perturbations, unrestricted initial live states, reset, autonomous loading and permanent halting protocols remain outside the theorems. These explicit failures delimit particular attempted extensions; they do not constitute a universal physical no-go.

## 6. Evidence, independence and provenance

The current repository baseline inspected for this work is `584755767deb8dfb670f07211d8446873fd0999b`. The candidate J-family classification and the Record-field/carving distinction were read from their primary notes. The derivations above are self-contained for the native persistence claims; no compression-based Majorana gap is a premise.

The finite one-excitation proof received a separate root analytical check. Before reading the full proposed proof, root implemented exact physical spin exchange and compared every odd column against a separately assembled Dirichlet/periodic Laplacian on4x3x3,6x3x3,8x3x3, covering9,18,27 columns. The raw Hamiltonian and the positive implementation are related by the explicitly stated scalar/sign convention. The two-excitation proof received a distinct root analytical check and exact full-spin implementation after the mechanism was described but before the full argument was read. Both author and root checked all encoded columns, normalization and orthogonality on4x6x3,4x8x4,4x10x3, with code dimensions9,16,9. The unstaggered and adjacent-singlet failures are preserved.

The infinite-lattice proof received a separate analytical check of its domain, core, local commutators, boundary diagonal, complete output and representation limits. Finite controls do not prove its infinite-dimensional statements. The check also supplies the local-operator domain-preservation argument included above.

These are source-exposed, same-selected-model checks with shared research context, not blind/model-diverse physical evidence. Re-running them or counting their predicates grants no audit status. Current primary execution and final publication review are recorded in the publication packet REVIEW_HISTORY.md; any eventual formal audit remains separate. No numerical simulation of a thermal phase or practical apparatus is claimed.

Bounded main-source searches for nodal-plane, dark-plane, reflection/excitation and Heisenberg/record variants are saved in PRIOR_ART_SEARCH.json. They did not locate a matching native persistence theorem in the searched source. This is not exhaustive literature novelty verification; the underlying one-magnon/reflection identities are standard and no novelty claim is made.

### Source and recovery references for this draft

Repository primary sources, all at the baseline above:

- `docs/MINIMAL_AXIOMS_2026-06-29.md`: framework language; does not select H, formation or preparation.
- `docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md`: the supplied candidate family and exact SWAP identity.
- `docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md`: compression as a supplied D-perm mechanism.
- `docs/DYNAMICS_CLAUSE_RECORDS_CARVE_KITAEV_MODELS_AT_THE_COMPASS_POINT_ZERO_FIELD_CARVINGS_ARE_CUBES_AND_TUBES_BOUNDED_THEOREM_NOTE_2026-09-24.md`: context for the distinct compass-carving target, not a proof input here.

Original working sources and actual selective checks are preserved in the branch-local publication packet:

- [Finite native route and proof](../.claude/science/physics-loops/native-nodal-persistence-20261018/NATIVE_PROTECTION_ROUTES.md); [root analytical check](../.claude/science/physics-loops/native-nodal-persistence-20261018/ROOT_REVIEW.md); [root exact implementation](../.claude/science/physics-loops/native-nodal-persistence-20261018/root_exact_check.py); [saved result](../.claude/science/physics-loops/native-nodal-persistence-20261018/root_exact_result.json).
- [Infinite-lattice source](../.claude/science/physics-loops/native-nodal-persistence-20261018/INFINITE_LATTICE_PROBE.md); [independent analytical check](../.claude/science/physics-loops/native-nodal-persistence-20261018/INFINITE_CHECK.md).
- [Two-excitation source](../.claude/science/physics-loops/native-nodal-persistence-20261018/MANY_BODY_DARK_CODE.md); [root analytical check](../.claude/science/physics-loops/native-nodal-persistence-20261018/ROOT_MANY_BODY_REVIEW.md); [author implementation](../.claude/science/physics-loops/native-nodal-persistence-20261018/many_body_dark_check.py); [author result](../.claude/science/physics-loops/native-nodal-persistence-20261018/many_body_dark_result.json); [root implementation](../.claude/science/physics-loops/native-nodal-persistence-20261018/root_two_particle_check.py); [root result](../.claude/science/physics-loops/native-nodal-persistence-20261018/root_two_particle_result.json).
- [Bounded source searches](../.claude/science/physics-loops/native-nodal-persistence-20261018/PRIOR_ART_SEARCH.json); [earlier compression prior-art report](../.claude/science/physics-loops/native-nodal-persistence-20261018/NATIVE_COMPRESSION_PRIOR_ART.md).

The publication packet freezes the original checked sources and receipts. Its scripts are historical check evidence; the declared primary runner imports the source-local finite-control helper for current execution. The sole live campaign checkpoint remains outside this publication snapshot. The empty upstream_dependencies list is intentional: the cited framework notes supply terminology and context, while the displayed model and mathematical hypotheses are explicitly supplied and the intertwiners are proved here. No upstream framework derivation is claimed as a load-bearing theorem.

## 7. Remaining scientific obligation

The concrete result is native persistence inside stated moving codes, including every finite excitation number on actual Z3, with the full spin Hamiltonian and full outputs retained. It removes an externally imposed compression mechanism at that restricted interface. It leaves selected dynamics, background and encoded preparation, physical Record admissibility/formation and readout, robustness, and the earlier operation's purpose unresolved. A useful next theorem would supply an actual loading interface or a larger interacting invariant sector while retaining those complete physical factors. It must not infer those suppliers merely from existence of the code.

### Frozen research source identities

These SHA256 values bind the research files read or cited for this draft; they are provenance, not mathematical validation.

- `../NATIVE_PROTECTION_ROUTES.md`: `3623ee3301483783bc3c991a86f6702eb7c8715a975d776869acf473a0384548`.
- `ROOT_REVIEW.md`: `4c5e3d8e27557034b61592c6edab9622c72be44d6c78e849a8fa1321024427fc`.
- `INFINITE_LATTICE_PROBE.md`: `d85f00866d575e03486ed876f0694b28e7f723f6d228ab3e2cf7854f2ddef1b0`.
- `INFINITE_CHECK.md`: `3518afc688da1f9003fb509f027bfe4b1e8b007008dc5eb1c27dd89536e0d91a`.
- `MANY_BODY_DARK_CODE.md`: `76b8e51ee20610585eecf253517047798ea1e03e0e6c77262caa13a7d7e5d9c8`.
- `ROOT_MANY_BODY_REVIEW.md`: `190e3d5b31448621b4f201f8dbc0fabf18db059a3fac2583dddd3cf98335c236`.
- `root_exact_check.py`: `32d468510489530a8c6ba4c3ebfe6dc4a9d8782d772676456b5708f65850a66e`.
- `root_exact_result.json`: `c08d56544b8a5cdc2f8f5ac7a64fd21128c01bf0f86f4bfd7dfdf4e42319a66e`.
- `many_body_dark_check.py`: `c59f25fffe35c13ff105bd8fce78d686ad30724e1ba435e99e9faa4e65cc9b43`.
- `many_body_dark_result.json`: `0066719ce121bb8b370c266e0ee09dc24aca4c554a0e7314c8dfd8a84be5936f`.
- `root_two_particle_check.py`: `ed34808a700bb78e667af02066493182bf87c707add34f3034bf75fdbb647a07`.
- `root_two_particle_result.json`: `19870bbb626f77c73d6ad1045293c5de3abf064284e9b7609c4fcb9c8c102734`.

## Reproduction and proof obligations

Run `python3 scripts/native_heisenberg_nodal_record_persistence_2026_10_18.py` for the finite controls; canonical execution uses `runner_cache.execute_and_write_cache` with timeout120. The imported helpers are `scripts/native_heisenberg_nodal_controls.py` and `scripts/native_heisenberg_many_particle_controls.py`. Nine fixtures comprise six periodic finite controls and three actual-Z3 finite-support controls. Ten scratch mutations across the two helpers were rejected; the packet preserves the individual mutation results in RUNNER_MUTATIONS.json and MANY_PARTICLE_MUTATIONS.json.

The proof obligations are: (i) full-spin restriction and finite odd intertwiner, proved in section2; (ii) self-adjoint infinite generator, core and local-interaction identity, proved in section3; (iii) nonadjacent singlet transfer and cancellation before repeated evolution, proved in section4; (iv) all-finite-n normalized embedding, adjacent-pair cancellation and reducing direct-sum domains, proved in section4A; (v) complete physical output/reference preservation, by the displayed intertwiners. The strongest unresolved physical obligation is an admissible preparation/formation mechanism for the chosen code under a selected native law. None of the finite checks discharges that obligation.

The all-finite-n derivation and independent check are frozen in `INFINITE_N_PROBE.md` and `INFINITE_MANY_EXCITATION_CHECK.md` in the publication packet. The new sparse helper checks actual unbounded-lattice neighbours through two actions; it does not simulate an infinite-density state.
