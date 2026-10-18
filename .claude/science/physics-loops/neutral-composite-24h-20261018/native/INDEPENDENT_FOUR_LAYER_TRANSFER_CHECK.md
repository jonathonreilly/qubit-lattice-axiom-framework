# Four-layer original-readout transfer and positivity: independent check

Disposition: PASS at each fixed open transverse size R>=3, assuming the stated complete native order-four classification and analytic block reduction. No numerical pole assumption is needed. No canonical/shared edits.

In the full wallfree block, the earlier native classification gives scalar coefficients below order four, and

 H_eff=scalar+Jz lambda^4 K/128+O(lambda^5),
 C_eff=scalar+lambda^4 O/(128sqrt(V))+O(lambda^5),
 K=-4P-5E, O=-12P-18E=3K-3E.

The lower source coefficients must be scalar on the ENTIRE N=0 block, not merely on the plaquette-ground subspace. This is the supplied second-/third-order local return-graph fact; it is consistent with the absence of an orientation-dependent return graph before the square and with first winding at Lz=4. Subject to that classification, centering removes every lower scalar contribution. This would fail if an omitted lower-order orientation-dependent source term existed, so retain that premise explicitly.

At fixed R, the coefficient ground gap proved by the PF argument separates its one-dimensional (even R) or two-dimensional (odd R) global ground space from the rest. The actual wall gap remains O(Jz), while its wallfree low spectrum has scale Jz lambda^4/128. Finite-dimensional spectral perturbation therefore gives the stated convergence of actual ground vectors into the coefficient ground space. No volume-uniform gap estimate is needed or implied.

For F smooth and compactly supported away from zero, all wall-excited states lie outside its scaled support for small lambda. The exact wallfree block reduction can thus be used on both the source and spectral function. After subtracting the actual Eg, the scaled Hamiltonian is K-e0+O(lambda); the centered projected source is lambda^4 qO/(128sqrt(V))+O(lambda^5), with fixed-R constants. Smooth functional calculus gives an O(lambda) operator error. Hence

 <qC,F(128(H-Eg)/(Jz lambda^4))qC>
 /[lambda^8/(128^2 V)]
 =<qO,F(K-e0)qO>+O_R(lambda).

Here qC and qO denote the respective centered source vectors. This normalization has the correct Jz and V factors. The remainder is absolute, not a relative estimate for a test F whose limiting weight vanishes. Positivity applies when F>=0; a general signed test gives a signed spectral functional.

Since K g=e0 g,

 qO=-3(E-<E>)g,
 ||qO||^2=9 Var_g(E).

In the all-row/column-positive X block, the plaquette flips connect all allowed bit patterns and have negative coefficient. Its PF ground g has strictly positive amplitude on every pattern. E is diagonal and is nonconstant for every R>=3: the all-positive pattern has every edge product +1, while flipping the four sites of a corner plaquette preserves all row/column parities and creates boundary edges with product -1 on a larger grid. Thus Var_g(E)>0 exactly. For R=2 the block's two configurations have the same E, so the exclusion is necessary.

The nonzero qO is orthogonal to the coefficient ground vector in the all-positive block. It therefore has strictly positive spectral weight at positive coefficient excitation energies. Since the finite coefficient spectrum is discrete and its ground gap is positive, one can choose a nonnegative smooth compact F away from zero that equals one on all excited eigenvalues carrying this vector. The limiting functional is then 9 Var_g(E)>0. This proves existence of positive original-readout spectral response at energy scale Jz lambda^4 with weight scale lambda^8; it does not assert positivity for every possible test window or a single isolated line.

For odd R, the exact physical plane symmetries supply the needed ground-state qualification. With periodic Lz=4, transverse X and Y plane products induce the logical row/column X actions in N=0. A longitudinal physical Z-plane product induces global logical Z and anticommutes with each odd-length row/column action. All these commute with the native Hamiltonian, and the original distance-two ZZ readout commutes with them. Use an equivariant block reduction. The coefficient ground doublet is their irreducible two-dimensional representation; finite-gap perturbation preserves this representation in the actual lowest cluster for small lambda. The symmetry forces equal energies and prevents splitting of this doublet, while the coefficient gap excludes additional actual ground vectors. Source correlation/spectral operators commute with the representation, so their compression is scalar. Consequently every pure or mixed actual ground state has the same response; this is not a selected-sector preparation assumption. For even R the actual ground is unique at sufficiently small lambda by the coefficient gap.

This is a fixed-box microscopic response theorem for the supplied native interaction and original readout. It gives no uniform R-growth limit, quasiparticle pole, propagating scalar, lifetime, cosmological state selection, or identification with a measured detector. It replaces a numerical nonzero-weight premise with an exact variance argument, while leaving the detailed distribution among excited states open.
