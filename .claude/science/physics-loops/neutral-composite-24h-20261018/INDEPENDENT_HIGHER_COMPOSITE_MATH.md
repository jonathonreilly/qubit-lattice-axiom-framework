# Higher balanced neutral composites: extension of the fixed-Q no-atom result

## Verdict and premises

The root's proposed finite-degree extension is valid under a precise independent-momentum/L2-kernel contract. It does **not** require an added interaction, analytic eigenvalue branches, or new numerical certificates for the exponentially larger matrices.

Assume h(k) is the same finite-dimensional Hermitian real-analytic Bloch Hamiltonian on the connected torus. Fix Q for which the bilinear certificate proves

    for every real z, det[L_Q(k)−z I] is not identically zero in k,
    L_Q(k)=h(k+Q) acting on creations − h(k)^T acting on annihilations.

This premise is stronger than excluding a single selected frequency and is exactly what the coprime two-momentum characteristic-polynomial certificate supplies.

## Finite-degree algebraic argument

A balanced normal-ordered 2n-fermion monomial has n creation momenta p_i and n annihilation momenta k_i with

    sum_i p_i−sum_i k_i=Q modulo reciprocal vectors.

Use independent coordinates p_1,...,p_n,k_1,...,k_(n−1), with

    k_n=sum_i p_i−sum_(i<n)k_i−Q.

The unconstrained band-index tensor space has finite dimension d^(2n). Its Liouvillian is the Kronecker sum

    L_n=sum_i h(p_i) on creation factor i
            −sum_i h(k_i)^T on annihilation factor i.

It is a Hermitian real-analytic matrix on the connected torus of dimension dim(k)(2n−1). Fermionic signs/ordering are handled by antisymmetrizing the kernel; this full tensor matrix is a valid ambient representation before that restriction.

Suppose, for a fixed real omega, det(L_n−omega I) were identically zero. Restrict to the analytic submanifold

    p_i=k_i=a_i for i=2,...,n,
    p_1=k_1+Q,

where a_i are any fixed momenta and k_1 varies. This submanifold is compatible with the total-momentum constraint; its being lower dimensional is no obstacle because the hypothesized identity holds everywhere, not just almost everywhere on a generic slice.

On this slice the matrix is a Kronecker sum of the varying bilinear L_Q(k_1) and n−1 fixed spectator-pair matrices. Let delta_j be the finite real spectrum of that fixed spectator sum, with multiplicities. Then

    det[L_n|slice−omega I]
       =product_j det[L_Q(k_1)−(omega−delta_j)I].

Every factor is real analytic and is not identically zero by the bilinear premise, since each omega−delta_j is real. A finite product of nonzero real-analytic functions on a connected torus cannot vanish identically: each factor has a measure-zero zero set, and a finite union cannot cover the torus. This contradicts the supposed identity.

Therefore, for every finite n and every real omega,

    det[L_n−omega I] is not identically zero.

Its zero set has Lebesgue measure zero in the full independent-momentum domain. Multiplication by L_n on the corresponding L2 tensor-kernel space consequently has no point eigenvalue at omega and no source spectral atom there. Restriction to an invariant fermion-antisymmetric subspace cannot add a point eigenvalue absent from the ambient space. The ambient determinant is defined even at coincident momenta where some physical antisymmetric amplitudes vanish; those coincidences do not invalidate the identity-by-restriction argument.

This proof does not assert that all higher-composite spectra are smooth or gapped. Continuous spectral weight and arbitrarily small residual wave packets can remain.

## Mapping to actual neutral observables

Finite-range, translation-covariant, charge-neutral local CAR polynomials Fourier transformed to total momentum Q have finite-degree relative-momentum kernels. After the usual per-volume normalization of the center-of-mass Fourier transform, their relative kernels are trigonometric polynomials and belong to the stated L2 fibers. Thus they are a concrete covered class, not just formal tensors.

