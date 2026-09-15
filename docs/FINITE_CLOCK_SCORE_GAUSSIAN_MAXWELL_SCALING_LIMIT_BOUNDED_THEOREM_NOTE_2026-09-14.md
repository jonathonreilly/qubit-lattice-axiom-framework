---
claim_id: finite_clock_score_gaussian_maxwell_scaling_limit_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "Conditional on the explicitly stated uniform all-affine integer-curl covariance input supplied in the same reviewed delta, bounded plaquette-score observables of isotropic four-dimensional finite-clock Villain models converge along beta,beta_d tending to infinity, lattice spacing tending to zero and physical torus side tending to infinity to the Gaussian Maxwell curvature distribution. All joint smeared moments converge; the explicit Gaussian OS quotient is a symmetric Fock space with two transverse modes of energy |p|. Clock order and couplings vary and the microscopic law is supplied. No fixed-N=3 phase, native law selection or axiom update is asserted."
upstream_dependencies:
  - periodic_finite_clock_villain_covariance_and_observable_masslessness_bounded_theorem_note_2026-09-14
runner: scripts/finite_clock_score_gaussian_maxwell_scaling_limit_2026_09_14.py
---

# Finite-clock scores converge to a Gaussian Maxwell curvature field

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

For the supplied varying-order finite-clock Villain family, the all-affine
integer-curl covariance input stated below implies joint-law convergence
of bounded physical score observables to a Gaussian Maxwell curvature
distribution, whose explicit positive-time quotient has two transverse
modes with energy |p|. This is a conditional model theorem. Independent
review of both its input and the new implication is pending.

The new ingredient beyond covariance convergence is an all-real-source
MGF squeeze. Conditional independence of the auxiliary lifts then removes
their noise without a volume loss, and cell-average smearing controls the
continuum normalization. Gaussianity is derived for the observables; it
is not assumed from their limiting two-point function.

## Status, inputs and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: periodic_finite_clock_villain_covariance_and_observable_masslessness_bounded_theorem_note_2026-09-14
target_blocker_text: "Upgrade the specified finite-clock massless observable sector to an actual Gaussian Maxwell scaling field, while retaining its supplied-law and varying-clock-order hypotheses."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the affine-curl input and the new all-source implication, then investigate charged observables and the fixed-alphabet Hamiltonian phase separately."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A conditional analytic joint-law and Gaussian reconstruction theorem for a supplied scaling family, with finite mathematical challenges."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The sole load-bearing repository dependency is
[the periodic finite-clock covariance source](PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md),
sections 2–8, at revision
`075a47fd49e98bb4c8f4b88ec149dcb78a52b5cd`, source SHA-256
`bfedf452ec4e5b4b19c7099cb4c5e7ebc69aca4198fbdfba1c8788647ddea237`.
Its full proof is carried in this PR's delta. It is provisional, not a
retained authority. The new implication is conditional on the precise
all-real-shift estimate stated in section 1; finite challenges here do
not independently establish that arbitrary-volume input.

| Input | Role | Provenance and status |
|---|---|---|
| Equal even four-tori, finite clock alphabets, isotropic Villain weights | Supplied probability models | Defined in section 1; no native identification |
| Uniform covariance bound on every affine integer-curl coset | Sole substantial mathematical premise | Linked source sections 3–8, provisional and included for joint review |
| Poisson summation and finite character duality | Finite-dimensional machinery | Normalizations and fiber multiplicities derived below, including composite N |
| Joint scaling of beta, beta_d, spacing and physical side | Explicit limit family | Defined in section 5, with a concrete integer sequence in section 6 |
| Bounded score observables and cell-average embedding | Supplied observable identification | Sections 4–5; no empirical normalization |

| Proof obligation | Status in this note | Consequence |
|---|---|---|
| Uniform all-affine curl and coexact covariance lower bound | Explicit provisional input, section 1 | Quantitative control at every real tilt |
| Exact positive lift and complementary covariance identity | Derived in section 2 | Full-rank lattice law and harmonic-aware variance control |
| Centered source maximum and integrated tilted curvature | Derived in section 3 | Gaussian joint laws for exact sources |
| Auxiliary-to-physical observable comparison | Derived in section 4 | Uniform l2 error with no volume factor |
| Cell-average projector convergence | Derived in section 5 | Continuum Maxwell covariance and harmonic removal |
| Distributional tightness and moment passage | Derived in section 6 | Actual Gaussian random-distribution limit |
| Electric–magnetic reflection kernel and dense quotient | Derived explicitly in section 7 | Two transverse modes and the full Gaussian Fock quotient |

