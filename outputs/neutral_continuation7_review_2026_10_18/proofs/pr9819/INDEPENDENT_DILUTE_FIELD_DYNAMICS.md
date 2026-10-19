<!-- Original PR9819 source SHA256 baa762a2f21d59dc2f16a82d7b8fde0f0788d343c4720f2de1af0932b9ce8ffa. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent dilute-field dynamical-transfer review

Reviewed `native/NATIVE_DILUTE_FIELD_PROOF.md`. Disposition: the local/contact construction and stated scale window are consistent with the inherited fixed-order bounds. One ground-replacement step should be made explicit by the finite-rank rotation below; a norm-close-ground substitution inside repeated globally bounded creation products is not enough. This is a finite-mode, fixed-occupation result, not full-Hilbert-space CCR or a full N0-band separation.

## 1. Local realization of the internal mode

It is important that the local reduction retains BOTH endpoint orientations. Their small splitting must not be inverted to construct a spatially local one-orientation transform. The proof does retain both and diagonalizes the finite two-by-two fibre only afterwards, which avoids this problem.

At fixed final order the other Q4 gaps have already been handled by the inherited local path reductions. Their retained intertwiner consists of finitely many four-defect patterns and coefficients with bounded small-lambda limits. A concrete local extension of each pattern transition is: project onto its complete source syndrome in a finite footprint with a positive buffer, apply the corresponding physical column-X word and any required diagonal phase, and project onto its target syndrome. Both source and target have four bad plaquettes. This acts identically to the one-feature matrix on an isolated feature and preserves Q locally. Pairing a transition with its adjoint gives a Hermitian/anti-Hermitian local extension when needed. All projectors and column words are plane invariant.

One does not need an exact convergent global unitary for this extra extension: the finite-order one-feature intertwining identities can be applied locally. Choose the incompatibility buffer larger than the support of EVERY retained Hamiltonian term, every retained pattern, and every retained Gram-correction path. Then on compatible separated configurations, each term sees either the vacuum or a single feature. Since the Hamiltonian terms are individually Q preserving after the homological projection, vacuum-subtracted terms annihilate the local positive vacuum; they cannot secretly create remote defects. The isolated-feature intertwining identities therefore add over features.

This is the substantive condition behind the statement that the internal-state realization is local. If the inherited reduction only supplied eigenvalues or a delocalized eigenvector, it would be insufficient. The finite local path/intertwiner property stated here is what is used.

## 2. Contact residual and histories

For finitely many normalized modes with sup amplitudes O(1/R), the incompatible pair-event probability is O_m(1/R^2). The incompatible vector norm is O_m(1/R). The bounded incoming-history multiplicity and finite-Q operator bounds are needed to retain this after coherent symmetrization; a classical probability argument alone would not do so. These are the hypotheses of the cited cluster algebra check.

Every retained vacuum-subtracted coefficient has a bounded restriction on a fixed Q sector, and its leading scale is J lambda^4. Enlarging the bad relation to include one action of the retained Hamiltonian handles good configurations that can be mapped into a collision. The remaining difference between actual local action and the sum of one-feature actions is consequently bounded by

    C_m J lambda^4/R.

No full-volume norm J R^2 is used here. The global tail contributes C_m J R^2 lambda^M. Finite Gram orthonormalization within each occupation sector preserves this bound up to constants: a common m times rest energy commutes with that correction, and the remaining differences are no larger than the conservative contact scale. Constants may depend on fixed m_max, fixed final order, and fixed mode count, but not on R.

## 3. Exact-ground replacement: explicit repair

The state distance O(R^2 lambda^(M-4)) by itself does not justify repeatedly applying bare creation operators to the actual ground. Their global norms can grow with R, and the actual-ground tail need not lie in a fixed-Q sector. Avoid that argument.

Instead construct the product isometry W0 using the dressed flat approximate vacuum Omega first. In the all-positive sector the latter has residual r=(H-E_g)Omega of norm O(delta), delta=J R^2 lambda^M, and distance s=O(delta/(J lambda^4)) from the exact ground g. Choose phases with Omega=alpha g+s eta, eta perpendicular to g. Let V be the two-dimensional rotation in span{g,eta} sending Omega to g and equal to identity on its complement. Then

    ||V-I||=O(s),
    ||[H,V]||=O(||r||)=O(delta).

For the second statement use (H-E_g)g=0 and (H-E_g)eta=r/s; every offdiagonal rotation coefficient is O(s), and 1-alpha=O(s^2). This controls the commutator without multiplying a state error by ||H||.

Define W=V W0 ONCE, after the product/Gram/dressing construction. It is still an isometry, has W|0>=g exactly, and inherits the dynamical intertwining bound with an additional O(delta). There is no R^m amplification. For the normalized extracted readout, its conservative global norm is O(R/lambda^10), so the field-transfer correction from V-I is

    O((R/lambda^10) R^2 lambda^(M-4))
      =O(R^3 lambda^(M-14)),

exactly the error already allowed in the proof. This is a rigorous realization of the intended “actual-ground replacement”; it should be stated rather than relying only on closeness of vectors.

## 4. Time window and rest phase

With s=2, p=14, M=80, and physical time t=tau/(J lambda^16), bounded tau gives

    (J lambda^4/R)t = O(lambda^2),
    (J R^2 lambda^M)t = O(lambda^36).

The one-particle dispersion errors J lambda^14 q^2 and J lambda^10 q^4 both give O(lambda^2) accumulated phase for q~lambda^2. Rounding allowed momenta has still smaller effect. The calculation is a prepared finite-span Duhamel comparison, not an assertion that no interaction exists at finite density.

Keeping the full retained epsilon(0) is essential: replacing it by Delta J lambda^4 over a lambda^(-16) time would leave uncontrolled divergent phases. With the common retained rest energy removed per occupation, residual scalar errors are bounded by the same global tail times time. The exact reference E_g and the finite-rank rotation above make this consistent.

## 5. Energy filters and source caveats

The spectral projectors P_m onto the fixed-Q=4m bands are justified only by the inherited GLOBAL all-Q and wall bounds plus the uniform fixed-Q widths. They do not follow from separation of the entire N0 band from walls, and no such separation is needed. To isolate a finite number of low Q bands, the all-Q lower bound first excludes large Q and the order-J wall bound excludes N>0; the finite remaining Q bands then separate at order lambda^4.

The exact filters are broad enough to include all internal shapes at that Q. The leading extracted readout creates the endpoint motif only when it misses existing defects; contact-supported alternatives are bounded by the finite incoming-degree argument. Higher coefficients and the orientation mismatch give O(lambda^2) at the chosen q scale. The cited uniform finite-sector norm is necessary when composing the full-vector field identities; the crude global norm alone would not establish the commutators.

The conservative projector/source error R^3 lambda^(M-14) equals lambda^24 at the displayed scales. The ground rotation has the same bound, as shown above. This supports the claimed finite-mode CCR limit with an occupation buffer, provided the source calculation uses the same dressing and filters. The original unfiltered ZZ observable is not thereby a closed bosonic field.

## Conclusion

The scale choices and the contact estimate are consistent. The local internal-mode extension can be made explicit using complete source/target syndrome projectors and an enlarged fixed buffer. The actual-ground substitution should use one common finite-rank residual-controlled rotation (or an equally strong construction), not repeated application to a merely norm-close reference. With that clarification the presented dynamical/source transfer is supported within the inherited normal-form hypotheses. Hamiltonian, weak coupling, slab height, dilute prepared states, and nonlocal spectral readout remain assumptions; no finite-density or relativistic claim follows.
