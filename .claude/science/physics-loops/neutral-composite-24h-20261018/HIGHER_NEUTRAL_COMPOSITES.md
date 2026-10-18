# Higher neutral composites: independently checked conditional extension

This is an independently checked mathematical extension, not a physical identification. Keep its state/domain assumptions separate from the existing bilinear certificate.

Consider a fixed finite n and a balanced n-creation/n-annihilation operator of total momentum q in the same translation-invariant quadratic fermion Hamiltonian. Parametrize its kernel by annihilation momenta k1,...,kn and creation momenta p2,...,pn, with

    p1=q+sum_i ki-sum_(i>=2) pi.

The corresponding finite internal fiber generator is the sum of n creation Hamiltonians minus n transposed annihilation Hamiltonians. Its dimension is d^(2n) before fermionic antisymmetry. Every matrix entry and its characteristic determinant is real analytic in the independent momenta because h is a finite Fourier polynomial. CAR antisymmetry restricts the allowed kernels and cannot introduce a frequency absent from this full fiber matrix.

Suppose some real omega is an atom for an absolutely-continuously weighted square-integrable kernel. The fiber matrix must have eigenvalue omega on a positive-measure set. Its characteristic determinant is therefore identically zero by real analyticity. This conclusion applies to the unrestricted analytic determinant, including its continuation to coincident-momentum configurations; it does not require a nonzero fermionic wavefunction on those configurations.

Now restrict spectator momenta pi=ki=ai for i>=2, with each ai fixed. Then p1=k1+q. The fiber generator is a Kronecker sum of the bilinear L_q(k1) and a finite constant spectator generator C. Let the finite eigenvalues of C be delta_j, with multiplicity. The restricted characteristic determinant is

    product_j det(L_q(k1)-(omega-delta_j)I).

If the bilinear determinant is not identically zero at any real frequency, every factor here is a nonzero real-analytic function. A finite product of such functions cannot vanish identically on a connected torus. This contradicts the assumed identity.

Thus the bilinear non-flat-frequency property implies absence of frequency atoms at the same total q for every fixed finite balanced degree, in the specified L2 kernel space with absolutely-continuous weights. This proof does not require a numerical search over the exponentially large higher-degree matrix.

## Boundaries requiring explicit retention

- It is the same supplied free Hamiltonian. Existing interactions in another one-qubit model are not ruled out.
- Fixed total q=Q is the certified application here; other momenta remain separate questions.
- This is an infinite-volume L2 statement, not removal of finite-box lines.
- Singular momentum distributions and singular state measures are outside the stated domain.
- Finite-degree Wick-ordered kernels in a stationary quasifree thermal state give a clean application. Arbitrary un-ordered products need their contractions/domains handled before use.
- Passing from each finite degree to an infinite sum requires an actual Hilbert direct-sum decomposition and a self-adjoint generator preserving it. Do not assume that step for arbitrary large-feature limits or encoded-sector states.
- The result does not prove decay rates, smooth spectral density, scalar transformation law, canonical coupling, or a cosmological relation.

The constructive implication is that if this theorem is confirmed, merely assembling more neutral free fermionic factors cannot produce an isolated sharp mode at Q within this regular domain. The next productive questions become which native nonquadratic dynamics or different symmetry/momentum channel the microscopic qubit Hamiltonian actually supplies, and whether that supply can be derived rather than chosen.