The strongest unresolved proof validation is independent review of the
uniform affine input. The strongest unresolved physical identification
is the relation of this varying-clock-order family to a selected native
law and to the fixed N=3 interacting Hamiltonian. These are not renamed
as conclusions of the scaling theorem. No axiom or registered primitive
is introduced or altered.

## 1. Supplied model and explicit input

Let T_L=(Z/LZ)^4, L even and L>=4, with canonical positive orientations
and the ordinary sum inner product on cochains. Write d=d_1 from edges to
plaquettes and P_e,P_c,P_h for the exact, coexact and harmonic orthogonal
projections on real two-forms. The harmonic space has dimension six.

Clock link angles take values in 2pi Z/N modulo 2pi, for an arbitrary
integer N>=2. The probability law is proportional to

    product_p phi_beta((d theta)_p),
    phi_beta(u)=sum_(n in Z) exp[-n^2/(2 beta)] exp(i n u).

All couplings, the geometry, and this law are supplied. Define

    beta_d=N^2/(4pi^2 beta),
    beta_1=(107 log 3+log 4)/(4pi^2),
    a(sigma)=sigma/384-beta_1, q(sigma)=exp[-2pi^2 a(sigma)],
    S_k(q)=sum_(r>=1) r^k q^r,
    delta(sigma)=sigma[8503056 S_6(q)+262144 S_5(q)]/[a(sigma)e].

AFF: on every such torus, the Gaussian proportional to
exp[-||z||^2/(2 sigma)] on every real affine translate b+d Z^E has
covariance at least sigma(1-delta(sigma))P_e, for sigma>=2000. The same
statement holds for the integer coexact lattice under the integral dual
Hodge map. A component of b perpendicular to im(d) changes only the
normalizing constant. Delta tends to zero as sigma tends to infinity.

The affine mean need not vanish. There is no general affine covariance
upper bound by sigma I; such an assertion is false even in dimension one.

## 2. Exact positive lift, including composite clock orders

Poisson summation gives the strictly positive representation

    phi_beta(u)=sqrt(2pi beta)
                sum_(m in Z) exp[-beta(u-2pi m)^2/2].

Augment each clock configuration by these plaquette integers. Conditional
on all clock links, the integers on distinct plaquettes are independent.
Choose representatives theta=2pi a/N with a_e in {0,...,N-1}, and put

    y=d theta-2pi m, z=d a-N m,
    M_N=N Z^P+d Z^E, X=sqrt(beta)y=z/sqrt(beta_d).

For each z in M_N, the possible a are exactly the solutions of
d a=z modulo N. Their number is |ker(d mod N)|, independent of z; m is
then uniquely determined. Thus the marginal law of z is exactly the
centered Gaussian on M_N with variance parameter beta_d. The constant
fiber includes both gauge and flat-holonomy multiplicities. No arithmetic
step treats Z/NZ as a field.

Let L_N={n in Z^P:d^T n belongs to N Z^E}. Finite character annihilation,
or integer Smith normal form, gives

    L_N^*=Z^P+(1/N)d Z^E, M_N=N L_N^*.

Poisson summation with a real source gives

    Cov_(L_N,beta)/beta+Cov_(M_N,beta_d)/beta_d=I.       (2.1)

Conditioning M_N on cosets of d Z^E and using AFF yields a lower bound
(1-delta(beta_d))P_e for C_X=Cov(X). Conditioning L_N on cosets of its
integer coexact sublattice, and using the dual Hodge version of AFF and
(2.1), yields the upper bound

    (1-delta(beta_d))P_e <= C_X
       <= P_e+delta(beta)P_c+P_h,  and C_X<=I.          (2.2)

Total covariance includes the positive covariance of conditional means;
those means are not silently set to zero. The harmonic term remains.

## 3. A centered MGF upper bound and an all-source lower curvature bound

For a full-rank lattice M in finite-dimensional Euclidean space and
sigma>0, define Z_M(u)=sum_(z in M) exp[-||z-u||^2/(2 sigma)]. Poisson
summation expresses this as a positive constant times

    sum_(w in M*) exp[-2pi^2 sigma||w||^2] exp(2pi i w.u).

