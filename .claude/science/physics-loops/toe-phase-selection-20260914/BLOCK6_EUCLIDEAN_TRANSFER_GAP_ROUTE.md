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

## Reading and derivation update, approximately 18:28 UTC

The original scanned pp.44--46 were visually inspected. Equation (2.90)
is a two-sided quadratic-form covariance bound on coclosed dual currents;
(2.91) uses liminf/limsup, not a single radial limit. The score in (2.89)
is imaginary, so its diagonal contact term must be treated explicitly.

Let phi(theta) = sum_n exp[-n^2/(2 beta)] exp(i n theta), using normalized
Haar measure. Put s=phi'/phi, a bounded real odd score, and Phi=-i s.
For the integer plaquette Fourier field n with delta n=0, separate-factor
insertion gives, at distinct plaquettes, E[Phi_p Phi_q]=E[n_p n_q].
At a repeated plaquette the insertion for n_p^2 is -phi''/phi. Hence, in a
translation-invariant charge-conjugation-even state,

    C_s(x) = kappa delta_{x,0} - C_n(x),
    kappa = E[-(log phi)''(d theta_p)] = E[n_p^2] + E[s_p^2].

This sign and contact correction will be checked by independent finite
Fourier and original-angle integrations. The dual orientation is the Hodge
complement of the original plaquette, including fixed anchor offsets.

Applying the imported FS quadratic-form bound with mu=delta sigma, for
sigma a test 2-form of one fixed dual orientation (rho,sigma), gives a
spectral-density sandwich

    beta'' q(k) <= S_n(k) <= beta q(k),
    q(k)=(|exp(i k_rho)-1|^2+|exp(i k_sigma)-1|^2)
         / sum_j |exp(i k_j)-1|^2.

The upper bound implies an L-infinity spectral density, therefore all
dual field-strength correlations tend to zero at infinity. The contact
identity transfers clustering to the bounded real score. If C_s were
absolutely summable, S_n would have a continuous version. The sandwich,
initially almost everywhere, would extend to each k != 0 by continuity;
approach through a complementary axis forces limit zero, while approach
through a plane axis forces liminf >= beta'' > 0. Thus no continuous
version, and C_s is not summable. This uses D >= 3 for a complementary
axis; the physical imported FS theorem used here is D=4 at large beta.

Ground-state uniqueness can be avoided. In an OS reconstruction, bounded
half-space functions have norm at most their sup norm. For a centered score
G, temporal decay of E[(Theta G) tau_t G] implies
||P_{T=1}[G]||^2=lim_t <[G],T^t[G]>=0. Therefore G has no invariant-space
component even if other ground states exist. A positive gap above the entire
invariant space then gives the same exponential insertion estimate.

For a score supported in a unit time slab, put G^sharp=tau_1 Theta G,
with site reflection at time zero. Then
<[F^sharp],T^(R-1)[G]>=E[F tau_R G] for R>=1, with spatial translation
unitaries inserted as needed. The orientation/reflection family is finite,
all members have the same sup norm, and isotropy rotates a largest coordinate
into time. Thus a spectral gap gamma would imply

    |C(x)| <= C^2 exp[-gamma max(||x||_infinity-1,0)].

For D=4, q_gap=exp(-gamma), its absolute sum is bounded by

    C^2 [1 + 64(1+4 q_gap+q_gap^2)/(1-q_gap)^4
             + 16/(1-q_gap)^2].

This derivation still needs an explicit construction/check of the OS
transfer and its state, plus deliberate tests of the contact and support
conventions. It has not yet established a claim about the finite-clock
Hamiltonian or a native probability law.

For the state limit, Chevyrev--Garban, arXiv:2404.09928v2 (10 March 2025),
Corollary 1.6 gives Villain Wilson-loop monotonicity in each plaquette
coupling, via the carpet-graph limit (Theorem 1.5). Definition 1.3, Corollary
1.6, Remark 1.7 and the proof at the end of section 4 were read. Remark 1.7
explicitly cautions that log Villain weight is not positive definite: the
ordinary direct Ginibre premise cannot simply be asserted. Their result
can establish the unique free-boundary expectation limit for all characters:
nonclosed characters vanish by gauge invariance, and every finite closed
integer current is represented by a loop, allowing repeated edges and
canceling connecting paths. Character convergence gives the local measure
limit. The bounded-rectangle net is cofinal, so translations, cubic rotations
and reflections are inherited. Reflection positivity can then be checked on
boxes symmetric about each required plane before taking this same limit.
