# Block29: clock Ginibre inequality, free state, and static transfer bridge

Private author proof candidate, 2026-09-15. Independent review pending.
This companion resolves a proposed route around the thin-slab restriction of
PR8133 at f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8. It does not extend that
source's Hessian estimate to slabs. It identifies the free-boundary state by
another argument and applies the cubic-limit Wilson bound in that state.

## 1. Domain, source, and claim separation

On a finite subcomplex of the cubic lattice, let the link variables belong to
Z_N, with positive plaquette weights

 w_beta(theta) = sum_(k in Z) exp[-beta(theta+2pi k)^2/2], beta>0.

Multiplicative constants do not affect the law. Set w_0=1 using the normalized
heat kernel's continuous beta-down-to-zero limit. Couplings may differ by
plaquette and be zero. N>=1 is fixed. Statements about monotonicity and the
free state below hold in every dimension and at every nonnegative coupling.
The later Wilson energy bound additionally assumes the pinned PR8133 large-beta
conditions and its explicit epsilon. These conditions are provisional inputs.

Published input: I. Chevyrev and C. Garban, *Villain Action in Lattice Gauge
Theory*, Journal of Statistical Physics192,38(2025), Theorem1.5, Example2.2,
Lemma3.3 and proof of Corollary1.6:
https://link.springer.com/article/10.1007/s10955-025-03420-1 .
Their U(1) carpet construction converges in total variation on coarse links;
microscopic Wilson plaquettes have coupling m^2 beta_p, and each coarse
plaquette is divided into m^2 pieces. Here m is refinement, N is clock order.
The source states Wilson-loop monotonicity for U(1); the pinned finite-clock
and arbitrary-character extensions below are proved here, not attributed to
its corollary verbatim. Its Remark1.7 rules out assuming that log w_beta has
nonnegative Fourier coefficients. The carpet construction avoids that false
shortcut.

## 2. Elementary cosine inequalities on a torus

Let theta belong to T^d with Haar measure and density proportional to
exp H(theta), where H=sum_alpha t_alpha cos(C_alpha.theta), t_alpha>=0 and
C_alpha are integer vectors. For every integer A, <cos(A.theta)> >=0: expand
each exponential in characters and use the nonnegative coefficients of
exp(t cos u). Its zero Fourier coefficient normalizes the measure.

For integer A,B, the following second inequality holds:

 Cov(cos(A.theta),cos(B.theta)) >=0.                         (1)