All Fourier coefficients are nonnegative. Pairing w and -w, or taking
real parts, proves Z_M(u)<=Z_M(0). Completing the square therefore gives,
for the centered lattice Gaussian X=z/sqrt(sigma),

    E exp(h.X)=exp(||h||^2/2) Z_M(sqrt(sigma)h)/Z_M(0)
              <= exp(||h||^2/2).                     (3.1)

This is an MGF bound at the centered measure; it is not an upper bound on
the Hessian of log Z at arbitrary affine shifts.

Now let X have the M_N law of section 2. Tilt by exp(r h.X) for any real
r. Conditional on a coset of d Z^E, completing the square merely changes
the real affine shift. AFF thus applies after every real tilt. Total
covariance implies, for F_h(r)=log E exp(r h.X),

    F_h''(r)>= (1-delta(beta_d))||P_e h||^2.           (3.2)

All derivatives and countable coset conditionings are justified by the
finite-dimensional Gaussian exponential moments. The untilted law is
even, hence F_h(0)=F_h'(0)=0. Integrating (3.2) and using (3.1), for an
exact source h=P_e h, gives

    exp((1-delta(beta_d))||h||^2/2)
        <= E exp(h.X) <= exp(||h||^2/2).             (3.3)

This lower bound holds for every real exact source, with no restriction
on its support or on the number of plaquettes.

For a triangular family of exact sources h_j with bounded norms, when
delta(beta_d,j)->0 and ||h_j||^2->v, (3.3) at every real scalar multiple
gives convergence of the moment generating functions to exp(v r^2/2).
The upper bound gives tightness and uniform exponential integrability.
Every weak subsequential limit has this MGF and is the centered Gaussian
of variance v; therefore the full sequence converges. Applying this to
all real linear combinations gives joint Gaussian convergence for any
finite family whose Gram matrices converge. Uniform exponential moments
also give convergence of all joint polynomial moments.

For a general source h, (2.2) and centering give

    E|((I-P_e)h).X|^2
        <= delta(beta)||P_c h||^2+||P_h h||^2.       (3.4)

Consequently the nonexact part vanishes in probability when the right
side tends to zero. Bounds (3.1) at positive and negative sources retain
uniform integrability of all moments for the full source. A covariance
limit alone would not establish Gaussianity; the all-source squeeze is
the additional ingredient.

## 4. Replace the auxiliary lift by a bounded physical clock observable

The real smooth odd score s_beta(u)=phi_beta'(u)/phi_beta(u) is bounded
on the circle for every finite beta. Define the actual clock observable

    Y_p=-s_beta((d theta)_p)/sqrt(beta)=E[X_p|theta].

The equality follows by differentiating the positive lift sum. In
particular Y is a function of the finite clock links alone. Conditional
independence of the plaquette lifts proves the exact identity

    E|h.(X-Y)|^2=sum_p h_p^2 E Var(X_p|theta).        (4.1)

Let v_p be the principal representative of (d theta)_p in [-pi,pi),
with that fixed endpoint convention. This is a function of theta. If
|y_p|<pi then v_p=y_p. Otherwise
|sqrt(beta)(y_p-v_p)|<=2|X_p|. The conditional mean minimizes the mean
squared prediction error, so

    E Var(X_p|theta)
       <=4 E[X_p^2 1_(|X_p|>=pi sqrt(beta))].        (4.2)

By (3.1) and Chernoff, Pr(|X_p|>=r)<=2 exp(-r^2/2). Integrating this
tail, E[X_p^2 1_(|X_p|>=r)]<=2(r^2+2)exp(-r^2/2). Hence

    E|h.(X-Y)|^2 <= epsilon(beta)||h||^2,
    epsilon(beta)=(8pi^2 beta+16)exp(-pi^2 beta/2).   (4.3)

The endpoint y=pi is included in the tail event. Jensen conditional on
theta also gives E exp(h.Y)<=E exp(h.X)<=exp(||h||^2/2).

The l2 norm in (4.3), rather than the square of an l1 norm, is essential:
it avoids a volume loss when taking a continuum limit. At N=2 the score
vanishes at every allowed plaquette angle; this is consistent with the
theorem because beta and beta_d cannot both diverge at fixed N.

## 5. Cell-average embedding and continuum geometric limit

