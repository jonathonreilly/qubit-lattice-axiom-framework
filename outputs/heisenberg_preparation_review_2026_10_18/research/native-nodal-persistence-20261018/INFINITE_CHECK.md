<!-- Original SHA256 3518afc688da1f9003fb509f027bfe4b1e8b007008dc5eb1c27dd89536e0d91a -->
**Provenance boundary:** Complete original source follows. Historical review labels and execution narratives are provenance, not fresh verification or current audit authority. Mathematical arguments retain their explicit hypotheses.

# Independent check of the infinite-lattice nodal construction

2026-10-18. Checked `INFINITE_LATTICE_PROBE.md`, SHA256 `d85f00866d575e03486ed876f0694b28e7f723f6d228ab3e2cf7854f2ddef1b0`, in full. This is a distinct analytical check of the stated construction; no runner or numerical result was used, and no retained/audit verdict is supplied. I authored the separate two-excitation finite-torus construction, so the common research context is disclosed; the argument checked here was authored by root.

**Finding:** the proposed dynamics, domain/core claim, local commutator identity, odd-sector/Dirichlet intertwiner, record-plane factorization and energy boundary are correct as stated. No substantive mathematical correction is required. Two useful details are proved below: extension of the local commutator identity to the operator domain, and the fact that all encoded one-excitation l2 inputs already have bounded energy, not only finite-support packets.

## 1. Bond action and sector operator

For a finite occupied set S, a bond with equal endpoint occupations annihilates |S> under 2j(I-SWAP). A bond with one occupied endpoint contributes 2j(|S>-|S triangle {x,y}>). Distinct crossing edges give distinct moved configurations; the configuration graph is simple and locally finite, with degree at most6n on its n-particle sector. This verifies the physical coefficient2j, the diagonal degree and the off-diagonal minus sign directly.

The configuration Laplacian has quadratic form

    <f,L_n f>=sum_{unordered configuration edges {S,T}} |f(S)-f(T)|^2.

Initially this is a finite sum for finite-support f, with finitely many neighbouring configurations. The inequality |a-b|^2<=2(|a|^2+|b|^2) bounds it by12n||f||^2. Polarization or the bounded-adjacency construction then gives a unique bounded nonnegative self-adjoint L_n with norm<=12n. Therefore H_n=2jL_n has norm<=24jn. The source's argument and normalization are correct, including n=0.

## 2. Direct sum, resolvent and core

Define D(H) by sum_n||H_n psi_n||^2<infinity. On each sector, H_n is bounded self-adjoint, so the inverse of H_n+/-i has norm<=1 and H_n(H_n+/-i)^-1 has norm<=1. Thus the blockwise resolvent not only is bounded on the Hilbert direct sum but maps it into D(H). It inverts H+/-i there, establishing self-adjointness of the symmetric direct-sum operator. Positivity follows sectorwise.

For psi in D(H), truncation to finitely many sectors converges both in norm and H norm by the defining two summability conditions. In a fixed finite group of sectors, finitely supported configuration vectors are dense and H_n is bounded. Approximating in each such sector therefore gives graph-norm approximation. The finite-configuration linear span is indeed an operator core; it is not asserted to be invariant under the finite-time unitary, which generally develops infinite spatial tails.

## 3. Local commutators and domain preservation

A local spin operator A supported on a finite site set maps a finite-configuration vector to a finite linear combination of configurations. On that core, both HA and AH are actual finite sums when applied to a basis vector. Disjoint bond operators commute with A, leaving only finitely many edges meeting supp(A). Let

    C_A=sum_(e meeting supp A) [2j(I-SWAP_e),A].

This is a bounded operator on the whole incomplete tensor product (for example each summand has norm at most8j||A||). The source's core identity [H,A]=C_A is therefore valid.