To prove it, write the covariance as the double integral of
[cos(A.theta)-cos(A.theta')][cos(B.theta)-cos(B.theta')]/(2Z^2)
against exp[H(theta)+H(theta')]. The torus map
(u,v) -> (theta,theta')=(u+v,u-v) is a surjective integer homomorphism;
it pushes normalized Haar measure to normalized Haar measure, despite its
multiple sheets. It need not have a single-valued inverse. The difference
of each cosine is -2sin(A.u)sin(A.v), while the weight is

 exp[2 sum_alpha t_alpha cos(C_alpha.u)cos(C_alpha.v)].

Expanding this exponential gives nonnegative coefficients multiplying squares

 [integral sin(A.u)sin(B.u) product_alpha cos(C_alpha.u)^n_alpha du]^2.

Uniform absolute convergence on the compact torus justifies integration
term by term. This proves(1). Differentiation in any t_alpha therefore makes
every cosine expectation nondecreasing. The proof uses continuous torus Haar
measure; it does not perform an invalid division by2 on an even-order clock.

## 3. Pinning the coarse links and taking limits in the correct order

For finite h>=0 multiply the coarse U(1) measure by

 P_h(theta)=exp[h sum_(coarse edges e) cos(N theta_e)].

On a carpet graph its pullback by the coarse-edge product map pi_m is again
an exponential of positive cosines of integer forms in microscopic angles.
The pullback of any coarse character cos(J.theta) is a cosine of an integer
form as well. Section2 implies nonnegative expectation and monotonicity in
each microscopic Wilson coupling. If beta_p<=gamma_p, each microscopic
coupling m^2 beta_p<=m^2 gamma_p, with the same P_h.

For fixed h and a finite coarse complex, Theorem1.5 passes this comparison
to Villain weights: reweighting by a bounded strictly positive P_h preserves
convergence in total variation. One may see this directly from Lemma3.3:
integrating the interiors of the carpets leaves a product of the convolved
coarse plaquette weights, multiplied by P_h. Coarse-edge products of Haar
variables remain independent Haar variables. Different plaquettes may have
different couplings, as in the proof of Corollary1.6. Zero-coupling plaquettes
are constant1 and can be omitted or reached by continuity.

Next send h to infinity. The one-edge probability measure proportional to
exp[h cos(N theta)] dtheta converges weakly to uniform measure on the N roots
of unity. The finite product does too. Multiplication by the finite positive
continuous Villain weight and subsequent normalization preserve this weak
limit. Hence the limit is exactly the given finite-clock Villain law, with
no residual extra interaction. The comparison survives. For every integer
link vector J, its expectation phi(J)=<exp(i J.theta)> is real by global
inversion symmetry and obeys

 0 <= phi_beta(J) <= phi_gamma(J) <=1 if beta<=gamma.       (2)

The two-cosine covariance inequality(1) also survives, since products of
bounded continuous cosines converge in both limits. These are sequential
limits m->infinity at fixed h, followed by h->infinity. No uniform estimate
in h or interchange of these limits is claimed or needed.

### A useful direct comparison with the continuous-angle law

The same proof also makes each character expectation nondecreasing in h,
because h multiplies positive cosine interactions on the carpet. Starting
at h=0 and ending at the clock limit gives, on the SAME finite complex,

 phi_(U1,beta)(J) <= phi_(Z_N,beta)(J).                    (2a)

Thus the Haar Wilson lower bound in the pinned free-cubic source directly
implies the finite-clock lower bound for any chosen integer representative.
The periodized upper-curvature argument in the companion is a separate
analytic route to the same estimate, explicitly displaying the full
current-lattice alias minimization (which also follows by applying(2a) to
every equivalent current). Neither proof uses a continuous variance
inequality on the integer-current law.

If M is a multiple of N, first pin to the M roots and then increase a
second positive term h sum_e cos(N theta_e). The remaining maxima are exactly
the N roots; passing the limits sequentially gives phi_(Z_M)(J)<=phi_(Z_N)(J).
There is no such ordering for arbitrary numerical orders N<M: the character
q=N is identically1 for Z_N, whereas q=M is identically1 for Z_M. Divisibility,
not the sizes alone, is the comparison condition. These comparisons also
pass to their free-boundary states. When both long-time rates exist, they
order the corresponding visible static energies in the opposite direction.

## 4. A unique free-boundary limit, independent of exhaustion

Embed two finite complexes in a common larger cubic box. Missing plaquettes
have coupling0 and extra links have independent clock Haar measure. For J
supported on the original links, adding plaquettes increases phi(J) by(2).
Thus phi(J) has a limit along the directed set of all finite plaquette sets
and edges containing its support, bounded between0 and1. Every cofinal
increasing exhaustion has this same limit.

Finite-clock Fourier characters determine each finite-dimensional marginal:
probabilities follow from the finite inverse Fourier transform. Compactness
therefore gives one limiting free-boundary measure mu_free, without choosing
a subsequence. At homogeneous coupling it is translation invariant and has
the lattice symmetries, because translating an exhaustion is cofinal. Its
finite Gibbs conditional identities pass by positivity and finite range.

This proves uniqueness of the free-boundary limit, NOT uniqueness among all
Gibbs states, clustering, ergodicity, or absence of broken symmetry. It also
does not prove a Gaussian continuum law.

For fixed spatial box L, let the time interval grow in both directions
around a fixed observable. That limit exists by the same monotonicity. Now
let L grow. For each character the resulting iterated limit is its supremum
over all finite space-time boxes, hence equals mu_free. Cubes are another
cofinal exhaustion, so their previously established Wilson lower bound
applies in this same state. Thin-slab curvature estimates were never used.

## 5. Explicit transfer matrix and external charge sector

Fix a finite connected spatial box, with spatial links E_s and vertices V_s.
Use counting Haar inner product on H_L=ell2(Z_N^E_s). For link a write

 V(a)=product_(spatial plaquettes p) w_beta((d1 a)_p),
 C(a,a')=product_(spatial links e) w_beta(a_e-a'_e),
 T=V^(1/2) C V^(1/2).                                  (3)

Angles in these formulas are2pi a/N. The kernel C is convolution with a
strictly positive function. Its Fourier eigenvalues are strictly positive:
each one-link coefficient is proportional to
sum_(r congruent k mod N) exp[-r^2/(2beta)]>0. Therefore T is positive definite
and self-adjoint. It is also strictly positive entrywise. Its largest
eigenvalue lambda_0 is simple, with a positive normalized eigenvector Omega_0.

Spatial gauge translations a->a+d0 eta commute with both C and V. Uniqueness
and positivity of Omega_0 imply gauge invariance. Let gamma be an oriented
spatial path from x to y, and U_gamma(a)=exp[2pi i q gamma.a/N]. With the
convention (R_eta f)(a)=f(a+d0 eta), the vector U_gamma Omega_0 is in the
character sector rho=q d0*gamma=q(delta_y-delta_x), modulo N. Call the
restriction of T to this sector T_rho. It is positive definite and its norm
is at most lambda_0. Only the total-zero charge sectors used here are needed.

For completeness the finite-time boundary vector is b=V^(1/2). Temporal
links can be put in temporal gauge on an open interval: recursively translate
the spatial link variables to remove each temporal link. This is an exact
bijection of finite clock variables up to the initial gauge freedom and a
constant multiplicity. Every temporal plaquette then has difference a-a',
each spatial plaquette keeps V, and the closed rectangular Wilson character
becomes U_gamma(a_0) conjugate(U_gamma(a_T)). The partition function is
<b,T^M b>. The square-root split in(3) gives full V on every time slice,
including the endpoint factors supplied by b.

Put the loop endpoints far from both free temporal boundaries. Perron-Frobenius
convergence T^n b/lambda_0^n -> <Omega_0,b> Omega_0 gives exactly

 W_L(R,T)=<U_gamma Omega_0,(T_rho/lambda_0)^T
                                  U_gamma Omega_0>.       (4)

Global inversion makes the sign-reversed convention identical. The spectral
measure nu_(L,R) of the normalized vector U_gamma Omega_0 is a probability
measure on(0,1]. Equation(4) is its Tth moment. This is the external static
charge sector of the isotropic clock Villain transfer matrix; it is not the
separate N=3 penalty Hamiltonian and contains no dynamical matter field.

## 6. Spatial limit, spectral meaning, and energy bound

For each nonnegative integer T, Section4 gives
W_L(R,T)->W_free(R,T) as L grows around gamma. Probability measures on[0,1]
are compact, and moments determine a measure there: polynomials are uniformly
dense in continuous functions. Consequently nu_(L,R) converges weakly to a
unique probability measure nu_R on[0,1], and

 W_free(R,T)=integral_[0,1] lambda^T nu_R(dlambda).         (5)

This alone constructs a positive-contraction representation on L2(nu_R),
with multiplication by lambda and cyclic vector1. A possible atom at0 is an
infinite-energy component killed after one time step; no absence of such an
atom is inferred from weak convergence. On(0,1] the Hamiltonian is the
self-adjoint multiplication operator -log lambda.

Let lambda_*(R)=sup support(nu_R). The elementary moment argument gives
lim_(T->infinity) W_free(R,T)^(1/T)=lambda_*(R): the upper bound uses
lambda<=lambda_*, and the lower bound uses positive mass in every interval
(lambda_* -eta,lambda_*]. Applying the cubic Wilson lower bound and its
exact rectangle Green limit proves lambda_*>0 and

 E_visible(R):=-log lambda_*(R)
   =-lim_(T->infinity) log W_free(R,T)/T
   <= (beta^-1+epsilon) q_eff^2 [G3(0)-G3(R e1)],          (6)

with E_visible(R)>=0 and q_eff a smallest absolute representative of q mod N.
For q=0 mod N the observable is identically1, nu_R=delta_1 and E_visible=0.
For unit spatial separation,6[G3(0)-G3(e1)]=1 fixes the normalization.
Since0<=G3(R)<=G3(0)<infinity, the energy cost is uniformly bounded as the
test charges separate.

E_visible is the bottom of the spectral support reached by this path
insertion in the matched limiting transfer representation. It need not be
the bottom of every conceivable infinite-volume charged representation; nor
does weak convergence justify exchanging spatial limits with spectral
infima. Equation(6) bounds this specific physically defined static insertion
without making either claim. It does not give a Coulomb force equality,
propagating charged particles, a photon, or an axiom-selected law.

## 7. Completed author challenges and remaining review

The companion runner checks16 finite three-cube coupling cases, each with
six separate plaquette increases and4000 sampled arbitrary-character pairs.
Clock orders2,3,4,5 include even orders. Fourier probabilities give minimum
cosine covariance and monotonicity increments no lower than-1e-15, within
floating error. Four integrated-carpet and three finite-pinning cases approach
their separately evaluated limits. Twelve Haar/clock comparisons, two
subgroup comparisons and a nondivisibility control challenge(2a).

Five spatial-square transfer systems have dimensions16,16,81,81,256. They
compare explicit temporal-link sums with temporal gauge at three lengths and
four charge labels each. The maximum discrepancy is below1.9e-15. Direct
spectral sums agree within3.3e-15. Omitting the temporal charge phases or the
spatial endpoint weights changes the observable, as the controls verify.

Two initial convergence checks used approximations too coarse for their
stated tolerances; their frozen sources and failures are preserved. Increasing
carpet refinement64->128 and pinning128->512 resolves them without loosening
tolerances. A later nondivisibility control requested an arbitrary0.1 numerical
separation that was too large at beta0.6; its failure is preserved and a
beta0.15 control resolves the two opposite signs with large margins. This is
a fixture change, not a change to the divisibility theorem.

These low-dimensional finite probes do not certify the four-dimensional
source theorem, infinite limits, or spectral identification. The written
proof and its source dependencies remain subject to independent review.