Choose a_j->0, even L_j>=4, physical side ell_j=a_j L_j->infinity,
beta_j->infinity, and beta_d,j=N_j^2/(4pi^2 beta_j)->infinity. The last
two parameters eventually exceed 2000. There is no further rate relation
between these four limits in this result.

For each of the six plaquette orientations, use the side-a_j four-cubes
centered on that orientation's plaquette midpoints in a translated
fundamental box centered near the origin. These cells tile its box. Put

    F_j,mu,nu(x)=a_j^-2 Y_p on the corresponding cell,
    F_j,mu,nu(x)=0 outside that box.

This is a real random two-form distribution. For a real two-form test f,

    F_j(f)=sum_p (J_j f)_p Y_p,
    (J_j f)_p=a_j^-2 integral_(cell_p) f_mu,nu(x) dx.

Cauchy-Schwarz on each four-cell gives exactly

    ||J_j f||_l2 <= ||f||_L2.                        (5.1)

The adjoint J_j* makes a lattice vector piecewise constant with factor
a_j^-2. Thus J_j J_j*=I, while J_j*J_j is the cell-average projection
on the corresponding expanding boxes and converges strongly to I in L2.

For the Maxwell curvature projection P on L2(R^4;Lambda^2), its Fourier
symbol for p!=0, using mu<nu and rho<sigma, is

    P_(mu,nu;rho,sigma)(p)=
      [p_mu p_rho delta_(nu,sigma)-p_mu p_sigma delta_(nu,rho)
       -p_nu p_rho delta_(mu,sigma)+p_nu p_sigma delta_(mu,rho)]/|p|^2.

Its value at p=0 is immaterial for L2 functions. It is the orthogonal
projection d(-Delta)^-1 d*, of rank three at nonzero Euclidean momentum.
The geometric limits are

    <J_j f,P_e,L_j J_j g> -> <f,P g>,
    ||P_h,L_j J_j f|| -> 0.                         (5.2)

Here is an explicit proof controlling sampling. First take Schwartz f,g
with smooth compact Fourier support bounded away from zero. Periodize
them with period ell_j in each coordinate. Their difference from the
original fields on the fundamental boxes tends to zero in L2 by Schwartz
tail estimates. In the Fourier bases centered at edge and plaquette
midpoints, the coboundary symbol is exterior multiplication by i xi,
where xi_mu=2 sin(a_j p_mu/2). The midpoint phase removes the forward
difference phase exactly. The exact two-form projector is the displayed
formula with p replaced by xi.

For small enough a_j the fixed Fourier support has no aliases. Integration
over the centered four-cell adds the common factor

    sinc_j(p)=product_mu sin(a_j p_mu/2)/(a_j p_mu/2).

With Fourier transform fhat(p)=integral exp(-i p.x)f(x)dx and the unitary
finite-lattice Fourier transform, the cell source coefficient is
ell_j^-2 sinc_j(p) fhat(p). Hence the pairing in (5.2) is a Riemann sum
ell_j^-4 sum_p sinc_j(p)^2 fhat(p)* P(xi(p)) ghat(p), with momentum
spacing 2pi/ell_j. On the chosen compact support P(xi)->P(p) uniformly,
and this sum tends to (2pi)^-4 integral fhat*P ghat.

Such test functions are dense in L2. The contractions J_j, P_e and P
extend the first limit to all L2 tests. For integrable f, the harmonic
constant-mode projection satisfies

    ||P_h,L_j J_j f||^2
       <= ell_j^-4 sum_(mu<nu) (integral |f_mu,nu|)^2.

Density and the same contractions extend its vanishing to all L2 tests.
Using cell integrals avoids unjustified point-sampling bounds on L2.

## 6. Gaussian random-distribution convergence

For any finite family of real L2 two-form tests f_1,...,f_k, apply
(3.3) to P_e J_j f_i and (5.2) to their Gram matrices. Equations (3.4)
and (5.2) remove their coexact and harmonic parts; (4.3) and (5.1)
remove the auxiliary lift noise. Thus

    (F_j(f_1),...,F_j(f_k)) => centered Gaussian
    with covariance E F(f_i)F(f_l)=<f_i,P f_l>.       (6.1)

All joint polynomial moments converge. Indeed conditional Jensen and
(5.1) bound every real linear-combination MGF by its L2 Gaussian bound,
uniformly in j. This supplies uniform integrability for the moment
passage, independently of the L2 approximation steps.