One can strengthen the statement without adding hypotheses. For psi in D(H), take graph-core approximants psi_k. Then A psi_k converges to A psi and H A psi_k=A H psi_k+C_A psi_k converges. Closedness of H yields A psi in D(H) and HA psi=AH psi+C_A psi. Thus every local spin operator preserves D(H), and the bounded commutator identity extends to that domain. No assertion about a representation-independent infinite-temperature state or norm convergence of the infinite Hamiltonian is needed.

## 4. Reflection and half-space operator

In the one-excitation sector, configuration degree is exactly6 and H_1=2j(6I-A_Z3). Spatial reflection F is unitary on l2(Z3), commutes with adjacency and preserves the bounded H_1. Hence the odd spectral subspace of F is reducing. Evaluation at any reflection-fixed lattice vertex vanishes for every odd amplitude; this is a literal coefficient statement in l2, with no distributional boundary subtlety.

The map V from l2(x>=1) has the two disjoint copies with relative minus sign and factor1/sqrt2, so it is an isometry onto the odd sector. At x=1, the missing neighbour's full-space amplitude is zero, but the full Laplacian diagonal remains6. At x=0, the +1 and -1 amplitudes cancel. Interior vertices obey the ordinary hopping formula. These three cases prove

    H_1 V = V 2j L_D,

with L_D diagonal6 and off-diagonal -1 on half-space edges. Calling L_D the degree5 boundary graph Laplacian would be incorrect; the source explicitly avoids this error. Both sides are bounded, so coefficient verification on finite-support vectors extends to all half-space l2 and exponentiates for every real time. The vacuum has energy0 and can be included as an orthogonal code summand.

Exactly the same pointwise argument applies to simultaneous oddness under any subset of the commuting coordinate reflections, with the stated normalization2^(-k/2). Fixed coordinate planes have zero excitation coefficient, and the orthant boundary diagonal remains6.

## 5. Full output, local records and references

Every vector in the vacuum-plus-odd code has no excitation on any site of the plane. A local plane projector onto q therefore acts identically on it and on its full time-evolved image. For any finite set of plane sites, those qubits factor as the pure product q from the remaining physical system. This extends to mixed encoded states and arbitrary passive reference systems because the isometry/intertwining equations extend by identity on the reference.

No half-space copy is discarded: V includes both physical reflected packets. The claimed output isometry is a complete physical comparison, not a reduced channel obtained by tracing one side. On this code H is bounded by24j, so every encoded l2 input (including reference-entangled ones) lies in the Hamiltonian domain and has finite first and second energy moments bounded by the corresponding operator norms. Finite support is useful for explicit prepared examples, but unnecessary for finite energy within this code.

The statement about infinite plane records is properly local. It neither invokes an infinite product as a quasi-local observable nor derives a stochastic formation event or permanence for arbitrary inputs outside the prepared code. The incomplete tensor-product representation does admit the corresponding plane/complement vacuum-sector factorization, but the finite-reduced-state formulation already suffices.

## 6. Energy and representation boundaries

The positive interaction j(I-sigma.sigma)=2j(I-SWAP) is an actual local model, annihilating the chosen vacuum termwise. Its infinite sum is defined by the sector construction and closure above. It is not obtained by subtracting a finite scalar from a pre-existing infinite unshifted Heisenberg Hamiltonian. The source correctly retains j|E| in finite volume and declines a finite absolute-energy equality for the divergent raw infinite sum.

The chosen q representation and the supplied homogeneous j remain premises. Positivity makes the vacuum a ground vector of this represented model; it does not select its physical preparation or a unique infinite-volume phase. Arbitrary thermal representations, finite-density initial states outside this representation, generic symmetry-breaking noise, formation/readout semantics and the previous engineered gate's operational objective are not covered. Those boundaries are explicit in the source and should survive downstream packaging.

## Disposition for the next research decision

The source provides a valid actual-Z3 extension of the one-excitation mechanism and removes the finite periodic-geometry premise for that sector. It supplies no protecting gap and does not by itself extend to generic many-excitation states. The distinct finite two-excitation code should be checked separately; neither proof inherits correctness merely because the other uses the same Heisenberg bonds.