Normal ordering must be specified. Vacuum CAR normal ordering gives a finite algebraic decomposition into balanced degrees. For a stationary, translation-invariant, gauge-invariant quasifree state, state-relative Wick ordering is particularly useful: distinct Wick-chaos degrees are orthogonal in the positive operator inner product, and the quadratic dynamics preserves each degree. The covariance commutes with h(k), so contractions are stationary; commuting H through a Wick-ordered polynomial gives precisely the displayed sum/difference Liouvillian, without a new interacting term.

In a band basis, each degree has products of occupation and vacancy weights, together with the required antisymmetrization and combinatorial normalization. Those weights are bounded and absolutely continuous with respect to the independent momentum measure. Quotient any zero-weight directions. Such weighting cannot create an atom from the measure-zero determinant set. A finite sum of these orthogonal degrees therefore has no source spectral atom at Q. Finite sums whose degrees have not been made orthogonal need the same invariant-Hilbert-space decomposition or another norm argument; one should not casually sum positive spectral densities from nonorthogonal terms.

A fixed-number/parity-projected finite-volume thermal state is not automatically quasifree. The determinant calculation still governs the formal degree-wise commutator, but translating it into that ensemble's thermodynamic positive spectral norm requires its own absolutely-continuous kernel representation or a controlled convergence to the quasifree state. The present argument does not supply that convergence.

## Direct-sum closure: what can safely be said

Within the explicitly defined orthogonal Hilbert direct sum of these finite-degree Wick sectors, the self-adjoint generator is the direct sum of the sector generators. Its spectral projection onto {omega} is the direct sum of their spectral projections. Since each is zero, the closure also has no point spectrum at Q.

This includes norm-convergent infinite-degree expansions **in that operator Hilbert space**. It does not by itself classify all thermodynamic observables, all representations, nonnormalizable collective variables, or sector-changing macroscopic limits. If making the direct-sum statement in a final artifact, define the GNS/Wick space and fixed-momentum fiber rather than saying 'all neutral operators' without qualification. Degree zero is the identity and carries only total momentum zero; Q here is nonzero modulo reciprocal vectors.

## Important exclusions and non-counterexamples

1. **Additional delta constraints.** A kernel imposing p_i=k_i, a sharp energy-shell relation, or other momentum correlations by delta functions can be supported on a lower-dimensional set and need not be L2 in the full independent variables. The proof's spectator slice is a logical test of an analytic identity, not a license to treat a delta-supported source as L2. Some products of extensive momentum-resolved conserved quantities with an excitation fall into this excluded class unless separately normalized and represented.
2. **Finite momentum grids.** They have discrete spectra. The theorem concerns the infinite-volume multiplication operator; convergence to it must be justified for finite-size probes.
3. **Narrow resonances.** No atom does not imply a uniform lower bound on variance/residual, nor exclude long-lived approximately monochromatic packets. Combine it with the source-overlap theorem only under that theorem's fixed-source/metric or controlled-volume-limit assumptions.
4. **Different Q or model.** The extension is at the certified Q for the fixed candidate (or an independently certified robust neighborhood). It says nothing about q=0 conserved charges, other momenta, flat-band candidates that fail the bilinear premise, or interacting Hamiltonians.
5. **Non-neutral/anomalous sectors.** Unequal numbers of creations and annihilations are not established by the spectator reduction given here.
6. **Autonomous fields outside the space.** A different microscopic degree of freedom, nonquasifree state mechanism, nonlocal/distributional construction or interaction is not excluded. It needs an explicit new contract rather than being counted as a finite balanced L2 composite of this free model.

## Bottom-line scope

The same exact bilinear certificate excludes a source-visible point atom at fixed Q for every finite-degree balanced neutral L2 composite in the stated free translation-invariant candidate, with compatible absolutely-continuous positive state metrics. This is a genuine extension beyond bilinear probes. It is not a blanket no-go theorem for composite particles, all neutral mechanisms, or all one-qubit Hamiltonians.