The conclusion can be strengthened from finite-dimensional laws to
random distributions. For every real L2 test f,

    E|F_j(f)|^2<=||f||_L2^2.                        (6.2)

Fix a bounded box U and a smooth cutoff chi supported strictly within
U. Expand chi F_j in a Dirichlet Laplacian eigenbasis e_n of U. Equation
(6.2) gives E|F_j(chi e_n)|^2<=||chi||_infinity^2. In four dimensions,
sum_n(1+lambda_n)^-s is finite for s>2, so the expected squared local
H^-s norm is bounded uniformly in j. For 2<s<s', compact inclusion from
H^-s into H^-s' on a bounded box, followed by Markov's inequality and a
countable exhaustion with cutoffs, proves tightness in H^-s'_loc for
every s'>2. This argument uses the usual local Sobolev topology, so
boundary conventions for the auxiliary box do not change the conclusion.

The Gaussian F=P W, with W six-component real white noise, has covariance
P because P*=P=P^2. Its finite-dimensional laws are exactly (6.1) and
uniquely identify every distributional limit. Consequently the full
sequence F_j converges in law locally in H^-s for every s>2 to this
Gaussian Maxwell curvature field.

For a concrete supplied sequence, j>=2, one may take

    a_j=1/j, L_j=2j^2, beta_j=2000+j, N_j=8 beta_j.

Then ell_j=2j and beta_d,j=16 beta_j/pi^2. Every clock alphabet is finite,
and all required limits hold. The clock order grows with j. This is not
a continuum theorem for one fixed finite alphabet.

## 7. Explicit OS one-particle reconstruction: two transverse modes

Use time coordinate 0, E_i=F_(0,i), and
B_i=(1/2)epsilon_(i,j,k)F_(j,k), so B=(F_23,-F_13,F_12). Under time
reflection E is odd and B is even. At spatial momentum p!=0 put

    r=|p|, P_T=I-p p^T/r^2, C_p v=p cross v.

Then C_p^T=-C_p and C_p^2=-r^2 P_T. In the Euclidean Fourier covariance,
with time inversion convention exp(i p_0(t_x-t_y)), the blocks are

    S_BB=(r^2 I-p p^T)/(p_0^2+r^2),
    S_EE=(p_0^2 I+p p^T)/(p_0^2+r^2),
    S_EB=-p_0 C_p/(p_0^2+r^2),
    S_BE=+p_0 C_p/(p_0^2+r^2).

For reflected first time -s and second time t, s,t>0, the constant I
piece in S_EE is a contact distribution at s+t=0 and contributes zero.
Using

    integral dp_0/(2pi) exp[-i p_0 u]/(p_0^2+r^2)=exp(-r u)/(2r),
    integral dp_0/(2pi) exp[-i p_0 u]p_0/(p_0^2+r^2)=-i exp(-r u)/2,

and the odd E reflection sign, the reflected kernel in (E,B) order is

    K_p(s,t)=(r/2)exp[-r(s+t)]
              [[P_T,-i C_p/r],[-i C_p/r,P_T]].       (7.1)

The matrix M=-i C_p/r is Hermitian and M^2=P_T. The block matrix is the
Gram matrix of the map (f_E,f_B) -> P_T f_E+M f_B. It is positive and
has rank exactly two. This checks the electric and magnetic sectors
together; the rank-three Euclidean exact projector is not the physical
polarization count.

After the positive-time Laplace transform, the one-particle norm is the
norm of P_T f_E+M f_B with measure (r/2)d^3p/(2pi)^3. These images are
dense in the transverse two-dimensional fibers: choose a nonnegative,
nonzero smooth positive-time test g whose Laplace transform is strictly
positive for r>0, and divide by that transform on any compact momentum
set separated from zero. Such compact transverse functions are dense.

Time translation by u>=0 multiplies the image by exp(-u|p|); spatial
translations multiply it by exp(i p.x). Thus the reconstructed
one-particle Hamiltonian is H_1(p)=|p|, with exactly two transverse
polarizations. The point p=0 has measure zero and supplies no extra
normalizable zero mode. Gaussian Wick moments give the corresponding
symmetric Fock reconstruction.

More explicitly, the Wick exponentials
:exp(F(f)):=exp(F(f)-<f,P f>/2) for real positive-time tests satisfy

    < :exp(F(theta f)): :exp(F(g)): >
         =exp(C(theta f,g))=exp(<J_OS f,J_OS g>).

