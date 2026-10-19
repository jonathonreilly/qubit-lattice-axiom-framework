<!-- Original SHA256 62a6135efd5861b6ecf97f9d1f938a6367b54507d0a134457611c442b3ddbb3d -->
**Provenance boundary:** Complete original source follows. Historical review labels and execution narratives are provenance, not fresh verification or current audit authority. Mathematical arguments retain their explicit hypotheses.

# Actual-Z3 finite-excitation plane persistence through coordinate antisymmetry

Root proposal 2026-10-18; independent proof check in progress. Uses the supplied positive homogeneous Heisenberg dynamics already defined in INFINITE_LATTICE_PROBE.md. No new interaction or physical factor is introduced.

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

Root exact sparse checks compare independently assembled ordered free hopping with unordered physical full-spin moves on actual Z3 for n=1,2,3. First and second actions agree, and all equality/plane nodes remain zero. A two-excitation control with symmetric x/y coordinate factors instead of two exterior factors fails the claimed free intertwiner. These finite-support checks are evidence for the mechanism, not the proof for every n.
