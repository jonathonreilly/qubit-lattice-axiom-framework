# An antisymmetric record fiber and physical singlet-cover states

2026-09-21. Root conditional construction with exact exploratory finite
controls. The new work in this note has not yet had a separate independent
check. It builds on the separately checked quantum-lift boundary, but that
earlier review does not cover this extension.

The positive result is an explicit coherent sector whose literal tensor-
qubit image is a product of singlets on each matching. It avoids the collapse
of the particular unsigned fiber previously tested. The resulting singlet
covers are nonorthogonal, so their metric, Hamiltonian and readout must be
handled explicitly. Classical paired formation does not prepare this sector.

## 1. Antisymmetric coherent fibers

Fix a finite bipartite graph with V=2K sites and a perfect matching M. Orient
every matched edge from its black to its white endpoint. Give the K distinct
antipodal record keys spinor representatives |k,+>,|k,-> forming an SU(2)
frame. A phase choice with determinant one is available for each of this
finite collection of frames; no globally continuous spinor section is used.

Let eta denote a marked arrangement of all 2K records with antipodal partners
on matching edges, and let sigma(eta) be the product over black sites of +1
if the record there is a + representative and -1 if it is a - representative.
In the additional orthogonal marked-configuration Hilbert space, define

    U_- |M> = (2^K K!)^(-1/2)
              sum_(eta over M) sigma(eta)|eta>.            (1)

The marked fibers are disjoint and each has 2^K K! states. Therefore U_- is
an isometry there. On a flippable elementary square, a one-step rotation of
the four complete records reverses the black/white roles of exactly two
pairs. Both orientation signs change, so sigma is invariant. Each rotation
sense bijects the complete fiber of M with that of its geometric flip.
Consequently the supplied marked Hamiltonian of the earlier note obeys

    H_mark U_- = U_- H_QDM.                                (2)

This remains an algebraic statement in the supplied orthogonal space.

Now use the literal product map V|eta>=tensor_x |record_eta(x)> into the
site-qubit Hilbert space. The orientation sum for one pair is

    |k,+>_b |k,->_w - |k,->_b |k,+>_w
       = sqrt(2) |s_bw>,
    |s_bw> = (|0>_b|1>_w-|1>_b|0>_w)/sqrt(2).             (3)

For any assignment of keys to the edges, the K orientation sums thus give
2^(K/2) times the same normalized singlet-cover state
D_M=tensor_({b,w} in M)|s_bw>. There are K! key assignments. Dividing by
the normalization in (1) proves

    V U_- |M> = sqrt(K!) D_M.                              (4)

If the chosen normalized antipodal frames have arbitrary determinants, the
right side gains their product, a common unit-modulus phase independent of
M. Equation (4) is therefore a phase-consistent finite-key construction.
It does not preserve a readable continuous key label in the physical vector:
the orientation-antisymmetric combination is a singlet independent of that
key's Bloch direction. Coherence and its interpretation remain extra premises.

## 2. The overlap metric is explicit

Let D be the matrix with normalized columns D_M. The overlay of M and P
consists of alternating even loops, counting a common dimer as a two-site
loop. In a computational-basis overlap, each loop admits exactly two spin
assignments. The common black-to-white orientation makes both contributions
positive. The normalization of 2K spin factors gives

    G_MP = <D_M,D_P> = 2^(ell(M,P)-K),                    (5)

where ell is the number of overlay loops. Distinct covers therefore overlap;
they are not an orthogonal set of geometric alternatives in this map.

On the square the Gram matrix is [[1,1/2],[1/2,1]], of rank two. On the
six-site ladder, with the checker ordering, it is

    [[1,1/4,1/2],[1/4,1,1/2],[1/2,1/2,1]],

of rank three. The nine covers of the eight-site simple cube also have full
column rank. No all-graph linear-independence assertion is needed here.

## 3. Which Hamiltonian actually acts on these vectors?

For a Hermitian physical operator satisfying H_phys D=D H_QDM, taking the
adjoint of D^dagger H_phys D requires

    G H_QDM = H_QDM G,                                    (6)

because H_QDM is Hermitian in the orthogonal matching convention. At t=1,
the square satisfies (6) for every potential v. The six-site ladder satisfies
it precisely at v=1/2. In that full-rank case

    H_phys = D H_QDM G^(-1) D^dagger                       (7)

is a Hermitian extension on the physical Hilbert space and acts as required
on all three cover columns. This is a positive finite lift; (7) supplies no
locality or thermodynamic assertion.

On the eight-site simple cube, two exact entries of the commutator require
(2v-1)/2=0 and (v-2)/4=0. There is no v at t=1 satisfying both. More generally
in this two-parameter potential/flip family, the corresponding equations
2v-t=0 and v-2t=0 force v=t=0. This is a boundary of the particular singlet
map and unmodified two-parameter QDM action on this particular graph. It
does not rule out overlap-corrected Hamiltonians or a quantum record model.

For any supplied Hermitian physical W, its orthogonal projection to the
full-rank cover span has coefficient matrix

    A = G^(-1) D^dagger W D,
    G A = A^dagger G.                                    (8)

Ordinary symmetry of A is not the physical Hermiticity condition. In an
orthonormalized cover basis the matrix is G^(-1/2)D^dagger W D G^(-1/2).
The inverse overlap factors can be nonlocal; projection alone does not
establish that a local spin Hamiltonian realizes a local dimer Hamiltonian.

## 4. A local positive parent and its unclosed obligations

There is a direct local positive Hamiltonian that annihilates every nearest-
neighbor singlet cover. For each site x let star(x) contain x and all its
nearest neighbors. Let P_x^max project those spins onto their fully symmetric
maximum-spin subspace, and define

    H_K = sum_x P_x^max.                                  (9)