Here theta includes the two-form reflection signs, C is the Gaussian
bilinear covariance, and J_OS is the Laplace/transverse map just derived.
This is exactly the inner product of symmetric Fock exponential vectors.
Differentiation yields the Wick-polynomial isometry, including all
particle sectors. Wick polynomials are dense in the Gaussian L2 space;
the dense range of J_OS proves that the completed positive-time quotient
is the symmetric Fock space over the stated one-particle space. The
semigroup is its second quantization and the Hamiltonian is dGamma(|p|).
This explicit Gaussian construction does not invoke a general interacting
OS reconstruction theorem with unchecked growth hypotheses.

Reflection positivity of the limiting Gaussian also follows directly
from (7.1) and the Gaussian Gram construction; no interchange of a
finite-clock transfer logarithm and a continuum limit is assumed. The
unit speed is set by the supplied isotropic coordinate normalization,
not an absolute physical constant derived from the framework.

The Euclidean random field obeys dF=0 distributionally. One must not
claim d*F=0 as an identity of Euclidean random distributions: the
Euclidean Maxwell equations have Schwinger contact terms. The transverse
massless OS sector is the stated on-shell conclusion.

## 8. Scope and remaining leverage

Conditional on AFF, the new result concerns full joint laws and a random
distribution limit of actual bounded physical finite-clock observables,
with explicit linear dispersion and two transverse reconstructed modes.
It does not follow merely from gaplessness or covariance convergence.

The finite-clock law and scaling sequence remain supplied. Nothing here
chooses a native formation law, derives Born probabilities, fixes a
finite N=3 Coulomb phase, identifies its continuous-time penalty
Hamiltonian, proves a charged particle spectrum, or supplies interacting
matter, gravity, or empirical normalization. Those are distinct open
obligations; this successful scaling construction does not force an
axiom update.


## 9. Finite mathematical challenges

The primary runner is
`scripts/finite_clock_score_gaussian_maxwell_scaling_limit_2026_09_14.py`.
It reads no external or repository scientific input and has no helper
runners. Its elementary formulas and its own finite configurations are
the executable domain. All lattice sums use explicit finite cutoffs;
their floating-point agreement is a challenge to identities, not a
certification of infinite sums or an arbitrary-volume phase proof.

| Family | Independent comparison and actual finite domain |
|---|---|
| Positive lift, score and duality | Three-face cycle-incidence toy at N=2,4,6: explicit clock fibers, positive image sums, an independent Fourier score and primal/dual lattice moment enumerations |
| Centered theta and affine shift | Nonorthogonal rank-two lattice with 25 seeded real sources; a shifted odd-integer lattice with variance 1 at Gaussian parameter 0.05 |
| Gaussian approach and covariance control | Five explicit three-face exact-plane lattice examples; a Rademacher variable with variance 1 and fourth moment 1 preserves the non-Gaussian alternative |
| Real tilt and coset mixing | Direct global moments, conditional moments and finite differences of source derivatives at three nonzero tilts; conditional means are retained |
| Midpoint Fourier geometry | Even side-six four-torus mode, direct cell quadrature, finite Fourier transform and independently constructed differential symbol; four refinement steps |
| Electric–magnetic OS kernel | Full six-component projector versus block formulas, independent oscillatory integrals, reflected Gram factorization and three spatial momenta |
| Bianchi identity and contacts | Exterior-algebra composition versus polynomial divergence covariance; a shared-noise example distinguishes conditional independence |
| Tail and parameter constants | Numerical tail integrals versus the analytic bound, three affine-input delta values and four members of the explicit scaling family |

For example, the three-face moment enumeration gives covariance duality
errors below 4e-15 for its stated parameters. The five exact-plane
examples have log MGF values approaching 0.32, with the final discrepancy
below 5e-7 and fourth moment approximately 3.00013234. These are toy
checks, not samples of the four-dimensional scaling limit. The reflected
six-by-six Gram matrix has eigenvalues 0,0,0,0,2,2 to rounding in each
checked momentum. Its rank follows analytically from section 7.

## 10. No-Go Discipline Gate

The following gate scopes the conditional theorem and the finite
counterexamples. It asserts no exhaustion of routes to a theory of
everything and no contradiction of the framework axioms.

### N1 — Materially distinct attempted failures of the implication

