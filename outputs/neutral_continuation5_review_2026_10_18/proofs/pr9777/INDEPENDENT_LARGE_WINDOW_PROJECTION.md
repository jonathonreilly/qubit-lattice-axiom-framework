<!-- Original PR9777 source SHA256 d432fbeec21c5f2042c48da4e17b9f7172bf86ac38b4f6bbfde01be598599633. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Actual microscopic positive spectral window: independent check

Disposition: PASS as a joint weak-coupling/growing-finite-volume theorem using the stated local normal-form and ground-gap inputs. The appended uniform coefficient/source/orbit arguments close the prerequisites left open in the initial draft. This is an actual positive spectral-window lower bound, not isolation of an actual band or pole.

Read /tmp/neutral_native_threshold_window_root.md, /private/tmp/neutral-native-threshold-window-check.md, and native/MICROSCOPIC_GROUND_WINDOW_PROOF.md and FOURIER_GROUND_WINDOW_PROOF.md in the specified worktree. No shared/canonical edits.

## Uniform trial and exact ground

The weighted Schur argument is valid provided the local D_j decomposition is individually N-preserving, with incident longitudinal neighbors included in its support. The existing microscopic proof explicitly supplies that decomposition by the commuting-N filter and bounded support enlargement. After subtracting each vacuum scalar, a term missing the two occupied intervals and their incident wall neighborhoods annihilates the configuration. There are at most C_j(ell+1) possible translated supports, independently of transverse separation, and each has bounded output degree. Since a fixed-support move changes the number of flipped spins by O_j(1), the output common-interval length differs by O_j(1). Applying the Schur test to (D_j-E_j,vac)/(ell+1) therefore proves the stated norm bound. The COM fiber cannot worsen this absolute row/column estimate.

The compact finite-excitation N=4, layer-even classification is essential here: two columns share one interval. The construction truncates that interval below a fraction of the torus length, so winding sectors are not silently included. The host has ell=1; the attached rays have a uniform ratio below .6 near b_c. Thus all fixed length moments are uniformly bounded, and the finite sum of coefficients j>=2 gives O(Jz lambda^2) on the normalized trial. No global norm estimate over arbitrary long intervals is used.

The background-orbit map is well-defined because stabilizer characters agree on the reference and the layer-even excitation. Different background images, including their fixed-order residual images, have disjoint computational supports: two short intervals plus a fixed number of spin changes cannot reverse an entire column. Therefore the map is isometric and its residual bound transfers to all P0 superpositions without a ground-rank factor. Plane invariance makes the leading source overlap a scalar operator on P0. The transverse localization cutoff is needed for finite/infinite approximation, not for this column-length disjointness argument.

The existing ground result supplies a map from EVERY exact ground vector to P0, not equality of the exact ground space with the entire lowest band. This distinction is respected. Its actual O(lambda^29) proximity can be weakened to O(lambda^25); multiplying by ||C_Q||=O(lambda^-6) still gives only O(lambda^19) source errors. Construct Xi from the normalized P0 image and the excitation map, then undress. Its residual is directly controlled by the coefficient action plus the global O(Jz lambda^29) remainder; it need not be inferred by applying an extensive Hamiltonian norm to the ground-vector difference. Use actual Eg in the center; Eg-Evac=O(Jz lambda^29) is harmless.

## Source norm and positivity

For each fixed source coefficient, its action on all-up is a finite collection of nonempty spin patterns. Translates have nonzero Gram overlap at only finitely many relative positions. The 1/sqrt(V) Fourier sum therefore has volume-independent vector norm, uniformly for real allowed Q. Scalar terms sum to zero at nonzero Q; explicit centering remains appropriate for arbitrary exact ground states. The orbit argument extends this estimate to every P0 vector. Thus the leading norm is O(lambda), the higher-source vector remainder is O(lambda^2), the exact source tail is O(lambda^35), and the ground-transfer error is O(lambda^19). An operator-norm estimate alone would not give this result, but the supplied Gram estimate does.

For complex Fourier source use q=(C_Q-<C_Q>)|g> and the POSITIVE measure

 <g|(C_Q-<C_Q>)^dagger P_w (C_Q-<C_Q>)|g>=||P_w q||^2.

Here C_Q^dagger=C_-Q. No Hermiticity of C_Q and no translation eigenstate assumption is needed. This is not the generally complex C_Q C_Q correlator, nor an assertion that a retarded or smooth-time filter is positive. Since the window is separated from Eg, P_w|g>=0 exactly, so source centering cannot change its spectral-window weight. Uniform vector-state bounds extend to arbitrary exact-ground densities by linearity of this excited-window measure.

## Window inequality and powers

From ||(H-Eg-Jz[8+lambda E_b])Xi||<=C Jz lambda^2 and w=Jz lambda delta/4,

 ||(1-P_w)Xi||<=4C lambda/delta.

For normalized Xi, splitting its overlap with q gives

 ||P_w q|| >= |<Xi,q>|-||(1-P_w)Xi||||q||.

With a=lambda sqrt(W0 delta)log(1/delta)[1+o(1)] and ||q||=O(lambda), the loss is O(lambda^2/delta); relative to a it is O(lambda/[delta^(3/2)log(1/delta)]). Hence delta=lambda^alpha with 0<alpha<2/3 gives

 ||P_w q||^2 >= W0 lambda^2 delta log^2(1/delta)[1-o(1)].

Jz cancels in the projection-error ratio. The higher-source O(lambda^2) error has relative size O(lambda/[sqrt(delta)log(1/delta)]), also vanishing. The strict alpha range is sufficient. Under precisely these estimates the endpoint alpha=2/3 would also pass the logarithmic test, but no endpoint claim is necessary. This is a LOWER bound; additional full-H spectral weight is allowed.

## Finite geometry and scope

The Fourier extension to transverse Q uses the same modulus-one weights and exact allowed mesh as the cited proof; it does not require its original small longitudinal p restriction for these norm arguments. The mesh shift O(lambda^4) changes log(delta) by O(lambda^4 log^2(1/lambda)) using the implicit threshold law, or can be handled by direct bracketing. L sqrt(delta) tends to infinity very rapidly. A small imaginary Fourier contour shift of order sqrt(delta), justified by the quadratic band minimum, gives exponential transverse tails with polynomial threshold prefactors. Combined with uniform vertical evanescence, all wrap/truncation and fixed-order residual errors are smaller than any power of lambda. Merely citing a generic gap-linear Combes-Thomas rate would also suffice at these box scales, but the stronger stated rate is valid for this explicit host.

The imported premises remain the supplied native Hamiltonian and weak-coupling regime, fixed-order local construction/remainder, actual-ground gap theorem in L proportional to lambda^-4 boxes, native K1 graph/source identification, and the nonzero critical source coefficient W0. The argument does not prove a fixed-lambda thermodynamic theorem or cosmological preparation. It does certify nonzero microscopic spectral weight for the original complex Fourier readout, from every actual ground state in the stated family, inside a shrinking controlled window. It does not certify an isolated full-H eigenvalue/band, a lifetime, a resonance pole, or a physical scalar-particle interpretation.
