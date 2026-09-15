# Coupled-defect source probe

Personal derivation/search checkpoint,2026-09-15. This is an incomplete
stretch attempt toward fixed-clock full-flux Gaussianity, not a theorem PR,
independent review, or axiom amendment. The controlling campaign deadline
remains2026-09-15 13:30:44UTC. No delegated workers are used.

## Target and inputs

The new obligation is a source-compatible control of BOTH quantized defect
species at fixed beta and N. Covariance bounds, a positive current marginal,
and a convex extension of its integer weights already exist as proposals.
Rewriting those conclusions is not a new phase mechanism.

Source revisions inspected:

- PR8127,5112b9e6ff7e77b0140d4fbcbaa68c6560525978: periodic covariance note,
  especially its finite positive current ensembles, original versus damped
  external phases, and affine integer-curl theta.
- PR8133,f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8: exact coupled electric/
  magnetic representation; free-cubic filling and source extension;
  quantized-current Poisson identity. These are unreviewed inputs.
- PR8136,8a5ace1afc3b41999e2296d0067a325294fb2c6e: exact electric smoothing
  and filtering, which retains the quantized magnetic carrier.

The supplied Villain law and its parameter range are not consequences of
the native Lattice/Qubit/Admissibility/Record axioms. No primitive or physical
coupling is selected here.

## 1. Positive auxiliary factors need not be conditional moment functions

Consider the entire function

    M(t)=exp(t^2/2) [1+z cos(c t)]/(1+z),
    z=1/64, c=4.

For real t it is positive, even and normalized at0. It is bounded between
(63/65)exp(t^2/2) and exp(t^2/2). Moreover

    (log M)''=1-c^2 z[cos(c t)+z]/[1+z cos(c t)]^2
              >=1-c^2 z/(1-z)=47/63>0.

Nevertheless M is NOT the moment generating function of a probability law.
If it were, its finiteness at every real argument would identify its entire
continuation with that law's complex moment function. At the imaginary
argument4i,

    M(4i)=[64 exp(-8)+exp(-8)cosh(16)]/65
           > exp(8)/130 > 297/130 > 1.

The last estimate follows from the exponential series through degree4.
A probability characteristic function has modulus at most1.

An independent inverse-transform calculation identifies the signed density

    (2pi)^(-1/2) exp(-x^2/2)
       [1+z exp(c^2/2)cos(c x)]/(1+z).

Its bilateral Laplace transform is M. It is negative at x=pi/4 because
z exp(8)>1. This control also shows why strong real log-convexity and a
near-Gaussian real envelope are insufficient tests of moment positivity.

This is an abstract source-function counterexample. It is NOT a clock
countermodel and does not refute the positivity or the exact identities of
the complete clock law. In particular, a finite positive oscillator
decomposition of a partition function must not be called a decomposition
into physical conditional laws without a separate moment-positivity proof.

## 2. Exact finite Gaussian contour identity keeps the source mismatch