| Honesty | Object and attempted failure | Disposition and authority |
|---|---|---|
| ATTEMPTED | Probability law: retain the limiting covariance but choose a non-Gaussian joint law | The Rademacher witness in section 9 has the same variance and a different fourth moment. Section 3 supplies the extra all-real-source squeeze needed for the stated model. |
| ATTEMPTED | Conditional measure: use nonzero affine means to spoil source curvature or accumulate auxiliary noise coherently | Sections 2–4 retain total covariance after every real tilt and derive independent conditional plaquette noise. The three-face tilt enumeration and shared-noise witness check these exact distinctions. |
| ATTEMPTED | Topology and limiting geometry: retain a norm-one harmonic mode or a sampling alias | Section 5 keeps the harmonic term until its smeared norm vanishes and uses cell integrals with a dense Fourier proof. A constant normalized source retains harmonic norm one and is outside the vanishing-harmonic source hypothesis. |
| ATTEMPTED | Spectral reconstruction: count three Euclidean exact components or four uncoupled electric/magnetic components as physical photons | Section 7 includes the reflection sign, cross blocks and contact subtraction. Its explicit Gram factorization has rank two, independently checked by oscillatory integrals and eigenvalues. |
| ATTEMPTED | Scaling contract: keep the clock order fixed while sending both electric and dual variances to infinity | Section 1 has beta beta_d=N^2/(4pi^2), so the stated limit necessarily varies N. The physical N=2 score is identically zero, and the displayed integer sequence respects all growing-parameter requirements. |

These attempts differ in the joint probability law, conditional measure,
cohomology and continuum geometry, Hilbert-space reconstruction, or
parameter contract. Their disposition is the written derivation and
finite witnesses in this source, subject to review. None is claimed
ruled out by prior retained authority, and the list is not exhaustive.

### N2 — Dependency and independence accounting

There is one substantial mathematical premise: the uniform all-affine
integer-curl estimate, including its dual Hodge version. The latter is
not counted as an independent wall; it follows from the same estimate
and the integral Hodge identification in the linked source. The model
law, four scaling limits and observable choice are definition-level
hypotheses, not an asserted independent-wall set.

| Pair of outstanding questions | Implication established here | Treatment |
|---|---|---|
| Validation of the affine input / selected native-law identification | Neither implication is established | Keep both open; independence is unknown, not asserted |
| Fixed N=3 Hamiltonian phase / selected native-law identification | Neither implication is established | Keep both open; neither is a premise of the varying-N theorem |
| Validation of the affine input / fixed N=3 Hamiltonian phase | Neither implication is established | Do not transfer this proof or its conservative parameter region to that Hamiltonian |

No headline claims a number of independent framework walls. The new
conditional implication is useful even while those physical questions
remain open; it does not collapse them by terminology.

### N3 — Hidden-condition scan

The full mathematical contract is explicit: dimension four; equal even
periodic side L>=4; canonical positive cell orientations; real sources;
the supplied Villain weights; arbitrary finite integer N at each step;
the all-real-affine covariance input; beta,beta_d tending to infinity;
spacing tending to zero and physical side tending to infinity; cell
averages of L2 tests; and strict positive-time support in the reflection
calculation. The Gaussian upper MGF bound is used only at the centered
law. Tilted lower curvature uses all affine cosets. The cutoff boxes in
the Sobolev argument are auxiliary and local. Gaussian Fock
reconstruction is given explicitly through Wick exponentials; no
general interacting reconstruction theorem, transfer-log locality,
phase uniqueness or native probability rule is silently assumed.

### N4 — Exact residual matching

| Source or witness | Residual addressed | Matching claim and disposition |
|---|---|---|
| Linked covariance source, sections 3–8, pinned revision and hash above | Uniform affine-curl covariance at all shifts and its dual application | Exact model and topology match; explicitly provisional mathematical premise |
| This source sections 2–4 and the primary clock/tilt families | Positive lift normalization, conditional means and physical score noise | Exact algebraic mechanism; finite toy domain is disclosed |
| This source sections 5–7 and the primary Fourier/OS families | Continuum projector and positive-time polarization quotient | Matching normalization and sign convention; arbitrary limits are derived in prose |
| Rademacher, shifted lattice and shared-noise witnesses in section 9 | Missing Gaussianity, false shifted upper bound, or missing conditional independence | Matching narrow inference controls, never witnesses against the supplied model or axioms |