In every nearest-neighbor cover, the singlet joining x to its partner lies
entirely in star(x). A fully symmetric vector is orthogonal to this
antisymmetric pair, irrespective of the other spins. Hence

    P_x^max D_M=0 for every x,M, and H_K D_M=0.             (10)

On the ordinary infinite cubic lattice these terms have seven-site support.
Equation (10) is a frustration-free inclusion, not a characterization of
the full ground space, a gap theorem, a selection of one coherent cover
superposition, or a derivation of (9) from the record axioms.

An exact finite control shows why equality of the ground space cannot be
silently substituted for inclusion. On the eight-vertex **degree-three
simple cube**, the stars have four sites. The cover span has dimension 9,
whereas the exact kernel of (9) has dimension 19: ten singlets and three
spin-one multiplets. Its additional space has dimension 10. The smallest
positive eigenvalue is numerically about 0.612574 in this finite graph only.
This is not a degree-six cubic-torus gap calculation.

For W_NN=sum_(physical edges) Swap_xy and
W_ring=sum_(elementary squares)(R_p+R_p^dagger), exact cube projections
obey (8) but have nonsymmetric ordinary coefficient matrices. Their leakage
out of the cover span has rank one, with squared Frobenius norms respectively
5 and 20 when tested on the normalized cover columns. On this cube that
leakage lies outside the entire parent kernel: neither operator couples a
cover column into the extra parent-groundspace directions at first order.
This useful finite fact does not establish controlled perturbation theory
or decoupling on larger graphs.

## 5. Local combination controls are patch dependent

The exact finite family W_ring+alpha W_NN illustrates both possibilities.
On a square both terms already preserve the cover span. On the six-site
ladder alpha=-1 cancels the leakage exactly. On the simple eight-site cube
alpha=-2 does so exactly. However, on the eight-site ladder the unique
candidate alpha=-1 leaves squared Frobenius leakage 3/4. In the declared
integer-column basis one residual entry is -1/2 before the common cover
normalization. These are exact rational calculations.

Thus the small positive examples do not constitute an arbitrary-graph
closure identity. Additional local operators or a controlled low-energy
construction remain possible. The larger 2x2x3 patch is being evaluated
separately; no unfinished result from it is used in this note.

## 6. Three different readouts on the same square

For the two normalized square covers D_1,D_2, their coherent equal-amplitude
sum has norm squared 3. The singlet projector on a fixed square edge has
expectation 3/4 in the normalized coherent sum. It has expectation 5/8 in
the incoherent uniform mixture of these two singlet covers. The same edge
has geometric occupation probability 1/2 in the classical uniform matching
ensemble. All three numbers are exact.

Consequently geometric diagonal observables in an orthogonal dimer space
cannot simply be relabeled as local singlet projectors after (4). Their
physical measurement interpretation is another required part of a bridge.

Even the elementary antipodal classical preparation is distinct. A uniform
mixture of |n><n| tensor |-n><-n| has density matrix

    rho=(1/4)[I-(sigma_1.sigma_2)/3].                       (11)

The six antipodal product states along the three coordinate axes give an
explicit finite separable decomposition of the same matrix. Its singlet
eigenvalue and singlet fidelity are 1/2; its three triplet eigenvalues are
1/6. It is not the pure singlet in (3). Our supplied even formation density
is different from uniform spherical area, but it also gives a classical
mixture of product states, not the coherent antisymmetric orientation sum.

## 7. Existing literature and the phase question

The local parent and nonorthogonal-cover route is established territory.
Raman, Moessner and Sondhi use Klein-type interactions, overlap
orthonormalization and decorated lattices for controlled spin-model
constructions. Those additions are meaningful extra hypotheses; their
conclusions are not imported to the undecorated permanent-record model.
[Primary paper, v2](https://arxiv.org/abs/cond-mat/0502146v2).

The most immediate equal-amplitude physical singlet-cover state on the
isotropic cubic lattice also has a known limitation. Albuquerque, Alet and
Moessner report numerical Neel order together with dipolar bond correlations
for that SU(2) nearest-neighbor RVB state. Dipolar correlations therefore do
not alone identify the physical singlet construction as a pure Coulomb spin
liquid. This is their numerical result, not an exact phase theorem proved
here. [Primary paper, v2](https://arxiv.org/abs/1204.3195v2).

Xu and Beach examine direction-weighted singlet-cover trial states and
report disordered regimes away from the isotropic point. Their weighting
selects an axis, and the paper does not give the parent Hamiltonian whose
ground state is being tested. Its trial-state correlations are not a proven
Hamiltonian gap or a symmetry-preserving native photon construction.
[Primary paper, v1](https://arxiv.org/abs/1311.0004v1).

The pinned PDFs and bibliographic receipts are external research references,
not redistributed evidence files. None of these papers is needed for the
finite algebra and the inclusion proof (1)-(11).

## 8. Check coverage and next decision

`geometric_singlet_fiber_check.py` checks the signed marked intertwiner,
the exact tensor-qubit image for square and ladder keys, the loop Gram
formula, the Hamiltonian commutators, the tuned ladder lift, and the distinct
square and antipodal-mixture readouts. `geometric_klein_parent_check.py`
checks every parent term, all magnetization-sector nullspaces and the local
perturbations on the simple cube. `geometric_local_quantum_combination_check.py`
tests the declared local-operator combination on open rectangular patches.

These calculations distinguish a positive coherent embedding from an
operational preparation or a local physical realization of the QDM. The
next useful obligations are a justified quantum state interpretation,
a local dynamical/preparation mechanism, and a controlled phase analysis
with the actual nonorthogonal overlap and readout. The classical formation
and color-wave theorems do not discharge those obligations.