Let C be a positive definite covariance on a finite real space, let r_i and
r'_i be real row vectors, and let0<=z_i<1. Define

    P(a)=E_gamma_C product_i [1+z_i cos(r'_i A+r_i a)],
    mu(dA)=P(0)^(-1) product_i[1+z_i cos(r'_i A)] gamma_C(dA).

The measure mu is positive. For every real vector v, direct Gaussian
completion/contour translation gives the exact identity

    exp(-v.Cv/2) P(-i Cv)/P(0)
      = E_mu exp(-i v.A)
          product_i {1+z_i cos[r'_i A-i(r_i-r'_i)Cv]
                     \over 1+z_i cos(r'_i A)}.                 (2.1)

For a finite product the integrand is entire and is a finite sum of Gaussian
Fourier integrals. Thus (2.1) can alternatively be proved by expanding the
product; no infinite contour interchange is needed. The Gaussian shift is
A=A'+iCv. Its density contributes exp(v.Cv/2-i v.A'), fixing both signs.

The ratio in(2.1) can be dropped only when its effect is proved negligible.
The positive measure mu by itself is not the original source law.

For the periodic integer-curl ensemble of PR8127, restrict to range Q,
where C=beta V and V=Q^+. Its damped frequency satisfies

    r_i-r'_i=Q u_i,
    v=d*h/sqrt(beta),
    (r_i-r'_i)Cv=sqrt(beta) u_i.d*h.                         (2.2)

The physical Fourier source therefore leaves a discrete-derivative
correction. This is a potentially useful source mechanism. It does not
yet control the full coupled clock law, an arbitrary affine background,
or the distribution of ensemble-dependent means and covariances.

For a fixed finite ensemble, putting eta_i=(r_i-r'_i)Cv, the linear term of
the logarithm of the ratio is

    i sum_i eta_i z_i sin(r'_i A)/(1+z_i cos(r'_i A)).        (2.3)

At zero real source mu is even and the expectation of this term is zero.
At a nonzero affine source this cancellation generally fails. Any use of
Brascamp-Lieb to bound its variance requires a uniform Hessian bound for
the actual continuous auxiliary measure and the full local filling/packing
estimates. A bound for a fixed coset does not control the remaining mixture.
Those all-volume estimates have not been proved in this block.

## 3. A positive mixed representation still has an integer carrier

The PR8133 magnetic cluster construction supplies, at its stated smallness,
a positive function exp V(phi,f) with the joint bound

    |D^2V[(h,g),(h,g)]|<=epsilon ||d_2* h+g||^2.

Before integrating phi, the exact positive electric-current marginal can
be represented by the joint weight

    gamma_{beta(H_3^-1-cI)}(dphi)
    exp[-N^2<a,H_1^-1 a>/(2beta)]
    exp V(phi, N d_1 H_1^-1 a),
    a in ker d_0* intersect Z^edges.                         (3.1)

The exact and coexact source directions are orthogonal:

    <d_2* h,d_1 H_1^-1 b>=0.

Consequently the existing joint derivative estimate gives a small
quadratic-form perturbation of the continuous Gaussian extension in both
variables. This is a restatement of that input's source geometry, not a
new phase result. The variable a in(3.1) is still an integer conserved
current. Applying the continuous preconditioned Langevin theorem to it
would change its measure. Conditional on phi its weights need not be even
in a; pairing phi with -phi does not prove pointwise positivity of a
second Fourier-transformed integrand.

## 4. Route audit and concrete residuals

| Mechanism considered | Actual progress | Remaining condition |
|---|---|---|
| Treat positive damped ensembles as physical conditional probabilities | Abstract entire-function control rejects that inference; exact contour formula retains the missing source factor | Establish moment positivity or prove the factor negligible for the actual coupled source |
| Continuous convexity of the exact electric marginal | Its integer values and constructed extension remain useful | Current quantization cannot be removed by continuous Langevin dynamics |
| Conditional integer-curl Gaussianity | The derivative source term in(2.2) is explicit | Ensemble/affine means and covariance concentration remain part of the full target |
| Add Gaussian derivative noise in both Hodge sectors | It can remove finite-volume singular support, but the resulting dual theta is not shown to be a small potential | Prove a uniform curvature/locality estimate for the actual smoothed law; no such estimate is asserted |
| Import scalar dipole-gas or Villain spin-wave Gaussianity | Primary papers provide concrete RG/convexity machinery | Match the actual two-species gauge carrier and source before importing a theorem |

No axiom update, general no-go, or complete exhaustion of these families is
claimed. This checkpoint preserves a worked source diagnostic and an exact
finite identity. The current analytic target remains a coupled-source
multiscale estimate or an equivalent new positive representation with its
integer/source obligations actually resolved.

## Reading scope

Shen,arXiv1311.2305v2: opening through Proposition1, Theorem7/context,
field/polymer norms and selected Taylor-remainder lemmas were inspected.
No continuous full-paper read or scalar-to-gauge theorem import is claimed.

Dario-Wu, https://www.math.ens.psl.eu/~dario/Villain3D__short_version_.pdf,
March27,2023,136pages: opening through lines430, including Theorem1 and
the initial proof strategy. This states precise two-point asymptotics for
the continuous-symmetry Villain rotator model. Its expectation of further
gauge extensions is not such a theorem. Later sections are not yet read.

General web searches also returned quantum-link/quantum-spin-ice model
papers and reviews. Search snippets have not been used as phase proofs.