No witness from a different microscopic Hamiltonian is used to infer
that Hamiltonian's phase. No external field-theory phase theorem is
imported. The prior source's complete proof remains in this reviewed
delta rather than being replaced by a bare unreviewed conclusion.

### N5 — Resolution and rhetoric

At per-element resolution the runner checks scalar lifts, sources and
tails. At per-site resolution it checks a disclosed three-face incidence
toy. At per-mode resolution it checks symbols, reflections and rank. At
per-block resolution it checks the named finite clock, lattice and
Fourier blocks. At lattice-wide resolution the scaling and tightness
statements are analytic consequences conditional on the uniform input;
they are checked and not executed. The five substantive resolution lines
in the canonical runner cache state this distinction. Finite agreement
is never used as evidence of a universal theorem or an axiom obstruction.

### N6 — Partial closure and primitive boundary

The successful partial result is a complete conditional field-scaling
construction for a supplied family. It permits further work on charged
observables, alternative fixed-alphabet limits, or identification of the
underlying law. The parameters and isotropic coordinate units remain
supplied. This note makes no primitive-absence claim and requests no
new axiom. No premise registry, approved primitive or framework text is
edited, and no convention is promoted into physical selection.

### N7 — Steelman

A hostile reviewer should challenge the all-affine input before accepting
anything downstream: finite coset checks do not establish a uniform
bound in growing four-tori. Even if that proof is correct, a growing
clock alphabet at weak coupling can yield a free field while the
fixed-alphabet interacting Hamiltonian has an entirely different phase.
The concrete obligations are independent review of the linked affine
estimate and, for the broader target, a separate uniform actual-state
estimate for the selected microscopic law. This objection defeats any
claim that the present scaling limit solves the native TOE target. The
paper instead states the precise conditional construction it establishes.

### N8 — Cross-cycle comparison

The same-delta periodic covariance source, sections 10–11, established a
proposed gapless bounded-score sector and expressly stopped before
Gaussian scaling or dispersion. This source supplies that further
implication under a varying-parameter limit; it does not retroactively
claim dispersion at its predecessor's fixed sufficient parameters.

The current-main source
`FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE_BOUNDED_NOTE_2026-05-30.md`,
sections 0–2 and 4–5, works inside an already supplied free fermionic
Gaussian/quasi-free category. Its covariance-to-moments mechanism is
Wick rigidity under that input. Here Gaussianity is initially absent
and is obtained through the all-source squeeze before using Wick
reconstruction. That earlier source neither proves nor rules out the
present implication. This is a source-scope comparison at main revision
`5deabeb698a27c2c3f68c5df685af2521ef15307`, not an audit-status claim or
an additional load-bearing dependency.

## 11. Author review and falsifiers

The full new source and runner were reviewed personally. Twenty-six
targeted in-memory faults were detected: clock orientation; dual
temperature; lift fiber; score sign; l1 noise accumulation; omitted
conditional variance; dual covariance sign; completed-square source
scale; removed affine shift; Gaussian source scale; omitted between-coset
covariance; tilted source sign; exterior orientation; projector
normalization; midpoint phase; cell-average factor; cell field scale;
magnetic orientation; electric reflection sign; cross-residue sign;
omitted electric–magnetic cross blocks; electric noncontact sign;
quadratic dispersion; discarded Euclidean contact covariance; tail
factor; and halved supplied clock order. The frozen primary source was
not modified by these injections.

The first tilted-sign challenge was invisible to a variance-only check
because the centered law is even and its Hessian is even in the tilt.
An independent finite-difference first derivative now checks the tilted
mean as well, and detects the fault. Direct cell quadrature separately
checks the sinc factor instead of reusing it on both comparison sides.
These are author-check improvements, not independent-review results.

The theorem is falsified by failure of its stated affine input, an
incorrect lift fiber or dual temperature, loss of the uniform real-source
squeeze, a volume factor in the conditional score error, failure of the
cell-average projection limit or tightness, or an incorrect reflected
Gram factorization. The finite challenges address accessible identities
and distinctions; the quantified analytic steps require proof review.

Run the primary executable through `scripts/runner_cache.py` with its
declared 180-second timeout. There are eight finite families. Mechanical
cache and source readiness is not an audit verdict. Integrated pipeline,
strict lint and exact combined-tree evidence gates remain required
before landing; formal retained status belongs to the independent audit
path. No main merge or audit verdict is performed by this author packet.
