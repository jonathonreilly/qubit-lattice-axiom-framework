# Block 6: isotropic Euclidean correlations and the transfer gap

Started 2026-09-14 after block 5 author review. Personal derivation route,
not yet a checked theorem or a claim about the selected finite-clock phase.

## Leverage hypothesis

The interacting canonical logarithm's locality may be unnecessary for a
spectral-gap conclusion from an isotropic Euclidean state. A positive transfer
gap gives exponential decay in Euclidean time. Cubic isotropy can rotate a
largest displacement component into that time axis. If the rotated bounded
plaquette observable is a one-slab insertion with a controlled vector norm,
all local plaquette covariances become absolutely summable. A rigorously
nonsummable local covariance would then force the reconstructed gap to vanish.

For a normalized positive kernel T with positive unit Perron vector Omega,
a slab insertion K_F satisfying |K_F(a,b)| <= C_F T(a,b) obeys
|K_F Omega| <= C_F Omega, hence ||K_F Omega|| <= C_F; the adjoint has the
same bound. If T has gap gamma above its unique unit eigenvector, the
connected two-insertion expectation is bounded by
C_F C_G exp[-gamma(t-1)]. The proof must track insertion orientation,
support separation, ground-space subtraction and the infinite-volume state.

## Candidate physical application and limits

Compact U(1) Villain weights are positive smooth functions on the circle with
strictly positive Fourier coefficients. The gauge transfer has the form
D P K D, where D is the square-root spatial weight, K the temporal heat
convolution, and P gauge averaging. On the physical subspace this suggests a
positive injective trace-class transfer and a unique positive finite-volume
Perron vector. A temporal plaquette score is bounded on the compact circle,
and integrating temporal links should preserve the insertion kernel bound.

Fröhlich--Spencer, IHES P/81/40 (published CMP 83, 411--454, 1982), section
2.11 proves a non-summability statement for a local U(1) field-strength
correlation. Section 3 establishes finite-Z_N order/disorder perimeter
estimates; it does not by itself give the same local covariance result.
Primary source: https://omeka.ihes.fr/document/P_81_40.pdf . Load-bearing
formulas need visual inspection because the available text extraction omits
equations. Bibliographic attribution is not an axiom-level premise.

Open hypotheses to discharge before applying the proposed implication:

- Exact observable and non-summability statement, including complex score
  conventions, contact terms, dimension and boundary/state hypotheses.
- Reflection-positive, isotropic infinite-volume state and reconstruction.
- Identification of that state with the limit of finite-cylinder ground
  states, if finite-volume transfer gaps are used in the proof.
- A bounded insertion argument that does not assume bounded T^{-1/2} K_F
  T^{-1/2}, since that stronger assertion need not hold.
- Unique ground vector, or explicit subtraction of the full invariant space.

A gapless canonical log would not establish its interaction locality, a
linear photon pole, the finite-clock continuous-time Hamiltonian, a native
formation law, or a TOE. Anisotropic spatial power-law states are an essential
missing-hypothesis challenge: a gapped nonlocal Hamiltonian can have them.

## Alternative held in reserve

The renormalized noncompact dual measure may admit two-sided covariance
bounds via uniform Hessian control: Brascamp--Lieb above and an integration-
by-parts/Cramer--Rao bound below. Extending this to finite Z_N requires the
actual observable map and control of electric/magnetic mixed phases, not an
arbitrarily introduced latent Gaussian. No such extension is derived here.

Next: finish the block-5 delivery receipt, then inspect the precise primary
formulas and prove the abstract insertion/isotropy lemma with finite tests
and missing-hypothesis counterexamples. Continue until 01:30:44 UTC.
